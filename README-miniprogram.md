# 童行 · 微信小程序

全国亲子活动日历微信小程序版本，基于微信云开发。

## 功能

- 🏛️ 场馆指南浏览（按城市 / 类型筛选、关键词搜索，即使没有活动也值得一去）
- 📅 活动日历浏览（支持分类 / 城市 / 时间 / 免费 / 收费 / 亲子筛选 + 关键词搜索）
- 📋 活动 / 场馆详情查看
- 🔔 订阅提醒（微信订阅消息，活动开始前一天 9:00 推送）
- 👤 我的订阅管理
- 🔄 列表页支持下拉刷新，随时拉取最新数据

## 技术架构

```
miniprogram/        # 小程序前端
├── app.js          # 应用入口，初始化云开发
├── app.json        # 全局配置（含 活动 / 场馆 / 我的 三个 tab）
├── pages/
│   ├── index/      # 活动列表页（首页，实时拉取 + 搜索 + 下拉刷新）
│   ├── detail/     # 活动详情页（含订阅按钮）
│   ├── venues/     # 场馆指南列表页（城市/类型筛选 + 搜索）
│   ├── venueDetail/# 场馆详情页
│   └── mine/       # 我的订阅页
├── data/
│   ├── activities.json  # 兜底数据（云函数不可用时使用）
│   └── venues.json      # 场馆兜底数据
└── assets/         # tabBar 图标

cloudfunctions/     # 云函数
├── getActivities/  # 实时拉取 Web 版活动数据（无需数据库）
├── getVenues/      # 实时拉取 Web 版场馆数据（无需数据库）
├── subscribe/      # 订阅/取消订阅
└── sendReminder/   # 定时发送提醒（每天8:00触发）
```

## 数据自动同步（核心特性）

小程序**不打包活动数据**，而是运行时通过云函数 `getActivities` 实时拉取
[童行 Web 版](https://islon.github.io/goout) 的 `output/exhibitions.json`；场馆指南同理，
通过云函数 `getVenues` 实时拉取 `output/venue_info.json`。

> **你在 GitHub 上更新网页数据并部署后，小程序自动跟随，无需改小程序代码、无需重新上传审核。**

- 列表页打开时调用云函数拉取最新数据，并缓存到本地 storage
- 详情页 / 我的订阅页从同一份缓存读取，保证按索引精确对应
- 云函数不可用时自动降级到本地 `activities.json` / `venues.json`，不白屏
- 下拉刷新可随时强制重新拉取最新数据

## 使用前需要做的

### 1. 注册小程序
- 去 [mp.weixin.qq.com](https://mp.weixin.qq.com) 注册个人小程序
- 获取 AppID，填入 `project.config.json` 的 `appid` 字段

### 2. 开通云开发
- 在微信开发者工具中打开项目
- 点击「云开发」按钮，创建环境
- 将环境 ID 填入 `miniprogram/app.js` 的 `env` 字段

### 3. 创建数据库集合
在云开发控制台创建以下集合（仅需 `subscriptions`，活动数据走云函数实时拉取，无需建表）：
- `subscriptions` — 用户订阅记录

### 4. 创建订阅消息模板
- 在小程序后台 → 订阅消息 → 公共模板库中申请模板
- 推荐模板：**活动提醒通知**
- 将模板 ID 填入以下文件：
  - `miniprogram/pages/detail/detail.js` 中的 `tmplIds`
  - `cloudfunctions/sendReminder/index.js` 中的 `templateId`

### 5. 部署云函数
- 在微信开发者工具中，右键每个云函数文件夹
- 选择「上传并部署：云端安装依赖」
- 为 `sendReminder` 配置定时触发器（已在 `config.json` 中配置）
- `getActivities` 与 `getVenues` 必须部署，否则活动 / 场馆列表走本地兜底数据（非实时）

### 6. 创建 tabBar 图标
- 在 `miniprogram/assets/` 目录下放置以下图标（81×81px PNG）：
  - `tab-home.png` / `tab-home-active.png`
  - `tab-mine.png` / `tab-mine-active.png`
- 或暂时在 `app.json` 中移除 `tabBar` 的 `iconPath` 字段

## 订阅消息流程

```
用户点击「提醒我」
       ↓
wx.requestSubscribeMessage 弹出授权弹窗
       ↓
用户点击「允许」
       ↓
调用 subscribe 云函数，记录到 subscriptions 集合
       ↓
每天 8:00，sendReminder 云函数定时触发
       ↓
查找 remindTime <= now 且 notified = false 的记录
       ↓
调用 cloud.openapi.subscribeMessage.send 发送提醒
       ↓
标记 notified = true
```

## 数据来源

活动数据**实时来自** [童行 Web 版](https://islon.github.io/goout)（GitHub Pages 自动部署），
当前约 1138 条活动，覆盖深圳、广州、上海、北京、杭州五城。
本地 `miniprogram/data/activities.json` 仅作云函数不可用时的兜底（已与线上格式保持一致）。

场馆数据**实时来自** Web 版的 `output/venue_info.json`，当前约 146 个场馆（以深圳为主，
另含广州 / 上海 / 北京 / 杭州）。本地 `miniprogram/data/venues.json` 为兜底。

> **关于「区县筛选」**：Web 版导出的 `exhibitions.json` 当前不含 `district` / `venue_type`
> 字段，因此小程序在走实时数据时区县联动筛选会自动隐藏（代码保留，待数据源补齐后自动生效）。
> 详情页的场馆类型、区县信息也会在字段存在时才展示。

## 合规检测机制（中国大陆）

为确保内容符合中国法律法规，系统在以下环节进行合规检测：

### 检测环节

| 环节 | 文件 | 说明 |
|------|------|------|
| 数据导入 | `scripts/db_import.py` | 导入 SQLite 前过滤 |
| 数据文件 | `scripts/compliance_check.py` | 独立检测脚本 |
| 云函数返回 | `cloudfunctions/getActivities/index.js` | 返回前端前过滤 |
| 小程序前端 | `miniprogram/utils/compliance.js` | 可选，二次检测 |

### 敏感词类别

- **政治敏感词**：台独、藏独、疆独、法轮功等
- **暴力恐怖**：恐怖袭击、ISIS、基地组织等
- **色情低俗**：嫖娼、卖淫、淫秽等
- **毒品相关**：冰毒、海洛因等
- **赌博相关**：网络赌博、六合彩等
- **地区主权**：中华民国、台湾共和国等

### 白名单

以下正常词汇不会误判：
- 北京地铁站名：天安门东站、天安门西站等
- 革命历史场馆：农民运动讲习所、农讲所等

### 使用方法

```bash
# 检测活动数据
python3 scripts/compliance_check.py output/exhibitions.json

# 检测场馆数据
python3 scripts/compliance_check.py output/venue_info.json
```

检测通过会返回 `✅ 所有内容合规`，不通过会列出具体违规记录。

## License

MIT
