---
title: "Console Certification Checklist: Get Your Game Ready for PlayStation, Xbox and Nintendo Cert"
hide_title: true
date: 2026-10-06
lastmod: 2026-10-06
slug: "console-certification-checklist"
categories: ["production"]
tool: true
description: "An interactive pre-certification checklist covering the areas every console platform tests: stability, save data, accounts, controllers, system events, online, achievements, purchases, localization, ratings and the submission package."
image: "/img/heroes/4523032.jpg"
author: "Stephen Brenish"
author_slug: "stephen-brenish"
author_title: "Lead Game Producer"
author_bio: "Stephen Brenish is a Lead Game Producer at Epic Games (Fortnite, Unreal Engine) and founder of GameDevProducer, with 14+ years shipping and running live games at scale (previously Senior Program Manager at Blizzard Entertainment). Certified ScrumMaster."
faqs:
  - q: "What is console certification?"
    a: "Certification is the compliance test a platform holder runs before your game can be sold on its store. Sony, Microsoft and Nintendo each test builds against their own technical requirements, covering areas such as stability, save data, account handling, controller behaviour, system events, online features, achievements and store presentation. If the build fails, you fix the issues and resubmit."
  - q: "What are TRC, XR and Lotcheck?"
    a: "They are the names associated with each platform's requirements and testing. TRC is Sony's Technical Requirements Checklist, XR stands for Xbox Requirements, and Lotcheck is the name long used for Nintendo's submission testing. The documents themselves are confidential and available to licensed developers through each platform's developer portal."
  - q: "When should we start preparing for certification?"
    a: "In pre-production, by reading the requirements and designing systems such as saves, account handling and error messages to meet them. Run a first internal compliance pass at alpha, a full pass at beta, and a full regression on the release candidate before you submit."
  - q: "How many certification submissions should we plan for?"
    a: "Plan for at least two. Many first submissions come back with failures, and a resubmission window in the schedule turns that from a crisis into a normal step. Confirm current turnaround times with each platform holder when you book your submission."
  - q: "Is this checklist the official requirements list?"
    a: "No. It covers the areas every console platform tests so you can find problems early, but each platform's actual requirements are confidential, platform-specific and updated over time. Map every item to the current documents from each platform holder before you submit."
---

Certification is the one test in game development you cannot argue with. A platform holder plays your build against its technical requirements, and if it fails, it does not ship. The failures are rarely exotic. They are save files that break on a full drive, a controller that drops mid-boss-fight with no pause, a network error that leaves an endless spinner, or a button prompt from the wrong console.

This checklist covers the areas every console platform tests. Work through it with your QA team before you book a submission, and the formal requirement documents become a verification step rather than a list of surprises.

{{< cert-checklist >}}

## How to run a pre-certification pass

A pre-cert pass is a deliberate internal test of your build against the platform's requirements, run before the platform holder runs its own.

1. **Get the current requirement documents for every platform** as soon as you are licensed, and check for updates before each pass. Requirements change.
2. **Give compliance one owner.** Someone on QA or production owns the mapping from requirements to test cases and tracks every open item. Shared ownership means no ownership.
3. **Map every requirement to a test case** in your test management tool, and tag each with the platforms it applies to.
4. **Test every hardware model and mode** you list on the store: base and upgraded consoles, digital editions, handheld and docked.
5. **Log failures against the requirement they break**, with reproduction steps, and verify every fix on a fresh build.
6. **Submit with complete paperwork.** Missing forms, wrong version numbers and asset errors delay submissions that would otherwise pass.

## When to do what

| Phase | Certification work |
|---|---|
| Pre-production | Read every platform's requirements. Design save, account, input and error handling to meet them from the start. |
| Production | Build compliance into features as they are made. Start age rating applications early. |
| Alpha | First internal compliance pass. Expect long lists; that is the point. |
| Beta | Full pass on every platform and hardware model. All declared languages tested. |
| Release candidate | Full regression on the exact build you will submit. Store assets and paperwork finalized. |
| Submission | Submit the build and package. Keep the team on fixes, not new work. |
| After results | Fix failures, verify, resubmit. A resubmission window in the schedule keeps launch intact. |

The [game development schedule planner](/game-development-schedule-planner/) reserves this window automatically when you select console platforms, including a separate milestone for age ratings and a resubmission window before gold.

## Where first-time teams get caught

Most certification failures fall into a handful of categories, and almost all of them are cheaper to design for than to fix late.

- **Edge-case hardware.** A crash that only happens on one console model is still a failure. Test everything you list.
- **Mid-session events.** Notifications, sign-outs, controller disconnects and suspend and resume all happen during play. Each needs a defined, tested behaviour.
- **Save data under stress.** Missing, corrupted and out-of-space cases need handling, not just the happy path.
- **Achievements.** Unobtainable or mis-triggered unlocks, and offline unlocks that never sync.
- **Localization.** If a language is declared on the store, every string must be translated and fit the UI.
- **The submission package.** Wrong asset sizes, inaccurate metadata and missing paperwork.

For the full process from developer registration through approval, read [how console certification works for producers](/posts/console-game-certification-process-for-producers/).

## What this checklist is and is not

It is a structured way to find compliance problems early, organized around the categories every console tests. It is not a copy of any platform's requirements. Sony, Microsoft and Nintendo provide those confidentially to licensed developers, they differ by platform, and they change. Use this to get ready, then verify against the current documents for every platform you ship on.

If you are planning the rest of the launch, the [indie game launch checklist](/posts/game-launch-checklist-for-indie-developers/) covers marketing and store readiness, and [alpha, beta and gold explained](/posts/what-is-a-game-milestone-alpha-beta-gold/) defines the milestones certification sits between.
