"""王平：从街亭收兵到兴势守险。"""
from profile_v3 import Q

ORIGIN = Q('v043-b0018', '王平字子均，巴西宕渠人也。')
NAME = Q('v043-b0018', '本養外家何氏。後復姓王。')
DEFECT = Q('v043-b0018', '從曹公征漢中，因降先主，拜牙門將、裨將軍。')
JIE = Q('v043-b0018', '謖捨水上山，舉措煩擾，平連規諫謖，謖不能用，大敗於街亭。')
DRUM = Q('v043-b0018', '惟平所領千人鳴鼓自持，魏將張郃疑其伏兵，不往逼也。')
RALLY = Q('v043-b0018', '於是平徐徐收合諸營遺迸，率將士而還。')
POST = Q('v043-b0019', '拜平前監軍、鎮北大將軍，統漢中。')
XING = Q('v043-b0020', '今宜先遣劉護軍、杜參軍據興勢，平為後拒。')
RELIEF = Q('v043-b0020', '涪諸軍及費禕自成都相繼而至，魏軍退還，如平本策。')
DEATH = Q('v043-b0021', '十一年卒，子訓嗣。')
LITERACY = Q('v043-b0021', '手不能書，其所識不過十字，而口授作書，皆有意理。')

PROFILE = dict(
    id='wang-ping', tier='C', reading=['043'],
    new=dict(name='王平', courtesy='子均', faction='蜀汉', period='汉末—248年', aliases=['何平', '王子均'], tags=['街亭', '兴势', '汉中']),
    eventRoles=[('first-northern-expedition', '街亭鸣鼓稳军并收残部'), ('xingshi-defense', '决策先据兴势，待援退敌')],
    lead='王平原随曹操征汉中，后归刘备。街亭败后他稳住部队、收拢散兵；掌管汉中后，又在兴势之战先占险要、等到援军，使曹爽所率魏军无功而返。',
    role='镇守汉中的蜀汉大将',
    facts=[
        dict(key='lifespan', label='生卒年', value='生年未详—248年', text='本书未载生年。《王平传》在延熙纪年下记十一年卒，即248年。', refs=[DEATH, Q('v043-b0019', '延熙元年')]),
        dict(key='hometown', label='籍贯', value='巴西郡宕渠县', text='本传记为巴西宕渠人。', refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='蜀汉汉中守将', text='先从曹操，后归刘备，最终统领汉中军务。', refs=[DEFECT, POST]),
        dict(key='office', label='最高官职', value='镇北大将军', text='归蜀后拜牙门将、裨将军，后任前监军、镇北大将军，统汉中。', refs=[DEFECT, POST]),
        dict(key='title', label='最高爵位', value='安汉侯', text='先封亭侯，继而进封安汉侯，接替吴壹督汉中。', refs=[Q('v043-b0018', '進位討寇將軍，封亭侯。'), Q('v043-b0019', '進封安漢侯，代壹督漢中。')]),
        dict(key='posthumous', label='身后称号', value='本书未载', text='本传记王平去世、子王训承袭爵位，未载谥号。', refs=[DEATH]),
        dict(key='deeds', label='代表事迹', items=['街亭收兵', '坚守南围', '兴势拒魏'], text='街亭收合散兵，后在祁山守住南围、在兴势拒曹爽。', refs=[RALLY, Q('v043-b0018', '平堅守不動，郃不能克。'), XING, RELIEF]),
    ],
    intro=[
        dict(title='归蜀与街亭收兵',
             text='王平是巴西宕渠人，早年由外家何氏抚养，后来复姓王。他曾随曹操征汉中，转而归附刘备。诸葛亮首次北伐时，王平隶属先行的马谡。马谡舍水上山，王平多次劝谏，马谡不听，终于在街亭大败。当其余部众四散时，王平带着自己的一千人鸣鼓固守，张郃怀疑有伏兵，不敢逼近。王平借此收拢散兵，带队退回，升任参军并统兵。三年后再遇张郃，他坚守祁山南围，魏军未能攻破。',
             refs=[ORIGIN, NAME, DEFECT, JIE, DRUM, RALLY, Q('v043-b0018', '平特見崇顯，加拜參軍，統五部兼當營事'), Q('v043-b0018', '張郃攻平，平堅守不動，郃不能克。')],
             eventLinks=[dict(label='诸葛亮首次北伐', eventId='first-northern-expedition')]),
        dict(title='先守兴势再待援军',
             text='王平后来负责汉中军务。曹爽率魏军从骆谷来攻时，汉中守兵不足三万，有人主张退守汉、乐两城等待援兵。王平判断涪地路远，一旦放任魏军占住险关便很难补救，于是主张先占兴势，自己在后接应，魏军若分兵攻黄金，便另率一部防御。护军刘敏赞同，立即照办。涪军和费祎所部陆续赶到，魏军最终撤回。王平识字很少，但能口授文书，常请人朗读《史记》《汉书》，听后能说出要旨。',
             refs=[POST, Q('v043-b0020', '前鋒已在駱谷。時漢中守兵不滿三萬'), Q('v043-b0020', '聽當固守漢、樂二城'), Q('v043-b0020', '漢中去涪垂千里。賊若得關，便為禍也。'), XING, Q('v043-b0020', '若賊分向黃金，平率千人下自臨之'), Q('v043-b0020', '惟護軍劉敏與平意同，即便施行。'), RELIEF, LITERACY, Q('v043-b0021', '使人讀《史》、《漢》諸紀傳，聽之，備知其大義')],
             eventLinks=[dict(label='先占兴势', eventId='xingshi-defense')]),
    ],
    careers=[
        dict(id='defect', when='随曹操征汉中时，确年未载', title='随曹军出征时转投刘备', office='牙门将、裨将军', text='《王平传》记他随曹操征汉中，期间转投刘备，未注明此事是哪一年。', refs=[DEFECT]),
        dict(id='jieting', when='228年', title='街亭败后收兵', office='后拜参军，进讨寇将军，封亭侯', text='劝马谡未果，败后稳住所部并撤回散兵，由此获拔擢。', refs=[JIE, DRUM, RALLY, Q('v043-b0018', '平特見崇顯，加拜參軍，統五部兼當營事，進位討寇將軍，封亭侯。')], eventIds=['first-northern-expedition']),
        dict(id='southern-camp', when='231年', title='祁山南围不动', office='—', text='诸葛亮围祁山，王平另守南围，张郃来攻而未能攻克。', refs=[Q('v043-b0018', '九年，亮圍祁山，平別守南圍。'), Q('v043-b0018', '張郃攻平，平堅守不動，郃不能克。')]),
        dict(id='govern-hanzhong', when='243年', title='统领汉中', office='前监军、镇北大将军', text='蒋琬回驻涪，王平受命统汉中。', refs=[Q('v043-b0019', '六年，琬還住涪'), POST]),
        dict(id='xing', when='244年', title='先据兴势，援军至而魏退', office='—', text='不退守城池，遣将抢据兴势，自为后援；费祎等相继赶到，曹爽军退。', refs=[XING, RELIEF, Q('v033-b0023', '鎮北大將軍王平拒興勢圍，大將軍費禕督諸軍往赴救，魏軍退。')], eventIds=['xingshi-defense']),
        dict(id='death', when='248年', title='去世，子王训袭爵', office='—', text='延熙十一年去世，王训承袭。', refs=[DEATH]),
    ],
    records=[
        dict(section='military', when='228年', title='败局中保住所部', category='稳军收兵', careerRef='jieting', eventIds=['first-northern-expedition'], text='在友军离散时用鼓声维持声势，让张郃不敢逼近，有余地收拢各营散兵。', refs=[DRUM, RALLY]),
        dict(section='military', when='244年', title='把防线放在险要处', category='守险待援', careerRef='xing', eventIds=['xingshi-defense'], text='王平认为让敌先入关再等援兵风险过高，刘敏支持先占兴势的判断；实际结果与其估计相符。', refs=[Q('v043-b0020', '賊若得關，便為禍也。'), XING, Q('v043-b0020', '惟護軍劉敏與平意同，即便施行。'), RELIEF]),
        dict(section='setback', when='在世时，确年未载', title='严整之外也有疑忌', category='处事局限', text='本传记王平遵守法度，也把心性狭窄、好疑看作他的缺点，未举出由此招致的具体败绩。', refs=[Q('v043-b0021', '遵履法度，言不戲諺'), Q('v043-b0021', '然性狹侵疑，為人自輕，以此為損焉。')]),
    ],
    sections={'civil': {'note': '王平兼任过汉中太守，《王平传》只交代其职任，没有叙述具体民政措施。'}},
    assessment=[dict(title='陈寿：忠勇而严整', text='陈寿以“忠勇而严整”概括王平，既指出勇于任事，也点出他治军守度的一面。', refs=[Q('v043-b0036', '王平忠勇而嚴整')])],
    relations=[
        dict(category='旧主', name='曹操', personId='caocao', label='曾随曹操征汉中', text='王平原从曹操攻汉中，于此次征战期间转归刘备。', refs=[DEFECT]),
        dict(category='同僚', name='马谡', personId='ma-su', label='街亭多次劝谏', text='王平随马谡先行，屡劝不听，马谡失败后自行收军。', refs=[Q('v043-b0018', '屬參軍馬謖先鋒。'), JIE, RALLY]),
        dict(category='敌对', name='张郃', personId='zhang-he', label='街亭、祁山两相遇', text='张郃在街亭没有逼近鸣鼓的王平部，后来攻其祁山南围又未攻克。', refs=[DRUM, Q('v043-b0018', '張郃攻平，平堅守不動，郃不能克。')]),
        dict(category='同僚', name='魏延', personId='wei-yan', label='蜀军撤回时交锋', text='诸葛亮死后，王平在南谷口斥退魏延所部；《魏延传》在这里称他为何平。', refs=[Q('v043-b0019', '魏延作亂，一戰而敗，平之功也。'), Q('v040-b0033', '儀等令何平在前禦延。'), NAME]),
    ],
    readingNotes=[
        dict(title='王平归附刘备的确年', text='本传只说王平随曹操征汉中，因而归附刘备，未标明年份。《武帝纪》在215年记杜濩、朴胡来附；《先主传》又记曹操219年亲自进至汉中对抗刘备，这两条纪年均未提到王平。', refs=[DEFECT, Q('v001-b0100', '九月，巴七姓夷王朴胡、賨邑侯杜濩舉巴夷、賨民來附'), Q('v032-b0021', '曹公自長安舉眾南征。')]),
    ],
    sourceScope='以卷四十三《王平传》为主，参看卷一《武帝纪》、卷三十二《先主传》、卷三十三《后主传》的纪年与卷四十《魏延传》的退兵记载。本页不声称穷尽全书所有提及王平之处。',
)
