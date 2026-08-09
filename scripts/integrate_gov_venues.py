#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把各子代理采集的政府场馆文件 (/workspace/gov_venues_<city>.json) 并入 scripts/auto_venues.json。

- 与既有 auto_venues + curated VENUES（名称/别名）按名称去重，避免重复。
- 同名不同城市允许并存（按 city+name 去重批内重复）。
- 成都等空文件（[]）自动跳过。
"""
import json
import os
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import venue_registry

AUTO_PATH = os.path.join(ROOT, 'scripts', 'auto_venues.json')
SRC_GLOB = '/workspace/gov_venues_*.json'


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
    existing = dedup_keys()
    auto = json.load(open(AUTO_PATH, encoding='utf-8')) if os.path.exists(AUTO_PATH) else []
    seen = set(v.get('name', '').strip().lower() for v in auto)
    batch_seen = set()
    total_added = 0
    total_skipped = 0
    for f in sorted(glob.glob(SRC_GLOB)):
        city = os.path.basename(f).replace('gov_venues_', '').replace('.json', '')
        try:
            data = json.load(open(f, encoding='utf-8'))
        except Exception as e:
            print(f"[skip] {city}: 解析失败 {e}")
            continue
        if not isinstance(data, list) or not data:
            print(f"[skip] {city}: 空/非数组")
            continue
        added = skipped = 0
        for e in data:
            nm = (e.get('name') or '').strip().lower()
            if not nm:
                continue
            key = (e.get('city'), nm)
            if nm in existing or nm in seen or key in batch_seen:
                skipped += 1
                continue
            auto.append(e)
            seen.add(nm)
            batch_seen.add(key)
            existing.add(nm)
            added += 1
        total_added += added
        total_skipped += skipped
        print(f"{city:10s} 新增 {added:5d}  跳过(已收录/重复) {skipped:5d}")
    json.dump(auto, open(AUTO_PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f"\n=== 合计新增 {total_added}  跳过 {total_skipped} | auto_venues 现 {len(auto)} 条 ===")


if __name__ == '__main__':
    main()
