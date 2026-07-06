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
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    
    activities = []
    
    # 尝试通过API获取数据
    # 南山图书馆活动系统可能使用类似深圳图书馆的API结构
    api_url = "https://activity.nslib.cn/activity/moreActive.html"
    
    try:
        response = requests.get(api_url, headers=headers, timeout=15)
        response.raise_for_status()
        
        # 解析HTML页面获取活动链接
        html_content = response.text
        
        # 提取活动ID和链接
        activity_pattern = r'/activity/info/(\d+)'
        activity_ids = re.findall(activity_pattern, html_content)
        
        print(f"Found {len(activity_ids)} activity IDs from NSLIB")
        
        # 获取每个活动的详情
        for activity_id in activity_ids[:100]:  # 限制数量避免请求过多
            try:
                detail_url = f"https://activity.nslib.cn/activity/info/{activity_id}"
                detail_response = requests.get(detail_url, headers=headers, timeout=10)
                detail_response.raise_for_status()
                
                # 解析活动详情
                activity = parse_activity_detail(detail_response.text, activity_id)
                if activity:
                    activities.append(activity)
                
                time.sleep(0.5)
                
            except Exception as e:
                print(f"Error fetching activity {activity_id}: {e}")
                continue
        
    except Exception as e:
        print(f"Error fetching NSLIB activities: {e}")
    
    return activities


def parse_activity_detail(html_content, activity_id):
    """解析活动详情页面"""
    try:
        # 提取活动名称
        title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', html_content)
        if not title_match:
            title_match = re.search(r'<div[^>]*class="[^"]*title[^"]*"[^>]*>([^<]+)</div>', html_content)
        title = title_match.group(1).strip() if title_match else ''
        
        if not title:
            return None
        
        # 提取活动时间
        time_match = re.search(r'活动时间[：:]\s*(\d{4})年(\d{1,2})月(\d{1,2})日[^\d]*(\d{1,2}):(\d{2})', html_content)
        if time_match:
            y, m, d, h, min = time_match.groups()
            start_date = f"{y}-{int(m):02d}-{int(d):02d}"
        else:
            # 尝试其他时间格式
            time_match = re.search(r'(\d{4})[年/-](\d{1,2})[月/-](\d{1,2})', html_content)
            if time_match:
                y, m, d = time_match.groups()
                start_date = f"{y}-{int(m):02d}-{int(d):02d}"
            else:
                return None
        
        end_date = start_date  # 单日活动
        
        # 提取地点
        location_match = re.search(r'地\s*点[：:]\s*([^<\n]+)', html_content)
        venue = location_match.group(1).strip() if location_match else NSLIB_NAME
        
        # 清理venue中的特殊字符
        venue = re.sub(r'[^\w\s\u4e00-\u9fff\-()]', '', venue)
        if not venue or len(venue) < 2:
            venue = NSLIB_NAME
        
        # 提取描述信息
        desc_match = re.search(r'<div[^>]*class="[^"]*content[^"]*"[^>]*>(.*?)</div>', html_content, re.DOTALL)
        description = ''
        if desc_match:
            desc_text = desc_match.group(1)
            # 清理HTML标签
            desc_text = re.sub(r'<[^>]+>', '', desc_text)
            desc_text = re.sub(r'\s+', ' ', desc_text).strip()
            description = desc_text[:300] if len(desc_text) > 300 else desc_text
        
        # 提取剩余名额判断是否需要报名
        signup_match = re.search(r'剩余名额[：:]\s*(\d+)/(\d+)', html_content)
        needs_signup = signup_match is not None
        
        if needs_signup and not description:
            description = "需预约报名"
        
        # 构建活动URL
        activity_url = f"https://activity.nslib.cn/activity/info/{activity_id}"
        
        activity = {
            'name': title,
            'venue': f"{NSLIB_NAME} ({venue})" if venue != NSLIB_NAME else NSLIB_NAME,
            'start_date': start_date,
            'end_date': end_date,
            'url': activity_url,
            'contact': '0755-26520380',
            'description': description,
            'source': 'nslib',
            'family_friendly': True  # 图书馆活动一般适合亲子
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