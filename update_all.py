#!/usr/bin/env python3
"""
update_all.py — 一键更新所有数据（网页版 + 小程序）

数据流向：
  scripts/main.py → output/*.json（网页版 + 小程序运行时实时拉取）
                → miniprogram/data/*.js（小程序离线打包兜底）
  一条命令，网页版 & 小程序同时更新

用法：
    python3 update_all.py          # 完整更新并推送
    python3 update_all.py --no-push  # 只更新不推送
"""

import json
import os
import subprocess
import sys
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR


def run_step(step_name, cmd, cwd=None):
    """运行一个步骤，失败则退出"""
    print()
    print("=" * 60)
    print(f"  {step_name}")
    print("=" * 60)
    print(f"  命令: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    print()

    result = subprocess.run(
        cmd,
        cwd=cwd or PROJECT_ROOT,
        shell=isinstance(cmd, str)
    )

    if result.returncode != 0:
        print(f"\n❌ {step_name} 失败（退出码: {result.returncode}）")
        sys.exit(1)

    print(f"\n✅ {step_name} 完成")


def check_data_valid():
    """检查活动数据是否有效"""
    exhibitions_path = os.path.join(PROJECT_ROOT, 'output', 'exhibitions.json')
    if not os.path.exists(exhibitions_path):
        print(f"❌ 活动数据不存在: {exhibitions_path}")
        sys.exit(1)
    try:
        with open(exhibitions_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✅ 活动数据验证通过: {len(data)} 条")
        return True
    except Exception as e:
        print(f"❌ 活动数据验证失败: {e}")
        sys.exit(1)


def git_commit_and_push():
    """提交并推送所有更改"""
    print()
    print("=" * 60)
    print("  提交并推送到 GitHub")
    print("=" * 60)

    os.chdir(PROJECT_ROOT)

    # 检查是否有更改
    result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    if not result.stdout.strip():
        print("⚠️  没有需要提交的更改")
        return

    # 添加文件
    subprocess.run(['git', 'add', 'output/'], check=True)

    mini_files = [
        'miniprogram/data/exhibitions.js',
        'miniprogram/data/venues.js',
        'miniprogram/data/filters.js',
    ]
    for f in mini_files:
        if os.path.exists(os.path.join(PROJECT_ROOT, f)):
            subprocess.run(['git', 'add', f], check=False)

    # 提交
    commit_msg = f"chore: 自动更新活动数据 & 同步小程序兜底 {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    result = subprocess.run(['git', 'commit', '-m', commit_msg], capture_output=True, text=True)
    if result.returncode != 0:
        if 'nothing to commit' in result.stdout:
            print("⚠️  没有需要提交的更改")
            return
        print(f"❌ 提交失败: {result.stderr}")
        sys.exit(1)

    print(f"✅ 已提交: {commit_msg}")

    # 推送
    result = subprocess.run(['git', 'push'], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ 推送失败: {result.stderr}")
        sys.exit(1)

    print("✅ 已推送到 GitHub（网页版 + 小程序）")


def main():
    no_push = '--no-push' in sys.argv

    print("=" * 60)
    print("  童行数据一键更新")
    print(f"  时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if no_push:
        print("  模式: 只更新不推送")
    print("=" * 60)

    # 1. 运行爬虫主脚本
    run_step("第1步：运行爬虫，采集活动数据",
             ['python3', 'scripts/main.py'])

    # 2. 区县映射补齐
    run_step("第2步：区县映射补齐（写入 district 字段）",
             ['python3', 'scripts/enrich_districts.py'])

    # 3. 验证数据
    print()
    print("=" * 60)
    print("  第3步：验证活动数据")
    print("=" * 60)
    check_data_valid()

    # 4. 同步小程序打包兜底数据
    run_step("第4步：同步小程序打包兜底数据",
             ['python3', 'scripts/sync_miniprogram_data.py'])

    # 5. 动态生成筛选器映射表
    run_step("第5步：动态生成小程序筛选器映射表",
             ['python3', 'scripts/generate_filters.py'])

    # 6. 生成各城市 ICS 订阅文件
    if os.path.exists(os.path.join(PROJECT_ROOT, 'scripts', 'generate_city_ics.py')):
        run_step("第6步：生成各城市 ICS 订阅文件",
                 ['python3', 'scripts/generate_city_ics.py'])

    # 7. 生成网页/小程序统一城市清单
    if os.path.exists(os.path.join(PROJECT_ROOT, 'scripts', 'generate_cities_manifest.js')):
        run_step("第7步：生成网页/小程序统一城市清单",
                 ['node', 'scripts/generate_cities_manifest.js'])

    # 8. 提交并推送
    if not no_push:
        git_commit_and_push()
    else:
        print()
        print("=" * 60)
        print("  ⚠️  --no-push 模式：跳过提交推送")
        print("=" * 60)

    print()
    print("=" * 60)
    print("  🎉 全部更新完成！")
    print("=" * 60)


if __name__ == '__main__':
    main()
