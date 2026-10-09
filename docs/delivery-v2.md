# 三国志第二版交付说明

2026年10月9日。已完成确认的事件线升级与本地交付。

- 38个事件，18个关键节点，184年黄巾起义至280年吴亡。
- 桌面三线并行/时间列表，手机单列；曹氏→曹魏→西晋、刘备→蜀汉、孙氏→孙吴。
- 关键/全部、势力、事件类型及简繁搜索可组合；状态保存在网址中，返回可恢复。
- 43条附解释与原文依据的事件关系；34人物与事件双向关联；未设卡人物为纯文字。
- 65卷全文与附表、正文/裴注、出处定位、版本来源和许可保留。

预览首页：http://127.0.0.1:4323/
事件线：http://127.0.0.1:4323/events/
全事件：http://127.0.0.1:4323/events/?importance=all

## 保存位置

源码、文档和构建文件：`/Users/zhangliang/ai/readbook/tmp/sanguozhi-timeline/`。
静态站点：`/Users/zhangliang/ai/readbook/tmp/sanguozhi-timeline/dist/`。
Git分支：`feat/sanguozhi-timeline-v2`。
原版保留：`/Users/zhangliang/ai/readbook/tmp/sanguozhi-web/`。

本地服务关闭后重启：

```bash
cd /Users/zhangliang/ai/readbook/tmp/sanguozhi-timeline
npm run preview -- --port 4323
```

修改内容后：`python3 scripts/create_cards.py`，再 `npm run build`。

## 验收

6个Python、15个Node测试通过；构建144页面（含404）；143正常页面、4918内部链接和锚点通过；1310处引用有效。1440/390/320宽度及桌面/手机实际截图检查通过。完整记录见docs/validation-v2.md，启动与增补说明见README.md，内容核对见docs/event-v2-review.md和docs/person-v2-review.md。

公开托管、域名配置继续按原计划留作后续安排。
