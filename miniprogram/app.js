// 本地数据作为离线兜底
const localExhibitions = require('./data/exhibitions.js');
const localVenues = require('./data/venues.js');

// 远程数据地址（GitHub raw 直连，缓存仅5分钟，接近实时）
const REMOTE_URL = 'https://raw.githubusercontent.com/islon/goout/main/output/exhibitions.json';
const REMOTE_VENUE_URL = 'https://raw.githubusercontent.com/islon/goout/main/output/venue_info.json';
// 缓存过期时间：6小时
const CACHE_EXPIRE = 6 * 60 * 60 * 1000;
const CACHE_KEY = 'goout_exhibitions_cache';
const CACHE_TIME_KEY = 'goout_exhibitions_cache_time';
const VENUE_CACHE_KEY = 'goout_venues_cache';
const VENUE_CACHE_TIME_KEY = 'goout_venues_cache_time';

// 加时间戳，绕过浏览器缓存
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
    isRemoteData: false
  },

  onLaunch() {
    this.buildVenueMap();
    this.fetchExhibitions();
    this.fetchVenues();
  },

  buildVenueMap() {
    const map = {};
    for (let i = 0; i < this.globalData.venues.length; i++) {
      const v = this.globalData.venues[i];
      if (v && v.name) {
        map[v.name] = v;
      }
    }
    this.globalData.venueMap = map;
  },

  fetchExhibitions() {
    const self = this;

    // 1. 先检查本地缓存是否有效
    const cacheTime = wx.getStorageSync(CACHE_TIME_KEY) || 0;
    const now = Date.now();

    if (cacheTime && (now - cacheTime < CACHE_EXPIRE)) {
      const cached = wx.getStorageSync(CACHE_KEY);
      if (cached && cached.length > 0) {
        console.log('[童行] 使用本地缓存活动数据，共', cached.length, '条');
        self.globalData.exhibitions = cached;
        self.globalData.dataReady = true;
        self.globalData.isRemoteData = false;
        self.notifyReady();
        // 缓存有效也后台静默更新
        self.silentUpdateExhibitions();
        return;
      }
    }

    // 2. 无有效缓存，远程拉取
    console.log('[童行] 正在从远程拉取最新活动数据...');
    wx.request({
      url: getFreshUrl(REMOTE_URL),
      method: 'GET',
      timeout: 15000,
      success: function(res) {
        if (res.statusCode === 200 && res.data && res.data.length > 0) {
          console.log('[童行] 远程活动数据拉取成功，共', res.data.length, '条');
          self.globalData.exhibitions = res.data;
          self.globalData.dataReady = true;
          self.globalData.isRemoteData = true;
          try {
            wx.setStorageSync(CACHE_KEY, res.data);
            wx.setStorageSync(CACHE_TIME_KEY, now);
          } catch (e) {
            console.error('[童行] 活动缓存写入失败', e);
          }
          self.notifyReady();
        } else {
          console.warn('[童行] 远程活动数据异常，使用本地数据');
          self.globalData.exhibitions = localExhibitions;
          self.globalData.dataReady = true;
          self.globalData.isRemoteData = false;
          self.notifyReady();
        }
      },
      fail: function(err) {
        console.warn('[童行] 远程拉取活动失败，使用本地数据', err);
        self.globalData.exhibitions = localExhibitions;
        self.globalData.dataReady = true;
        self.globalData.isRemoteData = false;
        self.notifyReady();
      }
    });
  },

  // 静默更新（缓存有效时后台拉取最新活动数据）
  silentUpdateExhibitions() {
    const self = this;
    wx.request({
      url: getFreshUrl(REMOTE_URL),
      method: 'GET',
      timeout: 15000,
      success: function(res) {
        if (res.statusCode === 200 && res.data && res.data.length > 0) {
          self.globalData.exhibitions = res.data;
          self.globalData.isRemoteData = true;
          try {
            wx.setStorageSync(CACHE_KEY, res.data);
            wx.setStorageSync(CACHE_TIME_KEY, Date.now());
          } catch (e) {}
          console.log('[童行] 活动静默更新完成，共', res.data.length, '条');
        }
      },
      fail: function() {}
    });
  },

  fetchVenues() {
    const self = this;
    const cacheTime = wx.getStorageSync(VENUE_CACHE_TIME_KEY) || 0;
    const now = Date.now();

    if (cacheTime && (now - cacheTime < CACHE_EXPIRE)) {
      const cached = wx.getStorageSync(VENUE_CACHE_KEY);
      if (cached && cached.length > 0) {
        console.log('[童行] 使用本地缓存场馆数据，共', cached.length, '条');
        self.globalData.venues = cached;
        self.buildVenueMap();
        self.silentUpdateVenues();
        return;
      }
    }

    console.log('[童行] 正在从远程拉取最新场馆数据...');
    wx.request({
      url: getFreshUrl(REMOTE_VENUE_URL),
      method: 'GET',
      timeout: 15000,
      success: function(res) {
        if (res.statusCode === 200 && res.data && res.data.length > 0) {
          console.log('[童行] 远程场馆数据拉取成功，共', res.data.length, '条');
          self.globalData.venues = res.data;
          self.buildVenueMap();
          try {
            wx.setStorageSync(VENUE_CACHE_KEY, res.data);
            wx.setStorageSync(VENUE_CACHE_TIME_KEY, now);
          } catch (e) {
            console.error('[童行] 场馆缓存写入失败', e);
          }
        } else {
          console.warn('[童行] 远程场馆数据异常，使用本地场馆数据');
        }
      },
      fail: function(err) {
        console.warn('[童行] 远程拉取场馆失败，使用本地场馆数据', err);
      }
    });
  },

  silentUpdateVenues() {
    const self = this;
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
          console.log('[童行] 场馆静默更新完成，共', res.data.length, '条');
        }
      },
      fail: function() {}
    });
  },

  // 通知等待数据的页面
  readyCallbacks: [],
  onReady(callback) {
    if (this.globalData.dataReady) {
      callback();
    } else {
      this.readyCallbacks.push(callback);
    }
  },
  notifyReady() {
    this.readyCallbacks.forEach(function(cb) { cb(); });
    this.readyCallbacks = [];
  }
});
