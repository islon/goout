import requests
import json
import os
import sys
import re
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, JSON_FILE

NSAQJY_URL = "https://www.szns.gov.cn"
NSAQJY_NAME = "南山安全教育体验馆"


def fetch_nsaqjy_activities():
    """从南山政府在线获取南山安全教育体验馆活动数据，失败时提供常设展兜底数据"""
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
        # 查找包含"安全教育"或"体验馆"相关的链接
        link_pattern = r'href=["\']([^"\']*)["\'][^>]*>([^<]*(?:安全教育|安全体验)[^<]*)</a>'
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
                        'venue': NSAQJY_NAME,
                        'start_date': start_date,
                        'end_date': end_date,
                        'url': url,
                        'contact': '0755-26738119',
                        'description': desc if desc else '南山安全教育体验馆活动，免费需预约。',
                        'source': 'nsaqjy',
                        'family_friendly': True
                    })

                time.sleep(0.3)
            except Exception as e:
                print(f"Error fetching detail page {url}: {e}")
                continue

    except Exception as e:
        print(f"Error fetching NSAQJY activities from gov site: {e}")

    # 如果没有爬到线上数据，使用常设体验项目兜底
    if not activities:
        print("No online data found, using permanent exhibition fallback data")
        activities = get_permanent_exhibitions(today)

    return activities


def get_permanent_exhibitions(today):
    """提供南山安全教育体验馆常设体验项目兜底数据"""
    exhibitions = [
        {
            'name': '消防安全体验区',
            'venue': NSAQJY_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.szns.gov.cn',
            'contact': '0755-26738119',
            'description': '消防安全隐患排查、灭火器使用模拟、火灾逃生演练等互动体验项目，免费需预约参观。',
            'source': 'nsaqjy',
            'family_friendly': True
        },
        {
            'name': '交通安全体验区',
            'venue': NSAQJY_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.szns.gov.cn',
            'contact': '0755-26738119',
            'description': '交通安全知识学习、模拟驾驶体验、交通事故应急处理等互动项目，免费需预约参观。',
            'source': 'nsaqjy',
            'family_friendly': True
        },
        {
            'name': '居家安全体验区',
            'venue': NSAQJY_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.szns.gov.cn',
            'contact': '0755-26738119',
            'description': '居家用电安全、燃气安全、电梯安全等生活安全知识互动体验，免费需预约参观。',
            'source': 'nsaqjy',
            'family_friendly': True
        },
        {
            'name': '自然灾害体验区',
            'venue': NSAQJY_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.szns.gov.cn',
            'contact': '0755-26738119',
            'description': '地震避险体验、台风模拟、应急救护技能学习等自然灾害应对体验项目，免费需预约参观。',
            'source': 'nsaqjy',
            'family_friendly': True
        },
        {
            'name': '生产安全体验区',
            'venue': NSAQJY_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.szns.gov.cn',
            'contact': '0755-26738119',
            'description': '建筑施工安全、危化品安全、职业健康防护等生产安全知识体验，免费需预约参观。',
            'source': 'nsaqjy',
            'family_friendly': True
        }
    ]
    return exhibitions


def main():
    activities = fetch_nsaqjy_activities()
    print(f"Fetched {len(activities)} activities from {NSAQJY_NAME}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"nsaqjy_{JSON_FILE}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)

    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()
