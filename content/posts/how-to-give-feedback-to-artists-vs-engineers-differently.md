---
title: "How To Give Feedback To Artists Vs Engineers Differently"
date: 2026-05-26T02:56:40.422288+00:00
draft: false
description: "Learn how to tailor feedback for artists and engineers effectively. Discover key communication differences to inspire creativity and drive technical precision i"
image: "https://images.pexels.com/photos/7915392/pexels-photo-7915392.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
categories: ["team psychology"]
tags: ["give", "feedback", "artists", "engineers", "differently"]
author: "Claire Novak"
author_bio: "Former financial advisor and certified paralegal who left the industry tired of jargon and upsells. Now writes plain-English breakdowns of the things professionals tend to overcomplicate. No padding, no hedging, no hand-holding."
slug: "how-to-give-feedback-to-artists-vs-engineers-differently"
affiliate_disclosure: true
---

You're in a sprint review. The combat animator shows a sword slash that reads slow and telegraphed. You say, "The timing feels off, can you punch it up?" She nods. Two days later, you see the revision and it's faster, snappier, and somehow worse. Meanwhile, across the room, you told your lead engineer the collision detection "felt a bit janky" and he came back with three questions, a spreadsheet of frame data, and a fix that worked perfectly. Same vague feedback. Completely opposite outcomes. That's not a coincidence.

Giving feedback is a core producer skill, and most coverage treats it like a personality quiz: are you a "sandwich method" person or a "radical candor" person? That framing misses the actual problem. Artists and engineers process feedback differently because they're working in different cognitive modes, and if you don't understand that, you'll keep getting revisions that miss the point.

## Why the Difference Exists in the First Place

Engineers operate in a world of defined states. Code either compiles or it doesn't. A bug is reproducible or it isn't. When you give an engineer a problem, they're trained to decompose it into discrete causes and testable solutions. Ambiguity is an obstacle. They'll either ask clarifying questions until the problem is specific enough to solve, or they'll make an assumption and build toward it.

Artists operate in a world of continuous refinement. A character model isn't done or not done, it exists somewhere on a spectrum from rough to final. Iteration is the process, not a symptom of failure. When you give an artist feedback, they're already in an interpretive mode, reading intent, feeling out direction, weighing options. Vague direction doesn't frustrate them the same way. But imprecise direction can send them down the wrong path entirely, because they'll fill your gaps with their own creative judgment, which may or may not match yours.

Neither mode is better. Both create problems when you apply the wrong feedback approach to the wrong discipline.

## How to Give Feedback to Artists

Start with intent, not prescription. The fastest way to kill a good artist's output is to tell them exactly what to do. "Make the sword swing faster" is a direction. "The player needs to feel the impact before they see it, right now the anticipation is eating up the window where they should feel the hit land" is intent. One of those unlocks the artist's skill. The other makes you the artist and them the executor.

Reference before you describe. Words like "punchy," "gritty," "clean," or "vibrant" mean different things to different people. When you're reviewing work, bring visual references whenever possible. This isn't because artists can't handle abstract language, it's because a single reference image eliminates a paragraph of miscommunication. Tools like [PureRef](https://www.pureref.com/) are free and purpose-built for building reference boards in exactly these conversations.

Separate what's working from what isn't. Artists are invested in their work in a way that's both their greatest strength and their greatest vulnerability to feedback. If you walk in and list five things that are wrong, they hear "this is bad." Start by naming what's landing: "The color palette is exactly right, the weight on the idle animation feels real." Then redirect: "The issue is the transition into the attack, it doesn't match the weight you've established." Now you're calibrating, not criticizing.

Protect creative ownership. If a piece needs significant changes, ask what the artist thinks before you give your read. Often they already know. "What do you feel is working and what's still unresolved?" surfaces their own critique first, which makes your feedback collaborative rather than corrective.

## How to Give Feedback to Engineers

Be specific about the observable problem, not the perceived cause. "The pathfinding is broken" is almost useless. "NPCs are clipping through the door frame on level 3 when the player approaches from the south side, reproducible every time" is actionable. Engineers need a clear problem statement. The more precisely you describe what you observed, the faster they can work.

Don't suggest the solution unless you're asked. This is where producers get into trouble. You might have an instinct that a certain system needs to be rebuilt from scratch, or that a different plugin would solve the problem. Maybe you're right. But engineers will rightly push back if you're prescribing solutions without understanding the codebase. Your job is to own the problem statement and the acceptance criteria. Their job is to own the solution. Respect that boundary and you'll get better results and a healthier working relationship.

Frame feedback in terms of player experience, not technical preference. "Can you optimize this?" is a bad ask. "Load times on the main menu are running 8 to 12 seconds in our current build. Target is under 4. What's causing it and what are our options?" is a real producer conversation. Engineers respond well to clearly scoped problems with defined success metrics.

## A Side-by-Side Comparison

| Situation | Feedback to an Artist | Feedback to an Engineer |
|---|---|---|
| Something feels wrong | "Here's the experience I want the player to have" | "Here's the specific behavior I observed and when" |
| Work misses the mark | Name what's working, then redirect | Define the gap between current state and acceptance criteria |
| You have a solution in mind | Offer it as a reference or example, not a mandate | Ask if they've considered it, then let them evaluate |
| Timing is tight | Prioritize the one change with the most impact | Give them the constraint first, ask what's feasible |
| You don't have the vocabulary | Use references, videos, or comparisons | Ask them to explain current behavior before giving notes |

## What to Do When Feedback Goes Sideways

Revisions that miss the point are almost always a communication failure on the producer's end, not a comprehension failure on the artist's or engineer's end. Before you escalate or repeat yourself louder, ask: did I give them the problem or did I give them my solution? Did I describe what I wanted to feel or what I wanted to see?

For artists, when a revision still misses: get in a room together. Stop using written feedback for anything that requires tone, feel, or direction. Ten minutes of real-time conversation with a reference image will outperform three rounds of written notes every time.

For engineers, when a fix introduces new issues: ask them to walk you through their approach before you review the output. Understanding their logic tells you where the gap is. Sometimes the spec was underspecified. Sometimes the fix is technically correct but the acceptance criteria didn't account for an edge case. Find that out before you call the ticket incomplete.

I've seen teams burn entire sprint cycles because a producer kept resubmitting the same vague feedback in slightly different words. Be the one who breaks that loop.

## Tools That Help You Give Better Feedback

Good feedback starts with clear tracking. [Jira](https://www.atlassian.com/software/jira) and [Shortcut](https://www.shortcut.com/) both let you structure bug reports and task notes in ways that force specificity. [Notion](https://www.notion.so/) works well for maintaining living feedback documents tied to art briefs.

For visual feedback on art assets, [Loom](https://www.loom.com/) lets you record screen walkthroughs with voiceover, which is dramatically better than typed notes for anything animation or UI-related. [Frame.io](https://frame.io/) handles frame-accurate video review and is worth the cost if you're doing any significant cinematic or animation work.

On the production knowledge side, *The Art of Game Design* by Jesse Schell sharpens your ability to articulate player experience, which is the foundation of useful creative feedback. For managing technical communication, *Peopleware* by DeMarco and Lister is still one of the most honest books about how technical teams actually work.

---

## FAQ

### Does this mean I need to be a psychologist to manage a mixed team?

No. It means you need to understand that different disciplines have different success criteria. Artists measure success by qualitative impact. Engineers measure success by defined outcomes. Your feedback needs to speak to what success looks like in their frame of reference. That's not psychology, it's communication discipline.

### What if an artist keeps asking for prescriptive direction? Some people want to be told exactly what to do.

Some do, especially junior team members who are still building confidence in their own judgment. In that case, give more directive notes, but pair them with the reasoning. "Make the idle animation loop at 1.2 seconds rather than 2" lands better when followed by "because it'll feel more alive during the long exploration sections." Direction plus context builds their calibration over time, so you're not just getting the right output, you're developing someone who can self-direct.

### How do I give feedback when I genuinely don't understand the technical side well enough?

Own that gap out loud. "I don't have the technical context to know what's causing this" is not a weakness, it's an accurate problem statement. Then describe what you observed: when it happens, under what conditions, what the player experience is. Engineers don't need you to understand the cause. They need you to define the problem and the acceptance criteria.

### What's the biggest mistake producers make when giving feedback to artists?

Giving notes on craft when the issue is actually direction. If you're telling an animator how to time a swing, but the real problem is that the whole combat system's pacing is off, you're solving the wrong level of the problem. Separate creative direction feedback (what should this feel like, what is it for) from craft feedback (is this technically well executed). The first is your job. The second often isn't.

### How do you handle it when an engineer thinks your feedback is outside scope?

Take it seriously. Engineers have context on technical debt, system architecture, and downstream consequences that you likely don't have full visibility into. Ask them to explain the constraint. If the scope objection is valid, reprioritize. If it's not, make the business case clearly: "I understand this is a change, here's why it's a P1 from a player experience standpoint, what do you need from me to make it feasible?" Acknowledging their concern before asserting the priority gets you a lot further than overriding it.

---

The underlying principle here isn't complicated: good feedback meets people where they actually are, not where you assume they are. Artists need to understand the experience you're trying to create. Engineers need to understand the problem you need solved. Get that distinction right, and your revision cycles get shorter, your team gets less frustrated, and you start shipping things that actually match the vision you had in your head.

*Photo: [RDNE Stock project](https://www.pexels.com/@rdne) via Pexels*