# コントリビューション

このリストは [Grok Bot](https://docs.x.ai/grok-bot/overview) — 2026-08-11 に公開された always-on のクラウドパソコン仲間 — の**厳選**ディレクトリです。発表記事の寄せ集めではありません。

[English](CONTRIBUTING.md) · [中文](CONTRIBUTING.zh.md)

## 掲載条件

エントリは次を満たす必要があります。

1. **Grok Bot という製品**についてのものであること（名前付き Bot、共有クラウド VM、ブラウザ/ファイル/ターミナル、Teach-a-task、routine）。grok.com のチャット、Grok Imagine、Grok 4.x のモデル記事は、直接比較でない限りここには置きません。
2. 自分で開いて確認できる URL があること。
3. 形式は `- [Name](URL) - 一文。` で、句点で終わること。
4. いちばん近いセクションに入れること。公式が先、そのあとチュートリアル、実地事例、プラグイン、比較、オープンソース、コミュニティ。
5. 同じ説明を `data/catalog.json` の **en**、**zh**、**ja** に書き、`python3 scripts/generate_readme.py` を実行すること。

## 送らないでください

- 死んでいるリンク、アフィリエイト導線、Grok Bot に触れただけの「10 ツール」記事
- 第三者全文の丸ごと転載
- 重複 URL
- 一次情報を示せない価格・用量・セキュリティの主張

## 流れ

1. Fork してブランチを切り、`data/catalog.json` を編集する。
2. README を再生成する。
3. `.github/PULL_REQUEST_TEMPLATE.md` のチェックリスト付きで PR を開く。
