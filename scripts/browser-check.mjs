import assert from "node:assert/strict";
import fs from "node:fs";
import { chromium } from "playwright";
const base = process.env.SANGUO_URL || "http://127.0.0.1:4324";
fs.mkdirSync("work",{recursive:true});
const cards = JSON.parse(fs.readFileSync("src/data/cards.json", "utf8"));
const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width: 1440, height: 1000 },
  permissions: ["clipboard-read", "clipboard-write"],
});
const page = await context.newPage();
const errors = [];
page.on("pageerror", (e) => errors.push(String(e)));
try {
  const response = await page.goto(base, { waitUntil: "networkidle" });
  assert.equal(response.status(), 200, "Homepage must be served successfully");
  assert.equal(await page.locator("h1").count(), 1);
  const homeTitle = await page.title();
  assert.ok(homeTitle.includes("三国志"));
  await page.screenshot({ path: "work/home-desktop.png", fullPage: true });
  await page.goto(base + "/people/", { waitUntil: "networkidle" });
  const search = page.getByRole("searchbox");
  await search.fill("劉備");
  assert.equal(await page.locator("[data-search-card]:visible").count(), 1);
  assert.ok(
    (await page.locator("[data-search-card]:visible").innerText()).includes(
      "刘备",
    ),
  );
  await search.fill("玄德");
  assert.equal(await page.locator("[data-search-card]:visible").count(), 1);
  await search.fill("不存在的人");
  assert.equal(await page.locator("[data-search-card]:visible").count(), 0);
  assert.equal(await page.locator("[data-empty]").isVisible(), true);
  await search.fill("");
  await page.getByRole("button", { name: "孙吴", exact: true }).click();
  assert.equal(await page.locator("[data-search-card]:visible").count(), cards.people.filter(p=>p.faction==="孙吴").length);
  await page.getByRole("button", { name: "全部", exact: true }).click();
  assert.equal(await page.locator("[data-search-card]:visible").count(), cards.people.length);
  await page.goto(base + "/events/", { waitUntil: "networkidle" });
  assert.equal(await page.locator("[data-search-card]:visible").count(),18,"Key events are the default");
  assert.equal(await page.locator("[data-search-card]").count(),38,"Each event has exactly one DOM card");
  assert.equal(new Set(await page.locator("[data-search-card]").evaluateAll(els=>els.map(e=>e.dataset.eventId))).size,38);
  await page.getByRole("button",{name:"全部",exact:true}).click();
  assert.equal(await page.locator("[data-search-card]:visible").count(),38);
  await page.getByRole("searchbox").fill("街亭");
  assert.equal(await page.locator("[data-search-card]:visible").count(),1);
  assert.ok((await page.locator("[data-search-card]:visible").innerText()).includes("首次北伐"));
  await page.getByRole("searchbox").fill("孫權稱帝");
  assert.equal(await page.locator("[data-search-card]:visible").count(),1);
  await page.getByRole("searchbox").fill("");
  const years=await page.locator("[data-search-card]").evaluateAll(els=>els.map(e=>Number(e.dataset.year)));
  assert.deepEqual(years,[...years].sort((a,b)=>a-b));
  assert.equal(years[0],184); assert.equal(years.at(-1),280);
  const aligned = await page.locator('[data-year-group="200"] [data-search-card]').evaluateAll(els=>els.map(e=>e.getBoundingClientRect().top));
  assert.equal(aligned.length,2);
  assert.ok(Math.abs(aligned[0]-aligned[1])<=1,'Independent 200-year events align in the same row');
  assert.equal(await page.locator('[data-year-group="234"]').count(),1,'234 shares one year group');
  await page.getByRole("button",{name:"曹魏与晋",exact:true}).click();
  await page.locator(".timeline-type-filter summary").click();
  await page.getByRole("button",{name:"战争",exact:true}).click();
  assert.equal(await page.locator("[data-search-card]:visible").count(),cards.events.filter(e=>e.lanes.includes('wei')&&e.categories.includes('war')).length);
  assert.ok(page.url().includes('lane=wei')&&page.url().includes('category=war'));
  await page.reload({waitUntil:'networkidle'});
  assert.equal(await page.getByRole("button",{name:"曹魏与晋",exact:true}).getAttribute('aria-pressed'),'true');
  assert.equal(await page.getByRole("button",{name:"战争",exact:true}).getAttribute('aria-pressed'),'true');
  await page.getByRole("button",{name:"蜀汉",exact:true}).click();
  await page.goBack({waitUntil:'networkidle'});
  assert.equal(await page.getByRole("button",{name:"曹魏与晋",exact:true}).getAttribute('aria-pressed'),'true');
  await page.goForward({waitUntil:'networkidle'});
  assert.equal(await page.getByRole("button",{name:"蜀汉",exact:true}).getAttribute('aria-pressed'),'true');
  await page.getByRole("button",{name:"时间列表",exact:true}).click();
  assert.equal(await page.locator('.timeline').getAttribute('data-timeline-view'),'list');
  const filteredURL=page.url();
  await page.locator('[data-search-card]:visible').first().click();
  assert.ok(await page.locator('#event-relations').isVisible());
  assert.equal(await page.locator('[data-timeline-back]').getAttribute('href'),new URL(filteredURL).pathname+new URL(filteredURL).search);
  await page.locator('[data-timeline-back]').click();
  assert.equal(page.url(),filteredURL);
  await page.getByRole('searchbox').fill('不存在的事件');
  assert.equal(await page.locator('[data-empty]').isVisible(),true);
  assert.equal(await page.locator('[data-phase]:visible').count(),0);
  await page.locator('[data-empty-reset]').click();
  assert.equal(await page.locator('[data-search-card]:visible').count(),38);
  assert.equal(await page.locator('[data-year-group="264"] [data-track-lane="shu"]').innerText(),'蜀汉 · 已结束');
  assert.equal(await page.locator('[data-year-group="265"] [data-track-lane="wei"]').innerText(),'西晋');
  await page.screenshot({path:'work/timeline-desktop.png',fullPage:false});
  await page.locator('[data-year-group="220"]').evaluate(el=>el.scrollIntoView({block:'start',behavior:'instant'}));
  await page.screenshot({path:'work/timeline-three-lines.png',fullPage:false});
  await page.goto(base+'/events/jingzhou/',{waitUntil:'networkidle'});
  assert.ok(await page.locator('#event-relations a[href="/events/yiling/"]').isVisible(),'Jingzhou links semantically to Yiling');
  await page.goto(base+'/events/cao-fang-succession/',{waitUntil:'networkidle'});
  assert.ok(await page.locator('.participant-name').count()>0,'Unmade people are text, not empty links');
  const noJS = await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:900}});
  const plainPage=await noJS.newPage();
  await plainPage.goto(base+'/events/');
  assert.equal(await plainPage.locator('[data-search-card]:visible').count(),38);
  assert.equal(await plainPage.locator('.timeline-controls').isVisible(),false);
  await noJS.close();
  await page.goto(base + "/people/caocao/", { waitUntil: "networkidle" });
  await page.getByRole("button", { name: "复制链接", exact: true }).click();
  assert.equal(
    await page.evaluate(() => navigator.clipboard.readText()),
    base + "/people/caocao/",
  );
  await page.evaluate(() =>
    Object.defineProperty(navigator, "share", {
      configurable: true,
      value: undefined,
    }),
  );
  await page.getByRole("button", { name: "分享", exact: true }).click();
  assert.equal(
    await page.evaluate(() => navigator.clipboard.readText()),
    base + "/people/caocao/",
  );
  await page.evaluate(() => {
    window.__shared = null;
    Object.defineProperty(navigator, "share", {
      configurable: true,
      value: async (payload) => {
        window.__shared = payload;
      },
    });
  });
  await page.getByRole("button", { name: "分享", exact: true }).click();
  assert.equal(
    (await page.evaluate(() => window.__shared)).url,
    base + "/people/caocao/",
  );
  // The annotation target must remain visible when a reader has hidden notes.
  await page.goto(base + "/read/001/", { waitUntil: "networkidle" });
  await page.getByRole("button", { name: "显示裴注", exact: true }).click();
  assert.equal(await page.locator("#v001-b0002-n02").isVisible(), false);
  await page.evaluate(() => {
    location.hash = "v001-b0002-n02";
  });
  await page.waitForFunction(() =>
    document.querySelector("#v001-b0002-n02")?.checkVisibility(),
  );
  assert.equal(await page.locator("#v001-b0002-n02").isVisible(), true);
  // Audit every internal href and fragment, not just the sampled pages.
  const book = JSON.parse(fs.readFileSync("src/data/book.json", "utf8"));
  const paths = [
    "/",
    "/people/",
    "/events/",
    "/read/",
    "/about/",
    "/404/",
    ...cards.people.map((p) => `/people/${p.id}/`),
    ...cards.events.map((e) => `/events/${e.id}/`),
    ...book.volumes.map((v) => `/read/${v.id}/`),
  ];
  const documents = new Map();
  const internalLinks = [];
  for (const path of paths) {
    const res = await context.request.get(base + path);
    // 404.html is tested separately by the static preview server.
    if (path === "/404/") continue;
    assert.equal(res.status(), 200, `${path} response`);
    const html = await res.text();
    await page.setContent(html);
    const data = await page.evaluate(() => ({
      ids: Array.from(document.querySelectorAll("[id]")).map((e) => e.id),
      links: Array.from(document.querySelectorAll("a[href]")).map((e) =>
        e.getAttribute("href"),
      ),
    }));
    assert.equal(
      new Set(data.ids).size,
      data.ids.length,
      `${path} duplicate DOM ids`,
    );
    documents.set(path, new Set(data.ids));
    for (const href of data.links) {
      if (href.startsWith("/") || href.startsWith("#"))
        internalLinks.push({ path, href });
    }
  }
  for (const { path, href } of internalLinks) {
    const u = new URL(href, base + path);
    const target = documents.get(u.pathname);
    assert.ok(target, `${path}: unknown internal route ${href}`);
    if (u.hash)
      assert.ok(
        target.has(decodeURIComponent(u.hash.slice(1))),
        `${path}: missing anchor ${href}`,
      );
  }
  for (const width of [1440, 390, 320]) {
    await page.setViewportSize({ width, height: 900 });
    for (const path of [
      "/",
      "/people/",
      "/events/",
      "/people/caocao/",
      "/events/chibi/",
      "/events/wei-founding/",
      "/events/fall-wu/",
      "/people/sima-yi/",
      "/people/du-yu/",
      "/read/001/",
      "/read/appendix/",
    ]) {
      await page.goto(base + path, { waitUntil: "networkidle" });
      assert.ok(
        await page.evaluate(
          () => document.documentElement.scrollWidth <= innerWidth + 1,
        ),
        `${width}px overflow at ${path}`,
      );
    }
    await page.goto(base+'/events/?importance=all',{waitUntil:'networkidle'});
    await page.screenshot({path:`work/timeline-${width}.png`,fullPage:false});
    if (width === 390) {
      await page.locator('[data-year-group="220"]').evaluate(el=>el.scrollIntoView({block:'start',behavior:'instant'}));
      await page.screenshot({path:'work/timeline-mobile-detail.png',fullPage:false});
      await page.goto(base, { waitUntil: "networkidle" });
      await page.screenshot({ path: "work/home-mobile.png", fullPage: true });
      await page.goto(base + "/people/caocao/", { waitUntil: "networkidle" });
      await page.screenshot({ path: "work/person-mobile.png", fullPage: true });
    }
  }
  assert.deepEqual(errors, [], "Browser runtime errors");
  console.log(
    `Browser checks passed: ${documents.size} pages, ${internalLinks.length} links, parallel/list timeline, compound filters, URL/history restoration, event relations, text participants, no-JS fallback, search, share/copy, annotation targets, 1440/390/320px layouts.`,
  );
  fs.writeFileSync(
    "work/browser-report.json",
    JSON.stringify(
      {
        pages: documents.size,
        links: internalLinks.length,
        widths: [1440, 390, 320],
        runtimeErrors: errors,
        date: new Date().toISOString(),
      },
      null,
      2,
    ),
  );
} finally {
  await browser.close();
}
