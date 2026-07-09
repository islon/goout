# 数据收集文档

## 项目概述

本项目收集深圳主要场馆的展览活动信息，为市民提供一站式活动查询服务。

## 数据来源

### 场馆列表

| 场馆名称 | 数据源标识 | 官方网站 | 区县 |
|---------|-----------|---------|------|
| 深圳会展中心 | szcec | http://www.szcec.com | 福田区 |
| 深圳国际会展中心 | shenzhen_world | http://www.shenzhen-world.com | 宝安区 |
| 深圳图书馆 | szlib | http://www.szlib.org.cn | 福田区 |
| 宝安图书馆 | balib | http://www.balib.cn | 宝安区 |
| 湾区之眼 | bayarea_eye | http://www.bayareaeye.com | 宝安区 |
| 宝安科技馆 | baoan_kjg | http://www.baoankjg.com | 宝安区 |
| 宝安体育中心 | baoan_ty | http://www.baoantiyuzhongxin.com | 宝安区 |
| **南山图书馆** | nslib | https://activity.nslib.cn | 南山区 |
| **南山博物馆** | nsmuseum | https://www.nanshanmuseum.com | 南山区 |
| **南山区文化馆** | nswhg | https://whgy.szmassart.com/nsqwhg | 南山区 |

### 数据采集方式

1. **会展中心类**：通过官网展会日历、公众号推送、行业协会发布获取
2. **图书馆类**：通过官网活动预告、微信公众号、读者服务系统获取
   - **南山图书馆**：使用活动系统API（https://activity.nslib.cn），获取报名活动数据
3. **科技馆类**：通过官网活动公告、科普活动报名系统获取
4. **体育中心类**：通过赛事官网、票务平台、场馆公告获取
5. **艺术场馆类**：通过展览官网、艺术平台、场馆公告获取
6. **博物馆类**：
   - **南山博物馆**：官网展览信息+活动公告（SPA网站，需解析API）
7. **文化馆类**：
   - **南山区文化馆**：深圳文化馆云平台活动预约系统

### 新增场馆开发步骤

1. 在 `config.py` 添加场馆配置
2. 创建 `scripts/scraper_xxx.py` 数据采集脚本
3. 在 `schedule.html` 添加：
   - 地点筛选按钮（data-source）
   - 区县映射（districtMapping）
   - 卡片颜色样式（.exhibition-card.xxx）
4. 运行脚本测试数据采集
5. 提交推送更新

## 数据字段说明

| 字段名 | 类型 | 说明 | 示例 |
|-------|------|------|------|
| name | string | 活动名称 | 深圳国际玩具展 |
| venue | string | 场馆名称 | 深圳会展中心 |
| start_date | string | 开始日期(YYYY-MM-DD) | 2026-07-08 |
| end_date | string | 结束日期(YYYY-MM-DD) | 2026-07-10 |
| url | string | **活动详情链接（原始链接）** | http://www.szcec.com |
| contact | string | 联系电话 | 0755-82848888 |
| description | string | 活动描述 | 包含时间、地点、活动介绍 |
| source | string | 数据源标识 | szcec |
| family_friendly | boolean | 是否适合亲子 | true |

## 数据刷新流程

```bash
# 进入项目目录
cd /workspace/goout

# 运行单个场馆数据采集
python3 scripts/scraper_nslib.py    # 南山图书馆
python3 scripts/scraper_nsmuseum.py # 南山博物馆
python3 scripts/scraper_nswhg.py    # 南山区文化馆

# 运行数据合并脚本
python3 scripts/fix_data.py

# 提交更新到GitHub
git add output/exhibitions.json
git commit -m "fix(data): regenerate activity data"
git push origin main
```

## 文件结构

```
展览活动/
├── output/
│   ├── exhibitions.json    # 主数据文件（JSON格式）
│   ├── exhibitions.ics     # 日历格式输出
│   └── exhibitions.rss     # RSS订阅格式
├── scripts/
│   ├── fix_data.py         # 数据生成脚本（主要）
│   ├── scraper_nslib.py    # 南山图书馆数据采集
│   ├── scraper_nsmuseum.py # 南山博物馆数据采集
│   ├── scraper_nswhg.py    # 南山区文化馆数据采集
│   └── *.py                # 其他辅助脚本
├── config.py               # 场馆配置
├── index.html              # 首页
├── schedule.html           # 日程列表页
├── DATA_COLLECTION.md      # 本文件
```

## 待开发场馆

- 南山区青少年活动中心（滨海部）- 通过公众号获取
- 何香凝美术馆
- 南山文体中心
- 深圳湾体育中心（春茧）