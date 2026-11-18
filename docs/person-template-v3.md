# 人物卡 v3 改造指南

本文是给执行者（Claude Sonnet 5.5、Codex 或人工）的操作规范。照本文即可把一位人物改造成 v3 人物卡，并通过自动校验。

- 状态：规范已确认（2026-11-13）。三个级别各有一个已完成的样例（详见 §14）：

  | 级别 | 样例 | 种子文件 | 页面 |
  |---|---|---|---|
  | A | 刘备 | [profile_v3_liubei.py](../scripts/profile_v3_liubei.py) | `/people/liubei/` |
  | B | 关羽 | [profile_v3_guanyu.py](../scripts/profile_v3_guanyu.py) | `/people/guanyu/` |
  | C | 张角 | [profile_v3_zhang_jiao.py](../scripts/profile_v3_zhang_jiao.py) | `/people/zhang-jiao/` |

- 写新人物前，先通读**同级别**的样例；结构、措辞和引文粒度都以它为准。
- 生平履历的行迹地点（`careers[].place`）另见 [atlas-trajectory-guide.md](atlas-trajectory-guide.md)，样例是刘备。

---

## 0. 执行者须知（先读）

1. **一次只改一个人物。** 只新增 `scripts/profile_v3_<id>.py`（id 中的 `-` 换成 `_`，例如 `zhang-jiao` → `profile_v3_zhang_jiao.py`），并在 [scripts/profile_v3.py](../scripts/profile_v3.py) 的 `V3_MODULES` 里加一行。然后运行生成脚本，更新 `src/data/cards.json`。
2. **不要改**：`src/components/`、`src/lib/`、其他人物的种子文件、`create_cards.py`、事件数据。确实需要改时，先停下来汇报原因。例外有两个：新建人物通过种子的 `eventRoles` 登记事件参与者，并把 `edition.json` 的人数加 1（见 §7.1）；迁移 A 级旧人物：要从 `profiles_*_expanded.py` 中删去该人物的旧数据（见 §14.1）。华佗的事件导航特例见 §7.1。
3. **不要提交 git，不要执行 `npm run build`。** `npm run build` 会覆盖 `dist/`，影响本地 4324 端口正在运行的站点。构建检查一律输出到临时目录（见 §8）。
4. **所有事实必须来自 `src/data/book.json`。** 你对三国的既有知识只能当作检索线索；《三国演义》、《晋书》、现代研究等本地书里没有的内容不得写入。
5. 正文用简体中文；引文 `quote` 必须照抄 book.json 里的**繁体原文**，逐字一致。
6. 遇到下列情况就停下，在汇报中说明，不要自行猜测：材料矛盾无法判断，必填栏目找不到原文，或者需要改渲染代码。

## 1. 背景

65 张人物卡原本分属三套结构：张飞版 dossier（58 人）、曹操版 expanded、六人版 expanded（刘备、诸葛亮、孙权、周瑜、陆逊、司马懿）。v3 把它们统一成**一套种子格式**，再按人物分级决定各栏目的必填项和篇幅。

渲染层还没有迁移（见 §11）。因此 v3 种子由适配器 `profile_v3.py` 转成现有页面能渲染的字段，页面会按 expanded 样式显示。

## 2. 硬性规则

| # | 规则 | 由谁检查 |
|---|---|---|
| R1 | 引文一律写成 `Q(id, quote[, work])` 的逐句形式；`quote` 是能直接支撑该句说法的最短原文，不超过 120 字。禁止只给段落 ID 引整段。 | 适配器 + `validateV3Profiles` |
| R2 | 引用裴注（ID 含 `-n`）时，必须给出注引书名 `work`，如 `'《蜀记》'`；含裴松之按语时写 `'《蜀记》；裴松之案'`。 | 适配器 + `validateReferences` |
| R3 | 基本档案每一项都要有自己的 refs。 | `validateV3Profiles` |
| R4 | 栏目条数和篇幅符合分级要求（§4）。 | `validateV3Profiles` |
| R5 | “失误、挫折与争议”各级必填。没有材料时写针对本人的说明，不得使用通用兜底句。 | `validateV3Profiles` |
| R6 | 年表每行要有唯一的 `id`。得失记录的 `careerRef` 必须指向已存在的年表 id。 | `validateV3Profiles` |
| R7 | 年表、记录、导语里出现的 `eventIds` / `eventLinks`，对应事件的 participants 中必须包含本人，且年份要吻合。 | `validatePersonEventLinks` |
| R8 | 不得内嵌附录原文。原文阅读交给阅读器（`reading` 字段）。 | `validateV3Profiles` |
| R9 | 正文和裴注分层写明，例如“裴注引《典略》另记……”；异说放进 `readingNotes`，不写成定论。 | 人工审查 |
| R10 | 不编造。年份不详写“确年未载”，字号或生卒不详写“本书未详”，没有独立本传的人物要在 `sourceScope` 中写明。 | 人工审查 |

## 3. 文件与流水线

```text
scripts/create_cards.py           生成入口：python3 scripts/create_cards.py
  └─ expanded_profiles.apply()    处理尚未迁移的曹操、诸葛亮、孙权、周瑜、陆逊、司马懿，以及所有 v3 人物
       └─ profile_v3.py           v3 适配器：load() / to_expanded() / finish()
            └─ profile_v3_<id>.py 每人一个种子文件，定义 PROFILE
scripts/content-validation.mjs    校验规则；v3 规则在 validateV3Profiles
scripts/validate-content.mjs      全量校验入口：node scripts/validate-content.mjs
scripts/source_lookup.py          取证工具（§6）
scripts/person_tiers.py           分级统计（§4）
scripts/migrate_expanded_to_v3.py A 级旧人物迁移草稿工具（§14.1）
tests/person-template-v3.test.mjs v3 规则测试（以关羽为基准）
scripts/profile_v3_liubei.py      A 级样例；profile_v3_guanyu.py 为 B 级样例；profile_v3_zhang_jiao.py 为 C 级样例
```

人物 id 以 `src/data/cards.json` 中的 `people[].id` 为准，例如 `zhangfei`、`zhang-liao`、`zhuge-liang`，不要自己拼写。

## 4. 分级与篇幅

篇幅与栏目数量按 `V3_LIMITS`（[content-validation.mjs](../scripts/content-validation.mjs)）校验；站点通用校验另要求每张卡都有代表事迹。

| 项目 | A 完整 | B 标准 | C 简版 |
|---|---|---|---|
| 必填 facts | 全部 8 项 | hometown、identity、office、posthumous、deeds | hometown、identity、office、posthumous、deeds |
| intro 段数 / 总字数 | 6—9 段 / 800—1300 字 | 3—5 段 / 400—700 字 | 1—2 段 / 300—450 字 |
| careers 年表 | 15—30 条 | 8—15 条 | 3—6 条 |
| 文治 / 武功 / 得失，每栏 | 5—15 条，可加 `group` 分组 | 2—6 条，不分组 | 1—6 条 |
| relations | 10—18 条 | 4—10 条 | 2—4 条 |
| assessment | 必填 | 必填 | 可选 |
| readingNotes | 5—12 条 | 2—5 条 | 0—2 条 |
| scholarship、relatedEventNotes | 可选 | 可选 | 不设 |
| sourceScope | 必填 | 必填 | 必填（一两句） |

每栏的条数下限只在该栏非空时检查。某栏确实没有材料时，留空并写本人专属的 `note`（§5.5）。

**分级规则（按史料多少）**

分级由 [scripts/person_tiers.py](../scripts/person_tiers.py) 按 book.json 统计后得出，结果写在 [profile_v3.py](../scripts/profile_v3.py) 的 `TIERS` 里。种子文件的 `tier` 必须与之一致，否则生成时报错。

- **A**：开创政权、主持一国军政或决定三国格局的人物，且材料足以展开。由人工指定，见脚本中的 `A_LIST`。
- **B**：有独立的帝纪、本传或附传，并且满足下面任一条件：
  - 正文 ≥ 600 字；
  - 正文 ≥ 300 字，且正文加裴注 ≥ 1500 字。

  另外，没有独立传记、但正文中有 ≥ 20 段散见记载的人物也定为 B，此时 `sourceScope` 第一句要写明“本书无独立本传”。
- **C**：其余人物，即本传很短，或只有少量散见记载的人物；**另外加上按人气入选的人物**（脚本中的 `POPULAR_C`，2026-11-18 确认）。人气入选的人物不论史料多少，一律按 C 级写简版卡；以后需要展开时，再单独升级。
- **移出计划**：知名度较低的 6 人（脚本中的 `EXCLUDED`）不再按 v3 改造，保留现有旧卡，不删页面。

**分级名单（2026-11-13 计算）**

- **A 级（7 人）**：曹操、孙权、刘备、诸葛亮、陆逊、周瑜、司马懿。目前仍是旧 expanded 结构，见 §11。
- **B 级（44 人）**：曹丕、曹叡、袁绍、董卓、孙皓、曹髦、孙策、荀彧、钟会、公孙瓒、刘禅、孙坚、邓艾、吕蒙、姜维、贾诩、曹爽、鲁肃、法正、郭嘉、张昭、荀攸、程昱、太史慈、庞统、陶谦、马超、张鲁、关羽✅、张辽、袁术、刘表、刘焉、赵云、蒋琬、吕范、费祎、刘璋、朱治、吕布、张飞，以及无本传、按散见记载定级的韩遂、司马师、司马昭。
- **C 级（31 人，2026-11-18 调整）**：
  - 迁移已有页面（8 人，均已完成）：黄忠、黄盖、程普、韩当、张绣、马腾、司马炎、张角。
  - 按人气新建页面（23 人，均已登记，流程见 §7.1）：
    - 魏：夏侯惇、夏侯渊、曹仁、典韦✅、许褚、徐晃、张郃、于禁、乐进、庞德；
    - 蜀：魏延、王平、马谡、廖化；
    - 吴：甘宁、凌统、周泰、徐盛、丁奉、蒋钦、潘璋；
    - 其他：华佗、陈宫。
  - 新增人物的 id 见 `person_tiers.POPULAR_C`，例如 `xiahou-dun`、`dian-wei`、`gan-ning`。
- **移出计划（6 人）**：孙乾、麋竺、杜预、王濬、袁谭、袁尚。保留旧卡，不写 v3 种子。

查看每人的统计依据：

```bash
python3 scripts/person_tiers.py           # 每人的传记卷号、正文字数和裴注字数（或散见段数）
python3 scripts/person_tiers.py --check   # 核对统计结果与 TIERS 一致
```

说明：

- 曹丕、曹叡的帝纪篇幅足够做 A 级，但不符合“开创政权或决定格局”这一条，暂定 B。要升级时，把人物 id 加进 `A_LIST`，再同步 `TIERS`。
- 散见段数用称谓关键词计数，只用来粗筛（例如“景王”也可能指别人）。临近 20 段的人物，取证时如发现材料明显不足，按 §0 第 6 条停下汇报。
- 达到 B 级线不等于每一栏都必须写满。B 级栏目的条数下限，只在该栏非空时才检查。

`dossier.tier`（核心人物 / 拓展人物）是页面上显示的标签，**不要改动**。v3 分级写在种子的 `tier` 字段（'A'/'B'/'C'），生成后存为 `dossier.contentTier`。

## 5. 种子格式与写法

文件 `scripts/profile_v3_<id>.py`：

```python
from profile_v3 import Q   # Q(block_or_note_id, 繁体原句, 注引书名=None)

PROFILE = dict(
    id='guanyu', tier='B', reading=['036'],        # reading：本传所在卷，用于“继续读原传”
    lead='…', role='…',
    facts=[...], intro=[...], careers=[...], records=[...],
    scholarship=[...], assessment=[...], relations=[...], readingNotes=[...],
    glossary=[('术语', '解释'), ...],
    sourceScope='…',
    sections={...},              # 可选：仅当某栏为空时写 note
    relatedEventNotes=[...],     # 可选
)
```

同一句引文用到两次以上时，在文件顶部定义成常量（如关羽样例里的 `BAIMA`），保证前后一致。

### 5.1 lead 与 role

- `lead`：60—110 字。一句定位，加上两三件关键事迹和结局。
- `role`：15 字以内，写此人的身份，例如“刘备麾下镇守荆州的前将军”。

### 5.2 facts（基本档案）

每项格式为 `dict(key, label, value, text, refs)`。其中 `deeds` 一项用 `items=[…]` 代替 `value`。

| key | label | value（侧栏短值） | text（详解） |
|---|---|---|---|
| lifespan | 生卒年 | “约155—220年” / “生年未详—219年” | 说明推算依据 |
| hometown | 籍贯 | 郡县 | |
| identity | 主要身份 | 一句话 | 说明势力归属与实际身份的差异（如“卒于称帝前”） |
| office | 最高官职 | | 列出前后历任的主要官职 |
| title | 最高爵位 | 没有就写“无封爵记载” | |
| posthumous | 身后称号 | 谥号 + 年份 | |
| names | 常见称谓 | | 区分本书出现的称谓与后世尊称 |
| deeds | 代表事迹 | `items`：3—8 个四到六字短语 | |

`label` 必须与上表一致，校验按 label 判断是否缺项。

非必填项可以不写（例如 C 级的张角没有 title）。缺项时，侧栏对应位置显示“本书未载”。

### 5.3 intro（人物介绍）

- 每段写成 `dict(title, text, refs, eventLinks=[...])`，按时间顺序排列，每段一个主题，标题 4—12 字。
- 写具体的行动、处境和结果，避免空泛的评价词。
- `eventLinks` 的 `label` 必须是 `text` 中原样出现的字串，多个链接按它们在正文中出现的先后排列。

### 5.4 careers（生平履历，唯一主线）

- 每行写成 `dict(id, when, title, text, office, refs, eventIds=[])`。
- `id` 用简短英文 slug，在同一人物内唯一，例如 `baima`、`fancheng`。
- `when`：明确年份写“200年”；不明确时写“早年，确年未载”或“赤壁战后，确年未载”。**不要从外部材料补年份。**
- `office`：本行发生的官爵变化；没有变化写 `'—'`。
- 事件经过只在年表里完整写一次，文治、武功、得失各栏不要重复复述。

### 5.5 records（文治 / 武功 / 得失）

- 每条写成 `dict(section, when, title, category, text, refs, careerRef=None, eventIds=[])`。
- `section` 只能是 `'civil'`、`'military'` 或 `'setback'`。
- `text` 写“做了什么、效果或后果、怎么评价”，经过由 `careerRef` 指回年表。
- `category` 是短标签，例如“斩将解围”“外交失策”“内部人事”。
- 不要硬凑功绩。关羽的文治只有两条有原文支撑的记录，而且注明了“敌方将领的判断”。
- 某栏完全没有材料时，不写记录，改写说明：

  ```python
  sections={'civil': {'note': '本书只记其统军作战，未见可单列的治理措施；任XX太守期间的施政未载。'}}
  ```

- 自定义栏目名（如文臣用“政务与建言”）要等渲染层迁移后才能使用。现在适配器会直接报错，不要使用。

### 5.6 relations（人物关系）

- 每条写成 `dict(category, name, personId=None, label, text, refs)`。
- `category` 从以下选择：君臣、旧主、亲族、同僚、旧识、邻境、敌对、部属、师友。
- `personId` 只在 cards.json 中存在该人物页面时填写，否则省略。
- `label` 不超过 15 字。`text` 写一两句具体交往。

### 5.7 assessment / readingNotes / scholarship

- 都写成 `dict(title, text, refs)`。
- `assessment`：第一条必须是陈寿的评语（各卷篇末的“評曰”）；其后可以加杨戏《季汉辅臣赞》、裴注所引的评论、同时代人的判断。
- `readingNotes`：放异说、演义与史书的差别、裴松之的辨析。标题直接点明要辨析的问题，`text` 说清谁说了什么、证据强弱如何。
- `scholarship`：读书、著述、个人侧面。没有材料就省略，不要写空条目。

### 5.8 sourceScope

写明以哪一卷为基础、交叉核对了哪些卷、异说放在哪里，结尾固定一句“本页不声称穷尽全书所有提及 X 之处”。没有本传的人物要在第一句说明。

## 6. 取证流程

```bash
python3 scripts/source_lookup.py volume 036 --start 1 --to 7     # 1. 通读本传：正文 + 全部裴注
python3 scripts/source_lookup.py find 關羽 雲長                  # 2. 全书检索（繁体），用本名、字、常见称呼
python3 scripts/source_lookup.py show v054-b0038 v054-b0038-n01   # 3. 读命中段落全文
python3 scripts/source_lookup.py check v054-b0038 '羽果信之，稍撤兵以赴樊。'   # 4. 逐句核对引句
```

1. 先通读本传全文，列出所有事件、官爵变化和人物，形成年表初稿。
2. 再全书检索，重点看相关人物的本传、帝纪、对手方的传记，以及裴注中的异说。
3. 每写一句话就配好对应的引句；第 4 步的核对可以批量做。
4. 裴注的 `books` 为空时，从注文开头的“某某曰”判断书名，例如 `蜀記曰` → `《蜀记》`。
5. 繁简异体以 book.json 为准，例如 `為/爲`、`衆/眾` 在不同卷中写法不同，必须照抄。

## 7. 单人改造步骤

1. 确认人物 id，在 `profile_v3.TIERS` 查出分级，用 `python3 scripts/person_tiers.py | grep <id>` 查本传卷号，再读现有卡片：
   ```bash
   python3 -c "import json;p=[x for x in json.load(open('src/data/cards.json'))['people'] if x['id']=='<id>'][0];print(json.dumps(p,ensure_ascii=False,indent=1))" | head -200
   ```
   现有 `eventIds` 要在新年表中保留，挂到年份对应的行上。
2. 按 §6 取证。
3. 复制同级别样例的结构（A 刘备、B 关羽、C 张角），新建 `profile_v3_<id>.py`，替换全部内容。A 级旧人物先按 §14.1 生成草稿。
4. 在 `profile_v3.py` 的 `V3_MODULES` 中加入 `'profile_v3_<id>'`。
5. 运行生成和校验（§8），按报错修改，直到全部通过。
6. 对照 §2 的 R9、R10 自查一遍，然后按 §9 汇报。

### 7.1 新建人物（尚无人物页的人）

样例：[profile_v3_dian_wei.py](../scripts/profile_v3_dian_wei.py)（典韦）。与改造已有人物相比，多出以下几步：

1. **种子加 `new` 字段**，写页面骨架所需的身份信息：
   ```python
   new=dict(name='典韦', faction='曹魏', period='汉末—197年', aliases=['典君'], tags=['宛城', '濮阳', '双戟']),
   ```
   - `faction` 只能用现有势力：汉末、曹魏、蜀汉、孙吴、西晋。
   - `courtesy`（字）本书有就写，没有就省略，页面会显示“字号未详”。
   - `id` 用 `person_tiers.POPULAR_C` 中给定的值，不要自己拼写。
2. **种子加 `eventRoles` 字段**，至少登记一个既有事件，把本人加入事件参与者：
   ```python
   eventRoles=[('yanzhou-struggle', '濮阳募陷阵，击退吕布'), ('wancheng', '守营门战死')],
   ```
   - 只能选现有事件。事件列表：`python3 -c "import json;print([(e['id'],e['year'],e['title']) for e in json.load(open('src/data/cards.json'))['events']])"`。
   - 角色描述不超过 15 字，写本人在事件中做了什么。
   - 至少一段 intro 要有 `eventLinks`、至少一行年表要有 `eventIds`，并且都要指向 eventRoles 里登记的事件，否则校验报 `Portrait without narrative events` / `milestone events`。
   - **没有合适的既有事件时停下汇报**，不要自己新建事件。华佗是本批的特例：卷二十九有独立本传，现有事件库没有可直接关联的条目，故保留空的 `eventRoles`，通过人物关系和原传继续阅读。其余新人物仍需有事件链接。
3. **facts 必须有 lifespan**。侧栏的生卒年会自动按 lifespan 的 `value` 和第一条引文生成。
4. **把 `src/data/edition.json` 中的 `"people"` 加 1**。这是新建人物时唯一允许修改的其他文件。
5. 验收时 §8 的 `changed:` 会显示本人；`events same` 会是 False，属于正常情况。改用下面的命令确认事件只多了本人这一个参与者：
   ```bash
   python3 -c "
   import json;a=json.load(open('/tmp/cards.before.json'));b=json.load(open('src/data/cards.json'));ea={e['id']:e for e in a['events']}
   for e in b['events']:
       old=ea[e['id']]
       if old!=e: print(e['id'],[k for k in e if old.get(k)!=e[k]],[p for p in e['participants'] if p not in old['participants']])"
   ```
   预期只看到 eventRoles 中的事件，变动字段只有 `participants` 和 `tags`。如果该人物已经以纯文本列在参与者中，则在原处转成链接；多人合列时保留其他人的姓名和原有说明。
6. 新人物与已有人物的关系，只在本人的 `relations` 中写。**不要去改对方的种子文件**补回链。如果尚未建页的人物（例如写典韦时的许褚）出现在关系里，省略 `personId`，等对方建页后再补。

## 8. 验收命令与通过标准

在仓库根目录依次运行：

```bash
cp src/data/cards.json /tmp/cards.before.json
python3 scripts/person_tiers.py --check
python3 scripts/create_cards.py > /tmp/gen.log && tail -1 /tmp/gen.log
cp src/data/cards.json /tmp/cards.run1.json && python3 scripts/create_cards.py >/dev/null && cmp src/data/cards.json /tmp/cards.run1.json && echo deterministic
python3 -c "
import json;a=json.load(open('/tmp/cards.before.json'));b=json.load(open('src/data/cards.json'))
pa={p['id']:p for p in a['people']};print('changed:',[i for i,p in ((p['id'],p) for p in b['people']) if pa[i]!=p]);print('events same:',a['events']==b['events'])"
node scripts/validate-content.mjs
npm test
npx astro check
npx astro build --outDir /tmp/sgz-dist
```

通过标准：

- 生成两次结果一致，输出 `deterministic`。
- `changed:` 中只有本次改造的人物，`events same: True`（新建人物见 §7.1 第 5 步）。
- validate、test、astro check 均无错误。
- `/tmp/sgz-dist/people/<id>/index.html` 的体积：A 级不超过 250KB，B 级不超过 150KB，C 级不超过 80KB。三个样例分别是 210KB、145KB、46KB。

  体积主要由“原文依据”列表决定，每条依据的固定标记约 0.9KB。渲染层迁移后会精简这部分标记，届时再把 A 级收紧到 200KB。超标时先合并重复的引句，不要删去必要的依据。
- 如有浏览器工具，用 `python3 -m http.server 4331 --directory /tmp/sgz-dist` 打开 `/people/<id>/`，检查：目录各栏都有内容、320px 宽度无横向溢出、控制台无错误、事件和人物链接可点击。

## 9. 汇报格式

```text
人物：<姓名>（<id>），分级 <A/B/C>
新增/修改文件：…
栏目统计：intro N 段 / X 字；careers N；文治 N；武功 N；得失 N；关系 N；评价 N；辨析 N；引文 N 条
验收：deterministic ✓ / 只改动本人 ✓ / validate ✓ / test ✓ / check ✓ / 页面 XKB
需人工确认：<材料矛盾、判断存疑、找不到原文的必填项；没有则写“无”>
```

## 10. 常见错误

| 报错 | 原因与处理 |
|---|---|
| `AssertionError: (id, quote)` | 引句不是原文子串。用 `source_lookup.py check` 核对，常见原因是繁简异体或标点不同。 |
| `只给了段落 ID` | 把 `'v036-b0002'` 改成 `Q('v036-b0002', '…')`。 |
| `裴注引文缺少注引书名` | 给 `Q()` 补第三个参数。 |
| `v3 quote too long` | 引句截短到能支撑该说法的那一句。 |
| `Missing reciprocal person event` | 事件 participants 中没有本人。去掉这个 eventId，不要改事件数据。 |
| `Expanded career event date mismatch` | 年表行的年份与事件年份不吻合，把 eventId 挂到正确的行。 |
| `Missing or unordered event label` | `eventLinks.label` 不在 text 中，或顺序与正文不一致。 |
| `out of range` | 按 §4 增删条目。不要为了凑数编造，宁可合并或改写说明。 |

## 11. 当前限制与后续迁移

渲染层（`PersonDossier.astro`、`catalog.ts`）尚未改动，所以存在以下差异：

1. 侧栏“主要身份”显示的是 `role`，“常见称谓”显示的是 `aliases`。facts 的 `identity`、`names` 详解只出现在“档案详解与依据”中。
2. 侧栏“生卒年”仍取自旧的 `lifespan` 字段，v3 的 lifespan 只出现在详解中，写的时候注意两者保持一致。
3. 不支持自定义栏目名，`careerRef` 也不会在页面上显示为链接。
4. A 级的“链接到阅读器卷”就是页面底部已有的“继续读原传”，不需要另外实现附录。

后续迁移顺序：

1. 渲染层支持 v3 字段：facts 列表、自定义 sections、careerRef 链接；新旧字段并存。
2. 把六人迁移为 v3 种子：facts 拆项并逐项补 refs，relations 补 category，civil、military、setbacks 合并为 records。**刘备已完成**（§14.1）；还剩诸葛亮、孙权、周瑜、陆逊、司马懿。
3. 迁移曹操：整段引文改为逐句；补齐年表 eventIds；删除内嵌附录。
4. 删除旧 expanded 分支与 `profiles_*_expanded.py`。
5. 其余 B、C 级人物按本文逐个改造，每次一人。

## 12. 交给 Sonnet / Codex 的任务提示词

```text
在 /Users/zhangliang/ai/readbook/sanguozhi/sanguozhi-simplified 中，按 docs/person-template-v3.md 把人物 <姓名>（id: <id>）改造成 v3 <B> 级人物卡（尚无人物页的人物，按 §7.1 新建）。
先完整阅读该文档和同级别样例（A：scripts/profile_v3_liubei.py；B：scripts/profile_v3_guanyu.py；C：scripts/profile_v3_zhang_jiao.py；新建人物：scripts/profile_v3_dian_wei.py），再用 scripts/source_lookup.py 取证。
只新增 scripts/profile_v3_<id>.py 并在 scripts/profile_v3.py 的 V3_MODULES 中登记（新建人物另把 src/data/edition.json 的 people 加 1）；不要改其他文件，不要 git 提交，不要运行 npm run build。
完成后运行文档 §8 的全部验收命令，并按 §9 的格式汇报。遇到 §0 第 6 条所列情况时停下汇报。
```

## 13. 已确认的决定（2026-11-13）

1. 分级按史料多少划分（规则与名单见 §4）：A 7 人、B 44 人、C 14 人。
2. 附录不再内嵌整卷原文，改为链接到阅读器。
3. “失误、挫折与争议”各级必填；没有材料时写本人专属说明。
4. 允许按人物自定义栏目名，但要等渲染层迁移后才能使用；默认栏目为“文治功绩 / 武功功绩 / 失误、挫折与争议”。
5. （2026-11-18）C 级改为“史料少的人物 + 按人气入选的三方武将”，共 31 人；人气入选者不论史料多少一律写 C 级简版卡。孙乾、麋竺、杜预、王濬、袁谭、袁尚移出 v3 计划，保留旧卡。名单见 §4。

## 14. 三个样例说明

三个样例都已通过 §8 的全部验收，并已在浏览器中检查过 320px 宽度。下表是各样例的栏目统计：

| 项目 | A 刘备 | B 关羽 | C 张角 |
|---|---|---|---|
| 材料基础 | 卷三十二《先主传》（正文 7562 字） | 卷三十六本传（正文 1145 字） | 无本传；正文 1 段 + 3 条裴注 |
| 人物介绍 | 8 段 / 954 字 | 4 段 / 455 字 | 2 段 / 330 字 |
| 生平履历 | 28 条 | 15 条 | 4 条 |
| 文治 / 武功 / 得失 | 9 / 11 / 9，按主题分组 | 2 / 4 / 5，不分组 | 0（写说明）/ 1 / 1 |
| 关系 / 评价 / 辨析 | 11 / 3 / 7 | 10 / 3 / 5 | 3 / 0 / 2 |
| 档案项 | 8 | 8 | 7（无 title） |
| 引文条数 / 页面 | 113 / 210KB | 95 / 145KB | 21 / 46KB |

### 14.1 A 级：刘备——旧人物迁移的示范

**为什么选他**：A 级 7 人都已有完整的旧版内容，A 级工作的重点是把旧数据迁到 v3，而不是重写。刘备的旧数据本来就是逐句引文，迁移步骤最典型。

**做法**：

1. 生成草稿：
   ```bash
   python3 scripts/migrate_expanded_to_v3.py profiles_shu_expanded <id> > /tmp/draft.py
   ```
   草稿原样搬运叙述、年表、得失、评价、辨析和名词，引文不变。
2. 人工补齐草稿中标 TODO 的部分：
   - **facts**：旧版只有一个合并字典，要拆成 8 项，每项写自己的依据。例如“最高官职”要区分 219 年群下推拜的大司马与 211 年刘璋所推的“行大司马”；生卒年写明 161 年是由“时年六十三”逆推。
   - **careers 的 id**：把 c01、c02…改成有意义的 slug（youth、xuzhou、chibi…），并同步 `careerRef`。
   - **relations**：补 category、personId 和具体交往的 text；关羽一条补上了卷三十六“恩若兄弟”的引文。
   - **sourceScope**：删去“附录收录全卷”的说法，改为指向阅读器。
   - **role**：压到 15 字以内（“蜀汉开国皇帝”）。
3. 从旧模块中删除该人物：删去 `LIUBEI = dict(...)`、对它的后续修改和分组代码，`PROFILES` 中去掉 `'liubei'`。删除后重新生成，确认 cards.json 与删除前完全一致。
4. 结果：内嵌附录去掉了，页面从 320KB 降到 210KB；只有刘备这张卡发生变化。

**可以借鉴的写法**：得失记录按主题分组（反复失据、扩张与刑罚、荆州丧失与晚年失策），把失败和争议当作一个独立的叙事维度来写，而不是零散罗列。

### 14.2 B 级：关羽——从零取证的标准写法

**为什么选他**：B 级 44 人是工作量最大的一批，多数人只有张飞版的短卡，需要从本传开始重新取证。

**看点**：

- **取证范围**：以本传正文和全部裴注为基础，再交叉核对 10 多卷相关传记（武帝纪、于禁、徐晃、庞德、费诗、吴主传、鲁肃、吕蒙、陆逊等）。对手一方的记载往往提供本传没有的细节，例如吕蒙称病诱关羽撤兵、擅取湘关米。
- **文治栏不硬凑**：只有两条有原文支撑的记录，其中“恩信大行”明确标注是敌方将领的判断。
- **得失栏写因果**：从驱逐吴方长吏、辱骂求婚使者，到与麋芳、士仁失和，再到轻信吕蒙、陆逊，每一条都对应败亡的一个环节。
- **史料辨析**：刮骨疗毒、秦宜禄之妻、许田劝杀曹操、马超直呼刘备的字、被擒地点。每条都写清出处和裴松之的判断，演义情节只说“本传未载”，不展开。

### 14.3 C 级：张角——无本传人物的写法

**为什么选他**：C 级里有一半人没有本传。张角材料最少，只有正文一段和三条裴注，最能说明在“材料很少”时应该怎么写。

**看点**：

- **sourceScope 第一句就说明“本书无张角传”**，并列出全部依据的出处。籍贯、生卒、被诛经过都写“本书未详”，不用《后汉书》补写。
- **档案用“未详 + 已知线索”的写法**：籍贯写“本书未详（起事于魏郡）”；最高官职写“无汉朝官职；自称天公将军”；没有爵位就不写 title。
- **空栏目写本人专属说明**：文治栏说明他不是官员，并指引读者去看“生平履历”和“阅读提示与史料辨析”。
- **辨析写出版本与立场问题**：“三十六（萬）”的括号是校勘标记，所以不写成“三十六万人”；太平道的描述全部出自《典略》，带有汉魏士人的立场。
- **字数下限**：C 级介绍至少 300 字，这是全站对每位人物介绍的最低要求。材料少时，用相关人物的反应（孙坚、曹操讨黄巾）和后续影响（黑山诸部、张鲁沿用道法）补足，但每句都要有引文。

### 14.4 选哪个样例照抄

- 迁移曹操、诸葛亮、孙权、周瑜、陆逊、司马懿：照**刘备**的做法。其中曹操的旧数据是整段引文，需要逐条改成逐句引文。
- 有本传、篇幅够 B 级线的人物：照**关羽**。
- 本传很短，或没有本传的人物：照**张角**。
- 尚无人物页、要新建的人物（人气 C 级的 23 人）：照**典韦**（§7.1）。他们多数本传较长，C 级篇幅装不下全部材料：只写最有代表性的两三件事，其余留给“继续读原传”。
- 没有本传但定为 B 级的人物（韩遂、司马师、司马昭）：篇幅照关羽，`sourceScope` 和档案的写法照张角。

