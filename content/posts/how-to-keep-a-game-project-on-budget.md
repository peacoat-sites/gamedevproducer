---
title: "Stop Game Projects From Bleeding Money"
date: 2026-06-16T13:08:53.550724+00:00
draft: false
description: "Learn proven strategies to keep your game project on budget, from planning and scope control to tracking costs and avoiding common financial pitfalls."
image: "/img/heroes/7821566.jpg"
categories: ["budgeting"]
tags: ["keep", "game", "project", "budget"]
author: "Samantha Roberts"
author_slug: "samantha-roberts"
author_title: "Publishing Strategist"
author_bio: "Samantha Roberts has spent her career navigating the publisher side of the games industry: first pitching indie studios to publishers, then working inside a publishing label evaluating hundreds of projects. She knows what publishers look for and what indie developers consistently get wrong in their pitch decks. At GameDevProducer, she covers publishing strategy, funding, and the business of bringing a game to market."
slug: "how-to-keep-a-game-project-on-budget"
affiliate_disclosure: true
faqs:
  - q: "How much contingency should a game budget include?"
    a: "The standard advice is 10-15%, but I think that's too low for anything with technical risk or a small team. I budget 20% on any project where there are unknowns I can't price out precisely, and on projects involving new engine versions, online features, or first-time contractors, I'll go to 25%. Contingency isn't pessimism; it's just accounting for reality."
  - q: "Should marketing come out of the development budget?"
    a: "Yes, always. Treating marketing as a separate problem to solve after you ship is one of the most common and most damaging mistakes indie teams make. You don't have to spend all of it during development, but the money needs to be allocated and reserved from the start."
  - q: "How do I track budget if I'm a solo developer?"
    a: "A single spreadsheet with two tabs: one for your total budget broken into categories, and one for actuals you update weekly. Track your own time even if you're not paying yourself, because it tells you if the project is on schedule, and schedule is budget. If you use a tool, Notion or even Trello with a time-tracking integration like Toggl (free tier covers most solo use cases) works fine."
  - q: "What's the biggest budget mistake first-time producers make?"
    a: "Underestimating the cost of iteration. First-time producers often budget for building a feature once. Experienced ones know most features get built, revised, and rebuilt at least twice. If your budget only covers the first pass, you're already in trouble by the time you hit playtesting."
  - q: "Is it worth hiring a dedicated producer for a small indie game?"
    a: "Depends entirely on team composition. If nobody on the team has a background in project management or finance, even a part-time producer at 10-15 hours a week can prevent overruns that would cost far more than their fee. The research here is genuinely mixed on ROI for very small projects, but my instinct from watching teams work is that the answer is yes more often than most developers want to admit."
lastmod: 2026-07-08
---
Sixty percent of the indie games I've seen die in development don't die because the idea was bad. They die because the money ran out three months before the game did.

I'll be honest: I spent years at a mid-size AAA studio where budget overruns were almost a ritual. We'd start a project with $4 million approved, and by alpha we'd be presenting a revised scope document to justify the $5.8 million we'd already spent. It was normalized. Nobody got fired. The publisher absorbed it because the title had enough commercial potential to survive the bleed. When I went indie, I had to completely rewire how I think about money in game development, because [there's no publisher safety net](/funding-options-for-indie-game-studios-explained/) catching your overage. The $40,000 you budgeted is the $40,000 you have. Full stop.

What surprised me most when I started digging into why budgets actually fail is that it's almost never the big items that kill you. It's not the composer fee or the character artist's contract. It's the thousand small decisions that each seem fine individually, and then you look at your burn rate in month seven and feel genuinely sick.

Here's what actually works.

## Know Your Real Number Before You Start

Most developers build a budget around what they think the game will cost. The smarter move is to build it around what you can actually afford to lose, and then work backward.

This sounds pessimistic. It's not. It's the single most clarifying exercise I've done on any project. If the game ships and makes nothing, what's the maximum damage you can absorb? That number, not some optimistic revenue projection, is your true ceiling. Everything you plan has to fit inside it, including a contingency buffer of at least 20 percent. If you can't fit the game inside that number with a 20 percent reserve, you either need to find more money or cut scope before you write a single line of code.

The tools I use for the initial budget are boring: a Google Sheet broken into labor, middleware and licensing, hardware and equipment, marketing (yes, this goes in the budget at project start, not as an afterthought), QA, localization, platform submission fees, and miscellaneous. I keep a separate tab just for monthly burn, which is labor plus any recurring costs like a Unity Pro subscription ($185/month as of this year for a small studio seat) or cloud storage. Monthly burn is your heartbeat. You need to know it cold.

Get specific on labor, because vague estimates destroy budgets. Don't write "artist: $15,000." Write out what you're actually buying: 60 hours of character concepting at $85/hour, 120 hours of environment assets at $75/hour. When you break it down, you either validate your estimate or discover it was fantasy. Usually a bit of both.

## Scope Is a Budget Problem, Not a Design Problem

I have never seen a budget overrun that wasn't, at root, a scope problem. Not once. The money doesn't disappear into a void; it gets spent on work that wasn't in the original plan.

Feature creep is the obvious culprit, and everyone knows to watch for it. What people underestimate is what I call scope drift: the slow accumulation of "while we're in there" additions that each take an hour or two but collectively represent weeks of unbudgeted work. The programmer who adds a parallax background because it looks better. The UI that gets rebuilt because the first iteration felt off. None of these show up in a change request. They just happen, and your schedule erodes, and since most game dev labor is time-based, eroding schedule means eroding budget.

The fix isn't a strict no-change policy, which is both impractical and demoralizing. I use a lightweight [change control habit instead](/how-to-plan-a-game-development-budget/). Simple column in the project board (Hacknplan works well for this, and their base tier is free) called "scope added." Every task that wasn't in the original plan gets tagged. Every week I look at the total hours sitting in that column. If it's growing faster than I'm closing work, that's a warning sign I can act on before it's a crisis.

What surprised me was how much just making scope additions visible changes team behavior. People don't stop having good ideas. They just start self-filtering, because now they know the producer actually looks.

## The Hidden Costs That Eat Indie Budgets

| Cost Category | Minimum | Maximum | Notes |
| --- | --- | --- | --- |
| Platform certification (per platform) | $3,000 | $5,000+ | Includes submission fees, fixes, and resubmits |
| Localization (per language, 50k words) | $5,000 | $7,500 | Translation only; does not include implementation |
| Voice acting (2-3 hours, professional SAG-AFTRA) | $15,000 | $25,000 | Modest indie title scope |
| Marketing (Steam indie launch) | $10,000 | $20,000 | Paid promotion minimum for visibility |
| Contingency buffer | 20% | - | Of total project budget |

Let me give you the things that blindsided me or people I know, because nobody talks about these in the abstract budgeting articles:

Platform certification costs more than the submission fee. Sony, Microsoft, and Nintendo all charge for cert, but they also require you to fix issues, resubmit, and potentially hire external QA to meet their technical requirements. Budget a minimum of $3,000-5,000 per platform for this process, more if your game has complex online features.

Localization compounds hard. Localizing into four languages isn't four times the cost of one; it's closer to five or six times because of integration, testing, and asset management overhead. A game with 50,000 words of text costs roughly $0.10-0.15 per word per language for translation at a reputable studio. That's $5,000-7,500 per language before you touch the implementation work.

Voice acting gets expensive fast. Even modest indie titles with 2-3 hours of voiced dialogue can run $15,000-25,000 for professional SAG-AFTRA talent. If you budgeted for "some voice acting" without pricing it out, you're in trouble.

Software licenses don't just cost money upfront. Unreal Engine's royalty structure (5% of gross revenue past a $1 million threshold, as of this year) is worth factoring into your long-term projections even if it doesn't hit your development budget. Unity's licensing situation has been volatile enough that you should read the current terms yourself rather than assuming they match what you heard in 2023.

Then there's marketing, the one teams skip most aggressively. It's not a post-launch line item. A realistic minimum for a Steam indie launch with any chance of visibility is $10,000-20,000 in paid promotion, festival submissions (Tribeca, PAX, IndieCade all have entry fees), trailer production, and press outreach. If this isn't in your development budget from day one, you will either underspend on it or gut something else to fund it.

## Track Budget Like Your Game Depends On It (Because It Does)

The teams that stay on budget aren't the ones with the most discipline at the start of a project. They're the ones who look at the numbers every single week without fail, even when the numbers are uncomfortable.

I run a weekly budget check that takes about 20 minutes. I log actual hours worked against the estimate for each line item, calculate the variance, and look at the trend. If we're 10% over on programming in week three, that's a conversation. If I let it go until week eight, it's a crisis. The difference is just the habit of looking.

For tracking, I've used everything from full project management platforms like Jira (overkill for small teams, but useful if you're already in an Atlassian stack) to a simple spreadsheet. The tool doesn't matter as much as the frequency. What I actually recommend for most indie producers is Notion combined with a Google Sheet: Notion for task tracking and team communication, Sheets for financial tracking, because the separation keeps the finance side clean and auditable.

If you're working with contractors, get weekly timesheets. Not monthly, weekly. Contractors have a natural tendency to underreport hours in real time and then reconcile at invoice time, which means by the time you know you've overrun a milestone, you're already paying for the next one.

## When You're Already Over Budget

## Sources

- [RDNE Stock project](https://www.pexels.com/@rdne)
- hours in real time and then reconcile at invoice time


Sometimes you follow all the rules and you're still running over. The studio that was supposed to deliver your audio middleware goes dark. A key contractor has a medical emergency. The engine update you needed for platform compliance introduced a bug that took three weeks to solve. This happens.

The worst thing you can do is quietly hope the project absorbs it. It won't. The second worst thing is making a bunch of small cuts that don't actually save much money but do damage team morale and product quality.

What actually works: stop, spend two days doing an honest reforecast, and present yourself with three real options. Option one is find more money. Option two is cut scope in a way that still produces a shippable, marketable game. Option three is the hardest one: accept that this project needs to pause, restructure, or be abandoned. I've had to choose option three. It's brutal. It's also sometimes the right call, and making it early is less damaging than making it six months later with nothing left.

The books that genuinely helped me think through these decisions were "The Game Production Handbook" by Heather Maxwell Chandler (dense but comprehensive on cost management) and "Blood, Sweat, and Pixels" by Jason Schreier (not a how-to, but an honest accounting of how budget decisions play out in real projects). If you want more formal training, the Game Production certificate at CGMA runs periodically and covers budget and scheduling in practical terms, not the theoretical stuff most courses default to.

*Photo: [RDNE Stock project](https://www.pexels.com/@rdne) via Pexels*