import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

print('=== Testing category 13 ===')
response = requests.get('https://www.balib.cn/category/13', headers=headers, timeout=10)
soup = BeautifulSoup(response.text, 'lxml')

links_with_dates = []
for link in soup.find_all('a', href=True):
    href = link['href']
    text = link.get_text().strip()
    if href.startswith('/information/'):
        date_match = re.search(r'(\d{4}/\d{2}/\d{2})', text)
        if date_match:
            links_with_dates.append((date_match.group(1), text, href))

for date, text, href in links_with_dates[:10]:
    print(f'{date} - {text}: {href}')

print()
print(f'Total links with dates: {len(links_with_dates)}')

print()
print('=== Testing some detail pages ===')
test_links = [
    '/information/43885',
    '/information/41022',
]

for href in test_links:
    try:
        response = requests.get(f'https://www.balib.cn{href}', headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'lxml')
        text = soup.get_text()
        
        date_patterns = re.findall(r'(\d{4})[-/年](\d{1,2})[-/月](\d{1,2})[日号]?', text)
        if date_patterns:
            print(f'{href}:')
            for dp in date_patterns[:3]:
                print(f'  Date: {dp[0]}-{int(dp[1]):02d}-{int(dp[2]):02d}')
        
        title_match = re.search(r'发布时间.*?(\d{4}-\d{2}-\d{2})', text)
        if title_match:
            print(f'  Publish date: {title_match.group(1)}')
        
    except Exception as e:
        print(f'{href}: Error - {e}')