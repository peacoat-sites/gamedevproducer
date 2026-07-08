---
title: "Master Your Game Dev Timeline in 5 Steps"
date: 2026-06-01T15:35:05.536548+00:00
draft: false
description: "Plan your game dev project with confidence. Learn how to create a realistic game development schedule, set milestones, manage tasks, and hit your deadlines."
image: "/img/heroes/273153.jpg"
categories: ["planning"]
tags: ["create", "game", "development", "schedule"]
author: "Ryan Cole"
author_bio: "Ryan Cole covers game production and milestone planning at GameDevProducer."
slug: "how-to-create-a-game-development-schedule"
affiliate_disclosure: true
faqs:
 - q: "How long should a game development schedule actually be for an indie game?"
   a: "Depends heavily on scope and team size, but here's a rough framework. Solo developer making a small arcade-style game: 6-12 months. 2-4 person team making a mid-scope narrative or platformer: 18-30 months. Team of 6-10 making something with substantial content (RPG, open world lite, etc.): 2-4 years. If your timeline is shorter than these, check your scope assumptions carefully. If it's longer, check your team structure. The research on indie completion rates suggests that projects scoped beyond 3 years for small teams have very low completion rates, largely due to team and motivation dynamics"
 - q: "What's the difference between a milestone schedule and a sprint schedule?"
   a: "A milestone schedule defines the major project gates: what the game looks like at pre-production complete, vertical slice, alpha, beta, and gold. These are typically monthly or quarterly checkpoints. A sprint schedule operates inside those milestones, usually in 2-week cycles, and defines exactly which tasks the team is working on right now. You need both. The milestone schedule tells you if you're on track for the big picture. The sprint schedule tells you what to do on Tuesday."
 - q: "Should I use story points or hours for game dev estimates?"
   a: "Honestly, the research here is mixed. Story points have the advantage of decoupling estimation from calendar time, which reduces the anchoring bias that comes when you say 'this will take 8 hours' and then feel obligated to finish in 8 hours regardless. Hours have the advantage of being immediately readable by non-technical stakeholders (producers, leads, publishers). For most game teams, I recommend starting with hours but converting to a velocity-based tracking system once you have 4-6 weeks of actual data. That data will tell you your team's real throughput far better than any upfront estim"
 - q: "How do you handle schedule dependencies, like when art blocks programming or vice versa?"
   a: "Map your critical path explicitly. The critical path is the sequence of dependent tasks where any delay directly delays the milestone. In game dev, this is often: design spec locks, then art starts, then programming integrates, then QA validates. If art is waiting on design, that's a critical path block. Dependencies need to be visible in your schedule tool, not just in someone's head. I keep a separate 'dependency register' (even if it's just a short table) that lists every cross-discipline hand-off point, who owns it, and when it needs to land."
 - q: "What do I do when my team consistently underestimates tasks?"
   a: "Stop trying to fix the estimates. Start tracking actuals and calculate your team's estimation ratio. If estimates are consistently 60% of actuals, apply a 1.7x multiplier to all future estimates automatically. This is called a velocity adjustment and it's much more reliable than trying to get people to estimate better through willpower. Over time, as you build a history of similar tasks, your estimates will naturally improve because they'll be anchored to real data rather than optimism."
author_slug: "ryan-cole"
author_title: "Senior Contributing Writer"
lastmod: 2026-07-08
---
Most game development schedules are wrong the moment you finish writing them. I don't mean slightly off. I mean the average game ships 40-75% later than its original internal estimate, and that's not a stat from bad studios, it's basically industry standard. I spent a long time thinking this was a discipline problem, a planning problem, or a "we just need better tools" problem. What I eventually figured out is that it's actually a fundamental misunderstanding of what a game development schedule is supposed to do.

## Why Your Mental Model of "The Schedule" Is Probably Broken

Most people come into game production thinking a schedule is a prediction. You list all the tasks, estimate the hours, stack them against your team's capacity, and land on a ship date. That's project management 101, and it works great for building a bridge or rolling out a software update with well-defined requirements.

Games don't have well-defined requirements. You're discovering the game as you make it. A mechanic that looked solid on paper spends three months in engine before your lead designer admits it isn't fun. An artist knocks out a character in two days and then spends three weeks on the next one because the reference was ambiguous. Your milestone date was based on the version of the game you imagined in month one, not the one you're actually building in month six.

What a game development schedule actually does: it's a communication tool. It tells your team where they're supposed to focus right now. It tells your publisher or leadership what you've committed to. It's a forcing function that creates accountability. The schedule being "wrong" isn't failure, it's information. What matters is how fast you respond to that information.

Once I started treating schedules as living documents that I expected to change, my whole approach to building them shifted.

## Start With the Big Shape Before You Touch a Spreadsheet

Before you open Jira or Hansoft or whatever tool you're using, you need to rough out the shape of your project at a high level. This is sometimes called top-down scheduling, and it's the step most first-time producers skip because it feels too vague. That's exactly why you need it.

Start with three anchor points:

**Your ship date (or funding runway).** Work backward from this. If you have 18 months of runway, you do not have 18 months to develop the game. You need 2-3 months of buffer for submission, certification, marketing asset delivery, and the inevitable crunch that happens when you think you're done but aren't.

**Your genre and scope benchmarks.** Look at games similar to yours made by teams of similar size. How long did they actually take, not their announced schedule, but the real timeline? For a 2-4 person indie team, a polished single-mechanic mobile game might be 8-12 months. A narrative RPG with 6 hours of content from a team of 10 might be 2-3 years. If your internal estimate is half the industry benchmark for your scope, someone is lying to themselves.

**Your phase gates.** Broadly: pre-production, production, alpha, beta, gold. These mean different things at different studios, so define them explicitly for your project. I've seen "alpha" mean "all features in but rough" at one studio and "content complete" at another. Write it down. Make everyone agree.

Only after this top-down sketch does detailed task-level scheduling make sense. Otherwise you're stacking bricks without knowing how tall the building is supposed to be.

## Building the Detailed Schedule: A Step-by-Step Approach

Here's the process I actually use, refined over a lot of painful projects:

**Step 1: Break work into features, not tasks.**
Start at the feature level: "Enemy AI patrol behavior," "main menu and settings flow," "procedural dungeon generation." Don't go to individual tasks yet. This is your feature list, and it should map directly to what makes your game the game.

**Step 2: Assign a t-shirt size to each feature.**
S, M, L, XL. This is fast, low-friction estimation. Get your leads in a room (or a call) and size each feature together. Disagreements here are gold, they surface misaligned assumptions early.

**Step 3: Convert sizes to time ranges, not point values.**
An S item might be 1-3 days. M is 3-8 days. L is 1-3 weeks. XL is 3-6 weeks. If something is bigger than XL, break it down further. You don't have enough clarity on it yet to schedule it.

**Step 4: Add a complexity multiplier.**
For anything involving new tech, untested design concepts, or external dependencies (voice recording, outsource partners, platform certification), multiply your estimate by 1.5-2x. This isn't pessimism. It's pattern recognition.

**Step 5: Plot features against milestones, not calendar dates.**
Assign features to milestones (pre-production complete, vertical slice, alpha) before you assign them to weeks. This way, if a milestone slips, you can see what moves with it rather than just watching dates cascade.

**Step 6: Load-balance against your actual team.**
Map features to people and check for overloads. One artist can't simultaneously own environment art, UI, and VFX for the same milestone. This sounds obvious. You'd be amazed how often it happens.

**Step 7: Build in explicit buffer at the milestone level.**
At least 15-20% buffer time before each major milestone. Not padding every individual task, that creates slack that gets filled with scope creep. Buffer at the gate level, where you can protect and manage it deliberately.

## The Tools That Actually Help (and What They're Not Good For)

| Tool | Best For | Watch Out For |
|---|---|---|
| **Jira** | Sprint-level task tracking, bug tracking, large teams | Setup overhead, can become a reporting theater exercise |
| **Hansoft** | AAA-scale milestone tracking, gantt-style views | Expensive, steep learning curve, overkill for indie |
| **Hack n Plan** | Game-specific task management, indie/mid-size teams | Limited integration options, smaller community |

Let's talk tools, because producers always want to know what to use.

| Tool | Best For | Watch Out For |
|---|---|---|
| **Jira** | Sprint-level task tracking, bug tracking, large teams | Setup overhead, can become a reporting theater exercise |
| **Hansoft** | AAA-scale milestone tracking, gantt-style views | Expensive, steep learning curve, overkill for indie |
| **Hack n Plan** | Game-specific task management, indie/mid-size | Smaller community, fewer integrations |
| **Notion** | Feature documentation, lightweight schedule wikis | Not a real project management tool, limits at scale |
| **Trello** | Very small teams, early pre-production | Falls apart fast above 4-5 people or complex schedules |
| **Spreadsheets (Sheets/Excel)** | Fast top-level milestone planning, reporting to execs | Doesn't scale, version control nightmare |

My honest take: for teams under 8 people, a well-maintained spreadsheet combined with Trello or Notion gets you 80% of the way there. For teams above 15, you need something like Jira or Hansoft because the coordination cost of informal systems starts eating everyone's time.

If you want to go deeper on production methodology, the book I recommend most often is *Game Production Toolbox* by Heather Maxwell Chandler. It's dense and practical, not theoretical. Clinton Keith's *Agile Game Development* is also worth reading if you want to understand how to actually adapt Scrum and Kanban to game teams, which is different from adapting it to software teams in ways that matter.

For online learning, the Game Producers community and GDC Vault both have solid production-focused sessions. The GDC talks by producers at Insomniac and Respawn in particular are unusually candid about scheduling and process.

## Tracking Actuals and Adjusting Without Losing Your Mind

Building the schedule is the easy part. Maintaining it is where most producers burn out or give up and let the schedule become a fiction everyone ignores.

The thing that made the biggest difference for me was weekly actuals tracking. Every week, every feature lead tells me what was completed, what's in progress, and what's blocked. Not what percentage done something is, percentage complete is a lie people tell themselves. I want to know: is this feature shippable right now? If yes, it's done. If no, it's not done. Binary.

When actuals diverge from plan by more than 10-15% two weeks running, you don't wait. You have three choices: cut scope, add time, or add resources (which often adds time, as Brooks' Law famously points out). There is no fourth option where you "make up the time." In 14 years, I've never seen a game team make up significant time. They almost always make it up with crunch, which costs you quality, team health, and future velocity.

The research on crunch and productivity is actually pretty clear here. Teams working 60-80 hour weeks see a short burst of output followed by a significant quality and velocity drop after about 3-4 weeks. The net time gain is often close to zero, and the human cost is real. Sustainable pace isn't a soft concept. It's a schedule integrity concept.

Reschedule early and visibly. The studios I've seen handle this best have a culture where re-estimating is normal and expected, not a sign of failure. The studios with the worst crunch cultures are the ones where acknowledging schedule risk feels career-threatening.

## Pre-Production Is Where the Schedule Is Actually Won or Lost

## Sources

- on crunch and productivity is actually pretty clear here
- to extrapolate your full production schedule


Here's the thing most new producers don't realize: the time you invest in pre-production directly determines how accurate your production schedule can be. You can't schedule what you don't understand. If your core loop isn't locked, if you haven't prototyped your riskiest systems, if your art style isn't defined enough to estimate asset counts, you're not scheduling production, you're scheduling hope.

A good vertical slice solves this. Not a vertical slice as a demo for investors (though it can serve that purpose), but a vertical slice as a production reality check. One level, fully representative of all your art, design, and tech systems. Time how long it actually took. Use that data to extrapolate your full production schedule. This is the most accurate scheduling method I know for games, because it's based on real measured velocity rather than theoretical estimates.

What surprised me when I first started doing this consistently was how often the vertical slice revealed that the original production timeline was off not by 10-20%, but by a factor of 2. Better to know that at month 3 than month 12.

Getting a game development schedule right isn't about finding the perfect template or the best tool. It's about building a system where you learn fast, communicate clearly, and make scope and timeline decisions based on what's actually happening rather than what you hoped would happen. The schedule is never going to be perfectly accurate. The goal is for it to be useful.