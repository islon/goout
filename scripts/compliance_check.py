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
    # 政治敏感词
    "politics": [
        "台独", "藏独", "疆独", "港独", "蒙独",
        "法轮功", "法轮", "FLG", "flg",
        "六四", "6.4", "64事件",
        "反共", "灭共", "推翻共产党",
        "邪教", "呼喊派", "全能神", "实际神",
        "达赖集团", "藏青会", "藏妇会",
        "热比娅", "世维会",
        "民运", "民联", "民阵",
        "七不准", "七不讲",
        "新闻管制", "言论管制",
    ],

    # 暴力恐怖
    "violence": [
        "恐怖袭击", "爆炸袭击", "自杀式袭击",
        "ISIS", "伊斯兰国", "基地组织", "塔利班",
        "恐怖分子", "恐怖主义",
        "自制炸弹", "炸弹制作", "炸药配方",
        "杀人方法", "自杀方法", "自杀指南",
    ],

    # 色情低俗
    "pornography": [
        "嫖娼", "卖淫", "招嫖", "约炮", "一夜情",
        "AV女优", "成人影片", "情色电影",
        "淫秽", "淫乱", "乱伦",
        "强奸", "强暴", "迷奸",
        "裸聊", "裸体表演", "脱衣舞",
        "三级片", "毛片",
    ],

    # 毒品相关
    "drugs": [
        "毒品购买", "毒品销售", "冰毒", "海洛因", "摇头丸",
        "大麻种子", "种植大麻", "制造毒品",
        "吸毒工具", "溜冰", "嗨场",
        "K粉", "可卡因", "安非他命",
    ],

    # 赌博相关
    "gambling": [
        "网络赌博", "在线博彩", "澳门赌场",
        "百家乐", "轮盘赌", "老虎机赌博",
        "地下钱庄", "非法集资",
        "私彩", "六合彩", "时时彩",
    ],

    # 迷信诈骗
    "fraud": [
        "法轮功", "全能神", "呼喊派",
        "算命大师", "风水大师", "改运大师",
        "包治百病", "根治癌症", "神奇疗效",
        "特效药", "秘方药", "神药",
        "代开发票", "办证刻章", "学历代办",
    ],

    # 领导人相关
    "leaders": [
        # 避免直接列出领导人姓名的正则匹配，使用模糊匹配
    ],

    # 地区主权
    "sovereignty": [
        "中华民国", "台湾共和国", "西藏国", "东突厥斯坦",
        "钓鱼岛是日本的", "南海是菲律宾的",
    ],
}

# 白名单 - 允许的正常词汇（如地铁站名、场馆名等）
WHITELIST = [
    # 北京地铁站名
    "天安门东站", "天安门西站", "天安门东", "天安门西",
    # 场馆名中包含的正常词汇
    "国家博物馆", "故宫博物院", "天安门广场",
    # 交通指引
    "地铁1号线天安门东站",
    # 革命历史场馆（"民运"会误判"农民运动"）
    "农民运动讲习所", "农讲所",
]

# ============================================================================
# 检测函数
# ============================================================================

def compile_patterns():
    """编译正则表达式"""
    patterns = {}
    for category, words in SENSITIVE_WORDS.items():
        # 跳过空列表
        if not words:
            continue
        # 构建正则：匹配完整词汇（避免误判包含关系的正常词）
        escaped = [re.escape(w) for w in words]
        patterns[category] = re.compile('|'.join(escaped), re.IGNORECASE)
    return patterns

def is_whitelisted(text):
    """检查是否在白名单中"""
    for item in WHITELIST:
        if item in text:
            return True
    return False

def check_text(text, patterns):
    """
    检测单条文本
    返回: (is_compliant, violations)
    """
    if not text or not isinstance(text, str):
        return True, []

    # 先检查白名单
    if is_whitelisted(text):
        return True, []

    violations = []
    for category, pattern in patterns.items():
        matches = pattern.findall(text)
        if matches:
            violations.append({
                "category": category,
                "matches": matches
            })

    return len(violations) == 0, violations

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

def main():
    if len(sys.argv) < 2:
        print("用法: python3 scripts/compliance_check.py <数据文件.json>")
        print("示例: python3 scripts/compliance_check.py output/exhibitions.json")
        sys.exit(1)

    filepath = Path(sys.argv[1])
    if not filepath.exists():
        print(f"错误: 文件不存在 {filepath}")
        sys.exit(1)

    print(f"开始合规检测: {filepath}")
    print("-" * 60)

    patterns = compile_patterns()
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