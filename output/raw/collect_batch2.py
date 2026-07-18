import json
import os

existing_file = '/workspace/goout/output/raw/real_activities_shanghai.json'
output_file = '/workspace/goout/output/raw/real_activities_shanghai_batch2.json'

with open(existing_file, 'r', encoding='utf-8') as f:
    existing = json.load(f)

existing_titles = {item['title'] for item in existing}

new_activities = [
    {
        "title": "当世界杯遇见中美洲古代文明青少年工作坊",
        "venue": "上海博物馆人民广场馆观众活动中心",
        "city": "shanghai",
        "start_date": "2026-07-19",
        "end_date": "2026-07-22",
        "link": "http://m.toutiao.com/group/7663403809405714970/",
        "description": "从世界树之巅特展中的球赛石板、球员陶像等文物出发，带领青少年沿着一只橡胶球的旅程，串联中美地区不同文明的历史与文化。体验世界树·蛇形时间游戏图和古代中美球赛玩法互动游戏。面向10-18岁青少年。",
        "fee": "免费（需预约）",
        "source": "上海博物馆",
        "family_friendly": True
    },
    {
        "title": "珠归海上：庄万里家族捐赠两塗轩书画展（第二期）",
        "venue": "上海博物馆东馆二楼书画特型馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2027-01-31",
        "link": "https://www.shanghaimuseum.net/mu/frontend/pg/m/article/id/I00004987",
        "description": "以书画史为线索，精选22件庄万里家族捐赠的书画精品，呈现传统书画艺术的璀璨魅力。包括明代谢时臣《溪山岁晚图轴》、晚明张瑞图《行书庾子山步虚词卷》、清代李因《芦雁图轴》等珍品。",
        "fee": "免费（需预约）",
        "source": "上海博物馆",
        "family_friendly": True
    },
    {
        "title": "暂得之乐：暂得楼捐赠明清瓷器展",
        "venue": "上海博物馆人民广场馆四楼第三展厅",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2027-10-31",
        "link": "https://www.shanghaimuseum.net/mu/frontend/pg/m/article/id/I00004987",
        "description": "精选香港著名收藏家胡惠春先生暂得楼旧藏明清陶瓷珍品，涵盖官窑名品与艺术佳作，包括景德镇窑粉彩云龙纹转心瓶等珍贵文物。",
        "fee": "收费（特展票）",
        "source": "上海博物馆",
        "family_friendly": True
    },
    {
        "title": "奇骥奔腾马年特展暑期互动活动",
        "venue": "上海科技馆",
        "city": "shanghai",
        "start_date": "2026-06-23",
        "end_date": "2026-08-30",
        "link": "http://news.qq.com/rain/a/20260623A086VI00",
        "description": "暑期隐藏玩法包括：马上有福100%有奖互动、谁是千里马科学问答NPC互动、模拟骑马体验、马成语PK、马主题蒲扇拓印等。每天30组家庭有机会解锁相对论剧场特别体验。",
        "fee": "收费（特展票）",
        "source": "上海科技馆",
        "family_friendly": True
    },
    {
        "title": "明日科创营STEM奇妙日",
        "venue": "上海科技馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7656039120107586063/",
        "description": "像科学家一样提问，像工程师一样解决问题。从真实情境出发，观察、提问、假设、验证，用跨学科视角解决没有标准答案的问题。建议四年级及以上，每课时50元。",
        "fee": "收费（每课时50元）",
        "source": "上海科技馆",
        "family_friendly": True
    },
    {
        "title": "明日科创营创客进化论",
        "venue": "上海科技馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7656039120107586063/",
        "description": "用双手把脑中的想法变成真实作品。从螺丝刀到3D打印机，从电路板到激光切割机，打造会动的装置、智能小工具或创意发明。建议一年级及以上。",
        "fee": "收费（每课时50元）",
        "source": "上海科技馆",
        "family_friendly": True
    },
    {
        "title": "科学怪咖沉浸式VR数字剧场",
        "venue": "上海科技馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7655278783741592079/",
        "description": "特斯拉VS爱迪生谁才是真正的光电之神？当电流火花擦过耳边、当百年实验室在眼前重构，一起化身历史见证者。沉浸式VR数字剧场体验。",
        "fee": "收费（需购票）",
        "source": "上海科技馆",
        "family_friendly": True
    },
    {
        "title": "星耀东方：青浦考古与长三角文明探源展",
        "venue": "青浦博物馆",
        "city": "shanghai",
        "start_date": "2026-05-18",
        "end_date": "2026-09-13",
        "link": "http://m.sh.bendibao.com/tour/307720.html",
        "description": "系统梳理青浦考古半个世纪成果，联动长三角9家博物馆，汇聚马家浜、崧泽、良渚至广富林文化的史前文物精品。以苏秉琦先生满天星斗文明观为精神内核，呈现长三角地区数千年文化共同体形成历程。",
        "fee": "免费",
        "source": "上海本地宝",
        "family_friendly": True
    },
    {
        "title": "熔光凝形——铸造玻璃的艺术叙事展",
        "venue": "上海琉璃艺术博物馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7657529437793944099/",
        "description": "上海琉璃艺术博物馆暑期特展，7月18日、8月1日、8月15日开放夜游至20:00。呈现铸造玻璃的艺术叙事，探索玻璃艺术的独特魅力。",
        "fee": "收费",
        "source": "上海市文化和旅游局",
        "family_friendly": True
    },
    {
        "title": "墨海楼藏近代名人墨展",
        "venue": "上海周虎臣曹素功笔墨博物馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7657529437793944099/",
        "description": "展出近代名人墨藏品，配合《近代名人墨知识》讲座、墨锭鉴赏交流活动。7月10日讲座，8月14日鉴赏交流，8月28日夜间开放至20:00。",
        "fee": "免费",
        "source": "上海市文化和旅游局",
        "family_friendly": True
    },
    {
        "title": "Moin·侬好——纪念上海-汉堡缔结友好城市关系40周年展",
        "venue": "上海市历史博物馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7657529437793944099/",
        "description": "上海与汉堡友好城市40周年纪念特展，呈现两座城市的文化交流历史与友好城市发展历程。",
        "fee": "免费（需预约）",
        "source": "上海市历史博物馆",
        "family_friendly": True
    },
    {
        "title": "传与承——哈萨克斯坦民俗文化展",
        "venue": "上海市历史博物馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7657529437793944099/",
        "description": "展示哈萨克斯坦传统民俗文化，包括服饰、手工艺、音乐舞蹈等多元文化内容，促进中哈文化交流。",
        "fee": "免费（需预约）",
        "source": "上海市历史博物馆",
        "family_friendly": True
    },
    {
        "title": "苏州河水上亲子研读航班",
        "venue": "悠游苏州河游船（昌化路码头）",
        "city": "shanghai",
        "start_date": "2026-07-18",
        "end_date": "2026-08-22",
        "link": "https://m.sohu.com/a/1047434197_121106854/",
        "description": "苏州河上首个面向亲子家庭的水上流动图书馆，联动上海图书馆。暑假限定4场：亲子绘本场（非遗之美金龙船绘本）7月18日、8月15日；国学润童心场（论语水的智慧）7月25日、8月22日。含专属绘本/课件、文创礼品、亲子讲解。",
        "fee": "收费（278元/组，1大1小）",
        "source": "悠游苏州河×上海图书馆",
        "family_friendly": True
    },
    {
        "title": "2026上海童话·暑期少儿阅读季",
        "venue": "上海少年儿童图书馆及全市252个阅读新空间",
        "city": "shanghai",
        "start_date": "2026-07-04",
        "end_date": "2026-09-30",
        "link": "https://m.sohu.com/a/1046506558_121106832/",
        "description": "第十四届上海童话节全新升级，以阅·万象为主题，七大板块1000余项阅读活动。包括主题活动、故事剧场、少儿讲座、创艺工坊、展览展示、志愿活动等。全公益零门槛，全市252个儿童友好城市阅读新空间联动。",
        "fee": "免费",
        "source": "上海少年儿童图书馆",
        "family_friendly": True
    },
    {
        "title": "书房中的文艺复兴——西方抄写印刷与装帧艺术特展",
        "venue": "上海图书馆东馆一楼一号展厅",
        "city": "shanghai",
        "start_date": "2026-06-27",
        "end_date": "2026-10-11",
        "link": "https://m.thepaper.cn/newsDetail_forward_33502534",
        "description": "中国大陆首个以书籍为核心的文艺复兴主题大展。涵盖古希腊、古罗马以及文艺复兴时期的人文主义经典，多个领域与珍贵书籍相互映照，构筑一间文艺复兴书房。",
        "fee": "收费（单人票60元，双人票115元）",
        "source": "上海图书馆东馆",
        "family_friendly": True
    },
    {
        "title": "大英图书馆·奇喵史展览",
        "venue": "上海图书馆东馆一楼2号展厅",
        "city": "shanghai",
        "start_date": "2026-06-27",
        "end_date": "2026-10-18",
        "link": "https://m.thepaper.cn/newsDetail_forward_33502534",
        "description": "治愈人心的喵喵展。溯源现代家猫的祖先非洲野猫，讲述猫与人类文明的故事。包含四屏动画电影讲埃及猫文化、黑死病与猫的历史、真实猫展品、互动游戏、宋代猫嫁仪式体验等。",
        "fee": "收费（30-60元/人）",
        "source": "上海图书馆东馆",
        "family_friendly": True
    },
    {
        "title": "皮影戏《大闹天宫》",
        "venue": "上海保利大剧院小剧场",
        "city": "shanghai",
        "start_date": "2026-07-12",
        "end_date": "2026-07-12",
        "link": "http://www.jiading.gov.cn/mspd/shgj/content_969975",
        "description": "百年剧团马氏皮影呈现的经典神话皮影戏。孙悟空挑战权威、追求自由，用光与影的交织将神话再现于舞台。约70分钟，适合亲子观看。",
        "fee": "收费（180-380元）",
        "source": "上海保利大剧院",
        "family_friendly": True
    },
    {
        "title": "芭蕾舞剧《爱丽丝梦游仙境》",
        "venue": "上海保利大剧院大剧场",
        "city": "shanghai",
        "start_date": "2026-07-12",
        "end_date": "2026-07-12",
        "link": "http://www.jiading.gov.cn/mspd/shgj/content_969975",
        "description": "150年全球顶流童话×正统俄式芭蕾。俄罗斯国家芭蕾舞团前首席德洛兹洛娃·娜杰塔亲自编舞执导，演绎极致唯美的亲子艺术大餐。约80分钟。",
        "fee": "收费（80-200元）",
        "source": "上海保利大剧院",
        "family_friendly": True
    },
    {
        "title": "儿童剧《哪吒大战红孩儿》",
        "venue": "上海保利大剧院大剧场",
        "city": "shanghai",
        "start_date": "2026-07-24",
        "end_date": "2026-07-24",
        "link": "http://www.jiading.gov.cn/mspd/shgj/content_969975",
        "description": "取经路上另起波澜，红孩儿假扮哪吒四处捣乱，哪吒下凡与红孩儿展开激烈对决。在众人帮助下红孩儿最终明白了交朋友的真谛。约70分钟。",
        "fee": "收费（80-200元）",
        "source": "上海保利大剧院",
        "family_friendly": True
    },
    {
        "title": "原创科学冒险舞台剧《哈小浪奇遇记之恐龙岛大冒险》",
        "venue": "上海保利大剧院大剧场",
        "city": "shanghai",
        "start_date": "2026-07-25",
        "end_date": "2026-07-25",
        "link": "http://www.jiading.gov.cn/mspd/shgj/content_969975",
        "description": "超3000万人喜欢的热门IP哈小浪首套正版授权舞台剧，改编自超亿播放人气音频故事。一场穿越时空的恐龙岛大冒险，一次寓教于乐的科学探索之旅。约70分钟。",
        "fee": "收费（80-200元）",
        "source": "上海保利大剧院",
        "family_friendly": True
    },
    {
        "title": "互动亲子剧《大卫，不可以！》",
        "venue": "上海保利大剧院大剧场",
        "city": "shanghai",
        "start_date": "2026-08-01",
        "end_date": "2026-08-01",
        "link": "http://www.jiading.gov.cn/mspd/shgj/content_969975",
        "description": "经典绘本改编的互动亲子剧，戳中亲子之间的笑点、痛点及泪点。讲述妈妈为什么发脾气，生活的细节，情商的培养，亲子关系的相爱相杀。约70分钟。",
        "fee": "收费（80-200元）",
        "source": "上海保利大剧院",
        "family_friendly": True
    },
    {
        "title": "木偶腹语儿童剧《小猩猩的大圣梦》",
        "venue": "浦东新区金海文化艺术中心影剧院",
        "city": "shanghai",
        "start_date": "2026-07-18",
        "end_date": "2026-07-18",
        "link": "http://m.toutiao.com/group/7663377358283424271/",
        "description": "小猩猩团团一心崇拜齐天大圣，疯狂模仿却频频闹笑话，最终放下模仿他人，发现自己独有的变水果本领。结合提线木偶、手偶腹语、面具等元素，传递不必成为别人、做真实自己的哲理。",
        "fee": "免费（需领票）",
        "source": "浦东新区金海文化艺术中心",
        "family_friendly": True
    },
    {
        "title": "大型神话木偶剧《孙悟空三打白骨精》",
        "venue": "九棵树（上海）未来艺术中心水岸舞台",
        "city": "shanghai",
        "start_date": "2026-07-21",
        "end_date": "2026-07-21",
        "link": "http://m.toutiao.com/group/7663310983120568847/",
        "description": "大量特技木偶表演，连演40余年经久不衰。角色众多造型丰富，带孩子走进经典神话故事，共度温馨欢乐的夏夜亲子时光。奉贤区相约滨海之夏广场文化系列活动。",
        "fee": "免费（公益演出）",
        "source": "奉贤区文化馆",
        "family_friendly": True
    },
    {
        "title": "原创音乐剧《寻找声音的耳朵》",
        "venue": "上海大剧院中剧场",
        "city": "shanghai",
        "start_date": "2026-07-10",
        "end_date": "2026-07-12",
        "link": "https://www.shgtheatre.com/shtheatre/#/ticket/detail/22507",
        "description": "儿童原创音乐剧，讲述关于童真与成长的故事，约120分钟。适合亲子家庭观看的优质儿童剧作品。",
        "fee": "收费（100-480元）",
        "source": "上海大剧院",
        "family_friendly": True
    },
    {
        "title": "塑我此生：贾科梅蒂艺术大展",
        "venue": "上海民生现代美术馆",
        "city": "shanghai",
        "start_date": "2026-07-17",
        "end_date": "2026-12-06",
        "link": "http://m.toutiao.com/group/7662557965647348258/",
        "description": "贾科梅蒂基金会212件藏品与档案资料，13个叙事单元，涵盖雕塑、绘画、素描、版画和手稿。从标志性的瘦长人物，到艺术家完整创作周期，呈现贾科梅蒂的艺术世界。",
        "fee": "收费",
        "source": "上海民生现代美术馆",
        "family_friendly": True
    },
    {
        "title": "玻璃应力：流动的威尼斯狂欢展",
        "venue": "上海久事美术馆",
        "city": "shanghai",
        "start_date": "2026-07-18",
        "end_date": "2026-10-31",
        "link": "http://m.toutiao.com/group/7662557965647348258/",
        "description": "穆拉诺玻璃传统带到上海外滩。19个国家52位艺术家60件作品，以威尼斯狂欢节为叙事线索，探索玻璃作为当代艺术材料的力量。",
        "fee": "收费",
        "source": "上海久事美术馆",
        "family_friendly": True
    },
    {
        "title": "陈世英双城展《他界之器》",
        "venue": "龙美术馆（西岸馆）",
        "city": "shanghai",
        "start_date": "2026-07-18",
        "end_date": "2026-10-25",
        "link": "https://m.thepaper.cn/newsDetail_forward_33502534",
        "description": "著名华人艺术家陈世英的钛金属雕塑艺术展。将工业材料转化为超凡的艺术形式，兼具精密技术与丰富象征意蕴。作品灵感源自天主教祝福仪式圣油，通过黄红蓝微妙色变唤起诞生成长与重生的循环。",
        "fee": "收费（全馆通票200元）",
        "source": "龙美术馆西岸馆",
        "family_friendly": True
    },
    {
        "title": "CHINA白——德化白瓷艺术展",
        "venue": "上海世界技能博物馆",
        "city": "shanghai",
        "start_date": "2026-07-16",
        "end_date": "2026-10-31",
        "link": "http://m.toutiao.com/group/7662557965647348258/",
        "description": "汇集数十位中国工艺美术大师、全国技术能手等业界领军人物的100余件白瓷艺术瑰宝。涉及镂雕、浮雕、彩绘等传统装饰技艺，也包括烧制工艺、当代设计与技能创新。",
        "fee": "收费",
        "source": "上海世界技能博物馆",
        "family_friendly": True
    },
    {
        "title": "今日蒙古——蒙古当代艺术邀请展",
        "venue": "海派艺术馆",
        "city": "shanghai",
        "start_date": "2026-07-10",
        "end_date": "2026-08-06",
        "link": "http://m.toutiao.com/group/7663063656262861366/",
        "description": "集结61位蒙古国艺术家，80余组作品，油画、青铜雕塑、毛毡装置、数字艺术多元呈现。打破草原绘画固有印象，游牧文明与当代先锋创作碰撞对话。",
        "fee": "免费（需预约）",
        "source": "海派艺术馆",
        "family_friendly": True
    },
    {
        "title": "花园·星星·小径：新锐青年艺术家原创作品展",
        "venue": "上海宝龙美术馆",
        "city": "shanghai",
        "start_date": "2026-06-30",
        "end_date": "2026-10-11",
        "link": "http://m.toutiao.com/group/7663063656262861366/",
        "description": "三十位新锐艺术家的插画、潮玩雕塑错落陈列，马卡龙色系展厅，圆洞拱门造景氛围感十足。设置互动绘画区，孩子可动手创作并将作品带回家。",
        "fee": "收费（双展联票88元）",
        "source": "上海宝龙美术馆",
        "family_friendly": True
    },
    {
        "title": "上海自然博物馆探索中心小小博物家",
        "venue": "上海自然博物馆B2探索中心一树一世界",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.snhm.org.cn/cgfw/cxyy.htm",
        "description": "在充满自然气息的一树一世界主题教室，模拟重现科学研究的探索过程。从羽众不同、有趣的毛皮等11个主题包中选择，通过博物馆笔记、配套工具仔细观察自然标本，动手操作记录总结，完成自主探究。60分钟。",
        "fee": "免费（需预约，含博物馆门票）",
        "source": "上海自然博物馆",
        "family_friendly": True
    },
    {
        "title": "上海自然博物馆昆虫世界的伪装大师",
        "venue": "上海自然博物馆B2探索中心主题教室2",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.snhm.org.cn/cgfw/cxyy.htm",
        "description": "保护色和拟态是昆虫伪装术的重要内容。通过互动游戏、案例分析、头脑风暴和手工制作等环节逐步掌握保护色和拟态的概念与作用，思考人类如何从昆虫伪装术中获得灵感。45分钟。",
        "fee": "免费（需预约，含博物馆门票）",
        "source": "上海自然博物馆",
        "family_friendly": True
    },
    {
        "title": "上美影泡泡米·国漫美育成长季",
        "venue": "上美影泡泡米益智乐园（上海环球港）",
        "city": "shanghai",
        "start_date": "2026-07-08",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7658285811556696585/",
        "description": "以上美影经典动画IP为核心，开设国漫手作、西游研学、光影剧场、非遗美育课堂，沉浸式感受东方美学。可购暑期联票、亲子套票，通过泡泡米小程序预约参与。",
        "fee": "收费（购票入园）",
        "source": "上海市文化和旅游局",
        "family_friendly": True
    },
    {
        "title": "感受篆刻的魅力暑期体验活动",
        "venue": "虹口区梧州路312号三楼篆刻室",
        "city": "shanghai",
        "start_date": "2026-07-05",
        "end_date": "2026-07-05",
        "link": "https://www.shhk.gov.cn/hkjy_nas/76bbdf5b-d8ad-4dc7-b55c-da7f90e94bbd/2810c5f6-909c-4d76-9266-010c9c3166e4/%E3%80%90%E7%AC%AC%E4%BA%8C%E6%89%B9%E3%80%912026%E5%B9%B4%E8%99%B9%E5%8F%A3%E5%8C%BA%E6%9C%AA%E6%88%90%E5%B9%B4%E4%BA%BA%E6%9A%91%E6%9C%9F%E6%B4%BB%E5%8A%A8%E9%A1%B9%E7%9B%AE.pdf",
        "description": "了解篆刻基本常识，学习印章设计中的章法规律，以姓名章为主题，运用小刀郎模拟篆刻软件刻制一方二字、三字或四字印章。面向三-五年级学生，限额18人。",
        "fee": "免费",
        "source": "虹口区未成年人暑期活动",
        "family_friendly": True
    },
    {
        "title": "国家级非遗项目——海派面塑体验",
        "venue": "上海市北郊学校非遗馆（大连西路205号）",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-07-01",
        "link": "https://www.shhk.gov.cn/hkjy_nas/76bbdf5b-d8ad-4dc7-b55c-da7f90e94bbd/2810c5f6-909c-4d76-9266-010c9c3166e4/%E3%80%90%E7%AC%AC%E4%BA%8C%E6%89%B9%E3%80%912026%E5%B9%B4%E8%99%B9%E5%8F%A3%E5%8C%BA%E6%9C%AA%E6%88%90%E5%B9%B4%E4%BA%BA%E6%9A%91%E6%9C%9F%E6%B4%BB%E5%8A%A8%E9%A1%B9%E7%9B%AE.pdf",
        "description": "依托国家级非遗项目海派面塑，指导学生学习和运用面塑技能，创作符合时代精神的作品。面向欧阳社区未成年人。",
        "fee": "免费",
        "source": "虹口区未成年人暑期活动",
        "family_friendly": True
    },
    {
        "title": "公益英语音乐剧夏令营（冰雪奇缘主题）",
        "venue": "嘉兴路街道新时代文明实践分中心（瑞虹路400号）",
        "city": "shanghai",
        "start_date": "2026-08-26",
        "end_date": "2026-08-28",
        "link": "https://www.shhk.gov.cn/hkjy_nas/76bbdf5b-d8ad-4dc7-b55c-da7f90e94bbd/2810c5f6-909c-4d76-9266-010c9c3166e4/%E3%80%90%E7%AC%AC%E4%BA%8C%E6%89%B9%E3%80%912026%E5%B9%B4%E8%99%B9%E5%8F%A3%E5%8C%BA%E6%9C%AA%E6%88%90%E5%B9%B4%E4%BA%BA%E6%9A%91%E6%9C%9F%E6%B4%BB%E5%8A%A8%E9%A1%B9%E7%9B%AE.pdf",
        "description": "嘉兴路街道开设的公益英文音乐剧夏令营，以冰雪奇缘为主题，传递勇气、成长与温暖情谊。零基础亦可参与。面向辖区未成年人。",
        "fee": "免费",
        "source": "虹口区嘉兴路街道",
        "family_friendly": True
    },
    {
        "title": "上海碳秘馆参观体验活动",
        "venue": "上海碳秘馆（大连路1409号）",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.shhk.gov.cn/hkjy_nas/76bbdf5b-d8ad-4dc7-b55c-da7f90e94bbd/2810c5f6-909c-4d76-9266-010c9c3166e4/%E3%80%90%E7%AC%AC%E4%BA%8C%E6%89%B9%E3%80%912026%E5%B9%B4%E8%99%B9%E5%8F%A3%E5%8C%BA%E6%9C%AA%E6%88%90%E5%B9%B4%E4%BA%BA%E6%9A%91%E6%9C%9F%E6%B4%BB%E5%8A%A8%E9%A1%B9%E7%9B%AE.pdf",
        "description": "带领大家走进碳普惠的世界，系统呈现碳普惠理念在本市的生动实践，帮助真切理解其价值内涵，引导形成绿色低碳生产生活方式。面向全体青少年。",
        "fee": "免费（散客无需预约）",
        "source": "上海碳秘馆",
        "family_friendly": True
    },
    {
        "title": "莫兰迪工作坊——肌理拼色袋",
        "venue": "浦东美术馆",
        "city": "shanghai",
        "start_date": "2026-07-22",
        "end_date": "2026-07-27",
        "link": "http://m.toutiao.com/group/7660191712152699407/",
        "description": "在手袋上以柔色皮料拼贴出陆家嘴天际线的轮廓，制作兼具设计感与实用性的原创手袋。体验莫兰迪色系的层次变化。",
        "fee": "收费（需购买美术馆门票）",
        "source": "浦东美术馆",
        "family_friendly": True
    },
    {
        "title": "莫兰迪工作坊——布艺小花器",
        "venue": "浦东美术馆",
        "city": "shanghai",
        "start_date": "2026-07-18",
        "end_date": "2026-07-18",
        "link": "http://m.toutiao.com/group/7660191712152699407/",
        "description": "用低饱和不织布塑造花朵与花器造型，粘合组装成永不凋谢的案头小景。体验莫兰迪低饱和色彩的美学。",
        "fee": "收费（需购买美术馆门票）",
        "source": "浦东美术馆",
        "family_friendly": True
    },
    {
        "title": "少图奇妙夜——阅享八五载，少图伴成长",
        "venue": "上海少年儿童图书馆（长风馆）",
        "city": "shanghai",
        "start_date": "2026-07-19",
        "end_date": "2026-07-19",
        "link": "https://m.sohu.com/a/1051137736_121106832/",
        "description": "上海少年儿童图书馆85周年馆庆特别夜间活动，面向400组亲子家庭。包括吉祥物蜜宝合影、书香游戏打卡集章、馆藏AI时光机、童年档案馆共读录制、蜜宝光影秀、天空画板。彩蛋活动有绘本《图书馆奇妙夜》首发、墨舞「兰亭」艺术赏析。集章兑换神秘礼物。",
        "fee": "免费（需预约）",
        "source": "上海少年儿童图书馆",
        "family_friendly": True
    },
    {
        "title": "探秘夜森林之湿地奇遇记",
        "venue": "共青森林公园",
        "city": "shanghai",
        "start_date": "2026-07-14",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7662329186924659227/",
        "description": "城市原生阔叶林夜游科普活动，寻找黄脉翅萤、锹甲、刺猬、金线蛙等夜间生物。配套鲁米诺荧光实验、原生水生生态缸展示、六角恐龙科普，兼顾野外观察与室内趣味科学实验。适合喜欢森林深度探索的亲子家庭。",
        "fee": "收费",
        "source": "共青森林公园",
        "family_friendly": True
    }
]

# 去重
unique_new = []
for activity in new_activities:
    if activity['title'] not in existing_titles:
        unique_new.append(activity)
        existing_titles.add(activity['title'])

print(f"现有活动: {len(existing)}")
print(f"新发现活动: {len(new_activities)}")
print(f"去重后新增: {len(unique_new)}")
print(f"总计: {len(existing) + len(unique_new)}")

# 保存新增的活动
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(unique_new, f, ensure_ascii=False, indent=2)

print(f"\n已保存到 {output_file}")

# 打印代表性活动名称
print("\n代表性新增活动（10个）：")
for i, activity in enumerate(unique_new[:10]):
    print(f"{i+1}. {activity['title']}")

# 打印来源列表
sources = set()
for activity in unique_new:
    sources.add(activity['source'])
print(f"\n来源列表（共{len(sources)}个）：")
for s in sorted(sources):
    print(f"- {s}")
