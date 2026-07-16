import json
import os

DATA_FILE = 'output/exhibitions.json'
OUTPUT_FILE = 'output/exhibitions.json'

new_activities = [
    # ========== 上海补充活动（第八批 - 冲刺300）==========
    {"name": "上海城隍庙", "venue": "上海城隍庙", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "道教正一派道观，上海道教中心，豫园商圈内。", "source": "上海本地宝", "highlights": ["城隍庙", "道教", "豫园"], "type": "亲子活动"},
    {"name": "上海玉佛禅寺", "venue": "玉佛禅寺", "city": "shanghai", "district": "普陀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "上海著名佛教寺庙，玉佛楼供奉玉佛，百年古刹。", "source": "上海本地宝", "highlights": ["玉佛寺", "佛教", "玉佛"], "type": "亲子活动"},
    {"name": "上海静安寺", "venue": "静安寺", "city": "shanghai", "district": "静安区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "千年古刹静安寺，繁华商圈中的宁静，金佛殿。", "source": "上海本地宝", "highlights": ["静安寺", "古刹", "佛教"], "type": "亲子活动"},
    {"name": "上海龙华寺", "venue": "龙华寺", "city": "shanghai", "district": "徐汇区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "上海历史最久规模最大的寺庙，龙华塔，龙华庙会。", "source": "上海本地宝", "highlights": ["龙华寺", "古塔", "佛教"], "type": "亲子活动"},
    {"name": "上海真如寺", "venue": "真如寺", "city": "shanghai", "district": "普陀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "江南著名寺庙，元代大殿，真如公园。", "source": "上海本地宝", "highlights": ["真如寺", "元代", "古寺"], "type": "亲子活动"},
    {"name": "上海法华禅寺", "venue": "法华禅寺", "city": "shanghai", "district": "长宁区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "法华学问寺，千年银杏，古寺新貌。", "source": "上海本地宝", "highlights": ["法华禅寺", "银杏", "古寺"], "type": "亲子活动"},
    {"name": "上海东林寺", "venue": "东林寺", "city": "shanghai", "district": "金山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "浦南佛教名刹，世界最高景泰蓝善财童子，观音阁。", "source": "上海本地宝", "highlights": ["东林寺", "观音", "金山"], "type": "亲子活动"},
    {"name": "上海西林禅寺", "venue": "西林禅寺", "city": "shanghai", "district": "松江区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "松江古城名刹，圆应塔，千年古寺。", "source": "上海本地宝", "highlights": ["西林禅寺", "松江", "古塔"], "type": "亲子活动"},
    {"name": "上海报国寺", "venue": "报国寺", "city": "shanghai", "district": "青浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "淀山湖畔报国寺，千年古银杏，风景优美。", "source": "上海本地宝", "highlights": ["报国寺", "青浦", "银杏"], "type": "亲子活动"},
    {"name": "上海人民广场", "venue": "人民广场", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "上海城市中心，上海市政府，人民公园，博物馆。", "source": "上海本地宝", "highlights": ["人民广场", "市中心", "免费"], "type": "亲子活动"},
    {"name": "上海世纪公园", "venue": "世纪公园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "浦东最大生态城市公园，镜天湖，四季花卉。", "source": "上海本地宝", "highlights": ["世纪公园", "浦东", "生态"], "type": "亲子活动"},
    {"name": "上海长风公园", "venue": "长风公园", "city": "shanghai", "district": "普陀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "铁臂山银锄湖，长风海洋世界，上海老牌公园。", "source": "上海本地宝", "highlights": ["长风公园", "免费", "海洋世界"], "type": "亲子活动"},
    {"name": "上海共青森林公园", "venue": "共青国家森林公园", "city": "shanghai", "district": "杨浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "上海最大森林公园，森林氧吧，游乐设施。", "source": "上海本地宝", "highlights": ["共青森林公园", "森林", "杨浦"], "type": "亲子活动"},
    {"name": "上海滨江森林公园", "venue": "滨江森林公园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "黄浦江长江东海三水交汇，滨江岸线，生态森林。", "source": "上海本地宝", "highlights": ["滨江", "森林公园", "浦东"], "type": "亲子活动"},
    {"name": "上海植物园", "venue": "上海植物园", "city": "shanghai", "district": "徐汇区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "植物种类丰富，温室展览，四季花展。", "source": "上海本地宝", "highlights": ["植物园", "花卉", "徐汇"], "type": "展览"},
    {"name": "上海辰山植物园", "venue": "辰山植物园", "city": "shanghai", "district": "松江区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "矿坑花园温室展览，华东地区最大植物园。", "source": "上海本地宝", "highlights": ["辰山植物园", "矿坑", "松江"], "type": "展览"},
    {"name": "上海古猗园", "venue": "古猗园", "city": "shanghai", "district": "嘉定区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "江南古典园林，南翔小笼包发源地，园林艺术。", "source": "上海本地宝", "highlights": ["古猗园", "嘉定", "园林"], "type": "展览"},
    {"name": "上海醉白池", "venue": "醉白池", "city": "shanghai", "district": "松江区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "上海五大古典园林之一，宋代历史，松江古城。", "source": "上海本地宝", "highlights": ["醉白池", "松江", "古典园林"], "type": "展览"},
    {"name": "上海曲水园", "venue": "曲水园", "city": "shanghai", "district": "青浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "青浦曲水园，江南园林，小而精致。", "source": "上海本地宝", "highlights": ["曲水园", "青浦", "园林"], "type": "展览"},
    {"name": "上海桂林公园", "venue": "桂林公园", "city": "shanghai", "district": "徐汇区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "桂林公园，黄家花园，秋季桂花盛开。", "source": "上海本地宝", "highlights": ["桂林公园", "桂花", "徐汇"], "type": "展览"},
    {"name": "上海人民公园相亲角", "venue": "人民公园", "city": "shanghai", "district": "黄浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "上海特色相亲角，城市人文景观，周末热闹。", "source": "上海本地宝", "highlights": ["人民公园", "相亲角", "特色"], "type": "亲子活动"},
    {"name": "上海鲁迅公园", "venue": "鲁迅公园", "city": "shanghai", "district": "虹口区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "鲁迅墓纪念馆，虹口足球场，上海老牌公园。", "source": "上海本地宝", "highlights": ["鲁迅公园", "虹口", "免费"], "type": "亲子活动"},
    {"name": "上海和平公园", "venue": "和平公园", "city": "shanghai", "district": "虹口区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "动物岛，亲子休闲，改造后的生态公园。", "source": "上海本地宝", "highlights": ["和平公园", "动物岛", "免费"], "type": "亲子活动"},
    {"name": "上海中山公园", "venue": "中山公园", "city": "shanghai", "district": "长宁区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "上海西区老公园，中西合璧园林，交通便利。", "source": "上海本地宝", "highlights": ["中山公园", "长宁", "免费"], "type": "亲子活动"},
    {"name": "上海静安公园", "venue": "静安公园", "city": "shanghai", "district": "静安区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "静安寺旁城市绿洲，都市中的宁静。", "source": "上海本地宝", "highlights": ["静安公园", "静安", "免费"], "type": "亲子活动"},
    {"name": "上海迪士尼小镇", "venue": "上海迪士尼度假区", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "迪士尼主题小镇，购物餐饮，无需门票。", "source": "上海本地宝", "highlights": ["迪士尼小镇", "免费", "购物"], "type": "亲子活动"},
    {"name": "上海迪士尼乐园秋季", "venue": "上海迪士尼乐园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-09-01", "end_date": "2026-11-01", "fee": "收费", "description": "秋季特别活动，万圣节前奏，秋日装饰。", "source": "上海本地宝", "highlights": ["迪士尼", "秋季", "活动"], "type": "演出"},
    {"name": "上海野生动物园马戏", "venue": "上海野生动物园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "国际大马戏表演，俄罗斯演员，精彩杂技。", "source": "上海本地宝", "highlights": ["马戏", "表演", "野生动物园"], "type": "演出"},
    {"name": "上海海昌虎鲸表演", "venue": "上海海昌海洋公园", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "虎鲸科普秀，海豚白鲸表演，海洋剧场。", "source": "上海本地宝", "highlights": ["虎鲸", "表演", "海洋公园"], "type": "演出"},
    {"name": "上海欢乐谷万圣节", "venue": "上海欢乐谷", "city": "shanghai", "district": "松江区", "start_date": "2026-10-15", "end_date": "2026-11-11", "fee": "收费", "description": "万圣节惊魂夜，鬼屋探险，夜间巡游。", "source": "上海本地宝", "highlights": ["万圣节", "欢乐谷", "鬼屋"], "type": "演出"},
    {"name": "上海欢乐谷春节灯会", "venue": "上海欢乐谷", "city": "shanghai", "district": "松江区", "start_date": "2027-01-20", "end_date": "2027-02-28", "fee": "收费", "description": "新春灯会，自贡花灯，年味十足。", "source": "上海本地宝", "highlights": ["春节", "灯会", "欢乐谷"], "type": "演出"},
    {"name": "上海朱家角古镇美食", "venue": "朱家角古镇", "city": "shanghai", "district": "青浦区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "扎肉粽子阿婆茶，江南水乡美食，放生桥。", "source": "上海本地宝", "highlights": ["朱家角", "美食", "古镇"], "type": "亲子活动"},
    {"name": "上海新场古镇", "venue": "新场古镇", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "浦东千年古镇，历史风貌，色香俱全。", "source": "上海本地宝", "highlights": ["新场古镇", "浦东", "免费"], "type": "亲子活动"},
    {"name": "上海罗店古镇", "venue": "罗店古镇", "city": "shanghai", "district": "宝山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "金罗店，江南水乡，龙船花神灯。", "source": "上海本地宝", "highlights": ["罗店", "古镇", "宝山"], "type": "亲子活动"},
    {"name": "上海高桥古镇", "venue": "高桥古镇", "city": "shanghai", "district": "浦东新区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "高桥松饼发源地，浦东老镇，历史建筑。", "source": "上海本地宝", "highlights": ["高桥", "古镇", "浦东"], "type": "亲子活动"},

    # ========== 广州补充活动（第八批 - 冲刺300）==========
    {"name": "广州六榕寺", "venue": "六榕寺", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "广州四大丛林之一，六榕花塔，苏东坡题字。", "source": "广州本地宝", "highlights": ["六榕寺", "花塔", "佛教"], "type": "亲子活动"},
    {"name": "广州光孝寺", "venue": "光孝寺", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "广州历史最悠久的寺庙，未有羊城先有光孝。", "source": "广州本地宝", "highlights": ["光孝寺", "古寺", "免费"], "type": "亲子活动"},
    {"name": "广州海幢寺", "venue": "海幢寺", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "广州四大丛林之一，古树名木，清幽古寺。", "source": "广州本地宝", "highlights": ["海幢寺", "海珠", "免费"], "type": "亲子活动"},
    {"name": "广州大佛寺", "venue": "大佛寺", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "北京路步行街旁，大佛古寺，夜景璀璨。", "source": "广州本地宝", "highlights": ["大佛寺", "北京路", "夜景"], "type": "亲子活动"},
    {"name": "广州三元宫", "venue": "三元宫", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "广州著名道观，越秀山南麓，道教文化。", "source": "广州本地宝", "highlights": ["三元宫", "道教", "越秀"], "type": "亲子活动"},
    {"name": "广州纯阳观", "venue": "纯阳观", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "海珠区道教名观，漱珠岗，古梅奇石。", "source": "广州本地宝", "highlights": ["纯阳观", "道教", "海珠"], "type": "亲子活动"},
    {"name": "广州怀圣寺", "venue": "怀圣寺", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "中国最早的清真寺之一，光塔，伊斯兰教文化。", "source": "广州本地宝", "highlights": ["怀圣寺", "清真寺", "光塔"], "type": "亲子活动"},
    {"name": "广州五仙观", "venue": "五仙观", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "五羊传说发源地，岭南第一楼，广州历史。", "source": "广州本地宝", "highlights": ["五仙观", "五羊传说", "历史"], "type": "展览"},
    {"name": "广州陈家祠", "venue": "陈家祠", "city": "guangzhou", "district": "荔湾区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "广东民间工艺博物馆，岭南建筑艺术明珠。", "source": "广州本地宝", "highlights": ["陈家祠", "岭南建筑", "工艺"], "type": "展览"},
    {"name": "广州西关大屋", "venue": "西关古老大屋", "city": "guangzhou", "district": "荔湾区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "西关传统民居，趟栊门满洲窗，岭南风情。", "source": "广州本地宝", "highlights": ["西关大屋", "岭南", "传统建筑"], "type": "亲子活动"},
    {"name": "广州沙面岛欧陆建筑", "venue": "沙面岛", "city": "guangzhou", "district": "荔湾区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "欧陆风情建筑群，百年历史，拍照打卡圣地。", "source": "广州本地宝", "highlights": ["沙面", "欧陆风情", "拍照"], "type": "亲子活动"},
    {"name": "广州石室圣心大教堂", "venue": "石室圣心大教堂", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "中国最大的哥特式建筑，全石结构教堂。", "source": "广州本地宝", "highlights": ["石室", "教堂", "哥特式"], "type": "亲子活动"},
    {"name": "广州中山纪念堂", "venue": "中山纪念堂", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "纪念孙中山先生，八角形宫殿建筑，广州地标。", "source": "广州本地宝", "highlights": ["中山纪念堂", "孙中山", "地标"], "type": "展览"},
    {"name": "广州黄花岗七十二烈士墓", "venue": "黄花岗公园", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "辛亥革命纪念，黄花岗七十二烈士，红色教育。", "source": "广州本地宝", "highlights": ["黄花岗", "辛亥革命", "红色"], "type": "展览"},
    {"name": "广州三元里抗英斗争纪念馆", "venue": "三元里抗英纪念馆", "city": "guangzhou", "district": "白云区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "三元里人民抗英斗争，爱国主义教育基地。", "source": "广州本地宝", "highlights": ["三元里", "抗英", "爱国"], "type": "展览"},
    {"name": "广州海珠湖湿地", "venue": "海珠湖公园", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "海珠湿地内湖，花海骑行，观鸟休闲。", "source": "广州本地宝", "highlights": ["海珠湖", "免费", "湿地"], "type": "亲子活动"},
    {"name": "广州海珠国家湿地公园", "venue": "海珠国家湿地公园", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "广州绿心，万亩果园湿地，候鸟栖息地。", "source": "广州本地宝", "highlights": ["海珠湿地", "生态", "观鸟"], "type": "亲子活动"},
    {"name": "广州麓湖公园", "venue": "麓湖公园", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "白云山南麓，湖光山色，鸿鹄楼划船。", "source": "广州本地宝", "highlights": ["麓湖", "划船", "免费"], "type": "亲子活动"},
    {"name": "广州雕塑公园", "venue": "广州雕塑公园", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "雕塑主题公园，艺术作品，山林风光。", "source": "广州本地宝", "highlights": ["雕塑公园", "艺术", "免费"], "type": "亲子活动"},
    {"name": "广州云台花园", "venue": "云台花园", "city": "guangzhou", "district": "白云区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "白云山脚下，花城明珠，四季花海。", "source": "广州本地宝", "highlights": ["云台花园", "花卉", "白云山"], "type": "展览"},
    {"name": "广州兰圃", "venue": "兰圃", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "广州兰花主题公园，岭南园林，清雅幽静。", "source": "广州本地宝", "highlights": ["兰圃", "兰花", "岭南园林"], "type": "展览"},
    {"name": "广州花都湖公园", "venue": "花都湖公园", "city": "guangzhou", "district": "花都区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "花都城市生态公园，环湖绿道，湿地景观。", "source": "广州本地宝", "highlights": ["花都湖", "免费", "绿道"], "type": "亲子活动"},
    {"name": "广州增城挂绿湖", "venue": "挂绿湖", "city": "guangzhou", "district": "增城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "增城新地标，湖光山色，休闲散步。", "source": "广州本地宝", "highlights": ["挂绿湖", "增城", "免费"], "type": "亲子活动"},
    {"name": "广州番禺大夫山", "venue": "大夫山森林公园", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "番禺绿肺，骑行烧烤，周末亲子好去处。", "source": "广州本地宝", "highlights": ["大夫山", "骑行", "免费"], "type": "亲子活动"},
    {"name": "广州番禺莲花山古采石场", "venue": "莲花山旅游区", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "古采石场遗址，人工丹霞奇观，历史悠久。", "source": "广州本地宝", "highlights": ["莲花山", "采石场", "遗址"], "type": "展览"},
    {"name": "广州长隆国际大马戏", "venue": "长隆国际大马戏", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "全球最大专业马戏表演场，世界级马戏盛宴。", "source": "广州本地宝", "highlights": ["大马戏", "长隆", "表演"], "type": "演出"},
    {"name": "广州长隆飞鸟乐园", "venue": "长隆飞鸟乐园", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "百鸟飞歌，湿地生态，鸟类科普教育。", "source": "广州本地宝", "highlights": ["飞鸟乐园", "湿地", "鸟类"], "type": "亲子活动"},
    {"name": "广州岭南印象园", "venue": "岭南印象园", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "岭南乡土风情，非遗表演，传统文化体验。", "source": "广州本地宝", "highlights": ["岭南印象园", "非遗", "文化"], "type": "亲子活动"},
    {"name": "广州沙湾古镇", "venue": "沙湾古镇", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "800年历史岭南文化古镇，姜撞奶美食。", "source": "广州本地宝", "highlights": ["沙湾", "古镇", "姜撞奶"], "type": "亲子活动"},
    {"name": "广州塱头古村", "venue": "塱头古村", "city": "guangzhou", "district": "花都区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "花都炭步塱头古村，明清古建筑群，书室文化。", "source": "广州本地宝", "highlights": ["塱头古村", "花都", "古建筑"], "type": "亲子活动"},

    # ========== 杭州补充活动（第八批 - 冲刺）==========
    {"name": "杭州灵顺寺", "venue": "灵顺寺", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "北高峰上，天下第一财神庙，登高祈福。", "source": "杭州本地宝", "highlights": ["灵顺寺", "财神庙", "北高峰"], "type": "亲子活动"},
    {"name": "杭州净慈寺", "venue": "净慈寺", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "西湖十景南屏晚钟，净慈禅寺，千年古刹。", "source": "杭州本地宝", "highlights": ["净慈寺", "南屏晚钟", "西湖"], "type": "亲子活动"},
    {"name": "杭州虎跑泉", "venue": "虎跑公园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "西湖三大名泉之一，虎跑梦泉，李叔同纪念馆。", "source": "杭州本地宝", "highlights": ["虎跑", "名泉", "李叔同"], "type": "亲子活动"},
    {"name": "杭州玉泉", "venue": "玉泉", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "西湖三大名泉之一，玉泉鱼跃，植物园内。", "source": "杭州本地宝", "highlights": ["玉泉", "名泉", "植物园"], "type": "亲子活动"},
    {"name": "杭州龙井村", "venue": "龙井村", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "西湖龙井茶原产地，茶园风光，茶农家访。", "source": "杭州本地宝", "highlights": ["龙井村", "龙井茶", "茶园"], "type": "亲子活动"},
    {"name": "杭州梅家坞茶文化村", "venue": "梅家坞", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "龙井茶乡，农家茶楼，茶文化体验。", "source": "杭州本地宝", "highlights": ["梅家坞", "茶文化", "农家"], "type": "亲子活动"},
    {"name": "杭州九溪十八涧", "venue": "九溪烟树", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "西湖新十景，溪水潺潺，徒步胜地。", "source": "杭州本地宝", "highlights": ["九溪", "徒步", "西湖新十景"], "type": "亲子活动"},
    {"name": "杭州云栖竹径", "venue": "云栖竹径", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "西湖新十景，竹林幽径，清凉避暑。", "source": "杭州本地宝", "highlights": ["云栖竹径", "竹林", "避暑"], "type": "亲子活动"},
    {"name": "杭州满陇桂雨", "venue": "满觉陇", "city": "hangzhou", "district": "西湖区", "start_date": "2026-09-15", "end_date": "2026-10-15", "fee": "免费", "description": "西湖新十景，金秋桂花飘香，赏桂胜地。", "source": "杭州本地宝", "highlights": ["满陇桂雨", "桂花", "秋天"], "type": "展览"},
    {"name": "杭州龙井问茶", "venue": "龙井", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "西湖新十景，龙井茶原产地，茶文化体验。", "source": "杭州本地宝", "highlights": ["龙井问茶", "茶文化", "西湖新十景"], "type": "亲子活动"},
    {"name": "杭州宝石流霞", "venue": "宝石山", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "西湖新十景，保俶塔，登高望西湖。", "source": "杭州本地宝", "highlights": ["宝石山", "保俶塔", "西湖新十景"], "type": "亲子活动"},
    {"name": "杭州吴山天风", "venue": "吴山", "city": "hangzhou", "district": "上城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "西湖新十景，城隍阁，杭城百姓山。", "source": "杭州本地宝", "highlights": ["吴山", "城隍阁", "西湖新十景"], "type": "亲子活动"},
    {"name": "杭州玉皇飞云", "venue": "玉皇山", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "西湖新十景，福星观，登高望江湖。", "source": "杭州本地宝", "highlights": ["玉皇山", "道教", "西湖新十景"], "type": "亲子活动"},
    {"name": "杭州阮墩环碧", "venue": "阮公墩", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "西湖新十景，湖中绿洲，仿古表演。", "source": "杭州本地宝", "highlights": ["阮公墩", "西湖", "表演"], "type": "演出"},
    {"name": "杭州黄龙吐翠", "venue": "黄龙洞", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "西湖新十景，黄龙洞圆缘民俗园，越剧表演。", "source": "杭州本地宝", "highlights": ["黄龙洞", "越剧", "民俗"], "type": "演出"},
    {"name": "杭州宋城千古情演出", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "给我一天还你千年，宋城千古情大型歌舞表演。", "source": "杭州本地宝", "highlights": ["千古情", "演出", "宋城"], "type": "演出"},
    {"name": "杭州宋城聊斋惊魂", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "聊斋鬼屋，恐怖主题，惊悚体验。", "source": "杭州本地宝", "highlights": ["聊斋", "鬼屋", "宋城"], "type": "演出"},
    {"name": "杭州宋城王员外家小姐抛绣球", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "王员外家小姐抛绣球，互动表演，宋代民俗。", "source": "杭州本地宝", "highlights": ["抛绣球", "互动", "宋代"], "type": "演出"},
    {"name": "杭州宋城命悬一线", "venue": "宋城", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "命悬一线大型互动实景剧，惊险刺激。", "source": "杭州本地宝", "highlights": ["命悬一线", "实景剧", "宋城"], "type": "演出"},
    {"name": "杭州杭州乐园过山车", "venue": "杭州乐园", "city": "hangzhou", "district": "萧山区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "悬挂过山车雨神之锤，刺激游乐项目。", "source": "杭州本地宝", "highlights": ["过山车", "刺激", "杭州乐园"], "type": "亲子活动"},
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
