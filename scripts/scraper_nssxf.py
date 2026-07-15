import requests
import json
import os
import sys
import re
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, JSON_FILE

NSSXF_URL = "https://activity.nslib.cn"
NSSXF_NAME = "南山书房"


def fetch_nssxf_activities():
    """从南山图书馆活动系统获取南山书房相关活动数据"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    activities = []
    today = datetime.now().strftime('%Y-%m-%d')

    # 从南山图书馆活动系统获取活动列表
    try:
        api_url = "https://activity.nslib.cn/activity/moreActive.html"

        response = requests.get(api_url, headers=headers, timeout=15)
        response.raise_for_status()
        html_content = response.text

        # 提取活动ID和链接
        activity_pattern = r'/activity/info/(\d+)'
        activity_ids = list(set(re.findall(activity_pattern, html_content)))

        print(f"Found {len(activity_ids)} activity IDs from NSLIB system")

        # 获取每个活动的详情，筛选南山书房相关
        for activity_id in activity_ids:
            try:
                detail_url = f"https://activity.nslib.cn/activity/info/{activity_id}"
                detail_response = requests.get(detail_url, headers=headers, timeout=10)
                detail_response.raise_for_status()

                activity = parse_activity_detail(detail_response.text, activity_id, today)
                if activity:
                    activities.append(activity)

                time.sleep(0.3)

            except Exception as e:
                print(f"Error fetching activity {activity_id}: {e}")
                continue

    except Exception as e:
        print(f"Error fetching NSSXF activities from NSLIB system: {e}")

    return activities


def parse_activity_detail(html_content, activity_id, today):
    """解析活动详情页面，筛选南山书房相关活动"""
    try:
        # 提取活动名称
        title_match = re.search(r'<title>([^<]+)</title>', html_content)
        title = title_match.group(1).strip() if title_match else ''

        if not title or title in ['南山图书馆', '活动详情']:
            return None

        # 提取活动时间
        time_pattern = r'活动时间[：:]\s*</span>\s*<span[^>]*>(\d{4})年(\d{2})月(\d{2})日\s*(\d{2}):(\d{2})\s*至\s*(\d{4})年(\d{2})月(\d{2})日\s*(\d{2}):(\d{2})'
        time_match = re.search(time_pattern, html_content)

        if time_match:
            start_date = f"{time_match.group(1)}-{time_match.group(2)}-{time_match.group(3)}"
            end_date = f"{time_match.group(6)}-{time_match.group(7)}-{time_match.group(8)}"
        else:
            time_pattern2 = r'活动时间[：:]\s*</span>\s*<span[^>]*>(\d{4})年(\d{2})月(\d{2})日\s*(\d{2}):(\d{2})'
            time_match2 = re.search(time_pattern2, html_content)
            if time_match2:
                start_date = f"{time_match2.group(1)}-{time_match2.group(2)}-{time_match2.group(3)}"
                end_date = start_date
            else:
                time_pattern3 = r'(\d{4})年(\d{1,2})月(\d{1,2})日'
                time_match3 = re.findall(time_pattern3, html_content)
                if time_match3 and len(time_match3) >= 1:
                    start_date = f"{time_match3[0][0]}-{int(time_match3[0][1]):02d}-{int(time_match3[0][2]):02d}"
                    end_date = start_date
                else:
                    return None

        # 只保留未来活动
        if end_date < today:
            return None

        # 提取地点
        location_pattern = r'地\s*点[：:]\s*</span>\s*<span[^>]*>([^<]+)</span>'
        location_match = re.search(location_pattern, html_content)
        venue = location_match.group(1).strip() if location_match else ''

        # 清理venue
        venue = re.sub(r'[^\w\s\u4e00-\u9fff\-()]', '', venue)

        # 筛选南山书房相关活动 - 通过地点或标题判断
        study_keywords = ['南山书房', '书房']
        is_study_activity = any(kw in venue for kw in study_keywords) or any(kw in title for kw in study_keywords)

        if not is_study_activity:
            return None

        if not venue or len(venue) < 2:
            venue = NSSXF_NAME

        # 提取描述信息
        desc = ""
        intro_pattern = r'活动简介[\s\S]*?<div[^>]*>([\s\S]*?)</div>'
        intro_match = re.search(intro_pattern, html_content)
        if intro_match:
            desc_text = re.sub(r'<[^>]+>', '', intro_match.group(1))
            desc = re.sub(r'\s+', ' ', desc_text).strip()[:300]

        if not desc:
            content_pattern = r'class="[^"]*volCon[^"]*"[\s\S]*?<span[^>]*>([\s\S]*?)</span>'
            content_matches = re.findall(content_pattern, html_content)
            if content_matches:
                for cm in content_matches:
                    clean = re.sub(r'<[^>]+>', '', cm).strip()
                    if len(clean) > 10 and len(clean) < 500:
                        desc = clean[:300]
                        break

        # 判断是否需报名
        if '我要报名' in html_content or '剩余名额' in html_content:
            if not desc:
                desc = "需预约报名"
            else:
                desc = "需预约报名。" + desc
        elif '直接前往' in html_content:
            if not desc:
                desc = "可直接前往参与"

        activity_url = f"https://activity.nslib.cn/activity/info/{activity_id}"

        activity = {
            'name': title,
            'venue': f"{NSSXF_NAME} ({venue})" if venue != NSSXF_NAME else NSSXF_NAME,
            'start_date': start_date,
            'end_date': end_date,
            'url': activity_url,
            'contact': '',
            'description': desc,
            'source': 'nssxf',
            'family_friendly': True
        }

        return activity

    except Exception as e:
        print(f"Error parsing activity {activity_id}: {e}")
        return None


def main():
    activities = fetch_nssxf_activities()
    print(f"Fetched {len(activities)} activities from {NSSXF_NAME}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"nssxf_{JSON_FILE}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)

    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()
