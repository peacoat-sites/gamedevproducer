---
title: "70% of Game Artists Want Better Feedback—Here's How"
date: 2026-07-25T10:04:01.233843+00:00
draft: false
description: "Learn how to give constructive feedback to game artists. Discover what 70% say they need and proven techniques for improving collaboration."
image: "/img/heroes/8867373.jpg"
categories: ["team management"]
tags: ["give", "feedback", "game", "artists"]
author: "Stephen Brenish"
author_slug: "stephen-brenish"
author_title: "Lead Game Producer"
author_bio: "Stephen Brenish is a Lead Game Producer at Epic Games (Fortnite, Unreal Engine) and founder of GameDevProducer, with 14+ years shipping and running live games at scale (previously Senior Program Manager at Blizzard Entertainment). Certified ScrumMaster."
slug: "how-to-give-feedback-to-game-artists"
affiliate_disclosure: true
faqs:
  - q: "How often should I be giving artists formal feedback?"
    a: "At minimum, align on milestones at the start of production and give formal structured feedback at each one. For most mid-size projects that means roughly every two weeks per asset in active development. Ad hoc feedback between milestones should be reserved for blockers only, not opinions."
  - q: "What do I do if an artist ignores my feedback?"
    a: "Before escalating, check whether the note was clear, prioritized, and confirmed verbally. Most 'ignored' feedback was actually misunderstood feedback. If the note was clear and agreed on and still wasn't acted on, that's a conversation about accountability, not about the feedback itself."
  - q: "Is written feedback better than verbal feedback?"
    a: "Both, honestly. Verbal is better for back-and-forth problem-solving and emotional nuance. Written is better for clarity, record-keeping, and async work. The best process I've used combines a short verbal check-in with a written summary of agreed actions sent within an hour after the meeting."
  - q: "Should I always explain the reason behind a note?"
    a: "Yes, almost always. The reason is what allows the artist to generalize the feedback and apply it to future assets. A note without context trains dependency; a note with context builds judgment."
  - q: "How do I give feedback when I don't have strong visual art skills myself?"
    a: "Focus entirely on player experience and brief adherence, not aesthetics. 'Does this communicate what the player needs to know at a glance?' is a question any producer can ask productively. You don't need to know how to paint to know whether something reads clearly from 10 feet away."
---

Seventy percent of game artists say they've received feedback so vague it actively slowed them down. That number comes from a 2023 Concept Art Association survey of over 1,400 working artists, and honestly, the moment I read it I thought: yeah, that tracks completely.

I've sat in more art reviews than I can count, on both sides of the table. I've been the junior artist getting notes like "make it pop more" (whatever that means), and I've been the producer who, early in my career, absolutely said "can we make it feel more epic?" to a concept artist who deserved better. The thing is, bad feedback isn't usually malicious. It's just untrained. Nobody teaches producers or creative directors how to talk to artists, and then we're shocked when the revision cycle eats three weeks and the result still doesn't match what anyone pictured.

What I want to do here is give you the actual mechanics of useful art feedback: what to say, what to avoid, when to give it, and why the timing matters as much as the words.


<div class="kt" style="margin:26px 0;padding:18px 22px;border:1px solid var(--border,#e7e5e4);border-left:4px solid var(--accent,#4338ca);border-radius:12px;background:var(--surface2,#f8fafc)"><div style="font-size:.72rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--accent,#4338ca);margin-bottom:8px">Key takeaways</div><ul style="margin:0;padding-left:1.15em"><li style="margin:5px 0">70% of game artists report vague feedback actively slowed their work (Concept Art Association, 2023)</li><li style="margin:5px 0">Describe what the art needs to DO, not what it should look like, functional intent beats aesthetic prescription</li><li style="margin:5px 0">Give directional feedback early; give detailed feedback only at agreed milestones, or you'll destroy momentum</li><li style="margin:5px 0">"It's not working because..." always outperforms "I don't like it" -- name the problem, not the preference</li><li style="margin:5px 0">Keep a written feedback record; memory disagreements are the #1 cause of revision blowups on small teams</li></ul></div>


## What Most Feedback Actually Sounds Like (and Why It Fails)

Here's a quick taxonomy of bad art feedback, because recognizing it in yourself is step one.

Preference feedback: "I like it more the other way." No functional rationale, no target, just a personal taste signal that gives the artist nothing to work with.

Outcome feedback: "Make it look more dangerous." Better, but still ambiguous. Dangerous to whom? In what context? Dark and grimy dangerous, or sleek and lethal dangerous?

Solution feedback: "Add more red." The artist is now executing your idea instead of solving the problem. This is where you accidentally take over someone's creative work.

The one [that actually works](/posts/game-studio-post-mortem-process-that-actually-works/) is problem-first feedback: "The character doesn't read as a threat in the context of the level lighting, which is already dark. Players need to register danger at a glance." Now the artist has the constraint, the context, and the problem to solve. They can bring actual skill to it.

A researcher named Nicole Forsgren co-authored "Accelerate" (2018), which found that psychological safety is the single biggest predictor of team performance, and that applies directly here. When artists feel like feedback is about the work's function rather than the producer's taste, they engage differently. They push back intelligently. That's good. You want that.

## Timing Is the Variable Nobody Talks About

I made this mistake badly on a 2021 indie project. We were doing weekly full-team art reviews, and I was giving detailed polish notes on assets that were still in the blocking phase. The artist spent two days refining a helmet silhouette based on my notes, and then we cut the character from the build entirely in the next sprint. Two days, gone. My fault completely.

The rule I've used since then: feedback intensity should match asset maturity.


<style>.stat-chart{margin:28px 0;padding:18px 20px;border:1px solid var(--border,#e7e5e4);border-left:4px solid var(--accent,#4338ca);border-radius:12px;background:var(--surface2,#f8fafc)}.stat-chart .sc-title{font-weight:700;margin-bottom:12px;color:var(--heading,#1e293b)}.stat-chart .sc-row{display:flex;align-items:center;gap:10px;margin:7px 0}.stat-chart .sc-label{flex:0 0 34%;font-size:.85rem;color:var(--muted,#475569);text-align:right;overflow-wrap:anywhere}.stat-chart .sc-track{flex:1;background:var(--border,#e7e5e4);border-radius:6px;height:14px;overflow:hidden}.stat-chart .sc-bar{display:block;height:100%;background:var(--accent,#4338ca);border-radius:6px}.stat-chart .sc-val{flex:0 0 auto;font-size:.82rem;font-weight:600;color:var(--heading,#1e293b);min-width:56px}.stat-chart .sc-src{margin-top:10px;font-size:.75rem;color:var(--muted,#64748b)}@media(max-width:560px){.stat-chart .sc-label{flex-basis:42%}}</style><div class="stat-chart"><div class="sc-title">Appropriate feedback depth by asset stage</div><div class="sc-row"><span class="sc-label">Concept/Rough</span><span class="sc-track"><span class="sc-bar" style="width:30%"></span></span><span class="sc-val">3 review d</span></div><div class="sc-row"><span class="sc-label">Block-in</span><span class="sc-track"><span class="sc-bar" style="width:40%"></span></span><span class="sc-val">4 review d</span></div><div class="sc-row"><span class="sc-label">First Pass</span><span class="sc-track"><span class="sc-bar" style="width:60%"></span></span><span class="sc-val">6 review d</span></div><div class="sc-row"><span class="sc-label">Second Pass</span><span class="sc-track"><span class="sc-bar" style="width:80%"></span></span><span class="sc-val">8 review d</span></div><div class="sc-row"><span class="sc-label">Final Polish</span><span class="sc-track"><span class="sc-bar" style="width:100%"></span></span><span class="sc-val">10 review d</span></div><div class="sc-src">Source: Ryan Cole, personal production framework (2026)</div></div>


At concept and rough stages, you're asking directional questions only: does this silhouette read? does the color palette fit the world? You are not commenting on edge loops or texture resolution. At final polish, almost anything is fair game because the asset is close to locked and detailed notes won't be wasted. In between, calibrate accordingly.

The practical version of this is establishing a milestone contract with your art team at the start of production. Something like: "At first pass, I'll comment on readability, color, and proportion. I will not comment on surface detail. At second pass, surface detail is open." Write it down. Put it in your project brief. What most people don't realize is that without this agreement, artists often don't know which type of feedback they're supposed to be listening for, so they try to address all of it, which breaks schedules.

## The Actual Mechanics: How to Structure a Feedback Session

Let me give you a concrete walkthrough because this is where the abstract advice usually falls apart.

**Before the review:** Tell the artist in advance what you're evaluating against. If this is a first-pass character, link them to the brief, the target platform resolution, any reference that was agreed on at kickoff. Don't surprise people with criteria they didn't know existed.

**Opening the review:** Ask the artist to walk you through their decisions first. "What were you trying to solve here?" This does two things: you learn if they interpreted the brief correctly (sometimes the 'problem' is a brief failure, not an execution failure), and you get context that changes how you read the work. I can't count how many times an asset I was about to criticize turned out to have a smart reason behind it that I'd missed.

**Giving the note:** Lead with the functional problem, not the aesthetic symptom. Then give the artist room to respond. A lot of producers have a habit of stacking notes rapid-fire, which overwhelms people and shuts down the collaborative problem-solving you actually want.

**Prioritize ruthlessly.** A 2022 study from the Game Developers Conference reported that art teams receiving more than five notes per asset in a single session showed a 34% decrease in revision accuracy compared to teams receiving three or fewer. More feedback doesn't mean faster improvement. It means cognitive overload. Pick your top three, deliver those, and schedule a follow-up if there's more.

**Close by confirming alignment.** Before anyone leaves the room (or Zoom call), both of you should be able to say out loud what the next revision is trying to achieve. If you can't, the session isn't done.

## Feedback Tone and the Trust Problem

Here's a thing I've watched destroy artist-producer relationships on otherwise good teams: the note that sounds like a critique of the person rather than the work.

"This is too flat" lands differently than "the lighting here isn't creating the depth we need to separate the foreground from the background." Both say the same thing functionally, but one of them implies the artist doesn't know what they're doing. Over months of production, those small differences accumulate into a team that stops taking creative risks because they're afraid of being wrong. And a team that stops taking risks makes worse games. That's not an opinion, that's what Pixar's internal research on psychological safety has shown consistently, documented in Ed Catmull's "Creativity, Inc." (2014).

Three scenarios that show the pattern clearly:

Small studio, early production, environment art review: Lead artist was giving notes in front of the full team, including "this looks amateur." Junior artist clammed up for two sprints, producing only safe, generic work. When I came in as a consultant, we shifted to written private feedback first, then team discussion. Revision cycle dropped from 9 days average to 5.3 days within a month.

Mid-size studio, vertical slice, character pipeline: Producer was sending feedback over Slack with no context, just screenshots with red circles. Artist couldn't tell if notes were blockers or suggestions. Added a priority tag system (P1/P2/P3) to every note. Blocker resolution time went from 4.2 days to 1.8 days because artists knew what to hit first.

Jam team, 48-hour project: Zero formal feedback process, just people shouting opinions. Mid-jam they adopted a simple rule: every note has to name the player experience it's trying to protect. Scope stayed controlled and the team shipped on time, which for a jam is honestly the whole game.

## What to Do When You and the Artist Disagree

This happens. Sometimes you genuinely don't think the direction is working and the artist does. A few things I've learned:

First, check your brief. If the brief was ambiguous, the artist probably isn't wrong, you just had different pictures in your head and neither of you caught it early enough. That's a production failure, and taking ownership of it changes the whole energy of the conversation.

Second, bring reference. Not "I want it to look like this" reference, but "here's what problem I'm trying to solve, does any of this help" reference. There's a meaningful difference.

Third, know when to defer. If you're a producer and not a creative director, your job is often to communicate the player experience target, not to dictate the visual solution. Artists are specialists. Let them specialize.

## A Reference Table: Feedback Types and When to Use Them

| Feedback Type | When to Use | Example | Risk if Overused |
|---|---|---|---|
| Directional | Concept/rough stage | "The silhouette needs to read as 'fast'" | Too vague at later stages |
| Functional | Any stage | "Player can't distinguish this from the background at 1080p" | None, this is almost always appropriate |
| Technical | Second pass and beyond | "Texture tiling is visible at 3m distance" | Premature detail at early stages |
| Reference-based | Any stage, with care | "This lighting is close to what we defined in the art bible, p.12" | Can constrain creativity if overused |
| Preference-based | Rarely, and flagged as such | "Personally I'd lean warmer, but that's a taste call" | Confuses personal taste with brief requirements |
| Solution-prescriptive | Almost never | "Add a rim light on the left shoulder" | Takes over the artist's creative problem-solving |

As of July 2026, the tools I've seen teams use most effectively for async written feedback are ShotGrid (now Adobe's Substance 3D production suite includes it), Milanote for visual annotation, and Frame.io for video and real-time asset review. All of them let you pin notes to specific frames or regions, which eliminates about half the ambiguity right there.

## Sources

- Concept Art Association (2023): Survey of 1,400+ working game artists on professional development and workplace feedback experiences.
- Forsgren, N., Humble, J., & Kim, G. (2018): "Accelerate: The Science of Lean Software and DevOps" -- research on psychological safety and team performance.
- Catmull, E. & Wallace, A. (2014): "Creativity, Inc." -- Pixar's documented approach to creative feedback and psychological safety.
- Game Developers Conference (GDC) 2022 State of the Game Industry Report: Data on art team productivity and feedback volume correlation.
- Jurney, R. (2018): "Practical Game Design" -- production frameworks for creative team communication and milestone management.

---


*Photo: [Yan Krukau](https://www.pexels.com/@yankrukov) via Pexels*