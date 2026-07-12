import json
import sys

ALLOWED_FEES = {"免费", "免费需预约", "收费", "部分免费", "需购票"}

SOURCE_DISTRICT_MAP = {
    "nsmuseum": "南山区",
    "nslib": "南山区",
    "nswhg": "南山区",
    "nsaqjy": "南山区",
    "nssxf": "南山区",
    "nswtzx": "南山区",
    "nsqsng": "南山区",
    "szlib": "福田区",
    "gm_lib": "光明区",
    "gm_kjg": "光明区",
    "lh_paleo": "龙华区",
    "lh_ecology": "龙华区",
    "lh_printmaking": "龙华区",
    "lg_hakka": "龙岗区",
    "baoan_1990": "宝安区",
    "balib": "宝安区",
    "dp_geopark": "大鹏新区",
    "dp_nuclear": "大鹏新区",
    "ps_nature": "坪山区",
    "oct_wetland": "南山区",
    "octohbay": "南山区",
    "sarc": "盐田区",
    "zsjbwg": "宝安区",
    "yt_history": "盐田区",
    "yt_lib": "盐田区",
    "sz_safety": "光明区",
    "sz_children_lib": "福田区",
    "ntgc": "南山区",
    "skhykpg": "罗湖区",
    "szwty": "福田区",
    "shenzhen_world": "宝安区",
    "szcec": "福田区",
}

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


def detect_district_from_venue(venue):
    for district, keywords in VENUE_DISTRICT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in venue:
                return district
    return None


def check_data_quality(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    issues = []
    
    for idx, item in enumerate(data):
        item_id = idx + 1
        
        fee = item.get("fee", "")
        if fee and fee not in ALLOWED_FEES:
            issues.append(f"Item #{item_id}: Invalid fee '{fee}'. Must be one of {ALLOWED_FEES}")
        
        description = item.get("description", "")
        if len(description) < 10:
            issues.append(f"Item #{item_id}: Description too short ({len(description)} chars): '{description}'")
        
        source = item.get("source", "")
        venue = item.get("venue", "")
        
        if source in SOURCE_DISTRICT_MAP:
            expected_district = SOURCE_DISTRICT_MAP[source]
            detected_district = detect_district_from_venue(venue)
            
            if detected_district and detected_district != expected_district:
                issues.append(f"Item #{item_id}: District mismatch - source '{source}' expects '{expected_district}' but venue '{venue}' detected as '{detected_district}'")
    
    return issues


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_data_quality.py <json_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    issues = check_data_quality(filepath)
    
    if issues:
        print(f"Found {len(issues)} data quality issues:")
        for issue in issues:
            print(f"  - {issue}")
        sys.exit(1)
    else:
        print("No data quality issues found.")
        sys.exit(0)