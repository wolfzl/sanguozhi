"""张角：v3 模版 C 级样例（docs/guides/person-template-v3.md）。

本书没有张角传，事迹散见于《孙坚传》正文和裴注引文；示范“无本传、散见记载”的写法。
"""
from profile_v3 import Q

RISE = Q('v046-b0004', '中平元年，黃巾賊師張角起於魏郡。')
ORGANIZE = Q('v046-b0004', '託有神靈，遣八使以善道教化天下，而潛相連結，自稱黃天泰平。')
OUTBREAK = Q('v046-b0004', '三月甲子，三十六（萬）一旦俱發，天下響應，燔燒郡縣，殺害長吏。')
TITLE = Q('v046-b0004-n01', '角稱天公將軍，角弟寶稱地公將軍，寶弟梁稱人公將軍。', '《献帝春秋》')
TAIPING = Q('v008-b0047-n01', '光和中，東方有張角', '《典略》')
DAO = Q('v008-b0047-n01', '角為太平道', '《典略》')
FUSHUI = Q('v008-b0047-n01', '師持九節杖為符祝，教病人叩頭思過，因以符水飲之', '《典略》')
KILLED = Q('v008-b0047-n01', '後角被誅，脩亦亡。', '《典略》')
SUPPRESS = Q('v046-b0004', '漢朝遣車騎將軍皇甫崧、中郎將朱儁將兵討擊之。')
WAN = Q('v046-b0004', '汝穎賊困迫，走保宛城。堅身當一面，登城先入，衆乃蟻附，遂大破之。')

PROFILE = dict(
    id='zhang-jiao',
    tier='C',
    reading=['046', '008'],
    lead='汉末太平道首领、黄巾起事的组织者。他派使者传道、联结信众，184年黄巾在各地同时起事，震动东汉；本书没有他的本传，事迹散见于《孙坚传》和裴注所引诸书。',
    role='太平道首领，黄巾起事组织者',

    facts=[
        dict(key='lifespan', label='生卒年', value='生卒年不详',
             text='本书只记他184年起事；裴注引《典略》说他后来被诛，没有年月。',
             refs=[RISE, KILLED]),
        dict(key='hometown', label='籍贯', value='本书未详（起事于魏郡）',
             text='本书未记籍贯，《孙坚传》只说他“起于魏郡”。不据外书补写。',
             refs=[RISE]),
        dict(key='identity', label='主要身份', value='太平道首领、黄巾“贼师”',
             text='《典略》称他传太平道；《孙坚传》称“黄巾贼师”，这是站在汉朝立场的称呼。',
             refs=[DAO, RISE]),
        dict(key='office', label='最高官职', value='自称天公将军',
             text='没有汉朝官职记载。裴注引《献帝春秋》记他自称天公将军，弟张宝、张梁分称地公、人公将军。',
             refs=[TITLE]),
        dict(key='posthumous', label='身后称号', value='本书未载',
             text='本书没有谥号或追封记载，只有《典略》“后角被诛”一句。',
             refs=[KILLED]),
        dict(key='names', label='常见称谓', value='黄巾贼师、天公将军',
             text='正文称“黄巾贼师”；《献帝春秋》记其自号“天公将军”。',
             refs=[RISE, TITLE]),
        dict(key='deeds', label='代表事迹', items=['传播太平道', '遣使联众', '发动黄巾起事'],
             text='传播太平道，遣使在各地传道、联结信众，发动黄巾起事。',
             refs=[DAO, ORGANIZE, OUTBREAK]),
    ],

    intro=[
        dict(title='太平道与黄巾起事',
             text='张角是汉末太平道的首领。裴注引《典略》说，光和年间东方有张角，传太平道：师者持九节杖用符祝祷，教病人叩头思过，再给符水饮用。中平元年（184），他在魏郡起事，托言神灵，派八名使者以“善道”教化天下，暗中联结信众，三月甲子各地同时发动，焚烧郡县、杀害长吏。裴注引《献帝春秋》说，他自称天公将军，弟张宝、张梁分称地公、人公将军。',
             refs=[TAIPING, FUSHUI, RISE, ORGANIZE, OUTBREAK, TITLE],
             eventLinks=[dict(label='魏郡起事', eventId='yellow-turbans')]),
        dict(title='起事之后',
             text='朝廷派皇甫嵩、朱儁讨击，孙坚、曹操都参战；汝颍一带的黄巾被迫退保宛城，后被攻破。张角本人的结局，本书只有《典略》“后角被诛”一句，没有时间和经过。《九州春秋》又说，张角起事时，黑山、白波等部也各自起兵，大者两三万人，朝廷未能讨平，转而遣使招抚。书中把这些部众写作各自起兵，没有说他们都受张角指挥。',
             refs=[SUPPRESS, Q('v046-b0004', '儁表請堅爲佐軍司馬'), Q('v001-b0003', '光和末，黃巾起。拜騎都尉，討潁川賊。'),
                   WAN, KILLED,
                   Q('v008-b0042-n01', '張角之反也，黑山、白波', '《九州春秋》'), Q('v008-b0042-n01', '等各起兵，大者二三萬，小者不減數千', '《九州春秋》'),
                   Q('v008-b0042-n01', '靈帝不能討，乃遣使拜楊鳳為黑山校尉', '《九州春秋》')]),
    ],

    careers=[
        dict(id='taiping', when='光和年间（178—184）', title='传播太平道', office='无',
             text='以符水治病、教人叩头思过的方式传道，吸引信众。',
             refs=[TAIPING, FUSHUI]),
        dict(id='organize', when='184年以前，确年未载', title='遣八使联结各地', office='无',
             text='托言神灵，派八名使者分赴各地，以“善道”教化，暗中联络。',
             refs=[ORGANIZE]),
        dict(id='uprising', when='184年', title='魏郡起事', office='自称天公将军', eventIds=['yellow-turbans'],
             text='三月甲子各地同时发动，焚烧郡县、杀害长吏；与弟张宝、张梁分称天公、地公、人公将军。',
             refs=[RISE, OUTBREAK, TITLE]),
        dict(id='suppressed', when='184年起事后，确年未载', title='遭讨击，被诛', office='—',
             text='朝廷派皇甫嵩、朱儁讨击，汝颍一带的黄巾被打败；张角被诛，具体时间、地点本书未载。',
             refs=[SUPPRESS, WAN, KILLED]),
    ],

    # 模式二：本书只明确记载魏郡起事，传道驻地和被诛地点未详。
    # span 仅供地图取景；被诛年份仍以 when 的“确年未载”为准。
    trajectory=dict(
        phases=[
            dict(id='taiping', title='传道与联结信众', when='光和年间至起事前，确年未载', span=(178, 184),
                 careers=['taiping', 'organize'],
                 unmappedReason='传道范围仅记“东方”，未载具体驻地。'),
            dict(id='uprising', title='魏郡起事', when='184年', span=(184, 184),
                 careers=['uprising'],
                 place=dict(name='魏郡', query='魏郡', province='河北', mapYear=184, approx=True)),
            dict(id='suppressed', title='遭讨击与被诛', when='184年起事后，确年未载', span=(184, 184),
                 careers=['suppressed'],
                 unmappedReason='本书未载张角被诛的具体时间、地点。'),
        ],
    ),

    records=[
        dict(section='military', when='184年', title='动员多地同时起事', category='组织动员', careerRef='uprising', eventIds=['yellow-turbans'],
             text='通过宗教传播事先联结各地信众，在同一天发动，造成“天下响应”的局面。本书没有记载张角本人指挥的具体战斗。',
             refs=[ORGANIZE, OUTBREAK]),
        dict(section='setback', when='184年起事后', title='起事被镇压，本人被诛', category='败亡', careerRef='suppressed',
             text='官军讨击之下，汝颍黄巾退保宛城后被攻破；张角本人被诛。裴注另载黑山等武装，朝廷无法讨平，只能派使者招抚。',
             refs=[WAN, KILLED,
                   Q('v008-b0042-n01', '靈帝不能討，乃遣使拜楊鳳為黑山校尉', '《九州春秋》')]),
    ],
    sections={
        'civil': {'note': '张角不是朝廷或地方官员，本书没有可以称作“文治”的记载；他组织信众的方式见“生平履历”和“阅读提示与史料辨析”。'},
    },

    relations=[
        dict(category='亲族', name='张宝、张梁', label='两个弟弟，同称将军',
             text='《献帝春秋》记张角自称天公将军，弟张宝称地公将军，张梁称人公将军。',
             refs=[TITLE]),
        dict(category='敌对', name='孙坚', personId='sun-jian', label='随朱儁讨黄巾起家',
             text='孙坚受朱儁表荐为佐军司马，招募淮泗精兵讨击黄巾，攻宛城时先登，因功拜别部司马。',
             refs=[Q('v046-b0004', '儁表請堅爲佐軍司馬'), Q('v046-b0004', '堅身當一面，登城先入')]),
        dict(category='敌对', name='曹操', personId='caocao', label='以骑都尉讨颍川黄巾',
             text='黄巾起事后，曹操拜骑都尉，讨伐颍川的黄巾。',
             refs=[Q('v001-b0003', '光和末，黃巾起。拜騎都尉，討潁川賊。')]),
    ],

    readingNotes=[
        dict(title='“三十六（萬）”的校勘括号',
             text='正文作“三十六（萬）一旦俱发”，括号是底本的校勘标记，表示“萬”字有疑问。页面只说“各地同时发动”，不据此写成“三十六万人”。',
             refs=[OUTBREAK]),
        dict(title='《典略》如何记符水治病',
             text='《典略》记太平道把病愈解释为信道，把不愈归为不信。这是史书对太平道做法的转述。后文“实无益于治病”紧接张脩所传五斗米道的叙述，不能单独拿来当作《典略》对张角的评语。',
             refs=[Q('v008-b0047-n01', '則云此人信道，其或不愈，則為不信道。', '《典略》'),
                   Q('v008-b0047-n01', '故號曰五斗米師。實無益於治病，但為淫妄', '《典略》')]),
    ],

    glossary=[
        ('太平道', '张角所传的道派，以符水治病、叩头思过为主要方式。'),
        ('长吏', '在这里指郡县的长官或地位较高的属吏。'),
    ],

    sourceScope='本书无张角传。本页依据卷四十六《孙坚传》正文及裴注引《献帝春秋》、卷八《张鲁传》《张燕传》裴注引《典略》《九州春秋》，并参看卷一《武帝纪》曹操讨黄巾的记载。本页不声称穷尽全书所有提及张角之处。',
)
