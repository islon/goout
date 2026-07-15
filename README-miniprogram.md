# 童行 · 微信小程序

全国亲子活动日历微信小程序版本，基于微信云开发。

## 功能

- 📅 活动日历浏览（支持分类/城市/免费/亲子筛选）
- 📋 活动详情查看
- 🔔 订阅提醒（微信订阅消息，活动开始前一天 9:00 推送）
- 👤 我的订阅管理

## 技术架构

```
miniprogram/        # 小程序前端
├── app.js          # 应用入口，初始化云开发
├── app.json        # 全局配置
├── pages/
│   ├── index/      # 活动列表页（首页，实时拉取）
│   ├── detail/     # 活动详情页（含订阅按钮）
│   └── mine/       # 我的订阅页
├── data/
│   └── activities.json  # 兜底数据（云函数不可用时使用）
└── utils/

cloudfunctions/     # 云函数
├── getActivities/  # 实时拉取 Web 版数据（无需数据库）
├── subscribe/      # 订阅/取消订阅
└── sendReminder/   # 定时发送提醒（每天8:00触发）
```

## 数据自动同步（核心特性）

小程序**不打包活动数据**，而是运行时通过云函数 `getActivities` 实时拉取
[童行 Web 版](https://islon.github.io/goout) 的 `output/exhibitions.json`。

> **你在 GitHub 上更新网页数据并部署后，小程序自动跟随，无需改小程序代码、无需重新上传审核。**

- 列表页打开时调用云函数拉取最新数据，并缓存到本地 storage
- 详情页 / 我的订阅页从同一份缓存读取，保证按索引精确对应
- 云函数不可用时自动降级到本地 `activities.json`，不白屏

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
- `getActivities` 必须部署，否则列表走本地兜底数据（非实时）

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
当前约 1187 条活动：深圳 801、北京 156、上海 111、广州 71、杭州 48。
本地 `miniprogram/data/activities.json` 仅作云函数不可用时的兜底。

## License

MIT
