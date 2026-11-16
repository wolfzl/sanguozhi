# 人物行迹地图指南

本文是给执行者（Claude Sonnet 5.5、Codex 或人工）的操作规范。照本文把一位 v3 人物的生平履历分成几个**时期**，页面就会按时期分组显示履历，并生成“行迹地图”，同时通过自动校验。

- 状态：第二版（2026-11-13）。第一版按履历逐行标地点，刘备有 23 站，太细，重点不突出，已经废弃。样例仍是刘备（详见 §13）：

  | 样例 | 种子文件 | 页面 |
  |---|---|---|
  | 刘备（模式一：复用江山时序路线） | [profile_v3_liubei.py](../scripts/profile_v3_liubei.py) 的 `trajectory` | `/people/liubei/#trajectory` |

- 本文是 [person-template-v3.md](person-template-v3.md) 的补充。人物卡的取证规则（R1–R10）照旧适用；本文只规定时期怎么分、地图怎么接。

---

## 0. 执行者须知（先读）

1. **只做 v3 人物。** 时期写在 v3 种子文件的 `trajectory` 字段里。还没迁到 v3 的人物（诸葛亮、孙权、周瑜、陆逊、司马懿、曹操）等迁移时再做。
2. **一次只改一个人物**，通常只改 `scripts/profile_v3_<id>.py`。不要改 `src/components/`、`src/lib/`、校验脚本和江山时序项目；需要支持新情况时先说明原因并获得授权。2026-11-13 经用户确认，模式二已支持“地点未详”的时期，见 §6。
3. **不要提交 git，不要执行 `npm run build`**（理由同人物卡指南 §0）。
4. **先查江山时序有没有这个人的路线**（§5）。有就用模式一，没有才用模式二。
5. 发现路线与本书记载冲突或地名解析错位时，先记录证据；若任务已明确要求修正路线，可在地图仓库的独立 worktree 修正，并与本站的站号、时期链接联动验收。普通人物卡新增任务不擅自扩大到地图数据改写。

## 1. 背景与两种模式

用户在本站看完人物，跳到江山时序，或者在江山时序里搜这个人，看到的应该是**同一条路线**。所以：

| 模式 | 适用 | 地图上的路线 | 本站负责 |
|---|---|---|---|
| 一：复用江山时序路线 | 江山时序已有路线的 15 人（§5） | 江山时序自己的人物路线（`?person=<key>`） | 时期划分、每个时期对应路线的哪几站 |
| 二：本站时期路线 | 其余人物 | 已知时期的代表地点连成路线（`?year=…&place=…`），地点未详的时期不标点 | 时期划分、代表地点或未标点原因 |

两种模式下，**本站页面上的文字都只来自本书**：时期名称、年份、履历内容。江山时序路线里的文字（例如“与关羽、张飞于涿县募兵”）只显示在江山时序里，本站不转述。

## 2. 硬性规则

| # | 规则 | 由谁检查 |
|---|---|---|
| M1 | 时期按顺序覆盖年表的**全部**行，每行只属于一个时期，顺序和年表一致，不跳行。 | `validateTrajectory` |
| M2 | 时期数：A 级 5–8，B 级 3–6，C 级 2–4。每个时期至少 1 行。 | `validateTrajectory` |
| M3 | `span` 是两个整数 `(起, 止)`，起 ≤ 止；时期之间不倒退（后一期的起年不早于前一期的起年）。 | `validateTrajectory` |
| M4 | 模式一：`atlasPerson` 写江山时序的人物 key；每个时期的 `atlasStops` 是路线中的站号（从 0 数），站点年份必须落在本时期 `span` 内；站号全程递增。和本人关系不大的站可以不挂。页面链接按首站到末站生成区间，所以同一时期的站号必须连续。 | `validateTrajectory` + `atlas-places.mjs check` |
| M5 | 模式二：每个时期提供 `place` 或非空的 `unmappedReason`，二者互斥；全程至少有一个已知地点。`place.name` 必须出现在本时期某一行的 `when`、`title` 或 `text` 中；`mapYear` 落在 `span` 内且不倒退；查询名、省份、近似标记规则见 §6。 | `validateTrajectory` + `atlas-places.mjs check` |
| M6 | 时期名称概括本期的发展阶段或重大事件，不超过 10 个字，不写本书没有的事。 | 人工审查 |

## 3. 数据格式

`trajectory` 写在 PROFILE 顶层：

```python
# 模式一：复用江山时序路线（刘备）
trajectory=dict(
    atlasPerson='liubei',
    phases=[
        dict(id='xuzhou', title='争夺徐州', when='193—199年', span=(193, 199),
             careers=['taoqian', 'xuzhou', 'yicheng', 'xiaopei', 'lvbu', 'dongcheng'],
             atlasStops=[1]),
        dict(id='jingzhou', title='荆州与赤壁', when='208—210年', span=(208, 210),
             careers=['changban', 'chibi', 'gongan'],
             atlasStops=[3, 4]),
        ...
    ],
),

# 模式二：本站时期路线（示意，非真实数据）
trajectory=dict(
    phases=[
        dict(id='hebei', title='据有冀州', when='191—199年', span=(191, 199),
             careers=['jizhou', 'jieqiao', 'yijing'],
             place=dict(name='邺', query='邺', province='河南', mapYear=191)),
        ...
    ],
),
```

| 字段 | 必填 | 含义 |
|---|---|---|
| `atlasPerson` | 模式一 | 江山时序人物 key，见 §5。 |
| `phases[].id` | 是 | 英文 slug，同一人物内唯一。 |
| `phases[].title` | 是 | 时期名称，页面上作为分组标题。 |
| `phases[].when` | 是 | 显示用的时间，写法同年表的 `when`（不明时写“确年未载”）。 |
| `phases[].span` | 是 | `(起, 止)` 整数年，只用于校验和地图取景，不显示。 |
| `phases[].careers` | 是 | 本时期包含的年表行 id，按顺序。 |
| `phases[].atlasStops` | 模式一 | 对应江山时序路线的站号列表（从 0 数）；可以为空列表。 |
| `phases[].place` | 模式二，地点已知时 | 代表地点 `dict(name, query, province, mapYear, approx=True?)`，含义同 §6。 |
| `phases[].unmappedReason` | 模式二，地点未详时 | 非空字符串，解释史料未载地点的情况；与 `place` 互斥，不生成地图站点或时期地图链接。 |

数据流向：种子 `trajectory` → `profile_v3.finish()` 原样写入 `cards.json` 的 `people[].dossier.trajectory` → 页面。

## 4. 怎么分时期

1. **按人生转折分，不按年份平均分。** 一个时期结束于一次处境的变化：失去根据地、投靠新主、称王称帝、战败等。
2. **重大事件可以单独成期。** 例如赤壁之战前后两三年，足以单列为“荆州与赤壁”。
3. **早年材料少时，早年与起兵合为一期**，不要为了凑数拆开。
4. **确年不明的行跟着上下文走。** 例如刘备的“博望设伏”（寄居荆州期间）归入“依附袁绍、刘表”。
5. **先写年表，再分时期。** 时期只是给年表分组，不新增史实，所以时期本身不需要引文。

## 5. 江山时序已有路线的人物

用下面的命令查看某人的路线和站号：

```bash
node scripts/atlas-places.mjs person liubei
```

截至 2026-11-16，本站 65 人中有 21 人在江山时序里有路线：

| 本站 id | `atlasPerson` | 站数 | 本站 id | `atlasPerson` | 站数 |
|---|---|---|---|---|---|
| caocao | caocao | 16 | luxun | luxun | 4 |
| liubei | liubei | 13 | sima-yi | simayi | 6 |
| zhuge-liang | zhugeliang | 11 | zhouyu | zhouyu | 5 |
| sunquan | sunquan | 7 | zhangfei | zhangfei | 10 |
| guanyu | guanyu | 7 | jiang-wei | jiangwei | 17 |
| du-yu | duyu | 7 | yuanshao | yuanshao | 3 |
| zhaoyun | zhaoyun | 9 | deng-ai | dengai | 3 |
| lv-bu | lvbu | 3 | ma-chao | machao | 7 |
| pang-tong | pangtong | 5 | fa-zheng | fazheng | 4 |
| liu-shan | liushan | 6 | jiang-wan | jiangwan | 5 |
| fei-yi | feiyi | 9 | | | |

本轮九名蜀汉人物使用带原文引用的独立人物站点（`curatedOnly`），不再混入只提及姓名的公共事件。详见 [核对数据](shu-trajectory-audit.json)。其他人物仍沿用既有路线。上游新增事件后，站号可能整体后移；`atlas-places.mjs check` 会按年份核对，发现错位就报错。

## 6. 模式二：代表地点

每个时期选一个最能代表这一时期的地点，一般是本人在这一时期主要驻扎或决定命运的地方，**标本人所在地**，不标部将作战地、出使目的地或只是建议攻打的地方。

**史料未载地点时**，保留时期和履历，以 `unmappedReason` 说明缺失，不写 `place`。页面显示“地点未详”及原因，保留跳回履历的链接；地图仅标已知地点，全程至少需要一个。只有一个已知地点时展示单点，不补造路线。若确年也未载，`when` 必须注明，`span` 只用于取景范围，不作为事件年份依据。样例为 `profile_v3_zhang_jiao.py`：传道与联结信众、魏郡起事、遭讨击与被诛三期，仅第二期在魏郡标点，地图近似解析为元城（大名）。

江山时序的地名库以名城、名关为主，三国县邑不全：

| 情况 | 例子 | 处理 |
|---|---|---|
| 能直接识别 | 新野、赤壁、成都、阳平关 | `query` 同 `name`，不写 `approx` |
| 识别到附近的地方 | 公安 → 江陵；博望 → 新野 | 写 `approx=True` |
| 识别不了 | 安喜、小沛、雒城 | 换查询名：安喜 → `中山`，小沛 → `沛国`；写 `approx=True` |
| **识别错位** | 平原 → 灵州（宁夏）；海西 → 青海 | 必须换查询名，例如平原 → `平原郡` |

规则：

- 地图解析出的地名（去掉括号注释后）与 `name` 不同，就必须写 `approx=True`，相同就不写。
- `province` 写今省份简称，用来发现解析错位。
- 解析结果会随年份变化，例如永安在 196 年解析为白帝城，在 223 年解析为永安本身。试查询名时 `--year` 要用打算写的 `mapYear`：

```bash
node scripts/atlas-places.mjs lookup 安喜 中山 平原 平原郡 --year 184
```

## 7. 页面效果

1. **生平履历按时期分组。** 每个时期前有一行标题：“一 · 争夺徐州 · 193—199年 · 在地图上看 ↗”。点链接会在新窗口打开江山时序：模式一用 `?person=<key>&stop=<首站>-<末站>` 把本期所有站和路线一起高亮为实线（只有一站时写 `stop=<站号>`），模式二打开代表地点。
2. **行迹地图**（`#trajectory`，紧接生平履历，并加入侧栏目录）：
   - 嵌入地图。模式一嵌入江山时序的人物路线，和在江山时序里搜这个人看到的完全一样；模式二嵌入各时期代表地点连成的路线。
   - 下方是时期清单：序号 · 时期名 · 时间 · 地图第几站（模式一）或代表地点／地点未详说明（模式二），以及本期包含的履历条目（点击可跳回履历）。地点未详的时期没有“在地图上看”链接。
   - “在江山时序中打开 ↗”。

地图地址由 `src/lib/atlas.mjs` 统一生成。本地默认 `http://127.0.0.1:8000/`，发布时用环境变量 `PUBLIC_ATLAS_BASE` 指定。

## 8. 单人步骤

1. 列出年表：
   ```bash
   python3 -c "import sys;sys.path.insert(0,'scripts');import profile_v3_<id> as m;[print(c['id'],c['when'],c['title']) for c in m.PROFILE['careers']]"
   ```
2. 按 §4 划分时期，写出 `id`、`title`、`when`、`span`、`careers`。
3. 查 §5：有路线就用 `atlas-places.mjs person <key>` 列出站号，按年份挂到各时期；没有路线就按 §6 选代表地点。
4. 写进种子文件，运行 §9 的验收命令，直到全部通过。
5. 用浏览器打开页面，点每个时期的“在地图上看”，确认落点正确。

## 9. 验收命令与通过标准

在仓库根目录依次运行：

```bash
python3 scripts/create_cards.py > /tmp/gen.log && tail -1 /tmp/gen.log
node scripts/validate-content.mjs
node scripts/atlas-places.mjs check <id>
npm test
npx astro check
npx astro build --outDir /tmp/sgz-dist
```

通过标准：

- 以上命令均无错误。
- 用 `python3 -m http.server 4331 --directory /tmp/sgz-dist` 打开 `/people/<id>/#trajectory`（需要 8000 端口在运行）：地图能加载；模式一的路线与江山时序里搜这个人看到的一致；320px 宽度下没有横向溢出。

`atlas-places.mjs` 依赖本机的江山时序项目（默认 `~/ai/github/jiangshan-map`，可用环境变量 `JIANGSHAN_DIR` 指定），所以不放进 `npm run build`。

## 10. 汇报格式

```text
人物：<姓名>（<id>），模式 <一/二>
时期：N 个——<时期名（行数）>，…
模式一：路线共 K 站，挂上 M 站；未挂的站：<站号及原因>
模式二：近似地点 X 个
验收：validate ✓ / atlas check ✓ / test ✓ / check ✓ / 浏览器 ✓
需人工确认：<江山时序路线与本书冲突之处；没有则写“无”>
```

## 11. 常见错误

| 报错 | 原因与处理 |
|---|---|
| `trajectory careers not covered in order` | 时期没有按顺序覆盖全部年表行。检查是否漏行、重复或顺序颠倒。 |
| `trajectory phase count out of range` | 时期数超出 M2 的范围。 |
| `trajectory span goes backwards` | 后一期的起年早于前一期。 |
| `trajectory atlasStops must increase` | 站号没有全程递增。 |
| `trajectory atlasStops must be consecutive` | 同一时期的站号不连续。区间链接会把中间的站一起高亮，所以要么把中间的站也挂进来，要么拆成两个时期。 |
| `trajectory needs atlasStops` / `needs place or unmappedReason` | 模式一的时期缺 `atlasStops`，或模式二的时期既无 `place` 也无有效的 `unmappedReason`。 |
| `trajectory has both place and unmappedReason` / `needs at least one mapped place` | 模式二的时期同时提供两种地点状态，或全程没有一个已知地点。 |
| `atlas stop year outside span` | 站点年份不在时期 `span` 内。多半是上游新增事件导致站号后移，重新用 `person` 命令查站号。 |
| `atlas place name not in phase` | 模式二的 `name` 不在本时期任何一行中。 |
| `未识别` / `province mismatch` / `approx should be …` | 见 §6。 |

## 12. 当前限制与后续

1. 江山时序的路线文字不受本站取证规则约束，本站不转述；发现与本书明显冲突的，记录依据；路线纠错任务按上文要求联动修改地图数据并验收。
2. 江山时序路线的站号依赖上游事件库，上游更新后要重跑 `check`。
3. 时期区间高亮（`stop=3-4`）是本地江山时序新增的功能，已合并到本地 `main`（提交 `9376084`，2026-11-13），8000 端口的服务已支持。上游 `DeanChensj/jiangshan-map` 和线上的 deanchen.me 还不支持区间，遇到区间会退回只高亮首站。发布到线上前，要么把这个功能合并到上游，要么让 `PUBLIC_ATLAS_BASE` 指向带此功能的部署。
4. 事件页暂时没有地图链接。
5. 诸葛亮等 6 位旧结构人物，迁移到 v3 时一并分期。

## 13. 样例：刘备（模式一）

年表 28 行分为 7 个时期。江山时序的刘备路线共 13 站，挂上 12 站；第 7 站（214 年“张飞镇守阆中”）主角是张飞，不挂。

| # | 时期 | when | 年表行 | 江山时序站号 | 站点 |
|---|---|---|---|---|---|
| 1 | 早年与起兵 | 少年至初平年间 | youth, yellow, duyou, gongsun | 0 | 184 涿县 |
| 2 | 争夺徐州 | 193—199年 | taoqian, xuzhou, yicheng, xiaopei, lvbu, dongcheng | 1 | 196 徐州 |
| 3 | 依附袁绍、刘表 | 200—207年 | yuanshao, liubiao, bowang, xuxi, longzhong | 2 | 207 隆中 |
| 4 | 荆州与赤壁 | 208—210年 | changban, chibi, gongan | 3, 4 | 208 长坂、赤壁 |
| 5 | 取益州 | 211—214年 | entershu, chengdu | 5, 6 | 212 葭萌、214 成都 |
| 6 | 争汉中、称汉中王 | 215—219年 | boundary, wudu, dingjun, hanzhongwang | 8, 9 | 219 阳平关、汉中 |
| 7 | 称帝、东征与托孤 | 220—223年 | liufeng, accession, yiling, entrust | 10, 11, 12 | 221 成都、222 夷陵、223 永安 |

**可以借鉴的地方**：

- **时期名称只用本书能支撑的说法。** 江山时序第 0 站写“与关羽、张飞于涿县募兵”，本书《先主传》只写“率其属从校尉邹靖讨黄巾”，所以本站这一期叫“早年与起兵”，不提“桃园”或“三人募兵”。
- **不硬挂无关的站。** 第 7 站是张飞的事，挂上去会让“取益州”看起来包括了张飞镇守阆中，所以留空。它夹在第 5 期（5、6 站）和第 6 期（8、9 站）之间，不在任何区间里，所以不会被高亮。
- **多站时期整段高亮。** 例如“荆州与赤壁”链接为 `?person=liubei&stop=3-4`，隆中→长坂→赤壁两段都是实线；第一版只跳到首站时，只有隆中→长坂一段是实线。
- **第一版的教训。** 按行标点会得到 23 站，读者看不出主线；按时期分组后，履历和地图都只突出 7 个阶段，地图也和江山时序一致。

## 2026-11-16 蜀汉九人路线修正

- 张飞、赵云、姜维补齐本书已明确记载的关键往返；其余六人从单个代表地点改为独立人物路线，与 A 类人物共用绘制与 `stop=首-末` 高亮。
- 一期可有多站；确年未载的站点在详情中标出取景排序年，不能将它当作确切史年。地域或战址未精确确定时在地点说明中标出近似范围。
- 线型只表达选中范围：选中时期的到达路段为实线，其余路段为虚线。全程概览沿用 A 类的虚线轨迹；没有站点的时期不生成地图链接。
- 原文只记计划、任官、追谥且不能定位的经历保留在履历，不强行标点。蒋琬留府的成都位置为上下文推定，地图说明明确标出；西平之役保留249/250年分歧。
- 联动验收必须用同一版本地图运行 `atlas-places.mjs check` 和地图侧 `node scripts/check_shu_trajectories.cjs`。地名查询的省份一致不足以证明位置正确；蜀汉江州、冀城、汉寿、沓中等使用独立坐标。
