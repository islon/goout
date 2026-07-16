import json
import os

DATA_FILE = 'output/exhibitions.json'
OUTPUT_FILE = 'output/exhibitions.json'

new_activities = [
    {"name": "杭州西湖音乐喷泉", "venue": "西湖音乐喷泉", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "西湖边音乐灯光喷泉，每晚定时表演，浪漫夜景。", "source": "杭州本地宝", "highlights": ["音乐喷泉", "西湖", "夜景"], "type": "演出"},
    {"name": "杭州宋城失落古城", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "高科技沉浸式体验，南宋临安城繁华再现。", "source": "杭州本地宝", "highlights": ["失落古城", "沉浸式", "宋城"], "type": "演出"},
    {"name": "杭州宋城清明上河图电影馆", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "活的清明上河图，画卷人物动起来。", "source": "杭州本地宝", "highlights": ["清明上河图", "电影馆", "宋城"], "type": "演出"},
    {"name": "杭州宋城丽江恋歌", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "大型实景演出，丽江少数民族爱情故事。", "source": "杭州本地宝", "highlights": ["丽江恋歌", "实景演出", "宋城"], "type": "演出"},
    {"name": "杭州宋城大地震", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "5D实景剧大地震，感人至深的抗震救灾故事。", "source": "杭州本地宝", "highlights": ["大地震", "5D", "宋城"], "type": "演出"},
    {"name": "杭州宋城映山红", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "红色主题演出，革命历史故事。", "source": "杭州本地宝", "highlights": ["映山红", "红色", "宋城"], "type": "演出"},
    {"name": "杭州宋城狂欢节", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "暑期泼水狂欢节，夏日清凉派对。", "source": "杭州本地宝", "highlights": ["狂欢节", "泼水", "暑期"], "type": "演出"},
    {"name": "杭州宋城辣椒节", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-09-01", "end_date": "2026-09-30", "fee": "收费", "description": "秋季辣椒节，火辣辣的民俗表演。", "source": "杭州本地宝", "highlights": ["辣椒节", "秋季", "宋城"], "type": "演出"},
    {"name": "杭州宋城天灯节", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-10-01", "end_date": "2026-10-31", "fee": "收费", "description": "国庆天灯节，放天灯许愿，民俗盛会。", "source": "杭州本地宝", "highlights": ["天灯节", "国庆", "宋城"], "type": "演出"},
    {"name": "杭州宋城火把节", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-11-01", "end_date": "2026-11-30", "fee": "收费", "description": "彝族火把节，篝火晚会，民族风情。", "source": "杭州本地宝", "highlights": ["火把节", "篝火", "民族"], "type": "演出"},
    {"name": "杭州宋城花灯节", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-12-01", "end_date": "2027-01-15", "fee": "收费", "description": "冬季花灯节，万盏花灯，新年氛围。", "source": "杭州本地宝", "highlights": ["花灯节", "新年", "宋城"], "type": "演出"},
    {"name": "杭州烂苹果乐园糖果小镇", "venue": "烂苹果乐园", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "糖果主题小镇，梦幻色彩，儿童最爱。", "source": "杭州本地宝", "highlights": ["糖果小镇", "烂苹果", "儿童"], "type": "亲子活动"},
    {"name": "杭州烂苹果乐园魔法丛林", "venue": "烂苹果乐园", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "神秘魔法丛林，互动体验，寓教于乐。", "source": "杭州本地宝", "highlights": ["魔法丛林", "烂苹果", "互动"], "type": "亲子活动"},
    {"name": "杭州烂苹果乐园荒诞小镇", "venue": "烂苹果乐园", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "荒诞有趣的小镇，颠倒房屋，奇幻世界。", "source": "杭州本地宝", "highlights": ["荒诞小镇", "烂苹果", "奇幻"], "type": "亲子活动"},
    {"name": "杭州烂苹果乐园爱的故事屋", "venue": "烂苹果乐园", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "温馨故事屋，亲子互动，儿童剧表演。", "source": "杭州本地宝", "highlights": ["故事屋", "烂苹果", "亲子"], "type": "演出"},
    {"name": "杭州长乔极地海洋公园白鲸表演", "venue": "长乔极地海洋公园", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "白鲸水下表演，人鲸共舞，精彩绝伦。", "source": "杭州本地宝", "highlights": ["白鲸", "表演", "极地海洋"], "type": "演出"},
    {"name": "杭州长乔极地海洋公园海豚表演", "venue": "长乔极地海洋公园", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "海豚跳跃表演，海洋剧场，欢乐互动。", "source": "杭州本地宝", "highlights": ["海豚", "表演", "极地海洋"], "type": "演出"},
    {"name": "杭州长乔极地海洋公园企鹅馆", "venue": "长乔极地海洋公园", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "南极企鹅近距离观赏，企鹅喂食体验。", "source": "杭州本地宝", "highlights": ["企鹅", "极地", "喂食"], "type": "展览"},
    {"name": "杭州长乔极地海洋公园北极熊", "venue": "长乔极地海洋公园", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "北极熊近距离观赏，北极生态展示。", "source": "杭州本地宝", "highlights": ["北极熊", "北极", "极地"], "type": "展览"},
    {"name": "杭州长乔极地海洋公园水母宫", "venue": "长乔极地海洋公园", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "梦幻水母宫，七彩水母，海底奇观。", "source": "杭州本地宝", "highlights": ["水母", "梦幻", "海底"], "type": "展览"},
    {"name": "杭州野生动物园步行区", "venue": "杭州野生动物世界", "city": "hangzhou", "district": "富阳区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "步行观赏各类动物，亲子互动体验。", "source": "杭州本地宝", "highlights": ["步行区", "野生动物园", "亲子"], "type": "亲子活动"},
    {"name": "杭州野生动物园自驾区", "venue": "杭州野生动物世界", "city": "hangzhou", "district": "富阳区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "自驾穿越猛兽区，近距离观赏野生动物。", "source": "杭州本地宝", "highlights": ["自驾区", "野生动物园", "猛兽"], "type": "亲子活动"},
    {"name": "杭州野生动物园森林剧场", "venue": "杭州野生动物世界", "city": "hangzhou", "district": "富阳区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "森林动物表演，精彩马戏，互动体验。", "source": "杭州本地宝", "highlights": ["森林剧场", "表演", "马戏"], "type": "演出"},
    {"name": "杭州野生动物园熊猫馆", "venue": "杭州野生动物世界", "city": "hangzhou", "district": "富阳区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "大熊猫馆，国宝大熊猫，萌态可掬。", "source": "杭州本地宝", "highlights": ["熊猫", "国宝", "萌宠"], "type": "展览"},
    {"name": "杭州野生动物园游乐场", "venue": "杭州野生动物世界", "city": "hangzhou", "district": "富阳区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "游乐设施，旋转木马小火车，亲子欢乐。", "source": "杭州本地宝", "highlights": ["游乐场", "亲子", "游乐设施"], "type": "亲子活动"},
    {"name": "杭州东方文化园", "venue": "东方文化园", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "儒释道三教文化，东方园林，宗教艺术。", "source": "杭州本地宝", "highlights": ["东方文化", "三教", "园林"], "type": "亲子活动"},
    {"name": "杭州湘湖游船", "venue": "湘湖旅游度假区", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "湘湖游船，湖光山色，休闲度假。", "source": "杭州本地宝", "highlights": ["湘湖", "游船", "休闲"], "type": "亲子活动"},
    {"name": "杭州湘湖花海", "venue": "湘湖旅游度假区", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "四季花海，四季不同花卉盛开。", "source": "杭州本地宝", "highlights": ["花海", "湘湖", "免费"], "type": "展览"},
    {"name": "杭州跨湖桥遗址博物馆", "venue": "跨湖桥遗址博物馆", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "八千年前独木舟，跨湖桥文化，考古遗址。", "source": "杭州本地宝", "highlights": ["跨湖桥", "遗址", "考古"], "type": "展览"},
    {"name": "杭州灵山风景区", "venue": "灵山风景区", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "灵山幻境溶洞，山水风光，避暑胜地。", "source": "杭州本地宝", "highlights": ["灵山", "溶洞", "避暑"], "type": "亲子活动"},
    {"name": "杭州白龙潭景区", "venue": "白龙潭景区", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "杭州近郊瀑布，山林溪水，自然野趣。", "source": "杭州本地宝", "highlights": ["白龙潭", "瀑布", "自然"], "type": "亲子活动"},
    {"name": "杭州西溪湿地洪园摇橹船", "venue": "西溪湿地洪园", "city": "hangzhou", "district": "余杭区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "摇橹船游湿地，慢享西溪，诗意水乡。", "source": "杭州本地宝", "highlights": ["摇橹船", "西溪湿地", "水乡"], "type": "亲子活动"},
    {"name": "杭州西溪湿地电瓶船", "venue": "西溪国家湿地公园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "电瓶船游西溪，深潭口烟水渔庄，生态观光。", "source": "杭州本地宝", "highlights": ["电瓶船", "西溪湿地", "生态"], "type": "亲子活动"},
    {"name": "杭州西溪湿地茭芦田庄", "venue": "西溪国家湿地公园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "西溪湿地东区景点，生态观鸟，自然野趣。", "source": "杭州本地宝", "highlights": ["茭芦田庄", "西溪湿地", "观鸟"], "type": "亲子活动"},
    {"name": "杭州西溪湿地火柿节", "venue": "西溪国家湿地公园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-09-15", "end_date": "2026-10-15", "fee": "收费", "description": "秋季火柿节，红柿满枝，采摘体验。", "source": "杭州本地宝", "highlights": ["火柿节", "秋季", "采摘"], "type": "亲子活动"},
    {"name": "杭州西溪花朝节", "venue": "西溪国家湿地公园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-03-15", "end_date": "2026-05-15", "fee": "收费", "description": "春季花朝节，百花盛放，花神祭祀。", "source": "杭州本地宝", "highlights": ["花朝节", "春天", "花"], "type": "展览"},
    {"name": "杭州西湖荷花展", "venue": "西湖景区", "city": "hangzhou", "district": "西湖区", "start_date": "2026-06-15", "end_date": "2026-08-31", "fee": "免费", "description": "西湖荷花盛开，曲院风荷，夏日美景。", "source": "杭州本地宝", "highlights": ["荷花", "西湖", "夏天"], "type": "展览"},
    {"name": "杭州西湖桂花节", "venue": "满觉陇", "city": "hangzhou", "district": "西湖区", "start_date": "2026-09-15", "end_date": "2026-10-15", "fee": "免费", "description": "满陇桂雨，金秋桂花飘香，赏桂胜地。", "source": "杭州本地宝", "highlights": ["桂花", "秋天", "满觉陇"], "type": "展览"},
    {"name": "杭州西湖菊花展", "venue": "杭州植物园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-10-25", "end_date": "2026-11-25", "fee": "收费", "description": "秋季菊花展，各色菊花争艳，秋日花景。", "source": "杭州本地宝", "highlights": ["菊花展", "秋天", "植物园"], "type": "展览"},
    {"name": "杭州西溪探梅节", "venue": "西溪国家湿地公园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-02-01", "end_date": "2026-03-15", "fee": "收费", "description": "春季探梅，曲水寻梅，早春第一景。", "source": "杭州本地宝", "highlights": ["探梅节", "梅花", "春天"], "type": "展览"},
    {"name": "杭州超山探梅", "venue": "超山风景区", "city": "hangzhou", "district": "临平区", "start_date": "2026-02-01", "end_date": "2026-03-15", "fee": "收费", "description": "十里梅花香雪海，中国五大古梅，赏梅胜地。", "source": "杭州本地宝", "highlights": ["超山", "梅花", "赏梅"], "type": "展览"},
    {"name": "杭州灵峰探梅", "venue": "杭州植物园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-02-01", "end_date": "2026-03-15", "fee": "收费", "description": "西湖三大赏梅胜地之一，灵峰探梅。", "source": "杭州本地宝", "highlights": ["灵峰", "梅花", "赏梅"], "type": "展览"},
    {"name": "杭州太子湾郁金香展", "venue": "太子湾公园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-03-15", "end_date": "2026-04-15", "fee": "免费", "description": "春季郁金香展，大片郁金香花海，春日盛景。", "source": "杭州本地宝", "highlights": ["郁金香", "太子湾", "春天"], "type": "展览"},
    {"name": "杭州太子湾樱花展", "venue": "太子湾公园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-03-20", "end_date": "2026-04-10", "fee": "免费", "description": "春季樱花盛开，粉色浪漫，春日限定。", "source": "杭州本地宝", "highlights": ["樱花", "太子湾", "春天"], "type": "展览"},
    {"name": "杭州虎跑泉水", "venue": "虎跑公园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "西湖三大名泉之一，虎跑梦泉，龙井茶配虎跑水。", "source": "杭州本地宝", "highlights": ["虎跑泉", "名泉", "西湖"], "type": "亲子活动"},
    {"name": "杭州龙井茶园采茶", "venue": "龙井村", "city": "hangzhou", "district": "西湖区", "start_date": "2026-03-20", "end_date": "2026-04-20", "fee": "收费", "description": "春季采茶体验，明前茶采摘，茶文化体验。", "source": "杭州本地宝", "highlights": ["采茶", "龙井", "茶文化"], "type": "亲子活动"},
    {"name": "杭州九溪烟树漂流", "venue": "九溪十八涧", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-09-30", "fee": "免费", "description": "夏日九溪玩水，溪水清凉，亲子溯溪。", "source": "杭州本地宝", "highlights": ["九溪", "玩水", "清凉"], "type": "亲子活动"},
    {"name": "杭州云栖竹径避暑", "venue": "云栖竹径", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "竹林避暑，清凉一夏，西湖新十景。", "source": "杭州本地宝", "highlights": ["云栖竹径", "避暑", "竹林"], "type": "亲子活动"},
]

if __name__ == '__main__':
    if not os.path.exists(DATA_FILE):
        print(f"文件 {DATA_FILE} 不存在！")
        exit(1)
    
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        exhibitions = json.load(f)
    
    existing_names = {e['name'] for e in exhibitions}
    added_count = 0
    
    for activity in new_activities:
        if activity['name'] not in existing_names:
            exhibitions.append(activity)
            print(f"添加: {activity['name']} ({activity['city']})")
            added_count += 1
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(exhibitions, f, ensure_ascii=False, indent=2)
    
    print(f"\n共添加 {added_count} 个活动")
    
    city_counts = {}
    for e in exhibitions:
        city_counts[e['city']] = city_counts.get(e['city'], 0) + 1
    print(f"\n各城市活动数量:")
    for city, count in sorted(city_counts.items()):
        print(f"  {city}: {count}")
