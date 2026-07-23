import json
import os

ALLOWED_FEE_VALUES = {'免费', '免费需预约', '收费', '部分免费', '需购票'}

DISTRICT_MAPPING = {
    '南山': ['南山', '南头', '蛇口', '招商', '粤海', '沙河', '西丽', '桃源', '前海'],
    '宝安': ['宝安', '新安', '西乡', '福永', '沙井', '松岗', '燕罗', '石岩'],
    '福田': ['福田', '园岭', '南园', '福田', '沙头', '梅林', '华富', '香蜜湖', '莲花'],
    '罗湖': ['罗湖', '东门', '南湖', '桂园', '笋岗', '清水河', '翠竹', '东湖', '东晓', '莲塘'],
    '龙岗': ['龙岗', '平湖', '坂田', '布吉', '南湾', '横岗', '龙岗', '龙城', '坪地'],
    '龙华': ['龙华', '民治', '龙华', '大浪', '观澜', '福城'],
    '光明': ['光明', '光明', '公明', '新湖', '凤凰', '玉塘', '马田'],
    '坪山': ['坪山'],
    '盐田': ['盐田', '沙头角', '海山', '盐田', '梅沙'],
    '大鹏': ['大鹏', '葵涌', '大鹏', '南澳'],
    '深圳': ['深圳'],
}


def get_district(text):
    if not text:
        return None
    for district, keywords in DISTRICT_MAPPING.items():
        if district == '深圳':
            continue
        for keyword in keywords:
            if keyword in text:
                return district
    return None


def check_data_quality(data):
    issues = []
    
    for idx, item in enumerate(data):
        item_issues = []
        
        fee = item.get('fee', '')
        if fee not in ALLOWED_FEE_VALUES:
            item_issues.append(f"fee值'{fee}'不在允许列表中")
        
        description = item.get('description', '')
        if len(description) < 10:
            item_issues.append(f"description长度不足10字（当前{len(description)}字）")
        
        venue = item.get('venue', '')
        source = item.get('source', '')
        
        venue_district = get_district(venue)
        source_district = get_district(source)
        
        if venue_district and source_district and venue_district != source_district:
            item_issues.append(f"venue区县'{venue_district}'与source区县'{source_district}'不匹配")
        
        if item_issues:
            issues.append({
                'index': idx,
                'title': item.get('title', ''),
                'venue': venue,
                'source': source,
                'fee': fee,
                'description': description[:50] + '...' if len(description) > 50 else description,
                'problems': item_issues
            })
    
    return issues


def main():
    manual_data_path = os.path.join(os.path.dirname(__file__), 'manual_data.json')
    output_data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output', 'exhibitions.json')
    
    print("=== 检查 manual_data.json ===")
    with open(manual_data_path, 'r', encoding='utf-8') as f:
        manual_data = json.load(f)
    
    manual_issues = check_data_quality(manual_data)
    print(f"发现 {len(manual_issues)} 个问题:\n")
    for issue in manual_issues:
        print(f"索引 {issue['index']}: {issue['title']}")
        print(f"  场馆: {issue['venue']}")
        print(f"  来源: {issue['source']}")
        print(f"  费用: {issue['fee']}")
        print(f"  描述: {issue['description']}")
        for problem in issue['problems']:
            print(f"    - {problem}")
        print()
    
    print("=== 检查 output/exhibitions.json ===")
    if os.path.exists(output_data_path):
        with open(output_data_path, 'r', encoding='utf-8') as f:
            output_data = json.load(f)
        
        output_issues = check_data_quality(output_data)
        print(f"发现 {len(output_issues)} 个问题:\n")
        for issue in output_issues:
            print(f"索引 {issue['index']}: {issue['title']}")
            print(f"  场馆: {issue['venue']}")
            print(f"  来源: {issue['source']}")
            print(f"  费用: {issue['fee']}")
            print(f"  描述: {issue['description']}")
            for problem in issue['problems']:
                print(f"    - {problem}")
            print()
    else:
        print("文件不存在")
    
    print("=== 检查完成 ===")
    return len(manual_issues) + len(output_issues)


if __name__ == "__main__":
    exit(main())