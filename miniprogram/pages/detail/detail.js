// pages/detail/detail.js
const activitiesData = require('../../data/activities.json')

// 订阅消息模板ID
// 在小程序后台 → 功能 → 订阅消息 → 公共模板库中申请
// 推荐模板：活动开始提醒（含活动名称、时间、地点）
const SUBSCRIBE_TMPL_ID = '替换为你的订阅消息模板ID'

Page({
  data: {
    activity: null,
    subscribed: false,
    subscribeLoading: false
  },

  onLoad(options) {
    const id = parseInt(options.id)
    const activity = activitiesData[id]
    if (!activity) {
      wx.showToast({ title: '活动不存在', icon: 'error' })
      setTimeout(() => wx.navigateBack(), 1500)
      return
    }

    const today = new Date()
    today.setHours(0, 0, 0, 0)
    const startDate = new Date(activity.start_date)
    const daysUntil = Math.ceil((startDate - today) / (1000 * 60 * 60 * 24))

    this.setData({
      activity: {
        ...activity,
        _id: id,
        _dateRange: activity.start_date === activity.end_date 
          ? activity.start_date 
          : `${activity.start_date} ~ ${activity.end_date}`,
        _isFree: activity.fee === '免费' || activity.fee === '免费需预约',
        _daysUntil: daysUntil,
        _daysUntilText: daysUntil > 0 ? `${daysUntil} 天后开始` : daysUntil === 0 ? '今天开始' : '进行中'
      }
    })

    this.checkSubscription(id)
  },

  checkSubscription(activityId) {
    const subs = wx.getStorageSync('subscriptions') || []
    this.setData({ subscribed: subs.includes(activityId) })
  },

  onSubscribeTap() {
    if (this.data.subscribed) {
      this.unsubscribe()
      return
    }

    this.setData({ subscribeLoading: true })

    // 如果模板ID未配置，先保存本地订阅，提示用户
    if (SUBSCRIBE_TMPL_ID.startsWith('替换为')) {
      this.saveSubscriptionLocal()
      this.setData({ subscribeLoading: false })
      wx.showToast({ title: '已收藏（订阅消息模板待配置）', icon: 'none', duration: 2500 })
      return
    }

    // 调用微信订阅消息授权
    wx.requestSubscribeMessage({
      tmplIds: [SUBSCRIBE_TMPL_ID],
      success: (res) => {
        if (res[SUBSCRIBE_TMPL_ID] === 'accept') {
          this.saveSubscription()
        } else {
          wx.showToast({ title: '需要授权才能发送提醒', icon: 'none' })
        }
      },
      fail: (err) => {
        console.error('订阅失败', err)
        // 降级：仍然保存本地订阅
        this.saveSubscriptionLocal()
        wx.showToast({ title: '已收藏，提醒功能待配置', icon: 'none' })
      },
      complete: () => {
        this.setData({ subscribeLoading: false })
      }
    })
  },

  // 保存订阅到本地 + 云端
  saveSubscription() {
    const activityId = this.data.activity._id
    const subs = wx.getStorageSync('subscriptions') || []
    if (!subs.includes(activityId)) {
      subs.push(activityId)
      wx.setStorageSync('subscriptions', subs)
    }

    // 调用云函数记录订阅（如果云开发已初始化）
    if (wx.cloud && wx.cloud.callFunction) {
      wx.cloud.callFunction({
        name: 'subscribe',
        data: {
          activityId: activityId,
          activityTitle: this.data.activity.title,
          startDate: this.data.activity.start_date,
          venue: this.data.activity.venue
        },
        success: (res) => {
          console.log('订阅记录成功', res)
        },
        fail: (err) => {
          console.error('云端订阅记录失败', err)
        }
      })
    }

    this.setData({ subscribed: true })
    wx.showToast({ title: '订阅成功，将提前提醒你', icon: 'success' })
  },

  // 仅保存到本地（云开发未就绪时的降级方案）
  saveSubscriptionLocal() {
    const activityId = this.data.activity._id
    const subs = wx.getStorageSync('subscriptions') || []
    if (!subs.includes(activityId)) {
      subs.push(activityId)
      wx.setStorageSync('subscriptions', subs)
    }
    this.setData({ subscribed: true })
  },

  unsubscribe() {
    const activityId = this.data.activity._id
    const subs = wx.getStorageSync('subscriptions') || []
    const newSubs = subs.filter(id => id !== activityId)
    wx.setStorageSync('subscriptions', newSubs)

    if (wx.cloud && wx.cloud.callFunction) {
      wx.cloud.callFunction({
        name: 'subscribe',
        data: {
          action: 'cancel',
          activityId: activityId
        }
      })
    }

    this.setData({ subscribed: false })
    wx.showToast({ title: '已取消订阅', icon: 'none' })
  },

  onCopyLink() {
    wx.setClipboardData({
      data: this.data.activity.link || '',
      success: () => {
        wx.showToast({ title: '链接已复制', icon: 'success' })
      }
    })
  },

  onShareAppMessage() {
    return {
      title: this.data.activity.title,
      path: `/pages/detail/detail?id=${this.data.activity._id}`
    }
  }
})
