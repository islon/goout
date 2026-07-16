// 童行小程序 - 场馆指南列表页
const { cities } = require('../../data/filters.js');
const { findVenue, buildVenueActivityCounts } = require('../../utils/helpers.js');
const app = getApp();

// 城市显示名映射（与 filters.cities 单一来源保持一致，避免两处维护漂移）
const cityNameMap = {};
cities.forEach(function(c) { cityNameMap[c.key] = c.name; });

// 城市 tab：直接来自 filters.cities（固定 10 城），不再依赖“已加载数据里有哪些城市”，
// 否则旧版 5 城缓存 / 远程未加载时场馆指南只会显示部分城市
const CITY_TABS = [{ key: 'all', name: '全部' }].concat(
  cities.map(function(c) { return { key: c.key, name: c.name }; })
);

const FILTER_STORAGE_KEY = 'goout_venue_filter_state';
const FILTER_KEYS = ['cityFilter', 'typeFilter', 'searchQuery'];

Page({
  data: {
    cityFilter: 'all',
    typeFilter: 'all',
    searchQuery: '',
    cities: [],
    types: [],
    venues: [],
    activityCounts: {},
    loading: true
  },

  onLoad() {
    this.restoreFilters();
    this.loadData();
  },

  onShow() {
    this.loadData();
  },

  // 恢复上次保存的场馆页筛选条件
  restoreFilters() {
    try {
      const saved = wx.getStorageSync(FILTER_STORAGE_KEY);
      if (saved && typeof saved === 'object') {
        const patch = {};
        FILTER_KEYS.forEach(function(k) {
          if (saved[k] !== undefined && saved[k] !== null) patch[k] = saved[k];
        });
        if (Object.keys(patch).length) this.setData(patch);
      }
    } catch (e) {
      console.warn('[童行] 恢复场馆筛选失败', e);
    }
  },

  // 保存场馆页筛选条件
  saveFilters() {
    try {
      const d = this.data;
      const saved = {};
      FILTER_KEYS.forEach(function(k) { saved[k] = d[k]; });
      wx.setStorageSync(FILTER_STORAGE_KEY, saved);
    } catch (e) {
      console.warn('[童行] 保存场馆筛选失败', e);
    }
  },

  loadData() {
    // 防御：远程数据异常(如被拦截返回HTML字符串)时 globalData.venues 可能不是数组，强制规整避免 .filter 崩潰白屏
    const allVenues = Array.isArray(app.globalData.venues) ? app.globalData.venues : [];
    const allExhibitions = Array.isArray(app.globalData.exhibitions) ? app.globalData.exhibitions : [];

    const typeSet = {};
    for (let i = 0; i < allVenues.length; i++) {
      const v = allVenues[i];
      if (v.type) typeSet[v.type] = true;
    }

    const types = [{ key: 'all', name: '全部类型' }];
    Object.keys(typeSet).sort().forEach(function(t) {
      types.push({ key: t, name: t });
    });

    const activityCounts = buildVenueActivityCounts(allVenues, allExhibitions);

    this.setData({
      cities: CITY_TABS,
      types: types,
      activityCounts: activityCounts,
      loading: false
    }, () => {
      this.applyFilters();
    });
  },

  applyFilters() {
    const allVenues = Array.isArray(app.globalData.venues) ? app.globalData.venues : [];
    const cityFilter = this.data.cityFilter;
    const typeFilter = this.data.typeFilter;
    const query = this.data.searchQuery.toLowerCase().trim();

    const filtered = allVenues.filter(v => {
      if (cityFilter !== 'all' && v.city !== cityFilter) return false;
      if (typeFilter !== 'all' && v.type !== typeFilter) return false;
      if (query) {
        const name = (v.name || '').toLowerCase();
        const address = (v.address || '').toLowerCase();
        const description = (v.description || '').toLowerCase();
        if (name.indexOf(query) < 0 && address.indexOf(query) < 0 && description.indexOf(query) < 0) {
          return false;
        }
      }
      return true;
    });

    this.setData({
      venues: filtered.map(v => {
        const count = this.data.activityCounts[v.name] || 0;
        return Object.assign({}, v, {
          cityName: cityNameMap[v.city] || v.city,
          activityCount: count,
          hasActivity: count > 0
        });
      })
    });
  },

  onCityTap(e) {
    this.setData({ cityFilter: e.currentTarget.dataset.key }, () => this.applyFilters());
    this.saveFilters();
  },

  onTypeTap(e) {
    this.setData({ typeFilter: e.currentTarget.dataset.key }, () => this.applyFilters());
    this.saveFilters();
  },

  onSearchInput(e) {
    this.setData({ searchQuery: e.detail.value }, () => this.applyFilters());
    this.saveFilters();
  },

  onVenueTap(e) {
    const name = e.currentTarget.dataset.name;
    wx.navigateTo({
      url: '/pages/venue/venue?id=' + encodeURIComponent(name)
    });
  },

  onShareAppMessage() {
    return {
      title: '童行 - 场馆指南',
      path: '/pages/venues/venues'
    };
  }
});
