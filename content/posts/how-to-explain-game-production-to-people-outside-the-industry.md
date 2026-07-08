---
title: "How To Explain Game Production To People Outside The Industry"
date: 2026-05-28T09:40:22.492275+00:00
draft: false
description: "Learn how to explain game production to friends, family, and clients in simple terms. Break down complex pipelines, roles, and processes without the industry ja"
image: "/img/heroes/8369603.jpg"
categories: ["role identity"]
tags: ["explain", "game", "production", "people", "outside"]
author: "Jordan Lee"
author_bio: "Jordan Lee has shipped indie titles and contributed to larger studio projects, writing from the trenches about what it actually takes to finish and release a game. At Gamedev Producer the focus is development workflow, scope, and shipping."
slug: "how-to-explain-game-production-to-people-outside-the-industry"
affiliate_disclosure: true
faqs:
 - q: "How do I explain what a producer does without making it sound like project management?"
   a: "Start with what a producer protects: the team's ability to do their best work. A project manager tracks tasks. A game producer tracks tasks and watches for creative drift, team burnout, scope creep, and dependency failures across disciplines that don't naturally talk to each other. The job is risk management in a medium where the product doesn't exist until the very end."
 - q: "What's the best analogy for explaining why games take so long?"
   a: "The theme park ride analogy works well for general audiences. For business-savvy people, try this: 'We're building a product where the quality of the experience can't be verified until the whole thing is working together. Every individual component can test as complete and the combined result can still be wrong.' That maps to software concepts they already understand, like integration testing versus unit testing."
 - q: "How do I handle the 'but couldn't you just make a simpler game?' comment?"
   a: "Acknowledge that it's a real option, then explain the tradeoff honestly. Simpler games do ship faster. They also compete in a different market, often against free mobile games or smaller studios with lower cost structures. The scope of your game reflects a commercial and creative decision, not a failure to think of the easy path. You can be direct about that."
 - q: "How do I explain scope creep to someone who thinks we just keep adding unnecessary features?"
   a: "Scope creep rarely starts with unnecessary features. It usually starts with a feature that seemed small, turned out to be structurally complex, or revealed a problem in an adjacent system that now also needs fixing. Use a physical analogy: 'We added a window to this room and discovered the wall it went into was load-bearing. Now we're also fixing the wall.' That gets the point across without sounding like you made a mistake."
 - q: "What do I do when someone just doesn't accept that game development is hard?"
   a: "Stop trying to convince them and shift to alignment. Ask what outcome they need and work backward from that. If an investor doesn't believe your timeline, the productive conversation isn't about game development theory. It's about what evidence would give them confidence. That reframes the conversation from debate to problem-solving, and it's usually more productive for everyone."
author_slug: "jordan-lee"
author_title: "Game Developer"
lastmod: 2026-07-07
---
Your publisher contact just forwarded your milestone report to their finance team, and now someone in accounting wants a 30-minute call to understand "why it takes so long to make a video game." You've been in production for eight months. You have 40,000 words of design documentation, a Jira board with 600 tickets, and a team of 12 people who haven't slept properly since Q1. And now you have to explain all of that to someone whose last gaming experience was Minesweeper.

This happens constantly. With investors. Family members at Thanksgiving. Journalists who cover tech but not games. Platform partners who understand software but not *creative* software. Most developers bomb these conversations, not because they're bad communicators, but because they're explaining the wrong things. They lead with process when they should lead with stakes. They default to jargon when they need analogies. And they badly underestimate how genuinely foreign the game development world looks from outside the industry.

Here's how to actually fix that.

## Why Game Development Defies Normal Software Logic

The first thing most outsiders reach for is a comparison: "So it's like building an app, right?" The honest answer is: kind of, but the parts that are different are the parts that make it hard.

Building a game means simultaneously producing software, art, music, narrative, UX, and interactive systems that all have to work together and *feel good*. That last part is the killer. "Feels good" isn't a spec. You can't unit-test fun. A combat system can be technically complete and still be miserable to play, which means you throw it out and start again. No app developer has to worry about whether their spreadsheet tool is emotionally satisfying.

I've used this framing with non-technical stakeholders and it lands every time: imagine you're building a theme park ride, except you don't know if it's enjoyable until you're actually on it, and you can only build one prototype at a time, and the prototype costs six months of work. That's game development. Every design decision is a hypothesis. Every milestone is a test.

What most people don't realize is that a huge chunk of game development time isn't spent building features. It's spent *evaluating* features, realizing they don't work, and either reworking or cutting them. A feature that actually ships might represent 30% of the work that went into that design area. The other 70%? Invisible.

## The Language of Scope, and Why It's Always More Than It Sounds

When you tell someone outside the industry that your game has "two hundred enemy types," they hear a list. When you're a producer, you hear: concept art, color variants, rigging, animation states, sound effect sets, AI behavior trees, combat balance testing, localization flags, and QA passes for each one. Times two hundred.

This is the multiplication problem. Every feature in a game description is actually a cluster of interdependent tasks across multiple disciplines. A single new weapon in an action RPG can touch character art, VFX, audio, UI, game design, engineering, and QA. If any one of those drops a ball, the weapon doesn't ship.

When explaining scope, use the "layers" method. Pick one feature your audience can actually picture, then walk them down the stack:

1. **Concept**: What is it supposed to do? How does it feel?
2. **Design**: How does it interact with existing systems?
3. **Art**: What does it look like, and how does it animate?
4. **Engineering**: How does the code make it work?
5. **Audio**: What does it sound like in every state?
6. **QA**: Where does it break, and on what hardware?
7. **Polish**: Does it feel right, or just function correctly?

Seven layers. One feature. That's not inefficiency. That's the work.

## How to Talk About Timelines Without Sounding Evasive

Nothing makes a game developer look worse to an outsider faster than a slipping release date. Finance people, publishers, and PR teams instinctively assume that delays mean poor planning. Sometimes that's true. But often it reflects something genuinely hard to explain: creative software development has irreducible uncertainty.

Here's a comparison that helps:

| What outsiders expect | What game production actually looks like |
|---|---|
| Linear process: design, build, ship | Iterative cycles: build, test, redesign, rebuild |
| Delays = something went wrong | Delays often = you discovered something important |
| Milestones = completion checkpoints | Milestones = risk reduction checkpoints |
| Scope is fixed at greenlight | Scope evolves as the game reveals itself |
| QA is a final step | QA is woven through the entire production |

When I'm talking to someone who needs a timeline they can trust, I stop defending the schedule and start explaining *how we manage uncertainty instead of eliminate it*. [Agile sprints](/game-producer-tools-and-software-for-project-management/). Vertical slices. Alpha and beta gates. These aren't bureaucratic overhead. They're tools for catching expensive mistakes early. Frame it that way and most intelligent business people get it immediately.

A line I've borrowed from senior producers: "We don't know exactly when we'll be done, but we know exactly what we'll know by this date, and that's what this milestone buys us."

## Making the Team Structure Make Sense

Game studios look bizarre from the outside. Why does a 15-person team need both a game designer and a level designer? What does a technical artist actually do? Why are there three different people with "producer" in their title?

The clearest explanation I've found maps studio structure to film production. It's not perfect, but it's close enough.

- The **game director** is your director. Creative vision, final say on feel.
- The **producer** is your line producer. Schedule, budget, people, risk.
- **Engineers** are your crew. They build the camera rigs and the lighting systems.
- **Artists** are your production designers and VFX team.
- **Game designers** are a hybrid of screenwriter and choreographer. They write the rules that create experience.
- **QA** is your continuity department, except they also stress-test the set for structural collapse.

Once people have that map, the org chart stops looking like redundancy.

## Practical Steps for Your Next Stakeholder Conversation

Whether you're prepping for an investor meeting, a publisher check-in, or explaining to family why the game "isn't done yet," here's what actually works:

1. **Lead with the experience, not the process.** Start with what the player will feel, not how the systems work. Stakeholders care about outcomes.
2. **Use one concrete example to represent the whole.** Don't try to explain all of production. Pick one feature and walk them through it completely.
3. **Translate time into decisions, not tasks.** Instead of "we spent two months on combat," say "we used those two months to figure out which combat system was worth building."
4. **Acknowledge what's hard without being defensive.** Saying "this part is genuinely difficult and here's why" builds more credibility than pretending everything is under control.
5. **Give them a role.** Ask what they need to feel confident. Sometimes a weekly status email replaces a 30-minute confusion call.

## Tools That Make This Easier

## Sources

- [Notion](https://www.notion.so)
- [Codecks](https://www.codecks.io)
- [RDNE Stock project](https://www.pexels.com/@rdne)
- to their finance team


If you're a producer trying to communicate production realities to people outside your team, the right tools help. A few that actually earn their place:

**[Notion](https://www.notion.so)** works well for building stakeholder-facing dashboards that show progress without exposing the chaos of your internal Jira board. You curate what they see.

**[Codecks](https://www.codecks.io)** was designed specifically for game developers. Its visual card format communicates progress in a way that non-technical stakeholders find intuitive.

For building your own communication skills, *The Art of Game Design* by Jesse Schell is the best book I know for understanding why games work the way they do. When you understand it deeply yourself, explaining it to others gets much easier.

Coursera's **Game Design and Development Specialization** from Michigan State also includes production-focused content that's useful if you're newer to the producer role and want structured frameworks for these conversations.

---

The goal of all this isn't to make outsiders love game development or fully understand it. The goal is to get them informed enough to trust you and your team. You're not writing a textbook. You're building just enough of a shared vocabulary that the conversation becomes useful. Most people, once they understand that "we're discovering the game as we build it" isn't an excuse but a description of how creative software works, will cut you way more slack than you'd expect.

*Photo: [RDNE Stock project](https://www.pexels.com/@rdne) via Pexels*