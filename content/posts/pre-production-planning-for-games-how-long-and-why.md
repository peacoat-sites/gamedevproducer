---
title: "Pre-Production Planning For Games How Long And Why"
date: 2026-05-22T02:30:23.037856+00:00
draft: false
description: "Plan your game's pre-production phase the right way. Discover how long pre-production planning takes, what's involved, and why skipping it can derail your entir"
image: "https://images.pexels.com/photos/4792491/pexels-photo-4792491.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
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
lastmod: 2026-07-07
---
Most studios miss their launch dates not because production goes sideways, but because they gutted pre-production six months earlier. I've watched teams pop champagne over hitting "full production" at the three-month mark on a project that needed eight months of groundwork, then spend the next two years in crunch, cutting features, and eventually canceling the whole thing. The hard part nobody wants to admit: pre-production is where your game either gets a real shot or gets quietly set up to fail.

## What Pre-Production Actually Is (And What It Isn't)

There's confusion in most studios, especially small ones, about what pre-production even means. They treat it like "the stuff before the real work starts," which is almost always fatal.

Pre-production isn't planning meetings and concept art and vibes. It's a structured phase where you prove your core loop actually works, establish your technical pipeline, and answer the expensive questions before you've hired 30 people betting on answers you haven't validated. The deliverable isn't a design doc. It's tested decisions. A prototype actual players have played. A vertical slice that proves you can hit your art quality. A technical proof-of-concept showing your engine can handle what you're promising.

What it isn't: a box to check before the "real" production starts. I've seen teams sprint through pre-production like they're late for something. By month 8 of full production, they hit a wall. The core mechanic doesn't feel good. The tech stack can't support the promised features. The art pipeline takes three times longer than they estimated. Now they're paying.

## How Long Pre-Production Should Actually Take

| Team Size | Project Type | Pre-Production Duration | Notes |
|---|---|---|---|
| 2-5 people | Focused indie | 3-6 months | Small scope, single-genre focus |
| 10-20 people | Mid-size console | 6-12 months | Established pipeline, known tech |
| Large team | Large-scale | 18-24 months | Complex scope, new tech risk, ramp-up time |
| Any size | New engine/tech | +3-6 months | Adds to base duration |
| Any size | New genre for studio | +3-6 months | First-time learning curve |
| Any size | Live service/multiplayer | +3-6 months | Infrastructure validation required |

There's no universal answer, and anyone claiming otherwise is selling you something. The industry data is genuinely all over the place. But patterns exist.

Small indie teams (2-5 people) making something focused: 3 to 6 months. Mid-size projects with 10-20 people on console: 6 to 12 months. Large-scale work: 18 to 24 months before you ramp up your full team.

What extends pre-production:

- New technology or a custom engine (adds 3-6 months minimum)
- First game in a genre your studio hasn't shipped before
- Live service or multiplayer infrastructure needing validation
- Licensed IP, platform exclusivity deals, or co-development commitments

What actually surprised me digging through post-mortems: studios that shipped on time reported longer pre-production phases than the industry average. Not shorter. The teams that "moved fast" in pre-production made it up elsewhere, in extended production or emergency redesigns or post-launch patches that basically rebuilt systems. They didn't save time. They just moved the cost.

## The Core Outputs Pre-Production Has to Deliver

Not sure if pre-production is actually finished? Look at what you have.

**1. A validated prototype**
Not polished. Functional and rough. Real people outside your team have played it. If your core mechanic isn't fun in a grey-box prototype, final art won't save it.

**2. A technical vertical slice**
One representative section built to final quality through your actual pipeline. Not for publishers (though that helps). To reveal how long things actually take and where the pipeline breaks.

**3. A [production plan with real estimates](/how-to-write-a-game-production-milestone-document/)**
Not a wish list. A schedule built from vertical slice data, where you know your art team produces X assets per sprint because you measured it. Tools like [Hacknplan](https://hacknplan.com/) or [Codecks](https://www.codecks.io/) handle game-specific planning better than generic tools like Jira, especially for smaller teams.

**4. Defined scope with cut criteria**
What's in. What's stretch. What are you willing to cut if you fall behind? Teams that skip this step make those decisions under pressure in full production, and panic cuts are almost never good ones.

**5. A staffing and budget plan**
Based on actual pipeline data, not optimism.

## A Practical Framework for Structuring Your Pre-Production

Here's how a mid-size project typically breaks down:

| Phase | Duration | Primary Goal |
|---|---|---|
| Concept Validation | 4-6 weeks | Is this a game worth making? Core mechanic prototype. |
| Technical Investigation | 4-8 weeks | Can we build this with our stack? Resolve major tech risks. |
| Vertical Slice | 8-12 weeks | Can we hit our quality bar? Build one section to ship quality. |
| Production Planning | 2-4 weeks | What does full production actually cost and how long does it take? |

These aren't always sequential. Technical investigation overlaps with concept validation constantly. But all of them need to happen before you're done. Skip one, and that's where the disasters start.

Jason Schreier's *Blood, Sweat, and Pixels* is less how-to and more diagnostic tool, a look at what actually broke in real productions. Pair it with the [MasterClass game design course from Will Wright](https://www.masterclass.com/instructors/will-wright) for structured methodology around early design validation.

## The Business Case for Longer Pre-Production

## Sources

- [Hacknplan](https://hacknplan.com/)
- [Codecks](https://www.codecks.io/)
- [MasterClass game design course from Will Wright](https://www.masterclass.com/instructors/will-wright)
- [Anete Lusina](https://www.pexels.com/@anete-lusina)
- is genuinely all over the place


I get the counterargument. Budget's tight. Investors want to see progress. Publishers want a greenlight build. Pre-production feels like burning money on something that doesn't ship.

The math is different. Say your full production team costs $150,000 a month. Production runs six months longer than planned because of a design pivot in month 10. That's $900,000 in costs you didn't budget. A longer pre-production costing three extra months at a five-person team runs $75,000. The actual math favors pre-production investment, not cuts.

Studios that scale well understand pre-production as risk purchasing. You're paying to kill the most expensive unknowns before the team grows big enough that surprises become catastrophic.

---

The studios shipping games on schedule and on budget aren't the ones who found a way to skip pre-production. They're the ones who ran it with discipline and treated it as their highest-leverage phase. Spend the time. Answer the expensive questions early. The game you actually ship will be better.

*Photo: [Anete Lusina](https://www.pexels.com/@anete-lusina) via Pexels*