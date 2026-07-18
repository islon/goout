// cloudfunctions/getActivities/index.js
// 实时拉取 GitHub Pages 上的活动数据，转发给小程序前端。
// 这样网页（goout 仓库）更新后，小程序自动跟随，无需改代码、无需重新上传。
// 本地 activities.json 仅作兜底（见前端逻辑）。

const cloud = require('wx-server-sdk')
cloud.init({ env: cloud.DYNAMIC_CURRENT_ENV })

const https = require('https')

// ============================================================================
// 合规检测 - 过滤敏感内容
// 词库与 compliance_check.py 保持同步
// ============================================================================

const SENSITIVE_WORDS = [
  // 政治敏感
  '台独', '藏独', '疆独', '港独', '蒙独',
  '法轮功', '法轮大法', '法轮', 'FLG', 'flg',
  '六四事件', '64事件',
  '反共', '灭共', '推翻共产党',
  '邪教', '呼喊派', '全能神', '实际神', '门徒会',
  '达赖集团', '藏青会', '藏妇会',
  '热比娅', '世维会', '东突',
  '民运分子', '民联', '民阵',
  '新闻管制', '言论管制',
  '反华势力', '反动组织',
  '自由西藏', '自由新疆', '自由香港', '自由台湾',
  // 暴力恐怖
  '恐怖袭击', '爆炸袭击', '自杀式袭击', '人体炸弹',
  'ISIS', '伊斯兰国', '基地组织', '塔利班',
  '恐怖分子', '恐怖主义',
  '自制炸弹', '炸弹制作', '炸药配方',
  '杀人方法', '自杀方法', '自杀指南',
  // 色情低俗
  '嫖娼', '卖淫', '招嫖', '约炮', '一夜情', '援交',
  'AV女优', '成人影片', '情色电影',
  '淫秽', '淫乱', '乱伦',
  '强奸', '强暴', '迷奸',
  '裸聊', '裸体表演', '脱衣舞',
  '三级片', '毛片', '黄片', 'A片',
  // 毒品
  '毒品购买', '毒品销售', '冰毒', '海洛因', '摇头丸',
  '大麻种子', '种植大麻', '制造毒品',
  '吸毒工具', '溜冰毒', '嗨场',
  'K粉', '可卡因', '安非他命',
  // 赌博
  '网络赌博', '在线博彩', '澳门赌场', '线上赌场',
  '百家乐', '轮盘赌', '老虎机',
  '地下钱庄', '非法集资', '传销',
  '私彩', '六合彩', '时时彩',
  // 地区主权
  '中华民国', '台湾共和国', '西藏国', '东突厥斯坦',
  '台湾国', '香港国',
  '台湾独立', '西藏独立', '新疆独立', '香港独立',
  '一中一台', '两个中国',
  // 迷信诈骗
  '算命大师', '风水大师', '改运大师',
  '包治百病', '根治癌症', '神奇疗效',
  '特效药', '秘方药', '神药',
  '代开发票', '办证刻章', '学历代办',
  '中奖诈骗', '电信诈骗', '网络诈骗',
  // 广告营销
  '点击领取', '扫码关注', '加微信', '加好友',
  '微信号:', '加QQ',
  '限量抢购', '售完即止', '最后机会',
  '立即购买', '马上下单',
]

const WHITELIST = [
  '天安门东站', '天安门西站', '天安门东', '天安门西',
  '天安门广场', '天安门城楼',
  '国家博物馆', '故宫博物院', '故宫',
  '农民运动讲习所', '农讲所',
  '辛亥革命博物院', '辛亥革命纪念馆',
  '革命博物馆', '革命历史', '革命先烈',
  '反恐', '禁毒', '扫黄打非', '反邪教',
  '法轮寺', '法轮殿', '法轮塔', '法轮经', '转法轮',
  '防范邪教', '反恐演习', '反恐演练',
  '恐怖电影', '恐怖小说', '恐怖游戏',
  '反赌博', '禁止赌博', '严禁赌博',
  '毒品危害', '禁毒教育', '禁毒宣传',
  '五四运动', '学生运动', '工人运动',
  '鸦片战争', '鸦片贸易',
  '微信公众号',
  '网络诈骗', '电信诈骗', '中奖诈骗',
  '校园欺凌',
]

function isCompliant(text) {
  if (!text || typeof text !== 'string') return true

  const lower = text.toLowerCase()

  // 白名单优先
  for (const w of WHITELIST) {
    if (lower.includes(w.toLowerCase())) return true
  }

  // 检测敏感词
  for (const w of SENSITIVE_WORDS) {
    if (lower.includes(w.toLowerCase())) return false
  }
  return true
}

function maskText(text) {
  if (!text || typeof text !== 'string') return text
  let result = text
  const lower = result.toLowerCase()

  // 白名单跳过
  for (const w of WHITELIST) {
    if (lower.includes(w.toLowerCase())) return text
  }

  for (const w of SENSITIVE_WORDS) {
    const regex = new RegExp(w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi')
    result = result.replace(regex, (match) => {
      if (match.length <= 2) return match[0] + '*'
      return match[0] + '*'.repeat(match.length - 2) + match[match.length - 1]
    })
  }
  return result
}

function maskRecord(record) {
  const fields = ['title', 'description', 'venue', 'address', 'transport', 'fee', 'contact']
  const masked = { ...record }
  for (const f of fields) {
    if (masked[f] && typeof masked[f] === 'string') {
      masked[f] = maskText(masked[f])
    }
  }
  return masked
}

function filterRecord(record) {
  const fields = ['title', 'description', 'venue', 'address', 'transport', 'fee', 'contact']
  for (const f of fields) {
    if (record[f] && !isCompliant(String(record[f]))) {
      return false
    }
  }
  return true
}

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

  // 合规过滤（必须步骤）
  const originalCount = list.length
  list = list.filter(filterRecord)
  const filteredCount = originalCount - list.length
  if (filteredCount > 0) {
    console.log(`合规过滤: 移除 ${filteredCount} 条不合规记录`)
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
    updatedAt: new Date().toISOString(),
    compliance: {
      checked: true,
      filtered: filteredCount
    }
  }
}
