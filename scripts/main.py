import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper_szcec import fetch_szcec_exhibitions
from scraper_shenzhen_world import fetch_shenzhen_world_exhibitions
from ics_generator import create_ics
from rss_generator import generate_rss
from config import OUTPUT_DIR, ICS_FILE, JSON_FILE


def main():
    print("=== 开始抓取深圳展览数据 ===")
    
    print("\n1. 抓取深圳会展中心数据...")
    szcec_exhibitions = fetch_szcec_exhibitions()
    print(f"   获取到 {len(szcec_exhibitions)} 个展会")
    
    print("\n2. 抓取深圳国际会展中心数据...")
    world_exhibitions = fetch_shenzhen_world_exhibitions()
    print(f"   获取到 {len(world_exhibitions)} 个展会")
    
    all_exhibitions = szcec_exhibitions + world_exhibitions
    all_exhibitions.sort(key=lambda x: x['start_date'])
    
    print(f"\n3. 共获取 {len(all_exhibitions)} 个展会")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    json_path = os.path.join(OUTPUT_DIR, JSON_FILE)
    import json
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(all_exhibitions, f, ensure_ascii=False, indent=2)
    print(f"   JSON数据已保存到 {json_path}")
    
    ics_content = create_ics(all_exhibitions)
    ics_path = os.path.join(OUTPUT_DIR, ICS_FILE)
    with open(ics_path, 'w', encoding='utf-8') as f:
        f.write(ics_content)
    print(f"   ICS日历已生成到 {ics_path}")
    
    generate_rss()
    print(f"   RSS订阅已生成到 {os.path.join(OUTPUT_DIR, 'exhibitions.rss')}")
    
    print("\n=== 完成 ===")


if __name__ == "__main__":
    main()