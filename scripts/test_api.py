import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

print("=== Testing APIs ===\n")

calendar_url = 'https://www.szlib.org.cn/m/activity/getLectureCalendars.jsp?customizedUrl=salon&library=044005'
try:
    response = requests.post(calendar_url, headers=headers, data={'year': 2026, 'month': 7, 'math': 99999}, timeout=10)
    print(f"SZ Library Calendar API:")
    print(f"  Status: {response.status_code}")
    print(f"  Content: {response.text[:300]}")
except Exception as e:
    print(f"SZ Library Calendar API Error: {e}")
print()

lectures_url = 'https://www.szlib.org.cn/m/activity/getLectures.jsp?customizedUrl=salon&library=044005'
try:
    response = requests.post(lectures_url, headers=headers, data={'year': 2026, 'month': 7, 'day': 15, 'math': 99999}, timeout=10)
    print(f"SZ Library Lectures API:")
    print(f"  Status: {response.status_code}")
    print(f"  Content: {response.text[:500]}")
except Exception as e:
    print(f"SZ Library Lectures API Error: {e}")
print()

print("=== Testing Bao'an Library ===")
balib_urls = [
    'https://www.balib.cn/',
    'https://www.balib.cn/category/132',
    'https://www.baoanlib.com/',
]
for url in balib_urls:
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f"{url}")
        print(f"  Status: {response.status_code}")
        print(f"  Length: {len(response.text)}")
    except Exception as e:
        print(f"{url} - Error: {e}")
    print()

print("=== Testing Government Sites ===")
gov_urls = [
    'http://www.baoan.gov.cn/',
    'https://www.baoan.gov.cn/',
    'http://www.baoan.gov.cn/bawtlyj/',
]
for url in gov_urls:
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f"{url}")
        print(f"  Status: {response.status_code}")
        print(f"  Length: {len(response.text)}")
    except Exception as e:
        print(f"{url} - Error: {e}")
    print()

print("=== Testing Bay Area Eye ===")
bayarea_urls = [
    'https://www.baoanartcenter.com/',
    'https://www.baoan.gov.cn/baoanart/',
]
for url in bayarea_urls:
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f"{url}")
        print(f"  Status: {response.status_code}")
        print(f"  Length: {len(response.text)}")
    except Exception as e:
        print(f"{url} - Error: {e}")
    print()