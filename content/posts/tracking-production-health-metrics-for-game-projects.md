---
title: "Production Health Metrics for Game Development Teams"
date: 2026-11-23T20:21:45.587697+00:00
draft: false
description: "Essential metrics and KPIs to monitor game project health, track team performance, and identify production issues before they escalate."
image: "/img/heroes/38888656.jpg"
categories: ["pm frameworks"]
tags: ["tracking", "production", "health", "metrics", "game"]
author: "Stephen Brenish"
author_slug: "stephen-brenish"
author_title: "Lead Game Producer"
author_bio: "Stephen Brenish is a Lead Game Producer at Epic Games (Fortnite, Unreal Engine) and the founder of GameDevProducer. Across 14+ years in game production he has shipped and operated live titles at scale, previously as a Senior Program Manager at Blizzard Entertainment. Certified ScrumMaster."
slug: "tracking-production-health-metrics-for-game-projects"
affiliate_disclosure: true
faqs:
  - q: "How many health metrics should a production team actually track?"
    a: "Six to eight is a practical ceiling for most teams. More than that and nobody reads the dashboard carefully. Pick one or two metrics per dimension (scope, velocity, quality, team load) and instrument those well before adding more."
  - q: "What's the difference between a KPI and a production health metric?"
    a: "KPIs (key performance indicators) are typically tied to business outcomes: sales, DAU, retention. Production health metrics are internal signals about process and team condition. They're related but distinct. A studio can hit its sales KPIs with a game that nearly destroyed the team, and a production health system exists to prevent that specific outcome."
  - q: "Should health metrics be shared with the whole team or just leads?"
    a: "Leads and producers should see the full picture. With the broader team, share simplified, contextualized summaries rather than raw dashboards. A developer seeing an uncontextualized red metric without explanation creates anxiety and speculation. Bring context with the data."
  - q: "How do you track health metrics on a very small team (5 people or fewer)?"
    a: "Formal dashboards are overkill. A weekly 15-minute sync where the producer explicitly asks about scope changes, blockers, and work hours accomplishes most of what a dashboard does for a small team. You can use a simple spreadsheet to log the answers over time and spot trends."
  - q: "When should a producer escalate a health metric to studio leadership?"
    a: "If a metric has been outside the acceptable band for two or more consecutive weeks and the team-level intervention hasn't moved it, escalate. Leadership needs to know early enough to actually make resourcing or scope decisions, not early enough to panic but late enough that the decision is already made for them."
---

Most production teams track the wrong things. They count tasks closed, velocity points burned, and milestone dates hit, then wonder why the project still shipped broken, late, or both. Those numbers tell you what happened. They don't tell you whether the project is healthy.

Production health metrics are a different category. They're leading indicators, not lagging ones. A closed ticket count tells you what the team finished; [scope creep](/posts/scope-creep-prevention-in-game-development/) rate tells you whether the team will ever finish. That distinction matters more than any sprint report.

The goal here is to give you a working system, not a theoretical one. What to measure, how often, and what to do when a number goes wrong.


<div class="kt" style="margin:26px 0;padding:18px 22px;border:1px solid var(--border,#e7e5e4);border-left:4px solid var(--accent,#4338ca);border-radius:12px;background:var(--surface2,#f8fafc)"><div style="font-size:.72rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--accent,#4338ca);margin-bottom:8px">Key takeaways</div><ul style="margin:0;padding-left:1.15em"><li style="margin:5px 0">Track 6-8 health metrics per project, not 20+; too many signals become noise.</li><li style="margin:5px 0">Scope creep above 10% per milestone is a production emergency, not a planning footnote.</li><li style="margin:5px 0">Bug arrival rate matters more than bug count; a rising rate signals systemic breakdown.</li><li style="margin:5px 0">Velocity should be stable or gently declining in Alpha; a sudden drop is a team health warning.</li><li style="margin:5px 0">Review health metrics weekly at the producer level, monthly with leads and stakeholders.</li></ul></div>


## What "Health" Actually Means in Production

A project can be on schedule and still be dying. Features shipping late inside a sprint don't always blow the milestone, so they get waved through. Tech debt accumulates quietly. The team starts cutting corners and nobody flags it because the burndown chart looks fine.

Health metrics are designed to catch that slow bleed. They're not about output. They're about the conditions that determine whether output will continue.

There are roughly four dimensions worth monitoring: scope integrity, velocity stability, quality signal, and team load. Measure one thing in each dimension and you've got a minimal viable dashboard. Measure two or three and you can actually make decisions before you're in crisis.

## The Metrics That Matter

**Scope creep rate.** Calculate this per milestone: (features added since milestone start) divided by (features scoped at milestone start), expressed as a percentage. Anything above 10% is a conversation. Above 20% means your milestone scope was fiction and you need to cut, defer, or reset the milestone date before you're two weeks from the deadline.

**Bug arrival rate vs. closure rate.** This one is the clearest quality signal in the business. Plot bugs opened per week against bugs closed per week. When arrival rate consistently exceeds closure rate, you have a systemic problem: either QA coverage expanded faster than the team can fix, the codebase is destabilizing, or both. The number of open bugs at any moment is almost useless without this trend line.

**Velocity variance.** Stable velocity isn't necessarily high velocity. What you want is predictability. A team delivering 60-70 points per sprint for eight sprints is in better shape than a team delivering 90 one sprint and 40 the next. High variance means your estimates are broken, your process is broken, or your team is burning out. Probably two of those.

**Crunch signal.** Hours worked above contract per week, tracked and reported honestly. Some studios use anonymous surveys; some use timesheets. Either way, if average weekly hours are running 20% over contracted hours for more than three consecutive weeks, you have a problem that will cost you people before the project ships.

**Feature complete percentage vs. target.** At any milestone checkpoint, what percentage of scoped features are fully done (not "in progress," not "in review," done)? This should be in the 85-95% band at milestone. Below 85% means you've been carrying forward debt and the milestone was soft. It also predicts whether your Alpha or Beta will be credible.

Here's how these metrics break down by project phase and what thresholds warrant action:

| Metric | Pre-Alpha Target | Alpha Target | Beta Target | Action Threshold |
|---|---|---|---|---|
| Scope creep rate (per milestone) | <15% | <10% | <5% | Any single milestone above these figures |
| Bug arrival vs. closure ratio | Arrival ok > closure | Arrival = closure | Closure > arrival | Arrival > closure for 2+ consecutive weeks in Beta |
| Velocity variance (sprint-to-sprint) | ±25% acceptable | ±15% | ±10% | Variance outside band for 3+ sprints |
| Feature complete at milestone | >75% | >85% | >95% | Below threshold triggers milestone re-scope meeting |
| Avg. overtime (hrs/week over contract) | <5 hrs | <8 hrs | <10 hrs | >10 hrs sustained for 3+ weeks |

The Beta overtime threshold looks high, and it is. Final polish and cert prep genuinely compress schedules. But sustained crunch above that level in Alpha is a warning sign that something structural is wrong in your planning.

## Building the Dashboard

Pick a single source of truth. That might be Jira, Shortcut (formerly Clubhouse), Hansoft, or even a well-maintained Google Sheet if the team is small enough. The tool matters less than the discipline of updating it and reviewing it on a fixed cadence.

For most teams, the right cadence is: producer reviews the full dashboard weekly, leads see a summary in the weekly production meeting, and stakeholders get a simplified version monthly. Don't send stakeholders the raw bug arrival rate chart unless they've asked for it and you're prepared to explain what they're looking at.

**Example:** A team of 25 people is in Alpha with 10 weeks to Beta. Their milestone scope is 120 features. At week 6, feature complete percentage is at 68%, scope creep rate is running at 18% (they added 22 features since milestone start), and bug arrival rate has exceeded closure rate for three consecutive weeks. Each of those numbers individually might be explainable. All three together signal that the Beta date is at risk and that the milestone scope needs surgery immediately, not at week 9. The producer's job is to surface that combination to leads and stakeholders before it becomes a death march.

If you haven't already built out your milestone structure, the [Schedule & Milestone Planner](/game-development-schedule-planner/) can turn a launch date into concrete phase checkpoints with built-in buffer, which makes it much easier to instrument the kind of per-milestone health tracking described here.

## What to Do When Numbers Go Red

The worst thing you can do with a bad metric is note it, add it to the weekly update, and move on. A red health metric is a question: *why is this number outside the acceptable band?* The answer determines the intervention.

Scope creep is almost always a people or process problem, not a creativity problem. Either the team doesn't have a clear gating process for adding scope, or someone with authority is overriding the process, or the original scope was under-specified and the team is discovering requirements late. Each of those has a different fix.

Rising bug arrival rate in Alpha usually means QA coverage grew faster than the team planned for. Sometimes that's a resource issue. More often it means the team shipped features too fast without sufficient internal testing before QA got them.

Velocity crashes (sudden, not gradual) are almost always a team health signal. Something external disrupted focus, someone key left or is about to leave, or there's a technical blocker that the team is working around instead of escalating. Ask the team directly. Don't wait for the next retrospective.

## Sources

- [Project Management Institute (PMI)](https://www.pmi.org): Standards and guidance for project health tracking, including earned value management concepts adaptable to game production.
- [International Game Developers Association (IGDA)](https://igda.org): Developer satisfaction surveys and working conditions reports, relevant to crunch and team health tracking.
- [Atlassian Jira Documentation](https://support.atlassian.com/jira-software-cloud/): Official documentation for configuring velocity charts, burndown reports, and custom dashboards.
- [Kotaku's "Crunch" reporting series](https://kotaku.com): Long-form industry reporting on how crunch and production dysfunction manifest in real projects.
- [Mike Cohn, *Agile Estimating and Planning* (Mountain Goat Software)](https://www.mountaingoatsoftware.com/books/agile-estimating-and-planning): Foundational reference on velocity measurement and sprint health in agile environments.

---


*Photo: [Jakub Zerdzicki](https://www.pexels.com/@jakubzerdzicki) via Pexels*