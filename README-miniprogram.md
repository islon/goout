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
│   ├── index/      # 活动列表页（首页）
│   ├── detail/     # 活动详情页（含订阅按钮）
│   └── mine/       # 我的订阅页
├── data/
│   └── activities.json  # 活动数据（403条）
└── utils/

cloudfunctions/     # 云函数
├── getActivities/  # 获取活动列表
├── subscribe/      # 订阅/取消订阅
└── sendReminder/   # 定时发送提醒（每天8:00触发）
```

## 使用前需要做的

### 1. 注册小程序
- 去 [mp.weixin.qq.com](https://mp.weixin.qq.com) 注册个人小程序
- 获取 AppID，填入 `project.config.json` 的 `appid` 字段

### 2. 开通云开发
- 在微信开发者工具中打开项目
- 点击「云开发」按钮，创建环境
- 将环境 ID 填入 `miniprogram/app.js` 的 `env` 字段

### 3. 创建数据库集合
在云开发控制台创建以下集合：
- `activities` — 活动数据
- `subscriptions` — 用户订阅记录

### 4. 导入活动数据
- 将 `miniprogram/data/activities.json` 导入 `activities` 集合
- 或使用云函数 `getActivities` 从本地数据加载

### 5. 创建订阅消息模板
- 在小程序后台 → 订阅消息 → 公共模板库中申请模板
- 推荐模板：**活动提醒通知**
- 将模板 ID 填入以下文件：
  - `miniprogram/pages/detail/detail.js` 中的 `tmplIds`
  - `cloudfunctions/sendReminder/index.js` 中的 `templateId`

### 6. 部署云函数
- 在微信开发者工具中，右键每个云函数文件夹
- 选择「上传并部署：云端安装依赖」
- 为 `sendReminder` 配置定时触发器（已在 `config.json` 中配置）

### 7. 创建 tabBar 图标
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

活动数据来自 [童行 Web 版](https://islon.github.io/goout)，共 403 条活动（深圳 355 条、北京 21 条、上海 16 条、广州 11 条）。

## License

MIT
