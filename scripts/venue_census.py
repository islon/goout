#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
场馆普查脚本 —— 让「数据采集覆盖城市里的所有场馆」成为可执行的常态化能力。

设计动机：
  原 venue_registry 是手工维护的「精选真相源」（约 90+ 个场馆），深圳 38 个爬虫
  只爬这 90 家的活动，城市里绝大多数场馆根本没进库；其他 9 城更只有活动浅抓。
  要做到「覆盖城市里的所有场馆」，需要一套自动化普查能力，而不是逐个手工补。

普查来源（两层，广度优先、可扩展）：
  1) 活动语料反向普查（主，可靠）：扫描 output/exhibitions*.json，把每条活动引用的
     venue 名提炼出来。凡 registry 里没有的，即视为「城市里被活动证明真实存在、
     但尚未收录」的场馆，自动纳入。随采集自动扩面，天然覆盖全部 10 城。
  2) 外部官方名录（辅，best-effort）：各城市官方场馆目录（国家公共文化云 culturedc、
     图书馆/博物馆系统）。能抓到就补，抓不到静默跳过，绝不中断管线。

产出：
  scripts/auto_venues.json  —— 自动发现的场馆池（status='auto'），纳入版本库，可审查、可增量。
  并调用 venue_registry.generate_venue_info_json 把「精选 + 自动」合并写出 venue_info.json，
  后续 generate_city_venues 自动按城市拆分，10 城场馆指南同步扩面。

去重：
  以归一化名称（去空格/标点/括号）为键，分别与「精选 registry」和「已有 auto 池」比对，
  已存在则跳过，避免重复累积。

用法：
  python3 scripts/venue_census.py            # 跑完整普查
  python3 scripts/venue_census.py --external # 额外尝试外部官方名录源
  python3 scripts/venue_census.py --limit 50 # 调试：最多处理 50 个新场馆
"""
import json
import os
import re
import sys
import argparse
from pathlib import Path
from collections import Counter, defaultdict

PROJECT_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = PROJECT_ROOT / 'scripts'
OUTPUT_DIR = PROJECT_ROOT / 'output'
AUTO_VENUES_FILE = SCRIPTS_DIR / 'auto_venues.json'

sys.path.append(str(SCRIPTS_DIR))
import venue_registry as vr

CITY_CODE_TO_NAME = {
    'shenzhen': '深圳', 'guangzhou': '广州', 'shanghai': '上海', 'beijing': '北京',
    'hangzhou': '杭州', 'chengdu': '成都', 'nanjing': '南京', 'wuhan': '武汉',
    'xian': '西安', 'chongqing': '重庆',
}

# 类型推断关键词（名称 → 类型）
TYPE_KEYWORDS = [
    ('博物馆', '博物馆'), ('博物院', '博物馆'), ('纪念馆', '博物馆'), ('遗址', '博物馆'),
    ('美术馆', '美术馆'), ('艺术馆', '美术馆'), ('画廊', '美术馆'),
    ('图书馆', '图书馆'), ('书屋', '图书馆'), ('书房', '图书馆'), ('阅览', '图书馆'),
    ('科技馆', '科技馆'), ('科学馆', '科技馆'), ('科普', '科普馆'), ('自然馆', '科普馆'),
    ('文化馆', '文化馆'), ('文化中心', '文化中心'), ('文化站', '文化中心'), ('文化活动中心', '文化中心'),
    ('剧院', '演出场馆'), ('剧场', '演出场馆'), ('音乐厅', '演出场馆'), ('演艺', '演出场馆'), ('戏院', '演出场馆'),
    ('体育', '体育中心'), ('健身', '体育中心'), ('体育馆', '体育中心'), ('运动', '体育中心'),
    ('青少年', '青少年宫'), ('少年宫', '青少年宫'), ('儿童', '青少年宫'),
    ('公园', '公园'), ('植物园', '公园'), ('动物园', '公园'), ('湿地', '公园'), ('郊野', '公园'),
    ('会展', '会展中心'), ('展览中心', '会展中心'),
]

EXTERNAL_SOURCES = [
    # 国家公共文化云「逛场馆」——覆盖全国，按 regionName 取各城市场馆
    {
        'name': '国家公共文化云-场馆',
        'type': 'culturedc',
        'url': 'https://www.culturedc.cn/web3.0/venue-home.html',
    },
]


def normalize_name(name, strip_paren=True):
    """归一化场馆名用于去重。
    strip_paren=True 时去掉括号内容（'深圳图书馆(中心馆)'→'深圳图书馆'），
    把同名变体/分馆合并到主场馆，避免重复累积。
    """
    if not name:
        return ''
    s = name.strip()
    s = s.replace('（', '(').replace('）', ')')
    if strip_paren:
        s = re.sub(r'\([^)]*\)', '', s)
        s = re.sub(r'（[^）]*）', '', s)
    s = re.sub(r'\s+', '', s)
    return s.lower()


# 明显非场馆的占位/噪声名，直接排除
NOISE_NAMES = ('待定', '详见公告', '线上', '网络平台', '官方平台', '公众号', '小程序',
               '直播间', '视频号', '官网', 'App', 'APP', '客户端', '详见', '电话咨询',
               '另行通知', '暂定', '待通知')


def is_noise_venue(name):
    if not name or len(name) < 3:
        return True
    for n in NOISE_NAMES:
        if n in name:
            return True
    return False


def infer_type(name):
    for kw, t in TYPE_KEYWORDS:
        if kw in name:
            return t
    return '其他'


def load_auto_venues():
    if AUTO_VENUES_FILE.exists():
        try:
            return json.loads(AUTO_VENUES_FILE.read_text(encoding='utf-8'))
        except Exception:
            return []
    return []


def mine_from_activities(min_activities=2):
    """从活动语料反向提炼场馆（主普查源）。
    以「去括号归一化键」聚合，同一主场馆的不同分馆/括号写法合并，
    规范名取出现频次最高的写法。仅保留被 ≥min_activities 场活动引用的场馆，
    避免一次性地点/噪声污染（准确性优先）。
    """
    groups = {}
    files = sorted(OUTPUT_DIR.glob('exhibitions*.json'))
    for f in files:
        try:
            arr = json.loads(f.read_text(encoding='utf-8'))
        except Exception:
            continue
        if not isinstance(arr, list):
            continue
        for rec in arr:
            venue = (rec.get('venue') or '').strip()
            city = rec.get('city') or ''
            if not venue or not city or is_noise_venue(venue):
                continue
            key = normalize_name(venue)
            if not key:
                continue
            g = groups.get(key)
            if g is None:
                g = groups[key] = {
                    'city': city,
                    'variants': Counter(),
                    'districts': Counter(),
                    'count': 0,
                }
            g['variants'][venue] += 1
            g['count'] += 1
            dist = rec.get('district') or ''
            if dist:
                g['districts'][dist] += 1

    results = []
    for key, g in groups.items():
        if g['count'] < min_activities:
            continue
        # 规范名：出现频次最高的写法；频次相同取最短
        canonical = sorted(g['variants'].items(), key=lambda kv: (-kv[1], len(kv[0])))[0][0]
        top_district = g['districts'].most_common(1)[0][0] if g['districts'] else ''
        results.append({
            'name': canonical,
            'city': g['city'],
            'district': top_district,
            'activity_count': g['count'],
        })
    return results


def fetch_external_venues():
    """best-effort 外部官方名录（当前预留 culturedc 入口，抓不到静默返回空）。"""
    # 国家公共文化云为 JS 渲染 SPA，列表经 XHR 加载，直接抓页面拿不到数据；
    # 此处保留扩展点：后续接入其 JSON 接口或各城市图书馆/博物馆系统。
    # 现阶段返回空，不阻断管线。
    return []


def build_auto_venues(mining_results, external_results, limit=0):
    """合并主/辅源，去重后生成 auto_venues 列表。"""
    curated = vr.get_all_venues()
    curated_keys = {normalize_name(v.get('name', '')) for v in curated}
    curated_codes = {v.get('source_code') for v in curated}

    existing_auto = load_auto_venues()
    existing_auto_keys = {normalize_name(v.get('name', '')) for v in existing_auto}

    merged = []
    seen_keys = set(curated_keys) | existing_auto_keys
    seen_codes = set(curated_codes)

    # 主源优先（带活动计数，可信度更高）
    pool = list(mining_results) + list(external_results)
    # 按活动计数降序，先收录被反复证明存在的场馆
    pool.sort(key=lambda x: x.get('activity_count', 0), reverse=True)

    for item in pool:
        key = normalize_name(item['name'])
        if not key or key in seen_keys:
            continue
        city = item['city']
        # 生成唯一 source_code
        base = re.sub(r'[^a-z0-9]', '', re.sub(r'[^\w]', '', item['name']).lower())[:12] or 'v'
        code = f"auto_{city[:3]}_{base}"
        n = 1
        while code in seen_codes:
            code = f"auto_{city[:3]}_{base}{n}"
            n += 1
        seen_codes.add(code)
        seen_keys.add(key)

        vtype = infer_type(item['name'])
        v = {
            'source_code': code,
            'name': item['name'],
            'city': city,
            'district': item.get('district', ''),
            'type': vtype,
            'address': '',
            'transport': '',
            'fee': '免费',
            'description': f"由活动语料自动普查收录的{city}场馆，常态举办亲子/文化活动。",
            'official_url': '',
            'links': [],
            'highlights': [],
            'aliases': [],
            'status': 'auto',
            'activity_count': item.get('activity_count', 0),
        }
        merged.append(v)
        if limit and len(merged) >= limit:
            break
    return merged


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--external', action='store_true', help='额外尝试外部官方名录源')
    parser.add_argument('--limit', type=int, default=0, help='最多新增 N 个场馆（调试）')
    parser.add_argument('--min-activities', type=int, default=2,
                        help='被至少 N 场活动引用的场馆才收录（默认 2，准确性优先）')
    parser.add_argument('--no-write', action='store_true', help='只统计不写文件')
    args = parser.parse_args()

    print('[census] 开始场馆普查...')
    mining = mine_from_activities(min_activities=args.min_activities)
    print(f'[census] 活动语料反向提炼候选场馆: {len(mining)} 个')

    external = fetch_external_venues() if args.external else []
    if external:
        print(f'[census] 外部名录补充: {len(external)} 个')

    new_venues = build_auto_venues(mining, external, limit=args.limit)

    existing = load_auto_venues()
    all_auto = existing + new_venues

    # 写入 auto_venues.json
    if not args.no_write:
        AUTO_VENUES_FILE.write_text(
            json.dumps(all_auto, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'[census] 已写入 {AUTO_VENUES_FILE.name}: 累计 {len(all_auto)} 个自动场馆（本次新增 {len(new_venues)}）')

    # 合并写出 venue_info.json（精选 + 自动）
    if not args.no_write:
        out = OUTPUT_DIR / 'venue_info.json'
        vr.generate_venue_info_json(str(out))
        # 统计各城市自动场馆数
        by_city = Counter(v['city'] for v in all_auto)
        print('[census] 各城市自动场馆分布:')
        for c in CITY_CODE_TO_NAME:
            if by_city.get(c):
                print(f'    {CITY_CODE_TO_NAME[c]}({c}): {by_city[c]}')

    total_venues = len(vr.get_all_venues()) + len(all_auto)
    print(f'[census] 完成。精选场馆 {len(vr.get_all_venues())} + 自动场馆 {len(all_auto)} = 合计 {total_venues}')
    if new_venues:
        print('[census] 新增示例: ' + '、'.join(v['name'] for v in new_venues[:10]))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'[census] 普查异常（已跳过，不影响数据更新）: {e}')
        sys.exit(0)
