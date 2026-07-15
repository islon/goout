"""童行 - 亲子活动数据 RESTful API 服务"""

import sqlite3
import json
import os
from contextlib import contextmanager
from typing import Optional, List

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(PROJECT_ROOT, 'data', 'goout.db')

app = FastAPI(title="童行 - 亲子活动数据 API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# 数据库连接管理
# ---------------------------------------------------------------------------

@contextmanager
def get_db():
    """数据库连接上下文管理器，自动关闭连接"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON')
    try:
        yield conn
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# Pydantic 模型
# ---------------------------------------------------------------------------

class Activity(BaseModel):
    id: int
    title: str
    venue_id: int
    venue_name: str
    city_id: int
    city_name: str
    category_id: Optional[int] = None
    category_name: Optional[str] = None
    fee_id: Optional[int] = None
    fee_name: Optional[str] = None
    start_date: str
    end_date: str
    link: str
    description: Optional[str] = None
    contact: Optional[str] = None
    family_friendly: bool
    source: Optional[str] = None
    created_at: str
    updated_at: str


class Venue(BaseModel):
    id: int
    name: str
    source: Optional[str] = None
    city_id: int
    city_name: str
    district_id: Optional[int] = None
    district_name: Optional[str] = None
    type_id: Optional[int] = None
    type_name: Optional[str] = None
    address: Optional[str] = None
    transport: Optional[str] = None
    fee: Optional[str] = None
    description: Optional[str] = None
    official_url: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    highlights: Optional[List[str]] = None
    created_at: str
    updated_at: str


class PaginatedActivities(BaseModel):
    total: int
    limit: int
    offset: int
    data: List[Activity]


class PaginatedVenues(BaseModel):
    total: int
    limit: int
    offset: int
    data: List[Venue]


# ---------------------------------------------------------------------------
# SQL 片段
# ---------------------------------------------------------------------------

VENUE_SELECT = '''
    SELECT v.id, v.name, v.source, v.city_id, c.name AS city_name,
           v.district_id, d.name AS district_name,
           v.type_id, vt.name AS type_name,
           v.address, v.transport, v.fee, v.description, v.official_url,
           v.latitude, v.longitude, v.highlights, v.created_at, v.updated_at
    FROM venues v
    JOIN cities c ON v.city_id = c.id
    LEFT JOIN districts d ON v.district_id = d.id
    LEFT JOIN venue_types vt ON v.type_id = vt.id
'''

ACTIVITY_SELECT = '''
    SELECT a.id, a.title, a.venue_id, v.name AS venue_name,
           a.city_id, c.name AS city_name,
           a.category_id, ac.name AS category_name,
           a.fee_id, af.name AS fee_name,
           a.start_date, a.end_date, a.link, a.description,
           a.contact, a.family_friendly, a.source, a.created_at, a.updated_at
    FROM activities a
    JOIN venues v ON a.venue_id = v.id
    JOIN cities c ON a.city_id = c.id
    LEFT JOIN activity_categories ac ON a.category_id = ac.id
    LEFT JOIN activity_fees af ON a.fee_id = af.id
'''


def _parse_highlights(venue: dict) -> dict:
    """将 highlights JSON 字符串转为列表"""
    if venue.get('highlights'):
        try:
            venue['highlights'] = json.loads(venue['highlights'])
        except (json.JSONDecodeError, TypeError):
            venue['highlights'] = []
    return venue


def _get_city_id(cursor, city_code: str) -> Optional[int]:
    """城市代码转城市 ID"""
    cursor.execute('SELECT id FROM cities WHERE code = ? AND status = 1', (city_code,))
    row = cursor.fetchone()
    return row['id'] if row else None


# ---------------------------------------------------------------------------
# 接口
# ---------------------------------------------------------------------------

@app.get("/")
def root():
    return {"message": "童行 - 亲子活动数据 API", "version": "1.0.0"}


@app.get("/health")
def health():
    """健康检查"""
    if not os.path.exists(DB_PATH):
        raise HTTPException(status_code=503, detail="数据库文件不存在")
    return {"status": "ok"}


@app.get("/api/cities", response_model=List[dict])
def get_cities():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, code, name, province FROM cities WHERE status = 1')
        return [dict(row) for row in cursor.fetchall()]


@app.get("/api/venues", response_model=PaginatedVenues)
def get_venues(
    city: Optional[str] = None,
    district: Optional[str] = None,
    type: Optional[str] = None,
    keyword: Optional[str] = None,
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    with get_db() as conn:
        cursor = conn.cursor()

        where = ['v.status = 1']
        params = []

        if city:
            city_id = _get_city_id(cursor, city)
            if city_id:
                where.append('v.city_id = ?')
                params.append(city_id)

        if district:
            where.append('d.name = ?')
            params.append(district)

        if type:
            where.append('vt.name = ?')
            params.append(type)

        if keyword:
            where.append('(v.name LIKE ? OR v.address LIKE ? OR v.description LIKE ?)')
            kw = f'%{keyword}%'
            params.extend([kw, kw, kw])

        where_clause = ' AND '.join(where)

        cursor.execute(f'SELECT COUNT(*) FROM venues v LEFT JOIN districts d ON v.district_id = d.id LEFT JOIN venue_types vt ON v.type_id = vt.id WHERE {where_clause}', params)
        total = cursor.fetchone()[0]

        cursor.execute(
            f'{VENUE_SELECT} WHERE {where_clause} ORDER BY v.name LIMIT ? OFFSET ?',
            params + [limit, offset],
        )
        rows = [_parse_highlights(dict(row)) for row in cursor.fetchall()]

        return {"total": total, "limit": limit, "offset": offset, "data": rows}


@app.get("/api/venues/{venue_id}", response_model=Venue)
def get_venue(venue_id: int):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(f'{VENUE_SELECT} WHERE v.id = ? AND v.status = 1', (venue_id,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="场馆不存在")
        return _parse_highlights(dict(row))


@app.get("/api/venues/{venue_id}/activities", response_model=List[Activity])
def get_venue_activities(
    venue_id: int,
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            f'{ACTIVITY_SELECT} WHERE a.venue_id = ? AND a.status = 1 AND a.end_date >= DATE(\'now\') ORDER BY a.start_date ASC LIMIT ? OFFSET ?',
            (venue_id, limit, offset),
        )
        return [dict(row) for row in cursor.fetchall()]


@app.get("/api/activities", response_model=PaginatedActivities)
def get_activities(
    city: Optional[str] = None,
    venue: Optional[int] = None,
    category: Optional[str] = None,
    fee: Optional[str] = None,
    family_friendly: Optional[bool] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    keyword: Optional[str] = None,
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    with get_db() as conn:
        cursor = conn.cursor()

        where = ['a.status = 1']
        params = []

        if city:
            city_id = _get_city_id(cursor, city)
            if city_id:
                where.append('a.city_id = ?')
                params.append(city_id)

        if venue:
            where.append('a.venue_id = ?')
            params.append(venue)

        if category:
            where.append('ac.name = ?')
            params.append(category)

        if fee:
            where.append('af.name = ?')
            params.append(fee)

        if family_friendly is not None:
            where.append('a.family_friendly = ?')
            params.append(1 if family_friendly else 0)

        if start_date:
            where.append('a.end_date >= ?')
            params.append(start_date)

        if end_date:
            where.append('a.start_date <= ?')
            params.append(end_date)

        if keyword:
            where.append('(a.title LIKE ? OR a.description LIKE ? OR v.name LIKE ?)')
            kw = f'%{keyword}%'
            params.extend([kw, kw, kw])

        where_clause = ' AND '.join(where)

        cursor.execute(
            f'SELECT COUNT(*) FROM activities a JOIN venues v ON a.venue_id = v.id LEFT JOIN activity_categories ac ON a.category_id = ac.id LEFT JOIN activity_fees af ON a.fee_id = af.id WHERE {where_clause}',
            params,
        )
        total = cursor.fetchone()[0]

        cursor.execute(
            f'{ACTIVITY_SELECT} WHERE {where_clause} ORDER BY a.start_date ASC LIMIT ? OFFSET ?',
            params + [limit, offset],
        )
        rows = [dict(row) for row in cursor.fetchall()]

        return {"total": total, "limit": limit, "offset": offset, "data": rows}


@app.get("/api/activities/{activity_id}", response_model=Activity)
def get_activity(activity_id: int):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(f'{ACTIVITY_SELECT} WHERE a.id = ? AND a.status = 1', (activity_id,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="活动不存在")
        return dict(row)


@app.get("/api/statistics")
def get_statistics():
    with get_db() as conn:
        cursor = conn.cursor()

        cursor.execute('SELECT COUNT(*) FROM venues WHERE status = 1')
        venue_count = cursor.fetchone()[0]

        cursor.execute('SELECT COUNT(*) FROM activities WHERE status = 1')
        activity_count = cursor.fetchone()[0]

        cursor.execute('SELECT COUNT(*) FROM cities WHERE status = 1')
        city_count = cursor.fetchone()[0]

        cursor.execute('''
            SELECT c.name, COUNT(a.id) AS activity_count
            FROM cities c
            LEFT JOIN activities a ON c.id = a.city_id AND a.status = 1
            GROUP BY c.id ORDER BY activity_count DESC
        ''')
        city_stats = [dict(row) for row in cursor.fetchall()]

        cursor.execute('''
            SELECT ac.name, COUNT(a.id) AS activity_count
            FROM activity_categories ac
            LEFT JOIN activities a ON ac.id = a.category_id AND a.status = 1
            GROUP BY ac.id ORDER BY activity_count DESC
        ''')
        category_stats = [dict(row) for row in cursor.fetchall()]

        cursor.execute('''
            SELECT af.name, COUNT(a.id) AS activity_count
            FROM activity_fees af
            LEFT JOIN activities a ON af.id = a.fee_id AND a.status = 1
            GROUP BY af.id ORDER BY activity_count DESC
        ''')
        fee_stats = [dict(row) for row in cursor.fetchall()]

        cursor.execute('''
            SELECT vt.name, COUNT(v.id) AS venue_count
            FROM venue_types vt
            LEFT JOIN venues v ON vt.id = v.type_id AND v.status = 1
            GROUP BY vt.id ORDER BY venue_count DESC
        ''')
        venue_type_stats = [dict(row) for row in cursor.fetchall()]

        return {
            "venue_count": venue_count,
            "activity_count": activity_count,
            "city_count": city_count,
            "by_city": city_stats,
            "by_category": category_stats,
            "by_fee": fee_stats,
            "by_venue_type": venue_type_stats,
        }


@app.get("/api/venue-types", response_model=List[dict])
def get_venue_types():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM venue_types ORDER BY name')
        return [dict(row) for row in cursor.fetchall()]


@app.get("/api/activity-categories", response_model=List[dict])
def get_activity_categories():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM activity_categories ORDER BY name')
        return [dict(row) for row in cursor.fetchall()]


@app.get("/api/activity-fees", response_model=List[dict])
def get_activity_fees():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM activity_fees ORDER BY name')
        return [dict(row) for row in cursor.fetchall()]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
