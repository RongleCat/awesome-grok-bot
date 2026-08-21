<h1 align="center">
  <img src="./assets/banner.png" alt="Awesome Grok Bot" width="800" />
</h1>

<p align="center">
  <a href="./README.md"><strong>EN</strong></a>
  ·
  <a href="./README.zh.md"><strong>中文</strong></a>
  ·
  <strong>日本語</strong>
  ·
  <a href="https://usegrokbot.com/">プレイブック用プロンプト</a>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <img src="https://img.shields.io/badge/entries-92-blueviolet" alt="Entry count" />
  <img src="https://img.shields.io/badge/Grok%20Bot-beta%20(2026--08--11)-informational" alt="Grok Bot status" />
  <img src="https://img.shields.io/badge/license-CC0-lightgrey" alt="License" />
</p>

<p align="center">
  <a href="https://grok-app.com"><strong>Grok App</strong></a>（<a href="https://github.com/RongleCat/grok-app">GitHub</a>）— オープンソースの Grok Build デスクトップアプリ · <a href="https://x.com/cgnot996">铁柱AGI @cgnot996</a>
</p>

<p align="center">グループのQRをスキャンして参加するか、友だち追加してもらえれば招待します。</p>
<p align="center">
  <img src="./assets/wechat/group-qr.jpg" alt="Grok Bot の WeChat グループ" width="140" />
  &nbsp;&nbsp;&nbsp;
  <img src="./assets/wechat/personal-qr.png" alt="铁柱AGI を WeChat で追加" width="140" />
</p>
<p align="center"><sub>WeChatグループ（8月27日まで有効）· 友だち追加</sub></p>

> Grok Bot は、2026-08-11 に xAI/SpaceXAI と Cursor が公開した always-on のクラウドパソコン仲間です。各 Bot は 1 台の永続クラウドパソコン（ブラウザ、ファイル、ターミナル）を共有し、ノート PC を閉じても動き続けます。grok.com のチャット、Grok Imagine、Grok 4.x のモデル解説ではありません。 非公式のコミュニティリストであり、xAI や Cursor とは無関係です。

## イベント

<table><tr><td width="320" valign="top"><a href="https://luma.com/5vkzzvqk"><img src="./assets/events/sz-20260830-cover.png" alt="Grok Bot Meetup Shenzhen" width="300" /></a></td><td valign="top"><strong>Grok Bot Meetup Shenzhen</strong><br />2026-08-30（日）14:00–17:30（GMT+8）<br />深圳 · 登録後に住所を表示<br /><br />中国初の Grok Bot オフライン。アイスブレイクと共有 / Workshop。事前登録、主催者承認、定員あり。铁柱AGI と 阿真 が参加。深圳の AI ブロガー歓迎。Grok Bot を使った人を優先。<br /><br /><a href="https://luma.com/5vkzzvqk"><strong>Luma で申し込む →</strong></a></td></tr></table>

## 目次

- [公式リソース](#公式リソース)
- [チュートリアルとガイド](#チュートリアルとガイド)
- [実地事例](#実地事例)
- [スキル、プラグインと MCP](#スキル、プラグインと-mcp)
- [レビューと比較](#レビューと比較)
- [オープンソースの代替](#オープンソースの代替)
- [コミュニティと障害事例](#コミュニティと障害事例)
- [関連リスト](#関連リスト)
- [貢献](#貢献)

## 公式リソース

- [Introducing Grok Bot](https://x.ai/news/introducing-grok-bot) - 発表記事：always-on のエージェントが専用パソコンを持ち、あなたのツール内で 24/7 働きます。
- [Grok Bot overview](https://docs.x.ai/grok-bot/overview) - 製品の公式概要：名前付き Bot が 1 台のクラウドパソコンを共有し、分離は Bot 単位ではなくユーザー単位です。
- [Get started](https://docs.x.ai/grok-bot/get-started) - デスクトップ版を入れ、Cursor でログインし、最初の Bot を作ります。公式の Linux デスクトップはありません。
- [Use cases](https://docs.x.ai/grok-bot/use-cases) - 公式の編成例：営業の夜間 CRM、運用の請求書処理、エンジニアリングのバグ潰し。
- [Grok Bot for iOS](https://docs.x.ai/grok-bot/mobile) - クラウドパソコン上で動き続ける Bot に、スマホからメッセージを送る同伴アプリです。
- [Create and manage Bots](https://docs.x.ai/grok-bot/bots) - Bot の命名と担当範囲の決め方、チャットスレッドではなく常駐の同僚として置く方法。
- [Message and collaborate](https://docs.x.ai/grok-bot/chat-and-collaboration) - Bot 同士がメッセージを送り、グループチャットに入り、仕事の担当を割り振ります。
- [Files and results](https://docs.x.ai/grok-bot/files-and-results) - 成果物が共有パソコンのどこに置かれ、どう手元へ戻すか。
- [Use the computer and apps](https://docs.x.ai/grok-bot/computer-and-apps) - ブラウザ、ファイルシステム、ターミナル。きれいな API がなければ、人と同じようにサイトをクリックします。
- [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations) - Teach a task（画面最大 10 分、マイクなし）で教え、再利用できる routine として保存します。
- [Settings and notifications](https://docs.x.ai/grok-bot/settings-and-notifications) - 通知のグループ分け、モバイル通知、止まっている仕事を Bot が追う方法。
- [Approvals, security, and privacy](https://docs.x.ai/grok-bot/approvals-security-and-privacy) - Bot はパスワードを見ません。承認ラインは不可逆な操作と 2FA の Take over に引きます。
- [Teams and enterprises](https://docs.x.ai/grok-bot/teams-and-enterprises) - チーム向けマーケット、SSO、共有アナリティクス。プラグインは既存の Cursor ポリシーに従います。
- [Troubleshooting](https://docs.x.ai/grok-bot/troubleshooting) - 再接続、runner、よくある beta 障害向けの公式トラブルシュート一覧。
- [FAQ](https://docs.x.ai/grok-bot/faq) - 利用資格、パソコンの共有、Bot が覚えられることについての公式の短い回答。
- [Get access with SuperGrok Heavy](https://cursor.com/help/grok-bot/supergrok-heavy) - Cursor ヘルプ：Heavy / Ultra / Teams Premium の条件。すでに Ultra でも枠は二重に積み上がりません。
- [Grok Bot on mobile (Cursor help)](https://cursor.com/help/grok-bot/mobile) - クラウドパソコン上に残る Bot と、iOS 同伴アプリがどう会話するか。
- [Connect plugins](https://cursor.com/help/grok-bot/connect-plugins) - プラグインを優先し、コネクタがなければクラウドブラウザに戻します。
- [Store secrets securely](https://cursor.com/help/grok-bot/secrets) - 秘密情報は secret card を使い、API キーを Bot のチャットに貼ってはいけません。
- [Grok Bot on the App Store](https://apps.apple.com/us/app/grok-bot/id6794501026) - 同伴アプリの公式 iOS ストアページ。
- [xAI plugin marketplace](https://github.com/xai-org/plugin-marketplace) - 公式の .grok-plugin マーケット。Grok Bot は Cursor のプラグインポリシーを継承します。

## チュートリアルとガイド

- [How to Get Started with Grok Bot](https://debbie.codes/blog/how-to-get-started-with-grok-bot) - Debbie の現場ガイド：最初の Bot、CoS プロンプト、編成の組み直し方。
- [Grok Bot Masterclass](https://www.dailydoseofds.com/p/grok-bot-masterclass/) - Avi / Daily Dose：一度録画して skill にし、routine に載せます。
- [How to Set Up Grok Bot and Build Your First AI Agents](https://www.mindstudio.ai/blog/grok-bot-setup-guide) - インストールから最初の Agent までを通し、Heavy / Ultra / Teams の条件も明記しています。
- [Grok Bot Explained](https://www.ayautomate.com/blog/grok-bot-xai-ai-agents-explained) - 製品を分かりやすく説明し、実際の iPhone の Bot 編成スクリーンショット付き。
- [Hand Off Real Work Across Your Apps](https://app.therundown.ai/guides/hand-off-real-work-across-your-apps-with-grok-bot) - The Rundown：複数アプリにまたがる仕事を Bot へ渡す手順。
- [Connect Multiple Slack Workspaces](https://www.usecarly.com/blog/how-to-connect-multiple-slack-workspaces-to-grok-bot/) - Slack イベントで routine を起こすことと、Grok Bot を Slack App として入れることは別です。
- [Peter Yang: 5 Must-Try Use Cases](https://www.youtube.com/watch?v=MkVcHbviYOw) - 顧問、YouTube リサーチャー、X scout、Gmail 断捨離、旅行コンシェルジュ。
- [Alex Finn: setup that actually sticks](https://www.youtube.com/watch?v=vrgO4D_mUlA) - すでに Cursor Cloud Agents で暮らしている人による、定着するセットアップの長編。
- [Nate Herk: Grok Bot is For Real](https://www.youtube.com/watch?v=PQBYZQqan2g) - 「入れてすぐ使える」実演と、200 ドルの席で実際に得られるもの。
- [Teach a task by screen recording](https://x.com/_avichawla/status/2089817006065496530) - 公式周辺のヒント：作業を一度見せると、Bot が skill を書きます。
- [Use the remote computer from your phone](https://x.com/bot/status/2089802847223468116) - @bot の体験改善：ノート PC を開かず、iOS からクラウドマシンを操作できます。
- [Uncle-Gizmo notes](https://github.com/Uncle-Gizmo/grok-bot-info) - 安全な例のワークフローと、Bot が Grok Build とどう並ぶかの公開ノート。
- [Grok Bot for GTM](https://github.com/bcharleson/grokbot-for-gtm) - Grok Bot のパソコン上でアウトバウンドを回すプレイブック。Instantly、HeyReach、リスト CLI。送信は人の承認が必要です。

## 実地事例

- [n2parko: CoS + EM + five eng ICs + Databricks + PM](https://x.com/n2parko/status/2087251704744235298) - SpaceXAI の製品編成。エージェント同士の PR 引き継ぎの実スクリーンショット付き。
- [Lee Robinson: four technical bets](https://x.com/leerob/status/2089169319099777364) - UI なし、薄いクライアントと厚いサーバー、常時稼働パソコン、ブラウザは第一級の道具。
- [Debbie: book my flights](https://debbie.codes/blog/i-tested-if-grok-bot-could-book-my-flights) - 正直な惜しい結果：Bot は航空会社サイトを操作できるが、最後のクリックはまだ人が要る。
- [Debbie: buy gluten-free beer on a Sunday night](https://debbie.codes/blog/i-sent-grok-bot-to-buy-my-gluten-free-beer) - CoS に日曜夜のグルテンフリービールの買い物を任せる事例。チャットではなくパソコン操作だと分かる。
- [Yun-Ta: calendar + reservations while walking](https://x.com/yunta_tsai/status/2087415205756391461) - 歩きながら中英混じりの音声で頼むと、Bot がカレンダーを見て席を予約します。
- [Gota: twelve jobs on one roster](https://x.com/gota_bara/status/2087666940450152841) - 画像工場、調査ブリーフ、3D、旅行の議論、解約、クラウド VM 上のローカル LLM。
- [Box: credit-committee pack](https://x.com/Box/status/2087275866950938662) - 与信委員会向け資料を突き合わせ、MCP 経由で Box に書き戻します。
- [WordPress updates taught once](https://x.com/mrfundman/status/2089760255890571404) - デプロイスクリプトを書く前に、本物の CMS で Teach a task します。
- [Arduino updates from a Bot](https://x.com/KettlebellDan/status/2089920364419874937) - Bot がハードウェアへ更新を送り、人が X を見なくて済むようにします。
- [Nate: twelve Bots in eight hours](https://natesnewsletter.substack.com/p/grok-bot-review) - 200 ドルの Agent チームは元が取れるか。初日の実際の編成付き。
- [24/7 support agent in 19 minutes](https://www.youtube.com/watch?v=bUALqTpUze0) - ヘルプデスクを作り直すのではなく、routine で 24/7 サポート Bot を組む。
- [Farzad roster: Webby / Shotry / Writey](https://x.com/farzyness/status/2087340859138224540) - 名前付きの専門 Bot にオーケストレーターを足す、繰り返し現れるパターン。
- [Sid: Polymarket daily settlement brief](https://x.com/sidshekhar24/status/2089735218861326727) - Bot がその日の決済済みマーケットを見てレポートを書きます。
- [Logan: the unlock is the computer, not 4.6](https://x.com/LoganJastremski/status/2089903051557491092) - API も MCP もホスト型ブラウザも使わず、Bot は人と同じようにソフトを使います。
- [Japanese note group: cloud-computer field notes](https://note.com/azumimusuhi/n/n0485219790bb) - 共有クラウドパソコンで 1 週間暮らした日本語の実地メモ。

## スキル、プラグインと MCP

- [grokbot-imessage-skill](https://github.com/jeffhuber/grokbot-imessage-skill) - ローカルの macOS helper 経由で、Bot が iMessage を読み、仕分け、送ります。
- [Grok Bot Discord gateway](https://github.com/davefmurray/grok-bot-discord) - Slack App のふりをせず、Bot を Discord に住ませるブリッジ。
- [Werewolf gamemaster skill](https://github.com/Heyvhuang/werewolf-gamemaster) - 本物のスキルパック：hello-world の SKILL.md ではなく、Bot が人狼の進行役をします。
- [Hyperliquid 7-agent trading desk](https://github.com/galleonlabs/hypergrok-trading-desk) - 7 体の専門 Bot で構成する取引デスク。実験的なので、権限を渡す前にコードを読んでください。
- [awesome-grok-bot-plugins](https://github.com/rdmgator12/awesome-grok-bot-plugins) - 2026-08-12 に取得したアプリ内マーケット 219 件を、カテゴリ別に整理。
- [superpowers (marketplace)](https://github.com/obra/superpowers) - 公式マーケット最大の汎用スキル集：計画、根拠あるデバッグ、通る文章を書く。
- [chrome-devtools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) - 実機 Chrome を操作：トレース、ネットワーク、sourcemap 付きのコンソールエラー。
- [Vercel plugin](https://github.com/vercel/vercel-plugin) - デプロイ、ログ、ドメイン。OAuth リダイレクト失敗のフォーラム投稿と合わせて読む。
- [Grok Ship](https://github.com/kunchenguid/grok-ship) - Grok Bot をソフトウェア工場にする配布物。scout と ship を分け、プロジェクトごとの仲間が Cursor Cloud Agent を動かし、PR 前にレビューします。
- [Coolify Cursor plugin](https://github.com/coollabsio/coolify-cursor-plugin) - Coolify 公式の Cursor / Grok Bot プラグイン。リモート HTTP MCP でサーバー、アプリ、デプロイ、ログを見ます。
- [Grok Bot Telegram bridge](https://github.com/SSBrouhard/grokbot-telegram-bridge) - 非公式の Telegram ブリッジ。Grok Bot のクラウドパソコン内で動き、ループバックの Sand ゲートウェイとだけ話します。

## レビューと比較

- [The Verge: an AI teammate you can assign work](https://www.theverge.com/ai-artificial-intelligence/978666/spacexai-grok-bot-ai-agent-beta-launch) - grok.com のチャットと混ぜずに製品を切り分けた発表報道。
- [VentureBeat: persistent digital coworkers](https://venturebeat.com/orchestration/spacexais-grok-bot-turns-agents-into-persistent-digital-coworkers-that-can-operate-your-apps-for-120-per-month) - 価格と常駐：Teams は約 120 ドル/席、パソコンは起動したまま。
- [Lenny's Newsletter: Grok Bot, Grok 4.6, and Cursor](https://www.lennysnewsletter.com/p/i-tested-grok-bot-grok-46-and-cursor) - Bot 製品と 4.6 モデルを分けて書いており、二つを一つにまとめてはいけない。
- [Grok Bot vs OpenClaw](https://myclaw.ai/blog/grok-bot-vs-openclaw) - マネージドのクラウドパソコン vs 自前ホスト・自前モデル。
- [Grok Bot vs OpenClaw vs ChatGPT](https://www.mindstudio.ai/blog/grok-bot-vs-openclaw-chatgpt) - 三者比較：常時稼働 VM、自前ホスト、ツール付きチャット。
- [Grok Bot vs ChatGPT for work](https://www.eigent.ai/blog/grok-bot-vs-chatgpt-work) - パソコンを使う同僚 vs ときどきツールを呼ぶチャット。
- [Grok Bot vs Claude Cowork](https://www.eigent.ai/blog/grok-bot-vs-claude-cowork) - 永続する共有 VM vs セッション単位の cowork。
- [YouTube: Grok Bot vs OpenClaw and Hermes](https://www.youtube.com/watch?v=sAoTrUijP4g) - 実際によく比較される 3 つの Agent スタックの動画横断レビュー。
- [10 Best Grok Bot Alternatives (2026)](https://www.vellum.ai/blog/best-grok-bot-alternatives) - Heavy/Ultra の席を買いたくないときの代替の見取り図。
- [Before You Hire a $200 Grok Bot](https://zchmael.substack.com/p/before-you-hire-a-200-grok-bot-ai) - 懐疑派チェックリスト：この席では買えないもの。

## オープンソースの代替

- [rakazo](https://github.com/elie222/rakazo) - オープンソースの Grok Bot 代替。always-on の仲間を自分でホストします。
- [guaca](https://github.com/madebywelch/guaca) - 持続するパソコン操作エージェントの、もう一つの自前ホスト実装。
- [OpenGrokBot](https://github.com/wolfqing/OpenGrokBot) - OpenClaw に自前モデルを足し、Bot の代わりとして組んだもの。
- [XinyunOpenBot](https://github.com/dongpen-max/XinyunOpenBot) - 同じ仕事を狙った中国語のオープンソース代替。
- [OpenMausBot](https://github.com/milind-soni/OpenMausBot) - 同じ always-on パソコンの型を探るコミュニティランタイム。
- [open-grokbot](https://github.com/ishandutta2007/open-grokbot) - 初期の同等実験。資格情報を渡す前に読んでください。
- [grok-bot-flake](https://github.com/jordangarrison/grok-bot-flake) - 公式 Linux .deb を詰め直した Nix flake（ソースからのビルドではない）。

## コミュニティと障害事例

- [Forum: Introducing Grok Bot](https://forum.cursor.com/t/introducing-grok-bot/168053) - 発表スレッド：公開後 48 時間で実際に聞かれたこと。
- [Bots are not a security boundary](https://forum.cursor.com/t/grok-bot-ship-real-session-fences-bots-are-not-a-security-boundary/168476) - 必読：アカウント上の全 Bot が同じログインとファイルを見ます。
- [Always-on workers vs topic threads](https://forum.cursor.com/t/grok-bots-as-always-on-workers-vs-topic-threads/168183) - コミュニティの合意：Bot は常駐の同僚であり、チャットのタブではない。
- [Free Cursor Ultra with Grok (Heavy bundle)](https://forum.cursor.com/t/free-cursor-ultra-with-grok/168286) - SuperGrok Heavy が Ultra + Bot にどう対応し、何が積み上がらないか。
- [Reconnect issue](https://forum.cursor.com/t/grok-bot-reconnect-issue/168500) - 再接続後の「パソコンに接続できない」実スクリーンショット。
- [X login lock on the Bot computer](https://forum.cursor.com/t/grok-bot-x-login-lock-limit-not-lifting/168541) - クラウドパソコンはサイトのリスク対策に当たる。X のログインロックは仮定ではない。
- [ExternalShell blocked despite Always allow](https://forum.cursor.com/t/grok-bot-externalshell-blocked-despite-always-allow/168180) - 許可リストでも止まる。Always allow が常に許可だと思わないこと。
- [Deleted Cursor account orphans the Grok link](https://forum.cursor.com/t/deleted-cursor-account-leaves-grok-link-orphaned-and-blocks-relinking/168783) - Cursor アカウント削除で、Bot が無効になった身元に固定されることがある。
- [Hacker News discussion](https://news.ycombinator.com/item?id=49261514) - 発表時の HN スレッド。懐疑的な読みに向く。
- [Native desktop on Arch / Linux](https://forum.cursor.com/t/native-grok-bot-desktop-app-for-arch-linux-and-linux-generally/168084) - Linux デスクトップは第一級ではない。要望とコミュニティのパッケージがここにある。
- [Does Grok Bot support local MCP?](https://forum.cursor.com/t/does-grok-bot-support-local-mcp-e-g-workflowy/168182) - 公式確認：Grok Bot はローカル / stdio の MCP を付けられません。リモート HTTP MCP かクラウドブラウザです。

## 関連リスト

- [ZeroPointRepo/awesome-grok-bot](https://github.com/ZeroPointRepo/awesome-grok-bot) - 公開初日の 19 件ディレクトリ。マーケット形式と自前ホストランタイムが厚い。
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - MCP サーバー一覧。Grok Bot は Cursor のプラグイン/MCP ポリシーに従います。
- [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Skill 形式の姉妹エコシステム。多くの SKILL.md は概念として移植できる。
- [botdirectory.ai (announced)](https://x.com/aiedge_/status/2089895147068924385) - 稼働中 Bot のコミュニティディレクトリ。サイト自体も beta 扱い。

## 貢献

8 セクションに 92 件を収録しています。PR の前に [CONTRIBUTING.ja.md](CONTRIBUTING.ja.md) を読んでください。対象はクラウドパソコン仲間としての Grok Bot、リンクは開けること、説明は句点で終わる一文です。

---

<p align="center">非公式のコミュニティリストであり、xAI/SpaceXAI や Cursor とは無関係です。リスト内容は <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>。</p>
