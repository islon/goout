#!/bin/bash
# 童行数据自动更新脚本
# 运行所有爬虫，同步小程序兜底数据，推送到GitHub
#
# 数据流向：
#   scripts/main.py → output/*.json（网页版 + 小程序运行时实时拉取）
#                 → miniprogram/data/*.js（小程序离线打包兜底，由本脚本同步）
#   一条命令，网页版 & 小程序同时更新

cd /workspace/goout 2>/dev/null || cd "$(dirname "$0")"

echo "=== 开始自动更新童行数据 ==="
echo "时间: $(date)"
echo ""

# 1. 运行爬虫主脚本 → 更新 output/
python3 scripts/main.py

# 1.5 区县映射补齐：给每条活动写入 district 字段，固化到数据层
#     避免下次爬虫覆盖（exhibitions.json 历史上无 district 字段，区县靠端上临时算）
python3 scripts/enrich_districts.py

# 2. 检查活动数据是否有效
if python3 -c "import json; json.load(open('output/exhibitions.json'))" 2>/dev/null; then
    echo "✅ 网页数据验证通过"
    
    # 3. 同步小程序打包兜底数据（output/ → miniprogram/data/）
    if [ -f "scripts/sync_miniprogram_data.py" ]; then
        echo ""
        python3 scripts/sync_miniprogram_data.py
    else
        echo "⚠️  同步脚本不存在，跳过小程序数据"
    fi
    
    # 4. 提交并推送（网页数据 + 小程序打包数据）
    git add output/exhibitions.json output/exhibitions.ics output/exhibitions.rss
    git add miniprogram/data/exhibitions.js miniprogram/data/venues.js 2>/dev/null || true
    git commit -m "chore: 自动更新活动数据 & 同步小程序兜底 $(date '+%Y-%m-%d %H:%M')"
    git push
    echo "✅ 已推送到 GitHub（网页版 + 小程序）"
else
    echo "❌ 数据验证失败，不推送"
fi

echo ""
echo "=== 更新完成 ==="
