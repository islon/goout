#!/usr/bin/env python3
"""
sync_miniprogram_data.py — 将 output/ 的最新数据同步到 miniprogram/data/

用法：
    python scripts/sync_miniprogram_data.py

功能：
    从 output/exhibitions.json 和 output/venue_info.json 重新生成：
      - miniprogram/data/exhibitions.js   （活动离线兜底）
      - miniprogram/data/venues.js         （场馆离线兜底）

数据流向（单一事实来源）：
    scripts/main.py → output/exhibitions.json / output/venue_info.json
                    ↘ 本脚本同步 → miniprogram/data/*.js（小程序打包兜底）

    运行时：
      · Web 版（index.html 等）：fetch('output/...') ← GitHub Pages 直接提供
      · 小程序运行时：wx.request(raw.githubusercontent.com/.../main/output/) ← 实时拉取
      · 小程序离线兜底：require('./data/*.js') ← 本文件生成的快照

本脚本保证「更新 output 时，小程序打包数据也同时刷新」。
"""

import json
import os
import sys

# 项目根目录（本脚本位于 scripts/，项目根是其上级）
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")
MINIPROGRAM_DATA_DIR = os.path.join(PROJECT_ROOT, "miniprogram", "data")


def load_json(path, name):
    """加载 JSON 文件，失败则报错退出"""
    full_path = os.path.join(OUTPUT_DIR, path)
    if not os.path.exists(full_path):
        print(f"❌ {name} 不存在: {full_path}")
        sys.exit(1)
    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"✅ 加载 {name}: {len(data)} 条")
    return data


def sync_exhibitions(data):
    """从 exhibitions.json 生成 exhibitions.js"""
    out_path = os.path.join(MINIPROGRAM_DATA_DIR, "exhibitions.js")
    header = (
        "// 童行活动数据 - 自动生成\n"
        f"// 共 {len(data)} 条活动（来源：islon/goout/output/exhibitions.json）\n"
        "module.exports = "
    )
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(header)
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    size_kb = os.path.getsize(out_path) // 1024
    print(f"  → {out_path} ({size_kb} KB)")


def sync_venues(data):
    """
    从 venue_info.json（数组格式）生成 venues.js。
    每条记录追加 id 字段（= name），保持与现有 venues.js 格式一致。
    """
    # 确保 data 是数组；如果是字典，转数组并保留原始 key 信息
    if isinstance(data, dict):
        items = [{"_key": k, **v} for k, v in data.items()]
    else:
        items = list(data)

    # 追加 id 字段（以 name 作为唯一标识）
    for item in items:
        if "id" not in item and "name" in item:
            item["id"] = item["name"]

    out_path = os.path.join(MINIPROGRAM_DATA_DIR, "venues.js")
    header = (
        "// 童行小程序 - 场馆信息本地兜底\n"
        f"// 共 {len(items)} 条（来源：islon/goout/output/venue_info.json）\n"
        "module.exports = "
    )
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(header)
        json.dump(items, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    size_kb = os.path.getsize(out_path) // 1024
    print(f"  → {out_path} ({size_kb} KB)")


def main():
    print("=" * 50)
    print("童行小程序数据同步工具")
    print("=" * 50)

    # 确保输出目录存在
    os.makedirs(MINIPROGRAM_DATA_DIR, exist_ok=True)

    # 1. 同步活动数据
    print("\n[1/2] 同步活动数据...")
    exhibitions = load_json("exhibitions.json", "exhibitions.json")
    sync_exhibitions(exhibitions)

    # 2. 同步场馆数据
    print("\n[2/2] 同步场馆数据...")
    venues = load_json("venue_info.json", "venue_info.json")
    sync_venues(venues)

    print("\n" + "=" * 50)
    print("✅ 数据同步完成")
    print("   网页版 & 小程序打包数据已统一更新。")
    print("=" * 50)


if __name__ == "__main__":
    main()
