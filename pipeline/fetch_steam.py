#!/usr/bin/env python3
"""Weekly Steam top-games feed via SteamSpy (public API, no key).
Writes data/steam.json for the steam-top shortcode."""
import json, urllib.request
from datetime import date

NAME_FIX = {"Counter-Strike: Global Offensive": "Counter-Strike 2"}

req = urllib.request.Request("https://steamspy.com/api.php?request=top100in2weeks",
                             headers={"User-Agent": "Mozilla/5.0"})
d = json.loads(urllib.request.urlopen(req, timeout=60).read())
games = sorted(d.values(), key=lambda g: -int(g.get("ccu", 0)))[:15]
if len(games) < 10:
    raise SystemExit(f"SteamSpy returned only {len(games)} games; keeping previous steam.json")

def devs(s):
    parts = [p.strip() for p in (s or "").split(",") if p.strip()]
    return ", ".join(parts[:2]) + (f" +{len(parts) - 2} more" if len(parts) > 2 else "")

out = []
for i, g in enumerate(games, 1):
    price = int(g.get("price") or 0) / 100
    name = g.get("name", "")
    out.append({"rank": i, "name": NAME_FIX.get(name, name), "developer": devs(g.get("developer", "")),
                "owners": g.get("owners", "").replace(" .. ", " - "),
                "ccu": int(g.get("ccu", 0)), "price": f"${price:.2f}" if price else "Free",
                "price_num": price})

paid = [g["price_num"] for g in out if g["price_num"] > 0]
total_ccu = sum(g["ccu"] for g in out) or 1
summary = {
    "free_count": sum(1 for g in out if g["price_num"] == 0),
    "paid_count": len(paid),
    "avg_paid_price": f"${sum(paid) / len(paid):.2f}" if paid else "n/a",
    "top3_ccu_share": round(100 * sum(g["ccu"] for g in out[:3]) / total_ccu),
}
data = {"as_of": date.today().isoformat(), "source": "SteamSpy (top by concurrent players, trailing 2 weeks)",
        "summary": summary, "games": out}
json.dump(data, open("data/steam.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(f"steam.json: {len(out)} games, as of {data['as_of']} | {summary}")
