"""
purge_auto_generated.py — 数据管线纵深防御：剔除所有 source === 'auto_generated' 的合成占位活动。

背景：
  历史版本曾用模板生成大量 source='auto_generated' 的占位活动（日期虚拟、场馆多为虚构、
  无官方链接），违反「数据必须真实」原则。当前爬虫（scripts/）已不再产生此类数据，但为
  防止未来某次爬虫改动/第三方逻辑误产出合成数据混入 output/，在 CI 管线爬虫之后、下游
  同步（小程序兜底 / ICS / 城市清单）之前做一道拦截：删除任何 auto_generated 条目。

覆盖范围：
  - output/exhibitions_*.json （各城市分文件）
  - output/exhibitions.json        （主文件，若存在）
  注：venue_info.json / cities.json 不含活动，无需处理；小程序兜底由 sync_miniprogram_data.py
      从已净化的 output 重新生成，故本步放在它之前即可保证兜底也干净。

行为：
  - 仅当确有剔除时才回写文件；
  - 打印被剔除条数；若 >0 以醒目 WARNING 提示（便于回溯是哪次爬虫产生了合成数据），
    但不中断管线（仍会把已净化数据提交，避免阻塞正常更新）。
"""
import os
import json
import glob

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")

# 参与活动清单的文件（排除场馆库 / 城市清单 / RSS / ICS）
ACTIVITY_FILE_PATTERNS = [
    os.path.join(OUTPUT_DIR, "exhibitions_*.json"),
    os.path.join(OUTPUT_DIR, "exhibitions.json"),
]

FAKE_SOURCE = "auto_generated"


def is_fake(ex):
    """判定是否为合成占位活动。"""
    if not isinstance(ex, dict):
        return False
    src = ex.get("source")
    if src == FAKE_SOURCE:
        return True
    # 防御：source 缺失但带 auto_generated 特征（无链接 + 无真实场馆）不在此处置，
    # 避免误删真实但信息不全的活动。仅精确匹配已知合成标记。
    return False


def purge_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return 0

    if isinstance(data, list):
        cleaned = [x for x in data if not is_fake(x)]
        removed = len(data) - len(cleaned)
        if removed:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(cleaned, f, ensure_ascii=False, indent=2)
        return removed
    elif isinstance(data, dict):
        # 兼容 {id: activity} 形式
        cleaned = {k: v for k, v in data.items() if not is_fake(v)}
        removed = len(data) - len(cleaned)
        if removed:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(cleaned, f, ensure_ascii=False, indent=2)
        return removed
    return 0


def main():
    files = []
    for pat in ACTIVITY_FILE_PATTERNS:
        for fp in glob.glob(pat):
            # 排除明显的非活动文件
            if fp.endswith("_all.json"):
                continue
            files.append(fp)

    total_removed = 0
    affected = []
    for path in sorted(set(files)):
        removed = purge_file(path)
        if removed:
            total_removed += removed
            affected.append((os.path.basename(path), removed))

    if total_removed == 0:
        print("[purge] 未发现 auto_generated 合成数据，output/ 已是纯净状态 ✓")
    else:
        print("=" * 60)
        print(f"[purge] WARNING: 检测到并剔除了 {total_removed} 条 auto_generated 合成活动！")
        for name, n in affected:
            print(f"           - {name}: 移除 {n} 条")
        print("           请核查最近的爬虫改动，确认为何产生了合成数据。")
        print("=" * 60)
    return total_removed


if __name__ == "__main__":
    main()
