// 童行小程序 - 工具函数
const { districtMapping, sourceToVenue, sourceChineseToDistrict, districtKeywords, districtsByCity } = require('../data/filters.js');

function normalizeCity(city) {
  if (!city) return 'shenzhen';
  const c = city.toLowerCase().trim();
  if (c === '深圳' || c === 'sz' || c === 'shenzhen') return 'shenzhen';
  if (c === '广州' || c === 'gz' || c === 'guangzhou') return 'guangzhou';
  if (c === '上海' || c === 'sh' || c === 'shanghai') return 'shanghai';
  if (c === '北京' || c === 'bj' || c === 'beijing') return 'beijing';
  if (c === '杭州' || c === 'hz' || c === 'hangzhou') return 'hangzhou';
  return c;
}

function getDistrict(input) {
  // input 可为活动对象或老的 source 字符串，统一处理
  var source = null, venue = null, dataDistrict = null;
  if (input && typeof input === 'object') {
    dataDistrict = input.district;
    source = input.source;
    venue = input.venue;
  } else {
    source = input;
  }
  // 1) 优先使用数据层已算好的 district 字段（exhibitions.json / exhibitions.js 均已含 district）
  if (dataDistrict && dataDistrict !== '其他') return dataDistrict;
  // 2) 回退：原映射（兼容老数据 / 客户端兜底）
  if (source && districtMapping[source]) return districtMapping[source];
  if (source && sourceChineseToDistrict && sourceChineseToDistrict[source]) return sourceChineseToDistrict[source];
  if (venue && sourceChineseToDistrict && sourceChineseToDistrict[venue]) return sourceChineseToDistrict[venue];
  // 3) 关键字兜底：源名/场馆名里含区县关键字直接归该区
  if (districtKeywords) {
    var text = [source, venue].filter(Boolean).join(' ');
    for (var i = 0; i < districtKeywords.length; i++) {
      if (text.indexOf(districtKeywords[i][0]) >= 0) {
        return districtKeywords[i][1];
      }
    }
  }
  return '其他';
}

// 返回某城市当前数据中"实际有活动"的区县列表（'全部区县' 始终在前）
// 这样区县筛选里不会出现一堆 0 活动的空区县
function getPresentDistricts(city, exhibitions) {
  const all = districtsByCity[city] || [];
  const found = {};
  (exhibitions || []).forEach(function(e) {
    if (normalizeCity(e.city) !== city) return;
    const d = getDistrict(e);
    if (d && d !== '其他') found[d] = true;
  });
  return all.filter(function(d) { return d === '全部区县' || found[d]; });
}

function matchSource(exhibition, sourceKey) {
  if (exhibition.source === sourceKey) return true;
  const venueName = sourceToVenue[sourceKey];
  if (venueName && exhibition.venue && exhibition.venue.indexOf(venueName) >= 0) return true;
  return false;
}

function getFeeType(exhibition) {
  const name = exhibition.name || '';
  const desc = exhibition.description || '';
  const venue = exhibition.venue || '';

  const freeKeywords = ['免费', '公益', '免门票', '免费开放', '免费参与'];
  const paidKeywords = ['收费', '门票', '购票', '票价', '预售', '报名费用', '￥', '元'];

  for (let i = 0; i < freeKeywords.length; i++) {
    if (name.indexOf(freeKeywords[i]) >= 0 || desc.indexOf(freeKeywords[i]) >= 0) return 'free';
  }
  for (let i = 0; i < paidKeywords.length; i++) {
    if (name.indexOf(paidKeywords[i]) >= 0 || desc.indexOf(paidKeywords[i]) >= 0) return 'paid';
  }

  const freeVenues = ['图书馆', '宝安科技馆', '湾区之眼'];
  for (let i = 0; i < freeVenues.length; i++) {
    if (venue.indexOf(freeVenues[i]) >= 0) return 'free';
  }
  const paidVenues = ['会展中心', '体育馆', '体育场', '体育中心'];
  for (let i = 0; i < paidVenues.length; i++) {
    if (venue.indexOf(paidVenues[i]) >= 0) return 'paid';
  }
  return 'unknown';
}

function getActivityType(exhibition) {
  if (exhibition.category) return exhibition.category;
  const name = exhibition.name || '';
  const venue = exhibition.venue || '';

  if (venue.indexOf('体育') >= 0 || name.indexOf('比赛') >= 0 || name.indexOf('健身') >= 0 ||
    name.indexOf('运动') >= 0 || name.indexOf('足球') >= 0 || name.indexOf('篮球') >= 0 ||
    name.indexOf('羽毛球') >= 0 || name.indexOf('乒乓球') >= 0 || name.indexOf('网球') >= 0 ||
    name.indexOf('游泳') >= 0 || name.indexOf('田径') >= 0 || name.indexOf('马拉松') >= 0 ||
    name.indexOf('瑜伽') >= 0 || name.indexOf('舞蹈') >= 0 || name.indexOf('武术') >= 0) {
    return '体育赛事';
  }

  if (venue.indexOf('科技馆') >= 0 || name.indexOf('科学') >= 0 || name.indexOf('科普') >= 0 ||
    name.indexOf('科技') >= 0 || name.indexOf('机器人') >= 0 || name.indexOf('编程') >= 0 ||
    name.indexOf('3D打印') >= 0 || name.indexOf('VR') >= 0 || name.indexOf('创客') >= 0) {
    return '科普活动';
  }

  if (venue.indexOf('湾区之眼') >= 0 || name.indexOf('艺术') >= 0 || name.indexOf('展览') >= 0 ||
    name.indexOf('画展') >= 0 || name.indexOf('摄影') >= 0 || name.indexOf('雕塑') >= 0) {
    return '展览';
  }

  if (venue.indexOf('图书馆') >= 0 || name.indexOf('讲座') >= 0 || name.indexOf('故事会') >= 0 ||
    name.indexOf('阅读') >= 0 || name.indexOf('沙龙') >= 0 || name.indexOf('分享') >= 0) {
    return '讲座阅读';
  }

  if (name.indexOf('亲子') >= 0 || name.indexOf('儿童') >= 0 || name.indexOf('手工') >= 0 ||
    name.indexOf('夏令营') >= 0 || name.indexOf('嘉年华') >= 0) {
    return '亲子活动';
  }

  if (name.indexOf('音乐会') >= 0 || name.indexOf('演唱会') >= 0 || name.indexOf('话剧') >= 0 ||
    name.indexOf('歌剧') >= 0 || name.indexOf('演出') >= 0 || name.indexOf('演奏') >= 0) {
    return '演出';
  }

  if (name.indexOf('电影') >= 0 || name.indexOf('放映') >= 0 || name.indexOf('观影') >= 0) {
    return '影视放映';
  }

  if (name.indexOf('展览') >= 0 || name.indexOf('展') >= 0) return '展览';

  return '展览';
}

function formatDate(dateStr) {
  const date = new Date(dateStr);
  const month = date.getMonth() + 1;
  const day = date.getDate();
  const weekDays = ['周日', '周一', '周二', '周三', '周四', '周五', '周六'];
  const weekDay = weekDays[date.getDay()];
  return month + '月' + day + '日 ' + weekDay;
}

function getDuration(startDate, endDate) {
  if (startDate === endDate) return '1天';
  const start = new Date(startDate);
  const end = new Date(endDate);
  const days = Math.floor((end - start) / (1000 * 60 * 60 * 24)) + 1;
  return days + '天';
}

function getDateBadge(startDate) {
  const now = new Date();
  const today = now.toISOString().split('T')[0];
  const tomorrow = new Date(now);
  tomorrow.setDate(now.getDate() + 1);
  const tomorrowStr = tomorrow.toISOString().split('T')[0];

  if (startDate === today) return 'today';
  if (startDate === tomorrowStr) return 'tomorrow';

  const diffDays = Math.floor((new Date(startDate) - now) / (1000 * 60 * 60 * 24));
  if (diffDays >= 0 && diffDays <= 7) return 'upcoming';

  return '';
}

function getFilteredExhibitions(allExhibitions, filters) {
  const now = new Date();
  const currentYear = now.getFullYear();
  const currentMonth = now.getMonth();
  const today = now.toISOString().split('T')[0];

  let filtered = allExhibitions.filter(function(e) {
    return normalizeCity(e.city) === filters.city;
  });

  if (filters.search) {
    var query = filters.search.toLowerCase();
    filtered = filtered.filter(function(e) {
      return (e.name || '').toLowerCase().indexOf(query) >= 0 ||
        (e.venue || '').toLowerCase().indexOf(query) >= 0 ||
        (e.description || '').toLowerCase().indexOf(query) >= 0;
    });
  }

  if (filters.district !== 'all') {
    filtered = filtered.filter(function(e) { return getDistrict(e) === filters.district; });
  }

  if (filters.source !== 'all') {
    filtered = filtered.filter(function(e) { return matchSource(e, filters.source); });
  }

  if (filters.fee !== 'all') {
    filtered = filtered.filter(function(e) { return getFeeType(e) === filters.fee; });
  }

  if (filters.type !== 'all') {
    filtered = filtered.filter(function(e) { return getActivityType(e) === filters.type; });
  }

  if (filters.family === 'family') {
    filtered = filtered.filter(function(e) { return e.family_friendly === true; });
  } else if (filters.family === 'other') {
    filtered = filtered.filter(function(e) { return e.family_friendly !== true; });
  }

  switch (filters.time) {
    case 'today':
      return filtered.filter(function(e) {
        return e.start_date === today || (e.start_date <= today && e.end_date >= today);
      });
    case 'tomorrow':
      var tomorrow2 = new Date(now);
      tomorrow2.setDate(now.getDate() + 1);
      var tomorrowStr2 = tomorrow2.toISOString().split('T')[0];
      return filtered.filter(function(e) {
        return e.start_date === tomorrowStr2 || (e.start_date <= tomorrowStr2 && e.end_date >= tomorrowStr2);
      });
    case 'week':
      var weekLater = new Date(now);
      weekLater.setDate(now.getDate() + 7);
      var weekLaterStr = weekLater.toISOString().split('T')[0];
      return filtered.filter(function(e) { return e.start_date <= weekLaterStr && e.end_date >= today; });
    case 'upcoming':
      return filtered.filter(function(e) { return e.start_date >= today; });
    case 'month':
      return filtered.filter(function(e) {
        var date = new Date(e.start_date);
        return date.getFullYear() === currentYear && date.getMonth() === currentMonth;
      });
    case 'next_month':
      var nextMonth = currentMonth + 1;
      var nextYear = currentYear;
      if (nextMonth > 11) { nextMonth = 0; nextYear++; }
      return filtered.filter(function(e) {
        var date = new Date(e.start_date);
        return date.getFullYear() === nextYear && date.getMonth() === nextMonth;
      });
    case 'all':
    default:
      return filtered;
  }
}

// 构建展示用的活动列表（添加 feeType, activityType, dateBadge 等）
function buildDisplayItems(exhibitions) {
  return exhibitions.map(function(e, idx) {
    var feeType = getFeeType(e);
    var activityType = getActivityType(e);
    var dateBadge = getDateBadge(e.start_date);
    var startDate = e.start_date;
    var endDate = e.end_date;
    var dateDisplay = startDate === endDate
      ? formatDate(startDate)
      : startDate.substring(5) + ' ~ ' + endDate.substring(5);
    var duration = getDuration(startDate, endDate);
    var monthLabel = startDate.substring(0, 4) + '年' + parseInt(startDate.substring(5, 7)) + '月';
    var cardId = e.id || (e.source + '-' + e.name + '-' + startDate);

    return Object.assign({}, e, {
      feeType: feeType,
      activityType: activityType,
      dateBadge: dateBadge,
      dateDisplay: dateDisplay,
      duration: duration,
      district: getDistrict(e),
      monthLabel: monthLabel,
      cardId: cardId
    });
  });
}

function buildVenueMap(venues) {
  const map = {};
  for (let i = 0; i < venues.length; i++) {
    const v = venues[i];
    if (v && v.name) {
      map[v.name] = v;
    }
  }
  return map;
}

function findVenue(venueName, venueMap) {
  if (!venueName || !venueMap) return null;
  const name = String(venueName).trim();
  if (!name) return null;
  if (venueMap[name]) return venueMap[name];

  // 模糊匹配：活动 venue 可能是"深圳博物馆（市民中心馆）"，场馆库只有"深圳博物馆"
  let bestMatch = null;
  let bestScore = 0;
  for (const key in venueMap) {
    const v = venueMap[key];
    const vn = v.name;
    if (name.indexOf(vn) >= 0 || vn.indexOf(name) >= 0) {
      const score = vn.length;
      if (score > bestScore) {
        bestScore = score;
        bestMatch = v;
      }
    }
  }
  return bestMatch;
}

function buildVenueActivityCounts(venues, exhibitions) {
  const venueMap = buildVenueMap(venues);
  const counts = {};
  for (let i = 0; i < exhibitions.length; i++) {
    const e = exhibitions[i];
    const venue = findVenue(e.venue, venueMap);
    if (venue && venue.name) {
      counts[venue.name] = (counts[venue.name] || 0) + 1;
    }
  }
  return counts;
}

module.exports = {
  normalizeCity,
  getDistrict,
  getPresentDistricts,
  matchSource,
  getFeeType,
  getActivityType,
  formatDate,
  getDuration,
  getDateBadge,
  getFilteredExhibitions,
  buildDisplayItems,
  buildVenueMap,
  findVenue,
  buildVenueActivityCounts
};
