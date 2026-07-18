import json
import os

output_path = os.path.join(os.path.dirname(__file__), 'real_activities_nanjing_batch4.json')
with open(output_path, 'r') as fp:
    current_activities = json.load(fp)

print(f"当前活动数: {len(current_activities)}")

existing_titles = set(item['title'] for item in current_activities)

# 读取所有现有活动标题用于去重
for f in ['real_activities_nanjing.json', 'real_activities_nanjing_batch2.json', 'real_activities_nanjing_batch3.json']:
    path = os.path.join(os.path.dirname(__file__), f)
    if os.path.exists(path):
        with open(path, 'r') as fp:
            data = json.load(fp)
            for item in data:
                existing_titles.add(item['title'])

print(f"所有现有标题数: {len(existing_titles)}")

more_activities = []

# ============ 补充更多文化馆/图书馆活动 ============

# 栖霞区更多活动
more_activities.append({
    "title": "栖霞区小机器人讲科学杠杆课",
    "venue": "栖霞街道阅山社区",
    "city": "nanjing",
    "start_date": "2026-07-14",
    "end_date": "2026-07-14",
    "link": "http://m.toutiao.com/group/7657380793634800155/",
    "description": "跟着小机器人粉刷墙壁，在踩跷跷板的场景里解锁杠杆原理，手作环节DIY投石车，亲手调试支点位置，感受力臂长短的秘密。",
    "fee": "免费",
    "source": "栖霞文旅",
    "family_friendly": True
})

more_activities.append({
    "title": "双语系列一起认识图书馆",
    "venue": "西岗街道仙林湖社区",
    "city": "nanjing",
    "start_date": "2026-07-15",
    "end_date": "2026-07-15",
    "link": "http://m.toutiao.com/group/7657380793634800155/",
    "description": "以中英双语绘本为引，带孩子走进图书的世界，从图书演变史到杂志出版全流程，读懂书背后的故事，手作环节自制迷你书。",
    "fee": "免费",
    "source": "栖霞文旅",
    "family_friendly": True
})

more_activities.append({
    "title": "小小CEO系列努力付出终有回报",
    "venue": "马群街道花岗社区",
    "city": "nanjing",
    "start_date": "2026-07-15",
    "end_date": "2026-07-15",
    "link": "http://m.toutiao.com/group/7657380793634800155/",
    "description": "共读绘本秋天的礼物，笨笨熊找秋天礼物的过程就是一分耕耘一分收获的具象化表达，手作用真实种子拼贴创作。",
    "fee": "免费",
    "source": "栖霞文旅",
    "family_friendly": True
})

more_activities.append({
    "title": "江南茶事美学与非遗技艺讲座",
    "venue": "泰康之家苏园",
    "city": "nanjing",
    "start_date": "2026-07-23",
    "end_date": "2026-07-23",
    "link": "http://m.toutiao.com/group/7657380793634800155/",
    "description": "二十四节气与茶的不解之缘，从雨生百谷到夏满芒夏，每一杯茶里都藏着时节的味道，走进节气与茶事交织的美学世界。",
    "fee": "免费",
    "source": "栖霞文旅",
    "family_friendly": True
})

# 秦淮区更多活动
more_activities.append({
    "title": "秦淮区七彩童年创意美术课",
    "venue": "秦淮区文化馆",
    "city": "nanjing",
    "start_date": "2026-07-12",
    "end_date": "2026-07-16",
    "link": "http://m.toutiao.com/group/7655674750219321919/",
    "description": "面向6-12岁儿童的创意美术课程，水彩、版画、黏土手工多种形式，激发孩子想象力与创造力，培养艺术审美。",
    "fee": "公益免费",
    "source": "秦淮文旅",
    "family_friendly": True
})

more_activities.append({
    "title": "秦淮区七彩童年少儿合唱团",
    "venue": "秦淮区文化馆小剧场",
    "city": "nanjing",
    "start_date": "2026-07-15",
    "end_date": "2026-07-25",
    "link": "http://m.toutiao.com/group/7655674750219321919/",
    "description": "少儿声乐启蒙与合唱训练，学习基础发声技巧与合唱配合，培养孩子的音乐素养与团队协作能力。",
    "fee": "公益免费",
    "source": "秦淮文旅",
    "family_friendly": True
})

more_activities.append({
    "title": "秦淮区七彩童年少儿舞蹈班",
    "venue": "秦淮区文化馆舞蹈房",
    "city": "nanjing",
    "start_date": "2026-07-18",
    "end_date": "2026-07-28",
    "link": "http://m.toutiao.com/group/7655674750219321919/",
    "description": "少儿中国舞基础训练，学习舞蹈基本功与简单剧目，培养孩子的身体协调性与艺术表现力。",
    "fee": "公益免费",
    "source": "秦淮文旅",
    "family_friendly": True
})

# 更多公益托管
more_activities.append({
    "title": "建邺区莲花嘉园社区暑托班",
    "venue": "建邺区莲花嘉园社区",
    "city": "nanjing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-20",
    "link": "http://www.njdaily.cn/news/2026/0716/8480558748823161574.html",
    "description": "面向双职工家庭子女的公益托管服务，包含课业辅导、兴趣课程、户外活动等，解决家长暑期看护难题。",
    "fee": "公益免费",
    "source": "南京日报",
    "family_friendly": True
})

more_activities.append({
    "title": "雨花台区西善桥街道红韵润心研学",
    "venue": "江苏省方志馆、雨花万象天地",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.njyh.gov.cn/ywdt/jdyq/202604/t20260421_5827593.html",
    "description": "带领少年儿童走进红色场馆、浸润书香文化，在行走中铭记解放荣光，在实践中赓续红色血脉。",
    "fee": "公益免费",
    "source": "雨花台区人民政府",
    "family_friendly": True
})

more_activities.append({
    "title": "江宁J6产业园暑托班",
    "venue": "江宁区J6产业园",
    "city": "nanjing",
    "start_date": "2026-07-10",
    "end_date": "2026-08-20",
    "link": "http://www.njdaily.cn/news/2026/0716/8480558748823161574.html",
    "description": "园区企业职工子女暑托班，提供安全看护、课业辅导、兴趣培养等服务，让职工安心工作。",
    "fee": "公益免费",
    "source": "南京日报",
    "family_friendly": True
})

# 更多博物馆/科技馆
more_activities.append({
    "title": "南京城墙博物馆暑期延时开放",
    "venue": "南京城墙博物馆",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_7880068258_1d5b04ca201901bzci.html",
    "description": "位于中华门瓮城东侧，有互动展示和创意城砖展厅，让历史变得生动有趣，暑期周五至周日延时开放至20:00。",
    "fee": "免费免预约",
    "source": "新浪新闻",
    "family_friendly": True
})

more_activities.append({
    "title": "南京云锦博物馆暑期参观",
    "venue": "南京云锦博物馆",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_7880068258_1d5b04ca201901bzci.html",
    "description": "免费参观了解国家级非遗云锦织造技艺，观看大花楼木织机现场操作，感受传统织锦工艺的精妙绝伦。",
    "fee": "免费",
    "source": "新浪新闻",
    "family_friendly": True
})

more_activities.append({
    "title": "南京市规划建设展览馆暑期参观",
    "venue": "南京市规划建设展览馆",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_7880068258_1d5b04ca201901bzci.html",
    "description": "玄武湖边的小众展馆，免费且无需预约，即到即参观，了解南京城市规划发展历史与未来蓝图。",
    "fee": "免费",
    "source": "新浪新闻",
    "family_friendly": True
})

more_activities.append({
    "title": "梅园新村纪念馆红色研学",
    "venue": "梅园新村纪念馆",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://news.longhoo.net/2026/xuanwu_0611/866482.html",
    "description": "聚焦红色教育，观展文物史料的同时学习红色雕塑和保密故事，走进革命先辈的那段峥嵘岁月。",
    "fee": "免费",
    "source": "龙虎网",
    "family_friendly": True
})

more_activities.append({
    "title": "孙中山铜像重塑专题展",
    "venue": "孙中山纪念馆",
    "city": "nanjing",
    "start_date": "2026-06-01",
    "end_date": "2026-09-30",
    "link": "http://news.longhoo.net/2026/xuanwu_0611/866482.html",
    "description": "了解孙中山先生的革命事迹与铜像历史，开展爱国主义教育，适合带孩子进行革命传统教育。",
    "fee": "免费",
    "source": "龙虎网",
    "family_friendly": True
})

more_activities.append({
    "title": "南京抗日航空烈士纪念馆主题展",
    "venue": "南京抗日航空烈士纪念馆",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-10-31",
    "link": "http://news.longhoo.net/2026/xuanwu_0611/866482.html",
    "description": "纪念台湾光复80周年主题展，了解抗日航空烈士的英勇事迹，开展爱国主义教育。",
    "fee": "免费",
    "source": "龙虎网",
    "family_friendly": True
})

# 更多青少年宫活动
more_activities.append({
    "title": "青少年宫幼儿暑托班",
    "venue": "南京市青少年宫马台街总部",
    "city": "nanjing",
    "start_date": "2026-07-10",
    "end_date": "2026-08-20",
    "link": "https://www.nqsng.cn/qsng/website/web_v2/index.html",
    "description": "专为学龄前儿童设计的暑托班，包含趣味游戏、绘本阅读、手工创意、音乐律动等丰富活动。",
    "fee": "1980元/月",
    "source": "南京市青少年宫",
    "family_friendly": True
})

more_activities.append({
    "title": "青少年宫三晋知行古建研学营",
    "venue": "山西",
    "city": "nanjing",
    "start_date": "2026-07-20",
    "end_date": "2026-07-25",
    "link": "https://www.nqsng.cn/qsng/website/web_v2/index.html",
    "description": "探秘梁林古建与晋商薪火，走进山西感受中国古建筑的魅力，了解晋商文化历史。",
    "fee": "3280元/人",
    "source": "南京市青少年宫",
    "family_friendly": True
})

more_activities.append({
    "title": "全国青少年宫红色基因主题教育活动",
    "venue": "南京市青少年宫",
    "city": "nanjing",
    "start_date": "2026-07-15",
    "end_date": "2026-08-15",
    "link": "https://www.nqsng.cn/qsng/website/web_v2/index.html",
    "description": "五城联动的红色基因主题教育实践活动，通过红色研学、主题宣讲、实践体验等形式传承红色基因。",
    "fee": "公益免费",
    "source": "南京市青少年宫",
    "family_friendly": True
})

more_activities.append({
    "title": "青少年宫海棠小天使才艺展示",
    "venue": "南京市青少年宫青春剧场",
    "city": "nanjing",
    "start_date": "2026-07-20",
    "end_date": "2026-08-10",
    "link": "https://www.nqsng.cn/qsng/website/web_v2/index.html",
    "description": "南京市第十八届海棠小天使才艺展示活动复评，声乐、舞蹈、器乐、语言表演等多种才艺展示。",
    "fee": "免费报名",
    "source": "南京市青少年宫",
    "family_friendly": True
})

# 更多景区活动
more_activities.append({
    "title": "银杏湖乐园水世界暑期开放",
    "venue": "江宁银杏湖乐园",
    "city": "nanjing",
    "start_date": "2026-06-20",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663510578668831286/",
    "description": "水上乐园焕新升级，多种水上游乐设施，造浪池、漂流河、水滑梯，夏日消暑亲子游玩好去处。",
    "fee": "门票260元/人",
    "source": "人民网",
    "family_friendly": True
})

more_activities.append({
    "title": "汤山龙尚村夏日泳池派对",
    "venue": "江宁汤山龙尚村",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663510578668831286/",
    "description": "夏日限定民宿泳池派对，在青山环抱中戏水狂欢，享受清凉夏日与乡村度假的双重乐趣。",
    "fee": "按民宿价格",
    "source": "人民网",
    "family_friendly": True
})

more_activities.append({
    "title": "龙尚度假两日游",
    "venue": "江宁汤山龙尚村",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663510578668831286/",
    "description": "萌宠互动、果蔬采摘、草坪露营、音乐轰趴等特色项目，两天一夜深度体验乡村度假生活。",
    "fee": "588元/人起",
    "source": "人民网",
    "family_friendly": True
})

more_activities.append({
    "title": "江宁横溪红星基地咖啡山水休闲",
    "venue": "江宁横溪红星基地",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7663510578668831286/",
    "description": "将咖啡文化与山水风光巧妙融合，成为消暑休闲新选择，适合亲子家庭周末休闲度假。",
    "fee": "免费入园",
    "source": "人民网",
    "family_friendly": True
})

more_activities.append({
    "title": "云水涧亲子度假区",
    "venue": "江宁云水涧",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1032504454_121106832/",
    "description": "专为亲子出游打造的休闲度假区，露天泳池可供消暑玩水，摩托快艇驰骋湖面，各类水上项目齐备。",
    "fee": "门票68元/人",
    "source": "南京妇联",
    "family_friendly": True
})

more_activities.append({
    "title": "水墨大埝暑期亲子游",
    "venue": "江北新区水墨大埝",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1032504454_121106832/",
    "description": "骑行绿道、大埝水库亲水、萌宠互动、山野露营打卡，山野清风相伴，亲子骑行好去处。",
    "fee": "门票40元/人",
    "source": "南京妇联",
    "family_friendly": True
})

more_activities.append({
    "title": "金牛湖水上运动体验",
    "venue": "六合金牛湖",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1032504454_121106832/",
    "description": "水上卡丁车、快艇、帆船、桨板等多种水上运动项目，在金牛湖面上体验速度与激情。",
    "fee": "80元/项起",
    "source": "南京妇联",
    "family_friendly": True
})

# 更多高校/研学活动
more_activities.append({
    "title": "南京农业大学校园开放日",
    "venue": "南京农业大学卫岗校区",
    "city": "nanjing",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "https://js.ifeng.com/c/8tb6oidwiq5",
    "description": "百年名校校园参观，金陵旧书市集期间特别开放，感受农业高校的学术氛围与校园风光。",
    "fee": "免费",
    "source": "凤凰网江苏",
    "family_friendly": True
})

more_activities.append({
    "title": "金陵旧书市集淘书寻宝",
    "venue": "南京各大高校",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://js.ifeng.com/c/8tb6oidwiq5",
    "description": "新华书店、凤凰书城、先锋书店等知名书商齐聚，绝版古书、怀旧绘本、专业好书、高颜值文创琳琅满目。",
    "fee": "免费入场",
    "source": "凤凰网江苏",
    "family_friendly": True
})

more_activities.append({
    "title": "南航集成电路学院夏令营",
    "venue": "南京航空航天大学江宁校区",
    "city": "nanjing",
    "start_date": "2026-07-09",
    "end_date": "2026-07-10",
    "link": "https://m.gaodun.com/baoyan/1782098.html",
    "description": "集成电路馆及实验室参观、导师面对面交流、名师讲座、学长学姐座谈，了解航天芯片特色研究方向。",
    "fee": "免费提供用餐",
    "source": "高顿教育",
    "family_friendly": True
})

more_activities.append({
    "title": "南大现代工学院优秀本科生开放日",
    "venue": "南京大学仙林校区",
    "city": "nanjing",
    "start_date": "2026-07-08",
    "end_date": "2026-07-10",
    "link": "http://m.toutiao.com/group/7663369688902074921/",
    "description": "学院宣讲、课题组开放、实验室参观、个人风采展示，来自80余所高校的300余名学生齐聚南大交流。",
    "fee": "免费",
    "source": "今日头条",
    "family_friendly": True
})

# 更多乡村游活动
more_activities.append({
    "title": "溧水石臼湖落日观景骑行",
    "venue": "溧水区石臼湖",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1032504454_121106832/",
    "description": "沿湖悠闲骑行，驻足东岸落日餐厅赏绝美落日、故禾咖啡慢享湖畔时光，亲子骑行赏景两不误。",
    "fee": "免费",
    "source": "南京妇联",
    "family_friendly": True
})

more_activities.append({
    "title": "溧水悦野轻奢营地亲子游",
    "venue": "溧水区悦野轻奢营地",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1032504454_121106832/",
    "description": "草坪开阔，围炉烤肉香气四溢，亲子嬉水撒欢，山野清风相伴，惬意十足的亲子露营体验。",
    "fee": "198元/人起",
    "source": "南京妇联",
    "family_friendly": True
})

more_activities.append({
    "title": "九龙湖温泉营地露营烧烤",
    "venue": "江宁九龙湖温泉营地",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.nanjing.gov.cn/zgnjsjb/jrtt/202607/t20260714_5876186.html",
    "description": "露营烧烤套餐，毕业生八折、在校师生九折，星空露营、温泉体验，适合家庭周末度假。",
    "fee": "268元/人起",
    "source": "南京市人民政府",
    "family_friendly": True
})

more_activities.append({
    "title": "野灶集营地毕业聚餐",
    "venue": "江宁野灶集营地",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.nanjing.gov.cn/zgnjsjb/jrtt/202607/t20260714_5876186.html",
    "description": "6-10人同窗聚餐，凭毕业证免费使用帐篷包间3小时，户外烧烤、团建活动，适合学生团体。",
    "fee": "人均88元起",
    "source": "南京市人民政府",
    "family_friendly": True
})

more_activities.append({
    "title": "六合云之行滑翔伞体验",
    "venue": "六合金牛湖滑翔伞基地",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.nanjing.gov.cn/zgnjsjb/jrtt/202607/t20260714_5876186.html",
    "description": "高空俯瞰沿江风光，毕业生特惠299元，毗邻的马术营地骑乘培训享八折，极限运动爱好者的天堂。",
    "fee": "原价699元",
    "source": "南京市人民政府",
    "family_friendly": True
})

more_activities.append({
    "title": "江宁方山玩水派对",
    "venue": "江宁方山风景区",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.nanjing.gov.cn/zgnjsjb/jrtt/202607/t20260714_5876186.html",
    "description": "39元起轻松解锁夏日戏水乐趣，水枪大战、泡泡派对、水上闯关，夏日消暑亲子游玩首选。",
    "fee": "39元/人起",
    "source": "南京市人民政府",
    "family_friendly": True
})

# 更多商业综合体活动
more_activities.append({
    "title": "新街口商圈暑期亲子嘉年华",
    "venue": "新街口商圈",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7648846342216319507/",
    "description": "市中心C位地铁1/2号线交汇，商场林立、美食遍地，多家商场推出暑期亲子活动与优惠。",
    "fee": "免费入场",
    "source": "今日头条",
    "family_friendly": True
})

more_activities.append({
    "title": "先锋书店暑期亲子阅读季",
    "venue": "先锋书店各门店",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://js.ifeng.com/c/8tb6oidwiq5",
    "description": "暑期亲子阅读季活动，绘本共读、作家分享、手作工坊等多种形式，培养孩子阅读习惯。",
    "fee": "免费入场",
    "source": "凤凰网江苏",
    "family_friendly": True
})

more_activities.append({
    "title": "凤凰书城暑期少儿读书节",
    "venue": "凤凰国际书城",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.weibo.cn/detail/5305757207626381",
    "description": "暑期少儿读书节，童书优惠、作家签售、阅读分享会等活动，打造书香夏日。",
    "fee": "免费入场",
    "source": "小译林童书",
    "family_friendly": True
})

more_activities.append({
    "title": "华采天地暑期亲子嘉年华",
    "venue": "河西华采天地",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1025960937_121124711/",
    "description": "西西弗书店历史喵主题展、多家亲子品牌暑期优惠、儿童游乐区，一站式亲子购物休闲。",
    "fee": "免费入场",
    "source": "悟空看非遗",
    "family_friendly": True
})

more_activities.append({
    "title": "南京海底世界海豚表演暑期加场",
    "venue": "南京海底世界",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://news.longhoo.net/2026/xuanwu_0611/866482.html",
    "description": "暑期海豚表演加场，海底奇遇记沉浸式演出，极地馆、海豚馆多场馆联动，海洋生物零距离接触。",
    "fee": "门票180元/人",
    "source": "龙虎网",
    "family_friendly": True
})

more_activities.append({
    "title": "园博园苏韵十三园暑期游",
    "venue": "江苏园博园",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_7880068258_1d5b04ca201901bzci.html",
    "description": "白天多个江苏城市展园免费开放，不用预约，适合citywalk和亲子遛娃，自驾首选。",
    "fee": "基础门票免费",
    "source": "新浪新闻",
    "family_friendly": True
})

more_activities.append({
    "title": "浦口不老村亲子陶艺体验",
    "venue": "浦口区不老村",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_7880068258_1d5b04ca201901bzci.html",
    "description": "村内有农家菜、咖啡店、亲子陶艺等配套，溯溪玩水后体验陶艺创作，丰富亲子行程。",
    "fee": "88元/人起",
    "source": "新浪新闻",
    "family_friendly": True
})

more_activities.append({
    "title": "江宁龙山水库露营烧烤",
    "venue": "江宁区龙山水库",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_7880068258_1d5b04ca201901bzci.html",
    "description": "免费露营、明火烧烤，孩子玩水、大人烧烤两不误，市区开车约45分钟，家庭周末出游好去处。",
    "fee": "免费",
    "source": "新浪新闻",
    "family_friendly": True
})

more_activities.append({
    "title": "高淳慢城国际慢城亲子游",
    "venue": "高淳国际慢城",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.njdaily.cn/news/2026/0713/8480558336506310023.html",
    "description": "中国首个国际慢城，田园风光、慢生活体验，亲子骑行、农家乐、采摘，享受慢节奏的乡村生活。",
    "fee": "免费入园",
    "source": "南京日报",
    "family_friendly": True
})

more_activities.append({
    "title": "浦口老母猪沟翡翠湖探秘",
    "venue": "浦口区老山林场",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_7880068258_1d5b04ca201901bzci.html",
    "description": "被称为翡翠湖，湖水碧绿，小溪水质清澈，是夏天玩水的好去处，老山小众秘境探险。",
    "fee": "免费",
    "source": "新浪新闻",
    "family_friendly": True
})

more_activities.append({
    "title": "江苏园博园酷野烘焙市集",
    "venue": "江苏园博园",
    "city": "nanjing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_7879923025_1d5ae155101901sy9u.html",
    "description": "艾草曲奇、粽形马卡龙亲子手作，全域骑行、每晚免费山水烟花秀，抱抱萌宠乐园适配亲子。",
    "fee": "门票118元/人",
    "source": "新浪新闻",
    "family_friendly": True
})

# 去重
new_count = 0
for act in more_activities:
    if act['title'] not in existing_titles:
        current_activities.append(act)
        existing_titles.add(act['title'])
        new_count += 1
    else:
        print(f"重复: {act['title']}")

print(f"\n新增活动数: {new_count}")
print(f"总活动数: {len(current_activities)}")

with open(output_path, 'w', encoding='utf-8') as fp:
    json.dump(current_activities, fp, ensure_ascii=False, indent=2)

print(f"已保存到: {output_path}")
