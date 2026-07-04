import requests
from bs4 import BeautifulSoup
import json
import os
import sys
import re
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import BAYAREA_EYE_URL, BAYAREA_EYE_NAME, OUTPUT_DIR, JSON_FILE


def fetch_bayarea_eye_activities():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    activities = []
    
    urls_to_try = [
        'http://www.baoan.gov.cn/xxgk/xwzx/bmdt/',
        'http://www.baoan.gov.cn/bawtlyj/gkmlpt/index',
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
                
                if '湾区之眼' in text or '艺术中心' in text or '美术馆' in text:
                    if href.startswith('http'):
                        info_links.append(href)
                    elif href.startswith('/'):
                        info_links.append(f"http://www.baoan.gov.cn{href}")
            
            info_links = list(set(info_links))[:10]
            
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
                    
                    start_date = ''
                    end_date = ''
                    
                    date_patterns = re.findall(r'(\d{4})年(\d{1,2})月(\d{1,2})日.*?(\d{1,2})月(\d{1,2})日', text)
                    if date_patterns:
                        year, start_month, start_day, end_month, end_day = date_patterns[0]
                        start_date = f"{year}-{int(start_month):02d}-{int(start_day):02d}"
                        end_date = f"{year}-{int(end_month):02d}-{int(end_day):02d}"
                    else:
                        date_patterns2 = re.findall(r'(\d{4})年(\d{1,2})月(\d{1,2})日', text)
                        if date_patterns2:
                            year, month, day = date_patterns2[0]
                            start_date = f"{year}-{int(month):02d}-{int(day):02d}"
                            end_date = start_date
                    
                    if not start_date:
                        continue
                    
                    paragraphs = soup.find_all('p')
                    description = ''
                    for p in paragraphs[:5]:
                        p_text = p.get_text().strip()
                        if len(p_text) > 20:
                            description += p_text + '\n'
                    
                    description = description.strip()[:300]
                    
                    activity = {
                        'name': name,
                        'venue': BAYAREA_EYE_NAME,
                        'start_date': start_date,
                        'end_date': end_date,
                        'url': url,
                        'contact': '',
                        'description': description,
                        'source': 'bayarea_eye'
                    }
                    activities.append(activity)
                    
                    time.sleep(0.3)
                    
                except Exception:
                    continue
            
        except Exception:
            continue
    
    return activities


def main():
    activities = fetch_bayarea_eye_activities()
    print(f"Fetched {len(activities)} activities from {BAYAREA_EYE_NAME}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"bayarea_eye_{JSON_FILE}")
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)
    
    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()