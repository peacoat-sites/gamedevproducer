#!/usr/bin/env python3
"""
Fetch game-industry trade news (business, production, platforms) from RSS.
Writes data/news.json for the /industry-news/ page.
Steam data is owned by fetch_steam.py (data/steam.json) — do not write it here.
"""
import json, re, datetime, time, html
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

FEEDS = [
    ("Game Developer",      "https://www.gamedeveloper.com/rss.xml"),
    ("GamesIndustry.biz",   "https://www.gamesindustry.biz/feed"),
    ("Game World Observer", "https://gameworldobserver.com/feed"),
]
PER_SOURCE = 12
KEEP = 40

# consumer/deals/entertainment items that don't belong on a production-focused site
EXCLUDE = re.compile(
    r"\b(deal|deals|% off|discount|on sale|lowest price|giveaway|prime day|black friday|"
    r"review:|review\b|netflix|movie|film|tv series|season \d+ episode|trailer reaction|"
    r"best .* to buy|gift guide|where to buy|preorder|pre-order)\b", re.I)

def iso(entry):
    for k in ("published_parsed", "updated_parsed"):
        t = entry.get(k)
        if t:
            return time.strftime("%Y-%m-%d", t)
    return TODAY

items = []
for source, url in FEEDS:
    try:
        feed = feedparser.parse(url, agent="GameDevProducer.com/1.0 (+https://gamedevproducer.com)")
        n = 0
        for entry in feed.entries:
            title = re.sub(r"\s+", " ", html.unescape(entry.get("title", ""))).strip()
            link = entry.get("link", "")
            if not title or not link or EXCLUDE.search(title):
                continue
            items.append({"source": source, "title": title, "url": link, "date": iso(entry)})
            n += 1
            if n >= PER_SOURCE:
                break
        print(f"  {source}: {n} items")
    except Exception as e:
        print(f"  [WARN] {source}: {e}")

seen, unique = set(), []
for item in sorted(items, key=lambda x: x["date"], reverse=True):
    key = item["title"][:60].lower()
    if key not in seen:
        seen.add(key)
        unique.append(item)

if unique:
    out = {"updated": TODAY, "count": len(unique[:KEEP]), "items": unique[:KEEP]}
    (DATA_DIR / "news.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  News: {out['count']} items")
else:
    print("  News: no items fetched; keeping previous news.json")
