import json
import os
import re
import requests

TOKEN = os.environ.get('GITHUB_TOKEN', '')
ALLOWED_FEE_VALUES = {'免费', '免费需预约', '收费', '部分免费', '需购票'}

CITY_NAME_MAP = {
    'shenzhen': '深圳',
    'guangzhou': '广州',
    'shanghai': '上海',
    'beijing': '北京',
    'hangzhou': '杭州',
    'chengdu': '成都',
    'nanjing': '南京',
    'wuhan': '武汉',
    'xian': '西安',
    'chongqing': '重庆',
}

CITY_CODE_MAP = {v: k for k, v in CITY_NAME_MAP.items()}


def get_open_issues():
    url = 'https://api.github.com/repos/islon/goout/issues?state=open'
    headers = {'Authorization': f'token {TOKEN}'}
    response = requests.get(url, headers=headers)
    return response.json()


def parse_event_issue(body):
    data = {}
    
    match = re.search(r'\*\*活动名称\*\* \| (.+)', body)
    if match:
        data['title'] = match.group(1).strip()
    
    match = re.search(r'\*\*场馆\*\* \| (.+)', body)
    if match:
        data['venue'] = match.group(1).strip()
    
    match = re.search(r'\*\*所在区\*\* \| (.+)', body)
    if match:
        data['district'] = match.group(1).strip()
    
    match = re.search(r'\*\*时间\*\* \| (.+)', body)
    if match:
        data['time'] = match.group(1).strip()
    
    match = re.search(r'\*\*地址\*\* \| (.+)', body)
    if match:
        data['address'] = match.group(1).strip()
    
    match = re.search(r'\*\*类型\*\* \| (.+)', body)
    if match:
        data['category'] = match.group(1).strip()
    
    desc_start = body.find('### 活动描述')
    if desc_start != -1:
        desc_end = body.find('### 证据链接')
        if desc_end == -1:
            desc_end = body.find('---')
        if desc_end != -1:
            description = body[desc_start + 6:desc_end].strip()
            data['description'] = description
    
    source_start = body.find('来源: ')
    if source_start != -1:
        source_end = body.find('\n', source_start)
        if source_end == -1:
            source_end = len(body)
        source_text = body[source_start + 4:source_end].strip()
        url_match = re.search(r'\[(.+?)\]\((.+?)\)', source_text)
        if url_match:
            data['source'] = url_match.group(1).strip()
            data['link'] = url_match.group(2).strip()
    
    return data


def convert_time_to_dates(time_str):
    start_date = None
    end_date = None
    
    if '至' in time_str:
        parts = time_str.split('至')
        start_str = parts[0].strip()
        end_str = parts[1].strip()
        
        year_match = re.search(r'(\d{4})年', time_str)
        year = year_match.group(1) if year_match else '2026'
        
        month_match = re.search(r'(\d{1,2})月', start_str)
        month = month_match.group(1).zfill(2) if month_match else '01'
        
        day_match = re.search(r'(\d{1,2})日', start_str)
        day = day_match.group(1).zfill(2) if day_match else '01'
        start_date = f'{year}-{month}-{day}'
        
        month_match2 = re.search(r'(\d{1,2})月', end_str)
        month2 = month_match2.group(1).zfill(2) if month_match2 else month
        
        day_match2 = re.search(r'(\d{1,2})日', end_str)
        day2 = day_match2.group(1).zfill(2) if day_match2 else '01'
        end_date = f'{year}-{month2}-{day2}'
    else:
        year_match = re.search(r'(\d{4})年', time_str)
        year = year_match.group(1) if year_match else '2026'
        
        month_match = re.search(r'(\d{1,2})月', time_str)
        month = month_match.group(1).zfill(2) if month_match else '01'
        
        day_match = re.search(r'(\d{1,2})日', time_str)
        day = day_match.group(1).zfill(2) if day_match else '01'
        start_date = f'{year}-{month}-{day}'
        end_date = start_date
    
    return start_date, end_date


def infer_city(district):
    for city_name, city_code in CITY_NAME_MAP.items():
        if city_name in district:
            return city_code
    return 'shenzhen'


def infer_fee(description):
    if not description:
        return '免费'
    description = description.lower()
    if '免费' in description and '预约' in description:
        return '免费需预约'
    if '免费' in description:
        return '免费'
    if '票' in description or '元' in description or '收费' in description:
        return '收费'
    return '免费'


def create_event_item(issue_data):
    item = {
        'title': issue_data.get('title', ''),
        'name': issue_data.get('title', ''),
        'venue': issue_data.get('venue', ''),
        'city': infer_city(issue_data.get('district', '')),
        'category': issue_data.get('category', '展览'),
        'description': issue_data.get('description', '暂无详细描述'),
        'fee': infer_fee(issue_data.get('description', '')),
        'source': issue_data.get('source', ''),
        'link': issue_data.get('link', ''),
        'url': issue_data.get('link', ''),
        'contact': '',
        'family_friendly': True,
    }
    
    start_date, end_date = convert_time_to_dates(issue_data.get('time', ''))
    if start_date:
        item['start_date'] = start_date
    if end_date:
        item['end_date'] = end_date
    
    if len(item['description']) < 10:
        item['description'] = f"{item['title']}，在{item['venue']}举办的{item['category']}活动。"
    
    if item['fee'] not in ALLOWED_FEE_VALUES:
        item['fee'] = '免费'
    
    return item


def close_issue(issue_number):
    url = f'https://api.github.com/repos/islon/goout/issues/{issue_number}'
    headers = {
        'Authorization': f'token {TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {'state': 'closed'}
    response = requests.patch(url, headers=headers, json=data)
    return response.status_code == 200


def main():
    issues = get_open_issues()
    
    new_event_issues = [i for i in issues if '[新活动发现]' in i['title']]
    print(f'发现 {len(new_event_issues)} 个新活动发现issues')
    
    output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output', 'exhibitions.json')
    
    with open(output_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    existing_titles = {item['title'] for item in data}
    added_count = 0
    
    for issue in new_event_issues:
        issue_data = parse_event_issue(issue['body'])
        title = issue_data.get('title', '')
        
        if not title:
            print(f"Issue #{issue['number']}: 无法解析活动名称，跳过")
            continue
        
        if title in existing_titles:
            print(f"Issue #{issue['number']}: {title} 已存在，跳过")
            continue
        
        event_item = create_event_item(issue_data)
        data.append(event_item)
        existing_titles.add(title)
        added_count += 1
        
        print(f"Issue #{issue['number']}: 添加活动 '{title}'")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f'\n共添加 {added_count} 个新活动')
    
    for issue in new_event_issues:
        issue_data = parse_event_issue(issue['body'])
        title = issue_data.get('title', '')
        
        if title and title in existing_titles:
            if close_issue(issue['number']):
                print(f"关闭 Issue #{issue['number']}: {title}")
            else:
                print(f"关闭 Issue #{issue['number']} 失败")


if __name__ == '__main__':
    main()
