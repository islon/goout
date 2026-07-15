/**
 * 合规检测工具 - 中国大陆内容合规性检测
 * 用于检测活动数据、场馆数据中的敏感内容
 */

// ============================================================================
// 敏感词库
// ============================================================================

const SENSITIVE_WORDS = {
  // 政治敏感词
  politics: [
    '台独', '藏独', '疆独', '港独', '蒙独',
    '法轮功', '法轮', 'FLG',
    '六四', '6.4', '64事件',
    '反共', '灭共', '推翻共产党',
    '邪教', '呼喊派', '全能神', '实际神',
    '达赖集团', '藏青会', '藏妇会',
    '热比娅', '世维会',
    '七不准', '七不讲',
    '新闻管制', '言论管制',
  ],

  // 暴力恐怖
  violence: [
    '恐怖袭击', '爆炸袭击', '自杀式袭击',
    'ISIS', '伊斯兰国', '基地组织', '塔利班',
    '恐怖分子', '恐怖主义',
    '自制炸弹', '炸弹制作', '炸药配方',
    '杀人方法', '自杀方法', '自杀指南',
  ],

  // 色情低俗
  pornography: [
    '嫖娼', '卖淫', '招嫖', '约炮', '一夜情',
    'AV女优', '成人影片', '情色电影',
    '淫秽', '淫乱', '乱伦',
    '强奸', '强暴', '迷奸',
    '裸聊', '裸体表演', '脱衣舞',
    '三级片', '毛片',
  ],

  // 毒品相关
  drugs: [
    '毒品购买', '毒品销售', '冰毒', '海洛因', '摇头丸',
    '大麻种子', '种植大麻', '制造毒品',
    '吸毒工具', '溜冰', '嗨场',
    'K粉', '可卡因', '安非他命',
  ],

  // 赌博相关
  gambling: [
    '网络赌博', '在线博彩', '澳门赌场',
    '百家乐', '轮盘赌', '老虎机赌博',
    '地下钱庄', '非法集资',
    '私彩', '六合彩', '时时彩',
  ],

  // 地区主权
  sovereignty: [
    '中华民国', '台湾共和国', '西藏国', '东突厥斯坦',
    '钓鱼岛是日本的', '南海是菲律宾的',
  ],
}

// 白名单 - 允许的正常词汇
const WHITELIST = [
  // 北京地铁站名
  '天安门东站', '天安门西站', '天安门东', '天安门西',
  // 场馆名
  '国家博物馆', '故宫博物院', '天安门广场',
  // 交通指引
  '地铁1号线天安门东站',
  // 革命历史场馆
  '农民运动讲习所', '农讲所',
]

// ============================================================================
// 检测函数
// ============================================================================

/**
 * 检测单条文本是否合规
 * @param {string} text 待检测文本
 * @returns {{isCompliant: boolean, matches: string[]}}
 */
function checkText(text) {
  if (!text || typeof text !== 'string') {
    return { isCompliant: true, matches: [] }
  }

  // 先检查白名单
  for (const item of WHITELIST) {
    if (text.includes(item)) {
      return { isCompliant: true, matches: [] }
    }
  }

  const matches = []

  for (const [category, words] of Object.entries(SENSITIVE_WORDS)) {
    for (const word of words) {
      if (text.toLowerCase().includes(word.toLowerCase())) {
        matches.push(word)
      }
    }
  }

  return {
    isCompliant: matches.length === 0,
    matches,
  }
}

/**
 * 检测单条记录是否合规
 * @param {Object} record 活动或场馆记录
 * @returns {{isCompliant: boolean, violations: Object[]}}
 */
function checkRecord(record) {
  const violations = []

  // 需要检测的文本字段
  const textFields = [
    'title', 'description', 'venue', 'address',
    'transport', 'fee', 'highlights', 'contact',
  ]

  for (const field of textFields) {
    if (record[field]) {
      const result = checkText(String(record[field]))
      if (!result.isCompliant) {
        violations.push({
          field,
          matches: result.matches,
        })
      }
    }
  }

  return {
    isCompliant: violations.length === 0,
    violations,
  }
}

/**
 * 过滤不合规记录（静默模式，只返回合规记录）
 * @param {Array} records 记录数组
 * @returns {Array} 过滤后的合规记录
 */
function filterCompliant(records) {
  if (!Array.isArray(records)) return []

  return records.filter(record => {
    const result = checkRecord(record)
    return result.isCompliant
  })
}

/**
 * 检测并返回结果（详细模式）
 * @param {Array} records 记录数组
 * @returns {{total: number, compliant: number, nonCompliant: number, details: Object[]}}
 */
function checkRecords(records) {
  if (!Array.isArray(records)) {
    return { total: 0, compliant: 0, nonCompliant: 0, details: [] }
  }

  const details = []
  let compliant = 0

  for (let i = 0; i < records.length; i++) {
    const result = checkRecord(records[i])
    if (result.isCompliant) {
      compliant++
    } else {
      details.push({
        index: i,
        title: records[i].title || records[i].name || `记录#${i}`,
        violations: result.violations,
      })
    }
  }

  return {
    total: records.length,
    compliant,
    nonCompliant: records.length - compliant,
    details,
  }
}

// ============================================================================
// 导出
// ============================================================================

module.exports = {
  checkText,
  checkRecord,
  checkRecords,
  filterCompliant,
  SENSITIVE_WORDS,
  WHITELIST,
}