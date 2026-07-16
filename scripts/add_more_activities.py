import json
import os

DATA_FILE = 'output/exhibitions.json'
OUTPUT_FILE = 'output/exhibitions.json'

new_activities = [
    # ========== 北京补充活动 ==========
    {"name": "红领巾志愿者培育", "venue": "香山革命纪念馆", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "招募中小学生志愿者20名（分2批），培训设置香山党史通识、科学发声、讲解礼仪、场馆服务四大课程。", "source": "北京本地宝", "highlights": ["志愿者", "党史", "讲解"], "type": "亲子活动"},
    {"name": "同学赶考CityWalk", "venue": "清华园车站旧址", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "精品小团研学，路线串联清华园车站旧址、颐和园益寿堂、中共中央香山驻地旧址、香山革命纪念馆，全程配备专属讲解员。", "source": "北京本地宝", "highlights": ["CityWalk", "红色研学", "亲子"], "type": "亲子活动"},
    {"name": "我是青年宣讲员", "venue": "香山革命纪念馆", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "招募青年宣讲员，入驻展厅开展定点公益讲解服务，联动高校开展暑期防暑急救、食品安全科普宣讲。", "source": "北京本地宝", "highlights": ["宣讲员", "公益讲解", "科普"], "type": "讲座"},
    {"name": "我是青年策展人", "venue": "香山革命纪念馆", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "参与专题展览暑期筹备，负责史料、历史照片搜集筛选，参与展览大纲、展陈设计研讨。", "source": "北京本地宝", "highlights": ["策展人", "展览筹备", "实践"], "type": "亲子活动"},
    {"name": "我是文物守护者", "venue": "香山革命纪念馆", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "馆内文物专家一对一导师带教，开展藏品拍照、档案编目、资料整理等实操。", "source": "北京本地宝", "highlights": ["文物保护", "导师带教", "实践"], "type": "亲子活动"},
    {"name": "赶考讲堂系列讲座", "venue": "香山革命纪念馆", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "7月-8月每周1场，邀请中央党史和文献研究院、中国国家博物馆等知名专家进行专题授课。", "source": "北京本地宝", "highlights": ["讲座", "党史", "专家"], "type": "讲座"},
    {"name": "赶考主题互动答题", "venue": "香山革命纪念馆", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "线上开发H5答题小程序，以'收集历史档案碎片'为主线，覆盖7处红色点位，集齐碎片可解锁专属'新时代赶考档案'。", "source": "北京本地宝", "highlights": ["答题", "互动", "H5"], "type": "亲子活动"},
    {"name": "文物证史集章打卡", "venue": "香山革命纪念馆", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "推出4款馆藏革命文物主题纪念印章，关注微信公众号即可免费领取卡片并加盖纪念印章。", "source": "北京本地宝", "highlights": ["集章", "打卡", "文物"], "type": "亲子活动"},
    {"name": "国家博物馆夏令营", "venue": "中国国家博物馆", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "包含'古代中国·通史'和'古代中国·通识'两大主题，共24门课程，围绕非遗传承、科技发明、艺术之美等展开。", "source": "北京本地宝", "highlights": ["国博", "夏令营", "通史"], "type": "亲子活动"},
    {"name": "故宫深度研学", "venue": "故宫博物院", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "专业研学团讲解神兽故事、皇家趣事，包含'在故宫讲文物'、学习榫卯结构等任务。", "source": "北京本地宝", "highlights": ["故宫", "研学", "榫卯"], "type": "亲子活动"},
    {"name": "天坛建筑探秘", "venue": "天坛公园", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "化身'建筑小侦探'，了解皇家建筑奥秘和回音壁声学奇迹。", "source": "北京本地宝", "highlights": ["天坛", "建筑", "声学"], "type": "亲子活动"},
    {"name": "胡同文化探索", "venue": "老北京胡同", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "走进老北京胡同逗蝈蝈、逛四合院，体验地道京味儿生活。", "source": "北京本地宝", "highlights": ["胡同", "四合院", "京味儿"], "type": "亲子活动"},
    {"name": "航天科技主题营", "venue": "中华航天博物馆", "city": "beijing", "district": "丰台区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "包含中华航天博物馆、北京航空航天大学、火箭超级工厂等，近距离接触火箭制造全过程。", "source": "北京本地宝", "highlights": ["航天", "火箭", "科技"], "type": "亲子活动"},
    {"name": "AI智能体创作", "venue": "门头沟京西研途", "city": "beijing", "district": "门头沟区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "通过扣子平台实操完成智能体创作，培养数字素养和科技创新能力。", "source": "北京本地宝", "highlights": ["AI", "智能体", "创作"], "type": "亲子活动"},
    {"name": "百花山生态研学", "venue": "百花山", "city": "beijing", "district": "门头沟区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "在登山中认识金莲花等高山植物，学习海拔梯度对植被的影响。", "source": "北京本地宝", "highlights": ["百花山", "生态", "植物"], "type": "亲子活动"},
    {"name": "星光植趣夜", "venue": "世界花卉大观园", "city": "beijing", "district": "丰台区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "夜探植物馆，包括DIY小夜灯、花钟探险、花果实验室等环节。", "source": "北京本地宝", "highlights": ["夜探", "植物", "DIY"], "type": "亲子活动"},
    {"name": "农耕文明研学", "venue": "门头沟谷山村", "city": "beijing", "district": "门头沟区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "融合农耕溯源、《诗经》植物科普、非遗体验与农事劳动，如独轮车运种、古法石磨做豆腐。", "source": "北京本地宝", "highlights": ["农耕", "非遗", "农事"], "type": "亲子活动"},
    {"name": "北大清华校园参访", "venue": "北京大学", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "走进北大未名湖、清华校园，感受名校氛围，听学霸分享学习经验。", "source": "北京本地宝", "highlights": ["名校", "参访", "励志"], "type": "亲子活动"},
    {"name": "北海公园夜游", "venue": "北海公园", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "印·静心夜游活动，在星光与灯火中感受园林的别样韵味。", "source": "北京本地宝", "highlights": ["夜游", "北海", "园林"], "type": "演出"},
    {"name": "香山奇妙夜", "venue": "香山公园", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "夜间体验项目，在星光与灯火中感受山林的静谧与神秘。", "source": "北京本地宝", "highlights": ["夜游", "香山", "山林"], "type": "演出"},
    {"name": "世园之夜消夏", "venue": "北京世园公园", "city": "beijing", "district": "延庆区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "消夏避暑季，配套夜间市集与露营餐饮服务。", "source": "北京本地宝", "highlights": ["世园", "消夏", "露营"], "type": "演出"},
    {"name": "晋国霸业文物展", "venue": "颐和园博物馆", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "山西出土两周时期文物精华展，让历史与艺术在园林中对话。", "source": "北京本地宝", "highlights": ["晋国", "文物", "展览"], "type": "展览"},
    {"name": "红山文化专题展", "venue": "天坛公园", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "文明溯源——牛河梁红山文化专题展，展现中华文明起源。", "source": "北京本地宝", "highlights": ["红山文化", "文明起源", "展览"], "type": "展览"},
    {"name": "荷间音画音乐会", "venue": "紫竹院公园", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "晚间音乐会，笛箫演奏家带来经典民乐曲目。", "source": "北京本地宝", "highlights": ["音乐会", "荷花", "民乐"], "type": "演出"},
    {"name": "湖畔琴韵音乐会", "venue": "玉渊潭公园", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "湖畔音乐会，让音乐与湖光夜色交相辉映。", "source": "北京本地宝", "highlights": ["音乐会", "湖畔", "夜色"], "type": "演出"},
    {"name": "湖光情歌七夕专场", "venue": "玉渊潭公园", "city": "beijing", "district": "海淀区", "start_date": "2026-08-20", "end_date": "2026-08-20", "fee": "免费", "description": "七夕专场音乐会，湖光情歌 鹊桥相会。", "source": "北京本地宝", "highlights": ["七夕", "音乐会", "情歌"], "type": "演出"},
    {"name": "大树音乐会", "venue": "广阳谷城市森林公园", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "每周日举办'大树音乐会'，让艺术走出传统剧场。", "source": "北京本地宝", "highlights": ["音乐会", "森林公园", "户外"], "type": "演出"},
    {"name": "百名青年演员公园行", "venue": "天坛公园", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "近百名青年演员齐聚公园，推出主题音乐会、民族音乐会、儿童艺术剧、舞剧派对等。", "source": "北京本地宝", "highlights": ["青年演员", "公园演出", "公益"], "type": "演出"},
    {"name": "玉渡山亲子乐园", "venue": "玉渡山", "city": "beijing", "district": "延庆区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "高山草甸、忘忧湖、林间步道与清凉溪流交织成天然游乐场。", "source": "北京本地宝", "highlights": ["玉渡山", "亲子", "自然"], "type": "亲子活动"},
    {"name": "野鸭湖观鸟", "venue": "野鸭湖", "city": "beijing", "district": "延庆区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "自然空调房，观鸟、漫步、骑行，是低强度遛娃的理想之选。", "source": "北京本地宝", "highlights": ["野鸭湖", "观鸟", "自然"], "type": "亲子活动"},
    # ========== 广州补充活动 ==========
    {"name": "黔红迹寻踪五脉汇心", "venue": "中共三大会址纪念馆", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "依托地铁串联五大红色核心片区，从中共三大会址到农讲所、烈士陵园，全程步行平缓。", "source": "广州本地宝", "highlights": ["红色", "五脉汇心", "徒步"], "type": "亲子活动"},
    {"name": "中轴揽胜都市文化", "venue": "广州塔", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "从海心桥启程，登广州塔俯瞰城市全貌，走进广州艺术博物院，漫步海珠国家湿地公园。", "source": "广州本地宝", "highlights": ["广州塔", "都市文化", "研学"], "type": "亲子活动"},
    {"name": "岛藏风云一岛百年", "venue": "黄埔军校旧址纪念馆", "city": "guangzhou", "district": "黄埔区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "在黄埔军校回望将帅摇篮的峥嵘岁月，于辛亥革命纪念馆感受觉醒年代。", "source": "广州本地宝", "highlights": ["黄埔军校", "辛亥革命", "历史"], "type": "亲子活动"},
    {"name": "文脉逢夏匠心手作", "venue": "沙湾古镇", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "在沙湾古镇体验传统开笔礼，探访红木古典家具馆拆解榫卯结构。", "source": "广州本地宝", "highlights": ["沙湾古镇", "榫卯", "非遗"], "type": "亲子活动"},
    {"name": "薪火流溪红色溯源", "venue": "黄沙坑革命旧址", "city": "guangzhou", "district": "从化区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "探访黄沙坑革命旧址重温东江纵队抗战岁月，体验车步社古法造纸。", "source": "广州本地宝", "highlights": ["红色", "古法造纸", "溯源"], "type": "亲子活动"},
    {"name": "云山叠翠绿意漫行", "venue": "白云山", "city": "guangzhou", "district": "白云区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "登顶羊城第一秀，漫步云萝与云溪，走进神农草堂的药草园林。", "source": "广州本地宝", "highlights": ["白云山", "自然", "中医药"], "type": "亲子活动"},
    {"name": "帽峰闻香氧吧疗愈", "venue": "帽峰山", "city": "guangzhou", "district": "白云区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "钻进主峰的森林秘境，在负离子爆棚的天然氧吧里洗肺登高。", "source": "广州本地宝", "highlights": ["帽峰山", "氧吧", "疗愈"], "type": "亲子活动"},
    {"name": "湿地探奇自然课堂", "venue": "南沙湿地", "city": "guangzhou", "district": "南沙区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "乘红树林游船穿行湿地，登观鸟塔远眺候鸟翩跹，在植物拓印中收藏自然的纹理。", "source": "广州本地宝", "highlights": ["湿地", "观鸟", "自然"], "type": "亲子活动"},
    {"name": "亚欧五百年艺术对话", "venue": "广东省博物馆", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-10-18", "fee": "收费", "description": "近70件格拉斯哥博物馆珍藏真迹首次集中亮相，总估值接近10亿元，特别加入郎世宁画作作为中西艺术对照。", "source": "广州本地宝", "highlights": ["艺术", "欧洲", "展览"], "type": "展览"},
    {"name": "MR巨鲸数字艺术展", "venue": "香港科技大学（广州）", "city": "guangzhou", "district": "南沙区", "start_date": "2026-07-01", "end_date": "2026-07-31", "fee": "免费", "description": "全球首个大型MR×AI艺术展，戴上MR眼镜，虚拟巨鲸、奇幻建筑在现实空间中穿梭游走。", "source": "广州本地宝", "highlights": ["MR", "数字艺术", "沉浸式"], "type": "展览"},
    {"name": "声光电互动艺术展", "venue": "时尚天河", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "以'万物循环'为核心理念，通过人体感应触发光影与音效变化。", "source": "广州本地宝", "highlights": ["声光电", "互动", "艺术"], "type": "展览"},
    {"name": "甲虫王国科普展", "venue": "广东省博物馆", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-17", "end_date": "2026-10-18", "fee": "免费", "description": "展出大量珍稀甲虫标本、昆虫主题少儿绘画作品，搭配多媒体互动装置。", "source": "广州本地宝", "highlights": ["甲虫", "科普", "互动"], "type": "展览"},
    {"name": "儿童公共艺术季", "venue": "广东美术馆", "city": "guangzhou", "district": "越秀区", "start_date": "2026-06-29", "end_date": "2026-09-13", "fee": "免费", "description": "聚焦自然美育主题，展出多所城乡学校师生共创的艺术作品。", "source": "广州本地宝", "highlights": ["儿童艺术", "美育", "展览"], "type": "展览"},
    {"name": "三丽鸥海岛快闪", "venue": "天河城", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "三丽鸥家族全员换上晒黑海岛造型，椰林沙滩主题场景满满夏日氛围。", "source": "广州本地宝", "highlights": ["三丽鸥", "快闪", "亲子"], "type": "展览"},
    {"name": "广州市文化馆暑期美育", "venue": "广州市文化馆", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "馆内一站式配齐多样美育课堂，观赏精美展览、体验器乐舞蹈，研习摄影、美妆、AI技能。", "source": "广州本地宝", "highlights": ["文化馆", "美育", "课堂"], "type": "讲座"},
    {"name": "沙湾古镇开笔礼", "venue": "沙湾古镇", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "传统开笔礼仪式，让孩子感受传统文化的庄重与美好。", "source": "广州本地宝", "highlights": ["开笔礼", "传统文化", "仪式"], "type": "亲子活动"},
    {"name": "黄埔古港研学", "venue": "黄埔古港", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "了解广州海上丝绸之路历史，参观古码头和古祠堂。", "source": "广州本地宝", "highlights": ["黄埔古港", "海上丝路", "历史"], "type": "亲子活动"},
    {"name": "广州动物园科普日", "venue": "广州动物园", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "动物科普讲解、喂食体验、亲子互动等暑期活动。", "source": "广州本地宝", "highlights": ["动物园", "科普", "亲子"], "type": "亲子活动"},
    {"name": "华南植物园自然课堂", "venue": "华南植物园", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "植物识别、昆虫观察、生态保护等主题活动，每周六日举办。", "source": "广州本地宝", "highlights": ["植物园", "自然课堂", "亲子"], "type": "亲子活动"},
    # ========== 上海补充活动 ==========
    {"name": "上海地铁博物馆", "venue": "上海地铁博物馆", "city": "shanghai", "district": "闵行区", "start_date": "2026-07-15", "end_date": "2026-12-31", "fee": "免费", "description": "中国第一家展示城市轨道交通发展历程的专业展馆，包括文献档案、隧道行走、模拟驾驶、虚拟列车DIY等。", "source": "上海本地宝", "highlights": ["地铁", "博物馆", "互动"], "type": "展览"},
    {"name": "世界树之境植物展", "venue": "上海温室花园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-11-14", "fee": "收费", "description": "凤梨做的羊驼母子、300多种美洲植物、30种难得一见的龙舌兰，与上海博物馆美洲古代文明大展深度联动。", "source": "上海本地宝", "highlights": ["植物", "美洲", "展览"], "type": "展览"},
    {"name": "花样年华音乐电影场", "venue": "西岸梦中心", "city": "shanghai", "district": "徐汇区", "start_date": "2026-07-15", "end_date": "2026-07-15", "fee": "免费", "description": "上海RJ爵士大乐团现场演奏电影主题曲，再看一场浪漫电影。", "source": "上海本地宝", "highlights": ["电影", "音乐会", "浪漫"], "type": "演出"},
    {"name": "申园纳夏凉园林消夏录", "venue": "世博文化公园申园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "市区江南古典园林，满池荷花盛放，汉服租赁游园、古法消夏手作、夜间园林雅集。", "source": "上海本地宝", "highlights": ["申园", "荷花", "汉服"], "type": "亲子活动"},
    {"name": "古猗园荷花展", "venue": "古猗园", "city": "shanghai", "district": "嘉定区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "第十三届荷花睡莲展，上百种珍稀荷花品种集中盛放，非遗荷文化研学。", "source": "上海本地宝", "highlights": ["荷花展", "古猗园", "非遗"], "type": "展览"},
    {"name": "豫园非遗体验", "venue": "豫园", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "糖画、面人、木版水印、皮影戏循环上演，老城厢研学路线。", "source": "上海本地宝", "highlights": ["豫园", "非遗", "研学"], "type": "亲子活动"},
    {"name": "朱家角古镇艺韵江南", "venue": "朱家角古镇", "city": "shanghai", "district": "青浦区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "36座明清石桥串联水乡河道，河道边每日有古琴、昆曲、江南评弹公益演出。", "source": "上海本地宝", "highlights": ["朱家角", "古镇", "昆曲"], "type": "亲子活动"},
    {"name": "枫泾古镇寻根", "venue": "枫泾古镇", "city": "shanghai", "district": "金山区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "吴越交汇之地，体验传统手工艺、品尝特色小吃。", "source": "上海本地宝", "highlights": ["枫泾", "古镇", "美食"], "type": "亲子活动"},
    {"name": "辰山植物园科普", "venue": "辰山植物园", "city": "shanghai", "district": "松江区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "大面积树荫、矿坑湖泊，科普植物生长知识，树荫下野餐露营。", "source": "上海本地宝", "highlights": ["植物园", "科普", "露营"], "type": "亲子活动"},
    {"name": "滨江森林公园", "venue": "滨江森林公园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "滨江步道、森林氧吧、湿地观鸟，适合亲子徒步和野餐。", "source": "上海本地宝", "highlights": ["滨江", "森林", "自然"], "type": "亲子活动"},
    {"name": "奉贤庄行采摘", "venue": "奉贤庄行田园", "city": "shanghai", "district": "奉贤区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "采摘基地+伏羊美食嘉年华，品尝非遗伏羊汤，感受江南三伏天食俗。", "source": "上海本地宝", "highlights": ["采摘", "美食", "非遗"], "type": "亲子活动"},
    {"name": "上海天文馆邂逅星空", "venue": "上海天文馆", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-04", "end_date": "2026-08-30", "fee": "收费", "description": "夜间观星活动，使用专业天文望远镜观测星空。", "source": "上海本地宝", "highlights": ["天文馆", "星空", "观测"], "type": "亲子活动"},
    {"name": "上海儿童博物馆", "venue": "上海儿童博物馆", "city": "shanghai", "district": "长宁区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "专为儿童设计的博物馆，包含航天馆、航海馆、玩具馆等。", "source": "上海本地宝", "highlights": ["儿童博物馆", "航天", "玩具"], "type": "展览"},
    {"name": "上海昆虫博物馆", "venue": "上海昆虫博物馆", "city": "shanghai", "district": "徐汇区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "展出各类昆虫标本，了解昆虫世界的奥秘。", "source": "上海本地宝", "highlights": ["昆虫", "博物馆", "科普"], "type": "展览"},
    {"name": "上海邮政博物馆", "venue": "上海邮政博物馆", "city": "shanghai", "district": "虹口区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "展示上海邮政发展历史，有老式邮筒、邮车等实物展示。", "source": "上海本地宝", "highlights": ["邮政", "博物馆", "历史"], "type": "展览"},
    {"name": "上海铁路博物馆", "venue": "上海铁路博物馆", "city": "shanghai", "district": "静安区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "展示中国铁路发展历程，有蒸汽机车等实物展示。", "source": "上海本地宝", "highlights": ["铁路", "博物馆", "历史"], "type": "展览"},
    {"name": "上海电信博物馆", "venue": "上海电信博物馆", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "展示电信发展历史，有老式电话机、电报机等实物展示。", "source": "上海本地宝", "highlights": ["电信", "博物馆", "历史"], "type": "展览"},
    {"name": "上海银行博物馆", "venue": "上海银行博物馆", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "展示银行发展历史，有古代货币、近代票据等实物展示。", "source": "上海本地宝", "highlights": ["银行", "博物馆", "历史"], "type": "展览"},
    {"name": "上海消防博物馆", "venue": "上海消防博物馆", "city": "shanghai", "district": "长宁区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "展示消防发展历史，有老式消防车、消防器材等实物展示。", "source": "上海本地宝", "highlights": ["消防", "博物馆", "科普"], "type": "展览"},
    {"name": "上海中医药博物馆", "venue": "上海中医药博物馆", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "展示中医药发展历史，有中草药标本、古代医疗器械等展示。", "source": "上海本地宝", "highlights": ["中医药", "博物馆", "科普"], "type": "展览"},
    # ========== 杭州补充活动 ==========
    {"name": "寒武纪化石展", "venue": "浙江自然博物院", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-06-01", "end_date": "2026-08-31", "fee": "免费", "description": "展出三叶虫、鱼龙、猛犸象化石骨架，6-8月整期开放。", "source": "杭州本地宝", "highlights": ["化石", "寒武纪", "展览"], "type": "展览"},
    {"name": "李家化石守护者", "venue": "建德李家镇", "city": "hangzhou", "district": "建德市", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "拿起地质锤在真实地质剖面敲出菊石，走进实验室用显微镜和剔针亲手修复化石。", "source": "杭州本地宝", "highlights": ["化石", "科考", "地质"], "type": "亲子活动"},
    {"name": "少年AI指挥官", "venue": "阿里巴巴全球总部", "city": "hangzhou", "district": "余杭区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "五日科技营，从AI通识课到AI创意实操，完整经历'从认知到创造'的科技之旅。", "source": "杭州本地宝", "highlights": ["AI", "科技营", "阿里"], "type": "亲子活动"},
    {"name": "五八智能科技探索", "venue": "五八智能", "city": "hangzhou", "district": "余杭区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "近距离观摩机器狗全地形实战测试，与军工工程师对话，动手拼装遥控机械狗。", "source": "杭州本地宝", "highlights": ["机器狗", "科技", "探索"], "type": "亲子活动"},
    {"name": "数字杭州科技筑梦", "venue": "吉利汽车生产基地", "city": "hangzhou", "district": "滨江区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "两日营，参观自动化整车生产线、学习汽车工业知识并体验无人机操作。", "source": "杭州本地宝", "highlights": ["吉利", "汽车", "科技"], "type": "亲子活动"},
    {"name": "千岛湖赛艇夏令营", "venue": "千岛湖国家水上训练中心", "city": "hangzhou", "district": "淳安县", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "由世界冠军/亚运冠军领衔执教，在国家队标准航道里挥桨破浪。", "source": "杭州本地宝", "highlights": ["赛艇", "夏令营", "冠军"], "type": "亲子活动"},
    {"name": "千岛逐风四日营", "venue": "千岛湖", "city": "hangzhou", "district": "淳安县", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "体验帆船运动、环湖绿道骑行、高空挑战，夜晚有《水之灵》实景演出。", "source": "杭州本地宝", "highlights": ["千岛湖", "帆船", "骑行"], "type": "亲子活动"},
    {"name": "最忆是杭州吴越营", "venue": "浙江省博物馆", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "三日营，探秘吴越文物和良渚玉器，西湖泛舟并开展塔影写生，了解钱镠'保境安民'功绩。", "source": "杭州本地宝", "highlights": ["吴越", "良渚", "西湖"], "type": "亲子活动"},
    {"name": "梅家坞茶文化", "venue": "梅家坞", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "换上汉服、背起茶篓，体验采茶炒茶全过程，还能选择扎染、点茶等传统手工艺项目。", "source": "杭州本地宝", "highlights": ["茶文化", "采茶", "非遗"], "type": "亲子活动"},
    {"name": "西湖小茶人三日营", "venue": "西湖博物馆", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "从博物馆到茶山，学习茶文化知识，体验采茶制茶。", "source": "杭州本地宝", "highlights": ["茶文化", "西湖", "研学"], "type": "亲子活动"},
    {"name": "动物园奇妙夜", "venue": "杭州动物园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "夜间探访动物园，观察动物夜间行为，体验不一样的动物世界。", "source": "杭州本地宝", "highlights": ["动物园", "夜场", "奇妙夜"], "type": "亲子活动"},
    {"name": "胡府夜游", "venue": "胡雪岩旧居", "city": "hangzhou", "district": "上城区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "胡雪岩旧居首开夜游活动，沉浸式体验清代豪宅的夜景魅力。", "source": "杭州本地宝", "highlights": ["胡雪岩", "夜游", "清代"], "type": "演出"},
    {"name": "湖山之约金石之美", "venue": "西湖博物馆", "city": "hangzhou", "district": "西湖区", "start_date": "2026-06-24", "end_date": "2026-09-30", "fee": "免费", "description": "金石篆刻艺术展览，感受传统艺术之美。", "source": "杭州本地宝", "highlights": ["金石", "篆刻", "展览"], "type": "展览"},
    {"name": "九溪烟树溯溪", "venue": "九溪烟树", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "夏日清凉自然体验，在溪水中嬉戏玩耍。", "source": "杭州本地宝", "highlights": ["九溪", "溯溪", "清凉"], "type": "亲子活动"},
    {"name": "龙井村茶园徒步", "venue": "龙井村", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "漫步茶园，了解茶文化，品尝龙井茶。", "source": "杭州本地宝", "highlights": ["龙井", "茶园", "徒步"], "type": "亲子活动"},
    {"name": "茅家埠小众徒步", "venue": "茅家埠", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "人少景美的西湖小众区域，适合亲子徒步和野餐。", "source": "杭州本地宝", "highlights": ["茅家埠", "小众", "徒步"], "type": "亲子活动"},
    {"name": "低碳科技馆", "venue": "杭州低碳科技馆", "city": "hangzhou", "district": "滨江区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "互动项目丰富，人相对少，适合亲子科普体验。", "source": "杭州本地宝", "highlights": ["低碳", "科技馆", "科普"], "type": "展览"},
    {"name": "中国丝绸博物馆", "venue": "中国丝绸博物馆", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "展示中国丝绸发展历史，有古代丝绸服饰、织机等实物展示。", "source": "杭州本地宝", "highlights": ["丝绸", "博物馆", "历史"], "type": "展览"},
    {"name": "武林门码头水上巴士", "venue": "武林门码头", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "乘坐水上巴士游览运河，感受杭州水上交通文化。", "source": "杭州本地宝", "highlights": ["水上巴士", "运河", "游览"], "type": "亲子活动"},
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
    for city, count in city_counts.items():
        print(f"  {city}: {count}")