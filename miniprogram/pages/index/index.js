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
    lastUpdateText: '',
    emptyHint: ''
  },

  onLoad() {
    const self = this;
    this.restoreFilters();
    this.syncCities();
    this.updateDistrictsAndVenues();
    this.updateLastUpdateText();
    // 统一刷新入口：从 globalData 取数重渲染，并在 render 后重新登记 onDataUpdated。
    // 关键：onDataUpdated 是一次性回调（每次 notify 即清空），必须每次刷新后重订，
    // 否则首屏静默更新(分级加载各级/Tier完成/场馆补齐)只触达一次，之后列表不再自动刷新。
    const refresh = function() {
      self.syncCities();
      self.loadData();
      self.updateDistrictsAndVenues();
      self.updateLastUpdateText();
      if (app && typeof app.onDataUpdated === 'function') app.onDataUpdated(refresh);
    };
    // 等待数据准备完成后首次加载
    app.onReady(refresh);
    // 后台静默更新到最新数据后，自动刷新列表（用户无感）
    app.onDataUpdated(refresh);
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
    var partialHint = app.globalData.isPartial ? ' · 全部加载中…' : '';
    this.setData({ lastUpdateText: text + ' · 共 ' + (app.globalData.exhibitions || []).length + ' 条活动' + partialHint });
  },

  // 更新区县和场馆列表
  updateDistrictsAndVenues() {
    const city = this.data.cityFilter;
    const district = this.data.districtFilter;
    let allVenues = venuesByCity[city] || [];
    // venuesByCity 仅对深圳/广州/上海/北京等早期城市手工维护；
    // 其余城市（或仅含"全部地点"占位）视为"无真实场馆清单"，改为数据驱动生成
    const hasRealVenues = allVenues.some(function(v) { return v.key && v.key !== 'all'; });
    if (!hasRealVenues) {
      // 未配置真实场馆清单时，从本城市真实活动汇总实际场馆名（e.venue）去重生成，
      // 保证新增城市也能自动拥有"地点"筛选，无需手工补 venuesByCity
      const seen = {};
      (app.globalData.exhibitions || []).forEach(function(e) {
        if ((e._cityKey || normalizeCity(e.city)) !== city) return;
        const v = e.venue;
        if (v && !seen[v]) seen[v] = { key: v, name: v };
      });
      allVenues = [{ key: 'all', name: '全部地点' }].concat(Object.keys(seen).map(function(k) { return seen[k]; }));
    }

    // 选择区县后，按区县过滤场馆列表，只显示该区县的场馆
    if (district && district !== 'all') {
      const districtVenues = {};
      // 从场馆信息中按 city + district 提取（用场馆名，兼容中文场馆名）
      (app.globalData.venues || []).forEach(function(v) {
        if (v.city === city && v.district === district && v.name) {
          districtVenues[v.name] = v.name;
        }
      });
      // 从活动数据中补充该区县的真实场馆
      (app.globalData.exhibitions || []).forEach(function(e) {
        if ((e._cityKey || normalizeCity(e.city)) === city && e.district === district && e.venue) {
          if (!districtVenues[e.venue]) districtVenues[e.venue] = e.venue;
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
    let filtered = getFilteredExhibitions(allExhibitions, filters);

    // 首屏/弱网安全网：当前时间筛选在某城市结果为 0，但该城市实际有活动（多为打包兜底日期偏旧
    // 或弱网仅加载到部分数据），则自动放宽到「全部」并提示，确保用户第一时间看到内容而非空白。
    let emptyHint = '';
    if (filtered.length === 0 && filters.time !== 'all') {
      const allOfCity = getFilteredExhibitions(allExhibitions, Object.assign({}, filters, { time: 'all' }));
      if (allOfCity.length > 0) {
        filtered = allOfCity;
        emptyHint = '该时段活动较少，已为你显示全部活动';
      }
    }

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
      loading: false,
      emptyHint: emptyHint
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

    // 城市置灰仅在“远程/完整数据已加载”后才生效；本地兜底阶段、或仅加载到「近期」子集
    // (isPartial) 时不置灰——否则加载途中某城在子集里恰好为 0 会被误置灰、无法点击。
    const isRemote = app.globalData.isRemoteData && !app.globalData.isPartial;
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
