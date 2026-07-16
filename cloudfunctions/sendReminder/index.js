// cloudfunctions/sendReminder/index.js
// 定时发送活动提醒云函数
// 配置为定时触发器：每天早上 8:00 执行一次
// 在云开发控制台 -> 云函数 -> 触发器 中配置，或通过 config.json

const cloud = require('wx-server-sdk')
cloud.init({ env: cloud.DYNAMIC_CURRENT_ENV })

const db = cloud.database()

exports.main = async (event, context) => {
  const now = new Date()
  
  // 查找需要发送提醒的订阅
  // 条件：提醒时间 <= 当前时间 且 尚未通知
  const _ = db.command
  try {
    const result = await db.collection('subscriptions')
      .where({
        remindTime: _.lte(now),
        notified: false
      })
      .get()

    console.log(`找到 ${result.data.length} 条待提醒订阅`)

    let successCount = 0
    let failCount = 0

    for (const sub of result.data) {
      try {
        // 发送订阅消息
        // 模板参数需要根据实际模板配置修改
        const sendResult = await cloud.openapi.subscribeMessage.send({
          touser: sub.openid,
          templateId: '请替换为你的订阅消息模板ID',
          // 跳转到活动详情页
          page: `pages/detail/detail?id=${sub.activityId}`,
          data: {
            // 以下字段需要根据你在小程序后台创建的模板来配置
            // 常见的「活动提醒」模板字段示例：
            thing1: {
              value: sub.activityTitle || '未知活动'
            },
            time2: {
              value: formatDate(sub.startDate)
            },
            thing3: {
              value: sub.venue || '待定'
            }
          },
          miniprogramState: 'formal'
        })

        console.log(`发送成功: ${sub.openid} - ${sub.activityTitle}`, sendResult)

        // 标记为已通知
        await db.collection('subscriptions')
          .doc(sub._id)
          .update({
            data: {
              notified: true,
              notifiedAt: new Date()
            }
          })

        successCount++
      } catch (err) {
        console.error(`发送失败: ${sub.openid} - ${sub.activityTitle}`, err)
        failCount++
      }
    }

    return {
      success: true,
      total: result.data.length,
      successCount,
      failCount,
      executeTime: now
    }
  } catch (err) {
    console.error('查询订阅失败', err)
    return { success: false, error: err.message }
  }
}

function formatDate(dateStr) {
  const d = new Date(dateStr)
  const y = d.getFullYear()
  const m = String(d.getMonth() + 1).padStart(2, '0')
  const day = String(d.getDate()).padStart(2, '0')
  return `${y}年${m}月${day}日`
}
