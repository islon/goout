# 深圳展览日历 - 项目文档

## 一、项目概述

本项目旨在创建一个深圳展览日历系统，整合深圳会展中心和深圳国际会展中心的展览日程数据，提供标准化的 iCalendar (.ics) 订阅服务，让用户可以在 iOS 和 Android 手机上一键订阅展览日程。

---

## 二、功能需求

### 2.1 核心功能

| 功能 | 描述 | 优先级 |
|------|------|--------|
| 数据爬取 | 自动抓取深圳两大会展中心的展览数据 | 高 |
| ICS 生成 | 将展览数据转换为标准 iCalendar 格式 | 高 |
| 一键订阅 | 用户点击按钮即可订阅日历 | 高 |
| 自动更新 | 定期更新展览数据 | 高 |

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