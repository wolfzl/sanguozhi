# 三国志事件线升级执行记录

计划：docs/history/superpowers/plans/2026-10-09-timeline-v2.md；已确认设计：docs/history/superpowers/specs/2026-10-09-timeline-design.md。

- worktree：<workspace>/tmp/sanguozhi-timeline；基线 c1ce3ab；分支 feat/sanguozhi-timeline-v2。
- 原生 create_worktree 返回 Not a git repository（当前对话无绑定仓库）；为遵守用户指定 /tmp 位置，使用独立源仓库 git worktree add 创建。
- 基线：Python 6 / Node 7 通过。
- 内容两个独立文件并行编写，父代理整合；没有多人编辑 cards.json。
- 接口：expand_people(base,R)；expand_events(base,R)；build_relationships(R)。统一生成 eventIds，关系只存一份。
- Task 3：四个时间线行为测试在缺失功能时失败，新增函数后通过；三个内容关系验证测试同样由失败转为通过。累计 Python 6 / Node 14 通过。
- 规则：264 年钟会之乱属于曹魏政权线，不能延续已经结束的蜀汉线；姜维仍作为人物参与。
- Ruling：年距非等比；同年内 order 表示阅读顺序，除明确史料外不推断月日。
- Ruling：独立编辑种子适用 dispatching-parallel-agents，集成与复核由父代理顺序完成，避免共享文件冲突。
- npm 审计：原有 Astro 5 依赖树报告 1 low/1 high/1 critical（修复建议 Astro 7 跨大版本）。当前保留批准的 Astro 5 静态本地方案，未在本内容升级中进行大版本迁移；公开部署前应独立评估框架升级。本站不接受上传、无服务端渲染接口，预览仅绑定127.0.0.1。

- 复核修正：同年独立势力事件使用显式行分配，200年孙权接班与官渡在同一行；筛选后重排行号避免留空。
- Ruling：234年蒋琬接掌蜀政归入第二阶段，与五丈原共用年份组，第三阶段从239开始；总数38不变，阶段9/16/13。用户要求同年对齐优先于设计草案的阶段计数。

- Task 3复核：work/ui-review.md，spec compliance / code quality通过；8个时间线相关测试、Astro检查0错误。集成后还需浏览器验证。
- 史料纠正：孙权受封吴王在221年，222为黄武改元；229年称帝。

- 集成首次生成在精确引句检查处停止：v047-b0020“封權爲吳王”不匹配本书字形；未写入cards.json。已交事件编辑在源模块修正，保留R严格子串验证。

- Task 1、2：扩展模块完成并统一生成38事件/34人物/43关系；准确引用1310，所有互链验证通过。
- 独立内容审查：发现并修正曹叡子嗣误读、钟会跨年节点、曹髦迎立证据；最终无阻断项。
- Task 4：21测试通过，Astro0错误，构建144页；最终浏览器143正常页/4918链接、无runtime错误，1440/390/320及同年布局验收通过。
- 视觉复核：桌面跨线卡、手机单列截图已实看，保存在docs/previews。
- 集成方式：依用户本地交付边界，保留开发分支与新worktree；原版分支不合并、不覆盖。
