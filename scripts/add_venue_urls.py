# -*- coding: utf-8 -*-
"""
为「其他9城 7-8月活动」新增的 95 条记录补充场馆官方链接。

策略：
- 仅对 2026-07-19 本批新增记录(verification.verified_at == '2026-07-19')补充。
- 新增字段 `venue_url` = 场馆官方网站（仅在我有把握的官方域名时填，来源=检索确认/知识库）。
- 没把握的场馆不填 `venue_url`，原 `link`(本地宝，已 http 200 验证) 仍作为可用参考，避免错链。
- 不改动既有 link/url/verification，保证可追溯性不破坏。

场馆→官网 映射经 WebSearch/WebFetch 核实（国博/上博/粤博/成都美术馆/重庆美术馆/南京奥体/
武汉国博/西安国展/陕西大剧院/中国动漫博物馆/民生现代美术馆/杭州植物园/海昌/等均已确认）。
"""
import json
import os

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'output')
VERIFIED_AT = "2026-07-19"

# (场馆名片段, 官方网址) — 片段命中即采用；None 表示无把握官方网址，留空。
VENUE_URL = [
    # 北京
    ("中国国家博物馆", "https://www.chnmuseum.cn/"),
    ("中国美术馆", "https://www.namoc.org/"),
    ("首都博物馆", "https://www.capitalmuseum.org.cn/"),
    # 中华世纪坛 worldartmuseum.cn 抓取失败，官网待确认 → 留空
    # 华熙LIVE huaxilive.com 抓取失败，官网待确认 → 留空
    # 国家体育场(鸟巢) nsgz.com 实为广州南视灯具，非鸟巢 → 留空
    ("明十三陵", "https://www.mingshisanling.com/"),
    ("黄花城水长城", "https://www.huanghuacheng.com/"),
    ("北京欢乐谷", "https://www.happyvalleybeijing.com/"),
    # 上海
    ("上海博物馆", "https://www.shanghaimuseum.net/"),
    ("上海当代艺术博物馆", "https://www.powerstationofart.com/"),
    ("上海欢乐谷", "https://sh.happyvalley.cn/"),
    ("上海民生现代美术馆", "https://minshengart.com/"),
    ("上海美术馆", "https://www.sh-artmuseum.org.cn/"),
    ("上海迪士尼乐园", "https://www.shanghaidisneyresort.com/"),
    ("上海野生动物园", "https://www.shwildlife.com/"),
    # 广州
    ("广东省博物馆", "https://www.gdmuseum.org.cn/"),
    ("广东美术馆", "https://www.gdmoa.org/"),
    ("广州艺术博物院", "https://www.gzam.com.cn/"),
    ("广州长隆", "https://www.chimelong.com/"),
    # 杭州
    ("中国动漫博物馆", "https://www.ccam.org.cn/"),
    ("杭州宋城", "https://www.songcn.com/"),
    ("杭州植物园", "http://www.hzbg.cn/"),
    ("浙江省博物馆", "https://www.zhejiangmuseum.com/"),
    ("西湖", "https://westlake.hangzhou.gov.cn/"),
    ("钱王祠", "https://westlake.hangzhou.gov.cn/"),
    # 成都
    ("A4美术馆", "https://www.a4am.com/"),
    ("四川博物院", "https://www.scmuseum.cn/"),
    ("成都市美术馆", "https://www.cdamuseum.cn/"),
    ("成都欢乐谷", "https://cd.happyvalley.cn/"),
    ("成都海昌极地海洋公园", "https://www.haichangoceanpark.com/chengdu"),
    ("成都自然博物馆", "https://www.cdmnh.com/"),
    ("知美术馆", "https://www.zhiartmuseum.com/"),
    ("西岭雪山", "https://www.xiling.cn/"),
    # 重庆
    ("重庆中国三峡博物馆", "https://www.3gmuseum.cn/"),
    ("重庆欢乐谷", "https://cq.happyvalley.cn/"),
    ("重庆科技馆", "https://www.cqkjg.com/"),
    ("重庆美术馆", "https://www.cqartmuseum.cn/"),
    # 南京
    ("南京博物院", "https://www.njmuseum.com/"),
    ("南京奥体中心", "https://www.njaoti.com/"),
    # 武汉
    ("武汉国际博览中心", "http://www.wniecm.com.cn/"),
    ("武汉欢乐谷", "https://wh.happyvalley.cn/"),
    ("湖北省博物馆", "https://www.hubeimuseum.net/"),
    # 西安
    ("西安国际会展中心", "https://www.xianicec.com/"),
    ("西安碑林博物馆", "https://www.beilin-museum.com/"),
    ("陕西历史博物馆", "https://www.sxhm.com/"),
    ("陕西大剧院", "https://www.snpac.com/"),
]


def find_venue_url(venue):
    for frag, url in VENUE_URL:
        if frag in venue:
            return url  # may be None
    return None


def main():
    cities = ['beijing', 'shanghai', 'guangzhou', 'hangzhou',
              'chengdu', 'chongqing', 'nanjing', 'wuhan', 'xian']
    total_added = 0
    total_fallback = 0
    fallback_venues = set()
    for c in cities:
        path = os.path.join(OUT_DIR, f'exhibitions_{c}.json')
        data = json.load(open(path, encoding='utf-8'))
        changed = 0
        for rec in data:
            v = rec.get('verification', {}).get('verified_at')
            if v != VERIFIED_AT:
                continue
            venue = rec.get('venue', '')
            url = find_venue_url(venue)
            if url:
                rec['venue_url'] = url
                changed += 1
                total_added += 1
            else:
                # 无把握官方网址：删掉可能残留的旧 venue_url，避免错链
                rec.pop('venue_url', None)
                total_fallback += 1
                fallback_venues.add(venue)
        json.dump(data, open(path, 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=2)
        print(f'{c}: +venue_url {changed}')
    print(f'\nTOTAL venue_url added = {total_added}, fallback(no official) = {total_fallback}')
    print('Fallback venues (still using 本地宝 link):')
    for v in sorted(fallback_venues):
        print('  -', v)


if __name__ == '__main__':
    main()
