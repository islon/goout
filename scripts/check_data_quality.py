import json
import os
import sys

ALLOWED_FEE_VALUES = {'免费', '免费需预约', '收费', '部分免费', '需购票'}

CITY_DISTRICT_KEYWORDS = {
    '深圳': {
        '市级': ['深圳', '市级', '市'],
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
    },
    '广州': {
        '市级': ['广州', '市级', '市'],
        '越秀': ['越秀', '越秀区'],
        '海珠': ['海珠', '海珠区'],
        '天河': ['天河', '天河区'],
        '白云': ['白云', '白云区'],
        '黄埔': ['黄埔', '黄埔区'],
        '番禺': ['番禺', '番禺区'],
        '花都': ['花都', '花都区'],
        '南沙': ['南沙', '南沙区'],
        '从化': ['从化', '从化区'],
        '增城': ['增城', '增城区'],
    },
    '北京': {
        '市级': ['北京', '市级', '市'],
        '东城': ['东城', '东城区'],
        '西城': ['西城', '西城区'],
        '朝阳': ['朝阳', '朝阳区'],
        '海淀': ['海淀', '海淀区'],
        '丰台': ['丰台', '丰台区'],
        '石景山': ['石景山', '石景山区'],
        '通州': ['通州', '通州区'],
        '昌平': ['昌平', '昌平区'],
    },
    '上海': {
        '市级': ['上海', '市级', '市'],
        '浦东': ['浦东', '浦东新区', '临港'],
        '黄浦': ['黄浦', '黄浦区'],
        '静安': ['静安', '静安区'],
        '徐汇': ['徐汇', '徐汇区'],
        '长宁': ['长宁', '长宁区'],
        '普陀': ['普陀', '普陀区'],
        '虹口': ['虹口', '虹口区'],
        '杨浦': ['杨浦', '杨浦区'],
        '闵行': ['闵行', '闵行区'],
        '嘉定': ['嘉定', '嘉定区'],
        '松江': ['松江', '松江区'],
    },
    '杭州': {
        '市级': ['杭州', '市级', '市'],
        '上城': ['上城', '上城区'],
        '拱墅': ['拱墅', '拱墅区'],
        '西湖': ['西湖', '西湖区'],
        '滨江': ['滨江', '滨江区'],
        '萧山': ['萧山', '萧山区'],
        '余杭': ['余杭', '余杭区'],
        '临平': ['临平', '临平区'],
        '钱塘': ['钱塘', '钱塘区'],
        '富阳': ['富阳', '富阳区'],
        '临安': ['临安', '临安区'],
    },
}


def get_city_district(text, city=None):
    if not text:
        return None
    if city and city in CITY_DISTRICT_KEYWORDS:
        specific_districts = [d for d in CITY_DISTRICT_KEYWORDS[city] if d != '市级']
        for district in specific_districts:
            for kw in CITY_DISTRICT_KEYWORDS[city][district]:
                if kw in text:
                    return district
        for kw in CITY_DISTRICT_KEYWORDS[city].get('市级', []):
            if kw in text:
                return '市级'
    return None


CITY_NAME_MAP = {
    'shenzhen': '深圳',
    'guangzhou': '广州',
    'shanghai': '上海',
    'beijing': '北京',
    'hangzhou': '杭州',
    'chengdu': '成都',
    'nanjing': '南京',
}


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

        link = item.get('link', '') or item.get('url', '')
        if not link:
            issues.append({
                'type': 'link_missing',
                'file': source_file,
                'item': item_num,
                'title': item.get('title', 'N/A'),
                'venue': item.get('venue', 'N/A'),
                'message': "缺少来源链接(link)，无法追溯数据来源"
            })

        venue = item.get('venue', '')
        source = item.get('source', '')
        city_code = item.get('city', '')
        city_name = CITY_NAME_MAP.get(city_code, '')

        if city_name:
            venue_district = get_city_district(venue, city_name)
            source_district = get_city_district(source, city_name)

            if venue_district and source_district and venue_district != source_district:
                if source_district == '市级':
                    pass
                else:
                    issues.append({
                        'type': 'district_mismatch',
                        'file': source_file,
                        'item': item_num,
                        'title': item.get('title', 'N/A'),
                        'venue': venue,
                        'source': source,
                        'city': city_name,
                        'venue_district': venue_district,
                        'source_district': source_district,
                        'message': f"venue区县({venue_district})与source区县({source_district})不匹配 [{city_name}]"
                    })

    return issues


def load_json_files():
    files_to_check = []

    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output')
    final_file = os.path.join(output_dir, 'exhibitions.json')
    if os.path.exists(final_file):
        files_to_check.append(('exhibitions.json', final_file))

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
