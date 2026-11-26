---
title: "Kanban Boards: The Project System Indie Studios Actually Need"
date: 2026-06-30T11:24:23.049744+00:00
draft: false
description: "Learn how kanban boards help indie game teams stay organized, track tasks, and ship games faster with simple visual workflow management."
image: "/img/heroes/7580842.jpg"
categories: ["project management"]
tags: ["kanban", "boards", "indie", "game", "teams"]
author: "Stephen Brenish"
author_slug: "stephen-brenish"
author_title: "Lead Game Producer"
author_bio: "Stephen Brenish is a Lead Game Producer at Epic Games (Fortnite, Unreal Engine) and founder of GameDevProducer, with 14+ years shipping and running live games at scale (previously Senior Program Manager at Blizzard Entertainment). Certified ScrumMaster."
slug: "kanban-boards-for-indie-game-teams-explained"
affiliate_disclosure: true
faqs:
 - q: "How many columns should a kanban board have for a small indie team?"
   a: "Somewhere between five and seven is the sweet spot for most teams under eight people. Fewer than five and you're losing visibility into where work actually stalls; more than seven and maintenance becomes a burden that kills adoption. Start with five and add a column only when you can name a specific problem it solves."
 - q: "Should we use kanban or Scrum for indie game development?"
   a: "For teams under six people, kanban usually fits better because it doesn't require sprint commitments you'll constantly break. Scrum adds value when you have a publisher or external stakeholder who needs regular delivery cadences. If nobody external is waiting on you, the overhead of sprint planning rarely pays off at small scale."
 - q: "What's the best free kanban tool for a solo or two-person game dev team?"
   a: "Trello's free tier is genuinely sufficient for solo or two-person teams. You get unlimited cards, basic WIP limit plugins (via the Butler automation), and color labels. Notion also works if your team is already using it for documentation, though it's slightly less visual than a dedicated kanban tool."
 - q: "How do we handle recurring tasks like weekly builds or playtesting sessions on a kanban board?"
   a: "Don't put recurring operational tasks on your kanban board at all. They're not flow work; they're scheduled events. Put them in your calendar or a separate recurring checklist. Mixing them into your task flow pollutes the board and makes cycle time metrics meaningless."
 - q: "When should we actually update the board, and how do we stop it going stale?"
   a: "Daily self-updates (each person moves their own cards) combined with a 30-minute weekly team review is the pattern that sticks. If you can't get daily updates, do them at the start and end of each work session. What doesn't work: assigning one person to maintain the board for everyone else. It always drifts, and then nobody trusts it."
 - q: "What's the difference between a kanban board and a Trello board?"
   a: "Kanban is a method: visualize work, limit work in progress, and watch for bottlenecks. Trello is a tool that gives you cards and columns. A Trello board only becomes a kanban board once you add meaningful columns that match your workflow and a limit on how many cards can sit in progress at once."
 - q: "What is a WIP limit and what should it be for a small game team?"
   a: "A WIP (work-in-progress) limit is the maximum number of cards allowed in a column at one time. For the In Progress column, a reasonable starting point is about twice your team size, then adjust based on what the board shows you. If the limit exposes a review bottleneck, add a separate limit to the Needs Review column too."
lastmod: 2026-11-26
---

A kanban board helps an indie game team see what work is in progress, limit how much is started at once, and spot where tasks get stuck, without the sprints and ceremony of Scrum. Most kanban advice online was written for software developers shipping features to paying enterprise customers, though, and indie game dev doesn't look anything like that. This guide covers how to adapt the board to how games actually get made.

A common mistake is copying a setup from a Scrum-style blog post, ending up with columns called "Backlog," "In Sprint," "Review," and "Done," and wondering why it feels so wrong. Artists don't know what "In Sprint" means for a texture pass. Audio work gets marked "Done" while half-finished because there's nowhere else to put it. The result is a tidy board that says almost nothing useful about the actual state of the game.

The fix wasn't complicated, but it required understanding what kanban is actually doing, and why the standard corporate template actively fights you on a creative project.

## What Kanban Is Actually Doing (And Why It Fits Indie Dev Surprisingly Well)

Kanban originated at Toyota in the 1940s as a manufacturing flow system. The word means "signboard" in Japanese. The core idea: visualize your work, limit how much is in progress at one time, and watch for where things get stuck. That's it. There's no prescribed ceremony, no sprints, no velocity points. You're not committing to a two-week block of work; you're just pulling the next card when you have capacity.

That model fits a small game team's reality better than most people expect. Indie dev is deeply asynchronous. Your composer works weird hours. Your artist is juggling contract gigs. Your programmer might disappear for a week into a hard rendering problem. Sprint commitments get broken constantly, which kills morale. Kanban doesn't ask you to commit. It asks you to keep moving and surface blockers fast.

The case for kanban on small teams is practical rather than theoretical: less ceremony, less coordination overhead, and a board that shows where work is stuck.

## Setting Up a Board That Actually Reflects How Games Get Made

| Tool | Best For | Cost | Setup Time |
| --- | --- | --- | --- |
| Trello | Teams up to 6 people | Free tier available | Minimal |
| HacknPlan | Game dev teams (Studio tier) | Free tier and paid plans | Moderate |
| Jira | Larger indie teams with publisher support | Variable | ~1 week |

The default "To Do / Doing / Done" setup will work at first. But games have a production reality that most kanban templates ignore: assets, mechanics, and content have multiple distinct states that matter differently to different people on the team.

Here's the column structure I'd recommend to most small teams:

**Backlog / Icebox / Ready to Pull / In Progress / Needs Review / In Integration / Done**

Let me break down the non-obvious ones.

"Icebox" is separate from Backlog intentionally. Backlog items are prioritized and will get done this month. Icebox is where you park the ideas that are interesting but not committed. This stops your backlog from becoming a graveyard of 200 tasks nobody will touch, which is demoralizing and destroys signal.

"Needs Review" is where work sits when the creator thinks it's done but it hasn't been approved or tested by anyone else. This column gets clogged constantly on teams that don't have a clear reviewer assigned. Watching that column fill up is one of the most useful diagnostic signals a producer gets.

"In Integration" is the column most teams skip and then suffer for. It covers the gap between "this asset/feature works in isolation" and "this thing actually works in the current build." On a Unity or Unreal project, integration is real, non-trivial work, and pretending it doesn't exist as its own stage creates invisible crunch.

Tool recommendation: for teams up to about six people, I genuinely like **Trello** (free tier is enough to start) or **Hacknplan**, which was built specifically for game dev and has built-in task types for art, code, design, and audio. HacknPlan has a free tier and paid plans per user, and it is worth it if your team is even slightly serious. For larger indie teams or anyone with a publisher relationship, **Jira** works but you'll spend a week configuring it before it stops fighting you.

## The WIP Limit Thing (Most Teams Skip This and It Kills Them)

Work-in-progress limits are the part of kanban that most indie teams implement last, if ever. That's backwards. WIP limits are the mechanism that transforms a visual task board into an actual flow management tool.

The concept: each column gets a maximum number of cards allowed at one time. If "In Progress" has a limit of 3 and there are already 3 cards there, nobody pulls a new card. Instead, they help clear a blocked card or do a review. The constraint forces collaboration and surfaces bottlenecks.

Without WIP limits, a small team tends to have far more tasks "In Progress" than it has people, and cycle time (the time from starting a task to it landing in Done) stretches out as everyone context-switches between half-finished work. Adding a limit to the In Progress column usually shortens cycle time, not because anyone is working faster, but because people are switching contexts less.

A reasonable starting point: set your WIP limit for "In Progress" at roughly 2x your team size. If you have 3 people, try a limit of 6. Then watch what happens. You'll almost certainly find that the limit reveals a review bottleneck, at which point you can add a separate WIP limit to "Needs Review" as well.

Picture a two-person team (one generalist dev, one artist) building a puzzle game for Steam. Two months in with no WIP limit, they have a pile of tasks stuck in "In Progress," most of them half-started art assets. They set a WIP limit of 4, finish or abandon everything currently in progress, and restart. With only a few cards active at once, finished work moves to Done much faster. No new people, no crunch, just focus.

## Where Kanban Breaks Down for Game Dev

I'd be doing you a disservice if I didn't acknowledge this: kanban is a flow tool, not a planning tool. It will not help you figure out your scope. It will not prevent feature creep. It will surface blockers, but only if your tasks are written clearly enough that a blocker is visible.

The most common failure mode is tasks that are too large. "Make the combat system" is not a kanban task. It will sit in "In Progress" for three months, the column will technically not look blocked, and you'll have no idea whether you're making progress. Break it down. "Implement basic melee hitbox detection" is a task. "First pass on combo animation states" is a task. If a card takes more than three or four days for one person, it should probably be two cards.

The second failure mode: teams that update the board religiously during the first month, then let it drift when things get busy. It happens on plenty of projects. The board becomes stale, people stop trusting it, and they go back to Slack threads and memory. The fix is a short, mandatory weekly board review (30 minutes, no longer), where everyone moves their cards and flags blockers. Ship it or skip it. There's no middle ground; a half-maintained board is genuinely worse than no board.

One book I recommend here without reservation: *Kanban: Successful Evolutionary Change for Your Technology Business* by David J. Anderson. It's the closest thing to a canonical text on modern kanban practice. It's written for software teams but translates cleanly.

## Sources

- Anderson, David J. *Kanban: Successful Evolutionary Change for Your Technology Business* (2010): The foundational text on kanban for software and knowledge work; covers WIP limits and flow metrics in depth.
- HacknPlan Official Documentation (hacknplan.com): Game-dev-specific project management tool with built-in task categorization for different production disciplines.
- Atlassian Kanban Guide (atlassian.com/agile/kanban): Well-maintained reference for kanban fundamentals including WIP limits and board setup; Trello and Jira integration guidance.
- *The Game Production Handbook*, Heather Maxwell Chandler (3rd ed.): Covers production methodologies for game teams, including lightweight agile approaches suited to small studios.

---


*Photo: [RDNE Stock project](https://www.pexels.com/@rdne) via Pexels*