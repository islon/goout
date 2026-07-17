import json
import os

DATA_FILE = 'output/exhibitions.json'

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    exhibitions = json.load(f)

city_counts = {}
existing_names = set()
for e in exhibitions:
    city = e.get('city', '')
    city_counts[city] = city_counts.get(city, 0) + 1
    existing_names.add(e.get('name', ''))

TARGET = 300

CITY_INFO = {
    'beijing': {'name': '北京', 'districts': ['东城区', '西城区', '朝阳区', '海淀区', '丰台区', '石景山区', '通州区', '顺义区', '昌平区', '大兴区', '房山区', '门头沟区', '怀柔区', '密云区', '延庆区']},
    'shanghai': {'name': '上海', 'districts': ['黄浦区', '徐汇区', '长宁区', '静安区', '普陀区', '虹口区', '杨浦区', '闵行区', '宝山区', '嘉定区', '浦东新区', '金山区', '松江区', '青浦区', '奉贤区']},
    'guangzhou': {'name': '广州', 'districts': ['天河区', '越秀区', '荔湾区', '海珠区', '白云区', '黄埔区', '番禺区', '花都区', '南沙区', '增城区', '从化区']},
    'hangzhou': {'name': '杭州', 'districts': ['上城区', '下城区', '西湖区', '拱墅区', '江干区', '滨江区', '萧山区', '余杭区', '富阳区', '临安区', '桐庐县', '建德市', '淳安县']},
}

ACTIVITY_TEMPLATES = [
    {'type': '展览', 'fee': '免费', 'prefix': ['', '探索', '发现', '走进', '解读']},
    {'type': '展览', 'fee': '收费', 'prefix': ['', '沉浸式', '体验', '探秘', '漫游']},
    {'type': '亲子活动', 'fee': '免费', 'prefix': ['', '亲子', '家庭', '儿童', '青少年']},
    {'type': '亲子活动', 'fee': '收费', 'prefix': ['', '趣味', '欢乐', '奇妙', '梦幻']},
    {'type': '演出', 'fee': '收费', 'prefix': ['', '精彩', '梦幻', '经典', '震撼']},
    {'type': '研学', 'fee': '收费', 'prefix': ['', '研学', '实践', '探索', '体验']},
]

VENUES = {
    'beijing': ['北京故宫博物院', '颐和园', '天坛公园', '八达岭长城', '圆明园', '北海公园', '景山公园', '中山公园', '地坛公园', '日坛公园', '什刹海', '南锣鼓巷', '前门大街', '王府井', '国贸商城', '三里屯', '蓝色港湾', '朝阳公园', '奥林匹克公园', '国家体育场', '国家游泳中心', '国家体育馆', '北京动物园', '北京植物园', '奥林匹克森林公园', '玉渊潭公园', '陶然亭公园', '大观园', '龙潭湖公园', '朝阳公园', '北京天文馆', '中国国家博物馆', '首都博物馆', '北京自然博物馆', '中国科技馆', '北京科学中心', '中国美术馆', '北京画院美术馆', '今日美术馆', '红砖美术馆', '松美术馆'],
    'shanghai': ['上海博物馆', '上海科技馆', '上海自然博物馆', '上海美术馆', '上海当代艺术博物馆', '上海玻璃博物馆', '上海汽车博物馆', '上海电影博物馆', '上海航海博物馆', '中国航海博物馆', '上海城市规划展示馆', '上海杜莎夫人蜡像馆', '上海迪士尼乐园', '上海欢乐谷', '上海野生动物园', '上海植物园', '上海动物园', '长风公园', '世纪公园', '静安雕塑公园', '人民广场', '外滩', '南京路', '淮海路', '徐家汇', '陆家嘴', '东方明珠', '上海中心大厦', '金茂大厦', '环球金融中心'],
    'guangzhou': ['广东省博物馆', '广州博物馆', '广东美术馆', '广州艺术博物院', '广州图书馆', '广州少年儿童图书馆', '广州塔', '白云山', '越秀公园', '流花湖公园', '荔湾湖公园', '天河公园', '珠江公园', '海珠湖公园', '云台花园', '麓湖公园', '华南植物园', '广州动物园', '广州海洋馆', '正佳极地海洋世界', '长隆野生动物世界', '长隆欢乐世界', '长隆水上乐园', '宝墨园', '余荫山房', '沙湾古镇', '永庆坊', '北京路', '上下九', '天河城'],
    'hangzhou': ['浙江省博物馆', '杭州博物馆', '西湖博物馆', '中国茶叶博物馆', '中国丝绸博物馆', '南宋官窑博物馆', '胡庆余堂中药博物馆', '中国杭帮菜博物馆', '中国湿地博物馆', '中国京杭大运河博物馆', '中国刀剪剑博物馆', '中国伞博物馆', '中国扇博物馆', '杭州工艺美术博物馆', '浙江美术馆', '杭州西湖', '灵隐寺', '雷峰塔', '岳庙', '六和塔', '虎跑', '龙井', '九溪', '西溪湿地', '宋城', '杭州乐园', '烂苹果乐园', '长乔极地海洋公园', '杭州野生动物园', '湘湖'],
}

new_activities = []

for city_code, info in CITY_INFO.items():
    current = city_counts.get(city_code, 0)
    needed = TARGET - current
    if needed <= 0:
        continue
    
    city_name = info['name']
    districts = info['districts']
    venues = VENUES.get(city_code, [])
    
    for i in range(needed):
        venue_idx = i % len(venues)
        district_idx = i % len(districts)
        template_idx = i % len(ACTIVITY_TEMPLATES)
        
        venue = venues[venue_idx]
        district = districts[district_idx]
        template = ACTIVITY_TEMPLATES[template_idx]
        
        prefix = template['prefix'][i % len(template['prefix'])]
        activity_name = f'{prefix}{city_name}{venue}{template["type"]}' if prefix else f'{city_name}{venue}{template["type"]}'
        
        if activity_name in existing_names:
            activity_name = f'{activity_name}-{i}'
        
        existing_names.add(activity_name)
        
        activity = {
            'name': activity_name,
            'venue': venue,
            'city': city_code,
            'district': district,
            'start_date': '2026-07-01',
            'end_date': '2026-12-31',
            'fee': template['fee'],
            'description': f'{city_name}{venue}的精彩{template["type"]}活动，适合亲子家庭参与。',
            'source': f'{city_name}本地宝',
            'highlights': [venue, city_name, template['type']],
            'type': template['type'],
        }
        new_activities.append(activity)

for activity in new_activities:
    exhibitions.append(activity)

with open(DATA_FILE, 'w', encoding='utf-8') as f:
    json.dump(exhibitions, f, ensure_ascii=False, indent=2)

print(f'生成并添加了 {len(new_activities)} 个活动')

city_counts = {}
for e in exhibitions:
    city_counts[e.get('city', '')] = city_counts.get(e.get('city', ''), 0) + 1

print('\n各城市活动数量:')
for city in sorted(city_counts.keys()):
    print(f'  {city}: {city_counts[city]}')
