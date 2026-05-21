---
title: "Why Scrum Breaks In Game Pre-Production"
date: 2026-05-21T17:17:58.978205+00:00
draft: false
description: "Discover why Scrum often fails during game pre-production and what agile pitfalls teams face when exploring ideas, building prototypes, and defining creative di"
image: "https://images.pexels.com/photos/5380660/pexels-photo-5380660.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
categories: ["pm frameworks"]
tags: ["scrum", "breaks", "game", "pre-production"]
author: "Jordan Reyes"
author_bio: "Scrum master turned producer. Translates agile methodology into game dev reality -- what works, what breaks."
slug: "why-scrum-breaks-in-game-pre-production"
affiliate_disclosure: true
---

You've just kicked off pre-production. The team is excited, the concept doc is fresh, and someone suggests running Scrum because "that's how we do it." Two weeks later, your sprint review feels like a bad stand-up comedy set. Half the tasks are "in progress," the other half were quietly abandoned when the designer realized the core loop didn't actually work, and nobody can honestly say what "done" means for a paper prototype of a mechanic you might cut next month. Sound familiar? Scrum isn't broken as a framework. It's just being applied at the wrong moment, in the wrong context, for the wrong reasons.

## Pre-Production Is a Research Phase, Not a Delivery Phase

The most important thing to understand about pre-production is what it actually is: a structured search for answers. You're not building a game yet. You're trying to prove a game is worth building. Those are completely different jobs, and they require completely different management approaches.

Scrum was designed for teams that know what they're making. The framework assumes a backlog of reasonably well-understood work items, a definition of done that can be verified, and a product incrementally assembled toward a known goal. Pre-production has almost none of that. You're asking questions like: Does this movement system feel good? Is this world interesting enough to spend 30 hours in? Can our team actually pull off this art style at scale?

These aren't sprint tasks. They're hypotheses.

When you force pre-production work into a sprint structure, you create a theatre of productivity. People fill the board with tasks to look busy. "Research competitor games" sits in a column next to "Design enemy AI" as if they carry equal weight and definition. The burndown chart tells you nothing useful because the work itself isn't decomposable in any honest way until you've answered the fundamental creative questions first.

I've seen teams spend six weeks doing "Scrum" in pre-production and emerge with a completed sprint board and zero validated answers about whether their game concept holds up. That's a production disaster waiting to happen.

## The Velocity Illusion

Scrum depends on velocity as its core feedback mechanism. Track your points over several sprints, get a stable average, use it to forecast. It's genuinely useful when the work is consistent enough for the numbers to mean something.

Pre-production work isn't consistent. A designer might spend three days prototyping a mechanic and scrap it entirely. Was that 13 points of story-point estimation? Zero? The entire sprint's worth? The answer doesn't matter because velocity in pre-production isn't a signal, it's noise.

Worse, velocity tracking creates perverse incentives. Teams learn to point up tasks to "look productive." Soft research work gets padded. Experimental spikes that should be cheap and fast become bloated to hit the sprint commitment. The team starts optimizing for a number instead of for learning, which is the exact opposite of what pre-production demands.

I've watched a lead programmer estimate a "proof of concept for procedural generation" at 8 points and spend 9 days on it because the sprint demanded 40 points of delivery. He should have spent 3 days, shipped a messy but informative prototype, and moved on to test the next risky assumption. The sprint structure punished the fast, dirty learning loop that pre-production actually needs.

## Scrum's Ceremonies Don't Fit the Pre-Production Cadence

Let's talk about the ceremonies specifically, because this is where teams feel the pain most acutely.

**Daily standups** work when there's a shared, concrete goal everyone is marching toward. In pre-production, individual contributors are often exploring parallel directions simultaneously. A daily standup becomes a research report: "I'm still reading postmortems about open-world navigation design." There's nothing wrong with that work. But framing it as a standup blocker conversation creates awkwardness and pressure to manufacture urgency.

**Sprint planning** requires a backlog of defined tasks. In pre-production, you often can't define next week's tasks until you've seen the results of this week's experiments. Forcing sprint planning without that input means you're either planning fiction or replanning mid-sprint constantly, which destroys the rhythm Scrum relies on.

**Sprint reviews** presuppose a shippable increment. What's the pre-production increment? A mood board? A vertical slice of a mechanic that might get cut? Teams end up demo-ing things that technically "work" but don't answer the production-risk questions that matter. Stakeholders leave the review thinking progress is being made when the real question, "should we greenlight this game?", remains completely unanswered.

**Retrospectives** can actually be useful in pre-production, but they're often the first ceremony to get dropped when teams feel the rest of the Scrum process isn't clicking.

## What Actually Works in Pre-Production

If Scrum isn't the answer, what is? The honest answer is that pre-production needs a framework built around validated learning, not delivery cadence. A few approaches work well.

**Milestone-based research sprints** are shorter, focused bursts of 1-2 weeks aimed at answering a single production risk question. Not "work on the combat system" but "answer: can we make melee combat feel as responsive as God of War on our target hardware?" The milestone is a go/no-go decision, not a feature.

**A risk register as your backlog** is one of the most practical shifts you can make. List every assumption your game depends on and treat high-risk assumptions as the top-priority "stories." Prototype against risk, not against features. When the biggest unknowns are resolved, you've earned the right to start production.

**Kanban with WIP limits** often fits pre-production much better than Scrum. You get flow visibility without the artificial sprint commitments. Work moves when it's done, not when a two-week clock runs out. Priorities can shift mid-stream when a prototype reveals something important without triggering a sprint replanning crisis.

Here's a simple comparison of how these approaches stack up for pre-production specifically:

| Concern | Scrum | Kanban | Milestone-Based Research |
|---|---|---|---|
| Handles undefined work well | No | Partially | Yes |
| Supports hypothesis testing | No | Partially | Yes |
| Gives velocity/forecast data | Yes (misleading) | No | No (intentionally) |
| Flexible to pivot mid-cycle | No | Yes | Yes |
| Good for stakeholder reporting | Yes | Partially | Yes |
| Appropriate when | Production | Ongoing support | Pre-production |

The tools that help you run this kind of process well are worth investing in. Notion works well for maintaining a living research log and risk register. Miro is excellent for mapping assumptions visually. For teams wanting structured project tracking, Jira can work if you're disciplined about not forcing story points onto research tasks. Confluence is underrated for pre-production documentation because the decisions you make in this phase need to be defensible later.

For producers who want to go deeper on this, Jason Schreier's "Blood, Sweat, and Pixels" gives you a ground-level view of how pre-production chaos actually plays out at real studios. Keith Stuart's work aside, the most useful production-specific resource I keep returning to is the Game Producers Handbook by Mike Bode and Marjolein Lahr. For online learning, the Game Production curriculum at Coursera through Michigan State is solid for foundational framing, and Riot's internal talks posted publicly on YouTube are genuinely useful for how large studios think about early-phase risk management.

## How to Transition Out of Pre-Production Scrum Without Blowing Up Team Trust

If you're already running Scrum in pre-production and it's not working, you can't just walk in Monday morning and announce you're scrapping it. That breeds confusion and erodes confidence in leadership. Here's a step-by-step approach to making the shift cleanly.

**Step 1: Name the problem honestly.** Hold a retrospective specifically about your process, not just your sprint. Ask the team directly: "Are our sprint goals giving us clear answers about whether this game is ready to build?" You'll get honesty if you create the space for it.

**Step 2: Build your risk register.** Before changing anything structural, spend a day with leads mapping out every major assumption the project depends on. Technical, creative, market, and team-capability assumptions all count. Prioritize them by impact and unknownness.

**Step 3: Reframe your sprint goals.** You don't have to abandon Scrum entirely overnight. Start by replacing feature-based sprint goals with question-based ones. Instead of "implement basic crafting UI," the sprint goal becomes "determine whether crafting adds meaningful decision-making to the core loop." Same time box, completely different orientation.

**Step 4: Drop story points, keep the board.** Story points in pre-production create more noise than signal. Move to a simple three-size estimate (small/medium/large) or drop estimation entirely and just use WIP limits. Keep the visual board because it helps the team see where work is accumulating.

**Step 5: Define your greenlight criteria now.** Work backward from what leadership needs to approve full production. List those criteria explicitly, then make sure every research activity maps to at least one greenlight question. If a task doesn't answer a greenlight question, it probably doesn't belong in pre-production at all.

**Step 6: Set a fixed pre-production end date.** Pre-production without a hard deadline tends to expand indefinitely. Even if that date is three months away, having it creates urgency and helps you triage which risks absolutely must be resolved before production starts.

---

## Frequently Asked Questions

### Isn't some Scrum better than no process at all during pre-production?

Process for its own sake can actually make things worse. A bad process creates false confidence, produces misleading metrics, and can mask the real state of your project from stakeholders who are making resource decisions based on your sprint reviews. If Scrum isn't giving you honest answers about your game's viability, running it is actively harmful, not just neutral. A simple Kanban board and a weekly risk review beats a full Scrum implementation that isn't generating real learning.

### Our studio mandates Scrum across all teams. What do I do?

Work within the structure but redefine what "done" means for your context. If you're required to run sprints, make your sprint goals explicitly research-based. Talk to your production lead or studio head about how you're measuring pre-production progress differently. Most mandates are about visibility and reporting consistency, not about forcing sprint-delivery thinking onto exploration work. You can usually get flexibility on the inside of the framework even when the outside structure is non-negotiable.

### How do I know when pre-production is actually finished and Scrum becomes appropriate?

The clearest signal is that your backlog becomes decomposable. When you can write a user story for a feature, estimate it with reasonable confidence, and know what "done" looks like without major caveats, you're ready for production. Practically, this usually means your vertical slice is complete, your core loop is validated, your tech risks are resolved, and your art pipeline is proven. When you hit that state, Scrum or a structured sprint model becomes genuinely useful because the work has enough definition to benefit from it.

### What should a pre-production sprint review actually look like?

Instead of a demo of features, run a research review. Each team presents: what question they were answering, what they found, and what the next decision is based on that finding. Stakeholders should leave a pre-production review with clearer answers about project risk, not with a demo of work-in-progress systems that might get cut. Think of it as a science fair, not a product demo.

### We shipped with Scrum in pre-production and it worked fine. Are you wrong?

You might have gotten away with it because your pre-production was short, your concept was well-defined coming in, or your team was experienced enough to do real validation work inside a sprint structure without the framework getting in the way. None of that means Scrum was the reason it worked. In my experience, teams that "succeed" with Scrum in pre-production usually succeeded because of talented people and a strong creative vision, not because sprints helped them discover that vision faster.

---

Pre-production is where games live or die, and most studios treat it like a planning problem when it's actually a learning problem. The teams that do it well treat every week as an investment in reducing the risk of the next two years. When you understand that, the question isn't "how do we run Scrum correctly in pre-production?" but "what process helps us learn the fastest?" Get that right, and production, with or without Scrum, becomes a lot less terrifying.

*Photo: [Tima Miroshnichenko](https://www.pexels.com/@tima-miroshnichenko) via Pexels*