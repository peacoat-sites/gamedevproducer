#!/usr/bin/env python3
"""
Fetch industry news from game dev RSS feeds + Steam new releases.
Writes data/news.json and data/steam.json for Hugo to render.
"""
import json, requests, datetime
from pathlib import Path

try:
    import feedparser
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "feedparser", "-q"])
    import feedparser

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

TODAY = datetime.datetime.utcnow().strftime("%Y-%m-%d")

# ── News feeds ────────────────────────────────────────────────────────────────
FEEDS = [
    ("Game Developer",  "https://www.gamedeveloper.com/rss.xml"),
    ("GDC",             "https://gdconf.com/feed"),
    ("Kotaku",          "https://kotaku.com/rss"),
    ("Polygon",         "https://www.polygon.com/rss/index.xml"),
    ("Eurogamer",       "https://www.eurogamer.net/?format=rss"),
    ("IGN",             "https://feeds.ign.com/ign/all"),
]

items = []
for source, url in FEEDS:
    try:
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:  # top 5 per source
            title = entry.get("title", "").strip()
            link  = entry.get("link", "")
            published = entry.get("published", "")[:10] if entry.get("published") else TODAY
            if title and link:
                items.append({
                    "source": source,
                    "title":  title,
                    "url":    link,
                    "date":   published,
                })
    except Exception as e:
        print(f"  [WARN] {source}: {e}")

# Sort by date descending, deduplicate
seen = set()
unique = []
for item in sorted(items, key=lambda x: x["date"], reverse=True):
    key = item["title"][:60]
    if key not in seen:
        seen.add(key)
        unique.append(item)

news_data = {
    "updated": TODAY,
    "count":   len(unique),
    "items":   unique[:60],  # keep top 60
}
(DATA_DIR / "news.json").write_text(json.dumps(news_data, indent=2))
print(f"  News: {len(unique)} items from {len(FEEDS)} sources")

# ── Steam new releases ─────────────────────────────────────────────────────────
try:
    # Steam featured new releases (no API key needed)
    r = requests.get(
        "https://store.steampowered.com/api/featuredcategories/",
        timeout=15,
        headers={"User-Agent": "GameDevProducer.com/1.0"}
    )
    if r.status_code == 200:
        data = r.json()
        new_releases = data.get("new_releases", {}).get("items", [])
        steam_items = []
        for game in new_releases[:12]:
            steam_items.append({
                "name":              game.get("name", ""),
                "header_image":      game.get("header_image", ""),
                "url":               f"https://store.steampowered.com/app/{game.get('id','')}/",
                "short_description": game.get("short_description", ""),
                "final_price":       game.get("final_price", 0),
            })
        steam_data = {"updated": TODAY, "items": steam_items}
        (DATA_DIR / "steam.json").write_text(json.dumps(steam_data, indent=2))
        print(f"  Steam: {len(steam_items)} new releases")
    else:
        print(f"  Steam API: {r.status_code}")
except Exception as e:
    print(f"  [WARN] Steam: {e}")

print("Done.")
