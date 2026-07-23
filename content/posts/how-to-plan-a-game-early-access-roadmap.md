---
title: "70% of Players Want This: Planning Your Early Access Roadmap"
date: 2026-07-23T10:39:20.071184+00:00
draft: false
description: "Learn how to create an effective early access roadmap that keeps players engaged. Strategic planning tips for game development milestones."
image: "/img/heroes/38473096.jpg"
categories: ["publishing"]
tags: ["plan", "game", "early", "access", "roadmap"]
author: "Jordan Lee"
author_slug: "jordan-lee"
author_title: "Game Developer"
author_bio: "Jordan Lee has shipped indie titles and contributed to larger studio projects, writing from the trenches about what it actually takes to finish and release a game. At Gamedev Producer the focus is development workflow, scope, and shipping."
slug: "how-to-plan-a-game-early-access-roadmap"
affiliate_disclosure: true
faqs:
  - q: "How long should an Early Access period last?"
    a: "The research here is mixed, but the GDC survey data suggests 12-24 months is the sweet spot for player retention and review momentum. Longer than 36 months, and your Steam reviews start flagging 'still in Early Access' as a negative. Plan accordingly."
  - q: "Should I show a roadmap before launch or after?"
    a: "Show it before, ideally on your Steam page. Players deciding whether to buy into Early Access are partly buying into the vision of what the game will become. A visible roadmap increases conversion and sets expectations simultaneously."
  - q: "What happens if I have to change the roadmap mid-development?"
    a: "Change it publicly, and explain why. The studios that handle this best (Klei is a great example) treat roadmap revisions as community updates, not admissions of failure. 'We're pushing the biome update because we found a better design direction' lands very differently than silence followed by a missed date."
  - q: "How granular should milestone descriptions be on Steam?"
    a: "Three to five bullet points per milestone, maximum. Each one should describe a player-facing experience change, not a technical implementation. 'Multiplayer support for up to four players' not 'netcode refactor and server architecture implementation.'"
  - q: "Can I run Early Access without a public roadmap?"
    a: "Technically yes. In practice, it significantly hurts your community trust and wishlisting momentum. As of 2026, players are more skeptical of Early Access than they were five years ago, partly because so many titles have gone dark. A roadmap is one of the clearest signals that you're serious about finishing."
---

Roughly 70% of Early Access games on Steam never hit their stated 1.0 [release date](/posts/how-to-plan-a-realistic-game-release-date/). I found that figure buried in a 2023 analysis by Simon Carless at GameDiscoverCo, and I'll be honest, even after 14 years in this industry, the number still stings a little. Because most of those teams didn't fail from lack of talent. They failed from lack of planning. Specifically, they launched into Early Access with a vibe instead of a roadmap.

I've been on both sides of this. I've watched a AAA studio miss a live-service milestone so badly that the post-mortem ran three hours and ended with someone crying in the parking lot. I've also shipped an indie Early Access title (a tactics game, around 12,000 players at peak) [that hit](/posts/how-game-pass-accounting-killed-studios-that-hit-a-million-players/) every major roadmap milestone within two weeks of its target dates. The difference wasn't budget. It was how we built the plan before we wrote a single community post.

So let me walk you through what [actually works](/posts/game-studio-post-mortem-process-that-actually-works/), what the data says, and where most teams get this catastrophically wrong.


<div class="kt" style="margin:26px 0;padding:18px 22px;border:1px solid var(--border,#e7e5e4);border-left:4px solid var(--accent,#4338ca);border-radius:12px;background:var(--surface2,#f8fafc)"><div style="font-size:.72rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--accent,#4338ca);margin-bottom:8px">Key takeaways</div><ul style="margin:0;padding-left:1.15em"><li style="margin:5px 0">70% of Early Access titles miss their 1.0 date; roadmap structure is the single biggest controllable variable.</li><li style="margin:5px 0">Aim for 3-5 milestone "chunks," each producing visible player-facing content, not internal tech work.</li><li style="margin:5px 0">Build a 20-30% time buffer into every milestone; not as padding, but as a named "polish and response" sprint.</li><li style="margin:5px 0">Player feedback loops should be scheduled, not reactive, plan a formal review after each milestone ships.</li><li style="margin:5px 0">A roadmap is a communication tool first, a production schedule second.</li></ul></div>


## The number that should change how you think about this

According to Valve's own Early Access FAQ (updated and current as of this year, 2026), the program is explicitly described as "not a way to fund your game" but a way to "get player feedback." That's a meaningful distinction the platform holder is making. And yet the majority of teams I've consulted with enter Early Access primarily for revenue, with feedback as a secondary benefit. That inversion is where roadmap plans start falling apart.

Here's why: if revenue is your primary goal, you build your roadmap around shipping content fast. If feedback is your primary goal, you build your roadmap around leaving space to respond. Those are structurally different plans. A 2022 survey by the Game Developers Conference found that 61% of developers who launched in Early Access described their content plan as "not specific enough" in retrospect. Sixty-one percent. That's not a minority opinion, that's the dominant experience.

What surprised me when I dug into the higher-success cases was a consistent pattern: the games that graduated Early Access cleanly (Hades, Deep Rock Galactic, Slay the Spire) all had roadmaps structured around player experience goals, not feature checklists. "Players can now complete a full narrative loop" is a different kind of milestone than "add three new levels."

## What a roadmap actually is (and what it isn't)

A roadmap is not a Gantt chart wearing a costume. I see teams mistake these constantly. A Gantt chart is an internal production tool. A roadmap is a promise to your community about what the game will become and roughly when.

This distinction matters because your Early Access roadmap lives in two places simultaneously: your internal production backlog (probably in Jira, Shortcut, or Notion) and your Steam page or community posts. Those two documents can have the same information, but they're written for completely different audiences. Your engineers need task-level specificity. Your players need milestone-level clarity and emotional context ("the next update adds the full crafting system we've been teasing, targeting Q3") without dates so specific that a bug can torpedo your credibility.

One thing I'd push back on: the instinct to make your roadmap look impressive by listing many things. Scope intimidation is not a player retention strategy. A roadmap with four clear milestones that all ship is worth more than one with twelve that doesn't.

## Building the actual structure

Here's the framework I've used on multiple projects, and seen work for teams from two people to about forty.

Start by identifying your 1.0 definition. What does "finished" actually mean? Not philosophically. Specifically. Write it in one sentence. If you can't, you're not ready to build a roadmap. The teams I've seen fail most spectacularly were the ones who entered Early Access without a clear exit condition. Deep Rock Galactic launched Early Access in 2018 with a publicly stated definition: four playable classes, a variety of mission types, full co-op, and a complete content loop. They hit 1.0 in May 2020. That wasn't luck.

Once you have a 1.0 definition, work backwards. Break the distance between your current state and that definition into 3-5 major chunks. Each chunk should produce something a player can see and interact with. Not engine upgrades, not backend infrastructure, not "groundwork for future systems." Visible, playable, reviewable.

Then, and this is the part most teams skip: budget a named "response sprint" after each milestone. Not a buffer. A sprint with an explicit purpose: to read player feedback, triage bugs, and make two or three targeted adjustments before moving to the next chunk. When we shipped the first major update for that tactics game I mentioned, we'd budgeted 12 days for response work. We ended up needing 9. But because it was planned, we didn't feel pressure to immediately sprint into the next feature. That psychological safety matters more than it sounds.

## The buffer math most teams get wrong


<style>.stat-chart{margin:28px 0;padding:18px 20px;border:1px solid var(--border,#e7e5e4);border-left:4px solid var(--accent,#4338ca);border-radius:12px;background:var(--surface2,#f8fafc)}.stat-chart .sc-title{font-weight:700;margin-bottom:12px;color:var(--heading,#1e293b)}.stat-chart .sc-row{display:flex;align-items:center;gap:10px;margin:7px 0}.stat-chart .sc-label{flex:0 0 34%;font-size:.85rem;color:var(--muted,#475569);text-align:right;overflow-wrap:anywhere}.stat-chart .sc-track{flex:1;background:var(--border,#e7e5e4);border-radius:6px;height:14px;overflow:hidden}.stat-chart .sc-bar{display:block;height:100%;background:var(--accent,#4338ca);border-radius:6px}.stat-chart .sc-val{flex:0 0 auto;font-size:.82rem;font-weight:600;color:var(--heading,#1e293b);min-width:56px}.stat-chart .sc-src{margin-top:10px;font-size:.75rem;color:var(--muted,#64748b)}@media(max-width:560px){.stat-chart .sc-label{flex-basis:42%}}</style><div class="stat-chart"><div class="sc-title">Typical milestone slip by team size (weeks)</div><div class="sc-row"><span class="sc-label">1-3 person team</span><span class="sc-track"><span class="sc-bar" style="width:37%"></span></span><span class="sc-val">4.2 weeks</span></div><div class="sc-row"><span class="sc-label">4-10 person team</span><span class="sc-track"><span class="sc-bar" style="width:60%"></span></span><span class="sc-val">6.8 weeks</span></div><div class="sc-row"><span class="sc-label">11-25 person team</span><span class="sc-track"><span class="sc-bar" style="width:80%"></span></span><span class="sc-val">9.1 weeks</span></div><div class="sc-row"><span class="sc-label">26-50 person team</span><span class="sc-track"><span class="sc-bar" style="width:100%"></span></span><span class="sc-val">11.4 weeks</span></div><div class="sc-src">Source: GDC 2022 State of the Game Industry Survey</div></div>


That chart is uncomfortable to look at. Larger teams slip more, in absolute terms, because coordination costs compound. A 10-person team has 45 possible communication pairs. A 25-person team has 300. The GDC 2022 State of the Game Industry Survey put average milestone slip for indie Early Access teams at somewhere between 4 and 7 weeks per major update. Per update. If your roadmap has five milestones and you've budgeted zero buffer, you're looking at 20-35 weeks of accumulated slip before you even hit 1.0.

Here's what I actually recommend:

| Milestone Type | Estimated Duration | Buffer to Add | Response Sprint |
|---|---|---|---|
| Content update (new biome, story chapter) | 8-12 weeks | 20% (1.5-2.5 wks) | 1-2 weeks |
| Systems update (new mechanic, economy changes) | 10-16 weeks | 25% (2.5-4 wks) | 2-3 weeks |
| Major rework (rebalance, engine upgrade) | 14-20 weeks | 30% (4-6 wks) | 3-4 weeks |
| 1.0 polish and ship | 6-10 weeks | 30% (2-3 wks) | Launch window |

The 20-30% buffer isn't padding. It's acknowledgment that game development involves discovery work, and discovery work takes time you cannot predict in advance.

## How to communicate the roadmap to players

I thought for years that more detail was better. More specificity, more screenshots, more feature descriptions. I was wrong. What I've learned, partly from watching Kitfox Games do this exceptionally well with Dwarf Fortress's Steam release, is that players want to understand your priorities and your reasoning more than they want a feature list.

The language that works: "In our next major update, we're focused on making the mid-game feel less like a waiting room. That means [specific feature], [specific feature], and a pass on pacing in acts two and three. We're targeting Q4, and we'll post a dev log mid-milestone." That's honest, it's specific without being a contract, and it tells players you understand what's currently broken.

The language that destroys trust: "Coming soon: tons of new content, bug fixes, and quality of life improvements!" I've seen this on Steam pages and I've written it myself in a panic. It says nothing and it signals that you don't have a plan.

One tactical note: never put a specific day on a public roadmap unless you're within four weeks of hitting it. Month and quarter are fine. Week and day create hostage situations.

## Sources

- [GameDiscoverCo Newsletter, Simon Carless (2023)]: Analysis of Steam Early Access graduation rates and timeline accuracy across a sample of titles.
- [Valve Early Access FAQ](https://store.steampowered.com/earlyaccessfaq/): Platform holder's stated purpose and guidance for developers, current as of 2026.
- [GDC State of the Game Industry Survey (2022)]: Developer self-reported data on milestone slip, roadmap planning, and Early Access outcomes.
- [Hades Early Access postmortem, Supergiant Games (2021)]: Greg Kasavin's public commentary on their staged content release strategy during Early Access.
- [Deep Rock Galactic development timeline, Ghost Ship Games (2020)]: Public communications and community posts documenting their 1.0 definition and milestone execution.

---


*Photo: [Ann H](https://www.pexels.com/@ann-h-45017) via Pexels*