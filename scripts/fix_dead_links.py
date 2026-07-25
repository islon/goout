#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复失效链接脚本

策略：
1. 对每个失效链接，测试 HTTPS 和 HTTP 两种方式
2. 如果 HTTP 可达（200-399），保留原链接（SSL 问题不影响链接有效性）
3. 如果具体页面 404 但根域名可达，替换为根域名 URL
4. 如果完全不可达，清空 link 字段（保留活动数据但不提供死链）
"""
import json
import re
import subprocess
import sys
import os
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FILE = os.path.join(PROJECT_ROOT, 'output', 'exhibitions.json')
MANUAL_DATA_FILE = os.path.join(PROJECT_ROOT, 'scripts', 'manual_data.json')


def curl_check(url, timeout=12):
    """测试 URL 可达性，返回 http_status 或 None。"""
    cmd = [
        'curl', '-sk', '-L', '-o', '/dev/null',
        '-w', '%{http_code}',
        '--connect-timeout', str(timeout),
        '--max-time', str(timeout + 8),
        '-A', 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        url
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 14)
        if result.returncode != 0:
            return None
        m = re.search(r'(\d{3})', result.stdout.strip())
        return int(m.group(1)) if m else None
    except Exception:
        return None


def test_url_comprehensive(url):
    """全面测试 URL，返回 (status, working_url)。
    
    返回:
        status: 'ok' | 'root_ok' | 'dead'
        working_url: 可达的 URL（如果 status != 'dead'）
    """
    if not url:
        return 'dead', None

    # 1. 尝试 HTTPS
    https_status = curl_check(url)
    if https_status is not None and 200 <= https_status < 400:
        return 'ok', url

    # 2. 尝试 HTTP
    if url.startswith('https://'):
        http_url = 'http://' + url[len('https://'):]
    elif url.startswith('http://'):
        http_url = url
    else:
        http_url = 'http://' + url

    http_status = curl_check(http_url)
    if http_status is not None and 200 <= http_status < 400:
        return 'ok', url  # 保留原 HTTPS 链接（HTTP 证明站点存活）

    # 3. 如果是具体页面，尝试根域名
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    if path:
        root_url = f'{parsed.scheme}://{parsed.netloc}/'
        root_https = curl_check(root_url)
        if root_https is not None and 200 <= root_https < 400:
            return 'root_ok', root_url

        root_http_url = f'http://{parsed.netloc}/'
        root_http = curl_check(root_http_url)
        if root_http is not None and 200 <= root_http < 400:
            return 'root_ok', root_url

    return 'dead', None


def main():
    print('[fix_dead_links] 读取数据...')
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 找出所有失效链接
    dead_activities = []
    for i, a in enumerate(data):
        v = a.get('verification', {})
        if v.get('status') == 'suspicious':
            dead_activities.append((i, a))

    print(f'[fix_dead_links] 失效链接活动: {len(dead_activities)} 条')

    # 收集所有唯一的失效 URL
    unique_urls = set()
    for _, a in dead_activities:
        link = a.get('link') or a.get('url') or ''
        if link:
            unique_urls.add(link)

    print(f'[fix_dead_links] 唯一失效 URL: {len(unique_urls)} 个')
    print(f'[fix_dead_links] 开始测试...')

    # 并发测试所有唯一 URL
    url_results = {}
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(test_url_comprehensive, url): url for url in unique_urls}
        completed = 0
        for future in as_completed(futures):
            url = futures[future]
            status, working_url = future.result()
            url_results[url] = (status, working_url)
            completed += 1
            if completed % 20 == 0 or completed == len(unique_urls):
                print(f'[fix_dead_links]   进度 {completed}/{len(unique_urls)}')

    # 统计测试结果
    ok_count = sum(1 for s, _ in url_results.values() if s == 'ok')
    root_ok_count = sum(1 for s, _ in url_results.values() if s == 'root_ok')
    dead_count = sum(1 for s, _ in url_results.values() if s == 'dead')
    print(f'[fix_dead_links] 测试结果: 原链接可达={ok_count}, 根域名可达={root_ok_count}, 完全失效={dead_count}')

    # 应用修复
    fixed_ok = 0
    fixed_root = 0
    fixed_dead = 0
    for idx, a in dead_activities:
        link = a.get('link') or a.get('url') or ''
        if not link:
            continue

        status, working_url = url_results.get(link, ('dead', None))

        if status == 'ok':
            # 链接实际可达（SSL 问题导致误判），更新验证状态
            a.setdefault('verification', {})
            a['verification']['status'] = 'auto_checked'
            a['verification']['link_reachable'] = True
            a['verification']['note'] = 'HTTP fallback verified'
            a['verified'] = True
            fixed_ok += 1

        elif status == 'root_ok':
            # 具体页面失效，替换为根域名
            a['link'] = working_url
            a['url'] = working_url
            if a.get('links'):
                a['links'] = [{'url': working_url, 'label': '活动详情'}]
            a.setdefault('verification', {})
            a['verification']['status'] = 'auto_checked'
            a['verification']['link_reachable'] = True
            a['verification']['note'] = f'Replaced dead page with root domain'
            a['verified'] = True
            fixed_root += 1

        else:
            # 完全失效，清空链接
            old_link = a.get('link', '')
            a['link'] = ''
            a['url'] = ''
            a['links'] = []
            a.setdefault('verification', {})
            a['verification']['status'] = 'unverified'
            a['verification']['link_reachable'] = False
            a['verification']['note'] = f'Dead link removed: {old_link[:80]}'
            a['verified'] = False
            fixed_dead += 1

    print(f'\n[fix_dead_links] 修复完成:')
    print(f'  原链接可达(SSL误判): {fixed_ok} 条')
    print(f'  替换为根域名: {fixed_root} 条')
    print(f'  清空死链: {fixed_dead} 条')

    # 保存主文件
    with open(INPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'[fix_dead_links] 已保存到 {INPUT_FILE}')

    # 同步到分城市文件
    output_dir = os.path.join(PROJECT_ROOT, 'output')
    city_files = [f for f in os.listdir(output_dir) if f.startswith('exhibitions_') and f.endswith('.json') and 'past' not in f and 'recent' not in f]
    
    # 建立 key -> activity 映射
    by_key = {}
    for a in data:
        key = f"{a.get('city','')}|{a.get('name') or a.get('title','')}|{a.get('start_date','')}"
        by_key[key] = a

    synced = 0
    for cf in city_files:
        cf_path = os.path.join(output_dir, cf)
        try:
            with open(cf_path, 'r', encoding='utf-8') as f:
                arr = json.load(f)
            changed = False
            for rec in arr:
                key = f"{rec.get('city','')}|{rec.get('name') or rec.get('title','')}|{rec.get('start_date','')}"
                ref = by_key.get(key)
                if ref:
                    if rec.get('link') != ref.get('link') or rec.get('url') != ref.get('url'):
                        rec['link'] = ref.get('link', '')
                        rec['url'] = ref.get('url', '')
                        rec['links'] = ref.get('links', [])
                        rec['verification'] = ref.get('verification', {})
                        rec['verified'] = ref.get('verified', False)
                        changed = True
            if changed:
                with open(cf_path, 'w', encoding='utf-8') as f:
                    json.dump(arr, f, ensure_ascii=False, indent=2)
                synced += 1
        except Exception as e:
            print(f'[fix_dead_links] 同步 {cf} 失败: {e}')

    print(f'[fix_dead_links] 已同步到 {synced} 个分城市文件')

    # 输出完全失效的链接列表（便于后续手动修复）
    dead_list_path = os.path.join(output_dir, 'dead_links_removed.txt')
    with open(dead_list_path, 'w', encoding='utf-8') as f:
        f.write(f'# 完全失效链接清单 - 生成于 2026-07-25\n')
        f.write(f'# 以下链接 HTTP 和 HTTPS 均不可达，已从活动数据中移除\n\n')
        for url, (status, _) in sorted(url_results.items()):
            if status == 'dead':
                f.write(f'{url}\n')
    print(f'[fix_dead_links] 失效链接清单: {dead_list_path}')


if __name__ == '__main__':
    main()
