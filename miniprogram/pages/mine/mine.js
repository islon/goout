// pages/mine/mine.js
const localActivities = require('../../data/activities.json')

Page({
  data: {
    subscriptions: [],
    isEmpty: true
  },

  onShow() {
    this.loadSubscriptions()
  },

  loadSubscriptions() {
    const subs = wx.getStorageSync('subscriptions') || []
    // 与列表同源：优先用缓存，兜底本地 JSON
    const source = wx.getStorageSync('activitiesCache') || localActivities
    const subActivities = subs.map(id => {
      const a = source[id]
      if (!a) return null
      return {
        ...a,
        _id: id,
        _dateRange: a.start_date === a.end_date ? a.start_date : `${a.start_date} ~ ${a.end_date}`,
        _isFree: a.fee === '免费' || a.fee === '免费需预约'
      }
    }).filter(Boolean)

    // 按开始日期排序
    subActivities.sort((a, b) => a.start_date.localeCompare(b.start_date))

    this.setData({
      subscriptions: subActivities,
      isEmpty: subActivities.length === 0
    })
  },

  onActivityTap(e) {
    wx.navigateTo({
      url: `/pages/detail/detail?id=${e.currentTarget.dataset.id}`
    })
  },

  onExploreTap() {
    wx.switchTab({ url: '/pages/index/index' })
  },

  onShareAppMessage() {
    return {
      title: '童行 - 全国亲子活动日历',
      path: '/pages/index/index'
    }
  }
})
