// cloudfunctions/subscribe/index.js
// 订阅管理云函数：记录/取消用户的活动订阅

const cloud = require('wx-server-sdk')
cloud.init({ env: cloud.DYNAMIC_CURRENT_ENV })

const db = cloud.database()

exports.main = async (event, context) => {
  const { OPENID } = cloud.getWXContext()
  const { activityId, activityTitle, startDate, venue, action } = event

  // 取消订阅
  if (action === 'cancel') {
    try {
      const res = await db.collection('subscriptions')
        .where({
          openid: OPENID,
          activityId: activityId
        })
        .remove()
      return { success: true, removed: res.stats.removed }
    } catch (err) {
      console.error('取消订阅失败', err)
      return { success: false, error: err.message }
    }
  }

  // 添加订阅
  try {
    // 先检查是否已存在
    const existing = await db.collection('subscriptions')
      .where({
        openid: OPENID,
        activityId: activityId
      })
      .get()

    if (existing.data.length > 0) {
      return { success: true, message: '已订阅过', duplicate: true }
    }

    // 计算提醒时间：活动开始前 1 天的 9:00
    const activityDate = new Date(startDate)
    const remindTime = new Date(activityDate)
    remindTime.setDate(remindTime.getDate() - 1)
    remindTime.setHours(9, 0, 0, 0)

    await db.collection('subscriptions').add({
      data: {
        openid: OPENID,
        activityId: activityId,
        activityTitle: activityTitle,
        startDate: startDate,
        venue: venue,
        remindTime: remindTime,
        notified: false,
        createdAt: new Date()
      }
    })

    return { success: true, remindTime: remindTime }
  } catch (err) {
    console.error('订阅失败', err)
    return { success: false, error: err.message }
  }
}
