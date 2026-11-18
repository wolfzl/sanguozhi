"""张绣：从宛城反曹到官渡立功。"""
from profile_v3 import Q

ORIGIN = Q('v008-b0044', '張繡，武威祖厲人，驃騎將軍濟族子也。')
EARLY = Q('v008-b0044', '繡為縣吏，間伺殺勝，郡內義之。遂招合少年，為邑中豪傑。')
FIRST_OFFICE = Q('v008-b0044', '繡隨濟，以軍功稍遷至建忠將軍，封宣威侯。')
INHERIT = Q('v008-b0044', '濟屯弘農，士卒飢餓，南攻穰，為流矢所中死。繡領其眾，屯宛，與劉表合。')
WAN = Q('v001-b0035', '二年春正月，公到宛。張繡降，旣而悔之，復反。公與戰，軍敗，爲流矢所中，長子昂、弟子安民遇害。')
MOTIVE = Q('v008-b0044', '太祖納濟妻，繡恨之。太祖聞其不悅，密有殺繡之計。計漏，繡掩襲太祖。')
ANZHONG = Q('v001-b0038', '到安衆，繡與表兵合守險，公軍前後受敵。')
ANZHONG_LOSS = Q('v001-b0038', '會明，賊謂公爲遁也，悉軍來追。乃縱奇兵步騎夾攻，大破之。')
RELIEF = Q('v001-b0038', '三月，公圍張繡於穰。夏五月，劉表遣兵救繡')
JOIN = Q('v010-b0044', '紹遣人招繡，并與詡書結援。')
JOIN_REASON = Q('v010-b0044', '紹彊盛，我以少衆從之，必不以我爲重。曹公衆弱，其得我必喜，其宜從二也。')
REJOIN = Q('v008-b0045', '繡從賈詡計，復以眾降。')
REJOIN_DATE = Q('v001-b0043', '冬十一月，張繡率衆降，封列侯。')
MARRIAGE = Q('v008-b0045', '繡至，太祖執其手，與歡宴，為子均取繡女，拜揚武將軍。')
GUANDU = Q('v008-b0045', '官渡之役，繡力戰有功，遷破羌將軍。')
NANPI = Q('v008-b0045', '從破袁譚於南皮，復增邑凡二千戶。')
END = Q('v008-b0045', '從征烏丸於柳城，未至，薨，諡曰定侯。')
EXPEDITION_YEAR = Q('v008-b0025', '十二年，太祖征三郡烏丸，屠柳城。')
FUZI = Q('v008-b0044-n01', '太祖愛其驍健，手以金與之。繡聞而疑太祖欲因左右刺之，遂反。', '《傅子》')
DEATH_VARIANT = Q('v008-b0045-n01', '君殺吾兄，何忍持面視人邪！」繡心不自安，乃自殺。', '《魏略》')

PROFILE = dict(
    id='zhang-xiu',
    tier='C',
    reading=['008', '001', '010'],
    lead='汉末据宛城的军事首领。接领张济旧部后与刘表结援，先降曹操又突袭曹军，后听从贾诩劝说再次归曹，在官渡力战受赏，最终死于随曹操北征乌桓期间。',
    role='宛城军事首领、曹军将领',

    facts=[
        dict(key='hometown', label='籍贯', value='武威祖厉',
             text='张绣本传记他是武威郡祖厉人、张济的族子。', refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='宛城军事首领、曹军将领',
             text='张济死后，他继领其众，与刘表结援；再次投降曹操后转为曹军将领。', refs=[INHERIT, REJOIN, MARRIAGE]),
        dict(key='office', label='最高官职', value='破羌将军',
             text='随张济时任建忠将军，再次归曹后拜扬武将军，官渡战后迁破羌将军。', refs=[FIRST_OFFICE, MARRIAGE, GUANDU]),
        dict(key='title', label='最高爵位', value='宣威侯',
             text='本书明确写出封号的是宣威侯。再次归曹时《武帝纪》只写封列侯；后来从破南皮，封邑共二千户。',
             refs=[FIRST_OFFICE, REJOIN_DATE, NANPI]),
        dict(key='posthumous', label='身后称号', value='定侯',
             text='本传记他从征途中去世，谥为定侯。', refs=[END]),
        dict(key='lifespan', label='生卒年', value='生年不详—207年',
             text='生年本书未详。卒年按本传所记的柳城之役与卷八《公孙度传》所载的建安十二年相核。', refs=[END, EXPEDITION_YEAR]),
        dict(key='deeds', label='代表事迹', items=['接领张济部众', '宛城突袭曹军', '官渡力战有功'],
             text='先在宛城一带自立，后来作为曹军将领参与官渡之战。', refs=[INHERIT, WAN, GUANDU]),
    ],

    intro=[
        dict(title='从县吏到宛城领兵',
             text='张绣早年在家乡做县吏。祖厉县长刘隽被麴胜杀害后，他伺机杀了麴胜，郡里人以此为义。他随后招聚当地青年，并随族中长辈张济征战，以军功封侯。张济攻穰城时中箭身亡，张绣接领旧部，屯兵宛城，与刘表结援。197年曹操南征，张绣率众投降，随后又在宛城突袭曹军。曹操中箭，长子曹昂与侄儿曹安民遇害；张绣退保穰城，次年与刘表的援兵合兵，在安众又败于曹操。',
             refs=[Q('v008-b0044', '金城麴勝襲殺祖厲長劉雋。'), EARLY, FIRST_OFFICE, INHERIT, WAN,
                   Q('v001-b0035', '繡奔穰，與劉表合。'), ANZHONG, ANZHONG_LOSS],
             eventLinks=[dict(label='宛城突袭曹军', eventId='wancheng')]),
        dict(title='再归曹操，官渡立功',
             text='袁绍遣使招揽时，张绣原想应允。贾诩却判断，袁绍兵强，未必看重张绣的兵力；曹操相对势弱，更需要张绣来投。张绣采纳建议，于199年再度归曹。曹操握手设宴，还让儿子曹均娶了张绣的女儿。次年官渡之战，张绣力战有功，升为破羌将军；后来随军击败袁谭，封邑增至二千户。本传写他在北征乌桓途中去世，未抵柳城；关于死因，裴注另录了一种说法。',
             refs=[JOIN, Q('v010-b0044', '繡欲許之'), JOIN_REASON, REJOIN,
                   REJOIN_DATE, MARRIAGE, GUANDU, NANPI, END, DEATH_VARIANT],
             eventLinks=[dict(label='官渡之战', eventId='guandu')]),
    ],

    careers=[
        dict(id='inherit', when='早年，确年未载', title='随张济征战，继领旧部', office='建忠将军、宣威侯',
             text='早年任县吏，后随张济征战，因军功升迁受封。张济身亡后接领其众，屯宛并与刘表结援。',
             refs=[EARLY, FIRST_OFFICE, INHERIT]),
        dict(id='wancheng', when='197年', title='宛城先降后战', office='—', eventIds=['wancheng'],
             text='率众降曹。本传说曹操纳张济之妻，又密谋杀他；消息走漏，张绣突袭曹军，曹操败退并受伤。',
             refs=[WAN, MOTIVE]),
        dict(id='anzhong', when='198年', title='合兵追击，败于安众', office='—',
             text='曹操围穰，刘表出兵来救。张绣与刘表军在安众合兵据险，追击时被曹军伏兵夹击而败。',
             refs=[Q('v001-b0038', '三年春正月'), RELIEF, ANZHONG, ANZHONG_LOSS]),
        dict(id='rejoin', when='199年', title='听贾诩劝说再次归曹', office='扬武将军、封列侯（封号未载）',
             text='面对袁绍招揽，他听从贾诩劝说，十一月率部再降曹操。曹操让儿子曹均娶其女。',
             refs=[JOIN, REJOIN, Q('v001-b0041', '四年春二月'), REJOIN_DATE, MARRIAGE]),
        dict(id='guandu', when='200年', title='官渡力战受赏', office='破羌将军', eventIds=['guandu'],
             text='随曹军在官渡力战，因战功升迁，后来又从军攻破袁谭。',
             refs=[GUANDU, NANPI]),
        dict(id='death', when='207年', title='北征乌桓途中去世', office='谥定侯',
             text='随曹操北征乌桓，未到柳城便去世；本传未说明死因。',
             refs=[END, EXPEDITION_YEAR]),
    ],

    records=[
        dict(section='military', when='197年', title='宛城突袭迫曹退兵', category='突袭', careerRef='wancheng', eventIds=['wancheng'],
             text='两军由受降转为交战，曹操受伤退兵，曹昂、曹安民遇害。张绣继续与刘表合作，未被曹操就此消灭。',
             refs=[WAN, Q('v008-b0044', '繡還保穰，太祖比年攻之，不克。')]),
        dict(section='military', when='200年', title='官渡以战功升迁', category='随军作战', careerRef='guandu', eventIds=['guandu'],
             text='本传明确把官渡力战与升任破羌将军相连，未记他在战中的具体任务。',
             refs=[GUANDU]),
        dict(section='setback', when='198年', title='安众追击受挫', category='追击失利', careerRef='anzhong',
             text='与刘表军合守险地时一度让曹军腹背受敌；误判曹军退走，追击后反遭伏兵夹攻。',
             refs=[ANZHONG, ANZHONG_LOSS]),
    ],
    sections={
        'civil': {'note': '本传只简记张绣早年任祖厉县吏，随后多记领兵、结援与军功，未见他在宛城或归曹后施行的地方治理措施。'},
    },

    relations=[
        dict(category='亲族', name='张济', label='从其征战，承领旧部',
             text='张绣是张济族子，随他以军功受封；张济死后接领其部众。',
             refs=[ORIGIN, FIRST_OFFICE, INHERIT]),
        dict(category='邻境', name='刘表', personId='liu-biao', label='南阳结援，共御曹军',
             text='张绣屯宛后与刘表结援；曹操围穰时，刘表派兵相救。',
             refs=[INHERIT, RELIEF]),
        dict(category='部属', name='贾诩', personId='jia-xu', label='礼为谋主，听其劝降',
             text='张绣请贾诩前来，以子孙之礼相待；贾诩在袁绍来招时劝他转归曹操。',
             refs=[Q('v010-b0044', '詡遂往，繡執子孫禮'), JOIN, REJOIN]),
        dict(category='君臣', name='曹操', personId='caocao', label='先降后战，再归并结亲',
             text='宛城受降之后双方反目；张绣再次归降后，曹操释怨任用，又让曹均娶其女。',
             refs=[WAN, REJOIN, MARRIAGE]),
    ],

    assessment=[
        dict(title='陈寿：转为功臣，免于危亡',
             text='陈寿在篇末把张绣与张燕、张鲁并论，认为三人归曹后得以列在功臣之中，处境胜过其他覆亡者。这是对他们选择归附的评价。',
             refs=[Q('v008-b0057', '燕、繡、魯舍群盜，列功臣，去危亡，保宗祀，則於彼為愈焉。')]),
    ],
    readingNotes=[
        dict(title='宛城反目的缘由',
             text='本传说曹操纳张济之妻，张绣因此怨恨，曹操密谋杀他的消息又走漏。裴注引《傅子》却说曹操赏金给张绣的亲信胡车儿，张绣怀疑他想借左右之手刺杀自己。两种记载的侧重点不同。',
             refs=[MOTIVE, Q('v008-b0044-n01', '繡有所親胡車兒，勇冠其軍。', '《傅子》'), FUZI]),
        dict(title='去世经过与死因异说',
             text='本传记张绣在207年北征途中去世，未交代死因。裴注引《魏略》说曹丕以兄长之死责问张绣，张绣因此不安而自杀，但称曹丕为“五官将”。据《文帝纪》，曹丕到211年才任五官中郎将。这里可能用了后来的官称，单凭这条注文无法确定死因。',
             refs=[END, EXPEDITION_YEAR, Q('v008-b0045-n01', '五官將數因請會，發怒曰', '《魏略》'),
                   DEATH_VARIANT, Q('v002-b0001', '建安十六年，爲五官中郎將、副丞相。')]),
    ],

    sourceScope='以卷八《张绣传》正文、裴注及篇末评语为主，参照同卷《公孙度传》及卷一《武帝纪》、卷二《文帝纪》、卷十《贾诩传》；宛城反目原因和死因异说列入辨析。本页不声称穷尽全书所有提及张绣之处。',
)
