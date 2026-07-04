import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

urls = [
    ('宝安图书馆', 'https://www.balib.cn/'),
    ('欢乐港湾', 'https://www.octharbor.com/'),
    ('湾区之眼', 'https://www.baculturalcenter.com/'),
    ('宝安文体官网', 'http://www.baoan.gov.cn/bawtlyj/'),
]

for name, url in urls:
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f'{name}: {url}')
        print(f'  Status: {response.status_code}')
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.title.string if soup.title else 'N/A'
        print(f'  Title: {title}')
        
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            text = link.get_text().strip()
            if '活动' in text or 'event' in href.lower() or '展览' in text or '演出' in text:
                links.append((text, href))
        
        print(f'  活动相关链接: {len(links)}')
        for text, href in links[:5]:
            print(f'    {text}: {href}')
        print('---')
    except Exception as e:
        print(f'{name}: {url}')
        print(f'  Error: {e}')
        print('---')