import json

CITY_VENUE_KEYWORDS = {
    'guangzhou': ['广东科学中心', '南越王博物院', '广州图书馆', '广州青少年科技馆', '广州地铁博物馆', '广州市文化馆', '广东省博物馆', '广州动物园', '广州海洋馆', '广州少年儿童图书馆'],
    'shanghai': ['上海科技馆', '上海自然博物馆', '上海博物馆', '上海少年儿童图书馆', '世界技能博物馆', '徐家汇书院', '上海天文馆', '上海动物园', '上海海洋水族馆', '上海昆虫博物馆'],
    'beijing': ['北京科学中心', '中国科学技术馆', '北京天文馆', '中国妇女儿童博物馆', '中国消防博物馆', '中国古动物馆', '中国园林博物馆', '首都图书馆', '国家图书馆', '北京动物园', '中国国家博物馆'],
}

with open('manual_data.json', 'r', encoding='utf-8') as f:
    activities = json.load(f)

fixed_count = 0
for activity in activities:
    if 'city' not in activity or not activity['city']:
        venue = activity.get('venue', '')
        for city_code, keywords in CITY_VENUE_KEYWORDS.items():
            for kw in keywords:
                if kw in venue:
                    activity['city'] = city_code
                    fixed_count += 1
                    break
            if 'city' in activity:
                break

with open('manual_data.json', 'w', encoding='utf-8') as f:
    json.dump(activities, f, ensure_ascii=False, indent=2)

print(f"共为 {fixed_count} 个活动添加了城市信息")
