import requests
import json
import os
import sys
import re
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import SZLIB_URL, SZLIB_NAME, OUTPUT_DIR, JSON_FILE


def fetch_szlib_activities():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    activities = []
    
    calendar_url = 'https://www.szlib.org.cn/m/activity/getLectureCalendars.jsp?customizedUrl=salon&library=044005'
    lectures_url = 'https://www.szlib.org.cn/m/activity/getLectures.jsp?customizedUrl=salon&library=044005'
    
    months_to_check = [
        (2026, 7),
        (2026, 8),
        (2026, 9),
        (2026, 10),
        (2026, 11),
        (2026, 12),
        (2027, 1),
        (2027, 2),
    ]
    
    for year, month in months_to_check:
        try:
            calendar_data = {'year': year, 'month': month, 'math': 99999}
            response = requests.post(calendar_url, headers=headers, data=calendar_data, timeout=10)
            response.raise_for_status()
            calendar_result = response.json()
            
            if calendar_result.get('data', {}).get('result') != 'success':
                continue
            
            records = calendar_result['data'].get('record', [])
            
            for record in records:
                day = record.get('day', 0)
                count = int(record.get('count', 0))
                
                if count > 0 and day > 0:
                    try:
                        lectures_data = {'year': year, 'month': month, 'day': day, 'math': 99999}
                        lectures_response = requests.post(lectures_url, headers=headers, data=lectures_data, timeout=10)
                        lectures_response.raise_for_status()
                        lectures_result = lectures_response.json()
                        
                        if lectures_result.get('data', {}).get('result') == 'success':
                            items = lectures_result['data'].get('record', [])
                            
                            for item in items:
                                title = item.get('title', '')
                                if not title or len(title) < 2:
                                    continue
                                
                                start_date_str = item.get('activityStartTime', '')
                                end_date_str = item.get('activityEndTime', '')
                                
                                start_date = ''
                                end_date = ''
                                
                                date_match = re.search(r'(\d{4})年(\d{1,2})月(\d{1,2})日', start_date_str)
                                if date_match:
                                    y, m, d = date_match.groups()
                                    start_date = f"{y}-{int(m):02d}-{int(d):02d}"
                                
                                date_match = re.search(r'(\d{4})年(\d{1,2})月(\d{1,2})日', end_date_str)
                                if date_match:
                                    y, m, d = date_match.groups()
                                    end_date = f"{y}-{int(m):02d}-{int(d):02d}"
                                
                                if not start_date:
                                    continue
                                
                                if not end_date:
                                    end_date = start_date
                                
                                location = item.get('location', '')
                                address = item.get('address', '')
                                library_name = item.get('libraryname', '')
                                organizer = item.get('organizer2', '')
                                needsignup = item.get('needsignup', 0)
                                signupnote = item.get('signupnote', '')
                                
                                venue = f"{SZLIB_NAME} ({library_name})" if library_name else SZLIB_NAME
                                
                                description = ''
                                if organizer:
                                    description += f"主办方：{organizer}\n"
                                if location:
                                    description += f"地点：{location}\n"
                                if address:
                                    description += f"地址：{address}\n"
                                if needsignup == 1:
                                    description += "需预约\n"
                                if signupnote:
                                    description += f"备注：{signupnote[:200]}"
                                
                                description = description.strip()
                                
                                activity_url = f"https://www.szlib.org.cn/m/activity/lectureInfo.jsp?id={item['id']}&year={year}&month={month}&customizedUrl=salon"
                                
                                activity = {
                                    'name': title,
                                    'venue': venue,
                                    'start_date': start_date,
                                    'end_date': end_date,
                                    'url': activity_url,
                                    'contact': '',
                                    'description': description,
                                    'source': 'szlib'
                                }
                                activities.append(activity)
                            
                            time.sleep(0.3)
                            
                    except Exception:
                        continue
            
            time.sleep(0.5)
            
        except Exception:
            continue
    
    return activities


def main():
    activities = fetch_szlib_activities()
    print(f"Fetched {len(activities)} activities from {SZLIB_NAME}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"szlib_{JSON_FILE}")
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)
    
    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()