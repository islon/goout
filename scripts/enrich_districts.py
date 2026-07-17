"""数据富集：给每条活动补上 district 区县字段，并确保场馆区县齐全。

为什么做：
  output/exhibitions.json 历史上没有 district 字段，区县一直是小程序端临时算的；
  而 SQLite 导入（db_import.py）只按地址关键字解析，导致大量场馆（尤其是名字带区名
  却不在 venue_info.json 里的"孤儿场馆"）落空。本脚本把区县作为一等字段写进数据，
  让网页版 / 小程序 / 数据库三方都直接读到，且不会被下次爬虫覆盖（已接入 update_data.sh 与 CI）。

用法：
  python scripts/enrich_districts.py
幂等：重复运行结果一致，已存在且一致的 district 不会改动。
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from district_map import resolve_district

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXHIBITIONS_FILE = os.path.join(PROJECT_ROOT, 'output', 'exhibitions.json')
VENUE_INFO_FILE = os.path.join(PROJECT_ROOT, 'output', 'venue_info.json')


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')


def enrich_exhibitions():
    if not os.path.exists(EXHIBITIONS_FILE):
        print(f'跳过活动富集：文件不存在 {EXHIBITIONS_FILE}')
        return
    ex = load_json(EXHIBITIONS_FILE)
    total = len(ex)
    changed = 0
    other = {}
    for e in ex:
        city = e.get('city')
        source = e.get('source')
        venue = e.get('venue')
        address = e.get('address')
        desc = e.get('description')
        d = resolve_district(city, source, venue, address, desc)
        if e.get('district') != d:
            e['district'] = d
            changed += 1
        if d == '其他':
            key = venue or source or '(无场馆)'
            other[key] = other.get(key, 0) + 1
    save_json(EXHIBITIONS_FILE, ex)

    # 按城市统计
    by_city = {}
    for e in ex:
        c = e.get('city', '?')
        by_city.setdefault(c, {'n': 0, 'other': 0})
        by_city[c]['n'] += 1
        if e.get('district') == '其他':
            by_city[c]['other'] += 1

    print(f'[活动] 共 {total} 条，更新 district 字段 {changed} 条')
    for c, s in by_city.items():
        pct = (s['other'] / s['n'] * 100) if s['n'] else 0
        print(f'  {c}: {s["n"]} 条，其他 {s["other"]} ({pct:.1f}%)')
    if other:
        print('  "其他" 来源 Top（多为 manual / 城市级聚合源，属合理）：')
        for k, n in sorted(other.items(), key=lambda x: -x[1])[:15]:
            print(f'    {k} ×{n}')
    else:
        print('  "其他" 来源：无')


# 网页版只读分城市文件 output/exhibitions_{city}.json，必须同步补齐 district，否则网页区县筛选与小程序不一致
CITY_CODES = ['shenzhen', 'guangzhou', 'shanghai', 'beijing', 'hangzhou']


def enrich_city_files():
    for city in CITY_CODES:
        path = os.path.join(PROJECT_ROOT, 'output', f'exhibitions_{city}.json')
        if not os.path.exists(path):
            continue
        arr = load_json(path)
        changed = 0
        for e in arr:
            d = resolve_district(city, e.get('source'), e.get('venue'),
                                 e.get('address'), e.get('description'))
            if e.get('district') != d:
                e['district'] = d
                changed += 1
        save_json(path, arr)
        print(f'[分城市] {city}: 补齐 district {changed} 条')


def enrich_venues():
    if not os.path.exists(VENUE_INFO_FILE):
        print(f'跳过场馆富集：文件不存在 {VENUE_INFO_FILE}')
        return
    venues = load_json(VENUE_INFO_FILE)
    if isinstance(venues, dict):
        venues = list(venues.values())
    total = len(venues)
    changed = 0
    for v in venues:
        if v.get('district'):
            continue
        d = resolve_district(v.get('city'), v.get('source'), v.get('name'),
                             v.get('address'), v.get('description'))
        v['district'] = d
        changed += 1
    save_json(VENUE_INFO_FILE, venues)
    print(f'[场馆] 共 {total} 个，补全 district 字段 {changed} 个')


if __name__ == '__main__':
    print('=== 开始数据富集（区县映射补齐）===')
    enrich_exhibitions()
    enrich_city_files()
    enrich_venues()
    print('=== 完成 ===')
