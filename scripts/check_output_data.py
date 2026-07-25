import json

OUTPUT_JSON_FILE = "/workspace/shenzhen-exhibitions/output/exhibitions.json"

VALID_FEES = {'免费', '免费需预约', '收费', '部分免费', '需购票'}

DISTRICT_MAP = {
    '深圳图书馆': '福田区', '深圳博物馆': '福田区', '深圳博物馆（历史民俗馆）': '福田区',
    '深圳博物馆（古代艺术馆）': '南山区', '深圳博物馆（改革开放展览馆）': '南山区',
    '深圳音乐厅': '福田区', '深圳滨海艺术中心': '宝安区', '深圳科学技术馆': '光明区',
    '深圳科学技术馆（光明新馆）': '光明区', '深圳市少年宫': '福田区', '深圳市青少年活动中心': '福田区',
    '深圳少年儿童图书馆': '福田区', '深圳市文化馆': '福田区', '深圳市安全教育基地': '龙华区',
    '深圳会展中心': '福田区', '深圳国际会展中心': '宝安区', '深圳湾体育中心': '南山区',
    '深圳市体育中心': '福田区', '深圳自然博物馆': '南山区', '深圳古生物博物馆': '福田区',
    '深圳当代艺术与城市规划馆': '福田区', '南山图书馆': '南山区', '南山博物馆': '南山区',
    '南山区文化馆': '南山区', '南山区青少年活动中心': '南山区', '南山文体中心': '南山区',
    '南山安全教育体验馆': '南山区', '蛇口海洋科普馆': '南山区', '深爱人才馆': '南山区',
    '南头古城博物馆群': '南山区', '招商局历史博物馆': '南山区', '南山书房': '南山区',
    '宝安图书馆': '宝安区', '宝安科技馆': '宝安区', '宝安区青少年宫': '宝安区',
    '宝安体育中心': '宝安区', '宝安1990文化馆': '宝安区', '湾区之眼': '宝安区',
    '福田区图书馆': '福田区', '罗湖区图书馆': '罗湖区', '龙岗区图书馆': '龙岗区',
    '龙岗区博物馆': '龙岗区', '龙岗区青少年宫': '龙岗区', '龙岗客家民俗博物馆': '龙岗区',
    '龙华区图书馆': '龙华区', '龙华区青少年宫': '龙华区', '龙华生态文明展览馆': '龙华区',
    '中国版画博物馆': '龙华区', '光明区图书馆': '光明区', '光明区科技馆': '光明区',
    '光明区文化馆': '光明区', '坪山区图书馆': '坪山区', '盐田区图书馆': '盐田区',
    '中英街历史博物馆': '盐田区', '大鹏新区图书馆': '大鹏新区', '大鹏地质公园博物馆': '大鹏新区',
    '大亚湾核能科技馆': '大鹏新区',
}

SOURCE_DISTRICT_MAP = {
    '深圳图书馆官网': '福田区', '深圳博物馆官网': '福田区', '深圳音乐厅官网': '福田区',
    '深圳滨海艺术中心官网': '宝安区', '深圳科学技术馆官网': '光明区', '深圳市少年宫官网': '福田区',
    '深圳市青少年活动中心官网': '福田区', '深圳少年儿童图书馆官网': '福田区', '深圳市文化馆官网': '福田区',
    '南山博物馆官网': '南山区', '南山图书馆官网': '南山区', '南山区文化馆官网': '南山区',
    '宝安图书馆官网': '宝安区', '福田区图书馆官网': '福田区', '罗湖区图书馆官网': '罗湖区',
    '龙岗区图书馆官网': '龙岗区', '龙华区图书馆官网': '龙华区', '光明区图书馆官网': '光明区',
    '坪山区图书馆官网': '坪山区', '盐田区图书馆官网': '盐田区', '大鹏新区图书馆官网': '大鹏新区',
    '宝安科技馆': '宝安区', '宝安区青少年宫': '宝安区', '龙岗区青少年宫': '龙岗区',
    '龙华区青少年宫': '龙华区', '深圳市体育中心': '福田区', '宝安体育中心': '宝安区',
    '深圳湾体育中心': '南山区', '龙岗区博物馆': '龙岗区', '大鹏地质公园博物馆': '大鹏新区',
    '光明区文化馆': '光明区', '深圳市少年宫': '福田区',
}

def get_district_from_venue(venue):
    for venue_key, district in DISTRICT_MAP.items():
        if venue_key in venue:
            return district
    for district in ['福田区', '南山区', '宝安区', '罗湖区', '龙岗区', '龙华区', '光明区', '坪山区', '盐田区', '大鹏新区']:
        if district in venue:
            return district
    return None

def get_district_from_source(source):
    if not source:
        return None
    for source_key, district in SOURCE_DISTRICT_MAP.items():
        if source_key in source:
            return district
    for district in ['福田区', '南山区', '宝安区', '罗湖区', '龙岗区', '龙华区', '光明区', '坪山区', '盐田区', '大鹏新区']:
        if district in source:
            return district
    return None

def check_data_quality(data):
    issues = []
    for i, item in enumerate(data):
        row = i + 1
        issues_for_item = []
        
        fee = item.get('fee', '')
        if fee not in VALID_FEES:
            issues_for_item.append(f"fee 字段值 '{fee}' 不合法")
        
        description = item.get('description', '')
        if len(description) < 10:
            issues_for_item.append(f"description 长度不足10字，当前长度: {len(description)}")
        
        venue = item.get('venue', '')
        source = item.get('source', '')
        
        venue_district = get_district_from_venue(venue)
        source_district = get_district_from_source(source)
        
        if venue_district and source_district and venue_district != source_district:
            issues_for_item.append(f"venue 区县({venue_district})与 source 区县({source_district})不匹配")
        
        if issues_for_item:
            issues.append({
                'row': row,
                'title': item.get('title', 'Unknown'),
                'venue': venue,
                'source': source,
                'fee': fee,
                'description_length': len(description),
                'issues': issues_for_item
            })
    
    return issues

def main():
    with open(OUTPUT_JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"检查 {len(data)} 条输出数据...")
    
    issues = check_data_quality(data)
    if issues:
        print(f"\n发现 {len(issues)} 个数据质量问题:")
        for issue in issues[:20]:
            print(f"\n第 {issue['row']} 条: {issue['title']}")
            for problem in issue['issues']:
                print(f"  - {problem}")
        if len(issues) > 20:
            print(f"\n...还有 {len(issues) - 20} 个问题未显示")
    else:
        print("\n未发现数据质量问题")

if __name__ == "__main__":
    main()