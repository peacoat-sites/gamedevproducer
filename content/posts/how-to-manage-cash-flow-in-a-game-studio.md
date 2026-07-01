---
title: "How To Manage Cash Flow In A Game Studio"
date: 2026-07-01T11:38:16.368899+00:00
draft: false
description: "Learn practical strategies to manage cash flow in your game studio, from budgeting milestones to securing funding and avoiding common financial pitfalls."
image: "https://images.pexels.com/photos/7821554/pexels-photo-7821554.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
categories: ["budgeting"]
tags: ["manage", "cash", "flow", "game", "studio"]
author: "Ryan Cole"
author_slug: "ryan-cole"
author_title: "Production Lead"
author_bio: "Ryan Cole has spent a decade working in game production across mobile, PC, and console projects. He started as a junior producer at a mid-size studio and worked his way up by learning to ship on schedule without burning out his team. At GameDevProducer, he covers production frameworks, milestone planning, and the practical side of getting a game from concept to launch."
slug: "how-to-manage-cash-flow-in-a-game-studio"
affiliate_disclosure: true
faqs:
  - q: "How much runway should a game studio keep in reserve?"
    a: "Most financial advisors suggest three to six months of operating expenses as a minimum buffer, but game studios should target the higher end because revenue timing is unpredictable and milestone payments are often delayed. If you're below three months of runway, treat it as a crisis requiring immediate action, not a planning note for next quarter."
  - q: "Is it better to pay contractors or hire full-time employees to manage cash flow?"
    a: "Contractors give you variable cost flexibility, which is valuable when revenue is uneven, but they're typically more expensive on an hourly basis and less invested in the long-term project. The honest answer is a hybrid approach: full-time for roles you need continuously and that require deep domain knowledge of your project, contractors for specialized work that has a defined end date."
  - q: "Can a signed publishing deal help me get a bank line of credit?"
    a: "Yes, and more studios should use this. A signed contract with a creditworthy publisher is collateral, and many banks with small business lending will extend a line of credit against it. You're essentially borrowing against money you're already owed. Terms vary, but this can bridge a two to three month gap without diluting equity or changing your deal terms."
  - q: "What's the most common cash flow mistake first-time studio founders make?"
    a: "Treating their annual budget as a cash flow plan. A budget tells you what you plan to spend over a year. It says nothing about whether you'll have the cash in hand when specific bills arrive. Build the weekly forecast. Seriously. The number of studios that have gone into distress despite having technically adequate budgets is sobering."
  - q: "How do grants affect cash flow planning?"
    a: "Grant money is real revenue but it's slow and uncertain until it's in your account. Never build a cash flow forecast that depends on a grant you haven't been awarded yet. Plan for the grant as upside; build your minimum viable plan around money you can predict. When the grant arrives, it extends runway rather than being the thing that creates it."
---

Thirty percent of indie studios that fail cite cash flow problems as the primary cause. Not bad games. Not marketing failures. Cash flow. The money was there on paper, and then it wasn't, and nobody saw it coming until it was too late.

I've watched this happen up close, more than once. A team spends eight months building something genuinely good, hits a funding gap six weeks before they'd planned to launch, can't make payroll, and the whole thing collapses. The game was real. The revenue projections were reasonable. But the cash wasn't in the account when the bills came due, and there's no emergency brake on a studio burn rate once you've got salaries, licenses, and contractor invoices all stacking up in the same month.

This isn't a topic that gets covered seriously in game dev circles. Everyone talks about GDD structure, Unreal vs Unity, how to pitch to publishers. Cash flow forecasting? That's "business stuff" and it gets deferred until someone's staring at a bank account that's three weeks from empty.

Let me try to fix that.

---

## The Difference Between Profit and Cash (and Why Most Producers Get This Wrong)

I'll be honest: I thought these were basically the same thing for the first two years of my career. I was wrong in a way that cost a team I was working with real money.

Profit is what's left after you subtract expenses from revenue on paper. Cash flow is the actual movement of money through your bank account in real time. A studio can be "profitable" on a quarterly report and completely broke in the middle of that same quarter because client payments came in 45 days late, contractor invoices hit early, and the SteamDeck dev kit charge cleared the same week.

This gap, the timing gap between money owed to you and money you owe, is where indie studios go under.

The mechanics matter here. If you're doing work-for-hire alongside your own IP development (which most small studios do to survive), your invoices probably have Net-30 terms, sometimes Net-60. That means you do the work in January, invoice in February, and get paid in March. Meanwhile you're paying your engine license (Unreal's per-seat subscriptions, Unity Pro at around $2,040 per seat annually as of mid-2026, or Godot at zero), your payroll every two weeks, and your AWS or Multiplay hosting bill every single month. The calendar misalignment will grind you down.

**The fix isn't complicated, but you have to actually do it.** Build a 13-week rolling cash flow forecast. Not a P&L, not an annual budget. A 13-week (three-month) week-by-week forecast of cash in and cash out. Update it every Monday morning. This single habit has saved more small studios than any amount of revenue optimization.

What goes in it: every known invoice you're expecting and its realistic collection date (not the due date, the date you'll actually have the money), every recurring cost with its exact billing cycle, every contractor payment schedule, and a column for "unplanned" that you seed with 10-15% of your monthly burn as a buffer.

Tools I'd use for this: Float (around $59/month, integrates directly with QuickBooks and Xero) or even a well-built Google Sheets template if you're early stage. Pulse is another option at $29/month that's simpler. The sophistication of the tool matters less than whether you're actually looking at it every week.

---

## Milestones, Publishers, and the Timing Trap

If you've got a publisher deal, congratulations. Also: pay close attention to your milestone payment schedule, because it's almost certainly not aligned with your actual cost curve.

Publisher advances are typically paid against milestones: Alpha, Beta, Gold, launch. What nobody tells you clearly enough is that your spend is front-loaded and the milestone payments are back-loaded. You're hiring people, buying assets, paying for tools from month one. The milestone money shows up when you've proven something exists.

A studio I worked with in the mid-2020s signed a solid $800K publishing deal for a narrative RPG. Four milestone payments across 18 months. The problem: their largest staffing costs hit months 3-7, the first milestone payment didn't clear until month 5, and the second wasn't until month 11. They nearly lost two senior engineers at month 6 because they simply didn't have the cash, even though the deal was healthy and the game was on track.

**Scenario:** Studio with $800K publishing deal, burn rate $52K/month, first milestone at month 5.
**Action taken:** Negotiated a $40K "development commencement" payment at contract signing (publishers will often do this, you just have to ask) and arranged a $75K line of credit with their bank against the signed contract as collateral.
**Result:** Bridged the month 3-5 gap without burning personal savings or missing payroll. Game shipped. Studio survived.

The lesson isn't "get more money." It's that you need to model the cash timing of your deal separately from its total value. A $1M deal with bad payment timing can be more dangerous than a $600K deal with front-loaded payments.

---

## Controlling Your Burn Rate Without Killing Morale

Burn rate is monthly cash out the door. It's the number that determines how many months of runway you have at any given moment. Runway equals current cash divided by monthly burn. That's it.

Every full-time salary slot is approximately $7,000-$15,000 per month in fully-loaded cost (salary plus benefits, employer taxes, equipment, software). Contractors are often cheaper on a per-month basis for specific skills you need in short bursts, though hourly rates for experienced game contractors have climbed significantly, with senior engineers running $90-$140/hour as of this year.

What I've seen work: keep your core team small and senior. Two experienced people who own their domains will outship a team of five junior hires who need constant management, and the cash math is often better too. Hire specialists as contractors for specific production phases. Build your art pipeline, your audio, your QA to expand and contract with the production schedule, not permanently.

The thing most people don't realize is that fixed costs are what kill you in a cash crisis, not variable ones. Variable costs (contractors, third-party services, per-unit licenses) flex down when revenue is delayed. Fixed costs (full-time salaries, office leases, annual tool subscriptions) do not. Structuring your cost base to be as variable as possible without destroying team cohesion is one of the most underrated strategic decisions a studio makes.

One more thing on burn: know your "minimum viable burn" number. What's the absolute floor of spending that keeps the core team together and the project technically alive? This is your emergency number. If cash drops to three months of runway, you activate minimum viable burn immediately. You don't wait for two months. You don't have a "let's see how it goes" conversation. Three months is when you act.

---

## Revenue Diversification (The Boring Thing That Actually Works)

Single-revenue-source studios are fragile. This isn't controversial, but almost nobody acts on it early enough.

The most common model I see indie teams survive on: one or two work-for-hire contracts or game service deals to fund operations, plus active development on their own IP. The WFH money is predictable, covers base burn, and buys you time to finish the project that actually has upside. It's unglamorous and it means your release schedule slips. It also means you don't close.

Other revenue levers worth knowing about:

Kickstarter or Fig campaigns can work, but they require marketing effort that competes with development time. I'd only pursue this if you have an existing audience and a scope-appropriate goal. Studios that use crowdfunding to "validate" with a $20K campaign and then need $400K to ship are just delaying their cash problem.

Engine fund grants are genuinely underutilized. Epic Games MegaGrants (up to $500K, no equity, applications open year-round), the Canada Media Fund, Creative Europe, and state-level arts and tech grants in places like California, Texas, and New York all have real money available. The application cost is just time. I've seen studios get $25K-$150K from sources they didn't know existed because they never Googled "game development grant [their country]."

Early access revenue is real but comes with strings: community expectations, update cadence demands, and reputation risk if you go quiet. Budget the community management time honestly before you decide.

**Scenario:** Three-person studio, $180K in savings, 14 months of projected development remaining.
**Action taken:** Picked up a $120K contract porting an existing mobile title to Switch (four months of work), used that cash to extend runway to 18 months, applied for and received a $50K state digital media grant.
**Result:** Reached beta without raising outside investment or reducing scope. Studio retained full IP ownership.

---

## The Tools Worth Knowing About

A few specific recommendations for producers building financial discipline into their process:

**QuickBooks Online** ($35-$75/month) remains the standard for small studios. Integrate it with Float or Pulse for the cash flow forecasting layer. Don't just use it at tax time.

**Notion or Linear** for project tracking, but build a "financial milestones" board alongside your sprint board so payment dates and cash inflows are visible in your production calendar, not siloed in a spreadsheet nobody checks.

**Crew** and **Bonsai** for contractor contract and invoice management if you're managing 5+ contractors at once. The time saved tracking payment status is real.

For learning the finance fundamentals: "The E-Myth Revisited" by Michael Gerber is not a game dev book but I've pushed it on more studio leads than any game-specific resource because the operational thinking translates directly. For production-specific reading, "The Game Producer's Handbook" by Dan Irish (old, still relevant on financial structure) and Jason Schreier's "Blood, Sweat, and Pixels" is required reading for understanding how badly cash mismanagement has historically burned real studios.

---

## Sources

- International Game Developers Association (IGDA) Developer Satisfaction Survey: Annual survey data on studio closures, funding sources, and financial stress cited by indie developers
- Epic Games MegaGrants Program (current as of July 2026): Official documentation on grant amounts, eligibility, and application process at unrealengine.com/en-US/megagrants
- Unity Technologies Pricing Page (2026): Current per-seat pricing for Unity Pro and enterprise tiers
- Xero Small Business Insights Report: Quarterly data on cash flow patterns, late payment trends, and SMB financial health across creative industries
- "Financial Intelligence for Entrepreneurs" by Karen Berman and Joe Knight: Foundational text on the distinction between profit and cash flow, widely used in business education programs

---


*Photo: [RDNE Stock project](https://www.pexels.com/@rdne) via Pexels*