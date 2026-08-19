const I18N = {
  en: {
    "nav.playbook": "Playbook",
    "nav.catalog": "Catalog",
    "nav.prompts": "Prompts",
    "hero.lede": "Grok Bot is the always-on AI teammate launched 2026-08-11. Each Bot shares one persistent cloud computer and keeps working after you close the laptop. This list is not grok.com chat, Grok Imagine, or a Grok 4.x model writeup.",
    "stat.entries": "entries",
    "stat.sections": "sections",
    "stat.prompts": "playbook prompts",
    "playbook.title": "Playbook — read this first",
    "search": "Search titles and blurbs",
    "prompts.title": "Playbook prompts",
    "prompts.note": "Paste into a named Bot. Start read-only. Draw the approval line on irreversible actions.",
    "footer": "Unofficial community list. Not affiliated with xAI/SpaceXAI or Cursor. Content CC0.",
    "all": "All",
    "rules": [
      "One computer, not one machine per Bot. Logins and files are visible to every Bot on the account.",
      "Draw the approval line on irreversible actions. Auto Review + take over for 2FA.",
      "The cloud computer hits site risk controls. X login locks and captchas show up in real threads.",
      "Reconnect can drop state. Rebuilding the bridge or deleting the Cursor account can orphan the Bot.",
      "Heavy / Ultra / Teams Premium is a gate, not infinite quota. Usage resets weekly.",
      "Linux desktop is not first-class. Community packs exist; official desktop is macOS / Windows + iOS."
    ]
  },
  zh: {
    "nav.playbook": "玩法",
    "nav.catalog": "清单",
    "nav.prompts": "提示词",
    "hero.lede": "Grok Bot 是 2026-08-11 上线的 always-on 云电脑队友。每个 Bot 共享一台持久云电脑，合上笔记本也不停。本清单不是 grok.com 聊天、Grok Imagine，也不是 Grok 4.x 模型评测。",
    "stat.entries": "条目",
    "stat.sections": "分类",
    "stat.prompts": "玩法提示词",
    "playbook.title": "玩法 — 先读这段",
    "search": "搜索标题和说明",
    "prompts.title": "玩法提示词",
    "prompts.note": "贴进一个有名字的 Bot。先只读。审批线画在不可逆动作上。",
    "footer": "非官方社区清单，与 xAI/SpaceXAI 或 Cursor 无隶属关系。内容 CC0。",
    "all": "全部",
    "rules": [
      "一台电脑，不是一人一机。登录和文件对账号下全部 Bot 可见。",
      "审批线画在不可逆动作上。Auto Review + 2FA Take over。",
      "云电脑会撞上站点风控。X 登录锁、验证码在真实帖里反复出现。",
      "重连会丢状态。重建桥或删 Cursor 号可能把 Bot 绑死。",
      "Heavy / Ultra / Teams Premium 是门槛不是无限。用量按周重置。",
      "Linux 桌面不是一等公民。社区有打包；官方桌面是 macOS / Windows + iOS。"
    ]
  }
};

const params = new URLSearchParams(location.search);
const state = {
  lang: params.get("lang") || localStorage.getItem("agb-lang") || "en",
  chip: "all",
  q: "",
  catalog: null,
  prompts: null,
};

function t(key) {
  return I18N[state.lang][key];
}

function applyStatic() {
  document.documentElement.lang = state.lang === "zh" ? "zh-CN" : "en";
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    el.textContent = t(el.dataset.i18n);
  });
  document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
    el.placeholder = t(el.dataset.i18nPlaceholder);
  });
  document.querySelectorAll(".lang button").forEach((b) => {
    b.classList.toggle("on", b.dataset.lang === state.lang);
  });
  const rules = I18N[state.lang].rules
    .map((line) => `<li>${line}</li>`)
    .join("");
  document.getElementById("playbook-list").innerHTML = rules;
}

function renderChips() {
  const chips = document.getElementById("chips");
  const items = [{ id: "all", title: { en: t("all"), zh: t("all") } }, ...state.catalog.sections];
  chips.innerHTML = items
    .map((s) => {
      const label = s.id === "all" ? t("all") : s.title[state.lang];
      const on = state.chip === s.id ? "on" : "";
      return `<button class="${on}" data-chip="${s.id}">${label}</button>`;
    })
    .join("");
}

function renderCatalog() {
  const q = state.q.trim().toLowerCase();
  const groups = document.getElementById("groups");
  groups.innerHTML = state.catalog.sections
    .filter((s) => state.chip === "all" || s.id === state.chip)
    .map((s) => {
      const items = s.items.filter((it) => {
        if (!q) return true;
        const blob = `${it.title} ${it.blurb.en} ${it.blurb.zh}`.toLowerCase();
        return blob.includes(q);
      });
      if (!items.length) return "";
      const lis = items
        .map(
          (it) =>
            `<a class="item" href="${it.url}" rel="noopener" target="_blank"><b>${it.title}</b><span>${it.blurb[state.lang]}</span></a>`
        )
        .join("");
      return `<section class="group" id="${s.id}"><h2>${s.title[state.lang]} <small class="muted">${items.length}</small></h2>${lis}</section>`;
    })
    .join("");
}

function renderPrompts() {
  const box = document.getElementById("prompt-list");
  box.innerHTML = (state.prompts.prompts || [])
    .map((p) => {
      const role = p.role[state.lang];
      const use = p.use[state.lang];
      return `<article class="card"><h3>${p.id}. ${role}</h3><p class="muted">${use}</p><pre>${p.prompt}</pre></article>`;
    })
    .join("");
}

function refresh() {
  applyStatic();
  if (!state.catalog) return;
  const n = state.catalog.sections.reduce((a, s) => a + s.items.length, 0);
  document.getElementById("stat-entries").textContent = n;
  document.getElementById("stat-sections").textContent = state.catalog.sections.length;
  renderChips();
  renderCatalog();
  if (state.prompts) renderPrompts();
}

document.querySelector(".lang").addEventListener("click", (e) => {
  const btn = e.target.closest("button[data-lang]");
  if (!btn) return;
  state.lang = btn.dataset.lang;
  localStorage.setItem("agb-lang", state.lang);
  const url = new URL(location.href);
  url.searchParams.set("lang", state.lang);
  history.replaceState(null, "", url);
  refresh();
});
document.getElementById("chips").addEventListener("click", (e) => {
  const btn = e.target.closest("button[data-chip]");
  if (!btn) return;
  state.chip = btn.dataset.chip;
  refresh();
});
document.getElementById("q").addEventListener("input", (e) => {
  state.q = e.target.value;
  renderCatalog();
});

Promise.all([
  fetch("./catalog.json").then((r) => r.json()),
  fetch("./prompts.json").then((r) => r.json()),
]).then(([catalog, prompts]) => {
  state.catalog = catalog;
  state.prompts = prompts;
  refresh();
});
