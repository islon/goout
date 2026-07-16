"""数据导入脚本 - 从 JSON 文件导入场馆和活动数据到 SQLite"""

import json
import sqlite3
import os
import sys
import re

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from db_init import DB_PATH, CITY_DATA, VENUE_TYPES, ACTIVITY_CATEGORIES, ACTIVITY_FEES
from district_map import resolve_district

# ============================================================================
# 合规检测 - 导入前过滤敏感内容
# ============================================================================

SENSITIVE_WORDS = [
    # 政治敏感词
    '台独', '藏独', '疆独', '港独', '蒙独',
    '法轮功', '法轮', 'FLG', 'flg',
    '六四', '6.4', '64事件',
    '反共', '灭共', '推翻共产党',
    '邪教', '呼喊派', '全能神', '实际神',
    # 暴力恐怖
    '恐怖袭击', '爆炸袭击', 'ISIS', '伊斯兰国', '基地组织', '塔利班',
    # 色情低俗
    '嫖娼', '卖淫', '招嫖', '约炮', '一夜情', '淫秽', '强奸',
    # 毒品
    '毒品购买', '冰毒', '海洛因', '摇头丸', 'K粉',
    # 赌博
    '网络赌博', '在线博彩', '百家乐', '六合彩',
    # 地区主权
    '中华民国', '台湾共和国', '西藏国', '东突厥斯坦',
]

WHITELIST = [
    '天安门东站', '天安门西站', '天安门东', '天安门西',
    '国家博物馆', '故宫博物院', '天安门广场',
    '农民运动讲习所', '农讲所',
]

def is_compliant(text):
    """检测文本是否合规"""
    if not text or not isinstance(text, str):
        return True

    # 白名单优先
    for w in WHITELIST:
        if w in text:
            return True

    # 检测敏感词
    lower = text.lower()
    for w in SENSITIVE_WORDS:
        if w.lower() in lower:
            return False
    return True

def check_record(record, text_fields):
    """检测记录是否合规"""
    for field in text_fields:
        if field in record and record[field]:
            if not is_compliant(str(record[field])):
                return False
    return True

VENUE_INFO_FILE = os.path.join(PROJECT_ROOT, 'output', 'venue_info.json')
EXHIBITIONS_FILE = os.path.join(PROJECT_ROOT, 'output', 'exhibitions.json')


def ensure_district(cursor, city_id, district_name):
    """按区县名查到或新建 district 行，返回 district_id；district_name 无效则返回 None。"""
    if not district_name or district_name == '其他':
        return None
    cursor.execute(
        'SELECT id FROM districts WHERE city_id = ? AND name = ?',
        (city_id, district_name),
    )
    row = cursor.fetchone()
    if row:
        return row[0]
    cursor.execute(
        'INSERT INTO districts (city_id, name) VALUES (?, ?)',
        (city_id, district_name),
    )
    return cursor.lastrowid


def import_data():
    """从 JSON 导入场馆和活动数据"""
    if not os.path.exists(VENUE_INFO_FILE):
        print(f'错误: 场馆数据文件不存在: {VENUE_INFO_FILE}')
        return
    if not os.path.exists(EXHIBITIONS_FILE):
        print(f'错误: 活动数据文件不存在: {EXHIBITIONS_FILE}')
        return

    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()

    # 构建 city_code → city_id 映射
    cursor.execute('SELECT id, code FROM cities')
    city_map = {row[1]: row[0] for row in cursor.fetchall()}

    # 构建 venue_type → type_id 映射
    cursor.execute('SELECT id, name FROM venue_types')
    type_map = {row[1]: row[0] for row in cursor.fetchall()}

    # 构建 category → id 和 fee → id 映射
    cursor.execute('SELECT id, name FROM activity_categories')
    category_map = {row[1]: row[0] for row in cursor.fetchall()}
    cursor.execute('SELECT id, name FROM activity_fees')
    fee_map = {row[1]: row[0] for row in cursor.fetchall()}

    # === 导入场馆 ===
    print('=== 导入场馆数据 ===')
    with open(VENUE_INFO_FILE, 'r', encoding='utf-8') as f:
        venues = json.load(f)

    # 合规检测
    venue_fields = ['name', 'address', 'transport', 'fee', 'description', 'highlights']
    original_venue_count = len(venues)
    venues = [v for v in venues if check_record(v, venue_fields)]
    filtered_venue_count = original_venue_count - len(venues)
    if filtered_venue_count > 0:
        print(f'合规过滤: 移除 {filtered_venue_count} 条不合规场馆')

    venue_name_map = {}  # name → venue_id
    for v in venues:
        city_code = v.get('city', 'shenzhen')
        city_id = city_map.get(city_code, city_map.get('shenzhen', 1))
        type_name = v.get('type', '其他')
        type_id = type_map.get(type_name) or _get_or_create(cursor, 'venue_types', type_name)
        district_name = resolve_district(v.get('city'), v.get('source'), v.get('name'),
                                         v.get('address'), v.get('description'))
        district_id = ensure_district(cursor, city_id, district_name)
        highlights = json.dumps(v.get('highlights', []), ensure_ascii=False) if v.get('highlights') else None

        cursor.execute('''
            INSERT OR IGNORE INTO venues
                (name, source, city_id, district_id, type_id, address, transport,
                 fee, description, official_url, highlights)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            v['name'], v.get('source'), city_id, district_id, type_id,
            v.get('address'), v.get('transport'), v.get('fee'),
            v.get('description'), v.get('official_url'), highlights,
        ))

        if cursor.lastrowid > 0:
            venue_name_map[v['name']] = cursor.lastrowid
        else:
            cursor.execute(
                'SELECT id FROM venues WHERE name = ? AND city_id = ?',
                (v['name'], city_id),
            )
            row = cursor.fetchone()
            if row:
                venue_name_map[v['name']] = row[0]

    conn.commit()
    print(f'导入场馆: {len(venue_name_map)} 个')

    # === 导入活动 ===
    print('=== 导入活动数据 ===')
    with open(EXHIBITIONS_FILE, 'r', encoding='utf-8') as f:
        exhibitions = json.load(f)

    # 合规检测
    activity_fields = ['title', 'venue', 'description', 'fee', 'contact']
    original_activity_count = len(exhibitions)
    exhibitions = [e for e in exhibitions if check_record(e, activity_fields)]
    filtered_activity_count = original_activity_count - len(exhibitions)

    # 预统计每个场馆的最佳（非空）区县，避免活动顺序导致孤儿场馆区县为空
    venue_best_district = {}
    for e in exhibitions:
        vn = e.get('venue', '')
        d = e.get('district')
        if vn and d and d != '其他' and vn not in venue_best_district:
            venue_best_district[vn] = d
    if filtered_activity_count > 0:
        print(f'合规过滤: 移除 {filtered_activity_count} 条不合规活动')

    imported_count = 0
    skipped_count = 0

    for e in exhibitions:
        venue_name = e.get('venue', '')
        if not venue_name:
            skipped_count += 1
            continue

        city_code = e.get('city', 'shenzhen')
        city_id = city_map.get(city_code, city_map.get('shenzhen', 1))

        # 活动中的场馆可能不在 venue_info.json 里，自动创建
        if venue_name not in venue_name_map:
            cursor.execute(
                'INSERT OR IGNORE INTO venues (name, city_id) VALUES (?, ?)',
                (venue_name, city_id),
            )
            cursor.execute(
                'SELECT id FROM venues WHERE name = ? AND city_id = ?',
                (venue_name, city_id),
            )
            row = cursor.fetchone()
            if row:
                venue_name_map[venue_name] = row[0]
                # 孤儿场馆：用其活动里最具体的 district 回填区县（activities 表无 district 列）
                did = ensure_district(cursor, city_id, venue_best_district.get(venue_name))
                if did:
                    cursor.execute('UPDATE venues SET district_id = ? WHERE id = ?', (did, row[0]))

        venue_id = venue_name_map.get(venue_name)
        if not venue_id:
            skipped_count += 1
            continue

        category_name = e.get('category', '其他')
        category_id = category_map.get(category_name) or _get_or_create(cursor, 'activity_categories', category_name)

        fee_name = e.get('fee', '免费')
        fee_id = fee_map.get(fee_name) or _get_or_create(cursor, 'activity_fees', fee_name)

        try:
            cursor.execute('''
                INSERT OR IGNORE INTO activities
                    (title, venue_id, city_id, category_id, fee_id,
                     start_date, end_date, link, description, contact,
                     family_friendly, source)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                e.get('title', ''), venue_id, city_id, category_id, fee_id,
                e.get('start_date', '2000-01-01'), e.get('end_date', '2099-12-31'),
                e.get('link', ''), e.get('description'), e.get('contact'),
                1 if e.get('family_friendly') else 0, e.get('source'),
            ))
            if cursor.rowcount > 0:
                imported_count += 1
            else:
                skipped_count += 1
        except Exception as ex:
            skipped_count += 1
            print(f'  跳过: {e.get("title", "")[:50]} - {str(ex)[:80]}')

    conn.commit()

    cursor.execute('SELECT COUNT(*) FROM venues')
    venue_count = cursor.fetchone()[0]
    cursor.execute('SELECT COUNT(*) FROM activities')
    activity_count = cursor.fetchone()[0]
    conn.close()

    print(f'导入活动: {imported_count} 条, 跳过: {skipped_count} 条')
    print(f'\n=== 导入完成 ===')
    print(f'场馆总数: {venue_count}')
    print(f'活动总数: {activity_count}')
    print(f'数据库: {DB_PATH}')


def _get_or_create(cursor, table, name):
    """查不到就插入，返回 id"""
    cursor.execute(f'SELECT id FROM {table} WHERE name = ?', (name,))
    row = cursor.fetchone()
    if row:
        return row[0]
    cursor.execute(f'INSERT INTO {table} (name) VALUES (?)', (name,))
    return cursor.lastrowid


if __name__ == '__main__':
    import_data()
