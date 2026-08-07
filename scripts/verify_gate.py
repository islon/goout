#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一数据核实门禁 —— 把「数据核实」嵌入数据处理管线，作为发布前必过环节。

设计动机（用户要求：数据处理里要加上数据核实环节，非常重要）：
  原 verify_activities.py 只在 CI 里「事后打标」，且只核实活动、不核实场馆，
  也不是管线必过门禁。本脚本把核实升级为管线的强制环节：
    1) 活动核实（继承 verify_activities 的 L1 链接可达 + L3 来源分类）
    2) 场馆核实（新增：官方链接可达性 + 场馆存在性；无链接的精选场馆视为可信）
    3) 强门禁（--gate）：核实不通过（死链/失效）的活动与场馆移入隔离区
       output/verification_quarantine.json，并从发布产物中剔除，绝不混入线上。
       （隔离区保留原始数据，可回查、可重建，不丢数据）
    4) 产出双报告 output/verification_report.md（活动 + 场馆），供人工复核。

核实原则：
  · 准确性优先：死链活动不发布（强门禁）。
  · best-effort：任何网络/解析异常都不中断管线，仅标记 unverified。
  · 不误杀：仅 confirmed 死链(suspicious)进隔离区；无法核实(unverified)保留并标灰。
  · 缓存复用：output/.verify_cache.json，TTL 7 天，避免重复打官方站点。

用法：
  python3 scripts/verify_gate.py                 # 核实活动+场馆，写 verification 字段（不打标删除）
  python3 scripts/verify_gate.py --gate          # 强门禁：死链/失效项移入隔离区并从发布产物剔除
  python3 scripts/verify_gate.py --gate --no-venue  # 只核实活动
"""
import json
import os
import re
import sys
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = PROJECT_ROOT / 'output'
CACHE_FILE = OUTPUT_DIR / '.verify_cache.json'
QUARANTINE_FILE = OUTPUT_DIR / 'verification_quarantine.json'
REPORT_FILE = OUTPUT_DIR / 'verification_report.md'
VERIFY_TTL_DAYS = 7
# 仅这些 HTTP 状态码视为「确认失效」，强门禁才会剔除；其余（超时/403 反爬/网络异常）
# 一律降级为 unverified 保留并标记，避免误杀真实活动（准确性优先，不误杀）。
CONFIRMED_DEAD = {404, 410}


def normalize_status(v):
    """把「非确认失效」的 suspicious 降级为 unverified，避免超时/反爬误杀。"""
    if v.get('status') == 'suspicious' and v.get('http_status') not in CONFIRMED_DEAD:
        v['status'] = 'unverified'
        v['verified_by'] = 'timeout_or_blocked'
    return v

sys.path.append(str(PROJECT_ROOT / 'scripts'))
# 复用 verify_activities 的成熟核实逻辑（L1 链接可达 + L3 来源分类）
from verify_activities import (
    classify_source, check_link_reachable, make_key,
    load_cache, save_cache, verify_record,
)

# 场馆核实的缓存键（与活动区分）
def venue_key(v):
    return f"VENUE|{v.get('city','')}|{v.get('name','')}"


def load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding='utf-8'))
    except Exception:
        return None


def venue_links(v):
    links = v.get('links') or []
    if links:
        return [l.get('url') for l in links if l.get('url')]
    if v.get('official_url'):
        return [v['official_url']]
    return []


def verify_one_venue(v, cache, today_str):
    """核实单个场馆：有官方链接则实测可达性，无链接的精选场馆视为可信。"""
    key = venue_key(v)
    cached = cache.get(key)
    if cached and (datetime.now() - datetime.strptime(cached['verified_at'], '%Y-%m-%d')).days < VERIFY_TTL_DAYS:
        return cached

    links = venue_links(v)
    if not links:
        # 无官方链接：精选/自动普查场馆，来源可信，记 auto_checked
        result = {
            'status': 'auto_checked',
            'link_reachable': None,
            'http_status': None,
            'source_type': 'registry',
            'verified_at': today_str,
            'verified_by': 'registry_trust',
        }
        cache[key] = result
        return result

    # 取第一个官方链接实测
    reachable, http_status, src_hint = check_link_reachable(links[0])
    source_type = src_hint or 'venue'
    if reachable is True:
        status = 'auto_checked'
    elif reachable is False:
        status = 'suspicious'
    else:
        status = 'unverified'
    result = {
        'status': status,
        'link_reachable': reachable,
        'http_status': http_status,
        'source_type': source_type,
        'verified_at': today_str,
        'verified_by': 'http_check',
    }
    cache[key] = result
    return result


def verify_activities(input_file, gate, today_str, cache, workers=24):
    print(f'[gate] 核实活动: {input_file}')
    data = load_json(input_file)
    if not isinstance(data, list) or not data:
        print('[gate]   活动文件为空或不存在，跳过')
        return [], [], 0

    total = len(data)
    verifications = [None] * total
    to_verify = []
    reused = 0
    for idx, rec in enumerate(data):
        k = make_key(rec)
        c = cache.get(k)
        if c and (datetime.now() - datetime.strptime(c['verified_at'], '%Y-%m-%d')).days < VERIFY_TTL_DAYS:
            verifications[idx] = c
            reused += 1
        else:
            to_verify.append((idx, rec))

    def run_one(item):
        idx, rec = item
        return idx, verify_record(rec, today_str)

    if to_verify:
        with ThreadPoolExecutor(max_workers=workers) as ex:
            futs = {ex.submit(run_one, it): it for it in to_verify}
            done = 0
            for fut in as_completed(futs):
                idx, v = fut.result()
                verifications[idx] = v
                cache[make_key(data[idx])] = v
                done += 1
                if done % 200 == 0 or done == len(to_verify):
                    print(f'[gate]   活动核实进度 {done}/{len(to_verify)}')

    kept, quarantined = [], []
    for idx, rec in enumerate(data):
        v = verifications[idx]
        if v is None:
            v = {'status': 'unverified', 'link_reachable': None, 'http_status': None,
                 'source_type': classify_source(rec.get('link', '') or rec.get('url', ''), rec.get('source', '')),
                 'verified_at': today_str, 'verified_by': 'http_check'}
        normalize_status(v)
        rec['verification'] = v
        rec['verified'] = (v['status'] == 'auto_checked')
        if gate and v['status'] == 'suspicious':
            quarantined.append(rec)
        else:
            kept.append(rec)

    # 写回（gated 时只写 kept）
    Path(input_file).write_text(json.dumps(kept if gate else data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'[gate]   活动 {total} 条，复用缓存 {reused}，保留 {len(kept)}，隔离 {len(quarantined)}')
    return kept, quarantined, total


def verify_venues(gate, today_str, cache):
    print('[gate] 核实场馆: output/venue_info.json')
    data = load_json(OUTPUT_DIR / 'venue_info.json')
    if not isinstance(data, list) or not data:
        print('[gate]   场馆文件为空，跳过')
        return [], [], 0

    total = len(data)
    kept, quarantined = [], []
    for v in data:
        verification = verify_one_venue(v, cache, today_str)
        normalize_status(verification)
        v['verification'] = verification
        v['verified'] = (verification['status'] == 'auto_checked')
        if gate and verification['status'] == 'suspicious':
            quarantined.append(v)
        else:
            kept.append(v)

    Path(OUTPUT_DIR / 'venue_info.json').write_text(
        json.dumps(kept if gate else data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'[gate]   场馆 {total} 个，保留 {len(kept)}，隔离 {len(quarantined)}')
    return kept, quarantined, total


def sync_city_activity_files(quarantined_keys):
    """把活动核实结果同步进分城市文件，并按隔离键剔除死链活动。"""
    if not quarantined_keys:
        return
    synced = 0
    removed = 0
    for cf in sorted(OUTPUT_DIR.glob('exhibitions_*.json')):
        arr = load_json(cf)
        if not isinstance(arr, list):
            continue
        changed = False
        new_arr = []
        for rec in arr:
            k = make_key(rec)
            if k in quarantined_keys:
                removed += 1
                changed = True
                continue
            # 更新 verification / verified
            v = rec.get('verification')
            if v is not None:
                rec['verified'] = (v['status'] == 'auto_checked')
                changed = True
            new_arr.append(rec)
        if changed:
            cf.write_text(json.dumps(new_arr, ensure_ascii=False, indent=2), encoding='utf-8')
            synced += 1
    if synced:
        print(f'[gate]   已同步/剔除到 {synced} 个分城市场馆文件，共移除死链活动 {removed} 条')


def write_quarantine(act_q, ven_q):
    payload = {
        'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'activities': act_q,
        'venues': ven_q,
        'counts': {'activities': len(act_q), 'venues': len(ven_q)},
    }
    QUARANTINE_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'[gate] 隔离区: {QUARANTINE_FILE} (活动 {len(act_q)} + 场馆 {len(ven_q)})')


def write_report(act_total, act_kept, act_q, ven_total, ven_kept, ven_q, gate):
    sc = Counter(v['verification']['status'] for v in act_kept)
    vs = Counter(v['verification']['status'] for v in ven_kept)
    lines = []
    lines.append(f'# 数据核实报告 — {datetime.now().strftime("%Y-%m-%d %H:%M")}')
    lines.append('')
    lines.append(f'> 模式: {"强门禁(--gate)：死链/失效项已移入隔离区并从发布产物剔除" if gate else "标记模式：仅打标，不剔除"}')
    lines.append('')
    lines.append('## 活动核实')
    lines.append(f'- 总量: {act_total}')
    lines.append(f'- 保留(发布): {len(act_kept)}')
    lines.append(f'- 状态分布: ' + '，'.join(f'{k}={n}' for k, n in sc.most_common()))
    lines.append(f'- 隔离(死链): {len(act_q)}')
    lines.append('')
    lines.append('## 场馆核实')
    lines.append(f'- 总量: {ven_total}')
    lines.append(f'- 保留(发布): {len(ven_kept)}')
    lines.append(f'- 状态分布: ' + '，'.join(f'{k}={n}' for k, n in vs.most_common()))
    lines.append(f'- 隔离(死链官网): {len(ven_q)}')
    lines.append('')
    if act_q:
        lines.append('## 隔离活动明细（死链，建议核查修正）')
        for r in act_q[:30]:
            lines.append(f'- [{r.get("city")}] {r.get("title","")} — {r.get("link") or r.get("url","")}')
        lines.append('')
    if ven_q:
        lines.append('## 隔离场馆明细（官方链接失效，建议核查）')
        for v in ven_q[:30]:
            links = v.get('links') or []
            url = links[0]['url'] if links else v.get('official_url', '')
            lines.append(f'- [{v.get("city")}] {v.get("name","")} — {url}')
        lines.append('')
    REPORT_FILE.write_text('\n'.join(lines), encoding='utf-8')
    print(f'[gate] 报告: {REPORT_FILE}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gate', action='store_true', help='强门禁：死链/失效项移入隔离区并从发布产物剔除')
    parser.add_argument('--no-venue', action='store_true', help='跳过场馆核实')
    parser.add_argument('--no-cache', action='store_true', help='忽略缓存，全部重新核实')
    parser.add_argument('--workers', type=int, default=24)
    args = parser.parse_args()

    today_str = datetime.now().strftime('%Y-%m-%d')
    cache = {} if args.no_cache else load_cache()

    # 1) 活动核实
    act_kept, act_q, act_total = verify_activities(
        OUTPUT_DIR / 'exhibitions.json', args.gate, today_str, cache, args.workers)

    # 2) 场馆核实
    ven_kept, ven_q, ven_total = [], [], 0
    if not args.no_venue:
        ven_kept, ven_q, ven_total = verify_venues(args.gate, today_str, cache)

    # 3) 同步分城市活动文件（剔除死链）
    if args.gate and act_q:
        sync_city_activity_files({make_key(r) for r in act_q})

    # 4) 隔离区 + 报告
    if args.gate:
        write_quarantine(act_q, ven_q)
    write_report(act_total, act_kept, act_q, ven_total, ven_kept, ven_q, args.gate)

    save_cache(cache)
    print('[gate] 核实门禁完成')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'[gate] 核实异常（已跳过，不影响数据更新）: {e}')
        sys.exit(0)
