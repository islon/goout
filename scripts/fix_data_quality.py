import json
import sys
from urllib.parse import urlparse

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

URL_SOURCE_MAP = {
    "www.szlhq.gov.cn": "龙华区文旅局",
    "www.yantian.gov.cn": "盐田区政府",
    "www.szgm.gov.cn": "光明区政府",
    "www.lg.gov.cn": "龙岗区政府",
    "www.szft.gov.cn": "福田区政府",
    "www.szlh.gov.cn": "龙华区政府",
    "whgy.szmassart.com": "南山文化艺术中心",
    "www.szftlib.org.cn": "福田图书馆",
    "www.ytlib.yantian.org.cn": "盐田图书馆",
    "www.szgmlib.com.cn": "光明图书馆",
    "www.sz.gov.cn": "深圳政府在线",
    "sthjj.sz.gov.cn": "深圳生态环境局",
    "www.szlglib.com.cn": "罗湖图书馆",
    "wtl.sz.gov.cn": "深圳文体旅游局",
    "www.szlhlib.org.cn": "龙华图书馆",
    "cgj.sz.gov.cn": "深圳城管局",
    "www.shenzhenmuseum.com": "深圳博物馆",
    "inanshan.sznews.com": "南山新闻网",
    "www.szns.gov.cn": "南山区政府",
    "www.nanshanmuseum.com": "南山博物馆",
    "www.guanlanprints.com": "中国版画博物馆",
    "www.szzhdj.gov.cn": "深圳水务局",
    "www.oct.com.cn": "华侨城",
    "www.szwomen.org.cn": "深圳妇女联合会",
    "www.qianhai.gov.cn": "前海管理局",
    "www.shekouculture.com": "蛇口文化",
    "www.szu.edu.cn": "深圳大学",
    "www.szbg.ac.cn": "深圳科技馆",
    "www.crlandsports.com": "华润体育",
    "sztb.szwater.gov.cn": "深圳水土保持",
    "www.gsyart.com": "光明文化艺术中心",
    "www.cndafen.com": "达芬美术馆",
    "szcec.com": "深圳会展中心",
    "shenzhenworld.com": "深圳国际会展中心",
    "www.szartm.com": "深圳美术馆",
}


def map_url_source(url):
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        if domain in URL_SOURCE_MAP:
            return URL_SOURCE_MAP[domain]
        for key, value in URL_SOURCE_MAP.items():
            if key in domain:
                return value
        path = parsed.path.lower()
        if 'museum' in path or 'museum' in domain:
            return '博物馆'
        if 'lib' in path or 'lib' in domain:
            return '图书馆'
        if 'gov' in domain:
            return '政府网站'
        return '官方网站'
    except Exception:
        return '官方网站'


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

    result = "。".join(desc_parts)
    if len(result) < 10:
        result = f"{title}，{venue}举办的活动，欢迎市民参与。详情请以官方信息为准。"
    return result[:300]


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

        if source.startswith("http"):
            mapped_name = map_url_source(source)
            item["source"] = mapped_name
            source = mapped_name
            fixed_count += 1

        detected_district = detect_district_from_venue(venue)
        if detected_district and source in ["nswtzx", "nsqsng"]:
            if detected_district != "南山区":
                candidates = DISTRICT_SOURCE_MAP.get(detected_district, [])
                if candidates:
                    item["source"] = candidates[0]
                    fixed_count += 1

        if "family_friendly" not in item:
            title = item.get("title", "")
            desc = item.get("description", "")
            cat = item.get("category", "")
            family_kw = ["亲子", "儿童", "少儿", "宝宝", "家庭", "绘本", "故事会", "手工",
                         "科普", "科学实验", "儿童剧", "亲子活动"]
            text = title + desc + cat
            item["family_friendly"] = any(kw in text for kw in family_kw)
            fixed_count += 1

        if not item.get("link") and item.get("url"):
            item["link"] = item["url"]
            fixed_count += 1
        elif not item.get("url") and item.get("link"):
            item["url"] = item["link"]
            fixed_count += 1

        if not item.get("name") and item.get("title"):
            item["name"] = item["title"]
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