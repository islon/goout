import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore', category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

print("=== 欢乐港湾官网 ===")
url = 'https://www.octohbay.net/'
response = requests.get(url, headers=headers, timeout=15, verify=False)
soup = BeautifulSoup(response.text, 'lxml')

links = []
for link in soup.find_all('a', href=True):
    href = link['href']
    text = link.get_text().strip()
    if href and text:
        links.append((text, href))

print(f"总链接数: {len(links)}")
print("\n活动相关链接:")
for text, href in links[:20]:
    if '活动' in text or 'event' in href.lower() or '展览' in text or '演出' in text or 'activity' in href.lower() or 'show' in href.lower():
        print(f"  {text}: {href}")

print("\n=== 宝安图书馆 ===")
url = 'https://www.balib.cn/'
response = requests.get(url, headers=headers, timeout=15, verify=False)
soup = BeautifulSoup(response.text, 'lxml')

links = []
for link in soup.find_all('a', href=True):
    href = link['href']
    text = link.get_text().strip()
    if href and text:
        links.append((text, href))

print(f"总链接数: {len(links)}")
print("\n活动相关链接:")
for text, href in links[:30]:
    if '活动' in text or '展览' in text or 'information' in href.lower() or '/hd' in href:
        print(f"  {text}: {href}")

print("\n=== 查找欢乐港湾活动页面 ===")
activity_urls = [
    'https://www.octohbay.net/activity',
    'https://www.octohbay.net/events',
    'https://www.octohbay.net/events/list',
    'https://www.octohbay.net/activities',
]

for url in activity_urls:
    try:
        response = requests.get(url, headers=headers, timeout=15, verify=False)
        print(f"{url}: {response.status_code}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            print(f"  Title: {soup.title.string if soup.title else 'N/A'}")
            print(f"  Content length: {len(response.text)}")
    except Exception as e:
        print(f"{url}: Error - {e}")