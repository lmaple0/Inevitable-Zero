# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't1520',
	'name2': 't1520',
	'location': 78,
	'bgm': 123,
	'flags': 8192,
	'includes': [
		't1520',
		None,
		't1500_1',
		None,
		None,
		None,
	],
	'name3': 't1520',
	'labels': [],
	'chcp': [
		'apl/ch50146',
		'chr/ch25600',
		'chr/ch32800',
		'chr/ch29400',
		'chr/ch29500',
		'chr/ch29800',
		'chr/ch29300',
		'chr/ch05300',
		'chr/ch32900',
	],
	'npcs': [
		{
			'name': Translate('亚苏拉主任'),
			'pos': (92529, 400, 49430),
			'angle': 315,
			'_1': b'\xd5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((0, 8)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('玛洛妮'),
			'pos': (-5199, 0, 17700),
			'angle': 90,
			'_1': b'\x05\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('实习医生夏鲁鲁'),
			'pos': (-47439, 0, 55720),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 10)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('实习医生利顿'),
			'pos': (3630, 0, 54689),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('实习医生古恩'),
			'pos': (202830, 0, 340),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((0, 12)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('护理师梅菲尔'),
			'pos': (204669, 0, 53000),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('诊断医生贝尔达因'),
			'pos': (-98839, 0, 53500),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((0, 14)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('亚苏拉主任'),
			'pos': (94459, 0, 52029),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x08\x00\x00\x00',
			'function': Function((0, 8)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('赛西儿'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x07\x00\x00\x00',
			'function': Function((0, 16)),
			'_2': b'\xff\x00\x00\x00',
		},
	],
	'monsters': [],
	'triggers': [],
	'objects': [
		{
			'pos': (155770, 0, 53330),
			'range': 1500,
			'bubble_pos': (155770, 1500, 53330),
			'_1': b'|\x00\x00',
			'function': Function((0, 19)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00N\x00', Function((0, 6)), Function((0, 7))),
	'code': [None]*20,
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
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('0x95', Char(254), (-310, 0, 17700), 2000, 0),
		Insn('0x95', Char(254), (-310, 0, 3650), 2000, 0),
		Insn('0x95', Char(254), (-310, 0, 17700), 2000, 0),
		Insn('0x95', Char(254), (-14660, 0, 17700), 2000, 0),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('0x95', Char(254), (79630, 0, 11390), 2000, 0),
		Insn('0x95', Char(254), (98920, 0, 11390), 2000, 0),
		Insn('0x95', Char(254), (98920, 0, 2680), 2000, 0),
		Insn('0x95', Char(254), (98920, 0, 11390), 2000, 0),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (201290, 460), (203720, 3610), 1000),
		Insn('SLEEP', 400),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (-101350, 52570), (-96560, 54600), 1000),
		Insn('SLEEP', 400),
	]),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('EMOTE', Char(254), 0, 1700, (28, 33, 250, 0)),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_SET_POS', Char(12), (203030, 0, 4610), 0),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_SET_POS', Char(16), (154520, 0, 53680), 90),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_SET_POS', Char(9), (98920, 0, 10770), 270),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 2))),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_SET_POS', Char(12), (203030, 0, 4610), 0),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('FORK_FUNC', Char(14), 0, Function((0, 4))),
			Insn('CHAR_SET_POS', Char(9), (98920, 0, 10770), 270),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 2))),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
			Insn('FORK_FUNC', Char(8), 0, Function((0, 5))),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('FORK_FUNC', Char(14), 0, Function((0, 4))),
			Insn('CHAR_SET_POS', Char(9), (98920, 0, 10770), 270),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 2))),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_SET_POS', Char(16), (154520, 0, 53680), 90),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('FORK_FUNC', Char(14), 0, Function((0, 4))),
			Insn('CHAR_SET_POS', Char(9), (98920, 0, 10770), 270),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 2))),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('FORK_FUNC', Char(12), 0, Function((0, 3))),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('FORK_FUNC', Char(12), 0, Function((0, 3))),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_SET_POS', Char(16), (154520, 0, 53680), 90),
			Insn('CHAR_SET_POS', Char(9), (98920, 0, 10770), 270),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 2))),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_SET_POS', Char(9), (98920, 0, 10770), 270),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 2))),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_SET_POS', Char(9), (98920, 0, 10770), 270),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 2))),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
			Insn('FORK_FUNC', Char(8), 0, Function((0, 5))),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
			Insn('FORK_FUNC', Char(8), 0, Function((0, 5))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'BED02', Insn('0', 1)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('0x65', 0, 1),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('0x65', 0, 1),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('0x65', 0, 1),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('1', 1)),
		]),
		(None, []),
	]),
	Insn('EXPR_CHAR_ATTR', Char(8), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(799)), Insn('FLAG', Flag(800)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xd2\xc8\x00\x00\x00\x00\x00'),
		]),
		(Expr([Insn('FLAG', Flag(1359)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xd2\xc8\x00\x00\x00\x00\x00'),
		]),
		(Expr([Insn('FLAG', Flag(1564)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xd2\xc8\x00\x00\x00\x00\x00'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'呼……呼……\n'
						'早安……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(254), 0, 2000, (2, 7, 80, 1)),
					Insn('SOUND_PLAY', 28, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(254), Text(
						'啊，不行！\n'
						'今天必须要去\n'
						'诊察室！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'夏鲁鲁早就去\n'
						'诊察室了吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哇哇……该怎么办啊！？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('EMOTE_STOP', Char(254)),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……呼……呼…………{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……再、再睡五分钟……呼呼……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'再睡五分钟……\n'
						'不，再睡十五分钟就起床……\n'
						'呼呼……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('EMOTE', Char(254), 0, 1700, (28, 33, 250, 0)),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('EMOTE_STOP', Char(254)),
			Insn('TEXT_TALK', Char(254), Text(
				'……呼……呼……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哇……这就是最新式的\n'
				'导力镭射手术刀…………{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯……\n'
				'竟然开发了这样的东西……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(254), 0, 1700, (28, 33, 250, 0)),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……呼呼……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(254), 0, 2000, (2, 7, 80, 1)),
					Insn('SOUND_PLAY', 28, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(254), Text(
						'……啊呀，都已经这么晚了！？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不丄好丄了～啊！\n'
						'明明要在傍晚赶到\n'
						'诊察室去的～！！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'因为通宵太累导致\n'
						'睡得太熟了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不快点过去的话，\n'
						'又要被凯瑞教授\n'
						'训斥了！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(787)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呼……呼……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……还是别吵醒她比较好吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('EMOTE_STOP', Char(254)),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'呼……呼……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……哇呀！？\n'
						'……爆炸了……！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'…………呼…………呼……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F……到、到底在做什么梦呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(310), Text(
						'#1302F亚苏拉主任\n'
						'是个很忙的人……\n'
						'现在就让她休息吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……呼…………呼……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('EMOTE', Char(254), 0, 1700, (28, 33, 250, 0)),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('EMOTE_STOP', Char(254)),
			Insn('TEXT_TALK', Char(254), Text(
				'呼……呼……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(254), 0, 1700, (28, 33, 250, 0)),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊，你是昨天被送到\n'
						'赛西儿小姐房间里的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0203F……让您担心了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呼，当时确实很担心呢。\n'
						'不过，你现在看起来倒是挺精神的，这就好。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'要是以后又觉得身体不舒服的话，\n'
						'请马上再过来哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'毕竟这里是专业的医院呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀，已经这么晚了！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'啊哇哇，必须快点完成\n'
				'今天的打扫工作啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'约亚西姆副教授也住在\n'
				'这边的宿舍哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'他早上出门时永远都是那么邋遢，\n'
				'所以我总是提醒他。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天亚苏拉主任竟然准时\n'
				'去研究区了，真是很少见。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，平时都是早上才回来睡一会的……\n'
				'不知道她昨天休息了没有。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'小女孩？\n'
				'我想没有来过这边哦……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'找过院区了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'这个时间，护理师希蓉\n'
						'一般都会在屋顶\n'
						'晒床单。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'前几天还在那边的露台上\n'
						'悠闲地仰望天空……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……我全都看到了呢。\n'
						'得让她多注意一点……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'该说希蓉是毫无防范意识\n'
						'还是什么呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'总之，必须要对总是喜欢\n'
						'往露台跑的男人\n'
						'多加注意。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'听说今天亚苏拉主任\n'
						'去参加教授会议了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'因为她起得很早，\n'
						'所以估计现在这个时候\n'
						'也还是睡眼惺忪的吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'亚苏拉主任是个\n'
						'爱睡懒觉的人。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'不会在教授会议上\n'
						'也昏昏沉沉地打瞌睡吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'好安静啊……\n'
						'医生、实习医生和护理师，\n'
						'大家似乎都出门了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……啊！\n'
						'这正是一个把所有角落\n'
						'都打扫干净的机会呢！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，既然决定了……\n'
						'在大家回来之前，\n'
						'必须要让这个地方焕然一新呢！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'打扫打扫，打扫打扫！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'这里是女子宿舍，男性禁止进入哦！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……开玩笑的。\n'
				'因为要去研究区的话，\n'
				'就必须经过这个职员宿舍……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'打扫打扫……\n'
				'职员宿舍真的很干净呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'医生也是，护理师也是，\n'
				'大家都会工作到很晚，\n'
				'所以基本上都没怎么使用过这里。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((2, 4))),
				]),
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'利顿医生刚才\n'
						'回房间去休息了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'他因为上个月的魔兽事件休假了，\n'
						'所以现在约亚西姆医生就\n'
						'推了很多工作给他。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但是，能休息时\n'
						'就应该尽量休息吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，\n'
						'我也差不多该去吃午饭了吧。\n'
						'只顾着打扫了，肚子好饿啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'刚才，亚苏拉主任\n'
				'慌慌张张就出门了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'今天也跟以前一样，\n'
				'好像又睡过头了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'明明已经打扫过一次了，\n'
				'结果还是因为在意小污渍，\n'
				'所以又打扫了一次。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……毕竟是女子宿舍，\n'
				'一定要非常非常干净才行。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'好了，打扫成这样就没问题了。\n'
				'……应该是吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'但是那些小污渍\n'
				'让我好在意啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'今天男子宿舍的人\n'
						'全部都出去了哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'大概都去研究区或者\n'
						'院区工作了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'好，为了努力工作的大家，\n'
						'打扫打扫～☆{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'打扫打扫……打扫打扫……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'打～扫～真～开～心～啊☆{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'亚苏拉主任出去工作，\n'
				'而我在宿舍待着……\n'
				'这也是很稀奇的事情。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……好不容易能放个假。\n'
				'能休息的时候就必须尽量休息。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'本来还以为亚苏拉主任\n'
				'今天也会迟到的，\n'
				'不过好像还是赶上了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'因为她经常埋头研究到深夜，\n'
				'所以早上迟到\n'
				'也是常有的事。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我今天本来是打算\n'
				'回到房间之后就好好休息的……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'但考试也已经临近了，所以必须要\n'
				'尽量挤出时间来学习啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啊……\n'
				'终于能放假了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然还是跟以前一样，没什么安排。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我也去向约亚西姆医生请教下，\n'
				'开始钓鱼好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'约亚西姆医生的想法，\n'
				'我到现在还是搞不清楚。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'一开始还以为他是\n'
				'为了让我多学点东西，\n'
				'才塞给我很多工作……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'结果他好像只是\n'
				'想让自己轻松一点而已……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……盖里丄罗塞尔着……\n'
						'这边的是……拉格丄尼克森着……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'在我所持有的众多医书中，\n'
						'有好几本是我们医院\n'
						'教授们的著作呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然平时没有特别的感觉，\n'
						'但那些教授们全都是不会辱及\n'
						'最先进医疗研究机构之名的优秀人才呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'对了，不知道有没有\n'
						'约亚西姆医生写的书呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'约亚西姆丄琼塔着……\n'
						'……没有找到呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过，那个人看上去\n'
						'就对出书没什么兴趣，\n'
						'所以我也并不觉得奇怪。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'离傍晚还有一段时间……\n'
				'还是稍微学习一会吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'因为我从家里带了一大堆\n'
				'有用的医书过来呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我预定在傍晚时\n'
				'去诊察室进行临床实习。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'必须让教授看看我\n'
				'优秀的地方。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((2, 7))),
				]),
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'虽然今天休息……\n'
						'但是也必须好好学习呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'同寝室的芙萝拉也是，\n'
						'连吃饭时间\n'
						'都一直在学习。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我下个月\n'
						'也要去临床实习了……\n'
						'所以必须趁现在好好预习呢！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'为了在下次的临床实习中\n'
						'取得好的评价，\n'
						'现在必须要努力学习～！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'虽然昨天休息……\n'
				'但是因为跟希蓉在一起，\n'
				'所以累死我了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'随时都要担心她又惹出什么乱子来。\n'
				'啊，真是让人担惊受怕……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(3)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'……呃，虽然弄得我有点手忙脚乱，\n'
				'但也缓解了不少压力。\n'
				'应该也算是一个有意义的假日……吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'……今天要值夜班，\n'
				'所以打算尽早小睡一会。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……明白了的话，就赶快出去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1256)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 15))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呼呜……\n'
						'没想到竟然连续休假了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'还是工作的时候比较轻松……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'随便进别人的房间\n'
				'真是不礼貌。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'如果不是急诊患者，\n'
				'就请出去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('TEXT_TALK', Char(254), Text(
		'我要来了有关医生的小说，\n'
		'试着读了一遍。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'要是多写一些实用\n'
		'技术之类的就好了……\n'
		'算了，反正就是本娱乐小说。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'……这个给你们吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'收下了{item 718}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 718, 1),
	Insn('FLAG_SET', Flag(1256)),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1893)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 18))),
				]),
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(16), Text(
						'#1304F……那么，今天是不是\n'
						'应该多去陪陪米海尔呢～{wait}'
						'{page}'
						'#1300F今天是小滴外出的日子，\n'
						'他肯定会觉得很寂寞吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F哈哈……赛西儿姐姐\n'
						'是大家的『姐姐』呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1894)), Insn('NOT'), Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('NE'), Insn('BOOL_AND'), Insn('END')]), [
							Insn('TEXT_TALK', Char(266), Text(
								'#0608F（……这位女性，记得是那家伙的……）{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(1894)),
						]),
						(None, []),
					]),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(16), Text(
						'#1304F那么，就去给米海尔\n'
						'读读故事书吧。{wait}'
						'{page}'
						'#1302F为了应对这种情况，\n'
						'我特意把当年给罗伊德\n'
						'读过的故事书带来了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F（总觉得有些难为情啊……）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1397)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 17))),
				]),
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(16), Text(
						'#1300F对了对了，我正要带小滴\n'
						'去院子里散步呢。{wait}'
						'{page}'
						'#1304F小滴的听力很好，\n'
						'所以经常会告诉我一些\n'
						'我察觉不到的动物们的动静呢。{wait}'
						'{page}'
						'#1300F呵呵，虽然是护理师工作的一部分，\n'
						'但是这个真的很让我期待呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(16), Text(
						'#1300F跟小滴一起散步的话，\n'
						'就会有各式各样的发现，很有趣哦。{wait}'
						'{page}'
						'呵呵，虽然是护理师工作的一部分，\n'
						'但是这个真的很让我期待呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1029)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1397)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 17))),
				]),
				(Expr([Insn('FLAG', Flag(1129)), Insn('NOT'), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1128)), Insn('END')]), [
							Insn('TEXT_TALK', Char(16), Text(
								'#1309F呵呵，你们又来了呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0005F啊，说起来，赛西儿姐姐……{wait}'
								'{page}'
								'#0000F昨天和你进行过导力通讯的朋友，\n'
								'指的就是彩虹剧团的伊莉雅小姐吗？{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('TEXT_TALK', Char(16), Text(
								'#1306F嗯，因为我也住在宿舍，\n'
								'所以两个人\n'
								'很少有机会见面呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0004F哈哈，说得也是啊。{wait}'
								'{page}'
								'#0001F赛西儿姐姐……\n'
								'工作虽然忙，\n'
								'但也别太勉强自己啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(16), Text(
								'#1309F呵呵，我没有在勉强自己啊。{wait}'
								'{page}'
								'有时会用导力通讯跟朋友们聊天，\n'
								'借此来舒缓心情。{wait}'
								'{page}'
								'#1302F昨天晚上也是，和一个久未联系\n'
								'的朋友聊了很长时间呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0005F莫，莫非……\n'
								'那个朋友就是彩虹剧团的伊莉雅小姐吗？{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
					Insn('TEXT_TALK', Char(16), Text(
						'#1305F哎呀，你知道了吗？{wait}'
						'{page}'
						'#1300F奇怪了呢，我什么时候告诉你的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0011F……咦！？{wait}'
						'{page}'
						'（糟糕了，就算是对赛西儿姐姐，\n'
						'\u3000也不能泄露调查的事情……）{wait}'
						'{page}'
						'#0012F那、那个……\n'
						'……大概是之前进行\n'
						'导力通讯的时候告诉我的吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(16), Text(
						'#1303F嗯…………{wait}'
						'{page}'
						'#1300F……也是，你这么说的话，\n'
						'好像是那样的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F（好、好危险……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1129)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(16), Text(
						'#1306F啊啊，真有点遗憾。{wait}'
						'{page}'
						'本来还打算下次偷偷带你去见伊莉雅，\n'
						'让你大吃一惊的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0012F哈、哈哈……\n'
						'（都已经见过了……）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1397)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 17))),
				]),
				(Expr([Insn('FLAG', Flag(1128)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(16), Text(
						'#1306F嗯，因为我也住在宿舍，\n'
						'所以两个人\n'
						'很少有机会见面呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0004F哈哈，说得也是啊。{wait}'
						'{page}'
						'#0001F赛西儿姐姐……\n'
						'工作虽然忙，\n'
						'但也别太勉强自己啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(16), Text(
						'#1309F呵呵，我没有在勉强自己啊。{wait}'
						'{page}'
						'有时会用导力通讯跟朋友们聊天，\n'
						'借此来舒缓心情。{wait}'
						'{page}'
						'#1302F昨天晚上也是，和一个久未联系\n'
						'的朋友聊了很长时间呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0009F哈哈，这样啊。{wait}'
						'{page}'
						'#0000F那个朋友\n'
						'是我认识的人吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(16), Text(
						'#1304F呵呵……你猜呢。{wait}'
						'{page}'
						'#1302F罗伊德你有着不通世事的\n'
						'意外一面，所以可能会不认识她呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F？？？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1128)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(16), Text(
						'#1304F她似乎也在拼命努力……\n'
						'所以我也必须好好加油了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F（到底是在说谁呢……）{wait}'
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

data['code'][17] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (153900, 1000, 53760), 0),
	Insn('CAM_ROTATE', 45, 27, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 19500, 0),
	Insn('CHAR_SET_POS', Char(257), (153000, 0, 54180), 90),
	Insn('CHAR_SET_POS', Char(258), (153000, 0, 53180), 90),
	Insn('CHAR_SET_POS', Char(259), (151800, 0, 53180), 90),
	Insn('CHAR_SET_POS', Char(260), (151800, 0, 54180), 90),
	Insn('CHAR_SET_FRAME', Char(16), 0),
	Insn('CHAR_ROTATE', Char(16), 270, 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(16), Text(
		'#1302F哎呀，是大家啊。\n'
		'呵呵，欢迎。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(845)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F啊，莫非这里是\n'
				'赛西儿姐姐的宿舍吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F这里果然是\n'
				'赛西儿姐姐的宿舍吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(16), Text(
		'#1300F嗯，没错。{wait}'
		'{page}'
		'#1304F但是我平时经常睡在\n'
		'院区和休息室，\n'
		'所以这里的利用率只有一半左右呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(0), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(1), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(2), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(3), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#0106F赛西儿小姐……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0208F……您工作努力过头了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0306F请让我多帮你\n'
		'分担一些事情吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'#1309F没关系，没关系。\n'
		'我并没有勉强自己。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_POS', Char(0), (153000, 0, 53680), 90),
	Insn('FLAG_SET', Flag(1397)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (153900, 1000, 53760), 0),
	Insn('CAM_ROTATE', 45, 27, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 19500, 0),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(4), 128),
			Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
			Insn('CHAR_SET_POS', Char(266), (150600, 0, 53680), 90),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_POS', Char(257), (153000, 0, 54180), 90),
	Insn('CHAR_SET_POS', Char(258), (153000, 0, 53180), 90),
	Insn('CHAR_SET_POS', Char(259), (151800, 0, 53180), 90),
	Insn('CHAR_SET_POS', Char(260), (151800, 0, 54180), 90),
	Insn('CHAR_SET_FRAME', Char(16), 0),
	Insn('CHAR_ROTATE', Char(16), 90, 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(16), Text(
		'#1308F………………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}赛西儿正望着柜子上的照片。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(845)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F赛西儿姐姐……？\n'
				'（啊，那张照片是……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F赛西儿姐姐……\n'
				'（那张照片是……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('NE'), Insn('END')]), [
			Insn('TEXT_TALK', Char(266), Text(
				'#0608F（……这位女性，记得是那家伙的……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1894)),
		]),
		(None, []),
	]),
	Insn('EMOTE', Char(16), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(16), 270, 500),
	Insn('TEXT_TALK', Char(16), Text(
		'#1302F哎呀，欢迎大家。{wait}'
		'{page}'
		'#1305F………？\n'
		'看起来好像很急呢，\n'
		'发生什么事情了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F哈哈，是的。\n'
		'现在正在调查，所以有点忙。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F赛西儿小姐是在休息吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'#1304F呵呵，算是吧。{wait}'
		'{page}'
		'虽然你们的工作确实很重要，\n'
		'但还是注意不要勉强自己哦。{wait}'
		'{page}'
		'#1300F要是太勉强自己，\n'
		'我会强行让你们住院治疗的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0011F我、我知道了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F呵呵，谨记于心。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0309F（嗯，如果动手的人是赛西儿小姐，\n'
		'\u3000我很乐意啊～！）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0206F（……我就知道你会这么说。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_POS', Char(0), (153000, 0, 53680), 90),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(4), 128),
			Insn('CHAR_FLAG2_SET', Char(4), 32768),
		]),
		(None, []),
	]),
	Insn('FLAG_SET', Flag(1893)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('TEXT_START', Char(255)),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis000.itp'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}有一张照片，\n'
		'照片上是赛西儿和罗伊德，\n'
		'还有一个干练精神的青年。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(845)), Insn('NOT'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1397)), Insn('FLAG', Flag(1566)), Insn('OR'), Insn('END')]), [
					Insn('TEXT_MESSAGE', Char(257), Text(
						'#0008F（……和赛西儿姐姐与\n'
						'\u3000大哥的合照。）{wait}'
						'{page}'
						'（我一直随身带着……\n'
						'\u3000赛西儿姐姐也将它放在房间中呢。）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_MESSAGE', Char(257), Text(
						'#0005F（啊……和赛西儿姐姐与\n'
						'\u3000大哥的合照。）{wait}'
						'{page}'
						'#0003F（这张照片会在这里，\n'
						'\u3000也就是说，这里莫非是\n'
						'\u3000赛西儿姐姐的宿舍吗？）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('FLAG_SET', Flag(845)),
		]),
		(None, []),
	]),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]
