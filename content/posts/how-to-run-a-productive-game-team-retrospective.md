---
title: "How To Run A Productive Game Team Retrospective"
date: 2026-06-30T11:26:56.621488+00:00
draft: false
description: "Learn how to run a productive game team retrospective that boosts collaboration, surfaces blockers, and helps your team ship better games faster."
image: "/img/heroes/15543117.jpg"
categories: ["team management"]
tags: ["productive", "game", "team", "retrospective"]
author: "Priya Sharma"
author_slug: "priya-sharma"
author_title: "Design & Narrative Editor"
author_bio: "Priya Sharma is a game designer with a particular focus on systems that create engaging games, covering everything from core loop design to narrative structure. She has worked on titles across multiple genres and believes that good design is invisible to the player. At GameDevProducer, she covers game design principles, narrative mechanics, player psychology, and the craft of building experiences that keep people playing."
slug: "how-to-run-a-productive-game-team-retrospective"
affiliate_disclosure: true
faqs:
 - q: "How long should a retrospective be?"
   a: "For a two-week sprint, fifty minutes is the practical ceiling. Longer sessions produce diminishing returns on action item quality and tank engagement. If your retros consistently run over an hour, the format has too many steps or the discussion is going unmoderated."
 - q: "What if the same problems keep coming up every sprint?"
   a: "That's usually a sign you're treating symptoms rather than causes. If 'communication is slow' appears three sprints in a row, the root cause is probably structural (the team's async setup, unclear ownership, missing tools) and needs a dedicated session or producer intervention, not another retro card."
 - q: "How many action items should a retrospective produce?"
   a: "Three is the hard cap I'd defend. One well-executed action item is worth more than six abandoned ones. If you're routinely producing more than three and completing them all, your team is an outlier, and even then, I'd ask whether the items are ambitious enough."
 - q: "Should the producer or team lead facilitate their own team's retro?"
   a: "It's workable, but there's a real tension: the producer often has opinions about what should change, which can steer the discussion. Rotating facilitation among senior team members, or having a peer producer from another team facilitate quarterly, removes that bias. I've done both, and external facilitation produces noticeably more candid outputs."
 - q: "What's the best retrospective tool for remote teams?"
   a: "As of June 2026, EasyRetro and Miro remain the most practical options for distributed game teams. EasyRetro is simpler and faster to set up for async card input. Miro is better if you need flexible formats or want to integrate retro boards with other project documentation. FigJam works if your team already lives in Figma. The tool choice matters far less than whether action items end up in the same system your team uses for actual work."
lastmod: 2026-07-07
---

Most retrospective advice focuses on the wrong problem. It treats the retro as a morale exercise, a place to vent, then move on. The actual job is to produce a short list of changes your team will actually make before the next sprint. Everything else is optional.

I've sat through probably 300 retros at this point, first at a studio outside Montreal running 80-person projects, then with tiny indie teams shipping on budgets that would barely cover a AAA cinematic. The failure mode is almost always the same: great conversation, zero follow-through, same issues surface again two weeks later. You haven't run a retrospective. You've run a support group.

Here's how to fix that.

---

## The Setup Nobody Talks About

The facilitator role gets underestimated every time. Most teams rotate facilitation casually, like it's a chore to share. That's fine in theory, but whoever facilitates needs to do one thing the night before: read the previous retro's action items and check which ones actually happened.

Not to shame anyone. To frame the opening.

If you walk in and say "last sprint we committed to daily build smoke tests; three of four happened, one was blocked by infrastructure access, let's note that and move on," you've done two things at once. You've shown the team their commitments matter, and you've implicitly set the bar: this retro will also produce commitments that matter.

Do this without that check-in and you're starting fresh every two weeks. You're not iterating. You're spinning.

Room setup: async or remote teams should use a dedicated board tool. Miro works, EasyRetro works. FigJam is decent if your team is already in Figma all day. I've used all three, and honestly the tool is the least important variable, what kills async retros is giving people too little time to add their cards before the session starts. Thirty minutes is too short. Overnight async input, then synchronous discussion, is the format that actually works.

---

## The Format Question (And How Most Teams Choose Wrong)

| Retrospective Format | Best Used When | Key Focus |
| --- | --- | --- |
| Start-Stop-Continue | Default format, general sprints | Action-oriented; forces deletion decisions |
| Glad-Sad-Mad | After shipping or crunch periods | Emotional processing before analysis |
| Sailboat | Project losing direction | Structural shifts; not just velocity loss |
| Custom Format | Based on team-flagged thorny issues | Addresses specific recurring problems |

There are maybe a dozen named retrospective formats. Start-Stop-Continue. Four Ls. Sailboat. Glad-Sad-Mad. Most teams pick one, use it every sprint forever, and wonder why engagement drops around month three.

The answer isn't to find the perfect format. It's to rotate them with a purpose.

Start-Stop-Continue is the best default because it's action-oriented by construction. "What should we stop doing?" forces deletion, which is rare and valuable. Glad-Sad-Mad is better when the team has just shipped something hard and emotions need naming before you can do any analysis. Sailboat (winds, anchors, rocks, destination) is specifically useful when a project is losing direction, not when it's just lost velocity.

Choosing a format based on the team's current emotional state isn't soft management. It's efficient. A team that needed to vent and didn't gets worse outputs from a process-analysis retro.

My general rotation for a six-week cycle: Start-Stop-Continue for sprints 1 and 3, Sailboat for sprint 2 if anything structural has shifted, Glad-Sad-Mad after any milestone or crunch period. Sprint 4 I'll sometimes do a completely custom format based on whatever the team flagged as thorny at the last one.

---

## Running the Session Itself

Fifty minutes is the right length for a two-week sprint retro. Not an hour. Fifty minutes. The ten-minute buffer forces you to end with a clear list, because you know you can't push to sixty.

Structure that fifty minutes like this:

Set the stage: five minutes. One word or one sentence from each person about how the sprint felt. No discussion. Just temperature check.

Gather data: fifteen minutes. Everyone adds cards to the board in silence. Separate columns for what went well, what didn't, what was confusing or unclear. Silent writing prevents anchoring, nobody adjusts their card because they saw someone else's first.

Generate insights: twenty minutes. Group the cards, vote on themes (two or three dots per person in tools like Miro), then discuss only the top-voted clusters. This is where the facilitator earns their keep: keep discussion specific ("the build was broken for six hours on Tuesday" beats "the build is always a problem"), cut tangents that are really complaints about a different problem, and name the underlying cause rather than the symptom.

Decide what to do: ten minutes. Maximum three action items. Hard cap. Each one needs an owner, not a team ("the team will improve documentation" is a commitment no one owns). Each one needs a rough definition of done.

Close: five minutes. Final temperature check and facilitator notes action items in whatever your team uses. I like Linear or Notion for this, not a separate retro tool, because the action items need to live where the team actually works, not in a board they'll never open again.

---

## The Action Item Problem (Where Most Retros Die)

Three action items, maximum. This is the rule I enforce hardest and get the most pushback on.

The argument against it: "we identified eight real problems, ignoring five of them seems wasteful." The counter: a retro that produces eight commitments and follows through on two is worse than a retro that produces three and completes all three. Attention is finite. You're also building a habit of completion, and that habit compounds.

Here's a worked example. An indie team I consulted with in early 2025 was averaging nine action items per retro, completing maybe two. Same issues kept surfacing, frustration was building, people stopped believing the retro did anything useful. We hard-capped at three for six consecutive sprints. Completion rate went from roughly 22% to 83%. Recurring issues dropped from an average of seven per retro to three. The team described their sprints as "actually getting better" for the first time in six months.

That's not a coincidence. Fewer commitments meant real accountability.

Each action item should pass what I call the "Monday morning test." Can the owner describe exactly what they'll do Monday morning to start this? If they're vague, the action item isn't defined tightly enough yet.

---

## When the Team Is Broken (Not Just Frustrated)

Most retro guides skip this part. There's a meaningful difference between a team that's frustrated with process and a team with unresolved interpersonal conflict. A standard retrospective makes the second case worse. You're putting people in a structured venting session when what they actually need is a direct conversation about the relationship fracture.

Signs you have an interpersonal problem, not a process problem: the same person's name keeps appearing in cards without anyone saying it out loud, silences that feel loaded rather than thoughtful, passive-aggressive card phrasing ("some people don't update the task board").

When I've seen this, the right move is to pause the standard retro format and have a direct conversation, sometimes with the producer mediating one-on-one first. Trying to run a Sailboat exercise over a team that's quietly furious at each other produces useless data and deeper resentment.

Liane Davey's book *The Good Fight* has the clearest framework I've read for distinguishing productive conflict from dysfunctional avoidance in teams. If your retros feel consistently low-energy despite positive surface responses, that's worth reading before your next session.

---

## A Few Quick Contrarian Points

Everyone says psychological safety is a prerequisite for a good retro. I'd say it's a goal, not a prerequisite. You build safety through how you run retros over time, not by declaring a safe space and expecting it to work immediately.

Anonymous cards help with new teams or teams with seniority imbalances. For mature teams, they often mask the accountability piece, if nobody knows who flagged an issue, nobody owns following up on it either.

And the async-versus-synchronous debate: the synthesis and decision phase needs to be synchronous. Everything else can flex. Async card input is actually better for quality, because people have time to think rather than respond to social pressure in the room. But voting, discussion, and action item commitment need shared presence.

---

## Sources

- Esther Derby & Diana Larsen, *Agile Retrospectives: Making Good Teams Great* (2006): The foundational text on retrospective structure, still the most cited resource in the field.
- Liane Davey, *The Good Fight* (2019): Practical framework for distinguishing healthy team conflict from avoidance behaviors, directly applicable to retro facilitation.
- State of Agile Report, Digital.ai (current as of 2026): Annual industry survey tracking agile adoption and retrospective practices across software and game development teams.
- Accelerate: The Science of Lean Software and DevOps, Forsgren, Humble & Kim (2018): Research-backed data on team iteration practices and their relationship to delivery outcomes, including retrospective frequency.

---


*Photo: [Walls.io](https://www.pexels.com/@walls-io-440716388) via Pexels*