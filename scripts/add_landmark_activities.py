import json
import os

DATA_FILE = 'output/exhibitions.json'
OUTPUT_FILE = 'output/exhibitions.json'

new_activities = [
    # ========== 北京补充活动（第五批）==========
    {"name": "北京欢乐谷暑期狂欢节", "venue": "北京欢乐谷", "city": "beijing", "district": "朝阳区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "暑期狂欢节，过山车等百余项游乐设施，夜场烟花秀，夏日狂欢好去处。", "source": "北京本地宝", "highlights": ["欢乐谷", "游乐设施", "夜场"], "type": "亲子活动"},
    {"name": "北京环球影城暑期活动", "venue": "北京环球影城", "city": "beijing", "district": "通州区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "七大主题园区，哈利波特变形金刚功夫熊猫等，暑期特别活动与演出。", "source": "北京本地宝", "highlights": ["环球影城", "主题乐园", "IP"], "type": "亲子活动"},
    {"name": "北京野生动物园暑期游", "venue": "北京野生动物园", "city": "beijing", "district": "大兴区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "自驾区猛兽体验步行区萌宠互动，暑期动物科普活动与动物见面会。", "source": "北京本地宝", "highlights": ["野生动物园", "动物", "亲子"], "type": "亲子活动"},
    {"name": "北京海洋馆探秘", "venue": "北京海洋馆", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "世界最大内陆海洋馆，海豚海狮表演，海底隧道，暑期海洋科普夏令营。", "source": "北京本地宝", "highlights": ["海洋馆", "海豚", "科普"], "type": "亲子活动"},
    {"name": "中国科学技术馆暑期活动", "venue": "中国科学技术馆", "city": "beijing", "district": "朝阳区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "科学乐园主展厅球幕影院，暑期推出科学表演科普实验小课堂等特别活动。", "source": "北京本地宝", "highlights": ["科技馆", "科学", "科普"], "type": "展览"},
    {"name": "北京自然博物馆恐龙展", "venue": "北京自然博物馆", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "恐龙公园古哺乳动物古爬行动物等展厅，暑期化石挖掘体验活动。", "source": "北京本地宝", "highlights": ["自然博物馆", "恐龙", "化石"], "type": "展览"},
    {"name": "北京天文馆暑期星空", "venue": "北京天文馆", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "天象厅宇宙剧场，暑期天文夏令营，望远镜观测星空，陨石标本展。", "source": "北京本地宝", "highlights": ["天文馆", "星空", "科普"], "type": "亲子活动"},
    {"name": "国家动物博物馆", "venue": "国家动物博物馆", "city": "beijing", "district": "朝阳区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "亚洲最大动物博物馆，濒危动物展蝴蝶展，暑期自然科普活动。", "source": "北京本地宝", "highlights": ["动物", "博物馆", "科普"], "type": "展览"},
    {"name": "北京汽车博物馆暑期", "venue": "北京汽车博物馆", "city": "beijing", "district": "丰台区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "汽车发展史展，互动体验项目，暑期汽车科技夏令营。", "source": "北京本地宝", "highlights": ["汽车", "博物馆", "科技"], "type": "展览"},
    {"name": "世界公园环球风情游", "venue": "世界公园", "city": "beijing", "district": "丰台区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "世界著名建筑微缩景观，暑期各国文化展演，夜景灯光秀。", "source": "北京本地宝", "highlights": ["世界公园", "微缩景观", "文化"], "type": "亲子活动"},
    {"name": "北京欢乐谷玛雅狂欢节", "venue": "北京欢乐谷", "city": "beijing", "district": "朝阳区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "玛雅主题狂欢节，水上狂欢派对，玛雅文化展演，夜场电音秀。", "source": "北京本地宝", "highlights": ["玛雅", "狂欢节", "水上"], "type": "演出"},
    {"name": "石景山游乐园夏日狂欢", "venue": "石景山游乐园", "city": "beijing", "district": "石景山区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "摩天轮过山车等游乐设施，暑期狂欢节夜场烟花表演。", "source": "北京本地宝", "highlights": ["游乐园", "摩天轮", "夜场"], "type": "亲子活动"},
    {"name": "北京动物园熊猫馆", "venue": "北京动物园", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "大熊猫萌兰等明星动物，暑期动物科普讲解，儿童动物园互动。", "source": "北京本地宝", "highlights": ["动物园", "熊猫", "科普"], "type": "亲子活动"},
    {"name": "北海公园荷花节", "venue": "北海公园", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "荷花节盛大启幕，荷花展游船赏荷，皇家园林夏日美景。", "source": "北京本地宝", "highlights": ["荷花", "北海", "皇家园林"], "type": "展览"},
    {"name": "圆明园荷花季", "venue": "圆明园遗址公园", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "曲院风荷等景点荷花盛放，游船赏荷，荷花摄影大赛。", "source": "北京本地宝", "highlights": ["荷花", "圆明园", "遗址"], "type": "展览"},
    {"name": "颐和园昆明湖游船", "venue": "颐和园", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-10-31", "fee": "收费", "description": "昆明湖画舫龙船游船，暑期皇家园林深度游，长廊彩绘讲解。", "source": "北京本地宝", "highlights": ["颐和园", "游船", "皇家园林"], "type": "亲子活动"},
    {"name": "居庸关长城研学营", "venue": "居庸关长城", "city": "beijing", "district": "昌平区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "长城历史文化研学，登长城体验，长城建筑知识科普。", "source": "北京本地宝", "highlights": ["长城", "研学", "历史"], "type": "亲子活动"},
    {"name": "明十三陵探秘", "venue": "明十三陵", "city": "beijing", "district": "昌平区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "定陵地宫长陵祾恩殿，明代历史文化研学，暑期特别讲解活动。", "source": "北京本地宝", "highlights": ["十三陵", "明代", "历史"], "type": "亲子活动"},
    {"name": "周口店北京人遗址", "venue": "周口店北京人遗址博物馆", "city": "beijing", "district": "房山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "北京人遗址探秘，古人类化石展，考古体验活动。", "source": "北京本地宝", "highlights": ["北京人", "遗址", "考古"], "type": "亲子活动"},
    {"name": "北京植物园暑期赏花", "venue": "北京植物园", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-09-30", "fee": "收费", "description": "热带植物馆温室，卧佛寺，夏季花卉展，植物科普活动。", "source": "北京本地宝", "highlights": ["植物园", "花卉", "科普"], "type": "展览"},

    # ========== 广州补充活动（第五批）==========
    {"name": "长隆野生动物世界", "venue": "长隆野生动物世界", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "500多种2万余只珍稀动物，自驾区小火车游览，考拉熊猫馆。", "source": "广州本地宝", "highlights": ["长隆", "野生动物", "熊猫"], "type": "亲子活动"},
    {"name": "长隆欢乐世界暑期狂欢", "venue": "长隆欢乐世界", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "垂直过山车等70余项游乐设施，暑期狂欢节主题活动，花车巡游。", "source": "广州本地宝", "highlights": ["长隆", "欢乐世界", "过山车"], "type": "亲子活动"},
    {"name": "长隆飞鸟乐园", "venue": "长隆飞鸟乐园", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "百鸟飞歌鹈鹕投喂，湿地生态探索，鸟类科普教育。", "source": "广州本地宝", "highlights": ["飞鸟", "湿地", "科普"], "type": "亲子活动"},
    {"name": "广州融创文旅城", "venue": "广州融创文旅城", "city": "guangzhou", "district": "花都区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "融创乐园雪世界水世界体育世界，一站式暑期亲子度假。", "source": "广州本地宝", "highlights": ["融创", "滑雪", "乐园"], "type": "亲子活动"},
    {"name": "融创雪世界暑期滑雪", "venue": "广州融创雪世界", "city": "guangzhou", "district": "花都区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "华南最大室内滑雪场，暑期冰雪体验，滑雪教学夏令营。", "source": "广州本地宝", "highlights": ["滑雪", "室内", "冰雪"], "type": "亲子活动"},
    {"name": "正佳极地海洋世界", "venue": "正佳极地海洋世界", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "白鲸企鹅北极熊等极地动物，海洋生物展，美人鱼表演。", "source": "广州本地宝", "highlights": ["极地海洋", "白鲸", "美人鱼"], "type": "展览"},
    {"name": "广州塔摩天轮", "venue": "广州塔", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "广州塔小蛮腰登顶，摩天轮俯瞰全城，夜景灯光秀。", "source": "广州本地宝", "highlights": ["广州塔", "摩天轮", "夜景"], "type": "亲子活动"},
    {"name": "珠江夜游", "venue": "珠江游", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "珠江夜游大沙头码头天字码头，两岸灯光秀，广州夜景尽收眼底。", "source": "广州本地宝", "highlights": ["珠江夜游", "夜景", "游船"], "type": "亲子活动"},
    {"name": "岭南印象园", "venue": "岭南印象园", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "岭南传统文化主题公园，镬耳屋趟栊门，非遗体验表演。", "source": "广州本地宝", "highlights": ["岭南文化", "非遗", "古建筑"], "type": "亲子活动"},
    {"name": "宝墨园岭南园林", "venue": "宝墨园", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "岭南园林艺术精品，锦鲤观赏，包青天文化，亲子捞鱼体验。", "source": "广州本地宝", "highlights": ["宝墨园", "岭南园林", "锦鲤"], "type": "亲子活动"},
    {"name": "余荫山房古典园林", "venue": "余荫山房", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "广东四大名园之一，精致小巧的岭南园林，亭台楼阁小桥流水。", "source": "广州本地宝", "highlights": ["余荫山房", "古典园林", "四大名园"], "type": "展览"},
    {"name": "沙湾古镇文化游", "venue": "沙湾古镇", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "800年历史岭南文化古镇，留耕堂何氏大宗祠，姜撞奶美食。", "source": "广州本地宝", "highlights": ["沙湾古镇", "岭南", "美食"], "type": "亲子活动"},
    {"name": "南沙天后宫", "venue": "南沙天后宫", "city": "guangzhou", "district": "南沙区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "天下天后第一宫，妈祖文化，海滨风光，南沙湿地相邻。", "source": "广州本地宝", "highlights": ["天后宫", "妈祖", "海滨"], "type": "亲子活动"},
    {"name": "广州科学中心科技探索", "venue": "广东科学中心", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "亚洲最大科学中心，常设展厅8个主题，IMAX球幕影院。", "source": "广州本地宝", "highlights": ["科学中心", "科技", "科普"], "type": "展览"},
    {"name": "广州少年儿童图书馆", "venue": "广州少年儿童图书馆", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "暑期阅读推广活动，绘本故事会，手工DIY，少儿阅读推广。", "source": "广州本地宝", "highlights": ["图书馆", "少儿", "阅读"], "type": "讲座"},
    {"name": "广州博物馆镇海楼", "venue": "广州博物馆", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "镇海楼历史文化展，广州城建史，暑期研学活动。", "source": "广州本地宝", "highlights": ["镇海楼", "历史", "广州"], "type": "展览"},
    {"name": "南越王博物院", "venue": "南越王博物院", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "南越王墓出土文物展，丝缕玉衣文帝行玺，岭南汉代历史。", "source": "广州本地宝", "highlights": ["南越王", "文物", "汉代"], "type": "展览"},
    {"name": "南汉二陵博物馆", "venue": "南汉二陵博物馆", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "五代十国南汉国历史展，德陵康陵出土文物，考古现场展示。", "source": "广州本地宝", "highlights": ["南汉", "考古", "五代十国"], "type": "展览"},
    {"name": "广州民俗博物馆", "venue": "广州民俗博物馆", "city": "guangzhou", "district": "花都区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "资政大夫祠古建筑群，广州民俗文化展，灰塑砖雕艺术。", "source": "广州本地宝", "highlights": ["民俗", "古建筑", "非遗"], "type": "展览"},
    {"name": "辛亥革命纪念馆", "venue": "辛亥革命纪念馆", "city": "guangzhou", "district": "黄埔区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "辛亥革命历史展，孙中山革命事迹，红色教育基地。", "source": "广州本地宝", "highlights": ["辛亥革命", "孙中山", "红色"], "type": "展览"},

    # ========== 上海补充活动（第五批）==========
    {"name": "上海迪士尼度假区", "venue": "上海迪士尼乐园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "七大主题园区，米奇大街探险岛宝藏湾，暑期特别活动烟花秀。", "source": "上海本地宝", "highlights": ["迪士尼", "主题乐园", "米奇"], "type": "亲子活动"},
    {"name": "上海欢乐谷暑期狂欢", "venue": "上海欢乐谷", "city": "shanghai", "district": "松江区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "百余项游乐设施，暑期狂欢节，夜场电音烟花秀。", "source": "上海本地宝", "highlights": ["欢乐谷", "游乐设施", "夜场"], "type": "亲子活动"},
    {"name": "上海野生动物园", "venue": "上海野生动物园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "车入区步行区，大熊猫老虎狮子长颈鹿，动物表演互动。", "source": "上海本地宝", "highlights": ["野生动物园", "大熊猫", "动物表演"], "type": "亲子活动"},
    {"name": "上海海昌海洋公园", "venue": "上海海昌海洋公园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "虎鲸海豚白鲸表演，五大主题区，暑期虎鲸造浪节夜场。", "source": "上海本地宝", "highlights": ["海昌", "海洋公园", "虎鲸"], "type": "亲子活动"},
    {"name": "上海科技馆", "venue": "上海科技馆", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "机器人世界信息时代生物万象等展厅，IMAX球幕影院，暑期科普活动。", "source": "上海本地宝", "highlights": ["科技馆", "机器人", "科普"], "type": "展览"},
    {"name": "上海自然博物馆", "venue": "上海自然博物馆", "city": "shanghai", "district": "静安区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "生命演化长河恐龙盛世，自然标本展，暑期自然探索营。", "source": "上海本地宝", "highlights": ["自然博物馆", "恐龙", "自然"], "type": "展览"},
    {"name": "上海杜莎夫人蜡像馆", "venue": "上海杜莎夫人蜡像馆", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "明星名人蜡像，互动体验，拍照打卡好去处。", "source": "上海本地宝", "highlights": ["蜡像馆", "明星", "互动"], "type": "展览"},
    {"name": "上海乐高探索中心", "venue": "上海乐高探索中心", "city": "shanghai", "district": "普陀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "乐高积木拼搭体验，迷你天地主题区，暑期乐高夏令营。", "source": "上海本地宝", "highlights": ["乐高", "积木", "儿童"], "type": "亲子活动"},
    {"name": "上海马戏城ERA时空之旅", "venue": "上海马戏城", "city": "shanghai", "district": "静安区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "ERA时空之旅超级多媒体梦幻剧，杂技表演，视觉盛宴。", "source": "上海本地宝", "highlights": ["马戏", "杂技", "表演"], "type": "演出"},
    {"name": "上海迪士尼乐园夏日狂欢", "venue": "上海迪士尼乐园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "夏日狂欢节，花车巡游，城堡烟花秀，迪士尼朋友见面会。", "source": "上海本地宝", "highlights": ["迪士尼", "夏日狂欢", "烟花"], "type": "演出"},
    {"name": "豫园夏日游园会", "venue": "豫园", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "夏日国风游园会，传统民俗表演，老字号美食，灯会展演。", "source": "上海本地宝", "highlights": ["豫园", "国风", "游园会"], "type": "演出"},
    {"name": "上海锦江乐园夜市", "venue": "锦江乐园", "city": "shanghai", "district": "闵行区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "锦江乐园夜市美食嘉年华，游乐设施夜场，夏日狂欢。", "source": "上海本地宝", "highlights": ["锦江乐园", "夜市", "美食"], "type": "亲子活动"},
    {"name": "上海动物园暑期", "venue": "上海动物园", "city": "shanghai", "district": "长宁区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "大熊猫长颈鹿大象等动物，暑期动物科普讲解，儿童游园。", "source": "上海本地宝", "highlights": ["动物园", "大熊猫", "科普"], "type": "亲子活动"},
    {"name": "东方明珠观光", "venue": "东方明珠广播电视塔", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "上海地标建筑，登塔观光，全透明悬空廊，上海城市历史发展陈列馆。", "source": "上海本地宝", "highlights": ["东方明珠", "地标", "观光"], "type": "亲子活动"},
    {"name": "上海中心大厦观光", "venue": "上海中心大厦", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "上海最高楼118层观光厅，俯瞰全城，360度城市美景。", "source": "上海本地宝", "highlights": ["上海中心", "观光", "高楼"], "type": "亲子活动"},
    {"name": "上海海洋水族馆", "venue": "上海海洋水族馆", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "世界最长海底隧道，15000多只海洋生物，中国区南极区等展区。", "source": "上海本地宝", "highlights": ["海洋水族馆", "海底隧道", "海洋生物"], "type": "展览"},
    {"name": "长风海洋世界", "venue": "长风海洋世界", "city": "shanghai", "district": "普陀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "白鲸表演海底世界，极地探险，暑期海洋科普活动。", "source": "上海本地宝", "highlights": ["海洋世界", "白鲸", "长风公园"], "type": "展览"},
    {"name": "辰山植物园花展", "venue": "辰山植物园", "city": "shanghai", "district": "松江区", "start_date": "2026-07-01", "end_date": "2026-10-31", "fee": "收费", "description": "矿坑花园温室展览，夏季花卉展，植物科普夏令营。", "source": "上海本地宝", "highlights": ["植物园", "矿坑", "花卉"], "type": "展览"},
    {"name": "上海野生动物园奇妙夜", "venue": "上海野生动物园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "夜间动物园探索，观察夜行动物，露营体验，亲子奇妙夜。", "source": "上海本地宝", "highlights": ["奇妙夜", "夜间动物园", "露营"], "type": "亲子活动"},
    {"name": "崇明西沙湿地生态游", "venue": "崇明西沙湿地公园", "city": "shanghai", "district": "崇明区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "崇明西沙湿地，观鸟生态步道，潮汐现象，自然科普。", "source": "上海本地宝", "highlights": ["湿地", "崇明", "观鸟"], "type": "亲子活动"},

    # ========== 杭州补充活动（第五批）==========
    {"name": "杭州宋城千古情", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "给我一天还你千年，宋城千古情演出，宋代文化主题公园。", "source": "杭州本地宝", "highlights": ["宋城", "千古情", "宋代文化"], "type": "演出"},
    {"name": "杭州乐园暑期狂欢", "venue": "杭州乐园", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "过山车大摆锤等游乐设施，暑期狂欢节，主题活动不断。", "source": "杭州本地宝", "highlights": ["杭州乐园", "过山车", "狂欢节"], "type": "亲子活动"},
    {"name": "杭州烂苹果乐园", "venue": "烂苹果乐园", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "全室内高科技亲子乐园，魔幻小镇，近百项互动体验。", "source": "杭州本地宝", "highlights": ["烂苹果", "亲子乐园", "室内"], "type": "亲子活动"},
    {"name": "杭州长乔极地海洋公园", "venue": "长乔极地海洋公园", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "白鲸海豚北极熊企鹅等极地海洋动物，海洋剧场表演。", "source": "杭州本地宝", "highlights": ["极地海洋", "白鲸", "海豚"], "type": "展览"},
    {"name": "杭州野生动物园", "venue": "杭州野生动物世界", "city": "hangzhou", "district": "富阳区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "自驾区小火车游览，大熊猫老虎狮子，动物表演互动。", "source": "杭州本地宝", "highlights": ["野生动物园", "大熊猫", "动物表演"], "type": "亲子活动"},
    {"name": "浙江自然博物院安吉馆", "venue": "浙江自然博物院安吉馆", "city": "hangzhou", "district": "安吉县", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "亚洲最大自然博物馆之一，地质馆贝林馆恐龙馆等，自然科普。", "source": "杭州本地宝", "highlights": ["自然博物馆", "安吉", "恐龙"], "type": "展览"},
    {"name": "杭州科技馆暑期活动", "venue": "杭州科技馆", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "科学实验科普表演，暑期科技夏令营，机器人互动体验。", "source": "杭州本地宝", "highlights": ["科技馆", "科学", "机器人"], "type": "展览"},
    {"name": "杭州植物园夏令营", "venue": "杭州植物园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "植物探索夏令营，植物识别昆虫观察，自然笔记创作。", "source": "杭州本地宝", "highlights": ["植物园", "夏令营", "自然"], "type": "亲子活动"},
    {"name": "西溪湿地龙舟胜会", "venue": "西溪国家湿地公园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-10-31", "fee": "收费", "description": "西溪湿地游船，龙舟体验，湿地生态科普，洪园景观。", "source": "杭州本地宝", "highlights": ["西溪湿地", "龙舟", "生态"], "type": "亲子活动"},
    {"name": "京杭大运河游船", "venue": "京杭大运河杭州段", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "运河游船，拱宸桥桥西历史街区，运河博物馆群。", "source": "杭州本地宝", "highlights": ["大运河", "游船", "历史"], "type": "亲子活动"},
    {"name": "杭州宋城我回大宋", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "我回大宋主题活动，穿汉服游宋城，沉浸式宋代生活体验。", "source": "杭州本地宝", "highlights": ["宋城", "汉服", "沉浸式"], "type": "演出"},
    {"name": "千岛湖亲水游", "venue": "千岛湖风景区", "city": "hangzhou", "district": "淳安县", "start_date": "2026-07-01", "end_date": "2026-09-30", "fee": "收费", "description": "游船游湖登梅峰岛，亲水活动，鱼头美食，暑期度假。", "source": "杭州本地宝", "highlights": ["千岛湖", "游船", "亲水"], "type": "亲子活动"},
    {"name": "乌镇水乡一日游", "venue": "乌镇", "city": "hangzhou", "district": "桐乡市", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "江南水乡古镇，东栅西栅，木心美术馆，水乡夜景。", "source": "杭州本地宝", "highlights": ["乌镇", "水乡", "古镇"], "type": "亲子活动"},
    {"name": "横店影视城穿越游", "venue": "横店影视城", "city": "hangzhou", "district": "东阳市", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "秦王宫明清宫苑梦幻谷，影视主题公园，看演出遇明星。", "source": "杭州本地宝", "highlights": ["横店", "影视", "穿越"], "type": "亲子活动"},
    {"name": "杭州动物园熊猫馆", "venue": "杭州动物园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "大熊猫成就双好，虎山中兽类区，动物科普讲解。", "source": "杭州本地宝", "highlights": ["动物园", "熊猫", "科普"], "type": "亲子活动"},
    {"name": "杭州少年儿童公园", "venue": "杭州少年儿童公园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-10-31", "fee": "收费", "description": "儿童游乐设施，满陇桂雨景区，暑期亲子活动。", "source": "杭州本地宝", "highlights": ["儿童公园", "游乐", "亲子"], "type": "亲子活动"},
    {"name": "杭州海底世界", "venue": "杭州海底世界", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "万松岭路口海底世界，海狮表演美人鱼表演，海底隧道。", "source": "杭州本地宝", "highlights": ["海底世界", "美人鱼", "海狮"], "type": "展览"},
    {"name": "浙西大峡谷漂流", "venue": "浙西大峡谷", "city": "hangzhou", "district": "临安区", "start_date": "2026-07-01", "end_date": "2026-09-30", "fee": "收费", "description": "峡谷漂流，山水景观，自然探险，暑期清凉体验。", "source": "杭州本地宝", "highlights": ["大峡谷", "漂流", "山水"], "type": "亲子活动"},
    {"name": "双溪竹海漂流", "venue": "双溪竹海漂流景区", "city": "hangzhou", "district": "余杭区", "start_date": "2026-07-01", "end_date": "2026-09-30", "fee": "收费", "description": "竹海漂流，竹筏皮筏可选，竹林探幽，夏日清凉。", "source": "杭州本地宝", "highlights": ["双溪漂流", "竹海", "竹筏"], "type": "亲子活动"},
    {"name": "杭州西湖音乐喷泉", "venue": "西湖音乐喷泉", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "西湖音乐喷泉夜景表演，灯光音乐水舞交融，西湖地标景观。", "source": "杭州本地宝", "highlights": ["音乐喷泉", "西湖", "夜景"], "type": "演出"},
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
