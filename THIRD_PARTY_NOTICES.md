# 第三方软件与数据 · Third-Party Notices

本项目使用了下列第三方作品。它们遵循各自的许可，不受本项目 MIT 或 CC BY-SA 4.0 许可的约束。
This project uses the third-party works listed below. Each is governed by its own license, not by this project's MIT or CC BY-SA 4.0 terms.

## 1. 原文 · Source text

**《三国志》，陈寿撰，裴松之注 · *Sanguozhi* by Chen Shou, commentary by Pei Songzhi**

- 原著：公有领域。Original work: public domain.
- 电子文本：维基文库网络录入本，2026-09-23 下载，按 CC BY-SA 4.0 提供。Digital text: Chinese Wikisource transcription, downloaded 2026-09-23, available under CC BY-SA 4.0.
- 来源：<https://zh.wikisource.org/wiki/三國志>。各卷的固定修订链接保存在 `src/data/book.json`，网站每卷顶部也有来源链接。Per-fascicle pinned revision links are stored in `src/data/book.json` and shown at the top of each fascicle on the site.
- 这是网络录入本，未逐字校勘，不等同于任何出版社的点校本。This is a crowd-sourced transcription; it has not been collated character by character and is not equivalent to any published critical edition.

## 2. 随网站分发的软件 · Software shipped with the site

以下代码会被打包进构建产物 `dist/`，在读者的浏览器中运行。
The following code is bundled into `dist/` and runs in the reader's browser.

| 软件 · Software | 用途 · Purpose | 许可 · License |
|---|---|---|
| [opencc-js](https://github.com/nk2028/opencc-js) 1.4.2 | 繁体转简体 · Traditional → Simplified conversion | MIT AND Apache-2.0 |
| [OpenCC](https://github.com/BYVoid/OpenCC) 词典数据（经 opencc-js 引入）· dictionary data via opencc-js | 简繁转换词典 · conversion dictionaries | Apache-2.0 |
| [Astro](https://github.com/withastro/astro) 运行时片段 · runtime fragments | 静态站点生成 · static site generation | MIT |

许可全文随网站一起发布，见 `public/licenses/`：
Full license texts are published with the site in `public/licenses/`:

- `public/licenses/opencc-js-license.txt`
- `public/licenses/Apache-2.0.txt`
- `public/licenses/opencc-third-party.md`

## 3. 仅用于开发的工具 · Development-only tools

这些工具只在本地构建和测试时使用，不随网站分发。
Used only for local builds and tests; not shipped with the site.

| 软件 · Software | 许可 · License |
|---|---|
| [Astro](https://github.com/withastro/astro) 5.x | MIT |
| [@astrojs/check](https://github.com/withastro/language-tools) | MIT |
| [TypeScript](https://github.com/microsoft/TypeScript) | Apache-2.0 |
| [Playwright](https://github.com/microsoft/playwright) | Apache-2.0 |

完整的依赖树及版本见 `package-lock.json`。
See `package-lock.json` for the full dependency tree and versions.

## 4. 江山时序 · Jiangshan Atlas

人物页的行迹地图和事件页的战役推演来自 [江山时序 Jiangshan Atlas](https://github.com/DeanChensj/jiangshan-map)（© 2026 DeanChensj）。
The itinerary maps on person pages and the battle playback on event pages come from [Jiangshan Atlas](https://github.com/DeanChensj/jiangshan-map) (© 2026 DeanChensj).

**本项目怎样使用它 · How this project uses it**

- 本仓库**不包含**江山时序的任何代码或地图数据。网站通过 `<iframe>` 和普通链接打开一个单独运行的江山时序实例，地址由构建时的 `PUBLIC_ATLAS_BASE` 指定（见 [.env.example](.env.example)）。
- This repository contains **no** Jiangshan Atlas code or map data. The site opens a separately running Jiangshan Atlas instance through an `<iframe>` and ordinary links; its address is set with `PUBLIC_ATLAS_BASE` at build time (see [.env.example](.env.example)).
- 本仓库保存的是人物在江山时序路线上的站号（`atlasPerson`、`atlasStops`）和本站自己的核对记录（`docs/audits/`），属于本项目内容。
- What this repository does store is the stop indices of each person on Jiangshan Atlas routes (`atlasPerson`, `atlasStops`) and this project's own check records (`docs/audits/`); these are this project's content.
- 部分三国人物路线、战役推演和 `stop=a-b` 区间高亮是为本项目补充进江山时序的，目前维护在分支 [wolfzl/jiangshan-map](https://github.com/wolfzl/jiangshan-map) 中，部署在 <https://wolfzl.github.io/jiangshan-map/>。本站正式部署时使用这个分支（构建时设置 `PUBLIC_ATLAS_BASE`）；改用其他实例时，请确认它包含这些改动，否则对应地图会缺少路线。
- Some Three Kingdoms itineraries, the battle playback and `stop=a-b` range highlighting were added to Jiangshan Atlas for this project. They are maintained in the fork [wolfzl/jiangshan-map](https://github.com/wolfzl/jiangshan-map), deployed at <https://wolfzl.github.io/jiangshan-map/>. The public deployment uses this fork (set `PUBLIC_ATLAS_BASE` at build time); if you point it at another instance, make sure that instance includes these changes, or those maps will be missing routes.

**江山时序的许可与限制 · Its license and restrictions**

- 江山时序按 **GPL-3.0** 发布。部署或修改江山时序时，须遵守 GPL-3.0，包括公开相应源码。
- Jiangshan Atlas is released under **GPL-3.0**. If you deploy or modify it, comply with GPL-3.0, including making the corresponding source available.
- **例外**：江山时序中由 CHGIS V6 和 Hartwell China Historical GIS 派生的郡、州、府级边界数据仍受原始条款约束，**仅限学术、非商业使用**，不按 GPL-3.0 再授权。详见江山时序的 `data/atlas/README.md`。
- **Exception**: prefecture-level boundaries (郡 / 州 / 府) in Jiangshan Atlas derived from CHGIS V6 and the Hartwell China Historical GIS remain under their original terms, **academic and non-commercial use only**, and are not relicensed under GPL-3.0. See `data/atlas/README.md` in Jiangshan Atlas.
- 因此，带地图的部署应保持非商业用途；如需商业使用，请先移除地图嵌入，或自行确认上游数据的授权。
- Deployments that include the maps should therefore stay non-commercial. For commercial use, remove the map embeds or obtain the upstream data permissions yourself.
- 江山时序的历史疆域与政区边界是示意性近似，不能当作精确边界引用。
- Historical borders in Jiangshan Atlas are schematic approximations and should not be cited as precise boundaries.

**署名 · Attribution**

江山时序要求再利用其地图、截图或数据时署名“江山时序 Jiangshan Atlas”并链接 <https://github.com/DeanChensj/jiangshan-map>，同时注明其上游来源：谭其骧主编《中国历史地图集》、CHGIS（哈佛燕京学社与复旦大学）、Robert M. Hartwell 历史 GIS 数据、[aourednik/historical-basemaps](https://github.com/aourednik/historical-basemaps)（GPL-3.0），以及 DataV GeoAtlas 现代行政区划数据。

Jiangshan Atlas asks that reuse of its maps, screenshots or data credit “江山时序 Jiangshan Atlas” with a link to <https://github.com/DeanChensj/jiangshan-map>, and cite its upstream sources: Tan Qixiang's *The Historical Atlas of China*, CHGIS (Harvard-Yenching Institute and Fudan University), Robert M. Hartwell's historical GIS datasets, [aourednik/historical-basemaps](https://github.com/aourednik/historical-basemaps) (GPL-3.0), and DataV GeoAtlas modern administrative boundaries.

本项目截图（`docs/images/`）中出现的地图画面同样适用上述署名要求。
The same attribution applies to any map imagery in this project's screenshots (`docs/images/`).
