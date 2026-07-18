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

def process_file(path, config, city_fallback=None, verbose=False):
    """给单个 exhibitions 文件的每条活动加 booking_method，返回 (total, matched)。

    city_fallback: 分城市文件里若某条活动缺 city 字段，用文件名推断的城市兜底。
    """
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    matched_count = 0
    unmatched_cities = []
    for activity in data:
        if city_fallback and not activity.get('city'):
            activity['city'] = city_fallback
        booking = match_booking(activity, config)
        if booking:
            activity['booking_method'] = booking
            matched_count += 1
        else:
            unmatched_cities.append(activity.get('city', 'unknown'))

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    if verbose and unmatched_cities:
        from collections import Counter
        print(f'  未匹配城市分布: {dict(Counter(unmatched_cities))}')
    return len(data), matched_count


def main():
    config = load_config()
    print(f'城市配置: {len(config["cities"])} 个城市')
    print('=' * 60)

    # 1) 主文件
    total, matched = process_file(EXHIBITIONS_FILE, config, verbose=True)
    print(f'[主文件] exhibitions.json: {matched}/{total} '
          f'({matched/total*100:.1f}%) 已写入 booking_method')

    # 2) 所有分城市文件（小程序/网页运行时实际读取的就是它们）
    print('-' * 60)
    output_dir = PROJECT_ROOT / 'output'
    city_files = sorted(output_dir.glob('exhibitions_*.json'))
    grand_total, grand_matched = total, matched
    for cf in city_files:
        city = cf.stem.replace('exhibitions_', '')
        t, m = process_file(cf, config, city_fallback=city)
        grand_total += t
        grand_matched += m
        print(f'[分文件] {cf.name}: {m}/{t} ({m/t*100:.1f}%)')

    print('=' * 60)
    print(f'合计写入 booking_method: {grand_matched}/{grand_total} '
          f'({grand_matched/grand_total*100:.1f}%)')

if __name__ == '__main__':
    main()
