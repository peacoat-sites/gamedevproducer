---
title: "What 20 Years of Game Postmortems Reveal: The Research, Summarized"
date: 2026-05-21T22:45:08.395370+00:00
lastmod: 2026-10-06
draft: false
description: "What researchers found when they analyzed hundreds of published game postmortems from 1997 to 2019: the most common problems, what went right, how problems changed over time, and what producers should do about it."
image: "/img/heroes/3321791.jpg"
categories: ["industry intel"]
tags: ["lessons", "from", "years", "post-mortems"]
author: "Stephen Brenish"
author_bio: "Stephen Brenish is a Lead Game Producer at Epic Games (Fortnite, Unreal Engine) and founder of GameDevProducer, with 14+ years shipping and running live games at scale (previously Senior Program Manager at Blizzard Entertainment). Certified ScrumMaster."
slug: "lessons-from-20-years-of-gdc-post-mortems"
affiliate_disclosure: true
author_slug: "stephen-brenish"
author_title: "Lead Game Producer"
faqs:
  - q: "What is the most common problem in game development postmortems?"
    a: "It depends on how researchers group them, but the same themes recur. An analysis of 200 postmortems from 1997 to 2019 found insufficient workforce and team environment problems the most common root causes, followed by wrong marketing strategy and underestimation. An earlier study of 155 postmortems found obstacles, schedule, development process and game design the most frequent things that went wrong."
  - q: "Are game development problems mostly technical?"
    a: "No. Researchers have found repeatedly that most root causes are about people, planning and management rather than technology. In the largest study, technical and game design problems declined over the years, while team and marketing problems grew."
  - q: "Do postmortems still mention crunch?"
    a: "Less than they used to. One study of 78 postmortems found crunch mentioned in 45% of them, and the 200-postmortem study saw mentions fall after 2015. Postmortems are written for publication, though, so a decline in mentions is not proof that crunch itself declined."
  - q: "How should a producer use postmortem research?"
    a: "Turn the most common failure modes into early checks on your own project: staffing against the plan, estimates against actuals, a written vision everyone can repeat, a marketing plan with an owner, and a prototype that proves the game is fun before full production."
---

For more than two decades, developers have published postmortems of their games: honest accounts of what went right and what went wrong, first in Game Developer magazine and then on Gamasutra, now Game Developer. Taken together, they are the closest thing the industry has to a public database of how projects succeed and fail.

Researchers have analyzed that database systematically. This is a summary of what they found, and what it means for anyone running production.

## The studies

| Study | Postmortems analyzed | What it looked at |
|---|---|---|
| Petrillo, Pimenta, Trindade and Dietrich, 2009 | 20 | Recurring problems, compared with traditional software projects |
| Washburn, Sathiyanarayanan, Nagappan, Zimmermann and Bird, 2016 | 155 | What went right and what went wrong, by category and team size |
| Edholm, Lidström, Steghöfer and Burden, 2017 | 78, plus interviews at four studios | Crunch: how common it is and why it happens |
| Politowski, Petrillo, Ullmann and Guéhéneuc, 2021 | 200, from 1997 to 2019 | 927 problems in 20 types, their root causes and how they changed over time |

The postmortems in these studies came mainly from Gamasutra, so they skew toward games that shipped and developers willing to write about them. Keep that in mind; the findings are still remarkably consistent.

## The problems are mostly about people, not technology

The earliest study, of 20 postmortems, concluded that game development suffers mostly from management problems rather than technical ones, and that the most common were scope that was unrealistic or too ambitious, feature creep, and cutting features. Twelve years and 200 postmortems later, the largest study reached a similar conclusion: most root causes were related to people, not technologies.

Here are the ten most common root causes in that 200-postmortem study:

| Root cause | Problem type | Times found |
|---|---|---|
| Insufficient workforce | Team | 49 |
| Environment problems (organization, pay, culture) | Team | 48 |
| Wrong marketing strategy | Marketing | 35 |
| Underestimation | Planning | 34 |
| Unclear game design vision | Game design | 28 |
| Lack of fun | Game design | 27 |
| Platform and technology constraints | Technical | 24 |
| Game design complexity | Game design | 23 |
| Inadequate or missing tools | Tools | 22 |
| Misaligned teams | Communication | 22 |

Only one of the ten is primarily technical. Insufficient workforce, the most common, usually came down to budget, weak planning or the difficulty of hiring the right skills: too few people for the work, or one person carrying too many roles.

## What went wrong, and what went right

The 155-postmortem study counted how often each category appeared in the "what went wrong" and "what went right" sections.

| Most common in "what went wrong" | Share of postmortems | Most common in "what went right" | Share of postmortems |
|---|---|---|---|
| Obstacles | 37% | Game design | 50% |
| Schedule | 25% | Development process | 43% |
| Development process | 24% | Team | 40% |
| Game design | 22% | Art | 39% |

The details behind those numbers are where the lessons are:

- **Obstacles** often came from newly formed teams that did not yet work well together. Half of small teams listed obstacles as something that went wrong, against about a quarter of large teams.
- **Schedule** problems came from estimation and optimistic scheduling, and from design changes late in development.
- **Development process** went wrong most often when teams started production without enough planning, and in at least one case because nobody was dedicated to project management and the lead programmer carried it on top of everything else.
- **Game design** failures were usually over-ambition: features that each looked doable but added up to far more work than the schedule held.

The "went right" side is the mirror image. Teams that praised their process had planned before production, built prototypes as proof of concept, often grew those prototypes into the game, and iterated. Teams that praised their design talked about a clear vision and a strong hook.

## What changed over two decades

The 200-postmortem study tracked problem types from 1997 to 2019:

- Management problems declined over the years, while business problems grew.
- Production problems stayed constant.
- Technical and game design problems declined, design problems only in the last decade.
- Team problems increased in the last decade.
- Marketing problems grew more than any other type, as games moved from magazines to forums, social media, storefronts and streamers, and as the market saturated.
- Feature creep became less common over time.

On crunch, the 78-postmortem study found it mentioned in 45% of postmortems, and more often at small studios (54%) than at micro (33%) or medium-sized ones (36%). In the 200-postmortem study, mentions of crunch fell after 2015. Postmortems are written for publication, so fewer mentions may reflect what developers are willing to write as much as what happened.

## What producers should take from this

Each of the most common failure modes maps to a check you can run on your own project, early:

1. **Staff to the plan, not the hope.** If the plan needs more people than you have, the plan is wrong. Insufficient workforce is the single most common root cause.
2. **Estimate from the bottom up, and compare with actuals.** Underestimation and optimistic schedules show up in every study. Hold explicit buffer before major gates; see [buffer time in game schedules](/posts/buffer-time-in-game-schedules-why-it-matters/).
3. **Write the vision down early.** Unclear vision and misaligned teams are both top-ten causes. If team members carry different pictures of the game, you will find out during production, at the most expensive moment.
4. **Treat marketing as production work.** It is the fastest-growing problem type. Give it an owner, a plan and milestones, not leftover time at the end. [Marketing an indie game on a budget](/posts/how-to-market-an-indie-game-on-a-budget/) covers where to start.
5. **Prove the fun before full production.** Lack of fun is a top-ten cause, and prototyping is a top reason process went right.
6. **Give new teams extra risk management.** Small and newly formed teams report obstacles far more often. Keep a [risk register](/posts/risk-register-template-for-game-development/) and review it on a schedule.
7. **Budget for tools.** Inadequate or missing tools appear in the top ten, and they are usually cheaper to fix than the time they waste.

For the practitioner view of the same patterns, see [why game projects fail](/posts/what-game-post-mortems-reveal-about-production-failures/), and to run a useful postmortem on your own project, see [a game studio postmortem process that works](/posts/game-studio-post-mortem-process-that-actually-works/).

## Sources

- Fábio Petrillo, Marcelo Pimenta, Francisco Trindade and Carlos Dietrich, ["What went wrong? A survey of problems in game development"](https://doi.org/10.1145/1486508.1486521), *Computers in Entertainment*, 2009.
- Michael Washburn, Pavithra Sathiyanarayanan, Meiyappan Nagappan, Thomas Zimmermann and Christian Bird, ["What went right and what went wrong: an analysis of 155 postmortems from game development"](https://swag.uwaterloo.ca/publications/what-went-right-and-what-went-wrong-an-analysis-of-155-postmortems-from-game-development.html), ICSE 2016.
- Edholm, Lidström, Steghöfer and Burden, "Crunch time: The reasons and effects of unpaid overtime in the games industry", ICSE 2017, as summarized by Politowski et al.
- Cristiano Politowski, Fabio Petrillo, Gabriel C. Ullmann and Yann-Gaël Guéhéneuc, ["Game industry problems: An extensive analysis of the gray literature"](https://arxiv.org/abs/2009.02440), *Information and Software Technology*, 2021.
