"""夏侯惇：以卷九《夏侯惇传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v009-b0002', '夏侯惇字元讓，沛國譙人，夏侯嬰之後也。')
EARLY = Q('v009-b0002', '太祖初起，惇常爲裨將，從征伐。')
YANZHOU_YEAR = Q('v001-b0023', '興平元年春，太祖自徐州還')
HOLD_PUYANG = Q('v009-b0002', '太祖征陶謙，留惇守濮陽。張邈叛，迎吕布，太祖家在鄄城，惇輕車往赴')
HOSTAGE = Q('v009-b0002', '遣將僞降，共執持惇，責以寶貨，惇軍中震恐。')
HAN_HAO = Q('v009-b0002', '促召兵擊持質者。持質者惶遽叩头')
LEFT_EYE = Q('v009-b0003', '惇從征吕布，爲流矢所中，傷左目。')
IRRIGATION = Q('v009-b0003', '時大旱，蝗蟲起，惇乃斷太壽水作陂，身自負土，率將士勸種稻，民賴其利。')
REARGUARD = Q('v009-b0003', '太祖平河北，爲大將軍後拒。鄴破，遷伏波將軍，領尹如故')
TRUST = Q('v009-b0003', '召惇常與同載，特見親重，出入臥内，諸將莫得比也。')
FINAL_OFFICE = Q('v009-b0003', '文帝即王位，拜惇大將軍，數月薨。')
DEATH = Q('v002-b0005', '庚午，大將軍夏侯惇薨。')
SHRINE = Q('v003-b0016', '詔祀故大將軍夏侯惇、大司馬曹仁、車騎將軍程昱於太祖廟庭。')
SURNAME = Q('v009-b0008', '夏侯淵字妙才，惇族弟也。')
MIRROR = Q('v009-b0003-n01', '軍中號惇爲盲夏侯。惇惡之，每照鏡恚怒，輒撲鏡於地。', '《魏略》')

PROFILE = dict(
    id='xiahou-dun',
    tier='C',
    reading=['009'],
    new=dict(name='夏侯惇', courtesy='元让', faction='曹魏', period='汉末—220年',
             aliases=['盲夏侯'], tags=['兖州', '濮阳', '太寿水']),
    eventRoles=[('yanzhou-struggle', '迎战吕布，被劫后获救'),
                ('yuan-succession', '平河北时担任后军')],
    lead='曹操起兵时的旧将。兖州之争中曾被劫持，后与吕布再战时伤及左眼；旱蝗之年带头筑陂、劝种水稻。曹丕继位为魏王后任命他为大将军，数月后夏侯惇去世。',
    role='曹操起兵旧将、魏大将军',

    facts=[
        dict(key='lifespan', label='生卒年', value='生年未详—220年',
             text='生年未载。曹丕继为魏王、改元延康后，夏侯惇在当年夏四月去世。',
             refs=[DEATH, Q('v002-b0005', '夏四月丁巳'), Q('v002-b0001', '改建安二十五年爲延康元年。')]),
        dict(key='hometown', label='籍贯', value='沛国谯县', text='本传明记他是沛国谯人，夏侯婴之后。', refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='曹操起兵旧将',
             text='曹操初起兵时就随军征伐，后来可以与曹操同车、出入卧内。',
             refs=[EARLY, TRUST]),
        dict(key='office', label='最高官职', value='大将军',
             text='先后任伏波将军、前将军；曹丕继为魏王后拜大将军。',
             refs=[REARGUARD, Q('v002-b0004', '以前將軍夏侯惇爲大將軍。')]),
        dict(key='posthumous', label='身后称号', value='忠侯；233年配享太祖庙庭',
             text='本传记谥忠侯；魏明帝青龙元年五月，下诏以夏侯惇等人配享曹操庙庭。',
             refs=[Q('v009-b0004', '諡曰忠侯。'), Q('v003-b0016', '青龍元年春正月甲申'), SHRINE]),
        dict(key='deeds', label='代表事迹', items=['兖州拒吕布', '筑陂劝稻', '河北后军'],
             text='兖州之争中迎战吕布；旱蝗时筑陂劝种稻；平河北时为曹操后军。',
             refs=[HOLD_PUYANG, Q('v009-b0002', '惇輕車往赴，適與布會，交戰。'), IRRIGATION, REARGUARD]),
    ],

    intro=[
        dict(title='濮阳遇变，左眼受伤',
             text='夏侯惇是沛国谯人，字元让，很早就在曹操麾下从征。曹操出兵徐州，命他留守濮阳。张邈迎吕布入兖州时，曹操家眷在鄄城，夏侯惇轻车赶去，途中与吕布交战。吕布转取濮阳，袭得夏侯惇的军资，又派人假降，将他挟持索财，军中一时慌乱。部将韩浩先稳住各营，随后下令进击，挟持者叩头求饶，夏侯惇才获救。曹操从徐州回军后，他又随军攻吕布，被流矢伤了左眼。',
             refs=[ORIGIN, EARLY, HOLD_PUYANG, Q('v009-b0002', '布退還，遂入濮陽，襲得惇軍輜重。'),
                   HOSTAGE, Q('v009-b0002', '皆案甲當部不得動，諸營乃定。'), HAN_HAO, LEFT_EYE],
             eventLinks=[dict(label='迎吕布入兖州', eventId='yanzhou-struggle')]),
        dict(title='带头兴修水利，晚年受重用',
             text='夏侯惇后来领陈留、济阴太守，大旱又遇蝗灾时，他拦太寿水筑陂，自己背土，带着将士劝种水稻，当地百姓因此受益。曹操平定河北时，他担任后军；邺城攻下后，升任伏波将军，仍领河南尹，获准酌情办事。晚年曹操在摩陂，把他召来同车，还准他出入卧内，本传说其他将领没有这样的待遇。曹丕继为魏王，拜他为大将军，几个月后他便去世，谥号为忠。',
             refs=[Q('v009-b0003', '復領陳留、濟陰太守'), IRRIGATION, Q('v009-b0003', '轉領河南尹。'),
                   REARGUARD, Q('v009-b0003', '使得以便宜從事，不拘科制。'), Q('v009-b0003', '太祖軍於摩陂'),
                   TRUST, FINAL_OFFICE, Q('v009-b0004', '諡曰忠侯。')],
             eventLinks=[dict(label='平定河北', eventId='yuan-succession')]),
    ],

    careers=[
        dict(id='enlist', when='曹操初起兵时，确年未载', title='早年从曹操征伐', office='裨将，后任司马、折冲校尉，领东郡太守',
             text='初为裨将，随后任司马、别屯白马，升折冲校尉，领东郡太守。',
             refs=[EARLY, Q('v009-b0002', '以惇爲司馬，别屯白馬，遷折衝校尉，領東郡太守。')]),
        dict(id='yanzhou', when='194—195年', title='兖州遇变，被劫后获救', office='—', eventIds=['yanzhou-struggle'],
             text='由濮阳赶赴鄄城，途中迎战吕布；被假降者挟持时由韩浩救下，后来随曹操再攻吕布，被流矢伤及左眼。',
             refs=[YANZHOU_YEAR, HOLD_PUYANG, HOSTAGE, HAN_HAO, Q('v009-b0002', '惇既免'), LEFT_EYE]),
        dict(id='irrigation', when='领陈留、济阴太守时，确年未载', title='筑陂劝种稻', office='陈留、济阴太守，加建武将军，封高安乡侯',
             text='大旱、蝗虫并起，带头筑陂蓄水，率将士劝种水稻。',
             refs=[Q('v009-b0003', '復領陳留、濟陰太守，加建武將軍，封高安鄉侯。'), IRRIGATION]),
        dict(id='hebei', when='204年', title='河北战事中担任后军', office='伏波将军，仍领河南尹', eventIds=['yuan-succession'],
             text='本传记其在曹操平河北时担任后军；204年邺城被攻下后，他升任伏波将军。',
             refs=[REARGUARD, Q('v001-b0060', '配逆戰，敗，生禽配，斬之，鄴定。')]),
        dict(id='last-office', when='220年', title='拜大将军后去世', office='大将军',
             text='曹丕继为魏王，由前将军转任大将军，夏四月去世。',
             refs=[Q('v002-b0001', '改建安二十五年爲延康元年。'), FINAL_OFFICE, DEATH]),
    ],

    records=[
        dict(section='civil', when='领陈留、济阴太守时，确年未载', title='拦太寿水筑陂', category='水利与农事', careerRef='irrigation',
             text='旱蝗之年，他把将士组织起来兴修水利，又亲自背土、劝种稻。本传明确写到百姓从中受益。',
             refs=[IRRIGATION]),
        dict(section='military', when='204年', title='作为后军参与平河北', category='后军', careerRef='hebei', eventIds=['yuan-succession'],
             text='本传交代了他担任后军以及邺破后升迁的次序，未将攻下邺城的战功单独归给他。',
             refs=[REARGUARD]),
        dict(section='setback', when='194—195年', title='军资被夺，继而受伤', category='战场受挫', careerRef='yanzhou', eventIds=['yanzhou-struggle'],
             text='吕布夺得其军资，假降者还挟持了他；韩浩稳住诸营才解围。此后再随曹操攻吕布，他又被流矢伤了左眼。',
             refs=[Q('v009-b0002', '遂入濮陽，襲得惇軍輜重。'), HOSTAGE, HAN_HAO, LEFT_EYE]),
    ],

    relations=[
        dict(category='君臣', name='曹操', personId='caocao', label='从征与亲重',
             text='初起兵时便任裨将，晚年仍得曹操同车、出入卧内的礼遇。',
             refs=[EARLY, TRUST]),
        dict(category='部属', name='韩浩', label='稳定军营后救出主将',
             text='夏侯惇被挟持时，他先约束各营，再出兵制住挟持者。',
             refs=[Q('v009-b0002', '惇將韓浩乃勒兵屯惇營門'), HAN_HAO, Q('v009-b0002', '惇既免')]),
        dict(category='亲族', name='夏侯渊', personId='xiahou-yuan', label='同族而同为将军',
             text='夏侯渊是他的族弟；《魏略》记载，两人都在军中任将军。',
             refs=[SURNAME, Q('v009-b0003-n01', '時夏侯淵與惇俱爲將軍', '《魏略》')]),
    ],

    assessment=[
        dict(title='陈寿：任以亲旧，亦有战功',
             text='陈寿把夏侯、曹氏诸将放在一起评价，既指出累世通婚的关系，也肯定夏侯惇等人协助曹氏建功。',
             refs=[Q('v009-b0059', '夏侯、曹氏，世爲婚姻'), Q('v009-b0059', '貴重於時，左右勳業，咸有効勞。')]),
    ],

    readingNotes=[
        dict(title='受伤经过与军中的外号',
             text='本传只说流矢伤左眼，没有交代是谁射的。《魏略》另记军中称他“盲夏侯”，他厌恶这个称呼，照镜时因而发怒摔镜。',
             refs=[LEFT_EYE, MIRROR]),
    ],

    sourceScope='以卷九《夏侯惇传》为基础，参看卷一《武帝纪》、卷二《文帝纪》、卷三《明帝纪》，并将《魏略》所记军中外号与正文分开。本页不声称穷尽全书所有提及夏侯惇之处。',
)
