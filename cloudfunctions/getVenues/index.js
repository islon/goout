// cloudfunctions/getVenues/index.js
// 实时拉取 GitHub Pages 上的场馆指南数据，转发给小程序前端。
// 与 getActivities 同理：网页（goout 仓库）更新后，小程序自动跟随。
// 本地 venues.json 仅作兜底（见前端逻辑）。

const cloud = require('wx-server-sdk')
cloud.init({ env: cloud.DYNAMIC_CURRENT_ENV })

const https = require('https')

// 网页数据地址（与 Web 版同源）
const DATA_URL = 'https://islon.github.io/goout/output/venue_info.json'

function fetchVenues() {
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
          // 网页数据为「以 source 为 key 的对象」，转成数组并附带 id
          const list = Array.isArray(data)
            ? data
            : Object.keys(data).map(k => ({ id: k, ...data[k] }))
          resolve(list)
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
  const { city, type, keyword } = event

  let list
  try {
    list = await fetchVenues()
  } catch (err) {
    console.error('拉取线上场馆数据失败', err)
    return {
      success: false,
      error: err.message,
      hint: '云函数拉取网页场馆数据失败，前端将降级使用本地 venues.json'
    }
  }

  // 服务端预筛（减少回包体积）；精细筛选仍在前端做
  let result = list
  if (city && city !== '全部') result = result.filter(v => v.city === city)
  if (type && type !== '全部') result = result.filter(v => v.type === type)
  if (keyword) {
    const kw = String(keyword).toLowerCase()
    result = result.filter(v =>
      (v.name && v.name.toLowerCase().indexOf(kw) > -1) ||
      (v.address && v.address.toLowerCase().indexOf(kw) > -1)
    )
  }

  return {
    success: true,
    total: result.length,
    data: result,
    updatedAt: new Date().toISOString()
  }
}
