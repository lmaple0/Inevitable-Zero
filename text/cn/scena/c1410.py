# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'c1410',
	'name2': 'c1410',
	'location': 117,
	'bgm': 117,
	'flags': 8192,
	'includes': [
		'c1410',
		None,
		't1500_1',
		None,
		None,
		None,
	],
	'name3': 'c1410',
	'labels': [],
	'chcp': [
		'chr/ch00400',
		'chr/ch06700',
		'chr/ch30900',
		'chr/ch31800',
		'apl/ch50016',
		'chr/ch24500',
		'chr/ch21300',
		'chr/ch09202',
		'chr/ch20500',
		'chr/ch21000',
		'chr/ch24502',
		'chr/ch21302',
		'chr/ch23702',
		'chr/ch23602',
		'apl/ch50375',
		'apl/ch50091',
	],
	'npcs': [
		{
			'name': Translate('瓦奇'),
			'pos': (0, 0, 11220),
			'angle': 135,
			'_1': b'\x85\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((0, 5)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('阿巴斯'),
			'pos': (2980, 0, 14779),
			'angle': 180,
			'_1': b'\x05\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('琴兹'),
			'pos': (2950, 29, 6579),
			'angle': 180,
			'_1': b'\x05\x01\x00\x00\x03\x00\x00\x01',
			'function': Function((0, 20)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('贝赛'),
			'pos': (10229, 0, 4409),
			'angle': 90,
			'_1': b'\x05\x01\x00\x00\x02\x00\x00\x02',
			'function': Function((0, 25)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('梁'),
			'pos': (14069, 0, 13409),
			'angle': 270,
			'_1': b'\x05\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 28)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('阿赛尔'),
			'pos': (12770, 0, 15310),
			'angle': 180,
			'_1': b'\x05\x01\x00\x00\x0e\x00\x00\x00',
			'function': Function((0, 34)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('瓦奇'),
			'pos': (-2599, 50, 12600),
			'angle': 0,
			'_1': b'\x05\x01\x00\x00\x04\x00\xff\xff',
			'function': Function((0, 6)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('艾胥莉'),
			'pos': (-479, 150, 12600),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x07\x00\xff\xff',
			'function': Function((0, 38)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('沙丽娜'),
			'pos': (0, 0, 5789),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x08\x00\x00\x00',
			'function': Function((0, 39)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('盖特纳'),
			'pos': (-1269, 0, 12640),
			'angle': 45,
			'_1': b'\x85\x01\x00\x00\t\x00\x00\x00',
			'function': Function((0, 40)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (-1240, 0, 4139),
			'angle': 0,
			'_1': b'\x95\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 41)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (-170, 0, 4019),
			'angle': 315,
			'_1': b'\x85\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((0, 45)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (-2900, 150, 3500),
			'angle': 0,
			'_1': b'\x95\x01\x00\x00\n\x00\xff\xff',
			'function': Function((0, 43)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (-4300, 150, 3500),
			'angle': 0,
			'_1': b'\x95\x01\x00\x00\x0b\x00\xff\xff',
			'function': Function((0, 46)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (3730, 150, 12600),
			'angle': 0,
			'_1': b'\x95\x01\x00\x00\x0c\x00\xff\xff',
			'function': Function((0, 47)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (1559, 150, 12600),
			'angle': 0,
			'_1': b'\x95\x01\x00\x00\r\x00\xff\xff',
			'function': Function((0, 50)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('玻璃杯'),
			'pos': (-2599, 519, 13449),
			'angle': 0,
			'_1': b'v\x01\x00\x00\x0f\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('玻璃杯'),
			'pos': (-479, 540, 13449),
			'angle': 0,
			'_1': b'\xf6\x01\x00\x04\x0f\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
	],
	'monsters': [],
	'triggers': [],
	'objects': [
		{
			'pos': (2590, 0, 13420),
			'range': 1500,
			'bubble_pos': (2980, 1500, 14780),
			'_1': b'~\x00\x00',
			'function': Function((0, 16)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (750, 0, 13420),
			'range': 1500,
			'bubble_pos': (750, 1500, 14770),
			'_1': b'~\x00\x00',
			'function': Function((0, 29)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (750, 0, 13420),
			'range': 1500,
			'bubble_pos': (750, 1500, 14770),
			'_1': b'~\x00\x00',
			'function': Function((0, 35)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00u\x00', Function((0, 3)), Function((0, 4))),
	'code': [None]*61,
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
		Insn('0x95', Char(254), (2970, 30, 4200), 1000, 0),
		Insn('CHAR_ROTATE', Char(254), 90, 300),
		Insn('SLEEP', 5500),
		Insn('0x95', Char(254), (2950, 30, 6580), 1000, 0),
		Insn('0x95', Char(254), (6630, 30, 6580), 1000, 0),
		Insn('CHAR_ROTATE', Char(254), 180, 300),
		Insn('SLEEP', 8500),
		Insn('0x95', Char(254), (2950, 30, 6580), 1000, 0),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('0x95', Char(254), (8850, 20, 2630), 1000, 0),
		Insn('0x95', Char(254), (6340, 20, 2420), 1000, 0),
		Insn('CHAR_ROTATE', Char(254), 0, 300),
		Insn('SLEEP', 5000),
		Insn('0x95', Char(254), (8850, 20, 2630), 1000, 0),
		Insn('0x95', Char(254), (10230, 0, 4410), 1000, 0),
		Insn('CHAR_ROTATE', Char(254), 90, 300),
		Insn('SLEEP', 3200),
		Insn('0x95', Char(254), (8850, 20, 2630), 1000, 0),
		Insn('0x95', Char(254), (5070, 20, 2420), 1000, 0),
		Insn('CHAR_ROTATE', Char(254), 315, 300),
		Insn('SLEEP', 5000),
		Insn('0x95', Char(254), (8850, 20, 2630), 1000, 0),
		Insn('0x95', Char(254), (10230, 0, 4410), 1000, 0),
		Insn('CHAR_ROTATE', Char(254), 90, 300),
		Insn('SLEEP', 3200),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(528)), Insn('FLAG', Flag(529)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x09', 268435456),
			Insn('EVENT', Function((0, 51))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(13), (-4000, 0, 16690), 0),
		]),
		(Expr([Insn('FLAG', Flag(1569)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(12), (1070, 0, 15400), 270),
			Insn('CHAR_SET_POS', Char(13), (-300, 0, 15400), 90),
			Insn('CHAR_FLAG1_SET', Char(12), 16),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(13), 16),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1669)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(14), 128),
					Insn('CHAR_FLAG1_SET', Char(24), 128),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(13), 128),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(13), (-4000, 0, 16690), 0),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(10), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(25), 128),
			Insn('CHAR_SET_FRAME', Char(15), 1),
			Insn('CHAR_SET_FRAME', Char(14), 2),
			Insn('CHAR_SET_POS', Char(13), (-4000, 0, 16690), 0),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(14), 128),
			Insn('CHAR_FLAG1_SET', Char(10), 128),
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_FLAG1_SET', Char(13), 128),
			Insn('CHAR_FLAG1_SET', Char(24), 128),
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(20), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
			Insn('CHAR_FLAG1_UNSET', Char(22), 128),
			Insn('CHAR_FLAG1_UNSET', Char(23), 128),
			Insn('CHAR_SET_FRAME', Char(22), 1),
			Insn('CHAR_SET_FRAME', Char(23), 2),
			Insn('CHAR_SET_POS', Char(12), (10230, 0, 4410), 90),
			Insn('CHAR_SET_POS', Char(17), (2950, 30, 6580), 180),
			Insn('FORK_FUNC', Char(12), 0, Function((0, 2))),
			Insn('FORK_FUNC', Char(17), 0, Function((0, 1))),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(9), 128),
			Insn('CHAR_FLAG1_SET', Char(13), 128),
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(22), 128),
			Insn('CHAR_FLAG1_UNSET', Char(23), 128),
			Insn('CHAR_SET_FRAME', Char(22), 1),
			Insn('CHAR_SET_FRAME', Char(23), 2),
			Insn('CHAR_SET_POS', Char(10), (-1730, 0, 6920), 0),
			Insn('CHAR_SET_POS', Char(12), (750, 0, 14770), 180),
			Insn('CHAR_SET_POS', Char(17), (2950, 30, 6580), 180),
			Insn('CHAR_FLAG1_SET', Char(18), 16),
			Insn('CHAR_FLAG1_SET', Char(19), 16),
			Insn('CHAR_SET_POS', Char(18), (-2600, 0, 10330), 0),
			Insn('CHAR_SET_POS', Char(19), (-1200, 0, 10360), 315),
			Insn('FORK_FUNC', Char(10), 0, Function((0, 0))),
			Insn('FORK_FUNC', Char(17), 0, Function((0, 1))),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(17), 16),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(14), 128),
			Insn('CHAR_FLAG1_SET', Char(9), 128),
			Insn('CHAR_FLAG1_SET', Char(13), 128),
			Insn('CHAR_FLAG1_SET', Char(24), 128),
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(22), 128),
			Insn('CHAR_FLAG1_UNSET', Char(23), 128),
			Insn('CHAR_SET_POS', Char(10), (0, 0, 7400), 180),
			Insn('CHAR_SET_POS', Char(11), (1000, 0, 7720), 225),
			Insn('CHAR_SET_POS', Char(12), (750, 0, 14770), 180),
			Insn('CHAR_SET_POS', Char(18), (0, 0, 5790), 0),
			Insn('CHAR_SET_POS', Char(19), (680, 0, 5200), 0),
			Insn('FORK_FUNC', Char(10), 0, Function((0, 0))),
			Insn('FORK_FUNC', Char(11), 0, Function((0, 0))),
			Insn('CHAR_FLAG1_SET', Char(11), 16),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(10), 16),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(17), 16),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(10), 128),
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('CHAR_FLAG1_SET', Char(19), 16),
			Insn('CHAR_SET_POS', Char(13), (750, 0, 14770), 180),
		]),
		(Expr([Insn('FLAG', Flag(1281)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(14), 128),
			Insn('CHAR_FLAG1_SET', Char(9), 128),
			Insn('CHAR_FLAG1_SET', Char(10), 128),
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_FLAG1_SET', Char(12), 128),
			Insn('CHAR_FLAG1_SET', Char(13), 128),
			Insn('CHAR_FLAG1_SET', Char(24), 128),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(14), 128),
			Insn('CHAR_FLAG1_SET', Char(24), 128),
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
			Insn('CHAR_SET_POS', Char(9), (1160, 0, 10170), 315),
			Insn('CHAR_SET_POS', Char(10), (2840, 30, 8000), 270),
			Insn('CHAR_SET_POS', Char(11), (1350, 0, 8000), 90),
			Insn('CHAR_SET_POS', Char(12), (-750, 0, 7000), 0),
			Insn('CHAR_SET_POS', Char(13), (-750, 0, 8500), 180),
			Insn('FORK_FUNC', Char(10), 0, Function((0, 0))),
			Insn('FORK_FUNC', Char(11), 0, Function((0, 0))),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(8), 16),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(12), 16),
					Insn('CHAR_FLAG1_SET', Char(13), 16),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(13), (-4000, 0, 16690), 0),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(25), 128),
			Insn('CHAR_SET_FRAME', Char(15), 1),
			Insn('CHAR_SET_FRAME', Char(14), 2),
			Insn('CHAR_SET_POS', Char(13), (-4000, 0, 16690), 0),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(9), (-4000, 0, 16690), 0),
					Insn('CHAR_SET_POS', Char(13), (-350, 0, 14760), 180),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
							Insn('CHAR_FLAG1_SET', Char(13), 16),
						]),
						(None, []),
					]),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(13), (-4000, 0, 16690), 0),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(13), (-4000, 0, 16690), 0),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_SET', Char(16), 16),
			Insn('CHAR_SET_POS', Char(13), (0, 0, 7400), 180),
			Insn('CHAR_SET_CHCP', Char(13), 2),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('CHAR_SET_CHCP', Char(13), 2),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(13), 128),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(627)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(10), 16),
				]),
				(None, []),
			]),
		]),
		(None, [
			Insn('CHAR_FLAG1_SET', Char(13), 128),
		]),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('IF', [
		(Expr([Insn('ATTR', 4), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
			Insn('EXIT_SET_ENABLED', 0, 0),
			Insn('EXIT_SET_ENABLED', 1, 1),
		]),
		(None, [
			Insn('EXIT_SET_ENABLED', 0, 1),
			Insn('EXIT_SET_ENABLED', 1, 0),
		]),
	]),
	Insn('0x65', 1, 1),
	Insn('0x65', 2, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('0x65', 0, 1),
			Insn('0x66', 1, 1),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('0x65', 0, 1),
			Insn('0x66', 1, 1),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('0x66', 2, 1),
		]),
		(Expr([Insn('FLAG', Flag(1281)), Insn('END')]), [
			Insn('0x65', 0, 1),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('0x65', 0, 1),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('0x65', 0, 1),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
			Insn('0x4B', Char(9), -1),
			Insn('TEXT_TALK', Char(8), Text(
				'#0404F阿巴斯，难得的好日子，\n'
				'我们就来干一杯吧。{wait}'
				'{page}'
				'#0400F呵呵，毕竟是歌颂\n'
				'克洛斯贝尔的重要节日啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x4C', Char(9), -1),
		]),
		(None, [
			Insn('TEXT_TALK', Char(8), Text(
				'#0404F我们正在商量今天要不要\n'
				'一起去参观纪念庆典呢。{wait}'
				'{page}'
				'#0400F……对了，你们也一起来如何？\n'
				'肯定会很开心的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0003F还是免了，不好意思，因为我们正在执勤。{wait}'
				'{page}'
				'#0001F对了，瓦奇，你是明知如此，\n'
				'还故意邀请我们的吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#0409F啊哈哈！\n'
				'你可真够死脑筋的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_ROTATE', Char(8), 135, 0),
			Insn('CHAR_FLAG1_SET', Char(8), 16),
			Insn('FLAG_SET', Flag(0)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
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
		(Expr([Insn('FLAG', Flag(10)), Insn('END')]), [
			Insn('TEXT_TALK', Char(14), Text(
				'#0400F（关于阿巴斯这个人，\n'
				'\u3000其实我也了解得不是很详细。）{wait}'
				'{page}'
				'（据说，他好像出身于\n'
				'\u3000塞姆利亚大陆中东部。）{wait}'
				'{page}'
				'（呵呵……\n'
				'\u3000总之他很喜欢给自己找事，这倒是不用怀疑的。）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1793)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
					Insn('TEXT_TALK', Char(14), Text(
						'#0400F太阳都快下山了啊。{wait}'
						'{page}'
						'虽然不知道你们要去哪，\n'
						'但还是早点出发比较好吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(14), Text(
						'#0404F……………………………………{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F瓦奇，怎么了？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(14), Text(
						'#0400F……没什么，说起来，\n'
						'今晚好像是满月呢。{wait}'
						'{page}'
						'#0402F今天的天空很晴朗，\n'
						'应该能看到美丽的月亮吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F是啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F但月亮不是\n'
						'不吉利的象征么……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0303F……在如今这种状况下，\n'
						'实在是开心不起来呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
					Insn('TEXT_TALK', Char(14), Text(
						'#0400F算了，至于剑蛇帮那边，\n'
						'我们也会留意的。{wait}'
						'{page}'
						'你们只要做好\n'
						'自己的工作就可以了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(14), Text(
						'#0403F瓦鲁多好像也\n'
						'开始焦虑起来了呢。{wait}'
						'{page}'
						'#0400F……他要是能把那种固执要强的性格稍微改改，\n'
						'这种时候也就能轻松一些了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F瓦奇，你好像相当\n'
						'关心瓦鲁多啊。{wait}'
						'{page}'
						'#0005F其实，你从一开始就一直\n'
						'很担心剑蛇帮那边的情况吧……？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(14), Text(
						'#0404F呵呵……怎么说呢。{wait}'
						'{page}'
						'#0402F只是，瓦鲁多那个人嘛，\n'
						'有些方面确实是让人放不下心。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1569)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1670)), Insn('END')]), [
					Insn('TEXT_TALK', Char(14), Text(
						'#0400F呵呵，你们竟然在和\n'
						'一课的精英一起行动啊。{wait}'
						'{page}'
						'正在做什么呢……\n'
						'算了，有些事情还是不问为好。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CALL', Function((0, 7))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1601)), Insn('END')]), [
					Insn('TEXT_TALK', Char(14), Text(
						'#0400F如今，除了那个叫迪诺\n'
						'的少年之外，旧市街中似乎\n'
						'就没有其他服用过那种药物的人了。{wait}'
						'{page}'
						'只是，那药物究竟是谁散发出去的，\n'
						'现在还不清楚呢。\n'
						'我们这边也会留意的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(14), Text(
						'#0402F……来了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0001F瓦奇，能拜托你尽快……\n'
						'将情况告诉我们吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(14), Text(
						'#0404F我本来是想先要情报费的，\n'
						'不过这次就算了吧。{wait}'
						'{page}'
						'#0406F毕竟，这件事和我们也不是完全无关……\n'
						'而且情况似乎相当严峻呢。{wait}'
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
					Insn('CALL', Function((0, 8))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1560)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
					Insn('TEXT_TALK', Char(14), Text(
						'#0404F话说回来……仅仅只是袭击，却没有把\n'
						'对方的首领干掉，手法实在是不太干净俐落呢。{wait}'
						'{page}'
						'#0402F如果我是鲁巴彻的人，肯定会想出一些\n'
						'把对方彻底做掉的计划。{wait}'
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
						'#0106F（瓦奇果然是个\n'
						'\u3000危险人物呢……）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(14), Text(
						'#0400F说起来，听说黑月的事务所\n'
						'遭到了袭击呢……{wait}'
						'{page}'
						'#0403F鲁巴彻也真是够乱来的啊。\n'
						'这种行为不就是在明目张胆地\n'
						'邀请对方前来复仇吗。{wait}'
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
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F瓦奇都这么说，确实是很有信服力呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(14), Text(
						'#0400F呵呵，这不是理所当然的嘛。\n'
						'我如果站在黑月的立场上，\n'
						'肯定也会回赠对方一份大礼的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
					Insn('TEXT_TALK', Char(14), Text(
						'#0403F看起来，市区那边似乎\n'
						'也陷入骚乱了呢……{wait}'
						'{page}'
						'#0402F呵呵，难道因为明天是满月，\n'
						'所以大家的热血全都沸腾了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(14), Text(
						'#0403F………………………………{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F瓦奇？怎么了？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(14), Text(
						'#0402F不，没什么……{wait}'
						'{page}'
						'只是有些在意剑蛇帮\n'
						'那边的情况而已。\n'
						'他们昨天晚上好像闹得很凶呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1668)), Insn('END')]), [
					Insn('CHAR_SET_FRAME', Char(14), 0),
					Insn('EXPR_CHAR_ATTR', Char(265), 5, Expr([Insn('CHAR_ATTR', Char(14), 4), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(14), 5, Expr([Insn('CHAR_ATTR', Char(14), 4), Insn('SET'), Insn('END')])),
					Insn('TEXT_START', Char(14)),
					Insn('CHAR_FLAG1_UNSET', Char(14), 16),
					Insn('CHAR_WATCH', Char(14), Char(265), 0),
					Insn('EXPR_CHAR_ATTR', Char(14), 4, Expr([Insn('CHAR_ATTR', Char(14), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(14), 4, Expr([Insn('CHAR_ATTR', Char(14), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(14), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(14), 5, Expr([Insn('CHAR_ATTR', Char(14), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
					Insn('IF', [
						(Expr([Insn('CHAR_ATTR', Char(14), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(14), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(14), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(14), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
						(Expr([Insn('CHAR_ATTR', Char(14), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
							Insn('EXPR_CHAR_ATTR', Char(14), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
						]),
						(Expr([Insn('CHAR_ATTR', Char(14), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
							Insn('EXPR_CHAR_ATTR', Char(14), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
						]),
						(None, [
							Insn('EXPR_CHAR_ATTR', Char(14), 8, Expr([Insn('CHAR_ATTR', Char(14), 5), Insn('SET'), Insn('END')])),
						]),
					]),
					Insn('EXPR_CHAR_ATTR', Char(14), 4, Expr([Insn('CHAR_ATTR', Char(265), 5), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(265), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(14), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
					Insn('CHAR_FLAG1_SET', Char(14), 16),
					Insn('TEXT_TALK', Char(265), Text(
						'#0501F明、明明是个未成年人，\n'
						'竟然在大白天公然喝酒，\n'
						'这可不好吧！？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(14), Text(
						'#0402F啊，这只是普通的果汁而已。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F（又面不改色地说谎……）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CALL', Function((0, 9))),
				]),
			]),
		]),
		(None, [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1409)), Insn('END')]), [
							Insn('TEXT_TALK', Char(14), Text(
								'#0400F#0400F总之，请各位慢慢享受吧。{wait}'
								'{page}'
								'如果有空，三个人\n'
								'一起喝点奶昔如何？{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('CALL', Function((0, 10))),
						]),
					]),
					Insn('TEXT_END', Char(254)),
					Insn('CHAR_SET_FRAME', Char(14), 2),
					Insn('RETURN'),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
							Insn('TEXT_TALK', Char(14), Text(
								'#0406F#0406F别看我现在这样，其实在纪念\n'
								'庆典期间，我也是很忙的哦。{wait}'
								'{page}'
								'#0400F#0400F呵呵，虽然很遗憾，但今天就\n'
								'随便敷衍一下，放她们回去吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('CALL', Function((0, 11))),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1408)), Insn('END')]), [
							Insn('TEXT_TALK', Char(14), Text(
								'#0400F#0400F总之，你们今天也\n'
								'好好放松一下吧。{wait}'
								'{page}'
								'阿巴斯的调酒技术\n'
								'可是十分高超的哦。{wait}'
								'{page}'
								'呵呵，今天的酒单里\n'
								'都是些上乘之品哦。\n'
								'你们也来一杯如何？{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('TEXT_TALK', Char(14), Text(
								'#0404F#0404F呵呵，昨天多谢你们了。{wait}'
								'{page}'
								'#0400F#0400F能跟那对很有名气的游击士二人组同场竞技，\n'
								'而且比赛本身也非常有趣。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0005F#0005F瓦奇你……\n'
								'难道没有疲惫不堪吗？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('EMOTE', Char(14), 0, 2000, (38, 38, 250, 1)),
							Insn('SLEEP', 1000),
							Insn('TEXT_TALK', Char(14), Text(
								'#0405F#0405F哎，疲惫？为什么？\n'
								'难道你是指昨天的竞赛吗？{wait}'
								'{page}'
								'#0402F#0402F啊哈哈，那不是很平常的娱乐活动嘛。{wait}'
								'{page}'
								'平时和瓦鲁多打架，\n'
								'每次也都会那么激烈的。{wait}'
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
							Insn('TEXT_TALK', Char(257), Text(
								'#0003F#0003F（真是不可小看不良少年的体力啊……）{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(260), Text(
								'#0306F#0306F（呼～让我感觉自己已经上了年纪呢……）{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(1408)),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 22))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 20))), Insn('BOOL_AND'), Insn('END')]), [
							Insn('CALL', Function((2, 21))),
						]),
						(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('END')]), [
							Insn('IF', [
								(Expr([Insn('FLAG', Flag(1151)), Insn('END')]), [
									Insn('CALL', Function((0, 13))),
								]),
								(None, [
									Insn('CALL', Function((0, 12))),
								]),
							]),
						]),
						(None, [
							Insn('CALL', Function((0, 13))),
						]),
					]),
				]),
				(None, [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
							Insn('IF', [
								(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 22))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 20))), Insn('BOOL_AND'), Insn('END')]), [
									Insn('CALL', Function((2, 21))),
								]),
								(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('END')]), [
									Insn('IF', [
										(Expr([Insn('FLAG', Flag(1151)), Insn('END')]), [
											Insn('CALL', Function((0, 14))),
										]),
										(None, [
											Insn('CALL', Function((0, 12))),
										]),
									]),
								]),
								(None, [
									Insn('CALL', Function((0, 14))),
								]),
							]),
							Insn('TEXT_END', Char(254)),
							Insn('CHAR_SET_FRAME', Char(14), 2),
							Insn('RETURN'),
						]),
						(None, []),
					]),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
							Insn('IF', [
								(Expr([Insn('FLAG', Flag(1149)), Insn('END')]), [
									Insn('TEXT_TALK', Char(14), Text(
										'#0400F#0400F最近，克洛斯贝尔的黑道势力中\n'
										'好像新加入了一个\n'
										'名叫『黑月』的组织呢。{wait}'
										'{page}'
										'#0400F#0400F近来他们好像在走私管道方面和鲁巴彻\n'
										'一直有些小摩擦。{wait}'
										'{page}'
										'#0406F#0406F哎呀哎呀……\n'
										'只要不要把战火烧到\n'
										'我们这边就好。{wait}'
									)),
									Insn('TEXT_WAIT'),
								]),
								(None, [
									Insn('TEXT_TALK', Char(14), Text(
										'#0400F#0400F最近，克洛斯贝尔的黑道势力中\n'
										'好像新加入了一个\n'
										'名叫『黑月』的组织呢。{wait}'
										'{page}'
										'似乎是来自东方国家呢。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(257), Text(
										'#0000F#0000F嗯，据说是控制着\n'
										'卡尔瓦德东方人街\n'
										'的巨大黑手党组织……{wait}'
										'{page}'
										'#0001F#0001F瓦奇，你了解什么内情吗？{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('EMOTE', Char(14), 0, 2000, (38, 38, 250, 1)),
									Insn('SLEEP', 1000),
									Insn('TEXT_TALK', Char(14), Text(
										'#0405F#0405F……哎？\n'
										'虽然还谈不上了解……{wait}'
										'{page}'
										'#0400F#0400F近来他们好像在走私管道方面和鲁巴彻\n'
										'一直有些小摩擦。{wait}'
										'{page}'
										'虽然鲁巴彻好像暂时落了下风，\n'
										'但也有传闻说，他们已经增强了战斗力。{wait}'
										'{page}'
										'#0406F#0406F战火也许会波及到我们这里，\n'
										'所以要提高警惕。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(257), Text(
										'#0001F#0001F是吗……{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(260), Text(
										'#0301F#0301F不过，你这些情报\n'
										'是从哪里听来的呢？{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(14), Text(
										'#0404F#0404F呵，探听情报虽然\n'
										'不是我的专长。{wait}'
										'{page}'
										'#0402F#0402F但我的交际面\n'
										'毕竟也算很广呢。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('FLAG_SET', Flag(1149)),
								]),
							]),
						]),
						(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
							Insn('IF', [
								(Expr([Insn('FLAG', Flag(1148)), Insn('END')]), [
									Insn('IF', [
										(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
											Insn('TEXT_TALK', Char(14), Text(
												'#0400F#0400F呵呵，最近这段时间，\n'
												'『特务支援课』这个名字\n'
												'似乎也变得广为人知了呢。{wait}'
												'{page}'
												'#0404F#0404F哈，就保持这种势头，继续加油吧。\n'
												'我也很期待你们的表现呢。{wait}'
											)),
											Insn('TEXT_WAIT'),
										]),
										(None, [
											Insn('TEXT_TALK', Char(14), Text(
												'#0400F#0400F呵呵，最近这段时间，\n'
												'『特务支援课』这个名字\n'
												'似乎也变得广为人知了呢。{wait}'
												'{page}'
												'#0409F#0409F不过，真要说的话，其实只是\n'
												'被人当作嘲笑的对象而已呢。\n'
												'啊哈哈哈哈……！{wait}'
											)),
											Insn('TEXT_WAIT'),
											Insn('TEXT_TALK', Char(260), Text(
												'#0303F#0303F……都怪克洛斯贝尔时报周刊，\n'
												'宣传方式太让人不爽了。{wait}'
											)),
											Insn('TEXT_WAIT'),
											Insn('TEXT_TALK', Char(258), Text(
												'#0106F#0106F是啊……{wait}'
											)),
											Insn('TEXT_WAIT'),
											Insn('FLAG_SET', Flag(0)),
										]),
									]),
								]),
								(None, [
									Insn('TEXT_TALK', Char(14), Text(
										'#0400F#0400F哎呀，这不是罗伊德和各位嘛。{wait}'
										'{page}'
										'最近一直都没见到你们，\n'
										'又在调查些什么吗？{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(257), Text(
										'#0000F#0000F不，今天只是在处理一些\n'
										'琐碎的支援请求而已。{wait}'
										'{page}'
										'#0006F#0006F最近也经常跑去总部帮忙呢。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(14), Text(
										'#0404F#0404F呵呵，大概是因为临近纪念庆典，\n'
										'到处都很热闹，所以警察局也很忙吧。{wait}'
										'{page}'
										'#0400F#0400F总之，就保持这种势头，继续加油吧。{wait}'
										'{page}'
										'最近这段时间，克洛斯贝尔时报周刊\n'
										'对你们的评价好像也比以前\n'
										'强了不少呢。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(257), Text(
										'#0003F#0003F嗯，是啊。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(260), Text(
										'#0305F#0305F（话说～这种鼓励的话，为什么是\n'
										'\u3000不良帮派的头目对我们说的啊……）{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('FLAG_SET', Flag(1148)),
								]),
							]),
						]),
						(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
							Insn('IF', [
								(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
									Insn('TEXT_TALK', Char(14), Text(
										'#0400F#0400F哎呀呀……今天差不多\n'
										'也该关门了吧。{wait}'
									)),
									Insn('TEXT_WAIT'),
								]),
								(None, [
									Insn('TEXT_TALK', Char(14), Text(
										'#0406F#0406F哎呀呀……\n'
										'我接下来还有\n'
										'工作哦。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(257), Text(
										'#0000F#0000F工作……？{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(14), Text(
										'#0402F#0402F呵呵，秘丄密丄哦。{wait}'
										'{page}'
										'如果想得到更多的情报，\n'
										'可就必须要付情报费了。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('FLAG_SET', Flag(0)),
								]),
							]),
						]),
						(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
							Insn('IF', [
								(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
									Insn('TEXT_TALK', Char(14), Text(
										'#0403F#0403F白色鬃毛的神狼，守护着\n'
										'钟声响起的宿命之地──\n'
										'……大概是这么说的吧？{wait}'
										'{page}'
										'#0400F#0400F七耀教会的圣典中\n'
										'好像有过这样的记载呢。{wait}'
										'{page}'
										'#0404F#0404F不过，以前从没当真过就是了。{wait}'
									)),
									Insn('TEXT_WAIT'),
								]),
								(None, [
									Insn('TEXT_TALK', Char(14), Text(
										'#0400F#0400F听说克洛斯贝尔的\n'
										'警备队正在山中猎捕\n'
										'狼型的魔兽？{wait}'
										'{page}'
										'#0404F#0404F哼……狼型吗……\n'
										'稍微有些让人在意呢。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(257), Text(
										'#0001F#0001F与其说是在山中猎捕，\n'
										'其实也只是警备巡逻而已吧……{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(260), Text(
										'#0301F#0301F话说～这些奇怪的情报，\n'
										'你到底是从哪里打探来的啊？{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(14), Text(
										'#0404F#0404F呵呵……\n'
										'看来确有其事呢。{wait}'
										'{page}'
										'#0400F#0400F……其实，我只是记得在教会的圣典中\n'
										'有过那样的记载。{wait}'
										'{page}'
										'#0403F#0403F白色鬃毛的神狼，守护着\n'
										'钟声响起的宿命之地──\n'
										'……大概是这么说的吧？{wait}'
										'{page}'
										'#0400F#0400F不过，以前从没当真过就是了。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(257), Text(
										'#0005F#0005F是、是吗……{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(258), Text(
										'#0100F#0100F村长先生的话……\n'
										'还真是意外的\n'
										'准确呢。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('FLAG_SET', Flag(0)),
								]),
							]),
						]),
						(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
							Insn('IF', [
								(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
									Insn('TEXT_TALK', Char(14), Text(
										'#0403F#0403F那天晚上，确实是承蒙\n'
										'你们支援课关照了。{wait}'
										'{page}'
										'#0402F#0402F呵呵，以后要是有什么事，尽管来找我。\n'
										'只要我有兴致，\n'
										'说不定可以助你们一臂之力哦。{wait}'
									)),
									Insn('TEXT_WAIT'),
								]),
								(None, [
									Insn('TEXT_TALK', Char(14), Text(
										'#0405F#0405F哎呀，这不是罗伊德嘛。{wait}'
										'{page}'
										'#0402F#0402F真开心呢……\n'
										'你是来找我的吗？{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
									Insn('SLEEP', 1000),
									Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 0)),
									Insn('SLEEP', 500),
									Insn('TEXT_TALK', Char(257), Text(
										'#0013F#0013F哎！？那个……{wait}'
										'{page}'
										'#0013F#0013F没有什么特别的意思，\n'
										'只是过来道个谢而已……{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('EMOTE_STOP', Char(257)),
									Insn('TEXT_TALK', Char(259), Text(
										'#0211F#0211F罗伊德前辈的反应很不自然，\n'
										'明显心慌了呢。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(14), Text(
										'#0403F#0403F呵呵……不开玩笑了。{wait}'
										'{page}'
										'#0400F#0400F那天晚上，确实是承蒙\n'
										'你们支援课关照了。{wait}'
										'{page}'
										'#0402F#0402F以后要是有什么事，尽管来找我。\n'
										'只要我有兴致，\n'
										'说不定可以助你们一臂之力哦。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(257), Text(
										'#0003F#0003F啊，那到时候就拜托了。\n'
										'（总觉和他说话很累呢……）{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('FLAG_SET', Flag(0)),
								]),
							]),
						]),
						(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
							Insn('IF', [
								(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
									Insn('TEXT_TALK', Char(14), Text(
										'#0404F#0404F我已经向成员们交代过了，\n'
										'让他们不要再擅自\n'
										'做出一些不妥的行动。{wait}'
										'{page}'
										'#0400F#0400F至少在今天一天，\n'
										'应该不会再有什么麻烦了。{wait}'
										'{page}'
										'#0402F#0402F呵呵……要进行调查的话，\n'
										'最好还是应该赶快行动吧？{wait}'
									)),
									Insn('TEXT_WAIT'),
								]),
								(None, [
									Insn('TEXT_TALK', Char(14), Text(
										'#0404F#0404F我已经向成员们交代过了，\n'
										'让他们不要再擅自\n'
										'做出一些不妥的行动。{wait}'
										'{page}'
										'#0400F#0400F至少在今天一天，\n'
										'应该不会再有什么麻烦了。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(257), Text(
										'#0001F#0001F是吗……那可真是多谢了。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(14), Text(
										'#0402F#0402F哈哈……真讨厌啊。\n'
										'我又不是为了你们\n'
										'才约束大家的。{wait}'
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
									Insn('TEXT_TALK', Char(14), Text(
										'#0402F#0402F只是趁现在积蓄一下战斗力，\n'
										'到时候才能去血洗\n'
										'剑蛇帮而已啊。{wait}'
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
									Insn('TEXT_TALK', Char(260), Text(
										'#0306F#0306F（虽然外表很可爱，\n'
										'\u3000但不良少年终究是不良少年呢……）{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('FLAG_SET', Flag(0)),
								]),
							]),
						]),
						(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
							Insn('TEXT_TALK', Char(14), Text(
								'#0400F#0400F呵呵……\n'
								'一定要带些有趣的消息回来啊。{wait}'
								'{page}'
								'短时间之内，\n'
								'我倒是可以在这里等等你们。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('TEXT_TALK', Char(14), Text(
								'#0400F#0400F你是叫罗伊德吧？\n'
								'还真是个很有意思的人。{wait}'
								'{page}'
								'#0402F#0402F呵呵……以后也可以\n'
								'随时来这里玩哦。\n'
								'还有，一定要带些有趣的消息回来啊。{wait}'
								'{page}'
								'短时间之内，\n'
								'我倒是可以在这里等等你们。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(0)),
						]),
					]),
				]),
			]),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('0x4B', Char(9), -1),
	Insn('CAM_OFFSET', (-1760, 1100, 11760), 0),
	Insn('CAM_ROTATE', 45, 30, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 23000, 0),
	Insn('CHAR_SET_POS', Char(257), (-890, 0, 11490), 315),
	Insn('CHAR_SET_POS', Char(258), (-780, 0, 10570), 315),
	Insn('CHAR_SET_POS', Char(259), (-2780, 0, 10550), 0),
	Insn('CHAR_SET_POS', Char(260), (-3990, 0, 10450), 45),
	Insn('CHAR_SET_POS', Char(266), (-1990, 0, 10100), 0),
	Insn('CHAR_SET_POS', Char(14), (-2500, 50, 12400), 135),
	Insn('CHAR_SET_FRAME', Char(14), 0),
	Insn('CHAR_FLAG1_UNSET', Char(4), 128),
	Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
	Insn('0x0D'),
	Insn('EMOTE', Char(14), 0, 1700, (38, 38, 250, 1)),
	Insn('CHAR_SET_FRAME', Char(14), 2),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(14), Text(
		'#0402F哎呀，这不是……\n'
		'你们这次带了稀客过来啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(266), Text(
		'#0603F好久不见了啊，\n'
		'瓦奇丄赫密士菲亚。{wait}'
		'{page}'
		'#0601F你还没打算停止这种\n'
		'无聊的不良少年游戏吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0404F呵呵，同样的话都回答过很多次了，\n'
		'对我来说，其实怎样都无所谓。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(257), Char(266), 350),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(258), Char(266), 350),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(259), Char(266), 350),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(260), Char(266), 350),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#0011F达德利搜查官……\n'
		'你们原来就认识吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(266), Text(
		'#0601F两年前就认识了，那时这小子刚来到旧市街，\n'
		'并建立起这个组织。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0404F呵呵，即使在搜查一课中，\n'
		'他也是唯一一位会定期\n'
		'来旧市街视察的人哦。{wait}'
		'{page}'
		'#0402F不过，这好像也是受\n'
		'我不认识的某人所影响呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F某人……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(266), Text(
		'#0603F无聊的闲话就到此为止吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(266), Char(9), 350),
	Insn('TEXT_TALK', Char(266), Text(
		'#0601F#6P阿巴斯，\n'
		'看好这小子，不要让他对瓦鲁多\n'
		'做出一些无意义的挑衅行为。{wait}'
		'{page}'
		'可不要逼迫我们一课正式介入啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(9), Char(266), 350),
	Insn('TEXT_TALK', Char(9), Text(
		'#04100F……明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(14), 0),
	Insn('TEXT_TALK', Char(14), Text(
		'#0404F哎呀呀。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_POS', Char(0), (-890, 0, 11490), 315),
	Insn('CHAR_SET_POS', Char(14), (-2600, 50, 12600), 0),
	Insn('CHAR_SET_POS', Char(9), (2980, 0, 14780), 180),
	Insn('CHAR_FLAG1_SET', Char(4), 128),
	Insn('CHAR_FLAG2_SET', Char(4), 32768),
	Insn('FLAG_SET', Flag(1670)),
	Insn('0x4C', Char(9), -1),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('EVENT_BEGIN', 0),
	Insn('CAM_OFFSET', (-2940, 1100, 11130), 0),
	Insn('CAM_ROTATE', 51, 30, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 18950, 0),
	Insn('CHAR_SET_POS', Char(257), (-2690, 0, 10450), 360),
	Insn('CHAR_SET_POS', Char(258), (-1410, 0, 10430), 315),
	Insn('CHAR_SET_POS', Char(259), (-4080, 0, 10220), 45),
	Insn('CHAR_SET_POS', Char(260), (-4600, 0, 11800), 90),
	Insn('CHAR_SET_POS', Char(14), (-2690, 50, 12150), 180),
	Insn('CHAR_SET_FRAME', Char(14), 0),
	Insn('CAM_DISTANCE', 19950, 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0403F#5P剑蛇帮新收的那个小跑腿，\n'
		'好像是叫迪诺吧。{wait}'
		'{page}'
		'#0401F他最近的样子好像很奇怪呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1647)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#0303F#6P嗯，我们也有所耳闻。\n'
				'好像是提出和干部单挑，然后把对方给怎么样了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#0402F#5P然后，听说他昨天\n'
				'终于向瓦鲁多发出了挑战。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#0008F#12P果然如此吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#0406F#5P嗯，完全不像是个新人，\n'
				'态度相当傲慢狂暴。{wait}'
				'{page}'
				'#0401F平时也经常会向我们的人\n'
				'挑衅，然后……{wait}'
				'{page}'
				'#0402F昨天他终于主动向\n'
				'瓦鲁多提出单挑了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#0007F#12P啊，和那个瓦鲁多……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0402F#5P正是。{wait}'
		'{page}'
		'#0404F我也只是听说而已，\n'
		'据说他的速度和力量都相当厉害，\n'
		'和瓦鲁多不相上下，打得很精彩呢。{wait}'
		'{page}'
		'据说，瓦鲁多最后拼尽了全力，\n'
		'总算是勉强取胜了……{wait}'
		'{page}'
		'#0400F而迪诺在战败之后，\n'
		'就直接飞奔离去了。\n'
		'今天早上，好像谁都没有见到他。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0306F#6P这真是很危险啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0108F#12P这样的话……\n'
		'事态确实不一般呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(14), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(14)),
	Insn('TEXT_TALK', Char(14), Text(
		'#0404F#5P那么……{wait}'
		'{page}'
		'#0402F果然是某种药物的影响吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#0011F#12P什么……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0105F#12P你是从哪里知道的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0405F#5P啊，果然是真的吗？{wait}'
		'{page}'
		'#0404F最近这段时间，克洛斯贝尔流传着一个都市传说，\n'
		'叫做『可以实现愿望的药』。\n'
		'我就在想，会不会和那个有关。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0211F#6P原来是在套我们的话吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0301F#6P喂，这些事情无论如何\n'
		'也不要到处说啊！{wait}'
		'{page}'
		'毕竟事态有些特殊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0409F#5P呵呵，我当然明白这些。{wait}'
		'{page}'
		'#0400F#5P还好，在这旧市街，\n'
		'除了那个叫迪诺的少年之外，\n'
		'似乎还没有其他人服用过那种药物呢。{wait}'
		'{page}'
		'#0404F只是，那药物究竟是谁散发出去的，\n'
		'现在还不清楚呢。\n'
		'我们这边也会留意的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F#12P……真是多谢了，瓦奇。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F#12P我们很期待你的消息。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (-2690, 0, 10250), 360),
	Insn('CHAR_SET_POS', Char(14), (-2600, 50, 12600), 0),
	Insn('FLAG_SET', Flag(1601)),
	Insn('QUEST', 76, Insn('TASK_SET', 9)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-1760, 1100, 11760), 0),
	Insn('CAM_ROTATE', 45, 30, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 22000, 0),
	Insn('CHAR_SET_POS', Char(257), (-890, 0, 11490), 315),
	Insn('CHAR_SET_POS', Char(258), (-780, 0, 10570), 315),
	Insn('CHAR_SET_POS', Char(259), (-2780, 0, 10550), 0),
	Insn('CHAR_SET_POS', Char(260), (-3990, 0, 10450), 45),
	Insn('CHAR_SET_POS', Char(265), (-1990, 0, 10100), 0),
	Insn('CHAR_SET_POS', Char(14), (-2500, 50, 12400), 135),
	Insn('CHAR_SET_FRAME', Char(14), 0),
	Insn('CHAR_FLAG1_UNSET', Char(4), 128),
	Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0402F哎呀，这不是罗伊德和各位嘛，\n'
		'今天也在努力工作吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0003F嗯，各式各样的工作都堆积成山了。{wait}'
		'{page}'
		'#0000F旧市街这边没什么特别情况吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0403F………………………………{wait}'
		'{page}'
		'#0400F算是吧，圣约帮还是和\n'
		'平时一样。{wait}'
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
	Insn('EMOTE', Char(265), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(14), Text(
		'#0400F呵呵，不过……{wait}'
		'{page}'
		'#0402F这次还带了位稀客过来啊，\n'
		'好像是警备队的人？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F嗯，正好有些事情要帮忙，\n'
		'所以暂时和我们同行……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#0500F初次见面，\n'
		'我是诺艾儿丄希卡。{wait}'
		'{page}'
		'您是罗伊德警官\n'
		'他们的朋友吧？\n'
		'请多多指教。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(14), 2),
	Insn('TEXT_TALK', Char(14), Text(
		'#0402F嘿……{wait}'
		'{page}'
		'#0404F呵呵，这位姐姐，\n'
		'该说你太过一本正经，\n'
		'还是该说非常有捉弄的价值呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(265), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(265), Text(
		'#0505F什么……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0011F喂，瓦奇……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0403F我说，对我这种不良帮派的小鬼，\n'
		'没必要特意使用礼貌用语吧。{wait}'
		'{page}'
		'#0402F相比之下，\n'
		'面对你这样严肃认真的姐姐，我宁愿\n'
		'被居高临下地唠叨教训一番呢。{wait}'
		'{page}'
		'#0405F啊，但这并不代表我是个Ｍ哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#0503F你、你可真是……{wait}'
		'{page}'
		'#0501F别人认真地和你打招呼，\n'
		'你却用那种嘲弄的态度回应，\n'
		'这样是不是不太好呢？{wait}'
		'{page}'
		'而且你那是什么打扮啊？\n'
		'请穿得正经一点，有个年轻人的样子！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0409F没错没错！要的就是这种感觉㈱{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#0505F呜……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#0003F（把一丝不苟的上士\n'
		'\u3000带到这种地方来，\n'
		'\u3000不得不说，真是有点失策呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F（哈哈，不过他们两个\n'
		'\u3000倒是意外地投缘呢。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_POS', Char(0), (-890, 0, 11490), 315),
	Insn('CHAR_SET_POS', Char(14), (-2600, 50, 12600), 0),
	Insn('CHAR_FLAG1_SET', Char(4), 128),
	Insn('CHAR_FLAG2_SET', Char(4), 32768),
	Insn('FLAG_SET', Flag(1668)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('CHAR_SET_FRAME', Char(14), 2),
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 500, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (-2840, 1100, 11440), 0),
	Insn('CAM_ROTATE', 45, 30, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(257), (-2660, 0, 10470), 0),
	Insn('CHAR_SET_POS', Char(239), (-1570, 0, 10560), 315),
	Insn('CHAR_SET_POS', Char(339), (-3700, 0, 10800), 45),
	Insn('CHAR_SET_POS', Char(14), (-2710, 0, 12150), 180),
	Insn('CHAR_SET_FRAME', Char(14), 0),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SLEEP', 750),
	Insn('TEXT_TALK', Char(339), Text(
		'#1110F啊，是瓦奇～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(14), 2),
	Insn('TEXT_TALK', Char(14), Text(
		'#0402F哎呀，好久不见。\n'
		'你最近还好吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#1109F嗯，琪雅很好哦。\n'
		'每天早上都有好好吃饭！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0402F呵呵，那就好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(14), 0),
	Insn('TEXT_TALK', Char(14), Text(
		'#0404F……看样子，\n'
		'总算是避过风头了吗？{wait}'
		'{page}'
		'#0400F听说鲁巴彻那边\n'
		'也打算不再深究了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F嗯，事情终于在今天早上平息了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F所以我们就带琪雅\n'
				'到街上熟悉一下。{wait}'
				'{page}'
				'#0101F……瓦奇，\n'
				'请不要对琪雅灌输一些\n'
				'奇怪的东西哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F所以我们就带琪雅\n'
				'到市里熟悉一下。{wait}'
				'{page}'
				'#0203F……瓦奇先生，\n'
				'拜托你不要对琪雅灌输一些\n'
				'奇怪的东西。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F于是我们就带着小琪，\n'
				'来街上熟悉一下环境。{wait}'
				'{page}'
				'#0301F……喂，瓦奇，你可别对小琪\n'
				'灌输一些莫名其妙的东西啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#0003F是啊……{wait}'
		'{page}'
		'#0001F瓦奇，请一定要\n'
		'注意措辞哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0404F呵呵，说得我真伤心啊。{wait}'
		'{page}'
		'#0400F话说回来，看你们两个的样子，\n'
		'完全就像是监护人嘛。{wait}'
		'{page}'
		'是想做她临时的\n'
		'爸爸妈妈吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#0105F大、大概算是吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F哈哈，不管怎么说，在找到她的家人之前，\n'
				'我们确实就算是她的监护人了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#0211F让我来当妈妈的话，\n'
				'实在是有些勉强吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F哈哈，不管怎么说，在找到她的家人之前，\n'
				'我们确实就算是她的监护人了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#0309F哦，这样的话，\n'
				'我是爸爸，罗伊德是妈妈吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0003F那个……{wait}'
				'{page}'
				'#0000F算了，不管怎么说，在找到她的家人之前，\n'
				'我们确实就算是她的监护人了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('FLAG_SET', Flag(1409)),
	Insn('CHAR_SET_POS', Char(14), (-2600, 50, 12600), 0),
	Insn('CHAR_SET_FRAME', Char(14), 2),
	Insn('CHAR_SET_FRAME', Char(15), 1),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('0x4B', Char(18), -1),
	Insn('0x4B', Char(19), -1),
	Insn('CHAR_SET_FRAME', Char(14), 2),
	Insn('TEXT_TALK', Char(18), Text(
		'可以坐在你旁边吗～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(18), Text(
		'那个，我们不小心\n'
		'迷了路呢～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'这一带的坏人可真多啊。\n'
		'真是很不安呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'不过，能遇到瓦奇先生，可真是超级幸运㈱\n'
		'哈哈～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0403F………………………………{wait}'
		'{page}'
		'#0400F呵，是吗？\n'
		'……不过，真遗憾啊。{wait}'
		'{page}'
		'#0402F其实我才是这里\n'
		'最大的恶人呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(18), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(19), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#0001F（瓦奇……这家伙………）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0306F（应对还真是熟练啊……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(0)),
	Insn('0x4C', Char(18), -1),
	Insn('0x4C', Char(19), -1),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('TEXT_TALK', Char(14), Text(
		'#0402F呵呵，各位辛苦了。{wait}'
		'{page}'
		'听说，不仅是我们的成员，\n'
		'连剑蛇帮的低级成员\n'
		'也接受了你们的训练呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0003F嗯……\n'
		'结果还算不错吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 0, 1, [
		Insn('CHAR_WATCH', Char(0), Char(9), 500),
	]),
	Insn('FORK', 1, 1, [
		Insn('CHAR_WATCH', Char(1), Char(9), 500),
	]),
	Insn('FORK', 2, 1, [
		Insn('CHAR_WATCH', Char(2), Char(9), 500),
	]),
	Insn('FORK', 3, 1, [
		Insn('CHAR_WATCH', Char(3), Char(9), 500),
	]),
	Insn('FORK_AWAIT', Char(0), 1),
	Insn('FORK_AWAIT', Char(1), 1),
	Insn('FORK_AWAIT', Char(2), 1),
	Insn('FORK_AWAIT', Char(3), 1),
	Insn('EMOTE', Char(0), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(1), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(2), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(3), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(0)),
	Insn('EMOTE_STOP', Char(1)),
	Insn('EMOTE_STOP', Char(2)),
	Insn('EMOTE_STOP', Char(3)),
	Insn('FORK', 0, 1, [
		Insn('CHAR_WATCH', Char(0), Char(14), 500),
	]),
	Insn('FORK', 1, 1, [
		Insn('CHAR_WATCH', Char(1), Char(14), 500),
	]),
	Insn('FORK', 2, 1, [
		Insn('CHAR_WATCH', Char(2), Char(14), 500),
	]),
	Insn('FORK', 3, 1, [
		Insn('CHAR_WATCH', Char(3), Char(14), 500),
	]),
	Insn('FORK_AWAIT', Char(0), 1),
	Insn('FORK_AWAIT', Char(1), 1),
	Insn('FORK_AWAIT', Char(2), 1),
	Insn('FORK_AWAIT', Char(3), 1),
	Insn('TEXT_TALK', Char(258), Text(
		'#0101F（但那个叫阿巴斯的人，\n'
		'\u3000究竟是何方神圣呢？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0306F（他的能力好像很强，\n'
		'\u3000游刃自若地掌控着状况呢。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0404F（呵呵，这个嘛。）{wait}'
		'{page}'
		'#0400F（据说他是出身于塞姆利亚\n'
		'\u3000大陆中东部的……）{wait}'
		'{page}'
		'（哈，总而言之，他自愿给我\n'
		'\u3000这样的怪人担当帮手，\n'
		'\u3000显然很喜欢给自己找事，这倒是不用怀疑的。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4B', Char(9), -1),
	Insn('CHAR_WATCH', Char(9), Char(14), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(9), Text(
		'#04100F我听到了哦，瓦奇。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(9), 180, 0),
		]),
		(None, [
			Insn('CHAR_ROTATE', Char(9), 0, 0),
		]),
	]),
	Insn('0x4C', Char(9), -1),
	Insn('FLAG_SET', Flag(1151)),
	Insn('FLAG_SET', Flag(10)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
			Insn('TEXT_TALK', Char(14), Text(
				'#0404F说起来，这个旧市街里住着\n'
				'一个充满魅力的东方女孩。{wait}'
				'{page}'
				'#0400F呵呵，据说她就是那个被破格提拔为\n'
				'彩虹剧团新剧码女二号的团员呢。{wait}'
				'{page}'
				'#0402F但是不管怎么想，她那么丰满，\n'
				'肯定会影响到表演吧。\n'
				'呵呵，不要紧吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(14), Text(
				'#0405F咦……\n'
				'你们怎么都皱着眉头呢？{wait}'
				'{page}'
				'#0400F呵呵，莫非又被卷进\n'
				'什么麻烦事了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F……嗯，说来话长。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#0402F虽然不知道发生了什么，\n'
				'总之，请继续加油吧。{wait}'
				'{page}'
				'我也很期待彩虹剧团\n'
				'的新剧呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0301F（明明什么都知道嘛。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F（也没准只是故意这么说，\n'
				'\u3000想借此套出我们的话……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(0)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('CHAR_SET_FRAME', Char(14), 2),
	Insn('TEXT_TALK', Char(14), Text(
		'#0402F嘿，这些货好像\n'
		'很危险吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#15504F并不危险。{wait}'
		'{page}'
		'#15500F我可不会订购\n'
		'自己处理不了的货。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(857)), Insn('END')]), [
					Insn('EMOTE', Char(0), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('EMOTE', Char(1), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('EMOTE', Char(2), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('EMOTE', Char(3), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(257), Text(
						'#0001F（好像正在谈话呢……）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F（在、在说些什么呢……？）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('FLAG_SET', Flag(0)),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 18, Insn('TASK_GET', 0))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 55))),
			Insn('RETURN'),
		]),
		(None, []),
	]),
	Insn('TEXT_START', Char(9)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('TASK_GET', 0))), Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F希望你们能指导圣约帮的成员\n'
				'学习防身术。{wait}'
				'{page}'
				'#04100F让他们见识一下警察特有的压制格斗技，\n'
				'可以吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('FADE_ON', 300, Color(0x00000000), 100),
			Insn('MENU', 0, -1, -1, 0, Text(
				'【接受】\n'
				'【放弃】\n'
			)),
			Insn('MENU_WAIT', 0),
			Insn('0x60', 0),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('0x5A'),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_END', Char(9)),
					Insn('EVENT_BEGIN', 0),
					Insn('0x4B', Char(9), -1),
					Insn('CROSSFADE', 800),
					Insn('CAM_OFFSET', (1290, 1000, 9450), 0),
					Insn('CAM_ROTATE', 52, 17, 0, 0),
					Insn('0x6E', 340, 0),
					Insn('CAM_DISTANCE', 25010, 0),
					Insn('CHAR_SET_POS', Char(9), (3060, 0, 8960), 270),
					Insn('CHAR_SET_POS', Char(257), (700, 0, 9600), 90),
					Insn('CHAR_SET_POS', Char(258), (560, 0, 8000), 90),
					Insn('CHAR_SET_POS', Char(259), (-990, 0, 8000), 90),
					Insn('CHAR_SET_POS', Char(260), (-990, 0, 9600), 90),
					Insn('0x4B', Char(13), -1),
					Insn('0x4B', Char(12), -1),
					Insn('0x4B', Char(10), -1),
					Insn('0x4B', Char(11), -1),
					Insn('CHAR_SET_POS', Char(13), (14390, 0, 7400), 178),
					Insn('CHAR_SET_POS', Char(12), (14000, 0, 7400), 268),
					Insn('CHAR_SET_POS', Char(10), (9250, 0, 4150), 225),
					Insn('CHAR_SET_POS', Char(11), (5000, 0, 2000), 90),
					Insn('0x0D'),
					Insn('CALL', Function((0, 56))),
					Insn('RETURN'),
				]),
				(None, []),
			]),
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F#0001F……请再稍等一下。\n'
				'我们也需要准备准备。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F我们今天一整天都有空。\n'
				'你们做好充足准备之后再来吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F这边没有异常。{wait}'
				'{page}'
				'#04100F请你们继续\n'
				'进行调查。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1601)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'#04100F……这边的事情就交给瓦奇吧。{wait}'
						'{page}'
						'#04100F请你们继续\n'
						'进行调查。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1669)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'#04100F……有什么事吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'#04100F瓦奇出门了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1560)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F找瓦奇有什么事吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F从上周开始，剑蛇帮的情况\n'
				'好像就有些奇怪。{wait}'
				'{page}'
				'#04100F……………………………………{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F………………………………{wait}'
				'{page}'
				'#04100F想点单的话和我说就好。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0006F（这个人的态度还是\n'
				'\u3000这么冷淡生硬呢……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'#04100F……瓦奇的判断不会出问题，\n'
						'全都交给他来判断吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(0), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('EMOTE', Char(1), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 1000),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'#04100F……………………………………{wait}'
						'{page}'
						'#04100F希望你们不要把瓦奇卷进\n'
						'警察的纠纷里。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F米修拉姆的事件\n'
						'是瓦奇自己决定要插手的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'#04100F……是瓦奇的判断吗…………\n'
						'………………那就没问题了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(0), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('EMOTE', Char(1), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F（态度的变化好像\n'
						'\u3000莫名地果断呢……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F瓦奇出门工作了。{wait}'
				'{page}'
				'#04100F如果找他有什么事，\n'
				'等以后有机会再说吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F工作……？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'#04100F我没有义务回答你们。{wait}'
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
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F（一点都没变，还是这么冷淡生硬啊……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F在纪念庆典期间，\n'
				'我们推出了特别鸡尾酒。{wait}'
				'{page}'
				'#04100F有兴趣的话就点一杯尝尝吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F……今天临时休业。{wait}'
				'{page}'
				'#04100F想喝东西的话，\n'
				'就请改日再来吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1153)), Insn('END')]), [
							Insn('CALL', Function((0, 18))),
						]),
						(None, [
							Insn('CALL', Function((0, 17))),
						]),
					]),
				]),
				(None, [
					Insn('CALL', Function((0, 18))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1153)), Insn('END')]), [
							Insn('CALL', Function((0, 19))),
						]),
						(None, [
							Insn('CALL', Function((0, 17))),
						]),
					]),
				]),
				(None, [
					Insn('CALL', Function((0, 19))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'#04100F为了防止那群黑手党潜入旧市街，\n'
						'我们准备开始在这里巡逻。{wait}'
						'{page}'
						'#04100F因为我们自己也不想让\n'
						'之前那种事件再度发生。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'#04100F如果黑手党之间的斗争不断升级，\n'
						'说不定也会影响到我们这边。{wait}'
						'{page}'
						'#04100F……我们也必须采取些措施了。{wait}'
						'{page}'
						'#04100F首先要做的就是\n'
						'在旧市街定期巡逻。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F听说最近这段时间，危险事件\n'
				'好像有所增多呢。{wait}'
				'{page}'
				'#04100F………………………………{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('EMOTE', Char(0), 0, 2000, (0, 1, 250, 2)),
					Insn('SOUND_PLAY', 29, 0, 0, 100),
					Insn('EMOTE', Char(1), 0, 2000, (0, 1, 250, 2)),
					Insn('SOUND_PLAY', 29, 0, 0, 100),
					Insn('EMOTE', Char(2), 0, 2000, (0, 1, 250, 2)),
					Insn('SOUND_PLAY', 29, 0, 0, 100),
					Insn('EMOTE', Char(3), 0, 2000, (0, 1, 250, 2)),
					Insn('SOUND_PLAY', 29, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(9), Text(
						'#04100F……不，没什么。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F我没打算要干预\n'
				'成员的私事。{wait}'
				'{page}'
				'#04100F是否要加入圣约帮就交给\n'
				'大家自行判断。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'#04100F阿赛尔由我们来照顾就好。{wait}'
						'{page}'
						'#04100F不需要多余的担心。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'#04100F阿赛尔还需要\n'
						'去医院复查。{wait}'
						'{page}'
						'#04100F因为他之前昏迷了很久。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F……姑且算是开始营业了。{wait}'
				'{page}'
				'#04100F如果想吃东西，\n'
				'就和我说吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F谢、谢谢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0301F（话说，这家店果然是\n'
						'\u3000这个大块头开的啊。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F如果探听到什么情报的话，\n'
				'就去告诉瓦奇吧。{wait}'
				'{page}'
				'#04100F没必要和我们说。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F……我们正在等待\n'
				'医院那边的联系。{wait}'
				'{page}'
				'#04100F如果话说完了，\n'
				'就赶快离开吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(9)),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('CALL', Function((0, 15))),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('TEXT_TALK', Char(9), Text(
		'#04100F把这个拿去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'收下了{item 469}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 469, 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F谢、谢谢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0203F（是刚才的工作报酬吧。但他的态度\n'
		'\u3000太过生硬，让人难以判断呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F（算了，我们就先收下吧。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(1153)),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('TEXT_TALK', Char(9), Text(
		'#04100F……那么。\n'
		'为了应对纪念庆典，\n'
		'我们也该开始做准备了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F（……………………？\n'
		'\u3000这家酒吧难道也打算\n'
		'\u3000展开优惠活动吗。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('TEXT_TALK', Char(9), Text(
		'#04100F………………………………{wait}'
		'{page}'
		'#04100F不要耽误瓦奇的时间。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'堂堂正正地战斗，然后战胜对手。\n'
						'圣约帮绝对不会使用\n'
						'卑鄙的手段。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'咳……你们也给我\n'
						'好好记住吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'剑蛇帮的战斗力已经削弱了，\n'
						'现在正是击溃他们的大好时机……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'不过……还是算了，瓦奇绝对\n'
						'不会那么做的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'他就是那样的人啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(10), Text(
				'瓦奇从今天早上开始，\n'
				'就一直是一脸严肃的表情。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'……我还是第一次见到\n'
				'那种样子的瓦奇呢，\n'
				'发生什么事了吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1560)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'要是能得到瓦奇的许可，\n'
						'像那种新人，轻轻松松就能收拾掉了……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'咳……剑蛇帮的底层成员竟会如此嚣张，\n'
						'确实是很蹊跷啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'那个少年我们也是认识的。\n'
						'因为他几乎每天都会来找我们麻烦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'……不过，瓦奇却说\n'
						'不要对他出手。\n'
						'可恶，真是咽不下这口气……！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'这次出了这么大的事情，\n'
						'警察也不得不出动了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'由于黑手党之间争斗不断，\n'
						'我老爸工作的乌尔斯拉医院\n'
						'好像也运进了很多伤患。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'……看起来还真不是谣传呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'哼，在市区中心，\n'
						'竟然干出了那么大胆的事。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'剑蛇帮的那群混蛋……\n'
						'最近又开始\n'
						'嚣张起来了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'我昨天在大街上\n'
						'被剑蛇帮的人缠住了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'哼……一点都没变，\n'
						'还是一群品行低劣的家伙。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'真想赶快把他们\n'
						'都干掉。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'一切都要听从瓦奇的意思，\n'
						'现在也只能交给瓦奇来处理了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'……瓦、瓦奇，对不起。\n'
						'本想趁瓦奇回来之前\n'
						'把她们打发走，可是……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'咳、咳咳……\n'
						'你们几个，不要打扰到瓦奇哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'『全都要听从瓦奇的意思』。\n'
						'如果是阿巴斯的话，\n'
						'肯定会这么说吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'瓦奇和阿巴斯\n'
						'都出门了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'我、我们必须加油\n'
						'把店看好呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CALL', Function((0, 21))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'和剑蛇帮之间的紧张关系，\n'
						'在短时间内仍然会持续。\n'
						'不过……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'……算了，毕竟到了纪念庆典。\n'
						'决斗什么的，就暂时延后吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'临近纪念庆典，\n'
						'黑手党的那些家伙\n'
						'好像也变老实了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'和剑蛇帮之间的紧张关系\n'
						'也暂时停止了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'哎呀呀，和他们的决斗\n'
						'就暂时推延一阵子吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1154)), Insn('END')]), [
							Insn('CALL', Function((0, 23))),
						]),
						(None, [
							Insn('CALL', Function((0, 22))),
						]),
					]),
				]),
				(None, [
					Insn('CALL', Function((0, 23))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1154)), Insn('END')]), [
							Insn('TEXT_TALK', Char(10), Text(
								'最近这段时间，鲁巴彻的家伙\n'
								'好像一直鬼鬼祟祟的。\n'
								'我们也要增加巡逻的力度。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'哼……下次要是再发现他们，\n'
								'绝对不会轻饶。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('CALL', Function((0, 22))),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'瓦奇的夜间工作\n'
						'本来就很多了，\n'
						'希望他能注意自己的身体啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'瓦奇好像又\n'
						'通宵喝酒了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'当然，我不是对瓦奇\n'
						'有什么不满。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'但希望他能好好注意自己的身体。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('TEXT_TALK', Char(10), Text(
				'欢乐街和小巷那一带好像也是\n'
				'事件的多发之地。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'哼……这都是因为你们警察\n'
				'怠忽职守所造成的吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'早晚要和剑蛇帮的那些家伙\n'
						'做个彻底了结。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'但在纪念庆典之前，暂时休战。\n'
						'警察和官员在场的话，\n'
						'就非常扫兴了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'最近这段时间，和剑蛇帮\n'
						'连一次像样的架都没打成。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'都是因为临近纪念庆典，警察和官员们\n'
						'一批接一批的不断跑来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'真是让人败兴啊。\n'
						'真是的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'先不提这个……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'阿赛尔他不会真的打算\n'
						'离开组织吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'刚才，剑蛇帮的人从广场那边\n'
						'过来了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'那些家伙该不会是\n'
						'又开始得意忘形了吧，\n'
						'真是一群碍眼的家伙。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'我也学习过武术哦，\n'
						'对徒手格斗还是很有自信的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'……当然，还远远比不上\n'
						'瓦奇啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'最近都没再和剑蛇帮的人\n'
						'打过架了。\n'
						'真是好无聊啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'但也不能放任自己的身手退步。\n'
						'看来也只能在平时多练习一下\n'
						'弹弓射击了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'顺便一说，我从小就\n'
						'开始习武呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'对徒手格斗还是很有自信的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'阿赛尔总算是出院了。\n'
						'感觉心中最后的一块石头也落了地啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'接下来，只要去和剑蛇帮的家伙们\n'
						'做个了结就可以了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'阿赛尔总算出院了啊，\n'
						'我们也终于可以放下心了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'……老实说，不得不向你们表示感谢。\n'
						'不过，可不要太得意忘形啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'我们圣约帮的成员就相当于瓦奇的手足。\n'
						'可以下达命令的人，\n'
						'只有首领瓦奇。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(627)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'真担心正在住院的阿赛尔啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'反正我老爸也在医院工作，\n'
						'不然明天直接去看看他好了……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CALL', Function((0, 24))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
			Insn('TEXT_TALK', Char(10), Text(
				'被打倒的阿赛尔，\n'
				'伤口是被钝器击打造成的，同时还有轻微的撕裂。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'那明显是被剑蛇帮的钉棍所造成的，\n'
				'绝对不会有错！\n'
				'……可恶……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(10), Text(
				'你们也许不清楚，\n'
				'其实我们是很少单独行动的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'但阿赛尔已经很久没回家了，\n'
				'那天他正好要回家……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'……等到我们赶到的时候，\n'
				'阿赛尔已经倒在地上了，\n'
				'伤口是被钝器击打造成的，同时还有轻微的撕裂。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'显然是被那群无脑混蛋们\n'
				'用钉棍打的，不会有错！\n'
				'……可恶……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(626)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F是吗……\n'
						'多谢你告诉我们这些。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'哼、哼……因为有瓦奇的许可，\n'
						'我才会和你们说这些的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'无能的警察，可不要太\n'
						'得意忘形啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(626)),
				]),
				(None, []),
			]),
			Insn('FLAG_SET', Flag(2)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('0x4B', Char(10), -1),
	Insn('0x4B', Char(11), -1),
	Insn('TEXT_TALK', Char(11), Text(
		'我、我很不擅、擅长接待客人的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'这里就交给琴兹吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'其、其实我也\n'
		'不是很擅长啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'不过，明白了，这里就交给我吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_UNSET', Char(10), 16),
	Insn('0x4C', Char(10), -1),
	Insn('0x4C', Char(11), -1),
	Insn('FLAG_SET', Flag(2)),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('TEXT_TALK', Char(10), Text(
		'其实我正在进行秘密特训呢，\n'
		'今天的实战确实很有参考价值。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'……虽然并不想向你们道谢，\n'
		'但确实是对我有所帮助呢。\n'
		'那、那个，谢啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(1154)),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('TEXT_TALK', Char(10), Text(
		'真没想到，竟然连剑蛇帮的家伙\n'
		'也开始巡逻了啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'哼，难怪最近这段时间\n'
		'经常看到他们。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'瓦奇好像并不打算\n'
		'要立刻开战呢。\n'
		'但关键还是要看对方的态度如何。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('TEXT_TALK', Char(10), Text(
		'……早知会有这种事情发生的话……\n'
		'我以前是不是也应该\n'
		'多看看老爸的医书呢……{wait}'
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
	Insn('TEXT_TALK', Char(259), Text(
		'#0205F……医书吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(10), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 500),
	Insn('CHAR_WATCH', Char(10), Char(0), 500),
	Insn('TEXT_TALK', Char(10), Text(
		'什、什么啊，又是你们吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'哼……有意见吗？\n'
		'每个人都有自己的隐情。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(10), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(10)),
	Insn('TEXT_TALK', Char(10), Text(
		'遭到暗算的阿赛尔被抬到了这里，\n'
		'并接受了简单的护理，可是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'他一直都没有恢复意识，\n'
		'最后还是等到了天亮，\n'
		'然后叫来了救护车。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'……我虽然很讨厌老爸，\n'
		'但以前真应该多向他学习一些\n'
		'基本的急救知识啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0003F是吗……\n'
		'确实是很让人担心呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'嗯，可是，不知为何，\n'
		'阿赛尔乘坐的那辆\n'
		'救护车没有立刻发车……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(621)), Insn('END')]), [
			Insn('EMOTE', Char(0), 0, 2000, (38, 38, 250, 1)),
			Insn('EMOTE', Char(1), 0, 2000, (38, 38, 250, 1)),
			Insn('EMOTE', Char(2), 0, 2000, (38, 38, 250, 1)),
			Insn('EMOTE', Char(3), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F啊，是吗。\n'
				'因为那辆救护车也要等\n'
				'剑蛇帮的那个受害者吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0203F这样也挺好的。\n'
				'至少不用耽误时间，\n'
				'让救护车跑两趟……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(10), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(10), Text(
				'#4S好、好什么好啊！？\n'
				'我们可是跟剑蛇帮的家伙上了一辆车哦！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('EMOTE', Char(0), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('EMOTE', Char(1), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('EMOTE', Char(2), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('EMOTE', Char(3), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(258), Text(
				'#0105F那是……怎么回事呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'从旧市街那边又送来了\n'
				'另一个受伤者。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'哼，就是剑蛇帮的那个家伙。\n'
				'他的同伴说他受了重伤。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'最后把两个伤患用同一辆\n'
				'救护车送走了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0003F是吗，\n'
				'两方人员都在同一个夜晚遭到袭击……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0301F该怎么说呢，\n'
				'这时机未免也太巧了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(10), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(10), Text(
				'#4S应该说时机实在是\n'
				'太糟了才对吧！\n'
				'我们可是跟剑蛇帮的家伙上了一辆车哦！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(621)),
		]),
	]),
	Insn('TEXT_TALK', Char(10), Text(
		'#2S……咳、咳咳，哎呀呀……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'真担心正在住院的阿赛尔啊。\n'
		'反正我老爸也在医院工作，\n'
		'不然明天直接去看看他好了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_UNSET', Char(10), 16),
	Insn('FLAG_SET', Flag(627)),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'向剑蛇帮发动奇袭作战的提议\n'
						'被瓦奇否决了{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'可恶的红衣爬虫们……\n'
						'算、算你们捡了条命啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'虽、虽然我很憎恨\n'
						'剑蛇帮的那群家伙……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'但、但既然瓦奇都那么说了，也就没办法了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'这次就先饶、饶他们一命吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(11), Text(
				'瓦奇最近经、经常外出。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'好、好像是在调查些什么。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1560)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'剑、剑蛇帮好像出现了\n'
						'很严重的内斗呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'哼……我才没有担心那些\n'
						'红衣爬虫呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'我刚、刚才过去看了一下，\n'
						'好像是真的呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'剑蛇帮的干部被打伤了，\n'
						'好像已经送去医院了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'这、这事发生得还真够没头没脑，\n'
						'真有白痴蛇帮成员的风格呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'那、那些混蛋黑手党们……\n'
						'再敢来旧市街的话，我绝对饶不了他们。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'那、那些混蛋黑手党们……\n'
						'又开始做什么鬼祟勾当了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'之前可真是承蒙他们的『关照』啊。\n'
						'要、要是让我看见他们的话，一、一定把他们捉到。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'那、那个蓝头发的红衣爬虫……\n'
						'最近经常来闹事。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'而且他、他的样子也变了，\n'
						'以前明明是个胆小懦弱的家伙。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'我、我能感觉得到，\n'
						'那个蓝头发的红衣爬虫似乎不太寻常。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'那、那个家伙原本只是\n'
						'负责看门的最底层成员。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(11), Text(
				'琴兹那家伙，\n'
				'去、去找他的父亲了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'那、那家伙的父亲\n'
				'是乌尔斯拉医院的医生。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'他、他和他父亲好像很合不来呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'多亏了梁，\n'
						'店铺可以维持营业了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'奇、奇怪的客人凑到了瓦奇身边，\n'
						'真是让人在意啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'梁竟然还有调制鸡尾酒的才能，\n'
						'我以前都不知道呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'阿、阿巴斯调制的鸡尾酒很好喝，\n'
						'不过梁也很厉害啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'说起来，\n'
						'阿梁那家伙虽然平时不起眼，\n'
						'但双手真的非常灵巧呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('0x4B', Char(18), -1),
					Insn('TEXT_TALK', Char(11), Text(
						'要是想打撞球的话，\n'
						'就、就来和我说。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'我可以把规则教给你。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('0x4C', Char(18), -1),
				]),
				(None, [
					Insn('CALL', Function((0, 21))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(11), Text(
				'大、大家今、今天要一起出门。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'瓦奇很忙的，\n'
				'昨天都没能挤出时间。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1156)), Insn('END')]), [
							Insn('CALL', Function((0, 27))),
						]),
						(None, [
							Insn('CALL', Function((0, 26))),
						]),
					]),
				]),
				(None, [
					Insn('CALL', Function((0, 27))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1156)), Insn('END')]), [
							Insn('TEXT_TALK', Char(11), Text(
								'要、要是能学好防身术，\n'
								'就不用再怕那些黑手党了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'发现他们之后，就把他们\n'
								'赶、赶出这旧市街。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('IF', [
								(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
									Insn('TEXT_TALK', Char(257), Text(
										'#0006F不过还是不要\n'
										'太乱来哦……{wait}'
									)),
									Insn('TEXT_WAIT'),
								]),
								(None, []),
							]),
							Insn('FLAG_SET', Flag(3)),
						]),
						(None, [
							Insn('CALL', Function((0, 26))),
						]),
					]),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'那、那位客人每个星期\n'
						'必来一次。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'好像和瓦奇有话说呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'瓦、瓦奇果然很成熟啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1155)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'旧市街这一带有很多的\n'
						'仓、仓库和废墟。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'据、据说那些黑手党\n'
						'就是在这\n'
						'附近开战的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'真、真会给人添麻烦啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'旧市街这一带有很多的\n'
						'仓、仓库和废墟。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'据、据说那些黑手党\n'
						'就是在这\n'
						'附近开战的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'真、真会给人添麻烦啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F原来如此啊……{wait}'
						'{page}'
						'#0001F鲁巴彻和黑月的斗争，\n'
						'也影响到这里了吗。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0306F呼～其实你们之间的\n'
						'斗争也挺让人头痛的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'我们之间的斗争\n'
						'和、和那些家伙可不一样。\n'
						'全都是必要的行动啊。{wait}'
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
						'#0106F我想不能这么说吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1155)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'来、来旧市街的那些官员\n'
						'全都是一群伪善者。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'那种家伙实在是\n'
						'无、无法让人信任。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'每年只要一到了临近纪念庆典的时候，\n'
						'就、就会有很多官员过来找麻烦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'不是检查营业许可证，\n'
						'就是提醒游客小心注意。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'但那些官员总、总是敷衍了事，\n'
						'实际上根本就没有检查过，\n'
						'最后却说已经确认好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'哼、哼……一群伪善者。\n'
						'那种家伙实在令人讨厌。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'阿赛尔到底会怎么决定呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'竟、竟然能\n'
						'找到这种地方来……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'真、真是吃惊。\n'
						'阿赛尔的姐姐可真是大胆啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'刚才我走在东侧大道上，\n'
						'就、就被一个女人给叫住了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'好像是阿赛尔的姐姐，\n'
						'问了我很多关于阿赛尔的事情。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'大概是因为阿赛尔住院了吧……\n'
						'她、她好像非常担心呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我在东侧大道被阿赛尔的姐姐\n'
						'问了话。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'说、说起来，在我离开的时候，\n'
						'她好像在用很锐利的目光瞪着我呢……\n'
						'……是、是错觉吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'警、警察局的走狗，\n'
						'我还是不信任你们。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'来这里是无妨，\n'
						'但、但不准你们太放肆啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'警、警察局的走狗……\n'
						'你们又、又来、来了吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'虽、虽然之前确实是\n'
						'得到了你们的帮助。\n'
						'但这间酒吧──崔尼蒂可是瓦奇的圣域哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'这里的规矩就是，一切都要遵从瓦奇的指示。\n'
						'听、听明白了没有啊！？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('TEXT_TALK', Char(11), Text(
				'剑、剑蛇帮的家伙……\n'
				'他们在上次的争斗中落了下风，\n'
				'所以就一直怀恨在心。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'这、这群卑鄙无耻的家伙。\n'
				'犯人除了他们之外，不做其它考虑。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
			Insn('TEXT_TALK', Char(11), Text(
				'我、我丝毫不打算\n'
				'对警、警察提供协助。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'赶、赶快从我眼前消失吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(11), Text(
				'听、听好啊，\n'
				'这间酒吧──崔尼蒂可是瓦奇的圣域。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'如果敢在这里乱来，\n'
				'可、可是不会被轻易放过的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(3)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('TEXT_TALK', Char(11), Text(
		'今天的训练是在\n'
		'事、事前就决定好的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'但、但在正式进行之前，\n'
		'完全都没有透露出丝毫口风。\n'
		'呵呵，是、是不是很吃惊啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F嗯，算是吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0306F真是的，吃惊又如何啊～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(1156)),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
			Insn('TEXT_TALK', Char(11), Text(
				'虽然很讨厌那些黑手党，\n'
				'但剑、剑蛇帮的那些家伙也很碍眼。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'我们最、最近宽宏大量，不和他们计较，\n'
				'结果他们反倒得意忘形，嚣张起来了！？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(11), Text(
				'最、最近这段时间，红衣爬虫们\n'
				'好像也开始在旧市街巡逻了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'真、真是群碍眼的家伙。\n'
				'光、光是昨、昨天巡逻一天，\n'
				'就见到了他们三次。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'……实、实在是太碍眼了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(3)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][28] = [
	Insn('TEXT_START', Char(12)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'不打架虽然挺好。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'不过，只要是为了同伴，\n'
				'不管是什么事情我都愿意做……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'我们都是志趣相投的好兄弟。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('0x4B', Char(12), -1),
					Insn('TEXT_TALK', Char(12), Text(
						'只要多练习，阿赛尔也能越来越厉害。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'……加油。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('0x4C', Char(12), -1),
				]),
				(None, [
					Insn('CALL', Function((0, 30))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1560)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'虽然很讨厌剑蛇帮……\n'
						'但还是不希望听到那种不好的传闻。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'我刚才听到了传闻……\n'
						'剑蛇帮好像发生了同伴之间的内斗。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'虽然我很讨厌剑蛇帮的那些家伙，\n'
						'但不知为何，还是有点担心呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'阿赛尔很担心他的家人，\n'
						'所以就回家了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'……阿赛尔还真是\n'
						'彻底学乖了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'港湾公园好像发生了事件呢，\n'
						'阿赛尔回去和家人团聚了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'……因为他家就在港湾区附近啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'旧市街还是一点都没变啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'……但正因如此，我才喜欢这里。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'最近这段时间，市里\n'
						'的经济好像很景气呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'总能听到一些有公司\n'
						'入驻之类的传闻。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'不过，旧市街的贫困\n'
						'还是一如既往呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'今天街上也很\n'
				'宁静悠闲啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'在这种日子散散步，\n'
				'似乎也是不错的选择。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'今天也要在店里帮忙。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'欢迎光临，\n'
						'想点餐的话就和阿巴斯说吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'欢迎光临。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'……大家今天也都\n'
						'出门了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'没办法了，\n'
						'只有由我来接待客人了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'其实瓦奇生气时很恐怖呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'……但一般来说，他也只对缠着自己不放\n'
						'的女人才会发脾气。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'那两个人都很可怜呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'肯定过不了多久，\n'
						'就会被无情地抛弃呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'阿巴斯出门了，{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'想点餐的话就和我说吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'想点些什么呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'阿巴斯现在不在，\n'
						'今天要点单的话就来找我。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'比起回家待着，\n'
						'还是跟同伴们在一起更加开心。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'……像我这么想的人，\n'
						'在世上应该\n'
						'有不少呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'在纪念庆典时，全家一起\n'
						'出游的人好像很多呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'可是我没有父母。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'家里面只有对我很凶的\n'
						'叔叔和婶婶……\n'
						'再也不想回去了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'啊……是警察。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'工作辛苦了。\n'
						'现在人很多，请小心点啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CALL', Function((0, 31))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1157)), Insn('END')]), [
							Insn('CALL', Function((0, 33))),
						]),
						(None, [
							Insn('CALL', Function((0, 32))),
						]),
					]),
				]),
				(None, [
					Insn('CALL', Function((0, 33))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1157)), Insn('END')]), [
							Insn('TEXT_TALK', Char(12), Text(
								'阿赛尔去柜台接待客人后，\n'
								'都没人和我打撞球了，真寂寞……{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('CALL', Function((0, 32))),
						]),
					]),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'你们今天有空吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'……不，没什么。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'我们也准备开始\n'
						'在旧市街巡逻了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'……放心吧，\n'
						'绝对不会再让那种事情发生了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'我最近也在偏僻的小巷中\n'
						'见到过黑手党的人。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'……就是之前暗算阿赛尔的家伙，\n'
						'见到他们，我当然非常火大。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'阿赛尔可以重新活动，\n'
				'差不多已经有一个星期了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我想多帮帮他，\n'
				'但他却不希望让我帮忙。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……不知为何，总觉得\n'
				'阿赛尔稍微变得成熟些了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'阿赛尔其实很喜欢\n'
				'他的姐姐呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'不过……他总是给姐姐惹麻烦，\n'
				'所以心里肯定会有些不自在吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'在遇到困难的时候，\n'
						'我们都会互相帮助。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'……这正是圣约帮\n'
						'的优点。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'阿赛尔还要再去医院\n'
						'复查几次。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'……不用担心钱的问题，\n'
						'医疗费已经由大家分摊了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'如果阿赛尔当时被打中要害的话，\n'
						'说不定就会死掉了呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'绝对不能原谅那些黑手党，\n'
						'我们今后也要多加留意才行。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'阿赛尔平安无事地出院了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'那个……虽然这句话说得有些晚，\n'
						'不过，真是谢谢你们了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'如果阿赛尔当时被打中要害，\n'
						'现在说不定就已经死掉了呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'……这么一想的话，\n'
						'实在是不能不感谢\n'
						'为我们报仇的各位啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'阿赛尔……现在怎么样了呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'意识差不多也该恢复了吧，\n'
				'希望他平安无事……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'同伴的仇，就由我们亲手来报。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'你们不要多事哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(12), Text(
				'遭到袭击的人是一个\n'
				'名叫阿赛尔的家伙。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'……我们本想亲手为同伴报仇。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'但瓦奇却阻止我们出手，\n'
				'让我们不要擅自行动。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(4)),
		]),
	]),
	Insn('TEXT_END', Char(12)),
	Insn('RETURN'),
]

data['code'][29] = [
	Insn('CALL', Function((0, 28))),
	Insn('RETURN'),
]

data['code'][30] = [
	Insn('0x4B', Char(12), -1),
	Insn('0x4B', Char(13), -1),
	Insn('TEXT_TALK', Char(13), Text(
		'……梁，你这家伙还真是\n'
		'很擅长调制鸡尾酒啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'说起来，你的手一直都很巧，\n'
		'打撞球的技术也是我们这里最厉害的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'只要多练习，阿赛尔也能越来越厉害。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'……加油。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'嗯、嗯。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_UNSET', Char(13), 16),
	Insn('0x4C', Char(12), -1),
	Insn('0x4C', Char(13), -1),
	Insn('FLAG_SET', Flag(4)),
	Insn('RETURN'),
]

data['code'][31] = [
	Insn('0x4B', Char(12), -1),
	Insn('0x4B', Char(13), -1),
	Insn('TEXT_TALK', Char(12), Text(
		'阿赛尔，你的家人如何了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'有需要就回去，用不着在意我们哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'嗯，纪念庆典的后半段时间，\n'
		'准备和姐姐一起过。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'今天就和大家一起开心一下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_UNSET', Char(12), 16),
	Insn('CHAR_FLAG1_UNSET', Char(13), 16),
	Insn('0x4C', Char(12), -1),
	Insn('0x4C', Char(13), -1),
	Insn('FLAG_SET', Flag(4)),
	Insn('RETURN'),
]

data['code'][32] = [
	Insn('TEXT_TALK', Char(12), Text(
		'刚才真是多谢了。\n'
		'你们的战斗方式很值得参考。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'以后和剑蛇帮的人打架时，\n'
		'应该也能派上用场……{wait}'
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
	Insn('TEXT_TALK', Char(257), Text(
		'#0006F拜托你，不要在那种场合派上用场啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(1157)),
	Insn('RETURN'),
]

data['code'][33] = [
	Insn('TEXT_TALK', Char(12), Text(
		'剑蛇帮的瓦鲁多一直在旧市街\n'
		'占山为王，以老大自居。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'但在两年前的时候，瓦奇出现了，\n'
		'前来滋事找碴的瓦鲁多，\n'
		'在一瞬间便被他打倒了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'自那之后，不服从瓦鲁多\n'
		'的组织『圣约帮』就建立起来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'……瓦奇可是非常强的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][34] = [
	Insn('TEXT_START', Char(13)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'我已经习惯了如今的工作，\n'
						'对打架越来越没有兴趣了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'……听到瓦奇让我们停止争斗时，\n'
						'老实说，还真是松了口气呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'听说剑蛇帮的瓦鲁多\n'
						'现在非常消沉沮丧，是真的吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'实、实在是难以想像啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'梁很有天赋，\n'
						'不管学什么都能很快掌握。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'有这样的好朋友真是很不错。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CALL', Function((0, 30))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'瓦奇在夜间工作中\n'
						'赚到了很多钱呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'该怎么说呢，真不愧是瓦奇啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'瓦奇每周都有两三天左右\n'
						'的时间要去做夜间工作。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'……看样子，他好像\n'
						'赚了不少钱呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(13), Text(
				'我已经很习惯店里的工作了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'……凭劳动赚钱的感觉\n'
				'果然很不错呢，\n'
				'必须要感谢大家才行啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'这肯定是以瓦奇\n'
						'为目标而光顾的客人啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'因为瓦奇他实在是太惹眼了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'客人开始增多了呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'果然是因为昨天那件事吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'游客源源不断地\n'
						'光顾这里。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'在纪念庆典的后半段时间，\n'
						'我准备和家人一起度过。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'圣约帮在这方面是很自由的，\n'
						'姐姐一定也会很高兴吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CALL', Function((0, 31))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 20))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((2, 22))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1158)), Insn('END')]), [
							Insn('CALL', Function((0, 37))),
						]),
						(None, [
							Insn('CALL', Function((0, 36))),
						]),
					]),
				]),
				(None, [
					Insn('CALL', Function((0, 37))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 20))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((2, 22))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1158)), Insn('END')]), [
							Insn('IF', [
								(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
									Insn('TEXT_TALK', Char(13), Text(
										'（这女人稍微有些\n'
										'\u3000可怕呢。）{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(13), Text(
										'（不过和瓦奇好像\n'
										'\u3000还挺投缘的。）{wait}'
									)),
									Insn('TEXT_WAIT'),
								]),
								(None, [
									Insn('TEXT_TALK', Char(13), Text(
										'那个，这是您点的鸡尾酒。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(15), Text(
										'#15503F哦，帮我记在账上吧。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(13), Text(
										'明、明白了，\n'
										'先记在账上是吗？{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('CHAR_FLAG1_UNSET', Char(13), 16),
									Insn('FLAG_SET', Flag(5)),
								]),
							]),
						]),
						(None, [
							Insn('CHAR_WATCH', Char(13), Char(0), 0),
							Insn('CALL', Function((0, 36))),
							Insn('CHAR_ROTATE', Char(13), 180, 0),
						]),
					]),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'咳，今天稍微有些\n'
						'重要的工作呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'差不多也该开始准备了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_ROTATE', Char(254), 0, 0),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，杯子已经擦过了，\n'
						'然后是进货单的检查……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(254), Char(0), 500),
					Insn('TEXT_TALK', Char(254), Text(
						'……阿巴斯还真是相当严厉呢。\n'
						'一旦做错什么，就会受到他的严肃警告。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然平时在一起的时候没发现过，\n'
						'但那副魁梧的身材实在是威严感十足呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'如果工作中犯了错误，\n'
						'就会被阿巴斯警告呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……呜呜，看来打工也不是\n'
						'一件很轻松的事啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我开始在这家酒吧里打工了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……我想用自己的劳力赚钱，\n'
						'把治疗费还给姐姐。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我总是让姐姐为我担心，\n'
						'是不是应该退出圣约帮，\n'
						'好好工作才对呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过，我暂时还是先试着在这里工作一段时间吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'虽然我也想过很多，\n'
						'但果然还是不愿意\n'
						'退出圣约帮呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我用劳力赚钱，把治疗费还给姐姐的举动，\n'
						'得到了姐姐的认可呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(13), Text(
				'姐姐跑到这里来找我了！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'这、这、这该怎么办啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'如果向姐姐道歉的话，\n'
						'她肯定会要求我\n'
						'退出圣约帮的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'唉，找不到合适的时机道歉啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'我找不到合适的时机\n'
						'向姐姐道歉。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'我总是让她担心，\n'
						'所以至少也要道个歉……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'嗯～检查期已经结束了，\n'
						'彻底痊愈之后，是不是该向姐姐道个歉呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
			Insn('TEXT_TALK', Char(13), Text(
				'确实是让姐姐担心了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'我也觉得很对不起她……\n'
				'唉，这下子又更加没脸见她了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(13), Text(
				'我的伤势已经几乎痊愈，\n'
				'总算是出院了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'但姐姐这段时间\n'
				'好像相当为我担心呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'在姐姐的心里，圣约帮\n'
				'实在不是一个好地方……\n'
				'因为我总是彻夜不归，还搞得受伤住院……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'……唉，事到如今，\n'
				'实在是没脸再面对她了啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(5)),
		]),
	]),
	Insn('TEXT_END', Char(13)),
	Insn('RETURN'),
]

data['code'][35] = [
	Insn('CALL', Function((0, 34))),
	Insn('RETURN'),
]

data['code'][36] = [
	Insn('TEXT_TALK', Char(13), Text(
		'刚、刚才真是承蒙关照了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'我之前曾被黑手党\n'
		'的人暗算得手，\n'
		'从今以后一定要好好练习防身术。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F是吗……那就加油吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'嗯，那当然。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(1158)),
	Insn('RETURN'),
]

data['code'][37] = [
	Insn('TEXT_TALK', Char(13), Text(
		'姐姐好像要在纪念庆典时\n'
		'申请休假呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'……如果我也能放假，\n'
		'就去陪陪她好了。\n'
		'平时总是让她为我担心。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][38] = [
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
				(Expr([Insn('FLAG', Flag(1413)), Insn('END')]), [
					Insn('CHAR_SET_FRAME', Char(15), 1),
					Insn('TEXT_TALK', Char(15), Text(
						'#15509F呵呵，和解休战还真是个滑稽的谢幕方式啊。{wait}'
						'{page}'
						'#15502F本来还希望能让我\n'
						'玩得再开心一些呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(14), Text(
						'#0402F啊哈哈，这位姐姐好坏啊。\n'
						'都已经一周了……\n'
						'那位先生也算是很能忍了。{wait}'
						'{page}'
						'#0404F不过，我倒是有些\n'
						'担心，当忍耐到极限\n'
						'之后会怎么收场……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F（究竟在说些什么呢……）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(15), Text(
						'#15505F嗯……？\n'
						'啊，真是个可爱的孩子啊。{wait}'
						'{page}'
						'#15500F和我家的晶歌\n'
						'好像差不多同岁呢。{wait}'
						'{page}'
						'#15502F我的店叫纳因瓦利，\n'
						'离这里很近的。\n'
						'哈，见到晶歌就陪她玩玩吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1413)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(15), Text(
				'#15505F……哎呀，都已经是早上了啊。{wait}'
				'{page}'
				'#15506F哎呀呀，又喝了\n'
				'一个通宵呢。{wait}'
				'{page}'
				'#15503F晶歌应该\n'
				'按时开店了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(9)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(15), Text(
				'#15509F呵呵，虽然看店的都是一些讨厌的臭小子，\n'
				'但这里的鸡尾酒还真是很地道呢。{wait}'
				'{page}'
				'#15502F怎么样，如果有兴趣的话，\n'
				'我也可以请你们喝一杯哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('CHAR_SET_FRAME', Char(15), 1),
	Insn('RETURN'),
]

data['code'][39] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'阿赛尔……\n'
						'你到底打算干什么啊……！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'你知道姐姐和\n'
						'约葛特有多\n'
						'担心你吗……！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(8)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'你在听我说话吗，阿赛尔……！{wait}'
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

data['code'][40] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
					Insn('TEXT_TALK', Char(17), Text(
						'真是有些不好意思，\n'
						'我之前确实是对他们有些偏见呢。{wait}'
						'{page}'
						'虽然是不良成员，\n'
						'但好像并不是什么坏人。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(17), Text(
						'哎呀，庆典真是开心啊！{wait}'
						'{page}'
						'虽说是旧市街的不良组织，\n'
						'但成员却并不是一些坏人呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
					Insn('TEXT_TALK', Char(17), Text(
						'哈哈哈，其实我也\n'
						'很擅长打撞球的！{wait}'
						'{page}'
						'嘿嘿，\n'
						'马上还要再进一球哦！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CHAR_WATCH', Char(17), Char(11), 0),
					Insn('TEXT_TALK', Char(17), Text(
						'……好，轮到我击球啦。{wait}'
						'{page}'
						'哈哈，好好看着吧。\n'
						'撞球可是我长项中的长项啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_FLAG1_UNSET', Char(17), 16),
					Insn('FLAG_SET', Flag(6)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
			Insn('TEXT_TALK', Char(17), Text(
				'哎呀，这里还真是间很不错的酒吧呢，\n'
				'今天应该能好好品尝一番了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('0x4B', Char(12), -1),
			Insn('0x4B', Char(17), -1),
			Insn('TEXT_TALK', Char(17), Text(
				'啊，那个，一杯威士卡……{wait}'
				'{page}'
				'要大杯的哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'一杯大杯的威士卡吗，\n'
				'马上就给您调制好。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_FLAG1_UNSET', Char(17), 16),
			Insn('FLAG_SET', Flag(6)),
			Insn('0x4C', Char(12), -1),
			Insn('0x4C', Char(17), -1),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][41] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
					Insn('TEXT_TALK', Char(18), Text(
						'怎、怎么会……\n'
						'……如果是瓦奇先生，我……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CALL', Function((0, 11))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('0x4B', Char(10), -1),
			Insn('TEXT_TALK', Char(18), Text(
				'瓦奇先生今天\n'
				'不在吗……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'不、不好意思，是的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'瓦奇他今天不在。\n'
				'我说……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'从刚才开始，同样的问题\n'
				'你已经问过我无数次了啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x4C', Char(10), -1),
		]),
		(None, [
			Insn('CALL', Function((0, 42))),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][42] = [
	Insn('0x4B', Char(18), -1),
	Insn('0x4B', Char(19), -1),
	Insn('TEXT_TALK', Char(18), Text(
		'喂喂，那不就是那个人吗～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(18), Text(
		'昨天那个冷峻的美少年！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'哎呀，他在喝鸡尾酒～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'好丄可丄爱丄呀～㈱{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(18), -1),
	Insn('0x4C', Char(19), -1),
	Insn('RETURN'),
]

data['code'][43] = [
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
	Insn('CALL', Function((0, 44))),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][44] = [
	Insn('CHAR_SET_FRAME', Char(20), 0),
	Insn('CHAR_SET_FRAME', Char(21), 0),
	Insn('TEXT_TALK', Char(20), Text(
		'瓦奇先生今天也不在啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'唉，那冷峻的眼神……\n'
		'……清爽飘逸，有着神秘色泽的秀发……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'瓦奇先生到底\n'
		'去哪里了呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][45] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
					Insn('TEXT_TALK', Char(19), Text(
						'（梳理头发）……\n'
						'不、不知为何，心中很苦闷……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CALL', Function((0, 11))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(19), Text(
				'今天也到这里来了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(19), Text(
				'瓦奇先生，为什么今天\n'
				'不让我见到你呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('CALL', Function((0, 42))),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][46] = [
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
	Insn('CALL', Function((0, 44))),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][47] = [
	Insn('TEXT_START', Char(254)),
	Insn('CHAR_SET_FRAME', Char(22), 0),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('END')]), [
					Insn('CHAR_SET_FRAME', Char(22), 1),
					Insn('TEXT_TALK', Char(22), Text(
						'啊～是吗～\n'
						'确实如此呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(22), Text(
						'旧市街的人\n'
						'应该都很贫穷呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CALL', Function((0, 48))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(7)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(22), 1),
			Insn('TEXT_TALK', Char(22), Text(
				'不错啊，真刺激。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(22), Text(
				'我相当开心呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('CALL', Function((0, 49))),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][48] = [
	Insn('CHAR_SET_FRAME', Char(22), 1),
	Insn('CHAR_SET_FRAME', Char(23), 2),
	Insn('TEXT_TALK', Char(22), Text(
		'这里的酒保先生\n'
		'超级魁梧呢～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'莫非他是个\n'
		'黑道人士吗～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'笨蛋～只有市区里\n'
		'才会有什么黑道吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'而且黑道成员怎么可能会这么穷呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(7)),
	Insn('RETURN'),
]

data['code'][49] = [
	Insn('CHAR_SET_FRAME', Char(22), 1),
	Insn('CHAR_SET_FRAME', Char(23), 2),
	Insn('TEXT_TALK', Char(22), Text(
		'这里还真是个好地方啊，{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'果然来对了，是吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'明明是你一直走，\n'
		'最后走过头了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'听说旧市街的不良帮派\n'
		'都是一群超恐怖的家伙呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(7)),
	Insn('RETURN'),
]

data['code'][50] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('END')]), [
					Insn('CHAR_SET_FRAME', Char(23), 2),
					Insn('TEXT_TALK', Char(23), Text(
						'要说黑道什么的，\n'
						'应该是像鲁巴彻那样的组织吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(23), Text(
						'他们可是超级有钱的，\n'
						'旧市街里可不会有那种组织啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CALL', Function((0, 48))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(7)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(23), 2),
			Insn('TEXT_TALK', Char(23), Text(
				'旧市街的不良帮派\n'
				'之前好像和黑道组织斗争过吧？\n'
				'那绝对都是一群超级凶残的家伙。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(23), Text(
				'……哈，其实我也没有\n'
				'亲眼看到啦～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('CALL', Function((0, 49))),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][51] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch30950', 30),
	Insn('LOAD_CHCP', 'chr/ch31850', 31),
	Insn('CAM_OFFSET', (12000, 1000, 12000), 0),
	Insn('CAM_ROTATE', 33, 27, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 21500, 0),
	Insn('CHAR_SET_POS', Char(257), (-300, 0, -500), 0),
	Insn('CHAR_SET_POS', Char(258), (500, 0, -500), 0),
	Insn('CHAR_SET_POS', Char(259), (-300, 0, -500), 0),
	Insn('CHAR_SET_POS', Char(260), (500, 0, -500), 0),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_SET', Char(14), 128),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_SET_CHCP', Char(8), 4),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('CHAR_FLAG1_SET', Char(8), 32768),
	Insn('CHAR_SET_POS', Char(8), (-2600, 50, 12600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 64),
	Insn('CHAR_FLAG1_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(10), 64),
	Insn('CHAR_FLAG1_SET', Char(11), 32768),
	Insn('CHAR_FLAG1_SET', Char(11), 64),
	Insn('0x4B', Char(9), -1),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('0x4B', Char(12), -1),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu00400.itp'),
	Insn('IMG_LOAD', ResId(1), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu04100.itp'),
	Insn('CAM_OFFSET', (4000, 1000, 7000), 8000),
	Insn('CAM_ROTATE', 25, 17, 0, 8000),
	Insn('CAM_DISTANCE', 23500, 8000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x6F', b'y'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (0, 1000, 1700), 0),
	Insn('CAM_ROTATE', 45, 27, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 25500, 0),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('CAM_DISTANCE', 24500, 2000),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (-500, 0, 2400), 2000, 0),
	]),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 400),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (700, 0, 2400), 2000, 0),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 400),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (-500, 0, 1200), 2000, 0),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 400),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (700, 0, 1200), 2000, 0),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10400226V#0105F#6P撞球桌……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10400227V#12P#0300F这就是所谓的撞球酒吧吗。\n'
		'还真是挺有情趣的呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10400228V#6P#0200F『崔尼蒂』……\n'
		'姑且是一家有经营许可的正规店面呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400229V#6P#0001F原来如此，这里就是\n'
		'『圣约帮』的集会所吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4B', Char(9), -1),
	Insn('CHAR_SET_POS', Char(9), (7200, 0, 9500), 180),
	Insn('CHAR_SET_COLOR', Char(9), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('TEXT_TALK2', Char(9), Translate('男人的声音'), Text(
		'#10400230V──有什么事？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_POS', Char(10), (7200, 0, 9500), 180),
	Insn('CHAR_SET_COLOR', Char(10), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_SET_POS', Char(11), (7200, 0, 9500), 180),
	Insn('CHAR_SET_COLOR', Char(11), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG2_UNSET', Char(11), 32768),
	Insn('CAM_OFFSET', (0, 1000, 3600), 3000),
	Insn('CAM_ROTATE', 45, 23, 0, 3000),
	Insn('CAM_DISTANCE', 22500, 3000),
	Insn('FORK_FUNC', Char(9), 3, Function((0, 52))),
	Insn('SLEEP', 700),
	Insn('FORK_FUNC', Char(10), 3, Function((0, 53))),
	Insn('SLEEP', 700),
	Insn('FORK_FUNC', Char(11), 3, Function((0, 54))),
	Insn('SLEEP', 1200),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(9), 3),
	Insn('FORK_AWAIT', Char(10), 3),
	Insn('FORK_AWAIT', Char(11), 3),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK2', Char(10), Translate('蓝衣青年'), Text(
		'#10400231V你们是……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(11), Translate('蓝衣青年'), Text(
		'#10400232V#5P警、警察局的走狗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(9), Translate('高大的光头男子'), Text(
		'#04100F#10400233V#5P……………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400234V#12P#0003F之前真是多谢配合了。{wait}'
		'{page}'
		'#10400235V#0000F这里好像正在营业吧，\n'
		'那我们就打扰一下了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(10), Translate('蓝衣青年'), Text(
		'#10400236V真、真够厚颜无耻的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(10), 31),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('CHAR_SET_CHCP', Char(11), 30),
	Insn('CHAR_SET_FRAME', Char(11), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x0D'),
	Insn('TEXT_TALK2', Char(10), Translate('蓝衣青年'), Text(
		'#10400237V#1P……你们来干什么！？\n'
		'如果没有一个像样的回答，可别想就这么回去了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(11), Translate('蓝衣青年'), Text(
		'#10400238V#5P刚、刚才的账，\n'
		'就连本带利和你们算清楚……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(9), Translate('高大的光头男子'), Text(
		'#04100F#10400239V#5P──慢着。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(10), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(11), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(10), 3),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('CHAR_SET_CHCP', Char(11), 2),
	Insn('CHAR_SET_FRAME', Char(11), 0),
	Insn('0x0D'),
	Insn('TEXT_TALK2', Char(10), Translate('蓝衣青年'), Text(
		'#10400240V#1P阿巴斯……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(11), Translate('蓝衣青年'), Text(
		'#10400241V#5P为、为什么阻止我们……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(9), Translate('高大的光头男子'), Text(
		'#04100F#10400242V#5P这里是圣域──\n'
		'不要引发不必要的骚乱。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(9), 0, 400),
	Insn('TEXT_TALK2', Char(9), Translate('高大的光头男子'), Text(
		'#04100F#10400243V#11P瓦奇，怎么办？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(8), Translate('声音'), Text(
		'#10400244V……嗯～这个嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-2600, 1000, 12600), 2000),
	Insn('CAM_ROTATE', 35, 23, 0, 2000),
	Insn('CAM_DISTANCE', 22000, 2000),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400245V#0404F只是进来也无所谓吧？\n'
		'让他们过来好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(9), Translate('高大的光头男子'), Text(
		'#04100F#10400246V……明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (0, 1000, 3600), 0),
	Insn('CAM_ROTATE', 45, 23, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 22500, 0),
	Insn('0x0D'),
	Insn('CHAR_ROTATE', Char(9), 180, 500),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(9), 500),
	]),
	Insn('FORK', 9, 1, [
		Insn('0x98', Char(254), (1300, 0, 0), 1500, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 10, 1, [
		Insn('0x98', Char(254), (1300, 0, 0), 1500, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 11, 1, [
		Insn('0x98', Char(254), (1300, 0, 0), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(9), 1),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('CHAR_WATCH', Char(9), Char(257), 500),
	Insn('TEXT_TALK2', Char(9), Translate('高大的光头男子'), Text(
		'#04100F#10400247V#5P……………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400248V#12P#0005F多、多谢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10400249V#4P#0305F（怎么回事，这种举动……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10400250V#0106F#6P（看起来简直像是在举行某种仪式呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 0, 500),
	Insn('FORK', 257, 1, [
		Insn('0x98', Char(254), (-1000, 0, 4000), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x98', Char(254), (-1000, 0, 4000), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x98', Char(254), (-1000, 0, 4000), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('0x98', Char(254), (-1000, 0, 4000), 2000, 0),
	]),
	Insn('SLEEP', 1500),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-2500, 1100, 10700), 0),
	Insn('CAM_ROTATE', 37, 21, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 22500, 0),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(259), 1),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('CHAR_SET_POS', Char(257), (-1600, 0, 6700), 0),
	Insn('CHAR_SET_POS', Char(258), (-600, 0, 6700), 0),
	Insn('CHAR_SET_POS', Char(259), (-1500, 0, 5500), 0),
	Insn('CHAR_SET_POS', Char(260), (-500, 0, 5500), 0),
	Insn('CHAR_SET_POS', Char(9), (1000, 0, 2400), 0),
	Insn('CHAR_SET_POS', Char(10), (1900, 0, 1700), 0),
	Insn('CHAR_SET_POS', Char(11), (1900, 0, 500), 0),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (-2600, 0, 9700), 2000, 0),
	]),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (-1600, 0, 9700), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (-2500, 0, 8500), 2000, 0),
	]),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (-1500, 0, 8500), 2000, 0),
	]),
	Insn('FORK', 9, 1, [
		Insn('0x96', Char(254), (0, 0, 11400), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 10, 1, [
		Insn('0x96', Char(254), (900, 0, 10700), 2000, 0),
	]),
	Insn('FORK', 11, 1, [
		Insn('0x96', Char(254), (900, 0, 9500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(9), 1),
	Insn('FORK', 9, 2, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('FORK', 10, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('FORK', 11, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('CHAR_FLAG1_SET', Char(8), 32),
	Insn('FORK', 8, 1, [
		Insn('0x96', Char(254), (-2500, 50, 12400), 1000, 0),
	]),
	Insn('FORK', 8, 2, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('FORK_AWAIT', Char(8), 2),
	Insn('CHAR_SET_FRAME', Char(8), 2),
	Insn('CHAR_FLAG1_UNSET', Char(8), 32),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 300),
	Insn('SOUND_PLAY', 1432, 0, 255, 90),
	Insn('TEXT_MESSAGE', Char(8), Text(
		'#10400251V──那么，有何贵干？{wait}'
		'{page}'
		'#10400252V我不是已经说过了吗？\n'
		'和警察局的走狗没什么好说的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400253V#12P#0003F虽然你没什么可说的，\n'
		'但我却有些事想问。{wait}'
		'{page}'
		'#10400254V#0000F希望你们能稍微配合一下，\n'
		'协助我们的调查工作。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400255V#5P#0403F哼～调查啊。{wait}'
		'{page}'
		'#10400256V#0402F我先把话说在前面，\n'
		'我们和剑蛇帮的决战是势在必行的，\n'
		'不要妄图去阻止。{wait}'
		'{page}'
		'#10400257V#0404F也许确实会给附近的居民造成不便，\n'
		'不过也没办法，只能让他们稍微忍耐一下了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400258V#12P#0003F我们并不是来\n'
		'阻止你们进行争斗的。{wait}'
		'{page}'
		'#10400259V#0001F只是想来问一问──\n'
		'你们决心要彻底击溃对方的理由……{wait}'
		'{page}'
		'#10400260V究竟是什么呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(8), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(10), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(11), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(9), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400261V#5P#0400F喔……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(10), Translate('蓝衣青年'), Text(
		'#10400262V#2P那、那是因为……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(9), Translate('高大的光头男子'), Text(
		'#04100F#10400263V#5P──不要多嘴，\n'
		'一切都交给瓦奇吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(10), Translate('蓝衣青年'), Text(
		'#10400264V#2P啊，好的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400265V#12P#0001F……看他这种反应，\n'
		'好像确实是有什么内情吧。{wait}'
		'{page}'
		'#10400266V可不可以告诉我们呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 150),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_POS', Char(8), (-2600, 0, 11500), 180),
	Insn('CHAR_SET_CHCP', Char(8), 0),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 45579, 158, 255, 90),
	Insn('TEXT_TALK', Char(8), Text(
		'#0403F#5A──我说啊。{wait}'
	)),
	Insn('SLEEP', 800),
	Insn('FORK', 8, 1, [
		Insn('0x96', Char(254), (-2600, 0, 10900), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400268V#0400F就算知道了，你们又能怎样？{wait}'
		'{page}'
		'#10400269V如果是游击士，倒也罢了……\n'
		'警察又能起到什么作用呢？{wait}'
		'{page}'
		'#10400270V难道还会帮助我们这些居住在\n'
		'旧市街的危险分子？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400271V#12P#0006F……我承认，警察局在这方面的\n'
		'应对措施确实是不够充分。{wait}'
		'{page}'
		'#10400272V而且就算知道了理由，\n'
		'我们也不一定能帮助你们。{wait}'
		'{page}'
		'#10400273V#0000F毕竟我们的工作性质，和以保卫市民\n'
		'为首要目的的游击士并不相同。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('TEXT_TALK', Char(260), Text(
		'#10400274V#0301F喂、喂……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10400275V#0101F#11P等一下，罗伊德……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400276V#0404F哎呀呀，和你真是很难沟通。{wait}'
		'{page}'
		'#10400277V#0402F连最基本的互利关系都不存在，\n'
		'就想套出我的情报吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400278V#12P#0004F──不，互利关系是存在的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400279V#0405F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400280V#12P#0001F搜查官的工作，就是将\n'
		'埋藏在黑暗深处的真相查明，\n'
		'为市民与社会带来光明……{wait}'
		'{page}'
		'#10400281V至少，我就是在这样的\n'
		'教育下成长的。{wait}'
		'{page}'
		'#10400282V#0004F哪怕只是一点点也好，\n'
		'如果你们对此次事件的内幕还抱有疑问……{wait}'
		'{page}'
		'#10400283V我们就一定会帮忙将其中的真相彻底查明。{wait}'
		'{page}'
		'#10400284V#0000F这就是……\n'
		'我们可以提供的『利』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10400285V#0105F#11P……啊…………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10400286V#0302F还真是会说呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10400287V#12P#0202F………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 150),
	Insn('SOUND_PLAY', 1434, 0, 255, 100),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400288V#0404F…………哼哼……………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('0x82', 100, 0, 3000, 500),
	Insn('SOUND_PLAY', 1431, 0, 255, 100),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400289V#0409F#4S啊哈哈哈哈哈哈哈！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400290V#0402F好！很好很好！{wait}'
		'{page}'
		'#10400291V这种一本正经的说词\n'
		'还真是难得听到一回啊！{wait}'
		'{page}'
		'#10400292V#0409F你是叫罗伊德吧！？\n'
		'哈哈～我很欣赏你！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400293V#12P#0006F……我并不是为了\n'
		'讨好你才说这些的啊。{wait}'
		'{page}'
		'#10400294V#0001F那么，究竟是为什么呢？{wait}'
		'{page}'
		'#10400295V『你们非要将对方彻底击溃的理由』……\n'
		'可以告诉我们了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 8, 1, [
		Insn('0x96', Char(254), (-2600, 0, 11500), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_POS', Char(8), (-2500, 50, 12400), 135),
	Insn('CHAR_SET_CHCP', Char(8), 4),
	Insn('CHAR_SET_FRAME', Char(8), 2),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400296V#5P#0404F#5P……呵呵，好吧。{wait}'
		'{page}'
		'#10400297V你都已经说出那么正经八百的话了，\n'
		'我再不表示一下，岂不是显得很小气。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400298V#5P#0402F──阿巴斯，\n'
		'告诉他们吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(9), Char(8), 400),
	Insn('TEXT_TALK2', Char(9), Translate('高大的光头男子'), Text(
		'#04100F#10400299V#11P……明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-2140, 1100, 10430), 1000),
	Insn('FORK', 9, 2, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('SLEEP', 1000),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(1), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 300),
	Insn('TEXT_SET_NAME', Translate('高大的光头男子')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#10400300V#5P我还没有自报家门。{wait}'
		'{page}'
		'#10400301V#5P我叫阿巴斯。\n'
		'是圣约帮的一员。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(1), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 0))),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400302V#6P#0005F啊……请多指教。{wait}'
		'\n'
		'#10400303V#0001F（好魁梧啊……他到底是做什么的？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#04100F#10400304V#5P事件的开端，是五天前的夜晚。{wait}'
		'{page}'
		'#04100F#10400305V#5P我们的一名成员\n'
		'在附近的偏僻小巷中\n'
		'被剑蛇帮的人暗算了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400306V#6P#0007F暗算……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10400307V#6P#0101F那个……\n'
		'并不是普通的打架吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(10), Translate('蓝衣青年'), Text(
		'#10400308V#11P哼，怎么会是普通的打架……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(10), Translate('蓝衣青年'), Text(
		'#10400309V#11P后脑部位挨了重重的一击，\n'
		'倒下之后又被围殴了一顿呢！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(11), Translate('蓝衣青年'), Text(
		'#10400310V完、完全是单方面的袭击……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(11), Translate('蓝衣青年'), Text(
		'#10400311V被暗算的那个同伴……\n'
		'已、已经被送到医院了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10400312V#12P#0306F下手还真是挺重的啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400313V#6P#0001F那个……\n'
		'受害者目前的伤势如何了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#04100F#10400314V#5P据医院那边的人说，\n'
		'现在好像还没有恢复意识。{wait}'
		'{page}'
		'#04100F#10400315V#5P医疗救治工作虽然已经完成了，\n'
		'但毕竟是头部受到了重击……{wait}'
		'{page}'
		'#04100F#10400316V#5P目前还在等待联系呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400317V#6P#0003F是吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10400318V#6P#0101F……那个，你们一直都\n'
		'没有报警吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#04100F#10400319V#5P就算报警，那些家伙也不会\n'
		'为了我们而出动的。{wait}'
		'{page}'
		'#04100F#10400320V#5P而且，犯人是谁，已经一目了然了。\n'
		'如果通报警察，反而会影响我们的复仇计划。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10400321V#6P#0108F……是吗。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(259), Text(
		'#10400322V#6P#0205F──请等一下。{wait}'
		'{page}'
		'#10400323V#0200F被袭击的人好像\n'
		'还没有恢复意识吧……{wait}'
		'{page}'
		'#10400324V既然如此，各位为什么\n'
		'就能肯定犯人是\n'
		'『剑蛇帮』的人呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400325V#6P#0005F这么一说……{wait}'
		'{page}'
		'#10400326V该不会是……\n'
		'单靠臆测而得出的结论吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(8), 2),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400327V#5P#0404F……哈，再怎么说，\n'
		'我们也不会武断到那种程度啊。{wait}'
		'{page}'
		'#10400328V#0402F再怎么说，我们也和那些家伙不同，\n'
		'算是知性派的组织呢。{wait}'
		'{page}'
		'#10400329V#0409F哈哈，不过，仔细想想的话，\n'
		'区区不良帮派说什么知性派也很可笑呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(10), Translate('蓝衣青年'), Text(
		'#10400330V#11P瓦奇……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400331V#5P#0404F呵呵，我们之所以断定\n'
		'犯人是他们，理由就是……{wait}'
		'{page}'
		'#10400332V#0400F你既然是个搜查官，\n'
		'想必已经有头绪了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400333V#12P#0003F………这个嘛…………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('MENU', 0, -1, -1, 0, Text(
		'【遭到袭击的场所】\n'
		'【受袭成员的伤口】\n'
		'【留在现场的脚印】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('TEXT_TALK', Char(257), Text(
				'#10400334V#12P#0001F那名成员受到袭击的场所……\n'
				'应该就是决定性的证据吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#10400335V#5P#0406F嗯～刚才都已经说过了，\n'
				'他们发动袭击的场所就是附近的偏僻小巷。{wait}'
				'{page}'
				'#10400336V#0400F剑蛇帮的人虽然也会从那里经过，\n'
				'但这显然不能算是什么决定性的证据。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#10400337V#12P#0005F是、是吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F#10400338V#5P──决定性的证据，\n'
				'就是受袭成员的伤口。{wait}'
				'{page}'
				'#04100F#10400339V#5P虽然主要是由钝器击打而造成的，\n'
				'但同时还有一些很明显的裂口……{wait}'
				'{page}'
				'#04100F#10400340V#5P感觉就像是某种坚硬的\n'
				'尖锐物体造成的撕裂伤口。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('QUEST_BONUS_DP', 62, 2),
			Insn('0xD0', 6, Expr([Insn('CONST', 2), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#10400341V#12P#0008F……是吗，我明白了。{wait}'
				'{page}'
				'#10400342V#0001F决定性的证据应该\n'
				'就是受袭成员的伤口吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#10400343V#5P#0409F答对啦，果然有一套嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F#10400344V#5P伤口虽然主要是由钝器击打而造成的，\n'
				'但同时还有一些很明显的裂口……{wait}'
				'{page}'
				'#04100F#10400345V#5P感觉就像是某种坚硬的\n'
				'尖锐物体造成的撕裂伤口。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		2: [
			Insn('QUEST_BONUS_DP', 62, 1),
			Insn('0xD0', 6, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#10400346V#12P#0008F你们和他们都穿着\n'
				'很独特的鞋子……{wait}'
				'{page}'
				'#10400347V#0001F决定性的证据，莫非就是\n'
				'残留在现场的脚印吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#10400348V#5P#0405F嘿，很有趣的观点啊。{wait}'
				'{page}'
				'#10400349V#0406F不过呢，旧市街的路面\n'
				'都是用陈旧的石板铺设而成的，\n'
				'基本留不下什么脚印。{wait}'
				'{page}'
				'#10400350V#0400F而且他们平时也经常会路过那里，\n'
				'所以并不能算是什么决定性的证据。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#10400351V#12P#0005F是吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'#04100F#10400352V#5P──决定性的证据，\n'
				'就是受袭成员的伤口。{wait}'
				'{page}'
				'#04100F#10400353V#5P虽然主要是由钝器击打而造成的，\n'
				'但同时还有一些很明显的裂口……{wait}'
				'{page}'
				'#04100F#10400354V#5P感觉就像是某种坚硬的\n'
				'尖锐物体造成的撕裂伤口。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('TEXT_TALK', Char(258), Text(
		'#10400355V#0105F#12P由钝器击打造成的伤口，\n'
		'还有坚硬的尖锐物体造成的裂伤……{wait}'
		'{page}'
		'#10400356V#0101F……啊……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10400357V#0301F#12P……原来如此，\n'
		'就是那些家伙用的钉棍吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10400358V#6P#0204F这种明显的特征，也许确实\n'
		'可以算是决定性的证据呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400359V#12P#0003F──事情的经过，我已经大致了解了。{wait}'
		'{page}'
		'#10400360V#0000F谢谢，这些情报很有参考价值。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400361V#5P#0405F有用就好，不过……\n'
		'只要这点情报就够了吗？{wait}'
		'{page}'
		'#10400362V难道不想说些『请停止报复行为』\n'
		'之类的劝言吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400363V#12P#0006F以我个人的立场来说，\n'
		'当然是很想阻止你们……{wait}'
		'{page}'
		'#10400364V#0001F但目前掌握到的判断材料实在是太少了。{wait}'
		'{page}'
		'#10400365V我们还要去剑蛇帮那边了解一下情况，\n'
		'如果有什么新发现，会再来和你们联系的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400366V#5P#0404F呵呵，原来如此。\n'
		'无论如何也要执着于所谓的『调查』啊。{wait}'
		'{page}'
		'#10400367V#0402F既然如此，我就期待着\n'
		'你们给我带来一些有趣的消息了。{wait}'
		'{page}'
		'#10400368V#0409F──呵呵，不过，如果没有什么进展，\n'
		'旧市街可就要迎来一场腥风血雨了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400369V#12P#0003F………明白了。{wait}'
		'{page}'
		'#10400370V#0000F我们不会辜负你的期待，\n'
		'一定能带回你所谓的有趣的消息。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('CHAR_FLAG1_UNSET', Char(8), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(9), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(9), 64),
	Insn('CHAR_FLAG1_UNSET', Char(10), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(10), 64),
	Insn('CHAR_FLAG1_UNSET', Char(11), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(11), 64),
	Insn('CHAR_SET_CHCP', Char(8), 4),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('CHAR_SET_POS', Char(8), (-2600, 50, 12600), 0),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG1_UNSET', Char(14), 128),
	Insn('CHAR_SET_POS', Char(9), (2980, 0, 14780), 180),
	Insn('0x4C', Char(9), -1),
	Insn('CHAR_SET_POS', Char(10), (2950, 30, 6580), 180),
	Insn('0x4C', Char(10), -1),
	Insn('CHAR_SET_POS', Char(11), (10230, 0, 4410), 90),
	Insn('0x4C', Char(11), -1),
	Insn('0x4C', Char(12), -1),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG2_UNSET', Char(12), 32768),
	Insn('CAM_OFFSET', (0, 1100, 9500), 0),
	Insn('CAM_ROTATE', 45, 30, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(0), (0, 0, 9500), 180),
	Insn('CHAR_SET_POS', Char(1), (0, 0, 9500), 180),
	Insn('CHAR_SET_POS', Char(2), (0, 0, 9500), 180),
	Insn('CHAR_SET_POS', Char(3), (0, 0, 9500), 180),
	Insn('0x0A', 268435456),
	Insn('FLAG_SET', Flag(529)),
	Insn('QUEST', 62, Insn('TASK_SET', 2)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][52] = [
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (7200, 0, 7000), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (2000, 0, 7000), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 9, 1, [
		Insn('0x95', Char(254), (0, 0, 4800), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(9), 1),
	Insn('CHAR_ROTATE', Char(9), 180, 500),
	Insn('RETURN'),
]

data['code'][53] = [
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (7200, 0, 7000), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (2000, 0, 7000), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 10, 1, [
		Insn('0x95', Char(254), (-600, 0, 6100), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('CHAR_ROTATE', Char(10), 180, 500),
	Insn('RETURN'),
]

data['code'][54] = [
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (7200, 0, 7000), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (2000, 0, 7000), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 11, 1, [
		Insn('0x95', Char(254), (700, 0, 6700), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('CHAR_ROTATE', Char(11), 180, 500),
	Insn('RETURN'),
]

data['code'][55] = [
	Insn('EVENT_BEGIN', 0),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu04100.itp'),
	Insn('0x4B', Char(9), -1),
	Insn('CHAR_WATCH', Char(0), Char(9), 0),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (2960, 1100, 12800), 0),
	Insn('CAM_ROTATE', 47, 15, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25980, 0),
	Insn('CHAR_SET_POS', Char(257), (2740, 0, 11700), 0),
	Insn('CHAR_SET_POS', Char(258), (1500, 0, 10260), 0),
	Insn('CHAR_SET_POS', Char(259), (1500, 0, 11700), 0),
	Insn('CHAR_SET_POS', Char(260), (2740, 0, 10260), 0),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 300),
	Insn('TEXT_SET_NAME', Translate('阿巴斯')),
	Insn('TEXT_MESSAGE', Char(9), Text(
		'#5P……来了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_TALK', Char(257), Text(
		'#0003F#11P……来是来了，但这不是重点。{wait}'
		'{page}'
		'#0001F所谓的『训练圣约帮成员』……\n'
		'这种委托内容也太乱来了吧。{wait}'
		'{page}'
		'警察怎么可能\n'
		'训练不良少年啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0105F委托人的姓名并不是瓦奇，\n'
		'而是您，也就是说……\n'
		'这是您的主意吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#04100F#5P嗯，看起来，\n'
		'你们好像是有些误会呢。{wait}'
		'{page}'
		'#04100F#5P我先来说明一下吧，\n'
		'请到这边来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('FORK_LOOP', 0, 1, [
		Insn('CHAR_WATCH', Char(254), Char(9), 300),
	]),
	Insn('FORK_LOOP', 1, 1, [
		Insn('CHAR_WATCH', Char(254), Char(9), 300),
	]),
	Insn('FORK_LOOP', 2, 1, [
		Insn('CHAR_WATCH', Char(254), Char(9), 300),
	]),
	Insn('FORK_LOOP', 3, 1, [
		Insn('CHAR_WATCH', Char(254), Char(9), 300),
	]),
	Insn('FORK', 9, 0, [
		Insn('0x95', Char(254), (7550, 0, 14780), 1000, 0),
	]),
	Insn('SLEEP', 400),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(0), 1),
	Insn('FORK_QUIT', Char(1), 1),
	Insn('FORK_QUIT', Char(2), 1),
	Insn('FORK_QUIT', Char(3), 1),
	Insn('FORK_QUIT', Char(9), 0),
	Insn('CAM_OFFSET', (1290, 1000, 9450), 0),
	Insn('CAM_ROTATE', 52, 17, 0, 0),
	Insn('0x6E', 340, 0),
	Insn('CAM_DISTANCE', 25010, 0),
	Insn('CHAR_SET_POS', Char(9), (3060, 0, 8960), 270),
	Insn('CHAR_SET_POS', Char(257), (700, 0, 9600), 90),
	Insn('CHAR_SET_POS', Char(258), (560, 0, 8000), 90),
	Insn('CHAR_SET_POS', Char(259), (-990, 0, 8000), 90),
	Insn('CHAR_SET_POS', Char(260), (-990, 0, 9600), 90),
	Insn('0x4B', Char(13), -1),
	Insn('0x4B', Char(12), -1),
	Insn('0x4B', Char(10), -1),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_SET_POS', Char(13), (14390, 0, 7400), 178),
	Insn('CHAR_SET_POS', Char(12), (14000, 0, 7400), 268),
	Insn('CHAR_SET_POS', Char(10), (9250, 0, 4150), 225),
	Insn('CHAR_SET_POS', Char(11), (5000, 0, 2000), 90),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('SLEEP', 800),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(9), Text(
		'#04100F#11P其实这件委托并没有那么复杂。{wait}'
		'{page}'
		'#04100F#11P──想委托你们的，\n'
		'只是指导我们的成员学习防身术而已。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 200),
	Insn('EMOTE', Char(0), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 8),
	Insn('EMOTE', Char(1), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 12),
	Insn('EMOTE', Char(2), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(3), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F……哎…………！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#6P#0305F防身术……？{wait}'
		'{page}'
		'#0301F喂喂，让他们学习那种东西，\n'
		'难道是想用来打架吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#04100F#11P我刚才说过，你们误会了。{wait}'
		'{page}'
		'#04100F#11P我们要警惕的敌人是黑手党。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0200F黑手党……\n'
		'鲁巴彻或是黑月吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#6P#0101F说起来，\n'
		'这些黑手党组织最近\n'
		'好像开始互相争斗了呢……{wait}'
		'{page}'
		'#0103F虽然都是些零星的活动，\n'
		'但听说有时也会出现\n'
		'枪击行为呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#04100F#11P正是如此。{wait}'
		'{page}'
		'#04100F#11P而且，旧市街往往\n'
		'处于风口浪尖的位置。{wait}'
		'{page}'
		'#04100F#11P因为附近尽是一些仓库、废屋、空地……\n'
		'对他们来说，都是些开战的好地方吧。{wait}'
		'{page}'
		'#04100F#11P对我们而言，\n'
		'这种状况实在是不容乐观。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0203F所以才想学习防身术……您是这个意思吧。{wait}'
		'{page}'
		'#0200F……话说起来，\n'
		'在旧市街之前的那起事件中，圣约帮就有\n'
		'一名成员遭到暗算，昏迷了整整一周呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0001F……原来如此…………\n'
		'是这么一回事啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#04102F#11P你们理解得很快。{wait}'
		'{page}'
		'#04100F#11P按照我们原本的方案，\n'
		'本来是想让大家学习\n'
		'瓦奇的格斗技……{wait}'
		'{page}'
		'#04100F#11P但他的战斗技术比较特殊，\n'
		'需要肢体有先天的柔软度。\n'
		'若缺乏合适的体质，便无法顺利掌握。{wait}'
		'{page}'
		'#04100F#11P而罗伊德丄班宁斯曾经使用过的\n'
		'警察特有的防身术很值得借鉴。{wait}'
		'{page}'
		'#04100F#11P不仅拥有出色的防御效果，\n'
		'而且技巧比较主流，人人皆可学习……{wait}'
		'{page}'
		'#04100F#11P……那种战斗方式，\n'
		'能否通过实战练习，\n'
		'让我们的成员再见识一次呢？{wait}'
		'{page}'
		'#04100F#11P当然了，这种技术肯定也不是一朝一夕\n'
		'就能掌握的。但只需在他们的心中留下印象，\n'
		'就能产生很好的刺激与督促效果了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 200),
	Insn('EMOTE', Char(0), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(1), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(2), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(3), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(0)),
	Insn('EMOTE_STOP', Char(1)),
	Insn('EMOTE_STOP', Char(2)),
	Insn('EMOTE_STOP', Char(3)),
	Insn('SLEEP', 300),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 400),
	]),
	Insn('SLEEP', 10),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 400),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 400),
	]),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 400),
	]),
	Insn('SLEEP', 400),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0100F看起来，好像确实是\n'
		'很正当的委托请求呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0203F嗯，既然如此，应该可以接受吧。{wait}'
		'{page}'
		'#0200F罗伊德前辈，要怎么做？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0003F实战形式的训练指导吗，\n'
		'这个嘛……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0001F其实我用的并不是防身术，\n'
		'而是在警察学校中学习的\n'
		'一种压制格斗技……{wait}'
		'{page}'
		'……这样也可以吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#04100F#11P当然。{wait}'
		'{page}'
		'#04100F#11P为了训练得彻底一些，\n'
		'你们那边的另外三位也可以参加。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F是吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, -1, 0, Text(
		'【接受】\n'
		'【放弃】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('QUEST', 18, Insn('TASK_SET', 1)),
			Insn('CALL', Function((0, 56))),
			Insn('RETURN'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#0001F#6P#0001F……请再稍等一下。\n'
		'我们也需要准备准备。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#04100F#11P是吗？{wait}'
		'{page}'
		'#04100F#11P我们今天一整天都有空。\n'
		'你们做好充足准备之后再来吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x4C', Char(13), -1),
	Insn('0x4C', Char(12), -1),
	Insn('0x4C', Char(10), -1),
	Insn('0x4C', Char(11), -1),
	Insn('CHAR_SET_POS', Char(13), (12470, 0, 16210), 180),
	Insn('CHAR_SET_POS', Char(12), (14030, 30, 11040), 270),
	Insn('CHAR_SET_POS', Char(10), (2950, 30, 6580), 180),
	Insn('CHAR_SET_POS', Char(11), (10230, 0, 4410), 90),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(13), (-4000, 0, 16690), 0),
		]),
		(None, []),
	]),
	Insn('FORK_FUNC', Char(10), 0, Function((0, 1))),
	Insn('CHAR_SET_POS', Char(0), (600, 0, 8000), 90),
	Insn('CHAR_SET_POS', Char(9), (2980, 0, 14780), 180),
	Insn('0x4C', Char(9), -1),
	Insn('FORK_FUNC', Char(9), 0, Function((0, 0))),
	Insn('QUEST', 18, Insn('TASK_SET', 0)),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][56] = [
	Insn('CHAR_FLAG1_SET', Char(13), 64),
	Insn('CHAR_FLAG1_SET', Char(12), 64),
	Insn('CHAR_FLAG1_SET', Char(10), 64),
	Insn('CHAR_FLAG1_SET', Char(11), 64),
	Insn('CHAR_SET_CHCP', Char(13), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F既然情况如此，\n'
		'我们自然没有拒绝的理由。{wait}'
		'{page}'
		'#0000F不如说，这也许还能\n'
		'帮助你们改过自新呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#6P#0306F呼……我就知道你会这么说啊。{wait}'
		'{page}'
		'#0300F罗伊德，即使是你，如果同时应付\n'
		'他们全体成员，恐怕也会吃不消吧。\n'
		'这种时候就不要客气了，让我们也加入吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 400),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 400),
	]),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 400),
	]),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0000F嗯，明白了。\n'
		'大家都来帮忙吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#04100F#11P那么，双方都已经达成一致了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('SLEEP', 300),
	Insn('CHAR_ROTATE', Char(9), 180, 400),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(9), Text(
		'#04107F#5P#4S──全员集合！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('CAM_OFFSET', (2240, 1100, 7350), 4200),
	Insn('CAM_ROTATE', 79, 30, 0, 4200),
	Insn('0x6E', 260, 4200),
	Insn('CAM_DISTANCE', 32250, 4200),
	Insn('FORK_FUNC', Char(10), 0, Function((0, 59))),
	Insn('SLEEP', 200),
	Insn('FORK_FUNC', Char(12), 0, Function((0, 58))),
	Insn('SLEEP', 400),
	Insn('FORK_FUNC', Char(13), 0, Function((0, 57))),
	Insn('SLEEP', 300),
	Insn('FORK_FUNC', Char(11), 0, Function((0, 60))),
	Insn('FORK', 0, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 300),
	]),
	Insn('SLEEP', 10),
	Insn('FORK', 1, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 300),
	]),
	Insn('FORK', 2, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 300),
	]),
	Insn('SLEEP', 8),
	Insn('FORK', 3, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 300),
	]),
	Insn('FORK_AWAIT', Char(13), 0),
	Insn('SLEEP', 700),
	Insn('TEXT_TALK', Char(9), Text(
		'#04107F#5P我们圣约帮现在就要\n'
		'展开模拟战斗了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', 290, 60, -1, -1),
	Insn('TEXT_SET_NAME', Translate('成员们')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#5S  明白！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 80, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}任务【圣约帮的训练委托】{color 0}开始！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 111), Insn('SET'), Insn('END')])),
	Insn('FLAG_SET', Flag(737)),
	Insn('NEW_SCENE', 'c1400', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][57] = [
	Insn('0x95', Char(13), (3340, 0, 7400), 2000, 0),
	Insn('0x95', Char(13), (2880, 30, 6910), 2000, 0),
	Insn('CHAR_ROTATE', Char(13), 315, 400),
	Insn('RETURN'),
]

data['code'][58] = [
	Insn('0x95', Char(12), (3340, 0, 7400), 2000, 0),
	Insn('0x95', Char(12), (2180, 0, 6080), 2000, 0),
	Insn('CHAR_ROTATE', Char(12), 315, 400),
	Insn('RETURN'),
]

data['code'][59] = [
	Insn('0x95', Char(10), (9250, 0, 7400), 2000, 0),
	Insn('0x95', Char(10), (3340, 0, 7400), 2000, 0),
	Insn('0x95', Char(10), (1330, 0, 5310), 2000, 0),
	Insn('CHAR_ROTATE', Char(10), 315, 400),
	Insn('RETURN'),
]

data['code'][60] = [
	Insn('0x95', Char(11), (2460, 20, 2000), 2000, 0),
	Insn('0x95', Char(11), (2460, 20, 4550), 2000, 0),
	Insn('0x95', Char(11), (490, 0, 4550), 2000, 0),
	Insn('CHAR_ROTATE', Char(11), 315, 400),
	Insn('RETURN'),
]
