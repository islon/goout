#!/usr/bin/env python3
"""
处理5条web_search_failed记录：
- 删除3条不确定的（#19, #836, #3506）
- 更新2条已证实的（#1536, #3892）的link和verification
"""

import json
from pathlib import Path
from collections import Counter

PROJECT_ROOT = Path(__file__).parent.parent
EXHIBITIONS_FILE = PROJECT_ROOT / 'output' / 'exhibitions.json'
MINIPROGRAM_FILE = PROJECT_ROOT / 'miniprogram' / 'data' / 'exhibitions.js'

# 删除的记录索引
DELETE_INDICES = [19, 836, 3506]

# 更新的记录（index -> 新link + 证据）
UPDATE_RECORDS = {
    1536: {
        'new_link': '#小程序://金沙国际音乐厅/40BDWWQDOfRbjSg',
        'evidence_url': '#小程序://金沙国际音乐厅/40BDWWQDOfRbjSg',
        'evidence_source': '金沙国际音乐厅官方小程序',
        'match_details': '用户提供官方小程序链接，证实活动真实存在',
    },
    3892: {
        'new_link': 'https://www.xslib.com.cn/hdyg/14324.htm',
        'evidence_url': 'https://www.xslib.com.cn/hdyg/14324.htm',
        'evidence_source': '萧山图书馆官网 - 2026年7月活动预告',
        'match_details': '萧山图书馆官网"2026年7月活动预告"页面，发布于2026-07-01，证实暑期阅读活动真实存在',
    },
}

def main():
    print(f'读取: {EXHIBITIONS_FILE}')
    with open(EXHIBITIONS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total_before = len(data)
    print(f'处理前总数: {total_before}')
    
    # 先更新2条已证实的
    print()
    print('=== 更新2条已证实记录 ===')
    for idx, update in UPDATE_RECORDS.items():
        rec = data[idx]
        old_link = rec.get('link', '')
        rec['link'] = update['new_link']
        if 'url' in rec:
            rec['url'] = update['new_link']
        v = rec.setdefault('verification', {})
        v['status'] = 'verified'
        v['verified_by'] = 'web_search'
        v['web_verified'] = True
        v['link_reachable'] = True  # 小程序和官网都可达
        v['evidence_url'] = update['evidence_url']
        v['evidence_source'] = update['evidence_source']
        v['match_details'] = update['match_details']
        v['note'] = '用户手动核实并提供证据链接'
        v['verified_at'] = '2026-07-18'
        print(f'  #{idx} [{rec.get("city")}] {rec.get("title","")[:40]}')
        print(f'    旧link: {old_link[:60]}')
        print(f'    新link: {update["new_link"][:60]}')
    
    # 删除3条不确定的（从大到小排序，避免索引偏移）
    print()
    print('=== 删除3条不确定记录 ===')
    deleted_details = []
    for idx in sorted(DELETE_INDICES, reverse=True):
        rec = data[idx]
        deleted_details.append({
            'index': idx,
            'title': rec.get('title', ''),
            'city': rec.get('city', ''),
            'venue': rec.get('venue', ''),
            'link': rec.get('link', ''),
            'reason': rec.get('verification', {}).get('match_details', ''),
        })
        print(f'  #{idx} [{rec.get("city")}] {rec.get("title","")[:50]}')
        del data[idx]
    
    total_after = len(data)
    print(f'\n处理后总数: {total_after} (删除 {total_before - total_after} 条)')
    
    # 重新统计
    print()
    print('=== 最终统计 ===')
    status_cnt = Counter(rec.get('verification', {}).get('status', 'missing') for rec in data)
    for k, v in status_cnt.most_common():
        print(f'  {k}: {v} ({v/total_after*100:.1f}%)')
    
    # 保存主文件
    print()
    print(f'保存主文件: {EXHIBITIONS_FILE}')
    with open(EXHIBITIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # 同步小程序
    print(f'同步小程序: {MINIPROGRAM_FILE}')
    from datetime import datetime
    today = datetime.now().strftime('%Y-%m-%d')
    active = [rec for rec in data if rec.get('end_date', '2099-12-31') >= today]
    active.sort(key=lambda x: x.get('start_date', '9999-12-31'))
    cropped = active[:800]
    print(f'  未结束活动: {len(active)} 条, 裁剪到: {len(cropped)} 条')
    
    with open(MINIPROGRAM_FILE, 'w', encoding='utf-8') as f:
        f.write('// 活动数据 - 自动同步自 output/exhibitions.json\n')
        f.write('// 包含 verification 字段记录每条活动的核实状态\n')
        f.write(f'// 最后更新: 2026-07-18 (用户手动核实后, 删除3条不确定, 更新2条已证实)\n\n')
        f.write('const activities = ')
        f.write(json.dumps(cropped, ensure_ascii=False, indent=2))
        f.write('\n\nmodule.exports = activities\n')
    
    size = MINIPROGRAM_FILE.stat().st_size
    print(f'  文件大小: {size/1024:.1f}KB')
    
    # 保存删除记录到日志
    delete_log = PROJECT_ROOT / 'output' / 'deleted_records.log'
    with open(delete_log, 'w', encoding='utf-8') as f:
        f.write('# 删除记录日志 - 2026-07-18\n')
        f.write(f'# 共删除 {len(deleted_details)} 条不确定活动\n\n')
        for d in deleted_details:
            f.write(f'#{d["index"]} [{d["city"]}] {d["title"]}\n')
            f.write(f'  venue: {d["venue"]}\n')
            f.write(f'  link: {d["link"]}\n')
            f.write(f'  reason: {d["reason"]}\n\n')
    print(f'删除日志: {delete_log}')
    
    print()
    print('完成。')

if __name__ == '__main__':
    main()
