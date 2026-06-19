---
title: "Live Service Game Production Vs Ship And Done Titles"
date: 2026-05-27T03:26:05.671809+00:00
draft: false
description: "Explore the key differences in producing live service games versus traditional ship and done titles, from ongoing costs and team structures to long-term player "
image: "https://images.pexels.com/photos/7862367/pexels-photo-7862367.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
categories: ["industry intel"]
tags: ["live", "service", "game", "production", "ship"]
author: "Samantha Roberts"
author_bio: "Samantha Roberts writes about game publishing, pitching, and bringing games to market."
slug: "live-service-game-production-vs-ship-and-done-titles"
affiliate_disclosure: true
faqs:
  - q: "Can a small indie team realistically run a live service game?"
    a: "Yes, but it requires a different kind of small team. Studios like Motion Twin (Dead Cells) and Re-Logic (Terraria) have supported long-running games with small teams, but they built games with exceptional word-of-mouth and didn't rely on constant new content for retention. If your live model depends on regular content drops to keep players engaged, you need more capacity than most indie teams have. A game that retains players through depth rather than novelty is much more sustainable at small scale."
  - q: "What's the right monetization model if I go live service?"
    a: "Battle passes with seasonal themes have become the baseline expectation for fairness in live service. Cosmetics-only monetization preserves competitive integrity. Pay-to-win mechanics damage long-term trust and accelerate churn, particularly in Western markets. Spend time in your genre's community before you finalize your monetization design. Players are vocal about what they consider predatory, and that reputation follows your game."
  - q: "How do I scope a live service game's initial launch content?"
    a: "Think of launch as your 'season zero.' It needs enough content to establish the core loop and justify the buy-in, but not so much that you've burned your content budget before you've validated retention. Many successful live service titles launched relatively lean and used early player data to prioritize what to build next. A 20-40 hour launch experience for a PvE game with strong seasonal content planned for months 2 and 4 is a reasonable structure."
  - q: "Should post-launch patches for a ship-and-done game be free?"
    a: "Almost always yes. Bug fixes and quality-of-life patches should be free. You're fulfilling the implicit promise of the game players bought. Paid DLC that adds substantial new content is fine and expected. Charging for patches or content that fixes design problems from the base game damages trust and review scores. If you're unsure, watch how your genre's community reacts when comparable studios charge for updates."
  - q: "What project management tools work best for live service production?"
    a: "Jira remains the industry standard for sprint-based live ops work, especially if you need custom workflows and integration with your CI/CD pipeline. Hacknplan is a strong alternative built specifically for game production that handles the hierarchical feature structure common in game dev better than generic PM tools. For communication and async coordination across a distributed live ops team, Slack combined with a solid Confluence or Notion wiki keeps institutional knowledge from walking out the door when staff turns over. The honest truth is that neither model is inherently better. Ship-and-d"
author_slug: "samantha-roberts"
author_title: "Contributing Writer"
---
You're six months into pre-production and someone just asked the question your whole team has been quietly avoiding: "Are we making a live service game or not?" The room goes silent. Everyone has opinions. Nobody has a plan. This single decision shapes your team size, budget runway, monetization model, post-launch roadmap, and your personal stress levels for the next several years. Get it wrong and it doesn't just hurt your game. It can sink your studio.

## What These Two Models Actually Mean in Practice

"Live service" and "ship and done" are shorthand for something much deeper than update frequency. They describe fundamentally different relationships with your players, your revenue, and your production pipeline.

A ship-and-done title (sometimes called a premium or packaged game) has defined scope. You build it, ship it, patch critical bugs, then your team moves on. *Disco Elysium*. *Hades*. *Return of the Obra Dinn*. Revenue is front-loaded. Success gets measured in launch window sales. The game is essentially a product you hand to players and step back from.

A live service game is a platform. It never really ships in the traditional sense. It launches. *Fortnite*, *Destiny 2*, *Path of Exile*, and *Warframe* are the obvious examples, but plenty of smaller games operate this way too. Revenue comes continuously through battle passes, cosmetics, expansions, and seasonal content. The production machine never fully stops. Your sprint cadences, team structure, QA processes, everything has to sustain ongoing output for months or years.

Here's what I tell people in that awkward pre-production meeting: the model you choose isn't a marketing decision. It's an infrastructure decision. Make it early, make it deliberately, and make it based on what your team can actually sustain.

## The Business Case Is Different for Each

You might be wondering which model makes more money. The honest answer is: live service titles have a higher ceiling and a more brutal floor.

The top-earning live service games generate billions annually. But the market has consolidated hard around a handful of dominant titles. Players have limited time and limited wallet share. Getting a new live service game into someone's regular rotation against *League of Legends* or *Apex Legends* is genuinely one of the hardest problems in games right now.

Ship-and-done titles follow different math. A well-reviewed indie game selling 200,000 units at $20 generates $4 million gross, which after platform cuts lands around $2.8 million. For a small team, that's real revenue. The risk profile is more predictable. You need a strong launch window, good review scores, and some word-of-mouth momentum, but you're not betting on player retention 18 months out.

The middle ground, a premium game with paid DLC or an expansion, can work but it requires you to be honest about which model you're actually building. I've watched studios convince themselves they're doing "premium plus optional live elements" and end up with the cost structure of live service and the revenue of a packaged game. That gap kills studios.

## Production Structure: Where They Diverge Most Sharply

| Factor | Ship and Done | Live Service |
|---|---|---|
| Team size at launch | Often scales down post-ship | Stays large or grows post-launch |
| Sprint structure | Milestone-driven toward gold master | Continuous cycles (2-4 week sprints ongoing) |
| QA investment | Peaks before launch | Must be sustained permanently |
| Content pipeline | Ends at ship | Needs seasonal or monthly output |
| Player support | Limited post-launch | Requires dedicated live ops staff |
| Post-launch budget | Small patch reserve | Ongoing operating cost (often 30-60% of dev cost annually) |
| Monetization timing | Revenue at purchase | Revenue distributed over game lifetime |

That "30-60% of dev cost annually" number is the one that surprises people. If it cost you $3 million to ship your game, plan to spend $900K to $1.8 million per year keeping a live service running at a professional level. That includes server infrastructure, live ops staff, community management, ongoing QA, and content production. Your investors or publisher need to understand this before you commit.

For production tooling, I lean on **Jira** or **Hacknplan** for sprint management. Hacknplan's built specifically for game dev and handles feature/task hierarchies better than most. **Confluence** or **Notion** works for documentation that needs to live across a multi-year project. If you're running a live service, **Amplitude** or **GameAnalytics** for live telemetry becomes essential, not optional.

## How to Actually Make the Decision

Work through these five questions with your leads before you commit.

1. **What's your realistic team size at launch?** If you're shipping with six people, live service will probably break you. A sustainable live service needs at minimum a dedicated live ops producer, ongoing engineering support, and a content team that isn't also doing core development.

2. **Do you have 18+ months of operating runway post-launch?** Live service games often take 6-12 months after launch to reach profitability. You need bridge capital to survive that period.

3. **Does your core loop support ongoing engagement?** Some games are built to be completed and set down. Narrative-heavy experiences, short-form puzzle games, and story-driven RPGs rarely convert well to live service because the engagement model doesn't fit. Be honest about whether your game's loop actually rewards hundreds of hours of play.

4. **Who is your publishing partner and what do they expect?** Publishers who invest in live service infrastructure have very different expectations than those who fund premium titles. Misalignment here creates conflict at every milestone.

5. **What happens if player count drops 40% in month three?** This is the question nobody wants to answer. For a ship-and-done title, that's fine. For a live service, it triggers a death spiral if you don't have a retention plan built in advance.

If you're looking to sharpen your thinking here, *Blood, Sweat, and Pixels* by Jason Schreier gives real-world context on how these decisions play out under pressure. For the production methodology side, **PMI's Game Production Certificate** or courses on **LinkedIn Learning** around agile game production can help you build the process vocabulary your team needs.

## The Live Ops Reality Nobody Warns You About

Even experienced producers underestimate how different live operations feel from development. In development, you're building toward something. In live ops, you're maintaining a relationship with a player base that has expectations, frustrations, and opinions they'll express loudly and publicly.

Community trust is your most important asset in live service. When *No Man's Sky* launched in 2016, it was a case study in a premium game that tried to pivot toward live service to recover from a disastrous launch. It worked, but only because Hello Games committed to years of free updates and relentless transparency. Most studios don't have that kind of runway or resilience.

I've seen smaller studios launch a "live service" game with one content designer and no dedicated community manager. By month four, players feel abandoned, reviews tank, new player acquisition dries up, and the game enters maintenance mode before it ever found its audience. The lesson is simple: if you're going to commit to live, commit fully, or don't start.