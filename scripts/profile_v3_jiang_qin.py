"""蒋钦：以卷五十五《蒋钦传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v055-b0015', '蔣欽字公弈，九江壽春人也。')
EAST = Q('v055-b0015', '及策東渡，拜別部司馬，授兵。與策周旋，平定三郡，又從定豫章。')
FIVE_COUNTIES = Q('v055-b0015', '會稽冶賊呂合、秦狼等爲亂，欽將兵討擊，遂禽合、狼，五縣平定')
HEFEI = Q('v055-b0015', '從征合肥，魏將張遼襲權於津北，欽力戰有功，遷盪寇將軍，領濡須督。')
JUSTICE = Q('v055-b0015', '後召還都，拜津右護軍，典領辭訟。')
FRUGAL = Q('v055-b0016', '權甞入其堂內，母踈帳縹被，妻妾布裙。權歎其在貴守約')
XU_ARREST = Q('v055-b0017', '蕪湖令徐盛收欽屯吏，表斬之，權以欽在遠不許，盛由是自嫌於欽。')
XU_PRAISE = Q('v055-b0017', '盛常畏欽因事害己，而欽每稱其善。盛旣服德，論者美焉。')
DEATH = Q('v055-b0018', '權討關羽，欽督水軍入沔，還，道病卒。')
MOURNING = Q('v055-b0018', '權素服舉哀，以蕪湖民二百戶、田二百頃，給欽妻子。')

PROFILE = dict(
    id='jiang-qin', tier='C', reading=['055'],
    new=dict(name='蒋钦', courtesy='公弈', faction='孙吴', period='汉末—孙权取荆州后', aliases=['蒋公弈'], tags=['孙策东渡', '逍遥津', '沔水']),
    eventRoles=[('sun-ce-jiangdong', '随孙策东渡，领兵平三郡'), ('hefei', '津北迎战张辽有功'),
                ('jingzhou', '督水军入沔水')],
    lead='蒋钦随孙策东渡，转战江东。合肥撤军遇袭时力战有功，升荡寇将军、领濡须督，后来回都掌管辞讼。徐盛曾请处死他属下的屯吏，他仍多次称赞徐盛。孙权征关羽时，他督水军入沔，回师途中病卒。',
    role='孙吴荡寇将军、水军将领',
    facts=[
        dict(key='lifespan', label='生卒年', value='生年未详—征关羽回军途中病卒',
             text='本传不载生年；孙权出兵讨关羽在建安二十四年（219），本传只记蒋钦从沔水回师途中病卒，未另记卒年。', refs=[DEATH, Q('v047-b0018', '閏月，權征羽，先遣呂蒙襲公安')]),
        dict(key='hometown', label='籍贯', value='九江郡寿春县', text='蒋钦字公弈，九江寿春人。', refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='孙策旧将，后为孙权领兵', text='随孙策东渡立功，孙权时督守濡须，讨关羽时统领水军。', refs=[EAST, HEFEI, DEATH]),
        dict(key='office', label='最高官职', value='荡寇将军；后任津右护军', text='随孙策东渡拜别部司马；合肥一役后升荡寇将军、领濡须督，后来召还任津右护军，掌管辞讼。', refs=[EAST, HEFEI, JUSTICE]),
        dict(key='posthumous', label='身后称号', value='未载谥号；孙权素服举哀', text='孙权为他举哀，并将民户及田地给其妻儿；本传没有记载追谥。', refs=[MOURNING]),
        dict(key='deeds', label='代表事迹', items=['随孙策东渡', '讨平会稽五县', '逍遥津力战', '督水军入沔'], text='随孙策渡江平三郡，后参与平定会稽五县，逍遥津力战，征关羽时督领水军入沔。', refs=[EAST, FIVE_COUNTIES, HEFEI, DEATH]),
    ],
    intro=[
        dict(title='随军渡江，津北立功',
             text='蒋钦字公弈，九江寿春人，早年便追随孙策。随孙策东渡时，他获授兵众，任别部司马，参与平定三郡，又随军攻定豫章。之后他历任县职，也曾领兵讨会稽的吕合、秦狼，平定五县。孙权攻合肥后撤兵，张辽袭击逍遥津北的孙权，蒋钦力战有功，迁荡寇将军，兼任濡须督。后来他被召回都城，任津右护军，负责处理辞讼；孙权到过他家，见其母、妻妾衣用俭朴，感叹他地位已高而仍守俭。',
             refs=[ORIGIN, EAST, Q('v055-b0015', '調授葛陽尉，歷三縣長'), FIVE_COUNTIES, HEFEI, JUSTICE, FRUGAL],
             eventLinks=[dict(label='随孙策东渡', eventId='sun-ce-jiangdong'), dict(label='攻合肥', eventId='hefei')]),
        dict(title='称许徐盛，督军入沔',
             text='徐盛任芜湖令时，曾收押蒋钦的一名屯吏，上表请求处斩。孙权因蒋钦在外而不允，徐盛从此怕蒋钦报复。后来曹操出兵濡须，蒋钦与吕蒙协调诸军，徐盛仍有顾虑，蒋钦却屡次称赞他，徐盛这才心服。219年孙权征讨关羽，蒋钦督水军进入沔水，在回师途中病卒。孙权为他着素服举哀，又赐芜湖民户、田地给他的家人。',
             refs=[XU_ARREST, Q('v055-b0017', '曹公出濡須，欽與呂蒙持諸軍節度。'), XU_PRAISE, Q('v047-b0018', '閏月，權征羽，先遣呂蒙襲公安'), DEATH, MOURNING],
             eventLinks=[dict(label='孙权征讨关羽', eventId='jingzhou')]),
    ],
    careers=[
        dict(id='jiangdong', when='195年起', title='随孙策东渡经营江东', office='别部司马', eventIds=['sun-ce-jiangdong'],
             text='随孙策渡江，获授兵众，参与平定三郡，后来又随军平定豫章。', refs=[EAST, Q('v046-b0014-n02', '策渡江攻繇牛渚營，盡得邸閣糧穀、戰具，是歳興平二年也。', '《江表传》')]),
        dict(id='kuaiji', when='孙权统事后，确年未载', title='平定会稽五县', office='讨越中郎将',
             text='移任县职和都尉后，领兵平定会稽吕合、秦狼之乱；《吕岱传》亦记两人共同出兵。', refs=[FIVE_COUNTIES, Q('v055-b0015', '徙討越中郎將'), Q('v060-b0020', '與將軍蔣欽等將兵討之，遂擒合、狼，五縣平定')]),
        dict(id='hefei', when='215年', title='合肥撤军时迎击张辽', office='荡寇将军，领濡须督', eventIds=['hefei'],
             text='张辽在津北突袭孙权，蒋钦力战立功。', refs=[HEFEI, Q('v055-b0041', '建安二十年，從攻合肥')]),
        dict(id='return-to-capital', when='合肥战后，确年未载', title='回都掌管辞讼', office='津右护军',
             text='孙权把蒋钦从濡须召回都城，任命他掌管辞讼。', refs=[JUSTICE]),
        dict(id='mian', when='219年起', title='督水军入沔，回师病卒', office='水军统督', eventIds=['jingzhou'],
             text='孙权征讨关羽时，领水军驶入沔水，回军途中患病去世。', refs=[Q('v047-b0018', '二十四年，關羽圍曹仁於襄陽'), DEATH]),
    ],
    records=[
        dict(section='civil', when='确年未载', title='不因旧嫌掩徐盛之才', category='识才荐士',
             text='徐盛曾请处死蒋钦的一名屯吏，蒋钦后来仍称其善。裴注引《江表传》说，他看重徐盛有胆略、能统兵，认为选人不应夹带私怨。', refs=[XU_ARREST, XU_PRAISE, Q('v055-b0017-n01', '臣聞公舉不挾私怨，盛忠而勤彊，有膽略器用，好萬人督也。', '《江表传》')]),
        dict(section='military', when='215年', title='逍遥津北力战', category='退军遇袭', careerRef='hefei', eventIds=['hefei'],
             text='吴军主力已经先行撤出，蒋钦仍随孙权在津北，张辽突袭时力战，战后受命领濡须督。', refs=[Q('v055-b0041', '軍旅皆已引出，唯車下虎士千餘人，并呂蒙、蔣欽、凌統及寧，從權逍遙津北。'), HEFEI]),
        dict(section='setback', when='征关羽回师时，确年未载', title='征战回师途中病卒', category='军中病卒', careerRef='mian', eventIds=['jingzhou'],
             text='入沔后回军，蒋钦在途中因病去世；本传未记水军败绩，也没有交代病因。', refs=[DEATH]),
    ],
    relations=[
        dict(category='旧主', name='孙策', personId='sun-ce', label='随其东渡，初领兵众', text='蒋钦随孙策渡江，任别部司马，参与平定三郡及豫章。', refs=[EAST]),
        dict(category='君臣', name='孙权', personId='sunquan', label='任护军，身后亲举哀', text='孙权召蒋钦回都任津右护军。他回师病卒后，孙权素服举哀并给其家人田地。', refs=[JUSTICE, DEATH, MOURNING]),
        dict(category='同僚', name='徐盛', personId='xu-sheng', label='有旧嫌仍予称许', text='徐盛因曾收押蒋钦屯吏而自嫌，蒋钦仍多次称其长处。', refs=[XU_ARREST, XU_PRAISE]),
    ],
    readingNotes=[
        dict(title='孙权也曾劝蒋钦读书', text='裴注引《江表传》说，孙权同时劝吕蒙、蒋钦学习，后来把二人并称为富贵之后仍“折节好学”。这段故事里较详的读书经历和鲁肃的对话，写的是吕蒙。', refs=[Q('v054-b0030-n01', '權謂蒙及蔣欽曰：「卿今並當塗掌事，宜學問以自開益。」', '《江表传》'), Q('v054-b0030-n01', '人長而進益，如呂蒙、蔣欽，蓋不可及也。富貴榮顯，更能折節好學', '《江表传》')]),
    ],
    sourceScope='以卷五十五《蒋钦传》为主，参看卷四十六、四十七的纪年、卷六十《吕岱传》和卷五十四《吕蒙传》裴注所引《江表传》。本页不声称穷尽全书所有提及蒋钦之处。',
)
