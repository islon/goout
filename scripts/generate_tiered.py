#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成「分级活动」快照，供小程序三级优先加载：

  小程序首屏需要从 GitHub raw 拉数据。全量分城市文件共约 4910 条、需 10 个并行请求，
  在中国大陆 raw.githubusercontent.com 常被拦截/超时，首屏体感很慢。
  本脚本把活动按「时间紧迫度」切成三级，小程序启动时按优先级依次拉取：

    Tier 1  近期活动 exhibitions_recent.json
            = 每个城市「未结束且最早举办」的前 N 条（默认 80），合并约 800 条。
            → 首屏最优先拉取（用户最关心「最近有什么可去的」），单请求、体积极小。
    Tier 2  后续活动  exhibitions_{城市}.json（分城市文件，沿用既有逻辑）
            = 全部分城市的完整当前活动（含 Tier1）。小程序在后台静默并行拉取补全。
    Tier 3  历史活动 exhibitions_past.json
            = 已结束(end_date < 今天)的活动，按结束时间倒序。
            → 优先级最低，最后再拉取，不挤占首屏带宽。

  加载顺序（见 miniprogram/app.js 的 loadStagedData）：
    先 recent（秒出首屏）→ 再全量分城市（补全当前活动）→ 最后 past（历史收尾）。

产物：output/exhibitions_recent.json、output/exhibitions_past.json
（结构与分城市文件一致，含 booking_method / verified 等全部字段）
"""
import json
import os
import glob
from datetime import date

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'output')
RECENT_FILE = os.path.join(OUTPUT_DIR, 'exhibitions_recent.json')
PAST_FILE = os.path.join(OUTPUT_DIR, 'exhibitions_past.json')
PER_CITY_CAP = 80  # 每城取最早未结束的前 N 条（Tier 1）


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
        print('[generate_tiered] 未找到任何 exhibitions_*.json，退出')
        return

    today = date.today()

    # 收集所有活动，按所属文件归类（用于推断城市兜底）
    per_city_recent = {}
    past = []
    for fp in files:
        # 跳过本脚本自己生成的快照文件，避免自我 glob 导致重复计数
        stem = os.path.basename(fp).replace('exhibitions_', '').replace('.json', '')
        if stem in ('recent', 'past'):
            continue
        try:
            with open(fp, 'r', encoding='utf-8') as f:
                arr = json.load(f)
        except Exception as e:
            print('[generate_tiered] 读取失败，跳过:', fp, e)
            continue
        if not isinstance(arr, list):
            arr = list(arr.values())
        city = os.path.basename(fp).replace('exhibitions_', '').replace('.json', '')

        # Tier 1 「近期」排序键：让「离当前时间最近的活动」排在最前
        #   - 正在进行中(start<=今天<=end)：最优先，按结束日期升序（最快结束的在前）
        #   - 即将开始(start>今天)：其次，按开始日期升序（最快开始的在前）
        # 这样即使某城有大量"很早开始、至今仍在展"的长期展览，首屏也优先露出
        # 正在发生 / 马上开始的活动，而不是最早开场的老活动。
        def recent_key(x):
            sd = parse_date(x.get('start_date'))
            ed = parse_date(x.get('end_date') or x.get('start_date'))
            if sd and sd <= today:
                return (0, ed or sd)          # 正在进行：结束越早越靠前
            return (1, sd or date.max)         # 即将开始：开始越早越靠前

        alive = []
        for x in arr:
            sd = parse_date(x.get('start_date'))
            ed = parse_date(x.get('end_date') or x.get('start_date'))
            if ed and ed < today:
                # 已结束 → 归入历史 Tier 3（保留原城市，没有则用文件名推断）
                if not x.get('city'):
                    x = dict(x, city=city)
                past.append(x)
            elif ed and ed >= today:
                alive.append(x)
        alive.sort(key=recent_key)
        per_city_recent[city] = alive[:PER_CITY_CAP]

    # ---- Tier 1：近期活动（每个城市离当前最近的前 N 条），按 recent_key 合并 ----
    def merged_key(x):
        sd = parse_date(x.get('start_date'))
        ed = parse_date(x.get('end_date') or x.get('start_date'))
        if sd and sd <= today:
            return (0, ed or sd)
        return (1, sd or date.max)

    merged_recent = []
    for city in sorted(per_city_recent.keys()):
        merged_recent.extend(per_city_recent[city])
    merged_recent.sort(key=merged_key)

    with open(RECENT_FILE, 'w', encoding='utf-8') as f:
        json.dump(merged_recent, f, ensure_ascii=False, indent=2)

    # ---- Tier 3：历史活动（已结束），按 end_date 倒序（最近的过往在前）----
    past.sort(key=lambda x: (x.get('end_date') or '0000'), reverse=True)
    with open(PAST_FILE, 'w', encoding='utf-8') as f:
        json.dump(past, f, ensure_ascii=False, indent=2)

    recent_kb = os.path.getsize(RECENT_FILE) / 1024
    past_kb = os.path.getsize(PAST_FILE) / 1024
    print(f'[generate_tiered] 已生成 {RECENT_FILE}')
    print(f'  Tier1 近期活动: {len(merged_recent)} 条 (各城合计取 {sum(len(v) for v in per_city_recent.values())})，{recent_kb:.1f} KB')
    print(f'[generate_tiered] 已生成 {PAST_FILE}')
    print(f'  Tier3 历史活动: {len(past)} 条，{past_kb:.1f} KB')


if __name__ == '__main__':
    main()
