import {Converter} from 'opencc-js/t2cn';
const root = document.querySelector<HTMLElement>('[data-expanded-sources]');
if (root) {
  const simplify = Converter({from:'t',to:'cn'});
  const input = root.querySelector<HTMLInputElement>('[data-source-query]')!;
  const count = root.querySelector<HTMLElement>('[data-source-count]')!;
  const rows = [...root.querySelectorAll<HTMLDetailsElement>('.source-item')];
  const normalize = (s: string) => simplify(s).toLocaleLowerCase().replace(/\s+/g,'');
  const texts = rows.map(row=>normalize(`${row.dataset.blockId} ${row.textContent}`));
  function filter() {
    const query = normalize(input.value);
    rows.forEach((row,i)=>row.hidden=Boolean(query&&!texts[i].includes(query)));
    count.textContent = `显示 ${rows.filter(row=>!row.hidden).length} / ${rows.length} 条依据`;
  }
  function reveal(hash: string, focus=false) {
    if (!/^#source-\d+$/.test(hash)) return;
    const target = document.getElementById(hash.slice(1)) as HTMLDetailsElement | null;
    if (!target || !root!.contains(target)) return;
    if (target.hidden) { input.value=''; filter(); }
    target.open = true;
    if (focus) target.querySelector('summary')?.focus({preventScroll:true});
    requestAnimationFrame(()=>target.scrollIntoView({block:'start'}));
  }
  input.addEventListener('input',filter);
  window.addEventListener('hashchange',()=>reveal(location.hash,true));
  document.addEventListener('click',event=>{
    const anchor=(event.target as Element).closest<HTMLAnchorElement>('a[href^="#source-"]');
    if (anchor) reveal(anchor.hash,true);
  });
  filter();
  reveal(location.hash);
}
