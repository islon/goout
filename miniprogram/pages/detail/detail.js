const { venueAddressMap } = require('../../data/filters.js');
const { getActivityType, getFeeType, formatDate, getDuration, normalizeCity, findVenue } = require('../../utils/helpers.js');

const app = getApp();

Page({
  data: {
    activity: null,
    activityType: '',
    feeType: '',
    dateDisplay: '',
    duration: '',
    venueAddress: '',
    showLink: false,
    showBooking: false,
    bookingApp: '',
    bookingHint: '',
    hasReminded: false,
    remindId: '',
    venue: null,
    hasVenue: false
  },

  onLoad(options) {
    const self = this;
    const id = decodeURIComponent(options.id || '');

    function findActivity() {
      const allExhibitions = app.globalData.exhibitions || [];
      // 通过 ID 查找活动
      let activity = null;
      for (let i = 0; i < allExhibitions.length; i++) {
        const e = allExhibitions[i];
        const cardId = e.id || (e.source + '-' + e.name + '-' + e.start_date);
        if (cardId === id) {
          activity = e;
          break;
        }
      }

      if (!activity) {
        wx.showToast({ title: '活动不存在', icon: 'none' });
        setTimeout(function() { wx.navigateBack(); }, 1500);
        return;
      }

      const startDate = activity.start_date;
      const endDate = activity.end_date;
      const dateDisplay = startDate === endDate
        ? formatDate(startDate)
        : formatDate(startDate) + ' ~ ' + formatDate(endDate);
      const duration = getDuration(startDate, endDate);
      const activityType = getActivityType(activity);
      const feeType = getFeeType(activity);
      // 优先用 venue_info.json 的地址（数据驱动），venueAddressMap 仅作兜底
      const venue = findVenue(activity.venue, app.globalData.venueMap || {});
      const venueAddress = (venue && venue.address && venue.address !== '待补充')
        ? venue.address
        : (venueAddressMap[activity.source] || '');

      self.setData({
        activity: activity,
        activityType: activityType,
        feeType: feeType,
        dateDisplay: dateDisplay,
        duration: duration,
        venueAddress: venueAddress,
        showLink: !!activity.url,
        showBooking: !!(activity.booking_method && activity.booking_method.app_name),
        bookingApp: activity.booking_method ? activity.booking_method.app_name : '',
        bookingHint: activity.booking_method ? (activity.booking_method.search_hint || '') : '',
        venue: venue,
        hasVenue: !!venue
      });

      wx.setNavigationBarTitle({ title: activity.name || '活动详情' });

      // 检查是否已设置提醒
      const remindId = activity.id || (activity.source + '-' + activity.name + '-' + startDate);
      const remindedIds = wx.getStorageSync('remindedIds') || [];
      const hasReminded = remindedIds.indexOf(remindId) >= 0;
      self.setData({ remindId: remindId, hasReminded: hasReminded });
    }

    // 等待数据准备完成
    app.onReady(function() {
      findActivity();
    });
  },

  onVenueTap() {
    if (!this.data.venue || !this.data.venue.name) return;
    wx.navigateTo({
      url: '/pages/venue/venue?id=' + encodeURIComponent(this.data.venue.name)
    });
  },

  onGoVenues() {
    wx.switchTab({
      url: '/pages/venues/venues'
    });
  },

  onCopyLink() {
    if (!this.data.activity || !this.data.activity.url) return;
    wx.setClipboardData({
      data: this.data.activity.url,
      success: function() {
        wx.showToast({ title: '链接已复制', icon: 'success' });
      }
    });
  },

  onBookingTap() {
    const bm = this.data.activity && this.data.activity.booking_method;
    if (!bm) return;
    const appName = bm.app_name || '';
    const hint = bm.search_hint || '';
    const appType = bm.app_type || 'wechat_mini_program';

    // 小程序/公众号类型：复制小程序名，提示用户去微信搜索
    if (appType === 'wechat_mini_program' || appType === 'wechat_official_account') {
      wx.setClipboardData({
        data: appName,
        success: function() {
          wx.showModal({
            title: '报名入口已复制',
            content: '小程序/公众号名称「' + appName + '」已复制。\n\n操作步骤：\n1. 退出本小程序，回到微信首页\n2. 点击顶部搜索框，粘贴并搜索\n3. ' + hint + '\n\n由于微信限制，需手动搜索进入对应场馆官方小程序。',
            showCancel: false,
            confirmText: '我知道了',
            confirmColor: '#D4A373'
          });
        }
      });
      return;
    }

    // App 类型：提示用户下载
    if (appType === 'app') {
      wx.showModal({
        title: '报名入口提示',
        content: '本活动需通过 App 报名：\n\n' + appName + '\n\n操作步骤：\n' + hint,
        showCancel: false,
        confirmText: '我知道了',
        confirmColor: '#D4A373'
      });
      return;
    }

    // Web 类型：直接复制 URL
    if (appType === 'web' && bm.platform_url) {
      wx.setClipboardData({
        data: bm.platform_url,
        success: function() {
          wx.showToast({ title: '网址已复制', icon: 'success' });
        }
      });
      return;
    }

    // 兜底
    wx.showModal({
      title: '报名入口',
      content: hint || appName,
      showCancel: false
    });
  },

  onRemindTap() {
    if (this.data.hasReminded) {
      // 已设置提醒，取消提醒
      const remindedIds = wx.getStorageSync('remindedIds') || [];
      const idx = remindedIds.indexOf(this.data.remindId);
      if (idx >= 0) remindedIds.splice(idx, 1);
      wx.setStorageSync('remindedIds', remindedIds);
      this.setData({ hasReminded: false });
      wx.showToast({ title: '已取消提醒', icon: 'none' });
      return;
    }

    // 请求订阅消息权限
    // 注意：templateId 需要在微信公众平台后台配置订阅消息模板后获取
    // 当前为占位ID，实际使用时请替换为真实的模板ID
    const templateId = 'REPLACE_WITH_YOUR_TEMPLATE_ID';
    
    wx.requestSubscribeMessage({
      tmplIds: [templateId],
      success: (res) => {
        if (res[templateId] === 'accept') {
          // 用户同意，保存提醒状态
          const remindedIds = wx.getStorageSync('remindedIds') || [];
          if (remindedIds.indexOf(this.data.remindId) < 0) {
            remindedIds.push(this.data.remindId);
          }
          wx.setStorageSync('remindedIds', remindedIds);
          this.setData({ hasReminded: true });

          // TODO: 在实际部署时，这里需要调用后端API记录提醒
          // wx.cloud.callFunction 或 wx.request 发送活动ID和用户openid到服务器
          // 服务器在活动开始前1天通过 subscribeMessage.send API 推送提醒

          wx.showToast({ title: '提醒设置成功', icon: 'success' });
        } else {
          wx.showToast({ title: '需要授权才能提醒哦', icon: 'none' });
        }
      },
      fail: (err) => {
        // 测试号或未配置模板时的降级处理
        if (err.errCode === 20002 || err.errMsg.indexOf('tmplId') >= 0 || templateId === 'REPLACE_WITH_YOUR_TEMPLATE_ID') {
          // 降级方案：仅本地记录，提示用户
          const remindedIds = wx.getStorageSync('remindedIds') || [];
          if (remindedIds.indexOf(this.data.remindId) < 0) {
            remindedIds.push(this.data.remindId);
          }
          wx.setStorageSync('remindedIds', remindedIds);
          this.setData({ hasReminded: true });
          wx.showModal({
            title: '提醒已设置',
            content: '微信提醒功能需要在正式发布后配置。目前已在本地记录，你也可以在「订阅日程」页面使用日历订阅功能。',
            showCancel: false,
            confirmText: '知道了'
          });
        } else {
          wx.showToast({ title: '设置失败，请重试', icon: 'none' });
        }
      }
    });
  },

  onShareAppMessage() {
    return {
      title: this.data.activity ? this.data.activity.name : '童行 - 亲子活动日历',
      path: '/pages/index/index'
    };
  }
});
