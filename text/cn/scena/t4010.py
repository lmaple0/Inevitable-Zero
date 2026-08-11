# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't4010',
	'name2': 't4010',
	'location': 93,
	'bgm': 124,
	'flags': 8192,
	'includes': [
		't4010',
		't4010_1',
		None,
		None,
		None,
		None,
	],
	'name3': 't4010',
	'labels': [],
	'chcp': [
		'chr/ch26500',
		'chr/ch25300',
		'chr/ch25400',
		'chr/ch25500',
		'chr/ch21802',
		'chr/ch00800',
		'chr/ch23800',
		'chr/ch23802',
		'chr/ch20702',
		'chr/ch22302',
		'chr/ch21402',
		'chr/ch20602',
		'chr/ch22202',
		'chr/ch09302',
		'chr/ch09402',
		'chr/ch07202',
		'chr/ch10300',
		'chr/ch24602',
		'chr/ch24702',
		'chr/ch23902',
		'chr/ch34202',
		'chr/ch21502',
		'chr/ch24400',
		'chr/ch17202',
		'chr/ch17302',
	],
	'npcs': [
		{
			'name': Translate('艾拉尔达大主教'),
			'pos': (-209, 379, 23229),
			'angle': 180,
			'_1': b'\x01\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((0, 5)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('基纳斯祭司'),
			'pos': (-2960, 250, 20010),
			'angle': 180,
			'_1': b'\x01\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('伦顿祭司'),
			'pos': (98069, 0, 6789),
			'angle': 315,
			'_1': b'\x01\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 8)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('哈缇娜修女'),
			'pos': (2950, 189, 19709),
			'angle': 165,
			'_1': b'\x01\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('玛布林修女'),
			'pos': (150800, 200, 17500),
			'angle': 180,
			'_1': b'\x01\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('贸易商摩尔吉奥'),
			'pos': (-3849, 150, 6519),
			'angle': 0,
			'_1': b'U\x01\x00\x00\x04\x00\xff\xff',
			'function': Function((0, 14)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('诺艾儿上士'),
			'pos': (1289, 0, 23229),
			'angle': 270,
			'_1': b'\x81\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('泰米尔'),
			'pos': (153690, 200, 16420),
			'angle': 45,
			'_1': b'\x81\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((0, 16)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('哈米尔'),
			'pos': (154850, 200, 16180),
			'angle': 0,
			'_1': b'\x81\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((0, 17)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('小桃'),
			'pos': (147139, 150, 12229),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x08\x00\xff\xff',
			'function': Function((0, 19)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('潘莎'),
			'pos': (148490, 150, 9130),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\t\x00\xff\xff',
			'function': Function((0, 20)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('库塔'),
			'pos': (148490, 150, 12229),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\n\x00\xff\xff',
			'function': Function((0, 21)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('约葛特'),
			'pos': (147139, 150, 9130),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x14\x00\xff\xff',
			'function': Function((0, 22)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('安里'),
			'pos': (154929, 150, 12229),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x0c\x00\xff\xff',
			'function': Function((0, 23)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客塔库特'),
			'pos': (1649, 0, 11819),
			'angle': 0,
			'_1': b'\x81\x01\x00\x00\x16\x00\x00\x00',
			'function': Function((0, 38)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('男孩'),
			'pos': (154929, 150, 9130),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x11\x00\xff\xff',
			'function': Function((0, 29)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('女孩'),
			'pos': (153619, 150, 6150),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x12\x00\xff\xff',
			'function': Function((0, 30)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('男孩'),
			'pos': (153619, 150, 6150),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x07\x00\xff\xff',
			'function': Function((0, 31)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('女孩'),
			'pos': (148490, 150, 6150),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x13\x00\xff\xff',
			'function': Function((0, 32)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('肯恩'),
			'pos': (154929, 150, 6150),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x17\x00\xff\xff',
			'function': Function((0, 25)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('娜娜'),
			'pos': (154929, 150, 9130),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x18\x00\xff\xff',
			'function': Function((0, 26)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('男孩'),
			'pos': (154929, 150, 12229),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x0b\x00\xff\xff',
			'function': Function((0, 27)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('女孩'),
			'pos': (153619, 150, 9130),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x15\x00\xff\xff',
			'function': Function((0, 28)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('哈罗德'),
			'pos': (-5250, 200, 16600),
			'angle': 360,
			'_1': b'\x85\x01\x00\x00\r\x00\xff\xff',
			'function': Function((0, 33)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('苏菲亚'),
			'pos': (-3250, 200, 16600),
			'angle': 360,
			'_1': b'\x85\x01\x00\x00\x0e\x00\xff\xff',
			'function': Function((0, 34)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('柯林'),
			'pos': (-4250, 200, 16600),
			'angle': 360,
			'_1': b'\x85\x01\x00\x00\x0f\x00\xff\xff',
			'function': Function((0, 35)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('雷缇'),
			'pos': (29, 0, 10930),
			'angle': 0,
			'_1': b'\x81\x01\x00\x00\x10\x00\x00\x00',
			'function': Function((0, 36)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('龙'),
			'pos': (153619, 150, 12229),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x0b\x00\xff\xff',
			'function': Function((0, 37)),
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
	],
	'monsters': [],
	'triggers': [],
	'objects': [
		{
			'pos': (150910, 200, 16530),
			'range': 1200,
			'bubble_pos': (150800, 1700, 17500),
			'_1': b'~\x00\x00',
			'function': Function((0, 10)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (40, 500, 21930),
			'range': 1200,
			'bubble_pos': (-210, 2100, 23230),
			'_1': b'~\x00\x00',
			'function': Function((0, 4)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00]\x00', Function((0, 2)), Function((0, 3))),
	'code': [None]*56,
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
		Insn('CHAR_IDLE', Char(254), (96910, 4700), (100000, 7500), 1000),
		Insn('SLEEP', 450),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('FORK_FUNC', Char(10), 0, Function((0, 1))),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(34), 128),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(11), (149530, 200, 17470), 90),
			Insn('CHAR_ROTATE', Char(12), 270, 0),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_ROTATE', Char(8), 90, 0),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('CHAR_FLAG1_UNSET', Char(20), 128),
			Insn('CHAR_FLAG1_UNSET', Char(25), 128),
			Insn('CHAR_FLAG1_UNSET', Char(26), 128),
			Insn('CHAR_FLAG1_UNSET', Char(29), 128),
			Insn('CHAR_FLAG1_UNSET', Char(30), 128),
			Insn('CHAR_FLAG1_UNSET', Char(27), 128),
			Insn('CHAR_FLAG1_UNSET', Char(28), 128),
			Insn('CHAR_SET_POS', Char(27), (153620, 150, 9130), 0),
			Insn('CHAR_SET_POS', Char(28), (154930, 150, 9130), 0),
			Insn('CHAR_SET_POS', Char(30), (153620, 150, 12230), 0),
			Insn('CHAR_FLAG1_SET', Char(11), 128),
		]),
		(Expr([Insn('FLAG', Flag(1514)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(35), 128),
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_SET_POS', Char(17), (154930, 150, 9130), 0),
			Insn('CHAR_SET_CHCP', Char(15), 7),
			Insn('CHAR_SET_FRAME', Char(15), 0),
			Insn('FORK_QUIT', Char(15), 0),
			Insn('CHAR_FLAG1_SET', Char(15), 4),
			Insn('CHAR_FLAG1_SET', Char(15), 16),
			Insn('CHAR_SET_POS', Char(15), (148490, 150, 12230), 0),
			Insn('CHAR_SET_CHCP', Char(16), 7),
			Insn('CHAR_SET_FRAME', Char(16), 0),
			Insn('FORK_QUIT', Char(16), 0),
			Insn('CHAR_FLAG1_SET', Char(16), 4),
			Insn('CHAR_FLAG1_SET', Char(16), 16),
			Insn('CHAR_SET_POS', Char(16), (147140, 150, 12230), 0),
			Insn('CHAR_FLAG1_UNSET', Char(27), 128),
			Insn('CHAR_FLAG1_UNSET', Char(28), 128),
			Insn('CHAR_SET_POS', Char(27), (147140, 150, 9130), 0),
			Insn('CHAR_SET_POS', Char(28), (148490, 150, 9130), 0),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(12), (148920, 0, 13890), 180),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_SET_POS', Char(12), (154300, 200, 17590), 180),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(31), 128),
			Insn('CHAR_FLAG1_UNSET', Char(32), 128),
			Insn('CHAR_FLAG1_UNSET', Char(33), 128),
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_SET_POS', Char(10), (96000, 0, 7830), 270),
			Insn('FORK_FUNC', Char(10), 0, Function((0, 0))),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_SET_POS', Char(10), (96000, 0, 7830), 270),
			Insn('FORK_FUNC', Char(10), 0, Function((0, 0))),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
			Insn('CHAR_FLAG1_UNSET', Char(23), 128),
			Insn('CHAR_FLAG1_UNSET', Char(24), 128),
			Insn('CHAR_SET_CHCP', Char(15), 7),
			Insn('CHAR_SET_FRAME', Char(15), 0),
			Insn('FORK_QUIT', Char(15), 0),
			Insn('CHAR_FLAG1_SET', Char(15), 4),
			Insn('CHAR_FLAG1_SET', Char(15), 16),
			Insn('CHAR_SET_POS', Char(15), (154930, 0, 12230), 0),
			Insn('CHAR_SET_CHCP', Char(16), 7),
			Insn('CHAR_SET_FRAME', Char(16), 0),
			Insn('FORK_QUIT', Char(16), 0),
			Insn('CHAR_FLAG1_SET', Char(16), 4),
			Insn('CHAR_FLAG1_SET', Char(16), 16),
			Insn('CHAR_SET_POS', Char(16), (153620, 0, 12230), 0),
			Insn('CHAR_FLAG1_UNSET', Char(27), 128),
			Insn('CHAR_FLAG1_UNSET', Char(28), 128),
			Insn('CHAR_SET_POS', Char(27), (147140, 150, 6150), 0),
			Insn('CHAR_SET_POS', Char(28), (148490, 150, 6150), 0),
			Insn('CHAR_FLAG1_SET', Char(27), 16),
			Insn('CHAR_FLAG1_SET', Char(28), 16),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), []),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1280)), Insn('FLAG', Flag(1342)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(22), 128),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1514)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('0x65', 0, 1),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('0x65', 0, 1),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), []),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 106), Insn('EQ'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1536)), Insn('FLAG', Flag(1554)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1077)), Insn('NOT'), Insn('END')]), [
							Insn('EVENT', Function((0, 40))),
						]),
						(None, []),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1024)), Insn('FLAG', Flag(1040)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1076)), Insn('NOT'), Insn('END')]), [
							Insn('EVENT', Function((0, 39))),
						]),
						(None, []),
					]),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('0x7D', b'\xff\xd2\xc8\x00\x00\x00\x00\x00'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('CALL', Function((0, 5))),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('TEXT_START', Char(8)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'遗迹中的那口大钟……\n'
						'到底是怎么回事呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'（如果那个钟是古代遗物的话……\n'
						'\u3000引来那些人插手的\n'
						'\u3000可能性就很高了。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'（……哼，岂能让他们得逞。\n'
						'\u3000我绝对不会允许那种人\n'
						'\u3000进入克洛斯贝尔。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'……嗯，那就这样吧。\n'
						'关于那个遗迹与『星见之塔』，\n'
						'我们这边也会进行调查。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 6))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'能够召唤出『恶魔』的钟……\n'
						'那个遗迹中居然还\n'
						'存在着这种东西吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'听说黑手党之间发生了斗争啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'没有将普通市民卷入，也算是万幸……\n'
						'但这种行为实在是太愚蠢了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'女神啊！请把人们从斗争\n'
						'的因果循环中解放出来吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'没有将无辜的市民卷入，\n'
						'实在是太好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'女神啊！请把人们从斗争\n'
						'的因果循环中解放出来吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(8), Text(
				'……嗯……是错觉吗？\n'
				'似乎从山道那边传来了钟声。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'奇怪，玛因兹那边\n'
				'应该没有钟楼之类的地方啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(265), Text(
				'#0505F（……钟……？\n'
				'\u3000有点在意呢……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'你们好像已经和\n'
						'玛布林修女谈过了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'……事情已经解决了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F是、是的。\n'
						'得到了贵重的情报，非常感谢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'……那就好，\n'
						'欢迎随时再来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'空之女神啊，请引导他们吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'要是有什么烦恼，\n'
						'欢迎随时前来拜访。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'空之女神啊，请引导他们吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'欢迎来到\n'
						'克洛斯贝尔大教堂。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(339), Text(
						'#1110F……啊，长胡子老爷爷！\n'
						'嘿嘿，我可以摸一下吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(8), Char(339), 500),
					Insn('EMOTE', Char(8), 0, 2000, (38, 38, 250, 1)),
					Insn('CHAR_WATCH', Char(8), Char(339), 500),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(8), Text(
						'唔……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0011F等一下，琪、琪雅！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
							Insn('TEXT_TALK', Char(258), Text(
								'#0103F真、真是十分抱歉，大主教。\n'
								'这孩子太没礼貌了……{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
							Insn('TEXT_TALK', Char(259), Text(
								'#0203F……失礼了。\n'
								'请您原谅，她毕竟只是个小孩子……{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
							Insn('TEXT_TALK', Char(260), Text(
								'#0303F真、真对不起，大主教。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, []),
					]),
					Insn('TEXT_TALK', Char(8), Text(
						'哪里……不用介意。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'对于小孩子来说，\n'
						'活泼有精神就是最好的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'女神啊，请赐予这孩子祝福……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'对于小孩子来说，活泼有精神就是最好的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'女神啊，请赐予这孩子祝福……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'好了……\n'
						'今晚的弥撒结束之后，\n'
						'创立纪念庆典的所有活动便将圆满落幕。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'今年也有很多人前来参加弥撒呢，\n'
						'愿女神的祝福与他们同在……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'今年的纪念庆典\n'
						'也来了很多参加弥撒的人。\n'
						'愿女神的祝福与他们同在……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'有一个看起来像是帝国政府要员的男人\n'
						'在深夜造访大教堂。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'似乎是看中了七耀教会的影响力，\n'
						'想要拉拢\n'
						'身为大主教的我……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'我以严厉的呵斥将他赶了出去。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'身为空之女神仆人的我\n'
						'必须要彻底保持中立。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'七耀教会在这片大陆上\n'
						'得到了人们深厚的信仰。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'竟然想要将它利用于政治，\n'
						'那简直是对女神的侮辱。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'听说昨晚有人在旧市街\n'
						'那边引起了很大的骚动。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'本来还以为只是旧市街的那些年轻人，\n'
						'没想到竟然连游击士和警察也跟着\n'
						'一起胡闹啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F（惊……！）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'……嗯？果然是你们吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'虽然纪念庆典让人情绪高昂，\n'
						'有时难免会失去冷静的判断力。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'但身为警察，可不能那样乱来啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0306F对、对不起……{wait}'
						'{page}'
						'（这个老爷爷\n'
						'\u3000有种奇妙的压迫感啊……！）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'……不过，在昨天的事件中\n'
						'并没有人遭受重伤，\n'
						'这可以算是不幸中的万幸了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'你们以后务必要严于律己、谨慎行动。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'创立７０周年纪念吗？\n'
						'想想的话，这段历史也不算短了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'痛苦与悲伤……\n'
						'这个自治州也发生过很多事情呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'大家都会以自己的方式\n'
						'来度过此次庆典吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'……唔，\n'
						'我也不能满足于\n'
						'只举行弥撒。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'还是回归初愿，\n'
						'读读调配药剂的书吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'我也不能在这７０周年\n'
						'的庆典中只顾着\n'
						'举行弥撒。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'还是回归初愿，\n'
						'读读调配药剂的书吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('TASK_GET', 1))), Insn('END')]), [
					Insn('CALL', Function((0, 45))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('TASK_GET', 0))), Insn('END')]), [
					Insn('CALL', Function((0, 43))),
				]),
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'据说，在向空之女神祈祷时，\n'
						'人们的心灵将会回归至最清净的状态。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'进而从苦闷中解放出来，\n'
						'闭上双眼，在黑暗中\n'
						'获得一个重新审视自己的机会……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'……你们如果愿意的话，\n'
						'也来参加弥撒吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'据说，在向空之女神祈祷时，\n'
						'人们的心灵将会回归至最清净的状态。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'……你们如果愿意的话，\n'
						'也来参加弥撒吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('TASK_GET', 1))), Insn('END')]), [
					Insn('CALL', Function((0, 45))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('TASK_GET', 0))), Insn('END')]), [
					Insn('CALL', Function((0, 43))),
				]),
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'今天将会在这个大教堂中\n'
						'举行弥撒哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'空之女神守护着人们的生活，\n'
						'赐予我们生命……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'为了让大家铭记女神的恩惠，\n'
						'举办弥撒这样的活动是很有必要的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'今天将会在这个大教堂中\n'
						'举行弥撒哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'你们也不要忘记\n'
						'向女神感恩哦！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'关于你们特务支援课的活动……\n'
						'虽然只有少许，但我也有所耳闻。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'虽然世人都挪揄说\n'
						'你们在模仿游击士……\n'
						'但你们并没有必要介意。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'空之女神\n'
						'绝对不会抛弃\n'
						'贯彻正确的信念而行动的人们。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'志愿帮助他人的人，\n'
						'对于这个世界来说，可谓是一笔财富。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'空之女神\n'
						'绝对不会抛弃\n'
						'贯彻正确的信念而行动的人们。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'欢迎各位来到这所\n'
						'克洛斯贝尔大教堂。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'看样子，你们似乎\n'
						'准备进入山道啊？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'空之女神啊，请引导他们吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'七耀的教诲定会将你们\n'
						'从迷茫中拯救出来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'空之女神啊，请引导他们吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(8)),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('0x4B', Char(8), -1),
	Insn('0x4B', Char(14), -1),
	Insn('CHAR_WATCH', Char(8), Char(14), 0),
	Insn('CHAR_WATCH', Char(14), Char(8), 0),
	Insn('TEXT_TALK', Char(14), Text(
		'#0501F……这是有关遗迹内部的\n'
		'调查报告书。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'呼唤出魔物的钟……\n'
		'那座遗迹里面竟然有那样的东西……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'………………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'确实，它很有可能\n'
		'是古代遗物……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'嗯，感谢你提供这些情报。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0500F是。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('NE'), Insn('END')]), [
			Insn('TEXT_TALK', Char(266), Text(
				'#0604F警备队的诺艾儿上士吗……\n'
				'听说她是一个恪守礼仪，并且很有才能的新星。{wait}'
				'{page}'
				'#0602F……哼，你们也稍微\n'
				'学习一下她的那股勤奋劲吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0310F（唔……\n'
				'\u3000小缇，他明显是在攻击\n'
				'\u3000我们的软肋啊。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0211F（哪有……被攻击的\n'
				'\u3000只有兰迪前辈你一个人吧。）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('FLAG_SET', Flag(0)),
	Insn('0x4C', Char(8), -1),
	Insn('0x4C', Char(14), -1),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天早上，警备队的诺艾儿上士\n'
				'把调查克洛斯贝尔遗迹\n'
				'的报告书送来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'既然很有可能\n'
				'与古代遗物有所关联……\n'
				'那么教会也不可能坐视不理啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'……诺艾儿上士所说的那口钟\n'
				'到底是个什么样的东西呢？\n'
				'真让人在意啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'而且，那口钟为什么会\n'
				'突然响起来呢……？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'对于在市内发生的那起袭击事件，\n'
				'艾拉尔达大主教感到十分痛心。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'因为大主教最厌恶\n'
				'有违道德之事……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哈缇娜修女\n'
				'今天要去给旧市街\n'
				'的孩子们授课。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'因为旧市街的孩子们\n'
				'几乎都不来主日学校，\n'
				'所以我们才会主动派人过去。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'教会里传承的『法术』与\n'
				'乌尔斯拉医院的近代医疗技术……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'两者所注重的领域分别为\n'
				'精神的治愈与身体的诊疗，共同为人们带来福音。\n'
				'但现阶段，这两者基本无法协同合作。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'这其中，也有近代医疗技术\n'
				'尚在发展途中，还未成熟的原因在内。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'在纪念庆典结束后的这一周，\n'
				'城市虽然和平……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'但有些市民似乎却\n'
				'感到了某种紧张的气氛，\n'
				'所以来教会进行祈祷。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯……\n'
				'是不是发生什么事了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今年也有很多人\n'
				'来参加弥撒了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'到了明年的纪念庆典，\n'
				'希望他们还能保持着愉快明朗的心情，\n'
				'再次造访这里……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'空之女神啊，请为迷途的羔羊们\n'
				'指引正确的道路吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'艾拉尔达大主教在药剂调配领域\n'
				'的成就十分卓越。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'乌尔斯拉医院的药\n'
				'有许多都是以大主教从前\n'
				'所调配的药剂为范本制作的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'庆典的第一天，为了祈祷纪念庆典能够成功，\n'
				'麦克道尔市长与哈尔特曼议长\n'
				'都来到了这里。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然两人一直都处于对立状态，\n'
				'但为了克洛斯贝尔市的市民，\n'
				'真希望他们两个能够携手合作啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(13)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'哈罗德先生一家\n'
						'经常拜访这所教堂，\n'
						'然后虔诚地祈祷。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不忘却对空之女神的信仰……\n'
						'这份诚心十分值得赞赏。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'伟大的空之女神啊，\n'
						'请保佑虔诚的他们……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(13)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'伟大的空之女神啊，\n'
						'请保佑虔诚的他们……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'ＩＢＣ的迪塔先生\n'
				'来祈祷的时候，\n'
				'总是开着巨大的高级轿车过来。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然好几次都差点被撞到，\n'
				'但只要一看到他面带爽朗笑容的道歉，\n'
				'便觉得生不起气来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'克洛斯贝尔市的\n'
				'市长阁下有时候也会\n'
				'拜访这所大教堂。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'似乎是趁着工作空闲的时候，\n'
				'为了克洛斯贝尔市的和平\n'
				'而来祈祷的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'从很久很久以前的大崩坏\n'
				'时代开始，七耀教会\n'
				'就一直为人们带来光明。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'这所大教堂也是七耀教会的设施之一……\n'
				'空之女神肯定会为迷途的人们\n'
				'指明正确的道路。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'艾拉尔达大主教对\n'
						'古代遗物的管理机关\n'
						'『封圣省』很没有好感。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'因为据传闻说，隶属于封圣省的组织\n'
						'『星杯骑士团』在暗地里进行了\n'
						'许多肮脏的勾当。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'对于厌恶非法活动的\n'
						'艾拉尔达大主教来说，\n'
						'他们是绝对无法原谅的存在。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'艾拉尔达大主教对隶属于封圣省的组织\n'
						'『星杯骑士团』很没有好感。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'对于厌恶非法活动的\n'
						'艾拉尔达大主教来说，\n'
						'他们是绝对无法原谅的存在。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'主日学校放假了哦，\n'
				'好安静啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'艾拉尔达大主教也对这次的事件\n'
				'感到非常愤慨。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然这次事件没有给市民带来伤害，\n'
				'但仅仅出于争斗这样自私的理由\n'
				'就让大家陷入不安，实在是无法原谅啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'教会的圣典中记载了\n'
				'『恶魔』这种存在。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'传说，那是与女神相对的负面存在，\n'
				'有时会利用人们心灵的弱点，\n'
				'引诱他们做下恶事。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'对我们教会的人来说，\n'
				'那确实是戒律的象征。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'玛布林修女从很久以前开始\n'
				'就在大教堂工作了，\n'
				'在七耀教会中有着很广的人脉。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'再加上她品行端方，\n'
				'为了向她求助而前来拜访的人也不少呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯……为了让艾拉尔达大主教\n'
				'能够安心工作，\n'
				'我必须要努力支持他。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'创立纪念庆典到今天就要结束了，\n'
				'主日学校也会从明天重新开课。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'一想到可以再次见到那群孩子们，\n'
				'就感觉突然充满了干劲呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'大主教这种职位，其发言\n'
				'在七耀教会中也有着相当大的影响力。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'特别艾拉尔达大主教，\n'
				'可是七耀教会的机关──典礼省\n'
				'的高层人士。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'他绝对不会参与违法行为，\n'
				'因此我们这些下属\n'
				'都能放心的追随他。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'ＩＢＣ的迪塔总裁\n'
				'利用他雄厚的经济实力\n'
				'进行着各式各样的慈善活动。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'作为教会的相关人员，\n'
				'我实在是非常敬佩他。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'经常来这所教堂祈祷的\n'
						'贸易商摩尔吉奥先生……\n'
						'有点过于依赖女神了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'他把自己的成功\n'
						'全部都归结于向女神献上了祈祷……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但我觉得，将自己的努力\n'
						'全部都归功于女神，\n'
						'似乎也不太好呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'经常来这所教堂祈祷的\n'
						'贸易商摩尔吉奥先生……\n'
						'有点过于依赖女神了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然由身为祭司的我来说有些不太合适，\n'
						'但我觉得过于依赖女神\n'
						'也不太好呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'嗯……希望那个羽扇豆草\n'
						'能帮上医院的忙啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我们七耀教会也对\n'
						'乌尔斯拉医院抱有很大期待。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('TASK_GET', 2))), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'哎，虽然大主教有些顽固……\n'
						'但却是一个明事理的人。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'对于拉格教授的实力，\n'
						'大主教还是很认可的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('TASK_GET', 1))), Insn('END')]), [
					Insn('CALL', Function((0, 44))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('TASK_GET', 0))), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'哎呀，有什么事情吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这里是艾拉尔达大主教的办公室，\n'
						'无关人员不能随便进入哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'艾拉尔达大主教\n'
						'出版了好几本\n'
						'有关七耀教会的书籍。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'读者都评价说书的内容\n'
						'言简意赅，十分好懂。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'旧市街的不良分子\n'
						'是叫『剑蛇帮』跟\n'
						'『圣约帮』吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'特别是圣约帮的孩子们，\n'
						'打扮得简直就像是个\n'
						'宗教团体。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真是令人叹息啊。\n'
						'如果可以的话，真希望他们能得到一个改过自新的机会呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'剑蛇帮还有\n'
						'圣约帮的孩子们……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'如果可以的话，真希望他们能得到一个改过自新的机会呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'艾拉尔达大主教是一个很严格的人。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'对有违道德的行为绝不姑息，\n'
						'但对心存迷惘的人，\n'
						'一定会温柔地伸出援助之手……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'作为祭司，\n'
						'我真是十分憧憬他。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'对有违道德的行为绝不姑息，\n'
						'但对心存迷惘的人，\n'
						'一定会温柔地伸出援助之手……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'艾拉尔达大主教就是那样的人，\n'
						'真是让人憧憬啊。{wait}'
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

data['code'][9] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'明天一大早\n'
				'要去矿山镇玛因兹出差。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'希望孩子们\n'
				'还像以前一样健康活泼。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'明天将要出差去矿山镇玛因兹，\n'
				'进行主日学校的授课，\n'
				'所以正在讨论上课的内容。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然出差很辛苦，\n'
				'但可以见到平时看不到的孩子们，\n'
				'很让人期待啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天来做礼拜的人数\n'
				'似乎比平时多了不少啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'由于港湾区的骚乱，\n'
				'市里的人似乎也感到了不安。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'……看你们的样子，\n'
				'应该是有些收获吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，真不愧是玛布林修女。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'遇到什么困难了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'如果有什么烦恼的话，可以去\n'
				'跟大主教或玛布林修女\n'
				'商量一下。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'那两位都长年\n'
				'在教会工作，\n'
				'一定能为你们提供一些有用的建议。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'创立纪念庆典剩下的日子\n'
				'就只有今天了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'空之女神啊，\n'
				'请保佑庆典就这样顺利结束……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'昨天真是吓了一大跳。\n'
						'那个人竟然\n'
						'对大主教提出了那种建议……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'笼罩在克洛斯贝尔自治州的黑暗，\n'
						'说不定比预想中还要根深蒂固得多呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'竟然如此大胆，妄图拉拢\n'
						'一个教区的大主教……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'笼罩在克洛斯贝尔自治州的黑暗，\n'
						'说不定比预想中还要根深蒂固得多呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'久久修女虽然很冒失，\n'
				'但十分擅长制作料理呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵……\n'
				'孩子们说不定就是被她做的饼干\n'
				'给吸引过来的呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'昨天是纪念庆典的第一天，\n'
						'有很多人来参加弥撒。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'悼念曾在过去发生的数次战争中\n'
						'不幸丧生的人们……\n'
						'很多人正是抱着这种想法而来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'以创立第７０周年为契机，\n'
						'克洛斯贝尔自治州\n'
						'到底会变成什么样呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'在克洛斯贝尔居民的脑海中，\n'
						'残留最深刻的大概还是有关战争的回忆吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'以创立第７０周年为契机，\n'
						'克洛斯贝尔自治州\n'
						'到底会变成什么样呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'在七耀教会的设施中，\n'
						'开设了向孩子们传授知识的\n'
						'『主日学校』。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'玛布林修女今天\n'
						'也在主日学校\n'
						'授课。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'这所大教堂的主日学校\n'
						'从很久以前开始\n'
						'就是由玛布林修女负责的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我明天也要去\n'
						'旧市街那边出差。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'听说外面现在\n'
						'正因为狼型魔兽的事件闹得沸沸扬扬。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'对很多人来说，魔兽本来就是不安的源头。\n'
						'如果魔兽再袭击人的话，就更加令人惶恐了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'希望之后不要再发生\n'
						'更加严重的事件了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'关于狼型魔兽所带来的受害情况……\n'
						'听说已经有受伤的人员出现了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'希望之后不要再发生\n'
						'更加严重的事件了……{wait}'
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

data['code'][10] = [
	Insn('CALL', Function((0, 11))),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('TEXT_START', Char(12)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1346)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 41))),
		]),
		(Expr([Insn('FLAG', Flag(1123)), Insn('NOT'), Insn('END')]), [
			Insn('EXPR_VAR', 3, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
				(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), []),
				(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
				(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
				(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
				(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
				(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
				(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
					Insn('EXPR_VAR', 3, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('FLAG', Flag(801)), Insn('END')]), []),
				(None, []),
			]),
			Insn('CALL', Function((0, 13))),
		]),
		(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'罗伊德、艾莉……\n'
				'虽然很高兴能再次见到你们，\n'
				'但我现在还在上课。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'如果你们不介意的话，\n'
				'可以等到学校没课的时候再来吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'听说你们也协助\n'
						'警备队参加了调查吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'呵呵，你们在各项工作中都表现得很活跃呢。\n'
						'作为你们曾经的老师，我感到很自豪啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'下次在主日学校上课时，要不要炫耀一下呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F哈哈……\n'
						'老师，您就放过我们吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0113F老师您可真是的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'呵呵，我真的很为你们感到自豪啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'我的学生罗伊德与艾莉\n'
						'作为市民的模范而展现出了正义的一面……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'我觉得没有比这\n'
						'更了不起的事情了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_ROTATE', Char(12), 270, 0),
					Insn('TEXT_TALK', Char(12), Text(
						'嗯……玛因兹那边\n'
						'从以前开始就一直支撑着\n'
						'克洛斯贝尔的经济。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'为了让年纪幼小的孩子们\n'
						'也能为此感到自豪，\n'
						'教他们学学历史如何呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'哎呀，罗伊德、艾莉……\n'
						'今天有什么事情吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'现在还有些忙，\n'
						'稍微晚点再过来找我吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'哎呀，罗伊德和艾莉……\n'
						'发生什么事情了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'你们的表情看起来好严肃……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0008F……不，没什么事情。{wait}'
						'{page}'
						'#0003F（在克洛斯贝尔市内\n'
						'\u3000发现了这种药锭，\n'
						'\u3000这种事情实在是无法向老师开口啊……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'……总之，\n'
						'不管发生什么事情，都要笑着面对哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'你们要是没有精神的话，\n'
						'对特务支援课抱有期待的人们\n'
						'也会陷入不安的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0103F……说的对啊。\n'
						'谢谢您，老师……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'你们要是没有精神的话，\n'
						'对特务支援课抱有期待的人们\n'
						'也会陷入不安的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'所以无论何时都不要忘记面带笑容。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('CALL', Function((1, 0))),
				]),
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_ROTATE', Char(12), 180, 0),
					Insn('EMOTE', Char(12), 0, 2000, (38, 38, 250, 1)),
					Insn('SLEEP', 1000),
					Insn('CHAR_WATCH', Char(12), Char(0), 500),
					Insn('TEXT_TALK', Char(12), Text(
						'哎呀，罗伊德……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'听说琪雅拒绝\n'
						'住院接受检查？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F是的……\n'
						'对不起，难得您提出建议，\n'
						'却浪费了您的一片心意……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'哎呀呀，没关系啦。\n'
						'不能强迫小孩子做他们不想做的事情嘛。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'以后总会有机会的，\n'
						'再耐心观察一段时间吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F说的也对……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(29), Text(
						'玛布林老师～\n'
						'上课时可以说无关的话吗～？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(12), Char(29), 500),
					Insn('TEXT_TALK', Char(12), Text(
						'哎呀呀，\n'
						'真对不起啊。\n'
						'身为一名老师，竟然会……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0305F喔喔，这……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F真是妨碍到您了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(12), Char(0), 500),
					Insn('TEXT_TALK', Char(12), Text(
						'（就是这样啦……\n'
						'\u3000等以后没课的时候，\n'
						'\u3000再来找我好好谈谈吧。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('CHAR_ROTATE', Char(12), 180, 0),
					Insn('TEXT_TALK', Char(12), Text(
						'那个……\n'
						'刚才讲到哪里了呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'呵呵，上了年纪之后，\n'
						'人就变得健忘了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1514)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 39, Insn('FLAG_GET', 16))), Insn('END')]), [
							Insn('IF', [
								(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
									Insn('TEXT_TALK', Char(12), Text(
										'辛苦了，罗伊德，\n'
										'今天真是谢谢了。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(12), Text(
										'琪雅，\n'
										'如果愿意的话，\n'
										'欢迎再来主日学校哦。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(339), Text(
										'#1109F嗯！知道啦～！{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('FLAG_SET', Flag(3)),
								]),
								(None, [
									Insn('TEXT_TALK', Char(12), Text(
										'琪雅。\n'
										'如果愿意的话，以后\n'
										'也要来主日学校哦。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(12), Text(
										'其他的孩子们\n'
										'肯定也会欢迎你的。{wait}'
									)),
									Insn('TEXT_WAIT'),
								]),
							]),
						]),
						(None, [
							Insn('CALL', Function((0, 46))),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'以我的『法术』，想要唤起\n'
						'琪雅更深层的记忆，\n'
						'恐怕就有点困难了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'圣乌尔斯拉医院\n'
						'『神经科』的医生，\n'
						'或许会对这方面有更加详细的了解。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'去找他们谈一下吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'如果去圣乌尔斯拉医院，\n'
						'或许能了解到有关\n'
						'琪雅记忆的详细情况。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'去找他们谈一下吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('CALL', Function((0, 41))),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'我正在思考从明天起的教学内容。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'嗯……我想，教他们外国的风俗人情\n'
						'也许会很有趣呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'教他们外国的风俗人情\n'
						'也许会很有趣呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'虽然同样位于塞姆利亚大陆，\n'
						'但各个国家之间的文化差异是相当大的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 12))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'呵呵，主日学校今天明明放假，\n'
						'却特意来找我……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'我当讲师已经很久了，\n'
						'每个时代的孩子都很可爱呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'在主日学校放假的时候，\n'
				'我会考虑下次上课\n'
				'的授课内容。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'但在休息日，\n'
				'偶尔也会有孩子\n'
				'来这里玩……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'呵呵，比想像中的要热闹呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'呵呵，有没有好好地享受纪念庆典呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'你们要是有空的话，\n'
				'也去祈祷吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'最近会定期安排主日学校的\n'
						'讲师去大教堂外出差。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'住在阿尔摩利卡村、矿山镇玛因兹\n'
						'还有旧市街的孩子们\n'
						'很难有机会来上课。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'哈缇娜修女最近\n'
						'也在协助我工作，\n'
						'真是帮了大忙啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'哈缇娜修女今天\n'
						'会代替我去旧市街那边出差。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'那边的孩子很少来主日学校，\n'
						'情况很棘手呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(12), 180, 0),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'据说，因为很久以前发生的『大崩坏』……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'这片塞姆利亚大陆\n'
						'遭到了毁灭。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'当时拥有先进技术的\n'
						'古代塞姆利亚文明\n'
						'也随之消亡了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'『大崩坏』，正如其名，\n'
						'它毁灭了塞姆利亚大陆……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'──呼，不知道这些孩子们\n'
						'有没有认真听我讲课。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'我现在也担任\n'
						'着主日学校的\n'
						'教师一职。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'如果愿意的话，有时间的时候\n'
						'就来看看我上课吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'现在的孩子们\n'
						'也都非常可爱。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'如果愿意的话，有时间的时候\n'
						'就来看看我上课吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(12)),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('0x4B', Char(12), -1),
	Insn('0x4B', Char(15), -1),
	Insn('0x4B', Char(16), -1),
	Insn('CHAR_ROTATE', Char(12), 180, 0),
	Insn('CHAR_WATCH', Char(15), Char(12), 0),
	Insn('CHAR_WATCH', Char(16), Char(12), 0),
	Insn('TEXT_TALK', Char(15), Text(
		'我们打算稍后去逛街。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'有很多露天商店都开张了，\n'
		'似乎很有趣的样子，修女也一起去吧～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'哎呀呀，\n'
		'那还真是让人羡慕啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'但我忙着举行弥撒，不能去呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'大家玩得开心点吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'哎，这样啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'唔唔，好遗憾啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(3)),
	Insn('FLAG_SET', Flag(9)),
	Insn('0x4C', Char(12), -1),
	Insn('0x4C', Char(15), -1),
	Insn('0x4C', Char(16), -1),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (150650, 1700, 16780), 0),
	Insn('CAM_ROTATE', 315, 25, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 27500, 0),
	Insn('CHAR_SET_POS', Char(257), (149440, 200, 17150), 90),
	Insn('CHAR_SET_POS', Char(258), (149390, 200, 15890), 45),
	Insn('CHAR_SET_POS', Char(259), (148500, 200, 17170), 90),
	Insn('CHAR_SET_POS', Char(260), (149330, 200, 18150), 135),
	Insn('CHAR_ROTATE', Char(12), 180, 0),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('0x0D'),
	Insn('IF', [
		(Expr([Insn('VAR', 3), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
			Insn('EMOTE', Char(12), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('CHAR_ROTATE', Char(12), 270, 500),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(12), Text(
				'哎呀，是哪位呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F#5P啊，不好意思。\n'
				'看到你们上课的情景，\n'
				'总觉得有些怀念……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0105F（……哎？\n'
				'\u3000这位修女，似乎曾在哪里……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(258), Text(
				'#0105F（……哎？\n'
				'\u3000这位修女，似乎曾在哪里……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_ROTATE', Char(12), 270, 500),
			Insn('EMOTE', Char(12), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1000),
		]),
	]),
	Insn('TEXT_TALK', Char(12), Text(
		'……啊……\n'
		'你难道是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'──罗伊德。\n'
		'是罗伊德丄班宁斯吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F#5P哎……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F什么啊，罗伊德，你们认识吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0002F#5P难、难道是……\n'
		'玛布林老师！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'真是好久不见了，罗伊德。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(12), Char(258), 500),
	Insn('TEXT_TALK', Char(12), Text(
		'还有……\n'
		'那边的是艾莉吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'呵呵……你们两个\n'
		'都长大成人了呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0109F果然……！\n'
		'好久不见了，老师。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(258), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F#11P那个……莫非\n'
		'艾莉你也认识玛布林老师？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(258), Char(257), 500),
	Insn('TEXT_TALK', Char(258), Text(
		'#0102F嗯，我在主日学校上课时，\n'
		'也是受教于老师的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(259), Char(258), 500),
	Insn('TEXT_TALK', Char(259), Text(
		'#0205F#5P罗伊德前辈与艾莉前辈\n'
		'的年龄不是很接近吗……{wait}'
		'{page}'
		'而且同样受教于修女，\n'
		'但当时却互不相识吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'克洛斯贝尔市是很广阔的，\n'
		'不同街区的孩子，来主日学校\n'
		'上课的日程也不一样。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'罗伊德与艾莉来学校\n'
		'的日子就是不同的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F原来～如此。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0104F……感觉有点奇怪呢。{wait}'
		'{page}'
		'#0102F要不是上课时间不同的话，\n'
		'当年或许还能成为童年玩伴呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0009F#11P哈哈，说得也是啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(257), 90, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(258), 45, 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(259), 90, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#0002F#5P说起来，玛布林老师您\n'
		'居然还记得我们啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'呵呵……\n'
		'只要是自己教过的学生，\n'
		'我一个都不会忘记的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'而且你们两个\n'
		'又都是非常有个性的孩子。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0205F#5P有个性……吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'没错。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'罗伊德是个喜欢粘着姐姐，\n'
		'很爱撒娇的孩子……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'艾莉小时候则非常不像个小孩子，\n'
		'该说是对男女之间的事很早熟吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0011F#5P等、等一下！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0112F老师……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0304F哈哈～\n'
		'听别人过去的事情真是有趣啊。{wait}'
		'{page}'
		'#0309F那么，具体来说，究竟发生过怎样的小故事呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'对了，比如──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0012F#5P老师，请您放过我吧……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0113F真是的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'呵呵，开玩笑啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0206F#5P……真遗憾。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'……罗伊德、艾莉，\n'
		'能与你们再会，\n'
		'我感到很高兴。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'如果愿意的话，随时\n'
		'欢迎你们来找我哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0002F#5P……好的！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (149440, 200, 17150), 90),
	Insn('FLAG_SET', Flag(1123)),
	Insn('IF', [
		(Expr([Insn('VAR', 3), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
			Insn('FLAG_SET', Flag(4)),
		]),
		(None, []),
	]),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][14] = [
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
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'……那位夫人，\n'
				'好像经常在教堂露面。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虔诚是非常重要的，\n'
				'我也不能忘记那份诚心。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀……我还是第一次看见\n'
				'警备队的人来到大教堂呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'该死的黑手党……\n'
				'竟然在那一带开战，\n'
				'真是无法无天……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'女神啊……保护我们这些热心做生意的人\n'
				'免遭那些凶恶毒牙的伤害吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我想把从玛因兹\n'
				'订购的七耀石\n'
				'作为下次交易的重头戏。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然贩卖新商品\n'
				'总让我感觉有点不安……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过没什么，空之女神肯定\n'
				'会对我展露笑容的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'空之女神啊……\n'
				'明年的纪念庆典\n'
				'也请多保佑我……！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我在今年的纪念庆典\n'
				'获得了很大的收益呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'因为游客的数量\n'
				'比往年多了很多。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'向空之女神\n'
				'虔诚地祈祷，\n'
				'果然没有白费啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天是庆典的最后一天了……\n'
				'很多客人都去了米修拉姆，\n'
				'现在正是做生意的良机。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'空之女神啊……\n'
				'请给我带来商机！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'空之女神啊……\n'
				'今年的业绩真是超好啊，\n'
				'商品卖得飞快。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'啊啊，真是感激不尽……！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'空之女神啊……\n'
				'昨天的销售额\n'
				'也非常可观。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'啊啊，实在是太感谢了……！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'虽然工作很忙……\n'
						'但我也不打算错过弥撒。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'因为，全靠平时坚持\n'
						'向空之女神献上祈祷，\n'
						'才能有今天的我。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'所以，像这样的活动，\n'
						'我一次都不会错过，\n'
						'这样才能表达我的感激之情。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我现在的成就全都是空之女神所赐……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'所以必须要一次不漏的参加这样的活动，\n'
						'这也是理所当然的吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'下个月终于要到创立纪念庆典了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'对我们贸易商来说，\n'
						'这是赚钱的大好时机。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'好了，为了今年也能生意兴隆，\n'
						'必须要向空之女神献上祈祷……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'空之女神啊……\n'
						'在这次的创立纪念庆典期间\n'
						'也请保佑我……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'嗯嗯，有孩子们在的话就很热闹呢，真好啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然我以前最讨厌小孩子了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但自从在这里坚持祈祷，事业大获成功之后，\n'
						'便感觉自己的心胸也变得宽阔起来了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'通过向空之女神祈祷，\n'
						'我的事业获得了成功，心胸也变得宽阔起来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'必须要感谢这个地方呢。\n'
						'哈哈哈……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我是一个贸易商……\n'
						'自从在这里祈祷之后，\n'
						'生意就取得了很大的成功。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'自那之后，我就经常\n'
						'来这里祈祷了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'啊啊，空之女神啊……\n'
						'请保佑我下次生意\n'
						'也一帆风顺……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 6))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(14), Text(
						'#0502F啊，支援课的各位……{wait}'
						'{page}'
						'#0504F我刚才已经向大主教\n'
						'报告了有关那处\n'
						'遗迹的情况。{wait}'
						'{page}'
						'#0508F如果调查工作可以因此\n'
						'而取得进展就好了……{wait}'
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
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
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
				(Expr([Insn('EXEC', Insn('QUEST_GET', 39, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'哼，还以为\n'
						'上了刚才的课，\n'
						'就不用再上普通的课了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'修女对这种事情\n'
						'真是从不敷衍啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呼……\n'
						'我完全忘了\n'
						'主日学校今天有课。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'啊啊～真想去外面玩啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('CHAR_SET_FRAME', Char(254), 0),
			Insn('TEXT_END', Char(254)),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_START', Char(254)),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 12))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'啧……\n'
						'难得我想带老师去\n'
						'参观城市的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'因为总是跟哈米尔在一起，\n'
						'都没有新鲜感了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('TEXT_END', Char(254)),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
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
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 18))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'哼，哈米尔那家伙，\n'
						'只不过是学习成绩比我稍微强一点，\n'
						'就那么得意忘形……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('CHAR_SET_FRAME', Char(254), 0),
			Insn('TEXT_END', Char(254)),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), []),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
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
				(Expr([Insn('EXEC', Insn('QUEST_GET', 39, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'真是的～泰米尔这家伙，\n'
						'明明刚才都还\n'
						'那么得意忘形。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'节制很重要，要节制。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CHAR_SET_FRAME', Char(254), 2),
					Insn('TEXT_TALK', Char(254), Text(
						'真是的～泰米尔这家伙\n'
						'直到刚才不是还\n'
						'一直都在玩吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'修女不是\n'
						'一直都教导我们说，\n'
						'节制是很重要的嘛。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('CHAR_SET_FRAME', Char(254), 0),
			Insn('TEXT_END', Char(254)),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_START', Char(254)),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 12))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'虽然很想和经常照顾我们的玛布林老师\n'
						'一起去逛逛露天店……\n'
						'但老师太忙，那就没办法了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'本来还想请\n'
						'老师吃冰淇淋什么的呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('TEXT_END', Char(254)),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_START', Char(254)),
					Insn('CALL', Function((0, 18))),
					Insn('TEXT_END', Char(254)),
				]),
				(None, [
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
					Insn('TEXT_TALK', Char(254), Text(
						'我的双胞胎兄弟泰米尔，\n'
						'学习完全不行呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'只是比较擅长运动的话，\n'
						'在主日学校可没资格骄傲。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_SET_FRAME', Char(254), 0),
					Insn('TEXT_END', Char(254)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), []),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('EXPR_CHAR_ATTR', Char(16), 5, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(15), 5, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('SET'), Insn('END')])),
	Insn('TEXT_START', Char(15)),
	Insn('CHAR_FLAG1_UNSET', Char(15), 16),
	Insn('CHAR_WATCH', Char(15), Char(16), 0),
	Insn('EXPR_CHAR_ATTR', Char(15), 4, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(15), 4, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(15), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(15), 5, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
		(Expr([Insn('CHAR_ATTR', Char(15), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(15), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('CHAR_ATTR', Char(15), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(15), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
		]),
		(None, [
			Insn('EXPR_CHAR_ATTR', Char(15), 8, Expr([Insn('CHAR_ATTR', Char(15), 5), Insn('SET'), Insn('END')])),
		]),
	]),
	Insn('EXPR_CHAR_ATTR', Char(15), 4, Expr([Insn('CHAR_ATTR', Char(16), 5), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(16), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(15), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(15), 16),
	Insn('TEXT_TALK', Char(15), Text(
		'我说，哈米尔。\n'
		'你听明白玛布林老师讲的东西了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EXPR_CHAR_ATTR', Char(15), 5, Expr([Insn('CHAR_ATTR', Char(16), 4), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(16), 5, Expr([Insn('CHAR_ATTR', Char(16), 4), Insn('SET'), Insn('END')])),
	Insn('TEXT_START', Char(16)),
	Insn('CHAR_FLAG1_UNSET', Char(16), 16),
	Insn('CHAR_WATCH', Char(16), Char(15), 0),
	Insn('EXPR_CHAR_ATTR', Char(16), 4, Expr([Insn('CHAR_ATTR', Char(16), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(16), 4, Expr([Insn('CHAR_ATTR', Char(16), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(16), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(16), 5, Expr([Insn('CHAR_ATTR', Char(16), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('CHAR_ATTR', Char(16), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(16), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(16), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(16), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
		(Expr([Insn('CHAR_ATTR', Char(16), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(16), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('CHAR_ATTR', Char(16), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(16), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
		]),
		(None, [
			Insn('EXPR_CHAR_ATTR', Char(16), 8, Expr([Insn('CHAR_ATTR', Char(16), 5), Insn('SET'), Insn('END')])),
		]),
	]),
	Insn('EXPR_CHAR_ATTR', Char(16), 4, Expr([Insn('CHAR_ATTR', Char(15), 5), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(15), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(16), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(16), 16),
	Insn('TEXT_TALK', Char(16), Text(
		'泰米尔，你有没有在认真听啊？\n'
		'并不是那么难的内容啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'是、是吗……？\n'
		'嗯，那等一下把笔记借给我看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('CHAR_SET_FRAME', Char(16), 0),
	Insn('FLAG_SET', Flag(9)),
	Insn('RETURN'),
]

data['code'][19] = [
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
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 39, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'刚才的课……\n'
						'虽然有点难，\n'
						'但是很开心啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那个……\n'
						'谢谢了，大哥哥。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'能够与龙和安里\n'
						'一起学习，\n'
						'真开心啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'今天的课会教些什么呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'大崩坏……\n'
				'原来还发生过那样的事情啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'好可怕啊……（发抖）……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][20] = [
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
		(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'塞姆利亚文明……\n'
				'似乎是我爸爸\n'
				'很喜欢的话题呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……说起来，龙与安里\n'
				'今天翘课了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'明明已经告诉过他们\n'
				'主日学校今天有课了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(5)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'……算了，不管那两个家伙了，\n'
				'要抓紧时间学习啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][21] = [
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
		(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('OR'), Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 2))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((1, 5))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'如果导力器就像这样\n'
				'继续发展下去的话，\n'
				'生活大概会变得更加便捷吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'比如说，待在家里\n'
				'就能购物之类的……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……啊！要是变成那样的话，\n'
				'帮家里买东西赚到的零钱就没有了！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][22] = [
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
		(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('OR'), Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 2))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((1, 6))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'当上游击士的话，\n'
				'就可以从爱普斯泰恩财团那里\n'
				'得到战术导力器了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'真好啊～\n'
				'有朝一日，我也想使用\n'
				'那些华丽的魔法。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][23] = [
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
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 39, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我对警察并不是\n'
				'很了解，\n'
				'所以在这堂课上真是学到了不少。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'以后还请再多教我们一些东西哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'啊，你是刚才的……\n'
				'是叫琪雅吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你也来\n'
				'上课了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(339), Text(
				'#1106F嗯～？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(17)), Insn('NOT'), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(27), 0),
			Insn('CHAR_SET_FRAME', Char(28), 0),
			Insn('TEXT_TALK', Char(27), Text(
				'呼啊～……快睡着了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EXPR_CHAR_ATTR', Char(27), 5, Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(28), 5, Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('SET'), Insn('END')])),
			Insn('TEXT_START', Char(28)),
			Insn('CHAR_FLAG1_UNSET', Char(28), 16),
			Insn('CHAR_WATCH', Char(28), Char(27), 0),
			Insn('EXPR_CHAR_ATTR', Char(28), 4, Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(28), 4, Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(28), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(28), 5, Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
			Insn('IF', [
				(Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
				(Expr([Insn('CHAR_ATTR', Char(28), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
					Insn('EXPR_CHAR_ATTR', Char(28), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('CHAR_ATTR', Char(28), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
					Insn('EXPR_CHAR_ATTR', Char(28), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, [
					Insn('EXPR_CHAR_ATTR', Char(28), 8, Expr([Insn('CHAR_ATTR', Char(28), 5), Insn('SET'), Insn('END')])),
				]),
			]),
			Insn('EXPR_CHAR_ATTR', Char(28), 4, Expr([Insn('CHAR_ATTR', Char(27), 5), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(27), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(28), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('CHAR_FLAG1_SET', Char(28), 16),
			Insn('TEXT_TALK', Char(28), Text(
				'不能睡哦！得好好听\n'
				'老师说话才可以哦──！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(27), Text(
				'但很无聊啊……\n'
				'嗯……呼……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(28), Text(
				'呣～……我要跟姐姐说\n'
				'你偷睡觉哦～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#00000F（哈哈，好可爱的孩子，是双胞胎吗？\n'
				'\u3000总觉得跟某人长得有点像……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(17)),
		]),
		(None, [
			Insn('CHAR_SET_FRAME', Char(27), 0),
			Insn('CHAR_SET_FRAME', Char(28), 0),
			Insn('TEXT_TALK', Char(27), Text(
				'……呼啊～……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EXPR_CHAR_ATTR', Char(27), 5, Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(28), 5, Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('SET'), Insn('END')])),
			Insn('TEXT_START', Char(28)),
			Insn('CHAR_FLAG1_UNSET', Char(28), 16),
			Insn('CHAR_WATCH', Char(28), Char(27), 0),
			Insn('EXPR_CHAR_ATTR', Char(28), 4, Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(28), 4, Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(28), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(28), 5, Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
			Insn('IF', [
				(Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
				(Expr([Insn('CHAR_ATTR', Char(28), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
					Insn('EXPR_CHAR_ATTR', Char(28), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('CHAR_ATTR', Char(28), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
					Insn('EXPR_CHAR_ATTR', Char(28), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, [
					Insn('EXPR_CHAR_ATTR', Char(28), 8, Expr([Insn('CHAR_ATTR', Char(28), 5), Insn('SET'), Insn('END')])),
				]),
			]),
			Insn('EXPR_CHAR_ATTR', Char(28), 4, Expr([Insn('CHAR_ATTR', Char(27), 5), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(27), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(28), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('CHAR_FLAG1_SET', Char(28), 16),
			Insn('TEXT_TALK', Char(28), Text(
				'快起来啦──！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(27), 0),
	Insn('CHAR_SET_FRAME', Char(28), 0),
	Insn('FLAG_SET', Flag(17)),
	Insn('RETURN'),
]

data['code'][25] = [
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
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(15)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(27), Text(
						'网、网络……？（抄抄写写）{wait}'
						'{page}'
						'虽然不是很懂，但是在说导力器的话，\n'
						'姐姐曾经教过我们喔。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(15)),
				]),
				(None, [
					Insn('CHAR_SET_FRAME', Char(27), 0),
					Insn('TEXT_TALK', Char(27), Text(
						'网络……导力……\n'
						'（抄抄写写）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 39, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(18)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(27), Text(
								'感觉有点难，\n'
								'不过似乎比平常更集中呢。{wait}'
								'{page}'
								'……多谢啦。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(18)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(27), Text(
								'似乎比平常更集中呢\n'
								'……多谢啦。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(15)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(27), Text(
						'被姐姐念说\n'
						'要好好听老师上课……{wait}'
						'{page}'
						'所以只好在快睡着的时候，\n'
						'用力捏自己的脸颊……痛痛痛。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(15)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(27), Text(
						'用力捏自己的脸颊\n'
						'虽然能赶跑睡意……痛痛痛。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CALL', Function((0, 24))),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][26] = [
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
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(16)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(28), Text(
						'最近肯恩变得会写\n'
						'很多很多笔记了哦──！{wait}'
						'{page}'
						'娜娜也不会输的──！\n'
						'（抄抄抄写写写）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(16)),
				]),
				(None, [
					Insn('CHAR_SET_FRAME', Char(28), 0),
					Insn('TEXT_TALK', Char(28), Text(
						'爱普斯泰恩博士……（抄抄写写）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 39, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(19)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(28), Text(
								'有很多不同的警察呢，\n'
								'娜娜之前都不知道呢──！{wait}'
								'{page}'
								'不过不过，特务支援课我知道哦！\n'
								'加油喔、罗伊德老师──！{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(19)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(28), Text(
								'特务支援课我知道哦！\n'
								'加油喔、罗伊德老师──！{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(16)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(28), Text(
						'肯恩他呀，老师在说话的时候，\n'
						'自己用力拉自己的脸颊呢──{wait}'
						'{page}'
						'耶嘿嘿，好怪的脸呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(16)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(28), Text(
						'肯恩，好怪的脸呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CALL', Function((0, 24))),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][27] = [
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
		(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('OR'), Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 2))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((1, 7))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'我记得，爱普斯泰恩财团好像就是以\n'
				'Ｃ丄爱普斯泰恩博士的\n'
				'庞大遗产为基础发展起来的……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'爱普斯泰恩博士到底\n'
				'是个怎样的人呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][28] = [
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
		(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('OR'), Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 2))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((1, 9))),
		]),
		(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'太简单了，简直让人发笑。\n'
				'这种程度的知识是常识啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……啊，居然在上课时随便\n'
				'和别人搭话，真没礼貌！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(8)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'真是的，到那边去！\n'
				'我要学习啦！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][29] = [
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
	Insn('TEXT_TALK', Char(254), Text(
		'以现在的技术水准来说，\n'
		'不是能够轻松避免\n'
		'那种严重的灾难吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][30] = [
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
	Insn('TEXT_TALK', Char(254), Text(
		'……啊！\n'
		'别看我的笔记啦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][31] = [
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
		(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('OR'), Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 2))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((1, 10))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'呼……只要一学习就想睡觉。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……哇，修女在看着呢，\n'
				'必须得打起精神。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][32] = [
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
		(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('OR'), Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 2))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((1, 8))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'为了将来，\n'
				'必须要好好学习，\n'
				'妈妈是这样说的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……大哥哥，你们以前\n'
				'有没有好好学习呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][33] = [
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
		(Expr([Insn('FLAG', Flag(1135)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(10)), Insn('END')]), [
					Insn('TEXT_TALK', Char(31), Text(
						'#3600F我一般都会注意时间，\n'
						'尽量来参加的……\n'
						'但经常会由于工作原因而无法赶过来。{wait}'
						'{page}'
						'#3603F老是给妻子增添负担。\n'
						'……我也真是没用呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(31), Text(
						'#3600F参加弥撒是\n'
						'妻子的习惯。\n'
						'她每周都会来，从未缺席过。{wait}'
						'{page}'
						'#3603F我一般都会注意时间，\n'
						'尽量来参加的……\n'
						'但经常会由于工作原因而无法赶过来。{wait}'
						'{page}'
						'#3600F哈哈，总是给妻子\n'
						'增添负担。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F（……………………？\n'
						'\u3000难道有什么必须\n'
						'\u3000来祈祷的理由吗……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(10)),
				]),
			]),
		]),
		(None, [
			Insn('TEXT_TALK', Char(31), Text(
				'#3605F啊，各位……{wait}'
				'{page}'
				'#3609F哈哈哈，竟会在这种地方相遇，还真巧啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F对了，今天是举行弥撒的日子啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F哈罗德先生也是来祈祷的吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(31), Text(
				'#3600F嗯，这是妻子的习惯。{wait}'
				'{page}'
				'#3609F虽然我经常缺席……\n'
				'但也会尽量抽时间\n'
				'陪妻子过来。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0309F还是一如既往地关心家人呢～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F在百忙之中还抽空前来，真是十分虔诚呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(31), Text(
				'#3609F哈哈，并不是那样的……{wait}'
				'{page}'
				'#3608F………………………………{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(0), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('EMOTE', Char(1), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('EMOTE', Char(2), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('EMOTE', Char(3), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(31), Text(
				'#3603F……不，没什么。{wait}'
				'{page}'
				'#3600F那个，其实我并没有\n'
				'那么深厚的信仰。{wait}'
				'{page}'
				'只是听说祈祷\n'
				'对保佑生意兴隆很有效。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0305F哎呀，是听那边那位说的吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(31), Text(
				'#3609F啊哈哈哈哈……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1135)),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][34] = [
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
	Insn('CHAR_SET_FRAME', Char(32), 0),
	Insn('TEXT_TALK', Char(32), Text(
		'#3700F祭司大人，那么今天\n'
		'也拜托您了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][35] = [
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
		(Expr([Insn('FLAG', Flag(11)), Insn('END')]), [
			Insn('TEXT_TALK', Char(33), Text(
				'#3809F祈祷～祈祷……{wait}'
				'{page}'
				'跟爸爸妈妈\n'
				'在一起好开心啊～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(33), Text(
				'#3800F今天是我和妈妈\n'
				'来祈祷的日子～{wait}'
				'{page}'
				'那个，结果爸爸\n'
				'也赶过来了！{wait}'
				'{page}'
				'#3809F爸爸总是很忙，\n'
				'这次也是匆匆忙忙的跑过来的～！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(11)),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][36] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(12)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#0105F啊……是赛西儿小姐的母亲。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀呀，大家聚在一起，\n'
				'莫非是来祈祷的吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(254), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('CHAR_WATCH', Char(254), Char(257), 500),
			Insn('TEXT_TALK', Char(254), Text(
				'罗伊德……发生什么事情了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(0), 0, 2000, (38, 38, 250, 1)),
			Insn('EMOTE', Char(1), 0, 2000, (38, 38, 250, 1)),
			Insn('EMOTE', Char(2), 0, 2000, (38, 38, 250, 1)),
			Insn('EMOTE', Char(3), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F哎……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……没什么，我只是随便问问。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，你真是\n'
				'越来越像盖了，\n'
				'在黄昏时很容易看错呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0011F啊，哈哈……\n'
				'再怎么说，也是有血缘关系的兄弟嘛。\n'
				'（……怎么，原来阿姨是来为大哥祈祷的吗？）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'要是方便的话，\n'
				'罗伊德也一起来祈祷吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'因为盖也……沉睡\n'
				'在这里呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'罗伊德真是\n'
				'越来越像盖了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵……你一定能够成为不输给\n'
				'盖的优秀搜查官。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'阿姨我会替你加油的。\n'
				'可不能输哦，罗伊德。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][37] = [
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
		(Expr([Insn('EXEC', Insn('QUEST_GET', 39, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'大哥哥讲的课\n'
				'好有趣啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我还会再去找赛特\n'
				'一起玩的～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'哼，老实说，\n'
				'学习真是让人提不起劲来～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过，修女的课其实挺有意思的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][38] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(14)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我是来向女神祈祷旅途平安的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'要是不小心受伤的话，\n'
				'难得的旅行也就泡汤了。\n'
				'必须得十分小心才行啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(14)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'要是不小心受伤，\n'
				'浪费了旅行的时光，\n'
				'可就太不划算了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'以防万一，\n'
				'再祈祷一次好了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][39] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (151810, 1500, 11060), 0),
	Insn('CAM_ROTATE', 315, 21, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 31350, 0),
	Insn('CHAR_SET_POS', Char(257), (148350, 0, 3500), 0),
	Insn('CHAR_SET_POS', Char(258), (146900, 0, 3750), 0),
	Insn('CHAR_SET_POS', Char(259), (148350, 0, 1920), 0),
	Insn('CHAR_SET_POS', Char(260), (146900, 0, 2250), 0),
	Insn('0x4B', Char(12), -1),
	Insn('CAM_OFFSET', (151810, 1500, 13060), 5000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(12), Text(
		'──据说，很久以前发生的『大崩坏』……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'这片塞姆利亚大陆\n'
		'遭到了毁灭。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'当时拥有先进技术的\n'
		'古代塞姆利亚文明\n'
		'也随之消亡了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (147550, 1500, 2910), 0),
	Insn('CAM_ROTATE', 315, 28, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 28000, 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F……看样子，主日学校正在上课呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1123)), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F哈哈，真让人怀念啊。\n'
				'而且孩子们当中也有我们认识的呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F哈哈，真让人怀念啊。\n'
				'而且孩子们当中也有我们认识的呢……{wait}'
				'{page}'
				'#0005F（……嗯？\n'
				'\u3000正在授课的修女……\n'
				'\u3000莫非是……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_POS', Char(0), (147550, 0, 2900), 0),
	Insn('0x4C', Char(12), -1),
	Insn('FLAG_SET', Flag(1076)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][40] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (151810, 1500, 11060), 0),
	Insn('CAM_ROTATE', 315, 21, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 31350, 0),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1076)), Insn('NOT'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(4), 128),
					Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
					Insn('CHAR_SET_POS', Char(265), (149460, 0, 1750), 0),
				]),
				(None, []),
			]),
			Insn('CHAR_SET_POS', Char(257), (148350, 0, 3500), 0),
			Insn('CHAR_SET_POS', Char(258), (146900, 0, 3750), 0),
			Insn('CHAR_SET_POS', Char(259), (148350, 0, 1920), 0),
			Insn('CHAR_SET_POS', Char(260), (146900, 0, 2250), 0),
		]),
		(None, []),
	]),
	Insn('0x4B', Char(12), -1),
	Insn('CAM_OFFSET', (151810, 1500, 13060), 5000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(12), Text(
		'──半世纪前，\n'
		'Ｃ丄爱普斯泰恩博士\n'
		'发起了『导力革命』……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'虽然一开始并不被人们所接受，\n'
		'但在如今，我们周围\n'
		'已经有了很多便利的『导力器』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'例如最近出现的导力车，\n'
		'便利的产品接二连三地被发明了出来……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1076)), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 39, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CROSSFADE', 500),
			Insn('CAM_OFFSET', (147550, 1500, 2910), 0),
			Insn('CAM_ROTATE', 315, 28, 0, 0),
			Insn('0x6E', 300, 0),
			Insn('CAM_DISTANCE', 28000, 0),
			Insn('0x0D'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F……主日学校\n'
				'好像正在上课呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F哈哈，真让人怀念啊。\n'
				'而且孩子们当中也有我们认识的呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_POS', Char(0), (147550, 0, 2900), 0),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(4), 128),
			Insn('CHAR_FLAG2_SET', Char(4), 32768),
		]),
		(None, []),
	]),
	Insn('0x4C', Char(12), -1),
	Insn('FLAG_SET', Flag(1077)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][41] = [
	Insn('EVENT_BEGIN', 2),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('EVENT_BEGIN', 0),
	Insn('LOAD_CHCP', 'apl/ch50381', 30),
	Insn('EFF_LOAD', ResId(0), 'event\\ev400_00.eff'),
	Insn('EFF_LOAD', ResId(1), 'event\\ev401_00.eff'),
	Insn('SOUND_LOAD', 840),
	Insn('0x4B', Char(12), -1),
	Insn('CHAR_SET_POS', Char(12), (148920, 0, 13890), 90),
	Insn('CHAR_SET_POS', Char(257), (150330, 0, 14130), 270),
	Insn('CHAR_SET_POS', Char(339), (151460, 0, 13520), 270),
	Insn('CHAR_SET_POS', Char(239), (150640, 0, 12780), 315),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (150000, 1100, 14000), 0),
	Insn('CAM_ROTATE', 315, 20, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 24000, 0),
	Insn('0x0D'),
	Insn('EMOTE', Char(12), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'#13600491V#5P哎呀……\n'
				'罗伊德，还有艾莉。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#13600492V#0002F#11P下午好，玛布林老师。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#13600493V#0102F#6P在您百忙之中还来打扰，真不好意思。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(12), Text(
				'#13600494V#5P哎呀……\n'
				'这不是罗伊德嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#13600495V#0002F#11P下午好，玛布林老师。{wait}'
				'{page}'
				'#13600496V在您百忙之中还来打扰，真不好意思。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600497V#5P呵呵，没关系啦，\n'
		'现在刚好是休息时间。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1123)), Insn('NOT'), Insn('FLAG', Flag(1356)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EMOTE', Char(12), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(12), Text(
				'#13600498V#5P说起来，你们似乎\n'
				'是同一个部门的同事吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#13600499V#5P呵呵，看到你们两个在一起，\n'
				'总觉得感慨万千啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#13600500V#0012F#11P哈哈……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#13600501V#0112F#6P是、是那样的吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#13600502V#5P呵呵……\n'
				'那么，你们来此有什么事呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#13600503V#5P今天是来做礼拜的吗？\n'
				'还是来扫墓的呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(12), Text(
				'#13600504V#5P你们是来做礼拜的吗，\n'
				'还是来扫墓的呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600505V#0008F#11P不，实际上……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600506V#1100F#12P喂喂，罗伊德。{wait}'
		'{page}'
		'#13600507V这个人是修女吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(12), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600508V#5P哎呀，这个孩子是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600509V#0003F#11P那个，实际上……{wait}'
		'{page}'
		'#13600510V#0001F我们想找您谈一谈\n'
		'关于这个孩子的一些事情。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('CAM_DISTANCE', 23000, 2000),
	Insn('0x6F', b'y'),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (151000, 1100, 12500), 0),
	Insn('CAM_ROTATE', 315, 20, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 24000, 0),
	Insn('CHAR_SET_POS', Char(12), (151000, 0, 13800), 180),
	Insn('CHAR_SET_POS', Char(339), (151000, 0, 12000), 0),
	Insn('CHAR_SET_POS', Char(257), (151500, 0, 10800), 0),
	Insn('CHAR_SET_POS', Char(239), (150500, 0, 10800), 0),
	Insn('SLEEP', 500),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600511V#11P……是吗，原来发生了那种事啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600512V#11P啊，女神啊……\n'
		'请赐予迷途的羔羊光明与幸福。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600513V#11P感谢您指引\n'
		'他们相遇……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600514V#0000F#6P玛布林老师……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600515V#0104F#6P……确实，能与她相遇，\n'
				'说不定都是因为女神#4R爱德斯#的指引呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600516V#0204F#6P……确实，能与她相遇，\n'
				'说不定都是因为某种指引呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600517V#0304F#6P……确实，能与她相遇，\n'
				'说不定都是因为女神#4R爱德斯#的指引啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600518V#1105F#6P咦咦……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600519V#11P总之……\n'
		'你们是来商量关于这个\n'
		'孩子失去记忆的事情吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600520V#11P听你所言，她除了名字之外\n'
		'什么都不记得……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600521V#0006F#6P嗯……是这样的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600522V#1106F#6P那个，虽然琪雅\n'
		'试着努力想过了。{wait}'
		'{page}'
		'#13600523V#1108F但好像完全想不起来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600524V#11P是吗……真是个好孩子哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(12), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(12)),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600525V#11P……教会中的确传承着\n'
		'关于心灵与精神\n'
		'领域的知识和技术。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600526V#11P而且……\n'
		'也有失忆症状的治疗方法。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(239), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600527V#0002F#6P那、那么……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600528V#0100F#6P您有办法找回\n'
				'这个孩子的记忆吗……！？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600529V#0202F#6P您有办法恢复\n'
				'这个孩子的记忆吗……！？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600530V#0300F#6P也就是说，这个孩子的记忆\n'
				'可以找回来吗！？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600531V#11P虽然不能断言，\n'
		'但应该值得一试。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600532V#11P时间并不充裕呢……\n'
		'立即来试试看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(239), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600533V#0005F#6P莫非……\n'
		'由老师您亲自帮忙吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600534V#11P嗯，我也算是\n'
		'学过一些东西吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600535V#11P就是在教会中传承的，\n'
		'有关心灵与精神的『法术』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600536V#0001F#6P『法术』……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600537V#0101F#6P在教会圣职者中传承的，\n'
				'与祈祷和圣礼相关的技术……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600538V#0201F#6P那是不依靠导力器，\n'
				'仅凭祈祷所引发的魔法……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600539V#0301F#6P传闻说，只有教会人员才能\n'
				'使用的不可思议的祈祷术吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600540V#11P嗯，本来有个组织是专门\n'
		'研究那些技术的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600541V#11P但很不巧，\n'
		'那方面的专家很少来克洛斯贝尔。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('EMOTE', Char(239), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600542V#0005F#6P专家吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600543V#11P……虽然不便公开提起，\n'
		'但教会中也是有很多内幕的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600544V#11P那个组织隶属于\n'
		'被称为『封圣省』的机关……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600545V#11P管理这座大教堂的\n'
		'艾拉尔达大主教似乎非常讨厌\n'
		'那个组织所进行的活动。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600546V#11P因此，那些专家很少有机会\n'
		'来克洛斯贝尔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600547V#0006F#6P感、感觉有很多\n'
		'复杂的背景呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600548V#0103F#6P隶属于『封圣省』的组织……\n'
				'也就是『星杯骑士团』吧。{wait}'
				'{page}'
				'#13600549V#0108F虽然听说过艾拉尔达大主教\n'
				'是偏向『典礼省』的教会高层人士，\n'
				'但没想到竟然还有那种内情啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#13600550V#11P呵呵，真不愧是艾莉，\n'
				'对这类情况很了解呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600551V#0201F#6P也就是说，这是教会\n'
				'内部的权利斗争吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#13600552V#11P嗯，真让人惭愧……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600553V#0301F#6P也就是说，是教会\n'
				'内部的权利斗争吗。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#13600554V#11P嗯，真让人惭愧……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600555V#11P不过，我所使用的法术\n'
		'与他们使用的并没有什么两样。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600556V#11P我想还是值得一试的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600557V#0000F#6P知道了，\n'
		'那就拜托您了。{wait}'
		'{page}'
		'#13600558V#0005F那个，是不是换个地方\n'
		'比较好呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600559V#11P不，在这里就可以了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600560V#11P你是叫琪雅吧，\n'
		'可以到我这里来吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600561V#1109F#6P好呀～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (151110, 1100, 12960), 1000),
	Insn('FORK', 339, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00 \x03\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(339), 1),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600562V#11P请闭上眼睛，\n'
		'慢慢深呼吸。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600563V#1110F#5P嗯！{wait}'
		'{page}'
		'#13600564V#1103F#40W呼……哈……{wait}'
		'{page}'
		'#13600565V#40W呼……哈……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600566V#11P嗯，这样就行了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600567V#11P……那么……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 2000),
	Insn('CROSSFADE', 500),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('CHAR_FLAG1_SET', Char(12), 2),
	Insn('CHAR_FLAG1_SET', Char(12), 16),
	Insn('CHAR_SET_CHCP', Char(12), 30),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('SOUND_PLAY', 882, 0, 0, 100),
	Insn('0x0D'),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'0\x01\x00'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600568V#11P#40W──以空之女神#8R爱德斯#之名，\n'
		'祝圣之七耀，于此处显现。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EFF_PLAY', (ResId(0), 0), Char(12), 64, 200, 0, 900, 0, -450, -1, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('SOUND_PLAY', 893, 0, 0, 100),
	Insn('SOUND_PLAY', 840, 0, 2, 100),
	Insn('CAM_DISTANCE', 23000, 30000),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600569V#0005F#6P（啊……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600570V#0105F#6P（这就是法术……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600571V#0201F#6P（这就是法术吗……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600572V#0301F#6P（这就是法术啊……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600573V#11P#40W空之金耀，识之银耀──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600574V#11P#40W以此融合为契，\n'
		'请为其明示\n'
		'缺失碎片之所在吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('EFF_PLAY', (ResId(1), 1), Char(339), 64, 0, 0, 800, 0, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('SOUND_PLAY', 228, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('FORK', 339, 2, [
		Insn('0xA6', Char(254), 0, 50, 300, 2000),
	]),
	Insn('SLEEP', 800),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600575V#1105F#5P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600576V#0013F#6P琪雅……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(12), 2),
	Insn('CHAR_FLAG1_UNSET', Char(12), 16),
	Insn('CHAR_SET_CHCP', Char(12), 3),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600577V#11P没关系，不必担心。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600578V#11P……感觉如何，琪雅。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600579V#11P想起什么了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600580V#1103F#5P#40W嗯……{wait}'
		'{page}'
		'#13600581V#40W………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(339), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(339)),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600582V#1108F#5P……感觉，\n'
		'脑袋里面浮现出了\n'
		'一个又黑暗又广阔的地方。{wait}'
		'{page}'
		'#13600583V#1112F上面有朦胧的光线洒下来，\n'
		'虽然很漂亮，但感觉又有点恐怖。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600584V#0005F#6P又黑暗又广阔的地方……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600585V#0108F#6P那是哪里呢……？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600586V#0208F#6P指的是哪里呢……？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600587V#0301F#6P到底是哪里啊……？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600588V#11P除了那个场景之外，\n'
		'还想起了别的什么吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600589V#11P比如家人是谁，\n'
		'住在什么地方之类的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600590V#1106F#5P唔……那些完全没想起来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600591V#11P这样啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600592V#11P…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('BGM_STOP', 4000),
	Insn('FORK_FUNC', Char(36), 1, Function((0, 42))),
	Insn('EFF_STOP', (ResId(1), 2)),
	Insn('SLEEP', 3000),
	Insn('EMOTE', Char(12), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('FORK_QUIT', Char(36), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600593V#0001F#6P那个，玛布林老师？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'|\x00\x00'),
	Insn('EMOTE_STOP', Char(12)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600594V#11P……看样子，使用法术的话，\n'
		'做到这点就已经是极限了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600595V#11P心理暗示所能唤起的记忆\n'
		'就只有这么多了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600596V#11P或许……\n'
		'是神经系统\n'
		'出了什么问题也说不定。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600597V#0005F#6P神经系统的问题……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600598V#0101F#6P这、这是怎么一回事呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600599V#0201F#6P请问，那是怎么一回事……？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600600V#0301F#6P那是怎么回事啊……？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600601V#11P……简单来说，\n'
		'就是有关脑神经的问题。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600602V#11P出于某种原因，\n'
		'掌管记忆功能的神经指令\n'
		'传达受到了阻碍……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600603V#11P这种可能性也是有的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600604V#0011F#6P怎、怎么会……{wait}'
		'{page}'
		'#13600605V#0007F那样的话……\n'
		'难道就束手无策了吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600606V#11P说的也对……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600607V#11P教会中传承的法术\n'
		'是关于心灵与精神领域的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600608V#11P说不定，\n'
		'近代医学技术更加适合\n'
		'解决这个问题。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600609V#0005F#6P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600610V#0105F#6P近代医学的话，也就是说……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600611V#0205F#6P近代医学的话，也就是……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600612V#0305F#6P说起近代医学的话，也就是……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600613V#11P没错，就是圣乌尔斯拉医科大学。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600614V#11P虽然近代医学\n'
		'对于心灵与精神领域的研究\n'
		'至今还不够充分……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600615V#11P但在几年前，那里成立了\n'
		'一个名为『神经科』的新部门，\n'
		'听说那里拥有十分优秀的研究者。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600616V#11P你们去那里寻求帮助的话，\n'
		'说不定会寻找到不同于教会的解决途径。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600617V#0000F#6P『神经科』吗……\n'
		'（咦，似乎在什么地方听到过。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600618V#0103F#6P我说，罗伊德……{wait}'
				'{page}'
				'#13600619V#0101F我们应该去找\n'
				'那里的人谈谈吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600620V#0203F#6P罗伊德前辈……{wait}'
				'{page}'
				'#13600621V#0201F我们还是应该\n'
				'去那边商量一下吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600622V#0303F#6P喂，罗伊德。{wait}'
				'{page}'
				'#13600623V#0300F我们应该\n'
				'去那边看看吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600624V#0003F#6P嗯，说得也是呢……{wait}'
		'{page}'
		'#13600625V#0002F──老师，\n'
		'谢谢您了。{wait}'
		'{page}'
		'#13600626V我们立刻就去乌尔斯拉\n'
		'医院看看。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600627V#11P嗯，那就好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600628V#11P……真不好意思，\n'
		'没能帮上什么忙。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600629V#0005F#6P没、没那回事！\n'
		'您都告诉我们有关神经科的事了。{wait}'
		'{page}'
		'#13600630V#0000F还有……\n'
		'琪雅回想起来的那个场景\n'
		'应该也会成为相关线索。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600631V#0103F#6P『又黑暗又广阔的地方』啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600632V#0203F#6P『又黑暗又广阔的地方』么……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600633V#0303F#6P『又黑暗又广阔的地方』吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_ROTATE', Char(339), 180, 500),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600634V#1103F#11P嗯，而且上面还有\n'
		'朦胧的光线照射下来。{wait}'
		'{page}'
		'#13600635V#1112F还有嗡嗡嗡嗡的声音……\n'
		'那地方虽然很漂亮，但是感觉有点可怕。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600636V#0003F#6P嗯、嗯……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600637V#11P听上去……\n'
		'确实不是普通的地方呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600638V#11P愿你们得到女神#4R爱德斯#的祝福。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13600639V#11P我也会祈祷琪雅的问题\n'
		'能有一个好的结果。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CAM_DISTANCE', 23250, 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0xD5', 30),
	Insn('CHAR_SET_POS', Char(0), (150800, 0, 14000), 180),
	Insn('CHAR_SET_POS', Char(12), (150800, 200, 17500), 180),
	Insn('0x4C', Char(12), -1),
	Insn('FLAG_SET', Flag(1346)),
	Insn('FLAG_SET', Flag(1123)),
	Insn('QUEST', 72, Insn('TASK_SET', 5)),
	Insn('0x66', 0, 1),
	Insn('SOUND_STOP', 840),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][42] = [
	Insn('SOUND_LOOP', 840, 90),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 840, 80),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 840, 70),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 840, 60),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 840, 50),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 840, 40),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 840, 30),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 840, 20),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 840, 10),
	Insn('SLEEP', 100),
	Insn('SOUND_STOP', 840),
	Insn('RETURN'),
]

data['code'][43] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (2780, 2290, 22200), 0),
	Insn('CAM_ROTATE', 319, 26, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 28080, 0),
	Insn('CHAR_ROTATE', Char(8), 90, 0),
	Insn('CHAR_SET_POS', Char(257), (2500, 500, 22500), 270),
	Insn('CHAR_SET_POS', Char(258), (2500, 500, 24000), 270),
	Insn('CHAR_SET_POS', Char(259), (4000, 500, 22500), 270),
	Insn('CHAR_SET_POS', Char(260), (4000, 500, 24000), 270),
	Insn('SLEEP', 500),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P欢迎各位来到这所\n'
		'克洛斯贝尔大教堂。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P今天有什么事情呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0000F您就是艾拉尔达大主教吧？{wait}'
		'{page}'
		'我们是警察局丄特务支援课的人，\n'
		'今天是因为工作上的事情来拜访您的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P唔？是工作吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0100F我们接到了乌尔斯拉医院\n'
		'内科教授拉格先生的委托。{wait}'
		'{page}'
		'来这里领取一种叫做『羽扇豆草』的药材，\n'
		'关于此事，他事先好像已经联系过您了吧？{wait}'
		'{page}'
		'#0103F教授由于工作繁忙，\n'
		'所以才委托我们代他过来，\n'
		'找您领取那种药草……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P……稍等一下。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P拉格……你刚才说的是拉格教授吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P嗯，之前确实\n'
		'收到过他的来信……\n'
		'但关于此事，我还是第一次听说。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11P#0305F……啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P原因很简单。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P因为拉格教授的来信，\n'
		'我是一封也不会看的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0005F咦……咦咦！？{wait}'
		'{page}'
		'您、您为什么不……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P不为什么。\n'
		'关于这件事，\n'
		'我已经向女神发过誓了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11P#0305F（喂，罗伊德，这样的话……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0203F（……这二人的关系\n'
		'\u3000似乎很麻烦呢。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0106F（真令人头痛呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0003F（但、但是我们已经接下了这项委托……\n'
		'\u3000总得想办法完成啊。）{wait}'
		'{page}'
		'#0001F那、那个……\n'
		'艾拉尔达大主教。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P……什么事？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0001F拉格教授委托我们领取的药草，\n'
		'据说是要用于内科研究的。{wait}'
		'{page}'
		'我想，以乌尔斯拉医院的研究条件，\n'
		'将来肯定可以让\n'
		'那种药草帮助到更多的病人。{wait}'
		'{page}'
		'#0008F那个……我并不准备打听\n'
		'您与拉格教授之间有什么过节。{wait}'
		'{page}'
		'#0003F只是，无论如何，\n'
		'也想请您将『羽扇豆草』交给\n'
		'拉格教授，可以吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P…………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P……你是不是\n'
		'误会了什么……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P我并没说过\n'
		'不把药草交给你们啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0005F……咦？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P……『羽扇豆草』的话，\n'
		'就在我的办公室里，在大教堂左侧的最里面。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P跟伦顿祭司说\n'
		'已经得到了我的许可，\n'
		'他就会给你们的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P……好了，话说完了。\n'
		'你们快点走吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0005F那、那个……\n'
		'谢谢您……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (2750, 2490, 2009), 0),
	Insn('CAM_ROTATE', 315, 26, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 27740, 1000),
	Insn('CHAR_ROTATE', Char(8), 90, 0),
	Insn('CHAR_SET_POS', Char(257), (-500, 500, 7500), 180),
	Insn('CHAR_SET_POS', Char(258), (1000, 500, 7500), 180),
	Insn('CHAR_SET_POS', Char(259), (-500, 500, 9000), 180),
	Insn('CHAR_SET_POS', Char(260), (1000, 500, 9000), 180),
	Insn('FORK', 257, 1, [
		Insn('0x98', Char(254), (0, 0, -4000), 2000, 0),
	]),
	Insn('FORK', 258, 1, [
		Insn('0x98', Char(254), (0, 0, -4000), 2000, 0),
	]),
	Insn('FORK', 259, 1, [
		Insn('0x98', Char(254), (0, 0, -4000), 2000, 0),
	]),
	Insn('FORK', 260, 1, [
		Insn('0x98', Char(254), (0, 0, -4000), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('CAM_DISTANCE', 26740, 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 315, 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0003F那、那个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0300F总觉得\n'
		'说服的过程太轻松了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0100F与其说是被罗伊德说服了，\n'
		'倒不如说是\n'
		'大主教自愿交给我们的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11P#0200F虽然不是很明白……{wait}'
		'{page}'
		'但趁着大主教还没有\n'
		'改变主意，还是赶快\n'
		'去拿药草为好吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0003F说得也是。{wait}'
		'{page}'
		'#0000F那个……应该是左侧里面的办公室，\n'
		'我们去看看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (1900, 2490, 2430), 0),
	Insn('CAM_ROTATE', 315, 26, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 22000, 0),
	Insn('CHAR_ROTATE', Char(8), 180, 0),
	Insn('CHAR_SET_POS', Char(0), (-500, 0, 3500), 180),
	Insn('CHAR_SET_POS', Char(1), (-500, 0, 3500), 180),
	Insn('CHAR_SET_POS', Char(2), (-500, 0, 3500), 180),
	Insn('CHAR_SET_POS', Char(3), (-500, 0, 3500), 180),
	Insn('QUEST', 19, Insn('TASK_SET', 1)),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][44] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (97580, 1200, 7510), 0),
	Insn('CAM_ROTATE', 314, 27, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 27740, 0),
	Insn('CHAR_ROTATE', Char(10), 90, 0),
	Insn('CHAR_SET_POS', Char(257), (98000, 0, 7000), 270),
	Insn('CHAR_SET_POS', Char(258), (98000, 0, 8300), 270),
	Insn('CHAR_SET_POS', Char(259), (99300, 500, 7000), 270),
	Insn('CHAR_SET_POS', Char(260), (99300, 500, 8300), 270),
	Insn('SLEEP', 500),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P哎呀，有什么事情吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P这里是艾拉尔达大主教的办公室，\n'
		'无关人员不能随便进入哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0000F那个，我们是\n'
		'警察局丄特务支援课的人……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}罗伊德将前来领取『羽扇豆草』的事情\n'
		'做了说明。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P……哦，原来如此，\n'
		'是这样啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P你们已经获得大主教的许可了吧？\n'
		'那么，请稍等一下。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (98390, 1500, 8960), 4000),
	Insn('CHAR_ROTATE', Char(10), 0, 500),
	Insn('FORK', 10, 1, [
		Insn('0x95', Char(254), (96000, 0, 11500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('FORK', 10, 1, [
		Insn('0x95', Char(254), (100000, 0, 11500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('CHAR_ROTATE', Char(10), 0, 500),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(10), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 910, 0, 0, 100),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('CAM_OFFSET', (97580, 1500, 7510), 4000),
	Insn('CHAR_ROTATE', Char(10), 270, 500),
	Insn('FORK', 10, 1, [
		Insn('0x95', Char(254), (96000, 0, 11500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('FORK', 10, 1, [
		Insn('0x95', Char(254), (96000, 0, 7830), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('CHAR_ROTATE', Char(10), 90, 500),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P好了，这就是『羽扇豆草』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'收下了{item 833}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 833, 1),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P羽扇豆（Ｌｕｐｉｎｕｓ）在古语中\n'
		'是『狼』的意思。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P据说是很久以前由神狼赠与人类，\n'
		'拥有悠久历史的药草。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P过去，似乎在克洛斯贝尔市附近\n'
		'就能采集到，但由于城市开发的影响，\n'
		'其数量正在逐渐减少……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0100F我小时候好像\n'
		'也听外公说过\n'
		'同样的事。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0005F这样啊……{wait}'
		'{page}'
		'#0003F但是……大主教为什么\n'
		'愿意把如此贵重的药草\n'
		'交给我们呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0306F真让人难以理解啊。\n'
		'大主教好像很讨厌\n'
		'拉格教授。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0200F大主教如此讨厌教授的理由\n'
		'也让人觉得有些在意……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P哦，那个啊。\n'
		'……唉，那也是没有办法的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P乌尔斯拉医院的拉格教授\n'
		'原来是这所大教堂\n'
		'的见习祭司。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0005F医院的医生以前竟然是祭司……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P没什么可奇怪的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P虽说是先进医疗技术，\n'
		'但内科与七耀教会的研究领域\n'
		'非常相近。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0200F确实，七耀教会中\n'
		'也在进行着关于药剂调配的研究。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0105F但是，为什么拉格教授\n'
		'会放弃成为祭司，而去了医院呢……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P据说，当时是医院的院长\n'
		'来挖角的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P拉格教授虽然在跟随大主教\n'
		'学习调配药剂……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P但他也很想挑战一下\n'
		'先进医疗这个领域，\n'
		'因此就放弃了祭司这条道路。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P而大主教也是个顽固的人，\n'
		'无法原谅放弃祭司之路的拉格教授。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0303F嗯，这种心情也不是不能理解啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P不过，大主教虽然很顽固……\n'
		'但也是个明事理的人。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P你看，他不是自愿\n'
		'把药草交给你们了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#5P对于拉格教授的实力，\n'
		'大主教还是很认可的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0203F看来，他们之间的关系并不是很麻烦……{wait}'
		'{page}'
		'#0200F而是超级麻烦呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0012F哈、哈哈……\n'
		'（说得还真直接啊……）{wait}'
		'{page}'
		'#0003F总之，\n'
		'已经得到了目标物品。{wait}'
		'{page}'
		'#0000F快点去乌尔斯拉医院，\n'
		'把药草交给拉格教授吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (98000, 2000, 7000), 0),
	Insn('CAM_ROTATE', 315, 28, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 33000, 0),
	Insn('CHAR_ROTATE', Char(8), 180, 0),
	Insn('CHAR_SET_POS', Char(0), (98000, 0, 7000), 270),
	Insn('CHAR_SET_POS', Char(1), (98000, 0, 7000), 270),
	Insn('CHAR_SET_POS', Char(2), (98000, 0, 7000), 270),
	Insn('CHAR_SET_POS', Char(3), (98000, 0, 7000), 270),
	Insn('QUEST', 19, Insn('TASK_SET', 2)),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][45] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('TEXT_TALK', Char(8), Text(
				'……拉格教授他\n'
				'是遵从自己的意志\n'
				'而选择从医之路的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'对此，我也无法\n'
				'再多说些什么。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('TASK_GET', 2))), Insn('END')]), [
			Insn('TEXT_TALK', Char(8), Text(
				'……怎么了，\n'
				'还有什么别的事情吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'拿到了药草的话，\n'
				'就快点送过去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('TASK_GET', 1))), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'『羽扇豆草』储备在教堂左侧\n'
						'的最里面，我的办公室内。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'去找伦顿祭司，\n'
						'他会拿给你们的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'『羽扇豆草』储备在教堂左侧\n'
						'的最里面，我的办公室内。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'去找伦顿祭司，\n'
						'他会拿给你们的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'……还有什么别的事情吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F不，没有了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][46] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (152600, 1700, 16650), 0),
	Insn('CAM_ROTATE', 322, 28, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 27870, 0),
	Insn('CHAR_ROTATE', Char(12), 90, 0),
	Insn('CHAR_SET_POS', Char(257), (153300, 200, 16500), 270),
	Insn('CHAR_SET_POS', Char(239), (154500, 200, 17180), 270),
	Insn('CHAR_SET_POS', Char(339), (153300, 200, 17700), 270),
	Insn('0x4B', Char(12), -1),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('0x0D'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 39, Insn('TASK_GET', 0))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(339), Text(
				'#11P#1110F午安，我们又来了！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P哎呀，午安，琪雅。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P……难道是忘记什么东西了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0000F不，并不是\n'
				'那样的……{wait}'
				'{page}'
				'其实，刚才正好跟孩子们擦肩而过，\n'
				'所以有点在意。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P呵呵，主日学校\n'
				'又要开始上课了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P不过……\n'
				'你们来得\n'
				'倒是正好。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(0), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('EMOTE', Char(1), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P实际上，很久之前……\n'
				'就想给孩子们讲讲\n'
				'关于克洛斯贝尔警察的事情了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#12P#0105F关于警察的……事吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#12P#0205F关于警察……？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#12P#0305F在主日学校\n'
						'给孩子们上关于警察的课吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P嗯，没错。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P因此，想拜托你们……\n'
				'担任这堂课的\n'
				'特别讲师。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(0), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('EMOTE', Char(1), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0005F特别讲师？也就是说……\n'
				'需要我上讲台吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P嗯，请一定要帮这个忙。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P警察的知识，\n'
				'果然还是由警察来讲\n'
				'最合适吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P我想，与我相比，\n'
				'你们来教的效果会好得多。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P怎么样？要不要试着做一回……\n'
				'主日学校的讲师呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('QUEST', 39, Insn('FLAG_UNSET', 2)),
			Insn('QUEST', 39, Insn('TASK_SET', 0)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(12), Text(
				'#5P担任主日学校的讲师一事……\n'
				'你们愿意\n'
				'接受了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, -1, 0, Text(
		'【接受】\n'
		'【拒绝】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0003F不……\n'
				'还请容我推辞。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P哎呀，这样吗？\n'
				'我还觉得\n'
				'这是个不错的想法呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P不过，如果不方便的话，\n'
				'那就不勉强你们了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P要是改变主意了，\n'
				'就再来找我吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_POS', Char(0), (153260, 200, 16760), 270),
			Insn('0x4C', Char(12), -1),
			Insn('EVENT_END', 5),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0000F……嗯，\n'
				'请务必让我接受这项委托。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P哎呀，真的吗？\n'
				'呵呵，真是帮大忙了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 239, 1, [
				Insn('CHAR_WATCH', Char(254), Char(257), 500),
			]),
			Insn('FORK', 339, 1, [
				Insn('CHAR_WATCH', Char(254), Char(257), 500),
			]),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#12P#0105F罗伊德……没问题吗？{wait}'
						'{page}'
						'#0103F我想，教人学习\n'
						'并不是一件\n'
						'简单的事情哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#12P#0200F……没问题吗？{wait}'
						'{page}'
						'#0203F教学生这种事情，\n'
						'半桶水是应付不来的呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#12P#0306F喂喂，你没问题吧？{wait}'
						'{page}'
						'#0300F虽然由我来说也不太合适……\n'
						'但这并不是\n'
						'可以轻易答应的事啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
			Insn('FORK', 257, 1, [
				Insn('CHAR_WATCH', Char(254), Char(239), 500),
			]),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F嗯，我知道。\n'
				'我也不是\n'
				'不经思考就接受的。{wait}'
				'{page}'
				'#0003F只是……我觉得这是一个\n'
				'让大家了解警察的\n'
				'难得机会。{wait}'
				'{page}'
				'#0000F就像过去的我和艾莉一样，\n'
				'在这些孩子当中，说不定也会有\n'
				'未来的警察呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#12P#0104F……原来如此，\n'
						'真是很符合罗伊德风格的想法呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#12P#0204F嗯……确实也有一定的道理呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#12P#0300F原来如此……\n'
						'也就是说，有点类似传教活动吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
			Insn('FORK', 257, 1, [
				Insn('CHAR_WATCH', Char(254), Char(339), 500),
			]),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F这样的话，就要迟一点再去\n'
				'乌尔斯拉医院了……\n'
				'琪雅，可以吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(339), Text(
				'#11P#1109F嗯，可以啊！{wait}'
				'{page}'
				'#1100F虽然不是很明白，\n'
				'但罗伊德要是想做的话，\n'
				'琪雅会支持你的！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0009F哈哈，谢谢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P好了，那么……\n'
				'先出去一下。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#5P我先把讲课的流程\n'
				'告诉你吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 257, 1, [
				Insn('CHAR_WATCH', Char(254), Char(12), 500),
			]),
			Insn('FORK', 239, 1, [
				Insn('CHAR_WATCH', Char(254), Char(12), 500),
			]),
			Insn('FORK', 339, 1, [
				Insn('CHAR_WATCH', Char(254), Char(12), 500),
			]),
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0000F拜托您了，\n'
				'玛布林老师。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('SOUND_PLAY', 80, 0, 0, 100),
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 2}任务【主日学校的特别讲师】{color 0}开始！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('SLEEP', 500),
			Insn('CALL', Function((0, 47))),
			Insn('CALL', Function((0, 48))),
			Insn('CALL', Function((0, 51))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][47] = [
	Insn('CAM_OFFSET', (7710, 2300, -90), 0),
	Insn('CAM_ROTATE', 315, 25, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 26410, 0),
	Insn('CHAR_SET_POS', Char(12), (7600, 0, 1320), 270),
	Insn('CHAR_SET_POS', Char(257), (5570, 0, 1350), 90),
	Insn('CHAR_SET_POS', Char(239), (4380, 0, 2050), 90),
	Insn('CHAR_SET_POS', Char(339), (4720, 0, 510), 90),
	Insn('SLEEP', 500),
	Insn('CAM_DISTANCE', 25410, 1000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('EMOTE_STOP', Char(12)),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0003F──原来如此，我大致清楚了。{wait}'
		'{page}'
		'首先要把有关警察的知识\n'
		'简单易懂地说明一遍……{wait}'
		'{page}'
		'#0000F最后再留出问答的时间。\n'
		'……差不多就是这样吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#12P嗯，那样就足够了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#12P另外，我有一个提议。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0005F提议……吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#12P对，如果方便的话……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#12P让琪雅也来\n'
		'听罗伊德讲课吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(0), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(1), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(339), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0005F哎……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#5P#0100F玛布林老师……\n'
				'真的可以吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#5P#0204F确实……\n'
				'那样好像很有趣呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#5P#0309F哈哈，不是挺有趣的嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(339), Text(
		'#5P#1105F琪雅也可以听\n'
		'罗伊德讲课吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#12P嗯，当然可以了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#12P像你这个年纪的孩子，\n'
		'本来也已经可以\n'
		'来主日学校上课了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#5P#1110F哇……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(339), Char(257), 500),
	Insn('TEXT_TALK', Char(339), Text(
		'#6P#1109F那琪雅\n'
		'也要听课！{wait}'
		'{page}'
		'因为琪雅想要知道很多\n'
		'有关罗伊德他们的事情！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(339), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 239, 1, [
		Insn('CHAR_WATCH', Char(254), Char(339), 500),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0005F琪雅……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(239), Char(257), 500),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#5P#0100F罗伊德，这样的话，\n'
				'你真是不上也不行了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#5P#0200F罗伊德前辈……\n'
				'似乎没有退路了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#5P#0300F话都说到这份上了，\n'
				'看来你是逃不掉了吧～？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0004F……哈哈，似乎是这样啊。{wait}'
		'{page}'
		'#0000F琪雅，要和其他孩子\n'
		'一起认真听课哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#6P#1110F嗯！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#5P#0104F我也到\n'
				'教室的后面\n'
				'去看看你上课的样子吧。{wait}'
				'{page}'
				'#0100F加油哦，罗伊德。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#5P#0203F我也打算去教室后面\n'
				'旁听一下。{wait}'
				'{page}'
				'#0211F……我会为前辈加油的，\n'
				'所以请不要搞砸。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#5P#0304F那么，我也去教室后面\n'
				'看看你上课的样子吧。{wait}'
				'{page}'
				'#0300F罗伊德老师，\n'
				'给我露一手吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(239), 500),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0006F（感、感觉好狡猾啊……）{wait}'
		'{page}'
		'#0000F不过……\n'
		'也只有加油上了。{wait}'
		'{page}'
		'这是一个让大家\n'
		'了解警察的好机会……\n'
		'可不能错过了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#12P就是要有那股气势。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#12P好了……\n'
		'差不多也该\n'
		'开始上课了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('RETURN'),
]

data['code'][48] = [
	Insn('LOAD_CHCP', 'chr/ch08202', 30),
	Insn('CAM_OFFSET', (151700, 1500, 4100), 0),
	Insn('CAM_ROTATE', 315, 23, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 29780, 0),
	Insn('CHAR_SET_POS', Char(12), (150800, 200, 17500), 180),
	Insn('CHAR_SET_POS', Char(339), (153000, 200, 17650), 180),
	Insn('CHAR_SET_POS', Char(257), (155630, 200, 17510), 270),
	Insn('CHAR_SET_POS', Char(239), (150910, 0, 1530), 0),
	Insn('CAM_OFFSET', (151620, 1500, 14920), 7000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(12), Text(
		'#11P那么……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#11P今天在上课之前，\n'
		'先给大家\n'
		'介绍一位新朋友。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(12), Char(339), 500),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P──琪雅，请做个自我介绍吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 12, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('0x98', Char(339), (0, 0, -2000), 2000, 0),
	Insn('TEXT_TALK', Char(339), Text(
		'#11P#1110F那个，我是琪雅哦！\n'
		'请多关照！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', 30, 200, -1, -1),
	Insn('TEXT_SET_NAME', Translate('小孩子们')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#5S请多关照～～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(12), Text(
		'#11P呵呵，谢谢你充满朝气的\n'
		'自我介绍。请找个\n'
		'空位置坐下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#11P#1109F好～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (154300, 1500, 8280), 4000),
	Insn('0x95', Char(339), (153000, 200, 14000), 2000, 0),
	Insn('0x95', Char(339), (152000, 200, 14000), 2000, 0),
	Insn('0x95', Char(339), (152000, 200, 9100), 2000, 0),
	Insn('CHAR_ROTATE', Char(339), 90, 300),
	Insn('CROSSFADE', 500),
	Insn('CHAR_SET_CHCP', Char(339), 30),
	Insn('CHAR_SET_POS', Char(339), (153620, 150, 9130), 0),
	Insn('CHAR_FLAG1_SET', Char(339), 4),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('CHAR_SET_FRAME', Char(339), 2),
	Insn('CHAR_SET_FRAME', Char(17), 1),
	Insn('EMOTE', Char(339), 0, 1700, (38, 39, 250, 2)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(339), Text(
		'#5P#1109F嘿嘿，请多关照哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(17), Text(
		'#12P嗯、嗯，\n'
		'请多关照。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (152620, 1500, 3180), 0),
	Insn('CAM_ROTATE', 331, 19, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 29780, 0),
	Insn('0x0D'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#6P#0104F（呵呵……感觉自己有点像\n'
				'\u3000参加教学旁听的母亲呢。）{wait}'
				'{page}'
				'#0100F（琪雅，加油啊！）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#6P#0204F（……家长们的教学参观……\n'
				'\u3000现在大概就是这种感觉吧。）{wait}'
				'{page}'
				'#0200F（必须要给琪雅加油呢。）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#6P#0304F（默默守护认真学习的女儿……\n'
				'\u3000哈，这种立场可真让人振奋百倍呢。）{wait}'
				'{page}'
				'#0309F（加油啊！小琪！）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('0x5A'),
	Insn('CROSSFADE', 500),
	Insn('CHAR_SET_FRAME', Char(339), 0),
	Insn('CHAR_SET_FRAME', Char(17), 0),
	Insn('CAM_OFFSET', (152750, 1500, 15630), 0),
	Insn('CAM_ROTATE', 315, 23, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 29780, 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(12), Text(
		'#11P还有……今天\n'
		'我们请来了特别讲师\n'
		'为大家讲课。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(12), Char(257), 300),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P──罗伊德，请吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0003F好、好的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (152250, 1700, 12670), 3000),
	Insn('CAM_ROTATE', 310, 14, 0, 3000),
	Insn('CAM_DISTANCE', 30190, 3000),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 49))),
	Insn('SLEEP', 500),
	Insn('FORK_FUNC', Char(12), 3, Function((0, 50))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(35), Text(
		'#6P喂喂，\n'
		'我刚才还在想，会不会是这样……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#6P真没想到，特别讲师居然就是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0003F那、那个……\n'
		'有些同学似乎\n'
		'已经认识我了呢……{wait}'
		'{page}'
		'#0000F我的名字是\n'
		'罗伊德丄班宁斯。{wait}'
		'{page}'
		'是隶属于克洛斯贝尔\n'
		'警察局丄特务支援课的\n'
		'现役警察。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P警察～？\n'
		'什么啊，你认识\n'
		'龙他们吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'#5P特务支援课……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'#5P啊，我好像看到过\n'
		'克洛斯贝尔时报周刊上的报道！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P……啊啊，说起来！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P虽然我没有读新闻，\n'
		'但记得上面登了张\n'
		'很小的照片……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#11P好了好了，大家安静。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#11P今天想让大家学习\n'
		'关于警察的知识，\n'
		'所以就拜托罗伊德老师过来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#11P大家要认真\n'
		'听讲哦～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_SET_POS', 100, 100, -1, -1),
	Insn('TEXT_SET_NAME', Translate('小孩子们')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#5S是～～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('CHAR_WATCH', Char(12), Char(257), 300),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P那么，接下来就拜托你啦，\n'
		'罗伊德老师㈱{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(12), 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0003F好、好的，\n'
		'请交给我吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(12), 270, 300),
	Insn('0x95', Char(12), (146430, 200, 17490), 2000, 0),
	Insn('CHAR_ROTATE', Char(12), 135, 300),
	Insn('CHAR_ROTATE', Char(257), 180, 300),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0003F（糟糕……\n'
		'\u3000突然好紧张啊……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(339), 0, 1700, (24, 27, 250, 0)),
	Insn('CAM_OFFSET', (153200, 1700, 9500), 3000),
	Insn('CAM_ROTATE', 319, 10, 0, 3000),
	Insn('0x6F', b'y'),
	Insn('EMOTE_STOP', Char(339)),
	Insn('0x82', 200, 0, 3000, 300),
	Insn('TEXT_TALK', Char(339), Text(
		'#6P#1107F#5S#N……罗伊德，加油哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(35), 0, 1700, (38, 39, 250, 2)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(35), Text(
		'#6P啊哈哈！怎么了啊，大哥哥！\n'
		'她在给你加油哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#6P我说龙，你别这样啦～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#6P大哥哥\n'
		'也很努力的～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0006F那个，琪雅……\n'
		'要开始上课了，安静一点哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#6P#1106F哼，琪雅明明是在给你加油。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0004F（……紧张的感觉\n'
		'\u3000好像稍微有点缓解了。）{wait}'
		'{page}'
		'#0000F……咳咳。\n'
		'那么，我们现在就开始吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('BGM_STOP', 2000),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (151090, 1500, 15660), 0),
	Insn('CAM_ROTATE', 0, 17, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 32470, 0),
	Insn('0x0D'),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'o\x00\x00'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}开始上课！\n'
		'～关于警察组织～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}※请选择正确的答案，\n'
		'使特别授课获得成功！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_TALK', Char(257), Text(
		'#0004F首先……\n'
		'大家知道警察\n'
		'是什么吗？{wait}'
		'{page}'
		'#0000F克洛斯贝尔自治州，\n'
		'被规定了不能拥有\n'
		'其它国家具备的『某项东西』的。{wait}'
		'{page}'
		'作为替代，才会有『警备队』以及\n'
		'我们这些『警察』存在。{wait}'
		'{page}'
		'#0003F克洛斯贝尔自治州所没有的，\n'
		'『对国家来说非常重要的东西』指的是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'克洛斯贝尔自治州所没有的，\n'
		'『对国家来说非常重要的东西』指的是？{0x18}{wait}'
	)),
	Insn('MENU', 0, -1, 150, 0, Text(
		'【①情报机关】\n'
		'【②游击士协会】\n'
		'【③军队】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……是情报机关。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 54))),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F（那种组织确实并不存在，\n'
				'\u3000但好像也没有被法律所禁止啊……）{wait}'
				'{page}'
				'#0012F那个……为了保护国家，\n'
				'收集邻近各国的情报\n'
				'是必不可少的……{wait}'
				'{page}'
				'虽然平时都致力于防止犯罪，\n'
				'但暗地里却通过游客等途径\n'
				'收集重要的情报。{wait}'
				'{page}'
				'#0011F（我、我到底在说些什么啊……\n'
				'\u3000果然是太紧张了吗？）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……游击士协会。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 54))),
			Insn('TEXT_TALK', Char(257), Text(
				'#0012F虽、虽然游击士协会\n'
				'现在的表现非常活跃……{wait}'
				'{page}'
				'但在过去，扮演其角色，\n'
				'并守卫着市民们的是警察。{wait}'
				'{page}'
				'#0006F（说、说的实在是乱七八糟……\n'
				'\u3000果然是太紧张了吗？）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		2: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……是军队。{wait}'
				'{page}'
				'举例来说，在邻国埃雷波尼亚，\n'
				'由军队全权负责抵御入侵\n'
				'与防止犯罪……{wait}'
				'{page}'
				'但在没有军队的克洛斯贝尔，\n'
				'这些职能就分别\n'
				'由数个组织来承担。{wait}'
				'{page}'
				'……在那之中，\n'
				'负责调查案件，以及防止犯罪的\n'
				'就是我们警察了。{wait}'
				'{page}'
				'#0004F（很好，应该没有错。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 55))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 55))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F警察局中设有各种部门，\n'
		'人员会依据职能被分配到不同部门中。{wait}'
		'{page}'
		'然后各事件会按照其种类与紧急程度\n'
		'被分派给各部门，以便他们\n'
		'采取妥善的方法来处理。{wait}'
		'{page}'
		'#0003F其中，有一个处理\n'
		'震动社会的大事件，\n'
		'以及国际性案件的部门……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'处理大事件以及\n'
		'国际性案件的部门是？{0x18}{wait}'
	)),
	Insn('MENU', 0, -1, 150, 0, Text(
		'【①搜查一课】\n'
		'【②搜查二课】\n'
		'【③特务支援课】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……是搜查一课。{wait}'
				'{page}'
				'要解决绑架、杀人之类的大案件，\n'
				'就需要一流的搜查官\n'
				'全力以赴。{wait}'
				'{page}'
				'因此，聚集了精英搜查官的\n'
				'搜查一课便负责全权处理\n'
				'此类案件。{wait}'
				'{page}'
				'#0004F（我们也不能输给他们，\n'
				'\u3000必须得继续加油啊。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……是搜查二课。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 54))),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F要处理绑架、杀人\n'
				'之类的大案件，当然也得具备\n'
				'解决小案子的能力。{wait}'
				'{page}'
				'平日就负责处理盗窃等案件的\n'
				'搜查二课，也会勤勤恳恳地\n'
				'对大型案件进行调查哦。{wait}'
				'{page}'
				'#0006F（……虽然说得\n'
				'\u3000像是有那么一回事……\n'
				'\u3000但真的是那样吗？）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		2: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……是我们，特务支援课。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 54))),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F要想解决绑架、杀人\n'
				'之类的大型案件，大范围的\n'
				'调查活动是很重要的。{wait}'
				'{page}'
				'从这层意义上讲，\n'
				'行动自由的特务支援课\n'
				'最适合调查大型案件了。{wait}'
				'{page}'
				'#0006F（……啊，好像把我们自己\n'
				'\u3000美化过头了呢……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 55))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 55))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F每一位警察都会得到一本叫做\n'
		'搜查手册的东西。{wait}'
		'{page}'
		'这本搜查手册\n'
		'除了可以证明我们的警察身份之外，\n'
		'还有一个最大，也是最重要的用途。{wait}'
		'{page}'
		'#0003F那是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'搜查手册的重要用途是？{0x18}{wait}'
	)),
	Insn('MENU', 0, -1, 150, 0, Text(
		'【①记录调查情况】\n'
		'【②代替逮捕令】\n'
		'【③报告当前位置】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……记录调查情况。\n'
				'也就是说，搜查手册与笔记本相同。{wait}'
				'{page}'
				'它在用于整理任务情况时非常便利，而警察局也会\n'
				'以此为依据来审核勤务，以及发放各种经费。{wait}'
				'{page}'
				'搜查手册确实是\n'
				'警察的必备物品啊。{wait}'
				'{page}'
				'#0004F（嗯，完全没有问题。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……代替逮捕令。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 54))),
			Insn('TEXT_TALK', Char(257), Text(
				'#0012F那、那个，要逮捕嫌疑犯的话，\n'
				'需要向警察局总部\n'
				'提交正式的申请……{wait}'
				'{page}'
				'#0000F但在紧急时刻，\n'
				'只要出示这本手册，\n'
				'即使没有逮捕令，也可以将嫌疑人逮捕。{wait}'
				'{page}'
				'#0006F（嗯、嗯……\n'
				'\u3000稍微有点没自信呢……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		2: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……报告当前位置。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 54))),
			Insn('TEXT_TALK', Char(257), Text(
				'#0012F那、那个……\n'
				'这本手册带有将\n'
				'所在地信息发送出去的机能……{wait}'
				'{page}'
				'#0000F所以，即使出勤在外，\n'
				'也能让同伴们知道\n'
				'自己所处的位置。{wait}'
				'{page}'
				'#0006F（不、不管怎么说，这都太夸张了啊。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 55))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 55))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F警察与游击士一样，\n'
		'配备有最新型的\n'
		'战术导力器。{wait}'
		'{page}'
		'#0003F警察虽然不是专门的战斗集团，\n'
		'但搜查官在追捕犯人时，\n'
		'经常避免不了战斗。{wait}'
		'{page}'
		'#0000F顺便说一下，战术导力器的型号\n'
		'已经更新过好几代了，\n'
		'而且每次更新都会追加新功能。{wait}'
		'{page}'
		'#0003F现在我们所使用的\n'
		'战术导力器的型号是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'目前的战术导力器的型号是？{0x18}{wait}'
	)),
	Insn('MENU', 0, -1, 150, 0, Text(
		'【①第５代】\n'
		'【②第６代】\n'
		'【③第７代】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……第５代，\n'
				'通常被称为\n'
				'『ＥＮＩＧＭＡ』。{wait}'
				'{page}'
				'ＥＮＩＧＭＡ内设有通讯器。\n'
				'因为可以在紧急时刻进行联系，\n'
				'所以这项功能对警察行业来说十分宝贵。{wait}'
				'{page}'
				'#0004F（嗯，应该没说错。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……第６代，\n'
				'通常被称为\n'
				'『ＥＮＩＧＭＡ』。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 54))),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F由于型号的变化，结晶回路也\n'
				'必须重新合成，\n'
				'所以用起来很麻烦。{wait}'
				'{page}'
				'#0006F（……咦，是第６代\n'
				'\u3000没错吗……？）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		2: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……第７代，\n'
				'通常被称为\n'
				'『ＥＮＩＧＭＡ』。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 54))),
			Insn('TEXT_TALK', Char(257), Text(
				'#0012F那、那个……\n'
				'因为各种功能都变得十分新颖，\n'
				'所以用起来很麻烦呢。{wait}'
				'{page}'
				'#0006F（嗯、嗯……\n'
				'\u3000更新过那么多代吗……？）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 55))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 55))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F巡警、搜查官……\n'
		'担当各类职责的警察们，\n'
		'都在为了克洛斯贝尔而辛勤工作。{wait}'
		'{page}'
		'#0003F虽然从表面上看起来，\n'
		'他们之间完全没有关联……{wait}'
		'{page}'
		'#0000F但是，警察们在工作时，\n'
		'都是按照某个基本理念来行动的。{wait}'
		'{page}'
		'#0003F那个基本理念是…………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'警察的基本理念是？{0x18}{wait}'
	)),
	Insn('MENU', 0, -1, 150, 0, Text(
		'【①保障克洛斯贝尔市民的安全】\n'
		'【②维持治安与遵守当地法律】\n'
		'【③警戒国外势力与维护和平】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……保障克洛斯贝尔市民的安全。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 54))),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F无论在何种情况下，\n'
				'都要誓死守护克洛斯贝尔市民……{wait}'
				'{page}'
				'创造一个让大家都能\n'
				'安心生活的社会，这就是警察的本职。{wait}'
				'{page}'
				'#0006F（嗯、嗯。\n'
				'\u3000说明好像稍微有点不够吧……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……是维持自治州的治安与遵守自治州法律。{wait}'
				'{page}'
				'通过管制破坏法规的人，\n'
				'来创造一个可以让大家\n'
				'安心生活的社会……{wait}'
				'{page}'
				'将自己遵纪守法的一面展示给市民，\n'
				'成为大家的榜样，\n'
				'从而抑制犯罪的发生。{wait}'
				'{page}'
				'综上所述，维持治安，\n'
				'努力建立一个没有\n'
				'犯罪的世界，便是警察的本职。{wait}'
				'{page}'
				'#0004F（好了……总结得非常不错！）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('BREAK'),
		],
		2: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……是保持对国外势力的警戒与维护和平。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 54))),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F被帝国与共和国\n'
				'这两个大国夹在中间的克洛斯贝尔，\n'
				'是个犯罪频发的地方。{wait}'
				'{page}'
				'抵御他国敌对势力的入侵，\n'
				'创造一个大家能够\n'
				'安心生活的社会，便是警察的本职。{wait}'
				'{page}'
				'#0006F（……呃，硬要说的话，\n'
				'\u3000这应该是\n'
				'\u3000警备队的工作吧……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 55))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 55))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0004F──综上所述，克洛斯贝尔警察局\n'
		'便是这样一种组织。{wait}'
		'{page}'
		'#0000F……虽然对你们来说可能还有些复杂，\n'
		'但大家应该都听明白了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (152620, 1500, 3180), 0),
	Insn('CAM_ROTATE', 331, 19, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 29780, 0),
	Insn('0x0D'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 4), Insn('CONST', 4), Insn('GE'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#6P#0100F（这样一来，教学的前半部分就结束了。）{wait}'
						'{page}'
						'#0104F（虽然刚开始还有点紧张，\n'
						'\u3000但却让人一点都看不出来，\n'
						'\u3000很有老师的样子呢。）{wait}'
						'{page}'
						'#0100F（真不愧是通过了\n'
						'\u3000搜查官考试的实力派。）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('VAR', 4), Insn('CONST', 3), Insn('GE'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#6P#0100F（这样一来，教学的前半部分就结束了。）{wait}'
						'{page}'
						'#0103F（嗯，即使是罗伊德，\n'
						'\u3000似乎也稍微陷入了苦战呢。）{wait}'
						'{page}'
						'（不知道是不是\n'
						'\u3000因为开始时太紧张了。）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(258), Text(
						'#6P#0103F（这样一来，教学的前半部分就结束了。）{wait}'
						'{page}'
						'#0111F（但是……\n'
						'\u3000总觉得，如果是罗伊德的话，\n'
						'\u3000应该能够表现得更好一点的。）{wait}'
						'{page}'
						'（也就是说，玛布林老师\n'
						'\u3000似乎看错人了呢……）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 4), Insn('CONST', 4), Insn('GE'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#6P#0200F（教学的前半部分\n'
						'\u3000终于结束了。）{wait}'
						'{page}'
						'#0204F（授课内容完美地把握住了重点，\n'
						'\u3000而且声音洪亮，讲解内容有条不紊……\n'
						'\u3000真是无懈可击。）{wait}'
						'{page}'
						'（罗伊德前辈就算\n'
						'\u3000去大学之类的地方执教，\n'
						'\u3000或许也足以胜任呢。）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('VAR', 4), Insn('CONST', 3), Insn('GE'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#6P#0200F（教学的前半部分\n'
						'\u3000终于结束了。）{wait}'
						'{page}'
						'#0203F（声音偶尔会有一种缺乏自信的感觉，\n'
						'\u3000让我稍稍担心了一下……）{wait}'
						'{page}'
						'（毕竟是我们的领队，\n'
						'\u3000希望他能再加把劲呢。）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(259), Text(
						'#6P#0203F（教学的前半部分\n'
						'\u3000终于结束了。）{wait}'
						'{page}'
						'#0211F（……眼睛完全不敢正视学生，\n'
						'\u3000紧张得联手都不知道该放在哪里了……）{wait}'
						'{page}'
						'（……讲得实在是不怎么样呢。\n'
						'\u3000就算由我来教，\n'
						'\u3000可能都要比这好一些……）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 4), Insn('CONST', 4), Insn('GE'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#6P#0305F（哦，前半战已经结束了啊。）{wait}'
						'{page}'
						'#0309F（真不错，\n'
						'\u3000挺有摸有样的嘛。）{wait}'
						'{page}'
						'#0303F（世界上的淑女们\n'
						'\u3000都对这样的男人没有抵抗力。\n'
						'\u3000真是个可恶的家伙……）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('VAR', 4), Insn('CONST', 3), Insn('GE'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#6P#0305F（哦，前半战已经结束了啊。）{wait}'
						'{page}'
						'#0303F（不过，感觉有点危险啊。\n'
						'\u3000连我都知道的问题也给弄错了，\n'
						'\u3000真是不应该啊。）{wait}'
						'{page}'
						'#0309F（不过，稍微笨拙一点，\n'
						'\u3000反而更容易激发出\n'
						'\u3000淑女们的母性本能吧。）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(260), Text(
						'#6P#0300F（哦，前半战已经结束了啊。）{wait}'
						'{page}'
						'#0306F（真是的，别让小鬼们看到\n'
						'\u3000你那么逊的样子啊～）{wait}'
						'{page}'
						'（如果不表现得知性十足，\n'
						'\u3000不就白白浪费了在米修拉姆\n'
						'\u3000发掘的眼镜属性了嘛。）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('0x5A'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (151640, 2100, 12440), 0),
	Insn('CAM_ROTATE', 329, 14, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 30960, 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P……那么，同学们，\n'
		'还有什么问题\n'
		'要问罗伊德老师吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P老师很有耐心，\n'
		'无论有什么问题，他都会为大家解答的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0005F（玛、玛布林老师！？\n'
		'\u3000这太勉强了……）{wait}'
		'{page}'
		'#0006F（……呼，看来也只有硬着头皮上了。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}提问时间到！\n'
		'～学生们会提出平时产生的任何疑问～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}※请选择正确的答案，\n'
		'解答各种棘手的问题！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F……那么，有人要提问吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(15), 0, 1700, (38, 38, 250, 1)),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P我、我！\n'
		'我有问题！我有问题！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (149370, 1500, 14370), 2000),
	Insn('CHAR_ROTATE', Char(257), 225, 300),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0000F嗯，想问什么呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#6P要怎样才能\n'
		'成为老师这样的警察呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#6P……那个，我倒是并没打算\n'
		'要成为警察啦，一点都没有。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(16), 2),
	Insn('TEXT_TALK', Char(16), Text(
		'#6P等一下啦，泰米尔。\n'
		'这样说太失礼了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0006F啊，没关系啦……{wait}'
		'{page}'
		'#0000F这个问题是指，想成为警察\n'
		'是否需要获得某些特别的资格吗？{wait}'
		'{page}'
		'这个嘛，要成为警察的话……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'要成为警察的话，\n'
		'该怎么做呢？{0x18}{wait}'
	)),
	Insn('MENU', 0, -1, 150, 0, Text(
		'【①通过搜查官考试】\n'
		'【②从警察学校毕业】\n'
		'【③没有特定的方法】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0000F……需要通过\n'
				'搜查官考试。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 53))),
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0006F不、不对……\n'
				'如果只是想成为警察的话，并不是一定要\n'
				'通过搜查官考试……{wait}'
				'{page}'
				'#0000F基本来说，只要\n'
				'修完警察学校的全套课程，\n'
				'就有成为警察的资格了。{wait}'
				'{page}'
				'虽然也有像我的同伴这样，\n'
				'没有去过警察学校就直接当上警察的……\n'
				'不过，那也算是非常特殊的例子了。{wait}'
				'{page}'
				'#0006F（真、真是危险啊，\n'
				'\u3000差一点就说错了。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0000F……需要从\n'
				'警察学校毕业。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0000F基本来说，只要\n'
				'修完警察学校的全套课程，\n'
				'就有成为警察的资格了。{wait}'
				'{page}'
				'但是，刚才也说过了，\n'
				'根据职能的不同，警察分为多个部门。{wait}'
				'{page}'
				'比如说，想要成为搜查官的话，\n'
				'除了修完警察学校的所有课程之外，\n'
				'还必须要另外通过搜查官考试。{wait}'
				'{page}'
				'虽然也有像我的同伴这样，\n'
				'没有去过警察学校就直接当上警察的……\n'
				'不过，那也算是非常特殊的例子了。{wait}'
				'{page}'
				'#0004F（嗯，大概就是这个样子吧。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('BREAK'),
		],
		2: [
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0000F……实际上，\n'
				'并没有特定的方法。{wait}'
			)),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 53))),
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0006F不、不对……\n'
				'我的同伴确实没有上过警察学校，\n'
				'就直接成为了警察……{wait}'
				'{page}'
				'#0000F但一般来说，只有\n'
				'修完警察学校的全套课程，\n'
				'才可以成为警察。{wait}'
				'{page}'
				'还有，刚才也已经说过了，\n'
				'警察按职能划分为各式各样的部门。{wait}'
				'{page}'
				'比如说，想要成为搜查官的话，\n'
				'除了修完警察学校的所有课程之外，\n'
				'还必须要另外通过搜查官考试。{wait}'
				'{page}'
				'#0006F（唔，稍微有点混乱吧……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('CHAR_SET_FRAME', Char(16), 0),
	Insn('TEXT_TALK', Char(15), Text(
		'#6P哼～原来如此。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#6P虽然我并没打算成为警察……\n'
		'但还是谢谢你告诉我，老师！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#5P啊，那么……\n'
		'我也可以提一个问题吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (152570, 1200, 14810), 2000),
	Insn('CHAR_ROTATE', Char(257), 135, 300),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0000F嗯，是什么呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#12P上次在克洛斯贝尔发生的事件，\n'
		'总觉得报道得不怎么详细，\n'
		'所以我不是很明白……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#12P关于之前发生的那起\n'
		'狼型魔兽事件，最后解决它的\n'
		'关键是什么呢？？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0005F啊，就是黑手党滥用军犬的\n'
		'那次事件啊。{wait}'
		'{page}'
		'#0003F我记得，将那次事件\n'
		'解决的关键是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'解决军犬事件的关键是？{0x18}{wait}'
	)),
	Insn('MENU', 0, -1, 150, 0, Text(
		'【①特务支援课的推理】\n'
		'【②白狼的帮助】\n'
		'【③警备队的支援】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0000F……是特务支援课的推理。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 53))),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0006F啊，但是……\n'
				'在最后关头，是靠赛特\n'
				'才将我们从危机中解救出来的。{wait}'
				'{page}'
				'要是没有它的话，\n'
				'得知真相的我们恐怕凶多吉少，\n'
				'事件也没法得到解决……{wait}'
				'{page}'
				'#0000F也就是说，解决事件的关键\n'
				'应该还是赛特和它带领的\n'
				'那些白狼吧。{wait}'
				'{page}'
				'#0006F（嗯……\n'
				'\u3000刚才的回答真是对不起赛特啊。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0000F……是白狼的帮助哦。{wait}'
				'{page}'
				'在我们只差一步就要\n'
				'被那些军犬干掉的时候，\n'
				'白狼率领狼群前来救援了。{wait}'
				'{page}'
				'在那之后，由于某些原因，\n'
				'狼群中的赛特\n'
				'就留在了特务支援课。{wait}'
				'{page}'
				'#0004F（因为那实在是太具有冲击性了……\n'
				'\u3000所以没法忘记呢。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('BREAK'),
		],
		2: [
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0000F……是警备队的支援。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 53))),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0005F嗯……？虽然最后确实\n'
				'是交给了警备队……\n'
				'但解决的关键应该在那之前吧。{wait}'
				'{page}'
				'#0000F是赛特它们将我们从\n'
				'那场令人绝望的危机中解救出来的，\n'
				'所以我们才能顺利将犯人逮捕。{wait}'
				'{page}'
				'#0006F（唔唔，\n'
				'\u3000似乎搞错了呢……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('TEXT_TALK', Char(21), Text(
		'#12P嘿……赛特果然\n'
		'好厉害啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#12P谢谢你，大哥哥。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(17), 0, 1700, (38, 38, 250, 1)),
	Insn('TEXT_TALK', Char(17), Text(
		'#6P#N那、那个……老师，\n'
		'我、我也有问题……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('CAM_OFFSET', (153270, 1500, 12030), 2000),
	Insn('CAM_DISTANCE', 30650, 2000),
	Insn('CAM_ROTATE', 327, 8, 0, 2000),
	Insn('0x6F', b'y'),
	Insn('CHAR_ROTATE', Char(257), 135, 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0000F嗯，是什么呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(17), Text(
		'#6P那个，之前\n'
		'龙跟安里\n'
		'在地下迷路了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(17), Text(
		'#6P那里是什么地方呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 500),
	Insn('CHAR_ROTATE', Char(35), 90, 0),
	Insn('CHAR_SET_FRAME', Char(35), 2),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(35), Text(
		'#5P笨蛋……小桃！\n'
		'别提那种让我丢脸的事啊～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(17), 0, 1700, (40, 43, 100, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(17)),
	Insn('TEXT_TALK', Char(17), Text(
		'#6P因、因为，\n'
		'你们都不肯告诉我啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0000F是发生在地下区域的那次事件吗……{wait}'
		'{page}'
		'#0003F孩子们误闯进去的是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'龙与安里\n'
		'误闯进去的地方是？{0x18}{wait}'
	)),
	Insn('MENU', 0, -1, 150, 0, Text(
		'【①地下区域丄Ａ区块】\n'
		'【②地下区域丄Ｂ区块】\n'
		'【③地下区域丄Ｃ区块】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0000F……是地下区域丄Ａ区块。{wait}'
				'{page}'
				'那个时候有魔兽出现，情况相当危险呢，\n'
				'幸好有亚里欧斯先生救援，\n'
				'大家才能平安无事地全部返回。{wait}'
				'{page}'
				'#0004F（嗯，似乎没有问题。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0000F……是地下区域丄Ｂ区块。{wait}'
				'{page}'
				'#0005F……嗯？\n'
				'好像不对……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 53))),
			Insn('TEXT_TALK', Char(21), Text(
				'#12P咦？好像是Ａ区块吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0012F是、是那样吗？{wait}'
				'{page}'
				'#0003F那、那个，总之……\n'
				'当时多亏有亚里欧斯先生帮忙，\n'
				'大家才能平安无事地全部返回。{wait}'
				'{page}'
				'#0006F（对了，Ｂ区块是\n'
				'\u3000约纳所在的地方……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		2: [
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0000F……是地下区域丄Ｃ区块。{wait}'
				'{page}'
				'#0005F……咦，我们\n'
				'去过Ｃ区块吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 53))),
			Insn('TEXT_TALK', Char(21), Text(
				'#12P咦？好像是Ａ区块吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0012F是、是那样吗？{wait}'
				'{page}'
				'#0003F那、那个，总之……\n'
				'当时多亏有亚里欧斯先生帮忙，\n'
				'大家才能平安无事地全部返回。{wait}'
				'{page}'
				'#0006F（嗯，记忆\n'
				'\u3000好像有点模糊了……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('TEXT_TALK', Char(17), Text(
		'#6P嘿嘿……\n'
		'老师，谢谢你。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(35), 0, 1700, (14, 15, 250, 2)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CROSSFADE', 500),
	Insn('CHAR_SET_FRAME', Char(35), 0),
	Insn('CHAR_ROTATE', Char(35), 0, 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0000F……那么，还有其它问题吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(35), 0, 1700, (38, 38, 250, 1)),
	Insn('TEXT_TALK', Char(35), Text(
		'#6P老师！我想到了一个问题！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (152480, 1500, 13840), 2000),
	Insn('CAM_DISTANCE', 29120, 2000),
	Insn('CHAR_ROTATE', Char(257), 135, 300),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0000F好的，请说。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(35), Text(
		'#6P这个问题我以前就想问了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(35), Text(
		'#6P像哥哥们这样的警察组织，\n'
		'跟游击士协会有什么区别呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(35), Text(
		'#6P你们不都是\n'
		'抓坏人的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0003F（来了个比较棘手的问题呢……）{wait}'
		'{page}'
		'#0000F（嗯，但是大家都很在意，\n'
		'\u3000就趁这个机会说清楚吧。）{wait}'
		'{page}'
		'#0003F我们警察与游击士的\n'
		'本质区别是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'警察与游击士的\n'
		'本质区别是？{0x18}{wait}'
	)),
	Insn('MENU', 0, -1, 150, 0, Text(
		'【①是否有逮捕权】\n'
		'【②是否有对政府权力的干涉力】\n'
		'【③基本没有】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0000F……大概是逮捕权的有无吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 3)),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0011F不、不对，游击士也有\n'
				'一般的逮捕权力。{wait}'
				'{page}'
				'#0003F──那个，游击士不能\n'
				'直接逮捕国家或\n'
				'自治州的政府要员。{wait}'
				'{page}'
				'当然，在其突然施暴，伤害他人\n'
				'的场合，还是可以无视规定，\n'
				'直接逮捕的。{wait}'
				'{page}'
				'#0001F相对地，\n'
				'警察拥有逮捕政治家\n'
				'以及政府官员的权力……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0004F虽然对你们来说还有点太难了……\n'
				'但简单来说，游击士会被『规章』所约束。{wait}'
				'{page}'
				'正是因为有这个规章的存在，\n'
				'游击士协会\n'
				'才能设立于大陆各国……{wait}'
				'{page}'
				'#0000F──那个，游击士不能\n'
				'直接逮捕国家或\n'
				'自治州的政府要员。{wait}'
				'{page}'
				'当然，在其突然施暴，伤害他人\n'
				'的场合，还是可以无视规定，\n'
				'直接逮捕的。{wait}'
				'{page}'
				'#0003F相对地，\n'
				'警察拥有逮捕政治家\n'
				'以及政府官员的权力……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('BREAK'),
		],
		2: [
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0004F……基本没有。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 3)),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0011F（喂，怎么可能！）{wait}'
				'{page}'
				'#0003F──那个，游击士不能\n'
				'直接逮捕国家或\n'
				'自治州的政府要员。{wait}'
				'{page}'
				'当然，在其突然施暴，伤害他人\n'
				'的场合，还是可以无视规定，\n'
				'直接逮捕的。{wait}'
				'{page}'
				'#0001F相对地，\n'
				'警察拥有逮捕政治家\n'
				'以及政府官员的权力……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('TEXT_TALK', Char(35), Text(
		'#6P哎，但是爸爸\n'
		'总是抱怨警察不好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(35), Text(
		'#6P说他们连贪污的政府官员\n'
		'都逮捕不了，真是没用。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#12P真、真是的，龙。\n'
		'你太失礼了啦～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0006F……嗯。\n'
		'我们的努力还远远不够，这也是事实。{wait}'
		'{page}'
		'#0000F虽说不能立刻解决这些问题，\n'
		'但我们会继续努力的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(35), Text(
		'#6P哦，我也会给你们加油的！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#12P真是的……\n'
		'说得那么嚣张。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 180, 300),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0012F哈哈……\n'
		'嗯，那么，\n'
		'提问就到这里了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(339), 0, 1700, (38, 38, 250, 1)),
	Insn('TEXT_TALK', Char(339), Text(
		'#6P#1109F#N──那个、那个！！\n'
		'琪雅也有问题！有问题！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (153250, 1500, 11180), 2000),
	Insn('CAM_DISTANCE', 29120, 2000),
	Insn('CHAR_ROTATE', Char(257), 135, 300),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0011F琪、琪雅……！？\n'
		'（本来还以为她肯乖乖待着呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#6P#1105F喂，我可以提问吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0000F嗯，可以啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#6P#1110F那个，罗伊德……{wait}'
		'{page}'
		'你为什么要成为警察呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0005F（啊……）{wait}'
		'{page}'
		'#0003F那、那个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0008F（来到特务支援课的第一天晚上……\n'
		'\u3000好像也思考过类似的事情呢。）{wait}'
		'{page}'
		'#0004F（……嗯，我觉得如今\n'
		'\u3000已经可以回答这个问题了。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(339), 0, 1700, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(339), Text(
		'#6P#1105F罗伊德？怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0002F……不，没什么。{wait}'
		'{page}'
		'#0003F（这个问题，\n'
		'\u3000肯定没有『正确的答案』。）{wait}'
		'{page}'
		'（只有将自己在支援课逐渐产生的\n'
		'\u3000真实心情坦率地告诉大家……\n'
		'\u3000以此作为回答。）{wait}'
		'{page}'
		'#0000F我成为警察的理由，\n'
		'就是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'罗伊德成为警察的理由是？{0x18}{wait}'
	)),
	Insn('MENU', 0, -1, 150, 0, Text(
		'【①想要变强】\n'
		'【②想要守护大家】\n'
		'【③自己也不知道】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0003F嗯，到底该怎么回答呢？\n'
				'有点让人犹豫呢……{wait}'
				'{page}'
				'#0000F大概是因为……\n'
				'想要帮助有困难的人，\n'
				'以及阻止做坏事的人吧。{wait}'
				'{page}'
				'#0008F为了做到那点，\n'
				'我自己也必须变强……{wait}'
				'{page}'
				'要想实现这个愿望的话，\n'
				'对我来说，就只有成为警察了……{wait}'
				'{page}'
				'#0012F……哈哈，但那样一来，\n'
				'似乎跟游击士没有什么区别呢。{wait}'
				'{page}'
				'#0006F对不起……\n'
				'我好像没法回答得很清楚。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(339), Text(
				'#6P#1104F嗯，但琪雅好像还是明白了什么。{wait}'
				'{page}'
				'#1110F罗伊德一定有\n'
				'自己的理由吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0002F哈哈……嗯，\n'
				'那倒是没错。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0003F嗯，到底该怎么回答呢？\n'
				'有点让人犹豫呢……{wait}'
				'{page}'
				'#0000F大概是因为……\n'
				'想要守护大家吧。{wait}'
				'{page}'
				'#0008F朋友和家人自不必说，\n'
				'不过，我所指的大家并不仅限于此，\n'
				'该说是……{wait}'
				'{page}'
				'克洛斯贝尔的市民吗？\n'
				'不，也不单是那样……{wait}'
				'{page}'
				'#0006F……对不起……\n'
				'我好像没法回答得很清楚。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(339), Text(
				'#6P#1104F嗯，但琪雅好像还是明白了什么。{wait}'
				'{page}'
				'#1110F罗伊德一定有\n'
				'自己的理由吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0002F哈哈……嗯，\n'
				'那倒是没错。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		2: [
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0006F老实说……\n'
				'我现在，还不是很清楚。{wait}'
				'{page}'
				'#0008F一开始，只是想\n'
				'追赶上自己的目标，\n'
				'所以才想像那个人一样成为警察的……{wait}'
				'{page}'
				'但现在认真想想的话，\n'
				'其实理由并不只是那样……{wait}'
				'{page}'
				'#0003F当然，想要超越大哥的\n'
				'这份心情还是没有改变，\n'
				'但也并不只是单纯的想要超越他……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
			Insn('SLEEP', 1500),
			Insn('EMOTE_STOP', Char(257)),
			Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 3)),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(257), Text(
				'#11P#0011F对、对不起，各位。\n'
				'好像对你们说了些奇怪的话。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(339), Text(
				'#6P#1110F嗯，但琪雅好像还是明白了什么。{wait}'
				'{page}'
				'#1109F罗伊德一定有\n'
				'自己的理由吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0002F哈哈……\n'
				'谢谢你，琪雅。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('CAM_OFFSET', (151640, 2100, 12440), 2000),
	Insn('CAM_ROTATE', 329, 14, 0, 2000),
	Insn('CAM_DISTANCE', 30960, 2000),
	Insn('CHAR_ROTATE', Char(257), 180, 300),
	Insn('0x6F', b'y'),
	Insn('CHAR_ROTATE', Char(12), 135, 300),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P呵呵……好了，提问\n'
		'就到这里吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P那么，罗伊德老师的课\n'
		'就此结束。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P同学们，请向老师表示感谢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 150, -1, -1),
	Insn('TEXT_SET_NAME', Translate('小孩子们')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 0}#5S谢谢老师～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0000F哈哈……那么，再见了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('CHAR_SET_CHCP', Char(339), 255),
	Insn('CHAR_SET_FRAME', Char(339), 0),
	Insn('CHAR_FLAG1_UNSET', Char(339), 4),
	Insn('0xD5', 30),
	Insn('RETURN'),
]

data['code'][49] = [
	Insn('0x95', Char(254), (151000, 200, 17500), 2000, 0),
	Insn('CHAR_ROTATE', Char(254), 180, 300),
	Insn('RETURN'),
]

data['code'][50] = [
	Insn('CHAR_ROTATE', Char(254), 270, 300),
	Insn('0x98', Char(254), (-1500, 0, 0), 2000, 0),
	Insn('CHAR_ROTATE', Char(254), 180, 300),
	Insn('RETURN'),
]

data['code'][51] = [
	Insn('CAM_OFFSET', (7710, 2300, -90), 0),
	Insn('CAM_ROTATE', 315, 25, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 26410, 0),
	Insn('CHAR_SET_POS', Char(12), (7600, 0, 1320), 270),
	Insn('CHAR_SET_POS', Char(257), (5570, 0, 1350), 90),
	Insn('CHAR_SET_POS', Char(239), (4380, 0, 2050), 90),
	Insn('CHAR_SET_POS', Char(339), (4720, 0, 510), 90),
	Insn('SLEEP', 500),
	Insn('BGM_PLAY', b'|\x00\x00'),
	Insn('CAM_DISTANCE', 25410, 1000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('IF', [
		(Expr([Insn('VAR', 4), Insn('CONST', 9), Insn('GE'), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'#12P辛苦了，罗伊德，\n'
				'今天真是谢谢了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#12P孩子们好像也都\n'
				'听得很开心。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0009F哈哈……\n'
				'如果真是那样就好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#12P呵呵，没必要那么谦虚哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#12P你教得非常不错了，\n'
				'连我都学到了很多东西呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#12P看到站在讲台上的你，\n'
				'感觉到你的成长，\n'
				'真是比什么都要高兴。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('QUEST', 39, Insn('TASK_SET', 1)),
		]),
		(Expr([Insn('VAR', 4), Insn('CONST', 7), Insn('GE'), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'#12P辛苦了，罗伊德，\n'
				'今天真是谢谢了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#12P孩子们好像也都\n'
				'听得很开心。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0000F哈哈……\n'
				'如果真是那样就好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#12P呵呵，我也\n'
				'学到了很多东西呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#12P看到站在讲台上的你，\n'
				'感觉到你的成长，\n'
				'真是比什么都要高兴。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('QUEST', 39, Insn('TASK_SET', 2)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(12), Text(
				'#12P辛苦了，罗伊德，\n'
				'今天真是谢谢了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#12P但是，你的学习似乎\n'
				'有点不足呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0006F那、那个……\n'
				'真是对不起。{wait}'
				'{page}'
				'我为自己的知识不足\n'
				'而感到十分羞愧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#12P不，在那么忙的时候还麻烦你，\n'
				'是我考虑不周呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('QUEST', 39, Insn('TASK_SET', 3)),
		]),
	]),
	Insn('CHAR_WATCH', Char(339), Char(257), 500),
	Insn('TEXT_TALK', Char(339), Text(
		'#5P#1109F琪雅觉得罗伊德上的课\n'
		'很有趣哦！{wait}'
		'{page}'
		'#1100F虽然你说的大部分话\n'
		'都不太能听懂。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(339), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 239, 1, [
		Insn('CHAR_WATCH', Char(254), Char(339), 500),
	]),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0003F嗯……对孩子来说，\n'
		'这些东西果然还是太难了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 239, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 39, Insn('TASK_GET', 3))), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#5P#0103F真是的，必须得再加把劲了。{wait}'
						'{page}'
						'#0111F虽然出了那么多丑，\n'
						'不过，从某种意义上来说，\n'
						'孩子们反而会觉得警察更加亲切吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#12P#0006F这、这么说，结果也不算太坏吗。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(258), Text(
						'#5P#0104F呵呵，能够\n'
						'顺利完成，真是太好了。{wait}'
						'{page}'
						'#0100F我想，孩子们对警察的感觉\n'
						'一定比以前更加亲近了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#12P#0004F……嗯，光是能够得到\n'
						'这样的机会，就算是一种收获了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 39, Insn('TASK_GET', 3))), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#5P#0203F……确实是一堂\n'
						'令人深感兴趣的课。{wait}'
						'{page}'
						'#0211F从某种意义上说，倒也让他们\n'
						'感受到警察只是很平易近人的存在了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#12P#0006F这、这么说，结果也不算太坏吗。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(259), Text(
						'#5P#0204F能够顺利结束，\n'
						'真是太好了。{wait}'
						'{page}'
						'#0202F而且似乎也让孩子们\n'
						'对警察留下了一个良好的印象。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#12P#0004F……嗯，光是能够得到\n'
						'这样的机会，就算是一种收获了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 39, Insn('TASK_GET', 3))), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#5P#0306F唉，没想到你竟然把\n'
						'那些乱七八糟的东西教给孩子。{wait}'
						'{page}'
						'#0309F不过，在某种意义上说，\n'
						'也算是在小鬼们的心目中\n'
						'树立了警察的良好形象吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#12P#0006F这、这么说，结果也不算太坏吗。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(260), Text(
						'#5P#0300F算啦，能够顺利结束就好，\n'
						'别想那么多了。{wait}'
						'{page}'
						'#0309F小鬼们似乎\n'
						'对警察留下了\n'
						'很好的印象嘛。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#12P#0004F……嗯，光是能够得到\n'
						'这样的机会，就算是一种收获了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(12), 500),
	]),
	Insn('FORK', 239, 1, [
		Insn('CHAR_WATCH', Char(254), Char(12), 500),
	]),
	Insn('FORK', 339, 1, [
		Insn('CHAR_WATCH', Char(254), Char(12), 500),
	]),
	Insn('TEXT_TALK', Char(12), Text(
		'#12P……那么，\n'
		'我还要回去上课，\n'
		'就先失陪了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#12P琪雅，\n'
		'如果方便的话，\n'
		'以后也请来主日学校哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#12P其他的孩子们\n'
		'肯定也会欢迎你的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#5P#1110F嗯！今天虽然很忙……\n'
		'但以后一定还会再来的～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0000F（哈哈……琪雅似乎\n'
		'\u3000很喜欢主日学校呢。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 39, Insn('TASK_GET', 1))), Insn('END')]), [
			Insn('QUEST_BONUS_DP', 39, 3),
			Insn('TEXT_TALK', Char(12), Text(
				'#12P呵呵，我会期待你的到来哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#12P……对了对了，罗伊德\n'
				'你能收下这个吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FADE_ON', 300, Color(0x00000000), 100),
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('SOUND_PLAY', 17, 0, 0, 100),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'收下了{item 97}{color 0}。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('0x5A'),
			Insn('ITEM_ADD', 97, 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0005F您太客气了……真的可以收下吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#12P你已经很忙了，但还是抽空给我们上了\n'
				'一堂如此精彩的课，这只是谢礼而已。\n'
				'不要客气，请收下吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#12P……那么，再见了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(12), Text(
				'#12P呵呵，我会期待你的到来哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'#12P那么，再见了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('FORK_FUNC', Char(12), 3, Function((0, 52))),
	Insn('FORK_AWAIT', Char(12), 3),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0003F……好了，\n'
		'稍微耗去了\n'
		'一点时间……{wait}'
		'{page}'
		'#0000F差不多也该去医院了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#5P#0100F说得也是哦，\n'
				'我们快点去\n'
				'南出口的巴士站吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#5P#0200F……说得也是呢，\n'
				'我们快点去\n'
				'南出口的巴士站吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#5P#0300F是啊，\n'
				'我们快点去\n'
				'南出口的巴士站吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(339), Text(
		'#5P#1110F嗯，走吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 9, 0, 0, 100),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}任务【主日学校的特别讲师】{color 0}完成！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('CHAR_SET_POS', Char(0), (5570, 0, 1350), 90),
	Insn('CHAR_SET_POS', Char(12), (150800, 200, 17500), 180),
	Insn('QUEST', 39, Insn('FLAG_UNSET', 16)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][52] = [
	Insn('FORK', 12, 1, [
		Insn('0x95', Char(254), (8600, 0, 1320), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(12), 1),
	Insn('FORK', 12, 1, [
		Insn('0x95', Char(254), (8600, 0, 2600), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(12), 1),
	Insn('FORK', 12, 1, [
		Insn('0x95', Char(254), (11600, 0, 2600), 2000, 0),
	]),
	Insn('SLEEP', 1000),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('FORK', 12, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(12), 1),
	Insn('RETURN'),
]

data['code'][53] = [
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('RETURN'),
]

data['code'][54] = [
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE', Char(16), 0, 1700, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(28), 0, 1700, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('CHAR_SET_FRAME', Char(27), 2),
	Insn('SLEEP', 200),
	Insn('CHAR_SET_FRAME', Char(35), 2),
	Insn('SLEEP', 300),
	Insn('EMOTE', Char(21), 0, 1700, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('CHAR_SET_FRAME', Char(21), 1),
	Insn('SLEEP', 200),
	Insn('EMOTE', Char(17), 0, 1700, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('RETURN'),
]

data['code'][55] = [
	Insn('EMOTE_STOP', Char(65535)),
	Insn('CHAR_SET_FRAME', Char(35), 0),
	Insn('CHAR_SET_FRAME', Char(21), 0),
	Insn('CHAR_SET_FRAME', Char(27), 0),
	Insn('RETURN'),
]
