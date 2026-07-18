#!/usr/bin/env python3
"""
generate_city_venues.py — 将全量场馆按城市拆分为分城市文件

生成：
    output/venue_info_{city_key}.json   （每个城市一个场馆数组，线上由小程序并行拉取）

用途：
    小程序「场馆指南」需要展示全部已收录场馆（目前约 2964 个）。若只打包一个
    861KB 的 venue_info.json，既会撑爆 2MB 主包，又因单文件过大在弱网下容易拉取失败
    （此前用户端卡在裁剪兜底的 481 个）。

    改为与活动数据一致的分城市小文件后：
      - 主包无需打包全量场馆（离线兜底仍是裁剪快照）；
      - 运行时并行拉取 10 个 ~90KB 的小文件，多源容灾 + 缺失城市自动补齐，
        与活动加载逻辑完全对称，弱网下更稳。

用法：
    python3 scripts/generate_city_venues.py
"""

import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")


def load_cities():
    """读取 output/cities.json，返回合法城市 key 集合"""
    path = os.path.join(OUTPUT_DIR, "cities.json")
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        cities = json.load(f)
    return set(c.get("key") for c in cities if c.get("key"))


def main():
    src = os.path.join(OUTPUT_DIR, "venue_info.json")
    if not os.path.exists(src):
        print("❌ venue_info.json 不存在:", src)
        sys.exit(1)

    with open(src, "r", encoding="utf-8") as f:
        venues = json.load(f)
    if isinstance(venues, dict):
        venues = list(venues.values())

    valid = load_cities()
    by_city = {}
    orphan = 0
    for v in venues:
        key = v.get("city")
        if not key:
            orphan += 1
            continue
        if valid is not None and key not in valid:
            # 城市不在当前清单中，仍按 key 落盘（保证数据不丢），但提示
            pass
        by_city.setdefault(key, []).append(v)

    total = 0
    for key, arr in sorted(by_city.items()):
        out_path = os.path.join(OUTPUT_DIR, f"venue_info_{key}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        total += len(arr)
        print(f"  · venue_info_{key}.json: {len(arr)} 条")

    print(f"\n✅ 已生成 {len(by_city)} 个分城市场馆文件，合计 {total} 条"
          f"（来源 {len(venues)} 条{'，'+str(orphan)+' 条无 city 字段已跳过' if orphan else ''}）")


if __name__ == "__main__":
    main()
