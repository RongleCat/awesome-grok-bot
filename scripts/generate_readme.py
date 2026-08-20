#!/usr/bin/env python3
"""Generate README.md (en), README.zh.md, and README.ja.md from data/catalog.json."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))

LANGS = ("en", "zh", "ja")
README_NAME = {
    "en": "README.md",
    "zh": "README.zh.md",
    "ja": "README.ja.md",
}
LANG_LABEL = {
    "en": "EN",
    "zh": "中文",
    "ja": "日本語",
}

# Chrome around the fixed header identity (Grok App, 铁柱AGI, QR codes).
CHROME = {
    "en": {
        "playbook": "Playbook prompts",
        "grok_app": (
            '<a href="https://grok-app.com"><strong>Grok App</strong></a> '
            '(<a href="https://github.com/RongleCat/grok-app">GitHub</a>) — '
            'open-source Grok Build desktop app · '
            '<a href="https://x.com/cgnot996">铁柱AGI @cgnot996</a>'
        ),
        "scan": "Scan the group QR to join, or add me as a friend and I will pull you in.",
        "group_alt": "Grok Bot WeChat group",
        "friend_alt": "Add 铁柱AGI on WeChat",
        "qr_sub": "WeChat group (valid until Aug 27) · Add friend",
        "unofficial": "Unofficial community list, not affiliated with xAI or Cursor.",
        "toc": "Contents",
        "contrib": "Contributing",
        "contrib_body": (
            "{n} curated entries across {nsec} sections. Please read "
            "[CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR: the resource "
            "must be about Grok Bot the cloud-computer teammate, the link must work, "
            "and the blurb is one sentence ending with a period."
        ),
        "footer": (
            "Unofficial community list. Not affiliated with xAI/SpaceXAI or Cursor. "
            'List content <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>.'
        ),
    },
    "zh": {
        "playbook": "玩法提示词",
        "grok_app": (
            '<a href="https://grok-app.com"><strong>Grok App</strong></a>'
            '（<a href="https://github.com/RongleCat/grok-app">GitHub</a>）— '
            "开源 Grok Build 桌面端 · "
            '<a href="https://x.com/cgnot996">铁柱AGI @cgnot996</a>'
        ),
        "scan": "扫码进交流群；加不上群就添加好友，我拉你进。",
        "group_alt": "Grok Bot 交流群",
        "friend_alt": "添加好友",
        "qr_sub": "交流群（8 月 27 日前有效）· 添加好友",
        "unofficial": "非官方社区清单，与 xAI / Cursor 无隶属关系。",
        "toc": "目录",
        "contrib": "贡献",
        "contrib_body": (
            "目前 {nsec} 个分类、{n} 条精选。提交前请读 "
            "[CONTRIBUTING.md](CONTRIBUTING.md)：必须是云电脑队友这个产品、"
            "链接能打开、一句话说明、句号结尾。"
        ),
        "footer": (
            "非官方社区清单，与 xAI/SpaceXAI 或 Cursor 无隶属关系。"
            '列表内容 <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>。'
        ),
    },
    "ja": {
        "playbook": "プレイブック用プロンプト",
        "grok_app": (
            '<a href="https://grok-app.com"><strong>Grok App</strong></a>'
            '（<a href="https://github.com/RongleCat/grok-app">GitHub</a>）— '
            "オープンソースの Grok Build デスクトップアプリ · "
            '<a href="https://x.com/cgnot996">铁柱AGI @cgnot996</a>'
        ),
        "scan": "グループのQRをスキャンして参加するか、友だち追加してもらえれば招待します。",
        "group_alt": "Grok Bot の WeChat グループ",
        "friend_alt": "铁柱AGI を WeChat で追加",
        "qr_sub": "WeChatグループ（8月27日まで有効）· 友だち追加",
        "unofficial": "非公式のコミュニティリストであり、xAI や Cursor とは無関係です。",
        "toc": "目次",
        "contrib": "貢献",
        "contrib_body": (
            "{nsec} セクションに {n} 件を収録しています。PR の前に "
            "[CONTRIBUTING.ja.md](CONTRIBUTING.ja.md) を読んでください。"
            "対象はクラウドパソコン仲間としての Grok Bot、リンクは開けること、"
            "説明は句点で終わる一文です。"
        ),
        "footer": (
            "非公式のコミュニティリストであり、xAI/SpaceXAI や Cursor とは無関係です。"
            'リスト内容は <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>。'
        ),
    },
}


def count_items() -> int:
    return sum(len(s["items"]) for s in CAT["sections"])


def require_i18n(obj: dict, path: str) -> None:
    missing = [lang for lang in LANGS if not str(obj.get(lang, "")).strip()]
    if missing:
        raise SystemExit(f"catalog missing {missing} at {path}")


def validate_catalog() -> None:
    require_i18n(CAT["product"], "product")
    for sec in CAT["sections"]:
        require_i18n(sec["title"], f"sections.{sec['id']}.title")
        for item in sec["items"]:
            require_i18n(item["blurb"], f"{sec['id']}:{item['url']}")


def section_anchor(title: str) -> str:
    return title.lower().replace(" ", "-").replace("&", "").replace(",", "")


def lang_switcher(lang: str) -> str:
    parts = []
    for code in LANGS:
        label = f"<strong>{LANG_LABEL[code]}</strong>"
        if code == lang:
            parts.append(label)
        else:
            parts.append(f'<a href="./{README_NAME[code]}">{label}</a>')
    return "\n  ·\n  ".join(parts)


def format_blurb(text: str, lang: str) -> str:
    # Keep en/zh output stable (zh catalog strings already end with 。).
    if lang == "ja":
        return text.rstrip("。.").rstrip() + "。"
    return text.rstrip(".") + "."


def render(lang: str) -> str:
    n = count_items()
    nsec = len(CAT["sections"])
    product = CAT["product"][lang]
    chrome = CHROME[lang]
    switcher = lang_switcher(lang)

    intro = f"""<h1 align="center">
  <img src="./assets/banner.png" alt="Awesome Grok Bot" width="800" />
</h1>

<p align="center">
  {switcher}
  ·
  <a href="https://usegrokbot.com/">{chrome["playbook"]}</a>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <img src="https://img.shields.io/badge/entries-{n}-blueviolet" alt="Entry count" />
  <img src="https://img.shields.io/badge/Grok%20Bot-beta%20(2026--08--11)-informational" alt="Grok Bot status" />
  <img src="https://img.shields.io/badge/license-CC0-lightgrey" alt="License" />
</p>

<p align="center">
  {chrome["grok_app"]}
</p>

<p align="center">{chrome["scan"]}</p>
<p align="center">
  <img src="./assets/wechat/group-qr.jpg" alt="{chrome["group_alt"]}" width="140" />
  &nbsp;&nbsp;&nbsp;
  <img src="./assets/wechat/personal-qr.png" alt="{chrome["friend_alt"]}" width="140" />
</p>
<p align="center"><sub>{chrome["qr_sub"]}</sub></p>

> {product} {chrome["unofficial"]}
"""

    lines = [intro, f"## {chrome['toc']}", ""]
    for sec in CAT["sections"]:
        t = sec["title"][lang]
        lines.append(f"- [{t}](#{section_anchor(t)})")
    contrib_h = chrome["contrib"]
    lines.append(f"- [{contrib_h}](#{section_anchor(contrib_h)})")
    lines.append("")

    for sec in CAT["sections"]:
        t = sec["title"][lang]
        lines.append(f"## {t}")
        lines.append("")
        for item in sec["items"]:
            blurb = format_blurb(item["blurb"][lang], lang)
            lines.append(f"- [{item['title']}]({item['url']}) - {blurb}")
        lines.append("")

    lines += [
        f"## {contrib_h}",
        "",
        chrome["contrib_body"].format(n=n, nsec=nsec),
        "",
        "---",
        "",
        f'<p align="center">{chrome["footer"]}</p>',
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    validate_catalog()
    for lang in LANGS:
        (ROOT / README_NAME[lang]).write_text(render(lang), encoding="utf-8")
    print("entries", count_items(), "sections", len(CAT["sections"]), "langs", ",".join(LANGS))


if __name__ == "__main__":
    main()
