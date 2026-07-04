import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

url = 'https://www.balib.cn/category/13'
response = requests.get(url, headers=headers, timeout=10)
soup = BeautifulSoup(response.text, 'lxml')

content_box = soup.find('div', class_='content-box')
if content_box:
    items = content_box.find_all('div', class_='item')
    print(f'items count: {len(items)}')
    
    for item in items[:3]:
        print()
        links = item.find_all('a', href=True)
        for link in links:
            href = link['href']
            text = link.get_text().strip()[:80]
            print(f'Link: {href} - {text}')
        
        spans = item.find_all('span')
        for span in spans:
            text = span.get_text().strip()
            if text:
                print(f'Span: {text[:80]}')
        
        divs = item.find_all('div')
        for div in divs:
            cls = div.get('class')
            if cls:
                cls_str = ' '.join(cls)
                text = div.get_text().strip()[:50]
                print(f'Div class={cls_str}: {text}')