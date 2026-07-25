#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
根据场馆信息补全活动的district字段
"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")

DISTRICT_KEYWORDS = {
    '福田区': ['福田', '市民中心', '少年宫', '莲花山', '会展中心', '华强北', '购物公园', '车公庙', '香蜜湖', '梅林', '景田', '竹子林', '皇岗', '保税区', '沙头角', '石厦', '岗厦', '八卦岭', '园岭', '华富', '莲花', '福田口岸', '深圳图书馆', '深圳博物馆', '改革开放展览馆', '历史民俗馆', '古代艺术馆', '深圳美术馆（新馆）', '深圳美术馆(新馆)', '中心馆'],
    '南山区': ['南山', '科技园', '华侨城', '世界之窗', '欢乐谷', '深圳湾', '蛇口', '后海', '前海', '西丽', '大学城', '南头', '粤海', '沙河', '招商', '桃源', '南山博物馆', '南山图书馆', '南山文体中心', '深圳大学', '海岸城', '海上世界', '赤湾', '塘朗', '万象天地', '国际美术馆', '四海公园', '松坪公园', '石鼓山公园', '丽湖公园', '留仙洞', '桂湾公园', '锦绣中华', '中轴云廊', '顶上空间', '人才公园', '何香凝美术馆', '南山书房', '南头古城', '中国版画博物馆'],
    '罗湖区': ['罗湖', '东门', '国贸', '地王', '京基100', '笋岗', '翠竹', '东湖', '莲塘', '清水河', '东晓', '南湖', '桂园', '黄贝', '翠竹', '深圳图书馆', '深圳博物馆', '大剧院', '万象城', '金光华'],
    '宝安区': ['宝安', '西乡', '福永', '沙井', '松岗', '新安', '石岩', '航城', '福海', '新桥', '燕罗', '宝安中心', '宝安体育馆', '宝安图书馆', '宝体', '灵芝', '翻身', '坪洲', '固戍', '碧海湾'],
    '龙岗区': ['龙岗', '布吉', '坂田', '南湾', '平湖', '横岗', '龙城', '坪地', '葵涌', '大鹏', '南澳', '大运', '龙岗中心', '龙岗体育馆', '龙城广场', '万科城', '华为'],
    '龙华区': ['龙华', '民治', '大浪', '观澜', '福城', '观湖', '龙华书城', '龙华图书馆', '深圳北站', '红山', '上塘', '清湖', '观澜湖'],
    '盐田区': ['盐田', '沙头角', '梅沙', '海山', '盐田港', '大小梅沙', '东部华侨城', '中英街', '梧桐山', '明思克'],
    '光明区': ['光明', '公明', '光明城', '光明农场', '光明科学城', '公明', '玉律', '长圳', '凤凰城'],
    '坪山区': ['坪山', '坑梓', '坪山中心', '坪山体育馆', '坪山图书馆', '马峦山', '燕子湖'],
    '大鹏新区': ['大鹏', '葵涌', '南澳', '大鹏半岛', '较场尾', '杨梅坑', '东西涌', '东冲', '西冲', '金沙湾', '七娘山'],
    '罗湖区': ['罗湖', '东门', '国贸', '地王', '京基', '笋岗', '翠竹', '东湖', '莲塘', '清水河'],
}

def infer_district(venue_name, venue_map=None, all_venues=None):
    if venue_map and venue_name in venue_map:
        venue = venue_map[venue_name]
        if venue.get('district'):
            return venue['district']
    
    if all_venues:
        for v in all_venues:
            vname = v.get('name', '')
            if vname and v.get('district'):
                if vname in venue_name or venue_name in vname:
                    return v['district']
    
    for district, keywords in DISTRICT_KEYWORDS.items():
        for kw in keywords:
            if kw in venue_name:
                return district
    
    return ''

def main():
    exhibitions_path = os.path.join(OUTPUT_DIR, "exhibitions.json")
    venues_path = os.path.join(OUTPUT_DIR, "venue_info.json")
    
    with open(exhibitions_path, "r", encoding="utf-8") as f:
        exhibitions = json.load(f)
    
    with open(venues_path, "r", encoding="utf-8") as f:
        venues = json.load(f)
    
    venue_map = {}
    for v in venues:
        if v.get('name'):
            venue_map[v['name']] = v
    
    # 先修复场馆的district
    fixed_venues = 0
    for v in venues:
        if not v.get('district') and v.get('name'):
            district = infer_district(v['name'], venue_map, venues)
            if district:
                v['district'] = district
                fixed_venues += 1
    
    with open(venues_path, "w", encoding="utf-8") as f:
        json.dump(venues, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 已补全 {fixed_venues} 个场馆的district字段")
    
    # 再修复活动的district
    fixed_count = 0
    shenzhen_venues = [v for v in venues if v.get('city') == 'shenzhen']
    for e in exhibitions:
        if not e.get('district') and e.get('venue'):
            district = infer_district(e['venue'], venue_map, shenzhen_venues)
            if district:
                e['district'] = district
                fixed_count += 1
    
    with open(exhibitions_path, "w", encoding="utf-8") as f:
        json.dump(exhibitions, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 已补全 {fixed_count} 条活动的district字段")
    
    # 重新生成分城市文件
    import sys
    sys.path.insert(0, SCRIPT_DIR)
    from generate_city_exhibitions import main as gen_city
    print("\n重新生成分城市活动文件...")
    gen_city()
    
    from generate_city_venues import main as gen_venues
    print("\n重新生成分城市场馆文件...")
    gen_venues()
    
    from generate_tiered import main as gen_tiered
    print("\n重新生成分级活动文件...")
    gen_tiered()
    
    from generate_data_meta import main as gen_meta
    print("\n重新生成数据元数据...")
    gen_meta()

if __name__ == "__main__":
    main()
