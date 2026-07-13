import json
import sys

ALLOWED_FEES = {"免费", "免费需预约", "收费", "部分免费", "需购票"}

VENUE_DISTRICT_KEYWORDS = {
    "南山区": ["南山", "南头", "蛇口", "科技园", "华侨城", "前海", "后海"],
    "福田区": ["福田", "市中心", "华强北", "CBD"],
    "罗湖区": ["罗湖", "东门", "笋岗"],
    "宝安区": ["宝安", "沙井", "福永", "西乡", "松岗"],
    "龙岗区": ["龙岗", "坪山", "横岗", "布吉"],
    "龙华区": ["龙华", "观澜"],
    "光明区": ["光明"],
    "盐田区": ["盐田", "沙头角"],
    "大鹏新区": ["大鹏", "葵涌", "南澳"],
    "坪山区": ["坪山"],
}

DISTRICT_SOURCE_MAP = {
    "南山区": ["nsmuseum", "nslib", "nswhg", "nsaqjy", "nssxf", "nswtzx", "nsqsng", "oct_wetland", "octohbay", "ntgc"],
    "福田区": ["szlib", "sz_children_lib", "szwty", "szcec"],
    "罗湖区": ["skhykpg"],
    "宝安区": ["baoan_1990", "balib", "zsjbwg", "shenzhen_world"],
    "龙岗区": ["lg_hakka"],
    "龙华区": ["lh_paleo", "lh_ecology", "lh_printmaking"],
    "光明区": ["gm_lib", "gm_kjg", "sz_safety"],
    "盐田区": ["sarc", "yt_history", "yt_lib"],
    "大鹏新区": ["dp_geopark", "dp_nuclear"],
    "坪山区": ["ps_nature"],
}


def detect_district_from_venue(venue):
    for district, keywords in VENUE_DISTRICT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in venue:
                return district
    return None


def generate_description(item):
    title = item.get("title", "")
    category = item.get("category", "")
    fee = item.get("fee", "")
    venue = item.get("venue", "")
    
    category_desc = {
        "展览": "展览活动，欢迎市民前往参观欣赏",
        "演出": "精彩演出活动，带来视听盛宴",
        "讲座阅读": "讲座阅读活动，丰富知识视野",
        "亲子活动": "亲子互动活动，增进家庭感情",
        "培训": "培训课程活动，提升技能水平",
        "综合": "综合性文化活动，内容丰富多样",
    }
    
    base_desc = category_desc.get(category, "文化活动")
    
    if fee:
        fee_text = f"{fee}"
    else:
        fee_text = ""
    
    desc_parts = []
    if fee_text:
        desc_parts.append(fee_text)
    if venue:
        desc_parts.append(f"地点：{venue}")
    if title:
        desc_parts.append(f"{title}。{base_desc}")
    
    return "。".join(desc_parts)


def fix_data_quality(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    fixed_count = 0
    
    for item in data:
        fee = item.get("fee", "")
        if fee and fee not in ALLOWED_FEES:
            item["fee"] = "免费"
            fixed_count += 1
        
        description = item.get("description", "")
        if len(description) < 10:
            new_desc = generate_description(item)
            item["description"] = new_desc
            fixed_count += 1
        
        source = item.get("source", "")
        venue = item.get("venue", "")
        
        detected_district = detect_district_from_venue(venue)
        if detected_district and source in ["nswtzx", "nsqsng"]:
            if detected_district != "南山区":
                candidates = DISTRICT_SOURCE_MAP.get(detected_district, [])
                if candidates:
                    item["source"] = candidates[0]
                    fixed_count += 1
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return fixed_count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fix_data_quality.py <json_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    fixed_count = fix_data_quality(filepath)
    print(f"Fixed {fixed_count} data quality issues.")