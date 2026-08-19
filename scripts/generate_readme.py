#!/usr/bin/env python3
"""Generate README.md (en) and README.zh.md from data/catalog.json."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))


def count_items() -> int:
    return sum(len(s["items"]) for s in CAT["sections"])


def section_anchor(title: str) -> str:
    return title.lower().replace(" ", "-").replace("&", "").replace(",", "")


def render(lang: str) -> str:
    n = count_items()
    nsec = len(CAT["sections"])
    product = CAT["product"][lang]
    other_file = "README.zh.md" if lang == "en" else "README.md"
    other_label = "中文" if lang == "en" else "English"

    if lang == "en":
        intro = f"""<h1 align="center">
  <img src="./assets/banner.png" alt="Awesome Grok Bot" width="800" />
</h1>

<p align="center">
  <a href="./{other_file}"><strong>{other_label}</strong></a>
  ·
  <a href="./prompts/playbook-prompts.md">Playbook prompts</a>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <img src="https://img.shields.io/badge/entries-{n}-blueviolet" alt="Entry count" />
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

> {product} Unofficial community list, not affiliated with xAI or Cursor.
"""
    else:
        intro = f"""<h1 align="center">
  <img src="./assets/banner.png" alt="Awesome Grok Bot" width="800" />
</h1>

<p align="center">
  <a href="./{other_file}"><strong>{other_label}</strong></a>
  ·
  <a href="./prompts/playbook-prompts.zh.md">玩法提示词</a>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <img src="https://img.shields.io/badge/entries-{n}-blueviolet" alt="Entry count" />
  <img src="https://img.shields.io/badge/Grok%20Bot-beta%20(2026--08--11)-informational" alt="Grok Bot status" />
  <img src="https://img.shields.io/badge/license-CC0-lightgrey" alt="License" />
</p>

<p align="center">
  <a href="https://grok-app.com"><strong>Grok App</strong></a>（<a href="https://github.com/RongleCat/grok-app">GitHub</a>）— 开源 Grok Build 桌面端 · <a href="https://x.com/cgnot996">铁柱AGI @cgnot996</a>
</p>

<p align="center">扫码进交流群；加不上群就添加好友，我拉你进。</p>
<p align="center">
  <img src="./assets/wechat/group-qr.jpg" alt="Grok Bot 交流群" width="140" />
  &nbsp;&nbsp;&nbsp;
  <img src="./assets/wechat/personal-qr.png" alt="添加好友" width="140" />
</p>
<p align="center"><sub>交流群（8 月 27 日前有效）· 添加好友</sub></p>

> {product} 非官方社区清单，与 xAI / Cursor 无隶属关系。
"""

    toc_title = "Contents" if lang == "en" else "目录"
    lines = [intro, f"## {toc_title}", ""]
    for sec in CAT["sections"]:
        t = sec["title"][lang]
        lines.append(f"- [{t}](#{section_anchor(t)})")
    contrib_h = "Contributing" if lang == "en" else "贡献"
    lines.append(f"- [{contrib_h}](#{section_anchor(contrib_h)})")
    lines.append("")

    for sec in CAT["sections"]:
        t = sec["title"][lang]
        lines.append(f"## {t}")
        lines.append("")
        for item in sec["items"]:
            blurb = item["blurb"][lang].rstrip(".")
            lines.append(f"- [{item['title']}]({item['url']}) - {blurb}.")
        lines.append("")

    if lang == "en":
        lines += [
            f"## {contrib_h}",
            "",
            f"{n} curated entries across {nsec} sections. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR: the resource must be about Grok Bot the cloud-computer teammate, the link must work, and the blurb is one sentence ending with a period.",
            "",
            "---",
            "",
            "<p align=\"center\">Unofficial community list. Not affiliated with xAI/SpaceXAI or Cursor. List content <a href=\"https://creativecommons.org/publicdomain/zero/1.0/\">CC0 1.0</a>.</p>",
            "",
        ]
    else:
        lines += [
            f"## {contrib_h}",
            "",
            f"目前 {nsec} 个分类、{n} 条精选。提交前请读 [CONTRIBUTING.md](CONTRIBUTING.md)：必须是云电脑队友这个产品、链接能打开、一句话说明、句号结尾。",
            "",
            "---",
            "",
            "<p align=\"center\">非官方社区清单，与 xAI/SpaceXAI 或 Cursor 无隶属关系。列表内容 <a href=\"https://creativecommons.org/publicdomain/zero/1.0/\">CC0 1.0</a>。</p>",
            "",
        ]
    return "\n".join(lines)


def main() -> None:
    (ROOT / "README.md").write_text(render("en"), encoding="utf-8")
    (ROOT / "README.zh.md").write_text(render("zh"), encoding="utf-8")
    print("entries", count_items(), "sections", len(CAT["sections"]))


if __name__ == "__main__":
    main()
