"""甘宁：以卷五十五《甘宁传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v055-b0036', '甘寧字興霸，巴郡臨江人也。')
OLD_MASTERS = Q('v055-b0036', '乃往依劉表，因居南陽，不見進用，後轉託黃祖，祖又以凡人畜之。')
WU = Q('v055-b0037', '於是歸吳。周瑜、呂蒙皆共薦達，孫權加異，同於舊臣。')
PLAN = Q('v055-b0037', '至尊當早規之，不可後操圖之。圖之之計，宜先取黃祖。')
HUANG_ZU = Q('v055-b0037', '權遂西，果禽祖，盡獲其士衆。')
NANJUN = Q('v055-b0038', '後隨周瑜拒破曹公於烏林。攻曹仁於南郡，未拔，寧建計先徑進取夷陵，往即得其城，因入守之。')
RELIEF = Q('v054-b0009', '寧告急於瑜。瑜用呂蒙計，留淩統以守其後，身與蒙上救寧。')
YIYANG = Q('v055-b0038', '肅便選千兵益寧，寧乃夜往。羽聞之，住不渡，而結柴營')
OFFICE = Q('v055-b0038', '權嘉寧功，拜西陵太守，領陽新、下雉兩縣。')
JIANG = Q('v055-b0039', '寧手持練，身緣城，爲吏士先，卒破獲朱光。計功，呂蒙爲最。寧次之，拜折衝將軍。')
HEFEI = Q('v055-b0041', '張遼覘望知之，即將步騎奄至。寧引弓射敵，與統等死戰。')
KILLING = Q('v055-b0042', '寧許蒙不殺。斯須還船，縛置桑樹，自挽弓射殺之。')
DEATH = Q('v055-b0043', '寧卒，權痛惜之。')

PROFILE = dict(
    id='gan-ning', tier='C', reading=['055'],
    new=dict(name='甘宁', courtesy='兴霸', faction='孙吴', period='汉末', aliases=['甘兴霸'], tags=['夷陵解围', '逍遥津', '濡须']),
    eventRoles=[('chibi', '随周瑜破曹军'), ('nanjun-campaign', '先据夷陵，被围获援'),
                ('jingzhou-boundary', '受鲁肃增兵阻关羽渡水'), ('hefei', '津北引弓御敌')],
    lead='甘宁先依刘表、黄祖，转投孙权后建议先取黄祖。赤壁战后，他先取夷陵，为曹仁军所围，得周瑜、吕蒙解救；合肥撤军遇袭，他引弓迎敌，和凌统等死战。死后孙权深为惋惜。',
    role='孙权麾下折冲将军',
    facts=[
        dict(key='lifespan', label='生卒年', value='生卒年未详', text='本传没有记载甘宁的生年或卒年，只记孙权深为痛惜。', refs=[DEATH]),
        dict(key='hometown', label='籍贯', value='巴郡临江县', text='本传称巴郡临江人；裴注引《吴书》另说他本是南阳人，先人客居巴郡。', refs=[ORIGIN, Q('v055-b0036-n01', '寧本南陽人，其先客於巴郡。', '《吴书》')]),
        dict(key='identity', label='主要身份', value='孙权麾下将领', text='先依刘表和黄祖，归吴后由周瑜、吕蒙引荐，孙权待之如旧臣。', refs=[OLD_MASTERS, WU]),
        dict(key='office', label='最高官职', value='折冲将军；曾任西陵太守', text='益阳拒关羽后拜西陵太守，领阳新、下雉；攻下皖城后拜折冲将军。', refs=[OFFICE, JIANG]),
        dict(key='posthumous', label='身后称号', value='本书未载谥号', text='本传记孙权痛惜甘宁去世，未载追谥。', refs=[DEATH]),
        dict(key='deeds', label='代表事迹', items=['进议攻黄祖', '先取夷陵', '益阳拒关羽', '津北引弓'], text='献计先取黄祖，以偏师夺夷陵，在益阳阻关羽渡水，于津北射御来敌。', refs=[PLAN, NANJUN, YIYANG, HEFEI]),
    ],
    intro=[
        dict(title='转投孙权，先据夷陵',
             text='甘宁字兴霸，本传称他为巴郡临江人。年轻时他招聚少年，曾放任部下掠夺财货；后来停止攻劫，读了些诸子之书，先依刘表，再转投黄祖，都没有受到重用。周瑜、吕蒙一同举荐他，孙权按旧臣相待。他判断黄祖治下士吏有怨，战船器具废弛，主张赶在曹操前谋取荆州，先从黄祖下手。孙权纳策，西征果然擒获黄祖。甘宁随周瑜在赤壁一役击败曹军，又在南郡之战中建议先夺夷陵；守军仅够千人，曹仁遣五六千人围攻，周瑜听从吕蒙建议前来解围。',
             refs=[ORIGIN, Q('v055-b0036', '即放所將奪其資貨'), Q('v055-b0036', '止不攻劫，頗讀諸子'), OLD_MASTERS, WU, PLAN, Q('v055-b0037', '吏士心怨，舟船戰具頓廢不脩'), HUANG_ZU, NANJUN,
                   Q('v055-b0038', '并所新得，僅滿千人。曹仁乃令五六千人圍寧。'), RELIEF],
             eventLinks=[dict(label='赤壁一役', eventId='chibi'), dict(label='南郡之战', eventId='nanjun-campaign')]),
        dict(title='益阳与逍遥津',
             text='吴蜀争荆州时，甘宁随鲁肃在益阳拒关羽。他请增兵防守上游浅滩，鲁肃给了一千人；他连夜赶去，关羽闻讯便没有渡水。合肥撤军时，张辽突然袭击留在逍遥津北的孙权一行，甘宁引弓射敌，和凌统等人死战。本传说他能厚待部下，却也记他失信杀死一名逃到吕蒙处的仆役，几乎引发二人兵戎相见。孙权在他死后深为痛惜，传中没有写明卒年。',
             refs=[YIYANG, HEFEI, Q('v055-b0041', '輕財敬士，能厚養健兒'), KILLING, Q('v055-b0042', '蒙大怒，擊鼓會兵，欲就船攻寧。'), DEATH],
             eventLinks=[dict(label='吴蜀争荆州', eventId='jingzhou-boundary'), dict(label='合肥撤军', eventId='hefei')]),
    ],
    careers=[
        dict(id='join-wu', when='208年及此前', title='转投孙权，献取黄祖之策', office='领兵屯当口',
             text='离开黄祖，获周瑜、吕蒙引荐，建议孙权先取黄祖再图荆州；孙权破黄祖后授他兵众。', refs=[OLD_MASTERS, WU, PLAN, Q('v055-b0037', '權遂西，果禽祖，盡獲其士衆。遂授寧兵，屯當口'), Q('v047-b0009', '十三年春，權復征黃祖')]),
        dict(id='chibi-nanjun', when='208—209年', title='随周瑜拒曹，先取夷陵', office='—', eventIds=['chibi', 'nanjun-campaign'],
             text='随周瑜破曹军于乌林，又抢占夷陵。曹仁遣兵围攻数日，甘宁遣使告急，周瑜用吕蒙之计解围。', refs=[NANJUN, RELIEF, Q('v047-b0009', '遇於赤壁，大破曹公軍。公燒其餘船引退')]),
        dict(id='wan', when='214年', title='率先登上皖城', office='升城督，拜折冲将军',
             text='攻皖城时负责督率先登，亲自攀城，破城后论功仅次于吕蒙。', refs=[JIANG, Q('v047-b0014', '十九年五月，權征皖城。閏月，克之。')]),
        dict(id='yiyang', when='215年', title='受援兵守浅滩', office='西陵太守', eventIds=['jingzhou-boundary'],
             text='随鲁肃与关羽在益阳对峙。获增兵后趁夜赶往浅滩，关羽没有渡水。', refs=[YIYANG, OFFICE, Q('v047-b0014', '會備到公安，使關羽將三萬兵至益陽')]),
        dict(id='hefei', when='215年', title='逍遥津北引弓迎敌', office='—', eventIds=['hefei'],
             text='合肥撤军时，仍随孙权留在津北的甘宁遭张辽步骑突袭，与凌统等人奋力迎战。', refs=[Q('v055-b0041', '建安二十年，從攻合肥'), HEFEI]),
    ],
    records=[
        dict(section='civil', when='208年及此前', title='建议先取黄祖', category='经营建言', careerRef='join-wu',
             text='从荆州的地势、敌方物资和军心判断，主张趁曹操尚未染指南荆，先攻黄祖。张昭担忧东吴后方有乱，孙权最终采纳甘宁的建议。', refs=[PLAN, HUANG_ZU, Q('v055-b0037', '若軍果行，恐必致亂。')]),
        dict(section='military', when='208—209年', title='夺夷陵牵动南郡战局', category='先遣夺城', careerRef='chibi-nanjun', eventIds=['nanjun-campaign'],
             text='在江陵攻而未下时先夺夷陵，迫使曹仁分兵；兵力悬殊，周瑜随后率军解围。', refs=[NANJUN, RELIEF]),
        dict(section='setback', when='确年未载', title='失信杀人，激怒吕蒙', category='失信伤人',
             text='承诺不杀归还的仆役，转身却亲手射杀。吕蒙召兵欲攻，听母亲劝阻才罢手，甘宁当面承认有负于他。', refs=[KILLING, Q('v055-b0042', '聞母言，即豁然意釋'), Q('v055-b0042', '寧涕泣歔欷曰：「負卿。」')]),
    ],
    relations=[
        dict(category='君臣', name='孙权', personId='sunquan', label='厚待并采纳攻荆之议', text='甘宁归吴后，孙权待他如旧臣，并采纳他先攻黄祖的意见。', refs=[WU, PLAN, HUANG_ZU]),
        dict(category='同僚', name='吕蒙', personId='lumeng', label='举荐、解围与失和', text='吕蒙举荐甘宁，又在夷陵之围时建议救援；两人也曾因甘宁失信杀人而险些动武。', refs=[WU, RELIEF, KILLING]),
        dict(category='同僚', name='凌统', personId='ling-tong', label='津北并战，兼有父仇', text='两人在逍遥津并肩作战。裴注引《吴书》另记，凌统因甘宁射杀其父而怀怨，孙权曾禁止他报仇。', refs=[HEFEI, Q('v055-b0041-n01', '凌統怨寧殺其父操，寧常備統，不與相見。權亦命統不得讎之。', '《吴书》')]),
    ],
    readingNotes=[
        dict(title='濡须夜袭的兵力与战果', text='本传记选百余人饮酒后衔枚夜袭，曹营惊动。裴注引《江表传》增写越营垒、斩数十级，以及孙权把甘宁与张辽并论；这些细节来自注文。', refs=[Q('v055-b0040', '至二更時，銜枚出斫敵。敵驚動，遂退。'), Q('v055-b0040-n01', '使拔鹿角，踰壘入營，斬得數十級。', '《江表传》'), Q('v055-b0040-n01', '孟德有張遼，孤有興霸，足相敵也。', '《江表传》')]),
    ],
    sourceScope='以卷五十五《甘宁传》为主，参核卷四十七《吴主传》和卷五十四《周瑜传》；有关籍贯、父仇和夜袭的注文注明出处。本页不声称穷尽全书所有提及甘宁之处。',
)
