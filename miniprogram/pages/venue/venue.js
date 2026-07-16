// 童行小程序 - 场馆详情页
const { findVenue, formatDate } = require('../../utils/helpers.js');
const app = getApp();

const cityNames = {
  shenzhen: '深圳',
  guangzhou: '广州',
  shanghai: '上海',
  beijing: '北京',
  hangzhou: '杭州',
  chengdu: '成都',
  nanjing: '南京',
  wuhan: '武汉',
  xian: '西安',
  chongqing: '重庆'
};

Page({
  data: {
    venue: null,
    cityName: '',
    hasOfficialUrl: false,
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

    app.onReady(function() {
      self.loadVenue(rawId);
    });
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

    this.setData({
      venue: venue,
      cityName: cityNames[venue.city] || venue.city,
      hasOfficialUrl: !!(venue.official_url && venue.official_url.length > 0),
      hasHighlights: !!(venue.highlights && venue.highlights.length > 0),
      hasAddress: !!(venue.address && venue.address.length > 0),
      hasTransport: !!(venue.transport && venue.transport.length > 0),
      hasDescription: !!(venue.description && venue.description.length > 0),
      activities: activities.slice(0, 50),
      hasActivities: activities.length > 0
    });

    wx.setNavigationBarTitle({ title: venue.name || '场馆介绍' });
  },

  onCopyUrl() {
    if (!this.data.venue || !this.data.venue.official_url) return;
    wx.setClipboardData({
      data: this.data.venue.official_url,
      success: () => wx.showToast({ title: '官网链接已复制', icon: 'success' })
    });
  },

  onCopyAddress() {
    if (!this.data.venue || !this.data.venue.address) return;
    wx.setClipboardData({
      data: this.data.venue.address,
      success: () => wx.showToast({ title: '地址已复制', icon: 'success' })
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
