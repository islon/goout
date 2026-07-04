import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore', category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

print("=== 深入分析欢乐港湾官网 ===")
url = 'https://www.octohbay.net/'
response = requests.get(url, headers=headers, timeout=15, verify=False)
soup = BeautifulSoup(response.text, 'lxml')

print("\n页面结构分析:")
divs = soup.find_all('div', class_=True)
classes = set()
for div in divs:
    for cls in div.get('class', []):
        classes.add(cls)

print(f"所有div class: {sorted(list(classes))[:30]}")

nav_items = soup.find_all(['nav', 'ul', 'li'])
print(f"\n导航元素数量: nav={len(soup.find_all('nav'))}, ul={len(soup.find_all('ul'))}, li={len(soup.find_all('li'))}")

print("\n=== 深入分析宝安图书馆官网 ===")
url = 'https://www.balib.cn/'
response = requests.get(url, headers=headers, timeout=15, verify=False)
soup = BeautifulSoup(response.text, 'lxml')

print("\n页面结构分析:")
divs = soup.find_all('div', class_=True)
classes = set()
for div in divs:
    for cls in div.get('class', []):
        classes.add(cls)

print(f"所有div class: {sorted(list(classes))[:40]}")

content_box = soup.find('div', class_='content-box')
if content_box:
    print(f"\ncontent-box 内容:")
    items = content_box.find_all('div', class_='item')
    print(f"  item数量: {len(items)}")
    if items:
        first_item = items[0]
        print(f"  第一个item HTML: {str(first_item)[:500]}")

print("\n=== 查找宝安图书馆信息页面 ===")
info_urls = [
    'https://www.balib.cn/information/',
    'https://www.balib.cn/information/index.html',
    'https://www.balib.cn/hd/',
    'https://www.balib.cn/hd/index.html',
]

for url in info_urls:
    try:
        response = requests.get(url, headers=headers, timeout=15, verify=False)
        print(f"{url}: {response.status_code}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            print(f"  Title: {soup.title.string if soup.title else 'N/A'}")
            print(f"  Content length: {len(response.text)}")
    except Exception as e:
        print(f"{url}: Error - {e}")