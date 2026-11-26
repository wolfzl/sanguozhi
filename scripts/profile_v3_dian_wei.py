"""典韦：v3 C 级“新建人物”样例（docs/guides/person-template-v3.md §7.1）。

本书原来没有典韦的人物页。种子里的 `new` 字段让生成脚本新建页面，
`eventRoles` 把他登记为既有事件的参与者，从而与事件页互相链接。
"""
from profile_v3 import Q

ORIGIN = Q('v018-b0033', '典韋，陳留己吾人也。')
PUYANG = Q('v018-b0033', '韋手持十餘戟，大呼起，所抵無不應手倒者。布眾退。')
DUWEI = Q('v018-b0033', '拜韋都尉，引置左右，將親兵數百人，常繞大帳。')
XIAOWEI = Q('v018-b0033', '遷為校尉。')
WAN_YEAR = Q('v001-b0035', '二年春正月，公到宛。張繡降，旣而悔之，復反。')
DEATH = Q('v018-b0034', '韋復前突賊，殺數人，創重發，瞋目大罵而死。')
SHRINE = Q('v004-b0010', '武猛校尉典韋於太祖廟庭')

PROFILE = dict(
    id='dian-wei',
    tier='C',
    reading=['018'],
    new=dict(name='典韦', faction='曹魏', period='汉末—197年', aliases=['典君'], tags=['宛城', '濮阳', '双戟']),
    eventRoles=[('yanzhou-struggle', '濮阳募陷阵，击退吕布'), ('wancheng', '守营门战死')],
    lead='曹操的贴身护卫将领，以膂力和双戟闻名。濮阳之战率应募者击退吕布军；197年张绣在宛城反叛袭营，他死守营门、力战而死，曹操得以脱身。',
    role='曹操帐下亲卫校尉',

    facts=[
        dict(key='lifespan', label='生卒年', value='生年未详—197年',
             text='本传未记生年。宛城之变在建安二年（197）正月，见《武帝纪》；典韦死于此役。',
             refs=[WAN_YEAR, DEATH]),
        dict(key='hometown', label='籍贯', value='陈留郡己吾县',
             text='陈留己吾人；死后曹操遣人归葬襄邑。',
             refs=[ORIGIN, Q('v018-b0034', '遣歸葬襄邑')]),
        dict(key='identity', label='主要身份', value='曹操的亲卫将领',
             text='濮阳战后被引置曹操左右，统领亲兵数百人环卫大帐。',
             refs=[DUWEI]),
        dict(key='office', label='最高官职', value='校尉（武猛校尉）',
             text='由司马、都尉迁为校尉；243年配享太庙的诏书称他“武猛校尉”。',
             refs=[XIAOWEI, SHRINE]),
        dict(key='posthumous', label='身后称号', value='无谥号记载；243年配享曹操庙庭',
             text='本书没有典韦的谥号。齐王曹芳正始四年（243），典韦与曹真、夏侯渊等人一起配享太祖庙庭。',
             refs=[SHRINE]),
        dict(key='deeds', label='代表事迹', items=['濮阳击退吕布', '宛城死守营门'],
             text='濮阳击退吕布、宛城死守营门。',
             refs=[PUYANG, Q('v018-b0034', '韋戰於門中，賊不得入。')]),
    ],

    intro=[
        dict(title='以勇力进入曹营',
             text='典韦是陈留己吾人，相貌魁梧，膂力过人。他曾替人报仇，独自刺杀富春长李永后从容脱身，从此为豪杰所知。张邈起兵时他入伍，后归夏侯惇部下，因屡次斩首立功拜司马。曹操与吕布在濮阳交战，形势危急，典韦率应募陷阵的数十人冲上前，手持十余支戟大呼突击，击退吕布军，曹操才得以撤出。此后他被拜为都尉，统领亲兵护卫大帐，军中称“帐下壮士有典君，提一双戟八十斤”。',
             refs=[ORIGIN, Q('v018-b0033', '形貌魁梧，旅力過人'), Q('v018-b0033', '懷匕首入殺永'), Q('v018-b0033', '後屬夏侯惇，數斬首有功，拜司馬。'),
                   PUYANG, DUWEI, Q('v018-b0033', '帳下壯士有典君，提一雙戟八十斤。')],
             eventLinks=[dict(label='濮阳交战', eventId='yanzhou-struggle')]),
        dict(title='宛城之变',
             text='197年张绣在宛城降而复叛，夜袭曹营。曹操战败轻骑撤走，典韦在营门死战，部下死伤殆尽，他身被数十创仍挟杀两敌，最后瞋目大骂而死，叛军这才敢上前。曹操退到舞阴，听说典韦战死后流泪，募人寻回遗体，亲自临哭，归葬襄邑，此后每过其地都要祭祀，又先后任用他的儿子典满为郎中、司马。四十多年后的243年，典韦与曹真、夏侯渊等人一同配享曹操庙庭。',
             refs=[WAN_YEAR, Q('v018-b0034', '太祖出戰不利，輕騎引去。韋戰於門中，賊不得入。'), Q('v018-b0034', '韋被數十創'), DEATH,
                   Q('v018-b0034', '聞韋死，為流涕，募間取其喪，親自臨哭之'), Q('v018-b0034', '車駕每過，常祠以中牢。'),
                   Q('v018-b0034', '太祖思韋，拜滿為司馬，引自近。'), SHRINE],
             eventLinks=[dict(label='宛城降而复叛', eventId='wancheng')]),
    ],

    careers=[
        dict(id='youth', when='早年，确年未载', title='为人报仇，为豪杰所识', office='未仕',
             text='替襄邑刘氏刺杀富春长李永，突围脱身。',
             refs=[Q('v018-b0033', '懷匕首入殺永'), Q('v018-b0033', '由是為豪傑所識。')]),
        dict(id='enlist', when='初平年间（190—193），确年未载', title='从军，拜司马', office='司马',
             text='张邈起兵时为士卒，后属夏侯惇，屡立斩首之功。',
             refs=[Q('v018-b0033', '初平中，張邈舉義兵，韋為士'), Q('v018-b0033', '後屬夏侯惇，數斬首有功，拜司馬。')]),
        dict(id='puyang', when='194年', title='濮阳陷阵，击退吕布', office='都尉，后迁校尉', eventIds=['yanzhou-struggle'],
             text='曹操在濮阳夜袭吕布别屯后遭反击，典韦率应募者陷阵击退敌军；战后统领亲兵护卫大帐。',
             refs=[Q('v018-b0033', '太祖討呂布於濮陽。'), PUYANG, DUWEI, XIAOWEI]),
        dict(id='wancheng', when='197年', title='宛城死守营门', office='—', eventIds=['wancheng'],
             text='张绣反叛袭营，典韦死守营门，力战而死。',
             refs=[WAN_YEAR, Q('v018-b0034', '韋戰於門中，賊不得入。'), DEATH]),
        dict(id='honor', when='243年', title='配享太祖庙庭', office='—',
             text='正始四年诏以典韦等人配享曹操庙庭。',
             refs=[SHRINE]),
    ],

    records=[
        dict(section='military', when='194年', title='濮阳陷阵', category='突击解围', careerRef='puyang', eventIds=['yanzhou-struggle'],
             text='在箭如雨下时等敌人逼近到五步才起身突击，击退吕布军，掩护曹操撤出战场。',
             refs=[Q('v018-b0033', '「五步乃白。」'), PUYANG, Q('v018-b0033', '會日暮，太祖乃得引去。')]),
        dict(section='military', when='197年', title='宛城护主', category='护卫断后', careerRef='wancheng', eventIds=['wancheng'],
             text='死守营门拖住叛军，曹操得以轻骑脱身。',
             refs=[Q('v018-b0034', '太祖出戰不利，輕騎引去。韋戰於門中，賊不得入。')]),
        dict(section='setback', when='197年', title='宛城战死', category='殉职', careerRef='wancheng', eventIds=['wancheng'],
             text='营门被叛军从他门绕入，左右死伤殆尽，典韦重伤战死。这是宛城之变中曹军的重大损失，不是他个人的指挥失误。',
             refs=[Q('v018-b0034', '兵遂散從他門併入。'), Q('v018-b0034', '左右死傷者略盡。'), DEATH]),
    ],
    sections={
        'civil': {'note': '典韦一直担任曹操的亲卫武官，本书没有他参与治理或谋议的记载。'},
    },

    assessment=[
        dict(title='陈寿：比作樊哙',
             text='陈寿把许褚、典韦并论，说他们护卫曹操左右、折冲御敌，好比汉初的樊哙。',
             refs=[Q('v018-b0050', '許褚、典韋折衝左右，抑亦漢之樊噲也。')]),
    ],

    relations=[
        dict(category='君臣', name='曹操', personId='caocao', label='亲卫与主君',
             text='濮阳战后被引置左右护卫大帐；典韦战死后，曹操流涕临哭，经过襄邑时常以中牢祭祀，并任用其子典满。',
             refs=[DUWEI, Q('v018-b0034', '車駕每過，常祠以中牢。'), Q('v018-b0034', '太祖思韋，拜滿為司馬，引自近。')]),
        dict(category='敌对', name='张绣', personId='zhang-xiu', label='宛城反叛袭营',
             text='张绣先降后叛，袭击曹营，典韦死于此役。',
             refs=[Q('v018-b0034', '後十餘日，繡反，襲太祖營')]),
        dict(category='同僚', name='许褚', label='并称的护卫名将',
             text='陈寿把二人并论。裴松之认为许褚功劳超过典韦，却没有配享太庙，不合情理。',
             refs=[Q('v018-b0050', '許褚、典韋折衝左右'), Q('v004-b0011-n01', '褚之功烈有過典韋，今祀韋而不及褚，文所未達也。', '裴松之案')]),
    ],

    readingNotes=[
        dict(title='“一双戟八十斤”是军中歌谣',
             text='这句话出自军中流传的歌谣，用来形容他的勇力，不宜当作兵器重量的实测记录。',
             refs=[Q('v018-b0033', '軍中為之語曰：「帳下壯士有典君，提一雙戟八十斤。」')]),
    ],

    glossary=[
        ('陷陈', '冲入敌阵。“陈”同“阵”。'),
        ('中牢', '祭祀所用的猪、羊二牲，规格低于太牢。'),
    ],

    sourceScope='以卷十八《典韦传》正文为基础，参看卷一《武帝纪》宛城之变的纪年、卷四正始四年配享诏和裴松之对配享名单的议论。本传无裴注。本页不声称穷尽全书所有提及典韦之处。',
)
