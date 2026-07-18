#!/usr/bin/env python3
"""
活动数据真实性核实脚本 - L1(HTTP链接验证) + L3(来源分类)
对每条活动写入 verification 字段，记录核实状态。

使用方式：
    python3 scripts/verify_activities.py
    python3 scripts/verify_activities.py --input output/exhibitions.json --output output/exhibitions.json
"""

import json
import re
import sys
import subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from urllib.parse import urlparse

PROJECT_ROOT = Path(__file__).parent.parent
INPUT_FILE = PROJECT_ROOT / 'output' / 'exhibitions.json'

# ============================================================================
# L3: 来源分类规则
# ============================================================================

# 政府域名特征
GOV_PATTERNS = [
    r'\.gov\.cn',
    r'gov\.cn',
    r'wglyj\.|whlyj\.|wlt\.|wglt\.',  # 文旅局
    r'wgxj\.|whlyw\.',                  # 文广旅
    r'szmassart\.com',                  # 深圳文化馆系统
    r'jijiang\.gov|nanjing\.gov|shanghai\.gov|guangzhou\.gov',
    r'\.lg\.gov\.cn|cq\.gov\.cn|hz\.gov\.cn',
    r'shenzhen-world\.com',             # 深圳世展
]

# 媒体域名特征
MEDIA_HOSTS = [
    'm.toutiao.com', 'toutiao.com', 'm.sohu.com', 'sohu.com',
    'k.sina.cn', 'sina.cn', 'm.sina.cn', 'cj.sina.cn', 'news.sina',
    'm.163.com', 'www.163.com', 'c.m.163.com', '163.com',
    'm.weibo.cn', 'weibo.cn', 'weibo.com',
    'm.thepaper.cn', 'thepaper.cn',
    'm.sh.bendibao.com', 'bendibao.com',
    'xinwen.bjd.com.cn', 'bjd.com.cn',           # 北京日报
    'hznews.hangzhou.com.cn',                    # 杭州新闻
    'weitoutiao.zjurl.cn',                       # 浙江头条
    'www.nationalreading.gov.cn',                # 全民阅读
    'm.thecover.cn',                             # 封面新闻
    'www.visitbeijing.com.cn',                   # 北京文旅
    'www.meet-in-shanghai.net',                  # 上海文旅
    'paper.cn', 'chinanews', 'people.com', 'xinhuanet',
    'cqn.com.cn', 'cnr.cn', 'ce.cn',
]

# 场馆官网特征（博物馆/图书馆/剧院/学校等）
VENUE_PATTERNS = [
    r'museum|bwg|博物馆',
    r'lib\.|library|tushuguan|tsl|lib\.org',
    r'whg|cultural.*center|wenhuaguan|文化馆',
    r'snj|children|shaonian|少年',
    r'artmuseum|meishuguan|美术馆',
    r'theatre|theater|juchang|剧院|drama',
    r'concert|yinyue|音乐',
    r'science|kexue|keji|科技|kexueguan',
    r'university|edu\.cn|daxue|xx\.edu|school',
    r'\.edu\.cn',
    r'jyzc\.com',                                # 教育资源
    r'szlib\.org\.cn|nslib\.|nslib',
    r'nanshanmuseum|nsmuseum',
    r'szcec\.com',                               # 深圳会展中心
    r'cdsszwhg\.com',                            # 成都文化馆
    r'jjqwhg\.cn',                               # 锦江区文化馆
    r'oct-|octohbay|oct.*wetland',
    r'sarc\.', r'ntgc\.', r'zsjbwg',
]

def classify_source(link, source):
    """根据 link host 和 source 字段分类来源"""
    text = f"{link} {source}".lower()
    
    # 政府类
    for pat in GOV_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return 'government'
    
    # 媒体类
    try:
        host = urlparse(link).netloc.lower() if link else ''
    except Exception:
        host = ''
    for media in MEDIA_HOSTS:
        if media in host or media in text:
            return 'media'
    
    # 场馆类
    for pat in VENUE_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return 'venue'
    
    # 包含具体机构名的也算venue
    if source and len(source) > 2 and source not in ('auto_generated', 'auto-generated'):
        # source不是auto_generated且有具体名字，多数是场馆/机构
        if any(kw in source for kw in ['馆', '院', '中心', '学校', '剧院', '书店', '公园', '街道', '社区', '区', '局', '委']):
            return 'venue'
    
    return 'unknown'

# ============================================================================
# L1: HTTP 链接验证（curl 并发）
# ============================================================================

def check_link_reachable(url, timeout=8):
    """用 curl 验证 link 可达性，返回 (reachable, http_status, final_url)"""
    if not url:
        return None, None, None
    
    cmd = [
        'curl', '-sI', '-L',  # -I HEAD请求, -L 跟随重定向, -s 静默
        '--connect-timeout', str(timeout),
        '--max-time', str(timeout + 5),
        '-A', 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        url
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 10)
        if result.returncode != 0:
            return False, None, None
        
        # 解析HTTP状态码（取最后一行，因为可能有重定向）
        status_match = re.search(r'HTTP/[\d.]+\s+(\d+)', result.stdout)
        if status_match:
            status = int(status_match.group(1))
            # 取最后一个状态码（重定向后的最终状态）
            all_statuses = re.findall(r'HTTP/[\d.]+\s+(\d+)', result.stdout)
            if all_statuses:
                status = int(all_statuses[-1])
            reachable = 200 <= status < 400
            return reachable, status, url
        return False, None, None
    except subprocess.TimeoutExpired:
        return False, None, None
    except Exception:
        return False, None, None

def verify_record(record, idx):
    """验证单条记录，返回 verification dict"""
    link = record.get('link', '') or record.get('url', '')
    source = record.get('source', '')
    
    # L1: HTTP验证
    reachable, http_status, _ = check_link_reachable(link)
    
    # L3: 来源分类
    source_type = classify_source(link, source)
    
    # 综合状态
    if reachable is True:
        status = 'auto_checked'
    elif reachable is False:
        if source_type in ('government', 'venue'):
            status = 'suspicious'  # 政府场馆类死链需要警惕
        else:
            status = 'suspicious'
    else:
        status = 'unverified'
    
    verification = {
        'status': status,
        'link_reachable': reachable,
        'http_status': http_status,
        'source_type': source_type,
        'verified_at': '2026-07-18',
        'verified_by': 'http_check',
    }
    
    return idx, verification

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default=str(INPUT_FILE))
    parser.add_argument('--output', default=None, help='输出文件，默认覆盖input')
    parser.add_argument('--workers', type=int, default=30, help='并发数')
    parser.add_argument('--limit', type=int, default=0, help='只验证前N条（测试用）')
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path
    
    print(f'读取: {input_path}')
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if args.limit > 0:
        data = data[:args.limit]
    
    total = len(data)
    print(f'总计 {total} 条活动')
    print(f'并发数: {args.workers}')
    print('-' * 60)
    
    # 并发验证
    verifications = [None] * total
    completed = 0
    
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(verify_record, record, idx): idx
            for idx, record in enumerate(data)
        }
        
        for future in as_completed(futures):
            idx = futures[future]
            try:
                result_idx, verification = future.result()
                verifications[result_idx] = verification
                completed += 1
                if completed % 200 == 0 or completed == total:
                    print(f'  进度: {completed}/{total} ({completed/total*100:.1f}%)')
            except Exception as e:
                verifications[idx] = {
                    'status': 'error',
                    'link_reachable': None,
                    'http_status': None,
                    'source_type': 'unknown',
                    'verified_at': '2026-07-18',
                    'verified_by': 'http_check',
                    'error': str(e)[:100],
                }
    
    # 写入verification字段
    print('-' * 60)
    print('写入 verification 字段...')
    for idx, record in enumerate(data):
        record['verification'] = verifications[idx]
    
    # 统计
    print('-' * 60)
    print('=== 验证结果统计 ===')
    
    from collections import Counter
    status_cnt = Counter(v['status'] for v in verifications)
    print('状态分布:')
    for k, v in status_cnt.most_common():
        print(f'  {k}: {v} ({v/total*100:.1f}%)')
    
    reachable_cnt = sum(1 for v in verifications if v['link_reachable'] is True)
    unreachable_cnt = sum(1 for v in verifications if v['link_reachable'] is False)
    print(f'\nlink可达: {reachable_cnt} ({reachable_cnt/total*100:.1f}%)')
    print(f'link不可达: {unreachable_cnt} ({unreachable_cnt/total*100:.1f}%)')
    
    src_type_cnt = Counter(v['source_type'] for v in verifications)
    print('\n来源类型分布:')
    for k, v in src_type_cnt.most_common():
        print(f'  {k}: {v} ({v/total*100:.1f}%)')
    
    # 死链明细
    dead_links = [(i, data[i]) for i, v in enumerate(verifications) if v['link_reachable'] is False]
    if dead_links:
        print(f'\n=== 死链明细（前20条）===')
        for i, rec in dead_links[:20]:
            print(f'  #{i} [{rec.get("city")}] {rec.get("title","")[:40]} | link={rec.get("link","")[:60]}')
    
    # 保存
    print(f'\n保存到: {output_path}')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print('完成。')
    
    # 输出死链列表到单独文件，便于人工复核
    dead_links_file = output_path.parent / 'verification_dead_links.txt'
    with open(dead_links_file, 'w', encoding='utf-8') as f:
        f.write(f'# 死链列表 - 生成于 2026-07-18\n')
        f.write(f'# 共 {len(dead_links)} 条 link 不可达，需要人工复核\n\n')
        for i, rec in dead_links:
            f.write(f'#{i} [{rec.get("city")}] {rec.get("title","")}\n')
            f.write(f'  link: {rec.get("link","")}\n')
            f.write(f'  source: {rec.get("source","")}\n')
            f.write(f'  venue: {rec.get("venue","")}\n\n')
    print(f'死链明细已保存到: {dead_links_file}')

if __name__ == '__main__':
    main()
