// 童行小程序 - 场馆指南列表页
// 打包内城市清单仅作离线兜底；运行期优先用 app.getCities()（来自远程 cities.json），
// 这样云侧新增城市后无需重新发布小程序版本即可出现在城市 tab。
const { cities: bundledCities } = require('../../data/filters.js');
const { findVenue, buildVenueActivityCounts } = require('../../utils/helpers.js');
const app = getApp();

// 取运行期城市清单：优先 app.getCities()（远程/缓存），回退打包兜底
function getRuntimeCities() {
  try {
    if (app && typeof app.getCities === 'function') {
      const list = app.getCities();
      if (Array.isArray(list) && list.length) return list;
    }
  } catch (e) {}
  return bundledCities;
}

// 由城市清单构建 key→显示名 映射
function buildCityNameMap(list) {
  const map = {};
  (list || []).forEach(function(c) { map[c.key] = c.name; });
  return map;
}

// 由城市清单构建城市 tab（含“全部”）
function buildCityTabs(list) {
  return [{ key: 'all', name: '全部' }].concat(
    (list || []).map(function(c) { return { key: c.key, name: c.name }; })
  );
}

// 模块级可变映射：applyFilters 用它把 city key 转显示名；loadData 时会随运行期清单重建
var cityNameMap = buildCityNameMap(getRuntimeCities());

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
    cityNameMap: cityNameMap,
    loading: true
  },

  onLoad() {
    this.restoreFilters();
    this.loadData();
    // 云侧新增/减少城市时（app 拉到新的 cities.json）刷新城市 tab
    const self = this;
    if (app && typeof app.onCitiesUpdated === 'function') {
      app.onCitiesUpdated(function() { self.loadData(); });
    }
    // 场馆数据异步加载/补齐完成后刷新本页（避免打开时仍显示裁剪兜底数）
    if (app && typeof app.onDataUpdated === 'function') {
      app.onDataUpdated(function() { self.loadData(); });
    }
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
    // 每次加载都按运行期城市清单重建 tab 与名称映射（响应云侧新增城市）
    const runtimeCities = getRuntimeCities();
    cityNameMap = buildCityNameMap(runtimeCities);
    const cityTabs = buildCityTabs(runtimeCities);

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
      cities: cityTabs,
      cityNameMap: cityNameMap,
      types: types,
      activityCounts: activityCounts,
      loading: false
    }, () => {
      this.applyFilters();
      // onDataUpdated 是一次性的，每次统计后重新登记自身，使场馆补齐/刷新后本页实时更新
      if (app && typeof app.onDataUpdated === 'function') {
        const self = this;
        app.onDataUpdated(function() { self.loadData(); });
      }
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
