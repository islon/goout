#!/usr/bin/env python3
"""
合并核实结果到 exhibitions.json
1. 重测所有 link_reachable=False 的记录（用GET替代HEAD，更准确）
2. 合并 L2 WebSearch 抽样验证结果（4个 verification_websearch_*.json）
3. 重新统计并输出报告
"""

import json
import re
import subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter
from urllib.parse import urlparse

PROJECT_ROOT = Path(__file__).parent.parent
EXHIBITIONS_FILE = PROJECT_ROOT / 'output' / 'exhibitions.json'
WEBSEARCH_FILES = [
    PROJECT_ROOT / 'output' / 'verification_websearch_beijing_shanghai.json',
    PROJECT_ROOT / 'output' / 'verification_websearch_guangzhou_shenzhen.json',
    PROJECT_ROOT / 'output' / 'verification_websearch_hangzhou_nanjing_wuhan.json',
    PROJECT_ROOT / 'output' / 'verification_websearch_chengdu_chongqing_xian.json',
]

def check_link_with_get(url, timeout=10):
    """用 GET 方法验证 link（只取前几百字节，避免下载大文件）"""
    if not url:
        return None, None
    cmd = [
        'curl', '-sL',
        '--connect-timeout', str(timeout),
        '--max-time', str(timeout + 5),
        '-r', '0-1023',  # 只取前1KB，避免下载整个页面
        '-A', 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        '-o', '/dev/null',
        '-w', '%{http_code}|%{url_effective}',
        url
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 10)
        if result.returncode != 0:
            return False, None
        output = result.stdout.strip()
        if '|' in output:
            status_str, final_url = output.split('|', 1)
            try:
                status = int(status_str)
                reachable = 200 <= status < 400
                return reachable, status
            except ValueError:
                return False, None
        return False, None
    except Exception:
        return False, None


def load_websearch_results():
    """加载4个WebSearch验证文件，返回 id -> verification dict 和 (title,venue) -> verification dict"""
    ws_by_id = {}
    ws_by_title = {}
    for fp in WEBSEARCH_FILES:
        if not fp.exists():
            print(f'警告: 文件不存在 {fp}')
            continue
        with open(fp, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for item in data:
            if item.get('id') is not None:
                ws_by_id[item['id']] = item
            else:
                # 用 title+venue 作为匹配键
                key = (item.get('title', ''), item.get('venue', ''))
                ws_by_title[key] = item
    return ws_by_id, ws_by_title


def main():
    print(f'读取: {EXHIBITIONS_FILE}')
    with open(EXHIBITIONS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total = len(data)
    print(f'总计 {total} 条')
    
    # 1. 收集需要重测的记录（link_reachable=False）
    print()
    print('=== 第1步：重测死链（GET方法）===')
    need_recheck = [(i, rec) for i, rec in enumerate(data) 
                    if rec.get('verification', {}).get('link_reachable') is False]
    print(f'需重测: {len(need_recheck)} 条')
    
    if need_recheck:
        recheck_results = {}
        completed = 0
        
        def recheck_one(idx_url):
            idx, url = idx_url
            reachable, status = check_link_with_get(url)
            return idx, reachable, status
        
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = {executor.submit(recheck_one, (i, rec.get('link', ''))): i 
                       for i, rec in need_recheck}
            for future in as_completed(futures):
                try:
                    idx, reachable, status = future.result()
                    recheck_results[idx] = (reachable, status)
                    completed += 1
                    if completed % 100 == 0 or completed == len(need_recheck):
                        print(f'  重测进度: {completed}/{len(need_recheck)}')
                except Exception:
                    pass
        
        # 更新verification字段
        recovered = 0
        still_dead = 0
        for idx, (reachable, status) in recheck_results.items():
            v = data[idx]['verification']
            v['http_status_get'] = status
            v['http_method'] = 'GET'
            if reachable:
                v['link_reachable'] = True
                v['http_status'] = status
                v['status'] = 'auto_checked'
                recovered += 1
            else:
                v['status'] = 'suspicious'
                still_dead += 1
        
        print(f'  恢复为可达: {recovered} 条')
        print(f'  仍然不可达: {still_dead} 条')
    
    # 2. 合并L2 WebSearch结果
    print()
    print('=== 第2步：合并L2 WebSearch抽样结果 ===')
    ws_by_id, ws_by_title = load_websearch_results()
    print(f'加载WebSearch验证: by_id={len(ws_by_id)}, by_title={len(ws_by_title)}')
    
    matched = 0
    for idx, rec in enumerate(data):
        ws_item = ws_by_id.get(idx)
        if ws_item is None:
            # 用title+venue匹配
            key = (rec.get('title', '') or rec.get('name', ''), rec.get('venue', ''))
            ws_item = ws_by_title.get(key)
        if ws_item is None:
            continue
        matched += 1
        v = rec.setdefault('verification', {})
        v['status'] = 'verified' if ws_item.get('web_verified') else 'web_search_failed'
        v['verified_by'] = 'web_search'
        v['evidence_url'] = ws_item.get('evidence_url', '')
        v['evidence_source'] = ws_item.get('evidence_source', '')
        v['match_details'] = ws_item.get('match_details', '')
        v['web_verified'] = ws_item.get('web_verified', False)
        # 保留之前的link_reachable和source_type
        v.setdefault('link_reachable', None)
        v.setdefault('source_type', 'unknown')
        v['verified_at'] = '2026-07-18'
    print(f'匹配到WebSearch结果: {matched} 条')
    
    # 3. 最终统计
    print()
    print('=== 第3步：最终统计 ===')
    status_cnt = Counter(rec.get('verification', {}).get('status', 'missing') for rec in data)
    print('状态分布:')
    for k, v in status_cnt.most_common():
        print(f'  {k}: {v} ({v/total*100:.1f}%)')
    
    reachable_cnt = sum(1 for rec in data if rec.get('verification', {}).get('link_reachable') is True)
    unreachable_cnt = sum(1 for rec in data if rec.get('verification', {}).get('link_reachable') is False)
    print(f'\nlink可达: {reachable_cnt} ({reachable_cnt/total*100:.1f}%)')
    print(f'link不可达: {unreachable_cnt} ({unreachable_cnt/total*100:.1f}%)')
    
    src_type_cnt = Counter(rec.get('verification', {}).get('source_type', 'unknown') for rec in data)
    print('\n来源类型分布:')
    for k, v in src_type_cnt.most_common():
        print(f'  {k}: {v} ({v/total*100:.1f}%)')
    
    # L2抽样统计
    ws_verified_total = 0
    ws_passed_total = 0
    for rec in data:
        v = rec.get('verification', {})
        if v.get('verified_by') == 'web_search':
            ws_verified_total += 1
            if v.get('web_verified') is True:
                ws_passed_total += 1
    if ws_verified_total > 0:
        print(f'\nL2 WebSearch抽样: {ws_verified_total}条, 通过 {ws_passed_total}/{ws_verified_total} ({ws_passed_total/ws_verified_total*100:.1f}%)')
    
    # 4. 保存
    print()
    print(f'保存到: {EXHIBITIONS_FILE}')
    with open(EXHIBITIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # 5. 生成报告
    report_file = PROJECT_ROOT / 'output' / 'verification_report.md'
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write('# 活动数据真实性核实报告\n\n')
        f.write(f'**生成时间**: 2026-07-18\n')
        f.write(f'**数据总量**: {total} 条\n')
        f.write(f'**核实方法**: 三层验证 (L1 HTTP + L2 WebSearch + L3 来源分类)\n\n')
        
        f.write('## 总体结论\n\n')
        verified = status_cnt.get('verified', 0)
        auto_checked = status_cnt.get('auto_checked', 0)
        suspicious = status_cnt.get('suspicious', 0)
        ws_failed = status_cnt.get('web_search_failed', 0)
        if ws_verified_total:
            f.write(f'- L2 WebSearch强验证通过: {ws_passed_total}/{ws_verified_total} ({ws_passed_total/ws_verified_total*100:.1f}%)\n')
        f.write(f'- L1 HTTP链接可达: {reachable_cnt}/{total} ({reachable_cnt/total*100:.1f}%)\n')
        f.write(f'- 综合状态 verified(已强验证): {verified}\n')
        f.write(f'- 综合状态 auto_checked(自动验证通过): {auto_checked}\n')
        f.write(f'- 综合状态 suspicious(死链可疑): {suspicious}\n')
        f.write(f'- 综合状态 web_search_failed(搜索未找到): {ws_failed}\n\n')
        
        f.write('## 状态字段说明\n\n')
        f.write('- `verified`: L2 WebSearch抽样验证通过，标题/场馆/日期至少2项匹配\n')
        f.write('- `auto_checked`: L1 HTTP验证link可达（200/3xx）\n')
        f.write('- `suspicious`: link不可达，需人工复核\n')
        f.write('- `web_search_failed`: L2抽样但WebSearch未找到证据\n\n')
        
        f.write('## 来源类型分布\n\n')
        f.write('| 类型 | 数量 | 占比 |\n|---|---|---|\n')
        for k, v in src_type_cnt.most_common():
            f.write(f'| {k} | {v} | {v/total*100:.1f}% |\n')
        
        f.write('\n## L2 WebSearch抽样明细\n\n')
        f.write('共抽样100条（每城10条），结果：\n\n')
        f.write('| 城市 | 通过/总数 |\n|---|---|\n')
        city_stats = {}
        for rec in data:
            v = rec.get('verification', {})
            if v.get('verified_by') == 'web_search':
                city = rec.get('city', '')
                if city not in city_stats:
                    city_stats[city] = [0, 0]
                city_stats[city][1] += 1
                if v.get('web_verified') is True:
                    city_stats[city][0] += 1
        for city in sorted(city_stats.keys()):
            passed, cnt = city_stats[city]
            f.write(f'| {city} | {passed}/{cnt} |\n')
        
        f.write('\n## 未通过L2验证的活动\n\n')
        for idx, rec in enumerate(data):
            v = rec.get('verification', {})
            if v.get('verified_by') == 'web_search' and v.get('web_verified') is not True:
                f.write(f'- **#{idx} [{rec.get("city")}] {rec.get("title", "")[:60]}**\n')
                f.write(f'  - venue: {rec.get("venue", "")}\n')
                f.write(f'  - date: {rec.get("start_date", "")} ~ {rec.get("end_date", "")}\n')
                f.write(f'  - link: {rec.get("link", "")}\n')
                f.write(f'  - match_details: {v.get("match_details", "")}\n\n')
        
        f.write('## 死链明细（GET重测后仍不可达）\n\n')
        dead_after_recheck = [(i, rec) for i, rec in enumerate(data) 
                              if rec.get('verification', {}).get('link_reachable') is False]
        f.write(f'共 {len(dead_after_recheck)} 条 link 不可达（已用GET方法重测）\n\n')
        for i, rec in dead_after_recheck[:50]:
            v = rec.get('verification', {})
            f.write(f'- **#{i} [{rec.get("city")}] {rec.get("title", "")[:50]}**\n')
            f.write(f'  - link: {rec.get("link", "")}\n')
            f.write(f'  - source: {rec.get("source", "")}\n')
            f.write(f'  - http_status: {v.get("http_status")} / http_status_get: {v.get("http_status_get")}\n\n')
        if len(dead_after_recheck) > 50:
            f.write(f'... 还有 {len(dead_after_recheck) - 50} 条未列出\n')
    
    print(f'报告已保存到: {report_file}')
    print('完成。')

if __name__ == '__main__':
    main()
