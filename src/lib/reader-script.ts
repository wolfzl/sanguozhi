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
  function setScript(script: 'simplified' | 'traditional', keepPosition = false) {
    // Keep the current paragraph in view when its line breaks change.
    const toolbarBottom = document.querySelector('.reader-toolbar')?.getBoundingClientRect().bottom ?? 0;
    const visible = keepPosition ? [...reader!.querySelectorAll<HTMLElement>('[id]')].filter(el => {
      const box = el.getBoundingClientRect();
      return box.bottom > toolbarBottom && box.top < innerHeight;
    }) : [];
    const anchor = visible.find(el => el.getBoundingClientRect().top >= toolbarBottom) ?? visible.at(-1);
    const top = anchor?.getBoundingClientRect().top;
    for (const text of texts) text.node.data = script === 'simplified' ? text.simplified : text.original;
    reader!.lang = script === 'simplified' ? 'zh-Hans' : 'zh-Hant';
    for (const button of buttons) button.setAttribute('aria-pressed', String(button.dataset.readerScript === script));
    if (stateLabel) stateLabel.textContent = script === 'simplified' ? '当前显示简体转换文字，可切换繁体底本对照。' : '当前显示繁体底本，可切换简体阅读。';
    try { localStorage.setItem('sanguo-reader-script', script); } catch {}
    if (anchor && top !== undefined) window.scrollBy(0, anchor.getBoundingClientRect().top - top);
  }
  let preferred: 'simplified' | 'traditional' = 'simplified';
  try {
    if (localStorage.getItem('sanguo-reader-script') === 'traditional') preferred = 'traditional';
  } catch {}
  setScript(preferred);
  controls.hidden = false;
  for (const button of buttons) button.addEventListener('click', () => {
    setScript(button.dataset.readerScript === 'traditional' ? 'traditional' : 'simplified', true);
  });
  // Initial conversion may change the height above a card's citation target.
  if (location.hash) {
    try {
      const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      if (target && reader.contains(target)) requestAnimationFrame(() => target.scrollIntoView({block:'start'}));
    } catch {}
  }
}
