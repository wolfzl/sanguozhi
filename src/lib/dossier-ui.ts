// 人物页渐进增强：目录高亮、手机章节条跟随、回到顶部、手机端收起小档案。
// 没有 JS 时，目录与章节条仍是普通锚点链接，档案默认展开。
const links = [...document.querySelectorAll<HTMLAnchorElement>('[data-spy]')];
const ids = [...new Set(links.map(a => a.dataset.spy!))];
const sections = ids.map(id => document.getElementById(id)).filter((el): el is HTMLElement => !!el);
const jump = document.querySelector<HTMLElement>('[data-dossier-jump]');
const toc = document.querySelector<HTMLElement>('[data-dossier-toc]');
const toTop = document.querySelector<HTMLAnchorElement>('[data-to-top]');
const facts = document.querySelector<HTMLDetailsElement>('[data-profile-facts]');
const mobile = matchMedia('(max-width: 800px)');

// 手机上先看人物介绍，档案收起成一行，需要时再点开。
if (facts && mobile.matches) facts.open = false;

let active = '';
function setActive(id: string) {
  if (id === active) return;
  active = id;
  for (const a of links) {
    if (a.dataset.spy === id) a.setAttribute('aria-current', 'location');
    else a.removeAttribute('aria-current');
  }
  // 只横向移动章节条，不能用 scrollIntoView，否则会带动整页滚动。
  const chip = jump?.querySelector<HTMLElement>(`[data-spy="${id}"]`);
  if (jump && chip && getComputedStyle(jump).display !== 'none') {
    jump.scrollTo({ left: chip.offsetLeft - (jump.clientWidth - chip.offsetWidth) / 2, behavior: 'smooth' });
  }
  const entry = toc?.querySelector<HTMLElement>(`[data-spy="${id}"]`);
  if (toc && entry && toc.scrollHeight > toc.clientHeight) {
    if (entry.offsetTop < toc.scrollTop || entry.offsetTop + entry.offsetHeight > toc.scrollTop + toc.clientHeight) toc.scrollTop = entry.offsetTop - toc.clientHeight / 2;
  }
}

let ticking = false;
function update() {
  ticking = false;
  if (toTop) toTop.classList.toggle('is-visible', scrollY > 700);
  // 取页面上方 30% 处已经进入的最后一个章节。
  const line = innerHeight * 0.3;
  let current = sections[0]?.id ?? '';
  for (const section of sections) if (section.getBoundingClientRect().top <= line) current = section.id;
  if (current) setActive(current);
}
addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
addEventListener('resize', update);
update();

toTop?.addEventListener('click', event => {
  event.preventDefault();
  scrollTo({ top: 0, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' });
});

export {};
