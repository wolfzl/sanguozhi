"""丁奉：以卷五十五《丁奉传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v055-b0066', '丁奉字承淵，廬江安豐人也。')
EARLY = Q('v055-b0066', '少以驍勇爲小將，屬甘寧、陸遜、潘璋等。')
PROMOTION = Q('v055-b0066', '稍遷偏將軍。孫亮即位，爲冠軍將軍，封都亭侯。')
DONGXING = Q('v055-b0067', '乃辟諸軍使下道，帥麾下三千人徑進。時北風，奉舉帆二日至，遂據徐塘。')
ATTACK = Q('v055-b0067', '乃使兵解鎧著冑，持短兵。敵人從而笑焉，不爲設備。奉縱兵斫之，大破敵前屯。會據等至，魏軍遂潰。')
SHOUCHUN = Q('v055-b0069', '復使奉與黎斐解圍。奉爲先登，屯於黎漿，力戰有功，拜左將軍。')
COUP = Q('v055-b0070', '可因臘會，有陛下兵以誅之也。')
EXECUTION = Q('v055-b0070', '休納其計，因會請綝，奉與張布目左右斬之。遷大將軍，加左右都護。')
ACCESSION = Q('v055-b0071', '休薨，奉與丞相濮陽興等從萬彧之言，共迎立孫皓，遷右大司馬左軍師。')
GUYANG = Q('v055-b0071', '建衡元年，奉復帥衆治徐塘，因攻晉穀陽。穀陽民知之，引去，奉無所獲。皓怒，斬奉導軍。')
DEATH = Q('v048-b0032', '右大司馬丁奉、司空孟仁卒。')
FAMILY = Q('v055-b0071', '奉貴而有功，漸以驕矜，或有毀之者，皓追以前出軍事，徙奉家於臨川。')

PROFILE = dict(
    id='ding-feng', tier='C', reading=['055'],
    new=dict(name='丁奉', courtesy='承渊', faction='孙吴', period='孙吴—271年', aliases=['丁承渊'], tags=['东兴', '寿春', '孙皓即位']),
    eventRoles=[('dongxing-battle', '先进据徐塘，破魏前屯'), ('shouchun-siege', '赴援寿春，屯黎浆力战'),
                ('sun-hao-succession', '与濮阳兴等迎立孙皓')],
    lead='丁奉早年为吴军小将，东兴之战先据徐塘、破魏军前屯，寿春再立战功。后来他献策助孙休除掉孙綝，又参与拥立孙皓，位至右大司马；晚年攻谷阳无功，死后家人被迁往临川。',
    role='孙吴右大司马',
    facts=[
        dict(key='lifespan', label='生卒年', value='生年未详—271年', text='本传未记生年。建衡三年（271），丁奉以右大司马去世，见《孙皓传》；《丁奉传》纪年相合。', refs=[Q('v055-b0071', '三年，卒。'), DEATH]),
        dict(key='hometown', label='籍贯', value='庐江郡安丰县', text='丁奉字承渊，庐江安丰人。', refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='孙吴武将及朝廷重臣', text='年轻时在甘宁、陆逊、潘璋等人部下领兵起家，后来协助孙休除孙綝、参与拥立孙皓。', refs=[EARLY, EXECUTION, ACCESSION]),
        dict(key='office', label='最高官职', value='右大司马、左军师', text='曾拜左将军。助孙休诛孙綝后迁大将军、加左右都护，孙皓即位后任右大司马、左军师。', refs=[SHOUCHUN, EXECUTION, ACCESSION]),
        dict(key='title', label='最高爵位', value='安丰侯', text='孙亮即位时封都亭侯，东兴战后进封都乡侯，迎接文钦的战事之后进封安丰侯。', refs=[PROMOTION, Q('v055-b0067', '遷滅寇將軍，進封都鄉侯。'), Q('v055-b0068', '進封安豐侯。')]),
        dict(key='posthumous', label='身后称号', value='本书未载谥号', text='本书记其去世，后因旧日出兵之事家人被迁往临川，未记追谥。', refs=[DEATH, FAMILY]),
        dict(key='deeds', label='代表事迹', items=['东兴破敌', '寿春赴援', '献策除孙綝', '迎立孙皓'], text='东兴破魏军前屯，寿春出兵赴援，协助孙休诛孙綝，后参与迎立孙皓。', refs=[ATTACK, SHOUCHUN, EXECUTION, ACCESSION]),
    ],
    intro=[
        dict(title='东兴抢先，寿春赴援',
             text='丁奉字承渊，庐江安丰人。早年在甘宁、陆逊、潘璋等人部下领兵，孙亮即位后任冠军将军。252年东兴之战，魏军来攻，吴将有人以为对方听到诸葛恪亲自赴援就会退走，丁奉却判断魏军大举出动，必有准备。他嫌诸军行进太慢，率三千人趁北风举帆抢占徐塘，见魏军将领饮酒、前屯兵少，下令部下脱甲戴盔、持短兵冲击。魏军遭突击后溃退，丁奉升灭寇将军。后来魏军围攻寿春，丁奉奉命解围，在黎浆力战有功，拜左将军。',
             refs=[ORIGIN, EARLY, PROMOTION, Q('v055-b0067', '敵聞太傅自來，上岸必遁走。'), Q('v055-b0067', '彼動其境內，悉許、洛兵大舉而來，必有成規'), DONGXING,
                   Q('v055-b0067', '天寒雪，敵諸將置酒高會，奉見其前部兵少'), ATTACK, Q('v055-b0067', '遷滅寇將軍，進封都鄉侯。'), SHOUCHUN],
             eventLinks=[dict(label='东兴之战', eventId='dongxing-battle'), dict(label='魏军围攻寿春', eventId='shouchun-siege')]),
        dict(title='参与朝局，晚年出兵',
             text='孙休即位后想除掉把持朝政的孙綝。丁奉认为孙綝党羽众多，建议借腊日会合、由孙休调动亲兵处置；孙休采纳，他和张布示意左右诛杀孙綝，事后升大将军。孙休去世，丁奉与濮阳兴等迎立孙皓，升任右大司马。晚年他出兵攻晋据有的谷阳，民众事先离开，吴军无功，孙皓下令杀了他的向导。丁奉于271年去世，孙皓追究此前出军之事，把他家人迁往临川。',
             refs=[Q('v055-b0070', '丞相兄弟友黨甚盛，恐人心不同，不可卒制'), COUP, EXECUTION, ACCESSION, GUYANG, DEATH, FAMILY],
             eventLinks=[dict(label='迎立孙皓', eventId='sun-hao-succession')]),
    ],
    careers=[
        dict(id='early', when='252年及此前', title='从小将升至冠军将军', office='偏将军，后为冠军将军、都亭侯',
             text='早年在甘宁、陆逊、潘璋等人部下屡次从征负伤。孙亮继位后升冠军将军，封都亭侯。', refs=[EARLY, Q('v055-b0066', '每斬將搴旗，身被創夷。'), PROMOTION, Q('v048-b0003', '太子即尊號，大赦，改。是歲，於魏嘉平四年也。')]),
        dict(id='dongxing', when='252年', title='先据徐塘，突击魏军前屯', office='迁灭寇将军，进封都乡侯', eventIds=['dongxing-battle'],
             text='率三千人先据徐塘，乘隙突击魏军前屯；吕据等随后到达，魏军溃败。', refs=[DONGXING, ATTACK, Q('v055-b0067', '遷滅寇將軍，進封都鄉侯。'), Q('v048-b0004', '戊午，兵及東興，交戰，大破魏軍')]),
        dict(id='shouchun', when='257年', title='赴寿春解围，屯黎浆力战', office='拜左将军', eventIds=['shouchun-siege'],
             text='诸葛诞据寿春降吴，魏军围城。丁奉与黎斐奉命往救，先登作战，屯兵黎浆。', refs=[Q('v055-b0069', '太平二年，魏大將軍諸葛誕據壽春來降，魏人圍之。'), SHOUCHUN]),
        dict(id='sun-xiu', when='258—263年', title='献策除孙綝，后领兵援蜀', office='大将军、左右都护；后假节领徐州牧',
             text='建议孙休在腊日会合时诛孙綝，与张布共同行事。后来领徐州牧；魏伐蜀时督军向寿春，得知蜀已降魏才撤军。', refs=[COUP, EXECUTION, Q('v048-b0013', '是歲，於魏甘露三年也。'), Q('v055-b0070', '永安二年，假節領徐州牧。'), Q('v055-b0070', '六年，魏伐蜀，奉率諸軍向壽春，爲救蜀之勢。蜀亡，軍還。')]),
        dict(id='accession', when='264年', title='迎立孙皓，拜右大司马', office='右大司马、左军师', eventIds=['sun-hao-succession'],
             text='孙休去世，丁奉与濮阳兴等听从万彧建议，迎立孙皓。', refs=[ACCESSION, Q('v048-b0024', '是歲，於魏咸熙元年也。')]),
        dict(id='last', when='269—271年', title='攻谷阳无功，建衡三年卒', office='—',
             text='攻谷阳无获，孙皓处死向导。丁奉两年后去世，孙皓又因旧日出军之事把其家人迁往临川。', refs=[GUYANG, Q('v055-b0071', '三年，卒。'), DEATH, FAMILY]),
    ],
    records=[
        dict(section='civil', when='264年', title='参与决定孙休后的继承', category='参与拥立', careerRef='accession', eventIds=['sun-hao-succession'],
             text='孙休去世后，丁奉与濮阳兴等同意依万彧建议立孙皓。《孙皓传》把拥立背景归于蜀亡、交趾反叛之下朝廷希望有一位年长君主。', refs=[ACCESSION, Q('v048-b0024', '蜀初亡，而交阯攜叛，國內震懼，貪得長君。')]),
        dict(section='military', when='252年', title='东兴抢先，占据徐塘', category='先遣突击', careerRef='dongxing', eventIds=['dongxing-battle'],
             text='认为先占险要比等待大军更有利，借北风先到徐塘，趁魏军防备松懈打破前屯。', refs=[Q('v055-b0067', '若敵據便地，則難與爭鋒矣。'), DONGXING, ATTACK]),
        dict(section='setback', when='269—271年及身后', title='谷阳出兵无获，身后家人受迁', category='出征无功', careerRef='last',
             text='谷阳民众预先离开，丁奉未有斩获，孙皓怒而杀其向导。本传说他功高渐骄，死后孙皓以先前出军之事迁其家。', refs=[GUYANG, FAMILY]),
    ],
    relations=[
        dict(category='旧主', name='潘璋', personId='pan-zhang', label='早年所属将领之一', text='本传开篇记丁奉早年曾在潘璋等将领部下从征。', refs=[EARLY]),
        dict(category='君臣', name='孙休', label='献策诛孙綝', text='孙休想除掉孙綝，召丁奉商议；事成后丁奉迁大将军。', refs=[COUP, EXECUTION]),
        dict(category='君臣', name='孙皓', personId='sun-hao', label='早年拥立，晚年获责', text='丁奉参与迎立孙皓，迁右大司马。晚年攻谷阳无获，孙皓处死向导，后来又以出军事迁其家。', refs=[ACCESSION, GUYANG, FAMILY]),
    ],
    readingNotes=[
        dict(title='丁奉参与废孙皓之谋吗', text='《陆凯传》以“或曰”引述陆凯、丁奉、丁固欲废孙皓之说。《吴录》注文另记陆凯想让丁奉领兵护卫，但孙皓改用留平。两条对计划写法有别，不能据以坐实丁奉亲自参与谋划。', refs=[Q('v061-b0014', '或曰寶鼎元年十二月，凱與大司馬丁奉、御史大夫丁固謀，因皓謁廟，欲廢皓立孫休子。'), Q('v061-b0014-n01', '凯欲因此兵以图之，令选曹白用丁奉。', '《吴录》'), Q('v061-b0014-n01', '皓曰：「用留平。」', '《吴录》')]),
    ],
    sourceScope='以卷五十五《丁奉传》为主，参核卷四十八吴主诸传、卷六十四《诸葛恪传》，另辨卷六十一《陆凯传》及裴注所记异说。本页不声称穷尽全书所有提及丁奉之处。',
)
