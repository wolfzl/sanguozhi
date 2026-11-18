"""潘璋：以卷五十五《潘璋传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v055-b0060', '潘璋字文珪，東郡發干人也。')
JOIN = Q('v055-b0060', '孫權爲陽羨長，始往隨權。')
POLICING = Q('v055-b0060', '後爲吳大巿刺姧，盜賊斷絕，由是知名，遷豫章西安長。')
HEFEI = Q('v055-b0061', '宋謙、徐盛皆披走，璋身次在後，便馳進，橫馬斬謙、盛兵走者二人，兵皆還戰。')
BLOCK = Q('v055-b0062', '權征關羽，璋與朱然斷羽走道，到臨沮，住夾石。')
CAPTURE = Q('v055-b0062', '璋部下司馬馬忠禽羽，并羽子平、都督趙累等。')
YILING = Q('v055-b0062', '劉備出夷陵，璋與陸遜并力拒之，璋部下斬備護軍馮習等')
RAFT = Q('v055-b0063', '伐葦數百萬束，縛作大筏，欲順流放火，燒敗浮橋。作筏適畢，伺水長當下，尚便引退。')
LAST_OFFICE = Q('v055-b0063', '權稱尊號，拜右將軍。')
MISCONDUCT = Q('v055-b0064', '吏兵富者，或殺取其財物，數不奉法。監司舉奏，權惜其功而輒原不問。')
DEATH = Q('v055-b0064', '嘉禾三年卒。')
FAMILY = Q('v055-b0064', '嘉禾三年卒。子平，以無行徙會稽。璋妻居建業，賜田宅，復客五十家。')

PROFILE = dict(
    id='pan-zhang', tier='C', reading=['055'],
    new=dict(name='潘璋', courtesy='文珪', faction='孙吴', period='汉末—234年', aliases=['潘文珪'], tags=['合肥', '截断关羽退路', '夷陵']),
    eventRoles=[('hefei', '斩逃兵使其余回战'), ('jingzhou', '与朱然断关羽退路'), ('yiling', '拒刘备，部下斩冯习')],
    lead='潘璋早年追随孙权，先治市捕盗，后领兵征战。合肥遇袭时斩逃兵使部队回战；攻取荆州时与朱然截断关羽退路，部下马忠擒获关羽。孙权称帝后拜他为右将军；他晚年屡犯法，孙权因其战功一再宽宥。',
    role='孙吴右将军',
    facts=[
        dict(key='lifespan', label='生卒年', value='生年未详—234年', text='本传未记潘璋生年，只记他于嘉禾三年（234）去世。', refs=[DEATH]),
        dict(key='hometown', label='籍贯', value='东郡发干县', text='潘璋字文珪，东郡发干人。', refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='孙权早年招募的领兵将领', text='孙权为阳羡长时潘璋即往追随。孙权令他募兵，得百余人后以其为将。', refs=[JOIN, Q('v055-b0060', '因使召募，得百餘人，遂以爲將。')]),
        dict(key='office', label='最高官职', value='右将军', text='合肥战后拜偏将军；攻取荆州后任振威将军、固陵太守；夷陵战后任平北将军、襄阳太守；孙权称帝后，拜右将军。', refs=[Q('v055-b0061', '拜偏將軍'), Q('v055-b0062', '拜璋爲太守、振威將軍'), Q('v055-b0062', '拜平北將軍、襄陽太守。'), LAST_OFFICE]),
        dict(key='title', label='最高爵位', value='溧阳侯', text='孙权攻取荆州后，封潘璋为溧阳侯。', refs=[Q('v055-b0062', '拜璋爲太守、振威將軍，封溧陽侯。')]),
        dict(key='posthumous', label='身后称号', value='本书未载谥号', text='本传记潘璋死后其家获赐田宅等，不载潘璋追谥。', refs=[FAMILY]),
        dict(key='deeds', label='代表事迹', items=['治市捕盗', '督兵回战', '截断关羽退路', '夷陵拒蜀'], text='任吴大市刺奸时治盗，在合肥止住溃势，攻荆州时截关羽退路，夷陵时随陆逊拒蜀。', refs=[POLICING, HEFEI, BLOCK, YILING]),
    ],
    intro=[
        dict(title='从治市捕盗到领兵',
             text='潘璋字文珪，东郡发干人。孙权任阳羡长时他就来追随，虽家贫嗜酒，孙权却赏识他，让他招募百余人并领兵。后来他在吴大市负责查禁奸盗，据本传记载，盗贼因此断绝，他也由此出名。合肥之战中，张辽突击，陈武战死，宋谦、徐盛的队伍退走。潘璋原在后面，策马赶上，斩了两名逃兵，其他士兵回身再战，孙权以此拜他为偏将军。',
             refs=[ORIGIN, JOIN, Q('v055-b0060', '性博蕩嗜酒，居貧，好賒酤'), Q('v055-b0060', '權奇愛之，因使召募，得百餘人，遂以爲將。'), POLICING,
                   Q('v055-b0061', '合肥之役，張遼奄至，諸將不備，陳武鬬死'), HEFEI, Q('v055-b0061', '權甚壯之，拜偏將軍')],
             eventLinks=[dict(label='合肥之战', eventId='hefei')]),
        dict(title='截关羽去路，继拒刘备',
             text='219年孙权攻取荆州，潘璋与朱然截断关羽退路，他的部下司马马忠擒获关羽、关平等人，潘璋获封溧阳侯。刘备后来出兵夷陵，他随陆逊拒敌，部下斩刘备的护军冯习等人。魏军围南郡时，他另出一计，扎芦苇为大筏，准备待水涨顺流烧毁魏军浮桥；筏已做好，夏侯尚先撤了。孙权称帝后拜潘璋为右将军。本传亦记他晚年愈发奢侈，甚至杀吏兵取财，孙权爱惜他的功劳，屡次不追究。',
             refs=[Q('v047-b0018', '二十四年，關羽圍曹仁於襄陽'), BLOCK, CAPTURE, Q('v055-b0062', '封溧陽侯'), YILING, RAFT, LAST_OFFICE,
                   Q('v055-b0064', '然性奢泰，末年彌甚，服物僭擬。'), MISCONDUCT],
             eventLinks=[dict(label='孙权攻取荆州', eventId='jingzhou'), dict(label='刘备后来出兵夷陵', eventId='yiling')]),
    ],
    careers=[
        dict(id='early', when='汉末，确年未载', title='随孙权从军，兼治市与县', office='别部司马、吴大市刺奸，历任西安、建昌长',
             text='孙权命潘璋招兵，后拔擢他为别部司马。任吴大市刺奸后治盗有功，迁豫章西安长，后来转领建昌。', refs=[JOIN, Q('v055-b0060', '討山賊有功，署別部司馬。'), POLICING, Q('v055-b0060', '比縣建昌起爲賊亂，轉領建昌')]),
        dict(id='hefei', when='215年', title='合肥遇袭，止兵退走', office='偏将军', eventIds=['hefei'],
             text='张辽突来时，潘璋赶到前面制止溃逃，斩两名逃兵，士兵回战。', refs=[Q('v055-b0041', '建安二十年，從攻合肥'), HEFEI, Q('v055-b0061', '權甚壯之，拜偏將軍')]),
        dict(id='jingzhou', when='219年', title='与朱然截断关羽退路', office='振威将军、固陵太守，封溧阳侯', eventIds=['jingzhou'],
             text='与朱然受命截断关羽退走的道路。部下司马马忠擒获关羽、关平和赵累等。', refs=[Q('v056-b0009', '建安二十四年，從討關羽，別與潘璋到臨沮禽羽'), BLOCK, CAPTURE, Q('v055-b0062', '拜璋爲太守、振威將軍，封溧陽侯。')]),
        dict(id='yiling', when='222年', title='与陆逊共同拒刘备', office='平北将军、襄阳太守', eventIds=['yiling'],
             text='刘备兵至夷陵，潘璋受陆逊都督，部下斩蜀军护军冯习等人。', refs=[YILING, Q('v058-b0009', '黃武元年，劉備率大眾來向西界'), Q('v055-b0062', '拜平北將軍、襄陽太守。')]),
        dict(id='nanjun-relief', when='222—223年', title='扎苇筏备焚浮桥', office='—',
             text='夏侯尚等围南郡，潘璋截取上游芦苇做大筏，打算待江水上涨顺流火攻；未及实施，魏军撤退。', refs=[Q('v055-b0063', '魏將夏侯尚等圍南郡，分前部三萬人作浮橋'), RAFT, Q('v047-b0026', '是月，魏軍皆退。')]),
        dict(id='last', when='229—234年', title='拜右将军，卒于嘉禾三年', office='右将军',
             text='孙权称帝，潘璋拜右将军；嘉禾三年去世。', refs=[Q('v047-b0034', '丙申，南郊即皇帝位。'), LAST_OFFICE, DEATH]),
    ],
    records=[
        dict(section='civil', when='汉末，确年未载', title='在吴大市任刺奸', category='治市捕盗', careerRef='early',
             text='负责大市巡察纠禁，本传说任内盗贼断绝，此后潘璋由地方小吏进为西安长。', refs=[POLICING]),
        dict(section='military', when='219年', title='截断荆州败军退路', category='拦截擒将', careerRef='jingzhou', eventIds=['jingzhou'],
             text='与朱然提前截住关羽可能经过的道路，部下马忠最终擒得关羽等人。', refs=[BLOCK, CAPTURE]),
        dict(section='setback', when='晚年，确年未载', title='杀取部下财物，屡不奉法', category='违法侵财', careerRef='last',
             text='本传说潘璋晚年更加奢纵，有时杀害富有的吏兵，夺取财物。监察官举奏，孙权因珍惜其战功屡次宽免。', refs=[Q('v055-b0064', '然性奢泰，末年彌甚，服物僭擬。'), MISCONDUCT]),
    ],
    assessment=[
        dict(title='陈寿：孙权忘过记功', text='陈寿直言潘璋“不修”，转而赞赏孙权能记其功而宽其过。这是陈寿对孙权御将方略的评价；本传也明记被宽免的是屡次不守法。', refs=[Q('v055-b0073', '以潘璋之不脩，權能忘過記功，其保據東南，宜哉！'), MISCONDUCT]),
    ],
    relations=[
        dict(category='君臣', name='孙权', personId='sunquan', label='早年任用，晚年宽宥', text='孙权早年令潘璋募兵并让他领兵，称帝后拜右将军；潘璋屡犯法时，又多次宽免。', refs=[JOIN, Q('v055-b0060', '因使召募，得百餘人，遂以爲將。'), LAST_OFFICE, MISCONDUCT]),
        dict(category='同僚', name='朱然', label='联手截关羽', text='孙权命潘璋与朱然合力截断关羽退路。', refs=[BLOCK]),
        dict(category='部属', name='马忠', label='带兵擒关羽', text='马忠是潘璋部下司马，擒得关羽、关平和赵累。', refs=[CAPTURE]),
    ],
    readingNotes=[
        dict(title='堵路、擒获和斩杀的记载', text='《潘璋传》说潘璋与朱然截断退路、部下马忠擒获关羽。《关羽传》正文只说孙权遣将拦截、关羽父子在临沮被斩，没有点名执行者。两传可用来分清截路、擒获和被斩这几件事。', refs=[BLOCK, CAPTURE, Q('v036-b0006', '權遣將逆擊羽，斬羽及子平於臨沮。')]),
    ],
    sourceScope='以卷五十五《潘璋传》为主，参核卷三十六《关羽传》、卷四十七《吴主传》、卷五十六《朱然传》和卷五十八《陆逊传》。本页不声称穷尽全书所有提及潘璋之处。',
)
