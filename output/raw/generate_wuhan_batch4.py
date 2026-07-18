import json

activities = []

# ==================== 1. 各区县暑期活动 ====================

# 江岸区
activities.append({
    "title": "江岸区非遗亲子游·文化伴成长线路",
    "venue": "江岸区汉口历史风貌区（吉庆民俗街、武汉市群众艺术馆、巴公房子、人民剧院汉剧博物馆等）",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.ctnews.com.cn/wenhua/m/content/2026-07/02/content_189235.html",
    "description": "以汉口历史风貌区为核心，串联吉庆民俗街非遗特色街区、武汉市群众艺术馆民俗展示厅、巴公房子、人民剧院汉剧博物馆、中南剧场木偶剧场、解放公园楚香本草博览苑等特色点位。可品尝武汉传统美食，参观汉绣、面塑、武汉木雕船模、剪纸等非遗展陈，参与剪纸、面塑、楚香等互动体验课程，观看武汉杖头木偶戏、汉剧等非遗展演。",
    "fee": "部分免费",
    "source": "湖北武汉江岸区推出非遗亲子游·文化伴成长线路",
    "family_friendly": True
})

activities.append({
    "title": "2026武汉渡江嘉年华",
    "venue": "汉口江滩三阳广场（主会场）、武昌汉阳门花园（分会场）",
    "city": "wuhan",
    "start_date": "2026-07-15",
    "end_date": "2026-07-17",
    "link": "http://m.cjn.cn/Detail/?id=5518904&typeid=0",
    "description": "以荷你游一夏为主题的渡江嘉年华，两大会场同步登场。设有荷风豚豚打卡地标、荷尔蒙渡江音乐派对、夏日亲子水枪大战、水上运动展销区等活动。集结来自24个城市的80+网红品牌美食，涵盖烘焙、冰饮、特色小吃等全品类，还有1200份免费盲盒餐食试吃。",
    "fee": "免费",
    "source": "2026武汉渡江嘉年华游玩攻略",
    "family_friendly": True
})

# 江汉区
activities.append({
    "title": "江汉区红领巾讲解员实践活动",
    "venue": "江汉区各革命旧址、文博场馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7657014676622033414/",
    "description": "江汉团区委、区少工委精心定制的暑期实践计划，招募40名小学三至六年级少先队员。提供专业培训（语言表达、形体礼仪、红色历史、讲解技巧），打卡上岗走进江汉区革命旧址和文博场馆实地讲解，还有亲子义卖、Citywalk行走的思政课、实践激励等丰富内容。",
    "fee": "免费",
    "source": "江汉区红领巾讲解员实践活动",
    "family_friendly": True
})

activities.append({
    "title": "童小楚的书铺少图快借活动",
    "venue": "江汉路新华书店",
    "city": "wuhan",
    "start_date": "2026-07-15",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663313279355290166/",
    "description": "凡持有武汉市少年儿童图书馆借阅卡的读者，均可前往江汉路新华书店现场挑选心仪图书，符合条件可直接现场办理借阅手续，将新书当场免费带回家。实现读者选书、图书馆买单、现场借走的创新服务模式，打通公共文化服务最后一公里。",
    "fee": "免费需办证",
    "source": "2026武汉青少年暑期阅读季启幕",
    "family_friendly": True
})

# 武昌区
activities.append({
    "title": "武昌区第十四届社区亲子读书季",
    "venue": "武昌区50余个阅读空间",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hb.people.com.cn/n2/2026/0704/c192237-41629497.html",
    "description": "以武昌区50余个阅读空间为主阵地，拟开展54场文明实践活动。包括翻书闯长征红色阅读知识擂台、AI带你读武昌趣味人工智能魔法训练营、汉腔萌娃武汉方言故事会、作家面对面趣味写作训练营等七类特色活动，将阅读+研学深度融合。",
    "fee": "免费",
    "source": "武昌区暑期集中行动启动",
    "family_friendly": True
})

activities.append({
    "title": "武昌区科普润万家科普活动",
    "venue": "武昌区各社区及科普阵地",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hb.people.com.cn/n2/2026/0704/c192237-41629497.html",
    "description": "武昌区科协推出50余场社区体验课、20场科普研学行，以及覆盖全区的科普知识网络竞答。内容涵盖科学实验、科普研学、知识竞赛等多种形式，让青少年在暑期近距离接触科学、激发探索热情。",
    "fee": "免费",
    "source": "武昌区暑期集中行动启动",
    "family_friendly": True
})

activities.append({
    "title": "武昌古城号观光巴士",
    "venue": "武昌古城14个站点（户部巷、红巷、昙华林、黄鹤楼等）",
    "city": "wuhan",
    "start_date": "2026-06-22",
    "end_date": "2026-12-31",
    "link": "https://jtj.wuhan.gov.cn/jtzx/zwdt/202606/t20260622_2780144_slhxq.shtml",
    "description": "14个站点单循环闭合线路，全程约90分钟，串联黄鹤楼、红巷、昙华林、户部巷、武昌湾等八大核心景区。车身融入黄鹤归来、首义之门等城市特色元素，车内智能语音讲解全程在线。一张票24小时内不限次乘坐，可在沿线指定商户享受折扣优惠。",
    "fee": "收费",
    "source": "武昌古城观光巴士发车了",
    "family_friendly": True
})

activities.append({
    "title": "武昌区缤纷文明实践假期乐学课堂",
    "venue": "武昌区31个点位",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hb.people.com.cn/n2/2026/0704/c192237-41629497.html",
    "description": "全区31个点位同步铺开，准备了175场非遗焕新、双碳绿动、文化传承等实践课。把学习变成沉浸式的探索，让青少年在动手实践中学习传统文化、环保知识等多元内容，度过充实有趣的暑假。",
    "fee": "免费",
    "source": "武昌区暑期集中行动启动",
    "family_friendly": True
})

activities.append({
    "title": "武昌区151个纳凉点免费开放",
    "venue": "武昌区各社区纳凉点",
    "city": "wuhan",
    "start_date": "2026-07-15",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663032197883920922/",
    "description": "武昌区151个纳凉点全面开放，免费对外开放无准入限制。按照八有标准建设：有冷暖空调、有饮用水、有应急药品、有文化娱乐设施、有消毒设备、有消防设施、有专人管理、有安全应急措施。部分纳凉点开设亲子活动区，有彩纸、黏土、胶水等手工材料，孩子们可在志愿者带领下制作卡通扇子和小动物。",
    "fee": "免费",
    "source": "武昌151个纳凉点免费开放",
    "family_friendly": True
})

# 洪山区
activities.append({
    "title": "洪山区洪孩子暑期系列阅读活动",
    "venue": "洪山区图书馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.hongshan.gov.cn/zfbm/qwtj/fdzdgknr/gzdt/202607/t20260715_2821032.shtml",
    "description": "以筑梦新时代 阅读向未来为主题，创新打造游园打卡+沉浸式体验新模式。设有国风体验区（茶韵书香品茶、脸谱绘梦京剧脸谱绘制）、数字科普体验区（VR宇宙探索、深海秘境、恐龙纪元），还有诗词传递、数独挑战两大互动关卡，以及书籍漂流·时光邮局公益板块。",
    "fee": "免费",
    "source": "洪孩子暑期阅读活动精彩启幕",
    "family_friendly": True
})

# 硚口区
activities.append({
    "title": "硚口区硚夏童年悦享成长暑期嘉年华",
    "venue": "硚口区图书馆及各社区",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7657757154769764905/",
    "description": "硚口区图书馆倾力打造硚硚童书会五大特色课堂（绘本、非遗、科普、智慧父母、国学），同步推出少儿电影展映、社区名家讲坛、小小图书管理员实践体验以及少儿书画展与故事大王展演等系列赛事。二十余场主题活动交织成立体的夏日成长地图。",
    "fee": "免费",
    "source": "硚口区图书馆2026年暑期嘉年华",
    "family_friendly": True
})

activities.append({
    "title": "硚口区117个社区纳凉点免费开放",
    "venue": "硚口区各社区纳凉点",
    "city": "wuhan",
    "start_date": "2026-07-15",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663342349015089691/",
    "description": "硚口区117个社区纳凉点全部免费开放，严格按照八有标准建设。部分纳凉点设有亲子溜娃区，有爬行垫、积木、绘本等，孩子们可以尽情玩耍。还有阅读看报区、观影区、共享厨房、充电蓄能区、政务服务岗等多功能分区。",
    "fee": "免费",
    "source": "硚口117个纳凉点免费开放",
    "family_friendly": True
})

# 汉阳区
activities.append({
    "title": "武汉美术馆琴台馆暑期参观",
    "venue": "武汉美术馆琴台馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7659744832406946304/",
    "description": "武汉颜值天花板级别的公立艺术展馆，总建筑面积约4.3万平方米。银色梯田式外观自带高级氛围感，23米挑高的无柱展厅开阔大气，馆内黑色旋转楼梯是热门打卡点。常年轮换展出现当代绘画、装置艺术、新媒体艺术、主题艺术展，风格多元、审美在线。",
    "fee": "免费需预约",
    "source": "雨天不用宅家！20+宝藏室内场馆遛娃绝了",
    "family_friendly": True
})

activities.append({
    "title": "月湖天然水上乐园暑期开放",
    "venue": "汉阳区月湖天然水上乐园",
    "city": "wuhan",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7657030241726120467/",
    "description": "夏季公益免费浅水区，适合小朋友戏水，岸边平缓，配套卫生间。位于琴台大道月湖公园，地铁4号线琴台站直达。是市区带娃踩水、夏日消暑的好去处，环境优美，周边还有月湖风景区可以散步游览。",
    "fee": "免费",
    "source": "武汉40家泳池将免费开放",
    "family_friendly": True
})

# 青山区
activities.append({
    "title": "青山江滩建五路游泳池暑期免费开放",
    "venue": "青山区青山江滩建五路游泳池",
    "city": "wuhan",
    "start_date": "2026-07-12",
    "end_date": "2026-07-31",
    "link": "http://m.toutiao.com/group/7657030241726120467/",
    "description": "全市义务教育阶段中小学生可免费游泳，每天9:00-11:00、15:00-17:00开放。水域面积1250平方米，额定人数500人。免费入场游泳的中小学生须有一名家长陪同监护，家长按优惠票价2元购票入场。需通过畅游江城小程序预约。",
    "fee": "学生免费家长2元",
    "source": "武汉40家泳池将免费开放",
    "family_friendly": True
})

# 东西湖区
activities.append({
    "title": "东西湖区暑期集中行动",
    "venue": "东西湖区12个街道新时代文明实践阵地",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hbwh.wenming.cn/zt2026/2026sqjzxd/2026dtjj/202607/t20260710_9295270.html",
    "description": "全区统筹18个部门力量，推出思想道德教育、文化环境整治、校外实践拓展、未成年人关爱帮扶等多个板块活动。区文化馆免费开设唱歌、绘画、手工制作、曲艺、舞蹈、古琴六大门类市民夜校及青少年戏剧、古筝培训班共80次课。区图书馆举办50余场绘本阅读、科普实验及非遗体验活动。",
    "fee": "免费",
    "source": "东西湖区暑期集中行动开启",
    "family_friendly": True
})

activities.append({
    "title": "第十五届中国儿童戏剧节武汉分会场",
    "venue": "武汉临空港大剧院",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hbwh.wenming.cn/zt2026/2026sqjzxd/2026dtjj/202607/t20260710_9295270.html",
    "description": "武汉临空港大剧院承办第十五届中国儿童戏剧节武汉分会场，推出12部剧目18场演出。同时开办汉剧非遗美育营、星河童声合唱夏令营，为青少年提供丰富的艺术体验和学习机会，是暑期亲子观剧、艺术启蒙的绝佳选择。",
    "fee": "收费",
    "source": "东西湖区暑期集中行动开启",
    "family_friendly": True
})

activities.append({
    "title": "东西湖区网谷爱科普科学实验公开课",
    "venue": "东西湖区12个街道托管班",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hbwh.wenming.cn/zt2026/2026sqjzxd/2026dtjj/202607/t20260710_9295270.html",
    "description": "区科协联合力翰科技馆走进12个街道托管班，开展60节网谷爱科普科学实验公开课。依托李培武食品安全科普工作室开展科普宣传，统筹全区科普阵地开启暑期开放日。让青少年在动手实验中感受科学的魅力。",
    "fee": "免费",
    "source": "东西湖区暑期集中行动开启",
    "family_friendly": True
})

# 蔡甸区
activities.append({
    "title": "武汉野生动物王国暑期夜场",
    "venue": "武汉野生动物王国（蔡甸区）",
    "city": "wuhan",
    "start_date": "2026-07-10",
    "end_date": "2026-08-30",
    "link": "http://m.toutiao.com/group/7663372547362177572/",
    "description": "动物伴游大世界暑期夜场，实行白+黑全天候运营。日场门票升级为日夜通玩票不加价。长颈鹿、童话牧场等场馆夜场继续开放。入夜后星河灯海、潘多拉奇幻隧道、雾森北极光等光影场景点亮。科普老师带队夜探动物王国，还有猜谜闯关、篝火晚会、非遗打铁花等丰富活动。",
    "fee": "收费",
    "source": "武汉野生动物王国夜场来了",
    "family_friendly": True
})

activities.append({
    "title": "九真山景区暑期避暑游",
    "venue": "九真山风景区（蔡甸区）",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7660065279015141888/",
    "description": "武汉周边远近闻名的山林避暑地，极高的森林覆盖率筑起天然绿色屏障。幽谷地势低洼，林间清风不断，气温明显低于城区。景区有完善的登山步道，全程林荫覆盖，漫步林间既能吸氧洗肺又能躲避酷暑，是市民夏日近郊轻户外的理想选择。",
    "fee": "收费",
    "source": "蔡甸解锁暑期新玩法",
    "family_friendly": True
})

activities.append({
    "title": "后官湖国家湿地公园欢乐水世界",
    "venue": "后官湖国家湿地公园（蔡甸区）",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7660065279015141888/",
    "description": "全新打造的欢乐水世界一开放便成为热门打卡地。整个水世界分区合理，动静兼顾。水上飞人、摩托艇、皮划艇、动力冲浪板等项目动感十足。自然探索乐园的抓鱼摸虾是专门打造的儿童戏水区，温和安全，适合全家共同体验。景区更衣、休憩、餐饮等配套设施齐全。",
    "fee": "部分收费",
    "source": "蔡甸解锁暑期新玩法",
    "family_friendly": True
})

activities.append({
    "title": "花博汇知音花月夜沉浸式光影秀",
    "venue": "花博汇景区（蔡甸区）",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7660065279015141888/",
    "description": "迭代升级知音花月夜沉浸式光影体系，重磅上新史诗实景大戏《盛世楚歌》与十二花神实景巡游两大核心内容。万亩花海被万千彩灯层层装点，裸眼3D全息水幕、山体投影、非遗打铁花轮番上演。夜间配套潮流市集、傣族泼水狂欢、户外电音舞台，龙虾啤酒美食档口同步开放。",
    "fee": "收费",
    "source": "蔡甸解锁暑期新玩法",
    "family_friendly": True
})

# 江夏区
activities.append({
    "title": "江夏区博物馆新馆参观",
    "venue": "江夏区博物馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7659744832406946304/",
    "description": "新馆展厅扩大至2900平方米，展陈文物300余件。设三大主题展厅，核心主打湖泗窑古瓷文化与江夏本土千年历史脉络，完整展示从新石器时代、商周青铜到明清书画的地域文明变迁。搭配全息投影、智能触控互动设备，可体验文物数字拓印、京剧脸谱换装等趣味项目。",
    "fee": "免费",
    "source": "雨天不用宅家！20+宝藏室内场馆遛娃绝了",
    "family_friendly": True
})

activities.append({
    "title": "湖北经济学院润心助学爱心托管班",
    "venue": "江夏区栗庙社区",
    "city": "wuhan",
    "start_date": "2026-07-15",
    "end_date": "2026-07-29",
    "link": "http://m.toutiao.com/group/7663477292051563014/",
    "description": "湖北省爱心托管班七彩假期省级立项志愿服务项目，20余名大学生心理协会志愿者扎根社区。以课业辅导+安全教育+心理团辅+习惯养成为一站式阵地。围绕人际交往、情绪管理、注意力训练、学习习惯养成、自我认知觉察五大维度，设计20节标准化团辅课程。",
    "fee": "免费",
    "source": "湖北经济学院点亮社区暑期托管",
    "family_friendly": True
})

# 黄陂区
activities.append({
    "title": "木兰云雾山陂西峡漂流",
    "venue": "木兰云雾山景区陂西峡漂流（黄陂区）",
    "city": "wuhan",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7658228015800877620/",
    "description": "黄陂老牌森林峡谷漂流，5公里河道、160米总落差，80%河道藏在密林隧道里，全程几乎无日晒。急弯冲浪段尖叫拉满，平缓浅滩可组队打水仗，大人刺激、小孩浅滩戏水两不误。今夏还推出夜漂体验，晚间出门来场夜漂刚刚好。",
    "fee": "收费",
    "source": "黄陂玩水最全攻略",
    "family_friendly": True
})

activities.append({
    "title": "木兰天池峡谷玻璃漂流",
    "venue": "木兰天池景区（黄陂区）",
    "city": "wuhan",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7658228015800877620/",
    "description": "玻璃漂流滑道全长2000米，有超百米高低落差，九曲十八弯、360°回转造型，让人感受极速转向的刺激。中间还有一段七彩花道，好看又浪漫。漂流时全程在峡谷、森林之中飞速穿行，湖水风光像电影一样在眼前划过，还可以欣赏滑道两侧的自然风景。",
    "fee": "收费",
    "source": "黄陂玩水最全攻略",
    "family_friendly": True
})

activities.append({
    "title": "木兰草原侏罗纪主题玻璃漂流",
    "venue": "木兰草原景区（黄陂区）",
    "city": "wuhan",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7658228015800877620/",
    "description": "草原上的网红项目，被游客爱称为水上过山车。漂流滑道全长达到2160米，最高落差有百米之多。滑道沿途装扮成了侏罗纪公园，设置有恐龙主题的互动装置，加上周围茂密的树林，有一种身处侏罗纪恐龙世界的乐趣。附近还有新西兰滑车、悬崖秋千、滑草等游乐项目。",
    "fee": "收费",
    "source": "黄陂玩水最全攻略",
    "family_friendly": True
})

activities.append({
    "title": "清凉寨悬崖高空玻璃漂流",
    "venue": "木兰清凉寨景区（黄陂区）",
    "city": "wuhan",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7658228015800877620/",
    "description": "漂流全长3.6公里，落差136米——相当于从45层高楼直冲而下！玻璃+漂流混搭，刺激翻倍。全程穿行丛林，架高悬空，360°无边际视野，风景无死角。更有360度大回旋、45度急转弯连环来袭，抓紧筏子别松手，是追求刺激的游客首选。",
    "fee": "收费",
    "source": "黄陂玩水最全攻略",
    "family_friendly": True
})

activities.append({
    "title": "野村谷亲子浪浪漂&花溪谷漂流",
    "venue": "野村谷景区（黄陂区）",
    "city": "wuhan",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7658228015800877620/",
    "description": "野村谷今夏双漂上线！1.2公里浪浪漂，平缓安全，老少皆宜；3公里花溪谷漂，蜿蜒穿行花海，移步换景。全线安全员护航，头盔救生衣免费，让全家玩得开心、玩得放心。漂完还可以去田园水乐园、鱼鳞坝接着浪。",
    "fee": "收费",
    "source": "黄陂玩水最全攻略",
    "family_friendly": True
})

activities.append({
    "title": "木兰山风景区7折优惠活动",
    "venue": "木兰山风景区（黄陂区）",
    "city": "wuhan",
    "start_date": "2026-07-17",
    "end_date": "2026-07-19",
    "link": "http://m.toutiao.com/group/7662970520765235738/",
    "description": "7·17超级文旅日木兰山限时7折优惠。成人门票70元，活动期间享7折专属优惠。前100名参与活动的游客可免费领取精美祈福带一份。木兰山林木葱郁，是天然的森林氧吧，古迹荟萃，是木兰传说的源头，千年文化胜地。登临金顶极目远眺，探访古刹寻木兰之源。",
    "fee": "收费7折",
    "source": "木兰山限时7折优惠",
    "family_friendly": True
})

# 新洲区
activities.append({
    "title": "新洲区全民健身恒温游泳馆暑期免费开放",
    "venue": "新洲区全民健身恒温游泳馆",
    "city": "wuhan",
    "start_date": "2026-07-12",
    "end_date": "2026-07-31",
    "link": "http://m.toutiao.com/group/7657030241726120467/",
    "description": "全市义务教育阶段中小学生可免费游泳，每天9:00-11:00、15:00-17:00开放。需通过畅游江城小程序预约，免费入场游泳的中小学生须有一名家长陪同监护，家长按优惠票价2元购票入场。是新洲区暑期亲子消暑健身的好去处。",
    "fee": "学生免费家长2元",
    "source": "武汉40家泳池将免费开放",
    "family_friendly": True
})

# 武汉经开区
activities.append({
    "title": "中国车谷全民健身中心南馆游泳馆暑期免费开放",
    "venue": "武汉经开区中国车谷全民健身中心南馆游泳馆",
    "city": "wuhan",
    "start_date": "2026-07-12",
    "end_date": "2026-07-31",
    "link": "http://m.toutiao.com/group/7657030241726120467/",
    "description": "全市义务教育阶段中小学生可免费游泳，每天9:00-11:00、15:00-17:00开放。需通过畅游江城小程序预约，免费入场游泳的中小学生须有一名家长陪同监护，家长按优惠票价2元购票入场。设施完善，环境舒适。",
    "fee": "学生免费家长2元",
    "source": "武汉40家泳池将免费开放",
    "family_friendly": True
})

# 东湖高新区
activities.append({
    "title": "2026中国光谷社区艺术季",
    "venue": "东湖高新区各社区及文化场馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-11-30",
    "link": "http://m.toutiao.com/group/7662204870187614746/",
    "description": "全年开展170余场活动，7-11月集中开展9+N场主题活动，包括儿童自然美育、青年潮流展演、中秋国风游园、国粹戏曲传承、精品话剧、主题音乐会等，每场同步配套创意市集、主题美陈、网红打卡互动体验。还有光谷艺起来达人秀，8场海选、2场复赛及总决赛。",
    "fee": "免费",
    "source": "2026光谷社区艺术季",
    "family_friendly": True
})

activities.append({
    "title": "光谷美术馆开馆四大首展",
    "venue": "光谷美术馆",
    "city": "wuhan",
    "start_date": "2026-07-18",
    "end_date": "2026-10-18",
    "link": "http://m.toutiao.com/group/7663369762512077352/",
    "description": "光谷美术馆重磅开馆，推出四大首展：中国国家画院光谷展厅首展、《宗师列传·唐宋八大家》主题全国美术作品邀请展、《微·观》显微成像学术实践大赛艺术展、《失真的世界》人工智能艺术展。是亲子艺术启蒙、审美培养的好去处。",
    "fee": "免费需预约",
    "source": "光谷美术馆开馆四大首展",
    "family_friendly": True
})

activities.append({
    "title": "光谷图书馆暑期阅读活动",
    "venue": "光谷图书馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662204870187614746/",
    "description": "暑期推出丰富多彩的阅读活动，包括拼贴诗互动墙、亲子共读回忆8090我们读过的童书、童趣绘画展、经典诗歌朗诵会、非遗漆扇制作、小小图书管理员体验等。8月还有双语小课堂绘本共读、亲子关系绘本共读、盛夏主题绘本共读等活动。",
    "fee": "免费",
    "source": "2026光谷社区艺术季",
    "family_friendly": True
})

activities.append({
    "title": "光谷城市书房暑期公益电影放映",
    "venue": "光谷13家城市书房",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662204870187614746/",
    "description": "全区13家城市书房开启光影遇上书香暑期公益电影放映活动，精选适合青少年观看的优秀影片，为孩子们提供暑期文化休闲好去处，让书香与光影相伴成长。是夏日亲子消暑、文化休闲的好选择。",
    "fee": "免费",
    "source": "2026光谷社区艺术季",
    "family_friendly": True
})

activities.append({
    "title": "光谷暑期免费游泳开放",
    "venue": "光谷3家泳池",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662204870187614746/",
    "description": "3家泳池面向市民免费开放，为广大青少年和市民提供暑期消暑健身的好去处。具体开放时间和预约方式可通过光谷文旅微信小程序查询。是光谷片区亲子家庭夏日健身消暑的优质选择。",
    "fee": "免费",
    "source": "2026光谷社区艺术季",
    "family_friendly": True
})

activities.append({
    "title": "互动零距离·操偶师带你走进神奇的木偶世界",
    "venue": "光谷书房·创意基地分馆",
    "city": "wuhan",
    "start_date": "2026-07-16",
    "end_date": "2026-07-16",
    "link": "http://m.toutiao.com/group/7662204870187614746/",
    "description": "带领大家认识各类木偶及其特色，揭秘木偶变脸背后的原理，欣赏精彩的长绸木偶技艺展示，细致讲解杖头木偶的内部机关与操控技巧，最后设置互动体验环节让大家现场上手学习、亲身操作木偶。",
    "fee": "免费",
    "source": "2026光谷社区艺术季",
    "family_friendly": True
})

# ==================== 2. 公益托管班 ====================

activities.append({
    "title": "武汉市青少年暑假爱心托管班（全市468个点位）",
    "venue": "全市16区468个托管点位",
    "city": "wuhan",
    "start_date": "2026-07-13",
    "end_date": "2026-08-21",
    "link": "http://hbwh.wenming.cn/rdjj/202607/t20260701_9285974.html",
    "description": "468个托管点位覆盖全市，免费提供暖心看护与多元课程。设置品德修养、科学素养、体育锻炼、艺术熏陶、劳动教育、安全自护6大类课程。面向小学阶段少年儿童，优先服务留守儿童、经济困难家庭子女、双职工家庭子女。每托管班配备不少于1名负责人、1名班主任、2名志愿者、1名安保员。",
    "fee": "免费",
    "source": "武汉青少年暑假爱心托管班启动",
    "family_friendly": True
})

activities.append({
    "title": "武昌区50个爱心托管班",
    "venue": "武昌区各社区",
    "city": "wuhan",
    "start_date": "2026-07-14",
    "end_date": "2026-08-21",
    "link": "http://m.toutiao.com/group/7662671908235657780/",
    "description": "武昌区共开设50个爱心托管班——7月第一批33个，8月第二批17个，免费提供暖心看护与多元趣味课程。开班第一天还组织孩子们走进武汉规划展示馆，开展逐梦十五五·童眼看武汉主题实践活动，用童真的眼睛读懂家乡的成长日记。",
    "fee": "免费",
    "source": "武昌区爱心托管班开班",
    "family_friendly": True
})

activities.append({
    "title": "洪山区暑假爱心托管班",
    "venue": "洪山区各社区（南湖、丽岛花园、保利蓝海郡等）",
    "city": "wuhan",
    "start_date": "2026-07-14",
    "end_date": "2026-08-21",
    "link": "https://m.wh.bendibao.com/edu/198213.shtm",
    "description": "洪山区暑假爱心托管班覆盖多个社区和小区。第一批次7月14日至31日，第二批次8月3日至21日，托管时段每天8:00-18:00。面向6至14岁少年儿童，不限户籍，洪山区及周边家庭均可报名。通过青春武汉公众号线上报名，全程免费。",
    "fee": "免费",
    "source": "洪山区暑假免费托管班",
    "family_friendly": True
})

activities.append({
    "title": "东西湖区72个公益托管班",
    "venue": "东西湖区各街道（实现街道全覆盖）",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hbwh.wenming.cn/zt2026/2026sqjzxd/2026dtjj/202607/t20260710_9295270.html",
    "description": "东西湖区团区委开设72个公益托管班，实现街道全覆盖。同步开放12355心理服务站，开展心理团辅100场次。深化童伴妈妈品牌，结对帮扶困境青少年。开展红领巾讲解员展示活动，为青少年提供丰富多彩的暑期生活。",
    "fee": "免费",
    "source": "东西湖区暑期集中行动开启",
    "family_friendly": True
})

# ==================== 3. 博物馆活动 ====================

activities.append({
    "title": "武汉博物馆江城消夏季夜游",
    "venue": "武汉博物馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-09-30",
    "link": "http://wlt.hubei.gov.cn/bmdt/mtjj/202607/t20260713_5975230.shtml",
    "description": "7至9月每周五晚间延时开放，推出浮生一日凉 江城消夏季夏夜文化盛宴。集国风展演、非遗市集、戏曲雅集、文化讲座、专场导览及沉浸式互动于一体，营造浸润式古风消暑意境。晚风配古韵，沉浸式复刻古人悠然消夏的惬意。",
    "fee": "免费",
    "source": "湖北文博暑期特色活动上线",
    "family_friendly": True
})

activities.append({
    "title": "浮生一日凉——古代消夏文化展",
    "venue": "武汉博物馆一楼珍藏厅",
    "city": "wuhan",
    "start_date": "2026-07-08",
    "end_date": "2026-10-31",
    "link": "http://wlt.hubei.gov.cn/bmdt/mtjj/202607/t20260713_5975230.shtml",
    "description": "武汉博物馆集结近200件跨馆文物，从馆藏器物中解锁古人纳凉智慧，沉浸式感受千年前的夏日闲情。仇英、八大山人、齐白石等名家真迹亮相，全方位展现古代先民的消夏生活与匠心意趣，一秒get古代版夏日避暑指南。",
    "fee": "免费",
    "source": "湖北文博暑期特色活动上线",
    "family_friendly": True
})

activities.append({
    "title": "克里姆林宫的瑰宝：从彼得一世到叶卡捷琳娜二斯特展",
    "venue": "湖北省博物馆北馆二楼",
    "city": "wuhan",
    "start_date": "2026-07-20",
    "end_date": "2026-10-25",
    "link": "http://www.hbwmw.gov.cn/c/2026/07/83871.shtml",
    "description": "共展出莫斯科克里姆林宫博物馆藏16世纪至19世纪的珍贵文物共129件（组），涵盖珠宝首饰、武器、服饰等品类，包括十七至十八世纪俄国沙皇的独特收藏。观众足不出境即可领略帝国宫廷风华，是亲子了解世界历史文化的绝佳机会。",
    "fee": "收费",
    "source": "湖北文博暑期特色活动清凉上线",
    "family_friendly": True
})

activities.append({
    "title": "湖北省博物馆小小考古学家亲子活动",
    "venue": "湖北省博物馆东馆二楼儿童馆",
    "city": "wuhan",
    "start_date": "2026-07-03",
    "end_date": "2026-08-30",
    "link": "https://m.wh.bendibao.com/tour/198440.shtm",
    "description": "湖北省博物馆儿童馆以考古发掘和研究为特色，为3-14岁孩子提供兼具科学性、知识性、趣味性的体验空间。活动包含参观展厅学习文物知识、学习考古与地层知识、手工DIY参与文物相关互动制作。每场限10组家庭参加，上午120元/儿童家庭，下午160元/儿童家庭。",
    "fee": "收费",
    "source": "湖北省博物馆暑假亲子活动推荐",
    "family_friendly": True
})

activities.append({
    "title": "湖北省博物馆跟着文物识汉字",
    "venue": "湖北省博物馆南馆二楼互动体验区",
    "city": "wuhan",
    "start_date": "2026-07-03",
    "end_date": "2026-08-30",
    "link": "https://m.wh.bendibao.com/tour/198440.shtm",
    "description": "活动以馆藏文物为载体，开展文物识汉字趣味学习，每件文物配套展示对应汉字、标准拼音与文物实景介绍。暑期每周二至周日10:30、14:30开展，无需报名即可参与。让孩子们在参观文物的同时学习汉字知识，寓教于乐。",
    "fee": "免费",
    "source": "湖北省博物馆暑假亲子活动推荐",
    "family_friendly": True
})

activities.append({
    "title": "湖北省博物馆小小讲解员夏令营",
    "venue": "湖北省博物馆各展厅",
    "city": "wuhan",
    "start_date": "2026-07-21",
    "end_date": "2026-08-28",
    "link": "https://m.wh.bendibao.com/tour/198440.shtm",
    "description": "荆楚故事我来讲红领巾讲解员夏令营是湖北省博物馆品牌教育项目，青少年在专业讲解老师指导下学习文物知识、讲解技巧和参观礼仪。经训练考核后，小小讲解员将在指定展厅为游客提供讲解服务。上岗实践时间为每日9:30-11:30、14:00-16:00。",
    "fee": "免费需预约",
    "source": "湖北省博物馆暑假亲子活动推荐",
    "family_friendly": True
})

activities.append({
    "title": "文物修复展示中心开放日",
    "venue": "湖北省博物馆文物修复展示中心",
    "city": "wuhan",
    "start_date": "2026-07-07",
    "end_date": "2026-08-27",
    "link": "http://m.toutiao.com/group/7658218372072620579/",
    "description": "位于北馆三楼与南馆四楼连廊处的文物修复展示中心，暑期7月7日、7月17日、8月7日、8月27日9:30-11:30开放。可零距离围观修复师的工作日常，了解文物修复技艺，亲眼见证文物如何重焕光彩，是非常难得的科普教育机会。",
    "fee": "免费需预约",
    "source": "延时!免费开放!武汉这些人放假",
    "family_friendly": True
})

activities.append({
    "title": "盘龙城遗址博物院暑期参观",
    "venue": "盘龙城遗址博物院（黄陂区）",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7659744832406946304/",
    "description": "见证武汉城市文明起源的核心展馆，被誉为武汉城市之根，主打商代早期古城文化与史前文明展示。馆内完整展出大量商代出土文物、古城聚落模型和遗址复原场景，生动还原三千多年前武汉地区的城市风貌与生活场景，科普趣味性极强。",
    "fee": "免费需预约",
    "source": "雨天不用宅家！20+宝藏室内场馆遛娃绝了",
    "family_friendly": True
})

# ==================== 4. 武汉科技馆活动 ====================

activities.append({
    "title": "武汉科技馆暑期科学季",
    "venue": "武汉科技馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1047050364_121106908/",
    "description": "暑遇科学·智探万物2026暑期科学季，整座场馆化身超好玩的科学游乐园。有KeKe老师故事会、科普小课堂、STEAM科学+、趣味实验小推车、科学实验秀、赛因斯科学探究课等品牌活动。还有小小讲解员、遇见科学大师见面会、心理疗愈集市、一夏爱上科学闯关等全新重磅活动。",
    "fee": "免费需预约",
    "source": "武汉科技馆暑期科学季重磅来袭",
    "family_friendly": True
})

activities.append({
    "title": "武汉科技馆小小讲解员活动",
    "venue": "武汉科技馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1047050364_121106908/",
    "description": "弘扬科学家精神，讲好钱学森故事——小小讲解员活动火热来袭。想成为传播科学精神的小使者吗？站上属于你的舞台，把伟大的科学家故事讲给更多人听！培养孩子的表达能力和科学素养，是暑期非常有意义的实践活动。",
    "fee": "免费需报名",
    "source": "武汉科技馆暑期科学季重磅来袭",
    "family_friendly": True
})

activities.append({
    "title": "武汉科技馆非遗手工坊科普+非遗体验",
    "venue": "武汉科技馆一楼非遗手工坊",
    "city": "wuhan",
    "start_date": "2026-07-08",
    "end_date": "2026-08-28",
    "link": "https://m.sohu.com/a/1047050364_121106908/",
    "description": "当科普遇见非遗，碰撞出怎样的火花？这个暑假，非遗手工坊打造科普+非遗公益免费体验活动，让广大亲子家庭近距离接触剪纸、纸编、面塑三大传统手工技艺。每周三、周五上午10:00，每场限15人，在动手动脑中感受传统手工艺的魅力。",
    "fee": "免费",
    "source": "武汉科技馆暑期科学季重磅来袭",
    "family_friendly": True
})

activities.append({
    "title": "派拉熊梦幻剧场《地心历险记》",
    "venue": "武汉科技馆派拉熊梦幻剧场",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1047050364_121106908/",
    "description": "派拉熊梦幻剧场暑期新增剧目《地心历险记》。恐龙爱好者绝对不能错过！跟随肖恩和特种兵吴迪深入冰岛火山洞穴，闯入神秘的地下世界。全息技术打造的精美地心世界，栩栩如生的恐龙，加上深入浅出的地球物理和生命科学知识，是一场眼界的飞跃。",
    "fee": "收费",
    "source": "武汉科技馆暑期科学季重磅来袭",
    "family_friendly": True
})

activities.append({
    "title": "武汉科技馆心理疗愈集市",
    "venue": "武汉科技馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.whstm.org.cn/shownews/detail/1979",
    "description": "心理集市暑期上新，特别打造了房树人绘画体验区：只需在纸上画一座房子、种一棵树、有故事的人，就能在一笔一画之间解锁内心世界。还有情绪树洞、心灵OH卡、人偶心游、心理格盘等多种体验活动，帮助孩子和家长了解心理状态、调节情绪。",
    "fee": "免费",
    "source": "心理集市暑期上新",
    "family_friendly": True
})

# ==================== 5. 武汉青少年宫活动 ====================

activities.append({
    "title": "武汉市青少年宫国学馆暑期素质训练营",
    "venue": "武汉市青少年宫",
    "city": "wuhan",
    "start_date": "2026-07-06",
    "end_date": "2026-08-07",
    "link": "https://m.sohu.com/a/1034317394_121106908/",
    "description": "课程依托传统国学内容，循序渐进帮助孩子夯实识字基础，提升自主阅读能力，培养良好的阅读习惯。同时将礼仪教养融入日常学习之中，引导孩子潜移默化懂礼貌、知礼仪、修品行。上课时间为周一到周五8:30-16:30。",
    "fee": "收费",
    "source": "武汉市青少年宫国学馆暑期素质训练营",
    "family_friendly": True
})

activities.append({
    "title": "武汉市青少年宫拾光绘夏美术启蒙班",
    "venue": "武汉市青少年宫",
    "city": "wuhan",
    "start_date": "2026-07-08",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1032934018_121106908/",
    "description": "4-8岁夏季美术启蒙课程，以色彩为引，陪孩子去触摸世界的轮廓。不教刻板的线条，只唤醒感知的触角。有周中沉浸班（每周三、四、五）和周末悠然班（每周六、日）两种班型可选，微班席位，静候小小艺术家。",
    "fee": "收费",
    "source": "武汉市青少年宫夏季美术启蒙",
    "family_friendly": True
})

activities.append({
    "title": "武汉市青少年宫系统美术专业课",
    "venue": "武汉市青少年宫",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1032934018_121106908/",
    "description": "9-18岁系统美术专业课，包括素描班（9岁+，从几何体起步，深耕线条、透视、明暗知识点）、色彩班（10岁+，水粉、彩铅、马克笔多媒介教学）、户外写生班（12岁+，走出画室实景采风）。系统化分层教学，兼顾兴趣与刚需。",
    "fee": "收费",
    "source": "武汉市青少年宫夏季美术启蒙",
    "family_friendly": True
})

activities.append({
    "title": "武汉市青少年宫暑期舞蹈剧目集训班",
    "venue": "武汉市青少年宫",
    "city": "wuhan",
    "start_date": "2026-07-10",
    "end_date": "2026-07-18",
    "link": "https://m.sohu.com/a/1047411246_121106908/",
    "description": "为提升孩子独舞演绎能力，全面夯实舞蹈专业水平，助力学员备战各类舞蹈赛事。共8次课，包括小组集体课和一对一小课，由优秀的青年教师进行教学。招生对象为6-12岁少年儿童，定制能参赛的优秀独舞剧目。",
    "fee": "收费",
    "source": "武汉市青少年宫暑期舞蹈剧目集训班",
    "family_friendly": True
})

activities.append({
    "title": "武汉市青少年宫双语国际暑期课程",
    "venue": "武汉市青少年宫",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1039822405_121106908/",
    "description": "秉持Open minds, explore worlds的理念，以语言为舟、兴趣为帆，带领孩子们在沉浸式英语体验中发现乐趣、拓展视野、自信表达。有洪恩英语动物环球派对、自然拼读寻宝营等特色活动，还有多种课程可选。",
    "fee": "收费",
    "source": "武汉市青少年宫双语国际火热报名中",
    "family_friendly": True
})

activities.append({
    "title": "武汉市青少年宫夏秋季兴趣课程",
    "venue": "武汉市青少年宫",
    "city": "wuhan",
    "start_date": "2026-06-05",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1032526642_121106908/",
    "description": "涵盖美术活动类、文艺活动类（舞蹈、器乐、声乐、表演等四大类20多种培训课程）、体育活动类（武术、棋类、球类、艺术体操、体育舞蹈、轮滑、格斗等）、文化活动类（双语国际、国学馆、365科学实验室、小小科学家等）四大类课程，为3-18岁学员量身定制。",
    "fee": "收费",
    "source": "武汉市青少年宫2026年夏秋季兴趣课程招生",
    "family_friendly": True
})

# ==================== 6. 景区/古镇暑期活动 ====================

activities.append({
    "title": "黄鹤楼中高考考生免票活动",
    "venue": "黄鹤楼公园",
    "city": "wuhan",
    "start_date": "2026-06-17",
    "end_date": "2026-06-30",
    "link": "http://m.toutiao.com/group/7649237708950274595/",
    "description": "2026年全国应届中、高考生，凭本人准考证及身份证，到人工售票窗口兑换免票凭证，即可免费入园。6月17日超级文旅日当天，参与活动的学子凭本人准考证及身份证，还可前往黄鹤楼主题咖啡馆免费领取一杯夏日特饮。登天下江山第一楼，亲身领略古诗词里的意境。",
    "fee": "考生免费",
    "source": "武汉40+景区官宣免票优惠",
    "family_friendly": True
})

activities.append({
    "title": "东湖听涛泳场暑期免费开放",
    "venue": "东湖听涛景区泳场",
    "city": "wuhan",
    "start_date": "2026-06-26",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7656667904083083818/",
    "description": "市区正规免费天然泳场，每日16:00-20:00开放，完全免费无需预约。官方划定湖泳区，救生员全程在岗，有淋浴、存包，湖水平缓。是武汉市区首选正规免费游泳点，也是亲子夏日消暑戏水的绝佳选择。",
    "fee": "免费",
    "source": "武汉可以免费玩水的地方",
    "family_friendly": True
})

activities.append({
    "title": "东湖帆船夏令营",
    "venue": "东湖帆船公园",
    "city": "wuhan",
    "start_date": "2026-06-22",
    "end_date": "2026-08-28",
    "link": "http://m.toutiao.com/group/7647733561180668454/",
    "description": "5天4夜零基础起步，中帆协认证培训中心，水域开阔风浪平稳。课程结束后获中帆协国家一级小水手证书。16小时水上训练穿插造船工程、CPR急救认证、游艇跳岛、电动水翼冲浪板。三位中帆协高级教练带队，安全有保障。",
    "fee": "收费",
    "source": "东湖隐藏玩法请查收",
    "family_friendly": True
})

activities.append({
    "title": "东湖童趣有氧骑趣东湖骑行研学营",
    "venue": "东湖绿道楚风园湖光序曲广场",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7647733561180668454/",
    "description": "专业骑行教练当导师，1:5高配比，领骑、护骑、收尾全程保障。用车为捷安特品牌，头盔马甲全配齐。学习单车理论、趣味battle赛（绕桩、慢骑、接力），在骑行中领略东湖湖光山色，锻炼身体的同时欣赏美景。",
    "fee": "收费",
    "source": "东湖隐藏玩法请查收",
    "family_friendly": True
})

activities.append({
    "title": "东湖之眼中高考考生免票活动",
    "venue": "东湖之眼摩天轮",
    "city": "wuhan",
    "start_date": "2026-06-12",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7649237708950274595/",
    "description": "2026年应届中、高考生，凭本人证件（准考证及身份证），可免票乘坐东湖之眼摩天轮一次。屹立在东湖之畔的粉色摩天轮，落日熔金，美得耀眼，是暑期亲子游玩、拍照打卡的热门选择。",
    "fee": "考生免费",
    "source": "武汉40+景区官宣免票优惠",
    "family_friendly": True
})

activities.append({
    "title": "木兰草原中高考考生免票+优惠套票",
    "venue": "木兰草原景区（黄陂区）",
    "city": "wuhan",
    "start_date": "2026-06-13",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7649237708950274595/",
    "description": "2026年应届中、高考考生，凭本人准考证原件，可享免景区大门票入园，以及118元购买总价值673元的娱乐套票。单人通玩娱乐套票包含云中战歌+山海烬长歌+小火车+13个通玩项目。武汉版呼伦贝尔，骑马驰骋，特畅快。",
    "fee": "考生免票",
    "source": "武汉40+景区官宣免票优惠",
    "family_friendly": True
})

activities.append({
    "title": "木兰花乡（木兰不夜城）考生免票",
    "venue": "木兰花乡景区（黄陂区）",
    "city": "wuhan",
    "start_date": "2026-06-07",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7649237708950274595/",
    "description": "2026年应届中、高考生，凭本人准考证，免票入园。换上古装，夜游木兰不夜城，亲历《木兰辞》里的名场面。木兰花乡荧光旋转玻璃漂流也很有特色，是暑期亲子出游、体验古风的好地方。",
    "fee": "考生免费",
    "source": "武汉40+景区官宣免票优惠",
    "family_friendly": True
})

activities.append({
    "title": "姚家山景区考生免票",
    "venue": "姚家山景区（黄陂区）",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-09-01",
    "link": "http://m.toutiao.com/group/7649237708950274595/",
    "description": "2026年应届中、高考生，凭本人准考证，免景区大门票。1.7公里溪谷在山下蜿蜒，溯溪露营好去处。是夏季避暑、亲近自然、开展红色教育的好地方，适合亲子家庭周末出游。",
    "fee": "考生免费",
    "source": "武汉40+景区官宣免票优惠",
    "family_friendly": True
})

activities.append({
    "title": "紫薇都市田园考生免票",
    "venue": "紫薇都市田园景区（新洲区）",
    "city": "wuhan",
    "start_date": "2026-06-10",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7649237708950274595/",
    "description": "2026年应届中、高考生，凭本人准考证，免票入园。钓虾、摸鱼、吃瓜……6月的每个周末，玩法不重样。景区内有大片紫薇花田，夏季盛开时非常美丽，还有多种游乐项目，适合亲子家庭游玩。",
    "fee": "考生免费",
    "source": "武汉40+景区官宣免票优惠",
    "family_friendly": True
})

activities.append({
    "title": "凤娃古寨景区考生免票",
    "venue": "凤娃古寨景区（新洲区）",
    "city": "wuhan",
    "start_date": "2026-06-09",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7649237708950274595/",
    "description": "2026年应届中、高考生，凭本人准考证原件，免景区大门票。凭本人准考证可在景区游客中心领取景区自营游乐票一张。有20余座明清古建筑，可以看到皮影戏、采蓬船等传统民俗表演。",
    "fee": "考生免费",
    "source": "武汉40+景区官宣免票优惠",
    "family_friendly": True
})

# ==================== 7. 书店/商业综合体活动 ====================

activities.append({
    "title": "武汉青少年暑期阅读季六大板块活动",
    "venue": "全市新华书店及少年儿童图书馆",
    "city": "wuhan",
    "start_date": "2026-07-15",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663313279355290166/",
    "description": "书香武汉 阅见未来2026年武汉青少年暑期阅读季，推出启动专场+少图快借+惠民展陈+非遗研学+美育未来+亲子读书六大板块。发布推荐书单涵盖长征故事、科学家精神、经典文学、科普百科等多个类别。全市18家新华书店门店同步设立主题展陈专区。",
    "fee": "免费",
    "source": "2026武汉青少年暑期阅读季启幕",
    "family_friendly": True
})

activities.append({
    "title": "新华书店暑期研学实践营",
    "venue": "全市新华书店门店",
    "city": "wuhan",
    "start_date": "2026-07-15",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663313279355290166/",
    "description": "知行合一 美育未来暑期研学实践营，有全天托管型、主题工作坊型、AI特色型、非遗传承型四种模式，覆盖全市新华书店。让青少年在翻书、闯关、行走、手作中读懂长江、读懂家乡，在实践中增长见识。",
    "fee": "收费",
    "source": "2026武汉青少年暑期阅读季启幕",
    "family_friendly": True
})

activities.append({
    "title": "翻书闯长征红色阅读知识擂台",
    "venue": "江汉路新华书店及全市各新华书店",
    "city": "wuhan",
    "start_date": "2026-07-15",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663313279355290166/",
    "description": "将读书找答案、翻书闯关卡、抢答赢徽章融为一体。在长征胜利90周年即将来临之际，带领孩子们翻开《长征的故事》《红军不怕远征难》等书目，重温湘江战役、遵义会议、四渡赤水等历史事件，还有手挽手感受红军过草地沉浸式体验环节。",
    "fee": "免费",
    "source": "2026武汉青少年暑期阅读季启幕",
    "family_friendly": True
})

activities.append({
    "title": "北师大分级阅读测评服务",
    "venue": "全市新华书店门店",
    "city": "wuhan",
    "start_date": "2026-07-15",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662804019517178409/",
    "description": "阅读季特别引入北京师范大学分级阅读课题组，面向全市6至12岁青少年推出分级阅读测评服务。青少年可在全市新华书店免费进行测评，并匹配推荐适读书目，帮助家长和孩子找到最适合的阅读材料。",
    "fee": "免费",
    "source": "2026年武汉青少年暑期阅读季启动",
    "family_friendly": True
})

activities.append({
    "title": "典耀中华第七届人教杯诵读活动",
    "venue": "全市各片区新华书店",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662804019517178409/",
    "description": "典耀中华第七届人教杯诵读活动在各片区新华书店展开。活动旨在引导青少年诵读经典、传承文化，通过诵读经典篇目，感受中华优秀传统文化的魅力，提升语言表达能力和文化素养。",
    "fee": "免费",
    "source": "2026年武汉青少年暑期阅读季启动",
    "family_friendly": True
})

activities.append({
    "title": "西西弗书店刘同新书分享会",
    "venue": "西西弗书店·武汉万象城店（江岸区）",
    "city": "wuhan",
    "start_date": "2026-05-31",
    "end_date": "2026-05-31",
    "link": "https://17bigstudy.huodongxing.com/event/3859885012712?qd=8828363103856",
    "description": "作家刘同《早上好，岛上好》新书分享会武汉站。刘同2026全新作品，继百万畅销小说《我在未来等你》后时隔9年，潜心淬炼的长篇回归。活动包括嘉宾分享、读者互动、排队签名等环节。",
    "fee": "免费（需购书）",
    "source": "刘同新书分享会武汉站",
    "family_friendly": True
})

# ==================== 8. 高校研学/科普活动 ====================

activities.append({
    "title": "华中师范大学校园开放日",
    "venue": "华中师范大学桂子山校区",
    "city": "wuhan",
    "start_date": "2026-06-14",
    "end_date": "2026-06-14",
    "link": "https://m.wh.bendibao.com/edu/197005.shtm",
    "description": "五大活动板块：现场高招咨询（23个学院+64个本科专业+4个职能部门驻场答疑）、高招宣讲（招生政策宣讲、志愿填报技巧讲座、机器人舞蹈互动等）、学院参访（各学院开放区域参观，特色体验）、文化体验（校史馆、博物馆、生物博物馆开放，毕业晚会）、打卡互动。",
    "fee": "免费",
    "source": "华中师范大学校园开放日",
    "family_friendly": True
})

activities.append({
    "title": "武汉大学地球与空间科学学院校园开放日",
    "venue": "武汉大学",
    "city": "wuhan",
    "start_date": "2026-07-20",
    "end_date": "2026-07-21",
    "link": "http://pc.baoyanwang.com.cn/articles/7527",
    "description": "优秀大学生校园开放日活动，设置学院介绍、师生面对面、实验室参观等环节。参观珞珈山野外观测台站等多个高水平科研基地，更有特色体验环节。了解空间物理、行星遥感、卫星导航、固体地球物理、天体物理等多个热门方向的前沿动态。",
    "fee": "免费（需报名）",
    "source": "武汉大学地球与空间科学学院校园开放日",
    "family_friendly": True
})

activities.append({
    "title": "中国地质大学（武汉）地质探秘研学营",
    "venue": "中国地质大学（武汉）",
    "city": "wuhan",
    "start_date": "2026-07-20",
    "end_date": "2026-08-05",
    "link": "https://yjxy.cug.edu.cn/info/1024/8554.htm",
    "description": "4天3晚封闭式研学，面向12-16岁中学生。采用实验室实操、野外科考、博物馆深度研学、名校人文探访、楚文化实景课堂模式。含逸夫博物馆、南望山科考、湖北省博物馆、黄鹤楼、武汉大学、东湖地质观察等点位。",
    "fee": "收费",
    "source": "中国地质大学青少年暑期研学营通知",
    "family_friendly": True
})

activities.append({
    "title": "武汉理工大学资源与环境工程学院夏令营",
    "venue": "武汉理工大学",
    "city": "wuhan",
    "start_date": "2026-07-08",
    "end_date": "2026-07-09",
    "link": "http://sree.whut.edu.cn/yjsjy/zsxx/202606/t20260626_1404511.shtml",
    "description": "全国优秀大学生暑期夏令营，活动包括学院领导致辞、学院情况介绍、优秀学子报告、营员自我介绍、分组座谈、参观团队工作室和实验室、参观院史馆、沟通交流等环节。面向2027届应届本科毕业生，对矿业工程、环境科学与工程、地理学等专业感兴趣的学生。",
    "fee": "免费",
    "source": "武汉理工大学资源与环境工程学院夏令营",
    "family_friendly": True
})

activities.append({
    "title": "中国地质大学（武汉）新能源学院校园开放日",
    "venue": "中国地质大学（武汉）未来城校区",
    "city": "wuhan",
    "start_date": "2026-07-03",
    "end_date": "2026-07-03",
    "link": "https://energy.cug.edu.cn/info/1014/6189.htm",
    "description": "第十二届研招校园开放日活动，包括招生政策及学科特色宣讲、交流互动、参观深层地热富集机理与高效开发全国重点实验室等。采用线上线下相结合的方式，外校学生线上参与，本校学生线下参与。",
    "fee": "免费",
    "source": "中国地质大学新能源学院校园开放日",
    "family_friendly": True
})

activities.append({
    "title": "小黄鹤儿童观察团研学活动",
    "venue": "东西湖区（海关、网安基地、智创小镇等）",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hbwh.wenming.cn/zt2026/2026sqjzxd/2026dtjj/202607/t20260710_9295270.html",
    "description": "东西湖区妇联开展的小黄鹤儿童观察团活动5场以上，带领儿童走进海关、网安基地、智创小镇研学议事。让孩子们近距离了解科技前沿、海关工作、网络安全等知识，培养观察能力和社会责任感。",
    "fee": "免费",
    "source": "东西湖区暑期集中行动开启",
    "family_friendly": True
})

# ==================== 9. 其他特色活动 ====================

activities.append({
    "title": "第41届马良杯少年儿童书画展示活动",
    "venue": "全市各区图书馆",
    "city": "wuhan",
    "start_date": "2026-05-29",
    "end_date": "2026-10-31",
    "link": "http://m.toutiao.com/group/7657549578228531753/",
    "description": "武汉市知识工程少儿读书系列活动重要一环，分为绘画和书法两大项，面向5至15周岁少年儿童，分为5-7岁、8-10岁、11-12岁、13-15岁四个组别。9月进行终选，10月优秀作品展示。是展示少年儿童艺术才华的平台。",
    "fee": "免费",
    "source": "第41届马良杯少年儿童书画展示活动报名开启",
    "family_friendly": True
})

activities.append({
    "title": "第49届武汉之夏系列群众文化活动",
    "venue": "汉口江滩大舞台及全市各文化场馆",
    "city": "wuhan",
    "start_date": "2026-06-26",
    "end_date": "2026-09-30",
    "link": "http://m.app.dawuhanapp.com/p/46931307.html",
    "description": "以夏至武汉 暑你精彩为主题，联动全市文化馆（站）、文化驿站，推出近300场群众文化活动，涵盖广场舞、文艺展演、戏曲、音乐会、书画展等八大板块。包括魅力广场舞展演、文艺团队秀、戏曲达人秀、街头音乐会、书画摄影展、江城文驿汇、露天电影院等。",
    "fee": "免费",
    "source": "第49届武汉之夏启幕",
    "family_friendly": True
})

activities.append({
    "title": "江城文驿汇200场公益文艺活动",
    "venue": "全市20家文化驿站",
    "city": "wuhan",
    "start_date": "2026-06-28",
    "end_date": "2026-09-20",
    "link": "https://m.sohu.com/a/1042651403_121106908/",
    "description": "全城20座特色文化驿站同步联动，200场公益文化活动全部免费开放。包括戏曲驿站（昆曲清唱、少儿京剧展演）、书画驿站（公益书法课程、手工体验）、陶瓷驿站（知音窑陶瓷烧造技艺体验）、舞蹈驿站（青少年汉字创意舞蹈、童心美育艺术启蒙）等。",
    "fee": "免费",
    "source": "第49届武汉之夏江城文驿汇",
    "family_friendly": True
})

activities.append({
    "title": "打开艺术之门系列演出",
    "venue": "琴台音乐厅、临空港大剧院",
    "city": "wuhan",
    "start_date": "2026-07-03",
    "end_date": "2026-08-23",
    "link": "https://m.hbtv.com.cn/p/4617778.html",
    "description": "武汉暑期公益文化品牌，20元起的惠民票价。临空港大剧院上演12部亲子剧目共18场演出；琴台音乐厅28场高水平演出与2场公益艺术课堂，涵盖交响乐、器乐、声乐、国风民乐、亲子视听音乐会等。是暑期亲子艺术启蒙的绝佳选择。",
    "fee": "收费（20元起）",
    "source": "武汉开启打开艺术之门惠民演出",
    "family_friendly": True
})

activities.append({
    "title": "武汉市少年儿童图书馆小脚印故事吧",
    "venue": "武汉市少年儿童图书馆五楼报告厅",
    "city": "wuhan",
    "start_date": "2026-07-04",
    "end_date": "2026-08-15",
    "link": "https://m.sohu.com/a/1042110965_121106908/",
    "description": "向3-7岁低龄儿童开展的绘本阅读活动。暑期共四场：7月4日童心向党 闪闪红星（献礼建党105周年）、7月18日《来喝水吧》、8月1日非遗文化《属于我们的宝藏》、8月15日小花伞专场。关注武汉市少年儿童图书馆微信公众号报名。",
    "fee": "免费需报名",
    "source": "武汉市少年儿童图书馆暑假活动安排",
    "family_friendly": True
})

activities.append({
    "title": "武汉市少年儿童图书馆千字屋儿童想象力空间",
    "venue": "武汉市少年儿童图书馆一楼千字屋",
    "city": "wuhan",
    "start_date": "2026-07-04",
    "end_date": "2026-08-30",
    "link": "https://m.sohu.com/a/1042110965_121106908/",
    "description": "沉浸式探索千字屋、分享绘本图书故事、开展趣味游戏，让孩子在游戏中分享互学。暑期每周六日开放，上午10:00-11:00，下午14:30-15:30。是培养孩子想象力、表达能力和社交能力的好地方。",
    "fee": "免费需报名",
    "source": "武汉市少年儿童图书馆暑假活动安排",
    "family_friendly": True
})

activities.append({
    "title": "武汉市少年儿童图书馆小小图书管理员",
    "venue": "武汉市少年儿童图书馆",
    "city": "wuhan",
    "start_date": "2026-07-14",
    "end_date": "2026-08-08",
    "link": "https://m.sohu.com/a/1042110965_121106908/",
    "description": "图书馆管理员职业体验活动，包括图书整理、图书咨询服务、读者借阅服务等。分两批：第一批培训7月14日，上岗7月15日-18日；第二批培训8月4日，上岗8月5日-8日。培养孩子的责任感和服务意识。",
    "fee": "免费需报名",
    "source": "武汉市少年儿童图书馆暑假活动安排",
    "family_friendly": True
})

activities.append({
    "title": "我是长江的孩子跟着诗词游长江城际童行研学",
    "venue": "武汉市、黄石市",
    "city": "wuhan",
    "start_date": "2026-07-15",
    "end_date": "2026-08-15",
    "link": "https://m.sohu.com/a/1042110965_121106908/",
    "description": "组织武汉都市圈城市的小读者从诗词走进现实，在行走中认识长江沿线城市，加深对长江文化的立体认知。活动时间7月中旬-8月中旬，在武汉市、黄石市等地开展。关注武汉市少年儿童图书馆微信公众号报名。",
    "fee": "部分免费",
    "source": "武汉市少年儿童图书馆暑假活动安排",
    "family_friendly": True
})

activities.append({
    "title": "非遗文化读书会（石头画、剪纸）",
    "venue": "武汉市少年儿童图书馆五楼报告厅",
    "city": "wuhan",
    "start_date": "2026-07-19",
    "end_date": "2026-08-02",
    "link": "https://m.sohu.com/a/1042110965_121106908/",
    "description": "围绕中国非物质文化遗产相关知识，开展有针对性的阅读+活动。第一场7月19日石头画（主讲人沈海鹰），第二场8月2日剪纸（主讲人余嘉）。让孩子们近距离接触非遗文化，动手实践传统技艺。",
    "fee": "免费需报名",
    "source": "武汉市少年儿童图书馆暑假活动安排",
    "family_friendly": True
})

activities.append({
    "title": "童音诵长江少儿诗词朗诵展演",
    "venue": "武汉市少年儿童图书馆",
    "city": "wuhan",
    "start_date": "2026-06-05",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1042110965_121106908/",
    "description": "参与者围绕长江主题，选择与长江流域相关的古典或现代诗词作品，以朗诵为基础，可融入诗词背后的故事、诗人故事或诗词解读。作品征集6月5日-7月15日，评审7月中下旬，结果8月中下旬公布。",
    "fee": "免费",
    "source": "武汉市少年儿童图书馆暑假活动安排",
    "family_friendly": True
})

activities.append({
    "title": "武汉自然博物馆小小探险家实景剧游",
    "venue": "武汉自然博物馆（园博园）",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.weibo.cn/detail/5320913085273553",
    "description": "馆内小小探险家实景剧游上线，8位趣味NPC在线带队闯关。沉浸式逛展厅解锁自然知识，避暑、研学、遛娃一站式搞定。活动时段14:00-17:00。全球最大的大河文明主题博物馆，恐龙化石、动物标本非常震撼。",
    "fee": "免费",
    "source": "武汉市文化和旅游局微博",
    "family_friendly": True
})

activities.append({
    "title": "武汉极地海洋度假区夜宿海洋馆",
    "venue": "武汉极地海洋度假区",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.wuhan.gov.cn/sy/whyw/202508/t20250825_2637728.shtml",
    "description": "和10000+动物一起入眠是什么样的体验？晚上在蔚蓝的海底隧道旁搭起白色气垫帐篷，伴着鱼儿入眠，是今夏亲子家庭的热门之选，独特的海洋夜宿体验令人难忘。还可以看企鹅、白鲸、海豚表演，孩子超兴奋。",
    "fee": "收费",
    "source": "武汉凭夜游跻身暑期全国热门旅游目的地",
    "family_friendly": True
})

activities.append({
    "title": "武汉植物园夜游研学活动",
    "venue": "武汉植物园",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.wuhan.gov.cn/sy/whyw/202508/t20250825_2637728.shtml",
    "description": "武汉植物园开启植植屋夏夜奇遇记独立夜宿营和夜游植物园单日营活动。孩子们第一次离开家自己整理睡袋，鼓起勇气抓昆虫、抱宠物蛇，亲手做叫花鸡腿、手工香皂，感受自然的神奇。",
    "fee": "收费",
    "source": "武汉凭夜游跻身暑期全国热门旅游目的地",
    "family_friendly": True
})

activities.append({
    "title": "武汉自然博物馆奇妙夜小小夜巡员",
    "venue": "武汉自然博物馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.wuhan.gov.cn/sy/whyw/202508/t20250825_2637728.shtml",
    "description": "小小夜巡员活动带着孩子们开启特别的夜间上岗体验，孩子们接受巡馆培训，完成展品检查、设备确认、安全巡视和环境观察等任务，完成后获得专属社会实践证书。是非常有意义的夜间科普体验活动。",
    "fee": "收费",
    "source": "武汉凭夜游跻身暑期全国热门旅游目的地",
    "family_friendly": True
})

activities.append({
    "title": "大国少年守护微笑天使长江生态文明实践行",
    "venue": "武汉白鳍豚馆（洪山区南望山西路7号）",
    "city": "wuhan",
    "start_date": "2026-07-22",
    "end_date": "2026-07-22",
    "link": "http://m.toutiao.com/group/7657007274824598079/",
    "description": "走进武汉白鳍豚馆，化身江豚科考小队员，探寻长江水生生物的秘密，聆听白鱀豚淇淇的动人故事。沉浸式科普课堂、江豚行为监测员、长江微生态瓶创作、结营认证等丰富内容。招募6-12岁少年儿童，20组家庭。",
    "fee": "免费需报名",
    "source": "市妇儿中心暑期关爱活动清单",
    "family_friendly": True
})

activities.append({
    "title": "挺膺护家国童心向未来国防教育实践行",
    "venue": "武汉大军山国际营地",
    "city": "wuhan",
    "start_date": "2026-07-08",
    "end_date": "2026-07-08",
    "link": "http://m.toutiao.com/group/7657007274824598079/",
    "description": "走进武汉大军山国际营地，触摸大国重器，重走长征险途，在沉浸式体验中厚植家国情怀。国防展厅零距离参观、专家讲堂涨知识、高射炮协同发射、气炮射击、坦克巡游打卡、绳索桥体验军旅热血。招募6-12岁少年儿童，25组家庭。",
    "fee": "免费需报名",
    "source": "市妇儿中心暑期关爱活动清单",
    "family_friendly": True
})

activities.append({
    "title": "大别山小作家7天6晚创作营",
    "venue": "大别山",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://cjweek.cjn.cn/h5/html5/2026-06/18/content_42487_3548960.htm",
    "description": "跟着楚才专家走进大别山，敲响创吉尼斯世界纪录的最大铜锣、亲手触摸歼-6战斗机、坐坦克越野、体验真人CS、射箭、提灯寻夏夜小生命、下田摘菜、土灶生火做饭、喂萌宠。学习五感观察法、细节雕琢术、情节巧构思三项创作本领。",
    "fee": "收费",
    "source": "六大暑期特色营",
    "family_friendly": True
})

activities.append({
    "title": "砺剑少年实训演练7天6晚独立营",
    "venue": "武汉国防教育基地",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://cjweek.cjn.cn/h5/html5/2026-06/18/content_42487_3548960.htm",
    "description": "7天6晚独立成长营，探秘装备构造并实操拆解自制模型可带走；体验战术攻防、救援协作、红蓝对抗、剧情任务；应急急救实训，止血、包扎、防溺水；触摸实战战斗机，听英雄故事；挑战重走长征路。",
    "fee": "收费",
    "source": "六大暑期特色营",
    "family_friendly": True
})

activities.append({
    "title": "智控苍穹解码未来3天2晚科创营",
    "venue": "武汉机场实训基地、AI实验室",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://cjweek.cjn.cn/h5/html5/2026-06/18/content_42487_3548960.htm",
    "description": "把前沿科技变成孩子能摸、能玩、能创造的实践课堂。在机场实训基地、AI实验室、无人机训练场，零距离探秘机库、塔台指挥、跑道系统；沉浸式参与无人机操控；拆解AI核心密码，直击自动驾驶核心技术。",
    "fee": "收费",
    "source": "六大暑期特色营",
    "family_friendly": True
})

activities.append({
    "title": "知音湖北博物之旅四大主题研学走廊",
    "venue": "湖北省各博物馆",
    "city": "wuhan",
    "start_date": "2026-07-16",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663294140938977827/",
    "description": "湖北省文物局正式发布四大主题研学走廊：荆楚文化溯源线、红色基因传承线、长江文明探源线、科技奥秘探索线，依托全省精华文博资源，实现文博+教育+旅游深度融合。是暑期亲子研学的优质选择。",
    "fee": "部分免费",
    "source": "全国大中小学生暑假礼物",
    "family_friendly": True
})

activities.append({
    "title": "武汉欢乐谷夏浪狂欢节",
    "venue": "武汉欢乐谷",
    "city": "wuhan",
    "start_date": "2026-07-04",
    "end_date": "2026-08-31",
    "link": "http://www.ctdsb.net/c1722_202607/2789827.html",
    "description": "集明星演艺、音乐现场、潮流文化与沉浸式互动于一体的夏日盛事。多位明星及网红轮番登场，创新推出天团综艺场模式，猫鼠游戏、平衡木挑战、海洋球寻宝等热门综艺桥段互动。夜场开至22:00，持续到8月31日。",
    "fee": "收费",
    "source": "武汉欢乐谷夏浪狂欢节启幕",
    "family_friendly": True
})

activities.append({
    "title": "武汉欢乐谷武汉话动物城",
    "venue": "武汉欢乐谷",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7659744832406946304/",
    "description": "2026年全新上线的全国首创方言文化沉浸式亲子主题区，涵盖2600平方米全室内恒温场馆与6大室外亲子游乐设备。四大原创方言萌宠IP——马呼象、虚狐、拉呱集体亮相，武汉话俚语被做成可爱的玩偶。",
    "fee": "收费",
    "source": "雨天不用宅家！20+宝藏室内场馆遛娃绝了",
    "family_friendly": True
})

activities.append({
    "title": "玛雅海滩水公园极速降温计划",
    "venue": "玛雅海滩水公园",
    "city": "wuhan",
    "start_date": "2026-06-27",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7655591655768097280/",
    "description": "17万平方米超大水上乐园，60+项目全面开放。搭建冰屋群落和真冰体验区，雾森降温系统、遮阳设施及冰块降温装置，推出全面防晒降温体系。水质管理方面全园水域每4小时完成一次整体水循环，安全有保障。",
    "fee": "收费",
    "source": "直冲35℃，武汉出招了！",
    "family_friendly": True
})

activities.append({
    "title": "全市40家泳池暑期免费开放",
    "venue": "全市40家定点游泳馆",
    "city": "wuhan",
    "start_date": "2026-07-12",
    "end_date": "2026-07-31",
    "link": "http://m.toutiao.com/group/7657030241726120467/",
    "description": "汗动青春，营在江城2026年奔跑吧·少年夏令营免费游泳服务活动，全市义务教育阶段的中小学生可免费游泳20天。每天9:00-11:00、15:00-17:00开放。免费入场的中小学生须有一名家长陪同监护，家长按优惠票价2元购票入场。",
    "fee": "学生免费家长2元",
    "source": "武汉40家泳池将免费开放",
    "family_friendly": True
})

# 继续添加更多活动...

activities.append({
    "title": "武昌区红领巾讲解员活动",
    "venue": "武昌区各红色场馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662671908235657780/",
    "description": "新时代红领巾小先生主题实践活动，组织青少年走进红色场馆、城市地标开展讲解实践。开班首日走进武汉规划展示馆，开展逐梦十五五·童眼看武汉主题活动，在总体规划模型大厅了解武汉未来发展蓝图。",
    "fee": "免费",
    "source": "武昌区爱心托管班开班首日活动",
    "family_friendly": True
})

activities.append({
    "title": "汉剧非遗美育营",
    "venue": "武汉临空港大剧院（东西湖区）",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hbwh.wenming.cn/zt2026/2026sqjzxd/2026dtjj/202607/t20260710_9295270.html",
    "description": "东西湖区暑期特色夏令营之一，让青少年近距离接触汉剧这一非遗传统艺术。学习汉剧基础知识、唱腔、身段，体验戏曲化妆、服装穿戴等，感受传统戏曲文化的魅力，培养艺术素养。",
    "fee": "收费",
    "source": "东西湖区暑期集中行动开启",
    "family_friendly": True
})

activities.append({
    "title": "星河童声合唱夏令营",
    "venue": "武汉临空港大剧院（东西湖区）",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hbwh.wenming.cn/zt2026/2026sqjzxd/2026dtjj/202607/t20260710_9295270.html",
    "description": "东西湖区暑期特色夏令营，为热爱歌唱的青少年提供专业的合唱训练机会。在专业老师指导下学习声乐技巧、合唱配合，培养音乐素养和团队协作能力，是暑期艺术学习的好选择。",
    "fee": "收费",
    "source": "东西湖区暑期集中行动开启",
    "family_friendly": True
})

activities.append({
    "title": "区文化馆市民夜校艺术课程",
    "venue": "东西湖区文化馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hbwh.wenming.cn/zt2026/2026sqjzxd/2026dtjj/202607/t20260710_9295270.html",
    "description": "免费开设含唱歌、绘画、手工制作、曲艺、舞蹈、古琴六大门类的市民夜校艺术课程，及青少年戏剧、古筝艺术普及两类专项培训班。各类课程合计80次课，是暑期学习艺术技能、丰富文化生活的好机会。",
    "fee": "免费",
    "source": "东西湖区暑期集中行动开启",
    "family_friendly": True
})

activities.append({
    "title": "东西湖区图书馆50余场暑期活动",
    "venue": "东西湖区图书馆及各社区",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hbwh.wenming.cn/zt2026/2026sqjzxd/2026dtjj/202607/t20260710_9295270.html",
    "description": "区图书馆举办50余场绘本阅读、科普实验及非遗体验活动，18场流动图书馆进社区。将优质的阅读和文化服务送到居民家门口，让青少年在书香中度过充实有意义的暑假。",
    "fee": "免费",
    "source": "东西湖区暑期集中行动开启",
    "family_friendly": True
})

activities.append({
    "title": "家公益幸福涟家亲子阅读活动",
    "venue": "东西湖区各社区",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hbwh.wenming.cn/zt2026/2026sqjzxd/2026dtjj/202607/t20260710_9295270.html",
    "description": "区妇联开展的家公益幸福涟家亲子阅读等活动20场以上，通过亲子共读、阅读分享、手工制作等多种形式，增进亲子关系，培养孩子的阅读兴趣和习惯，营造良好的家庭阅读氛围。",
    "fee": "免费",
    "source": "东西湖区暑期集中行动开启",
    "family_friendly": True
})

activities.append({
    "title": "护星计划法趣夏令营",
    "venue": "东西湖区各托管班",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hbwh.wenming.cn/zt2026/2026sqjzxd/2026dtjj/202607/t20260710_9295270.html",
    "description": "区司法局擦亮护星计划 法趣夏令营品牌，深入托管班普及《中华人民共和国宪法》《民法典》《未成年人保护法》。通过趣味普法课程、互动游戏、案例讲解等形式，让青少年在轻松愉快的氛围中学法、懂法、守法。",
    "fee": "免费",
    "source": "东西湖区暑期集中行动开启",
    "family_friendly": True
})

activities.append({
    "title": "凌云剧场暑期法治小课堂",
    "venue": "东西湖区法院",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hbwh.wenming.cn/zt2026/2026sqjzxd/2026dtjj/202607/t20260710_9295270.html",
    "description": "区法院组织模拟庭审，依托凌云剧场开设暑期法治小课堂，线上推出普法专栏。让青少年亲身体验法庭审判过程，了解法律程序和司法公正，增强法治观念和法律意识。",
    "fee": "免费",
    "source": "东西湖区暑期集中行动开启",
    "family_friendly": True
})

activities.append({
    "title": "关爱生命救在身边急救课堂",
    "venue": "东西湖区各社区、学校",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hbwh.wenming.cn/zt2026/2026sqjzxd/2026dtjj/202607/t20260710_9295270.html",
    "description": "区卫健局举办的关爱生命，救在身边急救课堂，组织专业人员进社区、进学校开展。教授心肺复苏、止血包扎、异物卡喉等急救知识和技能，提高青少年的应急救护能力和安全意识。",
    "fee": "免费",
    "source": "东西湖区暑期集中行动开启",
    "family_friendly": True
})

activities.append({
    "title": "武昌区非遗技忆系列活动",
    "venue": "武昌区各文化场馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hb.people.com.cn/n2/2026/0704/c192237-41629497.html",
    "description": "武昌区文旅局推出的非遗技忆系列活动，让传统文化与城市记忆可触可感。包括非遗体验、非遗展览、非遗市集等多种形式，让青少年近距离接触和体验传统非遗技艺，感受传统文化的魅力。",
    "fee": "免费",
    "source": "武昌区暑期集中行动启动",
    "family_friendly": True
})

activities.append({
    "title": "武昌区走读武昌系列活动",
    "venue": "武昌区各历史文化街区",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hb.people.com.cn/n2/2026/0704/c192237-41629497.html",
    "description": "武昌区文旅局推出的走读武昌系列活动，带领青少年走进武昌的大街小巷，探访历史建筑、了解城市故事、感受文化底蕴。在行走中学习，在探索中成长，深度认识这座英雄之城。",
    "fee": "免费",
    "source": "武昌区暑期集中行动启动",
    "family_friendly": True
})

activities.append({
    "title": "VR长征体验项目",
    "venue": "武昌区各文化场馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hb.people.com.cn/n2/2026/0704/c192237-41629497.html",
    "description": "人民网·梦幻灵境空间带来的VR长征体验项目，邀请青少年在虚拟与现实交织中重走长征路。通过先进的VR技术沉浸式感受长征的艰辛与伟大，接受红色教育，传承长征精神。",
    "fee": "免费",
    "source": "武昌区暑期集中行动启动",
    "family_friendly": True
})

activities.append({
    "title": "12355青少年心理服务站",
    "venue": "武昌区",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hb.people.com.cn/n2/2026/0704/c192237-41629497.html",
    "description": "团区委开放12355心理服务站，为青少年及家长提供心理咨询与疏导服务。帮助青少年缓解暑期学习压力、调节情绪、解决心理困惑，守护青少年心理健康，让孩子们度过一个阳光健康的假期。",
    "fee": "免费",
    "source": "武昌区暑期集中行动启动",
    "family_friendly": True
})

activities.append({
    "title": "硚口区图书馆小小理财家活动",
    "venue": "硚口区各街道社区",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-07-31",
    "link": "http://m.toutiao.com/group/7657757154769764905/",
    "description": "暑期托管班专场——生财有道·小小理财家成长记。通过《钱是怎么来的》导读与互动游戏，帮助孩子理解金钱的来源与流向，掌握基础金融知识，培养财商与防诈意识，现场实操规划个人账户。",
    "fee": "免费",
    "source": "硚口区图书馆2026年暑期嘉年华",
    "family_friendly": True
})

activities.append({
    "title": "硚口区图书馆皮影戏体验活动",
    "venue": "硚口区各街道社区",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-07-31",
    "link": "http://m.toutiao.com/group/7657757154769764905/",
    "description": "暑期托管班专场——光影魔法师·皮影戏里的大世界。讲解光影原理与非遗皮影艺术，指导孩子们亲手制作皮影角色并演绎迷你《西游记》，实现科学与传统文化的融合体验。社区统一招募参加。",
    "fee": "免费",
    "source": "硚口区图书馆2026年暑期嘉年华",
    "family_friendly": True
})

activities.append({
    "title": "硚口区图书馆香囊制作活动",
    "venue": "硚口区各街道社区",
    "city": "wuhan",
    "start_date": "2026-08-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7657757154769764905/",
    "description": "暑期托管班专场——香囊里的秘密·闻香识药小药师。带领孩子们认识多种芳香中草药，了解香囊的历史文化和药用价值，亲手制作属于自己的中药香囊，感受传统中医药文化的魅力。",
    "fee": "免费",
    "source": "硚口区图书馆2026年暑期嘉年华",
    "family_friendly": True
})

activities.append({
    "title": "硚口区图书馆少儿电影展播",
    "venue": "硚口区图书馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7657757154769764905/",
    "description": "缤纷暑期·光影童行少儿电影展播活动，7月-8月每周六14:30-16:30放映精彩少儿电影。每场50人，无需预约即可观看。是暑期亲子休闲、消暑纳凉的好选择，让孩子们在光影世界中收获快乐。",
    "fee": "免费",
    "source": "硚口区图书馆2026年暑期嘉年华",
    "family_friendly": True
})

activities.append({
    "title": "蔬菜精灵奇遇记绘本活动",
    "venue": "硚口区图书馆",
    "city": "wuhan",
    "start_date": "2026-07-05",
    "end_date": "2026-07-05",
    "link": "http://m.toutiao.com/group/7657757154769764905/",
    "description": "赏析绘本《一园青菜成了精》，体验蔬菜软陶制作。让孩子们在趣味绘本阅读中认识蔬菜，培养不挑食的好习惯，同时通过软陶手工锻炼动手能力和创造力。关注硚口区图书馆微信公众号报名。",
    "fee": "免费需报名",
    "source": "硚口区图书馆2026年暑期嘉年华",
    "family_friendly": True
})

activities.append({
    "title": "小小茶师养成记非遗活动",
    "venue": "硚口区图书馆",
    "city": "wuhan",
    "start_date": "2026-07-12",
    "end_date": "2026-07-12",
    "link": "http://m.toutiao.com/group/7657757154769764905/",
    "description": "了解中国茶文化及汉口茶市历史，体验茶中日月长相框手工制作。让孩子们学习茶道礼仪、了解茶文化知识，感受中华传统文化的博大精深，培养文雅的气质和良好的礼仪习惯。",
    "fee": "免费需报名",
    "source": "硚口区图书馆2026年暑期嘉年华",
    "family_friendly": True
})

activities.append({
    "title": "海洋护卫队生态瓶造梦师科普活动",
    "venue": "硚口区图书馆",
    "city": "wuhan",
    "start_date": "2026-07-19",
    "end_date": "2026-07-19",
    "link": "http://m.toutiao.com/group/7657757154769764905/",
    "description": "科普海洋知识，制作海洋生态瓶。让孩子们了解海洋生态系统，认识各种海洋生物，增强环保意识。亲手制作一个微型海洋生态瓶，把蓝色海洋带回家，是非常有意义的科普体验。",
    "fee": "免费需报名",
    "source": "硚口区图书馆2026年暑期嘉年华",
    "family_friendly": True
})

activities.append({
    "title": "指尖电光奇遇记静电魔法球活动",
    "venue": "硚口区图书馆",
    "city": "wuhan",
    "start_date": "2026-07-26",
    "end_date": "2026-07-26",
    "link": "http://m.toutiao.com/group/7657757154769764905/",
    "description": "科普静电原理，制作静电魔法球。通过趣味实验让孩子们直观感受静电现象，了解电学基础知识，激发对科学的兴趣。亲手制作一个神奇的静电魔法球，探索科学的奥秘。",
    "fee": "免费需报名",
    "source": "硚口区图书馆2026年暑期嘉年华",
    "family_friendly": True
})

activities.append({
    "title": "古人消暑生存史科普活动",
    "venue": "硚口区图书馆",
    "city": "wuhan",
    "start_date": "2026-08-02",
    "end_date": "2026-08-02",
    "link": "http://m.toutiao.com/group/7657757154769764905/",
    "description": "科普夏日节气与消暑知识，讲述老武汉消夏故事，制作花露水。了解古人在没有空调的年代是如何度过炎炎夏日的，感受古人的智慧，还能亲手制作一瓶独一无二的花露水带回家。",
    "fee": "免费需报名",
    "source": "硚口区图书馆2026年暑期嘉年华",
    "family_friendly": True
})

activities.append({
    "title": "玩转衍纸探秘非遗活动",
    "venue": "硚口区图书馆",
    "city": "wuhan",
    "start_date": "2026-08-22",
    "end_date": "2026-08-22",
    "link": "http://m.toutiao.com/group/7657757154769764905/",
    "description": "了解衍纸非遗技艺，制作衍纸书签。衍纸是一门古老的传统手工艺，通过卷、捏、拼贴等手法将细长的纸条变成精美的艺术品。亲手制作一张独特的衍纸书签，感受非遗技艺的魅力。",
    "fee": "免费需报名",
    "source": "硚口区图书馆2026年暑期嘉年华",
    "family_friendly": True
})

activities.append({
    "title": "小小姓氏寻根师国学活动",
    "venue": "硚口区图书馆",
    "city": "wuhan",
    "start_date": "2026-08-16",
    "end_date": "2026-08-16",
    "link": "http://m.toutiao.com/group/7657757154769764905/",
    "description": "了解《百家姓》与姓氏故事，制作姓氏挂件。追寻自己姓氏的起源和历史，了解家族文化的传承，增强对传统文化的认同感和自豪感。还能制作一个专属的姓氏挂件作为纪念。",
    "fee": "免费需报名",
    "source": "硚口区图书馆2026年暑期嘉年华",
    "family_friendly": True
})

# ==================== 补充活动：新洲区 ====================

activities.append({
    "title": "新洲区20个爱心托管班",
    "venue": "新洲区8个街镇20个托管点位",
    "city": "wuhan",
    "start_date": "2026-07-14",
    "end_date": "2026-08-21",
    "link": "http://hbwh.wenming.cn/oldweb/xz/202607/t20260717_9302547.html",
    "description": "全区开设20个标准化托管点位，较去年新增4个，分两批次开展托管，两期均设置15个工作日，每日服务时段8:00至18:00。优先服务留守儿童、经济困难家庭子女、双职工家庭子女。联动多所高校充实志愿师资，整合多部门资源开设安全、艺术、劳动等六大类公益课程。",
    "fee": "免费",
    "source": "新洲2026暑期托管班开课",
    "family_friendly": True
})

activities.append({
    "title": "新洲大峡谷漂流",
    "venue": "新洲区新洲大峡谷漂流景区",
    "city": "wuhan",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7657830589920035362/",
    "description": "武汉海拔最高的纯天然河道漂流项目，总落差高达350米，单段极限落差70米，全程7900米。一河四趣分段式设计：500米高空玻璃滑道、原始峡谷激流、彩虹暗漂隧道、下游平缓亲子河段，全程约2小时，年轻人刺激和家庭休闲都能满足。",
    "fee": "收费",
    "source": "新洲夏日玩水解暑指南",
    "family_friendly": True
})

activities.append({
    "title": "香草伊甸园花漾泼水狂欢季",
    "venue": "新洲区香草伊甸园景区",
    "city": "wuhan",
    "start_date": "2026-07-10",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7657830589920035362/",
    "description": "全新升级打造的花漾泼水狂欢季，傣族泼水节点燃夏日激情，水上非遗打铁花惊艳夜空，篝火晚会载歌载舞，花船巡游碧波缓缓。白天卷起裤腿摸鱼捉虾，夏日花海里泰国睡莲正盛。入夜后灯海秘境、萤火星光、迷雾森林，随手一拍就是大片。",
    "fee": "收费",
    "source": "新洲夏日玩水解暑指南",
    "family_friendly": True
})

activities.append({
    "title": "凤娃古寨水街夏日玩水活动",
    "venue": "新洲区凤娃古寨景区",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7657830589920035362/",
    "description": "高温酷暑的专属快乐藏在凤娃水街！巨型水桶定时倾泻，水花从天而降，园区贴心备好了各式玩水道具，水枪、水盆随时就位，大人小孩直接开启混战模式。还有高空透明滑道，坐上皮艇顺着水流俯冲而下，沿途满目绿意。",
    "fee": "收费",
    "source": "新洲夏日玩水解暑指南",
    "family_friendly": True
})

activities.append({
    "title": "花朝河湾景区暑期采摘赏花游",
    "venue": "新洲区花朝河湾景区",
    "city": "wuhan",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7649311322681426472/",
    "description": "以花朝文化为品牌基石的高品质休闲度假旅游综合体，整合花神文化、情缘文化、民俗文化。暑期可赏荷花、摘桃子，红冠桃、水蜜桃挂满枝头，走进果园亲手采摘新鲜饱满的桃子。还有游船篝火、实景演艺、垂钓采摘、亲子乐活等八大旅游产品板块。",
    "fee": "收费",
    "source": "新洲这些地方请你免费玩",
    "family_friendly": True
})

activities.append({
    "title": "稻田记忆农耕亲子体验",
    "venue": "新洲区稻田记忆景区",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7649311322681426472/",
    "description": "以有机水稻种植为核心的都市田园综合体，占地1456亩。与鸽子亲密互动、亲手推石磨磨豆浆，在朴素的农事活动中感受农耕文化。千亩稻田种植区可以亲历农耕过程，体会粒粒皆辛苦的道理，还有稻田民宿坐看天空云卷云舒。",
    "fee": "收费",
    "source": "新洲这些地方请你免费玩",
    "family_friendly": True
})

# ==================== 补充活动：江夏区 ====================

activities.append({
    "title": "江夏里袁夫稻田趣味插秧活动",
    "venue": "江夏区五里界锦绣村江夏里袁夫稻田大米王国",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.whjxtv.cn/jiangxia_356689.html",
    "description": "近百组亲子家庭走进田间地头，沉浸式体验传统农耕乐趣。传统开秧门仪式拉开序幕，农耕师傅撒谷祈福、示范插秧技法。趣味插秧大赛、泥地抓鸭、泥地龙舟赛等特色项目轮番上演，让城市孩子走出书本真切体会粮食种植的不易。",
    "fee": "收费",
    "source": "近百组家庭在江夏里种下欢乐",
    "family_friendly": True
})

activities.append({
    "title": "梁子湖龙湾半岛哪吒闹海夏日生活季",
    "venue": "江夏区梁子湖龙湾半岛景区",
    "city": "wuhan",
    "start_date": "2026-06-18",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1051642081_220682/",
    "description": "景区化身神话世界，随时随地偶遇神话角色，牵手打卡、趣味互动。鱼灯巡游、佤族喷火、锦鲤献瑞、水韵灵珠、陈塘关大巡游、非遗打铁花等系列实景演出。夏日限定泼水电音派对，清凉泼水狂欢搭配动感电音。购票还可免费玩快乐星球无动力亲子乐园。",
    "fee": "收费",
    "source": "周末来江夏这样玩好过瘾",
    "family_friendly": True
})

activities.append({
    "title": "江夏里武汉老码头夏夜民俗大妙会",
    "venue": "江夏区江夏里武汉老码头",
    "city": "wuhan",
    "start_date": "2026-07-15",
    "end_date": "2026-09-01",
    "link": "https://m.sohu.com/a/1051642081_220682/",
    "description": "夜游重磅升级，营业至凌晨2点。非遗舞龙虾、喷火顶缸、打铁花轮番炸场，李白大秀与情景剧实景上演。夜市烧烤龙虾啤酒不限量，雾森送爽、竹筏赏月，全新玩水乐园首开，大人孩子尽享清凉，越夜越精彩。",
    "fee": "部分收费",
    "source": "周末来江夏这样玩好过瘾",
    "family_friendly": True
})

activities.append({
    "title": "江夏中央大公园草坪音乐会",
    "venue": "江夏区中央大公园天空之城",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1051642081_220682/",
    "description": "7月至8月每个周末19:00-20:30上演浪漫的草坪音乐会（雨天除外）。经典歌曲现场演唱，钢琴旋律悠然流淌，没有舞台围栏，没有门票门槛。吹着柔柔的晚风，与音乐不期而遇，是暑期亲子休闲的绝佳选择。",
    "fee": "免费",
    "source": "周末来江夏这样玩好过瘾",
    "family_friendly": True
})

activities.append({
    "title": "蜜蜂探索馆亲子科普游",
    "venue": "江夏区纸坊街道八分山路蜜蜂探索馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.cyw.com/shop/154302714630",
    "description": "亚洲最大蜜蜂博物馆、国家3A景区、湖北省免费青少年科普教育基地。11个展区中3D蜜蜂探索区是核心，结合声光电技术还原蜜蜂生态。可进入酿蜜实验室亲手操作摇蜜机，换上养蜂人服装进入蜂园寻找蜂王，还能动手做蜂蜜果茶饼干、蜂蜡唇膏。",
    "fee": "收费",
    "source": "蜜蜂探索馆休闲游玩科普探险",
    "family_friendly": True
})

activities.append({
    "title": "江夏青少年宫暑期公益课程",
    "venue": "江夏区文化路43号江夏青少年宫",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://weitoutiao.zjurl.cn/rogue/topic_share/?concern_id=1788403207508009&prevent_activate=1",
    "description": "江夏性价比天花板级别的遛娃地，大部分公益课程免费或超低价。可选课程超多：美术、书法、中国舞、街舞、声乐、瑜伽、油画、素描、国画、动漫、非遗剪纸、南狮特色课。4-18岁小朋友都能报名，线上直接报，省心又划算。",
    "fee": "免费/低价",
    "source": "江夏青少年宫省钱又省力",
    "family_friendly": True
})

# ==================== 补充活动：黄陂区更多 ====================

activities.append({
    "title": "黄陂盘龙水上大世界",
    "venue": "黄陂区横店街道盘龙水上大世界",
    "city": "wuhan",
    "start_date": "2026-06-26",
    "end_date": "2026-08-31",
    "link": "https://www.huangpi.gov.cn/ywdt/jxdt/202606/t20260624_2780945.html",
    "description": "华中地区首座深度融合海洋+长江文脉+未来水科技三大主题的超大规模水乐园。室内+室外双园联动，汇聚20余项高科技玩水项目。室内恒温亲子戏水池、大喇叭、巨兽碗、双层178米水上飞龙、智能分轨峰回路转滑梯，还有小丑巡游、NPC互动、电音泼水节、佤族火秀等演艺。",
    "fee": "收费",
    "source": "黄陂盘龙水上大世界正式开园",
    "family_friendly": True
})

activities.append({
    "title": "裕和夫子山儿童水上乐园",
    "venue": "黄陂区长轩岭裕和夫子山景区",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://hb.news.cn/20260701/32ad98ae81a8444abac2142e6e44c95a/c.html",
    "description": "山野里的童话水世界，占地1370㎡，主打不打挤、不喧闹、水质干净。糖果水寨、七彩滑梯、雨蘑菇和樱桃树淋水阵充满童趣。水深约30-50cm，清澈见底，父母可以彻底安心。更衣区、沐浴区配套齐全。还有全新升级的水上运动中心，桨板、皮划艇等更多亲水玩法。",
    "fee": "收费",
    "source": "黄陂找到一座山有水乐园还有森林学堂",
    "family_friendly": True
})

activities.append({
    "title": "黄陂热雪奇迹+木兰草原联票活动",
    "venue": "黄陂区武汉城建热雪奇迹、木兰草原景区",
    "city": "wuhan",
    "start_date": "2026-06-26",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7657858273588167231/",
    "description": "一票双景解锁零下冰雪+夏日草原双重快乐。热雪奇迹夜场初级不限时滑雪，最长5小时畅滑，雪板雪鞋头盔配套齐全，十余项玩雪项目畅享，暑期限定卡皮巴拉小黄豚。木兰草原3日通玩，含云中战歌、天水盛典两大实景演出，观光小火车，12项游乐项目。",
    "fee": "收费（联票208元）",
    "source": "208元玩转黄陂2大顶流景区",
    "family_friendly": True
})

activities.append({
    "title": "锦里沟木兰神牛溪峡谷漂流",
    "venue": "黄陂区蔡店街锦里土司城景区",
    "city": "wuhan",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7658228015800877620/",
    "description": "一次解锁双重漂流体验！前半段高空玻璃滑道俯冲，后半段原生态森林峡谷河道，全长4.8公里、垂直落差220米，刺激度拉满。漂流结束直接衔接土家泼水广场，玩水一站式不转场，国风土司建筑拍照超出片。",
    "fee": "收费",
    "source": "黄陂玩水最全攻略",
    "family_friendly": True
})

activities.append({
    "title": "木兰胜天森林漂流",
    "venue": "黄陂区木兰胜天旅游景区",
    "city": "wuhan",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7658228015800877620/",
    "description": "藏在山林深处的原生态森林漂流，全程林荫覆盖，清凉无暴晒。水流缓急适中，既有冲刺的刺激，也有随波漂流的惬意，老人小孩都能玩。购票即可不限次数漂流，早上漂、下午漂、傍晚接着漂，实现漂流自由。",
    "fee": "收费",
    "source": "黄陂玩水最全攻略",
    "family_friendly": True
})

# ==================== 补充活动：商业综合体 ====================

activities.append({
    "title": "楚河汉街傣住夏天泼水狂欢",
    "venue": "武昌区楚河汉街太极广场",
    "city": "wuhan",
    "start_date": "2026-07-18",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663369762512077352/",
    "description": "汉街直接把傣式泼水狂欢搬到武汉！炎炎夏日一起来清凉狂欢。端起水盆、抄起水枪，在超嗨音浪中开启泼水大战，水花飞溅间快乐直冲头顶。是暑期亲子消暑、感受异域风情的绝佳选择，大小朋友都能玩得尽兴。",
    "fee": "免费",
    "source": "武汉周末超精彩10+活动",
    "family_friendly": True
})

activities.append({
    "title": "武商MALL众圆七彩风车亲子手工",
    "venue": "青山区武商MALL众圆B馆1F",
    "city": "wuhan",
    "start_date": "2026-07-11",
    "end_date": "2026-08-31",
    "link": "https://m.weibo.cn/detail/5318419232590989",
    "description": "七彩风车亲子手工活动，招募亲子家庭参与，材料工具全免费，空手到场就能玩。亲手做迎风转动的小风车，暑期亲子放电好去处。武商MALL众圆还有众多儿童游乐、餐饮、购物配套，可以安排一整天的亲子行程。",
    "fee": "免费",
    "source": "武商MALL众圆免费风车DIY",
    "family_friendly": True
})

activities.append({
    "title": "WS梦乐园蛋仔主题活动",
    "venue": "武昌区武商梦时代WS梦乐园",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://sw.wuhan.gov.cn/xwdt/gzdt/202606/t20260601_2771374.shtml",
    "description": "全新升级开放式游园，1000只蛋仔气球免费送、趣味蛋仔碰碰会、魔力蛋仔气球雨、童趣蛋仔巡游轮番上演。还有限定儿童剧温情上演，一站式解锁童真欢乐时光。室内乐园不怕日晒雨淋，是暑期遛娃的绝佳选择。",
    "fee": "收费",
    "source": "武商梦时代童潮风尚秀",
    "family_friendly": True
})

activities.append({
    "title": "造梦手帐节4.0",
    "venue": "汉阳区王家湾摩尔城1楼中庭",
    "city": "wuhan",
    "start_date": "2026-07-18",
    "end_date": "2026-07-19",
    "link": "http://m.toutiao.com/group/7663369762512077352/",
    "description": "原创手帐、独立插画、精品文具、手作达人齐聚的手账节。孩子们可以在这里发现各种有趣的文创产品，激发创造力和审美能力。还可以和手作达人交流学习，亲手制作属于自己的手账本，是非常有意义的亲子文化活动。",
    "fee": "免费",
    "source": "武汉周末超精彩10+活动",
    "family_friendly": True
})

# ==================== 补充活动：书店 ====================

activities.append({
    "title": "物外书店鱼妈妈讲故事",
    "venue": "汉阳区物外书店汉阳总店等门店",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_6453893061_180ae97c500100a451.html",
    "description": "物外书店经典品牌活动，每周六下午为孩子们带来精彩的绘本故事。由专业的阅读推广人带领，通过生动的讲述、互动问答，激发孩子们的阅读兴趣。还有手工延伸活动，让阅读变得更加立体有趣。",
    "fee": "免费",
    "source": "暑假武汉各大图书馆的正确打开方式",
    "family_friendly": True
})

activities.append({
    "title": "武汉科技馆书香伴夏科普阅读季",
    "venue": "武汉科技馆",
    "city": "wuhan",
    "start_date": "2026-06-27",
    "end_date": "2026-08-31",
    "link": "http://m.cjn.cn/Detail/?id=5492236&typeid=0",
    "description": "书香伴夏·科学同行2026暑期科普阅读季，组织名家科普讲座，邀请科学大家与文化名家走进科技馆、社区与青少年面对面交流。推出科普研学实践活动，带领青少年走进科技馆、高新企业、重点实验室等科创一线阵地。还有暑期阅读挑战、科普书单推荐、亲子共读分享等线上线下联动活动。",
    "fee": "免费",
    "source": "2026暑期科普阅读季启动",
    "family_friendly": True
})

# ==================== 补充活动：汉南区/武汉经开区 ====================

activities.append({
    "title": "汤湖图书馆暑期亲子阅读活动",
    "venue": "武汉经开区汤湖图书馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1012175619_121106908/",
    "description": "坐落于美丽的汤湖之滨，环境优美。暑期开展思政知识闯关、换书市集、奶龙IP亲子诗词分享会等丰富活动。作者亲临现场与职工家庭互动，将学习融入欢声笑语之中。旁边还有汤湖美术馆、汤湖戏院，可以一站式享受文化盛宴。",
    "fee": "免费",
    "source": "车谷职工思政文化主题活动",
    "family_friendly": True
})

activities.append({
    "title": "武汉经开区工人文化宫亲子活动",
    "venue": "武汉经开区工人文化宫",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1012175619_121106908/",
    "description": "被誉为最美的工人文化宫，坐落于汤湖之滨。暑期开展各类亲子文化活动，包括涂色创作、折纸飞机比赛、初心向远连环画公教活动等。还有儿童剧演出，传递勇敢与成长的力量。融思政教育、文化体验与互动交流于一体。",
    "fee": "部分免费",
    "source": "车谷职工思政文化主题活动",
    "family_friendly": True
})

# ==================== 补充活动：更多特色活动 ====================

activities.append({
    "title": "问津书院国学研学游",
    "venue": "新洲区旧街孔子河畔问津书院",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.whxinzhou.gov.cn/zjxz/xzgk/202004/t20200422_1055592.shtml",
    "description": "因《论语》中孔子使子路问津的典故而得名，距今已有两千多年历史，是武汉市乃至湖北省唯存的儒学遗迹。景区按礼、乐、射、御、书、数六艺思想建设，是传播国学和儒家文化的重要基地。暑期可开展国学诵读、传统礼仪学习、书法体验等研学活动。",
    "fee": "收费",
    "source": "新洲区风景名胜介绍",
    "family_friendly": True
})

activities.append({
    "title": "道观河风景旅游区暑期避暑游",
    "venue": "新洲区道观河风景旅游区",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.icauto.com.cn/trip/hot_5429.html",
    "description": "武汉新洲区著名的旅游景点，以宜人的环境和独特的文化底蕴闻名。有报恩禅寺、世界第一玉卧佛等景点。可以坐快艇环湖游览，湖中波光粼粼。适合徒步登山、避暑休闲，空气质量好，适合欣赏自然生态景观，是亲子避暑好去处。",
    "fee": "收费",
    "source": "新洲区必玩十大景区",
    "family_friendly": True
})

activities.append({
    "title": "中山舰博物馆暑期研学",
    "venue": "江夏区金口街道中山舰路特1号中山舰博物馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.cyw.com/xianlu/19062712014929",
    "description": "中山舰浓缩着中国近代史，经历风云变迁、战火创痛。一家人带孩子开启历史研学之旅，漫步中山舰展馆内了解近代历史。还可搭配金丝楠木博物馆、白云洞军事体验区、蜜蜂探索馆组成军事科普亲子游线路。",
    "fee": "免费需预约",
    "source": "亲子趣玩江夏军事科普游",
    "family_friendly": True
})

activities.append({
    "title": "白云洞军事体验区亲子游",
    "venue": "江夏区白云洞军事体验区",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.cyw.com/xianlu/19062712014929",
    "description": "实地接触军事，收藏有轻重机枪、地雷、火箭筒、无后坐力炮、反坦克导弹、水雷等轻重武器甚至坦克在内的1000多件现当代兵器。乘着坦克走进百年军工企业，探寻近代武器发展史，近距离感受陆战之王的震撼力量。",
    "fee": "收费",
    "source": "亲子趣玩江夏军事科普游",
    "family_friendly": True
})

activities.append({
    "title": "金丝楠木博物馆艺术研学",
    "venue": "江夏区金丝楠木博物馆",
    "city": "wuhan",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.cyw.com/xianlu/19062712014929",
    "description": "探访明清时代的奇珍异宝，赏艺术精品，寓教于乐。古朴的家具散发着古韵古香，石凳石桌经过精心雕琢。还能看老一辈的艺术家们挥毫洒墨，一书一画，让孩子在潜移默化中接受传统文化的熏陶。",
    "fee": "收费",
    "source": "亲子趣玩江夏军事科普游",
    "family_friendly": True
})

print(f"共生成 {len(activities)} 条活动")

with open('/workspace/goout/output/raw/real_activities_wuhan_batch4.json', 'w', encoding='utf-8') as f:
    json.dump(activities, f, ensure_ascii=False, indent=2)

print("文件已保存到 /workspace/goout/output/raw/real_activities_wuhan_batch4.json")
