import requests
import json
import os
import sys
import re
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, JSON_FILE

NSLIB_URL = "https://activity.nslib.cn"
NSLIB_NAME = "南山图书馆"


def fetch_nslib_activities():
    """从南山图书馆活动系统获取活动数据"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    
    activities = []
    
    # 获取活动列表页面
    api_url = "https://activity.nslib.cn/activity/moreActive.html"
    
    try:
        response = requests.get(api_url, headers=headers, timeout=15)
        response.raise_for_status()
        html_content = response.text
        
        # 提取活动ID和链接
        activity_pattern = r'/activity/info/(\d+)'
        activity_ids = list(set(re.findall(activity_pattern, html_content)))
        
        print(f"Found {len(activity_ids)} activity IDs from NSLIB")
        
        # 获取每个活动的详情
        for activity_id in activity_ids:
            try:
                detail_url = f"https://activity.nslib.cn/activity/info/{activity_id}"
                detail_response = requests.get(detail_url, headers=headers, timeout=10)
                detail_response.raise_for_status()
                
                activity = parse_activity_detail(detail_response.text, activity_id)
                if activity:
                    activities.append(activity)
                
                time.sleep(0.3)
                
            except Exception as e:
                print(f"Error fetching activity {activity_id}: {e}")
                continue
        
    except Exception as e:
        print(f"Error fetching NSLIB activities: {e}")
    
    return activities


def parse_activity_detail(html_content, activity_id):
    """解析活动详情页面"""
    try:
        # 提取活动名称 (从title标签)
        title_match = re.search(r'<title>([^<]+)</title>', html_content)
        title = title_match.group(1).strip() if title_match else ''
        
        if not title or title in ['南山图书馆', '活动详情']:
            return None
        
        # 提取活动时间 - 格式: 2026年07月10日 14:30 至 2026年07月10日 20:10
        time_pattern = r'活动时间[：:]\s*</span>\s*<span[^>]*>(\d{4})年(\d{2})月(\d{2})日\s*(\d{2}):(\d{2})\s*至\s*(\d{4})年(\d{2})月(\d{2})日\s*(\d{2}):(\d{2})'
        time_match = re.search(time_pattern, html_content)
        
        if time_match:
            start_date = f"{time_match.group(1)}-{time_match.group(2)}-{time_match.group(3)}"
            end_date = f"{time_match.group(6)}-{time_match.group(7)}-{time_match.group(8)}"
        else:
            # 尝试单日活动格式
            time_pattern2 = r'活动时间[：:]\s*</span>\s*<span[^>]*>(\d{4})年(\d{2})月(\d{2})日\s*(\d{2}):(\d{2})'
            time_match2 = re.search(time_pattern2, html_content)
            if time_match2:
                start_date = f"{time_match2.group(1)}-{time_match2.group(2)}-{time_match2.group(3)}"
                end_date = start_date
            else:
                # 尝试更宽松的格式
                time_pattern3 = r'(\d{4})年(\d{1,2})月(\d{1,2})日'
                time_match3 = re.findall(time_pattern3, html_content)
                if time_match3 and len(time_match3) >= 1:
                    start_date = f"{time_match3[0][0]}-{int(time_match3[0][1]):02d}-{int(time_match3[0][2]):02d}"
                    end_date = start_date
                else:
                    return None
        
        # 只保留未来活动
        today = datetime.now().strftime('%Y-%m-%d')
        if end_date < today:
            return None
        
        # 提取地点
        location_pattern = r'地\s*点[：:]\s*</span>\s*<span[^>]*>([^<]+)</span>'
        location_match = re.search(location_pattern, html_content)
        venue = location_match.group(1).strip() if location_match else NSLIB_NAME
        
        # 清理venue
        venue = re.sub(r'[^\w\s\u4e00-\u9fff\-()]', '', venue)
        if not venue or len(venue) < 2:
            venue = NSLIB_NAME
        
        # 提取描述信息 (活动详情内容)
        desc = ""
        # 尝试找活动简介
        intro_pattern = r'活动简介[\s\S]*?<div[^>]*>([\s\S]*?)</div>'
        intro_match = re.search(intro_pattern, html_content)
        if intro_match:
            desc_text = re.sub(r'<[^>]+>', '', intro_match.group(1))
            desc = re.sub(r'\s+', ' ', desc_text).strip()[:300]
        
        # 如果没有简介，尝试其他方式
        if not desc:
            # 找报名须知或活动说明
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
        
        # 构建活动URL
        activity_url = f"https://activity.nslib.cn/activity/info/{activity_id}"
        
        activity = {
            'name': title,
            'venue': f"{NSLIB_NAME} ({venue})" if venue != NSLIB_NAME else NSLIB_NAME,
            'start_date': start_date,
            'end_date': end_date,
            'url': activity_url,
            'contact': '0755-26520380',
            'description': desc,
            'source': 'nslib',
            'family_friendly': True
        }
        
        return activity
        
    except Exception as e:
        print(f"Error parsing activity {activity_id}: {e}")
        return None


def main():
    activities = fetch_nslib_activities()
    print(f"Fetched {len(activities)} activities from {NSLIB_NAME}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"nslib_{JSON_FILE}")
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)
    
    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()