import requests
from bs4 import BeautifulSoup
import re
import warnings
warnings.filterwarnings('ignore', category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

print("=== 分析欢乐港湾官网的JavaScript ===")
url = 'https://www.octohbay.net/'
response = requests.get(url, headers=headers, timeout=15, verify=False)
soup = BeautifulSoup(response.text, 'lxml')

scripts = soup.find_all('script', src=True)
print("\n外部JS文件:")
for script in scripts:
    print(f"  {script['src']}")

inline_scripts = soup.find_all('script')
for i, script in enumerate(inline_scripts):
    if script.string:
        text = script.string
        apis = re.findall(r'(https?://[^\s\'"]+/api/[^\s\'"]*)', text)
        if apis:
            print(f"\n脚本{i}中的API:")
            for api in apis:
                print(f"  {api}")

        urls_in_script = re.findall(r'(https?://[^\s\'"]+)', text)
        if urls_in_script:
            print(f"\n脚本{i}中的URL:")
            for u in urls_in_script[:5]:
                print(f"  {u}")

print("\n=== 查找欢乐港湾活动API ===")
api_urls = [
    'https://www.octohbay.net/api/events',
    'https://www.octohbay.net/api/activities',
    'https://www.octohbay.net/api/news',
    'https://www.octohbay.net/api/list',
    'https://www.octohbay.net/api/getEvents',
]

for url in api_urls:
    try:
        response = requests.get(url, headers=headers, timeout=15, verify=False)
        print(f"{url}: {response.status_code}")
        if response.status_code == 200:
            content = response.text[:500]
            print(f"  Response: {content}")
    except Exception as e:
        print(f"{url}: Error - {e}")

print("\n=== 查找湾区之眼官网 ===")
bay_eye_urls = [
    'https://www.bayeye.cn/',
    'https://www.bay-eye.cn/',
    'https://www.bayeye.com/',
    'https://www.baoanlibrary.com/',
    'https://www.sz-publishing.com/',
    'https://www.szpg.com/',
]

for name, url in [('湾区之眼1', 'https://www.bayeye.cn/'), ('湾区之眼2', 'https://www.bay-eye.cn/'), ('深圳出版集团', 'https://www.szpg.com/')]:
    try:
        response = requests.get(url, headers=headers, timeout=15, verify=False)
        print(f"{name}: {url}")
        print(f"  Status: {response.status_code}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            title = soup.title.string if soup.title else 'N/A'
            print(f"  Title: {title}")
    except Exception as e:
        print(f"{name}: {url}")
        print(f"  Error: {e}")