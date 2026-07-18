import json

with open('/workspace/goout/output/raw/real_activities_shanghai_batch4.json', 'r', encoding='utf-8') as f:
    activities = json.load(f)

print(f"当前活动数量: {len(activities)}")

final_supplement = [
    {
        "title": "上海图书馆东馆暑期少儿阅读季活动",
        "venue": "上海图书馆东馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://wap.51ldb.com/shsldb/ms/content/019f63ce7869c001000066d533acd97d.html",
        "description": "2026上海童话暑期少儿阅读季，主题活动故事剧场少儿讲座创艺工坊展览展示七大板块千余项阅读活动。",
        "fee": "免费（部分需预约）",
        "source": "上海图书馆",
        "family_friendly": True
    },
    {
        "title": "上海少年儿童图书馆南西馆暑期活动",
        "venue": "上海少年儿童图书馆南西馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://wap.51ldb.com/shsldb/ms/content/019f63ce7869c001000066d533acd97d.html",
        "description": "阅万象主题暑期少儿阅读季，绘本故事会科普手工坊儿童文学名家分享，打造多彩阅读假期。",
        "fee": "免费（需预约）",
        "source": "上海少年儿童图书馆",
        "family_friendly": True
    },
    {
        "title": "世博文化公园音乐之林暑期音乐会",
        "venue": "世博文化公园音乐之林",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7659976244997440009/",
        "description": "户外草坪音乐会，周末定期上演不同主题音乐演出，亲子野餐聆听音乐，夏日休闲好去处。",
        "fee": "免费",
        "source": "世博文化公园",
        "family_friendly": True
    },
    {
        "title": "上海海洋水族馆暑期海底探秘活动",
        "venue": "上海海洋水族馆",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7654463135662834222/",
        "description": "暑期推出海底探秘主题活动，潜水员喂食表演、海洋科普小课堂、海底隧道夜宿体验。",
        "fee": "以官方票价为准",
        "source": "上海海洋水族馆",
        "family_friendly": True
    },
    {
        "title": "上海欢乐谷EV音乐乐园暑期狂欢",
        "venue": "上海欢乐谷",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-30",
        "link": "http://m.sh.bendibao.com/tour/jd/307624.html",
        "description": "水陆双园联动，白天逐浪戏水夜晚音浪炸场，欢乐广场泼水派对巨型水炮矩阵水枪补给站。",
        "fee": "以官方票价为准",
        "source": "上海欢乐谷",
        "family_friendly": True
    },
    {
        "title": "上海马戏城ERA时空之旅2暑期演出",
        "venue": "上海马戏城",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.meet-in-shanghai.net/cn/news/a-min-is-astonishing-the-excitement-never-stops-all-year-%E2%86%92-532454/",
        "description": "经典杂技马戏升级版演出，高空特技梦幻舞台效果，全家共享的震撼视觉盛宴。",
        "fee": "以官方票价为准",
        "source": "上海马戏城",
        "family_friendly": True
    },
    {
        "title": "临港冰雪明城酒店室内滑雪体验",
        "venue": "临港冰雪明城",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7654463135662834222/",
        "description": "室内真雪滑雪场，暑期避暑滑雪好去处，专业教练指导，亲子滑雪体验清凉一夏。",
        "fee": "以官方票价为准",
        "source": "临港冰雪明城",
        "family_friendly": True
    },
    {
        "title": "上海世博源暑期亲子嘉年华",
        "venue": "上海世博源",
        "city": "shanghai",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7659976244997440009/",
        "description": "世博源购物中心暑期亲子嘉年华，儿童游乐市集互动演出，一站式遛娃购物休闲。",
        "fee": "免费入场，项目另收费",
        "source": "上海世博源",
        "family_friendly": True
    }
]

activities.extend(final_supplement)

with open('/workspace/goout/output/raw/real_activities_shanghai_batch4.json', 'w', encoding='utf-8') as f:
    json.dump(activities, f, ensure_ascii=False, indent=2)

print(f"最终补充活动数量: {len(final_supplement)}")
print(f"最终总活动数量: {len(activities)}")
