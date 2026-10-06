---
title: "How to Set Up a Build Pipeline for a Game: Unity, GitHub Actions and GameCI"
date: 2026-07-31T11:02:44.506890+00:00
lastmod: 2026-10-06
draft: false
description: "How to set up a game build pipeline step by step: choosing a CI system, a Unity walkthrough with GitHub Actions and GameCI, versioning builds for QA, and what changes for console and mobile."
image: "/img/heroes/276452.jpg"
categories: ["production"]
tags: ["build", "pipeline", "game"]
author: "Stephen Brenish"
author_slug: "stephen-brenish"
author_title: "Lead Game Producer"
author_bio: "Stephen Brenish is a Lead Game Producer at Epic Games (Fortnite, Unreal Engine) and founder of GameDevProducer, with 14+ years shipping and running live games at scale (previously Senior Program Manager at Blizzard Entertainment). Certified ScrumMaster."
slug: "how-to-set-up-a-build-pipeline-for-a-game"
affiliate_disclosure: true
faqs:
  - q: "How long does it take to set up a basic build pipeline?"
    a: "For GitHub Actions + GameCI on a Unity project, budget 1-2 days for a developer who's comfortable with YAML and has handled CI setup before. Expect 3-4 days if it's your first time. Jenkins from scratch is 3-5 days minimum."
  - q: "Do I need a build pipeline for a solo project?"
    a: "Honestly, probably not at the very start. Once you're pushing builds to playtesters more than once a week, or once you have a second person contributing code, the pipeline pays for itself almost immediately. Before that, it's optional infrastructure."
  - q: "Can I use Unity Build Automation for console platforms?"
    a: "No. Unity Build Automation (formerly Cloud Build) doesn't support console platforms (PS5, Xbox, Switch) due to NDA restrictions on the SDKs. For console, you need self-hosted runners or a vendor with console CI certification."
  - q: "How do I handle Unity license activation in CI without a Pro license?"
    a: "GameCI supports Unity Personal licenses in CI via a slightly different activation flow that generates a .alf file locally, activates it manually at Unity's license portal, and stores the resulting .ulf as a CI secret. It works, but the license is tied to a single machine ID, which can cause problems if your runner infrastructure changes. A Unity Plus or Pro license with serial-based activation is significantly less painful at scale."
  - q: "What's the cheapest way to store build artifacts long-term?"
    a: "AWS S3 with a lifecycle policy that moves builds older than 30 days to S3 Glacier is the standard approach. Storage costs drop from roughly $0.023/GB/month to $0.004/GB/month in Glacier. For a typical game dev team producing a few GB of builds per week, total artifact storage costs should be well under $20/month with a sensible retention policy."
---

Build problems quietly eat development time on almost every team: broken pipelines, manual packaging steps, and the one person who knows how to cut a release build going on vacation. The amount varies, but the category of waste is universal, and it is one of the easiest to fix.

The frustrating part? A solid build pipeline is a solved problem. The tooling exists, the patterns are documented, and it's not expensive to set up. Teams don't skip it because it's hard. They skip it because it feels like infrastructure work, and infrastructure work feels optional until it isn't.

It becomes very non-optional around month eight, when your QA lead is manually zipping builds and uploading them to Dropbox at midnight.


<div class="kt" style="margin:26px 0;padding:18px 22px;border:1px solid var(--border,#e7e5e4);border-left:4px solid var(--accent,#4338ca);border-radius:12px;background:var(--surface2,#f8fafc)"><div style="font-size:.72rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--accent,#4338ca);margin-bottom:8px">Key takeaways</div><ul style="margin:0;padding-left:1.15em"><li style="margin:5px 0">A functional CI/CD pipeline cuts release prep time from hours to under 10 minutes for most mid-size teams.</li><li style="margin:5px 0">Jenkins, GitHub Actions, and GameCI are the three setups worth evaluating; everything else is niche or legacy.</li><li style="margin:5px 0">Unity and Unreal both have cloud build options, but self-hosted runners avoid per-minute charges once you are building at volume.</li><li style="margin:5px 0">Version your builds from day one: semantic versioning tied to git tags prevents "which build did QA test?" confusion later.</li><li style="margin:5px 0">Automated build pipelines reduce "works on my machine" bugs by forcing a clean environment on every compile.</li></ul></div>


## What a Build Pipeline Actually Is (and What It Isn't)

A lot of devs conflate "build pipeline" with "CI/CD pipeline" with "deployment pipeline." They overlap, but they're not the same thing, and conflating them leads to over-engineered setups for teams that don't need them.

For a game, a build pipeline at minimum does three things: it compiles your project in a reproducible environment, packages it for one or more target platforms, and makes the output available somewhere for testing or distribution. That's it. You don't need automated deploys to Steam or continuous deployment on day one. You need a system where anyone on the team can trigger a build and get a playable artifact without touching your lead programmer's laptop.

The more ambitious version adds automated testing, platform certification checks, crash symbolication, and deployment to stores. That's the full pipeline. Most studios should build toward it incrementally, not start there.

## Choosing Your CI System

For Unity teams, the main options are GitHub Actions with GameCI, Jenkins, and Unity Build Automation (formerly Unity Cloud Build). Unreal teams more often use Jenkins, TeamCity or Horde, Epic's own build and automation system.

| System | Self-Hosted? | Cost (est.) | Unity Support | Unreal Support | Best For |
|---|---|---|---|---|---|
| GitHub Actions + GameCI | Both | Free hosted minutes, then per-minute; no per-minute charge on self-hosted runners | Strong | Limited | Teams already on GitHub |
| Jenkins | Yes | Infrastructure cost only | Manual setup | Manual setup | Studios wanting full control |
| Unity Build Automation | No | Free monthly minutes, then usage-based | Native | No | Unity teams, small budgets |
| Horde | Yes | Infrastructure cost only | No | Native | Unreal teams wanting Epic's own tooling |
| TeamCity | Both | Free tier, then licensed | Via scripts | Strong | Larger teams, especially on Unreal |

My honest take: for most indie and mid-size studios on Unity, GitHub Actions plus GameCI is the right answer. GameCI is an open-source project that handles Unity licensing, platform-specific build steps, and caching in pre-built Docker images. It saves days of configuration work, and the documentation is legitimately good.

Jenkins is powerful and free, but you're on your own for maintenance. If you already have someone with DevOps experience on staff, it's worth considering. If you don't, you'll spend more time running your pipeline than using it.

## The Actual Setup: Step by Step

Here's a concrete walkthrough for a Unity project on GitHub Actions with GameCI, which is what I'd recommend for most readers here.

**Step 1: Activate your Unity license for CI.** GameCI requires a valid Unity license. Run `docker run -it unityci/unity unity -batchmode -quit -createManualActivationFile` to generate a `.alf` file, activate it at license.unity3d.com, and store the resulting `.ulf` as a GitHub Actions secret. This is the step everyone forgets to document, and it bites you when the license expires mid-project.

**Step 2: Create your workflow file.** In `.github/workflows/build.yml`, define triggers (push to main, pull request, manual dispatch), the Unity version, and target platforms. GameCI's documentation has copy-paste YAML for Windows, macOS, iOS, Android, and WebGL builds.

**Step 3: Cache your Library folder.** The Library folder in Unity is regenerated on every clean build, which can add 10-25 minutes to build times depending on project size. GameCI supports caching it between runs via GitHub's cache action. On a project of any size, this is usually the single biggest speedup available.

**Step 4: Set up artifact storage.** By default, GitHub Actions can store artifacts for 90 days. For a game studio, you probably want builds to go somewhere more structured: an S3 bucket, a self-hosted Artifactory instance, or a service like itch.io (for dev builds) or a private Steam branch (for playtesting). Configure the upload step to name artifacts with a version string tied to the git commit SHA.

**Step 5: Add a notification hook.** Slack or Discord webhook at the end of the pipeline, success or failure, with the download link. This is optional but your team will actually use builds if they appear in chat. It sounds small. It changes behavior significantly.

**Step 6: Iterate.** Don't try to add automated testing, lint checks, and platform cert validation all at once. Get the basic build working first, then layer.





## Versioning, Artifacts, and the QA Problem

A common early mistake is producing builds without versioning them systematically. QA files a bug, someone asks "which build?", the answer is "the one from Tuesday," and that answers exactly nothing.

Version your builds from the first pipeline run. The pattern I use is `MAJOR.MINOR.PATCH.BUILD` where BUILD is an auto-incrementing integer tied to your CI run number. Tie MAJOR.MINOR.PATCH to git tags. Your YAML can read the current git tag and inject it into the game's version string at build time, which means every build in the game's own UI shows the version. QA can screenshot a bug and the version is right there.

**Illustration:** a six-person PC team where the lead programmer builds by hand, spending most of an hour on each build including packaging and uploading. With GitHub Actions, GameCI and artifact storage, every push to `develop` produces a versioned build with nobody touching it, and a chat notification carries the download link. A couple of days of setup pays for itself within weeks, because the team's most expensive engineer gets hours back every week.

## Platform-Specific Complications

Console builds are a different category entirely. If you're building for PS5, Xbox Series, or Switch, you're working with NDA-gated SDKs that can't go in public repositories or run on standard cloud runners. In practice that means self-hosted build machines you control, set up under each platform holder's rules for SDK access. Check the platform holders' developer documentation before you put any console SDK on cloud infrastructure.

Mobile has its own complexity. iOS builds require macOS runners and a valid Apple developer certificate. Storing that certificate securely as a GitHub Actions secret requires a bit of care: use Fastlane's Match tool to manage certs and provisioning profiles via an encrypted repository, and reference them in CI. Android is more straightforward, just a keystore file stored as a secret.

WebGL is the easiest. It's a straightforward Unity build target with no special signing requirements, and you can auto-deploy to a GitHub Pages branch or an itch.io project with a simple upload step.

## Sources

- [GameCI Documentation](https://game.ci/docs): Official docs for the open-source Unity/Unreal CI toolset; covers Docker images, licensing, and platform-specific build configuration
- [GitHub Actions pricing page](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions): Current per-minute pricing for hosted runners; self-hosted runner costs depend on your infrastructure
- [Unity support: Understanding Unity DevOps charges](https://support.unity.com/hc/en-us/articles/34748492914964-Understanding-Unity-DevOps-charges): Pricing and free allowances for Unity Build Automation and Version Control
- [Epic Games: Horde in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-in-unreal-engine): Epic's build automation and CI system for Unreal projects

---


*Photo: [Pixabay](https://www.pexels.com/@pixabay) via Pexels*