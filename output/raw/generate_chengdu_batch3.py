#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

activities = []

# ==================== 1. 博物馆展览与研学活动 (30条) ====================

# 成都博物馆
activities.append({
    "title": "钢铁与荣耀——意大利都灵王宫博物馆藏骑士文物展",
    "venue": "成都博物馆1号特展厅",
    "city": "chengdu",
    "start_date": "2026-04-30",
    "end_date": "2026-08-23",
    "link": "https://www.cdmuseum.com/xinwen/202607/4431.html",
    "description": "展出都灵王宫博物馆珍藏的140件/套盔甲、兵器、绘画、文献与印章等珍贵文物，聚焦欧洲骑士阶层，可体验锁子甲手套试戴、盔甲试穿拍照等互动环节，亲子观展沉浸式感受中世纪骑士文化。",
    "fee": "收费（单人票50元，亲子票68元）",
    "source": "成都博物馆",
    "family_friendly": True
})

activities.append({
    "title": "探索天府自然之秘自然科普研学活动",
    "venue": "成都博物馆",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662700939760943643/",
    "description": "依托成都博物馆近30万件藏品，聚焦湿地、岷江生态、华西雨屏等本土主题，结合一线科研成果，带青少年深入认识四川独特的生态环境，开展展厅探秘与手工体验。",
    "fee": "免费需预约",
    "source": "成都市文广旅局",
    "family_friendly": True
})

activities.append({
    "title": "周末儿童博物馆——皮影戏表演与互动体验",
    "venue": "成都博物馆",
    "city": "chengdu",
    "start_date": "2026-07-04",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662700939760943643/",
    "description": "周末儿童博物馆品牌活动暑期全面升级，孩子们在展厅探秘+手工体验中收获双倍快乐，更有皮影戏现场表演与互动，让孩子亲手操纵影偶，感受非遗魅力。",
    "fee": "免费需预约",
    "source": "成都博物馆",
    "family_friendly": True
})

activities.append({
    "title": "小小宣讲员2026年度培训活动",
    "venue": "成都博物馆",
    "city": "chengdu",
    "start_date": "2026-07-08",
    "end_date": "2026-08-31",
    "link": "https://www.cdmuseum.com/xinwen/202607/4440.html",
    "description": "成都博物馆80名新晋小小宣讲员接受集中培训，依托成都博物馆与中国东方航空公司'文博+航空'跨界合作，将文博学识和专业礼仪相结合，提升少年文化传播使者综合素养。",
    "fee": "免费需预约",
    "source": "成都博物馆",
    "family_friendly": True
})

activities.append({
    "title": "成都自然与人文讲堂——海洋巨兽主题讲座",
    "venue": "成都博物馆",
    "city": "chengdu",
    "start_date": "2026-07-12",
    "end_date": "2026-07-12",
    "link": "https://www.cdmuseum.com/xinwen/202607/4439.html",
    "description": "讲述从远古横行海域的邓氏鱼到如今遨游深蓝的蓝鲸、抹香鲸的海洋巨兽演化故事，揭秘一鲸落万物生的生态奥秘，适合学龄儿童与家长共同参与。",
    "fee": "免费需预约",
    "source": "成都博物馆",
    "family_friendly": True
})

# 成都自然博物馆
activities.append({
    "title": "白垩纪的回响：隅见地球最后的恐龙盛世特展",
    "venue": "成都自然博物馆（成都理工大学博物馆）",
    "city": "chengdu",
    "start_date": "2026-07-18",
    "end_date": "2026-10-11",
    "link": "http://m.toutiao.com/group/7660356549138776627/",
    "description": "以河南地区发现的白垩纪恐龙化石为主要展品，展出各类恐龙化石、模型及相关展品不少于55件套，深入了解中国角龙、特暴龙等本土恐龙的生存奥秘，亲子恐龙迷必看。",
    "fee": "免费需预约",
    "source": "成都自然博物馆",
    "family_friendly": True
})

activities.append({
    "title": "初见自然科普课堂——植物、昆虫与恐龙三大主题",
    "venue": "成都自然博物馆二楼EF区",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7657124795124843023/",
    "description": "系列课程以自然探索为主线，融合植物、昆虫、恐龙、地质矿产与动物奥秘五大主题。通过观察与压花手作认知植物，结合昆虫结构解析与刮刮卡创作，揭秘永川龙、合川马门溪龙等经典物种。",
    "fee": "免费需预约",
    "source": "成都自然博物馆",
    "family_friendly": True
})

activities.append({
    "title": "亿年秘境守护者的觉醒——博物馆夜宿主题活动",
    "venue": "成都自然博物馆（成都理工大学博物馆）",
    "city": "chengdu",
    "start_date": "2026-07-11",
    "end_date": "2026-08-22",
    "link": "http://m.toutiao.com/group/7661561363772228111/",
    "description": "面向6-12岁少年的博物馆夜宿活动，每场120名少年化身秘境守护者，彻夜留宿博物馆，分三大秘境守护小队驻守三层展厅，深夜破解亿年自然留下的隐秘讯息，体验恐龙纪元、大地秘境、缤纷生命三条探险路线。",
    "fee": "收费",
    "source": "成都自然博物馆",
    "family_friendly": True
})

activities.append({
    "title": "暑期闯关嘉年华——白垩纪恐龙主题互动闯关",
    "venue": "成都自然博物馆",
    "city": "chengdu",
    "start_date": "2026-07-18",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662700939760943643/",
    "description": "围绕白垩纪恐龙展推出的暑期闯关嘉年华，观众在动手动脑的闯关乐趣中深入了解中国角龙、特暴龙等本土恐龙的生存奥秘，亲子组队参与更有乐趣。",
    "fee": "免费需预约",
    "source": "成都自然博物馆",
    "family_friendly": True
})

activities.append({
    "title": "暑期非遗嘉年华——自然与非遗融合体验",
    "venue": "成都自然博物馆",
    "city": "chengdu",
    "start_date": "2026-07-20",
    "end_date": "2026-08-30",
    "link": "http://m.toutiao.com/group/7662700939760943643/",
    "description": "将自然科普与非遗手工艺相结合的暑期嘉年华活动，体验非遗技艺的同时学习自然知识，适合亲子家庭共同参与，动手又动脑。",
    "fee": "免费需预约",
    "source": "成都自然博物馆",
    "family_friendly": True
})

activities.append({
    "title": "白垩纪的回响主题剧本游",
    "venue": "成都自然博物馆",
    "city": "chengdu",
    "start_date": "2026-07-25",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662700939760943643/",
    "description": "沉浸式博物馆剧本游，以白垩纪恐龙世界为背景，亲子组队完成解谜任务，在游戏中学习恐龙知识，体验感与知识性双重收获。",
    "fee": "收费",
    "source": "成都自然博物馆",
    "family_friendly": True
})

# 杜甫草堂博物馆
activities.append({
    "title": "诗栖草堂·趣享暑期精品托管班",
    "venue": "成都杜甫草堂博物馆",
    "city": "chengdu",
    "start_date": "2026-07-06",
    "end_date": "2026-08-28",
    "link": "http://m.toutiao.com/group/7657124795124843023/",
    "description": "在千年诗圣故居、天然园林课堂里，让孩子放下电子产品，沉浸式学习知识、锻炼能力、品悟文脉，度过充实、治愈、有底蕴的诗意暑假，涵盖诗词学习、传统文化体验等内容。",
    "fee": "收费",
    "source": "成都杜甫草堂博物馆",
    "family_friendly": True
})

activities.append({
    "title": "月是故乡明-杜甫与秦州的中医药诗词之旅公益研学",
    "venue": "成都杜甫草堂博物馆",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662700939760943643/",
    "description": "公益研学活动，漫步杜甫药圃识草木，落座草堂一味品食养美味，步入小医侠沉浸体验馆探本草药理，了解诗圣杜甫与中药材的深厚渊源，学习中医药诗词文化。",
    "fee": "免费需预约",
    "source": "成都杜甫草堂博物馆",
    "family_friendly": True
})

activities.append({
    "title": "我为杜甫建茅屋——茅屋模型搭建体验活动",
    "venue": "成都杜甫草堂博物馆",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7660356549138776627/",
    "description": "孩子们变身小小建造师，等比例搭建茅屋模型，亲手触摸榫卯的智慧，了解传统建筑工艺，在动手实践中学习杜甫草堂历史文化。",
    "fee": "免费需预约",
    "source": "成都杜甫草堂博物馆",
    "family_friendly": True
})

activities.append({
    "title": "诗韵草堂·金石留痕——草堂碑刻拓印非遗体验",
    "venue": "成都杜甫草堂博物馆",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7660356549138776627/",
    "description": "了解拓印的历史渊源，认识拓印全套工具，在非遗传承人的指导下亲手体验碑刻拓印技艺，感受传统文化魅力，作品可带走留念。",
    "fee": "免费需预约",
    "source": "成都杜甫草堂博物馆",
    "family_friendly": True
})

activities.append({
    "title": "盖碗里的记忆——成都老茶馆的世界回响展览",
    "venue": "成都杜甫草堂博物馆万佛楼",
    "city": "chengdu",
    "start_date": "2026-06-01",
    "end_date": "2026-07-30",
    "link": "http://m.toutiao.com/group/7660356549138776627/",
    "description": "以诗词为内核、盖碗茶为载体，展出210份珍贵档案文献，在诗意雅致氛围里体会杜甫笔下春风啜茗的悠然意境，沉浸式感受老成都市井烟火与生活智慧。",
    "fee": "免费（博物馆门票需购买）",
    "source": "成都杜甫草堂博物馆",
    "family_friendly": True
})

# 武侯祠博物馆
activities.append({
    "title": "文博探秘——成都武侯祠公益研学活动",
    "venue": "成都武侯祠博物馆",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662700939760943643/",
    "description": "三国迷专属公益研学活动，在全国唯一君臣合祀祠庙中，瞻仰刘备与诸葛亮贴金塑像，了解三国历史文化，聆听英雄故事，适合喜爱历史的亲子家庭。",
    "fee": "免费需预约（门票自理）",
    "source": "成都武侯祠博物馆",
    "family_friendly": True
})

# 四川博物院
activities.append({
    "title": "观妙入真——永乐宫的建筑艺术与传承展览",
    "venue": "四川博物院",
    "city": "chengdu",
    "start_date": "2026-07-09",
    "end_date": "2026-10-09",
    "link": "http://m.toutiao.com/group/7662659206936068651/",
    "description": "汇集永乐宫及四川多家博物馆共125件套文物及藏品、48件辅助展品，融合数字化前沿技术，集中展示永乐宫的建筑与壁画艺术，融入四川古建与壁画内容，亲子领略传统文化之美。",
    "fee": "免费需预约",
    "source": "四川博物院",
    "family_friendly": True
})

activities.append({
    "title": "壁画填色体验活动——永乐宫艺术互动",
    "venue": "四川博物院",
    "city": "chengdu",
    "start_date": "2026-07-15",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662659206936068651/",
    "description": "永乐宫展览配套体验活动，孩子们可以在专业指导下体验壁画填色，感受传统壁画艺术魅力，培养审美能力与动手能力。",
    "fee": "免费需预约",
    "source": "四川博物院",
    "family_friendly": True
})

activities.append({
    "title": "古建模型拼装体验活动",
    "venue": "四川博物院",
    "city": "chengdu",
    "start_date": "2026-07-20",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7662659206936068651/",
    "description": "通过拼装古建模型，了解中国传统建筑结构与智慧，锻炼动手能力与空间思维，适合亲子共同参与完成，作品可带回家留念。",
    "fee": "免费需预约",
    "source": "四川博物院",
    "family_friendly": True
})

# 四川大学博物馆
activities.append({
    "title": "我是小小考古学家系列课程之汉代人的生活指南·饮食篇",
    "venue": "四川大学博物馆102研学教室",
    "city": "chengdu",
    "start_date": "2026-07-11",
    "end_date": "2026-07-11",
    "link": "http://m.toutiao.com/group/7657124795124843023/",
    "description": "通过深入研究馆藏汉代画像石、画像砖等实物材料上的图像信息，结合相关历史文献研究成果，带领小小考古队员穿越回两千多年前的汉代，开启舌尖上的探秘之旅。",
    "fee": "收费",
    "source": "四川大学博物馆",
    "family_friendly": True
})

# 三星堆博物馆
activities.append({
    "title": "云冈石窟：始建于北魏平城时代的世界文化遗产特展",
    "venue": "三星堆博物馆",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-10-08",
    "link": "https://e.thecover.cn/shtml/hxdsb/20260708/249186.shtml",
    "description": "三星堆博物馆年度重点原创展览，荟萃石刻造像、陶器、金器、玻璃器、铜器、大型高精度3D打印复制品等各类展品120余件套，三大篇章系统呈现云冈石窟历史脉络与艺术精髓。",
    "fee": "收费（包含在博物馆门票内）",
    "source": "三星堆博物馆",
    "family_friendly": True
})

activities.append({
    "title": "指尖三星堆·玩转博物馆暑期系列教育体验活动",
    "venue": "三星堆博物馆",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://e.thecover.cn/shtml/hxdsb/20260708/249186.shtml",
    "description": "依托三星堆基本陈列及两大临展，推出三星堆纸面具彩绘、金箔画制作、云冈石窟泥板画制作、非遗铜拓画制作等特色手工体验，近距离感受古蜀文明魅力。",
    "fee": "部分免费",
    "source": "三星堆博物馆",
    "family_friendly": True
})

# 成都市美术馆
activities.append({
    "title": "艺术与城市暑期系列活动",
    "venue": "成都市美术馆A/B区",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-23",
    "link": "http://m.toutiao.com/group/7657124795124843023/",
    "description": "快闪美术馆将写生、摄影、涂鸦共创等多元体验延伸至人民公园、太古里、祠堂街等城市公共空间；创新举办夏日舞会等跨界活动；培养小小美术馆之友，通过礼仪美育、展览培训、志愿讲解考核及主题绘画实践。",
    "fee": "免费需预约",
    "source": "成都市美术馆",
    "family_friendly": True
})

activities.append({
    "title": "小小美术馆之友培养计划",
    "venue": "成都市美术馆",
    "city": "chengdu",
    "start_date": "2026-07-05",
    "end_date": "2026-08-20",
    "link": "http://m.toutiao.com/group/7657124795124843023/",
    "description": "通过礼仪美育、展览培训、志愿讲解考核及主题绘画实践等课程，培养小小美术馆志愿者，提升孩子艺术素养与公众表达能力，获得官方认证证书。",
    "fee": "免费需预约",
    "source": "成都市美术馆",
    "family_friendly": True
})

activities.append({
    "title": "夏日限定盛大舞会——美术馆跨界艺术活动",
    "venue": "成都市美术馆",
    "city": "chengdu",
    "start_date": "2026-07-15",
    "end_date": "2026-08-23",
    "link": "http://m.toutiao.com/group/7662700939760943643/",
    "description": "美术馆内的夏日盛大舞会活动，跨界艺术与音乐，亲子家庭可盛装参与，在艺术氛围中体验舞蹈乐趣，享受独特的文化夏夜。",
    "fee": "免费需预约",
    "source": "成都市美术馆",
    "family_friendly": True
})

activities.append({
    "title": "烟火指数·成都双年展",
    "venue": "成都市美术馆",
    "city": "chengdu",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1042032692_121106884/",
    "description": "成都双年展重磅展览，汇聚国内外知名艺术家作品，涵盖多种艺术形式，亲子观展提升艺术审美，感受当代艺术魅力。",
    "fee": "免费需预约",
    "source": "成都市美术馆",
    "family_friendly": True
})

activities.append({
    "title": "艺术大师班——名家面对面",
    "venue": "成都市美术馆",
    "city": "chengdu",
    "start_date": "2026-07-10",
    "end_date": "2026-08-20",
    "link": "http://m.toutiao.com/group/7662700939760943643/",
    "description": "特邀科研学者与艺术名家开展大师班、跨界分享及工作坊，广东美术馆馆长王绍强、四川美术学院造型艺术学院院长唐勇等亲临现场，带来专业艺术分享。",
    "fee": "免费需预约",
    "source": "成都市美术馆",
    "family_friendly": True
})

# 广汇美术馆
activities.append({
    "title": "PBL小小策展人特训营",
    "venue": "广汇美术馆",
    "city": "chengdu",
    "start_date": "2026-07-10",
    "end_date": "2026-08-25",
    "link": "https://c.m.163.com/news/a/L1T14JCG0514OL9V.html",
    "description": "让孩子沉浸式体验美术馆幕后工作，学习策展知识与流程，完成属于自己的策展方案，锻炼策划能力与艺术思维，获得实践证书。",
    "fee": "收费",
    "source": "广汇美术馆",
    "family_friendly": True
})

activities.append({
    "title": "成都双年展研学营",
    "venue": "广汇美术馆",
    "city": "chengdu",
    "start_date": "2026-07-15",
    "end_date": "2026-08-20",
    "link": "https://c.m.163.com/news/a/L1T14JCG0514OL9V.html",
    "description": "专业导览解读双年展作品，参与艺术创作工作坊，完成研学手册，可获得官方实践证书，是艺术爱好者暑期必选。",
    "fee": "收费",
    "source": "广汇美术馆",
    "family_friendly": True
})

activities.append({
    "title": "七夕限定国风浪漫专场——传统美学体验",
    "venue": "广汇美术馆",
    "city": "chengdu",
    "start_date": "2026-08-10",
    "end_date": "2026-08-25",
    "link": "https://c.m.163.com/news/a/L1T14JCG0514OL9V.html",
    "description": "以传统国风美学结合艺术创作，带来沉浸式美学体验，亲子可共同参与国风手作、传统礼仪学习等活动，感受传统文化浪漫之美。",
    "fee": "收费",
    "source": "广汇美术馆",
    "family_friendly": True
})

# ==================== 2. 图书馆阅读与文化活动 (20条) ====================

activities.append({
    "title": "伴你读一夏·图图讲故事——绘本共读活动",
    "venue": "天府人文艺术图书馆",
    "city": "chengdu",
    "start_date": "2026-07-05",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7657124795124843023/",
    "description": "由成都图书馆喜阅相伴志愿者作为领读者，通过沉浸式讲读、互动提问和角色扮演，带领小读者共读《三只小猪》《胡萝卜幼儿园郊游日》等经典绘本，激发少儿读者阅读兴趣。",
    "fee": "免费需预约",
    "source": "成都图书馆",
    "family_friendly": True
})

activities.append({
    "title": "神奇糖果店绘本共读活动",
    "venue": "天府人文艺术图书馆一楼少儿阅读中心",
    "city": "chengdu",
    "start_date": "2026-07-05",
    "end_date": "2026-07-05",
    "link": "https://m.sohu.com/a/1044468760_121106884/",
    "description": "讲述关于自我接纳与真实力量的主题绘本，故事轻松有趣、图文并茂，环环相扣的悬念与反转设计，让孩子在一次次猜测中享受阅读乐趣，适合3-10岁读者。",
    "fee": "免费需预约",
    "source": "成都图书馆",
    "family_friendly": True
})

activities.append({
    "title": "牙齿牙齿扔屋顶绘本共读活动",
    "venue": "天府人文艺术图书馆一楼少儿阅读中心",
    "city": "chengdu",
    "start_date": "2026-07-12",
    "end_date": "2026-07-12",
    "link": "https://m.sohu.com/a/1044468760_121106884/",
    "description": "荣获多项大奖的国风原创绘本共读，讲述小女孩妞妞换牙的故事，教会孩子们保护牙齿，懂得接纳时光、珍藏美好时光，适合3-7岁读者。",
    "fee": "免费需预约",
    "source": "成都图书馆",
    "family_friendly": True
})

activities.append({
    "title": "数独入门趣味课堂——六宫数独启蒙",
    "venue": "天府人文艺术图书馆多功能厅（负一楼）",
    "city": "chengdu",
    "start_date": "2026-07-04",
    "end_date": "2026-07-25",
    "link": "https://m.sohu.com/a/1044468760_121106884/",
    "description": "通过趣味动画和故事带小读者认识数独起源，理解行列宫基本概念，学习六宫数独核心规则与唯一余数法，从入门到进阶梯度训练，一对一指导，适合6-9岁读者。",
    "fee": "免费需预约",
    "source": "成都图书馆",
    "family_friendly": True
})

activities.append({
    "title": "数独进阶课堂——行列排除法与宫排除法",
    "venue": "天府人文艺术图书馆多功能厅（负一楼）",
    "city": "chengdu",
    "start_date": "2026-07-11",
    "end_date": "2026-07-11",
    "link": "https://m.sohu.com/a/1044468760_121106884/",
    "description": "快速回顾数独规则与唯余法，重点学习行列排除法和宫排除法，掌握锁定数字、排除空位的推理方法，形成规范解题步骤，稳步提升数独推理能力。",
    "fee": "免费需预约",
    "source": "成都图书馆",
    "family_friendly": True
})

activities.append({
    "title": "异型数独趣味挑战课",
    "venue": "天府人文艺术图书馆多功能厅（负一楼）",
    "city": "chengdu",
    "start_date": "2026-07-18",
    "end_date": "2026-07-18",
    "link": "https://m.sohu.com/a/1044468760_121106884/",
    "description": "回顾六宫标准数独技巧，认识经典趣味异型数独如对角线数独或不规则宫格数独，讲解专属规则与解题要点，通过关卡挑战形式增加课堂趣味性。",
    "fee": "免费需预约",
    "source": "成都图书馆",
    "family_friendly": True
})

activities.append({
    "title": "喜阅到家——暑期免邮送书上门活动",
    "venue": "成都图书馆（线上）",
    "city": "chengdu",
    "start_date": "2026-07-10",
    "end_date": "2026-07-22",
    "link": "https://m.sohu.com/a/1049694730_121106884/",
    "description": "炎炎夏日不用出门，通过喜阅到家网借服务平台在线下单借阅，每人可享邮费减免9元福利一次，好书直接送到家，宅家也能开启舒爽阅读模式。",
    "fee": "免费（邮费减免）",
    "source": "成都图书馆",
    "family_friendly": True
})

activities.append({
    "title": "超级免邮日——免费送书到家",
    "venue": "成都图书馆（线上）",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-07-23",
    "link": "https://m.sohu.com/a/1044469643_121106884/",
    "description": "7月1日、7月23日超级免邮日，使用送书上门服务在线下单借阅，每人可享邮费减免9元福利一次，限量减免50单，先到先得。",
    "fee": "免费（邮费减免）",
    "source": "成都图书馆",
    "family_friendly": True
})

activities.append({
    "title": "阅读组团挑战赛——组队共赴书香之约",
    "venue": "成都图书馆（线上）",
    "city": "chengdu",
    "start_date": "2026-07-02",
    "end_date": "2026-07-12",
    "link": "https://m.sohu.com/a/1044469643_121106884/",
    "description": "邀请好友组成3人阅读小队，团队累计借阅达到15册即可获得幸运抽奖机会，和家人朋友一起组队阅读，共赴书香之约。",
    "fee": "免费",
    "source": "成都图书馆",
    "family_friendly": True
})

activities.append({
    "title": "城南旧事答题大闯关——共读书目线上挑战",
    "venue": "成都图书馆（线上）",
    "city": "chengdu",
    "start_date": "2026-07-24",
    "end_date": "2026-07-31",
    "link": "https://m.sohu.com/a/1044469643_121106884/",
    "description": "共读书目线上答题挑战，10道趣味阅读题限时作答，根据答题正确率和用时进行排名，优胜者将获得精美礼品，让阅读更有趣。",
    "fee": "免费",
    "source": "成都图书馆",
    "family_friendly": True
})

activities.append({
    "title": "第三季度喜阅之星评选活动",
    "venue": "成都图书馆（线上）",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-09-30",
    "link": "https://m.sohu.com/a/1044469643_121106884/",
    "description": "报名参与2026年第三季度喜阅之星评选并借阅，即有机会赢取精美文创礼品，分享阅读成果到小红书还可获得分享奖励，让阅读被更多人看见。",
    "fee": "免费",
    "source": "成都图书馆",
    "family_friendly": True
})

activities.append({
    "title": "灯笼街的故事——成都彩灯技艺体验",
    "venue": "营门口街道银沙社区党群服务中心",
    "city": "chengdu",
    "start_date": "2026-07-15",
    "end_date": "2026-07-15",
    "link": "https://m.sohu.com/a/1028263411_121106884/",
    "description": "成都彩灯技艺代表性传承人黄樱樱老师带您了解老成都灯笼街的尘封往事，从选竹到点灯，一步步感受老成都人的匠心与年味，亲手体验扎架、裱糊、彩绘等传统工序。",
    "fee": "免费需预约",
    "source": "成都图书馆",
    "family_friendly": True
})

activities.append({
    "title": "十一只猫进袋子——安全教育绘本活动",
    "venue": "天府人文艺术图书馆多功能厅（负一楼）",
    "city": "chengdu",
    "start_date": "2026-07-18",
    "end_date": "2026-07-18",
    "link": "https://m.sohu.com/a/1028263411_121106884/",
    "description": "高级绘本指导师周凤结合经典绘本故事，引导孩子们认识各类禁止安全标志，解读标识背后的意义，互动游戏+自主绘画设计标志，适合3-8岁亲子家庭。",
    "fee": "免费需预约",
    "source": "成都图书馆",
    "family_friendly": True
})

activities.append({
    "title": "逐梦星河：人类航天的过去、现在与未来科普讲座",
    "venue": "天府人文艺术图书馆多功能厅（负一楼）",
    "city": "chengdu",
    "start_date": "2026-07-19",
    "end_date": "2026-07-19",
    "link": "https://m.sohu.com/a/1028263411_121106884/",
    "description": "四川天文科普协会会员王大海老师主讲，从古人飞天梦想到当代航天成就，介绍载人航天、空间站运行、深空探测等知识，制作祝融号火星车模型，适合6岁以上亲子家庭。",
    "fee": "免费需预约",
    "source": "成都图书馆",
    "family_friendly": True
})

activities.append({
    "title": "从焦虑到从容：做孩子生命中的灯塔——亲子教育讲座",
    "venue": "天府人文艺术图书馆多功能厅（负一楼）",
    "city": "chengdu",
    "start_date": "2026-07-25",
    "end_date": "2026-07-25",
    "link": "https://m.sohu.com/a/1028263411_121106884/",
    "description": "《灯塔型父母》作者周玉亮老师运用案例剖析+话术拆解，传授可落地、易操作的亲子教育方法，解决学业焦虑、青春期叛逆、亲子沟通对立等难题。",
    "fee": "免费需预约",
    "source": "成都图书馆",
    "family_friendly": True
})

activities.append({
    "title": "非遗零距离——活的皮影戏体验活动",
    "venue": "天府人文艺术图书馆",
    "city": "chengdu",
    "start_date": "2026-07-26",
    "end_date": "2026-07-26",
    "link": "http://news.qq.com/rain/a/20260528A06HFO00",
    "description": "成都皮影戏非遗传承人王浩斐现场为孩子们讲解皮影趣味知识，表演经典皮影戏剧目，孩子可亲手操作皮影，感受非遗魅力，适合全年龄段亲子家庭。",
    "fee": "免费需预约",
    "source": "成都图书馆",
    "family_friendly": True
})

# 高新区图书馆
activities.append({
    "title": "成都高新区图书馆暑期少儿阅读系列活动",
    "venue": "成都高新区图书馆（天府四街688号3栋）",
    "city": "chengdu",
    "start_date": "2026-07-18",
    "end_date": "2026-08-31",
    "link": "https://m.weibo.cn/detail/5320954930531995",
    "description": "面向6-12岁读者的暑期少儿阅读系列活动，涵盖绘本共读、手工创作、科普讲座等多种形式，需家长陪同参与，丰富孩子暑期阅读生活。",
    "fee": "免费需预约",
    "source": "成都高新图书馆",
    "family_friendly": True
})

activities.append({
    "title": "智慧之眼少儿阅读活动",
    "venue": "成都高新区图书馆二楼智慧之眼",
    "city": "chengdu",
    "start_date": "2026-07-18",
    "end_date": "2026-08-30",
    "link": "https://m.weibo.cn/detail/5320954930531995",
    "description": "在图书馆二楼智慧之眼区域开展的特色少儿阅读活动，融合阅读与科技体验，让孩子在沉浸式环境中享受阅读乐趣，培养阅读习惯。",
    "fee": "免费需预约",
    "source": "成都高新图书馆",
    "family_friendly": True
})

activities.append({
    "title": "锦江区红领巾爱阅读暑期活动",
    "venue": "锦江区各图书馆及社区",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7657819273683567158/",
    "description": "2026年暑期锦江区红领巾爱阅读活动招募，组织少先队员开展各类阅读分享、读书交流、绘本共读等活动，丰富少先队员暑期文化生活。",
    "fee": "免费",
    "source": "锦江区教育局",
    "family_friendly": True
})

activities.append({
    "title": "双流区暑期亲子心理健康公益活动",
    "venue": "双流区未成年人心理健康辅导中心",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.weibo.cn/detail/5321685768339581",
    "description": "双流区未成年人心理健康辅导中心策划的2026年暑期公益服务季，涵盖亲子团辅、家长减压团辅、公益心理咨询三大板块，全部免费开放预约。",
    "fee": "免费需预约",
    "source": "天府双流",
    "family_friendly": True
})

# ==================== 3. 儿童剧与演出 (20条) ====================

activities.append({
    "title": "冰雪奇缘——艾莎的魔法消失了儿童剧",
    "venue": "成都国际剧院（龙湖滨江天街商场内三楼中庭）",
    "city": "chengdu",
    "start_date": "2026-08-08",
    "end_date": "2026-08-08",
    "link": "https://www.xinruipiao.com/ertongqinzi/28792.html",
    "description": "经典IP儿童剧暑期大促，雷元素精灵的出现打破了阿斯莫德大陆的自然平衡，艾莎的冰雪魔力逐渐消失，姐妹俩踏上旅程前往隆德王国解决危机，沉浸式暴风雪互动全场玩成一片。",
    "fee": "收费（39-99元）",
    "source": "新锐票",
    "family_friendly": True
})

activities.append({
    "title": "真假美猴王——儿童剧暑期专场",
    "venue": "成都国际剧院（龙湖滨江天街商场内三楼中庭）",
    "city": "chengdu",
    "start_date": "2026-08-09",
    "end_date": "2026-08-09",
    "link": "https://www.xinruipiao.com/ertongqinzi/28792.html",
    "description": "有着通天本领的齐天大圣居然被完美复制了，两个大圣长得一样、本领一样、金箍棒都难辨真假，3D多媒体特效呈现腾云驾雾、七十二变，全场一起辨真假，沉浸式互动超好玩。",
    "fee": "收费（39-99元）",
    "source": "新锐票",
    "family_friendly": True
})

activities.append({
    "title": "白雪公主之魔镜奇缘——儿童舞台剧",
    "venue": "成都国际剧院（龙湖滨江天街商场内三楼中庭）",
    "city": "chengdu",
    "start_date": "2026-08-30",
    "end_date": "2026-08-30",
    "link": "https://www.xinruipiao.com/ertongqinzi/28792.html",
    "description": "经典童话改编的舞台剧版本，轻松好懂小朋友瞬间代入剧情，舞美梦幻像掉进了童话书里，原创歌曲旋律超上头，群舞一出来全场气氛拉满，教孩子善良待人、相信美好。",
    "fee": "收费（39-99元）",
    "source": "新锐票",
    "family_friendly": True
})

activities.append({
    "title": "谜人的三星堆——文博互动儿童剧",
    "venue": "中国儿童剧场（成都站）",
    "city": "chengdu",
    "start_date": "2026-07-25",
    "end_date": "2026-07-26",
    "link": "https://m.sohu.com/a/1046640804_121119387/",
    "description": "三星堆博物馆官方支持的文博儿童剧，首次探索文博+舞台创作模式，让文物开口说话变成孩子能看懂共情的故事，融合音乐剧、说唱、多媒体等多种艺术形式，陶猪化身宇宙快乐使者。",
    "fee": "收费",
    "source": "第十五届中国儿童戏剧节",
    "family_friendly": True
})

activities.append({
    "title": "海王星飞船——奇幻海洋互动剧场",
    "venue": "中国儿童剧场（成都站）",
    "city": "chengdu",
    "start_date": "2026-08-22",
    "end_date": "2026-08-23",
    "link": "https://m.sohu.com/a/1046640804_121119387/",
    "description": "帆船奥运冠军徐莉佳专业指导的海洋科普+环保教育剧目，讲述帆船少年小天和鲸鱼大冬与濒危海洋动物相互拯救成长的奇幻燃情故事，传递海洋环保理念。",
    "fee": "收费",
    "source": "第十五届中国儿童戏剧节",
    "family_friendly": True
})

activities.append({
    "title": "一只叫伊古的恐龙——俄罗斯木偶音乐剧",
    "venue": "假日经典小剧场（成都站）",
    "city": "chengdu",
    "start_date": "2026-07-11",
    "end_date": "2026-07-12",
    "link": "https://m.sohu.com/a/1046640804_121119387/",
    "description": "荣获莫斯科假日大奖、墨西哥国际木偶艺术节最佳剧目等六大国际荣誉的俄罗斯顶级木偶作品，2名演员、17个木偶倾情演绎，全剧无语言用灵动木偶与治愈旋律打破壁垒。",
    "fee": "收费",
    "source": "第十五届中国儿童戏剧节",
    "family_friendly": True
})

activities.append({
    "title": "脚尖上的厨房——沉浸式视觉脚偶剧",
    "venue": "假日经典小剧场（成都站）",
    "city": "chengdu",
    "start_date": "2026-07-20",
    "end_date": "2026-07-26",
    "link": "https://m.sohu.com/a/1046640804_121119387/",
    "description": "艺术家以双脚化身为灵动优雅又充满趣味的角色，打造出一方充满想象力、节奏感、幽默感与温情的梦幻厨房天地，融合肢体剧场、傀儡演绎、默剧、舞蹈与视觉喜剧多种艺术形式。",
    "fee": "收费",
    "source": "第十五届中国儿童戏剧节",
    "family_friendly": True
})

activities.append({
    "title": "原色童心·互动亲子科学剧《妙趣实验室》",
    "venue": "原色童心亲子剧场(春熙路茂业百货店)",
    "city": "chengdu",
    "start_date": "2026-07-18",
    "end_date": "2026-08-31",
    "link": "https://sichuan.df962388.com/",
    "description": "互动亲子科学剧，通过趣味实验和互动表演激发孩子对科学的兴趣，每周六周日演出，涵盖物理、化学等多种科学主题，寓教于乐。",
    "fee": "收费（38-98元）",
    "source": "东方演出网",
    "family_friendly": True
})

activities.append({
    "title": "格林童话音乐儿童剧《小红帽》",
    "venue": "发伢剧场(苏宁店)",
    "city": "chengdu",
    "start_date": "2026-08-08",
    "end_date": "2026-08-08",
    "link": "https://sichuan.df962388.com/",
    "description": "经典格林童话改编的音乐儿童剧，讲述小红帽与大灰狼斗智斗勇的故事，适合亲子观看，音乐优美，互动性强。",
    "fee": "收费（48-240元）",
    "source": "东方演出网",
    "family_friendly": True
})

activities.append({
    "title": "百老汇互动亲子科学剧《化学秀》中文版",
    "venue": "成都城市音乐厅·歌剧厅",
    "city": "chengdu",
    "start_date": "2026-09-13",
    "end_date": "2026-09-13",
    "link": "https://www.xinruipiao.com/ertongqinzi/28705.html",
    "description": "百老汇正版授权互动亲子科学剧，用生动有趣的化学实验表演带领孩子探索化学世界的奥秘，演出时长约90分钟，寓教于乐激发科学兴趣。",
    "fee": "收费（108-480元）",
    "source": "新锐票",
    "family_friendly": True
})

activities.append({
    "title": "英文原版合家欢音乐剧《马达加斯加》",
    "venue": "成都高新中演大剧院",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-07-31",
    "link": "https://m.weibo.cn/detail/5315179667522788",
    "description": "英文原版合家欢音乐剧，讲述动物园里的动物们逃到马达加斯加的冒险故事，带娃和企鹅帮一起快乐冒险，亲子欢乐源泉，英文原版提升孩子英语听力。",
    "fee": "收费",
    "source": "成都高新微博",
    "family_friendly": True
})

activities.append({
    "title": "少儿版《只此青绿》舞蹈演出",
    "venue": "四川大剧院·大剧场",
    "city": "chengdu",
    "start_date": "2026-07-25",
    "end_date": "2026-07-25",
    "link": "https://m.weibo.cn/detail/5318022023614393",
    "description": "火爆出圈的《只此青绿》少儿版演出，小舞者们演绎经典青绿山水舞蹈，感受中国传统舞蹈之美，培养孩子艺术审美与舞蹈兴趣。",
    "fee": "收费",
    "source": "四川大剧院",
    "family_friendly": True
})

activities.append({
    "title": "少儿版《孔雀》舞蹈演出",
    "venue": "四川大剧院·大剧场",
    "city": "chengdu",
    "start_date": "2026-08-14",
    "end_date": "2026-08-14",
    "link": "https://m.weibo.cn/detail/5318022023614393",
    "description": "杨丽萍经典作品《孔雀》少儿版，小舞者们用优美舞姿演绎孔雀的灵动与优雅，感受舞蹈艺术魅力，适合喜爱舞蹈的亲子家庭观看。",
    "fee": "收费",
    "source": "四川大剧院",
    "family_friendly": True
})

activities.append({
    "title": "话剧《走出安全岛》——亲子温情剧目",
    "venue": "成都城市音乐厅·戏剧厅",
    "city": "chengdu",
    "start_date": "2026-07-31",
    "end_date": "2026-08-01",
    "link": "https://m.weibo.cn/detail/5320535752051597",
    "description": "关于恐惧、陪伴、选择与勇气的温情话剧，讲述孩子成长过程中的心路历程，适合亲子共同观看，在故事中感受陪伴的力量与成长的意义。",
    "fee": "收费",
    "source": "成都城市音乐厅",
    "family_friendly": True
})

activities.append({
    "title": "川剧秀—传奇变脸沉浸式文旅大秀",
    "venue": "锦江剧场",
    "city": "chengdu",
    "start_date": "2026-07-10",
    "end_date": "2026-08-31",
    "link": "https://sichuan.scol.com.cn/m/ggxw/202607/83289984.html",
    "description": "70分钟沉浸式文旅大秀，以独创的八头变脸绝技和现代光影技术带来极致视觉震撼，让孩子近距离感受川剧魅力，了解四川传统文化。",
    "fee": "收费",
    "source": "四川在线",
    "family_friendly": True
})

activities.append({
    "title": "悦来茶园周六折子戏专场",
    "venue": "悦来茶园",
    "city": "chengdu",
    "start_date": "2026-07-12",
    "end_date": "2026-08-30",
    "link": "https://sichuan.scol.com.cn/m/ggxw/202607/83289984.html",
    "description": "每周六折子戏专场恢复演出，品盖碗茶、摆龙门阵中尽享老成都市井慢生活，经典川剧折子戏轮番上演，是亲子体验传统戏曲文化的好选择。",
    "fee": "收费",
    "source": "四川在线",
    "family_friendly": True
})

activities.append({
    "title": "金沙国际音乐厅定格动画一日体验课",
    "venue": "金沙国际音乐厅",
    "city": "chengdu",
    "start_date": "2026-07-31",
    "end_date": "2026-07-31",
    "link": "https://sichuan.df962388.com/",
    "description": "心迹漫游·节气访谈定格动画一日体验课，孩子可以从零学习定格动画制作，完成自己的动画作品，结合二十四节气主题，艺术与传统文化双收获。",
    "fee": "收费（390元）",
    "source": "东方演出网",
    "family_friendly": True
})

activities.append({
    "title": "舞剧《永不消逝的电波》",
    "venue": "成都高新中演大剧院",
    "city": "chengdu",
    "start_date": "2026-07-15",
    "end_date": "2026-07-20",
    "link": "https://m.sohu.com/a/1042032692_121106884/",
    "description": "中演·成都大剧院开幕演出季重磅舞剧，口碑佳作《永不消逝的电波》，以优美舞蹈讲述红色故事，适合学龄儿童进行爱国主义教育与艺术熏陶。",
    "fee": "收费",
    "source": "成都文旅",
    "family_friendly": True
})

activities.append({
    "title": "舞剧《天工开物》",
    "venue": "成都高新中演大剧院",
    "city": "chengdu",
    "start_date": "2026-07-25",
    "end_date": "2026-07-30",
    "link": "https://m.sohu.com/a/1042032692_121106884/",
    "description": "以中国古代科技巨著《天工开物》为蓝本的原创舞剧，用舞蹈语言展现中国古代科技智慧，适合对历史和科技感兴趣的亲子家庭观看。",
    "fee": "收费",
    "source": "成都文旅",
    "family_friendly": True
})

activities.append({
    "title": "原创音乐剧《黑旗令》",
    "venue": "四川大剧院",
    "city": "chengdu",
    "start_date": "2026-08-10",
    "end_date": "2026-08-15",
    "link": "https://m.sohu.com/a/1042032692_121106884/",
    "description": "成都本土原创音乐剧《黑旗令》，讲述热血沸腾的传奇故事，音乐动听、剧情扣人，适合喜欢音乐剧的亲子家庭，感受本土原创戏剧的魅力。",
    "fee": "收费",
    "source": "成都文旅",
    "family_friendly": True
})

# ==================== 4. 夏令营与研学营 (25条) ====================

# 天府新区研学营
activities.append({
    "title": "海洋治愈营——极地海洋公园夜宿研学",
    "venue": "成都海昌极地海洋公园",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://c.m.163.com/news/a/L1T14JCG0514OL9V.html",
    "description": "夜宿海底和白鲸共度星光之夜，近距离邂逅白鲸、呆萌企鹅，跟着饲养员亲手投喂海洋小动物，海底隧道夜宿、浪漫星光晚宴、趣味科普实验一次打卡，伴着鱼群入眠。",
    "fee": "收费",
    "source": "天府发布",
    "family_friendly": True
})

activities.append({
    "title": "山野撒野营——半隐归野自然学校山林探索",
    "venue": "半隐·归野自然学校（天府新区）",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://c.m.163.com/news/a/L1T14JCG0514OL9V.html",
    "description": "206亩原生山林尽情放电，溯溪玩水、山林探秘、萤火虫夜观、森林剧本杀轮番上线，沉浸式户外撒欢解放孩子天性，让暑假回归山野与自由。",
    "fee": "收费",
    "source": "天府发布",
    "family_friendly": True
})

activities.append({
    "title": "硬核科创营——人造太阳与超算中心科创研学",
    "venue": "DAO+科创研学基地（天府新区）",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://c.m.163.com/news/a/L1T14JCG0514OL9V.html",
    "description": "探访人造太阳中国环流三号、国家超级计算成都中心，沉浸式体验AI趣味互动，走进顶尖光电实验室，近距离观摩高精尖科研设备，和一线科研工作者面对面交流。",
    "fee": "收费",
    "source": "天府发布",
    "family_friendly": True
})

activities.append({
    "title": "非遗手作营——同治龙窑陶艺研学",
    "venue": "同治龙窑（天府新区）",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://c.m.163.com/news/a/L1T14JCG0514OL9V.html",
    "description": "触摸百年窑火沉浸式玩古风陶艺，以历史探访+动手实践为主线，了解土陶历史，跟着非遗大师拉坯塑形、烧制陶品，感受传承百年的窑火文化，作品可带走。",
    "fee": "收费",
    "source": "天府发布",
    "family_friendly": True
})

activities.append({
    "title": "坨坨猫动画创作营——A4儿童艺术馆",
    "venue": "A4儿童艺术馆（麓湖生态城）",
    "city": "chengdu",
    "start_date": "2026-08-01",
    "end_date": "2026-08-31",
    "link": "https://c.m.163.com/news/a/L1T14JCG0514OL9V.html",
    "description": "让孩子体验动画从无到有的创作过程，从零打造专属原创动画，脑洞直接变现，学习动画制作全流程，培养创意思维与动手能力，报名通过微信小程序麓客岛。",
    "fee": "收费",
    "source": "天府发布",
    "family_friendly": True
})

activities.append({
    "title": "NOVA IMMERSE CAMP未来领袖国际创造营",
    "venue": "麓湖少年成长中心",
    "city": "chengdu",
    "start_date": "2026-07-15",
    "end_date": "2026-08-25",
    "link": "https://c.m.163.com/news/a/L1T14JCG0514OL9V.html",
    "description": "哈佛专家带队的未来领袖国际创造营，在真实情境中发现问题、展开探索、与团队协作、设计创新方案，培养领导力与创新思维，适合有国际视野的家庭。",
    "fee": "收费",
    "source": "天府发布",
    "family_friendly": True
})

# 航空科技馆
activities.append({
    "title": "四川航空科技馆一日航空研学营",
    "venue": "四川航空科技馆（彭州市丽春镇）",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1038481688_121106884/",
    "description": "探秘航空科技解锁硬核科创实践，从航空理论科普、展馆深度研学，到三大特色实操课程无人机组装飞行、创意3D打印、航模竞技制作三选一，理论+实操双向赋能。",
    "fee": "收费",
    "source": "成都科协",
    "family_friendly": True
})

activities.append({
    "title": "禾下寻梦记——新质农业科技探索营",
    "venue": "袁隆平杂交水稻科学园（郫都区）",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1038481688_121106884/",
    "description": "走进成都平原万亩高标准农田，致敬袁隆平院士传承稻魂初心，赤脚踏入稻田学插秧，操控农业机甲，组队攻坚水利挑战赛，一站式体验新式农业研学。",
    "fee": "收费",
    "source": "成都科协",
    "family_friendly": True
})

activities.append({
    "title": "AI应用体验馆科创研学营",
    "venue": "成都人工智能数字贸易中心展馆（聚霞路1号）",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1038481688_121106884/",
    "description": "专属青少年AI科创研学课程，覆盖低空航天、智能机器人、智慧生活、团队竞技多元板块，集科普学习、实操体验、竞技闯关、荣誉结营于一体。",
    "fee": "收费",
    "source": "成都科协",
    "family_friendly": True
})

# 环保科普
activities.append({
    "title": "践行垃圾分类守护绿水青山——职工亲子环保科普之旅",
    "venue": "海诺尔成都环保科普基地（新津区）",
    "city": "chengdu",
    "start_date": "2026-07-25",
    "end_date": "2026-07-25",
    "link": "http://m.toutiao.com/group/7663415090158387754/",
    "description": "成都市总工会组织的亲子环保科普活动，走进垃圾焚烧发电厂，生态农场互动投喂、裸眼3D科普+厂区实景参观、绿洲实验室趣味实验，全程免费，限35组职工亲子家庭。",
    "fee": "免费需预约",
    "source": "成都市总工会",
    "family_friendly": True
})

# 何以天府夏令营
activities.append({
    "title": "何以天府5天夏令营——三星堆+熊猫基地+都江堰+武侯祠",
    "venue": "成都及周边多地",
    "city": "chengdu",
    "start_date": "2026-07-18",
    "end_date": "2026-08-30",
    "link": "https://m.xialingying.cc/taoxiongmao/course/1677909695.html",
    "description": "5天4晚深度研学营，PBL项目制学习解码完整成都，考古修复双体验、都江堰水利研学、熊猫基地深度探访、武侯祠三国文化，多期可选，2人成团24人封顶。",
    "fee": "收费（4480元起）",
    "source": "淘熊猫夏令营",
    "family_friendly": True
})

# 成华区
activities.append({
    "title": "成华区暑期青少年红十字生命教育夏令营",
    "venue": "四川省红十字应急救护培训基地",
    "city": "chengdu",
    "start_date": "2026-07-10",
    "end_date": "2026-08-31",
    "link": "https://m.cd.bendibao.com/news/211101.shtm",
    "description": "全程免费的生命教育夏令营，学习溺水、烧烫伤、中暑等意外伤害处理，VR安全体验消防逃生、灭火等，培训结业颁发红十字应急救护普及培训证书。",
    "fee": "免费需预约",
    "source": "成都本地宝",
    "family_friendly": True
})

activities.append({
    "title": "成华区未成年人暑期心理夏令营",
    "venue": "成华区未成年人心理成长中心",
    "city": "chengdu",
    "start_date": "2026-08-15",
    "end_date": "2026-08-30",
    "link": "https://m.cd.bendibao.com/news/211101.shtm",
    "description": "聚焦未成年人心理健康核心素养，围绕情绪识别、情绪管理、人际交往、压力疏导等内容，以系统化趣味化互动式教学，引导青少年认识自我、调节心态。",
    "fee": "免费需预约",
    "source": "成都本地宝",
    "family_friendly": True
})

# 金牛区
activities.append({
    "title": "金牛区沙河源青少年暑期成长营",
    "venue": "五福桥东路8号院美育空间",
    "city": "chengdu",
    "start_date": "2026-08-03",
    "end_date": "2026-08-21",
    "link": "https://m.cd.bendibao.com/news/211101.shtm",
    "description": "面向企业职工、新就业群体家庭子女的公益免费成长营，6-12周岁青少年，每期15人，08:30-17:10周末休息，涵盖作业辅导+兴趣课程。",
    "fee": "免费需预约",
    "source": "成都本地宝",
    "family_friendly": True
})

# 锦江区
activities.append({
    "title": "锦江区社区雏鹰公益活动——42门精品课程",
    "venue": "锦江区各社区",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7657819273683567158/",
    "description": "锦江区第十一期暑期社区雏鹰公益活动，涵盖5大类别、42门精品课程、152节课时，从自然探秘到人文行走，从非遗传承到手作体验，更有艺术鉴赏类课程首次亮相。",
    "fee": "免费需预约",
    "source": "锦江区社区教育学院",
    "family_friendly": True
})

activities.append({
    "title": "锦江区3D打印创意营",
    "venue": "锦江区青少年宫",
    "city": "chengdu",
    "start_date": "2026-07-10",
    "end_date": "2026-08-25",
    "link": "http://m.toutiao.com/group/7657819273683567158/",
    "description": "每个孩子都是造物主！3D打印创意营零基础也能当小设计师，学习3D建模与打印技术，设计制作专属创意作品，培养空间思维与创新能力。",
    "fee": "收费",
    "source": "锦江区青少年宫",
    "family_friendly": True
})

activities.append({
    "title": "红领巾成长蓝图主题活动",
    "venue": "锦江区各中小学及社区",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7657819273683567158/",
    "description": "2026锦江区少先队红领巾·正成长主题活动，组织少先队员开展暑期实践活动，培养责任意识与实践能力，丰富少先队员暑期生活。",
    "fee": "免费",
    "source": "锦江区教育局",
    "family_friendly": True
})

# 青羊区
activities.append({
    "title": "青羊区全域科普研学——蝴蝶标本制作营",
    "venue": "青羊区科普研学基地",
    "city": "chengdu",
    "start_date": "2026-07-05",
    "end_date": "2026-07-05",
    "link": "https://www.scjjrb.com/2026/05/30/wap_99465079.html",
    "description": "青羊区全域科普研学活动首场，蝴蝶标本制作主题，在标本制作中探究昆虫分类与生态知识，专业导师全程指导，作品可带回家留念。",
    "fee": "免费需预约",
    "source": "青羊区科协",
    "family_friendly": True
})

activities.append({
    "title": "青羊区全域科普研学——浣花溪湿地观鸟营",
    "venue": "浣花溪湿地公园",
    "city": "chengdu",
    "start_date": "2026-07-12",
    "end_date": "2026-07-12",
    "link": "https://www.scjjrb.com/2026/05/30/wap_99465079.html",
    "description": "浣花溪湿地观鸟主题研学，在实地观鸟中学习生物多样性保护理念，专业鸟类导师带队，使用专业望远镜观察，记录鸟类图鉴。",
    "fee": "免费需预约",
    "source": "青羊区科协",
    "family_friendly": True
})

activities.append({
    "title": "青羊区全域科普研学——四川科技馆深度体验营",
    "venue": "四川科技馆",
    "city": "chengdu",
    "start_date": "2026-07-19",
    "end_date": "2026-07-19",
    "link": "https://www.scjjrb.com/2026/05/30/wap_99465079.html",
    "description": "四川科技馆深度体验研学，专业导师带队深度游览科技馆核心展区，讲解+实践相结合，在互动展项中感受前沿科技魅力。",
    "fee": "免费需预约",
    "source": "青羊区科协",
    "family_friendly": True
})

# 高新区
activities.append({
    "title": "高新区桂溪街道课外实践研学课程",
    "venue": "高新区桂溪街道各点位",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://www.cditv.cn/show/4813-2539328.html",
    "description": "桂溪街道链接辖区企业资源推出的课外实践课程，涵盖户外研学体验、职业体验、素质课堂、文化活动、儿童科技体验、志愿服务等丰富内容。",
    "fee": "部分免费",
    "source": "看度新闻",
    "family_friendly": True
})

# 天府新区共享教育
activities.append({
    "title": "天府新区小学特色托管——五大核心课程",
    "venue": "天府七中、海洋路中学、天府一小等点位",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-21",
    "link": "http://www.cditv.cn/show/4813-2539328.html",
    "description": "在基础托管基础上增加跑酷、VEX机器人、魔方、武术、体适能五大核心课程，共七期可自由组合，满足不同兴趣孩子的需求。",
    "fee": "收费（公益价格）",
    "source": "天府新区共享教育",
    "family_friendly": True
})

activities.append({
    "title": "天府新区幼儿素质托管班",
    "venue": "天府新区共享青少年宫",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-21",
    "link": "http://www.cditv.cn/show/4813-2539328.html",
    "description": "针对幼儿需求设计的素质托管，以兴趣培养为核心，通过游戏教学注重身心准备、生活准备、社会准备和学习准备的有机融合，提供学习活动、体育锻炼与餐食配套。",
    "fee": "收费（公益价格）",
    "source": "天府新区共享教育",
    "family_friendly": True
})

# 兴隆湖
activities.append({
    "title": "兴隆湖生态课堂·环湖探索跑——亲子研学跑",
    "venue": "成都兴隆湖湿地公园",
    "city": "chengdu",
    "start_date": "2026-07-11",
    "end_date": "2026-08-31",
    "link": "https://c.m.163.com/news/a/L181F07J0514OL9V.html",
    "description": "8.8公里环湖休闲步道亲子探险跑，5大生态打卡点位设置专属探索任务：观水下森林、探芦苇湿地、高台观候鸟、穿行滨水林、漫步浅滩，边跑边学通关兑换纪念好礼。",
    "fee": "收费（9.9元/人）",
    "source": "天府发布",
    "family_friendly": True
})

activities.append({
    "title": "中国农业科学院都市农业研究所大学生暑期夏令营",
    "venue": "中国农业科学院都市农业研究所（天府新区）",
    "city": "chengdu",
    "start_date": "2026-07-25",
    "end_date": "2026-07-25",
    "link": "https://c.m.163.com/news/a/L181F07J0514OL9V.html",
    "description": "面向优秀大学生的暑期夏令营，开展研究所介绍、专家报告、科研平台参观、交流互动等环节，了解都市农业学科特色与研究生培养体系，适合高中生亲子了解科研方向。",
    "fee": "免费需申请",
    "source": "天府发布",
    "family_friendly": True
})

# ==================== 5. 主题乐园与游乐场 (15条) ====================

activities.append({
    "title": "成都欢乐谷夏浪狂欢节——58天音乐狂欢",
    "venue": "成都欢乐谷（金牛区西华大道16号）",
    "city": "chengdu",
    "start_date": "2026-07-04",
    "end_date": "2026-08-30",
    "link": "https://m.weibo.cn/detail/5314115266675158",
    "description": "成都欢乐谷2026夏浪狂欢节，58天音乐狂欢，唐汉霄、余佳运、银河快递等明星轮番献唱，还有NPC互动、主题打卡、游乐设备畅玩，暑期亲子出游首选。",
    "fee": "收费（毕业生160元优惠）",
    "source": "欢乐谷集团",
    "family_friendly": True
})

activities.append({
    "title": "成都欢乐谷星光小镇——沉浸式主题街区",
    "venue": "成都欢乐谷",
    "city": "chengdu",
    "start_date": "2026-07-18",
    "end_date": "2026-08-30",
    "link": "https://cd.happyvalley.cn/?theme=dark",
    "description": "全新打造的星光小镇主题街区，每个人的灵魂都是一颗散发着真我之光的星辰，沉浸式场景打造，特色演艺与互动体验，适合亲子拍照打卡。",
    "fee": "收费（包含在欢乐谷门票内）",
    "source": "成都欢乐谷",
    "family_friendly": True
})

activities.append({
    "title": "成都海昌极地海洋公园16周年庆·冰淇淋狂欢节",
    "venue": "成都海昌极地海洋公园",
    "city": "chengdu",
    "start_date": "2026-07-04",
    "end_date": "2026-08-31",
    "link": "https://wlt.sc.gov.cn/scwlt/hydt/2026/7/9/dbd6f9e8cb144a03b6440084a968afb7.shtml",
    "description": "开园16周年庆与冰淇淋狂欢节同步启动，极地水乐园免费开放每日两场泼水狂欢，乐奇冰雪乐园免票游玩，-10℃冰雪空间搭配全新冰雕，全天候演艺活动精彩纷呈。",
    "fee": "收费（多重优惠）",
    "source": "四川省文旅厅",
    "family_friendly": True
})

activities.append({
    "title": "奶龙主题打卡点与冰淇淋DIY研学",
    "venue": "成都海昌极地海洋公园",
    "city": "chengdu",
    "start_date": "2026-07-04",
    "end_date": "2026-08-31",
    "link": "https://wlt.sc.gov.cn/scwlt/hydt/2026/7/9/dbd6f9e8cb144a03b6440084a968afb7.shtml",
    "description": "园区设奶龙及冰淇淋主题打卡点、冰淇淋DIY研学、凿冰寻宝等活动，中高考生及大学生可享专属门票，亲子家庭夏日避暑好去处。",
    "fee": "收费（包含在部分门票内）",
    "source": "四川省文旅厅",
    "family_friendly": True
})

activities.append({
    "title": "成都融创水世界神仙玩水季",
    "venue": "成都融创水世界",
    "city": "chengdu",
    "start_date": "2026-07-04",
    "end_date": "2026-08-31",
    "link": "https://wlt.sc.gov.cn/scwlt/hydt/2026/7/9/dbd6f9e8cb144a03b6440084a968afb7.shtml",
    "description": "造浪池化身奇幻天宫，众神NPC领衔电音派对，齐天大圣水上飞人表演、花式主题漂流、三楼27个瑶池仙汤汤池同步开放，室内玩水不怕晒。",
    "fee": "收费",
    "source": "四川省文旅厅",
    "family_friendly": True
})

activities.append({
    "title": "梦回青城·演艺小镇千灯夜",
    "venue": "梦回青城·演艺小镇",
    "city": "chengdu",
    "start_date": "2026-07-04",
    "end_date": "2026-08-31",
    "link": "https://wlt.sc.gov.cn/scwlt/hydt/2026/7/9/dbd6f9e8cb144a03b6440084a968afb7.shtml",
    "description": "水上廊桥荷花灯组、非遗药发木偶、梦回千灯夜孔明灯放飞、大型实景秀《梦回青城》非遗打铁花+裸眼3D水幕，全天超百场演艺及NPC互动游戏。",
    "fee": "收费",
    "source": "四川省文旅厅",
    "family_friendly": True
})

activities.append({
    "title": "国色天乡乐园暑期嘉年华",
    "venue": "国色天乡乐园（温江区天乡路88号）",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://chengdu-expat.com/activities-children-chengdu/",
    "description": "大型主题乐园+水上乐园，是西南最大户外水上中心之一，暑期推出暑期嘉年华活动，有多种游乐设施、水上项目、主题演艺，适合全家畅玩一整天。",
    "fee": "收费（30-280元）",
    "source": "Chengdu Expat",
    "family_friendly": True
})

activities.append({
    "title": "B.Duck小黄鸭城市乐园（东安湖店）",
    "venue": "B.Duck小黄鸭城市乐园（龙泉驿区东安湖）",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://chengdu-expat.com/activities-children-chengdu/",
    "description": "2026年初新开的小黄鸭主题乐园，毗邻东安湖，22个游乐项目，10米高巨型黄鸭，设家庭欢乐区和刺激游乐区，亲子友好，适合全年龄段孩子。",
    "fee": "收费（200元，1.2米以下免费）",
    "source": "Chengdu Expat",
    "family_friendly": True
})

activities.append({
    "title": "成都极趣探索主题乐园——洛水湿地店",
    "venue": "成都极趣探索主题乐园（洛带镇洛水湿地公园）",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://chengdu-expat.com/activities-children-chengdu/",
    "description": "洛带古镇旁的大型户外探险乐园，瑞士设计的树上障碍课程、水上活动、自然探索，适合所有年龄段，是喜欢户外挑战的亲子家庭的好选择。",
    "fee": "收费（儿童88元，成人118元）",
    "source": "Chengdu Expat",
    "family_friendly": True
})

activities.append({
    "title": "新希望种子乐园——亲子农场乐园",
    "venue": "新希望种子乐园（简阳市）",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://chengdu-expat.com/activities-children-chengdu/",
    "description": "大型家庭游乐园，8大主题区域：科学探索、萌宠乐园、农场体验等，有家庭过山车、摩天轮、海盗船、碰碰车和大量非动力设施，适合全家一日游。",
    "fee": "收费（成人45元）",
    "source": "Chengdu Expat",
    "family_friendly": True
})

activities.append({
    "title": "麓湖荒野之国——创意艺术乐园",
    "venue": "麓湖荒野之国（天府新区）",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://chengdu-expat.com/activities-children-chengdu/",
    "description": "艺术家乔小刀打造的创意乐园，各种奇思妙想的小屋和装置，充满想象力，适合带孩子打卡拍照，激发创造力与想象力。",
    "fee": "收费（成人80元，1.2-1.4米儿童40元）",
    "source": "Chengdu Expat",
    "family_friendly": True
})

activities.append({
    "title": "麓湖小岛动物农场——萌宠互动体验",
    "venue": "麓湖生态城小岛动物农场",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://chengdu-expat.com/activities-children-chengdu/",
    "description": "麓湖小岛上的萌宠农场，可以近距离接触和喂养各种小动物，适合低龄儿童，亲子共同体验田园乐趣，培养孩子爱心。",
    "fee": "收费（30元，1.2米以下免费）",
    "source": "Chengdu Expat",
    "family_friendly": True
})

activities.append({
    "title": "成都动物园暑期动物观赏季",
    "venue": "成都动物园（成华区昭觉寺南路234号）",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://chengdu-expat.com/activities-children-chengdu/",
    "description": "西南地区最大的动物园之一，300多种动物，还有著名的大熊猫展区，门票便宜，是亲子认识动物、亲近自然的高性价比选择。",
    "fee": "收费（成人20元，1.2米以下免费）",
    "source": "Chengdu Expat",
    "family_friendly": True
})

activities.append({
    "title": "成都大熊猫繁育研究基地暑期熊猫观赏",
    "venue": "成都大熊猫繁育研究基地",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://k.sina.cn/article_7879776359_1d5abd867019017qv8.html",
    "description": "全球最大大熊猫科研繁育基地，盛夏温度比市区低3-5℃，月亮产房太阳产房看熊猫宝宝，熊猫科普馆学习知识，DIY手工坊文创制作，亲子TOP1必去。",
    "fee": "收费（约55元，学生半价）",
    "source": "驴友探路社",
    "family_friendly": True
})

activities.append({
    "title": "西岭雪山后山免门票暑期避暑游",
    "venue": "西岭雪山",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-10-30",
    "link": "https://wlt.sc.gov.cn/scwlt/hydt/2026/7/9/dbd6f9e8cb144a03b6440084a968afb7.shtml",
    "description": "后山滑雪场景区面向所有游客免门票持续至10月30日，全新鸳鸯池索道360°全透明全景轿厢，云上市集、鸳鸯池湿地、云懒懒牧场三大休闲场景，亲子避暑好去处。",
    "fee": "免费（索道另行收费）",
    "source": "四川省文旅厅",
    "family_friendly": True
})

# ==================== 6. 亲水戏水活动 (15条) ====================

activities.append({
    "title": "第26届洛带客家水龙季——六大主题周末",
    "venue": "洛带古镇五凤楼广场",
    "city": "chengdu",
    "start_date": "2026-07-18",
    "end_date": "2026-08-23",
    "link": "https://m.thepaper.cn/newsDetail_forward_33605525",
    "description": "百年非遗泼水习俗，12个限定玩水日，6大主题周末：清凉悦己周、童趣亲子周、运动活力周、在地体验周、七夕姻缘周、国潮汉风簪花周，每个周末不重样。",
    "fee": "部分免费",
    "source": "见证龙泉驿",
    "family_friendly": True
})

activities.append({
    "title": "洛带客家水龙季童趣亲子周",
    "venue": "洛带古镇五凤楼广场",
    "city": "chengdu",
    "start_date": "2026-07-25",
    "end_date": "2026-07-26",
    "link": "https://m.thepaper.cn/newsDetail_forward_33605525",
    "description": "带娃家庭必看！海绵接力运水、家庭三脚运水亲子家庭专属互动游戏，浅水区安全护航，神兽放电爸妈放心，遛娃天花板，还能体验客家文化。",
    "fee": "免费",
    "source": "见证龙泉驿",
    "family_friendly": True
})

activities.append({
    "title": "洛带客家水龙季在地体验周——非遗手作",
    "venue": "洛带古镇五凤楼广场",
    "city": "chengdu",
    "start_date": "2026-08-08",
    "end_date": "2026-08-09",
    "link": "https://m.thepaper.cn/newsDetail_forward_33605525",
    "description": "免费漆扇手绘、古法擂茶、果壳铃铛手作，指尖触摸客家烟火气，把古镇记忆带回家，玩水之余体验非遗文化，亲子共同参与更有意义。",
    "fee": "免费",
    "source": "见证龙泉驿",
    "family_friendly": True
})

activities.append({
    "title": "都江堰虹口漂流——自然水域激爽漂流",
    "venue": "都江堰虹口漂流景区",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-10-07",
    "link": "https://wlt.sc.gov.cn/scwlt/hydt/2026/7/9/dbd6f9e8cb144a03b6440084a968afb7.shtml",
    "description": "国内唯一的自然水域漂流，10公里河道、90米落差带来近一小时激爽体验，漂流季持续至10月，期间还将举办中国漂流联赛等专业赛事，适合大孩子和家长。",
    "fee": "收费",
    "source": "四川省文旅厅",
    "family_friendly": True
})

activities.append({
    "title": "丹景谷漂流——亲子闲情漂",
    "venue": "东部新区丹景谷漂流",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-09-30",
    "link": "https://wlt.sc.gov.cn/scwlt/hydt/2026/7/9/dbd6f9e8cb144a03b6440084a968afb7.shtml",
    "description": "80%高森林覆盖率，贴心设置6公里激情漂与3公里闲情漂，分别适配寻求刺激的年轻群体与亲子家庭，更衣室、热水淋浴及专业救生员配备齐全。",
    "fee": "收费",
    "source": "四川省文旅厅",
    "family_friendly": True
})

activities.append({
    "title": "金堂龚家山丛林漂流——熊猫主题打卡",
    "venue": "金堂龚家山丛林漂流",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-09-30",
    "link": "https://wlt.sc.gov.cn/scwlt/hydt/2026/7/9/dbd6f9e8cb144a03b6440084a968afb7.shtml",
    "description": "经数月提质升级焕新迎客，396米总落差包含70米极限挑战段，配合全新观光隧道与熊猫主题打卡点，趣味十足，适合喜欢刺激的亲子家庭。",
    "fee": "收费",
    "source": "四川省文旅厅",
    "family_friendly": True
})

activities.append({
    "title": "世博园第二届戏水电音嘉年华",
    "venue": "成都世博园",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1042032692_121106884/",
    "description": "第二届戏水电音嘉年华特别增设七夕主题专场，融合实景演艺、数字光影技术的沉浸式体验，亲子玩水+音乐狂欢，夏日清凉好去处。",
    "fee": "收费",
    "source": "成都文旅",
    "family_friendly": True
})

activities.append({
    "title": "三岔湖首届水上运动嘉年华",
    "venue": "三岔湖",
    "city": "chengdu",
    "start_date": "2026-07-15",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1042032692_121106884/",
    "description": "集结多元新潮水上运动项目，皮划艇、桨板、水上自行车等多种项目体验，亲子共同参与水上运动，感受湖光山色中的夏日清凉。",
    "fee": "收费",
    "source": "成都文旅",
    "family_friendly": True
})

activities.append({
    "title": "葛仙山2026星空夜跑狂欢季",
    "venue": "葛仙山",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1042032692_121106884/",
    "description": "特色星空夜跑活动，夜间山间跑步，仰望星空，锻炼身体的同时享受自然美景，适合喜欢户外运动的亲子家庭，夏日避暑运动两不误。",
    "fee": "收费",
    "source": "成都文旅",
    "family_friendly": True
})

activities.append({
    "title": "新津第八届荷花季——荷塘赏荷寻香",
    "venue": "新津区千亩荷塘",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1042032692_121106884/",
    "description": "千亩荷塘荷花盛开，赏荷、划船、品尝荷花美食，夏日清凉好去处，亲子家庭可以感受田园风光，了解荷花文化，拍摄美照。",
    "fee": "部分免费",
    "source": "成都文旅",
    "family_friendly": True
})

activities.append({
    "title": "黄龙溪火龙灯舞夏季展演",
    "venue": "黄龙溪古镇",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1042032692_121106884/",
    "description": "黄龙溪古镇著名的火龙灯舞夏季展演，非遗民俗表演，古镇戏水纳凉，走街串巷感受川西民俗风情，是夏日亲子出游的经典选择。",
    "fee": "免费（古镇免费开放）",
    "source": "成都文旅",
    "family_friendly": True
})

activities.append({
    "title": "郫都三道堰水乡非遗体验季",
    "venue": "三道堰古镇",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1042032692_121106884/",
    "description": "水乡非遗体验季，亲水纳凉体验非遗文化，三道堰水乡特色风情，亲子可参与非遗手作体验，感受川西水乡文化魅力。",
    "fee": "部分免费",
    "source": "成都文旅",
    "family_friendly": True
})

activities.append({
    "title": "温江乌龙岛河畔森林营地——亲水露营",
    "venue": "温江区乌龙岛河畔森林营地",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://wlt.sc.gov.cn/scwlt/hydt/2026/6/17/99b54c710a6042eca4552e4faa13b74f.shtml",
    "description": "森系露营地，河畔森林环境，支持明火篝火、宠物友好、停车免费，亲子露营玩水好去处，享受自然野趣。",
    "fee": "收费",
    "source": "成都市农业农村局",
    "family_friendly": True
})

activities.append({
    "title": "温江悦椿酒店岛上部落亲子戏水活动",
    "venue": "成都温江悦椿酒店",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.weibo.cn/detail/5321707121283128",
    "description": "2大1小活动体验，日常活动：挖沙溯溪、水上手搓麻将、抓鱼比赛、桨板抓小黄鸭、沙滩寻宝；周末限定：水枪大战、部落寻宝、银票游园会（射箭、踢毽子、门球、套圈、投壶等）。",
    "fee": "收费",
    "source": "成都温江悦椿酒店",
    "family_friendly": True
})

activities.append({
    "title": "金堂淮口山水水上运动乐园",
    "venue": "金堂县淮口山水水上运动乐园",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-09-30",
    "link": "https://wlt.sc.gov.cn/scwlt/hydt/2026/7/9/dbd6f9e8cb144a03b6440084a968afb7.shtml",
    "description": "多种水上运动项目，适合亲子家庭玩水消暑，配套设施齐全，安全有保障，是夏日亲子水上玩乐的好去处。",
    "fee": "收费",
    "source": "四川省文旅厅",
    "family_friendly": True
})

# ==================== 7. 各区特色活动 (10条) ====================

activities.append({
    "title": "沙河流韵2026成华区音乐消夏少儿才艺大赛",
    "venue": "成华区文化馆503多功能厅",
    "city": "chengdu",
    "start_date": "2026-07-04",
    "end_date": "2026-07-05",
    "link": "http://m.toutiao.com/group/7657124795124843023/",
    "description": "以少儿才艺大赛为核心活动，涵盖个人声乐、个人舞蹈、个人器乐、团体舞蹈四大赛事类别，配套青年歌手大赛，打造全民音乐共享舞台，展示少儿艺术风采。",
    "fee": "免费需报名",
    "source": "成华区文化馆",
    "family_friendly": True
})

activities.append({
    "title": "成都大悦城暑期主题展览季",
    "venue": "成都大悦城",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-10-07",
    "link": "http://m.toutiao.com/group/7660790323567723048/",
    "description": "暑期超多主题展览轮番上新：MOMO物语IP展、SDN森贝儿快闪、得力超级文具节、CANOTWAIT_联名小黄人限定系列、松软港湾主题快闪、野兽王国迪士尼公主皇家派对。",
    "fee": "部分免费",
    "source": "武侯区文旅局",
    "family_friendly": True
})

activities.append({
    "title": "奈尔宝乐园暑期福利活动",
    "venue": "成都大悦城奈尔宝乐园",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-07-31",
    "link": "http://m.toutiao.com/group/7660790323567723048/",
    "description": "超高人气的奈尔宝乐园暑期福利持续到7月31日，超大游玩空间让孩子肆意撒欢放电，亲子遛娃好去处，各种游玩设施一应俱全。",
    "fee": "收费（暑期特惠）",
    "source": "武侯区文旅局",
    "family_friendly": True
})

activities.append({
    "title": "武侯吾悦广场御膳房偷吃进修班趣味挑战赛",
    "venue": "武侯吾悦广场",
    "city": "chengdu",
    "start_date": "2026-07-11",
    "end_date": "2026-07-12",
    "link": "http://m.toutiao.com/group/7660790323567723048/",
    "description": "老少皆宜免费参与的趣味挑战赛，宫廷御膳房场景氛围感十足，可换上特色穿搭化身趣味参赛者，玩法轻松有趣毫无门槛，超多丰厚好礼等你来拿。",
    "fee": "免费",
    "source": "武侯区文旅局",
    "family_friendly": True
})

activities.append({
    "title": "成都来福士森林清风沉浸式自然艺术装置",
    "venue": "成都来福士广场",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7660790323567723048/",
    "description": "把自然绿意、趣味艺术、文艺烟火搬进城市商圈，B1巫峡中庭森林清风、水波涟漪融入建筑，走进仿佛闯入城市秘境，夏日清凉打卡地，逛街遛娃两不误。",
    "fee": "免费",
    "source": "武侯区文旅局",
    "family_friendly": True
})

activities.append({
    "title": "BIGDAN全国首展《这么热的天，还要上班吗？》",
    "venue": "成都来福士广场",
    "city": "chengdu",
    "start_date": "2026-07-22",
    "end_date": "2026-08-31",
    "link": "http://m.toutiao.com/group/7660790323567723048/",
    "description": "超治愈的网红新展全国首展，以趣味主题精准戳中夏日心声，逛展还能免费解锁限定周边，亲子家庭拍照打卡好去处，轻松又有趣。",
    "fee": "免费",
    "source": "武侯区文旅局",
    "family_friendly": True
})

activities.append({
    "title": "十四行诗艺术手账市集",
    "venue": "成都来福士广场",
    "city": "chengdu",
    "start_date": "2026-08-01",
    "end_date": "2026-08-02",
    "link": "http://m.toutiao.com/group/7660790323567723048/",
    "description": "限时开市的浪漫手账市集，集结超多独立设计师原创好物，精致手账本、特色胶带、印章、贴纸一应俱全，还能偶遇插画师现场手绘创作，手账爱好者的天堂。",
    "fee": "免费",
    "source": "武侯区文旅局",
    "family_friendly": True
})

activities.append({
    "title": "都都学堂·主题暑假托管营（茶店子）",
    "venue": "茶店子街道党群服务中心",
    "city": "chengdu",
    "start_date": "2026-07-20",
    "end_date": "2026-08-28",
    "link": "https://m.sohu.com/a/1048654917_121106884/",
    "description": "唱成都童谣、玩成都游戏、学成都非遗的特色托管营，上午作业辅导下午特色课程，戏曲、美育、非遗、AI启蒙、科学实验、表达训练、安全教育全覆盖。",
    "fee": "收费（公益价格）",
    "source": "成都市文化馆",
    "family_friendly": True
})

activities.append({
    "title": "都都戏台国粹戏曲课堂",
    "venue": "茶店子街道党群服务中心",
    "city": "chengdu",
    "start_date": "2026-07-20",
    "end_date": "2026-08-28",
    "link": "https://m.sohu.com/a/1048654917_121106884/",
    "description": "携手成都京剧研究院专业戏曲老师授课，身段、唱腔、角色扮演沉浸式体验国粹，锻炼形体、克服怯场，深度感受中华传统文化魅力。",
    "fee": "收费（包含在托管营内）",
    "source": "成都市文化馆",
    "family_friendly": True
})

activities.append({
    "title": "温江夏趣潮玩运动季",
    "venue": "温江区旭辉Cmall及多地",
    "city": "chengdu",
    "start_date": "2026-06-19",
    "end_date": "2026-08-31",
    "link": "http://sc.cnr.cn/scpd/szlb/20260619/t20260619_527668474.shtml",
    "description": "9场特色活动，商圈亲子定向赛特别适合全家组队，家长带着孩子一起闯关打卡，飞盘、射箭、陆地冰壶、迷你高尔夫等十多款新潮运动，专业教练全程指导。",
    "fee": "部分免费",
    "source": "央广网",
    "family_friendly": True
})

# ==================== 8. 文化馆艺术培训 (10条) ====================

activities.append({
    "title": "成都市文化馆2026蓉文美育·趣学一夏暑期艺术班",
    "venue": "成都市文化馆",
    "city": "chengdu",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "http://m.toutiao.com/group/7651878047993332258/",
    "description": "38个公益基础班、264个教学班次普惠零基础爱好者；195个优惠提升班、2134个教学班次，少儿特色营开设小勇士拳击、配音表演、趣味烘焙、形意拳等特色课程。",
    "fee": "部分免费",
    "source": "成都市文化馆",
    "family_friendly": True
})

activities.append({
    "title": "少儿小勇士拳击暑期班",
    "venue": "成都市文化馆",
    "city": "chengdu",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "http://m.toutiao.com/group/7651878047993332258/",
    "description": "少儿特色拳击课程，强身健体，学习基础拳击动作与防身技能，培养意志力与自信心，专业教练指导，安全有保障。",
    "fee": "收费（公益价格）",
    "source": "成都市文化馆",
    "family_friendly": True
})

activities.append({
    "title": "少儿配音表演暑期班",
    "venue": "成都市文化馆",
    "city": "chengdu",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "http://m.toutiao.com/group/7651878047993332258/",
    "description": "少儿配音表演特色课程，学习声音塑造、台词表达、配音技巧，提升语言表达能力与自信心，发现声音的魅力，适合喜欢表演的孩子。",
    "fee": "收费（公益价格）",
    "source": "成都市文化馆",
    "family_friendly": True
})

activities.append({
    "title": "少儿趣味烘焙暑期班",
    "venue": "成都市文化馆",
    "city": "chengdu",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "http://m.toutiao.com/group/7651878047993332258/",
    "description": "趣味烘焙课程，学习制作各种小点心、蛋糕、饼干，锻炼动手能力，品尝自己的劳动成果，培养孩子对烘焙的兴趣与生活技能。",
    "fee": "收费（公益价格）",
    "source": "成都市文化馆",
    "family_friendly": True
})

activities.append({
    "title": "少儿形意拳暑期班",
    "venue": "成都市文化馆",
    "city": "chengdu",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "http://m.toutiao.com/group/7651878047993332258/",
    "description": "传统武术形意拳少儿班，强身健体，学习中华传统武术文化，培养孩子的毅力与专注力，专业武术老师授课。",
    "fee": "收费（公益价格）",
    "source": "成都市文化馆",
    "family_friendly": True
})

activities.append({
    "title": "艺术疗愈系列课程——动画疗愈心迹漫游",
    "venue": "成都市文化馆",
    "city": "chengdu",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "https://m.sohu.com/a/1043279146_121106884/",
    "description": "零基础适配教学，从剧本构思、画面搭建到拍摄成片全方位体验，帮孩子从零完成原创动画，收获专属作品，艺术创作+情绪疗愈+心智成长三重收获。",
    "fee": "收费（公益价格）",
    "source": "成都市文化馆",
    "family_friendly": True
})

activities.append({
    "title": "青少年AI素养通识特色课",
    "venue": "成都市文化馆",
    "city": "chengdu",
    "start_date": "2026-07-06",
    "end_date": "2026-08-30",
    "link": "https://m.sohu.com/a/1043279146_121106884/",
    "description": "四川广播电视台联合高校与成都市文化馆打造，以理解AI、善用AI、人机协同为核心目标，游戏化体验式项目式学习，建立面向未来的人工智能认知体系。",
    "fee": "收费（公益价格）",
    "source": "成都市文化馆",
    "family_friendly": True
})

activities.append({
    "title": "非遗烧箔画小件制作公益课",
    "venue": "成都市文化馆",
    "city": "chengdu",
    "start_date": "2026-07-10",
    "end_date": "2026-08-20",
    "link": "https://m.sohu.com/a/1043279146_121106884/",
    "description": "非遗烧箔画体验课程，沉浸式感受传统手作工艺魅力，学习烧箔画技法，完成自己的作品，了解非遗文化，适合亲子共同参与。",
    "fee": "免费需预约",
    "source": "成都市文化馆",
    "family_friendly": True
})

activities.append({
    "title": "壶中天地手作古典园林公益课",
    "venue": "成都市文化馆",
    "city": "chengdu",
    "start_date": "2026-07-15",
    "end_date": "2026-08-25",
    "link": "https://m.sohu.com/a/1043279146_121106884/",
    "description": "亲手打造微缩山水景致，学习中国古典园林造景艺术，培养审美能力与动手能力，作品可带回家作为装饰，非常适合亲子共同完成。",
    "fee": "免费需预约",
    "source": "成都市文化馆",
    "family_friendly": True
})

activities.append({
    "title": "成都市文化馆暑期青少年志愿者招募",
    "venue": "成都市文化馆",
    "city": "chengdu",
    "start_date": "2026-07-10",
    "end_date": "2026-08-15",
    "link": "https://m.sohu.com/a/1045462414_121106884/",
    "description": "面向14-17岁青少年的暑期志愿服务，现场管理协助青少年组，累计完成2次志愿服务且考核合格可获得志愿服务证书，含午餐，是社会实践的好机会。",
    "fee": "免费",
    "source": "成都市文化馆",
    "family_friendly": True
})

# ==================== 9. 自然户外与田园体验 (5条) ====================

activities.append({
    "title": "龙泉驿区水蜜桃采摘体验季",
    "venue": "龙泉驿区宝狮村、红花村等",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://wlt.sc.gov.cn/scwlt/hydt/2026/6/17/99b54c710a6042eca4552e4faa13b74f.shtml",
    "description": "中国水蜜桃之乡龙泉驿，20余个品种从5月下旬持续至8月，采摘价约10至18元/斤，四条水蜜桃采摘线路，亲子采摘体验田园乐趣，品尝新鲜水蜜桃。",
    "fee": "收费（按斤计价）",
    "source": "成都市农业农村局",
    "family_friendly": True
})

activities.append({
    "title": "德阳绵竹26℃的夏天亲子戏水避暑",
    "venue": "德阳绵竹山区镇域",
    "city": "chengdu",
    "start_date": "2026-07-10",
    "end_date": "2026-08-31",
    "link": "https://sichuan.scol.com.cn/m/ggxw/202607/83289984.html",
    "description": "酒香画境村游绵竹夏季系列活动，A线溯溪徒步寻凉之旅串联山区镇域，主打亲子戏水、峡谷漂流与森林徒步，26℃清凉夏天，成都周边亲子避暑好去处。",
    "fee": "部分免费",
    "source": "四川在线",
    "family_friendly": True
})

activities.append({
    "title": "蒲江明月村非遗匠心传承手作体验",
    "venue": "蒲江县明月村",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1042032692_121106884/",
    "description": "非遗匠心传承手作体验，参观明月村陶艺工坊，体验陶艺制作、蓝染等非遗手作，感受乡村文艺气息，亲子一日游或两日游都合适。",
    "fee": "收费",
    "source": "成都文旅",
    "family_friendly": True
})

activities.append({
    "title": "趣耍彭州山水诗韵文化研学路线",
    "venue": "彭州市",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://m.sohu.com/a/1042032692_121106884/",
    "description": "山水诗韵文化研学路线，彭州龙门山片区非遗万灯夜、古镇戏水非遗季及中医药非遗夜集，亲子在山水中学习文化，避暑与研学两不误。",
    "fee": "部分免费",
    "source": "成都文旅",
    "family_friendly": True
})

activities.append({
    "title": "双流区黄龙溪森林溪谷亲水游",
    "venue": "双流区黄龙溪森林溪谷",
    "city": "chengdu",
    "start_date": "2026-07-01",
    "end_date": "2026-08-31",
    "link": "https://wlt.sc.gov.cn/scwlt/hydt/2026/6/17/99b54c710a6042eca4552e4faa13b74f.shtml",
    "description": "森林溪谷清凉避暑，亲子戏水、森林徒步，亲近自然，夏日避暑好去处，与黄龙溪古镇联动，可安排一日游行程。",
    "fee": "部分免费",
    "source": "成都市农业农村局",
    "family_friendly": True
})

print(f"已生成 {len(activities)} 条活动数据")

# 保存到文件
output_path = "/workspace/goout/output/raw/real_activities_chengdu_batch3.json"
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(activities, f, ensure_ascii=False, indent=2)

print(f"已保存到 {output_path}")
