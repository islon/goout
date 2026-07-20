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

为什么只打包「裁剪后的小快照」而不是全量？
    微信小程序主包硬上限 2MB。全量活动(5241 条≈2.8MB)+全量场馆(4701 条≈2.1MB)
    合计≈4.9MB，远超 2MB，会导致小程序无法预览/上传。
    而线上数据走 GitHub raw 实时拉取，打包进小程序的 *.js 仅是「断网兜底」，
    因此只需保留：未结束的近期活动(前 MAX_FALLBACK_ACTIVITIES 条) + 这些活动引用到的场馆。
    既能离线打开有内容，又把主包压到 2MB 以内。
"""

import json
import os
import sys
from datetime import date

# 项目根目录（本脚本位于 scripts/，项目根是其上级）
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")
MINIPROGRAM_DATA_DIR = os.path.join(PROJECT_ROOT, "miniprogram", "data")

# 离线兜底最多打包的活动条数（控制 exhibitions.js 体积，保证主包 < 2MB）
MAX_FALLBACK_ACTIVITIES = 600


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


def normalize_venues(data):
    """统一为数组；字典则转数组并保留原始 key 信息，同时补 id 字段"""
    if isinstance(data, dict):
        items = [{"_key": k, **v} for k, v in data.items()]
    else:
        items = list(data)
    for item in items:
        if "id" not in item and "name" in item:
            item["id"] = item["name"]
    return items


def trim_exhibitions(exhibitions):
    """
    裁剪离线兜底活动：保留「尚未结束」的活动，按开始日期升序取前 N 条。
    end_date >= 今天 视为仍在进行/即将开始；ISO 日期字符串可直接按字典序比较。
    """
    today = date.today().isoformat()
    upcoming = [e for e in exhibitions if e.get("end_date", "") >= today]
    upcoming.sort(key=lambda e: e.get("start_date", ""))
    if len(upcoming) > MAX_FALLBACK_ACTIVITIES:
        upcoming = upcoming[:MAX_FALLBACK_ACTIVITIES]
    dropped = len(exhibitions) - len(upcoming)
    print(f"  · 未结束活动 {len(upcoming)} 条（已裁剪 {dropped} 条历史/超限活动）")
    return upcoming


def select_venues_for(activities, all_venues, per_city=80):
    """
    离线兜底场馆选择策略（兼顾「活动详情对得上」与「每城可浏览」）：

    1) 活动关联的场馆：用「模糊匹配」(活动 venue 含场馆名 或 反之)，
       解决场馆库扩张后「深圳博物馆（市民中心馆）」与库中「深圳博物馆」
       精确匹配失败、导致离线兜底场馆骤降(1042→46)的回归。
    2) 每城保底 per_city 条：即使真机 CDN 不可达(微信 request 合法域名
       白名单/网络问题)，每座城市也能浏览到场馆，避免非深圳城市全空。

    离线兜底只是断网兜底，线上全量仍由「分城市文件」实时拉取补充。
    """
    needed = set()
    for a in activities:
        v = a.get("venue")
        if v:
            needed.add(v.strip())

    selected = []
    selected_names = set()

    # 1) 活动关联场馆（模糊匹配）
    for v in all_venues:
        name = (v.get("name") or "").strip()
        if not name:
            continue
        if name in needed:
            selected.append(v)
            selected_names.add(name)
            continue
        for nv in needed:
            if nv and (name in nv or nv in name):
                selected.append(v)
                selected_names.add(name)
                break

    # 2) 每城保底，确保离线时每城都有场馆可看
    by_city = {}
    for v in all_venues:
        by_city.setdefault(v.get("city", ""), []).append(v)
    for city, vs in by_city.items():
        cnt = sum(1 for v in vs if (v.get("name") or "").strip() in selected_names)
        if cnt < per_city:
            for v in vs:
                nm = (v.get("name") or "").strip()
                if nm and nm not in selected_names:
                    selected.append(v)
                    selected_names.add(nm)
                    cnt += 1
                    if cnt >= per_city:
                        break

    print(f"  · 关联+每城保底场馆 {len(selected)} 条（全量 {len(all_venues)} 条，每城保底 {per_city}）")
    return selected


def sync_exhibitions(data):
    """从裁剪后的活动列表生成 exhibitions.js"""
    out_path = os.path.join(MINIPROGRAM_DATA_DIR, "exhibitions.js")
    header = (
        "// 童行活动数据 - 自动生成（离线兜底·裁剪快照）\n"
        f"// 共 {len(data)} 条活动（来源：islon/goout/output/exhibitions.json）\n"
        "// 注：线上数据走 GitHub raw 实时拉取，本文件仅断网兜底。\n"
        "module.exports = "
    )
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(header)
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    size_kb = os.path.getsize(out_path) // 1024
    print(f"  → {out_path} ({size_kb} KB)")
    return size_kb


def sync_venues(data):
    """从裁剪后的场馆列表生成 venues.js（离线兜底·裁剪快照）

    注意：线上场馆数据走「分城市文件」(output/venue_info_{city}.json) 实时并行拉取，
    因此打包进小程序的兜底只需保留被离线活动引用到的场馆（控制主包体积 < 2MB）。
    """
    out_path = os.path.join(MINIPROGRAM_DATA_DIR, "venues.js")
    header = (
        "// 童行小程序 - 场馆信息本地兜底（离线兜底·裁剪快照）\n"
        f"// 共 {len(data)} 条（来源：islon/goout/output/venue_info.json）\n"
        "// 注：线上数据走 GitHub raw/jsDelivr 实时拉取（分城市文件），本文件仅断网兜底。\n"
        "module.exports = "
    )
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(header)
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    size_kb = os.path.getsize(out_path) // 1024
    print(f"  → {out_path} ({size_kb} KB)")
    return size_kb


def main():
    print("=" * 50)
    print("童行小程序数据同步工具")
    print("=" * 50)

    # 确保输出目录存在
    os.makedirs(MINIPROGRAM_DATA_DIR, exist_ok=True)

    # 1. 活动：全量加载 → 裁剪 → 写文件
    print("\n[1/2] 同步活动数据（裁剪离线兜底）...")
    exhibitions = load_json("exhibitions.json", "exhibitions.json")
    exhibitions_trimmed = trim_exhibitions(exhibitions)
    act_kb = sync_exhibitions(exhibitions_trimmed)

    # 2. 场馆：全量加载 → 仅保留被打包活动引用到的 → 写文件（线上走分城市文件全量）
    print("\n[2/2] 同步场馆数据（仅保留关联场馆）...")
    venues = normalize_venues(load_json("venue_info.json", "venue_info.json"))
    venues_selected = select_venues_for(exhibitions_trimmed, venues)
    ven_kb = sync_venues(venues_selected)

    total_kb = act_kb + ven_kb
    print("\n" + "=" * 50)
    print("✅ 数据同步完成")
    print(f"   打包兜底体积: 活动 {act_kb}KB + 场馆 {ven_kb}KB = {total_kb}KB")
    if total_kb > 1900:
        print("   ⚠️ 接近 2MB 主包上限，建议调小 MAX_FALLBACK_ACTIVITIES")
    else:
        print("   ✓ 主包体积安全（< 2MB）")
    print("=" * 50)


if __name__ == "__main__":
    main()
