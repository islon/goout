import json
import os

existing_file = '/workspace/goout/output/raw/real_activities_guangzhou.json'
output_file = '/workspace/goout/output/raw/real_activities_guangzhou_batch2.json'

with open(existing_file, 'r', encoding='utf-8') as f:
    existing_activities = json.load(f)

existing_titles = set(act['title'] for act in existing_activities)

new_activities = [
    {
        "title": "越秀木棉红——越秀山红色史迹研学活动",
        "venue": "广州博物馆（镇海楼展区）、越秀公园",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1047996829_121107011/",
        "description": "由宣教人员带领学员在户外定向沉浸式寻觅越秀山上的红色史迹。学员化身报社记者等不同角色，通过音视频讲解、展厅参观等方式，结合线上小程序、线下游戏道具卡等素材，对越秀山上的红色史迹一一探访。",
        "fee": "免费需预约",
        "source": "广州博物馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "\"决战观音山\"剧本杀活动",
        "venue": "广州博物馆（镇海楼展区）、越秀公园",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1047996829_121107011/",
        "description": "以1927年广州起义历史事件为基础，依托剧本杀的形式，活化利用镇海楼展区及其周边观音山战斗遗址、四方炮台等史迹点，学员分饰不同角色，完成每一项任务，在沉浸式实景游戏中感悟革命先烈不屈不挠、舍生取义的奋斗精神。",
        "fee": "免费需预约",
        "source": "广州博物馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "\"清代广州人的一天\"主题研学活动",
        "venue": "广州博物馆（镇海楼展区）专题展厅",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-23",
        "link": "https://m.sohu.com/a/1047996829_121107011/",
        "description": "围绕\"海丝门户——文物里的清代广州\"展览，设计主题研学手册，青少年或亲子家庭可在外销画、通草水彩画、老物件等珍贵文物中寻找隐藏线索，破解趣味谜题，揭开珠江航运、十三行商贸、传统百工、桑茶技艺、非遗节庆、粤剧文化的神秘面纱。",
        "fee": "免费",
        "source": "广州博物馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "鳌越山海--鳌鱼挂饰制作研学活动",
        "venue": "广州博物馆（镇海楼展区）",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1047996829_121107011/",
        "description": "立足广州博物馆馆藏明代石湾窑三彩鳌鱼，由讲解员带领学员沉浸式了解馆藏文物，开展研学讲解。在沉浸式非遗实操环节——鳌鱼手工挂饰DIY活动中，指导学员勾勒鳌鱼形态，复刻文物经典配色，最后进行缝制，亲手打造专属鳌鱼挂饰。",
        "fee": "免费需预约",
        "source": "广州博物馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "陨石坑小夜灯DIY活动",
        "venue": "广州博物馆（镇海楼展区）",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1047996829_121107011/",
        "description": "通过科普类手工制作，把陨石撞击的\"暴力美学\"转化为柔和浪漫的小夜灯，让学员在动手实践中了解天文知识，感受宇宙的奇妙。",
        "fee": "免费需预约",
        "source": "广州博物馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "星火启程——从农讲所到天安门文物展",
        "venue": "农讲所纪念馆",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.gz.gov.cn/zlgz/whgz/content/mpost_10898120.html",
        "description": "集中呈现农讲所纪念馆自2023年启动\"历届教员学员足迹寻访项目\"以来的成果，展出藏品118件（其中珍贵文物72件），79件为近年来征集，单次集中展出文物数量为近十年之最。",
        "fee": "免费需预约",
        "source": "广州日报、广州市人民政府官网",
        "family_friendly": True
    },
    {
        "title": "救民水火——纪念国民革命军一百周年展",
        "venue": "黄埔军校旧址纪念馆",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.gz.gov.cn/zlgz/whgz/content/mpost_10898120.html",
        "description": "展览展出著名的《北伐画史》，这部1928年出版的良友杂志特刊登载了广州摄影师黄英随军北伐征途中拍摄的376幅照片。另一件重要展品《北伐途次》作者为郭沫若，讲述了国民革命军将士浴血奋战的英勇事迹。",
        "fee": "免费需预约",
        "source": "广州日报、广州市人民政府官网",
        "family_friendly": True
    },
    {
        "title": "开国上将 红色诗人——萧华同志的革命风范与长征记忆展览",
        "venue": "广州起义纪念馆",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.gz.gov.cn/zlgz/whgz/content/mpost_10898120.html",
        "description": "结合解放战争时期萧华用过的军毯、萧华出访东欧时穿过的大衣、萧华夫人王新兰回顾萧华创作《长征组歌》的手稿等珍贵文物和资料，深度解读《长征组歌》，通过主题油画、艺术场景、多媒体演绎等形式，还原长征重大历史场景。",
        "fee": "免费需预约",
        "source": "广州日报、广州市人民政府官网",
        "family_friendly": True
    },
    {
        "title": "微观万相——青海热贡唐卡数字艺术特展",
        "venue": "广州人民艺术中心1号馆",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.gz.gov.cn/zlgz/whgz/content/mpost_10898120.html",
        "description": "集中呈现青海热贡地区唐卡艺术的经典之作与数字化创新成果。2009年，热贡艺术被列入联合国教科文组织人类非物质文化遗产代表作名录。展览提供全套数字化观展服务：所有展品都可以扫码听数字语音讲解。",
        "fee": "免费需预约",
        "source": "广州日报、广州市人民政府官网",
        "family_friendly": True
    },
    {
        "title": "花漾穆夏：新艺术美学漫步慢闪体验",
        "venue": "广州人民艺术中心",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://www.gz.gov.cn/zlgz/whgz/content/mpost_10898120.html",
        "description": "观众在逛展的间隙，将偶遇翩翩白鸽、优雅曲线与绚烂窗花，并观赏其经典的代表原作，赴一场百年美学的跨界漫步。此次体验特别甄选穆夏的10余幅接近130年历史的石版画原作，观众可近距离探寻这位\"造梦师\"如何将自然诗性\"人格化\"。",
        "fee": "收费",
        "source": "广州日报、广州市人民政府官网",
        "family_friendly": True
    },
    {
        "title": "豆荚宝宝儿童音乐会《淘气旅行箱》",
        "venue": "星海音乐厅",
        "city": "guangzhou",
        "start_date": "2026-07-19",
        "end_date": "2026-07-20",
        "link": "http://book.newdu.com/m/view.php?aid=147283",
        "description": "朱宗庆打击乐团2打造的豆荚宝宝儿童音乐会，带领小朋友一同游历五大洲、七个地方，将各地特殊风情及世界音乐的奥妙尽收\"耳\"底。音乐会中编排了多首大小朋友耳熟能详的童谣，如《造飞机》《小印第安人》《两只老虎》等。",
        "fee": "收费",
        "source": "广州日报、新读网",
        "family_friendly": True
    },
    {
        "title": "音乐启蒙亲子剧《小蒲公英奇妙之旅》国风版",
        "venue": "星海音乐厅音乐空间",
        "city": "guangzhou",
        "start_date": "2026-07-18",
        "end_date": "2026-07-18",
        "link": "http://m.toutiao.com/group/7661995908999365163/",
        "description": "星海音乐厅出品的音乐启蒙亲子剧国风升级版，以传统八音中的\"丝\"为起点，通过\"小英\"和\"阿布\"两位主角的冒险故事，将传统五声音阶与节奏念白巧妙融入剧情。精选《落雨大》《彩云追月》《旱天雷》等广东音乐与广府童谣。",
        "fee": "收费",
        "source": "广州日报、今日头条",
        "family_friendly": True
    },
    {
        "title": "百老汇经典布偶绘本剧《好饿的毛毛虫秀》",
        "venue": "广州大剧院实验剧场",
        "city": "guangzhou",
        "start_date": "2026-07-23",
        "end_date": "2026-07-28",
        "link": "http://book.newdu.com/m/view.php?aid=147283",
        "description": "中国内地首演，用75只手工打造的可爱动物偶，串联起4本经典绘本——《好饿的毛毛虫》《棕色的熊，棕色的熊，你在看什么》《10只橡皮小鸭》《好寂寞的萤火虫》，让故事书变成真实场景。",
        "fee": "收费",
        "source": "广州日报、新读网",
        "family_friendly": True
    },
    {
        "title": "台湾纸风车剧团儿童剧《纸风车幻想曲》",
        "venue": "广州大剧院",
        "city": "guangzhou",
        "start_date": "2026-07-26",
        "end_date": "2026-07-27",
        "link": "https://ebookpc.gzdjy.org/view.html?cid=0&id=15250",
        "description": "台湾第一儿童剧团纸风车剧团首次来穗，汇集剧团二十年经典剧目，包括活泼舞蹈肢体剧场\"动作与声音\"、视觉美学剧场\"小口袋\"、黑光交响诗\"欢乐中国节\"、黑光奇想剧场\"神奇黑光棒\"、生活情境剧\"起床号\"、改编自吴念真绘本的多媒体戏剧\"八岁一个人去旅行\"六个部分。",
        "fee": "收费",
        "source": "广州大剧院官网",
        "family_friendly": True
    },
    {
        "title": "广州大剧院\"陪你玩一夏\"七大免费艺文游戏",
        "venue": "广州大剧院售票中心大厅",
        "city": "guangzhou",
        "start_date": "2026-07-20",
        "end_date": "2026-08-17",
        "link": "https://ebookpc.gzdjy.org/view.html?cid=0&id=15250",
        "description": "连续五个礼拜逢星期六15:00-17:00，开展7个免费艺文小游戏：尤克里里教学、乐高游戏、旧物改造及创意手工、风筝绘画、胶画制作、弹力布cosplay、《亚当斯一家》拍照抽奖。集满印章可换礼品。",
        "fee": "免费",
        "source": "广州大剧院官网",
        "family_friendly": True
    },
    {
        "title": "丹麦互动亲子音乐会《节拍翻斗乐》",
        "venue": "广州大剧院",
        "city": "guangzhou",
        "start_date": "2026-08-15",
        "end_date": "2026-08-18",
        "link": "http://book.newdu.com/m/view.php?aid=147283",
        "description": "儿童版\"破铜烂铁STOMP\"，演出创始人之一彼得·斯塔夫伦·尼尔森曾是\"破铜烂铁\"中的鼓手。从最简单的节拍开始玩起，带领孩子们一步步走进音乐世界，最后让每个孩子一起加入，完成一场身体的\"交响乐\"。",
        "fee": "收费",
        "source": "广州日报、新读网",
        "family_friendly": True
    },
    {
        "title": "家庭音乐剧《故宫里的大怪兽之吻兽使命》",
        "venue": "广州大剧院歌剧厅",
        "city": "guangzhou",
        "start_date": "2026-08-16",
        "end_date": "2026-08-17",
        "link": "http://book.newdu.com/m/view.php?aid=147283",
        "description": "由热门童书《故宫里的大怪兽》作者常怡亲自操刀编剧，讲述一则关于故宫的奇幻故事。音乐人李猛打造15首歌曲，穿插猜灯谜、京剧水旗等传统文化元素。",
        "fee": "收费",
        "source": "广州日报、新读网",
        "family_friendly": True
    },
    {
        "title": "美国原版音乐舞台剧《汪汪队立大功-救援先锋》",
        "venue": "广州大剧院歌剧厅",
        "city": "guangzhou",
        "start_date": "2026-08-22",
        "end_date": "2026-08-25",
        "link": "http://book.newdu.com/m/view.php?aid=147283",
        "description": "七只英勇、充满活力的小狗组成的救援队，在机智勇敢、精通科技的10岁小男孩莱德队长带领下，一起保护镇上的居民。在生动的剧情中培养孩子的社会责任感和团队合作精神。",
        "fee": "收费",
        "source": "广州日报、新读网",
        "family_friendly": True
    },
    {
        "title": "德国托尔策童声合唱团音乐会",
        "venue": "广州大剧院",
        "city": "guangzhou",
        "start_date": "2026-08-24",
        "end_date": "2026-08-24",
        "link": "https://ebookpc.gzdjy.org/view.html?cid=0&id=15250",
        "description": "世界三大童声合唱团之一，建团半个多世纪以来一直坚持专业的男童美声训练。这支曾为罗马教皇唱诵、为德国足球世界杯开幕献声的合唱团，将以歌声为夏日送来一缕直抵心田的清凉。",
        "fee": "收费",
        "source": "广州大剧院官网",
        "family_friendly": True
    },
    {
        "title": "魔术剧《遗失光芒的灯泡头》",
        "venue": "广州大剧院",
        "city": "guangzhou",
        "start_date": "2026-08-30",
        "end_date": "2026-08-31",
        "link": "https://ebookpc.gzdjy.org/view.html?cid=0&id=15250",
        "description": "来自芬兰的独特幽默剧，集魔术、小丑戏、黑光艺术、视频特效等多种元素为一体。讲述一个无法再发光的灯泡，是否能找回原先的自己的神奇魔幻之旅。",
        "fee": "收费",
        "source": "广州大剧院官网",
        "family_friendly": True
    },
    {
        "title": "《阿里巴巴赫》0-3岁宝宝音乐会",
        "venue": "广州大剧院",
        "city": "guangzhou",
        "start_date": "2026-08-17",
        "end_date": "2026-08-18",
        "link": "https://ebookpc.gzdjy.org/view.html?cid=0&id=15250",
        "description": "葡萄牙CMT剧团带来，首次举办为0-3岁的宝宝和爸爸妈妈们量身打造的专属音乐会。现场特别设计互动环节，父母可藉此增进亲子交流，为宝宝进行艺术早教。",
        "fee": "收费",
        "source": "广州大剧院官网",
        "family_friendly": True
    },
    {
        "title": "音乐舞蹈亲子剧场《胡桃夹子》",
        "venue": "星海音乐厅",
        "city": "guangzhou",
        "start_date": "2026-08-16",
        "end_date": "2026-08-17",
        "link": "http://wglj.gz.gov.cn/attachment/7/7858/7858616/10385320.pdf",
        "description": "星海音乐厅出品的音乐舞蹈亲子剧场，将经典童话《胡桃夹子》以音乐与舞蹈结合的形式呈现，适合全家大小共同观赏的亲子剧目。",
        "fee": "收费",
        "source": "广州市文化广电旅游局",
        "family_friendly": True
    },
    {
        "title": "英国原版创意音乐光影儿童剧《巴赫梦幻之旅》",
        "venue": "广州大剧院",
        "city": "guangzhou",
        "start_date": "2026-08-09",
        "end_date": "2026-08-09",
        "link": "http://wglj.gz.gov.cn/attachment/7/7858/7858616/10385320.pdf",
        "description": "英国原版创意音乐光影儿童剧，带领孩子们走进巴赫的音乐世界，在创意光影与音乐中感受古典音乐的魅力。",
        "fee": "收费",
        "source": "广州市文化广电旅游局",
        "family_friendly": True
    },
    {
        "title": "从化营地儿童戏剧艺术节",
        "venue": "从化荔枝球乐园未来剧场",
        "city": "guangzhou",
        "start_date": "2026-07-19",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7662684426802856489/",
        "description": "融合治愈人偶童话、沉浸式5D飞行电影、爆笑粤语即兴喜剧、治愈合唱音乐会，多元舞台演出轮番上演。搭配园区游船、竹筏、桨板、皮划艇水上项目，白天玩水撒欢，傍晚观演沉浸。",
        "fee": "收费",
        "source": "荔枝球乐园、今日头条",
        "family_friendly": True
    },
    {
        "title": "《神奇兔妈》儿童人偶剧",
        "venue": "从化荔枝球乐园未来剧场",
        "city": "guangzhou",
        "start_date": "2026-07-19",
        "end_date": "2026-07-19",
        "link": "http://m.toutiao.com/group/7662684426802856489/",
        "description": "专为3-10岁小朋友打造，用软萌人偶演绎细腻母爱。故事围绕亲子日常展开，讲述总被唠叨的兔妈妈，在小兔子的奇幻冒险里揭开温柔底色。现场超多近距离互动，引导孩子理解妈妈藏在唠叨里的深爱。",
        "fee": "收费",
        "source": "荔枝球乐园、今日头条",
        "family_friendly": True
    },
    {
        "title": "《青蛙王子》儿童人偶剧",
        "venue": "从化荔枝球乐园未来剧场",
        "city": "guangzhou",
        "start_date": "2026-08-02",
        "end_date": "2026-08-02",
        "link": "http://m.toutiao.com/group/7662684426802856489/",
        "description": "被魔法束缚的青蛙王子，等待真诚的友谊解除诅咒。华丽舞美搭配鲜活人偶角色，80分钟完整剧情跌宕有趣，演员会走下舞台和小朋友互动。教会孩子真诚待人、珍惜真挚情谊。",
        "fee": "收费",
        "source": "荔枝球乐园、今日头条",
        "family_friendly": True
    },
    {
        "title": "《三只小猪》儿童人偶剧",
        "venue": "从化荔枝球乐园未来剧场",
        "city": "guangzhou",
        "start_date": "2026-08-16",
        "end_date": "2026-08-16",
        "link": "http://m.toutiao.com/group/7662684426802856489/",
        "description": "家喻户晓的经典童话全新舞台改编！三只性格迥异的小猪，和大灰狼斗智斗勇。现场设置上台游戏、问答送礼、亲子互动环节，在欢声笑语中告诉孩子勤劳踏实、团结协作的力量。",
        "fee": "收费",
        "source": "荔枝球乐园、今日头条",
        "family_friendly": True
    },
    {
        "title": "广州海洋馆\"动物探险家三日夏令营\"",
        "venue": "广州海洋馆、广州动物园",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.mp.oeeee.com/oe/BAAFRD0000202606261615594.html",
        "description": "广州海洋馆与广州动物园梦幻联动，全新推出\"动物探险家三日夏令营\"，一连三天行程让孩子探秘双园秘境，解锁海陆空生物奥秘。推出双园暑期特惠，最低6.5折。",
        "fee": "收费",
        "source": "南方都市报、南都N视频",
        "family_friendly": True
    },
    {
        "title": "广州海洋馆奥飞娱乐IP主题活动",
        "venue": "广州海洋馆",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.mp.oeeee.com/oe/BAAFRD0000202606261615594.html",
        "description": "奥飞娱乐四大人气动漫IP暑期强势助阵，特色巡游、主题舞蹈等精彩活动轮番上演，为游客带来沉浸式互动狂欢。全新科普魔术秀以剧目形式生动传递海洋环保理念。",
        "fee": "收费",
        "source": "南方都市报、南都N视频",
        "family_friendly": True
    },
    {
        "title": "广州海洋馆夏日泡泡大战亲子捞鱼活动",
        "venue": "广州海洋馆",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.mp.oeeee.com/oe/BAAFRD0000202606261615594.html",
        "description": "亲子捞鱼、夏日泡泡大战等清凉亲水项目，为游客带来清爽欢快的夏日玩水体验。园区科普体验同步升级，科普互动墙焕新登场、淡水龟展示区全新开放。",
        "fee": "收费",
        "source": "南方都市报、南都N视频",
        "family_friendly": True
    },
    {
        "title": "\"堂小青\"第五期爱绿护绿志愿讲解员培训",
        "venue": "广州动物园、中山纪念堂",
        "city": "guangzhou",
        "start_date": "2026-07-14",
        "end_date": "2026-07-17",
        "link": "https://m.sohu.com/a/1048079217_121106875/",
        "description": "以\"生态+人文+科技+艺术\"的全新升级模式，四天沉浸式研学，涵盖夜间自然观察、动物园模拟讲解、VR潜艇与4D台风体验、无人机实操与机器人PK等跨维度课程。考核合格者可获聘书并正式加入服务队。",
        "fee": "免费需预约",
        "source": "广东林业、搜狐网",
        "family_friendly": True
    },
    {
        "title": "白云山明珠楼景区亲子戏水活动",
        "venue": "白云山风景名胜区明珠楼景区",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://huacheng.gz-cmc.com/pages/2026/07/15/ffee37a15b5942a0abac5c11989c2f49.html",
        "description": "明珠楼景区浅滩适配日常亲子休闲戏水，是市区亲子遛娃的好去处。",
        "fee": "收费",
        "source": "广州日报新花城",
        "family_friendly": True
    },
    {
        "title": "白云山麓湖景区水上运动嘉年华",
        "venue": "白云山风景名胜区麓湖景区",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://huacheng.gz-cmc.com/pages/2026/07/15/ffee37a15b5942a0abac5c11989c2f49.html",
        "description": "精心准备了热血飒爽的龙舟体验、温情治愈的皮划艇、悠闲自在的水上自行车、潮流刺激的桨板运动等，全龄段趣味玩法悉数上线。",
        "fee": "收费",
        "source": "广州日报新花城",
        "family_friendly": True
    },
    {
        "title": "广州市儿童公园暑期玩水活动",
        "venue": "广州市儿童公园",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://huacheng.gz-cmc.com/pages/2026/07/15/ffee37a15b5942a0abac5c11989c2f49.html",
        "description": "三大玩水片区全面开启，打造龙舟戏水乐园、海洋童趣戏水区与旱喷广场，是市区遛娃的好去处。",
        "fee": "免费",
        "source": "广州日报新花城",
        "family_friendly": True
    },
    {
        "title": "\"志愿童行\"文化艺术公益夏令营",
        "venue": "广东省文化馆、广州市文化馆等",
        "city": "guangzhou",
        "start_date": "2026-08-08",
        "end_date": "2026-08-15",
        "link": "https://m.sohu.com/a/1051621921_121106875/",
        "description": "广东省文化馆联动省市级公共文化场馆，以\"暑假当然来广东·游学\"为主题，策划文化、图书、博物、美术历史、非遗、考古、科技、音乐8条主题游学线路，推出亲子公益夏令营活动。",
        "fee": "免费需预约",
        "source": "广东省文化馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "虫篆·微观奇境——昆虫科普艺术游园会",
        "venue": "广东省文化馆",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1051621921_121106875/",
        "description": "以昆虫为纽带，有机融合科普教育、艺术创作与互动体验，配套科普分享会等活动，带领大家在轻松的氛围中触摸昆虫世界的鲜活与奇妙。",
        "fee": "免费需预约",
        "source": "广东省文化馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "传统香囊缝制亲子课程",
        "venue": "广东省文化馆",
        "city": "guangzhou",
        "start_date": "2026-07-26",
        "end_date": "2026-07-26",
        "link": "http://m.toutiao.com/group/7662310679189340710/",
        "description": "\"银龄联萌\"艺术学堂课程，1位成人+1位儿童组合报名。一针一线传承古韵风华，学习古法香囊缝制技艺，裁剪精美布料、穿针引线缝合、装填天然清香香料。成品既可随身佩戴驱蚊纳福，也能当作家居装饰。",
        "fee": "免费需预约",
        "source": "广东省文化馆、今日头条",
        "family_friendly": True
    },
    {
        "title": "正佳自然科学博物馆小小讲解员成长研学营",
        "venue": "正佳自然科学博物馆",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://cloud.kepuchina.cn/h5/detail?id=7448127079778914304",
        "description": "课程涵盖恐龙、甲骨、青铜三大主题，金牌讲师一对一带教，全方位提升孩子的语言表达、逻辑思维与自信心。通过互动教学、实景演练，让孩子在轻松愉悦的氛围中掌握讲解技巧。",
        "fee": "收费",
        "source": "科普中国、广东省科学技术协会",
        "family_friendly": True
    },
    {
        "title": "正佳自然科学博物馆巨虫森林探秘活动",
        "venue": "正佳自然科学博物馆",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1051621921_121106875/",
        "description": "在导师带领下穿越46亿年时光，探秘\"巨虫森林\"，了解石炭纪巨型生物的秘密，触摸鬃狮蜥、巨型马陆等活体萌宠，感受生命的多样与温度。化身\"小小化石清修师\"，体验修复三叶虫化石。",
        "fee": "收费",
        "source": "广东省文化馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "越王者旨於睗剑特展",
        "venue": "正佳中华文明探索馆",
        "city": "guangzhou",
        "start_date": "2026-06-13",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7650854135360799275/",
        "description": "流失海外多年的重量级国宝\"越王者旨於睗剑\"正式亮相广州。这把战国早期青铜宝剑为越王勾践之子鹿郢的自用佩剑，被誉为历年所见品相最好的者旨於睗剑之一。配合展览推出沉浸式公众活动。",
        "fee": "收费",
        "source": "羊城晚报、今日头条",
        "family_friendly": True
    },
    {
        "title": "第四届正佳星球动漫狂欢节",
        "venue": "正佳广场",
        "city": "guangzhou",
        "start_date": "2026-07-10",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7661173680902308388/",
        "description": "以\"G-Fest动漫狂欢节2026·次元英雄季\"为主题，全程持续至8月31日。超20个阵营、千名COSER全员集结，ACG摇滚现场、随机宅舞大赛、水幕摇滚LIVE、ONLY主题巡游等轮番来袭。",
        "fee": "免费",
        "source": "今日头条",
        "family_friendly": True
    },
    {
        "title": "蜘蛛侠巨型气模与蜘蛛科普展",
        "venue": "正佳广场、正佳自然科学博物馆",
        "city": "guangzhou",
        "start_date": "2026-07-17",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7661173680902308388/",
        "description": "广州唯一的漫威蜘蛛侠巨型气模落地正佳广场东南门，正佳自然科学博物馆内更有真实的巴西所罗门捕鸟蛛，实现虚拟英雄与现实生物的奇妙碰撞。正佳自然科学博物馆联动《万物》杂志打造华南首个线下主题阅读区。",
        "fee": "收费",
        "source": "今日头条",
        "family_friendly": True
    },
    {
        "title": "海珠区少年儿童图书馆STEM科普小课堂",
        "venue": "海珠区少年儿童图书馆",
        "city": "guangzhou",
        "start_date": "2026-07-18",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1050221299_121106875/",
        "description": "STEM科普小课堂系列活动，如第168期幻灯投影机DIY课，讲解凸透镜成像原理，孩子用KT板、凸透镜等材料组装，边做边懂光学奥秘，科学性与趣味性并重。",
        "fee": "免费需预约",
        "source": "广州市海珠区图书馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "海珠区少年儿童图书馆趣读英语活动",
        "venue": "海珠区少年儿童图书馆",
        "city": "guangzhou",
        "start_date": "2026-07-18",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1050221299_121106875/",
        "description": "领读英文绘本，用小游戏引导孩子认识树的作用和重要性，引导孩子树立保护环境的意识，同时进行英语启蒙。适合3-6岁亲子家庭。",
        "fee": "免费需预约",
        "source": "广州市海珠区图书馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "\"盛世榴芳耀中华\"主题绘画活动",
        "venue": "广州少年儿童图书馆童趣馆",
        "city": "guangzhou",
        "start_date": "2026-07-12",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1048572380_121106875/",
        "description": "以\"盛世榴芳\"系列民族主题油画、非遗版画展为审美启蒙，以原创民族美育绘本《盛世榴芳耀中华》为创作载体，通过\"共读+涂色\"的沉浸式亲子实践，引导家庭在色彩互动中感知艺术魅力。",
        "fee": "免费需预约",
        "source": "广州少年儿童图书馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "快乐读出英语力亲子活动",
        "venue": "广州少年儿童图书馆二楼外文馆",
        "city": "guangzhou",
        "start_date": "2026-07-18",
        "end_date": "2026-08-31",
        "link": "https://hd.gzst.org.cn/action/web/index.do?offset=12",
        "description": "英文亲子阅读活动，共读I Can Read分级阅读故事《A Green Green Garden》（绿油油的花园），由亲子英文阅读志愿者主讲，适合3-8岁亲子家庭。",
        "fee": "免费需预约",
        "source": "广州少年儿童图书馆官网",
        "family_friendly": True
    },
    {
        "title": "【阅见岭南】粤语文化交流会：有趣的粤语故事之俗语篇",
        "venue": "广州少年儿童图书馆二楼历史馆",
        "city": "guangzhou",
        "start_date": "2026-07-26",
        "end_date": "2026-07-26",
        "link": "https://hd.gzst.org.cn/action/web/index.do?offset=12",
        "description": "分享生活中经常讲到的粤语俗语背后的有趣故事，由国家一级粤语播音员主讲，使用粤语开展活动。",
        "fee": "免费需预约",
        "source": "广州少年儿童图书馆官网",
        "family_friendly": True
    },
    {
        "title": "【小篮子手工坊】扭扭棒\"铃兰花\"制作活动",
        "venue": "广州少年儿童图书馆一楼市民馆",
        "city": "guangzhou",
        "start_date": "2026-07-18",
        "end_date": "2026-07-18",
        "link": "https://hd.gzst.org.cn/action/web/index.do?offset=12",
        "description": "以扭扭棒为材料，通过扭转、缠绕、塑形等手法，家长与孩子相互配合，携手协作，将绒条变作垂坠如铃的铃兰花作品。适合6-12岁读者。",
        "fee": "免费需预约",
        "source": "广州少年儿童图书馆官网",
        "family_friendly": True
    },
    {
        "title": "知齐者，徐君也——徐悲鸿藏齐白石艺术研究展",
        "venue": "广东美术馆（白鹅潭馆区）",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-10-18",
        "link": "https://biznews.sohu.com/a/1045552995_121106875",
        "description": "以齐白石与徐悲鸿的知己之情为线索，集结徐悲鸿纪念馆、广东省博物馆藏的约100件齐白石艺术珍品，辅以若干珍贵齐白石照片影像，完整呈现齐白石的艺术全貌。",
        "fee": "收费",
        "source": "广东美术馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "四季倒影：光之镜中的自然——赫利顿·希夏个展",
        "venue": "广东美术馆（白鹅潭馆区）",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://biznews.sohu.com/a/1045552995_121106875",
        "description": "集中呈现艺术家近期围绕光、自然与环境创作的多件大型雕塑作品，如《春光》《夏光》《秋光》《冬光》系列，同时展出多件小型雕塑与创作手稿。",
        "fee": "免费",
        "source": "广东美术馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "风景与想象之间——意大利当代艺术在中国展",
        "venue": "广东美术馆（白鹅潭馆区）",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://biznews.sohu.com/a/1045552995_121106875",
        "description": "从西方美术史中\"观看\"的概念出发，强调观看不仅是视觉行为，更涉及人如何理解存在、时间与记忆。作品多以具象为基础，却带有诗意与抒情性。",
        "fee": "免费",
        "source": "广东美术馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "葵山——许江艺术展",
        "venue": "广东美术馆（白鹅潭馆区）",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://biznews.sohu.com/a/1045552995_121106875",
        "description": "分为\"葵颂\"\"炼歌\"\"重屏\"\"众览\"\"怀山\"五个板块，是对许江精神世界与创作脉络的系统呈现。\"葵\"和\"山\"共同构成了他绘画实践的两条主线。",
        "fee": "免费",
        "source": "广东美术馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "\"云星计划\"2026年暑期公益夏令营",
        "venue": "白云区、白云山鸣春谷",
        "city": "guangzhou",
        "start_date": "2026-07-15",
        "end_date": "2026-07-16",
        "link": "http://m.toutiao.com/group/7663405986014626358/",
        "description": "白云区教育局举办，以\"走读白云，探秘科创生态\"为主题，联动多家科研、文旅单位开设两日沉浸式实践课程。包括激光等离子体技术观摩、香氛博物馆调香体验、白云山鸣春谷观鸟等。",
        "fee": "免费需预约",
        "source": "白云融媒、今日头条",
        "family_friendly": True
    },
    {
        "title": "白云山鸣春谷VR观鸟与生态手工活动",
        "venue": "白云山鸣春谷",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://m.toutiao.com/group/7663405986014626358/",
        "description": "在鸣春谷内的天然大鸟笼，近距离观察150余种鸟类，参与VR观鸟、生态手工制作等互动项目；走进白云山自然科普馆，认识本土动植物、两栖爬行类物种。",
        "fee": "收费",
        "source": "白云融媒、今日头条",
        "family_friendly": True
    },
    {
        "title": "花都区第五届\"花开有声 童心向党\"小小红色讲解员培训班",
        "venue": "花都区博物馆各场馆",
        "city": "guangzhou",
        "start_date": "2026-07-15",
        "end_date": "2026-07-20",
        "link": "https://huacheng.gz-cmc.com/pages/2026/06/24/a21d03e75cea4b31ae0c92780ee214f1.html",
        "description": "少年变身\"红色主播\"，学历史、讲英雄，持证上岗C位出道。通过培训让青少年深入了解红色历史，提升表达能力。",
        "fee": "免费需预约",
        "source": "广州日报新花城",
        "family_friendly": True
    },
    {
        "title": "花都区\"花绘童年·阅享快乐\"亲子绘本阅读系列活动",
        "venue": "花都少年儿童图书馆玩具图书室",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://huacheng.gz-cmc.com/pages/2026/06/24/a21d03e75cea4b31ae0c92780ee214f1.html",
        "description": "每周两场，专业讲师带娃边读边玩，手工+情景互动，亲子关系up up！",
        "fee": "免费需预约",
        "source": "广州日报新花城",
        "family_friendly": True
    },
    {
        "title": "花都区2026年青少年暑期文化艺术节",
        "venue": "花都区文化馆",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://huacheng.gz-cmc.com/pages/2026/06/24/a21d03e75cea4b31ae0c92780ee214f1.html",
        "description": "暑期公益培训设置动态、静态、非遗三大课程板块，构建多元化课程体系，丰盈青少年暑期文化生活。",
        "fee": "免费需预约",
        "source": "广州日报新花城",
        "family_friendly": True
    },
    {
        "title": "花都区第九届青少年故事大赛",
        "venue": "花都区图书馆",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://huacheng.gz-cmc.com/pages/2026/06/24/a21d03e75cea4b31ae0c92780ee214f1.html",
        "description": "青少年故事大赛以花为媒，讲出花都故事！传承\"花城\"历史记忆，强化青少年生态保护意识。",
        "fee": "免费需预约",
        "source": "广州日报新花城",
        "family_friendly": True
    },
    {
        "title": "罗洞工匠小镇夏日青春派对季",
        "venue": "从化区江埔街罗洞工匠小镇",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1045415669_121124748/",
        "description": "7-8月周末全天，每周末轮换趣味玩法，有水战狂欢、星空露营、荧光夜跑、稻田音乐会、乡村泼水节及大学生联谊；兼具咖啡非遗DIY、疗愈手作，亲子青年皆可畅玩乡野夏日。",
        "fee": "收费",
        "source": "广州市文化馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "汇景阅动空间押花书签制作体验课",
        "venue": "广州天河区汇景新城亚太国际文化交流中心",
        "city": "guangzhou",
        "start_date": "2026-07-18",
        "end_date": "2026-07-18",
        "link": "https://m.sohu.com/a/1045415669_121124748/",
        "description": "以押花艺术为核心，亲手体验押花的艺术：依循花草本真形态创意构造，再到封膜、搭配流苏，一步步将鲜活的草木时光，定格成一枚独一无二的专属书签。",
        "fee": "免费需预约",
        "source": "广州市文化馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "\"向美而行\"公共文化产品配送社区活动",
        "venue": "广州市各社区（越秀、海珠、天河、白云等11区）",
        "city": "guangzhou",
        "start_date": "2026-07-20",
        "end_date": "2026-08-31",
        "link": "https://m.sohu.com/a/1051586874_121124748/",
        "description": "非遗手作、绘本阅读、正念疗愈等多场活动走进社区。包括夏桑菊制作、药油香牌手作、粤语童谣跟读、古诗品读、扎染技艺等，通过\"育文游\"小程序线上报名。",
        "fee": "免费需预约",
        "source": "广州市文化馆、搜狐网",
        "family_friendly": True
    },
    {
        "title": "广州科学嘉年华动物园奇妙夜活动",
        "venue": "广州动物园",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://news.ycwb.com/ikimvkntih/content_54136253.htm",
        "description": "夜间动物园奇妙夜活动，市民走进昼伏夜出的动物世界，昆虫科普径上中国巨竹节虫、长戟大兜虫、兰花螳螂等珍稀昆虫一一亮相；南美探秘区里，水獭灵动穿梭，水豚悠闲进食，树懒缓缓挪动。",
        "fee": "收费",
        "source": "羊城晚报",
        "family_friendly": True
    },
    {
        "title": "《当家猫遇上猫》粤普双语合家欢音乐剧",
        "venue": "广州大剧院",
        "city": "guangzhou",
        "start_date": "2026-08-23",
        "end_date": "2026-08-23",
        "link": "http://wglj.gz.gov.cn/attachment/7/7858/7858616/10385320.pdf",
        "description": "反转舞台x香港演戏家族粤普双语治愈系合家欢音乐剧，适合全家共同观赏。",
        "fee": "收费",
        "source": "广州市文化广电旅游局",
        "family_friendly": True
    },
    {
        "title": "合家欢魔法音乐剧《小龙的奇幻梦境》",
        "venue": "广东艺术剧院",
        "city": "guangzhou",
        "start_date": "2026-07-20",
        "end_date": "2026-07-20",
        "link": "http://book.newdu.com/m/view.php?aid=147283",
        "description": "玩了一把魔术和光影的游戏，光影之间，观众跟随小龙在梦境和现实之间穿梭。",
        "fee": "收费",
        "source": "广州日报、新读网",
        "family_friendly": True
    },
    {
        "title": "多媒体音乐剧《爱丽丝梦游仙境》",
        "venue": "广东艺术剧院",
        "city": "guangzhou",
        "start_date": "2026-07-27",
        "end_date": "2026-07-27",
        "link": "http://book.newdu.com/m/view.php?aid=147283",
        "description": "采用舞台影像实时交互技术，将戏剧、音乐、舞蹈和多媒体视觉效果融合一起。主创团队制作了10首原创歌曲，主题曲配乐由德国广播交响乐团现场演奏录制。",
        "fee": "收费",
        "source": "广州日报、新读网",
        "family_friendly": True
    },
    {
        "title": "莫斯科国立拉夫罗夫斯基少儿芭蕾舞团GALA演出",
        "venue": "广州大剧院",
        "city": "guangzhou",
        "start_date": "2026-07-22",
        "end_date": "2026-07-23",
        "link": "http://book.newdu.com/m/view.php?aid=147283",
        "description": "知名少儿芭蕾舞团带来精彩芭蕾GALA演出，适合少儿观看的经典芭蕾选段表演。",
        "fee": "收费",
        "source": "广州日报、新读网",
        "family_friendly": True
    },
    {
        "title": "《好饿的毛毛虫秀》演员故事角活动",
        "venue": "广州大剧院实验剧场",
        "city": "guangzhou",
        "start_date": "2026-07-24",
        "end_date": "2026-07-24",
        "link": "https://3w.gzdjy.org/view.html?type=art&cid=318&id=19",
        "description": "外百老汇原版儿童剧演员亲临的\"故事角\"活动，小朋友们浸没式体验剧中《棕色的熊，棕色的熊，你在看什么?》和《好饿的毛毛虫》的故事并进行互动。",
        "fee": "免费需预约",
        "source": "广州大剧院官网",
        "family_friendly": True
    },
    {
        "title": "原创少儿科幻音乐戏剧《本草纲目》",
        "venue": "广州大剧院",
        "city": "guangzhou",
        "start_date": "2026-07-24",
        "end_date": "2026-07-24",
        "link": "https://m.weibo.cn/detail/5317981634822961",
        "description": "以少年视角活化传统古籍《本草纲目》的原创少儿科幻音乐戏剧，助力青少年美育成长。",
        "fee": "收费",
        "source": "广州大剧院、新浪微博",
        "family_friendly": True
    },
    {
        "title": "原创戏剧《山海经》少儿版",
        "venue": "广州大剧院",
        "city": "guangzhou",
        "start_date": "2026-07-01",
        "end_date": "2026-08-31",
        "link": "http://ent.ycwb.com/2026-07/17/content_54235186.htm",
        "description": "以少年视角活化传统古籍《山海经》，助力青少年美育成长，是广州大剧院青少年艺术单元的重要演出。",
        "fee": "收费",
        "source": "羊城晚报",
        "family_friendly": True
    }
]

print(f"现有活动数量: {len(existing_activities)}")
print(f"新活动候选数量: {len(new_activities)}")

unique_new_activities = []
for act in new_activities:
    if act['title'] not in existing_titles:
        unique_new_activities.append(act)
    else:
        print(f"重复活动，跳过: {act['title']}")

print(f"\n新增活动数量: {len(unique_new_activities)}")

combined_activities = existing_activities + unique_new_activities
print(f"合并后总活动数量: {len(combined_activities)}")

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(combined_activities, f, ensure_ascii=False, indent=2)

print(f"\n已保存到: {output_file}")

sources = set()
for act in unique_new_activities:
    sources.add(act['source'])

print(f"\n新增活动来源列表:")
for s in sorted(sources):
    print(f"  - {s}")

print(f"\n新增代表性活动（前10个）:")
for i, act in enumerate(unique_new_activities[:10]):
    print(f"  {i+1}. {act['title']}")
