"""统一文化馆云平台爬虫

从 whgy.szmassart.com API 拉取全市所有区的文化活动数据。
该 API 返回宝安、福田、龙岗、光明、南山等全部区的活动，用 curl 绕过
Python requests 的 SSL BAD_ECPOINT 问题。
"""

import json
import os
import sys
import time
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from http_utils import curl_post

API_URL = "https://whgy.szmassart.com/nsqwhg/web/activity/list"
API_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://whgy.szmassart.com',
    'Referer': 'https://whgy.szmassart.com/nsqwhg/web/activity/list.html',
}

# 区域名映射
DISTRICT_MAP = {
    '宝安区': '宝安', '福田区': '福田', '龙岗区': '龙岗', '光明区': '光明',
    '南山区': '南山', '龙华区': '龙华', '坪山区': '坪山', '盐田区': '盐田',
    '大鹏新区': '大鹏', '罗湖区': '罗湖',
}


def fetch_culture_cloud_activities():
    """从文化馆云平台拉取全市活动数据"""
    activities = []
    today = datetime.now().strftime('%Y-%m-%d')
    seen_ids = set()

    for page in range(1, 4):
        data_str = f"page={page}&size=50"
        raw = curl_post(API_URL, data=data_str, headers=API_HEADERS, timeout=20)
        if not raw:
            print(f"  culture cloud page {page}: 请求失败")
            break

        try:
            resp = json.loads(raw)
        except json.JSONDecodeError:
            print(f"  culture cloud page {page}: JSON解析失败")
            break

        wrapper = resp.get('data', {})
        if not isinstance(wrapper, dict):
            break

        items = wrapper.get('data', [])
        if not items:
            break

        page_total = wrapper.get('pageTotal', 1)
        new_count = 0

        for item in items:
            aid = item.get('activityId', '')
            if aid in seen_ids:
                continue
            seen_ids.add(aid)
            new_count += 1

            title = item.get('activityName', '').strip()
            if not title:
                continue

            start_date = item.get('activityStartTime', '')
            end_date = item.get('activityEndTime', '') or start_date
            if not start_date:
                continue
            if end_date < today:
                continue

            venue_name = item.get('venueName', '') or ''
            location = item.get('activityLocationName', '') or ''
            area_str = item.get('activityArea', '') or ''
            district = ''
            for dist_full, dist_short in DISTRICT_MAP.items():
                if dist_full in area_str:
                    district = dist_short
                    break

            desc = item.get('activityProfile', '') or item.get('activityIntro', '') or ''
            tag_name = item.get('tagName', '') or ''
            host = item.get('activityHost', '') or ''
            if not desc:
                desc_parts = []
                if tag_name:
                    desc_parts.append(tag_name)
                if host:
                    desc_parts.append(host)
                if venue_name:
                    desc_parts.append(f"在{venue_name}举办")
                desc = '，'.join(desc_parts) if desc_parts else title
            if len(desc) < 10:
                desc = f"{title}，{tag_name}活动，在{venue_name or '文化馆'}举办。"

            is_free = item.get('activityIsFree', 0)
            reservation = item.get('activityIsReservation', 0)
            if is_free == 1:
                if reservation == 2:
                    fee = '免费需预约'
                else:
                    fee = '免费'
            else:
                fee = '收费'

            family_kw = ['少儿', '亲子', '儿童', '青少年', '少年', '暑期', '暑假']
            family_friendly = any(kw in title for kw in family_kw)

            activity_url = f"https://whgy.szmassart.com/nsqwhg/web/activity/detail.html?activityId={aid}"

            activities.append({
                'title': title,
                'name': title,
                'venue': venue_name or (f'{district}文化馆' if district else '深圳市文化馆'),
                'start_date': start_date,
                'end_date': end_date,
                'link': activity_url,
                'url': activity_url,
                'description': desc[:300],
                'fee': fee,
                'contact': '',
                'family_friendly': family_friendly,
                'source': venue_name or '文化馆云平台',
                'city': 'shenzhen',
            })

        print(f"  culture cloud page {page}/{page_total}: 新增 {new_count} 条，累计 {len(activities)} 条")
        if new_count == 0:
            break
        if page >= page_total:
            break
        time.sleep(0.5)

    return activities


def main():
    activities = fetch_culture_cloud_activities()
    print(f"\n共获取 {len(activities)} 条活动")

    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from config import OUTPUT_DIR
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, 'culture_cloud_exhibitions.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)
    print(f"已保存到 {out_path}")


if __name__ == '__main__':
    main()
