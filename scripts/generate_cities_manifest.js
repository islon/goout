/**
 * generate_cities_manifest.js — 生成网页版共用的城市清单 output/cities.json
 *
 * 唯一事实来源：miniprogram/data/filters.js 的 cities 数组（小程序与网页共用同一顺序/中文名）。
 * 过滤出 output/ 下确实存在 exhibitions_{key}.json 的城市，输出 [{ key, name }]。
 * 网页 4 个页面改为运行时读取该清单动态渲染城市按钮/选项/tab，
 * 之后新增城市只需：(1) 在 filters.js 的 cities 加一行 (2) 提供数据文件，CI 自动重新生成本清单。
 *
 * 运行：node scripts/generate_cities_manifest.js
 * 依赖：仅 Node 内置模块（require filters.js 为纯数据模块）
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const { cities } = require(path.join(ROOT, 'miniprogram', 'data', 'filters.js'));
const OUTPUT_DIR = path.join(ROOT, 'output');

const present = new Set();
for (const c of cities) {
  if (fs.existsSync(path.join(OUTPUT_DIR, `exhibitions_${c.key}.json`))) {
    present.add(c.key);
  }
}

const list = cities
  .filter(c => present.has(c.key))
  .map(c => ({ key: c.key, name: c.name }));

const outPath = path.join(OUTPUT_DIR, 'cities.json');
fs.writeFileSync(outPath, JSON.stringify(list, null, 2) + '\n', 'utf-8');
console.log(`生成 ${outPath}：${list.length} 个城市 -> ${list.map(c => c.name).join(' ')}`);
