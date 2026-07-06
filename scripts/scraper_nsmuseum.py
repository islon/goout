import requests
import json
import os
import sys
import re
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, JSON_FILE

NSMUSEUM_URL = "https://www.nanshanmuseum.com"
NSMUSEUM_NAME = "南山博物馆"


def fetch_nsmuseum_activities():
    """从南山博物馆获取展览和活动数据"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    
    activities = []
    
    # 南山博物馆网站是SPA，需要从API获取数据
    # 尝试获取展览列表API
    try:
        # 尝试展览API
        exhibition_api = "https://www.nanshanmuseum.com/api/exhibition/list"
        response = requests.get(exhibition_api, headers=headers, timeout=15)
        
        if response.status_code == 200:
            try:
                data = response.json()
                if data and 'data' in data:
                    for item in data.get('data', []):
                        activity = parse_exhibition_data(item)
                        if activity:
                            activities.append(activity)
            except:
                pass
        
    except Exception as e:
        print(f"API approach failed: {e}")
    
    # 如果API失败，尝试从主页解析
    if len(activities) == 0:
        try:
            # 南山博物馆主页有展览信息
            response = requests.get(NSMUSEUM_URL, headers=headers, timeout=15)
            response.raise_for_status()
            
            activities = parse_homepage(response.text)
            
        except Exception as e:
            print(f"Homepage parsing failed: {e}")
    
    # 尝试获取活动列表
    try:
        activity_api = "https://www.nanshanmuseum.com/api/activity/list"
        response = requests.get(activity_api, headers=headers, timeout=15)
        
        if response.status_code == 200:
            try:
                data = response.json()
                if data and 'data' in data:
                    for item in data.get('data', []):
                        activity = parse_activity_data(item)
                        if activity:
                            activities.append(activity)
            except:
                pass
                
    except Exception as e:
        print(f"Activity API failed: {e}")
    
    return activities


def parse_homepage(html_content):
    """解析主页获取展览信息"""
    activities = []
    
    # 提取展览名称和日期
    # 格式示例: 2026-06-12 / 2026-10-07 沧溟载艺——法国凯布朗利博物馆藏大洋洲艺术珍品展
    exhibition_pattern = r'(\d{4})-(\d{2})-(\d{2})\s*/\s*(\d{4})-(\d{2})-(\d{2})\s*([^\n<]+)'
    matches = re.findall(exhibition_pattern, html_content)
    
    for match in matches:
        try:
            start_date = f"{match[0]}-{match[1]}-{match[2]}"
            end_date = f"{match[3]}-{match[4]}-{match[5]}"
            title = match[6].strip()
            
            if title and len(title) > 5:
                activity = {
                    'name': title,
                    'venue': NSMUSEUM_NAME,
                    'start_date': start_date,
                    'end_date': end_date,
                    'url': NSMUSEUM_URL,
                    'contact': '0755-86700071',
                    'description': f"南山博物馆展览：{title}",
                    'source': 'nsmuseum',
                    'family_friendly': True
                }
                activities.append(activity)
        except:
            continue
    
    # 提取活动信息
    # 格式示例: #活动安排#南山博物馆"建党节"夜间沉浸式剧目活动 2026-07-01
    activity_pattern = r'#活动安排#[^\n]+\n\s*(\d{4})-(\d{2})-(\d{2})'
    activity_matches = re.findall(activity_pattern, html_content)
    
    for match in activity_matches:
        try:
            title_match = re.search(r'#活动安排#([^#\n]+)', html_content)
            if title_match:
                title = title_match.group(1).strip()
                date = f"{match[0]}-{match[1]}-{match[2]}"
                
                activity = {
                    'name': title,
                    'venue': NSMUSEUM_NAME,
                    'start_date': date,
                    'end_date': date,
                    'url': NSMUSEUM_URL,
                    'contact': '0755-86700071',
                    'description': f"南山博物馆活动：{title}",
                    'source': 'nsmuseum',
                    'family_friendly': True
                }
                activities.append(activity)
        except:
            continue
    
    return activities


def parse_exhibition_data(item):
    """解析展览API数据"""
    try:
        title = item.get('title', '') or item.get('name', '')
        if not title:
            return None
        
        start_date = item.get('startDate', '') or item.get('start_date', '')
        end_date = item.get('endDate', '') or item.get('end_date', '')
        
        if not start_date:
            return None
        
        if not end_date:
            end_date = start_date
        
        venue = item.get('venue', '') or item.get('location', '')
        if not venue:
            venue = NSMUSEUM_NAME
        
        description = item.get('description', '') or item.get('intro', '')
        
        url = item.get('url', '') or item.get('link', '')
        if not url:
            url = NSMUSEUM_URL
        
        activity = {
            'name': title,
            'venue': venue,
            'start_date': start_date,
            'end_date': end_date,
            'url': url,
            'contact': '0755-86700071',
            'description': description[:300] if description else '',
            'source': 'nsmuseum',
            'family_friendly': True
        }
        
        return activity
        
    except Exception as e:
        print(f"Error parsing exhibition: {e}")
        return None


def parse_activity_data(item):
    """解析活动API数据"""
    try:
        title = item.get('title', '') or item.get('name', '')
        if not title:
            return None
        
        date = item.get('date', '') or item.get('activityDate', '') or item.get('start_date', '')
        if not date:
            return None
        
        venue = item.get('venue', '') or item.get('location', '')
        if not venue:
            venue = NSMUSEUM_NAME
        
        description = item.get('description', '')
        
        url = item.get('url', '') or NSMUSEUM_URL
        
        activity = {
            'name': title,
            'venue': venue,
            'start_date': date,
            'end_date': date,
            'url': url,
            'contact': '0755-86700071',
            'description': description[:300] if description else '',
            'source': 'nsmuseum',
            'family_friendly': True
        }
        
        return activity
        
    except Exception as e:
        return None


def main():
    activities = fetch_nsmuseum_activities()
    print(f"Fetched {len(activities)} activities from {NSMUSEUM_NAME}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"nsmuseum_{JSON_FILE}")
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)
    
    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()