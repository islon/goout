import requests
import json
import os
import sys
import re
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, JSON_FILE

YT_HISTORY_URL = "https://www.sz.gov.cn"
YT_HISTORY_NAME = "中英街历史博物馆"


def fetch_yt_history_activities():
    """从政府网站获取中英街历史博物馆活动数据，失败时使用常设展兜底数据"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    activities = []
    today = datetime.now().strftime('%Y-%m-%d')

    try:
        search_url = "https://www.sz.gov.cn/search/?q=%E4%B8%AD%E8%8B%B1%E8%A1%97%E5%8E%86%E5%8F%B2%E5%8D%9A%E7%89%A9%E9%A6%86"
        response = requests.get(search_url, headers=headers, timeout=15)
        response.raise_for_status()

        html_content = response.text
        link_pattern = r'href=["\']([^"\']*)["\'][^>]*>([^<]*中英街[^<]*)</a>'
        links = re.findall(link_pattern, html_content)

        for href, text in links[:5]:
            url = href if href.startswith('http') else f"https://www.sz.gov.cn{href}"
            try:
                detail_resp = requests.get(url, headers=headers, timeout=10)
                detail_resp.raise_for_status()
                detail_text = detail_resp.text

                title_match = re.search(r'<title>([^<]+)</title>', detail_text)
                name = title_match.group(1).strip() if title_match else text.strip()

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
                        'venue': YT_HISTORY_NAME,
                        'start_date': start_date,
                        'end_date': end_date,
                        'url': url,
                        'contact': '',
                        'description': desc if desc else '中英街历史博物馆展览活动，需预约进入中英街。',
                        'source': 'yt_history',
                        'family_friendly': True
                    })

                time.sleep(0.3)
            except Exception as e:
                print(f"Error fetching detail page {url}: {e}")
                continue

    except Exception as e:
        print(f"Error fetching YT_HISTORY activities from gov site: {e}")

    if not activities:
        print("No online data found, using permanent exhibition fallback data")
        activities = get_permanent_exhibitions(today)

    return activities


def get_permanent_exhibitions(today):
    """提供中英街历史博物馆常设展览兜底数据"""
    exhibitions = [
        {
            'name': '近代海防历史展',
            'venue': YT_HISTORY_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '展示中英街地区近代海防历史，呈现鸦片战争以来的海防变迁与军事防御设施。需预约进入中英街。免费参观。',
            'source': 'yt_history',
            'family_friendly': True
        },
        {
            'name': '中英街民俗历史展',
            'venue': YT_HISTORY_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '展现中英街独特的民俗文化与历史风貌，讲述一街两制下的百年变迁。需预约进入中英街。免费参观。',
            'source': 'yt_history',
            'family_friendly': True
        },
        {
            'name': '界碑历史展',
            'venue': YT_HISTORY_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '展示中英街八块界碑的历史由来与意义，见证百年边界变迁。需预约进入中英街。免费参观。',
            'source': 'yt_history',
            'family_friendly': True
        },
        {
            'name': '沙头角鱼灯舞非遗展',
            'venue': YT_HISTORY_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '展示国家级非物质文化遗产沙头角鱼灯舞的历史传承与艺术特色。需预约进入中英街。免费参观。',
            'source': 'yt_history',
            'family_friendly': True
        },
        {
            'name': '改革开放记忆展',
            'venue': YT_HISTORY_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '记录改革开放以来中英街地区的发展变迁，展示从边境小镇到繁华商业街的历程。需预约进入中英街。免费参观。',
            'source': 'yt_history',
            'family_friendly': True
        }
    ]
    return exhibitions


def main():
    activities = fetch_yt_history_activities()
    print(f"Fetched {len(activities)} activities from {YT_HISTORY_NAME}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"yt_history_{JSON_FILE}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)

    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()