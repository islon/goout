#!/usr/bin/env python3
"""
enrich_activity_links.py — 将活动数据中的旧 link/url 字段归一为 links 数组

背景：
    - 原活动数据只有单链接 link/url（多为本地宝/官网活动页）。
    - 新 schema 用 links 数组支持「官方小程序 / 活动详情 / 新闻报道」等分类。
    - 本脚本对 output/ 下所有活动文件做结构归一：若已有 links 数组则保留；
      否则把旧 link/url 归一成 links=[{url,label:'活动详情'}]。
    - 不增删活动、不改其他字段，幂等可重复运行。

覆盖文件：
    output/exhibitions.json（全量）
    output/exhibitions_{city}.json（分城市，线上小程序/网页并行拉取对象）
    output/exhibitions_recent.json / exhibitions_past.json（网页近期/往期）

用法：
    python3 scripts/enrich_activity_links.py
"""
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")


def normalize_one(a):
    links = a.get('links')
    if isinstance(links, list) and any(l.get('url') for l in links if isinstance(l, dict)):
        # 已有有效 links 数组，保留
        return a, False
    link = (a.get('link') or a.get('url') or '').strip()
    if link:
        a['links'] = [{'url': link, 'label': '活动详情'}]
        return a, True
    # 无链接，不强行造
    return a, False


def process_file(path):
    if not os.path.exists(path):
        return 0, 0
    arr = json.load(open(path, 'r', encoding='utf-8'))
    if isinstance(arr, dict):
        arr = arr.get('exhibitions', arr.get('activities', []))
    changed = 0
    for a in arr:
        if isinstance(a, dict):
            _, c = normalize_one(a)
            if c:
                changed += 1
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(arr, f, ensure_ascii=False, indent=2)
    return len(arr), changed


def main():
    targets = ['exhibitions.json', 'exhibitions_recent.json', 'exhibitions_past.json']
    # 分城市
    import glob
    targets += [os.path.basename(p) for p in glob.glob(os.path.join(OUTPUT_DIR, 'exhibitions_*.json'))]
    total = changed_total = 0
    for name in targets:
        p = os.path.join(OUTPUT_DIR, name)
        n, c = process_file(p)
        if n:
            print(f"  · {name}: {n} 条，归一 {c} 条")
            total += n
            changed_total += c
    print(f"\n✅ 活动链接归一完成：共 {total} 条活动文件处理，{changed_total} 条补入 links（其余已有）")


if __name__ == "__main__":
    main()
