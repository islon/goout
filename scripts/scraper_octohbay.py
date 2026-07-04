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
from config import OCTOHBAY_URL, OCTOHBAY_NAME, OUTPUT_DIR, JSON_FILE


def fetch_octohbay_activities():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    activities = []
    
    try:
        response = requests.get(OCTOHBAY_URL, headers=headers, timeout=15, verify=False)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        
        news_section = soup.find('div', class_='inNews-section')
        if news_section:
            items = news_section.find_all('div', class_='inNews-section-item')
            for item in items:
                try:
                    date_span = item.find('span')
                    date_str = date_span.get_text().strip() if date_span else ''
                    
                    link = item.find('a', href=True)
                    if not link:
                        continue
                    
                    name = link.get_text().strip()
                    href = link['href']
                    
                    if href.startswith('javascript:'):
                        continue
                    
                    full_url = href if href.startswith('http') else f"{OCTOHBAY_URL}{href}"
                    
                    start_date = ''
                    end_date = ''
                    description = ''
                    
                    date_match = re.search(r'(\d{4})-(\d{1,2})-(\d{1,2})', date_str)
                    if date_match:
                        year, month, day = date_match.groups()
                        start_date = f"{year}-{int(month):02d}-{int(day):02d}"
                        end_date = start_date
                    
                    if not start_date:
                        try:
                            detail_response = requests.get(full_url, headers=headers, timeout=10, verify=False)
                            detail_soup = BeautifulSoup(detail_response.text, 'lxml')
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
                            
                            time.sleep(0.2)
                        except Exception:
                            pass
                    
                    if start_date:
                        activity = {
                            'name': name,
                            'venue': OCTOHBAY_NAME,
                            'start_date': start_date,
                            'end_date': end_date,
                            'url': full_url,
                            'contact': '',
                            'description': description,
                            'source': 'octohbay'
                        }
                        activities.append(activity)
                
                except Exception:
                    continue
        
        information_div = soup.find('div', class_='information')
        if information_div:
            links = information_div.find_all('a', href=True)
            for link in links:
                try:
                    text = link.get_text().strip()
                    href = link['href']
                    
                    if not text or href.startswith('#') or href.startswith('javascript:'):
                        continue
                    
                    full_url = href if href.startswith('http') else f"{OCTOHBAY_URL}{href}"
                    
                    try:
                        detail_response = requests.get(full_url, headers=headers, timeout=10, verify=False)
                        detail_soup = BeautifulSoup(detail_response.text, 'lxml')
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
                                'name': text,
                                'venue': OCTOHBAY_NAME,
                                'start_date': start_date,
                                'end_date': end_date,
                                'url': full_url,
                                'contact': '',
                                'description': description,
                                'source': 'octohbay'
                            }
                            activities.append(activity)
                            
                        time.sleep(0.2)
                    except Exception:
                        pass
                
                except Exception:
                    continue
    
    except Exception as e:
        print(f"Error fetching {OCTOHBAY_NAME}: {e}")
    
    return activities


def main():
    activities = fetch_octohbay_activities()
    print(f"Fetched {len(activities)} activities from {OCTOHBAY_NAME}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"octohbay_{JSON_FILE}")
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)
    
    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()