---
title: "Game Development Schedule Planner: Free Milestone and Roadmap Tool"
hide_title: true
date: 2026-10-06
lastmod: 2026-10-06
slug: "game-development-schedule-planner"
categories: ["planning"]
tool: true
description: "Free game development schedule planner. Enter a launch or start date, scope and platforms to get alpha, beta, certification, Steam Coming Soon and Next Fest dates with a protected buffer. Export to CSV or your calendar."
image: "/img/heroes/273153.jpg"
author: "Stephen Brenish"
author_slug: "stephen-brenish"
author_title: "Lead Game Producer"
author_bio: "Stephen Brenish is a Lead Game Producer at Epic Games (Fortnite, Unreal Engine) and founder of GameDevProducer, with 14+ years shipping and running live games at scale (previously Senior Program Manager at Blizzard Entertainment). Certified ScrumMaster."
faqs:
  - q: "How long does it take to make a video game?"
    a: "It depends almost entirely on scope. A focused prototype or demo can take two to eight months, a small indie game six to fifteen months, a full indie release one to two and a half years, a mid-size AA game around two to three and a half years, and a AAA game three years or more. The planner uses those ranges as defaults and warns you when your total time is short for the scope you picked."
  - q: "What is the difference between alpha and beta in game development?"
    a: "Alpha means feature complete: every feature is in and playable end to end, even if rough, and no new features are added afterwards. Beta means content complete: all levels, assets and text are in, and the team's effort shifts entirely to bugs, performance and polish. Treat both as definitions with exit criteria, not just dates."
  - q: "How much buffer should a game schedule have?"
    a: "Most teams protect somewhere between 10 and 25 percent of the schedule as explicit contingency. The planner defaults to 15 percent and places it as its own block after content complete, so you can see it, track what consumes it, and avoid quietly spending it on new features."
  - q: "How far ahead of launch should my Steam page go live?"
    a: "Valve requires a Coming Soon page to be live for at least two weeks before release, and you should submit it for review at least seven business days before you want it public. In practice you want it up much earlier, usually six months or more, because every week it is live collects wishlists. The planner schedules it just after your vertical slice, when you have footage worth showing."
  - q: "When should I submit my game for console certification?"
    a: "Leave a protected window before launch that is long enough for at least one failed submission and a resubmission. The planner reserves about ten weeks of release work for console projects, with the first submission roughly eight weeks before launch and gold master two weeks out. The exact requirements are confidential to licensed developers, so confirm timelines with each platform holder."
  - q: "Can I export the schedule?"
    a: "Yes. Download it as a CSV for Excel or Google Sheets, add every milestone to Google Calendar, Outlook or Apple Calendar with the .ics file, copy a share link that reopens your exact plan, or print it."
---

A game schedule is a list of promises about when specific things will be true: the core loop is fun, every feature works, all the content is in, the build passes certification. This planner turns your launch date (or your start date), scope and platforms into those promises. It shows every phase, every milestone, the platform and Steam deadlines that catch teams out, and an explicit buffer you can defend.

Fill in the four fields below and the plan updates as you type. Nothing is sent anywhere; it all runs in your browser.

{{< schedule-planner >}}

## How the planner builds your schedule

Three rules shape every plan it produces.

**Buffer lives inside the date, not after it.** Your total time runs from the start of concept to launch day. The planner carves your contingency out of that total and places it as its own block after content complete. A visible buffer gets managed. Buffer hidden inside every task estimate gets spent without anyone noticing, and then the date moves anyway.

**Release work has a floor.** Polishing, locking and shipping a build takes a minimum amount of calendar time no matter how small the game is. The planner reserves at least four weeks for a PC-only release, five for mobile, and ten when you ship on console. When your timeline is short, development gets squeezed instead of the release window, and the plan tells you so.

**Phase proportions follow scope.** Small projects spend proportionally more time finding the fun; large ones spend more in pre-production proving pipelines before the team scales up. These are the defaults, as a share of planned (non-buffer) time:

| Scope | Typical total | Concept | Pre-production | Production | Content complete | Polish and release |
|---|---|---|---|---|---|---|
| Prototype to demo | 2 to 8 months | 10% | 20% | 40% | 15% | 15% |
| Small indie | 6 to 15 months | 8% | 20% | 45% | 14% | 13% |
| Indie | 12 to 30 months | 6% | 20% | 48% | 14% | 12% |
| Mid-size / AA | 22 to 42 months | 5% | 22% | 47% | 14% | 12% |
| AAA | 36 months and up | 5% | 25% | 45% | 13% | 12% |

These are starting points drawn from common production practice, not a law of nature. If your vertical slice estimates say production needs longer, believe the estimates and move the date or the scope.

## The milestones, and what "done" means for each

A milestone is only useful if everyone agrees what has to be true to pass it. Dates without exit criteria turn into arguments about whether you are "basically there."

**Concept greenlight.** The core fantasy works in a rough prototype, and you have agreed the audience, platforms, scope range and budget range. This is the cheapest moment to kill or reshape the project, so treat it as a real decision.

**Vertical slice.** One section of the game at final quality for every discipline: art, audio, design, UI, performance. Its real purpose is estimation. Once you know what one finished minute of gameplay costs, you can plan the rest honestly. The [first playable checklist](/posts/first-playable-milestone-checklist-for-producers/) covers what to check before you call it.

**Alpha, or feature complete.** Every feature is in and playable end to end, even if rough. After alpha, new features are scope changes and go through a decision, not a backlog. More on the definitions in [alpha, beta and gold explained](/posts/what-is-a-game-milestone-alpha-beta-gold/).

**Beta, or content complete.** All levels, assets, text and audio are in. Effort shifts entirely to bugs, performance and polish, and localization strings lock. If content is still arriving, you are not in beta; see [what content complete really requires](/posts/what-is-a-content-complete-milestone-in-games/).

**Code lock and release candidate.** Only critical fixes go in, each through a gate. The release candidate is the build you would ship if nothing else turned up.

**Certification and gold.** On console, the release candidate goes to each platform holder for certification. Gold is the final build approved for release everywhere.

If you report milestones to a publisher, the [milestone document guide](/posts/how-to-write-a-game-production-milestone-document/) shows how to write them so approval is a formality rather than a negotiation.

## Where the buffer belongs, and how to spend it

Put the buffer after content complete and before code lock. That is where late surprises surface: performance problems once everything is in, a platform requirement nobody read, a feature that tests badly. A buffer at that point absorbs those without touching the launch date.

Two habits keep it working. Track what consumes it, by name, at every review. And do not spend it on new features because "we have time"; that is how a 15 percent buffer becomes a two-month slip. The reasoning behind sizing it is in [why buffer time matters in game schedules](/posts/buffer-time-in-game-schedules-why-it-matters/).

## Console certification: protect the window

Every console platform holder runs its own certification: a test pass against technical requirements covering things like save data, account handling, controller disconnects, network errors, system UI and ratings. The detailed requirements are confidential to licensed developers, but the planning lesson is universal: assume your first submission can fail, and leave room to fix and resubmit without moving launch.

The planner reserves that window automatically when you tick console. Age ratings (IARC, ESRB, PEGI and others) need to be secured before you submit, so they appear as their own milestone. For the full process, read [how console certification works for producers](/posts/console-game-certification-process-for-producers/), and work through the [console certification readiness checklist](/console-certification-checklist/) before your first submission.

## Steam dates that catch teams out

Valve's rules are short, but each one can cost you a week or a sale.

- **Coming Soon minimum.** A new product must have a Coming Soon page live for at least two weeks before release. Submit the page for review at least seven business days before you want it public.
- **Build review.** Valve reviews your release build too, typically in three to five business days. Plan for at least seven.
- **Next Fest eligibility.** Your store page must be public, your demo must be playable when the fest starts, and the game must release after the fest ends. Each game gets one Next Fest, and registration closes weeks before the event.
- **The 30-day release cooldown.** You cannot discount for 30 days after release, apart from an optional launch discount of up to 40 percent that runs 7 to 14 days. Launch two weeks before a seasonal sale and you sit that sale out.

The planner applies all four and flags conflicts. For every upcoming sale, fest and deadline in one place, use the [Steam sale and Next Fest calendar](/steam-sale-dates/). To estimate what the wishlists you collect turn into, try the [Steam wishlist calculator](/steam-wishlist-to-sales/).

## Live service and Early Access change the shape

**Live service** games launch into operation rather than finishing. The planner adds a closed technical test after alpha, an open beta or soft launch before launch, a live-ops readiness review (on-call rota, rollback plan, server scaling, incident communications), and Season 1 locked before launch with Season 2 due about ten weeks after. The cadence you announce at launch is the one players will hold you to, so plan the second season before the first one ships. For the longer view, see [how to plan a games-as-a-service roadmap](/posts/how-to-plan-a-games-as-a-service-roadmap/).

**Early Access** launches the game while development continues. Steam asks Early Access titles to explain on the store page what is planned and roughly how long the game will stay in Early Access, so the planner adds your first content update about six weeks after launch. Ship what you promised on the page.

## Five scheduling mistakes that sink launch dates

1. **Treating alpha as a date instead of a definition.** If "alpha" moves whenever the work is not done, it was never a milestone. Write the exit criteria first.
2. **No explicit buffer.** Padding every task feels safe and is not. Hold contingency in one visible block.
3. **Planning certification as a formality.** It is a test you can fail. Schedule the resubmission.
4. **Putting the store page up late.** Wishlists accumulate over time. A page that goes live two months before launch has had two months to collect them.
5. **Never re-planning.** A schedule is a model, and models drift. Re-run the plan at every milestone review with what you now know.

For the wider practice behind this tool, see [how to create a game development schedule](/posts/how-to-create-a-game-development-schedule/), [how to build a game development roadmap](/posts/how-to-build-a-game-development-roadmap/), and the [indie game budget calculator](/indie-game-budget-calculator/) for the cost side of the same plan.
