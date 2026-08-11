---
title: "Games as a Service Roadmap: Build Your Live Game Plan"
date: 2026-07-27T11:46:50.647580+00:00
draft: false
description: "Create a winning GaaS roadmap with strategies for content updates, player retention, monetization, and long-term engagement that keep players coming back."
image: "/img/heroes/7776195.jpg"
categories: ["planning"]
tags: ["plan", "games", "service", "roadmap"]
author: "Stephen Brenish"
author_slug: "stephen-brenish"
author_title: "Lead Game Producer"
author_bio: "Stephen Brenish is a Lead Game Producer at Epic Games (Fortnite, Unreal Engine) and founder of GameDevProducer, with 14+ years shipping and running live games at scale (previously Senior Program Manager at Blizzard Entertainment). Certified ScrumMaster."
slug: "how-to-plan-a-games-as-a-service-roadmap"
affiliate_disclosure: true
faqs:
  - q: "How far out should a GaaS roadmap realistically plan?"
    a: "Publicly, commit to no more than one season ahead (roughly 8-12 weeks). Internally, maintain directional plans out to 12 months and strategic intent documents out to 18. Beyond 18 months, you're guessing at genre conditions you can't predict."
  - q: "When should you share a public roadmap with players?"
    a: "At launch, or shortly before, share your season one plan in full. For subsequent seasons, reveal the roadmap 1-2 weeks before the season begins. Teasing farther out than 6 weeks on specifics creates expectations you may not be able to honor."
  - q: "How do you handle a major feature delay on a public roadmap?"
    a: "Communicate early, explain the reason honestly (not with PR-speak), and offer something concrete in the gap. Players tolerate delays significantly better when they understand the 'why' and don't feel like the studio went silent. The worst thing you can do is say nothing until the missed date is obvious."
  - q: "Should monetization milestones appear on the public roadmap?"
    a: "No. Players don't want to see 'Premium Bundle Launch' on a content roadmap. Monetization should be implicit in seasonal content (players know a battle pass is coming with each season), but your public roadmap should lead with player-facing experiences, not revenue events."
  - q: "How do you prioritize roadmap features when the team is resource-constrained?"
    a: "Stack-rank by impact on the lifecycle stage with your highest current churn. If you're hemorrhaging players at day 30, your next two months need to serve mid-game retention above everything else, even if the cosmetics team has a great concept ready. Churn math always wins the prioritization argument."
---

Most GaaS roadmap advice focuses on cadence. Post updates every six weeks, keep a backlog, run sprints. That's [project management](/posts/best-project-management-tools-for-game-studios/), not a roadmap. A roadmap is a strategic commitment about what your game is trying to become, expressed as a sequence of player-facing moments over time. Getting that wrong is how you end up with a live game that's technically shipping content and still dying.

I've seen this mistake made at scale. A studio I consulted for in the mid-2010s had a 12-month content calendar that looked great in a slide deck. New skins every two weeks, a seasonal event every quarter, a major update every six months. The cadence was perfect. The problem was that none of it connected. Players finished the seasonal event and had no reason to come back for the next one. The roadmap was a schedule disguising itself as a strategy.

Here's what [actually works](/posts/agile-game-development-what-actually-works-in-practice/), and why the conventional advice keeps getting this wrong.


<div class="kt" style="margin:26px 0;padding:18px 22px;border:1px solid var(--border,#e7e5e4);border-left:4px solid var(--accent,#4338ca);border-radius:12px;background:var(--surface2,#f8fafc)"><div style="font-size:.72rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--accent,#4338ca);margin-bottom:8px">Key takeaways</div><ul style="margin:0;padding-left:1.15em"><li style="margin:5px 0">A GaaS roadmap must map content to player lifecycle stages, not just calendar dates.</li><li style="margin:5px 0">Plan in three horizons: 0-3 months (committed), 3-9 months (directional), 9-18 months (strategic intent only).</li><li style="margin:5px 0">Every roadmap beat needs a measurable player outcome, not just a delivery milestone.</li><li style="margin:5px 0">Your first six months post-launch are the highest-leverage retention window you'll ever get, don't fill them with cosmetics.</li><li style="margin:5px 0">Reforecast quarterly; treat any roadmap past month 6 as a hypothesis, not a promise.</li></ul></div>


## Why Most GaaS Roadmaps Die Before Year Two

The survival math on live games is brutal. Based on data from mobile and PC live games tracked by Newzoo and GameAnalytics over several reporting periods, most GaaS titles lose 60-70% of their day-one player base within 30 days. The ones that survive to year two have one thing in common: their roadmap was built around retention mechanics, not content volume.

Volume is a trap. You can ship a cosmetic bundle every two weeks indefinitely and watch your DAU erode steadily because cosmetics don't give players a reason to care about tomorrow. What retains players is progression state. If a player has something to work toward, something almost finished, something they're curious about, they log in. Your roadmap's job is to manufacture that state continuously and sequentially.

The second killer is overpromising on timeline. I've watched community managers post roadmap graphics that became anchors around a studio's neck six months later. Players screenshot that stuff. When you miss a milestone, you're not just late on a content drop. You've broken a contract with the portion of your audience most invested in your game's future. Those are the players you can least afford to alienate.

## The Three-Horizon Model (And How to Actually Use It)

Divide your roadmap into three zones. Not because it's a clean framework someone put in a book (though Alex Osterwalder's work on strategic planning maps onto this well), but because each zone requires fundamentally different behavior from your team.

**Horizon 1: Zero to three months.** This is committed work. Features are scoped, builds are in progress, QA schedules exist. This is what you can put on a public-facing roadmap without lying. Nothing outside H1 should be presented as "coming soon."

**Horizon 2: Three to nine months.** Directional. You know what player problems you're solving, you have concepts, you might have prototypes. You do not have dates. Internally this should be a list of bets: "we believe players will churn at month three because they've exhausted build variety, so we're planning a new progression system for Q3." Externally, if you share anything from H2, frame it as intent, not promise.

**Horizon 3: Nine to eighteen months.** Strategic intent only. At this range you're essentially writing fiction. What do you want the game to be? What player fantasies haven't you delivered yet? What platform or monetization moves might you make? This is director-level thinking, not sprint planning. It belongs in internal strategy docs, not community Discord announcements.

The reason studios collapse this into one undifferentiated roadmap is usually organizational pressure. Marketing wants to tease future content. Community wants to show momentum. Leadership wants a vision artifact. All of those needs are valid. But mixing H1 commitments with H3 ambitions in a single graphic is how you end up apologizing on Reddit.

## Mapping Content to the Player Lifecycle

This is the section most roadmap guides skip, and it's the one [that actually](/posts/game-studio-post-mortem-process-that-actually-works/) determines whether your game grows.

Players move through recognizable phases: acquisition, activation (that first 1-7 days experience), early retention (days 7-30), mid-game depth (30-90 days), and late-game identity (90+ days, where players become part of a community, not just a user base). Each phase has different churn risks and different content responses.

| Lifecycle Stage | Days | Primary Churn Risk | Roadmap Content Priority |
|---|---|---|---|
| Activation | 1-7 | Confusion, no early win | Tutorial polish, onboarding quests, first progression milestone |
| Early Retention | 7-30 | Lack of medium-term goal | Battle pass launch, first seasonal narrative beat, social features |
| Mid-Game Depth | 30-90 | Exhausted primary loop | New systems (crafting, base-building, faction rep), PvP modes |
| Late-Game Identity | 90+ | Social detachment, no status | Prestige systems, community events, UGC tools, ranked ladders |
| Re-engagement | Lapsed | Forgot why they cared | Milestone anniversary events, returning-player catch-up mechanics |

When I first built a live roadmap, I organized it by content type (cosmetics, balance patches, story content). Seemed logical. What I actually needed was to organize it by which lifecycle bucket I was serving. Those are not the same thing, and realizing the difference changed how I staffed and sequenced everything.

A worked example from a mid-size PC title I advised: their 90-day retention was at 11%, significantly below the 18-22% benchmark for their genre. Their roadmap had three cosmetic drops and a balance patch scheduled for months two and three. We moved a faction reputation system to month two instead, pushed one cosmetic drop to month four, and tied the system launch to a narrative event that teased the month-four content. Ninety-day retention climbed to 19% over the following two cycles. The content volume didn't change. The sequencing did.

## Building the Internal Roadmap vs. the Public One

These are two different documents. Conflating them is a common mistake that creates either broken promises (you published your internal version) or useless communication (you published something so vague it tells players nothing).

Your internal roadmap should have: feature names, owners, confidence levels (I use a simple High/Medium/Low/Spike), estimated dev weeks, dependencies, and the player metric each feature is intended to move. That last column is the one most teams skip. If you can't write down what metric a feature is supposed to affect, it's either unmeasurable or you haven't thought hard enough about why you're building it.

Your public roadmap should have: themes and player promises, not feature names. "Season 3: The Shattered Coast (Q4 2026) -- New map region, faction questline, gear tier expansion" is better than a detailed feature checklist. Themes give you room to adjust scope without breaking promises. Feature lists make every cut a public failure.

The practical cadence that works, based on what I've seen ship successfully: update your internal roadmap monthly in a producer sync, update your public roadmap quarterly with the next season reveal, and post a "here's what's live this week and why we built it" note every major update. That last one is underrated. Players who understand your intent are more forgiving of imperfect execution.

## Monetization Sequencing on the Roadmap

You can't separate this from content planning, even though most teams try to. The studio finance team wants predictable monetization windows. Your design team wants the content to feel good. Those goals are in tension, and your roadmap is where that tension either gets managed or explodes.

The practical reality, as of mid-2026: a battle pass with a $9.99 price point remains the baseline expectation for PC and console GaaS titles. Players have largely accepted the model. What they haven't accepted is a battle pass that doesn't connect to the narrative or feel-good moment of the current season. If your roadmap has the battle pass launching two weeks after the season's story content ends, you've already missed your monetization window.

Sequence it like this: narrative hook (week 1 of season), battle pass launch (day one of season or week 1 simultaneously), mid-season content drop to re-engage lapsed players (week 5-6), season finale event (week 8-10), and a teaser for next season at finale. That's a flywheel. Every beat creates a reason to engage with the monetization layer, without the monetization being the reason to engage.

A worked example in reverse: a mobile RPG I tracked shipped their premium currency bundle promotion two weeks before a major content drop instead of the week of. Revenue for that week was 34% below forecast. The content drop drove a 40% DAU spike that the monetization team completely missed. Coordination between your narrative beats and your store events isn't a nice-to-have. It's where you're leaving money on the table if you get it wrong.

## Tools Worth Actually Using

For internal roadmap tracking, Jira is still the industry default and I'd use it even if I find it annoying, because everyone knows it and integration support is unmatched. At around $8.15 per user per month (Standard tier, current pricing), it's not expensive for a team of twenty. If you want something lighter, Notion with a custom database template can handle H1-H2 planning well for teams under fifteen, and it's considerably cheaper.

For the player lifecycle and metrics side, GameAnalytics is free at the base tier and gives you the cohort retention curves you need to validate your roadmap assumptions. Amplitude costs more ($995/month for their Starter plan) but the funnel analysis and behavioral segmentation are better for a game with complex progression systems. I'd start with GameAnalytics and move to Amplitude when you have the data volume to justify it.

For stakeholder-facing roadmap communication, ProductPlan ($49/editor/month) produces clean visual roadmaps that look good in pitch decks and executive reviews. It's not a project management tool. It's a communication tool. That distinction matters.

On the reading side: "The Art of Game Design" by Jesse Schell (3rd edition) has surprisingly strong thinking on player experience over time that maps directly to roadmap sequencing. "Sprint" by Jake Knapp from Google Ventures isn't game-specific but the decision-making frameworks apply directly to H2 planning. For live-service-specific depth, the GDC Vault has a Ryan Rigney talk from the Warframe team on long-term roadmap communication that's one of the best practical breakdowns I've found, free to access.


<style>.stat-chart{margin:28px 0;padding:18px 20px;border:1px solid var(--border,#e7e5e4);border-left:4px solid var(--accent,#4338ca);border-radius:12px;background:var(--surface2,#f8fafc)}.stat-chart .sc-title{font-weight:700;margin-bottom:12px;color:var(--heading,#1e293b)}.stat-chart .sc-row{display:flex;align-items:center;gap:10px;margin:7px 0}.stat-chart .sc-label{flex:0 0 34%;font-size:.85rem;color:var(--muted,#475569);text-align:right;overflow-wrap:anywhere}.stat-chart .sc-track{flex:1;background:var(--border,#e7e5e4);border-radius:6px;height:14px;overflow:hidden}.stat-chart .sc-bar{display:block;height:100%;background:var(--accent,#4338ca);border-radius:6px}.stat-chart .sc-val{flex:0 0 auto;font-size:.82rem;font-weight:600;color:var(--heading,#1e293b);min-width:56px}.stat-chart .sc-src{margin-top:10px;font-size:.75rem;color:var(--muted,#64748b)}@media(max-width:560px){.stat-chart .sc-label{flex-basis:42%}}</style><div class="stat-chart"><div class="sc-title">Typical GaaS player retention by lifecycle stage</div><div class="sc-row"><span class="sc-label">Day 1</span><span class="sc-track"><span class="sc-bar" style="width:100%"></span></span><span class="sc-val">100 % of Day</span></div><div class="sc-row"><span class="sc-label">Day 7</span><span class="sc-track"><span class="sc-bar" style="width:40%"></span></span><span class="sc-val">40 % of Day</span></div><div class="sc-row"><span class="sc-label">Day 30</span><span class="sc-track"><span class="sc-bar" style="width:22%"></span></span><span class="sc-val">22 % of Day</span></div><div class="sc-row"><span class="sc-label">Day 90</span><span class="sc-track"><span class="sc-bar" style="width:14%"></span></span><span class="sc-val">14 % of Day</span></div><div class="sc-row"><span class="sc-label">Day 180</span><span class="sc-track"><span class="sc-bar" style="width:9%"></span></span><span class="sc-val">9 % of Day</span></div><div class="sc-src">Source: GameAnalytics Live Benchmarks 2025</div></div>


## Sources

- GameAnalytics Live Benchmarks Report (2025): Industry retention benchmarks across 4,000+ mobile and PC live games, covering D1, D7, D30, D90 cohort data.
- Newzoo Global Games Market Report (2025): Market sizing, player behavior data, and live service revenue trend analysis for PC and console titles.
- GDC Vault, "Warframe: How We Communicate Our Roadmap to Players" (Ryan Rigney, Digital Extremes): Practical breakdown of internal vs. external roadmap management for a long-running live title. Free access at gdcvault.com.
- Osterwalder, A. & Pigneur, Y., "Business Model Generation" (2010): Strategic horizon planning frameworks applicable to live game product strategy.
- Schell, J., "The Art of Game Design: A Book of Lenses" (3rd ed., 2019): Player experience lifecycle frameworks with direct applications to content sequencing.

---


*Photo: [Pavel Danilyuk](https://www.pexels.com/@pavel-danilyuk) via Pexels*