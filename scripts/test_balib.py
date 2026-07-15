import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

response = requests.get('https://www.balib.cn/', headers=headers, timeout=10)
soup = BeautifulSoup(response.text, 'lxml')

print('=== Links containing activity keywords ===')
for link in soup.find_all('a', href=True):
    href = link['href']
    text = link.get_text().strip()
    keywords = ['活动', '讲座', '亲子', '沙龙', '展览']
    if any(k in text for k in keywords) and len(text) > 2:
        print(f'{text}: {href}')

print()
print('=== All category links ===')
for link in soup.find_all('a', href=True):
    href = link['href']
    if href.startswith('/category/'):
        print(f'{link.get_text().strip()}: {href}')

print()
print('=== Testing different URLs ===')
test_urls = [
    'https://www.balib.cn/category/13',
    'https://www.balib.cn/category/14',
    'https://www.balib.cn/category/270',
]
for url in test_urls:
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        soup2 = BeautifulSoup(resp.text, 'lxml')
        print(f'{url}: {resp.status_code}, {len(soup2.find_all("a"))} links')
    except Exception as e:
        print(f'{url}: Error - {e}')