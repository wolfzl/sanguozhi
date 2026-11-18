"""周泰：以卷五十五《周泰传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v055-b0020', '周泰字幼平，九江下蔡人也。')
JOIN = Q('v055-b0020', '與蔣欽隨孫策爲左右，服事恭敬，數戰有功。策入會稽，署別部司馬，授兵。')
SAVE = Q('v055-b0020', '惟泰奮激，投身衞權，膽氣倍人，左右由泰並能就戰。')
WOUNDS = Q('v055-b0020', '賊旣解散，身被十二創，良乆乃蘇。是日無泰，權幾危殆。')
CHIBI_NANJUN = Q('v055-b0021', '後與周瑜、程普拒曹公於赤壁，攻曹仁於南郡。')
RUXU = Q('v055-b0021', '曹公出濡須，泰復赴擊，曹公退，留督濡須，拜平虜將軍。')
COMMAND = Q('v055-b0021', '時朱然、徐盛等皆在所部，並不伏也')
BANQUET = Q('v055-b0021', '權自行酒到泰前，命泰解衣，權手自指其創痕，問以所起。泰輒記昔戰鬬處以對')
HONOR = Q('v055-b0021', '遣使者授以御蓋。於是盛等乃伏。')
DEATH = Q('v055-b0022', '後權破關羽，欲進圖蜀，拜泰漢中太守、奮威將軍，封陵陽侯。黃武中卒。')

PROFILE = dict(
    id='zhou-tai', tier='C', reading=['055'],
    new=dict(name='周泰', courtesy='幼平', faction='孙吴', period='汉末—孙吴黄武年间', aliases=['周幼平'], tags=['宣城护主', '赤壁', '濡须督']),
    eventRoles=[('sun-ce-jiangdong', '随孙策征战，入会稽授兵'), ('chibi', '随周瑜、程普拒曹'), ('nanjun-campaign', '随军进攻曹仁')],
    lead='周泰先随孙策转战江东，后在宣城拼死护卫孙权，身受十二处创伤。随周瑜、程普在赤壁拒曹、进攻南郡后，他又督守濡须；部将起初不服，孙权在宴上以一身旧伤为他立威。',
    role='曾督濡须的孙吴武将',
    facts=[
        dict(key='lifespan', label='生卒年', value='生年未详—黄武年间', text='本传未记生年，只记黄武年间（222—229）去世。', refs=[DEATH]),
        dict(key='hometown', label='籍贯', value='九江郡下蔡县', text='周泰字幼平，九江下蔡人。', refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='孙氏护卫出身的领兵将领', text='先为孙策左右，后被孙权请来随侍；赤壁、南郡从征后任濡须督。', refs=[JOIN, Q('v055-b0020', '權愛其爲人，請以自給。'), CHIBI_NANJUN, RUXU]),
        dict(key='office', label='最高官职', value='奋威将军，领汉中太守', text='曾任别部司马、平虏将军并督濡须。孙权破关羽后准备进图蜀地，授他汉中太守、奋威将军；这是任命，本传未载其到汉中任事。', refs=[JOIN, RUXU, DEATH]),
        dict(key='title', label='最高爵位', value='陵阳侯', text='孙权在任命周泰为奋威将军、汉中太守时，封其为陵阳侯。', refs=[DEATH]),
        dict(key='posthumous', label='身后称号', value='本书未载谥号', text='本传只记周泰卒于黄武年间，未记追谥。', refs=[DEATH]),
        dict(key='deeds', label='代表事迹', items=['宣城护主', '赤壁拒曹', '南郡攻坚', '留督濡须'], text='在宣城护卫孙权，跟随周瑜、程普拒曹并攻南郡，后来督守濡须。', refs=[SAVE, CHIBI_NANJUN, RUXU]),
    ],
    intro=[
        dict(title='江东从军，宣城护主',
             text='周泰字幼平，与同是九江人的蒋钦一同追随孙策。孙策经略江东，进驻会稽后任他为别部司马，授给他兵众；孙权喜欢他的为人，又向兄长请他来随侍。孙策外出讨山贼时，孙权驻宣城，守兵不足千人，又没有修治营垒。山贼数千人猝然来袭，刀刃已逼到孙权身旁，甚至砍到马鞍。周泰奋身护住孙权，左右受其带动也投入战斗。敌人散去后，周泰身上有十二处伤，许久才醒转。孙策深为感激，任他为春谷长。',
             refs=[ORIGIN, JOIN, Q('v055-b0015', '蔣欽字公弈，九江壽春人也。'), Q('v055-b0020', '權愛其爲人，請以自給。'), Q('v055-b0020', '不能千人，意尚忽略，不治圍落，而山賊數千人卒至。'), Q('v055-b0020', '或斫中馬鞌'), SAVE, WOUNDS, Q('v055-b0020', '策深德之，補春穀長。')],
             eventLinks=[dict(label='孙策经略江东', eventId='sun-ce-jiangdong')]),
        dict(title='赤壁拒曹，受命镇守',
             text='周泰后来随周瑜、程普在赤壁抵御曹操，接着进攻南郡的曹仁。曹操攻濡须时，他又赴援，曹军退走后受命留督濡须。部将朱然、徐盛起初不服，孙权亲自来到濡须坞设宴，让周泰解衣，指着一道道伤痕，问他各是在哪一仗受的伤；次日又赐他自己所用的仪仗车盖，众将这才服从。孙权击败关羽后封周泰为陵阳侯，周泰于黄武年间去世。',
             refs=[CHIBI_NANJUN, RUXU, COMMAND, BANQUET, HONOR, DEATH],
             eventLinks=[dict(label='在赤壁抵御曹操', eventId='chibi'), dict(label='进攻南郡', eventId='nanjun-campaign')]),
    ],
    careers=[
        dict(id='jiangdong', when='195—196年间', title='随孙策经营江东，入会稽授兵', office='别部司马', eventIds=['sun-ce-jiangdong'],
             text='与蒋钦同为孙策左右，屡战立功。孙策进据会稽时任命周泰为别部司马、拨给兵众。', refs=[JOIN, Q('v046-b0014-n02', '策渡江攻繇牛渚營，盡得邸閣糧穀、戰具，是歳興平二年也。', '《江表传》')]),
        dict(id='xuancheng', when='孙策在世时，确年未载', title='宣城负创护卫孙权', office='春谷长，后任宜春长',
             text='孙权留驻宣城，遇数千山贼突袭。周泰舍身护主，身受十二处创伤；其后历任春谷、宜春二县长。', refs=[SAVE, WOUNDS, Q('v055-b0020', '策深德之，補春穀長。'), Q('v055-b0020', '還過豫章，復補宜春長')]),
        dict(id='chibi-nanjun', when='208—209年', title='随军在赤壁、南郡抗曹', office='—', eventIds=['chibi', 'nanjun-campaign'],
             text='随周瑜、程普在赤壁抗击曹军，又参与南郡之战，进攻曹仁。', refs=[CHIBI_NANJUN, Q('v047-b0010', '十四年，瑜、仁相守歳餘，所殺傷甚眾。仁委城走。')]),
        dict(id='ruxu', when='赤壁、南郡战后，确年未载', title='镇守濡须，孙权亲临立威', office='平虏将军，督濡须',
             text='曹操攻濡须，周泰赴击；曹军退后留督濡须。朱然、徐盛等起初不服，孙权设宴示众他的战伤，并赐御盖。', refs=[RUXU, COMMAND, BANQUET, HONOR]),
        dict(id='last', when='219年以后至黄武年间', title='封陵阳侯，卒于黄武年间', office='汉中太守、奋威将军，封陵阳侯',
             text='孙权破关羽后准备进图蜀地，拜周泰为汉中太守、奋威将军，封陵阳侯。周泰于黄武年间去世，死因未载。', refs=[Q('v047-b0018', '二十四年，關羽圍曹仁於襄陽'), DEATH]),
    ],
    records=[
        dict(section='military', when='孙策在世时，确年未载', title='宣城挡住突袭', category='护卫救援', careerRef='xuancheng',
             text='守军少且乱，周泰先护住孙权，又使左右敢于应战；部众最后抵住了突袭。', refs=[SAVE, WOUNDS]),
        dict(section='setback', when='初督濡须时，确年未载', title='受命领兵，部将起初不服', category='统军阻力', careerRef='ruxu',
             text='本传记朱然、徐盛起初都不服从。孙权亲至濡须坞，让周泰指认战伤来历，次日赐御盖，两人才服从。', refs=[COMMAND, BANQUET, HONOR]),
    ],
    sections={'civil': {'note': '周泰先后任春谷、宜春县长，本传记他享该地征赋，没有交代任内施政。'}},
    relations=[
        dict(category='君臣', name='孙权', personId='sunquan', label='宣城救主，濡须受重用', text='周泰在宣城保护孙权，身受重伤；孙权后来以旧伤说明其战功，为他在濡须树立威信。', refs=[SAVE, WOUNDS, BANQUET, HONOR]),
        dict(category='同僚', name='蒋钦', personId='jiang-qin', label='同为孙策左右', text='两人早年一同追随孙策，从战立功。', refs=[JOIN]),
        dict(category='同僚', name='徐盛', personId='xu-sheng', label='濡须督属，始而不服', text='周泰督濡须时，徐盛是其部将之一；到孙权主持宴会、赐下御盖才服从。', refs=[COMMAND, HONOR]),
    ],
    readingNotes=[
        dict(title='十二处伤与数十处伤', text='本传记的是宣城遇袭这一日受十二创。裴注引《江表传》记孙权在濡须宴上说他为孙氏兄弟多次征战，遍体战伤；两处所指的范围不同。', refs=[WOUNDS, Q('v055-b0021-n01', '卿爲孤兄弟戰如熊虎，不惜軀命，被創數十，膚如刻畫', '《江表传》')]),
    ],
    sourceScope='以卷五十五《周泰传》为主，参看卷四十六《孙策传》、卷四十七《吴主传》和本传裴注引《江表传》。本页不声称穷尽全书所有提及周泰之处。',
)
