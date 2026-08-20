# Contributing

This list should stay a **curated** directory of [Grok Bot](https://docs.x.ai/grok-bot/overview) — the always-on cloud-computer teammate launched 2026-08-11. It is not a dump of every launch recap.

[中文版](CONTRIBUTING.zh.md) · [日本語](CONTRIBUTING.ja.md)

## Acceptance

An entry must:

1. Be about **Grok Bot the product** (named Bot, shared cloud VM, browser/files/terminal, Teach-a-task, routines). grok.com chat, Grok Imagine, and Grok 4.x model posts do not belong here unless they are a direct comparison.
2. Have a reachable URL you opened yourself.
3. Use the form `- [Name](URL) - one sentence.` ending with a period.
4. Land in the closest section. Official first, then tutorials, field cases, plugins, comparisons, open source, community.
5. Add the same blurb to `data/catalog.json` in **en**, **zh**, and **ja**, then run `python3 scripts/generate_readme.py`.

## Do not send

- Dead links, affiliate funnels, or “10 tools” posts that only mention Grok Bot in passing
- Wholesale reprints of third-party fulltext
- Duplicate URLs
- Claims about pricing, quotas, or security that you cannot point at a primary source

## Flow

1. Fork, branch, edit `data/catalog.json`.
2. Regenerate README files.
3. Open a PR with the checklist in `.github/PULL_REQUEST_TEMPLATE.md`.
