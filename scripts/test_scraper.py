import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

url = 'https://www.wuzhanliuhui.com/hall/10005/exh-t-k-p1.htm'
response = requests.get(url, headers=headers)

if response.encoding != 'utf-8':
    response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, 'lxml')

exh_items = soup.find_all('li', class_='exh-item')
print(f'找到 {len(exh_items)} 个展览项目')
print()

for item in exh_items:
    name_tag = item.find('a', class_='subject')
    name = name_tag.get_text().strip() if name_tag else 'N/A'
    date_p = item.find('p', class_='date')
    date_text = date_p.get_text().strip() if date_p else 'N/A'
    print(f'名称: {name[:30]}')
    print(f'原始日期: {date_text}')
    
    year_match = re.search(r'(\d{4})年', date_text)
    current_year = int(year_match.group(1)) if year_match else 2025
    
    month_match = re.search(r'(\d{1,2})月', date_text)
    current_month = int(month_match.group(1)) if month_match else 1
    
    date_range_pattern = re.search(r'(\d{1,2})[-~—–](\d{1,2})日', date_text)
    if date_range_pattern:
        start_day = int(date_range_pattern.group(1))
        end_day = int(date_range_pattern.group(2))
        start_date = f'{current_year}-{current_month:02d}-{start_day:02d}'
        end_date = f'{current_year}-{current_month:02d}-{end_day:02d}'
        print(f'解析结果: {start_date} ~ {end_date}')
    else:
        day_match = re.search(r'(\d{1,2})日', date_text)
        if day_match:
            day = int(day_match.group(1))
            print(f'解析结果: {current_year}-{current_month:02d}-{day:02d}')
        else:
            print('解析失败')
    print()