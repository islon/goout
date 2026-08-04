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

REAL_SCRAPERS = [
    # 市级核心场馆
    ('深圳图书馆', 'scraper_szlib', 'fetch_szlib_activities'),
    ('南山图书馆', 'scraper_nslib', 'fetch_nslib_activities'),
    ('南山博物馆', 'scraper_nsmuseum', 'fetch_nsmuseum_activities'),
    ('南山区文化馆', 'scraper_nswhg', 'fetch_nswhg_activities'),
    ('南山区青少年活动中心', 'scraper_nsqsng', 'fetch_nsqsng_activities'),
    ('南山文体中心', 'scraper_nswtzx', 'fetch_nswtzx_activities'),
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

# ========== 数据质量标准 ==========
# fee 白名单
_ALLOWED_FEE = {"免费", "免费需预约", "收费", "部分免费", "需购票"}
# fee 同义词 -> 标准值映射
_FEE_ALIASES = {
    '免费入场': '免费', '免票': '免费', '免预约': '免费', '公益': '免费',
    '凭票入场': '需购票', '购票入场': '需购票', '售票': '需购票', '买票': '需购票',
    '部分收费': '部分免费', '部分免票': '部分免费', '预约': '免费需预约',
    '预约免费': '免费需预约', '免费预约': '免费需预约', '需预约': '免费需预约',
    '收费预约': '收费', '付费': '收费',
}

# 区县关键词表（用于判断 source/venue 的行政区归属）
_DISTRICT_KEYWORDS = {
    '南山': ['南山', '南山区', 'nslib', 'nsmuseum', 'nswhg', 'nsqsng', 'nswtzx', 'nsaqjy', 'skhykpg', 'sarc', 'oct_wetland', 'ntgc', 'zsjbwg', 'nssxf', 'szwty', 'szns', '南头古城', '招商局', '蛇口', '桃源街道', '粤海', '西丽'],
    '宝安': ['宝安', '宝安区', 'balib', 'baoan', 'bamuseum', 'baoan_1990', 'baoan_kjg', 'baoan_ty', 'baoan_qsng', 'bayarea_eye', 'bawt', 'shenzhen_world', '深圳国际会展中心', '新桥街道'],
    '福田': ['福田', 'futian', 'ftlib', 'szlib', 'szbwg', '深圳博物馆', 'szstm', '深圳科学技术馆官网', 'szcp', 'szaac', 'sznm', 'szbo', 'szconcert', '深圳音乐厅', 'szmocap', 'szsports', 'szmassart', 'sz_children_lib', 'sz_safety', 'szcec', '深圳会展中心'],
    '罗湖': ['罗湖', 'luohu', 'lhlib', '罗湖区图书馆', 'lh_paleo', '深圳古生物博物馆', 'lhqsng2', '罗湖区青少年活动中心', 'lhtyzx2', '罗湖区体育中心', 'lhmuseum2', '罗湖区博物馆'],
    '龙岗': ['龙岗', 'longgang', 'lglib', '龙岗区图书馆', 'lgmuseum', 'lgkjg', '龙岗区科技馆', 'lgqsng', '龙岗区青少年宫', 'lhtyzx', '龙岗体育中心', 'lg_hakka', '龙岗客家民俗博物馆', 'lgguihua', '龙城街道', '坪地街道', '吉华街道'],
    '龙华': ['龙华', '龙华区', 'lhxqlib', '龙华区图书馆', 'lhmuseum', '龙华区博物馆', 'lhkjg', '龙华区科技馆', 'lhqsng', '龙华区青少年宫', 'lhwtzx', '龙华文体中心', 'lh_printmaking', '中国版画博物馆', 'lh_ecology', '龙华生态文明展览馆'],
    '光明': ['光明', 'guangming', 'gmlib', '光明区图书馆', 'gm_kjg', 'gmqsng', '光明区青少年活动中心', 'gmtyzx', '光明区群众体育中心', '光明新馆', 'gm_lib'],
    '坪山': ['坪山', 'pingshan', 'pslib', '坪山区图书馆', 'psqsng', '坪山区青少年宫', 'pstyzx', '坪山体育中心', 'ps_nature'],
    '盐田': ['盐田', 'yantian', 'ytlib', '盐田区图书馆', 'ytkjg', '盐田区科技馆', 'yttyzx', '盐田体育中心', 'yt_history', '中英街历史博物馆'],
    '大鹏': ['大鹏', 'dapeng', 'dplib', '大鹏新区图书馆', 'dpgeopark', '大鹏半岛国家地质公园博物馆', 'dp_geopark', 'dp_nuclear', '大亚湾核能科技馆'],
}

# source 标识 -> 区县 映射（更精准）
_SOURCE_DISTRICT = {
    'nslib': '南山', '南山图书馆': '南山',
    'nsmuseum': '南山', '南山博物馆': '南山',
    'nswhg': '南山', '南山区文化馆': '南山',
    'nsqsng': '南山', '南山区青少年活动中心': '南山',
    'nswtzx': '南山', '南山文体中心': '南山',
    'nsaqjy': '南山', '南山安全教育体验馆': '南山',
    'skhykpg': '南山', '蛇口海洋科普馆': '南山',
    'sarc': '南山', '深爱人才馆': '南山',
    'oct_wetland': '南山', '华侨城湿地': '南山',
    'ntgc': '南山', '南头古城博物馆群': '南山',
    'zsjbwg': '南山', '招商局历史博物馆': '南山',
    'nssxf': '南山', '南山书房': '南山',
    'szwty': '南山', '深圳湾体育中心': '南山',
    'balib': '宝安', '宝安图书馆': '宝安',
    'baoan_1990': '宝安', '宝安1990文化馆': '宝安',
    'baoan_kjg': '宝安', '宝安科技馆': '宝安',
    'baoan_ty': '宝安', '宝安体育中心': '宝安',
    'gm_kjg': '光明', '深圳科学技术馆（光明新馆）': '光明',
    'szcec': '福田', '深圳会展中心': '福田',
    'shenzhen_world': '宝安', '深圳国际会展中心': '宝安',
    'szlib': '福田', '深圳图书馆': '福田',
    'sz_children_lib': '福田', '深圳少年儿童图书馆': '福田',
    'gm_lib': '光明', '光明区少年儿童图书馆': '光明',
    'yt_lib': '盐田', '盐田区图书馆': '盐田',
    'dp_geopark': '大鹏', '大鹏半岛国家地质公园博物馆': '大鹏',
    'lg_hakka': '龙岗', '龙岗客家民俗博物馆': '龙岗',
    'lh_printmaking': '龙华', '中国版画博物馆': '龙华',
    'lh_ecology': '龙华', '龙华生态文明展览馆': '龙华',
    'dp_nuclear': '大鹏', '大亚湾核能科技馆': '大鹏',
    'ps_nature': '坪山', '深圳自然博物馆坪山馆': '坪山',
    'sz_safety': '福田', '深圳市安全教育基地': '福田',
    'yt_history': '盐田', '中英街历史博物馆': '盐田',
    'lh_paleo': '罗湖', '深圳古生物博物馆': '罗湖',
    'bayarea_eye': '宝安', '湾区之眼': '宝安',
}


def _get_district(text):
    """推断字符串(venue/source)属于哪个区县，返回 None 表示未知"""
    if not text:
        return None
    t = str(text)
    # 最高优先级：显式 [区县] 前缀（由 normalize_activity 校正时写入）
    import re
    m = re.match(r'^\[([^\]]{2,4})\]', t)
    if m:
        prefix = m.group(1)
        if prefix in _DISTRICT_KEYWORDS:
            return prefix
    t_low = t.lower()
    t_str = t
    if t_low in _SOURCE_DISTRICT:
        return _SOURCE_DISTRICT[t_low]
    if t_str in _SOURCE_DISTRICT:
        return _SOURCE_DISTRICT[t_str]
    for dist, keywords in sorted(_DISTRICT_KEYWORDS.items(), key=lambda kv: -sum(len(k) for k in kv[1])):
        for kw in keywords:
            if kw.lower() in t_low or kw in t_str:
                return dist
    return None


def normalize_activity(raw, venue_default=''):
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

    if not title or not start_date:
        return None

    # ========== 数据质量标准化 ==========
    # 1. fee 标准化到白名单
    fee_stripped = str(fee).strip()
    if fee_stripped not in _ALLOWED_FEE:
        # 先查别名表
        fee_lower = fee_stripped
        matched = None
        for alias, std in sorted(_FEE_ALIASES.items(), key=lambda kv: -len(kv[0])):
            if alias in fee_lower:
                matched = std
                break
        if not matched:
            # 启发式判断
            if any(k in fee_stripped for k in ['收费', '购票', '买票', '付费', '票价', '元']):
                matched = '收费'
            elif any(k in fee_stripped for k in ['免费']) and any(k in fee_stripped for k in ['预约', '需预约']):
                matched = '免费需预约'
            elif any(k in fee_stripped for k in ['免费', '免票', '免', '公益']):
                matched = '免费'
            elif any(k in fee_stripped for k in ['部分']):
                matched = '部分免费'
            else:
                matched = '免费'  # 缺省免费
        fee = matched

    # 2. description 不少于 10 字
    description = str(description).strip()
    if len(description) < 10:
        suffix = f"{title}。详情请访问官方链接了解更多信息。"
        if description:
            description = description + '。' + suffix
        else:
            description = suffix
        if len(description) > 500:
            description = description[:500]

    # 3. source 与 venue 区县对齐
    # 取 venue 区县作为主锚点（场馆实际所在地更可靠）
    dist_venue = _get_district(venue)
    dist_source = _get_district(source)
    if dist_venue and dist_source and dist_venue != dist_source:
        # 以 venue 所在区县为准，修正 source（保持原 source 文本，但不强改 key，
        # 而是在 source 前补 [区县] 标识，保证区县信息可被重新识别）
        if not source.startswith('['):
            source = f"[{dist_venue}]" + (source if source else dist_venue)

    category = categorize_activity(title, description)

    if not family_friendly:
        family_friendly = is_family_friendly(title, description, category)

    result = {
        'title': title,
        'name': title,
        'venue': venue,
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

    try:
        generate_rss()
        print("RSS订阅已生成")
    except Exception as e:
        print(f"RSS生成失败: {e}")

    print("\n=== 完成 ===")


if __name__ == "__main__":
    main()
