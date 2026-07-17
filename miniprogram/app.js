// 本地数据作为离线兜底（打包时生成，相对较新）
const localExhibitions = require('./data/exhibitions.js');
const localVenues = require('./data/venues.js');
const { precomputeDerived } = require('./utils/helpers.js');

// 预计算离线兜底数据的派生字段（运行期更新后的数据也会在 applyExhibitions 里预计算）
precomputeDerived(localExhibitions);

// 远程数据地址（GitHub raw 直连）
// 小程序直接读取各城市分文件 exhibitions_{城市}.json —— 与网页版同源（网页只读分城市文件）。
// 新增城市只需在 filters.js 的 cities 数组加一项，取数与筛选 UI 同步生效，无需维护主文件。
const CITY_FILE_BASE = 'https://raw.githubusercontent.com/islon/goout/main/output/exhibitions_';
const REMOTE_VENUE_URL = 'https://raw.githubusercontent.com/islon/goout/main/output/venue_info.json';
// 城市列表：同时驱动筛选 UI 与取数（单一事实来源）
const { cities } = require('./data/filters.js');

// 缓存 key（v2：打包数据已扩为 10 城场馆，旧 v1 缓存需重新播种，故升版本号）
const CACHE_KEY = 'goout_exhibitions_cache_v2';
const CACHE_TIME_KEY = 'goout_exhibitions_cache_time_v2';
const VENUE_CACHE_KEY = 'goout_venues_cache_v2';
const VENUE_CACHE_TIME_KEY = 'goout_venues_cache_time_v2';

// 加时间戳，绕过 CDN 缓存
function getFreshUrl(base) {
  return base + '?t=' + Date.now();
}

// 把远程/缓存数据统一规整为数组：数组原样返回；对象(按值)转数组；其余返回 null
// 防止 GitHub raw 被拦截返回 HTML 字符串时，直接赋值字符串导致页面 .filter 崩溃白屏
function toArray(data) {
  if (Array.isArray(data)) return data;
  if (data && typeof data === 'object') return Object.values(data);
  return null;
}

// 判断已加载的数据集是否已覆盖全部城市（用于决定城市筛选器是否可信任“无数据则置灰”）
function datasetHasAllCities(arr) {
  if (!Array.isArray(arr) || !arr.length) return false;
  var present = {};
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] && arr[i].city) present[arr[i].city] = true;
  }
  return (cities || []).every(function(c) { return present[c.key]; });
}

// 拉取单个城市分文件，规整为数组；被墙/非数组时返回 null（不污染整体）
function fetchCityArray(key) {
  return new Promise(function(resolve) {
    wx.request({
      url: getFreshUrl(CITY_FILE_BASE + key + '.json'),
      method: 'GET',
      timeout: 15000,
      success: function(res) {
        var arr = toArray(res.data);
        if (res.statusCode === 200 && arr && arr.length > 0) {
          resolve(arr);
        } else {
          console.warn('[童行] 城市分文件不可用:', key, res.statusCode);
          resolve(null);
        }
      },
      fail: function(err) {
        console.warn('[童行] 城市分文件请求失败:', key, (err && err.errMsg) || '');
        resolve(null);
      }
    });
  });
}

// 并行拉取所有城市分文件并合并为统一数组；任一城市失败不影响其他城市
function fetchAllExhibitions() {
  var promises = (cities || []).map(function(c) { return fetchCityArray(c.key); });
  return Promise.all(promises).then(function(lists) {
    var merged = [];
    lists.forEach(function(arr) {
      if (arr && arr.length > 0) merged = merged.concat(arr);
    });
    return merged;
  });
}

App({
  globalData: {
    cityFilter: 'shenzhen',
    timeFilter: 'upcoming',
    typeFilter: 'all',
    districtFilter: 'all',
    sourceFilter: 'all',
    feeFilter: 'all',
    familyFilter: 'family',
    searchQuery: '',
    exhibitions: localExhibitions,
    venues: localVenues,
    venueMap: {},
    dataReady: false,
    isRemoteData: false,
    lastUpdateTime: null  // 记录最近一次成功更新时间
  },

  onLaunch() {
    console.log('[童行] 启动中...');

    // 1. 构建场馆映射（基于当前 venues 数据）
    this.buildVenueMap();

    // 2. 首次启动：将打包数据写入本地缓存作为基线
    //    这样即使从未联网，后续启动也能从缓存读取较新的数据
    this.seedCacheIfNeeded();

    // 3. 优先从本地缓存加载（无论是否过期，保证即时渲染）
    const hasCache = this.loadFromCache();

    if (hasCache) {
      console.log('[童行] 从本地缓存加载数据');
    } else {
      console.log('[童行] 使用打包的离线数据');
    }

    // 4. 标记数据就绪 → 页面可以立即渲染
    this.globalData.dataReady = true;
    this.notifyReady();

    // 5. 后台静默拉取最新数据（不阻塞界面）
    this.silentUpdateAll();

    // 6. 检测小程序新版本（真机 / 体验版 / 正式版生效）
    this.checkForUpdate();
  },

  // ========== 缓存种子：首次启动写入打包数据 ==========

  seedCacheIfNeeded() {
    try {
      // 活动数据
      if (!wx.getStorageSync(CACHE_TIME_KEY)) {
        wx.setStorageSync(CACHE_KEY, localExhibitions);
        wx.setStorageSync(CACHE_TIME_KEY, Date.now());
        console.log('[童行] 已将', localExhibitions.length, '条活动数据写入缓存基线');
      }
      // 场馆数据
      if (!wx.getStorageSync(VENUE_CACHE_TIME_KEY)) {
        wx.setStorageSync(VENUE_CACHE_KEY, localVenues);
        wx.setStorageSync(VENUE_CACHE_TIME_KEY, Date.now());
        console.log('[童行] 已将', localVenues.length, '条场馆数据写入缓存基线');
      }
    } catch (e) {
      console.warn('[童行] 写入缓存基线失败', e);
    }
  },

  // ========== 从缓存加载 ==========

  loadFromCache() {
    var loadedAny = false;

    // 活动数据
    var cached = toArray(wx.getStorageSync(CACHE_KEY));
    if (cached && cached.length > 0) {
      precomputeDerived(cached); // 旧缓存可能未含派生字段，补齐以保证筛选 O(1)
      this.globalData.exhibitions = cached;
      // 若缓存已是完整 10 城数据（来自此前远程），则视为可信数据源，城市筛选器可正常置灰
      if (datasetHasAllCities(cached)) this.globalData.isRemoteData = true;
      loadedAny = true;
      var ct = wx.getStorageSync(CACHE_TIME_KEY);
      if (ct) {
        this.globalData.lastUpdateTime = new Date(ct).toLocaleString();
      }
    }

    // 场馆数据
    var vCached = toArray(wx.getStorageSync(VENUE_CACHE_KEY));
    if (vCached && vCached.length > 0) {
      this.globalData.venues = vCached;
      this.buildVenueMap();
      loadedAny = true;
    }

    return loadedAny;
  },

  // ========== 后台静默更新 ==========
  // 短 TTL：缓存较新（<5 分钟）时跳过请求，避免每次进 App 都发 10 个分城市请求浪费流量。
  // 用户主动下拉/点刷新（forceRefresh）不受影响，始终拉最新。
  SILENT_TTL_MS: 5 * 60 * 1000,

  silentUpdateAll() {
    var cacheTime = wx.getStorageSync(CACHE_TIME_KEY) || 0;
    if (cacheTime && (Date.now() - cacheTime) < this.SILENT_TTL_MS) {
      console.log('[童行] 缓存较新(<5分钟)，跳过静默更新');
      return;
    }
    this.silentUpdateExhibitions();
    this.silentUpdateVenues();
  },

  // ========== 统一写入活动数据（预计算 + 赋值 + 写缓存）==========
  // 返回是否成功写入（用于决定后续是否通知页面）
  applyExhibitions(merged) {
    if (!merged || merged.length === 0) return false;
    precomputeDerived(merged); // 一次性算好派生字段，后续筛选/渲染均 O(1)
    this.globalData.exhibitions = merged;
    this.globalData.isRemoteData = true;
    var now = Date.now();
    this.globalData.lastUpdateTime = new Date(now).toLocaleString();
    try {
      wx.setStorageSync(CACHE_KEY, merged);
      wx.setStorageSync(CACHE_TIME_KEY, now);
    } catch (e) {}
    return true;
  },

  // ========== 统一写入场馆数据 ==========
  applyVenues(arr) {
    if (!arr || arr.length === 0) return false;
    precomputeDerived(arr);
    this.globalData.venues = arr;
    this.buildVenueMap();
    try {
      wx.setStorageSync(VENUE_CACHE_KEY, arr);
      wx.setStorageSync(VENUE_CACHE_TIME_KEY, Date.now());
    } catch (e) {}
    return true;
  },

  silentUpdateExhibitions() {
    var self = this;
    fetchAllExhibitions().then(function(merged) {
      if (self.applyExhibitions(merged)) {
        console.log('[童行] 活动数据已更新至最新，共', merged.length, '条');
        // 通知页面刷新（如果页面已经显示旧数据）
        self.notifyDataUpdated();
      } else {
        console.warn('[童行] 远程活动数据全部不可用，继续使用本地缓存/打包数据');
      }
    });
  },

  silentUpdateVenues() {
    var self = this;
    wx.request({
      url: getFreshUrl(REMOTE_VENUE_URL),
      method: 'GET',
      timeout: 15000,
      success: function(res) {
        var arr = toArray(res.data);
        if (res.statusCode === 200 && self.applyVenues(arr)) {
          console.log('[童行] 场馆数据已更新至最新，共', arr.length, '条');
        } else {
          console.warn('[童行] 远程场馆数据异常(非数组或为空)，保持本地数据', res.statusCode);
        }
      },
      fail: function() {}
    });
  },

  // ========== 手动强制刷新（下拉刷新 / 点刷新按钮调用）==========

  forceRefresh(callback) {
    var self = this;
    console.log('[童行] 强制刷新中...');
    fetchAllExhibitions().then(function(merged) {
      var ok = self.applyExhibitions(merged);
      if (ok) console.log('[童行] 强制刷新完成，共', merged.length, '条');
      if (callback) callback(ok);
    });

    // 同时刷新场馆
    wx.request({
      url: getFreshUrl(REMOTE_VENUE_URL),
      method: 'GET',
      timeout: 15000,
      success: function(res) {
        var arr = toArray(res.data);
        if (res.statusCode === 200 && self.applyVenues(arr)) {
          console.log('[童行] 场馆数据已更新至最新，共', arr.length, '条');
        }
      },
      fail: function() {}
    });
  },

  // ========== 场馆映射 ==========

  buildVenueMap() {
    var map = {};
    var venues = this.globalData.venues || [];
    for (var i = 0; i < venues.length; i++) {
      var v = venues[i];
      if (v && v.name) {
        map[v.name] = v;
      }
    }
    this.globalData.venueMap = map;
  },

  // ========== 回调通知系统 ==========

  readyCallbacks: [],
  dataUpdatedCallbacks: [],

  onReady(callback) {
    if (this.globalData.dataReady) {
      callback();
    } else {
      this.readyCallbacks.push(callback);
    }
  },

  notifyReady() {
    var cbs = this.readyCallbacks;
    this.readyCallbacks = [];
    cbs.forEach(function(cb) { cb(); });
  },

  // 静默更新完成后通知页面刷新
  onDataUpdated(callback) {
    this.dataUpdatedCallbacks.push(callback);
  },

  notifyDataUpdated() {
    var cbs = this.dataUpdatedCallbacks;
    this.dataUpdatedCallbacks = [];
    cbs.forEach(function(cb) { cb(); });
  },

  // ========== 新版本检测 ==========
  checkForUpdate() {
    if (typeof wx.getUpdateManager !== 'function') return; // 基础库过低兼容
    var um = wx.getUpdateManager();
    um.onUpdateReady(function() {
      wx.showModal({
        title: '发现新版本',
        content: '童行已为你准备好新版本，重启后即可使用最新功能与活动数据。',
        confirmText: '立即重启',
        cancelText: '稍后再说',
        success: function(res) {
          if (res.confirm) um.applyUpdate();
        }
      });
    });
    um.onUpdateFailed(function() {
      wx.showToast({ title: '新版本下载失败，请删除小程序后重新打开', icon: 'none' });
    });
  }
});
