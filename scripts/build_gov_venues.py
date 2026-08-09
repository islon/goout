#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把各市政府门户的「文体场馆 / 文博场馆」策展列表批量纳入 scripts/auto_venues.json。

背景：
- 深圳「文体通」(sz.gov.cn/szzt2010/szwtt) 走 search.gd.gov.cn JSONP，字段齐全（见 build_szwtt_venues.py）。
- 其余城市没有同名「文体通」，各有自己的政府门户场馆目录（如广州 gz.gov.cn 的 文体场馆/文博场馆）。
  这些页面是 HTML 列表（场馆名 + 详情链接），详情页多为简介性质，缺地址/交通等结构化字段，
  因此本脚本只抽取 名称 / 类型 / 区县(从名称推断) / 来源链接，地址/交通留空。

用法：
    python3 scripts/build_gov_venues.py [city]
默认处理 guangzhou。每城市在 CITY_CONFIG 中配置列表页 URL 与类型判定。
"""
import json
import os
import re
import sys
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import venue_registry  # 读取 curated VENUES 名称/别名做去重

AUTO_PATH = os.path.join(ROOT, 'scripts', 'auto_venues.json')
CURL = ['curl', '-s', '--max-time', '30', '--curves', 'X25519:P-256']

# 各城市配置：source 标签 + listings[(url, kind)] + link_re(匹配详情链接与标题)
CITY_CONFIG = {
    'guangzhou': {
        'source': '广州市政府-文体场馆',
        'listings': [
            ('https://www.gz.gov.cn/zlgz/gzly/wzgz/wtcg/mindex.html', 'wtcg'),
            ('https://www.gz.gov.cn/zlgz/gzly/wzgz/wbcg/mindex.html', 'wbcg'),
        ],
        'link_re': r'href="(https://www\.gz\.gov\.cn/zlgz/gzly/wzgz/(?:wtcg|wbcg)/content/post_\d+\.html)"[^>]*title="([^"]*)"',
    },
}


def fetch(url):
    try:
        r = subprocess.run(CURL + [url], capture_output=True, text=True, timeout=45)
        return r.stdout or ''
    except Exception:
        return ''


def classify(kind, name):
    if kind == 'wtcg':  # 广州文体场馆：图书馆 + 体育场馆
        if '图书馆' in name:
            return '图书馆'
        return '体育中心'
    # wbcg 文博场馆：博物馆/美术馆/文化馆
    if '博物馆' in name or '博物院' in name:
        return '博物馆'
    if '美术' in name or '艺术' in name:
        return '美术馆'
    if '文化馆' in name:
        return '文化馆'
    return '文化中心'


def infer_district(name):
    m = re.search(r'([一-龥]{2,3})区', name)
    return (m.group(1) + '区') if m else ''


def collect(city):
    cfg = CITY_CONFIG[city]
    entries = []
    for url, kind in cfg['listings']:
        html = fetch(url)
        if not html:
            print(f"  [warn] 列表页拉取失败: {url}")
            continue
        for m in re.finditer(cfg['link_re'], html):
            detail, name = m.group(1), m.group(2).strip()
            if not name:
                continue
            postid = re.search(r'post_(\d+)\.html', detail)
            pid = postid.group(1) if postid else ''
            vtype = classify(kind, name)
            district = infer_district(name)
            entries.append({
                'source_code': f"{city[:2]}_gov_{pid}",
                'name': name,
                'source': cfg['source'],
                'city': city,
                'district': district,
                'type': vtype,
                'address': '',
                'transport': '',
                'fee': '',
                'description': '',
                'service_time': '',
                'official_url': '',
                'links': [{'url': detail, 'label': '广州市政府·场馆详情'}],
                'highlights': [v for v in [vtype, district] if v],
                'aliases': [],
                'status': 'auto',
                'activity_count': 0,
            })
    return entries


def dedup_keys():
    keys = set()
    if os.path.exists(AUTO_PATH):
        for v in json.load(open(AUTO_PATH, encoding='utf-8')):
            keys.add(v.get('name', '').strip().lower())
    for v in venue_registry.get_all_venues():
        keys.add(v.get('name', '').strip().lower())
        for a in v.get('aliases', []):
            keys.add(a.strip().lower())
    return keys


def main():
    city = sys.argv[1] if len(sys.argv) > 1 else 'guangzhou'
    if city not in CITY_CONFIG:
        print(f"未配置城市: {city}，已支持: {list(CITY_CONFIG)}")
        return
    print(f"=== 处理城市: {city} ===")
    entries = collect(city)
    print(f"列表解析到场馆: {len(entries)}")
    existing = dedup_keys()
    auto = json.load(open(AUTO_PATH, encoding='utf-8')) if os.path.exists(AUTO_PATH) else []
    added, skipped = [], []
    seen = set(v.get('name', '').strip().lower() for v in auto)
    for e in entries:
        nm = e['name'].strip().lower()
        if nm in existing or nm in seen:
            skipped.append(e['name'])
            continue
        auto.append(e)
        seen.add(nm)
        added.append(e['name'])
    json.dump(auto, open(AUTO_PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f"新增: {len(added)}  跳过(已收录): {len(skipped)}")
    for n in added:
        print("  +", n)
    if skipped:
        print("--- 跳过(已存在) ---")
        for n in skipped:
            print("  -", n)


if __name__ == '__main__':
    main()
