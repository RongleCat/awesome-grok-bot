# 贡献指南

本清单只收 [Grok Bot](https://docs.x.ai/grok-bot/overview)——2026-08-11 上线的 always-on 云电脑队友。不是把所有首发通稿再堆一遍。

[English](CONTRIBUTING.md) · [日本語](CONTRIBUTING.ja.md)

## 收录标准

1. 必须是 **Grok Bot 这个产品**（有名字的 Bot、共享云电脑、浏览器/文件/终端、Teach-a-task、routine）。grok.com 聊天、Imagine、Grok 4.x 模型文，除非是直接对比，否则不收。
2. 链接你自己打开过，能访问。
3. 格式：`- [名称](URL) - 一句话说明.` 句号结尾。
4. 放对分类。官方靠前，然后教程、案例、插件、对比、开源、社区。
5. 同一条说明要同时写进 `data/catalog.json` 的 `en`、`zh` 和 `ja`，再跑 `python3 scripts/generate_readme.py`。

## 不收

- 失效链、返佣、只提了一嘴名字的盘点文
- 第三方全文整包转载
- 重复 URL
- 说不清出处的定价、用量、安全结论

## 流程

1. Fork，改 `data/catalog.json`。
2. 重新生成 README。
3. 按 `.github/PULL_REQUEST_TEMPLATE.md` 提 PR。
