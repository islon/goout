import requests
from bs4 import BeautifulSoup
import json
import os
import sys
import re
import time
import warnings
warnings.filterwarnings('ignore', category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import BAYEYE_NAME, OUTPUT_DIR, JSON_FILE


def fetch_bayeye_activities():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    activities = []
    
    news_urls = [
        'https://www.baoan.gov.cn/xxgk/xwzx/tpxw/',
        'https://www.sznews.com/news/content/mb/',
    ]
    
    for news_url in news_urls:
        try:
            response = requests.get(news_url, headers=headers, timeout=15, verify=False)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'lxml')
            
            links = soup.find_all('a', href=True)
            for link in links:
                text = link.get_text().strip()
                href = link['href']
                
                if not text or not ('湾区之眼' in text or '湾区之眼' in href):
                    continue
                
                if not href.startswith('http'):
                    if href.startswith('/'):
                        href = f"https://www.baoan.gov.cn{href}"
                    else:
                        continue
                
                try:
                    detail_response = requests.get(href, headers=headers, timeout=10, verify=False)
                    detail_soup = BeautifulSoup(detail_response.text, 'lxml')
                    
                    article_title = detail_soup.find('h1')
                    name = article_title.get_text().strip() if article_title else text
                    
                    text = detail_soup.get_text()
                    
                    date_patterns = re.findall(r'(\d{4})年(\d{1,2})月(\d{1,2})日', text)
                    if date_patterns:
                        year, month, day = date_patterns[0]
                        start_date = f"{year}-{int(month):02d}-{int(day):02d}"
                        end_date = start_date
                        
                        if len(date_patterns) >= 2:
                            year2, month2, day2 = date_patterns[1]
                            end_date = f"{year2}-{int(month2):02d}-{int(day2):02d}"
                        
                        paragraphs = detail_soup.find_all('p')
                        combined_text = ' '.join([p.get_text().strip() for p in paragraphs])
                        if len(combined_text) > 50:
                            description = combined_text[:500]
                            description = re.sub(r'\s+', ' ', description).strip()
                        
                        activity = {
                            'name': name,
                            'venue': BAYEYE_NAME,
                            'start_date': start_date,
                            'end_date': end_date,
                            'url': href,
                            'contact': '',
                            'description': description,
                            'source': 'bayeye'
                        }
                        activities.append(activity)
                    
                    time.sleep(0.3)
                except Exception:
                    continue
            
        except Exception as e:
            continue
    
    return activities


def main():
    activities = fetch_bayeye_activities()
    print(f"Fetched {len(activities)} activities from {BAYEYE_NAME}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"bayeye_{JSON_FILE}")
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)
    
    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()