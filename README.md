# 三国志 · 人物与事件

基于《三国志·陈寿撰裴松之注》的手机友好静态网站。第二版提供 34 位人物、38 个事件（其中 18 个关键事件）、65 卷全文与《上三国志注表》。卡片以简体写成，原文保留繁体，引用区分陈寿正文与裴注。

项目位于 `/Users/zhangliang/ai/readbook/tmp/sanguozhi-timeline`，是 `.sanguozhi-repo` 的独立 Git worktree，开发分支为 `feat/sanguozhi-timeline-v2`。原始 EPUB 与原有阅读资料保持不变。

## 打开网站

本次交付的预览地址：**http://127.0.0.1:4323/**。

预览服务关闭后，在终端执行：

```bash
cd /Users/zhangliang/ai/readbook/tmp/sanguozhi-timeline
npm run preview -- --port 4323
```

再在浏览器打开上面的地址。源码和 `dist/` 均已生成。静态页面需要通过 HTTP 服务访问；目录、脚本及资源采用站点根路径。

在新环境恢复依赖或修改内容后，使用 Node.js 22.12 或更新版本：

```bash
npm ci
npm run build
npm run preview -- --port 4323
```

本次验证环境：Node.js 25.6.0，Astro 5.18.2。开发预览使用 `npm run dev`，默认地址为 http://127.0.0.1:4321/。

## 网站内容与行为

- 首页、人物列表、事件列表、人物详情、事件详情、全书目录、原文阅读、版本说明及 404 页面。
- 人物支持简繁姓名、字号、常见称谓搜索和主要历史势力筛选，覆盖汉末、魏、蜀、吴、晋。
- 184—280 年事件线默认显示 18 个关键事件，可切换全部 38 个事件。桌面支持三线并行/时间列表，手机使用单列时间汇总。
- 阅读范围、势力、事件类型与搜索组合筛选；URL 保存状态，刷新、历史返回、详情页“返回事件线”均可恢复。选一方时展开为单条线。
- 曹氏势力→曹魏→西晋、刘备势力→蜀汉、孙氏势力→孙吴按年代改变名称；蜀汉在 263 年结束。共享事件只有一张卡和一个页面。
- 事件页提供背景与后果、同一历史进程、并行对照、政权承继关联，附解释和引用。解读明确标注，时间相邻导航单独保留。
- 未设人物卡的参与者仅显示姓名，不生成失效页面。
- 每个关键生平节点、关系和事件段落附原文依据。点击引用编号展开节选，再进入精确的原文块。
- 原文可切换卷目、翻页及显示/隐藏裴注；从引用链接进入注文时自动显示相应裴注。
- 分享优先使用浏览器系统分享；不支持或分享失败时复制链接。用户取消分享时静默返回。
- 复制链接优先使用 Clipboard API，不可用时尝试兼容复制；两种方式都失败时提示从地址栏复制。

本地网址只在运行服务的电脑上可用。当前交付本地预览，不包含公开部署、账号、数据库、AI 对话、地图或海报导出。

## 内容结构与增补方法

- `src/data/book.json`：66 个原文章节、固定段落与注文标识、EPUB 哈希、各页来源和修订号。
- `src/data/cards.json`：人物与事件卡片。可直接编辑；已有卡片 ID 不应因改中文标题而改变。
- `src/lib/catalog.ts`：人物、事件、出处的 TypeScript 类型和页面查询。
- `scripts/extract_epub.py`：Python 标准库 EPUB 提取器。
- `scripts/create_cards.py`：保留原始卡片种子，再调用 `event_content.py` / `person_content.py` 扩充，统一生成卡片、关系与人物事件双向链接。重新运行会覆盖 `cards.json`；请编辑对应种子文件。
- `scripts/event_content.py`：30 张新增事件、38 个事件元数据及事件关系的编辑种子。
- `scripts/person_content.py`：22 张新增人物及原人物更新的编辑种子。
- `src/data/edition.json`：本期数量、关键事件数和时间范围；增补范围时同步更新。
- `src/lib/timeline.mjs`：筛选状态、时间线名称与位置的纯函数。
- `docs/event-v2-review.md` / `docs/person-v2-review.md`：新增内容的史料核对记录。
- `docs/validation-v2.md`：第二版验证记录。
- `docs/content-review.md`：首版史料核对记录。
- `docs/validation.md`：首版验收记录；新版结果见 `docs/validation-v2.md`。

新增人物至少填写稳定 ID、姓名、字号、势力标签、简介、生平段落、3—5 个节点、关系、阅读卷目和事件关联。生平正文目标 300—500 字。新增事件填写稳定 ID、标题、显示时间、起止年份、同年排序、阶段、参与势力、重要程度、事件类型、关联人物及四个事件段落，正文目标 400—700 字。

每处 `refs` 必须包含 `volume`、`blockId`、`kind`、`quote`；`quote` 是当前原文块中的精确子串。引用裴注时 `kind` 使用 `peizhu`，`blockId` 指向注文，另填写 `sourceBook`。人物与事件关联需双向一致。校验器从 `edition.json` 读取预期数量，并检查时间范围、势力终点、关系端点与每个事件的关联覆盖。关系用唯一 ID 和 from/to/type/summary/interpretation/refs 表达，parallel 只记录一条，在双方页面展示。

修改种子后先执行 `python3 scripts/create_cards.py`，再执行 `npm run build`；构建会先校验引用与关联。改变来源版本时，保留旧版标识与资料，不能直接覆盖旧引用。

重提取原书：

```bash
npm run extract
# 也可指定新的 EPUB 路径；输出前应先备份旧数据和核对引用。
python3 scripts/extract_epub.py /absolute/path/book.epub --output work/new-book.json
```

## 验证

```bash
npm test
npm run validate
npm run build
# 另一个终端先运行 npm run preview -- --port 4323
npm run test:browser
```

完整浏览器检查使用 Playwright Chromium；在新环境缺少浏览器时先执行 `npx playwright install chromium`。可用 `SANGUO_URL=http://127.0.0.1:其他端口 npm run test:browser` 更换地址。

全书比对测试读取原始 EPUB；原件不在指定路径时会明确跳过这两项测试，其他测试仍可运行。原件未复制进网站仓库。浏览器截图与临时报告在被 Git 忽略的 `work/` 内。

## 静态部署与许可

部署时上传 `dist/` 的全部内容，并以它作为站点根目录。真实域名确定后，构建时设置站点地址，以生成绝对的分享图片与页面链接：

```bash
SANGUO_SITE=https://your-domain.example npm run build
```

`public/share-card.png` 为通用分享预览图。公网平台是否展示预览取决于它的抓取规则，应在公开部署后验证。

原著属于公有领域；使用的维基文库网络文本及本站卡片整理按来源声明沿用 CC BY-SA 4.0。各卷提供固定修订链接，贡献者署名与修订历史可从原页面查阅。再利用时注明来源、许可及修改，并按同一许可分享演绎内容。

OpenCC 浏览器模块的许可及第三方声明保留在 `public/licenses/`，随静态构建一并交付。第三方软件遵循各自许可。
