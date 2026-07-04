import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore', category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

print("=== 深入分析欢乐港湾官网活动区域 ===")
url = 'https://www.octohbay.net/'
response = requests.get(url, headers=headers, timeout=15, verify=False)
soup = BeautifulSoup(response.text, 'lxml')

information_div = soup.find('div', class_='information')
if information_div:
    print(f"information div 内容:")
    items = information_div.find_all(['a', 'div', 'span'])
    for item in items[:20]:
        text = item.get_text().strip()
        if text:
            href = item.get('href', '')
            print(f"  {text[:50]}: {href}")

news_section = soup.find('div', class_='inNews-section')
if news_section:
    print(f"\ninNews-section 内容:")
    items = news_section.find_all('div', class_='inNews-section-item')
    print(f"  item数量: {len(items)}")
    if items:
        for item in items[:5]:
            text = item.get_text().strip()
            href = item.find('a', href=True)
            href = href['href'] if href else ''
            print(f"  {text[:80]}: {href}")

print("\n=== 深入分析宝安图书馆活动区域 ===")
url = 'https://www.balib.cn/'
response = requests.get(url, headers=headers, timeout=15, verify=False)
soup = BeautifulSoup(response.text, 'lxml')

act_not_area = soup.find('div', class_='actNotArea')
if act_not_area:
    print(f"actNotArea 内容:")
    items = act_not_area.find_all(['a', 'div', 'span'])
    for item in items[:20]:
        text = item.get_text().strip()
        if text:
            href = item.get('href', '')
            print(f"  {text[:50]}: {href}")

act_swiper = soup.find('div', class_='actSwiper')
if act_swiper:
    print(f"\nactSwiper 内容:")
    items = act_swiper.find_all(['a', 'div', 'span'])
    for item in items[:20]:
        text = item.get_text().strip()
        if text:
            href = item.get('href', '')
            print(f"  {text[:50]}: {href}")

print("\n=== 查找宝安图书馆信息列表 ===")
info_urls = [
    'https://www.balib.cn/information/43885',
    'https://www.balib.cn/information/23569',
    'https://www.balib.cn/information/list',
    'https://www.balib.cn/information/list_1.html',
]

for url in info_urls:
    try:
        response = requests.get(url, headers=headers, timeout=15, verify=False)
        print(f"{url}: {response.status_code}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            title = soup.title.string if soup.title else 'N/A'
            print(f"  Title: {title}")
            print(f"  Content length: {len(response.text)}")
            
            content_div = soup.find('div', class_=True)
            if content_div:
                text = content_div.get_text().strip()[:200]
                print(f"  Preview: {text}")
    except Exception as e:
        print(f"{url}: Error - {e}")