// 童行小程序 - 场馆指南列表页
const { findVenue, buildVenueActivityCounts } = require('../../utils/helpers.js');
const app = getApp();

const cityNames = {
  shenzhen: '深圳',
  guangzhou: '广州',
  shanghai: '上海',
  beijing: '北京',
  hangzhou: '杭州'
};

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
    this.loadData();
  },

  onShow() {
    this.loadData();
  },

  loadData() {
    const allVenues = app.globalData.venues || [];
    const allExhibitions = app.globalData.exhibitions || [];

    const citySet = {};
    const typeSet = {};
    for (let i = 0; i < allVenues.length; i++) {
      const v = allVenues[i];
      if (v.city) citySet[v.city] = true;
      if (v.type) typeSet[v.type] = true;
    }

    const cities = [{ key: 'all', name: '全部' }];
    Object.keys(citySet).sort().forEach(function(c) {
      cities.push({ key: c, name: cityNames[c] || c });
    });

    const types = [{ key: 'all', name: '全部类型' }];
    Object.keys(typeSet).sort().forEach(function(t) {
      types.push({ key: t, name: t });
    });

    const activityCounts = buildVenueActivityCounts(allVenues, allExhibitions);

    this.setData({
      cities: cities,
      types: types,
      activityCounts: activityCounts,
      loading: false
    }, () => {
      this.applyFilters();
    });
  },

  applyFilters() {
    const allVenues = app.globalData.venues || [];
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
          cityName: cityNames[v.city] || v.city,
          activityCount: count,
          hasActivity: count > 0
        });
      })
    });
  },

  onCityTap(e) {
    this.setData({ cityFilter: e.currentTarget.dataset.key }, () => this.applyFilters());
  },

  onTypeTap(e) {
    this.setData({ typeFilter: e.currentTarget.dataset.key }, () => this.applyFilters());
  },

  onSearchInput(e) {
    this.setData({ searchQuery: e.detail.value }, () => this.applyFilters());
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
