// pages/venues/venues.js
// 数据来源：运行时通过云函数 getVenues 实时拉取网页（GitHub Pages）场馆数据，
// 从而自动跟随 Web 版更新。本地 data/venues.json 仅作云函数不可用时的兜底。

const localVenues = require('../../data/venues.json')

const CITY_MAP = {
  '深圳': 'shenzhen', '北京': 'beijing', '上海': 'shanghai', '广州': 'guangzhou', '杭州': 'hangzhou'
}
const CITY_REVERSE = {
  'shenzhen': '深圳', 'beijing': '北京', 'shanghai': '上海', 'guangzhou': '广州', 'hangzhou': '杭州'
}

Page({
  data: {
    venues: [],
    filteredVenues: [],
    activeCity: '全部',
    activeType: '全部',
    keyword: '',
    cities: ['全部'],
    types: ['全部'],
    loading: true
  },

  onLoad() {
    this.loadVenues()
  },

  // 优先从云函数拉取实时数据，失败则降级本地 JSON
  loadVenues() {
    const useLocal = () => {
      wx.setStorageSync('venuesCache', localVenues)
      this.initData(localVenues)
    }

    if (!wx.cloud || !wx.cloud.callFunction) {
      useLocal()
      return
    }

    wx.cloud.callFunction({
      name: 'getVenues',
      data: {},
      success: (res) => {
        const r = res.result
        if (r && r.success && Array.isArray(r.data) && r.data.length > 0) {
          wx.setStorageSync('venuesCache', r.data)
          this.initData(r.data)
        } else {
          console.warn('云函数返回空，降级本地', r && r.hint)
          useLocal()
        }
      },
      fail: (err) => {
        console.warn('云函数调用失败，降级本地', err)
        useLocal()
      }
    })
  },

  initData(source) {
    const enriched = source.map(v => ({
      ...v,
      _cityName: CITY_REVERSE[v.city] || v.city,
      _isFree: v.fee === '免费' || v.fee === '免费需预约'
    }))

    // 动态构建城市 / 类型选项
    const citySet = new Set()
    const typeSet = new Set()
    enriched.forEach(v => {
      if (v.city && CITY_REVERSE[v.city]) citySet.add(CITY_REVERSE[v.city])
      if (v.type) typeSet.add(v.type)
    })

    this._allVenues = enriched
    this.setData({
      venues: enriched,
      cities: ['全部', ...Array.from(citySet)],
      types: ['全部', ...Array.from(typeSet).sort()],
      loading: false
    })
    this.applyFilters()
  },

  onCityTap(e) {
    this.setData({ activeCity: e.currentTarget.dataset.value })
    this.applyFilters()
  },

  onTypeTap(e) {
    this.setData({ activeType: e.currentTarget.dataset.value })
    this.applyFilters()
  },

  onSearchInput(e) {
    this.setData({ keyword: (e.detail.value || '').trim().toLowerCase() })
    this.applyFilters()
  },

  onClearSearch() {
    this.setData({ keyword: '' })
    this.applyFilters()
  },

  onPullDownRefresh() {
    this.loadVenues()
    wx.stopPullDownRefresh()
  },

  applyFilters() {
    const { activeCity, activeType, keyword } = this.data
    const cityCode = CITY_MAP[activeCity]
    let result = this._allVenues

    if (activeCity !== '全部') {
      result = result.filter(v => v.city === cityCode)
    }
    if (activeType !== '全部') {
      result = result.filter(v => v.type === activeType)
    }
    if (keyword) {
      result = result.filter(v =>
        (v.name && v.name.toLowerCase().indexOf(keyword) > -1) ||
        (v.address && v.address.toLowerCase().indexOf(keyword) > -1)
      )
    }

    result = result.slice().sort((a, b) =>
      (a._cityName || '').localeCompare(b._cityName || '') ||
      (a.name || '').localeCompare(b.name || '')
    )
    this.setData({ filteredVenues: result })
  },

  onVenueTap(e) {
    const id = e.currentTarget.dataset.id
    wx.navigateTo({ url: `/pages/venueDetail/venueDetail?id=${encodeURIComponent(id)}` })
  },

  onShareAppMessage() {
    return { title: '童行 · 场馆指南', path: '/pages/venues/venues' }
  }
})
