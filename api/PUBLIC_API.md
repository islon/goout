# 童行 (goout) 公开数据接口

童行的城市亲子活动 / 场馆数据已**公开在 GitHub Pages**，任何人都能直接调用，无需 token。

数据地址（已开启 `Access-Control-Allow-Origin: *`，浏览器 / 任意后端均可跨域 `fetch`）：

```
https://islon.github.io/goout/output/exhibitions_{城市}.json
```

城市代码：`beijing` `shanghai` `guangzhou` `shenzhen` `hangzhou` `chengdu` `chongqing` `nanjing` `wuhan` `xian`

示例：
- 北京全部活动 → `https://islon.github.io/goout/output/exhibitions_beijing.json`
- 深圳全部活动 → `https://islon.github.io/goout/output/exhibitions_shenzhen.json`

---

## 方式一：直接 fetch 公开 JSON（最简单，零部署）

适合前端 / 小程序 / 脚本直接拿全量数据，再在本地做过滤。

```js
const res = await fetch("https://islon.github.io/goout/output/exhibitions_beijing.json");
const data = await res.json();
// data 是活动数组，字段见文末「数据字段」
```

```bash
curl https://islon.github.io/goout/output/exhibitions_shanghai.json
```

> 调试台（纯前端，已部署）：<https://islon.github.io/goout/api/explorer.html>
> 可按城市 / 收费 / 状态 / 关键词筛选，并一键复制调用代码。

---

## 方式二：REST 接口（带服务端过滤 + 分页）

公开 JSON 是「全量文件」，没有 `?city=北京&fee=免费` 这种过滤能力。
如果你想要真正的 REST 接口，仓库里提供了 **Cloudflare Worker**（`api/worker.js`），
读取上面的公开 JSON，对外提供带过滤 / 分页的 REST + CORS，**免费、自带公网域名**。

### 部署（一次性，约 1 分钟）

```bash
npm i -g wrangler
wrangler login          # 浏览器授权 Cloudflare 账号
wrangler deploy         # 读取本仓库 wrangler.toml
```

部署后得到：`https://goout-api.<你的子域>.workers.dev`

### 接口（与本地 `api/json_api.py` 完全一致）

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/cities` | 城市列表（含活动数 / 场馆数） |
| GET | `/api/activities` | 活动列表，支持过滤 + 分页 |
| GET | `/api/activities/{id}` | 单个活动详情 |
| GET | `/api/venues` | 场馆列表（由活动聚合，官方链接优先） |
| GET | `/api/venues/{id}` | 单个场馆 + 其活动 |
| GET | `/api/statistics` | 统计（按城市 / 收费 / 分类） |

`/api/activities` 与 `/api/venues` 支持的查询参数：

`city`(城市代码) · `venue`(场馆名) · `category`(分类) · `fee`(免费/收费/需购票…)
· `status`(ongoing/upcoming/ended) · `family_friendly`(true/false) · `keyword`(关键词)
· `start_date` / `end_date`(日期区间) · `page` · `limit`(≤200)

```bash
# 深圳正在进行中的免费活动
curl "https://goout-api.xxx.workers.dev/api/activities?city=shenzhen&fee=免费&status=ongoing"
```

---

## 场馆链接优先级（所有接口统一）

场馆对象同时给出：

- `official_url` —— 场馆**官方网站**（优先）
- `third_party_url` —— 活动来源页（多为本地宝汇总页，官方缺失时兜底）
- `url` —— **对外展示用**，有官方用官方，否则用三方
- `url_source` —— `official` / `third_party` / 空

目前 2580 个场馆中已有 60 个补全了官方链接，其余自动回退三方来源页，不会空链。

---

## 数据字段（活动）

| 字段 | 说明 |
|------|------|
| `id` | 稳定唯一 id（Worker / 本地接口一致） |
| `title` / `name` | 活动名称 |
| `venue` | 场馆名称 |
| `city` / `city_name` | 城市代码 / 中文名 |
| `start_date` / `end_date` | 起止日期 `YYYY-MM-DD` |
| `status` | ongoing / upcoming / ended（接口计算） |
| `category` | 分类 |
| `fee` | 免费 / 免费需预约 / 收费 / 部分免费 / 需购票 |
| `family_friendly` | 是否亲子友好 |
| `description` | 简介 |
| `link` | 活动来源页（多为本地宝） |
| `venue_url` | 场馆官网直链（已补全的场馆有值） |
| `source` / `contact` / `booking_method` | 来源 / 联系方式 / 预约方式 |
| `verification` | 可追溯核验信息（含 `verified_at`、`http_status`、`verified_by`） |

---

## 本地自托管

不依赖任何外部服务，直接用 Python 标准库读本地 JSON：

```bash
PORT=8787 python3 api/json_api.py
# 文档页： http://127.0.0.1:8787/docs
```
