import json
import os

DATA_FILE = 'output/exhibitions.json'
OUTPUT_FILE = 'output/exhibitions.json'

new_activities = [
    # ========== 北京补充活动（第六批）==========
    {"name": "什刹海游船消夏", "venue": "什刹海", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-09-30", "fee": "收费", "description": "什刹海游船体验，胡同游览，后海酒吧街，夏日夜游好去处。", "source": "北京本地宝", "highlights": ["什刹海", "游船", "胡同"], "type": "亲子活动"},
    {"name": "南锣鼓巷胡同文化", "venue": "南锣鼓巷", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "北京最古老的街区之一，胡同四合院文化，文创小店美食。", "source": "北京本地宝", "highlights": ["胡同", "南锣鼓巷", "文化"], "type": "亲子活动"},
    {"name": "798艺术区参观", "venue": "798艺术区", "city": "beijing", "district": "朝阳区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "当代艺术聚集地，画廊展览创意小店，文艺青年打卡地。", "source": "北京本地宝", "highlights": ["798", "艺术", "展览"], "type": "展览"},
    {"name": "蓝色港湾暑期活动", "venue": "蓝色港湾", "city": "beijing", "district": "朝阳区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "夏日灯光节，儿童游乐，音乐喷泉，亲子购物休闲。", "source": "北京本地宝", "highlights": ["蓝色港湾", "灯光", "亲子"], "type": "演出"},
    {"name": "北京杜莎夫人蜡像馆", "venue": "北京杜莎夫人蜡像馆", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "前门大街杜莎夫人蜡像馆，明星名人蜡像，互动体验拍照。", "source": "北京本地宝", "highlights": ["蜡像馆", "明星", "前门"], "type": "展览"},
    {"name": "中国国家博物馆古代中国", "venue": "中国国家博物馆", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "古代中国基本陈列，从远古到明清，中华文明发展历程。", "source": "国家博物馆", "highlights": ["国博", "古代中国", "历史"], "type": "展览"},
    {"name": "北京规划展览馆", "venue": "北京市规划展览馆", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "北京城市规划展览，巨大城市模型，了解北京发展变迁。", "source": "北京本地宝", "highlights": ["规划馆", "城市", "模型"], "type": "展览"},
    {"name": "首都博物馆", "venue": "首都博物馆", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "北京历史文化展，佛像瓷器玉器青铜器，临时特展不断。", "source": "北京本地宝", "highlights": ["首博", "北京历史", "文物"], "type": "展览"},
    {"name": "中国人民革命军事博物馆", "venue": "中国人民革命军事博物馆", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "军事武器装备展，飞机坦克导弹，国防教育基地。", "source": "北京本地宝", "highlights": ["军事博物馆", "武器", "国防"], "type": "展览"},
    {"name": "中国航空博物馆", "venue": "中国航空博物馆", "city": "beijing", "district": "昌平区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "亚洲最大航空博物馆，数百架飞机，航空科普教育。", "source": "北京本地宝", "highlights": ["航空博物馆", "飞机", "科普"], "type": "展览"},
    {"name": "北京天文馆球幕影院", "venue": "北京天文馆", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "宇宙剧场球幕电影，星空科普，暑期天文电影展映。", "source": "北京天文馆", "highlights": ["球幕电影", "星空", "天文"], "type": "演出"},
    {"name": "古北水镇一日游", "venue": "古北水镇", "city": "beijing", "district": "密云区", "start_date": "2026-07-01", "end_date": "2026-10-31", "fee": "收费", "description": "司马台长城脚下的江南水乡，夜游长城，温泉度假。", "source": "北京本地宝", "highlights": ["古北水镇", "长城", "度假"], "type": "亲子活动"},
    {"name": "慕田峪长城暑期游", "venue": "慕田峪长城", "city": "beijing", "district": "怀柔区", "start_date": "2026-07-01", "end_date": "2026-10-31", "fee": "收费", "description": "长城秀美风光，缆车滑道，暑期长城研学活动。", "source": "北京本地宝", "highlights": ["慕田峪", "长城", "缆车"], "type": "亲子活动"},
    {"name": "八达岭长城夜游", "venue": "八达岭长城", "city": "beijing", "district": "延庆区", "start_date": "2026-07-01", "end_date": "2026-09-30", "fee": "收费", "description": "八达岭长城夜游活动，灯光璀璨，别样长城体验。", "source": "北京本地宝", "highlights": ["八达岭", "长城", "夜游"], "type": "亲子活动"},
    {"name": "龙庆峡暑期避暑", "venue": "龙庆峡", "city": "beijing", "district": "延庆区", "start_date": "2026-07-01", "end_date": "2026-09-30", "fee": "收费", "description": "北京小桂林，游船避暑，山水风光，清凉一夏。", "source": "北京本地宝", "highlights": ["龙庆峡", "避暑", "山水"], "type": "亲子活动"},
    {"name": "十渡山水漂流", "venue": "十渡风景区", "city": "beijing", "district": "房山区", "start_date": "2026-07-01", "end_date": "2026-09-30", "fee": "收费", "description": "拒马河漂流，蹦极玻璃栈道，山水风光，夏日清凉。", "source": "北京本地宝", "highlights": ["十渡", "漂流", "山水"], "type": "亲子活动"},
    {"name": "北京欢乐谷国潮狂欢节", "venue": "北京欢乐谷", "city": "beijing", "district": "朝阳区", "start_date": "2026-10-01", "end_date": "2026-10-31", "fee": "收费", "description": "国庆国潮主题活动，传统与现代碰撞，精彩演出不断。", "source": "北京本地宝", "highlights": ["国潮", "国庆", "欢乐谷"], "type": "演出"},
    {"name": "北京环球影城万圣节", "venue": "北京环球影城", "city": "beijing", "district": "通州区", "start_date": "2026-10-01", "end_date": "2026-11-11", "fee": "收费", "description": "万圣节特别活动，南瓜灯装饰，惊悚主题，环球大巡游。", "source": "北京本地宝", "highlights": ["万圣节", "环球影城", "南瓜"], "type": "演出"},
    {"name": "香山红叶节", "venue": "香山公园", "city": "beijing", "district": "海淀区", "start_date": "2026-10-15", "end_date": "2026-11-15", "fee": "收费", "description": "金秋十月香山红叶，漫山红遍，登高赏秋景。", "source": "北京本地宝", "highlights": ["香山", "红叶", "赏秋"], "type": "展览"},
    {"name": "北京植物园菊花展", "venue": "北京植物园", "city": "beijing", "district": "海淀区", "start_date": "2026-10-01", "end_date": "2026-11-15", "fee": "收费", "description": "秋季菊花展，数百品种菊花争艳，秋日花景。", "source": "北京本地宝", "highlights": ["菊花展", "秋天", "植物园"], "type": "展览"},

    # ========== 广州补充活动（第六批）==========
    {"name": "越秀公园五羊石像", "venue": "越秀公园", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "广州地标五羊石像，镇海楼，越秀山体育场，城市绿肺。", "source": "广州本地宝", "highlights": ["越秀公园", "五羊", "地标"], "type": "亲子活动"},
    {"name": "白云山风景区", "venue": "白云山风景名胜区", "city": "guangzhou", "district": "白云区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "羊城第一秀，登高望广州全景，摩星岭云台花园。", "source": "广州本地宝", "highlights": ["白云山", "登高", "风景"], "type": "亲子活动"},
    {"name": "莲花山旅游区", "venue": "莲花山旅游区", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "莲花山古采石场，望海观音，莲花塔，历史文化与自然风光。", "source": "广州本地宝", "highlights": ["莲花山", "采石场", "观音"], "type": "亲子活动"},
    {"name": "南沙湿地公园", "venue": "南沙湿地公园", "city": "guangzhou", "district": "南沙区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "候鸟栖息地，湿地游船，观鸟生态，自然科普教育。", "source": "广州本地宝", "highlights": ["湿地", "观鸟", "生态"], "type": "亲子活动"},
    {"name": "百万葵园", "venue": "百万葵园", "city": "guangzhou", "district": "南沙区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "花海主题公园，四季鲜花，松鼠乐园，亲子游乐。", "source": "广州本地宝", "highlights": ["百万葵园", "花海", "亲子"], "type": "亲子活动"},
    {"name": "广州动物园", "venue": "广州动物园", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "大熊猫长颈鹿大象等动物，海洋馆，市区亲子好去处。", "source": "广州本地宝", "highlights": ["动物园", "大熊猫", "市区"], "type": "亲子活动"},
    {"name": "广州海洋馆", "venue": "广州海洋馆", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "海底隧道，海豚表演，海洋生物展，广州动物园内。", "source": "广州本地宝", "highlights": ["海洋馆", "海豚", "海底隧道"], "type": "展览"},
    {"name": "广州塔阿尔法探索乐园", "venue": "广州塔", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "广州塔高空探险，云端漫步，刺激挑战，城市高空体验。", "source": "广州本地宝", "highlights": ["广州塔", "高空探险", "刺激"], "type": "亲子活动"},
    {"name": "花城广场灯光秀", "venue": "花城广场", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "广州新中轴地标，小蛮腰夜景，音乐喷泉，灯光秀。", "source": "广州本地宝", "highlights": ["花城广场", "灯光秀", "夜景"], "type": "演出"},
    {"name": "广州大剧院演出", "venue": "广州大剧院", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "歌剧舞剧音乐会儿童剧，世界顶级演出，艺术熏陶。", "source": "广州本地宝", "highlights": ["大剧院", "演出", "艺术"], "type": "演出"},
    {"name": "广东省博物馆免费展览", "venue": "广东省博物馆", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "广东历史文化展，自然资源展，潮州木雕端砚艺术。", "source": "广东省博物馆", "highlights": ["省博", "广东历史", "免费"], "type": "展览"},
    {"name": "广州少年儿童图书馆活动", "venue": "广州少年儿童图书馆", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "暑期阅读推广，绘本故事会，手工DIY活动。", "source": "广州本地宝", "highlights": ["图书馆", "少儿", "阅读"], "type": "讲座"},
    {"name": "广州市儿童公园暑期", "venue": "广州市儿童公园", "city": "guangzhou", "district": "白云区", "start_date": "2026-07-01", "end_date": "2026-10-31", "fee": "免费", "description": "广州最大免费儿童公园，20多个游乐区域，戏水乐园。", "source": "广州本地宝", "highlights": ["儿童公园", "免费", "游乐"], "type": "亲子活动"},
    {"name": "海珠湿地公园", "venue": "海珠国家湿地公园", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "广州绿心，湿地生态观鸟，花海果园，自然科普。", "source": "广州本地宝", "highlights": ["海珠湿地", "生态", "观鸟"], "type": "亲子活动"},
    {"name": "流溪河国家森林公园", "venue": "流溪河国家森林公园", "city": "guangzhou", "district": "从化区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "森林氧吧，湖泊游船，三桠塘幽谷，避暑胜地。", "source": "广州本地宝", "highlights": ["流溪河", "森林", "避暑"], "type": "亲子活动"},
    {"name": "从化温泉度假", "venue": "从化温泉度假区", "city": "guangzhou", "district": "从化区", "start_date": "2026-09-01", "end_date": "2026-12-31", "fee": "收费", "description": "广东温泉之乡，秋冬温泉度假，养生休闲。", "source": "广州本地宝", "highlights": ["温泉", "从化", "度假"], "type": "亲子活动"},
    {"name": "广州塔摩天轮夜景", "venue": "广州塔", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "世界最高摩天轮，俯瞰广州夜景，浪漫体验。", "source": "广州本地宝", "highlights": ["摩天轮", "夜景", "浪漫"], "type": "亲子活动"},
    {"name": "沙面岛欧陆风情", "venue": "沙面岛", "city": "guangzhou", "district": "荔湾区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "欧陆风情建筑群，百年历史，拍照打卡文艺范。", "source": "广州本地宝", "highlights": ["沙面", "欧陆风情", "拍照"], "type": "亲子活动"},
    {"name": "上下九步行街", "venue": "上下九步行街", "city": "guangzhou", "district": "荔湾区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "广州传统商业步行街，骑楼建筑，老字号美食。", "source": "广州本地宝", "highlights": ["上下九", "步行街", "美食"], "type": "亲子活动"},
    {"name": "北京路文化旅游区", "venue": "北京路步行街", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "千年古道，玻璃路面下的宋代路面遗址，购物美食文化。", "source": "广州本地宝", "highlights": ["北京路", "千年古道", "购物"], "type": "亲子活动"},

    # ========== 上海补充活动（第六批）==========
    {"name": "外滩万国建筑博览", "venue": "外滩", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "外滩万国建筑博览群，黄浦江夜景，上海地标必打卡。", "source": "上海本地宝", "highlights": ["外滩", "夜景", "地标"], "type": "亲子活动"},
    {"name": "豫园城隍庙", "venue": "豫园", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "江南古典园林，城隍庙小吃，上海传统民俗文化。", "source": "上海本地宝", "highlights": ["豫园", "城隍庙", "江南园林"], "type": "亲子活动"},
    {"name": "南京路步行街", "venue": "南京路步行街", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "中华商业第一街，百年老字号，购物美食观光。", "source": "上海本地宝", "highlights": ["南京路", "步行街", "购物"], "type": "亲子活动"},
    {"name": "田子坊石库门", "venue": "田子坊", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "石库门里弄改造，文艺小店创意市集，老上海风情。", "source": "上海本地宝", "highlights": ["田子坊", "石库门", "文艺"], "type": "亲子活动"},
    {"name": "新天地石库门", "venue": "上海新天地", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "石库门建筑改造，时尚餐饮，一大会址相邻。", "source": "上海本地宝", "highlights": ["新天地", "石库门", "时尚"], "type": "亲子活动"},
    {"name": "武康路历史风貌", "venue": "武康路", "city": "shanghai", "district": "徐汇区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "上海最浪漫的马路，武康大楼，梧桐树下老洋房。", "source": "上海本地宝", "highlights": ["武康路", "老洋房", "浪漫"], "type": "亲子活动"},
    {"name": "思南公馆", "venue": "思南公馆", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "花园洋房建筑群，历史名人故居，文艺咖啡小店。", "source": "上海本地宝", "highlights": ["思南公馆", "洋房", "文艺"], "type": "亲子活动"},
    {"name": "朱家角古镇", "venue": "朱家角古镇", "city": "shanghai", "district": "青浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "上海威尼斯，江南水乡古镇，放生桥北大街。", "source": "上海本地宝", "highlights": ["朱家角", "古镇", "水乡"], "type": "亲子活动"},
    {"name": "七宝古镇", "venue": "七宝古镇", "city": "shanghai", "district": "闵行区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "七宝老街，古镇美食小吃，七宝教寺，近郊古镇。", "source": "上海本地宝", "highlights": ["七宝", "古镇", "美食"], "type": "亲子活动"},
    {"name": "召稼楼古镇", "venue": "召稼楼古镇", "city": "shanghai", "district": "闵行区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "召稼楼古镇，江南水乡，特色小吃，周末休闲。", "source": "上海本地宝", "highlights": ["召稼楼", "古镇", "小吃"], "type": "亲子活动"},
    {"name": "枫泾古镇", "venue": "枫泾古镇", "city": "shanghai", "district": "金山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "上海西南门户，吴越名镇，枫泾丁蹄，金山农民画。", "source": "上海本地宝", "highlights": ["枫泾", "古镇", "金山"], "type": "亲子活动"},
    {"name": "上海迪士尼万圣节", "venue": "上海迪士尼乐园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-10-01", "end_date": "2026-11-11", "fee": "收费", "description": "迪士尼万圣节特别活动，唐式南瓜节，反派巡游，不给糖就捣蛋。", "source": "上海本地宝", "highlights": ["迪士尼", "万圣节", "南瓜"], "type": "演出"},
    {"name": "上海迪士尼圣诞节", "venue": "上海迪士尼乐园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-11-20", "end_date": "2027-01-03", "fee": "收费", "description": "圣诞季特别活动，圣诞装饰，节日演出，冰雪奇缘。", "source": "上海本地宝", "highlights": ["迪士尼", "圣诞节", "节日"], "type": "演出"},
    {"name": "上海迪士尼新春", "venue": "上海迪士尼乐园", "city": "shanghai", "district": "浦东新区", "start_date": "2027-01-20", "end_date": "2027-02-28", "fee": "收费", "description": "农历新年特别活动，新春装饰，年味儿演出，米奇拜年。", "source": "上海本地宝", "highlights": ["迪士尼", "新春", "春节"], "type": "演出"},
    {"name": "佘山国家森林公园", "venue": "佘山国家森林公园", "city": "shanghai", "district": "松江区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "上海唯一自然山林，东西佘山，天文台天主教堂。", "source": "上海本地宝", "highlights": ["佘山", "森林公园", "天文台"], "type": "亲子活动"},
    {"name": "东滩湿地公园", "venue": "东滩湿地公园", "city": "shanghai", "district": "崇明区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "崇明东滩候鸟保护区，湿地观鸟，生态科普。", "source": "上海本地宝", "highlights": ["东滩", "湿地", "观鸟"], "type": "亲子活动"},
    {"name": "东平国家森林公园", "venue": "东平国家森林公园", "city": "shanghai", "district": "崇明区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "华东最大平原人工林，森林氧吧，露营烧烤。", "source": "上海本地宝", "highlights": ["东平", "森林", "露营"], "type": "亲子活动"},
    {"name": "顾村公园樱花节", "venue": "顾村公园", "city": "shanghai", "district": "宝山区", "start_date": "2026-03-01", "end_date": "2026-04-30", "fee": "收费", "description": "上海最大樱花林，樱花季赏樱，春日限定美景。", "source": "上海本地宝", "highlights": ["樱花", "顾村公园", "春天"], "type": "展览"},
    {"name": "上海海湾国家森林公园", "venue": "海湾国家森林公园", "city": "shanghai", "district": "奉贤区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "东海之滨的森林氧吧，骑马划船，户外拓展。", "source": "上海本地宝", "highlights": ["海湾", "森林", "户外"], "type": "亲子活动"},
    {"name": "上海长风公园", "venue": "长风公园", "city": "shanghai", "district": "普陀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "铁臂山银锄湖，长风海洋世界相邻，亲子休闲。", "source": "上海本地宝", "highlights": ["长风公园", "免费", "亲子"], "type": "亲子活动"},

    # ========== 杭州补充活动（第六批）==========
    {"name": "西湖十景环湖游", "venue": "西湖风景名胜区", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "苏堤春晓断桥残雪雷峰夕照，西湖十景环湖游，船游西湖。", "source": "杭州本地宝", "highlights": ["西湖", "十景", "游船"], "type": "亲子活动"},
    {"name": "灵隐寺祈福", "venue": "灵隐寺", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "千年古刹灵隐寺，飞来峰石刻，佛教文化，祈福之旅。", "source": "杭州本地宝", "highlights": ["灵隐寺", "佛教", "飞来峰"], "type": "亲子活动"},
    {"name": "雷峰塔登塔", "venue": "雷峰塔景区", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "白娘子传说，登塔望西湖全景，雷峰夕照美景。", "source": "杭州本地宝", "highlights": ["雷峰塔", "白娘子", "西湖全景"], "type": "亲子活动"},
    {"name": "飞来峰石窟", "venue": "飞来峰景区", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "江南石窟艺术瑰宝，五代宋元石刻造像，历史文化价值高。", "source": "杭州本地宝", "highlights": ["飞来峰", "石窟", "石刻"], "type": "展览"},
    {"name": "岳王庙怀古", "venue": "岳王庙", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "岳飞纪念馆，精忠报国，爱国主义教育基地。", "source": "杭州本地宝", "highlights": ["岳飞", "历史", "爱国"], "type": "展览"},
    {"name": "六和塔观潮", "venue": "六和塔", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "钱塘江畔古塔，登塔望钱塘江，八月十八观潮胜地。", "source": "杭州本地宝", "highlights": ["六和塔", "钱塘江", "观潮"], "type": "亲子活动"},
    {"name": "河坊街南宋御街", "venue": "河坊街", "city": "hangzhou", "district": "上城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "杭州老城历史街区，南宋御街，老字号美食，文创小店。", "source": "杭州本地宝", "highlights": ["河坊街", "南宋", "美食"], "type": "亲子活动"},
    {"name": "南宋御街鼓楼", "venue": "南宋御街", "city": "hangzhou", "district": "上城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "南宋皇城根下，鼓楼朝天门，历史文化街区。", "source": "杭州本地宝", "highlights": ["南宋御街", "鼓楼", "历史"], "type": "亲子活动"},
    {"name": "京杭大运河桥西历史街区", "venue": "桥西历史街区", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "运河边老厂房改造，博物馆群，文艺小店，咖啡美食。", "source": "杭州本地宝", "highlights": ["桥西", "运河", "博物馆"], "type": "亲子活动"},
    {"name": "拱宸桥运河夜景", "venue": "拱宸桥", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "京杭大运河南端地标，古桥夜景，运河游船。", "source": "杭州本地宝", "highlights": ["拱宸桥", "运河", "夜景"], "type": "亲子活动"},
    {"name": "湘湖旅游度假区", "venue": "湘湖", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "西湖姊妹湖，越王城山跨湖桥遗址，休闲度假。", "source": "杭州本地宝", "highlights": ["湘湖", "休闲", "遗址"], "type": "亲子活动"},
    {"name": "超山风景区", "venue": "超山风景区", "city": "hangzhou", "district": "临平区", "start_date": "2026-01-01", "end_date": "2026-12-31", "fee": "收费", "description": "十里梅花香雪海，中国五大古梅有其二，赏梅胜地。", "source": "杭州本地宝", "highlights": ["超山", "梅花", "赏梅"], "type": "展览"},
    {"name": "瑶琳仙境溶洞", "venue": "瑶琳仙境", "city": "hangzhou", "district": "桐庐县", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "全国诸洞之冠，喀斯特溶洞，钟乳石奇观，地下长河。", "source": "杭州本地宝", "highlights": ["瑶琳仙境", "溶洞", "钟乳石"], "type": "亲子活动"},
    {"name": "大奇山国家森林公园", "venue": "大奇山国家森林公园", "city": "hangzhou", "district": "桐庐县", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "江南第一名山，森林瀑布溪谷，避暑胜地。", "source": "杭州本地宝", "highlights": ["大奇山", "森林", "避暑"], "type": "亲子活动"},
    {"name": "富春江小三峡", "venue": "富春江", "city": "hangzhou", "district": "桐庐县", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "富春江山水画廊，严子陵钓台，游船赏江景。", "source": "杭州本地宝", "highlights": ["富春江", "小三峡", "游船"], "type": "亲子活动"},
    {"name": "新安江山水画廊", "venue": "新安江", "city": "hangzhou", "district": "建德市", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "新安江漂流，17度江水，夏日清凉，雾漫新安江。", "source": "杭州本地宝", "highlights": ["新安江", "漂流", "清凉"], "type": "亲子活动"},
    {"name": "千岛湖环湖骑行", "venue": "千岛湖风景区", "city": "hangzhou", "district": "淳安县", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "绿道骑行，湖光山色，运动休闲，千岛湖啤酒美食。", "source": "杭州本地宝", "highlights": ["千岛湖", "骑行", "绿道"], "type": "亲子活动"},
    {"name": "龙井茶园采茶", "venue": "龙井村", "city": "hangzhou", "district": "西湖区", "start_date": "2026-03-15", "end_date": "2026-12-31", "fee": "收费", "description": "西湖龙井原产地，茶园采茶体验，炒茶品茶，茶乡风情。", "source": "杭州本地宝", "highlights": ["龙井", "采茶", "茶文化"], "type": "亲子活动"},
    {"name": "梅家坞茶文化村", "venue": "梅家坞", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "龙井茶乡，农家茶楼，茶宴美食，周末休闲。", "source": "杭州本地宝", "highlights": ["梅家坞", "茶", "休闲"], "type": "亲子活动"},
    {"name": "宋城万圣节活动", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-10-15", "end_date": "2026-11-11", "fee": "收费", "description": "宋城万圣潮趴，聊斋夜话，鬼屋探险，化妆舞会。", "source": "杭州本地宝", "highlights": ["宋城", "万圣节", "聊斋"], "type": "演出"},
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
