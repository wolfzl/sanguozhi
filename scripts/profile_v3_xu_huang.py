"""徐晃：以卷十七《徐晃传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v017-b0020', '徐晃字公明，河東楊人也。')
YANG_FENG = Q('v017-b0020', '爲郡吏，從車騎將軍楊奉討賊有功，拜騎都尉。')
RETURN = Q('v017-b0020', '晃説奉，令與天子還洛陽，奉從其計。')
JOIN = Q('v017-b0020', '太祖討奉於梁，晃遂歸太祖。')
GUANDU = Q('v017-b0021', '又與史渙擊袁紹運車於故市，功最多，封都亭侯。')
YIYANG = Q('v017-b0021', '晃至，飛矢城中，爲陳成敗。範悔，晃輒降之。')
PERSUADE = Q('v017-b0021', '今日滅易陽，明日皆以死守，恐河北無定時也。')
JIANG_LING = Q('v047-b0009', '曹公遂北還，留曹仁、徐晃於江陵，使樂進守襄陽。')
ZHOU_YU = Q('v017-b0021', '與曹仁擊周瑜於江陵。')
PU_BAN = Q('v001-b0077', '公急持之，而潛遣徐晃、朱靈等夜渡蒲阪津，據河西爲營。')
KEEP_CROSSING = Q('v017-b0021', '晃擊走之，太祖軍得渡。')
WAIT = Q('v017-b0022', '晃所將多新卒，以羽難與爭鋒，遂前至陽陵陂屯。')
FAN = Q('v017-b0022', '晃揚聲當攻圍頭屯，而密攻四冢。')
RELIEF = Q('v009-b0019', '徐晃救至，水亦稍减，晃從外擊羽，仁得溃圍出，羽退走。')
PRAISE = Q('v017-b0022', '而晃軍營整齊，將士駐陳不動。太祖嘆曰：「徐將軍可謂有周亞夫之風矣。」')
RIGHT_GENERAL = Q('v017-b0023', '文帝即王位，以晃爲右將軍，進封逯鄕侯。')
LEFT_GENERAL = Q('v004-b0010', '左將軍徐晃')
DEATH = Q('v017-b0024', '太和元年薨，諡曰壯侯。')
SECOND_JIANGLING = Q('v047-b0023', '曹眞、夏侯尚、張郃、徐晃圍南郡。')
WITHDRAWAL = Q('v047-b0026', '是月，魏軍皆退。')

PROFILE = dict(
    id='xu-huang',
    tier='C',
    reading=['017'],
    new=dict(name='徐晃', courtesy='公明', faction='曹魏', period='汉末—227年',
             tags=['官渡', '潼关', '樊城']),
    eventRoles=[('guandu', '截击袁绍运粮车'), ('nanjun-campaign', '留守江陵抵御周瑜'),
                ('tongguan', '渡蒲阪津据河西扎营'), ('jingzhou', '援曹仁解樊城之围')],
    lead='徐晃早年随杨奉，后归曹操。官渡截击袁绍粮车，潼关先渡黄河为大军开路，樊城之战又从外击退关羽、解曹仁之围。曹丕继为魏王后任他为右将军，227年去世。',
    role='曹魏右将军',

    facts=[
        dict(key='lifespan', label='生卒年', value='生年未详—227年',
             text='本传未记生年，记他在魏明帝太和元年（227）去世。',
             refs=[DEATH]),
        dict(key='hometown', label='籍贯', value='河东郡杨县',
             text='本传开篇记徐晃是河东杨人，字公明。',
             refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='由杨奉部下转入曹营的将领',
             text='原为郡吏，在杨奉手下拜骑都尉；曹操在梁地讨杨奉时，徐晃转归曹操。',
             refs=[YANG_FENG, JOIN]),
        dict(key='office', label='最高官职', value='右将军（本传）',
             text='曹丕继为魏王时拜右将军，后来叙及其封爵和驻防，本传没有再记升任将军职。卷四配享诏则称“左将军徐晃”。',
             refs=[RIGHT_GENERAL, Q('v017-b0023', '以晃鎮陽平，徙封陽平侯。明帝即位，拒吳將諸葛瑾於襄陽。'), LEFT_GENERAL]),
        dict(key='posthumous', label='身后称号', value='壮侯；243年配享太祖庙庭',
             text='本传记谥壮侯。魏齐王曹芳正始四年，徐晃列入配享曹操庙庭的名单。',
             refs=[DEATH, LEFT_GENERAL, Q('v004-b0010', '武猛校尉典韋於太祖廟庭。')]),
        dict(key='deeds', label='代表事迹', items=['官渡截粮', '先渡蒲阪', '樊城解围'],
             text='与史涣袭击袁绍粮车；领兵先渡蒲阪津；击退关羽军，为曹仁解围。',
             refs=[GUANDU, PU_BAN, RELIEF]),
    ],

    intro=[
        dict(title='从杨奉转入曹营',
             text='徐晃字公明，河东杨人，原为郡吏，随杨奉讨贼立功后拜骑都尉。李傕、郭汜在长安作乱时，他劝杨奉与汉献帝返回洛阳，杨奉听从。抵洛阳后，他再劝杨奉归附曹操，杨奉改了主意；曹操讨杨奉时，徐晃自己转归曹操。后来他在官渡战事中与史涣袭击袁绍的运粮车，本传称其功最多。争河北时，易阳令韩范原先诈降拒守，徐晃说降韩范，又劝曹操接受投降，以免未下各城闻讯死守。到曹操赤壁败退后，徐晃又随曹仁留守江陵，同周瑜作战。',
             refs=[ORIGIN, YANG_FENG, RETURN, Q('v017-b0020', '晃説奉令歸太祖；奉欲從之，後悔。'), JOIN, GUANDU,
                   Q('v017-b0021', '易陽令韓範僞以城降而拒守'), YIYANG, PERSUADE, JIANG_LING, ZHOU_YU],
             eventLinks=[dict(label='官渡战事', eventId='guandu'), dict(label='留守江陵', eventId='nanjun-campaign')]),
        dict(title='潼关先渡，樊城解围',
             text='潼关之战中，徐晃看到对方没有另派兵力守蒲阪，建议领兵先渡黄河，随后击退梁兴来军，曹操大军得以渡河。219年关羽围樊城，徐晃领兵驰援，因部下多是新卒，先停军等援。兵力集结后，他扬言进攻围头，却主攻四冢，击退出战的关羽，追入围阵，曹仁随即解围。徐晃归营后，曹操巡看各营，见徐晃部列阵不动，称他有西汉周亚夫之风。',
             refs=[Q('v017-b0021', '而賊不復別守蒲阪，知其無謀也。'), PU_BAN, KEEP_CROSSING,
                   Q('v017-b0022', '復遣晃助曹仁討關羽'), WAIT, Q('v017-b0022', '須兵馬集至，乃俱前。'),
                   FAN, Q('v017-b0022', '晃擊之，退走，遂追陷與俱入圍，破之'), RELIEF, PRAISE],
             eventLinks=[dict(label='潼关之战', eventId='tongguan'), dict(label='关羽围樊城', eventId='jingzhou')]),
    ],

    careers=[
        dict(id='guandu', when='200年', title='袭击袁绍运粮车', office='偏将军，封都亭侯', eventIds=['guandu'],
             text='随军参加白马、延津两处战事，随后与史涣在故市袭击袁绍的粮车。',
             refs=[Q('v001-b0047', '公還軍官渡。紹進保陽武。'), Q('v017-b0021', '又從破顔良，拔白馬，進至延津，破文醜，拜偏將軍。'), GUANDU]),
        dict(id='yiyang', when='204年', title='招降易阳，劝以降城示诸城', office='—',
             text='韩范拒守后被徐晃说服。徐晃向曹操建议接受易阳投降，以此影响其他未归附城邑的选择。',
             refs=[YIYANG, PERSUADE, Q('v017-b0021', '原公降易陽以示諸城，則莫不望風。」太祖善之。'),
                   Q('v001-b0060', '易陽令韓範、涉長梁岐舉縣降，賜爵關內侯。')]),
        dict(id='jiangling', when='208—209年', title='与曹仁留守江陵', office='—', eventIds=['nanjun-campaign'],
             text='曹操从赤壁战场北退，把徐晃与曹仁留在江陵；本传记徐晃与曹仁在江陵对抗周瑜。',
             refs=[JIANG_LING, ZHOU_YU]),
        dict(id='tongguan', when='211年', title='先渡蒲阪津，为大军开路', office='—', eventIds=['tongguan'],
             text='建议抢先渡河；到河西立营未稳，梁兴率部夜攻，徐晃击退来军，曹操大军随后得渡。',
             refs=[Q('v001-b0076', '十六年春正月'), PU_BAN, Q('v017-b0021', '作塹柵未成，賊梁興夜將步騎五千餘人攻晃'), KEEP_CROSSING]),
        dict(id='fancheng', when='219年', title='击退关羽，樊城解围', office='—', eventIds=['jingzhou'],
             text='先屯阳陵陂等待增援；逼退偃城守军后继续推进，进打四冢，击退关羽并破围。',
             refs=[Q('v036-b0006', '是歲，羽率眾攻曹仁於樊。'), WAIT, Q('v017-b0022', '賊燒屯走。晃得偃城'),
                   FAN, Q('v017-b0022', '遂追陷與俱入圍，破之'), RELIEF]),
        dict(id='late', when='220—227年', title='拜右将军，继续镇守前线', office='右将军；后封阳平侯',
             text='曹丕继为魏王后拜右将军，后镇阳平。又随曹真等围南郡，未能取得江陵，魏军撤退。太和元年去世。',
             refs=[RIGHT_GENERAL, Q('v017-b0023', '以晃鎮陽平，徙封陽平侯。'), SECOND_JIANGLING, WITHDRAWAL, DEATH]),
    ],

    records=[
        dict(section='civil', when='204年', title='建议容纳易阳投降', category='降附处置', careerRef='yiyang',
             text='徐晃关心易阳的处置会给周边城邑怎样的预期：若降城仍遭摧毁，其他守军更会决意死守。曹操认可这一建议。',
             refs=[PERSUADE, Q('v017-b0021', '原公降易陽以示諸城，則莫不望風。」太祖善之。')]),
        dict(section='military', when='211年', title='蒲阪渡河，奠定河西立足点', category='先渡开路', careerRef='tongguan', eventIds=['tongguan'],
             text='徐晃在蒲阪先行渡河并击退梁兴，本传明确把曹操大军得渡同这一行动联系起来。',
             refs=[PU_BAN, KEEP_CROSSING]),
        dict(section='military', when='219年', title='等待援军后打破樊城围阵', category='外围解围', careerRef='fancheng', eventIds=['jingzhou'],
             text='所部新卒多，徐晃先待增援；得兵后改变攻击方向，逼关羽出战，随后攻破围阵。',
             refs=[WAIT, Q('v017-b0022', '太祖前後遣殷署、朱蓋等凡十二營詣晃。'), FAN, RELIEF]),
        dict(section='setback', when='222—223年', title='围南郡未能夺城', category='攻城未果', careerRef='late',
             text='《吴主传》记徐晃随曹真等人围南郡，次年魏军撤退。这是曹魏攻吴的后一次江陵战事；徐晃本传未记他在这次围城中的具体行动。',
             refs=[SECOND_JIANGLING, Q('v047-b0026', '二年春正月，曹眞分軍據江陵中州。'), WITHDRAWAL]),
    ],

    relations=[
        dict(category='旧主', name='杨奉', label='旧主与归曹分歧',
             text='徐晃在杨奉麾下立功任骑都尉，又曾两次进言。杨奉接受还洛阳的意见，却没有依第二次建议归曹。',
             refs=[YANG_FENG, RETURN, Q('v017-b0020', '晃説奉令歸太祖；奉欲從之，後悔。')]),
        dict(category='君臣', name='曹操', personId='caocao', label='任用与赞其军纪',
             text='徐晃归附后得到曹操授兵；樊城解围后，曹操巡营见其部下列阵不动，以周亚夫相许。',
             refs=[JOIN, Q('v017-b0021', '太祖授晃兵，使擊卷原武賊'), PRAISE]),
        dict(category='同僚', name='曹仁', personId='cao-ren', label='江陵同守，樊城增援',
             text='二人曾一起留守江陵；关羽围樊时，徐晃从外围解了曹仁的困局。',
             refs=[JIANG_LING, ZHOU_YU, RELIEF]),
        dict(category='敌对', name='关羽', personId='guanyu', label='樊城交锋',
             text='徐晃进打四冢，关羽亲自率部出战，被击退；两人的本传都提到樊城解围。',
             refs=[FAN, Q('v017-b0022', '羽見四冢欲壞，自將步騎五千出戰，晃擊之，退走'), Q('v036-b0006', '曹公遣徐晃救曹仁，羽不能克，引軍退還。')]),
    ],

    assessment=[
        dict(title='陈寿：列为曹操麾下五位良将',
             text='陈寿把徐晃列入帮助曹操建立武功的五位良将，并认为徐晃、张辽的本传事迹记载较为详备。',
             refs=[Q('v017-b0028', '太祖建茲武功，而時之良將，五子爲先。'), Q('v017-b0028', '未如張遼、徐晃之備詳也。')]),
    ],

    readingNotes=[
        dict(title='徐晃的官职有左右两种记法',
             text='《徐晃传》明确记曹丕拜他为右将军；《齐王纪》配享诏称“左将军徐晃”。本页据本传写曹丕任命的官职，保留配享诏的异文，现有记载不能确定称号差异的原因。',
             refs=[RIGHT_GENERAL, LEFT_GENERAL]),
    ],

    sourceScope='以卷十七《徐晃传》为基础，参看卷一《武帝纪》、卷九《曹仁传》、卷三十六《关羽传》及卷四十七《吴主传》，并列卷四配享诏的官号异文。本页不声称穷尽全书所有提及徐晃之处。',
)
