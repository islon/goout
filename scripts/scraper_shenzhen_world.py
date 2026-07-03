import requests
from bs4 import BeautifulSoup
import json
import os
import sys
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import SHENZHEN_WORLD_NAME, OUTPUT_DIR, JSON_FILE


URLS = [
    "https://www.wuzhanliuhui.com/hall/10005/exh-t-k-p1.htm",
    "https://www.wuzhanliuhui.com/hall/10005/exh-t-k-p2.htm",
]


def fetch_shenzhen_world_exhibitions():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    exhibitions = []
    seen_names = set()
    
    for url in URLS:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'lxml')
            
            items = soup.find_all('a', href=re.compile(r'/exh/\d+\.htm'))
            
            for item in items:
                try:
                    name = item.get_text().strip()
                    
                    if not name or len(name) < 5:
                        continue
                    
                    if name in seen_names:
                        continue
                    
                    parent_div = item.find_parent('div')
                    date_text = ''
                    
                    if parent_div:
                        date_span = parent_div.find('span', string=re.compile(r'\d{4}年'))
                        if date_span:
                            date_text = date_span.get_text().strip()
                    
                    if not date_text:
                        siblings = item.find_next_siblings()
                        for sibling in siblings:
                            text = sibling.get_text().strip()
                            if re.search(r'\d{4}年', text):
                                date_text = text
                                break
                    
                    if not date_text or '取消' in date_text:
                        continue
                    
                    year_match = re.search(r'(\d{4})年', date_text)
                    current_year = int(year_match.group(1)) if year_match else 2025
                    
                    date_match = re.search(r'(\d{1,2})月(\d{1,2})日.*?(\d{1,2})月(\d{1,2})日', date_text)
                    if date_match:
                        start_month = int(date_match.group(1))
                        start_day = int(date_match.group(2))
                        end_month = int(date_match.group(3))
                        end_day = int(date_match.group(4))
                        
                        start_date = f"{current_year}-{start_month:02d}-{start_day:02d}"
                        
                        end_year = current_year
                        if end_month < start_month:
                            end_year = current_year + 1
                        end_date = f"{end_year}-{end_month:02d}-{end_day:02d}"
                    else:
                        continue
                    
                    event_url = item['href'] if 'href' in item.attrs else ''
                    
                    exhibition = {
                        'name': name,
                        'venue': SHENZHEN_WORLD_NAME,
                        'start_date': start_date,
                        'end_date': end_date,
                        'url': event_url,
                        'contact': '',
                        'source': 'shenzhen_world'
                    }
                    exhibitions.append(exhibition)
                    seen_names.add(name)
                    
                except Exception as e:
                    continue
        
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            continue
    
    return exhibitions


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