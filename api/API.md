# 童行 (goout) · 城市场馆 / 活动数据 API

基于 `output/exhibitions_<city>.json` 的**零依赖** REST 接口（仅用 Python 标准库），
可直接被网页、小程序、第三方服务调用（已开启 CORS：`Access-Control-Allow-Origin: *`）。

## 启动

```bash
python3 api/json_api.py            # 默认监听 0.0.0.0:8787
PORT=9000 python3 api/json_api.py  # 自定义端口
```

启动后访问：
- `http://127.0.0.1:8787/`     接口概览（JSON）
- `http://127.0.0.1:8787/docs`  接口文档（HTML，人可读）

## 当前数据规模

| 指标 | 数量 |
|------|------|
| 城市 | 10（北京/上海/广州/深圳/杭州/成都/重庆/南京/武汉/西安） |
| 活动 | 5024 |
| 场馆 | 2580 |

> 数据含本批新增的 95 条 7–8 月活动（已标注 `verification.verified_at=2026-07-19`），
> 以及已补全的 60 条场馆官网直链 `venue_url`。

## 接口一览

### 1. `GET /api/cities`
城市列表，含活动数 / 场馆数。
```json
[{ "code": "beijing", "name": "北京", "activity_count": 514, "venue_count": 353 }]
```

### 2. `GET /api/activities`
活动列表，支持过滤 + 分页。

**查询参数**

| 参数 | 类型 | 说明 |
|------|------|------|
| `city` | string | 城市 code，如 `beijing` / `shenzhen` |
| `venue` | string | 场馆名称（精确匹配） |
| `category` | string | 分类，如 `展览` / `演出` / `亲子` / `市集` |
| `fee` | string | 收费：`免费` / `收费` / `部分免费` / `免费需预约` / `需购票` |
| `family_friendly` | bool | `true` 仅返回亲子友好 |
| `status` | string | `all`(默认) / `ongoing`(进行中) / `upcoming`(未开始) / `ended`(已结束) |
| `keyword` | string | 模糊搜索 标题/场馆/描述/分类 |
| `start_date` | date | 仅返回结束日期 ≥ 该日 (YYYY-MM-DD) |
| `end_date` | date | 仅返回开始日期 ≤ 该日 (YYYY-MM-DD) |
| `limit` | int | 每页数量，默认 50，最大 500 |
| `offset` | int | 分页偏移，默认 0 |

**返回**
```json
{ "total": 141, "limit": 2, "offset": 0, "data": [ /* Activity 对象 */ ] }
```

**示例**
```
/api/activities?city=shenzhen&fee=免费&status=ongoing&limit=10
/api/activities?city=beijing&keyword=展览&category=展览
```

### 3. `GET /api/activities/{id}`
单个活动详情。`id` 由 `城市+标题+场馆+起止日期` 生成的稳定短码（sha1 前 12 位）。

### 4. `GET /api/venues`
场馆列表（由活动聚合），支持 `city` / `keyword` / `limit` / `offset`。
每个场馆含：名称、城市、区县、类型、**官网直链 `venue_url`**、活动数。

### 5. `GET /api/venues/{id}`
单个场馆详情 + 其下所有活动列表。

### 6. `GET /api/statistics`
统计分布：按城市 / 分类 / 收费。

### 7. `GET /api/reload`
重新从磁盘加载 JSON（数据更新后无需重启）。

## 活动对象字段 (Activity)

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | string | 稳定唯一 id（sha1 短码） |
| `title` / `name` | string | 活动标题 |
| `venue` | string | 举办场馆 |
| `city` / `city_name` | string | 城市 code / 中文名 |
| `start_date` / `end_date` | string | 起止日期 (YYYY-MM-DD) |
| `status` | string | `ongoing` / `upcoming` / `ended`（接口实时计算） |
| `category` | string | 分类 |
| `fee` | string | 收费类型 |
| `family_friendly` | bool | 是否亲子友好 |
| `description` | string | 活动简介 |
| `link` / `url` | string | 活动来源链接（多为本地宝汇总页） |
| `venue_url` | string | 场馆官网直链（部分记录有） |
| `source` | string | 数据来源（如 北京本地宝） |
| `contact` | string | 联系电话 |
| `booking_method` | object | 预约/购票方式说明 |
| `district` / `type` / `highlights` | string/list | 区县 / 类型 / 亮点（视城市而定） |
| `verification` | object | 可追溯核验信息（`http_status` 等） |

## 场馆对象字段 (Venue)

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | string | 稳定唯一 id |
| `name` | string | 场馆名称 |
| `city` / `city_name` | string | 城市 code / 中文名 |
| `district` / `type` | string | 区县 / 场馆类型 |
| `venue_url` | string | 场馆官网直链（已补全的；见下方链接优先级） |
| `official_url` | string | **场馆官方链接**（有则非空） |
| `third_party_url` | string | **三方链接**（活动来源页，多为本地宝汇总页），作为官方缺失时的兜底 |
| `url` | string | **对外展示用链接：优先 `official_url`，其次 `third_party_url`** |
| `url_source` | string | 链接来源：`official` / `third_party` / `""` |
| `activity_count` | int | 该场馆活动数 |
| `activity_ids` | list | 该场馆活动 id 列表（列表接口不返回，详情接口返回完整活动） |

### 场馆链接优先级规则
所有场馆对外暴露的 `url` 字段遵循：**官方链接优先，三方链接兜底**。
- 若场馆有官网（`official_url` 非空）→ `url = official_url`，`url_source = "official"`。
- 否则 → `url = third_party_url`（活动来源页，如本地宝），`url_source = "third_party"`。

> 当前数据：2580 个场馆中已有 **60 个**补全了官方链接（如鸟巢 n-s.cn、中华世纪坛 worldartmuseum.cn、上海博物馆东馆 shanghaimuseum.net、成都永陵博物馆 cdylbwg.org.cn、南京银杏湖乐园 gingkolake.com、中国光谷科技会展中心 covcec.com 等），其余场馆自动回退到三方来源页，不会出现空链接。

## 说明
- 与旧版 `api/server.py`（依赖不存在的 `data/goout.db` 且需 FastAPI）不同，本接口
  **无需任何依赖**，直接读取真实 JSON 数据，开箱即跑。
- 所有日期为 `YYYY-MM-DD`；`status` 由服务端按今天动态计算。
- 已过滤参数中的中文请按标准 URL 编码（浏览器 / `fetch` / `requests` 会自动处理）。
