// pages/index/index.js
const activitiesData = require('../../data/activities.json')

Page({
  data: {
    activities: [],
    filteredActivities: [],
    // 筛选状态
    activeCategory: '全部',
    activeFee: '全部',
    activeFamily: 'all',
    activeCity: '全部',
    activeTime: 'upcoming',     // 默认"最近活动"，与 Web 版一致
    activeDistrict: 'all',
    // 筛选选项
    categories: ['全部', '展览', '讲座阅读', '科普活动', '演出', '影视放映', '体育赛事', '亲子活动'],
    fees: ['全部', '免费', '收费'],
    times: ['upcoming', 'today', 'tomorrow', 'week', 'month'],
    timeLabels: { upcoming: '最近', today: '今天', tomorrow: '明天', week: '本周', month: '本月' },
    cities: ['全部', '深圳', '北京', '上海', '广州', '杭州'],
    cityMap: {
      '深圳': 'shenzhen',
      '北京': 'beijing',
      '上海': 'shanghai',
      '广州': 'guangzhou',
      '杭州': 'hangzhou'
    },
    cityReverseMap: {
      'shenzhen': '深圳',
      'beijing': '北京',
      'shanghai': '上海',
      'guangzhou': '广州',
      'hangzhou': '杭州'
    },
    // 按城市联动的区县列表（动态生成）
    districtOptions: ['全部区县'],
    loading: true
  },

  onLoad() {
    this.buildDistrictMap()
    this.initData()
  },

  // 从数据动态提取每个城市的区县，供联动筛选使用
  buildDistrictMap() {
    const map = {}
    activitiesData.forEach(a => {
      if (!a.city || !a.district) return
      if (!map[a.city]) map[a.city] = new Set()
      map[a.city].add(a.district)
    })
    // 转为有序数组存到全局
    this._districtMap = {}
    Object.keys(map).forEach(city => {
      this._districtMap[city] = ['全部区县', ...Array.from(map[city]).sort()]
    })
  },

  initData() {
    const today = this.getTodayStr()
    const enriched = activitiesData.map((a, idx) => {
      return {
        ...a,
        _id: idx,
        _cityName: this.data.cityReverseMap[a.city] || a.city,
        _dateRange: this.formatDateRange(a.start_date, a.end_date),
        _isFree: a.fee === '免费' || a.fee === '免费需预约',
        _isFamily: a.family_friendly === true
      }
    })
    // 用于后续筛选的源数据（不预先过滤，交给 applyFilters 统一处理）
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
    if (timeFilter === 'upcoming') {
      return a.end_date >= today
    }
    if (timeFilter === 'today') {
      return a.start_date === today || (a.start_date <= today && a.end_date >= today)
    }
    if (timeFilter === 'tomorrow') {
      const t = new Date()
      t.setDate(t.getDate() + 1)
      const ts = this.fmt(t)
      return a.start_date === ts || (a.start_date <= ts && a.end_date >= ts)
    }
    if (timeFilter === 'week') {
      const t = new Date()
      t.setDate(t.getDate() + 7)
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

  // 筛选切换
  onCategoryTap(e) {
    this.setData({ activeCategory: e.currentTarget.dataset.value })
    this.applyFilters()
  },

  onFeeTap(e) {
    this.setData({ activeFee: e.currentTarget.dataset.value === '免费' ? '免费' : (e.currentTarget.dataset.value === '收费' ? '收费' : '全部') })
    this.applyFilters()
  },

  onFamilyTap(e) {
    this.setData({ activeFamily: e.currentTarget.dataset.value === 'family' ? 'all' : 'family' })
    this.applyFilters()
  },

  onCityTap(e) {
    const city = e.currentTarget.dataset.value
    const cityCode = this.data.cityMap[city]
    // 切换城市时重置区县，并生成对应区县选项
    let districtOptions = ['全部区县']
    if (cityCode && this._districtMap && this._districtMap[cityCode]) {
      districtOptions = this._districtMap[cityCode]
    }
    this.setData({
      activeCity: city,
      activeDistrict: 'all',
      districtOptions: districtOptions
    })
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

    // 城市
    if (activeCity !== '全部') {
      const cityCode = cityMap[activeCity]
      result = result.filter(a => a.city === cityCode)
    }
    // 区县（仅当指定了具体城市时生效）
    if (activeCity !== '全部' && activeDistrict !== 'all') {
      result = result.filter(a => a.district === activeDistrict)
    }
    // 类型
    if (activeCategory !== '全部') {
      result = result.filter(a => a.category === activeCategory)
    }
    // 收费
    if (activeFee === '免费') {
      result = result.filter(a => a._isFree)
    } else if (activeFee === '收费') {
      result = result.filter(a => !a._isFree)
    }
    // 亲子
    if (activeFamily === 'family') {
      result = result.filter(a => a._isFamily)
    }
    // 时间
    result = result.filter(a => this.matchTime(a, activeTime, today))

    // 排序：开始日期升序
    result = result.slice().sort((a, b) => a.start_date.localeCompare(b.start_date))

    this.setData({ filteredActivities: result })
  },

  // 跳转详情页
  onActivityTap(e) {
    const id = e.currentTarget.dataset.id
    wx.navigateTo({
      url: `/pages/detail/detail?id=${id}`
    })
  },

  onShareAppMessage() {
    return {
      title: '童行 - 全国亲子活动日历',
      path: '/pages/index/index'
    }
  }
})
