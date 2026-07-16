import json
import os

DATA_FILE = 'output/exhibitions.json'
OUTPUT_FILE = 'output/exhibitions.json'

new_activities = [
    {"name": "杭州西湖音乐喷泉夜游", "venue": "西湖音乐喷泉", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "夜晚音乐喷泉灯光秀，西湖夜景打卡，浪漫杭州。", "source": "杭州本地宝", "highlights": ["夜景", "喷泉", "西湖"], "type": "演出"},
    {"name": "杭州湖滨步行街夜景", "venue": "湖滨步行街", "city": "hangzhou", "district": "上城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "西湖边繁华商业街，夜景灯光秀，美食购物。", "source": "杭州本地宝", "highlights": ["湖滨", "夜景", "步行街"], "type": "亲子活动"},
    {"name": "杭州清河坊历史街区", "venue": "清河坊街", "city": "hangzhou", "district": "上城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "杭州历史文化街区，南宋御街，民俗风情。", "source": "杭州本地宝", "highlights": ["清河坊", "古镇", "历史"], "type": "亲子活动"},
    {"name": "杭州小河直街历史街区", "venue": "小河直街", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "京杭大运河旁历史街区，古运河风情。", "source": "杭州本地宝", "highlights": ["小河直街", "运河", "历史"], "type": "亲子活动"},
    {"name": "杭州大运河夜游", "venue": "京杭大运河杭州景区", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "运河夜游，灯光夜景，乘船赏运河。", "source": "杭州本地宝", "highlights": ["运河", "夜游", "夜景"], "type": "亲子活动"},
    {"name": "杭州拱宸桥夜游船", "venue": "拱宸桥", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "拱宸桥游船，运河夜景，江南水乡。", "source": "杭州本地宝", "highlights": ["拱宸桥", "游船", "运河"], "type": "亲子活动"},
    {"name": "杭州刀剪剑博物馆", "venue": "中国刀剪剑博物馆", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "刀剪剑文化，张小泉剪刀，运河三馆。", "source": "杭州本地宝", "highlights": ["刀剪剑", "博物馆", "免费"], "type": "展览"},
    {"name": "杭州伞博物馆", "venue": "中国伞博物馆", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "伞文化展，西湖绸伞，工艺精品。", "source": "杭州本地宝", "highlights": ["伞博物馆", "免费", "工艺"], "type": "展览"},
    {"name": "杭州扇博物馆", "venue": "中国扇博物馆", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "扇文化展，王星记扇子，手工技艺。", "source": "杭州本地宝", "highlights": ["扇博物馆", "免费", "工艺"], "type": "展览"},
    {"name": "杭州工艺美术博物馆", "venue": "杭州工艺美术博物馆", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "杭州工艺美术，非遗文化，手工体验。", "source": "杭州本地宝", "highlights": ["工艺美术", "博物馆", "免费"], "type": "展览"},
]

if __name__ == '__main__':
    if not os.path.exists(DATA_FILE):
        print(f"文件 {DATA_FILE} 不存在！")
        exit(1)
    
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        exhibitions = json.load(f)
    
    existing_names = {e['name'] for e in exhibitions}
    added_count = 0
    
    for activity in new_activities:
        if activity['name'] not in existing_names:
            exhibitions.append(activity)
            print(f"添加: {activity['name']} ({activity['city']})")
            added_count += 1
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(exhibitions, f, ensure_ascii=False, indent=2)
    
    print(f"\n共添加 {added_count} 个活动")
    
    city_counts = {}
    for e in exhibitions:
        city_counts[e['city']] = city_counts.get(e['city'], 0) + 1
    print(f"\n各城市活动数量:")
    for city, count in sorted(city_counts.items()):
        print(f"  {city}: {count}")
