// 打包内 cities 仅作离线兜底；运行期优先用 app.getCities()（远程 cities.json），
// 云侧新增城市后无需重新发布小程序版本即可出现在城市 tab。
const { cities: bundledCities, timeFilters, familyFilters, typeFilters, feeFilters, districtsByCity, venuesByCity, sourceToVenue } = require('../../data/filters.js');
const { getFilteredExhibitions, buildDisplayItems, getActivityType, getFeeType, getDistrict, getPresentDistricts, matchSource, normalizeCity } = require('../../utils/helpers.js');

const PAGE_SIZE = 20;
const FILTER_STORAGE_KEY = 'goout_filter_state';
const FILTER_KEYS = ['cityFilter', 'timeFilter', 'familyFilter', 'typeFilter', 'districtFilter', 'sourceFilter', 'feeFilter', 'searchQuery'];
const app = getApp();

Page({
  data: {
    cities: bundledCities,
    timeFilters,
    familyFilters,
    typeFilters,
    feeFilters,
    districts: [],
    venues: [],
    displayVenues: [],

    // 当前筛选状态
    cityFilter: 'shenzhen',
    timeFilter: 'upcoming',
    familyFilter: 'all',
    typeFilter: 'all',
    districtFilter: 'all',
    sourceFilter: 'all',
    feeFilter: 'all',
    searchQuery: '',

    // 展示数据
    totalCount: 0,
    currentPage: 1,
    totalPages: 1,
    pageItems: [],
    pageSize: PAGE_SIZE,

    // 筛选可用性
    showAllSources: false,
    loading: false,
    refreshing: false,
    lastUpdateText: ''
  },

  onLoad() {
    const self = this;
    this.restoreFilters();
    this.syncCities();
    this.updateDistrictsAndVenues();
    this.updateLastUpdateText();
    // 等待数据准备完成后加载
    app.onReady(function() {
      self.syncCities();
      self.loadData();
      self.updateLastUpdateText();
    });
    // 后台静默更新到最新数据后，自动刷新列表（用户无感）
    app.onDataUpdated(function() {
      self.syncCities();
      self.loadData();
      self.updateDistrictsAndVenues();
      self.updateLastUpdateText();
    });
    // 云侧新增/减少城市时（app 拉到新的 cities.json）刷新城市 tab
    if (app && typeof app.onCitiesUpdated === 'function') {
      app.onCitiesUpdated(function() {
        self.syncCities();
        self.updateDistrictsAndVenues();
        self.loadData();
      });
    }
  },

  // 将运行期城市清单（app.getCities()，回退打包兜底）同步进页面 data.cities，
  // disabled 状态仍由 updateFilterAvailability 计算
  syncCities() {
    let runtime = bundledCities;
    try {
      if (app && typeof app.getCities === 'function') {
        const list = app.getCities();
        if (Array.isArray(list) && list.length) runtime = list;
      }
    } catch (e) {}
    this.setData({
      cities: runtime.map(function(c) { return { key: c.key, name: c.name }; })
    });
  },

  onShow() {
    // 如果从详情页返回，不需要重新加载
  },

  // 恢复上次保存的筛选条件（城市/时间/亲子/类型/区县/场馆/费用/搜索）
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
      console.warn('[童行] 恢复筛选条件失败', e);
    }
  },

  // 将当前筛选条件写入本地存储，下次进入自动恢复
  saveFilters() {
    try {
      const d = this.data;
      const saved = {};
      FILTER_KEYS.forEach(function(k) { saved[k] = d[k]; });
      wx.setStorageSync(FILTER_STORAGE_KEY, saved);
    } catch (e) {
      console.warn('[童行] 保存筛选条件失败', e);
    }
  },

  onPullDownRefresh() {
    this.doRefresh(true);
  },

  // 点击刷新按钮
  onRefreshTap() {
    if (this.data.refreshing) return;
    this.doRefresh(false);
  },

  // 统一刷新逻辑：委托 app.js 拉取最新数据并写缓存
  doRefresh(isPullDown) {
    const self = this;
    if (this.data.refreshing) return;
    this.setData({ refreshing: true });

    app.forceRefresh(function(success) {
      self.loadData();
      self.updateDistrictsAndVenues();
      self.updateLastUpdateText();
      self.setData({ refreshing: false });
      if (isPullDown) wx.stopPullDownRefresh();
      wx.showToast({
        title: success ? '数据已更新' : '网络不给力',
        icon: success ? 'success' : 'none'
      });
    });
  },

  // 显示数据更新时间
  updateLastUpdateText() {
    const cacheTime = wx.getStorageSync('goout_exhibitions_cache_time') || 0;
    if (!cacheTime) {
      this.setData({ lastUpdateText: '' });
      return;
    }
    const now = Date.now();
    const diff = now - cacheTime;
    let text = '';
    if (diff < 60000) {
      text = '刚刚更新';
    } else if (diff < 3600000) {
      text = Math.floor(diff / 60000) + '分钟前更新';
    } else if (diff < 86400000) {
      text = Math.floor(diff / 3600000) + '小时前更新';
    } else {
      text = Math.floor(diff / 86400000) + '天前更新';
    }
    this.setData({ lastUpdateText: text + ' · 共 ' + (app.globalData.exhibitions || []).length + ' 条活动' });
  },

  // 更新区县和场馆列表
  updateDistrictsAndVenues() {
    const city = this.data.cityFilter;
    const district = this.data.districtFilter;
    let allVenues = venuesByCity[city] || [];
    if (!allVenues.length) {
      // 新城市未配置 venuesByCity 时，从数据动态汇总去重 source，
      // 保证"往 filters.cities 加一个城市"即可自动拥有来源/场馆筛选，无需手工补 venuesByCity
      const seen = {};
      (app.globalData.exhibitions || []).forEach(function(e) {
        if ((e._cityKey || normalizeCity(e.city)) !== city) return;
        const s = e.source;
        if (s && !seen[s]) seen[s] = { key: s, name: sourceToVenue[s] || e.venue || s };
      });
      allVenues = [{ key: 'all', name: '全部地点' }].concat(Object.keys(seen).map(function(k) { return seen[k]; }));
    }

    // 选择区县后，按区县过滤场馆列表，只显示该区县的场馆
    if (district && district !== 'all') {
      const districtVenues = {};
      // 从场馆信息中按 city + district 提取
      (app.globalData.venues || []).forEach(function(v) {
        if (v.city === city && v.district === district && v.source) {
          districtVenues[v.source] = v.name || v.source;
        }
      });
      // 从活动数据中补充该区县的场馆
      (app.globalData.exhibitions || []).forEach(function(e) {
        if ((e._cityKey || normalizeCity(e.city)) === city && e.district === district && e.source) {
          if (!districtVenues[e.source]) districtVenues[e.source] = e.venue || e.source;
        }
      });
      allVenues = [{ key: 'all', name: '全部地点' }].concat(
        Object.keys(districtVenues).map(function(k) { return { key: k, name: districtVenues[k] }; })
      );
    }

    const displayVenues = this.data.showAllSources
      ? allVenues
      : allVenues.filter(function(v, i) { return i < 8 || v.key === 'all'; });
    const rawDistricts = getPresentDistricts(city, app.globalData.exhibitions || []);
    const districts = rawDistricts.map(function(d) {
      return { name: d, disabled: false };
    });
    this.setData({
      districts: districts,
      venues: allVenues,
      displayVenues: displayVenues
    });
  },

  loadData() {
    const filters = {
      city: this.data.cityFilter,
      time: this.data.timeFilter,
      family: this.data.familyFilter,
      type: this.data.typeFilter,
      district: this.data.districtFilter,
      source: this.data.sourceFilter,
      fee: this.data.feeFilter,
      search: this.data.searchQuery
    };

    const allExhibitions = app.globalData.exhibitions || [];
    const filtered = getFilteredExhibitions(allExhibitions, filters);
    filtered.sort(function(a, b) { return a.start_date.localeCompare(b.start_date); });

    const displayItems = buildDisplayItems(filtered);
    const totalPages = Math.ceil(displayItems.length / PAGE_SIZE) || 1;

    // 完整筛选结果存实例变量 this._all，避免把上千条对象整体 setData（小程序大数组序列化会卡顿）
    this._all = displayItems;
    this.setData({
      totalCount: displayItems.length,
      totalPages: totalPages,
      currentPage: 1,
      pageItems: displayItems.slice(0, PAGE_SIZE),
      loading: false
    });

    this.updateFilterAvailability(filtered);
  },

  // 检查筛选器是否有结果
  updateFilterAvailability(filtered) {
    const self = this;
    const baseFilters = {
      city: this.data.cityFilter,
      time: this.data.timeFilter,
      family: this.data.familyFilter,
      type: this.data.typeFilter,
      district: this.data.districtFilter,
      source: this.data.sourceFilter,
      fee: this.data.feeFilter,
      search: this.data.searchQuery
    };

    function checkResult(type, testValue) {
      const testFilters = Object.assign({}, baseFilters);
      if (type === 'city') {
        testFilters.city = testValue;
        testFilters.district = 'all';
        testFilters.source = 'all';
      } else {
        testFilters[type] = testValue;
      }
      const allExhibitions = app.globalData.exhibitions || [];
      return getFilteredExhibitions(allExhibitions, testFilters).length > 0;
    }

    // 城市置灰仅在“远程/完整数据已加载”后才生效；本地兜底(默认5城)阶段不置灰，
    // 否则西安/重庆等尚未加载到本地的城市会被永久置灰、无法点击
    const isRemote = app.globalData.isRemoteData;
    const citiesAvail = this.data.cities.map(function(c) {
      return Object.assign({}, c, { disabled: isRemote && !checkResult('city', c.key) && c.key !== self.data.cityFilter });
    });

    const timeAvail = this.data.timeFilters.map(function(t) {
      return Object.assign({}, t, { disabled: !checkResult('time', t.key) && t.key !== self.data.timeFilter });
    });

    const typeAvail = this.data.typeFilters.map(function(t) {
      return Object.assign({}, t, { disabled: !checkResult('type', t.key) && t.key !== self.data.typeFilter });
    });

    const feeAvail = this.data.feeFilters.map(function(f) {
      return Object.assign({}, f, { disabled: !checkResult('fee', f.key) && f.key !== self.data.feeFilter });
    });

    const familyAvail = this.data.familyFilters.map(function(f) {
      return Object.assign({}, f, { disabled: !checkResult('family', f.key) && f.key !== self.data.familyFilter });
    });

    const districtsAvail = (this.data.districts || []).map(function(d) {
      const name = d.name || d;
      return { name: name, disabled: name !== '全部区县' && !checkResult('district', name) && name !== self.data.districtFilter };
    });

    this.setData({
      cities: citiesAvail,
      timeFilters: timeAvail,
      typeFilters: typeAvail,
      feeFilters: feeAvail,
      familyFilters: familyAvail,
      districts: districtsAvail
    });
  },

  // 事件处理
  onCityTap(e) {
    if (e.currentTarget.dataset.disabled) return;
    const city = e.currentTarget.dataset.key;
    if (city === this.data.cityFilter) return;

    this.setData({
      cityFilter: city,
      districtFilter: 'all',
      sourceFilter: 'all',
      currentPage: 1
    });
    this.updateDistrictsAndVenues();
    this.saveFilters();
    this.loadData();
  },

  onTimeTap(e) {
    if (e.currentTarget.dataset.disabled) return;
    const key = e.currentTarget.dataset.key;
    if (key === this.data.timeFilter) return;
    this.setData({ timeFilter: key, currentPage: 1 });
    this.saveFilters();
    this.loadData();
  },

  onFamilyTap(e) {
    if (e.currentTarget.dataset.disabled) return;
    const key = e.currentTarget.dataset.key;
    if (key === this.data.familyFilter) return;
    this.setData({ familyFilter: key, currentPage: 1 });
    this.saveFilters();
    this.loadData();
  },

  onTypeTap(e) {
    if (e.currentTarget.dataset.disabled) return;
    const key = e.currentTarget.dataset.key;
    if (key === this.data.typeFilter) return;
    this.setData({ typeFilter: key, currentPage: 1 });
    this.saveFilters();
    this.loadData();
  },

  onDistrictTap(e) {
    if (e.currentTarget.dataset.disabled) return;
    const name = e.currentTarget.dataset.name;
    const district = name === '全部区县' ? 'all' : name;
    if (district === this.data.districtFilter) return;
    this.setData({ districtFilter: district, sourceFilter: 'all', currentPage: 1 });
    this.updateDistrictsAndVenues();
    this.saveFilters();
    this.loadData();
  },

  onSourceTap(e) {
    const key = e.currentTarget.dataset.key;
    if (key === this.data.sourceFilter) return;
    this.setData({ sourceFilter: key, currentPage: 1 });
    this.saveFilters();
    this.loadData();
  },

  onFeeTap(e) {
    if (e.currentTarget.dataset.disabled) return;
    const key = e.currentTarget.dataset.key;
    if (key === this.data.feeFilter) return;
    this.setData({ feeFilter: key, currentPage: 1 });
    this.saveFilters();
    this.loadData();
  },

  onSearchInput(e) {
    this.setData({ searchQuery: e.detail.value, currentPage: 1 });
    this.saveFilters();
    if (this._searchTimer) clearTimeout(this._searchTimer);
    this._searchTimer = setTimeout(this.loadData.bind(this), 300);
  },

  onClearSearch() {
    this.setData({ searchQuery: '', currentPage: 1 });
    this.saveFilters();
    this.loadData();
  },

  toggleSourceList() {
    const showAll = !this.data.showAllSources;
    const allVenues = this.data.venues;
    const displayVenues = showAll
      ? allVenues
      : allVenues.filter(function(v, i) { return i < 8 || v.key === 'all'; });
    this.setData({ showAllSources: showAll, displayVenues: displayVenues });
  },

  onPrevPage() {
    if (this.data.currentPage <= 1) return;
    const page = this.data.currentPage - 1;
    const all = this._all || [];
    this.setData({
      currentPage: page,
      pageItems: all.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE)
    });
    wx.pageScrollTo({ scrollTop: 0, duration: 200 });
  },

  onNextPage() {
    if (this.data.currentPage >= this.data.totalPages) return;
    const page = this.data.currentPage + 1;
    const all = this._all || [];
    this.setData({
      currentPage: page,
      pageItems: all.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE)
    });
    wx.pageScrollTo({ scrollTop: 0, duration: 200 });
  },

  onCardTap(e) {
    const id = e.currentTarget.dataset.id;
    wx.navigateTo({
      url: '/pages/detail/detail?id=' + encodeURIComponent(id)
    });
  },

  onShareAppMessage() {
    return {
      title: '童行 - 全国亲子活动日历',
      path: '/pages/index/index'
    };
  }
});
