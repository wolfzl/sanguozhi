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
