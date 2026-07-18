#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 output/data_meta.json —— 小程序「云端数据版本」清单。

内容：
  - version   : 由所有城市活动文件(exhibitions_{city}.json) + 城市场馆文件(venue_info_{city}.json)
                的内容哈希得出。数据内容不变 => version 不变；任一份文件变 => version 变。
  - updatedAt : 本次生成的时间（ISO 8601，UTC）。仅作展示/溯源，不参与版本比对。
  - activities: 活动总数
  - venues    : 场馆总数

小程序(app.js)启动时先拉这个极小文件(~200B)，比对本地缓存的 version：
  - 相同 => 云侧数据无变化，直接复用本地缓存，不再下载几 MB 的分城市大文件（省流量、秒开）。
  - 不同 => 有更新，下载最新数据并把新 version 落盘。
"""

import hashlib
import json
import glob
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(ROOT, 'output')


def _read_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def main():
    # 仅对「源数据」文件做哈希：10 城活动分文件 + 10 城场馆分文件。
    # 排除派生快照 recent/past（它们由城市文件生成，不应影响版本比对）。
    city_files = []
    for p in glob.glob(os.path.join(OUTPUT, 'exhibitions_*.json')):
        stem = os.path.splitext(os.path.basename(p))[0].split('_', 1)[1]
        if stem in ('recent', 'past'):
            continue
        city_files.append(p)
    venue_files = sorted(glob.glob(os.path.join(OUTPUT, 'venue_info_*.json')))

    all_files = sorted(city_files) + sorted(venue_files)

    h = hashlib.sha256()
    activities = 0
    venues = 0
    for p in all_files:
        h.update(p.encode('utf-8'))
        h.update(b'\x00')
        text = _read_text(p)
        h.update(text.encode('utf-8'))
        h.update(b'\x01')
        try:
            data = json.loads(text)
            if isinstance(data, list):
                if 'venue_info' in os.path.basename(p):
                    venues += len(data)
                else:
                    activities += len(data)
        except Exception:
            pass

    version = h.hexdigest()[:12]
    from datetime import datetime, timezone
    updated_at = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    meta = {
        'version': version,
        'updatedAt': updated_at,
        'activities': activities,
        'venues': venues
    }

    out_path = os.path.join(OUTPUT, 'data_meta.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
        f.write('\n')

    print('[data_meta] version=%s activities=%d venues=%d -> %s'
          % (version, activities, venues, out_path))


if __name__ == '__main__':
    main()
