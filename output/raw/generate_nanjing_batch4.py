import json
import os

existing_titles = set()
for f in ['real_activities_nanjing.json', 'real_activities_nanjing_batch2.json', 'real_activities_nanjing_batch3.json']:
    path = os.path.join(os.path.dirname(__file__), f)
    if os.path.exists(path):
        with open(path, 'r') as fp:
            data = json.load(fp)
            for item in data:
                existing_titles.add(item['title'])

print(f"现有活动标题数: {len(existing_titles)}")

activities = []

# ============ 1. 各区县暑期活动 ============

# 玄武区
activities.append({
    "title": "玄武湖观鸟小队暑期研学活动",
    "venue": "玄武湖景区情侣园",
    "city": "nanjing",
    "start_date": "2026-07-19",
    "end_date": "2026-07-25",
    "link": "https://www.yzwb.net/news/jiangsu/nanjing/202607/t20260715_372486.html",
    "description": "专业导师带队沿湖巡览，追寻池鹭、绿鹭、黄苇鳽等夏候鸟灵动身影，透过望远镜观察水鸟栖息繁衍的湖畔生态，适合喜爱自然的亲子家庭参与。",
    "fee": "免费需预约",
    "source": "紫牛新闻",
    "family_friendly": True
})

activities.append({
    "title": "明城墙博物一日营",
    "venue": "明城墙玄武湖段",
    "city": "nanjing",
    "start_date": "2026-07-15",
    "end_date": "2026-08-30",
    "link": "https://www.yzwb.net/news/jiangsu/nanjing/202607/t20260715_372486.html",
    "description": "研学少年漫步城墙根下，辨识城垣原生草木、深挖明城墙营建文史，亲手体验植物拓印技艺，将湖山草木与千年城史定格在手作之中。",
    "fee": "198元/人",
    "source": "紫牛新闻",
    "family_friendly": True
})

activities.append({
    "title": "玄武湖红领巾讲解员体验活动",
    "venue": "玄武湖景区玄武门、梁洲友谊厅",
    "city": "nanjing",
    "start_date": "2026-07-19",
    "end_date": "2026-07-26",
    "link": "https://www.yzwb.net/news/jiangsu/nanjing/202607/t20260715_372486.html",
    "description": "面向少年儿童开放的文化讲解体验活动，孩子们化身文化小使者，驻守玄武门、梁洲友谊厅、后湖黄册库遗址，自信讲述金陵湖城文脉。",
    "fee": "免费需报名",
    "source": "紫牛新闻",
    "family_friendly": True
})

activities.append({
    "title": "《玄武有灵》沉浸式数字剧本解谜",
    "venue": "玄武湖景区五洲堤岸",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.yzwb.net/news/jiangsu/nanjing/202607/t20260715_372486.html",
    "description": "景区上线沉浸式数字剧本，使用手机扫码变身文化小侦探，在五洲堤岸开启虚实交融的解谜冒险，古今故事在湖光之间奇妙碰撞。",
    "fee": "免费",
    "source": "紫牛新闻",
    "family_friendly": True
})

# 建邺区
activities.append({
    "title": "建邺区国风润心书香启智暑期文化阅读营第一期",
    "venue": "建邺区图书馆三楼建邺书房",
    "city": "nanjing",
    "start_date": "2026-07-14",
    "end_date": "2026-07-16",
    "link": "https://www.njjy.gov.cn/jyyw/202607/t20260709_5874005.html",
    "description": "面向6-12周岁少儿亲子家庭的公益夏令营，融合书香国风、自然科普、趣味实践，每场30组家庭参与，在阅读与手工中度过充实夏日。",
    "fee": "公益免费",
    "source": "建邺区人民政府",
    "family_friendly": True
})

activities.append({
    "title": "建邺区国风润心书香启智暑期文化阅读营第二期",
    "venue": "建邺区图书馆三楼建邺书房",
    "city": "nanjing",
    "start_date": "2026-07-27",
    "end_date": "2026-07-31",
    "link": "https://www.njjy.gov.cn/jyyw/202607/t20260709_5874005.html",
    "description": "为期5天的青少年暑期文化阅读营，面向6-12周岁少儿亲子家庭，30组家庭参与，内容涵盖国风文化、阅读分享、手工创作等多元体验。",
    "fee": "公益免费",
    "source": "建邺区人民政府",
    "family_friendly": True
})

activities.append({
    "title": "建邺高新区四点半课堂暑托班",
    "venue": "金陵河西学校",
    "city": "nanjing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-31",
    "link": "http://www.njdaily.cn/news/2026/0716/8480558748823161574.html",
    "description": "江苏省唯一入选教育部地方典型案例的暑期托管项目，近300名建邺区一至五年级儿童分两期入托，服务时段从早8:30至晚6点，九大特色课程体系。",
    "fee": "公益免费",
    "source": "南京日报",
    "family_friendly": True
})

# 秦淮区
activities.append({
    "title": "2026朝天宫读城品夏龙虾美食嘉年华",
    "venue": "熙南里奥灶馆门口广场",
    "city": "nanjing",
    "start_date": "2026-07-18",
    "end_date": "2026-07-19",
    "link": "http://m.toutiao.com/group/7663467543570481705/",
    "description": "集结20+家朝天宫小店，划分为红盔甲、金陵鸭韵、守味人、微醺时光、集章探城五大战队，涵盖龙虾、卤味、点心、非遗文创多元业态，老少皆宜。",
    "fee": "免费入场",
    "source": "美丽朝天宫",
    "family_friendly": True
})

activities.append({
    "title": "熙南里第六届不止有咖啡集",
    "venue": "熙南里街区",
    "city": "nanjing",
    "start_date": "2026-07-18",
    "end_date": "2026-07-19",
    "link": "http://m.toutiao.com/group/7663467543570481705/",
    "description": "多家特色咖啡好店齐聚熙南里青砖巷弄，从本土情怀满满的口碑好牌到脑洞十足的创意特调，设置咖啡主题特色打卡点，参与打卡集章挑战赢取福利。",
    "fee": "免费入场",
    "source": "熙南里街区",
    "family_friendly": True
})

# 江宁区
activities.append({
    "title": "江宁区非遗传承主题两天一夜研学营",
    "venue": "牛首山、汤山直立人化石遗址博物馆",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663510578668831286/",
    "description": "针对7至16周岁青少年推出的研学精品线路，在牛首山体验金陵金箔、敦煌壁画等传统技艺，在汤山直立人化石遗址博物馆探究远古地质与人类起源。",
    "fee": "680元/人",
    "source": "人民网",
    "family_friendly": True
})

activities.append({
    "title": "江宁区科技科普主题两天一夜研学营",
    "venue": "南航研究院、江宁开发区",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663510578668831286/",
    "description": "在南航研究院动手组装航空模型，深入航空航天科技前沿，了解航空工程基础知识，培养孩子的科学兴趣与动手实践能力。",
    "fee": "720元/人",
    "source": "人民网",
    "family_friendly": True
})

activities.append({
    "title": "江宁甜美瓜乡烽火横山红色研学营",
    "venue": "江宁横溪街道",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663510578668831286/",
    "description": "融合安全与红色教育的研学线路，在横山抗日根据地重温革命历史，体验田园采摘与乡村生活，培养孩子的爱国主义情怀与实践能力。",
    "fee": "580元/人",
    "source": "人民网",
    "family_friendly": True
})

activities.append({
    "title": "江宁秦淮源头文化湖熟研学营",
    "venue": "江宁湖熟街道",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663510578668831286/",
    "description": "聚焦传统文化的研学线路，探访湖熟文化遗址，了解4000年湖熟文化历史，体验传统手工艺，感受秦淮源头深厚的文化底蕴。",
    "fee": "498元/人",
    "source": "人民网",
    "family_friendly": True
})

activities.append({
    "title": "龙乡双范泡泡音乐溯溪派对",
    "venue": "江宁龙乡双范溪流营地",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663510578668831286/",
    "description": "依托200余亩自然水域打造的浅水溯溪道、桨板码头，一站式集齐露营、餐饮、休闲，泡泡派对与音乐演出轮番登场，亲子戏水消暑首选。",
    "fee": "门票88元/人",
    "source": "人民网",
    "family_friendly": True
})

activities.append({
    "title": "谷里森林童趣一日游",
    "venue": "江宁谷里街道",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663510578668831286/",
    "description": "体验萌宠互动、果蔬采摘、草坪露营、音乐轰趴等特色项目，在森林氧吧中享受亲子时光，适合全家周末出游。",
    "fee": "168元/人",
    "source": "人民网",
    "family_friendly": True
})

activities.append({
    "title": "百家湖国际啤酒节",
    "venue": "江宁百家湖商圈",
    "city": "nanjing",
    "start_date": "2026-07-17",
    "end_date": "2026-07-19",
    "link": "http://m.toutiao.com/group/7663510578668831286/",
    "description": "连嗨三天的盛夏狂欢派对，嗑瓜子大赛、乐队演出等活动轮番登场，多家餐饮品牌齐聚，适合全家逛吃消暑。",
    "fee": "免费入场",
    "source": "人民网",
    "family_friendly": True
})

# 栖霞区
activities.append({
    "title": "栖霞山自由研学季",
    "venue": "栖霞山风景区",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://nyncj.nanjing.gov.cn/nygzdt/202607/t20260709_5873698.html",
    "description": "三条自主探索线路供亲子家庭自由选择，萌宠乐园可喂养羊驼、柯尔鸭，森镜侏罗纪山林中仿真恐龙与科普展板把地球演化史变成探险故事。",
    "fee": "门票50元/人",
    "source": "南京市农业农村局",
    "family_friendly": True
})

activities.append({
    "title": "龙潭水乡研学一日营",
    "venue": "栖霞区龙潭街道水一方生态休闲旅游区",
    "city": "nanjing",
    "start_date": "2026-06-28",
    "end_date": "2026-08-31",
    "link": "http://www.njdaily.cn/news/2026/0713/8480558336506310023.html",
    "description": "体验非遗贴金、航空科普、美育画扇、农耕钓虾、基地劳作五大课堂，在金箔博物馆亲手贴金箔，在龙潭通用机场上航空科普课。",
    "fee": "298元/组",
    "source": "南京日报",
    "family_friendly": True
})

activities.append({
    "title": "八卦洲陌上花渡乡野童趣亲子研学夏令营",
    "venue": "栖霞区八卦洲陌上花渡",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7657380793634800155/",
    "description": "荷花科普研学、浑水摸鱼、丛林寻宝、鲜果采摘、田园露天KTV、洲头公园游览，专为3-10岁亲子家庭设计，让孩子远离电子产品拥抱自然。",
    "fee": "198元/人",
    "source": "栖霞文旅",
    "family_friendly": True
})

activities.append({
    "title": "八卦洲陌上花渡毕业露营套餐",
    "venue": "栖霞区八卦洲陌上花渡",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.nanjing.gov.cn/zgnjsjb/jrtt/202607/t20260714_5876186.html",
    "description": "138元囊括门票、烧烤、篝火、露天电影的毕业露营套餐，性价比十足，适合学生团体和亲子家庭体验田园露营乐趣。",
    "fee": "138元/人",
    "source": "南京市人民政府",
    "family_friendly": True
})

# 雨花台区
activities.append({
    "title": "雨花台稻香部落萌宠童趣乐园",
    "venue": "雨花台区稻香部落",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.nanjing.gov.cn/zgnjsjb/jrtt/202607/t20260714_5876186.html",
    "description": "9.9元畅玩萌宠乐园与童趣乐园，可现场投喂羊驼、水豚，还有多种无动力游乐设施，适合低龄儿童游玩。",
    "fee": "9.9元/人",
    "source": "南京市人民政府",
    "family_friendly": True
})

# 江北新区
activities.append({
    "title": "虫子谷博物公园暑期参观",
    "venue": "江北新区老山北麓虫子谷",
    "city": "nanjing",
    "start_date": "2026-06-26",
    "end_date": "2027-06-28",
    "link": "http://www.njdaily.cn/news/2026/0713/8480558336506310023.html",
    "description": "全新开放的自然艺术复合型文旅新地标，包含虫子美术馆、儿童美术馆、自然艺术馆、蚂蚁书店等七大区域，同步举办国际儿童艺术邀请展。",
    "fee": "免费需预约",
    "source": "南京日报",
    "family_friendly": True
})

activities.append({
    "title": "虫子和孩子国际儿童艺术邀请展",
    "venue": "江北新区虫子谷儿童美术馆",
    "city": "nanjing",
    "start_date": "2026-06-26",
    "end_date": "2027-06-28",
    "link": "https://k.sina.cn/article_7880068258_1d5b04ca201901bzci.html",
    "description": "汇集了6963名儿童创作的9847件作品的大型国际儿童艺术展，孩子们可钻进仿蚂蚁巢穴的地下展示空间，在儿童艺术工坊用自然材料自由创作。",
    "fee": "免费需预约",
    "source": "新浪新闻",
    "family_friendly": True
})

activities.append({
    "title": "江北新区简诺田园蔬果采摘体验",
    "venue": "江北新区简诺田园",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.nanjing.gov.cn/zgnjsjb/jrtt/202607/t20260714_5876186.html",
    "description": "支持师生免费采摘1公斤时令蔬菜，沉浸式感受田园生活，体验农耕乐趣，适合亲子家庭周末出游。",
    "fee": "入园免费，采摘另计",
    "source": "南京市人民政府",
    "family_friendly": True
})

# 溧水区
activities.append({
    "title": "郭兴庄园城市夏日自然博物研学系列",
    "venue": "溧水郭兴庄园",
    "city": "nanjing",
    "start_date": "2026-07-04",
    "end_date": "2026-07-28",
    "link": "http://www.njdaily.cn/news/2026/0713/8480558336506310023.html",
    "description": "涵盖观鸟、昆虫、爬宠、地质、植物、菌类、海洋、萤火虫夜观八大主题的系列研学课程，8场课程分批次开展。",
    "fee": "168元/场",
    "source": "南京日报",
    "family_friendly": True
})

activities.append({
    "title": "溧水傅家边夏季鲜果采摘节",
    "venue": "溧水区傅家边",
    "city": "nanjing",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1032504454_121106832/",
    "description": "千亩果林夏日果香四溢，杨梅、桃子挂满枝头，入园采摘尽享田园丰收之乐，适合全家出游体验采摘乐趣。",
    "fee": "入园30元/人，采摘按斤计费",
    "source": "南京妇联",
    "family_friendly": True
})

activities.append({
    "title": "溧水慧泽水上运动基地暑期体验",
    "venue": "溧水区慧泽水上运动基地",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1032504454_121106832/",
    "description": "体验皮划艇、桨板戏水，参与热闹水枪大战，沉浸式玩转缤纷水上乐趣，专业教练指导，安全有保障。",
    "fee": "128元/人起",
    "source": "南京妇联",
    "family_friendly": True
})

activities.append({
    "title": "溧水竹上云想水蜜桃采摘季",
    "venue": "溧水竹上云想",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-15",
    "link": "http://www.nanjing.gov.cn/zgnjsjb/jrtt/202607/t20260714_5876186.html",
    "description": "凭高考准考证可免费采摘2.5公斤清甜水蜜桃，就餐赠送鲜榨果汁，消费达标可免费兑换游泳、烧烤派对体验。",
    "fee": "采摘30元/斤",
    "source": "南京市人民政府",
    "family_friendly": True
})

activities.append({
    "title": "溧水南京玫瑰园暑期开放",
    "venue": "溧水区南京玫瑰园",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.nanjing.gov.cn/zgnjsjb/jrtt/202607/t20260714_5876186.html",
    "description": "免票开放的玫瑰主题园区，夏季玫瑰盛开，花香满园，适合亲子散步拍照，感受浪漫田园风光。",
    "fee": "免费",
    "source": "南京市人民政府",
    "family_friendly": True
})

# 高淳区
activities.append({
    "title": "固城湖水慢城暑期戏水嘉年华",
    "venue": "高淳区固城湖水慢城",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.njdaily.cn/news/2026/0713/8480558336506310023.html",
    "description": "整条溪道隐藏于浓密树荫下，搭配智能雾森系统持续降温，推出水枪大战、慢鸭漂流赛等潮玩新项目，亲子家庭轻松解锁夏日乐趣。",
    "fee": "门票80元/人",
    "source": "南京日报",
    "family_friendly": True
})

activities.append({
    "title": "高淳老街亲子研学一日游",
    "venue": "高淳老街",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1049666102_122924294/",
    "description": "集齐明清古建筑文化、江南非遗技艺、红色历史文化的亲子研学宝地，非遗展示馆、乾隆古井、杨厅、关王庙、新四军司令部旧址一线贯通。",
    "fee": "街区免费，展馆联票60元",
    "source": "搜狐网",
    "family_friendly": True
})

activities.append({
    "title": "漆桥古村方言文化研学",
    "venue": "高淳漆桥老街",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://news.longhoo.net/2026/gaochun_0710/870661.html",
    "description": "漆桥古镇底蕴深厚，青瓦古街绵延悠长，可探访高淳方言文化，了解古吴语活化石，感受孔氏传统文化与千年古镇风貌。",
    "fee": "免费",
    "source": "龙虎网",
    "family_friendly": True
})

activities.append({
    "title": "高淳桠溪都市现代农业园采摘季",
    "venue": "高淳桠溪都市现代农业园",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.nanjing.gov.cn/zgnjsjb/jrtt/202607/t20260714_5876186.html",
    "description": "入园零门槛免票，鲜果采摘七至八折，五人同行一人免采摘费，推出便携毕业鲜果礼盒，适合亲子采摘游。",
    "fee": "免门票，采摘按斤计费",
    "source": "南京市人民政府",
    "family_friendly": True
})

activities.append({
    "title": "高淳青山茶旅基地采茶制茶研学",
    "venue": "高淳青山茶旅基地",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.nanjing.gov.cn/zgnjsjb/jrtt/202607/t20260714_5876186.html",
    "description": "免入园门票，可免费品鉴雨花茶、碧螺春，采茶制茶研学半价优惠，适合带孩子了解茶文化与传统制茶工艺。",
    "fee": "免门票，研学体验88元/人",
    "source": "南京市人民政府",
    "family_friendly": True
})

# 六合区
activities.append({
    "title": "金牛湖葡萄庄园采摘季",
    "venue": "六合金牛湖葡萄庄园",
    "city": "nanjing",
    "start_date": "2026-07-15",
    "end_date": "2026-09-15",
    "link": "http://www.nanjing.gov.cn/zgnjsjb/jrtt/202607/t20260714_5876186.html",
    "description": "进入采摘旺季，关注官方账号即可领取试吃果盒，葡萄采摘、零售全部八折，多个品种可供选择，适合亲子采摘体验。",
    "fee": "入园免费，采摘20元/斤起",
    "source": "南京市人民政府",
    "family_friendly": True
})

activities.append({
    "title": "桂子山石柱林地质探秘研学",
    "venue": "六合桂子山石柱林景区",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.nanjing.gov.cn/zgnjsjb/jrtt/202607/t20260714_5876186.html",
    "description": "凭中高考准考证免费入园，观赏被誉为薯条山的地质奇观，了解火山地貌形成原理，开展地质科普研学。",
    "fee": "门票30元/人",
    "source": "南京市人民政府",
    "family_friendly": True
})

activities.append({
    "title": "平山森林公园暑期避暑游",
    "venue": "六合平山森林公园",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.nanjing.gov.cn/zgnjsjb/jrtt/202607/t20260714_5876186.html",
    "description": "凭中高考准考证免费入园，依托原生态山林避暑纳凉，森林覆盖率高，空气清新，适合全家休闲度假。",
    "fee": "门票40元/人",
    "source": "南京市人民政府",
    "family_friendly": True
})

activities.append({
    "title": "金牛湖野生动物王国暑期游",
    "venue": "六合金牛湖野生动物王国",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1032504454_121106832/",
    "description": "萌宠互动、西游演艺精彩纷呈，可近距离接触多种野生动物，适合亲子家庭游玩观赏。",
    "fee": "门票150元/人",
    "source": "南京妇联",
    "family_friendly": True
})

# ============ 2. 文化馆/图书馆活动 ============

# 栖霞区文化馆
activities.append({
    "title": "小暑纳凉香囊避疫非遗手作课",
    "venue": "栖霞区文化馆402教室",
    "city": "nanjing",
    "start_date": "2026-07-05",
    "end_date": "2026-07-05",
    "link": "http://m.toutiao.com/group/7657380793634800155/",
    "description": "从小暑节气科普讲起，了解古人如何顺应时节、祛暑纳福，亲手缝制古法香囊，填一味草药，留一缕清香，感受传统手艺的温润。",
    "fee": "免费需报名",
    "source": "栖霞文旅",
    "family_friendly": True
})

activities.append({
    "title": "大暑竹韵扇面生凉竹编体验课",
    "venue": "栖霞区文化馆402教室",
    "city": "nanjing",
    "start_date": "2026-07-26",
    "end_date": "2026-07-26",
    "link": "http://m.toutiao.com/group/7657380793634800155/",
    "description": "大暑天讲民俗、看竹编、做竹扇，从节气到手艺，一把扇子编完带回家，感受非遗竹编技艺的独特魅力。",
    "fee": "免费需报名",
    "source": "栖霞文旅",
    "family_friendly": True
})

activities.append({
    "title": "石语新篇矿石文明记忆展",
    "venue": "栖霞区文化艺术中心广场",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-07-31",
    "link": "http://m.toutiao.com/group/7657380793634800155/",
    "description": "以矿石为线索，从远古岩画到金石铭文，看矿石如何成为文字最早的载体，每一块石头都是一位沉默的史官。",
    "fee": "免费",
    "source": "栖霞文旅",
    "family_friendly": True
})

activities.append({
    "title": "生生之道中医文明千年智慧展",
    "venue": "栖霞区图书馆三楼展厅",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-07-31",
    "link": "http://m.toutiao.com/group/7657380793634800155/",
    "description": "从黄帝内经到伤寒杂病论，从针灸到推拿，用文物典籍、诊疗器具、药材标本，把中医五千年的脉络捋了一遍。",
    "fee": "免费",
    "source": "栖霞文旅",
    "family_friendly": True
})

activities.append({
    "title": "栖阅好少年恐龙达达之一起去寻宝",
    "venue": "栖霞区图书馆",
    "city": "nanjing",
    "start_date": "2026-07-11",
    "end_date": "2026-07-11",
    "link": "http://m.toutiao.com/group/7657380793634800155/",
    "description": "认识两位恐龙主角，共读寻宝故事，了解霸王龙和伤齿龙的小知识，适合喜欢恐龙的小朋友参与。",
    "fee": "免费",
    "source": "栖霞文旅",
    "family_friendly": True
})

activities.append({
    "title": "科普达人小米吴大世界章鱼不见了",
    "venue": "栖阅时光仙林大学书房",
    "city": "nanjing",
    "start_date": "2026-07-25",
    "end_date": "2026-07-25",
    "link": "http://m.toutiao.com/group/7657380793634800155/",
    "description": "节奏大挑战暖场破冰，共读绘本，章鱼知识趣味问答，最后来一场章鱼浮沉子科学魔法秀，边玩边学科普知识。",
    "fee": "免费",
    "source": "栖霞文旅",
    "family_friendly": True
})

activities.append({
    "title": "小郎中大智慧中医传承专场",
    "venue": "栖霞区图书馆三楼活动室",
    "city": "nanjing",
    "start_date": "2026-07-18",
    "end_date": "2026-07-18",
    "link": "http://m.toutiao.com/group/7657380793634800155/",
    "description": "分享中医文化传统，绘本精讲，讨论老虎为什么守着杏林，体验望闻问切，让孩子当一回小郎中。",
    "fee": "免费需报名",
    "source": "栖霞文旅",
    "family_friendly": True
})

# 秦淮区文化馆
activities.append({
    "title": "七彩童年曲艺少儿夏令营快板贯口班",
    "venue": "秦淮区文化馆二楼小剧场",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-07-10",
    "link": "http://m.toutiao.com/group/7655674750219321919/",
    "description": "张派相声非遗传承课程，学习快板、贯口基础技艺，融入南京方言与江南民俗，15个名额，8岁以上儿童可报名。",
    "fee": "公益免费",
    "source": "秦淮文旅",
    "family_friendly": True
})

activities.append({
    "title": "七彩童年亲子中式插花课",
    "venue": "秦淮区文化馆二楼会议室",
    "city": "nanjing",
    "start_date": "2026-07-02",
    "end_date": "2026-07-02",
    "link": "http://m.toutiao.com/group/7655674750219321919/",
    "description": "融合儒道禅美学的中式插花体验，追求天人合一、以花载道，8岁以上亲子家庭15组名额，需家长全程陪同。",
    "fee": "公益免费",
    "source": "秦淮文旅",
    "family_friendly": True
})

activities.append({
    "title": "七彩童年绒花非遗手作课",
    "venue": "秦淮区文化馆二楼会议室",
    "city": "nanjing",
    "start_date": "2026-07-03",
    "end_date": "2026-07-03",
    "link": "http://m.toutiao.com/group/7655674750219321919/",
    "description": "学习制作被誉为发髻上的春天的非遗绒花，以桑蚕丝为绒、铜丝为骨架纯手工制成，8岁以上亲子家庭10组名额。",
    "fee": "公益免费",
    "source": "秦淮文旅",
    "family_friendly": True
})

activities.append({
    "title": "七彩童年中药艾草锤制作课",
    "venue": "秦淮区文化馆二楼会议室",
    "city": "nanjing",
    "start_date": "2026-07-06",
    "end_date": "2026-07-06",
    "link": "http://m.toutiao.com/group/7655674750219321919/",
    "description": "融合中草药炮制技艺、中医经络养生、传统民俗手工的沉浸式体验课，亲手制作养生拍打锤，15个名额，8岁以上可报名。",
    "fee": "公益免费",
    "source": "秦淮文旅",
    "family_friendly": True
})

activities.append({
    "title": "七彩童年中医八段锦夏令营",
    "venue": "秦淮区文化馆二楼小剧场",
    "city": "nanjing",
    "start_date": "2026-07-08",
    "end_date": "2026-07-10",
    "link": "http://m.toutiao.com/group/7655674750219321919/",
    "description": "国家级非物质文化遗产八段锦教学，共八个动作，柔和连贯、舒展优美，8岁以上15个名额，需连续三天参加课程。",
    "fee": "公益免费",
    "source": "秦淮文旅",
    "family_friendly": True
})

activities.append({
    "title": "七彩童年秦淮灯彩非遗课",
    "venue": "秦淮区文化馆二楼会议室",
    "city": "nanjing",
    "start_date": "2026-07-08",
    "end_date": "2026-07-10",
    "link": "http://m.toutiao.com/group/7655674750219321919/",
    "description": "省级非物质文化遗产秦淮灯彩课程，以传统扎灯技艺为核心，了解秦淮灯彩历史与材料工艺，亲手制作花灯，15个名额。",
    "fee": "公益免费",
    "source": "秦淮文旅",
    "family_friendly": True
})

# 秦淮区图书馆
activities.append({
    "title": "四季变化与天气的那些事儿科普讲座",
    "venue": "秦淮区图书馆4楼报告厅",
    "city": "nanjing",
    "start_date": "2026-07-22",
    "end_date": "2026-07-22",
    "link": "http://m.toutiao.com/group/7663467508074103339/",
    "description": "结合二十四节气知识揭秘四季形成原因，融入气象谚语话题，从过去的经验总结到信息时代大数据的科学性，适合6-10岁儿童。",
    "fee": "免费需报名",
    "source": "秦淮区图书馆",
    "family_friendly": True
})

activities.append({
    "title": "听风读云天气变化奥秘研学行",
    "venue": "浦口气象防灾科普馆",
    "city": "nanjing",
    "start_date": "2026-07-29",
    "end_date": "2026-07-29",
    "link": "http://m.toutiao.com/group/7663467508074103339/",
    "description": "走进江苏省首个气象防灾专题馆，十大主题展区依托虚拟现实、多媒体数控等前沿技术，化身气象小主播模拟天气播报。",
    "fee": "免费需报名",
    "source": "秦淮区图书馆",
    "family_friendly": True
})

# ============ 3. 公益托管/暑期托管班 ============

activities.append({
    "title": "江浦街道爱心暑托班",
    "venue": "江北新区江浦街道各社区",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-20",
    "link": "http://m.toutiao.com/group/7663054549082604067/",
    "description": "围绕科技启智、非遗润心、红色铸魂、劳动育人四大方向，开设编程启蒙、物理实验、航天模型制作、漆扇手作等特色课程。",
    "fee": "公益免费",
    "source": "扬子晚报网",
    "family_friendly": True
})

activities.append({
    "title": "孝陵卫街道爱心暑托班小卫街社区点",
    "venue": "玄武区孝陵卫街道小卫街社区",
    "city": "nanjing",
    "start_date": "2026-07-06",
    "end_date": "2026-07-31",
    "link": "http://www.xwzf.gov.cn/xwzx/jddt/xlwjd/202607/t20260708_5872957.html",
    "description": "20个全日制工作日，优先面向困境青少年、新就业群体子女开放，含课业辅导、安全教育、科学实验、古诗词赏析等课程。",
    "fee": "公益免费",
    "source": "玄武区人民政府",
    "family_friendly": True
})

activities.append({
    "title": "孝陵卫街道爱心暑托班农科院社区点",
    "venue": "玄武区孝陵卫街道农科院社区",
    "city": "nanjing",
    "start_date": "2026-07-06",
    "end_date": "2026-07-31",
    "link": "http://www.xwzf.gov.cn/xwzx/jddt/xlwjd/202607/t20260708_5872957.html",
    "description": "立足农业科技产业集聚优势，增设3D打印笔创意制作、编程实验箱实操等前沿科技课程，为科创人才子女打造家门口的科学启蒙课堂。",
    "fee": "公益免费",
    "source": "玄武区人民政府",
    "family_friendly": True
})

activities.append({
    "title": "锁金村街道公益暑托班新庄社区点",
    "venue": "玄武区锁金村街道新庄社区",
    "city": "nanjing",
    "start_date": "2026-07-15",
    "end_date": "2026-08-10",
    "link": "http://m.toutiao.com/group/7663097378953757190/",
    "description": "优先保障梦想小屋关爱对象、困境青少年、新业态从业人员子女等五类重点群体，每日趣味阅读、科学小实验、创意手工、户外素质拓展。",
    "fee": "公益免费",
    "source": "扬子晚报网",
    "family_friendly": True
})

activities.append({
    "title": "锁金村街道公益暑托班紫鑫城社区点",
    "venue": "玄武区锁金村街道紫鑫城社区",
    "city": "nanjing",
    "start_date": "2026-07-15",
    "end_date": "2026-08-10",
    "link": "http://m.toutiao.com/group/7663097378953757190/",
    "description": "专职社工+大学生+社区辅助铁三角组合，开设劳动教育、法治小课堂、安全自护演练、心理健康悄悄话等课程，每天不重样。",
    "fee": "公益免费",
    "source": "扬子晚报网",
    "family_friendly": True
})

activities.append({
    "title": "鼓楼高新区创享益夏暑托班",
    "venue": "鼓楼高新区创新广场",
    "city": "nanjing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-20",
    "link": "http://www.njdaily.cn/news/2026/0716/8480558748823161574.html",
    "description": "开设非遗研学、红色研学等课程，面向园区企业职工和新就业群体子女开放，解决职工暑期子女看护难题。",
    "fee": "公益免费",
    "source": "南京日报",
    "family_friendly": True
})

activities.append({
    "title": "晨光1865创意产业园暑托班",
    "venue": "秦淮区晨光1865创意产业园",
    "city": "nanjing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-20",
    "link": "http://www.njdaily.cn/news/2026/0716/8480558748823161574.html",
    "description": "规划国学文化周、紫金银辉周、非遗体验周、企业探学周四大主题课程，让园区职工子女度过充实暑假。",
    "fee": "公益免费",
    "source": "南京日报",
    "family_friendly": True
})

activities.append({
    "title": "星河WORLD园区叮叮书房暑托班",
    "venue": "玄武区星河WORLD园区叮叮书房",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.njdaily.cn/news/2026/0716/8480558748823161574.html",
    "description": "家长上班孩子进班模式，全天托管含晨读、作业辅导、手工类特色课程、下午茶，方便园区职工子女就近托管。",
    "fee": "按天收费",
    "source": "南京日报",
    "family_friendly": True
})

# ============ 4. 南京科技馆活动 ============

activities.append({
    "title": "长空造物力学科探索工坊",
    "venue": "南京科技馆三楼科创教室",
    "city": "nanjing",
    "start_date": "2026-07-16",
    "end_date": "2026-07-18",
    "link": "https://m.sohu.com/a/1050698155_121106832/",
    "description": "南航科教筑梦团队开设七大物理实验课堂，理论讲解加动手实操，表面张力大冒险、霍尔效应解密、纸桥承重挑战赛等趣味实验。",
    "fee": "免费现场报名",
    "source": "南京科技馆",
    "family_friendly": True
})

activities.append({
    "title": "生命护航安全科普闯关营",
    "venue": "南京科技馆负一楼红十字会创伤救护展区",
    "city": "nanjing",
    "start_date": "2026-07-16",
    "end_date": "2026-07-18",
    "link": "https://m.sohu.com/a/1050698155_121106832/",
    "description": "河海大学博爱青春志愿团队开展沉浸式安全科普，急救大富翁、禁毒科普互动、水力趣味小实验，亲子互动学习自救技能。",
    "fee": "免费现场参与",
    "source": "南京科技馆",
    "family_friendly": True
})

activities.append({
    "title": "睛彩相伴全龄护眼科普站",
    "venue": "南京科技馆三楼科创教室",
    "city": "nanjing",
    "start_date": "2026-07-16",
    "end_date": "2026-07-16",
    "link": "https://m.sohu.com/a/1050698155_121106832/",
    "description": "中国药科大学志愿者打造分龄护眼课堂，近视科普小课堂、护眼问答集章兑奖、盲行协作体验，牢记20-20-20护眼法则。",
    "fee": "免费现场报名",
    "source": "南京科技馆",
    "family_friendly": True
})

activities.append({
    "title": "血脉寻踪人体生命科普课堂",
    "venue": "南京科技馆序厅",
    "city": "nanjing",
    "start_date": "2026-07-18",
    "end_date": "2026-07-18",
    "link": "https://m.sohu.com/a/1050698155_121106832/",
    "description": "聚焦基础人体血液科普，内容温和易懂，适配低龄小朋友开展生命启蒙教育，血液知识大转盘、人体流程拼图闯关。",
    "fee": "免费现场参与",
    "source": "南京科技馆",
    "family_friendly": True
})

activities.append({
    "title": "小科公益寻知记可口可乐工厂研学",
    "venue": "江北新区南京可口可乐观光工厂",
    "city": "nanjing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-31",
    "link": "http://www.njstm.org.cn/html/zxdt/kjgdt/4967.html",
    "description": "全新打造的亲子公益研学品牌，走进全透明观光走廊观摩智能化全自动生产线，了解现代化食品生产标准与低碳生产技术。",
    "fee": "公益免费",
    "source": "南京科技馆",
    "family_friendly": True
})

activities.append({
    "title": "飞向太空航天科创入门营",
    "venue": "南京科技馆",
    "city": "nanjing",
    "start_date": "2026-07-22",
    "end_date": "2026-07-26",
    "link": "https://m.sohu.com/a/1034814809_121106832/",
    "description": "专为1-4年级小学生打造的零基础航天启蒙体系，科普讲座加科学实验加手工创作加竞技挑战，5天沉浸式航天科创营。",
    "fee": "1980元/人",
    "source": "南京科技馆",
    "family_friendly": True
})

activities.append({
    "title": "深空探月航天科创进阶营",
    "venue": "南京科技馆",
    "city": "nanjing",
    "start_date": "2026-07-29",
    "end_date": "2026-08-02",
    "link": "https://m.sohu.com/a/1034814809_121106832/",
    "description": "3-7年级飞向太空营进阶版，紧扣嫦娥七号探月热点，接轨前沿深空探测技术，NASA授证航天导师领衔授课。",
    "fee": "2580元/人",
    "source": "南京科技馆",
    "family_friendly": True
})

# ============ 5. 南京青少年宫活动 ============

activities.append({
    "title": "南京市青少年宫AI全栈创作实战营",
    "venue": "南京市青少年宫马台街总部",
    "city": "nanjing",
    "start_date": "2026-07-15",
    "end_date": "2026-08-15",
    "link": "https://www.nqsng.cn/qsng/website/web_v2/index.html",
    "description": "零基础也能轻松入门的AI创作课程，学习AI绘画、AI编程、内容创作等前沿技能，培养孩子人工智能时代的核心素养。",
    "fee": "2980元/人",
    "source": "南京市青少年宫",
    "family_friendly": True
})

activities.append({
    "title": "小市分部美术书画零基础福利课",
    "venue": "南京市青少年宫小市分部",
    "city": "nanjing",
    "start_date": "2026-07-10",
    "end_date": "2026-08-20",
    "link": "https://www.nqsng.cn/qsng/website/web_v2/index.html",
    "description": "美术水平考级报名启动，同步推出零基础书画福利课程，儿童画、素描、书法等多种课程可选，培养孩子艺术素养。",
    "fee": "599元/12课时",
    "source": "南京市青少年宫",
    "family_friendly": True
})

activities.append({
    "title": "江宁分部古筝美育少儿体适能课",
    "venue": "南京市青少年宫江宁分部",
    "city": "nanjing",
    "start_date": "2026-07-10",
    "end_date": "2026-08-20",
    "link": "https://www.nqsng.cn/qsng/website/web_v2/index.html",
    "description": "6节精品课解锁夏日成长，古筝美育培养音乐素养，少儿体适能锻炼强健体魄，艺术与运动双管齐下。",
    "fee": "399元/6课时",
    "source": "南京市青少年宫",
    "family_friendly": True
})

activities.append({
    "title": "小市分部主持表演特价班",
    "venue": "南京市青少年宫小市分部",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.nqsng.cn/qsng/website/web_v2/index.html",
    "description": "599元12次课还送定制大礼包，小主持与表演课程，提升孩子表达能力与自信心，培养舞台表现力。",
    "fee": "599元/12课时",
    "source": "南京市青少年宫",
    "family_friendly": True
})

activities.append({
    "title": "青少年宫非遗手作成品短程课",
    "venue": "南京市青少年宫马台街总部",
    "city": "nanjing",
    "start_date": "2026-07-15",
    "end_date": "2026-08-15",
    "link": "https://www.nqsng.cn/qsng/website/web_v2/index.html",
    "description": "非遗手作体验课程，多种传统手工艺可选，亲手制作非遗成品带回家，感受传统文化魅力。",
    "fee": "199元/次",
    "source": "南京市青少年宫",
    "family_friendly": True
})

activities.append({
    "title": "青少年宫击剑VR模拟体验课",
    "venue": "南京市青少年宫马台街总部",
    "city": "nanjing",
    "start_date": "2026-07-15",
    "end_date": "2026-08-15",
    "link": "https://www.nqsng.cn/qsng/website/web_v2/index.html",
    "description": "仅限10个名额的击剑体验课，结合VR模拟技术，让孩子在安全环境中体验击剑运动的魅力。",
    "fee": "99元/体验课",
    "source": "南京市青少年宫",
    "family_friendly": True
})

activities.append({
    "title": "少年强红十字青少年夏令营",
    "venue": "南京未成年人社会实践行知基地",
    "city": "nanjing",
    "start_date": "2026-07-22",
    "end_date": "2026-07-25",
    "link": "http://m.toutiao.com/group/7659987225316164123/",
    "description": "四天三晚沉浸式实践夏令营，红十字生命教育、质检科普、无人机研学、毅行徒步、深度急救实训、水上挑战等多主题。",
    "fee": "850元/人",
    "source": "南京市红十字会",
    "family_friendly": True
})

# ============ 6. 景区/古镇暑期活动 ============

# 牛首山
activities.append({
    "title": "牛首山哞哞国学夏令营",
    "venue": "牛首山文化旅游区",
    "city": "nanjing",
    "start_date": "2026-06-21",
    "end_date": "2026-08-31",
    "link": "https://www.niushoushan.net/Notify/3248.html",
    "description": "携手德基与浦江学堂合作，面向四年级以上学生免费招募30名学员，开设系统国学课程，在山林间诵读经典、涵养品格。",
    "fee": "公益免费需选拔",
    "source": "牛首山官网",
    "family_friendly": True
})

activities.append({
    "title": "牛首山夜探佛顶宫沉浸式夜游",
    "venue": "牛首山佛顶宫",
    "city": "nanjing",
    "start_date": "2026-06-27",
    "end_date": "2026-08-31",
    "link": "https://www.niushoushan.net/Notify/3248.html",
    "description": "每周五、周六19:00-20:00上线，整合佛顶宫核心景观资源，植入实景NPC与完整叙事剧情，领取七宝图谱寻访非遗匠迹。",
    "fee": "含门票98元/人",
    "source": "牛首山官网",
    "family_friendly": True
})

activities.append({
    "title": "牛首山海丝文化周活动",
    "venue": "牛首山文化旅游区",
    "city": "nanjing",
    "start_date": "2026-07-08",
    "end_date": "2026-07-14",
    "link": "https://www.niushoushan.net/Notify/3248.html",
    "description": "主题文物展览、专家学术分享、青少年研学实践，全景再现郑和扬帆远航、海上丝绸之路繁荣兴盛的历史图景。",
    "fee": "含门票",
    "source": "牛首山官网",
    "family_friendly": True
})

activities.append({
    "title": "牛首山中国航海日免费开放日",
    "venue": "牛首山文化旅游区",
    "city": "nanjing",
    "start_date": "2026-07-11",
    "end_date": "2026-07-11",
    "link": "https://www.niushoushan.net/Notify/3248.html",
    "description": "7月11日中国航海日免费开放日，投放5万张免费门票，全网统一时段预约，先约先得、约满即止。",
    "fee": "免费需预约",
    "source": "牛首山官网",
    "family_friendly": True
})

activities.append({
    "title": "牛首山敦煌壁画临摹研学课",
    "venue": "牛首山文化旅游区",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.niushoushan.net/Notify/3248.html",
    "description": "慧行牛首研学系列课程之一，学习敦煌壁画艺术特点，亲手体验壁画临摹技法，感受千年艺术魅力。",
    "fee": "198元/人",
    "source": "牛首山官网",
    "family_friendly": True
})

activities.append({
    "title": "牛首山非遗金箔实操研学课",
    "venue": "牛首山文化旅游区",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.niushoushan.net/Notify/3248.html",
    "description": "了解金陵金箔制作工艺，亲手体验贴金箔技艺，感受国家级非遗的独特魅力，制作专属金箔文创作品。",
    "fee": "168元/人",
    "source": "牛首山官网",
    "family_friendly": True
})

activities.append({
    "title": "牛首山冰酷炫跑活动",
    "venue": "牛首山文化旅游区",
    "city": "nanjing",
    "start_date": "2026-08-01",
    "end_date": "2026-08-07",
    "link": "https://www.niushoushan.net/Notify/3248.html",
    "description": "第七届牛首山冰酷炫跑，融合敦煌美学与海丝文化元素，为亲子家庭提供趣味互动、户外休闲新选择。",
    "fee": "68元/人起",
    "source": "牛首山官网",
    "family_friendly": True
})

# 红山森林动物园
activities.append({
    "title": "红山森林动物园职业体验夏校",
    "venue": "红山森林动物园",
    "city": "nanjing",
    "start_date": "2026-07-20",
    "end_date": "2026-07-24",
    "link": "http://m.toutiao.com/group/7662729129090925102/",
    "description": "5天深度体验，孩子们轮番解锁园长、动物保育员、野生动物救护员、生态调研员等特色岗位，沉浸式感受野生动物保护工作。",
    "fee": "2980元/人",
    "source": "紫牛新闻",
    "family_friendly": True
})

activities.append({
    "title": "红山森林动物园森林走读夏校",
    "venue": "红山森林动物园",
    "city": "nanjing",
    "start_date": "2026-07-21",
    "end_date": "2026-07-31",
    "link": "http://m.toutiao.com/group/7662729129090925102/",
    "description": "户外山林探索搭配室内科普课堂，孩子们参与蘑菇种植与观察、动物运动会、手工制作，让生态知识在动手实践中落地生根。",
    "fee": "1680元/人",
    "source": "紫牛新闻",
    "family_friendly": True
})

activities.append({
    "title": "世界动物地图大冒险半日营",
    "venue": "红山森林动物园",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662729129090925102/",
    "description": "轻量化半日自然探索课程，从独特视角科普世界各地动物习性，趣味闯关游戏中学到动物知识。",
    "fee": "198元/人",
    "source": "紫牛新闻",
    "family_friendly": True
})

activities.append({
    "title": "屎命召唤营趣味科普课",
    "venue": "红山森林动物园",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662729129090925102/",
    "description": "另辟蹊径的趣味科普课程，从动物粪便的独特视角科普动物习性与生态系统知识，寓教于乐。",
    "fee": "168元/人",
    "source": "紫牛新闻",
    "family_friendly": True
})

activities.append({
    "title": "红山动物园奇妙夜夜探活动",
    "venue": "红山森林动物园",
    "city": "nanjing",
    "start_date": "2026-08-05",
    "end_date": "2026-08-26",
    "link": "https://party.hudongba.com/party/5g3m5.html",
    "description": "跟随自然导师踏入静谧园区，邂逅昼伏夜出的小动物，沉浸式感受昼夜截然不同的山林生态，解锁白天游园看不到的自然秘境。",
    "fee": "298元/两人（一大一小）",
    "source": "红山动物园",
    "family_friendly": True
})

activities.append({
    "title": "红山虎生日会互动体验",
    "venue": "红山森林动物园",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://news.longhoo.net/2026/xuanwu_0611/866482.html",
    "description": "孩子们可在饲养员指导下为动物制作专属生日蛋糕或节日粽子，了解动物饮食习性，近距离感受动物保护工作。",
    "fee": "含门票70元/人",
    "source": "龙虎网",
    "family_friendly": True
})

# 南京古生物博物馆
activities.append({
    "title": "南京古生物博物馆昆虫奇趣博物馆课",
    "venue": "南京古生物博物馆",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662729129090925102/",
    "description": "以新奇有趣的切入点拆解地球生命密码，认识丰富多彩的昆虫世界，了解昆虫演化历史与生态价值。",
    "fee": "128元/人",
    "source": "紫牛新闻",
    "family_friendly": True
})

activities.append({
    "title": "解码远古琥珀研学课",
    "venue": "南京古生物博物馆",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662729129090925102/",
    "description": "观察珍贵琥珀标本，了解琥珀形成过程与其中包裹的远古生物，穿越时空窥探亿万年前的生物世界。",
    "fee": "158元/人",
    "source": "紫牛新闻",
    "family_friendly": True
})

activities.append({
    "title": "㞎㞎故事多古生物科普课",
    "venue": "南京古生物博物馆",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662729129090925102/",
    "description": "从粪便化石的独特视角了解古生物饮食习惯与生态环境，趣味十足的科普课程。",
    "fee": "98元/人",
    "source": "紫牛新闻",
    "family_friendly": True
})

activities.append({
    "title": "古生物博物馆奇妙夜露营活动",
    "venue": "南京古生物博物馆",
    "city": "nanjing",
    "start_date": "2026-07-25",
    "end_date": "2026-07-25",
    "link": "http://m.toutiao.com/group/7662729129090925102/",
    "description": "在夜间的博物馆搭建帐篷、组队闯关解谜，在亿万年前的化石标本陪伴下，度过独一无二的博物馆之夜。",
    "fee": "398元/人",
    "source": "紫牛新闻",
    "family_friendly": True
})

activities.append({
    "title": "化石小猎人野外研学",
    "venue": "南京古生物博物馆+野外化石点",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662729129090925102/",
    "description": "走出展厅深入野外实地搜寻化石，探寻远古海洋变迁印记，跟随科研人员梳理化石碎片，推演复原亿万年前古生物全貌。",
    "fee": "268元/人",
    "source": "紫牛新闻",
    "family_friendly": True
})

activities.append({
    "title": "远古生命线索三日科创营",
    "venue": "南京古生物博物馆",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662729129090925102/",
    "description": "时长3日的科创营，少年们跟随科研人员梳理化石碎片，层层推演、拼凑复原亿万年前古生物全貌。",
    "fee": "1280元/人",
    "source": "紫牛新闻",
    "family_friendly": True
})

# 南京市规划建设展览馆
activities.append({
    "title": "2026少年城建说低碳科普课堂",
    "venue": "南京市规划建设展览馆",
    "city": "nanjing",
    "start_date": "2026-07-22",
    "end_date": "2026-07-22",
    "link": "http://m.toutiao.com/group/7662729129090925102/",
    "description": "围绕碳排放管控、绿色节能建筑、城市低碳发展路径、日常家庭减碳妙招展开教学，融合动画演示、沙盘观摩、互动问答。",
    "fee": "免费需预约",
    "source": "紫牛新闻",
    "family_friendly": True
})

# 汤山
activities.append({
    "title": "汤山欢乐水世界暑期焕新开放",
    "venue": "江宁汤山欢乐水世界",
    "city": "nanjing",
    "start_date": "2026-06-20",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663510578668831286/",
    "description": "夏日玩水消暑首选，多种水上滑梯、造浪池、漂流河等项目，适合全家大小一起戏水狂欢。",
    "fee": "门票180元/人起",
    "source": "人民网",
    "family_friendly": True
})

activities.append({
    "title": "汤山矿坑公园泼水派对",
    "venue": "江宁汤山矿坑公园",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_7879923025_1d5ae155101901sy9u.html",
    "description": "废弃矿坑改造的野趣公园，矿野溯溪泼水大战、露天电影、仙女棒互动、烟花瀑布，比园博园人流更少。",
    "fee": "免费入园",
    "source": "新浪新闻",
    "family_friendly": True
})

# 欢乐谷
activities.append({
    "title": "南京欢乐谷蓝鲸音乐节",
    "venue": "南京欢乐谷",
    "city": "nanjing",
    "start_date": "2026-06-27",
    "end_date": "2026-08-30",
    "link": "http://m.toutiao.com/group/7657380793634800155/",
    "description": "城市级音乐盛会，水陆双园联动，多组明星乐队轮番登场，夏日狂欢派对。",
    "fee": "门票260元/人起",
    "source": "栖霞文旅",
    "family_friendly": True
})

activities.append({
    "title": "玛雅海滩水公园暑期开放",
    "venue": "南京欢乐谷玛雅海滩水公园",
    "city": "nanjing",
    "start_date": "2026-06-19",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_7879923025_1d5ae155101901sy9u.html",
    "description": "超大儿童浅水区、造浪池、漂流河，国潮亲子舞台剧精彩上演，1.2米以下儿童免票，高温玩水避暑首选。",
    "fee": "门票220元/人",
    "source": "新浪新闻",
    "family_friendly": True
})

# 其他景区
activities.append({
    "title": "中山植物园昼夜双线研学营",
    "venue": "南京中山植物园",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://news.longhoo.net/2026/xuanwu_0611/866482.html",
    "description": "日间夏令营涵盖植物解构、标本制作等课程，夜间带领孩子们观察昆虫、聆听蛙叫虫鸣，体验奇妙的植物园夜生活。",
    "fee": "198元/人起",
    "source": "龙虎网",
    "family_friendly": True
})

activities.append({
    "title": "聚宝山公园亲子皮划艇体验",
    "venue": "玄武区聚宝山公园",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://news.longhoo.net/2026/xuanwu_0611/866482.html",
    "description": "城市免费郊野公园，大片草坪、开阔湖面，体验皮划艇水上运动，在自然中享受亲子运动时光。",
    "fee": "公园免费，皮划艇80元/小时",
    "source": "龙虎网",
    "family_friendly": True
})

# ============ 7. 书店/商业综合体活动 ============

activities.append({
    "title": "凤凰美术馆世界儿童文学经典大师插画展",
    "venue": "凤凰国际书城5楼凤凰美术馆",
    "city": "nanjing",
    "start_date": "2026-06-07",
    "end_date": "2026-08-31",
    "link": "https://m.weibo.cn/detail/5305757207626381",
    "description": "艺术总监本杰明拉贡布策划的插画展览，听译林编辑深度解读插画细节，体验骑鹅旅行记故事共读与创意绘画工坊。",
    "fee": "免费观展，研学活动另付费",
    "source": "小译林童书",
    "family_friendly": True
})

activities.append({
    "title": "西西弗书店历史喵主题互动展",
    "venue": "华采天地1F主中庭西西弗书店",
    "city": "nanjing",
    "start_date": "2026-05-15",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1025960937_121124711/",
    "description": "喵游华夏萌穿千年主题美陈展，1:1还原漫画经典场景，12只喵咪角色集体出没，完成任务领取限定透卡。",
    "fee": "免费入场",
    "source": "悟空看非遗",
    "family_friendly": True
})

activities.append({
    "title": "德基艺术博物馆暑期特展",
    "venue": "德基广场德基艺术博物馆",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-10-31",
    "link": "https://m.sohu.com/a/1050112394_122914897/",
    "description": "金陵图数字艺术展、动静无尽花卉主题艺术展、BEEPLE数字艺术大展三展同看，数字互动展览趣味十足。",
    "fee": "门票80元/人",
    "source": "搜狐网",
    "family_friendly": True
})

activities.append({
    "title": "马群花园城YONEE乐园",
    "venue": "马群花园城户外广场",
    "city": "nanjing",
    "start_date": "2026-06-27",
    "end_date": "2026-12-31",
    "link": "https://k.sina.cn/article_7880068258_1d5b04ca201901bzci.html",
    "description": "6月27日新开的城东首个户外无动力主题乐园，全天候24小时免费开放，精准适配1-12岁全年龄段孩童。",
    "fee": "免费",
    "source": "新浪新闻",
    "family_friendly": True
})

activities.append({
    "title": "鱼嘴自然能量场暑期开放",
    "venue": "鱼嘴湿地公园鱼嘴自然能量场",
    "city": "nanjing",
    "start_date": "2026-06-01",
    "end_date": "2026-12-31",
    "link": "https://k.sina.cn/article_7880068258_1d5b04ca201901bzci.html",
    "description": "6月1日新开的免费公园，有风之谷、水之镜、林之径、丘之野、森之憩五大区域，适合打卡拍照、运动健身、亲子遛娃。",
    "fee": "免费",
    "source": "新浪新闻",
    "family_friendly": True
})

# ============ 8. 高校研学/科普活动 ============

activities.append({
    "title": "南京师范大学问道南师校园开放日",
    "venue": "南京师范大学仙林校区",
    "city": "nanjing",
    "start_date": "2026-06-14",
    "end_date": "2026-07-03",
    "link": "https://www.163.com/dy/article/KV0SQ69S05345ARG.html",
    "description": "十二大主题开放活动，涵盖体育赛事、校园探秘、名师分享、民俗体验、文博鉴赏、科创研学、亲子赋能等特色板块。",
    "fee": "免费需预约",
    "source": "扬子晚报",
    "family_friendly": True
})

activities.append({
    "title": "南师大粽情阅美名师书香分享会",
    "venue": "南京师范大学仙林校区",
    "city": "nanjing",
    "start_date": "2026-06-18",
    "end_date": "2026-06-18",
    "link": "https://www.163.com/dy/article/KV0SQ69S05345ARG.html",
    "description": "名师面对面分享读书心得与文学见解，在书香氛围中感受百年名校的文化底蕴，适合学龄儿童与家长共同参与。",
    "fee": "免费需预约",
    "source": "扬子晚报",
    "family_friendly": True
})

activities.append({
    "title": "南师大文脉寻踪校史馆研学",
    "venue": "南京师范大学仙林校区校史馆",
    "city": "nanjing",
    "start_date": "2026-06-22",
    "end_date": "2026-06-22",
    "link": "https://www.163.com/dy/article/KV0SQ69S05345ARG.html",
    "description": "走进百年校史馆，了解南京师范大学发展历史与文化传承，在行走中感受教育发展脉络与人文精神。",
    "fee": "免费需预约",
    "source": "扬子晚报",
    "family_friendly": True
})

activities.append({
    "title": "东南大学校园开放日九龙湖校区",
    "venue": "东南大学九龙湖校区",
    "city": "nanjing",
    "start_date": "2026-06-14",
    "end_date": "2026-06-14",
    "link": "https://www.163.com/dy/article/KV0SQ69S05345ARG.html",
    "description": "全院系专业咨询、卓越东大科技大展、东大打卡互动企划，7个官方打卡点位领取东大限定文创，感受顶尖高校氛围。",
    "fee": "免费",
    "source": "扬子晚报",
    "family_friendly": True
})

activities.append({
    "title": "南航航空科普研学体验营",
    "venue": "南京航空航天大学",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1050698155_121106832/",
    "description": "南航科教筑梦团队打造的航空航天科普体验，纸桥承重、弹弓纸飞机、气体压强探究等七大物理实验课堂。",
    "fee": "公益免费",
    "source": "南京科技馆",
    "family_friendly": True
})

activities.append({
    "title": "南大匡亚明学院交叉学科开放日",
    "venue": "南京大学仙林校区匡亚明学院",
    "city": "nanjing",
    "start_date": "2026-07-25",
    "end_date": "2026-07-27",
    "link": "https://dii.nju.edu.cn/c3/f5/c11317a836597/page.htm",
    "description": "面向化学、物理、计算机、生物等基础学科及交叉学科相关专业本科生，学院宣讲、导师面对面交流、学生个人能力展示。",
    "fee": "免费提供用餐",
    "source": "南京大学",
    "family_friendly": True
})

activities.append({
    "title": "南大地球科学与工程学院开放日",
    "venue": "南京大学仙林校区",
    "city": "nanjing",
    "start_date": "2026-07-09",
    "end_date": "2026-07-10",
    "link": "https://m.sohu.com/a/1041504776_121124300/",
    "description": "专家讲座、课题组开放、实验室参观、个人风采展示，了解地球科学前沿研究与地质学A+学科实力。",
    "fee": "免费",
    "source": "搜狐网",
    "family_friendly": True
})

# ============ 9. 更多活动补充 ============

activities.append({
    "title": "2026南京市青少年创意编程大赛优秀作品展",
    "venue": "南京科技馆",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.njstm.org.cn/html/zxdt/kjgdt/?_d_id=0016624667f7708a040908ec621b0e",
    "description": "展示全市青少年创意编程优秀作品，激发孩子对编程与科技创新的兴趣，适合学龄儿童参观学习。",
    "fee": "免费含科技馆门票",
    "source": "南京科技馆",
    "family_friendly": True
})

activities.append({
    "title": "江宁博物馆甲骨文化展",
    "venue": "江宁博物馆",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-10-09",
    "link": "https://k.sina.cn/article_7880068258_1d5b04ca201901bzci.html",
    "description": "刻骨铭心——甲骨文化展，免费无需预约，刷身份证入馆，了解甲骨文与汉字起源历史。",
    "fee": "免费",
    "source": "新浪新闻",
    "family_friendly": True
})

activities.append({
    "title": "六朝博物馆郁郁乎唐唐代文物展",
    "venue": "六朝博物馆",
    "city": "nanjing",
    "start_date": "2026-06-01",
    "end_date": "2026-09-30",
    "link": "http://news.longhoo.net/2026/xuanwu_0611/866482.html",
    "description": "齐聚唐代三大窖藏文物，南京出土唐代文物首次大规模展出，展现民族交融史，暑期周一正常开放。",
    "fee": "门票30元/人",
    "source": "龙虎网",
    "family_friendly": True
})

activities.append({
    "title": "南京海底世界海底奇遇记演出",
    "venue": "南京海底世界",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://news.longhoo.net/2026/xuanwu_0611/866482.html",
    "description": "创新推出沉浸式演出活动，游客化身主角，极地馆上台担任全场指挥官，海豚馆与喜剧演员爆笑飙戏。",
    "fee": "门票180元/人",
    "source": "龙虎网",
    "family_friendly": True
})

activities.append({
    "title": "江宁织造博物馆红楼梦主题研学",
    "venue": "江宁织造博物馆",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://news.longhoo.net/2026/xuanwu_0611/866482.html",
    "description": "以红楼梦为蓝本推出主题研学活动，融入绒花制作等非遗体验，暑期周一正常开放。",
    "fee": "门票30元/人，研学另付费",
    "source": "龙虎网",
    "family_friendly": True
})

activities.append({
    "title": "明孝陵博物馆少儿陶印篆刻课",
    "venue": "明孝陵博物馆",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://news.longhoo.net/2026/xuanwu_0611/866482.html",
    "description": "少儿陶印篆刻爱莲说，实现廉洁教育与非遗传承双效合一，锻炼孩子动手能力与传统文化素养。",
    "fee": "88元/人",
    "source": "龙虎网",
    "family_friendly": True
})

activities.append({
    "title": "国防军事航天科普展",
    "venue": "南京国际展览中心",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662729129090925102/",
    "description": "环湖夏YE主题活动期间举办，前沿科技、大国重器一站式打卡，激发孩子的爱国热情与科学探索兴趣。",
    "fee": "门票80元/人",
    "source": "紫牛新闻",
    "family_friendly": True
})

activities.append({
    "title": "沃普探险乐园森林探险",
    "venue": "玄武湖畔沃普探险乐园",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662729129090925102/",
    "description": "依托树林搭建探险项目，让孩子们在闯关中锻炼胆识与体能，培养探索精神与运动能力。",
    "fee": "128元/人",
    "source": "紫牛新闻",
    "family_friendly": True
})

activities.append({
    "title": "不老村溯溪亲子体验",
    "venue": "浦口区江浦街道不老村",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_7880068258_1d5b04ca201901bzci.html",
    "description": "入园免费，大门直行约500米右手边即可溯溪，水质干净、水流平缓、水位较浅，适合幼童安全游玩。",
    "fee": "免费入园",
    "source": "新浪新闻",
    "family_friendly": True
})

activities.append({
    "title": "羊山湖公园露营玩水",
    "venue": "栖霞区羊山湖公园",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_7880068258_1d5b04ca201901bzci.html",
    "description": "免费超大草坪可露营野餐，湖泊加溪流可钓鱼、捞鱼虾，适合全家周末休闲出游。",
    "fee": "免费",
    "source": "新浪新闻",
    "family_friendly": True
})

activities.append({
    "title": "汤山直立人化石遗址博物馆研学",
    "venue": "江宁汤山直立人化石遗址博物馆",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663510578668831286/",
    "description": "探究远古地质与人类起源，了解南京直立人化石发现历史，适合开展地质考古主题研学。",
    "fee": "门票60元/人",
    "source": "人民网",
    "family_friendly": True
})

activities.append({
    "title": "高淳红色话剧染坊展演",
    "venue": "高淳漆桥老街谦泰染坊",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://dsb.nanjing.gov.cn/gzdt/gqdt/gcq/202607/t20260706_5871753.html",
    "description": "改编自高淳本土革命先烈真实事迹的原创红色话剧，在漆桥老街实景演出，开展沉浸式红色研学教育。",
    "fee": "88元/人",
    "source": "南京党史办",
    "family_friendly": True
})

# 去重
new_activities = []
for act in activities:
    if act['title'] not in existing_titles:
        new_activities.append(act)
    else:
        print(f"重复: {act['title']}")

print(f"\n新增活动数: {len(new_activities)}")

output_path = os.path.join(os.path.dirname(__file__), 'real_activities_nanjing_batch4.json')
with open(output_path, 'w', encoding='utf-8') as fp:
    json.dump(new_activities, fp, ensure_ascii=False, indent=2)

print(f"已保存到: {output_path}")
