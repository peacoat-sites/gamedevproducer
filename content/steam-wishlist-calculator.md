---
title: "Steam Wishlist Calculator: Estimate Your First-Week Sales from Wishlists"
hide_title: true
date: 2026-06-10
lastmod: 2026-10-06
slug: "steam-wishlist-to-sales"
tool: true
categories: ["publishing"]
description: "Estimate first-week, first-month and first-year Steam sales from your wishlist count, using GameDiscoverCo's published benchmarks, with weak, typical and strong launch scenarios."
image: "https://images.pexels.com/photos/2882655/pexels-photo-2882655.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"
author: "Stephen Brenish"
author_bio: "Stephen Brenish is a Lead Game Producer at Epic Games (Fortnite, Unreal Engine) and founder of GameDevProducer, with 14+ years shipping and running live games at scale (previously Senior Program Manager at Blizzard Entertainment). Certified ScrumMaster."
author_slug: "stephen-brenish"
author_title: "Lead Game Producer"
faqs:
  - q: "What is a good wishlist conversion rate on Steam?"
    a: "GameDiscoverCo's October 2025 analysis found a median of 0.15 first-week sales per wishlist for games launching with more than 25,000 wishlists, falling to 0.10 for games priced above $10. Results vary by 10 to 20 times between games, so beating the median for your price point is a good launch."
  - q: "How many wishlists do I need before launching on Steam?"
    a: "There is no fixed threshold. Work backwards from your budget: divide the revenue you need from launch week by your net revenue per copy, then divide by about 0.10 sales per wishlist for a game priced above $10. That gives the wishlist count at which a typical launch gets you there."
  - q: "Do Early Access games convert wishlists worse?"
    a: "On average, yes. A GameDiscoverCo analysis of about 700 launches released from September 2023 found Early Access conversion roughly a third lower than full 1.0 launches."
  - q: "Does the calculator work for free-to-play games?"
    a: "No. For free-to-play games, wishlists convert into downloads rather than sales, and revenue depends on monetization design, so a sales-per-wishlist model does not apply."
---

This free Steam wishlist calculator estimates your first-week and first-month sales from the number of wishlists you have at launch. It uses GameDiscoverCo's published benchmarks for recent Steam releases and shows weak, typical and strong launches side by side, because the honest answer to "how many copies will I sell?" is a range.

## What the benchmarks say

The standard measure is the ratio of first-week sales to launch wishlists. GameDiscoverCo, which tracks Steam launches closely, published its latest figures in October 2025:

- For games that launched with more than 25,000 wishlists between September 2024 and September 2025, the median was **0.15 first-week sales per wishlist**: about 15,000 sales from 100,000 wishlists.
- For games priced **above $10**, the median fell to **0.10**.
- The ratio varies by **10 to 20 times** between games. The underperformers averaged Mixed reviews (67% positive) and had been on Steam for an average of 411 days before launch; the top converters averaged Very Positive (91%).

An earlier GameDiscoverCo analysis of about 700 games released from September 2023, each with at least 5,000 wishlists and 500 first-month sales, found that sales keep coming after launch week, with a median of 22% in week one against 27% for the whole first month, and that Early Access launches converted about a third lower than full releases. Because that sample left out games that sold fewer than 500 copies, its medians run higher than the 2025 figures.

Older rules of thumb, some quoting 0.2 sales per wishlist or more, came from smaller or more selective samples. Plan with the recent medians.

## How the calculator works

- **Typical launch** uses the median: 0.10 sales per wishlist for games above $10, and 0.15 at $10 or less. The 0.15 figure is the overall median, which includes pricier games, so it is probably conservative for cheaper ones.
- **Weak and strong launches** are half and double the median. They are planning scenarios, not measured percentiles; real outcomes spread much wider in both directions.
- **Early Access** reduces the ratio by about a third.
- **Month one** is about 1.25 times week one, in line with the 22% and 27% medians above.
- **Year one** is 2.46 times week-one revenue, the median in GameDiscoverCo's July 2026 study of about 5,000 Steam games launched between July 2023 and July 2025. Units grow faster (2.59 times week one) than revenue, because most later sales happen at a discount.
- **Net revenue** is after Valve's standard 30% share and an 8% allowance for refunds. It does not account for sales tax or VAT, regional pricing or a publisher's share, all of which reduce what you receive.

{{< wishlist-calc >}}

## What different wishlist counts mean

First-week units for a full release priced above $10:

| Wishlists at launch | Weak (0.05) | Typical (0.10) | Strong (0.20) |
|---|---|---|---|
| 5,000 | 250 | 500 | 1,000 |
| 10,000 | 500 | 1,000 | 2,000 |
| 25,000 | 1,250 | 2,500 | 5,000 |
| 50,000 | 2,500 | 5,000 | 10,000 |
| 100,000 | 5,000 | 10,000 | 20,000 |

Ten thousand wishlists is often treated as a milestone for an indie launch. At $14.99 with a typical launch, that points to roughly 1,000 first-week sales: about $15,000 gross and about $9,650 net after Valve's share and refunds. The median long tail takes that to roughly $23,700 net over the first year. That is a meaningful result for a solo developer, but nowhere near enough to recoup a team's multi-year budget. The gap between your wishlists and your [development budget](/indie-game-budget-calculator/) matters more than any single benchmark.

## Growing wishlists before launch

The lever you control most is the number and quality of your wishlists. Steam Next Fest, a strong demo, outreach to content creators and a store page that converts visitors all add wishlists. Quality matters as much as count: the underperformers in GameDiscoverCo's 2025 analysis had sat on Steam for longer before launch, so if your page has been live for years, estimate cautiously.

For the details, see [how to plan a demo for Steam Next Fest](/posts/how-to-plan-a-game-demo-for-steam-next-fest/) and [how to build a Steam page that converts](/posts/how-to-build-a-steam-page-that-converts/). The [Steam sale and Next Fest calendar](/steam-sale-dates/) shows the upcoming festival dates and deadlines, and the [Steam revenue calculator](/posts/steam-revenue-calculator/) models what a game earns over its life.

## Sources

- Simon Carless, ["The state of Steam wishlist conversions"](https://newsletter.gamediscover.co/p/the-state-of-steam-wishlist-conversions), GameDiscoverCo, October 17, 2025.
- ["GameDiscoverCo: Conversion benchmarks of Steam wishlists into sales in the first month"](https://gamedevreports.substack.com/p/gamediscoverco-conversion-benchmarks), GameDev Reports, May 10, 2024.
- Simon Carless, ["What 'long tail' should you expect for your PC game in 2026?"](https://newsletter.gamediscover.co/p/what-long-tail-should-you-expect), GameDiscoverCo, July 21, 2026.
