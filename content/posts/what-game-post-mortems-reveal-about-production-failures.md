---
title: "What Game Post-Mortems Reveal About Production Failures"
date: 2026-05-23T07:37:14.864428+00:00
draft: false
description: "Learn what game post-mortems reveal about common production failures, from scope creep to poor communication, and how developers can avoid repeating costly mist"
image: "https://images.pexels.com/photos/7437090/pexels-photo-7437090.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
categories: ["industry intel"]
tags: ["what", "game", "post-mortems", "reveal", "about"]
author: "Ryan Cole"
author_bio: "Ryan Cole covers game production and milestone planning at GameDevProducer."
slug: "what-game-post-mortems-reveal-about-production-failures"
affiliate_disclosure: true
faqs:
  - q: "How long should a game post-mortem actually be?"
    a: "Long enough to be honest, short enough that people read it. For an internal post-mortem, I'd aim for 1,500 to 3,000 words with specific examples attached. GDC post-mortems run longer because they're written for a public audience. The format matters less than whether the people who made the decisions actually wrote it."
  - q: "Should post-mortems be shared publicly?"
    a: "That depends on your studio culture and contractual obligations. Public post-mortems are enormously valuable for the industry. But internal ones should happen first, without the editing that comes with public disclosure. Don't let the fear of public scrutiny turn your internal post-mortem into a PR document."
  - q: "When in development should you run a post-mortem?"
    a: "After every major milestone, not just at the end of the project. Waiting until ship means you're reviewing 18 months of decisions all at once. Milestone post-mortems let you actually change behavior during production, which is the whole point."
  - q: "What's the single most common production failure across post-mortems?"
    a: "Unclear ownership. Not scope, not crunch, not communication, though those all connect to it. When nobody knows who has final decision-making authority on a feature, that feature takes twice as long and satisfies nobody. Define ownership before you write a single line of code."
  - q: "Are there good resources for reading real game post-mortems?"
    a: "Yes. GDC Vault has hundreds archived, many free to access. The book Postmortems: Selected Essays Volume One by various GDC authors collects some of the best ones in print. Gamasutra (now Game Developer) has a full archive online. Reading ten of them back to back is more valuable than most production courses."
author_slug: "ryan-cole"
author_title: "Senior Contributing Writer"
---
You shipped the game. Or maybe you didn't, and it's sitting in a folder somewhere labeled "v_final_ACTUAL_final2." Either way, something went wrong during production, and you're trying to figure out what. Here's something that tends to surprise people outside the industry: the Game Developers Conference has published post-mortems since 1997, and across hundreds of them, the same five or six failure patterns show up over and over again. Not variations on a theme. The exact same problems. That should tell you something about how rarely teams learn from each other, and how much they could.

## Scope Creep Isn't a Feature Problem, It's a Decision Problem

Every post-mortem that mentions scope creep frames it as "we added too many features." That's accurate but incomplete. What actually happened is that someone didn't say no, and nobody built a system that made saying no easy.

The 2002 post-mortem for *Black & White* is a textbook case. The team kept layering in new mechanics because the game felt thin. The game shipped late, over budget, and still felt thin in places, because feature additions don't fix design problems. They bury them under the wreckage.

Here's what I tell people when they're in the middle of this: scope creep is a symptom of unclear success criteria. If you defined "done" precisely, adding a feature would feel like a violation of something concrete. When "done" is fuzzy, every new idea sounds reasonable.

Practical fix: before you enter production, write a one-page document that answers three questions. What does the player do every session? What's the one thing the game has to do better than anything else? What would you cut if you had to ship in half the time? If your team can't answer all three, you're not ready for production.

## Communication Failure Compounds Everything Else

Read enough post-mortems and you start noticing something. Teams rarely say "we had a communication problem." They say things like "the art team didn't know about the engine change" or "QA wasn't looped in until month eight" or "the publisher's feedback came too late." That's all communication failure wearing different clothes.

The *Ultima IX: Ascension* post-mortem from 2000 described a situation where engine changes invalidated months of level design work, and the level designers found out after it happened. The leads knew. The leads assumed someone else had told them. Nobody had.

In my experience, the most dangerous phrase in game dev is "I assumed they knew." You have to build workflows where critical information travels by default, not by memory. That means standups that actually surface blockers, not just status theater. It means a single source of truth for the current design spec, not a folder with seventeen versions of a design document.

Tools that help here: **Notion** or **Confluence** for living documentation that everyone can access and update. **Shortcut** (formerly Clubhouse) for tracking tasks with visibility across disciplines. For smaller teams, even a well-maintained **Trello** board beats email threads.

## Crunch Doesn't Save Schedules. It Extends Them.

This one is hard for people to accept because crunch feels productive. You're working 70 hours a week. Things must be getting done faster.

They're not.

Research from the Software Engineering Institute and repeated anecdotal evidence from post-mortems both point the same direction: sustained crunch above 50 hours a week produces net negative output after about three weeks because error rates climb, judgment degrades, and key people quit or burn out right when you need them most.

The *Fallout: New Vegas* post-mortem touched on this. Obsidian had an 18-month development window for a massive RPG. The crunch was severe. The game shipped with a legendary bug count. More hours went in during the final stretch. More bugs came out.

The pattern in post-mortems is almost mechanical: team hits a milestone late, management adds crunch to recover, crunch introduces bugs and reduces morale, next milestone slips further, more crunch is added. It's a compression spiral. You can't compress your way out of it.

Most crunch periods are symptoms of a schedule that was never realistic to begin with. Which leads to the next problem.

## Estimates Were Wrong Because Nobody Validated Them

Ask a programmer how long a feature will take. Double it. Now you're closer. This is a running joke in the industry but it's actually pointing at a real cognitive bias called the planning fallacy: people systematically underestimate task duration even when they have historical data showing they've been wrong before.

Post-mortems consistently show that initial estimates were made by the people who were most excited about the project, during the period when the project was least defined. That combination is almost guaranteed to produce underestimates.

Here's what actually works for getting better estimates before production locks in:

1. **Break every feature down to tasks under 8 hours.** If you can't do that, the feature isn't defined well enough to estimate.
2. **Have the person doing the work give the estimate, not the lead.** Leads are optimistic. Implementers are closer to reality.
3. **Add a 20% buffer to every sprint, minimum.** Not to absorb laziness. To absorb unknowns, which always exist.
4. **Track your estimate accuracy per sprint.** If you're consistently off by 40%, adjust your estimation formula. This is called velocity tracking, and it's standard in agile frameworks for good reason.
5. **Run a pre-mortem.** Before you commit to a timeline, ask the team: "Assume we shipped late. What caused it?" You'll surface risks nobody was consciously acknowledging.

Tools: **Jira** with proper sprint velocity tracking is the industry standard for mid-to-large teams. **Hack n' Plan** is built specifically for game dev and handles task breakdown well. For learning the methodology, Jason Schreier's *Blood, Sweat, and Pixels* is essential reading. It's not a textbook but it shows you what these failures look like from the inside.

## The "What Went Right" Section Is Often a Warning Sign

Most post-mortems follow a two-column format: what went right, what went wrong. The "what went right" section is supposed to be instructive. It often isn't, and here's why.

Teams list things like "our team was passionate" and "we shipped" as wins. Passion isn't a production methodology. Shipping something doesn't mean it shipped well. When a post-mortem's "what went right" column is full of cultural platitudes and the "what went wrong" column is full of process failures, that team did not actually learn why it succeeded or failed. It learned how to feel okay about it.

The post-mortems worth studying are the ones where the wins are as specific as the failures. "We built a vertical slice in week four and it revealed that our core mechanic wasn't fun, which let us pivot before we'd committed eighteen months to the wrong direction." That's actionable. "We had a great team" is not.

If you're writing a post-mortem right now, push your team to be uncomfortable in both columns. Specificity is the whole point.

---

The same failures keep appearing in post-mortems because reading about them isn't the same as building systems that prevent them. You can know every pattern in this article and still watch your next project repeat all of them, because production failures aren't knowledge problems. They're habit, incentive, and structure problems. The post-mortem is just the mirror. What you do after you look in it is the actual work.