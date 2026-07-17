import json
import os

DATA_DIR = 'output'
EXHIBITIONS_FILE = os.path.join(DATA_DIR, 'exhibitions.json')
VENUES_FILE = os.path.join(DATA_DIR, 'venue_info.json')

# 读取现有数据
with open(EXHIBITIONS_FILE, 'r', encoding='utf-8') as f:
    exhibitions = json.load(f)

with open(VENUES_FILE, 'r', encoding='utf-8') as f:
    venues = json.load(f)

existing_venue_names = {v['name'] for v in venues}

# 收集活动中出现但场馆列表中不存在的venue，同时记录对应的source
unmatched_venues = {}
for e in exhibitions:
    venue = e.get('venue', '').strip()
    if not venue:
        continue
    
    # 检查是否已经匹配（精确匹配或包含匹配）
    matched = False
    for vname in existing_venue_names:
        if vname == venue or vname in venue or venue in vname:
            matched = True
            break
    
    if not matched:
        city = e.get('city', '')
        district = e.get('district', '')
        source = e.get('source', '')
        if city not in unmatched_venues:
            unmatched_venues[city] = {}
        if venue not in unmatched_venues[city]:
            unmatched_venues[city][venue] = {
                'district': district,
                'count': 0,
                'sources': set()
            }
        unmatched_venues[city][venue]['count'] += 1
        if source:
            unmatched_venues[city][venue]['sources'].add(source)

# 生成新场馆数据
new_venues = []

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

TYPE_KEYWORDS = {
    '博物馆': '博物馆',
    '科技馆': '科技馆',
    '美术馆': '美术馆',
    '纪念馆': '纪念馆',
    '图书馆': '图书馆',
    '文化馆': '文化馆',
    '公园': '公园',
    '动物园': '动物园',
    '植物园': '植物园',
    '湿地': '公园',
    '乐园': '主题乐园',
    '广场': '广场',
    '剧院': '剧场',
    '体育馆': '体育场馆',
    '体育场': '体育场馆',
    '学校': '教育机构',
    '学院': '教育机构',
    '景区': '风景区',
    '度假区': '度假村',
    '古镇': '历史文化景点',
    '街区': '历史文化景点',
    '故居': '历史文化景点',
    '寺': '宗教场所',
    '宫': '宗教场所',
    '庙': '宗教场所',
    '祠堂': '宗教场所',
    '馆': '其他',
}

FEE_KEYWORDS = {
    '博物馆': '免费',
    '科技馆': '免费',
    '美术馆': '免费',
    '纪念馆': '免费',
    '图书馆': '免费',
    '文化馆': '免费',
    '公园': '免费',
    '湿地': '免费',
    '广场': '免费',
    '故居': '免费',
    '寺': '免费',
    '宫': '免费',
    '庙': '免费',
    '动物园': '收费',
    '植物园': '收费',
    '乐园': '收费',
    '度假区': '收费',
    '古镇': '免费',
    '景区': '收费',
    '剧院': '收费',
    '体育馆': '收费',
    '学校': '免费',
    '学院': '免费',
    '街区': '免费',
}

def infer_type(name):
    for kw, vtype in TYPE_KEYWORDS.items():
        if kw in name:
            return vtype
    return '其他'

def infer_fee(name):
    for kw, fee in FEE_KEYWORDS.items():
        if kw in name:
            return fee
    return '免费'

for city, venues_info in unmatched_venues.items():
    city_name = CITY_NAME_MAP.get(city, city)
    for venue_name, info in venues_info.items():
        district = info['district']
        vtype = infer_type(venue_name)
        fee = infer_fee(venue_name)
        
        # 使用活动中记录的source作为场馆的唯一标识，确保活动和场馆能正确关联
        sources = info.get('sources', set())
        source = ''
        if sources:
            # 优先选择短的、非中文的source（如 szlib），避免选择"深圳本地宝"这类来源标识
            # 同时过滤掉中文场馆名作为source的情况
            preferred = [s for s in sources if len(s) <= 20 and not any('\u4e00' <= c <= '\u9fff' for c in s)]
            source = preferred[0] if preferred else list(sources)[0]
        
        new_venue = {
            'name': venue_name,
            'source': source or f'{city_name}本地宝',
            'city': city,
            'district': district,
            'type': vtype,
            'address': '',
            'transport': '',
            'fee': fee,
            'description': f'{city_name}{venue_name}，提供各类亲子活动和展览。',
            'official_url': '',
            'highlights': [vtype, city_name]
        }
        new_venues.append(new_venue)

print(f'发现 {len(new_venues)} 个活动中出现但场馆列表中缺失的场馆')

# 添加到场馆列表
added_count = 0
for new_v in new_venues:
    if new_v['name'] not in existing_venue_names:
        venues.append(new_v)
        added_count += 1

with open(VENUES_FILE, 'w', encoding='utf-8') as f:
    json.dump(venues, f, ensure_ascii=False, indent=2)

print(f'成功添加 {added_count} 个新场馆')
print(f'场馆总数: {len(venues)}')

# 验证匹配情况
updated_venue_names = {v['name'] for v in venues}
still_unmatched = 0
for e in exhibitions:
    venue = e.get('venue', '')
    matched = False
    for vname in updated_venue_names:
        if vname == venue or vname in venue or venue in vname:
            matched = True
            break
    if not matched:
        still_unmatched += 1

print(f'验证结果: 仍有 {still_unmatched} 个活动场馆未匹配')
