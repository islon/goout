/**
 * 童行 (goout) 活动 / 场馆数据 API —— Cloudflare Worker
 * 读取 GitHub Pages 上公开的 output/exhibitions_*.json，对外提供 REST + CORS。
 * 本地自托管请用 api/json_api.py（功能完全一致）。
 *
 * 部署：
 *   npx wrangler login
 *   npx wrangler deploy
 * 部署后获得 https://goout-api.<你的子域>.workers.dev
 */

const CITY_NAMES = {
  beijing: "北京", shanghai: "上海", guangzhou: "广州", shenzhen: "深圳",
  hangzhou: "杭州", chengdu: "成都", chongqing: "重庆", nanjing: "南京",
  wuhan: "武汉", xian: "西安",
};

const DEFAULT_BASE = "https://islon.github.io/goout/output";

// ---------- 工具 ----------
async function sha1(s) {
  const buf = await crypto.subtle.digest("SHA-1", new TextEncoder().encode(s));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, "0")).join("").slice(0, 12);
}
async function makeId(...parts) {
  return sha1(parts.join("|"));
}
function statusOf(start, end, today) {
  if (start && start > today) return "upcoming";
  if (end && end < today) return "ended";
  return "ongoing";
}
function normBool(v) {
  if (typeof v === "boolean") return v;
  if (typeof v === "string") return v.trim().toLowerCase() in { true: 1, "1": 1, yes: 1, "是": 1 };
  return Boolean(v);
}
function todayISO() {
  return new Date().toISOString().slice(0, 10);
}
function json(body, status = 200, extra = {}) {
  return new Response(JSON.stringify(body, null, 0), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "access-control-allow-origin": "*",
      "access-control-allow-headers": "*",
      "cache-control": "public, max-age=60",
      ...extra,
    },
  });
}
function corsPreflight() {
  return new Response(null, {
    status: 204,
    headers: {
      "access-control-allow-origin": "*",
      "access-control-allow-headers": "*",
      "access-control-allow-methods": "GET, OPTIONS",
    },
  });
}

// 缓存（Workers Cache API，10 分钟）
const CACHE_TTL = 600;
async function fetchCity(code, base) {
  const url = `${base}/exhibitions_${code}.json`;
  const cache = caches.default;
  const ckey = new Request(url);
  const cached = await cache.match(ckey);
  if (cached) return cached.json();
  const res = await fetch(url, { headers: { "user-agent": "goout-api-worker" } });
  if (!res.ok) throw new Error(`city ${code} http ${res.status}`);
  const data = await res.json();
  const toCache = new Response(JSON.stringify(data), {
    headers: { "content-type": "application/json", "cache-control": `public, max-age=${CACHE_TTL}` },
  });
  // 后台写入缓存，不阻塞当前响应
  await cache.put(ckey, toCache.clone()).catch(() => {});
  return data;
}

// ---------- 数据构建 ----------
async function buildActivities(base) {
  const today = todayISO();
  const acts = [];
  const cities = {};
  const venueMap = {};
  await Promise.all(Object.keys(CITY_NAMES).map(async (code) => {
    let recs;
    try { recs = await fetchCity(code, base); }
    catch (e) { recs = []; }
    const cname = CITY_NAMES[code];
    const cityEntry = (cities[code] = { code, name: cname, activity_count: 0, venue_count: 0 });
    for (const rec of recs) {
      if (!rec || typeof rec !== "object") continue;
      const venue = (rec.venue || "").trim();
      const title = (rec.title || rec.name || "").trim();
      const start = (rec.start_date || "").trim();
      const end = (rec.end_date || "").trim();
      const id = await makeId(code, title, venue, start, end);
      const item = { ...rec, id, city: code, city_name: cname,
        family_friendly: normBool(rec.family_friendly ?? rec.is_family_friendly),
        start_date: start, end_date: end, status: statusOf(start, end, today) };
      acts.push(item);
      cityEntry.activity_count++;
      if (venue) {
        const vkey = code + "|" + venue;
        let v = venueMap[vkey];
        if (!v) {
          v = { id: await makeId(code, venue), name: venue, city: code, city_name: cname,
            district: (rec.district || "").trim(), type: (rec.type || "").trim(),
            venue_url: (rec.venue_url || "").trim(),
            third_party_url: (rec.link || rec.url || "").trim(),
            address: (rec.address || "").trim(), activity_count: 0, activity_ids: [] };
          venueMap[vkey] = v;
        }
        if (!v.venue_url && rec.venue_url) v.venue_url = rec.venue_url;
        if (!v.third_party_url && (rec.link || rec.url)) v.third_party_url = (rec.link || rec.url).trim();
        v.activity_count++;
        v.activity_ids.push(id);
      }
    }
  }));
  const venues = Object.values(venueMap).map(finalizeVenue);
  for (const c of Object.values(cities)) c.venue_count = venues.filter((v) => v.city === c.code).length;
  return { activities: acts, cities: Object.values(cities), venues };
}
function finalizeVenue(v) {
  const official = v.venue_url || "";
  const third = v.third_party_url || "";
  return {
    ...v,
    official_url: official,
    url: official || third,
    url_source: official ? "official" : (third ? "third_party" : ""),
  };
}

// ---------- 过滤 ----------
function filterActivities(acts, q) {
  const out = [];
  for (const a of acts) {
    if (q.city && a.city !== q.city) continue;
    if (q.venue && a.venue !== q.venue) continue;
    if (q.category && (a.category || "") !== q.category) continue;
    if (q.fee && (a.fee || "") !== q.fee) continue;
    if (q.status && a.status !== q.status) continue;
    if (q.family_friendly === "true" && !a.family_friendly) continue;
    if (q.family_friendly === "false" && a.family_friendly) continue;
    if (q.start_date && (a.end_date || "") && a.end_date < q.start_date) continue;
    if (q.end_date && (a.start_date || "") && a.start_date > q.end_date) continue;
    if (q.keyword) {
      const hay = [a.title, a.name, a.venue, a.description, a.category].join(" ").toLowerCase();
      if (!hay.includes(q.keyword.toLowerCase())) continue;
    }
    out.push(a);
  }
  return out;
}
function filterVenues(vens, q) {
  const out = [];
  for (const v of vens) {
    if (q.city && v.city !== q.city) continue;
    if (q.keyword) {
      const hay = (v.name + v.district + v.type).toLowerCase();
      if (!hay.includes(q.keyword.toLowerCase())) continue;
    }
    out.push(v);
  }
  return out;
}
function paginate(items, q) {
  const page = Math.max(1, parseInt(q.page || "1", 10));
  const limit = Math.min(200, Math.max(1, parseInt(q.limit || "20", 10)));
  const start = (page - 1) * limit;
  return { total: items.length, page, limit, count: Math.min(limit, items.length - start),
    data: items.slice(start, start + limit) };
}

// ---------- 路由 ----------
function overview() {
  return json({
    name: "童行 (goout) 活动 / 场馆数据 API",
    version: "1.0.0",
    description: "基于公开 output/exhibitions_*.json 的城市场馆与亲子活动数据接口，支持跨域访问。",
    endpoints: [
      { method: "GET", path: "/api/cities", desc: "城市列表（含活动数 / 场馆数）" },
      { method: "GET", path: "/api/activities", desc: "活动列表（过滤 + 分页）" },
      { method: "GET", path: "/api/activities/{id}", desc: "单个活动详情" },
      { method: "GET", path: "/api/venues", desc: "场馆列表（由活动聚合，官方链接优先）" },
      { method: "GET", path: "/api/venues/{id}", desc: "单个场馆 + 其活动" },
      { method: "GET", path: "/api/statistics", desc: "统计信息" },
    ],
  });
}

export default {
  async fetch(request, env) {
    const base = env.BASE_URL || DEFAULT_BASE;
    if (request.method === "OPTIONS") return corsPreflight();
    const url = new URL(request.url);
    const p = url.pathname;
    const q = Object.fromEntries(url.searchParams.entries());

    try {
      // 根路径概览
      if (p === "/" || p === "/api" || p === "/api/") return overview();

      const data = await buildActivities(base);

      if (p === "/api/cities") {
        return json({ cities: data.cities });
      }

      if (p === "/api/statistics") {
        const byCity = {}, byFee = {}, byCategory = {};
        for (const a of data.activities) {
          byCity[a.city_name] = (byCity[a.city_name] || 0) + 1;
          const f = a.fee || "未知";
          byFee[f] = (byFee[f] || 0) + 1;
          const c = a.category || "未分类";
          byCategory[c] = (byCategory[c] || 0) + 1;
        }
        const officialVenues = data.venues.filter((v) => v.url_source === "official").length;
        return json({
          activity_total: data.activities.length,
          venue_total: data.venues.length,
          city_total: data.cities.length,
          official_link_venues: officialVenues,
          by_city: byCity, by_fee: byFee, by_category: byCategory,
        });
      }

      if (p === "/api/activities") {
        const items = filterActivities(data.activities, q);
        return json(paginate(items, q));
      }

      let m = p.match(/^\/api\/activities\/([\w]+)$/);
      if (m) {
        const a = data.activities.find((x) => x.id === m[1]);
        return a ? json(a) : json({ error: "activity not found", id: m[1] }, 404);
      }

      if (p === "/api/venues") {
        const items = filterVenues(data.venues, q);
        items.sort((a, b) => (a.city > b.city ? 1 : a.city < b.city ? -1 : b.activity_count - a.activity_count || (a.name > b.name ? 1 : -1)));
        const clean = items.map((v) => { const { activity_ids, ...rest } = v; return rest; });
        return json(paginate(clean, q));
      }

      m = p.match(/^\/api\/venues\/([\w]+)$/);
      if (m) {
        const v = data.venues.find((x) => x.id === m[1]);
        if (!v) return json({ error: "venue not found", id: m[1] }, 404);
        const acts = data.activities.filter((a) => v.activity_ids.includes(a.id));
        return json({ ...v, activities: acts });
      }

      return json({ error: "not found", path: p, try: "/api/cities" }, 404);
    } catch (e) {
      return json({ error: "internal", detail: String(e && e.message || e) }, 500);
    }
  },
};
