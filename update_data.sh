#!/bin/bash
# 童行数据自动更新脚本
# 运行所有爬虫，更新数据，推送到GitHub

cd /workspace/shenzhen-exhibitions

echo "=== 开始自动更新童行数据 ==="
echo "时间: $(date)"
echo ""

# 运行爬虫主脚本
python3 scripts/main.py

# 检查数据是否有效
if python3 -c "import json; json.load(open('output/exhibitions.json'))" 2>/dev/null; then
    echo "数据验证通过"
    
    # 提交并推送
    git add output/exhibitions.json output/exhibitions.ics output/exhibitions.rss
    git commit -m "chore: 自动更新活动数据 $(date '+%Y-%m-%d %H:%M')"
    git push
    echo "已推送到GitHub"
else
    echo "数据验证失败，不推送"
fi

echo "=== 更新完成 ==="
