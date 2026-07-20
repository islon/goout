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
const CACHE_PARTIAL_KEY = 'goout_exhibitions_cache_partial_v3'; // true=缓存仅近期子集(残缺)，下次启动应强制补齐
const VENUE_CACHE_KEY = 'goout_venues_cache_v3';
const VENUE_CACHE_TIME_KEY = 'goout_venues_cache_time_v3';
const VENUE_PARTIAL_KEY = 'goout_venues_cache_partial_v3'; // true=场馆缓存残缺(部分城市缺失)，下次启动应强制补齐
// 云端数据版本标记：CI 生成的 data_meta.json 里的 version(数据内容哈希)。本地存上次成功拉到的版本，
// 下次启动先比版本——相同则说明云侧数据无变化，直接复用本地缓存、不再下载几 MB 的分城市大文件。
const DATA_META_VERSION_KEY = 'goout_data_meta_version_v1';
// 小程序代码版本标记：当其变化时（升级后），onLaunch 会强制拉取最新数据，不受 5 分钟 TTL 节流影响。
const APP_VERSION = '2026.07.18.16';

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

// 拉取云端数据版本清单 data_meta.json（极小文件，~200B）：含 version(数据内容哈希) + updatedAt + 活动/场馆计数。
// 用于「云侧数据无更新则不下载」的精准判定，避免每次进 App 都重复下载几 MB 分城市大文件。
function fetchDataMeta() {
  return fetchJsonFromSources('output/data_meta.json', { timeout: 10000, maxRetries: 2 }).then(function(res) {
    var o = (res && res.data) ? res.data : null;
    if (o && typeof o === 'object' && o.version) return o;
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

// 拉取「近期活动」小文件（首屏优先·Tier1：离当前时间最近、即将举办的活动），单请求、体积小
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

// 拉取「历史活动」小文件（Tier3：已结束的活动），优先级最低、最后再拉取，不挤占首屏带宽。
// 历史活动可能为空（都还是未来活动），此时返回 null，不影响“已完整加载”判定。
function fetchPast() {
  return fetchJsonFromSources('output/exhibitions_past.json', { timeout: 15000, maxRetries: 2 }).then(function(res) {
    if (!res) return null;
    var arr = toArray(res.data);
    return (arr && arr.length > 0) ? arr : null;
  });
}

// 并发受限的 Promise pool：限制同时进行的请求数，降低 jsDelivr 对 10 个并行请求的限流概率
function poolAll(items, limit, worker) {
  var i = 0;
  var results = new Array(items.length);
  return new Promise(function(resolve) {
    function next() {
      if (i >= items.length) { resolve(results); return; }
      var idx = i++;
      Promise.resolve(worker(items[idx]))
        .then(function(r) { results[idx] = r; })
        .catch(function() { results[idx] = null; })
        .then(next);
    }
    var start = Math.min(limit, items.length);
    for (var k = 0; k < start; k++) next();
  });
}

// 拉取一批城市分文件，返回 { merged: 合并数组, failed: 失败的城市 key 列表 }
// 与 fetchAllExhibitions 的区别：明确报告哪些城市没取到，便于后续「补齐」而非默默丢弃。
function fetchCityBatch(cities) {
  return poolAll(cities, 3, function(c) { return fetchCityArray(c.key); }).then(function(lists) {
    var merged = [];
    var failed = [];
    lists.forEach(function(arr, i) {
      if (arr && arr.length > 0) merged = merged.concat(arr);
      else failed.push(cities[i].key);
    });
    return { merged: merged, failed: failed };
  });
}

// 并行拉取所有城市分文件并合并；返回 { merged, failed }（failed 为空表示全部取到）
function fetchAllExhibitions() {
  return fetchCityBatch(activeCities || []);
}

// ========== 场馆：与活动完全对称的分城市拉取机制 ==========
// 此前场馆只有一个 861KB 的 venue_info.json 单文件，弱网下容易拉取失败，
// 导致用户端卡在裁剪兜底(481个)。改为分城市小文件后：并行拉取 + 多源容灾 +
// 缺失城市自动补齐，与活动加载逻辑一致，场馆指南可稳定展示全量(~2964个)。

// 拉取单个城市的场馆分文件（output/venue_info_{key}.json）
// 注：这批分城市文件是新建的，jsDelivr 首次命中为冷缓存，可能较慢/偶发超时，
// 故拉高超时与重试次数，降低弱网/冷缓存导致的整城失败概率。
function fetchVenueArray(cityKey) {
  return fetchJsonFromSources('output/venue_info_' + cityKey + '.json', { timeout: 25000, maxRetries: 3 }).then(function(res) {
    if (!res) return null;
    var arr = toArray(res.data);
    return (arr && arr.length > 0) ? arr : null;
  });
}

// 拉取一批城市场馆分文件，返回 { merged, failed }
function fetchVenueBatch(cities) {
  return poolAll(cities, 3, function(c) { return fetchVenueArray(c.key); }).then(function(lists) {
    var merged = [];
    var failed = [];
    lists.forEach(function(arr, i) {
      if (arr && arr.length > 0) merged = merged.concat(arr);
      else failed.push(cities[i].key);
    });
    return { merged: merged, failed: failed };
  });
}

// 并行拉取所有城市场馆分文件并合并；返回 { merged, failed }
function fetchAllVenues() {
  return fetchVenueBatch(activeCities || []);
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
    venuesPartial: false, // 当前 venues 是否仅部分城市取到（补齐完成前为 true）
    lastUpdateTime: null, // 记录最近一次成功更新时间
    appVersion: APP_VERSION,   // 小程序版本号（供关于页展示）
    buildDate: '2026-07-18',   // 构建/发布日期（供关于页展示）
    isLoading: false           // 是否正在后台刷新/下载数据（驱动首页刷新图标旋转动画）
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
        // 清掉可能过期的场馆缓存（避免旧裁剪兜底 481 被当成完整数据沿用），升级后重新拉全量分城市场馆
        try {
          wx.removeStorageSync(VENUE_CACHE_KEY);
          wx.removeStorageSync(VENUE_CACHE_TIME_KEY);
          wx.removeStorageSync(VENUE_PARTIAL_KEY);
        } catch (e) {}
        console.log('[童行] 检测到版本变化/首次使用，将强制拉取最新数据');
      }
    } catch (e) {}

    // 5.5 开发者工具与真机走同一套远程拉取逻辑（不内置全量包：731KB 超主包 2MB 限制，
    //     且 packOptions.ignore 会让开发者工具模拟器也加载不到该文件，本地分支不可靠已移除）。
    //     开发者工具若因本机企业 SSL 代理(aTrust)无法联网，场馆会停在打包兜底，属环境限制，请以真机验证全量。

    // 6. 后台静默拉取最新数据（不阻塞界面）
    this.silentUpdateAll();

    // 6. 检测小程序新版本（真机 / 体验版 / 正式版生效）
    this.checkForUpdate();

    // 7. 场馆数保险：启动数秒后若仍有城市场馆未加载（按城市覆盖判断，非数量阈值），
    //    触发缺失城市补齐重试，覆盖分城市请求慢/部分卡住的时序边界，避免长期停在打包兜底(378)。
    var self = this;
    setTimeout(function() {
      // 用「是否所有城市都已加载」判断，而非数量阈值；避免首屏渲染(打包378)被误判为偏少去拉 861KB 大单文件
      if (!self._allVenueCitiesLoaded()) {
        var missing = self._missingVenueCities();
        console.warn('[童行] 启动后仍有城市场馆未加载(' + missing.join(',') + ')，触发补齐');
        self._fillMissingVenueCities(missing, 6);
      }
    }, 5000);
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
      // 还原缓存的「是否残缺」标记：残缺缓存应在本次启动强制补齐，而非当作完整数据沿用
      this.globalData.isPartial = !!wx.getStorageSync(CACHE_PARTIAL_KEY);
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
    // 还原场馆「是否残缺」标记（与活动同理，残缺缓存应在本次启动强制补齐）
    this.globalData.venuesPartial = !!wx.getStorageSync(VENUE_PARTIAL_KEY);

    return loadedAny;
  },

  // ========== 后台静默更新 ==========
  // 短 TTL：缓存较新（<5 分钟）时跳过请求，避免每次进 App 都发 10 个分城市请求浪费流量。
  // 用户主动下拉/点刷新（forceRefresh）不受影响，始终拉最新。
  SILENT_TTL_MS: 5 * 60 * 1000,

  // 拉取云端数据版本清单并与本地比对：返回 { meta, changed }
  // changed=true 表示云侧数据相对本地有变化（或拿不到版本信息，按“需下载”处理，等价于旧 TTL 行为）
  _checkMeta() {
    var self = this;
    return fetchDataMeta().then(function(meta) {
      var cached = wx.getStorageSync(DATA_META_VERSION_KEY) || '';
      var changed = !meta || !meta.version || meta.version !== cached;
      return { meta: meta, changed: changed };
    });
  },

  silentUpdateAll() {
    var self = this;
    // 先拉取城市清单：新增城市能在不发版本的情况下出现在各页面 tab
    fetchCities().then(function(arr) {
      var citiesChanged = false;
      if (arr) {
        citiesChanged = !sameCityKeys(self.globalData.cities, arr);
        self.globalData.cities = arr;
        if (citiesChanged) {
          resetCityMaps(); // 清除 normalizeCity 缓存，用新城市列表重建映射（新增城市用中文名筛选也能命中）
          console.log('[童行] 城市清单已更新，共', arr.length, '城');
          self.notifyCitiesUpdated();
        }
      }
      // 拉取云端数据版本清单，与本地比对：版本相同 => 云侧数据无变化，直接复用缓存、不再下载几 MB 大文件
      self._checkMeta().then(function(r) {
        var dataChanged = r.changed;
        var cacheTime = wx.getStorageSync(CACHE_TIME_KEY) || 0;
        var fresh = cacheTime && (Date.now() - cacheTime) < self.SILENT_TTL_MS;
        var force = self._seededThisLaunch || self._versionChanged || self.globalData.isPartial || self.globalData.venuesPartial;
      // 跳过下载：云侧数据无变化 + 城市清单无增减 + 非强制（首启/升级/上次残缺）
      // 注意：即便云侧无变化，只要本地场馆明显未拉满(<90% 预期)也要继续尝试补齐，
      // 否则活动曾成功缓存并落盘版本号后，场馆会永久被"跳过下载"卡在打包兜底(378)。
      var venuesSatisfied = r.meta && r.meta.venues && (self.globalData.venues.length >= r.meta.venues * 0.9);
      if (!dataChanged && !citiesChanged && !force && venuesSatisfied) {
        console.log('[童行] 云侧数据无更新且场馆已拉满，跳过下载，复用本地缓存');
        return;
      }
      if (!dataChanged && !citiesChanged && !force) {
        console.warn('[童行] 云侧数据无更新，但本地场馆仅 ' + self.globalData.venues.length + ' 条(预期~' + (r.meta && r.meta.venues) + ')，仍尝试补齐场馆');
      }
        // 有更新或强制 => 下载最新数据；成功写入后把版本号落盘，供下次启动精准比对
        self._pendingMeta = r.meta || null;
        self._pendingMetaVersion = (r.meta && r.meta.version) || null;
        self.globalData.dataMeta = r.meta || null; // 供关于页展示“预期场馆数”
        self.silentUpdateExhibitions();
        self.silentUpdateVenues();
      });
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
      wx.setStorageSync(CACHE_PARTIAL_KEY, !!isPartial); // 记录是否残缺，避免下次启动误判为已完整
      // 全量写入成功 => 把云端数据版本号落盘，供下次启动精准比对（云侧无变化则跳过下载）
      if (!isPartial && this._pendingMetaVersion) {
        wx.setStorageSync(DATA_META_VERSION_KEY, this._pendingMetaVersion);
      }
    } catch (e) {}
    return true;
  },

  // ========== 统一写入场馆数据 ==========
  // isPartial=true 表示本次仅为部分城市子集（补齐完成前），下次启动应强制补齐
  applyVenues(arr, isPartial) {
    if (!arr || arr.length === 0) return false;
    // 不降级防护：远程返回远少于已加载（异常/截断响应）时，保留现有数据，
    // 避免把已正确的全量(2964)误抹成异常的小集。
    var cur = this.globalData.venues || [];
    if (cur.length > arr.length * 2) {
      console.warn('[童行] 远程场馆数(' + arr.length + ')远少于当前(' + cur.length + ')，疑似异常，保留现有数据');
      return false;
    }
    // 注意：场馆数据不含 start_date 等字段，不可调用活动的 precomputeDerived（会读 start_date.substring 崩溃）。
    // 场馆页面仅依赖 name/city/type 等原始字段，无需派生字段预计算。
    this.globalData.venues = arr;
    this.globalData.venuesPartial = !!isPartial;
    this.buildVenueMap();
    try {
      wx.setStorageSync(VENUE_CACHE_KEY, arr);
      wx.setStorageSync(VENUE_CACHE_TIME_KEY, Date.now());
      wx.setStorageSync(VENUE_PARTIAL_KEY, !!isPartial);
      // 全量写入成功 => 同步落盘云端数据版本号（与活动同理，避免下次误判为有变化而重下）
      if (!isPartial && this._pendingMetaVersion) {
        wx.setStorageSync(DATA_META_VERSION_KEY, this._pendingMetaVersion);
      }
    } catch (e) {}
    return true;
  },

  // ========== 三级分级加载（按时间紧迫度，优先级从高到低）==========
  // Tier1 近期活动(exhibitions_recent.json) → Tier2 全量分城市文件 → Tier3 历史活动(exhibitions_past.json)
  // 用户最关心「最近有什么可去的」，所以最先出近期；历史活动优先级最低，最后再填。
  // 三级累积合并、去重；isPartial 在全量(Tier2)到达后转 false（历史仅收尾，不影响置灰判定）。
  silentUpdateExhibitions() {
    var self = this;
    self._setLoading(true); // 开始下载活动数据，驱动首页刷新图标旋转
    this.loadStagedData(false, function() {
      self._setLoading(false); // 活动数据加载完成（含各级补齐），停止旋转
    });
  },

  // staged 加载；onDone(ok) 在最后一级完成后回调（ok=是否所有城市全量都取到）
  loadStagedData(force, onDone) {
    var self = this;
    self._staged = { recent: null, full: null, past: null, fullCities: {} };

    // Tier1：近期活动（首屏最优先，离当前时间最近、即将举办）
    fetchRecent().then(function(recent) {
      if (recent && recent.length) {
        self._staged.recent = recent;
        self.flushStaged(true);
        console.log('[童行] Tier1 近期活动已加载（首屏），共', recent.length, '条');
        self.notifyDataUpdated();
      }
      // Tier2：后续剩余活动（全量分城市文件，后台并行拉取补全）
      return fetchAllExhibitions();
    }).then(function(result) {
      var merged = result.merged, failed = result.failed;
      if (merged && merged.length) {
        self._staged.full = merged;
        // 记录已加载到的城市，用于判断全量是否“真的完整”
        merged.forEach(function(x) { if (x.city) self._staged.fullCities[x.city] = true; });
        var complete = failed.length === 0;
        self.flushStaged(!complete); // 有城市缺失时仍视为 partial（不污染缓存为“完整”）
        console.log('[童行] Tier2 全量活动已加载，共', merged.length, '条' + (complete ? '' : ('，缺失城市：' + failed.join(','))));
        self.notifyDataUpdated();
      }
      // Tier3：历史活动（已结束），最后再拉，不挤占首屏带宽
      return fetchPast();
    }).then(function(past) {
      if (past && past.length) {
        self._staged.past = past;
      }
      // 关键：是否“已完整”必须以“所有城市是否都取到”为准，绝不等同于 false。
      // 否则武汉/西安等个别城市在 Tier2 并行拉取失败、且补齐重试那一刻也失败时，
      // 会被错误标记为“完整”写入缓存，导致永久停在近期 80 条且下次启动不再重拉。
      var complete = self._allCitiesLoaded();
      self.flushStaged(!complete);
      console.log('[童行] Tier3 历史活动已加载，共', (past || []).length, '条' + (complete ? '' : '，仍有城市缺失，将补齐'));
      self.notifyDataUpdated();
      if (onDone) onDone(complete);
      // 最终兜底：仍有城市缺失则持续补齐（直到全部取到或次数耗尽）；
      // 因 isPartial 保持 true，即便本次没补齐，下次启动也会强制重拉，不会永久卡 80。
      if (!complete) {
        console.warn('[童行] 仍有城市缺失，开始补齐：', self._missingCities().join(','));
        self._fillMissingCities(self._missingCities(), 6);
      }
    }).catch(function() {
      if (onDone) onDone(self._allCitiesLoaded());
      // 整体异常：重试仍未加载到的城市
      self._fillMissingCities(self._missingCities(), 6);
    });
  },

  // 当前已加载的城市 key 集合是否覆盖全部 activeCities
  _allCitiesLoaded() {
    var loaded = (this._staged && this._staged.fullCities) || {};
    return (activeCities || []).every(function(c) { return loaded[c.key]; });
  },

  // 还缺失哪些城市（用于补齐/重试）
  _missingCities() {
    var loaded = (this._staged && this._staged.fullCities) || {};
    return (activeCities || []).filter(function(c) { return !loaded[c.key]; }).map(function(c) { return c.key; });
  },

  // 补齐缺失城市：单独重拉这些城市分文件，成功则合并进 full 并刷新；
  // 仍有缺失则退避后递归重试（rounds 递减），直到全部补齐或次数耗尽。
  // 这样即便某次并行请求被限流/抖动导致部分城市失败，最终也能补全，不会永远停在 80 条。
  _fillMissingCities(keys, rounds) {
    var self = this;
    if (!keys || !keys.length) return;
    fetchCityBatch(keys.map(function(k) { return { key: k }; })).then(function(res) {
      if (res.merged.length) {
        self._staged = self._staged || { fullCities: {} };
        self._staged.full = (self._staged.full || []).concat(res.merged);
        res.merged.forEach(function(x) { if (x.city) self._staged.fullCities[x.city] = true; });
        var stillMissing = self._missingCities();
        var complete = stillMissing.length === 0;
        self.flushStaged(!complete);
        console.log('[童行] 补齐成功 +' + res.merged.length + '条' + (stillMissing.length ? ('，仍缺：' + stillMissing.join(',')) : '，已全部补齐'));
        self.notifyDataUpdated();
        if (stillMissing.length && rounds > 1) {
          setTimeout(function() { self._fillMissingCities(stillMissing, rounds - 1); }, 3000);
        } else if (stillMissing.length) {
          console.warn('[童行] 缺失城市经多次重试仍不可用，保留近期子集：', stillMissing.join(','));
        }
      } else if (rounds > 1) {
        setTimeout(function() { self._fillMissingCities(keys, rounds - 1); }, 3000);
      }
    });
  },

  // 累积合并三级数据并写入：full 为全集（已含 Tier1 子集）优先；recent 仅在 full 未到时补充；
  // past 最后补。按 (city|name|start_date) 去重，避免 Tier1 与 Tier2 重叠导致重复渲染。
  flushStaged(isPartial) {
    var s = this._staged || {};
    if (!s.recent && !s.full && !s.past) return;
    var seen = {};
    var order = [];
    function add(arr) {
      if (!arr) return;
      arr.forEach(function(x) {
        var k = (x.city || '') + '|' + (x.name || x.title || '') + '|' + (x.start_date || '');
        if (!seen[k]) { seen[k] = true; order.push(x); }
      });
    }
    add(s.full);    // 全集优先（含近期子集）
    add(s.recent);  // 仅当 full 未加载时补充近期
    add(s.past);    // 历史最后补
    if (order.length) this.applyExhibitions(order, isPartial);
  },

  // 仅重试全量 + Tier3 历史（用于异常自愈）：合并而非覆盖，避免丢失已加载城市
  retryFullExhibitions() {
    var self = this;
    fetchAllExhibitions().then(function(result) {
      var merged = result.merged;
      if (merged && merged.length) {
        self._staged = self._staged || { fullCities: {} };
        self._staged.full = (self._staged.full || []).concat(merged);
        merged.forEach(function(x) { if (x.city) self._staged.fullCities[x.city] = true; });
        if (result.failed.length) self._fillMissingCities(result.failed, 3);
        else self.flushStaged(false);
        console.log('[童行] 全量重试完成，已合并', merged.length, '条');
        self.notifyDataUpdated();
      } else {
        console.warn('[童行] 全量重试仍不可用，保持近期/缓存数据');
      }
    });
  },

  silentUpdateVenues() {
    var self = this;
    self._venueStaged = { fullCities: {} };
    fetchAllVenues().then(function(result) {
      var merged = result.merged, failed = result.failed;
      if (merged && merged.length) {
        // 分城市部分成功：先显示已拉到的子集，再补缺失城市（与活动加载策略一致，不依赖大单文件）
        merged.forEach(function(v) { if (v.city) self._venueStaged.fullCities[v.city] = true; });
        var ok = self.applyVenues(merged, failed.length > 0);
        if (ok) {
          self.notifyDataUpdated();
          console.log('[童行] 场馆已加载', merged.length, '条' + (failed.length ? ('，缺失城市：' + failed.join(',')) : ''));
        }
        if (failed.length) {
          console.warn('[童行] 部分城市场馆未取到，开始补齐：', failed.join(','));
          self._fillMissingVenueCities(failed, 6);
        }
      } else {
        // 分城市全部失败（弱网/被墙）：最后才用单文件全量兜底，而非放弃分城市数据
        console.warn('[童行] 场馆分城市全部未取到，启用单文件全量兜底');
        self.fetchVenueFullFallback();
      }
    }).catch(function() {
      self.fetchVenueFullFallback();
    });
  },

  // 场馆兜底：单文件 venue_info.json（全量 2964，CDN 已长期缓存）。
  // 当分城市小文件整体/部分不可达时，用一次请求拿到完整场馆库，根治真机长期停在打包兜底(378) 的问题。
  fetchVenueFullFallback() {
    var self = this;
    fetchJsonFromSources('output/venue_info.json', { timeout: 60000, maxRetries: 2 }).then(function(res) {
      var arr = toArray(res && res.data);
      if (arr && arr.length) {
        self._venueStaged = self._venueStaged || { fullCities: {} };
        arr.forEach(function(v) { if (v.city) self._venueStaged.fullCities[v.city] = true; });
        // 单文件即全量，直接置 isPartial=false（不降级防护：2964 远小于已加载子集*2，必通过）
        var ok = self.applyVenues(arr, false);
        if (ok) {
          self.notifyDataUpdated();
          console.log('[童行] 场馆已由单文件回退补齐，共', arr.length, '条');
        }
      } else {
        // 单文件也失败：退回分城市补齐（极端弱网保留打包兜底，下次启动因 venuesPartial 强制重拉）
        self._fillMissingVenueCities(self._missingVenueCities(), 6);
      }
    }).catch(function() {
      self._fillMissingVenueCities(self._missingVenueCities(), 6);
    });
  },

  // 场馆：当前已加载城市是否覆盖全部 activeCities
  _allVenueCitiesLoaded() {
    var loaded = (this._venueStaged && this._venueStaged.fullCities) || {};
    return (activeCities || []).every(function(c) { return loaded[c.key]; });
  },

  _missingVenueCities() {
    var loaded = (this._venueStaged && this._venueStaged.fullCities) || {};
    return (activeCities || []).filter(function(c) { return !loaded[c.key]; }).map(function(c) { return c.key; });
  },

  // 场馆补齐缺失城市：单独重拉这些城市分文件，合并进现有数据（已有城市保留，补齐缺失），
  // 仍有缺失则退避递归重试（rounds 递减）。与活动补齐逻辑对称。
  _fillMissingVenueCities(keys, rounds) {
    var self = this;
    if (!keys || !keys.length) return;
    fetchVenueBatch(keys.map(function(k) { return { key: k }; })).then(function(res) {
      if (res.merged.length) {
        self._venueStaged = self._venueStaged || { fullCities: {} };
        res.merged.forEach(function(v) { if (v.city) self._venueStaged.fullCities[v.city] = true; });
        // 合并到现有数据：按名称去重，补齐缺失城市，不覆盖已加载城市
        var existing = self.globalData.venues || [];
        var byName = {};
        existing.forEach(function(v) { byName[v.name] = true; });
        var added = res.merged.filter(function(v) { return !byName[v.name]; });
        var mergedAll = existing.concat(added);
        var complete = self._allVenueCitiesLoaded();
        self.applyVenues(mergedAll, !complete);
        self.notifyDataUpdated();
        console.log('[童行] 场馆补齐 +' + added.length + '条' + (complete ? '，已全部补齐' : ('，仍缺：' + self._missingVenueCities().join(','))));
        if (!complete && rounds > 1) {
          setTimeout(function() { self._fillMissingVenueCities(self._missingVenueCities(), rounds - 1); }, 3000);
        } else if (!complete) {
          console.warn('[童行] 缺失城市场馆经多次重试仍不可用：', self._missingVenueCities().join(','));
        }
      } else if (rounds > 1) {
        setTimeout(function() { self._fillMissingVenueCities(keys, rounds - 1); }, 3000);
      }
    });
  },

  // ========== 手动强制刷新（下拉刷新 / 点刷新按钮调用）==========

  forceRefresh(callback) {
    var self = this;
    self._setLoading(true);
    console.log('[童行] 强制刷新中...');
    // 先拉城市清单（新增城市立即可见）；必须等城市清单更新完成再拉场馆，
    // 否则 fetchAllVenues 仍用旧 activeCities（不含新增城市），导致新城市场馆永远拉不到。
    fetchCities().then(function(arr) {
      if (arr && !sameCityKeys(self.globalData.cities, arr)) {
        self.globalData.cities = arr;
        resetCityMaps(); // 强制刷新时同样清除 normalizeCity 缓存
        self.notifyCitiesUpdated();
        console.log('[童行] 城市清单已更新，共', arr.length, '城');
      }
      // 城市清单就绪后再拉数据版本清单，决定是否真的需要下载
      return self._checkMeta();
    }).then(function(r) {
      var dataChanged = r.changed;
      var force = self._seededThisLaunch || self._versionChanged;
      // 主动刷新时，即便云侧无变化，只要场馆未拉满也要继续补齐（避免被活动缓存版本号永久跳过）
      var venuesSatisfied = r.meta && r.meta.venues && (self.globalData.venues.length >= r.meta.venues * 0.9);
      if (!dataChanged && !force && venuesSatisfied) {
        self._setLoading(false);
        console.log('[童行] 强制刷新：云侧数据无更新，已是最新');
        self.notifyDataUpdated(); // 用本地缓存重渲染
        if (callback) callback(true);
        return;
      }
      if (!dataChanged && !force) {
        console.warn('[童行] 强制刷新：云侧无更新，但本地场馆仅 ' + self.globalData.venues.length + ' 条，仍尝试补齐');
      }
      self._pendingMetaVersion = (r.meta && r.meta.version) || null;
      self.globalData.dataMeta = r.meta || null; // 供关于页展示“预期场馆数”
      // 三级分级拉取：近期 → 全量 → 历史；完成后回调
      self.loadStagedData(true, function(ok) {
        self._setLoading(false);
        if (ok) console.log('[童行] 强制刷新完成');
        if (callback) callback(ok);
      });
      // 同时刷新场馆（分城市并行拉取 + 缺失补齐 + 单文件兜底）
      // 此时 activeCities 已被 fetchCities 更新，fetchAllVenues 会覆盖新增城市
      self._venueStaged = { fullCities: {} };
      fetchAllVenues().then(function(result) {
        var merged = result.merged, failed = result.failed;
        if (merged && merged.length) {
          merged.forEach(function(v) { if (v.city) self._venueStaged.fullCities[v.city] = true; });
          self.applyVenues(merged, failed.length > 0);
          self.notifyDataUpdated();
          console.log('[童行] 场馆已刷新', merged.length, '条' + (failed.length ? ('，缺失：' + failed.join(',')) : ''));
        }
        if (failed.length) {
          self._fillMissingVenueCities(failed, 6);
          self.fetchVenueFullFallback();
        }
      });
    }).catch(function(err) {
      // fetchCities 失败时回退到旧的并行逻辑，保证刷新不中断
      console.warn('[童行] 城市清单拉取失败，沿用旧清单继续刷新', err);
      self._checkMeta().then(function(r) {
        var dataChanged = r.changed;
        var force = self._seededThisLaunch || self._versionChanged;
        var venuesSatisfied = r.meta && r.meta.venues && (self.globalData.venues.length >= r.meta.venues * 0.9);
        if (!dataChanged && !force && venuesSatisfied) {
          self._setLoading(false);
          self.notifyDataUpdated();
          if (callback) callback(true);
          return;
        }
        self._pendingMetaVersion = (r.meta && r.meta.version) || null;
        self.globalData.dataMeta = r.meta || null;
        self.loadStagedData(true, function(ok) {
          self._setLoading(false);
          if (callback) callback(ok);
        });
        self._venueStaged = self._venueStaged || { fullCities: {} };
        fetchAllVenues().then(function(result) {
          var merged = result.merged, failed = result.failed;
          if (merged && merged.length) {
            merged.forEach(function(v) { if (v.city) self._venueStaged.fullCities[v.city] = true; });
            self.applyVenues(merged, failed.length > 0);
            self.notifyDataUpdated();
          }
          if (failed.length) {
            self._fillMissingVenueCities(failed, 6);
            self.fetchVenueFullFallback();
          }
        });
      });
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
  loadingCallbacks: [],

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

  // 加载状态（是否正在后台刷新/下载数据）订阅：持久订阅（不自动清空），用于驱动首页刷新图标旋转。
  // 订阅时立即以当前状态回调一次，避免“订阅前已在下载”导致漏掉 true 事件、旋转不触发。
  onLoadingChange(callback) {
    this.loadingCallbacks.push(callback);
    try { callback(this.globalData.isLoading); } catch (e) {}
  },

  offLoadingChange(callback) {
    this.loadingCallbacks = this.loadingCallbacks.filter(function(cb) { return cb !== callback; });
  },

  _setLoading(v) {
    v = !!v;
    if (this.globalData.isLoading === v) return;
    this.globalData.isLoading = v;
    this.loadingCallbacks.forEach(function(cb) {
      try { cb(v); } catch (e) {}
    });
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
