import json

activities = []

# ========== 1. 博物馆奇妙夜系列活动（黄浦区） ==========
museum_night_activities = [
    {
        "title": "上海博物馆世界树之巅美洲古代文明大展夜场",
        "venue": "上海博物馆人民广场馆",
        "city": "shanghai",
        "start_date": "2026-07-09",
        "end_date": "2026-08-31",
        "link": "https://www.shanghai.gov.cn/nw9822/20260611/70add600f61840028c02b1d36ba6284f.html",
        "description": "每周二至周五17:00-21:00开放夜场，可在夜间参观美洲古代文明大展，汇聚墨西哥、秘鲁顶尖文博机构的1129组近3000件精美文物，全景式勾勒古代中南美洲文明长卷。",
        "fee": "收费",
        "source": "上海市政府新闻发布会",
        "family_friendly": True
    },
    {
        "title": "上海博物馆美洲萌萌TA奇妙夜",
        "venue": "上海博物馆人民广场馆",
        "city": "shanghai",
        "start_date": "2026-07-11",
        "end_date": "2026-08-31",
        "link": "https://k.sina.cn/article_7879776444_1d5abd8bc0190ay3pe.html",
        "description": "每周六晚18:30-21:30举办，羊驼、水豚等萌宠互动，展厅复刻美洲原生态场景，看文物见生灵，科普又好玩，单场限额3000人。",
        "fee": "198元/人",
        "source": "上海博物馆官方",
        "family_friendly": True
    },
    {
        "title": "中共一大纪念馆夜间开放活动",
        "venue": "中共一大纪念馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-01",
        "link": "http://m.sh.bendibao.com/tour/307215.html",
        "description": "7月1日、7月25日、8月1日17:00-20:00正门夜间开放，还有电影党课《火种》和微讲座《新四军臂章》，适合亲子红色教育。",
        "fee": "免费",
        "source": "上海博物馆奇妙夜系列",
        "family_friendly": True
    },
    {
        "title": "上海市历史博物馆奇妙夜系列活动",
        "venue": "上海市历史博物馆",
        "city": "shanghai",
        "start_date": "2026-07-03",
        "end_date": "2026-08-29",
        "link": "http://m.sh.bendibao.com/tour/307215.html",
        "description": "每周二至周六延长开放至20:00，小浪花讲解团带领青少年以童声讲述苏州河故事，还有苏州河夜游Citywalk和徽州非遗工坊主题文化研学活动。",
        "fee": "免费&收费",
        "source": "上海市历史博物馆",
        "family_friendly": True
    },
    {
        "title": "世博会博物馆故宫藏清代帝后服饰展夜场",
        "venue": "上海世博会博物馆",
        "city": "shanghai",
        "start_date": "2026-07-11",
        "end_date": "2026-08-29",
        "link": "http://m.sh.bendibao.com/tour/307215.html",
        "description": "每周六延时开放至20:00，展出康熙礼服褂、乾隆龙袍、嘉庆朝袍等最高等级帝后服装和珍稀首饰，九成从未出京，超三成首次面世。",
        "fee": "收费",
        "source": "世博会博物馆",
        "family_friendly": True
    },
    {
        "title": "上海琉璃艺术博物馆夜游看展",
        "venue": "上海琉璃艺术博物馆",
        "city": "shanghai",
        "start_date": "2026-07-18",
        "end_date": "2026-08-15",
        "link": "http://m.sh.bendibao.com/tour/307215.html",
        "description": "7月18日、8月1日、8月15日延长开放至20:00，可夜游观看《熔光凝形》铸造玻璃艺术叙事特展，感受琉璃艺术的独特魅力。",
        "fee": "收费",
        "source": "上海琉璃艺术博物馆",
        "family_friendly": True
    },
    {
        "title": "上海周虎臣曹素功笔墨博物馆近代名人墨知识讲座",
        "venue": "上海周虎臣曹素功笔墨博物馆",
        "city": "shanghai",
        "start_date": "2026-07-10",
        "end_date": "2026-08-28",
        "link": "http://m.sh.bendibao.com/tour/307215.html",
        "description": "7月10日举办近代名人墨知识讲座，8月14日墨锭鉴赏交流活动，8月28日夜间开放，适合亲子了解传统笔墨文化。",
        "fee": "免费",
        "source": "上海笔墨博物馆",
        "family_friendly": True
    },
    {
        "title": "国际乒联博物馆乒乓体验营",
        "venue": "国际乒联博物馆和中国乒乓球博物馆",
        "city": "shanghai",
        "start_date": "2026-07-08",
        "end_date": "2026-07-30",
        "link": "http://m.sh.bendibao.com/tour/307215.html",
        "description": "7月8日、7月16日面向中小学生开放乒乓体验营，还有乒乓球技术等级测试，让孩子在博物馆中体验国球魅力。",
        "fee": "免费",
        "source": "国际乒联博物馆",
        "family_friendly": True
    },
    {
        "title": "豫园夜游豫享山林活动",
        "venue": "上海豫园",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.sh.bendibao.com/tour/307215.html",
        "description": "每周二、三、五、六、日19:00-21:50开放夜游，古典园林夜景搭配灯光秀，感受江南园林的夏夜风情，适合亲子漫步。",
        "fee": "收费",
        "source": "上海豫园管理处",
        "family_friendly": True
    },
]

activities.extend(museum_night_activities)

# ========== 2. 浦东新区博物馆活动 ==========
pudong_museum_activities = [
    {
        "title": "上海天文馆邂逅星空奇妙夜",
        "venue": "上海天文馆",
        "city": "shanghai",
        "start_date": "2026-07-04",
        "end_date": "2026-08-30",
        "link": "http://m.sh.bendibao.com/tour/307215.html",
        "description": "7月4日、12日、19日、26日及8月每周六开放奇妙夜，收费358元，包含天文观测、星空科普、球幕电影等精彩内容，全年龄段适宜。",
        "fee": "358元",
        "source": "上海天文馆",
        "family_friendly": True
    },
    {
        "title": "中国航海博物馆邮轮出游记青少年科普展",
        "venue": "中国航海博物馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-09-20",
        "link": "http://m.toutiao.com/group/7662955572609696292/",
        "description": "上海市百展百课官方认证项目，学习邮轮文化和航海科技，体验科普课堂和模拟讲解，锻炼孩子胆量与表达能力。",
        "fee": "30元/人（博物馆门票）",
        "source": "中国航海博物馆",
        "family_friendly": True
    },
    {
        "title": "上海科技馆科好玩了暑假营",
        "venue": "上海科技馆",
        "city": "shanghai",
        "start_date": "2026-06-27",
        "end_date": "2026-08-31",
        "link": "https://k.sina.cn/article_7879924051_1d5ae1953068022t08.html",
        "description": "集结15大特色科普品牌，包括粒子奇遇球幕互动展演、VR数字剧场、科创实践营、巴斯夫小小化学家等，周六延时开放至20:00。",
        "fee": "以具体活动为准",
        "source": "上海科技馆",
        "family_friendly": True
    },
    {
        "title": "上海科技馆量子迷宫展区",
        "venue": "上海科技馆",
        "city": "shanghai",
        "start_date": "2026-05-23",
        "end_date": "2026-12-31",
        "link": "https://k.sina.cn/article_7879924051_1d5ae1953068022t08.html",
        "description": "全息投影再现量子纠缠，观众可亲手操作模拟器感受粒子分裂，是亲子了解前沿物理的绝佳科普体验。",
        "fee": "含在门票内",
        "source": "上海科技馆",
        "family_friendly": True
    },
    {
        "title": "上海科技馆AI创世纪展区",
        "venue": "上海科技馆",
        "city": "shanghai",
        "start_date": "2026-05-23",
        "end_date": "2026-12-31",
        "link": "https://k.sina.cn/article_7879924051_1d5ae1953068022t08.html",
        "description": "情感识别系统能与访客进行哲学对话，生成专属数字画像，让孩子近距离感受人工智能的魅力与神奇。",
        "fee": "含在门票内",
        "source": "上海科技馆",
        "family_friendly": True
    },
    {
        "title": "上海自然博物馆夜宿活动",
        "venue": "上海自然博物馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://app.xinhuanet.com/news/article.html?articleId=20260520c9f86c88153744949204999fbe7aaa7f",
        "description": "与恐龙、猛犸象等史前巨兽标本同眠，参加恐龙蝴蝶主题科普手工活动，跟随科普人员逛馆，亲子音乐会等，暑期增加频次。",
        "fee": "收费",
        "source": "上海自然博物馆",
        "family_friendly": True
    },
    {
        "title": "上海体育博物馆奇妙夜主题活动",
        "venue": "上海体育博物馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7663000385845527074/",
        "description": "7月-8月每周五16:30-20:30开放，夜间观展与定时讲解，8月特邀资深汽车设计师探秘汽车设计美学，主题讲座趣味分享轮番上阵。",
        "fee": "免费免预约",
        "source": "上海体育博物馆",
        "family_friendly": True
    },
]

activities.extend(pudong_museum_activities)

# ========== 3. 公园夜游/科普活动 ==========
park_night_activities = [
    {
        "title": "世纪公园萤火流星奇妙夜科普夜游",
        "venue": "世纪公园",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-30",
        "link": "https://www.pudong.gov.cn/rmt_pdxw/20260706/829334.html",
        "description": "以萤火虫为引线，包括趣味科普、荧光实验、习性游戏、户外夜观、萤火虫观察、亲饲幼虫五大环节，每逢周六周日开展。",
        "fee": "298元/一大一小",
        "source": "世纪公园官方",
        "family_friendly": True
    },
    {
        "title": "上海滨江森林公园小小昆虫观察家夜游",
        "venue": "上海滨江森林公园",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-07-12",
        "link": "https://www.pudong.gov.cn/rmt_pdxw/20260706/829334.html",
        "description": "孩子们通过动物惊奇箱、飞蛾与蝙蝠、夜行动物观察等环节，寻觅萤火虫，观察锹甲和天牛，探索暗夜中的自然世界。",
        "fee": "收费",
        "source": "上海滨江森林公园",
        "family_friendly": True
    },
    {
        "title": "上海植物园暗访夜精灵夜间观察活动",
        "venue": "上海植物园",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7662329186924659227/",
        "description": "沪上老牌夜游IP，分南区虫虫特工队和北区神秘水世界两大主题，学习昆虫识别、观察蛙类和水生生物，低龄儿童友好。",
        "fee": "298元/一大一小",
        "source": "上海植物园",
        "family_friendly": True
    },
    {
        "title": "辰山植物园辰山奇妙夜夏令营",
        "venue": "上海辰山植物园",
        "city": "shanghai",
        "start_date": "2026-07-15",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7662329186924659227/",
        "description": "专为8-10岁独立儿童设计，白天植物寻宝标本记录，入夜寻觅萤火虫观察夜行昆虫，含午餐晚餐小火车体验。",
        "fee": "450元/人",
        "source": "上海辰山植物园",
        "family_friendly": True
    },
    {
        "title": "上海动物园动物奇妙夜经典基础夜游",
        "venue": "上海动物园",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7662329186924659227/",
        "description": "室内科普课堂零距离触摸玉米蛇鬃狮蜥等温顺两爬动物，保育员带队夜探灵长区狮虎山天鹅湖，观察夜行动物。",
        "fee": "598元/一大一小",
        "source": "上海动物园",
        "family_friendly": True
    },
    {
        "title": "上海动物园Zoowalk夜猫子深度观测",
        "venue": "上海动物园",
        "city": "shanghai",
        "start_date": "2026-07-17",
        "end_date": "2026-07-31",
        "link": "http://m.toutiao.com/group/7662329186924659227/",
        "description": "配备红外相机高清夜视仪，分A/B两条专属路线，拍摄野生貉等动物影像，赠送动物文创和暗夜探索证书。",
        "fee": "269元/人",
        "source": "上海动物园",
        "family_friendly": True
    },
    {
        "title": "共青森林公园探秘夜森林科普活动",
        "venue": "共青森林公园",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1045269398_121106832/",
        "description": "拜访熟睡的蝴蝶、威武的锹甲、优雅的螳螂、善歌的寒蝉，还有萤火虫，跟随科普老师深入了解夜间森林生态系统。",
        "fee": "收费",
        "source": "共青森林公园",
        "family_friendly": True
    },
    {
        "title": "共青森林公园森林职业体验水质净化家",
        "venue": "共青森林公园",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7663000385845527074/",
        "description": "面向6-15岁亲子家庭，在生态课堂里化身水质净化家，学习检测水质的方法，为构建健康水下生态系统出力。",
        "fee": "收费",
        "source": "共青森林公园",
        "family_friendly": True
    },
    {
        "title": "上海野生动物园萌兽奇趣记夜游",
        "venue": "上海野生动物园",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.pudong.gov.cn/rmt_pdxw/20260706/829334.html",
        "description": "运营至21:00，水域探秘夜间游船、萤火星河光影秀、百兽夜行场景、蛋仔派对主题打卡、萌虎乐队NPC巡游。",
        "fee": "夜场票99元起",
        "source": "上海野生动物园",
        "family_friendly": True
    },
    {
        "title": "古猗园第十三届上海荷花睡莲展",
        "venue": "上海古猗园",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1045269398_121106832/",
        "description": "莲开海上悦享荷处主题，上百种珍稀荷花品种，一颗莲子的奇妙旅行科普研学，荷花宴美食体验，非遗剪纸竹编手工体验。",
        "fee": "门票12元",
        "source": "上海古猗园",
        "family_friendly": True
    },
]

activities.extend(park_night_activities)

# ========== 4. 景区/主题乐园活动 ==========
theme_park_activities = [
    {
        "title": "上海迪士尼乐园夏日缤纷主题体验",
        "venue": "上海迪士尼乐园",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.sh.bendibao.com/tour/jd/307624.html",
        "description": "开业十周年限定夏日狂欢，每周五六加时升级日延时至22:30，明日世界夏日音浪派对，水花巡游清凉水雾，达菲家族夏日新装。",
        "fee": "以官方票价为准",
        "source": "上海迪士尼度假区",
        "family_friendly": True
    },
    {
        "title": "上海海昌海洋公园虎鲸造浪节",
        "venue": "上海海昌海洋公园",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.sh.bendibao.com/tour/jd/307624.html",
        "description": "连续66天夜场至21点，四大戏水派对、14位人气大咖、6大夜秀、10大明星剧目升级，奥特曼60周年庆，7月11日起虎鲸造浪音乐节。",
        "fee": "儿童特惠59.9元起",
        "source": "上海海昌海洋公园",
        "family_friendly": True
    },
    {
        "title": "上海欢乐谷EV音乐乐园夏日狂欢",
        "venue": "上海欢乐谷",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-30",
        "link": "http://m.sh.bendibao.com/tour/jd/307624.html",
        "description": "与玛雅海滩水公园水陆双园联动，白天逐浪戏水夜晚音浪炸场，欢乐广场泼水派对，巨型水炮矩阵水枪补给站。",
        "fee": "以官方票价为准",
        "source": "上海欢乐谷",
        "family_friendly": True
    },
    {
        "title": "上海玛雅海滩水公园夏浪戏水节",
        "venue": "上海玛雅海滩水公园",
        "city": "shanghai",
        "start_date": "2026-06-14",
        "end_date": "2026-08-31",
        "link": "https://k.sina.cn/article_7879776444_1d5abd8bc0190ay3pe.html",
        "description": "六大亲子闯关项目、深海龙宫NPC天团亮相，40余项水上项目，24小时活水循环水质安全，全家嗨玩一整天。",
        "fee": "学生票180元起",
        "source": "上海玛雅海滩水公园",
        "family_friendly": True
    },
    {
        "title": "东方明珠钛空明珠星舰体验空间",
        "venue": "东方明珠电视塔",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-12-31",
        "link": "http://m.sh.bendibao.com/tour/jd/307624.html",
        "description": "98米与107米区域打造太空主题体验，从航天发射轨道飞行到火星探测深空漫游，沉浸式太空任务体验。",
        "fee": "以官方票价为准",
        "source": "东方明珠",
        "family_friendly": True
    },
    {
        "title": "上海乐高乐园暑期玩乐节",
        "venue": "上海乐高乐园度假区",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://k.sina.cn/article_7879776444_1d5abd8bc0190ay3pe.html",
        "description": "F1极速进站亲子对战等新玩法，周五至周日夜场千架无人机表演，八大主题区超75个互动骑乘设施。",
        "fee": "早鸟票339元起",
        "source": "上海乐高乐园",
        "family_friendly": True
    },
    {
        "title": "金山城市沙滩暑期活动",
        "venue": "金山城市沙滩",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7662947664883696134/",
        "description": "碧海金沙玩水胜地，青少年心理成长大赛参赛选手可凭证免费入园，周边花开海上生态园等景点联动。",
        "fee": "门票以官方为准",
        "source": "金山城市沙滩",
        "family_friendly": True
    },
    {
        "title": "金山滨海新片区绿地免费开放",
        "venue": "金山滨海新片区绿地",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-12-31",
        "link": "https://k.sina.cn/article_7879776444_1d5abd8bc0190ay3pe.html",
        "description": "56万㎡海上小呼伦贝尔滨海草坪，运动区儿童游乐区，免费露营休憩放风筝，适配亲子出游好友结伴。",
        "fee": "免费",
        "source": "金山区文旅",
        "family_friendly": True
    },
]

activities.extend(theme_park_activities)

# ========== 5. 青少年体育夏令营 ==========
sports_camp_activities = [
    {
        "title": "上海市青少年体育夏令营运动项目培训营",
        "venue": "全市170+个活动网点",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7645687556851515958/",
        "description": "近30个运动项目，350+期精彩营期，足球篮球排球乒乓球羽毛球网球击剑棒球攀岩滑板冰雪棋类跆拳道跳绳体适能等，公益收费享100元补贴。",
        "fee": "公益收费（享100元补贴）",
        "source": "上海市体育局",
        "family_friendly": True
    },
    {
        "title": "上海市青少年体育夏令营特殊儿童运动营",
        "venue": "全市各指定网点",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7645687556851515958/",
        "description": "专为孤独症唐氏综合征等特殊儿童开设的全公益运动营，足球羽毛球体适能等内容，科学运动帮助青少年促进交流改善行为。",
        "fee": "全程免费",
        "source": "上海市体育局",
        "family_friendly": True
    },
    {
        "title": "上海市青少年体育夏令营户外体育活动营",
        "venue": "全市各景区体育公园郊野公园",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7645687556851515958/",
        "description": "精选景区体育公园郊野公园科普场馆，体育技能体验+文化参访+红色研学+自然探索+亲子互动，享100元补贴。",
        "fee": "公益收费（享100元补贴）",
        "source": "上海市体育局",
        "family_friendly": True
    },
    {
        "title": "上海市青少年体育夏令营五健主题特色营",
        "venue": "全市各指定合作机构",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7645687556851515958/",
        "description": "与专业医疗机构科研团队合作，聚焦肥胖防控脊柱弯曲等健康问题，针对性运动方案与健康管理指导，享200元补贴。",
        "fee": "公益收费（享200元补贴）",
        "source": "上海市体育局",
        "family_friendly": True
    },
    {
        "title": "皮划艇暑期欢乐营",
        "venue": "奉贤区树修教育培训中心",
        "city": "shanghai",
        "start_date": "2026-07-04",
        "end_date": "2026-08-01",
        "link": "https://www.163.com/dy/article/KULPHN8N053478CE.html",
        "description": "住宿营2天1夜，每期限定8人小班精品教学，学习皮划艇技能，在清凉水面中锻炼体魄培养勇气。",
        "fee": "以官方报价为准",
        "source": "上海市青少年体育夏令营",
        "family_friendly": True
    },
    {
        "title": "林间小勇士攀树横渡丛林飞跃营",
        "venue": "浦东新区长桥村588号",
        "city": "shanghai",
        "start_date": "2026-07-11",
        "end_date": "2026-08-08",
        "link": "https://www.163.com/dy/article/KULPHN8N053478CE.html",
        "description": "走读营1天，每期限15人，攀树飞跃丛林探险射箭挑战，专业教练带领安全可控环境中体验冒险乐趣。",
        "fee": "以官方报价为准",
        "source": "上海市青少年体育夏令营",
        "family_friendly": True
    },
    {
        "title": "佘山亲子徒步登山人文户外技能营",
        "venue": "松江区东佘山",
        "city": "shanghai",
        "start_date": "2026-08-20",
        "end_date": "2026-08-20",
        "link": "https://www.163.com/dy/article/KULPHN8N053478CE.html",
        "description": "走读营1天，每期限10人小团深度体验，登山人文探索户外技能学习，在行走中感受城市之美和自然之力。",
        "fee": "以官方报价为准",
        "source": "上海市青少年体育夏令营",
        "family_friendly": True
    },
    {
        "title": "苏州河徒步探寻上海历史文化营",
        "venue": "长宁区苏州河沿线",
        "city": "shanghai",
        "start_date": "2026-08-21",
        "end_date": "2026-08-22",
        "link": "https://www.163.com/dy/article/KULPHN8N053478CE.html",
        "description": "走读营1天，每期限10人，沿苏州河漫步了解上海历史文化，运动与人文探索相结合的独特体验。",
        "fee": "以官方报价为准",
        "source": "上海市青少年体育夏令营",
        "family_friendly": True
    },
]

activities.extend(sports_camp_activities)

# ========== 6. 爱心暑托班（各区县） ==========
summer_care_activities = [
    {
        "title": "浦东新区小学生爱心暑托班",
        "venue": "浦东新区各办班点",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-14",
        "link": "http://m.toutiao.com/group/7649787076778459690/",
        "description": "分两期各3周，工作日全天，覆盖全区各街镇，红色教育科学普及体育锻炼趣味美育等丰富素质课程。",
        "fee": "以各区县标准为准",
        "source": "上海市爱心暑托班",
        "family_friendly": True
    },
    {
        "title": "黄浦区小学生爱心暑托班",
        "venue": "黄浦区各办班点",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-14",
        "link": "http://m.toutiao.com/group/7649787076778459690/",
        "description": "分两期各3周工作日全天，南京西路街道等办班点提供延时服务至5点半至6点，方便双职工家庭接送。",
        "fee": "以各区县标准为准",
        "source": "上海市爱心暑托班",
        "family_friendly": True
    },
    {
        "title": "静安区小学生爱心暑托班",
        "venue": "静安区各办班点",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-14",
        "link": "http://m.toutiao.com/group/7649787076778459690/",
        "description": "分两期各3周工作日全天，随申办报名，提供作业辅导兴趣拓展等服务，解决假期看护难题。",
        "fee": "以各区县标准为准",
        "source": "上海市爱心暑托班",
        "family_friendly": True
    },
    {
        "title": "徐汇区小学生爱心暑托班",
        "venue": "徐汇区各办班点",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-14",
        "link": "http://m.toutiao.com/group/7649787076778459690/",
        "description": "覆盖全区各街道，随申办徐汇区旗舰店报名，课程丰富寓教于乐，专业志愿服务团队陪伴孩子成长。",
        "fee": "以各区县标准为准",
        "source": "上海市爱心暑托班",
        "family_friendly": True
    },
    {
        "title": "长宁区小学生爱心暑托班",
        "venue": "长宁区各办班点",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-14",
        "link": "http://m.toutiao.com/group/7649792417670922815/",
        "description": "两期各3周，600元/期/人，一网通办线上全流程操作，家长线上报名缴费上传材料一次都不用跑。",
        "fee": "600元/期/人",
        "source": "长宁区爱心暑托班",
        "family_friendly": True
    },
    {
        "title": "普陀区小学生爱心暑托班",
        "venue": "普陀区各办班点",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-14",
        "link": "http://m.toutiao.com/group/7649787076778459690/",
        "description": "分两期各3周工作日全天，覆盖各街道镇，随申办普陀区旗舰店线上报名，课程丰富多彩。",
        "fee": "以各区县标准为准",
        "source": "上海市爱心暑托班",
        "family_friendly": True
    },
    {
        "title": "虹口区小学生爱心暑托班",
        "venue": "虹口区各办班点",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-14",
        "link": "http://m.toutiao.com/group/7649787076778459690/",
        "description": "分两期各3周工作日全天，随申办报名，课业辅导+兴趣拓展+安全看护三重保障。",
        "fee": "以各区县标准为准",
        "source": "上海市爱心暑托班",
        "family_friendly": True
    },
    {
        "title": "杨浦区小学生爱心暑托班",
        "venue": "杨浦区各办班点",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-14",
        "link": "http://m.toutiao.com/group/7649787076778459690/",
        "description": "分两期各3周工作日全天，随申办杨浦区旗舰店报名，多元化素质课程陪伴孩子快乐过暑假。",
        "fee": "以各区县标准为准",
        "source": "上海市爱心暑托班",
        "family_friendly": True
    },
    {
        "title": "宝山区小学生爱心暑托班",
        "venue": "宝山区各办班点",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-14",
        "link": "http://m.toutiao.com/group/7649787076778459690/",
        "description": "分两期各3周工作日全天，线上报名线下确认，课程结合宝山邮轮非遗红色滨江特色。",
        "fee": "以各区县标准为准",
        "source": "上海市爱心暑托班",
        "family_friendly": True
    },
    {
        "title": "闵行区小学生爱心暑托班",
        "venue": "闵行区各办班点",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-14",
        "link": "http://m.toutiao.com/group/7649787076778459690/",
        "description": "分两期各3周工作日全天，随申办闵行区旗舰店线上报名，全区各街镇覆盖，课程丰富多样。",
        "fee": "以各区县标准为准",
        "source": "上海市爱心暑托班",
        "family_friendly": True
    },
    {
        "title": "嘉定区小学生爱心暑托班",
        "venue": "嘉定区各办班点",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-14",
        "link": "http://m.toutiao.com/group/7649787076778459690/",
        "description": "分两期各3周工作日全天，线上报名线下确认，结合嘉定汽车文化非遗文化等地方特色课程。",
        "fee": "以各区县标准为准",
        "source": "上海市爱心暑托班",
        "family_friendly": True
    },
    {
        "title": "金山区小学生爱心暑托班",
        "venue": "金山区各办班点",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-14",
        "link": "http://m.toutiao.com/group/7649787076778459690/",
        "description": "分两期各3周工作日全天，随申办金山区旗舰店报名，金山农民画金山嘴渔村等乡土文化融入课程。",
        "fee": "以各区县标准为准",
        "source": "上海市爱心暑托班",
        "family_friendly": True
    },
    {
        "title": "松江区小学生爱心暑托班",
        "venue": "松江区各办班点",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-14",
        "link": "http://m.toutiao.com/group/7649787076778459690/",
        "description": "分两期各3周工作日全天，随申办松江区旗舰店报名，广富林文化佘山度假区等松江特色融入课程。",
        "fee": "以各区县标准为准",
        "source": "上海市爱心暑托班",
        "family_friendly": True
    },
    {
        "title": "青浦区小学生爱心暑托班",
        "venue": "青浦区各办班点",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-14",
        "link": "https://www.shanghai.gov.cn/nw17239/20260610/b78559e0e506422c812b32d813a55ab7.html",
        "description": "全区36个办班点覆盖11个街镇，389元/人/期含午餐25元/天保险14元/期，红色教育科普美育等课程。",
        "fee": "389元/人/期",
        "source": "青浦区爱心暑托班",
        "family_friendly": True
    },
    {
        "title": "奉贤区小学生爱心暑托班",
        "venue": "奉贤区各办班点",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-14",
        "link": "http://m.toutiao.com/group/7663094481465442851/",
        "description": "46个办班点覆盖13个街镇开发区，两期共6周工作日全天，预计服务2968人次，市区两级配送86门课程。",
        "fee": "以各区县标准为准",
        "source": "奉贤区爱心暑托班",
        "family_friendly": True
    },
    {
        "title": "崇明区小学生爱心暑托班",
        "venue": "崇明区各办班点",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-14",
        "link": "http://m.toutiao.com/group/7649787076778459690/",
        "description": "分两期各3周工作日全天，随申办崇明区旗舰店报名，生态岛特色课程融入暑托班教学。",
        "fee": "以各区县标准为准",
        "source": "上海市爱心暑托班",
        "family_friendly": True
    },
]

activities.extend(summer_care_activities)

# ========== 7. 青少年活动中心/少年宫活动 ==========
youth_center_activities = [
    {
        "title": "上海市青少年活动中心共童成长营我们要做小学生啦",
        "venue": "上海市青少年活动中心",
        "city": "shanghai",
        "start_date": "2026-08-10",
        "end_date": "2026-08-21",
        "link": "https://m.sohu.com/a/1037462902_121106832/",
        "description": "10日营面向新一年级学生，汉语言读写写字训练、数学逻辑思维、德智体美音综合素养课程，培养良好学习习惯。",
        "fee": "以官方报价为准",
        "source": "上海市青少年活动中心",
        "family_friendly": True
    },
    {
        "title": "上海市青少年活动中心乐语创造入门A班",
        "venue": "上海市青少年活动中心",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-07-24",
        "link": "https://m.sohu.com/a/1037462902_121106832/",
        "description": "5日半日营面向新幼儿园中班孩子，语言素养培养看图说话表达，乐高机器人趣味拼搭锻炼动手能力。",
        "fee": "以官方报价为准",
        "source": "上海市青少年活动中心",
        "family_friendly": True
    },
    {
        "title": "上海市青少年活动中心爱乐趣智夏日营",
        "venue": "上海市青少年活动中心",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-21",
        "link": "https://m.sohu.com/a/1025690720_121106832/",
        "description": "面向小学二至五年级，上午暑假作业辅导温故知新，下午双语口才乐高AI创意美术跆拳道空手道等兴趣课程。",
        "fee": "以官方报价为准",
        "source": "上海市青少年活动中心",
        "family_friendly": True
    },
    {
        "title": "上海市青少年活动中心童心绘梦成长营",
        "venue": "上海市青少年活动中心",
        "city": "shanghai",
        "start_date": "2026-08-10",
        "end_date": "2026-08-21",
        "link": "https://m.sohu.com/a/1025690720_121106832/",
        "description": "面向小学二至四年级，融合国潮美学社非遗博物馆创意大工坊8款特色主题，一米高度看上海专属研学任务单。",
        "fee": "以官方报价为准",
        "source": "上海市青少年活动中心",
        "family_friendly": True
    },
    {
        "title": "上海市青少年活动中心非遗童趣衣路敦煌",
        "venue": "上海市青少年活动中心",
        "city": "shanghai",
        "start_date": "2026-08-10",
        "end_date": "2026-08-21",
        "link": "https://m.sohu.com/a/1025690720_121106832/",
        "description": "面向小学一至五年级，敦煌千年壁画灵感，面部彩绘可动藻井手作立体莫高窟彩绘服装设计四大创意板块。",
        "fee": "以官方报价为准",
        "source": "上海市青少年活动中心",
        "family_friendly": True
    },
    {
        "title": "徐汇区青少年活动中心AIGC影像OPC夏令营",
        "venue": "徐汇区青少年活动中心",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://sh.wenming.cn/xhwmw/xh_wcnr/202607/t20260706_7002284.html",
        "description": "走近百年徐汇主题，单人全链路创作模式，学生独立完成文案构思AI绘图视频剪辑配乐配音等全部创作。",
        "fee": "以官方报价为准",
        "source": "徐汇区青少年活动中心",
        "family_friendly": True
    },
    {
        "title": "徐汇区青少年活动中心民航模拟飞行舱工程集训营",
        "venue": "徐汇区青少年活动中心",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://sh.wenming.cn/xhwmw/xh_wcnr/202607/t20260706_7002284.html",
        "description": "光启青少年未来工程师培养计划，专业工程师全程指导，在职机长机械师授课，结构搭建3D建模AI算法软硬件调试。",
        "fee": "以官方报价为准",
        "source": "徐汇区青少年活动中心",
        "family_friendly": True
    },
    {
        "title": "徐汇区行走的五育课堂高中生科学夏令营",
        "venue": "上海交大复旦同济等6所高校",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://sh.wenming.cn/xhwmw/xh_wcnr/202607/t20260706_7002284.html",
        "description": "联合6所高校14个重点院系，520名高中生分批进入重点实验室科研场馆，人工智能生命科学新材料等前沿学科学习。",
        "fee": "以官方报价为准",
        "source": "徐汇区青少年活动中心",
        "family_friendly": True
    },
    {
        "title": "徐汇区青少年活动中心瓷汇未来景德镇研学",
        "venue": "江西景德镇",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://sh.wenming.cn/xhwmw/xh_wcnr/202607/t20260706_7002284.html",
        "description": "跟随非遗代表性传承人和专业教师学习浮雕彩绘釉上瓷绘立体陶艺，揉泥拉坯手绘装饰全程动手操作。",
        "fee": "以官方报价为准",
        "source": "徐汇区青少年活动中心",
        "family_friendly": True
    },
    {
        "title": "上海市少年儿童海防夏令营",
        "venue": "上海市青少年实践活动金山基地",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7657558040450810408/",
        "description": "五天四晚沉浸式铸海魂主题，军事训练沙滩大坝拉练海军对抗赛，上博东馆海洋研学乐高乐园海防创意拼搭。",
        "fee": "以官方报价为准",
        "source": "上海市青少年活动中心",
        "family_friendly": True
    },
]

activities.extend(youth_center_activities)

# ========== 8. 图书馆暑期少儿活动 ==========
library_activities = [
    {
        "title": "静安区图书馆沪语文化训练营",
        "venue": "静安区图书馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.shobserver.cn/staticsg/wap/newsDetail?id=1145654",
        "description": "面向5至12岁亲子家庭，以童谣绕口令等传递海派方言魅力，暑期六大系列近50场活动覆盖3至12岁小读者。",
        "fee": "免费",
        "source": "静安区图书馆",
        "family_friendly": True
    },
    {
        "title": "静安区图书馆物理趣味小课堂",
        "venue": "静安区图书馆闻喜路馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.shobserver.cn/staticsg/wap/newsDetail?id=1145654",
        "description": "光影变变变纸杯投影大冒险等趣味科学实验，火山喷发非牛顿流体小行星探秘等，把抽象知识转化为动手游戏。",
        "fee": "免费",
        "source": "静安区图书馆",
        "family_friendly": True
    },
    {
        "title": "宝山区图书馆邮轮原创绘本巡展",
        "venue": "宝山区图书馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.shobserver.cn/staticsg/wap/newsDetail?id=1145654",
        "description": "深度扎根宝山邮轮非遗红色滨江特色，邮轮原创绘本巡展与亲子故事会，擦亮宝山邮轮文化名片。",
        "fee": "免费",
        "source": "宝山区图书馆",
        "family_friendly": True
    },
    {
        "title": "宝山区图书馆儿童文学创作大赛",
        "venue": "宝山区图书馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.shobserver.cn/staticsg/wap/newsDetail?id=1145654",
        "description": "邀请儿童文学名家线下分享，推出儿童文学创作大赛，挖掘青少年写作潜力，提升文学素养。",
        "fee": "免费",
        "source": "宝山区图书馆",
        "family_friendly": True
    },
    {
        "title": "杨浦区图书馆Science童创营",
        "venue": "杨浦区图书馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.shobserver.cn/staticsg/wap/newsDetail?id=1145654",
        "description": "7月食虫植物生态盒制作、8月海洋水母手工，树立生态保护理念，培养科学探索精神。",
        "fee": "免费",
        "source": "杨浦区图书馆",
        "family_friendly": True
    },
    {
        "title": "杨浦区图书馆大中华寻宝记传统文化课",
        "venue": "杨浦区图书馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.shobserver.cn/staticsg/wap/newsDetail?id=1145654",
        "description": "以大中华寻宝记为载体，解读秦代三秦文化丝路甘肃诗词等，让孩子在趣味阅读中了解历史文化。",
        "fee": "免费",
        "source": "杨浦区图书馆",
        "family_friendly": True
    },
    {
        "title": "长宁区图书馆线装书装帧体验",
        "venue": "长宁区图书馆",
        "city": "shanghai",
        "start_date": "2026-07-11",
        "end_date": "2026-07-11",
        "link": "https://www.shanghai.gov.cn/nw17239/20260706/a07986eae3f74517aaa9bb639defcb21.html",
        "description": "亲手体验线装书装帧工艺，了解古籍保护知识，感受传统文化魅力，关注长宁区图书馆微信号预约。",
        "fee": "免费",
        "source": "长宁区图书馆",
        "family_friendly": True
    },
    {
        "title": "长宁区图书馆茶百戏韵宋代四雅之点茶",
        "venue": "长宁区图书馆",
        "city": "shanghai",
        "start_date": "2026-07-25",
        "end_date": "2026-07-25",
        "link": "https://www.shanghai.gov.cn/nw17239/20260706/a07986eae3f74517aaa9bb639defcb21.html",
        "description": "传统文化美育体验活动，学习宋代点茶技艺，感受古代文人雅致生活方式，适合亲子共同参与。",
        "fee": "免费",
        "source": "长宁区图书馆",
        "family_friendly": True
    },
    {
        "title": "长宁区少年儿童图书馆非遗面塑家风家训",
        "venue": "长宁区少年儿童图书馆东馆",
        "city": "shanghai",
        "start_date": "2026-07-03",
        "end_date": "2026-07-03",
        "link": "https://www.shanghai.gov.cn/nw17239/20260706/a07986eae3f74517aaa9bb639defcb21.html",
        "description": "非遗面塑体验，将家风家训融入面塑创作，让孩子在动手过程中传承中华传统美德。",
        "fee": "免费",
        "source": "长宁区少儿图书馆",
        "family_friendly": True
    },
    {
        "title": "长宁区少儿图书馆长耳兔生物多样性讲座",
        "venue": "长宁区少年儿童图书馆东馆",
        "city": "shanghai",
        "start_date": "2026-07-04",
        "end_date": "2026-07-04",
        "link": "https://www.shanghai.gov.cn/nw17239/20260706/a07986eae3f74517aaa9bb639defcb21.html",
        "description": "虫虫总动员灌丛下的生命主题，认识各种昆虫了解生物多样性，激发孩子对大自然的好奇心和保护意识。",
        "fee": "免费",
        "source": "长宁区少儿图书馆",
        "family_friendly": True
    },
]

activities.extend(library_activities)

# ========== 9. 高校研学活动 ==========
university_activities = [
    {
        "title": "复旦大学AI+新工科高中生夏令营",
        "venue": "复旦大学邯郸校区/江湾校区",
        "city": "shanghai",
        "start_date": "2026-07-20",
        "end_date": "2026-08-13",
        "link": "https://m.sohu.com/a/1048973071_121106832/",
        "description": "未来学者体验计划，顶尖师资授课，前沿领域探秘，国家重点实验室科研实践，颁发复旦非学历结业证书。",
        "fee": "4800元/人",
        "source": "复旦大学终身教育学院",
        "family_friendly": True
    },
    {
        "title": "复旦大学综合素质拓展夏令营",
        "venue": "复旦大学",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.zizzs.com/gk/jianzhang/218607.html",
        "description": "面向初三及以上学生，综合素养提升，名校学子面对面交流，提前感受顶尖高校学术氛围与校园生活。",
        "fee": "以官方报价为准",
        "source": "复旦大学",
        "family_friendly": True
    },
    {
        "title": "同济大学暑期STEM创新百人计划研学营",
        "venue": "同济大学",
        "city": "shanghai",
        "start_date": "2026-08-03",
        "end_date": "2026-08-07",
        "link": "https://www.zizzs.com/gk/jianzhang/218607.html",
        "description": "STEM创新实践，工程思维训练，同济大学教授指导，实验室参观体验，培养科学素养与创新能力。",
        "fee": "以官方报价为准",
        "source": "同济大学",
        "family_friendly": True
    },
    {
        "title": "复旦大学相辉学堂未来科学家夏令营",
        "venue": "复旦大学",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.zizzs.com/gk/jianzhang/218607.html",
        "description": "面向优秀高中生，科研启蒙与学术探索，各学科前沿讲座，与教授和研究生交流，激发科学兴趣。",
        "fee": "以官方报价为准",
        "source": "复旦大学",
        "family_friendly": True
    },
    {
        "title": "AI创未来全国青少年上海研学营",
        "venue": "上海市青少年活动中心及各高校",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1043912374_121106854/",
        "description": "5天4晚3880元/人，亲临世界人工智能大会，上海中心探秘、AI精品课程、航宇科普中心、上海交大研学、浦江夜游。",
        "fee": "3880元/人",
        "source": "上海市青少年活动中心",
        "family_friendly": True
    },
]

activities.extend(university_activities)

# ========== 10. 剧场/儿童演出 ==========
theater_activities = [
    {
        "title": "儿童剧奥特传奇之外星生物来袭",
        "venue": "保利上海城市剧院",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.meet-in-shanghai.net/cn/news/a-min-is-astonishing-the-excitement-never-stops-all-year-%E2%86%92-532454/",
        "description": "经典奥特曼IP正版授权儿童剧，热血剧情与精彩打斗，圆孩子英雄梦，暑期合家欢必看演出。",
        "fee": "以官方票价为准",
        "source": "保利上海城市剧院",
        "family_friendly": True
    },
    {
        "title": "儿童剧屁屁侦探之怪盗U对怪盗U",
        "venue": "保利上海城市剧院",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.meet-in-shanghai.net/cn/news/a-min-is-astonishing-the-excitement-never-stops-all-year-%E2%86%92-532454/",
        "description": "人气绘本IP改编儿童剧，推理悬疑互动十足，锻炼孩子观察力和逻辑思维，亲子共同解谜乐趣多。",
        "fee": "以官方票价为准",
        "source": "保利上海城市剧院",
        "family_friendly": True
    },
    {
        "title": "3D多媒体儿童音乐剧绿野仙踪",
        "venue": "保利上海城市剧院",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.meet-in-shanghai.net/cn/news/a-min-is-astonishing-the-excitement-never-stops-all-year-%E2%86%92-532454/",
        "description": "经典童话改编，3D多媒体技术打造奇幻奥兹国，动听音乐与精彩表演，带孩子进入梦幻童话世界。",
        "fee": "以官方票价为准",
        "source": "保利上海城市剧院",
        "family_friendly": True
    },
    {
        "title": "亲子音乐剧爱丽丝梦游仙境中文版",
        "venue": "保利上海城市剧院",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.meet-in-shanghai.net/cn/news/a-min-is-astonishing-the-excitement-never-stops-all-year-%E2%86%92-532454/",
        "description": "加拿大多媒体亲子音乐剧中文版，裸眼3D视觉效果，经典童话全新演绎，沉浸式奇幻体验。",
        "fee": "以官方票价为准",
        "source": "保利上海城市剧院",
        "family_friendly": True
    },
    {
        "title": "布鲁伊的大宝藏亲子互动舞台剧",
        "venue": "保利上海城市剧院",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.meet-in-shanghai.net/cn/news/a-min-is-astonishing-the-excitement-never-stops-all-year-%E2%86%92-532454/",
        "description": "英国BBC正版授权，全球超人气动画改编，亲子互动欢乐满满，适合低龄儿童的温馨治愈舞台剧。",
        "fee": "以官方票价为准",
        "source": "保利上海城市剧院",
        "family_friendly": True
    },
    {
        "title": "木偶腹语儿童剧小猩猩的大圣梦",
        "venue": "浦东新区金海文化艺术中心",
        "city": "shanghai",
        "start_date": "2026-07-18",
        "end_date": "2026-07-18",
        "link": "http://m.toutiao.com/group/7663377358283424271/",
        "description": "腹语表演+趣味互动，小猩猩团团崇拜齐天大圣的成长故事，传递不必成为别人做自己就闪光的哲理。",
        "fee": "以官方票价为准",
        "source": "浦东新区金海文化艺术中心",
        "family_friendly": True
    },
    {
        "title": "上海儿童艺术剧场夏日音乐岛",
        "venue": "上海儿童艺术剧场",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.weibo.cn/detail/5318716108834873",
        "description": "暑期音乐主题活动，爵士亲子音乐会、大鲸鱼交响乐团十周年专场、欢唱团音乐剧GALA、音乐之声夏令营。",
        "fee": "以官方票价为准",
        "source": "上海儿童艺术剧场",
        "family_friendly": True
    },
    {
        "title": "小顽家飞翔的浴缸想象力儿童剧",
        "venue": "小顽家艺术剧场世纪汇店",
        "city": "shanghai",
        "start_date": "2026-08-05",
        "end_date": "2026-08-21",
        "link": "https://shanghaiertongqinzi.df962388.com/",
        "description": "想象力爆棚的创意儿童剧，一只会飞的浴缸带来奇妙冒险，启发孩子想象力与创造力。",
        "fee": "240-720元",
        "source": "小顽家艺术剧场",
        "family_friendly": True
    },
    {
        "title": "亲子肢体剧山海奇幻梦",
        "venue": "中国福利会儿童艺术剧院马兰花剧场",
        "city": "shanghai",
        "start_date": "2026-08-22",
        "end_date": "2026-08-22",
        "link": "https://shanghaiertongqinzi.df962388.com/",
        "description": "浙江儿童艺术剧团出品，山海经神话故事改编，肢体表演与视觉创意结合，传统文化启蒙好选择。",
        "fee": "80-280元",
        "source": "中福会儿艺马兰花剧场",
        "family_friendly": True
    },
]

activities.extend(theater_activities)

# ========== 11. 汽车博物馆活动 ==========
auto_museum_activities = [
    {
        "title": "上海汽车博物馆周一不闭馆暑期特别开放",
        "venue": "上海汽车博物馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://www.shautomuseum.com/news/info/352",
        "description": "整个暑假62天周一不闭馆，暑期双人票99元/套，全馆通票1大1小188元，含摩都儿童互动空间。",
        "fee": "暑期双人票99元",
        "source": "上海汽车博物馆",
        "family_friendly": True
    },
    {
        "title": "上海汽车博物馆博物馆之夜",
        "venue": "上海汽车博物馆",
        "city": "shanghai",
        "start_date": "2026-07-18",
        "end_date": "2026-08-01",
        "link": "http://www.shautomuseum.com/news/info/352",
        "description": "7月18日、25日、8月1日延时开放至19:30，16:00后半价优惠，公益讲解、避障/声控小车手作体验。",
        "fee": "16:00后半价",
        "source": "上海汽车博物馆",
        "family_friendly": True
    },
    {
        "title": "上海汽车博物馆火星计划一日研学营地",
        "venue": "上海汽车博物馆",
        "city": "shanghai",
        "start_date": "2026-07-04",
        "end_date": "2026-07-18",
        "link": "http://www.shautomuseum.com/news/info/352",
        "description": "大交通主题科技类研学，PBL项目式探究，打造原创火星教具车，展厅互动探索户外全地形测试。",
        "fee": "498元/人",
        "source": "上海汽车博物馆",
        "family_friendly": True
    },
    {
        "title": "上海玻璃博物馆暑期周一特惠",
        "venue": "上海玻璃博物馆",
        "city": "shanghai",
        "start_date": "2026-07-06",
        "end_date": "2026-08-31",
        "link": "https://cj.sina.cn/article/norm_detail?froms=ttmp&url=https%3A%2F%2Ffinance.sina.com.cn%2Fwm%2F2026-07-06%2Fdoc-inifvkkf8817805.shtml%3Ffinpagefr%3Dttzz",
        "description": "暑期每日开放周一不闭馆，周一限定特惠票仅66元一票逛遍所有场馆，丰富体验项目适合亲子。",
        "fee": "周一特惠票66元",
        "source": "上海玻璃博物馆",
        "family_friendly": True
    },
]

activities.extend(auto_museum_activities)

# ========== 12. 西岸/徐汇滨江活动 ==========
xuhui_riverside_activities = [
    {
        "title": "史前星球恐龙篇沉浸式巨幕体验",
        "venue": "西岸美术馆B1智造展厅",
        "city": "shanghai",
        "start_date": "2026-06-27",
        "end_date": "2027-01-27",
        "link": "https://www.meet-in-shanghai.net/cn/news/the-2026-shanghai-tourism-festival-summer-tourism-season-kicks-off-on-july-8-170-activities-and-six-major-themed-weeks-are-online-388024/",
        "description": "BBC经典纪录片改编，360°沉浸式投影系统，1:1还原史前恐龙，全景环幕打造沉浸式远古世界。",
        "fee": "收费",
        "source": "西岸美术馆",
        "family_friendly": True
    },
    {
        "title": "迪士尼米奇奇妙之旅快闪店",
        "venue": "徐汇滨江船坞区域",
        "city": "shanghai",
        "start_date": "2026-06-18",
        "end_date": "2026-08-02",
        "link": "http://m.toutiao.com/group/7663419363839509019/",
        "description": "八米高飞行员米奇巨型气模，米妮唐老鸭雕塑，复古大头贴限定文创，亲子出游必打卡点位。",
        "fee": "免费入场",
        "source": "徐汇滨江",
        "family_friendly": True
    },
    {
        "title": "西岸凤巢HeyBlue Oasis水上乐园",
        "venue": "西岸凤巢大师公园内",
        "city": "shanghai",
        "start_date": "2026-06-20",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7663419363839509019/",
        "description": "整片戏水区域配备多样水上互动设施，大片泳池适配全年龄段玩水，带娃消暑轻松省心。",
        "fee": "收费",
        "source": "西岸凤巢",
        "family_friendly": True
    },
    {
        "title": "GATE M水岸露天电影节",
        "venue": "西岸梦中心西岸凤巢",
        "city": "shanghai",
        "start_date": "2026-07-02",
        "end_date": "2026-07-20",
        "link": "http://m.toutiao.com/group/7663419363839509019/",
        "description": "四大观影场地三十余部动画经典科幻影片循环放映，江风晚霞伴光影，夏日浪漫氛围感拉满。",
        "fee": "免费（部分需预约）",
        "source": "西岸梦中心",
        "family_friendly": True
    },
    {
        "title": "元界夏日嘉年华",
        "venue": "元界元宇宙街区",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-30",
        "link": "https://nw.eastday.com/zq/zw/20260716/387c7a682da5229b3cfca03bad63f028.html",
        "description": "绝区零明日方舟一人之下三大热门游戏动漫IP，游戏动漫快闪主题市集音乐演艺户外休闲惠民消费。",
        "fee": "部分活动需预约",
        "source": "鑫耀光环Live",
        "family_friendly": True
    },
]

activities.extend(xuhui_riverside_activities)

# ========== 13. 崇明/青浦/奉贤郊野活动 ==========
suburban_activities = [
    {
        "title": "崇明东滩自然童行探索湿地研学夏令营",
        "venue": "崇明东滩湿地公园",
        "city": "shanghai",
        "start_date": "2026-07-24",
        "end_date": "2026-08-23",
        "link": "http://m.toutiao.com/group/7661942746675954211/",
        "description": "三天两晚独立营，湿地科普物种保护户外生存自然夜游生态农业公益护鸟，1888元/人每期限30人。",
        "fee": "1888元/人",
        "source": "崇明东滩湿地公园",
        "family_friendly": True
    },
    {
        "title": "崇明中国寻根之旅夏令营",
        "venue": "崇明各文化场馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7661157395813270058/",
        "description": "海外华裔青少年和崇明学生一起走进中华鲟自然保护基地瀛东村史馆，体验崇明土布非遗自然观察。",
        "fee": "以官方报价为准",
        "source": "崇明团区委",
        "family_friendly": True
    },
    {
        "title": "青浦朱家角安庄村蓝汐桨板体验",
        "venue": "青浦区朱家角镇安庄村",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7662978541574734371/",
        "description": "大莲湖淀山湖水清景美，桨板皮划艇俱乐部，新手友好水域开阔平静，亲子水上运动好去处。",
        "fee": "以俱乐部报价为准",
        "source": "青浦区文旅",
        "family_friendly": True
    },
    {
        "title": "青浦薛间村森林书屋生态游",
        "venue": "青浦区朱家角镇薛间村",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7662978541574734371/",
        "description": "1600亩生态林15条蜿蜒河道，迷你版青西郊野公园，森林书屋村咖林间栈道，亲子自然休闲好去处。",
        "fee": "免费",
        "source": "青浦区文旅",
        "family_friendly": True
    },
    {
        "title": "奉贤皮划艇暑期欢乐营",
        "venue": "奉贤区树修教育培训中心",
        "city": "shanghai",
        "start_date": "2026-07-04",
        "end_date": "2026-08-01",
        "link": "https://www.163.com/dy/article/KULPHN8N053478CE.html",
        "description": "2天1夜住宿营，共5期每期8人小班精品教学，专业教练指导，学习皮划艇技能清凉一夏。",
        "fee": "以官方报价为准",
        "source": "奉贤区文旅",
        "family_friendly": True
    },
]

activities.extend(suburban_activities)

# ========== 14. 嘉定区暑期活动 ==========
jiading_activities = [
    {
        "title": "嘉定博物馆我的博物馆日记亲子文博研学季",
        "venue": "嘉定博物馆",
        "city": "shanghai",
        "start_date": "2026-06-25",
        "end_date": "2026-08-31",
        "link": "https://whlyj.sh.gov.cn/gqfc/20260626/ddbe4df404b8473d9858bcc9780f689f.html",
        "description": "亲子文博研学活动，通过日记形式记录博物馆参观心得，深入了解嘉定历史文化，亲子共同成长。",
        "fee": "免费",
        "source": "嘉定博物馆",
        "family_friendly": True
    },
    {
        "title": "上海汽车博物馆神奇的闪电新能源科普",
        "venue": "上海汽车博物馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://whlyj.sh.gov.cn/gqfc/20260626/ddbe4df404b8473d9858bcc9780f689f.html",
        "description": "新能源汽车科普主题活动，了解电动汽车发展历程与未来趋势，动手实验激发科学兴趣。",
        "fee": "含门票",
        "source": "上海汽车博物馆",
        "family_friendly": True
    },
    {
        "title": "南翔古镇暑期主题活动",
        "venue": "南翔古镇",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://whlyj.sh.gov.cn/gqfc/20260626/ddbe4df404b8473d9858bcc9780f689f.html",
        "description": "潮生仲夏荷风送爽主题，书画作品展故事讲演大赛携宠皮划艇邀请赛智游南翔人文科技研学。",
        "fee": "部分收费",
        "source": "南翔古镇",
        "family_friendly": True
    },
    {
        "title": "保利艺夏演出季打开艺术之门",
        "venue": "上海保利大剧院",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://whlyj.sh.gov.cn/gqfc/20260626/ddbe4df404b8473d9858bcc9780f689f.html",
        "description": "芭蕾皮影音乐会等儿童剧目贯穿整个暑假，户外水景剧场湖畔视听盛宴，亲子艺术熏陶好去处。",
        "fee": "以官方票价为准",
        "source": "上海保利大剧院",
        "family_friendly": True
    },
    {
        "title": "嘉北郊野公园趣野一夏户外探索季",
        "venue": "嘉北郊野公园",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://whlyj.sh.gov.cn/gqfc/20260626/ddbe4df404b8473d9858bcc9780f689f.html",
        "description": "户外探索亲子活动，稻田野趣自然研学，亲子露营草坪活动，郊野风光中感受自然乐趣。",
        "fee": "免费入园",
        "source": "嘉北郊野公园",
        "family_friendly": True
    },
    {
        "title": "马陆葡萄公园藤下时光果香漫游",
        "venue": "嘉定马陆葡萄主题公园",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://whlyj.sh.gov.cn/gqfc/20260626/ddbe4df404b8473d9858bcc9780f689f.html",
        "description": "葡萄采摘田园体验，了解葡萄种植知识，品尝各种优质葡萄品种，亲子农耕科普好去处。",
        "fee": "门票+采摘另计",
        "source": "马陆葡萄主题公园",
        "family_friendly": True
    },
]

activities.extend(jiading_activities)

# ========== 15. 上美影/商业综合体活动 ==========
mall_activities = [
    {
        "title": "上美影泡泡米国漫美育成长季",
        "venue": "上美影泡泡米益智乐园环球港店",
        "city": "shanghai",
        "start_date": "2026-07-08",
        "end_date": "2026-08-31",
        "link": "https://www.meet-in-shanghai.net/cn/news/the-2026-shanghai-tourism-festival-summer-tourism-season-kicks-off-on-july-8-170-activities-and-six-major-themed-weeks-are-online-388024/",
        "description": "上美影经典动画IP为核心，国漫手作西游研学光影剧场非遗美育课堂，沉浸式感受东方美学。",
        "fee": "购票入园",
        "source": "上美影泡泡米",
        "family_friendly": True
    },
    {
        "title": "钟书阁泰晤士店书店奇妙夜",
        "venue": "钟书阁泰晤士小镇店",
        "city": "shanghai",
        "start_date": "2026-08-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7539499439153545782/",
        "description": "图书管理员职业体验，神探迈克狐剧本杀，书签制作，让孩子爱上阅读与书店的奇妙夜晚。",
        "fee": "收费",
        "source": "钟书阁",
        "family_friendly": True
    },
    {
        "title": "西西弗书店屁屁侦探解谜乐园游园会",
        "venue": "西西弗书店鑫耀光环Live店",
        "city": "shanghai",
        "start_date": "2026-06-06",
        "end_date": "2026-06-07",
        "link": "https://thepaper.huodongxing.com/event/7860468116012?qd=8828363103856",
        "description": "日本超人气童书IP，解谜游戏故事会，亲子共同挑战智力谜题，培养阅读兴趣与逻辑思维。",
        "fee": "免费",
        "source": "西西弗书店",
        "family_friendly": True
    },
    {
        "title": "世博文化公园申园纳夏凉活动",
        "venue": "世博文化公园申园",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7659976244997440009/",
        "description": "江南古典园林暑期专属活动，汉服租赁游园，古法消夏手作团扇香囊DIY，夜间园林雅集非遗市集。",
        "fee": "免费入园",
        "source": "世博文化公园",
        "family_friendly": True
    },
]

activities.extend(mall_activities)

# ========== 16. 上海旅游节六大主题周活动 ==========
tourism_festival_activities = [
    {
        "title": "2026上海旅游节暑期旅游季",
        "venue": "全市各文旅场所",
        "city": "shanghai",
        "start_date": "2026-07-08",
        "end_date": "2026-08-31",
        "link": "https://www.meet-in-shanghai.net/cn/news/the-2026-shanghai-tourism-festival-summer-tourism-season-kicks-off-on-july-8-170-activities-and-six-major-themed-weeks-are-online-388024/",
        "description": "第37届上海旅游节暑期季，六大主题周170项活动，海上萌主文博遗韵烟火申活艺彩申城乡野牧歌探趣魔都。",
        "fee": "部分免费部分收费",
        "source": "上海旅游节",
        "family_friendly": True
    },
    {
        "title": "上海旅游节文博奇妙夜打卡地图",
        "venue": "全市各文博场馆",
        "city": "shanghai",
        "start_date": "2026-07-08",
        "end_date": "2026-08-31",
        "link": "https://www.meet-in-shanghai.net/cn/news/the-2026-shanghai-tourism-festival-summer-tourism-season-kicks-off-on-july-8-170-activities-and-six-major-themed-weeks-are-online-388024/",
        "description": "联动全市文博场馆推出夜场导览古物修复工坊等活动，打卡集章兑换纪念礼品，亲子文博深度体验。",
        "fee": "部分免费",
        "source": "上海旅游节",
        "family_friendly": True
    },
    {
        "title": "诗韵上海逐景寻诗打卡行",
        "venue": "全市各文旅地标",
        "city": "shanghai",
        "start_date": "2026-07-08",
        "end_date": "2026-08-31",
        "link": "https://www.meet-in-shanghai.net/cn/news/the-2026-shanghai-tourism-festival-summer-tourism-season-kicks-off-on-july-8-170-activities-and-six-major-themed-weeks-are-online-388024/",
        "description": "植入诗词文化元素设置打卡点，串联城市历史建筑与风光节点，边走边打卡集章沉浸式品读城市古韵。",
        "fee": "免费",
        "source": "上海旅游节",
        "family_friendly": True
    },
    {
        "title": "乡野牧歌周辰山植物园系列活动",
        "venue": "上海辰山植物园及周边",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.meet-in-shanghai.net/cn/news/the-2026-shanghai-tourism-festival-summer-tourism-season-kicks-off-on-july-8-170-activities-and-six-major-themed-weeks-are-online-388024/",
        "description": "联动欢乐谷玛雅水公园广富林新浜荷花天马星空村，亲子夜游露营观星萌宠互动水上运动自然研学。",
        "fee": "各景点单独收费",
        "source": "上海旅游节",
        "family_friendly": True
    },
    {
        "title": "闵行博物馆清韵康雍乾时期文物特展",
        "venue": "闵行区博物馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-10-07",
        "link": "https://www.meet-in-shanghai.net/cn/news/the-2026-shanghai-tourism-festival-summer-tourism-season-kicks-off-on-july-8-170-activities-and-six-major-themed-weeks-are-online-388024/",
        "description": "与国博首博等14家文博单位合作，展出康熙雍正乾隆三代珍贵文物120余件套，了解清代帝王生活。",
        "fee": "收费",
        "source": "闵行区博物馆",
        "family_friendly": True
    },
]

activities.extend(tourism_festival_activities)

# ========== 17. 杨浦区未成年人暑假活动 ==========
yangpu_activities = [
    {
        "title": "杨浦区AI赋能非遗创新体验营",
        "venue": "杨浦区青少年活动中心",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.shyp.gov.cn/shypq/wcnrbh-xx/20260618/507746.html",
        "description": "智创非遗共生未来主题，AI非遗讲座非遗场馆实践智创工坊共创成果策展，AI图像识别绘画对话工具辅助探究。",
        "fee": "免费",
        "source": "杨浦区教育局",
        "family_friendly": True
    },
    {
        "title": "杨浦区轻盈成长计划体重健康管理营",
        "venue": "杨浦区妇女儿童服务指导中心",
        "city": "shanghai",
        "start_date": "2026-07-12",
        "end_date": "2026-09-06",
        "link": "https://www.shyp.gov.cn/shypq/wcnrbh-xx/20260618/507746.html",
        "description": "新华医院注册营养师领衔，认知习惯饮食习惯运动习惯健康小组，关注7-15岁儿童体重与身心健康。",
        "fee": "免费",
        "source": "杨浦区妇联",
        "family_friendly": True
    },
    {
        "title": "杨浦区AI心理健康主题海报创作活动",
        "venue": "线上（杨浦心馨家园公众号）",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-09-01",
        "link": "https://www.shyp.gov.cn/shypq/wcnrbh-xx/20260618/507746.html",
        "description": "鼓励中小学生运用AI技术释放创意潜能，海报设计营造积极向上温暖健康的心理氛围，活动期均可报名。",
        "fee": "免费",
        "source": "杨浦区未成年人心理辅导中心",
        "family_friendly": True
    },
]

activities.extend(yangpu_activities)

# ========== 18. 更多特色活动补充 ==========
more_activities = [
    {
        "title": "小小绿色夏令营华侨银行",
        "venue": "张江及全市各点",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.shobserver.cn/staticsg/wap/newsDetail?id=1146035",
        "description": "绿色与科技主题三天夏令营，风力发电机器人制作匹克球体验绿色金融家课，张江AI应用商店参观实践。",
        "fee": "公益免费",
        "source": "华侨银行中国",
        "family_friendly": True
    },
    {
        "title": "新场镇宝藏小屋暑期公益课敦煌STEAM研学",
        "venue": "浦东新区新场镇",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.pudong.gov.cn/016027005/index.html",
        "description": "跟着敦煌解锁趣味STEAM研学之旅，公益课程寓教于乐，艺术与科学结合的独特体验。",
        "fee": "公益免费",
        "source": "浦东新区新场镇",
        "family_friendly": True
    },
    {
        "title": "徐汇亲子阅读营书香润童心",
        "venue": "徐汇区儿童关爱服务中心",
        "city": "shanghai",
        "start_date": "2026-06-01",
        "end_date": "2026-07-31",
        "link": "http://m.toutiao.com/group/7654505435437613609/",
        "description": "融合身心健康航空航天科普非遗研学国风美学公益阅读等主题，沉浸式看世界学知识悟文化共成长。",
        "fee": "免费",
        "source": "徐汇区民政局",
        "family_friendly": True
    },
    {
        "title": "康健体育公园亲子体育嘉年华",
        "venue": "康健体育公园",
        "city": "shanghai",
        "start_date": "2026-06-27",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7654130518803448354/",
        "description": "足球网球击剑游泳篮球体适能一站式解锁，草地击瓶泡泡大作战精准投篮螃蟹搬家趣味项目。",
        "fee": "公益免费（需预约）",
        "source": "徐汇区体育局",
        "family_friendly": True
    },
    {
        "title": "外滩源足球嘉年华",
        "venue": "外滩源圆明园路步行街",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-07-26",
        "link": "https://cj.sina.cn/article/norm_detail?froms=ttmp&url=https%3A%2F%2Ffinance.sina.com.cn%2Fwm%2F2026-07-06%2Fdoc-inifvkkf8817805.shtml%3Ffinpagefr%3Dttzz",
        "description": "世界杯主题夏日派对，热血绿茵氛围百年欧式建筑烟火特色美食潮流创意玩乐，亲子足球互动体验。",
        "fee": "免费入场",
        "source": "外滩源",
        "family_friendly": True
    },
    {
        "title": "豫园黄油小熊烘焙主题展",
        "venue": "豫园商城",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://news.qq.com/rain/a/20260605A08TC700",
        "description": "现象级IP全国首个联名糖水店，泰文化周国际非遗文化，城市水乐园二次元快闪轮番登场。",
        "fee": "免费入场",
        "source": "豫园商城",
        "family_friendly": True
    },
    {
        "title": "思南夜派对气泡慢摇周",
        "venue": "思南公馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-07-31",
        "link": "http://news.qq.com/rain/a/20260605A08TC700",
        "description": "精酿美食潮流文创市集，民谣爵士轻流行现场演艺艺术装置展，适合亲子夏日傍晚休闲漫步。",
        "fee": "免费入场",
        "source": "思南公馆",
        "family_friendly": True
    },
    {
        "title": "金山十八斗半日研学营",
        "venue": "金山区枫泾镇",
        "city": "shanghai",
        "start_date": "2026-07-18",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7662947664883696134/",
        "description": "传统建筑文化课程研学，199元/户一大一小，小朋友单独制作，满15组成团，提前预订。",
        "fee": "199元/户（一大一小）",
        "source": "金山区文旅",
        "family_friendly": True
    },
    {
        "title": "盛宅村城市猫岛亲子一日游",
        "venue": "宝山区盛宅村",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7654463135662834222/",
        "description": "近500只温顺猫咪互动科普，搭配蔬果采摘森林骑行，打造低龄儿童友好型治愈系一日游。",
        "fee": "以实际收费为准",
        "source": "宝山区文旅",
        "family_friendly": True
    },
    {
        "title": "浦东航头镇菌菇小院采摘科普",
        "venue": "浦东新区航头镇菌菇小院",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7654463135662834222/",
        "description": "食用菌采摘科普，了解菌菇生长知识，亲手采摘新鲜菌菇，亲子农耕科普好去处。",
        "fee": "以实际收费为准",
        "source": "浦东新区文旅",
        "family_friendly": True
    },
    {
        "title": "浦东大团镇歆香农场双语自然课堂",
        "venue": "浦东新区大团镇歆香农场",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7654463135662834222/",
        "description": "双语自然课堂，果园认植物林间烧烤，适配家庭团建亲子自然教育，边玩边学英语。",
        "fee": "以实际收费为准",
        "source": "浦东新区文旅",
        "family_friendly": True
    },
    {
        "title": "朱家角古镇艺韵江南主题活动",
        "venue": "青浦区朱家角古镇",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7659976244997440009/",
        "description": "河道边每日古琴昆曲江南评弹公益演出，摇橹船穿行白墙黛瓦，非遗手作体验，沉浸式水乡文化。",
        "fee": "免费入园",
        "source": "朱家角古镇",
        "family_friendly": True
    },
    {
        "title": "上海儿童博物馆漫游太空等主题活动",
        "venue": "上海儿童博物馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7645920405466677800/",
        "description": "漫游太空邮忆时光亲子桌游非遗泥塑亲子阅读新能源科创等丰富多彩互动活动，有趣有爱有意义。",
        "fee": "免费",
        "source": "上海儿童博物馆",
        "family_friendly": True
    },
    {
        "title": "奉贤碧海金沙沙滩戏水",
        "venue": "奉贤碧海金沙",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7654463135662834222/",
        "description": "7万平方米沙滩，海湾国家森林公园千亩荷塘，泛舟赏荷水上索道赶海拾贝全覆盖，夏日消暑首选。",
        "fee": "门票以官方为准",
        "source": "奉贤区文旅",
        "family_friendly": True
    },
    {
        "title": "青浦蟠龙天地荷月夜游节",
        "venue": "青浦蟠龙新天地",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7654463135662834222/",
        "description": "长达3公里水上光影秀荷塘夜游，水上夜市漂流酒馆夜游巡游，夏日夜游新地标。",
        "fee": "免费入园",
        "source": "蟠龙天地",
        "family_friendly": True
    },
]

activities.extend(more_activities)

# 保存到文件
output_path = '/workspace/goout/output/raw/real_activities_shanghai_batch4.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(activities, f, ensure_ascii=False, indent=2)

print(f"成功生成 {len(activities)} 个活动")
print(f"保存路径: {output_path}")
