---
title: "How To Write A Game Design Document"
date: 2026-06-04T12:23:59.741108+00:00
draft: false
description: "Learn how to write a game design document with our step-by-step guide. Cover key sections, structure your ideas, and keep your team aligned throughout developme"
image: "https://images.pexels.com/photos/9572697/pexels-photo-9572697.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
categories: ["production"]
tags: ["write", "game", "design", "document"]
author: "Ryan Cole"
author_bio: "Ryan Cole covers game production and milestone planning at GameDevProducer."
slug: "how-to-write-a-game-design-document"
affiliate_disclosure: true
faqs:
  - q: "How long should a game design document be?"
    a: "There's no correct length. A focused indie game's GDD might be fifteen pages; a live-service title might have hundreds of pages spread across a wiki. The better question is whether every section is doing real work. If you can cut a page without losing any information the team actually needs, cut it."
  - q: "Should I write the GDD before or after prototyping?"
    a: "Write a short pitch and core mechanics overview first, then prototype, then expand the GDD based on what you learned. GDDs written entirely before any prototyping tend to describe imaginary games that don't match what actually feels good to play. The document should follow understanding, not substitute for it."
  - q: "What software is best for writing a GDD?"
    a: "Notion is the most popular choice for indie teams right now and it's genuinely good for the price (free for small teams). Confluence is the standard in larger studios. Google Docs works fine with discipline. Avoid Word or PDFs for anything you expect to keep current; static formats die the moment the game changes."
  - q: "Do solo developers actually need a GDD?"
    a: "Yes, but a short one. Even if you're the only person on the project, you're not the same person at month eight that you were at month one. A short document that records your core decisions and open questions saves you from relitigating the same design problems repeatedly. Think of it as writing notes to your future, exhausted self."
  - q: "What's the most common GDD mistake?"
    a: "Writing too much before anyone has played anything. The second most common is writing a document nobody can find or knows to update. Both of these kill the document's usefulness. Start lean, keep it in a shared wiki, and treat updates as a team habit."
author_slug: "ryan-cole"
author_title: "Senior Contributing Writer"
---
Most game design documents are dead on arrival. Not because the designer didn't care, not because the game idea was bad. Because the writer confused thoroughness with usefulness, and produced something so dense that nobody on the team actually read it.

I'll be honest: I've been guilty of this myself. My first GDD at a mid-size studio in 2011 was 94 pages. Gorgeous formatting, a table of contents with four levels of nesting, a five-page section on the fictional history of a kingdom the player would spend about forty minutes in. My lead programmer read the first twelve pages, then asked me to walk him through the rest verbally. That conversation took twenty minutes. The GDD took six weeks.

That experience broke something useful in me. I stopped thinking about the GDD as a document and started thinking about it as a communication tool with a specific job to do. Different job, different output entirely.

## What a GDD Is Actually For

Here's the thing most writing guides get wrong: they treat the GDD as a spec document, a legal record, a creative bible, and an onboarding manual all at once. It's none of those things, or rather, it can be one of them, but you have to pick.

The GDD's real job is to get your whole team to the same mental model of the game, fast, and to give them a place to go when they disagree about something. That's it. Every decision you make about format, length, and structure should serve that goal.

If you're a solo dev, your GDD is basically a decision journal. You're the only reader, so optimize for your future self who's tired and confused and needs to remember why you made a specific call three months ago. If you're on a team of five, the GDD needs to be readable by a programmer who hates prose, an artist who thinks in visuals, and a producer (hi) who's going to mine it for scope estimates. If you're pitching to a publisher, you're writing something closer to a pitch deck with mechanical detail. Totally different documents.

The mistake is writing one document that tries to speak to all of those audiences equally. It'll fail all of them.

## The Structure That Actually Gets Used

I've reviewed probably 300 GDDs at this point, from solo projects to $40M productions. The ones that get referenced, revised, and actually shape the game tend to share a specific structure. Not identical formatting, but the same load-bearing sections.

**The one-page pitch.** Always first. Before anything else, a reader needs to know: what is this game, who is it for, why does it exist, and what's the core loop. One page, no exceptions. If you can't do it in one page you don't understand your own game well enough yet. Harsh, but true. The format I use: a logline (one sentence, genre plus hook), a target player description, a core experience statement ("the player should feel like..."), and a short paragraph on the primary mechanic. Done.

**Core mechanics.** This is where the document either earns its keep or collapses entirely. You're not describing what the game looks like, you're describing how it works, specifically enough that someone could build a prototype without asking you a single question. I want to see: what the player can do, how systems interact, what creates tension or progression, and what the primary feedback loops are. Use diagrams if they help. A hand-drawn flowchart photographed on your phone beats three paragraphs of prose about the same system every time.

**Content inventory.** Levels, characters, items, enemy types, whatever the game contains. This section is primarily for your producer and your scope conversations. You don't need full design detail here, just enough to know what exists and roughly what it'll take to build. A table works fine. A list works fine. The point is that someone can look at this and say "oh, we have thirty enemy types, that's a conversation."

**Game feel and reference.** Most GDDs skip this entirely. Most teams miss it. How should this game feel? Not mechanically, but experientially. What are your reference games? What's the camera behavior trying to accomplish emotionally? What does juice mean in this project's context? I've started including short video reference links in digital GDDs and it's made art direction conversations dramatically more productive. A screenshot from Hollow Knight or a clip from a GDC talk communicates in four seconds what would take a paragraph to describe badly.

**Open questions.** Honest list of things you haven't decided yet. This sounds like weakness. It's actually the opposite. Every design has unresolved questions. Writing them down prevents the team from making silent assumptions that conflict with each other. I include a column for "decision deadline" next to each open question, which forces you to actually close them out.

Some GDDs need a narrative design section, a monetization section, an audio direction section. Most don't, or those sections belong in separate documents maintained by the people responsible for them. The narrative designer should own the narrative bible. The GDD just needs to say "tone is X, narrative delivery is Y, see the narrative bible for detail."

## Length, Format, and the Living Document Problem

Short answer on length: as short as possible while still being unambiguous. I've seen great GDDs at eight pages and terrible ones at three hundred. The page count tells you almost nothing.

What I've landed on for format: the GDD lives in a wiki, not a Word document or a PDF. Notion, Confluence, Nuclino, whatever your team already uses. The wiki format does three things a static document doesn't: it's linkable (so the character doc can link to the combat doc), it's versionable without the "GDD_FINAL_v3_ACTUALLY_FINAL.docx" naming disaster, and it's genuinely collaborative in a way that doesn't require emailing files around.

If you're a small team or solo, Notion is probably fine and it's free up to a point. If you're in a studio already on Jira, Confluence is the obvious choice since your tasks and your design docs live in the same ecosystem. I've also seen teams use Google Docs with aggressive use of internal links and it works perfectly well. The tool matters less than the discipline of keeping it updated.

And that's the living document problem. The GDD has to stay current or it becomes actively harmful, a source of outdated information that misleads new team members and generates arguments about what was "actually" decided. My rule: if a design decision changes, the person who owns that section updates the doc before the end of the sprint. Non-negotiable. I've enforced this by making GDD reviews part of sprint retrospectives, which sounds heavy but actually takes about ten minutes when the doc is well-maintained.

## The Section Nobody Tells You to Write

Write a "what this game is not" section. Seriously.

Scope creep doesn't usually come from someone proposing a wild, obviously-out-of-scope feature. It comes from reasonable people making reasonable extensions of the existing design, each one small, collectively catastrophic. A clear articulation of what you've deliberately excluded -- and why -- is worth more than any number of schedule buffers.

On a roguelike project I worked on a few years back, we had a line in the GDD that said "no player housing, no relationship systems, no persistent world state between runs beyond the meta-progression defined in section 4." Every time someone proposed a new feature (and they always did, features are fun to propose), we could point to that line and have a conversation grounded in an actual decision we'd documented, not a vague appeal to scope.

What surprised me about this section was how much the team liked writing it. There's something clarifying about articulating your constraints out loud. It makes the thing you are building feel more real.

## Making It Readable for Non-Designers

## Sources

- [Tima Miroshnichenko](https://www.pexels.com/@tima-miroshnichenko)


Your programmer doesn't read for pleasure. Your concept artist is going to open this document once, skim it, and leave. You have about ninety seconds before they close the tab.

Write section headers that are actual statements, not labels. Instead of "Combat System," write "Combat is fast, readable, and punishes passivity." The reader learns something from the header alone. If they never read the section, they got the main point.

Use a glossary. Define every piece of jargon the first time it appears and link to the glossary. This is especially true for internal vocabulary, the made-up names for mechanics that make perfect sense to you and sound like gibberish to everyone else.

Prototype before you write. I know that feels backwards, but the GDD for a system you've actually playtested is ten times more accurate and half as long as the GDD for a system you've only imagined. If something's in the doc but hasn't been touched in a prototype, flag it with an uncertainty marker. We use a simple emoji convention: a question mark for unvalidated assumptions. Keeps everyone honest.

For tools: I've found Machinations genuinely useful for documenting economy and loop systems visually, and the free tier covers most indie needs. For flowcharts, Miro or even FigJam work well if your team is already in Figma. For the actual writing, I like Notion for smaller teams and Confluence once you're past about fifteen people.

One last thing. The GDD doesn't make the game. The game makes the game. The document's only job is to get the team building the same thing. If it's doing that, it's a good GDD regardless of how it looks or how long it runs. If it's not doing that, adding more sections won't fix it.

*Photo: [Tima Miroshnichenko](https://www.pexels.com/@tima-miroshnichenko) via Pexels*