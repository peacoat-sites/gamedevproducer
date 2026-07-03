---
title: "How To Structure Roles In A Small Game Studio"
date: 2026-06-24T11:21:17.038493+00:00
draft: false
description: "Learn how to structure roles in a small game studio to boost productivity, avoid burnout, and ship better games with a lean, focused team."
image: "https://images.pexels.com/photos/5439478/pexels-photo-5439478.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
categories: ["team management"]
tags: ["structure", "roles", "small", "game", "studio"]
author: "Jordan Lee"
author_slug: "jordan-lee"
author_title: "Contributing Writer"
author_bio: "Jordan Lee went from solo developer to small studio founder, shipping three commercial titles across PC and mobile over six years. Along the way, he learned most of what he knows about pricing, discoverability, and platform strategy the hard way, usually by getting them wrong first. At GameDevProducer, Jordan covers the business side of indie development: Steam algorithms, pricing strategy, how to build a sustainable studio without outside funding, and what actually moves the needle on launch day."
slug: "how-to-structure-roles-in-a-small-game-studio"
affiliate_disclosure: true
faqs:
 - q: "How do you handle a co-founder who wants a title that doesn't reflect their actual role?"
   a: "Give them the title and also give them a clear internal responsibilities doc that describes what they actually own. Titles are partly social currency; the internal accountability structure is what keeps work from falling through gaps. Both can coexist."
 - q: "Should a small studio have a dedicated producer, or can someone double up?"
   a: "Doubling up works until it doesn't, which is usually somewhere between 6 and 10 people. Below that, a producer-hat worn by a lead (usually design or art) is fine if they're disciplined about it. Above it, production falls behind and you start missing dependencies."
 - q: "What happens when two people both think they own the same area?"
   a: "Pick one. Publicly, clearly, without ambiguity. Shared ownership of a decision area is not ownership. It's a veto system that slows everything down. The person who doesn't 'win' should get a clearly defined adjacent area where they have final say."
 - q: "Do contractors count toward your team structure?"
   a: "For recurring work (ongoing art support, a QA contractor embedded in your sprint), yes, treat them structurally like a team member. Assign them ownership over their area and include them in dependency tracking. For one-off engagements, no. Treating a one-off contractor as a team member just creates confusion about their scope."
 - q: "When should a small studio start using formal project management software?"
   a: "Earlier than feels necessary. Two people can get away with a shared doc. At four people, you want a real task board. Hacknplan is purpose-built for games and worth the monthly cost. Jira works if you already know it, but it's overkill to learn from scratch at small scale. The important thing is that every task has one owner and one status, and everyone can see it without asking."
---

Most small studios get roles wrong before they write a single line of code. Not because they're disorganized, but because they copy the org chart from a studio twenty times their size and then wonder why nobody knows what they're supposed to be doing.

I've watched this happen up close. A five-person team with a "CEO," a "Head of Marketing," a "Lead Designer," and a "Creative Director", and somehow nobody owns the build pipeline. The titles felt serious. The game didn't ship.

Here's what I actually believe, after working in teams from 4 people to 400: at small scale, **roles should map to work, not identity**. That distinction sounds obvious, but it changes almost every decision you'll make about how to structure your team.

## The Fundamental Problem With Copying AAA Structure

Big studios have roles built around specialization and redundancy. You can have three people whose entire job is lighting because the game has 80 hours of content and lighting quality at that scale genuinely requires it. A small studio borrowing that model ends up with a "Lighting Artist" who spends three weeks lighting and then has nothing to do, while the one person who understands Unity's render pipeline is drowning.

What surprised me when I first started tracking this seriously was how consistently the bottleneck was never the thing the team thought it was. Teams would say "we need another artist" and the real problem was that nobody owned asset integration. Tasks were being completed but not shipped into the build. That's a producer problem, not a headcount problem.

Small studios don't need more roles. They need clearer ownership.

## Start With Work, Not Titles

Before you name a single role, list every recurring category of work your game actually requires. Not aspirationally. What does the game need done in the next 90 days?

For a typical 4-8 person indie team making a mid-complexity 2D or 3D game, that list usually shakes out to something like: programming (gameplay, tools, build), art (concept, production, tech), design (systems, level, UX), audio (sound design, implementation, occasionally music), and production (scheduling, dependencies, communication, QA coordination). That's it. Five functional areas. If you have eight people, that means almost everyone is covering more than one area. That's fine. That's the job.

What I'd recommend: write out every discrete task category, then assign each to a person. Not a title. A person. If a task category has no owner, you've found your first structural problem. If one person owns six categories and another owns one, you've found your second.

Titles come after this exercise, not before. And honestly? For a studio of six people, titles mostly matter for external-facing stuff (press, investors, developer relations) rather than internal clarity. Internally, what matters is who answers for what.

## The Roles That Actually Matter in a Small Studio

There are four functional responsibilities that consistently decide whether small studios ship or stall. Not because they're the most creative or the most technically impressive, but because they're the ones that get skipped.

**Someone who owns the schedule.** This doesn't need to be a full-time producer. It can be your lead programmer who spends six hours a week on it. But there must be one named person who knows what's in progress, what's blocked, and what's at risk. Tools like [Hacknplan](https://hacknplan.com/) (built specifically for game dev) or even a well-structured Notion board work fine at this scale. What doesn't work is "we all kind of know" because you don't, and you'll find out during crunch.

**Someone who owns technical infrastructure.** Build pipeline, version control discipline, integration testing, platform SDKs. This is usually your most senior programmer, but the key is that it's explicitly their responsibility, not a shared assumption. I've seen games delayed by six weeks because nobody owned the submission pipeline until three weeks before release.

**Someone who owns the player-facing design.** I mean the moment-to-moment experience: how does it feel to play this game for the first time? This is a design responsibility, but it bleeds into UX, onboarding, and difficulty tuning. In small teams this is often the creative director or lead designer. The important thing is that someone has explicit authority to make final calls here, because ambiguity in this area creates the most debate-to-output ratio of anything in game development.

**Someone who owns external communication.** Press, wishlists, community, storefronts. At a small studio this is often a founder wearing another hat. That's fine. But if it's nobody's job, it doesn't happen. Marketing inertia is one of the most common reasons good small games underperform commercially, and it almost always traces back to structural neglect rather than bad games.

## Generalists, Specialists, and the Myth of the T-Shaped Person

You've probably heard the "T-shaped" framing: deep in one area, functional in several. It's a reasonable model. But I'll be honest: at really small scale, more of your team needs to be closer to hyphen-shaped. Wide across multiple areas, genuinely competent in two or three, expert in one. The T assumes you have enough people that someone else covers the width. At four people, you don't.

The practical implication: when you're hiring (or deciding whether to contract vs hire), weight breadth more than most job postings suggest. A programmer who can also do basic UX and talk to players intelligently is worth more to a six-person studio than a programmer who is better at programming but nothing else. The gap in programming quality is real but often less impactful than the reduction in coordination overhead.

Contracts and freelancers make sense for genuine specialty spikes: a composer, a localization pass, console certification QA, a trailer editor. Work that has a clear scope and a defined end. For the roles described above, schedule, infrastructure, player experience, external communication, you want named people on your core team.

## Growing Out of Your Structure

## Sources

- [Hacknplan](https://hacknplan.com/)
- [Tima Miroshnichenko](https://www.pexels.com/@tima-miroshnichenko)
- or three


The structure that ships your first game will probably break on your second. That's not failure, it's growth. What you want to avoid is the structure breaking mid-project, which usually happens when a team grows from 6 to 12 people without explicitly revisiting who owns what.

The signal to watch for: when someone says "I thought you were handling that," a role boundary has failed. Track those moments. If the same boundary fails twice, fix it explicitly. Write it down. Put it in your team handbook, even if that "handbook" is a single Notion page.

A book I genuinely recommend here is *The Art of Game Design* by Jesse Schell for the design side, but for the structural and production side, *Game Production* by Heather Maxwell Chandler is more directly useful than anything else I've found. It's not glamorous reading but it'll save you months.

---


*Photo: [Tima Miroshnichenko](https://www.pexels.com/@tima-miroshnichenko) via Pexels*