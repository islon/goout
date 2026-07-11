import requests
import json
import os
import sys
import re
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, JSON_FILE

NSWTZX_URL = "https://www.szns.gov.cn"
NSWTZX_NAME = "南山文体中心"

VENUE_SOURCE_MAP = {
    '南山文体中心': 'nswtzx',
    '南山区文化馆': 'nswhg',
    '南山': 'nswtzx',
    '桃源街道': 'nswtzx',
    '宝安区文化馆': 'baoan_1990',
    '宝安': 'baoan_1990',
    '燕罗': 'baoan_1990',
    '新桥': 'baoan_1990',
    '光明区文化馆': 'gmwhg',
    '光明': 'gmwhg',
    '公明': 'gmwhg',
    '马田': 'gmwhg',
    '玉塘': 'gmwhg',
    '塘家': 'gmwhg',
    '甲子塘': 'gmwhg',
    '迳口': 'gmwhg',
    '龙岗': 'lgwhg',
    '龙城': 'lgwhg',
    '坪地': 'lgwhg',
    '坂田': 'lgwhg',
    '吉华': 'lgwhg',
    '南湾': 'lgwhg',
    '平湖': 'lgwhg',
    '龙华': 'lhwhg',
    '罗湖': 'lhwhg2',
    '园岭': 'lhwhg2',
    '福田': 'ftwhg',
    '安托山': 'ftwhg',
    '梦工场': 'ftwhg',
    '盐田': 'ytwhg',
    '坪山': 'pswhg',
    '大鹏': 'dpwhg',
}

DEFAULT_SOURCE = 'szmassart'


def get_source_from_venue(venue_name):
    """根据场馆名称映射到对应的 source key"""
    if not venue_name:
        return DEFAULT_SOURCE
    for keyword, source_key in VENUE_SOURCE_MAP.items():
        if keyword in venue_name:
            return source_key
    return DEFAULT_SOURCE


def fetch_nswtzx_activities():
    """从文化馆云平台获取全市文化馆活动数据，按场馆映射到正确的source"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    activities = []
    today = datetime.now().strftime('%Y-%m-%d')

    # 从文化馆云平台获取文化馆活动
    try:
        api_url = "https://whgy.szmassart.com/nsqwhg/web/activity/list"
        api_headers = {
            'User-Agent': headers['User-Agent'],
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://whgy.szmassart.com',
            'Referer': 'https://whgy.szmassart.com/nsqwhg/web/activity/list.html',
        }

        page = 1
        max_pages = 10
        while page <= max_pages:
            params = {'page': page, 'size': 50}
            response = requests.post(api_url, headers=api_headers, data=params, timeout=15)
            response.raise_for_status()

            data = response.json()
            wrapper = data.get('data', {})
            if not wrapper or not isinstance(wrapper, dict):
                break

            items = wrapper.get('data', [])
            if not items:
                break

            for item in items:
                title = item.get('activityName', '')
                venue_name = item.get('venueName', '')
                location = item.get('activityLocationName', '')

                start_date = item.get('activityStartTime', '')
                end_date = item.get('activityEndTime', '')
                if not start_date:
                    continue
                if not end_date:
                    end_date = start_date
                if end_date < today:
                    continue

                description = item.get('activityProfile', '') or item.get('tagName', '')
                is_free = item.get('activityIsFree', 0)
                reservation = item.get('activityIsReservation', 0)
                tag = item.get('tagName', '')

                desc_parts = []
                if description and len(description) >= 15:
                    desc_parts.append(description)
                elif tag and description == tag:
                    pass
                elif description:
                    desc_parts.append(description)

                fee_info = "免费参与" if is_free == 1 else "收费活动"
                desc_parts.append(fee_info)

                if reservation == 2:
                    desc_parts.append("需预约报名")
                if venue_name:
                    desc_parts.append(f"地点：{venue_name}")

                final_desc = '。'.join([p for p in desc_parts if p])[:300]
                if len(final_desc) < 20:
                    extra = f"{title}。"
                    if venue_name:
                        extra += f"地点：{venue_name}。"
                    final_desc = extra + final_desc

                activity_url = f"https://whgy.szmassart.com/nsqwhg/web/activity/detail.html?activityId={item.get('activityId', '')}"

                family_keywords = ['少儿', '亲子', '儿童', '青少年', '少年']
                family_friendly = any(kw in title for kw in family_keywords)

                source_key = get_source_from_venue(venue_name or location)

                activities.append({
                    'name': title,
                    'venue': venue_name or NSWTZX_NAME,
                    'start_date': start_date,
                    'end_date': end_date,
                    'url': activity_url,
                    'contact': '0755-86051111',
                    'description': final_desc,
                    'source': source_key,
                    'family_friendly': family_friendly
                })

            page_total = wrapper.get('pageTotal', 1)
            if page >= page_total:
                break
            page += 1
            time.sleep(0.5)

    except Exception as e:
        print(f"Error fetching NSWVTZX activities from culture cloud: {e}")

    # 尝试从南山政府在线获取活动公告
    try:
        search_url = "https://www.szns.gov.cn/nsqwhg/"
        response = requests.get(search_url, headers=headers, timeout=15)
        response.raise_for_status()

        html_content = response.text
        link_pattern = r'href=["\']([^"\']*)["\'][^>]*>([^<]*文体中心[^<]*)</a>'
        links = re.findall(link_pattern, html_content)

        for href, text in links[:10]:
            url = href if href.startswith('http') else f"https://www.szns.gov.cn{href}"
            try:
                detail_resp = requests.get(url, headers=headers, timeout=10)
                detail_resp.raise_for_status()
                detail_text = detail_resp.text

                title_match = re.search(r'<title>([^<]+)</title>', detail_text)
                name = title_match.group(1).strip() if title_match else text.strip()
                name = re.sub(r'[-_].*$', '', name).strip()

                date_matches = re.findall(r'(\d{4})年(\d{1,2})月(\d{1,2})日', detail_text)
                start_date = ''
                end_date = ''
                if date_matches:
                    start_date = f"{date_matches[0][0]}-{int(date_matches[0][1]):02d}-{int(date_matches[0][2]):02d}"
                    if len(date_matches) > 1:
                        end_date = f"{date_matches[-1][0]}-{int(date_matches[-1][1]):02d}-{int(date_matches[-1][2]):02d}"
                    else:
                        end_date = start_date

                desc = ''
                content_match = re.search(r'class="[^"]*content[^"]*"[\s\S]*?>([\s\S]*?)</div>', detail_text)
                if content_match:
                    desc = re.sub(r'<[^>]+>', '', content_match.group(1))
                    desc = re.sub(r'\s+', ' ', desc).strip()[:300]

                if start_date and end_date >= today:
                    activities.append({
                        'name': name,
                        'venue': NSWTZX_NAME,
                        'start_date': start_date,
                        'end_date': end_date,
                        'url': url,
                        'contact': '0755-86051111',
                        'description': desc if desc else '南山文体中心活动，详情请查看官网。',
                        'source': 'nswtzx',
                        'family_friendly': True
                    })

                time.sleep(0.3)
            except Exception as e:
                print(f"Error fetching detail page {url}: {e}")
                continue

    except Exception as e:
        print(f"Error fetching NSWVTZX activities from gov site: {e}")

    # 去重
    seen = set()
    unique_activities = []
    for a in activities:
        key = a['name']
        if key not in seen:
            seen.add(key)
            unique_activities.append(a)
    activities = unique_activities

    return activities


def main():
    activities = fetch_nswtzx_activities()
    print(f"Fetched {len(activities)} activities from {NSWTZX_NAME}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"nswtzx_{JSON_FILE}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)

    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()
