<h1 align="center">
  <img src="./assets/banner.png" alt="Awesome Grok Bot" width="800" />
</h1>

<p align="center">
  <a href="./README.md"><strong>English</strong></a>
  ·
  <a href="./prompts/playbook-prompts.json">玩法提示词</a>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <img src="https://img.shields.io/badge/entries-88-blueviolet" alt="Entry count" />
  <img src="https://img.shields.io/badge/Grok%20Bot-beta%20(2026--08--11)-informational" alt="Grok Bot status" />
  <img src="https://img.shields.io/badge/license-CC0-lightgrey" alt="License" />
</p>

> **Grok Bot** 生态精选清单：官方文档、真实案例、教程、插件与开源替代。Grok Bot 是 xAI/SpaceXAI 与 Cursor 在 2026-08-11 上线的 always-on 云电脑队友。

Grok Bot 是 2026-08-11 由 xAI/SpaceXAI 与 Cursor 上线的 always-on 云电脑队友。每个 Bot 共享一台持久云电脑（浏览器、文件、终端），合上笔记本也不停。它不是 grok.com 聊天、Grok Imagine，也不是 Grok 4.x 模型评测。

用上面的 **English** 链接切回英文。

本清单**不是** grok.com 聊天、Grok Imagine 或 Grok 4.x 模型评测。**与 xAI / Cursor 无官方关系。**

## 目录

- [玩法（先读这段）](#玩法（先读这段）)
- [官方资源](#官方资源)
- [教程与上手指南](#教程与上手指南)
- [真实使用案例](#真实使用案例)
- [技能、插件与 MCP](#技能、插件与-mcp)
- [评测与对比](#评测与对比)
- [开源替代](#开源替代)
- [社区与故障现场](#社区与故障现场)
- [相关列表](#相关列表)
- [贡献](#贡献)

## 玩法（先读这段）

从本地 175 条过关材料里收出来的判断，是经验不是厂商 Canon。

1. **一台电脑，不是一人一机。** 登录和文件对账号下全部 Bot 可见。
2. **审批线画在不可逆动作上。** Auto Review + 2FA Take over。
3. **云电脑会撞上站点风控。** X 登录锁、验证码在真实帖里反复出现。
4. **重连会丢状态。** 重建桥或删 Cursor 号可能把 Bot 绑死。
5. **Heavy / Ultra / Teams Premium 是门槛不是无限。** 用量按周重置。
6. **Linux 桌面不是一等公民。** 社区有 `.deb` / Nix；官方桌面是 macOS / Windows + iOS。

反复出现的最小编制：幕僚长、只读收件箱、研究侦察、工程复现、值班客服。先只读，再 Teach，再挂 routine。可粘贴提示词见 [`prompts/playbook-prompts.json`](prompts/playbook-prompts.json)。

## 官方资源

- [Introducing Grok Bot](https://x.ai/news/introducing-grok-bot) - 首发稿：always-on 智能体自带电脑，在你的工具里 24/7 干活。.
- [Grok Bot overview](https://docs.x.ai/grok-bot/overview) - 产品总览：有名字的 Bot、共享一台云电脑；隔离按账号不按 Bot。.
- [Get started](https://docs.x.ai/grok-bot/get-started) - 装桌面端、用 Cursor 登录、建第一个 Bot。官方无 Linux 桌面。.
- [Use cases](https://docs.x.ai/grok-bot/use-cases) - 官方编制示例：销售夜间更 CRM、运营发票入职、工程复现 Bug。.
- [Grok Bot for iOS](https://docs.x.ai/grok-bot/mobile) - iOS 同伴 App：在手机上给仍在云电脑上干活的 Bot 发消息。.
- [Create and manage Bots](https://docs.x.ai/grok-bot/bots) - 怎么给 Bot 起名、定工种，把它当常驻同事而不是话题线程。.
- [Message and collaborate](https://docs.x.ai/grok-bot/chat-and-collaboration) - Bot 互发消息、进群聊、互相派活和认领。.
- [Files and results](https://docs.x.ai/grok-bot/files-and-results) - 产物落在共享电脑哪里，以及怎么把结果拿回来。.
- [Use the computer and apps](https://docs.x.ai/grok-bot/computer-and-apps) - 浏览器、文件系统、终端。没有干净 API 就用云浏览器点。.
- [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations) - Teach a task（最多录 10 分钟屏幕、不录麦），存成可复用 routine。.
- [Settings and notifications](https://docs.x.ai/grok-bot/settings-and-notifications) - 通知按 Bot 分组、手机提醒，以及 Bot 怎么跟未完成的活。.
- [Approvals, security, and privacy](https://docs.x.ai/grok-bot/approvals-security-and-privacy) - Bot 看不见密码；审批线画在不可逆动作和 2FA Take over 上。.
- [Teams and enterprises](https://docs.x.ai/grok-bot/teams-and-enterprises) - 团队市场、SSO、共享用量。插件策略跟现有 Cursor 政策走。.
- [Troubleshooting](https://docs.x.ai/grok-bot/troubleshooting) - 官方排障：重连、runner 挂掉、常见 beta 故障。.
- [FAQ](https://docs.x.ai/grok-bot/faq) - 官方短答：资格、共享电脑、Bot 记得什么。.
- [Get access with SuperGrok Heavy](https://cursor.com/help/grok-bot/supergrok-heavy) - Cursor 帮助：Heavy / Ultra / Teams Premium 门槛；已在 Ultra 再绑不叠用量。.
- [Grok Bot on mobile (Cursor help)](https://cursor.com/help/grok-bot/mobile) - iOS 同伴怎么跟仍在云电脑上的 Bot 说话。.
- [Connect plugins](https://cursor.com/help/grok-bot/connect-plugins) - 优先插件；没有连接器就退回云浏览器。.
- [Store secrets securely](https://cursor.com/help/grok-bot/secrets) - 密钥走 secret card，禁止把 Key 贴进聊天。.
- [Grok Bot on the App Store](https://apps.apple.com/us/app/grok-bot/id6794501026) - 官方 iOS 同伴 App 商店页。.
- [xAI plugin marketplace](https://github.com/xai-org/plugin-marketplace) - 官方 .grok-plugin 市场；Grok Bot 沿用 Cursor 插件政策。.

## 教程与上手指南

- [How to Get Started with Grok Bot](https://debbie.codes/blog/how-to-get-started-with-grok-bot) - Debbie 上手：第一个 Bot、CoS prompt、怎么重组编制。.
- [Grok Bot Masterclass](https://www.dailydoseofds.com/p/grok-bot-masterclass/) - Avi / Daily Dose：录一遍变 skill，再挂 routine，笔记本合上仍跑。.
- [How to Set Up Grok Bot and Build Your First AI Agents](https://www.mindstudio.ai/blog/grok-bot-setup-guide) - 从安装到第一个 Agent，并写清 Heavy / Ultra / Teams 门槛。.
- [Grok Bot Explained](https://www.ayautomate.com/blog/grok-bot-xai-ai-agents-explained) - 讲清楚产品是什么，并带真实 iPhone 编制截图。.
- [Hand Off Real Work Across Your Apps](https://app.therundown.ai/guides/hand-off-real-work-across-your-apps-with-grok-bot) - The Rundown：怎么把跨应用的活交给 Bot。.
- [Connect Multiple Slack Workspaces](https://www.usecarly.com/blog/how-to-connect-multiple-slack-workspaces-to-grok-bot/) - Slack 事件唤醒 routine ≠ 把 Grok Bot 装成 Slack App。.
- [Peter Yang: 5 Must-Try Use Cases](https://www.youtube.com/watch?v=MkVcHbviYOw) - 顾问、YouTube 研究员、X scout、Gmail 断舍离、旅行管家。.
- [Alex Finn: setup that actually sticks](https://www.youtube.com/watch?v=vrgO4D_mUlA) - 已经在用 Cursor Cloud Agent 的人讲怎么把 Grok Bot 装稳。.
- [Nate Herk: Grok Bot is For Real](https://www.youtube.com/watch?v=PQBYZQqan2g) - 「装上就能用」的实测，以及 200 美元座位到底买到什么。.
- [Teach a task by screen recording](https://x.com/_avichawla/status/2089817006065496530) - 官方周边提示：演示一遍，Bot 自己写成 skill。.
- [Use the remote computer from your phone](https://x.com/bot/status/2089802847223468116) - @bot 体验更新：不用开笔记本，手机也能用云电脑。.
- [Uncle-Gizmo notes](https://github.com/Uncle-Gizmo/grok-bot-info) - 公开笔记：安全示例工作流，以及它和 Grok Build 怎么并存。.

## 真实使用案例

- [n2parko: CoS + EM + five eng ICs + Databricks + PM](https://x.com/n2parko/status/2087251704744235298) - SpaceXAI 产品编制，带 Bot 互相当值守、交接 PR 的截图。.
- [Lee Robinson: four technical bets](https://x.com/leerob/status/2089169319099777364) - 没有 UI、瘦客户端厚服务端、常驻电脑、浏览器是一等工具。.
- [Debbie: book my flights](https://debbie.codes/blog/i-tested-if-grok-bot-could-book-my-flights) - 诚实的差一点：Bot 能点航司网站，最后一下仍要人。.
- [Debbie: buy gluten-free beer on a Sunday night](https://debbie.codes/blog/i-sent-grok-bot-to-buy-my-gluten-free-beer) - 让 CoS 周日夜去买无麸质啤酒：这是电脑操作，不是聊天。.
- [Yun-Ta: calendar + reservations while walking](https://x.com/yunta_tsai/status/2087415205756391461) - 走路时中英夹杂口述，Bot 扫日历并去网站订位。.
- [Gota: twelve jobs on one roster](https://x.com/gota_bara/status/2087666940450152841) - 出图、调研周报、3D、旅行讨论、退订、在云 VM 里跑本地 LLM。.
- [Box: credit-committee pack](https://x.com/Box/status/2087275866950938662) - 对账委员会材料，再通过 MCP 写回 Box。.
- [WordPress updates taught once](https://x.com/mrfundman/status/2089760255890571404) - 在真实 CMS 上 Teach a task，而不是先写部署脚本。.
- [Arduino updates from a Bot](https://x.com/KettlebellDan/status/2089920364419874937) - Bot 把更新推到硬件上，人少刷 X。.
- [Nate: twelve Bots in eight hours](https://natesnewsletter.substack.com/p/grok-bot-review) - 200 美元的 Agent 小队值不值：第一天就组了 12 个 Bot。.
- [24/7 support agent in 19 minutes](https://www.youtube.com/watch?v=bUALqTpUze0) - 用 routine 搭 24/7 客服，而不是重写工单系统。.
- [Farzad roster: Webby / Shotry / Writey](https://x.com/farzyness/status/2087340859138224540) - 给专科 Bot 起名，再加一个编排者：反复出现的编制。.
- [Sid: Polymarket daily settlement brief](https://x.com/sidshekhar24/status/2089735218861326727) - Bot 扫当天结算盘并出报告。.
- [Logan: the unlock is the computer, not 4.6](https://x.com/LoganJastremski/status/2089903051557491092) - 不靠 API / MCP / 托管浏览器，Bot 像人一样用软件。.
- [Japanese note group: cloud-computer field notes](https://note.com/azumimusuhi/n/n0485219790bb) - 日文实测：在共享云电脑上过一周是什么感觉。.

## 技能、插件与 MCP

- [grokbot-imessage-skill](https://github.com/jeffhuber/grokbot-imessage-skill) - 通过本机 macOS helper 让 Bot 读、分拣、发 iMessage。.
- [Grok Bot Discord gateway](https://github.com/davefmurray/grok-bot-discord) - Discord 网关：让 Bot 住在 Discord，而不是假装 Slack App。.
- [Werewolf gamemaster skill](https://github.com/Heyvhuang/werewolf-gamemaster) - 真技能包：Bot 当狼人杀主持人，不是 hello-world SKILL.md。.
- [Hyperliquid 7-agent trading desk](https://github.com/galleonlabs/hypergrok-trading-desk) - 七个专科 Bot 组成交易台。实验性质，先读代码再授权。.
- [awesome-grok-bot-plugins](https://github.com/rdmgator12/awesome-grok-bot-plugins) - 2026-08-12 抓到的 219 个应用内插件目录，按分类整理。.
- [superpowers (marketplace)](https://github.com/obra/superpowers) - 官方市场里最大的通用技能集：先计划、用证据调试、写能过审的东西。.
- [chrome-devtools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) - 驱动真实 Chrome：性能轨迹、网络、带 sourcemap 的控制台错误。.
- [Vercel plugin](https://github.com/vercel/vercel-plugin) - 部署、日志、域名。请对照论坛里 OAuth 回调失败的帖。.

## 评测与对比

- [The Verge: an AI teammate you can assign work](https://www.theverge.com/ai-artificial-intelligence/978666/spacexai-grok-bot-ai-agent-beta-launch) - 首发报道，没有把它和 grok.com 聊天混为一谈。.
- [VentureBeat: persistent digital coworkers](https://venturebeat.com/orchestration/spacexais-grok-bot-turns-agents-into-persistent-digital-coworkers-that-can-operate-your-apps-for-120-per-month) - 定价与常驻：Teams 约 120 美元/座，电脑不关。.
- [Lenny's Newsletter: Grok Bot, Grok 4.6, and Cursor](https://www.lennysnewsletter.com/p/i-tested-grok-bot-grok-46-and-cursor) - 把 Bot 产品和 4.6 模型拆开讲，不要混成一篇。.
- [Grok Bot vs OpenClaw](https://myclaw.ai/blog/grok-bot-vs-openclaw) - 托管云电脑 vs 自托管、自带模型。.
- [Grok Bot vs OpenClaw vs ChatGPT](https://www.mindstudio.ai/blog/grok-bot-vs-openclaw-chatgpt) - 三方对比：常驻 VM、自托管、带工具的聊天。.
- [Grok Bot vs ChatGPT for work](https://www.eigent.ai/blog/grok-bot-vs-chatgpt-work) - 会用电脑的同事 vs 偶尔调工具的聊天。.
- [Grok Bot vs Claude Cowork](https://www.eigent.ai/blog/grok-bot-vs-claude-cowork) - 持久共享 VM vs 按会话的 cowork。.
- [YouTube: Grok Bot vs OpenClaw and Hermes](https://www.youtube.com/watch?v=sAoTrUijP4g) - 视频横评：大家真正拿来比的三套 Agent。.
- [10 Best Grok Bot Alternatives (2026)](https://www.vellum.ai/blog/best-grok-bot-alternatives) - 不想买 Heavy/Ultra 座位时的替代盘点。.
- [Before You Hire a $200 Grok Bot](https://zchmael.substack.com/p/before-you-hire-a-200-grok-bot-ai) - 怀疑派清单：这个座位买不到什么。.

## 开源替代

- [rakazo](https://github.com/elie222/rakazo) - 开源 Grok Bot 替代：自己托管 always-on 队友。.
- [guaca](https://github.com/madebywelch/guaca) - 另一套自托管的持久电脑 Agent。.
- [OpenGrokBot](https://github.com/wolfqing/OpenGrokBot) - OpenClaw + 自带模型，拼成 Bot 替代。.
- [XinyunOpenBot](https://github.com/dongpen-max/XinyunOpenBot) - 面向同一任务的中文开源替代。.
- [OpenMausBot](https://github.com/milind-soni/OpenMausBot) - 社区运行时，探索同一套 always-on 电脑模式。.
- [open-grokbot](https://github.com/ishandutta2007/open-grokbot) - 早期等价实验，授权前先读代码。.
- [grok-bot-flake](https://github.com/jordangarrison/grok-bot-flake) - 把官方 Linux .deb 打成 Nix flake（不是从源码编）。.

## 社区与故障现场

- [Forum: Introducing Grok Bot](https://forum.cursor.com/t/introducing-grok-bot/168053) - 首发帖：上线 48 小时里大家真正在问什么。.
- [Bots are not a security boundary](https://forum.cursor.com/t/grok-bot-ship-real-session-fences-bots-are-not-a-security-boundary/168476) - 必读：账号下所有 Bot 看见同一套登录和文件。.
- [Always-on workers vs topic threads](https://forum.cursor.com/t/grok-bots-as-always-on-workers-vs-topic-threads/168183) - 社区共识：Bot 是常驻同事，不是聊天标签页。.
- [Free Cursor Ultra with Grok (Heavy bundle)](https://forum.cursor.com/t/free-cursor-ultra-with-grok/168286) - Heavy 怎么映射到 Ultra + Bot，以及什么不会叠。.
- [Reconnect issue](https://forum.cursor.com/t/grok-bot-reconnect-issue/168500) - 重连后「连不上你的电脑」的真实截图。.
- [X login lock on the Bot computer](https://forum.cursor.com/t/grok-bot-x-login-lock-limit-not-lifting/168541) - 云电脑会撞上站点风控。X 登录锁不是假设。.
- [ExternalShell blocked despite Always allow](https://forum.cursor.com/t/grok-bot-externalshell-blocked-despite-always-allow/168180) - 白名单仍会拦。Always allow 不等于永远允许。.
- [Deleted Cursor account orphans the Grok link](https://forum.cursor.com/t/deleted-cursor-account-leaves-grok-link-orphaned-and-blocks-relinking/168783) - 删 Cursor 号可能把 Bot 绑死在失效身份上。.
- [Hacker News discussion](https://news.ycombinator.com/item?id=49261514) - HN 首发讨论，适合看怀疑派怎么说。.
- [Native desktop on Arch / Linux](https://forum.cursor.com/t/native-grok-bot-desktop-app-for-arch-linux-and-linux-generally/168084) - Linux 桌面不是一等公民；这里是诉求和社区打包。.

## 相关列表

- [ZeroPointRepo/awesome-grok-bot](https://github.com/ZeroPointRepo/awesome-grok-bot) - 上线首日 19 条目录，市场格式和自托管运行时写得很清楚。.
- [awesome-workbuddy](https://github.com/staruhub/awesome-workbuddy) - 本仓对照的 WorkBuddy 清单：同一类活，另一个产品。.
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - MCP Server 大全。Grok Bot 走 Cursor 的插件/MCP 政策。.
- [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Skill 格式的姐妹生态；不少 SKILL.md 概念上可迁移。.
- [botdirectory.ai (announced)](https://x.com/aiedge_/status/2089895147068924385) - 社区 Bot 目录，站点本身也是 beta。.

## 贡献

目前 8 个分类、88 条精选。提交前请读 [CONTRIBUTING.md](CONTRIBUTING.md)：必须是云电脑队友这个产品、链接能打开、一句话说明、句号结尾。

---

<p align="center">非官方社区清单，与 xAI/SpaceXAI 或 Cursor 无隶属关系。列表内容 <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>。</p>
