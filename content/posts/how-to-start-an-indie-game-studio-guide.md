---
title: "How To Start An Indie Game Studio Guide"
date: 2026-06-14T11:13:39.514727+00:00
draft: false
description: "Learn how to start an indie game studio with our complete guide covering business setup, team building, funding options, game development tools, and marketing s"
image: "/img/heroes/38094552.jpg"
categories: ["strategy"]
tags: ["start", "indie", "game", "studio", "guide"]
author: "Tyler Brooks"
author_bio: "Tyler Brooks has run operations and led teams inside game studios, from hiring to milestone planning to the unglamorous work that keeps a project on track. At Gamedev Producer he covers studio management and leadership."
slug: "how-to-start-an-indie-game-studio-guide"
affiliate_disclosure: true
faqs:
 - q: "How much money do I need to start an indie studio?"
   a: "That depends almost entirely on your burn rate and timeline. A solo developer with a day job and a two-year part-time project might need $5,000-15,000 for software, assets, and legal setup. A two-person team going full-time with an 18-month target needs to cover $150,000-250,000 in living and operating costs before revenue. Know your actual monthly number before you quit anything."
 - q: "Do I need to incorporate before making my first game?"
   a: "Technically no, but you should do it before signing any contracts, accepting any payments, or working with collaborators. The protection and clarity it provides is worth the $200-500 it costs. Doing it retroactively when something goes wrong is more expensive and more stressful."
 - q: "Should my indie studio have a publisher?"
   a: "Not automatically. A publisher makes sense when you need capital you don't have, marketing infrastructure you can't build, or platform relationships you can't access on your own. If you can self-fund, ship, and market a smaller game, keeping 100% of revenue and 100% of IP is a real advantage. The calculus changes as your project scale increases."
 - q: "What engine should a new indie studio use?"
   a: "Unity and Unreal Engine 4/5 are the realistic choices for most teams. Unity has a larger indie ecosystem and more accessible learning curve; Unreal is more powerful out of the box for 3D but has a steeper ramp. Godot is free, open source, and increasingly capable for 2D. The honest answer: use whatever your team already knows. Switching engines to chase features costs more than people admit."
 - q: "How do I find co-founders or team members for an indie studio?"
   a: "The most reliable sources are people you've already worked with, game jams (Ludum Dare and Global Game Jam both produce real professional relationships), and communities like TIGSource forums or the r/gamedev Discord. Be skeptical of strangers who are 'very passionate' but have no shipped work and no specific skills. Passion without track record is a risk, not an asset."
author_slug: "tyler-brooks"
author_title: "Studio Operations Lead"
lastmod: 2026-07-07
---
Most guides about starting an indie studio spend three thousand words telling you to "follow your passion" and "build what you love." They skip the part where you run out of money in month eight and wonder why nobody told you about quarterly estimated taxes.

Here's what actually matters.

## The Legal and Financial Setup Nobody Wants to Think About

| Setup Type | Cost | Timeline | Notes |
| --- | --- | --- | --- |
| LLC (U.S.) | $50-$500 | ~1 afternoon | State filing fees vary |
| Limited Company (UK) | £12 | ~15 minutes | Via Companies House |
| Operating Agreement | $1,500-$3,000 | Varies | Full startup attorney setup |
| Steam Direct | $100 | N/A | Per game; 70/30 revenue split |
| Hacknplan (paid tier) | ~$5/month | N/A | Per user |
| Mercury/Relay Bank Account | Free | ~1 day | Dedicated business account |

Do this first, before you write a single line of code or sign a single contract. I've watched studios collapse not because the game was bad but because two co-founders had a handshake deal that meant nothing when one of them wanted to leave.

Form an LLC. In most U.S. states, it takes about $50-500 in filing fees and an afternoon on your state's Secretary of State website. If you're in the UK, a limited company through Companies House costs £12 and fifteen minutes. Yes, you can technically operate as a sole proprietor. Don't. The liability protection alone is worth the paperwork.

Co-founders need a [written operating agreement](/contract-basics-for-indie-game-developers/) before any work begins. This covers the important stuff: who owns what percentage, how decisions get made when you disagree, what happens if someone leaves in year one versus year three, who gets the IP if the studio dissolves. Clerky or a startup attorney (budget $1,500-3,000 for the full setup) will handle this properly. LegalZoom is cheaper but you often get what you pay for.

Open a dedicated business bank account. Mercury is free and works well for indie studios. Relay is another solid option. Mixing personal and business finances is how you create an audit nightmare and also how you accidentally pierce your liability protection.

Tax stuff: if you're in the U.S. and you're making any money, you're paying quarterly estimated taxes. Miss those and you'll owe penalties on top of what you already owe. Set aside 25-30% of every payment you receive into a separate savings account and pretend that money doesn't exist. I didn't do this the first year. Learn from that.

## Structuring Ownership and Roles Before You Need To

The most common co-founder conversation I've seen go badly is the one that never happened until it was too late. Two developers start a studio, never talk about equity, never talk about what "equal partners" means operationally, and then one of them is doing 80% of the production work while the other is "busy with other things." By month six there's resentment. By month twelve there's a lawyer.

Here's what I'd actually do: start with a conversation about contribution rather than ownership. Who's bringing what, when, and for how long? Sweat equity is real but it needs to be defined. Vesting schedules on founder equity (typically four years with a one-year cliff) are standard in tech startups for a reason, they apply to games too.

For solo founders, this is simpler, but you still need to decide whether you're bringing on contractors, revenue-share partners, or employees, and what the paperwork looks like for each. Contractors require 1099s in the U.S. Revenue share agreements need to be in writing with clear definitions of what "revenue" actually means (gross? net? after platform fees? after what costs?).

## Picking Your First Project Like Your Studio Depends On It (Because It Does)

The first game you ship matters more than the second or third. Not because it needs to be a masterpiece, but because it needs to actually ship.

Scope is the single most reliable predictor of whether an indie studio makes it to a second project. Not talent. Not funding. Scope. A studio with three people who ship a tight $8 puzzle game in fourteen months will outlast a studio of five people who spend three years on an RPG that never makes it out of pre-production.

Take your honest estimated timeline and double it. Take your honest estimated budget and add 40%. If you can still say yes to the project at those inflated numbers, you have a shot. If the only way the project makes sense is if everything goes perfectly, you're already in trouble.

Platform choice matters early. PC via Steam is still the most accessible entry point for most indie studios. Steam Direct costs $100 per game, the revenue split is 70/30 until you hit $10M in sales, and the audience is large enough that even a modest game can find buyers if it has a clear identity. Mobile is a different business entirely, closer to performance marketing than game development, and I'd steer most first studios away from it unless you have explicit experience there. Console ports are worth thinking about but they're not a day-one decision.

Pick a genre with a proven audience and a gap you can fill. This isn't selling out. It's product thinking. "Cozy farming sim with base-building" is specific enough to market. "A unique experience that blends many genres" is not a game description, it's a warning sign.

## The Production Infrastructure That Actually Scales

Even if your studio is two people in an apartment, you need the same production fundamentals as a larger team. The difference is just in how much process you apply.

Version control is non-negotiable. Git with GitHub or GitLab for code. Git LFS or Perforce for heavy binary assets. I've seen studios lose weeks of work to bad merge conflicts because they were emailing Unity project folders to each other.

For project management, Hacknplan is built specifically for game development and costs around $5/month per user for the paid tier. It models tasks the way game devs actually think, with disciplines and milestones baked in. Notion works well for documentation and wikis. For a small team that wants something free and familiar, even Trello with a disciplined board structure will do the job. The tool matters less than the habit of keeping it current.

Track your schedule. This sounds obvious. Most indie studios don't actually do it until they're already late. A simple milestone plan in a spreadsheet, updated weekly, showing what's done and what's slipping, will surface problems before they become disasters. This is genuinely 80% of what a producer does.

For communication, Slack or Discord both work. Discord is free and many indie teams already live there. The key thing: keep design decisions out of chat and into a documented decision log. Chat is ephemeral. Decisions about how your save system works need to be findable six months later.

"The Game Production Handbook" by Heather Maxwell Chandler is the closest thing to a complete reference for production processes. Jason Schreier's "Blood, Sweat, and Pixels" isn't a how-to, but reading what went wrong at studios larger than yours is useful calibration. On the business side, "The Business of Indie Games" by Alex Wawro (available as part of the Game Developer archives) covers the financial realities clearly.

The Game Production track on Coursera through Michigan State University is solid for foundational PM concepts. For something more game-specific and practical, the Game Developer Conference Vault (GDC Vault) has hundreds of postmortem talks, many free, where developers explain what worked and what didn't on actual shipped titles. That's your best continuing education.

## Getting to Revenue Without Burning Out

Most indie studios don't fail because the game was bad. They fail because they ran out of money and morale before shipping.

The financial model for a first-time indie studio is usually one of three things: self-funded (savings, part-time day jobs, low burn rate), revenue from contract work alongside original IP development, or a publishing deal. Each has real tradeoffs.

Self-funded is the most common and the hardest. Your runway is your personal savings minus your monthly burn. If you and a co-founder are both working part-time on this while keeping day jobs, your burn might be $1,000/month for software licenses and assets. If you've both quit your jobs to go full-time, you're burning $8,000-15,000/month just on living expenses depending on where you live. Know this number. Write it down.

Contract work, meaning paid work-for-hire on other games or adjacent projects, is how a lot of studios stay alive between original titles. It's not glamorous but it's real money. The risk is scope creep on the contract side eating into your IP development time. I've seen studios where the contract work kept the lights on so well that they never shipped their own game. If you go this route, ring-fence your IP development time and treat it as non-negotiable.

Publishing deals give you an advance, which is really a recoupable loan against future royalties, plus marketing support and sometimes platform relationships. Publishers like Raw Fury, Devolver, or Humble Games vary considerably in deal terms. Expect advances ranging from $100K to $1M+ depending on the project, with recoupment before you see royalties. Read any publishing contract carefully. The IP reversion clauses matter most.

Wishlist building on Steam should start the moment your game's concept is solid enough to show. Not when you're close to launch. The algorithm rewards wishlists at launch, and the time to build that audience is during development. Steam Next Fest (happens twice a year) is genuinely valuable for demo exposure if your game is far enough along.

---

Starting a studio is a production problem before it's a creative one. Get the foundation right, scope ruthlessly, and ship something you can learn from. The studios I've watched succeed weren't always the most talented rooms in the building. They were the ones that kept moving.