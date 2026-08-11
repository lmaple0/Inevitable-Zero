# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't0500',
	'name2': 't0500',
	'location': 60,
	'bgm': 121,
	'flags': 8192,
	'includes': [
		't0500',
		't0520_1',
		None,
		None,
		None,
		None,
	],
	'name3': 't0500',
	'labels': [
		{
			'pos': (11.0, 0.0, -23.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('玛因兹山道'),
		},
		{
			'pos': (-32.0, 0.0, 62.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('玛因兹矿山'),
		},
		{
			'pos': (-19.75, 0.0, 45.75),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-3.0, 0.0, 49.0),
			'unk': b'\x00\x00R\x00',
			'name': Translate(''),
		},
		{
			'pos': (-4.5, 0.0, 28.600000381469727),
			'unk': b'\x00\x00U\x00',
			'name': Translate(''),
		},
		{
			'pos': (-14.5, 0.0, 24.75),
			'unk': b'\x00\x00V\x00',
			'name': Translate(''),
		},
	],
	'chcp': [
		'chr/ch23700',
		'chr/ch23600',
		'chr/ch23000',
		'chr/ch26200',
		'chr/ch26300',
		'chr/ch22000',
		'chr/ch32200',
		'chr/ch30700',
		'chr/ch22100',
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
		None,
		None,
		None,
		None,
		None,
	],
	'npcs': [
		{
			'name': Translate('亚米'),
			'pos': (6739, 0, 42729),
			'angle': 0,
			'_1': b'\x01\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((0, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('卡洛斯'),
			'pos': (10399, 0, 55259),
			'angle': 90,
			'_1': b'\x01\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('亚雷库'),
			'pos': (28329, -3000, 62000),
			'angle': 180,
			'_1': b'\x01\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 14)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('矿工罗基'),
			'pos': (15710, -9000, 39830),
			'angle': 225,
			'_1': b'\x81\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('霍夫曼矿山长'),
			'pos': (-24540, 11439, 55959),
			'angle': 90,
			'_1': b'\x81\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((0, 17)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('矿工冈兹'),
			'pos': (-21579, 11439, 57630),
			'angle': 180,
			'_1': b'\x81\x01\x00\x00\x07\x00\x00\x00',
			'function': Function((0, 18)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('矿工玛尔罗'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\x81\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 20)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('矿工马库斯'),
			'pos': (850, 6000, 77519),
			'angle': 0,
			'_1': b'\x81\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 21)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (4519, -2000, 25190),
			'angle': 0,
			'_1': b'\x81\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 22)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客露娜莉'),
			'pos': (-610, 0, 67440),
			'angle': 270,
			'_1': b'\x81\x01\x00\x00\x08\x00\x00\x00',
			'function': Function((0, 23)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客科比'),
			'pos': (870, 6000, 77220),
			'angle': 0,
			'_1': b'\x81\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((0, 24)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('车'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('矿工玛尔罗'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x03\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('黑手党'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('黑手党'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('索妮亚副司令'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('诺艾儿上士'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('巴士'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('警备队员'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('警备队员'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('警备队员'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('警备队员'),
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
	],
	'monsters': [],
	'triggers': [
		{
			'pos': (19.399999618530273, 63.29999923706055, -1.0),
			'range': 56.25,
			'transform': [
				0.3333333432674408,
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
				-6.4666666984558105,
				-12.65999984741211,
				0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 36)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (5.199999809265137, 58.400001525878906, -1.0),
			'range': 506.25,
			'transform': [
				0.06666667014360428,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.3333333432674408,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				-0.3466666638851166,
				-19.46666717529297,
				0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 37)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (-4600, -2000, 28700),
			'range': 1500,
			'bubble_pos': (-4600, -500, 28700),
			'_1': b'|\x00\x00',
			'function': Function((0, 25)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (12000, 400, 70000),
			'range': 1500,
			'bubble_pos': (12000, 1400, 70000),
			'_1': b'|\x00\x00',
			'function': Function((0, 26)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-13210, -2000, 25680),
			'range': 1200,
			'bubble_pos': (-13210, 0, 25680),
			'_1': b'|\x00\x00',
			'function': Function((0, 60)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-25900, 11440, 56000),
			'range': 1500,
			'bubble_pos': (-25900, 12940, 56000),
			'_1': b'|\x00\x00',
			'function': Function((0, 27)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00<\x00', Function((0, 3)), Function((0, 4))),
	'code': [None]*63,
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
		Insn('CHAR_IDLE', Char(254), (7320, 36570), (8000, 46890), 1000),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (25740, 59960), (29310, 62600), 1000),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('FORK_FUNC', Char(10), 0, Function((0, 2))),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('FORK_FUNC', Char(8), 0, Function((0, 1))),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_SET_POS', Char(14), (900, 6000, 77780), 0),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('FORK_FUNC', Char(8), 0, Function((0, 1))),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_SET_POS', Char(14), (900, 6000, 77780), 0),
		]),
		(Expr([Insn('FLAG', Flag(1547)), Insn('END')]), [
			Insn('FORK_FUNC', Char(8), 0, Function((0, 1))),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_SET_POS', Char(11), (910, 0, 50450), 90),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_SET_POS', Char(12), (-22550, 11440, 56120), 90),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_SET_POS', Char(14), (-20140, 11440, 57900), 45),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
		]),
		(Expr([Insn('FLAG', Flag(1544)), Insn('END')]), [
			Insn('FORK_FUNC', Char(8), 0, Function((0, 1))),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('FORK_FUNC', Char(8), 0, Function((0, 1))),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_SET_POS', Char(14), (900, 6000, 77780), 0),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('FORK_FUNC', Char(8), 0, Function((0, 1))),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('FORK_FUNC', Char(8), 0, Function((0, 1))),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(8), (4520, -2000, 26540), 180),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('FORK_FUNC', Char(8), 0, Function((0, 1))),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('FORK_FUNC', Char(8), 0, Function((0, 1))),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('FORK_FUNC', Char(8), 0, Function((0, 1))),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
		]),
		(Expr([Insn('FLAG', Flag(813)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(8), 128),
			Insn('CHAR_FLAG1_SET', Char(9), 128),
			Insn('CHAR_FLAG1_SET', Char(10), 128),
		]),
		(Expr([Insn('FLAG', Flag(812)), Insn('END')]), [
			Insn('FORK_FUNC', Char(8), 0, Function((0, 1))),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_SET_POS', Char(11), (-21670, 11440, 55170), 270),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_SET_POS', Char(14), (-21580, 11440, 56390), 0),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('FORK_FUNC', Char(8), 0, Function((0, 1))),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(806)), Insn('FLAG', Flag(809)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x09', 268435456),
			Insn('EVENT', Function((0, 30))),
		]),
		(Expr([Insn('FLAG', Flag(1546)), Insn('FLAG', Flag(1547)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 54))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 42))),
		]),
		(Expr([Insn('FLAG', Flag(737)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(737)),
			Insn('EVENT', Function((0, 47))),
		]),
		(Expr([Insn('FLAG', Flag(738)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(738)),
			Insn('EVENT', Function((0, 52))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1280)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1008)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(1008)),
			Insn('EVENT', Function((0, 7))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1009)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(1009)),
			Insn('0xD0', 1, Expr([Insn('CONST', 10), Insn('SET'), Insn('END')])),
			Insn('EVENT', Function((0, 9))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(813)), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('OBJ_FLAG_SET', Object(8), 4),
	Insn('OBJ_FLAG_SET', Object(11), 4),
	Insn('OBJ_SET_FRAME', Object(11), 'light', Insn('0', 1)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1055)), Insn('NOT'), Insn('FLAG', Flag(1040)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(11), 4),
			Insn('0x78', b'\x0b', Char(19)),
			Insn('CHAR_SET_POS', Char(19), (-14260, -2000, 24500), 0),
			Insn('0xD3', Char(19), 0, 145000, 0, 0),
		]),
		(None, []),
	]),
	Insn('0x65', 1, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(809)), Insn('FLAG', Flag(811)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x66', 1, 1),
			Insn('OBJ_FLAG_UNSET', Object(4), 16),
		]),
		(None, []),
	]),
	Insn('0x65', 3, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(813)), Insn('NOT'), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(6), 16),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(812)), Insn('NOT'), Insn('END')]), [
			Insn('0x66', 3, 1),
		]),
		(None, []),
	]),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('CALL', Function((0, 28))),
	Insn('OBJ_FLAG_SET', Object(9), 4),
	Insn('0x65', 2, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1545)), Insn('FLAG', Flag(1548)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('CHAR_FLAG2_UNSET', Char(19), 32768),
			Insn('OBJ_FLAG_UNSET', Object(9), 4),
			Insn('OBJ_FLAG_SET', Object(9), 2),
			Insn('OBJ_FLAG_SET', Object(9), 1024),
			Insn('CHAR_FLAG1_SET', Char(19), 32768),
			Insn('0x78', b'\t', Char(19)),
			Insn('OBJ_FLAG_SET', Object(9), 4096),
			Insn('OBJ_SET_FRAME', Object(9), 'light', Insn('0', 1)),
			Insn('CHAR_SET_POS', Char(19), (-14260, -2000, 24500), 0),
			Insn('0xD3', Char(19), 0, 145000, 0, 0),
			Insn('0x74', Object(9), 7680),
			Insn('0x70', Object(9), b'\x00\x00'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1547)), Insn('END')]), [
					Insn('0x66', 2, 1),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(809)), Insn('FLAG', Flag(811)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 29))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1537)), Insn('FLAG', Flag(1542)), Insn('NOT'), Insn('BOOL_AND'), Insn('0x23', 1), Insn('CONST', 10), Insn('EQ'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('CHAR_FLAG2_UNSET', Char(19), 32768),
			Insn('OBJ_FLAG_UNSET', Object(9), 4),
			Insn('OBJ_FLAG_SET', Object(9), 2),
			Insn('OBJ_FLAG_SET', Object(9), 1024),
			Insn('0x78', b'\t', Char(19)),
			Insn('OBJ_FLAG_SET', Object(9), 4096),
			Insn('OBJ_SET_FRAME', Object(9), 'light', Insn('0', 1)),
			Insn('CHAR_SET_POS', Char(19), (-14260, -2000, 24500), 0),
			Insn('0xD3', Char(19), 0, 145000, 0, 0),
			Insn('0x74', Object(9), 7680),
			Insn('0x70', Object(9), b'\x00\x00'),
			Insn('0x66', 2, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1548)), Insn('END')]), [
			Insn('0x16', Insn('3', b'\x05\x01\x00')),
		]),
		(Expr([Insn('FLAG', Flag(1537)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('0x23', 1), Insn('CONST', 10), Insn('NE'), Insn('END')]), [
					Insn('0x16', Insn('3', b'\x05\x01\x00')),
				]),
				(None, []),
			]),
		]),
		(None, [
			Insn('0x16', Insn('3', b'\x05\x01\x00')),
		]),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(812)), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
			Insn('0x11', b'\xcc\x8f\x85', 0, 230, 0),
		]),
		(Expr([Insn('FLAG', Flag(1547)), Insn('FLAG', Flag(1548)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
			Insn('0x11', b'\xcc\x8f\x85', 0, 230, 0),
		]),
		(None, []),
	]),
	Insn('0x1B', 0, Function((255, 255)), 255),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(812)), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 0, Function((0, 62)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1544)), Insn('FLAG', Flag(1546)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 0, Function((0, 62)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1546)), Insn('FLAG', Flag(1554)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 0, Function((0, 62)), 0),
		]),
		(None, []),
	]),
	Insn('SOUND_POSITION', 132, [
		-2440,
		6990,
		87910,
		10000,
		50000,
	], 100, 0),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('EVENT_BEGIN', 1),
	Insn('0x09', 134217728),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}有一个巴士车站。\n'
		'要乘坐巴士吗？{wait}'
	)),
	Insn('MENU', 0, -1, -1, 1, Text(
		'克洛斯贝尔北出口\n'
		'停靠站（人偶工房附近）\n'
		'放弃\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('CALL', Function((0, 6))),
			Insn('0x0A', 134217728),
			Insn('NEW_SCENE', 'r2000', b'\x00\x00\x00\x07'),
		]),
		(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
			Insn('CALL', Function((0, 6))),
			Insn('0x0A', 134217728),
			Insn('NEW_SCENE', 'r2030', b'\x00\x00\x00\x07'),
		]),
		(None, []),
	]),
	Insn('0x0A', 134217728),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (1060, -550, -2890), 0),
	Insn('CAM_ROTATE', 308, 30, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 18500, 0),
	Insn('0xE0', b'\x01'),
	Insn('CHAR_SET_POS', Char(0), (-4540, -2000, 27710), 180),
	Insn('CHAR_SET_POS', Char(1), (-5300, -2000, 27570), 180),
	Insn('CHAR_SET_POS', Char(2), (-6100, -2000, 27430), 180),
	Insn('CHAR_SET_POS', Char(3), (-6860, -2000, 27250), 180),
	Insn('CHAR_FLAG1_UNSET', Char(25), 128),
	Insn('OBJ_FLAG_UNSET', Object(10), 4),
	Insn('OBJ_FLAG_UNSET', Object(10), 2),
	Insn('0x78', b'\n', Char(25)),
	Insn('OBJ_SET_FRAME', Object(10), 'light', Insn('0', 1)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(25), (0, -2000, -8290), 0),
	Insn('0xD3', Char(25), 0, 0, 0, 0),
	Insn('OBJ_FLAG_SET', Object(10), 4096),
	Insn('0x74', Object(10), 7680),
	Insn('0x71', Object(10), b'y\x00', 180, 32),
	Insn('FORK', 25, 1, [
		Insn('0x95', Char(254), (450, -2000, 6620), 4000, 0),
	]),
	Insn('SOUND_PLAY', 466, 0, 0, 100),
	Insn('SOUND_PLAY', 467, 0, 0, 100),
	Insn('FORK_AWAIT', Char(25), 1),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-3860, -550, 26120), 0),
	Insn('CAM_ROTATE', 315, 30, 0, 0),
	Insn('0x6E', 640, 0),
	Insn('CAM_DISTANCE', 18500, 0),
	Insn('CHAR_SET_POS', Char(25), (-6320, -2000, 18640), 0),
	Insn('FORK', 25, 1, [
		Insn('0x95', Char(254), (-6320, -2000, 21130), 3000, 0),
	]),
	Insn('FORK_AWAIT', Char(25), 1),
	Insn('0x71', Object(10), b'[\x00', 120, 0),
	Insn('0x79', b'\n\x00'),
	Insn('SLEEP', 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FLAG_SET', Flag(1008)),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('EVENT_BEGIN', 1),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('CHAR_SET_POS', Char(0), (-4540, -2000, 27710), 180),
	Insn('CHAR_SET_POS', Char(1), (-4540, -2000, 27710), 180),
	Insn('CHAR_SET_POS', Char(2), (-4540, -2000, 27710), 180),
	Insn('CHAR_SET_POS', Char(3), (-4540, -2000, 27710), 180),
	Insn('CAM_OFFSET', (-4540, -550, 27710), 0),
	Insn('CAM_ROTATE', 315, 21, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 18500, 0),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('EVENT_BEGIN', 1),
	Insn('0x09', 134217728),
	Insn('SOUND_PLAY', 1499, 0, 255, 100),
	Insn('SLEEP', 500),
	Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('EQ'), Insn('END')], [
		Insn('MENU', 0, 32, 26, 1, Text(
			'使用警备队车辆进行移动\n'
			'在此处休息\n'
			'放弃\n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
				Insn('SOUND_PLAY', 1500, 0, 255, 100),
				Insn('MENU_CUSTOM', Insn('INIT', ResId(1))),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄中央广场'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 0)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄中央广场'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄东出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 1)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄东出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄西出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 2)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄西出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 4), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄南出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 3)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄南出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 5), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄北出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 4)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄北出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 6), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★唐古拉姆门'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 5)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000唐古拉姆门'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 7), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★贝尔加德门'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 6)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000贝尔加德门'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 8), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★乌尔斯拉医科大学'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 7)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000乌尔斯拉医科大学'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 9), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★阿尔摩利卡村'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 8)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000阿尔摩利卡村'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 10), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★玛因兹矿山镇'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 9)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000玛因兹矿山镇'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 11), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★玛因兹山道丄隧道内'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 10)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000玛因兹山道丄隧道内'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 12), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★星见之塔'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 11)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000星见之塔'))),
					]),
				]),
				Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000放弃'))),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
				Insn('MENU_CUSTOM', Insn('FINISH', ResId(1), 1048816, 1)),
				Insn('MENU_WAIT', 0),
				Insn('0x60', 1),
				Insn('TEXT_RESET', b'\x00'),
				Insn('0x5A'),
				Insn('IF', [
					(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('GE'), Insn('VAR', 0), Insn('CONST', 12), Insn('LT'), Insn('BOOL_AND'), Insn('END')]), [
						Insn('0x60', 0),
						Insn('SLEEP', 500),
						Insn('SOUND_PLAY', 1501, 0, 255, 100),
						Insn('0x74', Object(9), 7680),
						Insn('0x71', Object(9), b'\x01\x00', 30, 0),
						Insn('SOUND_PLAY', 464, 0, 0, 100),
						Insn('0x79', b'\t\x00'),
						Insn('SLEEP', 500),
						Insn('FADE_ON', 1000, Color(0x00000000), 255),
						Insn('SLEEP', 500),
						Insn('0x0D'),
						Insn('SOUND_PLAY', 488, 0, 0, 100),
						Insn('SLEEP', 2500),
						Insn('FLAG_SET', Flag(1009)),
						Insn('FLAG_SET', Flag(1022)),
						Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
							0: [
								Insn('NEW_SCENE', 'c0100', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							1: [
								Insn('NEW_SCENE', 'r0000', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							2: [
								Insn('NEW_SCENE', 'r1000', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							3: [
								Insn('NEW_SCENE', 'r1500', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							4: [
								Insn('NEW_SCENE', 'r2000', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							5: [
								Insn('NEW_SCENE', 't2500', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							6: [
								Insn('NEW_SCENE', 't2000', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							7: [
								Insn('NEW_SCENE', 't1500', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							8: [
								Insn('NEW_SCENE', 't0000', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							9: [
								Insn('NEW_SCENE', 't0500', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							10: [
								Insn('NEW_SCENE', 'r2050', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							11: [
								Insn('NEW_SCENE', 'm1000', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							None: [],
						}),
					]),
					(None, [
						Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
					]),
				]),
			]),
			(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
				Insn('0x60', 0),
				Insn('TEXT_RESET', b'\x00'),
				Insn('BGM_STOP', 3000),
				Insn('FADE_ON', 1000, Color(0x00000000), 255),
				Insn('0x0D'),
				Insn('0x5A'),
				Insn('SOUND_PLAY', 13, 0, 0, 100),
				Insn('0x32', Party(255), -2, 0),
				Insn('0x6A', b'\x00\x00\x00\x00\x00\x00'),
				Insn('SLEEP', 3500),
				Insn('0x1F'),
				Insn('FADE_OFF', 1000, Color(0x00000000)),
				Insn('TEXT_RESET', b'\x00'),
			]),
			(None, [
				Insn('0x60', 0),
				Insn('TEXT_RESET', b'\x00'),
				Insn('SLEEP', 500),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			]),
		]),
	]),
	Insn('0x0A', 134217728),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('EVENT_BEGIN', 1),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('CHAR_SET_POS', Char(0), (-11920, -2000, 26400), 45),
	Insn('CHAR_SET_POS', Char(1), (-11920, -2000, 26400), 45),
	Insn('CHAR_SET_POS', Char(2), (-11920, -2000, 26400), 45),
	Insn('CHAR_SET_POS', Char(3), (-11920, -2000, 26400), 45),
	Insn('CHAR_SET_POS', Char(4), (-11920, -2000, 26400), 45),
	Insn('CHAR_SET_POS', Char(5), (-11920, -2000, 26400), 45),
	Insn('SLEEP', 1),
	Insn('CAM_OFFSET', (-11920, -550, 26400), 0),
	Insn('CAM_ROTATE', 315, 21, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 18500, 0),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('SOUND_PLAY', 489, 0, 0, 100),
	Insn('SLEEP', 2000),
	Insn('IF', [
		(Expr([Insn('RAND'), Insn('CONST', 100), Insn('MOD'), Insn('CONST', 50), Insn('LT'), Insn('END')]), [
			Insn('SOUND_PLAY', 1502, 0, 255, 100),
		]),
		(None, [
			Insn('SOUND_PLAY', 1503, 0, 255, 100),
		]),
	]),
	Insn('SLEEP', 500),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x0A', 134217728),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('EXPR_VAR', 3, Expr([Insn('CONST', 10), Insn('SET'), Insn('END')])),
	Insn('CALL', Function((0, 8))),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'镇长和冈兹先生\n'
				'昨天都没回来呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯～到底出了什么事呢……？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'听说冈兹先生其实是在克洛斯贝尔市\n'
				'挥金如土，过着奢华的生活？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'真会给人添麻烦啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1547)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'因为冈兹先生行踪不明，\n'
				'卡洛斯先生好像\n'
				'一直很自责。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'但我觉得这根本就不是\n'
				'卡洛斯先生的责任呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'真是的，他就是一本正经过头了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1544)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啊，差不多该到日落的时候了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'罗基哥哥今天\n'
				'似乎工作得很认真，\n'
				'回来时应该会很累吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_WATCH', Char(254), Char(265), 0),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯……\n'
						'真是威风凛凛，\n'
						'又很帅气……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'可惜是个女人呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(265), Text(
						'#0505F哎？那个……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'啊，请不必介意。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'本以为好不容易来了个帅哥，\n'
						'结果竟然是女人吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哎，没办法。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'结果，在今年的纪念庆典\n'
				'也没有什么像样的邂逅吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不行，明年一定要……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……不过，去年好像也这么说过……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'唉……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'昨天，我们镇上\n'
						'来了个很帅的\n'
						'游客呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但他就在风景好的地方\n'
						'眺望了一下，\n'
						'然后就立刻返回克洛斯贝尔市了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……呜～好不甘心！\n'
						'感觉就像被耍了一样！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'观赏了风景之后，\n'
						'竟然马上就\n'
						'返回克洛斯贝尔市……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真应该把他拉去\n'
						'《红砖亭》喝点好酒，\n'
						'然后灌醉啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 12))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'来，来。\n'
						'这位小哥，不要客气。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我带你去\n'
						'风景优美的地方吧㈱{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'《彩虹剧团》的首日公演\n'
				'好像去了超多人呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'能够动员那么多人，\n'
				'不愧是大明星伊莉雅丄普拉提耶。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'前一阵子，我坐巴士\n'
						'去克洛斯贝尔市\n'
						'看帅哥。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'穿过隧道的时候，\n'
						'看到了一个像人偶一样\n'
						'可爱的女孩子。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'好像不是这附近的孩子……\n'
						'她在那种地方干什么呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我记得那附近好像\n'
						'有个叫什么贝尔克的\n'
						'工房……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那孩子\n'
						'在那种地方干什么呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'唉……我们镇上\n'
						'为什么没有好男人呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'当矿工的哥哥\n'
						'经常偷懒，又不好相处。\n'
						'其他的矿工也都很土气……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'卡洛斯先生还算及格，\n'
						'但是文弱过头了，\n'
						'不是我喜欢的类型呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'果然还是只能去克洛斯贝尔市\n'
						'狩猎……不，是找帅哥了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'要找好男人，\n'
						'果然还是只能\n'
						'去克洛斯贝尔市了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'稍后就坐巴士去看看吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(813)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(812)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……（发抖）。\n'
						'天气冷起来了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……哦，镇长叫我\n'
						'在天黑之前\n'
						'赶紧回家。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我可不想在夜路上\n'
						'被魔兽袭击啊。\n'
						'赶紧回家吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'山里的夜晚很冷呢～\n'
						'晚饭不然\n'
						'就做炖菜吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(816)), Insn('NOT'), Insn('END')]), [
					Insn('FLAG_SET', Flag(816)),
					Insn('0xD0', 2, Expr([Insn('0x23', 2), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
					Insn('CALL', Function((0, 28))),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(894)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'（哎呀……\n'
						'\u3000竟然有两个帅哥！）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(257), 0, 2000, (0, 1, 250, 2)),
					Insn('SOUND_PLAY', 29, 0, 0, 100),
					Insn('EMOTE', Char(260), 0, 2000, (0, 1, 250, 2)),
					Insn('SOUND_PLAY', 29, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F那个……？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，我什么都没说哦，小哥。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这里是矿山镇玛因兹。\n'
						'请慢慢逛吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(894)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'（这个穿夹克衫的小哥\n'
						'\u3000长得很可爱，\n'
						'\u3000那个高个子的大哥也很帅㈱）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F（从刚才起就一直这样，怎么回事……？）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0304F（嗯～被女孩子盯着看，\n'
						'\u3000感觉果然不坏啊。）{wait}'
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

data['code'][12] = [
	Insn('0x4B', Char(8), -1),
	Insn('0x4B', Char(16), -1),
	Insn('CHAR_WATCH', Char(8), Char(16), 0),
	Insn('CHAR_WATCH', Char(16), Char(8), 0),
	Insn('TEXT_TALK', Char(16), Text(
		'这里好像……\n'
		'不是阿尔摩利卡村啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'嗯～坐错\n'
		'巴士了吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'小哥，我们矿山镇玛因兹\n'
		'也是风景优美的好地方哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'不介意的话，\n'
		'我来给你带路吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'嗯，那个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(8), -1),
	Insn('0x4C', Char(16), -1),
	Insn('FLAG_SET', Flag(3)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 54, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 54, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 54, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 54, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((1, 13))),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'昨晚我本来\n'
						'打算开车去接\n'
						'镇长他们的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但是镇长说可能\n'
						'还要再待一阵子，就拒绝了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'在通讯的时候，\n'
						'镇长的声音听起来\n'
						'好像没什么精神……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'说是可能要在\n'
						'克洛斯贝尔市\n'
						'再待上一阵子……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'镇长的声音好像没什么精神，很令人担心呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'镇长去克洛斯贝尔市\n'
				'接冈兹先生了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'唉，总而言之，\n'
				'只要知道他在哪里\n'
				'也就暂时放心了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1547)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'其实，那天是我把冈兹先生\n'
						'送到克洛斯贝尔市的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'反正要搬运矿石，\n'
						'就顺便送他去了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……可是，过了\n'
						'约定的时间，\n'
						'冈兹先生也没有回来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'拜托了……\n'
						'请务必要找到冈兹先生。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'是我把冈兹先生送到\n'
						'克洛斯贝尔市的，\n'
						'所以我也有责任。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'拜托了……\n'
						'请务必要找到冈兹先生。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1544)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊……你们是\n'
						'接到镇长联系而来的\n'
						'特务支援课成员吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'谢谢你们过来。\n'
						'镇长正在等着呢，请去里面那座房子找他吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'镇长正在等着呢，请去里面那座房子找他吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'来我们镇子的隧道途中，\n'
				'不是有条分岔路吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'那条路的尽头有处遗迹，\n'
				'最近从那里有时会传来\n'
				'类似钟声一样的奇怪声音。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'那一带明明没有人迹的，\n'
				'真是诡异啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'好，今天晚上\n'
				'还得去接矿工们呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'冈兹先生今年\n'
				'能不能赚到钱呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……嗯，应该没戏吧。\n'
				'毕竟是冈兹先生……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'因为有机会去看纪念庆典，\n'
				'所以就稍微转了转……\n'
				'呀，今年也是人山人海呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'据说那也是《彩虹剧团》的\n'
				'新剧的影响……\n'
				'我觉得一点也没错呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天准备搬运矿石，\n'
				'顺便看看纪念庆典。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯～真期待啊。\n'
				'去『龙老饭店』\n'
				'吃顿饭似乎也不错。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'年轻的矿工们\n'
				'都出镇去看纪念庆典了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'平时工作都很辛苦，\n'
				'希望他们趁此机会释放一下压力呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我们矿山开采出的七耀石\n'
				'会用于多种领域。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'细小的碎片用作结晶回路的材料，\n'
				'大颗的结晶用来加工成宝石等等。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'一想到由我运送的\n'
				'七耀石能派上某些用场，\n'
				'就不由得感慨良多啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我负责用搬运车来运送\n'
				'开采出来的七耀石……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'但真担心以后有那么一天，\n'
				'再也没有七耀石可以开采了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'埋在矿山里的七耀石\n'
				'可不是无限的，\n'
				'连我也明白这一点。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(813)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(812)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(848)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'从山上看晚霞可真美啊。\n'
						'仿佛连心灵都被净化了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'说起来……就在前一阵子，\n'
						'我见到有个很大的东西\n'
						'飞过这片天空。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'要比这附近的\n'
						'鸟或魔兽大得太多了。\n'
						'那到底是什么呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F（嗯～这话令人有点在意……\n'
						'\u3000但应该和这次事件没什么关系吧。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(848)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'前一阵子，\n'
						'我见到有个很大的东西\n'
						'飞过这片天空。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'要比这附近的\n'
						'鸟或魔兽大得太多了。\n'
						'那到底是什么呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过，那时是晚上，而且又下着雨，\n'
						'说不定只是我看错了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(817)), Insn('NOT'), Insn('END')]), [
					Insn('FLAG_SET', Flag(817)),
					Insn('0xD0', 2, Expr([Insn('0x23', 2), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
					Insn('CALL', Function((0, 28))),
				]),
				(None, []),
			]),
			Insn('TEXT_TALK', Char(254), Text(
				'停在村子入口的搬运车好高级……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'刚才那些人竟然\n'
				'拥有那么高级的好车，\n'
				'到底是什么来头呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'矿工叔叔们\n'
						'似乎把冈兹叔叔的工作\n'
						'也平摊做好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'大家都毫无怨言，\n'
						'默默担起了工作。\n'
						'就连最怕麻烦的罗基叔叔也是……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……矿工叔叔们真会为同伴着想啊，\n'
						'矿工果然是个令人憧憬的职业呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'虽然妈妈说那是危险的工作，\n'
						'不让我去做……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但是我也想成为像叔叔们一样，\n'
						'会为同伴着想的出色矿工呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'冈兹叔叔似乎被找到了。\n'
						'太好了～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那个，冈兹叔叔还好吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1559)), Insn('END')]), [
							Insn('TEXT_TALK', Char(257), Text(
								'#0008F…………………………{wait}'
								'{page}'
								'（他可能服用了那种药物的事，\n'
								'\u3000实在说不出口啊……）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F嗯，你就放心吧。\n'
								'（虽然情况有点不对劲……）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'等冈兹叔叔回来以后，\n'
						'要让他再给我讲讲\n'
						'克洛斯贝尔市的事。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1547)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'冈兹叔叔，到底\n'
				'去哪里了呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'平时最久也是\n'
				'去三天就回来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1544)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'听玛尔罗叔叔说，\n'
				'冈兹叔叔好像\n'
				'失踪了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'到底出了什么事呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'说起来……\n'
				'最近好像都没看到冈兹叔叔啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'还想听他讲讲市里的事情呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'昨天我听罗基叔叔\n'
						'说工作没意思，\n'
						'让我深有感触。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'矿工叔叔们都是\n'
						'很不情愿地工作着吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但在收工之后的饮酒会时，\n'
						'还有谈起赌场的时候，\n'
						'他们看上去都那么开心……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'矿工叔叔们都是\n'
						'很不情愿地工作着吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'对于想当矿工的我来说，\n'
						'还真有点受打击。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我很憧憬矿工这个职业，\n'
				'所以向罗基叔叔询问\n'
				'这工作有什么优点……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'罗基叔叔……\n'
				'不喜欢这工作吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我爸爸\n'
				'是矿山长，\n'
				'非常有男子汉气概。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'所以我将来也要当矿工。\n'
				'嘿嘿，不错吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'昨天爸爸好像也去\n'
				'参加了宴会，真是少见。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'真羡慕啊……\n'
				'要是也能带我去\n'
				'就好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'昨天我在外边跑来跑去时，\n'
						'狠狠摔了一跤……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'身上擦伤了好多处，\n'
						'回家之后被妈妈大骂了一顿呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呜呜……\n'
						'以后可得小心脚下才行啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'昨天我被那边的梯子绊到，\n'
						'狠狠摔了一跤……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真够痛的。\n'
						'以后小心点吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'在山道的岔路深处\n'
						'有座奇怪的遗迹，你们见过吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'看到那种东西，我就觉得很兴奋呢。\n'
						'以后有机会的话，真想去探险啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'在山道的岔路深处\n'
						'有座奇怪的遗迹，你们见过吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'里面会是什么样子呢……\n'
						'以后有机会的话，真想去探险啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(813)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(812)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我爸爸是\n'
				'管理整个矿山的矿山长。\n'
				'很厉害吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'今天爸爸在矿山中的工作\n'
				'好像也结束了……\n'
				'要不要去接他呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(818)), Insn('NOT'), Insn('END')]), [
					Insn('FLAG_SET', Flag(818)),
					Insn('0xD0', 2, Expr([Insn('0x23', 2), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
					Insn('CALL', Function((0, 28))),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'镇子外面有个\n'
						'封闭的坑道入口吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'听说那里是以前的废坑，\n'
						'真想去探险呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过，要是靠近的话，\n'
						'会被镇长叔叔骂的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'总觉得那种废坑里\n'
						'好像沉眠着什么宝物呢，\n'
						'真想去探险啊。{wait}'
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

data['code'][15] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1547)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呜……\n'
				'总算干完活了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'好累，赶紧\n'
				'回家吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1544)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'矿山长的儿子\n'
				'今天也没什么精神啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'果然是我的错吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'唉，竟然对小孩子发牢骚，\n'
				'我可真是没用啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'矿山长的儿子\n'
				'向我询问矿工的事……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我一不经意就说出了\n'
				'『这工作又烦又累』\n'
				'这种直白露骨的话。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'打击到他了吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呼～好累……\n'
				'喝酒之后，就会完全没有干劲呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……哈，不过我平时也没什么干劲。\n'
				'不管怎么说，反正现在是纪念庆典，没关系吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'矿工的薪水\n'
						'可没有多少啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然在这个镇上生活还好，\n'
						'但要是去克洛斯贝尔市的欢乐街，\n'
						'一转眼就会花个精光。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真是的，太不平衡了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'虽然不停工作，\n'
						'但我的生活还是没见好转……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……不过，事实上我也经常偷懒啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'嗯……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……我在偷懒，不行吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'就一小会，\n'
						'别告诉其他矿工哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我有点累了，\n'
						'所以正在偷懒。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……不要告诉\n'
						'其他矿工哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(813)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(812)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1250)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 16))),
				]),
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'呼啊～啊……\n'
						'我还是早点回去吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'（因为适当偷了会懒，\n'
						'\u3000所以也没有那么累呢……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呼啊～啊……\n'
						'早点回去睡觉吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(819)), Insn('NOT'), Insn('END')]), [
					Insn('FLAG_SET', Flag(819)),
					Insn('0xD0', 2, Expr([Insn('0x23', 2), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
					Insn('CALL', Function((0, 28))),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'前一阵子，有魔兽\n'
						'袭击了住在这里的矿工。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然伤势并不是非常重，\n'
						'但为了保险起见，\n'
						'还是让他在家静养。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……唉，我也想休息啊～\n'
						'或者说想偷懒……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'受那点伤\n'
						'就可以休息，真羡慕啊。\n'
						'我也想偷懒啊……{wait}'
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
	Insn('TEXT_TALK', Char(254), Text(
		'（……其实我在矿山里\n'
		'\u3000偷懒看书呢。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'（在被矿山长发现之前，\n'
		'\u3000你们能不能收下这本书？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'收下了{item 712}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 712, 1),
	Insn('FLAG_SET', Flag(1250)),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1547)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'总算把今天的工作干完了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'冈兹那家伙不在，\n'
				'效率果然很低啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不管怎么说，那家伙\n'
				'很擅长活跃气氛呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1544)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(813)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(812)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 90, 0),
			Insn('TEXT_TALK', Char(254), Text(
				'你们去喝酒是可以，\n'
				'但是尽量早点回来啊！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'在马库斯那家伙回来之前，\n'
				'今后一个人\n'
				'也不许缺席啊！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1547)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1544)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 19))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呜……头还在痛。\n'
						'完全宿醉了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'啧，还真羡慕\n'
						'完全醉倒的罗基啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(813)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(812)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 19))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我们从早到晚都在\n'
						'阴暗的洞穴里干活。\n'
						'这点奖励是应得的嘛。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('0x4B', Char(13), -1),
	Insn('0x4B', Char(14), -1),
	Insn('CHAR_WATCH', Char(13), Char(14), 0),
	Insn('CHAR_WATCH', Char(14), Char(13), 0),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1547)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1544)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(13), Text(
				'呜……\n'
				'头还是疼得厉害呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'不管怎么想，都是喝多了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'……不过，镇长真是好人啊。\n'
				'因为是纪念庆典，就请\n'
				'所有矿工喝酒。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'拜其所赐，罗基那家伙\n'
				'直到现在还睡在\n'
				'红砖亭呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'……嗯，反正昨天挺开心的，\n'
				'就算了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(813)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(812)), Insn('END')]), [
			Insn('TEXT_TALK', Char(14), Text(
				'呼～今天的工作也终于结束了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'喂，等下去《红砖亭》\n'
				'喝酒吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'喂喂，镇长不是说了吗？\n'
				'要我们早点回家……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'别扫兴嘛。\n'
				'离深夜还早呢，\n'
				'有什么关系嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'……真没办法啊。\n'
				'我就陪你去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), []),
		(None, []),
	]),
	Insn('0x4C', Char(13), -1),
	Insn('0x4C', Char(14), -1),
	Insn('FLAG_SET', Flag(7)),
	Insn('FLAG_SET', Flag(8)),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'最近人手不足，\n'
						'我们开工都比平时早。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'指标可不等人啊。\n'
						'冈兹不在的时候，\n'
						'他的工作就要由大家来分担。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嘿嘿……等冈兹那家伙回来以后，\n'
						'可要让他好好报答我们才是。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(8)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'指标可不等人啊。\n'
						'冈兹不在的时候，\n'
						'他的工作就要由大家来分担。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'好啦……我差不多也\n'
						'必须要回去干活了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'听说你们昨天找到\n'
						'冈兹那家伙了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……那家伙从以前开始\n'
						'就一直嫌矿工的工作太累，\n'
						'经常发牢骚。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'为了发泄压力，\n'
						'才会染上玩牌的嗜好，\n'
						'但没想到竟然会失踪啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'给你们添麻烦了，真抱歉。\n'
						'我代替他\n'
						'向你们道歉。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(8)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'矿工这个工作是辛苦的体力活，\n'
						'薪水也没多少。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我想，心怀不满\n'
						'的人应该有不少吧，\n'
						'可大家都不会说出来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'冈兹这次的事情，\n'
						'我觉得也是因为\n'
						'累积的压力爆发了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1547)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'冈兹是我从小玩到大的伙伴，\n'
				'从以前开始就经常在一起。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'所以，没有他在的时候，\n'
				'就总觉得少了点什么似的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1544)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'…………………………\n'
				'那家伙，到底跑到哪里去了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……呼……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽说是纪念庆典，\n'
						'但对我们来说，\n'
						'日子还是一如往常……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(8)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'嗯……我可不是在偷懒哦。\n'
						'别把我跟罗基那家伙混为一谈。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我是得到了矿山长的许可，\n'
						'才过来休息一下的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 19))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'昨晚可真开心啊。\n'
						'镇长请我们所有矿工\n'
						'喝了酒呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'托他的福，这下可养足精神了。\n'
						'……好，去干活吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(813)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(812)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 19))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，这也是人际交往嘛。\n'
						'一点点的话也没关系吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'这两周都没开过宴会呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'因为有同伴失踪，\n'
		'开宴会太不妥当了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((0, 12))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'伤、伤脑筋啊……\n'
				'本来是打算去阿尔摩利卡村的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……但难得来了，还是观光一下吧。\n'
				'这里地势高，风景似乎不错……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(10)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我本来对矿山镇的情况\n'
				'不是很熟悉……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过这里风景挺不错，\n'
				'还能看到许多稀奇的东西……\n'
				'倒是来对了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(10)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'话说回来，这机械……\n'
				'到底是干什么用的呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'外行人真是搞不懂啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(11)), Insn('NOT'), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 0, 0),
			Insn('TEXT_TALK', Char(254), Text(
				'……呀……喝～！！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_SET_POS', 300, 30, -1, -1),
			Insn('TEXT_SET_NAME', Translate('回音')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}#2S（……呀……喝……）{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('0x5A'),
			Insn('TEXT_TALK', Char(254), Text(
				'哈哈，听见了，听见了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(11)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'身处群山之中时，\n'
				'果然还是要这样喊一次才行啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……虽然稍微有点难为情。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1546)), Insn('FLAG', Flag(1554)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}有一个巴士停靠站。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('IF', [
				(Expr([Insn('ATTR', 10), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F这次似乎\n'
						'没必要乘坐啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('ATTR', 10), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F这次似乎\n'
						'没必要乘坐呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('ATTR', 10), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F这次似乎\n'
						'没必要乘坐。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('ATTR', 10), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#0300F哈哈，这次似乎\n'
						'没必要乘坐啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(265), Text(
						'#0500F嗯……似乎\n'
						'没必要乘坐呢。\n'
						'反正有警备队的车。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('TEXT_END', Char(255)),
		]),
		(Expr([Insn('FLAG', Flag(1544)), Insn('FLAG', Flag(1546)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}有一个巴士停靠站。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_END', Char(255)),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CALL', Function((0, 5))),
		]),
		(None, [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}有一个巴士停靠站。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F今天还是不要坐巴士了吧。{wait}'
				'{page}'
				'为了进行调查，\n'
				'还是徒步走一走比较好。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_END', Char(255)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(810)), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((0, 35))),
		]),
		(None, [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}门后传来了谈话声。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_END', Char(255)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('TEXT_START', Char(255)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
			Insn('SOUND_PLAY', 810, 0, 0, 100),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F这里……\n'
				'似乎是玛因兹矿山的\n'
				'入口啊。{wait}'
				'{page}'
				'#0003F……上锁了。\n'
				'说不定是针对狼型魔兽事件\n'
				'而采取的警戒措施啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(9)),
		]),
		(None, [
			Insn('SOUND_PLAY', 810, 0, 0, 100),
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F……上锁了，\n'
				'还是以后再来这边吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][28] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('FLAG', Flag(810)), Insn('BOOL_AND'), Insn('FLAG', Flag(811)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('0x23', 2), Insn('CONST', 12), Insn('EQ'), Insn('END')]), [
					Insn('0xB5', b'\x01\x00\x80\x00'),
					Insn('0xB5', b'\x01\x01\x80\x00'),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][29] = [
	Insn('CHAR_FLAG1_UNSET', Char(19), 128),
	Insn('CHAR_FLAG2_UNSET', Char(19), 32768),
	Insn('OBJ_FLAG_UNSET', Object(8), 4),
	Insn('OBJ_FLAG_SET', Object(8), 2),
	Insn('OBJ_FLAG_SET', Object(8), 1024),
	Insn('CHAR_FLAG1_SET', Char(19), 32768),
	Insn('0x78', b'\x08', Char(19)),
	Insn('OBJ_FLAG_SET', Object(8), 4096),
	Insn('OBJ_SET_FRAME', Object(8), 'light', Insn('0', 1)),
	Insn('CHAR_SET_POS', Char(19), (-5500, -2000, 20700), 180),
	Insn('0xD3', Char(19), 0, 180000, 0, 0),
	Insn('0x74', Object(8), 7680),
	Insn('0x70', Object(8), b'\x00\x00'),
	Insn('RETURN'),
]

data['code'][30] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_SET_POS', Char(257), (1130, -2000, 15860), 0),
	Insn('CHAR_SET_POS', Char(258), (-160, -2000, 13680), 0),
	Insn('CHAR_SET_POS', Char(259), (940, -2000, 13950), 0),
	Insn('CHAR_SET_POS', Char(260), (-70, -2000, 15410), 0),
	Insn('CALL', Function((0, 29))),
	Insn('0x11', b'j\xa3\xcc', 0, 280, 0),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (34130, -500, 46430), 0),
	Insn('CAM_ROTATE', 306, 31, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 49940, 0),
	Insn('CAM_OFFSET', (1670, -500, 43690), 10000),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (1190, 5500, 41450), 0),
	Insn('CAM_ROTATE', 309, 15, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 45590, 0),
	Insn('CAM_OFFSET', (1190, -500, 41450), 10000),
	Insn('CAM_DISTANCE', 72340, 10000),
	Insn('SLEEP', 5000),
	Insn('0xCB', b'T\x01\xc8\x00', 'c_plac17', b'\x00\x00\x00'),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (1200, -2000, 20000), 2000, 0),
	]),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (-100, -2000, 18700), 2000, 0),
	]),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (1200, -2000, 18700), 2000, 0),
	]),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (-100, -2000, 20000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'\x11'),
	Insn('0x0D'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (440, 350, 19370), 0),
	Insn('CAM_ROTATE', 330, 15, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 18000, 0),
	Insn('0x11', b'j\xa3\xcc', 0, 230, 0),
	Insn('CAM_OFFSET', (440, -850, 19370), 3000),
	Insn('0x6F', b'y'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200470V#0000F#6P这里就是七耀石的产地……\n'
		'『矿山镇玛因兹』吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200471V#0205F#6P竟然建在地势这么\n'
		'险峻的地方呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200472V#0300F#6P怎么说呢……{wait}'
		'{page}'
		'#11200473V#0300F和阿尔摩利卡村一样，\n'
		'跟市里的反差可真大啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200474V#0103F#6P是呀……{wait}'
		'{page}'
		'#11200475V#0100F不过，为了开采矿石，\n'
		'导力倒是有一定程度的普及。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(258), 270, 500),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200476V#0105F#12P哎呀……？\n'
		'那边的黑色车辆是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 300),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('SLEEP', 300),
	Insn('CAM_OFFSET', (-3300, -800, 21380), 2500),
	Insn('CAM_ROTATE', 310, 19, 0, 2500),
	Insn('CAM_DISTANCE', 17800, 2500),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 32))),
	Insn('SLEEP', 100),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 34))),
	Insn('SLEEP', 80),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 31))),
	Insn('SLEEP', 120),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 33))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x6F', b'y'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200477V#0005F#12P这个……\n'
		'是运送矿石的搬运车吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200478V#0301F#2P嗯～以搬运车来说，\n'
		'造型莫名地粗犷呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200479V#0203F#12P看起来，好像是帝国莱恩福尔特公司\n'
		'制造的特殊搬运车呢。{wait}'
		'{page}'
		'#11200480V#0200F而且似乎是最新型。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200481V#0105F#6P如果是最新型的话……\n'
		'价格应该相当昂贵。{wait}'
		'{page}'
		'#11200482V#0100F会是镇长先生\n'
		'他们的车吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200483V#0003F#12P说不定吧。{wait}'
		'{page}'
		'#11200484V#0000F……不管怎么说，\n'
		'先去拜访镇长吧。{wait}'
		'{page}'
		'#11200485V关于魔兽事件的受灾情况，\n'
		'还要听听他怎么说才行啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(0), (-280, -2000, 19780), 0),
	Insn('CHAR_FLAG1_UNSET', Char(19), 32768),
	Insn('OBJ_FLAG_UNSET', Object(8), 4096),
	Insn('0x66', 1, 1),
	Insn('OBJ_FLAG_UNSET', Object(4), 16),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('FLAG_SET', Flag(809)),
	Insn('QUEST', 64, Insn('TASK_SET', 7)),
	Insn('0xD0', 2, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][31] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-1850, -2000, 22150), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 270, 500),
	Insn('RETURN'),
]

data['code'][32] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-3100, -2000, 20750), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 270, 500),
	Insn('RETURN'),
]

data['code'][33] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-1850, -2000, 20650), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 270, 500),
	Insn('RETURN'),
]

data['code'][34] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-3100, -2000, 22250), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 270, 500),
	Insn('RETURN'),
]

data['code'][35] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (12530, 1450, 68850), 0),
	Insn('CAM_ROTATE', 325, 20, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 18140, 0),
	Insn('CHAR_SET_POS', Char(257), (12000, 250, 69500), 0),
	Insn('CHAR_SET_POS', Char(258), (11700, 0, 67400), 0),
	Insn('CHAR_SET_POS', Char(259), (13480, 0, 66130), 0),
	Insn('CHAR_SET_POS', Char(260), (11700, 0, 66100), 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200486V#0005F#5P咦……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}门后传来了谈话声。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200487V#0105F#6P怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200488V#0003F#5P嗯……\n'
		'好像正忙着呢。{wait}'
		'{page}'
		'#11200489V#0000F是在接待客人吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_UNSET', Char(20), 128),
	Insn('CHAR_FLAG2_UNSET', Char(20), 32768),
	Insn('CHAR_SET_POS', Char(20), (22250, -1420, 63410), 270),
	Insn('TEXT_TALK2', Char(20), Translate('青年的声音'), Text(
		'#11200490V咦……\n'
		'你们找镇长有事？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (14640, 1650, 65760), 2000),
	Insn('CAM_ROTATE', 325, 14, 0, 2000),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 300),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 300),
	]),
	Insn('FORK', 20, 1, [
		Insn('0x95', Char(254), (17000, 0, 63700), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(20), 1),
	Insn('CHAR_WATCH', Char(20), Char(257), 500),
	Insn('0x6F', b'A'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200491V#0000F#5P啊……\n'
		'嗯，是的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200492V#0100F#5P请问，这里\n'
		'是镇长先生的家吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(20), Text(
		'#11200493V嗯，是的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(20), Text(
		'#11200494V不过现在最好还是别进去哦，\n'
		'因为他们好像在谈什么\n'
		'正事呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200495V#0005F#5P正事……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(20), Text(
		'#11200496V嗯，警备队不是在\n'
		'今天早上撤退了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(20), Text(
		'#11200497V魔兽都还没消灭，\n'
		'就在烦恼不知道该怎么办时，\n'
		'市里似乎就正好有人来帮忙了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200498V#0001F#5P难道是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200499V#0301F#5P游击士协会的家伙们吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(20), Text(
		'#11200500V那我就不知道了，\n'
		'反正好像是在谈魔兽方面的对策。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(20), Text(
		'#11200501V不知道你们找镇长有什么事，\n'
		'总之，还是待会再去拜访比较好吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(20), 225, 500),
	Insn('CAM_OFFSET', (13760, 1650, 65630), 3000),
	Insn('FORK', 20, 1, [
		Insn('0x95', Char(254), (8330, 0, 61360), 2500, 0),
	]),
	Insn('FORK_LOOP', 257, 1, [
		Insn('CHAR_WATCH', Char(257), Char(20), 500),
	]),
	Insn('FORK_LOOP', 258, 1, [
		Insn('CHAR_WATCH', Char(258), Char(20), 500),
	]),
	Insn('FORK_LOOP', 259, 1, [
		Insn('CHAR_WATCH', Char(259), Char(20), 500),
	]),
	Insn('FORK_LOOP', 260, 1, [
		Insn('CHAR_WATCH', Char(260), Char(20), 500),
	]),
	Insn('FORK_AWAIT', Char(20), 1),
	Insn('CHAR_FLAG1_SET', Char(20), 128),
	Insn('CHAR_FLAG2_SET', Char(20), 32768),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(259), 1),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('CHAR_WATCH', Char(259), Char(257), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200502V#0200F#6P……该怎么办呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200503V#0006F#11P嗯……\n'
		'既然有客人，那就没办法了。{wait}'
		'{page}'
		'#11200504V#0001F先在镇上四处探听一遍，\n'
		'再过来拜访吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200505V#0106F#6P呼……\n'
		'也只好这样了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200506V#0303F#6P哎呀呀……\n'
		'事情的发展好像有点古怪啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (12000, 0, 67500), 180),
	Insn('FLAG_SET', Flag(2)),
	Insn('FLAG_SET', Flag(810)),
	Insn('QUEST', 64, Insn('TASK_SET', 8)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][36] = [
	Insn('FLAG_SET', Flag(0)),
	Insn('CALL', Function((0, 38))),
	Insn('RETURN'),
]

data['code'][37] = [
	Insn('FLAG_SET', Flag(1)),
	Insn('CALL', Function((0, 38))),
	Insn('RETURN'),
]

data['code'][38] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0xFFFFFFFF), 0),
	Insn('FADE_ON', 500, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FADE_OFF', 0, Color(0xFFFFFFFF)),
	Insn('LOAD_CHCP', 'chr/ch31000', 30),
	Insn('LOAD_CHCP', 'chr/ch31100', 31),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
			Insn('CAM_OFFSET', (21240, 1450, 62400), 0),
			Insn('CAM_ROTATE', 315, 21, 0, 0),
			Insn('0x6E', 500, 0),
			Insn('CAM_DISTANCE', 18500, 0),
			Insn('0x90', Char(257), (21200, -600, 62700), b'\x0e\x01'),
			Insn('0x90', Char(258), (21200, -600, 63800), b'\x0e\x01'),
			Insn('0x90', Char(260), (22200, -1300, 63800), b'\x0e\x01'),
			Insn('0x90', Char(259), (22200, -1300, 62700), b'\x0e\x01'),
		]),
		(None, [
			Insn('CAM_OFFSET', (6800, 1450, 57800), 0),
			Insn('CAM_ROTATE', 315, 21, 0, 0),
			Insn('0x6E', 500, 0),
			Insn('CAM_DISTANCE', 18500, 0),
			Insn('CHAR_SET_POS', Char(257), (7200, 0, 58500), 0),
			Insn('CHAR_SET_POS', Char(258), (5800, 0, 58500), 0),
			Insn('CHAR_SET_POS', Char(259), (7200, 0, 57100), 0),
			Insn('CHAR_SET_POS', Char(260), (5800, 0, 57100), 0),
		]),
	]),
	Insn('CHAR_FLAG1_UNSET', Char(21), 128),
	Insn('CHAR_FLAG1_UNSET', Char(21), 4),
	Insn('CHAR_FLAG1_SET', Char(21), 32768),
	Insn('CHAR_SET_CHCP', Char(21), 30),
	Insn('CHAR_SET_FRAME', Char(21), 0),
	Insn('CHAR_SET_POS', Char(21), (12000, 380, 71000), 180),
	Insn('CHAR_SET_COLOR', Char(21), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(22), 128),
	Insn('CHAR_FLAG1_UNSET', Char(22), 4),
	Insn('CHAR_FLAG1_SET', Char(22), 32768),
	Insn('CHAR_SET_CHCP', Char(22), 31),
	Insn('CHAR_SET_FRAME', Char(22), 0),
	Insn('CHAR_SET_POS', Char(22), (12000, 380, 71000), 180),
	Insn('CHAR_SET_COLOR', Char(22), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(19), (-4000, -2000, 20700), 180),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x71', Object(4), b'\x00\x00', 5, 0),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('0x79', b'\x04\x00'),
	Insn('SLEEP', 300),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1200),
	Insn('CAM_OFFSET', (12000, 1450, 68500), 2300),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK2', Char(21), Translate('男性的声音'), Text(
		'#11200507V#2S#1P那么，镇长！\n'
		'就请你们好好商量一下吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(22), Translate('男性的声音'), Text(
		'#11200508V#2S#11P我们明天\n'
		'还会再来拜访的！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 4000),
	Insn('CAM_OFFSET', (11750, 1450, 66200), 4000),
	Insn('FORK', 21, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 21, 1, [
		Insn('0x95', Char(254), (12000, 0, 65000), 2000, 0),
	]),
	Insn('SLEEP', 1000),
	Insn('FORK', 22, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 22, 1, [
		Insn('0x95', Char(254), (12000, 0, 66800), 2000, 0),
	]),
	Insn('SLEEP', 1000),
	Insn('0x71', Object(4), b'\x05\x00', 0, 0),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('0x79', b'\x04\x00'),
	Insn('FORK_AWAIT', Char(21), 1),
	Insn('FORK_AWAIT', Char(21), 2),
	Insn('CHAR_ROTATE', Char(21), 0, 500),
	Insn('FORK_AWAIT', Char(22), 1),
	Insn('FORK_AWAIT', Char(22), 2),
	Insn('0x6F', b'\x01'),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'.\x01\x00'),
	Insn('0xB8', 121, 302),
	Insn('TEXT_TALK', Char(21), Text(
		'#11200509V#6P呵呵……\n'
		'就差最后一把劲了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#11200510V#11P嗯，看样子，这下总算\n'
		'能立下功劳，拿到奖赏了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_FUNC', Char(21), 3, Function((0, 39))),
	Insn('SLEEP', 300),
	Insn('FORK_FUNC', Char(22), 3, Function((0, 40))),
	Insn('SLEEP', 2000),
	Insn('CROSSFADE', 500),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
			Insn('CAM_OFFSET', (20240, 1450, 62400), 0),
			Insn('CAM_ROTATE', 315, 21, 0, 0),
			Insn('0x6E', 500, 0),
			Insn('CAM_DISTANCE', 18500, 0),
			Insn('CAM_OFFSET', (21240, 1450, 62400), 3000),
			Insn('0x90', Char(257), (21200, -600, 62700), b'\x0e\x01'),
			Insn('0x90', Char(258), (21200, -600, 63800), b'\x0e\x01'),
			Insn('0x90', Char(260), (22200, -1300, 63800), b'\x0e\x01'),
			Insn('0x90', Char(259), (22200, -1300, 62700), b'\x0e\x01'),
			Insn('0x6F', b'\x01'),
			Insn('SLEEP', 1500),
			Insn('CAM_OFFSET', (17240, 1450, 62400), 4000),
			Insn('FORK', 257, 1, [
				Insn('0x97', Char(254), (-5500, 0, 0), 2000, 0),
			]),
			Insn('SLEEP', 200),
			Insn('FORK', 258, 1, [
				Insn('0x97', Char(254), (-5500, 0, 0), 2000, 0),
			]),
			Insn('SLEEP', 250),
			Insn('FORK', 259, 1, [
				Insn('0x97', Char(254), (-5000, 0, 0), 2000, 0),
			]),
			Insn('SLEEP', 200),
			Insn('FORK', 260, 1, [
				Insn('0x97', Char(254), (-5000, 0, 0), 2000, 0),
			]),
			Insn('FORK_AWAIT', Char(257), 1),
			Insn('FORK', 257, 1, [
				Insn('CHAR_ROTATE', Char(254), 180, 300),
			]),
			Insn('FORK_AWAIT', Char(258), 1),
			Insn('FORK', 258, 1, [
				Insn('CHAR_ROTATE', Char(254), 180, 500),
			]),
			Insn('FORK_AWAIT', Char(259), 1),
			Insn('FORK', 259, 1, [
				Insn('CHAR_ROTATE', Char(254), 180, 500),
			]),
			Insn('FORK_AWAIT', Char(260), 1),
			Insn('FORK', 260, 1, [
				Insn('CHAR_ROTATE', Char(254), 180, 300),
			]),
			Insn('FORK_AWAIT', Char(257), 1),
			Insn('FORK_AWAIT', Char(258), 1),
			Insn('FORK_AWAIT', Char(259), 1),
			Insn('FORK_AWAIT', Char(260), 1),
			Insn('0x6F', b'\x01'),
		]),
		(None, [
			Insn('CAM_OFFSET', (6070, 1450, 54600), 0),
			Insn('CAM_ROTATE', 315, 21, 0, 0),
			Insn('0x6E', 500, 0),
			Insn('CAM_DISTANCE', 18500, 0),
			Insn('CHAR_SET_POS', Char(257), (-1800, 250, 53800), 90),
			Insn('CHAR_SET_POS', Char(258), (-3200, 250, 53800), 90),
			Insn('CHAR_SET_POS', Char(259), (-1800, 250, 54840), 90),
			Insn('CHAR_SET_POS', Char(260), (-3200, 250, 54840), 90),
			Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
			Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
			Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
			Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
			Insn('SLEEP', 7000),
			Insn('CAM_OFFSET', (2070, 1450, 54600), 3000),
			Insn('0x6F', b'\x01'),
			Insn('0x71', Object(0), b'\x00\x00', 5, 0),
			Insn('SOUND_PLAY', 105, 0, 0, 100),
			Insn('0x79', b'\x00\x00'),
			Insn('SLEEP', 1000),
			Insn('CAM_OFFSET', (3070, 1450, 53600), 4000),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 41))),
			Insn('SLEEP', 200),
			Insn('FORK_FUNC', Char(258), 3, Function((0, 41))),
			Insn('SLEEP', 100),
			Insn('FORK_FUNC', Char(259), 3, Function((0, 41))),
			Insn('SLEEP', 150),
			Insn('FORK_FUNC', Char(260), 3, Function((0, 41))),
			Insn('SLEEP', 3000),
			Insn('0x71', Object(0), b'\x05\x00', 0, 0),
			Insn('SOUND_PLAY', 106, 0, 0, 100),
			Insn('0x79', b'\x00\x00'),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(258), 3),
			Insn('FORK_AWAIT', Char(259), 3),
			Insn('FORK_AWAIT', Char(260), 3),
			Insn('0x6F', b'\x01'),
		]),
	]),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200511V#0001F#11P………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200512V#0101F#11P『鲁巴彻』的手下……\n'
		'竟然会出现在这种地方。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200513V#0301F#11P喂喂……\n'
		'那些家伙怎么会来这里啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200514V#0206F#11P看来是比游击士\n'
		'更加麻烦的对手呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200515V#0006F#11P嗯，是啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200516V#0005F#11P哎……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FORK_AWAIT', Char(21), 3),
	Insn('FORK_AWAIT', Char(22), 3),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-700, -550, 21400), 0),
	Insn('CAM_ROTATE', 315, 21, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 18500, 0),
	Insn('CHAR_SET_POS', Char(21), (-2100, -2000, 20200), 270),
	Insn('CHAR_SET_POS', Char(22), (-2100, -2000, 25200), 180),
	Insn('FORK', 22, 1, [
		Insn('0x97', Char(254), (0, 0, -5000), 2000, 0),
	]),
	Insn('0x71', Object(8), b'\x01\x00', 30, 0),
	Insn('SOUND_PLAY', 464, 0, 0, 100),
	Insn('0x79', b'\x08\x00'),
	Insn('SLEEP', 300),
	Insn('CHAR_FLAG1_SET', Char(21), 4),
	Insn('FORK', 21, 1, [
		Insn('0x95', Char(254), (-3100, -1400, 20200), 2000, 0),
	]),
	Insn('FORK', 21, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(21), 1),
	Insn('FORK_AWAIT', Char(21), 2),
	Insn('FORK_AWAIT', Char(22), 1),
	Insn('CHAR_ROTATE', Char(22), 270, 500),
	Insn('SLEEP', 300),
	Insn('CHAR_FLAG1_SET', Char(22), 4),
	Insn('FORK', 22, 1, [
		Insn('0x95', Char(254), (-3100, -1400, 20200), 2000, 0),
	]),
	Insn('FORK', 22, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(22), 1),
	Insn('FORK_AWAIT', Char(22), 2),
	Insn('0x0D'),
	Insn('0x71', Object(8), b'\x1f\x00', 60, 0),
	Insn('SOUND_PLAY', 463, 0, 0, 100),
	Insn('0x79', b'\x08\x00'),
	Insn('0x71', Object(8), b'<\x00', 90, 0),
	Insn('SOUND_PLAY', 465, 0, 0, 100),
	Insn('0x79', b'\x08\x00'),
	Insn('0x71', Object(8), b'y\x00', 180, 32),
	Insn('FORK', 19, 1, [
		Insn('0x98', Char(254), (0, 0, -10000), 5000, 0),
	]),
	Insn('FORK_AWAIT', Char(19), 1),
	Insn('CHAR_FLAG1_SET', Char(21), 128),
	Insn('CHAR_FLAG1_SET', Char(21), 4),
	Insn('CHAR_FLAG1_UNSET', Char(21), 32768),
	Insn('CHAR_FLAG1_SET', Char(22), 128),
	Insn('CHAR_FLAG1_SET', Char(22), 4),
	Insn('CHAR_FLAG1_UNSET', Char(22), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(19), 32768),
	Insn('OBJ_FLAG_UNSET', Object(8), 4096),
	Insn('OBJ_FLAG_SET', Object(8), 4),
	Insn('CHAR_FLAG1_SET', Char(19), 128),
	Insn('CHAR_FLAG2_SET', Char(19), 32768),
	Insn('CAM_OFFSET', (610, -550, 25820), 5000),
	Insn('CHAR_SET_POS', Char(257), (1070, 0, 37010), 180),
	Insn('CHAR_SET_POS', Char(258), (-310, 0, 37020), 180),
	Insn('CHAR_SET_POS', Char(259), (1050, 0, 38460), 180),
	Insn('CHAR_SET_POS', Char(260), (-300, 0, 38460), 180),
	Insn('FORK', 257, 1, [
		Insn('0x97', Char(254), (0, 0, -10000), 2000, 0),
	]),
	Insn('SLEEP', 200),
	Insn('FORK', 258, 1, [
		Insn('0x97', Char(254), (0, 0, -10000), 2000, 0),
	]),
	Insn('SLEEP', 250),
	Insn('FORK', 259, 1, [
		Insn('0x97', Char(254), (0, 0, -10000), 2000, 0),
	]),
	Insn('SLEEP', 200),
	Insn('FORK', 260, 1, [
		Insn('0x97', Char(254), (0, 0, -10000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200517V#0001F#11P那辆搬运车……\n'
		'原来是他们的啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200518V#0106F#5P难怪拥有帝国制造的\n'
		'最新型车辆……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200519V#0201F#11P可是……{wait}'
		'{page}'
		'#11200520V黑手党的人到矿山镇来，\n'
		'到底有什么事呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200521V#0306F#11P是啊……印象中，\n'
		'他们似乎不太到市外活动。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200522V#0003F#11P……总之，先听听\n'
		'镇长怎么说吧。{wait}'
		'{page}'
		'#11200523V#0001F说不定还能顺便了解到\n'
		'黑手党来此的目的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('CHAR_SET_POS', Char(0), (310, -2000, 26720), 180),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('0xD0', 2, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('0x65', 1, 1),
	Insn('OBJ_FLAG_SET', Object(4), 16),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('FLAG_SET', Flag(811)),
	Insn('QUEST', 64, Insn('TASK_SET', 9)),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][39] = [
	Insn('CHAR_ROTATE', Char(21), 225, 500),
	Insn('FORK', 21, 1, [
		Insn('0x95', Char(254), (7000, 0, 60000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(21), 1),
	Insn('FORK', 21, 1, [
		Insn('0x95', Char(254), (7000, 0, 40000), 3000, 0),
	]),
	Insn('FORK_AWAIT', Char(21), 1),
	Insn('RETURN'),
]

data['code'][40] = [
	Insn('CHAR_ROTATE', Char(22), 225, 500),
	Insn('FORK', 22, 1, [
		Insn('0x95', Char(254), (7000, 0, 61800), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(22), 1),
	Insn('FORK', 22, 1, [
		Insn('0x95', Char(254), (7000, 0, 41800), 3000, 0),
	]),
	Insn('FORK_AWAIT', Char(22), 1),
	Insn('RETURN'),
]

data['code'][41] = [
	Insn('FORK', 254, 1, [
		Insn('0x97', Char(254), (5500, 0, 0), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('CHAR_ROTATE', Char(254), 180, 300),
	Insn('RETURN'),
]

data['code'][42] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (12030, 1250, 67730), 0),
	Insn('CAM_ROTATE', 330, 18, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 14310, 0),
	Insn('CHAR_SET_POS', Char(257), (11820, 400, 71040), 270),
	Insn('CHAR_SET_POS', Char(258), (11820, 400, 71040), 270),
	Insn('CHAR_SET_POS', Char(259), (11820, 400, 71040), 270),
	Insn('CHAR_SET_POS', Char(260), (11820, 400, 71040), 270),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xcc\x8f\x85', 0, 230, 0),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x71', Object(4), b'\x00\x00', 5, 0),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('0x79', b'\x04\x00'),
	Insn('CAM_OFFSET', (12030, 1250, 65730), 4000),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 43))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 44))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 45))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 46))),
	Insn('SLEEP', 1000),
	Insn('0x71', Object(4), b'\x05\x00', 0, 0),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('0x79', b'\x04\x00'),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200590V#0101F#5P罗伊德，没问题吗？\n'
		'这样轻易许诺……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200591V#0306F#11P狼型魔兽似乎有两种，\n'
		'这点已经弄清了……{wait}'
		'{page}'
		'#11200592V#0301F就在今明两天，光凭我们几个，\n'
		'能消灭黑色的那种吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200593V#0004F#6P……不，\n'
		'我们不一定非要消灭它们。{wait}'
		'{page}'
		'#11200594V#0000F我们本来的任务，\n'
		'只是将警备队调查书上的\n'
		'那些不明了的部分查清吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200595V#0105F#5P这么一说的话……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200596V#0206F#11P好像在不知不觉间，就变成\n'
		'要对付魔兽本身了呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200597V#0003F#6P所以，我有个提议……{wait}'
		'{page}'
		'#11200598V#0000F正像那头白狼所说，\n'
		'如此一来，所有的线索都已经凑全了。{wait}'
		'{page}'
		'#11200599V要不要针对这次事件，\n'
		'开个会讨论一下？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200600V#0106F#5P是啊……\n'
		'或许有必要整理一下情报。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200601V#0300F#11P那么，都已经到傍晚了，\n'
		'要坐巴士回克洛斯贝尔市吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200602V#0004F#6P不……\n'
		'今天就住在这个镇上吧。{wait}'
		'{page}'
		'#11200603V#0000F在酒馆的客房里开会就可以了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200604V#0101F#5P这……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200605V#0205F#11P罗伊德前辈，莫非……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200606V#0302F#11P看样子，和旧市街那次一样，\n'
		'你已经察觉到了什么吧……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200607V#0004F#6P嗯，虽然目前还\n'
		'无法断言。{wait}'
		'{page}'
		'#11200608V#0000F可以的话，希望大家\n'
		'在开会时一起验证我的推理。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200609V#0100F#5P嗯……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200610V#0204F#11P……那么，我们赶快去\n'
		'旅店订个房间吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 15310, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('FLAG_SET', Flag(812)),
	Insn('QUEST', 64, Insn('TASK_SET', 10)),
	Insn('0x1B', 0, Function((0, 62)), 0),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 516), Insn('SET'), Insn('END')])),
	Insn('0xB8', 0, 0),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 't052b', b'\x00\x00\x00\x07'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][43] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (11920, 0, 68420), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (11990, 0, 64780), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 254, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('RETURN'),
]

data['code'][44] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (11920, 0, 68420), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (10890, 0, 65950), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][45] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (11920, 0, 68420), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (12960, 0, 65970), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][46] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (11920, 0, 68420), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (11900, 0, 66840), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][47] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch05700', 30),
	Insn('LOAD_CHCP', 'chr/ch00800', 31),
	Insn('LOAD_CHCP', 'chr/ch31000', 32),
	Insn('LOAD_CHCP', 'chr/ch31100', 33),
	Insn('LOAD_CHCP', 'apl/ch50157', 35),
	Insn('LOAD_CHCP', 'apl/ch50158', 37),
	Insn('CHAR_SET_POS', Char(257), (550, -2000, 18000), 0),
	Insn('CHAR_SET_POS', Char(258), (-350, -2000, 17300), 0),
	Insn('CHAR_SET_POS', Char(259), (1450, -2000, 16700), 0),
	Insn('CHAR_SET_POS', Char(260), (550, -2000, 16000), 0),
	Insn('CHAR_FLAG1_UNSET', Char(23), 128),
	Insn('CHAR_FLAG2_UNSET', Char(23), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(23), 4),
	Insn('CHAR_FLAG1_SET', Char(23), 32768),
	Insn('CHAR_SET_CHCP', Char(23), 30),
	Insn('CHAR_SET_FRAME', Char(23), 0),
	Insn('CHAR_FLAG1_UNSET', Char(24), 128),
	Insn('CHAR_FLAG2_UNSET', Char(24), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 4),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('CHAR_SET_CHCP', Char(24), 31),
	Insn('CHAR_SET_FRAME', Char(24), 0),
	Insn('CHAR_SET_POS', Char(23), (50, -2000, 20000), 180),
	Insn('CHAR_SET_POS', Char(24), (1160, -2000, 20000), 180),
	Insn('CHAR_FLAG1_UNSET', Char(21), 128),
	Insn('CHAR_FLAG2_UNSET', Char(21), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(21), 4),
	Insn('CHAR_FLAG1_SET', Char(21), 32768),
	Insn('CHAR_SET_CHCP', Char(21), 32),
	Insn('CHAR_SET_FRAME', Char(21), 0),
	Insn('CHAR_SET_POS', Char(21), (12000, 380, 71000), 180),
	Insn('CHAR_FLAG1_UNSET', Char(22), 128),
	Insn('CHAR_FLAG2_UNSET', Char(22), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(22), 4),
	Insn('CHAR_FLAG1_SET', Char(22), 32768),
	Insn('CHAR_SET_CHCP', Char(22), 33),
	Insn('CHAR_SET_FRAME', Char(22), 0),
	Insn('CHAR_SET_POS', Char(22), (12000, 380, 71000), 180),
	Insn('CHAR_FLAG1_UNSET', Char(26), 128),
	Insn('CHAR_FLAG2_UNSET', Char(26), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(26), 4),
	Insn('CHAR_FLAG1_SET', Char(26), 32768),
	Insn('CHAR_SET_CHCP', Char(26), 37),
	Insn('CHAR_SET_FRAME', Char(26), 0),
	Insn('CHAR_FLAG1_UNSET', Char(27), 128),
	Insn('CHAR_FLAG2_UNSET', Char(27), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(27), 4),
	Insn('CHAR_FLAG1_SET', Char(27), 32768),
	Insn('CHAR_SET_CHCP', Char(27), 37),
	Insn('CHAR_SET_FRAME', Char(27), 0),
	Insn('CHAR_FLAG1_UNSET', Char(28), 128),
	Insn('CHAR_FLAG2_UNSET', Char(28), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(28), 4),
	Insn('CHAR_FLAG1_SET', Char(28), 32768),
	Insn('CHAR_SET_CHCP', Char(28), 35),
	Insn('CHAR_SET_FRAME', Char(28), 0),
	Insn('CHAR_FLAG1_UNSET', Char(29), 128),
	Insn('CHAR_FLAG2_UNSET', Char(29), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(29), 4),
	Insn('CHAR_FLAG1_SET', Char(29), 32768),
	Insn('CHAR_SET_CHCP', Char(29), 35),
	Insn('CHAR_SET_FRAME', Char(29), 0),
	Insn('CHAR_SET_POS', Char(26), (-4940, -2000, 23820), 180),
	Insn('CHAR_SET_POS', Char(27), (-3780, -2000, 23800), 180),
	Insn('CHAR_SET_POS', Char(28), (-4940, -2000, 14000), 0),
	Insn('CHAR_SET_POS', Char(29), (-3780, -2000, 14000), 0),
	Insn('CHAR_SET_POS', Char(21), (-4940, -2000, 15300), 0),
	Insn('CHAR_SET_POS', Char(22), (-3780, -2000, 15300), 0),
	Insn('CHAR_FLAG1_UNSET', Char(19), 128),
	Insn('CHAR_FLAG2_UNSET', Char(19), 32768),
	Insn('OBJ_FLAG_UNSET', Object(9), 4),
	Insn('CHAR_FLAG1_SET', Char(19), 32768),
	Insn('0x78', b'\t', Char(19)),
	Insn('OBJ_FLAG_SET', Object(9), 4096),
	Insn('OBJ_SET_FRAME', Object(9), 'light', Insn('0', 1)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(19), (-7240, -2000, 22350), 180),
	Insn('0xD3', Char(19), 0, 0, 0, 0),
	Insn('0x74', Object(9), 7680),
	Insn('0x70', Object(9), b'\x00\x00'),
	Insn('0x71', Object(9), b'\x0e\x01', 270, 0),
	Insn('0x79', b'\t\x00'),
	Insn('0x7D', b'\xff\xff\xff\x00\x00\x00\x00\x00'),
	Insn('0x11', b'j\xa3\xcc', 0, 280, 0),
	Insn('SOUND_PLAY', 829, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('BGM_PLAY', b'~\x00\x00'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (6920, 2550, 28230), 0),
	Insn('CAM_ROTATE', 318, 16, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 36300, 0),
	Insn('CAM_OFFSET', (1420, 2550, 18280), 8000),
	Insn('FORK_FUNC', Char(21), 0, Function((0, 48))),
	Insn('FORK_FUNC', Char(22), 0, Function((0, 49))),
	Insn('FORK_FUNC', Char(28), 0, Function((0, 50))),
	Insn('FORK_FUNC', Char(29), 0, Function((0, 51))),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (510, -800, 18460), 0),
	Insn('CAM_ROTATE', 317, 21, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 17880, 0),
	Insn('0x11', b'j\xa3\xcc', 0, 230, 0),
	Insn('CHAR_FLAG1_SET', Char(26), 128),
	Insn('CHAR_FLAG2_SET', Char(26), 32768),
	Insn('CHAR_FLAG1_SET', Char(27), 128),
	Insn('CHAR_FLAG2_SET', Char(27), 32768),
	Insn('CHAR_FLAG1_SET', Char(28), 128),
	Insn('CHAR_FLAG2_SET', Char(28), 32768),
	Insn('CHAR_FLAG1_SET', Char(29), 128),
	Insn('CHAR_FLAG2_SET', Char(29), 32768),
	Insn('SLEEP', 500),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(24), Text(
		'#11200956V#0509F#11P──各位真的好厉害啊！{wait}'
		'{page}'
		'#11200957V#0502F没想到一下就看穿了事件的真相，\n'
		'还顺势将其解决了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11200958V#2004F#5P嗯……说实话，真是令人吃惊。{wait}'
		'{page}'
		'#11200959V#2001F不过，在事态扩大之前，\n'
		'还是应该先通知我们……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200960V#0006F#6P那个，对不起。{wait}'
		'{page}'
		'#11200961V#0008F……因为考虑到\n'
		'警备队的司令阁下\n'
		'有可能将情报泄露给黑手党……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11200962V#2006F#5P呼……\n'
		'被你这么一说，还真是难受呢。{wait}'
		'{page}'
		'#11200963V#2001F不过，要是那些白狼\n'
		'没来相救的话，你们要怎么办？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200964V#0011F#6P这个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200965V#0306F#6P老实说，那可就真是很危险了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11200966V#2001F#5P在这种时候，应该和赛尔盖商量，\n'
		'或者直接跟我说，\n'
		'类似的方法还有很多种吧。{wait}'
		'{page}'
		'#11200967V的确，从克洛斯贝尔的现状来看，\n'
		'还存在着各种复杂的难题……{wait}'
		'{page}'
		'#11200968V但即使如此，光凭自己\n'
		'就想解决所有事情的话，\n'
		'也只是狂妄自大而已。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200969V#0006F#6P……是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200970V#0106F#6P……我们无言以对。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11200971V#2004F#5P呵呵……算啦，\n'
		'责备就到此为止吧。{wait}'
		'{page}'
		'#11200972V#2002F你们能平安无事，真是太好了。{wait}'
		'{page}'
		'#11200973V还有，感谢各位\n'
		'代替我们解决了此事件。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200974V#0000F#6P副司令……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200975V#0309F#6P哈哈……\n'
		'您说得这么郑重，反倒叫人不好意思了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(24), Text(
		'#11200976V#0504F#11P呵呵……对了，副司令。{wait}'
		'{page}'
		'#11200977V#0500F救了罗伊德警官他们的\n'
		'那些白狼要怎么办呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11200978V#2003F#5P这个嘛……\n'
		'它们似乎完全被冤枉了。{wait}'
		'{page}'
		'#11200979V#2000F我想，可以先放着它们不管，静观其变……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200980V#0204F#6P……我觉得这样做应该没问题。{wait}'
		'{page}'
		'#11200981V#0202F它们看起来并不会愚蠢到\n'
		'去惹些没意义的麻烦……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11200982V#2002F#5P呵呵，似乎是呢。{wait}'
		'{page}'
		'#11200983V#2006F……不过，从这层意义上来说，\n'
		'愚蠢的反倒是人类呢。{wait}'
		'{page}'
		'#11200984V没想到，居然会为了进行军犬的实战测试，\n'
		'而在各地引起骚乱……{wait}'
		'{page}'
		'#11200985V#2001F虽说有后盾撑腰，\n'
		'但未免也太瞧不起我们了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200986V#0108F#6P……是呀。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200987V#0000F#6P可是，都引起\n'
		'这么大的骚动了……{wait}'
		'{page}'
		'#11200988V他们这次终究是\n'
		'没法再抵赖了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(23), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(24), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(23)),
	Insn('EMOTE_STOP', Char(24)),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200989V#0011F#6P哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200990V#0101F#6P他们果然……\n'
		'还是有可能被保释吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11200991V#2003F#5P……嗯，很可能。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(24), Text(
		'#11200992V#0506F#11P──我们以前\n'
		'也曾揭发过黑手党在国境附近的\n'
		'走私行为……{wait}'
		'{page}'
		'#11200993V但上层每次都会向我们施压，\n'
		'使他们得到保释。{wait}'
		'{page}'
		'#11200994V#0508F不仅如此，还随便找了个名目，\n'
		'将走私品原封不动地返还回去……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200995V#0007F#6P什么……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200996V#0206F#6P真是没有长进呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200997V#0301F#6P这么一说的话，贝尔加德门\n'
		'也发生过同样的事呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200998V#0108F#6P……………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11200999V#2003F#5P可是……\n'
		'我们也不能一味消沉下去啊。{wait}'
		'{page}'
		'#11201000V#2001F在这种状况下，如果大家都放弃的话，\n'
		'克洛斯贝尔也就真的没救了……{wait}'
		'{page}'
		'#11201001V抱着这样的想法，为了不让克洛斯贝尔彻底堕入黑暗而\n'
		'努力做着力所能及之事的人，应该也不在少数呢。{wait}'
		'{page}'
		'#11201002V#2000F就像你们一样。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#11201003V#0002F#6P啊……{wait}'
		'{page}'
		'#11201004V#0004F──是。\n'
		'我们正是以此为目标的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11201005V#2002F#5P呵呵……\n'
		'我今后也会期待你们支援课的\n'
		'活跃表现。{wait}'
		'{page}'
		'#11201006V#2004F──走吧，用我们的车\n'
		'送你们回克洛斯贝尔市。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(23), Char(24), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(23), Text(
		'#11201007V#2000F#5P诺艾儿，准备出发。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(24), Char(23), 500),
	Insn('SLEEP', 300),
	Insn('SOUND_PLAY', 1479, 0, 255, 100),
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_TALK', Char(24), Text(
		'#11201008V#0502F#2P是，长官！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('0xB8', 100, 0),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 110), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(23), 128),
	Insn('CHAR_FLAG2_SET', Char(23), 32768),
	Insn('CHAR_FLAG1_SET', Char(24), 128),
	Insn('CHAR_FLAG2_SET', Char(24), 32768),
	Insn('CHAR_FLAG1_SET', Char(21), 128),
	Insn('CHAR_FLAG2_SET', Char(21), 32768),
	Insn('CHAR_FLAG1_SET', Char(22), 128),
	Insn('CHAR_FLAG2_SET', Char(22), 32768),
	Insn('CHAR_FLAG1_SET', Char(26), 128),
	Insn('CHAR_FLAG2_SET', Char(26), 32768),
	Insn('CHAR_FLAG1_SET', Char(27), 128),
	Insn('CHAR_FLAG2_SET', Char(27), 32768),
	Insn('CHAR_FLAG1_SET', Char(28), 128),
	Insn('CHAR_FLAG2_SET', Char(28), 32768),
	Insn('CHAR_FLAG1_SET', Char(29), 128),
	Insn('CHAR_FLAG2_SET', Char(29), 32768),
	Insn('CHAR_FLAG1_SET', Char(19), 128),
	Insn('CHAR_FLAG2_SET', Char(19), 32768),
	Insn('0x49'),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0xD5', 33),
	Insn('0xD5', 35),
	Insn('0xD5', 37),
	Insn('FLAG_SET', Flag(740)),
	Insn('NEW_SCENE', 'c0100', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][48] = [
	Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xc2\x1a\x00\x00\xe8\x03\x00\x00\x00'),
	Insn('CHAR_ROTATE', Char(254), 270, 300),
	Insn('CHAR_FLAG1_SET', Char(254), 4),
	Insn('FORK', 254, 1, [
		Insn('0x97', Char(254), (-1500, 400, 0), 1000, 0),
	]),
	Insn('SLEEP', 650),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('RETURN'),
]

data['code'][49] = [
	Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xc2\x1a\x00\x00\xe8\x03\x00\x00\x00'),
	Insn('CHAR_ROTATE', Char(254), 270, 300),
	Insn('CHAR_FLAG1_SET', Char(254), 4),
	Insn('FORK', 254, 1, [
		Insn('0x97', Char(254), (-1160, 0, 0), 1000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x97', Char(254), (-1500, 400, 0), 1000, 0),
	]),
	Insn('SLEEP', 650),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('RETURN'),
]

data['code'][50] = [
	Insn('0x9B', b'\x00', Char(254), b'\x00\x00d\x19\x00\x00\xe8\x03\x00\x00\x00'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('RETURN'),
]

data['code'][51] = [
	Insn('0x9B', b'\x00', Char(254), b'\x00\x00d\x19\x00\x00\xe8\x03\x00\x00\x00'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('RETURN'),
]

data['code'][52] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (3840, 4950, 31680), 0),
	Insn('CAM_ROTATE', 329, 11, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 54120, 0),
	Insn('0x11', b'j\xa3\xcc', 0, 280, 0),
	Insn('CAM_OFFSET', (3840, -250, 31680), 8000),
	Insn('CHAR_SET_POS', Char(257), (-940, -2000, 21970), 270),
	Insn('CHAR_SET_POS', Char(258), (150, -2000, 22750), 270),
	Insn('CHAR_SET_POS', Char(259), (890, -2000, 21090), 270),
	Insn('CHAR_SET_POS', Char(260), (1790, -2000, 21770), 270),
	Insn('CHAR_SET_POS', Char(265), (-2690, -2000, 22000), 90),
	Insn('CHAR_FLAG1_UNSET', Char(4), 128),
	Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(265), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(19), 128),
	Insn('CHAR_FLAG2_UNSET', Char(19), 32768),
	Insn('OBJ_FLAG_UNSET', Object(9), 4),
	Insn('OBJ_FLAG_SET', Object(9), 2),
	Insn('OBJ_FLAG_SET', Object(9), 1024),
	Insn('CHAR_FLAG1_SET', Char(19), 32768),
	Insn('0x78', b'\t', Char(19)),
	Insn('OBJ_FLAG_SET', Object(9), 4096),
	Insn('OBJ_SET_FRAME', Object(9), 'light', Insn('0', 1)),
	Insn('CHAR_SET_POS', Char(19), (-1260, -2000, -800), 0),
	Insn('0xD3', Char(19), 0, 180000, 0, 0),
	Insn('0x74', Object(9), 7680),
	Insn('0x70', Object(9), b'\x00\x00'),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(265), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('FORK_FUNC', Char(30), 1, Function((0, 53))),
	Insn('0x9F', Insn('0', Char(19))),
	Insn('0x9F', Insn('1', (-1150, -2000, 6310))),
	Insn('0x9F', Insn('1', (-5650, -2000, 15640))),
	Insn('0x9F', Insn('1', (-5760, -2000, 21610))),
	Insn('0x9F', Insn('2', Char(19), 160, 100663311)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(265), Color(0xFFFFFFFF), 0),
	Insn('CHAR_ROTATE', Char(19), 180, 0),
	Insn('0xD3', Char(19), 0, 180000, 0, 0),
	Insn('0x65', 2, 1),
	Insn('CHAR_SET_POS', Char(19), (-14260, -2000, 24500), 0),
	Insn('0xD3', Char(19), 0, 145000, 0, 0),
	Insn('CAM_OFFSET', (-3410, -1050, 22410), 0),
	Insn('CAM_ROTATE', 309, 13, 0, 0),
	Insn('0x6E', 460, 0),
	Insn('CAM_DISTANCE', 19530, 0),
	Insn('0x11', b'j\xa3\xcc', 0, 230, 0),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (-1410, -1050, 22410), 3000),
	Insn('0x6F', b'y'),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(30), 1),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100508V#0502F#5P好，到了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100509V#0002F#12P哈哈，真是\n'
		'一眨眼就到了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(260), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100510V#0000F#5P快点去找镇长先生\n'
		'询问一下详情吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100511V#0304F#12P是啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(258), Char(257), 500),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100512V#0100F#11P我记得是直走到\n'
		'尽头的那间房子吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (0, -2000, 18000), 0),
	Insn('CHAR_FLAG1_SET', Char(4), 128),
	Insn('CHAR_FLAG2_SET', Char(4), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('FLAG_SET', Flag(1545)),
	Insn('QUEST', 74, Insn('TASK_SET', 1)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][53] = [
	Insn('SLEEP', 1000),
	Insn('SOUND_PLAY', 485, 0, 0, 90),
	Insn('RETURN'),
]

data['code'][54] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (10950, 850, 69530), 0),
	Insn('CAM_ROTATE', 330, 15, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 15780, 0),
	Insn('CHAR_SET_POS', Char(257), (11820, 400, 71040), 270),
	Insn('CHAR_SET_POS', Char(258), (11820, 400, 71040), 270),
	Insn('CHAR_SET_POS', Char(259), (11820, 400, 71040), 270),
	Insn('CHAR_SET_POS', Char(260), (11820, 400, 71040), 270),
	Insn('CHAR_SET_POS', Char(265), (11820, 400, 71040), 270),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(265), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(4), 128),
	Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
	Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xcc\x8f\x85', 0, 230, 0),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x71', Object(4), b'\x00\x00', 5, 0),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('0x79', b'\x04\x00'),
	Insn('CAM_OFFSET', (10950, 850, 67290), 4000),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 55))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 56))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 57))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 58))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(265), 3, Function((0, 59))),
	Insn('SLEEP', 1000),
	Insn('0x71', Object(4), b'\x05\x00', 0, 0),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('0x79', b'\x04\x00'),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('FORK_AWAIT', Char(265), 3),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100553V#0005F#11P都已经到傍晚了吗……{wait}'
		'{page}'
		'#14100554V#0000F差不多也该回\n'
		'克洛斯贝尔市了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100555V#0103F#11P是呀……\n'
		'最好在今天之内\n'
		'将情报探听完。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(258), Char(265), 500),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100556V#0100F#6P诺艾儿上士，能麻烦你再送我们一程吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(265), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(265), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(265), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100557V#0509F#11P嗯，小事一桩。{wait}'
		'{page}'
		'#14100558V#0502F那么，\n'
		'我们就回车子那边吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (13210, 0, 65069), 270),
	Insn('CHAR_FLAG1_SET', Char(4), 128),
	Insn('CHAR_FLAG2_SET', Char(4), 32768),
	Insn('0x66', 2, 1),
	Insn('FLAG_SET', Flag(1547)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][55] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (11920, 0, 68420), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (12200, 0, 64769), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('RETURN'),
]

data['code'][56] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (11920, 0, 68420), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (10890, 0, 65950), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][57] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (11920, 0, 68420), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (12960, 0, 65970), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][58] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (11920, 0, 68420), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (12550, 0, 67610), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][59] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (11920, 0, 68420), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (11220, 0, 67760), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][60] = [
	Insn('EVENT_BEGIN', 1),
	Insn('SOUND_PLAY', 1499, 0, 255, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}要乘坐警备队的车辆移动吗？{wait}'
	)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1545)), Insn('FLAG', Flag(1548)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('MENU', 0, -1, -1, 1, Text(
				'克洛斯贝尔市\n'
				'放弃\n'
			)),
			Insn('MENU_WAIT', 0),
			Insn('0x60', 0),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('CALL', Function((0, 61))),
					Insn('BGM_STOP', 2000),
					Insn('BGM_WAIT'),
					Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 102), Insn('SET'), Insn('END')])),
					Insn('FLAG_SET', Flag(736)),
					Insn('NEW_SCENE', 'r2030', b'\x00\x00\x00\x07'),
				]),
				(None, []),
			]),
		]),
		(None, [
			Insn('EXPR_VAR', 3, Expr([Insn('CONST', 10), Insn('SET'), Insn('END')])),
			Insn('CALL', Function((0, 8))),
		]),
	]),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][61] = [
	Insn('FADE_ON', 500, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 470, 0, 0, 70),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CAM_OFFSET', (-290, -2150, 10870), 0),
	Insn('CAM_ROTATE', 341, 17, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 20940, 0),
	Insn('CAM_OFFSET', (-290, 750, 10870), 4000),
	Insn('CHAR_FLAG1_UNSET', Char(19), 128),
	Insn('CHAR_FLAG2_UNSET', Char(19), 32768),
	Insn('OBJ_FLAG_UNSET', Object(9), 4),
	Insn('OBJ_FLAG_SET', Object(9), 2),
	Insn('OBJ_FLAG_SET', Object(9), 1024),
	Insn('CHAR_FLAG1_SET', Char(19), 32768),
	Insn('0x78', b'\t', Char(19)),
	Insn('OBJ_FLAG_SET', Object(9), 4096),
	Insn('OBJ_SET_FRAME', Object(9), 'light', Insn('0', 1)),
	Insn('CHAR_SET_POS', Char(19), (180, -2000, 16790), 180),
	Insn('0xD3', Char(19), 0, 180000, 0, 0),
	Insn('0x74', Object(9), 7680),
	Insn('0x70', Object(9), b'\x00\x00'),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(265), Color(0x00FFFFFF), 0),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('SOUND_PLAY', 486, 0, 0, 100),
	Insn('0x71', Object(9), b'y\x00', 180, 32),
	Insn('FORK', 19, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00 N\x00\x00p\x17\x00\x00\x00'),
	]),
	Insn('0x0D'),
	Insn('SLEEP', 2500),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(19), 1),
	Insn('0x6F', b'\x01'),
	Insn('RETURN'),
]

data['code'][62] = [
	Insn('EVENT_BEGIN', 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(812)), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0003F天都快黑了，\n'
				'还是不要去郊外了吧。{wait}'
				'{page}'
				'#0001F还得在酒馆\n'
				'对推理进行验证才行呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1544)), Insn('FLAG', Flag(1546)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这边是郊外方向啊。{wait}'
				'{page}'
				'#0003F回去之前，还是先听听\n'
				'镇长先生怎么说吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1546)), Insn('FLAG', Flag(1554)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这边是郊外方向啊。{wait}'
				'{page}'
				'#0004F机会难得，\n'
				'还是让诺艾儿上士送我们一程吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (650, -2000, -4920), 0),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]
