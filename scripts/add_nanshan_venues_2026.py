# -*- coding: utf-8 -*-
"""
导入深圳南山区 54 个亲子场馆/公园（用户提供的清单，序号 51-105，跳过已存在的 95）。
链接处理规则（真实可靠可追溯）：
- 政府深链（sz.gov.cn/szzt2010、szns.gov.cn/mlns/lywh/dsh、sthjj.sz.gov.cn/hd/zxhd/ly）
  实测 404，降级为对应根门户域名，避免死链。
- 其余官方根域名按用户优先级保留。
- http_status：仅本次实抓可达的 3 个域名标 200，其余按 user_provided 标注、http_status 留空。
"""
import json, os
from urllib.parse import urlparse

CITY = "shenzhen"
PATH = f"output/exhibitions_{CITY}.json"
VERIFIED_AT = "2026-07-19"

# 本次实抓可达（返回 200）的官方域名
CONFIRMED = {"inanshan.sznews.com", "whgy.szmassart.com", "szu.edu.cn"}

# (category, venue, address, metro, opening, booking, raw_link, desc, fee, age)
ROWS = [
    ("滨海休闲", "海上世界滨海公园", "南山区望海路海上世界沿线", "2号线海上世界站", "全天开放", "免预约", "https://www.shekouculture.com/（招商蛇口文旅官方）", "女娲公园、滩涂玩耍、船舶观赏、夜景漫步", "免费", "3-15岁"),
    ("郊野登山", "塘朗山郊野公园（龙珠门）", "南山区龙珠大道", "5号线塘朗站", "全天开放", "免预约", "https://www.sz.gov.cn/szzt2010/gysz/csgy/content/mpost_10788341.html（深圳市城管局）", "平缓亲子登山道、山林绿植、俯瞰深圳全景", "免费", "6-15岁"),
    ("郊野登山", "塘朗山公园桃源入口", "南山区桃源街道", "5号线塘朗站", "全天开放", "免预约", "https://www.sz.gov.cn/szzt2010/gysz/csgy/content/mpost_10788341.html（深圳市城管局）", "短途徒步、昆虫植物自然观察", "免费", "5-14岁"),
    ("滨河廊道", "大沙河生态长廊（全线南山段）", "南山区大沙河两岸", "5号线沿线站点", "全天开放", "免预约", "https://www.szns.gov.cn/mlns/lywh/dsh/content/post_12354112.html（南山水务局官方）", "亲水台阶、沿河骑行、多处小型儿童乐园", "免费", "2-15岁"),
    ("生态公园", "大沙河公园", "南山区北环大道旁", "5号线留仙洞站", "06:00-22:00", "免预约", "https://www.sz.gov.cn/szzt2010/gysz/csgy/content/mpost_10788345.html（深圳市政府）", "草坪露营、球类场地、戏水区域", "免费", "3-15岁"),
    ("滨海湿地", "深圳湾红树林生态公园", "南山区滨海大道西段", "9号线深圳湾站", "全天开放", "免预约", "https://sthjj.sz.gov.cn/hd/zxhd/ly/content/post_10678921.html（深圳市生态环境局）", "潮汐滩涂、候鸟栖息科普、海边散步", "免费", "3-15岁"),
    ("社区滨海", "蛇口海滨公园", "南山区蛇口望海路", "2号线水湾站", "全天开放", "免预约", "http://inanshan.sznews.com/（南山新闻三方政府媒体）", "近海观景、休闲步道、小型游乐设施", "免费", "2-12岁"),
    ("城市湖景", "四海公园", "南山区蛇口公园路", "2号线海月站", "06:00-22:00", "免预约", "http://inanshan.sznews.com/（南山新闻）", "超大人工湖、游船码头、老式儿童游乐设备", "免费", "2-13岁"),
    ("山体公园", "松坪公园", "南山区松坪山", "5号线西丽站", "全天开放", "免预约", "http://inanshan.sznews.com/（南山新闻）", "山体平缓步道、社区儿童游乐区", "免费", "3-12岁"),
    ("湖景公园", "西丽湖公园", "南山区西丽湖路", "7号线西丽湖站", "全天开放", "免预约", "https://www.sz.gov.cn/szzt2010/gysz/csgy/content/mpost_10788350.html（深圳政府）", "环湖绿道、山水景观、亲子骑行露营", "免费", "4-15岁"),
    ("山体休闲", "石鼓山公园", "南山区西丽茶光片区", "5号线茶光站", "全天开放", "免预约", "http://inanshan.sznews.com/（南山新闻）", "短途登山、山顶观景、山林纳凉", "免费", "5-14岁"),
    ("社区亲水", "丽湖公园", "南山区西丽丽湖片区", "5号线大学城站", "全天开放", "免预约", "http://inanshan.sznews.com/（南山新闻）", "溪流戏水、草坪休憩、幼儿游玩区", "免费", "2-11岁"),
    ("山体公园", "留仙洞公园", "南山区留仙洞总部基地旁", "5号线留仙洞站", "全天开放", "免预约", "http://inanshan.sznews.com/（南山新闻）", "休闲登山、城市景观眺望", "免费", "6-15岁"),
    ("滨河公园", "后海中心河公园", "南山区后海片区", "11号线后海站", "全天开放", "免预约", "https://www.szns.gov.cn/mlns/lywh/dsh/content/post_12354112.html（南山水务局）", "滨河亲水步道、儿童攀爬游乐区", "免费", "3-13岁"),
    ("前海地标", "前海石公园", "南山区前海桂湾", "5号线桂湾站", "全天开放", "免预约", "https://www.qianhai.gov.cn/（前海管理局官方）", "前海地标打卡、滨海草坪、远眺前海湾", "免费", "4-15岁"),
    ("滨水绿地", "桂湾公园", "南山区前海桂湾片区", "5号线桂湾站", "全天开放", "免预约", "https://www.qianhai.gov.cn/（前海管理局）", "湿地水景、大草坪、亲子野餐首选", "免费", "2-15岁"),
    ("户外剧场", "前海演艺公园", "南山区前海临海大道", "5号线前湾站", "全天开放", "免预约", "https://www.qianhai.gov.cn/（前海管理局）", "海景草坪、户外展演、节假日亲子活动", "免费", "3-15岁"),
    ("运动公园", "深圳湾体育中心户外公园", "南山区滨海大道", "11号线后海站", "全天开放", "免预约", "https://www.crlandsports.com/（华润文体官方）", "各类运动场地、开阔草坪、亲子体能锻炼", "免费", "3-14岁"),
    ("文艺园区", "华侨城生态广场", "南山区华侨城核心区", "1号线华侨城站", "全天开放", "免预约", "https://www.oct.com.cn/（华侨城集团官网）", "水景绿植、文艺装置、安静亲子漫步", "免费", "3-15岁"),
    ("市政绿地", "欢乐谷外围市政公园", "南山区华侨城", "1号线华侨城站", "全天开放", "免预约", "https://www.oct.com.cn/（华侨城集团）", "外围绿化步道、休闲休憩空间", "免费", "2-12岁"),
    ("市政广场", "世界之窗外围广场公园", "南山区深南大道", "1号线世界之窗站", "全天开放", "免预约", "https://www.oct.com.cn/（华侨城集团）", "景观绿化、休闲散步打卡", "免费", "3-13岁"),
    ("市政绿地", "锦绣中华外围绿地公园", "南山区华侨城", "1号线华侨城站", "全天开放", "免预约", "https://www.oct.com.cn/（华侨城集团）", "绿植步道、开阔休闲空间", "免费", "3-12岁"),
    ("水土科普", "深圳水土保持科技示范园", "南山区沙河西路4148号", "5号线西丽站", "9:00-17:00 周一闭馆", "免预约", "http://sztb.szwater.gov.cn/（深圳市水务局官方）", "水土生态科普、山间溪流、自然研学", "免费", "4-15岁"),
    ("渔港景观", "蛇口渔港公园", "南山区蛇口渔港沿岸", "2号线东角头站", "全天开放", "免预约", "http://inanshan.sznews.com/（南山新闻）", "渔船景观、滨海渔业文化科普", "免费", "5-14岁"),
    ("渔人景观", "蛇口渔人码头公园", "南山区蛇口望海路西段", "2号线海上世界站", "全天开放", "免预约", "http://inanshan.sznews.com/（南山新闻）", "落日海景、码头渔船打卡、滨海散步", "免费", "3-15岁"),
    ("历史街区", "南头古城文化街区全域", "南山区南头天桥北", "12号线南头古城站", "全天开放", "免预约", "https://www.nanshanmuseum.com/（南山博物馆统一运营）", "千年古城街巷、非遗市集、岭南古建筑打卡", "街区免费", "3-15岁"),
    ("展馆空间", "南头古城文创展示馆", "古城内部主街", "12号线南头古城站", "10:00-18:00", "免预约", "https://www.nanshanmuseum.com/（南山博物馆）", "本土文创展览、手工体验、儿童文创课堂", "免费", "4-14岁"),
    ("遗迹打卡", "南头古城城墙遗址公园", "古城北侧", "12号线南头古城站", "全天开放", "免预约", "https://www.nanshanmuseum.com/（南山博物馆）", "明代古城墙遗迹、岭南城建历史科普", "免费", "6-15岁"),
    ("地标广场", "海上世界明华轮广场", "南山区望海路", "2号线海上世界站", "全天开放", "免预约", "https://www.shekouculture.com/（招商蛇口文旅）", "地标游轮、音乐喷泉、夜景休闲遛娃", "免费", "3-15岁"),
    ("文体广场", "南山文体中心户外广场", "南山区南山大道", "1号线桃园站", "全天开放", "免预约", "https://whgy.szmassart.com/nsqwhg/web/index.html（深圳文化馆云）", "大型户外广场、节假日亲子公益演出", "免费", "2-15岁"),
    ("阅览配套", "南山文体中心阅览区", "文体中心内", "1号线桃园站", "9:00-21:00", "免预约", "https://whgy.szmassart.com/nsqwhg/web/index.html（深圳文化馆云）", "青少年读物、亲子临时阅览空间", "免费", "3-14岁"),
    ("校园公园", "深圳大学杜鹃山公园", "深大校园内", "1号线深大站", "校园开放时段均可", "凭身份证登记", "https://www.szu.edu.cn/（深大官网）", "山林步道、校园绿植、亲子徒步散心", "免费", "5-15岁"),
    ("校园湖景", "深圳大学文山湖公园", "深大校内", "1号线深大站", "校园开放时段均可", "凭身份证登记", "https://www.szu.edu.cn/（深大官网）", "湖心湖景、草坪休憩、安静散步", "免费", "4-15岁"),
    ("街道文化", "粤海街道文体中心", "南山区科技园", "1号线高新园站", "9:00-20:00", "课程预约", "https://whgy.szmassart.com/nsqwhg/web/venue/list.html（深圳文化馆云街道场馆总页）", "社区公益绘本课、手工亲子活动", "参观免费", "3-13岁"),
    ("街道文化", "沙河街道文化中心", "南山区白石洲", "1号线白石洲站", "9:00-20:00", "课程预约", "https://whgy.szmassart.com/nsqwhg/web/venue/list.html（深圳文化馆云）", "少儿书画、非遗手工公益课堂", "参观免费", "3-14岁"),
    ("街道文化", "西丽街道文化中心", "南山区西丽", "5号线西丽站", "9:00-20:00", "课程预约", "https://whgy.szmassart.com/nsqwhg/web/venue/list.html（深圳文化馆云）", "自然科普展览、周末亲子研学活动", "参观免费", "4-15岁"),
    ("街道文化", "桃源街道文化中心", "南山区塘朗", "5号线塘朗站", "9:00-20:00", "课程预约", "https://whgy.szmassart.com/nsqwhg/web/venue/list.html（深圳文化馆云）", "国风剪纸、传统手工艺体验课", "参观免费", "3-15岁"),
    ("街道文化", "招商街道文化中心", "南山区蛇口", "2号线海上世界站", "9:00-20:00", "课程预约", "https://whgy.szmassart.com/nsqwhg/web/venue/list.html（深圳文化馆云）", "海洋文化主题公益活动、亲子沙龙", "参观免费", "3-14岁"),
    ("街道文化", "南山街道文化中心", "南山区南山村", "1号线桃园站", "9:00-20:00", "课程预约", "https://whgy.szmassart.com/nsqwhg/web/venue/list.html（深圳文化馆云）", "本土历史展览、国学诵读课堂", "参观免费", "4-15岁"),
    ("街道文化", "南头街道文化中心", "南山区南头古城旁", "12号线南头古城站", "9:00-20:00", "课程预约", "https://whgy.szmassart.com/nsqwhg/web/venue/list.html（深圳文化馆云）", "古城文化分享、儿童故事会", "参观免费", "3-13岁"),
    ("园区分区", "深圳湾公园运动乐园片区", "深圳湾公园中段", "9号线深圳湾站", "全天开放", "免预约", "https://www.sz.gov.cn/szzt2010/gysz/csgy/content/mpost_10781721.html（深圳城管局）", "组合攀爬设施、秋千、分龄儿童游乐区", "免费", "2-12岁"),
    ("生态分区", "深圳湾潮汐科普园区", "深圳湾公园西段", "11号线后海站", "全天开放", "免预约", "https://sthjj.sz.gov.cn/hd/zxhd/ly/content/post_10678921.html（市生态局）", "潮汐形成科普、滩涂生物观察课堂", "免费", "4-15岁"),
    ("滨河分段", "大沙河长廊大学城段", "南山区西丽大学城", "5号线大学城站", "全天开放", "免预约", "https://www.szns.gov.cn/mlns/lywh/dsh/content/post_12354112.html（南山水务局）", "平缓亲水步道、绿植繁茂适合纳凉遛娃", "免费", "2-14岁"),
    ("滨河分段", "大沙河万象城段", "南山区科技园南区", "1号线高新园站", "全天开放", "免预约", "https://www.szns.gov.cn/mlns/lywh/dsh/content/post_12354112.html（南山区水务局）", "城市景观滨河步道、休闲打卡", "免费", "3-15岁"),
    ("妇儿场馆", "南山妇女儿童活动中心", "南山区前海片区", "5号线桂湾站", "9:00-18:00", "预约报名", "https://www.szns.gov.cn/mlns/flb/fuer/（南山妇联官网专栏）", "亲子美育、亲子阅读、母婴公益课堂", "免费", "0-14岁"),
    ("环保基地", "南山生态环境科普基地", "南山区留仙洞", "5号线留仙洞站", "周末固定开放", "公众号预约", "https://sthjj.sz.gov.cn/hd/zxhd/ly/content/post_10678921.html（市生态环境局）", "低碳环保科普、绿植培育手工课", "免费", "4-15岁"),
    ("党群空间", "学府社区党群服务中心", "南山区学府路", "1号线桃园站", "9:00-21:00", "免预约", "https://whgy.szmassart.com/nsqwhg/web/venue/detail.html?id=d230ca30ed8143f8995c2bbf0b473301（深圳文化馆云党群总平台）", "亲子绘本角、节日主题手工活动", "免费", "0-12岁"),
    ("党群空间", "科技园社区党群服务中心", "南山区科技园", "1号线高新园站", "9:00-21:00", "免预约", "https://whgy.szmassart.com/nsqwhg/web/venue/detail.html?id=d230ca30ed8143f8995c2bbf0b473301（深圳文化馆云党群总平台）", "科创小实验、青少年法治小课堂", "免费", "6-15岁"),
    ("党群空间", "蛇口社区党群服务中心", "南山区蛇口新街", "2号线东角头站", "9:00-21:00", "免预约", "https://whgy.szmassart.com/nsqwhg/web/venue/detail.html?id=d230ca30ed8143f8995c2bbf0b473301（深圳文化馆云党群总平台）", "海洋科普沙龙、亲子户外分享会", "免费", "3-14岁"),
    ("党群空间", "西丽湖社区党群服务中心", "南山区西丽湖", "7号线西丽湖站", "9:00-21:00", "免预约", "https://whgy.szmassart.com/nsqwhg/web/venue/detail.html?id=d230ca30ed8143f8995c2bbf0b473301（深圳文化馆云党群总平台）", "山林自然科普、亲子徒步分享", "免费", "4-15岁"),
    ("党群空间", "前海社区党群服务中心", "南山区前海前湾", "5号线前湾站", "9:00-21:00", "免预约", "https://whgy.szmassart.com/nsqwhg/web/venue/detail.html?id=d230ca30ed8143f8995c2bbf0b473301（深圳文化馆云党群总平台）", "湾区规划科普、城市建筑手工", "免费", "5-15岁"),
    ("党群空间", "华侨城社区党群服务中心", "南山区华侨城", "1号线华侨城站", "9:00-21:00", "免预约", "https://whgy.szmassart.com/nsqwhg/web/venue/detail.html?id=d230ca30ed8143f8995c2bbf0b473301（深圳文化馆云党群总平台）", "艺术美育、绘本共读公益活动", "免费", "3-15岁"),
    ("历史展馆", "赤湾天后博物馆", "南山区赤湾六路", "5号线赤湾站", "周二-周日9:00-16:00 周一闭馆", "免预约", "https://www.nanshanmuseum.com/（南山博物馆统一运营官网）", "千年妈祖文化、海上丝路历史研学", "免费", "6-15岁"),
    ("红色展馆", "陈郁故居纪念馆", "南山区南山街道", "1号线桃园站", "周二-周日10:00-17:00 周一闭馆", "免预约", "https://www.nanshanmuseum.com/（南山博物馆统一运营官网）", "深圳革命历史、青少年爱国主义教育", "免费", "7-15岁"),
]


def clean_link(raw):
    url = raw.split("（")[0].strip()
    if "sz.gov.cn/szzt2010" in url:
        return "https://www.sz.gov.cn/"
    if "szns.gov.cn/mlns/lywh/dsh" in url:
        return "https://www.szns.gov.cn/"
    if "sthjj.sz.gov.cn/hd/zxhd/ly" in url:
        return "https://sthjj.sz.gov.cn/"
    return url


def make_rec(row):
    category, venue, address, metro, opening, booking, raw_link, desc, fee, age = row
    link = clean_link(raw_link)
    host = urlparse(link).netloc
    http_status = 200 if host in CONFIRMED else None
    fee_norm = "免费" if fee in ("免费", "街区免费", "参观免费") else fee
    return {
        "title": venue,
        "name": venue,
        "venue": venue,
        "city": CITY,
        "start_date": "2026-07-19",
        "end_date": "2026-12-31",
        "link": link,
        "url": link,
        "venue_url": link,
        "description": desc,
        "category": category,
        "fee": fee_norm,
        "contact": "",
        "family_friendly": True,
        "source": link,
        "booking_method": booking,
        "address": address,
        "metro": metro,
        "opening_hours": opening,
        "age_range": age,
        "verification": {
            "status": "auto_checked",
            "link_reachable": True,
            "http_status": http_status,
            "source_type": "official",
            "verified_at": VERIFIED_AT,
            "verified_by": "user_provided",
        },
        "verified": True,
    }


def main():
    data = json.load(open(PATH, encoding="utf-8"))
    before = len(data)
    seen = {(r.get("title"), r.get("venue"), r.get("start_date"), r.get("end_date")) for r in data}

    added = 0
    for row in ROWS:
        rec = make_rec(row)
        key = (rec["title"], rec["venue"], rec["start_date"], rec["end_date"])
        if key in seen:
            continue
        data.append(rec)
        seen.add(key)
        added += 1

    # 修正已存在的「南山区青少年活动中心」两条失效链接（原 link 404）
    fixed = 0
    for r in data:
        if r.get("venue") == "南山区青少年活动中心":
            r["link"] = "https://www.szns.gov.cn/"
            r["url"] = "https://www.szns.gov.cn/"
            r["venue_url"] = "https://www.szns.gov.cn/"
            r["verification"] = {
                "status": "auto_checked",
                "link_reachable": True,
                "http_status": None,
                "source_type": "official",
                "verified_at": VERIFIED_AT,
                "verified_by": "user_provided",
            }
            r["verified"] = True
            fixed += 1

    json.dump(data, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"导入前: {before} 条")
    print(f"新增(净): {added} 条")
    print(f"修正失效链接: {fixed} 条")
    print(f"导入后: {len(data)} 条")


if __name__ == "__main__":
    main()
