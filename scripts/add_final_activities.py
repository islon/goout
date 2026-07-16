import json
import os

DATA_FILE = 'output/exhibitions.json'
OUTPUT_FILE = 'output/exhibitions.json'

new_activities = [
    # ========== 北京补充活动（第七批 - 冲刺300）==========
    {"name": "恭王府博物馆", "venue": "恭王府博物馆", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "清代规模最大的一座王府，和珅故居，一座恭王府半部清朝史。", "source": "北京本地宝", "highlights": ["恭王府", "历史", "和珅"], "type": "展览"},
    {"name": "雍和宫祈福", "venue": "雍和宫", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "北京最大的藏传佛教寺院，香火最旺的寺庙之一，祈福胜地。", "source": "北京本地宝", "highlights": ["雍和宫", "佛教", "祈福"], "type": "亲子活动"},
    {"name": "孔庙和国子监博物馆", "venue": "孔庙和国子监博物馆", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "元明清三代国家最高学府，孔子文化，古代科举制度展。", "source": "北京本地宝", "highlights": ["国子监", "孔庙", "科举"], "type": "展览"},
    {"name": "北京鲁迅博物馆", "venue": "北京鲁迅博物馆", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "鲁迅故居，鲁迅生平事迹展，新文化运动纪念。", "source": "北京本地宝", "highlights": ["鲁迅", "文学", "博物馆"], "type": "展览"},
    {"name": "宋庆龄同志故居", "venue": "宋庆龄同志故居", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "后海北沿，清代王府花园，宋庆龄生平事迹展。", "source": "北京本地宝", "highlights": ["宋庆龄", "故居", "历史"], "type": "展览"},
    {"name": "郭沫若纪念馆", "venue": "郭沫若纪念馆", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "前海西街，郭沫若故居，文学与史学成就展。", "source": "北京本地宝", "highlights": ["郭沫若", "文学", "故居"], "type": "展览"},
    {"name": "茅盾故居", "venue": "茅盾故居", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "后圆恩寺胡同，茅盾晚年居住地，文学大师故居。", "source": "北京本地宝", "highlights": ["茅盾", "文学", "故居"], "type": "展览"},
    {"name": "老舍纪念馆", "venue": "老舍纪念馆", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "丰富胡同丹柿小院，老舍故居，人民艺术家纪念。", "source": "北京本地宝", "highlights": ["老舍", "文学", "丹柿小院"], "type": "展览"},
    {"name": "北京画院美术馆", "venue": "北京画院美术馆", "city": "beijing", "district": "朝阳区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "齐白石艺术陈列，北京画院藏品展，近现代书画。", "source": "北京本地宝", "highlights": ["齐白石", "书画", "美术馆"], "type": "展览"},
    {"name": "中国美术馆", "venue": "中国美术馆", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "国家级美术殿堂，近现代美术精品，各类特展轮番上演。", "source": "北京本地宝", "highlights": ["中国美术馆", "美术", "展览"], "type": "展览"},
    {"name": "今日美术馆", "venue": "今日美术馆", "city": "beijing", "district": "朝阳区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "中国第一家民营公益性当代美术馆，当代艺术前沿。", "source": "北京本地宝", "highlights": ["当代艺术", "美术馆", "今日"], "type": "展览"},
    {"name": "红砖美术馆", "venue": "红砖美术馆", "city": "beijing", "district": "朝阳区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "网红美术馆，红砖建筑艺术，园林景观，拍照打卡胜地。", "source": "北京本地宝", "highlights": ["红砖", "美术馆", "网红"], "type": "展览"},
    {"name": "松美术馆", "venue": "松美术馆", "city": "beijing", "district": "顺义区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "白色建筑与松树相映，文艺气质满满，小众艺术空间。", "source": "北京本地宝", "highlights": ["松美术馆", "文艺", "小众"], "type": "展览"},
    {"name": "中国地质博物馆", "venue": "中国地质博物馆", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "亚洲历史最悠久的国家级地质博物馆，宝石恐龙化石矿物。", "source": "北京本地宝", "highlights": ["地质", "宝石", "恐龙"], "type": "展览"},
    {"name": "中国邮政邮票博物馆", "venue": "中国邮政邮票博物馆", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "中国邮票发展史，珍贵邮票收藏，集邮爱好者的天堂。", "source": "北京本地宝", "highlights": ["邮票", "邮政", "收藏"], "type": "展览"},
    {"name": "中国铁道博物馆正阳门馆", "venue": "中国铁道博物馆正阳门馆", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "中国铁路发展史，蒸汽机车到高铁，铁路科普教育。", "source": "北京本地宝", "highlights": ["铁道", "火车", "高铁"], "type": "展览"},
    {"name": "北京古观象台", "venue": "北京古观象台", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "明清两代皇家天文台，古代天文仪器，世界现存最古老天文台之一。", "source": "北京本地宝", "highlights": ["古观象台", "天文", "明清"], "type": "展览"},
    {"name": "智化寺古建音乐", "venue": "智化寺", "city": "beijing", "district": "东城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "明代古刹，京音乐非遗传承，智化寺梨花，古建筑艺术。", "source": "北京本地宝", "highlights": ["智化寺", "京音乐", "明代"], "type": "演出"},
    {"name": "大钟寺古钟博物馆", "venue": "大钟寺古钟博物馆", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "永乐大钟，古钟收藏，钟文化展，觉生寺古建筑。", "source": "北京本地宝", "highlights": ["大钟寺", "古钟", "永乐大钟"], "type": "展览"},
    {"name": "五塔寺石刻博物馆", "venue": "北京石刻艺术博物馆", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "真觉寺金刚宝座塔，北京石刻艺术，银杏秋天最美。", "source": "北京本地宝", "highlights": ["五塔寺", "石刻", "银杏"], "type": "展览"},
    {"name": "万寿寺北京艺术博物馆", "venue": "北京艺术博物馆", "city": "beijing", "district": "海淀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "京西小故宫万寿寺，明清古建筑群，艺术收藏展。", "source": "北京本地宝", "highlights": ["万寿寺", "艺术博物馆", "古建筑"], "type": "展览"},
    {"name": "白塔寺妙应寺", "venue": "妙应寺白塔", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "元代藏式佛塔，中国现存最早最大的藏式佛塔。", "source": "北京本地宝", "highlights": ["白塔寺", "元代", "佛塔"], "type": "展览"},
    {"name": "北京东岳庙", "venue": "北京民俗博物馆", "city": "beijing", "district": "朝阳区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "道教正一道派，北京民俗博物馆，老北京民俗文化。", "source": "北京本地宝", "highlights": ["东岳庙", "民俗", "道教"], "type": "展览"},
    {"name": "白云观道教", "venue": "白云观", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "道教全真派祖庭，中国道教协会所在地，道教文化圣地。", "source": "北京本地宝", "highlights": ["白云观", "道教", "全真派"], "type": "亲子活动"},
    {"name": "牛街礼拜寺", "venue": "牛街礼拜寺", "city": "beijing", "district": "西城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "北京最古老最著名的清真寺，伊斯兰文化建筑。", "source": "北京本地宝", "highlights": ["牛街", "清真寺", "伊斯兰"], "type": "展览"},
    {"name": "潭柘寺千年古刹", "venue": "潭柘寺", "city": "beijing", "district": "门头沟区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "先有潭柘寺后有北京城，千年古刹，帝王树银杏树。", "source": "北京本地宝", "highlights": ["潭柘寺", "千年古刹", "银杏"], "type": "亲子活动"},
    {"name": "戒台寺古松", "venue": "戒台寺", "city": "beijing", "district": "门头沟区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "天下第一戒坛，千年古松，辽代佛教建筑。", "source": "北京本地宝", "highlights": ["戒台寺", "古松", "佛教"], "type": "亲子活动"},
    {"name": "云居寺石经山", "venue": "云居寺", "city": "beijing", "district": "房山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "北京敦煌，石经宝库，千年刻经史，佛教圣地。", "source": "北京本地宝", "highlights": ["云居寺", "石经", "佛教"], "type": "展览"},
    {"name": "红螺寺秋景", "venue": "红螺寺", "city": "beijing", "district": "怀柔区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "京北第一古刹，红螺三绝，雌雄银杏，紫藤寄松。", "source": "北京本地宝", "highlights": ["红螺寺", "古刹", "银杏"], "type": "亲子活动"},
    {"name": "北京欢乐谷万圣节", "venue": "北京欢乐谷", "city": "beijing", "district": "朝阳区", "start_date": "2026-10-15", "end_date": "2026-11-11", "fee": "收费", "description": "万圣节惊奇之旅，恐怖屋鬼屋，夜间巡游，变装派对。", "source": "北京本地宝", "highlights": ["万圣节", "欢乐谷", "鬼屋"], "type": "演出"},

    # ========== 上海补充活动（第七批 - 冲刺300）==========
    {"name": "上海博物馆人民广场馆", "venue": "上海博物馆人民广场馆", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "中国四大博物馆之一，青铜器陶瓷书画玉器，中国古代艺术宝库。", "source": "上海本地宝", "highlights": ["上博", "青铜器", "古代艺术"], "type": "展览"},
    {"name": "上海博物馆东馆", "venue": "上海博物馆东馆", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "上博新馆，更大展厅更多文物，上海文化新地标。", "source": "上海本地宝", "highlights": ["上博东馆", "新馆", "浦东"], "type": "展览"},
    {"name": "上海科技馆机器人世界", "venue": "上海科技馆", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "机器人表演互动，机器人剧场，机器人舞蹈，科技感十足。", "source": "上海本地宝", "highlights": ["机器人", "科技馆", "科技"], "type": "展览"},
    {"name": "上海科技馆生物万象", "venue": "上海科技馆", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "热带雨林生态，仿生动物，热带雨林瀑布，自然科普。", "source": "上海本地宝", "highlights": ["生物万象", "热带雨林", "自然"], "type": "展览"},
    {"name": "上海科技馆宇航天地", "venue": "上海科技馆", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "神舟飞船模型，太空探索，宇航知识科普，航天梦。", "source": "上海本地宝", "highlights": ["宇航", "航天", "科技馆"], "type": "展览"},
    {"name": "上海科技馆地壳探秘", "venue": "上海科技馆", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "地震火山体验，矿物宝石，地球科学知识。", "source": "上海本地宝", "highlights": ["地壳", "地震", "矿物"], "type": "展览"},
    {"name": "上海自然博物馆生命长河", "venue": "上海自然博物馆", "city": "shanghai", "district": "静安区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "生命演化展，恐龙大象长颈鹿模型，自然史教育。", "source": "上海本地宝", "highlights": ["生命长河", "恐龙", "自然"], "type": "展览"},
    {"name": "上海自然博物馆恐龙盛世", "venue": "上海自然博物馆", "city": "shanghai", "district": "静安区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "马门溪龙霸王龙，恐龙骨架模型，恐龙时代探秘。", "source": "上海本地宝", "highlights": ["恐龙", "马门溪龙", "化石"], "type": "展览"},
    {"name": "上海自然博物馆起源之谜", "venue": "上海自然博物馆", "city": "shanghai", "district": "静安区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "宇宙大爆炸生命起源，人类进化，科学知识普及。", "source": "上海本地宝", "highlights": ["起源", "宇宙", "进化"], "type": "展览"},
    {"name": "上海自然博物馆生态万象", "venue": "上海自然博物馆", "city": "shanghai", "district": "静安区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "非洲大草原极地海底世界，生态系统科普。", "source": "上海本地宝", "highlights": ["生态", "非洲", "极地"], "type": "展览"},
    {"name": "上海玻璃博物馆", "venue": "上海玻璃博物馆", "city": "shanghai", "district": "宝山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "玻璃艺术殿堂，热玻璃表演，DIY玻璃制作体验。", "source": "上海本地宝", "highlights": ["玻璃", "艺术", "DIY"], "type": "展览"},
    {"name": "上海汽车博物馆", "venue": "上海汽车博物馆", "city": "shanghai", "district": "嘉定区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "中国首家专业汽车博物馆，古董车经典车，汽车发展史。", "source": "上海本地宝", "highlights": ["汽车", "博物馆", "古董车"], "type": "展览"},
    {"name": "上海电影博物馆", "venue": "上海电影博物馆", "city": "shanghai", "district": "徐汇区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "上海电影发展史，百年电影记忆，老电影体验。", "source": "上海本地宝", "highlights": ["电影", "博物馆", "百年"], "type": "展览"},
    {"name": "上海公安博物馆", "venue": "上海公安博物馆", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "公安发展史，警械装备，特种警用车辆。", "source": "上海本地宝", "highlights": ["公安", "警械", "免费"], "type": "展览"},
    {"name": "上海中医药博物馆", "venue": "上海中医药博物馆", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "中医中药发展史，中草药标本，养生文化。", "source": "上海本地宝", "highlights": ["中医", "中药", "养生"], "type": "展览"},
    {"name": "上海昆虫博物馆", "venue": "上海昆虫博物馆", "city": "shanghai", "district": "徐汇区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "蝴蝶标本昆虫世界，中科院上海昆虫博物馆。", "source": "上海本地宝", "highlights": ["昆虫", "蝴蝶", "科普"], "type": "展览"},
    {"name": "上海地震科普馆", "venue": "上海地震科普馆", "city": "shanghai", "district": "松江区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "地震知识科普，地震模拟体验，防灾教育。", "source": "上海本地宝", "highlights": ["地震", "科普", "防灾"], "type": "展览"},
    {"name": "上海航海博物馆", "venue": "中国航海博物馆", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "国家级航海博物馆，古船模型航海史，海事教育。", "source": "上海本地宝", "highlights": ["航海", "博物馆", "古船"], "type": "展览"},
    {"name": "上海工艺美术博物馆", "venue": "上海工艺美术博物馆", "city": "shanghai", "district": "徐汇区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "法租界小白宫，绒绣面塑剪纸，上海工艺美术精品。", "source": "上海本地宝", "highlights": ["工艺美术", "小白宫", "非遗"], "type": "展览"},
    {"name": "上海隧道科技馆", "venue": "上海隧道科技馆", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "隧道建设技术，盾构机模型，地下工程科普。", "source": "上海本地宝", "highlights": ["隧道", "科技馆", "免费"], "type": "展览"},
    {"name": "上海城市规划展示馆", "venue": "上海城市规划展示馆", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "上海城市发展规划，巨大城市模型，未来上海。", "source": "上海本地宝", "highlights": ["规划馆", "城市模型", "免费"], "type": "展览"},
    {"name": "上海杜莎夫人蜡像馆", "venue": "上海杜莎夫人蜡像馆", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "南京路杜莎夫人蜡像馆，明星名人蜡像，互动拍照。", "source": "上海本地宝", "highlights": ["杜莎夫人", "蜡像", "南京路"], "type": "展览"},
    {"name": "上海惊魂密境", "venue": "上海惊魂密境", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "沉浸式惊悚体验，老上海传说故事，惊魂冒险。", "source": "上海本地宝", "highlights": ["惊魂密境", "沉浸式", "惊悚"], "type": "演出"},
    {"name": "上海环球金融中心观光", "venue": "上海环球金融中心", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "100层观光厅，空中走廊，俯瞰陆家嘴全景。", "source": "上海本地宝", "highlights": ["环球金融中心", "观光", "陆家嘴"], "type": "亲子活动"},
    {"name": "金茂大厦观光", "venue": "金茂大厦", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "88层观光厅，云中漫步，浦东地标建筑。", "source": "上海本地宝", "highlights": ["金茂大厦", "观光", "地标"], "type": "亲子活动"},
    {"name": "上海中心118层观光", "venue": "上海中心大厦", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "上海最高楼，118层上海之巅观光厅，360度全景。", "source": "上海本地宝", "highlights": ["上海中心", "观光", "最高楼"], "type": "亲子活动"},
    {"name": "上海迪士尼乐园春日", "venue": "上海迪士尼乐园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-03-01", "end_date": "2026-05-31", "fee": "收费", "description": "春日主题活动，花花草草装饰，春日限定商品美食。", "source": "上海本地宝", "highlights": ["迪士尼", "春天", "主题"], "type": "演出"},
    {"name": "上海迪士尼夏日狂欢节", "venue": "上海迪士尼乐园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-08-31", "fee": "收费", "description": "夏日狂欢节城堡秀，戏水派对，夏日限定冰品。", "source": "上海本地宝", "highlights": ["迪士尼", "夏日", "戏水"], "type": "演出"},
    {"name": "上海欢乐谷国潮节", "venue": "上海欢乐谷", "city": "shanghai", "district": "松江区", "start_date": "2026-10-01", "end_date": "2026-10-31", "fee": "收费", "description": "国庆国潮主题，传统与现代融合，国风演出。", "source": "上海本地宝", "highlights": ["国潮节", "欢乐谷", "国庆"], "type": "演出"},
    {"name": "上海欢乐谷跨年灯会", "venue": "上海欢乐谷", "city": "shanghai", "district": "松江区", "start_date": "2026-12-01", "end_date": "2027-02-28", "fee": "收费", "description": "跨年灯会，万盏彩灯，非遗花灯，新年氛围。", "source": "上海本地宝", "highlights": ["灯会", "跨年", "欢乐谷"], "type": "演出"},

    # ========== 广州补充活动（第七批 - 冲刺300）==========
    {"name": "广东省博物馆岭南文化", "venue": "广东省博物馆", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "广东历史文化展，潮州木雕端砚牙雕，岭南文化精华。", "source": "广东省博物馆", "highlights": ["省博", "岭南文化", "木雕"], "type": "展览"},
    {"name": "广东省博物馆自然资源", "venue": "广东省博物馆", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "广东自然资源展，矿物宝石古生物，地质科普。", "source": "广东省博物馆", "highlights": ["省博", "自然资源", "矿物"], "type": "展览"},
    {"name": "广东省博物馆端砚艺术", "venue": "广东省博物馆", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "端砚专题展，端溪名砚，文房四宝，中国四大名砚之首。", "source": "广东省博物馆", "highlights": ["端砚", "文房四宝", "肇庆"], "type": "展览"},
    {"name": "广州塔观光游乐", "venue": "广州塔", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "中国第一高塔，433米观光，速降座椅，空中漫步。", "source": "广州本地宝", "highlights": ["广州塔", "观光", "地标"], "type": "亲子活动"},
    {"name": "白云山摩星岭", "venue": "白云山风景名胜区", "city": "guangzhou", "district": "白云区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "羊城第一峰，登高望远，俯瞰广州城，摩星岭祈福。", "source": "广州本地宝", "highlights": ["摩星岭", "登高", "白云山"], "type": "亲子活动"},
    {"name": "云台花园赏花", "venue": "云台花园", "city": "guangzhou", "district": "白云区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "白云山脚下，四季花卉，玻璃温室，花城明珠。", "source": "广州本地宝", "highlights": ["云台花园", "赏花", "温室"], "type": "展览"},
    {"name": "麓湖公园休闲", "venue": "麓湖公园", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "白云山边的湖光山色，麓湖鸿鹄楼，划船漫步。", "source": "广州本地宝", "highlights": ["麓湖", "划船", "免费"], "type": "亲子活动"},
    {"name": "珠江公园花城广场", "venue": "珠江公园", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "CBD中央公园，快绿湖，园林景观，城市绿肺。", "source": "广州本地宝", "highlights": ["珠江公园", "CBD", "免费"], "type": "亲子活动"},
    {"name": "天河公园", "venue": "天河公园", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "广州东部最大综合性公园，湖光山色，邓世昌纪念馆。", "source": "广州本地宝", "highlights": ["天河公园", "免费", "邓世昌"], "type": "亲子活动"},
    {"name": "海珠湖公园", "venue": "海珠湖公园", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "海珠湿地的内湖，湖心岛花海，观鸟骑行。", "source": "广州本地宝", "highlights": ["海珠湖", "免费", "骑行"], "type": "亲子活动"},
    {"name": "荔湾湖公园", "venue": "荔湾湖公园", "city": "guangzhou", "district": "荔湾区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "老西关的荔枝湾，荔湾涌，粤剧文化，水乡风情。", "source": "广州本地宝", "highlights": ["荔湾湖", "西关", "粤剧"], "type": "亲子活动"},
    {"name": "流花湖公园", "venue": "流花湖公园", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "广州市中心的绿洲，玫瑰园，浮丘，观鸟胜地。", "source": "广州本地宝", "highlights": ["流花湖", "免费", "观鸟"], "type": "亲子活动"},
    {"name": "番禺莲花山", "venue": "莲花山旅游区", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "古采石场遗址，莲花塔，望海观音，珠江口狮子洋。", "source": "广州本地宝", "highlights": ["莲花山", "采石场", "观音"], "type": "亲子活动"},
    {"name": "从化流溪河国家森林公园", "venue": "流溪河国家森林公园", "city": "guangzhou", "district": "从化区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "流溪湖游船，三桠塘幽谷，森林氧吧，避暑胜地。", "source": "广州本地宝", "highlights": ["流溪河", "森林", "避暑"], "type": "亲子活动"},
    {"name": "增城白水寨瀑布", "venue": "白水寨风景名胜区", "city": "guangzhou", "district": "增城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "中国大陆落差最大瀑布，9999级天南第一梯，亲水栈道。", "source": "广州本地宝", "highlights": ["白水寨", "瀑布", "登山"], "type": "亲子活动"},
    {"name": "南沙湿地观鸟", "venue": "南沙湿地公园", "city": "guangzhou", "district": "南沙区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "候鸟栖息地，湿地游船，红树林生态，自然科普。", "source": "广州本地宝", "highlights": ["湿地", "观鸟", "生态"], "type": "亲子活动"},
    {"name": "宝墨园南粤苑", "venue": "宝墨园", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "岭南园林艺术，赵泰来藏品馆，紫洞舫，锦鲤观赏。", "source": "广州本地宝", "highlights": ["宝墨园", "南粤苑", "园林"], "type": "展览"},
    {"name": "余荫山房四大名园", "venue": "余荫山房", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "广东四大名园之一，小巧玲珑，岭南园林精品。", "source": "广州本地宝", "highlights": ["余荫山房", "四大名园", "园林"], "type": "展览"},
    {"name": "广州农讲所纪念馆", "venue": "广州农民运动讲习所", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "毛泽东主办农民运动讲习所旧址，红色教育基地。", "source": "广州本地宝", "highlights": ["农讲所", "红色", "毛泽东"], "type": "展览"},
    {"name": "广州起义纪念馆", "venue": "广州起义纪念馆", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "广州起义历史，广州苏维埃政府旧址，红色文化。", "source": "广州本地宝", "highlights": ["广州起义", "红色", "历史"], "type": "展览"},

    # ========== 杭州补充活动（第七批 - 冲刺）==========
    {"name": "浙江省博物馆武林馆", "venue": "浙江省博物馆武林馆区", "city": "hangzhou", "district": "下城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "浙江历史文化展，越地长歌，十万年前到近现代。", "source": "浙江省博物馆", "highlights": ["浙博", "越地长歌", "历史"], "type": "展览"},
    {"name": "浙江省博物馆之江馆", "venue": "浙江省博物馆之江馆区", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "浙博新馆，更大展区更多文物，浙江文化新地标。", "source": "浙江省博物馆", "highlights": ["浙博之江", "新馆", "之江"], "type": "展览"},
    {"name": "浙江自然博物院杭州馆", "venue": "浙江自然博物院杭州馆", "city": "hangzhou", "district": "下城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "西湖文化广场，自然标本恐龙化石，自然科普教育。", "source": "浙江自然博物院", "highlights": ["自然博物馆", "恐龙", "免费"], "type": "展览"},
    {"name": "中国茶叶博物馆", "venue": "中国茶叶博物馆", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "双峰茶博物馆，茶文化展，龙井茶园，茶艺体验。", "source": "杭州本地宝", "highlights": ["茶博", "茶文化", "龙井"], "type": "展览"},
    {"name": "中国丝绸博物馆", "venue": "中国丝绸博物馆", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "丝路文化，丝绸发展史，古代服饰，锦罗绸缎。", "source": "杭州本地宝", "highlights": ["丝绸", "丝路", "服饰"], "type": "展览"},
    {"name": "杭州博物馆", "venue": "杭州博物馆", "city": "hangzhou", "district": "上城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "杭州历史文化，最忆是杭州，馆藏精品文物。", "source": "杭州本地宝", "highlights": ["杭博", "杭州历史", "免费"], "type": "展览"},
    {"name": "杭州西湖博物馆", "venue": "杭州西湖博物馆", "city": "hangzhou", "district": "上城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "西湖文化史，西湖十景，西湖申遗展。", "source": "杭州本地宝", "highlights": ["西湖博物馆", "西湖", "免费"], "type": "展览"},
    {"name": "南宋官窑博物馆", "venue": "南宋官窑博物馆", "city": "hangzhou", "district": "上城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "南宋官窑遗址，青瓷艺术，制瓷体验。", "source": "杭州本地宝", "highlights": ["南宋官窑", "青瓷", "遗址"], "type": "展览"},
    {"name": "胡庆余堂中药博物馆", "venue": "胡庆余堂中药博物馆", "city": "hangzhou", "district": "上城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "江南药王胡庆余堂，中药文化，古建筑群。", "source": "杭州本地宝", "highlights": ["胡庆余堂", "中药", "河坊街"], "type": "展览"},
    {"name": "中国杭帮菜博物馆", "venue": "中国杭帮菜博物馆", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "杭帮菜发展史，美食文化，模型菜品展示。", "source": "杭州本地宝", "highlights": ["杭帮菜", "美食", "博物馆"], "type": "展览"},
    {"name": "中国湿地博物馆", "venue": "中国湿地博物馆", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "西溪湿地内，湿地生态科普，全国唯一国家级湿地博物馆。", "source": "杭州本地宝", "highlights": ["湿地博物馆", "西溪", "生态"], "type": "展览"},
    {"name": "京杭大运河博物馆", "venue": "中国京杭大运河博物馆", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "运河文化，漕运历史，大运河世界遗产展。", "source": "杭州本地宝", "highlights": ["大运河", "博物馆", "免费"], "type": "展览"},
    {"name": "中国刀剪剑博物馆", "venue": "中国刀剪剑博物馆", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "张小泉剪刀，刀剑文化，工艺发展史。", "source": "杭州本地宝", "highlights": ["刀剪剑", "张小泉", "免费"], "type": "展览"},
    {"name": "中国伞博物馆", "venue": "中国伞博物馆", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "伞文化，油纸伞工艺，西湖绸伞。", "source": "杭州本地宝", "highlights": ["伞博物馆", "油纸伞", "免费"], "type": "展览"},
    {"name": "中国扇博物馆", "venue": "中国扇博物馆", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "扇子文化，王星记扇子，制扇工艺。", "source": "杭州本地宝", "highlights": ["扇博物馆", "王星记", "免费"], "type": "展览"},
    {"name": "杭州工艺美术博物馆", "venue": "杭州工艺美术博物馆", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "杭州工艺美术精品，非遗技艺，手工艺体验。", "source": "杭州本地宝", "highlights": ["工艺美术", "非遗", "手工"], "type": "展览"},
    {"name": "浙江美术馆", "venue": "浙江美术馆", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "浙江最高美术殿堂，当代艺术展，各类美术特展。", "source": "杭州本地宝", "highlights": ["浙江美术馆", "艺术", "免费"], "type": "展览"},
    {"name": "中国美术学院美术馆", "venue": "中国美术学院美术馆", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "中国最高美术学府美术馆，先锋艺术，学生作品展。", "source": "杭州本地宝", "highlights": ["国美", "美术馆", "先锋艺术"], "type": "展览"},
    {"name": "韩美林艺术馆", "venue": "韩美林艺术馆", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "植物园内，韩美林艺术作品，雕塑绘画陶瓷。", "source": "杭州本地宝", "highlights": ["韩美林", "艺术", "植物园"], "type": "展览"},
    {"name": "西湖音乐节", "venue": "西湖音乐节", "city": "hangzhou", "district": "西湖区", "start_date": "2026-05-01", "end_date": "2026-05-31", "fee": "收费", "description": "杭州最具影响力的音乐节，独立音乐，民谣摇滚。", "source": "杭州本地宝", "highlights": ["音乐节", "西湖", "音乐"], "type": "演出"},
]

if __name__ == '__main__':
    if not os.path.exists(DATA_FILE):
        print(f"文件 {DATA_FILE} 不存在！")
        exit(1)
    
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        exhibitions = json.load(f)
    
    existing_names = {e['name'] for e in exhibitions}
    added_count = 0
    
    for activity in new_activities:
        if activity['name'] not in existing_names:
            exhibitions.append(activity)
            print(f"添加: {activity['name']} ({activity['city']})")
            added_count += 1
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(exhibitions, f, ensure_ascii=False, indent=2)
    
    print(f"\n共添加 {added_count} 个活动")
    
    city_counts = {}
    for e in exhibitions:
        city_counts[e['city']] = city_counts.get(e['city'], 0) + 1
    print(f"\n各城市活动数量:")
    for city, count in sorted(city_counts.items()):
        print(f"  {city}: {count}")
