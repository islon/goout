import json

# 读取新数据
with open('/workspace/goout/output/raw/real_activities_nanjing_batch2.json', 'r', encoding='utf-8') as f:
    batch2 = json.load(f)

# 读取原始数据
with open('/workspace/goout/output/raw/real_activities_nanjing.json', 'r', encoding='utf-8') as f:
    original = json.load(f)

# 找出重复的标题
original_titles = set(item['title'] for item in original)

# 描述补充字典 - 为过短的描述补充内容
description_supplements = {
    "六朝博物馆'小六文学院'暑期研学营": "跟着老师识香、品香、制香，解锁六朝贵族的氛围感秘籍，品味诗词里的墨香与药香，五感沉浸式研学体验，深度感受六朝文化魅力。",
    "六朝瓦当寻宝大冒险研学活动": "走进六朝博物馆探索瓦当的秘密，人面纹、莲花纹、兽面纹瓦当故事，完成小小文物代言人视频录制，深度了解六朝历史文化。",
    "六朝博物馆夏夜文博趣味课堂": "暑期夜间亲子体验活动，锻炼孩子表达力，亲手触摸传统技艺，夏夜两小时充实有意义，感受六朝文化独特魅力。",
    "紫金山天文台陨石标本研学营": "含陨石标本和望远镜观测，需提前2周报名，7月中旬场次仍有余额，探索宇宙奥秘天文科普之旅。",
    "南京地质博物馆暑期科普活动": "江宁研学线路地质考古主题，在汤山直立人化石遗址博物馆探究远古地质与人类起源，了解地球演化历史。",
    "南京古生物博物馆暑期恐龙主题活动": "古生物化石科普，了解远古生物演化，亲子可近距离观赏珍贵化石标本，探索生命演化奥秘。",
    "南京北极阁气象博物馆暑期科普": "气象科普教育基地，了解气象观测知识，亲子学习天气现象的科学原理，增长气象科学知识。",
    "无人机科普研学活动": "操纵飞行模拟器、手工制作航模，无人机科普教育基地研学活动，了解航空科技知识。",
    "南航御风园触摸大国重器研学": "少年金陵游平台预约，周末场次周四晚8点释放名额，参观航空航天展品，感受航空科技魅力。",
    "紫金大戏院暑期儿童木偶剧专场": "暑期儿童木偶剧展演，传统木偶艺术表演，亲子共同感受非遗木偶戏独特艺术魅力。",
    "南京人民大会堂亲子音乐会暑期专场": "暑期亲子音乐会系列，多种主题儿童音乐会，适合全家共同欣赏音乐艺术熏陶。",
    "红山森林动物园暑期特惠自然探索主题游": "专业老师带赏，深度揭秘熊猫狼谷冈瓦纳等明星路线，每日上下午两场，避开迷路趣闻环保知识拉满。",
    "南京欢乐谷蓝鲸音乐节": "暑期蓝鲸音乐节盛大开启，六大园区游乐项目+音乐节，毕业季特惠中高考生130元，夏日狂欢派对。",
    "银杏湖乐园端午民俗闯关活动": "20米巨型鳌鱼空降，射五毒飞花令钓粽子民俗闯关，摩天轮漂流沙滩戏水一票通玩，夏日亲子好去处。",
    "牛首山文化旅游区端午民俗体验": "制香囊编五彩绳投壶传统民俗，山间步道平缓舒适，傍晚山林音乐会，避暑休闲祈福绝佳去处。",
    "汤山紫清湖野生动物世界端午活动": "大熊猫小熊猫长颈鹿亚洲象萌宠近距离投喂，包粽子抓五福娃娃民俗体验，撸动物赏湖景泡温泉一站式。",
    "园博园酷野烘焙市集端午活动": "艾草系甜品手工粽点氛围感拉满，萌宠乐园适配小朋友，夜间山水烟花秀，白天逛园林夜晚赏烟火。",
    "汤山欢乐水世界暑期焕新升级": "全面更新升级，拍岸浪花南洋海岸，数不清水上设备滑道惊险刺激，夏日消暑玩水胜地。",
    "云水涧夏日泼水狂欢节": "每周末趣味泼水狂欢节，儿童趣味闯关清凉玩水，水枪大战泳池DJ狂欢，夏日沉浸式清凉体验。",
    "南京海底世界暑期海洋生物展": "暑期海洋生物主题展，美人鱼表演海豚海狮表演，亲子海洋科普之旅，探索神秘海底世界。",
    "玄武湖景区暑期荷花展": "暑期荷花盛开季节，玄武湖荷花展，亲子游船赏荷，夏日休闲好去处，感受夏日荷塘美景。",
}

# 修复数据
fixed_activities = []
duplicate_count = 0
short_desc_count = 0

for item in batch2:
    # 跳过重复项
    if item['title'] in original_titles:
        duplicate_count += 1
        continue
    
    # 补充过短的描述
    if len(item['description']) < 30:
        if item['title'] in description_supplements:
            item['description'] = description_supplements[item['title']]
            short_desc_count += 1
    
    fixed_activities.append(item)

# 保存修复后的数据
with open('/workspace/goout/output/raw/real_activities_nanjing_batch2.json', 'w', encoding='utf-8') as f:
    json.dump(fixed_activities, f, ensure_ascii=False, indent=2)

print(f"修复前活动数: {len(batch2)}")
print(f"删除重复活动数: {duplicate_count}")
print(f"补充描述活动数: {short_desc_count}")
print(f"修复后活动数: {len(fixed_activities)}")
print(f"加上原始数据总计: {len(original) + len(fixed_activities)}")

# 再次验证
required_fields = ['title', 'venue', 'city', 'start_date', 'end_date', 'link', 'description', 'fee', 'source', 'family_friendly']
issues = 0
for i, item in enumerate(fixed_activities):
    for field in required_fields:
        if field not in item:
            print(f'第{i}条缺少字段: {field}')
            issues += 1
    if len(item.get('description', '')) < 30:
        print(f'第{i}条描述过短: {len(item["description"])}字 - {item["title"]}')
        issues += 1
    if item.get('city') != 'nanjing':
        print(f'第{i}条城市不是nanjing: {item["city"]}')
        issues += 1
    if item.get('family_friendly') != True:
        print(f'第{i}条family_friendly不是true: {item["family_friendly"]}')
        issues += 1

if issues == 0:
    print("\n所有数据验证通过!")
else:
    print(f"\n发现 {issues} 个问题")
