# 开发指南

本文说明本地开发、内容生成、校验与测试的完整流程。项目概览见 [README](../README.md)，贡献规则见 [CONTRIBUTING](../CONTRIBUTING.md)。

## 环境

- Node.js 22.12 或更新版本（开发时使用 25.6.0，Astro 5.18）。
- Python 3.10 或更新版本：内容种子生成、原文提取和 Python 测试需要。只用到标准库。
- 浏览器检查使用 Playwright Chromium，新环境先执行 `npx playwright install chromium`。

```bash
npm ci
npm run dev                       # 开发预览 http://127.0.0.1:4321/
npm run build                     # validate → astro check → astro build，输出 dist/
npm run preview -- --port 4324    # 预览构建结果
```

可选的环境变量见 [.env.example](../.env.example)。

## 数据流

```text
原始 EPUB ──extract_epub.py──▶ src/data/book.json          （原文、段落与注文标识）
内容种子 scripts/*.py ──create_cards.py──▶ src/data/cards.json   （人物、事件、关系）
白话译文 ─────────────────────▶ src/data/translations/*.json （按卷，块 id 与原文一致）
                                         │
                         validate-content.mjs 校验 ──▶ Astro 构建 ──▶ dist/
```

### 原文：`src/data/book.json`

66 个阅读单元（65 卷 +《上三国志注表》），每个段落块和裴注都有固定标识（如 `v001-b0003`、`v001-b0003-n02`），另含 EPUB 的 SHA-256、各卷维基文库来源与修订号。标识一旦发布就不再改动，所有引用都依赖它们。

重新提取原文（原始 EPUB 不随仓库分发）：

```bash
# 把 EPUB 放到 work/ 下，或用 SANGUO_EPUB 指定路径
npm run extract
python3 scripts/extract_epub.py /path/to/book.epub --output work/new-book.json
```

更换来源版本时，先输出到 `work/` 与旧数据比对，保留旧版标识，不要直接覆盖已有引用。`tests/translations.test.mjs` 会用 `book.json` 的哈希校验译文，改动 `book.json` 会让译文校验失败。

卷目在页面上显示的名称来自 `src/data/volume-titles.json`，与 `book.json` 中的原始标题分开维护。

### 人物与事件：`src/data/cards.json`

`cards.json` 由 `python3 scripts/create_cards.py` 生成，**不要手改**。生成器依次合并以下种子：

| 种子 | 内容 |
|---|---|
| `scripts/create_cards.py` | 首版人物与事件卡片 |
| `scripts/event_content.py` | 事件元数据、事件正文与事件关系 |
| `scripts/person_content.py` | 第二版新增人物与更新 |
| `scripts/lords_content.py` | 汉末诸侯人物、事件与诸侯线 |
| `scripts/portraits_*.py`、`scripts/portrait_events_*.py` | 人物小传、生卒依据、纪年经历、补充事件 |
| `scripts/dossiers_*.py`、`scripts/profiles_*_expanded.py`、`scripts/profile_caocao_content.py`、`scripts/zhangfei_profile.py` | 人物档案扩展 |
| `scripts/profile_v3_*.py`（经 `scripts/profile_v3.py` 适配） | v3 人物档案，每人一个文件 |

人物档案的写法、分级（A/B/C）和字段说明见 [guides/person-template-v3.md](guides/person-template-v3.md)；行迹地图的数据规则见 [guides/atlas-trajectory-guide.md](guides/atlas-trajectory-guide.md)。

修改种子后：

```bash
python3 scripts/create_cards.py
npm run build
```

### 引用格式

每处 `refs` 包含：

- `volume`：卷号；
- `blockId`：原文块或注文标识；
- `kind`：`body`（陈寿正文）或 `peizhu`（裴注）；
- `quote`：该块中一字不差的子串；
- `sourceBook`：仅裴注需要，填写裴注所引书名。

人物与事件的关联必须双向一致。事件关系用唯一 ID 与 `from`、`to`、`type`、`summary`、`interpretation`、`refs` 表示，`parallel` 类型只记一条，在双方页面都展示。

### 校验

`npm run validate`（构建时自动执行）检查：

- 每条 `quote` 都能在对应原文块中找到；
- 人物与事件双向关联、事件关系端点存在；
- 数量与时间范围符合 `src/data/edition.json`；
- 人物正文中的事件链接文字存在且顺序正确；
- v3 档案与行迹时期的结构规则。

增补人物或事件时，同步更新 `src/data/edition.json` 中的数量。

### 白话译文：`src/data/translations/`

每卷一个 JSON，块 id 与原文一致，覆盖正文、裴注和篇末评语。译文为 AI 辅助试译，翻译进度和疑难处记录在 [reviews/wei-translation-progress.md](reviews/wei-translation-progress.md) 与 [reviews/shu-wu-translation-progress.md](reviews/shu-wu-translation-progress.md)。

## 页面与前端逻辑

| 位置 | 作用 |
|---|---|
| `src/pages/` | 首页、人物、事件、原文阅读、关于、404 |
| `src/components/PersonDossier.astro` | 人物档案页（折叠分组、行迹地图、引用） |
| `src/components/Timeline.astro`、`src/lib/timeline.mjs` | 四线事件时间线与筛选状态 |
| `src/lib/reader-script.ts` | 阅读器：简繁切换、裴注开关、白话与逐段对照 |
| `src/lib/person-links.ts` | 原文中已建档人名的链接 |
| `src/lib/citation-popover.ts` | 引用编号的浮层 |
| `src/lib/dossier-ui.ts` | 人物页吸顶目录与回到顶部 |
| `src/lib/atlas.mjs` | 生成江山时序地图链接 |

简体由 OpenCC 从繁体底本转换，只改变阅读区文字；切回繁体时直接恢复原字形。JavaScript 不可用时显示繁体底本，所有内容仍可阅读，折叠区使用原生 `<details>`。

## 测试

```bash
npm test               # Python 单元测试 + Node 单元测试
npm run validate       # 只跑内容校验
```

浏览器检查需要先启动预览（默认地址 `http://127.0.0.1:4324`，可用 `SANGUO_URL` 修改）：

```bash
npm run preview -- --port 4324
npm run test:browser     # 全站链接与页面结构
npm run test:reader      # 66 个阅读单元的简繁切换与锚点
npm run test:portraits   # 人物小传与事件链接
npm run test:dossier     # 单个档案页（张飞）多宽度检查
npm run test:dossiers    # 全部档案页
npm run test:baihua      # 白话阅读
```

全书比对测试（`tests/test_book_integrity.py`）需要原始 EPUB；找不到时自动跳过。

> 已知问题：`npm run test:baihua` 目前会失败，一是脚本仍假设卷 31 没有译文（现已全卷覆盖），二是卷 8 等少数卷的独立注文块与其注文共用 id。两者都早于当前版本，尚待修复。

## 本地预览脚本

`scripts/site.sh` 是一个可选的后台预览启停脚本（`start` / `status` / `restart` / `stop`），固定使用 4324 端口，日志写在 `work/site-control/`。把它复制到仓库的上一级目录即可使用；`npm run test:control` 会实际启停一次进行检查。

## 部署

`npm run build` 生成的 `dist/` 是纯静态文件，可以放到任意静态托管服务的站点根目录。页面链接都以 `/` 开头，部署在子路径下需要额外配置 Astro 的 `base`。

构建时：

- 设置 `SANGUO_SITE` 为正式网址，生成正确的分享链接与图片地址；
- 设置 `PUBLIC_ATLAS_BASE` 为已部署的江山时序地址，否则地图为空白。江山时序的许可要求见 [THIRD_PARTY_NOTICES](../THIRD_PARTY_NOTICES.md)。
