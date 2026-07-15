#!/usr/bin/env python3
"""Weekly Steam top-games feed via SteamSpy (public API, no key).
Writes data/steam.json for the steam-top shortcode."""
import json, urllib.request
from datetime import date

req = urllib.request.Request("https://steamspy.com/api.php?request=top100in2weeks",
                             headers={"User-Agent": "Mozilla/5.0"})
d = json.loads(urllib.request.urlopen(req, timeout=60).read())
games = sorted(d.values(), key=lambda g: -int(g.get("ccu", 0)))[:15]
out = []
for i, g in enumerate(games, 1):
    price = int(g.get("price") or 0) / 100
    out.append({"rank": i, "name": g.get("name", ""), "developer": g.get("developer", ""),
                "owners": g.get("owners", "").replace(" .. ", " - "),
                "ccu": int(g.get("ccu", 0)), "price": f"${price:.2f}" if price else "Free"})
data = {"as_of": date.today().isoformat(), "source": "SteamSpy (top by concurrent players, trailing 2 weeks)",
        "games": out}
json.dump(data, open("data/steam.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(f"steam.json: {len(out)} games, as of {data['as_of']}")
