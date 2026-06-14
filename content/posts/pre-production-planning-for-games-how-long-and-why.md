---
title: "Pre-Production Planning For Games How Long And Why"
date: 2026-05-22T02:30:23.037856+00:00
draft: false
description: "Plan your game's pre-production phase the right way. Discover how long pre-production planning takes, what's involved, and why skipping it can derail your entir"
image: "https://images.pexels.com/photos/7915395/pexels-photo-7915395.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
categories: ["pm frameworks"]
tags: ["pre-production", "planning", "games", "long"]
author: "Ryan Cole"
author_bio: "Ryan Cole covers game production and milestone planning at GameDevProducer."
slug: "pre-production-planning-for-games-how-long-and-why"
affiliate_disclosure: true
faqs:
  - q: "How do you know when pre-production is actually finished?"
    a: "Pre-production is done when you've answered your biggest unknowns, not when you've run out of time or money in the phase. Specifically: your core loop has been tested with real players and validated as fun, your technical risks have resolutions (not workarounds, actual solutions), and your production estimate is based on measured pipeline data from the vertical slice, not guesses. If any of those three things are still open questions, you're not done."
  - q: "Should pre-production time count toward the overall development timeline when pitching to publishers?"
    a: "Yes, and hiding it is a mistake that creates trust problems later. Publishers who fund game development understand pre-production. Pitching a 24-month timeline that quietly omits 6 months of pre-production you've already done, or that compresses it into an unrealistic 2 months, sets up a mismatch between your actual needs and your contractual commitments. Be upfront about the full timeline and make the case for why adequate pre-production reduces their financial risk."
  - q: "What's the most common thing teams skip in pre-production that causes problems later?"
    a: "Player testing of the core loop. Teams fall in love with their concept and skip the uncomfortable step of watching real players interact with a rough prototype. The vertical slice gets polished enough to impress people who are being polite. The first honest external playtest data arrives 18 months into full production. I've seen this pattern enough times that I now treat early external playtesting as a hard milestone, not an optional activity."
  - q: "Can a solo developer or very small team do real pre-production?"
    a: "Absolutely, and it's arguably more important at that scale because you have less capacity to absorb expensive mistakes later. The scope is different. A solo dev's pre-production might be 6-8 weeks of prototype iteration and a 2-week technical spike. The principles are the same: prove your loop works, validate your pipeline, estimate based on real data. Tools like Notion for documentation and Codecks for task tracking keep it lightweight without sacrificing structure."
  - q: "How does pre-production differ on a sequel or a game using an existing engine and IP?"
    a: "Significantly shorter in some areas, not shorter in others. Technical risks are lower if you're on a familiar engine. Art pipeline is more predictable. But design validation still matters, sometimes more, because the temptation on sequels is to assume what worked before will work again without testing it. Some of the most costly production failures I've seen were sequels that skipped design validation because 'we know this IP.' Treat the core loop as unproven until you've tested it, regardless of franchise history."
author_slug: "ryan-cole"
author_title: "Senior Contributing Writer"
---

Most studios blow their launch dates not in production, but months earlier, in a pre-production phase they rushed through or skipped entirely. I've watched teams celebrate hitting "full production" at the three-month mark on a project that needed at least eight months of foundational work, then spend the next two years paying for that decision in crunch, scope cuts, and eventual cancellation. The uncomfortable truth is that pre-production is where your game either gets a real shot at shipping, or gets quietly set up to fail.

## What Pre-Production Actually Is (And What It Isn't)

There's a persistent confusion in studios, especially smaller ones, between pre-production and "the part before we start making the real stuff." That framing is almost always fatal.

Pre-production is not planning meetings and concept art and vibes. It's a structured phase where you prove your core game loop works, establish your technical pipeline, and answer the most expensive questions before you've hired 30 people to assume the answers. The deliverable isn't a design doc. It's validated decisions. Prototype that tested with actual players. A vertical slice that shows you can hit your art bar. A technical proof-of-concept that confirms your engine can do what you need it to do.

What it isn't: a phase you sprint through to get to the "real" production. I've seen teams treat pre-production as a formality, a box to check before the actual work begins. Those teams almost universally hit a wall around month 8 of full production when they discover their core mechanic doesn't feel good, their tech stack can't support the feature set they promised, or their art pipeline takes three times longer than estimated.

## How Long Pre-Production Should Actually Take

Here's where I'll be honest: there's no universal answer, and anyone who tells you otherwise is selling something. The research and industry data here is genuinely mixed, and the range is wide. But there are patterns.

For a small indie team (2-5 people) making a focused game, pre-production typically runs 3 to 6 months. For a mid-size project with 10-20 people targeting console release, 6 to 12 months is more realistic. For a large-scale project, pre-production can legitimately run 18 to 24 months before a full team ramps up.

The factors that push pre-production longer:

- New technology or a custom engine (add 3-6 months minimum)
- First game in a genre your team hasn't shipped before
- Live service or multiplayer infrastructure that needs validation
- External dependencies like licensed IP, platform partnerships, or co-development

What surprised me when I started digging into post-mortems was how consistently studios that shipped on time reported longer pre-production phases than the industry average, not shorter ones. The teams that "moved fast" in pre-production almost always made up for it in extended full production, emergency redesigns, or post-launch patches that essentially rebuilt systems. They didn't save time. They deferred costs.

## The Core Outputs Pre-Production Has to Deliver

If you're unsure whether your pre-production is actually done, look at what you have at the end. A completed pre-production phase should produce:

**1. A validated prototype**
Not a polished demo. A rough, functional test of your core loop that real people outside your team have played. If your core mechanic isn't fun in a grey-box prototype, it won't magically get fun when you add final art.

**2. A technical vertical slice**
One representative level or section built to final quality through your actual pipeline. Not to show publishers (though that helps). To reveal how long things actually take and where the pipeline breaks.

**3. A production plan with genuine estimates**
Not a wishlist. A schedule built from the vertical slice data, where you know your art team can produce X assets per sprint because you measured it. Tools like [Hacknplan](https://hacknplan.com/) or [Codecks](https://www.codecks.io/) are well-suited to this kind of game-specific planning, and they handle the granular task tracking better than generic tools like Jira for smaller teams.

**4. Defined scope with cut criteria**
What's in the game, what's a stretch goal, and critically, what are you willing to cut if you fall behind? Teams that don't define cut criteria in pre-production make those decisions under pressure in full production, and pressure-driven scope decisions are almost never good ones.

**5. A staffing and budget plan**
Based on real pipeline data, not optimistic assumptions.

## A Practical Framework for Structuring Your Pre-Production

Here's a rough phase breakdown that has worked in my experience for a mid-size project:

| Phase | Duration | Primary Goal |
|---|---|---|
| Concept Validation | 4-6 weeks | Is this a game worth making? Core mechanic prototype. |
| Technical Investigation | 4-8 weeks | Can we build this with our stack? Resolve major tech risks. |
| Vertical Slice | 8-12 weeks | Can we hit our quality bar? Build one section to ship quality. |
| Production Planning | 2-4 weeks | What does full production actually cost and how long does it take? |

These phases aren't always sequential. Technical investigation often overlaps with concept validation. But they all need to happen before you call pre-production done. Skipping any one of them is where the surprises come from.

For reading that goes deep on this, Jason Schreier's *Blood, Sweat, and Pixels* is less a how-to and more a diagnostic tool, a look at what actually went wrong in real productions. Pair it with the [MasterClass game design course from Will Wright](https://www.masterclass.com/instructors/will-wright) if you want more structured methodology around early design validation.

## The Business Case for Longer Pre-Production

I know the counterargument. Budget is tight. Investors want to see progress. Publishers want a greenlight build by a specific date. Burning runway on pre-production feels like burning money on something that doesn't ship.

Here's the math that changed my mind. If your full production team costs $150,000 per month in salaries and overhead, and your production runs 6 months longer than planned because of a design pivot in month 10, that's $900,000 in unplanned costs. A longer pre-production that costs you 3 extra months at a 5-person team might cost $75,000. The risk-adjusted math almost always favors more pre-production investment, not less.

The studios I've watched scale well understand that pre-production is essentially risk purchasing. You're paying to eliminate the most expensive unknowns before the team is big enough that surprises become catastrophic.

---

## FAQ

### How do you know when pre-production is actually finished?

Pre-production is done when you've answered your biggest unknowns, not when you've run out of time or money in the phase. Specifically: your core loop has been tested with real players and validated as fun, your technical risks have resolutions (not workarounds, actual solutions), and your production estimate is based on measured pipeline data from the vertical slice, not guesses. If any of those three things are still open questions, you're not done.

### Should pre-production time count toward the overall development timeline when pitching to publishers?

Yes, and hiding it is a mistake that creates trust problems later. Publishers who fund game development understand pre-production. Pitching a 24-month timeline that quietly omits 6 months of pre-production you've already done, or that compresses it into an unrealistic 2 months, sets up a mismatch between your actual needs and your contractual commitments. Be upfront about the full timeline and make the case for why adequate pre-production reduces their financial risk.

### What's the most common thing teams skip in pre-production that causes problems later?

Player testing of the core loop. Teams fall in love with their concept and skip the uncomfortable step of watching real players interact with a rough prototype. The vertical slice gets polished enough to impress people who are being polite. The first honest external playtest data arrives 18 months into full production. I've seen this pattern enough times that I now treat early external playtesting as a hard milestone, not an optional activity.

### Can a solo developer or very small team do real pre-production?

Absolutely, and it's arguably more important at that scale because you have less capacity to absorb expensive mistakes later. The scope is different. A solo dev's pre-production might be 6-8 weeks of prototype iteration and a 2-week technical spike. The principles are the same: prove your loop works, validate your pipeline, estimate based on real data. Tools like [Notion](https://www.notion.so/) for documentation and [Codecks](https://www.codecks.io/) for task tracking keep it lightweight without sacrificing structure.

### How does pre-production differ on a sequel or a game using an existing engine and IP?

Significantly shorter in some areas, not shorter in others. Technical risks are lower if you're on a familiar engine. Art pipeline is more predictable. But design validation still matters, sometimes more, because the temptation on sequels is to assume what worked before will work again without testing it. Some of the most costly production failures I've seen were sequels that skipped design validation because "we know this IP." Treat the core loop as unproven until you've tested it, regardless of franchise history.

---

The studios shipping games on time and on budget aren't the ones who found a way to skip pre-production. They're the ones who figured out how to run it with discipline and treat it as the highest-leverage phase of development. Spend the time. Answer the expensive questions early. The game you actually ship will be better for it.

*Photo: [RDNE Stock project](https://www.pexels.com/@rdne) via Pexels*