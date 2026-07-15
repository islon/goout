// pages/venueDetail/venueDetail.js
const localVenues = require('../../data/venues.json')

const CITY_REVERSE = {
  'shenzhen': '深圳', 'beijing': '北京', 'shanghai': '上海', 'guangzhou': '广州', 'hangzhou': '杭州'
}

Page({
  data: {
    venue: null
  },

  onLoad(options) {
    let id = options.id
    try { id = decodeURIComponent(id) } catch (e) {}

    // 优先从列表页写入的缓存读取（与列表同源，id 一致），兜底本地 JSON
    const cache = wx.getStorageSync('venuesCache') || localVenues
    let venue = cache.find(v => v.id === id)
    if (!venue) venue = localVenues.find(v => v.id === id)

    if (!venue) {
      wx.showToast({ title: '场馆不存在', icon: 'error' })
      setTimeout(() => wx.navigateBack(), 1500)
      return
    }

    this.setData({
      venue: {
        ...venue,
        _cityName: CITY_REVERSE[venue.city] || venue.city,
        _isFree: venue.fee === '免费' || venue.fee === '免费需预约',
        _highlights: Array.isArray(venue.highlights) ? venue.highlights : []
      }
    })
  },

  onCopyLink() {
    const url = this.data.venue.official_url || ''
    if (!url) return
    wx.setClipboardData({
      data: url,
      success: () => wx.showToast({ title: '链接已复制', icon: 'success' })
    })
  },

  onCopyAddress() {
    const addr = this.data.venue.address || ''
    if (!addr) return
    wx.setClipboardData({
      data: addr,
      success: () => wx.showToast({ title: '地址已复制', icon: 'success' })
    })
  },

  onShareAppMessage() {
    return {
      title: this.data.venue.name,
      path: `/pages/venueDetail/venueDetail?id=${encodeURIComponent(this.data.venue.id)}`
    }
  }
})
