# 内容许可 · Content License

本项目的文本内容按 **知识共享 署名-相同方式共享 4.0 国际许可协议（CC BY-SA 4.0）** 提供。
The text content of this project is licensed under the **Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)**.

许可全文 / Full legal text: <https://creativecommons.org/licenses/by-sa/4.0/legalcode>

## 为什么是 CC BY-SA 4.0 · Why CC BY-SA 4.0

《三国志》由陈寿撰、裴松之注，原著属于公有领域。本项目使用的电子文本来自维基文库网络录入本，维基文库按 CC BY-SA 4.0 提供这些文字。本项目的人物卡、事件卡和白话译文都是在这份文本基础上整理、引用和翻译而成的演绎作品，因此按同一许可提供。

The original *Sanguozhi* by Chen Shou, with Pei Songzhi's commentary, is in the public domain. The digital text used here is the Chinese Wikisource transcription, which Wikisource provides under CC BY-SA 4.0. The people and event cards and the vernacular translations are adaptations built on that text, so they are released under the same license.

## 适用范围 · Scope

以下文件属于“内容”，按 CC BY-SA 4.0 提供：
The following files are content and are licensed under CC BY-SA 4.0:

| 路径 · Path | 说明 · Description |
|---|---|
| `src/data/book.json` | 原文（正文与裴注）及来源修订信息 · source text with revision metadata |
| `src/data/cards.json` | 人物与事件卡片（由内容种子生成）· generated people and event cards |
| `src/data/translations/` | AI 辅助白话试译 · AI-assisted vernacular translations |
| `src/data/volume-titles.json` | 卷目显示名 · display titles of fascicles |
| `scripts/create_cards.py` | 首版人物与事件卡片种子 · seed text for the first cards |
| `scripts/event_content.py`, `scripts/person_content.py`, `scripts/lords_content.py` | 人物、事件与关系的内容种子 · content seeds |
| `scripts/profile_v3_*.py`, `scripts/profile_caocao_content.py`, `scripts/profiles_*_expanded.py`, `scripts/zhangfei_profile.py` | 人物档案种子 · person dossier seeds |
| `scripts/portraits_*.py`, `scripts/portrait_events_*.py`, `scripts/dossiers_*.py` | 人物小传、补充事件与档案种子 · portrait, event and dossier seeds |
| `docs/` | 文档、史料核对记录、行迹审计数据与截图 · documentation, review records, audit data and screenshots |
| `README*.md`, `CONTRIBUTING.md` | 说明文档 · project documentation |

上述种子文件中的程序结构只是用来承载文字，整份文件按 CC BY-SA 4.0 提供。其余文件（`src/` 下的页面、组件、样式与逻辑，`scripts/` 下的其他脚本，`tests/` 与配置文件）属于代码，按 [MIT 许可](LICENSE) 提供。

The program structure in the seed files above exists to hold the text, so each of those files as a whole is under CC BY-SA 4.0. All other files (pages, components, styles and logic in `src/`, the remaining scripts in `scripts/`, `tests/` and configuration files) are code and are licensed under the [MIT License](LICENSE).

`public/licenses/` 中的文件是第三方许可文本，遵循各自的许可，见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
Files in `public/licenses/` are third-party license texts and follow their own terms; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## 再利用时请这样署名 · How to attribute

转载、改编或再发布本项目的内容时，请：

1. 注明来源，例如：“三国志 · 人物与事件，原文据维基文库《三国志》”，并附本项目链接；
2. 附上许可链接 <https://creativecommons.org/licenses/by-sa/4.0/>；
3. 说明你做了哪些修改；
4. 演绎作品以 CC BY-SA 4.0 或兼容许可发布。

When you reuse, adapt or redistribute the content:

1. Credit the source, e.g. “Sanguozhi · People and Events, source text from the Chinese Wikisource *Sanguozhi*”, with a link to this project;
2. Link to the license: <https://creativecommons.org/licenses/by-sa/4.0/>;
3. Indicate what you changed;
4. Release adaptations under CC BY-SA 4.0 or a compatible license.

维基文库各卷的贡献者署名与修订历史可从站内每卷的来源链接（固定修订号）查到。
Contributor credits and revision history for each Wikisource page are available from the per-fascicle source links (pinned revisions) on the site.

## 关于白话译文 · About the translations

白话译文由 AI 辅助生成，尚未经过逐句人工审阅，可能有误译。引用或研究时请以原文为准。
The vernacular translations were produced with AI assistance and have not been reviewed sentence by sentence; they may contain errors. Rely on the original text for citation or research.
