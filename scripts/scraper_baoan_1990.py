import requests
import json
import os
import sys
import re
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, JSON_FILE

BAOAN_1990_URL = "https://www.sz.gov.cn"
BAOAN_1990_NAME = "宝安1990文化馆"


def fetch_baoan_1990_activities():
    """从政府网站获取宝安1990文化馆活动数据"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    activities = []
    today = datetime.now().strftime('%Y-%m-%d')

    try:
        search_url = "https://www.sz.gov.cn/search/?q=%E5%AE%9D%E5%AE%891990%E6%96%87%E5%8C%96%E9%A6%86"
        response = requests.get(search_url, headers=headers, timeout=15)
        response.raise_for_status()

        html_content = response.text
        link_pattern = r'href=["\']([^"\']*)["\'][^>]*>([^<]*宝安1990[^<]*)</a>'
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
                        'venue': BAOAN_1990_NAME,
                        'start_date': start_date,
                        'end_date': end_date,
                        'url': url,
                        'contact': '',
                        'description': desc if desc else '宝安1990文化馆展览活动，免费参与。',
                        'source': 'baoan_1990',
                        'family_friendly': True
                    })

                time.sleep(0.3)
            except Exception as e:
                print(f"Error fetching detail page {url}: {e}")
                continue

    except Exception as e:
        print(f"Error fetching BAOAN_1990 activities from gov site: {e}")

    return activities


def main():
    activities = fetch_baoan_1990_activities()
    print(f"Fetched {len(activities)} activities from {BAOAN_1990_NAME}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"baoan_1990_{JSON_FILE}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)

    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()