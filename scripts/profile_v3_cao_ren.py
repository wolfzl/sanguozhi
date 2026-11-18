"""曹仁：以卷九《曹仁传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v009-b0015', '曹仁字子孝，太祖從弟也。')
EARLY = Q('v009-b0015', '仁亦陰結少年，得千餘人，周旋淮、泗之間，遂從太祖爲别部司馬，行厉鋒校尉。')
RAID_SOUTH = Q('v009-b0016', '將騎擊備，破走之，仁盡復收諸叛縣而還。')
HUGUAN = Q('v009-b0017', '今公告之必死，將人自爲守。')
HUGUAN_RESULT = Q('v009-b0017', '太祖從之，城降。')
JIANGLING = Q('v009-b0018', '從平荆州，以仁行征南將軍，留屯江陵，拒吴將周瑜。')
RESCUE = Q('v009-b0018', '仁径渡沟直前，衝入賊圍，金等乃得解。')
RETREAT = Q('v047-b0010', '十四年，瑜、仁相守歳餘，所殺傷甚眾。仁委城走。')
TONGGUAN = Q('v009-b0019', '太祖討馬超，以仁行安西將軍，督諸將拒潼關，破超渭南。')
FAN_SIEGE = Q('v009-b0019', '關羽攻樊，時漢水暴溢，于禁等七軍皆沒，禁降羽。')
FAN_DEFENSE = Q('v009-b0019', '仁激厉將士，示以必死，將士感之皆無二。')
FAN_RELIEF = Q('v009-b0019', '徐晃救至，水亦稍减，晃從外擊羽，仁得溃圍出，羽退走。')
DISCIPLINE = Q('v009-b0020', '及長爲將，嚴整奉法令，常置科於左右，案以從事。')
FINAL_RANK = Q('v002-b0020', '以大將軍曹仁爲大司馬。')
DEATH = Q('v009-b0020', '黃初四年薨，諡曰忠侯。')
AGE = Q('v009-b0020-n01', '仁時年五十六。', '《魏书》')
SHRINE = Q('v003-b0016', '詔祀故大將軍夏侯惇、大司馬曹仁、車騎將軍程昱於太祖廟庭。')

PROFILE = dict(
    id='cao-ren',
    tier='C',
    reading=['009'],
    new=dict(name='曹仁', courtesy='子孝', faction='曹魏', period='汉末—223年',
             tags=['江陵', '樊城', '大司马']),
    eventRoles=[('guandu', '击退刘备，收复叛县'), ('nanjun-campaign', '驻守江陵抵御周瑜'),
                ('tongguan', '督诸将拒马超于潼关'), ('jingzhou', '坚守樊城，待援解围')],
    lead='曹操的从弟。早年率骑兵作战，后镇守江陵与樊城。江陵经年相持后退守，樊城则在汉水涨溢中守到徐晃来援。曹丕称帝后升至大司马，223年去世。',
    role='镇守荆襄的曹魏宗室大将',

    facts=[
        dict(key='lifespan', label='生卒年', value='约168—223年',
             text='本传记卒于黄初四年（223）。裴注引《魏书》记享年五十六，按当时常用的计岁方式逆推生年约为168年。',
             refs=[DEATH, AGE]),
        dict(key='hometown', label='籍贯', value='本传未直书；族属沛国谯曹氏',
             text='《曹仁传》只写他是曹操从弟；《武帝纪》记曹操是沛国谯人，是曹仁籍贯的宗族线索。',
             refs=[ORIGIN, Q('v001-b0001', '太祖武皇帝，沛國譙人也，姓曹')]),
        dict(key='identity', label='主要身份', value='曹氏宗室统兵大将',
             text='曹操的从弟，初为别部司马，后来留守江陵、镇守樊城。',
             refs=[ORIGIN, EARLY, JIANGLING, Q('v009-b0019', '假節，屯樊，鎮荆州。')]),
        dict(key='office', label='最高官职', value='大司马',
             text='先任征南将军，曹丕继为魏王后拜车骑将军，此后升大将军、大司马。',
             refs=[Q('v009-b0019', '還屯樊，即拜征南將軍。'), Q('v009-b0020', '及即王位，拜仁车騎將軍'),
                   Q('v002-b0019', '以車騎將軍曹仁爲大將軍。'), FINAL_RANK]),
        dict(key='posthumous', label='身后称号', value='忠侯；233年配享太祖庙庭',
             text='本传记谥忠侯；魏明帝青龙元年下诏，以曹仁等配享曹操庙庭。',
             refs=[DEATH, Q('v003-b0016', '青龍元年春正月甲申'), SHRINE]),
        dict(key='deeds', label='代表事迹', items=['官渡却刘备', '江陵救牛金', '固守樊城'],
             text='官渡相持时击退刘备；在江陵出城救牛金；樊城被围时守至援军到达。',
             refs=[RAID_SOUTH, RESCUE, FAN_DEFENSE, FAN_RELIEF]),
    ],

    intro=[
        dict(title='统骑从征，转守江陵',
             text='曹仁字子孝，是曹操的从弟。豪杰并起时，他召集了一千多名少年，在淮、泗间活动，后来投奔曹操，曾在征徐州时督骑兵担任先锋。官渡相持期间，袁绍派刘备活动于许都以南，许多县响应。曹仁认为刘备刚接掌袁绍的部队，还不能使部众听用，于是受命率骑兵击退刘备，收回响应的县。曹操取得荆州后，曹仁留守江陵，对抗周瑜。部将牛金一度被围，他亲自出城救援；但双方相持一年多后，曹仁最终放弃了江陵。',
             refs=[ORIGIN, EARLY, Q('v009-b0015', '從征徐州，仁常督騎，爲軍前鋒。'),
                   Q('v009-b0016', '紹遣劉備徇㶏彊諸縣，多舉眾應之。'), Q('v009-b0016', '備新將紹兵，未能得其用，擊之可破也。'),
                   RAID_SOUTH, JIANGLING, Q('v009-b0018', '遂被甲上馬，將其麾下壯士數十騎出城。'), RESCUE, RETREAT],
             eventLinks=[dict(label='官渡相持', eventId='guandu'), dict(label='留守江陵', eventId='nanjun-campaign')]),
        dict(title='困守樊城，获援解围',
             text='曹仁随后督诸将守御潼关，参加渭南之战，后来转屯樊城。219年关羽围攻樊城，汉水暴涨，于禁的援军被淹，于禁投降，樊城城墙只剩几板高露在水面上。曹仁率部守城，面对断粮和外援未至的危险，申明死守的决心，激励将士。等到洪水渐退、徐晃从外击退关羽，曹仁才得以出围。曹丕继为魏王后任他为车骑将军，此后累迁大司马，223年去世。',
             refs=[TONGGUAN, Q('v009-b0019', '假節，屯樊，鎮荆州。'), Q('v036-b0006', '是歲，羽率眾攻曹仁於樊。'),
                   FAN_SIEGE, Q('v009-b0019', '仁人馬數千人守城，城不沒者數板。'), Q('v009-b0019', '糧食欲盡，救兵不至。'),
                   FAN_DEFENSE, FAN_RELIEF, Q('v009-b0020', '及即王位，拜仁车騎將軍'), FINAL_RANK, DEATH],
             eventLinks=[dict(label='守御潼关', eventId='tongguan'), dict(label='关羽围攻樊城', eventId='jingzhou')]),
    ],

    careers=[
        dict(id='guandu', when='200年', title='官渡相持时击退刘备', office='—', eventIds=['guandu'],
             text='刘备受袁绍之命进至许都南面的诸县，曹仁率骑兵破其军，收回响应刘备的县。',
             refs=[Q('v001-b0047', '公還軍官渡。紹進保陽武。'), Q('v009-b0016', '紹遣劉備徇㶏彊諸縣，多舉眾應之。'), RAID_SOUTH]),
        dict(id='huguan', when='河北平定后，围壶关时', title='建议取消尽杀城中人的命令', office='封都亭侯',
             text='曹操下令破城后尽杀城中人，久攻不下。曹仁指出逼人死守将增加伤亡、拖延战事，建议留一条出路；曹操听从，壶关投降。',
             refs=[Q('v009-b0017', '從圍壶關。太祖令曰：「城拔，皆坑之。」連月不下。'), HUGUAN,
                   HUGUAN_RESULT, Q('v009-b0017', '於是錄仁前後功，封都亭侯。')]),
        dict(id='jiangling', when='208—209年', title='守江陵救牛金，最终撤出', office='行征南将军，转封安平亭侯', eventIds=['nanjun-campaign'],
             text='曹操留曹仁拒周瑜。牛金所部遇围，曹仁率数十骑出城救出牛金，又折返救下余兵；双方经年相守，最终曹仁弃城退去。',
             refs=[JIANGLING, Q('v009-b0018', '轉封安平亭侯。'), RESCUE,
                   Q('v009-b0018', '仁復直還突之，拔出金兵'), RETREAT]),
        dict(id='tongguan', when='211年', title='督诸将拒潼关', office='行安西将军', eventIds=['tongguan'],
             text='奉曹操之命督将抵御马超军，后来参加渭南击破马超一方的作战。',
             refs=[Q('v001-b0076', '十六年春正月'), TONGGUAN]),
        dict(id='fancheng', when='219年', title='汉水暴涨时固守樊城', office='征南将军', eventIds=['jingzhou'],
             text='平侯音之乱后回屯樊城，正式拜征南将军；关羽乘水围城，曹仁激励部下固守，等到徐晃击退关羽才得解围。',
             refs=[Q('v001-b0115', '二十四年春正月，仁屠宛，斬音。'), Q('v009-b0019', '還屯樊，即拜征南將軍。'),
                   FAN_SIEGE, FAN_DEFENSE, FAN_RELIEF]),
        dict(id='late-ranks', when='220—223年', title='历任车骑将军、大司马', office='车骑将军、大将军、大司马',
             text='曹丕为魏王时任曹仁为车骑将军；受禅后再升大将军、大司马。黄初四年曹仁去世。',
             refs=[Q('v009-b0020', '及即王位，拜仁车騎將軍'), Q('v002-b0019', '以車騎將軍曹仁爲大將軍。'), FINAL_RANK, DEATH]),
    ],

    records=[
        dict(section='civil', when='河北平定后，围壶关时', title='反对破城尽杀的命令', category='军政建言', careerRef='huguan',
             text='曹仁从攻方代价和守军选择两方面说明为什么要留活路。曹操采纳后，壶关守军投降。',
             refs=[Q('v009-b0017', '圍城必示之活門，所以开其生路也。'), HUGUAN, HUGUAN_RESULT]),
        dict(section='military', when='219年', title='在洪水中稳住樊城守军', category='守城', careerRef='fancheng', eventIds=['jingzhou'],
             text='樊城一度内外隔绝，曹仁激励部下守到徐晃来援；解围有赖城内坚守与城外援兵。',
             refs=[Q('v009-b0019', '外内斷絕，糧食欲盡，救兵不至。'), FAN_DEFENSE, FAN_RELIEF]),
        dict(section='setback', when='209年', title='与周瑜相持后失江陵', category='弃城撤退', careerRef='jiangling', eventIds=['nanjun-campaign'],
             text='救出牛金是江陵攻守中的一次局部胜利。吴方纪传补足了战事结局：双方多有伤亡，曹仁弃城，周瑜领南郡太守。',
             refs=[RESCUE, RETREAT, Q('v047-b0010', '權以瑜爲南郡太守。')]),
    ],

    relations=[
        dict(category='亲族', name='曹操', personId='caocao', label='从弟与统将',
             text='曹仁是曹操从弟，从别部司马起随其征战，也曾以壶关的围城处置向他进言。',
             refs=[ORIGIN, EARLY, HUGUAN, HUGUAN_RESULT]),
        dict(category='敌对', name='周瑜', personId='zhouyu', label='争夺江陵',
             text='曹仁留屯江陵抵御周瑜，相持一年多后弃城，周瑜领南郡太守。',
             refs=[JIANGLING, RETREAT, Q('v047-b0010', '權以瑜爲南郡太守。')]),
        dict(category='同僚', name='徐晃', personId='xu-huang', label='内守外援解樊围',
             text='曹仁在城内固守，徐晃从外进兵击退关羽，曹仁才得以突围。',
             refs=[FAN_DEFENSE, FAN_RELIEF]),
        dict(category='部属', name='牛金', label='江陵被围获救',
             text='牛金率三百人挑战周瑜前军，因兵少被围，曹仁出城解围，又折返救出余兵。',
             refs=[Q('v009-b0018', '乃募得三百人，遣部曲將牛金逆與挑戰。'), RESCUE, Q('v009-b0018', '仁復直還突之，拔出金兵')]),
    ],

    assessment=[
        dict(title='陈寿：曹氏诸将各有勋劳',
             text='陈寿对同卷诸人的评价兼顾宗亲的地位和实际功劳。本传还写曹仁为将后严守法令，曹丕曾拿他来告诫曹彰。',
             refs=[Q('v009-b0059', '並以親舊肺腑，貴重於時，左右勳業，咸有効勞。'), DISCIPLINE,
                   Q('v009-b0020', '爲將奉法，不當如征南邪！')]),
    ],

    sourceScope='以卷九《曹仁传》为基础，参看卷一《武帝纪》、卷二《文帝纪》、卷三《明帝纪》、卷三十六《关羽传》和卷四十七《吴主传》；生年据裴注所引《魏书》推算。本页不声称穷尽全书所有提及曹仁之处。',
)
