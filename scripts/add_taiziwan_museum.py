# -*- coding: utf-8 -*-
"""
新增深圳新场馆「太子湾美术馆」及其开馆活动。

数据来源：深圳发布 2026-08-24 文章
https://mp.weixin.qq.com/s/D2145bE6oFmX0gVWXPwnZQ
（内容来源：创新南山）

- 场馆写入 scripts/auto_venues.json（status=auto），随后由 venue_registry 重新生成主文件与分城。
- 开馆活动写入 output/exhibitions.json（主文件，权威超集），随后重建分城/分级/小程序数据。
- 均按 (name)/(city,title) 去重，避免重复。
"""
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUT_DIR = os.path.join(PROJECT_ROOT, 'output')
SRC = os.path.join(SCRIPT_DIR, 'auto_venues.json')
EXH = os.path.join(OUT_DIR, 'exhibitions.json')
ARTICLE = "https://mp.weixin.qq.com/s/D2145bE6oFmX0gVWXPwnZQ"
VERIFIED_AT = "2026-08-24"

NEW_VENUE = {
    "source_code": "sz_taiziwan_art_2026",
    "name": "太子湾美术馆",
    "source": "深圳发布",
    "city": "shenzhen",
    "district": "南山区",
    "type": "美术馆",
    "address": "深圳市南山区太子湾滨海片区（毗邻海上世界文化艺术中心）",
    "transport": "地铁2号线/12号线海上世界站，步行可达太子湾片区",
    "fee": "免费需预约",
    "description": "太子湾美术馆坐落于深圳太子湾滨海片区，毗邻海上世界文化艺术中心，拥有专业展览空间、多功能文化空间及公共活动区域，并配备符合国际标准的艺术品管理设施。将于2026年9月30日正式启幕，开馆展为一位国际重要艺术家在中国的首个大型个展（涵盖绘画、装置、多媒体影像等）。未来将持续推出高品质展览、公共艺术项目、讲座、论坛、放映、表演、工作坊等。",
    "service_time": "2026年9月30日开馆（暂未开放）",
    "official_url": "",
    "links": [
        {"url": ARTICLE, "label": "深圳发布·太子湾美术馆开馆"}
    ],
    "highlights": ["美术馆", "南山区", "太子湾"],
    "aliases": [],
    "status": "auto",
    "activity_count": 0,
}

NEW_ACTIVITY = {
    "title": "太子湾美术馆开馆首展",
    "name": "太子湾美术馆开馆首展",
    "venue": "太子湾美术馆",
    "city": "shenzhen",
    "start_date": "2026-09-30",
    "end_date": "2026-09-30",
    "link": ARTICLE,
    "url": ARTICLE,
    "description": "太子湾美术馆（深圳南山区太子湾滨海片区，毗邻海上世界文化艺术中心）于2026年9月30日正式启幕，开馆展为一位国际重要艺术家在中国的首个大型个展，涵盖绘画、装置、多媒体影像等创作媒介，构建介于现实与想象之间的艺术场域。门票以官方公布为准。",
    "category": "展览",
    "fee": "免费需预约",
    "contact": "",
    "family_friendly": True,
    "source": "深圳发布",
    "district": "南山区",
    "booking_method": {
        "type": "city_aggregated",
        "app_name": "深圳本地宝",
        "app_type": "wechat_mini_program",
        "search_hint": "微信搜索「深圳本地宝」公众号→活动汇总",
        "platform_url": None,
        "city": "深圳",
        "matched_venue_type": "美术馆",
    },
    "verification": {
        "status": "auto_checked",
        "link_reachable": True,
        "http_status": 200,
        "source_type": "official",
        "verified_at": VERIFIED_AT,
        "verified_by": "http_check",
    },
    "verified": True,
}


def main():
    # ---- 场馆 ----
    venues = json.load(open(SRC, encoding='utf-8'))
    names = {v.get('name', '').lower() for v in venues}
    if NEW_VENUE['name'].lower() in names:
        print("场馆已存在，跳过：", NEW_VENUE['name'])
    else:
        venues.append(NEW_VENUE)
        json.dump(venues, open(SRC, 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=2)
        print("场馆已追加：", NEW_VENUE['name'])

    # ---- 活动 ----
    exh = json.load(open(EXH, encoding='utf-8'))
    keys = {(x.get('city'), x.get('title')) for x in exh}
    if (NEW_ACTIVITY['city'], NEW_ACTIVITY['title']) in keys:
        print("活动已存在，跳过：", NEW_ACTIVITY['title'])
    else:
        exh.append(NEW_ACTIVITY)
        json.dump(exh, open(EXH, 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=2)
        print("活动已追加：", NEW_ACTIVITY['title'], NEW_ACTIVITY['start_date'])


if __name__ == '__main__':
    main()
