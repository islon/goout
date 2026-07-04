import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore', category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

urls = [
    ('欢乐港湾官网', 'https://www.octohbay.net/'),
    ('欢乐港湾官网http', 'http://www.octohbay.net/'),
    ('宝安图书馆', 'https://www.balib.cn/'),
    ('宝安文体通', 'http://www.baoan.gov.cn/bawtlyj/'),
    ('深圳文体旅游局', 'https://wtl.sz.gov.cn/'),
    ('深圳政府在线活动', 'https://www.sz.gov.cn/hd/'),
]

for name, url in urls:
    try:
        response = requests.get(url, headers=headers, timeout=15, verify=False)
        print(f'{name}: {url}')
        print(f'  Status: {response.status_code}')
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.title.string if soup.title else 'N/A'
        print(f'  Title: {title}')
        print(f'  Content length: {len(response.text)}')
        
        meta_descs = soup.find_all('meta', attrs={'name': 'description'})
        if meta_descs:
            print(f'  Description: {meta_descs[0]["content"]}')
        
        print('---')
    except Exception as e:
        print(f'{name}: {url}')
        print(f'  Error: {e}')
        print('---')