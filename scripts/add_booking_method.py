#!/usr/bin/env python3
"""
给 exhibitions.json 中每条活动添加 booking_method 字段
根据 city + venue 关键词匹配城市级官方聚合小程序入口
"""

import json
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
CONFIG_FILE = PROJECT_ROOT / 'scripts' / 'city_mini_programs.json'
EXHIBITIONS_FILE = PROJECT_ROOT / 'output' / 'exhibitions.json'

def load_config():
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def match_booking(activity, config):
    """根据 city + venue 匹配报名入口"""
    city = activity.get('city', '')
    venue = activity.get('venue', '') or ''
    category = activity.get('category', '') or ''

    city_config = config['cities'].get(city)
    if not city_config:
        return None

    # 所有活动都默认使用城市级 primary 入口（兜底）
    primary = city_config['primary']

    # venue 关键词匹配（所有关键词都用 primary，因为入口都是城市级聚合）
    # 这里保持扩展性：未来可以针对特定场馆类型用 fallback
    keywords = [v['keyword'] for v in config.get('venue_keywords', [])]

    matched_keyword = None
    for kw in keywords:
        if kw in venue:
            matched_keyword = kw
            break

    booking = {
        "type": "city_aggregated",
        "app_name": primary['app_name'],
        "app_type": primary['app_type'],
        "search_hint": primary['search_hint'],
        "platform_url": primary.get('platform_url'),
        "city": city_config['city_name']
    }

    if matched_keyword:
        booking["matched_venue_type"] = matched_keyword

    return booking

def main():
    config = load_config()

    with open(EXHIBITIONS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f'加载活动: {len(data)} 条')
    print(f'城市配置: {len(config["cities"])} 个城市')
    print('-' * 60)

    matched_count = 0
    unmatched_cities = []

    for activity in data:
        booking = match_booking(activity, config)
        if booking:
            activity['booking_method'] = booking
            matched_count += 1
        else:
            unmatched_cities.append(activity.get('city', 'unknown'))

    print(f'匹配成功: {matched_count}/{len(data)} ({matched_count/len(data)*100:.1f}%)')

    if unmatched_cities:
        from collections import Counter
        print(f'未匹配城市分布: {dict(Counter(unmatched_cities))}')

    # 各城市匹配数
    from collections import Counter
    city_match = Counter()
    for a in data:
        if a.get('booking_method'):
            city_match[a.get('city', '')] += 1
    print()
    print('各城市匹配数:')
    for c, n in city_match.most_common():
        print(f'  {c}: {n}')

    # venue_type 分布
    venue_type_match = Counter()
    for a in data:
        bm = a.get('booking_method', {})
        vt = bm.get('matched_venue_type', '(无关键词)')
        venue_type_match[vt] += 1
    print()
    print('venue类型分布:')
    for v, n in venue_type_match.most_common():
        print(f'  {v}: {n}')

    # 写回
    with open(EXHIBITIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print()
    print(f'已写入: {EXHIBITIONS_FILE}')
    print(f'文件大小: {EXHIBITIONS_FILE.stat().st_size / 1024:.1f} KB')

if __name__ == '__main__':
    main()
