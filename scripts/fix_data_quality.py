#!/usr/bin/env python3
"""Standalone data quality fix script for islon/goout project.

Can be run independently to fix data quality issues:
1. fee values -> normalize to allowed set
2. source/venue district mismatches -> update source
3. description length < 10 chars -> expand

Usage: python3 fix_data_quality.py [--check-only]
"""

import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_DIR, 'output')

VALID_FEES = {'免费', '免费需预约', '收费', '部分免费', '需购票'}

SOURCE_DISTRICT_MAP = {
    'nslib': '南山区', 'nsmuseum': '南山区', 'nswhg': '南山区', 'nsqsng': '南山区',
    'nswtzx': '南山区', 'nssxf': '南山区', 'oct_wetland': '南山区', 'sarc': '南山区',
    'skhykpg': '南山区', 'nsaqjy': '南山区', 'ntgc': '南山区', 'zsjbwg': '南山区',
    'nsqwhg': '南山区',
    'balib': '宝安区', 'baoan_1990': '宝安区',
    'szlib': '福田区', 'sz_children_lib': '福田区',
    'gm_lib': '光明区', 'gm_kjg': '光明区',
    'yt_lib': '盐田区', 'yt_history': '盐田区',
    'dp_geopark': '大鹏新区', 'dp_nuclear': '大鹏新区',
    'lg_hakka': '龙岗区',
    'lh_ecology': '龙华区', 'lh_paleo': '龙华区', 'lh_printmaking': '龙华区',
    'ps_nature': '坪山区',
    'szwty': '南山区', 'sz_safety': '福田区',
}

VENUE_DISTRICT_MAP = {
    '南山': '南山区', '宝安': '宝安区', '福田': '福田区', '罗湖': '罗湖区',
    '盐田': '盐田区', '龙岗': '龙岗区', '龙华': '龙华区', '坪山': '坪山区',
    '光明': '光明区', '大鹏': '大鹏新区',
}

DISTRICT_SOURCE = {
    '南山区': 'nanshan', '宝安区': 'baoan', '福田区': 'futian',
    '罗湖区': 'luohu', '盐田区': 'yantian', '龙岗区': 'longgang',
    '龙华区': 'longhua', '坪山区': 'pingshan', '光明区': 'guangming',
    '大鹏新区': 'dapeng',
}


def get_source_district(source):
    import re
    # Check explicit [区县] prefix
    m = re.match(r'^\[([^\]]{2,4})\]', source)
    if m:
        prefix = m.group(1)
        if prefix + '区' in SOURCE_DISTRICT_MAP.values() or prefix == '大鹏':
            return prefix + '区' if prefix != '大鹏' else '大鹏新区'

    # Check URL path components
    url_match = re.match(r'https?://[^/]+/([^/?#]+)', source)
    if url_match:
        path_component = url_match.group(1).lower()
        if path_component in SOURCE_DISTRICT_MAP:
            return SOURCE_DISTRICT_MAP[path_component]
        for prefix, district in SOURCE_DISTRICT_MAP.items():
            if prefix.lower() in path_component:
                return district

    for prefix, district in SOURCE_DISTRICT_MAP.items():
        if source.startswith(prefix) or prefix in source:
            return district
    chinese_sources = {
        '南山': '南山区', '宝安': '宝安区', '福田': '福田区',
        '罗湖': '罗湖区', '盐田': '盐田区', '龙岗': '龙岗区',
        '龙华': '龙华区', '坪山': '坪山区', '光明': '光明区', '大鹏': '大鹏新区',
    }
    for keyword, district in chinese_sources.items():
        if keyword in source:
            return district
    return None


def get_venue_district(venue):
    for keyword, district in VENUE_DISTRICT_MAP.items():
        if keyword in venue:
            return district
    return None


def expand_description(title, venue, description, fee, category=''):
    desc = description.strip()
    if len(desc) >= 10:
        return desc

    clean_desc = desc.rstrip('。').rstrip('.')
    activity_type = ''
    if '培训' in desc or '培训' in title:
        activity_type = '培训课程'
    elif '展览' in desc or '展' in title or '画展' in title or '作品展' in title:
        activity_type = '展览活动'
    elif '演出' in desc or '音乐' in title or '舞' in title or '演唱' in title:
        activity_type = '文艺演出'
    elif '报名' in desc or '预约' in desc:
        activity_type = '预约报名活动'
    elif '综合' in desc:
        activity_type = '综合性活动'
    elif '讲座' in desc or '讲座' in title:
        activity_type = '讲座活动'
    elif '阅读' in title or '读书' in title:
        activity_type = '阅读活动'

    parts = []
    if clean_desc:
        if '。' in clean_desc:
            parts.append(clean_desc.split('。')[0])
        else:
            parts.append(clean_desc)
    if venue:
        parts.append(f'在{venue}举办')
    if activity_type:
        parts.append(activity_type)

    cat_desc = {
        '展览': '精彩展览', '讲座阅读': '主题讲座与阅读', '科普活动': '科普教育',
        '演出': '文艺演出', '体育赛事': '体育赛事', '亲子活动': '亲子互动',
        '影视放映': '影视放映', '其他': '特色活动',
    }
    if category and category in cat_desc:
        parts.append(cat_desc[category])

    fee_in_desc = any(f in clean_desc for f in ['免费', '收费', '购票', '付费'])
    if fee and not fee_in_desc:
        fee_text = {'免费': '免费开放', '免费需预约': '免费需预约', '收费': '收费参与',
                    '部分免费': '部分免费', '需购票': '需购票入场'}
        if fee in fee_text:
            parts.append(fee_text[fee])

    result = '，'.join(parts) + '。'
    if len(result) < 10:
        if title:
            result = f'{title}，{result}'
        else:
            result = f'精彩活动，{result}'
    return result


def fix_source_district_mismatch(activity):
    source = activity.get('source', '')
    venue = activity.get('venue', '')
    if not source or not venue:
        return activity

    src_district = get_source_district(source)
    venue_district = get_venue_district(venue)

    if src_district and venue_district and src_district != venue_district:
        new_source = DISTRICT_SOURCE.get(venue_district, '')
        if new_source:
            if '_' in source:
                suffix = source.split('_', 1)[1]
                activity['source'] = f'{new_source}_{suffix}'
            else:
                activity['source'] = new_source

    return activity


def fix_fee(activity):
    fee = activity.get('fee', '')
    if fee and fee not in VALID_FEES:
        fee_map = {
            '免费开放': '免费', '免费参观': '免费', '免费参与': '免费',
            '免票': '免费', '免费观看': '免费',
            '需预约': '免费需预约', '预约': '免费需预约', '需要预约': '免费需预约',
            '付费': '收费', '购票': '需购票', '需要购票': '需购票',
            '部分收费': '部分免费', '部分付费': '部分免费',
        }
        if fee in fee_map:
            activity['fee'] = fee_map[fee]
        elif '免费' in fee:
            activity['fee'] = '免费'
        elif '收费' in fee or '付费' in fee or '购票' in fee:
            activity['fee'] = '收费'
        else:
            activity['fee'] = '免费'
    return activity


def fix_activity(activity):
    activity = fix_fee(activity)
    activity = fix_source_district_mismatch(activity)
    desc = activity.get('description', '')
    if len(desc) < 10:
        activity['description'] = expand_description(
            activity.get('title', ''), activity.get('venue', ''),
            desc, activity.get('fee', ''), activity.get('category', ''))
    return activity


def check_file(filepath):
    """Check a file for issues without fixing."""
    issues = []
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, list):
        return issues

    for i, a in enumerate(data):
        desc = a.get('description', '')
        if len(desc) < 10:
            issues.append(f'  [{i}] SHORT desc: "{a.get("title","")}" desc="{desc}" ({len(desc)}c)')

        fee = a.get('fee', '')
        if fee and fee not in VALID_FEES:
            issues.append(f'  [{i}] INVALID fee: "{a.get("title","")}" fee="{fee}"')

        src = a.get('source', '')
        venue = a.get('venue', '')
        src_d = get_source_district(src)
        v_d = get_venue_district(venue)
        if src_d and v_d and src_d != v_d:
            issues.append(f'  [{i}] MISMATCH: "{a.get("title","")}" src={src}({src_d}) venue={venue}({v_d})')

    return issues


def fix_file(filepath):
    print(f'\nProcessing: {os.path.basename(filepath)}')
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, list):
        print('  Skipping: not a list')
        return 0

    fixed_count = 0
    for i, activity in enumerate(data):
        old_desc = activity.get('description', '')
        old_source = activity.get('source', '')
        old_fee = activity.get('fee', '')
        data[i] = fix_activity(activity)
        new_desc = data[i].get('description', '')
        new_source = data[i].get('source', '')
        new_fee = data[i].get('fee', '')

        changed = False
        if new_desc != old_desc:
            changed = True
            print(f'  [{i}] desc: "{old_desc}" -> "{new_desc}"')
        if new_source != old_source:
            changed = True
            print(f'  [{i}] source: "{old_source}" -> "{new_source}"')
        if new_fee != old_fee:
            changed = True
            print(f'  [{i}] fee: "{old_fee}" -> "{new_fee}"')
        if changed:
            fixed_count += 1

    if fixed_count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f'  Fixed {fixed_count} entries, saved.')
    else:
        print(f'  No issues found.')
    return fixed_count


def main():
    check_only = '--check-only' in sys.argv
    total_fixed = 0
    all_issues = []

    # Only process activity data files (exhibitions*.json) and manual data
    # Exclude venue_info, collected_venues, cities, and meta files
    json_files = []
    if os.path.isdir(OUTPUT_DIR):
        for fname in sorted(os.listdir(OUTPUT_DIR)):
            if fname.endswith('.json') and 'exhibition' in fname.lower():
                json_files.append(os.path.join(OUTPUT_DIR, fname))

    manual_path = os.path.join(SCRIPT_DIR, 'manual_data.json')
    if os.path.exists(manual_path):
        json_files.append(manual_path)

    if check_only:
        print('=== DATA QUALITY CHECK (check-only mode) ===')
        for fp in json_files:
            issues = check_file(fp)
            if issues:
                all_issues.extend(issues)
                print(f'\n{os.path.basename(fp)}: {len(issues)} issues')
                for issue in issues[:10]:
                    print(issue)
        if all_issues:
            print(f'\n⚠️  Total issues found: {len(all_issues)}')
            sys.exit(1)
        else:
            print('\n✅ All data quality checks passed!')
            return

    print('=== DATA QUALITY FIX ===')
    for fp in json_files:
        total_fixed += fix_file(fp)

    print(f'\nTotal entries fixed: {total_fixed}')

    print('\n=== FINAL VERIFICATION ===')
    main_file = os.path.join(OUTPUT_DIR, 'exhibitions.json')
    if os.path.exists(main_file):
        with open(main_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        short_desc = sum(1 for a in data if len(a.get('description', '')) < 10)
        invalid_fee = sum(1 for a in data if a.get('fee', '') and a.get('fee', '') not in VALID_FEES)
        mismatches = 0
        for a in data:
            src_d = get_source_district(a.get('source', ''))
            v_d = get_venue_district(a.get('venue', ''))
            if src_d and v_d and src_d != v_d:
                mismatches += 1
        print(f'Total activities: {len(data)}')
        print(f'Short descriptions (<10 chars): {short_desc}')
        print(f'Invalid fee values: {invalid_fee}')
        print(f'Source/venue district mismatches: {mismatches}')
        if short_desc == 0 and invalid_fee == 0 and mismatches == 0:
            print('\n✅ All data quality checks passed!')
        else:
            print('\n⚠️  Some issues remain.')
            sys.exit(1)


if __name__ == '__main__':
    main()
