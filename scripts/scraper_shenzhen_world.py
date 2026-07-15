import requests
import json
import os
import sys
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import SHENZHEN_WORLD_URL, SHENZHEN_WORLD_NAME, OUTPUT_DIR, JSON_FILE


def fetch_shenzhen_world_exhibitions():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Referer': 'https://www.shenzhen-world.com/scheduling/index.html'
    }
    proxies = {'http': 'http://127.0.0.1:18080', 'https': 'http://127.0.0.1:18080'}
    
    api_url = 'https://www.shenzhen-world.com/api/shows/v1/findByPage'
    
    try:
        payload = {
            "bean": {"languageType": 1},
            "sorts": {"startAt": "desc", "orderNumber": "desc"},
            "pageSize": 512,
            "page": 1
        }
        
        response = requests.post(api_url, headers=headers, json=payload,
                                 timeout=30, verify=False, proxies=proxies)
        response.raise_for_status()
        data = response.json()
        
        if data.get('code') != 1:
            print(f"API error: {data.get('msg')}")
            return []
        
        result = data.get('result', {})
        items = result.get('list', [])
        print(f"API returned {len(items)} items (total: {result.get('total')})")
        
        exhibitions = []
        for item in items:
            title = item.get('title', '').strip()
            if not title:
                continue
            
            start_at = item.get('startAt', '')
            end_at = item.get('endAt', '')
            
            # 解析日期 "2026-12-02 00:00:00"
            start_date = start_at.split(' ')[0] if start_at else ''
            end_date = end_at.split(' ')[0] if end_at else ''
            
            if not start_date:
                continue
            
            # 跳过已过期（2025年以前的）
            if start_date < '2026-01-01':
                continue
            
            site = item.get('site', '')
            organizer = item.get('organizer', '')
            contact = item.get('contact', '')
            thumb = item.get('thumb', '')
            
            description = f'{title}，{start_date}至{end_date}，深圳国际会展中心。'
            if organizer:
                description += f'主办方：{organizer}。'
            if contact:
                description += f'联系方式：{contact}。'
            
            exhibition = {
                'name': title,
                'title': title,
                'venue': SHENZHEN_WORLD_NAME,
                'start_date': start_date,
                'end_date': end_date,
                'link': site if site.startswith('http') else f'https://www.shenzhen-world.com',
                'contact': contact,
                'description': description,
                'category': '展览',
                'fee': '免费',
                'family_friendly': False,
                'source': 'shenzhen_world'
            }
            exhibitions.append(exhibition)
        
        return exhibitions
    
    except Exception as e:
        print(f"Error fetching Shenzhen World data: {e}")
        import traceback
        traceback.print_exc()
        return []


def main():
    exhibitions = fetch_shenzhen_world_exhibitions()
    print(f"Fetched {len(exhibitions)} exhibitions from {SHENZHEN_WORLD_NAME}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"shenzhen_world_{JSON_FILE}")
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(exhibitions, f, ensure_ascii=False, indent=2)
    
    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()