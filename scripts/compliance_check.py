#!/usr/bin/env python3
"""
合规检测脚本 - 中国大陆内容合规性检测
用于检测活动数据、场馆数据中的敏感内容

使用方式：
    python3 scripts/compliance_check.py output/exhibitions.json
    python3 scripts/compliance_check.py output/venue_info.json
"""

import json
import re
import sys
from pathlib import Path

# ============================================================================
# 敏感词库 - 根据中国法律法规和中国互联网内容审核标准制定
# ============================================================================

SENSITIVE_WORDS = {
    # 政治敏感
    "politics": [
        "台独", "藏独", "疆独", "港独", "蒙独",
        "法轮功", "法轮大法", "法轮", "FLG", "flg",
        "六四事件", "64事件", "六四屠杀",
        "反共", "灭共", "推翻共产党",
        "邪教", "呼喊派", "全能神", "实际神", "门徒会",
        "达赖集团", "藏青会", "藏妇会", "藏独分子",
        "热比娅", "世维会", "东突",
        "民运分子", "民联", "民阵",
        "新闻管制", "言论管制", "网络封锁",
        "反华势力", "反动组织",
        "自由西藏", "自由新疆", "自由香港", "自由台湾",
    ],

    # 暴力恐怖
    "violence": [
        "恐怖袭击", "爆炸袭击", "自杀式袭击", "人体炸弹",
        "ISIS", "伊斯兰国", "基地组织", "塔利班", "哈马斯",
        "恐怖分子", "恐怖主义", "极端主义",
        "自制炸弹", "炸弹制作", "炸药配方", "火药配方",
        "杀人方法", "自杀方法", "自杀指南", "自杀教程",
        "砍人", "灭门", "分尸", "食人",
        "校园枪击", "暴力袭击", "持刀伤人",
    ],

    # 色情低俗
    "pornography": [
        "嫖娼", "卖淫", "招嫖", "约炮", "一夜情", "援交",
        "AV女优", "成人影片", "情色电影", "色情电影",
        "淫秽", "淫乱", "乱伦", "奸淫",
        "强奸", "强暴", "迷奸", "诱奸", "轮奸",
        "裸聊", "裸体表演", "脱衣舞", "裸模",
        "三级片", "毛片", "黄片", "A片",
        "色情网站", "成人网站", "黄色网站",
        "自慰", "手淫", "性交", "性爱",
        "性奴", "性虐待",
    ],

    # 毒品相关
    "drugs": [
        "毒品购买", "毒品销售", "冰毒", "海洛因", "摇头丸",
        "大麻种子", "种植大麻", "制造毒品", "毒品制作",
        "吸毒工具", "溜冰毒", "嗨场",
        "K粉", "可卡因", "安非他命", "吗啡", "鸦片",
        " heroin", "cocaine", "marijuana",
        "毒贩", "吸毒者", "戒毒所",
    ],

    # 赌博相关
    "gambling": [
        "网络赌博", "在线博彩", "澳门赌场", "线上赌场",
        "百家乐", "轮盘赌", "老虎机", "牌九", "骰宝",
        "地下钱庄", "非法集资", "传销",
        "私彩", "六合彩", "时时彩", "快三",
        "赌博网站", "博彩网站",
        "赌球", "赌马", "赌石",
    ],

    # 迷信诈骗
    "fraud": [
        "算命大师", "风水大师", "改运大师", "算命先生",
        "包治百病", "根治癌症", "神奇疗效", "祖传秘方",
        "特效药", "秘方药", "神药", "仙丹",
        "代开发票", "办证刻章", "学历代办", "证件代办",
        "中奖诈骗", "电信诈骗", "网络诈骗",
        "传销组织", "直销诈骗",
        "消灾解难", "驱鬼辟邪",
    ],

    # 地区主权
    "sovereignty": [
        "中华民国", "台湾共和国", "西藏国", "东突厥斯坦",
        "钓鱼岛是日本的", "南海是菲律宾的",
        "台湾国", "香港国", "疆独",
        "台湾独立", "西藏独立", "新疆独立", "香港独立",
        "一中一台", "两个中国",
    ],

    # 广告营销（避免过度营销内容）
    "advertising": [
        "点击领取", "扫码关注", "加微信", "加好友",
        "微信号:", "加QQ",
        "限量抢购", "售完即止", "最后机会",
        "立即购买", "马上下单",
    ],
}

# 白名单 - 允许的正常词汇（避免误判）
# 格式：敏感词 -> [白名单词组列表]，当白名单词出现在同一段文本中时豁免
WHITELIST_MAP = {
    "鸦片": [
        "鸦片战争", "鸦片贸易", "鸦片历史",
    ],
    "法轮": [
        "法轮寺", "法轮殿", "法轮塔", "法轮经",
        "法轮常转", "转法轮",
    ],
    "邪教": [
        "反邪教", "防范邪教", "邪教警示", "邪教宣传",
    ],
    "恐怖": [
        "反恐", "反恐怖", "反恐演习", "反恐演练",
        "恐怖电影", "恐怖小说", "恐怖游戏", "鬼屋恐怖",
        "恐怖袭击事件", "反对恐怖",
    ],
    "赌博": [
        "反赌博", "禁止赌博", "严禁赌博", "赌博危害",
        "赌博机", "老虎机游戏",
    ],
    "毒品": [
        "禁毒", "反毒品", "毒品危害", "禁毒教育",
        "毒品预防", "禁毒宣传",
    ],
    "色情": [
        "反色情", "色情危害", "扫黄打非",
    ],
    "民运": [
        "农民运动", "农民运动讲习所", "农讲所",
        "工人运动", "学生运动", "五四运动",
    ],
    "天安门": [
        "天安门广场", "天安门东站", "天安门西站",
        "天安门城楼", "天安门东", "天安门西",
    ],
    "故宫": [
        "故宫博物院", "故宫",
    ],
    "国家博物馆": [
        "中国国家博物馆", "国家博物馆",
    ],
    "革命": [
        "辛亥革命", "革命历史", "革命纪念馆",
        "革命博物馆", "革命先烈", "革命传统",
        "农民运动", "工人运动",
    ],
    "自杀": [
        "自杀预防", "防止自杀", "自杀干预",
        "自杀率", "自杀事件",
    ],
    "强奸": [
        "强奸罪", "强奸案", "强奸犯",
        "反强奸", "防范强奸",
    ],
}

# 简单白名单（整词匹配，文本中包含即豁免）
SIMPLE_WHITELIST = [
    "国家博物馆", "故宫博物院", "天安门广场",
    "农民运动讲习所", "农讲所",
    "辛亥革命博物院", "辛亥革命纪念馆",
    "革命博物馆", "革命历史",
    "反恐", "禁毒", "扫黄打非", "反邪教",
    "鸦片战争", "鸦片贸易",
    "微信公众号",
    "网络诈骗", "电信诈骗", "中奖诈骗",
    "校园欺凌",
]

# ============================================================================
# 检测函数
# ============================================================================

def compile_patterns():
    """编译正则表达式"""
    patterns = {}
    for category, words in SENSITIVE_WORDS.items():
        if not words:
            continue
        escaped = [re.escape(w) for w in words]
        patterns[category] = re.compile('|'.join(escaped), re.IGNORECASE)
    return patterns

def is_whitelisted(text, matched_word=None):
    """
    检查文本是否在白名单中
    matched_word: 匹配到的敏感词，用于针对性白名单检查
    """
    if not text:
        return False

    text_lower = text.lower()

    # 简单白名单
    for item in SIMPLE_WHITELIST:
        if item.lower() in text_lower:
            return True

    # 映射白名单（针对特定敏感词的白名单）
    if matched_word:
        matched_lower = matched_word.lower()
        for key, whitelist_items in WHITELIST_MAP.items():
            if key.lower() in matched_lower or matched_lower in key.lower():
                for wl_item in whitelist_items:
                    if wl_item.lower() in text_lower:
                        return True

    return False

def check_text(text, patterns, return_details=False):
    """
    检测单条文本
    返回: (is_compliant, violations)
    """
    if not text or not isinstance(text, str):
        return True, []

    violations = []
    for category, pattern in patterns.items():
        matches = pattern.findall(text)
        if matches:
            valid_matches = []
            for m in matches:
                if not is_whitelisted(text, m):
                    valid_matches.append(m)
            if valid_matches:
                violations.append({
                    "category": category,
                    "matches": valid_matches
                })

    return len(violations) == 0, violations

def mask_text(text, patterns):
    """
    对文本中的敏感词进行脱敏替换（用*替换中间字符）
    返回: (脱敏后的文本, 替换数量)
    """
    if not text or not isinstance(text, str):
        return text, 0

    result = text
    total_masked = 0

    for category, pattern in patterns.items():
        def replace_fn(match):
            nonlocal total_masked
            word = match.group(0)
            if is_whitelisted(text, word):
                return word
            total_masked += 1
            if len(word) <= 2:
                return word[0] + '*'
            else:
                return word[0] + '*' * (len(word) - 2) + word[-1]

        result = pattern.sub(replace_fn, result)

    return result, total_masked

def mask_record(record, patterns, text_fields=None):
    """
    对单条记录中的敏感字段进行脱敏
    返回: (脱敏后的记录, 替换总数量)
    """
    if text_fields is None:
        text_fields = [
            "title", "description", "venue", "address",
            "transport", "fee", "highlights", "contact"
        ]

    masked_record = dict(record)
    total = 0

    for field in text_fields:
        if field in masked_record and masked_record[field]:
            masked_text, count = mask_text(str(masked_record[field]), patterns)
            if count > 0:
                masked_record[field] = masked_text
                total += count

    return masked_record, total

def check_record(record, patterns, record_type="activity"):
    """
    检测单条记录
    返回: (is_compliant, violations)
    """
    violations = []

    # 需要检测的文本字段
    text_fields = [
        "title", "description", "venue", "address",
        "transport", "fee", "highlights", "contact"
    ]

    for field in text_fields:
        if field in record and record[field]:
            is_ok, field_violations = check_text(str(record[field]), patterns)
            if not is_ok:
                for v in field_violations:
                    violations.append({
                        "field": field,
                        "value": str(record[field])[:100],  # 截断避免日志过长
                        "category": v["category"],
                        "matches": v["matches"]
                    })

    return len(violations) == 0, violations

def check_file(filepath, patterns):
    """
    检测整个文件
    返回: (total, compliant, violations_list)
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = [data]

    total = len(data)
    violations_list = []

    for i, record in enumerate(data):
        is_ok, violations = check_record(record, patterns)
        if not is_ok:
            violations_list.append({
                "index": i,
                "id": record.get("id") or record.get("name") or i,
                "title": record.get("title") or record.get("name") or f"记录#{i}",
                "violations": violations
            })

    return total, total - len(violations_list), violations_list

def mask_file(filepath, patterns, output_path=None):
    """
    对整个文件进行脱敏处理
    返回: (total, masked_count, output_path)
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    is_dict = isinstance(data, dict)
    records = [data] if is_dict else data

    total = len(records)
    total_masked = 0
    masked_records = []

    for record in records:
        masked_record, count = mask_record(record, patterns)
        masked_records.append(masked_record)
        total_masked += count

    result = masked_records[0] if is_dict else masked_records

    if output_path is None:
        output_path = filepath

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    return total, total_masked, output_path

def main():
    if len(sys.argv) < 2:
        print("用法: python3 scripts/compliance_check.py <数据文件.json> [--mask] [--output <文件>]")
        print("示例:")
        print("  python3 scripts/compliance_check.py output/exhibitions.json")
        print("  python3 scripts/compliance_check.py output/exhibitions.json --mask")
        print("  python3 scripts/compliance_check.py output/exhibitions.json --mask --output output/exhibitions_clean.json")
        sys.exit(1)

    args = sys.argv[1:]
    filepath = None
    do_mask = False
    output_path = None

    i = 0
    while i < len(args):
        arg = args[i]
        if arg == '--mask':
            do_mask = True
        elif arg == '--output':
            i += 1
            if i < len(args):
                output_path = args[i]
        elif arg.startswith('-'):
            print(f"未知参数: {arg}")
            sys.exit(1)
        else:
            filepath = Path(arg)
        i += 1

    if not filepath:
        print("错误: 请指定数据文件")
        sys.exit(1)

    if not filepath.exists():
        print(f"错误: 文件不存在 {filepath}")
        sys.exit(1)

    patterns = compile_patterns()

    if do_mask:
        print(f"开始脱敏处理: {filepath}")
        print("-" * 60)
        total, masked_count, out_path = mask_file(filepath, patterns, output_path)
        print(f"处理完成: 总计 {total} 条记录")
        print(f"脱敏替换: {masked_count} 处")
        print(f"输出文件: {out_path}")
        if masked_count > 0:
            print("⚠️  已对敏感内容进行脱敏处理")
        else:
            print("✅ 无需脱敏，所有内容合规")
        sys.exit(0)

    print(f"开始合规检测: {filepath}")
    print("-" * 60)

    total, compliant, violations = check_file(filepath, patterns)

    print(f"检测完成: 总计 {total} 条记录")
    print(f"合规: {compliant} 条 ({compliant/total*100:.1f}%)")
    print(f"不合规: {total - compliant} 条 ({(total-compliant)/total*100:.1f}%)")
    print()

    if violations:
        print("=" * 60)
        print("不合规记录详情:")
        print("=" * 60)
        for v in violations[:10]:  # 只显示前10条
            print(f"\n记录 #{v['index']}: {v['title']}")
            for detail in v['violations']:
                print(f"  - 字段 [{detail['field']}]: {detail['value'][:50]}...")
                print(f"    匹配敏感词: {detail['matches']} (类别: {detail['category']})")

        if len(violations) > 10:
            print(f"\n... 还有 {len(violations) - 10} 条不合规记录未显示")

    print()
    print("=" * 60)

    # 返回状态码
    if total - compliant > 0:
        print("⚠️  检测到不合规内容，请处理后再发布")
        sys.exit(1)
    else:
        print("✅ 所有内容合规")
        sys.exit(0)

if __name__ == "__main__":
    main()