---
title: "Platform Certification What Producers Need To Know"
date: 2026-05-29T00:01:37.787948+00:00
draft: false
description: "Learn what platform certification means for producers, why it matters, and how to meet key requirements to get your content approved and distributed successfull"
image: "https://images.pexels.com/photos/12899191/pexels-photo-12899191.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
categories: ["industry intel"]
tags: ["platform", "certification", "what", "producers", "need"]
author: "Tyler Brooks"
author_bio: "Tyler Brooks writes about studio management, team leadership, and the human side of game development."
slug: "platform-certification-what-producers-need-to-know"
affiliate_disclosure: true
faqs:
  - q: "How early should I start cert prep in the production schedule?"
    a: "Start tracking cert requirements at the beginning of beta, and do your first formal review pass at alpha. If you wait until content is locked, you're too late to address anything structural. Some technical requirements, like save system architecture or network error handling, touch core systems that are expensive to change late in development."
  - q: "What happens if we fail cert? Is the launch date automatically dead?"
    a: "Not automatically, but you need to be realistic. A failure with a few minor issues can sometimes be resolved and resubmitted within a week. A failure with multiple mandatory requirement violations, especially in areas like network behavior or save data, can take two to four weeks to fix and retest properly. If your launch date has zero slack, a single failure can blow it. Build your schedule with a buffer that assumes one failure cycle."
  - q: "Can we submit a day-one patch to fix cert issues instead of delaying?"
    a: "Sometimes, but not always. A day-one patch can fix gameplay bugs and content issues, but it cannot fix certain cert-specific behaviors (like save data handling or crash-on-boot) because those failures prevent the game from passing submission in the first place. The cert process tests the disc or download build. If that build fails, it doesn't ship."
  - q: "Do all games go through the same cert process, or does it vary by deal?"
    a: "The base requirements apply to everyone. That said, some platform holders offer a 'self-certification' or expedited path for certain developer tiers or for small, low-risk titles (particularly on Nintendo eShop). Larger partners with strong track records also tend to get more detailed feedback and sometimes faster turnaround. None of these exceptions eliminate the process, they just smooth some of the edges."
  - q: "What tools or resources should producers use to prepare for cert?"
    a: "The most useful resources are the official requirement documents themselves (always check the version number), your platform technical account manager if you have one, and a well-maintained tracking spreadsheet. For project management, Jira and Hacknplan both work well for tagging cert requirements to tasks. For broader production knowledge, the book 'The Game Production Handbook' by Heather Maxwell Chandler covers cert-adjacent processes clearly. Jason Schreier's 'Press Reset' is less prescriptive but gives you a clear picture of what goes wrong when these processes break down."
author_slug: "tyler-brooks"
author_title: "Contributing Writer"
---

You've locked content. The game runs. QA has signed off. Then someone on your team quietly mentions the cert submission deadline is in three days, and you realize you've never actually read the platform holder's technical requirements document. That moment of cold dread is completely avoidable, and it happens more often than anyone in the industry likes to admit. Platform certification has ended careers, delayed launches by months, and cost studios hundreds of thousands of dollars in overtime and lost revenue. It doesn't have to go that way.

## What Platform Certification Actually Is (And Why It Exists)

Certification, usually called "cert" in the industry, is the gatekeeping process platform holders use to ensure titles meet their technical, content, and business standards before appearing on their storefronts. Sony has its Technical Requirements Checklist (TRC). Microsoft uses the Xbox Requirements (XR) document. Nintendo calls theirs Lotcheck. Each one is a living document, updated regularly, and each has teeth.

The platform holders aren't doing this to torture you. Their reasoning is practical: one broken game that bricks consoles or exploits payment systems damages the entire platform. Certification is quality assurance at the ecosystem level. When you understand that framing, you stop fighting the process and start working with it.

What's in these documents? The categories typically cover: crash and hang behavior, save data integrity, online features and network error handling, age rating compliance, accessory support, user account handling, and content policies. Each requirement is numbered, and each one is a potential failure point. A single mandatory requirement failure means a full rejection, which usually means restarting the clock on a two to four week review window. That adds up fast.

Here's the part producers often underestimate: the requirements change. Microsoft updates XRs regularly. Sony's TRC evolves between console generations. A cert checklist you used on your last game may be out of date. Always download the current version directly from the dev portal. The version number is in the header. Check it.

## Building Cert Into Your Schedule (Not Bolting It On)

Most certification failures are scheduling failures before they're technical failures. The team never had enough runway to address cert requirements during production, so they're scrambling at the end.

I've seen projects where cert prep was literally a three-day task at the bottom of a milestone plan. Three days for a game shipping on three platforms. That's not a plan, it's a wish.

Here's a more realistic model. For a mid-size AA title shipping on PS5 and Xbox Series X|S simultaneously:

- **Cert review pass 1** should happen around alpha, roughly 12 to 16 weeks before launch. Assign your most technically literate QA lead to do a full manual review against both checklists. Document every requirement you haven't implemented yet.
- **Dev kit compliance testing** runs continuously from alpha through beta. This is where you catch save corruption, network timeout handling, and suspend/resume failures.
- **Cert submission prep** should begin no later than 6 weeks before your launch date. You want 4 weeks minimum for initial review, one potential failure/fix/resubmit cycle, and a buffer for anything unexpected.
- **Day-one patch** should be planned in your schedule regardless of whether you need it. Cert for patches goes through a lighter process, but it still takes time.

The tools that help most here are Jira or Hacknplan with a dedicated "Cert" label applied to any task touching a requirement, and a shared spreadsheet that maps each TRC/XR line item to the engineer or designer responsible for it. Accountability by name. Not "team" or "TBD." A person.

## The Most Common Cert Failure Reasons (And How to Prevent Them)

Platform holders don't usually publish failure rate statistics, but anyone who has managed multiple submissions has patterns burned into their brain. These are the areas that catch teams most often.

**Network error handling.** Your game must gracefully handle losing network connectivity at any moment. That means during matchmaking, mid-transaction, during a save, during a cutscene. Automated testing rarely catches all of these. Manual QA with network simulation tools is non-negotiable. On PlayStation, network error handling requirements are especially detailed.

**Save data behavior.** Corrupting a player's save file is among the worst things a game can do. Cert requirements mandate specific behavior when storage is full, when a save is interrupted, and when a save device is removed mid-write. These scenarios need dedicated test cases.

**Privilege and parental controls.** If your game has online features, in-game purchases, or user-generated content, you must respect platform-level parental control settings. This one fails submissions constantly because it's easy to implement the feature without wiring it to the platform's permission check.

**Age ratings.** You need ratings from the appropriate bodies (ESRB for North America, PEGI for Europe, CERO for Japan, etc.) before submission. You can't submit without them. Rating applications take time, sometimes 4 to 6 weeks. If you forgot to start that process, you're already behind.

**Localization and content policies.** Specific platforms and regions have rules about what can and can't appear in content. Nintendo's Lotcheck is particularly thorough about in-game text and visual content. If you're shipping in Germany, Japan, or Australia, know those regional rules before you finalize content.

## Step-by-Step: Running Your First Cert Submission

If you're a producer running a certification submission for the first time, here's the sequence that works.

1. **Download the current requirement document** from the official dev portal. Do this the day you start cert prep, not the day before submission.
2. **Create a requirement tracking sheet.** List every requirement by ID. Add columns for: status (pass/fail/N/A), assigned owner, notes, and date verified. Share it with your leads.
3. **Hold a cert kickoff meeting.** Walk your engineering and QA leads through the document section by section. Let them self-identify risks. You want them flagging problems, not you discovering them at submission.
4. **Run a focused cert build.** At least two weeks before submission, produce a build specifically tested against cert requirements. This isn't your regular QA build. It has cert-specific test cases.
5. **Complete the submission questionnaire accurately.** Platform holders ask you to declare what features your game uses: online play, in-game purchases, camera/mic support, etc. If you declare a feature that doesn't work, that's an automatic failure. If you omit a feature that's in the game, that's also a failure. Be precise.
6. **Submit during business hours, early in the week.** This is a small thing that matters. If you hit a technical issue with the submission portal on a Friday afternoon, you're losing two days. Monday morning gives you a full business week of support access.
7. **Prepare your failure response plan before you hear back.** If cert comes back with failures, you want to be able to fix and resubmit within 48 to 72 hours. That means having your cert engineer available and a tested build pipeline ready to go.

## Understanding the Difference Between Cert and Platform Review

These two processes are often conflated and they shouldn't be. Certification is technical and process-focused. Platform review (sometimes called store review or content review) is business and content-focused: does your game's store page comply with content policies? Is your trailer appropriate? Does your game description accurately represent the product?

Both can block your launch. Both have their own timelines. For a digital-only title, you typically need to submit your store assets (screenshots, description, trailer, pricing) at least two to three weeks before release. On consoles, store approval and cert are separate processes that sometimes run in parallel.

Plan for both in your schedule. Use a tool like Monday.com or Notion to build a pre-launch checklist that covers both tracks, not just cert.

## Comparing the Three Major Platform Cert Processes

| Platform | Document Name | Typical Review Time | Resubmission Wait | Portal |
|---|---|---|---|---|
| PlayStation (PS5/PS4) | TRC (Technical Requirements Checklist) | 2 to 4 weeks | 1 to 2 weeks | PlayStation Partners |
| Xbox (Series X|S / One) | Xbox Requirements (XR) | 2 to 4 weeks | 1 to 2 weeks | Partner Center |
| Nintendo Switch | Lotcheck | 2 to 5 weeks | Varies | Nintendo Developer Portal |

Nintendo's Lotcheck process tends to be the most detail-oriented of the three. The review is thorough, turnaround can be slower, and requirements around content and technical behavior are strictly enforced. Budget extra time for Nintendo submissions, especially if it's your first Lotcheck.

---

## FAQ

### How early should I start cert prep in the production schedule?

Start tracking cert requirements at the beginning of beta, and do your first formal review pass at alpha. If you wait until content is locked, you're too late to address anything structural. Some technical requirements, like save system architecture or network error handling, touch core systems that are expensive to change late in development.

### What happens if we fail cert? Is the launch date automatically dead?

Not automatically, but you need to be realistic. A failure with a few minor issues can sometimes be resolved and resubmitted within a week. A failure with multiple mandatory requirement violations, especially in areas like network behavior or save data, can take two to four weeks to fix and retest properly. If your launch date has zero slack, a single failure can blow it. Build your schedule with a buffer that assumes one failure cycle.

### Can we submit a day-one patch to fix cert issues instead of delaying?

Sometimes, but not always. A day-one patch can fix gameplay bugs and content issues, but it cannot fix certain cert-specific behaviors (like save data handling or crash-on-boot) because those failures prevent the game from passing submission in the first place. The cert process tests the disc or download build. If that build fails, it doesn't ship.

### Do all games go through the same cert process, or does it vary by deal?

The base requirements apply to everyone. That said, some platform holders offer a "self-certification" or expedited path for certain developer tiers or for small, low-risk titles (particularly on Nintendo eShop). Larger partners with strong track records also tend to get more detailed feedback and sometimes faster turnaround. None of these exceptions eliminate the process, they just smooth some of the edges.

### What tools or resources should producers use to prepare for cert?

The most useful resources are the official requirement documents themselves (always check the version number), your platform technical account manager if you have one, and a well-maintained tracking spreadsheet. For project management, Jira and Hacknplan both work well for tagging cert requirements to tasks. For broader production knowledge, the book "The Game Production Handbook" by Heather Maxwell Chandler covers cert-adjacent processes clearly. Jason Schreier's "Press Reset" is less prescriptive but gives you a clear picture of what goes wrong when these processes break down.

---

Certification doesn't reward heroics at the end of a project. It rewards diligence throughout. The producers who ship on time aren't the ones who got lucky in cert, they're the ones who treated the requirements document like a design constraint from day one, assigned real ownership to each item, and built their schedules around the reality of the process rather than the hope of skipping it. Start early, stay specific, and never assume your last game's checklist still applies. The platform holders will update their requirements whether you're watching or not.

*Photo: [Ron Lach](https://www.pexels.com/@ron-lach) via Pexels*