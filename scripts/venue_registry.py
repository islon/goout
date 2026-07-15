"""统一场馆注册表 — 全局唯一的场馆数据真相源。

所有业务（数据管线、前端、API）都从这里获取场馆信息，不再各自维护映射表。

核心设计：
  1. 每个场馆有唯一 source_code（短代码），作为活动-场馆关联主键
  2. 每个场馆有明确的 district（区县），不再需要关键词推导
  3. 每个场馆有明确的 type（类型），用于场馆指南分类
  4. 提供 lookup_venue(source_code) / lookup_venue_by_name(name) 查询接口
  5. 提供 get_district(source_code) 直接返回区县，无需前端推导

使用方式：
  from venue_registry import lookup_venue, get_district, get_all_venues

  # 查场馆信息
  venue = lookup_venue('pslib')  # → {'name': '坪山区图书馆', 'district': '坪山区', ...}

  # 查区县
  district = get_district('pslib')  # → '坪山区'

  # 获取所有场馆（用于生成 venue_info.json）
  venues = get_all_venues()
"""

import json
import os
import re

# ============================================================
# 场馆注册表 — source_code → 场馆完整定义
# ============================================================
# 字段说明:
#   source_code: 唯一短代码，活动的 source 字段必须用这个值
#   name:        场馆名称
#   city:        城市代码 (shenzhen/guangzhou/shanghai/beijing/hangzhou)
#   district:    区县（深圳: 南山区/福田区/罗湖区/宝安区/龙岗区/龙华区/光明区/坪山区/盐田区/大鹏新区）
#   type:        场馆类型 (博物馆/美术馆/科技馆/图书馆/文化馆/体育中心/青少年宫/演出场馆/公园/科普馆/会展中心/文化中心/其他)
#   address:     地址
#   transport:   交通指引
#   fee:         默认费用
#   description: 场馆描述
#   official_url: 官网
#   highlights:  亮点标签列表
#   aliases:     别名列表（用于模糊匹配，如旧source值、场馆简称等）

VENUES = [
    # ================================================================
    # 深圳市级核心场馆
    # ================================================================
    {
        "source_code": "szlib", "name": "深圳图书馆", "city": "shenzhen", "district": "福田区",
        "type": "图书馆", "address": "福田区福中一路2001号", "transport": "地铁3/4号线少年宫站",
        "fee": "免费", "description": "深圳中心图书馆，含中心馆和北馆，常设阅览、展览、讲座等活动。",
        "official_url": "https://www.szlib.org.cn", "highlights": ["阅读推广", "讲座展览", "暑期缤纷季"],
        "aliases": ["深圳图书馆中心馆", "深圳图书馆北馆", "深圳图书馆（中心馆）", "深圳图书馆（北馆）"],
    },
    {
        "source_code": "sz_children_lib", "name": "深圳少年儿童图书馆", "city": "shenzhen", "district": "福田区",
        "type": "图书馆", "address": "福田区红荔路1011号", "transport": "地铁3号线通新岭站",
        "fee": "免费", "description": "专为少年儿童服务的公共图书馆，定期举办绘本故事会、阅读推广等活动。",
        "official_url": "", "highlights": ["儿童阅读", "绘本故事", "暑期活动"],
        "aliases": ["深圳少儿图书馆"],
    },
    {
        "source_code": "szmuseum", "name": "深圳博物馆", "city": "shenzhen", "district": "福田区",
        "type": "博物馆", "address": "福田区福中路市民中心A区", "transport": "地铁2/4号线市民中心站",
        "fee": "免费", "description": "深圳综合性博物馆，常设古代深圳、近代深圳、深圳民俗等展览。",
        "official_url": "https://www.shenzhenmuseum.com", "highlights": ["深圳历史", "古代深圳", "民俗文化"],
        "aliases": ["深圳博物馆（市民中心馆）", "深圳博物馆（历史民俗馆）", "深圳博物馆官网"],
    },
    {
        "source_code": "szstm", "name": "深圳科学技术馆", "city": "shenzhen", "district": "光明区",
        "type": "科技馆", "address": "光明区光明街道", "transport": "地铁6号线光明站",
        "fee": "免费", "description": "深圳新建科技馆，含互动体验展区、科学实验区等。",
        "official_url": "", "highlights": ["科学实验", "互动体验", "科普教育"],
        "aliases": ["深圳科学技术馆（光明新馆）", "深圳科技馆（光明新馆）", "深圳科技馆（光明馆）", "深圳科学技术馆（光明"],
    },
    {
        "source_code": "szbo", "name": "深圳滨海艺术中心", "city": "shenzhen", "district": "宝安区",
        "type": "演出场馆", "address": "宝安区宝兴路8号", "transport": "地铁5号线宝华站",
        "fee": "收费", "description": "宝安滨海文化公园内的大型演艺中心，定期举办音乐会、音乐剧等演出。",
        "official_url": "", "highlights": ["滨海演艺", "音乐剧", "交响乐"],
        "aliases": ["深圳滨海艺术中心", "宝安滨海文化公园"],
    },
    {
        "source_code": "szconcert", "name": "深圳音乐厅", "city": "shenzhen", "district": "福田区",
        "type": "演出场馆", "address": "福田区福中一路2016号", "transport": "地铁3/4号线少年宫站",
        "fee": "收费", "description": "深圳专业音乐演出场馆，定期举办交响乐、室内乐等音乐会。",
        "official_url": "", "highlights": ["古典音乐", "交响乐"],
        "aliases": [],
    },
    {
        "source_code": "szmocap", "name": "深圳市当代艺术与城市规划馆", "city": "shenzhen", "district": "福田区",
        "type": "美术馆", "address": "福田区福中路184号", "transport": "地铁3/4号线少年宫站",
        "fee": "免费", "description": "集当代艺术展览与城市规划展示于一体的综合性场馆。",
        "official_url": "", "highlights": ["当代艺术", "城市规划"],
        "aliases": ["当代艺术与城市规划馆", "moacup"],
    },
    {
        "source_code": "szsports", "name": "深圳市体育中心", "city": "shenzhen", "district": "福田区",
        "type": "体育中心", "address": "福田区笋岗西路", "transport": "地铁7号线黄木岗站",
        "fee": "收费", "description": "深圳市级体育中心，含体育馆、游泳馆等设施。",
        "official_url": "", "highlights": ["体育赛事", "运动健身"],
        "aliases": ["深圳市体育中心体育馆", "sztyzx"],
    },
    {
        "source_code": "szmassart", "name": "深圳市文化馆", "city": "shenzhen", "district": "福田区",
        "type": "文化馆", "address": "福田区燕南路", "transport": "地铁2号线燕南站",
        "fee": "免费", "description": "深圳市级文化馆，举办各类公益文化活动。",
        "official_url": "", "highlights": ["公益文化", "艺术培训"],
        "aliases": [],
    },
    {
        "source_code": "sznm", "name": "深圳自然博物馆", "city": "shenzhen", "district": "坪山区",
        "type": "博物馆", "address": "坪山区石井街道", "transport": "地铁16号线",
        "fee": "免费", "description": "深圳新建自然博物馆，展示自然历史、生态环境等内容。",
        "official_url": "", "highlights": ["自然科学", "生态环境"],
        "aliases": ["深圳自然博物馆", "ps_nature"],
    },

    # ================================================================
    # 南山区场馆
    # ================================================================
    {
        "source_code": "nslib", "name": "南山图书馆", "city": "shenzhen", "district": "南山区",
        "type": "图书馆", "address": "南山区常兴路176号", "transport": "地铁1号线桃园站",
        "fee": "免费", "description": "南山区公共图书馆，定期举办阅读推广、讲座等活动。",
        "official_url": "", "highlights": ["阅读推广", "社区文化"],
        "aliases": ["南山图书馆", "南山区图书馆"],
    },
    {
        "source_code": "nsmuseum", "name": "南山博物馆", "city": "shenzhen", "district": "南山区",
        "type": "博物馆", "address": "南山区南山大道2093号", "transport": "地铁12号线南头古城站",
        "fee": "免费", "description": "南山区综合性博物馆，常设古代南山、近代南山展览，定期举办特展。",
        "official_url": "", "highlights": ["南山历史", "特色特展"],
        "aliases": ["南山博物馆一层一号展厅", "南山博物馆二层三号展厅", "南山博物馆二层二号展厅", "南山博物馆一层一号专题展厅"],
    },
    {
        "source_code": "nswhg", "name": "南山区文化馆", "city": "shenzhen", "district": "南山区",
        "type": "文化馆", "address": "南山区", "transport": "",
        "fee": "免费", "description": "南山区文化馆，举办公益文化培训、演出等活动。",
        "official_url": "", "highlights": ["公益培训", "群众文化"],
        "aliases": ["南山区文化馆"],
    },
    {
        "source_code": "nsqsng", "name": "南山区青少年活动中心", "city": "shenzhen", "district": "南山区",
        "type": "青少年宫", "address": "南山区", "transport": "",
        "fee": "免费", "description": "南山区青少年校外活动场所，开展各类兴趣培训。",
        "official_url": "", "highlights": ["青少年培训", "兴趣课程"],
        "aliases": ["南山区青少年活动中心"],
    },
    {
        "source_code": "nswtzx", "name": "南山文体中心", "city": "shenzhen", "district": "南山区",
        "type": "文化中心", "address": "南山区南山大道", "transport": "地铁1号线桃园站",
        "fee": "收费", "description": "南山文体中心，含大剧院、聚橙剧院等演出场馆。",
        "official_url": "", "highlights": ["演出", "体育"],
        "aliases": ["南山文体中心大剧院", "南山文体中心聚橙剧院"],
    },
    {
        "source_code": "nsaqjy", "name": "南山安全教育体验馆", "city": "shenzhen", "district": "南山区",
        "type": "科普馆", "address": "南山区", "transport": "",
        "fee": "免费需预约", "description": "安全主题沉浸式体验展，含消防、交通、自然灾害等互动体验区。",
        "official_url": "", "highlights": ["安全教育", "互动体验"],
        "aliases": [],
    },
    {
        "source_code": "skhykpg", "name": "蛇口海洋科普馆", "city": "shenzhen", "district": "南山区",
        "type": "科普馆", "address": "南山区蛇口", "transport": "地铁2号线蛇口港站",
        "fee": "免费", "description": "蛇口海洋科普馆，展示海洋生物标本、珊瑚等。",
        "official_url": "", "highlights": ["海洋生物", "标本展览"],
        "aliases": [],
    },
    {
        "source_code": "sarc", "name": "深爱人才馆", "city": "shenzhen", "district": "南山区",
        "type": "博物馆", "address": "南山区", "transport": "",
        "fee": "免费", "description": "展示深圳人才政策和科技创新成果。",
        "official_url": "", "highlights": ["人才政策", "科技创新"],
        "aliases": [],
    },
    {
        "source_code": "ntgc", "name": "南头古城博物馆群", "city": "shenzhen", "district": "南山区",
        "type": "博物馆", "address": "南山区南山大道3109号", "transport": "地铁12号线南头古城站",
        "fee": "免费", "description": "南头古城内多个主题博物馆群，展示深圳1700年城市历史。",
        "official_url": "", "highlights": ["古城历史", "考古发现"],
        "aliases": ["南头古城"],
    },
    {
        "source_code": "zsjbwg", "name": "招商局历史博物馆", "city": "shenzhen", "district": "南山区",
        "type": "博物馆", "address": "南山区蛇口", "transport": "地铁2号线蛇口港站",
        "fee": "免费", "description": "展示招商局150年发展历程和中国近代航运史。",
        "official_url": "", "highlights": ["招商局历史", "航运史"],
        "aliases": [],
    },
    {
        "source_code": "nssxf", "name": "南山书房", "city": "shenzhen", "district": "南山区",
        "type": "图书馆", "address": "南山区", "transport": "",
        "fee": "免费", "description": "南山区社区阅读空间，提供自助阅览服务。",
        "official_url": "", "highlights": ["社区阅读", "自助阅览"],
        "aliases": [],
    },
    {
        "source_code": "oct_wetland", "name": "华侨城湿地", "city": "shenzhen", "district": "南山区",
        "type": "公园", "address": "南山区白石路", "transport": "地铁1号线侨城东站",
        "fee": "免费需预约", "description": "华侨城湿地公园，开展自然教育、观鸟等亲子活动。",
        "official_url": "", "highlights": ["湿地生态", "观鸟", "自然教育"],
        "aliases": ["华侨城湿地公园", "华侨城创意文化园"],
    },
    {
        "source_code": "szwty", "name": "深圳湾体育中心", "city": "shenzhen", "district": "南山区",
        "type": "体育中心", "address": "南山区滨海大道", "transport": "地铁2号线后海站",
        "fee": "收费", "description": "深圳湾体育中心（春茧），含体育馆、游泳馆等。",
        "official_url": "", "highlights": ["体育赛事", "运动培训"],
        "aliases": [],
    },
    {
        "source_code": "hlgw", "name": "欢乐港湾", "city": "shenzhen", "district": "宝安区",
        "type": "文化中心", "address": "宝安区海天路", "transport": "地铁5号线临海站",
        "fee": "免费", "description": "宝安滨海文化公园，含摩天轮、商业综合体等。",
        "official_url": "", "highlights": ["滨海休闲", "摩天轮"],
        "aliases": ["宝安滨海文化公园"],
    },

    # ================================================================
    # 福田区场馆
    # ================================================================
    {
        "source_code": "ftlib", "name": "福田区图书馆", "city": "shenzhen", "district": "福田区",
        "type": "图书馆", "address": "福田区景田路70号", "transport": "地铁2号线景田站",
        "fee": "免费", "description": "福田区公共图书馆，定期举办阅读推广活动。",
        "official_url": "", "highlights": ["阅读推广", "社区文化"],
        "aliases": [],
    },
    {
        "source_code": "ftwhg", "name": "福田区文化馆", "city": "shenzhen", "district": "福田区",
        "type": "文化馆", "address": "福田区", "transport": "",
        "fee": "免费", "description": "福田区文化馆，举办公益文化培训、演出等活动。",
        "official_url": "", "highlights": ["公益培训", "群众文化"],
        "aliases": ["福田梦工场"],
    },
    {
        "source_code": "ftart", "name": "福田美术馆", "city": "shenzhen", "district": "福田区",
        "type": "美术馆", "address": "福田区", "transport": "",
        "fee": "免费", "description": "福田区美术馆，展示当代艺术和本土艺术家作品。",
        "official_url": "", "highlights": ["当代艺术", "本土艺术"],
        "aliases": ["福田美术馆"],
    },
    {
        "source_code": "lh_paleo", "name": "深圳古生物博物馆", "city": "shenzhen", "district": "罗湖区",
        "type": "博物馆", "address": "罗湖区仙湖植物园内", "transport": "地铁2号线仙湖路站",
        "fee": "免费", "description": "展示恐龙化石、三叶虫等古生物标本，介绍地球生命演化历程。",
        "official_url": "", "highlights": ["古生物化石", "恐龙", "生命演化"],
        "aliases": [],
    },

    # ================================================================
    # 罗湖区场馆
    # ================================================================
    {
        "source_code": "lhlib", "name": "罗湖区图书馆", "city": "shenzhen", "district": "罗湖区",
        "type": "图书馆", "address": "罗湖区怡景路1014号", "transport": "地铁5号线怡景站",
        "fee": "免费", "description": "罗湖区公共图书馆，定期举办阅读推广活动。",
        "official_url": "", "highlights": ["阅读推广", "社区文化"],
        "aliases": [],
    },
    {
        "source_code": "lhwhg2", "name": "罗湖区文化馆", "city": "shenzhen", "district": "罗湖区",
        "type": "文化馆", "address": "罗湖区", "transport": "",
        "fee": "免费", "description": "罗湖区文化馆，举办公益文化培训、演出等活动。",
        "official_url": "", "highlights": ["公益培训", "群众文化"],
        "aliases": [],
    },
    {
        "source_code": "lhtheatre", "name": "深圳戏院", "city": "shenzhen", "district": "罗湖区",
        "type": "演出场馆", "address": "罗湖区新园路1号", "transport": "地铁1/3号线老街站F出口",
        "fee": "需购票", "description": "深圳老牌演出场馆，定期举办京剧、儿童剧等演出。",
        "official_url": "", "highlights": ["京剧", "儿童剧", "少儿演出季"],
        "aliases": [],
    },
    {
        "source_code": "szdjy", "name": "深圳大剧院", "city": "shenzhen", "district": "罗湖区",
        "type": "演出场馆", "address": "罗湖区深南东路5018号", "transport": "地铁1/2号线大剧院站",
        "fee": "需购票", "description": "深圳大剧院，举办音乐会、歌剧、芭蕾等高端演出。",
        "official_url": "", "highlights": ["交响乐", "歌剧", "芭蕾"],
        "aliases": [],
    },

    # ================================================================
    # 宝安区场馆
    # ================================================================
    {
        "source_code": "balib", "name": "宝安图书馆", "city": "shenzhen", "district": "宝安区",
        "type": "图书馆", "address": "宝安区宝兴路1号", "transport": "地铁5号线宝华站",
        "fee": "免费", "description": "宝安区公共图书馆，含总馆和多个街道分馆。",
        "official_url": "", "highlights": ["阅读推广", "社区文化"],
        "aliases": ["宝安图书馆", "宝安区图书馆", "宝安图书馆（宝安1990分馆）"],
    },
    {
        "source_code": "bamuseum", "name": "宝安区博物馆", "city": "shenzhen", "district": "宝安区",
        "type": "博物馆", "address": "宝安区", "transport": "",
        "fee": "免费", "description": "宝安区博物馆，展示宝安历史文化。",
        "official_url": "", "highlights": ["宝安历史", "地方文化"],
        "aliases": [],
    },
    {
        "source_code": "baoan_1990", "name": "宝安1990文化馆", "city": "shenzhen", "district": "宝安区",
        "type": "文化馆", "address": "宝安区", "transport": "",
        "fee": "免费", "description": "宝安1990文化馆，含文化馆、博物馆、美术馆。",
        "official_url": "", "highlights": ["公益培训", "展览"],
        "aliases": ["宝安1990（文化馆博物馆美术馆）"],
    },
    {
        "source_code": "baoan_kjg", "name": "宝安科技馆", "city": "shenzhen", "district": "宝安区",
        "type": "科技馆", "address": "宝安区", "transport": "",
        "fee": "免费", "description": "宝安区科技馆，含互动体验展区。",
        "official_url": "", "highlights": ["科学实验", "互动体验"],
        "aliases": [],
    },
    {
        "source_code": "baoan_ty", "name": "宝安体育中心", "city": "shenzhen", "district": "宝安区",
        "type": "体育中心", "address": "宝安区", "transport": "",
        "fee": "收费", "description": "宝安区体育中心，含体育馆、游泳馆等。",
        "official_url": "", "highlights": ["体育赛事", "运动培训"],
        "aliases": ["宝安体育中心体育馆"],
    },
    {
        "source_code": "baoan_qsng", "name": "宝安区青少年宫", "city": "shenzhen", "district": "宝安区",
        "type": "青少年宫", "address": "宝安区", "transport": "",
        "fee": "免费", "description": "宝安区青少年校外活动场所。",
        "official_url": "", "highlights": ["青少年培训", "兴趣课程"],
        "aliases": [],
    },
    {
        "source_code": "baoan_guihua", "name": "宝安城市规划展览馆", "city": "shenzhen", "district": "宝安区",
        "type": "博物馆", "address": "宝安区", "transport": "",
        "fee": "免费", "description": "展示宝安区城市规划建设成就。",
        "official_url": "", "highlights": ["城市规划", "建设成就"],
        "aliases": [],
    },
    {
        "source_code": "bayarea_eye", "name": "湾区之眼", "city": "shenzhen", "district": "宝安区",
        "type": "文化中心", "address": "宝安区", "transport": "",
        "fee": "免费", "description": "湾区文化综合体，含图书馆、展览等。",
        "official_url": "", "highlights": ["文化综合体", "阅读空间"],
        "aliases": [],
    },

    # ================================================================
    # 龙岗区场馆
    # ================================================================
    {
        "source_code": "lglib", "name": "龙岗区图书馆", "city": "shenzhen", "district": "龙岗区",
        "type": "图书馆", "address": "龙岗区中心城", "transport": "地铁3号线龙城广场站",
        "fee": "免费", "description": "龙岗区公共图书馆，定期举办阅读推广活动。",
        "official_url": "", "highlights": ["阅读推广", "社区文化"],
        "aliases": [],
    },
    {
        "source_code": "lgmuseum", "name": "龙岗区博物馆", "city": "shenzhen", "district": "龙岗区",
        "type": "博物馆", "address": "龙岗区", "transport": "",
        "fee": "免费", "description": "龙岗区博物馆，展示龙岗历史文化。",
        "official_url": "", "highlights": ["龙岗历史", "地方文化"],
        "aliases": ["龙岗文博展览馆"],
    },
    {
        "source_code": "lgwhg", "name": "龙岗区文化馆", "city": "shenzhen", "district": "龙岗区",
        "type": "文化馆", "address": "龙岗区", "transport": "",
        "fee": "免费", "description": "龙岗区文化馆，举办公益文化培训、演出等活动。",
        "official_url": "", "highlights": ["公益培训", "群众文化"],
        "aliases": [],
    },
    {
        "source_code": "lgqsng", "name": "龙岗区青少年宫", "city": "shenzhen", "district": "龙岗区",
        "type": "青少年宫", "address": "龙岗区", "transport": "",
        "fee": "免费", "description": "龙岗区青少年校外活动场所。",
        "official_url": "", "highlights": ["青少年培训", "兴趣课程"],
        "aliases": [],
    },
    {
        "source_code": "lg_hakka", "name": "龙岗客家民俗博物馆", "city": "shenzhen", "district": "龙岗区",
        "type": "博物馆", "address": "龙岗区龙岗街道鹤湖新居", "transport": "地铁3号线南联站",
        "fee": "免费", "description": "全国最大的客家围屋之一，展示客家迁徙历史和民俗文化。",
        "official_url": "", "highlights": ["客家文化", "鹤湖新居", "民俗文物"],
        "aliases": ["龙岗客家民俗博物馆（鹤湖新居）"],
    },
    {
        "source_code": "lgtyzx", "name": "龙岗体育中心", "city": "shenzhen", "district": "龙岗区",
        "type": "体育中心", "address": "龙岗区", "transport": "",
        "fee": "收费", "description": "龙岗区体育中心。",
        "official_url": "", "highlights": ["体育赛事", "运动培训"],
        "aliases": [],
    },
    {
        "source_code": "lg_arts", "name": "深圳龙岗国际艺术中心", "city": "shenzhen", "district": "龙岗区",
        "type": "演出场馆", "address": "龙岗区", "transport": "",
        "fee": "收费", "description": "龙岗区国际艺术中心，举办高端演出。",
        "official_url": "", "highlights": ["国际演出", "艺术交流"],
        "aliases": ["深圳龙岗国际艺术中心"],
    },
    {
        "source_code": "lgkjg", "name": "龙岗区科技馆", "city": "shenzhen", "district": "龙岗区",
        "type": "科技馆", "address": "龙岗区", "transport": "",
        "fee": "免费", "description": "龙岗区科技馆（红立方）。",
        "official_url": "", "highlights": ["科学实验", "互动体验"],
        "aliases": ["龙岗红立方科技馆"],
    },
    {
        "source_code": "lgpark", "name": "龙岗儿童公园", "city": "shenzhen", "district": "龙岗区",
        "type": "公园", "address": "龙岗区", "transport": "",
        "fee": "免费", "description": "龙岗区儿童主题公园，适合亲子游玩。",
        "official_url": "", "highlights": ["亲子游乐", "无动力乐园"],
        "aliases": ["龙岗儿童公园"],
    },

    # ================================================================
    # 龙华区场馆
    # ================================================================
    {
        "source_code": "lhxqlib", "name": "龙华区图书馆", "city": "shenzhen", "district": "龙华区",
        "type": "图书馆", "address": "龙华区", "transport": "地铁4号线",
        "fee": "免费", "description": "龙华区公共图书馆，定期举办阅读推广活动。",
        "official_url": "", "highlights": ["阅读推广", "社区文化"],
        "aliases": [],
    },
    {
        "source_code": "lhqsng", "name": "龙华区青少年宫", "city": "shenzhen", "district": "龙华区",
        "type": "青少年宫", "address": "龙华区", "transport": "",
        "fee": "免费", "description": "龙华区青少年校外活动场所。",
        "official_url": "", "highlights": ["青少年培训", "兴趣课程"],
        "aliases": [],
    },
    {
        "source_code": "lhwhg", "name": "龙华区文化馆", "city": "shenzhen", "district": "龙华区",
        "type": "文化馆", "address": "龙华区", "transport": "",
        "fee": "免费", "description": "龙华区文化馆，举办公益文化培训、演出等活动。",
        "official_url": "", "highlights": ["公益培训", "群众文化"],
        "aliases": ["龙华文体中心"],
    },
    {
        "source_code": "lh_printmaking", "name": "中国版画博物馆", "city": "shenzhen", "district": "龙华区",
        "type": "美术馆", "address": "龙华区观澜街道", "transport": "地铁4号线牛湖站",
        "fee": "免费需预约", "description": "全国首个专业版画博物馆，紧邻观澜版画村。",
        "official_url": "", "highlights": ["版画艺术", "国际馆藏", "观澜版画村"],
        "aliases": [],
    },
    {
        "source_code": "lh_ecology", "name": "龙华生态文明展览馆", "city": "shenzhen", "district": "龙华区",
        "type": "科普馆", "address": "龙华区", "transport": "",
        "fee": "免费", "description": "展示龙华区生态文明建设成果。",
        "official_url": "", "highlights": ["生态文明", "环保科技"],
        "aliases": [],
    },
    {
        "source_code": "lhkjg", "name": "龙华区科技馆", "city": "shenzhen", "district": "龙华区",
        "type": "科技馆", "address": "龙华区", "transport": "",
        "fee": "免费", "description": "龙华区科技馆。",
        "official_url": "", "highlights": ["科学实验", "互动体验"],
        "aliases": ["龙华科技馆"],
    },
    {
        "source_code": "lhbljng", "name": "龙华白石龙纪念馆", "city": "shenzhen", "district": "龙华区",
        "type": "博物馆", "address": "龙华区", "transport": "",
        "fee": "免费", "description": "龙华白石龙中国文化名人大营救纪念馆。",
        "official_url": "", "highlights": ["红色文化", "历史纪念"],
        "aliases": ["龙华白石龙纪念馆"],
    },

    # ================================================================
    # 光明区场馆
    # ================================================================
    {
        "source_code": "gmlib", "name": "光明区图书馆", "city": "shenzhen", "district": "光明区",
        "type": "图书馆", "address": "光明区", "transport": "地铁6号线",
        "fee": "免费", "description": "光明区公共图书馆，定期举办阅读推广活动。",
        "official_url": "", "highlights": ["阅读推广", "社区文化"],
        "aliases": ["gm_lib"],
    },
    {
        "source_code": "gm_kjg", "name": "光明区科技馆", "city": "shenzhen", "district": "光明区",
        "type": "科技馆", "address": "光明区", "transport": "",
        "fee": "免费需预约", "description": "光明区科技馆，含互动科技体验展。",
        "official_url": "", "highlights": ["科学实验", "互动体验"],
        "aliases": [],
    },
    {
        "source_code": "gmwhg", "name": "光明区文化馆", "city": "shenzhen", "district": "光明区",
        "type": "文化馆", "address": "光明区", "transport": "",
        "fee": "免费", "description": "光明区文化馆。",
        "official_url": "", "highlights": ["公益培训", "群众文化"],
        "aliases": [],
    },
    {
        "source_code": "gmarts", "name": "光明文化艺术中心", "city": "shenzhen", "district": "光明区",
        "type": "文化中心", "address": "光明区", "transport": "地铁6号线",
        "fee": "收费", "description": "光明文化艺术中心，含大剧场、音乐厅、美术馆。",
        "official_url": "", "highlights": ["演出", "展览", "艺术"],
        "aliases": ["光明文化艺术中心·演艺中心·大剧场", "光明文化艺术中心·演艺中心·音乐厅", "光明文化艺术中心美术馆"],
    },
    {
        "source_code": "gmqsng", "name": "光明区青少年活动中心", "city": "shenzhen", "district": "光明区",
        "type": "青少年宫", "address": "光明区", "transport": "",
        "fee": "免费", "description": "光明区青少年校外活动场所。",
        "official_url": "", "highlights": ["青少年培训", "兴趣课程"],
        "aliases": [],
    },
    {
        "source_code": "gmtyzx", "name": "光明区群众体育中心", "city": "shenzhen", "district": "光明区",
        "type": "体育中心", "address": "光明区", "transport": "",
        "fee": "收费", "description": "光明区群众体育中心。",
        "official_url": "", "highlights": ["体育赛事", "运动培训"],
        "aliases": [],
    },
    {
        "source_code": "gmhbgy", "name": "光明虹桥公园", "city": "shenzhen", "district": "光明区",
        "type": "公园", "address": "光明区", "transport": "",
        "fee": "免费", "description": "光明区虹桥公园，以红色空中廊桥著称。",
        "official_url": "", "highlights": ["虹桥步道", "休闲健身"],
        "aliases": ["光明虹桥公园"],
    },
    {
        "source_code": "gmtysq", "name": "玉塘文体中心", "city": "shenzhen", "district": "光明区",
        "type": "文化中心", "address": "光明区玉塘街道", "transport": "",
        "fee": "免费", "description": "光明区玉塘街道文体中心。",
        "official_url": "", "highlights": ["社区文化", "体育"],
        "aliases": ["玉塘文体中心"],
    },

    # ================================================================
    # 坪山区场馆
    # ================================================================
    {
        "source_code": "pslib", "name": "坪山区图书馆", "city": "shenzhen", "district": "坪山区",
        "type": "图书馆", "address": "坪山区坪山街道", "transport": "地铁16号线",
        "fee": "免费", "description": "坪山区公共图书馆，定期举办阅读推广、暑期活动等。",
        "official_url": "", "highlights": ["阅读推广", "暑期活动", "亲子活动"],
        "aliases": ["坪山区图书馆官网", "坪山城市书房"],
    },
    {
        "source_code": "psart", "name": "坪山美术馆", "city": "shenzhen", "district": "坪山区",
        "type": "美术馆", "address": "坪山区", "transport": "",
        "fee": "免费", "description": "坪山美术馆，展示当代艺术作品。",
        "official_url": "", "highlights": ["当代艺术", "湾区艺术"],
        "aliases": ["坪山美术馆"],
    },
    {
        "source_code": "psthtr", "name": "坪山大剧院", "city": "shenzhen", "district": "坪山区",
        "type": "演出场馆", "address": "坪山区", "transport": "地铁16号线",
        "fee": "收费", "description": "坪山大剧院，举办舞剧、音乐剧、儿童剧等演出。",
        "official_url": "", "highlights": ["舞剧", "音乐剧", "儿童剧"],
        "aliases": ["坪山大剧院"],
    },
    {
        "source_code": "pskjg", "name": "坪山区科技馆", "city": "shenzhen", "district": "坪山区",
        "type": "科技馆", "address": "坪山区", "transport": "",
        "fee": "免费需预约", "description": "坪山区科技馆，含科普体验区。",
        "official_url": "", "highlights": ["科普教育", "互动体验"],
        "aliases": ["坪山区科技馆"],
    },
    {
        "source_code": "pstyzx", "name": "坪山体育中心", "city": "shenzhen", "district": "坪山区",
        "type": "体育中心", "address": "坪山区", "transport": "",
        "fee": "收费", "description": "坪山区体育中心。",
        "official_url": "", "highlights": ["体育赛事", "运动培训"],
        "aliases": ["坪山区体育中心"],
    },
    {
        "source_code": "psdjng", "name": "坪山东江纵队纪念馆", "city": "shenzhen", "district": "坪山区",
        "type": "博物馆", "address": "坪山区", "transport": "",
        "fee": "免费", "description": "展示东江纵队抗战历史。",
        "official_url": "", "highlights": ["红色文化", "抗战历史"],
        "aliases": ["坪山东江纵队纪念馆"],
    },
    {
        "source_code": "pszxgy", "name": "坪山中心公园", "city": "shenzhen", "district": "坪山区",
        "type": "公园", "address": "坪山区", "transport": "",
        "fee": "免费", "description": "坪山中心公园，含环湖步道、无动力乐园。",
        "official_url": "", "highlights": ["环湖步道", "无动力乐园", "亲子"],
        "aliases": ["坪山中心公园"],
    },
    {
        "source_code": "mlsgy", "name": "马峦山郊野公园", "city": "shenzhen", "district": "坪山区",
        "type": "公园", "address": "坪山区马峦山", "transport": "",
        "fee": "免费", "description": "马峦山郊野公园，可观瀑布、探访客家古村落。",
        "official_url": "", "highlights": ["徒步", "瀑布", "客家村落"],
        "aliases": ["马峦山郊野公园"],
    },
    {
        "source_code": "jlsgy", "name": "聚龙山生态公园", "city": "shenzhen", "district": "坪山区",
        "type": "公园", "address": "坪山区聚龙山", "transport": "",
        "fee": "免费需预约", "description": "聚龙山生态公园，定期开展自然课堂。",
        "official_url": "", "highlights": ["自然教育", "植物识别", "昆虫观察"],
        "aliases": ["聚龙山生态公园"],
    },
    {
        "source_code": "yhzgz", "name": "燕子湖国际会展中心", "city": "shenzhen", "district": "坪山区",
        "type": "会展中心", "address": "坪山区燕子湖", "transport": "",
        "fee": "免费", "description": "坪山燕子湖国际会展中心，承办各类博览会。",
        "official_url": "", "highlights": ["会展", "博览"],
        "aliases": ["燕子湖国际会展中心"],
    },

    # ================================================================
    # 盐田区场馆
    # ================================================================
    {
        "source_code": "ytlib", "name": "盐田区图书馆", "city": "shenzhen", "district": "盐田区",
        "type": "图书馆", "address": "盐田区", "transport": "地铁8号线",
        "fee": "免费", "description": "盐田区公共图书馆，定期举办海洋主题阅读推广活动。",
        "official_url": "", "highlights": ["阅读推广", "海洋主题"],
        "aliases": ["yt_lib"],
    },
    {
        "source_code": "ytwhg", "name": "盐田区文化馆", "city": "shenzhen", "district": "盐田区",
        "type": "文化馆", "address": "盐田区", "transport": "",
        "fee": "免费", "description": "盐田区文化馆。",
        "official_url": "", "highlights": ["公益培训", "群众文化"],
        "aliases": [],
    },
    {
        "source_code": "yt_history", "name": "中英街历史博物馆", "city": "shenzhen", "district": "盐田区",
        "type": "博物馆", "address": "盐田区沙头角中英街", "transport": "地铁8号线沙头角站",
        "fee": "免费", "description": "展示中英街百年沧桑历史和深港边境文化。",
        "official_url": "", "highlights": ["中英街历史", "深港文化"],
        "aliases": [],
    },
    {
        "source_code": "ytkjg", "name": "盐田科技馆", "city": "shenzhen", "district": "盐田区",
        "type": "科技馆", "address": "盐田区", "transport": "",
        "fee": "免费", "description": "盐田区科技馆。",
        "official_url": "", "highlights": ["科学实验", "互动体验"],
        "aliases": ["盐田科技馆"],
    },
    {
        "source_code": "yttyzx", "name": "盐田体育中心", "city": "shenzhen", "district": "盐田区",
        "type": "体育中心", "address": "盐田区", "transport": "",
        "fee": "收费", "description": "盐田区体育中心。",
        "official_url": "", "highlights": ["体育赛事", "运动培训"],
        "aliases": [],
    },
    {
        "source_code": "ytzgy", "name": "盐田中央公园", "city": "shenzhen", "district": "盐田区",
        "type": "公园", "address": "盐田区", "transport": "",
        "fee": "免费", "description": "盐田中央公园。",
        "official_url": "", "highlights": ["休闲散步"],
        "aliases": ["盐田中央公园"],
    },

    # ================================================================
    # 大鹏新区场馆
    # ================================================================
    {
        "source_code": "dpgeopark", "name": "大鹏地质公园博物馆", "city": "shenzhen", "district": "大鹏新区",
        "type": "博物馆", "address": "大鹏新区南澳街道地质公园路7号", "transport": "",
        "fee": "免费", "description": "大鹏半岛国家地质公园博物馆，展示地质演化和古生物化石。",
        "official_url": "", "highlights": ["地质科普", "古生物化石", "火山岩"],
        "aliases": ["dp_geopark", "大鹏半岛国家地质公园博物馆", "大鹏地质公园博物馆"],
    },
    {
        "source_code": "dp_nuclear", "name": "大亚湾核能科技馆", "city": "shenzhen", "district": "大鹏新区",
        "type": "科普馆", "address": "大鹏新区大亚湾核电基地", "transport": "",
        "fee": "免费需预约", "description": "大亚湾核能科技馆，展示核能发电原理和核安全知识。",
        "official_url": "", "highlights": ["核能科普", "清洁能源", "核安全"],
        "aliases": [],
    },
    {
        "source_code": "dplib", "name": "大鹏新区图书馆", "city": "shenzhen", "district": "大鹏新区",
        "type": "图书馆", "address": "大鹏新区大鹏街道", "transport": "",
        "fee": "免费", "description": "大鹏新区公共图书馆，定期举办海洋主题阅读推广活动。",
        "official_url": "", "highlights": ["阅读推广", "海洋主题"],
        "aliases": ["大鹏新区图书馆官网"],
    },
    {
        "source_code": "dpgcbwg", "name": "大鹏古城博物馆", "city": "shenzhen", "district": "大鹏新区",
        "type": "博物馆", "address": "大鹏新区大鹏街道", "transport": "",
        "fee": "免费", "description": "大鹏所城历史博物馆，展示海防文化。",
        "official_url": "", "highlights": ["古城历史", "海防文化"],
        "aliases": ["大鹏古城博物馆"],
    },
    {
        "source_code": "dpwhg", "name": "大鹏新区文化馆", "city": "shenzhen", "district": "大鹏新区",
        "type": "文化馆", "address": "大鹏新区大鹏街道", "transport": "",
        "fee": "免费", "description": "大鹏新区文化馆。",
        "official_url": "", "highlights": ["公益培训", "群众文化"],
        "aliases": [],
    },
    {
        "source_code": "xcart", "name": "深圳西涌天文台", "city": "shenzhen", "district": "大鹏新区",
        "type": "科普馆", "address": "大鹏新区南澳西涌", "transport": "",
        "fee": "免费需预约", "description": "深圳西涌天文台，定期对公众开放，可观星。",
        "official_url": "", "highlights": ["天文观测", "科普教育", "观星"],
        "aliases": ["深圳西涌天文台"],
    },
    {
        "source_code": "dchss", "name": "东涌红树林湿地公园", "city": "shenzhen", "district": "大鹏新区",
        "type": "公园", "address": "大鹏新区南澳东涌", "transport": "",
        "fee": "免费", "description": "东涌红树林湿地公园，开展红树林生态科普、观鸟等自然教育。",
        "official_url": "", "highlights": ["红树林", "观鸟", "自然教育"],
        "aliases": ["东涌红树林湿地公园"],
    },
    {
        "source_code": "bghsl", "name": "坝光红树林湿地公园", "city": "shenzhen", "district": "大鹏新区",
        "type": "公园", "address": "大鹏新区葵涌坝光", "transport": "",
        "fee": "免费", "description": "深圳面积最大的红树林保护区，有观鸟平台和科普栈道。",
        "official_url": "", "highlights": ["红树林", "观鸟", "生态保护"],
        "aliases": ["坝光红树林湿地公园"],
    },
    {
        "source_code": "mgha", "name": "玫瑰海岸", "city": "shenzhen", "district": "大鹏新区",
        "type": "公园", "address": "大鹏新区溪涌玫瑰海岸", "transport": "",
        "fee": "收费", "description": "玫瑰海岸滨海度假区，举办沙滩嘉年华等活动。",
        "official_url": "", "highlights": ["沙滩", "水上运动", "滨海度假"],
        "aliases": ["玫瑰海岸"],
    },
    {
        "source_code": "ymk", "name": "杨梅坑", "city": "shenzhen", "district": "大鹏新区",
        "type": "公园", "address": "大鹏新区南澳杨梅坑", "transport": "",
        "fee": "免费", "description": "杨梅坑海滨栈道，可徒步、骑行、探访鹿嘴山庄。",
        "official_url": "", "highlights": ["滨海徒步", "骑行", "海景"],
        "aliases": ["杨梅坑"],
    },
    {
        "source_code": "qns", "name": "七娘山", "city": "shenzhen", "district": "大鹏新区",
        "type": "公园", "address": "大鹏新区南澳七娘山", "transport": "",
        "fee": "免费", "description": "深圳第二高峰，登山步道沿途有地质科普解说牌。",
        "official_url": "", "highlights": ["登山", "地质科普", "海景"],
        "aliases": ["七娘山"],
    },
    {
        "source_code": "ghysq", "name": "官湖村艺象艺术区", "city": "shenzhen", "district": "大鹏新区",
        "type": "文化中心", "address": "大鹏新区葵涌官湖村", "transport": "",
        "fee": "免费", "description": "官湖村国际艺术园区，含海边画廊、儿童艺术工坊。",
        "official_url": "", "highlights": ["艺术园区", "海边画廊", "亲子工坊"],
        "aliases": ["官湖村艺象艺术区"],
    },
    {
        "source_code": "jsgjly", "name": "金沙湾国际乐园", "city": "shenzhen", "district": "大鹏新区",
        "type": "公园", "address": "大鹏新区金沙湾", "transport": "",
        "fee": "收费", "description": "金沙湾国际乐园，含水世界、冰雪世界等多个主题园区。",
        "official_url": "", "highlights": ["水世界", "冰雪世界", "亲子乐园"],
        "aliases": ["金沙湾国际乐园"],
    },
    {
        "source_code": "dpkjg", "name": "大鹏新区科学馆", "city": "shenzhen", "district": "大鹏新区",
        "type": "科技馆", "address": "大鹏新区", "transport": "",
        "fee": "免费需预约", "description": "大鹏新区科学馆，开展海洋科学、天文观测等科普活动。",
        "official_url": "", "highlights": ["海洋科学", "天文观测", "科普"],
        "aliases": ["大鹏新区科学馆"],
    },
    {
        "source_code": "jcw", "name": "大鹏较场尾沙滩", "city": "shenzhen", "district": "大鹏新区",
        "type": "公园", "address": "大鹏新区大鹏街道较场尾", "transport": "",
        "fee": "免费", "description": "较场尾滨海度假村，有沙滩、民宿、海鲜等。",
        "official_url": "", "highlights": ["沙滩", "民宿", "滨海度假"],
        "aliases": ["大鹏较场尾沙滩", "大鹏较场尾"],
    },
    {
        "source_code": "kcsigy", "name": "葵涌生态公园", "city": "shenzhen", "district": "大鹏新区",
        "type": "公园", "address": "大鹏新区葵涌", "transport": "",
        "fee": "免费", "description": "葵涌生态公园。",
        "official_url": "", "highlights": ["生态", "休闲"],
        "aliases": ["葵涌生态公园"],
    },

    # ================================================================
    # 深圳安全教育
    # ================================================================
    {
        "source_code": "sz_safety", "name": "深圳市安全教育基地", "city": "shenzhen", "district": "福田区",
        "type": "科普馆", "address": "福田区", "transport": "",
        "fee": "免费需预约", "description": "深圳市安全教育基地，含交通安全、消防安全等主题体验区。",
        "official_url": "", "highlights": ["安全教育", "互动体验"],
        "aliases": [],
    },

    # ================================================================
    # 深圳其他场馆
    # ================================================================
    {
        "source_code": "opower", "name": "OPOWER文化艺术中心", "city": "shenzhen", "district": "南山区",
        "type": "文化中心", "address": "南山区华侨城", "transport": "地铁1号线侨城东站",
        "fee": "免费", "description": "华侨城片区文化艺术综合体，集展览、市集、创意零售于一体。",
        "official_url": "", "highlights": ["文艺市集", "创意展览"],
        "aliases": [],
    },
    {
        "source_code": "psqsng", "name": "坪山区青少年宫", "city": "shenzhen", "district": "坪山区",
        "type": "青少年宫", "address": "坪山区", "transport": "",
        "fee": "免费", "description": "坪山区青少年校外活动场所。",
        "official_url": "", "highlights": ["青少年培训", "兴趣课程"],
        "aliases": [],
    },

    # ================================================================
    # 广州场馆
    # ================================================================
    {
        "source_code": "gdmuseum", "name": "广东省博物馆", "city": "guangzhou", "district": "天河区",
        "type": "博物馆", "address": "天河区珠江东路2号", "transport": "地铁3/APM线大剧院站",
        "fee": "免费", "description": "广东省综合性博物馆。",
        "official_url": "", "highlights": ["广东历史", "自然资源"],
        "aliases": [],
    },
    {
        "source_code": "gzmuseum", "name": "广州博物馆", "city": "guangzhou", "district": "越秀区",
        "type": "博物馆", "address": "越秀区镇海路", "transport": "地铁2号线越秀公园站",
        "fee": "收费", "description": "广州博物馆（镇海楼）。",
        "official_url": "", "highlights": ["广州历史"],
        "aliases": [],
    },
    {
        "source_code": "gzlib", "name": "广州图书馆", "city": "guangzhou", "district": "天河区",
        "type": "图书馆", "address": "天河区珠江东路4号", "transport": "地铁3/APM线大剧院站",
        "fee": "免费", "description": "广州图书馆。",
        "official_url": "", "highlights": ["阅读推广"],
        "aliases": [],
    },

    # ================================================================
    # 上海场馆
    # ================================================================
    {
        "source_code": "shanghaimuseum", "name": "上海博物馆", "city": "shanghai", "district": "黄浦区",
        "type": "博物馆", "address": "黄浦区人民大道201号", "transport": "地铁1/2/8号线人民广场站",
        "fee": "免费", "description": "上海博物馆。",
        "official_url": "", "highlights": ["中国古代艺术"],
        "aliases": [],
    },
    {
        "source_code": "shstm", "name": "上海科技馆", "city": "shanghai", "district": "浦东新区",
        "type": "科技馆", "address": "浦东新区世纪大道2000号", "transport": "地铁2号线上海科技馆站",
        "fee": "收费", "description": "上海科技馆。",
        "official_url": "", "highlights": ["科学实验", "互动体验"],
        "aliases": [],
    },

    # ================================================================
    # 北京场馆
    # ================================================================
    {
        "source_code": "chnmuseum", "name": "中国国家博物馆", "city": "beijing", "district": "东城区",
        "type": "博物馆", "address": "东城区东长安街16号", "transport": "地铁1号线天安门东站",
        "fee": "免费", "description": "中国国家博物馆。",
        "official_url": "", "highlights": ["国家历史", "古代文物"],
        "aliases": [],
    },
    {
        "source_code": "gugong", "name": "故宫博物院", "city": "beijing", "district": "东城区",
        "type": "博物馆", "address": "东城区景山前街4号", "transport": "地铁1号线天安门东站",
        "fee": "收费", "description": "故宫博物院。",
        "official_url": "", "highlights": ["明清宫廷", "古代文物"],
        "aliases": [],
    },

    # ================================================================
    # 深圳补充场馆（市级 + 各区街道级）
    # ================================================================
    {
        "source_code": "hxngallery", "name": "何香凝美术馆", "city": "shenzhen", "district": "南山区",
        "type": "美术馆", "address": "南山区深南大道9013号", "transport": "地铁1号线华侨城站",
        "fee": "免费", "description": "何香凝美术馆，展示何香凝书画作品及当代艺术。",
        "official_url": "", "highlights": ["何香凝书画", "当代艺术"],
        "aliases": ["何香凝美术馆"],
    },
    {
        "source_code": "gsyart", "name": "关山月美术馆", "city": "shenzhen", "district": "福田区",
        "type": "美术馆", "address": "福田区红荔路6026号", "transport": "地铁3/4号线少年宫站",
        "fee": "免费", "description": "关山月美术馆，展示关山月画作及当代美术。",
        "official_url": "", "highlights": ["关山月画作", "当代美术"],
        "aliases": ["关山月美术馆"],
    },
    {
        "source_code": "szartm", "name": "深圳美术馆", "city": "shenzhen", "district": "罗湖区",
        "type": "美术馆", "address": "罗湖区爱国路东湖公园内", "transport": "地铁5号线太安站",
        "fee": "免费", "description": "深圳美术馆，展示当代艺术和本土艺术家作品。",
        "official_url": "", "highlights": ["当代艺术", "本土艺术"],
        "aliases": ["深圳美术馆（新馆）", "深圳美术馆官网"],
    },
    {
        "source_code": "polytheatre", "name": "深圳保利剧院", "city": "shenzhen", "district": "南山区",
        "type": "演出场馆", "address": "南山区后海滨路", "transport": "地铁2号线后海站",
        "fee": "需购票", "description": "深圳保利剧院，举办音乐会、音乐剧等演出。",
        "official_url": "", "highlights": ["音乐会", "音乐剧"],
        "aliases": ["深圳保利剧院"],
    },
    {
        "source_code": "szcec", "name": "深圳会展中心", "city": "shenzhen", "district": "福田区",
        "type": "会展中心", "address": "福田区福华三路", "transport": "地铁1/4号线会展中心站",
        "fee": "免费", "description": "深圳会展中心，承办各类大型展览和博览会。",
        "official_url": "", "highlights": ["展览", "博览"],
        "aliases": [],
    },
    {
        "source_code": "shenzhen_world", "name": "深圳国际会展中心", "city": "shenzhen", "district": "宝安区",
        "type": "会展中心", "address": "宝安区福海街道", "transport": "地铁12号线国展站",
        "fee": "免费", "description": "深圳国际会展中心（新馆），承办大型国际展览。",
        "official_url": "", "highlights": ["国际展览", "博览"],
        "aliases": ["szicec"],
    },
    {
        "source_code": "theme_park", "name": "锦绣中华民俗村", "city": "shenzhen", "district": "南山区",
        "type": "公园", "address": "南山区深南大道9003号", "transport": "地铁1号线华侨城站",
        "fee": "收费", "description": "锦绣中华民俗村，含微缩景区和少数民族村寨。",
        "official_url": "", "highlights": ["微缩景观", "民俗文化", "泼水节"],
        "aliases": ["锦绣中华民俗村"],
    },
    {
        "source_code": "szcp", "name": "深圳市少年宫", "city": "shenzhen", "district": "福田区",
        "type": "青少年宫", "address": "福田区福中一路2006号", "transport": "地铁3/4号线少年宫站",
        "fee": "免费", "description": "深圳市少年宫，含科技展馆和培训课程。",
        "official_url": "", "highlights": ["科技展馆", "青少年培训"],
        "aliases": ["深圳市少年宫", "深圳市少年宫官网"],
    },
    {
        "source_code": "szaac", "name": "深圳市青少年活动中心", "city": "shenzhen", "district": "福田区",
        "type": "青少年宫", "address": "福田区红荔路", "transport": "地铁3号线通新岭站",
        "fee": "免费", "description": "深圳市青少年活动中心。",
        "official_url": "", "highlights": ["青少年培训", "兴趣课程"],
        "aliases": ["深圳市青少年活动中心", "深圳市青少年活动中心官网"],
    },
    {
        "source_code": "szbook", "name": "深圳书城", "city": "shenzhen", "district": "福田区",
        "type": "文化中心", "address": "福田区福中一路", "transport": "地铁3/4号线少年宫站",
        "fee": "免费", "description": "深圳书城中心城，大型图书零售和文化活动空间。",
        "official_url": "", "highlights": ["图书", "文化活动"],
        "aliases": ["深圳书城", "深圳书城中心城"],
    },
    {
        "source_code": "szhbgy", "name": "深圳湾公园", "city": "shenzhen", "district": "南山区",
        "type": "公园", "address": "南山区滨海大道", "transport": "地铁2号线湾厦站",
        "fee": "免费", "description": "深圳湾滨海休闲带，适合散步骑行。",
        "official_url": "", "highlights": ["滨海休闲", "骑行"],
        "aliases": ["深圳湾公园"],
    },
    {
        "source_code": "hssjwh", "name": "海上世界文化艺术中心", "city": "shenzhen", "district": "南山区",
        "type": "美术馆", "address": "南山区蛇口海上世界", "transport": "地铁2号线蛇口港站",
        "fee": "免费", "description": "海上世界文化艺术中心，展示当代艺术。",
        "official_url": "", "highlights": ["当代艺术", "滨海文化"],
        "aliases": ["海上世界文化艺术中心"],
    },
    {
        "source_code": "szzybwg", "name": "深圳中医药博物馆", "city": "shenzhen", "district": "福田区",
        "type": "博物馆", "address": "福田区", "transport": "",
        "fee": "免费", "description": "展示中医药文化和历史。",
        "official_url": "", "highlights": ["中医药文化", "健康科普"],
        "aliases": ["深圳中医药博物馆"],
    },
    {
        "source_code": "szjewg", "name": "深圳珠宝博物馆", "city": "shenzhen", "district": "盐田区",
        "type": "博物馆", "address": "盐田区", "transport": "",
        "fee": "免费", "description": "展示珠宝首饰文化和工艺。",
        "official_url": "", "highlights": ["珠宝", "工艺"],
        "aliases": ["深圳珠宝博物馆官网"],
    },
    {
        "source_code": "hlgj", "name": "深圳欢乐谷", "city": "shenzhen", "district": "南山区",
        "type": "公园", "address": "南山区华侨城", "transport": "地铁1/2号线世界之窗站",
        "fee": "收费", "description": "大型主题游乐园。",
        "official_url": "", "highlights": ["主题游乐", "刺激项目"],
        "aliases": ["深圳欢乐谷"],
    },
    {
        "source_code": "hoha", "name": "深圳欢乐海岸", "city": "shenzhen", "district": "南山区",
        "type": "文化中心", "address": "南山区白石路", "transport": "地铁9号线深圳湾公园站",
        "fee": "免费", "description": "华侨城欢乐海岸，集文化、商业、休闲于一体。",
        "official_url": "", "highlights": ["滨海休闲", "商业文化"],
        "aliases": ["深圳欢乐海岸"],
    },
    {
        "source_code": "szworld", "name": "深圳世界之窗", "city": "shenzhen", "district": "南山区",
        "type": "公园", "address": "南山区深南大道9003号", "transport": "地铁1/2号线世界之窗站",
        "fee": "收费", "description": "世界微缩景观主题公园。",
        "official_url": "", "highlights": ["微缩景观", "世界文化"],
        "aliases": ["深圳世界之窗"],
    },
    {
        "source_code": "hhgy", "name": "洪湖公园", "city": "shenzhen", "district": "罗湖区",
        "type": "公园", "address": "罗湖区文锦北路", "transport": "地铁3号线草埔站",
        "fee": "免费", "description": "以荷花著称的公园。",
        "official_url": "", "highlights": ["荷花", "观鸟"],
        "aliases": ["洪湖公园"],
    },
    {
        "source_code": "dshslc", "name": "大沙河生态长廊", "city": "shenzhen", "district": "南山区",
        "type": "公园", "address": "南山区大沙河", "transport": "",
        "fee": "免费", "description": "大沙河沿河生态绿道。",
        "official_url": "", "highlights": ["生态绿道", "骑行"],
        "aliases": ["大沙河生态长廊"],
    },
    {
        "source_code": "tjsgd", "name": "淘金山绿道", "city": "shenzhen", "district": "罗湖区",
        "type": "公园", "address": "罗湖区淘金山", "transport": "",
        "fee": "免费", "description": "淘金山绿道，适合徒步。",
        "official_url": "", "highlights": ["徒步", "山林"],
        "aliases": ["淘金山绿道"],
    },
    {
        "source_code": "xwhsl", "name": "西湾红树林公园", "city": "shenzhen", "district": "宝安区",
        "type": "公园", "address": "宝安区西乡", "transport": "",
        "fee": "免费", "description": "西湾红树林湿地公园。",
        "official_url": "", "highlights": ["红树林", "观鸟"],
        "aliases": ["西湾红树林公园"],
    },
    {
        "source_code": "mzohbd", "name": "茅洲河碧道", "city": "shenzhen", "district": "光明区",
        "type": "公园", "address": "光明区茅洲河", "transport": "",
        "fee": "免费", "description": "茅洲河碧道，适合散步骑行。",
        "official_url": "", "highlights": ["碧道", "生态"],
        "aliases": ["茅洲河碧道"],
    },
    {
        "source_code": "sysgy", "name": "石岩湖湿地公园", "city": "shenzhen", "district": "宝安区",
        "type": "公园", "address": "宝安区石岩", "transport": "",
        "fee": "免费", "description": "石岩湖湿地公园。",
        "official_url": "", "highlights": ["湿地", "观鸟"],
        "aliases": ["石岩湖湿地公园"],
    },
    {
        "source_code": "sywhzx", "name": "石岩文化艺术中心", "city": "shenzhen", "district": "宝安区",
        "type": "文化中心", "address": "宝安区石岩", "transport": "",
        "fee": "免费", "description": "石岩街道文化艺术中心。",
        "official_url": "", "highlights": ["社区文化"],
        "aliases": ["石岩文化艺术中心"],
    },
    {
        "source_code": "hhsgy", "name": "红花山公园", "city": "shenzhen", "district": "坪山区",
        "type": "公园", "address": "坪山区", "transport": "",
        "fee": "免费", "description": "坪山区红花山公园。",
        "official_url": "", "highlights": ["休闲", "登高"],
        "aliases": ["红花山公园"],
    },
    {
        "source_code": "dyzx", "name": "深圳大运中心", "city": "shenzhen", "district": "龙岗区",
        "type": "体育中心", "address": "龙岗区龙城街道", "transport": "地铁3号线大运站",
        "fee": "收费", "description": "深圳大运中心体育场和体育馆。",
        "official_url": "", "highlights": ["体育赛事", "大型活动"],
        "aliases": ["深圳大运中心体育场", "深圳大运中心体育馆", "深圳大运中心"],
    },
    {
        "source_code": "dzxgy", "name": "大运中心公园", "city": "shenzhen", "district": "龙岗区",
        "type": "公园", "address": "龙岗区大运中心", "transport": "地铁3号线大运站",
        "fee": "免费", "description": "大运中心公园。",
        "official_url": "", "highlights": ["休闲", "运动"],
        "aliases": ["大运中心公园"],
    },
    {
        "source_code": "atszx", "name": "安托山公共文化中心", "city": "shenzhen", "district": "福田区",
        "type": "文化中心", "address": "福田区安托山", "transport": "地铁2号线安托山站",
        "fee": "免费", "description": "安托山公共文化中心。",
        "official_url": "", "highlights": ["社区文化"],
        "aliases": ["安托山公共文化中心"],
    },
    {
        "source_code": "bzgx", "name": "北站中心公园", "city": "shenzhen", "district": "龙华区",
        "type": "公园", "address": "龙华区深圳北站", "transport": "地铁4/5号线深圳北站",
        "fee": "免费", "description": "深圳北站中心公园。",
        "official_url": "", "highlights": ["休闲", "城市公园"],
        "aliases": ["北站中心公园"],
    },
    {
        "source_code": "kxgny", "name": "深圳科学公园（南翼）", "city": "shenzhen", "district": "光明区",
        "type": "公园", "address": "光明区", "transport": "",
        "fee": "免费", "description": "深圳科学公园南翼。",
        "official_url": "", "highlights": ["科学", "休闲"],
        "aliases": ["深圳科学公园（南翼）"],
    },
    {
        "source_code": "rcgy", "name": "人才公园", "city": "shenzhen", "district": "南山区",
        "type": "公园", "address": "南山区科苑南路", "transport": "地铁2号线后海站",
        "fee": "免费", "description": "深圳人才公园。",
        "official_url": "", "highlights": ["人才主题", "滨海休闲"],
        "aliases": ["人才公园"],
    },
    # 街道级文化站
    {
        "source_code": "jhwtz", "name": "吉华街道文化站", "city": "shenzhen", "district": "龙岗区",
        "type": "文化馆", "address": "龙岗区吉华街道", "transport": "",
        "fee": "免费", "description": "龙岗区吉华街道文化站。",
        "official_url": "", "highlights": ["社区文化"],
        "aliases": ["吉华街道文化站"],
    },
    {
        "source_code": "nwwtz", "name": "南湾街道文化站", "city": "shenzhen", "district": "龙岗区",
        "type": "文化馆", "address": "龙岗区南湾街道", "transport": "",
        "fee": "免费", "description": "龙岗区南湾街道文化站。",
        "official_url": "", "highlights": ["社区文化"],
        "aliases": ["南湾街道文化站"],
    },
    {
        "source_code": "pdwtz", "name": "坪地街道文化站", "city": "shenzhen", "district": "龙岗区",
        "type": "文化馆", "address": "龙岗区坪地街道", "transport": "",
        "fee": "免费", "description": "龙岗区坪地街道文化站。",
        "official_url": "", "highlights": ["社区文化"],
        "aliases": ["坪地街道文化站"],
    },
    {
        "source_code": "ylwh", "name": "园岭街道综合性文化服务中心", "city": "shenzhen", "district": "福田区",
        "type": "文化馆", "address": "福田区园岭街道", "transport": "",
        "fee": "免费", "description": "福田区园岭街道综合性文化服务中心。",
        "official_url": "", "highlights": ["社区文化"],
        "aliases": ["园岭街道综合性文化服务中心"],
    },
    {
        "source_code": "tywh", "name": "桃源街道综合性文化服务中心", "city": "shenzhen", "district": "南山区",
        "type": "文化馆", "address": "南山区桃源街道", "transport": "",
        "fee": "免费", "description": "南山区桃源街道综合性文化服务中心。",
        "official_url": "", "highlights": ["社区文化"],
        "aliases": ["桃源街道综合性文化服务中心", "桃源街道文化服务中心"],
    },
    {
        "source_code": "fhwh", "name": "凤凰街道综合性文化服务中心", "city": "shenzhen", "district": "光明区",
        "type": "文化馆", "address": "光明区凤凰街道", "transport": "",
        "fee": "免费", "description": "光明区凤凰街道综合性文化服务中心。",
        "official_url": "", "highlights": ["社区文化"],
        "aliases": ["凤凰街道综合性文化服务中心"],
    },
    {
        "source_code": "jlwh", "name": "江岭社区公共文化服务中心", "city": "shenzhen", "district": "坪山区",
        "type": "文化馆", "address": "坪山区江岭社区", "transport": "",
        "fee": "免费", "description": "坪山区江岭社区公共文化服务中心。",
        "official_url": "", "highlights": ["社区文化"],
        "aliases": ["江岭社区公共文化服务中心"],
    },
    {
        "source_code": "jkwh", "name": "迳口社区综合性文化服务中心", "city": "shenzhen", "district": "光明区",
        "type": "文化馆", "address": "光明区迳口社区", "transport": "",
        "fee": "免费", "description": "光明区迳口社区综合性文化服务中心。",
        "official_url": "", "highlights": ["社区文化"],
        "aliases": ["迳口社区综合性文化服务中心"],
    },

    # ================================================================
    # 杭州场馆
    # ================================================================
    {
        "source_code": "zjam", "name": "浙江省博物馆", "city": "hangzhou", "district": "西湖区",
        "type": "博物馆", "address": "西湖区孤山路", "transport": "",
        "fee": "免费", "description": "浙江省博物馆。",
        "official_url": "", "highlights": ["浙江历史"],
        "aliases": [],
    },
]

# ============================================================
# 索引 — 启动时构建，O(1) 查找
# ============================================================

_BY_SOURCE_CODE = {}  # source_code → venue dict
_BY_NAME = {}         # name → venue dict (精确匹配)
_BY_ALIAS = {}        # alias → venue dict
_ALL_BY_CITY = {}     # city → list of venues

# 区县关键词（用于从 venue/source 文本中兜底匹配区县）
DISTRICT_KEYWORDS = {
    '南山区': ['南山', '蛇口', '南头', '粤海', '华侨城湿地', '滨海艺术中心', '前海'],
    '福田区': ['福田', '莲花', '市民中心', '华强北'],
    '罗湖区': ['罗湖', '东门', '黄贝', '翠竹', '地王', '大剧院', '深圳戏院', '古生物'],
    '宝安区': ['宝安', '西乡', '福永', '沙井', '松岗', '湾区之眼', '滨海文化公园'],
    '龙岗区': ['龙岗', '坂田', '布吉', '龙城', '横岗', '客家', '鹤湖新居'],
    '龙华区': ['龙华', '民治', '观澜', '大浪', '版画', '生态文明'],
    '光明区': ['光明', '公明', '玉塘', '马田', '光明文化艺术中心', '深圳科学技术馆（光明'],
    '坪山区': ['坪山', '聚龙', '马峦', '燕子湖', '石井', '深圳自然博物馆'],
    '盐田区': ['盐田', '沙头角', '中英街', '梅沙'],
    '大鹏新区': ['大鹏', '大亚湾', '葵涌', '南澳', '西涌', '杨梅坑', '七娘山', '官湖', '坝光', '金沙湾', '玫瑰海岸', '东涌', '较场尾', '地质公园', '核能科技'],
}


def _build_index():
    """构建查找索引"""
    for v in VENUES:
        # by source_code
        _BY_SOURCE_CODE[v['source_code']] = v
        # by name
        _BY_NAME[v['name']] = v
        # by aliases
        for alias in v.get('aliases', []):
            _BY_ALIAS[alias] = v
        # by city
        city = v['city']
        if city not in _ALL_BY_CITY:
            _ALL_BY_CITY[city] = []
        _ALL_BY_CITY[city].append(v)


_build_index()


# ============================================================
# 公共 API
# ============================================================

def lookup_venue(source_code):
    """通过 source_code 查场馆，返回完整场馆 dict 或 None"""
    return _BY_SOURCE_CODE.get(source_code)


def lookup_venue_by_name(name):
    """通过场馆名查场馆（含别名匹配），返回场馆 dict 或 None"""
    if not name:
        return None
    # 精确匹配
    v = _BY_NAME.get(name)
    if v:
        return v
    # 别名匹配
    v = _BY_ALIAS.get(name)
    if v:
        return v
    # 模糊匹配：name 包含某个注册名或别名
    for reg_name, reg_v in _BY_NAME.items():
        if reg_name in name or name in reg_name:
            return reg_v
    for alias, reg_v in _BY_ALIAS.items():
        if alias in name or name in alias:
            return reg_v
    return None


def get_district(source, venue_name=''):
    """查区县：先查 source_code，再查 venue_name，最后用关键词兜底"""
    # 1. source_code 直接查
    v = _BY_SOURCE_CODE.get(source)
    if v:
        return v['district']
    # 2. source 当作 name/alias 查
    v = lookup_venue_by_name(source)
    if v:
        return v['district']
    # 3. venue_name 查
    v = lookup_venue_by_name(venue_name)
    if v:
        return v['district']
    # 4. 关键词兜底
    text = f"{source} {venue_name}"
    for district, keywords in DISTRICT_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                return district
    return None


def get_venue_type(source, venue_name=''):
    """查场馆类型"""
    v = _BY_SOURCE_CODE.get(source) or lookup_venue_by_name(source) or lookup_venue_by_name(venue_name)
    if v:
        return v['type']
    return '其他'


def resolve_source_code(source, venue_name=''):
    """将任意 source/venue 文本解析为标准 source_code"""
    # 直接匹配
    if source and source in _BY_SOURCE_CODE:
        return source
    # 通过 source 文本查
    v = lookup_venue_by_name(source)
    if v:
        return v['source_code']
    # 通过 venue_name 查
    v = lookup_venue_by_name(venue_name)
    if v:
        return v['source_code']
    return None


def get_all_venues():
    """返回所有场馆列表"""
    return VENUES.copy()


def get_venues_by_city(city):
    """返回指定城市的所有场馆"""
    return _ALL_BY_CITY.get(city, [])


def get_venues_by_district(district):
    """返回指定区县的所有场馆"""
    return [v for v in VENUES if v['district'] == district]


def generate_venue_info_json(output_path=None):
    """生成 venue_info.json 格式的数据"""
    venues = []
    for v in VENUES:
        venues.append({
            'name': v['name'],
            'source': v['source_code'],
            'city': v['city'],
            'district': v['district'],
            'type': v['type'],
            'address': v.get('address', ''),
            'transport': v.get('transport', ''),
            'fee': v.get('fee', '免费'),
            'description': v.get('description', ''),
            'official_url': v.get('official_url', ''),
            'highlights': v.get('highlights', []),
        })
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(venues, f, ensure_ascii=False, indent=2)
        print(f"venue_info.json 已生成: {output_path} ({len(venues)} 个场馆)")
    return venues


if __name__ == '__main__':
    # 自测
    print(f"场馆总数: {len(VENUES)}")
    for city in ['shenzhen', 'guangzhou', 'shanghai', 'beijing', 'hangzhou']:
        venues = get_venues_by_city(city)
        print(f"  {city}: {len(venues)} 个场馆")

    # 测试区县查询
    test_cases = [
        ('pslib', '', '坪山区'),
        ('dp_nuclear', '', '大鹏新区'),
        ('', '坪山区图书馆', '坪山区'),
        ('', '大亚湾核能科技馆', '大鹏新区'),
        ('unknown', '马峦山郊野公园', '坪山区'),
        ('unknown', '深圳西涌天文台', '大鹏新区'),
    ]
    print("\n区县查询测试:")
    for source, venue, expected in test_cases:
        result = get_district(source, venue)
        status = '✓' if result == expected else '✗'
        print(f"  {status} get_district('{source}', '{venue}') = '{result}' (期望: '{expected}')")
