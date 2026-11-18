"""陈宫：以卷七《吕布臧洪传》附传及相关记载为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v007-b0016-n01', '陳宮字公臺，東郡人也。', '《典略》')
CHANGE = Q('v007-b0016-n01', '及天下亂，始隨太祖，後自疑，乃從呂布，爲布畫策，布每不從其計。', '《典略》')
PERSUADE = Q('v007-b0008', '今州軍東征，其處空虛，呂布壯士，善戰無前，若權迎之，共牧兖州')
DONG_COMMAND = Q('v007-b0008', '太祖初使宮將兵留屯東郡，遂以其衆東迎布爲兖州牧，據濮陽。')
YAN_LOSS = Q('v007-b0008', '二年間，太祖乃盡復收諸城，擊破布於鉅野。布東奔劉備。')
BLOCK_SURRENDER = Q('v007-b0014', '布欲降，陳宮等自以負罪深，沮其計。')
CAPTURE = Q('v007-b0014', '太祖塹圍之三月，上下離心，其將侯成、宋憲、魏續縛陳宮，將其衆降。')
DEATH = Q('v007-b0014', '布與宮、順等皆梟首送許，然後葬之。')
FAMILY = Q('v007-b0016', '太祖召養其母終其身，嫁其女。')
YEAR = Q('v007-b0014', '建安三年，布復叛爲術，遣高順攻劉備於沛，破之。')

PROFILE = dict(
    id='chen-gong', tier='C', reading=['007'],
    new=dict(name='陈宫', courtesy='公台', faction='汉末', period='汉末—198年',
             aliases=[], tags=['兖州', '吕布', '下邳']),
    eventRoles=[('yanzhou-struggle', '劝张邈迎吕布入兖州'), ('xiapi', '阻吕布投降，被缚处死')],
    lead='陈宫早年在曹操麾下领兵，194年乘曹操东征之机，劝张邈迎吕布入兖州。吕布败走后他仍为其谋划；198年曹操围下邳，陈宫被吕布部将捆缚献降，随后与吕布、高顺等一同被杀。',
    role='曾从曹操的吕布谋臣',

    facts=[
        dict(key='lifespan', label='生卒年', value='生年未详—198年',
             text='史书不记陈宫生年。卷七将曹操攻下邳、陈宫被擒杀的经过记于建安三年（198）。',
             refs=[YEAR, DEATH]),
        dict(key='hometown', label='籍贯', value='东郡',
             text='裴注引《典略》称陈宫是东郡人，未记县名。', refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='曹操旧将，后为吕布领兵画策',
             text='正文记曹操曾使他将兵屯东郡；裴注引《典略》称他转从吕布并为其出谋划策。',
             refs=[DONG_COMMAND, CHANGE]),
        dict(key='office', label='最高官职', value='本书未载确切官号',
             text='卷七称陈宫为“太祖将”，记他在东郡领兵，后来追随吕布，未明载其具体官号。',
             refs=[Q('v007-b0008', '太祖將陳宮'), DONG_COMMAND, CHANGE]),
        dict(key='posthumous', label='身后称号', value='本书未载谥号',
             text='正文记陈宫被杀后首级送许，随后安葬，没有记载谥号。',
             refs=[DEATH]),
        dict(key='deeds', label='代表事迹', items=['劝张邈迎吕布', '濮阳迎立吕布', '下邳阻降'],
             text='说服张邈迎吕布，率原部迎吕布为兖州牧、占据濮阳；吕布被围于下邳时一度欲降，陈宫等予以劝阻。',
             refs=[PERSUADE, Q('v007-b0008', '邈從之。'), DONG_COMMAND, BLOCK_SURRENDER]),
    ],

    intro=[
        dict(title='乘兖州空虚迎吕布',
             text='裴注引《典略》称陈宫字公台，东郡人，早年结交不少知名士人。曹操曾让他领兵驻守东郡。194年曹操再攻陶谦，兖州兵马在外，陈宫与张超等密谋反曹。他劝张邈利用兖州空虚的时机，迎吕布入兖州，先共同控制州中，再看天下形势如何变化。张邈听从，陈宫便率原部迎吕布为兖州牧。诸郡县大多响应，只有鄄城、东阿、范仍守曹操。双方在濮阳相持百余日，曹操后来陆续夺回失地，吕布败走，投奔刘备。',
             refs=[ORIGIN, Q('v007-b0016-n01', '少與海內知名之士皆相連結。', '《典略》'),
                   Q('v007-b0008', '興平元年，太祖復征謙'), PERSUADE, DONG_COMMAND,
                   Q('v007-b0008', '郡縣皆應，唯鄄城、東阿、范爲太祖守。'),
                   Q('v007-b0008', '太祖軍不利，相持百餘日。'), YAN_LOSS],
             eventLinks=[dict(label='迎吕布入兖州', eventId='yanzhou-struggle')]),
        dict(title='下邳被围与败亡',
             text='198年曹操亲征吕布。曹军推进到下邳，吕布一度想降，陈宫等自觉负罪已深，阻止了他。吕布出战失利，退回城中，又未能得到袁术救援。久围之下，部将侯成、宋宪、魏续捆缚陈宫，率部降曹；吕布随后也被擒，陈宫与吕布、高顺等一同被杀。按卷七正文，曹操曾问陈宫是否希望母亲和女儿活下来，陈宫将母亲的生死托付给曹操。曹操后来供养其母至终，替他的女儿安排婚嫁。',
             refs=[YEAR, Q('v007-b0014', '太祖自征布，至其城下'), BLOCK_SURRENDER,
                   Q('v007-b0014', '敗走，還保城，不敢出。術亦不能救。'), CAPTURE, DEATH,
                   Q('v007-b0016', '問宮欲活老母及女不？'), Q('v007-b0016', '老母在公，不在宮也。'), FAMILY],
             eventLinks=[dict(label='下邳', eventId='xiapi')]),
    ],

    careers=[
        dict(id='dong-command', when='转从吕布前，确年未载', title='在曹操麾下领兵屯东郡', office='曹操部将',
             text='曹操曾命陈宫领兵驻屯东郡。裴注引《典略》说，他天下大乱后开始追随曹操。',
             refs=[DONG_COMMAND, CHANGE]),
        dict(id='yanzhou', when='194年', title='说张邈迎吕布，据濮阳', office='—', eventIds=['yanzhou-struggle'],
             text='曹操东征陶谦时，陈宫与张超等谋反，劝张邈迎吕布，又以所部迎吕布为兖州牧。据濮阳后，多数郡县响应。',
             refs=[Q('v007-b0008', '興平元年，太祖復征謙'), PERSUADE, DONG_COMMAND,
                   Q('v007-b0008', '郡縣皆應，唯鄄城、東阿、范爲太祖守。')]),
        dict(id='juyeyanzhou', when='195年', title='与吕布再战兖州失利', office='—', eventIds=['yanzhou-struggle'],
             text='吕布为薛兰等解围不成，后来与陈宫率军再战，被曹操伏兵击破；曹操收复诸城，吕布转投刘备。',
             refs=[Q('v001-b0027', '布復從東緍與陳宮將萬餘人來戰，時太祖兵少，設伏，縱奇兵擊，大破之。'), YAN_LOSS]),
        dict(id='xiapi', when='198年', title='阻吕布投降，下邳被擒杀', office='—', eventIds=['xiapi'],
             text='曹操进围下邳，陈宫等阻止吕布归降。城中部将反叛，陈宫被缚降曹，最终与吕布、高顺一并被杀。',
             refs=[YEAR, BLOCK_SURRENDER, CAPTURE, DEATH]),
    ],

    records=[
        dict(section='military', when='194年', title='把握曹操东征的空档', category='谋划用兵', careerRef='yanzhou', eventIds=['yanzhou-struggle'],
             text='陈宫说服张邈并率原部迎吕布，曹操不得不从徐州回军。兖州多郡县虽一度响应，鄄城等三地仍为曹操所守。',
             refs=[PERSUADE, DONG_COMMAND, Q('v007-b0008', '郡縣皆應，唯鄄城、東阿、范爲太祖守。太祖引軍還')]),
        dict(section='setback', when='198年', title='阻降后被部将捆缚', category='围城败亡', careerRef='xiapi', eventIds=['xiapi'],
             text='陈宫等阻止吕布降曹，却未能改变城外无援、城内部将离心的局面。最终是吕布部将先缚陈宫、率众归降。',
             refs=[BLOCK_SURRENDER, Q('v007-b0014', '術亦不能救。'), CAPTURE, DEATH]),
    ],
    sections={
        'civil': {'note': '陈宫的主要记载围绕兖州结盟与下邳军议；本书未载他任郡县长官或主持民政的事迹。'},
    },

    relations=[
        dict(category='旧主', name='曹操', personId='caocao', label='曾受命领兵，后遭擒杀',
             text='曹操曾使陈宫屯东郡，陈宫后来迎吕布反曹；陈宫败亡后，曹操供养其母，并替他的女儿安排婚事。',
             refs=[DONG_COMMAND, DEATH, FAMILY]),
        dict(category='君臣', name='吕布', personId='lv-bu', label='迎入兖州，为其画策',
             text='陈宫迎吕布为兖州牧，转为其出谋、领兵；裴注引《典略》说吕布常不采纳他的建议。',
             refs=[DONG_COMMAND, CHANGE]),
        dict(category='同僚', name='张邈', label='合谋迎吕布入兖州',
             text='曹操东征陶谦时，陈宫劝张邈趁兖州空虚接应吕布，张邈采纳此议。',
             refs=[PERSUADE, Q('v007-b0008', '邈從之。')]),
    ],

    readingNotes=[
        dict(title='下邳的出城、守城之议有不同写法',
             text='裴注引《英雄记》说，吕布打算留陈宫、高顺守城，亲率骑兵截断曹操粮道，妻子以两将素有不和劝阻。《魏氏春秋》则将城内外策应之议归给陈宫，说吕布原已同意，妻子因不信陈宫而反对。两说都没有记这项安排实际付诸行动。',
             refs=[Q('v007-b0014-n02', '布欲令陳宮、高順守城，自將騎斷太祖糧道。', '《英雄记》'),
                   Q('v007-b0014-n02', '宮、順素不和', '《英雄记》'),
                   Q('v007-b0014-n02', '若將軍以步騎出屯，爲勢於外，宮將餘衆閉守於內', '《魏氏春秋》'),
                   Q('v007-b0014-n02', '布乃止。', '《魏氏春秋》')]),
    ],
    sourceScope='以卷七《吕布臧洪传》陈宫附传、张邈与吕布事迹为主，参看卷一《武帝纪》；籍贯、字和下邳军议的补充来自裴注所引各书。本页不声称穷尽全书所有提及陈宫之处。',
)
