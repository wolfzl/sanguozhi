"""廖化：关羽旧属与蜀汉末年的边军将领。"""
from profile_v3 import Q

ORIGIN = Q('v045-b0014', '廖化字元儉，本名淳，襄陽人也。')
GUAN = Q('v045-b0014', '為前將軍關羽主簿，羽敗，屬吳。')
RETURN = Q('v045-b0014', '思歸先主，乃詐死，時人謂為信然，因攜持老母晝夜西行。')
YILING = Q('v045-b0014', '會先主東征，遇於秭歸。先主大悅，以化為宜都太守。')
PROMOTION = Q('v045-b0014', '稍遷至右車騎將軍，假節，領并州刺史，封中鄉侯')
AID = Q('v044-b0024', '乃遣右車騎廖化詣沓中為維援')
DEFENSE = Q('v044-b0024', '維、化亦捨陰平而退。適與翼、厥合，皆退保劍閣以拒會。')
DEATH = Q('v045-b0015', '咸熙元年春，化、預俱內徙洛陽，道病卒。')
CRITICISM = Q('v045-b0014-n01', '智不出敵，而力少於寇，用之無厭，何以能立？', '《汉晋春秋》')
ADVANCE = Q('v033-b0042', '於是遣左右車騎將軍張翼、廖化、輔國大將軍董厥等拒之。')

PROFILE = dict(
    id='liao-hua', tier='C', reading=['045', '044'],
    new=dict(name='廖化', courtesy='元俭', faction='蜀汉', period='汉末—264年', aliases=['廖淳', '廖元俭'], tags=['荆州', '秭归', '剑阁']),
    eventRoles=[('jingzhou', '关羽败后属吴'), ('yiling', '东征时归蜀，任宜都太守'), ('fall-shu', '奉命援姜维，合守剑阁')],
    lead='廖化原是关羽的主簿，荆州失守后脱吴归蜀，历任宜都太守、右车骑将军。蜀亡前他奉命援助姜维，后与诸将合守剑阁；蜀亡后在内迁途中病逝。',
    role='蜀汉右车骑将军',
    facts=[
        dict(key='lifespan', label='生卒年', value='生年未详—264年', text='本书未记生年。魏咸熙元年春，廖化与宗预内迁洛阳，途中病卒。', refs=[DEATH]),
        dict(key='hometown', label='籍贯', value='襄阳', text='本传写襄阳人。', refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='关羽旧属、蜀汉末期将领', text='起初做关羽主簿，后来统军，蜀亡时奉命援助姜维。', refs=[GUAN, PROMOTION, AID]),
        dict(key='office', label='最高官职', value='右车骑将军', text='任过宜都太守、丞相参军、督广武，后任右车骑将军，假节，领并州刺史。', refs=[YILING, Q('v045-b0014', '為丞相參軍，後為督廣武'), PROMOTION]),
        dict(key='title', label='最高爵位', value='中乡侯', text='本传在升任右车骑将军之后记其封中乡侯。', refs=[PROMOTION]),
        dict(key='posthumous', label='身后称号', value='本书未载', text='本传记内迁道中病卒，未记谥号。', refs=[DEATH]),
        dict(key='deeds', label='代表事迹', items=['携母归蜀', '增援姜维', '共守剑阁'], text='携母脱吴；蜀亡前奉命援姜维，后同守剑阁。', refs=[RETURN, AID, DEFENSE]),
    ],
    intro=[
        dict(title='从关羽主簿到右车骑',
             text='廖化本名廖淳，字元俭，是襄阳人。关羽败亡后，他一度属吴；为了重归刘备，他佯称自己已死，带着年老的母亲昼夜向西。在刘备东征时，两人于秭归相遇，刘备任他为宜都太守。刘备去世后，廖化先为丞相参军，后来担任督广武，逐步升到右车骑将军，领并州刺史、封中乡侯。陈寿用“果烈”二字写其声望，并记他的官位与张翼相当，在宗预之上。',
             refs=[ORIGIN, GUAN, RETURN, YILING, Q('v045-b0014', '先主薨，為丞相參軍，後為督廣武'), PROMOTION, Q('v045-b0014', '以果烈稱。官位與張翼齊，而在宗預之右。')],
             eventLinks=[dict(label='关羽败亡', eventId='jingzhou'), dict(label='刘备东征', eventId='yiling')]),
        dict(title='魏军攻蜀与内迁',
             text='263年魏军多路进攻蜀汉，朝廷最初搁置了姜维预作部署的建议，到钟会将向骆谷、邓艾将入沓中才遣廖化前往增援。后来姜维、廖化撤离阴平，与张翼、董厥会合，退守剑阁抵抗钟会。钟会未能攻克剑阁，邓艾却另从阴平进军，攻破绵竹。刘禅向邓艾投降，姜维等奉诏放下兵器。次年春，廖化和宗预被内迁往洛阳，两人在途中病逝。',
             refs=[ADVANCE, Q('v044-b0024', '啟後主寢其事，而群臣不知。'), Q('v044-b0024', '及鐘會將向駱谷，鄧艾將入沓中。'), AID, DEFENSE, Q('v044-b0024', '會不能克，糧運縣遠，將議還歸。'), Q('v044-b0024', '鄧艾自陰平由景谷道傍入，遂破諸葛瞻於綿竹。後主請降於艾'), Q('v044-b0024', '尋被後主敕令乃投戈放甲'), DEATH],
             eventLinks=[dict(label='魏军多路进攻蜀汉', eventId='fall-shu')]),
    ],
    careers=[
        dict(id='jingzhou', when='219年', title='关羽败后属吴', office='此前为关羽主簿', text='廖化原任关羽主簿，关羽在荆州失败后转属吴。', refs=[GUAN], eventIds=['jingzhou']),
        dict(id='yiling', when='221—222年', title='携母归刘备', office='宜都太守', text='在吴佯称已死，带母亲西行；刘备东征时，廖化在秭归遇刘备并获任用。', refs=[RETURN, YILING], eventIds=['yiling']),
        dict(id='promotion', when='刘备去世后，确年未载', title='任丞相参军，后督广武', office='丞相参军、督广武', text='刘备去世后任丞相参军，后来负责督守广武。', refs=[Q('v045-b0014', '先主薨，為丞相參軍，後為督廣武')]),
        dict(id='chengzhong', when='248年', title='奉姜维命筑城于成重山', office='阴平太守', text='据魏方《郭淮传》，姜维西进接应治无戴，留廖化在成重山筑城。郭淮率军进攻廖化，姜维回军相救。', refs=[Q('v026-b0033', '九年，遮塞等屯河關、白土故城'), Q('v026-b0033', '乃西迎治無戴，留陰平太守廖化於成重山築城'), Q('v026-b0033', '淮自率諸軍就攻化等。維果馳還救化')]),
        dict(id='fall', when='263年', title='援姜维，与诸将保剑阁', office='时任右车骑将军', text='廖化此时已升任右车骑将军。魏军攻蜀时奉命赴援，后来和姜维等还保剑阁；蜀廷降魏后，守军奉命解除武装。', refs=[PROMOTION, ADVANCE, AID, DEFENSE, Q('v044-b0024', '後主請降於艾'), Q('v044-b0024', '尋被後主敕令乃投戈放甲')], eventIds=['fall-shu']),
        dict(id='death', when='264年', title='内迁途中病卒', office='—', text='与宗预同被迁往洛阳，途中因病去世。', refs=[DEATH]),
    ],
    records=[
        dict(section='military', when='263年', title='蜀军合守剑阁', category='增援防御', careerRef='fall', eventIds=['fall-shu'], text='廖化受调接应姜维；撤出阴平后与友军会合守剑阁，钟会军未能攻克。', refs=[AID, DEFENSE, Q('v044-b0024', '會不能克')]),
        dict(section='setback', when='263年', title='援军出发时魏兵已近', category='全局败势', careerRef='fall', eventIds=['fall-shu'], text='姜维请求事先分兵守要道，朝廷搁置，到魏军将入才遣廖化接应。剑阁尚能坚守，蜀廷却在邓艾破绵竹后决定投降。', refs=[Q('v044-b0024', '啟後主寢其事，而群臣不知。'), AID, Q('v044-b0024', '鄧艾自陰平由景谷道傍入，遂破諸葛瞻於綿竹。後主請降於艾')]),
    ],
    sections={'civil': {'note': '《廖化传》载他获任宜都太守、领并州刺史，未细叙本人在两职上的施政。'}},
    relations=[
        dict(category='旧主', name='关羽', personId='guanyu', label='早年任其主簿', text='廖化原是前将军关羽的主簿，关羽败亡改变了他的归属。', refs=[GUAN]),
        dict(category='君臣', name='刘备', personId='liubei', label='秭归相遇，任为太守', text='廖化从吴地携母西行回归，在秭归获刘备任用。', refs=[RETURN, YILING]),
        dict(category='同僚', name='姜维', personId='jiang-wei', label='援沓中，同守剑阁', text='蜀亡前受命增援姜维，后同退至剑阁；裴注引《汉晋春秋》另载廖化曾批评姜维屡次用兵。', refs=[AID, DEFENSE, CRITICISM]),
        dict(category='同僚', name='宗预', label='同被内迁洛阳', text='本传记廖化官位在宗预之上；蜀亡后两人同被内迁，途中病故。', refs=[Q('v045-b0014', '官位與張翼齊，而在宗預之右。'), DEATH]),
    ],
    readingNotes=[
        dict(title='对姜维用兵的批评来自裴注', text='“兵不戢，必自焚”见于裴注所引《汉晋春秋》。这段记载把批评放在景耀五年，早于廖化奉命救援姜维，不能由此说他在蜀亡时拒绝增援。', refs=[Q('v045-b0014-n01', '景耀五年，姜維率眾出狄道', '《汉晋春秋》'), CRITICISM, AID]),
        dict(title='“前有王、句，后有张、廖”', text='裴注引《华阳国志》录下时人的并称，把张翼、廖化与较早知名的王平、句扶相提并论。这是一条关于蜀汉将领声望的旁证。', refs=[Q('v043-b0023-n02', '後張翼、廖化並為大將軍，時人語曰：「前有王、句，後有張、廖。」', '《华阳国志》')]),
    ],
    sourceScope='以卷四十五《廖化传》为主，参卷二十六《郭淮传》、卷三十三《后主传》及卷四十四《姜维传》；裴注中的用兵议论与时语另列。本页不声称穷尽全书所有提及廖化之处。',
)
