---
title: "Why Scrum Breaks In Game Pre-Production"
date: 2026-05-29T15:17:14.397761+00:00
draft: false
description: "Discover why Scrum often fails during game pre-production and learn which agile approaches better support the creative, exploratory nature of early game develop"
image: "https://images.pexels.com/photos/6291261/pexels-photo-6291261.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
categories: ["pm frameworks"]
tags: ["scrum", "breaks", "game", "pre-production"]
author: "Jordan Reyes"
author_bio: "Scrum master turned producer. Translates agile methodology into game dev reality -- what works, what breaks."
slug: "why-scrum-breaks-in-game-pre-production"
affiliate_disclosure: true
faqs:
  - q: "Is Scrum ever appropriate for game pre-production?"
    a: "Yes, in specific situations. If your pre-production is primarily technical, with a known feature set and defined engine requirements, Scrum can work reasonably well. It also works if your team has strong Scrum discipline and experience adapting the framework creatively. The failure mode I'm describing is most acute when Scrum is applied rigidly to highly exploratory work by teams who treat the framework as a rule set rather than a set of tools."
  - q: "What about Scrumban or hybrid approaches?"
    a: "Scrumban, which combines Scrum's cadence with Kanban's flow-based task management, is often a solid middle ground for pre-production. You keep regular retrospectives and review meetings from Scrum, but you let work items flow based on priority rather than forcing them into sprint-sized buckets. Many game studios use something like this in practice even when they don't have a name for it. Tools like Jira support both modes without major reconfiguration."
  - q: "How do you explain a non-Scrum pre-production process to stakeholders who expect Scrum?"
    a: "Frame it in terms of outcomes, not process names. 'We're using a question-driven planning approach that gives us clearer visibility into creative and technical risk' lands better than 'we're not doing Scrum anymore.' Show stakeholders a clean list of open questions, their current status, and your exit criteria. That transparency usually satisfies the people who pushed for Scrum in the first place, because what they actually wanted was predictability and visibility."
  - q: "How long should pre-production last for a mid-size game?"
    a: "For an AA game with a team of 30-60 people, pre-production typically runs 6 to 18 months. A vertical slice is usually the production-ready milestone. The dangerous failure mode is pre-production that never officially ends, which happens when teams don't define their exit criteria upfront. If you don't know what questions must be answered before production starts, pre-production will expand to fill whatever time it's given."
  - q: "Can you recommend any tools specifically for pre-production planning?"
    a: "Hacknplan is built for game development and handles milestone-based, non-ticket work better than generic tools. Notion is excellent for decision logs and research documentation. Miro or FigJam work well for visual planning sessions where the team maps dependencies between open questions. For broader production management later in the project, Shotgrid (formerly Ftrack) is the industry standard for larger teams tracking asset pipelines. For learning the underlying skills, the Game Design and Production specialization on Coursera covers phase-specific production planning in detail."
---

Your team just wrapped a killer prototype. The creative director is buzzing, stakeholders are nodding, and someone tapes a sprint board to the wall. Two weeks later, half the tickets are in "In Progress," nobody can agree on what "done" means for a concept exploration task, and the lead designer hasn't touched the board in a week because she's busy writing a 30-page GDD that will probably change three more times before alpha. Sound familiar? That's not a discipline problem. That's Scrum colliding with a phase it was never built for.

## What Pre-Production Actually Is (and Why It's Different)

Pre-production is a discovery process. You're trying to answer questions you don't fully know how to ask yet. What's the core loop? Does it feel fun? What's the production risk? Can we actually build this with the team and budget we have? The deliverables are fuzzy by design, because the whole point is to reduce uncertainty, not ship increments of a known product.

Scrum, on the other hand, was designed for teams that already know what they're building. The framework assumes a stable product backlog, a clear definition of "done," and incremental delivery of working software. It works beautifully when a feature team is implementing a login system, adding weapon skins, or fixing a regression in a lighting system. The shape of the work is clear. The output is verifiable.

Pre-production breaks those assumptions completely. You might spend three days building a prototype that gets thrown away on purpose. A designer might need two weeks of open-ended play research before she can write a single user story. A technical director might need to spike on three different engine approaches before the team can scope anything at all. None of that maps cleanly to a two-week sprint with defined acceptance criteria.

## The Specific Ways Scrum Fails the Phase

Let me be specific about the failure modes, because "Scrum doesn't fit" is easy to say and hard to act on.

**Sprint velocity becomes meaningless.** In production, velocity is a useful forecasting tool. You track story points over time, smooth out the curve, and get a reasonable estimate of throughput. In pre-production, the work is so heterogeneous that point estimates are almost pure fiction. How many story points is "figure out whether we want a stamina bar"? You could assign three points and close the ticket in a day, or you could assign three points and still be debating it six weeks later. The metric teaches the team nothing.

**Definition of Done creates false confidence.** When you force a DoD onto exploratory work, one of two things happens. Either you write acceptance criteria so vague they're useless ("prototype feels fun"), or you write criteria that are technically completable but don't actually answer the creative question. I've watched teams ship "functional" prototypes that cleared every sprint criterion and still couldn't tell leadership whether the concept was worth pursuing. The checklist got checked. The real question stayed unanswered.

**Two-week cadence fights against creative iteration.** Some pre-production work runs on a shorter feedback loop. A game feel prototype might need daily or even hourly feedback from the creative director. Some work runs much longer. Writing a tech design document for a procedural generation system might take four weeks of research plus writing. Forcing both into the same two-week box either rushes the slow work or bores people waiting to review the fast work.

**The backlog becomes a graveyard.** Pre-production backlogs have a specific disease: they fill up with tickets that represent open questions rather than tasks, and open questions don't get "done," they get answered or abandoned. When the product owner dutifully grooms that backlog, they're often just reshuffling uncertainty. Teams start to feel like the process is busywork, which is death to morale during a phase where you absolutely need creative energy.

## A Better Mental Model: Pre-Production as Structured Inquiry

Think of pre-production not as a mini-production sprint sequence, but as a series of time-boxed experiments with explicit exit criteria. The question you're answering isn't "did we complete this sprint?" It's "did we reduce uncertainty enough to make the next decision?"

This reframe changes everything about how you structure the work. Instead of a backlog of tasks, you maintain a list of open questions ranked by risk and dependency. Instead of sprint goals, you set experiment goals: "By the end of week two, we will know whether physics-based traversal is technically feasible on our target platform." That's a pass/fail question. The team knows what they're running at.

This is closer to how the best pre-production teams I've seen actually operate, even when they're officially "doing Scrum." They're running Scrum on the outside and something closer to hypothesis-driven development on the inside. It's worth formalizing that instead of pretending the sprint board captures the real work.

## What to Use Instead (or Alongside)

You don't have to throw out every Agile tool. You just have to be selective.

| Scrum Element | Pre-Production Alternative |
|---|---|
| Sprint backlog of tasks | Risk register of open questions, ranked by impact |
| Two-week sprints | Variable-length exploration cycles (1, 2, or 4 weeks) tied to specific decisions |
| Velocity tracking | Decision throughput: how many key questions answered per month |
| Sprint review demo | Playable prototype review with explicit "what did we learn" debrief |
| Definition of Done | Explicit "question answered" criteria written before the experiment starts |
| Daily standup | Shorter, question-focused check-ins: what's blocking a decision? |

**Kanban** is often a better fit than Scrum for at least part of pre-production. It handles variable cycle times naturally and doesn't punish you for work that spills past a two-week boundary. Tools like Jira, Hacknplan, or even a physical board with swimlanes organized by risk category can work here. Hacknplan in particular was built for game development workflows and handles milestone-based planning better than a pure ticket queue.

**Weekly milestones** work better than sprints during this phase. Define what question you'll answer or what prototype you'll have by end of week, keep the team pointed at that, and run a lightweight retrospective focused on "did we answer the question and what did we learn?" not "did we hit our velocity target?"

For producers who want to go deeper on this, *The Art of Game Design* by Jesse Schell has a solid lens on iterative design thinking that maps well onto pre-production planning, even though it's not explicitly a production methodology book. *Blood, Sweat, and Pixels* by Jason Schreier is great for understanding how real pre-production actually went on shipped games, warts and all. For online learning, the Game Production curriculum on Coursera from Michigan State University covers phase-specific management in a way that most generic Agile courses skip entirely.

## How to Transition Your Team Without Blowing Up Trust

If you're a producer trying to change the process mid-pre-production, be careful. Teams that have been told "we do Scrum" and then suddenly get told "never mind, we're doing something else" will often hear "our process is a mess and leadership doesn't know what they're doing." You need to frame the change accurately.

Here's a step-by-step approach that works:

1. **Name the problem in a retrospective.** Don't show up with a new framework already decided. Ask the team: "What's not working about our current process?" Let them say the things they've been noticing. Usually they've noticed everything.

2. **Introduce the experiment framing.** Explain that pre-production is fundamentally about answering questions, not shipping increments. Write out your top ten open questions as a team. Rank them by risk and dependency. This exercise alone often clarifies the real work more than a full sprint backlog.

3. **Keep the cadence but change the goal.** Don't change your meeting rhythm yet. Keep standups, keep a weekly sync. But replace sprint goals with question goals. "This week we answer: can our AI systems support 40 NPCs at target framerate?" That's it. Keep everything else familiar.

4. **Introduce variable cycle lengths slowly.** After a few weeks, if the team agrees, try a four-week deep-dive on the biggest technical risk. Compare how that felt versus cramming it into two-week chunks. Let the team's experience drive the decision.

5. **Use a productivity tool to track decisions, not tasks.** Notion, Confluence, or even a well-structured Google Doc works for a decision log. Every answered question goes in: what was the question, what did we find, what do we do next. This becomes your pre-production artifact and your institutional memory.

6. **Define your pre-production exit criteria before you start.** This is the hardest part and the most important. What questions must be answered before production can start? Lock that list before the phase begins. That list is your actual milestone, not a sprint count.

## Signs Your Pre-Production Scrum Is Actively Hurting You

If you're unsure whether this applies to your current project, look for these signals:

Your sprint board has more than 20% of tickets in "In Progress" at any given time, and they've been there for more than five days. Your team is spending significant time in backlog grooming sessions but nobody's confidence in the schedule has improved. The same creative questions keep coming up in retrospectives without resolution. Your velocity graph is erratic enough that it provides no forecasting value. And the tell that I've seen more than any other: your creative director or lead designer has quietly stopped engaging with the process because they feel like the board doesn't reflect what they're actually doing.

That last one is the most dangerous. When your most creative people decouple from the process, you don't lose their productivity immediately. You lose it gradually, and you lose the process's ability to surface creative risk, which is exactly what you need pre-production to do.

---

## FAQ

### Is Scrum ever appropriate for game pre-production?

Yes, in specific situations. If your pre-production is primarily technical, with a known feature set and defined engine requirements, Scrum can work reasonably well. It also works if your team has strong Scrum discipline and experience adapting the framework creatively. The failure mode I'm describing is most acute when Scrum is applied rigidly to highly exploratory work by teams who treat the framework as a rule set rather than a set of tools.

### What about Scrumban or hybrid approaches?

Scrumban, which combines Scrum's cadence with Kanban's flow-based task management, is often a solid middle ground for pre-production. You keep regular retrospectives and review meetings from Scrum, but you let work items flow based on priority rather than forcing them into sprint-sized buckets. Many game studios use something like this in practice even when they don't have a name for it. Tools like Jira support both modes without major reconfiguration.

### How do you explain a non-Scrum pre-production process to stakeholders who expect Scrum?

Frame it in terms of outcomes, not process names. "We're using a question-driven planning approach that gives us clearer visibility into creative and technical risk" lands better than "we're not doing Scrum anymore." Show stakeholders a clean list of open questions, their current status, and your exit criteria. That transparency usually satisfies the people who pushed for Scrum in the first place, because what they actually wanted was predictability and visibility.

### How long should pre-production last for a mid-size game?

For an AA game with a team of 30-60 people, pre-production typically runs 6 to 18 months. A vertical slice is usually the production-ready milestone. The dangerous failure mode is pre-production that never officially ends, which happens when teams don't define their exit criteria upfront. If you don't know what questions must be answered before production starts, pre-production will expand to fill whatever time it's given.

### Can you recommend any tools specifically for pre-production planning?

Hacknplan is built for game development and handles milestone-based, non-ticket work better than generic tools. Notion is excellent for decision logs and research documentation. Miro or FigJam work well for visual planning sessions where the team maps dependencies between open questions. For broader production management later in the project, Shotgrid (formerly Ftrack) is the industry standard for larger teams tracking asset pipelines. For learning the underlying skills, the Game Design and Production specialization on Coursera covers phase-specific production planning in detail.

---

Pre-production is where games live or die. Get it wrong and you spend production fixing design problems that should have been caught earlier, which is the most expensive possible time to catch them. The framework you use during this phase should be designed to maximize learning speed and creative clarity, not task completion rate. Scrum is a great tool. It's just not always the right tool for this job, and knowing the difference is one of the things that separates a good producer from a great one.

*Photo: [RDNE Stock project](https://www.pexels.com/@rdne) via Pexels*