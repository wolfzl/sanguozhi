import { Converter } from 'opencc-js/t2cn';

const reader = document.querySelector<HTMLElement>('[data-reader]');
const controls = document.querySelector<HTMLElement>('[data-script-controls]');
if (reader && controls) {
  const simplify = Converter({from: 't', to: 'cn'});
  const walker = document.createTreeWalker(reader, NodeFilter.SHOW_TEXT);
  const texts: {node: Text; original: string; simplified: string}[] = [];
  while (walker.nextNode()) {
    const node = walker.currentNode as Text;
    const original = node.data;
    texts.push({node, original, simplified: simplify(original)});
  }
  const buttons = [...controls.querySelectorAll<HTMLButtonElement>('[data-reader-script]')];
  const stateLabel = document.querySelector<HTMLElement>('[data-reader-script-state]');
  const typeLabel = document.querySelector<HTMLElement>('[data-reader-type]');
  const template = document.querySelector<HTMLTemplateElement>('template[data-baihua]');
  const sourceNodes = [...reader.childNodes];
  const baihuaNodes = template ? [...template.content.cloneNode(true).childNodes] : [];
  let showingBaihua = false;
  const banner = document.querySelector<HTMLElement>('[data-baihua-banner]');
  const parallelButton = document.querySelector<HTMLButtonElement>('[data-parallel]');
  // 逐段对照：按原文块编号（与白话块 id 一一对应）把简体原文挂在每段白话下方。
  // 懒生成，且去掉所有 id 与 peizhu 类名，避免与白话块里的锚点重复。
  const sourceById = new Map<string, Element>();
  for (const node of sourceNodes) if (node instanceof Element && node.id) sourceById.set(node.id, node);
  let parallelReady = false;
  let showParallel = false;
  function buildParallel() {
    if (parallelReady) return;
    parallelReady = true;
    for (const block of baihuaNodes) {
      if (!(block instanceof HTMLElement) || !block.classList.contains('baihua-block')) continue;
      const source = sourceById.get(block.id);
      if (!source) continue;
      const clone = source.cloneNode(true) as Element;
      for (const el of [clone, ...clone.querySelectorAll('*')]) {
        el.removeAttribute('id');
        if (el.classList.contains('peizhu')) { el.classList.remove('peizhu'); el.classList.add('parallel-note'); }
      }
      const walker = document.createTreeWalker(clone, NodeFilter.SHOW_TEXT);
      while (walker.nextNode()) { const text = walker.currentNode as Text; text.data = simplify(text.data); }
      const wrap = document.createElement('div');
      wrap.className = 'parallel-source';
      wrap.lang = 'zh-Hans';
      const label = document.createElement('span');
      label.className = 'parallel-label';
      label.textContent = '原文';
      const body = document.createElement('div');
      body.className = 'parallel-body';
      // 段落与标题只取内容（避免标题样式、首行缩进影响对照行）；表格、列表、引文保持原结构。
      if (/^(P|H[1-6]|DIV)$/.test(clone.tagName)) body.append(...clone.childNodes);
      else body.append(clone);
      wrap.append(label, body);
      block.append(wrap);
    }
  }
  function setParallel(value: boolean, persist = true) {
    showParallel = value;
    if (value) buildParallel();
    reader!.classList.toggle('show-parallel', value);
    parallelButton?.setAttribute('aria-pressed', String(value));
    if (persist) try { localStorage.setItem('sanguo-reader-parallel', String(value)); } catch {}
  }
  type ReaderMode = 'simplified' | 'traditional' | 'baihua';
  function setScript(script: ReaderMode, keepPosition = false, persist = true) {
    // Keep the current paragraph in view when its line breaks change.
    const toolbarBottom = document.querySelector('.reader-toolbar')?.getBoundingClientRect().bottom ?? 0;
    const visible = keepPosition ? [...reader!.querySelectorAll<HTMLElement>('[id]')].filter(el => {
      const box = el.getBoundingClientRect();
      return box.bottom > toolbarBottom && box.top < innerHeight;
    }) : [];
    const anchor = visible.find(el => el.getBoundingClientRect().top >= toolbarBottom) ?? visible.at(-1);
    const anchorId = anchor?.id;
    const top = anchor?.getBoundingClientRect().top;
    const height = anchor?.getBoundingClientRect().height;
    const wantBaihua = script === 'baihua';
    if (wantBaihua !== showingBaihua) {
      reader!.replaceChildren(...(wantBaihua ? baihuaNodes : sourceNodes));
      showingBaihua = wantBaihua;
    }
    if (!wantBaihua) for (const text of texts) text.node.data = script === 'simplified' ? text.simplified : text.original;
    reader!.lang = script === 'traditional' ? 'zh-Hant' : 'zh-Hans';
    for (const button of buttons) button.setAttribute('aria-pressed', String(button.dataset.readerScript === script));
    if (stateLabel) stateLabel.textContent = wantBaihua ? '当前显示白话试译（AI 辅助翻译），可切换简繁原文核对。' : script === 'simplified' ? '当前显示简体转换文字，可切换繁体底本对照。' : '当前显示繁体底本，可切换简体阅读。';
    if (typeLabel) typeLabel.textContent = wantBaihua ? '白话试译' : '原文';
    if (banner) banner.hidden = !wantBaihua;
    if (parallelButton) parallelButton.hidden = !wantBaihua;
    reader!.classList.toggle('is-baihua', wantBaihua);
    if (persist) try {
      localStorage.setItem('sanguo-reader-mode', script);
      if (!wantBaihua) localStorage.setItem('sanguo-reader-script', script);
    } catch {}
    const newAnchor = anchorId ? document.getElementById(anchorId) : undefined;
    if (newAnchor && top !== undefined) {
      const box = newAnchor.getBoundingClientRect();
      // Long translations may shrink below the old offset; retain progress
      // within the paragraph or note so it remains the active reading block.
      const desiredTop = top < toolbarBottom && height
        ? toolbarBottom - Math.min(1, (toolbarBottom - top) / height) * box.height
        : top;
      window.scrollBy({top: box.top - desiredTop, behavior: 'instant'});
    }
  }
  let preferred: ReaderMode = 'simplified';
  try {
    if (localStorage.getItem('sanguo-reader-script') === 'traditional') preferred = 'traditional';
    if (localStorage.getItem('sanguo-reader-mode') === 'baihua' && template) preferred = 'baihua';
  } catch {}
  setScript(preferred, false, false);
  try { if (localStorage.getItem('sanguo-reader-parallel') === 'true' && template) setParallel(true, false); } catch {}
  parallelButton?.addEventListener('click', () => setParallel(!showParallel));
  controls.hidden = false;
  for (const button of buttons) button.addEventListener('click', () => {
    const mode = button.dataset.readerScript;
    setScript(mode === 'baihua' && template ? 'baihua' : mode === 'traditional' ? 'traditional' : 'simplified', true);
  });
  // Initial conversion may change the height above a card's citation target.
  if (location.hash) {
    try {
      const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      if (target && reader.contains(target)) requestAnimationFrame(() => target.scrollIntoView({block:'start'}));
    } catch {}
  }
}
