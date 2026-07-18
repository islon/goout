// 打包内 cities 仅作离线兜底；运行期优先 app.getCities()（远程 cities.json），新增城市自动出现在订阅列表
const { cities: bundledCities } = require('../../data/filters.js');

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

  const cityList = cities.map(function(c) {
    return {
      name: c.name,
      count: (actCount[c.key] || 0) + '条',
      venues: (venCount[c.key] || 0) + '个场馆',
      status: '已上线',
      color: '#166534'
    };
  });

  const links = cities.map(function(c) {
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
    appVersion: '',       // 小程序版本号
    buildDate: '',        // 构建/发布日期
    lastUpdateTime: '',   // 数据最后刷新时间（让用户了解数据实效性）
    venuesCount: 0,       // 当前已加载场馆数
    venuesExpected: ''    // 预期场馆数（来自 data_meta，取不到时按 2964 兜底）
  },

  onLoad() {
    this.refreshFromGlobal();
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
      self.setData({
        cities: r.cityList,
        subscribeLinks: r.links,
        appVersion: (app.globalData && app.globalData.appVersion) || '',
        buildDate: (app.globalData && app.globalData.buildDate) || '',
        lastUpdateTime: (app.globalData && app.globalData.lastUpdateTime) || '',
        venuesCount: ve.length,
        venuesExpected: ((app.globalData && app.globalData.dataMeta && app.globalData.dataMeta.venues) || 2964)
      });
      // 重新登记，等下一级加载完成（notifyDataUpdated）再次刷新计数
      if (app.onDataUpdated) app.onDataUpdated(render);
    };

    render();

    // 云侧新增/减少城市时刷新订阅列表
    if (app.onCitiesUpdated) {
      app.onCitiesUpdated(render);
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
