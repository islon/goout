import json

new_venues = [
    {
        "name": "广州市文化馆新馆",
        "source": "广州本地宝",
        "city": "guangzhou",
        "type": "文化中心",
        "address": "海珠区新滘中路288号（海珠湖公园北侧）",
        "transport": "地铁3号线大塘站B出口",
        "fee": "免费",
        "description": "占地面积全国居首的文化馆，融合汉唐风格与岭南风情，含翰墨园、广绣园等多个主题园区，适合亲子文化体验和拍照打卡。",
        "official_url": "",
        "highlights": ["岭南园林", "汉唐风格", "亲子文化", "拍照打卡"]
    },
    {
        "name": "广州开发区科技馆",
        "source": "广州本地宝",
        "city": "guangzhou",
        "type": "科技馆",
        "address": "黄埔区科学大道162号",
        "transport": "地铁6号线香雪站",
        "fee": "免费",
        "description": "黄埔区小众科技馆，展品77件，四楼探索与发现展厅有光学迷宫、模拟龙卷风等互动展项，人流较少体验舒适。",
        "official_url": "",
        "highlights": ["光学迷宫", "模拟龙卷风", "互动体验", "人流较少"]
    },
    {
        "name": "广州市儿童活动中心",
        "source": "广州本地宝",
        "city": "guangzhou",
        "type": "文化中心",
        "address": "白云区齐心路61号（市儿童公园旁）",
        "transport": "地铁2号线白云公园站C口",
        "fee": "免费",
        "description": "专为3-10岁孩子打造的室内活动中心，含VR航天体验、职业扮演小镇、巨型积木城堡、手工创作区，配套室外儿童公园。",
        "official_url": "",
        "highlights": ["VR航天", "职业扮演", "积木城堡", "手工创作"]
    },
    {
        "name": "广州地铁博物馆",
        "source": "广州本地宝",
        "city": "guangzhou",
        "type": "博物馆",
        "address": "海珠区新港东路1228号万胜广场C塔",
        "transport": "地铁4/8号线万胜围站A出口",
        "fee": "免费",
        "description": "地铁迷专属天堂，含沉浸式隧道、地铁模拟驾驶操作台、轨道科普展区，互动游戏丰富，适合男孩子体验。",
        "official_url": "",
        "highlights": ["地铁模拟驾驶", "轨道科普", "互动游戏", "男孩最爱"]
    },
    {
        "name": "广州市城市规划展览中心",
        "source": "广州本地宝",
        "city": "guangzhou",
        "type": "展览馆",
        "address": "白云区展览路1号",
        "transport": "地铁2号线白云文化广场站A口",
        "fee": "免费",
        "description": "国家4A级景点，运用大量高科技互动设备展示广州过去、现在和未来，4D影院、飞跃广州2049体验需预约。",
        "official_url": "",
        "highlights": ["城市规划", "4D影院", "飞跃广州", "高科技互动"]
    },
    {
        "name": "海心沙科技岛·未来岛",
        "source": "广州本地宝",
        "city": "guangzhou",
        "type": "展览馆",
        "address": "天河区海心沙亚运公园",
        "transport": "APM线海心沙站A口",
        "fee": "免费",
        "description": "全空间智能体验中心，可沉浸式体验低空经济示范场景等科技展示项目，适合亲子科技探索。",
        "official_url": "",
        "highlights": ["智能体验", "低空经济", "科技展示", "亲子探索"]
    },
    {
        "name": "世界技能博物馆",
        "source": "上海本地宝",
        "city": "shanghai",
        "type": "博物馆",
        "address": "静安区山海关路95号",
        "transport": "地铁1号线新闸路站",
        "fee": "免费",
        "description": "国内唯一世界级技能主题博物馆，涵盖科技、工程、美妆等互动区，4楼趣味生活技能展适合小朋友动手体验。",
        "official_url": "",
        "highlights": ["技能主题", "动手体验", "科技工程", "亲子互动"]
    },
    {
        "name": "中国近现代新闻出版博物馆",
        "source": "上海本地宝",
        "city": "shanghai",
        "type": "博物馆",
        "address": "杨浦区周家嘴路3688号",
        "transport": "地铁12号线隆昌路站",
        "fee": "免费",
        "description": "童声八音盒互动、国风亲子体验，可参与五彩粽手工、儿童汉服娃衣设计制作等亲子活动。",
        "official_url": "",
        "highlights": ["童声互动", "国风体验", "手工制作", "亲子活动"]
    },
    {
        "name": "浦东城市规划和公共艺术中心",
        "source": "上海本地宝",
        "city": "shanghai",
        "type": "展览馆",
        "address": "浦东新区世纪大道1号",
        "transport": "地铁2号线陆家嘴站",
        "fee": "免费",
        "description": "城市沙盘互动、亲子科普展厅，轻松了解浦东城市发展历程，适合亲子科普教育。",
        "official_url": "",
        "highlights": ["城市沙盘", "科普展厅", "浦东发展", "亲子科普"]
    },
    {
        "name": "奉贤区规划资源展示馆",
        "source": "上海本地宝",
        "city": "shanghai",
        "type": "展览馆",
        "address": "奉贤区南桥镇",
        "transport": "地铁5号线奉贤新城站",
        "fee": "免费",
        "description": "超大海洋球池、迷你霍比特小屋、巨型积木墙，低龄宝宝放电首选，室内恒温舒适。",
        "official_url": "",
        "highlights": ["海洋球池", "霍比特小屋", "积木墙", "低龄宝宝"]
    },
    {
        "name": "徐家汇书院",
        "source": "上海本地宝",
        "city": "shanghai",
        "type": "图书馆",
        "address": "徐汇区漕溪北路158号",
        "transport": "地铁1/9/11号线徐家汇站",
        "fee": "免费",
        "description": "巨型光启之门艺术装置、专属分龄少儿阅读区，落地窗海派氛围浓厚，适合低龄阅读启蒙和大孩子打卡。",
        "official_url": "",
        "highlights": ["光启之门", "分龄阅读", "海派氛围", "阅读启蒙"]
    },
    {
        "name": "中国妇女儿童博物馆",
        "source": "北京本地宝",
        "city": "beijing",
        "type": "博物馆",
        "address": "东城区北极阁路9号",
        "transport": "地铁5号线东四站",
        "fee": "免费",
        "description": "国家一级博物馆，馆藏近3万件藏品，常设展览分妇女和儿童两大主题，有虚拟现实、互动体验等沉浸式展陈。",
        "official_url": "",
        "highlights": ["妇女儿童主题", "VR体验", "互动展陈", "免费免预约"]
    },
    {
        "name": "中国消防博物馆",
        "source": "北京旅游网",
        "city": "beijing",
        "type": "博物馆",
        "address": "丰台区马家堡东路188号",
        "transport": "地铁4号线公益西桥站",
        "fee": "免费",
        "description": "国家防火防灾教育基地，展示消防历史和现代消防技术，可体验模拟灭火等互动项目，适合亲子安全教育。",
        "official_url": "",
        "highlights": ["消防历史", "模拟灭火", "安全教育", "亲子体验"]
    },
    {
        "name": "中国古动物馆",
        "source": "北京旅游网",
        "city": "beijing",
        "type": "博物馆",
        "address": "西城区西直门外大街142号",
        "transport": "地铁4号线动物园站",
        "fee": "收费",
        "description": "恐龙迷和古生物控的天堂，亿年前化石寻宝任务卡、免费时段讲解，可画恐龙小本子，适合低龄亲子体验。",
        "official_url": "",
        "highlights": ["恐龙化石", "古生物", "寻宝任务", "恐龙迷"]
    },
    {
        "name": "中国园林博物馆",
        "source": "北京旅游网",
        "city": "beijing",
        "type": "博物馆",
        "address": "丰台区射击场路15号",
        "transport": "地铁14号线园博园站",
        "fee": "免费",
        "description": "中国第一座以园林为主题的国家级博物馆，含室内展园与室外展区，展示中国园林悠久历史和艺术魅力。",
        "official_url": "",
        "highlights": ["园林主题", "室内展园", "室外展区", "传统文化"]
    },
    {
        "name": "中国印刷博物馆",
        "source": "北京旅游网",
        "city": "beijing",
        "type": "博物馆",
        "address": "大兴区黄村兴华北路25号",
        "transport": "地铁4号线大兴线清源路站",
        "fee": "免费",
        "description": "世界上收藏印刷机种类最多的博物馆，展示从古代印刷术到近现代技术设备的发展历程。",
        "official_url": "",
        "highlights": ["印刷历史", "印刷机收藏", "科技发展", "免费免预约"]
    },
    {
        "name": "中国考古博物馆",
        "source": "北京旅游网",
        "city": "beijing",
        "type": "博物馆",
        "address": "朝阳区国家体育场北路1号院1号楼",
        "transport": "地铁8/15号线奥林匹克公园站D出口",
        "fee": "免费",
        "description": "国家级专业考古博物馆，展示中华文明源远流长和中华文化辉煌灿烂，实行实名制分时段预约参观。",
        "official_url": "",
        "highlights": ["考古文物", "中华文明", "分时段预约", "国家级博物馆"]
    },
    {
        "name": "北京汽车博物馆",
        "source": "北京旅游网",
        "city": "beijing",
        "type": "博物馆",
        "address": "丰台区南四环西路126号",
        "transport": "地铁9号线科怡路站",
        "fee": "收费",
        "description": "汽车发烧友的天堂，含模拟驾驶舱、解构汽车悬浮展项、设计梦想汽车互动区，B1层模拟驾驶体验区适合1米以上儿童。",
        "official_url": "",
        "highlights": ["模拟驾驶", "解构汽车", "汽车设计", "男孩最爱"]
    },
    {
        "name": "中国铁道博物馆东郊馆",
        "source": "北京旅游网",
        "city": "beijing",
        "type": "博物馆",
        "address": "朝阳区酒仙桥北路1号",
        "transport": "地铁14号线将台站",
        "fee": "收费",
        "description": "真实火车头攀爬、户外大公园、主席专列参观，园区内设有小火车乘坐体验和火车餐厅，适合喜欢攀爬和拍照的孩子。",
        "official_url": "",
        "highlights": ["真实火车", "户外公园", "攀爬体验", "小火车"]
    }
]

with open('venue_info.json', 'r', encoding='utf-8') as f:
    venues = json.load(f)

existing_names = {v['name'] for v in venues}
added_count = 0
for venue in new_venues:
    if venue['name'] not in existing_names:
        venues.append(venue)
        added_count += 1
        print(f"添加: {venue['name']} ({venue['city']})")

with open('venue_info.json', 'w', encoding='utf-8') as f:
    json.dump(venues, f, ensure_ascii=False, indent=2)

print(f"\n共添加 {added_count} 个场馆")
from collections import Counter
print("更新后各城市场馆数量:")
print(Counter([v['city'] for v in venues]))