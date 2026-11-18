"""庞德：以卷十八《庞德传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v018-b0036', '龐德字令明，南安狟道人也。')
MA_TENG = Q('v018-b0036', '初平中，從馬騰擊反羌叛氐。數有功，稍遷至校尉。')
GUO_YUAN = Q('v018-b0036', '德隨騰子超拒援、幹於平陽，德為軍鋒，進攻援、幹，大破之，親斬援首。')
MA_CHAO = Q('v018-b0036', '太祖破超於渭南，德隨超亡入漢陽，保冀城。')
JOIN_CAO = Q('v018-b0036', '後復隨超奔漢中，從張魯。太祖定漢中，德隨眾降。')
OFFICE = Q('v018-b0036', '太祖素聞其驍勇，拜立義將軍，封關門亭侯，邑三百戶。')
WAN = Q('v018-b0037', '德將所領與曹仁共攻拔宛，斬音、開，遂南屯樊。')
WHITE_HORSE = Q('v018-b0037', '後親與羽交戰，射羽中額。時德常乘白馬，羽軍謂之白馬將軍，皆憚之。')
FLOOD = Q('v018-b0037', '會天霖雨十餘日，漢水暴溢，樊下平地五六丈，德與諸將避水上堤。')
CAPTURE = Q('v018-b0037', '水盛船覆，失弓矢，獨抱船覆水中，為羽所得，立而不跪。')
DEATH = Q('v018-b0037', '我寧為國家鬼，不為賊將也。」遂為羽所殺。')
DEATH_YEAR = Q('v036-b0006', '二十四年，先主為漢中王，拜羽為前將軍，假節鉞。')
DEATH_CROSSCHECK = Q('v036-b0006', '禁降羽，羽又斬將軍龐德。')
POSTHUMOUS = Q('v018-b0038', '文帝即王位，乃遣使就德墓賜謚')
POSTHUMOUS_TITLE = Q('v018-b0038', '寡人愍焉，謚曰壯侯。')

PROFILE = dict(
    id='pang-de', tier='C', reading=['018'],
    new=dict(name='庞德', courtesy='令明', faction='曹魏', period='汉末—219年',
             aliases=['白马将军'], tags=['马超', '汉中', '樊城']),
    eventRoles=[('tongguan', '随马超败走汉阳'), ('zhanglu-surrender', '在汉中随张鲁部众降曹'),
                ('jingzhou', '樊城力战，被俘拒降')],
    lead='庞德早年随马腾、马超在关中征战，后在汉中随张鲁部众归降曹操。219年樊城水涨，庞德率部力战，乘小船回营时翻船被俘，拒降后被关羽杀死。曹丕即魏王位后谥他为壮侯。',
    role='从马氏归曹的立义将军',

    facts=[
        dict(key='lifespan', label='生卒年', value='生年未详—219年',
             text='本传未记生年。《关羽传》把关羽斩庞德系在建安二十四年（219）樊城战事。',
             refs=[DEATH_YEAR, DEATH_CROSSCHECK, DEATH]),
        dict(key='hometown', label='籍贯', value='南安郡狟道县',
             text='本传记庞德字令明，南安狟道人。', refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='先事马氏，后为曹操统兵',
             text='先跟随马腾和马超，后随马超入汉中，曹操平定汉中时随众降曹。页面归入曹魏，庞德生前为魏王曹操效力。',
             refs=[MA_TENG, MA_CHAO, JOIN_CAO, OFFICE, Q('v018-b0037', '魏王帶甲百萬，威振天下。')]),
        dict(key='office', label='最高官职', value='立义将军',
             text='随马腾、马超作战时由校尉升中郎将。曹操平汉中后，以庞德为立义将军。',
             refs=[MA_TENG, Q('v018-b0036', '拜中郎將，封都亭侯。'), OFFICE]),
        dict(key='posthumous', label='身后称号', value='壮侯（220年）',
             text='曹丕于220年继为魏王，遣使到庞德墓前宣读策命，追谥壮侯。',
             refs=[Q('v002-b0001', '太祖崩，嗣位爲丞相、魏王。'), POSTHUMOUS, POSTHUMOUS_TITLE]),
        dict(key='deeds', label='代表事迹', items=['平阳斩郭援', '汉中归曹', '樊城被俘拒降'],
             text='在平阳前锋破敌并斩郭援，曹操取汉中时随张鲁部众归降，樊城被俘后拒降而死。',
             refs=[GUO_YUAN, JOIN_CAO, CAPTURE, DEATH]),
    ],

    intro=[
        dict(title='由马氏旧部转入曹营',
             text='庞德字令明，南安狟道人。年轻时做过郡吏、州从事，初平年间跟随马腾对抗叛乱的羌、氐部众，因屡次立功升到校尉。马超在平阳迎战郭援、高干时，庞德担任前锋，亲手斩杀郭援，拜中郎将、封都亭侯。马腾被征为卫尉后，庞德留在马超麾下。曹操在渭南击败马超，庞德随他逃往汉阳，后来又跟到汉中，投奔张鲁。曹操平定汉中，庞德随众归降；曹操听说过他的勇名，任他为立义将军，封关门亭侯。',
             refs=[ORIGIN, Q('v018-b0036', '少為郡吏州從事。'), MA_TENG, GUO_YUAN,
                   Q('v018-b0036', '拜中郎將，封都亭侯。'), Q('v018-b0036', '後騰徵為衛尉，德留屬超。'), MA_CHAO, JOIN_CAO, OFFICE],
             eventLinks=[dict(label='在渭南击败马超', eventId='tongguan'), dict(label='曹操平定汉中', eventId='zhanglu-surrender')]),
        dict(title='樊城水围中的绝战',
             text='庞德随曹仁攻破反叛的侯音、卫开后南屯樊城。诸将因他的兄长在汉中而疑虑，庞德表示要亲自迎击关羽。本传说他曾在交战中射中关羽额头，因常骑白马，被关羽军称为“白马将军”。219年关羽围樊城，久雨后汉水暴涨，庞德等避水登堤，关羽乘船从四面进攻。他力战到弓箭用尽，乘小船想回曹仁营中，船被水掀翻，庞德被俘。关羽想任用他，庞德拒绝，最终被杀。曹操闻讯流泪，封其二子为列侯。',
             refs=[WAN, Q('v018-b0037', '樊下諸將以德兄在漢中，頗疑之'), Q('v018-b0037', '我欲身自擊羽。'),
                   WHITE_HORSE, DEATH_YEAR, FLOOD, Q('v018-b0037', '羽乘船攻之，以大船四面射堤上。'),
                   Q('v018-b0037', '羽攻益急，矢盡，短兵接戰。'), Q('v018-b0037', '乘小船欲還仁營'),
                   CAPTURE, Q('v018-b0037', '我欲以卿為將'), DEATH, Q('v018-b0037', '太祖聞而悲之，為之流涕，封其二子為列侯。')],
             eventLinks=[dict(label='关羽围樊城', eventId='jingzhou')]),
    ],

    careers=[
        dict(id='first-service', when='初平至建安年间，确年未载', title='从马腾、马超作战，斩郭援', office='校尉，后拜中郎将、都亭侯',
             text='初随马腾攻叛乱部众，后随马超在平阳迎击郭援、高干，率先攻敌并斩郭援。',
             refs=[MA_TENG, GUO_YUAN, Q('v018-b0036', '拜中郎將，封都亭侯。')]),
        dict(id='weinan', when='211年战败后', title='在渭南败后随马超入汉阳', office='—', eventIds=['tongguan'],
             text='马腾入朝后庞德仍留马超麾下。马超在渭南战败，庞德与他逃往汉阳，退保冀城。',
             refs=[Q('v018-b0036', '後騰徵為衛尉，德留屬超。'), MA_CHAO]),
        dict(id='han-zhong', when='215年', title='张鲁失据后随众归曹', office='立义将军、关门亭侯', eventIds=['zhanglu-surrender'],
             text='随马超入汉中后一度从张鲁。曹操取汉中时，庞德随众投降，获曹操封拜。',
             refs=[JOIN_CAO, OFFICE]),
        dict(id='fan-cheng', when='219年', title='樊城遇洪水，被俘后拒降而死', office='—', eventIds=['jingzhou'],
             text='在樊城迎战关羽。汉水上涨后乘小船撤回曹仁营，船翻被俘；拒绝关羽招揽，被杀。',
             refs=[DEATH_YEAR, DEATH_CROSSCHECK, FLOOD, Q('v018-b0037', '乘小船欲還仁營'), CAPTURE, DEATH]),
        dict(id='honor', when='220年', title='曹丕遣使墓前追谥', office='追谥壮侯',
             text='曹丕即魏王位后遣使到庞德墓前授谥，另封其子庞会等四人为关内侯。',
             refs=[Q('v002-b0001', '太祖崩，嗣位爲丞相、魏王。'), POSTHUMOUS, POSTHUMOUS_TITLE,
                   Q('v018-b0038', '又賜子會等四人爵關內侯，邑各百戶。')]),
    ],

    records=[
        dict(section='military', when='建安年间，确年未载', title='平阳为军锋，击破郭援部', category='前锋破敌', careerRef='first-service',
             text='马超率军迎击郭援、高干，庞德负责率先冲击，本传把斩郭援列为其战果。',
             refs=[GUO_YUAN]),
        dict(section='military', when='219年', title='樊城迎击关羽', category='前线拒敌', careerRef='fan-cheng', eventIds=['jingzhou'],
             text='本传将白马称谓系于樊城交战，认为关羽军畏惧屡乘白马出战的庞德；这称谓来自敌军，并非官号。',
             refs=[WHITE_HORSE, OFFICE]),
        dict(section='setback', when='219年', title='洪水中撤退失败，被俘而死', category='水围失利', careerRef='fan-cheng', eventIds=['jingzhou'],
             text='曹军临水失去原有防地，庞德率部分人试图乘舟回营，因翻船被俘；关羽招揽未成，最终将他处死。',
             refs=[FLOOD, Q('v018-b0037', '乘小船欲還仁營'), CAPTURE, Q('v018-b0037', '我欲以卿為將'), DEATH]),
    ],
    sections={
        'civil': {'note': '庞德早年曾为郡吏、州从事。本传随后主要记其统军经历，未交代他任郡州属吏时的具体政绩。'},
    },

    assessment=[
        dict(title='陈寿：有周苛之节',
             text='陈寿以“授命叱敌”概括庞德的结局，将他比作汉初的周苛，着重于被擒后不肯屈从。',
             refs=[Q('v018-b0050', '龐德授命叱敵，有周苛之節。'), DEATH]),
    ],

    relations=[
        dict(category='旧主', name='马超', personId='ma-chao', label='平阳并战，渭南同退',
             text='庞德在马腾入朝后留属马超。马超为曹操所破，庞德先随他退往汉阳，后同奔汉中。',
             refs=[GUO_YUAN, Q('v018-b0036', '後騰徵為衛尉，德留屬超。'), MA_CHAO, JOIN_CAO]),
        dict(category='君臣', name='曹操', personId='caocao', label='降后任立义将军',
             text='庞德在汉中归曹后被授立义将军。庞德死讯传来，曹操流涕，并封他两个儿子为列侯。',
             refs=[OFFICE, Q('v018-b0037', '太祖聞而悲之，為之流涕，封其二子為列侯。')]),
        dict(category='同僚', name='曹仁', personId='cao-ren', label='共攻宛城，后屯樊城',
             text='二人攻下侯音据守的宛城；庞德在樊北受洪水所迫，曾设法乘小船返回曹仁营。',
             refs=[WAN, Q('v018-b0037', '仁使德屯樊北十里'), Q('v018-b0037', '乘小船欲還仁營')]),
        dict(category='敌对', name='关羽', personId='guanyu', label='樊城相战，被擒拒降',
             text='庞德与关羽交战并射中其额，后来落水被俘。关羽希望纳用庞德，庞德拒绝，被关羽杀死。',
             refs=[WHITE_HORSE, CAPTURE, Q('v018-b0037', '我欲以卿為將'), DEATH]),
    ],

    readingNotes=[
        dict(title='裴松之质疑从蜀地迎葬的说法',
             text='裴注引王隐《蜀记》说，钟会平蜀后从蜀地迎回庞德遗骸葬于邺。裴松之以庞德死于樊城、曹丕早已遣使到墓前追谥为依据，反驳这项记载。',
             refs=[Q('v018-b0038-n01', '鍾會平蜀，前後鼓吹，迎德屍喪還葬鄴', '《蜀记》'), POSTHUMOUS,
                   Q('v018-b0038-n01', '臣松之案德死於樊城，文帝即位，又遣使至德墓所，則其屍喪不應在蜀。', '裴松之案')]),
    ],
    sourceScope='以卷十八《庞德传》为主，参看卷二《文帝纪》、卷三十六《关羽传》；裴注所收迎葬异说单列辨析。本页不声称穷尽全书所有提及庞德之处。',
)
