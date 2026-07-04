import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

urls = [
    ('欢乐港湾1', 'https://octharbor.com/'),
    ('欢乐港湾2', 'https://www.oct-harbor.com/'),
    ('欢乐港湾3', 'https://oct-harbor.com/'),
    ('湾区之眼1', 'https://www.bacac.com.cn/'),
    ('湾区之眼2', 'https://bacac.com.cn/'),
    ('湾区之眼3', 'https://www.baoanartcenter.com/'),
    ('宝安文化艺术中心', 'https://www.bacac.cn/'),
    ('深圳活动网', 'https://www.sz.gov.cn/'),
]

for name, url in urls:
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f'{name}: {url}')
        print(f'  Status: {response.status_code}')
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.title.string if soup.title else 'N/A'
        print(f'  Title: {title}')
        print('---')
    except Exception as e:
        print(f'{name}: {url}')
        print(f'  Error: {e}')
        print('---')