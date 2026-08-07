# -*- coding: utf-8 -*-
"""
为「仍缺官方链接」的场馆补全官网直链 venue_url。

本批新增（经 WebSearch + WebFetch / 政府/文物局登记信息核实）：
  国家体育场(鸟巢)      -> https://www.n-s.cn/            (国家体育场官网)
  中华世纪坛            -> https://www.worldartmuseum.cn/ (国家文物局登记域名)
  华熙LIVE·五棵松       -> https://wks.bloomagelive.com/live/  (华熙国际场馆站)
  中国光谷科技会展中心   -> http://www.covcec.com/         (场馆官网)
  成都永陵博物馆(综合馆) -> https://www.cdylbwg.org.cn/    (博物馆官网)
  南京银杏湖乐园        -> http://www.gingkolake.com/      (景区官网)

规则：仅当记录当前 venue_url 为空时才写入（不覆盖已有官方链接），
幂等可重复运行。link/url 字段保持不变（仍指向活动来源页，作为三方兜底）。
"""
import json
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")

# (场馆名子串, 官方链接)
MAPPING = [
    ("国家体育场", "https://www.n-s.cn/"),
    ("中华世纪坛", "https://www.worldartmuseum.cn/"),
    ("华熙LIVE·五棵松", "https://wks.bloomagelive.com/live/"),
    ("中国光谷科技会展中心", "http://www.covcec.com/"),
    ("成都永陵博物馆", "https://www.cdylbwg.org.cn/"),
    ("南京银杏湖乐园", "http://www.gingkolake.com/"),
]

ADDED_AT = "2026-07-19"


def main():
    total_changed = 0
    per_venue = {}
    for fname in sorted(os.listdir(OUTPUT_DIR)):
        if not fname.startswith("exhibitions_") or not fname.endswith(".json"):
            continue
        path = os.path.join(OUTPUT_DIR, fname)
        data = json.load(open(path, encoding="utf-8"))
        changed = 0
        for rec in data:
            if not isinstance(rec, dict):
                continue
            venue = rec.get("venue", "") or ""
            if not venue:
                continue
            for substr, url in MAPPING:
                if substr in venue:
                    # 仅当当前没有官方链接时写入
                    if not rec.get("venue_url"):
                        rec["venue_url"] = url
                        changed += 1
                        per_venue[substr] = per_venue.get(substr, 0) + 1
                    break
        if changed:
            json.dump(data, open(path, "w", encoding="utf-8"),
                      ensure_ascii=False, indent=2)
        total_changed += changed
        if changed:
            print(f"{fname}: +{changed} 条 venue_url")

    print(f"\n合计新增 venue_url: {total_changed} 条")
    for k, v in per_venue.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
