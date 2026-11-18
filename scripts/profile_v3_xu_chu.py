"""许褚：以卷十八《许褚传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v018-b0029', '許褚字仲康，譙國譙人也。')
VILLAGE = Q('v018-b0029', '漢末，聚少年及宗族數千家，共堅壁以御寇。')
STONES = Q('v018-b0029', '兵矢盡，乃令壁中男女，聚治石如杅鬥者置四隅。褚飛石擲之，所值皆摧碎。賊不敢進。')
RECRUIT = Q('v018-b0030', '太祖徇淮、汝，褚以眾歸太祖。')
GUARD = Q('v018-b0030', '此吾樊噲也。」即日拜都尉，引入宿衛。諸從褚俠客，皆以為虎士。')
PLOT = Q('v018-b0030', '從討袁紹於官渡。時常從士徐他等謀為逆，以褚常侍左右，憚之不敢發。')
KILLED_PLOTTERS = Q('v018-b0030', '他色變，褚覺之，即擊殺他等。太祖益親信之，出入同行，不離左右。')
FERRY = Q('v018-b0030', '乃扶太祖上船。')
SADDLE = Q('v018-b0030', '左手舉馬鞍蔽太祖。')
TIGER = Q('v018-b0030', '公有虎侯者安在？」太祖顧指褚，褚瞋目盼之。超不敢動，乃各罷。')
TIGER_NICKNAME = Q('v018-b0030', '軍中以褚力如虎而痴，故號曰虎痴')
OFFICE = Q('v018-b0031', '文帝踐阼，進封萬歲亭侯，遷武衛將軍，都督中軍宿衛禁兵，甚親近焉。')
TITLE = Q('v018-b0031', '明帝即位，進牟鄉侯，邑七百戶，賜子爵一人關內侯。褚薨，謚曰壯侯。')
OMISSION = Q('v004-b0011-n01', '且潼關之危，非褚不濟，褚之功烈有過典韋，今祀韋而不及褚，文所未達也。', '裴松之案')

PROFILE = dict(
    id='xu-chu',
    tier='C',
    reading=['018'],
    new=dict(name='许褚', courtesy='仲康', faction='曹魏', period='汉末—魏明帝时',
             aliases=['虎痴', '虎侯'], tags=['虎士', '潼关', '宿卫']),
    eventRoles=[('guandu', '识破徐他等人图谋'), ('tongguan', '护曹操渡河及会谈')],
    lead='曹操亲卫，军中号“虎痴”。官渡时识破徐他等人的图谋；潼关之战中护曹操渡河，随曹操与马超会谈。曹丕称帝后任武卫将军，总领中军宿卫禁兵，卒谥壮侯。',
    role='曹魏武卫将军',

    facts=[
        dict(key='lifespan', label='生卒年', value='生卒年未详',
             text='本传没有记载生年，也没有写明卒年，只在曹叡即位、封他为牟乡侯之后记其去世。',
             refs=[TITLE]),
        dict(key='hometown', label='籍贯', value='谯国谯县',
             text='本传开篇称他是谯国谯人，字仲康。',
             refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='曹操亲卫，后统领曹魏宿卫禁兵',
             text='归曹后入宿卫，同来的侠客编为虎士；曹丕称帝后，由许褚总督中军禁兵。',
             refs=[RECRUIT, GUARD, OFFICE]),
        dict(key='office', label='最高官职', value='武卫将军',
             text='归曹时拜都尉，潼关战后迁武卫中郎将，继任中坚将军；曹丕称帝后任武卫将军。',
             refs=[GUARD, Q('v018-b0030', '遷武衛中郎將。武衛之號，自此始也。'), Q('v018-b0031', '遷中堅將軍。'), OFFICE]),
        dict(key='posthumous', label='身后称号', value='壮侯',
             text='本传记他去世后谥壮侯；《齐王纪》所载曹操庙庭配享名单未列许褚，裴松之对此提出异议。',
             refs=[TITLE, OMISSION]),
        dict(key='deeds', label='代表事迹', items=['乡里御寇', '潼关护主', '总督禁兵'],
             text='聚乡族抵御来寇；潼关战时护曹操渡河；曹丕即位后统领宿卫禁兵。',
             refs=[VILLAGE, FERRY, SADDLE, OFFICE]),
    ],

    intro=[
        dict(title='率乡里自保，继而入宿卫',
             text='许褚是谯国谯人，字仲康，以勇力出众闻名。汉末战乱中，他聚集乡里少年和宗族数千家，筑起营垒抵挡来攻之寇。一次箭矢用尽，他让营中男女聚拢石块，自己投石阻击，来军不敢再进。曹操进取淮、汝一带时，许褚带部众归附，曹操称他是自己的樊哙，当日就任为都尉、引入宿卫，随他归附的侠客编为虎士。官渡之战期间，徐他等人携刀入帐，发现当天轮休的许褚已经回来，神色有变；许褚察觉后杀了他们，曹操更加信任他。',
             refs=[ORIGIN, Q('v018-b0029', '容貌雄毅，勇力絕人。'), VILLAGE, STONES, RECRUIT, GUARD, PLOT,
                   Q('v018-b0030', '伺褚休下日，他等懷刀入。褚至下捨心動，即還侍。'),
                   Q('v018-b0030', '他等不知，入帳見褚，大驚愕。'), KILLED_PLOTTERS],
             eventLinks=[dict(label='官渡之战', eventId='guandu')]),
        dict(title='渡河护主，后来掌禁兵',
             text='潼关之战中，许褚和虎士留在南岸随曹操断后。马超军赶来，许褚扶曹操上船，用马鞍遮挡来箭，曹操得以渡河。后来曹操与韩遂、马超会谈，只带许褚在身边；马超原想突前，认出许褚后没有动手。两人在战场上的这次会面，也见于《马超传》。潼关一战结束，许褚迁武卫中郎将；曹丕称帝后，他又升武卫将军，总领中军宿卫禁兵。',
             refs=[Q('v018-b0030', '獨與褚及虎士百餘人留南岸斷後。超將步騎萬餘人，來奔太祖軍，矢下如雨。'),
                   FERRY, SADDLE, Q('v018-b0030', '僅乃得渡。'), Q('v018-b0030', '左右皆不得從，唯將褚。'), TIGER,
                   Q('v036-b0014', '曹公左右將許褚瞋目盻之，超乃不敢動。'),
                   Q('v018-b0030', '遷武衛中郎將。武衛之號，自此始也。'), OFFICE],
             eventLinks=[dict(label='潼关之战', eventId='tongguan')]),
    ],

    careers=[
        dict(id='village', when='汉末，确年未载', title='率少年与宗族固守营垒', office='未仕',
             text='组织乡族自保；葛陂来军围攻时，营中箭尽，曾聚石抵御。',
             refs=[VILLAGE, Q('v018-b0029', '時汝南葛陂賊萬餘人攻褚壁'), STONES]),
        dict(id='guard', when='曹操进取淮、汝时，确年未载', title='率众归曹，入宿卫', office='都尉，后迁校尉',
             text='率部归附曹操，拜都尉、入宿卫。随征张绣时登城在先，升为校尉。',
             refs=[RECRUIT, GUARD, Q('v018-b0030', '從徵張繡，先登，斬首萬計，遷校尉。')]),
        dict(id='guandu', when='200年', title='察觉徐他等谋刺', office='—', eventIds=['guandu'],
             text='在官渡从征期间，徐他等趁他休息时怀刀入帐，没料到他提前回去宿卫，最终为他察觉并击杀。',
             refs=[Q('v001-b0047', '公還軍官渡。紹進保陽武。'), PLOT, Q('v018-b0030', '伺褚休下日，他等懷刀入。褚至下捨心動，即還侍。'), KILLED_PLOTTERS]),
        dict(id='tongguan', when='211年', title='护曹操渡河，随同会谈', office='武卫中郎将', eventIds=['tongguan'],
             text='渡河遇袭时护曹操登船，随后陪同曹操会见韩遂、马超；战后迁武卫中郎将。',
             refs=[Q('v001-b0076', '十六年春正月'), Q('v001-b0077', '公自潼關北渡，未濟，超赴船急戰。'),
                   FERRY, SADDLE, TIGER, Q('v018-b0030', '遷武衛中郎將。武衛之號，自此始也。')]),
        dict(id='late-offices', when='曹丕称帝后至明帝时', title='总督禁兵，进封牟乡侯', office='武卫将军；封牟乡侯',
             text='曹丕称帝后迁武卫将军，总督中军禁兵。明帝即位后，他进封牟乡侯，卒谥壮侯。',
             refs=[OFFICE, TITLE]),
        dict(id='shrine-debate', when='243年', title='未列曹操庙庭配享诏', office='—',
             text='曹芳正始四年诏祀典韦等人于曹操庙庭，名单上没有许褚。裴松之在注文中提出质疑。',
             refs=[Q('v004-b0010', '武猛校尉典韋於太祖廟庭。'), OMISSION]),
    ],

    records=[
        dict(section='military', when='211年', title='断后遇袭时护主', category='近身护卫', careerRef='tongguan', eventIds=['tongguan'],
             text='曹操渡河时面对马超军追击，许褚扶他上船、以马鞍护他。本传认为当日没有许褚，曹操几乎遇险。',
             refs=[FERRY, SADDLE, Q('v018-b0030', '是日，微褚幾危。')]),
        dict(section='setback', when='243年', title='未列配享名单的争议', category='身后祭祀', careerRef='shrine-debate',
             text='裴松之认为，许褚在潼关护卫曹操，功劳超过典韦，因而不理解为何典韦入祀而许褚没有入祀。这是裴松之的比较和疑问，诏书未说明许褚落选的缘由。',
             refs=[Q('v004-b0010', '武猛校尉典韋於太祖廟庭。'), OMISSION]),
    ],
    sections={
        'civil': {'note': '许褚的事迹集中在乡里御寇、随军与宫中宿卫；本传未载他出任地方行政官或主持具体政务。'},
    },

    relations=[
        dict(category='君臣', name='曹操', personId='caocao', label='受命宿卫',
             text='归附当天即被曹操任为都尉、引入宿卫；察觉徐他等人的图谋后，越发受到信任。',
             refs=[GUARD, PLOT, KILLED_PLOTTERS]),
        dict(category='同僚', name='曹仁', personId='cao-ren', label='拒绝私下交谈',
             text='曹仁回朝邀他入内交谈，许褚认为自己身为内臣，与外任宗亲公开谈话已经足够，曹操闻知后更为看重。',
             refs=[Q('v018-b0031', '仁呼褚入便坐語，褚曰：「王將出。」'),
                   Q('v018-b0031', '褚備內臣，眾談足矣，入室何私乎？」太祖聞，愈愛待之')]),
        dict(category='敌对', name='马超', personId='ma-chao', label='潼关会谈相对',
             text='马超会谈时想突前擒拿曹操，见到许褚后没有动手，两人的传记都记有这段相遇。',
             refs=[TIGER, Q('v036-b0014', '陰欲突前捉曹公，曹公左右將許褚瞋目盻之，超乃不敢動。')]),
    ],

    assessment=[
        dict(title='陈寿：许褚、典韦可比樊哙',
             text='陈寿并论许褚与典韦，以汉初的樊哙作比，着眼于二人在主将身边护卫御敌的功劳。',
             refs=[Q('v018-b0050', '許褚、典韋折衝左右，抑亦漢之樊噲也。')]),
    ],

    readingNotes=[
        dict(title='“虎侯”是称呼，“牟乡侯”是封爵',
             text='《许褚传》说军中号许褚“虎痴”，并记马超称他“虎侯”；明帝即位后进封的牟乡侯，才是正式的封爵。',
             refs=[TIGER_NICKNAME, TIGER, TITLE]),
    ],

    sourceScope='以卷十八《许褚传》为基础，对读卷一《武帝纪》、卷三十六《马超传》及卷四《齐王纪》所载配享诏与裴松之按语。本页不声称穷尽全书所有提及许褚之处。',
)
