#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成「近期活动」小文件 output/exhibitions_recent.json。

目的：
  小程序首屏需要从 GitHub raw 拉数据。全量分城市文件共约 4910 条、需 10 个并行请求，
  在中国大陆 raw.githubusercontent.com 常被拦截/超时，首屏体感很慢。
  本脚本按 start_date 升序，取每个城市「未结束且最早举办」的前 N 条（默认 80），
  合并为单个小文件（约 800 条）。小程序启动先拉这个小文件秒出首屏（默认“即将举办”视图），
  全量分城市文件在后台静默拉取，拉到后再刷新。

产物：output/exhibitions_recent.json （数组，结构与分城市文件一致，含 booking_method 等全部字段）
"""
import json
import os
import glob
from datetime import date

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'output')
RECENT_FILE = os.path.join(OUTPUT_DIR, 'exhibitions_recent.json')
PER_CITY_CAP = 80  # 每城取最早未结束的前 N 条


def parse_date(s):
    if not s:
        return None
    try:
        return date.fromisoformat(str(s)[:10])
    except Exception:
        return None


def main():
    files = sorted(glob.glob(os.path.join(OUTPUT_DIR, 'exhibitions_*.json')))
    if not files:
        print('[generate_recent] 未找到任何 exhibitions_*.json，退出')
        return

    today = date.today()
    per_city = {}
    for fp in files:
        try:
            with open(fp, 'r', encoding='utf-8') as f:
                arr = json.load(f)
        except Exception as e:
            print('[generate_recent] 读取失败，跳过:', fp, e)
            continue
        if not isinstance(arr, list):
            arr = list(arr.values())
        city = os.path.basename(fp).replace('exhibitions_', '').replace('.json', '')
        # 仅保留「未结束」(end_date >= 今天) 的活动，并按 start_date 升序
        alive = [x for x in arr if parse_date(x.get('end_date') or x.get('start_date')) and parse_date(x.get('end_date') or x.get('start_date')) >= today]
        alive.sort(key=lambda x: (x.get('start_date') or '9999', x.get('city') or ''))
        per_city[city] = alive[:PER_CITY_CAP]

    # 合并并按 start_date 升序，保证首屏展示的是最早举办的近期活动
    merged = []
    for city in sorted(per_city.keys()):
        merged.extend(per_city[city])
    merged.sort(key=lambda x: (x.get('start_date') or '9999', x.get('city') or ''))

    with open(RECENT_FILE, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    total_city = sum(len(v) for v in per_city.values())
    size_kb = os.path.getsize(RECENT_FILE) / 1024
    print(f'[generate_recent] 已生成 {RECENT_FILE}')
    print(f'  覆盖城市数: {len(per_city)}')
    print(f'  近期活动条数: {len(merged)} (各城合计取 {total_city}，已按 start_date 升序合并)')
    print(f'  文件大小: {size_kb:.1f} KB')


if __name__ == '__main__':
    main()
