// cloudfunctions/getActivities/index.js
// 实时拉取 GitHub Pages 上的活动数据，转发给小程序前端。
// 这样网页（goout 仓库）更新后，小程序自动跟随，无需改代码、无需重新上传。
// 本地 activities.json 仅作兜底（见前端逻辑）。

const cloud = require('wx-server-sdk')
cloud.init({ env: cloud.DYNAMIC_CURRENT_ENV })

const https = require('https')

// 网页数据地址（与 Web 版同源）
const DATA_URL = 'https://islon.github.io/goout/output/exhibitions.json'

function fetchActivities() {
  return new Promise((resolve, reject) => {
    const req = https.get(DATA_URL, { timeout: 8000 }, (res) => {
      if (res.statusCode !== 200) {
        reject(new Error('HTTP ' + res.statusCode))
        res.resume()
        return
      }
      let raw = ''
      res.setEncoding('utf8')
      res.on('data', (chunk) => { raw += chunk })
      res.on('end', () => {
        try {
          const data = JSON.parse(raw)
          resolve(Array.isArray(data) ? data : [])
        } catch (e) {
          reject(e)
        }
      })
    })
    req.on('timeout', () => {
      req.destroy(new Error('请求超时'))
    })
    req.on('error', (err) => reject(err))
  })
}

exports.main = async (event, context) => {
  const { category, city, fee, familyOnly, district, page = 1, pageSize = 9999 } = event

  let list
  try {
    list = await fetchActivities()
  } catch (err) {
    console.error('拉取线上数据失败', err)
    return {
      success: false,
      error: err.message,
      hint: '云函数拉取网页数据失败，前端将降级使用本地 activities.json'
    }
  }

  // 服务端预筛（减少回包体积）；精细筛选仍在前端做
  let result = list
  const _ = (city && city !== '全部') ? city : null
  if (_) result = result.filter(a => a.city === _)
  if (district && district !== 'all') result = result.filter(a => a.district === district)
  // 分类：云端用 type 字段（旧数据用 category 兜底）
  if (category && category !== '全部') result = result.filter(a => (a.type || a.category) === category)
  if (fee === '免费') result = result.filter(a => ['免费', '免费需预约'].includes(a.fee))
  else if (fee === '收费') result = result.filter(a => !['免费', '免费需预约'].includes(a.fee))
  // 亲子：云端用 is_family_friendly（旧数据用 family_friendly 兜底）
  if (familyOnly) result = result.filter(a => a.is_family_friendly === true || a.family_friendly === true)

  return {
    success: true,
    total: result.length,
    data: result,
    updatedAt: new Date().toISOString()
  }
}
