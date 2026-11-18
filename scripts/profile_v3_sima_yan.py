"""司马炎：用魏、吴末年纪事与有关裴注写成的 v3 C 级人物卡。"""
from profile_v3 import Q

WELCOME = Q('v004-b0062', '使使持節行中護軍中壘將軍司馬炎北迎常道鄉公璜嗣明帝後。')
CAO_HUAN = Q('v004-b0067', '高貴鄉公卒，公卿議迎立公。')
DEPUTY = Q('v004-b0078', '命中撫軍司馬炎副貳相國事')
PROMOTION = Q('v004-b0080', '九月戊午，以中撫軍司馬炎為撫軍大將軍。')
HEIR = Q('v004-b0083', '命撫軍大將軍新昌鄉侯炎為晉世子。')
SUCCESSION = Q('v004-b0085', '秋八月辛卯，相國晉王薨。壬辰，晉太子炎紹封襲位，總攝百揆，備物典冊，一皆如前。')
ABDICATION = Q('v004-b0086', '使使者奉皇帝璽綬冊，禪位于晉嗣王，如漢魏故事。')
TITLE = Q('v009-b0057-n01', '晉武帝太始元年詔曰', '《汉晋春秋》')
FAMILY = Q('v013-b0032-n01', '肅女適司馬文王，即文明皇后，生晉武帝、齊獻王攸。', '《世语》')
CAMPAIGN = Q('v048-b0042', '鎮南將軍杜預向江陵，龍驤將軍王濬、廣武將軍唐彬浮江東下，太尉賈充爲大都督')
SURRENDER = Q('v048-b0047', '壬申，王濬最先到，於是受皓之降')
RELOCATE = Q('v048-b0047', '皓舉家西遷，以太康元年五月丁亥集于京邑。')
INVESTITURE = Q('v048-b0047', '前詔待之以不死，今皓垂至，意猶愍之，其賜號爲歸命侯。')
GRANTS = Q('v048-b0047', '田三十頃，歲給穀五千斛，錢五十萬，絹五百匹')
PRINCE_QI = Q('v005-b0017-n01', '太康中，大司馬齊王攸當之籓，德與左衛將軍王濟共諫請，時人嘉之。', '《晋诸公赞》')
DISMISSAL = Q('v019-b0031-n01', '乃建議以諫，辭旨甚切。帝大怒，免志官。後復為散騎常侍。', '《志别传》')

PROFILE = dict(
    id='sima-yan',
    tier='C',
    reading=['004', '048', '019', '005'],
    syncLifespan=True,
    lead='司马炎是西晋的开国皇帝。260年曹髦死后，他奉命北迎曹奂继位；265年承袭父亲司马昭的晋王位，继而受魏禅建晋。279年晋军分路攻吴，次年孙皓投降，三国分立结束。',
    role='西晋开国皇帝',

    facts=[
        dict(key='lifespan', label='生卒年', value='本书未详',
             text='本书未详其出生和去世的年月。卷四记他于260年奉命迎立曹奂，卷四十八记太康元年（280）晋廷处置孙皓归降。',
             refs=[WELCOME, RELOCATE]),
        dict(key='hometown', label='籍贯', value='本书未详',
             text='本书没有司马炎本纪；卷四记其姓名和仕履，卷十三裴注引《世语》记其父母，均未记他的籍贯。',
             refs=[WELCOME, FAMILY]),
        dict(key='identity', label='主要身份', value='西晋开国皇帝',
             text='司马昭之子，先承袭晋王位，后接受曹奂禅位，建立西晋。',
             refs=[FAMILY, SUCCESSION, ABDICATION]),
        dict(key='office', label='最高官职', value='皇帝（西晋帝位）',
             text='在魏先任中垒将军、行中护军，后来由中抚军迁抚军大将军；承袭晋王后受禅，登为皇帝。',
             refs=[WELCOME, PROMOTION, SUCCESSION, ABDICATION]),
        dict(key='title', label='最高爵位', value='晋王（即帝位前）',
             text='任抚军大将军时为新昌乡侯，后立为晋世子；司马昭死后承袭晋王。',
             refs=[HEIR, SUCCESSION]),
        dict(key='posthumous', label='身后称号', value='晋武帝（追谥年月未详）',
             text='裴注引《汉晋春秋》称“晋武帝”，本书未详追谥的年月和过程。',
             refs=[TITLE]),
        dict(key='deeds', label='代表事迹', items=['奉迎曹奂', '受禅建晋', '分路伐吴'],
             text='奉迎曹奂入继，接受魏禅建立西晋，命晋军分路伐吴。',
             refs=[WELCOME, ABDICATION, CAMPAIGN]),
    ],

    intro=[
        dict(title='从奉迎魏帝到受禅',
             text='260年曹髦遇害后，魏廷议迎常道乡公入继，司马炎奉命持节北迎，来者就是后来的魏帝曹奂。四年后，他以中抚军身份协理相国事务，随后升抚军大将军，被立为晋世子。265年司马昭去世，司马炎嗣晋王位，总摄朝政，沿用父亲的礼仪和典册。当年十二月，魏廷命群臣在南郊设坛，由使者奉送皇帝玺绶和册书，司马炎接受魏禅，建立西晋。继承晋王在八月，接受帝位在十二月，这是先后两件事。',
             refs=[CAO_HUAN, WELCOME, DEPUTY, PROMOTION, HEIR, SUCCESSION, Q('v004-b0086', '十二月壬戌'),
                   Q('v004-b0086', '詔羣公卿士具儀設壇于南郊'), ABDICATION],
             eventLinks=[dict(label='司马炎奉命持节北迎', eventId='cao-mao-death'), dict(label='司马炎接受魏禅', eventId='jin-founding')]),
        dict(title='分路伐吴与安置降主',
             text='西晋建立时，孙吴仍立国于江东。279年冬，西晋分路伐吴：贾充为大都督，杜预进攻江陵，王濬、唐彬率军沿江东下，其他晋军也从各自方向推进。次年，吴军防线相继失守，孙皓分别遣使向逼近的晋将请降，王濬最先抵达并受降。晋廷依先前留其性命的承诺，封孙皓为归命侯，给田地、谷帛；孙皓一家迁往晋都。到此，魏、蜀、吴三国分立的局面结束。',
             refs=[Q('v048-b0026', '十二月，晉受禪。'), Q('v048-b0042', '冬，晉命'), CAMPAIGN,
                   Q('v048-b0044', '預又斬江陵督伍延，渾復斬丞相張悌、丹楊太守沈瑩等，所在戰克。'),
                   Q('v048-b0046', '分遣使奉書於濬、伷、渾'), SURRENDER, INVESTITURE,
                   GRANTS, RELOCATE],
             eventLinks=[dict(label='西晋分路伐吴', eventId='jin-conquest-wu'), dict(label='孙皓分别遣使', eventId='fall-wu')]),
    ],

    careers=[
        dict(id='welcome-cao-huan', when='260年', title='曹髦死后奉迎曹奂', office='中垒将军、行中护军（奉命持节）',
             text='曹髦死后，魏廷遣司马炎迎常道乡公入继，曹奂于当年六月即位。',
             refs=[WELCOME, CAO_HUAN, Q('v004-b0067', '六月甲寅，入于洛陽，見皇太后，是日即皇帝位於太極前殿')],
             eventIds=['cao-mao-death']),
        dict(id='jin-heir', when='264年', title='协理相国事务，立为晋世子', office='中抚军，后为抚军大将军、新昌乡侯、晋世子',
             text='以中抚军身份协理相国事务，九月迁抚军大将军，当年被立为晋世子。',
             refs=[DEPUTY, PROMOTION, HEIR]),
        dict(id='found-jin', when='265年', title='嗣晋王，受禅建晋', office='晋王，后即帝位',
             text='八月司马昭死后，司马炎嗣晋王位并总摄百官，礼仪和典册沿用旧制；十二月魏帝命使者奉玺绶、册书禅位。',
             refs=[SUCCESSION, ABDICATION, Q('v048-b0026', '十二月，晉受禪。')], eventIds=['jin-founding']),
        dict(id='attack-wu', when='279年', title='命晋军分路伐吴', office='—',
             text='冬季晋军多路向吴进兵，贾充任大都督；杜预进攻江陵，王濬和唐彬率军沿江东下。',
             refs=[Q('v048-b0042', '冬，晉命'), CAMPAIGN], eventIds=['jin-conquest-wu']),
        dict(id='fall-wu', when='280年', title='吴亡，册封孙皓', office='—',
             text='王濬最先到达受降，孙皓一家西迁，晋廷封孙皓为归命侯。',
             refs=[SURRENDER, RELOCATE, INVESTITURE], eventIds=['fall-wu']),
        dict(id='prince-qi', when='太康年间，确年未载', title='齐王就藩引发劝谏', office='—',
             text='裴注引《晋诸公赞》记齐王司马攸将就藩，甄德、王济进谏；《志别传》另记曹志为此进谏，被司马炎免官。',
             refs=[PRINCE_QI, Q('v019-b0031-n01', '及齊王攸當之藩', '《志别传》'), DISMISSAL]),
    ],

    records=[
        dict(section='civil', when='280年', title='兑现不杀孙皓的承诺', category='安置降主', careerRef='fall-wu', eventIds=['fall-wu'],
             text='晋廷此前已诏许孙皓投降后不死，吴亡后封他为归命侯，给田地、谷帛，也授其太子和原封王的诸子官职。这些是本书明确记下的降主及家属安置措施。',
             refs=[INVESTITURE, GRANTS, Q('v048-b0047', '皓太子瑾拜中郎，諸子爲王者，拜郎中。')]),
        dict(section='military', when='279—280年', title='多路进军迫吴请降', category='统筹征吴', careerRef='attack-wu',
             eventIds=['jin-conquest-wu', 'fall-wu'],
             text='西晋同时从长江上游和下游向吴推进，各军先后取胜，迫使孙皓向多路晋军请降。司马炎是晋方君主，战场指挥和实际受降由诸将承担。',
             refs=[CAMPAIGN, Q('v048-b0044', '所在戰克。'), Q('v048-b0046', '分遣使奉書於濬、伷、渾'), SURRENDER]),
        dict(section='setback', when='太康年间，确年未载', title='齐王就藩，曹志因谏免官', category='宗室任用争议', careerRef='prince-qi',
             text='据裴注引《志别传》，曹志认为齐王司马攸既有才能又是近亲，应留朝辅政，司马炎却因其力谏而免其官，后来才复任。《晋诸公赞》也记有人联名劝谏，显示这个决定在朝中受到反对。',
             refs=[Q('v019-b0031-n01', '安有如此之才，如此之親，而不得樹本助化，而遠出海隅者乎？', '《志别传》'), DISMISSAL, PRINCE_QI]),
    ],

    relations=[
        dict(category='亲族', name='司马昭', personId='sima-zhao', label='承袭父亲的晋王位',
             text='裴注引《世语》记司马炎为司马昭与文明皇后之子；司马昭去世后，司马炎继其晋王位和总摄朝政的权力。',
             refs=[FAMILY, SUCCESSION]),
        dict(category='君臣', name='曹奂', label='先奉迎继位，后受其禅',
             text='司马炎先以魏将身份奉命迎曹奂入继，五年后以晋王身份接受魏帝禅位。',
             refs=[WELCOME, CAO_HUAN, ABDICATION]),
        dict(category='敌对', name='孙皓', personId='sun-hao', label='降晋后封归命侯',
             text='晋军攻吴，孙皓向晋将请降；吴亡后，晋廷保全孙皓性命并封为归命侯。',
             refs=[CAMPAIGN, SURRENDER, INVESTITURE]),
    ],

    readingNotes=[
        dict(title='迎立记载中的曹璜与曹奂',
             text='《三少帝纪》记司马炎所迎的是“常道乡公璜”，另载朝廷嫌其名难以避讳，下诏议改；同卷《陈留王纪》开头记他名奂。两处说的是同一个人。',
             refs=[WELCOME, Q('v004-b0065', '今常道鄉公諱字甚難避，其朝臣博議改易，列奏。'), Q('v004-b0067', '陳留王諱奐，字景明')]),
    ],

    glossary=[
        ('持节', '持有代表朝廷授命的符节。'),
        ('禅位', '用礼仪和册命把君位让给另一人。'),
        ('就藩', '受封的诸侯王离开朝廷，前往自己的封国。'),
    ],

    sourceScope='本书无司马炎的独立本纪，以卷四《三少帝纪》、卷四十八《三嗣主传》的孙皓纪事为主，参看卷五、九、十三、十九的裴注，追谥过程与确切生卒年未详。本页不声称穷尽全书所有提及司马炎之处。',
)
