---
title: "Write a Game Design Spec: Producer's Step-by-Step Guide"
date: 2026-11-22T16:26:17.957441+00:00
draft: false
description: "Learn how to create a comprehensive game design spec as a producer. Essential structure, templates, and best practices for documenting your game vision."
image: "/img/heroes/27043900.jpg"
categories: ["pm frameworks"]
tags: ["write", "game", "design", "spec", "producer"]
author: "Stephen Brenish"
author_slug: "stephen-brenish"
author_title: "Lead Game Producer"
author_bio: "Stephen Brenish is a Lead Game Producer at Epic Games (Fortnite, Unreal Engine) and the founder of GameDevProducer. Across 14+ years in game production he has shipped and operated live titles at scale, previously as a Senior Program Manager at Blizzard Entertainment. Certified ScrumMaster."
slug: "how-to-write-a-game-design-spec-as-a-producer"
affiliate_disclosure: true
faqs:
  - q: "How long should a game design spec be?"
    a: "For a single feature, aim for 4-10 pages. If you're consistently going over 10 pages, the feature probably needs to be broken into smaller, separately specced pieces. Shorter specs get read; longer ones get skimmed or skipped."
  - q: "Who should write the spec, the producer or the designer?"
    a: "It depends on the studio. In many setups, the designer writes the spec and the producer reviews it for completeness, feasibility, and testability. In others, the producer writes it from the designer's notes. What matters is that someone with authority over the feature owns the document and keeps it current."
  - q: "What's the difference between a GDD and a feature spec?"
    a: "A game design document (GDD) is a high-level description of the whole game, often written during pre-production. A feature spec covers one specific system or mechanic in enough detail to implement and test. Most teams find GDDs useful early on and feature specs more useful during active development."
  - q: "Do I need acceptance criteria if we have a QA team writing their own test cases?"
    a: "Yes. QA test cases describe how to test something. Acceptance criteria describe what 'correct' actually means. Without the latter, your QA team is writing test cases against assumptions, and those assumptions may not match what design or engineering intended."
  - q: "What project management tools work best for tracking specs?"
    a: "Confluence paired with Jira is the most common combination at mid-to-large studios and integrates reasonably well. Notion is a strong choice for smaller teams that want something less structured. The specific tool is less important than making sure specs are linked directly to the tickets that implement them, so there's no ambiguity about which version of a spec a task was built against."
---

Most producers writing their first [game design](/posts/how-to-write-a-game-design-document/) spec make the same mistake: they write a vision document instead of a contract with the future. Those aren't the same thing, and confusing them is how you end up six months into production with engineers who built something technically correct and completely wrong.

A game design spec (sometimes called a GDD section, feature spec, or functional spec depending on your studio) is not a creative pitch. It's a working document that answers three questions for every person who touches it: what are we building, how will it behave, and how do we know when it's done? If your spec can't answer all three, it's not ready.

The good news is that writing a solid spec is a learnable skill. It doesn't require years of design experience. It requires discipline about what goes in, what stays out, and who the document is actually for.


<div class="kt" style="margin:26px 0;padding:18px 22px;border:1px solid var(--border,#e7e5e4);border-left:4px solid var(--accent,#4338ca);border-radius:12px;background:var(--surface2,#f8fafc)"><div style="font-size:.72rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--accent,#4338ca);margin-bottom:8px">Key takeaways</div><ul style="margin:0;padding-left:1.15em"><li style="margin:5px 0">A spec answers: what are we building, how does it behave, and what does "done" look like.</li><li style="margin:5px 0">Write for engineers and QA first; designers already know what they meant.</li><li style="margin:5px 0">Scope your spec to one feature or system, not an entire game.</li><li style="margin:5px 0">Every spec needs explicit acceptance criteria or it cannot be tested or closed.</li><li style="margin:5px 0">A one-page spec that ships beats a 40-page doc that never gets read.</li></ul></div>


## Who You're Actually Writing For

Producers often write specs as if the reader is the design director who approved the feature. That's backwards. The people who need a spec most are the ones furthest from the original design conversation: an engineer who joined the team two weeks ago, a QA analyst writing test cases at 11pm before a build, a third-party vendor implementing one piece of a system they can't see the rest of.

Write every spec assuming the reader has zero context. Not because your team is inexperienced, but because context evaporates faster than you think. The person who was in the room for the original design discussion will not remember the edge case you all agreed on verbally. They just won't.

That said, don't write a novel. A spec that runs past 15 pages for a single feature is usually a spec that hasn't been scoped properly yet. Break it up.

## The Anatomy of a Feature Spec

There's no universal format, but the following structure works across most team sizes and feature types. Adapt it, but don't gut it.

**Overview (half a page or less).** One paragraph on what this feature is and why it exists in the game. Not the design philosophy. Not the competitive analysis. Just: what is it, and what player problem does it solve?

**Functional requirements.** This is the heart of the doc. What does the system do? Cover the happy path first (the thing works as intended), then every meaningful exception state. If the player has no currency when they try to buy something, what happens? If the server drops mid-transaction, what happens? If the input arrives out of order, what happens? Engineers need to know these answers before they write a single line of code, not after.

**Out of scope.** Underused and incredibly valuable. Explicitly list what this spec does NOT cover. This protects you from scope creep and from the engineer who, with the best intentions, adds a "nice to have" that breaks your timeline.

**UI/UX references.** Link to the wireframes or mockups. Don't describe the visual layout in prose; that's what images are for. Do describe the behavior triggered by each UI element.

**Acceptance criteria.** This is where most producer-written specs fall apart. Acceptance criteria are testable, binary statements. "The player can purchase items" is not an acceptance criterion. "When the player taps the Buy button with sufficient currency, the item appears in their inventory within 2 seconds and their currency total decrements correctly" is one. Write them like QA will use them as a checklist, because QA will use them as a checklist.

**Open questions.** A live list of unresolved decisions. Don't pretend a spec is complete when it isn't. Flag what's still being decided and who owns the decision.

## Scope Is the Real Problem

A common misconception is that a thorough spec means a long spec. Length isn't the issue. Scope is. Producers who try to spec an entire progression system in one document almost always produce something that's simultaneously too vague to implement and too long to read.

**Example:** Assume you're building a crafting system with four main behaviors: ingredient gathering, recipe unlocking, item crafting, and inventory management. Rather than one 30-page doc, you'd write four specs, each 4-8 pages, each with its own acceptance criteria and open questions. The dependency relationships between those specs get tracked in your project management tool (Jira, Shortcut, whatever you're using), not buried in the prose. Total effort: roughly the same. Utility: dramatically higher, because each spec can be handed to a different engineer or reviewed independently.

## Spec Types and When to Use Each

Different moments in production call for different levels of detail. A pitch-phase design brief and a sprint-ready feature spec aren't the same document, and treating them as interchangeable is expensive.

| Document Type | When to Write It | Length | Primary Reader | Contains Acceptance Criteria? |
|---|---|---|---|---|
| Concept brief | Pre-production, pitching | 1-2 pages | Leadership, stakeholders | No |
| Feature spec | Before sprint work begins | 4-10 pages | Engineers, QA | Yes |
| Technical design doc | Complex systems, engine work | 10-20 pages | Engineers only | Sometimes |
| Hotfix brief | Live-service patch | Half a page | Dev lead, QA | Yes |
| Post-launch change spec | Live feature modification | 2-5 pages | Full team | Yes |

The mistake most junior producers make is writing a concept brief when what engineering needs is a feature spec. You can tell because engineers start asking questions the document should have already answered.

## Keeping Specs Alive

A spec that's accurate on day one and ignored after that is still a liability. Someone will find the wrong version. Someone will implement the original design after it was changed verbally in a standup. This happens constantly.

Pick one place where specs live and enforce it without exceptions. Confluence is the most common choice at mid-to-large studios. Notion works well for smaller teams. The tool matters less than the discipline of updating the spec when decisions change, and noting in the document when and why something changed. A revision log at the top of the doc (even just two columns: date and change summary) has saved countless teams from "wait, I thought we decided..." conversations.

One more thing: specs shouldn't require a producer to interpret them. If your team is regularly coming to you to explain what the spec means, the spec isn't done yet.

## Sources

- [Game Developers Conference (GDC) Vault]: Searchable archive of talks on design documentation, production process, and feature scoping from shipped titles.
- [Gamasutra / Game Developer Magazine]: Articles and postmortems on production documentation practices across AAA and indie studios.
- [Jesse Schell, "The Art of Game Design: A Book of Lenses" (3rd edition)]: Covers design communication and documentation as part of the design process.
- [Atlassian Confluence documentation]: Official guides on structuring team wikis and living documentation, applicable directly to spec management.
- [Shortcut (formerly Clubhouse) knowledge base]: Practical guidance on linking specs and stories in agile game development workflows.

---


*Photo: [Ben Khatry](https://www.pexels.com/@ben-khatry-430197437) via Pexels*