#!/usr/bin/env python3
"""
generate_filters.py — 从 venue_info.json 动态生成小程序 filters.js 的映射表

城市列表 (cities) 保持手动维护 —— 新增城市必须与用户确认后手动添加。
其余所有映射表（区县、场馆、地址等）全部从 venue_info.json 自动生成，
更新场馆数据后无需修改任何代码。

用法：
    python scripts/generate_filters.py

生成内容：
  - districtMapping       source key → 区县名
  - sourceToVenue         source key → 场馆中文名
  - venueAddressMap       场馆名 → 地址
  - districtsByCity       城市 → 区县列表
  - venuesByCity          城市 → 场馆列表（含全部地点）
  - sourceChineseToDistrict  中文场馆名 → 区县（兜底）
  - districtKeywords      区县关键字 → 区县名（兜底）

保留手动维护：
  - cities                城市列表（新增城市需确认）
  - timeFilters           时间筛选
  - familyFilters         亲子筛选
  - typeFilters           类型筛选
  - feeFilters            费用筛选
"""

import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'output')
VENUE_INFO_PATH = os.path.join(OUTPUT_DIR, 'venue_info.json')
FILTERS_OUT_PATH = os.path.join(PROJECT_ROOT, 'miniprogram', 'data', 'filters.js')

# 各区县常住人口(2020 七普, 万人) —— 区县筛选按人口降序排序的依据。
# 人口缺失的区县在排序时落到末尾，不影响"全部区县"置顶。
DISTRICT_POPULATION = {
    # 深圳
    '宝安区': 447, '龙岗区': 397, '龙华区': 253, '南山区': 180, '福田区': 156,
    '罗湖区': 114, '光明区': 110, '坪山区': 55, '盐田区': 21, '大鹏新区': 15,
    # 广州
    '白云区': 374, '番禺区': 266, '天河区': 224, '海珠区': 182, '花都区': 170,
    '增城区': 146, '黄埔区': 126, '荔湾区': 123, '越秀区': 116, '南沙区': 84, '从化区': 71,
    # 上海
    '浦东新区': 568, '闵行区': 265, '宝山区': 223, '松江区': 191, '嘉定区': 184,
    '杨浦区': 131, '青浦区': 130, '普陀区': 129, '徐汇区': 111, '奉贤区': 114,
    '静安区': 98, '金山区': 82, '虹口区': 76, '长宁区': 69, '黄浦区': 66,
    # 北京
    '朝阳区': 345, '海淀区': 313, '昌平区': 227, '丰台区': 202, '大兴区': 199,
    '通州区': 184, '顺义区': 132, '房山区': 131, '西城区': 110, '东城区': 92,
    '石景山区': 57, '密云区': 46, '平谷区': 46, '怀柔区': 41, '门头沟区': 39, '延庆区': 23,
    # 杭州
    '萧山区': 205, '上城区': 133, '余杭区': 122, '临平区': 117, '富阳区': 83,
    '西湖区': 81, '钱塘区': 80, '建德市': 78, '桐庐县': 75, '拱墅区': 109,
    '临安区': 64, '滨江区': 53, '淳安县': 51,
    # 成都
    '郫都区': 167, '新都区': 156, '双流区': 146, '龙泉驿区': 135, '温江区': 99,
    '金牛区': 126, '武侯区': 121, '成华区': 96, '青羊区': 96, '锦江区': 90,
    '高新区': 130, '天府新区': 90, '都江堰市': 71,
    # 南京
    '江宁区': 156, '浦口区': 117, '鼓楼区': 94, '栖霞区': 98, '六合区': 94,
    '玄武区': 61, '秦淮区': 74, '建邺区': 48, '雨花台区': 46, '溧水区': 50, '高淳区': 43,
    # 武汉
    '洪山区': 172, '江夏区': 147, '武昌区': 128, '黄陂区': 115, '蔡甸区': 92,
    '东西湖区': 88, '硚口区': 83, '江汉区': 73, '汉阳区': 67, '江岸区': 71,
    '新洲区': 86, '青山区': 49,
    # 西安
    '雁塔区': 204, '长安区': 164, '未央区': 160, '碑林区': 76, '莲湖区': 71,
    '新城区': 62, '灞桥区': 70, '临潼区': 68, '高陵区': 30, '阎良区': 28, '鄠邑区': 39,
    # 重庆
    '渝北区': 219, '九龙坡区': 153, '沙坪坝区': 148, '南岸区': 120, '巴南区': 118,
    '江北区': 91, '北碚区': 84, '璧山区': 76, '渝中区': 58, '大渡口区': 43,
    # 珠海
    '香洲区': 112, '斗门区': 61, '金湾区': 44,
}


def load_venues():
    with open(VENUE_INFO_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_manual_cities():
    """从现有 filters.js 读取手动维护的城市列表（保持不变）"""
    import re
    filters_path = os.path.join(PROJECT_ROOT, 'miniprogram', 'data', 'filters.js')
    if not os.path.exists(filters_path):
        return None
    try:
        with open(filters_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # 提取 cities 数组里的每一项
        m = re.search(r'const cities = \[(.*?)\];', content, re.DOTALL)
        if not m:
            return None
        array_body = m.group(1)
        # 逐行提取 { key: 'xxx', name: 'yyy' }
        cities = []
        # 匹配每一条：{ key: 'xxx', name: 'yyy' }
        pattern = re.compile(r"\{\s*key:\s*'([^']+)'\s*,\s*name:\s*'([^']+)'\s*\}")
        for match in pattern.finditer(array_body):
            cities.append({'key': match.group(1), 'name': match.group(2)})
        if cities:
            return cities
    except Exception as e:
        print(f'⚠️  读取现有 cities 失败: {e}')
    return None


def generate_mappings(venues):
    district_mapping = {}
    source_to_venue = {}
    venue_address_map = {}
    districts_by_city = {}
    venues_by_city = {}
    source_chinese_to_district = {}
    district_keywords_set = set()

    for v in venues:
        name = v.get('name', '')
        source = v.get('source', '')
        city = v.get('city', '')
        district = v.get('district', '')
        address = v.get('address', '')

        if not name or not city:
            continue

        # districtMapping: source key → 区县
        if source and district:
            district_mapping[source] = district

        # sourceToVenue: source key → 场馆中文名
        if source:
            source_to_venue[source] = name

        # venueAddressMap: 场馆名 → 地址
        if address:
            venue_address_map[name] = address

        # districtsByCity: 城市 → 区县列表
        if city not in districts_by_city:
            districts_by_city[city] = set()
        if district:
            districts_by_city[city].add(district)

        # venuesByCity: 城市 → 场馆列表
        if city not in venues_by_city:
            venues_by_city[city] = []
        venues_by_city[city].append({
            'key': source if source else name,
            'name': name
        })

        # sourceChineseToDistrict: 中文场馆名 → 区县（兜底）
        if name and district:
            source_chinese_to_district[name] = district

        # districtKeywords: 区县关键字
        if district:
            district_keywords_set.add(district)

    # 区县列表排序：按常住人口降序（"全部区县"放最前），人口缺失的落到末尾
    for city in districts_by_city:
        districts_by_city[city] = ['全部区县'] + sorted(
            districts_by_city[city],
            key=lambda d: -DISTRICT_POPULATION.get(d, 0))

    # 场馆列表按名称排序，"全部地点"放最前
    for city in venues_by_city:
        venues_by_city[city].sort(key=lambda x: x['name'])
        venues_by_city[city].insert(0, {'key': 'all', 'name': '全部地点'})

    # districtKeywords 按字符串长度降序（长的优先匹配）
    district_keywords = sorted(
        [[kw, kw] for kw in district_keywords_set],
        key=lambda x: -len(x[0])
    )

    return {
        'districtMapping': district_mapping,
        'sourceToVenue': source_to_venue,
        'venueAddressMap': venue_address_map,
        'districtsByCity': districts_by_city,
        'districtPopulation': DISTRICT_POPULATION,
        'venuesByCity': venues_by_city,
        'sourceChineseToDistrict': source_chinese_to_district,
        'districtKeywords': district_keywords,
    }


def js_obj(obj, indent=2):
    """Python dict/list → 漂亮的 JS 对象字符串"""
    import io
    out = io.StringIO()

    def write_val(v, level):
        pad = ' ' * (level * indent)
        pad_inner = ' ' * ((level + 1) * indent)

        if isinstance(v, dict):
            if not v:
                out.write('{}')
                return
            out.write('{\n')
            items = list(v.items())
            for i, (k, val) in enumerate(items):
                # key 加引号（含特殊字符的 key 需要）
                key_str = f"'{k}'" if not k.replace('_', '').replace('-', '').isalnum() or k[0].isdigit() else k
                comma = ',' if i < len(items) - 1 else ''
                out.write(f"{pad_inner}{key_str}: ")
                write_val(val, level + 1)
                out.write(f"{comma}\n")
            out.write(f"{pad}}}")

        elif isinstance(v, list):
            if not v:
                out.write('[]')
                return
            # 判断是不是简单的短数组（如字符串数组）
            all_simple = all(isinstance(x, str) and len(x) < 10 for x in v)
            if all_simple and len(v) <= 15:
                # 单行输出
                items = [f"'{x}'" for x in v]
                out.write('[' + ', '.join(items) + ']')
                return

            out.write('[\n')
            for i, item in enumerate(v):
                comma = ',' if i < len(v) - 1 else ''
                out.write(pad_inner)
                write_val(item, level + 1)
                out.write(f"{comma}\n")
            out.write(f"{pad}]")

        elif isinstance(v, str):
            out.write(f"'{v}'")

        elif isinstance(v, bool):
            out.write('true' if v else 'false')

        elif isinstance(v, (int, float)):
            out.write(str(v))

        elif v is None:
            out.write('null')

        else:
            out.write(f"'{str(v)}'")

    write_val(obj, 0)
    return out.getvalue()


def render_filters_js(cities, mappings):
    lines = []

    lines.append('// 童行小程序 - 筛选器配置')
    lines.append('// 自动生成：由 scripts/generate_filters.py 从 venue_info.json 生成')
    lines.append('// 城市列表(cities)手动维护，其余映射表自动生成')
    lines.append('')

    # cities（手动维护，原样输出）
    lines.append('// 城市列表（手动维护，新增城市需确认）')
    lines.append(f'const cities = {js_obj(cities, 2)};')
    lines.append('')

    # 时间筛选
    lines.append('// 时间筛选')
    lines.append('const timeFilters = [')
    lines.append("  { key: 'upcoming', name: '最近活动' },")
    lines.append("  { key: 'today', name: '今天' },")
    lines.append("  { key: 'tomorrow', name: '明天' },")
    lines.append("  { key: 'week', name: '本周' },")
    lines.append("  { key: 'month', name: '本月' },")
    lines.append("  { key: 'next_month', name: '下月' },")
    lines.append("  { key: 'all', name: '全部活动' }")
    lines.append('];')
    lines.append('')

    # 亲子筛选
    lines.append('// 亲子筛选')
    lines.append('const familyFilters = [')
    lines.append("  { key: 'all', name: '全部活动' },")
    lines.append("  { key: 'family', name: '适合亲子' },")
    lines.append("  { key: 'other', name: '其他活动' }")
    lines.append('];')
    lines.append('')

    # 类型筛选
    lines.append('// 类型筛选')
    lines.append('const typeFilters = [')
    lines.append("  { key: 'all', name: '全部类型' },")
    lines.append("  { key: '展览', name: '展览' },")
    lines.append("  { key: '讲座阅读', name: '讲座阅读' },")
    lines.append("  { key: '科普活动', name: '科普活动' },")
    lines.append("  { key: '演出', name: '演出' },")
    lines.append("  { key: '影视放映', name: '影视放映' },")
    lines.append("  { key: '体育赛事', name: '体育赛事' },")
    lines.append("  { key: '亲子活动', name: '亲子活动' }")
    lines.append('];')
    lines.append('')

    # 费用筛选
    lines.append('// 费用筛选')
    lines.append('const feeFilters = [')
    lines.append("  { key: 'all', name: '全部' },")
    lines.append("  { key: 'free', name: '免费' },")
    lines.append("  { key: 'paid', name: '收费' }")
    lines.append('];')
    lines.append('')

    # 活动持续时长筛选
    lines.append('// 活动持续时长筛选（按 end_date - start_date + 1 天数）')
    lines.append('const durationFilters = [')
    lines.append("  { key: 'all', name: '全部时长活动' },")
    lines.append("  { key: 'week', name: '1周内' },")
    lines.append("  { key: '3months', name: '3个月内' },")
    lines.append("  { key: 'long', name: '3个月以上' }")
    lines.append('];')
    lines.append('')

    # districtMapping
    lines.append('// 区县映射（自动生成）')
    lines.append(f'const districtMapping = {js_obj(mappings["districtMapping"])};')
    lines.append('')

    # sourceToVenue
    lines.append('// source key 到场馆名映射（自动生成）')
    lines.append(f'const sourceToVenue = {js_obj(mappings["sourceToVenue"])};')
    lines.append('')

    # venueAddressMap
    lines.append('// 场馆地址映射（自动生成）')
    lines.append(f'const venueAddressMap = {js_obj(mappings["venueAddressMap"])};')
    lines.append('')

    # districtsByCity
    lines.append('// 按城市分组区县（自动生成，按人口降序）')
    lines.append(f'const districtsByCity = {js_obj(mappings["districtsByCity"])};')
    lines.append('')

    # districtPopulation
    lines.append('// 区县常住人口(2020 七普, 万人)，用于区县筛选按人口降序')
    lines.append(f'const districtPopulation = {js_obj(mappings["districtPopulation"])};')
    lines.append('')

    # sourceChineseToDistrict
    lines.append('// 中文 source 名称 → 区名映射（自动生成，兜底用）')
    lines.append(f'const sourceChineseToDistrict = {js_obj(mappings["sourceChineseToDistrict"])};')
    lines.append('')

    # districtKeywords
    lines.append('// 区县关键字兜底（自动生成，按长度降序）')
    lines.append(f'const districtKeywords = {js_obj(mappings["districtKeywords"])};')
    lines.append('')

    # venuesByCity
    lines.append('// 按城市分组场馆（自动生成）')
    lines.append(f'const venuesByCity = {js_obj(mappings["venuesByCity"])};')
    lines.append('')

    # module.exports
    lines.append('module.exports = {')
    lines.append('  cities,')
    lines.append('  timeFilters,')
    lines.append('  familyFilters,')
    lines.append('  typeFilters,')
    lines.append('  feeFilters,')
    lines.append('  durationFilters,')
    lines.append('  districtMapping,')
    lines.append('  sourceToVenue,')
    lines.append('  venueAddressMap,')
    lines.append('  districtsByCity,')
    lines.append('  districtPopulation,')
    lines.append('  venuesByCity,')
    lines.append('  sourceChineseToDistrict,')
    lines.append('  districtKeywords')
    lines.append('};')
    lines.append('')

    return '\n'.join(lines)


def main():
    print('=' * 60)
    print('生成小程序 filters.js 映射表')
    print('=' * 60)
    print()

    # 1. 加载场馆数据
    if not os.path.exists(VENUE_INFO_PATH):
        print(f'❌ 场馆数据不存在: {VENUE_INFO_PATH}')
        sys.exit(1)

    venues = load_venues()
    print(f'✅ 加载场馆数据: {len(venues)} 条')

    # 2. 读取现有的城市列表（手动维护）
    cities = load_manual_cities()
    if cities:
        print(f'✅ 读取城市列表（手动维护）: {len(cities)} 城')
        for c in cities:
            print(f'    - {c["name"]} ({c["key"]})')
    else:
        # 兜底：从 venue_info.json 提取城市列表
        # 但根据规则，新增城市必须确认，所以如果读不到现有 cities，应该报错
        print('❌ 无法读取现有 cities，请确认 miniprogram/data/filters.js 存在')
        sys.exit(1)

    print()

    # 3. 生成映射表
    print('生成映射表...')
    mappings = generate_mappings(venues)

    print(f'  districtMapping:       {len(mappings["districtMapping"])} 条')
    print(f'  sourceToVenue:         {len(mappings["sourceToVenue"])} 条')
    print(f'  venueAddressMap:       {len(mappings["venueAddressMap"])} 条')
    print(f'  districtsByCity:       {len(mappings["districtsByCity"])} 城')
    for city, ds in sorted(mappings['districtsByCity'].items()):
        print(f'    {city}: {len(ds) - 1} 个区县')
    print(f'  venuesByCity:          {len(mappings["venuesByCity"])} 城')
    for city, vs in sorted(mappings['venuesByCity'].items(), key=lambda x: -len(x[1])):
        print(f'    {city}: {len(vs) - 1} 个场馆')
    print(f'  sourceChineseToDistrict: {len(mappings["sourceChineseToDistrict"])} 条')
    print(f'  districtKeywords:      {len(mappings["districtKeywords"])} 个区县')

    # 4. 检查：venuesByCity 中的城市是否都在 cities 里
    city_keys = set(c['key'] for c in cities)
    extra_cities = set(mappings['venuesByCity'].keys()) - city_keys
    if extra_cities:
        print()
        print('⚠️  注意：venue_info.json 中有以下城市不在 cities 列表中：')
        for c in sorted(extra_cities):
            print(f'    - {c}')
        print('   （新增城市需与用户确认后手动添加到 cities 数组）')

    missing_cities = city_keys - set(mappings['venuesByCity'].keys())
    if missing_cities:
        print()
        print('⚠️  注意：cities 列表中有以下城市在 venue_info.json 中找不到数据：')
        for c in sorted(missing_cities):
            print(f'    - {c}')

    print()

    # 5. 写入文件
    os.makedirs(os.path.dirname(FILTERS_OUT_PATH), exist_ok=True)
    content = render_filters_js(cities, mappings)
    with open(FILTERS_OUT_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

    size_kb = os.path.getsize(FILTERS_OUT_PATH) // 1024
    print(f'✅ 已写入 {FILTERS_OUT_PATH} ({size_kb} KB)')
    print()
    print('=' * 60)
    print('完成')
    print('=' * 60)


if __name__ == '__main__':
    main()
