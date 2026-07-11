# 场馆搜索与活动采集经验手册 (SOP)

> 本文档总结自 islon/goout 项目历次数据采集实践经验，供后续更新活动和寻找场馆时直接参考。
> 最后更新：2026-07-11 | 活动总数：678+ | 覆盖城市：5

---

## 一、场馆搜索方法论

### 1.1 三级数据源优先级

```
政府官网名录 > 场馆独立官网 > 国家公共文化云 > 商业公众号
```

| 优先级 | 渠道类型 | 可靠性 | 覆盖面 | 操作难度 |
|--------|---------|--------|--------|---------|
| 第一级 | 市文旅局/体育局官网场馆名录 | 最高 | 全市公办场馆 | 低（批量导出） |
| 第二级 | 场馆独立官网/公众号 | 高 | 单个场馆 | 中（逐个采集） |
| 第三级 | 国家公共文化云（culturedc.cn） | 较高 | 全国通用 | 中（跨城市检索） |
| 第四级 | 商业公众号/小红书/大众点评 | 一般 | 商业综合体 | 高（需单独抓取） |

### 1.2 各城市官方汇总渠道（已验证可用）

#### 深圳
- 深圳市文旅局公共场馆总名录：http://wtl.sz.gov.cn/ggfw/index.html
- 深圳政府在线场馆专题：https://www.sz.gov.cn/szzt2010/szwtt/wtcg/whcg/mindex.html
- 深圳文体旅智慧服务平台（i深圳小程序/公众号「深圳文旅」）

#### 广州
- 广州市文广旅局资料下载页：http://wglj.gz.gov.cn/zlxz/index.html
  - 可下载：文化馆一览表、图书馆网点、博物馆名录、免费开放场馆汇总表
- 广东省文旅厅湾区展讯：https://whly.gd.gov.cn/service_new/hdyg/
- 广州数字文化馆

#### 上海
- 上海市文旅局图书馆名录：https://whlyj.sh.gov.cn/tsg/
- 上海市文化馆名录：https://whlyj.sh.gov.cn/wenhuaguan/
- 上海市文旅局七月出行指南：https://whlyj.sh.gov.cn/wlyw/

#### 北京
- 北京数字文化馆：https://www.bjszwhg.org.cn/
- 北京市体育局公共体育场馆公开表：https://tyj.beijing.gov.cn/bjsports/xxcx/tjxx/543531165/index.html
- 北京公共数据开放平台（可下载Excel）：https://data.beijing.gov.cn/
- 京报网七月展讯汇总：https://xinwen.bjd.com.cn/

#### 杭州
- 浙里文化圈（小程序/公众号）— 全省公共文化活动统一预约平台
- 杭州市文旅局：https://wgl.hangzhou.gov.cn/

#### 全国通用
- 国家公共文化云：https://www.culturedc.cn/
  - 全国各省市区县图书馆、博物馆、文化馆、少年宫全覆盖
  - 支持按城市筛选，查看地址、开放时间、实时活动

### 1.3 场馆分类与采集策略

#### 政府统一收录（可批量导出，优先采集）
| 类型 | 举例 | 数据稳定性 |
|------|------|-----------|
| 图书馆 | 市级图书馆、区级图书馆、街道图书馆 | 名录稳定、地址准确 |
| 少儿图书馆 | 少年儿童图书馆 | 名录稳定 |
| 博物馆 | 市级博物馆、区级博物馆、行业博物馆 | 名录稳定 |
| 科技馆 | 科技馆、科学中心、科普馆 | 名录稳定 |
| 青少年宫 | 青少年宫、青少年活动中心 | 名录稳定 |
| 文化馆 | 文化馆、群众艺术馆 | 名录稳定 |
| 公共体育中心 | 体育中心、文体中心 | 名录稳定 |
| 规划馆 | 城市规划展览馆 | 名录稳定 |

#### 商业综合体（需单独建库，无法批量获取）
| 类型 | 举例 | 获取渠道 |
|------|------|---------|
| 商业滨水综合体 | 欢乐港湾（深圳）、前滩太古里（上海） | 商场官方公众号、小程序 |
| 商业文旅街区 | 永庆坊（广州） | 公众号活动页面 |
| 民营美术馆 | - | 各自官网/公众号 |

### 1.4 新城市开拓步骤

1. **第一步：抓政府名录** — 访问目标城市文旅局官网，导出公办场馆名录（名称、地址、官网）
2. **第二步：补特色场馆** — 搜索该城市的特色博物馆、美术馆、科技馆
3. **第三步：搜当前活动** — 用 `城市名 + 场馆名 + 2026年7月 + 活动/展览` 搜索
4. **第四步：交叉验证** — 用国家公共文化云核对场馆信息完整性
5. **第五步：录入数据** — 将场馆信息添加到 `venue_info.json`，活动信息添加到 `manual_data.json`

---

## 二、活动数据采集流程

### 2.1 活动信息搜索关键词模板

```
# 搜索当前活动
{场馆名} 2026年7月 展览
{场馆名} 2026年7月 活动
{场馆名} 暑期 亲子活动
{场馆名} {当前年月} 展览

# 搜索场馆本身
{城市名} 博物馆 一览表
{城市名} 图书馆 名录
{城市名} 文化馆 地址
{城市名} 公共文化场馆 名录
```

### 2.2 活动数据字段标准

```json
{
    "title": "活动名称",
    "venue": "场馆名称",
    "start_date": "2026-07-01",
    "end_date": "2026-07-31",
    "link": "来源链接（必须有）",
    "description": "活动描述（≥10字）",
    "category": "展览/演出/亲子活动/讲座/市集",
    "fee": "免费/免费需预约/收费/部分免费/需购票",
    "contact": "",
    "family_friendly": true,
    "source": "场馆官网名称或数据源标识"
}
```

### 2.3 fee 字段判断规则（已积累经验）

| 原始信息 | 标准化值 | 判断依据 |
|---------|---------|---------|
| 免费免预约 / 免费开放 | `免费` | 无需任何费用 |
| 免费需预约 / 免费但要预约 | `免费需预约` | 免费但需提前预约 |
| 早鸟票99元起 / 全票68元 / 门票30元 | `收费` | 有明确票价 |
| 购票入场 / 需购票 | `需购票` | 需购票但未标明价格 |
| 部分免费 / 部分活动免费 | `部分免费` | 部分免费部分收费 |
| 200元/期 / 按课程收费 | `收费` | 非标准格式统一归为收费 |
| 含在门票内 | 继承场馆门票的fee类型 | 需判断场馆门票是否免费 |

### 2.4 source 与 venue 区县匹配规则

source 字段应与 venue 所在区县一致。以深圳为例：

| 区县 | source 标识 | 关键词匹配 |
|------|------------|-----------|
| 南山区 | nswtzx | 南山、桃源街道 |
| 宝安区 | baoan_1990 | 宝安、燕罗、新桥 |
| 光明区 | gmwhg | 光明、公明、马田、玉塘 |
| 龙岗区 | lgwhg | 龙岗、龙城、坪地、坂田、吉华、南湾、平湖 |
| 龙华区 | lhwhg2 | 龙华 |
| 罗湖区 | lhwhg2 | 罗湖、园岭 |
| 福田区 | ftwhg | 福田、安托山、梦工场 |
| 盐田区 | ytwhg | 盐田 |
| 坪山区 | pswhg | 坪山 |
| 大鹏新区 | dpwhg | 大鹏 |

**多城市扩展时**：source 填写场馆官网名称或城市+场馆简称，如 `广东省博物馆`、`上海博物馆`。

### 2.5 日期解析规则（已积累经验）

| 原始格式 | start_date | end_date | 说明 |
|---------|-----------|----------|------|
| 2026年7月5日至7月30日 | 2026-07-05 | 2026-07-30 | 标准格式直接拆分 |
| 即日起至2026年7月 | 推断为当月1日 | 2026-07-31 | "即日起"需推断 |
| 2026.7.1-10.18 | 2026-07-01 | 2026-10-18 | 点号分隔 |
| 7月全月 | 2026-07-01 | 2026-07-31 | |
| 长期/常设 | 2026-07-01 | 2026-12-31 | 常设展默认半年 |
| 展出中 | 2026-07-01 | 2026-12-31 | 未标明结束日期默认半年 |

### 2.6 description 自动补全逻辑

当 description 为空或长度 < 10 字时，`normalize_activity()` 会自动补全：

```python
description = f"{title}。{venue}举办。"
if fee and fee != '免费':
    description += f"{fee}。"
```

但建议手动填写更详细的描述，包含活动亮点、适合人群等。

---

## 三、数据管线运行指南

### 3.1 运行命令

```bash
cd /workspace/goout/scripts
python3 data_pipeline.py
```

### 3.2 数据管线处理流程

```
manual_data.json ──┐
各 scraper_*.py ────┤── data_pipeline.py ── normalize_activity() ── exhibitions.json
                    │                        ├── ics_generator.py ── exhibitions.ics
                    │                        └── rss_generator.py ── exhibitions.rss
```

### 3.3 数据质量检查

```bash
python3 check_data_quality.py
```

检查项：
- fee 字段是否在标准列表内（免费/免费需预约/收费/部分免费/需购票）
- source 与 venue 区县是否匹配
- description 长度是否 ≥ 10 字

### 3.4 常见错误及解决方案

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| `SSLError: [SSL: BAD_ECPOINT] bad ecpoint` | gov.cn 网站SSL证书问题 | data_pipeline.py 已全局禁用SSL验证，忽略即可 |
| `ModuleNotFoundError: No module named 'bs4'` | 缺少依赖 | `pip install bs4 lxml` |
| `ModuleNotFoundError: No module named 'requests'` | 缺少依赖 | `pip install requests` |
| `Author identity unknown` | git 未配置用户信息 | `git config user.email "islon@users.noreply.github.com" && git config user.name "islon"` |
| GitHub API 返回 `Bad credentials` | token 过期 | 需更新 GitHub token |
| 中间文件 description 太短 | scraper 输出未经标准化 | 不影响最终数据，normalize_activity 会自动补全 |

### 3.5 数据更新完整流程

```bash
# 1. 拉取最新代码
cd /workspace/goout && git pull origin main

# 2. 添加新活动到 manual_data.json（编辑文件）

# 3. 运行数据管线
cd scripts && python3 data_pipeline.py

# 4. 检查数据质量
python3 check_data_quality.py

# 5. 提交并推送
cd /workspace/goout
git add -A
git commit -m "feat: 添加XX城市XX活动"
git push origin main
```

---

## 四、多城市场馆清单（已收录）

### 4.1 深圳（已实现自动爬虫 + 手动数据）

**已覆盖场馆类型**：图书馆、少儿图书馆、博物馆、科技馆、文化馆、青少年宫、体育中心、美术馆、湿地公园、地质公园等

**数据源**：38个 scraper 脚本 + manual_data.json（411+条手动数据）

### 4.2 广州（已收录场馆名录 + 7月活动）

| 类型 | 核心场馆 | 官网 |
|------|---------|------|
| 博物馆 | 广东省博物馆、南越王博物院、广州博物馆 | gdmuseum.com / gznywmuseum.org / guangzhoumuseum.cn |
| 科技馆 | 广东科学中心、广东科学馆 | gdsc.cn |
| 图书馆 | 广东省立中山图书馆、广州图书馆、广州少年儿童图书馆 | zslib.com.cn / gzlib.org.cn / gzst.org.cn |
| 文化馆 | 广州市文化馆新馆 | gz-arts.com |
| 美术馆 | 广东美术馆（白鹅潭新馆）、广州艺术博物院 | gdmoa.org / gzam.org.cn |
| 会展 | 广交会展馆 | - |

### 4.3 上海（已收录场馆名录 + 7月活动）

| 类型 | 核心场馆 | 官网 |
|------|---------|------|
| 博物馆 | 上海博物馆、上海世博会博物馆 | shanghaimuseum.net / wsma.org.cn |
| 科技馆 | 上海科技馆、上海天文馆、上海自然博物馆 | sstm.org.cn / sstm-sam.org.cn / snhm.org.cn |
| 图书馆 | 上海图书馆、上海少年儿童图书馆 | library.sh.cn / sstlib.cn |
| 美术馆 | 中华艺术宫、上海当代艺术博物馆 | artmuseumonline.cn / powerstationofart.com |
| 文化馆 | 上海市群众艺术馆 | shqyg.com |
| 会展 | 上海世博展览馆、上海展览中心 | - |

### 4.4 北京（已收录场馆名录 + 7月活动）

| 类型 | 核心场馆 | 官网 |
|------|---------|------|
| 博物馆 | 中国国家博物馆、故宫博物院、首都博物馆 | chnmuseum.cn / dpm.org.cn / capitalmuseum.org.cn |
| 科技馆 | 中国科学技术馆、北京科学中心 | cstm.org.cn / bjsc.net.cn |
| 自然 | 北京自然博物馆（国家自然博物馆） | bmnh.org.cn / nnhm.org.cn |
| 天文 | 北京天文馆 | bjp.org.cn |
| 美术馆 | 中国美术馆 | namoc.org |
| 图书馆 | 国家图书馆、首都图书馆 | nlc.cn / clcn.net.cn |

### 4.5 杭州（已收录场馆名录 + 7月活动）

| 类型 | 核心场馆 | 官网 |
|------|---------|------|
| 博物馆 | 浙江省博物馆、杭州博物馆、良渚博物院 | zhejiangmuseum.com / hzmuseum.cn / lzmuseum.cn |
| 科技馆 | 浙江省科技馆 | zjstm.org |
| 自然 | 浙江自然博物院（杭州馆/安吉馆） | zmnh.com |
| 图书馆 | 杭州图书馆 | zjhzlib.cn |
| 专题博物馆 | 中国丝绸博物馆、中国茶叶博物馆 | chinasilkmuseum.com / teamuseum.cn |
| 工艺美术 | 杭州工艺美术博物馆群 | hzacm.cn |
| 青少年活动 | 杭州市青少年活动中心 | hzqsn.com |

---

## 五、活动采集实操技巧

### 5.1 高效搜索策略

1. **先搜官方汇总页** — 用 `城市名 + 文旅局 + 场馆名录` 找到政府汇总页
2. **再搜媒体汇总** — 用 `城市名 + 2026年7月 + 展览/活动推荐` 搜媒体报道
3. **最后搜单场馆** — 用 `场馆名 + 官网/公众号 + 7月活动` 搜具体场馆

### 5.2 搜索结果优先级

- **官方来源**（文旅局官网、政府门户）> 权威媒体（新华网、人民网、南方+）> 本地媒体（本地宝、搜狐号）> 商业平台（大众点评、小红书）

### 5.3 暑期活动特征（6-8月）

每年暑期是活动高峰期，需重点关注：

| 特征 | 说明 |
|------|------|
| 延时开放 | 多数场馆延时至20:00-21:00 |
| 夜间活动 | 博物馆奇妙夜、夜宿活动、夜读集市 |
| 亲子专场 | 科学实验秀、研学营、夏令营、绘本故事会 |
| 免费活动密集 | 图书馆/文化馆几乎全部免费 |
| 预约紧张 | 热门场馆需提前7天抢票 |

### 5.4 活动信息核实清单

每条活动信息录入前需核实：

- [ ] 活动名称完整准确
- [ ] 时间范围明确（开始日期 + 结束日期）
- [ ] 费用类型符合标准（免费/免费需预约/收费/部分免费/需购票）
- [ ] 来源链接可访问
- [ ] description ≥ 10 字
- [ ] source 与 venue 所在城市/区县一致
- [ ] family_friendly 已标注
- [ ] category 已分类（展览/演出/亲子活动/讲座/市集）

---

## 六、定时任务执行经验

### 6.1 每日23:00定时任务执行流程

```
1. 拉取最新代码 (git pull)
2. 检查 GitHub Open Issues
3. 运行数据管线 (data_pipeline.py)
4. 数据质量校验 (check_data_quality.py)
5. 处理新活动发现 Issues → 核实 → 添加到 manual_data.json
6. 修复数据质量 Issues
7. 重新运行数据管线
8. 提交并推送代码
9. 关闭已修复的 Issues（附说明评论）
10. 经验总结写入 experience_log.json
```

### 6.2 GitHub Issue 处理规则

| Issue 类型 | 处理方式 |
|-----------|---------|
| 新活动发现（格式：活动名/场馆/区/时间/地址/类型/描述/来源） | 核实后添加到 manual_data.json，关闭 Issue |
| 数据质量巡检报告 | 逐条检查 fee/区县匹配/description，修复后关闭 |
| 用户反馈/建议 | 评估可行性，能改的改，不确定的保留 open |

### 6.3 经验积累机制

每次执行后将以下信息记录到 `experience_log.json`：
- 执行日期
- 活动总数
| - 关闭/剩余 Issues 数
- 新增活动数
| - 修复的数据质量问题数
- lessons_learned（经验教训）
- improvement_ideas（改进建议）

**下次执行前先读取此文件**，参考历史经验避免重复踩坑。

---

## 七、已验证可用的数据源汇总

### 7.1 深圳（38个爬虫已覆盖）

| 数据源 | 爬虫脚本 | 数据量级 |
|--------|---------|---------|
| 深圳图书馆 | scraper_szlib.py | 大 |
| 深圳国际会展中心 | scraper_shenzhen_world.py | 大 |
| 深圳文化馆云平台 | scraper_szwty.py | 大 |
| 南山图书馆 | scraper_nslib.py | 中 |
| 南山博物馆 | scraper_nsmuseum.py | 中 |
| 南山少儿图书馆 | scraper_nsqsng.py | 中 |
| 南山文体中心 | scraper_nswtzx.py | 中 |
| 宝安1990文化馆 | scraper_baoan_1990.py | 中 |
| 光明区图书馆 | scraper_gm_lib.py | 中 |
| 龙岗客家民俗博物馆 | scraper_lg_hakka.py | 中 |
| 其他30+场馆 | 各 scraper_*.py | 小 |

### 7.2 手动数据源

| 文件 | 内容 | 条数 |
|------|------|------|
| manual_data.json | 手动添加的活动数据 | 411+ |
| venue_info.json | 场馆基础信息 | 100+ |
| experience_log.json | 执行经验记录 | 3+ |

---

## 八、改进方向与TODO

### 短期（下次执行可做）
- [ ] 为广州、上海、北京、杭州场馆编写 scraper 脚本
- [ ] 增加 fee 字段自动标准化逻辑到 normalize_activity()
- [ ] 增加活动过期自动清理机制
- [ ] 增加数据去重逻辑

### 中期
- [ ] 接入国家公共文化云 API 批量获取活动
- [ ] 对接各城市文旅局开放数据平台
- [ ] 增加微信公众号/小程序活动抓取
- [ ] 增加小红书活动信息抓取

### 长期
- [ ] 建设全城市场馆数据库（自动同步政府名录）
- [ ] 活动推荐算法（基于用户偏好和位置）
- [ ] 活动订阅和推送通知
- [ ] 多语言支持

---

## 九、关键文件索引

| 文件 | 用途 | 路径 |
|------|------|------|
| 数据管线主脚本 | 整合所有数据源生成最终数据 | [scripts/data_pipeline.py](file:///workspace/goout/scripts/data_pipeline.py) |
| 手动活动数据 | 手动添加的活动条目 | [scripts/manual_data.json](file:///workspace/goout/scripts/manual_data.json) |
| 场馆信息 | 场馆基础信息库 | [scripts/venue_info.json](file:///workspace/goout/scripts/venue_info.json) |
| 经验记录 | 每次执行的经验总结 | [scripts/experience_log.json](file:///workspace/goout/scripts/experience_log.json) |
| 数据质量检查 | 校验 fee/区县/description | [scripts/check_data_quality.py](file:///workspace/goout/scripts/check_data_quality.py) |
| 数据采集文档 | 场馆名录+采集指南 | [DATA_COLLECTION.md](file:///workspace/goout/DATA_COLLECTION.md) |
| 最终输出 | 生成的展览数据 | [output/exhibitions.json](file:///workspace/goout/output/exhibitions.json) |
| ICS日历 | 日历格式输出 | [output/exhibitions.ics](file:///workspace/goout/output/exhibitions.ics) |
| RSS订阅 | RSS格式输出 | [output/exhibitions.rss](file:///workspace/goout/output/exhibitions.rss) |

---

> **使用建议**：每次执行定时任务前，先通读本文档的"二、活动数据采集流程"和"六、定时任务执行经验"两个章节；每次添加新城市时，参考"一、场馆搜索方法论"和"四、多城市场馆清单"。
