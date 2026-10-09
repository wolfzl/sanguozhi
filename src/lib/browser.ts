import { normalizeSearch } from "./search.mjs";
let toastTimer: ReturnType<typeof setTimeout>;
function announce(message: string) {
  const toast = document.querySelector<HTMLElement>("[data-toast]");
  if (!toast) return;
  toast.textContent = message;
  toast.classList.add("visible");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove("visible"), 3500);
}
async function copyLink() {
  const url = location.href;
  try {
    await navigator.clipboard.writeText(url);
  } catch {
    const input = document.createElement("textarea");
    input.value = url;
    input.style.position = "fixed";
    input.style.left = "-9999px";
    document.body.append(input);
    input.select();
    let copied = false;
    try {
      copied = document.execCommand("copy");
    } finally {
      input.remove();
    }
    if (!copied) {
      announce("复制未成功，请从浏览器地址栏复制链接");
      return;
    }
  }
  announce("链接已复制");
}
for (const button of document.querySelectorAll<HTMLButtonElement>(
  "[data-copy]",
))
  button.addEventListener("click", () => {
    void copyLink();
  });
for (const button of document.querySelectorAll<HTMLButtonElement>(
  "[data-share]",
))
  button.addEventListener("click", async () => {
    const payload = {
      title: document.title,
      text: document.querySelector<HTMLMetaElement>('meta[name="description"]')
        ?.content,
      url: location.href,
    };
    if (navigator.share) {
      try {
        await navigator.share(payload);
        return;
      } catch (error) {
        if (error instanceof DOMException && error.name === "AbortError")
          return;
      }
    }
    await copyLink();
  });
for (const root of document.querySelectorAll<HTMLElement>(
  "[data-search-root]",
)) {
  const input = root.querySelector<HTMLInputElement>('input[type="search"]');
  const cards = [...root.querySelectorAll<HTMLElement>("[data-search-card]")];
  const count = root.querySelector<HTMLElement>("[data-count]");
  const empty = root.querySelector<HTMLElement>("[data-empty]");
  const filters = [
    ...root.querySelectorAll<HTMLButtonElement>("[data-filter]"),
  ];
  let faction = "all";
  function update() {
    const query = normalizeSearch(input?.value ?? "");
    let visible = 0;
    for (const card of cards) {
      const match =
        (faction === "all" || card.dataset.faction === faction) &&
        (card.dataset.search ?? "").includes(query);
      card.hidden = !match;
      if (match) visible++;
    }
    if (count) count.textContent = String(visible);
    if (empty) empty.hidden = visible !== 0;
  }
  input?.addEventListener("input", update);
  for (const filter of filters)
    filter.addEventListener("click", () => {
      faction = filter.dataset.filter ?? "all";
      for (const f of filters)
        f.setAttribute("aria-pressed", String(f === filter));
      update();
    });
  root.querySelector("[data-reset]")?.addEventListener("click", () => {
    if (input) input.value = "";
    faction = "all";
    for (const f of filters)
      f.setAttribute("aria-pressed", String(f.dataset.filter === "all"));
    update();
    input?.focus();
  });
  update();
}
const reader = document.querySelector<HTMLElement>("[data-reader]");
const noteButton = document.querySelector<HTMLButtonElement>("[data-notes]");
let showNotes = true;
try {
  showNotes = sessionStorage.getItem("sanguo-show-notes") !== "false";
} catch {}
function setNotes(value: boolean) {
  showNotes = value;
  reader?.classList.toggle("hide-notes", !value);
  noteButton?.setAttribute("aria-pressed", String(value));
  const label = noteButton?.querySelector("[data-note-state]");
  if (label) label.textContent = value ? "显示裴注" : "裴注已隐藏";
  try {
    sessionStorage.setItem("sanguo-show-notes", String(value));
  } catch {}
}
if (reader) setNotes(showNotes);
noteButton?.addEventListener("click", () => setNotes(!showNotes));
function revealTarget() {
  if (!location.hash) return;
  let id: string;
  try {
    id = decodeURIComponent(location.hash.slice(1));
  } catch {
    return;
  }
  const target = document.getElementById(id);
  if (!target) return;
  const detail = target.closest("details");
  if (detail) detail.open = true;
  if (target.classList.contains("peizhu") || target.closest(".peizhu"))
    setNotes(true);
  requestAnimationFrame(() => target.scrollIntoView({ block: "start" }));
}
window.addEventListener("hashchange", revealTarget);
revealTarget();
const selector = document.querySelector<HTMLSelectElement>(
  "[data-volume-select]",
);
selector?.addEventListener("change", () => {
  if (selector.value) location.assign(`/read/${selector.value}/`);
});
