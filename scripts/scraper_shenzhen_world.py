import requests
from bs4 import BeautifulSoup
import json
import os
import sys
import re
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import SHENZHEN_WORLD_NAME, OUTPUT_DIR, JSON_FILE


def fetch_exhibition_detail(url, headers):
    description = ''
    official_url = ''
    
    if not url or url.startswith('#'):
        return description, official_url
    
    try:
        full_url = url if url.startswith('http') else f"https://www.wuzhanliuhui.com{url}"
        response = requests.get(full_url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'lxml')
        
        content_divs = soup.find_all(['div', 'article'], class_=re.compile(r'(content|article|main|detail|body)'))
        
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
    
    return description, official_url


def fetch_shenzhen_world_exhibitions():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    URLS = [
        "https://www.wuzhanliuhui.com/hall/10005/exh-t-k-p1.htm",
        "https://www.wuzhanliuhui.com/hall/10005/exh-t-k-p2.htm",
    ]
    
    exhibitions = []
    seen_names = set()
    
    for url in URLS:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'lxml')
            
            exh_items = soup.find_all('li', class_='exh-item')
            
            for item in exh_items:
                try:
                    subject_link = item.find('a', class_='subject')
                    if not subject_link:
                        continue
                    
                    name = subject_link.get_text().strip()
                    event_url = subject_link['href'] if 'href' in subject_link.attrs else ''
                    
                    if not name or len(name) < 5:
                        continue
                    
                    if name in seen_names:
                        continue
                    
                    date_p = item.find('p', class_='date')
                    date_text = date_p.get_text().strip() if date_p else ''
                    
                    if not date_text or '取消' in date_text:
                        continue
                    
                    year_match = re.search(r'(\d{4})年', date_text)
                    current_year = int(year_match.group(1)) if year_match else 2025
                    
                    month_match = re.search(r'(\d{1,2})月', date_text)
                    current_month = int(month_match.group(1)) if month_match else 1
                    
                    date_pattern = re.search(r'(\d{1,2})[-~—–](\d{1,2})日', date_text)
                    if date_pattern:
                        start_day = int(date_pattern.group(1))
                        end_day = int(date_pattern.group(2))
                        
                        start_date = f"{current_year}-{current_month:02d}-{start_day:02d}"
                        end_date = f"{current_year}-{current_month:02d}-{end_day:02d}"
                    else:
                        day_match = re.search(r'(\d{1,2})日', date_text)
                        if day_match:
                            day = int(day_match.group(1))
                            start_date = f"{current_year}-{current_month:02d}-{day:02d}"
                            end_date = start_date
                        else:
                            continue
                    
                    description, official_url = fetch_exhibition_detail(event_url, headers)
                    time.sleep(0.3)
                    
                    final_url = official_url if official_url else event_url
                    
                    exhibition = {
                        'name': name,
                        'venue': SHENZHEN_WORLD_NAME,
                        'start_date': start_date,
                        'end_date': end_date,
                        'url': final_url,
                        'contact': '',
                        'description': description,
                        'source': 'shenzhen_world'
                    }
                    exhibitions.append(exhibition)
                    seen_names.add(name)
                    
                except Exception as e:
                    print(f"Error parsing item: {e}")
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