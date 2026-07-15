import requests
from bs4 import BeautifulSoup
import json
import os
import sys
import re
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import BAOAN_TY_URL, BAOAN_TY_NAME, OUTPUT_DIR, JSON_FILE


def extract_dates(text):
    date_patterns = [
        r'(\d{4})-(\d{1,2})-(\d{1,2})',
        r'(\d{4})/(\d{1,2})/(\d{1,2})',
        r'(\d{4})年(\d{1,2})月(\d{1,2})日',
    ]
    
    dates = []
    for pattern in date_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            year, month, day = match
            dates.append(f"{year}-{int(month):02d}-{int(day):02d}")
    
    dates = sorted(list(set(dates)))
    return dates


def extract_location(text):
    location_keywords = ['体育馆', '体育场', '体育中心', '游泳馆', '训练馆', '综合馆']
    for keyword in location_keywords:
        if keyword in text:
            return f"宝安{keyword}"
    return BAOAN_TY_NAME


def fetch_baoan_ty_activities():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    activities = []
    
    urls_to_try = [
        'http://www.baoan.gov.cn/bawtlyj/',
        'http://www.baoan.gov.cn/bawtlyj/gkmlpt/index',
        'http://www.baoan.gov.cn/xxgk/xwzx/bmdt/',
    ]
    
    for base_url in urls_to_try:
        try:
            response = requests.get(base_url, headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'lxml')
            
            info_links = []
            for link in soup.find_all('a', href=True):
                href = link['href']
                text = link.get_text().strip()
                
                activity_keywords = ['体育', '比赛', '赛事', '演出', '活动', '演唱会', '音乐会']
                if any(kw in text for kw in activity_keywords):
                    if href.startswith('http'):
                        info_links.append(href)
                    elif href.startswith('/'):
                        info_links.append(f"http://www.baoan.gov.cn{href}")
            
            info_links = list(set(info_links))[:20]
            
            for url in info_links:
                try:
                    response = requests.get(url, headers=headers, timeout=10)
                    response.raise_for_status()
                    soup = BeautifulSoup(response.text, 'lxml')
                    
                    title_tag = soup.find('h1') or soup.find('title')
                    name = title_tag.get_text().strip() if title_tag else ''
                    
                    if not name or len(name) < 2:
                        continue
                    
                    text = soup.get_text()
                    
                    dates = extract_dates(text)
                    
                    if len(dates) == 0:
                        continue
                    
                    start_date = dates[0]
                    end_date = dates[-1]
                    
                    venue = extract_location(text)
                    
                    content_divs = soup.find_all(['div', 'article'], class_=re.compile(r'(content|article|detail|text)'))
                    description = ''
                    for div in content_divs:
                        div_text = div.get_text().strip()
                        if len(div_text) > 50:
                            description = div_text[:500]
                            break
                    
                    if not description:
                        paragraphs = soup.find_all('p')
                        combined_text = ' '.join([p.get_text().strip() for p in paragraphs])
                        if len(combined_text) > 50:
                            description = combined_text[:500]
                    
                    description = re.sub(r'\s+', ' ', description).strip()
                    
                    activity = {
                        'name': name,
                        'venue': venue,
                        'start_date': start_date,
                        'end_date': end_date,
                        'url': url,
                        'contact': '',
                        'description': description,
                        'source': 'baoan_ty'
                    }
                    activities.append(activity)
                    
                    time.sleep(0.3)
                    
                except Exception:
                    continue
            
        except Exception:
            continue
    
    return activities


def main():
    activities = fetch_baoan_ty_activities()
    print(f"Fetched {len(activities)} activities from {BAOAN_TY_NAME}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"baoan_ty_{JSON_FILE}")
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)
    
    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()