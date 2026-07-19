#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
童行(goout) 活动数据健康巡检脚本
- 联网抓取 https://islon.github.io/goout/ 各城市线上数据
- 检查: 完全重复(可见冗余) / 已过期陈旧记录 / 日期倒挂 / 年份异常 /
        fee 取值非法 / 描述过短 / 缺来源链接 / 缺必填字段
- 前端展示规则: start_date <= 当日 <= end_date 才会显示; 因此 end_date < 今天 的记录
  用户端看不到, 归类为"陈旧记录"(数据源未清理); 而重复项若在有效期内, 用户会真实看到重复卡片。
用法: python3 check_activity_data.py
"""
import json, datetime, collections, hashlib, urllib.request, sys

BASE = "https://islon.github.io/goout/output/exhibitions_{}.json"
CITIES = {'shenzhen': '深圳', 'beijing': '北京', 'guangzhou': '广州',
          'shanghai': '上海', 'hangzhou': '杭州'}
ALLOWED_FEE = {'免费', '免费需预约', '收费', '部分免费', '需购票'}
TODAY = datetime.date.today()


def fetch(city):
    url = BASE.format(city)
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.loads(r.read().decode('utf-8'))


def sig(x):
    return hashlib.md5(json.dumps(x, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def check_city(city, data):
    iss = collections.defaultdict(list)

    # 完全重复(全字段一致)
    full = collections.defaultdict(list)
    for x in data:
        full[sig(x)].append(x)
    for v in full.values():
        if len(v) > 1:
            x = v[0]
            try:
                live = datetime.date.fromisoformat(x.get('end_date', '')) >= TODAY
            except Exception:
                live = True
            tag = '会展示' if live else '已过期'
            iss['完全重复'].append(
                (len(v) - 1,
                 f"x{len(v)}[{tag}] {x.get('title','')[:34]} | {x.get('venue','')[:18]} | {x.get('start_date')}~{x.get('end_date')}"))

    for x in data:
        t = x.get('title') or x.get('name') or 'N/A'
        sd, ed = x.get('start_date', ''), x.get('end_date', '')
        try:
            s = datetime.date.fromisoformat(sd)
            e = datetime.date.fromisoformat(ed)
            if e < s:
                iss['日期倒挂'].append((1, f"{t[:30]} | {sd}~{ed}"))
            if s.year not in (2025, 2026, 2027):
                iss['年份异常'].append((1, f"{t[:30]} | {sd}"))
            if e < TODAY:
                iss['已过期陈旧记录'].append((1, f"{t[:28]} | 结束{ed}"))
        except Exception:
            iss['日期缺失或格式错误'].append((1, f"{t[:30]} | {sd}~{ed}"))
        if x.get('fee') and x['fee'] not in ALLOWED_FEE:
            iss['fee取值非法'].append((1, f"{t[:30]} | {x['fee']}"))
        if len((x.get('description') or '')) < 10:
            iss['描述过短'].append((1, f"{t[:30]}"))
        if not (x.get('link') or x.get('url')):
            iss['缺来源链接'].append((1, f"{t[:30]}"))
        for f in ('title', 'venue', 'start_date', 'end_date', 'city'):
            if not x.get(f):
                iss['缺必填字段'].append((1, f"{t[:26]} 缺[{f}]"))
    return iss


def main():
    print(f"童行活动数据巡检  日期: {TODAY}\n{'='*50}")
    grand = 0
    visible_bug = 0
    for city, cn in CITIES.items():
        try:
            data = fetch(city)
        except Exception as ex:
            print(f"\n【{cn}】抓取失败: {ex}")
            continue
        iss = check_city(city, data)
        cnt = sum(sum(w for w, _ in v) for v in iss.values())
        grand += cnt
        vb = sum(w for _, line in iss.get('完全重复', []) for w in [line.count('')] if '[会展示]' in line)
        vb = sum(w for w, line in iss.get('完全重复', []) if '[会展示]' in line)
        visible_bug += vb
        print(f"\n【{cn} {city}】共 {len(data)} 条，问题 {cnt} 处"
              + (f"（其中会展示的重复 {vb} 处）" if vb else ""))
        if not cnt:
            print("   ✓ 无异常")
            continue
        for k, v in iss.items():
            print(f"  ▶ {k}: {sum(w for w, _ in v)} 处")
            for _, line in v[:15]:
                print(f"      - {line}")
            if len(v) > 15:
                print(f"      ... 另有 {len(v)-15} 组")
    print(f"\n{'#'*50}\n合计问题: {grand} 处；用户可见的重复卡片: {visible_bug} 处")
    return grand


if __name__ == '__main__':
    sys.exit(0 if main() == 0 else 1)
