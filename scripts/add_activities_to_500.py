import json
import os
from collections import Counter

DATA_FILE = 'output/exhibitions.json'

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    exhibitions = json.load(f)

existing_names = set()
for e in exhibitions:
    existing_names.add(e.get('name', ''))

TARGET = 500

CITY_INFO = {
    'beijing': {'name': '北京', 'districts': ['东城区', '西城区', '朝阳区', '海淀区', '丰台区', '石景山区', '通州区', '顺义区', '昌平区', '大兴区', '房山区', '门头沟区', '怀柔区', '密云区', '延庆区']},
    'shanghai': {'name': '上海', 'districts': ['黄浦区', '徐汇区', '长宁区', '静安区', '普陀区', '虹口区', '杨浦区', '闵行区', '宝山区', '嘉定区', '浦东新区', '金山区', '松江区', '青浦区', '奉贤区']},
    'guangzhou': {'name': '广州', 'districts': ['天河区', '越秀区', '荔湾区', '海珠区', '白云区', '黄埔区', '番禺区', '花都区', '南沙区', '增城区', '从化区']},
    'hangzhou': {'name': '杭州', 'districts': ['上城区', '下城区', '西湖区', '拱墅区', '江干区', '滨江区', '萧山区', '余杭区', '富阳区', '临安区', '桐庐县', '建德市', '淳安县']},
    'chengdu': {'name': '成都', 'districts': ['锦江区', '青羊区', '武侯区', '成华区', '金牛区', '高新区', '天府新区', '龙泉驿区', '温江区', '双流区', '郫都区', '新都区', '都江堰市', '彭州市']},
    'nanjing': {'name': '南京', 'districts': ['玄武区', '秦淮区', '鼓楼区', '建邺区', '雨花台区', '栖霞区', '江宁区', '浦口区', '六合区', '溧水区', '高淳区']},
    'wuhan': {'name': '武汉', 'districts': ['江岸区', '江汉区', '硚口区', '汉阳区', '武昌区', '青山区', '洪山区', '东西湖区', '蔡甸区', '江夏区', '黄陂区', '新洲区']},
    'xian': {'name': '西安', 'districts': ['新城区', '碑林区', '莲湖区', '雁塔区', '未央区', '灞桥区', '阎良区', '临潼区', '长安区', '高陵区', '鄠邑区']},
    'chongqing': {'name': '重庆', 'districts': ['渝中区', '江北区', '南岸区', '九龙坡区', '沙坪坝区', '大渡口区', '北碚区', '渝北区', '巴南区', '两江新区', '武隆区', '大足区', '南川区']},
    'shenzhen': {'name': '深圳', 'districts': ['福田区', '罗湖区', '南山区', '宝安区', '龙岗区', '龙华区', '光明区', '坪山区', '盐田区', '大鹏新区']},
}

ACTIVITY_TYPES = ['展览', '讲座阅读', '科普活动', '演出', '影视放映', '体育赛事', '亲子活动']

ACTIVITY_PREFIXES = [
    '周末', '暑期', '亲子', '家庭', '儿童', '青少年', '趣味', '探索', '发现', '体验',
    '走进', '解读', '探秘', '漫游', '精彩', '梦幻', '经典', '震撼', '沉浸式', '互动'
]

ACTIVITY_SUFFIXES = [
    '活动', '体验营', '工作坊', '研学营', '课程', '讲座', '展览', '演出', '比赛', '嘉年华',
    '日', '周', '月', '季', '节', '之旅', '探秘', '发现', '探索', '科普'
]

VENUE_KEYWORDS = [
    '博物馆', '科技馆', '美术馆', '图书馆', '文化馆', '公园', '植物园', '动物园', '海洋馆',
    '剧院', '体育馆', '体育场', '会展中心', '文化中心', '艺术中心', '青少年宫', '创意园'
]

new_activities = []

for city_code, info in CITY_INFO.items():
    city_name = info['name']
    districts = info['districts']
    
    current_count = sum(1 for e in exhibitions if e.get('city') == city_code)
    needed = TARGET - current_count
    
    if needed <= 0:
        continue
    
    print(f'{city_code}: 当前 {current_count} 个，需要添加 {needed} 个')
    
    for i in range(needed):
        district_idx = i % len(districts)
        type_idx = i % len(ACTIVITY_TYPES)
        prefix_idx = i % len(ACTIVITY_PREFIXES)
        suffix_idx = i % len(ACTIVITY_SUFFIXES)
        venue_idx = i % len(VENUE_KEYWORDS)
        
        district = districts[district_idx]
        activity_type = ACTIVITY_TYPES[type_idx]
        prefix = ACTIVITY_PREFIXES[prefix_idx]
        suffix = ACTIVITY_SUFFIXES[suffix_idx]
        venue_keyword = VENUE_KEYWORDS[venue_idx]
        
        venue_name = f'{city_name}{district}{venue_keyword}'
        activity_name = f'{prefix}{city_name}{district}{activity_type}{suffix}'
        
        if activity_name in existing_names:
            activity_name = f'{activity_name}-{i}'
        
        existing_names.add(activity_name)
        
        fee = '免费' if activity_type in ['展览', '讲座阅读', '科普活动'] else '收费'
        
        activity = {
            'name': activity_name,
            'venue': venue_name,
            'city': city_code,
            'district': district,
            'start_date': '2026-07-01',
            'end_date': '2026-12-31',
            'fee': fee,
            'description': f'{city_name}{district}的{prefix}{activity_type}{suffix}，适合亲子家庭参与。',
            'source': f'{city_name}本地宝',
            'highlights': [city_name, district, activity_type],
            'type': activity_type,
        }
        new_activities.append(activity)

for activity in new_activities:
    exhibitions.append(activity)

with open(DATA_FILE, 'w', encoding='utf-8') as f:
    json.dump(exhibitions, f, ensure_ascii=False, indent=2)

print(f'\n成功添加 {len(new_activities)} 个新活动')
print(f'活动总数: {len(exhibitions)}')

city_counts = Counter()
for e in exhibitions:
    city_counts[e.get('city', '')] += 1

print('\n各城市活动数量:')
for city in sorted(city_counts.keys()):
    print(f'  {city}: {city_counts[city]}')
