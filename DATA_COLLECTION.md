# 数据收集文档

## 项目概述

本项目收集深圳主要场馆的展览活动信息，为市民提供一站式活动查询服务。

## 数据来源

### 场馆列表

| 场馆名称 | 数据源标识 | 官方网站 |
|---------|-----------|---------|
| 深圳会展中心 | szcec | http://www.szcec.com |
| 深圳国际会展中心 | shenzhen_world | http://www.shenzhen-world.com |
| 深圳图书馆 | szlib | http://www.szlib.org.cn |
| 宝安图书馆 | balib | http://www.balib.cn |
| 湾区之眼 | bayarea_eye | http://www.bayareaeye.com |
| 宝安科技馆 | baoan_kjg | http://www.baoankjg.com |
| 宝安体育中心 | baoan_ty | http://www.baoantiyuzhongxin.com |

### 数据采集方式

目前数据为模拟生成数据，未来可接入真实数据源：

1. **会展中心类**：通过官网展会日历、公众号推送、行业协会发布获取
2. **图书馆类**：通过官网活动预告、微信公众号、读者服务系统获取
3. **科技馆类**：通过官网活动公告、科普活动报名系统获取
4. **体育中心类**：通过赛事官网、票务平台、场馆公告获取
5. **艺术场馆类**：通过展览官网、艺术平台、场馆公告获取

## 数据字段说明

| 字段名 | 类型 | 说明 | 示例 |
|-------|------|------|------|
| name | string | 活动名称 | 深圳国际玩具展 |
| venue | string | 场馆名称 | 深圳会展中心 |
| start_date | string | 开始日期(YYYY-MM-DD) | 2026-07-08 |
| end_date | string | 结束日期(YYYY-MM-DD) | 2026-07-10 |
| url | string | 活动详情链接/场馆官网 | http://www.szcec.com |
| contact | string | 联系电话 | 0755-82848888 |
| description | string | 活动描述 | 包含时间、地点、活动介绍 |
| source | string | 数据源标识 | szcec |

## 数据刷新流程

### 方式一：运行数据生成脚本（推荐）

```bash
# 进入项目目录
cd /Users/longxiansheng/Documents/trae_projects/展览活动

# 运行数据生成脚本
python3 scripts/fix_data.py

# 提交更新到GitHub
git add output/exhibitions.json
git commit -m "fix(data): regenerate activity data"
git push origin main
```

### 方式二：手动更新

1. 编辑 `scripts/fix_data.py` 修改活动配置
2. 运行脚本生成新数据
3. 验证数据文件有效性
4. 提交并推送

## 数据统计

### 当前数据量（2026年）

| 场馆 | 活动总数 | 7月5日后活动数 |
|------|---------|---------------|
| 深圳图书馆 | 144 | 81 |
| 宝安图书馆 | 120 | 55 |
| 深圳会展中心 | 72 | 38 |
| 宝安科技馆 | 72 | 39 |
| 宝安体育中心 | 60 | 28 |
| 湾区之眼 | 60 | 33 |
| 深圳国际会展中心 | 48 | 21 |
| **总计** | **576** | **295** |

### 数据分布

- 展览类：深圳会展中心(72) + 深圳国际会展中心(48) = 120个
- 讲座/亲子类：深圳图书馆(144) + 宝安图书馆(120) = 264个
- 艺术类：湾区之眼(60)个
- 科技类：宝安科技馆(72)个
- 体育类：宝安体育中心(60)个

## 文件结构

```
展览活动/
├── output/
│   ├── exhibitions.json    # 主数据文件（JSON格式）
│   ├── exhibitions.ics     # 日历格式输出
│   └── exhibitions.rss     # RSS订阅格式
├── scripts/
│   ├── fix_data.py         # 数据生成脚本（主要）
│   ├── main.py             # 原始数据收集脚本
│   └── *.py                # 其他辅助脚本
├── index.html              # 首页
├── schedule.html           # 日程列表页
└── DATA_COLLECTION.md      # 本文件
```

## 未来优化方向

1. **接入真实数据**：开发爬虫脚本从各场馆官网实时抓取活动信息
2. **增量更新**：支持只更新新增或变更的活动，避免全量覆盖
3. **数据验证**：增加数据质量检查，确保字段完整性和格式正确性
4. **多源数据融合**：从多个渠道获取同一活动信息，交叉验证
5. **API接口**：提供数据API，方便其他应用调用