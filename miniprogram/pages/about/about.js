// 打包内 cities 仅作离线兜底；运行期优先 app.getCities()（远程 cities.json），新增城市自动出现在订阅列表
const { cities: bundledCities } = require('../../data/filters.js');

// 将 “2026/7/19 16:30:22” 这类 toLocaleString 结果精简为 “2026-07-19 16:30”
function shortTime(s) {
  if (!s) return '';
  const parts = String(s).split(' ');
  let date = parts[0] || '';
  let time = parts[1] || '';
  date = date.replace(/\//g, '-');
  if (time.length > 5) time = time.slice(0, 5);
  return date + (time ? ' ' + time : '');
}

// 从运行时全局数据动态统计各城市活动数 / 场馆数；cityDefs 为运行期城市清单
function buildCityLists(exhibitions, venues, cityDefs) {
  const actCount = {};
  (exhibitions || []).forEach(function(e) {
    const c = e.city;
    if (c) actCount[c] = (actCount[c] || 0) + 1;
  });
  const venCount = {};
  (venues || []).forEach(function(v) {
    const c = v.city;
    if (c) venCount[c] = (venCount[c] || 0) + 1;
  });

  const cities = (Array.isArray(cityDefs) && cityDefs.length) ? cityDefs : bundledCities;
  // 按人口/GDP 降序，人口多的城市排在前面（无 population 字段时保持原顺序）
  const sorted = cities.slice().sort(function(a, b) {
    return (b.population || 0) - (a.population || 0);
  });

  const cityList = sorted.map(function(c) {
    return {
      name: c.name,
      count: (actCount[c.key] || 0) + '条',
      venues: (venCount[c.key] || 0) + '个场馆',
      status: '已上线',
      color: '#166534'
    };
  });

  const links = sorted.map(function(c) {
    return {
      city: c.name,
      count: (actCount[c.key] || 0) + '条活动',
      venues: (venCount[c.key] || 0) + '个场馆',
      url: 'webcal://islon.github.io/goout/output/exhibitions_' + c.key + '.ics'
    };
  });

  return { cityList: cityList, links: links };
}

Page({
  data: {
    cities: [],
    subscribeLinks: [],
    appVersion: '',          // 小程序版本号（原始，如 2026.07.18.16）
    appVersionFormatted: '', // 版本号展示用（截取到日期，如 2026.07.18）
    lastUpdateTime: '',   // 数据最后刷新时间（原始）
    lastUpdateShort: '',  // 精简后的更新时间（如 2026-07-19 16:30）
    venuesCount: 0,       // 当前已加载场馆数
    venuesExpected: '',   // 预期场馆数（来自 data_meta，取不到时按 2964 兜底）
    venuesSynced: false,  // 已加载数是否已达预期（决定「已同步」标签）
    venuesSyncing: false  // 是否正在加载中（决定「同步中」标签，仅在真正下载时显示）
  },

  onLoad() {
    this.refreshFromGlobal();
  },

  onUnload() {
    const app = getApp();
    if (app && app.offLoadingChange && this._renderRef) {
      app.offLoadingChange(this._renderRef);
    }
  },

  // 从 globalData 取数填充；只要数据有更新（含分级加载 Tier1→Tier2→Tier3 各级到达）就重新统计，
  // 避免停留在首屏 80 条子集不再刷新。onDataUpdated 是一次性回调（每次 notify 即清空），
  // 故每次 render 后重新登记自身，确保后续每一级加载都能触达本页。
  refreshFromGlobal() {
    const app = getApp();
    const self = this;
    const getCityDefs = function() {
      try {
        if (typeof app.getCities === 'function') {
          const list = app.getCities();
          if (Array.isArray(list) && list.length) return list;
        }
      } catch (e) {}
      return bundledCities;
    };
    const render = function() {
      const ex = (app.globalData && app.globalData.exhibitions) || [];
      const ve = (app.globalData && app.globalData.venues) || [];
      const r = buildCityLists(ex, ve, getCityDefs());
      const rawVer = (app.globalData && app.globalData.appVersion) || '';
      const venuesCnt = ve.length;
      const venuesExp = ((app.globalData && app.globalData.dataMeta && app.globalData.dataMeta.venues) || 2964);
      const isLoading = !!(app.globalData && app.globalData.isLoading);
      const synced = venuesCnt >= venuesExp;
      const syncing = isLoading && !synced;
      self.setData({
        cities: r.cityList,
        subscribeLinks: r.links,
        appVersion: rawVer,
        appVersionFormatted: rawVer ? rawVer.split('.').slice(0, 3).join('.') : '',
        lastUpdateTime: (app.globalData && app.globalData.lastUpdateTime) || '',
        lastUpdateShort: shortTime((app.globalData && app.globalData.lastUpdateTime) || ''),
        venuesCount: venuesCnt,
        venuesExpected: venuesExp,
        venuesSynced: synced,
        // 仅在真正下载中且未达预期时显示「同步中」；加载结束后无论是否拉满都不再显示同步中
        venuesSyncing: syncing
      });
      // 重新登记，等下一级加载完成（notifyDataUpdated）再次刷新计数
      if (app.onDataUpdated) app.onDataUpdated(render);
    };

    render();

    // 云侧新增/减少城市时刷新订阅列表
    if (app.onCitiesUpdated) {
      app.onCitiesUpdated(render);
    }

    // 订阅加载状态变化：加载结束(isLoading=false)时重渲染，避免徽标卡在「同步中」
    if (app.onLoadingChange) {
      app.onLoadingChange(render);
      self._renderRef = render; // 记录引用，页面卸载时注销
    }
  },

  onCopyUrl(e) {
    const url = e.currentTarget.dataset.url;
    wx.setClipboardData({
      data: url,
      success: function() {
        wx.showToast({ title: '订阅链接已复制', icon: 'success' });
      }
    });
  },

  onCopyH5Url() {
    wx.setClipboardData({
      data: 'https://islon.github.io/goout/',
      success: function() {
        wx.showToast({ title: '网页链接已复制', icon: 'success' });
      }
    });
  },

  onCopyScheduleUrl() {
    wx.setClipboardData({
      data: 'https://islon.github.io/goout/schedule.html',
      success: function() {
        wx.showToast({ title: '日程链接已复制', icon: 'success' });
      }
    });
  },

  onCopyGitHub() {
    wx.setClipboardData({
      data: 'https://github.com/islon/goout/issues',
      success: function() {
        wx.showToast({ title: 'GitHub 链接已复制', icon: 'success' });
      }
    });
  },

  onShareAppMessage() {
    return {
      title: '童行 - 全国亲子活动日历',
      path: '/pages/index/index'
    };
  }
});
