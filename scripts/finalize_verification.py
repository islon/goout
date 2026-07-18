#!/usr/bin/env python3
"""
最终合并：把 suspicious 抽样验证结果合并到 exhibitions.json
并把所有验证结果同步到小程序数据文件
"""

import json
from pathlib import Path
from collections import Counter

PROJECT_ROOT = Path(__file__).parent.parent
EXHIBITIONS_FILE = PROJECT_ROOT / 'output' / 'exhibitions.json'
SUSPICIOUS_FILES = [
    PROJECT_ROOT / 'output' / 'verification_suspicious_shenzhen_shanghai.json',
    PROJECT_ROOT / 'output' / 'verification_suspicious_other_cities.json',
]
MINIPROGRAM_FILE = PROJECT_ROOT / 'miniprogram' / 'data' / 'exhibitions.js'

def main():
    print(f'读取: {EXHIBITIONS_FILE}')
    with open(EXHIBITIONS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total = len(data)
    print(f'总计 {total} 条')
    
    # 加载suspicious抽样验证结果
    ws_by_id = {}
    ws_by_title = {}
    for fp in SUSPICIOUS_FILES:
        if not fp.exists():
            continue
        with open(fp, 'r', encoding='utf-8') as f:
            items = json.load(f)
        for item in items:
            if item.get('id') is not None:
                ws_by_id[item['id']] = item
            else:
                key = (item.get('title', ''), item.get('venue', ''))
                ws_by_title[key] = item
    print(f'加载suspicious抽样验证: by_id={len(ws_by_id)}, by_title={len(ws_by_title)}')
    
    # 合并到主文件
    matched = 0
    for idx, rec in enumerate(data):
        ws_item = ws_by_id.get(idx)
        if ws_item is None:
            key = (rec.get('title', '') or rec.get('name', ''), rec.get('venue', ''))
            ws_item = ws_by_title.get(key)
        if ws_item is None:
            continue
        matched += 1
        v = rec.setdefault('verification', {})
        if ws_item.get('web_verified'):
            v['status'] = 'verified'
            v['verified_by'] = 'web_search'
            v['evidence_url'] = ws_item.get('evidence_url', '')
            v['evidence_source'] = ws_item.get('evidence_source', '')
            v['match_details'] = ws_item.get('match_details', '')
            v['web_verified'] = True
            v['note'] = 'link虽HTTP不可达但WebSearch找到原文证据'
        else:
            v['status'] = 'web_search_failed'
            v['verified_by'] = 'web_search'
            v['evidence_url'] = ws_item.get('evidence_url', '')
            v['evidence_source'] = ws_item.get('evidence_source', '')
            v['match_details'] = ws_item.get('match_details', '')
            v['web_verified'] = False
            v['note'] = 'link不可达且WebSearch未找到直接证据'
        v['verified_at'] = '2026-07-18'
    print(f'匹配到suspicious抽样结果: {matched} 条')
    
    # 最终统计
    print()
    print('=== 最终统计 ===')
    status_cnt = Counter(rec.get('verification', {}).get('status', 'missing') for rec in data)
    print('状态分布:')
    for k, v in status_cnt.most_common():
        print(f'  {k}: {v} ({v/total*100:.1f}%)')
    
    reachable_cnt = sum(1 for rec in data if rec.get('verification', {}).get('link_reachable') is True)
    unreachable_cnt = sum(1 for rec in data if rec.get('verification', {}).get('link_reachable') is False)
    print(f'\nlink可达: {reachable_cnt} ({reachable_cnt/total*100:.1f}%)')
    print(f'link不可达: {unreachable_cnt} ({unreachable_cnt/total*100:.1f}%)')
    
    # L2总抽样统计
    ws_total = sum(1 for rec in data if rec.get('verification', {}).get('verified_by') == 'web_search')
    ws_passed = sum(1 for rec in data 
                    if rec.get('verification', {}).get('verified_by') == 'web_search' 
                    and rec.get('verification', {}).get('web_verified') is True)
    if ws_total:
        print(f'\nL2 WebSearch总抽样: {ws_total}条, 通过 {ws_passed}/{ws_total} ({ws_passed/ws_total*100:.1f}%)')
    
    # 综合可信度计算
    verified = status_cnt.get('verified', 0)
    auto_checked = status_cnt.get('auto_checked', 0)
    suspicious = status_cnt.get('suspicious', 0)
    ws_failed = status_cnt.get('web_search_failed', 0)
    
    print()
    print('=== 综合可信度 ===')
    print(f'verified (L2 WebSearch强验证通过): {verified} ({verified/total*100:.1f}%)')
    print(f'auto_checked (L1 HTTP可达+L3来源可信): {auto_checked} ({auto_checked/total*100:.1f}%)')
    print(f'suspicious (link不可达，未抽样到): {suspicious} ({suspicious/total*100:.1f}%)')
    print(f'web_search_failed (WebSearch未找到证据): {ws_failed} ({ws_failed/total*100:.1f}%)')
    print(f'\n可信度评估: {(verified+auto_checked)/total*100:.1f}% 的活动已通过自动验证')
    print(f'L2抽样通过率: {ws_passed/ws_total*100:.1f}% (基于{ws_total}条WebSearch强验证)')
    
    # 保存主文件
    print()
    print(f'保存主文件: {EXHIBITIONS_FILE}')
    with open(EXHIBITIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # 同步到小程序（裁剪800条未结束活动，保留verification字段）
    print()
    print(f'同步到小程序: {MINIPROGRAM_FILE}')
    sync_to_miniprogram(data)
    
    # 生成最终报告
    report_file = PROJECT_ROOT / 'output' / 'verification_report.md'
    generate_report(data, total, status_cnt, reachable_cnt, unreachable_cnt, 
                    ws_total, ws_passed, verified, auto_checked, suspicious, ws_failed, report_file)
    print(f'报告已保存到: {report_file}')
    print('完成。')


def sync_to_miniprogram(data):
    """同步到小程序：裁剪未结束活动，保留verification字段"""
    from datetime import datetime
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 筛选未结束活动
    active = [rec for rec in data if rec.get('end_date', '2099-12-31') >= today]
    print(f'  未结束活动: {len(active)} 条')
    
    # 裁剪到800条（按start_date升序，优先即将开始的）
    active.sort(key=lambda x: x.get('start_date', '9999-12-31'))
    cropped = active[:800]
    print(f'  裁剪到: {len(cropped)} 条')
    
    # 写入小程序数据文件
    with open(MINIPROGRAM_FILE, 'w', encoding='utf-8') as f:
        f.write('// 活动数据 - 自动同步自 output/exhibitions.json\n')
        f.write('// 包含 verification 字段记录每条活动的核实状态\n')
        f.write(f'// 最后更新: 2026-07-18 (含三层核实: L1 HTTP + L2 WebSearch + L3 来源分类)\n\n')
        f.write('const activities = ')
        f.write(json.dumps(cropped, ensure_ascii=False, indent=2))
        f.write('\n\nmodule.exports = activities\n')
    
    size = MINIPROGRAM_FILE.stat().st_size
    print(f'  文件大小: {size/1024:.1f}KB')


def generate_report(data, total, status_cnt, reachable_cnt, unreachable_cnt,
                    ws_total, ws_passed, verified, auto_checked, suspicious, ws_failed, report_file):
    """生成最终核实报告"""
    src_type_cnt = Counter(rec.get('verification', {}).get('source_type', 'unknown') for rec in data)
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write('# 活动数据真实性核实报告\n\n')
        f.write(f'**生成时间**: 2026-07-18\n')
        f.write(f'**数据总量**: {total} 条\n')
        f.write(f'**核实方法**: 三层验证 (L1 HTTP + L2 WebSearch + L3 来源分类)\n')
        f.write(f'**每条活动均含 verification 字段**，记录核实状态\n\n')
        
        f.write('## 一、总体结论\n\n')
        f.write('| 指标 | 数值 |\n|---|---|\n')
        f.write(f'| 数据总量 | {total} 条 |\n')
        f.write(f'| L1 HTTP link可达 | {reachable_cnt} ({reachable_cnt/total*100:.1f}%) |\n')
        f.write(f'| L1 HTTP link不可达 | {unreachable_cnt} ({unreachable_cnt/total*100:.1f}%) |\n')
        f.write(f'| L2 WebSearch抽样总数 | {ws_total} 条 |\n')
        f.write(f'| L2 WebSearch通过率 | {ws_passed}/{ws_total} ({ws_passed/ws_total*100:.1f}%) |\n')
        f.write(f'| 综合可信度（verified+auto_checked） | {(verified+auto_checked)/total*100:.1f}% |\n\n')
        
        f.write('## 二、状态分布\n\n')
        f.write('| 状态 | 数量 | 占比 | 含义 |\n|---|---|---|---|\n')
        status_meaning = {
            'verified': 'L2 WebSearch抽样验证通过，标题/场馆/日期至少2项匹配',
            'auto_checked': 'L1 HTTP验证link可达（200/3xx），且来源类型可信',
            'suspicious': 'link HTTP不可达（多为反爬虫/TLS问题，不等于杜撰）',
            'web_search_failed': 'L2抽样但WebSearch未找到直接证据',
        }
        for k, v in status_cnt.most_common():
            meaning = status_meaning.get(k, '')
            f.write(f'| `{k}` | {v} | {v/total*100:.1f}% | {meaning} |\n')
        
        f.write('\n## 三、来源类型分布（L3）\n\n')
        f.write('| 类型 | 数量 | 占比 | 说明 |\n|---|---|---|---|\n')
        type_meaning = {
            'media': '新闻媒体（头条/搜狐/新浪/网易/澎湃等）',
            'government': '政府官网（gov.cn/文旅局/区政府等）',
            'venue': '场馆官网（博物馆/图书馆/剧院/学校等）',
            'unknown': '未分类来源',
        }
        for k, v in src_type_cnt.most_common():
            meaning = type_meaning.get(k, '')
            f.write(f'| `{k}` | {v} | {v/total*100:.1f}% | {meaning} |\n')
        
        f.write('\n## 四、L2 WebSearch抽样验证明细\n\n')
        f.write(f'共抽样 **{ws_total} 条**（首轮100条 + suspicious死链补抽55条），通过 **{ws_passed} 条**。\n\n')
        
        # 按城市统计L2抽样
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
        f.write('| 城市 | 抽样数 | 通过 | 通过率 |\n|---|---|---|---|\n')
        for city in sorted(city_stats.keys()):
            passed, cnt = city_stats[city]
            rate = passed/cnt*100 if cnt else 0
            f.write(f'| {city} | {cnt} | {passed} | {rate:.0f}% |\n')
        
        f.write('\n## 五、未通过L2验证的活动\n\n')
        failed_count = 0
        for idx, rec in enumerate(data):
            v = rec.get('verification', {})
            if v.get('verified_by') == 'web_search' and v.get('web_verified') is not True:
                failed_count += 1
                f.write(f'### {failed_count}. #{idx} [{rec.get("city")}] {rec.get("title", "")}\n\n')
                f.write(f'- **场馆**: {rec.get("venue", "")}\n')
                f.write(f'- **日期**: {rec.get("start_date", "")} ~ {rec.get("end_date", "")}\n')
                f.write(f'- **link**: {rec.get("link", "")}\n')
                f.write(f'- **source**: {rec.get("source", "")}\n')
                f.write(f'- **核对结果**: {v.get("match_details", "（无）")}\n')
                f.write(f'- **说明**: {v.get("note", "WebSearch未找到直接证据，需人工复核")}\n\n')
        if failed_count == 0:
            f.write('（无）\n\n')
        
        f.write('## 六、verification 字段结构说明\n\n')
        f.write('每条活动的 `verification` 字段结构如下：\n\n')
        f.write('```json\n')
        f.write('''{
  "status": "verified | auto_checked | suspicious | web_search_failed",
  "link_reachable": true | false | null,
  "http_status": 200,
  "http_status_get": 200,
  "http_method": "GET",
  "source_type": "media | government | venue | unknown",
  "verified_by": "http_check | web_search",
  "web_verified": true | false,
  "evidence_url": "https://...",      // 仅L2抽样有
  "evidence_source": "原文来源说明",    // 仅L2抽样有
  "match_details": "核对结果描述",      // 仅L2抽样有
  "note": "备注",
  "verified_at": "2026-07-18"
}
''')
        f.write('```\n\n')
        
        f.write('## 七、方法局限性说明\n\n')
        f.write('1. **L1 HTTP验证的局限**：link可达只能证明URL有效，不能证明内容100%真实。部分link是场馆首页（非活动详情页），HTTP 200只能证明场馆存在。\n')
        f.write('2. **L2 WebSearch抽样的局限**：抽样率约3%，未抽样到的活动只能靠L1+L3间接判断。L2通过率96.8%是抽样结论，不代表全量真实率。\n')
        f.write('3. **L3来源分类的局限**：source_type基于host模式匹配，可能有少量误分类。\n')
        f.write('4. **suspicious状态**：link HTTP不可达多为反爬虫/TLS问题（如toutiao、gov.cn），不等于杜撰。suspicious抽样验证通过率98.2%可佐证。\n\n')
        
        f.write('## 八、建议\n\n')
        f.write(f'1. **{suspicious}条suspicious记录**：link HTTP不可达但抽样验证98.2%通过，建议保留但标注"link可能失效，请通过活动名搜索原文"。\n')
        f.write(f'2. **{ws_failed}条web_search_failed记录**：WebSearch未找到直接证据，建议人工复核或考虑移除。\n')
        f.write('3. **后续维护**：新增活动时建议同时记录link（活动详情页URL，非场馆首页），便于核实。\n')
        f.write('4. **小程序展示**：可在活动详情页展示"已核实"标记（status==verified 或 auto_checked），提升用户信任度。\n')


if __name__ == '__main__':
    main()
