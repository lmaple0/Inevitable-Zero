# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't1010',
	'name2': 't1010',
	'location': 66,
	'bgm': 111,
	'flags': 8192,
	'includes': [
		't1010',
		't1030_1',
		None,
		None,
		None,
		None,
	],
	'name3': 't1010',
	'labels': [
		{
			'pos': (-5.0, 0.0, 81.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('议长宅邸方向'),
		},
		{
			'pos': (65.0, 0.0, 0.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('翠雀饭店方向'),
		},
	],
	'chcp': [
		'chr/ch27700',
		'chr/ch22302',
		'chr/ch22202',
		'chr/ch33100',
		'chr/ch33000',
		'chr/ch10200',
	],
	'npcs': [
		{
			'name': Translate('艾美'),
			'pos': (2279, -3700, -12430),
			'angle': 180,
			'_1': b'U\x01\x00\x00\x01\x00\xff\xff',
			'function': Function((0, 6)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('瑟尔'),
			'pos': (3660, -3700, -12430),
			'angle': 180,
			'_1': b'U\x01\x00\x00\x02\x00\xff\xff',
			'function': Function((0, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('卡比朗'),
			'pos': (26860, -2000, 2200),
			'angle': 270,
			'_1': b'\x01\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('卢古曼'),
			'pos': (-1970, -2000, 34720),
			'angle': 180,
			'_1': b'\x01\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((0, 10)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('男性'),
			'pos': (2400, -1799, 55840),
			'angle': 0,
			'_1': b'\x81\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((0, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('咪西'),
			'pos': (-119, -1799, 4900),
			'angle': 45,
			'_1': b'\x81\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
	],
	'monsters': [],
	'triggers': [
		{
			'pos': (-6.460000038146973, -16.520000457763672, -3.799999952316284),
			'range': 156.25,
			'transform': [
				0.20000000298023224,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				1.2920000553131104,
				3.30400013923645,
				0.7599999904632568,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (-6460, -3800, -16520),
			'range': 1200,
			'bubble_pos': (-6210, -5800, -21830),
			'_1': b'|\x00\x00',
			'function': Function((0, 12)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00B\x00', Function((0, 4)), Function((0, 5))),
	'code': [None]*15,
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
		Insn('0x95', Char(254), (26860, -2000, 2200), 2000, 0),
		Insn('0x95', Char(254), (-4019, -1800, 2200), 2000, 0),
		Insn('0x95', Char(254), (-3510, -1800, -1500), 2000, 0),
		Insn('0x95', Char(254), (26860, -2000, -2060), 2000, 0),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('0x95', Char(254), (-1970, -2000, 34720), 2000, 0),
		Insn('0x95', Char(254), (-1970, -2000, 8940), 2000, 0),
		Insn('0x95', Char(254), (2029, -2000, 8940), 2000, 0),
		Insn('0x95', Char(254), (2029, -2000, 34720), 2000, 0),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (-5350, 47570), (3980, 54910), 1000),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1333)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1330)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1329)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1320)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1319)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 55, Insn('TASK_GET', 4))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('EVENT', Function((1, 17))),
		]),
		(None, [
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('FORK_FUNC', Char(10), 0, Function((0, 1))),
			Insn('FORK_FUNC', Char(11), 0, Function((0, 2))),
		]),
	]),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('FLAG', Flag(1342)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
			Insn('OBJ_SET_FRAME', Object(255), 't1010_sky', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 't1010_sky_y', Insn('1', 1)),
		]),
		(None, [
			Insn('OBJ_SET_FRAME', Object(255), 't1010_sky', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 't1010_sky_y', Insn('0', 1)),
		]),
	]),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 7))), Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 8))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x00\x80\x00'),
		]),
		(None, []),
	]),
	Insn('0x65', 0, 1),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 7))), Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 9))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x66', 0, 1),
			Insn('EFF_LOAD', ResId(8), 'eff\\mgm03_02.eff'),
			Insn('EFF_PLAY', (ResId(8), 8), Char(255), 0, -6210, -1, -5800, -1, -21830, -1, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
		]),
		(None, []),
	]),
	Insn('SOUND_PLAY', 126, 0, 1, 80),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('EXPR_CHAR_ATTR', Char(0), 5, Expr([Insn('CHAR_ATTR', Char(254), 4), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(254), 5, Expr([Insn('CHAR_ATTR', Char(254), 4), Insn('SET'), Insn('END')])),
	Insn('TEXT_START', Char(254)),
	Insn('CHAR_FLAG1_UNSET', Char(254), 16),
	Insn('CHAR_WATCH', Char(254), Char(0), 0),
	Insn('EXPR_CHAR_ATTR', Char(254), 4, Expr([Insn('CHAR_ATTR', Char(254), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(254), 4, Expr([Insn('CHAR_ATTR', Char(254), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(254), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(254), 5, Expr([Insn('CHAR_ATTR', Char(254), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('CHAR_ATTR', Char(254), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(254), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(254), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(254), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
		(Expr([Insn('CHAR_ATTR', Char(254), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(254), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('CHAR_ATTR', Char(254), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(254), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
		]),
		(None, [
			Insn('EXPR_CHAR_ATTR', Char(254), 8, Expr([Insn('CHAR_ATTR', Char(254), 5), Insn('SET'), Insn('END')])),
		]),
	]),
	Insn('EXPR_CHAR_ATTR', Char(254), 4, Expr([Insn('CHAR_ATTR', Char(0), 5), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(0), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(254), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(254), 16),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1333)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1330)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1329)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1320)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1319)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 8))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'瑟尔太差劲了，\n'
						'真是差劲。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'要是瑟尔成为医生的话，\n'
						'我就每天都要寂寞地\n'
						'独守空房了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 8))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'瑟尔太差劲了，\n'
						'真是差劲。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'总是这种样子的话，\n'
						'又怎能让我幸福。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('EXPR_CHAR_ATTR', Char(0), 5, Expr([Insn('CHAR_ATTR', Char(254), 4), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(254), 5, Expr([Insn('CHAR_ATTR', Char(254), 4), Insn('SET'), Insn('END')])),
	Insn('TEXT_START', Char(254)),
	Insn('CHAR_FLAG1_UNSET', Char(254), 16),
	Insn('CHAR_WATCH', Char(254), Char(0), 0),
	Insn('EXPR_CHAR_ATTR', Char(254), 4, Expr([Insn('CHAR_ATTR', Char(254), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(254), 4, Expr([Insn('CHAR_ATTR', Char(254), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(254), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(254), 5, Expr([Insn('CHAR_ATTR', Char(254), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('CHAR_ATTR', Char(254), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(254), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(254), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(254), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
		(Expr([Insn('CHAR_ATTR', Char(254), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(254), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('CHAR_ATTR', Char(254), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(254), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
		]),
		(None, [
			Insn('EXPR_CHAR_ATTR', Char(254), 8, Expr([Insn('CHAR_ATTR', Char(254), 5), Insn('SET'), Insn('END')])),
		]),
	]),
	Insn('EXPR_CHAR_ATTR', Char(254), 4, Expr([Insn('CHAR_ATTR', Char(0), 5), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(0), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(254), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(254), 16),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1333)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1330)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1329)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1320)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1319)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 8))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'艾美好任性，\n'
						'我也有自己的梦想啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 8))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'艾美说的话，对于还是孩子\n'
						'的我来说，实在是无法理解。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'订婚什么的，只是父母决定的，\n'
						'我根本就无所谓啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1333)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1330)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1329)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1320)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1319)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(9), 5, Expr([Insn('CHAR_ATTR', Char(8), 4), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(8), 5, Expr([Insn('CHAR_ATTR', Char(8), 4), Insn('SET'), Insn('END')])),
			Insn('TEXT_START', Char(8)),
			Insn('CHAR_FLAG1_UNSET', Char(8), 16),
			Insn('CHAR_WATCH', Char(8), Char(9), 0),
			Insn('EXPR_CHAR_ATTR', Char(8), 4, Expr([Insn('CHAR_ATTR', Char(8), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(8), 4, Expr([Insn('CHAR_ATTR', Char(8), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(8), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(8), 5, Expr([Insn('CHAR_ATTR', Char(8), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
			Insn('IF', [
				(Expr([Insn('CHAR_ATTR', Char(8), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(8), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(8), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(8), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
				(Expr([Insn('CHAR_ATTR', Char(8), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
					Insn('EXPR_CHAR_ATTR', Char(8), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('CHAR_ATTR', Char(8), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
					Insn('EXPR_CHAR_ATTR', Char(8), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, [
					Insn('EXPR_CHAR_ATTR', Char(8), 8, Expr([Insn('CHAR_ATTR', Char(8), 5), Insn('SET'), Insn('END')])),
				]),
			]),
			Insn('EXPR_CHAR_ATTR', Char(8), 4, Expr([Insn('CHAR_ATTR', Char(9), 5), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(9), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(8), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('CHAR_FLAG1_SET', Char(8), 16),
			Insn('EXPR_CHAR_ATTR', Char(8), 5, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(9), 5, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('SET'), Insn('END')])),
			Insn('TEXT_START', Char(9)),
			Insn('CHAR_FLAG1_UNSET', Char(9), 16),
			Insn('CHAR_WATCH', Char(9), Char(8), 0),
			Insn('EXPR_CHAR_ATTR', Char(9), 4, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(9), 4, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(9), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(9), 5, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
			Insn('IF', [
				(Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
				(Expr([Insn('CHAR_ATTR', Char(9), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
					Insn('EXPR_CHAR_ATTR', Char(9), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('CHAR_ATTR', Char(9), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
					Insn('EXPR_CHAR_ATTR', Char(9), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, [
					Insn('EXPR_CHAR_ATTR', Char(9), 8, Expr([Insn('CHAR_ATTR', Char(9), 5), Insn('SET'), Insn('END')])),
				]),
			]),
			Insn('EXPR_CHAR_ATTR', Char(9), 4, Expr([Insn('CHAR_ATTR', Char(8), 5), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(8), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(9), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('CHAR_FLAG1_SET', Char(9), 16),
			Insn('TEXT_TALK', Char(8), Text(
				'听好哦，瑟尔，\n'
				'我可是你的未婚妻，\n'
				'所以你必须认真规划我们的将来。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'你有什么\n'
				'想做的工作吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'那个……\n'
				'我想在乌尔斯拉医院\n'
				'当医生……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'不行。\n'
				'我听说，一旦成为医生，\n'
				'就会经常不能回家。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'不顾家的丈夫\n'
				'可不是好丈夫哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'怎、怎么会这样……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(9), 5, Expr([Insn('CHAR_ATTR', Char(8), 4), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(8), 5, Expr([Insn('CHAR_ATTR', Char(8), 4), Insn('SET'), Insn('END')])),
			Insn('TEXT_START', Char(8)),
			Insn('CHAR_FLAG1_UNSET', Char(8), 16),
			Insn('CHAR_WATCH', Char(8), Char(9), 0),
			Insn('EXPR_CHAR_ATTR', Char(8), 4, Expr([Insn('CHAR_ATTR', Char(8), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(8), 4, Expr([Insn('CHAR_ATTR', Char(8), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(8), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(8), 5, Expr([Insn('CHAR_ATTR', Char(8), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
			Insn('IF', [
				(Expr([Insn('CHAR_ATTR', Char(8), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(8), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(8), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(8), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
				(Expr([Insn('CHAR_ATTR', Char(8), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
					Insn('EXPR_CHAR_ATTR', Char(8), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('CHAR_ATTR', Char(8), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
					Insn('EXPR_CHAR_ATTR', Char(8), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, [
					Insn('EXPR_CHAR_ATTR', Char(8), 8, Expr([Insn('CHAR_ATTR', Char(8), 5), Insn('SET'), Insn('END')])),
				]),
			]),
			Insn('EXPR_CHAR_ATTR', Char(8), 4, Expr([Insn('CHAR_ATTR', Char(9), 5), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(9), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(8), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('CHAR_FLAG1_SET', Char(8), 16),
			Insn('EXPR_CHAR_ATTR', Char(8), 5, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(9), 5, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('SET'), Insn('END')])),
			Insn('TEXT_START', Char(9)),
			Insn('CHAR_FLAG1_UNSET', Char(9), 16),
			Insn('CHAR_WATCH', Char(9), Char(8), 0),
			Insn('EXPR_CHAR_ATTR', Char(9), 4, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(9), 4, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(9), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(9), 5, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
			Insn('IF', [
				(Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
				(Expr([Insn('CHAR_ATTR', Char(9), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
					Insn('EXPR_CHAR_ATTR', Char(9), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('CHAR_ATTR', Char(9), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
					Insn('EXPR_CHAR_ATTR', Char(9), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, [
					Insn('EXPR_CHAR_ATTR', Char(9), 8, Expr([Insn('CHAR_ATTR', Char(9), 5), Insn('SET'), Insn('END')])),
				]),
			]),
			Insn('EXPR_CHAR_ATTR', Char(9), 4, Expr([Insn('CHAR_ATTR', Char(8), 5), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(8), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(9), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('CHAR_FLAG1_SET', Char(9), 16),
			Insn('TEXT_TALK', Char(8), Text(
				'听好哦，瑟尔，\n'
				'我可是你的未婚妻，\n'
				'你必须变得更加干练才行。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'那么……该怎么做呢……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'这种事就要自己去想了。\n'
				'那样的话，你就能成为\n'
				'精明干练的人了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'好、好难啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('CHAR_SET_FRAME', Char(9), 0),
	Insn('FLAG_SET', Flag(0)),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1333)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1330)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1329)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1320)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1319)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'喂喂，\n'
				'不要穿成这样\n'
				'走进住宅区。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'每个人的穿着打扮\n'
				'都要与自己所在的场所相衬。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你们至少也该去时装店\n'
				'换身像样的衣服再来吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……哎呀呀。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'几位平民，\n'
						'来高级住宅区有何贵干呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'要观光的话，\n'
						'还是到主题乐园去吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'要观光的话，\n'
						'还是到主题乐园去吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'你们这些平民，即使看了我等贵族的住宅，\n'
						'也只有眼红羡慕的份吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1333)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1330)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1329)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1320)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1319)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'据说，今天要在哈尔特曼议长宅邸\n'
				'举行庆祝纪念庆典的晚宴。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'议长好像邀请了不少\n'
				'邻国的友人哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'再往前走，\n'
						'就是哈尔特曼议长宅邸了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'第一次见的话，或许会被\n'
						'那气派雄伟的设计吓到吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哎呀呀，我也想拥有那种豪宅呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'前面就是哈尔特曼议长宅邸了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那种豪宅，\n'
						'光是维护就要花费很多钱吧……\n'
						'哎呀呀，我也想拥有那种豪宅呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'哈尔特曼议长宅邸\n'
		'应该就是这个方向吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'好像还准备了客房呢。\n'
		'早点过去，好好休息一下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('EVENT_BEGIN', 1),
	Insn('SOUND_PLAY', 1094, 0, 255, 100),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F这里的话似乎可以钓到鱼。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-3780, -2000, -21590), 1500),
	Insn('CAM_ROTATE', 315, 25, 0, 1500),
	Insn('0x6E', 320, 1500),
	Insn('CAM_DISTANCE', 39000, 1500),
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
			Insn('FLAG_UNSET', Flag(3)),
			Insn('MINIGAME', 6, 4, [
				-6440,
				-3800,
				-15510,
				180,
				-6210,
				-5800,
				-21830,
			]),
			Insn('IF', [
				(Expr([Insn('ATTR', 69), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('0xE0', b'\x02'),
	Insn('EVENT_END', 4),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 9))), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 14))),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-4510, -2000, -17230), 0),
	Insn('CAM_ROTATE', 315, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 24740, 0),
	Insn('CHAR_SET_POS', Char(257), (-7200, -3800, -15000), 180),
	Insn('CHAR_SET_POS', Char(258), (-6000, -3800, -15000), 180),
	Insn('CHAR_SET_POS', Char(259), (-7200, -3800, -13800), 180),
	Insn('CHAR_SET_POS', Char(260), (-6000, -3800, -13800), 180),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(337), (-4800, -3800, -14400), 180),
		]),
		(None, []),
	]),
	Insn('EFF_STOP', (ResId(1), 2)),
	Insn('0x0D'),
	Insn('EMOTE', Char(0), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(1), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(2), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(3), 0, 2000, (38, 38, 250, 1)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('EMOTE', Char(337), 0, 2000, (38, 38, 250, 1)),
		]),
		(None, []),
	]),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (-2980, -2000, -24760), 3000),
	Insn('CAM_DISTANCE', 21000, 3000),
	Insn('0x6F', b'y'),
	Insn('EFF_LOAD', ResId(0), 'event\\eva00_00.eff'),
	Insn('EFF_PLAY', (ResId(0), 0), Char(255), 0, -6210, -1, -5800, -1, -21830, -1, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('SOUND_PLAY', 860, 0, 0, 100),
	Insn('SLEEP', 3000),
	Insn('EFF_STOP', (ResId(0), 2)),
	Insn('SLEEP', 2000),
	Insn('QUEST', 36, Insn('TASK_SET', 8)),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('CHAR_SET_POS', Char(0), (-7200, -3800, -15000), 180),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-4510, -2000, -17230), 0),
	Insn('CAM_ROTATE', 315, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 24740, 0),
	Insn('CHAR_SET_POS', Char(257), (-7200, -3800, -15000), 180),
	Insn('CHAR_SET_POS', Char(258), (-6000, -3800, -15000), 180),
	Insn('CHAR_SET_POS', Char(259), (-7200, -3800, -13800), 180),
	Insn('CHAR_SET_POS', Char(260), (-6000, -3800, -13800), 180),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(337), (-4800, -3800, -14400), 180),
		]),
		(None, []),
	]),
	Insn('EFF_STOP', (ResId(1), 2)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0005F这、这个难道是……\n'
		'托马先生的订婚戒指吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#5P#0205F鱼吞下了落入\n'
		'湖底的戒指……\n'
		'应该是这样吧。{wait}'
		'{page}'
		'#0206F……这种现象的稀有度，简直可以与\n'
		'天文学上的低概率事件相媲美了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0106F是、是啊……\n'
		'实在是令人\n'
		'意想不到啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('TEXT_TALK', Char(337), Text(
				'#11P#5709F哈哈哈！\n'
				'这就叫世事难料。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(260), Text(
		'#11P#0306F害我们四处跑了一遍，\n'
		'结果却是这样。\n'
		'总觉得有些无法接受……{wait}'
		'{page}'
		'#0300F不过，反正也找到了，\n'
		'也算是万事大吉吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0000F是啊……\n'
		'那么，去找托马先生\n'
		'确认一下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('QUEST', 36, Insn('TASK_SET', 9)),
	Insn('0x65', 0, 1),
	Insn('CHAR_SET_POS', Char(0), (-7200, -3800, -15000), 180),
	Insn('EFF_STOP', (ResId(8), 2)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]
