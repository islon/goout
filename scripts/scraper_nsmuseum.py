import requests
import json
import os
import sys
import re
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, JSON_FILE

NSMUSEUM_URL = "https://www.nanshanmuseum.com"
NSMUSEUM_NAME = "南山博物馆"


def fetch_nsmuseum_activities():
    """从南山博物馆获取展览和活动数据"""
    
    activities = []
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 根据公开信息整理当前展览
    exhibitions = [
        {
            'name': '沧溟载艺——法国凯布朗利博物馆藏大洋洲艺术珍品展',
            'venue': '南山博物馆一层一号专题展厅',
            'start_date': '2026-06-12',
            'end_date': '2026-10-07',
            'url': 'https://www.szns.gov.cn/ztzl/hdrl/content/post_12872774.html',
            'description': '精选法国国家凯布朗利博物馆馆藏大洋洲艺术珍品171件/套。展期至10月7日，免费免预约。定点讲解：每个开馆日10:50。',
            'family_friendly': True
        },
        {
            'name': '贞观长歌——大唐历史文化主题展',
            'venue': '南山博物馆二层二号展厅',
            'start_date': '2026-02-13',
            'end_date': '2026-10-31',
            'url': 'https://www.nanshanmuseum.com',
            'description': '大唐历史文化主题展览，展现盛唐风貌。',
            'family_friendly': True
        },
        {
            'name': '珍瓷萃美——中国古代瓷器艺术特展',
            'venue': '南山博物馆二层三号展厅',
            'start_date': '2026-02-07',
            'end_date': '2026-08-31',
            'url': 'https://www.nanshanmuseum.com',
            'description': '中国古代瓷器艺术精品展览。',
            'family_friendly': True
        },
        {
            'name': '壁上万千——山西宋金壁画中的众生气象',
            'venue': '南山博物馆一层一号展厅',
            'start_date': '2025-12-30',
            'end_date': '2026-09-30',
            'url': 'https://www.nanshanmuseum.com',
            'description': '山西宋金壁画艺术展览，展现古代壁画中的众生百态。',
            'family_friendly': True
        }
    ]
    
    for ex in exhibitions:
        # 只保留未结束的展览
        if ex['end_date'] >= today:
            activity = {
                'name': ex['name'],
                'venue': ex['venue'],
                'start_date': ex['start_date'],
                'end_date': ex['end_date'],
                'url': ex['url'],
                'contact': '0755-86700071',
                'description': ex['description'],
                'source': 'nsmuseum',
                'family_friendly': ex['family_friendly']
            }
            activities.append(activity)
    
    # 暑期夜间开放活动
    if today <= '2026-08-31':
        night_activity = {
            'name': '南山博物馆暑期夜间延时开放',
            'venue': '南山博物馆',
            'start_date': today,
            'end_date': '2026-08-31',
            'url': 'https://www.nanshanmuseum.com',
            'contact': '0755-86700071',
            'description': '2026年7月4日至8月31日，新增周五、周日夜间延时开放（周六常规夜间开放保持不变）。周二至周日10:00-18:00（17:30停止入场），周六夜间开放时间：18:00-21:00（20:30停止入场）。免费免预约。',
            'source': 'nsmuseum',
            'family_friendly': True
        }
        activities.append(night_activity)
    
    return activities


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
