# 文档索引

- [development.md](development.md)：开发指南，包括环境、数据流、引用格式、校验、测试与部署。

## guides/ · 写作与数据规范

| 文档 | 内容 |
|---|---|
| [person-template-v3.md](guides/person-template-v3.md) | 人物档案 v3 模板：分级、字段、写作要求 |
| [atlas-trajectory-guide.md](guides/atlas-trajectory-guide.md) | 人物行迹地图的数据规则与站号核对 |
| [design.md](guides/design.md) | 网站整体设计说明 |
| [simplified-reader.md](guides/simplified-reader.md) | 原文阅读的简繁切换设计 |
| [person-dossiers.md](guides/person-dossiers.md) | 全人物档案统一的做法 |
| [person-portraits.md](guides/person-portraits.md) | 人物小传的写作方式 |

## reviews/ · 史料核对与验收

人物、事件、行迹地图和白话译文的逐项核对记录。读者可以从这里查看某条内容是如何确认的。

| 文档 | 内容 |
|---|---|
| [content-review.md](reviews/content-review.md) | 首版内容核对 |
| [event-v2-review.md](reviews/event-v2-review.md) | 事件线第二版复核 |
| [person-v2-review.md](reviews/person-v2-review.md) | 人物第二版复核 |
| [han-lords-expansion.md](reviews/han-lords-expansion.md) | 汉末诸侯扩充的范围与验证 |
| [han-b-profile-review.md](reviews/han-b-profile-review.md)、[wei-b-profile-review.md](reviews/wei-b-profile-review.md)、[wu-b-profile-review.md](reviews/wu-b-profile-review.md) | 各势力 B 级人物与行迹验收 |
| [shu-trajectory-review.md](reviews/shu-trajectory-review.md) | 蜀汉人物行迹纠错 |
| [wei-translation-progress.md](reviews/wei-translation-progress.md)、[shu-wu-translation-progress.md](reviews/shu-wu-translation-progress.md) | 白话译文进度与疑难处 |

## audits/ · 行迹审计数据

`*-trajectory-audit.json` 是各势力人物行迹的逐站核对数据，由 `scripts/check-*-trajectories.mjs` 和 `scripts/atlas-places.mjs` 读取。

## history/ · 开发过程记录

早期版本的计划、执行记录、验收报告和设计稿，仅作存档。其中的路径用 `<repo>`、`<workspace>` 等占位符代替了原来的本地目录。

## images/

README 使用的截图。
