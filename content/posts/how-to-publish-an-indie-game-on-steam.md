---
title: "How To Publish An Indie Game On Steam"
date: 2026-06-09T11:34:45.922853+00:00
draft: false
description: "Learn how to publish your indie game on Steam with our step-by-step guide covering Steamworks, store page setup, pricing, and launch strategies for indie develo"
image: "/img/heroes/159393.jpg"
categories: ["publishing"]
tags: ["publish", "indie", "game", "steam"]
author: "Samantha Roberts"
author_bio: "Samantha Roberts writes about game publishing, pitching, and bringing games to market."
slug: "how-to-publish-an-indie-game-on-steam"
affiliate_disclosure: true
faqs:
  - q: "How long does it take to get a game approved on Steam?"
    a: "Account approval after the $100 payment takes roughly five business days. Once you submit your finished build for launch review, expect three to five more business days, sometimes longer during major sales events when Valve's review queue backs up."
  - q: "Can I release a demo separately from the main game?"
    a: "Yes. In Steamworks, you create a Demo App associated with your base game's App ID. The demo has its own store page (linked to the main game) and its own build upload. Wishlists and followers on the main game carry over; the demo page doesn't accumulate separate wishlists."
  - q: "What percentage does Steam take from sales?"
    a: "Steam takes 30% up to $10 million in lifetime revenue, 25% from $10 million to $50 million, and 20% above $50 million. For most indie games, you're planning around a 70% revenue share to you."
  - q: "Do I need a business entity to publish on Steam?"
    a: "No. Individuals can publish on Steam under their own name and SSN (or equivalent). That said, an LLC costs $50-$150 to form in most US states and protects your personal assets if something goes legally sideways. Talk to an actual lawyer or accountant about what makes sense for your situation before you start generating real revenue."
  - q: "When should I set my launch date?"
    a: "Don't set a launch date until your build is in final testing and you're confident in a two-to-four week window. Announcing a date and missing it damages player trust and gets you negative press coverage before you've sold a single copy. Pick the date when the game is done, not when you hope it'll be done."
author_slug: "samantha-roberts"
author_title: "Contributing Writer"
lastmod: 2026-07-07
---
Steam charges a $100 app fee, takes 30% of your revenue, and is still the obvious choice for almost every indie developer. That should tell you everything about where the market is.

I've watched developers spend six months on a beautiful game and then wreck the Steam launch so thoroughly the algorithm never recovers. The platform isn't hard to understand, but there are specific decisions around timing and [store page setup](/how-to-build-a-steam-page-that-converts/) where a mistake costs real money and real wishlist momentum. This is what I wish someone had explained before I did it wrong the first time.

## The Steamworks Setup Nobody Explains Clearly

You start at [partner.steamgames.com](https://partner.steamgames.com). Pay the $100 app deposit with a credit card or PayPal. That fee gets credited back against your first $1,000 in revenue, so it's not pure dead weight if your game makes anything.

Then you wait. Valve takes roughly five business days to approve your account. Read the Steamworks documentation during that time, specifically the DRM, build upload, and store page checklist sections. It's tedious. Skipping it just costs you more time later.

Once approved, you create an app. Each game gets its own App ID. Set your base price in whatever currencies you want, but understand that Steam auto-converts for regions unless you manually override it. Override it. Brazil, Turkey, and Argentina have lower purchasing power, and local pricing absolutely tanks conversion in those places. The Steamworks pricing tool suggests prices by region based on PPP data. Use those as a starting point.

Your tax setup needs to happen before you earn a cent. Complete the tax interview in the Partner portal. US developers fill out a W-9. International developers fill out a W-8BEN or W-8BEN-E depending on entity type. Mess this up and Valve withholds 30% of all US-sourced revenue for backup withholding. I've seen developers wait three months for a payout because they skipped this.

## Your Store Page Is the Actual Product

Most developers treat the store page like an afterthought. That's backwards. This is where people decide whether to buy, and Steam's algorithm uses wishlist velocity, conversion rate, and review scores to decide who sees your game. A weak store page is a traffic leak you never patch.

The capsule image is the most important thing you'll make. It's 460x215 pixels (plus 231x87 for the small version) and appears in every list, queue, and search result. It needs to work as a thumbnail without text, communicate genre and tone instantly, and hold its own next to AAA titles. Pay for this if you have to. A $200-400 capsule from someone good on ArtStation is the highest-ROI spend you'll make on marketing.

For screenshots, start with six, aim for eight to ten. Lead with your best visual and gameplay moment, not a title card. Valve explicitly says title cards as the first screenshot hurt conversion. Show the actual game loop. Puzzle game? Show puzzles. RPG? Show combat and exploration, not menu screens.

Your short description (160 characters) appears in search and feeds. Make it a book jacket blurb. Lead with genre, then hook. "A hand-drawn puzzle game about rewinding time to solve crimes" does more work in twelve words than "An atmospheric, narrative-driven experience" does in six.

The long description supports SEO. Steam indexes keywords from it. Don't spam keywords, but do use what players search for: "pixel art RPG," "cozy farming sim," "soulslike platformer." Write for humans first, search second.

Tags start with you and then players add more. Set your own tags before launch since they feed the discovery algorithm. Skip obvious ones like "Indie" (it's noise now). Go specific: "Metroidvania," "Dark Fantasy," "Local Co-op." You get up to 20.

## The Coming Soon Page and Wishlist Window

| Task | Requirement | Timeline |
| --- | --- | --- |
| Steamworks Account Approval | Pay $100 app fee | ~5 business days |
| Coming Soon Page Launch | Playable build + screenshots + clear concept | Minimum 6 months before launch |
| Steam Next Fest Demo Submission | Demo ready | A few months before event (June/October) |
| Wishlist Accumulation Target | Reach visibility threshold | 7,000-10,000 wishlists by launch day |
| Store Page Elements | Capsule image, 6-10 screenshots, descriptions, tags | Before Coming Soon publication |
| Tax Setup Completion | W-9 or W-8BEN forms | Before earning revenue |
| Achievements Design | 12-20 well-designed achievements | Before launch |

This is where I see most of the wasted potential.

Publish your store page as "Coming Soon" as soon as you have a playable build, solid screenshots, and a clear concept. Six months before launch is the minimum. A year is better if you're building from scratch. Wishlists accumulate while you sleep, and they're the primary signal Steam uses for Day 1 visibility. The threshold where Steam's algorithm really pays attention is usually around 7,000-10,000 wishlists, though Valve's never officially said so. Every developer I've talked to reports that crossing 10,000 wishlists by launch day meaningfully changes your trajectory.

Steam Next Fest goes here. Valve runs it twice a year, usually June and October. Submit a demo during the application window, which opens a few months before the event. Next Fest is arguably the single best free marketing opportunity on Steam. I've seen games pick up 3,000-8,000 wishlists in six days without any PR budget. Demo quality matters, obviously, but just being in the event puts you in front of players actively looking for new games.

One timing detail people miss: don't launch on Friday. Valve's weekly top sellers list resets Thursday, and you want maximum days in that cycle for sales momentum. Tuesday or Wednesday launches have generally performed better for games I've shipped and for the broader data other developers share on Twitter/X and in the [Game Dev Unlocked](https://gamedevunlocked.com) community.

## Building and Uploading Your Game

Steamworks uses the Steam SDK for achievements, cloud saves, and the overlay. You upload builds with the Steamworks command-line tools via SteamPipe. It sounds scarier than it is. You define depots (file packages for different platforms or DLC) and upload them with a config file. Most major engines have SteamPipe tutorials. Unity has solid ones on the forums. Godot 4's Steam plugin (GodotSteam) has excellent documentation.

Don't add thirty achievements just to have them. Players notice padding. Twelve to twenty well-designed achievements that reflect real play milestones beat fifty "open the menu" achievements. Achievements show on your store page and players check them.

Steam Cloud saves are worth the hour to set up. Players hate losing saves when they switch machines. It's a small feature with outsized goodwill.

## The Review Build and the Launch Checklist

Valve requires a review before launch, which typically takes three to five business days. Submit at least a week before your target date, ideally two. Expect a revision request.

The review checks: functional build that runs without crashing on basic hardware, store page content that matches the actual game, mature content properly flagged, and no copyright violations in assets. Do your own full pass through the store page review checklist in Steamworks docs before submitting.

Send review copies to press and streamers two to three weeks before launch. Use Keymailer or Terminals.io to distribute keys at scale. Don't rely on Steam reviews alone for Day 1. You want external visibility driving traffic on launch. A single mid-size streamer playing your game on Day 1 can move hundreds of units.

Set a launch discount, or don't. The research genuinely splits both ways. Some developers swear by 10-15% off to push conversion. Others say it trains players to wait for sales and kills the game's perceived value. I've shipped it both ways. I'd lean toward no discount on launch, then hit a first sale at 20-25% off during Autumn or Winter sales (late November and December).

After launch, respond to every review for the first month. Steam surfaces developer responses and players notice. A thoughtful response to a negative review often converts curious buyers better than a dozen positive ones.

## Tools Worth Having in Your Stack

## Sources

- [partner.steamgames.com](https://partner.steamgames.com)
- [Game Dev Unlocked](https://gamedevunlocked.com)
- [Pixabay](https://www.pexels.com/@pixabay)
- I've talked to
- other developers share on Twitter/X and in the [Game Dev Unlocked](https://gamed


For project management: Hacknplan (built for game dev, $0-$9/month) or Notion (free tier covers most solo and small teams). Linear is excellent for bug tracking if you've got engineers on the team.

For store analytics: SteamDB (free) and Game Data Crunch (paid, around $20/month for indie tier) both pull Steam's public data and show how your wishlist growth compares to similar titles before launch.

For launch planning and market comps: Game Discover Co's newsletter and website, run by Simon Carless, is the best industry-specific Steam analysis I read consistently. His GDCo Plus tier (around $12/month) includes detailed revenue estimates and launch breakdowns. Worth it if you're serious about timing.

Books: "Blood, Sweat, and Pixels" by Jason Schreier won't teach Steam specifically but it recalibrates your expectations about how games actually get made. For the business side, "The GameDev Business Handbook" by Michael Futter is the most pragmatic breakdown of indie publishing deals, rights, and distribution.

*Photo: [Pixabay](https://www.pexels.com/@pixabay) via Pexels*