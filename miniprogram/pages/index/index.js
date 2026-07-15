// pages/index/index.js
// 数据来源：运行时通过云函数 getActivities 实时拉取网页（GitHub Pages）数据，
// 从而自动跟随 Web 版更新，无需重新上传小程序代码。
// 本地 data/activities.json 仅作云函数不可用时的兜底。

const localActivities = require('../../data/activities.json')

Page({
  data: {
    activities: [],
    filteredActivities: [],
    activeCategory: '全部',
    activeFee: '全部',
    activeFamily: 'all',
    activeCity: '全部',
    activeTime: 'upcoming',
    activeDistrict: 'all',
    categories: ['全部', '展览', '讲座阅读', '科普活动', '演出', '影视放映', '体育赛事', '亲子活动'],
    fees: ['全部', '免费', '收费'],
    times: ['upcoming', 'today', 'tomorrow', 'week', 'month'],
    timeLabels: { upcoming: '最近', today: '今天', tomorrow: '明天', week: '本周', month: '本月' },
    cities: ['全部', '深圳', '北京', '上海', '广州', '杭州'],
    cityMap: {
      '深圳': 'shenzhen', '北京': 'beijing', '上海': 'shanghai', '广州': 'guangzhou', '杭州': 'hangzhou'
    },
    cityReverseMap: {
      'shenzhen': '深圳', 'beijing': '北京', 'shanghai': '上海', 'guangzhou': '广州', 'hangzhou': '杭州'
    },
    districtOptions: ['全部区县'],
    loading: true
  },

  onLoad() {
    this.loadActivities()
  },

  // 优先从云函数拉取实时数据，失败则降级本地 JSON
  loadActivities() {
    const useLocal = () => {
      wx.setStorageSync('activitiesCache', localActivities)
      this.buildDistrictMap(localActivities)
      this.initData(localActivities)
    }

    if (!wx.cloud || !wx.cloud.callFunction) {
      useLocal()
      return
    }

    wx.cloud.callFunction({
      name: 'getActivities',
      data: {},
      success: (res) => {
        const r = res.result
        if (r && r.success && Array.isArray(r.data) && r.data.length > 0) {
          wx.setStorageSync('activitiesCache', r.data)
          this.buildDistrictMap(r.data)
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

  // 从数据源动态提取"城市→区县"映射，供联动筛选
  buildDistrictMap(source) {
    const map = {}
    source.forEach(a => {
      if (!a.city || !a.district) return
      if (!map[a.city]) map[a.city] = new Set()
      map[a.city].add(a.district)
    })
    this._districtMap = {}
    Object.keys(map).forEach(city => {
      this._districtMap[city] = ['全部区县', ...Array.from(map[city]).sort()]
    })
  },

  initData(source) {
    const enriched = source.map((a, idx) => ({
      ...a,
      _id: idx,
      _cityName: this.data.cityReverseMap[a.city] || a.city,
      _dateRange: this.formatDateRange(a.start_date, a.end_date),
      _isFree: a.fee === '免费' || a.fee === '免费需预约',
      _isFamily: a.family_friendly === true
    }))
    this._allActivities = enriched
    this.setData({ activities: enriched, loading: false })
    this.applyFilters()
  },

  getTodayStr() {
    const d = new Date()
    const y = d.getFullYear()
    const m = String(d.getMonth() + 1).padStart(2, '0')
    const day = String(d.getDate()).padStart(2, '0')
    return `${y}-${m}-${day}`
  },

  formatDateRange(start, end) {
    if (start === end) return start
    return `${start} ~ ${end}`
  },

  // 时间筛选算法，与 Web 版保持一致
  matchTime(a, timeFilter, today) {
    if (timeFilter === 'all' || !timeFilter) return true
    if (timeFilter === 'upcoming') return a.end_date >= today
    if (timeFilter === 'today') {
      return a.start_date === today || (a.start_date <= today && a.end_date >= today)
    }
    if (timeFilter === 'tomorrow') {
      const t = new Date(); t.setDate(t.getDate() + 1)
      const ts = this.fmt(t)
      return a.start_date === ts || (a.start_date <= ts && a.end_date >= ts)
    }
    if (timeFilter === 'week') {
      const t = new Date(); t.setDate(t.getDate() + 7)
      const ts = this.fmt(t)
      return a.start_date <= ts && a.end_date >= today
    }
    if (timeFilter === 'month') {
      const d = new Date(a.start_date)
      const now = new Date()
      return d.getFullYear() === now.getFullYear() && d.getMonth() === now.getMonth()
    }
    return true
  },

  fmt(d) {
    const y = d.getFullYear()
    const m = String(d.getMonth() + 1).padStart(2, '0')
    const day = String(d.getDate()).padStart(2, '0')
    return `${y}-${m}-${day}`
  },

  onCategoryTap(e) {
    this.setData({ activeCategory: e.currentTarget.dataset.value })
    this.applyFilters()
  },

  onFeeTap(e) {
    const v = e.currentTarget.dataset.value
    this.setData({ activeFee: v === '免费' ? '免费' : (v === '收费' ? '收费' : '全部') })
    this.applyFilters()
  },

  onFamilyTap(e) {
    this.setData({ activeFamily: this.data.activeFamily === 'family' ? 'all' : 'family' })
    this.applyFilters()
  },

  onCityTap(e) {
    const city = e.currentTarget.dataset.value
    const cityCode = this.data.cityMap[city]
    let districtOptions = ['全部区县']
    if (cityCode && this._districtMap && this._districtMap[cityCode]) {
      districtOptions = this._districtMap[cityCode]
    }
    this.setData({ activeCity: city, activeDistrict: 'all', districtOptions })
    this.applyFilters()
  },

  onTimeTap(e) {
    this.setData({ activeTime: e.currentTarget.dataset.value })
    this.applyFilters()
  },

  onDistrictTap(e) {
    this.setData({ activeDistrict: e.currentTarget.dataset.value })
    this.applyFilters()
  },

  applyFilters() {
    const { activeCategory, activeFee, activeFamily, activeCity, activeTime, activeDistrict, cityMap } = this.data
    const today = this.getTodayStr()
    let result = this._allActivities

    if (activeCity !== '全部') {
      const cityCode = cityMap[activeCity]
      result = result.filter(a => a.city === cityCode)
    }
    if (activeCity !== '全部' && activeDistrict !== 'all') {
      result = result.filter(a => a.district === activeDistrict)
    }
    if (activeCategory !== '全部') {
      result = result.filter(a => a.category === activeCategory)
    }
    if (activeFee === '免费') {
      result = result.filter(a => a._isFree)
    } else if (activeFee === '收费') {
      result = result.filter(a => !a._isFree)
    }
    if (activeFamily === 'family') {
      result = result.filter(a => a._isFamily)
    }
    result = result.filter(a => this.matchTime(a, activeTime, today))

    result = result.slice().sort((a, b) => a.start_date.localeCompare(b.start_date))
    this.setData({ filteredActivities: result })
  },

  onActivityTap(e) {
    const id = e.currentTarget.dataset.id
    wx.navigateTo({ url: `/pages/detail/detail?id=${id}` })
  },

  onShareAppMessage() {
    return { title: '童行 - 全国亲子活动日历', path: '/pages/index/index' }
  }
})
