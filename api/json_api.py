# -*- coding: utf-8 -*-
"""
童行 (goout) —— 城市场馆 / 活动数据 REST API
================================================

零依赖（仅 Python 标准库），直接从 output/exhibitions_<city>.json 读取真实数据。
支持跨域（CORS）访问，可被网页 / 小程序 / 第三方直接调用。

启动：
    python3 api/json_api.py            # 默认 0.0.0.0:8787
    PORT=9000 python3 api/json_api.py  # 自定义端口

接口一览：
    GET /                      接口概览（JSON）
    GET /docs                  接口文档（HTML，人可读）
    GET /api/cities            城市列表（含活动数 / 场馆数）
    GET /api/activities        活动列表（支持多种过滤 + 分页）
    GET /api/activities/{id}   单个活动详情
    GET /api/venues            场馆列表（由活动聚合，含官网链接）
    GET /api/venues/{id}       单个场馆详情 + 其活动
    GET /api/statistics        统计（按城市 / 分类 / 收费）
    GET /api/reload            重新加载磁盘上的 JSON 数据
"""

import hashlib
import html
import json
import os
import re
import sys
import urllib.parse
from datetime import date
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# --------------------------------------------------------------------------- #
# 配置
# --------------------------------------------------------------------------- #
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")
PORT = int(os.environ.get("PORT", "8787"))
HOST = os.environ.get("HOST", "0.0.0.0")

CITY_NAMES = {
    "beijing": "北京",
    "shanghai": "上海",
    "guangzhou": "广州",
    "shenzhen": "深圳",
    "hangzhou": "杭州",
    "chengdu": "成都",
    "chongqing": "重庆",
    "nanjing": "南京",
    "wuhan": "武汉",
    "xian": "西安",
}

# --------------------------------------------------------------------------- #
# 数据加载
# --------------------------------------------------------------------------- #
def _make_id(*parts):
    """生成稳定的短 id（同一记录多次加载结果一致）"""
    raw = "|".join(str(p) for p in parts)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:12]


def _norm_bool(v):
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        return v.strip().lower() in ("true", "1", "yes", "是")
    return bool(v)


def load_data():
    """读取 output/exhibitions_*.json，构建内存索引。"""
    activities = []
    cities = {}
    venues = {}  # (city, venue) -> venue dict

    files = sorted(f for f in os.listdir(OUTPUT_DIR) if re.match(r"^exhibitions_[a-z]+\.json$", f))
    today = date.today().isoformat()

    for fname in files:
        code = fname[len("exhibitions_"):-len(".json")]
        if code not in CITY_NAMES:
            continue
        path = os.path.join(OUTPUT_DIR, fname)
        try:
            with open(path, encoding="utf-8") as f:
                recs = json.load(f)
        except Exception as e:
            print(f"[warn] 读取 {fname} 失败: {e}", file=sys.stderr)
            continue

        cname = CITY_NAMES[code]
        city_entry = cities.setdefault(code, {
            "code": code, "name": cname, "activity_count": 0, "venue_count": 0,
        })

        for rec in recs:
            if not isinstance(rec, dict):
                continue
            venue = (rec.get("venue") or "").strip()
            title = (rec.get("title") or rec.get("name") or "").strip()
            start = (rec.get("start_date") or "").strip()
            end = (rec.get("end_date") or "").strip()

            aid = _make_id(code, title, venue, start, end)
            item = dict(rec)
            item["id"] = aid
            item["city"] = code
            item["city_name"] = cname
            item["family_friendly"] = _norm_bool(
                rec.get("family_friendly", rec.get("is_family_friendly"))
            )
            # 统一一下日期字段
            item["start_date"] = start
            item["end_date"] = end
            item["status"] = _status(start, end, today)
            activities.append(item)
            city_entry["activity_count"] += 1

            # 聚合场馆
            if venue:
                vkey = (code, venue)
                v = venues.get(vkey)
                if v is None:
                    v = {
                        "id": _make_id(code, venue),
                        "name": venue,
                        "city": code,
                        "city_name": cname,
                        "district": (rec.get("district") or "").strip(),
                        "type": (rec.get("type") or "").strip(),
                        "venue_url": (rec.get("venue_url") or "").strip(),
                        "third_party_url": (rec.get("link") or rec.get("url") or "").strip(),
                        "address": (rec.get("address") or "").strip(),
                        "activity_count": 0,
                        "activity_ids": [],
                    }
                    venues[vkey] = v
                # 优先保留已验证的官网链接
                if not v["venue_url"] and rec.get("venue_url"):
                    v["venue_url"] = rec["venue_url"]
                # 记录三方链接（活动来源页，多为本地宝汇总页）作为兜底
                if not v["third_party_url"] and (rec.get("link") or rec.get("url")):
                    v["third_party_url"] = (rec.get("link") or rec.get("url")).strip()
                if not v["district"] and rec.get("district"):
                    v["district"] = rec["district"]
                if not v["type"] and rec.get("type"):
                    v["type"] = rec["type"]
                v["activity_count"] += 1
                v["activity_ids"].append(aid)

    for c in cities.values():
        c["venue_count"] = sum(1 for v in venues.values() if v["city"] == c["code"])

    return {
        "activities": activities,
        "cities": list(cities.values()),
        "venues": list(venues.values()),
        "loaded_at": today,
    }


def _status(start, end, today):
    if start and start > today:
        return "upcoming"
    if end and end < today:
        return "ended"
    return "ongoing"


# --------------------------------------------------------------------------- #
# 过滤逻辑
# --------------------------------------------------------------------------- #
def filter_activities(acts, q):
    city = q.get("city", "")
    venue = q.get("venue", "")
    category = q.get("category", "")
    fee = q.get("fee", "")
    kw = q.get("keyword", "").strip().lower()
    status = q.get("status", "")
    ff = q.get("family_friendly", "")
    start_date = q.get("start_date", "")
    end_date = q.get("end_date", "")

    out = []
    for a in acts:
        if city and a.get("city") != city:
            continue
        if venue and a.get("venue") != venue:
            continue
        if category and (a.get("category") or "") != category:
            continue
        if fee and (a.get("fee") or "") != fee:
            continue
        if status and a.get("status") != status:
            continue
        if ff in ("true", "1", "yes"):
            if not a.get("family_friendly"):
                continue
        elif ff in ("false", "0", "no"):
            if a.get("family_friendly"):
                continue
        if start_date and (a.get("end_date") or "") and a["end_date"] < start_date:
            continue
        if end_date and (a.get("start_date") or "") and a["start_date"] > end_date:
            continue
        if kw:
            hay = " ".join(str(a.get(k, "")) for k in ("title", "name", "venue", "description", "category"))
            hay = hay.lower()
            if kw not in hay:
                continue
        out.append(a)
    return out


def filter_venues(vens, q):
    city = q.get("city", "")
    kw = q.get("keyword", "").strip().lower()
    out = []
    for v in vens:
        if city and v.get("city") != city:
            continue
        if kw and kw not in (v.get("name", "") + v.get("district", "") + v.get("type", "")).lower():
            continue
        out.append(v)
    return out


# --------------------------------------------------------------------------- #
# 文档（HTML / 概览）
# --------------------------------------------------------------------------- #
def overview_json():
    return {
        "name": "童行 (goout) 活动 / 场馆数据 API",
        "version": "1.0.0",
        "description": "基于 output/exhibitions_*.json 的城市场馆与亲子活动数据接口，支持跨域访问。",
        "base_url": "/api",
        "endpoints": [
            {"method": "GET", "path": "/api/cities", "desc": "城市列表（含活动数 / 场馆数）"},
            {"method": "GET", "path": "/api/activities", "desc": "活动列表（过滤 + 分页）"},
            {"method": "GET", "path": "/api/activities/{id}", "desc": "单个活动详情"},
            {"method": "GET", "path": "/api/venues", "desc": "场馆列表（由活动聚合）"},
            {"method": "GET", "path": "/api/venues/{id}", "desc": "单个场馆 + 其活动"},
            {"method": "GET", "path": "/api/statistics", "desc": "统计信息"},
        ],
        "docs": "/docs",
    }


DOCS_HTML = """<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>童行 API 文档</title>
<style>
:root{{--bg:#0f1420;--card:#1a2233;--fg:#e6edf6;--mut:#8aa0bd;--acc:#5ac8fa;--line:#2a3650}}
*{{box-sizing:border-box}}body{{margin:0;font:14px/1.6 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--fg)}}
header{{padding:28px 24px 12px}}h1{{margin:0 0 4px;font-size:22px}}h2{{margin:28px 0 10px;font-size:17px;color:var(--acc);border-left:3px solid var(--acc);padding-left:10px}}
p.sub{{color:var(--mut);margin:2px 0 0}}
.wrap{{max-width:980px;margin:0 auto;padding:0 24px 60px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px 18px;margin:12px 0}}
code{{background:#0c1220;padding:1px 6px;border-radius:5px;color:#9be3a0;font-size:13px}}
.method{{display:inline-block;min-width:46px;text-align:center;font-weight:700;color:#0c1220;background:var(--acc);border-radius:5px;padding:1px 8px;margin-right:8px}}
.url{{color:#e6edf6;font-weight:600}}
table{{width:100%;border-collapse:collapse;margin-top:8px;font-size:13px}}
th,td{{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top}}
th{{color:var(--mut);font-weight:600}}
td.k{{color:#9be3a0;white-space:nowrap}}
td.t{{color:var(--mut)}}
ul{{margin:6px 0;padding-left:20px}}li{{margin:3px 0}}
.note{{color:var(--mut);font-size:12.5px;margin-top:6px}}
</style></head><body>
<header><h1>童行 (goout) · 数据 API 文档</h1>
<p class="sub">零依赖 · 直接读取 output/exhibitions_*.json · 支持跨域(CORS)</p></header>
<div class="wrap">

<h2>接口列表</h2>
<div class="card"><span class="method">GET</span><span class="url">/api/cities</span><div class="note">城市列表，返回每个城市的 code / 名称 / 活动数 / 场馆数</div></div>
<div class="card"><span class="method">GET</span><span class="url">/api/activities</span><div class="note">活动列表，支持过滤与分页（详见下）</div></div>
<div class="card"><span class="method">GET</span><span class="url">/api/activities/{"{id}"}</span><div class="note">单个活动详情（id 由 城市+标题+场馆+起止日期 生成）</div></div>
<div class="card"><span class="method">GET</span><span class="url">/api/venues</span><div class="note">场馆列表（由活动聚合，含官网链接 venue_url、活动数）</div></div>
<div class="card"><span class="method">GET</span><span class="url">/api/venues/{"{id}"}</span><div class="note">单个场馆详情 + 其下所有活动</div></div>
<div class="card"><span class="method">GET</span><span class="url">/api/statistics</span><div class="note">统计：城市 / 分类 / 收费 分布</div></div>

<h2>/api/activities 过滤参数</h2>
<div class="card"><table>
<tr><th>参数</th><th>类型</th><th>说明</th></tr>
<tr><td class="k">city</td><td class="t">string</td><td>城市 code，如 beijing / shanghai / shenzhen</td></tr>
<tr><td class="k">venue</td><td class="t">string</td><td>场馆名称精确匹配</td></tr>
<tr><td class="k">category</td><td class="t">string</td><td>分类，如 展览 / 演出 / 亲子 / 市集</td></tr>
<tr><td class="k">fee</td><td class="t">string</td><td>收费：免费 / 收费 / 部分免费 / 免费需预约 / 需购票</td></tr>
<tr><td class="k">family_friendly</td><td class="t">bool</td><td>true 仅返回亲子友好</td></tr>
<tr><td class="k">status</td><td class="t">string</td><td>all(默认) / ongoing(进行中) / upcoming(未开始) / ended(已结束)</td></tr>
<tr><td class="k">keyword</td><td class="t">string</td><td>模糊搜索 标题/场馆/描述/分类</td></tr>
<tr><td class="k">start_date</td><td class="t">date</td><td>仅返回结束日期 ≥ 该日的活动 (YYYY-MM-DD)</td></tr>
<tr><td class="k">end_date</td><td class="t">date</td><td>仅返回开始日期 ≤ 该日的活动 (YYYY-MM-DD)</td></tr>
<tr><td class="k">limit</td><td class="t">int</td><td>每页数量，默认 50，最大 500</td></tr>
<tr><td class="k">offset</td><td class="t">int</td><td>分页偏移，默认 0</td></tr>
</table><div class="note">返回结构：{"{"} "total":总条数, "limit":, "offset":, "data":[...] {"}"}</div></div>

<h2>活动对象字段 (Activity)</h2>
<div class="card"><table>
<tr><th>字段</th><th>类型</th><th>说明</th></tr>
<tr><td class="k">id</td><td class="t">string</td><td>稳定唯一 id（sha1 短码）</td></tr>
<tr><td class="k">title / name</td><td class="t">string</td><td>活动标题</td></tr>
<tr><td class="k">venue</td><td class="t">string</td><td>举办场馆</td></tr>
<tr><td class="k">city / city_name</td><td class="t">string</td><td>城市 code / 中文名</td></tr>
<tr><td class="k">start_date / end_date</td><td class="t">string</td><td>起止日期 (YYYY-MM-DD)</td></tr>
<tr><td class="k">status</td><td class="t">string</td><td>ongoing / upcoming / ended（接口计算）</td></tr>
<tr><td class="k">category</td><td class="t">string</td><td>分类</td></tr>
<tr><td class="k">fee</td><td class="t">string</td><td>收费类型</td></tr>
<tr><td class="k">family_friendly</td><td class="t">bool</td><td>是否亲子友好</td></tr>
<tr><td class="k">description</td><td class="t">string</td><td>活动简介</td></tr>
<tr><td class="k">link / url</td><td class="t">string</td><td>活动来源链接（多为本地宝汇总页）</td></tr>
<tr><td class="k">venue_url</td><td class="t">string</td><td>场馆官网直链（部分记录有）</td></tr>
<tr><td class="k">source</td><td class="t">string</td><td>数据来源（如 北京本地宝）</td></tr>
<tr><td class="k">contact</td><td class="t">string</td><td>联系电话</td></tr>
<tr><td class="k">booking_method</td><td class="t">object</td><td>预约/购票方式说明</td></tr>
<tr><td class="k">district / type / highlights</td><td class="t">string/list</td><td>区县 / 类型 / 亮点（视城市数据而定）</td></tr>
<tr><td class="k">verification</td><td class="t">object</td><td>可追溯核验信息（http_status 等）</td></tr>
</table></div>

<h2>场馆对象字段 (Venue)</h2>
<div class="card"><table>
<tr><th>字段</th><th>类型</th><th>说明</th></tr>
<tr><td class="k">id</td><td class="t">string</td><td>稳定唯一 id</td></tr>
<tr><td class="k">name</td><td class="t">string</td><td>场馆名称</td></tr>
<tr><td class="k">city / city_name</td><td class="t">string</td><td>城市 code / 中文名</td></tr>
<tr><td class="k">district / type</td><td class="t">string</td><td>区县 / 场馆类型</td></tr>
<tr><td class="k">venue_url</td><td class="t">string</td><td>场馆官网直链（已补全的）</td></tr>
<tr><td class="k">official_url</td><td class="t">string</td><td><b>场馆官方链接</b>（有则非空）</td></tr>
<tr><td class="k">third_party_url</td><td class="t">string</td><td><b>三方链接</b>（活动来源页，如本地宝），官方缺失时兜底</td></tr>
<tr><td class="k">url</td><td class="t">string</td><td><b>对外展示链接：优先 official_url，其次 third_party_url</b></td></tr>
<tr><td class="k">url_source</td><td class="t">string</td><td>official / third_party / 空</td></tr>
<tr><td class="k">links</td><td class="t">list</td><td><b>核验链接列表</b> [{url, label}]，优先官方，其次三方</td></tr>
<tr><td class="k">activity_count</td><td class="t">int</td><td>该场馆活动数</td></tr>
<tr><td class="k">activity_ids</td><td class="t">list</td><td>该场馆活动 id 列表</td></tr>
</table></div>

<h2>示例</h2>
<div class="card">
<ul>
<li><code>GET /api/cities</code></li>
<li><code>GET /api/activities?city=shenzhen&amp;fee=免费&amp;status=ongoing&amp;limit=10</code></li>
<li><code>GET /api/activities?city=beijing&amp;keyword=展览&amp;category=展览</code></li>
<li><code>GET /api/venues?city=shanghai</code></li>
<li><code>GET /api/statistics</code></li>
</ul>
<div class="note">所有接口返回 JSON，并已开启 CORS（Access-Control-Allow-Origin: *），可直接被浏览器 / 小程序 / 第三方调用。</div>
</div>
</div></body></html>"""


# --------------------------------------------------------------------------- #
# HTTP 处理
# --------------------------------------------------------------------------- #
def venue_public(v):
    """场馆对外输出：官方链接优先，三方链接兜底。

    返回字段：
      official_url     场馆官网（若有）
      third_party_url  活动来源页（如本地宝汇总页），作为兜底
      url              优先官方、其次三方（对外展示用）
      url_source       'official' / 'third_party' / ''
      links            核验链接列表 [{url, label}]
    """
    out = {k: val for k, val in v.items() if k != "activity_ids"}
    official = (v.get("venue_url") or "").strip()
    third = (v.get("third_party_url") or "").strip()
    out["official_url"] = official
    out["third_party_url"] = third
    out["url"] = official or third
    out["url_source"] = "official" if official else ("third_party" if third else "")
    links = []
    if official: links.append({"url": official, "label": "官方网站"})
    if third: links.append({"url": third, "label": "活动详情"})
    out["links"] = links
    return out


class Handler(BaseHTTPRequestHandler):
    DATA = None  # 类级缓存

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        if isinstance(body, (dict, list)):
            body = json.dumps(body, ensure_ascii=False)
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()
        self.wfile.write(body)

    def _qs(self):
        parsed = urllib.parse.urlparse(self.path)
        return parsed.path, dict(urllib.parse.parse_qsl(parsed.query, keep_blank_values=True))

    def do_OPTIONS(self):
        self._send(204, b"")

    def do_GET(self):
        path, q = self._qs()

        if path == "/" or path == "":
            return self._send(200, overview_json())

        if path == "/docs":
            return self._send(200, DOCS_HTML, "text/html; charset=utf-8")

        if path == "/api/reload":
            Handler.DATA = load_data()
            return self._send(200, {"ok": True, "activities": len(Handler.DATA["activities"]),
                                    "venues": len(Handler.DATA["venues"])})

        if path == "/api/cities":
            return self._send(200, sorted(Handler.DATA["cities"], key=lambda c: c["code"]))

        if path == "/api/statistics":
            return self._send(200, self._statistics())

        if path == "/api/activities":
            return self._send(200, self._activities(q))

        if path == "/api/venues":
            return self._send(200, self._venues(q))

        # /api/activities/{id}
        m = re.match(r"^/api/activities/([\w]+)$", path)
        if m:
            aid = m.group(1)
            for a in Handler.DATA["activities"]:
                if a["id"] == aid:
                    return self._send(200, a)
            return self._send(404, {"error": "activity not found", "id": aid})

        # /api/venues/{id}
        m = re.match(r"^/api/venues/([\w]+)$", path)
        if m:
            vid = m.group(1)
            for v in Handler.DATA["venues"]:
                if v["id"] == vid:
                    acts = [a for a in Handler.DATA["activities"] if a["id"] in v["activity_ids"]]
                    out = venue_public(v)
                    out["activities"] = acts
                    return self._send(200, out)
            return self._send(404, {"error": "venue not found", "id": vid})

        return self._send(404, {"error": "not found", "path": path})

    # ---- 业务方法 ----
    def _paginate(self, items, q):
        try:
            limit = max(1, min(500, int(q.get("limit", "50"))))
        except ValueError:
            limit = 50
        try:
            offset = max(0, int(q.get("offset", "0")))
        except ValueError:
            offset = 0
        total = len(items)
        return {"total": total, "limit": limit, "offset": offset,
                "data": items[offset:offset + limit]}

    def _activities(self, q):
        items = filter_activities(Handler.DATA["activities"], q)
        # 默认按开始日期升序
        items.sort(key=lambda a: a.get("start_date") or "9999")
        return self._paginate(items, q)

    def _venues(self, q):
        items = filter_venues(Handler.DATA["venues"], q)
        items.sort(key=lambda v: (v["city"], -v["activity_count"], v["name"]))
        # 输出：官方链接优先，三方兜底（不返回冗长的 activity_ids）
        clean = [venue_public(v) for v in items]
        return self._paginate(clean, q)

    def _statistics(self):
        acts = Handler.DATA["activities"]
        by_city = {}
        by_cat = {}
        by_fee = {}
        for a in acts:
            c = a.get("city_name") or a.get("city")
            by_city[c] = by_city.get(c, 0) + 1
            cat = a.get("category") or "未分类"
            by_cat[cat] = by_cat.get(cat, 0) + 1
            fee = a.get("fee") or "未知"
            by_fee[fee] = by_fee.get(fee, 0) + 1
        return {
            "activity_total": len(acts),
            "venue_total": len(Handler.DATA["venues"]),
            "city_total": len(Handler.DATA["cities"]),
            "by_city": sorted(by_city.items(), key=lambda x: -x[1]),
            "by_category": sorted(by_cat.items(), key=lambda x: -x[1]),
            "by_fee": sorted(by_fee.items(), key=lambda x: -x[1]),
        }

    def log_message(self, fmt, *args):
        sys.stderr.write("[api] " + (fmt % args) + "\n")


def main():
    Handler.DATA = load_data()
    print(f"已加载 {len(Handler.DATA['activities'])} 条活动 / "
          f"{len(Handler.DATA['venues'])} 个场馆 / "
          f"{len(Handler.DATA['cities'])} 个城市")
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"童行 API 已启动: http://{HOST}:{PORT}  (本地预览 http://127.0.0.1:{PORT})")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止")
        server.shutdown()


if __name__ == "__main__":
    main()
