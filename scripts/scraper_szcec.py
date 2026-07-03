import requests
from bs4 import BeautifulSoup
import json
import os
import sys
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import SZCEC_URL, SZCEC_NAME, OUTPUT_DIR, JSON_FILE


def fetch_szcec_exhibitions():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(SZCEC_URL, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'lxml')
        
        exhibitions = []
        current_year = 2025
        
        for element in soup.find_all(['h2', 'tr']):
            if element.name == 'h2':
                text = element.get_text().strip()
                year_match = re.search(r'(\d{4})', text)
                if year_match:
                    current_year = int(year_match.group(1))
                continue
            
            if element.name == 'tr':
                cells = element.find_all('td')
                if len(cells) < 3:
                    continue
                
                name_cell = cells[0]
                name_text = name_cell.get_text().strip()
                
                if not name_text:
                    continue
                
                if re.match(r'^\d+$', name_text):
                    continue
                
                if '年' in name_text and '月' in name_text:
                    year_match = re.search(r'(\d{4})', name_text)
                    if year_match:
                        current_year = int(year_match.group(1))
                    continue
                
                date_str = ''
                contact_info = ''
                url = ''
                
                for cell in cells:
                    text = cell.get_text().strip()
                    if re.search(r'\d{1,2}月\d{1,2}日', text):
                        date_str = text
                    elif '联系方式' in text:
                        continue
                
                if not date_str:
                    continue
                
                link = name_cell.find('a')
                if link and 'href' in link.attrs:
                    url = link['href']
                
                if cells[-1] != name_cell:
                    contact_info = cells[-1].get_text().strip()
                
                date_str = date_str.replace(' ', '').replace('\n', '')
                
                date_match = re.search(r'(\d{1,2})月(\d{1,2})日.*?(\d{1,2})月(\d{1,2})日', date_str)
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
                    date_match = re.search(r'(\d{1,2})月(\d{1,2})日', date_str)
                    if date_match:
                        month = int(date_match.group(1))
                        day = int(date_match.group(2))
                        start_date = f"{current_year}-{month:02d}-{day:02d}"
                        end_date = start_date
                    else:
                        continue
                
                if len(name_text) < 2:
                    continue
                
                exhibition = {
                    'name': name_text,
                    'venue': SZCEC_NAME,
                    'start_date': start_date,
                    'end_date': end_date,
                    'url': url,
                    'contact': contact_info,
                    'source': 'szcec'
                }
                exhibitions.append(exhibition)
        
        return exhibitions
    
    except Exception as e:
        print(f"Error fetching SZCEC data: {e}")
        import traceback
        traceback.print_exc()
        return []


def main():
    exhibitions = fetch_szcec_exhibitions()
    print(f"Fetched {len(exhibitions)} exhibitions from {SZCEC_NAME}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"szcec_{JSON_FILE}")
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(exhibitions, f, ensure_ascii=False, indent=2)
    
    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()