# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't1000',
	'name2': 't1000',
	'location': 65,
	'bgm': 111,
	'flags': 8192,
	'includes': [
		't1000',
		't1030_1',
		None,
		None,
		None,
		None,
	],
	'name3': 't1000',
	'labels': [
		{
			'pos': (-5.0, 0.0, 95.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('主题乐园方向'),
		},
		{
			'pos': (-95.0, 0.0, 20.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('宅邸方向'),
		},
		{
			'pos': (1.0, 0.0, 17.5),
			'unk': b'\x00\x00R\x00',
			'name': Translate(''),
		},
	],
	'chcp': [
		'chr/ch28400',
		'chr/ch20600',
		'chr/ch20200',
		'chr/ch20300',
		'chr/ch27800',
		'chr/ch26800',
		'chr/ch24400',
		'chr/ch27600',
		'chr/ch33300',
		'chr/ch34400',
		'chr/ch39000',
		'apl/ch50165',
		'apl/ch50169',
		'chr/ch22800',
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
	],
	'npcs': [
		{
			'name': Translate('乘务员萨尔莎'),
			'pos': (-3740, -4000, -47180),
			'angle': 180,
			'_1': b'\x81\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((0, 3)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('詹姆斯'),
			'pos': (15460, -2000, -24889),
			'angle': 180,
			'_1': b'\x81\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((0, 4)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('妮姬妲'),
			'pos': (15479, -2000, -25989),
			'angle': 0,
			'_1': b'\x81\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 5)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('男孩'),
			'pos': (9600, -4000, -47930),
			'angle': 268,
			'_1': b'\x81\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('男性'),
			'pos': (8069, -4000, -48130),
			'angle': 86,
			'_1': b'\x81\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 8)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('女性'),
			'pos': (8699, -4000, -49430),
			'angle': 45,
			'_1': b'\x81\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (-7000, -2000, -26329),
			'angle': 270,
			'_1': b'\x81\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((0, 10)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('邦德'),
			'pos': (-6340, -4000, -47330),
			'angle': 135,
			'_1': b'\x85\x01\x00\x00\x07\x00\x00\x00',
			'function': Function((0, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('克蕾优'),
			'pos': (-6869, -4000, -48279),
			'angle': 45,
			'_1': b'\x85\x01\x00\x00\x08\x00\x00\x00',
			'function': Function((0, 12)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('桑妮塔'),
			'pos': (-4769, -4000, -47900),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\t\x00\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('玛丽'),
			'pos': (-3809, -4000, -47520),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\n\x00\x00\x00',
			'function': Function((0, 14)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('彼得'),
			'pos': (20559, -5000, -56500),
			'angle': 180,
			'_1': b'\x15\x01\x00\x00\x0b\x00\xff\xff',
			'function': Function((0, 15)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('特级钓师罗伊德'),
			'pos': (18040, -5000, -56500),
			'angle': 180,
			'_1': b'\x15\x01\x00\x00\x0c\x00\xff\xff',
			'function': Function((0, 16)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('雾香'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('雷克多'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('水上巴士'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('乘客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('乘客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('乘客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('乘客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('乘客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('乘客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('乘客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('乘客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('SE控制'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (23049, -4000, -47340),
			'angle': 70,
			'_1': b'\x81\x01\x00\x00\r\x00\x00\x00',
			'function': Function((0, 28)),
			'_2': b'\xff\x00\x00\x00',
		},
	],
	'monsters': [],
	'triggers': [],
	'objects': [
		{
			'pos': (-24500, -4000, -45660),
			'range': 1200,
			'bubble_pos': (-24490, -6000, -38830),
			'_1': b'|\x00\x00',
			'function': Function((0, 17)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (10350, -3990, -46410),
			'range': 1200,
			'bubble_pos': (10350, -2500, -46410),
			'_1': b'|\x00\x00',
			'function': Function((0, 27)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-30180, -4000, -47980),
			'range': 1200,
			'bubble_pos': (-30180, -4000, -47980),
			'_1': b'|\x00\x00',
			'function': Function((0, 26)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00A\x00', Function((0, 1)), Function((0, 2))),
	'code': [None]*29,
	'anim': [],
}

data['code'][0] = [
	Insn('EXPR_VAR', 2, Expr([Insn('RAND'), Insn('CONST', 8), Insn('MOD'), Insn('SET'), Insn('END')])),
	Insn('SWITCH', [Insn('VAR', 2), Insn('END')], {
		0: [
			Insn('0xA0', Char(254), 1450, 64256),
			Insn('BREAK'),
		],
		1: [
			Insn('0xA0', Char(254), 1550, 64256),
			Insn('BREAK'),
		],
		2: [
			Insn('0xA0', Char(254), 1600, 64256),
			Insn('BREAK'),
		],
		3: [
			Insn('0xA0', Char(254), 1400, 64256),
			Insn('BREAK'),
		],
		4: [
			Insn('0xA0', Char(254), 1650, 64256),
			Insn('BREAK'),
		],
		5: [
			Insn('0xA0', Char(254), 1350, 64256),
			Insn('BREAK'),
		],
		6: [
			Insn('0xA0', Char(254), 1500, 64256),
			Insn('BREAK'),
		],
		None: [
			Insn('0xA0', Char(254), 1500, 64256),
			Insn('BREAK'),
		],
	}),
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('0xA0', Char(254), 1500, 64256),
	]),
	Insn('RETURN'),
]

data['code'][1] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 18))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 55, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(33), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1333)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1330)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1329)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1320)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1319)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('FLAG', Flag(1342)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
			Insn('OBJ_SET_FRAME', Object(255), 't1000_sky', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 't1000_sky_y', Insn('1', 1)),
			Insn('OBJ_FLAG_SET', Object(0), 4),
		]),
		(None, [
			Insn('OBJ_SET_FRAME', Object(255), 't1000_sky', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 't1000_sky_y', Insn('0', 1)),
		]),
	]),
	Insn('OBJ_SET_FRAME', Object(0), 'light', Insn('0', 1)),
	Insn('EFF_LOAD', ResId(8), 'eff\\mgm03_02.eff'),
	Insn('EFF_PLAY', (ResId(8), 8), Char(255), 0, -24490, -1, -5900, -1, 26706, -1, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('OBJ_FLAG_SET', Object(4), 4),
	Insn('OBJ_FLAG_SET', Object(5), 4),
	Insn('OBJ_FLAG_SET', Object(6), 4),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1312)), Insn('FLAG', Flag(1318)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(4), 4),
			Insn('OBJ_FLAG_UNSET', Object(5), 4),
			Insn('OBJ_FLAG_UNSET', Object(6), 4),
		]),
		(None, []),
	]),
	Insn('0x65', 2, 1),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 1))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EFF_LOAD', ResId(0), 'event\\eva00_00.eff'),
			Insn('EFF_PLAY', (ResId(0), 0), Char(255), 0, -30180, -1, -4000, -1, 17556, -1, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
			Insn('0x66', 2, 1),
		]),
		(None, []),
	]),
	Insn('SOUND_PLAY', 126, 0, 1, 80),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'前往往克洛斯贝尔市的水上巴士\n'
				'刚刚已经出发。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'下一班很快就将到达，\n'
				'需要乘坐的客人，请稍候片刻。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'水上巴士之旅让大家辛苦了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'请在米修拉姆\n'
				'度过梦幻般的时刻。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('TEXT_START', Char(254)),
	Insn('CHAR_WATCH', Char(9), Char(10), 0),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((0, 6))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'哈哈哈……\n'
				'我跟我太太说我出差去了，\n'
				'不必担心啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
			Insn('CHAR_WATCH', Char(10), Char(9), 0),
			Insn('CALL', Function((0, 6))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'那个拍卖会，\n'
				'我以前就很有兴趣了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵……能有人带我来，\n'
				'真是幸运啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('0x4B', Char(9), -1),
	Insn('0x4B', Char(10), -1),
	Insn('TEXT_TALK', Char(9), Text(
		'今晚要在议长宅邸举行宴会。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'就让我为你拍个\n'
		'美丽的饰品吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'呵呵……真是个坏人。\n'
		'明明都有妻子了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'哈哈哈……\n'
		'不是说好今晚不提这个的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(9), -1),
	Insn('0x4C', Char(10), -1),
	Insn('FLAG_SET', Flag(0)),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'刚才下船的那个大哥哥\n'
				'以超快的速度跑掉了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'他那么期待啊～\n'
				'我也要好好玩个痛快！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'今天爸爸也在……\n'
				'我要好好玩个痛快！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'好～快点前往\n'
		'主题乐园吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'任何游乐设施，爸爸今天\n'
		'都会陪你玩哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'哎呀呀，老公你真是的，\n'
		'这么爱逞强。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'呵呵，那我就不客气地\n'
		'去坐惊险刺激的游乐设施啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我打算逛完纪念庆典之后\n'
				'再来这里，\n'
				'结果就拖到傍晚了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'没办法，\n'
				'去时装店那边随便看看，\n'
				'然后就早点回去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'要是被卷入回程大潮，\n'
				'可就太糟糕了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(2)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'我来得太迟了呢，\n'
				'大概玩不到什么东西了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'去时装店那边随便看看，\n'
				'然后就早点回去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(15), Text(
		'哈哈，真愉快，\n'
		'今天全家人一起玩了个痛快呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'偶尔这样放松一下，\n'
		'感觉也不错啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(16), Text(
		'饭店都住满了……\n'
		'好遗憾……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
			Insn('TEXT_TALK', Char(17), Text(
				'爸爸和妈妈……\n'
				'以后会不会再带我来呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(17), Text(
				'因为爸爸还有工作，\n'
				'所以今天必须回去。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(17), Text(
				'……而且\n'
				'玛丽也累了，\n'
				'桑妮塔今天就先回去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(3)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(18), Text(
		'呼啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1736)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀，罗伊德团员\n'
				'也来钓鱼吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，你果然也还没从\n'
				'钓鱼大赛的热情中冷却下来啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'对了，你带着钓饵吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FADE_ON', 300, Color(0x00000000), 100),
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('SOUND_PLAY', 17, 0, 0, 100),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'获得了５个{item 391}{color 0}。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('0x5A'),
			Insn('ITEM_ADD', 391, 5),
			Insn('TEXT_TALK', Char(254), Text(
				'分给你一点好了，虽然不多。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，罗伊德团员\n'
				'也请加油哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1736)),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 8))), Insn('END')]), [
					Insn('FLAG_SET', Flag(1737)),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1737)), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 8))), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 391, 0)), Insn('CONST', 0), Insn('EQ'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 36, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 36, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀，罗伊德团员。\n'
				'莫非是\n'
				'钓饵不够了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FADE_ON', 300, Color(0x00000000), 100),
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('SOUND_PLAY', 17, 0, 0, 100),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'获得了２个{item 391}{color 0}。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('0x5A'),
			Insn('ITEM_ADD', 391, 2),
			Insn('TEXT_TALK', Char(254), Text(
				'分给你一点好了，虽然不多。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，罗伊德团员也很有热情呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1737)),
		]),
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀，水流的情况似乎\n'
				'改变了呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'很遗憾，今天\n'
				'就到此为止吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'这位罗伊德大师\n'
						'说也想到对岸来\n'
						'钓鱼呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，不愧是特级钓师，\n'
						'判断力就是不同呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'今天的钓鱼成果\n'
						'真是太棒了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'不愧是特级钓师，\n'
						'判断力真是太出色了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'唔，今天也就这样了吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'钓到了大口鲈鱼这样的大鱼，\n'
				'就算不错了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'纪念庆典结束以后，\n'
				'我就打算回利贝尔了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'在克洛斯贝尔能够\n'
				'体验到的钓鱼方式，\n'
				'可要全部尝试一次才行呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('EVENT_BEGIN', 1),
	Insn('SOUND_PLAY', 1094, 0, 255, 100),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F这里的话似乎可以钓到鱼。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-23140, -2400, -43580), 1500),
	Insn('CAM_ROTATE', 315, 36, 0, 1500),
	Insn('0x6E', 200, 1500),
	Insn('CAM_DISTANCE', 50000, 1500),
	Insn('SLEEP', 1000),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}要钓鱼吗？{color 0}{wait}'
	)),
	Insn('MENU', 0, -1, -1, 1, Text(
		'钓鱼\n'
		'放弃\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('0x6F', b'\x01'),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('0xE0', b'\x02'),
			Insn('MINIGAME', 6, 3, [
				-24500,
				-4000,
				-46830,
				0,
				-24490,
				-5900,
				-38830,
			]),
		]),
		(None, []),
	]),
	Insn('0xE0', b'\x02'),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('EVENT_BEGIN', 0),
	Insn('0xE5'),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch07400', 30),
	Insn('LOAD_CHCP', 'chr/ch07300', 31),
	Insn('LOAD_CHCP', 'chr/ch20600', 32),
	Insn('LOAD_CHCP', 'chr/ch20200', 33),
	Insn('LOAD_CHCP', 'chr/ch20300', 34),
	Insn('LOAD_CHCP', 'chr/ch21600', 35),
	Insn('LOAD_CHCP', 'chr/ch21300', 36),
	Insn('LOAD_CHCP', 'chr/ch21200', 37),
	Insn('LOAD_CHCP', 'chr/ch27700', 38),
	Insn('LOAD_CHCP', 'chr/ch23600', 39),
	Insn('CHAR_SET_POS', Char(257), (-7250, -4000, -40000), 180),
	Insn('CHAR_SET_POS', Char(258), (-7250, -4000, -40000), 180),
	Insn('CHAR_SET_POS', Char(259), (-7250, -4000, -40000), 180),
	Insn('CHAR_SET_POS', Char(260), (-7250, -4000, -40000), 180),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_CHCP', Char(22), 30),
	Insn('CHAR_SET_FRAME', Char(22), 0),
	Insn('CHAR_FLAG1_UNSET', Char(22), 128),
	Insn('CHAR_FLAG2_UNSET', Char(22), 32768),
	Insn('CHAR_SET_POS', Char(22), (-7250, -4000, -40000), 180),
	Insn('CHAR_SET_COLOR', Char(22), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_SET', Char(22), 32768),
	Insn('CHAR_SET_CHCP', Char(21), 31),
	Insn('CHAR_SET_FRAME', Char(21), 0),
	Insn('CHAR_FLAG1_UNSET', Char(21), 128),
	Insn('CHAR_FLAG2_UNSET', Char(21), 32768),
	Insn('CHAR_SET_POS', Char(21), (-7250, -4000, -40000), 180),
	Insn('CHAR_SET_COLOR', Char(21), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_SET', Char(21), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(23), 128),
	Insn('0x78', b'\x00', Char(23)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(23), (-45000, -5500, -38200), 0),
	Insn('0xD3', Char(23), 0, 90000, 0, 0),
	Insn('OBJ_FLAG_SET', Object(0), 4096),
	Insn('0x74', Object(0), 7680),
	Insn('0x71', Object(0), b'y\x00', 180, 32),
	Insn('OBJ_SET_FRAME', Object(0), 'light', Insn('0', 1)),
	Insn('OBJ_FLAG_SET', Object(4), 4),
	Insn('OBJ_FLAG_SET', Object(5), 4),
	Insn('OBJ_FLAG_SET', Object(6), 4),
	Insn('CHAR_SET_CHCP', Char(24), 32),
	Insn('CHAR_SET_CHCP', Char(25), 33),
	Insn('CHAR_SET_CHCP', Char(26), 34),
	Insn('CHAR_SET_CHCP', Char(27), 35),
	Insn('CHAR_SET_CHCP', Char(28), 36),
	Insn('CHAR_SET_CHCP', Char(29), 37),
	Insn('CHAR_SET_CHCP', Char(30), 38),
	Insn('CHAR_SET_CHCP', Char(31), 39),
	Insn('CHAR_SET_FRAME', Char(24), 0),
	Insn('CHAR_SET_FRAME', Char(25), 0),
	Insn('CHAR_SET_FRAME', Char(26), 0),
	Insn('CHAR_SET_FRAME', Char(27), 0),
	Insn('CHAR_SET_FRAME', Char(28), 0),
	Insn('CHAR_SET_FRAME', Char(29), 0),
	Insn('CHAR_SET_FRAME', Char(30), 0),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_FLAG1_UNSET', Char(24), 128),
	Insn('CHAR_FLAG2_UNSET', Char(24), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(25), 128),
	Insn('CHAR_FLAG2_UNSET', Char(25), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(26), 128),
	Insn('CHAR_FLAG2_UNSET', Char(26), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(27), 128),
	Insn('CHAR_FLAG2_UNSET', Char(27), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(28), 128),
	Insn('CHAR_FLAG2_UNSET', Char(28), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(29), 128),
	Insn('CHAR_FLAG2_UNSET', Char(29), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_COLOR', Char(24), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(25), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(26), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(27), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(28), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(29), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(30), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(31), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(24), (-7250, -4000, -40000), 180),
	Insn('CHAR_SET_POS', Char(25), (-7250, -4000, -40000), 180),
	Insn('CHAR_SET_POS', Char(26), (-7250, -4000, -40000), 180),
	Insn('CHAR_SET_POS', Char(27), (-7250, -4000, -40000), 180),
	Insn('CHAR_SET_POS', Char(28), (-7250, -4000, -40000), 180),
	Insn('CHAR_SET_POS', Char(29), (-7250, -4000, -40000), 180),
	Insn('CHAR_SET_POS', Char(30), (-7250, -4000, -40000), 180),
	Insn('CHAR_SET_POS', Char(31), (-7250, -4000, -40000), 180),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('CHAR_FLAG1_SET', Char(25), 32768),
	Insn('CHAR_FLAG1_SET', Char(26), 32768),
	Insn('CHAR_FLAG1_SET', Char(27), 32768),
	Insn('CHAR_FLAG1_SET', Char(28), 32768),
	Insn('CHAR_FLAG1_SET', Char(29), 32768),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('CHAR_FLAG1_SET', Char(31), 32768),
	Insn('0xCB', b'T\x01\xc8\x00', 'c_plac20', b'\x00\xb8\x0b'),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('CAM_OFFSET', (20240, -2400, -36530), 0),
	Insn('CAM_ROTATE', 334, 19, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 64730, 0),
	Insn('CAM_OFFSET', (-1240, -2400, -36530), 15000),
	Insn('FORK_FUNC', Char(32), 1, Function((0, 25))),
	Insn('FORK', 23, 1, [
		Insn('0x98', Char(254), (40000, 0, 0), 3000, 0),
	]),
	Insn('FORK_AWAIT', Char(23), 1),
	Insn('0x71', Object(0), b'[\x00', 120, 0),
	Insn('SOUND_PLAY', 478, 0, 0, 100),
	Insn('0x79', b'\x00\x00'),
	Insn('0x71', Object(0), b'-\x01', 360, 32),
	Insn('0x6F', b'\x01'),
	Insn('FORK_QUIT', Char(32), 1),
	Insn('0x0D'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-5240, -1300, -48610), 0),
	Insn('CAM_ROTATE', 327, 21, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 31570, 0),
	Insn('0x0D'),
	Insn('0x71', Object(0), b'\x01\x00', 30, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x00\x00'),
	Insn('0x71', Object(0), b'\xf1\x00', 300, 32),
	Insn('FORK_FUNC', Char(24), 3, Function((0, 19))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(25), 3, Function((0, 19))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(26), 3, Function((0, 19))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(27), 3, Function((0, 19))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(22), 3, Function((0, 19))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(28), 3, Function((0, 19))),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(22), 0, 2000, (8, 9, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('FORK_FUNC', Char(29), 3, Function((0, 19))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(30), 3, Function((0, 19))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(21), 3, Function((0, 19))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(31), 3, Function((0, 19))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 21))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 22))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 23))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 24))),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-530, -1300, -54200), 0),
	Insn('CAM_ROTATE', 326, 12, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 13040, 0),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('FORK_QUIT', Char(24), 3),
	Insn('FORK_QUIT', Char(25), 3),
	Insn('FORK_QUIT', Char(26), 3),
	Insn('FORK_QUIT', Char(27), 3),
	Insn('FORK_QUIT', Char(28), 3),
	Insn('FORK_QUIT', Char(29), 3),
	Insn('FORK_QUIT', Char(30), 3),
	Insn('FORK_QUIT', Char(31), 3),
	Insn('FORK_QUIT', Char(22), 3),
	Insn('FORK_QUIT', Char(22), 0),
	Insn('FORK_QUIT', Char(21), 3),
	Insn('0xE6'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500318V#0008F#5P──这里就是米修拉姆啊。{wait}'
		'{page}'
		'#13500319V#0006F该怎么说呢，真是比想像中\n'
		'更加奢华的地方……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500320V#0203F#5P这里原本是个高级游憩区，\n'
		'由ＩＢＣ着手开发为度假村……{wait}'
		'{page}'
		'#13500321V#0200F饭店和主题乐园好像\n'
		'也是在两年前才刚建成的呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500322V#0104F#5P嗯，从那以后，这里就成为了\n'
		'与彩虹剧团齐名的观光胜地。{wait}'
		'{page}'
		'#13500323V#0100F正面是饭店，\n'
		'一楼是商店街。{wait}'
		'{page}'
		'#13500324V其中有餐厅、时装店、\n'
		'珠宝店等等。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500325V#0306F#5P但价格全都高得离谱，\n'
		'平民很难承受就是了～{wait}'
		'{page}'
		'#13500326V#0300F我以前约会的时候，\n'
		'也只去过主题乐园\n'
		'和餐厅……{wait}'
		'{page}'
		'#13500327V那么，接下来该怎么办？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(260), 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500328V#0003F#12P这个嘛……{wait}'
		'{page}'
		'#13500329V#0001F先确认一下\n'
		'拍卖会场周边的情况吧。{wait}'
		'{page}'
		'#13500330V会场就在哈尔特曼议长宅邸，没错吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500331V#0100F#6P嗯……\n'
		'从左边穿过商店街，可以看到一片\n'
		'别墅林立的游憩区区域。{wait}'
		'{page}'
		'#13500332V议长宅邸应该就在最里面。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500333V#0004F#12P明白了。{wait}'
		'{page}'
		'#13500334V#0000F除此之外……\n'
		'能去的地方也都去看看吧。{wait}'
		'{page}'
		'#13500335V说不定还会遇到\n'
		'像雷克多那样的\n'
		'『拍卖会』宾客呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500336V#0202F#5P……是啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500337V#0106F#6P说起来，那个人……{wait}'
		'{page}'
		'#13500338V#0101F言行举止相当奇怪，\n'
		'真的是帝国贵族吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500339V#0303F#5P……谁知道。{wait}'
		'{page}'
		'#13500340V#0301F说不定和他之前自称为铁血宰相的代理人一样，\n'
		'只是在信口开河而已……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500341V#0006F#12P只是，似乎连这种奇怪的人\n'
		'也都被邀请为来宾了。{wait}'
		'{page}'
		'#13500342V#0013F『黑之拍卖会#10RSchwarz Auction#』──\n'
		'果然不能以常理度之啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('CAM_DISTANCE', 13290, 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_CHCP', Char(24), 0),
	Insn('CHAR_SET_CHCP', Char(25), 0),
	Insn('CHAR_SET_CHCP', Char(26), 0),
	Insn('CHAR_SET_CHCP', Char(27), 0),
	Insn('CHAR_SET_CHCP', Char(28), 0),
	Insn('CHAR_SET_CHCP', Char(29), 0),
	Insn('CHAR_SET_CHCP', Char(30), 0),
	Insn('CHAR_SET_CHCP', Char(31), 0),
	Insn('CHAR_SET_FRAME', Char(24), 0),
	Insn('CHAR_SET_FRAME', Char(25), 0),
	Insn('CHAR_SET_FRAME', Char(26), 0),
	Insn('CHAR_SET_FRAME', Char(27), 0),
	Insn('CHAR_SET_FRAME', Char(28), 0),
	Insn('CHAR_SET_FRAME', Char(29), 0),
	Insn('CHAR_SET_FRAME', Char(30), 0),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_FLAG1_SET', Char(24), 128),
	Insn('CHAR_FLAG2_SET', Char(24), 32768),
	Insn('CHAR_FLAG1_SET', Char(25), 128),
	Insn('CHAR_FLAG2_SET', Char(25), 32768),
	Insn('CHAR_FLAG1_SET', Char(26), 128),
	Insn('CHAR_FLAG2_SET', Char(26), 32768),
	Insn('CHAR_FLAG1_SET', Char(27), 128),
	Insn('CHAR_FLAG2_SET', Char(27), 32768),
	Insn('CHAR_FLAG1_SET', Char(28), 128),
	Insn('CHAR_FLAG2_SET', Char(28), 32768),
	Insn('CHAR_FLAG1_SET', Char(29), 128),
	Insn('CHAR_FLAG2_SET', Char(29), 32768),
	Insn('CHAR_FLAG1_SET', Char(30), 128),
	Insn('CHAR_FLAG2_SET', Char(30), 32768),
	Insn('CHAR_FLAG1_SET', Char(31), 128),
	Insn('CHAR_FLAG2_SET', Char(31), 32768),
	Insn('CHAR_FLAG1_SET', Char(22), 128),
	Insn('CHAR_FLAG2_SET', Char(22), 32768),
	Insn('CHAR_FLAG1_SET', Char(21), 128),
	Insn('CHAR_FLAG2_SET', Char(21), 32768),
	Insn('0x49'),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0xD5', 33),
	Insn('0xD5', 34),
	Insn('0xD5', 35),
	Insn('0xD5', 36),
	Insn('0xD5', 37),
	Insn('0xD5', 38),
	Insn('0xD5', 39),
	Insn('OBJ_FLAG_UNSET', Object(4), 4),
	Insn('OBJ_FLAG_UNSET', Object(5), 4),
	Insn('OBJ_FLAG_UNSET', Object(6), 4),
	Insn('CHAR_SET_POS', Char(0), (-2000, -4000, -50200), 90),
	Insn('FLAG_SET', Flag(1312)),
	Insn('QUEST', 71, Insn('TASK_SET', 1)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 24, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 24, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 24, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 24, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 24, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 26, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 26, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 28, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 28, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 28, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 28, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 28, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 30, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 30, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 33, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 33, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 34, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 34, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 34, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 34, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 34, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 35, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 35, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-7250, -4000, -50000), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (7250, -4000, -50000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('EMOTE', Char(254), 0, 2000, (8, 9, 250, 2)),
		Insn('SOUND_PLAY', 27, 0, 0, 100),
		Insn('SLEEP', 3000),
	]),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-7250, -4000, -50000), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-2940, -4000, -50580), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 90, 300),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-7250, -4000, -50000), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-4019, -4000, -51400), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 90, 500),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-7250, -4000, -50000), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-4680, -4000, -49050), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 90, 500),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-7250, -4000, -50000), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-5640, -4000, -50180), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 90, 500),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('SLEEP', 1000),
	Insn('SOUND_PLAY', 475, 0, 0, 100),
	Insn('SLEEP', 1500),
	Insn('SOUND_PLAY', 477, 0, 0, 100),
	Insn('SLEEP', 4000),
	Insn('SOUND_PLAY', 476, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('SOUND_PLAY', 477, 0, 0, 100),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-28230, -2400, -50050), 0),
	Insn('CAM_ROTATE', 315, 20, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 34310, 0),
	Insn('CHAR_SET_POS', Char(257), (-28000, -4000, -48730), 270),
	Insn('CHAR_SET_POS', Char(258), (-28000, -4000, -47510), 225),
	Insn('CHAR_SET_POS', Char(259), (-26240, -4000, -49940), 270),
	Insn('CHAR_SET_POS', Char(260), (-26310, -4000, -48550), 270),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(337), (-25030, -4000, -49530), 270),
		]),
		(None, []),
	]),
	Insn('EFF_STOP', (ResId(0), 2)),
	Insn('0x0D'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'获得了{item 844}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 844, 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0005F咦，这个戒指……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11P#0105F说不定正是托马先生\n'
		'之前说的订婚戒指呢。{wait}'
		'{page}'
		'#0100F稍后拿到饭店的房间里\n'
		'给他看看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('QUEST', 36, Insn('TASK_SET', 1)),
	Insn('0x65', 2, 1),
	Insn('CHAR_SET_POS', Char(0), (-28000, -4000, -48730), 270),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}前往『克洛斯贝尔市』的水上巴士丄时刻表\n'
		'\n'
		'※期待着您的\n'
		'下次光临！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][28] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 55, Insn('TASK_GET', 2))), Insn('END')]), [
			Insn('CALL', Function((1, 6))),
		]),
		(None, [
			Insn('CALL', Function((1, 5))),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]
