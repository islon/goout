import requests
from bs4 import BeautifulSoup
import json
import os
import sys
import re
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import SZCEC_URL, SZCEC_NAME, OUTPUT_DIR, JSON_FILE


def fetch_exhibition_detail(url, headers):
    description = ''
    full_dates = None
    
    if not url or url.startswith('#'):
        return description, full_dates
    
    try:
        full_url = url if url.startswith('http') else f"https://www.szcec.com{url}"
        response = requests.get(full_url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'lxml')
        
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
    
    return description, full_dates


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
        current_month = 1
        
        table = soup.find('table')
        if not table:
            print("No table found")
            return []
        
        rows = table.find_all('tr')
        
        for row in rows:
            cells = row.find_all('td')
            if len(cells) < 4:
                continue
            
            seq_cell = cells[0].get_text().strip()
            name_cell = cells[1]
            date_cell = cells[2]
            contact_cell = cells[3]
            
            name_text = name_cell.get_text().strip()
            
            if not name_text:
                continue
            
            if re.match(r'^\d+$', seq_cell):
                pass
            elif name_text and '年' in name_text and '月' in name_text:
                year_match = re.search(r'(\d{4})', name_text)
                month_match = re.search(r'(\d{1,2})月', name_text)
                if year_match:
                    current_year = int(year_match.group(1))
                if month_match:
                    current_month = int(month_match.group(1))
                continue
            
            date_str = date_cell.get_text().strip()
            date_str = date_str.replace('\n', '').strip()
            
            if not date_str:
                continue
            
            month_match = re.search(r'(\d{1,2})月', date_str)
            if month_match:
                current_month = int(month_match.group(1))
            
            day_match = re.search(r'(\d{1,2})日', date_str)
            if not day_match:
                continue
            
            start_day = int(day_match.group(1))
            start_date = f"{current_year}-{current_month:02d}-{start_day:02d}"
            end_date = start_date
            
            url = ''
            link = name_cell.find('a')
            if link and 'href' in link.attrs:
                url = link['href']
            
            contact_info = contact_cell.get_text().strip()
            contact_info = re.sub(r'\s+', ' ', contact_info)
            
            if len(name_text) < 2:
                continue
            
            description, full_dates = fetch_exhibition_detail(url, headers)
            time.sleep(0.3)
            
            if full_dates:
                start_date, end_date = full_dates
            
            exhibition = {
                'name': name_text,
                'venue': SZCEC_NAME,
                'start_date': start_date,
                'end_date': end_date,
                'url': url,
                'contact': contact_info,
                'description': description,
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