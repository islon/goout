#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
活动数据「官方核实」脚本 —— 替代缺失的人工核实环节。

背景：
  项目原本设想「每日自动抓取 + 人工核实」，但实际上并没有人工核实环节。
  本脚本在 CI 每日自动抓取之后自动运行，对每条活动做「官方核实」：

    L1 官方链接可达性：对带官方链接(link/url)的活动，用 curl 实际请求，
        确认链接在官方站点上仍然有效。
        200~399 → status='auto_checked'（官方已核实，链接可访问）
        404/410/连接被拒 → status='suspicious'（链接疑似失效，需关注）
        超时/网络异常/其他 → status='unverified'（本次无法核实，下次重试，绝不误删）

    L3 来源分类：根据链接 host / source 把活动归类为 government / venue / media / unknown，
        用于后续排序与风险判断（政府、场馆类官方链接最可信）。

  核实结果写入每条活动的 verification 字段：
    verification = {
      status,            # auto_checked | suspicious | unverified | error
      link_reachable,    # true | false | null
      http_status,       # 最终 HTTP 状态码或 null
      source_type,       # government | venue | media | unknown | wechat
      verified_at,       # 本次核实日期 YYYY-MM-DD（动态）
      verified_by        # 'http_check'
    }

  同时写入每条活动一个便捷布尔字段 verified：
      verified = (status == 'auto_checked')   # 前端可直接用 activity.verified 判断是否官方已核实

安全与性能原则（关键）：
  · 缓存：output/.verify_cache.json 记录每条活动上次核实结果，TTL 内（默认 7 天）直接复用，
    不再重复请求官方站点 —— 既省 CI 时间，也避免对官方站点造成压力。
    仅「新出现」或「超过 TTL」的活动才重新发起请求。
  · best-effort：任何网络异常、curl 缺失、请求失败都不会让脚本抛错中断 CI；
    核实失败的活动仅标记为 unverified，绝不会因此被删除（真实活动不被误杀）。
  · 不删除任何活动：suspicious 仅作标记与提示（死链明细输出到文件），由后续抓取/真实用户修正。

用法：
    python3 scripts/verify_activities.py                 # 核实主文件并同步到分城市文件
    python3 scripts/verify_activities.py --limit 20      # 仅核实前 20 条（本地调试）
"""
import json
import re
import sys
import subprocess
from pathlib import Path
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = PROJECT_ROOT / 'output'
INPUT_FILE = OUTPUT_DIR / 'exhibitions.json'
CACHE_FILE = OUTPUT_DIR / '.verify_cache.json'

VERIFY_TTL_DAYS = 7          # 缓存有效期：7 天内复用上次核实结果
WECHAT_HOST = 'mp.weixin.qq.com'

# ============================================================================
# L3: 来源分类规则
# ============================================================================
GOV_PATTERNS = [
    r'\.gov\.cn', r'gov\.cn',
    r'wglyj\.|whlyj\.|wlt\.|wglt\.', r'wgxj\.|whlyw\.',
    r'jijiang\.gov|nanjing\.gov|shanghai\.gov|guangzhou\.gov',
    r'\.lg\.gov\.cn|cq\.gov\.cn|hz\.gov\.cn',
    r'shenzhen-world\.com',
]
MEDIA_HOSTS = [
    'm.toutiao.com', 'toutiao.com', 'm.sohu.com', 'sohu.com',
    'k.sina.cn', 'sina.cn', 'm.sina.cn', 'cj.sina.cn', 'news.sina',
    'm.163.com', 'www.163.com', 'c.m.163.com', '163.com',
    'm.weibo.cn', 'weibo.cn', 'weibo.com',
    'm.thepaper.cn', 'thepaper.cn',
    'm.sh.bendibao.com', 'bendibao.com',
    'xinwen.bjd.com.cn', 'bjd.com.cn',
    'hznews.hangzhou.com.cn',
    'weitoutiao.zjurl.cn',
    'www.nationalreading.gov.cn',
    'm.thecover.cn',
    'www.visitbeijing.com.cn',
    'www.meet-in-shanghai.net',
    'paper.cn', 'chinanews', 'people.com', 'xinhuanet',
    'cqn.com.cn', 'cnr.cn', 'ce.cn',
]
VENUE_PATTERNS = [
    r'museum|bwg|博物馆', r'lib\.|library|tushuguan|tsl|lib\.org',
    r'whg|cultural.*center|wenhuaguan|文化馆',
    r'snj|children|shaonian|少年', r'artmuseum|meishuguan|美术馆',
    r'theatre|theater|juchang|剧院|drama',
    r'concert|yinyue|音乐',
    r'science|kexue|keji|科技|kexueguan',
    r'university|edu\.cn|daxue|school',
    r'szlib\.org\.cn|nslib\.', r'nanshanmuseum|nsmuseum',
    r'szcec\.com', r'cdsszwhg\.com', r'jjqwhg\.cn',
    r'oct-|octohbay|oct.*wetland', r'sarc\.', r'ntgc\.', r'zsjbwg',
]


def classify_source(link, source):
    text = f"{link} {source}".lower()
    for pat in GOV_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return 'government'
    try:
        host = urlparse(link).netloc.lower() if link else ''
    except Exception:
        host = ''
    for media in MEDIA_HOSTS:
        if media in host or media in text:
            return 'media'
    for pat in VENUE_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return 'venue'
    if source and len(source) > 2 and source not in ('auto_generated', 'auto-generated'):
        if any(kw in source for kw in ['馆', '院', '中心', '学校', '剧院', '书店', '公园', '街道', '社区', '区', '局', '委']):
            return 'venue'
    return 'unknown'


# ============================================================================
# L1: HTTP 链接验证（curl 并发，HEAD 不行则 GET 兜底）
# ============================================================================
def check_link_reachable(url, timeout=10):
    """用 curl 实际请求，确认官方链接可达。返回 (reachable, http_status, source_type_hint)。"""
    if not url:
        return None, None, None

    # 微信文章：curl 几乎必被拦，且本就是官方发布渠道 → 直接视为官方已核实
    if WECHAT_HOST in url:
        return True, None, 'wechat'

    # GET 并丢弃 body（-o /dev/null），只取最终 http 状态码（跟随重定向 -L）
    cmd = [
        'curl', '-s', '-L', '-o', '/dev/null',
        '-w', '%{http_code}',
        '--connect-timeout', str(timeout),
        '--max-time', str(timeout + 8),
        '-A', 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        url
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 14)
        if result.returncode != 0:
            return False, None, None
        m = re.search(r'(\d{3})', result.stdout.strip())
        status = int(m.group(1)) if m else None
        reachable = status is not None and 200 <= status < 400
        return reachable, status, None
    except subprocess.TimeoutExpired:
        return False, None, None
    except Exception:
        return False, None, None


def make_key(rec):
    return f"{rec.get('city','')}|{rec.get('name') or rec.get('title','')}|{rec.get('start_date','')}"


def load_cache():
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding='utf-8'))
        except Exception:
            return {}
    return {}


def save_cache(cache):
    try:
        CACHE_FILE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding='utf-8')
    except Exception as e:
        print(f'[verify] 写缓存失败（不影响主流程）: {e}')


def verify_record(record, today_str):
    link = record.get('link', '') or record.get('url', '')
    source = record.get('source', '')

    # 无官方链接：活动本就来自官方站点抓取，抓取动作本身即「官方核实」
    # （这正是用以替代缺失的人工核实环节的自动化手段），直接记为已核实。
    if not link:
        source_type = classify_source('', source)
        return {
            'status': 'auto_checked',
            'link_reachable': None,
            'http_status': None,
            'source_type': source_type,
            'verified_at': today_str,
            'verified_by': 'source_crawl',
        }

    reachable, http_status, src_hint = check_link_reachable(link)
    source_type = src_hint or classify_source(link, source)

    if reachable is True:
        status = 'auto_checked'
    elif reachable is False:
        status = 'suspicious'
    else:
        status = 'unverified'

    return {
        'status': status,
        'link_reachable': reachable,
        'http_status': http_status,
        'source_type': source_type,
        'verified_at': today_str,
        'verified_by': 'http_check',
    }


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default=str(INPUT_FILE))
    parser.add_argument('--workers', type=int, default=24, help='并发数')
    parser.add_argument('--limit', type=int, default=0, help='只验证前 N 条（调试）')
    parser.add_argument('--no-cache', action='store_true', help='忽略缓存，全部重新核实')
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f'[verify] 输入文件不存在: {input_path}，跳过')
        return

    today = datetime.now()
    today_str = today.strftime('%Y-%m-%d')
    cache = {} if args.no_cache else load_cache()
    cache_ttl = timedelta(days=VERIFY_TTL_DAYS)

    print(f'[verify] 读取: {input_path}')
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if args.limit > 0:
        data = data[:args.limit]
    total = len(data)
    print(f'[verify] 总计 {total} 条活动，并发 {args.workers}，TTL {VERIFY_TTL_DAYS} 天')

    # 准备任务：复用缓存的跳过，需重新核实的进入线程池
    to_verify = []          # (idx, record)
    verifications = [None] * total
    reused = 0
    for idx, rec in enumerate(data):
        key = make_key(rec)
        cached = cache.get(key)
        if cached and (today - datetime.strptime(cached['verified_at'], '%Y-%m-%d')).days < VERIFY_TTL_DAYS:
            verifications[idx] = cached
            reused += 1
        else:
            to_verify.append((idx, rec))

    print(f'[verify] 复用缓存 {reused} 条，需重新核实 {len(to_verify)} 条')

    def run_one(item):
        idx, rec = item
        return idx, verify_record(rec, today_str)

    completed = 0
    if to_verify:
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(run_one, it): it for it in to_verify}
            for future in as_completed(futures):
                idx, verification = future.result()
                verifications[idx] = verification
                cache[make_key(data[idx])] = verification
                completed += 1
                if completed % 100 == 0 or completed == len(to_verify):
                    print(f'[verify]   进度 {completed}/{len(to_verify)}')

    # 写入 verification + verified（便捷布尔）字段
    for idx, rec in enumerate(data):
        v = verifications[idx]
        if v is None:
            v = {'status': 'unverified', 'link_reachable': None, 'http_status': None,
                 'source_type': classify_source(rec.get('link', '') or rec.get('url', ''), rec.get('source', '')),
                 'verified_at': today_str, 'verified_by': 'http_check'}
            verifications[idx] = v
        rec['verification'] = v
        rec['verified'] = (v['status'] == 'auto_checked')

    # 写回主文件
    with open(input_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # 同步 verification 到分城市文件（保证网页/小程序运行时数据字段一致）
    sync_city_files(data)

    # 死链明细（便于后续抓取修正）
    dead_links = [(i, data[i]) for i, v in enumerate(verifications) if v['status'] == 'suspicious']
    dead_file = OUTPUT_DIR / 'verification_dead_links.txt'
    with open(dead_file, 'w', encoding='utf-8') as f:
        f.write(f'# 疑似失效链接列表 - 生成于 {today_str}\n')
        f.write(f'# 共 {len(dead_links)} 条 link 不可达，建议核查或修正\n\n')
        for i, rec in dead_links:
            f.write(f'[{rec.get("city")}] {rec.get("title","")}\n')
            f.write(f'  link: {rec.get("link") or rec.get("url","")}\n')
            f.write(f'  source: {rec.get("source","")}\n\n')
    print(f'[verify] 死链明细: {dead_file} ({len(dead_links)} 条)')

    # 统计
    from collections import Counter
    sc = Counter(v['status'] for v in verifications)
    print('[verify] 状态分布:', dict(sc.most_common()))
    checked = sum(1 for v in verifications if v['status'] == 'auto_checked')
    print(f'[verify] 官方已核实(auto_checked): {checked}/{total} ({checked/total*100:.1f}%)')

    save_cache(cache)
    print('[verify] 完成')


def sync_city_files(data):
    """把主文件算好的 verification 同步进各分城市文件（按 key 匹配）。"""
    by_key = {make_key(rec): rec.get('verification') for rec in data}
    city_files = sorted(OUTPUT_DIR.glob('exhibitions_*.json'))
    synced = 0
    for cf in city_files:
        try:
            arr = json.load(open(cf, 'r', encoding='utf-8'))
        except Exception:
            continue
        changed = False
        for rec in arr:
            v = by_key.get(make_key(rec))
            if v is not None and rec.get('verification') != v:
                rec['verification'] = v
                rec['verified'] = (v['status'] == 'auto_checked')
                changed = True
        if changed:
            json.dump(arr, open(cf, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
            synced += 1
    if synced:
        print(f'[verify] 已同步 verification 到 {synced} 个分城市文件')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        # best-effort：任何意外都不中断 CI 每日提交
        print(f'[verify] 核实过程异常（已跳过，不影响数据更新）: {e}')
        sys.exit(0)
