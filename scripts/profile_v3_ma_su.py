"""马谡：从深受器重到街亭失守。"""
from profile_v3 import Q

FAMILY = Q('v039-b0009', '馬良字季常，襄陽宜城人也。兄弟五人，並有才名')
ORIGIN = Q('v039-b0011', '良弟謖，字幼常，以荊州從事隨先主入蜀，除綿竹成都令、越雋太守。')
ABILITY = Q('v039-b0011', '才器過人，好論軍計，丞相諸葛亮深加器異。')
WARNING = Q('v039-b0011', '馬謖言過其實，不可大用，君其察之！')
ADVICE = Q('v039-b0011-n01', '夫用兵之道，攻心為上，攻城為下，心戰為上，兵戰為下，原公服其心而已。', '《襄阳记》')
APPOINT = Q('v039-b0011', '而亮違眾拔謖，統大眾在前，與魏將張郃戰於街亭')
DEFEAT = Q('v035-b0012', '謖違亮節度，舉動失宜，大為張郃所破。')
ON_HILL = Q('v043-b0018', '謖捨水上山，舉措煩擾，平連規諫謖，謖不能用，大敗於街亭。')
DEATH = Q('v039-b0011', '謖下獄物故，亮為之流涕。良死時年三十六，謖年三十九。')
EXECUTION = Q('v035-b0012', '戮謖以謝眾。')

PROFILE = dict(
    id='ma-su', tier='C', reading=['039', '035'],
    new=dict(name='马谡', courtesy='幼常', faction='蜀汉', period='汉末—228年', aliases=['马幼常'], tags=['街亭', '第一次北伐', '参军']),
    eventRoles=[('enter-shu', '以荆州从事随刘备入蜀'), ('first-northern-expedition', '督前军，街亭败于张郃')],
    role='诸葛亮帐下参军',
    lead='马谡随刘备入蜀，曾任县令、太守，因喜论军计为诸葛亮所重。228年被拔为先头统将，在街亭违令败于张郃，迫使诸葛亮退军；本传记他下狱而死。',
    facts=[
        dict(key='lifespan', label='生卒年', value='生年未详—228年', text='马谡死于建兴六年街亭败后，本传载终年三十九，未记其出生年。', refs=[DEATH, Q('v039-b0011', '建興六年 ，亮出軍向祁山')]),
        dict(key='hometown', label='籍贯', value='襄阳郡宜城县', text='《马良传》记马良籍贯襄阳宜城，并于卷内附记其弟马谡。', refs=[FAMILY, ORIGIN]),
        dict(key='identity', label='主要身份', value='诸葛亮参军，曾督前军', text='善谈军计，受诸葛亮重用；北伐时督军在前，非本传所记的常任将军。', refs=[ABILITY, Q('v039-b0011', '以謖為參軍'), APPOINT]),
        dict(key='office', label='最高官职', value='越巂太守；后为丞相参军', text='曾任绵竹、成都县令和越巂太守，后来受诸葛亮任用为参军。', refs=[ORIGIN, Q('v039-b0011', '以謖為參軍')]),
        dict(key='posthumous', label='身后称号', value='本书未载', text='本书记下狱后身亡及诸葛亮流泪，未记谥号。', refs=[DEATH]),
        dict(key='deeds', label='代表事迹', items=['随主入蜀', '献攻心策', '街亭失守'], text='先随刘备入蜀；裴注引书写他献攻心之策；正文记其街亭战败。', refs=[ORIGIN, ADVICE, DEFEAT]),
    ],
    intro=[
        dict(title='刘备与诸葛亮的不同判断',
             text='马谡是马良之弟，以荆州从事随刘备入蜀，历任绵竹、成都县令及越巂太守。他好议军计，诸葛亮很器重他。刘备临终却告诫诸葛亮，马谡的话常超出实际，不可把大任交给他。诸葛亮没有因此弃用马谡，任他为参军，还时常与他从白天谈到深夜。裴注引《襄阳记》说，诸葛亮南征时马谡送行数十里，考虑到蜀汉还要北伐，很难长期依靠重兵压服南中，主张使当地人心悦服；引书记诸葛亮采纳了这一建议。',
             refs=[ORIGIN, ABILITY, WARNING, Q('v039-b0011', '亮猶謂不然，以謖為參軍，每引見談論，自晝達夜。'), Q('v039-b0011-n01', '建興三年，亮征南中，謖送之數十里。', '《襄阳记》'), ADVICE, Q('v039-b0011-n01', '亮納其策，赦孟獲以服南方。', '《襄阳记》')],
             eventLinks=[dict(label='随刘备入蜀', eventId='enter-shu')]),
        dict(title='街亭失守与问责',
             text='228年诸葛亮率军向祁山，众人原以为宜由魏延或吴壹等宿将担任先头，诸葛亮却选了马谡。王平本传记，马谡舍水上山，王平接连劝谏而无效。张郃击破马谡所部后，士卒离散，诸葛亮因失去继续进军的依托而撤回汉中。《马良传》附记马谡下狱身亡，诸葛亮为他流涕；《诸葛亮传》记处置马谡以向众人交代，并载诸葛亮上疏自责用人失当。',
             refs=[Q('v039-b0011', '時有宿將魏延、吳壹等，論者皆言以為宜令為先鋒'), APPOINT, ON_HILL, Q('v039-b0011', '為郃所破，士卒離散。亮進無所據，退軍還漢中。'), DEATH, EXECUTION, Q('v035-b0012', '咎皆在臣授任無方。')],
             eventLinks=[dict(label='张郃击破马谡所部', eventId='first-northern-expedition')]),
    ],
    careers=[
        dict(id='enter-shu', when='211—214年', title='随刘备入蜀', office='荆州从事，后任县令、太守', text='自荆州随刘备入蜀，后来历任绵竹令、成都令与越巂太守。', refs=[ORIGIN], eventIds=['enter-shu']),
        dict(id='staff', when='刘备去世后，确年未载', title='受诸葛亮任为参军', office='丞相参军', text='刘备临终曾告诫诸葛亮谨慎用他；诸葛亮仍任他为参军，常召见论军。', refs=[WARNING, Q('v039-b0011', '以謖為參軍，每引見談論，自晝達夜。')]),
        dict(id='nanzhong', when='225年（裴注引书记载）', title='南征前进言攻心', office='—', text='据裴注引《襄阳记》，马谡送诸葛亮南征，建议以服人心来减轻日后的反复动兵。', refs=[Q('v039-b0011-n01', '建興三年，亮征南中，謖送之數十里。', '《襄阳记》'), ADVICE]),
        dict(id='jieting', when='228年', title='督军在前，街亭大败', office='督前军', text='他舍水上山，没有采纳王平的劝告，战败后部队离散，诸葛亮退回汉中。', refs=[APPOINT, ON_HILL, Q('v039-b0011', '為郃所破，士卒離散。亮進無所據，退軍還漢中。')], eventIds=['first-northern-expedition']),
        dict(id='death', when='228年', title='败后下狱而死', office='—', text='卷三十九写他下狱物故；《诸葛亮传》则用“戮谡”。', refs=[DEATH, EXECUTION]),
    ],
    records=[
        dict(section='military', when='225年（裴注引书记载）', title='论南中宜先服其心', category='用兵建言', careerRef='nanzhong', text='《襄阳记》把这番建议和将来用兵关中相联系：只攻破一时，不能免除后方再叛的风险。', refs=[Q('v039-b0011-n01', '彼知官勢內虛，其叛亦速。', '《襄阳记》'), ADVICE]),
        dict(section='setback', when='228年', title='街亭违令败军', category='指挥失当', careerRef='jieting', eventIds=['first-northern-expedition'], text='在明知王平反对的情况下坚持舍水上山，所部溃散；诸葛亮在自劾中也承担授任失当的责任。', refs=[ON_HILL, DEFEAT, Q('v035-b0012', '咎皆在臣授任無方。')]),
    ],
    sections={'civil': {'note': '马谡担任过县令与太守，附传仅列职名，未记这些任上的民政措施。'}},
    relations=[
        dict(category='亲族', name='马良', label='兄长，本书附传于此', text='马谡是马良之弟，两人的事迹同见《马良传》。', refs=[FAMILY, ORIGIN]),
        dict(category='同僚', name='诸葛亮', personId='zhuge-liang', label='赏识并授以前军', text='诸葛亮选马谡做参军，又越过宿将托付前军，战败后在上疏中归咎于自己授任无方。', refs=[ABILITY, APPOINT, Q('v035-b0012', '咎皆在臣授任無方。')]),
        dict(category='同僚', name='王平', personId='wang-ping', label='街亭进谏而未被采纳', text='王平曾多次劝谏，马谡不纳。王平在失利后独立收兵而归。', refs=[ON_HILL, Q('v043-b0018', '於是平徐徐收合諸營遺迸，率將士而還。')]),
        dict(category='敌对', name='张郃', personId='zhang-he', label='交战于街亭', text='马谡在街亭被张郃击败，蜀军前进受阻。', refs=[APPOINT, DEFEAT]),
    ],
    readingNotes=[
        dict(title='“戮谡”与“下狱物故”', text='《诸葛亮传》用“戮谡”，《马良传》附传写“下狱物故”。《向朗传》还说马谡曾逃亡，向朗因知情不报而被免官。书中未交代这些记载之间的完整经过。', refs=[EXECUTION, DEATH, Q('v041-b0009', '謖逃亡，朗知情不舉，亮恨之，免官還成都。')]),
        dict(title='军法与惜才之争见于裴注', text='裴注引《襄阳记》让蒋琬与诸葛亮分别谈惜才、明法，又附习凿齿的批评；这些议论与陈寿正文对街亭战况的叙述应分开读。', refs=[Q('v039-b0011-n02', '天下未定而戮智計之士，豈不惜乎！', '《襄阳记》'), Q('v039-b0011-n02', '若復廢法，何用討賊邪！', '《襄阳记》'), Q('v039-b0011-n02', '明法勝才，不師三敗之道，將以成業，不亦難乎！', '习凿齿曰')]),
    ],
    sourceScope='本书无独立《马谡传》，生平附见卷三十九《马良传》，并参卷三十五《诸葛亮传》、卷四十一《向朗传》及卷四十三《王平传》；裴注另作区分。本页不声称穷尽全书所有提及马谡之处。',
)
