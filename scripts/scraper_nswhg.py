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
    """从南山区文化馆活动预约系统获取活动数据"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    
    activities = []
    
    # 尝试API接口
    try:
        # 深圳文化馆云平台可能有API
        api_url = "https://whgy.szmassart.com/nsqwhg/web/activity/list"
        
        # 尝试POST请求获取分页数据
        params = {
            'page': 1,
            'size': 50,
            'status': 'all'
        }
        
        response = requests.post(api_url, headers=headers, data=params, timeout=15)
        
        if response.status_code == 200:
            try:
                data = response.json()
                if data and 'data' in data or 'list' in data:
                    items = data.get('data', []) or data.get('list', [])
                    for item in items:
                        activity = parse_activity_item(item)
                        if activity:
                            activities.append(activity)
            except:
                pass
    except Exception as e:
        print(f"API approach failed: {e}")
    
    # 如果API失败，尝试解析HTML页面
    if len(activities) == 0:
        try:
            response = requests.get(NSWHG_URL, headers=headers, timeout=15)
            response.raise_for_status()
            
            activities = parse_activity_list_page(response.text)
            
            # 获取后续页面（如果有）
            for page in range(2, 5):  # 尝试获取前5页
                try:
                    page_url = f"https://whgy.szmassart.com/nsqwhg/web/activity/list.html?page={page}"
                    page_response = requests.get(page_url, headers=headers, timeout=10)
                    page_activities = parse_activity_list_page(page_response.text)
                    
                    # 只添加未来的活动
                    for act in page_activities:
                        if act['start_date'] >= datetime.now().strftime('%Y-%m-%d'):
                            activities.append(act)
                    
                    time.sleep(0.5)
                except:
                    break
            
        except Exception as e:
            print(f"HTML parsing failed: {e}")
    
    return activities


def parse_activity_list_page(html_content):
    """解析活动列表页面"""
    activities = []
    
    # 提取活动信息
    # 页面格式: 名称 地点：xxx 时间：2026-07-29 状态
    
    # 尝试提取活动块
    activity_blocks = re.findall(r'<div[^>]*class="[^"]*activity-item[^"]*"[^>]*>(.*?)</div>', html_content, re.DOTALL)
    
    if not activity_blocks:
        # 尝试其他模式
        activity_blocks = re.findall(r'<li[^>]*>(.*?)</li>', html_content, re.DOTALL)
    
    for block in activity_blocks:
        try:
            # 提取名称
            title_match = re.search(r'>([^<]{5,100})<', block)
            title = title_match.group(1).strip() if title_match else ''
            
            if not title or title in ['首页', '上一页', '下一页', '尾页']:
                continue
            
            # 提取地点
            location_match = re.search(r'地点[：:]\s*([^<\n]+)', block)
            venue = location_match.group(1).strip() if location_match else NSWHG_NAME
            venue = re.sub(r'[^\w\s\u4e00-\u9fff\-()]', '', venue)
            
            # 提取时间
            time_match = re.search(r'时间[：:]\s*(\d{4})-(\d{2})-(\d{2})', block)
            if time_match:
                date = f"{time_match.group(1)}-{time_match.group(2)}-{time_match.group(3)}"
            else:
                time_match = re.search(r'(\d{4})-(\d{2})-(\d{2})', block)
                if time_match:
                    date = f"{time_match.group(1)}-{time_match.group(2)}-{time_match.group(3)}"
                else:
                    continue
            
            # 提取状态（判断是否需要报名）
            status_match = re.search(r'(报名中|进行中|已结束|直接前往)', block)
            status = status_match.group(1) if status_match else ''
            
            description = ''
            if status == '报名中':
                description = '需预约报名'
            elif status == '直接前往':
                description = '可直接前往参与'
            elif status == '已结束':
                continue  # 跳过已结束的活动
            
            activity = {
                'name': title,
                'venue': venue if venue else NSWHG_NAME,
                'start_date': date,
                'end_date': date,
                'url': NSWHG_URL,
                'contact': '',  # 文化馆没有统一电话
                'description': description,
                'source': 'nswhg',
                'family_friendly': True
            }
            
            activities.append(activity)
            
        except Exception as e:
            continue
    
    return activities


def parse_activity_item(item):
    """解析API返回的活动数据"""
    try:
        title = item.get('title', '') or item.get('name', '') or item.get('activityName', '')
        if not title:
            return None
        
        date = item.get('activityDate', '') or item.get('date', '') or item.get('startDate', '')
        if not date:
            return None
        
        venue = item.get('venue', '') or item.get('address', '') or item.get('location', '')
        if not venue:
            venue = NSWHG_NAME
        
        description = item.get('description', '') or item.get('content', '')
        
        url = item.get('url', '') or item.get('link', '')
        if not url:
            url = NSWHG_URL
        
        # 判断是否适合亲子
        family_keywords = ['少儿', '亲子', '儿童', '青少年', '少年', '幼儿']
        family_friendly = any(kw in title for kw in family_keywords) or item.get('familyFriendly', True)
        
        activity = {
            'name': title,
            'venue': venue,
            'start_date': date,
            'end_date': date,
            'url': url,
            'contact': '',
            'description': description[:300] if description else '',
            'source': 'nswhg',
            'family_friendly': family_friendly
        }
        
        return activity
        
    except Exception as e:
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