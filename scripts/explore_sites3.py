import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

urls = [
    ('欢乐港湾官网', 'https://www.octohbay.net/'),
    ('欢乐港湾官网http', 'http://www.octohbay.net/'),
    ('欢乐港湾活动页', 'https://www.octohbay.net/activity'),
    ('宝安文体通', 'http://www.baoan.gov.cn/bawtlyj/'),
    ('宝安文体通活动', 'http://www.baoan.gov.cn/bawtlyj/hd/'),
    ('深圳文体旅游局活动', 'https://wtl.sz.gov.cn/bsfw/mzwhhd/'),
]

for name, url in urls:
    try:
        response = requests.get(url, headers=headers, timeout=15)
        print(f'{name}: {url}')
        print(f'  Status: {response.status_code}')
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.title.string if soup.title else 'N/A'
        print(f'  Title: {title}')
        print(f'  Content length: {len(response.text)}')
        
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            text = link.get_text().strip()
            if '活动' in text or 'event' in href.lower() or '展览' in text or '演出' in text or 'activity' in href.lower():
                if href not in [l[1] for l in links]:
                    links.append((text, href))
        
        print(f'  活动相关链接: {len(links)}')
        for text, href in links[:10]:
            print(f'    {text}: {href}')
        print('---')
    except Exception as e:
        print(f'{name}: {url}')
        print(f'  Error: {e}')
        print('---')