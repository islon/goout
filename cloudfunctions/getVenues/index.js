// cloudfunctions/getVenues/index.js
// 实时拉取 GitHub Pages 上的场馆指南数据，转发给小程序前端。
// 与 getActivities 同理：网页（goout 仓库）更新后，小程序自动跟随。
// 本地 venues.json 仅作兜底（见前端逻辑）。

const cloud = require('wx-server-sdk')
cloud.init({ env: cloud.DYNAMIC_CURRENT_ENV })

const https = require('https')

// ============================================================================
// 合规检测 - 过滤敏感内容
// ============================================================================

const SENSITIVE_WORDS = [
  '台独', '藏独', '疆独', '港独', '蒙独',
  '法轮功', '法轮', 'FLG', 'flg',
  '六四', '6.4', '64事件',
  '反共', '灭共', '推翻共产党',
  '邪教', '呼喊派', '全能神', '实际神',
  '恐怖袭击', '爆炸袭击', 'ISIS', '伊斯兰国', '基地组织', '塔利班',
  '嫖娼', '卖淫', '招嫖', '约炮', '一夜情', '淫秽', '强奸',
  '毒品购买', '冰毒', '海洛因', '摇头丸', 'K粉',
  '网络赌博', '在线博彩', '百家乐', '六合彩',
  '中华民国', '台湾共和国', '西藏国', '东突厥斯坦',
]

const WHITELIST = [
  '天安门东站', '天安门西站', '天安门东', '天安门西',
  '国家博物馆', '故宫博物院', '天安门广场',
  '农民运动讲习所', '农讲所',
]

function isCompliant(text) {
  if (!text || typeof text !== 'string') return true
  for (const w of WHITELIST) {
    if (text.includes(w)) return true
  }
  const lower = text.toLowerCase()
  for (const w of SENSITIVE_WORDS) {
    if (lower.includes(w.toLowerCase())) return false
  }
  return true
}

function filterRecord(record) {
  const fields = ['name', 'address', 'transport', 'fee', 'description', 'highlights']
  for (const f of fields) {
    if (record[f] && !isCompliant(String(record[f]))) {
      return false
    }
  }
  return true
}

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

  // 合规过滤（必须步骤）
  const originalCount = list.length
  list = list.filter(filterRecord)
  const filteredCount = originalCount - list.length
  if (filteredCount > 0) {
    console.log(`合规过滤: 移除 ${filteredCount} 条不合规场馆`)
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
    updatedAt: new Date().toISOString(),
    compliance: {
      checked: true,
      filtered: filteredCount
    }
  }
}
