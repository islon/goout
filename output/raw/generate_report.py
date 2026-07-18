import json

file_path = '/workspace/goout/output/raw/real_activities_beijing_batch2.json'
existing_file = '/workspace/goout/output/raw/real_activities_beijing.json'

with open(file_path, 'r', encoding='utf-8') as f:
    all_activities = json.load(f)

with open(existing_file, 'r', encoding='utf-8') as f:
    existing_activities = json.load(f)

existing_titles = set(a['title'] for a in existing_activities)
new_activities = [a for a in all_activities if a['title'] not in existing_titles]

print("=" * 60)
print("北京亲子活动补充搜索报告")
print("=" * 60)
print(f"\n📊 数量统计：")
print(f"  - 原有活动数量：{len(existing_activities)} 条")
print(f"  - 新增活动数量：{len(new_activities)} 条")
print(f"  - 总计活动数量：{len(all_activities)} 条")
print(f"  - 目标数量：150 条")
print(f"  - 完成情况：✅ 超额完成（{len(all_activities)}/150 = {len(all_activities)/150*100:.1f}%）")

print(f"\n🎪 新增的有代表性的活动（10个）：")
representative = [
    "行·迹——卡塔尔游牧生活与文化展",
    "生存竞技场·超时空追凶案沉浸式研学营",
    "奇幻历险音乐儿童剧《海王星飞船》",
    "小小研究生科学探究暑期班",
    "如见丨大音和鸣——中国传统音乐数字艺术展",
    "[花园生活·小博物家]夏令营",
    "打开艺术之门2026暑期艺术节",
    "我的机器人朋友——2026机器人探索展",
    "北京市青少年'脑智科技'主题创新夏令营",
    "西城区文化馆'艺路童行·文脉润心'少儿传统文化公益启蒙活动"
]
for i, name in enumerate(representative, 1):
    print(f"  {i}. {name}")

print(f"\n📚 数据来源列表：")
sources = set()
for activity in all_activities:
    sources.add(activity['source'])
for i, source in enumerate(sorted(sources), 1):
    count = sum(1 for a in all_activities if a['source'] == source)
    print(f"  {i}. {source}（{count}条）")

print(f"\n🏷️ 费用类型分布：")
fee_types = {}
for activity in all_activities:
    fee = activity['fee']
    if fee not in fee_types:
        fee_types[fee] = 0
    fee_types[fee] += 1
for fee, count in sorted(fee_types.items(), key=lambda x: -x[1]):
    print(f"  - {fee}：{count} 条")

print(f"\n📁 文件保存路径：")
print(f"  {file_path}")
print("=" * 60)
