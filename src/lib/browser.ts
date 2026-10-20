import { normalizeSearch } from "./search.mjs";
import { parseTimelineState, encodeTimelineState, categories, layoutYearEvents } from "./timeline.mjs";
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

// The event explorer uses one canonical DOM card per event in both views.
const timelineRoot = document.querySelector<HTMLElement>("[data-timeline-root]");
if (timelineRoot) {
  const input = timelineRoot.querySelector<HTMLInputElement>('input[type="search"]');
  const cards = [...timelineRoot.querySelectorAll<HTMLElement>("[data-search-card]")];
  const buttons = [...timelineRoot.querySelectorAll<HTMLButtonElement>("[data-timeline-filter]")];
  const timeline = timelineRoot.querySelector<HTMLElement>(".timeline");
  let state = parseTimelineState(location.search);
  let searchTimer: ReturnType<typeof setTimeout>;
  function updateTimeline() {
    const query = normalizeSearch(state.q);
    let visible = 0;
    for (const card of cards) {
      const match = (state.importance === "all" || card.dataset.importance === "key") && (state.lane === "all" || (card.dataset.lanes?.split(" ").includes(state.lane) || (state.lane === "lords" && card.dataset.lanes?.split(" ").includes("common")))) && (state.category === "all" || card.dataset.categories?.split(" ").includes(state.category)) && (card.dataset.search ?? "").includes(query);
      card.hidden = !match;
      if (match) visible++;
    }
    for (const group of timelineRoot!.querySelectorAll<HTMLElement>("[data-year-group], [data-phase]")) group.hidden = ![...group.querySelectorAll<HTMLElement>("[data-search-card]")].some(card => !card.hidden);
    for (const group of timelineRoot!.querySelectorAll<HTMLElement>("[data-year-group]")) {
      const shown = [...group.querySelectorAll<HTMLElement>("[data-search-card]")].filter(card => !card.hidden);
      const placements = layoutYearEvents(shown.map(card => ({lanes:(card.dataset.lanes ?? "").split(" ")})));
      shown.forEach((card,index) => card.style.setProperty("--lane-row",String(placements[index].row)));
    }
    for (const button of buttons) button.setAttribute("aria-pressed", String(state[button.dataset.timelineFilter as keyof typeof state] === button.dataset.value));
    const count = timelineRoot!.querySelector("[data-count]");
    if (count) count.textContent = String(visible);
    const empty = timelineRoot!.querySelector<HTMLElement>("[data-empty]");
    if (empty) empty.hidden = visible !== 0;
    if (timeline) {
      timeline.dataset.timelineView = state.view;
      timeline.classList.toggle("timeline-single", state.lane !== "all");
      for (const element of timeline.querySelectorAll<HTMLElement>("[data-track-lane], [data-header-lane], [data-rail-lane]")) {
        const lane = element.dataset.trackLane ?? element.dataset.headerLane ?? element.dataset.railLane;
        element.hidden = state.lane !== "all" && lane !== state.lane;
      }
    }
    const categoryLabel = timelineRoot!.querySelector("[data-category-label]");
    if (categoryLabel) categoryLabel.textContent = state.category === "all" ? "全部类型" : categories[state.category as keyof typeof categories];
  }
  function syncURL(push: boolean) {
    const next = new URL(location.href);
    const encoded = new URLSearchParams(encodeTimelineState(state));
    for (const name of ["importance","lane","category","q","view"]) {
      next.searchParams.delete(name);
      if (encoded.has(name)) next.searchParams.set(name,encoded.get(name)!);
    }
    if (next.href !== location.href) history[push ? "pushState" : "replaceState"](null,"",next);
    try { sessionStorage.setItem("sanguo-timeline-url",next.pathname+next.search+next.hash); } catch {}
  }
  function restore() {
    clearTimeout(searchTimer);
    state = parseTimelineState(location.search);
    if (input) input.value = state.q;
    if (state.category !== "all") {
      const detail = timelineRoot!.querySelector<HTMLDetailsElement>(".timeline-type-filter");
      if (detail) detail.open = true;
    }
    updateTimeline();
    try { sessionStorage.setItem("sanguo-timeline-url",location.pathname+location.search+location.hash); } catch {}
  }
  input?.addEventListener("input", () => {
    state.q = input.value;
    updateTimeline();
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => syncURL(false), 180);
  });
  // Save immediately before following a result; back restores the current query.
  timelineRoot.addEventListener("click", (event) => {
    if ((event.target as Element).closest("a[href]")) {
      clearTimeout(searchTimer);
      syncURL(false);
    }
  });
  for (const button of buttons) button.addEventListener("click", () => {
    clearTimeout(searchTimer);
    const next = {...state,[button.dataset.timelineFilter!]:button.dataset.value};
    state = parseTimelineState(encodeTimelineState(next));
    updateTimeline();
    syncURL(true);
  });
  function reset(all = false) {
    clearTimeout(searchTimer);
    state = parseTimelineState(all ? "?importance=all" : "");
    if (input) input.value = "";
    updateTimeline(); syncURL(true);
  }
  timelineRoot.querySelector("[data-reset]")?.addEventListener("click", () => reset());
  timelineRoot.querySelector("[data-empty-reset]")?.addEventListener("click", () => reset(true));
  window.addEventListener("popstate",restore);
  window.addEventListener("pageshow",restore);
  restore();
}

try {
  const remembered = sessionStorage.getItem("sanguo-timeline-url");
  if (remembered) {
    const url = new URL(remembered,location.origin);
    if (url.origin === location.origin && url.pathname === "/events/") for (const link of document.querySelectorAll<HTMLAnchorElement>("[data-timeline-back]")) link.href = url.pathname + url.search + url.hash;
  }
} catch {}
