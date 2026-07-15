"""数据库初始化脚本 - 创建表结构和索引"""

import sqlite3
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(PROJECT_ROOT, 'data', 'goout.db')

CITY_DATA = {
    'shenzhen': {'name': '深圳', 'province': '广东'},
    'guangzhou': {'name': '广州', 'province': '广东'},
    'shanghai': {'name': '上海', 'province': '上海'},
    'beijing': {'name': '北京', 'province': '北京'},
    'hangzhou': {'name': '杭州', 'province': '浙江'},
}

VENUE_TYPES = [
    '博物馆', '美术馆', '科技馆', '图书馆', '公园', '青少年宫',
    '文化馆', '体育中心', '演出场馆', '商业综合体', '会展中心',
    '文化中心', '民俗馆', '科普馆', '规划馆', '湿地', '其他',
]

ACTIVITY_CATEGORIES = [
    '展览', '讲座阅读', '科普活动', '演出', '体育赛事', '亲子活动',
    '影视放映', '市集', '研学活动', '论坛', '培训课程', '其他',
]

ACTIVITY_FEES = [
    '免费', '免费需预约', '收费', '部分免费', '需购票',
]


def init_database():
    """初始化数据库：建表、建索引、插入基础数据"""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()

    # --- 建表 ---

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code VARCHAR(20) UNIQUE NOT NULL,
        name VARCHAR(50) NOT NULL,
        province VARCHAR(50),
        country VARCHAR(50) DEFAULT '中国',
        timezone VARCHAR(50) DEFAULT 'Asia/Shanghai',
        status INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS districts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_id INTEGER NOT NULL,
        name VARCHAR(50) NOT NULL,
        code VARCHAR(20),
        FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE CASCADE,
        UNIQUE(city_id, name)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS venue_types (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) UNIQUE NOT NULL,
        icon VARCHAR(50),
        color VARCHAR(20),
        description TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS venues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(200) NOT NULL,
        source VARCHAR(100),
        city_id INTEGER NOT NULL,
        district_id INTEGER,
        type_id INTEGER,
        address TEXT,
        transport TEXT,
        fee VARCHAR(50),
        description TEXT,
        official_url VARCHAR(500),
        latitude DECIMAL(10,7),
        longitude DECIMAL(10,7),
        highlights TEXT,
        status INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE CASCADE,
        FOREIGN KEY (district_id) REFERENCES districts(id) ON DELETE SET NULL,
        FOREIGN KEY (type_id) REFERENCES venue_types(id) ON DELETE SET NULL,
        UNIQUE(name, city_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS activity_categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) UNIQUE NOT NULL,
        icon VARCHAR(50),
        color VARCHAR(20),
        description TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS activity_fees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) UNIQUE NOT NULL,
        description TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS activities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(500) NOT NULL,
        venue_id INTEGER NOT NULL,
        city_id INTEGER NOT NULL,
        category_id INTEGER,
        fee_id INTEGER,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL,
        link VARCHAR(1000) NOT NULL,
        description TEXT,
        contact VARCHAR(200),
        family_friendly BOOLEAN DEFAULT 0,
        source VARCHAR(100),
        status INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (venue_id) REFERENCES venues(id) ON DELETE CASCADE,
        FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE CASCADE,
        FOREIGN KEY (category_id) REFERENCES activity_categories(id) ON DELETE SET NULL,
        FOREIGN KEY (fee_id) REFERENCES activity_fees(id) ON DELETE SET NULL,
        UNIQUE(title, venue_id, start_date)
    )
    ''')

    # --- 索引 ---

    cursor.execute('CREATE INDEX IF NOT EXISTS idx_activities_venue_id ON activities(venue_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_activities_city_id ON activities(city_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_activities_date ON activities(start_date, end_date)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_activities_family ON activities(family_friendly) WHERE family_friendly = 1')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_venues_city_id ON venues(city_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_venues_type_id ON venues(type_id)')

    # --- updated_at 触发器 ---

    for table in ['cities', 'venues', 'activities']:
        cursor.execute(f'''
        CREATE TRIGGER IF NOT EXISTS trg_{table}_updated_at
        AFTER UPDATE ON {table}
        FOR EACH ROW
        BEGIN
            UPDATE {table} SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
        END
        ''')

    # --- 基础数据 ---

    for code, info in CITY_DATA.items():
        cursor.execute(
            'INSERT OR IGNORE INTO cities (code, name, province) VALUES (?, ?, ?)',
            (code, info['name'], info['province']),
        )

    for vt in VENUE_TYPES:
        cursor.execute('INSERT OR IGNORE INTO venue_types (name) VALUES (?)', (vt,))

    for ac in ACTIVITY_CATEGORIES:
        cursor.execute('INSERT OR IGNORE INTO activity_categories (name) VALUES (?)', (ac,))

    for af in ACTIVITY_FEES:
        cursor.execute('INSERT OR IGNORE INTO activity_fees (name) VALUES (?)', (af,))

    conn.commit()
    conn.close()
    print(f"数据库初始化完成: {DB_PATH}")


if __name__ == '__main__':
    init_database()
