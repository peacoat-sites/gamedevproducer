---
title: "Press Kit Essentials For Indie Game Launches"
date: 2026-06-25T11:13:16.804601+00:00
draft: false
description: "Learn what every indie game press kit needs, from screenshots and trailers to bios and logos, to help journalists cover your launch effectively."
image: "https://images.pexels.com/photos/6804605/pexels-photo-6804605.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
categories: ["publishing"]
tags: ["press", "essentials", "indie", "game", "launches"]
author: "Ryan Cole"
author_slug: "ryan-cole"
author_title: "Production Lead"
author_bio: "Ryan Cole has spent a decade working in game production across mobile, PC, and console projects. He started as a junior producer at a mid-size studio and worked his way up by learning to ship on schedule without burning out his team. At GameDevProducer, he covers production frameworks, milestone planning, and the practical side of getting a game from concept to launch."
slug: "press-kit-essentials-for-indie-game-launches"
affiliate_disclosure: true
faqs:
 - q: "How long before launch should a press kit be ready?"
   a: "Have it live at least six to eight weeks before your launch date. Journalists working on preview features often need lead time, and some outlets have publishing calendars that require weeks of advance notice. Two weeks before launch is too late for most long-lead coverage."
 - q: "Do I need a separate press kit for each platform?"
   a: "Not a fully separate kit, but note platform-specific differences clearly in one place. If your Switch version has different features or launches later than Steam, make that explicit so nobody covers your game with wrong information."
 - q: "What's the right format for a press kit, a PDF or a website?"
   a: "A webpage. PDFs are annoying to link to, often look bad on mobile, and make journalists extract assets manually. A simple webpage with a zip download at the top is what journalists actually want. The presskit() tool generates exactly this and takes about an hour to set up."
 - q: "Should I include review codes in my press kit?"
   a: "Include a clear instruction for how to request review codes, not the codes themselves in the public kit. A contact email or a form (Keymailer and Woovit are both reasonable for this) keeps things manageable and prevents keys from being scraped."
 - q: "What if my game doesn't have any press coverage yet, does a press kit still matter?"
   a: "Yes, more than if you already had coverage. A clean, professional press kit is often the thing that signals to a journalist that you're serious and have done the work. Without coverage to validate you, the quality of your materials does a lot of the credibility work. Think of it as your studio's handshake."
lastmod: 2026-07-07
---

Most indie devs build a press kit two days before launch because a journalist finally emailed them and they panicked. I've done exactly this. You're scrambling through Google Drive at midnight trying to find a screenshot that isn't just a debug menu, writing a "short description" that somehow ends up being 400 words, and wondering why you didn't just handle this in March. The press kit you throw together in that panic is almost always fine. But "fine" means you're leaving real coverage on the table.

Here's what actually matters, and what most people treat as filler.

## The Assets Journalists Actually Use

| Element | Format | Minimum Quantity | Key Detail |
| --- | --- | --- | --- |
| Screenshots | PNG, 1920x1080 | 8 | Show actual gameplay, not UI or menus |
| Capsule Art | Multiple sizes | 4+ | Include 460x215, 231x87, 600x900, 1:1 square, 1200x628 |
| Trailer | MP4/WebM | 1 | Under 90 seconds, gameplay in first 5 seconds |
| Short Description | Plain text | 1 | 150 words max |
| Long Description | Plain text | 1 | 300-500 words |
| Metadata Block | Text or table | 1 | Studio name, title, platforms, release date, price, URLs, contact, socials |

Forget about what you *think* looks good. Think about what a person at a desk, writing about six games today, can drop straight into a CMS without editing it.

Start with screenshots. You need a minimum of eight, formatted at 1920x1080, saved as PNG. That's it on format. On content: show the game actually running. Not your UI. Not your main menu. Not concept art. Show the most visually interesting moment you can find in actual gameplay, with the HUD either hidden or looking intentional. A lot of press kit screenshots feel like the developer was embarrassed to show the real game. If your game looks like what it is, just show what it is.

Capsule art at multiple sizes. Steam has specific sizes (460x215, 231x87, the vertical 600x900), and you want those ready. But also include a simple 1:1 square version and a horizontal banner around 1200x628 for social and press use. Journalists crop things. Give them something that still reads at small sizes.

The trailer is the one thing you cannot cheap out on. Not because it needs to be cinematic, but because it's the single piece of media that does the most work per second. Keep it under 90 seconds. Show gameplay within the first five seconds, full stop. I've watched journalists close trailers that opened with 30 seconds of logo sting and atmospheric music. They're not being unfair, they're just busy and your game is one of 40 in their inbox.

If you don't have a trailer yet and you're reading this, go make one before you build the rest of the kit. Prioritize accordingly.

## The Writing That's Actually Hard

Two pieces of copy and most developers get both wrong.

The short description is 150 words or fewer and has to tell someone what kind of game this is, who it's for, and why they should care. That's a lot to do in 150 words. The genre, tone, unique hook, and one specific thing that makes it different. Write it like you're telling a friend who doesn't play games what you made. Then cut it in half.

The long description is where people dump everything they're afraid to leave out. Don't. It should be 300-500 words. Lead with what makes the game interesting, not with the lore. Nobody reading a press kit cares about your world's political history until after they care about the game. Save the lore for the game itself.

One thing I'd push back on: a lot of press kit guides tell you to keep descriptions "professional and neutral." I think that's wrong. Your game has a voice. Your description should too. If it's a weird, surreal game, the copy should feel a little weird. If it's brutal and punishing, the description shouldn't read like a corporate product brief. Match the register of your game, because that's actually useful information for a journalist trying to quickly figure out who their audience is.

## The Metadata Nobody Thinks About

This section exists because I've seen press kit requests from journalists who needed this information and had to follow up a second time. That follow-up email sometimes doesn't come.

Include: studio name, game title, platforms, release date (or window), price, the store page URL, your contact email, and your social handles. Put this in a plain text block or a simple table at the top of your presskit page or kit folder. Not buried in a PDF.

Also include: a one-line description of your studio. One sentence. "Three-person studio based in Warsaw, formerly worked at X" takes three seconds and tells a journalist something real. That context matters more than you'd think when someone is trying to build a narrative around covering a small team.

Factsheet generators like presskit() (the static site tool originally by Rami Ismail, still widely used and hosted in various places online) will prompt you for most of this automatically. It's not fancy, but it's clean and journalists know how to read it. Using a recognized format is genuinely worth something.

## Where to Host It and How to Share It

Host your press kit somewhere always-on, linkable, and not behind a login. That means not a Google Drive folder with permission settings. Not a Dropbox link that expires. A subdomain of your own site (press.yourgame.com or yourstudio.com/press) is ideal. Even a static presskit() page on GitHub Pages works fine.

Put the link in your email signature now. Put it on your [Steam page](/how-to-build-a-steam-page-that-converts/). Include it in every pitch email you send. Make it the thing you can drop into any conversation without friction.

One practical note: put a zip file at the top of the page that contains all your assets, labeled with your game name and the date. Something like `GameName_PressKit_June2026.zip`. Journalists sometimes just want to grab everything in one shot and move on. Make that easy.

## Pitching With the Kit

## Sources

- [Notion](https://www.notion.so)
- [cottonbro studio](https://www.pexels.com/@cottonbro)
- Nobody Thinks About


The kit isn't the pitch. This confuses a lot of developers who build a beautiful press kit and then just email a link to it and wait. That's not how this works.

Your [pitch email](/how-to-pitch-a-game-to-a-publisher/) is a separate, personal message. Two to four short paragraphs. Why this game, why this journalist specifically (did they cover something similar?), what's interesting about the launch timing or story, and then the link to the kit. The kit is supporting material. The pitch is the actual communication.

I use Notion to keep track of who I've pitched, what I sent them, and when. Nothing fancy, just a table with a journalist name, outlet, date contacted, and response status. [Notion](https://www.notion.so) is free at indie scale and it'll keep you from accidentally emailing the same person twice, which is embarrassing enough to have happened to me once to make me very careful about it.

---


*Photo: [cottonbro studio](https://www.pexels.com/@cottonbro) via Pexels*