# 深圳展览日历 - 项目文档

## 一、项目概述

本项目旨在创建一个深圳展览日历系统，整合深圳会展中心和深圳国际会展中心的展览日程数据，提供标准化的 iCalendar (.ics) 订阅服务，让用户可以在 iOS 和 Android 手机上一键订阅展览日程。

---

## 二、功能需求

### 2.1 核心功能

| 功能 | 描述 | 优先级 |
|------|------|--------|
| 数据爬取 | 自动抓取深圳各场馆的展览活动数据 | 高 |
| ICS 生成 | 将展览数据转换为标准 iCalendar 格式 | 高 |
| 一键订阅 | 用户点击按钮即可订阅日历 | 高 |
| 自动更新 | 定期更新展览数据 | 高 |
| 访问统计 | 匿名统计网站访问量、订阅次数、活动点击情况 | 中 |

### 2.2 订阅方式

- **iOS 用户**：点击订阅按钮 → 自动打开「日历」应用 → 点击「添加全部」完成订阅
- **Android 用户**：点击订阅按钮 → 选择「Google 日历」打开 → 点击「添加」完成订阅
- **微信分享**：通过微信分享链接，用户打开后按上述方式订阅

---

## 三、技术方案

### 3.1 架构设计

```
┌─────────────────────────────────────────────────────────────┐
│                      数据爬取层                              │
│  ┌─────────────────────┐  ┌─────────────────────────────┐   │
│  │ scraper_szcec.py    │  │ scraper_shenzhen_world.py   │   │
│  │ 深圳会展中心爬虫     │  │ 深圳国际会展中心爬虫         │   │
│  └──────────┬──────────┘  └────────────────┬────────────┘   │
│             │                              │                │
└─────────────┼──────────────────────────────┼────────────────┘
              ▼                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      数据处理层                              │
│                     main.py                                 │
│              整合数据 → 排序 → 保存                          │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                      文件生成层                              │
│                   ics_generator.py                          │
│              JSON → iCalendar (.ics)                        │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                      展示层                                  │
│                     index.html                              │
│              落地页 + 订阅按钮 + iOS/Android 教程             │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 文件结构

```
展览活动/
├── index.html                    # 落地页
├── config.py                     # 配置文件
├── requirements.txt              # Python 依赖
├── .gitignore                    # Git 忽略文件
├── .github/
│   └── workflows/
│       └── update.yml            # GitHub Actions 自动更新
├── output/
│   ├── exhibitions.json          # 展览数据（JSON）
│   └── exhibitions.ics           # iCalendar 文件
└── scripts/
    ├── main.py                   # 主脚本
    ├── scraper_szcec.py          # 深圳会展中心爬虫
    ├── scraper_shenzhen_world.py # 深圳国际会展中心爬虫
    └── ics_generator.py          # ICS 文件生成器
```

### 3.3 关键技术

| 技术 | 说明 |
|------|------|
| iCalendar (.ics) | 标准日历订阅格式，iOS/Android 原生支持 |
| webcal:// 协议 | iOS 日历订阅专用协议 |
| Python 爬虫 | requests + BeautifulSoup |
| GitHub Pages | 静态网站托管 |
| GitHub Actions | 定期自动更新数据 |

---

## 四、数据来源

### 4.1 深圳会展中心 (SZCEC)

- 官网：http://www.szcec.com
- 数据页：/szcec/cn-schedule/review/index.html

### 4.2 深圳国际会展中心 (Shenzhen World)

- 第三方平台：www.wuzhanliuhui.com

### 4.3 数据字段

| 字段 | 类型 | 说明 |
|------|------|------|
| name | string | 展会名称 |
| venue | string | 场馆名称 |
| start_date | string | 开始日期 (YYYY-MM-DD) |
| end_date | string | 结束日期 (YYYY-MM-DD) |
| url | string | 详情链接 |
| contact | string | 联系方式 |

---

## 五、部署方案

### 5.1 GitHub Pages 部署

1. 创建 GitHub 仓库：`https://github.com/islon/shenzhen-exhibitions`
2. 启用 GitHub Pages：Settings → Pages → Source: main / (root)
3. 访问地址：`https://islon.github.io/shenzhen-exhibitions/`

### 5.2 自动更新

通过 GitHub Actions 每周日自动运行爬虫更新数据：

```yaml
name: Update Exhibition Data
on:
  schedule:
    - cron: '0 0 * * 0'
  workflow_dispatch:
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - run: pip install -r requirements.txt
      - run: python scripts/main.py
      - run: git add output/ && git commit -m "chore: update exhibition data"
      - uses: ad-m/github-push-action@master
```

---

## 六、使用方式

### 6.1 用户订阅

1. 打开落地页：`https://islon.github.io/shenzhen-exhibitions/`
2. 点击「添加到我的日历」按钮
3. 按照提示完成订阅

### 6.2 手动更新数据

```bash
cd /Users/longxiansheng/Documents/trae_projects/展览活动
source venv/bin/activate
python scripts/main.py
```

---

## 七、访问链接

| 链接类型 | URL |
|----------|-----|
| 落地页 | https://islon.github.io/shenzhen-exhibitions/ |
| ICS 文件 | https://islon.github.io/shenzhen-exhibitions/output/exhibitions.ics |
| 订阅链接 | webcal://islon.github.io/shenzhen-exhibitions/output/exhibitions.ics |
| GitHub 仓库 | https://github.com/islon/shenzhen-exhibitions |

---

## 八、注意事项

1. **数据准确性**：展览数据来源于第三方平台，如有变动请以官方公告为准
2. **订阅同步**：订阅后日历会自动同步更新，无需重复订阅
3. **网络要求**：首次订阅需要网络连接，后续可离线查看
4. **平台兼容**：支持 iOS 日历和 Android Google 日历，其他日历应用可能需要手动导入 ICS 文件

---

## 九、统计功能

### 9.1 统计方式

本项目集成了两种统计方式：

| 方式 | 说明 | 数据范围 |
|------|------|---------|
| **不蒜子** | 页面访问量和访客数统计，无需注册 | 公开显示在页面上 |
| **百度统计** | 详细的用户行为分析，需注册账号 | 后台查看详细数据 |

### 9.2 统计事件

| 页面 | 事件分类 | 事件名称 | 说明 |
|------|---------|---------|------|
| index.html | 订阅 | iOS添加日历 | 用户点击iOS订阅按钮 |
| index.html | 订阅 | Android下载日历 | 用户下载Android日历文件 |
| index.html | 订阅 | Android复制链接 | 用户复制Android订阅链接 |
| schedule.html | 活动详情 | 打开弹窗 | 用户点击活动卡片 |
| schedule.html | 活动详情 | 点击原始链接 | 用户点击查看原始活动链接 |

### 9.3 启用百度统计

1. 注册百度统计账号：https://tongji.baidu.com
2. 新增网站，获取统计ID（格式：`12345678`）
3. 替换以下文件中的 `你的百度统计ID`：
   - `index.html` 第739行
   - `schedule.html` 第689行
4. 提交推送更新

### 9.4 隐私保护

- **匿名统计**：不收集任何个人敏感信息（姓名、手机号、邮箱等）
- **仅收集**：页面访问量、设备类型、浏览器信息、自定义事件
- **用户提示**：页面显示"本站使用匿名统计，不收集任何个人信息"