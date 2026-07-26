---
title: "Game Post Mortem: Learning From What Went Right and Wrong"
date: 2026-07-26T10:15:43.684899+00:00
draft: false
description: "Discover how game studios conduct post mortems on finished projects to identify successes, failures, and lessons for future development."
image: "/img/heroes/8117405.jpg"
categories: ["production"]
tags: ["post", "mortem", "process", "finished", "games"]
author: "Samantha Roberts"
author_slug: "samantha-roberts"
author_title: "Publishing Strategist"
author_bio: "Samantha Roberts has spent her career navigating the publisher side of the games industry: first pitching indie studios to publishers, then working inside a publishing label evaluating hundreds of projects. She knows what publishers look for and what indie developers consistently get wrong in their pitch decks. At GameDevProducer, she covers publishing strategy, funding, and the business of bringing a game to market."
slug: "post-mortem-process-for-finished-games"
affiliate_disclosure: true
faqs:
  - q: "How long should a post mortem take?"
    a: "Budget two to three hours for the full-team session, plus significant async time before and after. The meeting itself is only a fraction of the process; the pre-survey, data audit, and written report are where most of the value is generated."
  - q: "Should contractors and external QA be included?"
    a: "Yes, with caveats. They often have the clearest view of process failures because they're less embedded in the studio culture. But they need explicit assurance that honest feedback won't affect future work. If you can't credibly offer that, collect their input through the anonymous survey only."
  - q: "What if the team is too burned out right after ship to do this well?"
    a: "Give people the decompression window first. Two weeks is reasonable. But don't let it slide past four weeks, because that's when memory starts softening and people mentally move on. Schedule the post mortem date before launch if you can."
  - q: "Do we need a formal facilitator?"
    a: "For teams under eight people, probably not. For anything larger, or any project that had significant conflict during development, yes. An internal producer from outside the project works fine. An external facilitator (some consultants run these for $800-$2,500 depending on team size) is worth it if interpersonal dynamics are particularly charged."
  - q: "What happens if leadership ignores the action items?"
    a: "Then the post mortem was theater, and your team knows it. This is the most common failure mode I see, and it does real damage to trust. If there's organizational resistance to acting on findings, the producer's job is to get explicit, on-record acknowledgment of which items will and won't be addressed and why. Silence is the worst outcome."
---

Most teams skip the [post mortem](/posts/game-studio-post-mortem-process-that-actually-works/) entirely. They ship the game, collapse for two weeks, and then immediately get pulled into the next project pitch before anyone has processed what actually happened. I've watched this cycle repeat at three different studios, and I'll be honest: it's one of the most expensive mistakes you can make in this industry, because you're essentially agreeing to repeat every mistake you just survived.

The post mortem is one of those things that sounds administrative until you've done one that actually worked. Then you realize it's less about documentation and more about collective sense-making. You're trying to figure out what was real versus what just felt true in the moment.


<div class="kt" style="margin:26px 0;padding:18px 22px;border:1px solid var(--border,#e7e5e4);border-left:4px solid var(--accent,#4338ca);border-radius:12px;background:var(--surface2,#f8fafc)"><div style="font-size:.72rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--accent,#4338ca);margin-bottom:8px">Key takeaways</div><ul style="margin:0;padding-left:1.15em"><li style="margin:5px 0">Run the post mortem within 3-4 weeks of ship, before memory degrades and people disperse to new projects.</li><li style="margin:5px 0">Separate the "what happened" data gathering from the "why it happened" discussion, conflating them kills honesty.</li><li style="margin:5px 0">Anonymous pre-surveys surface problems that almost never get spoken aloud in group settings.</li><li style="margin:5px 0">Written post mortems published publicly (like on Gamasutra/Game Developer) generate recruiting and credibility returns that justify the time.</li><li style="margin:5px 0">The single most common post mortem failure is generating a great document and then never referencing it again.</li></ul></div>


## Before You Even Schedule the Meeting

The instinct is to call everyone into a room and start talking. Resist it. The most valuable thing I learned from running about eleven of these across different team sizes is that the in-room conversation is almost always dominated by whoever talks loudest and whoever is most comfortable with conflict. Which means you get the official story, not the real one.

What [actually works](/posts/agile-game-development-what-actually-works-in-practice/): send an anonymous pre-survey about ten days before any group discussion. I've used Google Forms for this on smaller teams and SurveyMonkey on larger ones. Ask specific questions, not vague ones. "What was the single biggest process failure on this project?" gets you real answers. "How do you feel the project went overall?" gets you noise.

One thing that only becomes obvious after you've done a few of these: ask people to rate their own performance honestly, separately from the team's performance. The gap between those two numbers tells you something important about accountability culture on your team. If everyone rates themselves a 7/10 and the project a 4/10, you have a diffusion of responsibility problem that no meeting is going to surface on its own.

## The Actual Structure That Works

I'll be honest, the classic "what went well / what went wrong" format is fine for small indie teams and basically useless for anything over fifteen people. It produces a list of grievances masquerading as analysis. Here's what I've settled on after enough failed [post mortems](/posts/lessons-from-20-years-of-gdc-post-mortems/) to be embarrassed about:

**Phase 1: Data before opinions.** Pull the actual numbers first. Schedule adherence (what percentage of milestones hit on time), bug counts by sprint, crunch hours logged, scope changes by quarter, QA pass rates. You want a factual spine before you let people start interpreting. What surprised me on a 22-person project a few years back was that the team universally felt like scope had ballooned in the last four months, but the data showed the real scope creep had happened in month three. The emotional experience of a project often lags the actual events by weeks.

**Phase 2: Individual written submissions.** Before anyone talks in a group, everyone writes down their three biggest "what went wrong" and three biggest "what went well" items. Written, not spoken. This takes the air out of the loudest-voice problem. Collect these, synthesize them into themes, and present those themes anonymously to the group.

**Phase 3: Facilitated group discussion.** Now you can have the conversation, but you're starting from synthesized data rather than competing individual narratives. The facilitator's only job is to push past the "what" to the "why." If the team agrees that vertical slice delivery was late, that's the what. The why is usually one of three things: unclear ownership, underestimated technical complexity, or a leadership decision that nobody felt safe pushing back on. You want the why.

**Phase 4: Prioritized action items, not a wish list.** The output of the post mortem should be a ranked list of process changes with clear owners and deadlines, not a twelve-page document of observations. I've seen that twelve-page document written beautifully and then opened exactly once, six months later, when someone was making a slide deck.

## What the Timeline Actually Looks Like

Post mortem timing matters more than most producers think. Too soon (first week after ship) and people are still in fight-or-flight mode. Too late (two months out) and memory has softened, people have moved on emotionally, and the institutional knowledge has already started to evaporate.

| Phase | Timing After Ship | Duration | Format |
|---|---|---|---|
| Anonymous pre-survey | Days 10-14 | 20-30 min per respondent | Async, written |
| Data audit (producer-led) | Days 12-16 | 4-8 hrs total | Quantitative pull |
| Survey synthesis | Days 16-18 | 2-3 hrs | Thematic clustering |
| Department-level discussions | Days 18-22 | 60-90 min per dept | Small group, facilitated |
| Full team session | Days 22-28 | 2-3 hrs | Facilitated, themes only |
| Written report draft | Days 28-35 | Producer, 4-6 hrs | Internal document |
| Action item review | Day 42 | 30 min | Confirmation meeting |

That 42-day checkpoint is the one teams skip. It's the difference between a post mortem and a post mortem that actually changes something.

## The Hard Conversation Nobody Wants to Have

Leadership. Specifically, how the producer or director's decisions contributed to the problems the team is describing.

I've been in the room when a well-meaning post mortem turned into a thinly veiled grievance session aimed at one lead, and I've also watched a director sit through an entire post mortem nodding thoughtfully while the team listed failures that were clearly rooted in her decision-making, and nobody said it directly. Both of those are failures of psychological safety, but in opposite directions.

The way I've handled this: the producer running the post mortem should not be the same person being evaluated. If you were the project lead, get someone neutral to facilitate. Even if it's a producer from another team or an outside contractor. The cost is low (a day of someone's time) and the quality of honesty you get in the room goes up dramatically.

Scenario from my own experience: a team I was embedded with did a post mortem where the lead producer ran the session herself. Everyone praised her communication. Three months later I was doing exit interviews and two people who'd left cited her communication as their primary reason for leaving. The post mortem had measured nothing real.

## Publishing Your Post Mortem

Game Developer Magazine (formerly Gamasutra) has been publishing post mortems since 1997. A good chunk of the industry knowledge base is actually sitting in those public post mortems, and I'd argue they're underused as training material. As of July 2026, the Game Developer site archives go back decades and are still searchable.

Publishing your post mortem publicly is a choice that scares a lot of studios, and I get it. You're airing your failures. But what I've seen happen in practice: the studios that publish honest, specific post mortems get better job applicants, better press relationships, and more trust from their communities than the ones that only ever talk about what went right. Specificity is the thing. "We underestimated UI iteration by 340 hours due to unclear sign-off ownership" is more valuable to the reader, and more credibility-building for you, than "scope management was difficult."

Worked example: a small studio published a detailed post mortem for their 2019 release acknowledging a 9-month crunch and the structural decisions behind it. Within six weeks, two senior developers reached out about joining specifically because the honesty signaled a culture willing to examine itself. The next project ran with explicit crunch-prevention mechanisms in the production plan, named directly from that post mortem. Scope overruns dropped by roughly 40% on the follow-up title.

## Sources

- [Game Developer Magazine Post Mortem Archive](https://www.gamedeveloper.com/tag/postmortem): Decades of published post mortems across genres and team sizes, invaluable primary source for real studio data.
- Schell, Jesse. *The Art of Game Design* (3rd ed., 2019): Chapter-level treatment of production reflection and iterative design evaluation.
- [International Game Developers Association Developer Satisfaction Survey](https://igda.org/resources-archive/developer-satisfaction-survey-2023/): Annual survey data on crunch, project outcomes, and team health indicators.
- Fullerton, Tracy. *Game Design Workshop* (4th ed., 2018): Covers playtesting and retrospective documentation as formal production practice.
- Humphrey, Watts S. *Introduction to the Team Software Process* (2000): The root source for a lot of modern post mortem methodology; still worth reading for the structured retrospective framework.

---


*Photo: [Ivan S](https://www.pexels.com/@ivan-s) via Pexels*