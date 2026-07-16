Page({
  data: {
    cities: [
      { name: '深圳', count: '741条', venues: '138个场馆', status: '已上线', color: '#166534' },
      { name: '杭州', count: '306条', venues: '135个场馆', status: '已上线', color: '#166534' },
      { name: '广州', count: '304条', venues: '104个场馆', status: '已上线', color: '#166534' },
      { name: '北京', count: '301条', venues: '116个场馆', status: '已上线', color: '#166534' },
      { name: '上海', count: '301条', venues: '103个场馆', status: '已上线', color: '#166534' },
      { name: '成都', count: '300条', venues: '120个场馆', status: '已上线', color: '#166534' },
      { name: '重庆', count: '300条', venues: '105个场馆', status: '已上线', color: '#166534' },
      { name: '南京', count: '300条', venues: '106个场馆', status: '已上线', color: '#166534' },
      { name: '西安', count: '300条', venues: '109个场馆', status: '已上线', color: '#166534' },
      { name: '武汉', count: '300条', venues: '103个场馆', status: '已上线', color: '#166534' }
    ],
    subscribeLinks: [
      { city: '深圳', count: '741条活动', url: 'webcal://islon.github.io/goout/output/exhibitions_shenzhen.ics' },
      { city: '杭州', count: '306条活动', url: 'webcal://islon.github.io/goout/output/exhibitions_hangzhou.ics' },
      { city: '广州', count: '304条活动', url: 'webcal://islon.github.io/goout/output/exhibitions_guangzhou.ics' },
      { city: '北京', count: '301条活动', url: 'webcal://islon.github.io/goout/output/exhibitions_beijing.ics' },
      { city: '上海', count: '301条活动', url: 'webcal://islon.github.io/goout/output/exhibitions_shanghai.ics' },
      { city: '成都', count: '300条活动', url: 'webcal://islon.github.io/goout/output/exhibitions_chengdu.ics' },
      { city: '重庆', count: '300条活动', url: 'webcal://islon.github.io/goout/output/exhibitions_chongqing.ics' },
      { city: '南京', count: '300条活动', url: 'webcal://islon.github.io/goout/output/exhibitions_nanjing.ics' },
      { city: '西安', count: '300条活动', url: 'webcal://islon.github.io/goout/output/exhibitions_xian.ics' },
      { city: '武汉', count: '300条活动', url: 'webcal://islon.github.io/goout/output/exhibitions_wuhan.ics' }
    ],
    faqs: [
      { q: '订阅后多久能看到活动？', a: '添加订阅后，手机日历会自动同步，通常几分钟内即可看到最新活动。之后每天自动更新。' },
      { q: '国产手机日历不支持订阅怎么办？', a: '华为/小米/OPPO等自带日历大多不支持ICS订阅。建议使用方式一的「微信提醒」，或安装Google Calendar等第三方日历应用。' },
      { q: '微信提醒会一直推送吗？', a: '每个活动只提醒一次，在活动开始前1天推送。你可以在微信设置中随时取消订阅。' },
      { q: '订阅链接打不开？', a: 'webcal:// 开头的链接需要复制到日历App中添加，不能直接在浏览器打开。如果用HTTP链接，请用 https://islon.github.io/goout/output/ 对应城市的.ics文件。' },
      { q: '场馆信息从哪里来？', a: '场馆指南中的场馆介绍由项目团队整理，覆盖已收录的活动场馆。如果你发现错误或想补充，欢迎在反馈页提交。' }
    ]
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

  onGoVenues() {
    wx.switchTab({
      url: '/pages/venues/venues'
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
