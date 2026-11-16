"""赵云：B 级；正文与《云别传》分层。"""
from profile_v3 import Q
HOME = Q('v036-b0021', '趙雲字子龍，常山真定人也。')
FOLLOW = Q('v036-b0021', '本屬公孫瓚，瓚遣先主為田楷拒袁紹，雲遂隨從，為先主主騎。')
SAVE = Q('v036-b0021', '雲身抱弱子，即後主也，保護甘夫人，即後主母也，皆得免難。')
SHU = Q('v036-b0022', '至江州，分遣雲從外水上江陽，與亮會於成都。成都既定，以雲為翊軍將軍。')
OFFICE = Q('v036-b0022', '建興元年，為中護軍、征南將軍，封永昌亭侯，遷鎮東將軍。')
JI = Q('v036-b0022', '雲、芝兵弱敵強，失利於箕谷，然斂眾固守，不至大敗。軍退，貶為鎮軍將軍。')
LAND = Q('v036-b0022-n01', '益州人民，初罹兵革，田宅皆可歸還，今安居複業，然後可役調，得其歡心。', '《云别传》')
HAN = Q('v036-b0022-n01', '而雲入營，更大開門，偃旗息鼓。公軍疑雲有伏兵，引去。', '《云别传》')
ADVICE = Q('v036-b0022-n01', '不應置魏，先與吳戰；兵勢一交，不得卒解。', '《云别传》')
REAR = Q('v036-b0022-n02', '雲身自斷後，軍資什物，略無所棄，兵將無緣相失。', '《云别传》')
SHI = Q('v036-b0022', '七年卒，追諡順平侯。')
PROFILE = dict(
 id='zhaoyun', tier='B', reading=['036'], role='蜀汉中护军、镇东将军',
 lead='先属公孙瓒，后长期追随刘备；长坂保护甘夫人与幼年刘禅，溯江参与平定益州。228年与邓芝在箕谷失利而能收众固守，退军后被贬，次年去世。归还田宅、汉水拒敌和反对伐吴等侧面见于裴注引《云别传》。',
 facts=[
  dict(key='hometown', label='籍贯', value='常山真定', text='字子龙，常山真定人。', refs=[HOME]),
  dict(key='identity', label='主要身份', value='刘备旧将、蜀汉将领', text='原属公孙瓒，随刘备主骑，后在蜀汉任中护军等职。', refs=[FOLLOW, OFFICE]),
  dict(key='office', label='最高官职', value='中护军、镇东将军', text='建兴元年任中护军、征南将军，迁镇东将军；箕谷退军后贬为镇军将军。', refs=[OFFICE, JI]),
  dict(key='title', label='最高爵位', value='永昌亭侯', text='建兴元年封永昌亭侯。', refs=[OFFICE]),
  dict(key='posthumous', label='身后称号', value='顺平侯（261年追谥）', text='本传记谥顺平侯，《后主传》将追谥系于景耀四年三月。', refs=[SHI, Q('v033-b0040', '四年春三月，追諡故將軍趙雲。')]),
  dict(key='deeds', label='代表事迹', items=['长坂护主', '溯江定蜀', '箕谷固守'], text='长坂保护刘备家属、进军江阳会成都、箕谷失利后收众固守。', refs=[SAVE, SHU, JI]),
 ],
 intro=[
  dict(title='由公孙瓒转随刘备', text='赵云字子龙，常山真定人，最初属于公孙瓒。公孙瓒派刘备帮助田楷抵御袁绍时，赵云开始随刘备，替他掌管骑兵。裴注引《云别传》另补充两人的交往，包括在邺城会合和招募部曲；这些细节属于注引材料，不能与陈寿正文混作同一层叙述。', refs=[HOME, FOLLOW, Q('v036-b0021-n01', '先主就袁紹，雲見於鄴。', '《云别传》'), Q('v036-b0021-n01', '密遣雲合募得數百人，皆稱劉左將軍部曲，紹不能知。', '《云别传》')]),
  dict(title='长坂护人与溯江', text='208年刘备在当阳长坂被追，赵云身抱幼年刘禅，保护甘夫人，使母子免难，随后迁牙门将军。刘备入蜀之初，赵云留在荆州，后来随诸葛亮、张飞溯江，另走外水进军江阳，最终会于成都。益州平定后任翊军将军，护卫旧主与独当一路是正文所呈现的两个侧面。', refs=[SAVE, Q('v036-b0021', '遷為牙門將軍。先主入蜀，雲留荊州。'), SHU, Q('v036-b0022', '亮率雲與張飛等俱溯江西上，平定郡縣。')], eventLinks=[dict(label='当阳长坂', eventId='jingzhou-surrender'), dict(label='刘备入蜀', eventId='enter-shu')]),
  dict(title='别传中的谨慎建言', text='《云别传》写益州平定后，有人提议将成都田宅分给将领，赵云主张归还百姓以便安居复业，刘备采纳。该书还记他在汉水迎救同军、开营偃旗退敌，以及反对先与孙权交战。这些故事丰富了他的形象，但本页逐处注明来源，不把别传的称誉当作正文原话。', refs=[LAND, Q('v036-b0022-n01', '先主即從之。', '《云别传》'), HAN, ADVICE, Q('v036-b0022-n01', '時議欲以成都中屋舍及城外園地桑田分賜諸將。', '《云别传》'), Q('v036-b0022-n01', '忠過期不還，雲將數十騎輕行出圍，迎視忠等。', '《云别传》')], eventLinks=[dict(label='汉水', eventId='hanzhong')]),
  dict(title='箕谷退军与身后', text='228年首次北伐，诸葛亮令赵云、邓芝率疑军在箕谷牵制曹真，自己进攻祁山。赵云一部兵弱敌强，虽失利仍能收众固守，没有大败，退军后贬为镇军将军。次年去世，后来追谥顺平侯。对这位将领，既应读到护卫、谨慎和勇敢，也应保留本传明确记载的败绩与处分。', refs=[Q('v035-b0012', '使趙雲、鄧芝為疑軍，據箕谷'), JI, SHI, Q('v036-b0022', '亮令雲與鄧芝往拒，而身攻祁山。')], eventLinks=[dict(label='首次北伐', eventId='first-northern-expedition')]),
 ],
 careers=[
  dict(id='follow', when='早年，确年未载', title='离公孙瓒随刘备', office='主骑', text='原属公孙瓒，随刘备帮助田楷拒袁绍，为刘备主骑。', refs=[FOLLOW]),
  dict(id='changban', when='208年', title='长坂保护甘夫人与刘禅', office='牙门将军', text='在当阳长坂抱幼主、护甘夫人，使二人免难。', refs=[SAVE, Q('v036-b0021', '遷為牙門將軍。')], eventIds=['jingzhou-surrender']),
  dict(id='stay', when='211年刘备入蜀时', title='留守荆州', office='—', text='刘备入蜀时留赵云于荆州；《云别传》补记领留营司马、掌内事。', refs=[Q('v036-b0021', '先主入蜀，雲留荊州。'), Q('v036-b0021-n02', '先主入益州，雲領留營司馬。', '《云别传》'), Q('v036-b0021-n02', '先主以雲嚴重，必能整齊，特任掌內事。', '《云别传》')], eventIds=['enter-shu']),
  dict(id='shu', when='刘备攻璋后至214年', title='由江阳会军成都', office='翊军将军', text='随诸葛亮溯江，至江州后分军走江阳，会于成都，战后升翊军将军。', refs=[SHU, Q('v036-b0022', '亮率雲與張飛等俱溯江西上，平定郡縣。')]),
  dict(id='land', when='214年定益州后', title='主张归还田宅', office='—', text='裴注引《云别传》记赵云反对分田宅给诸将，主张让百姓复业，刘备采纳。', refs=[LAND, Q('v036-b0022-n01', '先主即從之。', '《云别传》'), Q('v036-b0022-n01', '時議欲以成都中屋舍及城外園地桑田分賜諸將。', '《云别传》')]),
  dict(id='hanshui', when='219年', title='汉水迎救与开营退敌', office='—', text='《云别传》记赵云迎视黄忠，返救负伤张著，归营后大开营门，使追兵疑伏而退，再以弩射击。', refs=[Q('v036-b0022-n01', '將張著被創，雲復馳馬還營迎著。', '《云别传》'), HAN, Q('v036-b0022-n01', '忠過期不還，雲將數十騎輕行出圍，迎視忠等。', '《云别传》'), Q('v036-b0022-n01', '雲雷鼓震天，惟以戎弩於後射公軍', '《云别传》')], eventIds=['hanzhong']),
  dict(id='jiangzhou', when='刘备东征前后，确年未载', title='谏伐吴，督江州', office='—', text='《云别传》记赵云劝先讨魏，刘备未听；留赵云督江州，败后赵云进至永安。', refs=[ADVICE, Q('v036-b0022-n01', '先主不聽，遂東征，留雲督江州。先主失利於秭歸，雲進兵至永安，吳軍已退。', '《云别传》')]),
  dict(id='office', when='223年', title='封侯，任中护军', office='中护军、征南将军，后迁镇东将军；永昌亭侯', text='建兴元年升官封侯，本段未明确迁镇东将军的月日。', refs=[OFFICE]),
  dict(id='hanzhong', when='227年', title='随诸葛亮驻汉中', office='—', text='建兴五年随诸葛亮驻军汉中。', refs=[Q('v036-b0022', '五年，隨諸葛亮駐漢中。')]),
  dict(id='jigu', when='228年', title='箕谷失利，退军被贬', office='镇军将军', text='与邓芝为疑军拒曹真，兵弱敌强而失利，收众固守后退军，被贬。', refs=[JI, Q('v035-b0012', '使趙雲、鄧芝為疑軍，據箕谷')], eventIds=['first-northern-expedition']),
  dict(id='death', when='229年', title='去世', office='—', text='建兴七年卒，子赵统嗣爵。', refs=[SHI, Q('v036-b0022', '雲子統嗣')]),
  dict(id='posthumous', when='261年', title='追谥顺平侯', office='追谥顺平侯', text='《后主传》记景耀四年三月追谥赵云。', refs=[SHI, Q('v033-b0040', '四年春三月，追諡故將軍趙雲。')]),
 ],
 trajectory=dict(atlasPerson='zhaoyun', phases=[
  dict(id='early', title='随刘与长坂护卫', when='早年至208年', span=(190, 208), careers=['follow', 'changban'], atlasStops=[0]),
  dict(id='shu', title='留荆与入蜀', when='211—214年', span=(211, 214), careers=['stay', 'shu', 'land'], atlasStops=[]),
  dict(id='hanshui', title='汉水拒敌与谏征', when='219年至东征前后', span=(219, 222), careers=['hanshui', 'jiangzhou'], atlasStops=[1]),
  dict(id='north', title='北驻与箕谷退军', when='223—228年', span=(223, 228), careers=['office', 'hanzhong', 'jigu'], atlasStops=[2]),
  dict(id='after', title='去世与追谥', when='229—261年', span=(229, 261), careers=['death', 'posthumous'], atlasStops=[]),
 ]),
 records=[
  dict(section='civil', when='214年后', title='主张还田安民', category='复业建言', careerRef='land', text='《云别传》把还田宅与百姓复业、役调和人心联系起来，并记刘备采纳。', refs=[LAND, Q('v036-b0022-n01', '先主即從之。', '《云别传》')]),
  dict(section='civil', when='箕谷退军后', title='余绢归库，留待冬赐', category='军资管理', careerRef='jigu', text='《云别传》记赵云认为无功不应受赏，请将剩余绢帛交赤岸府库，等待冬赐，诸葛亮赞同。', refs=[Q('v036-b0022-n02', '其物請悉入赤岸府庫，須十月為冬賜。', '《云别传》'), Q('v036-b0022-n02', '軍事無利，何為有賜？', '《云别传》'), Q('v036-b0022-n02', '亮大善之。', '《云别传》')]),
  dict(section='military', when='208年', title='长坂保护家属', category='危难护卫', careerRef='changban', text='正文把功劳写为使甘夫人与幼年刘禅免难，并未列杀敌数字。', refs=[SAVE]),
  dict(section='military', when='219年', title='开营疑敌后反击', category='临阵应变', careerRef='hanshui', text='《云别传》写以开门偃旗使追兵疑伏，待退再用弩射击；这是该注引材料中的用兵。', refs=[HAN, Q('v036-b0022-n01', '雲雷鼓震天，惟以戎弩於後射公軍', '《云别传》')]),
  dict(section='setback', when='228年', title='箕谷失利受贬', category='战败处分', careerRef='jigu', text='虽未大败，失利与贬官仍是正文明确记载；有序撤退不能抹去战果不利。', refs=[JI]),
  dict(section='setback', when='东征前，确年未载', title='劝先讨魏未被采纳', category='建言未行', careerRef='jiangzhou', text='《云别传》记其反对先伐吴而未获采纳。这是建言未行，不把东征败绩归为赵云指挥责任。', refs=[ADVICE, Q('v036-b0022-n01', '先主不聽', '《云别传》')]),
 ],
 assessment=[dict(title='陈寿：强挚壮猛', text='陈寿合评黄忠、赵云强挚壮猛、并作爪牙，以灌婴、滕公相比；这是对武将才质与辅佐作用的总评。', refs=[Q('v036-b0024', '黃忠、趙雲強摯壯猛，並作爪牙，其灌、滕之徒歟？')])],
 relations=[
  dict(category='君臣', name='刘备', personId='liubei', label='长期追随的主君', text='从公孙瓒麾下转随刘备，为其主骑，长坂保护其家属。', refs=[FOLLOW, SAVE]),
  dict(category='君臣', name='刘禅', personId='liu-shan', label='长坂所护幼主', text='正文明确赵云所抱弱子即后主刘禅。', refs=[SAVE]),
  dict(category='旧主', name='公孙瓒', personId='gongsun-zan', label='早年所属', text='原属公孙瓒，因刘备助田楷拒袁绍而开始随刘备。', refs=[FOLLOW]),
  dict(category='同僚', name='诸葛亮', personId='zhuge-liang', label='入蜀与北伐统帅', text='随诸葛亮入蜀，后又奉命与邓芝拒曹真。', refs=[SHU, Q('v036-b0022', '亮令雲與鄧芝往拒'), Q('v036-b0022', '亮率雲與張飛等俱溯江西上，平定郡縣。')]),
  dict(category='同僚', name='邓芝', label='箕谷共同作战', text='二人以弱兵拒强敌，失利后收众固守。', refs=[JI]),
 ],
 readingNotes=[
  dict(title='正文与《云别传》的范围', text='长坂护人、入蜀和箕谷失利见正文；还田、汉水开营与谏伐吴见《云别传》，引文分别标明。', refs=[SAVE, LAND, HAN, ADVICE]),
  dict(title='229年卒与261年追谥', text='本传把去世与追谥连写，不能据此把追谥也系于229年；《后主传》明确另记景耀四年三月追谥。', refs=[SHI, Q('v033-b0040', '四年春三月，追諡故將軍趙雲。')]),
 ],
 sourceScope='以卷三十六《赵云传》正文及全部裴注为基础，交叉核对卷三十二《先主传》、卷三十五《诸葛亮传》和卷三十三《后主传》。裴注引《云别传》的叙述逐处标明，不混同正文。本页不声称穷尽全书所有提及赵云之处。',
)
