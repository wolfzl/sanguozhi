"""黄忠：以卷三十六本传为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v036-b0019', '黃忠字漢升，南陽人也。')
LIU_BIAO = Q('v036-b0019', '荊州牧劉表以為中郎將，與表從子磐共守長沙攸縣。')
CAO_JING = Q('v036-b0019', '及曹公克荊州')
HAN_XUAN = Q('v036-b0019', '假行裨將軍，仍就故任，統屬長沙守韓玄。')
JOIN = Q('v036-b0019', '先主南定諸郡，忠遂委質，隨從入蜀。')
ENTER_YEAR = Q('v032-b0016', '十六年，益州牧劉璋遙聞曹公將遣鍾繇等向漢中討張魯')
ATTACK_COMMAND = Q('v032-b0017', '乃使黃忠、卓膺勒兵向璋。')
ATTACK = Q('v036-b0019', '自葭萌受任，還攻劉璋，忠常先登陷陣，勇毅冠三軍。')
YIZHOU = Q('v036-b0019', '益州既定，拜為討虜將軍。')
DINGJUN = Q('v036-b0019', '建安二十四年，於漢中定軍山擊夏侯淵。')
VICTORY = Q('v036-b0019', '淵眾甚精，忠推鋒必進，勸率士卒，金鼓振天，歡聲動谷，一戰斬淵，淵軍大敗。')
HIGH_GROUND = Q('v032-b0021', '先主命黃忠乘高鼓譟攻之，大破淵軍，斬淵及曹公所署益州刺史趙顒等。')
PROMOTION = Q('v036-b0019', '遷征西將軍。是歲，先主為漢中王，欲用忠為後將軍')
CONCERN = Q('v036-b0019', '馬、張在近，親見其功，尚可喻指；關遙聞之，恐必不悅，得無不可乎！')
RANK = Q('v036-b0019', '遂與羽等齊位，賜爵關內侯。')
DEATH = Q('v036-b0019', '明年卒，追諡剛侯。')
HONOR = Q('v033-b0039', '三年秋九月，追諡故將軍關羽、張飛、馬超、龐統、黃忠。')
REFUSAL = Q('v041-b0024', '羽聞黃忠為後將軍，（羽）怒曰：「大丈夫終不與老兵同列！」不肯受拜。')
ACCEPTANCE = Q('v041-b0024', '羽大感悟，遂即受拜。')

PROFILE = dict(
    id='huang-zhong',
    tier='C',
    reading=['036', '032', '033', '041'],
    lead='黄忠起初在荆州领兵，归附刘备后随军入蜀。219年，他在定军山率部击破夏侯渊，后来升任后将军，与关羽等人同列。次年去世，身后谥刚侯。',
    role='刘备麾下后将军',

    facts=[
        dict(key='lifespan', label='生卒年', value='生年未详—220年',
             text='本传未载生年和享年。“明年卒”承上文建安二十四年（219），故卒于220年。',
             refs=[DINGJUN, DEATH]),
        dict(key='hometown', label='籍贯', value='南阳郡',
             text='本传明记黄忠为南阳人，未载具体县籍。',
             refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='刘备麾下将领',
             text='初受荆州牧刘表任用，曹操取荆州后仍在原任；刘备平定荆州南部诸郡时归附。',
             refs=[LIU_BIAO, CAO_JING, HAN_XUAN, JOIN]),
        dict(key='office', label='最高官职', value='后将军',
             text='平定益州后任讨虏将军，定军山战后迁征西将军；刘备成为汉中王后任命他为后将军。',
             refs=[YIZHOU, PROMOTION, REFUSAL]),
        dict(key='title', label='最高爵位', value='关内侯',
             text='刘备为汉中王以后，任黄忠为后将军，并赐爵关内侯。',
             refs=[PROMOTION, RANK]),
        dict(key='posthumous', label='身后称号', value='刚侯（260年追谥）',
             text='本传记谥号为刚侯，《后主传》记黄忠在景耀三年（260）与关羽等人同批获追谥。',
             refs=[DEATH, HONOR]),
        dict(key='deeds', label='代表事迹', items=['随军入蜀', '攻蜀先登', '定军山破敌'],
             text='随刘备入蜀，进攻刘璋时屡次先登，后在定军山率部打败夏侯渊。',
             refs=[JOIN, ATTACK, DINGJUN, VICTORY]),
    ],

    intro=[
        dict(title='从荆州旧将到随军入蜀',
             text='黄忠字汉升，南阳人。刘表任他为中郎将，让他与刘磐共守长沙攸县。曹操攻取荆州后，黄忠暂行裨将军，仍在原地任职，受长沙太守韩玄节制。待刘备平定南部诸郡，他才归附刘备，随后跟随刘备入蜀。刘备与刘璋决裂后，派他和卓膺领兵进攻。黄忠在这一阶段常率先登城、冲入敌阵。成都平定后，他被任为讨虏将军。短短几句本传，交代了他如何从旧部的一员，成为刘备征战益州时倚重的将领。',
             refs=[ORIGIN, LIU_BIAO, CAO_JING, HAN_XUAN, JOIN, ATTACK_COMMAND, ATTACK, YIZHOU],
             eventLinks=[dict(label='跟随刘备入蜀', eventId='enter-shu')]),
        dict(title='定军山之后的任命',
             text='219年，刘备在定军山据高扎营，夏侯渊领兵来争。黄忠奉命居高突击，率部打败曹军，夏侯渊在这一战中被斩。黄忠先升征西将军，又在刘备称汉中王后获任后将军，爵关内侯。诸葛亮担心远在荆州的关羽没有亲眼见到黄忠的战功，听闻两人同列会不高兴。《费诗传》另记，关羽得知消息后果然一度不肯领受自己的任命，经费诗劝说才接受。黄忠次年去世，后来获谥刚侯。',
             refs=[DINGJUN, Q('v032-b0021', '於定軍山勢作營。淵將兵來爭其地。'), HIGH_GROUND, PROMOTION,
                   RANK, CONCERN, REFUSAL, ACCEPTANCE, DEATH],
             eventLinks=[dict(label='黄忠奉命居高突击', eventId='hanzhong')]),
    ],

    careers=[
        dict(id='jingzhou', when='曹操取荆州前后，初任确年未载', title='领兵守攸县', office='中郎将，后暂行裨将军',
             text='刘表任黄忠与刘磐共守攸县；曹操取荆州后，黄忠仍在原任，隶属韩玄。',
             refs=[LIU_BIAO, CAO_JING, HAN_XUAN]),
        dict(id='enter-shu', when='211年', title='跟随刘备入蜀', office='—', eventIds=['enter-shu'],
             text='此前刘备平定荆州南部诸郡，黄忠归附；刘备于建安十六年入益州时，黄忠随行。',
             refs=[ENTER_YEAR, JOIN, Q('v032-b0016', '將步卒數万人入益州。')]),
        dict(id='yizhou', when='212—214年', title='攻刘璋，拜讨虏将军', office='讨虏将军',
             text='刘备派黄忠、卓膺领兵进攻刘璋；黄忠常先登陷阵，益州平定后受任讨虏将军。',
             refs=[ATTACK_COMMAND, ATTACK, Q('v032-b0018', '十九年夏，雒城破，進圍成都數十日，璋出降。'), YIZHOU]),
        dict(id='dingjun', when='219年', title='定军山破夏侯渊，任后将军', office='征西将军，后将军、关内侯', eventIds=['hanzhong'],
             text='奉刘备之命率部在定军山突击，斩夏侯渊、破其军；先升征西将军，刘备成为汉中王后又任他为后将军，赐爵关内侯。',
             refs=[DINGJUN, HIGH_GROUND, PROMOTION, REFUSAL, RANK]),
        dict(id='death', when='220年', title='去世', office='—',
             text='本传在建安二十四年的事迹之后记“明年卒”，未述死因。',
             refs=[DINGJUN, DEATH]),
        dict(id='posthumous', when='260年', title='获追谥刚侯', office='—',
             text='据《后主传》，朝廷在景耀三年秋九月追谥黄忠等五人；黄忠的谥号见本传。',
             refs=[HONOR, DEATH]),
    ],

    records=[
        dict(section='military', when='212—214年', title='攻益州屡次先登', category='先登陷阵', careerRef='yizhou',
             text='本传用“常先登陷阵”概括黄忠攻刘璋时的表现，他因而以作战勇毅见于记载，益州平定后受拜为讨虏将军。',
             refs=[ATTACK, YIZHOU]),
        dict(section='military', when='219年', title='定军山击破夏侯渊', category='居高突击', careerRef='dingjun', eventIds=['hanzhong'],
             text='夏侯渊部众精锐，黄忠借高地发动突击，率部击溃对方并斩其主将。这场胜利发生在曹操亲率援军到达之前；刘备据险相持，到曹操引军撤回才取得汉中。',
             refs=[VICTORY, HIGH_GROUND, Q('v032-b0021', '曹公自長安舉眾南征。'), Q('v032-b0021', '夏，曹公果引軍還，先主遂有漢中。')]),
        dict(section='setback', when='219年', title='任后将军引起同列争议', category='任命争议', careerRef='dingjun',
             text='诸葛亮事先担心黄忠资望与关羽、马超有别，关羽确曾因黄忠与自己同列而拒受任命，费诗劝说后才接受。这场争议出在刘备的人事安排，本书未说黄忠本人参与争执。',
             refs=[Q('v036-b0019', '忠之名望，素非關、馬之倫也。而今便令同列。'), CONCERN, REFUSAL, ACCEPTANCE]),
    ],
    sections={
        'civil': {'note': '黄忠在本书中主要以领兵、攻城和战功受任的经历见载；守攸县期间没有记下由他主持的地方治理措施。'},
    },

    assessment=[
        dict(title='陈寿：刘备的勇猛武将',
             text='陈寿将黄忠与赵云并论，称二人强悍勇猛，以“灌、滕”作比。',
             refs=[Q('v036-b0024', '黃忠、趙雲強摯壯猛，並作爪牙，其灌、滕之徒歟？')]),
    ],

    relations=[
        dict(category='旧主', name='刘表', personId='liu-biao', label='任中郎将守攸县',
             text='刘表任黄忠为中郎将，让他与自己的从子刘磐共同镇守攸县。',
             refs=[LIU_BIAO]),
        dict(category='君臣', name='刘备', personId='liubei', label='率其入蜀并授后将军',
             text='黄忠归附后随刘备入蜀，定军山之战奉命突击；刘备自认能化解对任命的顾虑，仍使黄忠与关羽等人同列。',
             refs=[JOIN, HIGH_GROUND, Q('v036-b0019', '先主曰：「吾自當解之。」遂與羽等齊位，賜爵關內侯。')]),
        dict(category='同僚', name='关羽', personId='guanyu', label='同列前、后将军',
             text='刘备遣费诗拜关羽为前将军时，关羽因黄忠任后将军不愿受拜，听完费诗劝说才改变主意。',
             refs=[Q('v041-b0024', '遣詩拜關羽為前將軍'), REFUSAL, ACCEPTANCE]),
    ],

    readingNotes=[
        dict(title='“老兵”不能确定生年',
             text='“老兵”是《费诗传》所记关羽动怒时的称呼。黄忠本传未载其生年或享年，不能凭这两个字算出他在定军山作战时的年龄。',
             refs=[REFUSAL, DEATH]),
    ],

    glossary=[
        ('假行', '临时代理某一官职。'),
        ('先登陷阵', '率先登城、冲入敌阵。'),
    ],

    sourceScope='以卷三十六《黄忠传》为主，参看卷三十二《先主传》的入蜀与汉中战事记载、卷三十三《后主传》的追谥纪年和卷四十一《费诗传》的授官争议。本页不声称穷尽全书所有提及黄忠之处。',
)
