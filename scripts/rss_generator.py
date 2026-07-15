import json
import os
import sys
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, JSON_FILE

def generate_rss():
    json_path = os.path.join(OUTPUT_DIR, JSON_FILE)
    
    with open(json_path, 'r', encoding='utf-8') as f:
        exhibitions = json.load(f)
    
    exhibitions.sort(key=lambda x: x['start_date'], reverse=True)
    
    rss_items = []
    for ex in exhibitions[:50]:
        title = ex.get('title') or ex.get('name', '')
        link = ex.get('link') or ex.get('url', 'https://islon.github.io/shenzhen-exhibitions/')
        date_range = ex['start_date'] if ex['start_date'] == ex['end_date'] else f"{ex['start_date']} ~ {ex['end_date']}"
        description = ex.get('description', '')[:300]
        rss_items.append(f"""    <item>
        <title>{title}</title>
        <link>{link}</link>
        <description><![CDATA[
            <strong>日期：</strong>{date_range}<br>
            <strong>地点：</strong>{ex['venue']}<br>
            {description if description else ''}
        ]]></description>
        <pubDate>{datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')}</pubDate>
        <guid>{title}</guid>
    </item>""")
    
    rss_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
    <title>深圳展览日历</title>
    <link>https://islon.github.io/shenzhen-exhibitions/</link>
    <description>深圳会展中心 & 深圳国际会展中心 展览日程</description>
    <language>zh-CN</language>
    <lastBuildDate>{datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')}</lastBuildDate>
    <ttl>60</ttl>
{chr(10).join(rss_items)}
</channel>
</rss>"""
    
    rss_path = os.path.join(OUTPUT_DIR, 'exhibitions.rss')
    with open(rss_path, 'w', encoding='utf-8') as f:
        f.write(rss_content)
    
    print(f"RSS feed generated: {rss_path}")

if __name__ == "__main__":
    generate_rss()