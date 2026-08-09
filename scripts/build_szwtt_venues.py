#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把深圳政府在线·文体通 (sz.gov.cn/szzt2010/szwtt) 的场馆目录批量纳入 auto_venues.json。
数据来源：search.gd.gov.cn JSONP 接口（sites=755001，文化场馆 category_id=157970，体育场馆=157971）。
已通过 TLS 曲线绕过从接口抓取并落盘到 /tmp/whcg.json / /tmp/tycg.json。
本脚本：解析 -> 字段映射 -> 按名称对现有 curated+auto 去重 -> 追加到 scripts/auto_venues.json。
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import venue_registry  # 用于读取 curated VENUES 的名称/别名做去重

SOURCE_LABEL = "深圳政府-文体通"
AUTO_PATH = os.path.join(ROOT, 'scripts', 'auto_venues.json')


def strip_html(text):
    if not text:
        return ''
    t = re.sub(r'<[^>]+>', '', text)
    t = t.replace('&middot;', '·').replace('&nbsp;', ' ').replace('&amp;', '&')
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def je(x):
    try:
        return json.loads(x.get('json_ext', '{}')) or {}
    except Exception:
        return {}


TYPE_MAP_WH = {  # 文化场馆 cglx -> 项目类型词表
    '博物馆': '博物馆',
    '图书馆': '图书馆',
    '美术馆': '美术馆',
    '展览馆': '文化中心',
    '戏剧院': '演出场馆',
    '其他': '文化中心',
}


def map_type(cat, j):
    if cat == 'whcg':
        return TYPE_MAP_WH.get(j.get('cglx', ''), '其他')
    return '体育中心'  # 体育场馆统一归为体育中心


def original_type(cat, j):
    if cat == 'whcg':
        return j.get('cglx', '')
    lx = j.get('lx_string') or (j.get('lx')[0] if isinstance(j.get('lx'), list) else '')
    return lx or ''


def build_entries():
    entries = []
    for cat, fname in [('whcg', '/tmp/whcg.json'), ('tycg', '/tmp/tycg.json')]:
        data = json.load(open(fname, encoding='utf-8'))
        for x in data.get('results', []):
            j = je(x)
            name = strip_html(j.get('cgmc', ''))
            if not name:
                continue
            district = (j.get('ssq') or '').strip()
            address = strip_html(j.get('dz', ''))
            dtz = (j.get('dtz') or '').strip()
            ggjt = strip_html(j.get('ggjt', ''))
            transport = (f"地铁{dtz}；" if dtz else '') + ggjt
            fwsj = strip_html(j.get('fwsj', ''))
            desc = strip_html(j.get('cgjs', ''))
            otype = original_type(cat, j)
            vtype = map_type(cat, j)
            fee = '免费' if cat == 'whcg' else '收费'
            detail = x.get('url') or x.get('post_url') or ''
            links = [{'url': detail, 'label': '深圳政府在线·场馆详情'}] if detail else []
            hi = [v for v in [otype, district] if v]
            entries.append({
                'source_code': f"szwt_{x.get('id')}",
                'name': name,
                'source': SOURCE_LABEL,
                'city': 'shenzhen',
                'district': district,
                'type': vtype,
                'address': address,
                'transport': transport,
                'fee': fee,
                'description': desc,
                'service_time': fwsj,
                'official_url': '',
                'links': links,
                'highlights': hi,
                'aliases': [],
                'status': 'auto',
                'activity_count': 0,
            })
    return entries


def dedup_keys():
    keys = set()
    # 现有 auto 名称
    if os.path.exists(AUTO_PATH):
        for v in json.load(open(AUTO_PATH, encoding='utf-8')):
            keys.add(v.get('name', '').strip().lower())
    # curated VENUES 名称 + 别名
    for v in venue_registry.get_all_venues():
        keys.add(v.get('name', '').strip().lower())
        for a in v.get('aliases', []):
            keys.add(a.strip().lower())
    return keys


def main():
    entries = build_entries()
    print(f"接口解析到场馆: {len(entries)}")
    existing = dedup_keys()
    auto = json.load(open(AUTO_PATH, encoding='utf-8')) if os.path.exists(AUTO_PATH) else []
    added, skipped = [], []
    seen_names = set(v.get('name', '').strip().lower() for v in auto)
    for e in entries:
        nm = e['name'].strip().lower()
        if nm in existing or nm in seen_names:
            skipped.append(e['name'])
            continue
        auto.append(e)
        seen_names.add(nm)
        added.append(e['name'])
    json.dump(auto, open(AUTO_PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f"新增: {len(added)}  跳过(已收录): {len(skipped)}")
    print("--- 新增场馆示例(前15) ---")
    for n in added[:15]:
        print("  +", n)
    if skipped:
        print("--- 跳过(已存在于 curated/auto) ---")
        for n in skipped:
            print("  -", n)


if __name__ == '__main__':
    main()
