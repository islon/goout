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
    // 筛选选项
    categories: ['全部', '演出', '展览', '亲子活动', '科普活动', '讲座阅读', '体育赛事', '影视放映', '其他'],
    fees: ['全部', '免费', '收费'],
    cities: ['全部', '深圳', '北京', '上海', '广州'],
    // 城市映射
    cityMap: {
      '深圳': 'shenzhen',
      '北京': 'beijing',
      '上海': 'shanghai',
      '广州': 'guangzhou'
    },
    cityReverseMap: {
      'shenzhen': '深圳',
      'beijing': '北京',
      'shanghai': '上海',
      'guangzhou': '广州'
    },
    showFilter: false,
    loading: true
  },

  onLoad() {
    this.initData()
  },

  initData() {
    const today = this.getTodayStr()
    // 只展示今天及以后的活动
    const upcoming = activitiesData.filter(a => {
      return a.end_date >= today || a.start_date >= today
    }).map((a, idx) => {
      return {
        ...a,
        _id: idx,
        _cityName: this.data.cityReverseMap[a.city] || a.city,
        _dateRange: this.formatDateRange(a.start_date, a.end_date),
        _isFree: a.fee === '免费' || a.fee === '免费需预约',
        _isFamily: a.family_friendly === true
      }
    })
    // 按开始日期排序
    upcoming.sort((a, b) => a.start_date.localeCompare(b.start_date))
    
    this.setData({
      activities: upcoming,
      filteredActivities: upcoming,
      loading: false
    })
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

  // 筛选切换
  onCategoryTap(e) {
    this.setData({ activeCategory: e.currentTarget.dataset.value })
    this.applyFilters()
  },

  onFeeTap(e) {
    this.setData({ activeFee: e.currentTarget.dataset.value })
    this.applyFilters()
  },

  onFamilyTap(e) {
    this.setData({ activeFamily: e.currentTarget.dataset.value })
    this.applyFilters()
  },

  onCityTap(e) {
    this.setData({ activeCity: e.currentTarget.dataset.value })
    this.applyFilters()
  },

  applyFilters() {
    const { activities, activeCategory, activeFee, activeFamily, activeCity, cityMap } = this.data
    let result = activities

    if (activeCategory !== '全部') {
      result = result.filter(a => a.category === activeCategory)
    }
    if (activeFee !== '全部') {
      if (activeFee === '免费') {
        result = result.filter(a => a._isFree)
      } else {
        result = result.filter(a => !a._isFree)
      }
    }
    if (activeFamily === 'family') {
      result = result.filter(a => a._isFamily)
    }
    if (activeCity !== '全部') {
      const cityCode = cityMap[activeCity]
      result = result.filter(a => a.city === cityCode)
    }

    this.setData({ filteredActivities: result })
  },

  toggleFilter() {
    this.setData({ showFilter: !this.data.showFilter })
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
