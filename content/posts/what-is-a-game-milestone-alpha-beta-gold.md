---
title: "What Is A Game Milestone Alpha Beta Gold"
date: 2026-05-22T10:02:50.859818+00:00
draft: false
description: "A game milestone explained: discover what alpha, beta, and gold mean in game development, how each stage differs, and why they matter before a game launches."
image: "https://images.pexels.com/photos/30965502/pexels-photo-30965502.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
categories: ["industry intel"]
tags: ["what", "game", "milestone", "alpha", "beta"]
author: "Samantha Roberts"
author_bio: "Samantha Roberts writes about game publishing, pitching, and bringing games to market."
slug: "what-is-a-game-milestone-alpha-beta-gold"
affiliate_disclosure: true
faqs:
  - q: "What's the difference between Alpha and Beta in game development?"
    a: "Alpha means all planned features are implemented but the game isn't content complete and has significant bugs. Beta means the game is content complete, meaning you can play it start to finish, and the team is focused on bug closure, performance, and preparing for platform certification. The boundary between them is content completion, not quality."
  - q: "Do indie studios need to follow these milestone definitions?"
    a: "You're not legally required to use any specific labels, but if you're working with a publisher or a platform holder, your contract will almost certainly reference these terms with specific exit criteria attached to them. Even self-publishing indie teams benefit from treating milestones formally because it forces scope discipline. Informal development with no milestone gates is one of the top causes of scope creep."
  - q: "How long does platform certification take?"
    a: "Initial cert reviews typically take 2-5 business days on major platforms, but a failed submission and resubmission cycle can cost you 1-2 weeks or more. Budget for at least two submission rounds in your schedule. Some certification requirements (like achievement/trophy configurations and age rating submissions through ESRB/PEGI) need to be started weeks before your planned submission date."
  - q: "What happens if a publisher rejects a milestone?"
    a: "The publisher will usually issue a formal rejection with a list of deficiencies. Your contract should specify a cure period, typically 2-4 weeks, during which you address the issues and resubmit. Payment for that milestone is withheld until acceptance. This is why exit criteria documents matter so much. If your criteria were clear and agreed upon upfront, a rejection dispute is much easier to resolve."
  - q: "What tools do game producers use to track milestones?"
    a: "Jira is industry-standard for bug tracking and sprint management in studios with 10 or more people. Hack n Plan is a strong choice for smaller indie teams and has milestone tracking built specifically for game production workflows. For documentation and production bibles, Notion and Confluence are both commonly used. Some studios use Shotgun (now ShotGrid) for asset tracking alongside a separate task manager. The specific tool matters less than having a consistent, team-wide practice of updating it."
author_slug: "samantha-roberts"
author_title: "Contributing Writer"
---

You're three months into production on a mid-sized mobile RPG when the publisher emails asking for your Alpha build delivery date. Your lead programmer looks at you. Your art director looks at you. You look at the calendar. Nobody in the room agrees on what "Alpha" actually means, and now you're negotiating a contractual deadline against a definition your team has never formally discussed. This happens constantly, and it costs studios real money.

Milestone terminology sounds like basic industry vocabulary, but it's one of the most consistently misunderstood areas in game development. I've been in rooms where two senior producers argued for twenty minutes about whether a build qualified as Beta. The labels are old, they're borrowed from software development, and different publishers use them slightly differently. What you need is a working framework that keeps your team aligned and protects you during publisher conversations.

## Why Milestone Definitions Matter More Than You Think

Milestone gates aren't just vocabulary. They're contractual triggers. Most publishing agreements tie payment tranches directly to milestone approvals: 20% on Alpha acceptance, 20% on Beta, final payment on Gold. If your contract says "Alpha" but your team is building to a different internal definition, you're setting up a billing dispute before you've even finished the game.

Beyond the money, milestone definitions drive sprint planning, staffing decisions, and QA scope. A team that treats Alpha as "all features in, even if broken" will staff and schedule completely differently than a team that treats it as "playable vertical slice." Neither interpretation is universally wrong. The problem is operating without a shared definition.

Get this locked down in your production bible before you sign anything. If you're already signed and this is fuzzy, call a definition meeting this week.

## Pre-Alpha: The Work Nobody Talks About

Pre-Alpha is the phase most articles skip, but it's where the game actually gets built. There's no single industry standard for when Pre-Alpha starts, but practically it covers everything from concept lock through first playable.

During Pre-Alpha you're doing foundational work: engine selection, core loop prototyping, pipeline setup, art style validation, and early tech spikes. Your team is small. Content is sparse. The builds you're shipping internally aren't representative of the final product and shouldn't be shown to anyone outside the core team.

The milestone that ends Pre-Alpha is usually called "First Playable" or "Proof of Concept." This is a narrow, polished slice, maybe 10-15 minutes of gameplay, that proves the core mechanic works and the visual style is achievable. Publishers often fund or greenlight based on this deliverable. Don't treat it as a rough prototype. Treat it like a pitch. It's making a promise about what the full game will be.

**Key Pre-Alpha deliverables typically include:**

- Core gameplay loop functional in-engine
- Art style guide finalized with at least one hero asset
- Target platform confirmed with hardware performance benchmarks
- Production schedule drafted through Alpha
- Tech stack and pipeline documented

## Alpha: Every Feature Exists, Not Everything Works

Alpha is the most abused term in game development. Here's the clearest definition I've landed on after years of using it across multiple projects: **Alpha means all features are implemented, but the game is not yet content complete and quality is not final.**

Every system the game ships with should be code-complete or very close to it by Alpha. Combat, inventory, save systems, UI flows, monetization hooks, whatever your game has, they should all exist and be testable. You're not adding new features after Alpha. That's the line.

What Alpha is not: bug-free. Not content-complete. Not polished. Alpha builds are often a mess, and that's expected. QA begins ramping up seriously at Alpha because you now have enough surface area to test methodically. Bug counts typically spike at Alpha acceptance, and that's a healthy sign, not a bad one.

For a 30-person studio shipping a 15-hour action RPG, a realistic Alpha might have:

- 60-70% of final content authored (levels, enemies, items)
- All core systems functional, with placeholder assets in some areas
- Initial performance pass complete, but optimization ongoing
- 300-600 known bugs logged, with P1s and P2s being actively closed

Publishers reviewing an Alpha build are checking whether you've built what you promised. They're not expecting perfection. They are expecting accountability to your GDD (Game Design Document) feature list.

## Beta: Content Complete, Quality Campaign Begins

Beta is where the game becomes the game. The defining characteristic of Beta: **content complete.** Every level is in. Every enemy type is in. Every cutscene, every item, every quest. The end credits play. You can finish the game.

What Beta is not: ship-ready. The Beta phase is a sustained quality campaign. Your QA team is running full regression passes. You're closing bugs, tuning difficulty curves, and stress-testing multiplayer if your game has it. Platform certification requirements (TRCs for PlayStation, TCRs for Xbox, Nintendo's lotcheck) become a daily concern.

Beta is often split into two sub-phases in larger productions:

| Phase | Definition | Primary Focus |
|---|---|---|
| Feature Complete / Alpha | All features implemented | System stability, QA ramp |
| Beta | All content complete | Bug closure, performance, certification prep |
| Gold Candidate (RC) | Believed ship-ready | Final cert submission, regression |
| Gold / RTM | Certified, released | Release, post-launch monitoring |

First-party console submissions typically take 2-5 business days for an initial response, but a failed cert submission can cost you 1-2 weeks. Build your schedule assuming at least two submission attempts. I've rarely seen a first submission pass clean on a complex title.

## Gold and RTM: The Finish Line Has Two Flags

"Going Gold" is the moment the game is certified and approved for manufacturing (for physical) or store submission (for digital). RTM stands for "Release to Manufacturing," a term that technically predates digital distribution but still appears in contracts and Slack channels everywhere.

Gold doesn't mean perfect. It means the game meets the minimum quality bar for release on its target platforms. By the time you go Gold, you almost certainly have a day-one patch already in cert or queued up. That's standard practice, not a sign of failure. The gap between Gold and release gives you time to push the patch through certification so it's available the moment players download the game.

The practical steps to get from Beta to Gold usually look like this:

1. **Bug triage meeting:** Lock the known issue list. Classify every open bug as fix-required, fix-if-time, or ship-with-known-issue with disclosure.
2. **RC (Release Candidate) build:** Compile a build you're prepared to submit. This build gets a unique version number and is archived permanently.
3. **Internal regression:** QA runs a scripted regression pass against the RC. Time-box this, typically 3-5 days depending on game scope.
4. **Platform submission:** Submit to Microsoft, Sony, Nintendo, Apple, Google, or whatever your targets are. Submission portals each have their own requirements and quirks.
5. **Certification pass or fail:** If fail, address the blocker issues and resubmit. Track your days carefully, cert failures directly threaten your release date.
6. **Gold declaration:** Once cert passes, you declare Gold internally. Pop the champagne. Briefly.
7. **Day-one patch queue:** Your patch should already be in cert or close to submission at this point.

Skipping or rushing any of these steps is how you end up with a botched launch that generates headlines for the wrong reasons.

## How to Keep Your Team Aligned on Milestones

Definitions alone aren't enough. You need process structures that make everyone operate from the same understanding.

**Write an exit criteria document for each milestone.** This is a one-to-two page document that lists specific, binary conditions that must be true for a milestone to be accepted. Not "game feels fun" (not binary). Instead: "All P1 and P2 bugs are closed," "All 14 levels are authored and playable start to finish," "Frame rate holds 30fps minimum on target low-spec hardware." If a condition is met, check it off. If it's not, you haven't hit the milestone.

Exit criteria documents also protect you in publisher conversations. If a publisher pushes back on a milestone delivery, you're not arguing about opinions. You're comparing a checklist.

**Use a purpose-built project management tool.** For game production, [Jira](https://www.atlassian.com/software/jira) remains the most widely used bug and task tracker in mid-to-large studios. For smaller teams, [Hack n Plan](https://hacknplan.com/) was built specifically for game development and has milestone tracking baked in. [Notion](https://www.notion.so/) works well for your production bible and exit criteria docs. Whatever you use, your milestone definitions should live somewhere the whole team can access, not just in the producer's head.

**For producers who want to go deeper on milestone management and production fundamentals,** _The Game Production Handbook_ by Heather Maxwell Chandler is the most thorough reference I've found. _Blood, Sweat, and Pixels_ by Jason Schreier is not a how-to manual, but it shows in painful detail what happens when milestone planning breaks down in the real world. Both belong on your shelf.

---


---

Milestone definitions won't make your game good on their own, but blurry definitions will absolutely make your project harder than it needs to be. Get your exit criteria written before your next milestone gate, share them with your publisher if you have one, and make sure every department lead can recite what "Beta" means on your project without looking anything up. That single discipline change has saved more than one project I've worked on from a very expensive disagreement at exactly the wrong moment.

*Photo: [Markus Winkler](https://www.pexels.com/@markus-winkler-1430818) via Pexels*