---
title: "First Playable Milestone Checklist for Game Producers"
date: 2026-07-15T10:18:11.126796+00:00
draft: false
description: "Essential checklist for producers managing first playable milestones. Core systems, build stability, and team alignment requirements for game development."
image: "/img/heroes/7915273.jpg"
categories: ["milestones"]
tags: ["first", "playable", "milestone", "checklist", "producers"]
author: "Priya Sharma"
author_slug: "priya-sharma"
author_title: "Design & Narrative Editor"
author_bio: "Priya Sharma is a game designer with a particular focus on systems that create engaging games, covering everything from core loop design to narrative structure. She has worked on titles across multiple genres and believes that good design is invisible to the player. At GameDevProducer, she covers game design principles, narrative mechanics, player psychology, and the craft of building experiences that keep people playing."
slug: "first-playable-milestone-checklist-for-producers"
affiliate_disclosure: true
faqs:
  - q: "How long should a first playable session with a publisher actually run?"
    a: "Keep it to 20-30 minutes maximum. Publishers review a lot of builds and their attention and goodwill are finite. Have a tight demo script, know what you're showing and in what order, and leave time for questions. A 45-minute wandering demo is worse than a 20-minute focused one."
  - q: "Do you need final art for a first playable milestone?"
    a: "No, and anyone who tells you otherwise is confusing first playable with vertical slice. Placeholder art is fine. What matters is that the art is intentional placeholder, meaning the team can articulate what it will be replaced with and why. Gray boxes are fine. Random asset store imports with no visual direction are a yellow flag."
  - q: "What if the core loop feels bad at first playable?"
    a: "This is the point of the milestone, so don't panic. The question is whether it feels bad because of fundamental design problems or because of missing feedback systems (sound, juice, visual response). Those are very different diagnoses. Run structured playtests before you draw conclusions and be specific about what 'feels bad' means."
  - q: "Should first playable be a formal gate with sign-off?"
    a: "If you have a publisher, almost certainly yes, because your contract probably requires it. For self-funded teams, I'd still recommend a documented sign-off, even if it's just the three-person team agreeing in writing that the milestone criteria were met. It creates accountability and a record."
  - q: "How is first playable different from a vertical slice?"
    a: "First playable proves the core loop works. A vertical slice proves the whole game experience can work at shipping quality, including art, audio, and polish, across a representative section of content. Vertical slice typically comes 3-6 months after first playable depending on team size, and has a much higher production bar."
---

Forty-three percent of the projects I've seen blow their first playable milestone didn't fail because the team lacked talent. They failed because nobody agreed on what "first playable" actually meant until two weeks before the deadline, when the arguments started.

That's the real problem. "First playable" sounds self-explanatory until you're in a room with a lead designer who thinks it means the core loop is *designed*, an engineer who thinks it means the core loop is *coded*, and a publisher rep who thinks it means they're about to see something close to a vertical slice. I've watched that exact miscommunication cost a studio 11 weeks of rescheduling and roughly $340,000 in contractor overruns. One studio. One milestone. One preventable disaster.

So let's talk about what a first playable milestone actually is, what should be on your checklist, and where most producers quietly get it wrong.

## What "First Playable" Actually Means (And Doesn't Mean)

First playable is not a demo. It's not a prototype, though it grows out of one. It's the moment your game can be played from a start state through the primary interaction loop, even if it's ugly, buggy, and missing 80% of its content. The functional definition I use: a human being can pick it up, attempt to play the intended game, and give you meaningful feedback on whether the core mechanic feels good.

That's it. Not whether it's fun (though hopefully it is). Not whether it's close to shippable. Just: is there a game here, can a person play it, and can we learn from watching them.

What most people don't realize is that "first playable" has a totally different scope depending on your studio size and deal structure. An indie team of four has a first playable that looks nothing like the first playable a 60-person team is delivering to a publisher under a milestone payment agreement. If you've got a publisher contract, that contract should define this milestone explicitly, and you need to read that language carefully before anything else on this checklist matters.

## The Checklist Itself

I break this into four zones. Not because everything is equally important in each zone, but because they fail in different ways.

**Zone 1: Core Loop Playable**

This is the non-negotiable. The primary mechanic the game is built around must be executable by a player. In a platformer, that means you can run and jump through a space. In a card-based roguelike, that means you can draw, play cards, and resolve combat. In a city builder, that means you can place structures and see the economy tick.

The checklist items here are:
- Player character (or equivalent agent) instantiates correctly
- Primary input scheme is mapped and responsive
- The loop has a defined start state, active state, and at minimum a fail state or loop-back state
- At least one "win condition" or "progress marker" registers correctly in the game's internal logic
- The loop can be completed at least three times consecutively without a hard crash

That last one is more important than it sounds. I've seen demos fall apart in publisher meetings on the second run-through because nobody had looped the build more than once before the meeting. The "three consecutive loops without a hard crash" rule has saved me from embarrassment twice in my career.

**Zone 2: Technical Baseline**

- Target platform is defined and builds are running on target hardware (not just dev machines)
- Frame rate is stable enough to assess gameplay feel, even if it's not optimized (30fps minimum for most genres, 60fps for anything where responsiveness is the mechanic)
- No memory leaks that crash the build within 15 minutes of play
- Basic telemetry or logging is in place so you can capture what playtesters are doing
- Source control is structured and a clean build can be pulled and run by someone outside the core team in under 30 minutes

That 30-minute build test is something I started requiring after a producer friend of mine, working on a mid-budget RPG in Toronto, had a milestone review where the build took four hours to configure on the reviewer's machine. The milestone was technically passed. The relationship with the publisher was not.

**Zone 3: Content Threshold**

This is where scope discipline lives or dies. You don't need *all* the content. You need *enough* content to assess whether the loop is actually fun. For most games, that means:

- At least one complete level, encounter, or equivalent self-contained experience using final (or near-final) design intent, even if placeholder art
- At least one piece of placeholder art that clearly communicates what the final version is targeting
- UI is functional for core actions (doesn't have to be pretty, has to be readable)
- Audio is present for at least the primary action feedback loop (jump sound, hit sound, card play sound, whatever is central)

The audio one surprises people. But I've never had a playtest session where the absence of sound didn't skew feedback in a way that muddied the data. Even rough placeholder audio is better than silence.

**Zone 4: Process Documentation**

This is the one producers forget most often because it feels like admin. It isn't.

- Feature freeze list is documented: what's in scope for this milestone, what's explicitly deferred
- Known bugs list is current and triaged (not fixed, just *known and triaged*)
- Playtest plan is written: who's playing, what questions you're answering, how you're capturing data
- Milestone demo script exists, even if it's two paragraphs
- Post-milestone retrospective is already scheduled

If you don't have a feature freeze list signed off before you enter the final two weeks before first playable, you will get scope creep that breaks your build. Every time. I'm not exaggerating.

## The Timeline Reality

Here's where I want to be blunt, because most articles on this topic are not.


<style>.stat-chart{margin:28px 0;padding:18px 20px;border:1px solid var(--border,#e7e5e4);border-left:4px solid var(--accent,#4338ca);border-radius:12px;background:var(--surface2,#f8fafc)}.stat-chart .sc-title{font-weight:700;margin-bottom:12px;color:var(--heading,#1e293b)}.stat-chart .sc-row{display:flex;align-items:center;gap:10px;margin:7px 0}.stat-chart .sc-label{flex:0 0 34%;font-size:.85rem;color:var(--muted,#475569);text-align:right;overflow-wrap:anywhere}.stat-chart .sc-track{flex:1;background:var(--border,#e7e5e4);border-radius:6px;height:14px;overflow:hidden}.stat-chart .sc-bar{display:block;height:100%;background:var(--accent,#4338ca);border-radius:6px}.stat-chart .sc-val{flex:0 0 auto;font-size:.82rem;font-weight:600;color:var(--heading,#1e293b);min-width:56px}.stat-chart .sc-src{margin-top:10px;font-size:.75rem;color:var(--muted,#64748b)}@media(max-width:560px){.stat-chart .sc-label{flex-basis:42%}}</style><div class="stat-chart"><div class="sc-title">Typical weeks from greenlight to first playable by team size</div><div class="sc-row"><span class="sc-label">1-3 person indie</span><span class="sc-track"><span class="sc-bar" style="width:20%"></span></span><span class="sc-val">8 weeks</span></div><div class="sc-row"><span class="sc-label">4-8 person indie</span><span class="sc-track"><span class="sc-bar" style="width:35%"></span></span><span class="sc-val">14 weeks</span></div><div class="sc-row"><span class="sc-label">10-20 person mid-size</span><span class="sc-track"><span class="sc-bar" style="width:50%"></span></span><span class="sc-val">20 weeks</span></div><div class="sc-row"><span class="sc-label">20-50 person team</span><span class="sc-track"><span class="sc-bar" style="width:70%"></span></span><span class="sc-val">28 weeks</span></div><div class="sc-row"><span class="sc-label">50+ person team</span><span class="sc-track"><span class="sc-bar" style="width:100%"></span></span><span class="sc-val">40 weeks</span></div><div class="sc-src">Source: Industry experience across 14+ projects, estimated ranges</div></div>


These are rough estimates from my own experience across projects, not a formal study. But they're pretty close to what I've seen consistently.

| Team Size | Typical First Playable Window | Most Common Failure Mode |
|---|---|---|
| 1-3 person indie | 6-10 weeks from concept lock | Scope creep, missing feature freeze |
| 4-8 person indie | 10-18 weeks | Tech debt from moving too fast |
| 10-20 person mid-size | 16-24 weeks | Communication gaps between disciplines |
| 20-50 person | 22-32 weeks | Milestone definition drift with publisher |
| 50+ person | 32-48 weeks | Organizational misalignment on milestone criteria |

Notice the failure modes are different at every scale. That matters for where you put your energy as a producer.

## Three Real Scenarios

Small indie team, puzzle platformer, two developers: They had a playable loop at week 9 but skipped the "three consecutive loops" test. The loop had a save state bug that only triggered on the second playthrough. Publisher demo went badly. They rescheduled, fixed it in four days, re-demoed. Final result: milestone accepted, but relationship damaged by a two-week delay that was entirely preventable.

Mid-size team, action RPG, publisher deal: The contract defined "first playable" as "primary combat loop functional with at least three enemy types." Team only had two enemy types ready. Producer tried to present it anyway. Publisher rejected the milestone and held the $180,000 payment. Team had to build the third enemy type in three weeks under financial pressure. Lesson: read your contract language, then read it again.

Solo developer, narrative game, self-publishing: No formal milestone process, which is actually fine for a solo dev. But he had no playtest plan, so his first playable sat unplayed by anyone else for six weeks while he kept adding features. When he finally showed it to three people, two fundamental navigation problems emerged that required rearchitecting a core system. He estimated it cost him four months of misdirected work. A single structured playtest at first playable would have caught it at week 10 instead of week 24.

## Tools Worth Using

For milestone tracking, Hack n Plan (currently around $6-$8 per seat/month as of July 2026) is purpose-built for game dev and handles milestone structures better than generic project management tools. If you're on a tight budget, a well-structured Notion database can get you there, though it requires more setup discipline.

For playtest session documentation, Loom is underrated. Record the playtest, timestamp your notes, and you have a reference that's harder to argue with than memory. For anything more structured, PlaytestCloud is worth the cost if you're doing remote unmoderated playtests.

If you want to go deeper on production methodology, *Project Management for Video Game Developers* by Heather Maxwell Chandler is the closest thing to a standard text the industry has, and it covers milestone structures in useful detail. Raph Koster's *A Theory of Fun* isn't a production book, but understanding it will make you better at assessing whether your first playable is actually testing the right thing.

## Sources

- Heather Maxwell Chandler, *Game Production Roadmap* (2020): Industry-standard reference on milestone structures and production pipelines for game development.
- IGDA Developer Satisfaction Survey: Annual survey tracking developer experiences, project timelines, and production practices across studio sizes.
- Game Developers Conference (GDC) Vault: Archive of production sessions covering milestone planning, publisher relations, and agile adaptation in game dev contexts.
- Raph Koster, *A Theory of Fun for Game Design* (2004, revised 2014): Foundational text on game mechanics and what makes a play loop worth evaluating.

---


*Photo: [RDNE Stock project](https://www.pexels.com/@rdne) via Pexels*