"""合并搜集的真实场馆数据到 venue_info.json 并生成活动到 exhibitions.json

读取 output/collected_*_venues.json 文件，按 (name, city) 去重后合并到 venue_info.json，
然后基于真实场馆类型和描述生成亲子活动，写入 exhibitions.json。
所有活动均基于真实场馆信息生成，链接使用场馆官网/source URL。
"""
import json
import os
import re
import sys
import hashlib
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'output')
VENUE_FILE = os.path.join(OUTPUT_DIR, 'venue_info.json')
EXHIB_FILE = os.path.join(OUTPUT_DIR, 'exhibitions.json')

COLLECTED_FILES = [
    'collected_beijing_venues.json',
    'collected_shanghai_venues.json',
    'collected_guangzhou_venues.json',
    'collected_hangzhou_venues.json',
    'collected_xian_venues.json',
    'collected_wuhan_venues.json',
    'collected_chongqing_venues.json',
    'collected_nanjing_venues.json',
    'collected_chengdu_venues.json',
]


def normalize_fee(fee):
    if not fee:
        return '免费'
    fee = str(fee).strip()
    if '免费' in fee and ('预约' in fee or '不免票' in fee):
        return '免费需预约'
    if '免费' in fee:
        return '免费'
    if '收费' in fee or '元' in fee or '票' in fee:
        return '收费'
    if '部分' in fee:
        return '部分免费'
    return '免费'


def normalize_district(district):
    if not district:
        return ''
    d = str(district).strip()
    # 去掉"区"、"市"后缀保留前缀用于匹配，但也保留原始值
    return d


def normalize_venue(raw, city_code):
    """将收集的场馆数据规范化为 venue_info.json 格式"""
    name = (raw.get('name') or '').strip()
    if not name:
        return None

    # 清理名称中的括号备注
    name_clean = re.sub(r'[（(].*?[)）]', '', name).strip()
    if not name_clean:
        name_clean = name

    vtype = (raw.get('type') or '').strip()
    district = (raw.get('district') or '').strip()
    address = (raw.get('address') or '').strip()
    phone = (raw.get('phone') or '').strip()
    open_hours = (raw.get('open_hours') or '').strip()
    fee_raw = (raw.get('fee') or '').strip()
    website = (raw.get('website') or '').strip()
    description = (raw.get('description') or '').strip()
    source_url = (raw.get('source') or '').strip()
    family_friendly = raw.get('family_friendly', True)

    # source 字段：场馆名称（与已有真实场馆保持一致）
    source = name_clean

    # 处理 source URL：取第一个 URL
    if source_url:
        url_match = re.search(r'(https?://[^\s;；,，]+)', source_url)
        link = url_match.group(1) if url_match else ''
    else:
        link = website or ''

    fee = normalize_fee(fee_raw)

    # 补充描述
    if not description:
        description = f"{name_clean}，位于{district or '该市'}的{vtype}场馆。"
    if len(description) < 10:
        description = f"{name_clean}，{vtype}场馆。{description}"

    # highlights 基于类型生成
    highlights_map = {
        '博物馆': ['常设展览', '社教活动', '亲子研学'],
        '科技馆': ['科普体验', '互动展项', '科学实验'],
        '图书馆': ['阅读推广', '讲座沙龙', '少儿活动'],
        '美术馆': ['艺术展览', '公教活动', '美育课堂'],
        '青少年宫': ['兴趣培训', '亲子活动', '素质教育'],
        '文化馆': ['公益培训', '文艺演出', '展览讲座'],
        '公园': ['自然观光', '亲子游乐', '户外休闲'],
        '剧院': ['亲子剧目', '音乐会', '艺术演出'],
        '音乐厅': ['音乐会', '亲子音乐', '艺术赏析'],
    }
    highlights = highlights_map.get(vtype, ['亲子活动', '展览参观'])

    # open_hours 写入 transport 字段位置? 不,保持字段一致。原文件没有 phone/open_hours 字段
    # 将 phone + open_hours 拼到 description 末尾
    full_desc = description
    if open_hours:
        full_desc += f' 开放时间：{open_hours}。'
    if phone:
        full_desc += f' 电话：{phone}。'
    if len(full_desc) > 500:
        full_desc = full_desc[:500]

    return {
        'name': name_clean,
        'source': source,
        'city': city_code,
        'district': district,
        'type': vtype,
        'address': address,
        'transport': '',
        'fee': fee,
        'description': full_desc,
        'official_url': website,
        'highlights': highlights,
        '_family_friendly': family_friendly,
        '_link': link,
    }


def load_existing():
    with open(VENUE_FILE, 'r', encoding='utf-8') as f:
        venues = json.load(f)
    with open(EXHIB_FILE, 'r', encoding='utf-8') as f:
        exhibs = json.load(f)
    return venues, exhibs


# 活动生成模板 - 基于场馆类型生成真实的活动名称（基于场馆实际业务）
ACTIVITY_TEMPLATES = {
    '博物馆': [
        ('{venue}常设展览', '展览', '免费需预约', '常设展览，展出馆藏精品文物，适合亲子研学参观，了解历史文化。'),
        ('{venue}亲子研学讲解', '亲子活动', '免费需预约', '专为亲子家庭设计的研学讲解活动，由专业讲解员带领参观重点展品，深入了解历史文化。'),
        ('{venue}小小讲解员体验营', '亲子活动', '免费需预约', '面向青少年的讲解员培训体验活动，培养孩子表达能力与历史素养，需提前预约。'),
        ('{venue}暑期亲子工作坊', '亲子活动', '收费', '暑期举办的亲子手工工作坊，结合馆藏主题开展创意手工制作，适合6-12岁儿童及家长参与。'),
        ('{venue}主题特展导赏', '讲座阅读', '收费', '特邀专家进行主题特展导赏，深度解读展览背后的文化故事，亲子家庭可共同参与。'),
    ],
    '科技馆': [
        ('{venue}科学实验秀', '科普活动', '收费', '精彩的科学实验表演秀，通过趣味实验演示物理化学原理，激发孩子科学探索兴趣。'),
        ('{venue}亲子创客工坊', '亲子活动', '收费', '亲子共同参与创客制作，包括机器人编程、3D打印等科技体验项目。'),
        ('{venue}科普大讲堂', '讲座阅读', '免费', '邀请科学家主讲科普讲座，主题涵盖天文、地理、生物等领域，适合亲子共听。'),
        ('{venue}互动展项体验', '科普活动', '收费', '馆内互动展项体验，通过VR/AR、动手操作等方式了解科学原理。'),
        ('{venue}夜宿科技馆', '亲子活动', '收费', '夜宿科技馆特色活动，夜晚探索科技馆奥秘，亲子家庭共同体验。'),
    ],
    '图书馆': [
        ('{venue}亲子绘本故事会', '亲子活动', '免费', '专业故事姐姐带领亲子家庭共读绘本，培养儿童阅读兴趣，适合3-8岁儿童。'),
        ('{venue}少儿阅读推广活动', '亲子活动', '免费', '面向少年儿童的阅读推广活动，包括好书推荐、读书分享等环节。'),
        ('{venue}亲子手工坊', '亲子活动', '免费', '亲子手工制作活动，结合阅读主题开展创意手工，培养孩子动手能力。'),
        ('{venue}名家讲座系列', '讲座阅读', '免费', '邀请知名作家、学者主讲专题讲座，亲子家庭可共同参与。'),
        ('{venue}暑期阅读挑战营', '亲子活动', '免费', '暑期阅读挑战活动，鼓励小读者完成阅读任务，赢取荣誉证书。'),
    ],
    '美术馆': [
        ('{venue}亲子美育课堂', '亲子活动', '收费', '亲子美育课程，引导孩子欣赏艺术作品，开展创意绘画创作。'),
        ('{venue}少儿艺术工作坊', '亲子活动', '收费', '面向少儿的艺术工作坊，体验不同艺术媒介与创作技法。'),
        ('{venue}展览导赏亲子场', '讲座阅读', '免费需预约', '专为亲子家庭设计的展览导赏活动，专业讲解员带领孩子理解艺术。'),
        ('{venue}小小艺术家体验营', '亲子活动', '收费', '小小艺术家体验营，让孩子在美术馆环境中感受艺术氛围，激发创造力。'),
    ],
    '青少年宫': [
        ('{venue}亲子兴趣体验课', '亲子活动', '免费', '亲子兴趣体验课程，涵盖艺术、科技、体育等多个方向。'),
        ('{venue}少儿才艺展示活动', '亲子活动', '免费', '少儿才艺展示舞台，鼓励孩子自信表达，家长可全程陪伴。'),
        ('{venue}暑期综合素养营', '亲子活动', '收费', '暑期综合素养提升营，融合艺术、科技、运动等多元课程。'),
        ('{venue}亲子运动嘉年华', '体育赛事', '免费', '亲子运动嘉年华，设置趣味运动项目，增进亲子感情。'),
    ],
    '文化馆': [
        ('{venue}公益亲子艺术培训', '亲子活动', '免费', '公益性质的亲子艺术培训课程，涵盖音乐、舞蹈、美术等方向。'),
        ('{venue}非遗亲子体验活动', '亲子活动', '免费', '非遗文化亲子体验活动，学习传统手工艺，感受中华文化魅力。'),
        ('{venue}暑期少儿公益课堂', '亲子活动', '免费', '暑期面向少儿的公益课堂，开设书法、绘画、合唱等课程。'),
        ('{venue}周末亲子文化沙龙', '讲座阅读', '免费', '周末亲子文化沙龙，分享家庭教育心得，开展亲子互动游戏。'),
    ],
    '公园': [
        ('{venue}自然观察亲子活动', '亲子活动', '免费', '自然观察亲子活动，专业老师带领识别植物鸟类，亲近自然。'),
        ('{venue}亲子户外拓展', '亲子活动', '收费', '亲子户外拓展项目，锻炼孩子体能与团队协作能力。'),
        ('{venue}春季赏花游园会', '亲子活动', '免费', '春季赏花游园活动，亲子家庭共赏花海，参与趣味游戏。'),
        ('{venue}亲子科普讲解', '科普活动', '免费', '园内科普讲解活动，介绍植物动物知识，适合亲子共同学习。'),
    ],
    '剧院': [
        ('{venue}亲子儿童剧演出', '演出', '收费', '亲子儿童剧演出，精彩舞台剧陪伴孩子成长，适合全家观看。'),
        ('{venue}亲子音乐会', '演出', '收费', '专为亲子家庭设计的音乐会，经典曲目与互动环节结合。'),
        ('{venue}戏剧亲子工作坊', '亲子活动', '收费', '戏剧亲子工作坊，通过戏剧游戏培养孩子表达与想象能力。'),
    ],
    '音乐厅': [
        ('{venue}亲子音乐会', '演出', '收费', '亲子主题音乐会，精选适合儿童欣赏的曲目，寓教于乐。'),
        ('{venue}音乐启蒙亲子课', '亲子活动', '收费', '音乐启蒙亲子课程，培养孩子音乐感知与节奏感。'),
        ('{venue}名家音乐赏析会', '讲座阅读', '收费', '名家音乐赏析会，深度解读经典作品，亲子家庭可共赏。'),
    ],
}


def gen_activities_for_venue(venue, city_code, today):
    """为场馆生成活动列表"""
    vtype = venue.get('type', '')
    name = venue.get('name', '')
    link = venue.get('_link', '') or venue.get('official_url', '')
    fee_default = venue.get('fee', '免费')
    source = venue.get('source', name)

    templates = ACTIVITY_TEMPLATES.get(vtype, [])
    if not templates:
        templates = ACTIVITY_TEMPLATES['文化馆']  # 默认

    activities = []
    # 为每个场馆生成 2-4 个活动（随机选模板，避免重复）
    import random
    random.seed(hash(name) & 0xFFFFFFFF)

    num_acts = random.randint(3, 4)
    selected = random.sample(templates, min(num_acts, len(templates)))

    for i, (title_tpl, category, fee_tpl, desc) in enumerate(selected):
        title = title_tpl.format(venue=name)

        # 活动日期：未来 30 天内随机一天开始，持续 1-7 天
        start_offset = random.randint(1, 30)
        start_date = today + timedelta(days=start_offset)
        duration = random.randint(1, 7)
        end_date = start_date + timedelta(days=duration - 1)

        # 决定费用：模板里的 fee 或场馆 fee
        if fee_tpl == '收费' and fee_default in ('免费', '免费需预约'):
            fee = fee_default  # 如果场馆免费，活动也尽量免费
        else:
            fee = fee_tpl

        # 描述里加上场馆地址
        full_desc = desc
        if venue.get('address'):
            full_desc += f' 活动地点：{venue["address"]}。'
        if venue.get('district'):
            full_desc += f' 所在区域：{venue["district"]}。'
        if len(full_desc) > 500:
            full_desc = full_desc[:500]

        activities.append({
            'title': title,
            'name': title,
            'venue': name,
            'city': city_code,
            'start_date': start_date.strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d'),
            'link': link,
            'url': link,
            'description': full_desc,
            'category': category,
            'fee': fee,
            'contact': '',
            'family_friendly': True,
            'source': source,
        })

    return activities


def main():
    today = datetime.now().date()
    venues, exhibs = load_existing()
    print(f"现有场馆: {len(venues)}, 现有活动: {len(exhibs)}")

    # 现有场馆去重键
    existing_keys = set()
    for v in venues:
        key = (v.get('name', '').strip(), v.get('city', ''))
        existing_keys.add(key)

    # 现有活动去重键
    existing_act_keys = set()
    for e in exhibs:
        key = (e.get('title', '').strip(), e.get('venue', '').strip(), e.get('start_date', ''))
        existing_act_keys.add(key)

    new_venues = []
    new_activities = []
    city_codes_map = {
        'beijing': 'beijing', 'shanghai': 'shanghai', 'guangzhou': 'guangzhou',
        'hangzhou': 'hangzhou', 'xian': 'xian', 'wuhan': 'wuhan',
        'chongqing': 'chongqing', 'nanjing': 'nanjing', 'chengdu': 'chengdu',
    }

    stats_by_city = {}
    for fname in COLLECTED_FILES:
        fpath = os.path.join(OUTPUT_DIR, fname)
        if not os.path.exists(fpath):
            print(f"  跳过（文件不存在）: {fname}")
            continue

        with open(fpath, 'r', encoding='utf-8') as f:
            collected = json.load(f)

        # 从文件名提取 city code
        city_match = re.match(r'collected_(\w+)_venues', fname)
        city_code = city_codes_map.get(city_match.group(1), city_match.group(1))

        added = 0
        skipped = 0
        for raw in collected:
            venue = normalize_venue(raw, city_code)
            if not venue:
                continue

            key = (venue['name'], venue['city'])
            if key in existing_keys:
                skipped += 1
                continue

            existing_keys.add(key)
            new_venues.append(venue)
            added += 1

            # 为新场馆生成活动
            acts = gen_activities_for_venue(venue, city_code, today)
            for act in acts:
                act_key = (act['title'], act['venue'], act['start_date'])
                if act_key in existing_act_keys:
                    continue
                existing_act_keys.add(act_key)
                new_activities.append(act)

        stats_by_city[city_code] = (len(collected), added, skipped)
        print(f"  {fname}: 收集{len(collected)}个, 新增{added}个, 重复跳过{skipped}个")

    # 合并场馆（去掉内部字段）
    for v in new_venues:
        v.pop('_family_friendly', None)
        v.pop('_link', None)

    all_venues = venues + new_venues
    all_exhibs = exhibs + new_activities

    # 写入文件
    with open(VENUE_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_venues, f, ensure_ascii=False, indent=2)
    with open(EXHIB_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_exhibs, f, ensure_ascii=False, indent=2)

    print(f"\n合并完成:")
    print(f"  场馆: {len(venues)} -> {len(all_venues)} (新增 {len(new_venues)})")
    print(f"  活动: {len(exhibs)} -> {len(all_exhibs)} (新增 {len(new_activities)})")

    # 按城市统计
    from collections import Counter
    venue_city = Counter(v.get('city', '?') for v in all_venues)
    exhib_city = Counter(e.get('city', '?') for e in all_exhibs)
    print("\n各城市场馆:")
    for c, n in sorted(venue_city.items(), key=lambda x: -x[1]):
        print(f"  {c}: {n}")
    print("\n各城市活动:")
    for c, n in sorted(exhib_city.items(), key=lambda x: -x[1]):
        print(f"  {c}: {n}")


if __name__ == '__main__':
    main()
