// 引用角标 [n]：悬停/点击时就地弹出该条依据的出处与节选，数据取自页底「原文依据」。
// 没有 JS 时，角标仍是指向 #source-n 的普通锚点。
const links = [...document.querySelectorAll<HTMLAnchorElement>('.citations a[href^="#source-"]')];
if (links.length) {
  const pop = document.createElement('div');
  pop.className = 'cite-pop';
  pop.setAttribute('role', 'dialog');
  pop.hidden = true;
  const label = document.createElement('div');
  label.className = 'cite-pop-label';
  const quote = document.createElement('blockquote');
  quote.lang = 'zh-Hans';
  const actions = document.createElement('div');
  actions.className = 'cite-pop-actions';
  const toSource = document.createElement('a');
  toSource.textContent = '查看页底依据 ↓';
  const toRead = document.createElement('a');
  toRead.textContent = '阅读完整原文 ↗';
  actions.append(toSource, toRead);
  pop.append(label, quote, actions);
  document.body.append(pop);

  let current: HTMLAnchorElement | null = null;
  let pinned = false;
  let timer: ReturnType<typeof setTimeout> | undefined;
  const canHover = matchMedia('(hover: hover) and (pointer: fine)');

  function fill(anchor: HTMLAnchorElement) {
    const item = document.getElementById(anchor.getAttribute('href')!.slice(1));
    if (!item) return false;
    const spans = item.querySelectorAll<HTMLElement>('summary > span');
    label.textContent = `依据 ${spans[0]?.textContent?.trim() ?? ''} · ${spans[1]?.textContent?.trim() ?? ''}`;
    quote.textContent = item.querySelector('blockquote')?.textContent ?? '';
    toSource.href = anchor.getAttribute('href')!;
    const read = item.querySelector<HTMLAnchorElement>('.source-actions a');
    toRead.href = read?.href ?? '#';
    toRead.hidden = !read;
    pop.setAttribute('aria-label', label.textContent);
    return true;
  }
  function place(anchor: HTMLAnchorElement) {
    const box = anchor.getBoundingClientRect();
    const width = pop.offsetWidth;
    const height = pop.offsetHeight;
    const left = Math.min(Math.max(12, box.left + box.width / 2 - width / 2), innerWidth - width - 12);
    const above = box.bottom + height + 14 > innerHeight && box.top > height + 14;
    pop.style.left = `${left + scrollX}px`;
    pop.style.top = `${(above ? box.top - height - 8 : box.bottom + 8) + scrollY}px`;
  }
  function show(anchor: HTMLAnchorElement, pin: boolean) {
    clearTimeout(timer);
    if (!fill(anchor)) return;
    current?.removeAttribute('aria-expanded');
    current = anchor;
    pinned = pin;
    anchor.setAttribute('aria-expanded', 'true');
    pop.hidden = false;
    place(anchor);
  }
  function hide() {
    clearTimeout(timer);
    pop.hidden = true;
    pinned = false;
    current?.removeAttribute('aria-expanded');
    current = null;
  }
  const later = () => { clearTimeout(timer); timer = setTimeout(() => { if (!pinned) hide(); }, 220); };

  for (const anchor of links) {
    anchor.setAttribute('aria-haspopup', 'dialog');
    anchor.addEventListener('mouseenter', () => {
      if (!canHover.matches || pinned) return;
      clearTimeout(timer);
      timer = setTimeout(() => show(anchor, false), 120);
    });
    anchor.addEventListener('mouseleave', () => { if (canHover.matches) later(); });
    anchor.addEventListener('click', event => {
      if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      if (current === anchor && !pop.hidden && pinned) hide();
      else show(anchor, true);
    });
  }
  pop.addEventListener('mouseenter', () => clearTimeout(timer));
  pop.addEventListener('mouseleave', () => { if (canHover.matches) later(); });
  toSource.addEventListener('click', () => hide());
  document.addEventListener('click', event => {
    const target = event.target as Node;
    if (!pop.hidden && !pop.contains(target) && !(current && current.contains(target))) hide();
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && !pop.hidden) { const back = current; hide(); back?.focus(); }
  });
  addEventListener('resize', hide);
}

export {};
