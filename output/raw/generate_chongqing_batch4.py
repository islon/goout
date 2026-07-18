import json
from datetime import datetime

activities = []

# ===== 1. 公益托管/暑期托管班（20条）=====

activities.append({
    "title": "重庆市'共青团·伙伴计划'2026年暑假公益托管营",
    "venue": "全市各区县1300余个托管点位",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "http://www.cq.gov.cn/zwgk/zfxxgkml/zdlyxxgk/jy1/jy/202607/t20260701_15788870.html",
    "description": "市级重点民生实事项目，全市39个区县开设1300余个托管点位，为6-12岁少年儿童提供免费公益托管服务，涵盖作业辅导、红色教育、安全自护科普、趣味手工、心理陪伴、非遗课程等多元内容，采用'专业教师+志愿者'双轨模式，切实解决暑期'看护难'问题。",
    "fee": "免费",
    "source": "重庆市人民政府",
    "family_friendly": True
})

activities.append({
    "title": "万州区2026年暑假公益托管营",
    "venue": "万州区26个城乡公益托管点位",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-28",
    "link": "http://dpaper.sxcm.net/sxdsb/html/202607/01/content_128497.html",
    "description": "万州区布局26个城乡公益托管点位，覆盖镇乡街道、村社区、青少年宫等多元阵地，提供作业辅导、红色教育、安全自护科普、趣味手工、心理陪伴、非遗课程等丰富公益课程，每期5天，每班不超过30人，全程公益免费。",
    "fee": "免费",
    "source": "三峡都市报",
    "family_friendly": True
})

activities.append({
    "title": "涪陵区'共青团·伙伴计划'暑假公益托管营",
    "venue": "涪陵区敦仁街道、荔枝街道、江东街道等7个点位",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "https://m.sohu.com/a/1047164994_121106884/",
    "description": "涪陵区暑假公益托管营实行'学业辅导+素质拓展'多维课程模式，涵盖课业辅导、五育培养、心理团辅、体育锻炼等内容，开设大量兴趣课堂、安全课堂、健康课堂，面向6-12岁少年儿童，优先保障困境儿童、留守儿童及新就业群体子女。",
    "fee": "免费",
    "source": "共青团涪陵区委",
    "family_friendly": True
})

activities.append({
    "title": "合川区'合你童行'暑期公益托管班",
    "venue": "合川区30个镇街48个托管班",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "https://biz.ifeng.com/c/8umtowsDg40",
    "description": "共青团合川区委、合川区教委利用青少年活动中心、社区居委会活动室等场地开办48个暑期公益托管班，覆盖30个镇街，为少年儿童提供暑期看护、课业辅导及素质拓展服务，被市民亲切称为'官方带娃'。",
    "fee": "免费",
    "source": "新华社",
    "family_friendly": True
})

activities.append({
    "title": "南岸区2026年暑假公益托管营",
    "venue": "南岸区38个托管点位",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "http://m.toutiao.com/group/7663083537611948585/",
    "description": "南岸区设38个点位、开展116期活动，覆盖12个街镇，服务小学生3500余人。采用'学业辅导+素质拓展'模式，课业辅导答疑解惑，科普手工趣味纷呈，护航孩子们清凉度夏、畅游学海。",
    "fee": "免费",
    "source": "重庆日报",
    "family_friendly": True
})

activities.append({
    "title": "渝中区2026年暑假公益托管营",
    "venue": "渝中区11个街道26个托管点位",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "https://admin.cq.gov.cn/zwgk/zfxxgkml/zdlyxxgk/jy1/jy/202607/t20260708_15807343.html",
    "description": "渝中区在全区11个街道共设置26个托管点位，计划开展149期公益托管班，预计覆盖未成年人4000余人。以公益性看护为主，兼顾学业辅导与兴趣培育，同步覆盖安全自护、红色思政、科普阅读、文体活动、心理健康等多元课程。",
    "fee": "免费",
    "source": "重庆市渝中区人民政府",
    "family_friendly": True
})

activities.append({
    "title": "海棠溪街道御泰社区暑期公益托管服务",
    "venue": "南岸区海棠溪街道御泰社区党群服务中心",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "http://m.toutiao.com/group/7662066665571598867/",
    "description": "御泰社区暑期少年儿童公益托管服务面向辖区6-14岁少年儿童开放，优先保障特殊困难家庭子女。服务时间为每周一至周五9:30至16:30，提供作业辅导、红色宣讲、手工绘画、安全教育等课程，物业接力护送服务延伸至'最后一百米'。",
    "fee": "免费",
    "source": "南岸区海棠溪街道",
    "family_friendly": True
})

activities.append({
    "title": "磁器口街道凤凰山社区'青仔益起来'暑期公益托管班",
    "venue": "沙坪坝区磁器口街道凤凰山社区微型少年宫",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "https://www.cqspb.gov.cn/zj/cqkjd_64377/sy_64378/xzdt_64380/202607/t20260714_15820594.html",
    "description": "凤凰山社区微型少年宫暑期公益托管班，提供作业辅导、课外阅读等基础服务，帮助孩子高效完成暑期作业，培养良好学习习惯，还融入安全教育、趣味手工、科普小课堂等特色活动，兼顾知识性与趣味性。",
    "fee": "免费",
    "source": "沙坪坝区磁器口街道办事处",
    "family_friendly": True
})

activities.append({
    "title": "江津区四面山镇青少年公益托管班",
    "venue": "江津区四面山镇文化站",
    "city": "chongqing",
    "start_date": "2026-07-20",
    "end_date": "2026-08-21",
    "link": "http://news.cqjjnet.com/web/aritcle/1523734206641029120/web/content_1523734206641029120.html",
    "description": "四面山镇青少年公益托管班提供课业辅导、兴趣培养、安全看护一站式服务，解决避暑家庭带娃难题，让家长安心度假，孩子快乐成长。位于四面山核心景区，避暑托管两不误。",
    "fee": "免费",
    "source": "江津区融媒体中心",
    "family_friendly": True
})

activities.append({
    "title": "涪陵区武陵山镇暑校",
    "venue": "涪陵区武陵山镇九年制学校",
    "city": "chongqing",
    "start_date": "2026-07-13",
    "end_date": "2026-08-14",
    "link": "https://m.sohu.com/a/1049282112_121106884/",
    "description": "涪陵区青少年活动中心在武陵山镇开设暑期分校，开设魔方、书法美术、播音主持、体能训练、机器人编程、作业辅导、幼小衔接等课程，专业老师全程护航，清凉避暑又学本领，让孩子在山林间度过充实假期。",
    "fee": "收费",
    "source": "共青团涪陵区委",
    "family_friendly": True
})

activities.append({
    "title": "涪陵区大木镇暑校",
    "venue": "涪陵区大木镇中心小学校",
    "city": "chongqing",
    "start_date": "2026-07-13",
    "end_date": "2026-08-14",
    "link": "https://m.sohu.com/a/1049282112_121106884/",
    "description": "大木镇暑校由共青团涪陵区委联合相关部门举办，开设魔方、书法美术、播音主持、体能训练、机器人编程、作业辅导、幼小衔接等多元课程，依托大木镇优质避暑资源，让孩子在清凉山水中学习成长。",
    "fee": "收费",
    "source": "共青团涪陵区委",
    "family_friendly": True
})

activities.append({
    "title": "重庆市工会2026年夏令营",
    "venue": "奉节中国三峡研学大本营、云阳山地综合实训基地、酉阳桃花源营地",
    "city": "chongqing",
    "start_date": "2026-07-13",
    "end_date": "2026-07-17",
    "link": "https://m.sohu.com/a/1051601538_121106884/",
    "description": "重庆市总工会主办的职工子女夏令营，在奉节、云阳、酉阳三地同步开展，为900余名一线职工子女打造集红色教育、自然探索、文化传承、团队成长于一体的多彩暑期课堂，精准关爱困难职工、新就业形态劳动者等群体子女。",
    "fee": "免费",
    "source": "重庆市总工会",
    "family_friendly": True
})

activities.append({
    "title": "合川公司'乐学成长·安心一夏'职工子女工会夏令营",
    "venue": "合川区合川公司营地",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-14",
    "link": "http://m.toutiao.com/group/7662324714190275107/",
    "description": "为期40天的职工子女夏令营，面向5-12岁职工子女，以基本看护服务为主，辅导孩子完成暑假作业，每天安排课间操、眼保健操、跳绳、乒乓球等体育锻炼，开设书法、手工创意、科学小实验、实践课程等特色课程。",
    "fee": "免费",
    "source": "合川公司工会",
    "family_friendly": True
})

activities.append({
    "title": "江津公司'电亮童心 相伴成长'职工子女夏令营",
    "venue": "江津区江津公司营地",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-14",
    "link": "http://m.toutiao.com/group/7662324714190275107/",
    "description": "以'托管+教育+实践'创新模式，为近50名职工子女打造集学习、体验、成长于一体的暑期乐园。开设广播体操、乒乓球、跳绳等体育活动，以及作业辅导、创意美术、趣味阅读、手工制作等多元化内容。",
    "fee": "免费",
    "source": "江津公司工会",
    "family_friendly": True
})

activities.append({
    "title": "璧山公司暑期职工子女工会夏令营",
    "venue": "璧山区璧山公司营地",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-14",
    "link": "http://m.toutiao.com/group/7662324714190275107/",
    "description": "配备专人看护管理，合理规划每日作息，设置暑期作业辅导、绘本阅读、手工绘画、趣味小游戏等丰富活动，兼顾学习与趣味，让孩子们度过充实又安全的假期，解决职工暑期子女'看护难'问题。",
    "fee": "免费",
    "source": "璧山公司工会",
    "family_friendly": True
})

activities.append({
    "title": "忠县公司2026年职工子女工会夏令营",
    "venue": "忠县忠县公司营地",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-14",
    "link": "http://m.toutiao.com/group/7662324714190275107/",
    "description": "面向5-12岁职工子女，构建'托管+实践'管理模式。除基础作业辅导外，开设手工实践、电力科普小实验、阅读写作等特色课程，增设社会实践活动，带领孩子们参观供电所、营业厅，了解电力生产供应流程。",
    "fee": "免费",
    "source": "忠县公司工会",
    "family_friendly": True
})

activities.append({
    "title": "两江新区'戎耀'夏令营",
    "venue": "涪陵区武陵山大裂谷夏令营营地",
    "city": "chongqing",
    "start_date": "2026-07-04",
    "end_date": "2026-08-30",
    "link": "http://m.toutiao.com/group/7659323710909792831/",
    "description": "由两江新区退役军人志愿服务队指导的暑期夏令营，前往武陵山大裂谷营地，融合红色教育、国防实践与自然探索的成长旅程。通过标准化军事基础训练锤炼自律自强品格，走进自然探秘地质科普知识。",
    "fee": "收费",
    "source": "两江新区退役军人志愿服务队",
    "family_friendly": True
})

activities.append({
    "title": "重庆大学教职工'亲子体育夏令营'",
    "venue": "重庆大学虎溪校园体育中心",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-07-16",
    "link": "http://m.toutiao.com/group/7661858344047280690/",
    "description": "以'亲子同行、健康相伴'为核心理念，涵盖游泳、篮球、乒乓球、羽毛球、网球、匹克球、幼儿体适能七大特色项目，体育学院专业师资全程带队，将运动技巧教学、体能锻炼、安全常识普及融入趣味游戏、团队竞赛、亲子协作任务中。",
    "fee": "收费",
    "source": "重庆大学",
    "family_friendly": True
})

activities.append({
    "title": "万州区总工会职工子女夏令营",
    "venue": "万州区总工会营地",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-07-10",
    "link": "http://www.sxcm.net/web/article/2026/07/06/1523785821773717504/web/content_1523785821773717504.html",
    "description": "万州区总工会聚焦职工暑期子女看护难问题，精心组织20名参营学生开展5天4夜夏令营，研学实践、素质拓展、安全教育、才艺互动一一排进课表，全程专人带队、分组管理、定时打卡、实时报备。",
    "fee": "免费",
    "source": "看万州",
    "family_friendly": True
})

activities.append({
    "title": "高新区财商启蒙特色托管课",
    "venue": "高新区各托管点位",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "http://www.cq.gov.cn/zwgk/zfxxgkml/zdlyxxgk/jy1/jy/202607/t20260701_15788870.html",
    "description": "高新区联动税务局业务骨干，在暑期公益托管中开设财商启蒙特色课，通过动画科普、角色扮演等形式，把财税知识融入到趣味体验课中，提升青少年财商认知，是公益托管中的特色创新课程。",
    "fee": "免费",
    "source": "重庆市人民政府",
    "family_friendly": True
})

# ===== 2. 科技馆/自然博物馆活动（15条）=====

activities.append({
    "title": "重庆科技馆'小科娃 大智慧'暑假科学营",
    "venue": "重庆科技馆A区一楼青少年科学梦工场",
    "city": "chongqing",
    "start_date": "2026-07-20",
    "end_date": "2026-08-14",
    "link": "https://m.sohu.com/a/1041001423_121106884/",
    "description": "开启太空'筑巢'计划，特邀天文科普专家，通过科学实验、科技探索、创意搭建，让太空想象变为现实。深入科技馆宇航科技展厅，围绕八大行星、航天器、星球家园等，融合天文学、力学、电磁学等多学科知识。",
    "fee": "收费（1580元/人/期）",
    "source": "重庆科技馆",
    "family_friendly": True
})

activities.append({
    "title": "重庆科技馆'小小科技辅导员'培训活动",
    "venue": "重庆科技馆",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1007342736_121106884/",
    "description": "聚焦'健康中国'新主题，围绕'合理膳食''科学运动''心理健康'三大方向，开设科普讲解训练营，课程包括专家小课堂、语言表达培训、讲解技能技巧、展品知识、科学实验等内容，培养青少年科学思维与表达能力。",
    "fee": "免费",
    "source": "重庆科技馆",
    "family_friendly": True
})

activities.append({
    "title": "重庆自然博物馆'神兽之夜'恐龙过夜营",
    "venue": "重庆自然博物馆恐龙展厅",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://qa.trip.com/moments/detail/chongqing-158-144515029",
    "description": "6岁以上儿童可独立参加的恐龙过夜营，398元/人，2天1夜。包含3D电影观影、手提灯夜游恐龙厅、恐龙骨架组装、三叶虫化石修复、恐龙厅帐篷搭建过夜、地质早餐、'小小古生物学家'结营证书等丰富内容。",
    "fee": "收费（398元/人）",
    "source": "重庆自然博物馆",
    "family_friendly": True
})

activities.append({
    "title": "重庆自然博物馆'科学之夜'专场活动",
    "venue": "重庆自然博物馆",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.chinanews.com/wap/detail/cht/zw/10631624.shtml",
    "description": "以'星夜自博·点亮科学之光'为主题，融合科普市集、AI恐龙机器人互动、图形化编程、沉浸式自然寻踪任务、原创科普剧及线上直播等多元形式，打造全年龄段参与的夜间沉浸式科普盛宴。",
    "fee": "免费",
    "source": "中国新闻网",
    "family_friendly": True
})

activities.append({
    "title": "重庆自然博物馆雅安-宝兴熊猫夏令营",
    "venue": "四川雅安碧峰峡熊猫基地、邓池沟、蜂桶寨自然保护区",
    "city": "chongqing",
    "start_date": "2026-07-15",
    "end_date": "2026-08-20",
    "link": "https://m.weibo.cn/detail/5310101697071795",
    "description": "重庆自然博物馆携手重庆动物园、重庆自然资源科普馆共同开展的5天4晚暑期夏令营。全脉络溯源路线覆盖碧峰峡熊猫基地+邓池沟+蜂桶寨核心自然保护区，保护区专家授课、专业野外巡护、夜间昆虫灯诱实验、鸟类迁徙观察。",
    "fee": "收费",
    "source": "重庆动物园",
    "family_friendly": True
})

activities.append({
    "title": "重庆自然博物馆'魔术背后的科学'趣味实验课",
    "venue": "重庆科技馆趣味科学实验室",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.cqkjg.cn/web/article/1372793586865922048/web/content_1372793586865922048.html",
    "description": "面向1-6年级学生的45分钟趣味科学实验课程，以魔术表演、趣味实验的方式，介绍日常生活中有关浮力及密度的现象，揭示高分子材料的特性，启迪学生好奇心，培养科学探究能力。",
    "fee": "免费",
    "source": "重庆科技馆",
    "family_friendly": True
})

activities.append({
    "title": "'飞奔月球'科学制作活动",
    "venue": "重庆科技馆宇航科技展厅",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.cqkjg.cn/web/article/1489199942159261696/web/content_1489199942159261696.html",
    "description": "90分钟科学制作活动，面向7-9年级学生。结合宇航科技展厅'绕月飞行模拟器''月球探测体验'等展品，通过月旁起源、玉兔神话传说、探月小分队等情景设置，引导学生了解中国探月工程，制作'月球探测车'。",
    "fee": "免费",
    "source": "重庆科技馆",
    "family_friendly": True
})

activities.append({
    "title": "'一起趣造纸'科学小制作",
    "venue": "重庆科技馆梦工场科学小制作教室",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.cqkjg.cn/web/article/1489199866905059328/web/content_1489199866905059328.html",
    "description": "动手体验古法造纸工艺，了解造纸术的历史演变与科学原理，亲手制作一张属于自己的花草纸，培养孩子的动手能力与传统文化认知，适合亲子共同参与体验。",
    "fee": "免费",
    "source": "重庆科技馆",
    "family_friendly": True
})

activities.append({
    "title": "'万无一湿'科学实验课",
    "venue": "重庆科技馆趣味科学实验室",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.cqkjg.cn/web/article/1372793601822810112/web/content_1372793601822810112.html",
    "description": "趣味科学实验课程，探索表面张力与疏水材料的奥秘，通过神奇的沙不湿水、荷叶效应等实验，让孩子在玩中学，了解材料科学的基础知识，激发对科学的好奇心。",
    "fee": "免费",
    "source": "重庆科技馆",
    "family_friendly": True
})

activities.append({
    "title": "'好玩的偏振片'科学实验课",
    "venue": "重庆科技馆趣味科学实验室",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://www.cqkjg.cn/web/article/1372793595288084480/web/content_1372793595288084480.html",
    "description": "光学主题趣味实验课，通过偏振片的神奇现象，探索光的偏振原理，了解3D眼镜、液晶显示等生活中的偏振应用，培养孩子的科学观察能力与逻辑思维。",
    "fee": "免费",
    "source": "重庆科技馆",
    "family_friendly": True
})

activities.append({
    "title": "重庆自然博物馆博物馆奇妙夜亲子夏令营",
    "venue": "重庆自然博物馆恐龙厅",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.ytszg.com/chongqing/r5293.html",
    "description": "亲子二日夏令营，夜宿重庆自然博物馆恐龙厅，DIY绘制恐龙主题T恤、观看环幕电影、夜游恐龙厅寻宝、学习恐龙骨架知识、三叶虫化石修复、恐龙厅搭建帐篷过夜、观鸟课程、地质早餐，颁发结营证书。",
    "fee": "收费（368元起/人）",
    "source": "重庆青旅",
    "family_friendly": True
})

activities.append({
    "title": "梁平麓渝自然中心'生态影像创作'自然营",
    "venue": "重庆梁平麓渝自然中心、双桂湖国家湿地公园",
    "city": "chongqing",
    "start_date": "2026-07-07",
    "end_date": "2026-07-12",
    "link": "https://m.cq.bendibao.com/xiuxian/165857.shtm",
    "description": "深入双桂湖腹地，用镜头探索隐秘的微观世界、记录广袤的湿地生境、记录乡村的生态变迁，完成一部属于自己的生态纪录短片。适合8-14岁亲子家庭/成人参与。",
    "fee": "收费",
    "source": "重庆本地宝",
    "family_friendly": True
})

activities.append({
    "title": "梁平麓渝自然中心'湿地科学家'养成营",
    "venue": "重庆梁平麓渝自然中心、双桂湖国家湿地公园",
    "city": "chongqing",
    "start_date": "2026-07-14",
    "end_date": "2026-07-19",
    "link": "https://m.cq.bendibao.com/xiuxian/165857.shtm",
    "description": "参与湿地监测与观鸟记录，在麓渝自然中心亲手修复生态池塘，用科学的方法理解自然运行的法则，培养孩子的科学探究精神与环境保护意识，适合10-18岁青少年。",
    "fee": "收费",
    "source": "重庆本地宝",
    "family_friendly": True
})

activities.append({
    "title": "梁平麓渝自然中心自然全科探索营",
    "venue": "重庆梁平麓渝自然中心、双桂湖国家湿地公园",
    "city": "chongqing",
    "start_date": "2026-08-09",
    "end_date": "2026-08-15",
    "link": "https://m.cq.bendibao.com/xiuxian/165857.shtm",
    "description": "在树荫下读一首关于夏天的诗，在湖畔用英语描述飞过的鸟群，在草地上用树枝和石子解一道数学题，把课堂搬进乡村湿地，将学科学习融入自然的每一个角落，适合6-12岁儿童。",
    "fee": "收费",
    "source": "重庆本地宝",
    "family_friendly": True
})

activities.append({
    "title": "梁平麓渝自然中心非遗文化体验营",
    "venue": "重庆梁平麓渝自然中心、双桂湖国家湿地公园",
    "city": "chongqing",
    "start_date": "2026-08-18",
    "end_date": "2026-08-21",
    "link": "https://m.cq.bendibao.com/xiuxian/165857.shtm",
    "description": "画一幅竹帘画，染一次蓝印花布，4天不重样的非遗手作体验，一天学一门老手艺，一天带一件作品回家，让孩子在动手实践中感受传统文化的魅力，适合5-14岁亲子家庭。",
    "fee": "收费",
    "source": "重庆本地宝",
    "family_friendly": True
})

# ===== 3. 欢乐谷/融创文旅城/乐和乐都（12条）=====

activities.append({
    "title": "重庆欢乐谷'夜猫子音乐公园'夏浪狂欢节",
    "venue": "重庆欢乐谷（两江新区礼嘉金渝大道29号）",
    "city": "chongqing",
    "start_date": "2026-07-04",
    "end_date": "2026-08-30",
    "link": "https://www.liangjiang.gov.cn/mixmedia/a/202607/06/WS6a4b5b6ae4b0adfdc81856f1.html",
    "description": "重庆首个音乐主题乐园，推出九大明星艺人、六大音乐舞台、每天百场微醺演艺、五大主题派对，千架无人机星空秀、湖面大秀等内容。58天超长狂欢覆盖整个暑期，夜场运营至22点。",
    "fee": "收费",
    "source": "两江新区官网",
    "family_friendly": True
})

activities.append({
    "title": "重庆玛雅海滩水公园'撒泼一夏 泰浪啦'主题活动",
    "venue": "重庆玛雅海滩水公园（两江新区礼嘉）",
    "city": "chongqing",
    "start_date": "2026-06-13",
    "end_date": "2026-08-31",
    "link": "https://www.liangjiang.gov.cn/mixmedia/a/202607/06/WS6a4b5b6ae4b0adfdc81856f1.html",
    "description": "拥有1万平方米风洞造浪池、双龙水上过山车、超级大喇叭、巨兽碗等大型水上项目，以及10余项亲子戏水设备。三大主题泼水大战、花车巡游、纯正泰式风情演艺持续整个暑期。",
    "fee": "收费",
    "source": "两江新区官网",
    "family_friendly": True
})

activities.append({
    "title": "重庆欢乐谷超级飞侠主题街区",
    "venue": "重庆欢乐谷超级飞侠主题区",
    "city": "chongqing",
    "start_date": "2026-07-04",
    "end_date": "2026-08-30",
    "link": "https://m.weibo.cn/detail/5318816842122480",
    "description": "超级飞侠主题街区亲子出游必打卡，小朋友最爱的动画IP实景呈现，多种亲子互动游乐设施、角色见面会、主题巡游，让孩子和超级飞侠一起冒险，是暑期亲子游玩的热门选择。",
    "fee": "含在门票内",
    "source": "欢乐谷集团",
    "family_friendly": True
})

activities.append({
    "title": "重庆融创文旅城'夏日奇幻潮玩季'",
    "venue": "重庆融创文旅城（沙坪坝区西永）",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1051528117_563335/",
    "description": "奇幻演艺、清凉玩水、潮流夜游、互动体验全都有，涵盖渝乐小镇封神世界沉浸式演艺、国风泼水狂欢、奇趣水世界赛博电音、海世界8大全新场景焕新、热雪奇迹零下6度玩雪，从早到晚玩一整天。",
    "fee": "收费",
    "source": "沙坪坝发布",
    "family_friendly": True
})

activities.append({
    "title": "融创渝乐小镇封神世界沉浸式演艺",
    "venue": "重庆融创渝乐小镇",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1051528117_563335/",
    "description": "封神世界沉浸式演艺、奇幻潮玩大巡游、国风泼水狂欢等精彩内容，从白天嗨到深夜，每一刻都有新惊喜。NPC互动、古风体验、实景演艺，带来沉浸式的封神主题冒险体验。",
    "fee": "收费",
    "source": "沙坪坝发布",
    "family_friendly": True
})

activities.append({
    "title": "融创海世界暑期全新场景焕新",
    "venue": "重庆融创海世界",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1051528117_563335/",
    "description": "海底书屋、企鹅科普区、动态投影墙、小丑鱼香槟塔等8大全新场景，集打卡出片、趣味游玩、科普知识于一体，全家满足。看海豚表演、探秘海底隧道、学习海洋知识，亲子科普好去处。",
    "fee": "收费",
    "source": "沙坪坝发布",
    "family_friendly": True
})

activities.append({
    "title": "融创水世界赛博电音派对",
    "venue": "重庆融创水世界",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1051528117_563335/",
    "description": "赛博电音、焰火空中飞人、AI人机共舞轮番上演，全家戏水闯关、小黄鸭漂流赛、泼水接龙、击球落水等趣味项目，全家组队玩超欢乐，超多水上项目一站式畅玩。",
    "fee": "收费",
    "source": "沙坪坝发布",
    "family_friendly": True
})

activities.append({
    "title": "融创热雪奇迹暑期冰雪体验",
    "venue": "重庆融创热雪奇迹",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1051528117_563335/",
    "description": "逃离山城热浪，开启零下6摄氏度的玩雪之旅，涮火锅、堆雪人、滑雪，解锁冰火两重天的畅快。专业雪道、娱雪区、冰雪主题活动，全家老小都能找到乐趣。",
    "fee": "收费",
    "source": "沙坪坝发布",
    "family_friendly": True
})

activities.append({
    "title": "乐和乐都'野闯计划'夜探动物世界",
    "venue": "重庆永川乐和乐都动物主题乐园",
    "city": "chongqing",
    "start_date": "2026-07-07",
    "end_date": "2026-08-31",
    "link": "https://www.163.com/dy/article/L1T0KHR2053469M5.html",
    "description": "每周五、六、日及节假日晚间开放夜探动物世界，游览鹦鹉馆、犀牛河马馆、松鼠猴馆、树懒馆等特色场馆，沿途设有科普讲解和动物互动，还可以体验放飞萤火虫活动，自然科普亲子互动深度融合。",
    "fee": "收费",
    "source": "上游新闻",
    "family_friendly": True
})

activities.append({
    "title": "乐和乐都'虎山行——勇者之路'沉浸式猛兽徒步",
    "venue": "重庆永川乐和乐都动物主题乐园",
    "city": "chongqing",
    "start_date": "2026-07-07",
    "end_date": "2026-08-31",
    "link": "https://www.163.com/dy/article/L1T0KHR2053469M5.html",
    "description": "依托园区原生山地地貌，打造安全沉浸式的猛兽观赏徒步线路，徒步穿行原生态猛兽区域，与老虎、狮子、黑熊等大型猛兽一网之隔，近距离观赏猛兽自在漫步、觅食休憩的野性姿态。",
    "fee": "收费",
    "source": "上游新闻",
    "family_friendly": True
})

activities.append({
    "title": "乐和乐都水上乐园暑期开放",
    "venue": "重庆永川乐和乐都水上乐园",
    "city": "chongqing",
    "start_date": "2026-06-20",
    "end_date": "2026-08-31",
    "link": "https://m.cq.bendibao.com/tour/154651.shtm",
    "description": "乐和乐都水上乐园暑期开放，一票连续畅玩两天「陆地全园+水上乐园」，多种水上滑梯、造浪池、亲子戏水区，清凉玩水加陆地游乐，打造一站式夏日亲子度假体验。",
    "fee": "收费",
    "source": "重庆本地宝",
    "family_friendly": True
})

activities.append({
    "title": "万州万达广场'小恐龙大冒险'游乐园",
    "venue": "万州万达广场1F连廊",
    "city": "chongqing",
    "start_date": "2026-07-04",
    "end_date": "2026-07-31",
    "link": "https://m.weibo.cn/detail/5321362247783743",
    "description": "恐龙科普课堂、侏罗纪寻宝、一米恐龙图书馆，遛娃打卡圣地。小朋友可以在恐龙主题乐园中学习恐龙知识、参与寻宝游戏、阅读恐龙绘本，边玩边学，快乐度夏。",
    "fee": "收费",
    "source": "重庆万州万达广场",
    "family_friendly": True
})

# ===== 4. 各区县文化馆/图书馆活动（15条）=====

activities.append({
    "title": "江津区图书馆'课外拾光'少儿公益课堂",
    "venue": "江津区图书馆",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-07-17",
    "link": "http://news.cqjjnet.com/web/aritcle/1520084384441462784/web/content_1520084384441462784.html",
    "description": "开设公益科普、公益科创、公益书法三大特色课程。公益科普课堂通过趣味实验、科学观察激发科学好奇心；公益科创课堂以少儿趣味编程为核心；公益书法课堂聚焦卷面书写提升，全程免费开放。",
    "fee": "免费",
    "source": "江津区图书馆",
    "family_friendly": True
})

activities.append({
    "title": "大渡口区'非遗小匠·暑期有约'亲子非遗课堂",
    "venue": "新世纪百货大渡口商都",
    "city": "chongqing",
    "start_date": "2026-07-27",
    "end_date": "2026-08-07",
    "link": "http://m.toutiao.com/group/7662567113005040155/",
    "description": "大渡口区非物质文化遗产保护中心主办，共计10场亲子非遗课堂，每场限定20组家庭。面向全区6-15岁青少年及家长，体验非遗传统技艺，传承非遗文化，亲子共同动手感受传统工艺魅力。",
    "fee": "免费",
    "source": "大渡口区非物质文化遗产保护中心",
    "family_friendly": True
})

activities.append({
    "title": "重庆图书馆'童话森林故事会'",
    "venue": "重庆图书馆儿童阅览室智绘空间",
    "city": "chongqing",
    "start_date": "2026-07-04",
    "end_date": "2026-08-31",
    "link": "https://whlyw.cq.gov.cn/zwgk_221/zfxxgkml/ggwhfwlyjczwgk_390142/ggfw_390145/qwhd/202606/t20260626_15779603.html",
    "description": "周末邀请儿童及家长参加，通过讲座让家长掌握教育少儿的巧妙方式方法，通过与少儿互动的活动启发少儿思维，增强少儿的动手能力并增加知识量，通过亲子互动加强家长与子女的默契。",
    "fee": "免费",
    "source": "重庆市文化旅游委",
    "family_friendly": True
})

activities.append({
    "title": "重庆图书馆'光影童年·成长剧场'",
    "venue": "重庆图书馆童话森林绘本馆",
    "city": "chongqing",
    "start_date": "2026-07-05",
    "end_date": "2026-08-31",
    "link": "https://whlyw.cq.gov.cn/zwgk_221/zfxxgkml/ggwhfwlyjczwgk_390142/ggfw_390145/qwhd/202606/t20260626_15779603.html",
    "description": "精选国内外优质电影、纪录片与科普影片，涵盖自然科普、历史文化、艺术启蒙、成长教育等多元主题，打造寓教于乐的观影体验，让孩子们在轻松愉悦的氛围中开阔视野、启迪智慧。",
    "fee": "免费",
    "source": "重庆市文化旅游委",
    "family_friendly": True
})

activities.append({
    "title": "重庆图书馆小小志愿者活动",
    "venue": "重庆图书馆少年儿童阅览室",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-07-31",
    "link": "https://whlyw.cq.gov.cn/zwgk_221/zfxxgkml/ggwhfwlyjczwgk_390142/ggfw_390145/qwhd/202606/t20260626_15779603.html",
    "description": "让小读者们了解图书馆的大致运作流程，学习图书如何整理上架，如何更有效的利用图书资源，锻炼自己的社会实践能力，培养责任感与服务意识，度过有意义的暑假。",
    "fee": "免费",
    "source": "重庆市文化旅游委",
    "family_friendly": True
})

activities.append({
    "title": "大渡口区图书馆'四季童读'夏季卷阅读挑战赛",
    "venue": "大渡口区图书馆二楼少儿借阅室",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662567113005040155/",
    "description": "国图少儿馆特别策划的'四季童读'新书推荐项目，夏季卷共推荐新书29种，分为文学、人文、科普三大类别。小读者选取4册本季度图书进行阅读打卡挑战活动，培养阅读习惯。",
    "fee": "免费",
    "source": "大渡口区图书馆",
    "family_friendly": True
})

activities.append({
    "title": "大渡口区图书馆科普绘本讲座",
    "venue": "大渡口区图书馆、各镇街分馆",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662567113005040155/",
    "description": "根据'四季童读'2026年夏季卷推荐的29种新书，邀请专业老师为少年儿童开展科普绘本分享讲座，用生动有趣的方式讲解科普知识，激发孩子的阅读兴趣和科学探索精神。",
    "fee": "免费",
    "source": "大渡口区图书馆",
    "family_friendly": True
})

activities.append({
    "title": "石柱县图书馆萌宝'悦'读'绘'活动",
    "venue": "石柱县图书馆",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-07-15",
    "link": "http://cqszx.gov.cn/bm/xwhlyw/zwgk_51502/jczwgk_bm/ggwhfwlyxxgk/ggfw/qwhd/202607/t20260710_15816390.html",
    "description": "面向低幼儿童的绘本阅读活动，两期精彩内容，通过绘本故事、手工互动、亲子共读等形式，培养孩子的阅读兴趣和语言表达能力，是暑期亲子阅读的好去处。",
    "fee": "免费",
    "source": "石柱县图书馆",
    "family_friendly": True
})

activities.append({
    "title": "石柱县'少年儿童爱心接力服务'活动",
    "venue": "石柱县图书馆",
    "city": "chongqing",
    "start_date": "2026-07-15",
    "end_date": "2026-07-25",
    "link": "http://cqszx.gov.cn/bm/xwhlyw/zwgk_51502/jczwgk_bm/ggwhfwlyxxgk/ggfw/qwhd/202607/t20260710_15816390.html",
    "description": "重庆市少年儿童图书馆主办的爱心接力活动，通过图书漂流、阅读分享、爱心传递等形式，让孩子们在阅读中学会分享与关爱，培养社会责任感与同理心。",
    "fee": "免费",
    "source": "重庆市少年儿童图书馆",
    "family_friendly": True
})

activities.append({
    "title": "石柱县'书之韵'读书会活动",
    "venue": "石柱县良玉大讲堂",
    "city": "chongqing",
    "start_date": "2026-07-15",
    "end_date": "2026-07-31",
    "link": "http://cqszx.gov.cn/bm/xwhlyw/zwgk_51502/jczwgk_bm/ggwhfwlyxxgk/ggfw/qwhd/202607/t20260710_15816390.html",
    "description": "在良玉大讲堂举办的读书分享活动，邀请文化学者、作家等与读者面对面交流，分享阅读心得与人生感悟，营造浓厚的全民阅读氛围，丰富市民精神文化生活。",
    "fee": "免费",
    "source": "石柱县图书馆",
    "family_friendly": True
})

activities.append({
    "title": "石柱县少年儿童电子绘本创作培训",
    "venue": "石柱县图书馆",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-07-31",
    "link": "http://cqszx.gov.cn/bm/xwhlyw/zwgk_51502/jczwgk_bm/ggwhfwlyxxgk/ggfw/qwhd/202607/t20260710_15816390.html",
    "description": "线上线下结合的电子绘本创作培训活动，教孩子们如何使用电脑、手机等工具创作属于自己的电子绘本，用图画和文字讲述故事，培养创造力与数字素养。",
    "fee": "免费",
    "source": "石柱县图书馆",
    "family_friendly": True
})

activities.append({
    "title": "大渡口区图书馆'我最喜爱的童书'阅读分享会",
    "venue": "大渡口区图书馆、各镇街分馆",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662567113005040155/",
    "description": "根据'2026年我最喜爱的童书'推荐图书，邀请专业老师为少年儿童开展阅读分享会，通过互动讨论、角色扮演、手工延伸等形式，让孩子深度理解书籍内容，爱上阅读。",
    "fee": "免费",
    "source": "大渡口区图书馆",
    "family_friendly": True
})

activities.append({
    "title": "大渡口区图书馆微生物科普展",
    "venue": "大渡口区图书馆",
    "city": "chongqing",
    "start_date": "2026-08-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662567113005040155/",
    "description": "'小身材 大能量'微生物科普展，揭开微生物的神秘面纱，深入微观宇宙，了解微生物在生态循环、科学研究、日常生活中的重要作用，适合亲子共同参观学习。",
    "fee": "免费",
    "source": "大渡口区图书馆",
    "family_friendly": True
})

activities.append({
    "title": "重庆图书馆'山城作家谈'亲子分享会",
    "venue": "重庆图书馆四楼多功能厅",
    "city": "chongqing",
    "start_date": "2026-07-11",
    "end_date": "2026-07-11",
    "link": "https://whlyw.cq.gov.cn/zwgk_221/zfxxgkml/ggwhfwlyjczwgk_390142/ggfw_390145/qwhd/202606/t20260626_15779603.html",
    "description": "儿童文学作家李姗姗分享三星堆主题作品《青铜神树》的创作故事，带领孩子走进三星堆的神秘世界，激发对历史文化的兴趣，适合亲子家庭共同参与。",
    "fee": "免费",
    "source": "重庆市文化旅游委",
    "family_friendly": True
})

activities.append({
    "title": "大足区文化馆'音乐释压仓'周末音乐会",
    "venue": "大足区文化馆",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_7879923025_1d5ae155101901sfa8.html",
    "description": "区文化馆每周末推出不同主题专场音乐活动，涵盖古典、流行、民族等多种音乐风格，为市民带来精彩的音乐盛宴，适合全家老小一起欣赏，陶冶艺术情操。",
    "fee": "免费",
    "source": "达轻一景",
    "family_friendly": True
})

# ===== 5. 各区县暑期活动（25条）=====

activities.append({
    "title": "丰都南天湖第八届避暑音乐季",
    "venue": "丰都县南天湖景区音乐广场",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_7879923025_1d5ae155101901sfa8.html",
    "description": "周末主题音乐晚会、群仙齐舞泡沫蹦迪狂欢、周内音乐派对、仙乐缥缈秀、立体悬浮秀、夏日瓜瓜乐活动、江湖酒肆音浪市集、环湖观光小火车、星空露营趴，夏季均温约20度，避暑度假胜地。",
    "fee": "收费",
    "source": "达轻一景",
    "family_friendly": True
})

activities.append({
    "title": "大足石刻2026年暑期消夏季",
    "venue": "大足石刻宝顶山景区、昌州古城等",
    "city": "chongqing",
    "start_date": "2026-06-15",
    "end_date": "2026-08-31",
    "link": "http://cq.news.cn/20260617/aed6b11f76834643afa61037b4ce0b96/c.html",
    "description": "以毕业季为主题，融合端午、七夕等传统佳节，推出非遗展演、国风音乐、游戏互动、农事体验等29项活动。宝顶山石刻'穿越宋朝'NPC互动、古风簪花、石刻拓印、火漆印章等沉浸式文化体验。",
    "fee": "收费（中高考生免票）",
    "source": "重庆日报",
    "family_friendly": True
})

activities.append({
    "title": "龙水湖非遗龙舟赛",
    "venue": "大足区龙水湖",
    "city": "chongqing",
    "start_date": "2026-06-19",
    "end_date": "2026-06-22",
    "link": "http://cq.news.cn/20260617/aed6b11f76834643afa61037b4ce0b96/c.html",
    "description": "22人制龙舟200米直道竞速比赛，以水为媒点燃夏日激情，传统民俗赛事与现代观赛体验相结合，是亲子家庭感受传统文化、体验端午氛围的绝佳活动。",
    "fee": "免费观看",
    "source": "重庆日报",
    "family_friendly": True
})

activities.append({
    "title": "璧山夏季文旅系列活动",
    "venue": "璧山区梦界水世界、玉泉湖等",
    "city": "chongqing",
    "start_date": "2026-06-13",
    "end_date": "2026-08-31",
    "link": "https://wap.cq.gov.cn/zwgk/zfxxgkml/zdlyxxgk/ggwh/ly/zxdt/202606/t20260605_15731284.html",
    "description": "五大核心主题活动：梦界水世界全新升级开放、玉泉湖龙舟赛、王者荣耀职业联赛重庆狼队主场赛事、'渝BA'璧山主场赛事、田园采摘体验，亲子越野跑、溪水摸鱼钓虾、水上露营、农耕研学等配套活动。",
    "fee": "不同活动不同价格",
    "source": "璧山区人民政府",
    "family_friendly": True
})

activities.append({
    "title": "璧山梦界水世界夏季开放",
    "venue": "璧山区梦界水世界",
    "city": "chongqing",
    "start_date": "2026-06-13",
    "end_date": "2026-08-31",
    "link": "https://wap.cq.gov.cn/zwgk/zfxxgkml/zdlyxxgk/ggwh/ly/zxdt/202606/t20260605_15731284.html",
    "description": "全市首个夏威夷风造浪池，十大王牌水上游乐项目，日间海狮互动、趣味摸鱼、水上闯关、萌宠互动，夜间电音演出、水幕光影、焰火表演，千米环园漂流河，昼夜差异化游玩场景。",
    "fee": "收费",
    "source": "璧山区人民政府",
    "family_friendly": True
})

activities.append({
    "title": "南川金佛山夏季避暑旅游季",
    "venue": "南川区金佛山景区",
    "city": "chongqing",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "http://cq.news.cn/20260617/aed6b11f76834643afa61037b4ce0b96/c.html",
    "description": "重庆主城最近的世遗避暑地，推荐神龙峡景区、金山湖等20处避暑地，涵盖森林康养、峡谷亲水、高山草甸、田园山居四大品类，夏季均温比中心城区低8-10度，避暑亲子游首选。",
    "fee": "收费",
    "source": "重庆日报",
    "family_friendly": True
})

activities.append({
    "title": "彭水阿依河第二届木叶漂流季",
    "venue": "彭水苗族土家族自治县阿依河景区",
    "city": "chongqing",
    "start_date": "2026-04-20",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_7879923025_1d5ae155101901sfa8.html",
    "description": "全程14公里非遗文化漂流，融入苗歌对唱、苗饰苗服展示、拦门酒、竹竿舞等苗乡非遗体验，三条精品徒步线路：穿越地心徒步、摩围山户外运动、云顶寺古韵徒步，夏日亲水避暑好去处。",
    "fee": "收费",
    "source": "达轻一景",
    "family_friendly": True
})

activities.append({
    "title": "武隆赵家乡避暑纳凉休闲系列活动",
    "venue": "武隆区赵家乡",
    "city": "chongqing",
    "start_date": "2026-07-17",
    "end_date": "2026-08-16",
    "link": "http://www.cqnews.net/app/content_1520085908022390784.html",
    "description": "平均海拔1100米，夏季平均气温仅22℃，十余项特色文旅活动：乡野徒手摸鱼挑战赛、丛林捉鸡大赛、河畔星空露营音乐会、亲子抓鱼溯溪、泥地足球、捉泥鳅、星河旷野童趣夜、世界杯露营狂欢夜、全民才艺挑战赛。",
    "fee": "部分活动免费",
    "source": "华龙网",
    "family_friendly": True
})

activities.append({
    "title": "奉节三峡凉都避暑季",
    "venue": "奉节县兴隆镇三峡凉都",
    "city": "chongqing",
    "start_date": "2026-07-16",
    "end_date": "2026-08-31",
    "link": "http://cq.xinhuanet.com/20260717/b9b28b260b8e48e2922a733bdbb79a58/c.html",
    "description": "土家山歌、篝火摆手舞每晚固定节目，街舞邀请赛、自行车赛轮番登台，云雾土家女儿会、长安采药节等活动穿插其间，周周有主题、天天有看头，核心避暑区平均海拔1248米，清凉避暑胜地。",
    "fee": "部分活动免费",
    "source": "重庆日报",
    "family_friendly": True
})

activities.append({
    "title": "巫山摩天岭长江云上生活季",
    "venue": "巫山云雨康养旅游度假区月亮谷公园",
    "city": "chongqing",
    "start_date": "2026-07-10",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1048945605_121124408/",
    "description": "海拔1350米，夏季平均气温23℃，16项农商文旅体融合活动：亲子趣味运动会、青少年篮球赛、摩天杯羽毛球邀请赛、啤酒露营音乐节、云端康养、美食市集、夜游三峡，清凉避暑好去处。",
    "fee": "部分活动免费",
    "source": "巫山发布",
    "family_friendly": True
})

activities.append({
    "title": "江津四面山之夏系列活动",
    "venue": "江津区四面山镇",
    "city": "chongqing",
    "start_date": "2026-07-10",
    "end_date": "2026-08-30",
    "link": "http://news.cqjjnet.com/web/aritcle/1523734206641029120/web/content_1523734206641029120.html",
    "description": "硒居四面·寻古游园会五大古风关卡、硒游四面·寻趣农耕体验（掰玉米、稻田摸鱼、林间寻蛋）、四面山之夜文艺演出、星空电影夜、青少年公益托管班，避暑亲子游首选。",
    "fee": "部分活动免费",
    "source": "江津区融媒体中心",
    "family_friendly": True
})

activities.append({
    "title": "梁平双桂湖滨湖仲夏夜潮玩季",
    "venue": "梁平区双桂湖国家湿地公园",
    "city": "chongqing",
    "start_date": "2026-07-10",
    "end_date": "2026-08-31",
    "link": "https://cq.ifeng.com/c/8ungSEfb4AJ",
    "description": "湖畔草坪晚风观影、落日音乐会、滨湖美食体验、亲子漫游体验（充气城堡、泡泡乐园、亲子卡丁车、环湖观光车）、文创手工市集，双桂湖畔夏夜休闲好去处。",
    "fee": "部分活动免费",
    "source": "凤凰网重庆",
    "family_friendly": True
})

activities.append({
    "title": "梁平百里竹海避暑季",
    "venue": "梁平区百里竹海景区",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://cq.ifeng.com/c/8ungSEfb4AJ",
    "description": "寿海、猎神景区、观音洞等景点，猎神亲子环线5公里徒步，矿山咖啡、琴海、梯塘花田、小微湿地等打卡点，夏季竹林均温比城区低5-8度，是避暑纳凉、亲子徒步的好选择。",
    "fee": "收费",
    "source": "凤凰网重庆",
    "family_friendly": True
})

activities.append({
    "title": "开州童话森林王国暑期优惠季",
    "venue": "开州区郭家镇童话森林王国",
    "city": "chongqing",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "https://m.cq.bendibao.com/tour/165002.shtm",
    "description": "孩子们的欢乐天堂，10大主题区、40余个游乐项目，通过四条趣味童话故事主线串联，萌宠动物园、滑世界、梦幻金沙滩、科技体验馆等应有尽有，沉浸式体验童话乐趣。",
    "fee": "收费（中高考生半价）",
    "source": "开州文旅",
    "family_friendly": True
})

activities.append({
    "title": "开州盛山植物园暑期活动",
    "venue": "开州区盛山植物园",
    "city": "chongqing",
    "start_date": "2026-06-10",
    "end_date": "2026-08-30",
    "link": "https://m.cq.bendibao.com/tour/165002.shtm",
    "description": "以四美文化为IP、以山水园林为基础，园内环境优美，花香四季，满园碧翠，拥有珍稀花木、家禽野鸟、人文景观，是高富氧离子的自然氧吧，教师、考生免门票。",
    "fee": "收费（教师考生免票）",
    "source": "开州文旅",
    "family_friendly": True
})

activities.append({
    "title": "开州七彩仁和夏季花海节",
    "venue": "开州区七彩仁和景区",
    "city": "chongqing",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "https://m.cq.bendibao.com/tour/165002.shtm",
    "description": "500亩花海铺就四季画卷，夏季马鞭草紫浪，沿1.6千米悬崖景观带漫步，索桥跨峡谷、花影漫石阶，水上摇摆桥、儿童游乐园、自助野炊、天空之镜等体验丰富，尽享自然野趣。",
    "fee": "收费（高考生5折）",
    "source": "开州文旅",
    "family_friendly": True
})

activities.append({
    "title": "万州乡村一日游亲子线路",
    "venue": "万州区各乡村旅游点",
    "city": "chongqing",
    "start_date": "2026-07-14",
    "end_date": "2026-08-31",
    "link": "https://wzwz.cqliving.com/#/hotsPot-detail?id=5001019830&infoId=11116488",
    "description": "两条亲子专属半自由行线路：人文体验行（何其芳故居+巴国部落/同鑫农业园采摘+万州大瀑布）、山林秘境游（安澜谷+青山里悬崖部落+龙冠山），适合家庭周末出游。",
    "fee": "不同景点不同价格",
    "source": "万州文旅",
    "family_friendly": True
})

activities.append({
    "title": "綦江亲子研学三日线路",
    "venue": "綦江区各景点",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662836432118596137/",
    "description": "三条亲子研学线路：红色传承+乡村体验+地质科普线、非遗+红色+人文+乡村线、长征文化+古镇+乡村线，从重庆中心城区出发1小时车程，沉浸式传承红色基因，体验乡村文旅。",
    "fee": "不同景点不同价格",
    "source": "綦江文旅",
    "family_friendly": True
})

activities.append({
    "title": "綦江响马河亲子漂流",
    "venue": "綦江区赶水镇盐河村响马河",
    "city": "chongqing",
    "start_date": "2026-05-19",
    "end_date": "2026-08-31",
    "link": "http://www.cqnews.net/app/content_1507074059773820928.html",
    "description": "全长6.8公里，90%的漂道为天然河床，常年水流冲刷石面光滑。不同于高落差强刺激的漂流，响马河主打亲子漂流，河道平缓、落差小、安全性高，全家出游适配度拉满。",
    "fee": "收费",
    "source": "綦江日报",
    "family_friendly": True
})

activities.append({
    "title": "武隆大洞河乡罩云山观星避暑季",
    "venue": "武隆区大洞河乡罩云山",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://cq.xinhuanet.com/20260717/b9b28b260b8e48e2922a733bdbb79a58/c.html",
    "description": "全市唯一入选全国暑期观星地图的点位，森林覆盖率95%，观星条件达到波特尔暗夜2级。12号风车观景台等打卡点，专业天文观测设备，星空研学，吸引亲子家庭和年轻'追星族'前来。",
    "fee": "部分活动免费",
    "source": "重庆日报",
    "family_friendly": True
})

activities.append({
    "title": "北碚金刀峡镇水上趣味活动季",
    "venue": "北碚区金刀峡镇",
    "city": "chongqing",
    "start_date": "2026-07-11",
    "end_date": "2026-08-31",
    "link": "http://cq.xinhuanet.com/20260717/b9b28b260b8e48e2922a733bdbb79a58/c.html",
    "description": "浑水摸鱼、水上吃西瓜比赛，每个周末还有水上'村BA'、水上拔河和歌唱赛，注重参与性，亲子游客和主城避暑团明显增多，夏日亲水趣味活动好去处。",
    "fee": "部分活动免费",
    "source": "重庆日报",
    "family_friendly": True
})

activities.append({
    "title": "南川大观镇番茄采摘季",
    "venue": "南川区大观现代农业示范基地",
    "city": "chongqing",
    "start_date": "2026-06-25",
    "end_date": "2026-09-01",
    "link": "http://cq.xinhuanet.com/20260717/b9b28b260b8e48e2922a733bdbb79a58/c.html",
    "description": "玻璃大棚里'罗兰''黑娃'等特色品种番茄挂满枝头，轨道车采摘、番茄科普等研学活动吸引不少家庭参与，大棚自带降温功能避免暴晒，适合亲子体验现代农业。",
    "fee": "收费（按采摘重量计费）",
    "source": "重庆日报",
    "family_friendly": True
})

activities.append({
    "title": "荣昌万灵古镇夏季文化旅游季",
    "venue": "荣昌区万灵古镇",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://cq.news.cn/20260617/aed6b11f76834643afa61037b4ce0b96/c.html",
    "description": "中国历史文化名镇，濑溪河穿镇而过，夏布、折扇等非遗文化体验，古镇游船、非遗展演、民俗活动，暑期推出系列亲子体验项目，感受千年古镇的独特魅力。",
    "fee": "免费进入（部分项目收费）",
    "source": "重庆日报",
    "family_friendly": True
})

activities.append({
    "title": "铜梁安居古城夏季活动季",
    "venue": "铜梁区安居古城",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://cq.news.cn/20260617/aed6b11f76834643afa61037b4ce0b96/c.html",
    "description": "中国第四大古城，暑期推出县令出巡、翰林省亲、婚嫁民俗等实景演出，龙舞表演、非遗体验、传统美食，适合亲子家庭沉浸式感受古城文化，了解铜梁龙文化。",
    "fee": "免费进入（部分项目收费）",
    "source": "重庆日报",
    "family_friendly": True
})

activities.append({
    "title": "巫溪红池坝夏季避暑季",
    "venue": "巫溪县红池坝景区",
    "city": "chongqing",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7649276365384057379/",
    "description": "中国南方最大的高山草甸，夏季平均气温17℃，万亩花海、高山草原、原始森林，春申湖游船、沙滩车项目，是避暑纳凉、亲子露营、户外探险的绝佳去处。",
    "fee": "收费（中高考生优惠）",
    "source": "巫溪文旅",
    "family_friendly": True
})

# ===== 6. 古镇/景区暑期活动（10条）=====

activities.append({
    "title": "磁器口古镇潮马艺术展",
    "venue": "磁器口后街·井中天（茶壶）广场",
    "city": "chongqing",
    "start_date": "2026-04-30",
    "end_date": "2026-07-28",
    "link": "https://k.sina.cn/article_7879923025_1d5ae155101901sfa8.html",
    "description": "重庆首个马主题艺术商展，由重庆文旅集团主办，以'艺术+商业+古镇'三位一体模式，将潮马雕塑、打卡点融入老街街巷，全程免费向公众开放，亲子拍照打卡好去处。",
    "fee": "免费",
    "source": "达轻一景",
    "family_friendly": True
})

activities.append({
    "title": "龚滩古镇'端午·粽夏游园会'",
    "venue": "酉阳县龚滩古镇",
    "city": "chongqing",
    "start_date": "2026-06-19",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1039077243_121106884/",
    "description": "千年吊脚楼沿江错落排布，乌江画廊碧波澄澈，包粽竞技、土家非遗上刀山、江畔民谣演出、答题获奖、集章打卡五大主题活动，游船集章兑换手工艾草香囊，非遗绝技展演。",
    "fee": "免费进入（部分项目收费）",
    "source": "酉阳发布",
    "family_friendly": True
})

activities.append({
    "title": "涞滩古镇夏季文化体验季",
    "venue": "合川区涞滩古镇",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://epaper.yongchuanwang.com.cn/html/2024-07/17/content_123198_17622689.htm",
    "description": "首批中国十大历史文化名镇，集古寺、古佛、古民居于一体，国家AAAA级旅游景区。暑期可听折子戏、喝盖碗茶、吃涞滩豆花，品味烟火人间，感受禅宗文化与石刻艺术。",
    "fee": "免费进入（部分项目收费）",
    "source": "合川区融媒体中心",
    "family_friendly": True
})

activities.append({
    "title": "松溉古镇长江原生态文化体验",
    "venue": "永川区松溉古镇",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7661205105059873299/",
    "description": "长江边千年水运古镇，商业化极低，青石板十里老街，明清古县衙、罗家祠堂、玉皇观、临江老码头、吊脚楼江岸。汉服换装、油纸伞非遗手工、古衙实景互动、江边喝茶看轮船。",
    "fee": "免费",
    "source": "永川文旅",
    "family_friendly": True
})

activities.append({
    "title": "巫溪灵巫洞景区夏季探秘",
    "venue": "巫溪县灵巫洞景区",
    "city": "chongqing",
    "start_date": "2026-06-10",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7649276365384057379/",
    "description": "大宁河漂流、旱地雪橇、空中缆车、电梯溶洞等多种体验项目，考生可享半价优惠，是夏季避暑探险、亲子游乐的好去处，感受大自然的鬼斧神工。",
    "fee": "收费（中高考生优惠）",
    "source": "巫溪文旅",
    "family_friendly": True
})

activities.append({
    "title": "云阳龙缸景区暑期游",
    "venue": "云阳县龙缸景区",
    "city": "chongqing",
    "start_date": "2026-06-15",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7649276365384057379/",
    "description": "天下第一缸，国家AAAAA级景区，玻璃廊桥、龙洞、清水湖等景点，夏季平均气温22度，避暑纳凉胜地，中高考生免门票，同行2人享五折优惠，适合亲子家庭户外探险。",
    "fee": "收费（中高考生免票）",
    "source": "云阳文旅",
    "family_friendly": True
})

activities.append({
    "title": "奉节白帝城·瞿塘峡暑期研学游",
    "venue": "奉节县白帝城·瞿塘峡景区",
    "city": "chongqing",
    "start_date": "2026-06-10",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7649276365384057379/",
    "description": "诗城奉节，三峡之巅，2026届毕业生免首道门票，诗词文化研学、三峡工程科普、传统皮影体验，在山水与文脉交融中，近距离触摸奉节深厚的诗词底蕴与独特的在地文化。",
    "fee": "收费（毕业生免票）",
    "source": "奉节文旅",
    "family_friendly": True
})

activities.append({
    "title": "酉阳桃花源民俗体验季",
    "venue": "酉阳县桃花源景区",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1051601538_121106884/",
    "description": "探访桃花源、叠石花谷、松鼠丛林乐园，近距离观察叠层石、三叶虫等远古化石，了解农耕石器、传统农具的发展变迁；深度体验木叶吹奏、棕编、竹编等非遗技艺，参与特色摆手舞民俗活动。",
    "fee": "收费",
    "source": "重庆市总工会",
    "family_friendly": True
})

activities.append({
    "title": "石柱黄水避暑康养季",
    "venue": "石柱县黄水镇、大风堡、千野草场",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7649276365384057379/",
    "description": "中国黄连之乡，夏季平均气温21度，大风堡原始森林、千野草场高山草甸、毕兹卡绿宫、广寒宫溶洞，土家风情体验，高考生免景区门票，避暑亲子游绝佳选择。",
    "fee": "收费（高考生免票）",
    "source": "石柱文旅",
    "family_friendly": True
})

activities.append({
    "title": "黔江濯水古镇暑期游",
    "venue": "黔江区濯水景区",
    "city": "chongqing",
    "start_date": "2026-06-10",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7649276365384057379/",
    "description": "世界第一风雨廊桥，古镇水乡风情，土家文化体验，中高考生享门票3折优惠，同行人员7折。适合亲子家庭感受土家族文化，体验古镇慢生活。",
    "fee": "收费（中高考生3折）",
    "source": "黔江文旅",
    "family_friendly": True
})

# ===== 7. 社区/街道活动（8条）=====

activities.append({
    "title": "两江新区邢家桥社区非遗拓印体验",
    "venue": "两江新区人和街道邢家桥社区",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "http://www.cq.gov.cn/zwgk/zfxxgkml/zdlyxxgk/jy1/jy/202607/t20260701_15788870.html",
    "description": "假期公益托管点特色活动，志愿者和孩子们一起体验非遗拓印技艺，在动手实践中感受传统文化的魅力，培养孩子的动手能力与文化自信，是托管营中的特色亮点课程。",
    "fee": "免费",
    "source": "重庆市人民政府",
    "family_friendly": True
})

activities.append({
    "title": "渝中区望龙门小学新就业群体专属托管班",
    "venue": "渝中区望龙门小学",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "http://www.cq.gov.cn/zwgk/zfxxgkml/zdlyxxgk/jy1/jy/202607/t20260701_15788870.html",
    "description": "专门服务外卖骑手、网约车司机等新就业群体子女的专属托管班，切实补齐新就业群体子女假期照护短板，用心化解新业态从业者后顾之忧，提供作业辅导、兴趣培养、安全看护等服务。",
    "fee": "免费",
    "source": "重庆市人民政府",
    "family_friendly": True
})

activities.append({
    "title": "涪陵区医护人员专属托管班",
    "venue": "涪陵区医疗机构托管点位",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "http://www.cq.gov.cn/zwgk/zfxxgkml/zdlyxxgk/jy1/jy/202607/t20260701_15788870.html",
    "description": "依托医疗机构开设的医护人员专属托管点位，为医务工作者解除后顾之忧，让白衣天使安心工作，孩子有人照顾、快乐成长，提供课业辅导、素质拓展、安全看护等全方位服务。",
    "fee": "免费",
    "source": "重庆市人民政府",
    "family_friendly": True
})

activities.append({
    "title": "璧山区消防救援支队专属托管班",
    "venue": "璧山区消防救援支队托管点位",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "http://www.cq.gov.cn/zwgk/zfxxgkml/zdlyxxgk/jy1/jy/202607/t20260701_15788870.html",
    "description": "开设消防救援支队专属托管点位，解决消防指战员子女假期看护难题，让消防员安心执勤、守护城市，孩子在安全的环境中学习成长，还可以学习消防知识、体验消防文化。",
    "fee": "免费",
    "source": "重庆市人民政府",
    "family_friendly": True
})

activities.append({
    "title": "开州区企业托管营",
    "venue": "开州区华兰生物单采血浆有限公司",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "http://www.cq.gov.cn/zwgk/zfxxgkml/zdlyxxgk/jy1/jy/202607/t20260701_15788870.html",
    "description": "联动华兰生物单采血浆有限公司设立企业托管营，精准覆盖厂区产业工人子女，把托管服务送到企业门口，解决产业工人暑期带娃难题，让职工安心生产。",
    "fee": "免费",
    "source": "重庆市人民政府",
    "family_friendly": True
})

activities.append({
    "title": "九龙坡区红心蚂蚁登途驿站托管点",
    "venue": "九龙坡区红心蚂蚁登途驿站",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "http://www.cq.gov.cn/zwgk/zfxxgkml/zdlyxxgk/jy1/jy/202607/t20260701_15788870.html",
    "description": "志愿者给孩子们普及科学的生活常识，开展形式多样的科普教育活动，培养孩子的科学素养与生活技能，在快乐中学习成长，是九龙坡区知名的公益托管品牌。",
    "fee": "免费",
    "source": "重庆市人民政府",
    "family_friendly": True
})

activities.append({
    "title": "万州区青少年宫新兴领域托管班",
    "venue": "万州区青少年宫电报路、五桥校区",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-28",
    "link": "http://dpaper.sxcm.net/sxdsb/html/202607/01/content_128497.html",
    "description": "区青少年宫电报路、五桥两大校区同步开设新兴领域托管班级，专业师资、设施完善，提供优质的托管服务与兴趣培养课程，服务快递、网约车等新兴领域青年群体子女。",
    "fee": "免费",
    "source": "三峡都市报",
    "family_friendly": True
})

activities.append({
    "title": "涪陵区江东街道中通快递托管点",
    "venue": "涪陵区江东街道中通快递涪陵分拨中心",
    "city": "chongqing",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "https://m.sohu.com/a/1047164994_121106884/",
    "description": "设在快递分拨中心的托管班，让快递小哥小姐姐们上班带娃两不误，提供作业辅导、趣味活动、安全看护等服务，切实解决新就业形态劳动者子女暑期看护难题。",
    "fee": "免费",
    "source": "共青团涪陵区委",
    "family_friendly": True
})

# ===== 8. 书店/商业综合体活动（15条）=====

activities.append({
    "title": "重庆时代广场'企遇·酷玩山城'Pingu主题展",
    "venue": "重庆时代广场（渝中区解放碑）",
    "city": "chongqing",
    "start_date": "2026-06-27",
    "end_date": "2026-09-15",
    "link": "https://www.163.com/dy/article/L0LP43PU0517AK3R.html",
    "description": "企鹅家族Pingu重庆首展，五大主题场景将极地趣味与山城在地元素巧妙融合：巨型Pingu打卡、雪屋邮局、套圈挑战、Pingu一家围坐吃火锅山城限定画面、雾都索道特色装置，集社交打卡、潮玩互动于一体。",
    "fee": "免费观展",
    "source": "重庆时代广场",
    "family_friendly": True
})

activities.append({
    "title": "重庆万象城'无疯不起浪'玩水派对",
    "venue": "九龙坡区重庆万象城",
    "city": "chongqing",
    "start_date": "2026-07-18",
    "end_date": "2026-07-19",
    "link": "https://m.weibo.cn/detail/5321370863928564",
    "description": "夏日限定玩水派对，画上酷炫图案，畅享夏日清凉，适合亲子家庭共同参与，在商场内就能体验玩水乐趣，避开户外高温，收获夏日清凉与欢乐。",
    "fee": "收费",
    "source": "九龙坡文旅",
    "family_friendly": True
})

activities.append({
    "title": "西西弗书店《名侦探柯南抓帧漫画》图书见面会",
    "venue": "西西弗书店·重庆万象城店",
    "city": "chongqing",
    "start_date": "2026-07-27",
    "end_date": "2026-07-27",
    "link": "https://4292817522623.huodongxing.com/event/5764554000512?qd=5428363092855&layout=EN",
    "description": "《名侦探柯南抓帧漫画》1-5辑30周年纪念版图书见面会，柯南&基德见面会、排队合影、互动问答环节，答对即可获得精美小礼品，是柯南迷小朋友的暑期必去活动。",
    "fee": "免费",
    "source": "西西弗书店",
    "family_friendly": True
})

activities.append({
    "title": "重庆书城第五届图书现采会",
    "venue": "重庆书城（渝中区邹容路108号国泰城市优活广场负二楼）",
    "city": "chongqing",
    "start_date": "2026-07-04",
    "end_date": "2026-07-04",
    "link": "https://m.sohu.com/a/1044746023_121106884/",
    "description": "邀请读者当'选书官'，组队奔赴解放碑重庆书城挑书，小朋友可由一名家长陪同，每人可选书不超过20种，总金额上限2000元，把牵挂已久的好书'请'进馆，采书结束后还有暖心分享会。",
    "fee": "免费",
    "source": "渝中区图书馆",
    "family_friendly": True
})

activities.append({
    "title": "万州万达广场特步少年趣味闯关赛",
    "venue": "万州万达广场3号中庭",
    "city": "chongqing",
    "start_date": "2026-07-17",
    "end_date": "2026-07-19",
    "link": "https://m.weibo.cn/detail/5321362247783743",
    "description": "特步少年趣味闯关赛，直观体验特步少年'助力运动追高'的品牌理念，参与完通关即可领取专业检测报告与100元优惠券，是暑期亲子运动、健康成长的好活动。",
    "fee": "免费参与",
    "source": "重庆万州万达广场",
    "family_friendly": True
})

activities.append({
    "title": "大渡口区万象汇暑期主题活动",
    "venue": "大渡口区万象汇",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.weibo.cn/detail/5320890440747291",
    "description": "暑期主题活动精彩纷呈，涵盖亲子互动、儿童游乐、暑期特惠等多元内容，是大渡口及周边亲子家庭避暑遛娃的好去处，商场内凉爽舒适，吃喝玩乐一站式搞定。",
    "fee": "部分活动免费",
    "source": "大渡口发布",
    "family_friendly": True
})

activities.append({
    "title": "新天泽国际广场暑期狂欢活动",
    "venue": "大渡口区新天泽国际广场",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.weibo.cn/detail/5320890440747291",
    "description": "暑期推出系列亲子活动、儿童游乐、暑期特惠促销，是大渡口区亲子家庭避暑逛街的好去处，室内凉爽舒适，集购物、餐饮、娱乐于一体，暑期遛娃好选择。",
    "fee": "部分活动免费",
    "source": "大渡口发布",
    "family_friendly": True
})

activities.append({
    "title": "重庆购书中心暑期亲子阅读季",
    "venue": "重庆购书中心（大坪龙湖时代天街C馆）",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1029338855_122759948/",
    "description": "6000平方米超大文化空间，16万种图书，150万册库存，儿童绘本区、原型地台玩耍区域，适合周末家庭亲子出行。家长可以在儿童区陪孩子阅读绘本，孩子能在原型地台区域玩耍。",
    "fee": "免费阅读",
    "source": "红芽教辅",
    "family_friendly": True
})

activities.append({
    "title": "涪陵'放下手机 体验未来'小小规划师亲子活动",
    "venue": "涪陵规划展览馆",
    "city": "chongqing",
    "start_date": "2026-07-09",
    "end_date": "2026-08-31",
    "link": "https://m.weibo.cn/detail/5319532042521340",
    "description": "暑期职业体验营'小小规划师'专场活动，18组亲子家庭走进展馆，开启从'屏前'到'城前'的奇妙之旅，了解城市规划知识，培养孩子的空间思维与家国情怀。",
    "fee": "免费",
    "source": "涪陵规划展览馆",
    "family_friendly": True
})

activities.append({
    "title": "昌州古城'昌州夜宴·猫鼠奇遇'真人趣跑",
    "venue": "大足区昌州古城",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://cq.news.cn/20260617/aed6b11f76834643afa61037b4ce0b96/c.html",
    "description": "暑期夜间特色活动，真人户外趣跑游戏'猫鼠奇遇'，游客可在大足夜色中开启一场追逐趣跑，兼具运动与娱乐，适合亲子家庭、朋友组队参与，是夏夜消暑娱乐的好选择。",
    "fee": "收费",
    "source": "重庆日报",
    "family_friendly": True
})

activities.append({
    "title": "大足石刻荷花艺术季",
    "venue": "大足石刻宝顶山景区",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://cq.news.cn/20260617/aed6b11f76834643afa61037b4ce0b96/c.html",
    "description": "充满宋代美学的荷花艺术季，荷香弥漫整个夏日，赏花、品宋韵、感受石刻文化，适合亲子家庭在欣赏美景的同时学习历史文化，沉浸式感受宋代美学与石刻艺术的魅力。",
    "fee": "含在景区门票内",
    "source": "重庆日报",
    "family_friendly": True
})

activities.append({
    "title": "重庆书城暑期阅读一夏活动",
    "venue": "重庆书城（渝中区解放碑）",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://yuzhong.cbg.cn/wap/a/5576/20260717/86454bc0a4fb4db6b46ccbb5053159ac.html",
    "description": "书店消暑、阅读一夏，在炎炎夏日为市民提供清凉的阅读空间，精选暑期推荐书单，举办多场阅读分享、亲子阅读活动，是亲子家庭避暑充电的好去处。",
    "fee": "免费阅读",
    "source": "渝中发布",
    "family_friendly": True
})

activities.append({
    "title": "美心红酒小镇水乐园暑期开放",
    "venue": "涪陵区美心红酒小镇",
    "city": "chongqing",
    "start_date": "2026-06-13",
    "end_date": "2026-08-31",
    "link": "http://cq.news.cn/20260617/aed6b11f76834643afa61037b4ce0b96/c.html",
    "description": "水乐园占地近2万平方米，配备3000平方米大型造浪池、20米高双道螺旋滑梯等20余项游乐设施，可容纳超3000人同时游玩，应届中高考毕业生免费畅玩水乐园。",
    "fee": "收费（中高考生免费）",
    "source": "重庆日报",
    "family_friendly": True
})

activities.append({
    "title": "涪陵美心红酒小镇'清凉大礼包'活动",
    "venue": "涪陵区美心红酒小镇",
    "city": "chongqing",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "http://cq.news.cn/20260617/aed6b11f76834643afa61037b4ce0b96/c.html",
    "description": "面向应届中高考毕业生送出'清凉大礼包'：6月30日前免费畅玩水乐园，8月31日前美心彩色酒店景观房188元/晚特惠（原价368元），性价比超高的毕业旅行目的地。",
    "fee": "收费（毕业生优惠）",
    "source": "重庆日报",
    "family_friendly": True
})

activities.append({
    "title": "重庆汉海海洋公园暑期活动",
    "venue": "巴南区重庆汉海海洋公园",
    "city": "chongqing",
    "start_date": "2026-06-09",
    "end_date": "2026-08-31",
    "link": "https://m.cq.bendibao.com/tour/154651.shtm",
    "description": "中高考生优惠票80元（原价120元），热带雨林馆、大洋馆两大主题场馆，海豚表演、美人鱼演出、海底隧道等，暑期还有特别活动，适合亲子家庭近距离接触海洋生物，学习海洋知识。",
    "fee": "收费（中高考生80元）",
    "source": "重庆本地宝",
    "family_friendly": True
})

# ===== 补充更多活动确保达到120条 =====

activities.append({
    "title": "重庆市少年宫2026年夏令营",
    "venue": "重庆市少年宫及各研学目的地",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1031211929_121106884/",
    "description": "市少年宫2026年夏令营线路合集，涵盖新疆哈密民族文化研学营、粤港澳大湾区科技营、北京人文科技与大使馆交流营、江苏上海名校名迹研学营、西安古都历史与非遗传承营、宜昌三峡美育与艺术写生营等多条线路。",
    "fee": "收费",
    "source": "重庆校外教育",
    "family_friendly": True
})

activities.append({
    "title": "重庆少年宫热血少年军事夏令营",
    "venue": "重庆市少年宫合作营地",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1031211929_121106884/",
    "description": "硬核军事训练、趣味拓展训练、行为习惯养成、心理情绪训练、战地实战训练、生命安全教育、感恩教育、国防教育，培养孩子的自律自强、团队协作和爱国情怀。",
    "fee": "收费",
    "source": "重庆校外教育",
    "family_friendly": True
})

activities.append({
    "title": "武隆白马山精英少年动力营",
    "venue": "武隆区白马山",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1031211929_121106884/",
    "description": "10天成长计划！用番茄专注、目标拆解、四象限法则，帮孩子告别拖拉、学会自我管理；搭配非遗手作、丛林实战、团队挑战，同步提升情商与学习力。清凉避暑、公办师资全程护航。",
    "fee": "收费",
    "source": "重庆校外教育",
    "family_friendly": True
})

activities.append({
    "title": "快乐阳光户外探险情商营",
    "venue": "贵州自然秘境",
    "city": "chongqing",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1031211929_121106884/",
    "description": "走进贵州自然秘境，户外探险+情商成长双赋能！探秘亚洲第一长洞，挑战飞拉达、洞穴桨板、荒野生存等趣味项目，同步开展情绪管理、沟通协作、勇气突破等情商课程。",
    "fee": "收费",
    "source": "重庆校外教育",
    "family_friendly": True
})

activities.append({
    "title": "重庆海洋动物世界暑期科普季",
    "venue": "渝中区重庆海洋动物世界",
    "city": "chongqing",
    "start_date": "2026-06-09",
    "end_date": "2026-08-31",
    "link": "https://m.cq.bendibao.com/tour/154651.shtm",
    "description": "2026届中、高考生凭本人准考证可免费预约入园（每日限量100张），近距离接触海洋生物，学习海洋科普知识，是亲子家庭暑期科普教育的好去处。",
    "fee": "收费（中高考生免费）",
    "source": "重庆本地宝",
    "family_friendly": True
})

print(f"总共生成了 {len(activities)} 条活动")

# 保存到JSON文件
output_path = "/workspace/goout/output/raw/real_activities_chongqing_batch4.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(activities, f, ensure_ascii=False, indent=2)

print(f"已保存到 {output_path}")
