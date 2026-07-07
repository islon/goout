import os
import sys
import json
import traceback

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ics_generator import create_ics
from rss_generator import generate_rss
from config import OUTPUT_DIR, ICS_FILE, JSON_FILE

# 所有爬虫模块，按场馆分组
SCRAPERS = [
    # 会展中心
    ("深圳会展中心", "scraper_szcec", "fetch_szcec_exhibitions"),
    ("深圳国际会展中心", "scraper_shenzhen_world", "fetch_shenzhen_world_exhibitions"),
    # 图书馆
    ("深圳图书馆", "scraper_szlib", "fetch_szlib_activities"),
    ("宝安图书馆", "scraper_balib", "fetch_balib_activities"),
    ("南山图书馆", "scraper_nslib", "fetch_nslib_activities"),
    ("深圳少儿图书馆", "scraper_sz_children_lib", "fetch_sz_children_lib_activities"),
    ("光明少儿图书馆", "scraper_gm_lib", "fetch_gm_lib_activities"),
    ("盐田区图书馆", "scraper_yt_lib", "fetch_yt_lib_activities"),
    # 博物馆
    ("南山博物馆", "scraper_nsmuseum", "fetch_nsmuseum_activities"),
    ("蛇口海洋科普馆", "scraper_skhykpg", "fetch_skhykpg_activities"),
    ("深爱人才馆", "scraper_sarc", "fetch_sarc_activities"),
    ("南头古城博物馆群", "scraper_ntgc", "fetch_ntgc_activities"),
    ("招商局历史博物馆", "scraper_zsjbwg", "fetch_zsjbwg_activities"),
    ("深圳自然博物馆", "scraper_ps_nature", "fetch_ps_nature_activities"),
    ("深圳科技馆（光明）", "scraper_gm_kjg", "fetch_gm_kjg_activities"),
    ("中英街历史博物馆", "scraper_yt_history", "fetch_yt_history_activities"),
    ("大鹏地质公园博物馆", "scraper_dp_geopark", "fetch_dp_geopark_activities"),
    ("大亚湾核能科技馆", "scraper_dp_nuclear", "fetch_dp_nuclear_activities"),
    # 文化馆/文体中心
    ("南山区文化馆", "scraper_nswhg", "fetch_nswhg_activities"),
    ("南山文体中心", "scraper_nswtzx", "fetch_nswtzx_activities"),
    ("深圳湾体育中心", "scraper_szwty", "fetch_szwty_activities"),
    ("青少年活动中心", "scraper_nsqsng", "fetch_nsqsng_activities"),
    ("安全教育体验馆", "scraper_nsaqjy", "fetch_nsaqjy_activities"),
    ("南山书房", "scraper_nssxf", "fetch_nssxf_activities"),
    # 宝安区
    ("宝安科技馆", "scraper_baoan_kjg", "fetch_baoan_kjg_activities"),
    ("宝安体育中心", "scraper_baoan_ty", "fetch_baoan_ty_activities"),
    ("宝安1990馆", "scraper_baoan_1990", "fetch_baoan_1990_activities"),
    # 龙华区
    ("龙华生态文明展览馆", "scraper_lh_ecology", "fetch_lh_ecology_activities"),
    ("龙华古生物博物馆", "scraper_lh_paleo", "fetch_lh_paleo_activities"),
    ("龙华版画基地", "scraper_lh_printmaking", "fetch_lh_printmaking_activities"),
    # 龙岗区
    ("龙岗客家民俗博物馆", "scraper_lg_hakka", "fetch_lg_hakka_activities"),
    # 其他
    ("湾区之眼", "scraper_bayarea_eye", "fetch_bayarea_eye_activities"),
    ("华侨城湿地", "scraper_oct_wetland", "fetch_oct_wetland_activities"),
    ("安全教育基地", "scraper_sz_safety", "fetch_sz_safety_activities"),
]


def main():
    print("=== 开始抓取深圳展览与亲子活动数据 ===\n")

    all_exhibitions = []
    success_count = 0
    fail_count = 0

    for i, (name, module_name, func_name) in enumerate(SCRAPERS, 1):
        print(f"{i}. 抓取{name}数据...")
        try:
            mod = __import__(module_name)
            func = getattr(mod, func_name)
            results = func()
            print(f"   获取到 {len(results)} 个活动")
            all_exhibitions.extend(results)
            success_count += 1
        except Exception as e:
            print(f"   [失败] {e}")
            traceback.print_exc()
            fail_count += 1

    all_exhibitions.sort(key=lambda x: x.get('start_date', ''))

    print(f"\n--- 共获取 {len(all_exhibitions)} 个活动（成功{success_count}个源，失败{fail_count}个源）---")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    json_path = os.path.join(OUTPUT_DIR, JSON_FILE)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(all_exhibitions, f, ensure_ascii=False, indent=2)
    print(f"JSON数据已保存到 {json_path}")

    ics_content = create_ics(all_exhibitions)
    ics_path = os.path.join(OUTPUT_DIR, ICS_FILE)
    with open(ics_path, 'w', encoding='utf-8') as f:
        f.write(ics_content)
    print(f"ICS日历已生成到 {ics_path}")

    try:
        generate_rss()
        print(f"RSS订阅已生成")
    except Exception as e:
        print(f"RSS生成失败: {e}")

    print("\n=== 完成 ===")
    return all_exhibitions


if __name__ == "__main__":
    main()
