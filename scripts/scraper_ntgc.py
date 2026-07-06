import requests
import json
import os
import sys
import re
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, JSON_FILE

NTGC_URL = "https://www.szns.gov.cn"
NTGC_NAME = "南头古城博物馆群"


def fetch_ntgc_activities():
    """从南山政府在线获取南头古城博物馆群活动数据，失败时提供常设展兜底数据"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    activities = []
    today = datetime.now().strftime('%Y-%m-%d')

    # 尝试从南山政府在线获取活动公告
    try:
        search_url = "https://www.szns.gov.cn/nsqwhg/"
        response = requests.get(search_url, headers=headers, timeout=15)
        response.raise_for_status()

        html_content = response.text
        # 查找包含"南头古城"相关的链接
        link_pattern = r'href=["\']([^"\']*)["\'][^>]*>([^<]*南头古城[^<]*)</a>'
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
                        'venue': NTGC_NAME,
                        'start_date': start_date,
                        'end_date': end_date,
                        'url': url,
                        'contact': '0755-26603800',
                        'description': desc if desc else '南头古城博物馆群活动公告，免费参观。',
                        'source': 'ntgc',
                        'family_friendly': True
                    })

                time.sleep(0.3)
            except Exception as e:
                print(f"Error fetching detail page {url}: {e}")
                continue

    except Exception as e:
        print(f"Error fetching NTGC activities from gov site: {e}")

    # 如果没有爬到线上数据，使用常设展兜底
    if not activities:
        print("No online data found, using permanent exhibition fallback data")
        activities = get_permanent_exhibitions(today)

    return activities


def get_permanent_exhibitions(today):
    """提供南头古城博物馆群常设展览兜底数据"""
    exhibitions = [
        {
            'name': '南头古城历史展',
            'venue': '南头古城博物馆',
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.szns.gov.cn',
            'contact': '0755-26603800',
            'description': '展示南头古城1700年历史变迁，包括古城考古发掘、城池演变等内容，免费参观。',
            'source': 'ntgc',
            'family_friendly': True
        },
        {
            'name': '陈郁故居生平事迹展',
            'venue': '陈郁故居',
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.szns.gov.cn',
            'contact': '0755-26603800',
            'description': '展示无产阶级革命家陈郁同志生平事迹与革命历史，免费参观。',
            'source': 'ntgc',
            'family_friendly': True
        },
        {
            'name': '南头古城非遗文化展',
            'venue': '南头古城博物馆',
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.szns.gov.cn',
            'contact': '0755-26603800',
            'description': '展示南山区非物质文化遗产项目与传统民俗文化，免费参观。',
            'source': 'ntgc',
            'family_friendly': True
        }
    ]
    return exhibitions


def main():
    activities = fetch_ntgc_activities()
    print(f"Fetched {len(activities)} activities from {NTGC_NAME}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"ntgc_{JSON_FILE}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)

    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()
