import requests
from bs4 import BeautifulSoup
import json
import os
import sys
import re
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import BALIB_URL, BALIB_NAME, OUTPUT_DIR, JSON_FILE


def fetch_activity_detail(url, headers):
    description = ''
    full_dates = None
    
    if not url or url.startswith('#'):
        return description, full_dates
    
    try:
        full_url = url if url.startswith('http') else f"https://www.balib.cn{url}"
        response = requests.get(full_url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        
        text = soup.get_text()
        
        date_patterns = re.findall(r'(\d{4})年(\d{1,2})月(\d{1,2})日.*?(\d{1,2})月(\d{1,2})日', text)
        if date_patterns:
            year, start_month, start_day, end_month, end_day = date_patterns[0]
            start_date = f"{year}-{int(start_month):02d}-{int(start_day):02d}"
            end_date = f"{year}-{int(end_month):02d}-{int(end_day):02d}"
            if start_date <= end_date:
                full_dates = (start_date, end_date)
        
        if not full_dates:
            date_patterns2 = re.findall(r'(\d{4})年(\d{1,2})月(\d{1,2})日', text)
            if len(date_patterns2) >= 2:
                year1, month1, day1 = date_patterns2[0]
                year2, month2, day2 = date_patterns2[1]
                start_date = f"{year1}-{int(month1):02d}-{int(day1):02d}"
                end_date = f"{year2}-{int(month2):02d}-{int(day2):02d}"
                if start_date <= end_date:
                    full_dates = (start_date, end_date)
        
        if not full_dates:
            date_patterns3 = re.findall(r'(\d{4})-(\d{1,2})-(\d{1,2})', text)
            if len(date_patterns3) >= 2:
                year1, month1, day1 = date_patterns3[0]
                year2, month2, day2 = date_patterns3[1]
                start_date = f"{year1}-{int(month1):02d}-{int(day1):02d}"
                end_date = f"{year2}-{int(month2):02d}-{int(day2):02d}"
                if start_date <= end_date:
                    full_dates = (start_date, end_date)
        
        content_divs = soup.find_all(['div', 'article'], class_=re.compile(r'(content|article|main|detail|body|info)'))
        
        for div in content_divs:
            text = div.get_text().strip()
            if len(text) > 50:
                description = text[:500]
                break
        
        if not description:
            paragraphs = soup.find_all('p')
            combined_text = ' '.join([p.get_text().strip() for p in paragraphs])
            if len(combined_text) > 50:
                description = combined_text[:500]
        
        description = re.sub(r'\s+', ' ', description).strip()
        
    except Exception:
        pass
    
    return description, full_dates


def fetch_balib_activities():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    activities = []
    
    category_urls = [
        'https://www.balib.cn/category/132',
        'https://www.balib.cn/category/13',
        'https://www.balib.cn/category/270',
    ]
    
    for category_url in category_urls:
        try:
            response = requests.get(category_url, headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'lxml')
            
            content_box = soup.find('div', class_='content-box')
            if not content_box:
                continue
            
            items = content_box.find_all('div', class_='item')
            
            for item in items:
                try:
                    links = item.find_all('a', href=True)
                    href = ''
                    name = ''
                    
                    for link in links:
                        if link['href'].startswith('/information/'):
                            href = link['href']
                            text = link.get_text().strip()
                            if text and len(text) > 1:
                                name = text
                    
                    if not href or not name:
                        continue
                    
                    pub = item.find('div', class_='pub')
                    date_str = ''
                    if pub:
                        date_str = pub.get_text().strip()
                    
                    start_date = ''
                    end_date = ''
                    
                    date_match = re.search(r'(\d{4})年(\d{1,2})月(\d{1,2})日', date_str)
                    if date_match:
                        year, month, day = date_match.groups()
                        start_date = f"{year}-{int(month):02d}-{int(day):02d}"
                        end_date = start_date
                    else:
                        full_url = f"https://www.balib.cn{href}"
                        response_detail = requests.get(full_url, headers=headers, timeout=10)
                        response_detail.raise_for_status()
                        soup_detail = BeautifulSoup(response_detail.text, 'lxml')
                        text = soup_detail.get_text()
                        date_match = re.search(r'(\d{4})年(\d{1,2})月(\d{1,2})日', text)
                        if date_match:
                            year, month, day = date_match.groups()
                            start_date = f"{year}-{int(month):02d}-{int(day):02d}"
                            end_date = start_date
                    
                    if not start_date:
                        continue
                    
                    description, full_dates = fetch_activity_detail(href, headers)
                    if full_dates:
                        start_date, end_date = full_dates
                    
                    activity = {
                        'name': name,
                        'venue': BALIB_NAME,
                        'start_date': start_date,
                        'end_date': end_date,
                        'url': f"https://www.balib.cn{href}",
                        'contact': '',
                        'description': description,
                        'source': 'balib'
                    }
                    activities.append(activity)
                    
                    time.sleep(0.2)
                    
                except Exception as e:
                    continue
            
        except Exception as e:
            continue
    
    return activities


def main():
    activities = fetch_balib_activities()
    print(f"Fetched {len(activities)} activities from {BALIB_NAME}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"balib_{JSON_FILE}")
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)
    
    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()