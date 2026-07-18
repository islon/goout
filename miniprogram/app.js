// 本地数据作为离线兜底（打包时生成，相对较新）
const localExhibitions = require('./data/exhibitions.js');
const localVenues = require('./data/venues.js');
const { precomputeDerived } = require('./utils/helpers.js');

// 预计算离线兜底数据的派生字段（运行期更新后的数据也会在 applyExhibitions 里预计算）
precomputeDerived(localExhibitions);

// 远程数据地址：多数据源容灾（见下方 DATA_SOURCES）。
// 小程序直接读取各城市分文件 exhibitions_{城市}.json —— 与网页版同源（网页只读分城市文件）。
// 新增城市只需在 filters.js 的 cities 数组加一项，取数与筛选 UI 同步生效，无需维护主文件。
// 近期活动小文件（每城最早未结束前 80 条，约 800 条）：首屏优先拉取，单请求、体积极小。
// 城市清单：运行时拉取，新增城市无需重新发布小程序版本。
// 场馆库：2964 个真实场馆。
// 以上文件均通过 DATA_SOURCES 多源顺序拉取（jsDelivr 镜像优先、raw.githubusercontent 兜底），
// 彻底规避“单一域名被墙导致全量拉不到、卡在近期子集”的问题。
// 打包内城市清单：仅作离线兜底（首启/网络不可达时用）
const { cities: bundledCities } = require('./data/filters.js');
// 运行期生效的城市清单（模块级，驱动取数）：默认用打包兜底，成功拉取 cities.json 后覆盖
var activeCities = bundledCities;

// 多数据源容灾：国内优先 jsDelivr 镜像，raw.githubusercontent 兜底。
// 两者被墙相互独立——任一可达即可加载，根治“单源被墙导致全量拉不到/卡在近期子集”的问题。
const DATA_SOURCES = [
  { base: 'https://cdn.jsdelivr.net/gh/islon/goout@main/', bust: false },
  { base: 'https://raw.githubusercontent.com/islon/goout/main/', bust: true }
];

// 缓存 key（v3：数据已净化移除合成条目、场馆库扩充至2964个，旧缓存需重新播种）
const CACHE_KEY = 'goout_exhibitions_cache_v3';
const CACHE_TIME_KEY = 'goout_exhibitions_cache_time_v3';
const VENUE_CACHE_KEY = 'goout_venues_cache_v3';
const VENUE_CACHE_TIME_KEY = 'goout_venues_cache_time_v3';
// 小程序代码版本标记：当其变化时（升级后），onLaunch 会强制拉取最新数据，不受 5 分钟 TTL 节流影响。
const APP_VERSION = '2026.07.18.6';

// 带重试的 wx.request 封装：GitHub raw 在中国大陆常被拦截/超时，
// 这里做指数退避重试（默认 3 次，间隔 0.7s / 1.4s / 2.1s），显著提升首屏拉取成功率。
// 无论成功失败都 resolve（与原有 fetchXxx 的容错语义一致）；最终失败返回 {statusCode:0,data:null}
function requestWithRetry(url, options) {
  options = options || {};
  var maxRetries = (options.maxRetries != null) ? options.maxRetries : 3;
  var timeout = options.timeout || 15000;
  return new Promise(function(resolve) {
    var attempt = 0;
    function tryOnce() {
      attempt++;
      wx.request({
        url: url,
        method: 'GET',
        timeout: timeout,
        success: function(res) {
          // 被墙时常返回 HTML 字符串（statusCode 200 但 data 以 < 开头），需重试
          var data = res.data;
          var blocked = (typeof data === 'string') && data.charAt(0) !== '[' && data.charAt(0) !== '{';
          if (res.statusCode === 200 && !blocked) {
            resolve(res);
          } else if (attempt < maxRetries) {
            console.warn('[童行] 数据未就绪，第' + attempt + '次重试:', url);
            setTimeout(tryOnce, 700 * attempt);
          } else {
            resolve(res); // 交由调用方按 toArray 处理（被墙字符串 → null）
          }
        },
        fail: function(err) {
          if (attempt < maxRetries) {
            console.warn('[童行] 请求失败，第' + attempt + '次重试:', url, (err && err.errMsg) || '');
            setTimeout(tryOnce, 700 * attempt);
          } else {
            resolve({ statusCode: 0, data: null, __err: err });
          }
        }
      });
    }
    tryOnce();
  });
}

// 多数据源顺序容灾拉取 relPath（相对仓库根路径）：依次尝试 DATA_SOURCES 中每个源，
// 每个源内部由 requestWithRetry 做指数退避重试；全部失败 resolve(null)。
// 任一源返回有效 JSON 数组即胜出，彻底规避“单一域名被墙则全盘拉取失败”。
function fetchJsonFromSources(relPath, opts) {
  opts = opts || {};
  return new Promise(function(resolve) {
    var idx = 0;
    function tryNext() {
      if (idx >= DATA_SOURCES.length) { resolve(null); return; }
      var s = DATA_SOURCES[idx++];
      var url = s.base + relPath + (s.bust ? ('?t=' + Date.now()) : '');
      requestWithRetry(url, opts).then(function(res) {
        var arr = toArray(res && res.data);
        if (res && res.statusCode === 200 && arr && arr.length > 0) {
          resolve(res);
        } else {
          console.warn('[童行] 数据源不可达，切换下一个:', (s.base || '').split('/')[2], (res && res.statusCode));
          tryNext();
        }
      });
    }
    tryNext();
  });
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
  return (activeCities || []).every(function(c) { return present[c.key]; });
}

// 校验 cities.json 结构：数组且每项含 key/name
function isValidCities(arr) {
  return Array.isArray(arr) && arr.length > 0 && arr.every(function(c) {
    return c && typeof c.key === 'string' && c.key && typeof c.name === 'string' && c.name;
  });
}

// 比较两份城市清单的 key 集合是否一致（用于判断是否新增/删减了城市）
function sameCityKeys(a, b) {
  var ka = (a || []).map(function(c) { return c.key; }).sort().join(',');
  var kb = (b || []).map(function(c) { return c.key; }).sort().join(',');
  return ka === kb;
}

// 运行时拉取城市清单 cities.json；成功且结构合法则更新模块级 activeCities 并返回该数组，否则返回 null（保持兜底）
function fetchCities() {
  return fetchJsonFromSources('output/cities.json', { timeout: 15000, maxRetries: 2 }).then(function(res) {
    if (!res) {
      console.warn('[童行] cities.json 全部数据源不可用，沿用打包城市清单');
      return null;
    }
    var arr = toArray(res.data);
    if (isValidCities(arr)) {
      activeCities = arr;
      return arr;
    }
    console.warn('[童行] cities.json 结构异常，沿用打包城市清单', res.statusCode);
    return null;
  });
}

// 拉取单个城市分文件，规整为数组；被墙/非数组时返回 null（不污染整体）
function fetchCityArray(key) {
  return fetchJsonFromSources('output/exhibitions_' + key + '.json', { timeout: 15000, maxRetries: 2 }).then(function(res) {
    if (!res) {
      console.warn('[童行] 城市分文件全部数据源不可用:', key);
      return null;
    }
    var arr = toArray(res.data);
    if (arr && arr.length > 0) return arr;
    console.warn('[童行] 城市分文件为空:', key, res.statusCode);
    return null;
  });
}

// 拉取「近期活动」小文件（首屏优先，单请求、体积小）；被墙/非数组时返回 null
function fetchRecent() {
  return fetchJsonFromSources('output/exhibitions_recent.json', { timeout: 15000, maxRetries: 2 }).then(function(res) {
    if (!res) {
      console.warn('[童行] 近期活动文件全部数据源不可用');
      return null;
    }
    var arr = toArray(res.data);
    if (arr && arr.length > 0) return arr;
    console.warn('[童行] 近期活动文件为空', res.statusCode);
    return null;
  });
}

// 并行拉取所有城市分文件并合并为统一数组；任一城市失败不影响其他城市
function fetchAllExhibitions() {
  var promises = (activeCities || []).map(function(c) { return fetchCityArray(c.key); });
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
    familyFilter: 'all',
    searchQuery: '',
    exhibitions: localExhibitions,
    venues: localVenues,
    venueMap: {},
    cities: bundledCities,  // 运行期城市清单：默认打包兜底，拉取 cities.json 后覆盖（各页面 tab 据此渲染）
    dataReady: false,
    isRemoteData: false,
    isPartial: false,     // 当前 exhibitions 是否仅为「近期活动」子集（全量后台拉取完成后置 false）
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

    // 5. 检测是否“首次启动(刚播种打包基线)”或“升级后(版本号变化)”：
    //    这两种情况应强制拉取最新数据，忽略 5 分钟 TTL 节流；普通重复进入仍走节流。
    try {
      var lastVer = wx.getStorageSync('goout_app_version');
      if (!lastVer || lastVer !== APP_VERSION) {
        this._versionChanged = true;
        wx.setStorageSync('goout_app_version', APP_VERSION);
        console.log('[童行] 检测到版本变化/首次使用，将强制拉取最新数据');
      }
    } catch (e) {}

    // 6. 后台静默拉取最新数据（不阻塞界面）
    this.silentUpdateAll();

    // 6. 检测小程序新版本（真机 / 体验版 / 正式版生效）
    this.checkForUpdate();
  },

  // ========== 缓存种子：首次启动写入打包数据 ==========

  seedCacheIfNeeded() {
    try {
      // 活动数据
      if (!wx.getStorageSync(CACHE_TIME_KEY)) {
        // 标记“本次启动刚播种打包基线”——首次进入应强制拉最新，而非沿用旧基线后跳过静默更新
        this._seededThisLaunch = true;
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
    var self = this;
    // 先拉取城市清单：新增城市能在不发版本的情况下出现在各页面 tab
    fetchCities().then(function(arr) {
      var changed = false;
      if (arr) {
        changed = !sameCityKeys(self.globalData.cities, arr);
        self.globalData.cities = arr;
        if (changed) {
          console.log('[童行] 城市清单已更新，共', arr.length, '城');
          self.notifyCitiesUpdated();
        }
      }
      // 城市清单有增减时，或“首次启动/升级后”时，即便缓存较新也强制拉数据；否则按 TTL 节流
      var cacheTime = wx.getStorageSync(CACHE_TIME_KEY) || 0;
      var fresh = cacheTime && (Date.now() - cacheTime) < self.SILENT_TTL_MS;
      var force = self._seededThisLaunch || self._versionChanged;
      if (fresh && !changed && !force) {
        console.log('[童行] 缓存较新(<5分钟)且城市清单无变化，跳过静默更新');
        return;
      }
      self.silentUpdateExhibitions();
      self.silentUpdateVenues();
    });
  },

  // ========== 统一写入活动数据（预计算 + 赋值 + 写缓存）==========
  // isPartial=true 表示本次写入的仅是「近期活动」子集（首屏优先），全量拉到后置 false
  // 返回是否成功写入（用于决定后续是否通知页面）
  applyExhibitions(merged, isPartial) {
    if (!merged || merged.length === 0) return false;
    precomputeDerived(merged); // 一次性算好派生字段，后续筛选/渲染均 O(1)
    this.globalData.exhibitions = merged;
    this.globalData.isRemoteData = true;
    this.globalData.isPartial = !!isPartial;
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
    // 1) 先拉「近期活动」小文件（约 800 条、单请求），秒出首屏
    fetchRecent().then(function(recent) {
      if (recent && recent.length) {
        self.applyExhibitions(recent, true);
        console.log('[童行] 近期活动已加载（首屏），共', recent.length, '条');
        self.notifyDataUpdated();
      }
      // 2) 后台静默拉取全量分城市文件；拉到后刷新为完整数据（不影响首屏已渲染）
      fetchAllExhibitions().then(function(merged) {
        if (self.applyExhibitions(merged, false)) {
          console.log('[童行] 活动数据已更新至最新，共', merged.length, '条');
          self.notifyDataUpdated();
        } else {
          console.warn('[童行] 远程全量活动数据暂不可用，8s 后自动重试补全');
          // 自愈：瞬时被墙/抖动时，稍后重试一次全量（不重复拉近期），避免长期卡在近期子集
          setTimeout(function() { self.retryFullExhibitions(); }, 8000);
        }
      });
    });
  },

  // 仅重试全量分城市文件（用于 silentUpdateExhibitions 自愈）
  retryFullExhibitions() {
    var self = this;
    fetchAllExhibitions().then(function(merged) {
      if (self.applyExhibitions(merged, false)) {
        console.log('[童行] 全量重试成功，活动已补全，共', merged.length, '条');
        self.notifyDataUpdated();
      } else {
        console.warn('[童行] 全量重试仍不可用，保持近期/缓存数据');
      }
    });
  },

  silentUpdateVenues() {
    var self = this;
    fetchJsonFromSources('output/venue_info.json', { timeout: 15000, maxRetries: 2 }).then(function(res) {
      if (!res) {
        console.warn('[童行] 场馆数据全部数据源不可用，保持本地数据');
        return;
      }
      var arr = toArray(res.data);
      if (self.applyVenues(arr)) {
        console.log('[童行] 场馆数据已更新至最新，共', arr.length, '条');
      } else {
        console.warn('[童行] 远程场馆数据异常(非数组或为空)，保持本地数据', res.statusCode);
      }
    });
  },

  // ========== 手动强制刷新（下拉刷新 / 点刷新按钮调用）==========

  forceRefresh(callback) {
    var self = this;
    console.log('[童行] 强制刷新中...');
    // 先刷新城市清单，再按最新清单拉活动（保证新增城市立即可见且有数据）
    fetchCities().then(function(arr) {
      if (arr && !sameCityKeys(self.globalData.cities, arr)) {
        self.globalData.cities = arr;
        self.notifyCitiesUpdated();
        console.log('[童行] 城市清单已更新，共', arr.length, '城');
      }
      // 先秒出近期活动首屏
      fetchRecent().then(function(recent) {
        if (recent && recent.length) {
          self.applyExhibitions(recent, true);
          self.notifyDataUpdated();
        }
        // 再拉全量分城市文件
        fetchAllExhibitions().then(function(merged) {
          var ok = self.applyExhibitions(merged, false);
          if (ok) console.log('[童行] 强制刷新完成，共', merged.length, '条');
          if (callback) callback(ok);
        });
      });
    });

    // 同时刷新场馆（多数据源容灾）
    fetchJsonFromSources('output/venue_info.json', { timeout: 15000, maxRetries: 2 }).then(function(res) {
      if (!res) {
        console.warn('[童行] 场馆数据全部数据源不可用，保持本地数据');
        return;
      }
      var arr = toArray(res.data);
      if (self.applyVenues(arr)) {
        console.log('[童行] 场馆数据已更新至最新，共', arr.length, '条');
      }
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
  citiesUpdatedCallbacks: [],

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

  // 城市清单更新后通知页面刷新 tab（持久订阅：页面 onLoad 注册一次，可被多次强制刷新触发）
  onCitiesUpdated(callback) {
    this.citiesUpdatedCallbacks.push(callback);
  },

  notifyCitiesUpdated() {
    var cities = this.globalData.cities;
    this.citiesUpdatedCallbacks.forEach(function(cb) {
      try { cb(cities); } catch (e) {}
    });
  },

  // 供页面读取当前生效的城市清单（运行时优先，回退打包兜底）
  getCities() {
    var g = this.globalData && this.globalData.cities;
    return (Array.isArray(g) && g.length) ? g : bundledCities;
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
