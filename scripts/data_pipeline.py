import json
import os
import re
import sys
import ssl
import warnings
from datetime import datetime, timedelta

# 全局禁用 SSL 验证（gov.cn 网站证书有 BAD_ECPOINT 问题）
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

# Monkey-patch requests Session 以全局禁用 SSL 验证
import requests
_original_request = requests.Session.request
def _patched_request(self, method, url, **kwargs):
    kwargs['verify'] = False
    return _original_request(self, method, url, **kwargs)
requests.Session.request = _patched_request

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OUTPUT_DIR, JSON_FILE, ICS_FILE
from ics_generator import create_ics
from rss_generator import generate_rss

WECHAT_ACCOUNTS_FILE = os.path.join(os.path.dirname(__file__), 'wechat_accounts.json')

DEFAULT_CITY = 'shenzhen'

CITY_NAME_TO_CODE = {
    '深圳': 'shenzhen',
    '广州': 'guangzhou',
    '上海': 'shanghai',
    '北京': 'beijing',
    'shenzhen': 'shenzhen',
    'guangzhou': 'guangzhou',
    'shanghai': 'shanghai',
    'beijing': 'beijing',
}

REAL_SCRAPERS = [
    # 市级核心场馆
    ('深圳图书馆', 'scraper_szlib', 'fetch_szlib_activities'),
    ('南山图书馆', 'scraper_nslib', 'fetch_nslib_activities'),
    ('南山博物馆', 'scraper_nsmuseum', 'fetch_nsmuseum_activities'),
    ('南山区文化馆', 'scraper_nswhg', 'fetch_nswhg_activities'),
    ('南山区青少年活动中心', 'scraper_nsqsng', 'fetch_nsqsng_activities'),
    ('南山文体中心', 'scraper_nswtzx', 'fetch_nswtzx_activities'),
    # 会展中心（API / HTML 解析，数据量大）
    ('深圳会展中心', 'scraper_szcec', 'fetch_szcec_exhibitions'),
    ('深圳国际会展中心', 'scraper_shenzhen_world', 'fetch_shenzhen_world_exhibitions'),
    # 其他有抓取能力的爬虫（即使当前环境可能失败，GitHub Actions 环境可能成功）
    ('宝安图书馆', 'scraper_balib', 'fetch_balib_activities'),
    ('深圳少年儿童图书馆', 'scraper_sz_children_lib', 'fetch_sz_children_lib_activities'),
    ('光明区图书馆', 'scraper_gm_lib', 'fetch_gm_lib_activities'),
    ('光明区科技馆', 'scraper_gm_kjg', 'fetch_gm_kjg_activities'),
    ('盐田区图书馆', 'scraper_yt_lib', 'fetch_yt_lib_activities'),
    ('大鹏地质公园博物馆', 'scraper_dp_geopark', 'fetch_dp_geopark_activities'),
    ('龙岗客家民俗博物馆', 'scraper_lg_hakka', 'fetch_lg_hakka_activities'),
    ('中国版画博物馆', 'scraper_lh_printmaking', 'fetch_lh_printmaking_activities'),
    ('龙华生态文明展览馆', 'scraper_lh_ecology', 'fetch_lh_ecology_activities'),
    ('南山安全教育体验馆', 'scraper_nsaqjy', 'fetch_nsaqjy_activities'),
    ('蛇口海洋科普馆', 'scraper_skhykpg', 'fetch_skhykpg_activities'),
    ('深爱人才馆', 'scraper_sarc', 'fetch_sarc_activities'),
    ('宝安1990文化馆', 'scraper_baoan_1990', 'fetch_baoan_1990_activities'),
    ('华侨城湿地', 'scraper_oct_wetland', 'fetch_oct_wetland_activities'),
    ('深圳自然博物馆', 'scraper_ps_nature', 'fetch_ps_nature_activities'),
    ('大亚湾核能科技馆', 'scraper_dp_nuclear', 'fetch_dp_nuclear_activities'),
    ('南山书房', 'scraper_nssxf', 'fetch_nssxf_activities'),
    ('深圳湾体育中心', 'scraper_szwty', 'fetch_szwty_activities'),
    ('宝安科技馆', 'scraper_baoan_kjg', 'fetch_baoan_kjg_activities'),
    ('宝安体育中心', 'scraper_baoan_ty', 'fetch_baoan_ty_activities'),
    ('深圳市安全教育基地', 'scraper_sz_safety', 'fetch_sz_safety_activities'),
    ('中英街历史博物馆', 'scraper_yt_history', 'fetch_yt_history_activities'),
    ('招商局历史博物馆', 'scraper_zsjbwg', 'fetch_zsjbwg_activities'),
    ('南头古城博物馆群', 'scraper_ntgc', 'fetch_ntgc_activities'),
    ('深圳古生物博物馆', 'scraper_lh_paleo', 'fetch_lh_paleo_activities'),
    ('湾区之眼', 'scraper_bayarea_eye', 'fetch_bayarea_eye_activities'),
]

MANUAL_DATA_FILE = os.path.join(os.path.dirname(__file__), 'manual_data.json')

CATEGORY_KEYWORDS = {
    '展览': ['展', '展览', '博览会', '艺术展', '书画展', '摄影展', '特展', '沉浸展', '推理展', '侨批', '珍品展', '爱丽丝漫游奇境'],
    '讲座阅读': ['讲座', '沙龙', '分享会', '读书', '阅读', '绘本', '故事会', '论坛', '讲', '分享', '签售', '作家', '诗词', '朗诵', '书海探底', '走进图书馆', '参访', '法律', '咨询', '心理', '荟', '悦读', '思辨', '普法', '疗愈', '不被定义', '书法', '合唱', '培训'],
    '科普活动': ['科普', '科学', '实验', '机器人', '编程', '3D打印', 'VR', '创客', '科技', '天文', '探索', 'AI', '科技馆', '博物馆', '延时开放', '夜间开放', '科幻'],
    '演出': ['音乐会', '歌剧', '话剧', '戏曲', '舞蹈', '演唱会', '演出', '音乐剧', '儿童剧', '演奏', '剧场', '音乐赏析', '聆赏', '民乐', '声音舞台', '乐队节', '形体'],
    '体育赛事': ['足球', '篮球', '羽毛球', '乒乓球', '网球', '马拉松', '游泳', '比赛', '赛事', '体育', '运动', '中超', '粤BA'],
    '亲子活动': ['亲子', '儿童', '少儿', '宝宝', '家庭', '手工', '烘焙', '露营', '亲子活动', '儿童剧', '绘本', '故事会', '少年', '暑期', '非遗', '体验', '培育', '提升', '公益', '古典舞'],
    '影视放映': ['电影', '放映', '观影', '她影', '书影', '原声带', '心迷宫', '楚门', '妖猫传', '风暴', '海上花', '美丽新世界', '小说家', '1917', '东方幻境', '照明商店', '侍神令', '沙丘', '明日战纪', '明日之战', '749局', '月球陨落', '流浪地球', '蜘蛛侠'],
}


ALLOWED_FEE_VALUES = {'免费', '免费需预约', '收费', '部分免费', '需购票'}

DISTRICT_MAPPING = {
    '深圳': ['深圳', '市级'],
    '南山': ['南山', '南山区'],
    '宝安': ['宝安', '宝安区'],
    '福田': ['福田', '福田区'],
    '罗湖': ['罗湖', '罗湖区'],
    '龙岗': ['龙岗', '龙岗区'],
    '龙华': ['龙华', '龙华区'],
    '光明': ['光明', '光明区'],
    '坪山': ['坪山', '坪山区'],
    '盐田': ['盐田', '盐田区'],
    '大鹏': ['大鹏', '大鹏新区'],
}


def get_district_from_text(text):
    if not text:
        return None
    specific_districts = ['南山', '宝安', '福田', '罗湖', '龙岗', '龙华', '光明', '坪山', '盐田', '大鹏']
    for district in specific_districts:
        if district in text:
            return district
    if '深圳' in text:
        return '深圳'
    return None


def fix_description(title, description, venue, category, fee):
    if len(description) >= 10:
        return description
    
    parts = []
    if category:
        parts.append(f"{category}活动")
    if venue:
        parts.append(f"在{venue}举行")
    if title:
        parts.append(f"详情请关注官方信息")
    
    if fee and fee in ALLOWED_FEE_VALUES:
        if fee == '免费':
            parts.insert(0, "免费参与")
        elif fee == '免费需预约':
            parts.insert(0, "免费需预约")
        elif fee == '收费':
            parts.insert(0, "收费活动")
        elif fee == '部分免费':
            parts.insert(0, "部分免费")
        elif fee == '需购票':
            parts.insert(0, "需购票")
    
    result = '，'.join(parts)
    if len(result) < 10:
        result = f"{title}，{venue}举办的活动，欢迎参与。"
    
    return result[:300]


def normalize_activity(raw, venue_default='', city=DEFAULT_CITY):
    title = raw.get('title') or raw.get('name') or ''
    link = raw.get('link') or raw.get('url') or ''
    venue = raw.get('venue') or venue_default
    start_date = raw.get('start_date') or ''
    end_date = raw.get('end_date') or start_date
    description = raw.get('description') or ''
    fee = raw.get('fee') or '免费'
    contact = raw.get('contact') or ''
    family_friendly = raw.get('family_friendly', False)
    source = raw.get('source') or ''
    city_val = raw.get('city') or city
    city_val = CITY_NAME_TO_CODE.get(city_val, city_val)

    if not title or not start_date:
        return None

    category = categorize_activity(title, description)

    if not description or len(description) < 10:
        description = f"{title}。{venue}举办。"
        if fee and fee != '免费':
            description += f"{fee}。"

    if not family_friendly:
        family_friendly = is_family_friendly(title, description, category)

    if fee not in ALLOWED_FEE_VALUES:
        fee = '免费'

    venue_district = get_district_from_text(venue)
    source_district = get_district_from_text(source)
    
    if source and venue_district and source_district and venue_district != source_district:
        city_sources = ['深圳文旅游局', '深圳政府在线', '深圳新闻网', '深圳融媒体中心', '深圳商报', '深圳晚报', '深圳卫视', '深圳广播', '深圳发布']
        if source in city_sources or (source_district == '深圳' and venue_district != '深圳'):
            pass
        else:
            source_map = {
                'nsqsng': '南山区青少年活动中心',
                'nswtzx': '南山文体中心',
                'nslib': '南山图书馆',
                'nsmuseum': '南山博物馆',
                'nswhg': '南山区文化馆',
                'balib': '宝安图书馆',
                'szlib': '深圳图书馆',
                'gm_lib': '光明区图书馆',
                'gm_kjg': '光明区科技馆',
                'yt_lib': '盐田区图书馆',
                'dp_geopark': '大鹏地质公园博物馆',
                'lg_hakka': '龙岗客家民俗博物馆',
                'lh_printmaking': '中国版画博物馆',
                'lh_ecology': '龙华生态文明展览馆',
                'nsaqjy': '南山安全教育体验馆',
                'skhykpg': '蛇口海洋科普馆',
                'sarc': '深爱人才馆',
                'baoan_1990': '宝安1990文化馆',
                'oct_wetland': '华侨城湿地',
                'ps_nature': '深圳自然博物馆',
                'dp_nuclear': '大亚湾核能科技馆',
                'nssxf': '南山书房',
                'szwty': '深圳湾体育中心',
                'baoan_kjg': '宝安科技馆',
                'baoan_ty': '宝安体育中心',
                'sz_safety': '深圳市安全教育基地',
                'yt_history': '中英街历史博物馆',
                'zsjbwg': '招商局历史博物馆',
                'ntgc': '南头古城博物馆群',
                'lh_paleo': '深圳古生物博物馆',
                'bayarea_eye': '湾区之眼',
                'sz_children_lib': '深圳少年儿童图书馆',
            }
            if source in source_map:
                source = source_map[source]

    description = fix_description(title, description, venue, category, fee)

    result = {
        'title': title,
        'name': title,
        'venue': venue,
        'city': city_val,
        'start_date': start_date,
        'end_date': end_date,
        'link': link,
        'url': link,
        'description': description,
        'category': category,
        'fee': fee,
        'contact': contact,
        'family_friendly': family_friendly,
        'source': source,
    }

    if 'types' in raw:
        result['types'] = raw['types']

    return result


def categorize_activity(title, description):
    text = title + description
    scores = {}
    for cat, keywords in CATEGORY_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in text)
        if score > 0:
            scores[cat] = score
    if scores:
        return max(scores, key=scores.get)
    return '其他'


def is_family_friendly(title, description, category):
    text = title + description
    parent_child_kw = ['亲子', '儿童', '少儿', '宝宝', '家庭', '绘本', '故事会', '手工',
                       '科普', '科学实验', '创客', '编程', '3D打印', '机器人',
                       '儿童剧', '亲子活动', '亲子阅读', '亲子手工']
    if any(kw in text for kw in parent_child_kw):
        return True
    if category in ['科普活动', '亲子活动']:
        return True
    return False


def is_valid_activity(activity):
    if not activity or not activity.get('title'):
        return False
    if not activity.get('start_date'):
        return False
    today = datetime.now().strftime('%Y-%m-%d')
    end_date = activity.get('end_date') or activity.get('start_date')
    if end_date < today:
        return False
    return True


def load_manual_data():
    if not os.path.exists(MANUAL_DATA_FILE):
        return []
    try:
        with open(MANUAL_DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"加载手动数据失败: {e}")
        return []


def fetch_wechat_activities(max_accounts=10, max_articles_per_account=5):
    try:
        from wechat_crawler import crawl_wechat_articles
        from ai_analyzer import analyze_articles
    except ImportError:
        print("  微信爬虫模块未安装，跳过")
        return []

    if not os.path.exists(WECHAT_ACCOUNTS_FILE):
        print("  公众号配置文件不存在")
        return []

    try:
        with open(WECHAT_ACCOUNTS_FILE, 'r', encoding='utf-8') as f:
            accounts_config = json.load(f)
    except Exception as e:
        print(f"  加载公众号配置失败: {e}")
        return []

    all_accounts = []
    for category, accounts in accounts_config.items():
        all_accounts.extend(accounts)

    selected_accounts = all_accounts[:max_accounts]
    account_names = [acc['account'] for acc in selected_accounts]

    print(f"  爬取 {len(account_names)} 个公众号...")
    articles = crawl_wechat_articles(account_names, max_articles_per_account=max_articles_per_account)
    print(f"  获取到 {len(articles)} 篇文章")

    print("  分析文章内容...")
    api_key = os.environ.get('OPENAI_API_KEY') or os.environ.get('ANTHROPIC_API_KEY')
    activities = analyze_articles(articles, api_key=api_key, use_llm=bool(api_key))
    print(f"  提取到 {len(activities)} 个活动")

    return activities


def collect_all_activities():
    all_activities = []

    print("=== 抓取真实场馆数据 ===\n")

    for i, (name, module_name, func_name) in enumerate(REAL_SCRAPERS, 1):
        print(f"{i}. 抓取{name}...")
        try:
            mod = __import__(module_name)
            func = getattr(mod, func_name)
            results = func()
            normalized = []
            for raw in results:
                activity = normalize_activity(raw, venue_default=name)
                if activity and is_valid_activity(activity):
                    normalized.append(activity)
            print(f"   有效活动: {len(normalized)} 条")
            all_activities.extend(normalized)
        except Exception as e:
            print(f"   [失败] {e}")

    print("\n=== 加载手动整理数据 ===")
    manual_data = load_manual_data()
    manual_valid = []
    for raw in manual_data:
        activity = normalize_activity(raw)
        if activity and is_valid_activity(activity):
            manual_valid.append(activity)
    print(f"有效活动: {len(manual_valid)} 条")
    all_activities.extend(manual_valid)

    print("\n=== 抓取微信公众号数据 ===")
    wechat_data = fetch_wechat_activities(max_accounts=10, max_articles_per_account=3)
    wechat_valid = []
    for raw in wechat_data:
        activity = normalize_activity(raw)
        if activity and is_valid_activity(activity):
            wechat_valid.append(activity)
    print(f"有效活动: {len(wechat_valid)} 条")
    all_activities.extend(wechat_valid)

    all_activities.sort(key=lambda x: x['start_date'])

    has_link = sum(1 for a in all_activities if a.get('link'))
    print(f"\n=== 汇总: 共 {len(all_activities)} 条有效活动，其中 {has_link} 条有官方来源 ===")

    by_category = {}
    for a in all_activities:
        cat = a['category']
        by_category[cat] = by_category.get(cat, 0) + 1
    print("按分类统计:")
    for cat, count in sorted(by_category.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}条")

    by_venue = {}
    for a in all_activities:
        v = a['venue']
        by_venue[v] = by_venue.get(v, 0) + 1
    print("\n按场馆统计 (TOP10):")
    for v, count in sorted(by_venue.items(), key=lambda x: -x[1])[:10]:
        print(f"  {v}: {count}条")

    return all_activities


def main():
    activities = collect_all_activities()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    json_path = os.path.join(OUTPUT_DIR, JSON_FILE)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)
    print(f"\nJSON数据已保存到 {json_path}")

    ics_content = create_ics(activities)
    ics_path = os.path.join(OUTPUT_DIR, ICS_FILE)
    with open(ics_path, 'w', encoding='utf-8') as f:
        f.write(ics_content)
    print(f"ICS日历已生成到 {ics_path}")

    city_codes = ['shenzhen', 'guangzhou', 'shanghai', 'beijing']
    for city_code in city_codes:
        city_activities = [a for a in activities if a.get('city') == city_code]
        if not city_activities:
            continue

        city_json_path = os.path.join(OUTPUT_DIR, f'exhibitions_{city_code}.json')
        with open(city_json_path, 'w', encoding='utf-8') as f:
            json.dump(city_activities, f, ensure_ascii=False, indent=2)
        print(f"  [{city_code}] JSON: {len(city_activities)} 条 -> {city_json_path}")

        city_ics = create_ics(city_activities)
        city_ics_path = os.path.join(OUTPUT_DIR, f'exhibitions_{city_code}.ics')
        with open(city_ics_path, 'w', encoding='utf-8') as f:
            f.write(city_ics)
        print(f"  [{city_code}] ICS -> {city_ics_path}")

    try:
        generate_rss()
        print("RSS订阅已生成")
    except Exception as e:
        print(f"RSS生成失败: {e}")

    print("\n=== 完成 ===")


if __name__ == "__main__":
    main()
