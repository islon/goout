# -*- coding: utf-8 -*-
"""
向 output/exhibitions.json 添加成都(chengdu)的300个暑期亲子活动数据。
涵盖10大类活动：博物馆研学、科技馆科普、公园自然、主题乐园、文化体验、
图书馆阅读、历史文化研学、体育运动、古镇民俗、商业综合体亲子活动。
"""
import json
import os

DATA_FILE = 'output/exhibitions.json'
OUTPUT_FILE = 'output/exhibitions.json'

# 各类别活动数据，每条包含：name, venue, district, start_date, end_date, fee,
# description, highlights, type。city 与 source 统一在下方补充。
new_activities = [
    # ========== 1. 博物馆研学活动（30个）==========
    {"name": "成都博物馆小小讲解员夏令营", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-05", "end_date": "2026-08-25", "fee": "免费需预约", "description": "成都博物馆小小讲解员夏令营，培养孩子表达能力与历史素养。", "highlights": ["讲解员", "博物馆", "表达能力"], "type": "研学"},
    {"name": "成都博物馆考古体验营", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-08", "end_date": "2026-08-20", "fee": "收费", "description": "模拟考古发掘，体验考古学家的工作日常，了解文物发掘过程。", "highlights": ["考古", "体验", "文物"], "type": "研学"},
    {"name": "成都博物馆文物拓印体验", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-10", "end_date": "2026-08-30", "fee": "收费", "description": "学习传统拓印技艺，亲手制作文物拓片，感受金石之美。", "highlights": ["拓印", "技艺", "文物"], "type": "研学"},
    {"name": "成都博物馆皮影戏展演亲子日", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-12", "end_date": "2026-08-18", "fee": "免费需预约", "description": "观看皮影戏展演，了解皮影历史，亲子共赏非遗艺术。", "highlights": ["皮影", "非遗", "亲子"], "type": "亲子活动"},
    {"name": "成都博物馆古代服饰体验", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-15", "end_date": "2026-08-28", "fee": "收费", "description": "试穿汉服等古代服饰，了解历代服饰文化，拍照留念。", "highlights": ["汉服", "服饰", "体验"], "type": "亲子活动"},
    {"name": "成都博物馆青铜器探秘", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-18", "end_date": "2026-08-22", "fee": "免费需预约", "description": "探索古蜀青铜器奥秘，了解青铜铸造工艺与纹饰含义。", "highlights": ["青铜器", "古蜀", "探秘"], "type": "研学"},
    {"name": "成都博物馆陶器修复体验", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-20", "end_date": "2026-09-06", "fee": "收费", "description": "学习陶器修复基本方法，体验文物修复师的匠心工艺。", "highlights": ["陶器", "修复", "匠心"], "type": "研学"},
    {"name": "成都博物馆汉代画像砖研学", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-22", "end_date": "2026-08-30", "fee": "免费需预约", "description": "研究汉代画像砖，解读汉代社会生活与生产场景。", "highlights": ["画像砖", "汉代", "研学"], "type": "研学"},
    {"name": "成都博物馆蜀锦文化课堂", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-25", "end_date": "2026-08-28", "fee": "收费", "description": "了解蜀锦历史与织造工艺，感受东方织锦艺术之美。", "highlights": ["蜀锦", "织造", "非遗"], "type": "研学"},
    {"name": "成都博物馆夜游博物馆活动", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费需预约", "description": "夏夜夜游博物馆，别样视角参观展陈，感受文化之夜。", "highlights": ["夜游", "博物馆", "夜场"], "type": "亲子活动"},
    {"name": "四川博物院小小讲解员培训", "venue": "四川博物院", "district": "武侯区", "start_date": "2026-07-06", "end_date": "2026-08-24", "fee": "免费需预约", "description": "四川博物院小小讲解员培训，系统学习讲解技巧与文物知识。", "highlights": ["讲解员", "培训", "文物"], "type": "研学"},
    {"name": "四川博物院文物拓印工坊", "venue": "四川博物院", "district": "武侯区", "start_date": "2026-07-09", "end_date": "2026-08-21", "fee": "收费", "description": "文物拓印工坊，在老师指导下完成拓片制作，带走作品。", "highlights": ["拓印", "工坊", "手作"], "type": "研学"},
    {"name": "四川博物院考古发掘模拟", "venue": "四川博物院", "district": "武侯区", "start_date": "2026-07-11", "end_date": "2026-08-27", "fee": "收费", "description": "模拟考古发掘现场，使用专业工具体验发掘全过程。", "highlights": ["考古", "模拟", "发掘"], "type": "研学"},
    {"name": "四川博物院藏羌绣体验", "venue": "四川博物院", "district": "武侯区", "start_date": "2026-07-14", "end_date": "2026-08-26", "fee": "免费需预约", "description": "体验藏族羌族刺绣工艺，了解少数民族纺织文化。", "highlights": ["藏羌绣", "民族", "刺绣"], "type": "亲子活动"},
    {"name": "四川博物院张大千画展研学", "venue": "四川博物院", "district": "武侯区", "start_date": "2026-07-16", "end_date": "2026-09-15", "fee": "免费需预约", "description": "张大千画作研学，临摹大师作品，了解国画技法。", "highlights": ["张大千", "国画", "临摹"], "type": "研学"},
    {"name": "四川博物院巴蜀青铜文化探秘", "venue": "四川博物院", "district": "武侯区", "start_date": "2026-07-19", "end_date": "2026-08-23", "fee": "免费需预约", "description": "巴蜀青铜文化探秘，了解古蜀文明与青铜礼器。", "highlights": ["青铜", "巴蜀", "文明"], "type": "研学"},
    {"name": "四川博物院民族服饰体验", "venue": "四川博物院", "district": "武侯区", "start_date": "2026-07-21", "end_date": "2026-08-29", "fee": "收费", "description": "试穿各民族服饰，了解四川多民族文化与服饰特色。", "highlights": ["民族服饰", "体验", "多元文化"], "type": "亲子活动"},
    {"name": "四川博物院书画临摹课堂", "venue": "四川博物院", "district": "武侯区", "start_date": "2026-07-24", "end_date": "2026-08-28", "fee": "收费", "description": "在馆藏书画前临摹学习，提升孩子国画鉴赏与创作能力。", "highlights": ["书画", "临摹", "课堂"], "type": "研学"},
    {"name": "四川博物院汉代陶俑研学", "venue": "四川博物院", "district": "武侯区", "start_date": "2026-07-26", "end_date": "2026-09-10", "fee": "免费需预约", "description": "研究汉代说唱俑等陶俑，了解汉代市井生活与艺术。", "highlights": ["陶俑", "汉代", "说唱俑"], "type": "研学"},
    {"name": "金沙遗址博物馆太阳神鸟探秘", "venue": "成都金沙遗址博物馆", "district": "青羊区", "start_date": "2026-07-05", "end_date": "2026-08-25", "fee": "需购票", "description": "探秘太阳神鸟金饰，了解古蜀太阳崇拜与金器工艺。", "highlights": ["太阳神鸟", "金器", "古蜀"], "type": "研学"},
    {"name": "金沙遗址博物馆古蜀玉器研学", "venue": "成都金沙遗址博物馆", "district": "青羊区", "start_date": "2026-07-08", "end_date": "2026-08-22", "fee": "需购票", "description": "研究古蜀玉器，了解玉琮玉璧等礼器与玉文化。", "highlights": ["玉器", "玉文化", "古蜀"], "type": "研学"},
    {"name": "金沙遗址博物馆象牙发掘体验", "venue": "成都金沙遗址博物馆", "district": "青羊区", "start_date": "2026-07-12", "end_date": "2026-08-28", "fee": "收费", "description": "模拟象牙发掘，了解古蜀祭祀文化与象牙堆积之谜。", "highlights": ["象牙", "发掘", "祭祀"], "type": "研学"},
    {"name": "金沙遗址博物馆金面具探秘", "venue": "成都金沙遗址博物馆", "district": "青羊区", "start_date": "2026-07-15", "end_date": "2026-09-05", "fee": "需购票", "description": "探秘金面具，了解古蜀金器铸造工艺与神秘面具文化。", "highlights": ["金面具", "金器", "古蜀"], "type": "研学"},
    {"name": "金沙遗址博物馆古蜀文明夏令营", "venue": "成都金沙遗址博物馆", "district": "青羊区", "start_date": "2026-07-18", "end_date": "2026-08-20", "fee": "收费", "description": "古蜀文明主题夏令营，多日深度研学，探索金沙奥秘。", "highlights": ["夏令营", "古蜀", "深度研学"], "type": "研学"},
    {"name": "武侯祠博物馆三国文化研学", "venue": "成都武侯祠博物馆", "district": "武侯区", "start_date": "2026-07-06", "end_date": "2026-08-24", "fee": "需购票", "description": "三国文化主题研学，走访武侯祠，了解蜀汉历史。", "highlights": ["三国", "武侯祠", "蜀汉"], "type": "研学"},
    {"name": "武侯祠博物馆诸葛亮智慧课堂", "venue": "成都武侯祠博物馆", "district": "武侯区", "start_date": "2026-07-13", "end_date": "2026-08-22", "fee": "收费", "description": "诸葛亮智慧课堂，讲述丞相故事，启迪孩子思辨能力。", "highlights": ["诸葛亮", "智慧", "思辨"], "type": "研学"},
    {"name": "杜甫草堂博物馆诗词研学营", "venue": "成都杜甫草堂博物馆", "district": "青羊区", "start_date": "2026-07-09", "end_date": "2026-08-21", "fee": "需购票", "description": "杜甫诗词研学营，诵读诗圣名篇，感受唐诗之美。", "highlights": ["杜甫", "诗词", "唐诗"], "type": "研学"},
    {"name": "杜甫草堂博物馆书法体验", "venue": "成都杜甫草堂博物馆", "district": "青羊区", "start_date": "2026-07-16", "end_date": "2026-08-28", "fee": "收费", "description": "在诗圣故里体验书法，临写杜甫诗句，传承书法艺术。", "highlights": ["书法", "杜甫", "体验"], "type": "研学"},
    {"name": "成都动物园小小饲养员体验", "venue": "成都动物园", "district": "成华区", "start_date": "2026-07-05", "end_date": "2026-08-30", "fee": "收费", "description": "小小饲养员体验，近距离接触动物，学习动物保护知识。", "highlights": ["饲养员", "动物", "保护"], "type": "亲子活动"},
    {"name": "成都动物园动物科普大讲堂", "venue": "成都动物园", "district": "成华区", "start_date": "2026-07-11", "end_date": "2026-08-27", "fee": "需购票", "description": "动物科普大讲堂，专家讲解动物习性，激发科学兴趣。", "highlights": ["科普", "动物", "讲堂"], "type": "亲子活动"},

    # ========== 2. 科技馆科普活动（30个）==========
    {"name": "四川科技馆科学实验秀", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-04", "end_date": "2026-08-30", "fee": "免费需预约", "description": "科学实验秀表演，干冰、液氮等趣味实验，引爆科学热情。", "highlights": ["实验秀", "科学", "趣味"], "type": "亲子活动"},
    {"name": "四川科技馆机器人编程夏令营", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-07", "end_date": "2026-08-21", "fee": "收费", "description": "机器人编程夏令营，学习图形化编程，动手搭建机器人。", "highlights": ["机器人", "编程", "夏令营"], "type": "研学"},
    {"name": "四川科技馆航天体验营", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-10", "end_date": "2026-08-25", "fee": "收费", "description": "航天体验营，模拟太空舱，了解火箭发射与空间站生活。", "highlights": ["航天", "太空", "体验"], "type": "研学"},
    {"name": "四川科技馆3D打印体验", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-13", "end_date": "2026-08-28", "fee": "免费需预约", "description": "3D打印体验，了解增材制造原理，打印专属小作品。", "highlights": ["3D打印", "制造", "体验"], "type": "亲子活动"},
    {"name": "四川科技馆机器人格斗赛", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-16", "end_date": "2026-08-23", "fee": "免费需预约", "description": "机器人格斗赛，操控机器人对战，感受科技竞技魅力。", "highlights": ["机器人", "格斗", "竞技"], "type": "亲子活动"},
    {"name": "四川科技馆VR太空漫步", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-19", "end_date": "2026-08-29", "fee": "收费", "description": "VR太空漫步，沉浸式体验太空行走，感受宇宙浩瀚。", "highlights": ["VR", "太空", "沉浸"], "type": "亲子活动"},
    {"name": "四川科技馆电磁大探索", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-22", "end_date": "2026-09-12", "fee": "免费需预约", "description": "电磁大探索，动手做电磁实验，理解电与磁的奥秘。", "highlights": ["电磁", "实验", "探索"], "type": "研学"},
    {"name": "四川科技馆声学奥秘课堂", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-25", "end_date": "2026-08-28", "fee": "收费", "description": "声学奥秘课堂，探究声音传播，制作简易乐器。", "highlights": ["声学", "声音", "乐器"], "type": "研学"},
    {"name": "四川科技馆光学实验工坊", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-28", "end_date": "2026-08-30", "fee": "收费", "description": "光学实验工坊，探究光的折射反射，制作光学玩具。", "highlights": ["光学", "实验", "工坊"], "type": "研学"},
    {"name": "四川科技馆生命科学探秘", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-30", "end_date": "2026-09-20", "fee": "免费需预约", "description": "生命科学探秘，了解人体与基因，探索生命奥秘。", "highlights": ["生命科学", "基因", "人体"], "type": "研学"},
    {"name": "四川科技馆无人机飞行体验", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-03", "end_date": "2026-08-22", "fee": "收费", "description": "无人机飞行体验，学习飞行原理，亲手操控无人机起降。", "highlights": ["无人机", "飞行", "操控"], "type": "亲子活动"},
    {"name": "四川科技馆编程创客营", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-06", "end_date": "2026-08-20", "fee": "收费", "description": "编程创客营，结合软硬件，开发创意互动作品。", "highlights": ["编程", "创客", "创意"], "type": "研学"},
    {"name": "四川科技馆人工智能启蒙", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-09", "end_date": "2026-08-26", "fee": "收费", "description": "人工智能启蒙课程，了解AI原理，体验图像识别应用。", "highlights": ["人工智能", "AI", "启蒙"], "type": "研学"},
    {"name": "四川科技馆化学魔法秀", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-12", "end_date": "2026-08-28", "fee": "免费需预约", "description": "化学魔法秀，变色反应与发光实验，感受化学魅力。", "highlights": ["化学", "魔法", "实验"], "type": "亲子活动"},
    {"name": "四川科技馆力学乐园", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-15", "end_date": "2026-08-30", "fee": "免费需预约", "description": "力学乐园，杠杆滑轮斜面实验，在游戏中理解力学。", "highlights": ["力学", "杠杆", "游戏"], "type": "亲子活动"},
    {"name": "四川科技馆天文观星夜", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-18", "end_date": "2026-08-25", "fee": "收费", "description": "天文观星夜，使用天文望远镜观测星空，认识星座。", "highlights": ["天文", "观星", "望远镜"], "type": "亲子活动"},
    {"name": "四川科技馆火箭模型制作", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-21", "end_date": "2026-09-08", "fee": "收费", "description": "火箭模型制作，了解火箭结构，制作并发射水火箭。", "highlights": ["火箭", "模型", "水火箭"], "type": "研学"},
    {"name": "四川科技馆机器人足球赛", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-24", "end_date": "2026-08-29", "fee": "免费需预约", "description": "机器人足球赛，编程控制机器人踢球，培养协作能力。", "highlights": ["机器人", "足球", "编程"], "type": "亲子活动"},
    {"name": "四川科技馆恐龙化石探秘", "venue": "四川科技馆", "district": "青羊区", "start_date": "2026-07-27", "end_date": "2026-09-15", "fee": "免费需预约", "description": "恐龙化石探秘，了解恐龙时代，模拟化石发掘。", "highlights": ["恐龙", "化石", "探秘"], "type": "研学"},
    {"name": "环球中心海洋乐园科普日", "venue": "环球中心天堂岛海洋乐园", "district": "高新区", "start_date": "2026-07-05", "end_date": "2026-08-30", "fee": "需购票", "description": "海洋乐园科普日，了解海洋生态，亲子戏水学知识。", "highlights": ["海洋", "科普", "戏水"], "type": "亲子活动"},
    {"name": "环球中心海洋乐园亲子戏水节", "venue": "环球中心天堂岛海洋乐园", "district": "高新区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "需购票", "description": "亲子戏水节，巨大造浪池与水滑梯，清凉一夏。", "highlights": ["戏水", "造浪", "清凉"], "type": "亲子活动"},
    {"name": "环球中心海洋乐园夏夜派对", "venue": "环球中心天堂岛海洋乐园", "district": "高新区", "start_date": "2026-07-10", "end_date": "2026-08-25", "fee": "需购票", "description": "夏夜派对，室内沙滩夜场，灯光音乐与亲子互动。", "highlights": ["夜场", "派对", "沙滩"], "type": "亲子活动"},
    {"name": "海昌极地海洋公园企鹅科普", "venue": "成都海昌极地海洋公园", "district": "天府新区", "start_date": "2026-07-04", "end_date": "2026-08-28", "fee": "需购票", "description": "企鹅科普讲堂，了解极地企鹅生活，参与互动问答。", "highlights": ["企鹅", "极地", "科普"], "type": "亲子活动"},
    {"name": "海昌极地海洋公园白鲸表演", "venue": "成都海昌极地海洋公园", "district": "天府新区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "需购票", "description": "白鲸表演秀，海洋精灵与驯养员共舞，震撼视听。", "highlights": ["白鲸", "表演", "海洋"], "type": "演出"},
    {"name": "海昌极地海洋公园海洋生物研学", "venue": "成都海昌极地海洋公园", "district": "天府新区", "start_date": "2026-07-08", "end_date": "2026-08-26", "fee": "收费", "description": "海洋生物研学，了解极地与海洋生物习性，完成研学手册。", "highlights": ["海洋生物", "研学", "极地"], "type": "研学"},
    {"name": "海昌极地海洋公园海豚互动", "venue": "成都海昌极地海洋公园", "district": "天府新区", "start_date": "2026-07-12", "end_date": "2026-08-30", "fee": "收费", "description": "海豚互动体验，与海豚近距离接触，感受海洋智慧。", "highlights": ["海豚", "互动", "亲密"], "type": "亲子活动"},
    {"name": "海昌极地海洋公园北极熊探秘", "venue": "成都海昌极地海洋公园", "district": "天府新区", "start_date": "2026-07-16", "end_date": "2026-09-10", "fee": "需购票", "description": "北极熊探秘，观察北极熊行为，了解极地环境保护。", "highlights": ["北极熊", "极地", "环保"], "type": "研学"},
    {"name": "海昌极地海洋公园深海夜宿", "venue": "成都海昌极地海洋公园", "district": "天府新区", "start_date": "2026-07-20", "end_date": "2026-08-25", "fee": "收费", "description": "深海夜宿，在海洋馆搭帐篷过夜，与鱼群共眠。", "highlights": ["夜宿", "帐篷", "海洋馆"], "type": "亲子活动"},
    {"name": "海昌极地海洋公园鲨鱼科普", "venue": "成都海昌极地海洋公园", "district": "天府新区", "start_date": "2026-07-23", "end_date": "2026-09-05", "fee": "需购票", "description": "鲨鱼科普讲堂，了解鲨鱼种类与生态，破除恐惧。", "highlights": ["鲨鱼", "科普", "生态"], "type": "研学"},
    {"name": "海昌极地海洋公园海洋环保课堂", "venue": "成都海昌极地海洋公园", "district": "天府新区", "start_date": "2026-07-26", "end_date": "2026-08-29", "fee": "收费", "description": "海洋环保课堂，学习减少塑料污染，做海洋小卫士。", "highlights": ["环保", "海洋", "卫士"], "type": "研学"},

    # ========== 3. 公园自然活动（30个）==========
    {"name": "人民公园夏日观鸟活动", "venue": "人民公园", "district": "青羊区", "start_date": "2026-07-05", "end_date": "2026-08-30", "fee": "免费", "description": "人民公园夏日观鸟，携带望远镜观察城市常见鸟类。", "highlights": ["观鸟", "望远镜", "城市"], "type": "亲子活动"},
    {"name": "人民公园盖碗茶文化体验", "venue": "人民公园", "district": "青羊区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "盖碗茶文化体验，在鹤鸣茶社学泡盖碗茶，感受慢生活。", "highlights": ["盖碗茶", "茶社", "慢生活"], "type": "亲子活动"},
    {"name": "人民公园荷塘摄影日", "venue": "人民公园", "district": "青羊区", "start_date": "2026-07-10", "end_date": "2026-08-20", "fee": "免费", "description": "荷塘摄影日，夏日荷花盛开，亲子摄影打卡。", "highlights": ["荷花", "摄影", "打卡"], "type": "亲子活动"},
    {"name": "浣花溪公园植物认知课", "venue": "浣花溪公园", "district": "青羊区", "start_date": "2026-07-06", "end_date": "2026-08-25", "fee": "免费", "description": "植物认知课，老师带领识别公园植物，制作自然笔记。", "highlights": ["植物", "认知", "自然笔记"], "type": "研学"},
    {"name": "浣花溪公园夏日寻虫记", "venue": "浣花溪公园", "district": "青羊区", "start_date": "2026-07-09", "end_date": "2026-08-28", "fee": "免费", "description": "夏日寻虫记，观察昆虫生活，了解城市昆虫生态。", "highlights": ["昆虫", "寻虫", "生态"], "type": "亲子活动"},
    {"name": "浣花溪公园诗歌朗诵会", "venue": "浣花溪公园", "district": "青羊区", "start_date": "2026-07-13", "end_date": "2026-08-23", "fee": "免费", "description": "诗歌朗诵会，在诗圣故里诵读经典，感受诗意。", "highlights": ["诗歌", "朗诵", "诗意"], "type": "亲子活动"},
    {"name": "白鹭湾湿地公园观鸟营", "venue": "白鹭湾湿地公园", "district": "锦江区", "start_date": "2026-07-04", "end_date": "2026-08-27", "fee": "免费", "description": "白鹭湾观鸟营，观察白鹭等水鸟，学习鸟类知识。", "highlights": ["白鹭", "观鸟", "湿地"], "type": "研学"},
    {"name": "白鹭湾湿地公园骑行寻宝", "venue": "白鹭湾湿地公园", "district": "锦江区", "start_date": "2026-07-08", "end_date": "2026-08-30", "fee": "免费", "description": "骑行寻宝，环湿地骑行，按图索骥完成自然寻宝任务。", "highlights": ["骑行", "寻宝", "湿地"], "type": "亲子活动"},
    {"name": "白鹭湾湿地公园生态课堂", "venue": "白鹭湾湿地公园", "district": "锦江区", "start_date": "2026-07-12", "end_date": "2026-08-26", "fee": "免费", "description": "生态课堂，了解湿地净化水质功能，做湿地小卫士。", "highlights": ["生态", "湿地", "水质"], "type": "研学"},
    {"name": "白鹭湾湿地夏日露营节", "venue": "白鹭湾湿地公园", "district": "锦江区", "start_date": "2026-07-16", "end_date": "2026-08-22", "fee": "收费", "description": "夏日露营节，湿地旁搭帐篷，看星星听虫鸣。", "highlights": ["露营", "帐篷", "星空"], "type": "亲子活动"},
    {"name": "青龙湖湿地公园骑行日", "venue": "青龙湖湿地公园", "district": "龙泉驿区", "start_date": "2026-07-05", "end_date": "2026-08-31", "fee": "免费", "description": "青龙湖骑行日，环湖绿道骑行，享受湖光山色。", "highlights": ["骑行", "绿道", "湖光"], "type": "亲子活动"},
    {"name": "青龙湖湿地公园观鸟研学", "venue": "青龙湖湿地公园", "district": "龙泉驿区", "start_date": "2026-07-09", "end_date": "2026-08-28", "fee": "免费", "description": "青龙湖观鸟研学，观察湖边候鸟，完成观鸟记录。", "highlights": ["观鸟", "候鸟", "记录"], "type": "研学"},
    {"name": "青龙湖湿地公园亲子露营", "venue": "青龙湖湿地公园", "district": "龙泉驿区", "start_date": "2026-07-13", "end_date": "2026-08-25", "fee": "收费", "description": "亲子露营，湖畔草坪扎营，户外烧烤与亲子游戏。", "highlights": ["露营", "烧烤", "亲子"], "type": "亲子活动"},
    {"name": "青龙湖湿地公园皮划艇体验", "venue": "青龙湖湿地公园", "district": "龙泉驿区", "start_date": "2026-07-18", "end_date": "2026-08-30", "fee": "收费", "description": "皮划艇体验，在青龙湖上划艇，感受水上运动乐趣。", "highlights": ["皮划艇", "水上", "运动"], "type": "亲子活动"},
    {"name": "兴隆湖湿地公园湖畔露营", "venue": "兴隆湖湿地公园", "district": "天府新区", "start_date": "2026-07-04", "end_date": "2026-08-31", "fee": "收费", "description": "湖畔露营，兴隆湖边扎营，欣赏日落与夜景。", "highlights": ["露营", "日落", "夜景"], "type": "亲子活动"},
    {"name": "兴隆湖湿地公园环湖骑行", "venue": "兴隆湖湿地公园", "district": "天府新区", "start_date": "2026-07-08", "end_date": "2026-08-30", "fee": "免费", "description": "环湖骑行，十公里绿道，挑战自我欣赏湖景。", "highlights": ["骑行", "环湖", "挑战"], "type": "亲子活动"},
    {"name": "兴隆湖湿地公园皮划艇", "venue": "兴隆湖湿地公园", "district": "天府新区", "start_date": "2026-07-12", "end_date": "2026-08-28", "fee": "收费", "description": "兴隆湖皮划艇，宽阔湖面畅划，体验水上自由。", "highlights": ["皮划艇", "湖面", "自由"], "type": "亲子活动"},
    {"name": "兴隆湖湿地公园星空观测", "venue": "兴隆湖湿地公园", "district": "天府新区", "start_date": "2026-07-16", "end_date": "2026-08-26", "fee": "免费", "description": "星空观测，远离城市灯光，用望远镜观测夏季星空。", "highlights": ["星空", "观测", "望远镜"], "type": "亲子活动"},
    {"name": "成都植物园夏日植物认知", "venue": "成都植物园", "district": "新都区", "start_date": "2026-07-06", "end_date": "2026-08-28", "fee": "免费需预约", "description": "夏日植物认知，专业老师讲解，识别百种植物。", "highlights": ["植物", "认知", "百种"], "type": "研学"},
    {"name": "成都植物园多肉种植体验", "venue": "成都植物园", "district": "新都区", "start_date": "2026-07-10", "end_date": "2026-08-30", "fee": "收费", "description": "多肉种植体验，亲手栽种多肉，带走萌趣小盆栽。", "highlights": ["多肉", "种植", "盆栽"], "type": "亲子活动"},
    {"name": "成都植物园标本制作课堂", "venue": "成都植物园", "district": "新都区", "start_date": "2026-07-14", "end_date": "2026-08-26", "fee": "收费", "description": "标本制作课堂，采集落叶制作植物标本画。", "highlights": ["标本", "植物", "手作"], "type": "研学"},
    {"name": "成都植物园药用植物探秘", "venue": "成都植物园", "district": "新都区", "start_date": "2026-07-18", "end_date": "2026-09-10", "fee": "免费需预约", "description": "药用植物探秘，了解身边的中草药，学习传统药理。", "highlights": ["药用植物", "中草药", "药理"], "type": "研学"},
    {"name": "成都植物园亲子插花课", "venue": "成都植物园", "district": "新都区", "start_date": "2026-07-22", "end_date": "2026-08-29", "fee": "收费", "description": "亲子插花课，学习花艺基础，创作专属插花作品。", "highlights": ["插花", "花艺", "创作"], "type": "亲子活动"},
    {"name": "三圣花乡荷塘月色赏荷", "venue": "三圣花乡", "district": "锦江区", "start_date": "2026-07-01", "end_date": "2026-08-20", "fee": "免费", "description": "荷塘月色赏荷，百亩荷花盛开，亲子赏花拍照。", "highlights": ["荷花", "赏花", "拍照"], "type": "亲子活动"},
    {"name": "三圣花乡花田摄影日", "venue": "三圣花乡", "district": "锦江区", "start_date": "2026-07-05", "end_date": "2026-08-25", "fee": "免费", "description": "花田摄影日，多彩花海取景，亲子摄影留念。", "highlights": ["花田", "摄影", "花海"], "type": "亲子活动"},
    {"name": "三圣花乡农家采摘体验", "venue": "三圣花乡", "district": "锦江区", "start_date": "2026-07-09", "end_date": "2026-08-30", "fee": "收费", "description": "农家采摘体验，采摘时令蔬果，体验田园生活。", "highlights": ["采摘", "蔬果", "田园"], "type": "亲子活动"},
    {"name": "三圣花乡亲子绘画写生", "venue": "三圣花乡", "district": "锦江区", "start_date": "2026-07-13", "end_date": "2026-08-28", "fee": "收费", "description": "亲子绘画写生，在花田中写生，培养艺术感受力。", "highlights": ["写生", "绘画", "艺术"], "type": "亲子活动"},
    {"name": "三圣花乡花艺手作课堂", "venue": "三圣花乡", "district": "锦江区", "start_date": "2026-07-17", "end_date": "2026-08-26", "fee": "收费", "description": "花艺手作课堂，制作干花书签与花环，留下夏日记忆。", "highlights": ["花艺", "干花", "手作"], "type": "亲子活动"},
    {"name": "白鹭湾湿地夏日观鹭", "venue": "白鹭湾湿地公园", "district": "锦江区", "start_date": "2026-07-20", "end_date": "2026-08-27", "fee": "免费", "description": "夏日观鹭，定点观察白鹭栖息，了解鹭鸟生态。", "highlights": ["白鹭", "栖息", "生态"], "type": "研学"},
    {"name": "人民公园鹤鸣茶社亲子茶艺", "venue": "人民公园", "district": "青羊区", "start_date": "2026-07-15", "end_date": "2026-08-29", "fee": "收费", "description": "鹤鸣茶社亲子茶艺，学习盖碗茶冲泡，品味川茶文化。", "highlights": ["鹤鸣茶社", "茶艺", "川茶"], "type": "亲子活动"},

    # ========== 4. 主题乐园活动（30个）==========
    {"name": "成都欢乐谷水上狂欢节", "venue": "成都欢乐谷", "district": "金牛区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "需购票", "description": "水上狂欢节，造浪池与水滑道，全家清凉嗨翻天。", "highlights": ["水上", "狂欢", "清凉"], "type": "亲子活动"},
    {"name": "成都欢乐谷夜场派对", "venue": "成都欢乐谷", "district": "金牛区", "start_date": "2026-07-05", "end_date": "2026-08-30", "fee": "需购票", "description": "夜场派对，灯光秀与电音，夏夜畅玩游乐设施。", "highlights": ["夜场", "灯光", "电音"], "type": "亲子活动"},
    {"name": "成都欢乐谷亲子嘉年华", "venue": "成都欢乐谷", "district": "金牛区", "start_date": "2026-07-10", "end_date": "2026-08-28", "fee": "需购票", "description": "亲子嘉年华，游乐项目与亲子互动游戏全家齐欢乐。", "highlights": ["嘉年华", "游乐", "互动"], "type": "亲子活动"},
    {"name": "成都欢乐谷过山车挑战日", "venue": "成都欢乐谷", "district": "金牛区", "start_date": "2026-07-14", "end_date": "2026-08-26", "fee": "需购票", "description": "过山车挑战日，挑战多条刺激过山车，勇气大考验。", "highlights": ["过山车", "挑战", "勇气"], "type": "亲子活动"},
    {"name": "成都欢乐谷夏日电音节", "venue": "成都欢乐谷", "district": "金牛区", "start_date": "2026-07-18", "end_date": "2026-08-22", "fee": "需购票", "description": "夏日电音节，DJ现场打碟，灯光舞美震撼演出。", "highlights": ["电音", "DJ", "演出"], "type": "演出"},
    {"name": "成都欢乐谷花车巡游", "venue": "成都欢乐谷", "district": "金牛区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "需购票", "description": "花车巡游，主题花车与卡通人偶巡游，亲子互动合影。", "highlights": ["花车", "巡游", "人偶"], "type": "演出"},
    {"name": "成都欢乐谷万圣夜场预热", "venue": "成都欢乐谷", "district": "金牛区", "start_date": "2026-08-20", "end_date": "2026-10-31", "fee": "需购票", "description": "万圣夜场预热，主题鬼屋与Cosplay，惊悚又欢乐。", "highlights": ["万圣", "鬼屋", "Cosplay"], "type": "亲子活动"},
    {"name": "成都欢乐谷亲子游乐挑战", "venue": "成都欢乐谷", "district": "金牛区", "start_date": "2026-07-22", "end_date": "2026-08-29", "fee": "需购票", "description": "亲子游乐挑战，完成打卡任务赢取纪念奖品。", "highlights": ["挑战", "打卡", "奖品"], "type": "亲子活动"},
    {"name": "成都融创水世界夏日狂欢", "venue": "成都融创水世界", "district": "都江堰市", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "需购票", "description": "夏日狂欢，室内恒温水世界，四季畅玩不受天气影响。", "highlights": ["水世界", "恒温", "室内"], "type": "亲子活动"},
    {"name": "成都融创水世界夜场派对", "venue": "成都融创水世界", "district": "都江堰市", "start_date": "2026-07-06", "end_date": "2026-08-28", "fee": "需购票", "description": "夜场派对，水上灯光秀，夜场畅玩所有水上游乐。", "highlights": ["夜场", "灯光", "水上"], "type": "亲子活动"},
    {"name": "成都融创水世界亲子戏水节", "venue": "成都融创水世界", "district": "都江堰市", "start_date": "2026-07-10", "end_date": "2026-08-30", "fee": "需购票", "description": "亲子戏水节，儿童戏水区与家庭滑道，全家齐欢乐。", "highlights": ["戏水", "家庭", "滑道"], "type": "亲子活动"},
    {"name": "成都融创水世界造浪池派对", "venue": "成都融创水世界", "district": "都江堰市", "start_date": "2026-07-14", "end_date": "2026-08-26", "fee": "需购票", "description": "造浪池派对，模拟海浪，随浪起伏尽享清凉。", "highlights": ["造浪", "海浪", "清凉"], "type": "亲子活动"},
    {"name": "成都融创水世界滑道挑战赛", "venue": "成都融创水世界", "district": "都江堰市", "start_date": "2026-07-18", "end_date": "2026-08-29", "fee": "需购票", "description": "滑道挑战赛，多条刺激滑道比拼速度与勇气。", "highlights": ["滑道", "挑战", "速度"], "type": "亲子活动"},
    {"name": "成都融创水世界儿童水上乐园", "venue": "成都融创水世界", "district": "都江堰市", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "需购票", "description": "儿童水上乐园，浅水区与趣味喷水装置，幼儿也安心。", "highlights": ["儿童", "浅水", "喷水"], "type": "亲子活动"},
    {"name": "成都融创雪世界夏日滑雪", "venue": "成都融创水世界", "district": "都江堰市", "start_date": "2026-07-05", "end_date": "2026-08-30", "fee": "需购票", "description": "夏日滑雪，室内雪场反季体验，炎夏感受冰雪乐趣。", "highlights": ["滑雪", "室内", "冰雪"], "type": "亲子活动"},
    {"name": "成都国色天乡乐园水上狂欢", "venue": "成都国色天乡乐园", "district": "温江区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "需购票", "description": "水上狂欢，主题水上乐园，全家畅玩清凉一夏。", "highlights": ["水上", "狂欢", "乐园"], "type": "亲子活动"},
    {"name": "成都国色天乡乐园夜场嘉年华", "venue": "成都国色天乡乐园", "district": "温江区", "start_date": "2026-07-05", "end_date": "2026-08-28", "fee": "需购票", "description": "夜场嘉年华，灯光与音乐交织，夜场畅玩不停。", "highlights": ["夜场", "嘉年华", "灯光"], "type": "亲子活动"},
    {"name": "成都国色天乡乐园亲子游乐日", "venue": "成都国色天乡乐园", "district": "温江区", "start_date": "2026-07-10", "end_date": "2026-08-30", "fee": "需购票", "description": "亲子游乐日，旋转木马与摩天轮，温馨亲子时光。", "highlights": ["游乐", "摩天轮", "温馨"], "type": "亲子活动"},
    {"name": "成都国色天乡乐园花车巡游", "venue": "成都国色天乡乐园", "district": "温江区", "start_date": "2026-07-14", "end_date": "2026-08-26", "fee": "需购票", "description": "花车巡游，主题花车与卡通人物巡游互动。", "highlights": ["花车", "巡游", "卡通"], "type": "演出"},
    {"name": "成都国色天乡乐园童话节", "venue": "成都国色天乡乐园", "district": "温江区", "start_date": "2026-07-18", "end_date": "2026-08-22", "fee": "需购票", "description": "童话节，经典童话人物齐聚，沉浸式童话体验。", "highlights": ["童话", "沉浸", "经典"], "type": "亲子活动"},
    {"name": "成都国色天乡乐园旋转木马派对", "venue": "成都国色天乡乐园", "district": "温江区", "start_date": "2026-07-22", "end_date": "2026-08-29", "fee": "需购票", "description": "旋转木马派对，梦幻灯光下乘坐旋转木马，拍照打卡。", "highlights": ["旋转木马", "梦幻", "拍照"], "type": "亲子活动"},
    {"name": "成都国色天乡乐园摩天轮之夜", "venue": "成都国色天乡乐园", "district": "温江区", "start_date": "2026-07-26", "end_date": "2026-08-30", "fee": "需购票", "description": "摩天轮之夜，高空俯瞰乐园夜景，浪漫亲子时刻。", "highlights": ["摩天轮", "夜景", "高空"], "type": "亲子活动"},
    {"name": "成都国色天乡乐园夏日音乐节", "venue": "成都国色天乡乐园", "district": "温江区", "start_date": "2026-07-30", "end_date": "2026-08-28", "fee": "需购票", "description": "夏日音乐节，乐队现场演出，亲子共赏户外音乐。", "highlights": ["音乐节", "乐队", "户外"], "type": "演出"},
    {"name": "成都海昌极地海洋公园水上乐园", "venue": "成都海昌极地海洋公园", "district": "天府新区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "需购票", "description": "水上乐园，海洋主题戏水区，清凉与科普结合。", "highlights": ["水上", "海洋主题", "戏水"], "type": "亲子活动"},
    {"name": "成都海昌极地海洋公园夜场派对", "venue": "成都海昌极地海洋公园", "district": "天府新区", "start_date": "2026-07-06", "end_date": "2026-08-28", "fee": "需购票", "description": "夜场派对，海洋馆夜场开放，灯光与海洋生物共舞。", "highlights": ["夜场", "灯光", "海洋"], "type": "亲子活动"},
    {"name": "成都海昌极地海洋公园夏日狂欢", "venue": "成都海昌极地海洋公园", "district": "天府新区", "start_date": "2026-07-10", "end_date": "2026-08-30", "fee": "需购票", "description": "夏日狂欢，海洋生物表演与戏水结合，全家欢乐。", "highlights": ["狂欢", "表演", "戏水"], "type": "亲子活动"},
    {"name": "成都海昌极地海洋公园花车巡游", "venue": "成都海昌极地海洋公园", "district": "天府新区", "start_date": "2026-07-14", "end_date": "2026-08-26", "fee": "需购票", "description": "花车巡游，海洋主题花车与卡通人偶巡游互动。", "highlights": ["花车", "海洋", "巡游"], "type": "演出"},
    {"name": "成都海昌极地海洋公园亲子嘉年华", "venue": "成都海昌极地海洋公园", "district": "天府新区", "start_date": "2026-07-18", "end_date": "2026-08-29", "fee": "需购票", "description": "亲子嘉年华，海洋知识闯关与亲子游戏相结合。", "highlights": ["嘉年华", "闯关", "亲子"], "type": "亲子活动"},
    {"name": "成都融创乐园主题游乐日", "venue": "成都融创水世界", "district": "都江堰市", "start_date": "2026-07-22", "end_date": "2026-08-30", "fee": "需购票", "description": "主题游乐日，蜀文化主题乐园，游乐与演艺结合。", "highlights": ["主题", "蜀文化", "演艺"], "type": "亲子活动"},
    {"name": "成都欢乐谷亲子魔法秀", "venue": "成都欢乐谷", "district": "金牛区", "start_date": "2026-07-26", "end_date": "2026-08-29", "fee": "需购票", "description": "亲子魔法秀，魔术师现场表演，邀请小朋友上台互动。", "highlights": ["魔法", "魔术", "互动"], "type": "演出"},

    # ========== 5. 文化体验活动（30个）==========
    {"name": "宽窄巷子川剧变脸体验", "venue": "宽窄巷子", "district": "青羊区", "start_date": "2026-07-04", "end_date": "2026-08-30", "fee": "收费", "description": "川剧变脸体验，近距离观看变脸，学习基本身段。", "highlights": ["川剧", "变脸", "身段"], "type": "亲子活动"},
    {"name": "宽窄巷子蜀绣体验课堂", "venue": "宽窄巷子", "district": "青羊区", "start_date": "2026-07-08", "end_date": "2026-08-28", "fee": "收费", "description": "蜀绣体验课堂，在绣娘指导下绣制简单图案。", "highlights": ["蜀绣", "绣娘", "手作"], "type": "亲子活动"},
    {"name": "宽窄巷子皮影制作工坊", "venue": "宽窄巷子", "district": "青羊区", "start_date": "2026-07-12", "end_date": "2026-08-26", "fee": "收费", "description": "皮影制作工坊，亲手制作皮影人物并上台表演。", "highlights": ["皮影", "制作", "表演"], "type": "亲子活动"},
    {"name": "宽窄巷子盖碗茶艺体验", "venue": "宽窄巷子", "district": "青羊区", "start_date": "2026-07-16", "end_date": "2026-08-30", "fee": "收费", "description": "盖碗茶艺体验，学习川式盖碗茶冲泡礼仪与文化。", "highlights": ["盖碗茶", "茶艺", "礼仪"], "type": "亲子活动"},
    {"name": "宽窄巷子糖画手作", "venue": "宽窄巷子", "district": "青羊区", "start_date": "2026-07-20", "end_date": "2026-08-29", "fee": "收费", "description": "糖画手作，跟随糖画艺人用糖稀绘制生肖图案。", "highlights": ["糖画", "糖稀", "生肖"], "type": "亲子活动"},
    {"name": "宽窄巷子捏面人体验", "venue": "宽窄巷子", "district": "青羊区", "start_date": "2026-07-24", "end_date": "2026-08-28", "fee": "收费", "description": "捏面人体验，学习面塑基础，捏制卡通面人。", "highlights": ["捏面人", "面塑", "卡通"], "type": "亲子活动"},
    {"name": "宽窄巷子剪纸艺术课堂", "venue": "宽窄巷子", "district": "青羊区", "start_date": "2026-07-28", "end_date": "2026-09-12", "fee": "收费", "description": "剪纸艺术课堂，学习传统剪纸技法，剪出窗花作品。", "highlights": ["剪纸", "窗花", "传统"], "type": "亲子活动"},
    {"name": "宽窄巷子川剧变脸表演", "venue": "宽窄巷子", "district": "青羊区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "川剧变脸表演专场，绝活变脸吐火，震撼视听。", "highlights": ["变脸", "吐火", "绝活"], "type": "演出"},
    {"name": "宽窄巷子掏耳朵民俗体验", "venue": "宽窄巷子", "district": "青羊区", "start_date": "2026-07-05", "end_date": "2026-08-30", "fee": "收费", "description": "掏耳朵民俗体验，体验成都采耳绝技，感受慢生活。", "highlights": ["采耳", "民俗", "慢生活"], "type": "亲子活动"},
    {"name": "锦里川剧变脸专场", "venue": "锦里", "district": "武侯区", "start_date": "2026-07-03", "end_date": "2026-08-30", "fee": "收费", "description": "锦里川剧变脸专场，古街戏台看变脸，沉浸三国氛围。", "highlights": ["变脸", "戏台", "三国"], "type": "演出"},
    {"name": "锦里蜀绣手作课堂", "venue": "锦里", "district": "武侯区", "start_date": "2026-07-07", "end_date": "2026-08-28", "fee": "收费", "description": "锦里蜀绣手作课堂，古街中体验非遗蜀绣技艺。", "highlights": ["蜀绣", "非遗", "古街"], "type": "亲子活动"},
    {"name": "锦里皮影戏表演", "venue": "锦里", "district": "武侯区", "start_date": "2026-07-11", "end_date": "2026-08-26", "fee": "收费", "description": "锦里皮影戏表演，传统皮影戏讲述三国故事。", "highlights": ["皮影", "三国", "传统"], "type": "演出"},
    {"name": "锦里糖画亲子体验", "venue": "锦里", "district": "武侯区", "start_date": "2026-07-15", "end_date": "2026-08-30", "fee": "收费", "description": "锦里糖画亲子体验，老艺人手把手教孩子画糖画。", "highlights": ["糖画", "艺人", "亲子"], "type": "亲子活动"},
    {"name": "锦里三国主题巡游", "venue": "锦里", "district": "武侯区", "start_date": "2026-07-19", "end_date": "2026-08-29", "fee": "免费", "description": "三国主题巡游，人物扮演巡游古街，沉浸式体验。", "highlights": ["三国", "巡游", "扮演"], "type": "亲子活动"},
    {"name": "锦里茶艺表演", "venue": "锦里", "district": "武侯区", "start_date": "2026-07-23", "end_date": "2026-08-28", "fee": "收费", "description": "锦里茶艺表演，长嘴壶茶艺绝活，赏心悦目。", "highlights": ["茶艺", "长嘴壶", "绝活"], "type": "演出"},
    {"name": "锦里川派古琴体验", "venue": "锦里", "district": "武侯区", "start_date": "2026-07-27", "end_date": "2026-09-10", "fee": "收费", "description": "川派古琴体验，聆听古琴雅韵，学习抚琴基础。", "highlights": ["古琴", "川派", "雅韵"], "type": "亲子活动"},
    {"name": "锦里民俗手作市集", "venue": "锦里", "district": "武侯区", "start_date": "2026-07-30", "end_date": "2026-08-30", "fee": "免费", "description": "民俗手作市集，汇聚非遗手作，逛市集体验民俗。", "highlights": ["市集", "手作", "非遗"], "type": "亲子活动"},
    {"name": "锦里灯谜会亲子日", "venue": "锦里", "district": "武侯区", "start_date": "2026-08-05", "end_date": "2026-08-28", "fee": "免费", "description": "灯谜会亲子日，猜灯谜赢小礼品，感受传统民俗。", "highlights": ["灯谜", "猜谜", "民俗"], "type": "亲子活动"},
    {"name": "蜀锦织绣博物馆蜀绣体验", "venue": "蜀锦织绣博物馆", "district": "青羊区", "start_date": "2026-07-05", "end_date": "2026-08-30", "fee": "免费需预约", "description": "蜀锦织绣博物馆蜀绣体验，专业老师指导刺绣技法。", "highlights": ["蜀绣", "博物馆", "刺绣"], "type": "研学"},
    {"name": "蜀锦织绣博物馆织锦课堂", "venue": "蜀锦织绣博物馆", "district": "青羊区", "start_date": "2026-07-09", "end_date": "2026-08-28", "fee": "收费", "description": "织锦课堂，了解提花织机原理，体验织造过程。", "highlights": ["织锦", "提花", "织造"], "type": "研学"},
    {"name": "蜀锦织绣博物馆非遗研学", "venue": "蜀锦织绣博物馆", "district": "青羊区", "start_date": "2026-07-13", "end_date": "2026-08-26", "fee": "免费需预约", "description": "非遗研学，系统了解蜀锦历史与四大名锦文化。", "highlights": ["非遗", "蜀锦", "四大名锦"], "type": "研学"},
    {"name": "成都川剧院变脸表演夜场", "venue": "成都川剧院", "district": "锦江区", "start_date": "2026-07-04", "end_date": "2026-08-30", "fee": "需购票", "description": "川剧院变脸表演夜场，专业演员献演经典川剧折子戏。", "highlights": ["川剧", "变脸", "折子戏"], "type": "演出"},
    {"name": "成都川剧院亲子戏曲体验", "venue": "成都川剧院", "district": "锦江区", "start_date": "2026-07-08", "end_date": "2026-08-28", "fee": "收费", "description": "亲子戏曲体验，学唱川剧唱段，体验戏曲身段。", "highlights": ["戏曲", "唱段", "身段"], "type": "亲子活动"},
    {"name": "成都川剧院戏服体验日", "venue": "成都川剧院", "district": "锦江区", "start_date": "2026-07-12", "end_date": "2026-08-26", "fee": "收费", "description": "戏服体验日，试穿川剧戏服，了解服饰与角色。", "highlights": ["戏服", "角色", "体验"], "type": "亲子活动"},
    {"name": "成都川剧院脸谱绘画课堂", "venue": "成都川剧院", "district": "锦江区", "start_date": "2026-07-16", "end_date": "2026-08-30", "fee": "收费", "description": "脸谱绘画课堂，学习川剧脸谱色彩含义，手绘脸谱。", "highlights": ["脸谱", "绘画", "色彩"], "type": "亲子活动"},
    {"name": "非遗博览园皮影制作", "venue": "国际非遗博览园", "district": "青羊区", "start_date": "2026-07-06", "end_date": "2026-08-28", "fee": "收费", "description": "非遗博览园皮影制作，制作皮影并登台表演小剧场。", "highlights": ["皮影", "非遗", "剧场"], "type": "亲子活动"},
    {"name": "非遗博览园糖画体验", "venue": "国际非遗博览园", "district": "青羊区", "start_date": "2026-07-10", "end_date": "2026-08-30", "fee": "收费", "description": "非遗博览园糖画体验，跟随传承人学习糖画技艺。", "highlights": ["糖画", "传承人", "技艺"], "type": "亲子活动"},
    {"name": "非遗博览园剪纸课堂", "venue": "国际非遗博览园", "district": "青羊区", "start_date": "2026-07-14", "end_date": "2026-08-26", "fee": "收费", "description": "非遗博览园剪纸课堂，剪出各式传统花样作品。", "highlights": ["剪纸", "花样", "传统"], "type": "亲子活动"},
    {"name": "非遗博览园蜀绣研学", "venue": "国际非遗博览园", "district": "青羊区", "start_date": "2026-07-18", "end_date": "2026-09-08", "fee": "收费", "description": "非遗博览园蜀绣研学，深度了解蜀绣传承与针法。", "highlights": ["蜀绣", "针法", "传承"], "type": "研学"},
    {"name": "非遗博览园川剧脸谱体验", "venue": "国际非遗博览园", "district": "青羊区", "start_date": "2026-07-22", "end_date": "2026-08-29", "fee": "收费", "description": "川剧脸谱体验，亲手绘制脸谱面具，了解角色行当。", "highlights": ["脸谱", "行当", "面具"], "type": "亲子活动"},

    # ========== 6. 图书馆阅读活动（30个）==========
    {"name": "成都图书馆绘本故事会", "venue": "成都图书馆", "district": "青羊区", "start_date": "2026-07-05", "end_date": "2026-08-30", "fee": "免费", "description": "绘本故事会，老师生动讲述绘本，培养阅读兴趣。", "highlights": ["绘本", "故事", "阅读"], "type": "亲子活动"},
    {"name": "成都图书馆暑期阅读挑战", "venue": "成都图书馆", "district": "青羊区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "暑期阅读挑战，完成阅读打卡任务赢取奖品。", "highlights": ["阅读", "打卡", "挑战"], "type": "亲子活动"},
    {"name": "成都图书馆名家讲座系列", "venue": "成都图书馆", "district": "青羊区", "start_date": "2026-07-08", "end_date": "2026-08-28", "fee": "免费", "description": "名家讲座系列，知名作家与读者面对面分享阅读。", "highlights": ["名家", "讲座", "分享"], "type": "亲子活动"},
    {"name": "成都图书馆亲子手工阅读", "venue": "成都图书馆", "district": "青羊区", "start_date": "2026-07-12", "end_date": "2026-08-26", "fee": "免费", "description": "亲子手工阅读，结合绘本做手工，边读边玩。", "highlights": ["手工", "绘本", "阅读"], "type": "亲子活动"},
    {"name": "成都图书馆童书漂流活动", "venue": "成都图书馆", "district": "青羊区", "start_date": "2026-07-16", "end_date": "2026-08-30", "fee": "免费", "description": "童书漂流活动，交换闲置童书，让好书流动起来。", "highlights": ["童书", "漂流", "交换"], "type": "亲子活动"},
    {"name": "成都图书馆国学经典诵读", "venue": "成都图书馆", "district": "青羊区", "start_date": "2026-07-20", "end_date": "2026-08-29", "fee": "免费", "description": "国学经典诵读，诵读《弟子规》《论语》，传承国学。", "highlights": ["国学", "诵读", "经典"], "type": "亲子活动"},
    {"name": "成都图书馆科幻故事会", "venue": "成都图书馆", "district": "青羊区", "start_date": "2026-07-24", "end_date": "2026-08-28", "fee": "免费", "description": "科幻故事会，分享科幻名作，激发想象力。", "highlights": ["科幻", "故事", "想象"], "type": "亲子活动"},
    {"name": "成都图书馆英文绘本课堂", "venue": "成都图书馆", "district": "青羊区", "start_date": "2026-07-28", "end_date": "2026-09-12", "fee": "免费", "description": "英文绘本课堂，外教领读英文绘本，启蒙英语。", "highlights": ["英文", "绘本", "外教"], "type": "亲子活动"},
    {"name": "成都图书馆小读者分享会", "venue": "成都图书馆", "district": "青羊区", "start_date": "2026-07-30", "end_date": "2026-08-30", "fee": "免费", "description": "小读者分享会，孩子上台分享读书心得，锻炼表达。", "highlights": ["分享", "心得", "表达"], "type": "亲子活动"},
    {"name": "四川省图书馆绘本故事会", "venue": "四川省图书馆", "district": "青羊区", "start_date": "2026-07-04", "end_date": "2026-08-30", "fee": "免费", "description": "四川省图书馆绘本故事会，专业馆员讲述精选绘本。", "highlights": ["绘本", "馆员", "故事"], "type": "亲子活动"},
    {"name": "四川省图书馆暑期阅读营", "venue": "四川省图书馆", "district": "青羊区", "start_date": "2026-07-08", "end_date": "2026-08-28", "fee": "免费", "description": "暑期阅读营，多日主题阅读，深度沉浸书香世界。", "highlights": ["阅读营", "主题", "书香"], "type": "亲子活动"},
    {"name": "四川省图书馆名家大讲堂", "venue": "四川省图书馆", "district": "青羊区", "start_date": "2026-07-12", "end_date": "2026-08-26", "fee": "免费", "description": "名家大讲堂，文化学者开讲，拓宽孩子文化视野。", "highlights": ["名家", "讲堂", "文化"], "type": "亲子活动"},
    {"name": "四川省图书馆国学讲座", "venue": "四川省图书馆", "district": "青羊区", "start_date": "2026-07-16", "end_date": "2026-08-30", "fee": "免费", "description": "国学讲座，讲解传统经典，弘扬中华优秀传统文化。", "highlights": ["国学", "经典", "传统"], "type": "亲子活动"},
    {"name": "四川省图书馆亲子共读日", "venue": "四川省图书馆", "district": "青羊区", "start_date": "2026-07-20", "end_date": "2026-08-29", "fee": "免费", "description": "亲子共读日，全家共读一本书，分享阅读感悟。", "highlights": ["共读", "亲子", "感悟"], "type": "亲子活动"},
    {"name": "四川省图书馆巴蜀文化讲座", "venue": "四川省图书馆", "district": "青羊区", "start_date": "2026-07-24", "end_date": "2026-09-08", "fee": "免费", "description": "巴蜀文化讲座，讲述四川历史与文化，了解家乡。", "highlights": ["巴蜀", "文化", "家乡"], "type": "亲子活动"},
    {"name": "四川省图书馆儿童戏剧阅读", "venue": "四川省图书馆", "district": "青羊区", "start_date": "2026-07-28", "end_date": "2026-08-28", "fee": "免费", "description": "儿童戏剧阅读，把绘本演出来，戏剧化阅读体验。", "highlights": ["戏剧", "绘本", "演绎"], "type": "亲子活动"},
    {"name": "四川省图书馆诗词朗诵会", "venue": "四川省图书馆", "district": "青羊区", "start_date": "2026-07-30", "end_date": "2026-08-30", "fee": "免费", "description": "诗词朗诵会，朗诵唐诗宋词，感受古典诗词之美。", "highlights": ["诗词", "朗诵", "古典"], "type": "亲子活动"},
    {"name": "四川省图书馆科学绘本课堂", "venue": "四川省图书馆", "district": "青羊区", "start_date": "2026-08-02", "end_date": "2026-08-29", "fee": "免费", "description": "科学绘本课堂，通过绘本学科学，阅读与科普结合。", "highlights": ["科学", "绘本", "科普"], "type": "亲子活动"},
    {"name": "四川省图书馆小小图书管理员", "venue": "四川省图书馆", "district": "青羊区", "start_date": "2026-07-06", "end_date": "2026-08-26", "fee": "免费需预约", "description": "小小图书管理员，体验图书分类上架，了解图书馆。", "highlights": ["图书管理员", "分类", "体验"], "type": "研学"},
    {"name": "天府人文艺术图书馆绘本课堂", "venue": "天府人文艺术图书馆", "district": "金牛区", "start_date": "2026-07-05", "end_date": "2026-08-30", "fee": "免费", "description": "绘本课堂，在最美图书馆读绘本，感受艺术氛围。", "highlights": ["绘本", "艺术", "图书馆"], "type": "亲子活动"},
    {"name": "天府人文艺术图书馆阅读挑战", "venue": "天府人文艺术图书馆", "district": "金牛区", "start_date": "2026-07-09", "end_date": "2026-08-28", "fee": "免费", "description": "阅读挑战，设定阅读目标，完成挑战获证书。", "highlights": ["挑战", "目标", "证书"], "type": "亲子活动"},
    {"name": "天府人文艺术图书馆艺术讲座", "venue": "天府人文艺术图书馆", "district": "金牛区", "start_date": "2026-07-13", "end_date": "2026-08-26", "fee": "免费", "description": "艺术讲座，赏析中外名画，提升孩子艺术鉴赏力。", "highlights": ["艺术", "名画", "鉴赏"], "type": "亲子活动"},
    {"name": "天府人文艺术图书馆亲子手工", "venue": "天府人文艺术图书馆", "district": "金牛区", "start_date": "2026-07-17", "end_date": "2026-08-30", "fee": "免费", "description": "亲子手工，结合阅读主题做手工，动手又动脑。", "highlights": ["手工", "动手", "动脑"], "type": "亲子活动"},
    {"name": "天府人文艺术图书馆美术绘本课", "venue": "天府人文艺术图书馆", "district": "金牛区", "start_date": "2026-07-21", "end_date": "2026-08-29", "fee": "免费", "description": "美术绘本课，边读绘本边学绘画，培养审美。", "highlights": ["美术", "绘本", "审美"], "type": "亲子活动"},
    {"name": "天府人文艺术图书馆音乐故事会", "venue": "天府人文艺术图书馆", "district": "金牛区", "start_date": "2026-07-25", "end_date": "2026-08-28", "fee": "免费", "description": "音乐故事会，音乐伴奏讲述故事，视听双重享受。", "highlights": ["音乐", "故事", "视听"], "type": "亲子活动"},
    {"name": "天府人文艺术图书馆摄影讲座", "venue": "天府人文艺术图书馆", "district": "金牛区", "start_date": "2026-07-29", "end_date": "2026-09-10", "fee": "免费", "description": "摄影讲座，学习手机摄影技巧，记录生活美好。", "highlights": ["摄影", "手机", "记录"], "type": "亲子活动"},
    {"name": "天府人文艺术图书馆建筑美学课", "venue": "天府人文艺术图书馆", "district": "金牛区", "start_date": "2026-08-02", "end_date": "2026-08-29", "fee": "免费", "description": "建筑美学课，赏析建筑之美，培养空间审美。", "highlights": ["建筑", "美学", "审美"], "type": "亲子活动"},
    {"name": "天府人文艺术图书馆夏夜读书会", "venue": "天府人文艺术图书馆", "district": "金牛区", "start_date": "2026-08-05", "end_date": "2026-08-30", "fee": "免费", "description": "夏夜读书会，夜晚共读好书，享受静谧阅读时光。", "highlights": ["夏夜", "共读", "静谧"], "type": "亲子活动"},
    {"name": "成都图书馆亲子电影日", "venue": "成都图书馆", "district": "青羊区", "start_date": "2026-07-18", "end_date": "2026-08-29", "fee": "免费", "description": "亲子电影日，放映经典儿童电影，观影后分享讨论。", "highlights": ["电影", "观影", "讨论"], "type": "亲子活动"},
    {"name": "四川省图书馆作家见面会", "venue": "四川省图书馆", "district": "青羊区", "start_date": "2026-07-22", "end_date": "2026-08-28", "fee": "免费", "description": "作家见面会，与儿童文学作家面对面交流创作故事。", "highlights": ["作家", "见面", "创作"], "type": "亲子活动"},

    # ========== 7. 历史文化研学（30个）==========
    {"name": "武侯祠三国文化研学营", "venue": "成都武侯祠博物馆", "district": "武侯区", "start_date": "2026-07-05", "end_date": "2026-08-25", "fee": "收费", "description": "三国文化研学营，多日深度研学，走访武侯祠寻访蜀汉遗迹。", "highlights": ["三国", "研学营", "蜀汉"], "type": "研学"},
    {"name": "武侯祠诸葛亮智慧课堂", "venue": "成都武侯祠博物馆", "district": "武侯区", "start_date": "2026-07-09", "end_date": "2026-08-28", "fee": "收费", "description": "诸葛亮智慧课堂，讲述丞相治蜀故事，启迪思辨。", "highlights": ["诸葛亮", "智慧", "治蜀"], "type": "研学"},
    {"name": "武侯祠蜀汉历史探秘", "venue": "成都武侯祠博物馆", "district": "武侯区", "start_date": "2026-07-13", "end_date": "2026-08-26", "fee": "需购票", "description": "蜀汉历史探秘，参观文物陈列，了解蜀汉兴衰。", "highlights": ["蜀汉", "历史", "文物"], "type": "研学"},
    {"name": "武侯祠三国兵器展研学", "venue": "成都武侯祠博物馆", "district": "武侯区", "start_date": "2026-07-17", "end_date": "2026-08-30", "fee": "需购票", "description": "三国兵器展研学，了解古代兵器与冷兵器战争。", "highlights": ["兵器", "冷兵器", "战争"], "type": "研学"},
    {"name": "武侯祠刘备惠陵探秘", "venue": "成都武侯祠博物馆", "district": "武侯区", "start_date": "2026-07-21", "end_date": "2026-08-29", "fee": "需购票", "description": "刘备惠陵探秘，参观刘备墓，了解陵寝制度与历史。", "highlights": ["惠陵", "刘备", "陵寝"], "type": "研学"},
    {"name": "武侯祠三国演义故事会", "venue": "成都武侯祠博物馆", "district": "武侯区", "start_date": "2026-07-25", "end_date": "2026-08-28", "fee": "需购票", "description": "三国演义故事会，讲述经典桥段，辨析史实与演义。", "highlights": ["三国演义", "故事", "史实"], "type": "亲子活动"},
    {"name": "杜甫草堂诗词研学营", "venue": "成都杜甫草堂博物馆", "district": "青羊区", "start_date": "2026-07-06", "end_date": "2026-08-26", "fee": "收费", "description": "诗词研学营，多日深度研学，诵读杜甫名篇感受诗史。", "highlights": ["诗词", "杜甫", "诗史"], "type": "研学"},
    {"name": "杜甫草堂唐诗朗诵会", "venue": "成都杜甫草堂博物馆", "district": "青羊区", "start_date": "2026-07-10", "end_date": "2026-08-28", "fee": "需购票", "description": "唐诗朗诵会，在草堂朗诵杜甫诗作，感受诗韵。", "highlights": ["唐诗", "朗诵", "诗韵"], "type": "亲子活动"},
    {"name": "杜甫草堂书法体验课", "venue": "成都杜甫草堂博物馆", "district": "青羊区", "start_date": "2026-07-14", "end_date": "2026-08-30", "fee": "收费", "description": "书法体验课，临写杜甫诗句，传承书法与诗学。", "highlights": ["书法", "临写", "诗学"], "type": "研学"},
    {"name": "杜甫草堂诗圣文化探秘", "venue": "成都杜甫草堂博物馆", "district": "青羊区", "start_date": "2026-07-18", "end_date": "2026-08-29", "fee": "需购票", "description": "诗圣文化探秘，了解杜甫生平与成都草堂岁月。", "highlights": ["诗圣", "生平", "草堂"], "type": "研学"},
    {"name": "杜甫草堂唐代生活体验", "venue": "成都杜甫草堂博物馆", "district": "青羊区", "start_date": "2026-07-22", "end_date": "2026-08-28", "fee": "收费", "description": "唐代生活体验，模拟唐人日常，了解唐代文化风俗。", "highlights": ["唐代", "生活", "风俗"], "type": "研学"},
    {"name": "杜甫草堂古琴雅集", "venue": "成都杜甫草堂博物馆", "district": "青羊区", "start_date": "2026-07-26", "end_date": "2026-09-08", "fee": "收费", "description": "古琴雅集，草堂听琴品茗，感受文人雅趣。", "highlights": ["古琴", "雅集", "品茗"], "type": "亲子活动"},
    {"name": "金沙遗址古蜀文明研学", "venue": "成都金沙遗址博物馆", "district": "青羊区", "start_date": "2026-07-05", "end_date": "2026-08-28", "fee": "需购票", "description": "古蜀文明研学，系统了解金沙遗址与古蜀文明脉络。", "highlights": ["古蜀", "金沙", "文明"], "type": "研学"},
    {"name": "金沙遗址太阳崇拜探秘", "venue": "成都金沙遗址博物馆", "district": "青羊区", "start_date": "2026-07-09", "end_date": "2026-08-30", "fee": "需购票", "description": "太阳崇拜探秘，了解古蜀太阳神鸟与太阳崇拜文化。", "highlights": ["太阳崇拜", "神鸟", "文化"], "type": "研学"},
    {"name": "金沙遗址古蜀王陵探秘", "venue": "成都金沙遗址博物馆", "district": "青羊区", "start_date": "2026-07-13", "end_date": "2026-08-26", "fee": "需购票", "description": "古蜀王陵探秘，了解古蜀王陵与祭祀坑的发现历程。", "highlights": ["王陵", "祭祀坑", "发现"], "type": "研学"},
    {"name": "金沙遗址玉器文化课堂", "venue": "成都金沙遗址博物馆", "district": "青羊区", "start_date": "2026-07-17", "end_date": "2026-08-29", "fee": "收费", "description": "玉器文化课堂，研究玉琮玉璋，理解古蜀玉礼文化。", "highlights": ["玉器", "玉琮", "礼制"], "type": "研学"},
    {"name": "金沙遗址青铜面具研学", "venue": "成都金沙遗址博物馆", "district": "青羊区", "start_date": "2026-07-21", "end_date": "2026-09-05", "fee": "需购票", "description": "青铜面具研学，了解面具造型与古蜀宗教信仰。", "highlights": ["青铜面具", "宗教", "信仰"], "type": "研学"},
    {"name": "成都博物馆蜀文化探秘", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-06", "end_date": "2026-08-28", "fee": "免费需预约", "description": "蜀文化探秘，参观古蜀文明展，了解成都城市发展史。", "highlights": ["蜀文化", "城市史", "展览"], "type": "研学"},
    {"name": "成都博物馆古蜀文明展", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-01", "end_date": "2026-10-31", "fee": "免费需预约", "description": "古蜀文明展，系统展示古蜀文明从宝墩到金沙的演进。", "highlights": ["古蜀", "展览", "演进"], "type": "展览"},
    {"name": "成都博物馆巴蜀文化研学", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-10", "end_date": "2026-08-30", "fee": "免费需预约", "description": "巴蜀文化研学，了解巴蜀文化特色与历史名人。", "highlights": ["巴蜀", "文化", "名人"], "type": "研学"},
    {"name": "成都博物馆宋代茶文化体验", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-14", "end_date": "2026-08-26", "fee": "收费", "description": "宋代茶文化体验，学习点茶技艺，了解宋代茶事。", "highlights": ["宋代", "点茶", "茶事"], "type": "研学"},
    {"name": "成都博物馆古钱币探秘", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-18", "end_date": "2026-09-10", "fee": "免费需预约", "description": "古钱币探秘，了解历代钱币形制与经济文化。", "highlights": ["钱币", "形制", "经济"], "type": "研学"},
    {"name": "武侯祠锦里三国文化游", "venue": "成都武侯祠博物馆", "district": "武侯区", "start_date": "2026-07-22", "end_date": "2026-08-29", "fee": "需购票", "description": "三国文化游，串联武侯祠与锦里，沉浸式三国体验。", "highlights": ["三国", "锦里", "沉浸"], "type": "亲子活动"},
    {"name": "杜甫草堂浣花溪诗画游", "venue": "成都杜甫草堂博物馆", "district": "青羊区", "start_date": "2026-07-26", "end_date": "2026-08-30", "fee": "需购票", "description": "浣花溪诗画游，草堂与浣花溪串联，诗画一体研学。", "highlights": ["浣花溪", "诗画", "研学"], "type": "亲子活动"},
    {"name": "金沙遗址亲子考古日", "venue": "成都金沙遗址博物馆", "district": "青羊区", "start_date": "2026-07-30", "end_date": "2026-08-28", "fee": "收费", "description": "亲子考古日，模拟发掘金沙文物，体验考古乐趣。", "highlights": ["考古", "发掘", "亲子"], "type": "亲子活动"},
    {"name": "武侯祠三国名将故事会", "venue": "成都武侯祠博物馆", "district": "武侯区", "start_date": "2026-08-02", "end_date": "2026-08-29", "fee": "需购票", "description": "三国名将故事会，讲述五虎上将故事，激发历史兴趣。", "highlights": ["名将", "五虎将", "故事"], "type": "亲子活动"},
    {"name": "杜甫草堂诗圣故里研学", "venue": "成都杜甫草堂博物馆", "district": "青羊区", "start_date": "2026-08-05", "end_date": "2026-08-30", "fee": "收费", "description": "诗圣故里研学，深度了解杜甫成都诗作与草堂生活。", "highlights": ["诗圣", "故里", "诗作"], "type": "研学"},
    {"name": "金沙遗址古蜀祭祀探秘", "venue": "成都金沙遗址博物馆", "district": "青羊区", "start_date": "2026-08-08", "end_date": "2026-09-10", "fee": "需购票", "description": "古蜀祭祀探秘，了解祭祀坑与古蜀宗教祭祀文化。", "highlights": ["祭祀", "宗教", "祭祀坑"], "type": "研学"},
    {"name": "成都博物馆清代瓷器展", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-01", "end_date": "2026-11-30", "fee": "免费需预约", "description": "清代瓷器展，展出精美清代官窑瓷器，鉴赏瓷艺。", "highlights": ["清代", "瓷器", "官窑"], "type": "展览"},
    {"name": "成都博物馆民俗文化展", "venue": "成都博物馆", "district": "青羊区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费需预约", "description": "民俗文化展，展示成都老民俗与市井生活，留住乡愁。", "highlights": ["民俗", "市井", "乡愁"], "type": "展览"},

    # ========== 8. 体育运动活动（30个）==========
    {"name": "青龙湖皮划艇培训营", "venue": "青龙湖湿地公园", "district": "龙泉驿区", "start_date": "2026-07-06", "end_date": "2026-08-26", "fee": "收费", "description": "皮划艇培训营，系统学习划艇技术，培养水上运动技能。", "highlights": ["皮划艇", "培训", "水上"], "type": "亲子活动"},
    {"name": "兴隆湖帆船体验", "venue": "兴隆湖湿地公园", "district": "天府新区", "start_date": "2026-07-10", "end_date": "2026-08-30", "fee": "收费", "description": "帆船体验，专业教练指导，感受帆船运动魅力。", "highlights": ["帆船", "教练", "运动"], "type": "亲子活动"},
    {"name": "锦江绿道亲子骑行", "venue": "锦江绿道", "district": "锦江区", "start_date": "2026-07-04", "end_date": "2026-08-30", "fee": "免费", "description": "锦江绿道亲子骑行，沿锦江绿道骑行，享受沿途风景。", "highlights": ["骑行", "绿道", "锦江"], "type": "亲子活动"},
    {"name": "天府绿道骑行挑战", "venue": "天府绿道", "district": "高新区", "start_date": "2026-07-08", "end_date": "2026-08-28", "fee": "免费", "description": "天府绿道骑行挑战，长距离绿道骑行，锻炼体能。", "highlights": ["骑行", "绿道", "体能"], "type": "亲子活动"},
    {"name": "成都足球夏令营", "venue": "成都足球训练基地", "district": "武侯区", "start_date": "2026-07-06", "end_date": "2026-08-25", "fee": "收费", "description": "足球夏令营，专业教练带队，提升足球技能与团队意识。", "highlights": ["足球", "夏令营", "团队"], "type": "亲子活动"},
    {"name": "成都篮球夏令营", "venue": "成都体育馆", "district": "青羊区", "start_date": "2026-07-10", "end_date": "2026-08-28", "fee": "收费", "description": "篮球夏令营，系统训练篮球基本功，提升球技。", "highlights": ["篮球", "训练", "球技"], "type": "亲子活动"},
    {"name": "成都游泳培训班", "venue": "成都市游泳馆", "district": "青羊区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "游泳培训班，分龄教学，让孩子掌握游泳技能。", "highlights": ["游泳", "培训", "技能"], "type": "亲子活动"},
    {"name": "成都羽毛球夏令营", "venue": "成都体育学院", "district": "武侯区", "start_date": "2026-07-14", "end_date": "2026-08-26", "fee": "收费", "description": "羽毛球夏令营，专业教练指导，提升羽毛球水平。", "highlights": ["羽毛球", "教练", "提升"], "type": "亲子活动"},
    {"name": "成都网球培训营", "venue": "四川省体育馆", "district": "武侯区", "start_date": "2026-07-18", "end_date": "2026-08-30", "fee": "收费", "description": "网球培训营，学习网球基本功，体验网球运动。", "highlights": ["网球", "培训", "运动"], "type": "亲子活动"},
    {"name": "成都攀岩体验日", "venue": "成都攀岩馆", "district": "武侯区", "start_date": "2026-07-06", "end_date": "2026-08-29", "fee": "收费", "description": "攀岩体验日，专业保护下挑战攀岩墙，锻炼勇气。", "highlights": ["攀岩", "勇气", "挑战"], "type": "亲子活动"},
    {"name": "成都轮滑培训营", "venue": "成都轮滑场", "district": "金牛区", "start_date": "2026-07-10", "end_date": "2026-08-28", "fee": "收费", "description": "轮滑培训营，学习轮滑基础动作，安全畅滑。", "highlights": ["轮滑", "培训", "安全"], "type": "亲子活动"},
    {"name": "成都击剑体验日", "venue": "成都击剑馆", "district": "武侯区", "start_date": "2026-07-14", "end_date": "2026-08-30", "fee": "收费", "description": "击剑体验日，学习击剑礼仪与基本剑法，绅士运动。", "highlights": ["击剑", "礼仪", "剑法"], "type": "亲子活动"},
    {"name": "成都跆拳道夏令营", "venue": "成都跆拳道馆", "district": "武侯区", "start_date": "2026-07-18", "end_date": "2026-08-26", "fee": "收费", "description": "跆拳道夏令营，学习跆拳道品势与腿法，强身健体。", "highlights": ["跆拳道", "品势", "健体"], "type": "亲子活动"},
    {"name": "成都武术体验营", "venue": "成都武术馆", "district": "青羊区", "start_date": "2026-07-22", "end_date": "2026-08-29", "fee": "收费", "description": "武术体验营，学习传统武术基本功，传承国术。", "highlights": ["武术", "国术", "基本功"], "type": "亲子活动"},
    {"name": "成都瑜伽亲子课", "venue": "成都瑜伽馆", "district": "锦江区", "start_date": "2026-07-26", "end_date": "2026-08-30", "fee": "收费", "description": "瑜伽亲子课，亲子共练瑜伽，增进感情放松身心。", "highlights": ["瑜伽", "亲子", "放松"], "type": "亲子活动"},
    {"name": "兴隆湖水上桨板", "venue": "兴隆湖湿地公园", "district": "天府新区", "start_date": "2026-07-05", "end_date": "2026-08-30", "fee": "收费", "description": "水上桨板体验，在桨板上划行，锻炼平衡与核心。", "highlights": ["桨板", "平衡", "核心"], "type": "亲子活动"},
    {"name": "青龙湖亲子垂钓", "venue": "青龙湖湿地公园", "district": "龙泉驿区", "start_date": "2026-07-09", "end_date": "2026-08-28", "fee": "收费", "description": "亲子垂钓，在青龙湖畔钓鱼，享受悠闲亲子时光。", "highlights": ["垂钓", "悠闲", "亲子"], "type": "亲子活动"},
    {"name": "白鹭湾湿地亲子骑行", "venue": "白鹭湾湿地公园", "district": "锦江区", "start_date": "2026-07-13", "end_date": "2026-08-30", "fee": "免费", "description": "亲子骑行，湿地绿道骑行，观景运动两不误。", "highlights": ["骑行", "湿地", "观景"], "type": "亲子活动"},
    {"name": "锦城湖皮划艇体验", "venue": "锦城湖公园", "district": "高新区", "start_date": "2026-07-17", "end_date": "2026-08-29", "fee": "收费", "description": "锦城湖皮划艇体验，城市湖泊划艇，亲近水面。", "highlights": ["皮划艇", "湖泊", "亲水"], "type": "亲子活动"},
    {"name": "锦城湖亲子帆船", "venue": "锦城湖公园", "district": "高新区", "start_date": "2026-07-21", "end_date": "2026-08-30", "fee": "收费", "description": "亲子帆船，在锦城湖学帆船，城市中体验航海乐趣。", "highlights": ["帆船", "航海", "城市"], "type": "亲子活动"},
    {"name": "天府绿道亲子马拉松", "venue": "天府绿道", "district": "高新区", "start_date": "2026-07-25", "end_date": "2026-08-28", "fee": "免费", "description": "亲子马拉松，绿道欢乐跑，全家齐参与锻炼毅力。", "highlights": ["马拉松", "欢乐跑", "毅力"], "type": "亲子活动"},
    {"name": "成都高尔夫体验日", "venue": "成都高尔夫球场", "district": "双流区", "start_date": "2026-07-29", "end_date": "2026-09-10", "fee": "收费", "description": "高尔夫体验日，学习挥杆基本动作，体验优雅运动。", "highlights": ["高尔夫", "挥杆", "优雅"], "type": "亲子活动"},
    {"name": "成都滑冰体验", "venue": "成都冰场", "district": "锦江区", "start_date": "2026-07-05", "end_date": "2026-08-30", "fee": "收费", "description": "滑冰体验，室内真冰场滑冰，炎夏感受冰上乐趣。", "highlights": ["滑冰", "冰场", "冰上"], "type": "亲子活动"},
    {"name": "成都平衡车培训", "venue": "成都平衡车场", "district": "武侯区", "start_date": "2026-07-09", "end_date": "2026-08-28", "fee": "收费", "description": "平衡车培训，幼儿平衡车教学，锻炼平衡与协调。", "highlights": ["平衡车", "幼儿", "协调"], "type": "亲子活动"},
    {"name": "成都射箭体验日", "venue": "成都射箭馆", "district": "武侯区", "start_date": "2026-07-13", "end_date": "2026-08-30", "fee": "收费", "description": "射箭体验日，学习射箭基本姿势，专注力训练。", "highlights": ["射箭", "专注", "姿势"], "type": "亲子活动"},
    {"name": "成都蹦床公园", "venue": "成都蹦床馆", "district": "武侯区", "start_date": "2026-07-17", "end_date": "2026-08-29", "fee": "收费", "description": "蹦床公园，自由蹦跳与花式动作，释放活力。", "highlights": ["蹦床", "蹦跳", "活力"], "type": "亲子活动"},
    {"name": "成都跑酷训练营", "venue": "成都跑酷场", "district": "成华区", "start_date": "2026-07-21", "end_date": "2026-08-28", "fee": "收费", "description": "跑酷训练营，学习跑酷基础翻越动作，挑战障碍。", "highlights": ["跑酷", "翻越", "障碍"], "type": "亲子活动"},
    {"name": "成都亲子游泳日", "venue": "成都亲子游泳馆", "district": "高新区", "start_date": "2026-07-25", "end_date": "2026-08-30", "fee": "收费", "description": "亲子游泳日，亲子共游，水中游戏增进感情。", "highlights": ["游泳", "亲子", "水中"], "type": "亲子活动"},
    {"name": "成都滑板体验营", "venue": "成都滑板场", "district": "成华区", "start_date": "2026-07-29", "end_date": "2026-09-08", "fee": "收费", "description": "滑板体验营，学习滑板基础动作，街头潮流运动。", "highlights": ["滑板", "潮流", "街头"], "type": "亲子活动"},
    {"name": "成都马术体验日", "venue": "成都马术俱乐部", "district": "双流区", "start_date": "2026-08-02", "end_date": "2026-08-30", "fee": "收费", "description": "马术体验日，学习马术基础骑行，与马匹亲密接触。", "highlights": ["马术", "骑行", "马匹"], "type": "亲子活动"},

    # ========== 9. 古镇民俗活动（30个）==========
    {"name": "黄龙溪古镇玩水节", "venue": "黄龙溪古镇", "district": "双流区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "黄龙溪玩水节，古镇溪流打水仗，全家清凉一夏。", "highlights": ["玩水", "打水仗", "清凉"], "type": "亲子活动"},
    {"name": "黄龙溪古镇水龙节", "venue": "黄龙溪古镇", "district": "双流区", "start_date": "2026-07-05", "end_date": "2026-08-30", "fee": "免费", "description": "水龙节，舞水龙巡游泼水，感受古镇民俗狂欢。", "highlights": ["水龙节", "泼水", "民俗"], "type": "亲子活动"},
    {"name": "黄龙溪古镇火龙表演", "venue": "黄龙溪古镇", "district": "双流区", "start_date": "2026-07-10", "end_date": "2026-08-28", "fee": "免费", "description": "火龙表演，非遗火龙钢花，夜空璀璨震撼人心。", "highlights": ["火龙", "钢花", "非遗"], "type": "演出"},
    {"name": "黄龙溪古镇民俗体验", "venue": "黄龙溪古镇", "district": "双流区", "start_date": "2026-07-14", "end_date": "2026-08-30", "fee": "免费", "description": "民俗体验，古镇逛老街看民俗表演，体验川西风情。", "highlights": ["民俗", "老街", "川西"], "type": "亲子活动"},
    {"name": "黄龙溪古镇亲子漂流", "venue": "黄龙溪古镇", "district": "双流区", "start_date": "2026-07-18", "end_date": "2026-08-29", "fee": "收费", "description": "亲子漂流，古镇溪流漂流戏水，清凉又刺激。", "highlights": ["漂流", "戏水", "刺激"], "type": "亲子活动"},
    {"name": "黄龙溪古镇古街寻宝", "venue": "黄龙溪古镇", "district": "双流区", "start_date": "2026-07-22", "end_date": "2026-08-28", "fee": "免费", "description": "古街寻宝，按线索在古镇寻宝，了解古镇历史。", "highlights": ["寻宝", "线索", "历史"], "type": "亲子活动"},
    {"name": "洛带古镇水龙节", "venue": "洛带古镇", "district": "龙泉驿区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "洛带水龙节，客家水龙巡游泼水，盛大民俗狂欢。", "highlights": ["水龙节", "客家", "泼水"], "type": "亲子活动"},
    {"name": "洛带古镇客家文化研学", "venue": "洛带古镇", "district": "龙泉驿区", "start_date": "2026-07-06", "end_date": "2026-08-28", "fee": "免费", "description": "客家文化研学，了解客家迁徙史与洛带客家风情。", "highlights": ["客家", "迁徙", "研学"], "type": "研学"},
    {"name": "洛带古镇火龙节", "venue": "洛带古镇", "district": "龙泉驿区", "start_date": "2026-07-10", "end_date": "2026-08-30", "fee": "免费", "description": "火龙节，刘家龙舞火龙，客家非遗震撼上演。", "highlights": ["火龙节", "刘家龙", "非遗"], "type": "演出"},
    {"name": "洛带古镇客家美食体验", "venue": "洛带古镇", "district": "龙泉驿区", "start_date": "2026-07-14", "end_date": "2026-08-29", "fee": "收费", "description": "客家美食体验，品尝伤心凉粉等客家美食，学做艾蒿馍馍。", "highlights": ["美食", "凉粉", "客家"], "type": "亲子活动"},
    {"name": "洛带古镇会馆探秘", "venue": "洛带古镇", "district": "龙泉驿区", "start_date": "2026-07-18", "end_date": "2026-08-28", "fee": "免费", "description": "会馆探秘，参观四大会馆，了解客家会馆建筑与文化。", "highlights": ["会馆", "建筑", "客家"], "type": "研学"},
    {"name": "洛带古镇古街亲子游", "venue": "洛带古镇", "district": "龙泉驿区", "start_date": "2026-07-22", "end_date": "2026-08-30", "fee": "免费", "description": "古街亲子游，逛古镇老街看古建，亲子休闲一日游。", "highlights": ["古街", "老街", "休闲"], "type": "亲子活动"},
    {"name": "安仁古镇民国风情游", "venue": "安仁古镇", "district": "大邑县", "start_date": "2026-07-04", "end_date": "2026-08-30", "fee": "免费", "description": "民国风情游，安仁古镇公馆老街，感受民国风韵。", "highlights": ["民国", "公馆", "老街"], "type": "亲子活动"},
    {"name": "安仁古镇博物馆研学", "venue": "安仁古镇", "district": "大邑县", "start_date": "2026-07-08", "end_date": "2026-08-28", "fee": "收费", "description": "博物馆研学，安仁博物馆聚落，多馆联游深度研学。", "highlights": ["博物馆", "聚落", "研学"], "type": "研学"},
    {"name": "安仁古镇建川博物馆探秘", "venue": "安仁古镇", "district": "大邑县", "start_date": "2026-07-12", "end_date": "2026-08-30", "fee": "需购票", "description": "建川博物馆探秘，参观抗战系列展，铭记历史。", "highlights": ["建川", "抗战", "历史"], "type": "研学"},
    {"name": "安仁古镇老街电车体验", "venue": "安仁古镇", "district": "大邑县", "start_date": "2026-07-16", "end_date": "2026-08-29", "fee": "收费", "description": "老街电车体验，乘坐有轨电车游古镇，复古情怀。", "highlights": ["电车", "有轨", "复古"], "type": "亲子活动"},
    {"name": "安仁古镇民国服饰体验", "venue": "安仁古镇", "district": "大邑县", "start_date": "2026-07-20", "end_date": "2026-08-28", "fee": "收费", "description": "民国服饰体验，换上旗袍长衫，公馆前拍复古照。", "highlights": ["旗袍", "长衫", "复古"], "type": "亲子活动"},
    {"name": "安仁古镇公馆探秘", "venue": "安仁古镇", "district": "大邑县", "start_date": "2026-07-24", "end_date": "2026-09-08", "fee": "收费", "description": "公馆探秘，参观刘氏公馆群，了解民国公馆建筑。", "highlights": ["公馆", "建筑", "民国"], "type": "研学"},
    {"name": "平乐古镇漂流玩水", "venue": "平乐古镇", "district": "邛崃市", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "平乐漂流，白沫江竹筏漂流，古镇玩水纳凉。", "highlights": ["漂流", "竹筏", "白沫江"], "type": "亲子活动"},
    {"name": "平乐古镇竹海探秘", "venue": "平乐古镇", "district": "邛崃市", "start_date": "2026-07-06", "end_date": "2026-08-28", "fee": "免费", "description": "竹海探秘，游览芦沟竹海，感受川西竹乡清幽。", "highlights": ["竹海", "芦沟", "竹乡"], "type": "亲子活动"},
    {"name": "平乐古镇古桥寻访", "venue": "平乐古镇", "district": "邛崃市", "start_date": "2026-07-10", "end_date": "2026-08-30", "fee": "免费", "description": "古桥寻访，走访乐善桥等古桥，了解古桥建筑。", "highlights": ["古桥", "乐善桥", "建筑"], "type": "亲子活动"},
    {"name": "平乐古镇茶马古道研学", "venue": "平乐古镇", "district": "邛崃市", "start_date": "2026-07-14", "end_date": "2026-08-29", "fee": "免费", "description": "茶马古道研学，了解平乐茶马古道历史与马帮文化。", "highlights": ["茶马古道", "马帮", "历史"], "type": "研学"},
    {"name": "平乐古镇民俗体验", "venue": "平乐古镇", "district": "邛崃市", "start_date": "2026-07-18", "end_date": "2026-08-28", "fee": "免费", "description": "民俗体验，古镇看民俗表演，体验竹编手作。", "highlights": ["民俗", "竹编", "手作"], "type": "亲子活动"},
    {"name": "平乐古镇夜游古街", "venue": "平乐古镇", "district": "邛崃市", "start_date": "2026-07-22", "end_date": "2026-08-30", "fee": "免费", "description": "夜游古街，夜晚古镇灯火阑珊，漫步江边纳凉。", "highlights": ["夜游", "灯火", "纳凉"], "type": "亲子活动"},
    {"name": "街子古镇古街亲子游", "venue": "街子古镇", "district": "崇州市", "start_date": "2026-07-05", "end_date": "2026-08-30", "fee": "免费", "description": "古街亲子游，逛街子古街看字库塔，感受川西水乡。", "highlights": ["古街", "字库塔", "水乡"], "type": "亲子活动"},
    {"name": "街子古镇凤栖山探秘", "venue": "街子古镇", "district": "崇州市", "start_date": "2026-07-09", "end_date": "2026-08-28", "fee": "免费", "description": "凤栖山探秘，登凤栖山访古寺，感受山林清幽。", "highlights": ["凤栖山", "古寺", "山林"], "type": "亲子活动"},
    {"name": "街子古镇字库塔研学", "venue": "街子古镇", "district": "崇州市", "start_date": "2026-07-13", "end_date": "2026-08-30", "fee": "免费", "description": "字库塔研学，了解字库塔与古人敬惜字纸的文化。", "highlights": ["字库塔", "敬字", "文化"], "type": "研学"},
    {"name": "街子古镇光严禅院探秘", "venue": "街子古镇", "district": "崇州市", "start_date": "2026-07-17", "end_date": "2026-09-05", "fee": "免费", "description": "光严禅院探秘，访无漏秋山古寺，了解禅宗文化。", "highlights": ["禅院", "禅宗", "古寺"], "type": "研学"},
    {"name": "街子古镇康道寻幽", "venue": "街子古镇", "district": "崇州市", "start_date": "2026-07-21", "end_date": "2026-08-29", "fee": "免费", "description": "康道寻幽，徒步古镇康道，避暑纳凉亲子徒步。", "highlights": ["康道", "徒步", "纳凉"], "type": "亲子活动"},
    {"name": "街子古镇茶艺体验", "venue": "街子古镇", "district": "崇州市", "start_date": "2026-07-25", "end_date": "2026-08-30", "fee": "收费", "description": "茶艺体验，在古镇茶馆学泡茶，感受川西茶文化。", "highlights": ["茶艺", "茶馆", "川西"], "type": "亲子活动"},

    # ========== 10. 商业综合体亲子活动（30个）==========
    {"name": "成都IFS熊猫打卡活动", "venue": "成都IFS国际金融中心", "district": "锦江区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "IFS熊猫打卡，与巨型爬墙熊猫合影，成都地标打卡。", "highlights": ["熊猫", "打卡", "地标"], "type": "亲子活动"},
    {"name": "成都IFS亲子艺术展", "venue": "成都IFS国际金融中心", "district": "锦江区", "start_date": "2026-07-05", "end_date": "2026-08-30", "fee": "部分免费", "description": "亲子艺术展，IFS商场当代艺术展，提升孩子审美。", "highlights": ["艺术展", "当代", "审美"], "type": "展览"},
    {"name": "成都IFS暑期手作课堂", "venue": "成都IFS国际金融中心", "district": "锦江区", "start_date": "2026-07-09", "end_date": "2026-08-28", "fee": "收费", "description": "暑期手作课堂，商场内手作体验，亲子DIY乐趣。", "highlights": ["手作", "DIY", "亲子"], "type": "亲子活动"},
    {"name": "成都IFS儿童时装秀", "venue": "成都IFS国际金融中心", "district": "锦江区", "start_date": "2026-07-13", "end_date": "2026-08-26", "fee": "免费", "description": "儿童时装秀，小模特T台走秀，时尚亲子体验。", "highlights": ["时装秀", "T台", "时尚"], "type": "演出"},
    {"name": "成都IFS屋顶花园派对", "venue": "成都IFS国际金融中心", "district": "锦江区", "start_date": "2026-07-17", "end_date": "2026-08-29", "fee": "免费", "description": "屋顶花园派对，七楼雕塑庭院亲子活动，城市观景。", "highlights": ["屋顶", "花园", "观景"], "type": "亲子活动"},
    {"name": "成都太古里手作市集", "venue": "成都远洋太古里", "district": "锦江区", "start_date": "2026-07-04", "end_date": "2026-08-30", "fee": "免费", "description": "手作市集，太古里开放式街区逛手作市集，亲子淘宝。", "highlights": ["市集", "手作", "街区"], "type": "亲子活动"},
    {"name": "成都太古里亲子艺术展", "venue": "成都远洋太古里", "district": "锦江区", "start_date": "2026-07-08", "end_date": "2026-08-28", "fee": "部分免费", "description": "亲子艺术展，太古里公共艺术装置展，打卡拍照。", "highlights": ["艺术", "装置", "拍照"], "type": "展览"},
    {"name": "成都太古里亲子绘画日", "venue": "成都远洋太古里", "district": "锦江区", "start_date": "2026-07-12", "end_date": "2026-08-30", "fee": "收费", "description": "亲子绘画日，在太古里户外写生，城市中感受艺术。", "highlights": ["绘画", "写生", "城市"], "type": "亲子活动"},
    {"name": "成都太古里夏日艺术节", "venue": "成都远洋太古里", "district": "锦江区", "start_date": "2026-07-16", "end_date": "2026-08-29", "fee": "免费", "description": "夏日艺术节，太古里艺术活动周，展览演出齐聚。", "highlights": ["艺术节", "展览", "演出"], "type": "亲子活动"},
    {"name": "成都太古里亲子DIY工坊", "venue": "成都远洋太古里", "district": "锦江区", "start_date": "2026-07-20", "end_date": "2026-08-28", "fee": "收费", "description": "亲子DIY工坊，太古里品牌手作活动，动手创作。", "highlights": ["DIY", "工坊", "创作"], "type": "亲子活动"},
    {"name": "环球中心亲子购物节", "venue": "成都环球中心", "district": "高新区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "免费", "description": "亲子购物节，环球中心暑期促销与亲子活动结合。", "highlights": ["购物节", "促销", "亲子"], "type": "亲子活动"},
    {"name": "环球中心儿童乐园派对", "venue": "成都环球中心", "district": "高新区", "start_date": "2026-07-05", "end_date": "2026-08-30", "fee": "收费", "description": "儿童乐园派对，环球中心室内乐园，派对游戏嗨翻天。", "highlights": ["乐园", "派对", "室内"], "type": "亲子活动"},
    {"name": "环球中心亲子美食节", "venue": "成都环球中心", "district": "高新区", "start_date": "2026-07-09", "end_date": "2026-08-28", "fee": "免费", "description": "亲子美食节，环球中心美食汇，亲子品尝全球美食。", "highlights": ["美食", "全球", "亲子"], "type": "亲子活动"},
    {"name": "环球中心室内冲浪体验", "venue": "成都环球中心", "district": "高新区", "start_date": "2026-07-13", "end_date": "2026-08-30", "fee": "收费", "description": "室内冲浪体验，环球中心冲浪馆，城市里体验冲浪。", "highlights": ["冲浪", "室内", "城市"], "type": "亲子活动"},
    {"name": "环球中心亲子冰场", "venue": "成都环球中心", "district": "高新区", "start_date": "2026-07-17", "end_date": "2026-08-29", "fee": "收费", "description": "亲子冰场，环球中心真冰场，全家滑冰欢乐时光。", "highlights": ["冰场", "滑冰", "欢乐"], "type": "亲子活动"},
    {"name": "万象城亲子嘉年华", "venue": "成都万象城", "district": "成华区", "start_date": "2026-07-04", "end_date": "2026-08-30", "fee": "免费", "description": "亲子嘉年华，万象城暑期亲子嘉年华，游戏互动集市。", "highlights": ["嘉年华", "游戏", "集市"], "type": "亲子活动"},
    {"name": "万象城儿童艺术展", "venue": "成都万象城", "district": "成华区", "start_date": "2026-07-08", "end_date": "2026-08-28", "fee": "部分免费", "description": "儿童艺术展，万象城展出儿童画作，激发艺术兴趣。", "highlights": ["艺术展", "儿童画", "兴趣"], "type": "展览"},
    {"name": "万象城亲子手作课堂", "venue": "成都万象城", "district": "成华区", "start_date": "2026-07-12", "end_date": "2026-08-30", "fee": "收费", "description": "亲子手作课堂，万象城手作工坊，亲子共同创作。", "highlights": ["手作", "工坊", "创作"], "type": "亲子活动"},
    {"name": "万象城暑期童玩节", "venue": "成都万象城", "district": "成华区", "start_date": "2026-07-16", "end_date": "2026-08-29", "fee": "免费", "description": "暑期童玩节，万象城童玩体验区，怀旧与新潮结合。", "highlights": ["童玩", "怀旧", "体验"], "type": "亲子活动"},
    {"name": "万象城亲子科技展", "venue": "成都万象城", "district": "成华区", "start_date": "2026-07-20", "end_date": "2026-09-08", "fee": "部分免费", "description": "亲子科技展，万象城互动科技展，体验科技魅力。", "highlights": ["科技", "互动", "体验"], "type": "展览"},
    {"name": "成都大悦城亲子派对", "venue": "成都大悦城", "district": "武侯区", "start_date": "2026-07-05", "end_date": "2026-08-30", "fee": "免费", "description": "亲子派对，大悦城主题亲子派对，互动游戏欢乐多。", "highlights": ["派对", "主题", "互动"], "type": "亲子活动"},
    {"name": "成都大悦城儿童剧演出", "venue": "成都大悦城", "district": "武侯区", "start_date": "2026-07-09", "end_date": "2026-08-28", "fee": "收费", "description": "儿童剧演出，大悦城剧场儿童剧，沉浸式观剧体验。", "highlights": ["儿童剧", "剧场", "沉浸"], "type": "演出"},
    {"name": "成都大悦城亲子市集", "venue": "成都大悦城", "district": "武侯区", "start_date": "2026-07-13", "end_date": "2026-08-30", "fee": "免费", "description": "亲子市集，大悦城跳蚤市集，孩子当掌柜交换玩具。", "highlights": ["市集", "跳蚤", "交换"], "type": "亲子活动"},
    {"name": "成都大悦城暑期乐园", "venue": "成都大悦城", "district": "武侯区", "start_date": "2026-07-17", "end_date": "2026-08-29", "fee": "收费", "description": "暑期乐园，大悦城室内乐园，旋转木马与海洋球。", "highlights": ["乐园", "旋转木马", "海洋球"], "type": "亲子活动"},
    {"name": "成都大悦城亲子手作日", "venue": "成都大悦城", "district": "武侯区", "start_date": "2026-07-21", "end_date": "2026-08-28", "fee": "收费", "description": "亲子手作日，大悦城手作活动，陶艺彩绘DIY。", "highlights": ["手作", "陶艺", "彩绘"], "type": "亲子活动"},
    {"name": "银泰中心亲子艺术展", "venue": "成都银泰中心", "district": "高新区", "start_date": "2026-07-06", "end_date": "2026-08-28", "fee": "部分免费", "description": "亲子艺术展，银泰中心艺术空间，当代艺术亲子导览。", "highlights": ["艺术", "导览", "当代"], "type": "展览"},
    {"name": "银泰中心亲子手作课堂", "venue": "成都银泰中心", "district": "高新区", "start_date": "2026-07-10", "end_date": "2026-08-30", "fee": "收费", "description": "亲子手作课堂，银泰中心手工课，制作夏日手作。", "highlights": ["手作", "手工", "夏日"], "type": "亲子活动"},
    {"name": "来福士广场亲子嘉年华", "venue": "成都来福士广场", "district": "武侯区", "start_date": "2026-07-14", "end_date": "2026-08-29", "fee": "免费", "description": "亲子嘉年华，来福士广场暑期活动，亲子游戏集市。", "highlights": ["嘉年华", "游戏", "集市"], "type": "亲子活动"},
    {"name": "来福士广场儿童剧场", "venue": "成都来福士广场", "district": "武侯区", "start_date": "2026-07-18", "end_date": "2026-08-28", "fee": "收费", "description": "儿童剧场，来福士小型儿童剧演出，互动观剧。", "highlights": ["剧场", "儿童剧", "互动"], "type": "演出"},
    {"name": "IFS夏日亲子艺术市集", "venue": "成都IFS国际金融中心", "district": "锦江区", "start_date": "2026-07-22", "end_date": "2026-08-30", "fee": "免费", "description": "夏日艺术市集，IFS艺术主题市集，亲子逛集看展。", "highlights": ["市集", "艺术", "夏日"], "type": "亲子活动"},
]


def main():
    if not os.path.exists(DATA_FILE):
        print(f"文件 {DATA_FILE} 不存在！")
        exit(1)

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        exhibitions = json.load(f)

    # 统一补充 city 与 source 字段
    for item in new_activities:
        item['city'] = 'chengdu'
        item['source'] = '成都本地宝'

    # 名称唯一性自检（脚本内部数据不能重名）
    names_in_new = [a['name'] for a in new_activities]
    if len(names_in_new) != len(set(names_in_new)):
        dup = [n for n in names_in_new if names_in_new.count(n) > 1]
        print(f"脚本内部存在重复名称: {set(dup)}")
        exit(1)

    # 按已存在 name 去重
    existing_names = {e.get('name') for e in exhibitions}
    added_count = 0
    skipped_count = 0
    for activity in new_activities:
        if activity['name'] in existing_names:
            print(f"跳过(已存在): {activity['name']}")
            skipped_count += 1
            continue
        exhibitions.append(activity)
        print(f"添加: {activity['name']} ({activity['district']})")
        added_count += 1

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(exhibitions, f, ensure_ascii=False, indent=2)

    print("\n========== 添加统计 ==========")
    print(f"待添加活动总数: {len(new_activities)}")
    print(f"实际添加: {added_count}")
    print(f"跳过(已存在): {skipped_count}")
    print(f"当前成都活动总数: {sum(1 for e in exhibitions if e.get('city') == 'chengdu')}")
    print(f" exhibitions.json 总活动数: {len(exhibitions)}")

    # 按区县统计成都活动分布
    district_counts = {}
    for e in exhibitions:
        if e.get('city') == 'chengdu':
            d = e.get('district', '未知')
            district_counts[d] = district_counts.get(d, 0) + 1
    print("\n成都活动区县分布:")
    for d, c in sorted(district_counts.items(), key=lambda x: -x[1]):
        print(f"  {d}: {c}")

    # 按类型统计
    type_counts = {}
    for e in exhibitions:
        if e.get('city') == 'chengdu':
            t = e.get('type', '未知')
            type_counts[t] = type_counts.get(t, 0) + 1
    print("\n成都活动类型分布:")
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")


if __name__ == '__main__':
    main()
