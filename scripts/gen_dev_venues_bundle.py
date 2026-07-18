#!/usr/bin/env python3
"""生成开发者工具专用的本地全量场馆文件（miniprogram/data/venues_dev.js）。

用途：本机若运行企业 SSL 代理(如 aTrust)，微信开发者工具的 Chromium 内核会因不信任其根证书，
到 jsDelivr/raw 的 HTTPS 握手被重置(net_error -101)，导致远程场馆拉取失败、长期停在打包兜底(378)。
开发者工具本地运行不限制主包大小，故直接内置一份全量场馆，让本地验证场馆逻辑/UI 时无需联网。
该文件通过 project.config.json 的 packOptions.ignore 在「上传发布」时自动剔除，不影响真机体积。
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'output', 'venue_info.json')
OUT = os.path.join(ROOT, 'miniprogram', 'data', 'venues_dev.js')


def main():
    with open(SRC, 'r', encoding='utf-8') as f:
        venues = json.load(f)
    if not isinstance(venues, list):
        raise SystemExit('venue_info.json 不是数组')
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write('// 自动生成：开发者工具专用本地全量场馆（上传发布时由 packOptions.ignore 排除）。\n')
        f.write('// 生成脚本：scripts/gen_dev_venues_bundle.py\n')
        f.write('module.exports = ')
        json.dump(venues, f, ensure_ascii=False, separators=(',', ':'))
        f.write(';\n')
    print('已生成 %s，共 %d 条场馆' % (OUT, len(venues)))


if __name__ == '__main__':
    main()
