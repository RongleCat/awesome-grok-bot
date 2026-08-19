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
  Also shipping <a href="https://grok-app.com"><strong>Grok App</strong></a> (<a href="https://github.com/RongleCat/grok-app">GitHub</a>) — open-source Grok Build desktop app · <a href="https://x.com/cgnot996">铁柱AGI @cgnot996</a>
</p>

> A curated list of official docs, field cases, tutorials, plugins, and open-source stand-ins for **Grok Bot** — xAI/SpaceXAI and Cursor's always-on AI teammates, each sharing one persistent cloud computer. Launched in beta 2026-08-11.

{product}

Switch language with the **中文** link above.

This list is **not** grok.com chat, Grok Imagine, or a Grok 4.x model roundup. It is also **not affiliated with xAI or Cursor**.
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
  顺手做了 <a href="https://grok-app.com"><strong>Grok App</strong></a>（<a href="https://github.com/RongleCat/grok-app">GitHub</a>）— 开源 Grok Build 桌面端 · <a href="https://x.com/cgnot996">铁柱AGI @cgnot996</a>
</p>

> **Grok Bot** 生态精选清单：官方文档、真实案例、教程、插件与开源替代。Grok Bot 是 xAI/SpaceXAI 与 Cursor 在 2026-08-11 上线的 always-on 云电脑队友。

{product}

用上面的 **English** 链接切回英文。

本清单**不是** grok.com 聊天、Grok Imagine 或 Grok 4.x 模型评测。**与 xAI / Cursor 无官方关系。**
"""

    toc_title = "Contents" if lang == "en" else "目录"
    lines = [intro, f"## {toc_title}", ""]
    playbook_h = "Playbook (read this first)" if lang == "en" else "玩法（先读这段）"
    lines.append(f"- [{playbook_h}](#{section_anchor(playbook_h)})")
    for sec in CAT["sections"]:
        t = sec["title"][lang]
        lines.append(f"- [{t}](#{section_anchor(t)})")
    contrib_h = "Contributing" if lang == "en" else "贡献"
    lines.append(f"- [{contrib_h}](#{section_anchor(contrib_h)})")
    lines.append("")

    if lang == "en":
        lines += [
            f"## {playbook_h}",
            "",
            "Field notes distilled from the local research catalog (175 reviewed sources). They are rules of thumb, not vendor canon.",
            "",
            "1. **One computer, not one machine per Bot.** Logins and files are visible to every Bot on the account.",
            "2. **Draw the approval line on irreversible actions.** Auto Review + take over for 2FA.",
            "3. **The cloud computer hits site risk controls.** X login locks and captchas show up in real threads.",
            "4. **Reconnect can drop state.** Rebuilding the bridge or deleting the Cursor account can orphan the Bot.",
            "5. **Heavy / Ultra / Teams Premium is a gate, not infinite quota.** Usage resets weekly.",
            "6. **Linux desktop is not first-class.** Community `.deb` / Nix packs exist; official desktop is macOS / Windows + iOS.",
            "",
            "Minimum roster that keeps showing up: Chief of Staff, read-only inbox, research scout, engineering squasher, on-call support. Start read-only, then Teach a task, then hang a routine. Copy-paste prompts: [`prompts/playbook-prompts.md`](prompts/playbook-prompts.md).",
            "",
        ]
    else:
        lines += [
            f"## {playbook_h}",
            "",
            "从本地 175 条过关材料里收出来的判断，是经验不是厂商 Canon。",
            "",
            "1. **一台电脑，不是一人一机。** 登录和文件对账号下全部 Bot 可见。",
            "2. **审批线画在不可逆动作上。** Auto Review + 2FA Take over。",
            "3. **云电脑会撞上站点风控。** X 登录锁、验证码在真实帖里反复出现。",
            "4. **重连会丢状态。** 重建桥或删 Cursor 号可能把 Bot 绑死。",
            "5. **Heavy / Ultra / Teams Premium 是门槛不是无限。** 用量按周重置。",
            "6. **Linux 桌面不是一等公民。** 社区有 `.deb` / Nix；官方桌面是 macOS / Windows + iOS。",
            "",
            "反复出现的最小编制：幕僚长、只读收件箱、研究侦察、工程复现、值班客服。先只读，再 Teach，再挂 routine。可粘贴提示词见 [`prompts/playbook-prompts.zh.md`](prompts/playbook-prompts.zh.md)。",
            "",
        ]

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
