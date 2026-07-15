import json

with open('output/exhibitions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data.sort(key=lambda x: x['start_date'])

print('深圳展览日程表（共 %d 个）' % len(data))
print('=' * 130)
print('%-6s | %-45s | %-12s | %-28s' % ('序号', '展会名称', '日期', '地点'))
print('-' * 130)

for i, ex in enumerate(data, 1):
    venue = '深圳会展中心' if ex['source'] == 'szcec' else '深圳国际会展中心'
    if ex['start_date'] == ex['end_date']:
        date_range = ex['start_date']
    else:
        date_range = ex['start_date'] + '~' + ex['end_date'][5:]
    name = ex['name'][:42] + '..' if len(ex['name']) > 42 else ex['name']
    print('%-6d | %-45s | %-12s | %-28s' % (i, name, date_range, venue))

print('=' * 130)