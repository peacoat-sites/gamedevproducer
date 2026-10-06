---
title: "Steam Revenue Calculator: Estimate Your Game's Earnings on Steam"
image: "/img/heroes/7948037.jpg"
slug: "steam-revenue-calculator"
tool: true
date: 2026-06-10
categories: ["industry intel"]
description: "Estimate a Steam game's sales and revenue before launch from wishlists, or after launch from review count, using GameDiscoverCo and Gamalytic benchmarks and Valve's revenue share."
author: "Stephen Brenish"
author_bio: "Stephen Brenish is a Lead Game Producer at Epic Games (Fortnite, Unreal Engine) and founder of GameDevProducer, with 14+ years shipping and running live games at scale (previously Senior Program Manager at Blizzard Entertainment). Certified ScrumMaster."
author_title: "Lead Game Producer"
author_slug: "stephen-brenish"
lastmod: 2026-10-06
faqs:
  - q: "How much does Steam take from each sale?"
    a: "Valve's standard revenue share is 30%. It drops to 25% on a game's lifetime revenue between $10 million and $50 million, and to 20% above $50 million, so almost every indie game pays 30%. Sales tax or VAT and refunds come out before you are paid as well."
  - q: "What is the Boxleiter method?"
    a: "A rule of thumb that estimates a game's lifetime Steam sales by multiplying its review count by a sales-per-review ratio. Published ratios mostly fall between about 30 and 80, lower for smaller and more recent games. It estimates units, not revenue, because it cannot see how many copies sold at a discount."
  - q: "How much does a Steam game earn in its first year compared with launch week?"
    a: "GameDiscoverCo's July 2026 study of about 5,000 Steam games found a median of 2.46 times week-one revenue over the first year, and 2.99 times over two years. Unit sales grow faster than revenue because most later copies sell at a discount."
  - q: "How accurate are Steam revenue estimates?"
    a: "They are order-of-magnitude estimates. Individual games vary from the medians by 10 times or more in either direction, so use them to test whether a budget is plausible, not to predict a specific number."
---

Launching a game on Steam without a revenue projection is like shipping without a milestone plan: you might land somewhere interesting, or you might run out of runway first. This calculator gives you a grounded starting point, built on the most recent published benchmarks rather than guesswork.

There are two honest ways to estimate Steam revenue, depending on where you are. Before launch, your best signal is wishlists. After launch, it is your review count.

{{< steam-revenue-calc >}}

## Before launch: from wishlists

GameDiscoverCo's October 2025 analysis put the median at about **0.15 first-week sales per wishlist** for games launching with more than 25,000 wishlists, and about **0.10** for games priced above $10. Early Access launches convert roughly a third lower than full releases, according to an earlier GameDiscoverCo study of about 700 games.

Launch week is only the start. GameDiscoverCo's July 2026 study of about 5,000 Steam games launched between July 2023 and July 2025, each selling more than 1,000 copies in its first month, measured the long tail:

| Period | Units, as a multiple of week one | Revenue, as a multiple of week one |
|---|---|---|
| First year | 2.59x | 2.46x |
| First two years | 3.32x | 2.99x |

Games priced at $10 or more reached about 2.7 times week-one units in year one, against about 2.32 times for cheaper games, and co-op games ran well above the median, at 3.53 times. The calculator uses the overall medians. The [Steam wishlist calculator](/steam-wishlist-to-sales/) goes deeper on launch week, with weak, typical and strong scenarios.

## After launch: from reviews

Once a game is out, its public review count is the best free clue to its sales. The Boxleiter method multiplies the review count by a sales-per-review ratio, and published ratios have moved over time:

- Jake Birkett's 2018 dataset, written up for Game Developer, had a median of about 77 sales per review, falling to about 65 for games released from 2017, with a range of roughly 30 to 150.
- Gamalytic data published by GameDiscoverCo in 2023 found about 36 sales per review for games with fewer than 100 reviews, and about 53 for games with 1,000 to 10,000 reviews.

The calculator shows 30, 50 and 70 sales per review side by side. Two cautions. Review counts tell you units, not revenue, because they cannot show how many copies sold at a discount, so the full-price figures are an upper bound. And the ratio varies with genre, price and age, so compare against similar games rather than trusting one number.

## What Valve takes, and what else comes off

Valve's standard revenue share is **30%**, dropping to 25% on lifetime revenue between $10 million and $50 million and to 20% above that. Players can request a refund within 14 days of purchase if they have played for less than two hours; the calculator applies an 8% refund allowance, which is an assumption you should replace with your own data once you have it. Sales tax or VAT, regional pricing and any publisher or partner split reduce what you receive further, and none of those are modeled.

## A worked illustration

Assume a full release at $19.99 with 20,000 wishlists at launch:

1. Week one at the median of 0.10 sales per wishlist: **2,000 copies**, or $39,980 gross.
2. After Valve's 30% and the 8% refund allowance: about **$25,700 net** in week one.
3. At the median long tail of 2.46 times week-one revenue: about **$63,300 net** in the first year, and about **$77,000** after two years.

That is a respectable result for a solo developer and a small one for a team of five. Run the same numbers at half the median, which is a plausible weak launch, and the first year falls to about $31,700.

## Plan for the downside

The most common financial failure in indie development is not a bad game. It is a studio sized for the optimistic case. Model at least three outcomes, make sure the studio survives the weak one, and treat anything above the median as upside. Then compare the result with what you are spending: the [indie game budget calculator](/indie-game-budget-calculator/) covers the cost side, and [how to estimate game development costs](/posts/how-to-estimate-game-development-costs/) explains the method behind it.

## Sources

- Simon Carless, ["The state of Steam wishlist conversions"](https://newsletter.gamediscover.co/p/the-state-of-steam-wishlist-conversions), GameDiscoverCo, October 17, 2025.
- Simon Carless, ["What 'long tail' should you expect for your PC game in 2026?"](https://newsletter.gamediscover.co/p/what-long-tail-should-you-expect), GameDiscoverCo, July 21, 2026.
- ["GameDiscoverCo: Conversion benchmarks of Steam wishlists into sales in the first month"](https://gamedevreports.substack.com/p/gamediscoverco-conversion-benchmarks), GameDev Reports, May 10, 2024.
- Jake Birkett, ["Using Steam reviews to estimate sales"](https://www.gamedeveloper.com/business/using-steam-reviews-to-estimate-sales), Game Developer, May 4, 2018.
- Simon Carless, ["What 'Steam review count' tells us about your game"](https://newsletter.gamediscover.co/p/what-steam-review-count-tells-us), GameDiscoverCo, August 28, 2023.
