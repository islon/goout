// 童行小程序 - 场馆指南列表页
// 打包内城市清单仅作离线兜底；运行期优先用 app.getCities()（来自远程 cities.json），
// 这样云侧新增城市后无需重新发布小程序版本即可出现在城市 tab。
const { cities: bundledCities, districtPopulation } = require('../../data/filters.js');
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

// 由城市清单构建城市 tab（不含“全部”）
function buildCityTabs(list) {
  return (list || []).map(function(c) { return { key: c.key, name: c.name }; });
}

// 模块级可变映射：applyFilters 用它把 city key 转显示名；loadData 时会随运行期清单重建
var cityNameMap = buildCityNameMap(getRuntimeCities());

const FILTER_STORAGE_KEY = 'goout_venue_filter_state';
const FILTER_KEYS = ['cityFilter', 'districtFilter', 'typeFilter', 'searchQuery'];

// 类型筛选超过该数量时，默认折叠成一行并出现「展开/收起」按钮
const TYPE_COLLAPSE_THRESHOLD = 8;

Page({
  data: {
    cityFilter: 'shenzhen',
    districtFilter: 'all',
    typeFilter: 'all',
    searchQuery: '',
    cities: [],
    districts: [],
    types: [],
    venues: [],
    activityCounts: {},
    cityNameMap: cityNameMap,
    typeExpanded: false,
    typeCollapseThreshold: TYPE_COLLAPSE_THRESHOLD,
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
          if (saved[k] !== undefined && saved[k] !== null) {
            if (k === 'cityFilter' && saved[k] === 'all') {
              patch[k] = 'shenzhen';
            } else {
              patch[k] = saved[k];
            }
          }
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

    // 判断是否仍在使用打包内兜底（CDN 全量场馆尚未到达）
    const bundled = Array.isArray(app.globalData._bundledVenues) ? app.globalData._bundledVenues : [];
    const stillLoadingBundled = allVenues.length <= bundled.length && app.globalData.isLoading;

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

    const patch = {
      cities: cityTabs,
      cityNameMap: cityNameMap,
      types: types,
      activityCounts: activityCounts,
      loading: stillLoadingBundled  // CDN 未到达时保持 loading 态，避免显示"没有找到"
    };

    this.setData(patch, () => {
      this.rebuildDistricts();
      this.applyFilters();
      // onDataUpdated 是一次性的，每次统计后重新登记自身，使场馆补齐/刷新后本页实时更新
      if (app && typeof app.onDataUpdated === 'function') {
        const self = this;
        app.onDataUpdated(function() { self.loadData(); });
      }
    });
  },

  applyFilters() {
    const rawVenues = Array.isArray(app.globalData.venues) ? app.globalData.venues : [];
    // 兜底：若 globalData 尚未加载（CDN 未返回），用打包内离线兜底保证不白屏
    const allVenues = rawVenues.length > 0 ? rawVenues : (Array.isArray(app.globalData._bundledVenues) ? app.globalData._bundledVenues : []);
    const cityFilter = this.data.cityFilter;
    const districtFilter = this.data.districtFilter;
    const typeFilter = this.data.typeFilter;
    const query = this.data.searchQuery.toLowerCase().trim();

    // 城市匹配：兼容英文key / 中文名（防御数据源格式不一致）
    function cityMatch(v) {
      return v.city === cityFilter
        || v.city === (cityNameMap[cityFilter] || cityFilter);
    }

    const filtered = allVenues.filter(v => {
      if (!cityMatch(v)) return false;
      if (districtFilter !== 'all' && v.district !== districtFilter) return false;
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
      }),
      // 数据已到位后关闭加载态（避免全局数据就绪后仍卡在loading）
      loading: false
    });
  },

  onCityTap(e) {
    const key = e.currentTarget.dataset.key;
    // 切换城市时重置区县筛选（区县仅在该城市内有意义）
    this.setData({ cityFilter: key, districtFilter: 'all' }, () => {
      this.rebuildDistricts();
      this.applyFilters();
    });
    this.saveFilters();
  },

  // 根据当前选定城市，从场馆数据动态汇总实际存在的区县（不含空/“其他”）
  rebuildDistricts() {
    const allVenues = Array.isArray(app.globalData.venues) ? app.globalData.venues : [];
    const city = this.data.cityFilter;
    const found = {};
    for (let i = 0; i < allVenues.length; i++) {
      const v = allVenues[i];
      if (v.city !== city) continue;
      const d = v.district;
      if (d && d !== '其他') found[d] = true;
    }
    const districtKeys = Object.keys(found).sort(function(a, b) {
      return (districtPopulation[b] || 0) - (districtPopulation[a] || 0);
    });
    const districts = ['全部区县'].concat(districtKeys);
    this.setData({ districts: districts });
  },

  onDistrictTap(e) {
    this.setData({ districtFilter: e.currentTarget.dataset.key }, () => this.applyFilters());
    this.saveFilters();
  },

  onTypeTap(e) {
    this.setData({ typeFilter: e.currentTarget.dataset.key }, () => this.applyFilters());
    this.saveFilters();
  },

  onToggleType() {
    this.setData({ typeExpanded: !this.data.typeExpanded });
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
