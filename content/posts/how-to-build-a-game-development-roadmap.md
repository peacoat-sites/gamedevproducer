---
title: "Your Game Dev Roadmap: Steps From Concept to Launch"
date: 2026-06-12T11:58:23.150495+00:00
draft: false
description: "Learn how to build a game development roadmap with clear steps, timelines, and milestones to take your game from concept to launch successfully."
image: "/img/heroes/7964147.jpg"
categories: ["project management"]
tags: ["build", "game", "development", "roadmap"]
author: "Stephen Brenish"
author_bio: "Stephen Brenish is a Lead Game Producer at Epic Games (Fortnite, Unreal Engine) and founder of GameDevProducer, with 14+ years shipping and running live games at scale (previously Senior Program Manager at Blizzard Entertainment). Certified ScrumMaster."
slug: "how-to-build-a-game-development-roadmap"
affiliate_disclosure: true
faqs:
  - q: "How far out should a game development roadmap go?"
    a: "For most projects, plan in detail for the next three to four months and keep everything beyond that at milestone granularity. If your total production timeline is under 18 months, you can sketch the full arc. Beyond 24 months, detailed long-range planning is mostly fiction."
  - q: "What's the difference between a roadmap and a production schedule?"
    a: "A roadmap defines what you're building and when you'll hit key gates. A production schedule defines who is doing what task on which days. You need both, but they live at different levels of detail and change for different reasons. Don't conflate them or you'll manage by spreadsheet and lose sight of direction."
  - q: "Should I use Agile or a milestone-based approach for my game?"
    a: "Honestly, most successful game teams I've worked with use both. Agile sprints handle day-to-day task management and keep teams moving. Milestone gates handle the bigger directional decisions. The mistake is trying to use pure Scrum all the way to ship, because it creates the illusion of progress without answering whether you're building the right thing."
  - q: "When should I first share the roadmap with my team?"
    a: "Early and often. The roadmap shouldn't be a producer artifact handed down from above. Getting your leads involved in setting milestone definitions and identifying the critical path dramatically improves buy-in and surfaces risks you won't see from a spreadsheet. Even a 30-minute working session with your leads before you finalize anything is worth it."
  - q: "What do I do when the roadmap is clearly wrong but leadership won't adjust it?"
    a: "Document everything. Update your confidence percentages. Make the delta between the current plan and realistic delivery visible in writing, repeatedly. If you're being pressured to maintain a roadmap you know is wrong, that's a project health problem, not a roadmap problem, and your job is to make the risk legible, not to paper over it."
author_slug: "stephen-brenish"
author_title: "Lead Game Producer"
lastmod: 2026-08-12
---
Most game development roadmaps I've seen are either dishonestly optimistic or so vague they're useless. And I'll be honest: I was guilty of building both kinds before I figured out what actually works.

The roadmap problem in game dev is specific and weird. Unlike software products shipping to millions of users with clean analytics and fast feedback loops, games have long creative development cycles, enormous scope uncertainty, and a finish line that keeps moving because "fun" is a design target, not a checkbox. The tools that work great for SaaS sprints don't translate cleanly. Scrum purists will tell you to run two-week sprints and hold your standups and trust the process. What they won't tell you is that a sprint velocity means almost nothing when your lead designer is prototyping a combat system that might get cut in month four.

So let's talk about what actually makes a game development roadmap useful.

## Start with milestones, not tasks

The first mistake most new producers make is building a roadmap that's really just a massive backlog sorted by date. That's a schedule. Not a roadmap. A roadmap answers a different question: *where are we going, and how will we know we've arrived?*

For game development, milestones are the answer. Specific, demonstrable milestones. Not "complete combat" but "player can attack, dodge, and die with final placeholder animations, reviewed and signed off by creative director." The difference matters enormously when you're three months in and someone's debating whether combat is "done enough" to move on.

The industry has fairly standard milestone gates: First Playable, Vertical Slice, Alpha, Beta, Gold. But the definitions vary wildly between studios, and if you're building a roadmap for an indie project or a smaller team, you probably don't need all of them. What you do need is a shared understanding of what each gate means *for your specific project*. Write that definition down, ideally in a real [milestone document](/posts/how-to-write-a-game-production-milestone-document/), and make it concrete. I've been in milestone reviews where two senior developers had completely different mental models of what "Alpha" meant, and neither of them was wrong by generic industry standards. They were just building different things in their heads.

Define no more than four or five major milestones for a project under two years. Each one should be something you can put in front of a publisher, investor, or even just a fresh playtest group and have them understand the state of the game without you explaining it. If you need to explain why something counts as a milestone, it probably doesn't.

## The Vertical Slice is doing a lot of heavy lifting

I want to spend some time here because the Vertical Slice milestone is where most roadmaps silently fail.

The Vertical Slice is supposed to be a representative slice of your finished game: one level, one encounter, one complete loop, built to near-shipping quality. The point is to prove the concept before you commit to full production. What actually happens on most projects I've seen, and ran myself, is that the Vertical Slice becomes a showcase artifact built by your best people under crunch, completely disconnected from the production pipeline the rest of the team will use. Then Full Production starts and everything slows to a crawl because nobody built the actual systems during the VS, they built the *impression* of the systems.

What stands out talking to producers across different studios is how differently they approach this. Some skip a formal VS entirely in favor of aggressive prototyping phases where they're explicitly allowed to throw things away. Others treat the VS as a systems test, not a visual quality test. The specific approach matters less than the intent: use the pre-production phase to answer your highest-risk questions, not to build something impressive.

When you're plotting this milestone on your roadmap, ask yourself: what are the three things most likely to kill this project? Put those in front of the VS. If the core loop is risky, prototype it first. If the tech is risky, prove the tech. Don't build the UI before you know whether the core mechanic is fun.

## Building the actual roadmap document

Okay, practically speaking. Here's how I'd approach this.

Start in whatever tool your team will actually look at. Notion, Confluence, even a shared Google Doc works better than a beautifully formatted document in a tool nobody opens. I've used Hacknplan (it's built specifically for game dev, runs about $6-9 per user per month for the paid tier) and it's solid for studios that want game-specific task tracking. Productboard works if you're managing a more complex stakeholder situation. For most indie teams, an honest Notion database with a timeline view is completely sufficient.

Your roadmap document should contain, at minimum:

The major milestones with their concrete definitions. Dates attached to milestones, not to individual tasks (you'll move tasks constantly; you move milestone dates rarely and deliberately). The critical path: which features or systems have to be done before other things can start? A rough capacity map: how many people are on the project, in what disciplines, and for how long? Any known external dependencies: hardware certification windows, platform submission deadlines, convention demo dates that are immovable.

What the roadmap should *not* contain at this level: individual task assignments, daily or weekly granularity, speculative features without a decision made, or a final ship date before you've completed your Vertical Slice. I know that last one is uncomfortable when publishers or bosses want a date. The honest answer is that you can give a target window, but committing to a specific ship date before you know your game works is how you end up in a death march.

## Scope: the conversation nobody wants to have

Every producer I respect has developed a habit I'd call aggressive scope interrogation. You question everything on the list, repeatedly, throughout the project. Not because you're trying to make a smaller game, but because you're trying to ship a *finished* game.

The research on this is genuinely mixed. Some designers argue that constraints breed creativity and a tight scope forces better design decisions. Others, particularly on bigger systemic games like RPGs or sims, argue you need generous scope to find the fun through iteration. Both are true in different contexts. Scope management is more about *when* you cut than *how much* you cut.

The roadmap is your tool for making scope decisions visible. When someone wants to add a feature, the question isn't "is this a good idea?" The question is: "which milestone does this fall before, and what does it push out?" Making the tradeoff explicit changes the conversation. I've watched feature requests evaporate the moment a developer has to say out loud which other thing they're willing to delay.

There are two books I keep recommending on this. "The Art of Game Design" by Jesse Schell covers design decision-making in ways that directly inform scope conversations. For the production and business side, "Blood, Sweat, and Pixels" by Jason Schreier is required reading. Not as a how-to, but because it documents, with brutal specificity, what happens when scope and roadmap discipline break down.

## The endgame: code lock, cert, and going gold

There's one stretch of the roadmap worth calling out on its own, because it runs on someone else's clock: the path from code lock to a shipping build. On console especially, "launch" is not the real deadline. Certification is, and it sits weeks earlier.

The back end of the schedule usually runs in this order:

- **Feature complete / code complete.** Everything intended is in and building; no new systems after this point.
- **The locks.** Larger teams lock in stages to stabilize: art lock, audio lock, design lock. A locked department stops producing new content and only fixes and tunes. The last of these, content lock, is the bridge to certification.
- **Code lock (hard lock).** Only critical, cert-blocking fixes go in, because every change is now a risk to a build you are about to submit.
- **Release candidate / candidate master.** The build you actually submit.
- **Certification.** The platform holders test your build against their technical and policy requirements. Sony's checklist is the TRC, Microsoft's the TCR, and Nintendo runs Lotcheck.
- **Gold master.** The approved build, locked for distribution. Going gold means certification passed.

The reason this belongs on the roadmap and not just in a QA plan is the calendar cost. Certification review commonly runs one to four weeks per submission, and roughly six to ten weeks per platform from first submission to approval once resubmissions are counted. First submissions frequently come back with issues, so it's reasonable to budget two to three rounds per platform, with each rejection adding a few weeks to fix, rebuild, regression-test, and resubmit. On a multi-platform launch, those windows stack.

The practical implication is straightforward: schedule backward from the certification submission date rather than the store date, and set code lock earlier than the team expects to need it. Placing the cert window on the roadmap early, and treating it as fixed, lets the final stretch of production plan around it instead of colliding with it.

## Living with uncertainty without lying to yourself

Your roadmap is a hypothesis. The moment you treat it as a commitment, it starts killing your project. This sounds obvious but the pressure comes from everywhere: publishers want dates, team members want clarity, you want to believe you know what you're doing. The answer isn't a more detailed roadmap. It's a more honest conversation about confidence levels.

A practice I started leaning on a few years ago is explicitly labeling each milestone with a confidence percentage. Not "the game ships in Q3 2026" but "we're targeting Q3 2026, currently 60% confident." That number forces a conversation. When it drops, something's wrong. When it rises, you've de-risked something real. It sounds soft but it's actually more rigorous than a clean date, because it acknowledges what you actually know.

Update your roadmap in a regular cadence, at least monthly, more often if you're in pre-production. Treat updates as a ritual, not a crisis response. If your roadmap only changes when something goes catastrophically wrong, you've lost the plot.

## Sources

- [Game development process and milestone gates (GDKeys)](https://gdkeys.com/game-development-process/)
- [Certification and submission testing: TRC, TCR, and Lotcheck (Kudos QA)](https://www.kudosqa.com/services/certification-submission-testing)

*Photo: [Felicity Tai](https://www.pexels.com/@felicity-tai) via Pexels*
