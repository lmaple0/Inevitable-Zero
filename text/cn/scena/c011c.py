# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'c011c',
	'name2': 'c011c',
	'location': 9,
	'bgm': 100,
	'flags': 8192,
	'includes': [
		None,
		None,
		None,
		None,
		None,
		None,
	],
	'name3': 'c011c',
	'labels': [],
	'chcp': [
		'chr/ch02500',
		'chr/ch02502',
		'chr/ch39200',
		'chr/ch02707',
		'apl/ch50092',
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
		None,
		None,
		None,
		None,
	],
	'npcs': [
		{
			'name': Translate('赛尔盖课长'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\x81\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('赛尔盖课长'),
			'pos': (64000, 200, 11399),
			'angle': 180,
			'_1': b'\xd5\x01\x00\x00\x01\x00\xff\xff',
			'function': Function((0, 5)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('赛特'),
			'pos': (123940, 0, 5840),
			'angle': 225,
			'_1': b'\x94\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 6)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('柯贝'),
			'pos': (123139, 0, 7639),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('比利'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('柯林'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('哈罗德'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('苏菲亚'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('艾丝蒂尔'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('约书亚'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('赛特'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('餐具'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xf6\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('餐具'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xf6\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('餐具'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xf6\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('餐具'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xf6\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('餐具'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xf6\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('餐具'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xf6\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('餐具'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xf6\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('餐具'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xf6\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('餐具'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xf6\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('餐具'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xf6\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('伊斯'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('金色蔷薇卡片'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('诺邦'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
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
			'pos': (7.0, 10.5, 0.0),
			'range': 25.0,
			'transform': [
				0.5,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.19999998807907104,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.19999998807907104,
				0.0,
				-3.5,
				-2.0999999046325684,
				-0.0,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 42)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (18240, 850, 7560),
			'range': 1000,
			'bubble_pos': (18240, 1850, 7560),
			'_1': b'|\x00\x00',
			'function': Function((0, 3)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (64000, 30, 9800),
			'range': 1500,
			'bubble_pos': (64000, 1500, 11400),
			'_1': b'~\x00\x00',
			'function': Function((0, 4)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-12920, 0, 7560),
			'range': 2000,
			'bubble_pos': (-12920, 0, 7560),
			'_1': b'|\x00\x00',
			'function': Function((0, 46)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (16960, 850, 10840),
			'range': 2000,
			'bubble_pos': (16960, 1300, 10840),
			'_1': b'|\x00\x00',
			'function': Function((0, 8)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (180910, 0, 62020),
			'range': 1500,
			'bubble_pos': (180910, 1500, 62020),
			'_1': b'|\x00\x00',
			'function': Function((0, 45)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (19980, 0, 63920),
			'range': 1500,
			'bubble_pos': (19980, 1500, 63920),
			'_1': b'|\x00\x00',
			'function': Function((0, 45)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (175940, 0, 63930),
			'range': 1500,
			'bubble_pos': (175940, 1500, 63930),
			'_1': b'|\x00\x00',
			'function': Function((0, 45)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-3150, 0, 122280),
			'range': 1200,
			'bubble_pos': (-3150, 1000, 122280),
			'_1': b'|\x00\x00',
			'function': Function((0, 56)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-2300, 0, 129960),
			'range': 1200,
			'bubble_pos': (-2300, 2000, 129960),
			'_1': b'|\x00\x00',
			'function': Function((0, 57)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (155150, 30, 129699),
			'range': 1200,
			'bubble_pos': (153340, 2029, 130490),
			'_1': b'|\x00\x00',
			'function': Function((0, 58)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (155120, 30, 123880),
			'range': 1200,
			'bubble_pos': (155120, 2029, 123880),
			'_1': b'|\x00\x00',
			'function': Function((0, 59)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (207280, 30, 128039),
			'range': 1200,
			'bubble_pos': (208840, 3000, 130410),
			'_1': b'|\x00\x00',
			'function': Function((0, 60)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (209020, 0, 126830),
			'range': 1200,
			'bubble_pos': (209210, 2000, 127040),
			'_1': b'|\x00\x00',
			'function': Function((0, 61)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (51920, 0, 130570),
			'range': 1200,
			'bubble_pos': (51920, 2500, 130570),
			'_1': b'|\x00\x00',
			'function': Function((0, 62)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (52900, 0, 124470),
			'range': 1200,
			'bubble_pos': (53700, 2000, 125270),
			'_1': b'|\x00\x00',
			'function': Function((0, 63)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (2750, 0, 125420),
			'range': 1200,
			'bubble_pos': (2750, 1500, 125420),
			'_1': b'|\x00\x00',
			'function': Function((0, 65)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (153580, 30, 127880),
			'range': 1200,
			'bubble_pos': (153370, 1530, 128389),
			'_1': b'|\x00\x00',
			'function': Function((0, 66)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (207040, 30, 128539),
			'range': 1200,
			'bubble_pos': (207640, 1500, 129090),
			'_1': b'|\x00\x00',
			'function': Function((0, 67)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (48000, 30, 127860),
			'range': 1200,
			'bubble_pos': (47560, 1500, 128630),
			'_1': b'|\x00\x00',
			'function': Function((0, 68)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\t\x00', Function((0, 1)), Function((0, 2))),
	'code': [None]*69,
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
		(Expr([Insn('ATTR', 0), Insn('CONST', 100), Insn('EQ'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('0x23', 7), Insn('CONST', 2), Insn('EQ'), Insn('0x23', 7), Insn('CONST', 7), Insn('EQ'), Insn('OR'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (-2190, 0, 68010), 90),
					Insn('CHAR_SET_POS', Char(1), (-2190, 0, 68010), 90),
					Insn('CHAR_SET_POS', Char(2), (-2190, 0, 68010), 90),
					Insn('CHAR_SET_POS', Char(3), (-2190, 0, 68010), 90),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-2190, 0, 68010), 90),
							Insn('CHAR_SET_POS', Char(5), (-2190, 0, 68010), 90),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-2190, 0, 68010), 90),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 108), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('0xD0', 7, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 110), Insn('EQ'), Insn('EXEC', Insn('PARTY_POSITION', Party(0))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(0))), Insn('CONST', 4), Insn('LT'), Insn('BOOL_AND'), Insn('FLAG', Flag(646)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 848, 0)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 47))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 110), Insn('EQ'), Insn('EXEC', Insn('PARTY_POSITION', Party(0))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(0))), Insn('CONST', 4), Insn('LT'), Insn('BOOL_AND'), Insn('FLAG', Flag(647)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 849, 0)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 48))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 118), Insn('EQ'), Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 4), Insn('LT'), Insn('BOOL_AND'), Insn('FLAG', Flag(648)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 850, 0)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 49))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 118), Insn('EQ'), Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 4), Insn('LT'), Insn('BOOL_AND'), Insn('FLAG', Flag(649)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 851, 0)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 50))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 120), Insn('EQ'), Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 4), Insn('LT'), Insn('BOOL_AND'), Insn('FLAG', Flag(650)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 852, 0)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 51))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 120), Insn('EQ'), Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 4), Insn('LT'), Insn('BOOL_AND'), Insn('FLAG', Flag(651)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 853, 0)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 52))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 112), Insn('EQ'), Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 4), Insn('LT'), Insn('BOOL_AND'), Insn('FLAG', Flag(652)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 854, 0)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 53))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 112), Insn('EQ'), Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 4), Insn('LT'), Insn('BOOL_AND'), Insn('FLAG', Flag(653)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 855, 0)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 54))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 64),
			Insn('CHAR_SET_POS', Char(19), (122440, 0, 7540), 45),
			Insn('CHAR_SET_CHCP', Char(19), 4),
			Insn('CHAR_SET_FRAME', Char(19), 0),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1286)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1362)), Insn('FLAG', Flag(1293)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('ATTR', 0), Insn('CONST', 100), Insn('EQ'), Insn('END')]), [
					Insn('0x09', 268435456),
					Insn('EVENT', Function((0, 39))),
				]),
				(Expr([Insn('ATTR', 0), Insn('CONST', 105), Insn('EQ'), Insn('END')]), [
					Insn('EVENT', Function((0, 40))),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('FLAG_SET', Flag(3)),
			Insn('EVENT', Function((0, 9))),
		]),
		(Expr([Insn('FLAG', Flag(737)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(737)),
			Insn('EVENT', Function((0, 11))),
		]),
		(Expr([Insn('FLAG', Flag(738)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(738)),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('0xDA', b'\x00')), Insn('CONST', 1), Insn('EQ'), Insn('EXEC', Insn('0xDA', b'\x00')), Insn('CONST', 255), Insn('EQ'), Insn('OR'), Insn('END')]), [
					Insn('EVENT', Function((0, 12))),
				]),
				(Expr([Insn('EXEC', Insn('0xDA', b'\x00')), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
					Insn('EVENT', Function((0, 13))),
				]),
				(Expr([Insn('EXEC', Insn('0xDA', b'\x00')), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
					Insn('EVENT', Function((0, 15))),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(739)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(739)),
			Insn('EVENT', Function((0, 18))),
		]),
		(Expr([Insn('FLAG', Flag(740)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(740)),
			Insn('EVENT', Function((0, 21))),
		]),
		(Expr([Insn('FLAG', Flag(741)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(741)),
			Insn('EVENT', Function((0, 24))),
		]),
		(Expr([Insn('FLAG', Flag(742)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(742)),
			Insn('EVENT', Function((0, 32))),
		]),
		(Expr([Insn('FLAG', Flag(743)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(743)),
			Insn('FLAG_SET', Flag(2)),
			Insn('EVENT', Function((0, 36))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('FLAG', Flag(2)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1072)), Insn('FLAG', Flag(1280)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('FLAG', Flag(1291)), Insn('FLAG', Flag(1292)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('EXPR_CHAR_ATTR', Char(10), 45, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(10), 46, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(10), 47, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('0x65', 0, 1),
	Insn('0x65', 1, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('0x66', 0, 1),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('0x66', 1, 1),
		]),
		(None, []),
	]),
	Insn('OBJ_SET_FRAME', Object(255), 'tanmatu2', Insn('0', 1)),
	Insn('OBJ_FLAG_SET', Object(10), 4),
	Insn('OBJ_FLAG_SET', Object(11), 4),
	Insn('OBJ_FLAG_SET', Object(12), 4),
	Insn('OBJ_FLAG_SET', Object(13), 4),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(646)), Insn('NOT'), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), '01', Insn('0', 1)),
			Insn('0x65', 7, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(647)), Insn('NOT'), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), '02', Insn('0', 1)),
			Insn('0x65', 8, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(648)), Insn('NOT'), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), '05', Insn('0', 1)),
			Insn('0x65', 9, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(649)), Insn('NOT'), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), '06', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), '06a', Insn('0', 1)),
			Insn('0x65', 10, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(650)), Insn('NOT'), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), '07', Insn('0', 1)),
			Insn('0x65', 11, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(651)), Insn('NOT'), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), '08', Insn('0', 1)),
			Insn('0x65', 12, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(652)), Insn('NOT'), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), '03', Insn('0', 1)),
			Insn('0x65', 13, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(653)), Insn('NOT'), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), '04', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), '04a', Insn('0', 1)),
			Insn('0x65', 14, 1),
		]),
		(None, []),
	]),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1280)), Insn('FLAG', Flag(1281)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 22, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x00\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1282)), Insn('FLAG', Flag(1283)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 27, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x00\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1292)), Insn('FLAG', Flag(1293)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 31, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x00\x80\x00'),
		]),
		(None, []),
	]),
	Insn('0x1B', 8, Function((255, 255)), 255),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1286)), Insn('FLAG', Flag(1292)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 8, Function((0, 44)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('OBJ_FLAG_SET', Object(7), 16),
			Insn('0x65', 4, 1),
		]),
		(None, [
			Insn('OBJ_FLAG_UNSET', Object(7), 16),
			Insn('0x66', 4, 1),
		]),
	]),
	Insn('OBJ_FLAG_UNSET', Object(8), 16),
	Insn('OBJ_FLAG_UNSET', Object(9), 16),
	Insn('0x66', 5, 1),
	Insn('0x66', 6, 1),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('TEXT_START', Char(255)),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}留言板上写有消息。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}『我去出席总部的会议。\n'
		'\u3000到时候就回来，你们先去工作吧。\n'
		'\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000赛尔盖』{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('CALL', Function((0, 5))),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('EXPR_CHAR_ATTR', Char(0), 5, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(9), 5, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('SET'), Insn('END')])),
	Insn('TEXT_START', Char(9)),
	Insn('CHAR_FLAG1_UNSET', Char(9), 16),
	Insn('CHAR_WATCH', Char(9), Char(0), 0),
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
	Insn('EXPR_CHAR_ATTR', Char(9), 4, Expr([Insn('CHAR_ATTR', Char(0), 5), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(0), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(9), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(9), 16),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'#1000F在纪念庆典期间，\n'
				'支援请求也会接连不断地\n'
				'发过来吧。{wait}'
				'{page}'
				'到最终日为止的四天内，\n'
				'就专心完成支援请求吧。{wait}'
				'{page}'
				'#1003F我大概也会时不时地\n'
				'去支援下总部那边……\n'
				'不过，你们不用管我，做好自己的工作就是。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F明白。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(0)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(9), Text(
				'#1000F在纪念庆典期间，\n'
				'支援请求也会接连不断地\n'
				'发过来吧。{wait}'
				'{page}'
				'你们不用管我，\n'
				'专心完成支援请求吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(9), 0),
	Insn('TEXT_END', Char(9)),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(10), Text(
		'#1200F…………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(11), Text(
				'喵～～呜……㈱{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F咦……？\n'
				'饵食都放在外面，\n'
				'没收进去吗。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(254), 0, 1700, (8, 9, 250, 2)),
			Insn('SOUND_PLAY', 27, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('FLAG_SET', Flag(1)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(11), Text(
				'喵～～呜……㈱{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('TEXT_START', Char(255)),
	Insn('0xE3', 10),
	Insn('FADE_ON', 300, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0xE3', 5),
	Insn('EXPR_VAR', 3, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('VAR', 3), Insn('CONST', 255), Insn('NE'), Insn('END')], [
		Insn('EXPR_VAR', 3, Expr([Insn('EXEC', Insn('0xE3', 0)), Insn('SET'), Insn('END')])),
		Insn('SWITCH', [Insn('VAR', 3), Insn('END')], {
			0: [
				Insn('IF', [
					(Expr([Insn('FLAG', Flag(1792)), Insn('FLAG', Flag(724)), Insn('BOOL_AND'), Insn('END')]), [
						Insn('QUEST_LIST', [
							52,
							49,
							50,
							43,
							51,
							46,
							40,
							41,
							47,
							-1,
						]),
					]),
					(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
						Insn('QUEST_LIST', [
							49,
							50,
							43,
							51,
							46,
							40,
							41,
							47,
							-1,
						]),
					]),
					(Expr([Insn('FLAG', Flag(1560)), Insn('END')]), [
						Insn('QUEST_LIST', [
							45,
							46,
							40,
							41,
							47,
							-1,
						]),
					]),
					(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
						Insn('QUEST_LIST', [
							40,
							41,
							47,
							-1,
						]),
					]),
					(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('QUEST_GET', 39, Insn('FLAG_GET', 32))), Insn('END')]), [
								Insn('QUEST_LIST', [
									40,
									41,
									42,
									47,
									54,
									57,
									-1,
								]),
							]),
							(None, [
								Insn('QUEST_LIST', [
									40,
									41,
									42,
									47,
									54,
									-1,
								]),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
						Insn('QUEST_LIST', [
							37,
							-1,
						]),
					]),
					(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
						Insn('QUEST_LIST', [
							34,
							35,
							24,
							26,
							28,
							30,
							33,
							55,
							-1,
						]),
					]),
					(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
						Insn('QUEST_LIST', [
							31,
							32,
							33,
							24,
							26,
							28,
							30,
							-1,
						]),
					]),
					(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
						Insn('QUEST_LIST', [
							27,
							28,
							29,
							30,
							24,
							26,
							-1,
						]),
					]),
					(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
						Insn('QUEST_LIST', [
							22,
							23,
							24,
							25,
							26,
							-1,
						]),
					]),
					(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
						Insn('QUEST_LIST', [
							17,
							18,
							19,
							20,
							14,
							16,
							56,
							58,
							-1,
						]),
					]),
					(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
						Insn('QUEST_LIST', [
							13,
							14,
							15,
							16,
							58,
							-1,
						]),
					]),
					(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
						Insn('QUEST_LIST', [
							9,
							10,
							11,
							5,
							6,
							7,
							-1,
						]),
					]),
					(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
						Insn('QUEST_LIST', [
							5,
							6,
							7,
							-1,
						]),
					]),
					(Expr([Insn('EXEC', Insn('QUEST_GET', 1, Insn('FLAG_GET', 32))), Insn('END')]), [
						Insn('QUEST_LIST', [
							1,
							53,
							2,
							3,
							-1,
						]),
					]),
					(None, [
						Insn('QUEST_LIST', [
							1,
							-1,
						]),
					]),
				]),
				Insn('BREAK'),
			],
			1: [
				Insn('0x09', 1073741824),
				Insn('0xE3', 7),
				Insn('SLEEP', 500),
				Insn('TEXT_SET_NAME', Translate('接待小姐芙兰')),
				Insn('IF', [
					(Expr([Insn('RAND'), Insn('CONST', 100), Insn('MOD'), Insn('CONST', 50), Insn('LT'), Insn('END')]), [
						Insn('SOUND_PLAY', 2062, 0, 255, 100),
						Insn('TEXT_MESSAGE', Char(255), Text(
							'您好，这里是克洛斯贝尔警察局～！{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(None, [
						Insn('SOUND_PLAY', 2061, 0, 255, 100),
						Insn('TEXT_MESSAGE', Char(255), Text(
							'各位，真是辛苦了～{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('EXEC', Insn('0xE3', 4)), Insn('END')]), [
						Insn('SOUND_PLAY', 2067, 0, 255, 100),
						Insn('TEXT_SET_NAME', Translate('接待小姐芙兰')),
						Insn('TEXT_MESSAGE', Char(255), Text(
							'那么，我将对各位的报告进行处理～{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_RESET', b'\x00'),
						Insn('EXPR_VAR', 6, Expr([Insn('ATTR', 47), Insn('SET'), Insn('END')])),
						Insn('0xE3', 12),
						Insn('IF', [
							(Expr([Insn('VAR', 6), Insn('ATTR', 47), Insn('NE'), Insn('END')]), [
								Insn('SWITCH', [Insn('ATTR', 47), Insn('END')], {
									14: [
										Insn('SOUND_PLAY', 2075, 0, 255, 100),
										Insn('TEXT_SET_NAME', Translate('接待小姐芙兰')),
										Insn('TEXT_MESSAGE', Char(255), Text(
											'级别１ｓｔ──\n'
											'罗伊德警官，实在太厉害了！{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('BREAK'),
									],
									13: [
										Insn('SOUND_PLAY', 2074, 0, 255, 100),
										Insn('TEXT_SET_NAME', Translate('接待小姐芙兰')),
										Insn('TEXT_MESSAGE', Char(255), Text(
											'级别２ｎｄ──\n'
											'罗伊德警官，好厉害呢！{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('BREAK'),
									],
									12: [
										Insn('SOUND_PLAY', 2073, 0, 255, 100),
										Insn('TEXT_SET_NAME', Translate('接待小姐芙兰')),
										Insn('TEXT_MESSAGE', Char(255), Text(
											'级别３ｒｄ──\n'
											'罗伊德警官，做得很好啊！{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('BREAK'),
									],
									None: [],
								}),
								Insn('SOUND_PLAY', 2076, 0, 255, 100),
								Insn('TEXT_SET_NAME', Translate('接待小姐芙兰')),
								Insn('TEXT_MESSAGE', Char(255), Text(
									'奖励物品\n'
									'也会马上给你们送去的～！{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('SOUND_PLAY', 2077, 0, 255, 100),
								Insn('TEXT_MESSAGE', Char(255), Text(
									'大家辛苦了～！\n'
									'以后也请随时来向我报告～{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('SOUND_PLAY', 2078, 0, 255, 100),
								Insn('TEXT_SET_NAME', Translate('接待小姐芙兰')),
								Insn('TEXT_MESSAGE', Char(255), Text(
									'报告就是以上这些吧～{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('SOUND_PLAY', 2079, 0, 255, 100),
								Insn('TEXT_MESSAGE', Char(255), Text(
									'那么，以后如果完成了新的委托，\n'
									'请再来向我报告吧～{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
						Insn('FLAG_SET', Flag(4)),
					]),
					(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
						Insn('SOUND_PLAY', 2063, 0, 255, 100),
						Insn('TEXT_SET_NAME', Translate('接待小姐芙兰')),
						Insn('TEXT_MESSAGE', Char(255), Text(
							'哎呀……\n'
							'刚才已经报告过了哦。{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('SOUND_PLAY', 2064, 0, 255, 100),
						Insn('TEXT_MESSAGE', Char(255), Text(
							'等完成了新的委托之后再来报告吧～{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(None, [
						Insn('SOUND_PLAY', 2065, 0, 255, 100),
						Insn('TEXT_SET_NAME', Translate('接待小姐芙兰')),
						Insn('TEXT_MESSAGE', Char(255), Text(
							'哎呀，好像并没有可以\n'
							'报告的委托哦～{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('SOUND_PLAY', 2066, 0, 255, 100),
						Insn('TEXT_MESSAGE', Char(255), Text(
							'请下次再来报告吧～{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
				]),
				Insn('TEXT_RESET', b'\x00'),
				Insn('0xE3', 8),
				Insn('0x0A', 1073741824),
				Insn('BREAK'),
			],
			None: [],
		}),
	]),
	Insn('0xE3', 6),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0xE3', 11),
	Insn('TEXT_END', Char(255)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 27, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 27, Insn('TASK_GET', 0))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 41))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('LOAD_CHCP', 'chr/ch00202', 32),
	Insn('LOAD_CHCP', 'chr/ch00302', 33),
	Insn('LOAD_CHCP', 'apl/ch50090', 34),
	Insn('LOAD_CHCP', 'apl/ch50092', 35),
	Insn('LOAD_CHCP', 'chr/ch02702', 36),
	Insn('CAM_OFFSET', (12600, 2350, 5600), 0),
	Insn('CAM_ROTATE', 40, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_SET_CHCP', Char(259), 32),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_SET_CHCP', Char(260), 33),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_POS', Char(257), (13900, 900, 6650), 270),
	Insn('CHAR_SET_POS', Char(258), (13900, 900, 4600), 270),
	Insn('CHAR_SET_POS', Char(259), (11300, 900, 6650), 90),
	Insn('CHAR_SET_POS', Char(260), (11300, 900, 4600), 90),
	Insn('CHAR_SET_CHCP', Char(18), 36),
	Insn('CHAR_SET_FRAME', Char(18), 0),
	Insn('CHAR_SET_POS', Char(18), (16000, 850, 6400), 180),
	Insn('CHAR_FLAG1_UNSET', Char(18), 128),
	Insn('CHAR_FLAG2_UNSET', Char(18), 32768),
	Insn('FORK_FUNC', Char(18), 0, Function((0, 10))),
	Insn('CHAR_SET_CHCP', Char(19), 35),
	Insn('CHAR_SET_FRAME', Char(19), 5),
	Insn('CHAR_FLAG1_SET', Char(19), 32768),
	Insn('CHAR_SET_POS', Char(19), (13000, 1400, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(19), 128),
	Insn('CHAR_FLAG2_UNSET', Char(19), 32768),
	Insn('CHAR_SET_CHCP', Char(20), 34),
	Insn('CHAR_SET_FRAME', Char(20), 12),
	Insn('CHAR_FLAG1_SET', Char(20), 32768),
	Insn('CHAR_SET_POS', Char(20), (13400, 1300, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(20), 128),
	Insn('CHAR_FLAG2_UNSET', Char(20), 32768),
	Insn('CHAR_SET_CHCP', Char(21), 35),
	Insn('CHAR_SET_FRAME', Char(21), 5),
	Insn('CHAR_FLAG1_SET', Char(21), 32768),
	Insn('CHAR_SET_POS', Char(21), (12400, 1400, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(21), 128),
	Insn('CHAR_FLAG2_UNSET', Char(21), 32768),
	Insn('CHAR_SET_CHCP', Char(22), 34),
	Insn('CHAR_SET_FRAME', Char(22), 12),
	Insn('CHAR_FLAG1_SET', Char(22), 32768),
	Insn('CHAR_SET_POS', Char(22), (12000, 1300, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(22), 128),
	Insn('CHAR_FLAG2_UNSET', Char(22), 32768),
	Insn('CHAR_SET_CHCP', Char(23), 35),
	Insn('CHAR_SET_FRAME', Char(23), 5),
	Insn('CHAR_FLAG1_SET', Char(23), 32768),
	Insn('CHAR_SET_POS', Char(23), (13000, 1400, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(23), 128),
	Insn('CHAR_FLAG2_UNSET', Char(23), 32768),
	Insn('CHAR_SET_CHCP', Char(24), 34),
	Insn('CHAR_SET_FRAME', Char(24), 12),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('CHAR_SET_POS', Char(24), (13400, 1300, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(24), 128),
	Insn('CHAR_FLAG2_UNSET', Char(24), 32768),
	Insn('CHAR_SET_CHCP', Char(25), 35),
	Insn('CHAR_SET_FRAME', Char(25), 5),
	Insn('CHAR_FLAG1_SET', Char(25), 32768),
	Insn('CHAR_SET_POS', Char(25), (12400, 1400, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(25), 128),
	Insn('CHAR_FLAG2_UNSET', Char(25), 32768),
	Insn('CHAR_SET_CHCP', Char(26), 34),
	Insn('CHAR_SET_FRAME', Char(26), 12),
	Insn('CHAR_FLAG1_SET', Char(26), 32768),
	Insn('CHAR_SET_POS', Char(26), (12000, 1300, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(26), 128),
	Insn('CHAR_FLAG2_UNSET', Char(26), 32768),
	Insn('CHAR_SET_CHCP', Char(27), 34),
	Insn('CHAR_SET_FRAME', Char(27), 7),
	Insn('CHAR_FLAG1_SET', Char(27), 32768),
	Insn('CHAR_SET_POS', Char(27), (12700, 1400, 5500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(27), 128),
	Insn('CHAR_FLAG2_UNSET', Char(27), 32768),
	Insn('CHAR_SET_CHCP', Char(28), 35),
	Insn('CHAR_SET_FRAME', Char(28), 0),
	Insn('CHAR_FLAG1_SET', Char(28), 32768),
	Insn('CHAR_SET_POS', Char(28), (16000, 750, 5500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(28), 128),
	Insn('CHAR_FLAG2_UNSET', Char(28), 32768),
	Insn('EXPR_CHAR_ATTR', Char(28), 45, Expr([Insn('CONST', 1100), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(28), 46, Expr([Insn('CONST', 1100), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(28), 47, Expr([Insn('CONST', 1100), Insn('SET'), Insn('END')])),
	Insn('SLEEP', 1000),
	Insn('0xC7', b'\x00\x00\x08\x00\x00'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{0x18}{color 0}#1K创立纪念庆典\u3000第三天{wait}'
	)),
	Insn('SLEEP', 2500),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0xC7', b'\x01\x00\x08\x00\x00'),
	Insn('BGM_PLAY', b'n\x00\x00'),
	Insn('CAM_OFFSET', (12600, 1850, 5600), 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13300001V#6P#0306F呼～哎呀呀，\n'
		'昨天可真是累死了。{wait}'
		'{page}'
		'#13300002V#0302F一想到这样的日子还要过三天，\n'
		'就不由得烦躁起来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(259), 2),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(259), Text(
		'#13300003V#5P#0200F昨天那件事只是自作自受吧……？{wait}'
		'{page}'
		'#13300004V#0204F提议展开那种追逐赛的人\n'
		'可是兰迪前辈你自己……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(260), Text(
		'#13300005V#6P#0301F事到如今，我已经后悔啦～{wait}'
		'{page}'
		'#13300006V#0306F我都一把年纪了，\n'
		'不该陪着年轻人胡闹的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13300007V#0102F才刚过二十岁的人，\n'
		'说什么呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13300008V#11P#0008F……………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#13300009V#0105F罗伊德？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13300010V#6P#0205F……怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13300011V#5P#0005F哦，嗯……{wait}'
		'{page}'
		'#13300012V#0012F我有点在意昨天\n'
		'艾丝蒂尔他们说的话。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13300013V#0101F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13300014V#6P#0301F是那个『黑之拍卖会#10RSchwarz Auction#』吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13300015V#6P#0200F可是，也很有可能\n'
		'只是传闻而已吧……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13300016V#5P#0003F嗯，话虽如此啦。{wait}'
		'{page}'
		'#13300017V#0001F考虑到克洛斯贝尔目前的形势，\n'
		'总感觉，并非只是\n'
		'单纯的传闻啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('TEXT_TALK', Char(260), Text(
		'#13300018V#6P#0306F的确，连黑手党\n'
		'都可以在这里横行霸道呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13300019V#6P#0203F不管发生什么事都不足为奇……\n'
		'或许的确如此。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13300020V#0108F……………………………………{wait}'
		'{page}'
		'#13300021V#0103F……其实，我以前也听过一个\n'
		'令人有点在意的传闻。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(259), 2),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13300022V#5P#0005F令人在意的传闻……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13300023V#3P#0205F具体来说是……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13300024V#0103F以前和大家说过，\n'
		'我曾经去各国留过学……{wait}'
		'{page}'
		'#13300025V就是当时从一位认识的\n'
		'贵族小姐那里听来的。{wait}'
		'{page}'
		'#13300026V#0101F据说，每年在克洛斯贝尔的\n'
		'某处都会召开一场秘密的社交宴会。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13300027V#5P#0011F秘密的社交宴会……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13300028V#6P#0302F我说，听上去就很可疑啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13300029V#0106F似乎是各国的贵族和企业家\n'
		'暗中齐聚一堂的宴会……{wait}'
		'{page}'
		'#13300030V#0108F当时我只觉得\n'
		'是单纯的传闻……{wait}'
		'{page}'
		'#13300031V#0101F不过，你们不觉得有些令人在意吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13300032V#5P#0003F的确……{wait}'
		'{page}'
		'#13300033V#0001F那很有可能就是\n'
		'『黑之拍卖会#10RSchwarz Auction#』吗……{wait}'
		'{page}'
		'#13300034V#0008F嗯～这样一来，课长\n'
		'很可能会知道些什么……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(259), Text(
		'#13300035V#6P#0200F不过，课长今天\n'
		'去了总部那边呢。{wait}'
		'{page}'
		'#13300036V说是有推不开的会议。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13300037V#5P#0006F是啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#13300038V#6P#0303F不过，就算是真的，\n'
		'我们也无能为力吧？{wait}'
		'{page}'
		'#13300039V#0301F再怎么想，议员们肯定也会下达指示，\n'
		'让警察局总部装聋作哑的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13300040V#5P#0008F……这倒也是啊。{wait}'
		'{page}'
		'#13300041V#0006F嗯～可是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13300042V#0103F……我明白你的心情。{wait}'
		'{page}'
		'#13300043V#0100F总之，在纪念庆典期间\n'
		'姑且留意一下吧。{wait}'
		'{page}'
		'#13300044V说不定能获得什么情报呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13300045V#5P#0003F──是啊。{wait}'
		'{page}'
		'#13300046V#0000F好，赶快把饭吃完，\n'
		'然后去解决今天的支援请求吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13300047V#6P#0202F…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 25500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 2000),
	Insn('BGM_WAIT'),
	Insn('CHAR_FLAG1_UNSET', Char(257), 4),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_FLAG1_UNSET', Char(258), 4),
	Insn('CHAR_SET_CHCP', Char(258), 255),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_FLAG1_UNSET', Char(259), 4),
	Insn('CHAR_SET_CHCP', Char(259), 255),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_FLAG1_UNSET', Char(260), 4),
	Insn('CHAR_SET_CHCP', Char(260), 255),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('CHAR_FLAG1_SET', Char(18), 128),
	Insn('CHAR_FLAG2_SET', Char(18), 32768),
	Insn('CHAR_FLAG1_SET', Char(19), 128),
	Insn('CHAR_FLAG2_SET', Char(19), 32768),
	Insn('CHAR_FLAG1_SET', Char(20), 128),
	Insn('CHAR_FLAG2_SET', Char(20), 32768),
	Insn('CHAR_FLAG1_SET', Char(21), 128),
	Insn('CHAR_FLAG2_SET', Char(21), 32768),
	Insn('CHAR_FLAG1_SET', Char(22), 128),
	Insn('CHAR_FLAG2_SET', Char(22), 32768),
	Insn('CHAR_FLAG1_SET', Char(23), 128),
	Insn('CHAR_FLAG2_SET', Char(23), 32768),
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
	Insn('0x49'),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0xD5', 33),
	Insn('0xD5', 34),
	Insn('0xD5', 35),
	Insn('0xD5', 36),
	Insn('CAM_OFFSET', (12000, 1850, 8700), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 340, 0),
	Insn('CAM_DISTANCE', 27500, 0),
	Insn('CHAR_SET_POS', Char(0), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(1), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(2), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(3), (12000, 850, 8700), 270),
	Insn('FLAG_SET', Flag(1282)),
	Insn('QUEST', 68, Insn('TASK_SET', 2)),
	Insn('QUEST', 68, Insn('TASK_SET', 3)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 23, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 23, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 23, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 25, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 25, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 25, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 25, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 25, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('0xB5', b'\x01\x00\x80\x00'),
	Insn('FLAG_UNSET', Flag(3)),
	Insn('BGM_PLAY', b'j\x00\x00'),
	Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 106), Insn('SET'), Insn('END')])),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_ANIMATION', Char(254), 1500, [
			0,
			1,
			2,
			1,
			0,
			3,
			4,
			3,
		]),
	]),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('LOAD_CHCP', 'chr/ch00202', 32),
	Insn('LOAD_CHCP', 'chr/ch00302', 33),
	Insn('LOAD_CHCP', 'apl/ch50090', 34),
	Insn('LOAD_CHCP', 'apl/ch50092', 35),
	Insn('LOAD_CHCP', 'chr/ch02702', 36),
	Insn('LOAD_CHCP', 'chr/ch23600', 37),
	Insn('CAM_OFFSET', (12600, 2350, 5600), 0),
	Insn('CAM_ROTATE', 40, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('CHAR_SET_CHCP', Char(259), 32),
	Insn('CHAR_SET_FRAME', Char(259), 2),
	Insn('CHAR_SET_CHCP', Char(260), 33),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_POS', Char(257), (13900, 900, 6650), 270),
	Insn('CHAR_SET_POS', Char(258), (13900, 900, 4600), 270),
	Insn('CHAR_SET_POS', Char(259), (11300, 900, 6650), 90),
	Insn('CHAR_SET_POS', Char(260), (11300, 900, 4600), 90),
	Insn('CHAR_SET_CHCP', Char(12), 37),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('CHAR_FLAG1_SET', Char(12), 32768),
	Insn('CHAR_SET_CHCP', Char(19), 35),
	Insn('CHAR_SET_FRAME', Char(19), 8),
	Insn('CHAR_FLAG1_SET', Char(19), 32768),
	Insn('CHAR_SET_POS', Char(19), (12700, 1400, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(19), 128),
	Insn('CHAR_FLAG2_UNSET', Char(19), 32768),
	Insn('CHAR_SET_CHCP', Char(20), 34),
	Insn('CHAR_SET_FRAME', Char(20), 24),
	Insn('CHAR_FLAG1_SET', Char(20), 32768),
	Insn('CHAR_SET_POS', Char(20), (13300, 1300, 6700), 0),
	Insn('CHAR_FLAG1_UNSET', Char(20), 128),
	Insn('CHAR_FLAG2_UNSET', Char(20), 32768),
	Insn('CHAR_SET_CHCP', Char(21), 34),
	Insn('CHAR_SET_FRAME', Char(21), 24),
	Insn('CHAR_FLAG1_SET', Char(21), 32768),
	Insn('CHAR_SET_POS', Char(21), (12100, 1300, 6700), 0),
	Insn('CHAR_FLAG1_UNSET', Char(21), 128),
	Insn('CHAR_FLAG2_UNSET', Char(21), 32768),
	Insn('CHAR_SET_CHCP', Char(22), 35),
	Insn('CHAR_SET_FRAME', Char(22), 8),
	Insn('CHAR_FLAG1_SET', Char(22), 32768),
	Insn('CHAR_SET_POS', Char(22), (12700, 1400, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(22), 128),
	Insn('CHAR_FLAG2_UNSET', Char(22), 32768),
	Insn('CHAR_SET_CHCP', Char(23), 34),
	Insn('CHAR_SET_FRAME', Char(23), 24),
	Insn('CHAR_FLAG1_SET', Char(23), 32768),
	Insn('CHAR_SET_POS', Char(23), (13300, 1300, 4700), 0),
	Insn('CHAR_FLAG1_UNSET', Char(23), 128),
	Insn('CHAR_FLAG2_UNSET', Char(23), 32768),
	Insn('CHAR_SET_CHCP', Char(24), 34),
	Insn('CHAR_SET_FRAME', Char(24), 24),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('CHAR_SET_POS', Char(24), (12100, 1300, 4700), 0),
	Insn('CHAR_FLAG1_UNSET', Char(24), 128),
	Insn('CHAR_FLAG2_UNSET', Char(24), 32768),
	Insn('CHAR_SET_CHCP', Char(25), 34),
	Insn('CHAR_SET_FRAME', Char(25), 7),
	Insn('CHAR_FLAG1_SET', Char(25), 32768),
	Insn('CHAR_SET_POS', Char(25), (12700, 1400, 5500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(25), 128),
	Insn('CHAR_FLAG2_UNSET', Char(25), 32768),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis062.itp'),
	Insn('SLEEP', 1000),
	Insn('0xC7', b'\x00\x00\x08\x00\x00'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{0x18}{color 0}#1K创立纪念庆典\u3000最终日{wait}'
	)),
	Insn('SLEEP', 2500),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0xC7', b'\x01\x00\x08\x00\x00'),
	Insn('BGM_PLAY', b'n\x00\x00'),
	Insn('CAM_OFFSET', (12600, 1850, 5600), 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500001V#6P#0309F哎呀～！\n'
		'话说，昨天听到的那些事情可真是不得了啊。{wait}'
		'{page}'
		'#13500002V#0300F那两个人，到底经历过\n'
		'何等惊人的试炼啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500003V#0103F关于利贝尔的异变，\n'
		'我虽然也听过不少传闻……{wait}'
		'{page}'
		'#13500004V#0100F不过，真相远比\n'
		'传闻更加惊人啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500005V#6P#0206F还有那个『结社』……{wait}'
		'{page}'
		'#13500006V#0201F凭借最尖端技术，实力甚至\n'
		'超越了爱普斯泰恩财团和ＺＣＦ，\n'
		'这些传闻倒是听说过一二……{wait}'
		'{page}'
		'#13500007V没想到它真的存在，\n'
		'而且还有那么大的规模……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500008V#5P#0006F嗯……\n'
		'老实说，真是很难想像呢。{wait}'
		'{page}'
		'#13500009V#0000F不过，据约书亚说，\n'
		'『结社』的势力基本还没有\n'
		'扩张到克洛斯贝尔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500010V#0108F说不定是因为在这里，帝国和共和国的\n'
		'监视比别处都森严吧。{wait}'
		'{page}'
		'#13500011V两国应该都派遣了\n'
		'很多谍报工作人员进来，\n'
		'所以结社不想被抓到尾巴……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500012V#5P#0006F……这真是\n'
		'完全不值得高兴的原因啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500013V#6P#0303F又是神秘结社，又是大国的谍报组织，\n'
		'再加上巨大的犯罪分子吗。{wait}'
		'{page}'
		'#13500014V#0301F唉，每一个都同样棘手啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500015V#6P#0206F……是啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 811, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(257), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(260), 2),
	Insn('CHAR_SET_POS', Char(12), (800, 0, -1500), 0),
	Insn('CHAR_SET_COLOR', Char(12), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG2_UNSET', Char(12), 32768),
	Insn('TEXT_TALK2', Char(12), Translate('声音'), Text(
		'#13500016V#5P各位好～！\n'
		'我是莱姆斯运送公司！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (800, 1000, 1500), 2000),
	Insn('0x6F', b'\x01'),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG2_UNSET', Char(12), 32768),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('FORK', 12, 1, [
		Insn('0x96', Char(254), (800, 0, 1500), 2000, 0),
	]),
	Insn('FORK', 12, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(12), 2),
	Insn('FORK_AWAIT', Char(12), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500017V#3P#0005F您是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500018V#0105F昨天那个运输公司的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (800, 1100, 5500), 0),
	Insn('CAM_ROTATE', 50, 23, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25500, 0),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_CHCP', Char(258), 255),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_SET_CHCP', Char(259), 255),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_SET_CHCP', Char(260), 255),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('CHAR_FLAG1_UNSET', Char(257), 4),
	Insn('CHAR_FLAG1_UNSET', Char(258), 4),
	Insn('CHAR_FLAG1_UNSET', Char(259), 4),
	Insn('CHAR_FLAG1_UNSET', Char(260), 4),
	Insn('0x90', Char(257), (300, 850, 7500), b'\xb4\x00'),
	Insn('0x90', Char(258), (1300, 850, 7500), b'\xb4\x00'),
	Insn('0x90', Char(259), (300, 850, 8700), b'\xb4\x00'),
	Insn('0x90', Char(260), (1300, 850, 8700), b'\xb4\x00'),
	Insn('CAM_OFFSET', (800, 1100, 2500), 2000),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (300, 0, 3500), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (1300, 0, 3500), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (300, 0, 4700), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (1300, 0, 4700), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13500019V#2P哎呀～昨天可真是辛苦各位了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13500020V#2P不过，真是太好了！\n'
		'总算是顺利找到了那个孩子！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13500021V#2P他的父母一定很担心吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500022V#5P#0012F哈哈，那自然。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500023V#5P#0300F你有没有\n'
		'被公司责骂啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13500024V#2P嗯，因为送货迟到了，\n'
		'还被警备队的人抱怨了一顿。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13500025V#2P不过老爸──呃，社长倒是\n'
		'没怎么责怪我呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13500026V#2P嗯，也就挨了一拳头，\n'
		'叫我以后好好检查车里。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500027V#5P#0102F呵呵……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500028V#5P#0204F嗯，这种程度就了事，\n'
		'应该算是幸运了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13500029V#2P哈哈，没错。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13500030V#2P──啊，我可不是来\n'
		'汇报昨天的事情啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13500031V#2P是给你们送货来的。{wait}'
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
	Insn('TEXT_TALK', Char(257), Text(
		'#13500032V#5P#0005F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500033V#5P#0105F从警察局总部发来的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13500034V#2P不，好像是一大早\n'
		'送来的一个快件……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13500035V#2P就是这个，请收下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 12, 1, [
		Insn('0x96', Char(254), (300, 0, 2500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(12), 1),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}收下了一个小包裹。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FORK', 12, 1, [
		Insn('0x96', Char(254), (800, 0, 1500), 1500, 0),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500036V#5P#0005F这是……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500037V#11P#0100F好像是个很小的东西……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_AWAIT', Char(12), 1),
	Insn('TEXT_TALK', Char(12), Text(
		'#13500038V#2P那么，货已经送到了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13500039V#2P还有其它的货要送，\n'
		'我这就告辞了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_ROTATE', Char(258), 180, 500),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500040V#5P#0300F哦，辛苦了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500041V#5P#0202F请多加小心，\n'
		'不要再让走失的孩子钻进车里了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#13500042V#2P哈哈，我会铭记在心的！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(12), 180, 500),
	Insn('FORK', 12, 1, [
		Insn('0x96', Char(254), (800, 0, -1500), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 12, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(12), 2),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('FORK_AWAIT', Char(12), 1),
	Insn('CAM_OFFSET', (800, 1100, 4100), 1500),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500043V#6P#0008F…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_WATCH', Char(258), Char(257), 500),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500044V#5P#0305F那么，究竟是谁送来的呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500045V#6P#0003F──这里写有寄件人姓名。{wait}'
		'{page}'
		'#13500046V#0000F好像是『小猫#4RKitty#』寄来的。{wait}'
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
		'#13500047V#0105F#11P哎……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500048V#0205F#5P是蕾恩寄来的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 25000, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 4000),
	Insn('CAM_OFFSET', (12600, 1850, 5600), 0),
	Insn('CAM_ROTATE', 40, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 24000, 0),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('CHAR_SET_CHCP', Char(259), 32),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_SET_CHCP', Char(260), 33),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_POS', Char(257), (13900, 900, 6650), 270),
	Insn('CHAR_SET_POS', Char(258), (13900, 900, 4600), 270),
	Insn('CHAR_SET_POS', Char(259), (11300, 900, 6650), 90),
	Insn('CHAR_SET_POS', Char(260), (11300, 900, 4600), 90),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(18), 128),
	Insn('CHAR_FLAG2_SET', Char(18), 32768),
	Insn('CHAR_FLAG1_SET', Char(19), 128),
	Insn('CHAR_FLAG2_SET', Char(19), 32768),
	Insn('CHAR_FLAG1_SET', Char(20), 128),
	Insn('CHAR_FLAG2_SET', Char(20), 32768),
	Insn('CHAR_FLAG1_SET', Char(21), 128),
	Insn('CHAR_FLAG2_SET', Char(21), 32768),
	Insn('CHAR_FLAG1_SET', Char(22), 128),
	Insn('CHAR_FLAG2_SET', Char(22), 32768),
	Insn('CHAR_FLAG1_SET', Char(23), 128),
	Insn('CHAR_FLAG2_SET', Char(23), 32768),
	Insn('CHAR_FLAG1_SET', Char(24), 128),
	Insn('CHAR_FLAG2_SET', Char(24), 32768),
	Insn('CHAR_FLAG1_SET', Char(25), 128),
	Insn('CHAR_FLAG2_SET', Char(25), 32768),
	Insn('CHAR_FLAG1_SET', Char(26), 128),
	Insn('CHAR_FLAG2_SET', Char(26), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(12), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(18), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(19), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(20), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(21), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(22), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(23), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(25), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(26), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('0x78', b'\x0c', Char(30)),
	Insn('OBJ_FLAG_UNSET', Object(12), 4),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(30), (12700, 1650, 6400), 0),
	Insn('0xD3', Char(30), 0, 0, 0, 0),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'o\x00\x00'),
	Insn('CAM_DISTANCE', 25000, 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}罗伊德打开小包裹，\n'
		'取出了里面的东西。{wait}'
		'{page}'
		'除了留言卡，\n'
		'还有一张漆黑的卡片。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SOUND_PLAY', 18, 0, 0, 100),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_POS', -1, 140, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13500049V『──作为昨天的谢礼，\n'
		'\u3000这张卡送给你们了。』{wait}'
		'{page}'
		'#13500050V『听说那里会展出很有趣的商品，\n'
		'\u3000所以我本打算过去看看。不过，\n'
		'\u3000就把机会让给大哥哥你们好了。』{wait}'
		'{page}'
		'#13500051V『呵呵，要有效利用哦。』{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'获得了{item 809}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 809, 1),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('EMOTE', Char(257), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500052V#11P#0013F『黑之拍卖会#10RSchwarz Auction#』的……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500053V#0105F那、那孩子怎么会有\n'
		'这种东西……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500054V#6P#0305F我记得，这是只发给各国ＶＩＰ的\n'
		'邀请卡吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500055V#6P#0206F而且……{wait}'
		'{page}'
		'#13500056V#0201F她怎么会知道\n'
		'我们对这件事\n'
		'有兴趣呢……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500057V#5P#0003F──关于那孩子的事，\n'
		'想太多似乎也无济于事。{wait}'
		'{page}'
		'#13500058V#0001F话说回来……\n'
		'你们觉得这张卡是真品吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500059V#0108F这个……{wait}'
		'{page}'
		'#13500060V#0101F从这种高档的制作工艺来看，\n'
		'我觉得是真品的可能性很高。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500061V#6P#0201F金色蔷薇的刻印……\n'
		'用的是真正的金箔呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500062V#6P#0301F今晚七时，于游憩区米修拉姆的\n'
		'哈尔特曼议长宅邸举行啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500063V#5P#0006F──那个，各位。{wait}'
		'{page}'
		'#13500064V#0008F虽然课长在不久前\n'
		'还那么郑重地叮嘱过我们……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500065V#0100F不用说了，罗伊德，我们都懂的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500066V#6P#0309F嗯，这就是所谓的，\n'
		'有便宜不占就是那个什么了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500067V#6P#0202F……幸好课长今天\n'
		'也去了总部。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500068V#5P#0001F大家……这样好吗？{wait}'
		'{page}'
		'#13500069V总是勉强大家\n'
		'迁就我的任性……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500070V#0104F呵呵，你可别误会哦。{wait}'
		'{page}'
		'#13500071V#0108F就某种意义上而言，\n'
		'我比你还对『黑之拍卖会#10RSchwarz Auction#』感兴趣……{wait}'
		'{page}'
		'#13500072V#0101F因为会参加这个宴会的，\n'
		'似乎都是与我所处的政界相近之人。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500073V#6P#0204F我则是纯粹\n'
		'对拍卖会感到好奇。{wait}'
		'{page}'
		'#13500074V蕾恩所说的\n'
		'『有趣的商品』\n'
		'也很令人在意。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500075V#6P#0309F哈，我是对豪华的\n'
		'上流社会晚宴本身很有兴趣呢。{wait}'
		'{page}'
		'#13500076V#0304F可以尽情享用美食美酒，\n'
		'而且还有机会接近上流社会那些\n'
		'高贵的大小姐们……{wait}'
		'{page}'
		'#13500077V#0302F怎么可能错过呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500078V#5P#0002F……各位……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500079V#5P#0003F──今天就是最终日了。{wait}'
		'{page}'
		'#13500080V#0001F中午之前，把其它工作都处理完，\n'
		'然后就去港湾区的水上巴士渡口吧。{wait}'
		'{page}'
		'#13500081V而是否真的要潜入拍卖会……\n'
		'等去了『米修拉姆』之后再考虑吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500082V#0100F嗯，明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500083V#6P#0300F那么，就赶快把\n'
		'剩下的工作解决掉吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500084V#6P#0204F还是先去终端\n'
		'确认一下有没有新委托吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 25500, 2000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_FLAG1_UNSET', Char(257), 4),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_FLAG1_UNSET', Char(258), 4),
	Insn('CHAR_SET_CHCP', Char(258), 255),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_FLAG1_UNSET', Char(259), 4),
	Insn('CHAR_SET_CHCP', Char(259), 255),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_FLAG1_UNSET', Char(260), 4),
	Insn('CHAR_SET_CHCP', Char(260), 255),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0xD5', 33),
	Insn('0xD5', 34),
	Insn('0xD5', 35),
	Insn('0xD5', 36),
	Insn('0xD5', 37),
	Insn('CAM_OFFSET', (12000, 1850, 8700), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 340, 0),
	Insn('CAM_DISTANCE', 27500, 0),
	Insn('CHAR_SET_POS', Char(0), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(1), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(2), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(3), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(30), (25600, 1650, 9500), 0),
	Insn('CHAR_FLAG1_SET', Char(30), 128),
	Insn('OBJ_FLAG_SET', Object(12), 4),
	Insn('FLAG_SET', Flag(1307)),
	Insn('0xC7', b'\x01\x00\x10\x00\x00'),
	Insn('QUEST', 68, Insn('TASK_SET', 8)),
	Insn('QUEST', 70, Insn('TASK_SET', 15)),
	Insn('QUEST', 70, Insn('FLAG_UNSET', 16)),
	Insn('BGM_STOP', 2000),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'g\x00\x00'),
	Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 103), Insn('SET'), Insn('END')])),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50332', 30),
	Insn('LOAD_CHCP', 'apl/ch50107', 31),
	Insn('CAM_OFFSET', (3000, 700, 126000), 0),
	Insn('CAM_ROTATE', 45, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 22500, 0),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(257), 32),
	Insn('CHAR_FLAG1_SET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 10),
	Insn('CHAR_SET_POS', Char(257), (2450, 300, 125550), 180),
	Insn('EXPR_CHAR_ATTR', Char(257), 36, Expr([Insn('CONST', 170), Insn('SET'), Insn('END')])),
	Insn('CHAR_SET_POS', Char(258), (1000, 30, 125300), 90),
	Insn('OBJ_SET_FRAME', Object(255), 'r_huton', Insn('0', 1)),
	Insn('OBJ_FLAG_UNSET', Object(13), 4),
	Insn('0x70', Object(13), b'\x05\x00'),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu00101.itp'),
	Insn('SOUND_PLAY', 910, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('？？？')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#13400001V#2S#60W……伊德……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#13400002V#2S#50W………罗伊德……真是的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#13400003V#5206F#40W嗯……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('SOUND_PLAY', 910, 0, 0, 100),
	Insn('TEXT_SET_NAME', Translate('？？？')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#13400004V……好啦，快起床。\n'
		'已经到开会时间了哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#13400005V#5205F#4S！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('BGM_PLAY', b'h\x00\x00'),
	Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 104), Insn('SET'), Insn('END')])),
	Insn('0xB8', 100, 104),
	Insn('0xB8', 101, 104),
	Insn('0x14', b'\x01\x00\x00\x00\xff\xff\xff\xbb\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
	Insn('CAM_DISTANCE', 23500, 1000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('SLEEP', 500),
	Insn('0x71', Object(13), b'\x05\x00', 20, 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('CHAR_SET_FRAME', Char(257), 11),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(257), 12),
	Insn('SLEEP', 300),
	Insn('SOUND_PLAY', 1128, 0, 255, 90),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (700, 30, 125300), 1500, 0),
	]),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400006V#6P#0105F#8A呀……{wait}'
	)),
	Insn('SLEEP', 1000),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('CHAR_SET_FRAME', Char(257), 13),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_FRAME', Char(257), 14),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_FRAME', Char(257), 13),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_FRAME', Char(257), 12),
	Insn('SLEEP', 300),
	Insn('0x6F', b'\x10'),
	Insn('0x15', b'\x00\x00\x00\x00'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400007V#11P#5205F啊……{wait}'
		'{page}'
		'#13400008V……早安，艾莉，\n'
		'你怎么在这里……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (1000, 30, 125300), 1000, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('SOUND_PLAY', 1187, 0, 255, 100),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 500),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'呵呵，早上好，罗伊德。{wait}'
	)),
	Insn('SLEEP', 1600),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'#13400009V因为你一直没起来，\n'
		'所以我来看看情况。{wait}'
		'{page}'
		'#13400010V看来，你一定是昨晚想得太多，\n'
		'所以睡不着吧？{wait}'
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
		'#13400011V#11P#5212F哈哈……都被你看穿了吗。{wait}'
		'{page}'
		'#13400012V#5200F艾莉你……好像没受什么影响啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400013V#6P#0104F如果遇到这种程度的事情就消沉，\n'
		'烦恼可就没完没了啦。{wait}'
		'{page}'
		'#13400014V#0108F而且……我可能\n'
		'早就隐约察觉到了。{wait}'
		'{page}'
		'#13400015V在克洛斯贝尔举办的\n'
		'所谓『秘密社交宴会』\n'
		'可能另有黑幕……{wait}'
		'{page}'
		'#13400016V#0106F但是，我之前或许只是在自欺欺人，\n'
		'装作没察觉的样子罢了。{wait}'
		'{page}'
		'#13400017V因为不想再经历会让自己沮丧\n'
		'或是悔恨的事。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400018V#11P#5201F艾莉……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400019V#6P#0102F所以现在，我决定坦然接受\n'
		'这种悔恨和沮丧。{wait}'
		'{page}'
		'#13400020V不是因为课长的话……\n'
		'而是因为我觉得这会成为我的动力。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400021V#11P#5204F是吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 13),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(257), 14),
	Insn('SLEEP', 300),
	Insn('EMOTE', Char(257), -500, 1500, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('CHAR_SET_FRAME', Char(257), 13),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(257), 12),
	Insn('SLEEP', 300),
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400022V#11P#5200F──好！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (2750, 700, 127100), 500),
	Insn('CAM_ROTATE', 45, 18, 0, 500),
	Insn('0x6E', 400, 500),
	Insn('CAM_DISTANCE', 23500, 500),
	Insn('CHAR_FLAG1_UNSET', Char(257), 4),
	Insn('CHAR_FLAG1_UNSET', Char(257), 32),
	Insn('CHAR_FLAG1_UNSET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 31),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('CHAR_SET_POS', Char(257), (1000, 30, 126400), 270),
	Insn('EXPR_CHAR_ATTR', Char(257), 36, Expr([Insn('CONST', 176), Insn('SET'), Insn('END')])),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('0x0D'),
	Insn('CHAR_ROTATE', Char(257), 180, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400023V#5204F#5P既然连艾莉都这么\n'
		'努力地调整心态了，\n'
		'我也不能再优柔寡断了。{wait}'
		'{page}'
		'#13400024V#5200F我这就去换衣服，\n'
		'你先在一楼等我吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400025V#12P#0102F嗯，好。{wait}'
		'{page}'
		'#13400026V#0109F早餐也准备好了，\n'
		'边吃边开会吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400027V#5202F#5P嗯，谢了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(258), 180, 500),
	Insn('CAM_OFFSET', (2000, 700, 124000), 2000),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (0, 0, 120500), 2000, 1),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (0, 0, 119000), 2000, 0),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 300),
	]),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(258), 2),
	Insn('0x6F', b'\x01'),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (1000, 1000, 126400), 0),
	Insn('CAM_ROTATE', 45, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 22500, 0),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400028V#5202F#5P（艾莉……和之前谈心时比起来，\n'
		'\u3000似乎已经没有那么多迷惘了。）{wait}'
		'{page}'
		'#13400029V#5204F（嗯，我也不能输给她呢。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (1390, 1000, 128419), 1500),
	Insn('CHAR_ROTATE', Char(257), 355, 400),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400030V#2P#5200F纪念庆典也到了第四天……{wait}'
		'{page}'
		'#13400031V看来今天也会很忙呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 23000, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('OBJ_SET_FRAME', Object(255), 'r_huton', Insn('1', 1)),
	Insn('OBJ_FLAG_SET', Object(13), 4),
	Insn('CALL', Function((0, 17))),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50332', 30),
	Insn('LOAD_CHCP', 'apl/ch50107', 31),
	Insn('LOAD_CHCP', 'chr/ch00250', 32),
	Insn('CAM_OFFSET', (3000, 700, 126000), 0),
	Insn('CAM_ROTATE', 45, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 22500, 0),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(257), 32),
	Insn('CHAR_FLAG1_SET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 10),
	Insn('CHAR_SET_POS', Char(257), (2450, 300, 125550), 180),
	Insn('EXPR_CHAR_ATTR', Char(257), 36, Expr([Insn('CONST', 170), Insn('SET'), Insn('END')])),
	Insn('CHAR_SET_POS', Char(259), (1000, 30, 125300), 90),
	Insn('CHAR_SET_CHCP', Char(259), 32),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('OBJ_SET_FRAME', Object(255), 'r_huton', Insn('0', 1)),
	Insn('OBJ_FLAG_UNSET', Object(13), 4),
	Insn('0x70', Object(13), b'\x05\x00'),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu00200.itp'),
	Insn('SOUND_PLAY', 910, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('？？？')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#13400032V#2S#60W…………………（摇摇）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#13400033V#5206F#40W……嗯…………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('SOUND_PLAY', 910, 0, 0, 100),
	Insn('TEXT_SET_NAME', Translate('？？？')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#13400034V#2S#40W…………………………………\n'
		'（摇摇，摇摇，摇摇）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#13400035V#5208F#30W（……怎么了……地震？）{wait}'
		'{page}'
		'#13400036V（可是，地震的话……\n'
		'\u3000好像不会这么舒服……）{wait}'
		'{page}'
		'#13400037V#5203F（不行了……还是很困……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_NAME', Translate('？？？')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#13400038V#2S#40W…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 1219, 0, 255, 90),
	Insn('SLEEP', 1200),
	Insn('TEXT_SET_NAME', Translate('？？？')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#13400039V#2S……输出功率最低，极小档。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_NAME', Translate('？？？')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#13400040V#2S冻结程序开启───发动。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('SLEEP', 150),
	Insn('SOUND_PLAY', 1221, 0, 255, 100),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 184, 0, 0, 90),
	Insn('SLEEP', 700),
	Insn('SOUND_PLAY', 371, 0, 0, 90),
	Insn('SLEEP', 300),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#13400041V#5211F#4S好冷！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('BGM_PLAY', b'h\x00\x00'),
	Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 104), Insn('SET'), Insn('END')])),
	Insn('0xB8', 100, 104),
	Insn('0xB8', 101, 104),
	Insn('0x14', b'\x01\x00\x00\x00\xff\xff\xff\xbb\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
	Insn('CAM_DISTANCE', 23500, 1000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('SLEEP', 500),
	Insn('0x71', Object(13), b'\x05\x00', 20, 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('CHAR_SET_FRAME', Char(257), 11),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(257), 12),
	Insn('SLEEP', 300),
	Insn('CHAR_SET_FRAME', Char(257), 13),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_FRAME', Char(257), 14),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_FRAME', Char(257), 13),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_FRAME', Char(257), 12),
	Insn('SLEEP', 300),
	Insn('0x6F', b'\x10'),
	Insn('0x15', b'\x00\x00\x00\x00'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400042V#11P#5205F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 300),
	Insn('SOUND_PLAY', 1283, 0, 255, 100),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#13400043V……早安。\n'
		'罗伊德前辈。{wait}'
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
		'#13400044V#11P#5202F嗯，早安……{wait}'
		'{page}'
		'#13400045V#5205F咦……\n'
		'缇欧怎么会在这里……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400046V#6P#0203F开会时间到了，\n'
		'可是罗伊德前辈一直没下来，\n'
		'所以我来叫醒你。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(257), -500, 1500, (2, 7, 80, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400047V#11P#5205F啊……\n'
		'都已经这么晚了吗。{wait}'
		'{page}'
		'#13400048V#5206F不过，好奇怪啊……{wait}'
		'{page}'
		'#13400049V我感觉有什么冰凉的东西\n'
		'打在我的脖子上，\n'
		'难道是做梦吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400050V#6P#0203F不，不是做梦。{wait}'
		'{page}'
		'#13400051V#0200F因为我怎么摇晃，你都不醒，\n'
		'就尝试释放了极小功率的\n'
		'钻石星尘。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(257), -500, 1500, (16, 19, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400052V#11P#5211F──等一下。{wait}'
		'{page}'
		'#13400053V我好像听到了什么\n'
		'难以忽略的词语……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400054V#6P#0204F……没问题。\n'
		'因为我把功率设置到最低了。{wait}'
		'{page}'
		'#13400055V#0202F是不是完全清醒了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400056V#11P#5212F这个……倒是没错。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('SLEEP', 300),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(259), 255),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400057V#6P#0208F而且，要如何叫醒熟睡的人，\n'
		'这个问题令我十分迷惑……{wait}'
		'{page}'
		'#13400058V#0206F所以就不由得选择了\n'
		'最有效的方法。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400059V#11P#5205F如何叫醒熟睡的人……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), -500, 1500, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(257), -500, 1500, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400060V#11P#5208F（……是吗……）{wait}'
		'{page}'
		'#13400061V（这孩子以前连叫别人起床\n'
		'\u3000的经验都没有……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400062V#6P#0205F……罗伊德前辈？{wait}'
		'{page}'
		'#13400063V#0206F那个，你生气了吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400064V#11P#5204F不……怎么会生气呢。{wait}'
		'{page}'
		'#13400065V#5202F不过，以后你再叫我的时候，\n'
		'不要光是摇晃，\n'
		'出声叫我就好了。{wait}'
		'{page}'
		'#13400066V这样我一定会醒来的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400067V#6P#0202F……原来如此。{wait}'
		'{page}'
		'#13400068V#0204F──那样的话，\n'
		'只要叫『早安，主人㈱』\n'
		'就可以了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400069V#11P#5201F……为什么会是这种叫法～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400070V#6P#0211F那么，『哥哥，再不起来的话，\n'
		'我就要踢你了哦！』──这样？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('0x82', 100, 0, 2000, 200),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400071V#11P#5207F你这些都是从哪里学来的啊！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400072V#6P#0204F开玩笑的。{wait}'
		'{page}'
		'#13400073V#0202F艾莉前辈准备了早餐，\n'
		'换好衣服就请下楼来吧。{wait}'
		'{page}'
		'#13400074V那么，我就先……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(259), 180, 400),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400075V#11P#5205F啊，稍等一下。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(259), 90, 500),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400076V#6P#0205F……什么事呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('SLEEP', 150),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (2750, 700, 127100), 500),
	Insn('CAM_ROTATE', 45, 18, 0, 500),
	Insn('0x6E', 400, 500),
	Insn('CAM_DISTANCE', 23500, 500),
	Insn('CHAR_FLAG1_UNSET', Char(257), 4),
	Insn('CHAR_FLAG1_UNSET', Char(257), 32),
	Insn('CHAR_FLAG1_UNSET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 31),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_POS', Char(257), (1000, 30, 126400), 270),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('EXPR_CHAR_ATTR', Char(257), 36, Expr([Insn('CONST', 176), Insn('SET'), Insn('END')])),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('0x0D'),
	Insn('CHAR_ROTATE', Char(257), 180, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400077V#5204F#5P──谢谢你了，缇欧。{wait}'
		'{page}'
		'#13400078V#5202F你是关心我，\n'
		'才过来看看情况的吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400079V#12P#0205F哎……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 14))),
	Insn('SLEEP', 1800),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400080V#5205F#5P#N啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (1000, 1000, 126400), 0),
	Insn('CAM_ROTATE', 45, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 22500, 0),
	Insn('0x0D'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400081V#5204F#5P哈哈……\n'
		'不知为何，感觉昨天的烦恼\n'
		'全都烟消云散了。{wait}'
		'{page}'
		'#13400082V#5202F……要感谢缇欧才是啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (1390, 1000, 128419), 1500),
	Insn('CHAR_ROTATE', Char(257), 355, 400),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400083V#2P#5200F纪念庆典也到了第四天……{wait}'
		'{page}'
		'#13400084V看来今天也会很忙呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x6F', b'\x01'),
	Insn('CAM_DISTANCE', 23000, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('OBJ_SET_FRAME', Object(255), 'r_huton', Insn('1', 1)),
	Insn('OBJ_FLAG_SET', Object(13), 4),
	Insn('CALL', Function((0, 17))),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('CHAR_ROTATE', Char(259), 180, 700),
	Insn('EMOTE', Char(259), 0, 1700, (40, 43, 100, 0)),
	Insn('CAM_OFFSET', (2000, 700, 124000), 1500),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (0, 0, 120500), 4000, 1),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('EMOTE_STOP', Char(259)),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (0, 0, 119000), 4000, 0),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 300),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(259), 2),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('0x6F', b'\x01'),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50332', 30),
	Insn('LOAD_CHCP', 'apl/ch50107', 31),
	Insn('CAM_OFFSET', (3000, 700, 126000), 0),
	Insn('CAM_ROTATE', 45, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 22500, 0),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(257), 32),
	Insn('CHAR_FLAG1_SET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 10),
	Insn('CHAR_SET_POS', Char(257), (2450, 300, 125550), 180),
	Insn('EXPR_CHAR_ATTR', Char(257), 36, Expr([Insn('CONST', 170), Insn('SET'), Insn('END')])),
	Insn('CHAR_SET_POS', Char(260), (700, 30, 125300), 90),
	Insn('OBJ_SET_FRAME', Object(255), 'r_huton', Insn('0', 1)),
	Insn('OBJ_FLAG_UNSET', Object(13), 4),
	Insn('0x70', Object(13), b'\x05\x00'),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu00300.itp'),
	Insn('SOUND_PLAY', 910, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('？？？')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#13400085V#2S#60W……喂……快起床啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#13400086V#2S#50W不要一直\n'
		'呼呼大睡个没完啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#13400087V#5206F#40W……嗯…………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_NAME', Translate('？？？')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#13400088V#2S#30W唉，真拿你没办法啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 1377, 0, 255, 90),
	Insn('TEXT_SET_NAME', Translate('？？？')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#35A喂，快点起来啊！{wait}'
	)),
	Insn('SLEEP', 4200),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#13400089V#5205F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('BGM_PLAY', b'h\x00\x00'),
	Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 104), Insn('SET'), Insn('END')])),
	Insn('0xB8', 100, 104),
	Insn('0xB8', 101, 104),
	Insn('0x14', b'\x01\x00\x00\x00\xff\xff\xff\xbb\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
	Insn('CAM_DISTANCE', 23500, 1000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('SLEEP', 500),
	Insn('0x71', Object(13), b'\x05\x00', 20, 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('CHAR_SET_FRAME', Char(257), 11),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(257), 12),
	Insn('SLEEP', 300),
	Insn('CHAR_SET_FRAME', Char(257), 13),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_FRAME', Char(257), 14),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_FRAME', Char(257), 13),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_FRAME', Char(257), 12),
	Insn('SLEEP', 300),
	Insn('0x6F', b'\x10'),
	Insn('0x15', b'\x00\x00\x00\x00'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400090V#11P#5205F咦……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('SOUND_PLAY', 1366, 0, 255, 90),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 500),
	Insn('TEXT_MESSAGE', Char(260), Text(
		'#13400091V话说回来，我为什么非得\n'
		'过来叫男人起床不可啊～！{wait}'
		'{page}'
		'#13400092V被漂亮姐姐\n'
		'在早晨温柔地叫醒，\n'
		'才是本大爷的风格啊～{wait}'
		'{page}'
		'#13400093V然后再泡杯咖啡，\n'
		'悠闲享受两人世界……{wait}'
		'{page}'
		'#13400094V不不，还是直接就这样\n'
		'做点什么呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400095V#11P#5206F……抱歉。\n'
		'我的思绪还没有清醒到\n'
		'可以陪你想入非非……{wait}'
		'{page}'
		'#13400096V#5205F呃……\n'
		'已经到开会时间了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400097V#6P#0304F嗯，早就到了。{wait}'
		'{page}'
		'#13400098V#0300F大小姐和小缇\n'
		'给我们做了早饭，\n'
		'赶快去吃吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400099V#11P#5200F是吗……\n'
		'我马上换衣服。{wait}'
		'{page}'
		'#13400100V#5209F……哈哈……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400101V#6P#0305F……怎么啦？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400102V#11P#5204F只是觉得兰迪有些帅气啊。{wait}'
		'{page}'
		'#13400103V#5202F像这种关心人的方式，\n'
		'我可是怎么也都学不会呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(260), 0, 2000, (40, 43, 100, 3)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400104V#6P#0301F笨、笨蛋，你小子……\n'
		'说什么肉麻的话呢！{wait}'
		'{page}'
		'#13400105V#0303F我可没兴趣安慰\n'
		'消沉的男人啊～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400106V#11P#5214F哈哈，你这不是自己承认了吗。{wait}'
		'{page}'
		'#13400107V#5204F──没问题。\n'
		'睡了一晚上，好像镇定下来了。{wait}'
		'{page}'
		'#13400108V#5200F虽然还是有点懊悔的感觉。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400109V#6P#0302F……是吗。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CAM_OFFSET', (3420, 700, 126420), 1500),
	Insn('CHAR_FLAG1_SET', Char(260), 64),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (1400, 30, 126000), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('SLEEP', 500),
	Insn('CAM_DISTANCE', 22330, 500),
	Insn('CROSSFADE', 500),
	Insn('CHAR_FLAG1_SET', Char(260), 8),
	Insn('CHAR_SET_POS', Char(257), (2350, 150, 125820), 180),
	Insn('EXPR_CHAR_ATTR', Char(257), 45, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(257), 46, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(257), 47, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('CHAR_SET_FRAME', Char(257), 5),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(257), 6),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(257), 7),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('SLEEP', 100),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 16))),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400110V#6P#0309F──嗯，尽管去悔恨吧，青少年。{wait}'
		'{page}'
		'#13400111V只有经历过这种挫折，\n'
		'才能成长为真正的男子汉啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400112V#11P#5211F都说过不要把我\n'
		'当小孩子看待了……{wait}'
		'{page}'
		'#13400113V#5213F我换个衣服，\n'
		'你先下去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400114V#6P#0300F好好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(260), 8),
	Insn('FORK_QUIT', Char(257), 3),
	Insn('CHAR_SET_POS', Char(257), (2450, 300, 125550), 180),
	Insn('CHAR_SET_FRAME', Char(257), 12),
	Insn('EXPR_CHAR_ATTR', Char(257), 45, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(257), 46, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(257), 47, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (1000, 30, 125800), 1200, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('SLEEP', 300),
	Insn('CHAR_FLAG1_UNSET', Char(260), 64),
	Insn('CHAR_ROTATE', Char(260), 180, 500),
	Insn('CAM_OFFSET', (2000, 700, 124000), 2000),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (0, 0, 120500), 2000, 1),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (0, 0, 119000), 2000, 0),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 300),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400115V#5204F#5P#N那么……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (1000, 1000, 126400), 0),
	Insn('CAM_ROTATE', 45, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 22500, 0),
	Insn('CHAR_FLAG1_UNSET', Char(257), 4),
	Insn('CHAR_FLAG1_UNSET', Char(257), 32),
	Insn('CHAR_FLAG1_UNSET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 31),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_POS', Char(257), (1000, 30, 126400), 270),
	Insn('EXPR_CHAR_ATTR', Char(257), 36, Expr([Insn('CONST', 176), Insn('SET'), Insn('END')])),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (1390, 1000, 128419), 1500),
	Insn('CHAR_ROTATE', Char(257), 355, 400),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400116V#2P#5200F纪念庆典也到了第四天……{wait}'
		'{page}'
		'#13400117V看来今天也会很忙呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 23000, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('OBJ_SET_FRAME', Object(255), 'r_huton', Insn('1', 1)),
	Insn('OBJ_FLAG_SET', Object(13), 4),
	Insn('CALL', Function((0, 17))),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_ANIMATION', Char(254), 1000, [
			7,
			8,
			9,
			8,
		]),
	]),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (12000, 1850, 9700), 0),
	Insn('CAM_ROTATE', 37, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 26000, 0),
	Insn('CHAR_SET_POS', Char(257), (11300, 850, 9100), 45),
	Insn('CHAR_SET_POS', Char(258), (11300, 850, 10400), 135),
	Insn('CHAR_SET_POS', Char(259), (12600, 850, 9100), 315),
	Insn('CHAR_SET_POS', Char(260), (12600, 850, 10400), 225),
	Insn('SLEEP', 1000),
	Insn('0xC7', b'\x00\x00\x08\x00\x00'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{0x18}{color 0}#1K创立纪念庆典\u3000第四天{wait}'
	)),
	Insn('SLEEP', 2500),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0xC7', b'\x01\x00\x08\x00\x00'),
	Insn('CAM_DISTANCE', 25000, 2000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400118V#6P#0004F──好了，\n'
		'开始处理第四天的公务吧。{wait}'
		'{page}'
		'#13400119V#0000F保险起见，得先确认一下\n'
		'有没有收到新的请求才行。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400120V#0102F是呀。{wait}'
		'{page}'
		'#13400121V#0104F市内今天会有游行活动，\n'
		'另外，应该也会有一些游客\n'
		'前去郊外观光……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400122V#0202F寻找遗失物品和迷路走失的游客……\n'
		'类似的委托似乎都很可能出现呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400123V#5P#0306F嗯，老实说，像这些事情，\n'
		'也没可能全部照顾到。{wait}'
		'{page}'
		'#13400124V#0300F就在我们能力所及的范围之内\n'
		'尽量提供协助就好了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400125V#6P#0000F嗯，说得也是。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CAM_DISTANCE', 25250, 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (12000, 1850, 8700), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 340, 0),
	Insn('CAM_DISTANCE', 27500, 0),
	Insn('CHAR_SET_POS', Char(0), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(1), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(2), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(3), (12000, 850, 8700), 270),
	Insn('FLAG_SET', Flag(1292)),
	Insn('0xC7', b'\x01\x00\x10\x00\x00'),
	Insn('QUEST', 68, Insn('TASK_SET', 5)),
	Insn('QUEST', 69, Insn('TASK_SET', 5)),
	Insn('QUEST', 69, Insn('FLAG_UNSET', 16)),
	Insn('0xB5', b'\x01\x00\x80\x00'),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50335', 30),
	Insn('LOAD_CHCP', 'apl/ch50011', 31),
	Insn('CAM_OFFSET', (1300, 2850, 12300), 0),
	Insn('CAM_ROTATE', 45, 21, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(257), (1300, 3850, 14800), 180),
	Insn('CHAR_SET_POS', Char(258), (800, 0, 0), 0),
	Insn('CHAR_SET_POS', Char(259), (800, 0, 0), 0),
	Insn('CHAR_SET_POS', Char(260), (800, 0, 0), 0),
	Insn('CHAR_FLAG1_SET', Char(352), 4),
	Insn('CHAR_FLAG1_SET', Char(352), 2),
	Insn('CHAR_FLAG1_SET', Char(352), 32),
	Insn('CHAR_SET_CHCP', Char(352), 30),
	Insn('CHAR_SET_FRAME', Char(352), 0),
	Insn('CHAR_SET_POS', Char(352), (16500, 950, 10400), 45),
	Insn('FORK_FUNC', Char(352), 3, Function((0, 19))),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(29), 128),
	Insn('OBJ_FLAG_SET', Object(14), 4096),
	Insn('OBJ_FLAG_UNSET', Object(14), 4),
	Insn('0x78', b'\x0e', Char(29)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(29), (16200, 0, 10100), 0),
	Insn('0xD3', Char(29), 0, 45000, 0, 0),
	Insn('IMG_LOAD', ResId(0), 180, 0, b'\xb4\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis007.itp'),
	Insn('FORK_FUNC', Char(32), 1, Function((0, 20))),
	Insn('CAM_OFFSET', (1300, 1850, 10300), 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (1300, 850, 10300), 2500, 0),
	]),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 2),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('CHAR_ROTATE', Char(257), 90, 500),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400487V#6P#0005F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 4000),
	Insn('CAM_OFFSET', (16100, 1850, 10000), 3000),
	Insn('CAM_DISTANCE', 24000, 3000),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (13900, 850, 10300), 2500, 0),
	]),
	Insn('0x6F', b'\x01'),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'\n\x02\x00'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400488V#3301F#5P………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400489V#6P#0001F……莫非你是在\n'
		'通过导力网络\n'
		'搜索车辆的情报？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400490V#3303F#5P嗯，是啊。{wait}'
		'{page}'
		'#13400491V一小时前至现在，\n'
		'曾经有可能停在港湾区东南部的\n'
		'所有车辆……{wait}'
		'{page}'
		'#13400492V正在连接克洛斯贝尔的所有\n'
		'网络终端进行检索。{wait}'
		'{page}'
		'#13400493V#3300FＩＢＣ的主终端\n'
		'和小雀斑的数据库\n'
		'也让我利用一下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400494V#6P#0006F你……到底是什么人呢？{wait}'
		'{page}'
		'#13400495V#0001F著名人偶师的孙女……\n'
		'似乎并不是这么简单吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400496V#3304F#5P呵呵……爷爷只是\n'
		'蕾恩的协助者而已。{wait}'
		'{page}'
		'#13400497V会帮忙修好『爸爸和妈妈』，\n'
		'是蕾恩的同伴之一……{wait}'
		'{page}'
		'#13400498V#3302F『博士』不太值得信任，\n'
		'所以就秘密拜托他了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400499V#6P#0011F博、博士……？{wait}'
		'{page}'
		'#13400500V#0001F还有，『爸爸和妈妈』是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400501V#3304F#5P呵呵，大哥哥没有必要知道哦。{wait}'
		'{page}'
		'#13400502V在克洛斯贝尔，\n'
		'蕾恩只不过是个观察者而已。{wait}'
		'{page}'
		'#13400503V#3302F名为『小猫#4RKitty#』的观察者。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400504V#6P#0003F……果然是你吗。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400505V#3309F#5P呵呵，昨天的追踪游戏\n'
		'惊险刺激，让我紧张得心怦怦跳呢。{wait}'
		'{page}'
		'#13400506V小雀斑干得还算不错，\n'
		'那位姐姐似乎也相当有一手哦～{wait}'
		'{page}'
		'#13400507V#3302F呵呵，虽然好像用了\n'
		'一点有趣的小伎俩。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400508V#6P#0005F竟然连那个都能看得出来吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('CAM_OFFSET', (900, 1000, 3000), 2500),
	Insn('CAM_DISTANCE', 25000, 2500),
	Insn('SLEEP', 1500),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (900, 0, 3000), 2000, 0),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 450),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (1600, 0, 2000), 2000, 0),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 450),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (200, 0, 1600), 2000, 0),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 2),
	Insn('0x6F', b'\x11'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400509V#0105F#6P我们回来了，罗伊德。\n'
		'按照你说的，返回支援课了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400510V#0105F#6P哎呀……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400511V#0205F#6P这孩子是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400512V#0305F#12P好像是……\n'
		'人偶工房的那个女孩……是人偶师的孙女吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400513V#6P#0006F嗯……\n'
		'因为发生了点事。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (13000, 1850, 10000), 0),
	Insn('CAM_ROTATE', 45, 21, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_ROTATE', Char(257), 270, 0),
	Insn('CHAR_SET_POS', Char(258), (6500, 850, 9800), 90),
	Insn('CHAR_SET_POS', Char(259), (6500, 850, 10800), 90),
	Insn('CHAR_SET_POS', Char(260), (5300, 850, 10300), 90),
	Insn('CAM_OFFSET', (15000, 1850, 10000), 2500),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (12500, 850, 9800), 2500, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (12500, 850, 10800), 2500, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (11300, 850, 10300), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_QUIT', Char(32), 1),
	Insn('SLEEP', 300),
	Insn('EMOTE', Char(352), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK_QUIT', Char(352), 3),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400514V#5P#3301F──找到了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400515V#5P#3308F『莱姆斯运送公司』的搬运车\n'
		'好像在半小时之前停在那里。{wait}'
		'{page}'
		'#13400516V下一个送货点是贝尔加德门……{wait}'
		'{page}'
		'#13400517V#3304F搬运车的通讯号码是……\n'
		'嗯，这样应该就行了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('CHAR_SET_FRAME', Char(352), 0),
	Insn('SLEEP', 70),
	Insn('CHAR_SET_FRAME', Char(352), 1),
	Insn('SLEEP', 70),
	Insn('CHAR_SET_FRAME', Char(352), 2),
	Insn('SLEEP', 70),
	Insn('CHAR_SET_FRAME', Char(352), 3),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400518V#11P#3300F请联系那个通讯号码试试。{wait}'
		'{page}'
		'#13400519V应该能查出那孩子的去向。{wait}'
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
	Insn('SLEEP', 1300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400520V#6P#0004F……干得漂亮。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400521V#6P#0108F那个……这是怎么回事？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400522V#6P#0306F从刚才开始，就完全\n'
		'跟不上你们的步调……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400523V#0203F#5P──原来如此。{wait}'
		'{page}'
		'#13400524V#0201F你就是『小猫#4RKitty#』吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_WATCH', Char(258), Char(259), 500),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400525V#12P#0105F咦……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400526V#6P#0301F喂喂……\n'
		'这到底是怎么回事啊！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400527V#11P#3309F呵呵，真要感谢姐姐\n'
		'昨天陪我玩呢。{wait}'
		'{page}'
		'#13400528V#3302F不过，现在是不是应该\n'
		'把这个问题延后一下呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400529V#0206F#5P……嗯，确实没错。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400530V#6P#0001F好……\n'
		'这就联系一下试试吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('BGM_STOP', 4000),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_SET', Char(257), 32),
	Insn('CHAR_FLAG1_SET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 31),
	Insn('CHAR_SET_FRAME', Char(257), 4),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('CHAR_SET_FRAME', Char(257), 5),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('FADE_ON', 500, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}罗伊德联系了蕾恩给的通讯号码。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('SOUND_PLAY', 902, 0, 0, 100),
	Insn('SLEEP', 2700),
	Insn('SLEEP', 1100),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('青年的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400531V喂喂！\n'
		'您是哪位！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'g\x00\x00'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#13400532V#0005F啊……{wait}'
		'{page}'
		'#13400533V#0001F嗯，我是克洛斯贝尔警察局丄\n'
		'特务支援课的人……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('青年的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400534V！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400535V太、太好了！\n'
		'我正想联系游击士协会\n'
		'或者警察局呢！{wait}'
		'{page}'
		'#13400536V可、可是两边的号码我都不知道，\n'
		'所以就想联系老爸……唔！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#13400537V#0011F请、请冷静一点。{wait}'
		'{page}'
		'#13400538V#0001F您似乎有些慌乱……\n'
		'请问到底发生了什么事？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('青年的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400539V这、这个……{wait}'
		'{page}'
		'#13400540V小、小、小男孩\n'
		'不知道跑到哪里去了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#13400541V#0005F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('青年的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400542V刚才，我在西克洛斯贝尔街道的\n'
		'途中停了下车……！{wait}'
		'{page}'
		'#13400543V因为听到有动静，就去确认一下货箱，\n'
		'结果发现有个小男孩在里面……！{wait}'
		'{page}'
		'#13400544V好像是自己偷偷钻进去的。\n'
		'就这么把他带到贝尔加德门也不太好，\n'
		'所以便打算和公司商量一下……！{wait}'
		'{page}'
		'#13400545V结果，就在我通话的时候，\n'
		'那孩子不知道跑到哪里去了！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#13400546V#0013F！！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 50, 30, -1, -1),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'#13400547V#0101F怎、怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('CHAR_SET_FRAME', Char(257), 4),
	Insn('SLEEP', 300),
	Insn('CHAR_FLAG1_UNSET', Char(257), 32),
	Insn('CHAR_FLAG1_UNSET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('CHAR_ROTATE', Char(257), 270, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400548V#11P#0001F嗯……\n'
		'事情有些不妙了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}罗伊德简短地说明了情况。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('EMOTE', Char(352), 0, 1700, (2, 7, 80, 1)),
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
	Insn('TEXT_TALK', Char(352), Text(
		'#13400549V#11P#3305F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400550V#0201F#5P……怎么会……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400551V#6P#0301F这可不太妙啊……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400552V#11P#0003F嗯，赶快出发吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_SET', Char(257), 32),
	Insn('CHAR_FLAG1_SET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 31),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('FADE_ON', 500, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#13400553V#0001F我们立即就赶过去。{wait}'
		'{page}'
		'#13400554V请您不要随便乱动，\n'
		'就留在原处等待吧。{wait}'
		'{page}'
		'#13400555V说不定那个孩子还会回来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('青年的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400556V麻、麻烦你们了！{wait}'
		'{page}'
		'#13400557V无论如何，请尽快赶来……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(257), 32),
	Insn('CHAR_FLAG1_UNSET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400558V#11P#0003F赶快从西出口出去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 90, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400559V#0001F#6P还有小蕾，你就……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (14790, 1850, 10210), 500),
	Insn('CHAR_FLAG1_UNSET', Char(352), 4),
	Insn('CHAR_FLAG1_UNSET', Char(352), 2),
	Insn('CHAR_FLAG1_UNSET', Char(352), 32),
	Insn('CHAR_SET_CHCP', Char(352), 255),
	Insn('CHAR_SET_FRAME', Char(352), 0),
	Insn('CHAR_SET_POS', Char(352), (15300, 950, 10300), 315),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('0x0D'),
	Insn('CHAR_ROTATE', Char(352), 270, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400560V#11P#3300F……要一起去。{wait}'
		'{page}'
		'#13400561V蕾恩不会碍手碍脚的，\n'
		'让蕾恩也一起去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400562V#6P#0105F但、但是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400563V#0205F#5P你还是在这里等待\n'
		'比较安全吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400564V#11P#3303F找到那孩子下落的\n'
		'可是蕾恩哦。{wait}'
		'{page}'
		'#13400565V#3300F所以，蕾恩必须要\n'
		'见证到最后。{wait}'
		'{page}'
		'#13400566V#3302F呵呵……无论降临于那孩子身上的\n'
		'是何种命运。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400567V#6P#0101F你……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400568V#6P#0306F虽然不清楚有什么内情，\n'
		'不过你好像意外地执着呢。{wait}'
		'{page}'
		'#13400569V#0301F刻不容缓。\n'
		'罗伊德，带上她一起走吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400570V#0006F#6P嗯。{wait}'
		'{page}'
		'#13400571V#0001F──小蕾，\n'
		'虽然我已经知道你不是普通的\n'
		'女孩子了，但还是千万不要乱来啊。{wait}'
		'{page}'
		'#13400572V只有这一点，请一定要做到。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400573V#11P#3306F知道啦。{wait}'
		'{page}'
		'#13400574V#3300F还有，直接叫\n'
		'蕾恩的名字就可以了。{wait}'
		'{page}'
		'#13400575V不然会让人家觉得\n'
		'有点难为情呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400576V#0004F#6P哈哈，明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 270, 500),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400577V#11P#0007F──好，那就\n'
		'立即赶往西出口吧。{wait}'
		'{page}'
		'#13400578V去西克洛斯贝尔街道\n'
		'寻找柯林。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400579V#6P#0101F嗯……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400580V#0201F#5P明白了……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400581V#11P#3308F………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 25250, 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_FLAG1_SET', Char(29), 128),
	Insn('OBJ_FLAG_UNSET', Object(14), 4096),
	Insn('OBJ_FLAG_SET', Object(14), 4),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('CAM_OFFSET', (12000, 1850, 8700), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 340, 0),
	Insn('CAM_DISTANCE', 27500, 0),
	Insn('CHAR_SET_POS', Char(0), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(1), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(2), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(3), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(4), (12000, 850, 8700), 270),
	Insn('FLAG_SET', Flag(1303)),
	Insn('QUEST', 70, Insn('TASK_SET', 12)),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_ANIMATION', Char(254), 1000, [
			0,
			6,
			7,
			6,
		]),
	]),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('SOUND_PLAY', 849, 0, 0, 70),
		Insn('SOUND_PLAY', 850, 0, 0, 70),
		Insn('SLEEP', 900),
		Insn('SOUND_PLAY', 849, 0, 0, 70),
		Insn('SLEEP', 900),
	]),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50343', 30),
	Insn('LOAD_CHCP', 'chr/ch09300', 31),
	Insn('LOAD_CHCP', 'chr/ch09400', 32),
	Insn('LOAD_CHCP', 'apl/ch50344', 33),
	Insn('LOAD_CHCP', 'apl/ch50345', 34),
	Insn('CAM_OFFSET', (3000, 700, 127500), 0),
	Insn('CAM_ROTATE', 45, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('CHAR_SET_POS', Char(257), (0, 0, 119000), 0),
	Insn('CHAR_SET_POS', Char(258), (0, -1000, 118000), 0),
	Insn('CHAR_SET_POS', Char(259), (0, 0, 119000), 0),
	Insn('CHAR_SET_POS', Char(260), (0, 0, 119000), 0),
	Insn('CHAR_SET_POS', Char(352), (1000, 30, 125300), 90),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_SET', Char(13), 32),
	Insn('CHAR_FLAG1_SET', Char(13), 2),
	Insn('CHAR_SET_CHCP', Char(13), 30),
	Insn('CHAR_SET_FRAME', Char(13), 0),
	Insn('CHAR_SET_POS', Char(13), (3000, 350, 126100), 180),
	Insn('EXPR_CHAR_ATTR', Char(13), 36, Expr([Insn('CONST', 170), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_UNSET', Char(13), 128),
	Insn('CHAR_FLAG2_UNSET', Char(13), 32768),
	Insn('CHAR_SET_CHCP', Char(14), 31),
	Insn('CHAR_SET_FRAME', Char(14), 0),
	Insn('CHAR_SET_POS', Char(14), (0, -1000, 118000), 0),
	Insn('CHAR_SET_COLOR', Char(14), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_CHCP', Char(15), 32),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('CHAR_SET_POS', Char(15), (0, 0, 119000), 0),
	Insn('CHAR_SET_COLOR', Char(15), Color(0x00FFFFFF), 0),
	Insn('OBJ_SET_FRAME', Object(255), 'r_huton', Insn('0', 1)),
	Insn('OBJ_FLAG_UNSET', Object(13), 4),
	Insn('0x70', Object(13), b'\x05\x00'),
	Insn('IMG_LOAD', ResId(0), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis058.itp'),
	Insn('IMG_LOAD', ResId(1), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis059.itp'),
	Insn('IMG_LOAD', ResId(2), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis060.itp'),
	Insn('IMG_LOAD', ResId(3), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis061.itp'),
	Insn('CAM_OFFSET', (3000, 700, 126000), 3000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('SOUND_PLAY', 811, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (0, 0, 122000), 2000, 1),
	]),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 1000),
	Insn('FORK_LOOP', 352, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (1000, 30, 124000), 2000, 0),
	]),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_QUIT', Char(352), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400683V#12P#0002F……睡着了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400684V#3304F#5P呵呵……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_SET', Char(352), 32),
	Insn('CHAR_FLAG1_SET', Char(352), 2),
	Insn('CHAR_SET_CHCP', Char(352), 33),
	Insn('CHAR_SET_FRAME', Char(352), 0),
	Insn('SLEEP', 70),
	Insn('CHAR_SET_FRAME', Char(352), 1),
	Insn('SLEEP', 70),
	Insn('CHAR_SET_FRAME', Char(352), 2),
	Insn('SLEEP', 70),
	Insn('CHAR_SET_FRAME', Char(352), 3),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400685V#3300F#5P好可爱的睡脸呢……{wait}'
		'{page}'
		'#13400686V是个对罪恶一无所知，\n'
		'纯洁无垢的好孩子啊……{wait}'
		'{page}'
		'#13400687V#3304F……都长得这么大了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400688V#12P#0008F…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(352), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400689V#12P#0003F我刚才联系了\n'
		'这孩子的父母。{wait}'
		'{page}'
		'#13400690V#0000F他们说马上就来接他。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400691V#3308F#5P是吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400692V#12P#0001F你是最大的功臣。{wait}'
		'{page}'
		'#13400693V我认为，理应把你\n'
		'介绍给他们……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400694V#3303F#5P──没这个必要哦。{wait}'
		'{page}'
		'#13400695V#3300F蕾恩的名字，以及存在，\n'
		'都没有必要告诉那些人。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400696V#12P#0008F可是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400697V#12P#0001F──我说，蕾恩。{wait}'
		'{page}'
		'#13400698V我已经明白你不是可以用常识\n'
		'来衡量的普通女孩子了。{wait}'
		'{page}'
		'#13400699V#0003F投掷那把大镰刀的能力、\n'
		'以『小猫#4RKitty#』的身份所使用的黑客技术……{wait}'
		'{page}'
		'#13400700V还有推定那孩子所在位置时的\n'
		'理性而多角度的推理能力……{wait}'
		'{page}'
		'#13400701V#0008F……你实在是太过多才多艺，\n'
		'甚至都让人感觉有些不太现实……{wait}'
		'{page}'
		'#13400702V#0000F我现在已经理解了，\n'
		'你就是那种真正意义上的『天才』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400703V#3304F#5P呵呵……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_CHCP', Char(352), 33),
	Insn('CHAR_SET_FRAME', Char(352), 3),
	Insn('SLEEP', 70),
	Insn('CHAR_SET_FRAME', Char(352), 2),
	Insn('SLEEP', 70),
	Insn('CHAR_SET_FRAME', Char(352), 1),
	Insn('SLEEP', 70),
	Insn('CHAR_FLAG1_UNSET', Char(352), 32),
	Insn('CHAR_FLAG1_UNSET', Char(352), 2),
	Insn('CHAR_SET_CHCP', Char(352), 255),
	Insn('CHAR_SET_FRAME', Char(352), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400704V#3302F#5P──大哥哥，你果然\n'
		'很有一套呢。{wait}'
		'{page}'
		'#13400705V#3304F没错，蕾恩的本质正在于此。{wait}'
		'{page}'
		'#13400706V吸收各种情报并加以处理，\n'
		'对包括自己在内的环境进行适当操作……{wait}'
		'{page}'
		'#13400707V#3300F战斗技术、黑客知识、博士论文、\n'
		'人偶操作、茶会礼仪等等，\n'
		'可以说，全都是由这个本质发展而来的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400708V#12P#0011F博、博士论文！？{wait}'
		'\n'
		'#13400709V#0003F──好吧，这个暂且忽略。{wait}'
		'{page}'
		'#13400710V#0001F也就是说，你心里是很清楚的。{wait}'
		'{page}'
		'#13400711V清楚到底应该怎样做，\n'
		'才能实现自己的愿望。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400712V#3309F#5P嘻嘻，正是。{wait}'
		'{page}'
		'#13400713V#3302F不管是什么愿望，\n'
		'蕾恩都能够实现。{wait}'
		'{page}'
		'#13400714V不，正确来说，\n'
		'是明白应该怎样做，\n'
		'才能让世界为蕾恩实现愿望。{wait}'
		'{page}'
		'#13400715V#3304F因为这就是蕾恩的力量的本质。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400716V#12P#0006F……原来如此啊。{wait}'
		'{page}'
		'#13400717V#0001F既然如此──\n'
		'那你究竟有什么愿望呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(352), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400718V#3305F#5P…………哎………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400719V#12P#0003F你本应是无论有什么愿望，\n'
		'都能让世界为你实现的小公主……{wait}'
		'{page}'
		'#13400720V但是，现在的你，\n'
		'看起来却更像是一只不知该何去何从，\n'
		'完全迷失了路途的小猫。{wait}'
		'{page}'
		'#13400721V#0008F不……说不定，你其实早就知道\n'
		'自己真正的归宿在哪里。{wait}'
		'{page}'
		'#13400722V然而，却有好几块巨石\n'
		'阻挡在归途中，让你无法回去……{wait}'
		'{page}'
		'#13400723V#0001F难道不是这样吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400724V#3308F#5P……………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400725V#12P#0004F……这都是我的直觉和臆测。\n'
		'如果猜错的话，我愿意道歉。{wait}'
		'{page}'
		'#13400726V#0000F──但是，我们是特务支援课。{wait}'
		'{page}'
		'#13400727V如果有女孩子在烦恼，\n'
		'就希望能尽力帮助她……{wait}'
		'{page}'
		'#13400728V#0002F即使没办法陪你一起回去，\n'
		'至少也可以帮你搬走那些岩石。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400729V#3309F#5P……呵呵……{wait}'
		'{page}'
		'#13400730V#3300F大哥哥，看来你不仅擅长推理，\n'
		'连妄想也很拿手呢。{wait}'
		'{page}'
		'#13400731V#3302F像你这种人……\n'
		'又能了解蕾恩多少呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400732V#12P#0006F我当然不了解你。{wait}'
		'{page}'
		'#13400733V而且，说不定你其实已经有了\n'
		'真正想要依靠的人。{wait}'
		'{page}'
		'#13400734V#0000F不过──横在路上的岩石\n'
		'并不只有一块吧？{wait}'
		'{page}'
		'#13400735V有没有那种连我们也能搬走的……\n'
		'比较小的岩石呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400736V#3308F#5P#30W那种……那种事……{wait}'
		'{page}'
		'#13400737V#3306F#40W……………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 811, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(352), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(257), 190, 500),
	Insn('TEXT_TALK2', Char(258), Translate('艾莉的声音'), Text(
		'#13400738V#1P#2S……罗伊德？\n'
		'哈罗德夫妇已经来了。{wait}'
		'{page}'
		'#13400739V#2S我带他们进来了哦？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400740V#0011F#5P不，那个──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(352), 500),
	Insn('SLEEP', 800),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400741V#3308F#40W#5P………………啊…………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400742V#12P#0000F……不然的话，\n'
		'你先藏在衣橱里如何？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400743V#3305F#5P啊……{wait}'
		'{page}'
		'#13400744V#3306F………………（点头）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(352), 500),
	]),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (0, 30, 124000), 1500, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 352, 1, [
		Insn('0x95', Char(254), (1000, 0, 122500), 4000, 1),
	]),
	Insn('FORK_AWAIT', Char(352), 1),
	Insn('FORK', 352, 1, [
		Insn('0x95', Char(254), (2000, 30, 121500), 4000, 0),
	]),
	Insn('FORK_AWAIT', Char(352), 1),
	Insn('OBJ_SET_FRAME', Object(255), 'boxopen', Insn('2', 'move')),
	Insn('SOUND_PLAY', 913, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('FORK', 352, 1, [
		Insn('0x96', Char(254), (3000, 30, 121000), 1000, 0),
	]),
	Insn('FORK', 352, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(352), 1),
	Insn('FORK_AWAIT', Char(352), 2),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('OBJ_SET_FRAME', Object(255), 'boxopen', Insn('2', 'move2')),
	Insn('SOUND_PLAY', 914, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('CHAR_ROTATE', Char(257), 180, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400745V#0000F#5P──嗯！\n'
		'请他们进来吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(258), Translate('艾莉的声音'), Text(
		'#13400746V#1P#2S……？\n'
		'好的，稍等一下哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 811, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('CHAR_FLAG1_UNSET', Char(14), 128),
	Insn('CHAR_FLAG2_UNSET', Char(14), 32768),
	Insn('TEXT_TALK2', Char(14), Translate('男性的声音'), Text(
		'#13400747V#1P#2S打扰了……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_FLAG1_UNSET', Char(15), 128),
	Insn('CHAR_FLAG2_UNSET', Char(15), 32768),
	Insn('CHAR_SET_POS', Char(14), (0, 0, 119000), 0),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('FORK_FUNC', Char(14), 3, Function((0, 22))),
	Insn('SLEEP', 500),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(14), 500),
	]),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (-900, 30, 126000), 1500, 0),
	]),
	Insn('FORK_FUNC', Char(15), 3, Function((0, 23))),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(15), Text(
		'#13400748V#3707F#5P#8A啊啊……柯林！{wait}'
	)),
	Insn('FORK_AWAIT', Char(14), 3),
	Insn('FORK_AWAIT', Char(15), 3),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('TEXT_TALK', Char(14), Text(
		'#13400749V#3609F#5P太好了……\n'
		'真是太好了……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (1000, 700, 126000), 2500),
	Insn('CAM_ROTATE', 45, 21, 0, 2500),
	Insn('CAM_DISTANCE', 24000, 2500),
	Insn('CHAR_SET_POS', Char(258), (0, 0, 119000), 0),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (-900, 30, 124500), 2000, 0),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (-1100, 30, 123100), 2000, 0),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (-100, 30, 123100), 2000, 0),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('0x6F', b'y'),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400750V#12P#0105F（咦……蕾恩呢？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(258), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400751V#0006F#5P（嗯……\n'
		'\u3000她有点原因，不方便露面。）{wait}'
		'{page}'
		'#13400752V#0008F（就藏在那边的衣橱里。）{wait}'
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
		'#13400753V#12P#0101F（哎？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400754V#12P#0205F（这又是怎么回事呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400755V#12P#0305F（好像有什么隐情啊。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(14), 270, 500),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(14), Text(
		'#13400756V#11P#3610F──各位，\n'
		'真是太感激你们了。{wait}'
		'{page}'
		'#13400757V#3601F我真不知该如何道谢才好……\n'
		'大恩大德，实在是永生难忘……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}哈罗德深深低下了头。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 3)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400758V#6P#0011F您言重了……！\n'
		'请赶快把头抬起来吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400759V#6P#0100F那个，对我们来说，\n'
		'寻找柯林也只是执行分内的任务而已……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(15), 270, 500),
	Insn('TEXT_TALK', Char(15), Text(
		'#13400760V#3701F#11P哪里，哪里！{wait}'
		'{page}'
		'#13400761V#3708F如果各位没有找到他，\n'
		'柯林可能就……这孩子可能就会……{wait}'
		'{page}'
		'#13400762V#3710F……呜呜呜……\n'
		'真是……真是太好了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(14), Char(15), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(14), Text(
		'#13400763V#3600F没事了……已经没事了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400764V#12P#0301F唔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400765V#6P#0208F为什么会如此激动……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13400766V#11P#60W嗯……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(14), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(15), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (3000, 700, 126000), 1500),
	Insn('CAM_ROTATE', 45, 24, 0, 1500),
	Insn('CAM_DISTANCE', 23500, 1500),
	Insn('FORK', 14, 2, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK', 15, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('SLEEP', 1200),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(13), 34),
	Insn('CHAR_SET_FRAME', Char(13), 1),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('CHAR_SET_FRAME', Char(13), 0),
	Insn('SLEEP', 250),
	Insn('CHAR_SET_FRAME', Char(13), 1),
	Insn('SLEEP', 250),
	Insn('CHAR_SET_FRAME', Char(13), 0),
	Insn('SLEEP', 250),
	Insn('CHAR_SET_FRAME', Char(13), 1),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(15), Text(
		'#13400767V#6P#3700F柯林……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13400768V#11P#3805F哎……？{wait}'
		'{page}'
		'#13400769V为什么\n'
		'爸爸和妈妈会在这里～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#13400770V#6P#3709F啊啊，柯林……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#13400771V#6P#3609F……太好了……真是太好了……！{wait}'
		'{page}'
		'#13400772V#3600F以后可不能再这样了哦……\n'
		'让爸爸和妈妈这么担心……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13400773V#11P#3800F？？？{wait}'
		'{page}'
		'#13400774V#3809F听我说哦～！\n'
		'刚刚玩得好开心呢～！{wait}'
		'{page}'
		'#13400775V我追着咪西的车子，\n'
		'还交了好多原本不认识的朋友！{wait}'
		'{page}'
		'#13400776V然后一起玩捉迷藏，爬上了\n'
		'都是货物的车子，里面好黑好暗的～！{wait}'
		'{page}'
		'#13400777V出来之后，又看到了\n'
		'好漂亮的黄色蝴蝶哦！{wait}'
		'{page}'
		'#13400778V#3802F然后、然后呢……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(13), -400, 1200, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(13)),
	Insn('TEXT_TALK', Char(13), Text(
		'#13400779V#11P#3805F哎……？{wait}'
		'{page}'
		'#13400780V紫色的姐姐呢～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(14), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(15), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(14), Text(
		'#13400781V#6P#3605F紫色的……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#13400782V#6P#3700F姐姐……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13400783V#11P#3809F嗯～！{wait}'
		'{page}'
		'#13400784V跟你们说哦！\n'
		'她好强好强呢～！{wait}'
		'{page}'
		'#13400785V而且好温柔，\n'
		'还很香……{wait}'
		'{page}'
		'#13400786V#3802F还有哦……\n'
		'她的头发和爸爸一样，\n'
		'是紫色的哦～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(14), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(15), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(15), Text(
		'#13400787V#6P#3705F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 14, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 400),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_ROTATE', Char(15), 270, 400),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(14), Text(
		'#13400788V#11P#3601F请问……\n'
		'那位女孩是！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400789V#6P#0006F那个……是帮我们寻找\n'
		'柯林的女孩子。{wait}'
		'{page}'
		'#13400790V#0008F好像是外国的旅行者……\n'
		'至于身份，我们也不太清楚。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#13400791V#11P#3603F是、是这样啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#13400792V#11P#3708F………竟然有这种事…………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13400793V#5P#3809F#40W姐姐……\n'
		'……好想再见她一面哦……{wait}'
		'{page}'
		'#13400794V#60W嘿嘿……\n'
		'然后再……\n'
		'………请她和我玩………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(13), 30),
	Insn('CHAR_SET_FRAME', Char(13), 0),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('FORK', 15, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_ROTATE', Char(14), 90, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(15), Text(
		'#13400795V#6P#3705F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(13), Text(
		'#13400796V#5P#60W……呼～呼……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#13400797V#6P#3700F柯林……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#13400798V#6P#3600F哈哈……\n'
		'又睡着了吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400799V#6P#0004F不嫌弃的话，\n'
		'就让他在这继续睡吧。{wait}'
		'{page}'
		'#13400800V#0000F我们这里没问题的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (1420, 700, 126070), 2000),
	Insn('CAM_ROTATE', 45, 21, 0, 2000),
	Insn('CAM_DISTANCE', 24000, 2000),
	Insn('FORK', 14, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 400),
	]),
	Insn('SLEEP', 100),
	Insn('CHAR_ROTATE', Char(15), 270, 400),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(14), Text(
		'#13400801V#11P#3609F太感谢了。\n'
		'真是一直给你们添麻烦……{wait}'
		'{page}'
		'#13400802V#3600F话说回来……\n'
		'和我同样发色的女孩吗？{wait}'
		'{page}'
		'#13400803V#3604F或许这也是女神#4R爱德斯#\n'
		'和那孩子的指引啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#13400804V#3700F#11P嗯……我也这么觉得。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400805V#6P#0001F那个……\n'
		'似乎有什么隐情啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#13400806V#11P#3605F啊，不……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(15), Char(14), 400),
	Insn('TEXT_TALK', Char(15), Text(
		'#13400807V#3700F……亲爱的，我不介意。{wait}'
		'{page}'
		'#13400808V人家帮了我们这么大的忙，\n'
		'没必要对他们隐瞒……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#13400809V#11P#3600F……说得也是。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 15, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 400),
	]),
	Insn('EMOTE', Char(14), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(14)),
	Insn('TEXT_TALK', Char(14), Text(
		'#13400810V#11P#3603F──我们夫妇\n'
		'曾经有过一个女儿。{wait}'
		'{page}'
		'#13400811V那已经是七年以前的事情了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400812V#6P#0005F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400813V#6P#0101F请问……\n'
		'您说曾经，也就是说……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#13400814V#11P#3608F是的，因为一场不幸的事故……{wait}'
		'{page}'
		'#13400815V#3610F不──不是事故。{wait}'
		'{page}'
		'#13400816V#3601F那孩子……可以说是\n'
		'被我们亲手害死的。{wait}'
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
	Insn('TEXT_TALK', Char(259), Text(
		'#13400817V#6P#0205F哎……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400818V#12P#0301F这话怎么说……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 23500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 4000),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'\x01\x02\x00'),
	Insn('0xC7', b'\x00\x00\x08\x00\x00'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{0x18}{color 12}#13400819V#30W──八年前。{wait}'
		'{page}'
		'#13400820V#30W我还是个初出茅庐的贸易商。\n'
		'为了在逐渐扩大的克洛斯贝尔贸易市场\n'
		'占据一席之地，我拼尽了浑身解数。{wait}'
		'{page}'
		'#13400821V#30W最后不惜在共和国那边\n'
		'做起了危险的投机买卖……{wait}'
		'{page}'
		'#13400822V#30W结果，因此背上了巨额的债务。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0xC7', b'\x01\x00\x08\x00\x00'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 1000, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('SLEEP', 500),
	Insn('0xC7', b'\x00\x00\x08\x00\x00'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{0x18}{color 12}#13400823V#30W我们带着年幼的女儿，开始了逃亡生活……{wait}'
		'{page}'
		'#13400824V可是，我们逃到哪里，债主就会追到哪里，\n'
		'我们找不到任何安身之处。{wait}'
		'{page}'
		'#13400825V#30W再这样下去，说不定会迫使\n'
		'恶名昭彰的黑手党出马──{wait}'
		'{page}'
		'#13400826V#30W害怕事态发展到那种地步的我们，\n'
		'便将女儿托付给了一个老朋友。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0xC7', b'\x01\x00\x08\x00\x00'),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 1000, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 0, 0),
	Insn('SLEEP', 500),
	Insn('0xC7', b'\x00\x00\x08\x00\x00'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{0x18}{color 12}#13400827V#30W──那是一个居住在共和国，很值得信赖的友人。{wait}'
		'{page}'
		'#13400828V#30W我们打算尽快偿还掉所有欠款……\n'
		'等到再无借债之后，\n'
		'再回来迎接女儿。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 1000, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{0x18}{color 12}#13400829V#30W──幸好，在一位可靠律师的帮助之下，\n'
		'我们总算是理清了债务。{wait}'
		'{page}'
		'#13400830V#30W然后托关系、找门路、重建事业，\n'
		'拼死拼活地努力工作……{wait}'
		'{page}'
		'#13400831V#30W最后，总算在一年之内，\n'
		'成功还清了所有的欠款。{wait}'
		'{page}'
		'#13400832V#30W这下终于能见到女儿了……\n'
		'一家三口终于能再次团聚在一起，幸福地生活了……{wait}'
		'{page}'
		'#13400833V#30W……我们怀着这样的喜悦之情……\n'
		'来到了那个朋友的家，准备接回女儿……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0xC7', b'\x01\x00\x08\x00\x00'),
	Insn('IMG_0xC9', (ResId(2), 3), Color(0xFFFFFFFF), 2000, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
	Insn('SLEEP', 1500),
	Insn('0xC7', b'\x00\x00\x08\x00\x00'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{0x18}{color 12}#13400834V#30W──听说，是发生了原因不明的火灾。{wait}'
		'{page}'
		'#13400835V#30W当时，有组织的放火抢劫事件\n'
		'在共和国那边似乎频频发生……{wait}'
		'{page}'
		'#13400836V#30W我那个朋友的家也遭到了袭击。{wait}'
		'{page}'
		'#13400837V#30W由于朋友的家位于郊外，\n'
		'所以负责处理的部门发现得很晚……{wait}'
		'{page}'
		'#13400838V#30W而且……我们寄养在那里的女儿\n'
		'也被卷入到了事件……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(2), 3), Color(0x00FFFFFF), 1000, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{0x18}{color 12}#13400839V#30W我们……\n'
		'几近疯狂地寻找着女儿。{wait}'
		'{page}'
		'#13400840V#30W可是……每具遗体都是无法辨认的惨状。\n'
		'最终，我们得到了家中所有人都已身亡的\n'
		'验尸结果。{wait}'
		'{page}'
		'#13400841V#30W我们的女儿……\n'
		'我们无可替代的宝贝，\n'
		'已经永远地失去了。{wait}'
		'{page}'
		'#13400842V#30W留给我们的……\n'
		'只有无尽的绝望。{wait}'
		'{page}'
		'#13400843V#30W……是我们将死亡的命运带给了那孩子，\n'
		'而自己继续活下去，究竟还有什么意义……{wait}'
		'{page}'
		'#13400844V#30W我们甚至都想过自尽，\n'
		'夫妻二人一起追随那孩子而去……{wait}'
		'{page}'
		'#13400845V#30W──可就在这时，却突然发生了一件意外之事。{wait}'
		'{page}'
		'#13400846V#30W我的妻子已经怀上了柯林……\n'
		'也就是那个孩子的弟弟。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0xC7', b'\x01\x00\x08\x00\x00'),
	Insn('IMG_0xC9', (ResId(3), 3), Color(0xFFFFFFFF), 1000, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(3), 3))),
	Insn('SLEEP', 500),
	Insn('0xC7', b'\x00\x00\x08\x00\x00'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{0x18}{color 12}#13400847V#30W人就是这么现实，当发现了这一事实后，\n'
		'我们便找回了生存的勇气。{wait}'
		'{page}'
		'#13400848V#30W我们下定了决心，绝不会再重蹈覆辙，\n'
		'之后就脚踏实地，一心一意地诚信经商……{wait}'
		'{page}'
		'#13400849V#30W就这样，柯林诞生了……\n'
		'我们也渐渐从绝望的打击中再次站了起来。{wait}'
		'{page}'
		'#13400850V#30W──然而，长久以来，\n'
		'我们其实一直都在逃避。{wait}'
		'{page}'
		'#13400851V#30W逃避着自己因为无能\n'
		'而将爱女害死的痛苦……{wait}'
		'{page}'
		'#13400852V#30W……逃避着我们所犯下的罪孽……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0xC7', b'\x01\x00\x08\x00\x00'),
	Insn('IMG_0xC9', (ResId(3), 3), Color(0x00FFFFFF), 1000, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(3), 3))),
	Insn('CAM_DISTANCE', 24000, 2000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(15), Text(
		'#13400853V#3710F#11P…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#13400854V#11P#3608F这就是──\n'
		'我们夫妇所背负的罪孽。{wait}'
		'{page}'
		'#13400855V#3603F实在抱歉……\n'
		'让你们听我说了这么多令人难受的话……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400856V#6P#0008F……竟然有这种事…………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400857V#6P#0106F这……真不知该说什么好……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400858V#12P#0306F……这就是因果循环啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400859V#6P#0208F…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#13400860V#3708F#11P可是……\n'
		'随着这孩子逐渐长大，\n'
		'模样就和女儿越来越像……{wait}'
		'{page}'
		'#13400861V不知不觉中，我们又开始\n'
		'被强烈的罪恶感所苛责。{wait}'
		'{page}'
		'#13400862V#3710F……当时，若是没有放开\n'
		'那双小手该多好……{wait}'
		'{page}'
		'#13400863V无论多么痛苦、多么艰辛，\n'
		'一家人一起坚持努力就好了……{wait}'
		'{page}'
		'#13400864V这追悔莫及的感觉，\n'
		'无时无刻不萦绕在我们心头……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#13400865V#11P#3603F……于是，我们便重新\n'
		'坚定了这样一个信念。{wait}'
		'{page}'
		'#13400866V#3600F能怀上柯林，\n'
		'是因为亡女和女神#4R爱德斯#的指引……{wait}'
		'{page}'
		'#13400867V正因如此，我们一家人……\n'
		'必须要过得幸福才行。{wait}'
		'{page}'
		'#13400868V这才是回报女儿的\n'
		'唯一方法……{wait}'
		'{page}'
		'#13400869V#3603F……即使我们深知，\n'
		'这只不过是自私的借口罢了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400870V#6P#0108F哈罗德先生……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400871V#6P#0204F……我认为，这也是\n'
		'一种值得赞同的思考方式。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400872V#12P#0302F嗯……比起捶胸顿足、\n'
		'止步不前可要强得多了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#13400873V#11P#3609F哈哈……谢谢你们。{wait}'
		'{page}'
		'#13400874V#3600F……话说回来……\n'
		'还真是不可思议呢。{wait}'
		'{page}'
		'#13400875V听说，那位救了柯林的小姑娘……\n'
		'发色和我一样吧。{wait}'
		'{page}'
		'#13400876V#3604F那孩子──我们去世的女儿\n'
		'也有同样的紫色头发呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400877V#6P#0005F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400878V#6P#0108F也就是说……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#13400879V#3709F#11P嗯……简直就像是那孩子\n'
		'从天堂降临，保护了柯林一样……{wait}'
		'{page}'
		'#13400880V#3700F──对了，各位。{wait}'
		'{page}'
		'#13400881V如果以后找到那位小姑娘的话，\n'
		'可以再和我们联系吗？{wait}'
		'{page}'
		'#13400882V希望能与她正式见个面……\n'
		'衷心地向她表示感谢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400883V#6P#0003F──我明白了。{wait}'
		'{page}'
		'#13400884V#0000F……如果能联系上的话，\n'
		'我一定会转告给那孩子。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 24500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 514), Insn('SET'), Insn('END')])),
	Insn('CHAR_SET_COLOR', Char(352), Color(0xFFFFFFFF), 0),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'c020c', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('FORK', 14, 1, [
		Insn('0x95', Char(254), (0, 0, 122000), 3000, 1),
	]),
	Insn('FORK', 14, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(14), 1),
	Insn('FORK', 14, 1, [
		Insn('0x95', Char(254), (1200, 30, 125700), 3000, 0),
	]),
	Insn('FORK_AWAIT', Char(14), 1),
	Insn('CHAR_ROTATE', Char(14), 90, 500),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('FORK', 15, 1, [
		Insn('0x95', Char(254), (0, 0, 122000), 3000, 1),
	]),
	Insn('FORK', 15, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(15), 1),
	Insn('FORK', 15, 1, [
		Insn('0x95', Char(254), (1200, 30, 124700), 3000, 0),
	]),
	Insn('FORK_AWAIT', Char(15), 1),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('LOAD_CHCP', 'chr/ch00202', 32),
	Insn('LOAD_CHCP', 'chr/ch00302', 33),
	Insn('LOAD_CHCP', 'chr/ch00600', 34),
	Insn('LOAD_CHCP', 'apl/ch50346', 35),
	Insn('LOAD_CHCP', 'chr/ch00700', 36),
	Insn('LOAD_CHCP', 'apl/ch50349', 37),
	Insn('LOAD_CHCP', 'apl/ch50115', 38),
	Insn('CAM_OFFSET', (0, 900, 121500), 0),
	Insn('CAM_ROTATE', 45, 17, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 23000, 0),
	Insn('CHAR_SET_POS', Char(257), (100, 30, 121800), 90),
	Insn('CHAR_SET_POS', Char(260), (200, 30, 123100), 135),
	Insn('CHAR_SET_POS', Char(259), (-800, 30, 123000), 135),
	Insn('CHAR_SET_POS', Char(258), (-1300, 30, 121300), 90),
	Insn('CHAR_SET_POS', Char(352), (3000, 30, 121000), 315),
	Insn('CHAR_SET_COLOR', Char(352), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_CHCP', Char(16), 34),
	Insn('CHAR_SET_FRAME', Char(16), 0),
	Insn('CHAR_SET_CHCP', Char(17), 36),
	Insn('CHAR_SET_FRAME', Char(17), 0),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu00800.itp'),
	Insn('IMG_LOAD', ResId(1), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu00900.itp'),
	Insn('IMG_LOAD', ResId(2), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis163.itp'),
	Insn('CAM_OFFSET', (1500, 900, 121500), 3000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400885V#6P#0003F……他们回去了。{wait}'
		'{page}'
		'#13400886V#0000F你可以出来了哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(352), Translate('蕾恩'), Text(
		'#13400887V#2S#11P#40W………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('OBJ_SET_FRAME', Object(255), 'boxopen', Insn('2', 'move')),
	Insn('SOUND_PLAY', 913, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('CAM_DISTANCE', 21500, 2500),
	Insn('FORK', 352, 1, [
		Insn('0x96', Char(254), (2000, 30, 121500), 800, 0),
	]),
	Insn('FORK', 352, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(352), 1),
	Insn('FORK_AWAIT', Char(352), 2),
	Insn('OBJ_SET_FRAME', Object(255), 'boxopen', Insn('2', 'move2')),
	Insn('SOUND_PLAY', 914, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('CHAR_ROTATE', Char(352), 270, 400),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400888V#11P#3313F#60W……………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400889V#6P#0105F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400890V#0208F#6P蕾恩……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400891V#6P#0008F……这样好吗？{wait}'
		'{page}'
		'#13400892V#0001F现在追过去的话，\n'
		'应该还来得及……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400893V#11P#3312F#40W……不……不用了……{wait}'
		'{page}'
		'#13400894V因为，蕾恩来这个城市的原因……\n'
		'已经有一个消失掉了……{wait}'
		'{page}'
		'#13400895V#3314F所以……这样就足够了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400896V#6P#0006F是吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400897V#6P#0101F怎么能这样……\n'
		'真的没关系吗……！？{wait}'
		'{page}'
		'#13400898V蕾恩，\n'
		'不管再怎么想，你也……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(260), Char(258), 500),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400899V#0306F#5P──别说了，大小姐。{wait}'
		'{page}'
		'#13400900V#0301F这世上，有一些隐情\n'
		'是遵纪守法的普通人无法想像的。{wait}'
		'{page}'
		'#13400901V外人还是不要插嘴为好啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400902V#6P#0108F这、这个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(259), Char(258), 500),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400903V#0206F……我也有同感。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400904V#6P#0008F……………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400905V#11P#3314F#40W呵呵……别露出这种表情嘛。{wait}'
		'{page}'
		'#13400906V#3312F#40W──谢谢你，大哥哥。{wait}'
		'{page}'
		'#13400907V挡在蕾恩的归途上的\n'
		'#40W几块大石头……{wait}'
		'{page}'
		'#13400908V#3300F你已经帮我搬掉其中一块了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 135, 400),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 135, 400),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400909V#6P#0006F是吗……{wait}'
		'{page}'
		'#13400910V#0000F能帮助你，是我的荣幸。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(352), Text(
		'#13400911V#11P#3300F呵呵……\n'
		'也要感谢大姐姐们。{wait}'
		'{page}'
		'#13400912V#3312F……今天的谢礼，\n'
		'以后一定会补上的……{wait}'
		'{page}'
		'#13400913V#3314F所以……\n'
		'蕾恩就先告辞啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('CHAR_FLAG1_SET', Char(352), 32),
	Insn('CHAR_FLAG1_SET', Char(352), 2),
	Insn('CHAR_SET_CHCP', Char(352), 38),
	Insn('CHAR_SET_FRAME', Char(352), 4),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(352), 5),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(352), 6),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(352), 7),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(352), 6),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(352), 5),
	Insn('SLEEP', 100),
	Insn('CHAR_FLAG1_UNSET', Char(352), 32),
	Insn('CHAR_FLAG1_UNSET', Char(352), 2),
	Insn('CHAR_SET_CHCP', Char(352), 255),
	Insn('CHAR_SET_FRAME', Char(352), 0),
	Insn('SLEEP', 500),
	Insn('0x92', Char(352), 0, 120400, 500),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(352), 500),
	]),
	Insn('FORK_LOOP', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(352), 500),
	]),
	Insn('FORK_LOOP', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(352), 500),
	]),
	Insn('FORK_LOOP', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(352), 500),
	]),
	Insn('FORK', 352, 1, [
		Insn('0x95', Char(254), (0, 0, 120400), 2000, 1),
	]),
	Insn('FORK_AWAIT', Char(352), 1),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('FORK', 352, 1, [
		Insn('0x95', Char(254), (0, 0, 119000), 2000, 0),
	]),
	Insn('FORK', 352, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 300),
	]),
	Insn('SLEEP', 800),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400914V#0011F#5P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FORK_AWAIT', Char(352), 1),
	Insn('FORK_AWAIT', Char(352), 2),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('FORK_QUIT', Char(258), 2),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (3300, 1000, 63700), 0),
	Insn('CAM_ROTATE', 40, 23, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('CHAR_SET_POS', Char(257), (8000, 0, 64500), 180),
	Insn('CHAR_SET_POS', Char(258), (8000, 0, 64500), 180),
	Insn('CHAR_SET_POS', Char(259), (8000, 0, 64500), 180),
	Insn('CHAR_SET_POS', Char(260), (8000, 0, 64500), 180),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(352), (2700, 0, 62700), 270),
	Insn('CHAR_SET_COLOR', Char(352), Color(0xFFFFFFFF), 0),
	Insn('FORK_FUNC', Char(352), 3, Function((0, 31))),
	Insn('CAM_OFFSET', (-700, 1000, 63700), 4000),
	Insn('0x0D'),
	Insn('SLEEP', 1000),
	Insn('OBJ_FLAG_UNSET', Object(2), 16),
	Insn('0x71', Object(2), b'\x00\x00', 5, 0),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('0x79', b'\x02\x00'),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 27))),
	Insn('SLEEP', 450),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 28))),
	Insn('SLEEP', 450),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 29))),
	Insn('SLEEP', 450),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 30))),
	Insn('FORK_AWAIT', Char(352), 3),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400915V#0008F#11P………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400916V#12P#0108F……这样真的好吗？\n'
		'不追上去保护她没关系吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400917V#5P#0006F嗯……\n'
		'这个我当然也想过。{wait}'
		'{page}'
		'#13400918V#0000F不过，我感觉\n'
		'那并不是属于我们的使命。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400919V#0305F哎……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400920V#0205F#11P又是罗伊德前辈\n'
		'拿手的推理吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400921V#5P#0002F不，与其说是推理──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_POS', Char(16), (2000, -1000, 69500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(16), 128),
	Insn('CHAR_FLAG2_UNSET', Char(16), 32768),
	Insn('CHAR_FLAG1_SET', Char(16), 8),
	Insn('SLEEP', 300),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK2', Char(16), Translate('？？？'), Text(
		'#13400922V#1P#2S#15A#40W请问～有人在吗～！{wait}'
	)),
	Insn('SLEEP', 2000),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400923V#0005F#6P这声音是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400924V#12P#0105F好像是从一楼传来的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-700, 500, 63700), 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('CAM_OFFSET', (1500, 2850, 10200), 0),
	Insn('CAM_ROTATE', 47, 21, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 26500, 0),
	Insn('CHAR_SET_POS', Char(257), (900, 3000, 14000), 180),
	Insn('CHAR_SET_POS', Char(258), (2000, 3000, 14000), 180),
	Insn('CHAR_SET_POS', Char(259), (900, 3500, 14500), 180),
	Insn('CHAR_SET_POS', Char(260), (2000, 3500, 14500), 180),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(16), (400, 0, 1700), 0),
	Insn('CHAR_SET_POS', Char(17), (1500, 0, 1500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(16), 128),
	Insn('CHAR_FLAG2_UNSET', Char(16), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(16), 8),
	Insn('CHAR_FLAG1_UNSET', Char(17), 128),
	Insn('CHAR_FLAG2_UNSET', Char(17), 32768),
	Insn('CAM_OFFSET', (1500, 1850, 10100), 3000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (900, 850, 9500), 2000, 0),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (2000, 850, 9500), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (900, 850, 10800), 2000, 0),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (2000, 850, 10800), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
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
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400925V#0102F#5P哎呀……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400926V#5P#0000F你们是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 4000),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('CAM_OFFSET', (400, 1100, 2900), 2000),
	Insn('CAM_ROTATE', 53, 19, 0, 2000),
	Insn('CAM_DISTANCE', 25000, 2000),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (200, 0, 4000), 2000, 0),
	]),
	Insn('SLEEP', 200),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (1500, 0, 4500), 2000, 0),
	]),
	Insn('SLEEP', 80),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (-100, 0, 5100), 2000, 0),
	]),
	Insn('SLEEP', 120),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (1200, 0, 5600), 2000, 0),
	]),
	Insn('0x6F', b'y'),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'\x08\x02\x00'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('TEXT_MESSAGE', Char(16), Text(
		'#13400927V嘿嘿……你们好。{wait}'
		'{page}'
		'#13400928V突然来访，真是抱歉哦。\n'
		'也没事先联系一下……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(1), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('TEXT_MESSAGE', Char(17), Text(
		'#13400929V我知道打扰各位了，\n'
		'但是，有件事情急着要确认……{wait}'
		'{page}'
		'#13400930V能不能占用各位一点时间呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(1), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 0))),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400931V#0000F#5P这个倒是没问题……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400932V#5P#0305F到底是什么事情呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400933V#5P#0201F是关于\n'
		'『黑之拍卖会#10RSchwarz Auction#』吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'#13400934V#12P#0806F啊～那件事\n'
		'就先不用去管啦……{wait}'
		'{page}'
		'#13400935V#0801F……更、更重要的是……{wait}'
		'{page}'
		'#13400936V我们获取了一份目击情报，\n'
		'据说罗伊德今天下午\n'
		'曾和某个人物一起行动……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400937V#0005F#5P某个人物……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(17), Text(
		'#13400938V#12P#0903F……是一个紫色头发的女孩子。{wait}'
		'{page}'
		'#13400939V#0901F我想，应该\n'
		'还穿着白裙子……{wait}'
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
		'#13400940V#0011F#5P哎，这个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400941V#5P#0101F是说蕾恩吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(16), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(17), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('0x82', 100, 0, 3000, 200),
	Insn('TEXT_TALK', Char(16), Text(
		'#13400942V#12P#0813F#4S啊！！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(17), Text(
		'#13400943V#12P#0901F果然是……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400944V#0011F#5P稍、稍微等一下。{wait}'
		'{page}'
		'#13400945V#0001F那孩子……\n'
		'原来和你们有关系吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(17), Text(
		'#13400946V#12P#0903F嗯……是的。{wait}'
		'{page}'
		'#13400947V#0908F虽然我们也有好几个月\n'
		'都没见到她了……{wait}'
		'{page}'
		'#13400948V#0902F不过……\n'
		'她果然还在克洛斯贝尔啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'#13400949V#12P#0809F#40W……啊、啊哈哈…………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('CHAR_FLAG1_SET', Char(16), 32),
	Insn('CHAR_FLAG1_SET', Char(16), 2),
	Insn('CHAR_SET_CHCP', Char(16), 35),
	Insn('CHAR_SET_FRAME', Char(16), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('SLEEP', 130),
	Insn('CHAR_SET_FRAME', Char(16), 1),
	Insn('SLEEP', 130),
	Insn('CHAR_SET_FRAME', Char(16), 2),
	Insn('SLEEP', 200),
	Insn('EMOTE', Char(17), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_WATCH', Char(17), Char(16), 500),
	Insn('TEXT_TALK', Char(17), Text(
		'#13400950V#0901F#11P艾丝蒂尔……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 200),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_FRAME', Char(16), 3),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(16), Text(
		'#13400951V#12P#0806F没、没关系……\n'
		'一放下心来，就有些全身脱力……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('SLEEP', 200),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(16), 32),
	Insn('CHAR_FLAG1_UNSET', Char(16), 2),
	Insn('CHAR_SET_CHCP', Char(16), 34),
	Insn('CHAR_SET_FRAME', Char(16), 0),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(16), Text(
		'#13400952V#12P#0804F好……！\n'
		'既然如此，我就不客气了～！{wait}'
		'{page}'
		'#13400953V#0802F已经彻底锁定目标，\n'
		'这次绝对要抓到她！{wait}'
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
	Insn('TEXT_TALK', Char(260), Text(
		'#13400954V#5P#0302F喂喂，\n'
		'那个小姑娘好受欢迎啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400955V#5P#0204F约纳好像也对她很执着……\n'
		'还真不是一般地受欢迎呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400956V#0006F#5P那个……那孩子\n'
		'该不会是游击士吧？{wait}'
		'{page}'
		'#13400957V#0001F她的年纪太小了……\n'
		'而且好像也做过不少危险的事。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(17), 0, 500),
	Insn('TEXT_TALK', Char(17), Text(
		'#13400958V#12P#0904F嗯……她的确不是游击士。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'#13400959V#12P#0804F不过，对我们来说，\n'
		'她可是如同家人一般重要的孩子哦。{wait}'
		'{page}'
		'#13400960V#0800F这大半年来……\n'
		'我们一直在寻找她。{wait}'
		'{page}'
		'#13400961V为了抓住那孩子……\n'
		'让她成为我们的『家人』。{wait}'
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
		'#13400962V#0005F#5P家、家人……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400963V#5P#0101F这个……\n'
		'似乎有很多隐情呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'#13400964V#12P#0806F那是自然啊……\n'
		'事情相当错综复杂呢。{wait}'
		'{page}'
		'#13400965V#0808F#30W……来到克洛斯贝尔之后，\n'
		'我们也查清了不少事……{wait}'
		'{page}'
		'#13400966V#40W……………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(17), Char(16), 500),
	Insn('TEXT_TALK', Char(17), Text(
		'#13400967V#0906F#11P唉，你可不能\n'
		'自己在那里沮丧啊。{wait}'
		'{page}'
		'#13400968V#0900F我们不是收集了海瓦兹夫妇的情报，\n'
		'准备让那孩子敞开心扉的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(16), Char(17), 500),
	Insn('TEXT_TALK', Char(16), Text(
		'#13400969V#6P#0800F嗯、嗯……是呀！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400970V#0001F#5P海瓦兹夫妇……\n'
		'是指哈罗德先生他们吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(16), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(17), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 16, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK', 17, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 500),
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_TALK', Char(16), Text(
		'#13400971V#12P#0813F咦咦咦！？{wait}'
		'{page}'
		'#13400972V为什么你们会知道\n'
		'这个名字啊！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400973V#0012F#5P这个，其实\n'
		'我也正想问这句呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400974V#5P#0106F……看来，还是把今天发生的事情\n'
		'从头到尾说明一下比较好呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 24500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (5500, 950, 4200), 0),
	Insn('CAM_ROTATE', 49, 17, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 22500, 0),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_FLAG1_SET', Char(16), 32),
	Insn('CHAR_FLAG1_SET', Char(16), 2),
	Insn('CHAR_FLAG1_UNSET', Char(16), 1),
	Insn('CHAR_SET_CHCP', Char(16), 35),
	Insn('CHAR_SET_FRAME', Char(16), 14),
	Insn('FORK_FUNC', Char(16), 3, Function((0, 25))),
	Insn('CHAR_FLAG1_SET', Char(17), 32),
	Insn('CHAR_FLAG1_SET', Char(17), 2),
	Insn('CHAR_FLAG1_UNSET', Char(17), 1),
	Insn('CHAR_SET_CHCP', Char(17), 37),
	Insn('CHAR_SET_FRAME', Char(17), 0),
	Insn('CHAR_SET_POS', Char(257), (5000, 130, 2200), 0),
	Insn('CHAR_SET_POS', Char(258), (6000, 130, 2200), 0),
	Insn('CHAR_SET_POS', Char(259), (3300, 0, 2500), 45),
	Insn('CHAR_SET_POS', Char(260), (7000, 0, 3500), 315),
	Insn('CHAR_SET_POS', Char(16), (5000, 130, 6250), 180),
	Insn('CHAR_SET_POS', Char(17), (5800, 130, 6250), 180),
	Insn('CAM_DISTANCE', 23000, 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('CAM_ROTATE', 37, 17, 0, 50000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400975V#12P#0003F──事情就是这样，\n'
		'那个孩子刚刚回去，\n'
		'正好和你们错过了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400976V#12P#0011F等、等一下，艾丝蒂尔！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'#13400977V#5P#0808F#60W啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(17), 1),
	Insn('FORK_QUIT', Char(16), 3),
	Insn('CHAR_SET_FRAME', Char(16), 14),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(16), 5),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(16), 6),
	Insn('SLEEP', 100),
	Insn('FORK_FUNC', Char(16), 3, Function((0, 26))),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(16), Text(
		'#13400978V#5P#0811F#50W讨、讨厌……\n'
		'……怎么会这样……{wait}'
		'{page}'
		'#13400979V#0810F#60W呜……呜……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('FORK_QUIT', Char(16), 3),
	Insn('CHAR_SET_FRAME', Char(16), 11),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('FORK', 16, 2, [
		Insn('0xA6', Char(254), 0, 20, 1000, 3000),
	]),
	Insn('0x82', 200, 0, 3000, 800),
	Insn('TEXT_TALK', Char(16), Text(
		'#13400980V#0810F#5P……呜呜……\n'
		'哇啊啊啊啊啊啊啊……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('CHAR_SET_FRAME', Char(17), 2),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_FRAME', Char(17), 3),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_FRAME', Char(17), 4),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_FRAME', Char(17), 5),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(17), Text(
		'#13400981V#11P#0910F#40W艾丝蒂尔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(16), Text(
		'#13400982V#5P#0810F#40W对、对不起啊，约书亚……\n'
		'……还有罗伊德和大家……{wait}'
		'{page}'
		'#13400983V#40W可是我……\n'
		'不知道该说什么好……{wait}'
		'{page}'
		'#13400984V#0808F#40W……她并不是被抛弃的……\n'
		'是被爸爸妈妈爱着的……{wait}'
		'{page}'
		'#13400985V#40W那孩子终于……\n'
		'可以敞开心扉……去面对这痛苦悲哀……\n'
		'……而又温暖的事实了……{wait}'
		'{page}'
		'#13400986V#0810F#40W………呜呜呜…………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400987V#12P#0108F痛苦悲哀，而又温暖的事实……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400988V#12P#0008F就是哈罗德先生他们所说的往事吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_TALK', Char(17), Text(
		'#13400989V#5P#0908F──在这其中，曾出现过数次\n'
		'悲哀的偶然与误解。{wait}'
		'{page}'
		'#13400990V其结果……\n'
		'就是让那个经历过残酷地狱的孩子\n'
		'开始欺骗自己。{wait}'
		'{page}'
		'#13400991V#0903F她制造出虚假的双亲──帕蒂尔丄玛蒂尔，\n'
		'而放弃去寻找真相。{wait}'
		'{page}'
		'#13400992V可是……这也不能怪她。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400993V#0306F……原来如此，正因为年幼，\n'
		'所以只能用这种方式来进行自我保护吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400994V#6P#0208F可是……\n'
		'这样是无法前进的。{wait}'
		'{page}'
		'#13400995V#0206F别说前进……\n'
		'就连真正的归所也回不去。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(17), Text(
		'#13400996V#5P#0908F嗯……{wait}'
		'{page}'
		'#13400997V#0903F所以我们打算\n'
		'帮助她燃起\n'
		'面对真相的勇气。{wait}'
		'{page}'
		'#13400998V因为，根据我们的调查得知，真相虽然悲哀，\n'
		'但其中依然包含着真实的亲情……{wait}'
		'{page}'
		'#13400999V所以，我们觉得……\n'
		'现在的她，一定能克服自己的过去。{wait}'
		'{page}'
		'#13401000V#0902F不过……\n'
		'看来已经没有这个必要了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13401001V#12P#0004F……嗯。{wait}'
		'{page}'
		'#13401002V#0000F至少，她看上去\n'
		'好像已经完全理解了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(17), Text(
		'#13401003V#5P#0911F是吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_FRAME', Char(17), 0),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(17), Text(
		'#13401004V#0903F#5P谢谢你，罗伊德，\n'
		'还有支援课的各位。{wait}'
		'{page}'
		'#13401005V真不知该如何感谢你们……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13401006V#12P#0004F哈哈……不必放在心上。{wait}'
		'{page}'
		'#13401007V#0002F这应该算是顺水推舟吧，\n'
		'而且那孩子也帮了我们很多忙呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13401008V#12P#0104F呵呵……的确是哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'#13401009V#5P#0810F呜……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_FRAME', Char(16), 20),
	Insn('0x0D'),
	Insn('CHAR_SET_FRAME', Char(16), 21),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(16), 22),
	Insn('SLEEP', 200),
	Insn('CHAR_SET_FRAME', Char(16), 21),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(16), 12),
	Insn('SLEEP', 500),
	Insn('0x82', 100, 0, 3000, 500),
	Insn('TEXT_TALK', Char(16), Text(
		'#13401010V#5P#0800F#4S──嗯，决定了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(17), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(17), 1),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_FRAME', Char(16), 13),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(16), Text(
		'#13401011V#5P#0802F既然最大的障碍已经消失了，\n'
		'我就再也不会跟她客气了！{wait}'
		'{page}'
		'#13401012V#0809F你看着吧～蕾恩！{wait}'
		'{page}'
		'#13401013V我绝对会继续铲平障碍，\n'
		'让你成为我们家的一份子！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(17), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13401014V#12P#0009F哈哈……好厉害的气势啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13401015V#0309F#12P哎呀～虽然不太明白状况，\n'
		'不过，这才是艾丝蒂尔啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13401016V#6P#0202F该怎么说呢……真是太耀眼了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(17), Text(
		'#13401017V#11P#0904F呵呵，热情值得肯定。{wait}'
		'{page}'
		'#13401018V#0902F再没有什么能比鼓足干劲的\n'
		'艾丝蒂尔更可怕了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'#13401019V#5P#0804F哼哼，一切都包在我的身上吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_FRAME', Char(16), 4),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(16), Text(
		'#13401020V#5P#0800F──罗伊德先生、艾莉小姐，\n'
		'还有小缇欧和兰迪先生。{wait}'
		'{page}'
		'#13401021V也请允许我郑重\n'
		'向你们道谢。{wait}'
		'{page}'
		'#13401022V#0804F真是太谢谢你们了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}艾丝蒂尔深深低下了头。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13401023V#12P#0002F艾丝蒂尔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13401024V#12P#0102F……艾丝蒂尔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(17), 0),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(17), Text(
		'#13401025V#5P#0904F今后如果需要我们帮忙，\n'
		'请不要客气，随时告诉我们。{wait}'
		'{page}'
		'#13401026V#0902F我们之间，应该没必要在意\n'
		'警察与游击士的芥蒂了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'#13401027V#5P#0809F嗯嗯！\n'
		'我们会尽全力协助你们的！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13401028V#12P#0004F哈哈……明白了。{wait}'
		'{page}'
		'#13401029V#0000F万一发生了紧急状况，\n'
		'我们肯定会向你们求助的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 23500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('SLEEP', 800),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}其后，罗伊德与艾丝蒂尔等人\n'
		'来到东侧大道的『龙老饭店』，\n'
		'共进了晚餐，彼此的关系变得更加融洽了。{wait}'
		'{page}'
		'关于发生在两人的故乡──『利贝尔王国』的\n'
		'『异变』真相及其始末……{wait}'
		'{page}'
		'以及蕾恩所属的，\n'
		'名为『结社』的神秘组织……{wait}'
		'{page}'
		'各种惊天动地的情报接踵而至，\n'
		'而纪念庆典第四天的夜色也渐渐深了。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 1000),
	Insn('SOUND_PLAY', 13, 0, 0, 100),
	Insn('SLEEP', 4000),
	Insn('MINIGAME', 24, 0, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
	Insn('OBJ_FLAG_SET', Object(2), 16),
	Insn('IMG_0xC9', (ResId(2), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
	Insn('SLEEP', 2000),
	Insn('IMG_0xC9', (ResId(2), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
	Insn('CHAR_FLAG1_SET', Char(16), 128),
	Insn('CHAR_FLAG2_SET', Char(16), 32768),
	Insn('CHAR_FLAG1_SET', Char(17), 128),
	Insn('CHAR_FLAG2_SET', Char(17), 32768),
	Insn('0x2F', b'_\x00'),
	Insn('CHAR_FLAG1_UNSET', Char(257), 4),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_FLAG1_UNSET', Char(258), 4),
	Insn('CHAR_SET_CHCP', Char(258), 255),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_FLAG1_UNSET', Char(259), 4),
	Insn('CHAR_SET_CHCP', Char(259), 255),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_FLAG1_UNSET', Char(260), 4),
	Insn('CHAR_SET_CHCP', Char(260), 255),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0xD5', 33),
	Insn('0xD5', 34),
	Insn('0xD5', 35),
	Insn('0xD5', 36),
	Insn('0xD5', 37),
	Insn('0xD5', 38),
	Insn('ITEM_REMOVE', 807, 1),
	Insn('ITEM_REMOVE', 808, 1),
	Insn('CALL', Function((0, 11))),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_ANIMATION', Char(254), 1000, [
			14,
			15,
			16,
		]),
	]),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_ANIMATION', Char(254), 1000, [
			6,
			7,
			8,
			9,
		]),
	]),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (8000, 0, 62700), 4000, 1),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (700, 0, 62700), 4000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('CHAR_ROTATE', Char(257), 315, 500),
	Insn('RETURN'),
]

data['code'][28] = [
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (8000, 0, 62700), 4000, 1),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (700, 0, 61500), 4000, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('CHAR_ROTATE', Char(258), 315, 500),
	Insn('RETURN'),
]

data['code'][29] = [
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (8000, 0, 62700), 4000, 1),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (2000, 0, 62700), 4000, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('CHAR_ROTATE', Char(259), 315, 500),
	Insn('RETURN'),
]

data['code'][30] = [
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (8000, 0, 62700), 4000, 1),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (2000, 0, 61500), 4000, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('CHAR_ROTATE', Char(260), 315, 500),
	Insn('RETURN'),
]

data['code'][31] = [
	Insn('FORK', 352, 1, [
		Insn('0x95', Char(254), (-700, 0, 62700), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(352), 1),
	Insn('FORK', 352, 1, [
		Insn('0x95', Char(254), (-2200, 0, 67900), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(352), 1),
	Insn('FORK', 352, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('FORK', 352, 1, [
		Insn('0x95', Char(254), (-5000, 0, 67900), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(352), 1),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('FORK_AWAIT', Char(352), 2),
	Insn('RETURN'),
]

data['code'][32] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (64000, 1100, 8600), 0),
	Insn('CAM_ROTATE', 50, 17, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(257), (63000, 0, 6700), 0),
	Insn('CHAR_SET_POS', Char(258), (64300, 0, 6700), 0),
	Insn('CHAR_SET_POS', Char(259), (63200, 0, 5400), 0),
	Insn('CHAR_SET_POS', Char(260), (64500, 0, 5400), 0),
	Insn('CHAR_SET_POS', Char(8), (64000, 150, 11400), 180),
	Insn('CHAR_SET_CHCP', Char(8), 1),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu01000.itp'),
	Insn('IMG_LOAD', ResId(1), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis156.itp'),
	Insn('MINIGAME', 24, 0, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
	Insn('SLEEP', 1000),
	Insn('0xC7', b'\x00\x00\x08\x00\x00'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{0x18}{color 0}#1K创立纪念庆典\u3000第二天{wait}'
	)),
	Insn('SLEEP', 2500),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0xC7', b'\x01\x00\x08\x00\x00'),
	Insn('BGM_PLAY', b'n\x00\x00'),
	Insn('CAM_DISTANCE', 24000, 1500),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('TEXT_MESSAGE', Char(8), Text(
		'#13200001V──好了，你们几个，\n'
		'假期过得开心吗？{wait}'
		'{page}'
		'#13200002V说是代价也许有点不合适吧，不过，\n'
		'从今天开始，到最终日的四天之内……{wait}'
		'{page}'
		'#13200003V你们可要鼓足干劲，拼命工作，\n'
		'拜托了哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(257), Text(
		'#13200004V#12P#0006F呼……明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13200005V#0306F话说，五天的纪念庆典，\n'
		'居然只有第一天放假……{wait}'
		'{page}'
		'#13200006V#0301F这未免也太小气了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13200007V#0106F算了，这也正能说明\n'
		'警察局上下都很忙吧。{wait}'
		'{page}'
		'#13200008V#0100F警备和巡逻工作，在庆典的第一天\n'
		'应该是最忙的吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13200009V#5P#1004F嗯，就是这么回事。{wait}'
		'{page}'
		'#13200010V#1002F所以，给你们放假姑且算是\n'
		'将暗杀市长事件防范于未然的褒奖吧。{wait}'
		'{page}'
		'#13200011V而且总部似乎也不打算在纪念庆典期间\n'
		'把杂务扔给你们哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13200012V#12P#0006F相对地，支援请求\n'
		'倒是发来了不少呢。{wait}'
		'{page}'
		'#13200013V#0000F游客好像也比平时多了好几倍呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13200014V#5P#1002F哼哼，你们好不容易\n'
		'打出名声，人气差不多也快接近\n'
		'游击士的脚跟了。{wait}'
		'{page}'
		'#13200015V不趁现在努力的话，更待何时？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13200016V#12P#0002F嗯，这倒是。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13200017V#0306F我怎么觉得，好像是被\n'
		'巧妙地哄骗了过去……{wait}'
		'{page}'
		'#13200018V#0308F唉，其实我好想和\n'
		'那些护理师妹妹一起去\n'
		'『米修拉姆』玩啊～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(259), Char(260), 500),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(259), Text(
		'#13200019V#6P#0205F说到『米修拉姆』……\n'
		'是从港湾区乘游览船\n'
		'就能抵达的那个主题乐园吧？{wait}'
		'{page}'
		'#13200020V#0202F听说『咪西』\n'
		'是那里的吉祥物……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_WATCH', Char(258), Char(260), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#13200021V#5P#0005F『咪西』……\n'
		'啊，是那个猫咪吉祥物啊。{wait}'
		'{page}'
		'#13200022V#0000F那个造型，我以前见过。\n'
		'不过，主题乐园这种东西，\n'
		'在三年前应该还没有吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13200023V#5P#0104F『米修拉姆』本身\n'
		'一直以游憩区而著称……{wait}'
		'{page}'
		'#13200024V#0102F至于主题乐园那边，\n'
		'应该是在两年多之前建成的吧。{wait}'
		'{page}'
		'#13200025V自那以来，似乎就十分受欢迎呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13200026V#0309F嗯，我以前也去过一次，\n'
		'那里可真是相当壮观呢。{wait}'
		'{page}'
		'#13200027V#0302F不过，那里的游客平时就络绎不绝，\n'
		'在纪念庆典期间肯定就更加拥挤了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13200028V#6P#0204F原来如此……\n'
		'我也有一点兴趣呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13200029V#5P#1003F……………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_ROTATE', Char(259), 0, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#13200030V#12P#0005F……课长？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13200031V#5P#1005F哦，嗯……{wait}'
		'{page}'
		'#13200032V#1003F总而言之，到最终日为止的四天之内，\n'
		'你们只要专心解决支援请求就好了。{wait}'
		'{page}'
		'#13200033V#1002F嗯，至于具体该怎么做，\n'
		'就和以前一样，由你们自己判断。{wait}'
		'{page}'
		'#13200034V支援请求应该会每天更新，\n'
		'好好期待吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 24500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('0xE3', 10),
	Insn('SLEEP', 1000),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 800, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('TEXT_RESET', b'\x03'),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 800, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('0xE3', 11),
	Insn('CAM_OFFSET', (18000, 1850, 3500), 0),
	Insn('CAM_ROTATE', 37, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(257), (19000, 850, 3500), 270),
	Insn('CHAR_SET_POS', Char(258), (19000, 850, 3500), 270),
	Insn('CHAR_SET_POS', Char(259), (19000, 850, 3500), 270),
	Insn('CHAR_SET_POS', Char(260), (19000, 850, 3500), 270),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('BGM_PLAY', b'j\x00\x00'),
	Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 106), Insn('SET'), Insn('END')])),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('OBJ_FLAG_UNSET', Object(0), 16),
	Insn('0x71', Object(0), b'\x00\x00', 5, 0),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('0x79', b'\x00\x00'),
	Insn('CAM_OFFSET', (16000, 1850, 3500), 2000),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (16000, 850, 2900), 2000, 0),
	]),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 250),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (16000, 850, 4200), 2000, 0),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 400),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (17300, 850, 2900), 2000, 0),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 250),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (17300, 0, 4200), 2000, 0),
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
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('0x71', Object(0), b'\x05\x00', 0, 0),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('0x79', b'\x00\x00'),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 315, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('OBJ_FLAG_SET', Object(0), 16),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13200035V#6P#0004F#6P好吧……总之，\n'
		'先去确认一下终端上的支援请求吧。{wait}'
		'{page}'
		'#13200036V#0000F视情况，\n'
		'说不定还有必要前往\n'
		'克洛斯贝尔市外呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13200037V#0103F#5P嗯，是呀。{wait}'
		'{page}'
		'#13200038V#0100F最近去阿尔摩利卡村\n'
		'那边观光的人\n'
		'似乎也有不少……{wait}'
		'{page}'
		'#13200039V除了铁道和飞行船之外，\n'
		'好像还有从陆路来的游客呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13200040V#5P#0305F也就是说，东西国境门的\n'
		'客流量也会比平时多啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13200041V#0203F……诺艾儿上士他们\n'
		'在纪念庆典期间肯定也很辛苦吧。{wait}'
		'{page}'
		'#13200042V#0200F游击士们就\n'
		'更不用说了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13200043V#6P#0001F嗯，\n'
		'我们也不能认输啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13200044V#0104F#5P不过，要是绷得太紧，\n'
		'我们的体力也会撑不住吧。{wait}'
		'{page}'
		'#13200045V#0102F先确认一下委托的紧急程度，\n'
		'安排好之后再处理会比较好吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13200046V#6P#0000F这倒也是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13200047V#5P#0300F好啦，一件件认真解决吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('CAM_OFFSET', (16600, 1850, 3500), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 340, 0),
	Insn('CAM_DISTANCE', 27500, 0),
	Insn('CHAR_SET_POS', Char(0), (16600, 850, 3500), 0),
	Insn('CHAR_SET_POS', Char(1), (16600, 850, 3500), 0),
	Insn('CHAR_SET_POS', Char(2), (16600, 850, 3500), 0),
	Insn('CHAR_SET_POS', Char(3), (16600, 850, 3500), 0),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('FLAG_SET', Flag(1280)),
	Insn('QUEST', 67, Insn('TASK_SET', 14)),
	Insn('QUEST', 68, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 68, Insn('TASK_SET', 0)),
	Insn('0xB5', b'\x01\x00\x80\x00'),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][33] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_ANIMATION', Char(259), 1500, [
			0,
			1,
			2,
			1,
		]),
	]),
	Insn('RETURN'),
]

data['code'][34] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_ANIMATION', Char(259), 3000, [
			0,
			1,
			2,
			3,
		]),
	]),
	Insn('RETURN'),
]

data['code'][35] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 0, 0),
		Insn('SLEEP', 300),
		Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 0, 0),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][36] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('IMG_LOAD', ResId(0), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis068.itp'),
	Insn('IMG_LOAD', ResId(1), 289, 127, b'a\x01\xbf\x00\x00\x00\x00\x00@\x00@\x00\x00\x00\x00\x00@\x00@\x00\xff\xff\xff\x00\x01', 'c_vis069.itp'),
	Insn('EFF_LOAD', ResId(0), 'event\\ev398_00.eff'),
	Insn('CAM_OFFSET', (190000, 10000, 111000), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 340, 0),
	Insn('CAM_DISTANCE', 1000, 0),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_SET_POS', Char(259), (206000, 50, 127000), 180),
	Insn('LOAD_CHCP', 'chr/ch02707', 31),
	Insn('CHAR_SET_CHCP', Char(18), 31),
	Insn('CHAR_SET_FRAME', Char(18), 0),
	Insn('CHAR_FLAG1_SET', Char(18), 0),
	Insn('CHAR_SET_POS', Char(18), (206000, 0, 127100), 180),
	Insn('FORK_FUNC', Char(18), 0, Function((0, 0))),
	Insn('CHAR_FLAG1_UNSET', Char(18), 128),
	Insn('CHAR_FLAG2_UNSET', Char(18), 32768),
	Insn('CHAR_FLAG1_SET', Char(18), 32768),
	Insn('LOAD_CHCP', 'apl/ch50302', 30),
	Insn('CHAR_SET_CHCP', Char(259), 30),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_FLAG1_SET', Char(259), 2),
	Insn('OBJ_FLAG_UNSET', Object(11), 4),
	Insn('0x78', b'\x0b', Char(31)),
	Insn('CHAR_SET_POS', Char(31), (206000, 500, 126300), 0),
	Insn('0xD3', Char(31), 0, 180000, 0, 0),
	Insn('0xE5'),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('FORK_FUNC', Char(259), 0, Function((0, 33))),
	Insn('FORK_FUNC', Char(32), 1, Function((0, 37))),
	Insn('EMOTE', Char(259), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 2500),
	Insn('CAM_OFFSET', (190000, 10000, 108000), 1000),
	Insn('EMOTE_STOP', Char(259)),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 1000, 0),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(259), 2, Function((0, 35))),
	Insn('SLEEP', 3000),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0x00000000), 0, 0),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFF000000), 500, 0),
	Insn('FADE_ON', 0, Color(0xFFFFFFFF), 0),
	Insn('FADE_ON', 500, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('BGM_SET_VOLUME', b'<\xf4\x01\x00\x00'),
	Insn('FADE_OFF', 0, Color(0x00000000)),
	Insn('0xB6', 0, 'ed7_ev06.pmf', 65640),
	Insn('SOUND_PLAY', 725, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_RESET', b'\x02'),
	Insn('0xB6', 1, '', 0),
	Insn('BGM_SET_VOLUME', b'd\xf4\x01\x00\x00'),
	Insn('FADE_OFF', 0, Color(0xFFFFFFFF)),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('FORK_QUIT', Char(259), 255),
	Insn('FORK_QUIT', Char(32), 1),
	Insn('0x6E', 280, 3000),
	Insn('CHAR_ANIMATION', Char(259), 1500, [
		0,
		3,
		4,
		5,
	]),
	Insn('CHAR_ANIMATION', Char(259), 1500, [
		5,
		6,
		7,
		6,
	]),
	Insn('CHAR_ANIMATION', Char(259), 1500, [
		5,
		4,
		3,
		0,
	]),
	Insn('FORK_FUNC', Char(259), 2, Function((0, 35))),
	Insn('EFF_PLAY', (ResId(0), 0), Char(259), 0, 0, 0, 4928, 2, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('SOUND_PLAY', 1199, 0, 255, 100),
	Insn('SOUND_PLAY', 506, 0, 0, 100),
	Insn('SOUND_PLAY', 565, 0, 0, 100),
	Insn('SLEEP', 2000),
	Insn('FORK_FUNC', Char(259), 0, Function((0, 34))),
	Insn('FORK_FUNC', Char(32), 1, Function((0, 38))),
	Insn('SLEEP', 1500),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 0, 0),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFF000000), 500, 0),
	Insn('FADE_ON', 0, Color(0xFFFFFFFF), 0),
	Insn('FADE_ON', 500, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 0, 0),
	Insn('CAM_OFFSET', (190000, 10000, 111000), 0),
	Insn('0x6E', 350, 0),
	Insn('EFF_STOP', (ResId(0), 0)),
	Insn('BGM_SET_VOLUME', b'<\xf4\x01\x00\x00'),
	Insn('FADE_OFF', 0, Color(0x00000000)),
	Insn('0xB6', 0, 'ed7_ev07.pmf', 65640),
	Insn('SOUND_PLAY', 726, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_RESET', b'\x02'),
	Insn('0xB6', 1, '', 0),
	Insn('BGM_SET_VOLUME', b'd\xf4\x01\x00\x00'),
	Insn('FADE_OFF', 0, Color(0xFFFFFFFF)),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 1282, 0, 255, 90),
	Insn('FORK_QUIT', Char(32), 1),
	Insn('FORK_QUIT', Char(259), 255),
	Insn('CHAR_ANIMATION', Char(259), 1000, [
		0,
		3,
		4,
		5,
	]),
	Insn('EMOTE', Char(259), 0, 1700, (8, 9, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('SLEEP', 2000),
	Insn('0x6E', 360, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_FLAG1_UNSET', Char(259), 4),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xE6'),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'c0570', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][37] = [
	Insn('SOUND_PLAY', 849, 0, 0, 100),
	Insn('SLEEP', 900),
	Insn('SOUND_PLAY', 850, 0, 0, 100),
	Insn('SLEEP', 1800),
	Insn('SOUND_PLAY', 849, 0, 0, 100),
	Insn('SLEEP', 900),
	Insn('SOUND_PLAY', 850, 0, 0, 100),
	Insn('SLEEP', 1800),
	Insn('SOUND_PLAY', 849, 0, 0, 100),
	Insn('RETURN'),
]

data['code'][38] = [
	Insn('SOUND_PLAY', 849, 0, 0, 100),
	Insn('SLEEP', 200),
	Insn('SOUND_PLAY', 850, 0, 0, 100),
	Insn('SLEEP', 700),
	Insn('SOUND_PLAY', 849, 0, 0, 100),
	Insn('RETURN'),
]

data['code'][39] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50011', 30),
	Insn('SOUND_LOAD', 806),
	Insn('CAM_OFFSET', (1000, 900, 1900), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25500, 0),
	Insn('CHAR_SET_POS', Char(257), (400, 0, 1900), 0),
	Insn('CHAR_SET_POS', Char(258), (1600, 0, 1900), 0),
	Insn('CHAR_SET_POS', Char(259), (400, 0, 700), 0),
	Insn('CHAR_SET_POS', Char(260), (1600, 0, 700), 0),
	Insn('IMG_LOAD', ResId(0), 180, 0, b'\xb4\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis007.itp'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 806, 0, 2, 100),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_WATCH', Char(260), Char(257), 500),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_SET', Char(257), 32),
	Insn('CHAR_FLAG1_SET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('CHAR_SET_FRAME', Char(257), 3),
	Insn('SOUND_STOP', 806),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('FADE_ON', 500, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('SOUND_PLAY', 1084, 0, 255, 90),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#13400126V#0000F您好，这里是罗伊德。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('芙兰的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400127V抱歉，百忙之中打扰了哦。\n'
		'现在方便吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#13400128V#0000F嗯……\n'
		'工作刚刚告一段落，\n'
		'应该没问题。{wait}'
		'{page}'
		'#13400129V总部有紧急任务吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('芙兰的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400130V不，是有位先生希望与你们\n'
		'当面商量委托事宜。{wait}'
		'{page}'
		'#13400131V他是位贸易商，\n'
		'名叫哈罗德……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#13400132V#0005F啊，我们认识……\n'
		'究竟是什么事呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('芙兰的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400133V这个……{wait}'
		'{page}'
		'#13400134V好像是在观看市内游行的时候，\n'
		'他的孩子走失了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#13400135V#0003F是吗，明白了。{wait}'
		'{page}'
		'#13400136V#0001F我们要去哪里和他见面呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('芙兰的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400137V就在警察局总部附近，\n'
		'喷泉前面的长椅那里。{wait}'
		'{page}'
		'#13400138V孩子似乎就是在那附近\n'
		'走失的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#13400139V#0000F明白了，我们立刻赶去看看。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('芙兰的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400140V好的，麻烦各位了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'{color 0}#13400141V#11P#0105F怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(257), 32),
	Insn('CHAR_FLAG1_UNSET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x0D'),
	Insn('CHAR_WATCH', Char(257), Char(258), 500),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400142V#6P#0003F啊，贸易商哈罗德先生\n'
		'有事要委托我们。{wait}'
		'{page}'
		'#13400143V#0001F说是在看游行的时候，\n'
		'他的孩子走失了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400144V#11P#0101F这……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400145V#12P#0206F今天这么多人，\n'
		'走散了可真是不得了啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400146V#0300F#11P这么说，也就是庆典时期的\n'
		'惯例任务──寻找走失的小孩吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(260), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400147V#5P#0004F嗯，多半是。{wait}'
		'{page}'
		'#13400148V#0000F说是在警察局总部附近的\n'
		'喷泉前等我们，\n'
		'总之，先去问问情况吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('CHAR_SET_POS', Char(0), (1000, 0, 1900), 0),
	Insn('0x0A', 268435456),
	Insn('FLAG_SET', Flag(1293)),
	Insn('QUEST', 68, Insn('TASK_SET', 7)),
	Insn('SOUND_STOP', 806),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][40] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50011', 30),
	Insn('SOUND_LOAD', 806),
	Insn('CAM_OFFSET', (1300, 1950, 9900), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25500, 0),
	Insn('CHAR_SET_POS', Char(257), (1900, 850, 9900), 180),
	Insn('CHAR_SET_POS', Char(258), (700, 850, 9900), 180),
	Insn('CHAR_SET_POS', Char(259), (700, 850, 11100), 180),
	Insn('CHAR_SET_POS', Char(260), (1900, 850, 11100), 180),
	Insn('IMG_LOAD', ResId(0), 180, 0, b'\xb4\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis007.itp'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 806, 0, 2, 100),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_WATCH', Char(259), Char(257), 500),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_SET', Char(257), 32),
	Insn('CHAR_FLAG1_SET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 6),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('CHAR_SET_FRAME', Char(257), 7),
	Insn('SOUND_STOP', 806),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('FADE_ON', 500, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('SOUND_PLAY', 1084, 0, 255, 90),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#13400126V#0000F您好，这里是罗伊德。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('芙兰的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400127V抱歉，百忙之中打扰了哦。\n'
		'现在方便吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#13400128V#0000F嗯……\n'
		'工作刚刚告一段落，\n'
		'应该没问题。{wait}'
		'{page}'
		'#13400129V总部有紧急任务吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('芙兰的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400130V不，是有位先生希望与你们\n'
		'当面商量委托事宜。{wait}'
		'{page}'
		'#13400131V他是位贸易商，\n'
		'名叫哈罗德……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#13400132V#0005F啊，我们认识……\n'
		'究竟是什么事呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('芙兰的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400133V这个……{wait}'
		'{page}'
		'#13400134V好像是在观看市内游行的时候，\n'
		'他的孩子走失了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#13400135V#0003F是吗，明白了。{wait}'
		'{page}'
		'#13400136V#0001F我们要去哪里和他见面呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('芙兰的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400137V就在警察局总部附近，\n'
		'喷泉前面的长椅那里。{wait}'
		'{page}'
		'#13400138V孩子似乎就是在那附近\n'
		'走失的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#13400139V#0000F明白了，我们立刻赶去看看。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('芙兰的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400140V好的，麻烦各位了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('CHAR_SET_FRAME', Char(257), 6),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'{color 0}#13400141V#6P#0105F怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(257), 32),
	Insn('CHAR_FLAG1_UNSET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x0D'),
	Insn('CHAR_WATCH', Char(257), Char(258), 500),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400142V#11P#0003F啊，贸易商哈罗德先生\n'
		'有事要委托我们。{wait}'
		'{page}'
		'#13400143V#0001F说是在看游行的时候，\n'
		'他的孩子走失了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#13400144V#6P#0101F这……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13400145V#5P#0206F今天这么多人，\n'
		'走散了可真是不得了啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13400146V#0300F#5P这么说，也就是庆典时期的\n'
		'惯例任务──寻找走失的小孩吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(260), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400147V#12P#0004F嗯，多半是。{wait}'
		'{page}'
		'#13400148V#0000F说是在警察局总部附近的\n'
		'喷泉前等我们，\n'
		'总之，先去问问情况吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('CHAR_SET_POS', Char(0), (1300, 850, 9900), 180),
	Insn('0x0A', 268435456),
	Insn('FLAG_SET', Flag(1293)),
	Insn('QUEST', 68, Insn('TASK_SET', 7)),
	Insn('SOUND_STOP', 806),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][41] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (15760, 1850, 10150), 0),
	Insn('CAM_ROTATE', 79, 22, 0, 0),
	Insn('0x6E', 340, 0),
	Insn('CAM_DISTANCE', 22000, 0),
	Insn('CHAR_SET_POS', Char(257), (15760, 850, 10150), 45),
	Insn('CHAR_SET_POS', Char(258), (16560, 850, 9350), 45),
	Insn('CHAR_SET_POS', Char(259), (14830, 850, 9220), 45),
	Insn('CHAR_SET_POS', Char(260), (15630, 850, 8410), 45),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F搜查二课发来了委托呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0105F揭发假货贩子……\n'
		'具体委托内容到底是什么呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0302F话说，从警察局总部\n'
		'发来重要的支援请求，\n'
		'这还是头一次吧？{wait}'
		'{page}'
		'#0304F这也就表示，警察局的其他家伙\n'
		'总算也承认了我们的实力吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0203F#12P这个……也难说吧。{wait}'
		'{page}'
		'#0211F也有可能只是又把\n'
		'一些麻烦的杂务推过来而已。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F嗯，总之，先去听听\n'
		'多诺邦警部怎么说吧。{wait}'
		'{page}'
		'顺利的话，说不定以后还能获得\n'
		'更多与其它课合作的机会呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F是呀……\n'
		'去行政区的警察局总部看看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('QUEST', 27, Insn('TASK_SET', 0)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][42] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1280)), Insn('FLAG', Flag(1281)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 22, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('CALL', Function((0, 43))),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (9350, 850, 10320), 89),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1282)), Insn('FLAG', Flag(1283)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 27, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('CALL', Function((0, 43))),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (9350, 850, 10320), 89),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1292)), Insn('FLAG', Flag(1293)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 31, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('CALL', Function((0, 43))),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (9350, 850, 10320), 89),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][43] = [
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F出门之前，\n'
		'还是先确认一下\n'
		'支援请求吧……{wait}'
		'{page}'
		'说不定会有\n'
		'紧急的委托。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][44] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1286)), Insn('FLAG', Flag(1292)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('IF', [
				(Expr([Insn('ATTR', 10), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F罗伊德前辈，约纳\n'
						'可能会发来联系。{wait}'
						'{page}'
						'还是不要走太远为好吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F说得也是……\n'
						'做好准备之后，\n'
						'就赶快去地下区域吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F……约纳\n'
						'可能会发来联系。{wait}'
						'{page}'
						'#0000F做好准备之后，\n'
						'就赶快去地下区域吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-2190, 0, 68010), 90),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][45] = [
	Insn('TEXT_START', Char(255)),
	Insn('SOUND_PLAY', 810, 0, 0, 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}门上了锁。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][46] = [
	Insn('RETURN'),
]

data['code'][47] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('OBJ_SET_FRAME', Object(255), '01', Insn('1', 1)),
	Insn('CAM_OFFSET', (-1560, 1330, 122920), 0),
	Insn('CAM_ROTATE', 38, 16, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 21500, 0),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(0), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 11), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(1), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 12), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(2), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 13), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(3), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(4), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(5), 8),
		]),
		(None, []),
	]),
	Insn('CHAR_FLAG1_UNSET', Char(257), 8),
	Insn('CHAR_SET_POS', Char(257), (-1830, 30, 122400), 270),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F放在这里就可以了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}罗伊德的房间中\n'
		'追加了新的家具。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('ITEM_REMOVE', 848, 1),
	Insn('FLAG_SET', Flag(646)),
	Insn('0x66', 7, 1),
	Insn('CALL', Function((0, 55))),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(0), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 11), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(1), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 12), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(2), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 13), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(3), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(4), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(5), 8),
		]),
		(None, []),
	]),
	Insn('CALL', Function((0, 64))),
	Insn('CHAR_SET_POS', Char(0), (20, 30, 121010), 0),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][48] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('OBJ_SET_FRAME', Object(255), '02', Insn('1', 1)),
	Insn('CAM_OFFSET', (-2440, 1300, 129810), 0),
	Insn('CAM_ROTATE', 36, 14, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 20500, 0),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(0), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 11), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(1), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 12), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(2), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 13), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(3), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(4), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(5), 8),
		]),
		(None, []),
	]),
	Insn('CHAR_FLAG1_UNSET', Char(257), 8),
	Insn('CHAR_SET_POS', Char(257), (-1940, 0, 128820), 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F放在这里就可以了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}罗伊德的房间中\n'
		'追加了新的家具。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('ITEM_REMOVE', 849, 1),
	Insn('FLAG_SET', Flag(647)),
	Insn('0x66', 8, 1),
	Insn('CALL', Function((0, 55))),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(0), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 11), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(1), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 12), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(2), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 13), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(3), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(4), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(5), 8),
		]),
		(None, []),
	]),
	Insn('CALL', Function((0, 64))),
	Insn('CHAR_SET_POS', Char(0), (20, 30, 121010), 0),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][49] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('OBJ_SET_FRAME', Object(255), '05', Insn('1', 1)),
	Insn('CAM_OFFSET', (153830, 1330, 130810), 0),
	Insn('CAM_ROTATE', 29, 16, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(0), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 11), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(1), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 12), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(2), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 13), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(3), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(4), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(5), 8),
		]),
		(None, []),
	]),
	Insn('CHAR_FLAG1_UNSET', Char(258), 8),
	Insn('CHAR_SET_POS', Char(258), (155090, 30, 129770), 344),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F放在这里就好了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}艾莉的房间中\n'
		'追加了新的家具。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('ITEM_REMOVE', 850, 1),
	Insn('FLAG_SET', Flag(648)),
	Insn('0x66', 9, 1),
	Insn('CALL', Function((0, 55))),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(0), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 11), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(1), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 12), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(2), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 13), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(3), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(4), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(5), 8),
		]),
		(None, []),
	]),
	Insn('CALL', Function((0, 64))),
	Insn('CHAR_SET_POS', Char(0), (155990, 30, 120980), 0),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][50] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('OBJ_SET_FRAME', Object(255), '06', Insn('1', 1)),
	Insn('OBJ_SET_FRAME', Object(255), '06a', Insn('1', 1)),
	Insn('CAM_OFFSET', (154150, 1330, 121920), 0),
	Insn('CAM_ROTATE', 53, 18, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 21500, 0),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(0), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 11), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(1), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 12), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(2), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 13), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(3), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(4), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(5), 8),
		]),
		(None, []),
	]),
	Insn('CHAR_FLAG1_UNSET', Char(258), 8),
	Insn('CHAR_SET_POS', Char(258), (154150, 30, 121920), 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F放在这里就好了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}艾莉的房间中\n'
		'追加了新的家具。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('ITEM_REMOVE', 851, 1),
	Insn('FLAG_SET', Flag(649)),
	Insn('0x66', 10, 1),
	Insn('CALL', Function((0, 55))),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(0), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 11), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(1), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 12), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(2), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 13), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(3), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(4), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(5), 8),
		]),
		(None, []),
	]),
	Insn('CALL', Function((0, 64))),
	Insn('CHAR_SET_POS', Char(0), (155990, 30, 120980), 0),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][51] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('OBJ_SET_FRAME', Object(255), '07', Insn('1', 1)),
	Insn('CAM_OFFSET', (208030, 1330, 127590), 0),
	Insn('CAM_ROTATE', 25, 17, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(0), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 11), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(1), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 12), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(2), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 13), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(3), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(4), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(5), 8),
		]),
		(None, []),
	]),
	Insn('CHAR_FLAG1_UNSET', Char(259), 8),
	Insn('CHAR_SET_POS', Char(259), (208030, 30, 127590), 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F就放在这里吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}缇欧的房间中\n'
		'追加了新的家具。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('ITEM_REMOVE', 852, 1),
	Insn('FLAG_SET', Flag(650)),
	Insn('0x66', 11, 1),
	Insn('CALL', Function((0, 55))),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(0), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 11), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(1), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 12), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(2), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 13), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(3), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(4), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(5), 8),
		]),
		(None, []),
	]),
	Insn('CALL', Function((0, 64))),
	Insn('CHAR_SET_POS', Char(0), (206030, 30, 121140), 0),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][52] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('OBJ_SET_FRAME', Object(255), '08', Insn('1', 1)),
	Insn('CAM_OFFSET', (207830, 1330, 127120), 0),
	Insn('CAM_ROTATE', 56, 17, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(0), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 11), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(1), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 12), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(2), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 13), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(3), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(4), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(5), 8),
		]),
		(None, []),
	]),
	Insn('CHAR_FLAG1_UNSET', Char(259), 8),
	Insn('CHAR_SET_POS', Char(259), (207830, 30, 127120), 107),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F就放在这里吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}缇欧的房间中\n'
		'追加了新的家具。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('ITEM_REMOVE', 853, 1),
	Insn('FLAG_SET', Flag(651)),
	Insn('0x66', 12, 1),
	Insn('CALL', Function((0, 55))),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(0), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 11), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(1), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 12), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(2), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 13), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(3), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(4), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(5), 8),
		]),
		(None, []),
	]),
	Insn('CALL', Function((0, 64))),
	Insn('CHAR_SET_POS', Char(0), (206030, 30, 121140), 0),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][53] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('OBJ_SET_FRAME', Object(255), '03', Insn('1', 1)),
	Insn('CAM_OFFSET', (51760, 1300, 129800), 0),
	Insn('CAM_ROTATE', 29, 14, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 21000, 0),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(0), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 11), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(1), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 12), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(2), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 13), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(3), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(4), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(5), 8),
		]),
		(None, []),
	]),
	Insn('CHAR_FLAG1_UNSET', Char(260), 8),
	Insn('CHAR_SET_POS', Char(260), (51760, 0, 129800), 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F放在这里挺不错啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}兰迪的房间中\n'
		'追加了新的家具。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('ITEM_REMOVE', 854, 1),
	Insn('FLAG_SET', Flag(652)),
	Insn('0x66', 13, 1),
	Insn('CALL', Function((0, 55))),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(0), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 11), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(1), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 12), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(2), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 13), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(3), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(4), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(5), 8),
		]),
		(None, []),
	]),
	Insn('CALL', Function((0, 64))),
	Insn('CHAR_SET_POS', Char(0), (49930, 0, 121070), 0),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][54] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('OBJ_SET_FRAME', Object(255), '04', Insn('1', 1)),
	Insn('OBJ_SET_FRAME', Object(255), '04a', Insn('1', 1)),
	Insn('CAM_OFFSET', (52520, 1300, 124040), 0),
	Insn('CAM_ROTATE', 70, 13, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 22000, 0),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(0), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 11), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(1), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 12), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(2), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 13), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(3), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(4), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(5), 8),
		]),
		(None, []),
	]),
	Insn('CHAR_FLAG1_UNSET', Char(260), 8),
	Insn('CHAR_SET_POS', Char(260), (52520, 0, 124040), 25),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F放在这里挺不错啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}兰迪的房间中\n'
		'追加了新的家具。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('ITEM_REMOVE', 855, 1),
	Insn('FLAG_SET', Flag(653)),
	Insn('0x66', 14, 1),
	Insn('CALL', Function((0, 55))),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(0), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 11), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(1), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 12), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(2), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 13), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(3), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(4), 8),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(5), 8),
		]),
		(None, []),
	]),
	Insn('CALL', Function((0, 64))),
	Insn('CHAR_SET_POS', Char(0), (49930, 0, 121070), 0),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][55] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(654)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}如果获得了家具类的道具，\n'
				'就可以将其放入主人公们的房间。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('FLAG_SET', Flag(654)),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][56] = [
	Insn('TEXT_START', Char(255)),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis164.itp'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}摆放着导力车模型。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][57] = [
	Insn('TEXT_START', Char(255)),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis165.itp'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}摆放着导力音响。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('BGM_STOP', 500),
	Insn('BGM_WAIT'),
	Insn('EXPR_VAR', 2, Expr([Insn('RAND'), Insn('CONST', 8), Insn('MOD'), Insn('SET'), Insn('END')])),
	Insn('SWITCH', [Insn('VAR', 2), Insn('END')], {
		0: [
			Insn('BGM_PLAY', b'\x90\x01\x00'),
			Insn('BREAK'),
		],
		1: [
			Insn('BGM_PLAY', b'\x91\x01\x00'),
			Insn('BREAK'),
		],
		2: [
			Insn('BGM_PLAY', b'\x92\x01\x00'),
			Insn('BREAK'),
		],
		3: [
			Insn('BGM_PLAY', b'\xcc\x00\x00'),
			Insn('BREAK'),
		],
		4: [
			Insn('BGM_PLAY', b'\xcd\x00\x00'),
			Insn('BREAK'),
		],
		5: [
			Insn('BGM_PLAY', b'\xc9\x00\x00'),
			Insn('BREAK'),
		],
		6: [
			Insn('BGM_PLAY', b'\xc8\x00\x00'),
			Insn('BREAK'),
		],
		7: [
			Insn('BGM_PLAY', b'\xca\x00\x00'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][58] = [
	Insn('TEXT_START', Char(255)),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis167.itp'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}墙上挂着壁挂钟。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][59] = [
	Insn('TEXT_START', Char(255)),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis166.itp'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}摆放着典雅花瓶。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][60] = [
	Insn('TEXT_START', Char(255)),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis168.itp'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}墙上挂着壁挂咪西。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][61] = [
	Insn('TEXT_START', Char(255)),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis057.itp'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}摆放着坐坐咪西。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][62] = [
	Insn('TEXT_START', Char(255)),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis171.itp'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}墙上张贴着伊莉雅的海报。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][63] = [
	Insn('TEXT_START', Char(255)),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis170.itp'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}墙上挂着飞镖套组。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][64] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(646)), Insn('FLAG', Flag(647)), Insn('BOOL_AND'), Insn('FLAG', Flag(648)), Insn('BOOL_AND'), Insn('FLAG', Flag(649)), Insn('BOOL_AND'), Insn('FLAG', Flag(650)), Insn('BOOL_AND'), Insn('FLAG', Flag(651)), Insn('BOOL_AND'), Insn('FLAG', Flag(652)), Insn('BOOL_AND'), Insn('FLAG', Flag(653)), Insn('BOOL_AND'), Insn('FLAG', Flag(1925)), Insn('BOOL_AND'), Insn('FLAG', Flag(1926)), Insn('BOOL_AND'), Insn('FLAG', Flag(1927)), Insn('BOOL_AND'), Insn('FLAG', Flag(1928)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xDE', b'\x16\x00'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][65] = [
	Insn('0xF2', Insn('BED')),
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, -1, 1, Text(
		'在此地休息\n'
		'放弃\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('SOUND_LOAD', 13),
			Insn('BGM_STOP', 3000),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('SLEEP', 700),
			Insn('SOUND_PLAY', 13, 0, 0, 100),
			Insn('0x0D'),
			Insn('0x32', Party(255), -2, 0),
			Insn('0x6A', b'\x00\x00\x00\x00\x00\x00'),
			Insn('0x31', b'\x01\x08\xac\r'),
			Insn('0x1F'),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_END', Char(255)),
			Insn('RETURN'),
		]),
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), [
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('TEXT_END', Char(255)),
			Insn('RETURN'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][66] = [
	Insn('0xF2', Insn('BED')),
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, -1, 1, Text(
		'在此地休息\n'
		'放弃\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('SOUND_LOAD', 13),
			Insn('BGM_STOP', 3000),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('SLEEP', 700),
			Insn('SOUND_PLAY', 13, 0, 0, 100),
			Insn('0x0D'),
			Insn('0x32', Party(255), -2, 0),
			Insn('0x6A', b'\x00\x00\x00\x00\x00\x00'),
			Insn('0x31', b'\x01\x08\xac\r'),
			Insn('0x1F'),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_END', Char(255)),
			Insn('RETURN'),
		]),
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), [
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('TEXT_END', Char(255)),
			Insn('RETURN'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][67] = [
	Insn('0xF2', Insn('BED')),
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, -1, 1, Text(
		'在此地休息\n'
		'放弃\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('SOUND_LOAD', 13),
			Insn('BGM_STOP', 3000),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('SLEEP', 700),
			Insn('SOUND_PLAY', 13, 0, 0, 100),
			Insn('0x0D'),
			Insn('0x32', Party(255), -2, 0),
			Insn('0x6A', b'\x00\x00\x00\x00\x00\x00'),
			Insn('0x31', b'\x01\x08\xac\r'),
			Insn('0x1F'),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_END', Char(255)),
			Insn('RETURN'),
		]),
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), [
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('TEXT_END', Char(255)),
			Insn('RETURN'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][68] = [
	Insn('0xF2', Insn('BED')),
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, -1, 1, Text(
		'在此地休息\n'
		'放弃\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('SOUND_LOAD', 13),
			Insn('BGM_STOP', 3000),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('SLEEP', 700),
			Insn('SOUND_PLAY', 13, 0, 0, 100),
			Insn('0x0D'),
			Insn('0x32', Party(255), -2, 0),
			Insn('0x6A', b'\x00\x00\x00\x00\x00\x00'),
			Insn('0x31', b'\x01\x08\xac\r'),
			Insn('0x1F'),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_END', Char(255)),
			Insn('RETURN'),
		]),
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), [
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('TEXT_END', Char(255)),
			Insn('RETURN'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]
