import requests
import json
import os
import sys
import re
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, JSON_FILE

SKHYKPG_URL = "https://www.szns.gov.cn"
SKHYKPG_NAME = "蛇口海洋科普馆"


def fetch_skhykpg_activities():
    """从南山政府在线获取蛇口海洋科普馆活动数据，失败时提供常设展兜底数据"""
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
        # 查找包含"蛇口海洋科普馆"的链接
        link_pattern = r'href=["\']([^"\']*)["\'][^>]*>([^<]*蛇口海洋科普馆[^<]*)</a>'
        links = re.findall(link_pattern, html_content)

        for href, text in links[:10]:
            url = href if href.startswith('http') else f"https://www.szns.gov.cn{href}"
            try:
                detail_resp = requests.get(url, headers=headers, timeout=10)
                detail_resp.raise_for_status()
                detail_text = detail_resp.text

                # 提取标题
                title_match = re.search(r'<title>([^<]+)</title>', detail_text)
                name = title_match.group(1).strip() if title_match else text.strip()
                name = re.sub(r'[-_].*$', '', name).strip()

                # 提取日期
                date_matches = re.findall(r'(\d{4})年(\d{1,2})月(\d{1,2})日', detail_text)
                start_date = ''
                end_date = ''
                if date_matches:
                    start_date = f"{date_matches[0][0]}-{int(date_matches[0][1]):02d}-{int(date_matches[0][2]):02d}"
                    if len(date_matches) > 1:
                        end_date = f"{date_matches[-1][0]}-{int(date_matches[-1][1]):02d}-{int(date_matches[-1][2]):02d}"
                    else:
                        end_date = start_date

                # 提取描述
                desc = ''
                content_match = re.search(r'class="[^"]*content[^"]*"[\s\S]*?>([\s\S]*?)</div>', detail_text)
                if content_match:
                    desc = re.sub(r'<[^>]+>', '', content_match.group(1))
                    desc = re.sub(r'\s+', ' ', desc).strip()[:300]

                if start_date and end_date >= today:
                    activities.append({
                        'name': name,
                        'venue': SKHYKPG_NAME,
                        'start_date': start_date,
                        'end_date': end_date,
                        'url': url,
                        'contact': '0755-26862327',
                        'description': desc if desc else '蛇口海洋科普馆活动公告，免费参观。',
                        'source': 'skhykpg',
                        'family_friendly': True
                    })

                time.sleep(0.3)
            except Exception as e:
                print(f"Error fetching detail page {url}: {e}")
                continue

    except Exception as e:
        print(f"Error fetching SKHYKPG activities from gov site: {e}")

    # 如果没有爬到线上数据，使用常设展兜底
    if not activities:
        print("No online data found, using permanent exhibition fallback data")
        activities = get_permanent_exhibitions(today)

    return activities


def get_permanent_exhibitions(today):
    """提供蛇口海洋科普馆常设展览兜底数据"""
    exhibitions = [
        {
            'name': '海洋贝类标本展',
            'venue': SKHYKPG_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.szns.gov.cn/nsqwhg/',
            'contact': '0755-26862327',
            'description': '展示各类海洋贝类标本，包括腹足纲、双壳纲等珍稀贝类，免费参观。',
            'source': 'skhykpg',
            'family_friendly': True
        },
        {
            'name': '珊瑚标本展',
            'venue': SKHYKPG_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.szns.gov.cn/nsqwhg/',
            'contact': '0755-26862327',
            'description': '展示各类珊瑚标本，包括石珊瑚、软珊瑚等，了解珊瑚礁生态系统，免费参观。',
            'source': 'skhykpg',
            'family_friendly': True
        },
        {
            'name': '砗磲标本展',
            'venue': SKHYKPG_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.szns.gov.cn/nsqwhg/',
            'contact': '0755-26862327',
            'description': '展示大型砗磲标本及海洋生态知识，免费参观。',
            'source': 'skhykpg',
            'family_friendly': True
        },
        {
            'name': '海洋生态保护科普展',
            'venue': SKHYKPG_NAME,
            'start_date': today,
            'end_date': '2027-12-31',
            'url': 'https://www.szns.gov.cn/nsqwhg/',
            'contact': '0755-26862327',
            'description': '介绍深圳海域生态保护成果与海洋环保知识，免费参观。',
            'source': 'skhykpg',
            'family_friendly': True
        }
    ]
    return exhibitions


def main():
    activities = fetch_skhykpg_activities()
    print(f"Fetched {len(activities)} activities from {SKHYKPG_NAME}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"skhykpg_{JSON_FILE}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)

    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()
