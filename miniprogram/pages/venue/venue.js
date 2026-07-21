// 童行小程序 - 场馆详情页
const { findVenue, formatDate } = require('../../utils/helpers.js');
// 打包内 cities 仅作离线兜底；运行期优先 app.getCities()（远程 cities.json），新增城市自动生效
const { cities: bundledCities } = require('../../data/filters.js');
const app = getApp();

// 提取链接数组（向后兼容 official_url 旧格式）
function getLinks(item) {
  if (item.links && Array.isArray(item.links) && item.links.length > 0) return item.links;
  if (item.official_url && item.official_url.trim()) return [{ url: item.official_url.trim(), label: '官方网站' }];
  return [];
}

// 运行时构建城市名映射：优先 app.getCities()，回退打包兜底
function buildCityNames() {
  const map = {};
  let list = bundledCities;
  try {
    if (app && typeof app.getCities === 'function') {
      const remote = app.getCities();
      if (Array.isArray(remote) && remote.length) list = remote;
    }
  } catch (e) {}
  (list || []).forEach(function(c) { map[c.key] = c.name; });
  return map;
}

Page({
  data: {
    venue: null,
    cityName: '',
    hasLinks: false,
    links: [],
    hasHighlights: false,
    hasAddress: false,
    hasTransport: false,
    hasDescription: false,
    activities: [],
    hasActivities: false
  },

  onLoad(options) {
    const self = this;
    const rawId = decodeURIComponent(options.id || '');
    if (!rawId) {
      wx.showToast({ title: '场馆不存在', icon: 'none' });
      setTimeout(() => wx.navigateBack(), 1500);
      return;
    }

    this._venueId = rawId;

    app.onReady(function() {
      self.loadVenue(rawId);
    });

    if (app && typeof app.onDataUpdated === 'function') {
      app.onDataUpdated(function() {
        self.loadVenue(rawId);
      });
    }
  },

  loadVenue(rawId) {
    const venueMap = app.globalData.venueMap || {};
    let venue = venueMap[rawId] || findVenue(rawId, venueMap);

    if (!venue) {
      wx.showToast({ title: '未找到场馆介绍', icon: 'none' });
      setTimeout(() => wx.navigateBack(), 1500);
      return;
    }

    // 查找该场馆的活动（支持模糊匹配）
    const exhibitions = app.globalData.exhibitions || [];
    const activities = [];
    for (let i = 0; i < exhibitions.length; i++) {
      const e = exhibitions[i];
      const matched = findVenue(e.venue, { [venue.name]: venue });
      if (matched) {
        const startDate = e.start_date;
        const endDate = e.end_date;
        const dateDisplay = startDate === endDate
          ? formatDate(startDate)
          : formatDate(startDate) + ' ~ ' + formatDate(endDate);
        activities.push(Object.assign({}, e, {
          dateDisplay: dateDisplay,
          cardId: e.id || (e.source + '-' + e.name + '-' + startDate)
        }));
      }
    }
    activities.sort((a, b) => (a.start_date || '').localeCompare(b.start_date || ''));

    const cityNames = buildCityNames();
    const links = getLinks(venue);
    this.setData({
      venue: venue,
      cityName: cityNames[venue.city] || venue.city,
      hasLinks: links.length > 0,
      links: links,
      hasHighlights: !!(venue.highlights && venue.highlights.length > 0),
      hasAddress: !!(venue.address && venue.address.length > 0),
      hasTransport: !!(venue.transport && venue.transport.length > 0),
      hasDescription: !!(venue.description && venue.description.length > 0),
      activities: activities.slice(0, 50),
      hasActivities: activities.length > 0
    });

    wx.setNavigationBarTitle({ title: venue.name || '场馆介绍' });
  },

  onCopyLink(e) {
    const url = e.currentTarget.dataset.url;
    if (!url) return;
    wx.setClipboardData({
      data: url,
      success: () => wx.showToast({ title: '链接已复制', icon: 'success' })
    });
  },

  // 通用复制：通过 data-text 传入要复制的文本，确保复制内容与显示一致
  onCopyText(e) {
    const text = e.currentTarget.dataset.text;
    if (!text) return;
    wx.setClipboardData({
      data: text,
      success: () => wx.showToast({ title: '已复制', icon: 'success' })
    });
  },

  onOpenMap() {
    const venue = this.data.venue;
    if (!venue) return;
    const lat = venue.latitude;
    const lng = venue.longitude;
    const searchText = venue.name + (venue.address ? (' ' + venue.address) : '');

    if (lat && lng) {
      wx.openLocation({
        latitude: Number(lat),
        longitude: Number(lng),
        name: venue.name || '',
        address: venue.address || '',
        scale: 16,
        fail: () => {
          this.showMapOptions(searchText, lat, lng);
        }
      });
    } else {
      this.showMapOptions(searchText);
    }
  },

  showMapOptions(searchText, lat, lng) {
    const items = [];
    if (lat && lng) {
      items.push({ text: '高德地图', url: 'amapuri://route/plan/?sourceApplication=童行&dlat=' + lat + '&dlon=' + lng + '&dname=' + encodeURIComponent(searchText) + '&dev=0&t=0' });
      items.push({ text: '百度地图', url: 'baidumap://map/direction?destination=name:' + encodeURIComponent(searchText) + '|latlng:' + lat + ',' + lng + '&mode=driving&src=童行' });
      items.push({ text: '腾讯地图', url: 'qqmap://map/routeplan?type=drive&to=' + encodeURIComponent(searchText) + '&tocoord=' + lat + ',' + lng + '&referer=童行' });
    }
    items.push({ text: '复制地址', url: null });

    wx.showActionSheet({
      itemList: items.map(item => item.text),
      success: (res) => {
        const selected = items[res.tapIndex];
        if (selected.url) {
          wx.setClipboardData({
            data: selected.url,
            success: () => {
              wx.showModal({
                title: '已复制链接',
                content: '请打开「' + selected.text + '」粘贴链接导航',
                showCancel: false,
                confirmText: '知道了',
                confirmColor: '#D4A373'
              });
            }
          });
        } else {
          wx.setClipboardData({
            data: searchText,
            success: () => {
              wx.showToast({ title: '已复制地址', icon: 'success' });
            }
          });
        }
      }
    });
  },

  onActivityTap(e) {
    const cardId = e.currentTarget.dataset.id;
    wx.navigateTo({
      url: '/pages/detail/detail?id=' + encodeURIComponent(cardId)
    });
  },

  onFeedbackTap() {
    const venue = this.data.venue;
    const venueName = venue ? venue.name : '';
    wx.navigateTo({
      url: '/pages/feedback/feedback?type=venue&target=' + encodeURIComponent(venueName)
    });
  },

  onShareAppMessage() {
    return {
      title: this.data.venue ? this.data.venue.name : '童行 - 场馆介绍',
      path: '/pages/venue/venue?id=' + encodeURIComponent(this.data.venue ? this.data.venue.name : '')
    };
  }
});
