"""黄盖：以卷五十五《黄盖传》及卷五十四《周瑜传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v055-b0007', '黃蓋字公覆，零陵泉陵人也。')
EARLY = Q('v055-b0007', '初爲郡吏，察孝廉，辟公府。')
SUN_JIAN = Q('v055-b0007', '孫堅舉義兵，蓋從之。堅南破山賊，北走董卓，拜蓋別部司馬。')
SUCCESSORS = Q('v055-b0007', '堅薨，蓋隨策及權，擐甲周旋，蹈刃屠城。')
SUN_CE = Q('v049-b0012', '策從騎十三，皆韓當、宋謙、黃蓋輩也。')
STONE_COUNTY = Q('v055-b0008', '石城縣吏，特難檢御，蓋乃署兩掾，分主諸曹。')
EXECUTED = Q('v055-b0008', '「前已相勑，終不以鞭杖相加，非相欺也。」遂殺之。縣中震慄。')
NINE_COUNTIES = Q('v055-b0008', '後轉春穀長，尋陽令。凡守九縣，所在平定。')
DANYANG = Q('v055-b0008', '遷丹楊都尉，抑彊扶弱，山越懷附。')
FIRE_PLAN = Q('v054-b0008', '今寇眾我寡，難與持久。然觀操軍船艦，首尾相接，可燒而走也。')
FALSE_SURRENDER = Q('v054-b0008', '裹以帷幕，上建牙旗，先書報曹公，欺以欲降。')
FIRE = Q('v054-b0008', '蓋放諸船，同時發火。時風盛猛，悉延燒岸上營落。')
CHIBI_OFFICE = Q('v055-b0009', '建策火攻，語在〈瑜傳〉。拜武鋒中郎將。')
RESCUE = Q('v055-b0009-n01', '當聞之，曰：「此公覆聲也。」向之垂涕，解易其衣，遂以得生。', '《吴书》')
WULING = Q('v055-b0009', '武陵蠻夷反亂，攻守城邑，乃以蓋領太守。')
AMBUSH = Q('v055-b0009', '時郡兵才五百人，自以不敵，因開城門，賊半入，乃擊之')
PARDON = Q('v055-b0009', '誅討魁帥，附從者赦之。')
DEATH = Q('v055-b0009', '後長沙益陽縣爲山賊所攻，蓋又平討。加偏將軍，病卒于官。')
HONOR = Q('v055-b0010', '及權踐阼，追論其功，賜子柄爵關內侯。')

PROFILE = dict(
    id='huang-gai',
    tier='C',
    reading=['055', '054'],
    lead='黄盖历事孙坚、孙策、孙权。赤壁之战中，他判断曹军船舰相连，向周瑜提出火攻，又以诈降掩护火船接敌。战后领武陵太守，平定当地叛乱，升偏将军，最终病卒任上。',
    role='历事孙氏三代的武将',

    facts=[
        dict(key='lifespan', label='生卒年', value='生年不详—208年以后',
             text='本传未载生年；赤壁之战后，他领武陵太守，平定武陵、益阳的战事之后病卒，确年未载。',
             refs=[CHIBI_OFFICE, WULING, DEATH]),
        dict(key='hometown', label='籍贯', value='零陵郡泉陵县',
             text='本传记黄盖是零陵泉陵人。裴注引《吴书》说，他的祖辈迁到零陵，家族遂定居当地。',
             refs=[ORIGIN, Q('v055-b0007-n01', '自祖遷于零陵，遂家焉。', '《吴书》')]),
        dict(key='identity', label='主要身份', value='孙氏旧部、赤壁火攻的献策者',
             text='孙坚举兵时开始跟随，孙坚死后继续随孙策、孙权征战。赤壁时为周瑜部将，提出火攻。',
             refs=[SUN_JIAN, SUCCESSORS, FIRE_PLAN]),
        dict(key='office', label='最高官职', value='偏将军，领武陵太守',
             text='初拜别部司马。历任多县守长，迁丹杨都尉。赤壁献计后拜武锋中郎将，后领武陵太守，加偏将军。',
             refs=[SUN_JIAN, NINE_COUNTIES, DANYANG, CHIBI_OFFICE, WULING, DEATH]),
        dict(key='posthumous', label='身后称号', value='未载谥号；孙权追论其功',
             text='孙权即帝位后追论黄盖的功劳，赐其子黄柄关内侯爵。关内侯是黄柄所受之爵，本传未载黄盖本人的谥号。',
             refs=[HONOR]),
        dict(key='deeds', label='代表事迹', items=['石城治吏', '赤壁火攻', '武陵平乱'],
             text='出任石城守长，整饬属吏；在赤壁献策并实施火攻；领武陵太守后平定叛乱。',
             refs=[STONE_COUNTY, EXECUTED, FIRE_PLAN, FIRE, WULING, AMBUSH, PARDON]),
    ],

    intro=[
        dict(title='从军与治理县邑',
             text='黄盖字公覆，起初任郡吏，经举荐为孝廉，又获公府征辟。孙坚起兵后，他随军南击山贼、北讨董卓，拜别部司马；孙坚死后，他又追随孙策和孙权。《太史慈传》记载，孙策与太史慈猝然相遇时，身边的十三名随骑中就有黄盖等人。黄盖也常被派到遭受袭扰的县任职。在石城，他把文书分交两名属吏，令他们督察各曹；后来查到两人自己多次违法，便召集属吏，当面诘问并处死二人，全县震动。他先后出任九县守长，后来升任丹杨都尉。',
             refs=[ORIGIN, EARLY, SUN_JIAN, SUCCESSORS, SUN_CE, STONE_COUNTY,
                   Q('v055-b0008', '各得兩掾不奉法數事。乃悉請諸掾吏，賜酒食，因出事詰問。'),
                   EXECUTED, NINE_COUNTIES, DANYANG],
             eventLinks=[dict(label='北讨董卓', eventId='anti-dong-coalition'),
                         dict(label='孙策与太史慈猝然相遇', eventId='sun-ce-jiangdong')]),
        dict(title='赤壁献策与武陵平乱',
             text='208年赤壁之战，黄盖判断己方兵少，难以久战，但曹军船舰首尾相连，正可用火。吴军把柴草、油脂装进战船，另系小船备撤；黄盖先向曹操诈降，再纵船点火，借风烧到岸边营地。黄盖后来领武陵太守，手中只有五百名郡兵，便开城门，等攻城者进了一半才出击。平乱时他诛讨首领，赦免跟从者。此后他又平定攻打益阳的山贼，加偏将军，病卒任上。',
             refs=[FIRE_PLAN, Q('v054-b0008', '乃取蒙沖鬥艦數十艘，實以薪草，膏油灌其中。'),
                   FALSE_SURRENDER, Q('v054-b0008', '又豫備走舸，各系大船後'), FIRE,
                   WULING, AMBUSH, PARDON, DEATH],
             eventLinks=[dict(label='赤壁之战', eventId='chibi')]),
    ],

    careers=[
        dict(id='clerk', when='早年，确年未载', title='由郡吏获举荐', office='郡吏',
             text='任郡吏，经察举为孝廉，后获公府征辟。', refs=[EARLY]),
        dict(id='sun-jian', when='190年起', title='随孙坚讨董', office='别部司马', eventIds=['anti-dong-coalition'],
             text='随孙坚起兵，先南击山贼，后北讨董卓，获拜别部司马。', refs=[SUN_JIAN]),
        dict(id='jiangdong', when='195—196年', title='随孙策征战江东', office='—', eventIds=['sun-ce-jiangdong'],
             text='孙坚去世后转随孙策。孙策与太史慈相遇时，黄盖在孙策的随骑中。', refs=[SUCCESSORS, SUN_CE]),
        dict(id='county-office', when='任县守长时，确年未载', title='历治九县，迁丹杨都尉', office='县守长，后迁丹杨都尉',
             text='常获派到遭受袭扰的县，先后历任石城、春谷、寻阳等九县守长；迁丹杨都尉后，本传称他抑强扶弱，山越归附。',
             refs=[Q('v055-b0008', '有寇難之縣，輙用蓋爲守長。'), STONE_COUNTY, NINE_COUNTIES, DANYANG]),
        dict(id='chibi', when='208年', title='向周瑜献火攻计', office='武锋中郎将', eventIds=['chibi'],
             text='看准曹军船舰相连，先诈降，再发火烧船，火势延烧岸营。战后拜武锋中郎将。',
             refs=[FIRE_PLAN, FALSE_SURRENDER, FIRE, CHIBI_OFFICE]),
        dict(id='wuling', when='赤壁战后，确年未载', title='平定武陵、益阳，病卒', office='领武陵太守，加偏将军',
             text='领武陵太守时以少兵开城诱敌，平乱后赦免跟从者；又平定攻击益阳的山贼，加偏将军，病卒任上。',
             refs=[WULING, AMBUSH, PARDON, DEATH]),
    ],

    records=[
        dict(section='civil', when='任丹杨都尉时，确年未载', title='抑强扶弱', category='地方治理', careerRef='county-office',
             text='本传认为他遏制强横者、扶助弱小者，使当地山越归附。传文只概括了结果，没有记下具体政令。',
             refs=[DANYANG]),
        dict(section='military', when='208年', title='用火船瓦解曹军船营', category='水战决策', careerRef='chibi', eventIds=['chibi'],
             text='船舰首尾相连，使火势容易蔓延；诈降又让曹军没有立即拦截。黄盖的办法正针对敌军布置与己方兵少的处境。',
             refs=[FIRE_PLAN, FALSE_SURRENDER, Q('v054-b0008', '曹公軍吏士皆延頸觀望，指言蓋降。'), FIRE]),
        dict(section='setback', when='任石城时，确年未载', title='处死两掾以震慑县吏', category='严酷处置', careerRef='county-office',
             text='黄盖曾告诫两掾若有欺弊也不加鞭杖，查得他们违法后却以这条告诫为由直接处死二人。本传记下了县中的恐惧，没有交代审判程序。',
             refs=[Q('v055-b0008', '若有姦欺，終不加以鞭杖'), EXECUTED]),
        dict(section='setback', when='208年', title='中箭落水，一度无人识认', category='战场受伤', careerRef='chibi', eventIds=['chibi'],
             text='裴注引《吴书》记黄盖在赤壁中流矢、坠入寒水。吴军捞起他后没有认出来，直到他呼喊韩当才得到救护。',
             refs=[Q('v055-b0009-n01', '蓋爲流矢所中，時寒墮水，爲吳軍人所得，不知其蓋也', '《吴书》'),
                   Q('v055-b0009-n01', '蓋自彊以一聲呼韓當', '《吴书》'), RESCUE]),
    ],

    assessment=[
        dict(title='陈寿：江表虎臣', text='陈寿把黄盖等人合评为“江表之虎臣”，说孙氏厚待这些将领；黄盖本传也记他办事果断，死后国人仍怀念他。',
             refs=[Q('v055-b0073', '凡此諸將，皆江表之虎臣，孫氏之所厚待也。'),
                   Q('v055-b0010', '蓋當官決斷，事無留滯，國人思之。')]),
    ],

    relations=[
        dict(category='旧主', name='孙坚', personId='sun-jian', label='从起兵，拜别部司马',
             text='黄盖在孙坚起兵时追随，随他南破山贼、北讨董卓，获拜别部司马。', refs=[SUN_JIAN]),
        dict(category='旧主', name='孙策', personId='sun-ce', label='随军征战江东',
             text='孙坚死后，黄盖随孙策征战；《太史慈传》记黄盖在孙策的随骑中。', refs=[SUCCESSORS, SUN_CE]),
        dict(category='同僚', name='周瑜', personId='zhouyu', label='在其麾下献火攻计',
             text='黄盖以周瑜部将身份提出烧曹军船舰，并亲自下令放火。', refs=[FIRE_PLAN, FIRE]),
        dict(category='同僚', name='韩当', personId='han-dang', label='赤壁遇险时获其救护',
             text='裴注引《吴书》记韩当在赤壁辨出黄盖的声音，为他更换衣物，黄盖才得以生还。', refs=[RESCUE]),
    ],

    readingNotes=[
        dict(title='火攻与焚余船是两段记载',
             text='《周瑜传》详叙黄盖诈降、纵火，写火势烧到岸营；《吴主传》还记曹操烧余船而退。《武帝纪》只记交战失利、军中大疫后撤军。三处着眼不同，可对读战况。',
             refs=[FALSE_SURRENDER, FIRE, Q('v047-b0009', '公燒其餘船引退，士卒饑疫，死者大半。'),
                   Q('v001-b0073', '公至赤壁，與備戰，不利。於是大疫，吏士多死者，乃引軍還。')]),
    ],

    sourceScope='以卷五十五《黄盖传》正文为主，赤壁战况参看卷五十四《周瑜传》、卷四十七《吴主传》与卷一《武帝纪》，江东从征参看卷四十九《太史慈传》；裴注《吴书》的记载另标出处。本页不声称穷尽全书所有提及黄盖之处。',
)
