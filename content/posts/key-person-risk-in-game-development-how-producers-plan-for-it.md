---
title: "Key Person Risk in Game Development: How Studios Protect Projects"
date: 2026-11-24T19:35:08.963121+00:00
draft: false
description: "Learn how game development studios identify and mitigate key person risk through succession planning, documentation, and team redundancy strategies."
image: "/img/heroes/6804084.jpg"
categories: ["industry intel"]
tags: ["person", "risk", "game", "development", "producers"]
author: "Stephen Brenish"
author_slug: "stephen-brenish"
author_title: "Lead Game Producer"
author_bio: "Stephen Brenish is a Lead Game Producer at Epic Games (Fortnite, Unreal Engine) and the founder of GameDevProducer. Across 14+ years in game production he has shipped and operated live titles at scale, previously as a Senior Program Manager at Blizzard Entertainment. Certified ScrumMaster."
slug: "key-person-risk-in-game-development-how-producers-plan-for-it"
affiliate_disclosure: true
faqs:
  - q: "What's a 'bus factor' and how does it relate to key person risk?"
    a: "Bus factor (sometimes called lottery factor) is the number of team members who would need to be hit by a bus before a project is in serious trouble. A bus factor of one means a single person's absence cripples the project. It's the same concept as key person risk, just expressed as a team-level metric rather than an individual one. Tracking it per system or feature is a quick way to surface concentrations."
  - q: "How often should a producer review key person risk?"
    a: "At a minimum, revisit it at every major milestone and after any team composition change. For projects in active production, a quarterly review of your documentation coverage and succession status is a reasonable cadence."
  - q: "Should you tell a key person that they're considered a key person risk?"
    a: "This depends on context, but in most cases, yes. Framing it as 'we're investing in documentation and cross-training because your domain is critical' is honest and usually well-received. It also signals that the studio takes continuity seriously, which can itself be a mild retention signal."
  - q: "Does key person risk apply to leadership as well as individual contributors?"
    a: "Absolutely. A game director or creative director who is the sole author of the product vision is a key person risk. So is a producer who is the only person with relationships to key platform partners. Leadership key persons are often harder to mitigate because the knowledge is relational and contextual, not just technical."
  - q: "How do you handle key person risk with a very small team (under 10 people)?"
    a: "Smaller teams have higher bus factors almost by definition. The practical mitigation shifts toward documentation quality and transparent communication over succession pairing, since there may not be anyone with bandwidth to serve as a backup. Recorded video walkthroughs of core systems are a low-overhead option that scales well for small teams."
---

Key person risk doesn't get enough airtime until someone quits mid-production. Then it becomes the only thing anyone wants to talk about.

A "key person" is any individual whose absence would materially delay your schedule, degrade your product quality, or require months to replace. In game dev, that's a wider group than most leads admit: the senior engineer who owns your custom physics layer, the tech artist bridging art and pipeline, the narrative director who holds the entire lore bible in their head. Losing one of them without a plan doesn't just slow you down. It can sink a game that was otherwise on track.

The good news is that producers can plan for this systematically. It's not dramatic. It's documentation, cross-training, and honest conversation with your team and your leadership about where your single points of failure actually live.


<div class="kt" style="margin:26px 0;padding:18px 22px;border:1px solid var(--border,#e7e5e4);border-left:4px solid var(--accent,#4338ca);border-radius:12px;background:var(--surface2,#f8fafc)"><div style="font-size:.72rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--accent,#4338ca);margin-bottom:8px">Key takeaways</div><ul style="margin:0;padding-left:1.15em"><li style="margin:5px 0">Any team member whose absence stalls your schedule for 2+ weeks qualifies as a key person risk.</li><li style="margin:5px 0">Documentation coverage and cross-training reduce replacement ramp time from months to weeks.</li><li style="margin:5px 0">Studios should identify key persons formally at project kickoff, not after the first resignation letter.</li><li style="margin:5px 0">Succession pairing (designating a backup for each critical role) is the most practical mitigation for small teams.</li><li style="margin:5px 0">Key person risk applies equally to contractors and freelancers, often more so, because the relationship is easier to end.</li></ul></div>


## How to Actually Identify Your Key Persons

Most teams skip the formal step and assume they already know. Sometimes they do. But the exercise of actually listing every critical dependency forces you to be honest about concentrations of knowledge you've normalized.

A practical starting point: map your critical path tasks (if you're already running a schedule, something like the [Schedule & Milestone Planner](/game-development-schedule-planner/) gives you a structured place to do this), then ask who is the sole owner of each one. If the answer to "who else can do this?" is "nobody" or a long pause, that's your key person.

Three signals that someone qualifies:

- They're the only person who can interpret, fix, or extend a core system without a full re-read of documentation they wrote themselves.
- Their departure would trigger a knowledge-transfer effort measured in weeks, not days.
- Other team members route critical questions through them as a default, even when they don't have to.

Don't forget contractors and freelancers. A freelance composer who holds exclusive rights to the game's soundtrack format and all working sessions is a key person. So is the porting specialist you hired to handle console certification on a fixed contract. The employment relationship doesn't change the dependency.

## The Real Cost of Doing Nothing

**Example:** Assume a 20-person studio, 18 months into a 24-month project. The lead gameplay programmer has a 6-month ramp time (conservative for a mid-sized codebase with limited documentation). If they depart, the realistic best case is a 10-week delay while a replacement is sourced, onboarded, and brought up to speed on the architecture, assuming you can find someone. At a studio burn rate of $200,000/month (a rough mid-tier figure, adjust to your actuals), that's $500,000 in unplanned cost before you count the morale impact on the remaining team or the platform cert deadline you've now missed.

The delay cost is usually larger than the mitigation cost. That's the number to put in front of your executive producer or investors.

## Mitigation Strategies That Actually Work

The approaches below are roughly ordered by effort required, not by importance. All of them matter.

**Documentation coverage audits.** Once per quarter, review which systems have no written runbook and no secondary owner. A simple spreadsheet with columns for "system name," "primary owner," "secondary owner," and "documentation status" is enough. It's unglamorous and it works.

**Succession pairing.** For every critical role, designate a backup who gets regular exposure to that domain. This isn't about overloading a junior dev with documentation they'll never read. It means the designated backup attends key design sessions, reviews commits, and pairs on complex tasks monthly. When something goes wrong, they're already partially oriented.

**Knowledge transfer as sprint work.** Treat documentation and cross-training as first-class sprint tasks with estimates and acceptance criteria. If it only happens when someone announces they're leaving, it's already too late to get the depth you need.

**Contract protections for external dependencies.** If a contractor holds the only working version of a critical system, your contract should require source code escrow or handoff deliverables at defined milestones. This is not unusual to request; most experienced contractors expect it.

**Retention investment.** Sometimes the cheapest mitigation is just not losing the person. Competitive comp, meaningful work, psychological safety, a roadmap for growth. None of these are magic, but chronic turnover in key roles is usually a signal of something producible.

## Effort vs. Protection: What Each Mitigation Actually Buys You

| Mitigation | Effort to Implement | Reduction in Replacement Ramp Time | Works for Contractors? |
|---|---|---|---|
| Runbook / technical documentation | Medium (ongoing) | 30-50% | Yes |
| Succession pairing | Medium (ongoing) | 40-60% | Partially |
| Recorded architecture walkthroughs | Low (one-time + updates) | 20-35% | Yes |
| Source code escrow for contractors | Low (contractual) | N/A (preserves access) | Yes |
| Retention / comp review | High (org-wide) | Prevents the event entirely | Partially |
| Bus factor tracking in sprint board | Low (visibility only) | Indirect | Yes |

These are directional, not precise. Ramp time reduction depends heavily on the complexity of the domain and the experience level of the backup.

## What to Tell Leadership

Producers sometimes soft-pedal this conversation because it feels morbid or disloyal. Don't. Frame it correctly: key person planning is schedule [risk management](/posts/risk-management-in-game-production-explained/), the same category as dependency delays or platform cert risk. It belongs in your risk register.

If your studio doesn't have a formal risk register, start one. Document the key person, the nature of the dependency, the current mitigation status, and an estimated delay impact if the risk materializes. Review it at major milestones. When a dependency is resolved (documentation is in place, a backup is trained), update the register. It becomes your paper trail that you were managing this proactively.

---

## Sources

- [International Game Developers Association (IGDA)](https://www.igda.org/): Developer satisfaction surveys and workforce research relevant to retention and burnout.
- [Project Management Institute (PMI)](https://www.pmi.org/): Risk management frameworks including risk registers and risk response planning (PMBOK Guide).
- [Game Developers Conference (GDC) Vault](https://www.gdcvault.com/): Talks on team structure, production process, and technical documentation practices in game development.
- [Gamasutra / Game Developer Magazine](https://www.gamedeveloper.com/): Postmortems and production articles covering team dependency failures and mitigation approaches.

---


*Photo: [cottonbro studio](https://www.pexels.com/@cottonbro) via Pexels*