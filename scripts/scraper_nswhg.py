import requests
import json
import os
import sys
import re
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, JSON_FILE

NSWHG_URL = "https://whgy.szmassart.com/nsqwhg/web/activity/list.html"
NSWHG_NAME = "南山区文化馆"


def fetch_nswhg_activities():
    """从深圳文化馆云平台获取南山区活动数据"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://whgy.szmassart.com',
        'Referer': 'https://whgy.szmassart.com/nsqwhg/web/activity/list.html',
    }
    
    activities = []
    seen_ids = set()
    page = 1
    max_pages = 50
    
    while page <= max_pages:
        try:
            # 文化馆云平台API
            api_url = "https://whgy.szmassart.com/nsqwhg/web/activity/list"
            
            params = {
                'page': page,
                'size': 50,
            }
            
            response = requests.post(api_url, headers=headers, data=params, timeout=15)
            response.raise_for_status()
            
            data = response.json()
            
            # 数据结构: {"err": 0, "data": {"data": [...], "pageTotal": x}}
            wrapper = data.get('data', {})
            if not wrapper or not isinstance(wrapper, dict):
                break
            
            items = wrapper.get('data', [])
            if not items:
                break
            
            for item in items:
                # 去重
                activity_id = item.get('activityId', '')
                if activity_id in seen_ids:
                    continue
                seen_ids.add(activity_id)
                
                # 只保留南山区的活动
                activity_area = item.get('activityArea', '')
                if '南山区' not in activity_area:
                    continue
                
                # 跳过已结束的活动
                end_date = item.get('activityEndTime', '')
                today = datetime.now().strftime('%Y-%m-%d')
                if end_date and end_date < today:
                    continue
                
                activity = parse_activity_item(item)
                if activity:
                    activities.append(activity)
            
            page_total = wrapper.get('pageTotal', 1)
            if page >= page_total:
                break
            
            page += 1
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Error fetching page {page}: {e}")
            break
    
    return activities


def parse_activity_item(item):
    """解析API返回的活动数据"""
    try:
        title = item.get('activityName', '')
        if not title:
            return None
        
        # 清理HTML实体
        title = title.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
        
        start_date = item.get('activityStartTime', '')
        end_date = item.get('activityEndTime', '')
        
        if not start_date:
            return None
        
        if not end_date:
            end_date = start_date
        
        # 场馆信息
        venue_name = item.get('venueName', '')
        location_name = item.get('activityLocationName', '')
        
        venue = venue_name or location_name or NSWHG_NAME
        
        # 描述信息
        description = item.get('activityProfile', '')
        if not description:
            description = item.get('tagName', '')
        
        # 判断是否免费
        is_free = item.get('activityIsFree', 0)
        price = item.get('activityPrice', '')
        
        # 报名方式
        reservation = item.get('activityIsReservation', 0)
        subject = item.get('activitySubject', '')
        
        desc_parts = []
        if is_free == 1:
            desc_parts.append("免费")
        elif price and price != '0':
            desc_parts.append(f"费用：{price}元")
        
        if subject:
            desc_parts.append(subject)
        
        if reservation == 2:
            desc_parts.append("需预约报名")
        elif reservation == 1:
            desc_parts.append("可直接前往")
        
        if description:
            desc_parts.append(description)
        
        final_desc = '。'.join([p for p in desc_parts if p]) if desc_parts else ''
        
        # URL
        url = f"https://whgy.szmassart.com/nsqwhg/web/activity/detail.html?activityId={item.get('activityId', '')}"
        
        # 判断是否适合亲子
        family_keywords = ['少儿', '亲子', '儿童', '青少年', '少年', '幼儿', '家庭']
        family_friendly = any(kw in title for kw in family_keywords)
        
        activity = {
            'name': title,
            'venue': venue,
            'start_date': start_date,
            'end_date': end_date,
            'url': url,
            'contact': '',
            'description': final_desc[:300] if final_desc else '',
            'source': 'nswhg',
            'family_friendly': family_friendly
        }
        
        return activity
        
    except Exception as e:
        print(f"Error parsing activity: {e}")
        return None


def main():
    activities = fetch_nswhg_activities()
    print(f"Fetched {len(activities)} activities from {NSWHG_NAME}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"nswhg_{JSON_FILE}")
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)
    
    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()
