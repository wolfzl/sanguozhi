"""韩当：以卷五十五《韩当传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v055-b0012', '韓當字義公，遼西令支人也。')
SUN_JIAN = Q('v055-b0012', '以便弓馬，有膂力，幸於孫堅，從征伐周旋，數犯危難，陷敵擒虜，爲別部司馬。')
JIANGDONG = Q('v055-b0012', '及孫策東渡，從討三郡，遷先登校尉，授兵二千，騎五十匹。')
LE_AN = Q('v055-b0012', '從征劉勳，破黃祖，還討鄱陽，領樂安長，山越畏服。')
CHIBI = Q('v055-b0012', '後以中郎將與周瑜等拒破曹公')
RESCUE = Q('v055-b0009-n01', '蓋自彊以一聲呼韓當，當聞之，曰：「此公覆聲也。」向之垂涕，解易其衣，遂以得生。', '《吴书》')
ZANG_BA = Q('v018-b0015', '當遣兵逆霸，霸與戰於逢龍，當復遣兵邀霸於夾石，與戰破之，還屯舒。')
JINGZHOU = Q('v055-b0012', '又與呂蒙襲取南郡，遷偏將軍，領永昌太守。')
YILING = Q('v055-b0012', '宜都之役，與陸遜、朱然等共攻蜀軍於涿鄉，大破之，徙威烈將軍，封都亭侯。')
LU_XUN = Q('v058-b0009', '黃武元年，劉備率大眾來向西界，權命遜為大都督、假節，督朱然、潘璋、宋謙、韓當、徐盛、鮮于丹、孫桓等五萬人拒之。')
DEFENSE = Q('v055-b0012', '曹真攻南郡，當保東南。在外爲帥，厲將士同心固守，又敬望督司，奉遵法令，權善之。')
PROMOTION = Q('v055-b0012', '黃武二年，封石城侯，遷昭武將軍，領冠軍太守，後又加都督之號。')
DANYANG = Q('v055-b0012', '將敢死及解煩兵萬人，討丹楊賊，破之。')
DEATH = Q('v055-b0012', '會病卒，子綜襲侯領兵。')
SHIYANG = Q('v047-b0029', '秋七月，權聞魏文帝崩，征江夏，圍石陽，不克而還。')
HAN_ZONG = Q('v055-b0013', '綜內懷懼，載父喪，將母家屬部曲男女數千人奔魏。')
ZANG_BA_MISSION = Q('v018-b0015', '張遼之討陳蘭，霸別遣至皖，討吳將韓當，使權不得救蘭。')
SAME_YEAR = Q('v055-b0013', '其年，權征石陽')

PROFILE = dict(
    id='han-dang',
    tier='C',
    reading=['055'],
    lead='韩当因弓马和勇力为孙坚所用，随孙策渡江，又为孙权参加赤壁、袭取南郡和夷陵等战事。晚年封石城侯，以昭武将军领冠军太守，后加都督号，平定丹杨叛军后病卒。',
    role='历事孙氏三代的武将',

    facts=[
        dict(key='lifespan', label='生卒年', value='生年不详—约226年',
             text='本传未载出生年份。接着韩当病卒一事，本传说“其年”孙权征石阳，对照《吴主传》黄武五年（226）的记载，可以推知他约在这年去世。',
             refs=[DEATH, SAME_YEAR, SHIYANG]),
        dict(key='hometown', label='籍贯', value='辽西郡令支县',
             text='本传开篇记韩当字义公，辽西令支人。', refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='历事孙坚、孙策、孙权的孙氏旧将',
             text='孙坚因其娴熟弓马、力气过人而亲信他。孙策东渡时他参与从征，后来又为孙权统军作战。',
             refs=[SUN_JIAN, JIANGDONG, DEFENSE]),
        dict(key='office', label='最高官职', value='昭武将军，领冠军太守，加都督号',
             text='早年任别部司马、先登校尉，参加赤壁之战时为中郎将。后来迁偏将军、领永昌太守，再升威烈将军、昭武将军，领冠军太守并加都督号。',
             refs=[SUN_JIAN, JIANGDONG, CHIBI, JINGZHOU, YILING, PROMOTION]),
        dict(key='title', label='最高爵位', value='石城侯',
             text='夷陵战后封都亭侯，黄武二年（223）封石城侯。', refs=[YILING, PROMOTION]),
        dict(key='posthumous', label='身后称号', value='未载谥号',
             text='本传记韩当病逝后，其子韩综承袭侯爵、统领原有部队，未载韩当本人的谥号或追赠。',
             refs=[DEATH]),
        dict(key='deeds', label='代表事迹', items=['随策东渡', '随吕蒙取南郡', '涿乡破蜀'],
             text='随孙策东渡征战三郡，与吕蒙袭取南郡，与陆逊、朱然等在涿乡击败蜀军。',
             refs=[JIANGDONG, JINGZHOU, YILING]),
    ],

    intro=[
        dict(title='从骑射起家到赤壁',
             text='韩当字义公，辽西令支人。他娴熟弓马，力气过人，追随孙坚时屡次冒险冲入敌阵、擒拿俘虏，做了别部司马。后来他随孙策东渡，征讨三郡，升先登校尉，获拨两千士兵和五十匹战马。他又随军讨刘勋、破黄祖，回军后讨鄱阳、领乐安长，本传称当地山越因而畏服。208年，他以中郎将与周瑜等参加赤壁之战。裴注引《吴书》说，黄盖中箭落水，一度无人认出，韩当听出他的喊声，为他更换衣服，黄盖得以生还。',
             refs=[ORIGIN, SUN_JIAN, JIANGDONG, LE_AN, CHIBI,
                   Q('v055-b0009-n01', '蓋爲流矢所中，時寒墮水，爲吳軍人所得，不知其蓋也', '《吴书》'), RESCUE],
             eventLinks=[dict(label='随孙策东渡', eventId='sun-ce-jiangdong'),
                         dict(label='赤壁之战', eventId='chibi')]),
        dict(title='袭取南郡与晚年统兵',
             text='219年，韩当跟随吕蒙袭取南郡，升偏将军、领永昌太守。222年夷陵战事中，他与陆逊、朱然等在涿乡击败蜀军，升威烈将军，封都亭侯。曹真攻南郡时，韩当承担东南守备，鼓励将士同心固守，严格遵守法令，得到孙权肯定。223年他封石城侯，升昭武将军、领冠军太守，后来又加都督号。他率敢死兵、解烦兵共万人击破丹杨叛军，随后病逝，由儿子韩综袭爵领兵。',
             refs=[JINGZHOU, YILING, LU_XUN, DEFENSE, PROMOTION, DANYANG, DEATH],
             eventLinks=[dict(label='随吕蒙袭取南郡', eventId='jingzhou'),
                         dict(label='夷陵战事', eventId='yiling')]),
    ],

    careers=[
        dict(id='jiangdong', when='195年起', title='随孙策东渡，征讨三郡', office='先登校尉，后领乐安长', eventIds=['sun-ce-jiangdong'],
             text='早年因弓马勇力受孙坚赏识，任别部司马。后随孙策东渡，征讨三郡，获拨步骑；又随军讨刘勋、黄祖，回军后讨鄱阳、任乐安长。',
             refs=[SUN_JIAN, JIANGDONG, LE_AN,
                   Q('v046-b0014-n02', '策渡江攻繇牛渚營，盡得邸閣糧穀、戰具，是歳興平二年也。', '《江表传》')]),
        dict(id='chibi', when='208年', title='与周瑜等拒曹', office='中郎将', eventIds=['chibi'],
             text='以中郎将随周瑜等抗击曹军。本传只简记参战；裴注引《吴书》另记他救护中箭落水的黄盖。',
             refs=[CHIBI, Q('v047-b0009', '與備俱進，遇於赤壁，大破曹公軍。'), RESCUE]),
        dict(id='zang-ba', when='张辽讨陈兰时，确年未载', title='派兵迎击臧霸失利', office='—',
             text='据《臧霸传》，曹方派臧霸到皖阻断孙权方面救援陈兰。韩当先派兵迎击，继而在夹石截击，派出的部队被臧霸击败。',
             refs=[ZANG_BA_MISSION, ZANG_BA]),
        dict(id='jingzhou', when='219年', title='随吕蒙袭取南郡', office='偏将军，领永昌太守', eventIds=['jingzhou'],
             text='随吕蒙袭取关羽辖境中的南郡，升偏将军，领永昌太守。',
             refs=[JINGZHOU, Q('v047-b0018', '蒙到南郡，南郡太守糜芳以城降，蒙據江陵')]),
        dict(id='yiling', when='222年', title='涿乡破蜀，守备东南', office='威烈将军，都亭侯', eventIds=['yiling'],
             text='夷陵之战中，与陆逊、朱然等在涿乡击败蜀军。后来曹真围攻南郡，韩当承担东南守备。',
             refs=[YILING, LU_XUN, DEFENSE, Q('v047-b0023', '曹眞、夏侯尚、張郃、徐晃圍南郡。')]),
        dict(id='late-service', when='223年起，约226年卒', title='封石城侯，平丹杨后病卒', office='石城侯，昭武将军，领冠军太守，后加都督号',
             text='黄武二年封石城侯。后来率敢死兵与解烦兵击破丹杨叛军；韩当病逝后，由子韩综袭爵领兵。',
             refs=[PROMOTION, DANYANG, DEATH, SAME_YEAR, SHIYANG]),
    ],

    records=[
        dict(section='military', when='222年', title='在陆逊统领下与诸将破蜀', category='协同作战', careerRef='yiling', eventIds=['yiling'],
             text='《陆逊传》把韩当列入陆逊所督诸将，《韩当传》则点明他与陆逊、朱然等共同在涿乡破敌。这两处分别交代了全军指挥和韩当所在部队的战功。',
             refs=[LU_XUN, YILING]),
        dict(section='military', when='曹真围南郡时', title='东南守备获孙权认可', category='守备与军纪', careerRef='yiling',
             text='任外军统帅时，韩当勉励将士合力固守，也敬重督察官员、遵守军中法令，孙权因此称许他。本传没有详细记载守备中的交战经过。',
             refs=[DEFENSE]),
        dict(section='setback', when='张辽讨陈兰时，确年未载', title='截击臧霸未成', category='战场失利', careerRef='zang-ba',
             text='韩当派兵拦截臧霸，夹石一战失利。《臧霸传》把它记在阻断吴军救援陈兰的战事中；韩当本传没有记这次交锋，无法核定他本人是否在场或所部损失。',
             refs=[ZANG_BA_MISSION, ZANG_BA]),
    ],
    sections={
        'civil': {'note': '韩当先后领乐安长、永昌太守和冠军太守。本传只概记任乐安长时“山越畏服”，没有交代可单列的民政措施。'},
    },

    assessment=[
        dict(title='陈寿：江表虎臣', text='陈寿在卷末把韩当和同传诸将合称“江表之虎臣”，指出他们都是孙氏厚待的将领。',
             refs=[Q('v055-b0073', '凡此諸將，皆江表之虎臣，孫氏之所厚待也。')]),
    ],

    relations=[
        dict(category='旧主', name='孙坚', personId='sun-jian', label='赏识其弓马和勇力',
             text='韩当因骑射和力气受到孙坚赏识，从征时屡次冒险破敌，任别部司马。', refs=[SUN_JIAN]),
        dict(category='同僚', name='黄盖', personId='huang-gai', label='赤壁辨声救护黄盖',
             text='裴注引《吴书》记黄盖在赤壁落水后呼喊韩当，韩当听出是黄盖的声音，为他换衣，使他活了下来。',
             refs=[RESCUE]),
        dict(category='同僚', name='陆逊', personId='luxun', label='在其麾下拒刘备',
             text='夷陵战事中受大都督陆逊统辖，和朱然等共同在涿乡击败蜀军。', refs=[LU_XUN, YILING]),
        dict(category='亲族', name='韩综', label='袭爵领兵，后奔魏',
             text='韩综在父亲死后袭爵、领兵，随后带着父亲的灵柩与家属部曲奔魏。', refs=[DEATH, HAN_ZONG]),
    ],

    readingNotes=[
        dict(title='韩当病逝与韩综降魏的纪年',
             text='《韩当传》在写韩当病卒后，接着说“其年”孙权征石阳；《吴主传》把征石阳系于黄武五年（226），把韩综降魏记在次年。页面据两处互证估计韩当的卒年，韩综降魏是父亲去世后的事。',
             refs=[DEATH, SAME_YEAR, SHIYANG, Q('v047-b0032', '六年春正月，諸將獲彭綺。閏月，韓當子綜以其眾降魏。')]),
    ],

    sourceScope='以卷五十五《韩当传》为主，参看卷四十六《孙策传》、卷四十七《吴主传》、卷五十八《陆逊传》及卷十八《臧霸传》，救护黄盖的故事另标为裴注引《吴书》。本页不声称穷尽全书所有提及韩当之处。',
)
