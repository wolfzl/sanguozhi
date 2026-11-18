"""夏侯渊：以卷九《夏侯渊传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v009-b0008', '夏侯淵字妙才，惇族弟也。')
DUN_HOME = Q('v009-b0002', '夏侯惇字元讓，沛國譙人')
EARLY = Q('v009-b0008', '太祖起兵，以别部司馬、騎都尉從，遷陳留、潁川太守。')
GUANDU = Q('v009-b0008', '及與袁紹戰於官渡，行督軍校尉。')
SUPPLY = Q('v009-b0008', '紹破，使督兖、豫、徐州軍糧；時軍食少，淵傳饋相繼，軍以復振。')
WEINAN = Q('v009-b0008', '從征韓遂等，戰於渭南。')
QISHAN = Q('v009-b0009', '遂行，使張郃督步騎五千在前，從陳倉狹道入，淵自督糧在後。')
LONGYOU = Q('v009-b0010', '淵别遣張郃等平河關，渡河入小湟中，河西諸羌盡降，隴右平。')
ZHANG_LU = Q('v009-b0010', '會魯降，漢中平，以淵行都護將軍，督張郃、徐晃等平巴郡。')
HOLD_HANZHONG = Q('v009-b0010', '太祖還鄴，留淵守漢中，即拜淵征西將軍。')
DINGJUN = Q('v009-b0010', '淵分所將兵半助郃，爲備所襲，淵遂戰死。諡曰愍侯。')
HUANG_ZHONG = Q('v036-b0019', '建安二十四年，於漢中定軍山擊夏侯淵。')
SHRINE = Q('v004-b0010', '征西將軍夏侯淵')
WARNING = Q('v009-b0011', '將當以勇爲本，行之以智計；但知任勇，一匹夫敵耳。')

PROFILE = dict(
    id='xiahou-yuan',
    tier='C',
    reading=['009'],
    new=dict(name='夏侯渊', courtesy='妙才', faction='曹魏', period='汉末—219年',
             tags=['官渡', '陇右', '定军山']),
    eventRoles=[('guandu', '任督军校尉，后督军粮'), ('tongguan', '随军战于渭南'),
                ('zhanglu-surrender', '张鲁降后督将平巴郡'), ('hanzhong', '守汉中，定军山战死')],
    lead='曹操的西线主将。官渡战后接续运粮，曾出兵解祁山之围、平定陇右。张鲁投降后留守汉中，任征西将军；219年在定军山受到刘备军突击，战死。',
    role='曹操镇守汉中的征西将军',

    facts=[
        dict(key='lifespan', label='生卒年', value='生年未详—219年',
             text='本传未载生年，记他于建安二十四年正月战死。',
             refs=[Q('v009-b0010', '二十四年正月，備夜燒圍鹿角。'), DINGJUN, HUANG_ZHONG]),
        dict(key='hometown', label='籍贯', value='本传未直书；族兄为沛国谯人',
             text='本传开篇只写夏侯渊是夏侯惇的族弟。夏侯惇为沛国谯人，这条亲缘提供了籍贯线索。',
             refs=[ORIGIN, DUN_HOME]),
        dict(key='identity', label='主要身份', value='曹操部将，留守汉中',
             text='曹操起兵即追随；张鲁投降后受命留守汉中，在曹丕称帝之前战死。',
             refs=[EARLY, HOLD_HANZHONG, DINGJUN]),
        dict(key='office', label='最高官职', value='征西将军',
             text='官渡时代理督军校尉，张鲁投降后代理都护将军，曹操回邺时正式拜为征西将军。',
             refs=[GUANDU, ZHANG_LU, HOLD_HANZHONG]),
        dict(key='posthumous', label='身后称号', value='愍侯；243年配享太祖庙庭',
             text='战死后谥愍侯。魏齐王曹芳正始四年，夏侯渊列入配享太祖庙庭的诏书。',
             refs=[DINGJUN, SHRINE, Q('v004-b0010', '武猛校尉典韋於太祖廟庭。')]),
        dict(key='deeds', label='代表事迹', items=['接续军粮', '急援祁山', '镇守汉中'],
             text='官渡战后督运三州粮食；率兵救祁山；张鲁归降后奉命守汉中。',
             refs=[SUPPLY, QISHAN, ZHANG_LU, HOLD_HANZHONG]),
    ],

    intro=[
        dict(title='从官渡督粮到陇右统兵',
             text='夏侯渊字妙才，是夏侯惇的族弟，曹操起兵后便随军征伐。官渡之战时代理督军校尉，袁绍兵败后受命督运兖、豫、徐三州军粮。曹军一时缺粮，他接续运送，才使军队恢复。此后随曹操参加渭南之战。马超后来自汉中回攻祁山，诸将有人想等曹操下令；夏侯渊认为邺城路远，往返请示将让求救者先败，便命张郃率军先行，自己在后督粮。此后他继续与韩遂交兵，又攻下枹罕、杀宋建，分遣张郃等平定河关。',
             refs=[ORIGIN, EARLY, GUANDU, SUPPLY, WEINAN, Q('v009-b0009', '超奔漢中，還圍祁山。'),
                   Q('v009-b0009', '公在鄴，反覆四千里，比報，叙等必敗，非救急也。'), QISHAN,
                   Q('v009-b0009', '大破遂軍，得其旌麾'), Q('v009-b0010', '圍枹罕，月餘拔之，斬建'), LONGYOU],
             eventLinks=[dict(label='官渡之战', eventId='guandu'), dict(label='渭南之战', eventId='tongguan')]),
        dict(title='留守汉中，战死定军山',
             text='张鲁投降后，夏侯渊受命督张郃、徐晃等平巴郡，继而在曹操回邺后领军守汉中。刘备进至阳平关，他率将应战，两军相持。219年正月，刘备夜烧营围的鹿角，夏侯渊命张郃守东围，自己带轻兵守南围。张郃作战受挫，夏侯渊分一半所部援助，随后遭刘备军袭击战死。《黄忠传》从刘备军一方补记，黄忠率部在定军山进攻并斩了夏侯渊。',
             refs=[ZHANG_LU, HOLD_HANZHONG, Q('v009-b0010', '二十三年，劉備軍陽平關，淵率諸將拒之，相守連年。'),
                   Q('v009-b0010', '備夜燒圍鹿角。淵使張郃護東圍，自將輕兵護南圍。'),
                   Q('v009-b0010', '備挑郃戰，郃軍不利。'), DINGJUN, HUANG_ZHONG, Q('v036-b0019', '一戰斬淵，淵軍大敗。')],
             eventLinks=[dict(label='张鲁投降', eventId='zhanglu-surrender'), dict(label='在定军山进攻', eventId='hanzhong')]),
    ],

    careers=[
        dict(id='guandu', when='200年及战后', title='官渡任督军校尉，战后运粮', office='行督军校尉', eventIds=['guandu'],
             text='官渡相持时代理督军校尉；袁绍战败后督三州军粮，接续运送以补曹军所缺。',
             refs=[Q('v001-b0047', '公還軍官渡。紹進保陽武。'), GUANDU, SUPPLY]),
        dict(id='tongguan', when='211年', title='随曹操战于渭南', office='—', eventIds=['tongguan'],
             text='随曹操与韩遂、马超一方在渭南交战，又督朱灵平隃糜、汧两地氐人，后来在安定与曹操会合。',
             refs=[Q('v001-b0076', '十六年春正月'), Q('v001-b0077', '九月，進軍渡渭。'), WEINAN,
                   Q('v009-b0008', '又督朱靈平隃糜、汧氐。與太祖會安定，降楊秋。')]),
        dict(id='longyou', when='214年', title='救祁山，进取陇右', office='假节',
             text='不等邺城回令，先派张郃救祁山；随后击败韩遂，攻下枹罕，分遣诸将进取河关。',
             refs=[Q('v009-b0009', '十九年，趙衢、尹奉等謀討超'), QISHAN, Q('v009-b0009', '大破遂軍，得其旌麾'),
                   Q('v009-b0009', '乃假淵節。'), Q('v009-b0010', '圍枹罕，月餘拔之，斬建'), LONGYOU]),
        dict(id='zhanglu', when='215年', title='张鲁归降后受命领军', office='行都护将军', eventIds=['zhanglu-surrender'],
             text='曹操西征时带领凉州诸将、侯王等与其会于休亭；张鲁归降后督张郃、徐晃等平巴郡。',
             refs=[Q('v001-b0097', '二十年春正月'), Q('v001-b0102', '十一月，魯自巴中將其餘衆降。'),
                   Q('v009-b0010', '淵等將涼州諸將侯王已下，與太祖會休亭。'), ZHANG_LU]),
        dict(id='dingjun', when='219年', title='守汉中，战死定军山', office='—', eventIds=['hanzhong'],
             text='此前曹操回邺后留他守汉中，拜征西将军。刘备军攻围，夏侯渊分兵支援张郃后遭袭，在定军山战死。',
             refs=[HOLD_HANZHONG, Q('v009-b0010', '二十四年正月，備夜燒圍鹿角。'), DINGJUN, HUANG_ZHONG]),
    ],

    records=[
        dict(section='military', when='200年战后', title='接续运送三州军粮', category='军粮转运', careerRef='guandu',
             text='袁绍战败后，曹军仍有粮荒。夏侯渊督运兖、豫、徐三州粮食，使供给接续、军力得以恢复。',
             refs=[SUPPLY]),
        dict(section='military', when='214年', title='急赴祁山解围', category='及时发兵', careerRef='longyou',
             text='判断向邺城请示会贻误救援，便派张郃先行；马超没有接战就退去。',
             refs=[Q('v009-b0009', '比報，叙等必敗，非救急也。'), QISHAN, Q('v009-b0009', '未戰，超走，郃進軍收超軍器械。')]),
        dict(section='setback', when='219年', title='分兵援张郃后战死', category='主将阵亡', careerRef='dingjun', eventIds=['hanzhong'],
             text='东围战事不利，夏侯渊调出一半所部增援，随后遭袭身亡。传文给出了战场次序，没有断言分兵就是失败的唯一原因。',
             refs=[Q('v009-b0010', '備挑郃戰，郃軍不利。'), DINGJUN, Q('v032-b0021', '先主命黃忠乘高鼓譟攻之，大破淵軍')]),
    ],
    sections={
        'civil': {'note': '本传记夏侯渊曾任陈留、颍川太守，却没有交代两郡的具体施政；督三州军粮属于作战补给，见武功一栏。'},
    },

    relations=[
        dict(category='亲族', name='夏侯惇', personId='xiahou-dun', label='同族兄弟',
             text='夏侯渊是夏侯惇的族弟；《魏略》记两人都曾任将军。',
             refs=[ORIGIN, Q('v009-b0003-n01', '時夏侯淵與惇俱爲將軍', '《魏略》')]),
        dict(category='君臣', name='曹操', personId='caocao', label='留守汉中受命',
             text='夏侯渊自曹操起兵时跟随。曹操回邺后留他守汉中，任征西将军。',
             refs=[EARLY, HOLD_HANZHONG]),
        dict(category='同僚', name='张郃', personId='zhang-he', label='多次并肩作战',
             text='夏侯渊曾派张郃先赴祁山；汉中决战时张郃守东围不利，夏侯渊分兵相助。',
             refs=[QISHAN, Q('v009-b0010', '淵使張郃護東圍'), DINGJUN]),
        dict(category='敌对', name='黄忠', personId='huang-zhong', label='定军山交战',
             text='《先主传》记刘备命黄忠居高进攻，《黄忠传》记这一战斩了夏侯渊。',
             refs=[Q('v032-b0021', '先主命黃忠乘高鼓譟攻之，大破淵軍'), Q('v036-b0019', '一戰斬淵，淵軍大敗。')]),
    ],

    assessment=[
        dict(title='陈寿：亲旧受重，确有勋绩',
             text='陈寿指出夏侯、曹氏世代通婚，夏侯渊等人因亲旧受重用；同时肯定他们建立的勋业。',
             refs=[Q('v009-b0059', '夏侯、曹氏，世爲婚姻'), Q('v009-b0059', '貴重於時，左右勳業，咸有効勞。')]),
    ],

    readingNotes=[
        dict(title='告诫与战败经过分开看',
             text='陈寿在夏侯渊战死之后，回叙曹操曾提醒他不可只靠勇猛。评读战败，可以把这条统兵告诫与本传所记的分兵、《先主传》所记的争夺高地分别对照。',
             refs=[WARNING, DINGJUN, Q('v032-b0021', '淵將兵來爭其地。先主命黃忠乘高鼓譟攻之')]),
    ],

    sourceScope='以卷九《夏侯渊传》为基础，参看卷一《武帝纪》、卷四配享诏、卷三十二《先主传》和卷三十六《黄忠传》。本页不声称穷尽全书所有提及夏侯渊之处。',
)
