---
title: "Capacity Planning For Game Development Teams"
date: 2026-05-28T22:07:45.713676+00:00
draft: false
description: "Plan game dev team capacity effectively with proven strategies. Learn to balance workloads, allocate resources, and hit deadlines without burning out your team."
image: "https://images.pexels.com/photos/29901199/pexels-photo-29901199.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
categories: ["pm frameworks"]
tags: ["capacity", "planning", "game", "development", "teams"]
author: "Ryan Cole"
author_bio: "Ryan Cole covers game production and milestone planning at GameDevProducer."
slug: "capacity-planning-for-game-development-teams"
affiliate_disclosure: true
faqs:
 - q: "How do I convince stakeholders that a 70% capacity model isn't sandbagging?"
   a: "Show them the data from previous sprints. If your team consistently planned at 100% and delivered 65%, the argument makes itself. If you don't have that data yet, start collecting it now. Three sprints of evidence is more persuasive than any theoretical argument."
 - q: "Should I use hours or story points for capacity planning?"
   a: "The research here is genuinely mixed. Story points reduce the illusion of false precision and work well for teams with stable velocity. Hours work better when team composition changes frequently or when you need to communicate timelines to non-developers. I've seen both work. Pick one and be consistent for at least six sprints before deciding it isn't working."
 - q: "How do I handle capacity planning for a team with a lot of contractors?"
   a: "Contractors often have split attention across multiple clients. Treat their stated weekly availability at 50 to 60% of what they quote unless you have direct evidence otherwise. Also factor in ramp-up time for any new contractor: the first two weeks are rarely full-productivity weeks."
 - q: "What's the biggest capacity planning mistake new producers make?"
   a: "Counting people, not work. New producers often start by listing who's on the team. The better starting point is listing the work that needs to happen, estimating it honestly, and then figuring out whether the team can do it. That order change forces a confrontation with reality earlier."
 - q: "How often should I revisit capacity models during a long production cycle?"
   a: "At minimum, every milestone. In practice, I'd recommend a light recalibration every four to six sprints, especially if team composition has changed, scope has shifted, or your velocity data is drifting significantly from your estimates. Capacity models are not set-and-forget."
author_slug: "ryan-cole"
author_title: "Senior Contributing Writer"
lastmod: 2026-07-07
---
You planned for 8 weeks of feature work. Your team delivered 4 weeks worth. The [post-mortem reveals](/how-to-run-a-game-development-retrospective/) no single catastrophic failure, just a slow bleed: a programmer pulled into an unplanned engine upgrade, an artist out sick for two weeks, three "quick" feedback rounds that each took a week, and a lead who spent 40% of her time in meetings instead of making things. Sound familiar? This is capacity planning failure, and it's the most common reason game projects ship late or die in development.

## Why Game Studios Get Capacity Planning Wrong

Most studios treat capacity planning like a math problem. They count seats, assume eight hours of productive work per person per day, and call it done. What they're actually calculating is *availability*, not *capacity*.

Real capacity is what your team can actually deliver, after accounting for meetings, context switching, bug triage, integration work, sick days, and the cognitive load of creative problem-solving. Research on knowledge worker productivity suggests that three to five hours of deep focused work per day is closer to the realistic ceiling for most people. For game developers doing complex, iterative creative-technical work, I'd argue it's even lower some weeks.

What surprised me when I dug into this was how poorly most studios track the gap between planned and actual capacity. They know they missed dates. They don't always know *why* at a granular level. And without that data, every sprint plan is basically informed guessing.

## The Capacity Planning Model That Actually Works

Here's the approach I've seen hold up across indie and mid-size teams.

**Step 1: Establish your baseline velocity first.** Don't plan capacity for a new sprint until you have at least three sprints of actual throughput data. Use whatever unit fits your workflow: story points, task count, hours completed. The unit matters less than consistency.

**Step 2: Apply a capacity multiplier.** Take your team's total available hours and multiply by 0.6 to 0.7. This accounts for overhead you can't eliminate: standups, reviews, one-on-ones, ad hoc Slack questions. If you're in crunch or pushing toward a critical milestone, resist the temptation to use 0.8 or 0.9. You'll just be lying to yourself and your stakeholders.

**Step 3: Reserve a buffer for unplanned work.** On any given sprint, 15 to 20% of your team's actual output will get consumed by things that weren't on the board two weeks ago. Plan for this explicitly. An empty buffer at the end of a sprint is a success, not waste.

**Step 4: Track individual availability, not just team averages.** One senior engineer going to GDC for a week can collapse an entire sprint if that person is the only one who owns a critical system.

**Step 5: Run a weekly capacity check-in.** Not a status meeting. Five minutes where anyone flags known disruptions to their week before they become surprises.

## Discipline-Specific Capacity Is Different

A common planning mistake is treating all team members as interchangeable capacity units. A character artist and a technical artist aren't the same resource. A gameplay programmer and a graphics programmer aren't the same resource. When you plan at the discipline level, scheduling conflicts and bottlenecks become visible before they become emergencies.

Build a simple capacity map broken down by discipline. Spreadsheet, Notion table, or a dedicated tool like **Jira** with proper team configurations or **Hacknplan** (built specifically for game dev workflows) all work. The point is seeing, at a glance, where your art pipeline is under-resourced relative to what's scheduled in the next milestone.

## Comparing Capacity Planning Tools for Game Teams

| Tool | Best For | Capacity Planning Features | Game Dev Fit |
|---|---|---|---|
| **Hacknplan** | Small to mid-size game teams | Built-in task estimation, milestone tracking | Excellent |
| **Jira + Advanced Roadmaps** | Larger studios with complex backlogs | Capacity by sprint, team availability | Good with setup overhead |
| **Notion + custom templates** | Indie teams who want flexibility | Manual, lightweight | Good for simple structures |
| **Shotgrid (Autodesk)** | Asset-heavy production pipelines | Resource scheduling, bid tracking | Strong for art-heavy teams |
| **Trello** | Very small teams | None natively | Limited for real capacity work |

| Tool | Best For | Capacity Planning Features | Game Dev Fit |
|---|---|---|---|
| **Hacknplan** | Small to mid-size game teams | Built-in task estimation, milestone tracking | Excellent |
| **Jira + Advanced Roadmaps** | Larger studios with complex backlogs | Capacity by sprint, team availability | Good with setup overhead |
| **Notion + custom templates** | Indie teams who want flexibility | Manual, lightweight | Good for simple structures |
| **Shotgrid (Autodesk)** | Asset-heavy production pipelines | Resource scheduling, bid tracking | Strong for art-heavy teams |
| **Trello** | Very small teams | None natively | Limited for real capacity work |

**"The Game Production Handbook" by Heather Maxwell Chandler** remains one of the most practical references on resource planning in actual game production. Coursera and LinkedIn Learning both offer project management courses that cover capacity fundamentals, though you'll need to adapt frameworks from general software to game dev realities.

## The Invisible Capacity Drain: Lead Time

## Sources

- on knowledge worker productivity suggests that three to five hours of deep focus


One thing that rarely shows up in capacity models is lead time for decisions. If an art director needs to approve an asset before a junior artist can proceed, and that approval takes two days, you've lost two days of capacity that never gets counted anywhere. Multiply this across a team over six months of production.

[Map your decision dependencies](/dependency-mapping-in-game-development-schedules/) the same way you map task dependencies. Know who the bottlenecks are before the sprint starts, not after.

---

Capacity planning isn't glamorous work. It doesn't show up in game design post-mortems or GDC talks about creative vision. But I've watched more projects fail from poor resource planning than from bad design decisions. Get this right and everything else gets more predictable: your sprints, your milestones, your team's morale. And in game development, predictability is a competitive advantage most studios are leaving on the table.