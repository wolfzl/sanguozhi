"""乐进：以卷十七《乐进传》为主的 v3 C 级人物卡。"""
from profile_v3 import Q

ORIGIN = Q('v017-b0007', '樂進字文謙，陽平衞國人也。')
RECRUIT = Q('v017-b0007', '遣還本郡募兵，得千餘人，還爲軍假司馬、陷陳都尉。')
VANGUARD = Q('v017-b0007', '從擊呂布於濮陽，張超於雍丘，橋曨於苦，皆先登有功，封廣昌亭侯。')
XIAPI = Q('v017-b0007', '圍呂布於下邳，破別將')
GUANDU = Q('v017-b0007', '從擊袁紹於官渡，力戰，斬紹將淳于瓊。')
NANPI = Q('v017-b0007', '從擊袁譚於南皮，先登，入譚東門。')
HUGUAN = Q('v017-b0008', '幹等還守壺關，連戰斬首。幹堅守未下，會太祖自征之，乃拔。')
XIANGYANG = Q('v017-b0008', '後從平荆州，留屯襄陽，擊關羽、蘇非等，皆走之，南郡諸郡山谷蠻夷詣進降。')
HEFEI = Q('v017-b0004', '太祖旣征孫權還，使遼與樂進、李典等將七千餘人屯合肥。')
ORDER = Q('v017-b0004', '若孫權至者，張李將軍出戰；樂將軍守護軍，勿得與戰。')
OFFICE = Q('v017-b0008', '進遷右將軍。')
DEATH = Q('v017-b0008', '建安二十三年薨，諡曰威侯。子綝嗣。')

PROFILE = dict(
    id='yue-jin', tier='C', reading=['017'],
    new=dict(name='乐进', courtesy='文谦', faction='曹魏', period='汉末—218年',
             aliases=[], tags=['先登', '官渡', '合肥']),
    eventRoles=[('yanzhou-struggle', '濮阳先登立功'), ('xiapi', '围下邳，击破吕布别将'),
                ('guandu', '从曹操力战'), ('yuan-succession', '南皮先登攻入东门'),
                ('hefei', '城中守备')],
    lead='乐进从曹操帐下吏做起，在濮阳、南皮等战事中以先登闻名。215年孙权围合肥，曹操留下的命令让张辽、李典出战，乐进留守城内。乐进官至右将军，218年去世，谥威侯。',
    role='以先登战功著称的曹将',

    facts=[
        dict(key='lifespan', label='生卒年', value='生年未详—218年',
             text='本传没记乐进生年，明记建安二十三年（218）去世。',
             refs=[DEATH]),
        dict(key='hometown', label='籍贯', value='阳平郡卫国县',
             text='本传记乐进字文谦，阳平卫国人。', refs=[ORIGIN]),
        dict(key='identity', label='主要身份', value='曹操早期帐下吏、统兵将领',
             text='曹操因其有胆气而收为帐下吏，令他回本郡募兵，随后由军假司马、陷陈都尉领兵作战。',
             refs=[Q('v017-b0007', '容貌短小，以膽烈從太祖，爲帳下吏。'), RECRUIT]),
        dict(key='office', label='最高官职', value='右将军',
             text='初任军假司马、陷陈都尉，后为折冲将军、假节，最终升右将军。',
             refs=[RECRUIT, Q('v017-b0007', '進，折衝；遼，蕩寇將軍。'), Q('v017-b0008', '後從征孫權，假進節。'), OFFICE]),
        dict(key='title', label='最高爵位', value='广昌亭侯',
             text='本传记乐进因数次先登立功封广昌亭侯；后增封邑，并分五百户封一子为列侯。',
             refs=[VANGUARD, Q('v017-b0008', '增邑五百，並前凡千二百戸。以進數有功，分五百戸，封一子列侯')]),
        dict(key='posthumous', label='身后称号', value='威侯',
             text='218年去世，谥威侯，子乐綝嗣爵。', refs=[DEATH]),
        dict(key='deeds', label='代表事迹', items=['濮阳先登', '南皮破门', '合肥守城'],
             text='攻濮阳时先登立功；攻南皮时首先进入袁谭东门；合肥之战时奉曹操命留守城内。',
             refs=[VANGUARD, NANPI, ORDER]),
    ],

    intro=[
        dict(title='从帐下吏到军中先登',
             text='乐进字文谦，阳平卫国人。陈寿说他身材短小，却以胆气追随曹操，最初只是帐下吏。他受命回本郡募得千余人，归来担任军假司马、陷陈都尉。在濮阳攻吕布、雍丘攻张超等战斗中，乐进屡次先登立功，封广昌亭侯。曹操围下邳时，他又击破吕布别将，后来从征袁绍，在官渡之战中力战。袁氏兄弟相争以后，乐进随曹军进攻南皮，率先冲入袁谭的东门。曹操上表称许他与于禁、张辽的勇力、谋略和军纪，乐进因此升为折冲将军。',
             refs=[ORIGIN, Q('v017-b0007', '容貌短小，以膽烈從太祖，爲帳下吏。'), RECRUIT, VANGUARD, XIAPI, GUANDU, NANPI,
                   Q('v017-b0007', '太祖表漢帝，稱進及于禁、張遼曰：「武力旣弘，計略周備'), Q('v017-b0007', '進，折衝；遼，蕩寇將軍。')],
             eventLinks=[dict(label='濮阳攻吕布', eventId='yanzhou-struggle'), dict(label='围下邳', eventId='xiapi'),
                         dict(label='官渡之战', eventId='guandu'), dict(label='进攻南皮', eventId='yuan-succession')]),
        dict(title='屯襄阳与留守合肥',
             text='曹操取得荆州后，乐进留屯襄阳，本传记他击退关羽、苏非等人。后来他跟随曹操攻孙权，获授军节，又与张辽、李典等同屯合肥。215年孙权围合肥，守军拆看曹操留下的密令，张辽、李典负责出战，乐进奉命留在城内守备。吴军围攻十余日未能攻下，随后撤退。乐进以屡次立功，分封一子为列侯，自己升右将军，218年去世，谥威侯。',
             refs=[XIANGYANG, Q('v017-b0008', '後從征孫權，假進節。'), HEFEI, ORDER,
                   Q('v017-b0004', '權守合肥十餘日，城不可拔，乃引退。'),
                   Q('v017-b0008', '以進數有功，分五百戸，封一子列侯'), OFFICE, DEATH],
             eventLinks=[dict(label='孙权围合肥', eventId='hefei')]),
    ],

    careers=[
        dict(id='puyang', when='194—195年', title='濮阳、雍丘先登立功', office='广昌亭侯', eventIds=['yanzhou-struggle'],
             text='早年由募兵获授军职。随曹操在濮阳攻吕布、在雍丘攻张超，均有先登之功；本传合叙数役后记封广昌亭侯。',
             refs=[RECRUIT, VANGUARD]),
        dict(id='xiapi', when='198年', title='围下邳，击破吕布别将', office='—', eventIds=['xiapi'],
             text='跟随曹操围下邳，在吕布覆灭的战事中攻破其别将所部。', refs=[XIAPI, Q('v007-b0014', '建安三年，布復叛爲術')]),
        dict(id='guandu', when='200年', title='从曹操在官渡作战', office='—', eventIds=['guandu'],
             text='随曹操出战。本传记乐进力战并斩淳于琼，《武帝纪》则对所斩诸将作集体归功。',
             refs=[GUANDU, Q('v001-b0051', '士卒皆殊死戰，大破瓊等，皆斬之。')]),
        dict(id='hebei', when='205—206年', title='南皮先登，进击高干', office='折冲将军（206）', eventIds=['yuan-succession'],
             text='攻袁谭于南皮，率先攻入东门。其后攻高干，高干退守壶关，直至曹操亲征方告攻克；206年曹操上表称其功，乐进获授折冲将军。',
             refs=[NANPI, HUGUAN, Q('v001-b0067', '十一年春正月，公征幹。'), Q('v017-b0007', '建安十一年，太祖表漢帝'),
                   Q('v017-b0007', '進，折衝；遼，蕩寇將軍。')]),
        dict(id='xiangyang', when='曹操平荆州后，确年未载', title='留屯襄阳，击退关羽等', office='—',
             text='随曹操平荆州后驻襄阳，先后与关羽、苏非以及刘备所置县长等交战。',
             refs=[XIANGYANG, Q('v017-b0008', '又討劉備臨沮長杜普、旌陽長梁大，皆大破之。')]),
        dict(id='hefei', when='215年；218年卒', title='奉密令守合肥，后官至右将军', office='后迁右将军', eventIds=['hefei'],
             text='与张辽、李典等屯合肥。围城时按曹操密令留守，张辽、李典出战，孙权围城不克而退；乐进后来升右将军，218年去世。',
             refs=[HEFEI, ORDER, Q('v017-b0004', '權守合肥十餘日，城不可拔，乃引退。'), OFFICE, DEATH]),
    ],

    records=[
        dict(section='military', when='205年', title='南皮率先攻入袁谭东门', category='先登攻城', careerRef='hebei', eventIds=['yuan-succession'],
             text='《乐进传》把攻入东门记为他的战功，具体展示了传中反复出现的“先登”。', refs=[NANPI]),
        dict(section='military', when='215年', title='合肥战事奉令守城', category='守备分工', careerRef='hefei', eventIds=['hefei'],
             text='曹操的密令明确区分守备与出击，把留守任务交给乐进。吴军最终未克城，不能把张辽率军突击的功劳移写为乐进出战。',
             refs=[ORDER, Q('v017-b0004', '權守合肥十餘日，城不可拔，乃引退。')]),
        dict(section='setback', when='205—206年', title='初攻壶关未克', category='遇阻待援', careerRef='hebei',
             text='乐进、李典先攻高干，高干退入壶关仍能坚守。乐进虽在交锋中得胜，最终克城还须等曹操亲征；史书没有把僵持归咎于乐进。',
             refs=[Q('v001-b0067', '遣樂進、李典擊之，幹還守壺關城。'), HUGUAN]),
    ],
    sections={
        'civil': {'note': '本传记乐进募兵、统军与守城，曹操也称许其抚众守令；未见他主持郡县民政的具体记载。'},
    },

    assessment=[
        dict(title='陈寿：以骁果显名',
             text='陈寿将乐进列为曹操麾下领先的五位良将，称他以勇猛果敢闻名，同时指出传中记下的事迹未尽呈现实际声名，可能有所遗漏。',
             refs=[Q('v017-b0028', '樂進以驍果顯名，而鑑其行事，未副所聞。或注記有遺漏，未如張遼、徐晃之備詳也。')]),
    ],

    relations=[
        dict(category='君臣', name='曹操', personId='caocao', label='遣其募兵，上表论功',
             text='乐进以胆气从曹操，受命回乡募兵；后来曹操向汉帝上表，与于禁、张辽一起称许其战功和军纪。',
             refs=[RECRUIT, Q('v017-b0007', '太祖表漢帝，稱進及于禁、張遼曰：「武力旣弘，計略周備')]),
        dict(category='同僚', name='张辽', personId='zhang-liao', label='合肥分别出战守备',
             text='二人同屯合肥。孙权来攻时，曹操命张辽、李典出战，由乐进留城守备。', refs=[HEFEI, ORDER]),
        dict(category='同僚', name='于禁', personId='yu-jin', label='沿黄河合击袁军',
             text='于禁守延津后，与乐进等率部沿黄河进攻袁绍的别营。', refs=[Q('v017-b0011', '復與樂進等將步騎五千，擊紹別營')]),
    ],

    readingNotes=[
        dict(title='官渡斩淳于琼的两种叙述焦点',
             text='《乐进传》把斩淳于琼写入乐进的战绩；《武帝纪》把破乌巢、斩淳于琼等写成曹操统率部队的集体战果，没逐一记下动手者。两处记法可以并读。',
             refs=[GUANDU, Q('v001-b0051', '士卒皆殊死戰，大破瓊等，皆斬之。')]),
    ],
    glossary=[('先登', '攻城或攻营时率先登上城垣、突破防线。')],
    sourceScope='以卷十七《乐进传》为主，参看同卷《张辽传》《于禁传》、卷一《武帝纪》与卷七《吕布传》。本页不声称穷尽全书所有提及乐进之处。',
)
