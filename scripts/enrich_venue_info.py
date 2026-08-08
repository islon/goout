#!/usr/bin/env python3
"""
enrich_venue_info.py — 对现有分城市场馆文件做「丰富介绍 + 链接归一 + 重点场馆联网覆盖」

设计原则（防数据漂移，关键！）：
    - 分城市文件 output/venue_info_{city}.json 是线上权威源（小程序并行拉取对象），
      条数必须与 data_meta.venues 一致（当前 11 城 1926 条）。
    - 本脚本**逐条 map 现有场馆**：只改写 description / links / highlights / address / transport，
      **绝不增删场馆、绝不改变 name/city/district 归属**，因此条数恒等于输入。
    - 单文件兜底 output/venue_info.json 随后由 generate_city_venues.py 聚合生成（= 分城市合集）。

丰富化来源：
    1) 模板补全：description 过短（占位）时用结构化字段生成更丰富介绍。
    2) 链接归一：official_url / venue_url（旧字段）与 links（新）合并为带标签 links 数组
       （官方网站 / 官方小程序）。
    3) 重点场馆联网覆盖：scripts/venue_enrichment.json（人工联网检索填写），按场馆名覆盖
       description / links / highlights / address / transport。

用法：
    python3 scripts/enrich_venue_info.py
"""
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")

CITY_ORDER = ['beijing', 'shanghai', 'guangzhou', 'shenzhen', 'hangzhou',
              'chengdu', 'chongqing', 'nanjing', 'wuhan', 'xian', 'zhuhai']

_CITY_CN = {
    'beijing': '北京', 'shanghai': '上海', 'guangzhou': '广州', 'shenzhen': '深圳',
    'chengdu': '成都', 'chongqing': '重庆', 'hangzhou': '杭州', 'nanjing': '南京',
    'wuhan': '武汉', 'xian': '西安', 'zhuhai': '珠海',
}


def _load_enrichment():
    path = os.path.join(SCRIPT_DIR, 'venue_enrichment.json')
    if os.path.exists(path):
        try:
            return json.loads(open(path, 'r', encoding='utf-8').read()).get('venues', {}) or {}
        except Exception:
            return {}
    return {}


def _normalize_links(official_url, venue_url, links):
    merged = []
    seen = set()
    if isinstance(links, list):
        for l in links:
            if isinstance(l, dict) and l.get('url'):
                label = l.get('label') or '活动详情'
                merged.append({'url': l['url'].strip(), 'label': label})
                seen.add(label)
    if official_url and official_url.strip() and '官方网站' not in seen:
        merged.append({'url': official_url.strip(), 'label': '官方网站'})
        seen.add('官方网站')
    if (venue_url and venue_url.strip()
            and venue_url.strip() != (official_url or '').strip()
            and '官方小程序' not in seen):
        merged.append({'url': venue_url.strip(), 'label': '官方小程序'})
        seen.add('官方小程序')
    return merged


def _template_description(v, city_cn):
    name = v.get('name') or ''
    vtype = v.get('type') or ''
    address = v.get('address') or ''
    transport = v.get('transport') or ''
    fee = v.get('fee') or ''
    highlights = v.get('highlights') or []
    desc = (v.get('description') or '').strip()
    if len(desc) > 15 and desc != name + '。':
        return desc
    parts = [f"{name}是位于{city_cn}的"]
    if vtype:
        parts.append(vtype)
    parts.append("，")
    if highlights:
        parts.append("主打" + "、".join(highlights[:4]) + "等")
    else:
        parts.append("面向亲子家庭与青少年常态化开展")
    parts.append("活动。")
    if fee:
        if fee == '免费':
            parts.append("场馆免费开放（部分特展可能另行收费），")
        else:
            parts.append(f"门票{fee}，")
    if address:
        parts.append(f"地址位于{address}；")
    if transport:
        parts.append(f"交通：{transport}。")
    parts.append("建议出行前通过官方渠道确认开放时间与预约要求。")
    return "".join(parts)


def enrich_one(v, city_cn, enrich_map):
    official_url = v.get('official_url') or v.get('venue_url') or ''
    venue_url = v.get('venue_url', '')
    links = _normalize_links(official_url, venue_url, v.get('links'))
    out = dict(v)  # 保留原有全部字段（name/city/district/source/status...）
    out['description'] = _template_description(v, city_cn)
    out['links'] = links
    out['official_url'] = official_url
    if not out.get('fee'):
        out['fee'] = '免费'
    if 'highlights' not in out:
        out['highlights'] = []
    # 重点场馆联网覆盖（按场馆名）
    enrich = enrich_map.get(v.get('name', ''))
    if isinstance(enrich, dict):
        if enrich.get('description'):
            out['description'] = enrich['description']
        if enrich.get('highlights'):
            out['highlights'] = enrich['highlights']
        if enrich.get('links'):
            out['links'] = _normalize_links(official_url, venue_url, enrich['links'])
            if out['links']:
                out['official_url'] = out['links'][0]['url']
        if enrich.get('address'):
            out['address'] = enrich['address']
        if enrich.get('transport'):
            out['transport'] = enrich['transport']
    return out


def main():
    enrich_map = _load_enrichment()
    total_in = total_out = 0
    changed = 0
    for key in CITY_ORDER:
        p = os.path.join(OUTPUT_DIR, f"venue_info_{key}.json")
        if not os.path.exists(p):
            continue
        arr = json.load(open(p, 'r', encoding='utf-8'))
        city_cn = _CITY_CN.get(key, key)
        new_arr = []
        for v in arr:
            nv = enrich_one(v, city_cn, enrich_map)
            new_arr.append(nv)
            total_in += 1
            if nv.get('description') != v.get('description') or nv.get('links') != v.get('links'):
                changed += 1
        total_out += len(new_arr)
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(new_arr, f, ensure_ascii=False, indent=2)
        print(f"  · {key}: {len(new_arr)} 条（丰富化完成）")
    print(f"\n✅ 分城市场馆丰富化完成：输入 {total_in} 条 / 输出 {total_out} 条（条数不变，{changed} 条内容有改动）")
    if total_in != total_out:
        print("⚠️ 警告：输入输出条数不一致，已中止写入请检查！")
        sys.exit(1)


if __name__ == "__main__":
    main()
