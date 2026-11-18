"""马腾：西州起事、关中领兵与入朝宿卫。"""
from profile_v3 import Q

NAME = Q('v036-b0013-n01', '騰字壽成，馬援後也。', '《典略》')
HOME = Q('v036-b0013-n01', '後失官，因留隴西，與羌錯居。家貧無妻，遂娶羌女，生騰。', '《典略》')
POVERTY = Q('v036-b0013-n01', '騰少貧無產業，常從彰山中斫材木，負販詣城市，以自供給。', '《典略》')
RISE = Q('v036-b0013', '父騰，靈帝末與邊章、韓遂等俱起事於西州。')
RECRUIT = Q('v036-b0013-n01', '州郡募發民中有勇力者，欲討之，騰在募中。', '《典略》')
EARLY_OFFICE = Q('v036-b0013-n01', '署為軍從事，典領部眾。討賊有功，拜軍司馬，後以功遷偏將軍', '《典略》')
CHANGAN = Q('v036-b0013', '初平三年，遂、騰率眾詣長安。漢朝以遂為鎮西將軍，遣還金城，騰為征西將軍，遣屯郿。')
PLOT = Q('v006-b0012', '侍中馬宇與諫議大夫种邵、左中郎將劉範等謀，欲使騰襲長安，己爲內應，以誅傕等。')
FAILURE = Q('v006-b0012', '騰引兵至長平觀，宇等謀泄，出奔槐里。稠擊騰，騰敗走，還涼州')
BROTHER = Q('v036-b0013-n01', '與鎮西將軍韓遂結為異姓兄弟，始甚相親，後轉以部曲相侵入，更為讎敵。', '《典略》')
FEUD = Q('v036-b0013-n01', '騰攻遂，遂走，合眾還攻騰，殺騰妻子，連兵不解。', '《典略》')
MEDIATION = Q('v036-b0013-n01', '乃使司隸校尉鍾繇、涼州牧韋端和解之。', '《典略》')
HUAILI = Q('v036-b0013-n01', '徵騰還屯槐裏，轉拜為前將軍，假節，封槐裏侯。', '《典略》')
GOVERN = Q('v036-b0013-n01', '待士進賢，矜救民命，三輔甚安愛之。', '《典略》')
BAIQI = Q('v018-b0036', '後張白騎叛於弘農，德復隨騰徵之，破白騎於兩殽間。')
COURT = Q('v036-b0013', '後騰與韓遂不和，求還京畿。於是徵為衛尉，以超為偏將軍，封都亭侯，領騰部曲。')
COURT_YEAR = Q('v036-b0013-n01', '十（五）年，徵為衛尉，騰自見年老，遂入宿衛。', '《典略》')
FAMILY = Q('v036-b0013-n01', '徙其家屬皆詣鄴，惟超獨留。', '《典略》')
REBELLION = Q('v006-b0016', '十六年，超與關中諸將及遂等反，太祖征破之。')
TONGGUAN = Q('v036-b0014', '超既統眾，遂與韓遂合從，及楊秋、李堪、成宜等相結，進軍至潼關。')
END = Q('v006-b0016', '超據漢陽，騰坐夷三族。')

PROFILE = dict(
    id='ma-teng',
    tier='C',
    reading=['036', '006', '031', '018'],
    syncLifespan=True,
    lead='马腾是汉末凉州、关中一带的领兵者，曾与韩遂结盟，又因部曲相争而反目。后来入朝任卫尉，部众由儿子马超接领。马超在关中起兵后，他虽已交出军队，仍遭株连而死。',
    role='关中领兵者、汉廷卫尉',

    facts=[
        dict(key='hometown', label='籍贯', value='本书未详（生于陇西）',
             text='裴注引《典略》记其父失官后留居陇西，在当地生下马腾，未明载马腾的籍贯郡县。《马超传》正文的“右扶风茂陵人”说的是马超。',
             refs=[HOME, Q('v036-b0013', '馬超字孟起，右扶風茂陵人也。')]),
        dict(key='identity', label='主要身份', value='关中领兵者、汉廷卫尉',
             text='汉末在西州起事，后率众赴长安受朝廷任命，再由掌兵转为入朝宿卫。',
             refs=[RISE, CHANGAN, COURT]),
        dict(key='office', label='最高官职', value='卫尉',
             text='正文记在长安受征西将军、后入朝为卫尉；裴注引《典略》另记他曾拜前将军、假节。',
             refs=[CHANGAN, HUAILI, COURT]),
        dict(key='title', label='最高爵位', value='槐里侯',
             text='据裴注引《典略》，还屯槐里时封槐里侯。',
             refs=[HUAILI]),
        dict(key='posthumous', label='身后称号', value='本书未载追谥',
             text='卷六只记马腾坐罪被诛及于三族，未载追谥；槐里侯是生前的封爵。',
             refs=[END, HUAILI]),
        dict(key='lifespan', label='生卒年', value='生卒年不详',
             text='生年未载。卷六明记建安十六年（211）马超起兵，又记马腾此后遭诛，未单独标出马腾被诛的确年。',
             refs=[END, REBELLION]),
        dict(key='names', label='常见称谓', value='马腾、马寿成',
             text='马腾字寿成，见裴注引《典略》。', refs=[NAME]),
        dict(key='deeds', label='代表事迹', items=['西州领兵', '抚恤三辅', '入朝宿卫'],
             text='起事后在关中领兵，裴注记他抚恤三辅百姓；后来受征入朝为卫尉。',
             refs=[RISE, CHANGAN, GOVERN, COURT]),
    ],

    intro=[
        dict(title='西州起事，长安受官',
             text='马腾字寿成。裴注引《典略》说，他年轻时家贫，靠上山伐木卖到城里维持生活；凉州发生叛乱，州郡招募勇士，他应募领兵，以军功升迁。《马超传》正文则记载，汉灵帝末年，他与边章、韩遂等同在西州起事。192年，他与韩遂率众到长安，被任为征西将军，屯兵于郿。后来他与朝中想除掉李傕等人的马宇、刘范等合谋，出兵袭长安，因谋事泄露、战事失利而退回凉州。',
             refs=[NAME, POVERTY, RECRUIT, EARLY_OFFICE, RISE, CHANGAN, PLOT, FAILURE]),
        dict(title='由领兵转入朝廷',
             text='据裴注引《典略》，马腾与韩遂曾结为异姓兄弟，后来因部曲相侵而互相攻打，韩遂反攻时杀了马腾的妻儿。钟繇、韦端奉命调解，马腾还屯槐里，礼待士人并救济百姓。此后马腾求还京畿，朝廷任他为卫尉，由马超接掌部曲。《典略》还说，其他家属随之迁往邺，只有马超留在关中。211年马超与韩遂等在关中起兵，进军潼关抵抗曹操。马腾当时已在朝任职，后来仍因马超起兵被诛，株连三族。',
             refs=[BROTHER, FEUD, MEDIATION, HUAILI, GOVERN, COURT, FAMILY, REBELLION, TONGGUAN, END],
             eventLinks=[dict(label='进军潼关', eventId='tongguan')]),
    ],

    careers=[
        dict(id='western-rise', when='汉灵帝末年，确年未载', title='西州起事，开始领兵', office='军从事、军司马、偏将军（《典略》）',
             text='《马超传》记马腾与边章、韩遂等在西州起事。裴注引《典略》另记他先应募讨乱，领兵后以功升迁。',
             refs=[RISE, RECRUIT, EARLY_OFFICE]),
        dict(id='changan', when='192年', title='长安受官，后来袭长安', office='征西将军', eventIds=['changan-counterattack'],
             text='李傕、郭汜入长安后，马腾与韩遂率众到长安受官。马腾屯郿，后来与马宇、刘范等谋袭长安，事泄后败于樊稠，退回凉州。袭击的确年未载。',
             refs=[Q('v006-b0011', '十日城陷，與布戰城中，布敗走。'), CHANGAN, PLOT, FAILURE]),
        dict(id='huaili', when='建安年间，入朝前', title='与韩遂相攻，还屯槐里', office='前将军、假节、槐里侯（《典略》）',
             text='裴注引《典略》记他与韩遂互相攻杀，钟繇、韦端奉命调解。其后他还屯槐里，礼待士人、救济百姓。',
             refs=[BROTHER, FEUD, MEDIATION, HUAILI, GOVERN]),
        dict(id='court', when='211年以前，确年有校记', title='入朝宿卫，马超接掌部曲', office='卫尉',
             text='马腾与韩遂不和，求还京畿，受任卫尉；马超留在关中接领部曲。裴注引《典略》记其余家属迁到邺。',
             refs=[COURT, COURT_YEAR, FAMILY]),
        dict(id='tongguan', when='211年', title='马超起兵时已在朝任职', office='—', eventIds=['tongguan'],
             text='马超接掌部曲后，与韩遂等屯潼关，后来败于曹操。马腾此前已经入朝，卷六把这场战事记在马超领军之后。',
             refs=[COURT, TONGGUAN, REBELLION]),
        dict(id='execution', when='211年起兵后，确年未载', title='因马超起兵遭株连', office='—',
             text='卷六在马超据汉阳之后记马腾坐罪被诛，株连三族，未标出受刑的具体年月。',
             refs=[REBELLION, END]),
    ],

    records=[
        dict(section='civil', when='驻槐里时，确年未载', title='荐贤抚恤三辅', category='荐贤抚民', careerRef='huaili',
             text='裴注引《典略》记马腾礼待士人、推举贤才、救济百姓，并称三辅百姓感到安定而爱戴他；治理举措的具体细节未载。',
             refs=[HUAILI, GOVERN]),
        dict(section='military', when='建安年间，入朝以前', title='出征讨破张白骑', category='领兵作战',
             text='《庞德传》载张白骑在弘农起兵时，庞德随马腾出征，在两崤之间击败张白骑。至于平阳击郭援，《马超传》写的是马腾遣马超出战，庞德斩郭援。',
             refs=[BAIQI, Q('v036-b0013', '騰遣超隨繇討郭援、高幹於平陽，超將龐德親斬援首。')]),
        dict(section='setback', when='192年到长安后，确年未载', title='谋袭长安未成', category='军事失利', careerRef='changan',
             text='朝中内应的谋划败露，马腾也被樊稠击退，没能同朝臣合力除掉李傕等人。',
             refs=[PLOT, FAILURE]),
        dict(section='setback', when='211年起兵后，确年未载', title='入朝后仍遭族诛', category='家族株连', careerRef='execution',
             text='马腾已任卫尉，所领部众转由马超掌握；当马超与关中诸将起兵，朝中的马腾仍遭株连。',
             refs=[COURT, REBELLION, END]),
    ],

    relations=[
        dict(category='亲族', name='马超', personId='ma-chao', label='父子，交接部曲',
             text='马腾入朝任卫尉，马超代领其部曲。马超后来起兵，马腾因而受株连。',
             refs=[COURT, REBELLION, END]),
        dict(category='同僚', name='韩遂', personId='han-sui', label='从异姓兄弟到仇敌',
             text='两人一同率众到长安。裴注引《典略》称，他们一度结为异姓兄弟，后因部曲相侵而长期交兵。',
             refs=[CHANGAN, BROTHER, FEUD]),
        dict(category='邻境', name='刘焉', personId='liu-yan', label='合谋袭长安',
             text='《刘焉传》记刘焉与儿子刘范同马腾合谋袭击长安；事泄后马腾败退，刘范被杀。',
             refs=[Q('v031-b0006', '焉及範與騰通謀，引兵襲長安。範謀洩，奔槐里，騰敗，退還涼州，範應時見殺')]),
        dict(category='同僚', name='钟繇', label='调解争端，协调出兵',
             text='裴注引《典略》记钟繇和韦端奉命调解马腾、韩遂的冲突。《马超传》还记钟繇向两人阐明利害，马腾派马超随钟繇出兵。',
             refs=[MEDIATION, Q('v036-b0013', '司隸校尉鍾繇鎮關中，移書遂、騰，為陳禍福。騰遣超隨繇討郭援、高幹於平陽')]),
    ],

    readingNotes=[
        dict(title='西州起事与应募讨乱',
             text='正文把马腾和边章、韩遂并列为灵帝末年西州起事者；裴注引《典略》则从州郡募兵写起，说他起初领兵讨乱。两处叙事侧重不同，未交代他从应募到与韩遂共同行动的确切经过。',
             refs=[RISE, RECRUIT, EARLY_OFFICE]),
        dict(title='入朝之年的底本校记',
             text='《马超传》正文只说马腾受征为卫尉，未系年。裴注引《典略》的年次写作“十（五）年”，括号是底本校记，依据正文的先后只确定他入朝在211年马超起兵之前。',
             refs=[COURT, COURT_YEAR, REBELLION]),
    ],

    glossary=[
        ('部曲', '这里指军将统领的部队。'),
        ('卫尉', '汉朝负责宫门警卫、宿卫事务的官职。'),
    ],

    sourceScope='本书无马腾独立本传。本页以卷三十六《马超传》及其裴注《典略》、卷六《董卓传》中马腾与韩遂的合记为主，参看卷三十一《刘焉传》与卷十八《庞德传》。入朝的年次校记见辨析。本页不声称穷尽全书所有提及马腾之处。',
)
