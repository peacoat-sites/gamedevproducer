---
title: "Platform Certification What Producers Need To Know"
date: 2026-05-21T17:30:53.656598+00:00
draft: false
description: "Learn what platform certification means for producers, why it matters, and the key steps you need to take to get certified and distribute your content successfu"
image: "https://images.pexels.com/photos/7915392/pexels-photo-7915392.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
categories: ["industry intel"]
tags: ["platform", "certification", "what", "producers", "need"]
author: "Jordan Reyes"
author_bio: "Scrum master turned producer. Translates agile methodology into game dev reality -- what works, what breaks."
slug: "platform-certification-what-producers-need-to-know"
affiliate_disclosure: true
---

You're three weeks from your target ship date. The build is stable, QA has signed off, and then your certification submission comes back with a Critical failure on TRC-R4052: your game doesn't properly handle a user's storage device being removed mid-save. The platform holder won't budge. You either fix it or you don't ship. Suddenly that three-week runway looks like a weekend.

Platform certification is one of the most underestimated risks in console game development. I've watched teams burn an entire launch window because they treated cert prep as a last-mile checkbox rather than a process woven into the whole production. It doesn't have to go that way.

## What Certification Actually Is (And Why It's Not Just QA)

Every major console platform, PlayStation, Xbox, and Nintendo, maintains a set of technical requirements that every game must pass before it can be distributed on that platform. Sony calls theirs Technical Requirements Checklist (TRC). Microsoft uses Title Requirements (TR). Nintendo uses Lotcheck guidelines. Apple has App Store Review Guidelines for iOS. These aren't suggestions. They're gatekeeping documents, and a single Critical failure blocks your submission entirely.

The confusion I see most often is teams treating cert like a QA pass. It's not. Your QA team is testing whether your game works as intended. Certification tests whether your game works within the platform's ecosystem. That means system-level behaviors: proper handling of notifications, suspend and resume cycles, screenshot functionality, accessibility compliance, online service integration, age rating enforcement, parental controls, and dozens of other requirements that have nothing to do with whether your gameplay loop is fun or your collision detection is solid.

The requirements documents are long. Sony's TRC for PlayStation 5 runs into hundreds of line items. Many of them are conditional based on your game's feature set, but you still need someone who knows which ones apply to you. Producers who haven't shipped on a specific platform before often don't realize how many edge cases exist around seemingly simple features like cloud saves or party chat.

## Building a Cert-Ready Production Calendar

Here's the honest timeline math. First-party cert review typically takes between 5 and 14 business days per submission, depending on the platform and their current queue depth. If you fail and need to resubmit, you're looking at another full review cycle. If you're launching on three platforms simultaneously, you're managing three independent queues that don't care about each other's schedules.

Work backwards from your target ship date. Add a minimum of three submission attempts per platform into your schedule. Not because you expect to fail three times, but because you need the buffer. Most experienced producers I know build in two failures as a baseline assumption for a first-time submission on a given platform.

A practical calendar structure looks like this:

1. **Identify all applicable requirements** at the start of production, not two months before launch. Pull the relevant platform documentation during pre-production and assign an engineer to own each requirement category.
2. **Schedule a Cert Readiness Review** at Alpha. Go through every applicable requirement line by line with your lead engineer and QA lead. Flag anything not yet implemented.
3. **Run internal cert testing during Beta.** Treat it as a formal test pass with written results, not a casual check.
4. **Lock a cert candidate build** at least 8 weeks before your intended ship date if you're a first-time submitter on that platform.
5. **Submit your first candidate** 6 to 7 weeks out. This gives you room for two resubmission cycles before your date becomes impossible.
6. **Hold a post-cert retrospective** regardless of outcome. Document what you learned for the next project.

If you're using Jira, Hack n Plan, or Shotgrid for production tracking, create a dedicated cert epic with individual tickets for every requirement category. Don't let this live in a spreadsheet that only one person has open.

## The Most Common Failure Categories (And How to Prevent Them)

Platforms publish their most common failure reasons, and yet teams keep hitting the same walls. Here's what actually shows up most often.

**Save data handling.** Interrupted saves, full storage states, and corrupted save detection are responsible for a disproportionate share of Critical failures. Build save error handling early. Test it obsessively. Physically pull a USB drive mid-save in your testing environment. Simulate a full hard drive. Don't assume your save system handles these gracefully just because it's never crashed during normal playtesting.

**Suspend and resume.** On modern platforms, your game can be suspended at virtually any moment: during a loading screen, mid-cutscene, inside a multiplayer session. Restoring correctly from a suspended state is non-trivial. This requires dedicated engineering time and dedicated test coverage. It is not a "we'll get to it" feature.

**Online requirements.** If your game has any online component, from leaderboards to cloud saves to multiplayer, the online requirement surface area expands dramatically. Network loss scenarios, server downtime handling, and age-gated online features all have specific requirements that vary by platform.

**Accessibility requirements.** This area is growing fast. Platforms are increasingly mandating minimum accessibility features. Subtitle controls, audio description support, and high-contrast UI modes have moved from nice-to-have to required in some submission contexts. Start accessibility implementation early. Retrofitting UI systems late in production is painful.

**Age rating and content descriptors.** Submitting without the correct ratings from ESRB, PEGI, or CERO is a basic but surprisingly common failure mode. The rating submission process takes time. Start it during Beta.

## Comparison: First-Party Cert vs. Third-Party Platform Review

Not all platform reviews work the same way. Understanding the differences helps you plan appropriately.

| Factor | Console First-Party (PS/Xbox/Nintendo) | PC Storefronts (Steam/Epic) | Mobile (iOS/Google Play) |
|---|---|---|---|
| Review time | 5 to 14 business days | 1 to 5 business days | 1 to 7 business days |
| Requirements document | Formal TRC/TR/Lotcheck | Minimal (store policies) | App Store / Play policies |
| Failure consequence | Full block, resubmission required | Usually patchable post-launch | Rejection, resubmission |
| Version control | Platform-controlled build versioning | Developer-controlled | Developer-controlled |
| Age rating | Mandatory pre-submission | IARC self-rating option | IARC or regional boards |
| Cert support access | Publisher/developer portal + platform rep | Developer support ticket | Developer support ticket |

Console certification is the highest-stakes environment because failures are absolute blocks and the review cycle is long. If you're a self-publishing indie team, you may not have a platform rep to ask questions to, which means the documentation is your only guidance. Read it carefully. Read it again.

## Working With Platform Representatives

If you have a platform relationship, meaning you've been assigned a developer relations contact or have access to a first-party developer support portal, use it actively throughout production. Not just at submission time.

I've seen teams sit on a requirements question for six weeks because no one wanted to "bother" the platform rep. That silence cost them a submission failure that a 10-minute conversation would have prevented. Platform reps field these questions constantly. It's their job. Ask early and ask specifically.

When you do reach out, be precise. Instead of "we have a question about online requirements," say "our game uses platform cloud saves but also has a local save fallback when the user is offline. We want to confirm whether TRC-O2214 applies to offline-only sessions." Specific questions get specific answers. Vague questions get you pointed back to the documentation you've already read.

Some platforms also offer pre-certification programs or lotcheck pre-checks for Nintendo specifically. These services let you get preliminary feedback on your submission before the formal review. Take advantage of them. The cost in time is trivial compared to a surprise failure.

## Tools and Resources Worth Using

Production management and cert prep are easier when you have the right infrastructure.

**Hack n Plan** is purpose-built for game development and handles cert tracking better than generic project management tools in my experience. Its task hierarchy maps cleanly to requirements categories.

**Jira** with a custom cert workflow (Backlog, In Dev, In QA, Verified, N/A) is the standard approach for larger teams. The overhead of setup pays off.

**TestRail** or **Zephyr Scale** for structured test case management during your internal cert pass. You need written test cases with expected results and actual results, not just a QA engineer's memory.

For learning the fundamentals, *Game Production Fundamentals* by Heather Chandler is a solid foundation. For platform-specific knowledge, there's no substitute for reading the actual requirements documents on the developer portals, but the book *The Game Producer's Handbook* by Dan Irish gives useful context on how to structure the overall process.

**Codecks** is worth looking at for smaller teams that find Jira too heavyweight. It integrates production tasks with a card-based interface that many developers find less friction-heavy.

For online courses, the Game Production certificate program at Coursera from Michigan State University covers milestone and submission processes in practical terms. Brandon Yanez's production courses on Udemy are more accessible and game-dev specific if you want something you can finish in a weekend.

---

## Frequently Asked Questions

### How early should we start cert prep on a new platform?

Start at the beginning of production, not at the end. Pull the TRC or equivalent document during pre-production. Assign requirement ownership to engineers by feature area. The goal isn't to implement everything immediately, it's to make sure every requirement has a named owner and a place in the backlog. Discovering a critical system requirement eight weeks from launch is avoidable if you read the docs early.

### What happens if we ship a patch and it breaks a cert requirement?

Platform policies on post-launch updates vary. On console, patch submissions go through a review process as well, though typically faster than initial certification. If a patch introduces a new Critical-level issue, it can be rejected. This is why regression testing against cert requirements should be part of every patch QA cycle, not just the initial submission.

### Do we need a publisher to access first-party developer portals?

No, but the process differs. Self-publishing developers can apply directly to first-party developer programs. Sony, Microsoft, and Nintendo all have application processes for independent studios. Approval timelines vary and can take several weeks. Apply early. Some platforms have minimum revenue or portfolio requirements for full access, so check the current qualification criteria for each platform.

### How do we handle certification for a simultaneous multi-platform launch?

Manage each platform's cert process as an independent workstream. Don't let them share a single review slot on your schedule. Stagger your first submissions by a few days if you can, so you're not managing parallel failures at the same time. Your platform-specific build configurations should be isolated enough that a fix for one platform doesn't require a new full test pass on another, but that depends on your architecture.

### What's the difference between a Critical and a Major failure in certification?

A Critical failure is a hard block. Your submission is rejected and you can't proceed without fixing it. A Major failure is a significant issue that typically requires resolution before approval but may allow limited exceptions in some contexts depending on the platform and the specific requirement. Minor failures are lower-priority issues that may require acknowledgment or a fix-by-plan. Definitions vary slightly by platform, so read your platform's specific severity classifications rather than assuming they're universal.

---

Certification doesn't have to be the crisis at the end of your project. It's a process with known requirements, known timelines, and known failure patterns. Treat it that way. Build your calendar around it, assign clear ownership, test early, and talk to your platform rep. The teams that get cert right aren't smarter than the ones that don't. They just started earlier and took the documentation seriously.

*Photo: [RDNE Stock project](https://www.pexels.com/@rdne) via Pexels*