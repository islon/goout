import json
import datetime

with open('output/exhibitions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('=== 检查8月26日的展览 ===')
aug26 = [ex for ex in data if ex['start_date'] == '2026-08-26' or ex['end_date'] == '2026-08-26']
for ex in aug26:
    print(f"  {ex['start_date']} ~ {ex['end_date']}: {ex['name'][:50]}")

print(f'\n8月26日相关展览数量: {len(aug26)}')

print('\n=== 按月份统计展览数量 ===')
month_counts = {}
for ex in data:
    month = ex['start_date'][:7]
    month_counts[month] = month_counts.get(month, 0) + 1

for month in sorted(month_counts.keys()):
    print(f"  {month}: {month_counts[month]} 个")

print('\n=== 检查所有异常日期 ===')
errors = []
for ex in data:
    start = datetime.date.fromisoformat(ex['start_date'])
    end = datetime.date.fromisoformat(ex['end_date'])
    if end < start:
        errors.append(f"  日期倒序: {ex['start_date']} ~ {ex['end_date']}: {ex['name'][:30]}")
    if start.year not in [2025, 2026]:
        errors.append(f"  年份异常: {ex['start_date']}: {ex['name'][:30]}")

if errors:
    print('\n'.join(errors))
else:
    print('  日期验证通过，无异常')

print('\n=== 检查深圳会展中心爬虫源数据 ===')
szcec_data = [ex for ex in data if ex['source'] == 'szcec']
print(f"深圳会展中心展览数: {len(szcec_data)}")

print('\n=== 检查深圳国际会展中心爬虫源数据 ===')
world_data = [ex for ex in data if ex['source'] == 'shenzhen_world']
print(f"深圳国际会展中心展览数: {len(world_data)}")

print('\n=== 检查2026年8月26日的展览详情 ===')
aug26_2026 = [ex for ex in data if ex['start_date'] == '2026-08-26']
for ex in aug26_2026:
    print(f"\n  名称: {ex['name']}")
    print(f"  日期: {ex['start_date']} ~ {ex['end_date']}")
    print(f"  地点: {ex['venue']}")
    print(f"  来源: {ex['source']}")
    print(f"  URL: {ex.get('url', 'N/A')}")