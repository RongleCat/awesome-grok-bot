<h1 align="center">
  <img src="./assets/banner.png" alt="Awesome Grok Bot" width="800" />
</h1>

<p align="center">
  <a href="./README.zh.md"><strong>中文</strong></a>
  ·
  <a href="./prompts/playbook-prompts.md">Playbook prompts</a>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <img src="https://img.shields.io/badge/entries-88-blueviolet" alt="Entry count" />
  <img src="https://img.shields.io/badge/Grok%20Bot-beta%20(2026--08--11)-informational" alt="Grok Bot status" />
  <img src="https://img.shields.io/badge/license-CC0-lightgrey" alt="License" />
</p>

<p align="center">
  <a href="https://grok-app.com"><strong>Grok App</strong></a> (<a href="https://github.com/RongleCat/grok-app">GitHub</a>) — open-source Grok Build desktop app · <a href="https://x.com/cgnot996">铁柱AGI @cgnot996</a>
</p>

<p align="center">Scan the group QR to join, or add me as a friend and I will pull you in.</p>
<p align="center">
  <img src="./assets/wechat/group-qr.jpg" alt="Grok Bot WeChat group" width="140" />
  &nbsp;&nbsp;&nbsp;
  <img src="./assets/wechat/personal-qr.png" alt="Add 铁柱AGI on WeChat" width="140" />
</p>
<p align="center"><sub>WeChat group (valid until Aug 27) · Add friend</sub></p>

> Grok Bot is the always-on AI teammate launched 2026-08-11 by xAI/SpaceXAI with Cursor. Each Bot shares one persistent cloud computer (browser, files, terminal) and keeps working after you close the laptop. It is not grok.com chat, Grok Imagine, or a Grok 4.x model writeup. Unofficial community list, not affiliated with xAI or Cursor.

## Contents

- [Official Resources](#official-resources)
- [Tutorials & Guides](#tutorials--guides)
- [Field Cases](#field-cases)
- [Skills, Plugins & MCP](#skills-plugins--mcp)
- [Reviews & Comparisons](#reviews--comparisons)
- [Open-Source Alternatives](#open-source-alternatives)
- [Community & Failure Modes](#community--failure-modes)
- [Related Lists](#related-lists)
- [Contributing](#contributing)

## Official Resources

- [Introducing Grok Bot](https://x.ai/news/introducing-grok-bot) - Launch note: always-on agents with their own computer, working inside your tools 24/7.
- [Grok Bot overview](https://docs.x.ai/grok-bot/overview) - Canonical product page: one named Bot, one shared cloud computer, isolation is per user not per Bot.
- [Get started](https://docs.x.ai/grok-bot/get-started) - Install desktop, sign in with Cursor, create the first Bot. No official Linux desktop.
- [Use cases](https://docs.x.ai/grok-bot/use-cases) - Official roster ideas: sales CRM nights, ops invoices, engineering bug squash.
- [Grok Bot for iOS](https://docs.x.ai/grok-bot/mobile) - Companion phone app for messaging Bots that keep running on the cloud machine.
- [Create and manage Bots](https://docs.x.ai/grok-bot/bots) - How a Bot is named, scoped, and kept as a standing coworker instead of a chat thread.
- [Message and collaborate](https://docs.x.ai/grok-bot/chat-and-collaboration) - Bots message each other, join group chats, and assign ownership of work.
- [Files and results](https://docs.x.ai/grok-bot/files-and-results) - Where artifacts live on the shared computer and how you pull results back.
- [Use the computer and apps](https://docs.x.ai/grok-bot/computer-and-apps) - Browser, filesystem, terminal. No clean API? Click the site like a person.
- [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations) - Teach a task (up to 10 minutes of screen, no mic), save as a reusable routine.
- [Settings and notifications](https://docs.x.ai/grok-bot/settings-and-notifications) - Notification grouping, mobile alerts, and how Bots follow up stalled work.
- [Approvals, security, and privacy](https://docs.x.ai/grok-bot/approvals-security-and-privacy) - Bots do not see passwords; draw the approval line on irreversible actions and 2FA takeover.
- [Teams and enterprises](https://docs.x.ai/grok-bot/teams-and-enterprises) - Team marketplace, SSO, shared analytics. Plugins follow existing Cursor policy.
- [Troubleshooting](https://docs.x.ai/grok-bot/troubleshooting) - Official fix list for reconnect, runners, and common beta failures.
- [FAQ](https://docs.x.ai/grok-bot/faq) - Short official answers on access, computer sharing, and what Bots can remember.
- [Get access with SuperGrok Heavy](https://cursor.com/help/grok-bot/supergrok-heavy) - Cursor help: Heavy / Ultra / Teams Premium gates, and Ultra does not stack twice.
- [Grok Bot on mobile (Cursor help)](https://cursor.com/help/grok-bot/mobile) - How the iOS companion talks to Bots that stay on the cloud computer.
- [Connect plugins](https://cursor.com/help/grok-bot/connect-plugins) - Prefer a plugin; fall back to the cloud browser when the connector is missing.
- [Store secrets securely](https://cursor.com/help/grok-bot/secrets) - Use the secret card. Never paste API keys into the Bot chat.
- [Grok Bot on the App Store](https://apps.apple.com/us/app/grok-bot/id6794501026) - Official iOS listing for the companion app.
- [xAI plugin marketplace](https://github.com/xai-org/plugin-marketplace) - Official .grok-plugin marketplace Grok Bot inherits under Cursor plugin policy.

## Tutorials & Guides

- [How to Get Started with Grok Bot](https://debbie.codes/blog/how-to-get-started-with-grok-bot) - Debbie's field guide: first Bot, CoS prompt, and how she reorganizes the roster.
- [Grok Bot Masterclass](https://www.dailydoseofds.com/p/grok-bot-masterclass/) - Avi / Daily Dose: record once, turn it into a skill, hang it on a routine.
- [How to Set Up Grok Bot and Build Your First AI Agents](https://www.mindstudio.ai/blog/grok-bot-setup-guide) - Install-to-first-agent walkthrough with the Heavy / Ultra / Teams gates called out.
- [Grok Bot Explained](https://www.ayautomate.com/blog/grok-bot-xai-ai-agents-explained) - Clear explainer with a real iPhone screenshot of a Bot roster.
- [Hand Off Real Work Across Your Apps](https://app.therundown.ai/guides/hand-off-real-work-across-your-apps-with-grok-bot) - The Rundown's how-to for handing multi-app jobs to a Bot.
- [Connect Multiple Slack Workspaces](https://www.usecarly.com/blog/how-to-connect-multiple-slack-workspaces-to-grok-bot/) - Slack event wake-up is not the same as installing Grok Bot as a Slack App.
- [Peter Yang: 5 Must-Try Use Cases](https://www.youtube.com/watch?v=MkVcHbviYOw) - Advisor, YouTube researcher, X scout, Gmail declutter, travel concierge.
- [Alex Finn: setup that actually sticks](https://www.youtube.com/watch?v=vrgO4D_mUlA) - Long-form setup from someone already living on Cursor Cloud Agents.
- [Nate Herk: Grok Bot is For Real](https://www.youtube.com/watch?v=PQBYZQqan2g) - Install-first agent pitch plus what the $200 seat actually buys.
- [Teach a task by screen recording](https://x.com/_avichawla/status/2089817006065496530) - Official-adjacent tip: show the workflow once, Bot writes the skill.
- [Use the remote computer from your phone](https://x.com/bot/status/2089802847223468116) - @bot QoL: drive the cloud machine from iOS without opening the laptop.
- [Uncle-Gizmo notes](https://github.com/Uncle-Gizmo/grok-bot-info) - Public notes on safe example workflows and how Bot sits next to Grok Build.

## Field Cases

- [n2parko: CoS + EM + five eng ICs + Databricks + PM](https://x.com/n2parko/status/2087251704744235298) - SpaceXAI product roster with real agent-to-agent PR handoff screenshots.
- [Lee Robinson: four technical bets](https://x.com/leerob/status/2089169319099777364) - No UI, thin client / thick server, always-on computer, browser as a first-class tool.
- [Debbie: book my flights](https://debbie.codes/blog/i-tested-if-grok-bot-could-book-my-flights) - Honest near-miss: the Bot can drive the airline site, the last click still needs you.
- [Debbie: buy gluten-free beer on a Sunday night](https://debbie.codes/blog/i-sent-grok-bot-to-buy-my-gluten-free-beer) - CoS shopping run — the fun case that shows computer-use, not chat.
- [Yun-Ta: calendar + reservations while walking](https://x.com/yunta_tsai/status/2087415205756391461) - Mixed Chinese/English voice, Bot scans calendars and books a table.
- [Gota: twelve jobs on one roster](https://x.com/gota_bara/status/2087666940450152841) - Image factory, research briefs, 3D, travel debate, cancel subscriptions, local LLM on the VM.
- [Box: credit-committee pack](https://x.com/Box/status/2087275866950938662) - Reconcile materials, write the pack back into Box via MCP.
- [WordPress updates taught once](https://x.com/mrfundman/status/2089760255890571404) - Teach-a-task on a real CMS instead of writing a deploy script.
- [Arduino updates from a Bot](https://x.com/KettlebellDan/status/2089920364419874937) - Bot pushes hardware updates so the human can stay off X.
- [Nate: twelve Bots in eight hours](https://natesnewsletter.substack.com/p/grok-bot-review) - Is the $200 agent team worth it — with a real first-day roster.
- [24/7 support agent in 19 minutes](https://www.youtube.com/watch?v=bUALqTpUze0) - Customer-support Bot built on a routine, not a helpdesk rewrite.
- [Farzad roster: Webby / Shotry / Writey](https://x.com/farzyness/status/2087340859138224540) - Named specialists plus an orchestrator — the pattern that keeps showing up.
- [Sid: Polymarket daily settlement brief](https://x.com/sidshekhar24/status/2089735218861326727) - Bot scans the day's settled markets and writes the report.
- [Logan: the unlock is the computer, not 4.6](https://x.com/LoganJastremski/status/2089903051557491092) - No API, no MCP, no hosted browser — the Bot just uses software like a person.
- [Japanese note group: cloud-computer field notes](https://note.com/azumimusuhi/n/n0485219790bb) - Hands-on JP writeup of living on the shared VM for a week.

## Skills, Plugins & MCP

- [grokbot-imessage-skill](https://github.com/jeffhuber/grokbot-imessage-skill) - Read, triage, and send iMessage from the Bot via a local macOS helper.
- [Grok Bot Discord gateway](https://github.com/davefmurray/grok-bot-discord) - Bridge so a Bot can live in Discord without pretending to be a Slack App.
- [Werewolf gamemaster skill](https://github.com/Heyvhuang/werewolf-gamemaster) - A real skill pack: the Bot runs a Werewolf table, not a hello-world SKILL.md.
- [Hyperliquid 7-agent trading desk](https://github.com/galleonlabs/hypergrok-trading-desk) - Seven specialized Bots on one desk — treat as experimental, read the code first.
- [awesome-grok-bot-plugins](https://github.com/rdmgator12/awesome-grok-bot-plugins) - 219 in-app marketplace listings captured 2026-08-12, grouped by category.
- [superpowers (marketplace)](https://github.com/obra/superpowers) - Largest general skill collection in the official marketplace: plan, debug, write.
- [chrome-devtools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) - Drive a live Chrome: traces, network, source-mapped console errors.
- [Vercel plugin](https://github.com/vercel/vercel-plugin) - Deployments, logs, domains. Pair with the forum thread on OAuth redirect failures.

## Reviews & Comparisons

- [The Verge: an AI teammate you can assign work](https://www.theverge.com/ai-artificial-intelligence/978666/spacexai-grok-bot-ai-agent-beta-launch) - Launch coverage that keeps the product distinct from grok.com chat.
- [VentureBeat: persistent digital coworkers](https://venturebeat.com/orchestration/spacexais-grok-bot-turns-agents-into-persistent-digital-coworkers-that-can-operate-your-apps-for-120-per-month) - Pricing and persistence: $120/seat Teams path, computer stays on.
- [Lenny's Newsletter: Grok Bot, Grok 4.6, and Cursor](https://www.lennysnewsletter.com/p/i-tested-grok-bot-grok-46-and-cursor) - Separates the Bot product from the 4.6 model — do not collapse the two.
- [Grok Bot vs OpenClaw](https://myclaw.ai/blog/grok-bot-vs-openclaw) - Managed cloud computer vs self-hosted, bring-your-own-model.
- [Grok Bot vs OpenClaw vs ChatGPT](https://www.mindstudio.ai/blog/grok-bot-vs-openclaw-chatgpt) - Three-way: always-on VM, self-host, and chat-with-tools.
- [Grok Bot vs ChatGPT for work](https://www.eigent.ai/blog/grok-bot-vs-chatgpt-work) - Computer-use coworker vs a chat that sometimes calls tools.
- [Grok Bot vs Claude Cowork](https://www.eigent.ai/blog/grok-bot-vs-claude-cowork) - Persistent shared VM vs session-scoped cowork.
- [YouTube: Grok Bot vs OpenClaw and Hermes](https://www.youtube.com/watch?v=sAoTrUijP4g) - Video bake-off of the three agent stacks people actually compare.
- [10 Best Grok Bot Alternatives (2026)](https://www.vellum.ai/blog/best-grok-bot-alternatives) - Landscape of substitutes if you do not want the Heavy/Ultra seat.
- [Before You Hire a $200 Grok Bot](https://zchmael.substack.com/p/before-you-hire-a-200-grok-bot-ai) - Skeptical checklist: what the seat does not buy you.

## Open-Source Alternatives

- [rakazo](https://github.com/elie222/rakazo) - Open-source Grok Bot alternative — self-host the always-on teammate idea.
- [guaca](https://github.com/madebywelch/guaca) - Another self-hosted take on persistent computer-use agents.
- [OpenGrokBot](https://github.com/wolfqing/OpenGrokBot) - OpenClaw plus bring-your-own-model, assembled as a Bot stand-in.
- [XinyunOpenBot](https://github.com/dongpen-max/XinyunOpenBot) - Chinese-language open alternative aimed at the same job-to-be-done.
- [OpenMausBot](https://github.com/milind-soni/OpenMausBot) - Community runtime exploring the same always-on computer pattern.
- [open-grokbot](https://github.com/ishandutta2007/open-grokbot) - Early equivalent / experiment — read before you grant credentials.
- [grok-bot-flake](https://github.com/jordangarrison/grok-bot-flake) - Nix flake that repackages the official Linux .deb (no source build).

## Community & Failure Modes

- [Forum: Introducing Grok Bot](https://forum.cursor.com/t/introducing-grok-bot/168053) - Launch thread: what people actually asked in the first 48 hours.
- [Bots are not a security boundary](https://forum.cursor.com/t/grok-bot-ship-real-session-fences-bots-are-not-a-security-boundary/168476) - Must-read: every Bot on the account sees the same logins and files.
- [Always-on workers vs topic threads](https://forum.cursor.com/t/grok-bots-as-always-on-workers-vs-topic-threads/168183) - Community consensus: a Bot is a standing coworker, not a chat tab.
- [Free Cursor Ultra with Grok (Heavy bundle)](https://forum.cursor.com/t/free-cursor-ultra-with-grok/168286) - How SuperGrok Heavy maps onto Ultra + Bot, and what does not stack.
- [Reconnect issue](https://forum.cursor.com/t/grok-bot-reconnect-issue/168500) - Real screenshot of “can't reach your computer” after a reconnect.
- [X login lock on the Bot computer](https://forum.cursor.com/t/grok-bot-x-login-lock-limit-not-lifting/168541) - Cloud computers hit site risk controls. X locks are not theoretical.
- [ExternalShell blocked despite Always allow](https://forum.cursor.com/t/grok-bot-externalshell-blocked-despite-always-allow/168180) - Allow-lists still fail. Do not assume Always allow means always.
- [Deleted Cursor account orphans the Grok link](https://forum.cursor.com/t/deleted-cursor-account-leaves-grok-link-orphaned-and-blocks-relinking/168783) - Account deletion can pin the Bot to a dead Cursor identity.
- [Hacker News discussion](https://news.ycombinator.com/item?id=49261514) - HN thread on the launch — useful for the skeptical read.
- [Native desktop on Arch / Linux](https://forum.cursor.com/t/native-grok-bot-desktop-app-for-arch-linux-and-linux-generally/168084) - Linux desktop is not first-class; this is the request plus community packs.

## Related Lists

- [ZeroPointRepo/awesome-grok-bot](https://github.com/ZeroPointRepo/awesome-grok-bot) - Day-one 19-entry directory, strong on marketplace format and self-hosted runtimes.
- [awesome-workbuddy](https://github.com/staruhub/awesome-workbuddy) - Curated WorkBuddy resources — another always-on work-agent directory.
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - MCP server catalog. Grok Bot follows Cursor plugin/MCP policy.
- [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Skill-format sibling ecosystem; many SKILL.md packs are conceptually portable.
- [botdirectory.ai (announced)](https://x.com/aiedge_/status/2089895147068924385) - Community directory of live Bots — treat the site as beta.

## Contributing

88 curated entries across 8 sections. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR: the resource must be about Grok Bot the cloud-computer teammate, the link must work, and the blurb is one sentence ending with a period.

---

<p align="center">Unofficial community list. Not affiliated with xAI/SpaceXAI or Cursor. List content <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>.</p>
