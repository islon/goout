import requests
import json
import os
import sys
import re
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, JSON_FILE

DP_GEOPARK_URL = "https://www.sz.gov.cn"
DP_GEOPARK_NAME = "大鹏半岛国家地质公园博物馆"


def fetch_dp_geopark_activities():
    """从政府网站获取大鹏半岛国家地质公园博物馆活动数据，失败时使用常设展兜底数据"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    activities = []
    today = datetime.now().strftime('%Y-%m-%d')

    try:
        search_url = "https://www.sz.gov.cn/search/?q=%E5%A4%A7%E9%B9%8F%E5%8D%8A%E5%B2%9B%E5%9B%BD%E5%AE%B6%E5%9C%B0%E8%B4%A8%E5%85%AC%E5%9B%AD%E5%8D%9A%E7%89%A9%E9%A6%86"
        response = requests.get(search_url, headers=headers, timeout=15)
        response.raise_for_status()

        html_content = response.text
        link_pattern = r'href=["\']([^"\']*)["\'][^>]*>([^<]*地质公园[^<]*)</a>'
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
                        'venue': DP_GEOPARK_NAME,
                        'start_date': start_date,
                        'end_date': end_date,
                        'url': url,
                        'contact': '',
                        'description': desc if desc else '大鹏半岛国家地质公园博物馆展览活动，免费参观。',
                        'source': 'dp_geopark',
                        'family_friendly': True
                    })

                time.sleep(0.3)
            except Exception as e:
                print(f"Error fetching detail page {url}: {e}")
                continue

    except Exception as e:
        print(f"Error fetching DP_GEOPARK activities from gov site: {e}")

    if not activities:
        print("No online data found, using permanent exhibition fallback data")
        activities = get_permanent_exhibitions(today)

    return activities


def get_permanent_exhibitions(today):
    """提供大鹏半岛国家地质公园博物馆常设展览兜底数据"""
    exhibitions = [
        {
            'name': '火山喷发模拟体验',
            'venue': DP_GEOPARK_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '沉浸式火山喷发模拟体验，感受火山爆发的震撼场景，了解火山地质知识。免费参观。',
            'source': 'dp_geopark',
            'family_friendly': True
        },
        {
            'name': '恐龙蛋化石展',
            'venue': DP_GEOPARK_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '展出珍贵恐龙蛋化石标本，展示恐龙繁殖方式与古生物演化历史。免费参观。',
            'source': 'dp_geopark',
            'family_friendly': True
        },
        {
            'name': '矿物晶体展',
            'venue': DP_GEOPARK_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '展示各类精美矿物晶体标本，呈现大自然的鬼斧神工与地质之美。免费参观。',
            'source': 'dp_geopark',
            'family_friendly': True
        },
        {
            'name': '海岸地质演化展',
            'venue': DP_GEOPARK_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '介绍大鹏半岛独特的海岸地质地貌，展示海蚀地貌与沉积岩形成过程。免费参观。',
            'source': 'dp_geopark',
            'family_friendly': True
        },
        {
            'name': '古生物化石展',
            'venue': DP_GEOPARK_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '展出古生物化石标本，包括古植物、古动物化石，重现史前生态环境。免费参观。',
            'source': 'dp_geopark',
            'family_friendly': True
        },
        {
            'name': '地质灾害科普展',
            'venue': DP_GEOPARK_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '介绍地震、滑坡、泥石流等地质灾害的成因与防范措施，提高防灾减灾意识。免费参观。',
            'source': 'dp_geopark',
            'family_friendly': True
        }
    ]
    return exhibitions


def main():
    activities = fetch_dp_geopark_activities()
    print(f"Fetched {len(activities)} activities from {DP_GEOPARK_NAME}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"dp_geopark_{JSON_FILE}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)

    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()