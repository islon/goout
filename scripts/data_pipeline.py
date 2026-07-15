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
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import OUTPUT_DIR, JSON_FILE, ICS_FILE
from ics_generator import create_ics
from rss_generator import generate_rss
from venue_registry import get_district as registry_get_district
from venue_registry import resolve_source_code, lookup_venue_by_name, get_venue_type
from venue_registry import generate_venue_info_json

WECHAT_ACCOUNTS_FILE = os.path.join(os.path.dirname(__file__), 'wechat_accounts.json')

DEFAULT_CITY = 'shenzhen'

CITY_NAME_TO_CODE = {
    '深圳': 'shenzhen',
    '广州': 'guangzhou',
    '上海': 'shanghai',
    '北京': 'beijing',
    '杭州': 'hangzhou',
    'shenzhen': 'shenzhen',
    'guangzhou': 'guangzhou',
    'shanghai': 'shanghai',
    'beijing': 'beijing',
    'hangzhou': 'hangzhou',
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

VALID_FEE_VALUES = {'免费', '免费需预约', '收费', '部分免费', '需购票'}

DISTRICT_KEYWORDS = {
    '南山': ['南山', 'nanshan', 'ns', '蛇口', '南头', '沙河', '粤海', '招商', '桃源', '西丽', 'nsmuseum', 'nslib', 'nswtzx', 'nswhg', 'nsaqjy', 'skhykpg', 'nsqsng', 'nssxf', 'ntgc', 'zsjbwg', 'sarc', 'oct_wetland', 'szwt', 'shenzhen_world', 'sz_children_lib', 'szmuseum', 'szlib'],
    '福田': ['福田', 'futian', 'ft', '华强', '莲花', '园岭', '南园', '沙头', '梅林', '华富', '香蜜湖', '福保'],
    '罗湖': ['罗湖', 'luohu', 'lh', '东门', '翠竹', '南湖', '黄贝', '桂园', '笋岗', '清水河', '莲塘', '东湖', 'lh_paleo'],
    '宝安': ['宝安', 'baoan', 'ba', '新安', '西乡', '福永', '沙井', '松岗', '石岩', 'balib', 'baoan_1990', 'baoan_kjg', 'baoan_ty', 'bayarea_eye'],
    '龙岗': ['龙岗', 'longgang', 'lg', '龙城', '龙岗街道', '坂田', '布吉', '南湾', '平湖', '横岗', '坪地', '吉华', '园山', '宝龙', 'lg_hakka', 'lgmuseum'],
    '龙华': ['龙华', 'longhua', 'lhx', '龙华街道', '民治', '大浪', '观澜', '福城', '观湖', 'lh_ecology', 'lh_printmaking', 'lhmuseum'],
    '光明': ['光明', 'guangming', 'gm', '光明街道', '公明', '新湖', '凤凰', '玉塘', '马田', '光明文化艺术中心', 'gm_lib', 'gm_kjg', 'gmqsng', 'gmtyzx'],
    '坪山': ['坪山', 'pingshan', 'ps', '坪山街道', '坑梓', '龙田', '石井', '马峦', '碧岭', 'ps_nature', 'pslib', 'psqsng', 'pstyzx'],
    '盐田': ['盐田', 'yantian', 'yt', '沙头角', '海山', '盐田街道', '梅沙', '中英街', 'yt_history', 'yt_lib', 'yttyzx'],
    '大鹏': ['大鹏', 'dapeng', 'dp', '葵涌', '大鹏街道', '南澳', '大亚湾', '地质公园', 'dp_geopark', 'dp_nuclear'],
    # 广州
    '天河区': ['天河', '珠江新城', '广东省博物馆', '广州大剧院', '星海音乐厅', '广东科学中心', '广东省文化馆', '广州市少年宫', '广州市儿童公园', '华南植物园', '正佳极地', '广州图书馆东馆', '广州文化馆', '广州青少年科技馆', '广东美术馆', '广州市文化馆', '广州图书馆', '中国科学院华南植物园', '正佳大剧院', '正佳极地海洋世界'],
    '越秀区': ['越秀', '东山', '麓湖', '镇海楼', '南越王', '广州艺术博物院', '广东美术馆二沙', '广州博物馆', '农讲所', '中山纪念堂', '广东省立中山图书馆', '孙中山大元帅府', '广州动物园', '广州海洋馆', '广州图书馆总馆', '中山图书馆', '广东革命历史博物馆', '广州少年儿童图书馆', '南越王博物院', '农讲所纪念馆'],
    '荔湾区': ['荔湾', '永庆坊', '恩宁路', '陈家祠', '沙面', '上下九', '荔湾博物馆', '西关', '广东民间工艺博物馆'],
    '海珠区': ['海珠', '琶洲', '阅江', '广州塔', '中山大学', '海珠湿地', '广东美术馆新馆', '广州市文化馆新馆', '广州地铁博物馆', '广州艺术博物院'],
    '白云区': ['白云', '白云山', '白云机场', '白云国际会议中心'],
    '番禺区': ['番禺', '大学城', '长隆', '南汉二陵', '余荫山房', '番禺博物馆', '长隆旅游度假区', '南汉二陵博物馆', '广东科学中心'],
    '黄埔区': ['黄埔', '萝岗', '黄埔军校', '南海神庙', '香雪公园', '黄埔区图书馆', '黄埔军校旧址纪念馆'],
    '花都区': ['花都', '花都湖'],
    '南沙区': ['南沙', '天后宫', '百万葵园', '南沙湿地'],
    '从化区': ['从化', '温泉'],
    '增城区': ['增城'],
    # 上海
    '黄浦区': ['黄浦', '人民广场', '南京路', '外滩', '豫园', '原法租界', '复兴中路', '上海大世界', '大世界', '上海图书馆', '上海市少年宫', '上海博物馆', '中共一大纪念馆', '上海当代艺术博物馆', '上海文化广场', '捷豹上海交响音乐厅', '上海市历史博物馆'],
    '浦东新区': ['浦东', '临港', '世纪大道', '上南路', '国展路', '张江', '前滩', '世博', '浦东美术馆', '中华艺术宫', '上海天文馆', '上海科技馆', '上海海昌', '上海迪士尼', '上海迪士尼度假区', '上海中心大厦', '陆家嘴', '东方明珠', '野生动物园', '金桥', '川沙', '上海海洋水族馆', '上海世博会博物馆', '上海美术馆', '上海海昌海洋公园', '浦东美术馆'],
    '徐汇区': ['徐汇', '衡山路', '西岸', '徐家汇', '武康路', '上海图书馆总馆', '上海图书馆东馆', '徐汇区图书馆', '上海植物园', '上海图书馆'],
    '静安区': ['静安', '北京西路', '南京西路', '静安寺', '上海自然博物馆', '上海博物馆', '上海少年儿童图书馆', '上海展览中心', '上海儿童博物馆', '上海展览中心', '上海铁路博物馆'],
    '长宁区': ['长宁', '中山公园', '虹桥', '上海动物园'],
    '虹口区': ['虹口', '东大名路', '北外滩', '鲁迅公园'],
    '普陀区': ['普陀', '长风', '真如', '曹杨', '普陀青少年水主题', '上海消防博物馆', '乐高探索中心'],
    '杨浦区': ['杨浦', '五角场', '杨浦区图书馆', '世界技能博物馆'],
    '宝山区': ['宝山', '顾村', '上海玻璃博物馆', '宝山区图书馆'],
    '闵行区': ['闵行', '七宝', '莘庄', '闵行区图书馆'],
    '嘉定区': ['嘉定', '嘉定图书馆'],
    '金山区': ['金山', '枫泾', '乐高', '金山城市沙滩', '上海乐高乐园'],
    '松江区': ['松江', '佘山', '广富林', '方塔园'],
    '青浦区': ['青浦', '朱家角', '淀山湖'],
    '奉贤区': ['奉贤', '海湾'],
    # 北京
    '东城区': ['东城', '东长安街', '王府井', '天坛', '故宫', '景山', '前门', '国子监', '雍和宫', '南锣鼓巷', '首都剧场', '中国国家博物馆', '中国美术馆', '国家自然博物馆', '北京古观象台', '明城墙遗址', '钟鼓楼', '中国考古博物馆', '中国妇女儿童博物馆', '故宫博物院', '天坛公园', '中山公园音乐堂', '北京规划展览馆', '北京古代建筑博物馆', '北京市少年宫', '北京自然博物馆', '北京鲁迅博物馆', '京报网'],
    '西城区': ['西城', '西长安街', '西直门', '复兴门外', '广安门外', '什刹海', '北海', '国家大剧院', '国家话剧院', '北京天文馆', '北京科学中心', '首都博物馆', '北京展览馆', '中国地质博物馆', '北京动物园', '北京海洋馆', '北京宋庆龄故居', '恭王府', '梅兰芳大剧院', '北京鲁迅博物馆', '北京艺术博物馆', '万寿寺', '北海公园', '国家大剧院', '北京旅游网'],
    '朝阳区': ['朝阳', '北辰', '国贸', '三里屯', '奥运', '798', '中国科技馆', '国家体育场', '奥林匹克公园', '朝阳公园', '欢乐谷', '朝阳大悦城', '红砖美术馆', '北京民生现代美术馆', '炎黄艺术馆', '首都图书馆', '鸿博公园', '中国电影博物馆', '北京欢乐谷', '首都图书馆', '奥林匹克森林公园', '大望京公园', '太阳宫市民活动中心', '亮马河滨水步道', '老君堂公园', '马家湾湿地公园', '温榆河公园', '北京市文化馆', '北京数字文化馆', '新华网'],
    '海淀区': ['海淀', '复兴路', '中关村', '颐和园', '圆明园', '香山', '北京大学', '清华大学', '玉渊潭', '国家图书馆', '中国人民革命军事博物馆', '北京植物园', '北京石刻艺术博物馆', '大钟寺', '五塔寺', '紫竹院', '海淀公园', '中国古动物馆', '清华大学艺术博物馆', '三山五园文化艺术中心', '中华世纪坛', '北京艺术博物馆', '万寿寺', '北京市青少年活动中心'],
    '丰台区': ['丰台', '宛平', '园博园', '世界公园', '北京汽车博物馆', '中国园林博物馆', '北京花乡', '南苑', '中国消防博物馆', '北京消防科普教育基地'],
    '石景山区': ['石景山', '首钢', '八大处', '北京国际雕塑公园', '永定河休闲森林公园', '莲石湖公园'],
    '通州区': ['通州', '绿心', '大运河', '通州运河', '宋庄', '环球影城', '北京环球度假区', '西海子公园', '北京大运河博物馆'],
    '大兴区': ['大兴', '南海子', '大兴机场', '北京野生动物园', '呀路古', '念坛公园', '亦庄滨河森林公园'],
    '房山区': ['房山', '周口店', '云居寺', '十渡', '石花洞', '云居城市休闲公园', '长沟湿地公园'],
    '昌平区': ['昌平', '明十三陵', '居庸关', '银山塔林', '昌平新城滨河', '东小口森林公园'],
    '门头沟区': ['门头沟', '潭柘寺', '戒台寺', '妙峰山'],
    '顺义区': ['顺义', '国际鲜花港', '顺义奥林匹克水上公园', '潮白河森林公园'],
    # 杭州
    '西湖区': ['西湖', '孤山', '龙井', '灵隐', '西溪湿地', '浙江大学', '杭州植物园', '浙江图书馆', '浙江省文化馆', '浙江省科技馆', '浙江自然博物院', '中国丝绸博物馆', '浙江省博物馆孤山', '西湖文化广场', '浙江美术馆', '中国印学博物馆', '杭州动物园', '中国湿地博物馆', '中国茶叶博物馆', '天目里', '杭州宋城', '浙江省博物馆', '杭州图书馆'],
    '上城区': ['上城', '南宋御街', '河坊街', '杭州博物馆', '中国财税博物馆', '杭州孔庙', '中国杭帮菜博物馆', '杭州图书馆少儿分馆'],
    '下城区': ['下城', '浙江展览馆'],
    '拱墅区': ['拱墅', '大运河', '小河直街', '中国刀剪剑博物馆', '中国扇博物馆', '中国伞博物馆', '杭州工艺美术博物馆', '京杭大运河博物馆', '杭州运河大剧院', '浙江交响乐团', '中国京杭大运河博物馆'],
    '江干区': ['江干', '钱江新城', '杭州国际博览中心', '杭州图书馆'],
    '滨江区': ['滨江', '西兴', '白马湖', '中国动漫博物馆'],
    '萧山区': ['萧山', '跨湖桥遗址博物馆', '浙江省现代陶瓷艺术博物馆'],
    '余杭区': ['余杭', '良渚', '径山', '良渚博物院', '国家版本馆', '余杭区图书馆', '良渚古城遗址公园'],
    '富阳区': ['富阳', '富阳博物馆', '黄公望隐居地'],
    '临安区': ['临安', '天目山', '临安博物馆', '大明山'],
    '桐庐县': ['桐庐', '桐庐博物馆'],
    '淳安县': ['淳安', '千岛湖'],
    '建德市': ['建德', '新安江'],
}


def get_district(text):
    if not text:
        return None
    text_lower = text.lower()
    for dist, keywords in DISTRICT_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in text_lower:
                return dist
    return None


def normalize_fee(fee):
    if not fee:
        return '免费'
    fee = fee.strip()
    if fee in VALID_FEE_VALUES:
        return fee
    fee_lower = fee.lower()
    if '免费' in fee and '预约' in fee:
        return '免费需预约'
    if '免费' in fee:
        return '免费'
    if '收费' in fee or '票' in fee or '元' in fee:
        if '需购票' in fee or '购票' in fee:
            return '需购票'
        return '收费'
    if '部分' in fee:
        return '部分免费'
    return '免费'


def validate_and_fix_activity(activity):
    if not activity:
        return None
    fee = activity.get('fee', '免费')
    activity['fee'] = normalize_fee(fee)
    description = activity.get('description', '')
    title = activity.get('title', '')
    if len(description) < 10:
        if description:
            activity['description'] = f"{title}，{description}。详情请以官方信息为准。"
        else:
            activity['description'] = f"{title}活动，详情请以官方信息为准。"
    if len(activity['description']) > 500:
        activity['description'] = activity['description'][:500]
    source = activity.get('source', '')
    venue = activity.get('venue', '')
    source_dist = get_district(source)
    venue_dist = get_district(venue)
    if source_dist and venue_dist and source_dist != venue_dist:
        if venue_dist:
            pass
    return activity

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
    """从任意文本中匹配区县关键词（支持深圳、广州、上海、北京、杭州）"""
    if not text:
        return None
    for district, keywords in DISTRICT_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
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
    fee_raw = raw.get('fee') or ''
    contact = raw.get('contact') or ''
    family_friendly = raw.get('family_friendly', False)
    source = raw.get('source') or ''
    city_val = raw.get('city') or city
    city_val = CITY_NAME_TO_CODE.get(city_val, city_val)

    if not title or not start_date:
        return None

    # 保留原始 category（如已指定），否则自动分类
    raw_category = raw.get('category') or ''
    if raw_category and raw_category in {'展览', '讲座阅读', '科普活动', '演出', '体育赛事', '亲子活动', '影视放映', '其他', '户外活动'}:
        category = raw_category if raw_category != '户外活动' else '其他'
    else:
        category = categorize_activity(title, description)

    fee = standardize_fee(fee_raw, title, description)

    if not description or len(description) < 10:
        description = f"{title}。{venue}举办。"
        if fee and fee != '免费':
            description += f"{fee}。"

    if not family_friendly:
        family_friendly = is_family_friendly(title, description, category)

    if fee not in ALLOWED_FEE_VALUES:
        fee = '免费'

    # === 从 venue_registry 注入 district 和 venue_type ===
    # 优先保留原始数据中已有的 district（manual_data 等可信来源）
    raw_district = raw.get('district', '')
    if raw_district:
        district = raw_district
    else:
        # 尝试解析标准 source_code
        resolved_code = resolve_source_code(source, venue)
        if resolved_code:
            source = resolved_code
        # 查区县（优先 registry，兜底关键词）
        district = registry_get_district(source, venue)
        if not district or district == '深圳':
            # 用 venue 文本兜底
            venue_dist = get_district_from_text(venue)
            if venue_dist and venue_dist != '深圳':
                district = venue_dist
            elif not district:
                district = get_district_from_text(source) or ''
    # 查场馆类型
    venue_type = get_venue_type(source, venue)

    description = fix_description(title, description, venue, category, fee)

    result = {
        'title': title,
        'venue': venue,
        'city': city_val,
        'district': district or '',
        'venue_type': venue_type,
        'start_date': start_date,
        'end_date': end_date,
        'link': link,
        'description': description,
        'category': category,
        'fee': fee,
        'contact': contact,
        'family_friendly': family_friendly,
        'source': source,
    }

    if 'types' in raw:
        result['types'] = raw['types']

    result = validate_and_fix_activity(result)

    return result


VALID_FEE_TYPES = {'免费', '免费需预约', '收费', '部分免费', '需购票'}

FREE_KEYWORDS = ['免费', '公益', '免门票', '免票', '不要钱', '无需费用', '无费用']
FREE_RESERVATION_KEYWORDS = ['免费需预约', '免费预约', '预约入馆', '提前预约', '预约免费', '免费但需预约', '需预约']
CHARGE_KEYWORDS = ['收费', '元', '票价', '门票', '购票', '单人票', '双人票', '亲子票', '学生票', '半价', '早鸟', 'vip', 'VIP', '￥', '¥', '$', 'dollar', '含在门票内']
PARTIAL_FREE_KEYWORDS = ['部分免费', '部分收费', '有的免费', '有免费有收费', '部分项目免费', '部分活动免费']
TICKET_REQUIRED_KEYWORDS = ['需购票', '凭票入场', '购票入场', '买票', '需要门票', '需门票']


def standardize_fee(fee_raw, title='', description=''):
    if not fee_raw:
        return '免费'

    fee_str = str(fee_raw).strip()

    if fee_str in VALID_FEE_TYPES:
        return fee_str

    combined = f"{fee_str} {title} {description}"

    for kw in FREE_RESERVATION_KEYWORDS:
        if kw in combined and any(fk in combined for fk in FREE_KEYWORDS):
            return '免费需预约'

    for kw in TICKET_REQUIRED_KEYWORDS:
        if kw in combined:
            return '需购票'

    for kw in PARTIAL_FREE_KEYWORDS:
        if kw in combined:
            return '部分免费'

    has_free = any(kw in combined for kw in FREE_KEYWORDS)
    has_charge = any(kw in combined for kw in CHARGE_KEYWORDS)

    if has_charge and has_free:
        return '部分免费'
    if has_charge:
        return '收费'
    if has_free:
        return '免费'

    return '免费'


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

    print("=== 抓取文化馆云平台（全市统一）===\n")
    try:
        from scraper_culture_cloud import fetch_culture_cloud_activities
        cloud_results = fetch_culture_cloud_activities()
        cloud_normalized = []
        for raw in cloud_results:
            activity = normalize_activity(raw, venue_default='文化馆')
            if activity and is_valid_activity(activity):
                cloud_normalized.append(activity)
        print(f"  文化馆云平台有效活动: {len(cloud_normalized)} 条\n")
        all_activities.extend(cloud_normalized)
    except Exception as e:
        print(f"  文化馆云平台抓取失败: {e}\n")

    print("=== 抓取场馆数据 ===\n")

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

    city_codes = ['shenzhen', 'guangzhou', 'shanghai', 'beijing', 'hangzhou']
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

    # 从 venue_registry 生成 venue_info.json（唯一真相源）
    venue_info_path = os.path.join(OUTPUT_DIR, 'venue_info.json')
    generate_venue_info_json(venue_info_path)
    # 同步到 scripts 目录
    scripts_venue_info = os.path.join(os.path.dirname(__file__), 'venue_info.json')
    generate_venue_info_json(scripts_venue_info)

    try:
        generate_rss()
        print("RSS订阅已生成")
    except Exception as e:
        print(f"RSS生成失败: {e}")

    print("\n=== 完成 ===")


if __name__ == "__main__":
    main()
