import json
from datetime import datetime

# 读取现有活动数据
with open('/workspace/goout/output/raw/real_activities_chengdu.json', 'r', encoding='utf-8') as f:
    existing_activities = json.load(f)

existing_titles = set(activity['title'] for activity in existing_activities)

# 新收集的活动数据
new_activities = [
    # 儿童剧演出类
    {
        "title": "原色童心·互动亲子科学剧《妙趣实验室》",
        "venue": "原色童心亲子剧场(春熙路茂业百货店)",
        "city": "chengdu",
        "start_date": "2026-07-18",
        "end_date": "2026-07-26",
        "link": "https://m.df962388.com/yanchu/401609.html",
        "description": "互动亲子科学剧，通过趣味实验和互动表演，激发孩子对科学的兴趣，每周六周日演出。",
        "fee": "收费（38-98元）",
        "source": "东方演出网",
        "family_friendly": True
    },
    {
        "title": "格林童话音乐儿童剧《小红帽》",
        "venue": "发伢剧场(苏宁店)",
        "city": "chengdu",
        "start_date": "2026-08-08",
        "end_date": "2026-08-08",
        "link": "https://sichuan.df962388.com/",
        "description": "经典格林童话改编的音乐儿童剧，讲述小红帽与大灰狼斗智斗勇的故事，适合亲子观看。",
        "fee": "收费（48-240元）",
        "source": "东方演出网",
        "family_friendly": True
    },
    {
        "title": "百老汇互动亲子科学剧《化学秀》中文版",
        "venue": "成都城市音乐厅·歌剧厅",
        "city": "chengdu",
        "start_date": "2026-09-13",
        "end_date": "2026-09-13",
        "link": "https://www.xinruipiao.com/ertongqinzi/28705.html",
        "description": "百老汇正版授权互动亲子科学剧，用生动有趣的化学实验表演，带领孩子探索化学世界的奥秘，演出时长约90分钟。",
        "fee": "收费（108-480元）",
        "source": "新锐票",
        "family_friendly": True
    },
    {
        "title": "英文原版合家欢音乐剧《马达加斯加》",
        "venue": "成都高新中演大剧院",
        "city": "chengdu",
        "start_date": "2026-07-01",
        "end_date": "2026-07-31",
        "link": "https://m.weibo.cn/detail/5315179667522788",
        "description": "英文原版合家欢音乐剧，讲述动物园里的动物们逃到马达加斯加的冒险故事，带娃和企鹅帮一起快乐冒险，亲子欢乐源泉。",
        "fee": "收费",
        "source": "成都高新微博",
        "family_friendly": True
    },
    {
        "title": "儿童剧《真假美猴王》",
        "venue": "成都高新中演大剧院",
        "city": "chengdu",
        "start_date": "2026-06-01",
        "end_date": "2026-06-01",
        "link": "http://m.toutiao.com/group/7646060329910174271/",
        "description": "经典西游记故事改编儿童剧，讲述真假美猴王的传奇故事，适合全年龄段儿童观看。",
        "fee": "收费",
        "source": "天府艺展",
        "family_friendly": True
    },
    {
        "title": "儿童剧《疯狂的废纸世界》",
        "venue": "四川大剧院",
        "city": "chengdu",
        "start_date": "2026-06-01",
        "end_date": "2026-06-01",
        "link": "http://m.toutiao.com/group/7646060329910174271/",
        "description": "创意互动儿童剧，通过废纸的奇妙世界启发孩子的想象力和环保意识。",
        "fee": "收费",
        "source": "天府艺展",
        "family_friendly": True
    },
    {
        "title": "儿童剧《哪吒之再世英雄》",
        "venue": "成都国际剧院",
        "city": "chengdu",
        "start_date": "2026-06-01",
        "end_date": "2026-06-01",
        "link": "http://m.toutiao.com/group/7646060329910174271/",
        "description": "以哪吒故事为背景的原创儿童剧，展现少年英雄的成长历程，传递勇敢正义的价值观。",
        "fee": "收费",
        "source": "天府艺展",
        "family_friendly": True
    },
    {
        "title": "儿童剧《屁屁侦探之怪盗U对怪盗U》",
        "venue": "成都国际剧院",
        "city": "chengdu",
        "start_date": "2026-06-06",
        "end_date": "2026-06-06",
        "link": "http://m.toutiao.com/group/7646060329910174271/",
        "description": "改编自人气儿童绘本《屁屁侦探》，充满趣味推理和互动环节，适合亲子共同参与。",
        "fee": "收费",
        "source": "天府艺展",
        "family_friendly": True
    },
    {
        "title": "舞剧《花木兰》",
        "venue": "成都城市音乐厅",
        "city": "chengdu",
        "start_date": "2026-07-04",
        "end_date": "2026-07-05",
        "link": "https://m.sohu.com/a/1044889386_355475/",
        "description": "斩获中国舞蹈最高奖荷花奖的舞剧，聚焦少女木兰内心成长，铜镜、圆月、可旋转圆形舞台贯穿全场，刚柔并济展现巾帼风骨，亲子家庭观演主力。",
        "fee": "收费",
        "source": "锦观新闻",
        "family_friendly": True
    },
    {
        "title": "舞剧《陈寿·三国志》",
        "venue": "四川大剧院",
        "city": "chengdu",
        "start_date": "2026-07-02",
        "end_date": "2026-07-03",
        "link": "https://m.sohu.com/a/1044889386_355475/",
        "description": "本土原创舞剧，以巨型竹简、文字雨等沉浸式东方美学装置，还原史学家陈寿编撰《三国志》的全过程，叙事浅显易懂，适合带孩子了解巴蜀历史。",
        "fee": "收费（79-99元惠民票价）",
        "source": "锦观新闻",
        "family_friendly": True
    },
    # 主题乐园类
    {
        "title": "成都欢乐谷夏浪狂欢节·星光小镇",
        "venue": "成都欢乐谷",
        "city": "chengdu",
        "start_date": "2026-07-04",
        "end_date": "2026-08-30",
        "link": "https://cd.happyvalley.cn/?id=8710871.htm",
        "description": "成都欢乐谷暑期重磅活动，包含星光小镇、夏浪狂欢节、音乐缘宇宙三大主题，水陆双园齐开，百余游乐设备一票通玩，夜场延时至22点，适合全家出游。",
        "fee": "收费",
        "source": "成都欢乐谷官网",
        "family_friendly": True
    },
    {
        "title": "成都欢乐谷HOMO电音节",
        "venue": "成都欢乐谷",
        "city": "chengdu",
        "start_date": "2026-07-02",
        "end_date": "2026-08-28",
        "link": "https://www.qianggen.net/2009/tuan83347/",
        "description": "持续近两个月的电音盛宴，每周邀约大咖演出，涵盖嘻哈、摇滚、电音、流行等多种风格，水陆双园百余项目一票通玩。",
        "fee": "收费（夜场票100元）",
        "source": "墙根网",
        "family_friendly": True
    },
    {
        "title": "成都海昌极地海洋公园冰淇淋狂欢节·16周年庆",
        "venue": "成都海昌极地海洋公园",
        "city": "chengdu",
        "start_date": "2026-07-04",
        "end_date": "2026-08-31",
        "link": "https://wlt.sc.gov.cn/scwlt/hydt/2026/7/9/dbd6f9e8cb144a03b6440084a968afb7.shtml",
        "description": "园区16周年庆活动，极地水乐园免费开放，每日两场泼水狂欢；乐奇冰雪乐园免票游玩；全天候演艺包括女侠飞人水飞秀、周年庆音乐节等；设奶龙及冰淇淋主题打卡点、冰淇淋DIY研学、凿冰寻宝等活动。",
        "fee": "收费（16重福利优惠）",
        "source": "四川省文化和旅游厅",
        "family_friendly": True
    },
    {
        "title": "成都海昌极地海洋公园夜宿海底研学营",
        "venue": "成都海昌极地海洋公园",
        "city": "chengdu",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://c.m.163.com/news/a/L1T14JCG0514OL9V.html",
        "description": "夜宿海底，和白鲸共度星光之夜。近距离邂逅白鲸、呆萌企鹅，跟着饲养员亲手投喂海洋小动物。海底隧道夜宿、浪漫星光晚宴、趣味科普实验一次打卡，伴着鱼群入眠。活动时间13:00-次日11:00。",
        "fee": "收费",
        "source": "天府发布",
        "family_friendly": True
    },
    {
        "title": "国色天乡水上乐园西瓜电音节",
        "venue": "国色天乡水上乐园",
        "city": "chengdu",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1051572320_498271/",
        "description": "森系玩水主题，14项水上设备一票通玩，含蒙太奇漩涡、极速太空舱、3米造浪池、漂流航道、大小水寨等。西瓜电音节包含国潮电音DJ、快闪舞蹈秀、肌肉猛男SHOW、非遗火舞等，1.2米以下儿童免费。",
        "fee": "收费（1.2米以下儿童免费）",
        "source": "成都本地宝",
        "family_friendly": True
    },
    {
        "title": "国色天乡陆地乐园三界仙游季",
        "venue": "国色天乡陆地乐园",
        "city": "chengdu",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1051572320_498271/",
        "description": "沉浸式仙侠主题活动，百位仙侠NPC全天互动，包含李逍遥、赵灵儿、哪吒、苏妲己等角色。仙门启幕、风华歌舞、仙韵演绎、奇术武韵等多元互动，飞花令、绕口令等游戏赢银票，30+游乐设备一票玩两天。",
        "fee": "收费（亲子套票129元）",
        "source": "成都本地宝",
        "family_friendly": True
    },
    # 景区公园类
    {
        "title": "熊猫基地·熊猫'宝藏'造纸奇遇记一日研学",
        "venue": "成都大熊猫繁育研究基地",
        "city": "chengdu",
        "start_date": "2026-07-09",
        "end_date": "2026-07-23",
        "link": "https://m.sohu.com/a/1046674421_121118742/",
        "description": "用熊猫竹纤维废料亲手造一张纸，探秘熊猫食竹奥秘，竹纤维废料变废为宝。手把手教学，体验完整手工造纸流程，沉浸式收获国宝知识。含专属通道入园、专属观光车、专业科普讲解。",
        "fee": "收费",
        "source": "成都大熊猫繁育研究基地",
        "family_friendly": True
    },
    {
        "title": "熊猫基地·滚滚的清凉一夏半日研学",
        "venue": "成都大熊猫繁育研究基地",
        "city": "chengdu",
        "start_date": "2026-07-11",
        "end_date": "2026-07-25",
        "link": "https://m.sohu.com/a/1046674421_121118742/",
        "description": "探秘大熊猫夏日防暑秘籍，破译国宝生存智慧，解锁夏日圈养保育知识。限定创意手工DIY，收获专属清凉扇。含官方研学证书、专属通道入园、专属观光车、专业科普讲解。",
        "fee": "收费",
        "source": "成都大熊猫繁育研究基地",
        "family_friendly": True
    },
    {
        "title": "熊猫基地·我做熊猫丰容设计师一日研学",
        "venue": "成都大熊猫繁育研究基地",
        "city": "chengdu",
        "start_date": "2026-07-16",
        "end_date": "2026-07-30",
        "link": "https://m.sohu.com/a/1046674421_121118742/",
        "description": "为大熊猫设计、打造专属家园，观察国宝日常生活，探究场馆建设，传递动物福利理念，解读动物丰容概念，亲手创作熊猫生态微景观家园。",
        "fee": "收费",
        "source": "成都大熊猫繁育研究基地",
        "family_friendly": True
    },
    {
        "title": "熊猫基地·滚滚的夏日半日研学（创意草帽）",
        "venue": "成都大熊猫繁育研究基地",
        "city": "chengdu",
        "start_date": "2026-07-18",
        "end_date": "2026-07-18",
        "link": "https://m.sohu.com/a/1046674421_121118742/",
        "description": "探秘大熊猫夏日防暑秘籍，解锁夏日圈养保育知识，限定创意手工DIY收获专属草帽，含官方研学证书。",
        "fee": "收费",
        "source": "成都大熊猫繁育研究基地",
        "family_friendly": True
    },
    {
        "title": "2026成都熊猫基地大熊猫生日丰容季",
        "venue": "成都大熊猫繁育研究基地",
        "city": "chengdu",
        "start_date": "2026-07-17",
        "end_date": "2026-07-31",
        "link": "https://m.weibo.cn/detail/5321592563042970",
        "description": "7月寿星萌宝和花、和叶、北辰、北侠、北香果等一众大熊猫过生日，线上直播庆生活动，云赴国宝生日现场。",
        "fee": "需购门票",
        "source": "成都大熊猫繁育研究基地微博",
        "family_friendly": True
    },
    {
        "title": "成都动物园'探秘神秘的两爬动物们'科普夏令营",
        "venue": "成都动物园",
        "city": "chengdu",
        "start_date": "2026-07-22",
        "end_date": "2026-07-22",
        "link": "https://m.sohu.com/a/1050877617_121118743/",
        "description": "专为6-10岁儿童设计的科普夏令营，苏卡达陆龟互动喂食洗澡、鬃狮蜥近距离触摸观察、趣味石膏手工创作，含动物园门票、营养午餐、马甲、手工材料费、活动证书等。20人成团。",
        "fee": "收费（240元/人）",
        "source": "成都动物园",
        "family_friendly": True
    },
    {
        "title": "成都动物园向日葵金色花海暑期限定",
        "venue": "成都动物园",
        "city": "chengdu",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1047419602_121118743/",
        "description": "从北大门到樱花林，伯特、高富帅、红宝石等七种向日葵盛放，高度0.6-1.8米，罕见红宝石向日葵是最大亮点。金红交织的向阳繁花与灵动可爱的动物相映成趣，暑假亲子打卡好去处。",
        "fee": "需购门票",
        "source": "成都动物园",
        "family_friendly": True
    },
    {
        "title": "成都动物园葵林小集",
        "venue": "成都动物园",
        "city": "chengdu",
        "start_date": "2026-07-10",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1048306345_121118743/",
        "description": "蒲葵林休闲区全新市集，紧邻狮虎苑，清凉树荫下一站式承包游园快乐：清爽特调饮品、动物园限定萌趣文创、精致小零食，开业抽奖大转盘100%中奖，趣味小丑互动巡游免费送动物造型气球。",
        "fee": "免费进入，消费自理",
        "source": "成都动物园",
        "family_friendly": True
    },
    {
        "title": "成都植物园'自然密语·五感探索'暑期实践课",
        "venue": "成都市植物园",
        "city": "chengdu",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7661944957808149034/",
        "description": "城市共享课堂美育天府主题，在植物园里开启五感自然探索之旅，观察感知风雨的树干'眼睛'、乘风飘散的飞行种子、可预报天气的神奇果荚，利用艾草、薄荷等天然驱蚊草本亲手制作专属驱蚊手环。",
        "fee": "收费",
        "source": "成都市教师共享中心",
        "family_friendly": True
    },
    # 金沙遗址博物馆类
    {
        "title": "金沙遗址博物馆'考古小达人'体验活动",
        "venue": "金沙遗址博物馆",
        "city": "chengdu",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.163.com/dy/article/KTMH0N9K0556M8VG.html",
        "description": "考古体验包包含用石膏浇铸太阳神鸟、用显微镜观察陶片等内容，孩子可以领考古任务卡，在展区找特定纹饰、拼陶片、记录修复步骤，集齐印章换小礼品，提前7天官方小程序预约。",
        "fee": "收费（78-88元/人含材料包）",
        "source": "孟鸿游游",
        "family_friendly": True
    },
    {
        "title": "金沙遗址博物馆文物修复体验",
        "venue": "金沙遗址博物馆",
        "city": "chengdu",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1041947548_122415890/",
        "description": "文物修复体验馆对公众开放预约，每天限量80人，可走进修复室隔着玻璃看修复师清理青铜器，现场互动装置模拟拼陶片，上午10点下午2点有演示。",
        "fee": "需购博物馆门票，体验需预约",
        "source": "秀秀向导",
        "family_friendly": True
    },
    {
        "title": "金沙遗址博物馆太阳神鸟二创作品征集活动",
        "venue": "金沙遗址博物馆",
        "city": "chengdu",
        "start_date": "2026-06-13",
        "end_date": "2026-07-20",
        "link": "https://www.jinshasitemuseum.com/seardetail/4771",
        "description": "面向全社会征集太阳神鸟主题的绘画、设计、非遗手作、短视频等多元形式原创作品，审核通过可获得'太阳神鸟守护者'电子证书，优秀作品有机会在'神鸟巡宇'线下文化共创展中展出。",
        "fee": "免费",
        "source": "金沙遗址博物馆官网",
        "family_friendly": True
    },
    # 科幻馆类
    {
        "title": "成都科幻馆'星云·巡航日志'暑期系列活动",
        "venue": "成都科幻馆",
        "city": "chengdu",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7528258493015474738/",
        "description": "以'星云·巡航日志'为主题，特色临展包括'超越想象·科幻与科技之旅'等7个主题展，公益活动包括飞行器奇遇记、机甲竞技比赛、3D建模打印等体验场景，'大咖讲科幻'主题讲座累计超600场。",
        "fee": "免费需预约",
        "source": "天府郫都",
        "family_friendly": True
    },
    {
        "title": "成都科幻馆'火星登陆计划'大型沉浸式科普展",
        "venue": "成都科幻馆",
        "city": "chengdu",
        "start_date": "2026-05-01",
        "end_date": "2026-08-31",
        "link": "https://www.pdrmtzx.com/2026/0529/165187.html",
        "description": "全新上线的大型沉浸式科普展，带孩子开启'落户'火星的奇妙旅程，VR设备沉浸式体验火星漫游，适合亲子家庭探索科幻世界。",
        "fee": "免费需预约",
        "source": "天府郫都",
        "family_friendly": True
    },
    {
        "title": "天宫阙·航天科学探索与艺术馆",
        "venue": "成都科幻馆",
        "city": "chengdu",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.tripvivid.com/47313.html",
        "description": "规划火箭、卫星、空间站、月球基地等18大航天主题场景，搭载VR/AR、数字全息等前沿技术，50%首发展项、70%互动体验项目，配套科学实验、手工实践、航天特色餐食等全流程服务。",
        "fee": "收费",
        "source": "执惠",
        "family_friendly": True
    },
    # 其他活动
    {
        "title": "'蓉光闪闪艺show天府'2026成都社区少儿艺术节",
        "venue": "成都高新区鹭州里街区（多区域）",
        "city": "chengdu",
        "start_date": "2026-07-18",
        "end_date": "2026-08-31",
        "link": "https://www.wccdaily.com.cn/wapepaper/html/20260717/249694.html",
        "description": "由华西社区报主办，为5至15岁热爱表演的少年儿童搭建舞台，以歌唱、舞蹈、朗诵等才艺为主要形式，设五场晋级赛和一场总决赛，专业评审+人气复活双轨晋级机制，免费报名参赛。",
        "fee": "免费报名",
        "source": "华西社区报",
        "family_friendly": True
    },
    {
        "title": "成都市教师共享中心2026暑期共享课程",
        "venue": "成都市内多个实景研学基地",
        "city": "chengdu",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7661944957808149034/",
        "description": "8大主题40堂课，覆盖运动、美育、科创、工匠、财商、荣光、志说、法治等多元成长维度，博物馆、科技馆、植物园、名师工作室等城市资源转化为实景研学基地，首期20堂课开放招募。",
        "fee": "收费",
        "source": "成都市教师共享中心",
        "family_friendly": True
    },
    {
        "title": "天府新区暑期16大精品研学营",
        "venue": "天府新区多个研学基地",
        "city": "chengdu",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://c.m.163.com/news/a/L1T14JCG0514OL9V.html",
        "description": "涵盖山野自然、前沿科创、非遗手工、美学艺术、职业体验六大板块，包括海洋治愈营、山野撒野营、硬核科创营、非遗手作营、广汇美术馆艺术营、科创动画双营等16大精品研学营。",
        "fee": "收费",
        "source": "天府发布",
        "family_friendly": True
    },
    {
        "title": "成都融创水世界'神仙玩水季'",
        "venue": "成都融创水世界",
        "city": "chengdu",
        "start_date": "2026-07-04",
        "end_date": "2026-08-31",
        "link": "https://wlt.sc.gov.cn/scwlt/hydt/2026/7/9/dbd6f9e8cb144a03b6440084a968afb7.shtml",
        "description": "造浪池化身'奇幻天宫'，众神NPC领衔电音派对，'齐天大圣'水上飞人表演、花式主题漂流、27个'瑶池仙汤'汤池同步开放，室内恒温水乐园不怕晒。",
        "fee": "收费",
        "source": "四川省文化和旅游厅",
        "family_friendly": True
    },
    {
        "title": "金沙国际音乐厅定格动画一日体验课",
        "venue": "金沙国际音乐厅",
        "city": "chengdu",
        "start_date": "2026-07-31",
        "end_date": "2026-07-31",
        "link": "https://m.df962388.com/yanchu/401911.html",
        "description": "'心迹漫游·节气访谈'主题定格动画一日体验课，适合亲子家庭参与，学习定格动画制作技巧。",
        "fee": "收费（390元）",
        "source": "东方演出网",
        "family_friendly": True
    },
    {
        "title": "儿童经典动漫音乐会《环游历险记》",
        "venue": "成都城市音乐厅",
        "city": "chengdu",
        "start_date": "2026-08-07",
        "end_date": "2026-08-08",
        "link": "https://www.xinruipiao.com/ertongqinzi/28738.html",
        "description": "用音符穿越动漫世界，原汁原味再现经典动画音乐，8月7日-8日多场演出，适合亲子家庭。",
        "fee": "收费（早鸟8折）",
        "source": "新锐票",
        "family_friendly": True
    }
]

# 去重 - 只添加标题不重复的活动
unique_new_activities = []
for activity in new_activities:
    if activity['title'] not in existing_titles:
        unique_new_activities.append(activity)
        existing_titles.add(activity['title'])

print(f"现有活动数量: {len(existing_activities)}")
print(f"新收集活动数量: {len(new_activities)}")
print(f"去重后新增活动数量: {len(unique_new_activities)}")
print(f"合并后总活动数量: {len(existing_activities) + len(unique_new_activities)}")

# 保存新增的活动到batch2文件
with open('/workspace/goout/output/raw/real_activities_chengdu_batch2.json', 'w', encoding='utf-8') as f:
    json.dump(unique_new_activities, f, ensure_ascii=False, indent=2)

print(f"\n新增活动已保存到 /workspace/goout/output/raw/real_activities_chengdu_batch2.json")

# 来源统计
sources = set(activity['source'] for activity in unique_new_activities)
print(f"\n新增活动来源列表（共{len(sources)}个）:")
for s in sorted(sources):
    print(f"  - {s}")

# 打印前10个代表性活动
print("\n新增代表性活动（10个）:")
for i, activity in enumerate(unique_new_activities[:10], 1):
    print(f"  {i}. {activity['title']}")
