#!/usr/bin/env python3
"""
generate_city_venues.py — 由分城市场馆文件统一生成单文件兜底，并保证二者一致

生成：
    output/venue_info.json   全量单文件兜底（= 分城市合集，当前 11 城 1897 条）

设计原则（防退化）：
    - 分城市文件 venue_info_{city_key}.json 是权威源（小程序并行拉取的对象）。
    - 单文件兜底 venue_info.json 必须始终等于分城市文件的合集，绝不允许从过时的
      scripts/venue_info.json 复制（曾导致单文件退化成 5 城 596 条，手机走兜底时丢失
      成都/重庆/南京/武汉/西安/珠海 6 城场馆）。
    - 因此本脚本「以分城市为权威」：分城市存在时，仅聚合生成单文件，不改动分城市文件；
      仅当分城市文件完全缺失（首次生成）时，才从单文件/scripts 源拆分写回分城市。

用法：
    python3 scripts/generate_city_venues.py
"""

import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")

CITY_ORDER = ['beijing', 'shanghai', 'guangzhou', 'shenzhen', 'hangzhou',
              'chengdu', 'chongqing', 'nanjing', 'wuhan', 'xian', 'zhuhai']


def load_city_keys():
    """读取 output/cities.json，返回合法城市 key 顺序列表"""
    path = os.path.join(OUTPUT_DIR, "cities.json")
    if not os.path.exists(path):
        return list(CITY_ORDER)
    with open(path, "r", encoding="utf-8") as f:
        cities = json.load(f)
    keys = [c.get("key") for c in cities if c.get("key")]
    for k in CITY_ORDER:
        if k not in keys:
            keys.append(k)
    return keys


def _write_single(merged):
    single_path = os.path.join(OUTPUT_DIR, "venue_info.json")
    with open(single_path, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)


def main():
    city_keys = load_city_keys()

    # 1) 加载分城市文件（权威源）
    per_city = {}
    for key in city_keys:
        p = os.path.join(OUTPUT_DIR, f"venue_info_{key}.json")
        if os.path.exists(p):
            try:
                per_city[key] = json.load(open(p, encoding="utf-8"))
            except Exception as e:
                print(f"⚠️ 读取 {p} 失败: {e}")

    per_total = sum(len(a) for a in per_city.values())

    if per_total > 0:
        # 分城市为权威：单文件 = 分城市合集（保持各城市原序），不改动分城市文件
        merged = []
        for key in city_keys:
            merged.extend(per_city.get(key, []))
        _write_single(merged)
        print(f"✅ 单文件兜底已按分城市合集生成：{len(merged)} 条 / {len(per_city)} 城"
              f"（分城市文件未改动）")
        return

    # 2) 无分城市文件：从单文件 / scripts 源拆分（兼容首次生成场景）
    single_path = os.path.join(OUTPUT_DIR, "venue_info.json")
    src = None
    if os.path.exists(single_path):
        try:
            src = json.load(open(single_path, encoding="utf-8"))
        except Exception as e:
            print(f"⚠️ 读取 {single_path} 失败: {e}")
    if not src:
        alt = os.path.join(SCRIPT_DIR, "venue_info.json")
        if os.path.exists(alt):
            try:
                src = json.load(open(alt, encoding="utf-8"))
            except Exception as e:
                print(f"⚠️ 读取 {alt} 失败: {e}")
    if isinstance(src, dict):
        src = list(src.values())
    if not src:
        print("❌ 既无分城市文件也无单文件/scripts 源，无法生成。")
        sys.exit(1)

    _write_single(src)
    by_city = {}
    for v in src:
        by_city.setdefault(v.get("city"), []).append(v)
    for key in city_keys:
        arr = by_city.get(key, [])
        out_path = os.path.join(OUTPUT_DIR, f"venue_info_{key}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        print(f"  · venue_info_{key}.json: {len(arr)} 条")
    print(f"\n✅ 已从单文件拆分生成分城市文件 + 单文件兜底，合计 {len(src)} 条")


if __name__ == "__main__":
    main()
