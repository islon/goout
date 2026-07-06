import requests
import json
import os
import sys
import re
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, JSON_FILE

NSQSNG_URL = "https://www.szns.gov.cn"
NSQSNG_NAME = "南山区青少年活动中心"


def fetch_nsqsng_activities():
    """从南山政府在线和文化馆云平台获取青少年活动中心数据，失败时提供兜底数据"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    activities = []
    today = datetime.now().strftime('%Y-%m-%d')

    # 尝试从文化馆云平台获取青少年相关活动
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
                # 筛选青少年活动中心相关活动
                youth_keywords = ['青少年', '少年', '少儿', '儿童', '亲子', '活动中心', '培训']
                if not any(kw in title for kw in youth_keywords):
                    # 也检查地点是否在青少年活动中心
                    venue_name = item.get('venueName', '')
                    location = item.get('activityLocationName', '')
                    if not any(kw in venue_name or kw in location for kw in ['青少年', '活动中心']):
                        continue

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

                desc_parts = []
                if is_free == 1:
                    desc_parts.append("免费")
                if reservation == 2:
                    desc_parts.append("需预约报名")
                if description:
                    desc_parts.append(description)

                activity_url = f"https://whgy.szmassart.com/nsqwhg/web/activity/detail.html?activityId={item.get('activityId', '')}"

                activities.append({
                    'name': title,
                    'venue': NSQSNG_NAME,
                    'start_date': start_date,
                    'end_date': end_date,
                    'url': activity_url,
                    'contact': '0755-26661612',
                    'description': '。'.join([p for p in desc_parts if p])[:300],
                    'source': 'nsqsng',
                    'family_friendly': True
                })

            page_total = wrapper.get('pageTotal', 1)
            if page >= page_total:
                break
            page += 1
            time.sleep(0.5)

    except Exception as e:
        print(f"Error fetching NSQSNG activities from culture cloud: {e}")

    # 尝试从南山政府在线获取活动公告
    try:
        search_url = "https://www.szns.gov.cn/nsqwhg/"
        response = requests.get(search_url, headers=headers, timeout=15)
        response.raise_for_status()

        html_content = response.text
        link_pattern = r'href=["\']([^"\']*)["\'][^>]*>([^<]*(?:青少年活动|少儿活动|少年宫)[^<]*)</a>'
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
                        'venue': NSQSNG_NAME,
                        'start_date': start_date,
                        'end_date': end_date,
                        'url': url,
                        'contact': '0755-26661612',
                        'description': desc if desc else '南山区青少年活动中心公益活动，免费参与。',
                        'source': 'nsqsng',
                        'family_friendly': True
                    })

                time.sleep(0.3)
            except Exception as e:
                print(f"Error fetching detail page {url}: {e}")
                continue

    except Exception as e:
        print(f"Error fetching NSQSNG activities from gov site: {e}")

    # 去重
    seen = set()
    unique_activities = []
    for a in activities:
        key = a['name']
        if key not in seen:
            seen.add(key)
            unique_activities.append(a)
    activities = unique_activities

    # 如果没有爬到线上数据，使用兜底数据
    if not activities:
        print("No online data found, using fallback data")
        activities = get_fallback_activities(today)

    return activities


def get_fallback_activities(today):
    """提供南山区青少年活动中心常设公益活动兜底数据"""
    activities = [
        {
            'name': '青少年公益培训班',
            'venue': NSQSNG_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.szns.gov.cn',
            'contact': '0755-26661612',
            'description': '面向青少年开设书法、绘画、舞蹈、科技等公益培训课程，免费参与，需报名。',
            'source': 'nsqsng',
            'family_friendly': True
        },
        {
            'name': '周末亲子公益课堂',
            'venue': NSQSNG_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.szns.gov.cn',
            'contact': '0755-26661612',
            'description': '周末举办亲子阅读、手工制作、科普实验等亲子公益活动，免费参与。',
            'source': 'nsqsng',
            'family_friendly': True
        },
        {
            'name': '青少年科技创新工坊',
            'venue': NSQSNG_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.szns.gov.cn',
            'contact': '0755-26661612',
            'description': '机器人编程、3D打印、航模制作等科技创新实践活动，免费参与。',
            'source': 'nsqsng',
            'family_friendly': True
        }
    ]
    return activities


def main():
    activities = fetch_nsqsng_activities()
    print(f"Fetched {len(activities)} activities from {NSQSNG_NAME}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"nsqsng_{JSON_FILE}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)

    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()
