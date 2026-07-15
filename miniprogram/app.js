// 本地数据作为离线兜底（打包时生成，相对较新）
const localExhibitions = require('./data/exhibitions.js');
const localVenues = require('./data/venues.js');

// 远程数据地址（GitHub raw 直连）
const REMOTE_URL = 'https://raw.githubusercontent.com/islon/goout/main/output/exhibitions.json';
const REMOTE_VENUE_URL = 'https://raw.githubusercontent.com/islon/goout/main/output/venue_info.json';

// 缓存 key
const CACHE_KEY = 'goout_exhibitions_cache';
const CACHE_TIME_KEY = 'goout_exhibitions_cache_time';
const VENUE_CACHE_KEY = 'goout_venues_cache';
const VENUE_CACHE_TIME_KEY = 'goout_venues_cache_time';

// 加时间戳，绕过 CDN 缓存
function getFreshUrl(base) {
  return base + '?t=' + Date.now();
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
    var cached = wx.getStorageSync(CACHE_KEY);
    if (cached && Array.isArray(cached) && cached.length > 0) {
      this.globalData.exhibitions = cached;
      loadedAny = true;
      var ct = wx.getStorageSync(CACHE_TIME_KEY);
      if (ct) {
        this.globalData.lastUpdateTime = new Date(ct).toLocaleString();
      }
    }

    // 场馆数据
    var vCached = wx.getStorageSync(VENUE_CACHE_KEY);
    if (vCached && Array.isArray(vCached) && vCached.length > 0) {
      this.globalData.venues = vCached;
      this.buildVenueMap();
      loadedAny = true;
    }

    return loadedAny;
  },

  // ========== 后台静默更新（始终执行）==========

  silentUpdateAll() {
    this.silentUpdateExhibitions();
    this.silentUpdateVenues();
  },

  silentUpdateExhibitions() {
    var self = this;
    wx.request({
      url: getFreshUrl(REMOTE_URL),
      method: 'GET',
      timeout: 15000,
      success: function(res) {
        if (res.statusCode === 200 && res.data && res.data.length > 0) {
          self.globalData.exhibitions = res.data;
          self.globalData.isRemoteData = true;
          var now = Date.now();
          self.globalData.lastUpdateTime = new Date(now).toLocaleString();
          try {
            wx.setStorageSync(CACHE_KEY, res.data);
            wx.setStorageSync(CACHE_TIME_KEY, now);
          } catch (e) {}
          console.log('[童行] 活动数据已更新至最新，共', res.data.length, '条');

          // 通知页面刷新（如果页面已经显示旧数据）
          self.notifyDataUpdated();
        }
      },
      fail: function(err) {
        console.log('[童行] 远程活动数据不可用，继续使用本地缓存/打包数据', err.errMsg || '');
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
        if (res.statusCode === 200 && res.data && res.data.length > 0) {
          self.globalData.venues = res.data;
          self.buildVenueMap();
          try {
            wx.setStorageSync(VENUE_CACHE_KEY, res.data);
            wx.setStorageSync(VENUE_CACHE_TIME_KEY, Date.now());
          } catch (e) {}
          console.log('[童行] 场馆数据已更新至最新，共', res.data.length, '条');
        }
      },
      fail: function() {}
    });
  },

  // ========== 手动强制刷新（下拉刷新 / 点刷新按钮调用）==========

  forceRefresh(callback) {
    var self = this;
    console.log('[童行] 强制刷新中...');
    wx.request({
      url: getFreshUrl(REMOTE_URL),
      method: 'GET',
      timeout: 15000,
      success: function(res) {
        if (res.statusCode === 200 && res.data && res.data.length > 0) {
          self.globalData.exhibitions = res.data;
          self.globalData.isRemoteData = true;
          var now = Date.now();
          self.globalData.lastUpdateTime = new Date(now).toLocaleString();
          try {
            wx.setStorageSync(CACHE_KEY, res.data);
            wx.setStorageSync(CACHE_TIME_KEY, now);
          } catch (e) {}
          console.log('[童行] 强制刷新完成，共', res.data.length, '条');
        }
        if (callback) callback(true);
      },
      fail: function(err) {
        console.warn('[童行] 强制刷新失败', err);
        if (callback) callback(false);
      }
    });

    // 同时刷新场馆
    wx.request({
      url: getFreshUrl(REMOTE_VENUE_URL),
      method: 'GET',
      timeout: 15000,
      success: function(res) {
        if (res.statusCode === 200 && res.data && res.data.length > 0) {
          self.globalData.venues = res.data;
          self.buildVenueMap();
          try {
            wx.setStorageSync(VENUE_CACHE_KEY, res.data);
            wx.setStorageSync(VENUE_CACHE_TIME_KEY, Date.now());
          } catch (e) {}
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
  }
});
