---
title: "Get Your Game on Steam: The $100 Fee and What Comes Next"
date: 2026-11-18T17:22:31.854715+00:00
draft: false
description: "Learn the Steam publishing fee, revenue split, and complete steps to launch your indie game on the world's largest PC gaming platform."
image: "/img/heroes/13450798.jpg"
categories: ["publishing"]
tags: ["your", "game", "steam"]
author: "Stephen Brenish"
author_slug: "stephen-brenish"
author_title: "Lead Game Producer"
author_bio: "Stephen Brenish is a Lead Game Producer at Epic Games (Fortnite, Unreal Engine) and the founder of GameDevProducer. Across 14+ years in game production he has shipped and operated live titles at scale, previously as a Senior Program Manager at Blizzard Entertainment. Certified ScrumMaster."
slug: "how-to-get-your-game-on-steam"
affiliate_disclosure: true
faqs:
  - q: "How long does Steam review take after you submit a build?"
    a: "Typically 2 to 5 business days for a standard review, but Valve doesn't guarantee a fixed window. First-time submissions and accounts with no prior release history can sometimes take longer. Build at least a week of buffer into your launch plan."
  - q: "Can you publish on Steam as an individual, without a company?"
    a: "Yes. Valve accepts individual (sole proprietor) applications. You'll complete a W-9 as an individual if you're in the US, or the appropriate W-8 form if you're outside it. Having a legal entity isn't required, though it's worth considering for liability reasons."
  - q: "Does Valve approve or reject games based on quality?"
    a: "No. Steam is not a curated platform in that sense. Valve's review checks that your game runs, that your store page is accurate, and that you're complying with their content policies. They're not judging whether the game is good."
  - q: "What happens if your game doesn't sell enough to recoup the $100 fee?"
    a: "The $100 is simply not returned. The recoupment only triggers once your game earns $1,000 in adjusted gross revenue on Steam. If it earns less, Valve keeps the fee. This is true per app, so if you submit three games, you've paid $300 in fees regardless of recoupment."
  - q: "Can you change your game's price after launch?"
    a: "Yes, any time outside of an active sale window. Valve restricts price changes during sales events and for a short period before them. You can run your own discounts via the Steamworks dashboard once 30 days have passed since launch."
---

Getting a game on Steam is not complicated. The platform is more open than it's ever been, the upfront cost is a fixed $100 per app (more on what [that actually](/posts/game-studio-post-mortem-process-that-actually-works/) buys you below), and Valve has published clear documentation covering nearly every step. What trips people up isn't the process itself, it's the parts nobody tells you about: review timelines, the build submission checklist, the metadata decisions that affect discoverability before your game ever goes live.

Here's what you actually need to know, in the order you'll need to know it.

The $100 fee (called the "Steam Direct fee") is a deposit, not a one-time charge you lose. Valve credits it back to your developer account once your game earns $1,000 in adjusted gross revenue. It's not a large barrier, but it does mean that if your game earns nothing, you're out $100. That's intentional. It filters out placeholder submissions without meaningfully blocking anyone with a real project.


<div class="kt" style="margin:26px 0;padding:18px 22px;border:1px solid var(--border,#e7e5e4);border-left:4px solid var(--accent,#4338ca);border-radius:12px;background:var(--surface2,#f8fafc)"><div style="font-size:.72rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--accent,#4338ca);margin-bottom:8px">Key takeaways</div><ul style="margin:0;padding-left:1.15em"><li style="margin:5px 0">The Steam Direct fee is $100 per app; Valve recoup it once your game earns $1,000 in revenue.</li><li style="margin:5px 0">Valve's review period after your first build submission is typically 2-5 business days, but can extend.</li><li style="margin:5px 0">You need a Steamworks account, a legal entity or individual with tax info on file, and a completed store page before your game can go live.</li><li style="margin:5px 0">Setting your release date to "Coming Soon" before you're ready is free and starts building your wishlist immediately.</li><li style="margin:5px 0">Steam takes a 30% revenue cut by default; this drops to 25% after $10M in lifetime sales on Steam, and 20% after $50M.</li></ul></div>


## Setting Up Your Steamworks Account

Before anything else, you need a Steam account in good standing, then you apply for a Steamworks developer account at partner.steamgames.com. The application asks for business or individual details and payment information, because Valve needs to pay you eventually and needs to satisfy their own tax obligations. You'll go through a tax interview (W-9 for US individuals and entities, W-8 forms for international developers), and you'll need to provide banking details for direct deposit.

This setup step takes longer than people expect, especially for international developers dealing with W-8BEN or W-8BEN-E forms. Don't treat it as a 20-minute formality. Some developers have waited a week or more for their banking details to be verified. Start this before you think you need to.

One common misconception: you do not need a registered LLC or corporation to publish on Steam. Sole proprietors and individuals can submit. That said, publishing under a business entity has real tax and liability advantages, and you should talk to an accountant who works with games if you're unsure which structure makes sense.

## Building Your Store Page

Once you've paid the $100 fee for your app, you get access to the Steamworks dashboard for that title. This is where you'll build your store page, and the quality of this page is arguably more important than when you submit your build.

Your store page needs:

- Capsule art (required sizes include the header capsule at 460x215px, the small capsule at 231x87px, the library capsule at 600x900px, plus several others; check the current Steamworks documentation for the full and up-to-date list)
- At least 5 screenshots, all of which must show actual gameplay or in-game content. Marketing text overlays will get your page flagged.
- One trailer (optional but strongly recommended)
- A short description (up to 300 characters, shown above the fold)
- A long description with no arbitrary character limit but subject to Valve's content guidelines
- Tags, genre, categories (single-player, controller support, cloud saves, etc.)
- System requirements for minimum and recommended specs
- Age rating (you do this through Valve's integrated rating questionnaire, not through ESRB separately)

The tags matter more than most first-time developers realize. Steam's discovery algorithm uses them to surface your game in "More Like This" sections and tag-based browsing. Under-tagging, or picking broad tags that don't reflect your actual game, leaves wishlist traffic on the table before you've sold a single copy.

Set your page to "Coming Soon" as early as your store page and capsule art are finished. Every day your page is live in Coming Soon mode is a day someone can wishlist your game. Valve's data (published in their own developer blog posts) shows that wishlists correlate directly with day-one and launch-week sales.

## Submitting Your Build

Build submission happens through the Steamworks SDK, specifically through a command-line tool called SteamPipe. It's not glamorous but it works. You create depots (packages of files), configure your app's launch options, and upload. Your first build submission triggers a Valve review, and that review is currently taking somewhere between 2 and 5 business days under normal circumstances, though that window can stretch.

What Valve is checking in that review: that your game launches, that it doesn't falsely claim features (like "Full Controller Support" when only partial support exists), that the content matches what your store page describes, and that you're not violating any content policies. They're not reviewing it for quality. That's not a gatekeeping function Steam performs.

You need a Release Candidate build, your store page must be fully complete and reviewed, and your bank and tax information must be verified before you can request to go live. Missing any one of these blocks you at the final step. Plan for it.

**Example:** Suppose you finish your game in late September and want to launch in October. You should have your Steamworks account fully set up and your store page in "Coming Soon" state no later than mid-August. That gives you 6-8 weeks of wishlist accumulation and leaves a comfortable buffer for the build review plus any revisions Valve requests. If you're a first-time developer with no prior Steamworks submissions, budget an extra week for account verification. Submitting your first build in early October for a mid-October launch is technically possible but leaves you no margin.

## Revenue Split and Pricing

Steam's revenue share is straightforward, though it has tiers most [indie developers](/posts/game-launch-checklist-for-indie-developers/) won't hit:

| Lifetime net sales on Steam | Valve's cut | Your cut |
|---|---|---|
| $0 to $10M | 30% | 70% |
| $10M to $50M | 25% | 75% |
| Above $50M | 20% | 80% |

The 30/70 split on the first $10M is what virtually every indie developer will live with indefinitely. For context, $10M in net sales at a $20 price point with 30% going to Valve means you've sold roughly 714,000 copies. If you're at that tier, you have other, better problems to worry about.

Pricing is set in your Steamworks dashboard, and you can configure individual regional prices or use Valve's suggested pricing tool [that converts](/posts/how-to-build-a-steam-page-that-converts/) your base USD price into regional equivalents. Take regional pricing seriously. Players in markets where your default price converts to something unaffordable simply won't buy. Valve's suggested prices aren't perfect but they're a reasonable starting point.

## Sources

- [Valve / Steamworks Documentation](https://partner.steamgames.com/doc/home): Official developer documentation covering account setup, SteamPipe, store page requirements, and launch process.
- [Valve Steam Direct page](https://partner.steamgames.com/steamdirect): Official description of the $100 fee, what it covers, and recoupment terms.
- [Valve Steamworks Developer Blog](https://store.steampowered.com/news/group/4145017): Valve's own published data on wishlists, discoverability, and platform changes.
- [SteamPipe documentation](https://partner.steamgames.com/doc/sdk/uploading): Detailed reference for build uploads, depot configuration, and content server tools.

---


*Photo: [Jonathan Borba](https://www.pexels.com/@jonathanborba) via Pexels*