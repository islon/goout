import requests
import json
import os
import sys
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import SZCEC_URL, SZCEC_NAME, OUTPUT_DIR, JSON_FILE

# 从月日格式解析为完整日期，输入如 "01月15日 - 01月16日"
def parse_date_range(date_str, current_year):
    months_days = re.findall(r'(\d{1,2})月(\d{1,2})日', date_str)
    if len(months_days) < 2:
        return None, None
    
    start_month, start_day = int(months_days[0][0]), int(months_days[0][1])
    end_month, end_day = int(months_days[1][0]), int(months_days[1][1])
    
    # 确定年份：如果结束月份小于开始月份，说明跨年了，结束年份+1
    start_year = current_year
    end_year = current_year
    if end_month < start_month:
        end_year = current_year + 1
    
    # 如果只有一个月日对
    start_date = f"{start_year}-{start_month:02d}-{start_day:02d}"
    end_date = f"{end_year}-{end_month:02d}-{end_day:02d}"
    
    return start_date, end_date


def fetch_szcec_exhibitions():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    proxies = {'http': 'http://127.0.0.1:18080', 'https': 'http://127.0.0.1:18080'}
    
    try:
        response = requests.get(SZCEC_URL, headers=headers, timeout=30, verify=False, proxies=proxies)
        response.raise_for_status()
        response.encoding = 'utf-8'
        text = response.text
        
        # 解析表格结构
        tds = re.findall(r'<td[^>]*>([\s\S]*?)</td>', text)
        
        exhibitions = []
        current_year = 2025  # 列表从2025年12月开始
        
        i = 0
        while i < len(tds):
            cell_text = re.sub(r'<[^>]+>', '', tds[i]).strip()
            cell_text = cell_text.replace('&nbsp;', '').replace('&ldquo;', '').replace('&rdquo;', '')
            
            # 跳过表头
            if cell_text == '序号':
                i += 4
                continue
            
            # 月份标题行，更新年份
            if re.match(r'(\d{4})年(\d{1,2})月', cell_text):
                m = re.match(r'(\d{4})年(\d{1,2})月', cell_text)
                current_year = int(m.group(1))
                i += 2  # 月份标题占2个td
                continue
            
            # 空行
            if cell_text == '':
                i += 1
                continue
            
            # 序号 + 展会名称 + 日期 + 联系方式
            if re.match(r'^\d+$', cell_text) and i + 3 < len(tds):
                name = re.sub(r'<[^>]+>', '', tds[i+1]).strip()
                name = name.replace('&nbsp;', ' ').replace('&ldquo;', '').replace('&rdquo;', '')
                
                date_range = re.sub(r'<[^>]+>', '', tds[i+2]).strip()
                date_range = re.sub(r'\s+', ' ', date_range)
                
                contact = re.sub(r'<[^>]+>', '', tds[i+3]).strip()
                contact = re.sub(r'\s+', ' ', contact)
                
                start_date, end_date = parse_date_range(date_range, current_year)
                
                if name and start_date and end_date and name != '展览时间':
                    # 检测是否为"无名称"的条目（仅"展览时间"标记）
                    # 跳过已过期的（2025年末的）
                    if start_date >= '2026-01-01':
                        exhibition = {
                            'name': name,
                            'title': name,
                            'venue': SZCEC_NAME,
                            'start_date': start_date,
                            'end_date': end_date,
                            'link': 'https://www.szcec.com',
                            'contact': contact,
                            'description': f'{name}，{start_date}至{end_date}，深圳会展中心。{contact}',
                            'category': '展览',
                            'fee': '免费',
                            'family_friendly': False,
                            'source': 'szcec'
                        }
                        exhibitions.append(exhibition)
                
                i += 4
                continue
            
            i += 1
        
        return exhibitions
    
    except Exception as e:
        print(f"Error fetching SZCEC data: {e}")
        import traceback
        traceback.print_exc()
        return []


def main():
    exhibitions = fetch_szcec_exhibitions()
    print(f"Fetched {len(exhibitions)} exhibitions from {SZCEC_NAME}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_path = os.path.join(OUTPUT_DIR, f"szcec_{JSON_FILE}")
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(exhibitions, f, ensure_ascii=False, indent=2)
    
    print(f"Data saved to {json_path}")


if __name__ == "__main__":
    main()