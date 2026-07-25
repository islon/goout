import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")

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
    '体育馆': '体育中心',
    '体育场': '体育中心',
    '学校': '教育机构',
    '学院': '教育机构',
    '景区': '公园',
    '度假区': '度假区',
    '古镇': '历史文化景点',
    '街区': '历史文化街区',
    '故居': '历史文化景点',
    '寺': '寺庙',
    '宫': '寺庙',
    '庙': '寺庙',
    '祠堂': '寺庙',
    '会展中心': '会展中心',
    '文化中心': '文化中心',
    '艺术中心': '艺术中心',
    '青少年宫': '青少年活动中心',
    '少年宫': '青少年活动中心',
    '科普馆': '科普馆',
    '展览中心': '展览馆',
    '博览中心': '展览馆',
    '体育馆': '体育中心',
    '游泳馆': '体育中心',
    '奥体中心': '体育中心',
    '演艺中心': '剧院',
    '音乐厅': '剧院',
    '中心': '文化中心',
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
    '会展中心': '视展览而定',
    '文化中心': '免费',
    '艺术中心': '收费',
    '青少年宫': '免费',
    '科普馆': '免费',
}

ACTIVITY_TYPES = {'展览', '讲座阅读', '科普活动', '演出', '影视放映', '体育赛事', '亲子活动', '研学', '讲座'}

CITY_NAME_MAP = {
    'beijing': '北京',
    'shanghai': '上海',
    'guangzhou': '广州',
    'shenzhen': '深圳',
    'hangzhou': '杭州',
    'chengdu': '成都',
    'nanjing': '南京',
    'wuhan': '武汉',
    'xian': '西安',
    'chongqing': '重庆',
    'zhuhai': '珠海',
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

def fix_venue(venue, city_name):
    changed = False
    
    if 'type' in venue and venue['type'] in ACTIVITY_TYPES:
        venue['type'] = infer_type(venue['name'])
        changed = True
    
    if 'fee' not in venue or not venue['fee']:
        venue['fee'] = infer_fee(venue['name'])
        changed = True
    
    if 'transport' not in venue:
        venue['transport'] = ''
    
    if 'official_url' not in venue:
        venue['official_url'] = ''
    
    if 'highlights' not in venue or not venue['highlights']:
        venue['highlights'] = [venue['type'], city_name]
    
    if 'description' not in venue or not venue['description']:
        venue['description'] = f'{city_name}{venue["name"]}，提供各类亲子活动和展览。'
    
    return changed

def main():
    src = os.path.join(OUTPUT_DIR, "venue_info.json")
    if not os.path.exists(src):
        print("❌ venue_info.json 不存在:", src)
        return
    
    with open(src, "r", encoding="utf-8") as f:
        venues = json.load(f)
    
    total_changed = 0
    for venue in venues:
        city = venue.get('city', '')
        city_name = CITY_NAME_MAP.get(city, city)
        if fix_venue(venue, city_name):
            total_changed += 1
    
    with open(src, "w", encoding="utf-8") as f:
        json.dump(venues, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 已修复 {total_changed} 个场馆数据")
    
    from generate_city_venues import main as regenerate
    print("\n重新生成分城市场馆文件...")
    regenerate()

if __name__ == "__main__":
    main()
