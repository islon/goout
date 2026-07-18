import json
import os

output_path = os.path.join(os.path.dirname(__file__), 'real_activities_nanjing_batch4.json')
with open(output_path, 'r') as fp:
    activities = json.load(fp)

existing_titles = set(item['title'] for item in activities)

# 读取所有现有活动标题
for f in ['real_activities_nanjing.json', 'real_activities_nanjing_batch2.json', 'real_activities_nanjing_batch3.json']:
    path = os.path.join(os.path.dirname(__file__), f)
    if os.path.exists(path):
        with open(path, 'r') as fp:
            data = json.load(fp)
            for item in data:
                existing_titles.add(item['title'])

print(f"当前去重后总数: {len(existing_titles)}")

# 补充2条新活动
new_acts = [
    {
        "title": "溧水区天生桥胭脂河龙舟文化节",
        "venue": "溧水区洪蓝街道天生桥河",
        "city": "nanjing",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://k.sina.cn/article_7879923025_1d5ae155101901sy9u.html",
        "description": "南京规模最大的民间龙舟活动之一，配套亲子划龙舟体验、水枪泡泡泼水派对、花船巡游、夜市美食、夜间乐队演出，河面开阔观赛无遮挡。",
        "fee": "免费观赛，体验项目另收费",
        "source": "新浪新闻",
        "family_friendly": True
    },
    {
        "title": "南京市民俗博物馆甘熙宅第暑期非遗展",
        "venue": "南京市民俗博物馆（甘熙宅第）",
        "city": "nanjing",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://k.sina.cn/article_7880068258_1d5b04ca201901bzci.html",
        "description": "暑期周一正常开放，展示南京地区民俗文化与非遗技艺，孩子们可以了解老南京的风土人情与传统手工艺，感受古都文化底蕴。",
        "fee": "门票20元/人",
        "source": "新浪新闻",
        "family_friendly": True
    }
]

added = 0
for act in new_acts:
    if act['title'] not in existing_titles:
        activities.append(act)
        existing_titles.add(act['title'])
        added += 1
        print(f"新增: {act['title']}")
    else:
        print(f"已存在: {act['title']}")

print(f"\n本轮新增: {added}")
print(f"batch4总数: {len(activities)}")
print(f"去重后总数: {len(existing_titles)}")

with open(output_path, 'w', encoding='utf-8') as fp:
    json.dump(activities, fp, ensure_ascii=False, indent=2)

print(f"已保存到: {output_path}")
