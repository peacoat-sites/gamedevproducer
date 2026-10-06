---
title: "Getting Your Game Certified: Console Approval Roadmap"
date: 2026-05-24T09:15:10.803142+00:00
draft: false
description: "Learn how the console game certification process works for producers, covering submission requirements, technical checks, and approval steps for major platforms"
image: "/img/heroes/4523032.jpg"
categories: ["industry intel"]
tags: ["console", "game", "certification", "process", "producers"]
author: "Stephen Brenish"
author_bio: "Stephen Brenish is a Lead Game Producer at Epic Games (Fortnite, Unreal Engine) and founder of GameDevProducer, with 14+ years shipping and running live games at scale (previously Senior Program Manager at Blizzard Entertainment). Certified ScrumMaster."
slug: "console-game-certification-process-for-producers"
affiliate_disclosure: true
faqs:
 - q: "How far in advance should I start the certification process?"
   a: "Start your internal compliance pass no later than eight weeks before your target ship date. If you're doing a simultaneous multi-platform launch, add another two weeks of buffer. Platform cert windows are largely outside your control, so the only variable you can manage is how ready your build is when it enters the queue."
 - q: "What happens if we fail certification?"
   a: "You'll receive a report listing the failures the platform holder found. You fix the issues, cut a new build, and resubmit. There's no penalty beyond time lost. That said, if you're on a tight retailer-mandated ship date for a physical release, repeat failures can have real business consequences."
 - q: "Can we ship a patch day-one to fix things that didn't make cert?"
   a: "No. The build that passes cert is the build that ships. Any changes after certification require a patch, which also goes through a (usually faster) certification review. Day-one patches are common, but they don't replace certification."
 - q: "Is certification different for patches and DLC?"
   a: "Yes, and usually faster. Patch and DLC submissions go through a lighter review process than a full game submission. Turnaround is usually quicker than for a full game submission. The requirements still apply, but the scope of testing is smaller."
 - q: "Do indie studios get treated differently in cert than large publishers?"
   a: "The requirements are the same regardless of studio size. What differs is access to platform support. Larger publishers often have a dedicated platform relations contact who can expedite questions or flag issues before submission. Indie studios working through the standard developer programs typically rely on documentation and developer forums. Joining programs like the ID@Xbox or PlayStation Indies initiative can improve your access to support resources."
author_slug: "stephen-brenish"
author_title: "Lead Game Producer"
lastmod: 2026-10-06
---
You've just hit your ship date. The build is stable, the team is exhausted, and someone in the room asks, "So how long does cert actually take?" The honest answer is: longer than you budgeted, almost certainly. Each submission takes time, turnaround varies by platform and by season, and a single failure means another round. If you didn't plan for that buffer, you're already in trouble. This article is for producers who want to stop being surprised by that number.

## What Certification Actually Is (and Why It Exists)

Cert isn't a formality. It's a mandatory quality and compliance gate controlled by the platform holder. Sony, Microsoft, and Nintendo each maintain their own set of technical requirements, and your game has to pass every single applicable one before it can appear on their storefronts.

These requirements aren't arbitrary. They're designed to protect the platform experience: consistent network behavior, correct handling of system-level events like low storage or incoming calls, accessibility standards, age rating compliance, and crash-free operation across all supported hardware SKUs. Players expect a certain floor of quality when they buy from a walled-garden storefront. Certification is how the platform holder enforces it.

Each platform runs its own process with its own documentation. The mechanics differ, but the stakes don't: fail, and you don't ship.

## The Cert Requirements Documents You Need to Read Before Your Pre-Alpha

Read the technical requirements documentation now, not six weeks before submission. All three major holders publish their requirements documents through their developer portals. Sony has the Technical Requirements Checklist (TRC). Microsoft has the Xbox Requirements (XR). Nintendo has their Guidelines documentation.

These documents are dense, sometimes hundreds of items long, but they're your actual test plan. The ones that bite studios most often are:

- **Save and load behavior**: Your game must handle corrupt or missing save data gracefully, without crashing or hanging.
- **Network error handling**: Every online feature must fail cleanly if the connection drops mid-session.
- **System notifications**: If a party invite, trophy notification, or system alert appears during gameplay, your game can't break.
- **Suspend and resume**: On modern consoles, players can put their system in rest mode and come back. Your game needs to handle that without data loss.
- **Trophy and Achievement integration**: These must behave exactly as the platform specifies, including offline unlocking behavior.

Assign someone on your team the explicit job of tracking your compliance against these requirements from day one. It's infinitely easier to build to spec than to retrofit compliance in the last two months.

## The Submission Process, Step by Step

This is the part producers actually need to manage. The exact steps vary by platform, but here's the general shape:

1. **Complete your first-party developer registration**: You need an approved developer account and access to the partner portal before you can submit anything. This alone can take weeks if you haven't started the process.
2. **Obtain your age ratings**: You'll need ratings from ESRB (North America), PEGI (Europe), and any other relevant regional bodies before submission. Apply early. IARC (the unified self-classification tool) speeds this up for digital releases.
3. **Build your submission binary**: This is a cert-specific build, not your debug build. It has to be close to final, with [gold master-level stability](/posts/what-is-a-game-milestone-alpha-beta-gold/).
4. **Run your internal first-party compliance pass**: Using the requirements documents, your QA team needs to systematically verify your build against every applicable requirement. Use a spreadsheet or a purpose-built test management tool. Zephyr Scale inside Jira or TestRail are both solid choices here.
5. **Submit your build and documentation through the partner portal**: This includes your submission form, marketing assets, and any required legal agreements. Missing documentation is a fast path to rejection.
6. **Wait for first-party QA**: The platform holder's team will test your build. Turnaround varies by platform and by season, and queues tend to lengthen ahead of the holidays, so ask for current estimates when you book.
7. **Address any certification failures (CFs)**: If you fail, you'll get a report. Fix the issues, cut a new build, resubmit. This cycle can repeat.
8. **Receive cert approval**: Once you pass, you'll get a cert approval and can schedule your release date.

Plan for at least two submission attempts. Plenty of games don't pass on the first try. That's not a failure of your team; it's the reality of how many requirements exist. The [game development schedule planner](/game-development-schedule-planner/) builds that resubmission window into your dates automatically.

## Platform Comparison: What's Different Between Sony, Microsoft, and Nintendo

| Factor | PlayStation (Sony) | Xbox (Microsoft) | Switch (Nintendo) |
|---|---|---|---|
| Requirements documentation | TRC (Technical Requirements Checklist) | Xbox Requirements (XR) | Guidelines on the Nintendo Developer Portal |
| Where you manage submissions | PlayStation Partners | Partner Center | Nintendo Developer Portal |
| Age ratings | ESRB, PEGI and IARC as applicable | ESRB, PEGI and IARC as applicable | ESRB, PEGI and IARC as applicable |
| Physical release | Arranged with the platform holder or your publisher | Arranged with the platform holder or your publisher | Game cards are manufactured through Nintendo |

Budget the timeline separately for each platform you ship on. Requirements, tooling and turnaround differ, and passing on one platform tells you nothing about the others. If you ship on handheld hardware such as Switch, give memory and performance particular attention.

## Common Certification Failures and How to Prevent Them

The same categories of failures show up across almost every studio going through cert for the first time.

**Crash on edge-case hardware configurations**: Test on every hardware SKU the platform supports, including older models and digital editions. A PS5 crash on the disc version that doesn't happen on the digital edition is a cert failure.

**Improper handling of mid-session events**: A notification pops up, the player gets a friend request, or the system goes into standby. If your game can't handle these cleanly, you'll fail.

**Incorrect trophy or achievement logic**: Offline unlocking needs to sync properly. Trophies can't be awarded for things that haven't happened. Platinum logic must work correctly.

**Missing or broken localization**: If you've declared support for a language, every piece of player-facing text and UI must be translated. Partial localization gets flagged.

**Store page asset errors**: Wrong resolutions, incorrect aspect ratios, missing required screenshots. This sounds trivial, but it delays submission.

Run a pre-certification audit six to eight weeks before your planned submission date. This gives you time to fix issues without torching your ship date.

## Tools That Help Producers Manage Cert

You don't need to manage this process in a spreadsheet and prayer.

**TestRail** is purpose-built for test case management. Create a test suite directly mapped to the TRC or XR document items and track your team's compliance pass results in one place.

**Jira with Zephyr Scale** works well if your studio already lives in Jira. You get test cycle tracking alongside your existing project backlog.

**Notion or Confluence** are solid for building your certification knowledge base. Document every certification failure you receive, how you fixed it, and what caused it. That institutional memory is gold on your next project.

Before your first submission, run the build through the [console certification readiness checklist](/console-certification-checklist/). It covers the areas every platform tests, saves your progress, and exports to CSV for your test tracker.

---

Certification isn't the enemy. It's a system you can learn, plan for, and build around. The studios that get blindsided are the ones who treated it as someone else's problem until the last month of development. The ones who ship on time are the ones who made compliance a first-class part of production from the start. That's the whole secret.

*Photo: [Polina Tankilevitch](https://www.pexels.com/@polina-tankilevitch) via Pexels*
