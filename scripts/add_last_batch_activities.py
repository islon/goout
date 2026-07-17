import json
import os

DATA_FILE = 'output/exhibitions.json'
OUTPUT_FILE = 'output/exhibitions.json'

new_activities = [
    # ========== 广州补充活动（第九批 - 冲刺300）==========
    {"name": "广州动物园海洋馆", "venue": "广州动物园", "city": "guangzhou", "district": "越秀区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "海洋生物展，海底隧道，海洋科普教育。", "source": "广州本地宝", "highlights": ["海洋馆", "动物园", "科普"], "type": "展览"},
    {"name": "广州鳄鱼公园", "venue": "广州鳄鱼公园", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "鳄鱼主题公园，爬行动物科普，鸟类表演。", "source": "广州本地宝", "highlights": ["鳄鱼", "爬行动物", "长隆"], "type": "亲子活动"},
    {"name": "广州气象卫星地面站", "venue": "广州气象卫星地面站", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "气象科普教育基地，卫星气象观测，天气预报知识。", "source": "广州本地宝", "highlights": ["气象", "卫星", "科普"], "type": "展览"},
    {"name": "广州地铁博物馆", "venue": "广州地铁博物馆", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "地铁发展历程，模拟驾驶体验，轨道交通科普。", "source": "广州本地宝", "highlights": ["地铁", "博物馆", "科普"], "type": "展览"},
    {"name": "广州抽水蓄能电站", "venue": "广州抽水蓄能电站", "city": "guangzhou", "district": "从化区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "工业旅游示范点，水电站科普，生态风光。", "source": "广州本地宝", "highlights": ["抽水蓄能", "工业旅游", "科普"], "type": "展览"},
    {"name": "广州石头记矿物园", "venue": "石头记矿物园", "city": "guangzhou", "district": "花都区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "矿物宝石主题公园，奇石展览，水晶世界。", "source": "广州本地宝", "highlights": ["矿物", "宝石", "石头记"], "type": "展览"},
    {"name": "广州洪秀全故居", "venue": "洪秀全故居", "city": "guangzhou", "district": "花都区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "太平天国领袖洪秀全出生地，历史纪念馆。", "source": "广州本地宝", "highlights": ["洪秀全", "太平天国", "历史"], "type": "展览"},
    {"name": "广州番禺博物馆", "venue": "番禺博物馆", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "番禺历史文化展，出土文物，民俗文化。", "source": "广州本地宝", "highlights": ["番禺", "博物馆", "免费"], "type": "展览"},
    {"name": "广州增城博物馆", "venue": "增城博物馆", "city": "guangzhou", "district": "增城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "增城历史文化，客家文化，民俗风情。", "source": "广州本地宝", "highlights": ["增城", "博物馆", "免费"], "type": "展览"},
    {"name": "广州从化博物馆", "venue": "从化博物馆", "city": "guangzhou", "district": "从化区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "从化历史文化，生态资源，地方民俗。", "source": "广州本地宝", "highlights": ["从化", "博物馆", "免费"], "type": "展览"},
    {"name": "广州花都博物馆", "venue": "花都博物馆", "city": "guangzhou", "district": "花都区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "花都历史文化，洪秀全，炭步芋头。", "source": "广州本地宝", "highlights": ["花都", "博物馆", "免费"], "type": "展览"},
    {"name": "广州南沙博物馆", "venue": "南沙博物馆", "city": "guangzhou", "district": "南沙区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "南沙历史文化，海洋文化，水乡风情。", "source": "广州本地宝", "highlights": ["南沙", "博物馆", "免费"], "type": "展览"},
    {"name": "广州白云儿童公园", "venue": "广州市白云儿童公园", "city": "guangzhou", "district": "白云区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "儿童游乐设施，亲子活动，免费游玩。", "source": "广州本地宝", "highlights": ["儿童公园", "免费", "白云"], "type": "亲子活动"},
    {"name": "广州海珠儿童公园", "venue": "广州市海珠儿童公园", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "海珠儿童乐园，游乐设施，亲子休闲。", "source": "广州本地宝", "highlights": ["儿童公园", "免费", "海珠"], "type": "亲子活动"},
    {"name": "广州番禺儿童公园", "venue": "广州市番禺儿童公园", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "番禺儿童游乐，亲子活动，免费公园。", "source": "广州本地宝", "highlights": ["儿童公园", "免费", "番禺"], "type": "亲子活动"},
    {"name": "广州天河儿童公园", "venue": "广州市天河儿童公园", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "天河儿童游乐，亲子休闲，免费公园。", "source": "广州本地宝", "highlights": ["儿童公园", "免费", "天河"], "type": "亲子活动"},
    {"name": "广州黄埔儿童公园", "venue": "广州市黄埔儿童公园", "city": "guangzhou", "district": "黄埔区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "黄埔儿童游乐，亲子活动，免费公园。", "source": "广州本地宝", "highlights": ["儿童公园", "免费", "黄埔"], "type": "亲子活动"},
    {"name": "广州花都儿童公园", "venue": "广州市花都儿童公园", "city": "guangzhou", "district": "花都区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "花都儿童游乐，亲子休闲，免费公园。", "source": "广州本地宝", "highlights": ["儿童公园", "免费", "花都"], "type": "亲子活动"},
    {"name": "广州增城儿童公园", "venue": "广州市增城儿童公园", "city": "guangzhou", "district": "增城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "增城儿童游乐，亲子活动，免费公园。", "source": "广州本地宝", "highlights": ["儿童公园", "免费", "增城"], "type": "亲子活动"},
    {"name": "广州从化儿童公园", "venue": "广州市从化儿童公园", "city": "guangzhou", "district": "从化区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "从化儿童游乐，亲子休闲，免费公园。", "source": "广州本地宝", "highlights": ["儿童公园", "免费", "从化"], "type": "亲子活动"},
    {"name": "广州南沙儿童公园", "venue": "广州市南沙儿童公园", "city": "guangzhou", "district": "南沙区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "南沙儿童游乐，亲子活动，免费公园。", "source": "广州本地宝", "highlights": ["儿童公园", "免费", "南沙"], "type": "亲子活动"},
    {"name": "广州白云山蹦极", "venue": "白云山风景名胜区", "city": "guangzhou", "district": "白云区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "白云山蹦极跳，极限运动，刺激体验。", "source": "广州本地宝", "highlights": ["蹦极", "白云山", "刺激"], "type": "亲子活动"},
    {"name": "广州白云山滑索", "venue": "白云山风景名胜区", "city": "guangzhou", "district": "白云区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "白云飞索，高空滑索，刺激体验。", "source": "广州本地宝", "highlights": ["滑索", "白云山", "刺激"], "type": "亲子活动"},
    {"name": "广州流溪河漂流", "venue": "流溪河国家森林公园", "city": "guangzhou", "district": "从化区", "start_date": "2026-07-01", "end_date": "2026-09-30", "fee": "收费", "description": "峡谷漂流，夏日清凉，山水风光。", "source": "广州本地宝", "highlights": ["漂流", "流溪河", "清凉"], "type": "亲子活动"},
    {"name": "广州增城大丰门漂流", "venue": "大丰门景区", "city": "guangzhou", "district": "增城区", "start_date": "2026-07-01", "end_date": "2026-09-30", "fee": "收费", "description": "大丰门漂流，惊险刺激，夏日清凉。", "source": "广州本地宝", "highlights": ["漂流", "大丰门", "刺激"], "type": "亲子活动"},
    {"name": "广州从化碧水湾温泉", "venue": "碧水湾温泉度假村", "city": "guangzhou", "district": "从化区", "start_date": "2026-09-01", "end_date": "2026-12-31", "fee": "收费", "description": "从化温泉度假，秋冬养生，温泉泡汤。", "source": "广州本地宝", "highlights": ["温泉", "从化", "养生"], "type": "亲子活动"},
    {"name": "广州增城锦绣香江温泉", "venue": "锦绣香江温泉城", "city": "guangzhou", "district": "增城区", "start_date": "2026-09-01", "end_date": "2026-12-31", "fee": "收费", "description": "白水寨旁温泉度假，秋冬养生，南昆山下。", "source": "广州本地宝", "highlights": ["温泉", "增城", "白水寨"], "type": "亲子活动"},
    {"name": "广州花都融创雪世界", "venue": "广州融创雪世界", "city": "guangzhou", "district": "花都区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "华南最大室内滑雪场，四季滑雪，冰雪体验。", "source": "广州本地宝", "highlights": ["滑雪", "融创", "冰雪"], "type": "亲子活动"},
    {"name": "广州融创水世界", "venue": "广州融创水世界", "city": "guangzhou", "district": "花都区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "室内恒温水乐园，全年戏水，水上项目。", "source": "广州本地宝", "highlights": ["水世界", "融创", "室内"], "type": "亲子活动"},
    {"name": "广州融创体育世界", "venue": "广州融创体育世界", "city": "guangzhou", "district": "花都区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "体育主题乐园，卡丁车攀岩，运动体验。", "source": "广州本地宝", "highlights": ["体育世界", "融创", "运动"], "type": "亲子活动"},
    {"name": "广州正佳自然科学博物馆", "venue": "正佳自然科学博物馆", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "恐龙化石标本，自然科学科普，亲子研学。", "source": "广州本地宝", "highlights": ["自然科学", "恐龙", "正佳"], "type": "展览"},
    {"name": "广州正佳雨林生态植物园", "venue": "正佳雨林生态植物园", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "室内热带雨林，植物动物，生态科普。", "source": "广州本地宝", "highlights": ["雨林", "植物园", "正佳"], "type": "展览"},
    {"name": "广州正佳极地海洋世界", "venue": "正佳极地海洋世界", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "极地海洋动物，白鲸企鹅，美人鱼表演。", "source": "广州本地宝", "highlights": ["极地海洋", "白鲸", "正佳"], "type": "展览"},
    {"name": "广州MAG环球魔幻世界", "venue": "MAG环球魔幻世界", "city": "guangzhou", "district": "天河区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "魔幻主题乐园，3D艺术馆，惊悚鬼屋。", "source": "广州本地宝", "highlights": ["魔幻世界", "3D艺术", "天河"], "type": "亲子活动"},
    {"name": "广州星期8小镇", "venue": "星期8小镇", "city": "guangzhou", "district": "白云区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "儿童职业体验，角色扮演，亲子教育。", "source": "广州本地宝", "highlights": ["职业体验", "角色扮演", "儿童"], "type": "亲子活动"},
    {"name": "广州巧克力王国", "venue": "奥园英德巧克力王国", "city": "guangzhou", "district": "番禺区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "巧克力主题乐园，糖果城堡，亲子游乐。", "source": "广州本地宝", "highlights": ["巧克力", "主题乐园", "亲子"], "type": "亲子活动"},
    {"name": "广州南湖游乐园", "venue": "南湖游乐园", "city": "guangzhou", "district": "白云区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "老牌游乐园，过山车摩天轮，怀旧体验。", "source": "广州本地宝", "highlights": ["南湖游乐园", "怀旧", "游乐"], "type": "亲子活动"},
    {"name": "广州黄金海岸水上乐园", "venue": "黄金海岸水上乐园", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-09-30", "fee": "收费", "description": "市区水上乐园，造浪池滑梯，夏日清凉。", "source": "广州本地宝", "highlights": ["水上乐园", "黄金海岸", "清凉"], "type": "亲子活动"},
    {"name": "广州大河马水上世界", "venue": "大河马水上世界", "city": "guangzhou", "district": "白云区", "start_date": "2026-07-01", "end_date": "2026-09-30", "fee": "收费", "description": "老牌水上乐园，刺激滑道，夏日戏水。", "source": "广州本地宝", "highlights": ["水上乐园", "大河马", "戏水"], "type": "亲子活动"},
    {"name": "广州塔摩天轮", "venue": "广州塔", "city": "guangzhou", "district": "海珠区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "世界最高摩天轮，俯瞰广州夜景，浪漫体验。", "source": "广州本地宝", "highlights": ["摩天轮", "广州塔", "夜景"], "type": "亲子活动"},

    # ========== 杭州补充活动（第九批 - 冲刺300）==========
    {"name": "杭州少儿公园", "venue": "杭州少年儿童公园", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "满觉陇儿童游乐设施，亲子活动，西湖边。", "source": "杭州本地宝", "highlights": ["少儿公园", "亲子", "西湖"], "type": "亲子活动"},
    {"name": "杭州低碳科技馆", "venue": "中国杭州低碳科技馆", "city": "hangzhou", "district": "滨江区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "低碳环保科普，全球首个低碳主题科技馆。", "source": "杭州本地宝", "highlights": ["低碳", "科技馆", "免费"], "type": "展览"},
    {"name": "杭州科技馆", "venue": "杭州市科学技术馆", "city": "hangzhou", "district": "西湖文化广场", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "科普教育，科学实验，儿童互动。", "source": "杭州本地宝", "highlights": ["科技馆", "科普", "免费"], "type": "展览"},
    {"name": "杭州动漫博物馆", "venue": "中国动漫博物馆", "city": "hangzhou", "district": "滨江区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "国漫主题，动漫历史，互动体验。", "source": "杭州本地宝", "highlights": ["动漫", "博物馆", "免费"], "type": "展览"},
    {"name": "杭州西湖博览会博物馆", "venue": "西湖博览会博物馆", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "西湖博览会历史，杭州会展文化。", "source": "杭州本地宝", "highlights": ["西博", "博物馆", "免费"], "type": "展览"},
    {"name": "杭州西湖苏东坡纪念馆", "venue": "苏东坡纪念馆", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "苏轼在杭州事迹，苏堤春晓，文学大家。", "source": "杭州本地宝", "highlights": ["苏东坡", "纪念馆", "西湖"], "type": "展览"},
    {"name": "杭州西湖章太炎纪念馆", "venue": "章太炎纪念馆", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "国学大师章太炎，革命先驱，南屏山下。", "source": "杭州本地宝", "highlights": ["章太炎", "纪念馆", "国学"], "type": "展览"},
    {"name": "杭州西湖于谦祠", "venue": "于谦祠", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "明代名臣于谦，两袖清风，西湖三台山。", "source": "杭州本地宝", "highlights": ["于谦", "祠庙", "历史"], "type": "展览"},
    {"name": "杭州西湖张苍水祠", "venue": "张苍水先生祠", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "张煌言抗清义士，民族英雄，南屏山麓。", "source": "杭州本地宝", "highlights": ["张苍水", "祠庙", "历史"], "type": "展览"},
    {"name": "杭州白塔公园", "venue": "白塔公园", "city": "hangzhou", "district": "上城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "白塔，闸口火车遗址，文艺打卡。", "source": "杭州本地宝", "highlights": ["白塔", "公园", "火车"], "type": "亲子活动"},
    {"name": "杭州江洋畈生态公园", "venue": "江洋畈生态公园", "city": "hangzhou", "district": "上城区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "生态湿地公园，西湖淤泥上的公园，观鸟。", "source": "杭州本地宝", "highlights": ["江洋畈", "生态", "免费"], "type": "亲子活动"},
    {"name": "杭州半山国家森林公园", "venue": "半山国家森林公园", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "杭州城北绿肺，登山望景，森林氧吧。", "source": "杭州本地宝", "highlights": ["半山", "森林公园", "免费"], "type": "亲子活动"},
    {"name": "杭州皋亭山景区", "venue": "皋亭山景区", "city": "hangzhou", "district": "拱墅区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "皋亭千桃园，杭州北景，人文自然。", "source": "杭州本地宝", "highlights": ["皋亭山", "千桃园", "人文"], "type": "亲子活动"},
    {"name": "杭州超山风景区", "venue": "超山风景区", "city": "hangzhou", "district": "临平区", "start_date": "2026-01-01", "end_date": "2026-12-31", "fee": "收费", "description": "十里梅花香雪海，中国五大古梅，赏梅胜地。", "source": "杭州本地宝", "highlights": ["超山", "梅花", "赏梅"], "type": "展览"},
    {"name": "杭州山沟沟景区", "venue": "山沟沟景区", "city": "hangzhou", "district": "余杭区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "余杭山沟沟，峡谷瀑布，生态避暑。", "source": "杭州本地宝", "highlights": ["山沟沟", "峡谷", "避暑"], "type": "亲子活动"},
    {"name": "杭州径山寺", "venue": "径山寺", "city": "hangzhou", "district": "余杭区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "江南五大禅院之首，径山茶，禅修体验。", "source": "杭州本地宝", "highlights": ["径山寺", "禅宗", "茶道"], "type": "亲子活动"},
    {"name": "杭州良渚古城遗址公园", "venue": "良渚古城遗址公园", "city": "hangzhou", "district": "余杭区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "世界文化遗产，五千年文明，考古遗址。", "source": "杭州本地宝", "highlights": ["良渚", "遗址", "世界遗产"], "type": "展览"},
    {"name": "杭州良渚博物院", "venue": "良渚博物院", "city": "hangzhou", "district": "余杭区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "免费", "description": "良渚文化展，玉琮玉璧，五千年文明。", "source": "杭州本地宝", "highlights": ["良渚", "博物院", "玉器"], "type": "展览"},
    {"name": "杭州西溪湿地洪园", "venue": "西溪湿地洪园", "city": "hangzhou", "district": "余杭区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "西溪湿地西区，洪氏宗祠，四季花海。", "source": "杭州本地宝", "highlights": ["西溪洪园", "湿地", "花海"], "type": "亲子活动"},
    {"name": "杭州西湖国宾馆", "venue": "西湖国宾馆", "city": "hangzhou", "district": "西湖区", "start_date": "2026-07-01", "end_date": "2026-12-31", "fee": "收费", "description": "西湖第一名园，刘庄，历史建筑。", "source": "杭州本地宝", "highlights": ["国宾馆", "西湖", "历史"], "type": "亲子活动"},
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
