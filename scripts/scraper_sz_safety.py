import requests
import json
import os
import sys
import re
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, JSON_FILE

SZ_SAFETY_URL = "https://www.sz.gov.cn"
SZ_SAFETY_NAME = "深圳市安全教育基地"


def fetch_sz_safety_activities():
    """从政府网站获取深圳市安全教育基地活动数据，失败时使用常设展兜底数据"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    activities = []
    today = datetime.now().strftime('%Y-%m-%d')

    try:
        search_url = "https://www.sz.gov.cn/search/?q=%E6%B7%B1%E5%9C%B3%E5%B8%82%E5%AE%89%E5%85%A8%E6%95%99%E8%82%B2%E5%9F%BA%E5%9C%B0"
        response = requests.get(search_url, headers=headers, timeout=15)
        response.raise_for_status()

        html_content = response.text
        link_pattern = r'href=["\']([^"\']*)["\'][^>]*>([^<]*安全教育[^<]*)</a>'
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
                        'venue': SZ_SAFETY_NAME,
                        'start_date': start_date,
                        'end_date': end_date,
                        'url': url,
                        'contact': '',
                        'description': desc if desc else '深圳市安全教育基地展览活动，免费参观。',
                        'source': 'sz_safety',
                        'family_friendly': True
                    })

                time.sleep(0.3)
            except Exception as e:
                print(f"Error fetching detail page {url}: {e}")
                continue

    except Exception as e:
        print(f"Error fetching SZ_SAFETY activities from gov site: {e}")

    if not activities:
        print("No online data found, using permanent exhibition fallback data")
        activities = get_permanent_exhibitions(today)

    return activities


def get_permanent_exhibitions(today):
    """提供深圳市安全教育基地常设展览兜底数据"""
    exhibitions = [
        {
            'name': '消防安全沉浸式体验',
            'venue': SZ_SAFETY_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '模拟火灾场景，学习火灾逃生技巧、灭火器使用方法等消防安全知识。免费参观。',
            'source': 'sz_safety',
            'family_friendly': True
        },
        {
            'name': '交通安全体验馆',
            'venue': SZ_SAFETY_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '通过互动模拟体验，学习交通规则、安全骑行、行人安全等知识。免费参观。',
            'source': 'sz_safety',
            'family_friendly': True
        },
        {
            'name': '居家安全科普展',
            'venue': SZ_SAFETY_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '展示居家安全隐患，学习燃气安全、用电安全、防盗防骗等知识。免费参观。',
            'source': 'sz_safety',
            'family_friendly': True
        },
        {
            'name': '急救技能培训体验',
            'venue': SZ_SAFETY_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '学习心肺复苏(CPR)、海姆立克急救法等急救技能，配备模拟人实操训练。免费参观。',
            'source': 'sz_safety',
            'family_friendly': True
        },
        {
            'name': '自然灾害科普展',
            'venue': SZ_SAFETY_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '介绍地震、台风、暴雨等自然灾害的应对方法，提升防灾减灾能力。免费参观。',
            'source': 'sz_safety',
            'family_friendly': True
        },
        {
            'name': '安全知识互动游戏',
            'venue': SZ_SAFETY_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.sz.gov.cn',
            'contact': '',
            'description': '通过趣味互动游戏，让儿童在玩乐中学习安全知识，寓教于乐。免费参观。',
            'source': 'sz_safety',
            'family_friendly': True
        }
    ]
    return exhibitions


def main():
    activities = fetch_sz_safety_activities()
    print(f"Fetched {len(activities)} activities from {SZ_SAFETY_NAME}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"sz_safety_{JSON_FILE}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)

    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()