// 重建小程序离线兜底数据 miniprogram/data/exhibitions.js
// 从真实数据(output/exhibitions.json)按城市取「未来即将举办」(start_date >= 今天)的前 N 条，
// 保证首屏即时渲染有真实活动（不再因打包样本日期过期而在 upcoming 筛选下全空）。
// 保留 booking_method 等真实字段；每条对象与线上数据同结构，离线详情页也能用报名入口。
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const SRC = path.join(ROOT, 'output', 'exhibitions.json');
const OUT = path.join(ROOT, 'miniprogram', 'data', 'exhibitions.js');

const PER_CITY = 40; // 每城保留条数（控制主包体积，<2MB）
const today = new Date().toISOString().split('T')[0];

function normalizeCity(city) {
  const map = {
    '深圳': 'shenzhen', '广州': 'guangzhou', '上海': 'shanghai', '北京': 'beijing',
    '杭州': 'hangzhou', '成都': 'chengdu', '南京': 'nanjing', '武汉': 'wuhan',
    '西安': 'xian', '重庆': 'chongqing'
  };
  return map[city] || city;
}

const all = JSON.parse(fs.readFileSync(SRC, 'utf8'));
const byCity = {};
for (const e of all) {
  const key = normalizeCity(e.city);
  (byCity[key] = byCity[key] || []).push(e);
}

const picked = [];
const report = {};
for (const key of Object.keys(byCity).sort()) {
  const arr = byCity[key];
  const upcoming = arr
    .filter((e) => e.start_date && e.start_date >= today)
    .sort((a, b) => a.start_date.localeCompare(b.start_date))
    .slice(0, PER_CITY);
  report[key] = { total: arr.length, upcoming: upcoming.length, picked: upcoming.length };
  picked.push(...upcoming);
}

// 写出：保留与线上同结构（含 booking_method）。用 JSON 直出，保持可读且可被 require。
const header = '// 自动生成（离线兜底：每城 ' + PER_CITY + ' 条未来即将举办真实活动，含 booking_method；首屏即时渲染用）\nmodule.exports = ';
fs.writeFileSync(OUT, header + JSON.stringify(picked) + ';\n');

const kb = (fs.statSync(OUT).size / 1024).toFixed(1);
console.log('已写入兜底:', picked.length, '条 | 文件', kb, 'KB');
console.log('各城(真实总数 / 未来数 / 选取):');
for (const k of Object.keys(report)) {
  const r = report[k];
  console.log('  ' + k + ': ' + r.total + ' / ' + r.upcoming + ' / ' + r.picked + (r.upcoming === 0 ? '  ⚠️ 该城未来无活动' : ''));
}
