import json

activities = []

# ============================================
# 1. 博物馆/纪念馆特展与活动
# ============================================

activities.append({
    "title": "俑见大唐——长安荔枝路中的盛世风华特展",
    "venue": "西安大唐西市博物馆艺术品中心",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-10-31",
    "link": "http://www.dtxsmuseum.com/news_show.aspx?id=1460",
    "description": "以馆藏彩绘侍女俑视角，聚焦大唐荔枝路特展，展出八十余件精美文物，其中80%首次展出，含三彩马、彩绘戏童女立俑、彩绘胡人牵猞猁骑马俑等珍品，现场可体验唐三彩制作。",
    "fee": "收费",
    "source": "西安大唐西市博物馆官网",
    "family_friendly": True
})

activities.append({
    "title": "西影电影博物馆追光夜",
    "venue": "西影电影博物馆",
    "city": "xian",
    "start_date": "2026-07-11",
    "end_date": "2026-08-30",
    "link": "http://m.toutiao.com/group/7663083850490249779/",
    "description": "暑期每晚17:30开启博物馆夜场，九大NPC全员巡游互动，沉浸式夜游、XR电影多元体验，还有快闪秀、集体定格大片等活动，适合亲子家庭感受电影文化魅力。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "陕西唐三彩艺术博物馆数字化公益体验",
    "venue": "陕西唐三彩艺术博物馆",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663083850490249779/",
    "description": "参与博物馆数字化公益活动，成为数字守艺人，通过手机扫码、拍照等方式体验文物数字化，光影秀让唐三彩文物活起来，适合亲子家庭了解科技与文化的融合。",
    "fee": "免费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "大明宫考古探索中心暑期研学",
    "venue": "大明宫国家遗址公园考古探索中心",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663083850490249779/",
    "description": "五大主题展厅致敬考古人、铲释地书、宫阙万千、大明宫印象、梦回大唐，五大模拟探方实景沉浸式挖宝，可亲手发掘仿真文物碎片，学习考古知识。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "昭陵博物馆唐代壁画文博沙龙",
    "venue": "西安城墙永宁门箭楼",
    "city": "xian",
    "start_date": "2026-07-13",
    "end_date": "2026-07-13",
    "link": "http://m.toutiao.com/group/7663083850490249779/",
    "description": "文脉千秋·博物馆奇妙季首场重磅活动，昭陵博物馆专家解读初唐服饰礼制、仪仗风貌与乐舞人文，深入浅出讲述唐代壁画背后的历史故事，适合亲子家庭。",
    "fee": "免费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "昭陵壁画光影秀——《梦长安——大唐迎宾盛礼》",
    "venue": "西安城墙永宁门",
    "city": "xian",
    "start_date": "2026-07-14",
    "end_date": "2026-07-19",
    "link": "http://m.toutiao.com/group/7663083850490249779/",
    "description": "昭陵博物馆馆藏文物影像融入大唐迎宾盛礼实景演艺，永宁门冰屏滚动播放唐代壁画高清影像，瓮城墙体化身巨型光影画布，现代光影技术复刻唐画风貌。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "昭陵文物免费文博宣讲专场",
    "venue": "西安城墙和平门13号敌楼文化展馆",
    "city": "xian",
    "start_date": "2026-07-18",
    "end_date": "2026-07-18",
    "link": "http://m.toutiao.com/group/7663083850490249779/",
    "description": "昭陵博物馆专业讲解员现场解读壁画、陶俑、碑石等珍贵文物知识，市民游客在游览中读懂长安历史，践行主客共享的文旅服务理念。",
    "fee": "免费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "行走的历史课——汉阳陵+陕历博+城墙研学路线",
    "venue": "汉景帝阳陵博物院、陕西历史博物馆、西安城墙",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://sxggwhy.com/news/detail?id=68552918e25ad2452909e96e",
    "description": "一日穿越千年研学路线，上午汉阳陵探方考古体验，下午陕历博寻宝任务卡寻找镶金兽首玛瑙杯等国宝，傍晚西安城墙骑行漫步，沉浸式感受历史温度。",
    "fee": "收费",
    "source": "陕西省文旅厅",
    "family_friendly": True
})

# ============================================
# 2. 科技馆/科普场馆活动
# ============================================

activities.append({
    "title": "探秘数学之美——小小科学家亲子活动",
    "venue": "西安文理学院数学探索馆",
    "city": "xian",
    "start_date": "2026-08-16",
    "end_date": "2026-08-16",
    "link": "https://www.xakpw.com/single/36902",
    "description": "西安市科学技术馆联合西安文理学院举办，20组亲子家庭参与，500余件数学教具环绕，密铺大挑战、拓扑变形装置、概率游戏等互动体验，触摸数学玩转艺术。",
    "fee": "免费需预约",
    "source": "西安市科学技术馆官网",
    "family_friendly": True
})

activities.append({
    "title": "西安科技馆科趣夜场活动",
    "venue": "西安科技馆（长安云）",
    "city": "xian",
    "start_date": "2026-07-07",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7526116292928209454/",
    "description": "暑期每周五、周六17:00-20:30增设主题夜场，7个常设展厅近400件沉浸式互动展品，科学探究、硬核力量、逐梦空天、生命健康、科学童梦园等区域畅玩。",
    "fee": "免费需预约",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "西安科技馆暑期两周仅闭馆一次开放政策",
    "venue": "西安科技馆（长安云）",
    "city": "xian",
    "start_date": "2026-07-07",
    "end_date": "2026-08-30",
    "link": "http://m.toutiao.com/group/7526116292928209454/",
    "description": "暑期实行两周仅闭馆一次的开放政策，5.9万㎡超级造梦空间，球幕影院、4D影院影片上新，奥秘秀场、机器人核心危机互动剧场，百余场主题活动。",
    "fee": "免费需预约",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "西安综合减灾科普馆参观体验",
    "venue": "西安综合减灾科普馆",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-12-31",
    "link": "http://news.qq.com/rain/a/20250807A08OF400",
    "description": "共三层约12000平方米，有序厅、灾害科普区、儿童区、公共安全区、4D影院、应急演练培训区等区域，适合亲子家庭学习防灾减灾知识。",
    "fee": "免费需预约",
    "source": "西安本地宝",
    "family_friendly": True
})

activities.append({
    "title": "中国秦腔艺术博物馆互动体验",
    "venue": "中国秦腔艺术博物馆",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-12-31",
    "link": "http://news.qq.com/rain/a/20250807A08OF400",
    "description": "真人比例经典戏曲人物、珍贵戏曲文献和音像资料，互动触摸显示屏近距离与秦腔艺术互动，边玩边了解秦腔，适合亲子家庭感受传统戏曲文化。",
    "fee": "免费需预约",
    "source": "西安本地宝",
    "family_friendly": True
})

activities.append({
    "title": "国际口腔医学博物馆参观",
    "venue": "国际口腔医学博物馆",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-12-31",
    "link": "http://news.qq.com/rain/a/20250807A08OF400",
    "description": "来自世界30余个国家的7800余件展品，18个展区，从远古动物牙颌化石到现代牙科诊疗器械一应俱全，适合亲子家庭了解口腔医学知识。",
    "fee": "免费",
    "source": "西安本地宝",
    "family_friendly": True
})

activities.append({
    "title": "科学你好AI！——小小侦探探秘智能未来课程",
    "venue": "陕西科技馆科学工作室",
    "city": "xian",
    "start_date": "2026-07-05",
    "end_date": "2026-08-31",
    "link": "https://www.ishaanxi.com/c/2025/0709/3462671.shtml",
    "description": "陕西科技馆暑期三秦筑梦智燃盛夏主题活动，青少年体验图像识别、语音交互等AI技术，了解人工智能原理，激发科学兴趣。",
    "fee": "免费需预约",
    "source": "陕西网",
    "family_friendly": True
})

activities.append({
    "title": "流动的力量——伯努利原理的奇妙世界课程",
    "venue": "陕西科技馆科学工作室",
    "city": "xian",
    "start_date": "2026-07-05",
    "end_date": "2026-08-31",
    "link": "https://www.ishaanxi.com/c/2025/0709/3462671.shtml",
    "description": "揭秘伯努利原理，通过有趣的科学实验展现物理定律的神奇，让孩子们在动手实践中理解流体力学知识，培养科学思维。",
    "fee": "免费需预约",
    "source": "陕西网",
    "family_friendly": True
})

activities.append({
    "title": "布里藏奇趣——非遗扎染的魔法创想活动",
    "venue": "陕西科技馆科学工作室",
    "city": "xian",
    "start_date": "2026-07-05",
    "end_date": "2026-08-31",
    "link": "https://www.ishaanxi.com/c/2025/0709/3462671.shtml",
    "description": "结合传统扎染技艺实践，激发艺术创造力，增进对非物质文化遗产的热爱，在科学与艺术的交融中体验传统文化魅力。",
    "fee": "免费需预约",
    "source": "陕西网",
    "family_friendly": True
})

activities.append({
    "title": "一捧陶土——手塑生活的温度美学活动",
    "venue": "陕西科技馆科学工作室",
    "city": "xian",
    "start_date": "2026-07-05",
    "end_date": "2026-08-31",
    "link": "https://www.ishaanxi.com/c/2025/0709/3462671.shtml",
    "description": "陶艺制作体验活动，亲手塑造陶土作品，感受传统陶艺魅力，培养动手能力和艺术审美，适合亲子家庭共同参与。",
    "fee": "免费需预约",
    "source": "陕西网",
    "family_friendly": True
})

activities.append({
    "title": "数字赋能AI特色活动——AI与生活主题",
    "venue": "陕西科技馆",
    "city": "xian",
    "start_date": "2026-07-05",
    "end_date": "2026-08-31",
    "link": "https://www.ishaanxi.com/c/2025/0709/3462671.shtml",
    "description": "引导学生掌握生成式AI工具，感受科技进步为生活带来的切实便利，了解AI在日常生活中的应用场景。",
    "fee": "免费需预约",
    "source": "陕西网",
    "family_friendly": True
})

activities.append({
    "title": "智创未来·科玩一夏科学体验活动",
    "venue": "陕西科技馆常设展厅",
    "city": "xian",
    "start_date": "2026-07-05",
    "end_date": "2026-08-31",
    "link": "https://www.ishaanxi.com/c/2025/0709/3462671.shtml",
    "description": "深度挖掘展品科学内涵，打造探究性与沉浸感兼具的科普体验，通过互动实验让孩子们在玩中学科学知识。",
    "fee": "免费需预约",
    "source": "陕西网",
    "family_friendly": True
})

# ============================================
# 3. 图书馆活动
# ============================================

activities.append({
    "title": "从书本到世界名师领读计划",
    "venue": "西安图书馆少儿服务区",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7531595343558001188/",
    "description": "针对6至12岁孩子认知特点，精选《童年》《十万个为什么》等经典绘本与图书，名师带领深度阅读，培养阅读兴趣与能力。",
    "fee": "免费",
    "source": "人民网",
    "family_friendly": True
})

activities.append({
    "title": "萌眼观影·童梦盛宴经典放映活动",
    "venue": "西安图书馆彩虹剧场",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7531595343558001188/",
    "description": "近百部高分动画与科普影片放映，暑期每日多场，让孩子们在光影中放飞童年梦想，学习科普知识。",
    "fee": "免费",
    "source": "人民网",
    "family_friendly": True
})

activities.append({
    "title": "书田伴读第四季——共读《宝葫芦的秘密》",
    "venue": "陕西省图书馆高新馆区少年儿童馆一楼小剧场",
    "city": "xian",
    "start_date": "2026-08-30",
    "end_date": "2026-09-04",
    "link": "https://www.sxlib.org.cn/wap/hd/hdyg/202508/t20250829_1163014.html",
    "description": "一天线下导读加六天线上伴读，20组亲子家庭参与，深入解读张天翼经典童话，掌握思维导图阅读方法，适合6-12岁儿童。",
    "fee": "免费需预约",
    "source": "陕西省图书馆官网",
    "family_friendly": True
})

activities.append({
    "title": "双语阅读·带着绘本去旅行系列分享课程",
    "venue": "陕西省图书馆一楼多功能厅（长安路馆区）",
    "city": "xian",
    "start_date": "2026-08-03",
    "end_date": "2026-08-06",
    "link": "https://www.sxlib.org.cn/wap/hd/hdyg/202507/t20250730_1161791.html",
    "description": "学在陕图公益课堂，四天课程带你环游世界，从澳大利亚到大堡礁，从英语阅读到动手实践，认识地球多样性，适合儿童英语启蒙。",
    "fee": "免费需预约",
    "source": "陕西省图书馆官网",
    "family_friendly": True
})

activities.append({
    "title": "《小猪变形记》绘本阅读交流课",
    "venue": "西安图书馆小荷成长空间",
    "city": "xian",
    "start_date": "2026-07-11",
    "end_date": "2026-07-11",
    "link": "https://m.sohu.com/a/911993619_121106869/",
    "description": "自主阅读公益课，陕西省教学能手许本鑫老师主讲，通过经典绘本培养孩子自我价值认知，适合5-11岁热爱阅读的学生及家长。",
    "fee": "免费需预约",
    "source": "西安图书馆",
    "family_friendly": True
})

activities.append({
    "title": "打造儿童自主阅读能力的实践策略讲座",
    "venue": "西安图书馆小荷成长空间",
    "city": "xian",
    "start_date": "2026-07-11",
    "end_date": "2026-07-11",
    "link": "https://m.sohu.com/a/911993619_121106869/",
    "description": "自主阅读公益讲座，分享培养孩子自主阅读能力的实用方法，帮助家长建立科学的阅读教育理念。",
    "fee": "免费需预约",
    "source": "西安图书馆",
    "family_friendly": True
})

activities.append({
    "title": "从害怕失败到不怕试错——成长型思维培养讲座",
    "venue": "西安图书馆小荷成长空间",
    "city": "xian",
    "start_date": "2026-07-13",
    "end_date": "2026-07-13",
    "link": "https://m.sohu.com/a/911993619_121106869/",
    "description": "3-9岁成长型思维培养课，用科学方法和实用技巧帮助孩子打破恐惧枷锁，把我不行变成我能行，建议亲子共同参与。",
    "fee": "免费需预约",
    "source": "西安图书馆",
    "family_friendly": True
})

activities.append({
    "title": "童享非遗话传承——烧箔画体验活动",
    "venue": "西安市雁塔区图书馆",
    "city": "xian",
    "start_date": "2026-08-16",
    "end_date": "2026-08-16",
    "link": "http://www.yanta.gov.cn/xxgk/zdxxgk/ggwhfw/wlhd/1957371326528872449.html",
    "description": "少儿非遗体验活动，先讲《九色鹿》经典绘本故事，后亲子家庭共同实践烧箔技艺，加热金属箔片创作金属光泽作品，培养动手能力。",
    "fee": "免费",
    "source": "雁塔区文化和旅游体育局",
    "family_friendly": True
})

# ============================================
# 4. 儿童剧/演出
# ============================================

activities.append({
    "title": "奇趣装置阳光探险剧《北极熊飞上天》",
    "venue": "开元大剧院",
    "city": "xian",
    "start_date": "2026-09-20",
    "end_date": "2026-09-21",
    "link": "http://m.toutiao.com/group/7544366892329255424/",
    "description": "小不点大视界出品的合家欢亲子剧，没有对白却融入大量肢体语言和幽默情节，适合2-6岁儿童，简单温柔暖心幽默。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "儿童剧《我们是秦俑》",
    "venue": "陕西中太天恩艺术剧院",
    "city": "xian",
    "start_date": "2026-08-16",
    "end_date": "2026-08-17",
    "link": "http://m.toutiao.com/group/7537285927564116518/",
    "description": "西安儿童艺术剧院出品，讲述秦俑复活的奇幻故事，将文物知识融入剧情，让孩子在欢乐中了解秦代历史文化。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "亲子剧《盒子总动员》",
    "venue": "西安浐灞保利大剧院",
    "city": "xian",
    "start_date": "2026-08-08",
    "end_date": "2026-08-09",
    "link": "https://m.dahepiao.com/yanchupiaowu1/20250526514481.html",
    "description": "创意亲子互动剧，通过奇妙的盒子世界带领孩子们展开想象力冒险，充满创意互动和欢乐，适合全家共同观看。",
    "fee": "收费",
    "source": "大河票务网",
    "family_friendly": True
})

activities.append({
    "title": "儿童剧《灰姑娘的水晶鞋》",
    "venue": "陕西省图书馆丝路艺术剧院",
    "city": "xian",
    "start_date": "2026-08-02",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/920469562_121443915/?pvid=000115_3w_a&scm=10001.8085_13-8085_13.0.0-0-0-0-0.0&spm=smpc.channel_437.PureFeedListText_657446spmCode.111.1771545600010DA5oXoZ_8086",
    "description": "经典童话儿童剧，演员表演惟妙惟肖，孩子可参与互动，在故事里学习勇气与善良，暑期每周3-5场轮番上演。",
    "fee": "收费",
    "source": "搜狐网",
    "family_friendly": True
})

activities.append({
    "title": "丝路欢乐世界儿童剧《驼可少年团》",
    "venue": "丝路欢乐世界",
    "city": "xian",
    "start_date": "2026-07-05",
    "end_date": "2026-08-24",
    "link": "http://www.xixianxinqu.gov.cn:9602/zmhd/hygq/whly/1944598730681888769.html",
    "description": "讲述丝路少年冒险故事的原创儿童剧，融合西域乐舞、敦煌飞天等元素，百场演艺贯穿整个暑期音浪狂欢季。",
    "fee": "收费",
    "source": "西咸新区管委会官网",
    "family_friendly": True
})

activities.append({
    "title": "诗经里儿童剧《夫人巡山》",
    "venue": "诗经里景区得月楼",
    "city": "xian",
    "start_date": "2026-07-11",
    "end_date": "2026-09-15",
    "link": "http://www.xixianxinqu.gov.cn:9602/zmhd/hygq/whly/1944598730681888769.html",
    "description": "以《周南·兔罝》为原型的儿童剧，融合诗经文化与戏剧表演，让孩子在观剧中了解传统文化，适合亲子家庭。",
    "fee": "收费",
    "source": "西咸新区管委会官网",
    "family_friendly": True
})

activities.append({
    "title": "哪吒之混元珠的秘密儿童剧",
    "venue": "丝路欢乐世界",
    "city": "xian",
    "start_date": "2026-07-05",
    "end_date": "2026-08-24",
    "link": "http://m.toutiao.com/group/7510196842412425739/",
    "description": "经典神话改编儿童剧，讲述哪吒成长故事，融合特技表演与互动环节，深受小朋友喜爱。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "驼可少年团之拯救绿洲儿童剧",
    "venue": "丝路欢乐世界",
    "city": "xian",
    "start_date": "2026-07-05",
    "end_date": "2026-08-24",
    "link": "http://m.toutiao.com/group/7510196842412425739/",
    "description": "丝路主题原创儿童剧，讲述驼可少年团拯救绿洲的冒险故事，传递环保与友谊理念，适合亲子观看。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "驼可波罗奇遇记儿童剧",
    "venue": "丝路欢乐世界",
    "city": "xian",
    "start_date": "2026-07-05",
    "end_date": "2026-08-24",
    "link": "http://m.toutiao.com/group/7510196842412425739/",
    "description": "以马可波罗东游为蓝本的奇幻儿童剧，带领孩子领略丝路沿线风土人情，开阔视野增长见识。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

# ============================================
# 5. 景区/乐园暑期活动
# ============================================

activities.append({
    "title": "乐华城88度温泉乐园芭提雅之夜狂欢派对",
    "venue": "乐华城88度温泉乐园",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.xixianxinqu.gov.cn:9602/zmhd/hygq/whly/1944598730681888769.html",
    "description": "全天候沉浸式派对，花车巡游与高颜值NPC互动，全天多场演出，芭提雅之夜主舞台狂欢，泼水音浪双重暴击，大喇叭等刺激项目畅玩。",
    "fee": "收费",
    "source": "西咸新区管委会官网",
    "family_friendly": True
})

activities.append({
    "title": "欢乐谷玛雅海滩夏浪泼水节",
    "venue": "西安欢乐谷玛雅海滩水公园",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.xixianxinqu.gov.cn:9602/zmhd/hygq/whly/1944598730681888769.html",
    "description": "水上泼水大战，水枪水盆高压水炮齐上阵，电音浪潮水上蹦迪，高空水上飞人、异域风情表演、无人机灯光秀，高颜值NPC泼水小队互动。",
    "fee": "收费",
    "source": "西咸新区管委会官网",
    "family_friendly": True
})

activities.append({
    "title": "丝路欢乐世界三秦四季冰爽一夏音浪狂欢季",
    "venue": "丝路欢乐世界",
    "city": "xian",
    "start_date": "2026-07-05",
    "end_date": "2026-08-24",
    "link": "http://www.xixianxinqu.gov.cn:9602/zmhd/hygq/whly/1944598730681888769.html",
    "description": "花车巡游首秀，每周解锁七国主题盲盒，意大利冰淇淋节、夏威夷海岛风、日韩动漫电音、英国摇滚露营等不同主题，百场演艺精彩纷呈。",
    "fee": "收费",
    "source": "西咸新区管委会官网",
    "family_friendly": True
})

activities.append({
    "title": "诗经里秘境灯光秀夜游",
    "venue": "诗经里景区",
    "city": "xian",
    "start_date": "2026-07-11",
    "end_date": "2026-09-15",
    "link": "http://www.xixianxinqu.gov.cn:9602/zmhd/hygq/whly/1944598730681888769.html",
    "description": "每晚18:00开始，昆虫秘境、国潮隧道、欢乐花海等主题灯组营造奇幻氛围，水上火壶表演、非遗打铁花、诗经小剧、舞蹈表演等精彩节目。",
    "fee": "收费",
    "source": "西咸新区管委会官网",
    "family_friendly": True
})

activities.append({
    "title": "小知了亲子教育农场夏日活动",
    "venue": "小知了亲子教育农场",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.xixianxinqu.gov.cn:9602/zmhd/hygq/whly/1944598730681888769.html",
    "description": "浑水摸鱼、挖掘机、梦幻水世界、萌宠喂养，周末增开小火车、拖拉机、丛林穿越、真人CS，特色小猪跳水表演、夏日泡沫派对。",
    "fee": "收费",
    "source": "西咸新区管委会官网",
    "family_friendly": True
})

activities.append({
    "title": "秦岭野生动物园第九届纳凉避暑节",
    "venue": "西安秦岭野生动物园",
    "city": "xian",
    "start_date": "2026-07-04",
    "end_date": "2026-08-31",
    "link": "https://1949390mxiaozhu.sjdzp.cn/Miniwx/Index/buy.html?goods_id=12780050",
    "description": "每日下午16:00-20:00纳凉节，彩虹喷泉、亲子水池、演艺舞台，小丑军团巡游，周五至周日乐队歌手表演，奇幻上林苑国际大秀演出。",
    "fee": "收费",
    "source": "西安秦岭野生动物园",
    "family_friendly": True
})

activities.append({
    "title": "动物森友会——秦岭野生动物园4日夏令营",
    "venue": "西安秦岭野生动物园",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7521979270915277352/",
    "description": "四天三夜沉浸式探索之旅，夜探动物园、星空故事会、林间鸟类观测、动物小医生、穿越草原区，解锁教科书外的奇幻篇章。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "细尾獴沙丘建筑师互动课堂",
    "venue": "西安秦岭野生动物园非洲沙地生态馆",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.qyer.com/feeds/p/V5xDekHY2m0bpqVMkg4TuA.html",
    "description": "20+细尾獴家族首次入驻，国内独家地暖系统，亲子家庭参与沙丘建筑师互动课堂，每日限20组，了解动物习性。",
    "fee": "收费",
    "source": "穷游网",
    "family_friendly": True
})

activities.append({
    "title": "丹顶鹤鹤舞云天行为艺术展示",
    "venue": "西安秦岭野生动物园丹顶鹤展区",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.qyer.com/feeds/p/V5xDekHY2m0bpqVMkg4TuA.html",
    "description": "新展区芦苇湿地加瀑布造景，每日10:00/15:00上演鹤舞云天行为艺术，丹顶鹤展翅掠过水雾，科普馆答题解锁纪念卡。",
    "fee": "收费",
    "source": "穷游网",
    "family_friendly": True
})

activities.append({
    "title": "秦岭野生动物园萤火虫小道夜场体验",
    "venue": "西安秦岭野生动物园朱鹮馆后方竹林小径",
    "city": "xian",
    "start_date": "2026-08-01",
    "end_date": "2026-08-31",
    "link": "https://m.qyer.com/feeds/p/V5xDekHY2m0bpqVMkg4TuA.html",
    "description": "步行区暗藏生态秘境，8月可邂逅成群萤火虫，暑期每周五/六19:30星空动物剧场，猛兽行为展示升级声光特效。",
    "fee": "收费",
    "source": "穷游网",
    "family_friendly": True
})

activities.append({
    "title": "昆明池端午亲子龙舟拼图等民俗活动",
    "venue": "昆明池·七夕公园",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7510196842412425739/",
    "description": "汉风广场长弓射五毒、龙舟套圈、手作香囊、非遗油纸伞彩绘，画舫游船亲子龙舟拼图等趣味体验，传统佳节更添韵味。",
    "fee": "免费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "昆明池丘也林谷和萌宠乐园亲子游",
    "venue": "昆明池·七夕公园",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.xa.gov.cn/ztzl/ztzl/lzledc/ywdc/1932270710850330625.html",
    "description": "集合无动力游乐设施和可爱萌宠，让亲子共享温馨时光，适合全家出游放松身心，亲近自然。",
    "fee": "收费",
    "source": "西安市人民政府官网",
    "family_friendly": True
})

# ============================================
# 6. 青少年活动中心/少年宫
# ============================================

activities.append({
    "title": "超能AI工坊暑期限定课程",
    "venue": "西安市青少年宫浐灞半岛校区",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1042234095_121106869/",
    "description": "专为8岁+中小学生定制的AI实践课，AI对话、智能绘画、数据标注、AI模型训练、AI辅助编程全覆盖，项目式沉浸式实战教学。",
    "fee": "收费",
    "source": "西安市青少年宫",
    "family_friendly": True
})

activities.append({
    "title": "西安市青少年活动中心乐高玩学中心亲子活动",
    "venue": "西安市青少年活动中心四楼乐高玩学中心",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7545702878564991534/",
    "description": "通过乐高积木搭建立体交通轨道等复杂模型，构建少儿逻辑思维与空间想象力，亲子共同参与增进互动。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "哇塞快乐星球XR影院沉浸式体验",
    "venue": "西安市青少年活动中心三楼哇塞快乐星球XR影院",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7545702878564991534/",
    "description": "借助虚拟现实技术将课本天文地理知识变为可触可交互的震撼场景，暑假最受欢迎的沉浸式体验项目之一。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "西安市妇女儿童活动中心暑期公益课堂进社区",
    "venue": "西安多个社区",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.xiancn.com/content/2025-08/07/content_7188565.htm",
    "description": "美术、科学、专注力提升三大板块，橡皮泥、水彩笔创作，水变干净了、反重力轨道等科学实验，舒尔特方格专注力训练。",
    "fee": "免费",
    "source": "西安新闻网",
    "family_friendly": True
})

activities.append({
    "title": "暑期名校行系列研学活动",
    "venue": "西安交通大学、西北工业大学、西安电子科技大学",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.xiancn.com/content/2025-09/04/content_7210931.htm",
    "description": "市妇联主办，150余名中小学生走进三大名校，西迁博物馆参观、航空科普讲座、无线电发报机组装实践，感受学术氛围。",
    "fee": "免费需报名",
    "source": "西安新闻网",
    "family_friendly": True
})

activities.append({
    "title": "家门口青少年宫创意美术课程",
    "venue": "西安市青少年宫翠华路小学长大校区",
    "city": "xian",
    "start_date": "2026-07-04",
    "end_date": "2026-07-31",
    "link": "https://m.sohu.com/a/1037444921_121106869/",
    "description": "涵盖绘画、手工制作、作品赏析，多元化教学方法提高观察力想象力创造力，6岁及以上有无基础均可报名。",
    "fee": "收费",
    "source": "西安市青少年宫",
    "family_friendly": True
})

activities.append({
    "title": "家门口青少年宫中国舞课程",
    "venue": "西安市青少年宫翠华路小学长大校区",
    "city": "xian",
    "start_date": "2026-07-04",
    "end_date": "2026-07-31",
    "link": "https://m.sohu.com/a/1037444921_121106869/",
    "description": "参照中国舞考级教材，身体软开度、协调能力、音乐反应能力综合训练，培养自信心审美情感和集体荣誉感。",
    "fee": "收费",
    "source": "西安市青少年宫",
    "family_friendly": True
})

activities.append({
    "title": "家门口青少年宫航模课程",
    "venue": "西安市青少年宫翠华路小学长大校区",
    "city": "xian",
    "start_date": "2026-09-01",
    "end_date": "2027-01-26",
    "link": "https://m.sohu.com/a/1037444921_121106869/",
    "description": "6岁及以上可学，综合性体育运动，空气动力学、材料学、机械制图多学科融合，培养科学素养和动手能力。",
    "fee": "收费",
    "source": "西安市青少年宫",
    "family_friendly": True
})

# ============================================
# 7. 文化馆/非遗活动
# ============================================

activities.append({
    "title": "陕西省非遗体验中心AR沉浸式互动展",
    "venue": "陕西省文化馆曲江馆区二楼非遗体验中心",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-12-31",
    "link": "https://m.sohu.com/a/963728533_121106869/",
    "description": "4700㎡超大空间，35个AR互动点位，小精灵闪闪导览，女娲塑像苏醒、皮影会讲故事、耀州青瓷360度品鉴，西北地区唯一非遗+AR深度融合展。",
    "fee": "免费",
    "source": "西安文旅",
    "family_friendly": True
})

activities.append({
    "title": "非遗体验营——面塑与披萨研学活动",
    "venue": "陕西省文化馆曲江馆区非遗体验中心",
    "city": "xian",
    "start_date": "2026-07-29",
    "end_date": "2026-08-31",
    "link": "https://c.m.163.com/news/a/K5SJOTII05568TOW.html",
    "description": "参观+体验+创造多元形式，面塑非遗传承人张倍源教学，面塑大雁塔披萨，了解非遗面塑技艺同时体验美食制作乐趣。",
    "fee": "收费",
    "source": "三秦都市报",
    "family_friendly": True
})

activities.append({
    "title": "书院门秦缘非遗文化体验馆陶塑DIY",
    "venue": "书院门秦缘非遗文化体验馆",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.cnr.cn/sxpd/sx/20250728/t20250728_527285672.shtml",
    "description": "秦始皇兵马俑手工陶塑DIY制作、拓印DIY手作、研学皮影DIY手工制作等暑期热门项目，孩子亲手做陶塑培养动手能力。",
    "fee": "收费",
    "source": "西安日报",
    "family_friendly": True
})

activities.append({
    "title": "西安非遗大剧院皮影戏+秦腔+华阴老腔演出",
    "venue": "西安非遗大剧院",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.cnr.cn/sxpd/sx/20250728/t20250728_527285672.shtml",
    "description": "周二至周五每天4场，周末节假日5场，《孙悟空三打白骨精》皮影戏、秦腔、华阴老腔轮番登场，现场体验感震撼。",
    "fee": "收费",
    "source": "西安日报",
    "family_friendly": True
})

activities.append({
    "title": "非遗工坊亲子面花制作体验",
    "venue": "陕西省非遗体验中心研学区",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/910393829_121119385/",
    "description": "非遗大师手把手教学，孩子能亲手捏面花、做唐果子、画马勺脸谱，做完作品可带回家，每天名额有限需提前预约。",
    "fee": "免费需预约",
    "source": "搜狐网",
    "family_friendly": True
})

activities.append({
    "title": "陕西省非遗体验中心秦风方言互动体验",
    "venue": "陕西省非遗体验中心秦蕴炎黄根脉展区",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-12-31",
    "link": "https://m.sohu.com/a/910393829_121119385/",
    "description": "方言盲盒互动灯牌，伸手一碰地道陕西方言版民谣响起，牛郎织女传说、老陕人生活智慧谚语，寓教于乐。",
    "fee": "免费",
    "source": "搜狐网",
    "family_friendly": True
})

activities.append({
    "title": "凤翔泥塑与华州皮影非遗体验",
    "venue": "陕西省非遗体验中心秦艺民族之魂展区",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-12-31",
    "link": "https://m.sohu.com/a/910393829_121119385/",
    "description": "1米高凤翔泥塑大坐虎，华州皮影光影绝活，戴上耳机听西安鼓乐，陕北民歌现场互动，视听双重盛宴。",
    "fee": "免费",
    "source": "搜狐网",
    "family_friendly": True
})

# ============================================
# 8. 体育/户外夏令营与研学
# ============================================

activities.append({
    "title": "寻迹古都探秘秦岭——西安科技与人文亲子研学营",
    "venue": "西安及秦岭多地",
    "city": "xian",
    "start_date": "2026-07-19",
    "end_date": "2026-07-25",
    "link": "https://www.hlnhw.com/m/actlist/detail.html?id=10420",
    "description": "7天6晚亲子研学营，国家授时中心时间科学馆、9号宇宙深空博物馆、兵马俑制作、秦岭四宝探秘、城墙骑行，科技人文双重体验。",
    "fee": "收费",
    "source": "广州好少年户外",
    "family_friendly": True
})

activities.append({
    "title": "探秘古都西安5天夏令营",
    "venue": "西安及临潼",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://news.qq.com/rain/a/20250520A06FEL00",
    "description": "五天四晚，兵马俑亲手塑形、秦岭四宝科学公园、西北工业大学航天探秘、华阴老腔皮影戏、biangbiang面制作，历史生态非遗名校全覆盖。",
    "fee": "收费",
    "source": "都市快报",
    "family_friendly": True
})

activities.append({
    "title": "翠华山秦岭小游侠三天两晚夏令营",
    "venue": "翠华山国家地质公园",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.whysw.org/m/view.php?aid=117604",
    "description": "秦岭地质地貌探索、户外生存技能训练、森林探险、星空观测，在大自然中学习地质知识和户外技能。",
    "fee": "收费",
    "source": "文化艺术网",
    "family_friendly": True
})

activities.append({
    "title": "朱雀国家森林公园21℃快乐森林夏令营",
    "venue": "朱雀国家森林公园秦岭国际青少年儿童营地",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.whysw.org/m/view.php?aid=117604",
    "description": "秦岭首家集科普教育、研学旅行、森林探险、休闲娱乐、亲子活动为一体的青少年儿童营地，科普体能娱乐手工全覆盖。",
    "fee": "收费",
    "source": "文化艺术网",
    "family_friendly": True
})

activities.append({
    "title": "楼观暑期研学营——穿越千年文化共赴成长之约",
    "venue": "楼观生态文化旅游景区",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.whysw.org/m/view.php?aid=117604",
    "description": "深度挖掘道文化内涵，非遗文化体验、传统文化学习、探索实践等核心内容，文旅加教育创新研学产品。",
    "fee": "收费",
    "source": "文化艺术网",
    "family_friendly": True
})

activities.append({
    "title": "常宁宫第十八届水花少年派快乐成长夏令营",
    "venue": "常宁宫休闲山庄",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.whysw.org/m/view.php?aid=117604",
    "description": "游泳技能学习、开笔礼国学体验、蒋介石西北行宫参观、星空露营、趣味手作，水上狂欢加文化体验的成长夏令营。",
    "fee": "收费",
    "source": "文化艺术网",
    "family_friendly": True
})

activities.append({
    "title": "大唐芙蓉园东仓鼓乐深度研学",
    "venue": "大唐芙蓉园紫云楼",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663097292823609892/",
    "description": "近距离观摩1400年传承的东仓鼓乐，逛鼓乐博物馆，亲手书写千年工尺谱，看听写三重维度读懂古乐传承。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "大唐芙蓉园御宴宫非遗唐宴体验",
    "venue": "大唐芙蓉园御宴宫",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663097292823609892/",
    "description": "临水唐风宴席空间，品尝列入陕西非遗的唐代菜点宴席，用餐穿插唐诗酒令互动，一餐吃透关中饮食文脉。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "大唐芙蓉园汉服换装与唐礼簪花手作",
    "venue": "大唐芙蓉园仕女馆",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663097292823609892/",
    "description": "解锁全套唐代制式汉服，学习万福礼叉手礼，亲手制作非遗簪花和花钿妆饰，带走专属唐风纪念品。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "唐诗峡诗词雅集与唐代古趣竞技",
    "venue": "大唐芙蓉园唐诗峡",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663097292823609892/",
    "description": "化身盛唐文人玩转飞花令，和研学导师对诗论词，体验投壶蹴鞠等唐代传统竞技，在玩乐中读懂唐诗意境。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

# ============================================
# 9. 高校/科研院所研学
# ============================================

activities.append({
    "title": "西安交通大学现代能源技术线下研学营",
    "venue": "西安交通大学能源与动力工程学院",
    "city": "xian",
    "start_date": "2026-07-16",
    "end_date": "2026-07-19",
    "link": "https://www.dengfengpingtai.com/news/d/record/215.html",
    "description": "登峰计划大学实验室开放活动，能源动力加能源环境加智慧能源多维度体验，专家讲座、沉浸式VR体验、能源实验实操。",
    "fee": "收费",
    "source": "登峰平台",
    "family_friendly": True
})

activities.append({
    "title": "西安交通大学智能制造线下研学营",
    "venue": "西安交通大学机械工程学院",
    "city": "xian",
    "start_date": "2026-07-17",
    "end_date": "2026-07-20",
    "link": "https://www.dengfengpingtai.com/news/d/record/215.html",
    "description": "世界排名第一的机械工程学科体验，电工电子、单片机、传感器、C语言编程、CAD/CAM等核心工科技能深度实践。",
    "fee": "收费",
    "source": "登峰平台",
    "family_friendly": True
})

activities.append({
    "title": "西安交通大学电亮世界线下研学营",
    "venue": "西安交通大学电气工程学院",
    "city": "xian",
    "start_date": "2026-07-17",
    "end_date": "2026-07-20",
    "link": "https://www.dengfengpingtai.com/news/d/record/215.html",
    "description": "电气工程A+学科体验，走进中国西部科技创新港全国重点实验室，基础加进阶加创新电路实操，完成LED灯等创意作品。",
    "fee": "收费",
    "source": "登峰平台",
    "family_friendly": True
})

activities.append({
    "title": "西安交通大学核能线上研学营",
    "venue": "西安交通大学线上",
    "city": "xian",
    "start_date": "2026-08-01",
    "end_date": "2026-08-04",
    "link": "https://www.dengfengpingtai.com/news/d/record/215.html",
    "description": "核电厂与火电厂系统国家级虚拟仿真实验教学中心主办，线上学习核能知识，虚拟仿真实验，适合对核工程感兴趣的高中生。",
    "fee": "收费",
    "source": "登峰平台",
    "family_friendly": True
})

activities.append({
    "title": "西北工业大学三航科技研学",
    "venue": "西北工业大学长安校区",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.xiancn.com/content/2025-09/04/content_7210931.htm",
    "description": "航空科普讲座、校史馆参观、为国铸剑勇士雕塑打卡，了解航空航天航海三航科技成就，点燃科技报国热情。",
    "fee": "免费需报名",
    "source": "西安新闻网",
    "family_friendly": True
})

activities.append({
    "title": "西安电子科技大学无线电发报实践研学",
    "venue": "西安电子科技大学",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.xiancn.com/content/2025-09/04/content_7210931.htm",
    "description": "校史馆半部电台参观，亲手组装调试无线电发报机，辨识零件成功发送摩尔斯电码，体验通信科技魅力。",
    "fee": "免费需报名",
    "source": "西安新闻网",
    "family_friendly": True
})

activities.append({
    "title": "西安交大苏州研究院暑期科创研学营",
    "venue": "西安交通大学及周边科创基地",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.xjtusz.cn/jiaoyudongtai/4257.html",
    "description": "文化溯源加科技砺新加名校启航，钱学森展馆、重点实验室参观，航天六院火箭发动机基地探访，吉利汽车黑灯工厂参访。",
    "fee": "收费",
    "source": "西安交通大学苏州研究院",
    "family_friendly": True
})

activities.append({
    "title": "中国科学院国家授时中心时间科学研学",
    "venue": "中国科学院国家授时中心时间科学馆",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.hlnhw.com/m/actlist/detail.html?id=10420",
    "description": "我国唯一以时间为主题的科学展馆，了解北京时间如何产生，傅科摆等互动体验，亲手制作日晷，学习计时仪器发展历史。",
    "fee": "收费",
    "source": "广州好少年户外",
    "family_friendly": True
})

activities.append({
    "title": "9号宇宙深空博物馆星际穿越体验",
    "venue": "9号宇宙深空博物馆",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-12-31",
    "link": "https://www.hlnhw.com/m/actlist/detail.html?id=10420",
    "description": "国内首家浸入式深空博物馆，学习太空知识，体验星际穿越，4D观影，科学实验室，适合亲子家庭体验航天科普。",
    "fee": "收费",
    "source": "广州好少年户外",
    "family_friendly": True
})

activities.append({
    "title": "西安双高5日研学夏令营",
    "venue": "西安多景点及高校",
    "city": "xian",
    "start_date": "2026-07-05",
    "end_date": "2026-08-16",
    "link": "https://m.cct.cn/dujia/390970.html",
    "description": "大明宫唐宫古建斗拱搭建、制陶DIY、西安交大学术交流、非遗剧场戏曲体验、城墙汉字拼拼乐，多期团可选。",
    "fee": "收费",
    "source": "携程旅行",
    "family_friendly": True
})

# ============================================
# 10. 其他特色亲子活动
# ============================================

activities.append({
    "title": "长安十二时辰主题街区大唐穿越体验",
    "venue": "长安十二时辰主题街区",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://sxggwhy.com/news/detail?id=68552918e25ad2452909e96e",
    "description": "梳仿唐妆发换精美衣服一秒穿越，与李白对诗、看胡姬旋舞、参与市井游戏，沉浸式体验大唐百姓日常生活。",
    "fee": "收费",
    "source": "陕西省文旅厅",
    "family_friendly": True
})

activities.append({
    "title": "茯茶镇非遗体验亲子游",
    "venue": "茯茶镇",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7510196842412425739/",
    "description": "安塞腰鼓、华县皮影非遗展演，茯茶手工压制互动项目，点茶茶艺、制香调配，包粽子做香包五彩绳DIY，陕西非遗大剧院演出。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "华夏文旅水世界海豚漂流河亲子游",
    "venue": "西安华夏文旅水世界",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7654868163607429675/",
    "description": "800米环形漂流河穿越海豚表演馆，恒温净水系统，唐风汤泉区20余种泡池，周末水上DJ派对，亲子玩水好去处。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "曲江欢乐童年亲子乐园",
    "venue": "曲江欢乐童年亲子乐园",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-12-31",
    "link": "http://m.toutiao.com/group/7497909817286132233/",
    "description": "专为1-10岁儿童设计，无动力设施沙池、攀爬网、小火车，园区内有咖啡厅家长可休息，低龄儿童友好。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "丝路欢乐世界奇幻飞越裸眼3D项目",
    "venue": "丝路欢乐世界",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-12-31",
    "link": "http://m.toutiao.com/group/7497909817286132233/",
    "description": "类似迪士尼飞跃地平线的裸眼3D项目，七大主题街区波斯风罗马风拍照，长安大牌档分店美食，新晋网红打卡地。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "西影电影园区夏日多巴胺放映计划",
    "venue": "西影电影园区",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7526116292928209454/",
    "description": "拾光音乐SHOW、光影漫游纪、仲夏趣市会、艺术生活季四大主题活动，露天电影、文创市集、精酿品鉴，全家共享。",
    "fee": "免费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "太空奥德赛VR科幻展",
    "venue": "西影电影园区",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-12-31",
    "link": "http://m.toutiao.com/group/7526116292928209454/",
    "description": "全球首个8K加AI加持加多模态互动VR科幻巨制，10大区域17个场景36分钟超长体验，2.2亿公里星际远征。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

activities.append({
    "title": "生命的纪元沉浸式探索体验",
    "venue": "西影电影园区",
    "city": "xian",
    "start_date": "2026-07-01",
    "end_date": "2026-12-31",
    "link": "http://m.toutiao.com/group/7526116292928209454/",
    "description": "消失的法老原班制作团队出品，45分钟纵览地球35亿年，近距离感受生命演化奇迹，与恐龙同行伴鱼龙同游。",
    "fee": "收费",
    "source": "今日头条",
    "family_friendly": True
})

print(f"共生成 {len(activities)} 条新活动")

with open('/workspace/goout/output/raw/real_activities_xian_batch2.json', 'w', encoding='utf-8') as f:
    json.dump(activities, f, ensure_ascii=False, indent=2)

print(f"已保存到 real_activities_xian_batch2.json")
