import json
import os
import sys

ALLOWED_FEE_VALUES = {'免费', '免费需预约', '收费', '部分免费', '需购票'}

DISTRICT_MAPPING = {
    '深圳': ['深圳', '市级'],
    '南山': ['南山', '南山区'],
    '宝安': ['宝安', '宝安区'],
    '福田': ['福田', '福田区'],
    '罗湖': ['罗湖', '罗湖区'],
    '龙岗': ['龙岗', '龙岗区'],
    '龙华': ['龙华', '龙华区'],
    '光明': ['光明', '光明区'],
    '坪山': ['坪山', '坪山区'],
    '盐田': ['盐田', '盐田区'],
    '大鹏': ['大鹏', '大鹏新区'],
}


def get_district_from_text(text):
    if not text:
        return None
    specific_districts = ['南山', '宝安', '福田', '罗湖', '龙岗', '龙华', '光明', '坪山', '盐田', '大鹏']
    for district in specific_districts:
        if district in text:
            return district
    if '深圳' in text:
        return '深圳'
    return None


def check_data_quality(data, source_file):
    issues = []
    
    for i, item in enumerate(data):
        item_num = i + 1
        
        if 'fee' in item and item['fee'] not in ALLOWED_FEE_VALUES:
            issues.append({
                'type': 'fee_invalid',
                'file': source_file,
                'item': item_num,
                'title': item.get('title', 'N/A'),
                'venue': item.get('venue', 'N/A'),
                'current_value': item.get('fee', 'N/A'),
                'allowed_values': list(ALLOWED_FEE_VALUES),
                'message': f"fee字段值 '{item['fee']}' 不在允许范围内"
            })
        
        description = item.get('description', '')
        if len(description) < 10:
            issues.append({
                'type': 'description_too_short',
                'file': source_file,
                'item': item_num,
                'title': item.get('title', 'N/A'),
                'venue': item.get('venue', 'N/A'),
                'current_length': len(description),
                'description': description,
                'message': f"description长度 {len(description)} 小于10字"
            })
        
        venue = item.get('venue', '')
        source = item.get('source', '')
        
        venue_district = get_district_from_text(venue)
        source_district = get_district_from_text(source)
        
        city_sources = ['深圳文旅游局', '深圳政府在线', '深圳新闻网', '深圳融媒体中心', '深圳商报', '深圳晚报', '深圳卫视', '深圳广播', '深圳发布', '深圳博物馆官网', '深圳音乐厅官网', '深圳科学技术馆官网', '深圳图书馆官网', '深圳市文化馆官网', '深圳市少年宫官网', '深圳少年儿童图书馆官网', '深圳滨海艺术中心官网', '深圳国际会展中心', '深圳会展中心']
        
        if venue_district and source_district and venue_district != source_district:
            if source in city_sources or (source_district == '深圳' and venue_district != '深圳'):
                pass
            else:
                issues.append({
                    'type': 'district_mismatch',
                    'file': source_file,
                    'item': item_num,
                    'title': item.get('title', 'N/A'),
                    'venue': venue,
                    'source': source,
                    'venue_district': venue_district,
                    'source_district': source_district,
                    'message': f"venue区县({venue_district})与source区县({source_district})不匹配"
                })
    
    return issues


def load_json_files():
    files_to_check = []
    
    manual_file = os.path.join(os.path.dirname(__file__), 'manual_data.json')
    if os.path.exists(manual_file):
        files_to_check.append(('manual_data.json', manual_file))
    
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output')
    if os.path.exists(output_dir):
        for filename in os.listdir(output_dir):
            if filename.endswith('_exhibitions.json') or filename == 'exhibitions.json':
                files_to_check.append((filename, os.path.join(output_dir, filename)))
    
    return files_to_check


def main():
    all_issues = []
    files_to_check = load_json_files()
    
    for file_name, file_path in files_to_check:
        print(f"检查 {file_name}...")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            issues = check_data_quality(data, file_name)
            all_issues.extend(issues)
            print(f"  发现 {len(issues)} 个问题")
        except Exception as e:
            print(f"  读取失败: {e}")
    
    print(f"\n=== 检查结果汇总 ===")
    print(f"总共发现 {len(all_issues)} 个数据质量问题")
    
    if all_issues:
        print("\n--- 问题详情 ---")
        for issue in all_issues:
            print(f"\n[{issue['type']}] {issue['file']} 第{issue['item']}条")
            print(f"  标题: {issue['title']}")
            print(f"  场馆: {issue['venue']}")
            print(f"  问题: {issue['message']}")
    
    return all_issues


if __name__ == "__main__":
    main()
