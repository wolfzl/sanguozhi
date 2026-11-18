"""程普：以卷五十五《程普传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v055-b0002', '程普字德謀，右北平土垠人也。')
CLERK = Q('v055-b0002', '初爲州郡吏，有容貌計略，善於應對。')
EARLY_WARS = Q('v055-b0002', '從孫堅征伐，討黃巾於宛、鄧，破董卓於陽人，攻城野戰，身被創夷。')
JIANGDONG = Q('v055-b0003', '堅薨，復隨孫策在淮南，從攻廬江，拔之，還俱東渡。')
EASTERN_WARS = Q('v055-b0003', '轉下秣陵、湖熟、句容、曲阿，普皆有功，增兵二千，騎五十匹。')
EASTERN_OFFICES = Q('v055-b0003', '以普爲吳郡都尉，治錢唐。後徙丹楊都尉，居石城。')
RELIEF = Q('v055-b0003', '策甞攻祖郎，大爲所圍，普與一騎共蔽扞策，驅馬疾呼，以矛突賊，賊披，策因隨出。')
SUCCESSION = Q('v055-b0004', '策薨，與張昭等共輔孫權，遂周旋三郡，平討不服。')
CHIBI = Q('v047-b0009', '瑜、普爲左右督，各領萬人，與備俱進，遇於赤壁，大破曹公軍。')
NANJUN = Q('v055-b0004', '與周瑜爲左右督，破曹公於烏林，又進攻南郡，走曹仁。')
JIANGXIA = Q('v055-b0004', '拜裨將軍，領江夏太守，治沙羨，食四縣。')
ELDER = Q('v055-b0005', '先出諸將，普最年長，時人皆呼程公。')
LATE_OFFICES = Q('v055-b0005', '周瑜卒，代領南郡太守。權分荊州與劉備，普復還領江夏，遷盪寇將軍，卒。')
HONOR = Q('v055-b0005', '權稱尊號，追論普功，封子咨爲亭侯。')
DISCORD = Q('v054-b0011', '惟與程普不睦。')
LU_MENG = Q('v051-b0009', '雖事決於瑜，普自恃久將，且俱是督，遂共不睦，幾敗國事，此目前之戒也。')
RECONCILIATION = Q('v054-b0011-n01', '普後自敬服而親重之，乃告人曰：「與周公瑾交，若飲醇醪，不覺自醉。」', '《江表传》')
DEATH_NOTE = Q('v055-b0005-n01', '普殺叛者數百人，皆使投火，即日病癘，百餘日卒。', '《吴书》')
CAO_REN_RETREATS = Q('v047-b0010', '仁委城走。')

PROFILE = dict(
    id='cheng-pu',
    tier='C',
    reading=['055'],
    lead='程普历事孙坚、孙策、孙权，随孙策征战江东，曾持矛突围救他。赤壁时与周瑜分任左右督，联刘备拒曹，又进攻南郡。晚年历领南郡、江夏太守，迁荡寇将军后去世。',
    role='历事孙氏三代的武将',

    facts=[
        dict(key='hometown', label='籍贯', value='右北平郡土垠县',
             text='《程普传》开篇记程普字德谋，右北平土垠人。', refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='孙氏旧将、赤壁左右督之一',
             text='早年为州郡吏，随后历事孙坚、孙策、孙权；诸将中程普最年长，时人称他“程公”。赤壁时，他与周瑜分任左右督。',
             refs=[CLERK, EARLY_WARS, JIANGDONG, SUCCESSION, ELDER, CHIBI]),
        dict(key='office', label='最高官职', value='荡寇将军，历领南郡、江夏太守',
             text='在孙策部下曾任吴郡、丹杨都尉，后拜荡寇中郎将、领零陵太守。赤壁、南郡战事后拜裨将军、领江夏太守；代领过南郡，再回江夏，迁荡寇将军。',
             refs=[EASTERN_OFFICES, Q('v055-b0003', '後拜盪寇中郎將，領零陵太守'), JIANGXIA, LATE_OFFICES]),
        dict(key='posthumous', label='身后称号', value='未载谥号；孙权追论其功',
             text='孙权称帝后追论程普的功劳，封其子程咨为亭侯；该爵授给程咨，本传未载程普本人的谥号。',
             refs=[HONOR, Q('v047-b0034', '黃龍元年春，公卿百司皆勸權正尊號。夏四月，夏口、武昌並言黃龍、鳳凰見。丙申，南郊即皇帝位。')]),
        dict(key='deeds', label='代表事迹', items=['持矛护主', '赤壁分督', '南郡逐曹仁'],
             text='持矛护孙策突围，与周瑜分督吴军在赤壁拒曹，随后进攻南郡，迫使曹仁退走。',
             refs=[RELIEF, CHIBI, NANJUN]),
    ],

    intro=[
        dict(title='随孙坚、孙策从征',
             text='程普字德谋，原是州郡吏，本传说他有计略、善于应对。跟随孙坚后，他在宛、邓讨黄巾，又随军在阳人击破董卓的军队，攻城野战中曾受伤。孙坚去世后，程普随孙策渡江，在秣陵、湖熟、句容、曲阿等地作战有功，增领两千士兵和五十匹战马。孙策攻祖郎时陷入包围，程普和另一名骑兵护住孙策，策马持矛冲开敌阵，孙策跟随他们脱围。他也先后出任吴郡、丹杨都尉。',
             refs=[ORIGIN, CLERK, EARLY_WARS, JIANGDONG, EASTERN_WARS, RELIEF, EASTERN_OFFICES],
             eventLinks=[dict(label='讨黄巾', eventId='yellow-turbans'),
                         dict(label='在阳人击破董卓的军队', eventId='anti-dong-coalition'),
                         dict(label='随孙策渡江', eventId='sun-ce-jiangdong')]),
        dict(title='辅孙权与督军拒曹',
             text='200年孙策去世，程普与张昭等辅佐孙权，转战三郡，平讨不服从者。曹操南下时，孙权以周瑜、程普为左右督，《吴主传》记二人各领万人，与刘备合力在赤壁击败曹军。随后二人又进攻南郡，曹仁弃城而走。其后程普拜裨将军、领江夏太守；周瑜去世，他接任南郡太守，后来又回江夏，升荡寇将军后去世。孙权称帝后追录他的功劳，封其子程咨为亭侯。',
             refs=[SUCCESSION, Q('v047-b0003', '五年。策薨，以事授權'), CHIBI, NANJUN,
                   CAO_REN_RETREATS, JIANGXIA, LATE_OFFICES, HONOR],
             eventLinks=[dict(label='辅佐孙权', eventId='sun-quan-succession'),
                         dict(label='赤壁击败曹军', eventId='chibi'),
                         dict(label='进攻南郡', eventId='nanjun-campaign')]),
    ],

    careers=[
        dict(id='yellow-turbans', when='184年', title='随孙坚讨黄巾', office='—', eventIds=['yellow-turbans'],
             text='由州郡吏从军，随孙坚在宛、邓讨黄巾。',
             refs=[CLERK, EARLY_WARS, Q('v046-b0004', '儁表請堅爲佐軍司馬'), Q('v046-b0004', '汝穎賊困迫，走保宛城。')]),
        dict(id='anti-dong', when='190年起', title='随孙坚讨董卓', office='—', eventIds=['anti-dong-coalition'],
             text='随孙坚参与讨董，在阳人击破董卓军。本传记其攻城野战曾受创伤。',
             refs=[EARLY_WARS, Q('v046-b0006', '諸州郡並興義兵，欲以討卓。堅亦舉兵。'),
                   Q('v046-b0007', '堅復相收兵，合戰於陽人，大破卓軍')]),
        dict(id='jiangdong', when='195年起', title='随孙策东渡，转战江东', office='吴郡都尉，后迁丹杨都尉', eventIds=['sun-ce-jiangdong'],
             text='随孙策渡江，在秣陵至曲阿等多地立功，增得步骑。孙策攻祖郎被围时，他与另一骑持矛掩护孙策脱围。',
             refs=[JIANGDONG, EASTERN_WARS, EASTERN_OFFICES, RELIEF,
                   Q('v046-b0014-n02', '策渡江攻繇牛渚營，盡得邸閣糧穀、戰具，是歳興平二年也。', '《江表传》')]),
        dict(id='succession', when='200年起', title='与张昭等辅佐孙权', office='—', eventIds=['sun-quan-succession'],
             text='孙策去世后，辅孙权统事，转战三郡。后来从攻江夏，另军讨平乐安，再代太史慈防守海昏。',
             refs=[SUCCESSION, Q('v055-b0004', '又從征江夏，還過豫章，別討樂安。樂安平定，代太史慈備海昏')]),
        dict(id='chibi-nanjun', when='208—209年', title='赤壁拒曹，继攻南郡', office='裨将军，领江夏太守', eventIds=['chibi', 'nanjun-campaign'],
             text='与周瑜分任左右督，联合刘备击败曹军；继攻南郡，迫使曹仁退走，程普后领江夏太守。',
             refs=[CHIBI, NANJUN, Q('v047-b0010', '十四年，瑜、仁相守歳餘，所殺傷甚眾。仁委城走。'), JIANGXIA]),
        dict(id='last-offices', when='周瑜卒后，确年未载', title='历领南郡、江夏后卒', office='领南郡太守，复领江夏太守，迁荡寇将军',
             text='周瑜死后接任南郡太守。孙权把荆州部分地区交给刘备后，程普回任江夏太守，迁荡寇将军后去世。',
             refs=[LATE_OFFICES, Q('v054-b0024', '令程普領南郡太守。')]),
    ],

    records=[
        dict(section='military', when='随孙策征战时，确年未载', title='持矛护孙策突围', category='战场救援', careerRef='jiangdong',
             text='孙策被祖郎围住时，程普以一骑为援，主动冲散围兵，为孙策打开去路。这里记的是程普本人如何救援，和传中概记的攻城战功不同。',
             refs=[RELIEF]),
        dict(section='military', when='208—209年', title='分督吴军，与刘备合兵', category='联军统率', careerRef='chibi-nanjun', eventIds=['chibi', 'nanjun-campaign'],
             text='《吴主传》记程普与周瑜各领万人。吴军在赤壁取胜后继续进攻南郡，直至曹仁弃城，程普的作用见于两处战事的连续统兵。',
             refs=[CHIBI, NANJUN, CAO_REN_RETREATS]),
        dict(section='setback', when='与周瑜共事时，确年未载', title='分任左右督而不睦', category='将帅失和', careerRef='chibi-nanjun',
             text='《周瑜传》明记程普与周瑜不睦。吕蒙后来反对与孙皎共同统兵，拿程普自恃资历、两督不和为戒，说这几乎误了大事；这是吕蒙提出的先例，南郡之战最终仍迫退曹仁。',
             refs=[DISCORD, LU_MENG, NANJUN]),
    ],
    sections={
        'civil': {'note': '程普历任吴郡、丹杨都尉，并领过零陵、南郡、江夏太守。本传只说他好施与、喜士大夫，没有记下可单列的地方政务或治理成效。'},
    },

    assessment=[
        dict(title='陈寿：江表虎臣',
             text='陈寿把程普与同卷诸将合评为“江表之虎臣”，强调孙氏对这些领兵将领的厚待。',
             refs=[Q('v055-b0073', '凡此諸將，皆江表之虎臣，孫氏之所厚待也。')]),
    ],

    relations=[
        dict(category='旧主', name='孙坚', personId='sun-jian', label='随军讨黄巾与董卓',
             text='随孙坚在宛、邓讨黄巾，又参加阳人之战。', refs=[EARLY_WARS]),
        dict(category='旧主', name='孙策', personId='sun-ce', label='随军东渡，持矛护主',
             text='先后随孙策攻庐江、渡江征战，在孙策遭祖郎包围时掩护他突围。', refs=[JIANGDONG, RELIEF]),
        dict(category='君臣', name='孙权', personId='sunquan', label='辅其接掌江东',
             text='程普与张昭等辅佐孙权接掌江东。孙权称帝后又追录程普的功劳，封其子程咨为亭侯。',
             refs=[SUCCESSION, HONOR]),
        dict(category='同僚', name='周瑜', personId='zhouyu', label='并为左右督',
             text='两人共同拒曹并攻南郡，曾不睦；周瑜去世后，程普接领南郡太守。',
             refs=[NANJUN, DISCORD, LATE_OFFICES]),
    ],

    readingNotes=[
        dict(title='“不睦”之后是否和解',
             text='《周瑜传》正文只说二人不睦；裴注引《江表传》说程普自恃年长，数次轻侮周瑜，后来佩服周瑜的度量，把与他相交比成饮醇酒。和解与比喻都来自这条裴注。',
             refs=[DISCORD, Q('v054-b0011-n01', '普頗以年長，數陵侮瑜。瑜折節容下，終不與校。', '《江表传》'), RECONCILIATION]),
        dict(title='程普之死：正文与裴注',
             text='本传仅记程普迁荡寇将军后去世。裴注引《吴书》另说他令数百名叛者投火，当日染病，百余日后去世；这条注没有说明处置叛者的时间或地点，也不足以确定死因。',
             refs=[LATE_OFFICES, DEATH_NOTE]),
    ],

    sourceScope='以卷五十五《程普传》为主，参看卷四十六《孙坚传》《孙策传》、卷四十七《吴主传》、卷五十一《孙皎传》和卷五十四《周瑜传》《鲁肃传》；裴注里的和解与病逝细节另见史料辨析。本页不声称穷尽全书所有提及程普之处。',
)
