#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""添加珠海市场馆和活动数据"""

import json
import os

ZHUHAI_VENUES = [
    # === 香洲区 ===
    {"name": "珠海博物馆", "source": "zhmuseum", "city": "zhuhai", "district": "香洲区", "type": "博物馆", "address": "香洲区海虹路88号", "transport": "公交4/5/12/14/15/16/204/B2/B3/Z19路海虹总站", "fee": "免费", "description": "珠海文化地标，馆藏陶瓷器、青铜器、书画等21个门类，设《珠海历史》《传统艺文和民俗文化》《共同的记忆》三大固定展厅。", "official_url": "https://www.zhsm.org.cn", "highlights": ["珠海历史", "民俗文化", "常设展览"]},
    {"name": "珠海市图书馆", "source": "zhlib", "city": "zhuhai", "district": "香洲区", "type": "图书馆", "address": "香洲区梅华街道迎宾北路3061号", "transport": "公交9/55/B10路市工人文化宫站", "fee": "免费", "description": "珠海中心图书馆，周二至周日9:00-21:00开放，逢周一闭馆，提供阅览、借阅、讲座等服务。", "official_url": "https://www.zhlib.gov.cn", "highlights": ["阅读推广", "讲座展览", "暑期活动"]},
    {"name": "珠海市文化馆", "source": "zhwhg", "city": "zhuhai", "district": "香洲区", "type": "文化馆", "address": "香洲区兰埔路164号", "transport": "公交1/13/25/60/62/69/991/992/B7/G991路圆明新园站", "fee": "免费", "description": "中国古典式四合院建筑风格，八大公共服务空间免费开放，含多功能厅、展览厅、免费阅读空间。", "official_url": "https://www.zhwhg.com", "highlights": ["艺术培训", "展览演出", "公益课程"]},
    {"name": "古元美术馆", "source": "gymuseum", "city": "zhuhai", "district": "香洲区", "type": "美术馆", "address": "香洲区梅华东路388号", "transport": "公交至梅华东路站", "fee": "免费", "description": "坐落于凤凰山南麓，常设版画、油画、雕塑等多元展览，从齐白石真迹到当代艺术作品。", "official_url": "https://www.gymuseum.cn", "highlights": ["版画收藏", "当代艺术", "网红楼梯"]},
    {"name": "珠海大剧院", "source": "zhtheatre", "city": "zhuhai", "district": "香洲区", "type": "剧院", "address": "香洲区情侣路野狸岛海韵城", "transport": "公交至野狸岛站", "fee": "收费", "description": "中国唯一建在海上的歌剧院，日月贝造型，含大剧场和多功能小剧场。", "official_url": "https://www.zhgrandtheatre.com", "highlights": ["海上歌剧院", "日月贝", "演出季"]},
    {"name": "香山文化艺术中心", "source": "xsart", "city": "zhuhai", "district": "香洲区", "type": "文化中心", "address": "香洲区建民路868号", "transport": "公交46/B10/B9/Z16路香山文化艺术中心站", "fee": "免费", "description": "综合性文化场馆，09:00-21:00开放，含展览、演出、培训等功能。", "official_url": "", "highlights": ["艺术展览", "演出活动", "文化培训"]},
    {"name": "珠海规划展览馆", "source": "zhplan", "city": "zhuhai", "district": "香洲区", "type": "展览馆", "address": "香洲区海虹路88号", "transport": "公交至海虹总站", "fee": "免费", "description": "与珠海博物馆相连，展示珠海城市规划建设成就和发展历程。", "official_url": "", "highlights": ["城市规划", "建设成就", "互动展示"]},
    {"name": "国家方志馆粤港澳大湾区分馆", "source": "fzg", "city": "zhuhai", "district": "香洲区", "type": "方志馆", "address": "香洲区", "transport": "公交至附近站点", "fee": "免费", "description": "华南地区首家国家方志馆分馆，珠海首家国字号文化场馆，2万平方米建筑面积，馆藏图书超5.3万册。", "official_url": "", "highlights": ["大湾区记忆", "地方志", "国字号场馆"]},
    {"name": "珠海市青少年妇女儿童活动中心", "source": "zhqsng", "city": "zhuhai", "district": "香洲区", "type": "青少年活动中心", "address": "香洲区", "transport": "公交至附近站点", "fee": "免费", "description": "面向青少年妇女儿童的综合性活动中心，提供培训、活动、展览等服务。", "official_url": "", "highlights": ["亲子活动", "兴趣培训", "暑期活动"]},
    {"name": "珠海市工人文化宫", "source": "zhgrwhg", "city": "zhuhai", "district": "香洲区", "type": "文化宫", "address": "香洲区", "transport": "公交9/55/B10路市工人文化宫站", "fee": "免费", "description": "职工文化活动阵地，提供文体活动、培训、展览等服务。", "official_url": "", "highlights": ["职工文化", "文体活动", "公益培训"]},
    {"name": "圆明新园", "source": "ymxy", "city": "zhuhai", "district": "香洲区", "type": "主题公园", "address": "香洲区兰埔路", "transport": "公交1/13/25/60/62/69路圆明新园站", "fee": "免费", "description": "以北京圆明园为原型的大型主题公园，免费开放，含皇家建筑、江南园林等景观。", "official_url": "", "highlights": ["皇家建筑", "江南园林", "免费开放"]},
    {"name": "梅溪牌坊", "source": "mxpf", "city": "zhuhai", "district": "香洲区", "type": "文物保护单位", "address": "香洲区前山镇梅溪村", "transport": "公交至梅溪牌坊站", "fee": "收费", "description": "光绪帝赐建的首任驻外大使陈芳故居，珠海重要历史人文景观。", "official_url": "", "highlights": ["历史人文", "陈芳故居", "牌坊建筑"]},
    {"name": "珠海国际会展中心", "source": "zhcec", "city": "zhuhai", "district": "香洲区", "type": "会展中心", "address": "香洲区湾仔南湾南路", "transport": "公交至会展中心站", "fee": "视展览而定", "description": "珠海大型国际会展中心，承办各类展览、会议、活动。", "official_url": "https://www.zicec.com", "highlights": ["国际展览", "会议承办", "大型活动"]},
    {"name": "华发商都", "source": "hfsd", "city": "zhuhai", "district": "香洲区", "type": "商业文化综合体", "address": "香洲区珠海大道8号", "transport": "公交至华发商都站", "fee": "免费", "description": "大型商业文化综合体，含文化展览、演出活动等。", "official_url": "", "highlights": ["文化展览", "商业活动", "亲子娱乐"]},
    {"name": "珠海海滨公园", "source": "hbgy", "city": "zhuhai", "district": "香洲区", "type": "公园", "address": "香洲区海滨南路", "transport": "公交至海滨公园站", "fee": "免费", "description": "情侣路沿线标志性公园，海景优美，适合休闲散步。", "official_url": "", "highlights": ["海景", "休闲散步", "亲子游玩"]},
    {"name": "景山公园", "source": "jsgy", "city": "zhuhai", "district": "香洲区", "type": "公园", "address": "香洲区吉大景山路", "transport": "公交至景山公园站", "fee": "免费", "description": "登高望远好去处，可俯瞰珠海城市景观和海景。", "official_url": "", "highlights": ["登高望远", "城市景观", "缆车索道"]},

    # === 金湾区 ===
    {"name": "金湾区图书馆", "source": "jwlib", "city": "zhuhai", "district": "金湾区", "type": "图书馆", "address": "金湾区三灶镇西城社区金河东路530号", "transport": "公交540/541/801/Z102/Z126/Z127路金湾市民中心南站", "fee": "免费", "description": "珠海最大公共图书馆，超100万册藏书，含少儿阅览区、自习室等。", "official_url": "", "highlights": ["百万藏书", "少儿阅览", "自习空间"]},
    {"name": "金湾区文化馆", "source": "jwwhg", "city": "zhuhai", "district": "金湾区", "type": "文化馆", "address": "金湾区三灶镇", "transport": "公交K9/Z102/Z103路金岛路东站", "fee": "免费", "description": "展示三灶鹤舞、竹草编织、狮舞民歌等12个非遗项目，9:00-21:00开放。", "official_url": "", "highlights": ["非遗展示", "青少儿艺术", "公益培训"]},
    {"name": "金湾区博物馆", "source": "jwmuseum", "city": "zhuhai", "district": "金湾区", "type": "博物馆", "address": "金湾区三灶镇鱼月村", "transport": "公交201/504/801/803/K9路月堂站或唐人街站", "fee": "免费", "description": "展陈面积2060㎡，常设林伟民主题陈列展、金湾文物展，周二至周日9:00-17:30开放。", "official_url": "", "highlights": ["林伟民陈列", "金湾文物", "工人运动史"]},
    {"name": "金湾艺术中心", "source": "jwart", "city": "zhuhai", "district": "金湾区", "type": "艺术中心", "address": "金湾区", "transport": "公交至金湾艺术中心站", "fee": "收费", "description": "金湾区标志性文化建筑，含剧场、展厅等功能空间。", "official_url": "", "highlights": ["演出展览", "艺术活动", "地标建筑"]},
    {"name": "汤臣倍健透明工厂", "source": "tcbj", "city": "zhuhai", "district": "金湾区", "type": "工业旅游", "address": "金湾区三灶镇星汉路19号", "transport": "公交Z106路汤臣倍健站", "fee": "部分免费", "description": "生产车间参观免费，营养探索馆互动体验收费，工作日9:00-17:00，周末9:00-17:30。", "official_url": "https://www.by-health.com", "highlights": ["工业旅游", "营养科普", "互动体验"]},
    {"name": "珠海航展馆", "source": "zhairshow", "city": "zhuhai", "district": "金湾区", "type": "展览馆", "address": "金湾区机场路航展馆", "transport": "航展期间专线", "fee": "需购票", "description": "中国国际航空航天博览会举办地，拥有多个标准化展馆及配套多功能新闻中心。", "official_url": "https://www.airshow.com.cn", "highlights": ["中国航展", "航空航天", "国际展览"]},
    {"name": "珠海海泉湾度假区", "source": "hqw", "city": "zhuhai", "district": "金湾区", "type": "度假区", "address": "金湾区平沙镇海泉湾路", "transport": "公交至海泉湾站", "fee": "收费", "description": "海洋温泉主题度假区，含温泉、酒店、主题乐园等。", "official_url": "https://www.hotspringbay.com", "highlights": ["海洋温泉", "主题乐园", "度假休闲"]},
    {"name": "金湾体育中心", "source": "jwtyzx", "city": "zhuhai", "district": "金湾区", "type": "体育中心", "address": "金湾区三灶镇", "transport": "公交至金湾体育中心站", "fee": "免费", "description": "金湾区综合性体育场馆，含田径场、游泳馆、体育馆等。", "official_url": "", "highlights": ["体育赛事", "全民健身", "场馆租赁"]},
    {"name": "三灶镇文化中心", "source": "szwhzx", "city": "zhuhai", "district": "金湾区", "type": "文化中心", "address": "金湾区三灶镇", "transport": "公交至三灶站", "fee": "免费", "description": "三灶镇基层文化服务阵地，提供图书阅览、文艺培训等服务。", "official_url": "", "highlights": ["基层文化", "文艺培训", "社区活动"]},
    {"name": "金海岸文化艺术中心", "source": "jhawhys", "city": "zhuhai", "district": "金湾区", "type": "文化中心", "address": "金湾区金海岸大道", "transport": "公交至金海岸站", "fee": "免费", "description": "金海岸片区文化活动场所，含展览、演出等功能。", "official_url": "", "highlights": ["社区文化", "展览演出", "文艺活动"]},

    # === 斗门区 ===
    {"name": "斗门区图书馆", "source": "dmlib", "city": "zhuhai", "district": "斗门区", "type": "图书馆", "address": "斗门区江湾中路2号", "transport": "公交303/306/405/502/503/504/510/601/B37/K5/T12/Z278路尖峰站", "fee": "免费", "description": "斗门区公共图书馆，周二至周五9:00-21:00，周六至周日9:00-18:00。", "official_url": "", "highlights": ["图书借阅", "阅读推广", "暑期活动"]},
    {"name": "斗门区博物馆", "source": "dmmuseum", "city": "zhuhai", "district": "斗门区", "type": "博物馆", "address": "斗门区井岸镇", "transport": "公交至斗门区博物馆站", "fee": "免费", "description": "展示斗门历史文化和民俗风情，含斗门旧事、民俗文化等展览。", "official_url": "", "highlights": ["斗门历史", "民俗文化", "常设展览"]},
    {"name": "斗门区文化馆", "source": "dmwhg", "city": "zhuhai", "district": "斗门区", "type": "文化馆", "address": "斗门区井岸镇", "transport": "公交至斗门区文化馆站", "fee": "免费", "description": "斗门区文化活动阵地，提供文艺培训、展览演出等服务。", "official_url": "", "highlights": ["文艺培训", "非遗传承", "群众文化"]},
    {"name": "斗门旧街", "source": "dmjj", "city": "zhuhai", "district": "斗门区", "type": "历史文化街区", "address": "斗门区斗门镇", "transport": "公交至斗门旧街站", "fee": "免费", "description": "珠海保存最完整的骑楼街之一，中西合璧建筑风格，充满历史韵味。", "official_url": "", "highlights": ["骑楼建筑", "历史文化", "特色美食"]},
    {"name": "金台寺", "source": "jts", "city": "zhuhai", "district": "斗门区", "type": "寺庙", "address": "斗门区乾务镇黄杨山", "transport": "公交至金台寺站", "fee": "免费", "description": "黄杨山风景区著名寺庙，环境清幽，香火旺盛。", "official_url": "", "highlights": ["佛教文化", "黄杨山景", "祈福圣地"]},
    {"name": "御温泉", "source": "ywq", "city": "zhuhai", "district": "斗门区", "type": "温泉度假", "address": "斗门区斗门镇", "transport": "公交至御温泉站", "fee": "收费", "description": "日式温泉度假村，含多种温泉池、日式住宿、美食等。", "official_url": "https://www.yuwengquan.com", "highlights": ["日式温泉", "度假休闲", "特色美食"]},
    {"name": "斗门体育中心", "source": "dmtyzx", "city": "zhuhai", "district": "斗门区", "type": "体育中心", "address": "斗门区井岸镇", "transport": "公交至斗门体育中心站", "fee": "免费", "description": "斗门区综合性体育场馆，含田径场、游泳馆、体育馆等。", "official_url": "", "highlights": ["体育赛事", "全民健身", "场馆租赁"]},
    {"name": "井岸镇文化中心", "source": "jawhzx", "city": "zhuhai", "district": "斗门区", "type": "文化中心", "address": "斗门区井岸镇", "transport": "公交至井岸镇站", "fee": "免费", "description": "井岸镇基层文化服务阵地，提供图书阅览、文艺培训等服务。", "official_url": "", "highlights": ["基层文化", "文艺培训", "社区活动"]},
    {"name": "黄杨山", "source": "hys", "city": "zhuhai", "district": "斗门区", "type": "风景名胜", "address": "斗门区乾务镇", "transport": "公交至黄杨山站", "fee": "免费", "description": "珠海第一峰，风景秀丽，有金台寺、石景山等景点。", "official_url": "", "highlights": ["登山徒步", "自然风光", "金台寺"]},
    {"name": "斗门非遗展示馆", "source": "dmfy", "city": "zhuhai", "district": "斗门区", "type": "展览馆", "address": "斗门区斗门镇", "transport": "公交至斗门镇站", "fee": "免费", "description": "展示斗门区非物质文化遗产，含水上婚嫁、装泥鱼等非遗项目。", "official_url": "", "highlights": ["非遗展示", "水上婚嫁", "装泥鱼"]},

    # === 横琴新区 ===
    {"name": "横琴文化艺术中心", "source": "hqwhys", "city": "zhuhai", "district": "横琴新区", "type": "文化中心", "address": "横琴新区琴朗路与琴政路交叉口东南角", "transport": "公交Z50/Z56路横琴文化艺术中心站", "fee": "免费", "description": "横琴新区综合性文化场馆，周二至周日10:00-18:00开放，周一闭馆。", "official_url": "", "highlights": ["艺术展览", "文化培训", "演出活动"]},
    {"name": "珠海长隆海洋王国", "source": "zhlh", "city": "zhuhai", "district": "横琴新区", "type": "主题乐园", "address": "香洲区横琴镇环岛路长隆大道1号", "transport": "公交至长隆站", "fee": "收费", "description": "世界级海洋主题乐园，八大主题园区，含海洋动物、游乐设备、大型演艺，10:00-20:00。", "official_url": "https://www.chimelong.com", "highlights": ["海洋动物", "大型演艺", "烟花秀"]},
    {"name": "珠海长隆飞船乐园", "source": "zhfclc", "city": "zhuhai", "district": "横琴新区", "type": "主题乐园", "address": "香洲区环岛东路与长隆大道交叉口西南1500米", "transport": "公交至长隆飞船乐园站", "fee": "收费", "description": "15大主题区域，含宇宙世界、峡谷星球、星际站台、珊瑚秘境等，10:00-18:00。", "official_url": "https://www.chimelong.com", "highlights": ["宇宙主题", "互动体验", "亲子乐园"]},
    {"name": "珠海长隆横琴剧院", "source": "zhhqtj", "city": "zhuhai", "district": "横琴新区", "type": "剧院", "address": "香洲区环岛路富祥海湾长隆度假区内", "transport": "公交至长隆站", "fee": "收费", "description": "国际顶尖团队打造的大马戏节目《长隆秀》，常规开演时间17:00。", "official_url": "https://www.chimelong.com", "highlights": ["国际马戏", "长隆秀", "演艺盛宴"]},
    {"name": "横琴国际网球中心", "source": "hqwlqzx", "city": "zhuhai", "district": "横琴新区", "type": "体育中心", "address": "横琴新区横琴大道", "transport": "公交至横琴国际网球中心站", "fee": "视赛事而定", "description": "WTA超级精英赛等国际赛事举办地，含中心球场、训练场等。", "official_url": "https://www.hengqintennis.com", "highlights": ["国际赛事", "WTA网球", "体育演出"]},
    {"name": "星乐度露营小镇", "source": "xld", "city": "zhuhai", "district": "横琴新区", "type": "露营度假", "address": "横琴新区环岛北路", "transport": "公交至星乐度站", "fee": "收费", "description": "户外露营主题度假小镇，含房车、木屋、星空露营等住宿体验。", "official_url": "https://www.starryland.cn", "highlights": ["户外露营", "房车体验", "亲子活动"]},
    {"name": "横琴湿地公园", "source": "hqsdgy", "city": "zhuhai", "district": "横琴新区", "type": "公园", "address": "横琴新区琴海北路", "transport": "公交至横琴湿地公园站", "fee": "免费", "description": "红树林湿地生态公园，观鸟、赏红树林、自然教育好去处。", "official_url": "", "highlights": ["红树林", "观鸟", "自然教育"]},
    {"name": "横琴花海长廊", "source": "hqhchl", "city": "zhuhai", "district": "横琴新区", "type": "公园", "address": "横琴新区环岛北路", "transport": "公交至花海长廊站", "fee": "免费", "description": "五公里花海长廊，四季花开，适合骑行、散步、拍照。", "official_url": "", "highlights": ["花海景观", "骑行散步", "拍照打卡"]},
    {"name": "横琴口岸", "source": "hqka", "city": "zhuhai", "district": "横琴新区", "type": "口岸", "address": "横琴新区琴朗路", "transport": "公交至横琴口岸站", "fee": "免费", "description": "连接珠海横琴与澳门的口岸，24小时通关，含免税购物区。", "official_url": "", "highlights": ["口岸通关", "免税购物", "珠澳往来"]},
    {"name": "横琴金融岛", "source": "hqjrd", "city": "zhuhai", "district": "横琴新区", "type": "商务区", "address": "横琴新区金融岛", "transport": "公交至金融岛站", "fee": "免费", "description": "横琴新区金融商务核心区，现代建筑景观，海景优美。", "official_url": "", "highlights": ["金融商务", "现代建筑", "海景风光"]},

    # === 补充场馆 ===
    {"name": "珠海渔女景区", "source": "zhyn", "city": "zhuhai", "district": "香洲区", "type": "风景名胜", "address": "香洲区情侣中路", "transport": "公交9/99路珠海渔女站", "fee": "免费", "description": "珠海标志性景点，渔女雕像矗立在海边，是珠海的城市象征。", "official_url": "", "highlights": ["城市地标", "海边雕塑", "拍照打卡"]},
    {"name": "野狸岛音乐广场", "source": "yld", "city": "zhuhai", "district": "香洲区", "type": "广场", "address": "香洲区野狸岛", "transport": "公交至野狸岛站", "fee": "免费", "description": "野狸岛海韵城音乐广场，与珠海大剧院相邻，海景广场休闲好去处。", "official_url": "", "highlights": ["海景广场", "音乐活动", "休闲散步"]},
    {"name": "珠海市体育中心", "source": "zhtyzx", "city": "zhuhai", "district": "香洲区", "type": "体育中心", "address": "香洲区红山路163号", "transport": "公交至体育中心站", "fee": "免费", "description": "珠海市综合性体育场馆，含体育场、体育馆、游泳馆等，承办各类体育赛事和演出。", "official_url": "", "highlights": ["体育赛事", "大型演出", "全民健身"]},
    {"name": "香洲区文化馆", "source": "xzwhg", "city": "zhuhai", "district": "香洲区", "type": "文化馆", "address": "香洲区", "transport": "公交至香洲区文化馆站", "fee": "免费", "description": "香洲区文化服务阵地，提供文艺培训、展览演出、图书阅览等服务。", "official_url": "", "highlights": ["群众文化", "文艺培训", "社区活动"]},
]

ZHUHAI_ACTIVITIES = [
    # === 香洲区活动（40个）===
    {"title": "珠海历史常设展", "venue": "珠海博物馆", "start_date": "2026-01-01", "end_date": "2026-12-31", "link": "https://www.zhsm.org.cn", "description": "从新石器时代先民用具到近代香山名人手稿，展示珠海从远古到近代的完整历史印记，常设展览免费参观。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "珠海博物馆"},
    {"title": "传统艺文和民俗文化展", "venue": "珠海博物馆", "start_date": "2026-01-01", "end_date": "2026-12-31", "link": "https://www.zhsm.org.cn", "description": "展示珠海传统艺文和民俗文化，含香山文化、客家文化、水上人家等主题内容。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "珠海博物馆"},
    {"title": "共同的记忆——珠海城市变迁展", "venue": "珠海博物馆", "start_date": "2026-01-01", "end_date": "2026-12-31", "link": "https://www.zhsm.org.cn", "description": "回顾珠海城市发展的共同记忆，从渔村到现代化城市的变迁历程。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "珠海博物馆"},
    {"title": "珠海博物馆暑期亲子讲解活动", "venue": "珠海博物馆", "start_date": "2026-07-15", "end_date": "2026-08-31", "link": "https://www.zhsm.org.cn", "description": "暑期期间珠海博物馆推出亲子讲解活动，专业讲解员带领小朋友了解珠海历史，寓教于乐。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "珠海博物馆"},
    {"title": "珠海市图书馆暑期阅读季", "venue": "珠海市图书馆", "start_date": "2026-07-01", "end_date": "2026-08-31", "link": "https://www.zhlib.gov.cn", "description": "珠海市图书馆暑期阅读推广活动，含阅读分享会、亲子故事会、好书推荐等系列活动。", "category": "讲座阅读", "fee": "免费", "contact": "", "family_friendly": True, "source": "珠海市图书馆"},
    {"title": "珠海市图书馆公益讲座", "venue": "珠海市图书馆", "start_date": "2026-07-05", "end_date": "2026-07-05", "link": "https://www.zhlib.gov.cn", "description": "珠海市图书馆周末公益讲座，邀请专家学者分享文化、历史、艺术等主题内容。", "category": "讲座阅读", "fee": "免费", "contact": "", "family_friendly": False, "source": "珠海市图书馆"},
    {"title": "亲子绘本故事会", "venue": "珠海市图书馆", "start_date": "2026-07-12", "end_date": "2026-07-12", "link": "https://www.zhlib.gov.cn", "description": "珠海市图书馆少儿阅览区亲子绘本故事会，适合3-8岁儿童及家长参与。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "珠海市图书馆"},
    {"title": "珠海市文化馆公益艺术培训", "venue": "珠海市文化馆", "start_date": "2026-07-01", "end_date": "2026-08-31", "link": "https://www.zhwhg.com", "description": "暑期公益艺术培训班，含书法、绘画、舞蹈、声乐等课程，面向市民免费开放。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "珠海市文化馆"},
    {"title": "珠海市文化馆非遗展示活动", "venue": "珠海市文化馆", "start_date": "2026-07-20", "end_date": "2026-07-20", "link": "https://www.zhwhg.com", "description": "珠海非物质文化遗产展示活动，含粤剧、醒狮、茶果制作等非遗项目体验。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "珠海市文化馆"},
    {"title": "古元美术馆版画艺术展", "venue": "古元美术馆", "start_date": "2026-07-01", "end_date": "2026-09-30", "link": "https://www.gymuseum.cn", "description": "古元版画艺术精品展，展示珠海版画大师古元的经典作品及当代版画创作。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "古元美术馆"},
    {"title": "齐白石真迹展", "venue": "古元美术馆", "start_date": "2026-07-15", "end_date": "2026-08-15", "link": "https://www.gymuseum.cn", "description": "齐白石真迹精品展，展示齐白石先生的绘画真迹，感受国画大师的艺术魅力。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "古元美术馆"},
    {"title": "当代艺术邀请展", "venue": "古元美术馆", "start_date": "2026-08-01", "end_date": "2026-09-30", "link": "https://www.gymuseum.cn", "description": "当代艺术邀请展，汇聚多位当代艺术家的先锋创作，从传统水墨到现代装置艺术。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": False, "source": "古元美术馆"},
    {"title": "珠海大剧院交响乐演出季", "venue": "珠海大剧院", "start_date": "2026-07-25", "end_date": "2026-07-25", "link": "https://www.zhgrandtheatre.com", "description": "珠海大剧院夏季交响乐演出，知名交响乐团带来经典曲目，海上歌剧院享受音乐盛宴。", "category": "演出", "fee": "收费", "contact": "", "family_friendly": False, "source": "珠海大剧院"},
    {"title": "珠海大剧院亲子音乐剧", "venue": "珠海大剧院", "start_date": "2026-08-02", "end_date": "2026-08-02", "link": "https://www.zhgrandtheatre.com", "description": "适合全家观看的亲子音乐剧，在日月贝造型的海上歌剧院享受亲子时光。", "category": "演出", "fee": "收费", "contact": "", "family_friendly": True, "source": "珠海大剧院"},
    {"title": "珠海大剧院话剧演出", "venue": "珠海大剧院", "start_date": "2026-08-09", "end_date": "2026-08-09", "link": "https://www.zhgrandtheatre.com", "description": "知名话剧团体在珠海大剧院演出经典话剧作品，感受戏剧艺术的魅力。", "category": "演出", "fee": "收费", "contact": "", "family_friendly": False, "source": "珠海大剧院"},
    {"title": "香山文化艺术中心暑期展览", "venue": "香山文化艺术中心", "start_date": "2026-07-01", "end_date": "2026-08-31", "link": "", "description": "香山文化艺术中心暑期系列展览，含书画展、摄影展、手工艺品展等。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "香山文化艺术中心"},
    {"title": "香山文化艺术中心少儿才艺展演", "venue": "香山文化艺术中心", "start_date": "2026-07-28", "end_date": "2026-07-28", "link": "", "description": "香山文化艺术中心少儿才艺展演活动，为孩子们提供展示才艺的舞台。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "香山文化艺术中心"},
    {"title": "珠海规划展览馆城市记忆展", "venue": "珠海规划展览馆", "start_date": "2026-01-01", "end_date": "2026-12-31", "link": "", "description": "展示珠海从渔村到现代化城市的规划建设成就，含互动模型、多媒体展示等。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "珠海规划展览馆"},
    {"title": "国家方志馆大湾区记忆展", "venue": "国家方志馆粤港澳大湾区分馆", "start_date": "2026-01-01", "end_date": "2026-12-31", "link": "", "description": "华南地区首家国家方志馆分馆，馆藏图书超5.3万册，展示大湾区历史文化和城市记忆。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "国家方志馆"},
    {"title": "珠海青少年妇女儿童活动中心暑期班", "venue": "珠海市青少年妇女儿童活动中心", "start_date": "2026-07-15", "end_date": "2026-08-25", "link": "", "description": "暑期兴趣培训班，含美术、音乐、舞蹈、科技等课程，面向青少年和妇女儿童。", "category": "亲子活动", "fee": "收费", "contact": "", "family_friendly": True, "source": "珠海市青少年妇女儿童活动中心"},
    {"title": "珠海工人文化宫职工文化节", "venue": "珠海市工人文化宫", "start_date": "2026-07-20", "end_date": "2026-08-20", "link": "", "description": "职工文化节系列活动，含文艺汇演、体育比赛、技能展示等，丰富职工文化生活。", "category": "其他", "fee": "免费", "contact": "", "family_friendly": False, "source": "珠海市工人文化宫"},
    {"title": "圆明新园夏日文化游园会", "venue": "圆明新园", "start_date": "2026-07-01", "end_date": "2026-08-31", "link": "", "description": "圆明新园夏日文化游园会，免费开放，含皇家建筑参观、园林游览、文化表演等。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "圆明新园"},
    {"title": "梅溪牌坊历史文化讲解", "venue": "梅溪牌坊", "start_date": "2026-07-10", "end_date": "2026-08-31", "link": "", "description": "梅溪牌坊历史文化讲解活动，了解首任驻外大使陈芳的传奇人生和珠海华侨历史。", "category": "科普活动", "fee": "收费", "contact": "", "family_friendly": True, "source": "梅溪牌坊"},
    {"title": "珠海国际会展中心暑期展览", "venue": "珠海国际会展中心", "start_date": "2026-07-15", "end_date": "2026-08-30", "link": "https://www.zicec.com", "description": "珠海国际会展中心暑期系列展览，含文创展、家居展、美食展等，具体以现场为准。", "category": "展览", "fee": "部分免费", "contact": "", "family_friendly": True, "source": "珠海国际会展中心"},
    {"title": "华发商都夏日文化市集", "venue": "华发商都", "start_date": "2026-07-25", "end_date": "2026-08-15", "link": "", "description": "华发商都夏日文化市集，含文创摊位、手作体验、街头表演等，适合全家参与。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "华发商都"},
    {"title": "海滨公园亲子户外活动", "venue": "珠海海滨公园", "start_date": "2026-07-01", "end_date": "2026-08-31", "link": "", "description": "情侣路海滨公园亲子户外活动，海景优美，适合放风筝、散步、观海等休闲活动。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "珠海海滨公园"},
    {"title": "景山公园缆车观景体验", "venue": "景山公园", "start_date": "2026-01-01", "end_date": "2026-12-31", "link": "", "description": "景山公园缆车索道观景体验，登高俯瞰珠海城市景观和海景，天气晴好时视野极佳。", "category": "亲子活动", "fee": "收费", "contact": "", "family_friendly": True, "source": "景山公园"},
    {"title": "珠海博物馆夜间开放活动", "venue": "珠海博物馆", "start_date": "2026-07-19", "end_date": "2026-08-30", "link": "https://www.zhsm.org.cn", "description": "暑期周五夜间开放活动，夜游博物馆，感受不同于白天的观展体验。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "珠海博物馆"},
    {"title": "珠海市图书馆古诗词鉴赏讲座", "venue": "珠海市图书馆", "start_date": "2026-07-26", "end_date": "2026-07-26", "link": "https://www.zhlib.gov.cn", "description": "古诗词鉴赏公益讲座，邀请文学专家解读经典诗词，感受中华传统文化之美。", "category": "讲座阅读", "fee": "免费", "contact": "", "family_friendly": True, "source": "珠海市图书馆"},
    {"title": "珠海市文化馆书画展览", "venue": "珠海市文化馆", "start_date": "2026-08-01", "end_date": "2026-08-31", "link": "https://www.zhwhg.com", "description": "珠海市文化馆八月书画展览，展示本地书画家作品，含山水、花鸟、书法等。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "珠海市文化馆"},
    {"title": "香山文化艺术中心交响音乐会", "venue": "香山文化艺术中心", "start_date": "2026-08-15", "end_date": "2026-08-15", "link": "", "description": "香山文化艺术中心夏季交响音乐会，知名乐团演绎经典曲目。", "category": "演出", "fee": "收费", "contact": "", "family_friendly": False, "source": "香山文化艺术中心"},
    {"title": "珠海大剧院芭蕾舞演出", "venue": "珠海大剧院", "start_date": "2026-08-16", "end_date": "2026-08-16", "link": "https://www.zhgrandtheatre.com", "description": "经典芭蕾舞剧在珠海大剧院上演，在海上日月贝享受优雅的芭蕾艺术。", "category": "演出", "fee": "收费", "contact": "", "family_friendly": True, "source": "珠海大剧院"},
    {"title": "古元美术馆少儿美术工作坊", "venue": "古元美术馆", "start_date": "2026-07-22", "end_date": "2026-07-22", "link": "https://www.gymuseum.cn", "description": "古元美术馆少儿美术工作坊，专业老师指导小朋友学习版画、绘画等艺术创作。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "古元美术馆"},
    {"title": "珠海博物馆考古体验活动", "venue": "珠海博物馆", "start_date": "2026-08-03", "end_date": "2026-08-03", "link": "https://www.zhsm.org.cn", "description": "珠海博物馆考古体验活动，模拟考古发掘，了解考古知识，适合中小学生参与。", "category": "科普活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "珠海博物馆"},
    {"title": "珠海市图书馆电影放映活动", "venue": "珠海市图书馆", "start_date": "2026-08-04", "end_date": "2026-08-04", "link": "https://www.zhlib.gov.cn", "description": "珠海市图书馆公益电影放映活动，播放经典文化主题电影，免费入场。", "category": "影视放映", "fee": "免费", "contact": "", "family_friendly": True, "source": "珠海市图书馆"},
    {"title": "珠海市文化馆广场舞大赛", "venue": "珠海市文化馆", "start_date": "2026-08-10", "end_date": "2026-08-10", "link": "https://www.zhwhg.com", "description": "珠海市文化馆广场舞大赛，各社区广场舞队伍同台竞技，展现群众文化风采。", "category": "其他", "fee": "免费", "contact": "", "family_friendly": True, "source": "珠海市文化馆"},
    {"title": "圆明新园传统文化表演", "venue": "圆明新园", "start_date": "2026-08-17", "end_date": "2026-08-17", "link": "", "description": "圆明新园传统文化表演，含古典舞蹈、民乐演奏、戏曲等，免费观看。", "category": "演出", "fee": "免费", "contact": "", "family_friendly": True, "source": "圆明新园"},
    {"title": "珠海国际会展中心动漫展", "venue": "珠海国际会展中心", "start_date": "2026-08-22", "end_date": "2026-08-23", "link": "https://www.zicec.com", "description": "珠海国际动漫展览，含动漫周边、cosplay、声优见面会等，二次元文化盛宴。", "category": "展览", "fee": "收费", "contact": "", "family_friendly": True, "source": "珠海国际会展中心"},
    {"title": "华发商都露天音乐会", "venue": "华发商都", "start_date": "2026-08-24", "end_date": "2026-08-24", "link": "", "description": "华发商都露天音乐会，本地乐队和歌手现场表演，免费观看，适合夏夜休闲。", "category": "演出", "fee": "免费", "contact": "", "family_friendly": True, "source": "华发商都"},
    {"title": "景山公园日出观景活动", "venue": "景山公园", "start_date": "2026-08-25", "end_date": "2026-08-25", "link": "", "description": "景山公园日出观景活动，清晨登高观日出，俯瞰珠海晨景，需提前预约。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "景山公园"},

    # === 金湾区活动（20个）===
    {"title": "金湾区图书馆暑期阅读营", "venue": "金湾区图书馆", "start_date": "2026-07-10", "end_date": "2026-08-31", "link": "", "description": "金湾区图书馆暑期阅读营活动，含阅读分享、亲子共读、好书推荐等，少儿阅览区免费参与。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "金湾区图书馆"},
    {"title": "手作·造物——现代手工艺师生作品展", "venue": "金湾区图书馆", "start_date": "2026-06-15", "end_date": "2026-07-29", "link": "", "description": "陶瓷、广府金绣、掐丝珐琅与非遗点翠等20余个门类的工艺美术作品在一楼中庭展出。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "金湾区图书馆"},
    {"title": "金湾区图书馆「云」自习室体验", "venue": "金湾区图书馆", "start_date": "2026-01-01", "end_date": "2026-12-31", "link": "", "description": "金湾区图书馆「云」自习室和24小时「开卷」自习室，提供专注学习空间。", "category": "讲座阅读", "fee": "免费", "contact": "", "family_friendly": False, "source": "金湾区图书馆"},
    {"title": "金湾区文化馆非遗体验活动", "venue": "金湾区文化馆", "start_date": "2026-07-15", "end_date": "2026-08-30", "link": "", "description": "三灶鹤舞、竹草编织、狮舞民歌等12个非遗项目体验活动，边看边玩。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "金湾区文化馆"},
    {"title": "童心向党——金湾区青少儿艺术花会优秀作品展", "venue": "金湾区文化馆", "start_date": "2026-06-15", "end_date": "2026-07-31", "link": "", "description": "金湾区青少儿艺术花会优秀作品展，展出813件艺术感十足的青少儿艺术作品。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "金湾区文化馆"},
    {"title": "金湾区博物馆林伟民主题陈列展", "venue": "金湾区博物馆", "start_date": "2026-01-01", "end_date": "2026-12-31", "link": "", "description": "以林伟民生平为线索，分五个篇章串起珍贵历史照片与场景复原，了解早期工人运动历史。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "金湾区博物馆"},
    {"title": "金湾文物展", "venue": "金湾区博物馆", "start_date": "2026-01-01", "end_date": "2026-12-31", "link": "", "description": "金湾文物展，展示数千年的海洋文明，探寻先民在珠海创造的海岛文明。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "金湾区博物馆"},
    {"title": "广东省第一次全国可移动文物普查成果图片展", "venue": "金湾区博物馆", "start_date": "2026-07-14", "end_date": "2026-10-18", "link": "", "description": "近百幅图表展示岭南文物精华，带你一次看遍广东省可移动文物普查成果。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "金湾区博物馆"},
    {"title": "金湾艺术中心夏季演出季", "venue": "金湾艺术中心", "start_date": "2026-07-20", "end_date": "2026-08-31", "link": "", "description": "金湾艺术中心夏季演出季，含音乐会、话剧、舞蹈等多种演出形式。", "category": "演出", "fee": "收费", "contact": "", "family_friendly": False, "source": "金湾艺术中心"},
    {"title": "汤臣倍健透明工厂参观", "venue": "汤臣倍健透明工厂", "start_date": "2026-07-01", "end_date": "2026-08-31", "link": "https://www.by-health.com", "description": "营养健康科普参观，生产车间免费参观，营养探索馆互动体验收费，了解营养健康知识。", "category": "科普活动", "fee": "部分免费", "contact": "", "family_friendly": True, "source": "汤臣倍健透明工厂"},
    {"title": "金湾区图书馆亲子手工坊", "venue": "金湾区图书馆", "start_date": "2026-07-19", "end_date": "2026-07-19", "link": "", "description": "金湾区图书馆少儿阅览区亲子手工坊活动，专业老师指导手工制作，适合4-10岁儿童。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "金湾区图书馆"},
    {"title": "金湾区文化馆公益舞蹈培训", "venue": "金湾区文化馆", "start_date": "2026-07-22", "end_date": "2026-08-26", "link": "", "description": "金湾区文化馆暑期公益舞蹈培训班，含民族舞、现代舞等课程，面向市民免费开放。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "金湾区文化馆"},
    {"title": "金湾体育中心暑期游泳班", "venue": "金湾体育中心", "start_date": "2026-07-15", "end_date": "2026-08-25", "link": "", "description": "金湾体育中心暑期游泳培训班，专业教练指导，适合青少年及成人报名。", "category": "体育赛事", "fee": "收费", "contact": "", "family_friendly": True, "source": "金湾体育中心"},
    {"title": "金海岸文化艺术中心社区文艺汇演", "venue": "金海岸文化艺术中心", "start_date": "2026-08-02", "end_date": "2026-08-02", "link": "", "description": "金海岸社区文艺汇演，各社区文艺队伍同台演出，展现社区文化风采。", "category": "演出", "fee": "免费", "contact": "", "family_friendly": True, "source": "金海岸文化艺术中心"},
    {"title": "三灶镇文化中心暑期少儿活动", "venue": "三灶镇文化中心", "start_date": "2026-07-18", "end_date": "2026-08-18", "link": "", "description": "三灶镇文化中心暑期少儿系列活动，含书法、绘画、阅读等，免费参与。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "三灶镇文化中心"},
    {"title": "金湾区图书馆英语角活动", "venue": "金湾区图书馆", "start_date": "2026-08-09", "end_date": "2026-08-09", "link": "", "description": "金湾区图书馆英语角活动，外教带领练习英语口语，适合青少年及英语爱好者。", "category": "讲座阅读", "fee": "免费", "contact": "", "family_friendly": True, "source": "金湾区图书馆"},
    {"title": "海泉湾夏日温泉度假活动", "venue": "珠海海泉湾度假区", "start_date": "2026-07-01", "end_date": "2026-08-31", "link": "https://www.hotspringbay.com", "description": "海泉湾夏日温泉度假活动，含海洋温泉、水上乐园、主题酒店等，适合亲子度假。", "category": "亲子活动", "fee": "收费", "contact": "", "family_friendly": True, "source": "珠海海泉湾度假区"},
    {"title": "金湾区文化馆摄影展", "venue": "金湾区文化馆", "start_date": "2026-08-15", "end_date": "2026-09-15", "link": "", "description": "金湾区文化馆摄影作品展，展示金湾区自然风光、人文风情，免费参观。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "金湾区文化馆"},
    {"title": "金湾体育中心篮球邀请赛", "venue": "金湾体育中心", "start_date": "2026-08-20", "end_date": "2026-08-21", "link": "", "description": "金湾体育中心夏季篮球邀请赛，各企事业单位和社区队伍参赛，免费观赛。", "category": "体育赛事", "fee": "免费", "contact": "", "family_friendly": True, "source": "金湾体育中心"},
    {"title": "金湾区博物馆小小讲解员培训", "venue": "金湾区博物馆", "start_date": "2026-08-05", "end_date": "2026-08-12", "link": "", "description": "金湾区博物馆小小讲解员培训班，面向中小学生，学习讲解技巧和历史文化知识。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "金湾区博物馆"},

    # === 斗门区活动（20个）===
    {"title": "斗门区图书馆暑期阅读活动", "venue": "斗门区图书馆", "start_date": "2026-07-05", "end_date": "2026-08-31", "link": "", "description": "斗门区图书馆暑期阅读推广活动，含读书会、绘本故事、好书推荐等系列活动。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "斗门区图书馆"},
    {"title": "斗门区图书馆公益讲座", "venue": "斗门区图书馆", "start_date": "2026-07-13", "end_date": "2026-07-13", "link": "", "description": "斗门区图书馆周末公益讲座，邀请本地学者分享斗门历史文化、民俗风情等主题。", "category": "讲座阅读", "fee": "免费", "contact": "", "family_friendly": False, "source": "斗门区图书馆"},
    {"title": "斗门区博物馆历史展", "venue": "斗门区博物馆", "start_date": "2026-01-01", "end_date": "2026-12-31", "link": "", "description": "斗门区博物馆常设展览，展示斗门历史文化和民俗风情，含斗门旧事、民俗文化等。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "斗门区博物馆"},
    {"title": "斗门区文化馆暑期公益培训", "venue": "斗门区文化馆", "start_date": "2026-07-10", "end_date": "2026-08-20", "link": "", "description": "斗门区文化馆暑期公益培训班，含书法、国画、舞蹈、声乐等课程，免费报名。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "斗门区文化馆"},
    {"title": "斗门旧街历史文化游览", "venue": "斗门旧街", "start_date": "2026-07-01", "end_date": "2026-08-31", "link": "", "description": "斗门旧街历史文化游览，珠海保存最完整的骑楼街之一，中西合璧建筑风格，免费参观。", "category": "科普活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "斗门旧街"},
    {"title": "金台寺夏日祈福活动", "venue": "金台寺", "start_date": "2026-07-01", "end_date": "2026-08-31", "link": "", "description": "金台寺夏日祈福活动，黄杨山风景区著名寺庙，环境清幽，免费参观。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "金台寺"},
    {"title": "御温泉夏日亲子活动", "venue": "御温泉", "start_date": "2026-07-01", "end_date": "2026-08-31", "link": "https://www.yuwengquan.com", "description": "御温泉夏日亲子活动，日式温泉度假村，含多种温泉池、日式住宿、美食体验。", "category": "亲子活动", "fee": "收费", "contact": "", "family_friendly": True, "source": "御温泉"},
    {"title": "斗门体育中心暑期运动营", "venue": "斗门体育中心", "start_date": "2026-07-15", "end_date": "2026-08-25", "link": "", "description": "斗门体育中心暑期运动营，含足球、篮球、游泳等项目，专业教练指导。", "category": "体育赛事", "fee": "收费", "contact": "", "family_friendly": True, "source": "斗门体育中心"},
    {"title": "井岸镇文化中心社区活动", "venue": "井岸镇文化中心", "start_date": "2026-07-25", "end_date": "2026-08-25", "link": "", "description": "井岸镇文化中心暑期社区文化活动，含文艺演出、图书阅览、兴趣培训等。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "井岸镇文化中心"},
    {"title": "黄杨山登山活动", "venue": "黄杨山", "start_date": "2026-08-08", "end_date": "2026-08-08", "link": "", "description": "黄杨山登山活动，珠海第一峰，风景秀丽，适合户外运动爱好者，免费参与。", "category": "体育赛事", "fee": "免费", "contact": "", "family_friendly": True, "source": "黄杨山"},
    {"title": "斗门非遗展示馆水上婚嫁展示", "venue": "斗门非遗展示馆", "start_date": "2026-07-20", "end_date": "2026-08-30", "link": "", "description": "斗门非遗展示馆水上婚嫁展示，了解斗门独特的疍家水上婚嫁民俗文化。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "斗门非遗展示馆"},
    {"title": "斗门区文化馆粤剧表演", "venue": "斗门区文化馆", "start_date": "2026-08-03", "end_date": "2026-08-03", "link": "", "description": "斗门区文化馆粤剧表演活动，本地粤剧团体演出经典曲目，免费观看。", "category": "演出", "fee": "免费", "contact": "", "family_friendly": True, "source": "斗门区文化馆"},
    {"title": "斗门区图书馆亲子阅读会", "venue": "斗门区图书馆", "start_date": "2026-08-10", "end_date": "2026-08-10", "link": "", "description": "斗门区图书馆亲子阅读会，适合3-8岁儿童及家长，分享绘本故事。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "斗门区图书馆"},
    {"title": "斗门区博物馆小小讲解员", "venue": "斗门区博物馆", "start_date": "2026-08-15", "end_date": "2026-08-22", "link": "", "description": "斗门区博物馆小小讲解员培训班，面向中小学生，学习斗门历史和讲解技巧。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "斗门区博物馆"},
    {"title": "斗门旧街美食文化节", "venue": "斗门旧街", "start_date": "2026-08-16", "end_date": "2026-08-18", "link": "", "description": "斗门旧街美食文化节，品尝斗门特色美食，体验骑楼街历史文化氛围。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "斗门旧街"},
    {"title": "金台寺禅修体验", "venue": "金台寺", "start_date": "2026-08-23", "end_date": "2026-08-23", "link": "", "description": "金台寺禅修体验活动，在黄杨山清幽环境中体验禅修文化，需提前报名。", "category": "其他", "fee": "免费", "contact": "", "family_friendly": False, "source": "金台寺"},
    {"title": "御温泉夏日花火大会", "venue": "御温泉", "start_date": "2026-08-24", "end_date": "2026-08-24", "link": "https://www.yuwengquan.com", "description": "御温泉夏日花火大会，日式花火表演结合温泉体验，浪漫夏日夜晚。", "category": "演出", "fee": "收费", "contact": "", "family_friendly": True, "source": "御温泉"},
    {"title": "斗门区文化馆非遗传承展", "venue": "斗门区文化馆", "start_date": "2026-08-25", "end_date": "2026-09-25", "link": "", "description": "斗门区文化馆非遗传承展，展示装泥鱼、水上婚嫁等斗门非遗项目。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "斗门区文化馆"},
    {"title": "斗门体育中心足球邀请赛", "venue": "斗门体育中心", "start_date": "2026-08-29", "end_date": "2026-08-30", "link": "", "description": "斗门体育中心夏季足球邀请赛，各社区和企事业单位队伍参赛，免费观赛。", "category": "体育赛事", "fee": "免费", "contact": "", "family_friendly": True, "source": "斗门体育中心"},
    {"title": "井岸镇文化中心书画展", "venue": "井岸镇文化中心", "start_date": "2026-08-30", "end_date": "2026-09-15", "link": "", "description": "井岸镇文化中心书画作品展，展示本地书画爱好者作品，免费参观。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "井岸镇文化中心"},

    # === 横琴新区活动（20个）===
    {"title": "珠海长隆海洋王国夏日狂欢节", "venue": "珠海长隆海洋王国", "start_date": "2026-07-01", "end_date": "2026-08-31", "link": "https://www.chimelong.com", "description": "长隆海洋王国夏日狂欢节，八大主题园区全面开放，含海洋动物展示、大型演艺和海洋幻彩烟花秀。", "category": "亲子活动", "fee": "收费", "contact": "", "family_friendly": True, "source": "珠海长隆海洋王国"},
    {"title": "长隆海洋幻彩烟花秀", "venue": "珠海长隆海洋王国", "start_date": "2026-07-01", "end_date": "2026-08-31", "link": "https://www.chimelong.com", "description": "每晚海洋幻彩烟花秀，一场令人难忘的烟花盛宴，结合灯光和音乐，绚丽多彩。", "category": "演出", "fee": "收费", "contact": "", "family_friendly": True, "source": "珠海长隆海洋王国"},
    {"title": "长隆飞船乐园宇宙探索之旅", "venue": "珠海长隆飞船乐园", "start_date": "2026-07-01", "end_date": "2026-08-31", "link": "https://www.chimelong.com", "description": "15大主题区域宇宙探索之旅，含宇宙世界、峡谷星球、星际站台、珊瑚秘境等，10:00-18:00。", "category": "亲子活动", "fee": "收费", "contact": "", "family_friendly": True, "source": "珠海长隆飞船乐园"},
    {"title": "长隆横琴剧院《长隆秀》", "venue": "珠海长隆横琴剧院", "start_date": "2026-07-01", "end_date": "2026-08-31", "link": "https://www.chimelong.com", "description": "国际顶尖团队打造的大马戏节目《长隆秀》，俄罗斯马戏世家传人执导，常规开演时间17:00。", "category": "演出", "fee": "收费", "contact": "", "family_friendly": True, "source": "珠海长隆横琴剧院"},
    {"title": "横琴文化艺术中心艺术展览", "venue": "横琴文化艺术中心", "start_date": "2026-07-05", "end_date": "2026-08-30", "link": "", "description": "横琴文化艺术中心夏季艺术展览，含当代艺术、摄影、装置等多种艺术形式，免费参观。", "category": "展览", "fee": "免费", "contact": "", "family_friendly": True, "source": "横琴文化艺术中心"},
    {"title": "横琴国际网球中心WTA超级精英赛", "venue": "横琴国际网球中心", "start_date": "2026-10-20", "end_date": "2026-10-26", "link": "https://www.hengqintennis.com", "description": "WTA超级精英赛在横琴国际网球中心举行，世界顶级女子网球选手参赛，精彩赛事不容错过。", "category": "体育赛事", "fee": "需购票", "contact": "", "family_friendly": True, "source": "横琴国际网球中心"},
    {"title": "星乐度露营小镇夏日露营节", "venue": "星乐度露营小镇", "start_date": "2026-07-10", "end_date": "2026-08-31", "link": "https://www.starryland.cn", "description": "星乐度露营小镇夏日露营节，含房车、木屋、星空露营等住宿体验，亲子户外活动。", "category": "亲子活动", "fee": "收费", "contact": "", "family_friendly": True, "source": "星乐度露营小镇"},
    {"title": "横琴湿地公园自然教育活动", "venue": "横琴湿地公园", "start_date": "2026-07-18", "end_date": "2026-08-18", "link": "", "description": "横琴湿地公园自然教育活动，红树林湿地生态公园，观鸟、赏红树林、自然教育。", "category": "科普活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "横琴湿地公园"},
    {"title": "横琴花海长廊骑行活动", "venue": "横琴花海长廊", "start_date": "2026-07-20", "end_date": "2026-08-31", "link": "", "description": "五公里花海长廊骑行活动，四季花开，适合骑行、散步、拍照，免费参与。", "category": "体育赛事", "fee": "免费", "contact": "", "family_friendly": True, "source": "横琴花海长廊"},
    {"title": "横琴口岸免税购物节", "venue": "横琴口岸", "start_date": "2026-07-15", "end_date": "2026-08-15", "link": "", "description": "横琴口岸免税购物节，连接珠海横琴与澳门的口岸，含免税购物区，24小时通关。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "横琴口岸"},
    {"title": "横琴金融岛夜景游览", "venue": "横琴金融岛", "start_date": "2026-07-01", "end_date": "2026-08-31", "link": "", "description": "横琴金融岛夜景游览，现代建筑景观，海景优美，适合夜游拍照。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "横琴金融岛"},
    {"title": "长隆海洋王国海洋科普讲堂", "venue": "珠海长隆海洋王国", "start_date": "2026-07-25", "end_date": "2026-07-25", "link": "https://www.chimelong.com", "description": "长隆海洋王国海洋科普讲堂，专业讲解员介绍海洋生物知识，适合中小学生参与。", "category": "科普活动", "fee": "收费", "contact": "", "family_friendly": True, "source": "珠海长隆海洋王国"},
    {"title": "长隆飞船乐园亲子科学实验秀", "venue": "珠海长隆飞船乐园", "start_date": "2026-08-01", "end_date": "2026-08-31", "link": "https://www.chimelong.com", "description": "长隆飞船乐园亲子科学实验秀，互动科学实验表演，寓教于乐。", "category": "科普活动", "fee": "收费", "contact": "", "family_friendly": True, "source": "珠海长隆飞船乐园"},
    {"title": "横琴文化艺术中心亲子工作坊", "venue": "横琴文化艺术中心", "start_date": "2026-08-02", "end_date": "2026-08-02", "link": "", "description": "横琴文化艺术中心亲子工作坊，含手工制作、绘画等亲子艺术活动，免费参与。", "category": "亲子活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "横琴文化艺术中心"},
    {"title": "星乐度露营小镇星空观测活动", "venue": "星乐度露营小镇", "start_date": "2026-08-09", "end_date": "2026-08-09", "link": "https://www.starryland.cn", "description": "星乐度露营小镇星空观测活动，专业天文望远镜观测星空，了解天文知识。", "category": "科普活动", "fee": "收费", "contact": "", "family_friendly": True, "source": "星乐度露营小镇"},
    {"title": "横琴湿地公园观鸟活动", "venue": "横琴湿地公园", "start_date": "2026-08-15", "end_date": "2026-08-15", "link": "", "description": "横琴湿地公园观鸟活动，专业导师带领观察红树林湿地鸟类，了解候鸟迁徙知识。", "category": "科普活动", "fee": "免费", "contact": "", "family_friendly": True, "source": "横琴湿地公园"},
    {"title": "长隆横琴剧院国际马戏节", "venue": "珠海长隆横琴剧院", "start_date": "2026-08-20", "end_date": "2026-08-27", "link": "https://www.chimelong.com", "description": "国际马戏节汇聚世界各地顶尖马戏表演团体，精彩纷呈的马戏盛宴。", "category": "演出", "fee": "收费", "contact": "", "family_friendly": True, "source": "珠海长隆横琴剧院"},
    {"title": "横琴花海长廊摄影比赛", "venue": "横琴花海长廊", "start_date": "2026-08-25", "end_date": "2026-09-10", "link": "", "description": "横琴花海长廊摄影比赛，以花海为主题，面向摄影爱好者征集作品，免费参与。", "category": "其他", "fee": "免费", "contact": "", "family_friendly": True, "source": "横琴花海长廊"},
    {"title": "横琴文化艺术中心音乐会", "venue": "横琴文化艺术中心", "start_date": "2026-08-30", "end_date": "2026-08-30", "link": "", "description": "横琴文化艺术中心夏季音乐会，知名乐团演绎经典曲目，免费领票入场。", "category": "演出", "fee": "免费", "contact": "", "family_friendly": True, "source": "横琴文化艺术中心"},
    {"title": "长隆海洋王国万圣节主题活动", "venue": "珠海长隆海洋王国", "start_date": "2026-10-01", "end_date": "2026-10-31", "link": "https://www.chimelong.com", "description": "长隆海洋王国万圣节主题活动，万圣主题装饰、鬼屋体验、夜间巡游等，刺激好玩。", "category": "亲子活动", "fee": "收费", "contact": "", "family_friendly": True, "source": "珠海长隆海洋王国"},
]


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 保存场馆数据
    venue_file = os.path.join(script_dir, 'zhuhai_venues.json')
    with open(venue_file, 'w', encoding='utf-8') as f:
        json.dump(ZHUHAI_VENUES, f, ensure_ascii=False, indent=2)
    print(f"珠海场馆数据已保存: {venue_file} ({len(ZHUHAI_VENUES)} 个场馆)")
    
    # 保存活动数据
    activity_file = os.path.join(script_dir, 'zhuhai_activities.json')
    with open(activity_file, 'w', encoding='utf-8') as f:
        json.dump(ZHUHAI_ACTIVITIES, f, ensure_ascii=False, indent=2)
    print(f"珠海活动数据已保存: {activity_file} ({len(ZHUHAI_ACTIVITIES)} 个活动)")
    
    # 统计
    print(f"\n=== 统计 ===")
    print(f"场馆总数: {len(ZHUHAI_VENUES)}")
    print(f"活动总数: {len(ZHUHAI_ACTIVITIES)}")
    
    districts = {}
    for v in ZHUHAI_VENUES:
        d = v['district']
        districts[d] = districts.get(d, 0) + 1
    print(f"\n场馆分布:")
    for d, n in sorted(districts.items(), key=lambda x: -x[1]):
        print(f"  {d}: {n} 个")
    
    categories = {}
    for a in ZHUHAI_ACTIVITIES:
        c = a['category']
        categories[c] = categories.get(c, 0) + 1
    print(f"\n活动分类:")
    for c, n in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {c}: {n} 个")


if __name__ == '__main__':
    main()
