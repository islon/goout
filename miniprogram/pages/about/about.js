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
      url: 'webcal://islon.github.io/goout/output/exhibitions_' + c.key + '.ics'
    };
  });

  return { cityList: cityList, links: links };
}

Page({
  data: {
    cities: [],
    subscribeLinks: []
  },

  onLoad() {
    this.refreshFromGlobal();
  },

  // 从 globalData 取数填充；若数据尚未就绪，注册更新回调等首次拉取后再刷新
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
      self.setData({ cities: r.cityList, subscribeLinks: r.links });
    };

    render();

    const exhibitions = (app.globalData && app.globalData.exhibitions) || [];
    const venues = (app.globalData && app.globalData.venues) || [];
    if ((!exhibitions.length || !venues.length) && app.onDataUpdated) {
      app.onDataUpdated(render);
    }
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

  onGoFeedback() {
    wx.navigateTo({
      url: '/pages/feedback/feedback'
    });
  },

  onShareAppMessage() {
    return {
      title: '童行 - 全国亲子活动日历',
      path: '/pages/index/index'
    };
  }
});
