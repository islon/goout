"""
generate_city_ics.py — 为 output/ 下每个分城市活动文件生成对应的 .ics 日历订阅文件。

产出：output/exhibitions_{city}.ics （与 about.js 小程序订阅页、schedule.html 的 webcal:// 链接对应）

运行：python3 scripts/generate_city_ics.py
依赖：仅标准库（不依赖第三方包），可在 CI 中直接执行。
"""
import os
import json
import glob
from datetime import datetime, timedelta
from hashlib import md5

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")

CITY_CN = {
    "shenzhen": "深圳", "guangzhou": "广州", "shanghai": "上海", "beijing": "北京",
    "hangzhou": "杭州", "chengdu": "成都", "nanjing": "南京", "wuhan": "武汉",
    "xian": "西安", "chongqing": "重庆",
}

TIMEZONE = "Asia/Shanghai"


def generate_uid(exhibition):
    title = exhibition.get("title") or exhibition.get("name", "")
    venue = exhibition.get("venue", "")
    start = exhibition.get("start_date", "")
    content = f"{title}{venue}{start}"
    return md5(content.encode("utf-8")).hexdigest()[:16]


def format_date(date_str, is_end=False):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    if is_end:
        date = date + timedelta(days=1)
    return date.strftime("%Y%m%d")


def create_ics(city, exhibitions):
    cn = CITY_CN.get(city, city)
    cal_name = f"童行 ({cn}亲子活动)"
    cal_desc = f"{cn}展览与亲子活动日历 - 涵盖展览、图书馆活动、文体活动、科技馆活动等"

    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//TongXing GoOut//Calendar//ZH",
        f"X-WR-CALNAME:{cal_name}",
        f"X-WR-CALDESC:{cal_desc}",
        f"X-WR-TIMEZONE:{TIMEZONE}",
        "BEGIN:VTIMEZONE",
        "TZID:Asia/Shanghai",
        "BEGIN:STANDARD",
        "DTSTART:19701001T030000",
        "RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU",
        "TZNAME:CST",
        "TZOFFSETFROM:+0800",
        "TZOFFSETTO:+0800",
        "END:STANDARD",
        "BEGIN:DAYLIGHT",
        "DTSTART:19700401T020000",
        "RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=-1SU",
        "TZNAME:CST",
        "TZOFFSETFROM:+0800",
        "TZOFFSETTO:+0800",
        "END:DAYLIGHT",
        "END:VTIMEZONE",
    ]

    for ex in exhibitions:
        uid = generate_uid(ex)
        lines.append("BEGIN:VEVENT")
        lines.append(f"UID:{uid}@goout-{city}")
        lines.append(f"DTSTAMP:{datetime.now().strftime('%Y%m%dT%H%M%SZ')}")

        start_dt = format_date(ex["start_date"])
        end_dt = format_date(ex["end_date"], is_end=True)
        lines.append(f"DTSTART;VALUE=DATE:{start_dt}")
        lines.append(f"DTEND;VALUE=DATE:{end_dt}")

        summary = ex.get("title") or ex.get("name", "")
        lines.append(f"SUMMARY:{summary}")
        lines.append(f"LOCATION:{ex.get('venue', '')}")

        parts = []
        if ex.get("description"):
            parts.append(ex["description"])
        parts.append(f"地点: {ex.get('venue', '')}")
        parts.append(f"时间: {ex.get('start_date', '')} 至 {ex.get('end_date', '')}")
        link = ex.get("link") or ex.get("url")
        if link:
            parts.append(f"详情: {link}")
        if ex.get("contact"):
            parts.append(f"联系: {ex['contact']}")

        lines.append("DESCRIPTION:" + "\\n".join(parts))
        lines.append("END:VEVENT")

    lines.append("END:VCALENDAR")
    return "\r\n".join(lines)


def main():
    pattern = os.path.join(OUTPUT_DIR, "exhibitions_*.json")
    files = [f for f in glob.glob(pattern) if not f.endswith("_all.json")]
    if not files:
        print("未找到任何分城市活动文件 exhibitions_*.json")
        return

    total = 0
    for path in sorted(files):
        base = os.path.basename(path)
        city = base[len("exhibitions_"):-len(".json")]
        with open(path, "r", encoding="utf-8") as f:
            exhibits = json.load(f)
        if not isinstance(exhibits, list):
            exhibits = list(exhibits.values())
        exhibits.sort(key=lambda x: x.get("start_date", ""))
        ics = create_ics(city, exhibits)
        out_path = os.path.join(OUTPUT_DIR, f"exhibitions_{city}.ics")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ics)
        print(f"生成 exhibitions_{city}.ics ({len(exhibits)} 条)")
        total += len(exhibits)
    print(f"完成：共 {len(files)} 个城市，{total} 条活动写入 ICS。")


if __name__ == "__main__":
    main()
