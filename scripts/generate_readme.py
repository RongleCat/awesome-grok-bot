#!/usr/bin/env python3
"""Generate README.md (en), README.zh.md, and README.ja.md from data/catalog.json."""

from __future__ import annotations

import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))

LANGS = ("en", "zh", "ja")
README_NAME = {
    "en": "README.md",
    "zh": "README.zh.md",
    "ja": "README.ja.md",
}
EVENTS_NAME = {
    "en": "EVENTS.md",
    "zh": "EVENTS.zh.md",
    "ja": "EVENTS.ja.md",
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
        "scan": "Follow the WeChat official account, or add me as a friend.",
        "group_alt": "WeChat official account 铁柱AGI",
        "friend_alt": "Add 铁柱AGI on WeChat",
        "qr_sub": "Official account (search 铁柱AGI) · Add friend",
        "unofficial": "Unofficial community list, not affiliated with xAI or Cursor.",
        "events": "Upcoming",
        "events_more": "Full meetup notes",
        "events_page_lead": "Posters, venues, and how to register. The README groups cities by country; tap a name to jump here.",
        "events_back": "Back to the list",
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
        "scan": "扫码关注公众号，或添加好友。",
        "group_alt": "微信公众号 铁柱AGI",
        "friend_alt": "添加好友",
        "qr_sub": "公众号（搜 铁柱AGI）· 添加好友",
        "unofficial": "非官方社区清单，与 xAI / Cursor 无隶属关系。",
        "events": "活动",
        "events_more": "全部活动介绍",
        "events_page_lead": "海报、场地和报名方式。首页按国家列出城市，点名称跳到这一页的对应场次。[回 README](README.zh.md)。",
        "events_back": "回清单",
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
        "scan": "公式アカウントをフォローするか、友だち追加してください。",
        "group_alt": "WeChat 公式アカウント 铁柱AGI",
        "friend_alt": "铁柱AGI を WeChat で追加",
        "qr_sub": "公式アカウント（铁柱AGI で検索）· 友だち追加",
        "unofficial": "非公式のコミュニティリストであり、xAI や Cursor とは無関係です。",
        "events": "イベント",
        "events_more": "イベントの詳細",
        "events_page_lead": "ポスター、会場、申し込み。README は国ごとに都市を並べ、名前を押すとこのページの該当イベントへ飛びます。",
        "events_back": "一覧に戻る",
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
    for ev in CAT.get("events") or []:
        eid = ev.get("id", "?")
        for key in ("title", "when", "where", "body", "cta"):
            require_i18n(ev[key], f"events.{eid}.{key}")



SHANGHAI = timezone(timedelta(hours=8))


def active_events() -> list[dict]:
    now = datetime.now(SHANGHAI)
    out = []
    for ev in CAT.get("events") or []:
        raw = ev.get("expires")
        if not raw:
            out.append(ev)
            continue
        exp = datetime.fromisoformat(raw)
        if exp.tzinfo is None:
            exp = exp.replace(tzinfo=SHANGHAI)
        if now <= exp:
            out.append(ev)
    return out


def events_switcher(lang: str) -> str:
    parts = []
    for code in LANGS:
        label = f"<strong>{LANG_LABEL[code]}</strong>"
        if code == lang:
            parts.append(label)
        else:
            parts.append(f'<a href="./{EVENTS_NAME[code]}">{label}</a>')
    return " · ".join(parts)


COUNTRY_LABEL = {
    "cn": {"en": "China", "zh": "中国", "ja": "中国"},
    "us": {"en": "United States", "zh": "美国", "ja": "アメリカ"},
    "jp": {"en": "Japan", "zh": "日本", "ja": "日本"},
    "ca": {"en": "Canada", "zh": "加拿大", "ja": "カナダ"},
    "mx": {"en": "Mexico", "zh": "墨西哥", "ja": "メキシコ"},
    "ar": {"en": "Argentina", "zh": "阿根廷", "ja": "アルゼンチン"},
    "ec": {"en": "Ecuador", "zh": "厄瓜多尔", "ja": "エクアドル"},
    "pe": {"en": "Peru", "zh": "秘鲁", "ja": "ペルー"},
    "co": {"en": "Colombia", "zh": "哥伦比亚", "ja": "コロンビア"},
    "br": {"en": "Brazil", "zh": "巴西", "ja": "ブラジル"},
    "gt": {"en": "Guatemala", "zh": "危地马拉", "ja": "グアテマラ"},
    "sv": {"en": "El Salvador", "zh": "萨尔瓦多", "ja": "エルサルバドル"},
    "ph": {"en": "Philippines", "zh": "菲律宾", "ja": "フィリピン"},
    "my": {"en": "Malaysia", "zh": "马来西亚", "ja": "マレーシア"},
    "id": {"en": "Indonesia", "zh": "印度尼西亚", "ja": "インドネシア"},
    "sg": {"en": "Singapore", "zh": "新加坡", "ja": "シンガポール"},
    "in": {"en": "India", "zh": "印度", "ja": "インド"},
    "mm": {"en": "Myanmar", "zh": "缅甸", "ja": "ミャンマー"},
    "il": {"en": "Israel", "zh": "以色列", "ja": "イスラエル"},
    "ke": {"en": "Kenya", "zh": "肯尼亚", "ja": "ケニア"},
    "cm": {"en": "Cameroon", "zh": "喀麦隆", "ja": "カメルーン"},
    "tg": {"en": "Togo", "zh": "多哥", "ja": "トーゴ"},
    "nl": {"en": "Netherlands", "zh": "荷兰", "ja": "オランダ"},
    "dk": {"en": "Denmark", "zh": "丹麦", "ja": "デンマーク"},
    "al": {"en": "Albania", "zh": "阿尔巴尼亚", "ja": "アルバニア"},
    "gb": {"en": "United Kingdom", "zh": "英国", "ja": "イギリス"},
    "au": {"en": "Australia", "zh": "澳大利亚", "ja": "オーストラリア"},
    "mt": {"en": "Malta", "zh": "马耳他", "ja": "マルタ"},
    "pt": {"en": "Portugal", "zh": "葡萄牙", "ja": "ポルトガル"},
    "be": {"en": "Belgium", "zh": "比利时", "ja": "ベルギー"},
    "de": {"en": "Germany", "zh": "德国", "ja": "ドイツ"},
    "online": {"en": "Online", "zh": "线上", "ja": "オンライン"},
    "other": {"en": "Other", "zh": "其他", "ja": "その他"},
}

# Hong Kong, Macau, and Taiwan are listed under China.
# (country, place_en, place_zh, place_ja)
EVENT_GEO = {
    "sz-20260830": ("cn", "Shenzhen", "深圳", "深圳"),
    "mo-20260905": ("cn", "Macao", "澳门", "マカオ"),
    "cd-20260905": ("cn", "Chengdu", "成都", "成都"),
    "lv-20260915": ("us", "Las Vegas", "拉斯维加斯", "ラスベガス"),
    "sf-20260903": ("us", "San Francisco (women)", "旧金山（女性场）", "サンフランシスコ（女性）"),
    "sfb-20260901": ("us", "San Francisco (demo)", "旧金山（演示）", "サンフランシスコ（デモ）"),
    "sfs-20260903": ("us", "San Francisco (students)", "旧金山（学生）", "サンフランシスコ（学生）"),
    "sfd-20260902": ("us", "San Francisco After Dark", "旧金山 After Dark", "サンフランシスコ After Dark"),
    "nyd-20260902": ("us", "New York After Dark", "纽约 After Dark", "ニューヨーク After Dark"),
    "nyc-20260903": ("us", "New York (students)", "纽约（学生）", "ニューヨーク（学生）"),
    "phl-20260903": ("us", "Penn / Philadelphia", "费城宾大", "ペンシルベニア大"),
    "uiuc-20260903": ("us", "UIUC", "香槟 UIUC", "UIUC"),
    "isu-20260903": ("us", "Iowa State / Ames", "爱荷华州立", "アイオワ州立"),
    "pitt-20260903": ("us", "Pitt", "匹兹堡大学", "ピッツバーグ大"),
    "cmu-20260903": ("us", "CMU / Pittsburgh", "卡内基梅隆", "CMU"),
    "ncsu-20260903": ("us", "NC State", "北卡州立", "NC State"),
    "rose-20260903": ("us", "Rose-Hulman", "Rose-Hulman", "Rose-Hulman"),
    "roc-20260903": ("us", "URochester", "罗切斯特大学", "ロチェスター大"),
    "rit-20260903": ("us", "RIT / Rochester", "RIT 罗切斯特", "RIT"),
    "chf-20260903": ("us", "Chaffey College", "Chaffey College", "Chaffey College"),
    "slo-20260903": ("us", "Cal Poly", "Cal Poly", "Cal Poly"),
    "sba-20260903": ("us", "UC Santa Barbara", "UCSB", "UCSB"),
    "udel-20260903": ("us", "Delaware", "特拉华大学", "デラウェア大"),
    "davis-20260903": ("us", "UC Davis", "UC Davis", "UC Davis"),
    "a2-20260903": ("us", "Michigan / Ann Arbor", "密歇根大学", "ミシガン大"),
    "uf-20260903": ("us", "Florida / Gainesville", "佛罗里达大学", "フロリダ大"),
    "tamu-20260903": ("us", "Texas A&M", "德州农工", "テキサスA&M"),
    "txl-20260903": ("us", "TX Luminescence", "德州 TX Luminescence", "TX Luminescence"),
    "jhu-20260903": ("us", "Johns Hopkins", "约翰霍普金斯", "ジョンズホプキンス"),
    "prin-20260903": ("us", "Princeton", "普林斯顿", "プリンストン"),
    "laf-20260903": ("us", "Purdue", "普渡", "パデュー"),
    "mcn-20260903": ("us", "McNeese / Lake Charles", "McNeese", "McNeese"),
    "hvd-20260903": ("us", "Harvard", "哈佛", "ハーバード"),
    "ucr-20260903": ("us", "UC Riverside", "UCR 河滨", "UCR"),
    "cla-20260903": ("us", "5Cs / Claremont", "5Cs 克莱蒙特", "5Cs / Claremont"),
    "tem-20260903": ("us", "MSJC / Temecula", "MSJC 特曼库拉", "MSJC / Temecula"),
    "oxf-20260903": ("us", "Miami U / Oxford OH", "迈阿密大学 Oxford", "Miami U / Oxford OH"),
    "tmp-20260903": ("us", "Temple / Philadelphia", "天普大学 费城", "Temple / フィラデルフィア"),
    "unc-20260903": ("us", "UNC / Chapel Hill", "UNC 教堂山", "UNC / Chapel Hill"),
    "sjsu-20260903": ("us", "SJSU / San Jose", "SJSU 圣何塞", "SJSU / San Jose"),
    "usc-20260903": ("us", "USC / Los Angeles", "USC 洛杉矶", "USC / Los Angeles"),
    "mlt-20260917": ("mt", "Ta' Xbiex / Malta", "马耳他 Ta' Xbiex", "マルタ Ta' Xbiex"),
    "bab-20260903": ("us", "Babson / Wellesley", "Babson 韦尔斯利", "Babson / Wellesley"),
    "tlv-20260908": ("il", "Tel Aviv", "特拉维夫", "テルアビブ"),
    "mty-20260910": ("mx", "Monterrey", "蒙特雷", "モンテレイ"),
    "pue-20260924": ("mx", "Puebla", "普埃布拉", "プエブラ"),
    "vhs-20260903": ("mx", "Villahermosa", "比亚埃尔莫萨", "ビヤエルモサ"),
    "mnl-20260904": ("ph", "Manila", "马尼拉", "マニラ"),
    "ceb-20260919": ("ph", "Cebu", "宿务", "セブ"),
    "brc-20260910": ("ar", "Bariloche", "巴里洛切", "バリローチェ"),
    "bue-20260916": ("ar", "Buenos Aires", "布宜诺斯艾利斯", "ブエノスアイレス"),
    "mdz-20261003": ("ar", "Mendoza", "门多萨", "メンドサ"),
    "sla-20260916": ("ar", "Salta", "萨尔塔", "サルタ"),
    "aqp-20260911": ("pe", "Arequipa", "阿雷基帕", "アレキパ"),
    "lim-20260911": ("pe", "Lima", "利马", "リマ"),
    "ctg-20260911": ("co", "Cartago", "卡塔戈", "カルタゴ"),
    "lfw-20260912": ("tg", "Lomé", "洛美", "ロメ"),
    "mec-20260912": ("ec", "Manta", "曼塔", "マンタ"),
    "uio-20260924": ("ec", "Quito", "基多", "キト"),
    "cumb-20261003": ("ec", "Cumbayá", "昆巴亚", "クンバヤ"),
    "nbo-20260917": ("ke", "Nairobi", "内罗毕", "ナイロビ"),
    "tgr-20260911": ("id", "Tangerang", "坦格朗", "タンゲラン"),
    "kul-20260919": ("my", "Kuala Lumpur", "吉隆坡", "クアラルンプール"),
    "yyc-20260930": ("ca", "Calgary", "卡尔加里", "カルガリー"),
    "vic-20260921": ("ca", "Victoria BC", "维多利亚（BC）", "ビクトリア（BC）"),
    "sud-20260917": ("ca", "Sudbury", "萨德伯里", "サドベリー"),
    "yyz-20260917": ("ca", "Toronto", "多伦多", "トロント"),
    "spk-20261002": ("jp", "Sapporo", "札幌", "札幌"),
    "tyo-20260909": ("jp", "Tokyo", "东京", "東京"),
    "osa-20260917": ("jp", "Osaka", "大阪", "大阪"),
    "syd-20260826": ("au", "Sydney", "悉尼", "シドニー"),
    "syd-20261007": ("au", "Sydney", "悉尼", "シドニー"),
    "maa-20260829": ("in", "Chennai", "钦奈", "チェンナイ"),
    "vad-20260905": ("in", "Vadodara", "巴罗达", "ヴァドーダラー"),
    "nij-20260902": ("nl", "Nijmegen", "奈梅亨", "ナイメーヘン"),
    "utr-20261029": ("nl", "Utrecht", "乌得勒支", "ユトレヒト"),
    "ams-20260922": ("nl", "Amsterdam", "阿姆斯特丹", "アムステルダム"),
    "cph-20260909": ("dk", "Copenhagen", "哥本哈根", "コペンハーゲン"),
    "yde-20260910": ("cm", "Yaoundé", "雅温得", "ヤウンデ"),
    "tia-20260917": ("al", "Tirana", "地拉那", "ティラナ"),
    "ygn-20260926": ("mm", "Yangon", "仰光", "ヤンゴン"),
    "sg-20260904": ("sg", "Singapore", "新加坡", "シンガポール"),
    "xela-20260920": ("gt", "Quetzaltenango", "克萨尔特南戈", "ケツァルテナンゴ"),
    "gua-20261003": ("gt", "Guatemala City", "危地马拉城", "グアテマラシティ"),
    "rec-20260923": ("br", "Recife", "累西腓", "レシフェ"),
    "cwb-20261111": ("br", "Curitiba", "库里蒂巴", "クリチバ"),
    "sal-20260919": ("sv", "San Salvador", "圣萨尔瓦多", "サンサルバドル"),
    "ldn-20260916": ("gb", "London", "伦敦", "ロンドン"),
    "gtm-20260826": ("online", "GTM workshop", "GTM 课", "GTM"),
    "pbp-20260902": ("online", "Product practice", "产品实践课", "プロダクト実践"),
    "ru-20260903": ("us", "New Brunswick / Rutgers", "罗格斯 新布朗斯维克", "Rutgers / New Brunswick"),
    "utep-20260903": ("us", "UTEP / El Paso", "UTEP 埃尔帕索", "UTEP / El Paso"),
    "lc-20260903": ("us", "Salisbury / Livingstone", "索尔兹伯里 Livingstone", "Salisbury / Livingstone"),
    "dpu-20260903": ("us", "Greencastle / DePauw", "格林卡斯尔 DePauw", "Greencastle / DePauw"),
    "sfi-20260904": ("us", "San Francisco", "旧金山", "サンフランシスコ"),
    "hnl-20260905": ("us", "Honolulu", "檀香山", "ホノルル"),
    "amd-20260912": ("in", "Ahmedabad", "艾哈迈达巴德", "アーメダバード"),
    "bli-20260915": ("id", "Uluwatu / Bali", "巴厘岛乌鲁瓦图", "ウルワツ / バリ"),
    "g101-20260915": ("us", "San Francisco", "旧金山", "サンフランシスコ"),
    "sfe-20260915": ("us", "San Francisco", "旧金山", "サンフランシスコ"),
    "sfse-20260916": ("us", "San Francisco", "旧金山", "サンフランシスコ"),
    "sfsdr-20260916": ("us", "San Francisco", "旧金山", "サンフランシスコ"),
    "sfmo-20260917": ("us", "San Francisco", "旧金山", "サンフランシスコ"),
    "sfps-20260917": ("us", "San Francisco", "旧金山", "サンフランシスコ"),
    "sfm-20260917": ("us", "San Francisco", "旧金山", "サンフランシスコ"),
    "etamu-20260903": ("us", "East Texas A&M / Commerce", "东德州农工 Commerce", "East Texas A&M / Commerce"),
    "prt-20260909": ("pt", "Porto", "波尔图", "ポルト"),
    "leu-20260919": ("be", "Leuven", "鲁汶", "ルーヴェン"),
    "fln-20260926": ("br", "Florianópolis", "弗洛里亚诺波利斯", "フロリアノポリス"),
    "bliw-20261004": ("id", "Jimbaran / Bali (Udayana)", "巴厘岛金巴兰（乌达亚纳）", "ジンバラン / バリ（Udayana）"),
    "sha-20261017": ("cn", "Shanghai", "上海", "上海"),
    "hzo-20260905": ("cn", "Hangzhou", "杭州", "杭州"),
    "hzo-20260919": ("cn", "Hangzhou", "杭州", "杭州"),
    "sfpm-20260915": ("us", "San Francisco (PMs)", "旧金山（产品经理）", "サンフランシスコ（PM）"),
    "sffo-20260915": ("us", "San Francisco (Founders)", "旧金山（创始人）", "サンフランシスコ（Founders）"),
    "sfsales-20260916": ("us", "San Francisco (Sales)", "旧金山（销售）", "サンフランシスコ（Sales）"),
    "frb-20260917": ("de", "Freiburg", "弗赖堡", "フライブルク"),
    "bj-20260919": ("cn", "Beijing", "北京", "北京"),
    "bdg-20260919": ("id", "Bandung", "万隆", "バンドン"),
    "cuu-20260924": ("mx", "Chihuahua", "奇瓦瓦", "チワワ"),
    "cdmx-20260926": ("mx", "Mexico City", "墨西哥城", "メキシコシティ"),
}


def event_geo(ev: dict) -> tuple[str, dict[str, str]]:
    eid = ev.get("id") or ""
    if eid in EVENT_GEO:
        code, en, zh, ja = EVENT_GEO[eid]
        return code, {"en": en, "zh": zh, "ja": ja}
    where = " ".join(
        str((ev.get("where") or {}).get(k, "")) for k in ("en", "zh", "ja")
    ) + " " + " ".join(str((ev.get("title") or {}).get(k, "")) for k in ("en", "zh", "ja"))
    # HK / TW / Macau always China.
    if any(k in where for k in ("香港", "Hong Kong", "台湾", "Taiwan", "澳門", "澳门", "Macau", "Macao")):
        place = "Macao" if any(k in where for k in ("澳门", "澳門", "Macau", "Macao")) else (
            "Hong Kong" if any(k in where for k in ("香港", "Hong Kong")) else "Taiwan"
        )
        zh_place = {"Macao": "澳门", "Hong Kong": "香港", "Taiwan": "台湾"}[place]
        ja_place = {"Macao": "マカオ", "Hong Kong": "香港", "Taiwan": "台湾"}[place]
        return "cn", {"en": place, "zh": zh_place, "ja": ja_place}
    if any(k in where for k in ("Zoom", "线上", "Online", "オンライン")):
        return "online", {"en": "Online", "zh": "线上", "ja": "オンライン"}
    title = (ev.get("title") or {}).get("zh") or (ev.get("title") or {}).get("en") or eid
    return "other", {"en": title, "zh": title, "ja": title}


def grouped_events(events: list[dict]) -> list[tuple[str, list[dict]]]:
    buckets: dict[str, list[dict]] = {}
    for ev in events:
        code, _ = event_geo(ev)
        buckets.setdefault(code, []).append(ev)
    codes = list(buckets)
    codes.sort(key=lambda c: (0 if c == "cn" else 2 if c == "online" else 1, -len(buckets[c]), c))
    return [(c, buckets[c]) for c in codes]


def first_sentence(text: str, lang: str) -> str:
    text = (text or "").strip()
    if not text:
        return text
    if lang in ("zh", "ja"):
        head, sep, _ = text.partition("。")
        return (head + "。") if sep else text
    head, sep, _ = text.partition(". ")
    if sep:
        return head.rstrip(".") + "."
    return text.rstrip(".") + "."


def render_events_index(lang: str, chrome: dict) -> str:
    events = active_events()
    if not events:
        return ""
    more = EVENTS_NAME[lang]
    blocks = [
        f"## {chrome['events']}",
        "",
        f"[{chrome['events_more']}](./{more})",
        "",
    ]
    for code, group in grouped_events(events):
        country = COUNTRY_LABEL[code][lang]
        links = []
        for ev in group:
            _, place = event_geo(ev)
            links.append(f"[{place[lang]}](./{more}#{ev['id']})")
        blocks.append(f"- **{country}**（{len(group)}）：{' · '.join(links)}")
    blocks.append("")
    return "\n".join(blocks)


def render_event_card(ev: dict, lang: str) -> str:
    title = ev["title"][lang]
    when = ev["when"][lang]
    where = ev["where"][lang]
    body = ev["body"][lang]
    cta = ev["cta"][lang]
    img = ev.get("image", "")
    url = ev["url"]
    eid = ev.get("id", "")
    return (
        f'<a id="{eid}"></a>\n'
        f'<table><tr>'
        f'<td width="320" valign="top">'
        f'<a href="{url}"><img src="{img}" alt="{title}" width="300" /></a>'
        f"</td>"
        f'<td valign="top">'
        f"<strong>{title}</strong><br />"
        f"{when}<br />"
        f"{where}<br /><br />"
        f"{body}<br /><br />"
        f'<a href="{url}"><strong>{cta} →</strong></a>'
        f"</td>"
        f"</tr></table>"
    )


def render_events_page(lang: str) -> str:
    chrome = CHROME[lang]
    events = active_events()
    readme = README_NAME[lang]
    lines = [
        f'# {chrome["events"]}',
        "",
        f'<p align="center">{events_switcher(lang)}</p>',
        "",
        chrome["events_page_lead"],
        "",
        f'[{chrome["events_back"]}](./{readme})',
        "",
    ]
    if not events:
        return "\n".join(lines)
    for code, group in grouped_events(events):
        country = COUNTRY_LABEL[code][lang]
        lines.append(f'<a id="country-{code}"></a>')
        lines.append(f"### {country}")
        lines.append("")
        for ev in group:
            lines.append(render_event_card(ev, lang))
            lines.append("")
    return "\n".join(lines)

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
  <img src="./assets/wechat/mp-search-scan.png" alt="{chrome["group_alt"]}" width="280" />
  &nbsp;&nbsp;&nbsp;
  <img src="./assets/wechat/personal-qr.png" alt="{chrome["friend_alt"]}" width="140" />
</p>
<p align="center"><sub>{chrome["qr_sub"]}</sub></p>

> {product} {chrome["unofficial"]}
"""

    events_md = render_events_index(lang, chrome)
    lines = [intro]
    if events_md:
        lines += [events_md]
    lines += [f"## {chrome['toc']}", ""]
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
        (ROOT / EVENTS_NAME[lang]).write_text(render_events_page(lang), encoding="utf-8")
    print("entries", count_items(), "sections", len(CAT["sections"]), "langs", ",".join(LANGS), "events", len(active_events()))


if __name__ == "__main__":
    main()
