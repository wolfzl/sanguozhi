"""张郃：以卷十七《张郃传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v017-b0014', '張郃字雋乂，河間鄚人也。')
YUAN = Q('v017-b0014', '馥敗，以兵歸袁紹。紹以郃爲校尉，使拒公孫瓚。瓚破，郃功多，遷寧國中郎將。')
WUCHAO = Q('v017-b0014', '瓊等破，則將軍事去矣，宜急引兵救之。')
DEFECTION = Q('v017-b0014', '太祖果破瓊等，紹軍潰。圖慚，又更譖郃曰：「郃快軍敗，出言不遜。」郃懼，乃歸太祖。')
ALTERNATE = Q('v001-b0051', '乃使張郃、高覽攻曹洪。郃等聞瓊破，遂來降。紹衆大潰')
ENLIST = Q('v017-b0015', '拜郃偏將軍，封都亭侯。')
ZHANGLU = Q('v017-b0015', '太祖從散關入漢中，又先遣郃督步卒五千於前通路。至陽平，魯降，太祖還，留郃與夏侯淵等守漢中，拒劉備。')
HANZHONG = Q('v017-b0015', '遂推郃爲軍主。郃出，勒兵安陳，諸將皆受郃節度，衆心乃定。')
RETREAT = Q('v017-b0015', '太祖乃引出漢中諸軍，郃還屯陳倉。')
JIETING = Q('v017-b0016', '遣督諸軍，拒亮將馬謖於街亭。謖依阻南山，不下據城。郃絶其汲道，擊，大破之。')
JIETING_YEAR = Q('v026-b0031', '太和二年，蜀相諸葛亮出祁山，遣將軍馬謖至街亭，高詳屯列柳城。張郃擊謖')
OFFICE = Q('v017-b0016', '詔郃還京都，拜征西車騎將軍。')
RECOMMEND = Q('v017-b0017', '郃雖武將而愛樂儒士，嘗薦同鄕卑湛經明行修')
DEATH = Q('v017-b0018', '郃追至木門，與亮軍交戰，飛矢中郃右膝，薨，諡曰壯侯。')
DEATH_YEAR = Q('v035-b0016', '九年，亮復出祁山，以木牛運，糧盡退軍，與魏將張郃交戰，射殺郃。')

PROFILE = dict(
    id='zhang-he', tier='C', reading=['017'],
    new=dict(name='张郃', courtesy='隽乂', faction='曹魏', period='汉末—231年',
             aliases=[], tags=['官渡', '汉中', '街亭', '木门']),
    eventRoles=[('guandu', '主张救乌巢，后归曹操'), ('zhanglu-surrender', '督步卒为大军开路'),
                ('hanzhong', '夏侯渊战死后整军'), ('first-northern-expedition', '街亭断水击败马谡')],
    lead='张郃原属袁绍，官渡之战转投曹操。夏侯渊战死后，他在汉中临时接掌诸军；诸葛亮首次北伐，他在街亭截断汲水道路，击败马谡。231年追击蜀军至木门时中箭阵亡。',
    role='曹魏征西车骑将军',

    facts=[
        dict(key='lifespan', label='生卒年', value='生年未详—231年',
             text='本传不记生年。卷三十五《诸葛亮传》记建兴九年（231）魏将张郃交战被射杀，本传详记其在木门中矢而死。',
             refs=[DEATH_YEAR, DEATH]),
        dict(key='hometown', label='籍贯', value='河间国鄚县',
             text='本传记张郃字隽乂，河间鄚人。', refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='从袁绍转投曹操的曹魏将领',
             text='先属韩馥、袁绍，官渡转投曹操。陈寿把他与张辽、乐进、于禁、徐晃列为曹操军中领先的良将。',
             refs=[YUAN, DEFECTION, Q('v017-b0028', '太祖建茲武功，而時之良將，五子爲先。')]),
        dict(key='office', label='最高官职', value='征西车骑将军',
             text='投曹后拜偏将军。曹丕即魏王位时任左将军，曹叡时加位特进，蜀军撤出陈仓后拜征西车骑将军。',
             refs=[ENLIST, Q('v017-b0016', '以郃爲左將軍'), Q('v017-b0016', '加郃位特進'), OFFICE]),
        dict(key='title', label='最高爵位', value='鄚侯',
             text='投曹后封都亭侯，曹丕即魏王位后进都乡侯、称帝后进鄚侯。',
             refs=[ENLIST, Q('v017-b0016', '進爵都鄕侯。及踐阼，進封鄚侯。')]),
        dict(key='posthumous', label='身后称号', value='壮侯',
             text='追蜀军至木门中箭而死，谥壮侯，由儿子张雄承袭。', refs=[DEATH, Q('v017-b0018', '子雄嗣。')]),
        dict(key='deeds', label='代表事迹', items=['官渡劝救乌巢', '汉中接掌诸军', '街亭断水破敌'],
             text='劝袁绍救援乌巢，夏侯渊战死后接掌汉中诸军，并在街亭击败马谡。',
             refs=[WUCHAO, HANZHONG, JIETING]),
    ],

    intro=[
        dict(title='官渡易主与汉中整军',
             text='张郃字隽乂，河间鄚人。汉末应募讨黄巾，先属韩馥，后归袁绍，因讨公孙瓒有功升任宁国中郎将。官渡之战中，他劝袁绍救援粮屯乌巢；乌巢被破后，张郃转投曹操，拜偏将军。曹操西取汉中时，张郃率步兵先行开路，随后留在当地拒刘备。219年夏侯渊战死，曹军失了主帅，郭淮推举张郃领军。他整顿阵列、号令诸将，军心才安定下来。曹操后来撤出汉中，张郃退屯陈仓。',
             refs=[ORIGIN, Q('v017-b0014', '漢末應募討黃巾，爲軍司馬，屬韓馥。'), YUAN, WUCHAO, DEFECTION, ENLIST, ZHANGLU,
                   Q('v017-b0015', '當是時，新失元帥，恐爲備所乘，三軍皆失色。'), HANZHONG, RETREAT],
             eventLinks=[dict(label='官渡之战', eventId='guandu'), dict(label='西取汉中', eventId='zhanglu-surrender'),
                         dict(label='夏侯渊战死', eventId='hanzhong')]),
        dict(title='街亭破敌，木门中矢',
             text='228年诸葛亮首次北伐，张郃奉命在街亭迎击蜀将马谡。马谡据南山，没有进城，张郃截断蜀军汲水的道路，大破其军。后来诸葛亮再攻陈仓，曹叡担心援军未到城就已失，张郃却估计蜀军粮食撑不到十天。他赶至南郑时，诸葛亮已经退兵，张郃随后被拜为征西车骑将军。231年诸葛亮再出祁山，史书又一次写到蜀军退兵；这次张郃追至木门，交战中右膝中箭而死。',
             refs=[JIETING_YEAR, JIETING, Q('v017-b0016', '亮得無已得陳倉乎！'), Q('v017-b0016', '屈指計亮糧不至十日。'),
                   Q('v017-b0016', '郃晨夜進至南鄭，亮退。'), OFFICE, DEATH_YEAR, DEATH],
             eventLinks=[dict(label='诸葛亮首次北伐', eventId='first-northern-expedition')]),
    ],

    careers=[
        dict(id='yuan-shao', when='汉末，确年未载', title='应募讨黄巾，转事袁绍', office='军司马，后迁宁国中郎将',
             text='应募为韩馥的军司马，韩馥败后归袁绍，拒击公孙瓒有功。', refs=[Q('v017-b0014', '漢末應募討黃巾，爲軍司馬，屬韓馥。'), YUAN]),
        dict(id='guandu', when='200年', title='劝救乌巢，转投曹操', office='偏将军、都亭侯', eventIds=['guandu'],
             text='张郃主张救乌巢，袁绍只遣轻骑驰援，以重兵攻曹营。曹操破乌巢后，张郃归曹，获封拜。',
             refs=[WUCHAO, Q('v017-b0014', '紹但遣輕騎救瓊，而以重兵攻太祖營，不能下。'), DEFECTION, ENLIST]),
        dict(id='yangping', when='215年', title='督步卒开路，留守汉中', office='—', eventIds=['zhanglu-surrender'],
             text='曹操自散关入汉中，命张郃率步兵在前开路。张鲁降后，张郃与夏侯渊等留守汉中。', refs=[ZHANGLU]),
        dict(id='hanzhong', when='219年', title='夏侯渊战死后接掌诸军', office='假节', eventIds=['hanzhong'],
             text='夏侯渊死后，郭淮推举张郃领军。张郃稳定诸营，曹操遣使假节；曹军退出汉中后，他退屯陈仓。',
             refs=[Q('v017-b0015', '淵遂沒，郃還陽平。'), Q('v017-b0015', '淵司馬郭淮乃令衆曰'), HANZHONG,
                   Q('v017-b0015', '太祖在長安，遣使假郃節。'), RETREAT]),
        dict(id='jieting', when='228年', title='街亭击败马谡', office='加位特进', eventIds=['first-northern-expedition'],
             text='张郃切断据南山的蜀军汲水道路，击败马谡。诸葛亮撤回汉中，响应他的三郡被魏平定。',
             refs=[JIETING, JIETING_YEAR, Q('v035-b0012', '亮拔西縣千余家，還于漢中'), Q('v003-b0006', '亮敗走，三郡平。')]),
        dict(id='mumen', when='231年', title='追击蜀军至木门，中箭而死', office='—',
             text='诸葛亮再次出祁山，粮尽退军；张郃率军追到木门，交战中右膝中箭而死。',
             refs=[DEATH_YEAR, DEATH]),
    ],

    records=[
        dict(section='civil', when='确年未载', title='荐举同乡卑湛', category='荐举儒士',
             text='张郃称卑湛精通经书、品行端正，魏明帝称许他的荐举，擢卑湛为博士。', refs=[RECOMMEND, Q('v017-b0017', '今擢湛爲博士。')]),
        dict(section='military', when='219年', title='汉中新失主帅后稳定军心', category='整顿军阵', careerRef='hanzhong', eventIds=['hanzhong'],
             text='夏侯渊战死后，郭淮认为只有张郃能安顿诸军。张郃接手后各部听其节度，稳住了曹军。',
             refs=[Q('v017-b0015', '今日事急，非張將軍不能安也。'), HANZHONG]),
        dict(section='military', when='228年', title='截断街亭蜀军汲水路', category='断水破敌', careerRef='jieting', eventIds=['first-northern-expedition'],
             text='马谡的军队据山，张郃发现其取水路线可以切断，以此破敌。蜀魏两方传记皆记马谡失利。',
             refs=[JIETING, Q('v035-b0012', '謖違亮節度，舉動失宜，大為張郃所破。')]),
        dict(section='setback', when='231年', title='追击退军，在木门阵亡', category='追击遇险', careerRef='mumen',
             text='正文记张郃追击而中矢阵亡，未说明追击是谁的决定。裴注引《魏略》另记司马懿命追，张郃曾反对，随后不得已出兵。',
             refs=[DEATH, Q('v017-b0018-n01', '亮軍退，司馬宣王使郃追之', '《魏略》'),
                   Q('v017-b0018-n01', '宣王不聽。郃不得已，遂進。', '《魏略》')]),
    ],

    assessment=[
        dict(title='陈寿：以巧变著称',
             text='陈寿称张郃以“巧变”闻名，又感到现存记载不够充分，不能像张辽、徐晃的传记那样完整呈现他的表现。',
             refs=[Q('v017-b0028', '張郃以巧變爲稱，樂進以驍果顯名，而鑑其行事，未副所聞。或注記有遺漏，未如張遼、徐晃之備詳也。')]),
    ],

    relations=[
        dict(category='旧主', name='袁绍', personId='yuanshao', label='受其任用，官渡转投曹操',
             text='袁绍任张郃为校尉，命拒公孙瓒；官渡时未全力救乌巢，后来张郃转投曹操。', refs=[YUAN, WUCHAO, DEFECTION]),
        dict(category='君臣', name='曹操', personId='caocao', label='受降封侯，汉中授节',
             text='曹操得张郃甚喜，封为都亭侯。夏侯渊战死后曹操又遣使授张郃军节。',
             refs=[Q('v017-b0015', '太祖得郃甚喜'), ENLIST, Q('v017-b0015', '太祖在長安，遣使假郃節。')]),
        dict(category='同僚', name='夏侯渊', personId='xiahou-yuan', label='同守汉中，渊死后领军',
             text='二人同守汉中；夏侯渊战死后，张郃被推举接掌诸军。', refs=[ZHANGLU, Q('v017-b0015', '淵遂沒，郃還陽平。'), HANZHONG]),
        dict(category='敌对', name='马谡', personId='ma-su', label='街亭交锋',
             text='马谡在街亭据山，张郃断其取水道路，击败所部。', refs=[JIETING]),
    ],

    readingNotes=[
        dict(title='官渡投曹在袁军溃散之前还是之后',
             text='《张郃传》写乌巢被破后袁军先溃，张郃害怕郭图进谗才投曹。《武帝纪》《袁绍传》都把张郃、高览投降写在袁军大溃之前，裴松之已指出两种叙事顺序不同。',
             refs=[DEFECTION, ALTERNATE, Q('v006-b0026', '紹將高覽、張郃等率其衆降。紹衆大潰'),
                   Q('v017-b0014-n02', '是則緣郃等降而後紹軍壞也。', '裴松之案')]),
    ],
    sourceScope='以卷十七《张郃传》为主，参看卷一《武帝纪》、卷三《明帝纪》及卷六《袁绍传》、卷二十六《郭淮传》、卷三十五《诸葛亮传》。本页不声称穷尽全书所有提及张郃之处。',
)
