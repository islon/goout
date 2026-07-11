// cloudfunctions/getActivities/index.js
// 获取活动列表云函数（从云数据库读取，或返回本地数据）
// 首次使用时需要先导入数据到云数据库

const cloud = require('wx-server-sdk')
cloud.init({ env: cloud.DYNAMIC_CURRENT_ENV })

const db = cloud.database()

exports.main = async (event, context) => {
  const { category, city, fee, familyOnly, page = 1, pageSize = 50 } = event

  // 构建查询条件
  const where = {}
  
  // 只查今天及以后的活动
  const today = new Date()
  today.setHours(0, 0, 0, 0)
  // 注意：云数据库日期查询需要用 db.command
  const _ = db.command
  where.end_date = _.gte(today)

  if (category && category !== '全部') {
    where.category = category
  }
  if (city && city !== '全部') {
    where.city = city
  }
  if (fee === '免费') {
    where.fee = _.in(['免费', '免费需预约'])
  } else if (fee === '收费') {
    where.fee = _.in(['收费', '需购票'])
  }
  if (familyOnly) {
    where.family_friendly = true
  }

  try {
    const countResult = await db.collection('activities')
      .where(where)
      .count()
    
    const total = countResult.total

    const listResult = await db.collection('activities')
      .where(where)
      .orderBy('start_date', 'asc')
      .skip((page - 1) * pageSize)
      .limit(pageSize)
      .get()

    return {
      success: true,
      data: listResult.data,
      total: total,
      page: page,
      pageSize: pageSize,
      hasMore: (page * pageSize) < total
    }
  } catch (err) {
    // 如果集合不存在（首次使用），返回提示
    console.error('查询失败', err)
    return {
      success: false,
      error: err.message,
      hint: '请先在小程序云开发控制台创建 activities 集合并导入数据'
    }
  }
}
