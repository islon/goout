import json
import os
import re

ALLOWED_FEE_VALUES = {'免费', '免费需预约', '收费', '部分免费', '需购票'}

NEW_EVENTS = [
    {
        "title": "深圳世界之窗·WoW狂欢节+啤酒节",
        "venue": "深圳世界之窗",
        "start_date": "2026-06-18",
        "end_date": "2026-08-30",
        "link": "https://m.sohu.com/a/1045463665_675420/",
        "description": "33天狂欢音乐季，汇集尖叫鸡、HIGH5、啤酒等艺人，罗马假日广场冰城啤酒+烧烤+音乐派对。",
        "category": "户外活动",
        "fee": "收费",
        "contact": "",
        "family_friendly": True,
        "source": "深圳世界之窗",
        "city": "shenzhen"
    },
    {
        "title": "深圳欢乐海岸·夏日狂欢节",
        "venue": "深圳欢乐海岸",
        "start_date": "2026-07-04",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1045463665_675420/",
        "description": "全网爆火'大胖鸡天团'空降，夏日音乐节周周有大牌，清凉水枪+电音派对+明星演出。票价130-228元。",
        "category": "户外活动",
        "fee": "收费",
        "contact": "",
        "family_friendly": True,
        "source": "深圳欢乐海岸",
        "city": "shenzhen"
    },
    {
        "title": "《海洋奇旅：起航》迪士尼电影主题展",
        "venue": "深圳人才公园潮汐广场",
        "start_date": "2026-07-01",
        "end_date": "2026-07-31",
        "link": "http://m.toutiao.com/group/7658324154139148850/",
        "description": "还原莫阿娜同款航海木船、巨型莫兰迪鲸鱼气球、寻路花环等电影场景，拍照打卡。免费免预约。地铁13号线'人才公园站'B1出口。",
        "category": "展览",
        "fee": "免费",
        "contact": "",
        "family_friendly": True,
        "source": "南山融媒体中心",
        "city": "shenzhen"
    },
    {
        "title": "青绿同心——深港两地书画艺术交流展",
        "venue": "福田美术馆",
        "start_date": "2026-07-05",
        "end_date": "2026-07-30",
        "link": "http://m.toutiao.com/group/7659258111554961955/",
        "description": "汇聚深港两地书画名家精品力作140余幅，涵盖国画山水、书法、现代水墨、油画等。免费开放。",
        "category": "展览",
        "fee": "免费",
        "contact": "",
        "family_friendly": True,
        "source": "南方都市报",
        "city": "shenzhen"
    }
]


def validate_and_fix_event(event):
    fixed = False
    
    if 'fee' in event and event['fee'] not in ALLOWED_FEE_VALUES:
        print(f"  修复fee字段: {event['fee']} -> 免费")
        event['fee'] = '免费'
        fixed = True
    
    description = event.get('description', '')
    if len(description) < 10:
        print(f"  修复description字段: 长度不足10字")
        title = event.get('title', '')
        venue = event.get('venue', '')
        fee = event.get('fee', '')
        new_desc = f"{title}。活动地点：{venue}。{fee}。"
        event['description'] = new_desc
        fixed = True
    
    return fixed


def add_new_events_to_manual_data():
    manual_data_path = os.path.join(os.path.dirname(__file__), 'manual_data.json')
    
    with open(manual_data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    existing_titles = {item['title'] for item in data}
    added_count = 0
    
    for event in NEW_EVENTS:
        if event['title'] in existing_titles:
            print(f"跳过已存在活动: {event['title']}")
            continue
        
        fixed = validate_and_fix_event(event)
        data.append(event)
        added_count += 1
        print(f"添加新活动: {event['title']}")
        if fixed:
            print("  (已进行数据质量修复)")
    
    with open(manual_data_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n共添加 {added_count} 个新活动")
    return added_count


if __name__ == "__main__":
    add_new_events_to_manual_data()