import os
import sys
import json
from datetime import datetime, timedelta
from hashlib import md5

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, ICS_FILE, JSON_FILE, CALENDAR_NAME, CALENDAR_DESCRIPTION, CALENDAR_TIMEZONE


def generate_uid(exhibition):
    content = f"{exhibition['name']}{exhibition['venue']}{exhibition['start_date']}"
    return md5(content.encode()).hexdigest()[:16]


def format_date(date_str, is_end=False):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    if is_end:
        date = date + timedelta(days=1)
    return date.strftime('%Y%m%d')


def create_ics(exhibitions):
    lines = []
    lines.append('BEGIN:VCALENDAR')
    lines.append('VERSION:2.0')
    lines.append('PRODID:-//Shenzhen Exhibitions//Calendar//ZH')
    lines.append(f'X-WR-CALNAME:{CALENDAR_NAME}')
    lines.append(f'X-WR-CALDESC:{CALENDAR_DESCRIPTION}')
    lines.append(f'X-WR-TIMEZONE:{CALENDAR_TIMEZONE}')
    
    lines.append('BEGIN:VTIMEZONE')
    lines.append('TZID:Asia/Shanghai')
    lines.append('BEGIN:STANDARD')
    lines.append('DTSTART:19701001T030000')
    lines.append('RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU')
    lines.append('TZNAME:CST')
    lines.append('TZOFFSETFROM:+0800')
    lines.append('TZOFFSETTO:+0800')
    lines.append('END:STANDARD')
    lines.append('BEGIN:DAYLIGHT')
    lines.append('DTSTART:19700401T020000')
    lines.append('RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=-1SU')
    lines.append('TZNAME:CST')
    lines.append('TZOFFSETFROM:+0800')
    lines.append('TZOFFSETTO:+0800')
    lines.append('END:DAYLIGHT')
    lines.append('END:VTIMEZONE')
    
    for exhibition in exhibitions:
        uid = generate_uid(exhibition)
        
        lines.append('BEGIN:VEVENT')
        lines.append(f'UID:{uid}@shenzhen-exhibitions')
        lines.append(f'DTSTAMP:{datetime.now().strftime("%Y%m%dT%H%M%SZ")}')
        
        start_dt = format_date(exhibition['start_date'])
        end_dt = format_date(exhibition['end_date'], is_end=True)
        
        lines.append(f'DTSTART;VALUE=DATE:{start_dt}')
        lines.append(f'DTEND;VALUE=DATE:{end_dt}')
        
        lines.append(f'SUMMARY:{exhibition["name"]}')
        lines.append(f'LOCATION:{exhibition["venue"]}')
        
        description_parts = []
        if exhibition.get('description'):
            description_parts.append(exhibition['description'])
        description_parts.append(f'地点: {exhibition["venue"]}')
        description_parts.append(f'时间: {exhibition["start_date"]} 至 {exhibition["end_date"]}')
        if exhibition.get('url'):
            description_parts.append(f'详情: {exhibition["url"]}')
        if exhibition.get('contact'):
            description_parts.append(f'联系: {exhibition["contact"]}')
        
        description = '\\n'.join(description_parts)
        lines.append(f'DESCRIPTION:{description}')
        
        lines.append('END:VEVENT')
    
    lines.append('END:VCALENDAR')
    
    return '\r\n'.join(lines)


def main():
    all_exhibitions = []
    
    main_path = os.path.join(OUTPUT_DIR, JSON_FILE)
    if os.path.exists(main_path):
        with open(main_path, 'r', encoding='utf-8') as f:
            all_exhibitions = json.load(f)
    
    all_exhibitions.sort(key=lambda x: x['start_date'])
    
    ics_content = create_ics(all_exhibitions)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ics_path = os.path.join(OUTPUT_DIR, ICS_FILE)
    
    with open(ics_path, 'w', encoding='utf-8') as f:
        f.write(ics_content)
    
    print(f"Generated {ICS_FILE} with {len(all_exhibitions)} events")


if __name__ == "__main__":
    main()