# 人物内容独立任务
只编辑 scripts/person_content.py 和 docs/reviews/person-v2-review.md。不改 cards.json/create_cards.py 或其他代码，不提交，勿启动子代理。
实现 expand_people(base,R) 返回原12+新增22=34人。参照 scripts/create_cards.py 数据结构，R(blockId,quote=None,work=None) 返回已核对引句ref。
新22 id/name：zhang-jiao张角,dong-zhuo董卓,sun-jian孙坚,sun-ce孙策,cao-pi曹丕,cao-rui曹叡,liu-shan刘禅,cao-shuang曹爽,cao-mao曹髦,sima-yi司马懿,sima-shi司马师,sima-zhao司马昭,sima-yan司马炎,jiang-wan蒋琬,fei-yi费祎,jiang-wei姜维,deng-ai邓艾,zhong-hui钟会,sun-hao孙皓,wang-jun王濬,du-yu杜预,zhang-liao张辽。
人物300—500字（paragraphs合计），3—5人生节点；至少一个人物关系，refs真实准确支持事实，引用裴注注明书名。reading卷id真实。eventIds可先[]主代理自动从事件participants构建。没有本书完整传记的张角/司马氏/王濬/杜预卡应以本书散见角色材料描述，不虚构完整生平，note说明范围。生卒/字号本书不足则用“本书未详”/时段，不靠外部未引材料硬填。诸葛亮已知姜维与蒋琬继承；孙权补222吴王/229称帝/252继承，刘备明确221称帝，曹操不称自己建立曹魏；关羽吕蒙陆逊鲁肃补事件网络相关经历（事件Ids自动）。必要新增关系回链但不要为了完全对称编造。
势力可汉末、曹魏、蜀汉、孙吴、西晋、袁氏；孙坚孙策用孙吴作为主要势力索引但说明早期孙氏；司马懿师昭用曹魏、司马炎王濬杜预用西晋。保留别名/简繁搜索，王濬别名王浚，曹叡别名曹睿；司马人物谥号若只有称谓出现要准确。
本书 book.json blocks fields mainText/notes，用Python检索后精确核对。write review文档逐人原文证据和限制。不要只输出模板重复式读法，需要每个人具体行动、处境和结果。
