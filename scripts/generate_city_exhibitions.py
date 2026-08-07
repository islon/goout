#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 exhibitions.json 生成分城市活动文件
"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")

def main():
    src = os.path.join(OUTPUT_DIR, "exhibitions.json")
    if not os.path.exists(src):
        print("❌ exhibitions.json 不存在:", src)
        return

    with open(src, "r", encoding="utf-8") as f:
        exhibitions = json.load(f)
    
    by_city = {}
    for e in exhibitions:
        city = e.get("city", "")
        if not city:
            continue
        by_city.setdefault(city, []).append(e)

    total = 0
    for city, arr in sorted(by_city.items()):
        out_path = os.path.join(OUTPUT_DIR, f"exhibitions_{city}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        total += len(arr)
        print(f"  · exhibitions_{city}.json: {len(arr)} 条")

    print(f"\n✅ 已生成 {len(by_city)} 个分城市活动文件，合计 {total} 条")

if __name__ == "__main__":
    main()
