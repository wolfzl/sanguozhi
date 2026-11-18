"""凌统：以卷五十五《凌统传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v055-b0045', '凌統字公績，吳郡餘杭人也。')
FATHER = Q('v055-b0045', '入夏口，先登，破其前鋒，輕舟獨進，中流矢死。')
SUCCESSION = Q('v055-b0046', '統年十五，左右多稱述者，權亦以操死國事，拜統別部司馬，行破賊都尉，使攝父兵。')
KILLING = Q('v055-b0046', '勤乘酒凶悖，又於道路辱統。統不忍，引刀斫勤，數日乃死。')
REDEMPTION = Q('v055-b0046', '還，自拘於軍正。權壯其果毅，使得以功贖罪。')
JIANGXIA = Q('v055-b0047', '時呂蒙敗其水軍，而統先搏其城，於是大獲。')
CHIBI = Q('v055-b0047', '與周瑜等拒破曹公於烏林，遂攻曹仁，遷爲校尉。')
NANJUN = Q('v054-b0009', '瑜用呂蒙計，留淩統以守其後，身與蒙上救寧。')
HEFEI = Q('v055-b0048', '統率親近三百人陷圍，扶扞權出。')
LOSS = Q('v055-b0048', '統復還戰，左右盡死，身亦被創')
RETURN = Q('v055-b0048', '橋敗路絕，統被甲潛行。權旣御船，見之驚喜。')
PROMOTION = Q('v055-b0048', '拜偏將軍，倍給本兵。')
DEATH = Q('v055-b0050', '事畢當出，會病卒，時年四十九。')
ORPHANS = Q('v055-b0051', '二子烈、封，年各數歲，權內養於宮，愛待與諸子同')
GAN = Q('v055-b0041-n01', '凌統怨寧殺其父操，寧常備統，不與相見。權亦命統不得讎之。', '《吴书》')

PROFILE = dict(
    id='ling-tong', tier='C', reading=['055'],
    new=dict(name='凌统', courtesy='公绩', faction='孙吴', period='汉末', aliases=['凌公绩'], tags=['江夏', '南郡', '逍遥津']),
    eventRoles=[('chibi', '随周瑜破曹军'), ('nanjun-campaign', '吴军救夷陵时留守后方'), ('hefei', '率亲兵护孙权突围')],
    lead='凌统十五岁接领父兵，曾为孙权征江夏的前锋，随周瑜在赤壁拒曹、进攻南郡。合肥撤军遇袭，他率亲兵护孙权冲出包围，自己负伤脱险，左右亲兵尽死。后来奉命招兵，事毕病卒。',
    role='孙权麾下偏将军',
    facts=[
        dict(key='lifespan', label='生卒年', value='生卒年未详', text='本传作病卒“时年四十九”，没有记下卒年，不能由此倒推生年。', refs=[DEATH]),
        dict(key='hometown', label='籍贯', value='吴郡余杭县', text='凌统字公绩，吴郡余杭人。', refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='孙权麾下将领', text='父凌操战死后，十五岁接领旧部；合肥之战任右部督，率亲兵护孙权突围。', refs=[FATHER, SUCCESSION, Q('v055-b0048', '從往合肥，爲右部督。'), HEFEI]),
        dict(key='office', label='最高官职', value='偏将军；曾领沛相', text='由别部司马、行破贼都尉起家，后历校尉、荡寇中郎将并领沛相，合肥战后拜偏将军。', refs=[SUCCESSION, CHIBI, Q('v055-b0048', '又從破皖，拜盪寇中郎將，領沛相。'), PROMOTION]),
        dict(key='posthumous', label='身后称号', value='未载谥号；长子因功封侯', text='孙权为他命人撰铭诔，又追记其功而封儿子凌烈为亭侯。本传未载凌统谥号。', refs=[Q('v055-b0050', '使張承爲作銘誄。'), Q('v055-b0051', '追錄統功，封烈亭侯，還其故兵。')]),
        dict(key='deeds', label='代表事迹', items=['江夏先攻', '南郡留守', '津北护主', '招集精兵'], text='征江夏先攻城，南郡作战时留后，逍遥津护主，后来奉命招募精兵。', refs=[JIANGXIA, NANJUN, HEFEI, Q('v055-b0050', '得精兵萬餘人')]),
    ],
    intro=[
        dict(title='接父兵，随军拒曹',
             text='凌统的父亲凌操跟随孙权征江夏时中箭身亡。凌统十五岁便由孙权授官，接领父亲的部队。后来攻山中屯寨之前，部将陈勤借酒辱及亡父，凌统挥刀砍伤他，陈勤数日后死亡。攻屯时凌统奋战立功，回军即向军正自拘，孙权准其以功赎罪。再征江夏时，他担任前锋，在吕蒙击败黄祖水军后率先攻城。随后凌统随周瑜在赤壁一役拒曹；吴军转攻南郡，甘宁被围在夷陵，周瑜留下凌统守后方，亲自与吕蒙往救。',
             refs=[FATHER, SUCCESSION, Q('v055-b0046', '勤怒詈統，及其父操'), KILLING, REDEMPTION, JIANGXIA, CHIBI, NANJUN],
             eventLinks=[dict(label='赤壁一役', eventId='chibi'), dict(label='转攻南郡', eventId='nanjun-campaign')]),
        dict(title='津北护主，亲兵尽失',
             text='215年合肥撤军，张辽突然杀到逍遥津北，前队已走远。凌统率亲兵三百人护孙权突围，自己折回迎战，左右尽死，他也受伤。退路的桥已破坏，他披甲潜行才回到孙权船边，看不到亲兵回来，悲痛不已。孙权拜他为偏将军，增其部众。凌统后来主张招揽山中壮勇，奉命办成后病卒。本传记孙权命张承撰铭诔，又在宫中养育凌统的两个儿子。',
             refs=[Q('v047-b0014', '權與淩統、甘寧等在津北爲魏將張遼所襲'), Q('v055-b0048', '權使追還前兵，兵去已遠，勢不相及'), HEFEI, LOSS, RETURN,
                   Q('v055-b0048', '統痛親近無反者，悲不自勝。'), PROMOTION, Q('v055-b0050', '統以山中人尚多壯悍，可以威恩誘也'), DEATH,
                   Q('v055-b0050', '使張承爲作銘誄。'), ORPHANS],
             eventLinks=[dict(label='合肥撤军', eventId='hefei')]),
    ],
    careers=[
        dict(id='inherit', when='十五岁，确年未载', title='接领父亲旧部', office='别部司马，行破贼都尉',
             text='凌操从征江夏战死，孙权命凌统摄其旧兵。', refs=[FATHER, SUCCESSION]),
        dict(id='chen-qin', when='确年未载', title='斫伤陈勤，以功赎罪', office='—',
             text='陈勤当众骂及凌操，随后又在路上侮辱凌统。凌统砍伤陈勤致死，攻屯立功后投案，获准以功赎罪。', refs=[Q('v055-b0046', '勤怒詈統，及其父操'), KILLING, REDEMPTION]),
        dict(id='jiangxia', when='208年春', title='任前锋，再征江夏', office='承烈都尉',
             text='率数十人先行，斩黄祖将张硕。吕蒙击破水军后，凌统率先攻城。', refs=[Q('v055-b0047', '行入右江，斬黃祖將張碩，盡獲船人。'), JIANGXIA, Q('v055-b0047', '權以統爲承烈都尉'), Q('v047-b0009', '十三年春，權復征黃祖')]),
        dict(id='chibi-nanjun', when='208—209年', title='随军破曹，南郡留后', office='迁校尉', eventIds=['chibi', 'nanjun-campaign'],
             text='随周瑜等破曹军于乌林。攻南郡时，周瑜用吕蒙的计策去救甘宁，留下凌统守后方。', refs=[CHIBI, NANJUN, Q('v047-b0009', '遇於赤壁，大破曹公軍。')]),
        dict(id='hefei', when='215年', title='逍遥津护孙权脱险', office='右部督，战后拜偏将军', eventIds=['hefei'],
             text='撤军遭袭，率三百亲兵突入包围护孙权脱身；折回再战后，左右俱死，他负伤披甲潜行而还。', refs=[Q('v055-b0041', '建安二十年，從攻合肥'), HEFEI, LOSS, RETURN, PROMOTION]),
        dict(id='recruiting', when='合肥战后，确年未载', title='招集壮勇，事毕病卒', office='—',
             text='向孙权建议招抚山中壮勇，奉命招得精兵万余人。任务结束将要出发时病卒。', refs=[Q('v055-b0050', '統以山中人尚多壯悍，可以威恩誘也'), Q('v055-b0050', '得精兵萬餘人'), DEATH]),
    ],
    records=[
        dict(section='civil', when='合肥战后，确年未载', title='建议招抚山中壮勇', category='招抚征募', careerRef='recruiting',
             text='以“威恩诱”招集兵员，孙权准地方官先供应招募所需，再行报告。', refs=[Q('v055-b0050', '權令東占且討之，命勑屬城，凡統所求，皆先給後聞。')]),
        dict(section='military', when='215年', title='以亲兵打开退路', category='战场救援', careerRef='hefei', eventIds=['hefei'],
             text='前军已去，凌统以身边三百人护孙权突围；孙权得以策马越桥，凌统负伤归船。', refs=[HEFEI, RETURN, Q('v047-b0014', '權乘駿馬越津橋得去。')]),
        dict(section='setback', when='确年未载', title='酒宴结怨，斫伤同僚致死', category='军中冲突', careerRef='chen-qin',
             text='陈勤一再侮辱凌统，凌统动刀致其死亡；后来获以功赎罪，足见本传把这视为应当承担的罪责。', refs=[KILLING, REDEMPTION]),
    ],
    relations=[
        dict(category='君臣', name='孙权', personId='sunquan', label='津北护主，身后养孤', text='凌统护孙权脱险，孙权战后增拨兵众；凌统死后，两子由孙权在宫中抚养。', refs=[HEFEI, PROMOTION, ORPHANS]),
        dict(category='亲族', name='凌操', label='父死后接领旧部', text='凌操随孙权进攻江夏，独进中箭而死；凌统十五岁接领父亲的部下。', refs=[FATHER, SUCCESSION]),
        dict(category='同僚', name='甘宁', personId='gan-ning', label='并肩御敌，另有父仇', text='二人曾在津北共同迎战。裴注引《吴书》记凌统怨甘宁杀父，孙权不许他报仇。', refs=[Q('v055-b0041', '寧引弓射敵，與統等死戰。'), GAN]),
    ],
    readingNotes=[
        dict(title='凌操中箭，谁放的箭', text='凌统本传只写其父凌操“中流矢死”。裴注引《吴书》则从甘宁为黄祖断后的角度记载，射死凌操的人是甘宁。', refs=[FATHER, Q('v055-b0036-n03', '寧以善射，將兵在後，射殺校尉凌操。', '《吴书》')]),
    ],
    sourceScope='以卷五十五《凌统传》为主，参核同卷《甘宁传》正文和裴注、卷四十七《吴主传》及卷五十四《周瑜传》。本页不声称穷尽全书所有提及凌统之处。',
)
