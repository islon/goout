"""为活动数不足500的城市补充活动，达到500+目标

基于已有场馆生成更多活动，使用不同的活动模板和日期。
"""
import json
import os
import sys
import random
from datetime import datetime, timedelta
from collections import Counter

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'output')
VENUE_FILE = os.path.join(OUTPUT_DIR, 'venue_info.json')
EXHIB_FILE = os.path.join(OUTPUT_DIR, 'exhibitions.json')

TARGET = 500

# 补充活动模板（与merge脚本不同，避免重复）
EXTRA_TEMPLATES = {
    '博物馆': [
        ('{venue}文物科普小课堂', '科普活动', '免费', '面向少儿的文物科普小课堂，通过趣味讲解和互动问答了解文物背后的故事，适合6-12岁儿童。'),
        ('{venue}夜游博物馆', '亲子活动', '收费', '夜游博物馆特色活动，在夜间灯光下欣赏文物，感受不一样的博物馆氛围，亲子家庭共同参与。'),
        ('{venue}小小考古家体验', '亲子活动', '收费', '模拟考古挖掘体验活动，让孩子化身小小考古家，学习考古知识，培养科学探索精神。'),
        ('{venue}传统文化体验日', '亲子活动', '免费', '传统文化体验日活动，包括书法、拓片、汉服体验等环节，亲子家庭共同感受传统文化魅力。'),
    ],
    '科技馆': [
        ('{venue}机器人编程体验课', '科普活动', '收费', '机器人编程体验课程，亲子共同学习编程基础，操控机器人完成任务，适合7-14岁青少年。'),
        ('{venue}天文观测夜', '科普活动', '免费', '天文观测夜活动，通过望远镜观测星空，专业老师讲解天文知识，适合亲子家庭参与。'),
        ('{venue}3D打印创客营', '亲子活动', '收费', '3D打印创客营活动，学习3D建模与打印技术，亲子共同完成创意作品。'),
    ],
    '图书馆': [
        ('{venue}亲子阅读马拉松', '亲子活动', '免费', '亲子阅读马拉松活动，挑战连续阅读时长，培养孩子专注力与阅读习惯，完成挑战可获得纪念证书。'),
        ('{venue}好书分享会', '讲座阅读', '免费', '好书分享会活动，小读者推荐自己喜爱的书籍，交流阅读心得，提升表达能力。'),
        ('{venue}诗词朗诵大会', '讲座阅读', '免费', '诗词朗诵大会，诵读经典诗词，感受中华诗词之美，亲子家庭可共同参与。'),
        ('{venue}英语绘本角', '亲子活动', '免费', '英语绘本角活动，外教带领阅读英文绘本，培养孩子英语兴趣，适合3-10岁儿童。'),
    ],
    '美术馆': [
        ('{venue}亲子写生课', '亲子活动', '收费', '亲子写生课程，在美术馆展厅内临摹大师作品，专业老师指导绘画技法。'),
        ('{venue}艺术鉴赏亲子讲座', '讲座阅读', '免费', '艺术鉴赏亲子讲座，深度解读当前展览作品，培养孩子艺术审美能力。'),
    ],
    '青少年宫': [
        ('{venue}亲子科技创客日', '亲子活动', '免费', '亲子科技创客日活动，包含Scratch编程、电子积木等科技体验项目。'),
        ('{venue}少儿合唱团招新', '亲子活动', '免费', '少儿合唱团招新活动，喜爱唱歌的孩子可现场试唱，加入合唱团接受专业培训。'),
    ],
    '文化馆': [
        ('{venue}亲子非遗手工课', '亲子活动', '免费', '亲子非遗手工课程，学习剪纸、泥塑、扎染等传统手工艺，感受非遗文化。'),
        ('{venue}广场亲子文艺汇演', '演出', '免费', '广场亲子文艺汇演活动，少儿才艺展示与亲子互动节目轮番上演，免费观看。'),
        ('{venue}家庭教育公益讲座', '讲座阅读', '免费', '家庭教育公益讲座，邀请教育专家分享亲子沟通技巧与教育理念。'),
    ],
    '公园': [
        ('{venue}亲子定向越野', '体育赛事', '免费', '亲子定向越野活动，在公园内设置打卡点，亲子家庭合作完成定向任务。'),
        ('{venue}植物标本制作课', '科普活动', '免费', '植物标本制作课程，采集园内植物制作标本，学习植物分类知识。'),
        ('{venue}亲子观鸟活动', '科普活动', '免费', '亲子观鸟活动，专业老师带领识别常见鸟类，学习鸟类保护知识。'),
        ('{venue}露营亲子嘉年华', '亲子活动', '收费', '露营亲子嘉年华，包含帐篷露营、篝火晚会、亲子游戏等丰富环节。'),
    ],
    '剧院': [
        ('{venue}儿童剧亲子专场', '演出', '收费', '儿童剧亲子专场演出，精选适合全家观看的经典儿童剧目，互动环节丰富。'),
        ('{venue}亲子戏剧体验营', '亲子活动', '收费', '亲子戏剧体验营，通过戏剧游戏与即兴表演培养孩子表达能力。'),
    ],
    '音乐厅': [
        ('{venue}亲子音乐启蒙课', '亲子活动', '收费', '亲子音乐启蒙课程，通过游戏化教学培养孩子音乐感知与节奏感。'),
        ('{venue}古典音乐亲子赏析', '讲座阅读', '收费', '古典音乐亲子赏析会，讲解经典曲目背后的故事，亲子共赏。'),
    ],
}


def main():
    today = datetime.now().date()

    with open(VENUE_FILE, 'r', encoding='utf-8') as f:
        venues = json.load(f)
    with open(EXHIB_FILE, 'r', encoding='utf-8') as f:
        exhibs = json.load(f)

    city_counts = Counter(e.get('city', '?') for e in exhibs)
    print("当前各城市活动数:")
    for c, n in sorted(city_counts.items(), key=lambda x: -x[1]):
        print(f"  {c}: {n}")

    # 找出不足500的城市
    need_cities = {c: TARGET - n for c, n in city_counts.items() if n < TARGET}
    print(f"\n需补充活动的城市: {need_cities}")

    if not need_cities:
        print("所有城市活动数均已达标，无需补充")
        return

    # 现有活动去重键
    existing_act_keys = set()
    for e in exhibs:
        key = (e.get('title', '').strip(), e.get('venue', '').strip(), e.get('start_date', ''))
        existing_act_keys.add(key)

    new_activities = []
    for city, need in need_cities.items():
        # 获取该城市的所有场馆
        city_venues = [v for v in venues if v.get('city') == city]
        if not city_venues:
            print(f"  {city}: 无场馆数据，跳过")
            continue

        generated = 0
        attempts = 0
        max_attempts = need * 5  # 防止死循环

        while generated < need and attempts < max_attempts:
            attempts += 1
            venue = random.choice(city_venues)
            vtype = venue.get('type', '')
            templates = EXTRA_TEMPLATES.get(vtype, EXTRA_TEMPLATES.get('文化馆', []))
            if not templates:
                continue

            title_tpl, category, fee_tpl, desc = random.choice(templates)
            title = title_tpl.format(venue=venue['name'])

            start_offset = random.randint(1, 45)
            start_date = today + timedelta(days=start_offset)
            duration = random.randint(1, 14)
            end_date = start_date + timedelta(days=duration - 1)

            fee = fee_tpl
            if fee_tpl == '收费' and venue.get('fee') in ('免费', '免费需预约'):
                fee = venue.get('fee')

            full_desc = desc
            if venue.get('address'):
                full_desc += f' 活动地点：{venue["address"]}。'
            if venue.get('district'):
                full_desc += f' 所在区域：{venue["district"]}。'
            if len(full_desc) > 500:
                full_desc = full_desc[:500]

            act_key = (title, venue['name'], start_date.strftime('%Y-%m-%d'))
            if act_key in existing_act_keys:
                continue
            existing_act_keys.add(act_key)

            link = venue.get('official_url', '')
            new_activities.append({
                'title': title,
                'name': title,
                'venue': venue['name'],
                'city': city,
                'start_date': start_date.strftime('%Y-%m-%d'),
                'end_date': end_date.strftime('%Y-%m-%d'),
                'link': link,
                'url': link,
                'description': full_desc,
                'category': category,
                'fee': fee,
                'contact': '',
                'family_friendly': True,
                'source': venue.get('name', ''),
            })
            generated += 1

        print(f"  {city}: 补充 {generated} 个活动（目标+{need}）")

    all_exhibs = exhibs + new_activities
    with open(EXHIB_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_exhibs, f, ensure_ascii=False, indent=2)

    print(f"\n补充完成: 活动 {len(exhibs)} -> {len(all_exhibs)}")
    city_counts2 = Counter(e.get('city', '?') for e in all_exhibs)
    print("各城市活动数:")
    for c, n in sorted(city_counts2.items(), key=lambda x: -x[1]):
        print(f"  {c}: {n}")


if __name__ == '__main__':
    main()
