"""马超：B 级；西州起兵与归刘分期。"""
from profile_v3 import Q
HOME = Q('v036-b0013', '馬超字孟起，右扶風茂陵人也。')
FIRST = Q('v036-b0013', '騰遣超隨繇討郭援、高幹於平陽，超將龐德親斬援首。')
ARMY = Q('v036-b0013', '以超為偏將軍，封都亭侯，領騰部曲。')
DEFEAT = Q('v036-b0014', '曹公用賈詡謀，離間超、遂，更相猜疑，軍以大敗。')
JI = Q('v036-b0014', '殺涼州刺史韋康，據冀城，有其眾。')
LOST = Q('v036-b0014', '寬、衢閉冀城門，超不得入。進退狼狽，乃奔漢中依張魯。')
SHU = Q('v036-b0015', '先主遣人迎超，超將兵徑到城下。城中震怖，璋即稽首，以超為平西將軍，督臨沮，因為前都亭侯。')
OFFICE = Q('v036-b0016', '章武元年，遷驃騎將軍，領涼州牧，進封斄鄉侯')
FAMILY = Q('v036-b0017', '臣門宗二百餘口，為孟德所誅略盡，惟有從弟岱')
SHI = Q('v036-b0017', '追諡超曰威侯，子承嗣。')
PROFILE = dict(
 id='ma-chao', tier='B', reading=['036'], role='蜀汉骠骑将军、领凉州牧',
 lead='起自西州军阀马腾部曲，联合韩遂在潼关对抗曹操，败后争据陇上，又失冀城、投奔张鲁。214年归刘备，兵临成都促成刘璋投降，后任蜀汉骠骑将军；222年卒，临终上疏托付残存宗族。',
 facts=[
  dict(key='hometown', label='籍贯', value='右扶风茂陵', text='字孟起，右扶风茂陵人。', refs=[HOME]),
  dict(key='identity', label='主要身份', value='西州军阀，后归刘备', text='先领父亲马腾部曲，与韩遂联合；败后归刘备，成为蜀汉将领。', refs=[ARMY, DEFEAT, SHU]),
  dict(key='office', label='最高官职', value='骠骑将军，领凉州牧', text='章武元年所授；此前拜左将军、假节。领凉州牧是任命，不能据此认定归蜀后实际控制凉州。', refs=[OFFICE, Q('v036-b0016', '先主為漢中王，拜超為左將軍，假節。')]),
  dict(key='title', label='最高爵位', value='斄乡侯', text='章武元年由都亭侯进封斄乡侯，字形依本书。', refs=[OFFICE]),
  dict(key='posthumous', label='身后称号', value='威侯（260年追谥）', text='本传记谥威侯，《后主传》系追谥于景耀三年九月。', refs=[SHI, Q('v033-b0039', '三年秋九月，追諡故將軍關羽、張飛、馬超、龐統、黃忠。')]),
  dict(key='deeds', label='代表事迹', items=['平阳讨援', '潼关抗曹', '兵临成都'], text='随钟繇讨郭援，联合关中诸将抗曹，归刘后兵临成都。', refs=[FIRST, DEFEAT, SHU]),
 ],
 intro=[
  dict(title='承接父亲部曲', text='马超字孟起，右扶风茂陵人，其父马腾与韩遂等在西州起兵。马超曾随钟繇讨郭援、高幹于平阳，斩郭援者是他的部将庞德。后来马腾请求入朝，马超受拜偏将军、封都亭侯，接领父亲部曲。这时他已经是掌握军队的地方将领，尚未加入刘备集团。', refs=[HOME, FIRST, ARMY, Q('v036-b0013', '父騰，靈帝末與邊章、韓遂等俱起事於西州。'), Q('v036-b0013', '後騰與韓遂不和，求還京畿。')]),
  dict(title='潼关与陇上的败局', text='211年马超与韩遂等结盟，进军潼关。曹操采用贾诩离间之计，使联军互相猜疑而败。马超随后借诸戎之力攻取陇上，杀凉州刺史韦康，据冀城并自称征西将军。韦康旧吏杨阜、姜叙等反击，马超出城攻敌，梁宽、赵衢却关闭城门，使他无家可归，最终逃往汉中。', refs=[DEFEAT, JI, LOST, Q('v036-b0014', '超既統眾，遂與韓遂合從，及楊秋、李堪、成宜等相結，進軍至潼關。'), Q('v036-b0014', '超果率諸戎以擊隴上郡縣'), Q('v036-b0014', '超自稱征西將軍，領并州牧，督涼州軍事。'), Q('v036-b0014', '康故吏民楊阜、姜敘、梁寬、趙衢等，合謀擊超。阜、敘起於鹵城，超出攻之，不能下；')], eventLinks=[dict(label='潼关', eventId='tongguan')]),
  dict(title='穷困归刘与再获任用', text='马超在张鲁处不能舒展，听说刘备围成都，秘密请降。刘备迎接并令他进至成都城下，城中震恐，刘璋投降。马超先任平西将军，后来又与张飞等屯下辩，战事不利后退往汉中。刘备称汉中王后拜他为左将军，称帝后迁骠骑将军、领凉州牧，进封斄乡侯。', refs=[Q('v036-b0014', '聞先主圍劉璋於成都，密書請降。'), SHU, Q('v001-b0110', '三月，張飛、馬超走漢中'), OFFICE, Q('v036-b0014', '魯不足與計事，內懷於邑'), Q('v001-b0108', '劉備遣張飛、馬超、吳蘭等屯下辯'), Q('v036-b0016', '先主為漢中王，拜超為左將軍，假節。')], eventLinks=[dict(label='刘备围成都', eventId='enter-shu'), dict(label='称汉中王', eventId='hanzhong')]),
  dict(title='临终所忧的宗族', text='222年马超去世，年四十七。临终上疏说宗族二百余口几乎被曹操杀尽，希望刘备照顾从弟马岱，维系祭祀。陈寿既批评他倚恃武勇而使宗族覆灭，也承认他能从穷困中重新获用。阅读其归蜀后的高位时，仍应记住此前失败与家族损失构成的沉重背景。', refs=[Q('v036-b0017', '二年卒，時年四十七。'), FAMILY, Q('v036-b0024', '馬超阻戎負勇，以覆其族，惜哉！能因窮致泰，不猶愈乎！'), Q('v036-b0017', '當為微宗血食之繼，深讬陛下，餘無複言。')]),
 ],
 careers=[
  dict(id='pingyang', when='早年，确年未载', title='随钟繇讨郭援', office='本书未详', text='在平阳参战，部将庞德斩郭援。', refs=[FIRST]),
  dict(id='army', when='马腾入朝时，确年未载', title='接领父亲部曲', office='偏将军、都亭侯', text='马腾任卫尉，马超受命掌握其部曲。', refs=[ARMY, Q('v036-b0013', '於是徵為衛尉')]),
  dict(id='tongguan', when='211年', title='潼关联军败于曹操', office='—', text='与韩遂等进据潼关，被离间后联军大败。', refs=[DEFEAT, Q('v036-b0014-n02', '建安十六年，超與關中諸將', '《典略》'), Q('v036-b0014', '超既統眾，遂與韓遂合從，及楊秋、李堪、成宜等相結，進軍至潼關。')], eventIds=['tongguan']),
  dict(id='jicheng', when='潼关败后，确年未载', title='据冀城后失城', office='自称征西将军、领并州牧', text='攻陇上杀韦康，据冀城；杨阜等反击，马超出战不能下，返城被拒。', refs=[JI, LOST, Q('v036-b0014', '超自稱征西將軍，領并州牧，督涼州軍事。'), Q('v036-b0014', '康故吏民楊阜、姜敘、梁寬、趙衢等，合謀擊超。阜、敘起於鹵城，超出攻之，不能下；')]),
  dict(id='zhanglu', when='归蜀前，确年未载', title='投张鲁于汉中', office='—', text='失去冀城后依张鲁，后向围成都的刘备秘密请降。', refs=[LOST, Q('v036-b0014', '聞先主圍劉璋於成都，密書請降。')]),
  dict(id='chengdu', when='214年', title='兵临成都，刘璋投降', office='平西将军、督临沮、都亭侯', text='刘备派人迎接，马超领兵到成都城下，城中震怖，刘璋出降。', refs=[SHU], eventIds=['enter-shu']),
  dict(id='xiabian', when='217—218年', title='屯下辩，退汉中', office='—', text='《武帝纪》记刘备遣张飞、马超、吴兰屯下辩；曹洪破吴兰，张飞、马超退汉中。', refs=[Q('v001-b0108', '劉備遣張飛、馬超、吳蘭等屯下辯'), Q('v001-b0110', '三月，張飛、馬超走漢中'), Q('v001-b0110', '曹洪破吳蘭，斬其將任夔等。')]),
  dict(id='left', when='219年', title='拜左将军', office='左将军，假节', text='刘备为汉中王后授官。', refs=[Q('v036-b0016', '先主為漢中王，拜超為左將軍，假節。')], eventIds=['hanzhong']),
  dict(id='office', when='221年', title='迁骠骑将军', office='骠骑将军、领凉州牧、斄乡侯', text='章武元年迁官进爵，策书以其信著北土相期。', refs=[OFFICE, Q('v036-b0016', '以君信著北土，威武並昭')], eventIds=['shu-founding']),
  dict(id='death', when='222年', title='卒前托付马岱', office='—', text='四十七岁卒，临终向刘备托付从弟马岱。', refs=[Q('v036-b0017', '二年卒，時年四十七。'), FAMILY]),
  dict(id='shi', when='260年', title='追谥威侯', office='追谥威侯', text='后主追谥，子马承嗣爵。', refs=[SHI, Q('v033-b0039', '三年秋九月，追諡故將軍關羽、張飛、馬超、龐統、黃忠。')]),
 ],
 trajectory={'phases': [{'id': 'early',
             'title': '早年领军',
             'when': '早年，确年未载',
             'span': [190, 210],
             'careers': ['pingyang', 'army'],
             'atlasStops': [0]},
            {'id': 'west',
             'title': '潼关与陇上争战',
             'when': '211年至投张鲁前',
             'span': [211, 214],
             'careers': ['tongguan', 'jicheng'],
             'atlasStops': [1, 2]},
            {'id': 'shu',
             'title': '投张鲁后归刘',
             'when': '归蜀前至218年',
             'span': [214, 218],
             'careers': ['zhanglu', 'chengdu', 'xiabian'],
             'atlasStops': [3, 4, 5, 6]},
            {'id': 'late',
             'title': '蜀汉任官与去世',
             'when': '219—222年',
             'span': [219, 222],
             'careers': ['left', 'office', 'death'],
             'atlasStops': []},
            {'id': 'shi', 'title': '身后追谥', 'when': '260年', 'span': [260, 260], 'careers': ['shi'], 'atlasStops': []}],
 'atlasPerson': 'machao'},
 records=[
  dict(section='military', when='214年', title='兵至成都促降', category='威慑受降', careerRef='chengdu', text='本传以城中震怖、刘璋稽首相连，说明其兵临城下的威慑效果，不写成单人攻下成都。', refs=[SHU]),
  dict(section='military', when='潼关败后，确年未载', title='重新集结诸戎', category='动员兵众', careerRef='jicheng', text='败后仍能率诸戎攻取陇上，体现其地方号召力；这一能力未能转化为持久统治。', refs=[Q('v036-b0014', '超果率諸戎以擊隴上郡縣，隴上郡縣皆應之，')]),
  dict(section='setback', when='211年', title='联军互疑而败', category='联盟破裂', careerRef='tongguan', text='曹操用贾诩离间计，马超、韩遂猜疑，联合兵力未能维持。', refs=[DEFEAT]),
  dict(section='setback', when='潼关败后，确年未载', title='失冀城而依张鲁', category='失去根据地', careerRef='jicheng', text='杀韦康后遭其旧吏反击，出战不克、返城不得，失去经营陇上的基础。', refs=[JI, LOST, Q('v036-b0014', '康故吏民楊阜、姜敘、梁寬、趙衢等，合謀擊超。阜、敘起於鹵城，超出攻之，不能下；')]),
  dict(section='setback', when='222年临终', title='宗族近乎覆灭', category='家族后果', careerRef='death', text='遗疏自述家族几乎被杀尽，陈寿将此与负勇起兵相联系；这是史家判断，不把灭族倒写成起兵前已发生。', refs=[FAMILY, Q('v036-b0024', '馬超阻戎負勇，以覆其族，惜哉！')]),
 ],
 sections={'civil': {'note': '马超归刘后本传主要记受官封爵，未载可独立展开的施政；领凉州牧不表示实际治理凉州，不据此列文治功绩。'}},
 assessment=[dict(title='陈寿：负勇覆族，穷而复泰', text='陈寿批评马超凭借诸戎、倚恃勇力而使宗族覆灭，也认为他穷困后能重新获用，仍有可取。', refs=[Q('v036-b0024', '馬超阻戎負勇，以覆其族，惜哉！能因窮致泰，不猶愈乎！')])],
 relations=[
  dict(category='亲族', name='马腾', personId='ma-teng', label='父亲与部曲来源', text='马腾入朝任卫尉，马超接领其军队。', refs=[ARMY, Q('v036-b0013', '於是徵為衛尉')]),
  dict(category='同僚', name='韩遂', personId='han-sui', label='潼关联军首领', text='结盟抗曹，后中离间而互疑。', refs=[DEFEAT]),
  dict(category='敌对', name='曹操', personId='caocao', label='潼关交战的对手', text='曹操击败联军，马超遗疏又指其诛杀宗族。', refs=[DEFEAT, FAMILY]),
  dict(category='旧主', name='张鲁', personId='zhang-lu', label='失冀城后的收留者', text='马超失城后投奔汉中张鲁，后来另向刘备请降。', refs=[LOST, Q('v036-b0014', '聞先主圍劉璋於成都，密書請降。')]),
  dict(category='君臣', name='刘备', personId='liubei', label='归降后授以高位', text='迎马超入成都之战，后拜左将军、骠骑将军。', refs=[SHU, OFFICE, Q('v036-b0016', '先主為漢中王，拜超為左將軍，假節。')]),
 ],
 readingNotes=[
  dict(title='起兵与家族被诛的先后', text='《典略》先叙211年反叛与战败，再记诏收灭其家属；本页不采用先为父复仇而起兵的叙述。', refs=[Q('v036-b0014-n02', '超等敗走。超至安定，遂奔涼州。詔收滅超家屬。', '《典略》')]),
  dict(title='关张持刀威慑之说被驳', text='《山阳公载记》称关羽、张飞因马超直呼刘备字而威慑他；裴松之指出关羽未到益州，斥为不合情理，不作事实采用。', refs=[Q('v036-b0015-n02', '羽未嘗在益土也。', '《山阳公载记》；裴松之按'), Q('v036-b0015-n02', '與備言，常呼備字', '《山阳公载记》')]),
 ],
 sourceScope='以卷三十六《马超传》正文及全部裴注为基础，交叉核对卷一《武帝纪》下辩战事、卷三十二《先主传》与卷三十三追谥纪年。《典略》与《山阳公载记》异说分层处理。本页不声称穷尽全书所有提及马超之处。',
)
