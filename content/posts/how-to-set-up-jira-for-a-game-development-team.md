---
title: "Getting Your Game Team Started With Jira"
date: 2026-06-21T11:27:12.518137+00:00
draft: false
description: "Learn how to configure Jira for game development workflows, from sprint planning and bug tracking to asset management and milestone delivery."
image: "/img/heroes/5569379.jpg"
categories: ["tools"]
tags: ["jira", "game", "development", "team"]
author: "Jordan Lee"
author_slug: "jordan-lee"
author_title: "Game Developer"
author_bio: "Jordan Lee has shipped indie titles and contributed to larger studio projects, writing from the trenches about what it actually takes to finish and release a game. At Gamedev Producer the focus is development workflow, scope, and shipping."
slug: "how-to-set-up-jira-for-a-game-development-team"
affiliate_disclosure: true
faqs:
 - q: "Should we use Jira's built-in roadmap or a separate tool like Miro or Notion?"
   a: "Jira's Roadmap view works fine once you're in production and your epics are defined, but it's genuinely bad for anything involving visual planning or fuzzy, pre-production thinking. I'd use Jira's Roadmap for milestone tracking and dependency visibility, and Miro or a whiteboard tool for anything that needs creative flexibility."
 - q: "How many projects should a game have in Jira?"
   a: "Usually one project per game, with components handling the discipline breakdown. You might add a second project specifically for QA bug tracking if your QA team is external or working under a separate process, but keep it to two maximum. More than that and your cross-project queries become a full-time job."
 - q: "What's the best Jira template to start from for game dev?"
   a: "Start from the 'Scrum' template, not 'Kanban' and not 'Business.' Then immediately customize the issue types and workflow states as described above. The Scrum template gives you sprint infrastructure without locking you into a pure Kanban flow, which most game teams eventually want some version of for production."
 - q: "How do we track QA regression without drowning the dev board in bug tickets?"
   a: "Create a dedicated 'QA' component and a saved filter that separates QA-reported bugs from dev-discovered ones. During a regression phase, your QA lead owns a separate board filtered to just that component. Devs see only the bugs assigned to them, not the full bug list. This is one of those things where Jira actually shines once it's configured correctly."
 - q: "Is Jira worth it for a 2-3 person indie team?"
   a: "Probably not, honestly. Jira Free (up to 10 users) costs nothing, but the overhead of maintaining it is real. For a team under four people, I'd recommend Notion with a simple kanban template, or even Linear, which has a much lighter setup cost and a free tier. Come back to Jira when you're adding your fifth or sixth person and the coordination cost starts to hurt."
lastmod: 2026-07-08
---

Most Jira setups I've seen in game studios are basically a software engineering template with "sprint" swapped for "milestone" and a handful of custom fields nobody fills out. That's not a game dev workflow. That's a web app workflow wearing a hat.

If you're setting Jira up for the first time, or you've inherited a mess and you're trying to fix it, you might be wondering where the standard advice goes wrong. Here's what I tell people: Jira is genuinely good for game dev, but only if you set it up around how games are actually made, not how software products ship. Those are different enough that the defaults will actively hurt you.

## Start with your issue type hierarchy, not your board

The first mistake teams make is jumping straight to the board view and starting to drag cards around. Don't. The board is just a window into your data. If the data structure is wrong, no board layout saves you.

Here's the hierarchy I use, and have used across projects from a 4-person indie to a 60-person console team:

**Epic** = a major feature or system. "Player Combat," "Level 2," "Audio Pass," "UI Overhaul." These map to the things your leads talk about in milestone reviews.

**Story** = a discrete, shippable unit of work within that feature. "Implement sword swing animation state machine," "Wire up health bar to player stats." A story should be completable by one person in a week or less. If it takes three weeks, it's not a story, it's an epic you mislabeled.

**Task** = the smallest tracked unit. Art tasks, bug investigation, a specific document to write. Some teams skip stories and go straight to tasks under epics, which works fine for small teams (under 10 people).

**Bug** = its own type, always. Never mix bugs into your story backlog. They need separate tracking, separate priority logic, and separate reporting. I've seen teams put bugs into the main sprint backlog and wonder why their velocity numbers make no sense. Bugs aren't velocity work, they're debt payment.

Sub-tasks are optional. I'd say avoid them until you feel actual pain from not having them, because they add overhead fast.

## The fields that actually matter (and the ones to kill)

Jira's default fields include things like "Fix Version," "Affects Version," "Priority" (using a scale from Blocker to Trivial), and a bunch of others that game teams fill in inconsistently and then never use for anything.

Here's what I'd actually configure:

**Discipline label or component.** You need to know at a glance whether a ticket is Art, Engineering, Design, Audio, or QA. Jira's "Components" field handles this well. Set it up. It'll save you from spending 20 minutes hunting for all the audio tickets before a milestone review.

**Milestone or target build.** Not sprint. In game dev, sprints are internal delivery cycles, but milestones (Alpha, Beta, Gold, whatever your publisher calls them) are the external commitments. Track both. Use a custom "Milestone" field tied to your release structure. This is how you answer "what's at risk for Alpha" without rebuilding a spreadsheet every time.

**Priority.** Keep it simple. I use four levels: Critical (blocking someone right now), High (this milestone), Medium (next milestone or flexible), Low (nice to have). The five-level default scale causes more arguments than it prevents.

Kill the "Story Points" field if your team isn't doing estimation seriously. Points without calibration are noise. A lot of small game teams are better served by T-shirt sizing (S/M/L/XL) or just tracking days. Don't cargo-cult scrum practices you don't have the team size to support.

## Board configuration for a game team

You probably want two boards, not one.

The first is a sprint board for your active work. This is what your team looks at daily. Columns should reflect your actual workflow states, not the generic "To Do / In Progress / Done." For a game dev team, something like:

**Backlog > Ready > In Progress > In Review / QA > Done**

"Ready" means the ticket is groomed, has acceptance criteria, and someone can pick it up without asking questions. That column alone will improve your standups. If something's been in "In Review" for more than three days, it's blocked, not in review.

The second board is a milestone or roadmap board. This is what your producers and leads look at weekly. Filter it to show only epics and their status. Jira's Roadmap view (in next-gen projects) does this reasonably well without much configuration.

Don't give everyone edit access to both boards. It sounds restrictive, but open-access boards in game studios tend to turn into a game of ticket archaeology within about six weeks.

## Automation that's worth setting up on day one

Jira's automation rules are underused. Here are three that pay for themselves immediately:

When a bug is marked Critical, auto-assign it to the lead for that component and post to your team's Slack channel. Takes 10 minutes to set up. Saves you from a Critical bug sitting unnoticed over a weekend.

When all sub-tasks under a story are done, transition the parent story to "In Review." This sounds minor until you're managing 40 active stories and trying to figure out what's actually closeable.

When a sprint ends with open tickets, auto-transition them to the next sprint backlog rather than dumping them into the main backlog black hole. You'll still want to review them manually, but at least they don't get lost.

Jira's built-in automation (under Project Settings > Automation) handles all of this without any external tools or scripting.

## The one thing most teams get wrong about Jira and game dev

## Sources

- [Jorge David Arley Campos](https://www.pexels.com/@jorge-david-arley-campos-3570916)
- structure is wrong


Here's the take that might push back against you: Jira is not great for tracking creative work at the concept stage, and trying to force it to be is where most game teams lose trust in their tooling.

Pre-production doesn't fit sprints. Concept art direction, narrative exploration, prototype iteration, those things are messy and non-linear. If you put a concept artist's exploration work into a sprint board, they'll either game the ticket system or stop using it, and either outcome is bad.

My recommendation is to keep Jira out of pre-production entirely, or create a separate "Sandbox" project with almost no structure, no sprint commitments, and just labels. Use Notion or even a shared Google Doc to track pre-production progress. Once something is in production, meaning the design is locked enough to build against, bring it into Jira. That transition point is the real milestone anyway.

---


*Photo: [Jorge David Arley Campos](https://www.pexels.com/@jorge-david-arley-campos-3570916) via Pexels*