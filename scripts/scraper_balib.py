import requests
import json
import os
import sys
import re
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import BALIB_NAME, OUTPUT_DIR, JSON_FILE


def fetch_balib_activities():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    activities = []
    api_url = 'https://www.balib.cn/api/getSZAction'
    seen_ids = set()
    proxies = {'http': 'http://127.0.0.1:18080', 'https': 'http://127.0.0.1:18080'}

    # 尝试翻页获取所有活动
    for page in range(1, 50):
        try:
            params = {'page': page, 'limit': 10}
            response = requests.get(api_url, headers=headers, params=params,
                                   timeout=30, verify=False, proxies=proxies)
            response.raise_for_status()
            data = response.json()

            if data.get('code') != 0:
                break

            records = data.get('record', [])
            if not records:
                break

            new_count = 0
            for item in records:
                item_id = item.get('id')
                if item_id in seen_ids:
                    continue
                seen_ids.add(item_id)

                title = item.get('title', '').strip()
                if not title or len(title) < 2:
                    continue

                content = item.get('content', '').strip()
                start_time = item.get('activityStartTime', '')
                end_time = item.get('activityEndTime', '')
                location = item.get('location', '')
                address = item.get('address', '')
                library_name = item.get('libraryname', '')
                signup_note = item.get('signupnote', '')
                way = item.get('way', '')
                speaker = item.get('speaker', '')
                speaker_summary = item.get('speakersummary', '')
                organizer = item.get('organizer2', '') or item.get('organizer4', '')

                # 解析日期
                start_date = ''
                end_date = ''
                date_match = re.search(r'(\d{4})年(\d{1,2})月(\d{1,2})日', start_time)
                if date_match:
                    y, m, d = date_match.groups()
                    start_date = f"{y}-{int(m):02d}-{int(d):02d}"

                date_match = re.search(r'(\d{4})年(\d{1,2})月(\d{1,2})日', end_time)
                if date_match:
                    y, m, d = date_match.groups()
                    end_date = f"{y}-{int(m):02d}-{int(d):02d}"

                if not start_date:
                    continue

                if not end_date:
                    end_date = start_date

                venue = f"{BALIB_NAME} ({library_name})" if library_name and library_name != BALIB_NAME else BALIB_NAME

                # 构建描述
                description_parts = []
                if content and content != title:
                    description_parts.append(content)
                if speaker:
                    description_parts.append(f"主讲人：{speaker}")
                if speaker_summary:
                    description_parts.append(speaker_summary)
                if location:
                    description_parts.append(f"地点：{location}")
                if address and address != '详见活动简介':
                    description_parts.append(f"地址：{address}")
                if way:
                    description_parts.append(f"方式：{way}")
                if signup_note:
                    description_parts.append(f"咨询：{signup_note}")
                if organizer:
                    description_parts.append(f"主办：{organizer}")

                description = '；'.join(description_parts)

                activity = {
                    'name': title,
                    'venue': venue,
                    'start_date': start_date,
                    'end_date': end_date,
                    'url': f"https://www.balib.cn",
                    'contact': signup_note or '',
                    'description': description,
                    'source': 'balib'
                }
                activities.append(activity)
                new_count += 1

            if new_count == 0:
                break  # 连续两页无新数据则停止

            time.sleep(0.3)

        except Exception as e:
            print(f"balib page {page} error: {e}")
            break

    return activities


def main():
    activities = fetch_balib_activities()
    print(f"Fetched {len(activities)} activities from {BALIB_NAME}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"balib_{JSON_FILE}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)

    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()