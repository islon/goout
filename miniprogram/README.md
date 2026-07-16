# 童行小程序 (WeChat Mini Program)

基于 [童行 - 全国亲子活动日历](https://islon.github.io/goout/) 的微信小程序版本。

## 快速开始

1. 打开微信开发者工具
2. 选择「导入项目」
3. 项目目录选择本文件夹 `goout-miniprogram`
4. AppID 可选择「测试号」或填入自己的 AppID
5. 点击确定即可预览

## 项目结构

```
goout-miniprogram/
├── app.js                # 小程序入口
├── app.json              # 全局配置（页面路由、tabBar、窗口样式）
├── app.wxss             # 全局样式
├── project.config.json  # 微信开发者工具项目配置
├── sitemap.json         # 小程序索引配置
├── assets/              # tabBar 图标
├── data/
│   ├── exhibitions.js   # 活动数据（488条，四城）
│   └── filters.js       # 筛选器配置（场馆映射、区县映射等）
├── utils/
│   └── helpers.js       # 工具函数（筛选、格式化、类型判断）
└── pages/
    ├── index/           # 活动列表页（主页）
    ├── detail/          # 活动详情页
    └── about/           # 关于/订阅页
```

## 功能

- 四城活动浏览：深圳、广州、上海、北京
- 多维筛选：城市、时间、类型、区县、地点、费用、亲子友好
- 搜索功能：按名称、地点、描述搜索
- 智能筛选：无结果的筛选选项自动置灰
- 活动详情：展示完整信息和原始链接
- 日历订阅：复制 ICS 订阅链接到手机日历

## 数据来源

所有数据来自原项目 https://islon.github.io/goout/ 的 GitHub Pages 静态数据，共 488 条活动。
