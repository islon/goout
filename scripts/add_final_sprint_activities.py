import json
import os

DATA_FILE = 'output/exhibitions.json'
OUTPUT_FILE = 'output/exhibitions.json'

new_activities = [
    {"name": "广州珠江新城花城广场灯光秀", "venue": "花城广场", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "广州新中轴线地标，每晚灯光音乐秀，城市夜景。", "source": "广州本地宝", "highlights": ["灯光秀", "花城广场", "夜景"], "type": "演出"},
    {"name": "广州北京路千年古道", "venue": "北京路步行街", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "千年古道遗址，玻璃路面下的唐宋明清路面。", "source": "广州本地宝", "highlights": ["千年古道", "北京路", "历史"], "type": "展览"},
    {"name": "广州动物园熊猫馆", "venue": "广州动物园", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "大熊猫明星，萌态可掬，亲子打卡必看。", "source": "广州本地宝", "highlights": ["熊猫", "动物园", "萌宠"], "type": "亲子活动"},
    {"name": "广州二沙岛艺术公园", "venue": "二沙岛", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "珠江上的绿洲，艺术公园，江景休闲。", "source": "广州本地宝", "highlights": ["二沙岛", "艺术", "江景"], "type": "亲子活动"},
    {"name": "广州生物岛", "venue": "广州国际生物岛", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "江心岛绿道骑行，生态休闲，亲子骑行。", "source": "广州本地宝", "highlights": ["生物岛", "骑行", "生态"], "type": "亲子活动"},
    {"name": "杭州千岛湖啤酒小镇", "venue": "千岛湖啤酒小镇", "city": "hangzhou", "district": "淳安县", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "千岛湖啤酒主题小镇，啤酒博物馆，工业旅游。", "source": "杭州本地宝", "highlights": ["啤酒", "小镇", "千岛湖"], "type": "亲子活动"},
    {"name": "杭州千岛湖石林", "venue": "千岛湖石林景区", "city": "hangzhou", "district": "淳安县", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "华东第一石林，喀斯特地貌，怪石嶙峋。", "source": "杭州本地宝", "highlights": ["石林", "喀斯特", "千岛湖"], "type": "亲子活动"},
    {"name": "杭州建德大慈岩", "venue": "大慈岩风景区", "city": "hangzhou", "district": "建德市", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "江南悬空寺，天然立佛，建德名山。", "source": "杭州本地宝", "highlights": ["大慈岩", "悬空寺", "建德"], "type": "亲子活动"},
    {"name": "杭州建德灵栖洞", "venue": "灵栖洞景区", "city": "hangzhou", "district": "建德市", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "地下艺术宫殿，喀斯特溶洞，86版西游记取景地。", "source": "杭州本地宝", "highlights": ["灵栖洞", "溶洞", "西游记"], "type": "亲子活动"},
    {"name": "杭州临安太湖源", "venue": "太湖源景区", "city": "hangzhou", "district": "临安区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "太湖源头，小九寨沟，峡谷溪水。", "source": "杭州本地宝", "highlights": ["太湖源", "峡谷", "临安"], "type": "亲子活动"},
    {"name": "杭州临安大明山", "venue": "大明山景区", "city": "hangzhou", "district": "临安区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "浙江小黄山，高山草甸，万米岩洞。", "source": "杭州本地宝", "highlights": ["大明山", "登山", "临安"], "type": "亲子活动"},
    {"name": "杭州富阳龙门古镇", "venue": "龙门古镇", "city": "hangzhou", "district": "富阳区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "孙权故里，千年古镇，江南古村落。", "source": "杭州本地宝", "highlights": ["龙门古镇", "孙权", "富阳"], "type": "亲子活动"},
    {"name": "杭州富阳黄公望隐居地", "venue": "黄公望隐居地", "city": "hangzhou", "district": "富阳区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "富春山居图原创地，黄公望结庐处。", "source": "杭州本地宝", "highlights": ["黄公望", "富春山居图", "富阳"], "type": "展览"},
    {"name": "杭州桐庐严子陵钓台", "venue": "严子陵钓台", "city": "hangzhou", "district": "桐庐县", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "东汉严子陵隐居处，富春江畔，钓台古迹。", "source": "杭州本地宝", "highlights": ["严子陵钓台", "富春江", "桐庐"], "type": "亲子活动"},
    {"name": "杭州桐庐瑶琳仙境", "venue": "瑶琳仙境", "city": "hangzhou", "district": "桐庐县", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "全国诸洞冠，钟乳石奇观，地下长河。", "source": "杭州本地宝", "highlights": ["瑶琳仙境", "溶洞", "桐庐"], "type": "展览"},
    {"name": "杭州淳安文渊狮城", "venue": "文渊狮城", "city": "hangzhou", "district": "淳安县", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "水下古城复刻，千年狮城，徽派建筑。", "source": "杭州本地宝", "highlights": ["文渊狮城", "水下古城", "淳安"], "type": "亲子活动"},
    {"name": "杭州建德梅城古镇", "venue": "梅城古镇", "city": "hangzhou", "district": "建德市", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "严州府城，千年古镇，建德美食。", "source": "杭州本地宝", "highlights": ["梅城", "古镇", "严州"], "type": "亲子活动"},
    {"name": "杭州塘栖古镇", "venue": "塘栖古镇", "city": "hangzhou", "district": "临平区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "京杭大运河起点，广济桥，塘栖枇杷。", "source": "杭州本地宝", "highlights": ["塘栖", "古镇", "运河"], "type": "亲子活动"},
    {"name": "杭州河桥古镇", "venue": "河桥古镇", "city": "hangzhou", "district": "临安区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "柳溪江畔，千年古镇，临安风情。", "source": "杭州本地宝", "highlights": ["河桥", "古镇", "临安"], "type": "亲子活动"},
    {"name": "杭州瓶窑老街", "venue": "瓶窑老街", "city": "hangzhou", "district": "余杭区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "良渚旁的古镇，瓶窑老街，非遗体验。", "source": "杭州本地宝", "highlights": ["瓶窑", "老街", "良渚"], "type": "亲子活动"},
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
