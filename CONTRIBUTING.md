# 参与贡献

感谢你愿意改进这个项目。English summary at the end. 日本語の要約は末尾にあります。

## 可以帮忙的事

- **报告问题**：史料错误、引文对不上、错别字、人名误链、年份换算错误、页面显示问题。提 Issue 时请附页面地址，涉及史料的请写明卷号和原文句子。不方便使用 GitHub 的话，也可以发邮件到 wolfzhang008@gmail.com。
- **校对白话译文**：译文是 AI 辅助的试译，最需要懂文言的读者逐段核对。
- **补充人物与事件**：请先读 [docs/guides/person-template-v3.md](docs/guides/person-template-v3.md)，再开 Issue 说明要补充的人物或事件，避免重复劳动。
- **改进代码**：页面、交互、无障碍、性能。

## 内容规则

这几条是本项目最重要的约定，审查时会逐条核对。

1. **只用《三国志》正文与裴注。** 不用《三国演义》、影视剧或游戏情节补写史料。生卒年确需引用其他史书（如《晋书》）时，单独注明书名和出处。
2. **每条叙述都要有引用。** 每处 `refs` 必须包含 `volume`、`blockId`、`kind`、`quote`，`quote` 必须是该原文块中**一字不差**的子串。引用裴注时 `kind` 用 `peizhu`，并填写 `sourceBook`（裴注所引的书名）。
3. **区分记载与解读。** 原文明确写到的写成叙述；推断、评价放在“阅读解读”“史料辨析”等明确标注的位置。
4. **保留分歧。** 不同篇章、正文与裴注说法不一时并列呈现，不替读者裁决。
5. **年份写清依据。** 由享年推算、有异说或史书未载的年份要注明，不能拿活动年代代替生卒年。
6. **不改原文。** `src/data/book.json` 是来源文本，不做文字校订；发现录入错误请提 Issue。

## 修改流程

1. 人物和事件的内容在 `scripts/` 下的种子文件里，`src/data/cards.json` 是生成结果，**不要直接改 JSON**。
2. 改完种子后运行：

   ```bash
   python3 scripts/create_cards.py   # 重新生成 cards.json
   npm run build                     # 校验引用与关联，再构建
   npm test
   ```

3. 改动页面或交互时，再启动预览运行浏览器检查（需要 `npx playwright install chromium`）：

   ```bash
   npm run preview -- --port 4324
   SANGUO_URL=http://127.0.0.1:4324 npm run test:browser
   ```

4. 提交 Pull Request 时说明改了什么、依据哪几卷，并贴上测试结果。

更详细的数据结构与脚本说明见 [docs/development.md](docs/development.md)。

## 许可

提交到本项目的代码按 [MIT](LICENSE) 授权；提交的文本内容（卡片、译文、文档、内容种子）按 [CC BY-SA 4.0](LICENSE-CONTENT.md) 授权。提交即表示你同意以上述许可提供你的贡献。

---

## English summary

Bug reports, source corrections, translation proofreading and new people or events are all welcome. The rules that matter most:

- Use only the *Sanguozhi* main text and Pei Songzhi's commentary; never fill in from *Romance of the Three Kingdoms* or film and TV.
- Every statement needs a citation whose `quote` is an exact substring of the referenced source block.
- Keep what the text says separate from interpretation, and keep conflicting accounts side by side.
- Edit the seed files in `scripts/`, not the generated `src/data/cards.json`; then run `python3 scripts/create_cards.py`, `npm run build` and `npm test`.

Code contributions are licensed under [MIT](LICENSE); text contributions under [CC BY-SA 4.0](LICENSE-CONTENT.md).

## 日本語の要約

不具合の報告、史料の訂正、現代語訳の校閲、人物や出来事の追加を歓迎します。重要な決まりは次のとおりです。

- 『三国志』本文と裴注だけを使い、『三国志演義』や映像作品で補わないこと。
- すべての記述に引用を付け、`quote` は参照する原文ブロックの文字列と完全に一致させること。
- 原文の記述と解釈を分け、異なる記述は並べて示すこと。
- 生成された `src/data/cards.json` ではなく `scripts/` の元データを編集し、`python3 scripts/create_cards.py`、`npm run build`、`npm test` を実行すること。

コードの貢献は [MIT](LICENSE)、テキストの貢献は [CC BY-SA 4.0](LICENSE-CONTENT.md) で提供されます。
