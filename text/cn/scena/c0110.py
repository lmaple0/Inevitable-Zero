# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'c0110',
	'name2': 'c0110',
	'location': 9,
	'bgm': 100,
	'flags': 8192,
	'includes': [
		'c0110',
		'c0110_1',
		None,
		None,
		None,
		None,
	],
	'name3': 'c0110',
	'labels': [],
	'chcp': [
		'chr/ch02500',
		'chr/ch08200',
		'chr/ch02700',
		'chr/ch08700',
		'chr/ch02502',
		'chr/ch02707',
		'chr/ch02708',
		'chr/ch08202',
		None,
		'chr/ch02702',
		'chr/ch00100',
		'chr/ch00202',
		'chr/ch00302',
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
			'pos': (14699, 850, 11199),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((1, 2)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('赛尔盖课长'),
			'pos': (64000, 200, 11399),
			'angle': 180,
			'_1': b'\xd5\x01\x00\x00\x04\x00\xff\xff',
			'function': Function((1, 3)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('琪雅'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((1, 4)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('琪雅'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x07\x00\xff\xff',
			'function': Function((1, 6)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('赛特'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x02\x00\xff\xff',
			'function': Function((1, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('赛特'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\x94\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((1, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('赛特'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\x95\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((1, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('小滴'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\x95\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((1, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('艾莉'),
			'pos': (155759, 29, 129339),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\n\x00\x00\x00',
			'function': Function((1, 10)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('缇欧'),
			'pos': (203660, 150, 128610),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x0b\x00\xff\xff',
			'function': Function((1, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('兰迪'),
			'pos': (51840, 150, 126410),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x0c\x00\xff\xff',
			'function': Function((1, 12)),
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
			'name': Translate('莉夏'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('达德利搜查官'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('白板'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('魔兽调查报告'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
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
			'name': Translate('书籍'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xf6\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
	],
	'monsters': [],
	'triggers': [
		{
			'pos': (10.0, 10.5, 0.0),
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
				-5.0,
				-2.0999999046325684,
				-0.0,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 17)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
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
			'function': Function((0, 51)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (11.0, 13.5, 0.0),
			'range': 4.0,
			'transform': [
				0.5,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.5,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				-5.5,
				-6.75,
				-0.0,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 52)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (19.0, 4.0, 0.0),
			'range': 4.0,
			'transform': [
				0.5,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.5,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				-9.5,
				-2.0,
				-0.0,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 53)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (16960, 850, 10840),
			'range': 2000,
			'bubble_pos': (16960, 1300, 10840),
			'_1': b'|\x00\x00',
			'function': Function((0, 3)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (18240, 850, 7560),
			'range': 1000,
			'bubble_pos': (18240, 1850, 7560),
			'_1': b'|\x00\x01',
			'function': Function((0, 0)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (12500, 850, 5600),
			'range': 2500,
			'bubble_pos': (12500, 1500, 5600),
			'_1': b'|\x00\x00',
			'function': Function((0, 4)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (64000, 30, 9800),
			'range': 1500,
			'bubble_pos': (64000, 1500, 11400),
			'_1': b'~\x00\x01',
			'function': Function((0, 1)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (180910, 0, 62020),
			'range': 1500,
			'bubble_pos': (180910, 1500, 62020),
			'_1': b'|\x00\x00',
			'function': Function((0, 56)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (19980, 0, 63920),
			'range': 1500,
			'bubble_pos': (19980, 1500, 63920),
			'_1': b'|\x00\x00',
			'function': Function((0, 56)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (175940, 0, 63930),
			'range': 1500,
			'bubble_pos': (175940, 1500, 63930),
			'_1': b'|\x00\x00',
			'function': Function((0, 56)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-3150, 0, 122280),
			'range': 1200,
			'bubble_pos': (-3150, 1000, 122280),
			'_1': b'|\x00\x01',
			'function': Function((0, 31)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-2300, 0, 129960),
			'range': 1200,
			'bubble_pos': (-2300, 2000, 129960),
			'_1': b'|\x00\x01',
			'function': Function((0, 32)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (155150, 30, 129699),
			'range': 1200,
			'bubble_pos': (153340, 2029, 130490),
			'_1': b'|\x00\x01',
			'function': Function((0, 33)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (155120, 30, 123880),
			'range': 1200,
			'bubble_pos': (155120, 2029, 123880),
			'_1': b'|\x00\x01',
			'function': Function((0, 34)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (208570, 0, 128030),
			'range': 1200,
			'bubble_pos': (208840, 3000, 130410),
			'_1': b'|\x00\x01',
			'function': Function((0, 35)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (208680, 0, 126170),
			'range': 1200,
			'bubble_pos': (209210, 2000, 127040),
			'_1': b'|\x00\x01',
			'function': Function((0, 36)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (51920, 0, 130570),
			'range': 1200,
			'bubble_pos': (51920, 2500, 130570),
			'_1': b'|\x00\x01',
			'function': Function((0, 37)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (52900, 0, 124470),
			'range': 1200,
			'bubble_pos': (53700, 2000, 125270),
			'_1': b'|\x00\x01',
			'function': Function((0, 38)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (2750, 0, 125420),
			'range': 1200,
			'bubble_pos': (2750, 1500, 125420),
			'_1': b'|\x00\x00',
			'function': Function((0, 57)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (153580, 30, 127880),
			'range': 1200,
			'bubble_pos': (153370, 1530, 128389),
			'_1': b'|\x00\x00',
			'function': Function((0, 58)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (207040, 30, 128539),
			'range': 1200,
			'bubble_pos': (207640, 1500, 129090),
			'_1': b'|\x00\x00',
			'function': Function((0, 59)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (48000, 30, 127860),
			'range': 1200,
			'bubble_pos': (47560, 1500, 128630),
			'_1': b'|\x00\x00',
			'function': Function((0, 60)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (257190, 0, 67990),
			'range': 1200,
			'bubble_pos': (257350, 1500, 68870),
			'_1': b'~\x00\x01',
			'function': Function((0, 9)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\xe8\x03\x00\x00\x00\x00\x00\x00\xd0\x07\x00\x00\x00\x00\x00\x00\x01\x00\t\x00', Function((0, 1)), Function((0, 2))),
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
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('ATTR', 0), Insn('CONST', 110), Insn('EQ'), Insn('EXEC', Insn('PARTY_POSITION', Party(0))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(0))), Insn('CONST', 4), Insn('LT'), Insn('BOOL_AND'), Insn('FLAG', Flag(646)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 848, 0)), Insn('BOOL_AND'), Insn('END')]), [
					Insn('EVENT', Function((1, 22))),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('ATTR', 0), Insn('CONST', 110), Insn('EQ'), Insn('EXEC', Insn('PARTY_POSITION', Party(0))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(0))), Insn('CONST', 4), Insn('LT'), Insn('BOOL_AND'), Insn('FLAG', Flag(647)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 849, 0)), Insn('BOOL_AND'), Insn('END')]), [
					Insn('EVENT', Function((1, 23))),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('ATTR', 0), Insn('CONST', 118), Insn('EQ'), Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 4), Insn('LT'), Insn('BOOL_AND'), Insn('FLAG', Flag(648)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 850, 0)), Insn('BOOL_AND'), Insn('END')]), [
					Insn('EVENT', Function((1, 24))),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('ATTR', 0), Insn('CONST', 118), Insn('EQ'), Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 4), Insn('LT'), Insn('BOOL_AND'), Insn('FLAG', Flag(649)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 851, 0)), Insn('BOOL_AND'), Insn('END')]), [
					Insn('EVENT', Function((1, 25))),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('ATTR', 0), Insn('CONST', 120), Insn('EQ'), Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 4), Insn('LT'), Insn('BOOL_AND'), Insn('FLAG', Flag(650)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 852, 0)), Insn('BOOL_AND'), Insn('END')]), [
					Insn('EVENT', Function((1, 26))),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('ATTR', 0), Insn('CONST', 120), Insn('EQ'), Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 4), Insn('LT'), Insn('BOOL_AND'), Insn('FLAG', Flag(651)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 853, 0)), Insn('BOOL_AND'), Insn('END')]), [
					Insn('EVENT', Function((1, 27))),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('ATTR', 0), Insn('CONST', 112), Insn('EQ'), Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 4), Insn('LT'), Insn('BOOL_AND'), Insn('FLAG', Flag(652)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 854, 0)), Insn('BOOL_AND'), Insn('END')]), [
					Insn('EVENT', Function((1, 28))),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('ATTR', 0), Insn('CONST', 112), Insn('EQ'), Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 4), Insn('LT'), Insn('BOOL_AND'), Insn('FLAG', Flag(653)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 855, 0)), Insn('BOOL_AND'), Insn('END')]), [
					Insn('EVENT', Function((1, 29))),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_SET_POS', Char(10), (256490, 30, 69370), 180),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_SET_POS', Char(15), (257350, 0, 68870), 225),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_SET_POS', Char(13), (255850, 0, 67920), 225),
		]),
		(Expr([Insn('FLAG', Flag(1569)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_SET_POS', Char(11), (5570, 150, 6230), 180),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_SET_POS', Char(14), (3470, 30, 6380), 180),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_SET_POS', Char(11), (257620, 350, 68650), 270),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_SET_POS', Char(14), (256820, 30, 69850), 180),
		]),
		(Expr([Insn('FLAG', Flag(1560)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_SET_POS', Char(11), (5570, 150, 6230), 180),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_SET_POS', Char(13), (2880, 0, 1750), 225),
		]),
		(Expr([Insn('FLAG', Flag(1559)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_FLAG1_SET', Char(10), 16),
			Insn('CHAR_SET_POS', Char(10), (117660, 30, 8100), 0),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_SET_POS', Char(13), (2970, 0, 4170), 225),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
			Insn('CHAR_SET_POS', Char(8), (124620, 30, 5490), 90),
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_SET_POS', Char(10), (117660, 30, 8100), 0),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_SET_POS', Char(13), (2970, 0, 4170), 225),
		]),
		(Expr([Insn('FLAG', Flag(1550)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_SET_POS', Char(14), (14350, 850, 12060), 180),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(17), 128),
					Insn('CHAR_FLAG1_UNSET', Char(18), 128),
				]),
				(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(16), 128),
					Insn('CHAR_FLAG1_UNSET', Char(18), 128),
				]),
				(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(16), 128),
					Insn('CHAR_FLAG1_UNSET', Char(17), 128),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(13), 128),
					Insn('CHAR_SET_POS', Char(13), (3490, 30, 5850), 225),
				]),
				(Expr([Insn('FLAG', Flag(1199)), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(13), 128),
					Insn('CHAR_SET_POS', Char(13), (3490, 30, 5850), 225),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('TASK_GET', 1))), Insn('END')]), []),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(13), 128),
					Insn('CHAR_SET_POS', Char(13), (3490, 30, 5850), 225),
				]),
				(None, [
					Insn('CHAR_FLAG1_UNSET', Char(13), 128),
					Insn('CHAR_SET_POS', Char(13), (3490, 30, 5850), 225),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(13), 128),
					Insn('CHAR_SET_POS', Char(13), (3490, 30, 5850), 225),
				]),
				(Expr([Insn('FLAG', Flag(1199)), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(13), 128),
					Insn('CHAR_SET_POS', Char(13), (3490, 30, 5850), 225),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('TASK_GET', 1))), Insn('END')]), []),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(13), 128),
					Insn('CHAR_SET_POS', Char(13), (3490, 30, 5850), 225),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
			Insn('CHAR_SET_POS', Char(8), (97720, 0, 72570), 0),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
		]),
		(Expr([Insn('FLAG', Flag(536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
		]),
		(Expr([Insn('FLAG', Flag(527)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
		]),
		(Expr([Insn('FLAG', Flag(525)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
			Insn('CHAR_SET_POS', Char(8), (14700, 870, 11200), 180),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 102), Insn('EQ'), Insn('FLAG', Flag(533)), Insn('BOOL_AND'), Insn('FLAG', Flag(534)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 11))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1025)), Insn('FLAG', Flag(1026)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('ATTR', 0), Insn('CONST', 100), Insn('EQ'), Insn('END')]), [
					Insn('0x09', 268435456),
					Insn('EVENT', Function((0, 30))),
				]),
				(Expr([Insn('ATTR', 0), Insn('CONST', 105), Insn('EQ'), Insn('END')]), [
					Insn('EVENT', Function((0, 31))),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 5))),
		]),
		(Expr([Insn('FLAG', Flag(737)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(737)),
			Insn('EVENT', Function((0, 6))),
		]),
		(Expr([Insn('FLAG', Flag(738)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(738)),
			Insn('EVENT', Function((0, 19))),
		]),
		(Expr([Insn('FLAG', Flag(739)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(739)),
			Insn('FLAG_SET', Flag(14)),
			Insn('EVENT', Function((0, 20))),
		]),
		(Expr([Insn('FLAG', Flag(740)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(740)),
			Insn('EVENT', Function((0, 21))),
		]),
		(Expr([Insn('FLAG', Flag(741)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(741)),
			Insn('EVENT', Function((0, 27))),
		]),
		(Expr([Insn('FLAG', Flag(742)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(742)),
			Insn('EVENT', Function((0, 29))),
		]),
		(Expr([Insn('FLAG', Flag(743)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(743)),
		]),
		(Expr([Insn('FLAG', Flag(744)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(744)),
			Insn('EVENT', Function((0, 33))),
		]),
		(Expr([Insn('FLAG', Flag(745)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(745)),
			Insn('EVENT', Function((0, 34))),
		]),
		(Expr([Insn('FLAG', Flag(746)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(746)),
			Insn('FLAG_SET', Flag(14)),
			Insn('EVENT', Function((0, 37))),
		]),
		(Expr([Insn('FLAG', Flag(747)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(747)),
			Insn('EVENT', Function((0, 38))),
		]),
		(Expr([Insn('FLAG', Flag(748)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(748)),
			Insn('EVENT', Function((0, 44))),
		]),
		(Expr([Insn('FLAG', Flag(749)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(749)),
			Insn('EVENT', Function((0, 46))),
		]),
		(Expr([Insn('FLAG', Flag(750)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(750)),
			Insn('EVENT', Function((0, 49))),
		]),
		(Expr([Insn('FLAG', Flag(751)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(751)),
			Insn('EVENT', Function((0, 50))),
		]),
		(Expr([Insn('FLAG', Flag(753)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(753)),
			Insn('EVENT', Function((1, 18))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('ATTR', 0), Insn('CONST', 122), Insn('EQ'), Insn('BOOL_AND'), Insn('FLAG', Flag(1734)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((1, 14))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(524)), Insn('FLAG', Flag(525)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('FLAG', Flag(14)), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('FLAG_UNSET', Flag(14)),
		]),
		(Expr([Insn('FLAG', Flag(800)), Insn('FLAG', Flag(801)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('FLAG', Flag(1341)), Insn('FLAG', Flag(1342)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('EXPR_CHAR_ATTR', Char(13), 45, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(13), 46, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(13), 47, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(14), 45, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(14), 46, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(14), 47, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('0x65', 1, 1),
	Insn('0x65', 3, 1),
	Insn('0x65', 19, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('0x66', 3, 1),
			Insn('0x66', 19, 1),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('0x66', 3, 1),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('0x66', 3, 1),
		]),
		(Expr([Insn('FLAG', Flag(1560)), Insn('END')]), [
			Insn('0x66', 3, 1),
		]),
		(Expr([Insn('FLAG', Flag(1559)), Insn('END')]), [
			Insn('0x66', 3, 1),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1550)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('0x66', 1, 1),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('0x66', 3, 1),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('0x66', 3, 1),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('0x66', 1, 1),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('0x66', 3, 1),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('0x66', 3, 1),
		]),
		(Expr([Insn('FLAG', Flag(536)), Insn('END')]), [
			Insn('0x66', 1, 1),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('0x66', 3, 1),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('0x66', 3, 1),
		]),
		(Expr([Insn('FLAG', Flag(525)), Insn('END')]), []),
		(None, []),
	]),
	Insn('OBJ_SET_FRAME', Object(255), 'tanmatu2', Insn('0', 1)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'tanmatu_add', Insn('0', 1)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('NOT'), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'box01', Insn('0', 1)),
		]),
		(None, [
			Insn('OBJ_SET_FRAME', Object(255), 'objects2', Insn('0', 1)),
		]),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1341)), Insn('NOT'), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'objects2', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'box01', Insn('1', 1)),
			Insn('0x1D', Insn('0', Char(258), 0, 257500, -1000, 68700, 11000, 5000, 90000)),
		]),
		(None, [
			Insn('OBJ_SET_FRAME', Object(255), 'box01', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'objects2', Insn('1', 1)),
		]),
	]),
	Insn('0x65', 2, 1),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(537)), Insn('FLAG', Flag(538)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x66', 2, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(536)), Insn('FLAG', Flag(537)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x00\x80\x00'),
		]),
		(None, []),
	]),
	Insn('OBJ_FLAG_SET', Object(13), 4),
	Insn('OBJ_FLAG_SET', Object(14), 4),
	Insn('OBJ_FLAG_SET', Object(15), 4),
	Insn('OBJ_FLAG_SET', Object(16), 4),
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
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1037)), Insn('FLAG', Flag(1038)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xd2\xc8\x00\x00\x00\x00\x00'),
		]),
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('0x7D', b'\xff\xd2\xc8\x00\x00\x00\x00\x00'),
		]),
		(None, []),
	]),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('0xB5', b'\x00\x02\x80\x00'),
	Insn('0xB5', b'\x00\x03\x80\x00'),
	Insn('0x1B', 8, Function((255, 255)), 255),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(526)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x01\x80\x00'),
			Insn('0xB5', b'\x01\x02\x80\x00'),
			Insn('0xB5', b'\x01\x03\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1024)), Insn('FLAG', Flag(1025)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 13, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x01\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(526)), Insn('FLAG', Flag(609)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 8, Function((0, 55)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1343)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 8, Function((0, 55)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 8, Insn('TASK_GET', 1))), Insn('EXEC', Insn('QUEST_GET', 8, Insn('TASK_GET', 2))), Insn('OR'), Insn('EXEC', Insn('QUEST_GET', 8, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 8, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 0, Function((0, 54)), 0),
		]),
		(None, []),
	]),
	Insn('OBJ_FLAG_UNSET', Object(8), 16),
	Insn('OBJ_FLAG_UNSET', Object(9), 16),
	Insn('0x66', 5, 1),
	Insn('0x66', 6, 1),
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
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(526)), Insn('NOT'), Insn('END')]), [
			Insn('0x65', 15, 1),
			Insn('0x65', 16, 1),
			Insn('0x65', 17, 1),
			Insn('0x65', 18, 1),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('TEXT_START', Char(255)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}终端的导力已经停止了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1477)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F说起来，总部的\n'
						'终端线路不是要在\n'
						'今天进行维护吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(258), Text(
								'#0100F芙兰小姐也说过\n'
								'这件事呢。{wait}'
								'{page}'
								'说是今天一天都不能使用终端，\n'
								'所以她也可以\n'
								'放假了。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(259), Text(
								'#0200F嗯，确实如此。{wait}'
								'{page}'
								'听芙兰小姐说，因为一整天\n'
								'都不能使用终端，所以她也可以\n'
								'得到休假了。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(260), Text(
								'#0300F是啊，小芙兰\n'
								'也说过的吧。{wait}'
								'{page}'
								'今天一天都不能使用终端，\n'
								'所以她也可以\n'
								'休息一下了。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, []),
					]),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F哈哈……我们也\n'
						'有一段时间没工作了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1477)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F总部的终端线路\n'
						'正在进行维护，\n'
						'今天就不能使用终端了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('TEXT_END', Char(255)),
			Insn('RETURN'),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 1, Insn('FLAG_GET', 16))), Insn('EXEC', Insn('QUEST_GET', 1, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((1, 20))),
			Insn('RETURN'),
		]),
		(None, []),
	]),
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
						Insn('FLAG_SET', Flag(13)),
					]),
					(Expr([Insn('FLAG', Flag(13)), Insn('END')]), [
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
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('EXEC', Insn('QUEST_GET', 1, Insn('FLAG_GET', 2))), Insn('BOOL_AND'), Insn('FLAG', Flag(526)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xE3', 11),
			Insn('TEXT_END', Char(255)),
			Insn('CALL', Function((0, 9))),
			Insn('RETURN'),
		]),
		(None, []),
	]),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0xE3', 11),
	Insn('TEXT_END', Char(255)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1024)), Insn('EXEC', Insn('QUEST_GET', 13, Insn('FLAG_GET', 2))), Insn('BOOL_AND'), Insn('FLAG', Flag(1026)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 65, Insn('TASK_SET', 1)),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(537)), Insn('FLAG', Flag(538)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 2),
			Insn('FADE_ON', 300, Color(0x00000000), 100),
			Insn('0x0D'),
			Insn('MENU', 0, -1, -1, 0, Text(
				'【开始临时会议】\n'
				'【还有其它要事】\n'
			)),
			Insn('MENU_WAIT', 0),
			Insn('0x60', 0),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('0x0D'),
			Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
				0: [
					Insn('TEXT_TALK', Char(257), Text(
						'#10400987V#0001F那么，我们赶快\n'
						'开始临时会议吧。{wait}'
						'{page}'
						'#10400988V首先试着整理一下\n'
						'和事件有关的情报吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FADE_ON', 1000, Color(0x00000000), 255),
					Insn('0x0D'),
					Insn('BGM_STOP', 3000),
					Insn('BGM_WAIT'),
					Insn('0x65', 2, 1),
					Insn('CALL', Function((0, 18))),
					Insn('BREAK'),
				],
				1: [
					Insn('TEXT_TALK', Char(258), Text(
						'#10400989V#0100F那么，在处理完其它要事之后，\n'
						'再回到这里吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FADE_ON', 300, Color(0x00000000), 100),
					Insn('SOUND_PLAY', 828, 0, 0, 100),
					Insn('TEXT_SET_POS', -1, -1, -1, -1),
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'{color 5}若想要开始进行临时会议，\n'
						'请在桌上显示！符号的状态\n'
						'按下按钮。{color 0}{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('FADE_OFF', 300, Color(0x00000000)),
					Insn('TEXT_SET_POS', -1, 280, 60, 3),
					Insn('0x5A'),
					Insn('BREAK'),
				],
				None: [],
			}),
			Insn('EVENT_END', 3),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('IMG_LOAD', ResId(0), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis163.itp'),
	Insn('CAM_OFFSET', (64000, 1100, 8600), 0),
	Insn('CAM_ROTATE', 50, 17, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('0x2E', b'\x01\xff\xff'),
	Insn('0x2E', b'\x02\xff\xff'),
	Insn('0x2E', b'\x03\xff\xff'),
	Insn('CHAR_SET_POS', Char(257), (63000, 0, 6700), 0),
	Insn('CHAR_SET_POS', Char(258), (64300, 0, 6700), 0),
	Insn('CHAR_SET_POS', Char(259), (63200, 0, 5400), 0),
	Insn('CHAR_SET_POS', Char(260), (64500, 0, 5400), 0),
	Insn('CHAR_SET_POS', Char(8), (64000, 150, 11400), 180),
	Insn('CHAR_SET_CHCP', Char(8), 4),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(8), Text(
		'#10200312V那么……\n'
		'就来听听你们的答复吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('BGM_PLAY', b'n\x00\x00'),
	Insn('CAM_DISTANCE', 24000, 1500),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10200313V#0304F我没问题，\n'
		'就在这里继续混下去吧。{wait}'
		'{page}'
		'#10200314V#0301F话说回来，当时把我拉到\n'
		'警察局总部的人不就是你嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10200315V#5P#1002F呵呵，如果你不愿意待在这里，\n'
		'我也可以推荐你去一课啊。{wait}'
		'{page}'
		'#10200316V他们或许也很需要\n'
		'你这样的战斗力呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10200317V#0306F呼……好麻烦，还是免了。{wait}'
		'{page}'
		'#10200318V#0300F要是警备队的话倒还可以，\n'
		'像那种紧张死板的地方就算了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10200319V#5P#1000F艾莉你呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10200320V#0104F我也想继续\n'
		'留在这里。{wait}'
		'{page}'
		'#10200321V#0100F赛尔盖课长，再次\n'
		'请您多加关照了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10200322V#5P#1006F呼，你的加入\n'
		'倒真是连我都没想到呢……{wait}'
		'{page}'
		'#10200323V#1001F总部的大人物们之所以会\n'
		'把你推荐到这里来，是因为他们以为\n'
		'这个课负责的都是些安全的杂务吧……{wait}'
		'{page}'
		'#10200324V当然，这里今后的工作可不是那么\n'
		'简单的，你应该早有觉悟了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10200325V#0102F嗯，当然。{wait}'
		'{page}'
		'#10200326V#0104F我已经开始期待着\n'
		'高密度的繁重工作了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10200327V#5P#1004F哼，有骨气。{wait}'
		'{page}'
		'#10200328V#1002F缇欧嘛……嗯，应该就不必再问了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10200329V#4P#0203F嗯，因为和这边从最初开始\n'
		'就是这样约定的。{wait}'
		'{page}'
		'#10200330V#0200F话说回来……\n'
		'今天下午好像有导力缆线的\n'
		'配线工程吧。{wait}'
		'{page}'
		'#10200331V终端的设置\n'
		'就交给我如何？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10200332V#5P#1004F嗯，原本就是这样打算的。{wait}'
		'{page}'
		'#10200333V#1000F那么──\n'
		'就只剩下你了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(8), Text(
		'#10200334V#5P#1003F──罗伊德丄班宁斯。{wait}'
		'{page}'
		'#10200335V毕业于警察学校，在课堂培训和\n'
		'实战训练中全都取得了优秀成绩──{wait}'
		'{page}'
		'#10200336V随即便挑战搜查官资格考试，\n'
		'并漂亮地取得了资格证。{wait}'
		'{page}'
		'#10200337V#1001F说实话，你待在这里，\n'
		'完全可以称得上是屈才了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10200338V#12P#0001F……………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10200339V#5P#1004F像你这种人才，无论\n'
		'去哪个课就职，恐怕都是游刃有余的。{wait}'
		'{page}'
		'#10200340V已经有好几个人来要求我\n'
		'放你去他们的部门了。{wait}'
		'{page}'
		'#10200341V#1002F你是不是也感到有些犹豫呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10200342V#12P#0004F──不。\n'
		'我在经过多方面的考虑之后，已经做出了决定。{wait}'
		'{page}'
		'#10200343V#0000F赛尔盖课长，\n'
		'今后请您多多关照了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10200344V#11P#0302F嘿嘿……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10200345V#11P#0102F罗伊德……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10200346V#12P#0202F………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10200347V#5P#1006F什么嘛，真是没意思。{wait}'
		'{page}'
		'#10200348V我还期待你会稍微露出些\n'
		'烦恼迷惑的表情呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10200349V#12P#0012F……请您严肃一点啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 300),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 300),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 300),
	]),
	Insn('FORK_AWAIT', Char(259), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(8), Text(
		'#10200350V#5P#1003F算啦，今天一天，\n'
		'就让你们全体休假好了。{wait}'
		'{page}'
		'#10200351V把这当作是地狱般的工作量到来之前，\n'
		'最后的一次休假吧。{wait}'
		'{page}'
		'#10200352V#1002F啊，缇欧。\n'
		'终端的设置就拜托你了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10200353V#12P#0204F是，了解。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10200354V#5P#1005F噢……\n'
		'对了，把这个给忘了。{wait}'
		'{page}'
		'#10200355V#1003F那么，再次确认──\n'
		'罗伊德丄班宁斯。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10200356V#12P#0001F到！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10200357V#5P#1001F艾莉丄麦克道尔。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10200358V#0101F到。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10200359V#5P#1001F兰迪丄奥兰多。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10200360V#0301F在。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10200361V#5P#1001F缇欧丄普拉托。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10200362V#12P#0201F……到。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10200363V#5P#1003F本日９：００，\n'
		'正式认可以上四名人员分配至此。{wait}'
		'{page}'
		'#10200364V#1002F欢迎来到特务支援课。{wait}'
		'{page}'
		'#10200365V你们今后将要面对的，是\n'
		'五花八门、堆积如山的工作。\n'
		'敬请期待吧──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 23500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('SOUND_PLAY', 9, 0, 0, 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 0}作为初期调查的津贴，\n'
		'得到了１０００米拉。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('MIRA_ADD', b'\xe8\x03'),
	Insn('SLEEP', 500),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('SLEEP', 2000),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 't4100', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('CAM_OFFSET', (12600, 2350, 5200), 0),
	Insn('CAM_ROTATE', 40, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 1),
	Insn('CHAR_SET_CHCP', Char(259), 11),
	Insn('CHAR_SET_FRAME', Char(259), 2),
	Insn('CHAR_SET_CHCP', Char(260), 12),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_POS', Char(257), (11300, 900, 6650), 90),
	Insn('CHAR_SET_POS', Char(258), (11300, 900, 4600), 90),
	Insn('CHAR_SET_POS', Char(259), (13900, 900, 4600), 270),
	Insn('CHAR_SET_POS', Char(260), (11300, 900, 2550), 90),
	Insn('CHAR_SET_CHCP', Char(8), 4),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('CHAR_FLAG1_SET', Char(8), 64),
	Insn('CHAR_SET_POS', Char(8), (13900, 900, 6650), 270),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_SET_FRAME', Char(8), 1),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis011.itp'),
	Insn('IMG_LOAD', ResId(1), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis120.itp'),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('男人的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#10300029V──那么，从今天开始，\n'
		'就要正式展开工作了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('BGM_PLAY', b'n\x00\x00'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 110), Insn('SET'), Insn('END')])),
	Insn('CAM_OFFSET', (12600, 1850, 5200), 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10300030V#5P#1000F好啦，不管怎么样，\n'
		'总之先补充说明一下好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(8), Text(
		'#10300031V#11P#1000F罗伊德，把搜查手册拿出来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300032V#0001F啊……是的！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('SLEEP', 500),
	Insn('TEXT_MESSAGE', Char(260), Text(
		'#10300033V#0300F是那个印有警察徽章的黑色手册吗，\n'
		'这东西确实很有搜查手册的感觉啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'#10300034V#0100F这个也可以算是警官的\n'
		'身份证明吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(8), Text(
		'#10300035V#1003F嗯，而且上面还记载着\n'
		'各种说明与注意事项。{wait}'
		'{page}'
		'#10300036V同时也有着关于战术导力器的说明，\n'
		'你们可以适当参考。{wait}'
		'{page}'
		'#10300037V#1002F──不过，这手册最主要的用处\n'
		'是对『调查状况』的记录与确认。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(260), Text(
		'#10300038V#0305F『调查状况』……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(8), Text(
		'#10300039V#1003F罗伊德，你来说明。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#10300040V#0000F啊，是。\n'
		'（这都是在警察学校里学过的东西啊。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300041V#0000F──根据警察局的规定，\n'
		'无论进行何种调查任务，\n'
		'都要做好详细记录。{wait}'
		'{page}'
		'#10300042V#0003F在接受了调查任务之后，\n'
		'就要把调查过程中的一切进展与\n'
		'状况记录到搜查手册上。{wait}'
		'{page}'
		'#10300043V在完成任务之后，还要用它来进行报告，\n'
		'所以也关系到考勤评定与特别津贴的发放。{wait}'
		'{page}'
		'#10300044V#0000F因此，在记录的时候，\n'
		'一定要尽可能的详细简练。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10300045V#6P#0100F原来如此，很有道理啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10300046V#12P#0306F唉……\n'
		'听起来好像很麻烦呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10300047V#11P#1000F嗯，大概就是这样。{wait}'
		'{page}'
		'#10300048V#1003F不过呢，在我们特务支援课，\n'
		'情况会稍微有些特殊。{wait}'
		'{page}'
		'#10300049V#1002F除了正规的『调查任务』之外，\n'
		'还会有一些其它的『支援请求』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SLEEP', 50),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300050V#0005F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(8), 1),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(8), Text(
		'#10300051V#5P#1002F缇欧，接下来就拜托你了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10300052V#2P#0203F……是。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(259), 4),
	Insn('CHAR_SET_CHCP', Char(259), 255),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_SET_POS', Char(259), (14800, 850, 5400), 270),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#10300053V#2P#0200F各位，请看这里。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (16100, 1850, 10000), 3000),
	Insn('CAM_ROTATE', 7, 21, 0, 3000),
	Insn('CAM_DISTANCE', 25000, 3000),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (16100, 850, 10000), 2000, 0),
	]),
	Insn('SLEEP', 750),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(8), 0),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('0x90', Char(8), (14700, 850, 7600), b'\x0e\x01'),
	Insn('0x0D'),
	Insn('0x92', Char(8), 14700, 11200, 500),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (14700, 850, 11200), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(257), 4),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('0x90', Char(257), (10400, 850, 7600), b'Z\x00'),
	Insn('CHAR_FLAG1_UNSET', Char(258), 4),
	Insn('CHAR_SET_CHCP', Char(258), 255),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('0x90', Char(258), (10400, 850, 5400), b'}\x00'),
	Insn('CHAR_FLAG1_UNSET', Char(260), 4),
	Insn('CHAR_SET_CHCP', Char(260), 255),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('0x90', Char(260), (10400, 850, 3200), b'}\x00'),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 8))),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 7))),
	Insn('0x92', Char(257), 15200, 8500, 500),
	Insn('SLEEP', 150),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (15200, 850, 8500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('FORK', 8, 2, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x6F', b'Q'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300054V#6P#0000F啊，这是前天的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10300055V#3P#0100F这个就是连接到导力网络的\n'
		'终端装置吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(259), 225, 500),
	Insn('TEXT_TALK', Char(259), Text(
		'#10300056V#11P#0200F是的，我在昨天\n'
		'已经设置完毕了。{wait}'
		'{page}'
		'#10300057V基本来说，它会一直保持着运作状态，\n'
		'登录之后，就会转到这个画面。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(259), 45, 500),
	Insn('SLEEP', 300),
	Insn('SOUND_PLAY', 72, 0, 0, 100),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('SLEEP', 500),
	Insn('TEXT_MESSAGE', Char(260), Text(
		'#10300058V#0305F好像出现了什么文字呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#10300059V#0005F要在这里……接受『支援请求』吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(8), Text(
		'#10300060V#1000F嗯，除了正规的任务之外，\n'
		'这里还会收到从各处发来的委托。{wait}'
		'{page}'
		'#10300061V#1003F例如市民和游客的委托，\n'
		'克洛斯贝尔市政府的协助请求等等，\n'
		'大概会有各式各样的委托吧。{wait}'
		'{page}'
		'#10300062V#1002F但这些委托并不一定要全部接受──\n'
		'有些任务，就算放着不管，\n'
		'也会有游击士那边的人负责解决。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('FORK_AWAIT', Char(259), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300063V#12P#0001F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10300064V#3P#0309F哈哈，原来如此啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10300065V#3P#0103F游击士在市民中有着极高的评价，\n'
		'而我们或多或少也要为警察挽回一些声誉……{wait}'
		'{page}'
		'#10300066V#0100F大概就是这么一回事吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(8), Char(257), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(8), Text(
		'#10300067V#5P#1002F哈，算是吧。{wait}'
		'{page}'
		'#10300068V除此之外，在总部繁忙的时候，\n'
		'大概也会叫你们帮忙。{wait}'
		'{page}'
		'#10300069V像市内的巡逻工作啦，或是\n'
		'一些无足轻重的文案工作啦，等等。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(260), Text(
		'#10300070V#3P#0306F唉……真的假的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300071V#12P#0012F哈哈……\n'
		'总之，先不说那个。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 45, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300072V#6P#0000F好像已经有『支援请求』\n'
		'被发送到这个终端了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10300073V#5P#1003F哦，那你们就\n'
		'自己去确认吧。{wait}'
		'{page}'
		'#10300074V#1000F在进行确认之后，记得将『支援请求』\n'
		'记录在搜查手册里啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(8), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300075V#12P#0000F了解。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0x4C', Char(8), -1),
	Insn('CHAR_FLAG1_UNSET', Char(8), 64),
	Insn('CHAR_SET_POS', Char(0), (15000, 850, 8900), 45),
	Insn('FLAG_SET', Flag(525)),
	Insn('QUEST', 61, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 61, Insn('TASK_SET', 0)),
	Insn('0xB5', b'\x01\x01\x80\x00'),
	Insn('0xB5', b'\x01\x02\x80\x00'),
	Insn('0xB5', b'\x01\x03\x80\x00'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('SLEEP', 100),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (10400, 850, 9300), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (14000, 850, 9300), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (10400, 850, 10000), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (13200, 850, 10000), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (15900, 1750, 9800), 0),
	Insn('CAM_ROTATE', 45, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 24000, 0),
	Insn('CHAR_SET_POS', Char(257), (15200, 850, 9800), 45),
	Insn('CHAR_SET_POS', Char(258), (15900, 850, 9100), 45),
	Insn('CHAR_SET_POS', Char(259), (14100, 850, 9500), 45),
	Insn('CHAR_SET_POS', Char(260), (15600, 850, 8000), 45),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG1_SET', Char(8), 64),
	Insn('CHAR_SET_POS', Char(8), (12400, 850, 10200), 90),
	Insn('0x4B', Char(8), -1),
	Insn('IMG_LOAD', ResId(0), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis120.itp'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 80, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}{color 2}任务【支援请求的补充说明】{color 0}开始！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#10300076V#12P#0305F哎，我还以为是什么大任务，\n'
		'原来只是工作联系而已啊。{wait}'
		'{page}'
		'#10300077V#0300F总之，只要去警察局总部\n'
		'听取那些说明就可以了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300078V#5P#0003F是啊，似乎是这样没错。{wait}'
		'{page}'
		'#10300079V#0000F不过，『导力网络』吗……\n'
		'好像有点明白\n'
		'它是什么东西了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10300080V#11P#0100F和通讯器有所区别的是，\n'
		'它除了声音之外，连图像和文字情报也能发送呢。{wait}'
		'{page}'
		'#10300081V之前也听过相关介绍……\n'
		'现在看来，确实是可以应用到各种场合呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10300082V#6P#0203F嗯，现在已经开始在克洛斯贝尔\n'
		'进行各式各样的实验应用了。{wait}'
		'{page}'
		'#10300083V#0200F目前导入警察局的这个\n'
		'系统也是其中一环呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10300084V#6P#1003F嗯，听说在游击士协会\n'
		'也导入了同样技术的试验装置呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(8), 135, 300),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(8), Text(
		'#10300085V#6P#1002F──概要就是这些了。{wait}'
		'{page}'
		'#10300086V那么，你们就尽快\n'
		'将刚才那个『支援请求』\n'
		'完成吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 315, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300087V#11P#0000F明白了。{wait}'
		'{page}'
		'#10300088V#0001F那个，在那之后\n'
		'该做些什么呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10300089V#3P#1003F随你们高兴……本来是想这样说的，\n'
		'不过，在你们去总部听取说明之后，应该\n'
		'就会接到好几件正式的支援请求了。{wait}'
		'{page}'
		'#10300090V#1002F……对了。{wait}'
		'{page}'
		'#10300091V考虑到是第一次，而且还要向总部交差，\n'
		'所以你们至少先完成一件委托吧。{wait}'
		'{page}'
		'#10300092V那样一来，总部的人也就\n'
		'不会像那样挖苦讽刺你们了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300093V#11P#0006F（问题并不在那里吧……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(8), 90, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(8), Text(
		'#10300094V#3P#1000F另外，罗伊德……\n'
		'你顺便带大家熟悉一下市里吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300095V#11P#0005F熟悉一下……市里吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10300096V#3P#1000F这个城市，可以说是你们今后\n'
		'将要守护的地方了。\n'
		'所以先亲眼做个大致的了解吧。{wait}'
		'{page}'
		'#10300097V出门之后，附近就有武器商会\n'
		'和『导力商店』，先去这两个\n'
		'地方看看吧。{wait}'
		'{page}'
		'#10300098V身为警官，今后可能\n'
		'经常需要到那里去。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300099V#11P#0000F原来如此……明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(8), 135, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(8), Text(
		'#10300100V#3P#1003F我基本上都会待在那边的房间里，\n'
		'但还要午睡、看杂志，所以很忙的。{wait}'
		'{page}'
		'#10300101V如果有事的话，最好别打扰我，\n'
		'尽量自己解决吧。{wait}'
		'{page}'
		'#10300102V#1002F那就先这样吧～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('FORK_LOOP', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('FORK_LOOP', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('FORK_FUNC', Char(8), 3, Function((0, 10))),
	Insn('SLEEP', 1000),
	Insn('FORK_LOOP', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300103V#6P#0011F等、等一下……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_AWAIT', Char(8), 3),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('TEXT_TALK', Char(260), Text(
		'#10300104V#6P#0301F喂喂……\n'
		'真是个不负责任的大叔啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10300105V#0106F唉，这样散漫，不要紧吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10300106V#0211F……对今后充满不安呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300107V#0012F算、算啦……\n'
		'总之，这是我们的初次任务。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (15900, 1750, 9800), 1500),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(259), 2),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300108V#5P#0000F先在市内逛一逛，\n'
		'然后就去处理『支援请求』吧。{wait}'
		'{page}'
		'#10300109V因为是第一次，所以不必太过焦急。\n'
		'要把事情稳妥处理好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10300110V#2P#0100F嗯，说得也是。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10300111V#6P#0204F了解。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10300112V#12P#0300F嗯，那我们就出发吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('BGM_STOP', 2000),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}※调查放在支援课的终端机，\n'
		'\u3000从项目中选择［确认支援请求］，\n'
		'\u3000就会显示罗伊德一行人收到的工作请托（委托）一览表。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}※虽然并没有必要接受每一个委托，\n'
		'\u3000但顺利完成之后，便可获得ＤＰ与米拉。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('CAM_OFFSET', (15000, 1850, 8900), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 340, 0),
	Insn('CAM_DISTANCE', 27500, 0),
	Insn('CHAR_SET_POS', Char(0), (15000, 850, 8900), 225),
	Insn('CHAR_SET_POS', Char(1), (15000, 850, 8900), 225),
	Insn('CHAR_SET_POS', Char(2), (15000, 850, 8900), 225),
	Insn('CHAR_SET_POS', Char(3), (15000, 850, 8900), 225),
	Insn('FLAG_SET', Flag(526)),
	Insn('QUEST', 61, Insn('TASK_SET', 1)),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('SLEEP', 500),
	Insn('BGM_PLAY', b'd\x00\x00'),
	Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 100), Insn('SET'), Insn('END')])),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('CAM_OFFSET', (15900, 1750, 5400), 4000),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (16500, 850, 6000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (16500, 850, 3900), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (18300, 850, 3900), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('0x71', Object(0), b'\x00\x00', 5, 0),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('0x79', b'\x00\x00'),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (19800, 850, 3900), 2000, 0),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 8, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('0x71', Object(0), b'\x05\x00', 0, 0),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('0x79', b'\x00\x00'),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('FORK_QUIT', Char(258), 2),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('0x6F', b'\x01'),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50091', 30),
	Insn('CAM_OFFSET', (64000, 1100, 11400), 0),
	Insn('CAM_ROTATE', 50, 17, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(257), (58500, 0, 3200), 90),
	Insn('CHAR_SET_POS', Char(258), (58500, 0, 3200), 90),
	Insn('CHAR_SET_POS', Char(259), (58500, 0, 3200), 90),
	Insn('CHAR_SET_POS', Char(260), (58500, 0, 3200), 90),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(8), (64000, 150, 11400), 180),
	Insn('CHAR_SET_CHCP', Char(8), 4),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_SET_CHCP', Char(40), 30),
	Insn('CHAR_SET_FRAME', Char(40), 29),
	Insn('CHAR_FLAG1_SET', Char(40), 32768),
	Insn('CHAR_SET_POS', Char(40), (63700, 750, 10300), 0),
	Insn('CHAR_FLAG1_UNSET', Char(40), 128),
	Insn('CHAR_FLAG2_UNSET', Char(40), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('EFF_LOAD', ResId(0), 'event\\eva05_00.eff'),
	Insn('EFF_PLAY', (ResId(0), 0), Char(8), 320, 0, 0, 1300, 0, 350, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu01000.itp'),
	Insn('CAM_DISTANCE', 24000, 1500),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('CAM_OFFSET', (64000, 1100, 8600), 5000),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 12))),
	Insn('SLEEP', 650),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 13))),
	Insn('SLEEP', 650),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 15))),
	Insn('SLEEP', 650),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 14))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x6F', b'\x01'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('TEXT_MESSAGE', Char(8), Text(
		'#10400754V噢噢，回来了啊。{wait}'
		'{page}'
		'#10400755V已经顺利阻止了\n'
		'不良分子的斗殴了？{wait}'
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
		'#10400756V#12P#0006F课长……这个嘛。{wait}'
		'{page}'
		'#10400757V#0001F情况可能\n'
		'变得比之前更麻烦了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400758V#5P#1005F嗯……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}罗伊德将事情的经过\n'
		'对赛尔盖进行了说明。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400759V#5P#1001F……哼，原来如此啊。{wait}'
		'{page}'
		'#10400760V#1003F……………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(8), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(8)),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400761V#12P#0005F那个，课长……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400762V#5P#1003F……对了。{wait}'
		'{page}'
		'#10400763V#1000F这件事情，就交给你们\n'
		'全权处理吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400764V#12P#0011F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10400765V#0105F那个，这是什么意思？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400766V#5P#1003F就此罢手也好，继续追查下去也好，\n'
		'一切都交给你们自己去判断。{wait}'
		'{page}'
		'#10400767V#1000F关于『鲁巴彻』方面的事情，\n'
		'我也没有什么可告诉你们的。{wait}'
		'{page}'
		'#10400768V全部都要靠你们自己去调查。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400769V#12P#0013F这、这种不负责任的发言也太乱来了吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400770V#5P#1001F……如果我让你们就此收手的话，\n'
		'你们能接受吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400771V#12P#0005F哎……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400772V#5P#1003F只要牵扯到黑手党，\n'
		'情况肯定就会变得非常麻烦。{wait}'
		'{page}'
		'#10400773V如果要我以上司的立场\n'
		'做出最妥当的判断，\n'
		'那我也只能让你们别再管了。{wait}'
		'{page}'
		'#10400774V#1001F那样也可以吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400775V#12P#0008F…………不。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10400776V#0306F哎，如果在这种时候放弃，\n'
		'以后要是想起来，也许会觉得很不甘心吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10400777V#0108F是啊……\n'
		'我们都已经了解到这么多情况了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10400778V#4P#0203F……同感。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400779V#5P#1004F──嗯，不过呢。{wait}'
		'{page}'
		'#10400780V如果放任你们这群什么都不懂的小鬼们\n'
		'莽撞乱来，最后身受重伤的话，\n'
		'我大概也会睡不安稳吧……{wait}'
		'{page}'
		'#10400781V#1002F所以至少也给你们介绍一位有用的\n'
		'指引者吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400782V#12P#0005F有用的指引者……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(8), 0),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('CHAR_SET_POS', Char(8), (62800, 0, 11600), 270),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('FORK_LOOP', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('FORK_LOOP', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('FORK_LOOP', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('0x0D'),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (61600, 0, 11600), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('CAM_OFFSET', (64120, 1100, 7920), 2500),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (61600, 0, 8300), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (63000, 0, 7800), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('CHAR_ROTATE', Char(8), 180, 500),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('FORK_QUIT', Char(258), 2),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}赛尔盖递给罗伊德一张名片。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400783V#12P#0005F『格林伍德法律事务所』？{wait}'
		'{page}'
		'#10400784V#0001F哎，好像在哪里\n'
		'听到过这个名字呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400785V#1004F#5P那是家位于西侧大道的法律事务所。{wait}'
		'{page}'
		'#10400786V#1002F里面有位名叫伊安的\n'
		'大胡子律师。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400787V#12P#0000F啊啊……！\n'
		'那家事务所就在面包店的旁边吧？{wait}'
		'{page}'
		'#10400788V说起来，我以前住在那里时，\n'
		'也曾和他打过几次招呼呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10400789V#0104F我也听说过。{wait}'
		'{page}'
		'#10400790V#0100F伊安律师好像是为企业、贸易商等群体\n'
		'提供法律咨询的律师吧？{wait}'
		'{page}'
		'#10400791V同时，他好像也经常亲自给一般市民\n'
		'提供法律援助……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400792V#1003F#5P嗯，因为他满脸胡子，像熊一样，\n'
		'所以总是被人称作『熊胡子律师』。{wait}'
		'{page}'
		'#10400793V那位律师应该掌握着\n'
		'不少关于黑手党的情报。{wait}'
		'{page}'
		'#10400794V#1002F说不定……\n'
		'甚至还有一些连警察都不了解的最新情报呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400795V#12P#0002F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10400796V#12P#0202F……那可真是很厉害呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10400797V#2P#0305F那位律师到底是何方神圣啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#10400798V#1004F#5P哈，见到他之后，马上就会知道啦。{wait}'
		'{page}'
		'#10400799V#1000F我之前去见他的时候，\n'
		'也提起过有关特务支援课的事。{wait}'
		'{page}'
		'#10400800V只要你们将自己的身份表明，\n'
		'他至少应该会把你们的话听完。{wait}'
		'{page}'
		'#10400801V正好趁这个机会去和他打个招呼吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400802V#12P#0001F明、明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400803V#6P#0000F……西侧大道离这里很近。{wait}'
		'{page}'
		'#10400804V总之，我们就去那个\n'
		'法律事务所拜访一下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10400805V#11P#0100F嗯，明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_FLAG1_SET', Char(40), 128),
	Insn('CHAR_FLAG2_SET', Char(40), 32768),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('CHAR_SET_POS', Char(8), (64000, 150, 11400), 180),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('EFF_STOP', (ResId(0), 0)),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CAM_OFFSET', (64000, 1330, 6000), 0),
	Insn('CAM_ROTATE', 45, 26, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(0), (64000, 0, 6000), 0),
	Insn('CHAR_SET_POS', Char(1), (64000, 0, 6000), 0),
	Insn('CHAR_SET_POS', Char(2), (64000, 0, 6000), 0),
	Insn('CHAR_SET_POS', Char(3), (64000, 0, 6000), 0),
	Insn('FLAG_SET', Flag(534)),
	Insn('QUEST', 62, Insn('TASK_SET', 6)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (61000, 0, 3200), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (63000, 0, 6700), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('CHAR_ROTATE', Char(257), 0, 500),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (61000, 0, 3200), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (64300, 0, 6700), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('CHAR_ROTATE', Char(258), 0, 500),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (61000, 0, 3200), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (63200, 0, 5400), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('CHAR_ROTATE', Char(259), 0, 500),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (61000, 0, 3200), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (64500, 0, 5400), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('CHAR_ROTATE', Char(260), 0, 500),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('0x92', Char(8), 61600, 8100, 500),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (61600, 0, 8300), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (61600, 30, 11600), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (62800, 30, 11600), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_POS', Char(8), (64000, 0, 11500), 180),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('0x0D'),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (9900, 1750, 10600), 0),
	Insn('CAM_ROTATE', 50, 22, 0, 0),
	Insn('0x6E', 340, 0),
	Insn('CAM_DISTANCE', 27500, 0),
	Insn('CHAR_SET_POS', Char(257), (9900, 850, 9800), 90),
	Insn('CHAR_SET_POS', Char(259), (9900, 850, 11000), 135),
	Insn('CHAR_SET_POS', Char(258), (8700, 850, 9800), 90),
	Insn('CHAR_SET_POS', Char(260), (8700, 850, 11000), 135),
	Insn('0x0D'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400977V#6P#0005F那是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10400978V#6P#0105F……好像写着什么呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (16800, 1750, 7500), 3500),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (16500, 850, 7000), 2000, 0),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (16200, 850, 8500), 2000, 0),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (15100, 850, 6500), 2000, 0),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (14800, 850, 8300), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'\x01'),
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
		'{color 5}#10400979V『有点私事，出去了。\n'
		'\u3000那件事就交给你们随便处理吧。\n'
		'\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000 赛尔盖』{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_TALK', Char(257), Text(
		'{color 0}#10400980V#6P#0003F课长不在吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'{color 0}#10400981V#3P#0301F那个大叔不会因为怕麻烦，\n'
		'所以故意逃走了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'{color 0}#10400982V#0203F确实无法否定\n'
		'那种可能性呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(258), 0, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'{color 0}#10400983V#12P#0100F算啦算啦……\n'
		'其实允许我们自由处理，\n'
		'也算是对我们有利。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(258), 90, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#10400984V#6P#0101F那么，该怎么办？{wait}'
		'{page}'
		'#10400985V要立刻展开关于\n'
		'此次事件的临时会议吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 270, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400986V#11P#0000F嗯，我想想──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}若想要开始进行临时会议，\n'
		'请在桌上显示！符号的状态\n'
		'按下按钮。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (16500, 850, 7000), 90),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('0x66', 2, 1),
	Insn('FLAG_SET', Flag(537)),
	Insn('QUEST', 62, Insn('TASK_SET', 8)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00102', 30),
	Insn('CAM_OFFSET', (12600, 2350, 7000), 0),
	Insn('CAM_ROTATE', 35, 17, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_CHCP', Char(258), 30),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('CHAR_SET_CHCP', Char(259), 11),
	Insn('CHAR_SET_FRAME', Char(259), 1),
	Insn('CHAR_SET_CHCP', Char(260), 12),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_POS', Char(257), (13500, 850, 8400), 315),
	Insn('CHAR_SET_POS', Char(258), (13900, 900, 6650), 270),
	Insn('CHAR_SET_POS', Char(259), (11300, 900, 6650), 90),
	Insn('CHAR_SET_POS', Char(260), (11300, 900, 4600), 90),
	Insn('OBJ_SET_FRAME', Object(255), 'white', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'white_sd', Insn('0', 1)),
	Insn('CHAR_FLAG1_UNSET', Char(23), 128),
	Insn('0x78', b'\n', Char(23)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(23), (12600, 850, 9500), 0),
	Insn('0xD3', Char(23), 0, 0, 0, 0),
	Insn('IMG_LOAD', ResId(0), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis012.itp'),
	Insn('IMG_LOAD', ResId(1), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis013.itp'),
	Insn('IMG_LOAD', ResId(2), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis163.itp'),
	Insn('IMG_LOAD', ResId(3), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis114.itp'),
	Insn('BGM_PLAY', b'\x04\x02\x00'),
	Insn('CAM_OFFSET', (12600, 1850, 7000), 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10400990V#11P#0003F──案发时间是五天前的深夜。{wait}'
		'{page}'
		'#10400991V『剑蛇帮』和\n'
		'『圣约帮』的成员\n'
		'都遭受到了某些人的袭击。{wait}'
		'{page}'
		'#10400992V#0001F案发地点是旧市街中两个不同的场所。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('SLEEP', 300),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#10400993V#0001F也就是这里，还有这里。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(1), 4), Color(0x00000000), 0, 0),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 0, 0),
	Insn('SLEEP', 1000),
	Insn('IMG_0xC9', (ResId(3), 4), Color(0x00000000), 0, 0),
	Insn('IMG_0xC9', (ResId(3), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(3), 3))),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 0, 0),
	Insn('SLEEP', 500),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'#10400994V#0101F『圣约帮』的成员\n'
		'遭到袭击的地点是西边的小巷……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(260), Text(
		'#10400995V#0301F然后，东边的小演唱厅门前\n'
		'则是『剑蛇帮』的成员\n'
		'遭到袭击的地点。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(3), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(3), 3))),
	Insn('EMOTE', Char(259), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(259), Text(
		'#10400996V#6P#0205F……这么一看的话，\n'
		'就是旧市街完全相反的两侧呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 225, 500),
	Insn('SLEEP', 300),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(621)), Insn('END')]), [
			Insn('QUEST_BONUS_DP', 62, 1),
			Insn('0xD0', 6, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#10400997V#5P#0001F嗯，所以两起事件即使是在同一夜发生，\n'
				'双方应该也无法立刻得知对方成员遇袭。{wait}'
				'{page}'
				'#10400998V#0008F把伤患运送到各自的据点进行\n'
				'包扎救治，第二天早上再送往医院……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#10400999V#12P#0101F被袭击的两个人好像\n'
				'是用同一辆救护车送走的吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#10401000V#5P#0006F嗯，救护车上的工作人员\n'
				'想必也很手忙脚乱吧。{wait}'
				'{page}'
				'#10401001V#0001F接下来，双方才终于确信\n'
				'此次暗算是对方下的手了。\n'
				'然后事态便发展至如今的状况──大概就是这样了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#10401002V#5P#0003F嗯，所以两起事件即使是在同一夜发生，\n'
				'双方应该也无法立刻得知对方成员遇袭。{wait}'
				'{page}'
				'#10401003V#0000F接下来，双方才终于确信\n'
				'此次暗算是对方下的手了。\n'
				'然后事态便发展至如今的状况──大概就是这样了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(260), Text(
		'#10401004V#6P#0306F嗯……这样一来，\n'
		'果然只能理解为，有第三势力插手吧。{wait}'
		'{page}'
		'#10401005V#0301F双方成员都没有\n'
		'事先统一过口径，在此情况下，\n'
		'恐怕任何一方都没有作案的可能吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10401006V#5P#0000F嗯……以现阶段的情报为基础，\n'
		'暂时先把两起案件都假设为\n'
		'是第三者所为吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10401007V#12P#0104F是啊……\n'
		'不把握住每一点可能性的话，\n'
		'推理也就无法继续进展了。{wait}'
		'{page}'
		'#10401008V#0101F──那么，关于那个第三者，\n'
		'我们应该已经可以想到那个名字了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10401009V#5P#0003F是啊。{wait}'
		'{page}'
		'#10401010V#0001F『鲁巴彻商会』，\n'
		'他们是掌控着克洛斯贝尔\n'
		'黑道势力的黑手党。{wait}'
		'{page}'
		'#10401011V根据格蕾丝小姐的情报，\n'
		'大约在半个月之前，曾有人在\n'
		'旧市街目击到了他们的成员。{wait}'
		'{page}'
		'#10401012V#0006F我们现在并没有时间去\n'
		'确认这个情报的真假，不过……{wait}'
		'{page}'
		'#10401013V#0001F暂且就先假定这两起伤害\n'
		'事件都是『鲁巴彻』所为，然后\n'
		'以这个假设为前提继续推理下去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10401014V#6P#0203F……这样一来……{wait}'
		'{page}'
		'#10401015V#0201F接下来的问题果然就是『动机』了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10401016V#5P#0003F嗯，那正是关键问题。{wait}'
		'{page}'
		'#10401017V#0001F……反过来说，\n'
		'如果不把这个问题弄清，\n'
		'推理说不定还会回到原点。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10401018V#6P#0303F嗯～动机嘛……{wait}'
		'{page}'
		'#10401019V#0308F黑手党和两个不良分子，\n'
		'这三方之间应该也扯不上什么利害关系……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10401020V#12P#0103F连接三『点』，\n'
		'应该就能结成一『线』……{wait}'
		'{page}'
		'#10401021V#0100F──那个，罗伊德，\n'
		'你心里应该已经大致有数了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10401022V#5P#0004F哈哈，虽然还不能\n'
		'完全确信吧……{wait}'
		'{page}'
		'#10401023V#0000F连接三『点』，结成一『线』。\n'
		'这样的话，应该考虑的是──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('MENU', 0, -1, -1, 0, Text(
		'【瓦奇的经历】\n'
		'【瓦鲁多的过去】\n'
		'【黑月的存在】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('QUEST_BONUS_DP', 62, 1),
			Insn('0xD0', 6, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#10401024V#5P#0003F这也许是个比较荒谬的\n'
				'想法，不过……{wait}'
				'{page}'
				'#10401025V#0001F两年前出现在旧市街的\n'
				'瓦奇，有可能正是那条『线』。{wait}'
				'{page}'
				'#10401026V比如说，他有可能是鲁巴彻首领的\n'
				'儿子什么的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(258), 0, 1700, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 50),
			Insn('EMOTE', Char(260), 0, 1700, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 50),
			Insn('EMOTE', Char(259), 0, 1700, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(258), Text(
				'#10401027V#12P#0105F然、然后呢……！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#10401028V#6P#0301F喂喂，这是真的吗！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#10401029V#5P#0006F可能性，只是可能性而已啦。{wait}'
				'{page}'
				'#10401030V#0000F在这种情况下，首领为了\n'
				'将离家出走的儿子带回去，\n'
				'就在旧市街设计了那两起事件。{wait}'
				'{page}'
				'#10401031V#0012F不过，假设到这个份上，\n'
				'与其说是推理，倒更像是在幻想了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#10401032V#6P#0306F喂喂……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(257), Text(
				'#10401033V#5P#0003F虽然这仅仅是一种可能性……{wait}'
				'{page}'
				'#10401034V#0001F也许那个瓦鲁多过去\n'
				'曾经得罪过黑手党中的\n'
				'某个成员。{wait}'
				'{page}'
				'#10401035V于是招来怨恨与报复，\n'
				'从而引发了这次的事件……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#10401036V#12P#0106F嗯……\n'
				'这种情况确实也不能排除。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#10401037V#6P#0301F但是，就为了这种程度的小事，\n'
				'再怎么说也不会如此大费周折吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#10401038V#5P#0006F……确实如此，果然是想错了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		2: [
			Insn('QUEST_BONUS_DP', 62, 3),
			Insn('0xD0', 6, Expr([Insn('CONST', 3), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#10401039V#5P#0003F说到可能性的话……\n'
				'比较实际的也就是『黑月』了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#10401040V#6P#0305F哦哦，是那位大胡子律师\n'
				'和我们说的那个组织吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#10401041V#12P#0103F确实，在各种可能性之中，\n'
				'这个大概是最接近真相的……{wait}'
				'{page}'
				'#10401042V#0101F不过，如果是这样的话，\n'
				'要怎样才能把事件连成一条线呢……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#10401043V#6P#0203F如果想把各个点连接成一条线，\n'
				'就需要某种程度的『必然性』……{wait}'
				'{page}'
				'#10401044V#0200F也就是说，『黑月』与\n'
				'黑手党袭击两组不良分子这件事\n'
				'之间，存在着某些『必然性』的联系吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('OR'), Insn('END')]), [
			Insn('EMOTE', Char(259), 0, 1700, (24, 27, 250, 0)),
			Insn('SLEEP', 2000),
			Insn('EMOTE_STOP', Char(259)),
			Insn('TEXT_TALK', Char(259), Text(
				'#10401045V#6P#0200F……那个，罗伊德前辈。{wait}'
				'{page}'
				'#10402001V『黑月』才是那条线──难道就没有\n'
				'这个可能性吗……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 50),
			Insn('EMOTE', Char(260), 0, 1700, (38, 38, 250, 1)),
			Insn('SLEEP', 50),
			Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('CHAR_SET_FRAME', Char(258), 0),
			Insn('TEXT_TALK', Char(257), Text(
				'#10401046V#5P#0005F哎……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#10401047V#6P#0305F喂喂，难道幕后真凶不是\n'
				'黑手党，而是同他们对抗的组织吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#10401048V#6P#0203F不……我们是在『真凶是黑手党』\n'
				'这个前提下展开讨论的。{wait}'
				'{page}'
				'#10401049V#0200F在此基础上，『黑月』也有可能\n'
				'就是那条『线』吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#10401050V#5P#0008F──是啊。\n'
		'这样一来，就能说得通了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('TEXT_TALK', Char(258), Text(
		'#10401051V#12P#0105F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10401052V#6P#0300F你想到什么了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (12600, 850, 8400), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('CHAR_ROTATE', Char(257), 180, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#10401053V#0001F#5P就是那个『必然性』。{wait}'
		'{page}'
		'#10401054V如果『黑月』想要在克洛斯贝尔的黑道势力分一杯羹，\n'
		'那么鲁巴彻将会采取何种对策呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10401055V#6P#0305F这个嘛……\n'
		'单纯来考虑，就是增强战斗力吧。{wait}'
		'{page}'
		'#10401056V#0303F部队的增强和武装的强化，\n'
		'这两点他们应该都会想要实现吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10401057V#0003F#5P身为黑手党，武装强化方面应该\n'
		'可以通过走私交易来解决。{wait}'
		'{page}'
		'#10401058V#0001F可是，他们该如何增加战斗人员呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10401059V#6P#0305F这个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10401060V#12P#0108F按照一般想法来考虑的话，\n'
		'自然是雇佣猎兵团吧……{wait}'
		'{page}'
		'#10401061V#0103F……不对，好像行不通呢。\n'
		'克洛斯贝尔这个地区在很多意义上\n'
		'都一直被周边诸国密切注视着。{wait}'
		'{page}'
		'#10401062V#0101F再加上《不战条约》的签订，\n'
		'在这种情况下，如果擅自动用猎兵团的话，\n'
		'帝国与共和国恐怕都不会坐视不理的。{wait}'
		'{page}'
		'#10401063V而遵从两国意愿的那些\n'
		'政治家与议员们也是一样……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#10401064V#12P#0105F──啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10401065V#6P#0205F罗伊德前辈，莫非他们……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10401066V#6P#0301F是想将那些不良分子的成员\n'
		'当作部队的候补士兵！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10401067V#0003F#5P嗯……那些成员们都是一些血气方刚，\n'
		'并且具有一定组织性的年轻人。{wait}'
		'{page}'
		'#10401068V#0001F作为在这个城市中使用的战斗力，\n'
		'他们实在是再合适不过了吧。{wait}'
		'{page}'
		'#10401069V可是，无论在哪个分子中，\n'
		'都存在着很大的障碍呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10401070V#12P#0101F原来如此……{wait}'
		'{page}'
		'#10401071V不出意外的话，那个瓦奇\n'
		'应该是不会愿意协助黑手党的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10401072V#6P#0203F而以那个瓦鲁多先生的性格来说，\n'
		'应该也只想当老大……{wait}'
		'{page}'
		'#10401073V#0201F无论如何，他肯定也不会愿意\n'
		'在黑手党的手下工作吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10401074V#6P#0308F所以，要设计让他们自相残杀，\n'
		'使两边的实力都被削弱。然后抓准时机，\n'
		'一口气将他们全都收为己用……{wait}'
		'{page}'
		'#10401075V#0301F原来如此，是这么回事啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10401076V#0012F#5P这仅仅是可能之一罢了。{wait}'
		'{page}'
		'#10401077V#0000F而且也只是将现有的情报\n'
		'逐一拼凑起来的结果而已。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10401078V#6P#0309F又来了～！\n'
		'何必这么谦虚嘛～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10401079V#12P#0104F嗯，我也认为这种\n'
		'分析很接近真相了。{wait}'
		'{page}'
		'#10401080V#0102F推理过程严丝合缝，\n'
		'而且就目前情况来看，也相当具有说服力。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10401081V#6P#0202F……搜查官的资格证\n'
		'果然不是摆设呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10401082V#0004F#5P哈哈……谢谢夸奖。{wait}'
		'{page}'
		'#10401083V#0000F──那么，接下来。{wait}'
		'{page}'
		'#10401084V我们就去把这些推理……传达给\n'
		'那两人如何呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#10401085V#12P#0105F那两个人……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10401086V#6P#0305F喂喂，难道是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10401087V#0003F#5P没错……{wait}'
		'{page}'
		'#10401088V就是瓦鲁多丄瓦雷斯\n'
		'和瓦奇丄赫密士菲亚──{wait}'
		'{page}'
		'#10401089V#0000F『剑蛇帮』与\n'
		'『圣约帮』的两个头目。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 26000, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('0xB8', 100, 0),
	Insn('IMG_0xC9', (ResId(2), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
	Insn('SLEEP', 2000),
	Insn('IMG_0xC9', (ResId(2), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
	Insn('MINIGAME', 24, 0, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
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
	Insn('FLAG_SET', Flag(538)),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'c000b', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('CAM_OFFSET', (12600, 2350, 5600), 0),
	Insn('CAM_ROTATE', 40, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_SET_CHCP', Char(259), 11),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_SET_CHCP', Char(260), 12),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_POS', Char(257), (13900, 900, 6650), 270),
	Insn('CHAR_SET_POS', Char(258), (13900, 900, 4600), 270),
	Insn('CHAR_SET_POS', Char(259), (11300, 900, 6650), 90),
	Insn('CHAR_SET_POS', Char(260), (11300, 900, 4600), 90),
	Insn('CAM_OFFSET', (12600, 1850, 5600), 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100053V#11P#0006F……课长来得好慢啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100054V#5P#0001F差不多也该开始早晨的\n'
		'临时会议了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100055V#0106F再怎么说，也不能把课长\n'
		'排除在外吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100056V#6P#0303F嗯～既然如此，\n'
		'我不如再去睡个回笼觉吧。{wait}'
		'{page}'
		'#11100057V#0302F一直睡到中午之后再起来，\n'
		'然后去赌场之类的地方玩玩。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(259), 2),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100058V#5P#0211F真是典型的游手好闲者呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_POS', Char(8), (6000, 850, 10200), 90),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 8),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('TEXT_TALK2', Char(8), Translate('男人的声音'), Text(
		'#11100059V#2P……我迟到了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_FLAG1_UNSET', Char(8), 8),
	Insn('CAM_OFFSET', (3000, 1850, 10200), 2000),
	Insn('CHAR_SET_POS', Char(8), (3000, 850, 10200), 90),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('CHAR_SET_FRAME', Char(259), 1),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('0x6F', b'\x01'),
	Insn('FORK', 8, 1, [
		Insn('0x96', Char(254), (12600, 850, 8400), 2000, 0),
	]),
	Insn('SLEEP', 3000),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (12600, 1850, 6600), 0),
	Insn('CAM_ROTATE', 35, 17, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('CHAR_ROTATE', Char(8), 180, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100060V#2P#0000F──课长，\n'
		'早安。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100061V#4P#0100F早安，\n'
		'我们立刻开始临时会议吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11100062V#5P#1003F不，没那个必要。{wait}'
		'{page}'
		'#11100063V#1000F刚才总部发来了联系。{wait}'
		'{page}'
		'#11100064V今天要你们去执行\n'
		'一项特别任务。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 1700, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 1700, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 1700, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100065V#2P#0005F特别任务……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100066V#6P#0301F听起来好像很可疑啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100067V#6P#0200F……还是像上次\n'
		'那样的调查任务吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11100068V#5P#1004F很遗憾，我也不清楚。{wait}'
		'{page}'
		'#11100069V#1002F先去警察局总部吧，\n'
		'应该有客人在那里等你们。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 25500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 3000),
	Insn('BGM_WAIT'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
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
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('FLAG_SET', Flag(737)),
	Insn('NEW_SCENE', 'c1100', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('CAM_OFFSET', (12600, 1850, 5600), 0),
	Insn('CAM_ROTATE', 40, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 24500, 0),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('CHAR_SET_CHCP', Char(259), 11),
	Insn('CHAR_SET_FRAME', Char(259), 2),
	Insn('CHAR_SET_CHCP', Char(260), 12),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_POS', Char(257), (13900, 900, 6650), 270),
	Insn('CHAR_SET_POS', Char(258), (13900, 900, 4600), 270),
	Insn('CHAR_SET_POS', Char(259), (11300, 900, 6650), 90),
	Insn('CHAR_SET_POS', Char(260), (11300, 900, 4600), 90),
	Insn('CHAR_FLAG1_UNSET', Char(24), 128),
	Insn('0x78', b'\x0b', Char(24)),
	Insn('OBJ_FLAG_UNSET', Object(11), 4),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(24), (12700, 1650, 5300), 0),
	Insn('0xD3', Char(24), 0, 90000, 0, 0),
	Insn('IMG_LOAD', ResId(0), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis120.itp'),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 18, 0, 0, 100),
	Insn('0xBB', b'\xd4\x02\xff\x00'),
	Insn('SLEEP', 500),
	Insn('BGM_PLAY', b'n\x00\x00'),
	Insn('CAM_DISTANCE', 25000, 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100207V#0001F#5P这是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100208V#0103F#11P真的是在各地都发生了呢……{wait}'
		'{page}'
		'#11100209V#0101F但媒体方面却几乎\n'
		'没有任何报道呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100210V#6P#0303F嗯……原来如此啊。{wait}'
		'{page}'
		'#11100211V#0301F看起来，这好像并不是\n'
		'普通的魔兽侵害事件呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100212V#6P#0200F狼型魔兽……\n'
		'会是克洛斯贝尔的特有品种吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100213V#5P#0003F这还真是不太清楚……{wait}'
		'{page}'
		'#11100214V#0001F不过，在受害地点\n'
		'似乎有清晰的\n'
		'脚印残留。{wait}'
		'{page}'
		'#11100215V应该可以确定那种魔兽是真实存在的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100216V#0101F#11P不过，警备队在搜索之后，\n'
		'好像还没有正式确认其存在吧？{wait}'
		'{page}'
		'#11100217V这个稍微让人有些在意呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100218V#6P#0306F嗯……还会隐藏行踪，\n'
		'看来是种相当狡猾的魔兽呢。{wait}'
		'{page}'
		'#11100219V#0301F这种时候，是不是该雇个\n'
		'经验丰富的猎人比较好啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100220V#6P#0203F……是啊。{wait}'
		'{page}'
		'#11100221V#0200F就算我们几个出动，\n'
		'大概也不会有什么收获吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE', Char(260), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 700),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100222V#0105F#11P罗伊德，怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100223V#6P#0300F怎么了？\n'
		'又突然想到什么了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100224V#5P#0004F与其说是突然想到……{wait}'
		'{page}'
		'#11100225V#0000F其实我一直在考虑，如果以『办案』的视角\n'
		'来对此次的魔兽侵害事件进行调查，\n'
		'应该能发现一些关键点吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100226V#0105F#11P以『办案』的视角……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100227V#6P#0205F来调查魔兽侵害事件……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100228V#5P#0000F比如说，如果将这一连串的魔兽侵害事件\n'
		'当作『案件』来看待……{wait}'
		'{page}'
		'#11100229V那么在这种场合下，『犯人』会是谁呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100230V#6P#0300F那肯定是报告中提到的\n'
		'那些狼型魔兽吧。{wait}'
		'{page}'
		'#11100231V而且好像并不只是一只，\n'
		'而是成群结队地行动的呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100232V#5P#0003F那就继续说下一个问题……{wait}'
		'{page}'
		'#11100233V#0001F那个『犯人』的『身份』\n'
		'与『动机』，你们怎么看？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100234V#6P#0305F这个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100235V#0104F#11P……原来如此。{wait}'
		'{page}'
		'#11100236V#0100F只看调查报告书的话，\n'
		'是无法掌握到这些的，对吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100237V#5P#0003F嗯，既然是高智慧魔兽，\n'
		'通常情况下，应该会生活在远离人类的地方。{wait}'
		'{page}'
		'#11100238V如果动机仅仅是因为饥饿，\n'
		'那医院方面的受害报告就完全解释不通了。{wait}'
		'{page}'
		'#11100239V#0000F如此一来，总会存在某种可以让这\n'
		'一切谜团都得到合理解释的『真相』吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100240V#6P#0300F嗯……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100241V#6P#0204F确实……\n'
		'从理论上说，确实如此呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100242V#0100F#11P这样一来，调查方针\n'
		'就已经决定了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100243V#5P#0003F嗯……\n'
		'总之，我们先去受害场所，\n'
		'询问一下相关人员吧。{wait}'
		'{page}'
		'#11100244V#0000F再怎么说，以我们的方式\n'
		'至少能给出一个最低限度的成果，\n'
		'也就是将调查报告书补充完整。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100245V#0104F#11P是啊……{wait}'
		'{page}'
		'#11100246V#0100F哪怕只是一点点也好，只要能对警备队的\n'
		'工作起到帮助，也就不算是白费力气了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100247V#6P#0309F呼～得救了。{wait}'
		'{page}'
		'#11100248V还好不用漫无目的地\n'
		'跑到荒山里去抓捕魔兽啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100249V#6P#0203F那么，罗伊德前辈。{wait}'
		'{page}'
		'#11100250V#0200F如果要进行询问的话……\n'
		'首先要从哪个地方开始问起呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100251V#11P#0005F这个嘛……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100252V#11P#0000F那就先去最初遭到侵害的\n'
		'阿尔摩利卡村看看吧。{wait}'
		'{page}'
		'#11100253V那里的受害情况报告是最具体的……\n'
		'如果能在那里掌握到一点\n'
		'魔兽的特征，就再好不过了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100254V#0104F#11P原来如此……\n'
		'这个提议好像不错呢。{wait}'
		'{page}'
		'#11100255V#0100F那个，阿尔摩利卡村，\n'
		'我记得是在城市的东北方吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100256V#5P#0000F嗯，从东出口出去，\n'
		'然后乘坐导力巴士就可以了。{wait}'
		'{page}'
		'#11100257V#0003F而且……\n'
		'这是我们的第一次市外行动。{wait}'
		'{page}'
		'#11100258V#0001F还不知道将会在目的地遇到何种情况。\n'
		'先做好充分准备再出发吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100259V#6P#0300F说得对。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100260V#6P#0202F谨慎起见，最好也先查看\n'
		'一下其它的支援请求。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
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
	Insn('CHAR_SET_POS', Char(24), (25600, 1650, 9500), 0),
	Insn('CHAR_FLAG1_SET', Char(24), 128),
	Insn('OBJ_FLAG_SET', Object(11), 4),
	Insn('FLAG_SET', Flag(768)),
	Insn('0x65', 1, 1),
	Insn('QUEST', 62, Insn('TASK_SET', 9)),
	Insn('QUEST', 63, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 63, Insn('TASK_SET', 0)),
	Insn('BGM_PLAY', b'd\x00\x00'),
	Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 100), Insn('SET'), Insn('END')])),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch05700', 30),
	Insn('LOAD_CHCP', 'chr/ch00800', 31),
	Insn('LOAD_CHCP', 'apl/ch50106', 34),
	Insn('LOAD_CHCP', 'apl/ch50107', 35),
	Insn('LOAD_CHCP', 'apl/ch50108', 36),
	Insn('LOAD_CHCP', 'apl/ch50109', 37),
	Insn('LOAD_CHCP', 'apl/ch50117', 38),
	Insn('LOAD_CHCP', 'apl/ch50092', 39),
	Insn('IMG_LOAD', ResId(0), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis020.itp'),
	Insn('IMG_LOAD', ResId(1), 180, 0, b'\xb4\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis007.itp'),
	Insn('IMG_LOAD', ResId(2), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu00500.itp'),
	Insn('EFF_LOAD', ResId(0), 'event\\eva05_00.eff'),
	Insn('CAM_OFFSET', (3000, 700, 126000), 0),
	Insn('CAM_ROTATE', 45, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(257), 32),
	Insn('CHAR_FLAG1_SET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 34),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_POS', Char(257), (3000, 450, 126000), 180),
	Insn('CHAR_SET_CHCP', Char(25), 39),
	Insn('CHAR_SET_FRAME', Char(25), 18),
	Insn('CHAR_FLAG1_SET', Char(25), 32768),
	Insn('CHAR_SET_POS', Char(25), (2800, 850, 128500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(25), 128),
	Insn('CHAR_FLAG2_UNSET', Char(25), 32768),
	Insn('OBJ_SET_FRAME', Object(255), 'r_huton', Insn('0', 1)),
	Insn('OBJ_FLAG_UNSET', Object(16), 4),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('少年的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 12}#11200001V#30W等、等一下啊……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('BGM_PLAY', b'\x03\x02\x00'),
	Insn('SLEEP', 1000),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 1000, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('SLEEP', 800),
	Insn('TEXT_SET_POS', 50, 170, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 12}#11200002V说什么要出趟远门……\n'
		'这也太突然了吧。{wait}'
		'{page}'
		'#11200003V你究竟要去哪里啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 250, 110, -1, -1),
	Insn('TEXT_SET_NAME', Translate('青年')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 12}#13300380V雷米菲利亚公国。{wait}'
		'{page}'
		'#13300381V不过呢，虽说是出趟『远门』，\n'
		'大概也只要两个月左右就能回来了吧。{wait}'
		'{page}'
		'#11200006V如果情况顺利，也许\n'
		'不到半个月就能回来了哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 50, 170, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 12}#11200007V这、这我知道，可是……{wait}'
		'{page}'
		'#11200008V哥哥好歹也是\n'
		'警察局的搜查官吧？{wait}'
		'{page}'
		'#11200009V花那么长的时间去旅行，\n'
		'真的没问题吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 250, 110, -1, -1),
	Insn('TEXT_SET_NAME', Translate('青年')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 12}#11200010V噢，怎么啦～{wait}'
		'{page}'
		'#11200011V哥哥不在家，\n'
		'你就那么寂寞吗～？{wait}'
		'{page}'
		'#11200012V真是的，小罗伊德原来是个\n'
		'这么离不开人的孩子吗～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 50, 170, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 12}#11200013V……我说，你别只出去两个月，\n'
		'干脆去旅行两年怎么样？{wait}'
		'{page}'
		'#11200014V就算那样，我一个人也完全没问题。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 250, 110, -1, -1),
	Insn('TEXT_SET_NAME', Translate('青年')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 12}#11200015V抱歉抱歉，是我玩笑开过头了。{wait}'
		'{page}'
		'#11200016V其实呢……\n'
		'我这次出行，是有很重要的理由的。{wait}'
		'{page}'
		'#11200017V也就是所谓的绝密任务啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 50, 170, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 12}#11200018V实在是很可疑啊。{wait}'
		'{page}'
		'#11200019V顺便问一下，\n'
		'是什么样的绝密任务啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 250, 110, -1, -1),
	Insn('TEXT_SET_NAME', Translate('青年')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 12}#11200020V噢噢，问得好。{wait}'
		'{page}'
		'#11200021V其实……\n'
		'我要护送一位特别可爱的女孩，\n'
		'和她一起去旅行啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 50, 170, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 12}#11200022V咦……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 250, 110, -1, -1),
	Insn('TEXT_SET_NAME', Translate('青年')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 12}#11200023V我要带着那个女孩，\n'
		'逃亡到美丽的北国──雷米菲利亚。{wait}'
		'{page}'
		'#11200024V怎么样啊，很羡慕吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 50, 170, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 12}#11200025V…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 250, 110, -1, -1),
	Insn('TEXT_SET_NAME', Translate('青年')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 12}#11200026V算啦，玩笑就开到这里吧。{wait}'
		'{page}'
		'#11200027V我不在的这段日子，你的晚饭\n'
		'我已经拜托邻居帮忙了。{wait}'
		'{page}'
		'#11200028V早饭和午饭的话，自己应该就能解决了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 50, 170, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 12}#11200029V那个，吃饭问题倒是无所谓啦，\n'
		'我自己就完全可以……{wait}'
		'{page}'
		'#11200030V──不对，重点不是这个啦！{wait}'
		'{page}'
		'#11200031V可爱的女孩……\n'
		'你究竟打算做什么啊！？{wait}'
		'{page}'
		'#11200032V这种事情，要是被赛西儿姐姐\n'
		'知道的话怎么办啊！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 250, 110, -1, -1),
	Insn('TEXT_SET_NAME', Translate('青年')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 12}#11200033V哎……{wait}'
		'{page}'
		'#11200034V这和赛西儿有什么关系啊，\n'
		'为什么要在这里提她的名字啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 50, 170, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 12}#11200035V你还问为什么……啊啊，真是受不了！！{wait}'
		'{page}'
		'#11200036V（赛西儿姐姐为何\n'
		'\u3000会对如此迟钝的白痴大哥……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 250, 110, -1, -1),
	Insn('TEXT_SET_NAME', Translate('青年')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 12}#11200037V？？？{wait}'
		'{page}'
		'#11200038V说起来的话，这件事情\n'
		'我早就已经和赛西儿说过了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 50, 170, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 12}#11200039V！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 250, 110, -1, -1),
	Insn('TEXT_SET_NAME', Translate('青年')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 12}#11200040V嗯～但她好像产生了\n'
		'一些奇怪的误解呢。{wait}'
		'{page}'
		'#11200041V虽说是旅行，\n'
		'但也算是警察的出差工作吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 3000, 0),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 12}#11200042V#40W#30A而且那个孩子……\n'
		'#50W才只有……#100W岁而已啊……{color 0}{wait}'
	)),
	Insn('SLEEP', 3000),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('SOUND_LOAD', 806),
	Insn('SOUND_PLAY', 829, 0, 0, 100),
	Insn('SLEEP', 2000),
	Insn('CAM_DISTANCE', 23500, 3000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200043V#5P………嗯…………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SLEEP', 100),
	Insn('0x71', Object(16), b'\x00\x00', 20, 0),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_FRAME', Char(257), 3),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(257), 4),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_FRAME', Char(257), 5),
	Insn('SLEEP', 1000),
	Insn('0x79', b'\x10\x00'),
	Insn('CHAR_SET_FRAME', Char(257), 7),
	Insn('SLEEP', 700),
	Insn('CHAR_SET_FRAME', Char(257), 5),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(257), 6),
	Insn('SLEEP', 700),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200044V#5206F#5P……是梦吗………{wait}'
		'{page}'
		'#11200045V#5208F真怀念啊……\n'
		'那是什么时候的事情了……{wait}'
		'{page}'
		'#11200046V好像是我十二……\n'
		'不，是十三岁左右时的事情吧？{wait}'
		'{page}'
		'#11200047V#5205F说起来，我记得在那之后──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 806, 0, 2, 100),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(257), 0, 1400, (2, 7, 80, 1)),
	Insn('SLEEP', 1000),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(257), 4),
	Insn('CHAR_FLAG1_UNSET', Char(257), 32),
	Insn('CHAR_FLAG1_UNSET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 35),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_POS', Char(257), (1000, 30, 125700), 270),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('0x0D'),
	Insn('CHAR_ROTATE', Char(257), 0, 500),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (1000, 30, 128100), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (1700, 30, 128100), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_SET', Char(25), 128),
	Insn('CHAR_FLAG2_SET', Char(25), 32768),
	Insn('CHAR_FLAG1_SET', Char(257), 32),
	Insn('CHAR_FLAG1_SET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 36),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SOUND_STOP', 806),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('FADE_ON', 500, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#11200048V#5201F你好，我是罗伊德。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('BGM_PLAY', b'o\x00\x00'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('赛尔盖的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#11200049V噢，起来了吗？{wait}'
		'{page}'
		'#11200050V调查报告书\n'
		'已经整理好了吧？{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#11200051V#5205F啊，是的。{wait}'
		'{page}'
		'#11200052V#5200F关于昨天的调查，\n'
		'已经全部整理过了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('赛尔盖的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#11200053V那就可以了。{wait}'
		'{page}'
		'#11200054V赶快收拾准备一下，\n'
		'然后都来课长室。{wait}'
		'{page}'
		'#11200055V有客人在等你们。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#11200056V#5201F！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 2000, 0),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('CHAR_FLAG1_UNSET', Char(257), 32),
	Insn('CHAR_FLAG1_UNSET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CAM_OFFSET', (63800, 1000, 7900), 0),
	Insn('CAM_ROTATE', 60, 15, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 21500, 0),
	Insn('CHAR_SET_CHCP', Char(19), 30),
	Insn('CHAR_SET_FRAME', Char(19), 0),
	Insn('CHAR_SET_CHCP', Char(20), 31),
	Insn('CHAR_SET_FRAME', Char(20), 0),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_SET_CHCP', Char(8), 0),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(8), 32768),
	Insn('CHAR_SET_POS', Char(8), (62900, 0, 7900), 90),
	Insn('CHAR_FLAG1_UNSET', Char(19), 128),
	Insn('CHAR_FLAG2_UNSET', Char(19), 32768),
	Insn('CHAR_FLAG1_SET', Char(19), 32768),
	Insn('CHAR_SET_POS', Char(19), (64599, 0, 7900), 270),
	Insn('CHAR_FLAG1_UNSET', Char(20), 128),
	Insn('CHAR_FLAG2_UNSET', Char(20), 32768),
	Insn('CHAR_FLAG1_SET', Char(20), 32768),
	Insn('CHAR_SET_POS', Char(20), (65600, 0, 7400), 270),
	Insn('CHAR_SET_POS', Char(257), (59000, -1000, 3000), 90),
	Insn('CHAR_SET_POS', Char(258), (59000, 0, 3400), 90),
	Insn('CHAR_SET_POS', Char(259), (59000, 0, 3400), 90),
	Insn('CHAR_SET_POS', Char(260), (59000, 0, 3400), 90),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('SLEEP', 500),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 811, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200057V#11P──打扰了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CAM_OFFSET', (64080, 1000, 7060), 4000),
	Insn('CAM_DISTANCE', 22500, 4000),
	Insn('FORK', 8, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK', 19, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK', 20, 2, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('SLEEP', 200),
	Insn('CHAR_SET_POS', Char(257), (59000, 0, 3400), 90),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 23))),
	Insn('SLEEP', 700),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 24))),
	Insn('SLEEP', 700),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 26))),
	Insn('SLEEP', 700),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 25))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('0x6F', b'\x11'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200058V#0005F#12P索妮亚副司令……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200059V#0300F#12P果然猜中了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200060V#5P#2002F#5P呵呵，早安。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(20), Translate('女性队员'), Text(
		'#11200061V#5P#0502F大家辛苦了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200062V#6P#0104F早安。{wait}'
		'{page}'
		'#11200063V#0102F课长所说的客人\n'
		'果然就是副司令啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200064V#5P#1002F#5P嗯，她们也是\n'
		'刚刚才到的。{wait}'
		'{page}'
		'#11200065V好像是想问问你们的\n'
		'调查情况。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200066V#12P#0000F那倒是没问题……\n'
		'不过，还真是突然呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200067V#6P#0105F矿山镇那边的调查工作\n'
		'还没有完成呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200068V#5P#2006F不好意思哦，原本\n'
		'也没打算要这么急的……{wait}'
		'{page}'
		'#11200069V不过，我们那边的状况\n'
		'稍微发生了一些变故呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200070V#0305F#12P状况发生变故……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200071V#5P#2001F事实上，截至昨天为止，\n'
		'我们都在矿山镇那边进行警备\n'
		'与巡逻工作……{wait}'
		'{page}'
		'#11200072V可是，就在今天早上，\n'
		'却全都撤退回去了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200073V#12P#0001F警备队撤退了……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200074V#12P#0201F魔兽出现在矿山镇，\n'
		'应该是三天前的事情吧……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200075V#5P#2003F嗯，按照我们原本的计划，\n'
		'至少也要将警备工作持续\n'
		'一周左右的……{wait}'
		'{page}'
		'#11200076V#2001F可是，警备队司令下达了指示。\n'
		'说什么不要再做毫无意义的事了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200077V#6P#0101F怎、怎么会毫无意义……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200078V#0308F#12P啧……\n'
		'那个只会阿谀奉承的大叔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(260), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(260), 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_WATCH', Char(259), Char(260), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200079V#5P#0005F兰迪，你认识他吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200080V#0303F#12P我在贝尔加德门任职的时候，\n'
		'见过他无数次呢。{wait}'
		'{page}'
		'#11200081V#0301F虽说身为警备队的领头人物，\n'
		'但似乎与帝国派议员中的一些\n'
		'权贵人物有着很深的瓜葛。{wait}'
		'{page}'
		'#11200082V根本就没在工作，\n'
		'好像一天到晚都在接待应酬。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200083V#6P#0108F虽然早就听过传闻……\n'
		'他果然就是这种人呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200084V#6P#0201F不过，如果对魔兽侵害事件\n'
		'放任不管的话，\n'
		'恐怕还会出现更严重的问题吧……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200085V#5P#2003F嗯……正如你所说。{wait}'
		'{page}'
		'#11200086V#2001F如果只是局部地区遭受侵害的话，\n'
		'以最坏的事态来说，也可以委托\n'
		'游击士协会解决……{wait}'
		'{page}'
		'#11200087V但这次的受害范围实在是太大了。{wait}'
		'{page}'
		'#11200088V身为警备队的成员，我们无论如何\n'
		'也不能再继续坐视下去了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK2', Char(20), Translate('女性队员'), Text(
		'#11200089V#5P#0506F──问题是，\n'
		'都已经过去三周了，但魔兽的\n'
		'来历却仍然未能查明……{wait}'
		'{page}'
		'#11200090V而且，虽然受害范围很广，\n'
		'但实际的受害状况却并不是\n'
		'非常严重……{wait}'
		'{page}'
		'#11200091V#0501F基于这种理由，司令阁下\n'
		'便下达了终止警备工作的命令。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200092V#12P#0001F原来如此啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(19), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200093V#5P#2005F啊，话说回来，\n'
		'还没给你们做过介绍呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(19), Char(20), 500),
	Insn('FORK', 8, 2, [
		Insn('CHAR_WATCH', Char(254), Char(20), 500),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(20), 500),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(20), 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200094V#5P#2004F──这位是诺艾儿上士。{wait}'
		'{page}'
		'#11200095V#2002F虽然还很年轻，但战斗能力\n'
		'和驾驶技术都相当优秀呢。{wait}'
		'{page}'
		'#11200096V目前正在担任我的\n'
		'护卫与支援工作。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(20), 37),
	Insn('CHAR_SET_FRAME', Char(20), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('IMG_0xC9', (ResId(2), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(2), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 1100),
	Insn('TEXT_SET_NAME', Translate('女性队员')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#11200097V我是诺艾儿丄希卡。\n'
		'再次问候，今后请多多关照。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(2), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(2), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 0))),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200098V#12P#0000F彼此彼此……\n'
		'请多多指教了。{wait}'
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
		'#11200099V#12P#0005F哎，希卡……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200100V#6P#0100F莫非，是警察局总部\n'
		'接待员芙兰小姐的……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(20), Text(
		'#11200101V#5P#0509F嗯，我是她的姐姐。{wait}'
		'{page}'
		'#11200102V#0502F听说我妹妹一直\n'
		'承蒙各位的关照呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200103V#12P#0002F哈哈，哪里，应该说是\n'
		'我们一直在给她添麻烦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200104V#0304F#12P不过，原来如此……\n'
		'你就是诺艾儿上士啊。{wait}'
		'{page}'
		'#11200105V#0300F我听说过你哦。\n'
		'唐古拉姆门的女性队员，\n'
		'倍受期待的希望之星啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 150),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(20), 31),
	Insn('CHAR_SET_FRAME', Char(20), 0),
	Insn('0x0D'),
	Insn('CHAR_WATCH', Char(20), Char(260), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(20), Text(
		'#11200106V#5P#0504F呵呵，我也久闻\n'
		'兰迪前辈的大名了。{wait}'
		'{page}'
		'#11200107V#0500F我听说过各式各样关于你的传闻……\n'
		'一直都希望能见上一面呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200108V#0309F#12P哈哈，这可真是让我倍感光荣啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200109V#6P#0005F各式各样的传闻……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200110V#6P#0211F肯定是女性关系方面的吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200111V#0304F#12P没错没错，因为我受到\n'
		'大量女性队员的爱慕，\n'
		'而男人们也只能向我投来羡慕的目光……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(19), 180, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200112V#5P#2004F#5P好了，社交辞令\n'
		'差不多就到此为止吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200113V#0306F#12P（唔）……{wait}'
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
	Insn('FORK', 8, 2, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_ROTATE', Char(20), 225, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200114V#5P#2001F正如我刚才所说……\n'
		'目前的状况稍微有些不妙呢。{wait}'
		'{page}'
		'#11200115V要说能打破现状的要素，\n'
		'也就只有你们的调查结果了……{wait}'
		'{page}'
		'#11200116V说实话，我只是抱着聊胜于无的心态\n'
		'到你们这里确认一下情况的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200117V#12P#0001F原来如此……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200118V#6P#0103F那么，在提交调查报告书的同时，\n'
		'让我来做个大致的说明吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 22000, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('SLEEP', 500),
	Insn('CAM_OFFSET', (64080, 1000, 7060), 0),
	Insn('CAM_ROTATE', 60, 15, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 22000, 0),
	Insn('SLEEP', 1000),
	Insn('CAM_DISTANCE', 22500, 2000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200119V#5P#2005F………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200120V#5P#1003F嗯……原来如此啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(8), Char(19), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200121V#6P#1002F索妮亚，我们课这些小家伙们的\n'
		'能力怎么样啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200122V#5P#2004F……超出期待呢。{wait}'
		'{page}'
		'#11200123V『神狼』的传说，\n'
		'还有魔兽出现在医院屋顶的入侵路线……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(19), Char(20), 400),
	Insn('SLEEP', 400),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200124V#5P#2000F怎么样，诺艾儿？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(20), Char(19), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(20), Text(
		'#11200125V#11P#0506F……老实说，我真的很吃惊。{wait}'
		'{page}'
		'#11200126V#0500F不愧是专业的搜查官，\n'
		'看问题的着眼点果然和常人有所不同呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200127V#5P#2000F与其说是着眼点，\n'
		'倒不如说是思路不同呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(19), 180, 500),
	Insn('FORK', 20, 2, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('FORK', 8, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200128V#5P#2004F──嗯，决定了。{wait}'
		'{page}'
		'#11200129V#2001F请你们继续进行\n'
		'矿山镇那边的调查吧。{wait}'
		'{page}'
		'#11200130V按照这种势头，说不定\n'
		'还能发现一些出乎意料的新线索呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200131V#12P#0005F嗯，我们也\n'
		'正有此意……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200132V#0301F#12P但这样一来，\n'
		'不就等于违反司令大人的那个命令了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200133V#5P#2004F呵呵，他可没说要连委托给\n'
		'你们的支援请求也一并撤销啊。{wait}'
		'{page}'
		'#11200134V#2002F既然都已经发现了魔兽的线索，\n'
		'在此情况下，自然应该马上采取下一步的行动──{wait}'
		'{page}'
		'#11200135V这样的话，应该就没有问题了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200136V#0302F#12P原来如此啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200137V#6P#0102F呵呵，您还真是\n'
		'足智多谋呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(20), Text(
		'#11200138V#5P#0503F……而且，\n'
		'总觉得那些魔兽好像\n'
		'可以感知到我们的行动。{wait}'
		'{page}'
		'#11200139V比起大部队的搜索，\n'
		'也许还是少数人的行动\n'
		'更容易探查到对手的破绽吧……{wait}'
		'{page}'
		'#11200140V#0500F这也正是我们期待各位的原因哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200141V#12P#0000F原来如此……明白了。{wait}'
		'{page}'
		'#11200142V总之，我们接下来就\n'
		'打算前往矿山镇了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200143V#5P#2000F嗯，拜托了。{wait}'
		'{page}'
		'#11200144V如果有什么发现，就请与\n'
		'唐古拉姆门的副司令部联系。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_WATCH', Char(19), Char(8), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200145V#11P#2000F那么，赛尔盖，\n'
		'那件事情就容后再谈吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(8), Char(19), 500),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200146V#6P#1003F嗯，知道了。{wait}'
		'{page}'
		'#11200147V#1000F你可别太过勉强自己啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200148V#11P#2002F呵呵，这话应该是我对你说。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(19), Char(20), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(19), Text(
		'#11200149V#2000F#5P诺艾儿，我们就先行告辞吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 1478, 0, 255, 100),
	Insn('TEXT_TALK', Char(20), Text(
		'#11200150V#0502F#5P是。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(20), Char(257), 500),
	Insn('SLEEP', 300),
	Insn('CROSSFADE', 250),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('CHAR_SET_CHCP', Char(20), 37),
	Insn('CHAR_SET_FRAME', Char(20), 0),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 1498, 0, 255, 100),
	Insn('TEXT_TALK', Char(20), Text(
		'#0500F#5P#8A那么，我们就先告辞了！{wait}'
	)),
	Insn('SLEEP', 1500),
	Insn('FORK', 19, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_CHCP', Char(20), 31),
	Insn('CHAR_SET_FRAME', Char(20), 0),
	Insn('CHAR_ROTATE', Char(20), 225, 500),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(19), 38),
	Insn('CHAR_SET_FRAME', Char(19), 0),
	Insn('CHAR_SET_CHCP', Char(20), 37),
	Insn('CHAR_SET_FRAME', Char(20), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('SLEEP', 750),
	Insn('CHAR_SET_CHCP', Char(19), 30),
	Insn('CHAR_SET_FRAME', Char(19), 0),
	Insn('CHAR_SET_CHCP', Char(20), 31),
	Insn('CHAR_SET_FRAME', Char(20), 0),
	Insn('FORK_LOOP', 8, 2, [
		Insn('CHAR_WATCH', Char(254), Char(19), 500),
	]),
	Insn('FORK_FUNC', Char(19), 3, Function((0, 22))),
	Insn('SLEEP', 500),
	Insn('FORK_FUNC', Char(20), 3, Function((0, 22))),
	Insn('SLEEP', 300),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(19), 500),
	]),
	Insn('FORK_LOOP', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(19), 500),
	]),
	Insn('FORK_LOOP', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(19), 500),
	]),
	Insn('FORK_LOOP', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(19), 500),
	]),
	Insn('SLEEP', 2700),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('FORK_AWAIT', Char(19), 3),
	Insn('FORK_AWAIT', Char(20), 3),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('FORK_QUIT', Char(258), 2),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('FORK_QUIT', Char(8), 2),
	Insn('BGM_STOP', 3000),
	Insn('0x6F', b'\x01'),
	Insn('CHAR_FLAG1_SET', Char(19), 128),
	Insn('CHAR_FLAG2_SET', Char(19), 32768),
	Insn('CHAR_FLAG1_SET', Char(20), 128),
	Insn('CHAR_FLAG2_SET', Char(20), 32768),
	Insn('SLEEP', 200),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'n\x00\x00'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200152V#5P#0001F好像很忙啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200153V#5P#0103F是啊……警备队好像是今天早上\n'
		'才刚从矿山镇撤出的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200154V#5P#1003F嗯，看来是被无能的上司\n'
		'折腾了一趟呢。{wait}'
		'{page}'
		'#11200155V#1000F而且，对共和国那边的警戒\n'
		'工作也不能掉以轻心……{wait}'
		'{page}'
		'#11200156V她还是那么倒霉，抽到了下下签呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200157V#11P#0003F原来如此……{wait}'
		'{page}'
		'#11200158V#0005F对了，课长您和\n'
		'副司令很熟吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200159V#12P#0200F相互之间还轻松随意地\n'
		'直呼对方的名字……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200160V#0303F说起来，把我\n'
		'推荐到这里的人\n'
		'就是副司令哦。{wait}'
		'{page}'
		'#11200161V#0302F你们到底是什么关系啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(8), 180, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200162V#5P#1003F呵，可以说是老交情了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 852, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('EFF_PLAY', (ResId(0), 0), Char(8), 320, 0, 0, 1300, 0, 350, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200163V#5P#1003F呼……{wait}'
		'{page}'
		'#11200164V#1002F先不说这些，你们几个\n'
		'昨天好像很辛苦啊。{wait}'
		'{page}'
		'#11200165V看来今天还要去矿山镇啊，\n'
		'又打算步行去吗？{wait}'
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
		'#11200166V#11P#0006F不，昨天那只是因为\n'
		'重重偶然而已……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200167V#12P#0100F再怎么说，今天\n'
		'也得坐巴士去了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200168V#5P#1005F什么嘛，原来只是这样啊？{wait}'
		'{page}'
		'#11200169V#1004F哼哼，本来还以为\n'
		'你们肯定是在效仿游击士呢。{wait}'
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
	Insn('TEXT_TALK', Char(259), Text(
		'#11200170V#12P#0205F效仿游击士……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200171V#0305F什么意思呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200172V#5P#1002F据说这是他们的习惯……\n'
		'在正式开始工作之前，首先要徒步\n'
		'在周边地区转一圈。{wait}'
		'{page}'
		'#11200173V#1004F既能增强耐力，\n'
		'又能累积与魔兽实战的经验，\n'
		'最重要的是可以勘察一遍地形……{wait}'
		'{page}'
		'#11200174V#1002F正所谓一举三得呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200175V#11P#0001F徒步勘察周边地区……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200176V#0301F原来如此……\n'
		'他们还会这样做啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200177V#12P#0201F莫非，我们昨天遇到的\n'
		'艾丝蒂尔他们也是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200178V#12P#0103F……说不定正是打算\n'
		'徒步走遍这一带呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200179V#5P#1002F呵呵，那两个人啊……\n'
		'好像有过相当不得了的经历呢。{wait}'
		'{page}'
		'#11200180V在解决去年发生的那起\n'
		'利贝尔的异变之中，\n'
		'他们也做出了重要贡献呢。{wait}'
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
		'#11200181V#11P#0001F利贝尔的异变……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200182V#12P#0205F是那件……整个王国的\n'
		'导力全部停滞的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200183V#0301F喂喂，真的假的啊……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200184V#12P#0106F如果那是真的……\n'
		'也就不难理解他们为什么拥有那么强的实力了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200185V#5P#1002F呵，但在克洛斯贝尔的话，\n'
		'他们可是比你们还要新的新人啊。{wait}'
		'{page}'
		'#11200186V如果不希望在转瞬之间就被追上，\n'
		'并被他们远远抛在后面的话，\n'
		'可就要拼命努力了。{wait}'
		'{page}'
		'#11200187V#1003F这次的事件也是一样，如果拖得太久，\n'
		'游击士协会那边恐怕就会出动了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200188V#11P#0003F……明白了，\n'
		'我们会努力将事件解决的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200189V#5P#0001F那么，各位，\n'
		'我们这就向矿山镇出发吧。{wait}'
		'{page}'
		'#11200190V首先应该去的地方是\n'
		'城市北出口的巴士站。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200191V#6P#0101F要是有什么补给品已经用完，\n'
		'可以先到街上补充一下哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200192V#6P#0203F谨慎起见，最好\n'
		'也检查一下终端上的信息。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200193V#0300F#12P哈，总之我们就一步一步地耐心来吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 22750, 2000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('BGM_STOP', 2000),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('EFF_STOP', (ResId(0), 0)),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('0x66', 3, 1),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 34),
	Insn('0xD5', 35),
	Insn('0xD5', 36),
	Insn('0xD5', 37),
	Insn('0xD5', 38),
	Insn('0xD5', 39),
	Insn('CAM_OFFSET', (64000, 1330, 6000), 0),
	Insn('CAM_ROTATE', 45, 26, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(0), (64000, 0, 6000), 0),
	Insn('CHAR_SET_POS', Char(1), (64000, 0, 6000), 0),
	Insn('CHAR_SET_POS', Char(2), (64000, 0, 6000), 0),
	Insn('CHAR_SET_POS', Char(3), (64000, 0, 6000), 0),
	Insn('OBJ_SET_FRAME', Object(255), 'r_huton', Insn('1', 1)),
	Insn('OBJ_FLAG_SET', Object(16), 4),
	Insn('FLAG_SET', Flag(801)),
	Insn('QUEST', 64, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 64, Insn('TASK_SET', 0)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 8, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 8, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 8, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 8, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 8, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'g\x00\x00'),
	Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 103), Insn('SET'), Insn('END')])),
	Insn('0xB8', 100, 103),
	Insn('SOUND_STOP', 806),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('0x92', Char(254), 63700, 7000, 500),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (63700, 0, 7300), 2000, 1),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (61600, 0, 6100), 2000, 1),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (61600, 0, 3300), 2000, 1),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (59000, 0, 3300), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (61600, 0, 3400), 2000, 0),
	]),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (64099, 30, 5500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('CHAR_ROTATE', Char(257), 0, 500),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (61600, 0, 3400), 2000, 0),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (62800, 30, 5500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('CHAR_ROTATE', Char(258), 0, 500),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (61600, 0, 3400), 2000, 0),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (62800, 30, 4400), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('CHAR_ROTATE', Char(259), 0, 500),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (61600, 0, 3400), 2000, 0),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (64099, 30, 4400), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('CHAR_ROTATE', Char(260), 0, 500),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch02607', 30),
	Insn('LOAD_CHCP', 'chr/ch02608', 31),
	Insn('LOAD_CHCP', 'apl/ch50116', 32),
	Insn('CAM_OFFSET', (900, 700, 6200), 0),
	Insn('CAM_ROTATE', 50, 21, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 26500, 0),
	Insn('CHAR_SET_POS', Char(257), (800, 0, 500), 0),
	Insn('CHAR_SET_POS', Char(258), (800, 0, 500), 0),
	Insn('CHAR_SET_POS', Char(259), (800, 0, 0), 0),
	Insn('CHAR_SET_POS', Char(260), (800, 0, 0), 0),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_CHCP', Char(12), 30),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG2_UNSET', Char(12), 32768),
	Insn('CHAR_SET_POS', Char(12), (900, 0, 6200), 180),
	Insn('FORK_FUNC', Char(12), 3, Function((0, 0))),
	Insn('EXPR_CHAR_ATTR', Char(12), 36, Expr([Insn('CONST', 183), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(12), 7, Expr([Insn('CONST', 1800), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(12), 52, Expr([Insn('CONST', 1800), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(12), 45, Expr([Insn('CONST', 1100), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(12), 46, Expr([Insn('CONST', 1100), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(12), 47, Expr([Insn('CONST', 1100), Insn('SET'), Insn('END')])),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 64),
	Insn('CHAR_SET_POS', Char(8), (800, 0, 0), 0),
	Insn('CHAR_SET_COLOR', Char(8), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu01200.itp'),
	Insn('IMG_LOAD', ResId(1), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis153.itp'),
	Insn('CAM_DISTANCE', 24500, 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('SLEEP', 500),
	Insn('CAM_OFFSET', (900, 700, 5200), 2000),
	Insn('CAM_DISTANCE', 25500, 2000),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (200, 0, 3000), 2000, 0),
	]),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 250),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (1300, 0, 3000), 2000, 0),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 400),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (200, 0, 1800), 2000, 0),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 250),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (1300, 0, 1800), 2000, 0),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('SLEEP', 500),
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
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11201038V#12P#0011F什么……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11201039V#0105F哎……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11201040V#0307F哈！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11201041V#4P#0205F为什么……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (800, 0, 600), 2000, 1),
	]),
	Insn('FORK', 8, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (2850, 0, 2000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('CHAR_ROTATE', Char(8), 270, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(8), Text(
		'#11201042V#1011F#11P果然和你们认识吗？{wait}'
		'{page}'
		'#11201043V#1001F哎，它突然就闯了进来，\n'
		'我想都没想就直接拔出了枪……{wait}'
		'{page}'
		'#11201044V但它却毫不在意，\n'
		'直接就到那里睡起来了，\n'
		'这样的话，我实在是没法出手啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (-900, 0, 3000), 3000, 1),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('CAM_OFFSET', (1470, 700, 5610), 1000),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (600, 0, 4500), 3000, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('CHAR_ROTATE', Char(259), 0, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#11201045V#11P#0205F你怎么了……？{wait}'
		'{page}'
		'#11201046V为什么会来这种地方……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FORK_QUIT', Char(12), 3),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(12), 31),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('EXPR_CHAR_ATTR', Char(12), 7, Expr([Insn('CONST', 1800), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(12), 52, Expr([Insn('CONST', 1800), Insn('SET'), Insn('END')])),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_NAME', Translate('白狼')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#11201047V#30W呜噜噜噜……{wait}'
		'{page}'
		'#11201048V呜噜噜噜噜噜噜……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(259), Text(
		'#11201049V#11P#0202F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11201050V#12P#0005F……缇欧。\n'
		'它在说什么呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(259), 180, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#11201051V#0204F#5P……那个。{wait}'
		'{page}'
		'#11201052V#0202F『我的名字是赛特。』{wait}'
		'{page}'
		'#11201053V『各位替我们洗刷了冤屈，\n'
		'\u3000辛苦了。』{wait}'
		'{page}'
		'#11201054V#0204F──就是这样。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11201055V#12P#0002F『赛特』……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11201056V#0102F是、是来道谢的吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11201057V#0309F不、不管怎么说，\n'
		'还真是个傲气十足的家伙啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#11201058V#5414F#5P#30W呜噜噜噜噜噜噜……{wait}'
		'{page}'
		'#11201059V呜噜噜噜噜噜噜噜噜……{wait}'
		'{page}'
		'#11201060V#5413F呜噜噜噜……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(259), 0, 500),
	Insn('TEXT_TALK', Char(259), Text(
		'#11201061V#11P#0205F哎……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11201062V#12P#0001F怎、怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(259), 180, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#11201063V#0208F那个……{wait}'
		'{page}'
		'#11201064V#0203F『但你们还太年轻，\n'
		'\u3000实在是靠不住……』{wait}'
		'{page}'
		'#11201065V『没办法，我只能暂时\n'
		'\u3000助你们一臂之力了。』{wait}'
		'{page}'
		'#11201066V『心情好时，我会帮助你们的。』{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11201067V#12P#0011F什么！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11201068V#0105F哎哎哎哎！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11201069V#0307F喂喂喂喂！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#11201070V#5414F#5P#30W呜嗷……{wait}'
		'{page}'
		'#11201071V#5412F呜噜噜噜……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11201072V#0204F#5P『不用担心。』{wait}'
		'{page}'
		'#11201073V『狼群已经交给部下来指挥了，\n'
		'\u3000你们尽管放心吧。』{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 3)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11201074V#12P#0012F那个，我们并不是\n'
		'在担心那种事啦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('CHAR_SET_CHCP', Char(12), 32),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('EXPR_CHAR_ATTR', Char(12), 7, Expr([Insn('CONST', 1800), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(12), 52, Expr([Insn('CONST', 1800), Insn('SET'), Insn('END')])),
	Insn('SLEEP', 130),
	Insn('FORK', 12, 2, [
		Insn('0xA6', Char(254), 0, 30, 1000, 3000),
	]),
	Insn('SOUND_PLAY', 848, 0, 0, 100),
	Insn('CHAR_SET_FRAME', Char(12), 1),
	Insn('SLEEP', 1100),
	Insn('CHAR_SET_FRAME', Char(12), 2),
	Insn('SLEEP', 130),
	Insn('CHAR_SET_FRAME', Char(12), 3),
	Insn('SLEEP', 130),
	Insn('CHAR_SET_FRAME', Char(12), 4),
	Insn('SLEEP', 130),
	Insn('CHAR_SET_CHCP', Char(12), 30),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('EXPR_CHAR_ATTR', Char(12), 7, Expr([Insn('CONST', 1800), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(12), 52, Expr([Insn('CONST', 1800), Insn('SET'), Insn('END')])),
	Insn('SLEEP', 300),
	Insn('EMOTE', Char(12), 500, 1200, (28, 33, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1600),
	Insn('TEXT_TALK', Char(8), Text(
		'#11201075V#1004F#11P呵呵，传说中的『神狼』吗……{wait}'
		'{page}'
		'#11201076V#1002F看这个样子，你们可被一个\n'
		'相当奇妙的家伙认可了啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#11201077V#6P#0011F课长……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11201078V#1002F#11P总之，和上层说是\n'
		'『警犬』就可以了。{wait}'
		'{page}'
		'#11201079V至于今后要怎么和它相处，\n'
		'就由你们自己来决定吧。{wait}'
		'{page}'
		'#11201080V#1004F那我就回去睡啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_FUNC', Char(8), 3, Function((0, 28))),
	Insn('SLEEP', 500),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('FORK_LOOP', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('FORK_LOOP', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('FORK_LOOP', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 0)),
	Insn('EMOTE', Char(258), 0, 2000, (40, 43, 100, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (40, 43, 100, 0)),
	Insn('EMOTE', Char(260), 0, 2000, (40, 43, 100, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('TEXT_TALK', Char(257), Text(
		'#11201081V#12P#0011F等、等一下啊，课长！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_AWAIT', Char(8), 3),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('FORK_QUIT', Char(258), 2),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('TEXT_TALK', Char(260), Text(
		'#11201082V#0301F这还真是麻烦了啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11201083V#0106F呼……这么做没问题吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11201084V#0204F……我赞成，\n'
		'因为感觉它非常可靠呢。{wait}'
		'{page}'
		'#11201085V#0202F更重要的是，它这柔软的\n'
		'白色绒毛好有魅力……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11201086V#0109F嗯、嗯……\n'
		'这个倒是不能否认呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11201087V#0302F算啦，可靠的帮手又多了一个。\n'
		'这样想的话，不是也很好嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11201088V#6P#0006F哈……是啊。{wait}'
		'{page}'
		'#11201089V#0000F但一直这样下去，情况可能会变得麻烦，\n'
		'还是先去哪里给它买个项圈吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 25000, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 5000),
	Insn('BGM_WAIT'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 302), Insn('SET'), Insn('END')])),
	Insn('QUEST', 63, Insn('FLAG_UNSET', 16)),
	Insn('QUEST', 64, Insn('FLAG_UNSET', 16)),
	Insn('QUEST', 64, Insn('FLAG_UNSET', 32)),
	Insn('ITEM_REMOVE', 724, 1),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 5, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 5, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 5, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 6, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 6, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 6, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 6, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 6, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 7, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 7, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 7, Insn('FLAG_UNSET', 64)),
			Insn('ITEM_REMOVE', 859, 1),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 7, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 7, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 9, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 9, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 9, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 9, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 9, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 10, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 10, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 10, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 10, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 10, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 11, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 11, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 12, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 12, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 12, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 12, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 12, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('ITEM_REMOVE', 725, 1),
	Insn('ITEM_REMOVE', 726, 1),
	Insn('ITEM_REMOVE', 727, 1),
	Insn('0xE3', 10),
	Insn('SLEEP', 1000),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 800, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('TEXT_RESET', b'\x03'),
	Insn('0xE3', 3),
	Insn('SLEEP', 100),
	Insn('MINIGAME', 43, 0, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
	Insn('0xDE', b'%\x00'),
	Insn('0xDE', b'\x1e\x00'),
	Insn('0xDE', b'\x1f\x00'),
	Insn('SLEEP', 100),
	Insn('CAM_OFFSET', (-1000000, 0, 0), 0),
	Insn('0xC7', b'\x00\x10\x00\x00\x00'),
	Insn('EXPR_ATTR', 80, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
	Insn('EXPR_ATTR', 49, Expr([Insn('CONST', 151), Insn('SET'), Insn('END')])),
	Insn('SAVE'),
	Insn('MINIGAME', 43, 1, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 800, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xC7', b'\x01\x10\x00\x00\x00'),
	Insn('0xE3', 11),
	Insn('EXPR_ATTR', 4, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'c050b', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][28] = [
	Insn('CHAR_FLAG1_UNSET', Char(8), 4),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (2600, 850, 9000), 2000, 1),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (1300, 850, 10300), 2000, 1),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (1300, 2650, 13800), 2000, 0),
	]),
	Insn('SLEEP', 1500),
	Insn('FORK', 8, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('RETURN'),
]

data['code'][29] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('LOAD_CHCP', 'apl/ch50090', 32),
	Insn('LOAD_CHCP', 'apl/ch50092', 33),
	Insn('IMG_LOAD', ResId(0), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis113.itp'),
	Insn('CAM_OFFSET', (500, 1100, 2500), 0),
	Insn('CAM_ROTATE', 45, 21, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 24500, 0),
	Insn('CHAR_SET_POS', Char(257), (1000, 0, 0), 0),
	Insn('CHAR_SET_POS', Char(258), (11100, 870, 5700), 90),
	Insn('CHAR_SET_POS', Char(259), (12700, 870, 8200), 180),
	Insn('CHAR_SET_POS', Char(260), (1000, 0, 0), 0),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_CHCP', Char(25), 33),
	Insn('CHAR_SET_FRAME', Char(25), 10),
	Insn('CHAR_FLAG1_SET', Char(25), 32768),
	Insn('CHAR_SET_POS', Char(25), (13000, 1400, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(25), 128),
	Insn('CHAR_FLAG2_UNSET', Char(25), 32768),
	Insn('CHAR_SET_CHCP', Char(26), 32),
	Insn('CHAR_SET_FRAME', Char(26), 12),
	Insn('CHAR_FLAG1_SET', Char(26), 32768),
	Insn('CHAR_SET_POS', Char(26), (13400, 1300, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(26), 128),
	Insn('CHAR_FLAG2_UNSET', Char(26), 32768),
	Insn('CHAR_SET_CHCP', Char(27), 33),
	Insn('CHAR_SET_FRAME', Char(27), 10),
	Insn('CHAR_FLAG1_SET', Char(27), 32768),
	Insn('CHAR_SET_POS', Char(27), (12400, 1400, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(27), 128),
	Insn('CHAR_FLAG2_UNSET', Char(27), 32768),
	Insn('CHAR_SET_CHCP', Char(28), 32),
	Insn('CHAR_SET_FRAME', Char(28), 12),
	Insn('CHAR_FLAG1_SET', Char(28), 32768),
	Insn('CHAR_SET_POS', Char(28), (12000, 1300, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(28), 128),
	Insn('CHAR_FLAG2_UNSET', Char(28), 32768),
	Insn('CHAR_SET_CHCP', Char(29), 33),
	Insn('CHAR_SET_FRAME', Char(29), 10),
	Insn('CHAR_FLAG1_SET', Char(29), 32768),
	Insn('CHAR_SET_POS', Char(29), (13000, 1400, 4600), 0),
	Insn('CHAR_SET_CHCP', Char(30), 32),
	Insn('CHAR_SET_FRAME', Char(30), 12),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('CHAR_SET_POS', Char(30), (13400, 1300, 4600), 0),
	Insn('CHAR_SET_CHCP', Char(31), 33),
	Insn('CHAR_SET_FRAME', Char(31), 10),
	Insn('CHAR_FLAG1_SET', Char(31), 32768),
	Insn('CHAR_SET_POS', Char(31), (12400, 1400, 4600), 0),
	Insn('CHAR_SET_CHCP', Char(32), 32),
	Insn('CHAR_SET_FRAME', Char(32), 12),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_SET_POS', Char(32), (12000, 1300, 4600), 0),
	Insn('CHAR_SET_CHCP', Char(33), 32),
	Insn('CHAR_SET_FRAME', Char(33), 7),
	Insn('CHAR_FLAG1_SET', Char(33), 32768),
	Insn('CHAR_SET_POS', Char(33), (12700, 1400, 5500), 0),
	Insn('CAM_DISTANCE', 25000, 2500),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('SLEEP', 500),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (500, 0, 2100), 2000, 0),
	]),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 700),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (1500, 0, 1800), 2000, 0),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100189V#0000F#5P我们回来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100190V#0300F#11P回来啦～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(258), 270, 500),
	Insn('TEXT_TALK2', Char(258), Translate('艾莉的声音'), Text(
		'#12100191V#3P啊，你们回来了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('CAM_OFFSET', (11100, 1950, 5700), 2000),
	Insn('CAM_ROTATE', 45, 19, 0, 2000),
	Insn('0x6F', b'A'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100192V#0005F#2P怎么，\n'
		'你们先回来了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100193V#11P#0104F呵呵，因为我们只是在总部\n'
		'做了一点简单的档案整理啦。{wait}'
		'{page}'
		'#12100194V#0102F回来以后，还和缇欧\n'
		'一起把午餐做好了哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100195V#0302F#2P噢，也准备了我们的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(259), 225, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100196V#0202F#5P是的……不过也只是做了简单的\n'
		'通心粉和沙拉而已，不嫌弃的话请用。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100197V#0009F#9P这就足够了，\n'
		'那我们就不客气了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100198V#11P#0109F呵呵，那你们两个\n'
		'先去洗手吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 24500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('CAM_OFFSET', (12600, 1850, 5600), 0),
	Insn('CAM_ROTATE', 40, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 24000, 0),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_SET_CHCP', Char(259), 11),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_SET_CHCP', Char(260), 12),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_POS', Char(257), (13900, 900, 6650), 270),
	Insn('CHAR_SET_POS', Char(258), (13900, 900, 4600), 270),
	Insn('CHAR_SET_POS', Char(259), (11300, 900, 6650), 90),
	Insn('CHAR_SET_POS', Char(260), (11300, 900, 4600), 90),
	Insn('CHAR_FLAG1_UNSET', Char(29), 128),
	Insn('CHAR_FLAG2_UNSET', Char(29), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('SLEEP', 500),
	Insn('CAM_DISTANCE', 25000, 2000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100199V#6P#0205F对了……{wait}'
		'{page}'
		'#12100200V#0200F罗伊德前辈那边的\n'
		'交通管理工作，做得如何了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100201V#11P#0006F啊，那工作相当麻烦呢。{wait}'
		'{page}'
		'#12100202V#0000F要用人力将那些违章停靠的导力车\n'
		'都推到墙边。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100203V#6P#0300F欢乐街那里有很多车呢。{wait}'
		'{page}'
		'#12100204V因为正好是在公演之前，\n'
		'所以相当热闹啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100205V#0104F#11P说起来……\n'
		'下个月终于就要公开演出了呢。{wait}'
		'{page}'
		'#12100206V#0100F《彩虹剧团》的新剧码。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100207V#6P#0300F是叫『金之太阳、银之月』啊。{wait}'
		'{page}'
		'#12100208V#0306F我之前也想去买票的，但不幸的是，\n'
		'连下个月的票都已经全部卖光了～{wait}'
		'{page}'
		'#12100209V最后总算是勉强买到了\n'
		'下下个月的Ｂ席票。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(259), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100210V#6P#0205F《彩虹剧团》，\n'
		'竟然如此受欢迎吗……{wait}'
		'{page}'
		'#12100211V#0203F虽然我也知道剧团的\n'
		'招牌明星伊莉雅丄普拉提耶\n'
		'是个超级名人。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100212V#5P#0003F说起来，我虽然\n'
		'看过彩虹剧团的舞剧……{wait}'
		'{page}'
		'#12100213V#0000F但从没欣赏过\n'
		'伊莉雅丄普拉提耶的表演啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100214V#6P#0306F哎呀呀，那可真是太令人同情了。{wait}'
		'{page}'
		'#12100215V#0301F──这个世界上的人只分为两种。{wait}'
		'{page}'
		'#12100216V#0304F欣赏过伊莉雅丄普拉提耶之表演的人\n'
		'与没有欣赏过的人──\n'
		'ｂｙ兰迪丄奥兰多。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100217V#5P#0012F这也太夸张了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100218V#0102F呵呵，不过她确实很厉害呢。{wait}'
		'{page}'
		'#12100219V#0104F该怎么说才好呢……\n'
		'只要欣赏过一次她的表演，\n'
		'仿佛就连灵魂也要被夺去一般……{wait}'
		'{page}'
		'#12100220V#0100F如果这个世界上存在着『天才』，\n'
		'那她毫无疑问就是其中之一了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100221V#5P#0005F这样啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100222V#6P#0202F……稍微有点兴趣了呢。{wait}'
		'{page}'
		'#12100223V#0206F不过，我们最近的工作\n'
		'真是莫名其妙地多呢……{wait}'
		'{page}'
		'#12100224V#0200F彩虹剧团的公演也是原因之一吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100225V#0106F因为克洛斯贝尔的创立纪念庆典\n'
		'和彩虹剧团的新剧公开日\n'
		'正好赶在一起了……{wait}'
		'{page}'
		'#12100226V#0100F警察的工作肯定要比\n'
		'往年都忙得多啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100227V#6P#0306F哈，不过丢到咱们这里的工作\n'
		'全都是一些杂务啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100228V#5P#0012F算了算了。{wait}'
		'{page}'
		'#12100229V#0000F再怎么说，和最初那时相比，\n'
		'我们接到的工作已经重要不少了。{wait}'
		'{page}'
		'#12100230V克洛斯贝尔时报周刊也不再\n'
		'写那种讽刺我们的报道了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100231V#6P#0203F……不过，现在仍然\n'
		'还会将我们与游击士做比较呢。{wait}'
		'{page}'
		'#12100232V#0211F特别是和……艾丝蒂尔他们……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100233V#5P#0006F呼……确实啊。{wait}'
		'{page}'
		'#12100234V#0001F他们只有两个人而已，\n'
		'为什么可以活跃到这种程度呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100235V#0108F因为他们和其他游击士也有合作，\n'
		'所以工作效率应该会比较高……{wait}'
		'{page}'
		'#12100236V#0106F而我们虽然有四个人，\n'
		'但和其它的部门基本没形成互助关系……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100237V#6P#0303F不，在我看来，\n'
		'更关键的是那个叫约书亚的小子。{wait}'
		'{page}'
		'#12100238V他为那个莽撞冲动的艾丝蒂尔\n'
		'提供了非常高效的后方支援工作。{wait}'
		'{page}'
		'#12100239V#0301F战斗也好，各种日常工作也好，\n'
		'两个人的默契程度实在是非同寻常。{wait}'
		'{page}'
		'#12100240V再加上，他们的经验相当丰富呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100241V#6P#0206F这也就是说，现在的我们\n'
		'还差得很远吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(258), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('EMOTE', Char(257), 0, 1700, (40, 43, 100, 3)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100242V#5P#0012F算、算啦……\n'
		'我们也已经成长了不少呢。{wait}'
		'{page}'
		'#12100243V#0000F而且最近，也多了位\n'
		'可靠的帮手来帮我们──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100244V#11P#0005F……说起来，赛特去哪里了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100245V#0105F今天都没看见它呢……{wait}'
		'{page}'
		'#12100246V#0100F昨天倒是一整天都在屋顶上\n'
		'晒太阳睡觉呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100247V#6P#0306F在和魔兽战斗的时候，\n'
		'它确实是帮了我们不少……{wait}'
		'{page}'
		'#12100248V#0300F但平时究竟都在干些什么呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(259), 2),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100249V#6P#0204F……它的性格非常孤高。{wait}'
		'{page}'
		'#12100250V即使想用我们人类的规章制度\n'
		'去束缚它，也是毫无意义的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100251V#11P#0006F不过，毕竟是作为警犬登记的，\n'
		'所以希望它至少也能遵守最低限度的规章啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100252V#5P#0000F话说回来，最初我还担心\n'
		'周围的居民们会怕它呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100253V#6P#0302F但没想到它竟然会\n'
		'在那起车祸中救出了小孩啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_SET_VOLUME', b'2\xb8\x0b\x00\x00'),
	Insn('MINIGAME', 23, 3000, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
	Insn('SLEEP', 3000),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('SLEEP', 1000),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'#12100254V#0103F搬运车的方向盘失灵了，\n'
		'撞上了路边的围栏……{wait}'
		'{page}'
		'#12100255V#0102F当时我还在想是什么声音呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#12100256V#0004F慌慌张张地跑到外面一看，\n'
		'正好看到赛特把即将被车轮辗过的\n'
		'龙救下的飒爽之姿……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(260), Text(
		'#12100257V#0309F哈哈，如此出色的表现，大概\n'
		'都能和那位亚里欧斯大叔一较高下了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#12100258V#0202F……确实呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 1000, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('BGM_SET_VOLUME', b'd\xe8\x03\x00\x00'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100259V#0104F呵呵……自那之后，\n'
		'它在西侧大道就变得特别受欢迎了。{wait}'
		'{page}'
		'#12100260V#0102F龙他们好像也\n'
		'非常喜欢和它亲近呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100261V#5P#0004F哈哈，是啊。{wait}'
		'{page}'
		'#12100262V#0000F算啦，也不能太过依赖\n'
		'赛特博得的人气……{wait}'
		'{page}'
		'#12100263V我们要靠自己努力才行啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100264V#6P#0204F……赞成。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100265V#6P#0300F那么，从下午开始，\n'
		'我们就来处理支援请求吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 517, 0, 0, 100),
	Insn('PARTY_CRAFT_ADD', Party(2), 172),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}缇欧习得了特殊战技\n'
		'『赛特召唤』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}在战斗中使用此战技，\n'
		'赛特就会出现在ＡＴ表中，\n'
		'并于相应回合进行支援行动。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}另外，根据剧情的进展，\n'
		'此战技有时也会无法使用。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FLAG_SET', Flag(722)),
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
	Insn('CHAR_FLAG1_SET', Char(32), 128),
	Insn('CHAR_FLAG2_SET', Char(32), 32768),
	Insn('CHAR_FLAG1_SET', Char(33), 128),
	Insn('CHAR_FLAG2_SET', Char(33), 32768),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0xD5', 33),
	Insn('CHAR_SET_POS', Char(0), (13820, 850, 9650), 270),
	Insn('CHAR_SET_POS', Char(1), (13820, 850, 9650), 270),
	Insn('CHAR_SET_POS', Char(2), (13820, 850, 9650), 270),
	Insn('CHAR_SET_POS', Char(3), (13820, 850, 9650), 270),
	Insn('FLAG_SET', Flag(1024)),
	Insn('QUEST', 64, Insn('TASK_SET', 13)),
	Insn('QUEST', 65, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 65, Insn('TASK_SET', 0)),
	Insn('0xB5', b'\x01\x01\x80\x00'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][30] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch05200', 30),
	Insn('LOAD_CHCP', 'chr/ch05202', 31),
	Insn('LOAD_CHCP', 'chr/ch00002', 32),
	Insn('LOAD_CHCP', 'chr/ch00102', 33),
	Insn('LOAD_CHCP', 'apl/ch50090', 34),
	Insn('LOAD_CHCP', 'apl/ch50091', 35),
	Insn('CAM_OFFSET', (1000, 900, 2800), 0),
	Insn('CAM_ROTATE', 50, 21, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(257), (500, 0, 1800), 0),
	Insn('CHAR_SET_POS', Char(258), (1500, 0, 1800), 0),
	Insn('CHAR_SET_POS', Char(259), (500, 0, 700), 0),
	Insn('CHAR_SET_POS', Char(260), (1500, 0, 700), 0),
	Insn('CHAR_SET_CHCP', Char(21), 30),
	Insn('CHAR_SET_FRAME', Char(21), 0),
	Insn('CHAR_FLAG1_SET', Char(21), 32768),
	Insn('CHAR_SET_POS', Char(21), (3000, 0, 4700), 90),
	Insn('CHAR_FLAG1_UNSET', Char(21), 128),
	Insn('CHAR_FLAG2_UNSET', Char(21), 32768),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu01800.itp'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
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
	Insn('FORK_AWAIT', Char(257), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100293V#6P#0005F噢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100294V#6P#0100F好像已经来了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(21), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_WATCH', Char(21), Char(257), 500),
	Insn('SOUND_PLAY', 1635, 0, 255, 100),
	Insn('TEXT_TALK2', Char(21), Translate('紫发的女孩'), Text(
		'#12100295V#5P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (620, 1000, 2850), 1500),
	Insn('EMOTE', Char(21), 0, 2000, (40, 43, 100, 3)),
	Insn('FORK', 21, 1, [
		Insn('0x95', Char(254), (880, 0, 4250), 2500, 0),
	]),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(21), 500),
	]),
	Insn('FORK_LOOP', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(21), 500),
	]),
	Insn('FORK_LOOP', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(21), 500),
	]),
	Insn('FORK_LOOP', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(21), 500),
	]),
	Insn('FORK_AWAIT', Char(21), 1),
	Insn('CHAR_WATCH', Char(21), Char(257), 500),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK2', Char(21), Translate('紫发的女孩'), Text(
		'#12100296V#1805F#5P对、对不起……！{wait}'
		'{page}'
		'#12100297V#1803F我擅自就进来了。\n'
		'……那个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('FORK_QUIT', Char(258), 2),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100298V#12P#0004F不，没关系的，\n'
		'我们已经知道你要来了。{wait}'
		'{page}'
		'#12100299V#0002F是来找我们商量事情的吧？\n'
		'欢迎来到特务支援课。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(21), Translate('紫发的女孩'), Text(
		'#12100300V#1802F#5P呼……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 1636, 0, 255, 100),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 1700),
	Insn('TEXT_SET_NAME', Translate('紫发的女孩')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#12100302V那个，我的名字叫莉夏丄毛。{wait}'
		'{page}'
		'#12100303V非常感谢各位今天\n'
		'愿意接受商量……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
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
	Insn('TEXT_SET_POS', -1, 80, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#12100304V#12P#0005F（呜哇……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 20, -1, -1),
	Insn('TEXT_MESSAGE', Char(260), Text(
		'#12100305V#0301F（这、这真是……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 200, -1, -1),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#12100306V#0205F#12P（身材娇小，内涵丰富呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 200, -1, -1),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'#12100307V#0106F（呼……\n'
		'\u3000别这么露骨地盯着人家看啊。）{wait}'
		'{page}'
		'#12100308V#0111F（──喂，罗伊德？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 80, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#12100309V#12P#0011F（啊……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100310V#12P#0003F总、总之，\n'
		'请到那边就坐吧。{wait}'
		'{page}'
		'#12100311V#0000F然后可以请你先把事情大概说明一下吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 24500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 2500),
	Insn('BGM_WAIT'),
	Insn('0x0A', 268435456),
	Insn('CALL', Function((0, 32))),
	Insn('RETURN'),
]

data['code'][31] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch05200', 30),
	Insn('LOAD_CHCP', 'chr/ch05202', 31),
	Insn('LOAD_CHCP', 'chr/ch00002', 32),
	Insn('LOAD_CHCP', 'chr/ch00102', 33),
	Insn('LOAD_CHCP', 'apl/ch50090', 34),
	Insn('LOAD_CHCP', 'apl/ch50091', 35),
	Insn('CAM_OFFSET', (1700, 1200, 7000), 0),
	Insn('CAM_ROTATE', 55, 21, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(257), (1900, 850, 9900), 180),
	Insn('CHAR_SET_POS', Char(258), (700, 850, 9900), 180),
	Insn('CHAR_SET_POS', Char(259), (700, 850, 11100), 180),
	Insn('CHAR_SET_POS', Char(260), (1900, 850, 11100), 180),
	Insn('CHAR_SET_CHCP', Char(21), 30),
	Insn('CHAR_SET_FRAME', Char(21), 0),
	Insn('CHAR_FLAG1_SET', Char(21), 32768),
	Insn('CHAR_SET_POS', Char(21), (2700, 0, 3200), 90),
	Insn('CHAR_FLAG1_UNSET', Char(21), 128),
	Insn('CHAR_FLAG2_UNSET', Char(21), 32768),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu01800.itp'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100293V#0005F#6P噢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100294V#0100F好像已经来了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(21), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_WATCH', Char(21), Char(257), 500),
	Insn('SOUND_PLAY', 1635, 0, 255, 100),
	Insn('TEXT_TALK2', Char(21), Translate('紫发的女孩'), Text(
		'#12100295V#2P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (900, 1850, 7450), 1500),
	Insn('CAM_DISTANCE', 26000, 1500),
	Insn('EMOTE', Char(21), 0, 2000, (40, 43, 100, 3)),
	Insn('FORK', 21, 1, [
		Insn('0x95', Char(254), (1150, 0, 6330), 2500, 0),
	]),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (1900, 850, 8400), 1500, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (700, 850, 8400), 1500, 0),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (1900, 850, 9600), 1500, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (700, 850, 9600), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(21), 1),
	Insn('CHAR_WATCH', Char(21), Char(257), 500),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK2', Char(21), Translate('紫发的女孩'), Text(
		'#12100296V#1805F#2P对、对不起……！{wait}'
		'{page}'
		'#12100297V#1806F我擅自就进来了。\n'
		'……那个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100298V#5P#0004F不，没关系的，\n'
		'我们已经知道你要来了。{wait}'
		'{page}'
		'#12100299V#0002F是来找我们商量事情的吧？\n'
		'欢迎来到特务支援课。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(21), Translate('紫发的女孩'), Text(
		'#12100300V#2P#1802F呼……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 1636, 0, 255, 100),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 1700),
	Insn('TEXT_SET_NAME', Translate('紫发的女孩')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#12100302V那个，我的名字叫莉夏丄毛。{wait}'
		'{page}'
		'#12100303V非常感谢各位今天\n'
		'愿意接受商量……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
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
	Insn('TEXT_SET_POS', -1, 80, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#12100304V#12P#0005F（呜哇……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 20, -1, -1),
	Insn('TEXT_MESSAGE', Char(260), Text(
		'#12100305V#0301F（这、这真是……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 200, -1, -1),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#12100306V#0205F#12P（身材娇小，内涵丰富呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 200, -1, -1),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'#12100307V#0106F（呼……\n'
		'\u3000别这么露骨地盯着人家看啊。）{wait}'
		'{page}'
		'#12100308V#0111F（──喂，罗伊德？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 80, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#12100309V#12P#0011F（啊……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100310V#0003F#5P总、总之，\n'
		'请到那边就坐吧。{wait}'
		'{page}'
		'#12100311V#0000F然后可以请你先把事情大概说明一下吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 25500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 2500),
	Insn('BGM_WAIT'),
	Insn('CALL', Function((0, 32))),
	Insn('RETURN'),
]

data['code'][32] = [
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (5500, 950, 4300), 0),
	Insn('CAM_ROTATE', 43, 19, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 22500, 0),
	Insn('CHAR_SET_CHCP', Char(257), 32),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(258), 33),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_SET_CHCP', Char(259), 11),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_SET_CHCP', Char(260), 12),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_POS', Char(257), (6050, 130, 6250), 180),
	Insn('CHAR_SET_POS', Char(258), (4600, 130, 2200), 0),
	Insn('CHAR_SET_POS', Char(259), (5500, 130, 2200), 0),
	Insn('CHAR_SET_POS', Char(260), (6400, 130, 2200), 0),
	Insn('CHAR_SET_CHCP', Char(21), 31),
	Insn('CHAR_SET_FRAME', Char(21), 0),
	Insn('CHAR_SET_POS', Char(21), (4900, 130, 6250), 180),
	Insn('CHAR_SET_CHCP', Char(25), 34),
	Insn('CHAR_SET_FRAME', Char(25), 25),
	Insn('CHAR_FLAG1_SET', Char(25), 32768),
	Insn('CHAR_SET_POS', Char(25), (4900, 280, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(25), 128),
	Insn('CHAR_FLAG2_UNSET', Char(25), 32768),
	Insn('CHAR_SET_CHCP', Char(26), 34),
	Insn('CHAR_SET_FRAME', Char(26), 26),
	Insn('CHAR_FLAG1_SET', Char(26), 32768),
	Insn('CHAR_SET_POS', Char(26), (5500, 330, 4300), 0),
	Insn('CHAR_FLAG1_UNSET', Char(26), 128),
	Insn('CHAR_FLAG2_UNSET', Char(26), 32768),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#12100312V#0013F──恐吓信！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('BGM_PLAY', b'o\x00\x00'),
	Insn('CAM_DISTANCE', 23000, 1500),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(21), Text(
		'#12100313V#1P#1803F是的……是一周前的事。{wait}'
		'{page}'
		'#12100314V伊莉雅小姐收到了\n'
		'一封寄信人不明的信……{wait}'
		'{page}'
		'#12100315V#1805F啊，伊莉雅小姐就是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100316V#0303F拥有『炎之舞姬』的称号，\n'
		'彩虹剧团的超级大明星。{wait}'
		'{page}'
		'#12100317V#0301F在国际上都有着极高知名度的\n'
		'红牌女演员，顶级艺术家。{wait}'
		'{page}'
		'#12100318V#0309F呀呀～！\n'
		'真没想到，居然是要商量有关\n'
		'伊莉雅丄普拉提耶的事啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 1700, (8, 9, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100319V#12P#0203F兰迪前辈……\n'
		'请稍微冷静一点。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100320V#11P#0003F那个，毕竟是名人，\n'
		'所以名字我们还是知道的……{wait}'
		'{page}'
		'#12100321V#0001F不过……\n'
		'那恐吓信是发给她的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#12100322V#1P#1803F是的……虽然她本人\n'
		'说这只是恶作剧而已……{wait}'
		'{page}'
		'#12100323V但总觉得信中的措辞有些诡异……\n'
		'似乎并不像是普通的恶作剧呢。{wait}'
		'{page}'
		'#12100324V#1801F然后，我和剧团长讨论了一下，\n'
		'最后决定还是找警察商量。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100325V#6P#0101F……那封恐吓信现在在谁手里呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#12100326V#1P#1806F那个……\n'
		'在伊莉雅小姐自己手中。{wait}'
		'{page}'
		'#12100327V她本打算马上就扔掉的，\n'
		'但总算是被我们阻止了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100328V#11P#0003F既然如此，我们首先还是\n'
		'应该亲眼看看那封恐吓信吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100329V#11P#0005F对了……\n'
		'你是叫莉夏吧。{wait}'
		'{page}'
		'#12100330V#0000F想必你是《彩虹剧团》的\n'
		'工作人员吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(21), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(21), Text(
		'#12100331V#1P#1802F啊，是的。\n'
		'算是剧团的演员吧。{wait}'
		'{page}'
		'#12100332V#1809F不过……\n'
		'我还只是个新人而已。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100333V#0305F#4S哎！！啊啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(21), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(21), 0),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(259), 2),
	Insn('SLEEP', 50),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100334V#5P#0011F怎、怎么了啊，从刚才开始就一直大呼小叫的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100335V#0301F我、我在新剧特辑页中\n'
		'看见过你！{wait}'
		'{page}'
		'#12100336V#0303F你是与伊莉雅扮演的『太阳之姬』演对手戏的，\n'
		'扮演『月之姬』的第二主角……{wait}'
		'{page}'
		'#12100337V#0302F由伊莉雅丄普拉提耶亲自破格提拔，\n'
		'如彗星一般突然闪现的超级新人！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(21), 0, 1700, (40, 43, 100, 3)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(21), Text(
		'#12100338V#1P#1805F没、没那回事，我并不算什么超级新人。{wait}'
		'{page}'
		'#12100339V#1806F我的练习还远远不够呢……\n'
		'总是拖大家的后腿。{wait}'
		'{page}'
		'#12100340V#1808F要想正式登台出道，\n'
		'我觉得自己还需要多加磨练呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100341V#6P#0109F呵呵，那也很厉害了啊。{wait}'
		'{page}'
		'#12100342V#0102F竟然能被彩虹剧团所选拔，\n'
		'并在出道时就出演这么重要的角色。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#12100343V#1P#1806F唔唔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100344V#11P#0004F哈哈……我们已经了解大致情况了。{wait}'
		'{page}'
		'#12100345V#0001F不过，据你所说，\n'
		'伊莉雅小姐本人好像\n'
		'并不在意这件事吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#12100346V#1P#1808F是的……而且她说，\n'
		'为了提高舞台表演的完成度，现在要\n'
		'专心排练，所以不想让无关人员前去打扰……{wait}'
		'{page}'
		'#12100347V#1806F特别是，那个……\n'
		'特别是警察，更是绝对免谈……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100348V#11P#0011F那个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100349V#12P#0211F那就是说，我们好像\n'
		'也没有什么能做的了吧……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#12100350V#1P#1802F不、不过，各位不是\n'
		'『特务支援课』的吗？{wait}'
		'{page}'
		'#12100351V从杂志上的报道来看，\n'
		'你们与普通警察相比，\n'
		'似乎更加亲和近民吧……{wait}'
		'{page}'
		'#12100352V#1809F这样一来，伊莉雅小姐\n'
		'或许也可以接受了吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100353V#11P#0003F嗯、嗯……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100354V#6P#0100F虽然这话由我们来说似乎不太合适……\n'
		'不过，你们没有和游击士协会那边沟通吗？{wait}'
		'{page}'
		'#12100355V伊莉雅小姐属于民间人士……\n'
		'我想应该属于他们的保护对象吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#12100356V#1P#1808F这、这个嘛……{wait}'
		'{page}'
		'#12100357V#1803F因为游击士协会在克洛斯贝尔\n'
		'也相当受欢迎……{wait}'
		'{page}'
		'#12100358V如果那些备受关注的人在公演之前频繁进出剧团，\n'
		'恐怕会引起一些奇怪的传闻吧……{wait}'
		'{page}'
		'#12100359V#1802F出于这种考虑，我认为如果是各位，\n'
		'大概就不会引起那么大的话题……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('EMOTE', Char(21), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(21), 0, 1700, (40, 43, 100, 3)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(21), Text(
		'#12100360V#1P#1801F啊！对、对不起！\n'
		'我竟然说了如此失礼的话……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100361V#11P#0012F没、没什么，\n'
		'我们完全没有在意啦。{wait}'
		'{page}'
		'#12100362V#0000F总而言之……\n'
		'事情的大致情况，我们已经了解了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100363V#5P#0000F……这个委托，我觉得\n'
		'还是受理比较好，\n'
		'各位，你们怎么想？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100364V#6P#0102F我当然赞成啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100365V#12P#0204F我也没有异议。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100366V#0309F哈，这还用说，\n'
		'当然没有拒绝的理由吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100367V#11P#0004F就是这样了，莉夏小姐。{wait}'
		'{page}'
		'#12100368V#0000F有关恐吓信的委托，就由我们\n'
		'特务支援课正式受理了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(21), 1),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(21), Text(
		'#12100369V#1P#1802F非、非常感谢！{wait}'
		'{page}'
		'#12100370V#1809F那我就……\n'
		'先回剧团了。{wait}'
		'{page}'
		'#12100371V我会提前去向剧团长和\n'
		'伊莉雅小姐报告的，\n'
		'所以各位可以随时来访。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100372V#6P#0102F嗯，明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100373V#0309F下次见啊～小莉夏！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('SLEEP', 300),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(21), 30),
	Insn('CHAR_SET_FRAME', Char(21), 0),
	Insn('CHAR_SET_POS', Char(21), (4900, 30, 5500), 180),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 1638, 0, 255, 100),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (3000, 950, 1800), 3500),
	Insn('FORK', 21, 1, [
		Insn('0x95', Char(254), (3600, 30, 5500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(21), 1),
	Insn('FORK', 21, 1, [
		Insn('0x95', Char(254), (1000, 0, 1200), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('CHAR_SET_FRAME', Char(259), 1),
	Insn('SLEEP', 500),
	Insn('CHAR_SET_FRAME', Char(258), 1),
	Insn('FORK_AWAIT', Char(21), 1),
	Insn('FORK', 21, 1, [
		Insn('0x95', Char(254), (1000, 0, -1000), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('FORK', 21, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(21), 1),
	Insn('FORK_AWAIT', Char(21), 2),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('CHAR_FLAG1_SET', Char(21), 128),
	Insn('CHAR_FLAG2_SET', Char(21), 32768),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 500),
	Insn('CAM_OFFSET', (6060, 950, 4530), 1600),
	Insn('SLEEP', 500),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100375V#5P#0003F那么……\n'
		'总之我们就去剧团看看吧。{wait}'
		'{page}'
		'#12100376V#0000F如果不亲眼对恐吓信进行确认，\n'
		'调查也就无法展开呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100377V#12P#0204F是啊。{wait}'
		'{page}'
		'#12100378V#0202F而且，那也许只是一起恶作剧而已，\n'
		'这种可能性也不能否认……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100379V#0302F呀～不过还真是赚到了啊！{wait}'
		'{page}'
		'#12100380V竟然得到了在公演开始之前\n'
		'进入彩虹剧团的机会呢！{wait}'
		'{page}'
		'#12100381V#0309F而且还能见到伊莉雅本人啊！是伊莉雅本人哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100382V#6P#0108F确实如此……\n'
		'说不定要和那个伊莉雅丄普拉提耶小姐\n'
		'面对面地直接对话呢。{wait}'
		'{page}'
		'#12100383V#0106F还真是有点紧张起来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100384V#5P#0005F有、有那么紧张吗？{wait}'
		'{page}'
		'#12100385V#0006F嗯～不过，从杂志上来看，\n'
		'她确实是个美人……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100386V#12P#0202F……稍微有些期待哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('BGM_STOP', 2000),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'd\x00\x00'),
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
	Insn('CHAR_FLAG1_SET', Char(25), 128),
	Insn('CHAR_FLAG2_SET', Char(25), 32768),
	Insn('CHAR_FLAG1_SET', Char(26), 128),
	Insn('CHAR_FLAG2_SET', Char(26), 32768),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0xD5', 33),
	Insn('0xD5', 34),
	Insn('0xD5', 35),
	Insn('CAM_OFFSET', (3000, 1030, 4300), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 340, 0),
	Insn('CAM_DISTANCE', 27500, 0),
	Insn('CHAR_SET_POS', Char(0), (3000, 0, 4300), 270),
	Insn('CHAR_SET_POS', Char(1), (3000, 0, 4300), 270),
	Insn('CHAR_SET_POS', Char(2), (3000, 0, 4300), 270),
	Insn('CHAR_SET_POS', Char(3), (3000, 0, 4300), 270),
	Insn('FLAG_SET', Flag(1026)),
	Insn('QUEST', 66, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 66, Insn('TASK_SET', 0)),
	Insn('QUEST', 65, Insn('TASK_SET', 3)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][33] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50120', 30),
	Insn('CAM_OFFSET', (64000, 1100, 8600), 0),
	Insn('CAM_ROTATE', 50, 17, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(257), (63600, 0, 6700), 0),
	Insn('CHAR_SET_POS', Char(258), (64300, 0, 6700), 0),
	Insn('CHAR_SET_POS', Char(259), (63200, 0, 5400), 0),
	Insn('CHAR_SET_POS', Char(260), (64500, 0, 5400), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(8), (64000, 150, 11400), 180),
	Insn('CHAR_SET_CHCP', Char(8), 4),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_SET_CHCP', Char(12), 5),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('0x4B', Char(12), -1),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG2_UNSET', Char(12), 32768),
	Insn('CHAR_SET_POS', Char(12), (61600, 30, 8000), 225),
	Insn('EXPR_CHAR_ATTR', Char(12), 36, Expr([Insn('CONST', 183), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(12), 7, Expr([Insn('CONST', 1800), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(12), 52, Expr([Insn('CONST', 1800), Insn('SET'), Insn('END')])),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu01000.itp'),
	Insn('CAM_DISTANCE', 24000, 1500),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 500),
	Insn('TEXT_MESSAGE', Char(8), Text(
		'#12101488V原来如此……\n'
		'好啦，情况我已经基本知道了。{wait}'
		'{page}'
		'#12101489V然后呢？\n'
		'你们准备忍气吞声，就此罢手吗？{wait}'
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
		'#12101490V#12P#0006F你、你说忍气吞声……{wait}'
		'{page}'
		'#12101491V#0001F一课都已经出动了，\n'
		'以我们的立场来说，\n'
		'不也只能选择退让了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#12101492V#5P#1003F嗯，大概也只能如此了吧。{wait}'
		'{page}'
		'#12101493V#1000F不然的话，那个老狐狸副局长多半\n'
		'又要唠唠叨叨，对你们做出严重警告了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101494V#12P#0006F是啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101495V#12P#0200F那样的话，我们就提出申请，\n'
		'对一课进行协助如何？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101496V#0306F唔，从那个西装眼镜男的\n'
		'态度来看，这恐怕是很难的吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#12101497V#5P#1000F嗯，多半如此。{wait}'
		'{page}'
		'#12101498V#1003F警察的领地意识是很强的，\n'
		'一般都不希望别人插手自己的案子。{wait}'
		'{page}'
		'#12101499V特别是一课这种精英部门，\n'
		'像你们这种小鬼如果提出协助，\n'
		'肯定会被他们二话不说直接拒绝吧。{wait}'
		'{page}'
		'#12101500V#1002F──不过，如果你们暗中行事的话，\n'
		'那就另当别论了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101501V#12P#0011F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#12101502V#5P#1004F呵呵……我们特务支援课，\n'
		'从某种意义上来说，是属于编制之外的部门。{wait}'
		'{page}'
		'#12101503V虽然经常被总部排斥在外，\n'
		'但反过来说，也可以解释为\n'
		'拥有一定程度的自主裁量权。{wait}'
		'{page}'
		'#12101504V#1002F如果抓准这一点的话，\n'
		'我们就可以暗中行动，\n'
		'插足到其它部门的领域中。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101505V#12P#0005F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101506V#0305F喂喂……\n'
		'说这种话没问题吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101507V#12P#0211F真是个不良上司呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#12101508V#5P#1004F呵呵，我也说过的吧？{wait}'
		'{page}'
		'#12101509V我基本上是不会给你们提供什么帮助的，\n'
		'顶多出差错时负责收拾残局而已。{wait}'
		'{page}'
		'#12101510V#1002F真正需要下决心办案的还是你们自己。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101511V#12P#0008F…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#12101512V#5P#1003F不过，话虽如此，\n'
		'但看你们的样子，好像还是很勉强啊。{wait}'
		'{page}'
		'#12101513V#1000F毕竟在我们的团队中\n'
		'有一位迷茫不定的同伴啊。{wait}'
		'{page}'
		'#12101514V以现在的状态，还没法团结一心，\n'
		'做出重大决定吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101515V#12P#0006F……那个………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101516V#0306F算啦，看大小姐现在的样子，\n'
		'恐怕没办法在短时间内打起精神吧。{wait}'
		'{page}'
		'#12101517V#0308F总觉得，她的情绪好像\n'
		'相当低迷呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101518V#12P#0208F确实，感觉她今天一整天\n'
		'都是那种状态……{wait}'
		'{page}'
		'#12101519V#0206F……艾莉前辈，\n'
		'不要紧吧……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101520V#12P#0008F…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 500),
	Insn('CHAR_SET_CHCP', Char(12), 30),
	Insn('CHAR_SET_FRAME', Char(12), 4),
	Insn('SLEEP', 130),
	Insn('CHAR_SET_FRAME', Char(12), 3),
	Insn('SLEEP', 130),
	Insn('CHAR_SET_FRAME', Char(12), 2),
	Insn('SLEEP', 130),
	Insn('FORK', 12, 2, [
		Insn('0xA6', Char(254), 0, 30, 1000, 3000),
	]),
	Insn('SOUND_PLAY', 848, 0, 0, 100),
	Insn('CHAR_SET_FRAME', Char(12), 1),
	Insn('SLEEP', 1100),
	Insn('CHAR_SET_FRAME', Char(12), 2),
	Insn('SLEEP', 130),
	Insn('CHAR_SET_FRAME', Char(12), 3),
	Insn('SLEEP', 130),
	Insn('CHAR_SET_FRAME', Char(12), 4),
	Insn('SLEEP', 130),
	Insn('CHAR_SET_CHCP', Char(12), 5),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('SLEEP', 300),
	Insn('EMOTE', Char(12), 300, 1000, (28, 33, 250, 0)),
	Insn('SLEEP', 500),
	Insn('CAM_DISTANCE', 23500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 5000),
	Insn('BGM_WAIT'),
	Insn('0xB8', 513, 515),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('MINIGAME', 24, 0, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
	Insn('0x2F', b'\x01\x00'),
	Insn('0x2F', b'\x02\x00'),
	Insn('0x2F', b'\x03\x00'),
	Insn('FLAG_SET', Flag(738)),
	Insn('NEW_SCENE', 'c010b', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][34] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('CAM_OFFSET', (12600, 2350, 5600), 0),
	Insn('CAM_ROTATE', 40, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('CHAR_SET_CHCP', Char(259), 11),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_SET_CHCP', Char(260), 12),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_POS', Char(257), (13900, 900, 6650), 270),
	Insn('CHAR_SET_POS', Char(258), (13900, 900, 4600), 270),
	Insn('CHAR_SET_POS', Char(259), (11300, 900, 6650), 90),
	Insn('CHAR_SET_POS', Char(260), (11300, 900, 4600), 90),
	Insn('IMG_LOAD', ResId(0), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis121.itp'),
	Insn('CAM_OFFSET', (12600, 1850, 5600), 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200001V#0103F──不过，还真是奇怪啊。{wait}'
		'{page}'
		'#12200002V#0101F这次的事件，一课会采取行动\n'
		'看起来只是结果导致如此而已。{wait}'
		'{page}'
		'#12200003V因为要不是莉夏小姐不愿意闹出\n'
		'太大动静而来委托我们，\n'
		'估计他们根本就不会知道。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200004V#5P#0006F嗯～确实……{wait}'
		'{page}'
		'#12200005V#0008F也就是说，那并不是犯人为了\n'
		'混淆一课的视线而采取的策略吗……{wait}'
		'{page}'
		'#12200006V#0001F说起来，知道『银』的\n'
		'存在的人都有谁呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200007V#0103F这个嘛……身为其雇主的\n'
		'『黑月』当然不用说。{wait}'
		'{page}'
		'#12200008V还有一直与他们进行竞争的『鲁巴彻』\n'
		'和密切关注其动向的搜查一课……{wait}'
		'{page}'
		'#12200009V#0100F然后就是，和鲁巴彻有着密切\n'
		'关系的哈尔特曼议长应该也知道吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200010V#5P#0005F哈尔特曼议长……\n'
		'就是昨天说的那个？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200011V#0106F嗯，帝国派议员的领袖人物，\n'
		'在议会中拥有首脑级地位的大政治家。{wait}'
		'{page}'
		'#12200012V大概可以算是\n'
		'鲁巴彻的最大后盾了。{wait}'
		'{page}'
		'#12200013V#0101F顺便一提，外公的改革方案\n'
		'几乎全都是被这个人推翻的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200014V#5P#0008F是吗……\n'
		'我只是听说过他的名字而已。{wait}'
		'{page}'
		'#12200015V#0001F这样一来，对于『银』来说，\n'
		'他也属于敌对势力了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200016V#0106F嗯嗯……似乎没什么关联呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE', Char(257), 0, 1700, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 1700, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('SLEEP', 500),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200017V#11P#0005F缇欧、兰迪？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200018V#0105F#11P怎么了？\n'
		'为什么一脸若有所思的表情。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200019V#6P#0306F啊……那个，该怎么说呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200020V#6P#0202F艾莉前辈……\n'
		'你今天好像很有精神啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200021V#0105F#11P啊，那个……{wait}'
		'{page}'
		'#12200022V#0106F──对不起，\n'
		'昨天真是让大家担心了。{wait}'
		'{page}'
		'#12200023V#0100F不过，我已经没事了。\n'
		'绝对不会拖大家后腿的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200024V#5P#0003F那个，艾莉……\n'
		'不必说拖后腿这种见外的话啦。{wait}'
		'{page}'
		'#12200025V#0000F这段时间以来，我们不也都\n'
		'经常依靠你的各种帮助嘛。{wait}'
		'{page}'
		'#12200026V你看，现在也是，有艾莉在，\n'
		'推理的进展也都顺利很多。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200027V#0102F是、是吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200028V#6P#0301F……有问题。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200029V#6P#0211F……很可疑呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(257), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200030V#11P#0005F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200031V#0112F#11P等、等一下……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200032V#6P#0303F说起来，就在昨天晚上……\n'
		'我听到屋顶上传来了谈话声呢。{wait}'
		'{page}'
		'#12200033V#0302F莫非……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200034V#6P#0202F……原来如此。{wait}'
		'{page}'
		'#12200035V#0204F恭喜你们，\n'
		'罗伊德前辈、艾莉前辈。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (40, 43, 100, 0)),
	Insn('EMOTE', Char(258), 0, 1700, (40, 43, 100, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200036V#11P#0011F慢、慢着啊，有什么\n'
		'特别的事情需要恭喜吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200037V#0112F#11P对、对啊……{wait}'
		'{page}'
		'#12200038V#0113F我们只不过是随便\n'
		'谈了些各方面的事情而已……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200039V#6P#0302F原来如此，各方面的事情吗？{wait}'
		'{page}'
		'#12200040V#0309F──那，已经进展到什么程度了啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200041V#5P#0007F兰迪！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200042V#0112F#11P等、等一下啦！\n'
		'缇欧还在这里呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200043V#6P#0205F进展到什么程度……{wait}'
		'{page}'
		'#12200044V#0204F啊，我明白了，这是指在交往的过程中，\n'
		'需要一步一步逐渐进展到各个阶段──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 150),
	Insn('EMOTE', Char(257), 0, 1700, (40, 43, 100, 3)),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200045V#11P#0012F不对不对，没那回事啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200046V#6P#0309F咻～咻～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200047V#6P#0202F……咻～咻～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('0x82', 100, 0, 1000, 1500),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200048V#0109F#4S#90W#11P请 你 们 适 可 而 止 哦。#20W{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200049V#6P#0306F是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200050V#11P#0006F真是的……{wait}'
		'{page}'
		'#12200051V竟然会怀疑我和艾莉的关系，\n'
		'那种事情根本就不可能吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200052V#0105F#40W………哎…………#20W{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200053V#11P#0012F我们两个根本就不配啊，\n'
		'还是该说，完全不会有那种感觉呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200054V#5P#0000F对吧，艾莉？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200055V#0101F#70W…………………………………#20W{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200056V#5P#0005F……咦？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200057V#6P#0306F（喂喂……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200058V#6P#0211F（好像踩到地雷了呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200059V#0104F#40W……对啊，说得没错……{wait}'
		'{page}'
		'#12200060V那只是一次非常普通的谈话而已，完全就是\n'
		'麻烦你耐着性子听我说了一大堆无聊的话……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('0x82', 0, 100, 3000, 500),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200061V#0101F#4S说得没错，完全没有产生过什么\n'
		'甜蜜的氛围！一点都没有！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200062V#5P#0011F……那、那个……{wait}'
		'{page}'
		'#12200063V#0012F那个，我刚才说我们两个\n'
		'不配，意思其实是我\n'
		'配不上艾莉你……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200064V#0111F（瞪眼）……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200065V#5P#0006F……对不起。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200066V#6P#0309F呵呵呵……{wait}'
		'{page}'
		'#12200067V#0302F算了，不管这些啦，\n'
		'总之，能打起精神就是最好了，对吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200068V#0105F#11P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(259), 2),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200069V#6P#0204F……我也安心了。{wait}'
		'{page}'
		'#12200070V#0208F我还以为前辈会……\n'
		'会辞去警察的工作，\n'
		'离开我们呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200071V#0106F#11P……抱歉哦，让你担心了。{wait}'
		'{page}'
		'#12200072V#0102F虽然我还不知道\n'
		'将来的路该怎么走……{wait}'
		'{page}'
		'#12200073V但对于现在的我来说，最正确的\n'
		'选择就是留在这里，这是一定没错的。{wait}'
		'{page}'
		'#12200074V#0104F所以，就再一次……\n'
		'请大家多多关照吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200075V#5P#0002F艾莉……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200076V#6P#0202F……艾莉前辈。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200077V#6P#0309F哈哈，要是没有了大小姐的说教，\n'
		'就产生不了紧张感啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200078V#0111F#11P我之所以会说教，\n'
		'还不都是因为你们……{wait}'
		'{page}'
		'#12200079V#0103F──算啦，这都无所谓了。{wait}'
		'{page}'
		'#12200080V#0101F调查方针已经考虑过了吧，\n'
		'最后决定要怎么做呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200081V#5P#0003F这个嘛……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200082V#6P#0206F虽说是决定了要使用与\n'
		'一课不同的途径来接近『银』……{wait}'
		'{page}'
		'#12200083V但如今出现了这么多个切入点，\n'
		'反而让人有些迷惑了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200084V#6P#0303F既然如此，那就这样吧。{wait}'
		'{page}'
		'#12200085V#0300F我们就先去卡尔瓦德的\n'
		'东方人街看看，怎么样？{wait}'
		'{page}'
		'#12200086V这样一来，多少也能掌握一点\n'
		'关于『银』的线索吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200087V#5P#0005F这、这确实是个盲点呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200088V#0101F#11P不过，上层会批准我们\n'
		'去外国出差吗？{wait}'
		'{page}'
		'#12200089V似乎已经超过支援课的\n'
		'责任范畴了呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200090V#6P#0203F………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(259), 4),
	Insn('CHAR_SET_CHCP', Char(259), 255),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_SET_POS', Char(259), (10400, 850, 7600), 90),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('CAM_OFFSET', (16100, 1850, 10000), 3000),
	Insn('CAM_ROTATE', 7, 21, 0, 3000),
	Insn('CAM_DISTANCE', 25000, 3000),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (16100, 850, 10000), 2000, 0),
	]),
	Insn('SLEEP', 300),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SLEEP', 500),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('SLEEP', 500),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('0x6F', b'Q'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200091V#0005F缇欧……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200092V#0105F#5P怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200093V#0200F我想稍微调查一下\n'
		'警察局的数据库。{wait}'
		'{page}'
		'#12200094V或许能掌握到\n'
		'一课的动向呢……{wait}'
		'{page}'
		'#12200095V#0203F不过，昨天晚上才刚刚调查过，\n'
		'现在大概也不会有什么新情报。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200096V#0001F是吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200097V#1P#0300F哎，总比什么都不干好嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(257), 4),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('0x90', Char(257), (14800, 850, 7600), b'\x0e\x01'),
	Insn('CHAR_FLAG1_UNSET', Char(258), 4),
	Insn('CHAR_SET_CHCP', Char(258), 255),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('0x90', Char(258), (14800, 850, 5400), b'\x0e\x01'),
	Insn('CHAR_FLAG1_UNSET', Char(260), 4),
	Insn('CHAR_SET_CHCP', Char(260), 255),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('0x90', Char(260), (10400, 850, 5400), b'Z\x00'),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 36))),
	Insn('SLEEP', 100),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 35))),
	Insn('0x92', Char(257), 15200, 8500, 500),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (15200, 850, 8500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('SOUND_PLAY', 824, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200098V#0205F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200099V#6P#0001F怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200100V#0202F……真少见呢……{wait}'
		'{page}'
		'#12200101V好像有导力邮件\n'
		'发送过来了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200102V#6P#0005F导力邮件？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200103V#6P#0100F也就是发送到终端的\n'
		'文字类情报吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200104V#0206F是的，虽然非常便利，\n'
		'但在警察系统，却几乎没有人\n'
		'使用到这个功能……{wait}'
		'{page}'
		'#12200105V可能是因为目前会操作\n'
		'键盘的人太少了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200106V#6P#0006F原来如此……\n'
		'确实，我也不会用呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200107V#0300F先不说这些了，这到底是谁发的？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200108V#0202F我来打开看看。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 849, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200109V#0205F…………哎………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200110V#6P#0005F怎么了……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200111V#6P#0105F到底是谁啊──{wait}'
		'{page}'
		'#12200112V#0101F！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 72, 0, 0, 100),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_POS', -1, 130, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}此乃『银』之委托。\n'
		'越过试炼，至吾所在。\n'
		'如是，将授予汝等使命。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#12200113V#0007F这、这是……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(260), Text(
		'#12200114V#0307F喂喂……\n'
		'这是谁搞的恶作剧吧！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'#12200115V#0101F缇欧……\n'
		'这邮件是从哪里发来的！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#12200116V#0201F不是警察局总部……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('SOUND_PLAY', 849, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#12200117V#0205F……找到了。{wait}'
		'{page}'
		'#12200118V#0203F『克洛斯贝尔国际银行』\n'
		'（International Bank of Crossbell）……{wait}'
		'{page}'
		'#12200119V#0201F──通称ＩＢＣ。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200120V#6P#0013F……怎么回事……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200121V#0301FＩＢＣ的话，也就是那个\n'
		'汇聚了整个大陆的米拉的银行吧？{wait}'
		'{page}'
		'#12200122V这种恶作剧邮件\n'
		'为什么会从那种地方发来呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200123V#0206F……问我也没用啊。{wait}'
		'{page}'
		'#12200124V#0201F不过，这封邮件确实是从\n'
		'ＩＢＣ的终端发来的，肯定没错。{wait}'
		'{page}'
		'#12200125V虽然并不知道发信人是谁。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200126V#6P#0008F莫非，『银』已经潜入到\n'
		'ＩＢＣ中了吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(258), 315, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200127V#12P#0103F说实话，这也并非完全不可能啊。{wait}'
		'{page}'
		'#12200128V#0101F而且ＩＢＣ的大楼内\n'
		'也入驻了好几家外部公司。{wait}'
		'{page}'
		'#12200129V好像……连爱普斯泰恩财团的\n'
		'事务所也在那里面吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(259), Char(258), 500),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200130V#0203F是的……\n'
		'我的熟人就在那里工作。{wait}'
		'{page}'
		'#12200131V#0200F可是……这封邮件似乎\n'
		'是从ＩＢＣ的主终端\n'
		'发送来的。{wait}'
		'{page}'
		'#12200132V我想，和外部公司产生关联的\n'
		'可能性应该很低……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200133V#6P#0006F……那就只能直接去问问看了吧。{wait}'
		'{page}'
		'#12200134V虽说我们要尽量在瞒着一课的\n'
		'前提下展开调查……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(260), Char(257), 500),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200135V#0306F但如果我们不公开身份，\n'
		'恐怕很难在那里进行询问工作啊。{wait}'
		'{page}'
		'#12200136V#0300F不过，总之必须要在某些人\n'
		'横插一腿之前赶快行动，对吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200137V#12P#0103F……………………………………{wait}'
		'{page}'
		'#12200138V#0100F……说不定，\n'
		'ＩＢＣ会允许我们进行秘密调查呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(257), 135, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200139V#5P#0005F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200140V#0205F要怎么做呢……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200141V#12P#0104F……我有个朋友\n'
		'是ＩＢＣ的相关人员哦。{wait}'
		'{page}'
		'#12200142V#0100F如果和她父亲说清楚事情经过的话，\n'
		'或许可以得到一些协助吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200143V#5P#0000F原来如此啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200144V#0309F#5P噢噢，这可真是及时雨啊。{wait}'
		'{page}'
		'#12200145V#0300F不愧是大小姐，\n'
		'关系网真广啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200146V#12P#0104F呵，普普通通啦。{wait}'
		'{page}'
		'#12200147V#0108F不过，她的父亲可是个大忙人，\n'
		'而且还不知道现在是否在克洛斯贝尔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200148V#0200F他到底是什么身份呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200149V#12P#0103F……我想你们大概听说过他。{wait}'
		'{page}'
		'#12200150V#0100F他的名字是迪塔丄库罗伊斯。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200151V#5P#0005F哎！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200152V#0205F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200153V#0305F#5P什么啊，他很有名吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200154V#5P#0000F啊，那个……{wait}'
		'{page}'
		'#12200155V#0003F从某种意义上来说，他的知名度\n'
		'或许和伊莉雅小姐不相上下呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200156V#0204F迪塔丄库罗伊斯……{wait}'
		'{page}'
		'#12200157V大陆中首屈一指的资产家，\n'
		'国际经济界的中心人物之一……{wait}'
		'{page}'
		'#12200158V#0202F也是ＩＢＣ的现任总裁，没错吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200159V#0307F#5P哦哦，原来是银行的首脑啊！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200160V#12P#0104F他是我爸爸以前的老朋友。{wait}'
		'{page}'
		'#12200161V和我外公也是早有往来，关系甚好，\n'
		'所以我才能与他熟识的……{wait}'
		'{page}'
		'#12200162V#0102F他的女儿和我也是童年的玩伴呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200163V#5P#0002F原来如此啊……{wait}'
		'{page}'
		'#12200164V#0006F不过，像那种日理万机的人……\n'
		'不在自治州内也是常有的事啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200165V#12P#0106F嗯……一年之中，他似乎有\n'
		'大半时间都在国外奔波忙碌呢。{wait}'
		'{page}'
		'#12200166V#0101F不过，就算白跑一趟，也没什么损失啊。{wait}'
		'{page}'
		'#12200167V而且我的朋友应该在的。\n'
		'即使只是去拜访一下也好，总之就过去看看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12200168V#5P#0000F嗯，就这么办吧。{wait}'
		'{page}'
		'#12200169V#0003F不过，虽然这样一来，\n'
		'调查的目标是已经确定了，可是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12200170V#0206F……邮件的用意还不能确定，对吧？{wait}'
		'{page}'
		'#12200171V#0201F恐吓信也是一样，\n'
		'发信人的目的究竟是什么呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12200172V#0302F#5P算了，难得对方特意\n'
		'与我们主动接触。{wait}'
		'{page}'
		'#12200173V我们就大胆迎上去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12200174V#12P#0104F是啊……{wait}'
		'{page}'
		'#12200175V#0100F出发吧，目标是ＩＢＣ大楼。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('BGM_STOP', 2000),
	Insn('CAM_OFFSET', (15000, 1850, 8900), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 340, 0),
	Insn('CAM_DISTANCE', 27500, 0),
	Insn('CHAR_SET_POS', Char(0), (15000, 850, 8900), 45),
	Insn('CHAR_SET_POS', Char(1), (15000, 850, 8900), 45),
	Insn('CHAR_SET_POS', Char(2), (15000, 850, 8900), 45),
	Insn('CHAR_SET_POS', Char(3), (15000, 850, 8900), 45),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('CHAR_SET_POS', Char(0), (15000, 850, 8900), 45),
	Insn('FLAG_SET', Flag(1040)),
	Insn('0xC7', b'\x01\x00\x10\x00\x00'),
	Insn('QUEST', 67, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 67, Insn('TASK_SET', 0)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 15, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 15, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 15, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 15, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 15, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'd\x00\x00'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][35] = [
	Insn('SLEEP', 500),
	Insn('CHAR_ROTATE', Char(258), 0, 500),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (16400, 850, 7900), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('RETURN'),
]

data['code'][36] = [
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (10400, 850, 8600), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (14400, 850, 9900), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('CHAR_ROTATE', Char(260), 90, 500),
	Insn('RETURN'),
]

data['code'][37] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'apl/ch50091', 31),
	Insn('CAM_OFFSET', (5500, 900, 4200), 0),
	Insn('CAM_ROTATE', 37, 17, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 23000, 0),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_CHCP', Char(259), 11),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_SET_CHCP', Char(260), 12),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_SET_POS', Char(257), (5500, 130, 6250), 180),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_SET_POS', Char(259), (4900, 130, 2200), 0),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_POS', Char(260), (6000, 130, 2200), 0),
	Insn('CHAR_FLAG1_SET', Char(258), 8),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG2_UNSET', Char(12), 32768),
	Insn('CHAR_SET_CHCP', Char(12), 5),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('CHAR_SET_POS', Char(12), (3000, 0, 2500), 225),
	Insn('CHAR_FLAG1_UNSET', Char(12), 1),
	Insn('FORK_FUNC', Char(12), 3, Function((0, 0))),
	Insn('CHAR_SET_CHCP', Char(40), 31),
	Insn('CHAR_SET_FRAME', Char(40), 29),
	Insn('CHAR_FLAG1_SET', Char(40), 32768),
	Insn('CHAR_SET_POS', Char(40), (5300, 350, 4500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(40), 128),
	Insn('CHAR_FLAG2_UNSET', Char(40), 32768),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 18, 0, 0, 100),
	Insn('0xBB', b'\xbf\x02\xff\x00'),
	Insn('SLEEP', 500),
	Insn('BGM_PLAY', b'n\x00\x00'),
	Insn('CAM_DISTANCE', 24000, 2000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12201710V#4P#0306F哎呀……\n'
		'事态扩大了呢。{wait}'
		'{page}'
		'#12201711V#0301F眼下，恐怕大部分市民\n'
		'都已经陷入骚乱了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12201712V#12P#0206F这也没办法啊，在彩虹剧团的\n'
		'新剧首次公开的过程中，\n'
		'竟然发生了暗杀市长未遂的事件……{wait}'
		'{page}'
		'#12201713V#0211F丑闻这个词汇的意义，我想在此时\n'
		'已经发挥到了极致吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12201714V#5P#0006F同情市长的意见占到了多数，\n'
		'倒还算是不幸中的万幸……{wait}'
		'{page}'
		'#12201715V#0008F不过，和阿奈斯特有关的那个\n'
		'帝国派议员，到最后也没有被曝光姓名呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12201716V#4P#0303F当然，报社一定被下了封口令吧。{wait}'
		'{page}'
		'#12201717V#0301F而且，再怎么说，这次暗杀未遂事件的\n'
		'主要起因还在于那个混蛋秘书自己发疯吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12201718V#5P#0003F嗯……多半如此。{wait}'
		'{page}'
		'#12201719V#0001F对帝国派而言，\n'
		'暗杀市长这种事情并不会\n'
		'给他们带来什么好处……{wait}'
		'{page}'
		'#12201720V#0008F只是，共和国派与『黑月』有所瓜葛，\n'
		'所以只要将暗杀者的嫌疑推到『银』头上，\n'
		'就能成为针对共和国派的攻击材料了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12201721V#4P#0305F原来如此啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12201722V#12P#0208F可是，那个秘书……\n'
		'总觉得他的样子很奇怪呢。{wait}'
		'{page}'
		'#12201723V#0201F该说是一时冲动、失去理智……\n'
		'还是已经听不进人说话了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12201724V#5P#0006F嗯……我也很在意呢。{wait}'
		'{page}'
		'#12201725V#0001F据说一课已经审问过他了，\n'
		'最后的结果如何呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(8), 8),
	Insn('CHAR_SET_POS', Char(8), (16500, 850, 3700), 270),
	Insn('TEXT_TALK2', Char(8), Translate('男人的声音'), Text(
		'#12201726V──似乎是精神完全错乱，\n'
		'已经陷入无法正常对话的状态了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_FLAG1_UNSET', Char(8), 8),
	Insn('CHAR_FLAG1_UNSET', Char(8), 4),
	Insn('CAM_OFFSET', (14500, 1850, 3700), 2000),
	Insn('CAM_DISTANCE', 23500, 2000),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(260), 2),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(259), 2),
	Insn('0x6F', b'\x11'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12201727V#0005F课长……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(8), 0, 500),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (16500, 850, 9100), 2000, 0),
	]),
	Insn('SLEEP', 1000),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (6500, 900, 5000), 0),
	Insn('CAM_ROTATE', 37, 17, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 24000, 0),
	Insn('CAM_OFFSET', (4500, 900, 5000), 3000),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('FORK_QUIT', Char(8), 1),
	Insn('CHAR_SET_POS', Char(8), (4500, 850, 9100), 270),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (2500, 850, 9100), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (2500, 0, 5000), 2000, 0),
	]),
	Insn('SLEEP', 700),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('SLEEP', 300),
	Insn('CHAR_SET_FRAME', Char(259), 1),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('CHAR_ROTATE', Char(8), 90, 500),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12201728V#11P#0301F精神状态已经混乱\n'
		'到了没法接受审问的程度吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#12201729V#6P#1003F嗯，审问工作一无所获，\n'
		'所以暂时将他送到拘留所去了。{wait}'
		'{page}'
		'#12201730V#1000F据说是打算去\n'
		'请教会的精神问题专家或\n'
		'乌尔斯拉医院的相关人员来帮忙。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12201731V#5P#0006F是吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#12201732V#6P#1002F呵呵，不过你们\n'
		'还真是立了大功哦。{wait}'
		'{page}'
		'#12201733V今天去总部的时候，\n'
		'连那个老狐狸都满脸\n'
		'堆笑地表扬你们呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12201734V#5P#0011F哎……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12201735V#12P#0211F这场面真是难以想像呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12201736V#11P#0306F就算听到这种消息，\n'
		'也完全高兴不起来啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#12201737V#6P#1003F不光是老狐狸一个人，\n'
		'全体警察都在夸奖你们呢。{wait}'
		'{page}'
		'#12201738V#1002F哈，至于一课那边的人，心情大概会有些\n'
		'复杂吧，不过这样一来，他们肯定也会对\n'
		'你们有少许改观，这是毫无疑问的。{wait}'
		'{page}'
		'#12201739V你们就坦率一点，表现得开心些吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12201740V#5P#0000F说得……也对啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12201741V#12P#0208F不过……\n'
		'说心里话，还真是开心不起来呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12201742V#11P#0303F是啊……\n'
		'只要一想到大小姐此刻的心情……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 24500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 523), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_UNSET', Char(257), 4),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_FLAG1_UNSET', Char(259), 4),
	Insn('CHAR_SET_CHCP', Char(259), 255),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_FLAG1_UNSET', Char(260), 4),
	Insn('CHAR_SET_CHCP', Char(260), 255),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('CHAR_FLAG1_UNSET', Char(258), 8),
	Insn('CHAR_FLAG1_SET', Char(40), 128),
	Insn('CHAR_FLAG2_SET', Char(40), 32768),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'c0300', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][38] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('MINIGAME', 24, 0, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('LOAD_CHCP', 'apl/ch50090', 32),
	Insn('LOAD_CHCP', 'chr/ch05000', 33),
	Insn('LOAD_CHCP', 'chr/ch08201', 34),
	Insn('LOAD_CHCP', 'apl/ch50380', 35),
	Insn('LOAD_CHCP', 'apl/ch50092', 36),
	Insn('CAM_OFFSET', (258000, 700, 68700), 0),
	Insn('CAM_ROTATE', 40, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_SET_CHCP', Char(10), 33),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('CHAR_SET_POS', Char(10), (256399, 0, 68100), 180),
	Insn('CHAR_SET_POS', Char(259), (254900, 0, 68100), 90),
	Insn('CHAR_SET_POS', Char(258), (256399, 0, 66600), 0),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG2_UNSET', Char(12), 32768),
	Insn('CHAR_SET_CHCP', Char(12), 5),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('CHAR_SET_POS', Char(12), (255400, 30, 71000), 180),
	Insn('FORK_LOOP', 12, 1, [
		Insn('0xA0', Char(254), 1500, 64256),
	]),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu01109.itp'),
	Insn('IMG_LOAD', ResId(2), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis158.itp'),
	Insn('OBJ_FLAG_UNSET', Object(14), 4),
	Insn('OBJ_SET_FRAME', Object(255), 'tanmatu_add', Insn('0', 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}──１周过去了。{wait}'
		'{page}'
		'救出琪雅的罗伊德一行人\n'
		'将她藏匿在了特务支援课的大楼内，\n'
		'并随时警戒着黑手党们前来报复。{wait}'
		'{page}'
		'通过警察局总部的监视，外加约纳的情报网，大家随时\n'
		'都在密切注意着黑手党与哈尔特曼议长的动向，\n'
		'日子就这么一天天过去……{wait}'
		'{page}'
		'而另一方面，虽然记忆还没有恢复，\n'
		'但琪雅却没有表现出丝毫不安，\n'
		'反而很快就和支援课的成员们混熟了。{wait}'
		'{page}'
		'接下来──{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('EMOTE', Char(258), 0, 2000, (38, 39, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 39, 250, 0)),
	Insn('BGM_PLAY', b'n\x00\x00'),
	Insn('CAM_OFFSET', (257000, 700, 68700), 2000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 39))),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (255800, 0, 68100), 2000, 0),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 10, 2, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('EMOTE', Char(10), 0, 1700, (8, 9, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('SLEEP', 1500),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (254900, 0, 68100), 1000, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 10, 2, [
		Insn('CHAR_ROTATE', Char(10), 90, 800),
	]),
	Insn('FORK_AWAIT', Char(10), 2),
	Insn('FORK', 10, 2, [
		Insn('CHAR_ROTATE', Char(10), 271, 800),
	]),
	Insn('FORK_AWAIT', Char(10), 2),
	Insn('EMOTE', Char(10), 0, 1700, (10, 11, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 39))),
	Insn('CAM_OFFSET', (256000, 700, 68700), 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('FORK_QUIT', Char(258), 255),
	Insn('FORK_QUIT', Char(10), 255),
	Insn('CHAR_SET_CHCP', Char(10), 1),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('OBJ_FLAG_SET', Object(14), 4),
	Insn('CAM_OFFSET', (64000, 1100, 6900), 0),
	Insn('CAM_ROTATE', 50, 17, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_SET_POS', Char(8), (65300, 0, 6900), 270),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_SET_POS', Char(257), (62700, 0, 6300), 90),
	Insn('CHAR_SET_POS', Char(260), (62700, 0, 7500), 90),
	Insn('SLEEP', 1000),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#13600001V#0005F──停战吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('CAM_DISTANCE', 24000, 1500),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600002V#1003F#11P嗯，虽然并不是正式声明，\n'
		'但听说鲁巴彻向警察局总部传达了这个意向。{wait}'
		'{page}'
		'#13600003V#1001F那个孩子之所以会混在拍卖商品中，\n'
		'完全是因为某些地方出了差错──也就是说，\n'
		'他们对那孩子的事情也是一无所知。{wait}'
		'{page}'
		'#13600004V#1006F虽然他们主张说这一切都是『黑月』布的局，\n'
		'不过，就现阶段而言，这个说法也许很难成立吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600005V#6P#0006F……是啊。{wait}'
		'{page}'
		'#13600006V#0001F我们闯进去的时候，\n'
		'刚好看到『银』打倒了房间中的黑手党部下，\n'
		'时机非常巧。{wait}'
		'{page}'
		'#13600007V我想他应该并没有把琪雅从外面带进来，\n'
		'并同箱子里的人偶进行调包的时间。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1355)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600008V#6P#0306F也就是说，在那个箱子\n'
				'刚被搬运到宅子里时，\n'
				'里面的东西就已经被掉过包了吧。{wait}'
				'{page}'
				'#13600010V#0301F话说，那个本来应该被展出的\n'
				'人偶是从哪里来的呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600009V#6P#0306F也就是说，在那个箱子\n'
				'刚被搬运到宅子里时，\n'
				'里面的东西就已经被掉过包了吧。{wait}'
				'{page}'
				'#13600010V#0301F话说，那个本来应该被展出的\n'
				'人偶是从哪里来的呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600011V#1003F#11P具体的情况我也不清楚，\n'
		'但好像是通过雷米菲利亚那边的\n'
		'地下交易而获得的。{wait}'
		'{page}'
		'#13600012V#1001F好像是在纪念庆典的最终日──\n'
		'也就是拍卖会的当天\n'
		'才被送到议长宅邸里的……{wait}'
		'{page}'
		'#13600013V他们还主张说，那个运送公司\n'
		'也是个徒有空壳的虚构公司。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600014V#6P#0011F这怎么可能……{wait}'
		'{page}'
		'#13600015V#0010F也就是说，那些家伙坚决\n'
		'主张自己是完全的受害者吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600016V#1003F#11P呵，就是这么回事。{wait}'
		'{page}'
		'#13600017V虽然还不清楚那些主张是真是假……\n'
		'但他们肯定要拼命辩解就是了。{wait}'
		'{page}'
		'#13600018V#1001F──因为要是处理不妥，\n'
		'可就要背上『贩卖人口』的嫌疑了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600019V#6P#0008F…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13600020V#6P#0303F武器走私、洗黑钱、\n'
		'连违法赃物都可拍卖的地下拍卖会……{wait}'
		'{page}'
		'#13600021V#0301F连这些犯罪行为都可以轻松为之的\n'
		'家伙们，却唯独害怕贩卖人口的罪行，\n'
		'无论如何也想拼命洗刷自己的嫌疑啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600022V#1001F#11P这也是理所当然的吧。{wait}'
		'{page}'
		'#13600023V#1003F人口交易属于最恶劣的罪行……\n'
		'是绝对不会被原谅的重罪。{wait}'
		'{page}'
		'#13600024V所以警察无论如何都不会再坐视不理，\n'
		'而且，如果消息传到游击士协会那里，\n'
		'恐怕他们也会倾尽全力来进行制裁吧。{wait}'
		'{page}'
		'#13600025V#1000F──这也是为了不让其标志徽章『支援之手甲』蒙灰。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600026V#6P#0006F这么巨大的风险，议长就不用说了，\n'
		'即使是鲁巴彻也无法承担……{wait}'
		'{page}'
		'#13600027V#0001F──虽然道理上明白，\n'
		'但说实话，我还是很难接受呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600028V#1003F#11P嗯，所以才更要暂时休战啊。{wait}'
		'{page}'
		'#13600029V#1000F关于你们的潜入调查──\n'
		'依那边的主张来说就是非法入侵。\n'
		'总之，他们可以从此不再追究。{wait}'
		'{page}'
		'#13600030V而你们『偶然』救出的那名少女，\n'
		'他们也同意完全交给我们来负责。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13600031V#6P#0306F作为代价，对于这次的事件，\n'
		'就要认同他们的主张吧……{wait}'
		'{page}'
		'#13600032V而且绝对不能对游击士协会\n'
		'透露半点风声，没错吧？{wait}'
		'{page}'
		'#13600033V#0300F哎呀呀，他们确实很拼命呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600034V#6P#0008F……………………………………{wait}'
		'{page}'
		'#13600035V#0006F……虽然一想到琪雅所受的对待，\n'
		'就无法认同这种暧昧不清的处理办法……{wait}'
		'{page}'
		'#13600036V#0000F但只要能保证那个孩子今后\n'
		'不会再成为那些黑手党的目标，\n'
		'我们或许还是应该接受吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600037V#1002F#11P嗯，我也这么想。{wait}'
		'{page}'
		'#13600038V#1003F……不过呢，最关键的\n'
		'问题还是那个孩子的身份。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600039V#6P#0006F嗯……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13600040V#6P#0306F除了名字之外，\n'
		'她好像什么都不记得呢。{wait}'
		'{page}'
		'#13600041V#0302F──不过呢，\n'
		'性格倒是很开朗活泼，\n'
		'总之是个很愿意与人亲近的小鬼。{wait}'
		'{page}'
		'#13600042V总觉得才过了很短时间，\n'
		'她就和我们所有人都混熟了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600043V#6P#0014F哈哈……确实如此。{wait}'
		'{page}'
		'#13600044V#0002F赛特就不用说了，\n'
		'她和课长都很亲近呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600045V#1004F#11P哈哈，还好吧。{wait}'
		'{page}'
		'#13600046V#1002F因为我抽烟，所以\n'
		'小孩一般都不会靠近我……{wait}'
		'{page}'
		'#13600047V但她好像一点都不在意呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13600048V#6P#0302F大小姐和小缇简直就像是\n'
		'对这小鬼着了迷似地……{wait}'
		'{page}'
		'#13600049V今天还去了百货\n'
		'给她买一大堆衣服回来呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600050V#6P#0004F哈哈，这种时候有\n'
		'女性成员在，可真是得救了呢。{wait}'
		'{page}'
		'#13600051V有些事情，我们男人\n'
		'无论如何也都做不好呢……{wait}'
		'{page}'
		'#13600052V#0008F不过……\n'
		'她到底是哪里的孩子呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('BGM_STOP', 4000),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (59700, 900, 3400), 0),
	Insn('CAM_ROTATE', 40, 19, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 21500, 0),
	Insn('CAM_OFFSET', (61700, 900, 3400), 1500),
	Insn('CHAR_SET_POS', Char(10), (59000, 0, 3400), 90),
	Insn('CHAR_SET_COLOR', Char(10), Color(0x00FFFFFF), 0),
	Insn('FORK', 10, 1, [
		Insn('0x96', Char(254), (61700, 0, 3400), 2000, 0),
	]),
	Insn('FORK', 10, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('CHAR_ROTATE', Char(10), 0, 500),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(10), Text(
		'#13600053V#12P#1110F啊，找到了！{wait}'
		'{page}'
		'#13600054V#1109F罗伊德，快看快看～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(8), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK', 8, 2, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'i\x00\x00'),
	Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 105), Insn('SET'), Insn('END')])),
	Insn('0xB8', 100, 105),
	Insn('0xB8', 101, 105),
	Insn('CAM_OFFSET', (62600, 1200, 5800), 1000),
	Insn('CAM_ROTATE', 50, 15, 0, 1000),
	Insn('CAM_DISTANCE', 23000, 1000),
	Insn('CHAR_FLAG1_SET', Char(10), 64),
	Insn('CHAR_SET_CHCP', Char(10), 34),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('FORK', 10, 1, [
		Insn('0x95', Char(254), (62600, 0, 5800), 4000, 0),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('CHAR_SET_CHCP', Char(10), 35),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('FORK', 257, 2, [
		Insn('0xA6', Char(254), 0, 50, 500, 3000),
	]),
	Insn('SOUND_PLAY', 819, 0, 0, 100),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600055V#0011F#5P哇哇……\n'
		'等一下啊，琪雅！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#13600056V#12P#1109F艾莉和缇欧给我\n'
		'买了很多新衣服哦！{wait}'
		'{page}'
		'#13600057V虽然每件都很可爱，\n'
		'但我还是最喜欢这件！{wait}'
		'{page}'
		'#13600058V#1110F看啊看啊，合身吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600059V#0012F#5P哎，你一直这么抱着我，\n'
		'我要怎么看呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#13600060V#12P#1105F啊，对哦～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (62700, 1200, 4900), 1000),
	Insn('CHAR_SET_CHCP', Char(10), 1),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('FORK', 10, 1, [
		Insn('0x96', Char(254), (62700, 0, 4900), 1000, 0),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('0x6F', b'\x01'),
	Insn('FORK', 10, 2, [
		Insn('CHAR_ROTATE', Char(10), 180, 500),
	]),
	Insn('FORK_AWAIT', Char(10), 2),
	Insn('FORK', 10, 2, [
		Insn('CHAR_ROTATE', Char(10), 359, 500),
	]),
	Insn('SLEEP', 150),
	Insn('SOUND_PLAY', 2031, 0, 255, 100),
	Insn('FORK_AWAIT', Char(10), 2),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_POS', Char(259), (64599, 30, 5100), 90),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('TEXT_SET_POS', 280, 150, -1, -1),
	Insn('TEXT_TALK2', Char(259), Translate('琪雅'), Text(
		'#13600062V#1P看啊看啊，合身吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 40, 120, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#13600063V#0002F嗯……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 80, 70, -1, -1),
	Insn('TEXT_MESSAGE', Char(260), Text(
		'#13600064V#0305F哦哦……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 40, 20, -1, -1),
	Insn('TEXT_MESSAGE', Char(8), Text(
		'#13600065V#1002F嗯……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_TALK', Char(10), Text(
		'#13600066V#12P#1110F怎么样！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600067V#0004F#5P嗯……非常可爱。{wait}'
		'{page}'
		'#13600068V#0002F特别适合琪雅呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#13600069V#12P#1109F真的吗～！？{wait}'
		'{page}'
		'#13600070V#1102F喂喂，兰迪和课长\n'
		'也觉得可爱吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13600071V#5P#0309F噢～可爱可爱。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600072V#5P#1002F嗯，不错啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#13600073V#12P#1109F嘿嘿嘿……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_POS', Char(258), (59000, 0, 3400), 90),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(259), (59000, 0, 3400), 90),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (61600, 0, 3400), 2000, 0),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 700),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (60000, 0, 3400), 2000, 0),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (61000, 0, 4000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('CHAR_ROTATE', Char(259), 45, 500),
	Insn('TEXT_TALK', Char(258), Text(
		'#13600074V#12P#0102F呵呵，马上\n'
		'就来展示给大家看了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13600075V#6P#0206F……还有很多衣服\n'
		'想给你试穿呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(10), 225, 500),
	Insn('TEXT_TALK', Char(10), Text(
		'#13600076V#1110F艾莉、缇欧！\n'
		'罗伊德他们都说我可爱！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13600077V#12P#0109F呵呵，那太好啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13600078V#6P#0202F不过，罗伊德前辈的话，\n'
		'不管琪雅穿什么衣服\n'
		'也都会说可爱的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 225, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600079V#0012F#5P这个……\n'
		'哈哈，也许说得没错呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13600080V#5P#0309F哈哈，你们简直就像溺爱小孩的父母嘛。{wait}'
		'{page}'
		'#13600081V#0300F嗯～不过，小琪\n'
		'才刚来了一个星期吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13600082V#12P#0104F呵呵……\n'
		'总觉得有些难以相信呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#13600083V#12P#0105F对了……{wait}'
		'{page}'
		'#13600084V#0101F警察局总部发来的联系，\n'
		'最后怎么样了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13600085V#6P#0200F听说鲁巴彻那边\n'
		'好像传达了什么意向……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600086V#5P#1003F啊，那个嘛……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600087V#0006F#5P……等到吃午饭的时候\n'
		'再慢慢说给你们听吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 23500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('CAM_OFFSET', (12600, 2350, 4800), 0),
	Insn('CAM_ROTATE', 40, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('CHAR_SET_CHCP', Char(259), 11),
	Insn('CHAR_SET_FRAME', Char(259), 1),
	Insn('CHAR_SET_CHCP', Char(260), 12),
	Insn('CHAR_SET_FRAME', Char(260), 2),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_POS', Char(257), (13900, 900, 4600), 270),
	Insn('CHAR_SET_POS', Char(258), (11300, 900, 6650), 90),
	Insn('CHAR_SET_POS', Char(259), (11300, 900, 2550), 90),
	Insn('CHAR_SET_POS', Char(260), (13900, 900, 2550), 270),
	Insn('CHAR_FLAG1_SET', Char(10), 4),
	Insn('CHAR_FLAG1_UNSET', Char(10), 64),
	Insn('CHAR_SET_CHCP', Char(10), 7),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('CHAR_SET_POS', Char(10), (11300, 900, 4600), 90),
	Insn('CHAR_FLAG1_SET', Char(8), 4),
	Insn('CHAR_SET_CHCP', Char(8), 4),
	Insn('CHAR_SET_FRAME', Char(8), 1),
	Insn('CHAR_SET_POS', Char(8), (13900, 900, 6650), 270),
	Insn('CHAR_SET_CHCP', Char(12), 9),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('CHAR_SET_POS', Char(12), (16000, 850, 6400), 180),
	Insn('FORK_QUIT', Char(12), 255),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_SET_CHCP', Char(25), 36),
	Insn('CHAR_SET_FRAME', Char(25), 6),
	Insn('CHAR_FLAG1_SET', Char(25), 32768),
	Insn('CHAR_SET_POS', Char(25), (13000, 1400, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(25), 128),
	Insn('CHAR_FLAG2_UNSET', Char(25), 32768),
	Insn('CHAR_SET_CHCP', Char(26), 32),
	Insn('CHAR_SET_FRAME', Char(26), 12),
	Insn('CHAR_FLAG1_SET', Char(26), 32768),
	Insn('CHAR_SET_POS', Char(26), (13400, 1300, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(26), 128),
	Insn('CHAR_FLAG2_UNSET', Char(26), 32768),
	Insn('CHAR_SET_CHCP', Char(27), 36),
	Insn('CHAR_SET_FRAME', Char(27), 6),
	Insn('CHAR_FLAG1_SET', Char(27), 32768),
	Insn('CHAR_SET_POS', Char(27), (12400, 1400, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(27), 128),
	Insn('CHAR_FLAG2_UNSET', Char(27), 32768),
	Insn('CHAR_SET_CHCP', Char(28), 32),
	Insn('CHAR_SET_FRAME', Char(28), 12),
	Insn('CHAR_FLAG1_SET', Char(28), 32768),
	Insn('CHAR_SET_POS', Char(28), (12000, 1300, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(28), 128),
	Insn('CHAR_FLAG2_UNSET', Char(28), 32768),
	Insn('CHAR_SET_CHCP', Char(29), 36),
	Insn('CHAR_SET_FRAME', Char(29), 6),
	Insn('CHAR_FLAG1_SET', Char(29), 32768),
	Insn('CHAR_SET_POS', Char(29), (13000, 1400, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(29), 128),
	Insn('CHAR_FLAG2_UNSET', Char(29), 32768),
	Insn('CHAR_SET_CHCP', Char(30), 32),
	Insn('CHAR_SET_FRAME', Char(30), 12),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('CHAR_SET_POS', Char(30), (13400, 1300, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('CHAR_SET_CHCP', Char(31), 36),
	Insn('CHAR_SET_FRAME', Char(31), 6),
	Insn('CHAR_FLAG1_SET', Char(31), 32768),
	Insn('CHAR_SET_POS', Char(31), (12400, 1400, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_CHCP', Char(32), 32),
	Insn('CHAR_SET_FRAME', Char(32), 12),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_SET_POS', Char(32), (12000, 1300, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_CHCP', Char(33), 36),
	Insn('CHAR_SET_FRAME', Char(33), 6),
	Insn('CHAR_FLAG1_SET', Char(33), 32768),
	Insn('CHAR_SET_POS', Char(33), (12400, 1400, 2600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_CHCP', Char(34), 32),
	Insn('CHAR_SET_FRAME', Char(34), 12),
	Insn('CHAR_FLAG1_SET', Char(34), 32768),
	Insn('CHAR_SET_POS', Char(34), (12000, 1300, 2600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(34), 128),
	Insn('CHAR_FLAG2_UNSET', Char(34), 32768),
	Insn('CHAR_SET_CHCP', Char(35), 36),
	Insn('CHAR_SET_FRAME', Char(35), 6),
	Insn('CHAR_FLAG1_SET', Char(35), 32768),
	Insn('CHAR_SET_POS', Char(35), (13000, 1400, 2600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(35), 128),
	Insn('CHAR_FLAG2_UNSET', Char(35), 32768),
	Insn('CHAR_SET_CHCP', Char(36), 32),
	Insn('CHAR_SET_FRAME', Char(36), 12),
	Insn('CHAR_FLAG1_SET', Char(36), 32768),
	Insn('CHAR_SET_POS', Char(36), (13400, 1300, 2600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(36), 128),
	Insn('CHAR_FLAG2_UNSET', Char(36), 32768),
	Insn('CHAR_SET_CHCP', Char(37), 32),
	Insn('CHAR_SET_FRAME', Char(37), 7),
	Insn('CHAR_FLAG1_SET', Char(37), 32768),
	Insn('CHAR_SET_POS', Char(37), (12700, 1400, 5500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(37), 128),
	Insn('CHAR_FLAG2_UNSET', Char(37), 32768),
	Insn('CHAR_SET_CHCP', Char(38), 32),
	Insn('CHAR_SET_FRAME', Char(38), 7),
	Insn('CHAR_FLAG1_SET', Char(38), 32768),
	Insn('CHAR_SET_POS', Char(38), (12700, 1400, 3500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(38), 128),
	Insn('CHAR_FLAG2_UNSET', Char(38), 32768),
	Insn('CHAR_SET_CHCP', Char(39), 36),
	Insn('CHAR_SET_FRAME', Char(39), 0),
	Insn('CHAR_FLAG1_SET', Char(39), 32768),
	Insn('CHAR_SET_POS', Char(39), (16000, 750, 5500), 0),
	Insn('CAM_OFFSET', (12600, 1850, 4800), 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13600088V#0104F原来如此……{wait}'
		'{page}'
		'#13600089V#0100F总之，暂时是不必再担心\n'
		'黑手党那边了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13600090V#6P#0208F只是，最根本的问题\n'
		'却仍然留在我们的眼前……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600091V#5P#1006F嗯，把最棘手的那部分\n'
		'完全丢给我们了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600092V#0003F#11P总之，最关键的\n'
		'还是琪雅的记忆与身份……{wait}'
		'{page}'
		'#13600093V#0001F──那个，琪雅，\n'
		'还是什么都想不起来吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#13600094V#6P#1100F嗯……完全想不起来。{wait}'
		'{page}'
		'#13600095V#1109F罗伊德张大嘴，\n'
		'眼睛瞪圆的样子\n'
		'倒是想得起来～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600096V#0006F#11P（唔）……{wait}'
		'{page}'
		'#13600097V#0011F那是一周之前，\n'
		'我们第一次见面时的事吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#13600098V#6P#1108F可是，那之前的事情\n'
		'我就什么也想不起来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600099V#0000F#11P是吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13600100V#0304F#11P算啦，既然想不起来，\n'
		'那也就没办法了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13600101V#6P#0200F#6P……对各方面的咨询，\n'
		'有什么结果吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600102V#5P#1000F啊……那个啊。{wait}'
		'{page}'
		'#13600103V车站、机场，还有国境门那边都问过了，\n'
		'但目前似乎还没有发现任何线索。{wait}'
		'{page}'
		'#13600104V#1003F以后恐怕也不会有什么进展吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600105V#0008F#11P……这样啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#13600106V#6P#1105F？？？{wait}'
		'{page}'
		'#13600107V#1101F怎么了，罗伊德？\n'
		'你肚子疼吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600108V#0012F#11P哈哈，没有啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600109V#0003F#11P──课长，\n'
		'今天下午……{wait}'
		'{page}'
		'#13600110V#0001F我可不可以带琪雅\n'
		'去外面散散步呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(8), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600111V#5P#1001F嗯……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13600112V#0101F罗伊德，你有什么想法吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600113V#0004F#11P嗯……{wait}'
		'{page}'
		'#13600114V#0000F我想去委托\n'
		'游击士协会帮忙试试。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(8), 0, 1700, (2, 7, 80, 1)),
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
	Insn('TEXT_TALK', Char(258), Text(
		'#13600115V#0105F咦咦！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13600116V#6P#0205F你是认真的吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#13600117V#6P#1111F游击士？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600118V#5P#1004F……原来如此啊。{wait}'
		'{page}'
		'#13600119V#1002F那些家伙在大陆各地\n'
		'都设有协会分部……{wait}'
		'{page}'
		'#13600120V你想利用他们那庞大的情报网寻找线索吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600121V#0006F#11P嗯，在这种时候，\n'
		'我觉得应该请求他们帮忙。{wait}'
		'{page}'
		'#13600122V#0001F……不行吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600123V#5P#1002F算啦，这不是也挺好的吗？{wait}'
		'{page}'
		'#13600124V#1004F警察和游击士协会\n'
		'又不是对立关系。{wait}'
		'{page}'
		'#13600125V要说稍微有些心存芥蒂的话，\n'
		'那肯定也主要是我们警察这边吧。{wait}'
		'{page}'
		'#13600126V#1002F而且案件情况也摆在那里，如果请求\n'
		'他们协助，应该不会被拒绝吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600127V#0004F#11P嗯，我也是这么想的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13600128V#0300F#11P哈，反正我们和艾丝蒂尔\n'
		'他们的关系也一直都挺融洽的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13600129V#0104F确实，如果想与协会商量的话，\n'
		'现在也许是个很好的机会呢。{wait}'
		'{page}'
		'#13600130V#0101F不过，罗伊德……\n'
		'你说要带琪雅出去，\n'
		'是准备一个人带着她吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600131V#0005F#11P我确实是这么打算的……{wait}'
		'{page}'
		'#13600132V#0000F这并不是什么值得全员出动的事情，\n'
		'我觉得自己一个人就已经足够了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13600133V#0103F……我无法赞同哦。{wait}'
		'{page}'
		'#13600134V#0111F琪雅本来就和你最亲密，\n'
		'你居然还想更进一步地独占她。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600135V#0011F#11P哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13600136V#6P#0206F罗伊德前辈好狡猾。{wait}'
		'{page}'
		'#13600137V#0211F我想，和这孩子接触的机会，\n'
		'应该平等地分给大家啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#13600138V#6P#1100F哎～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600139V#0011F#11P那个，这是什么意思？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13600140V#0309F#11P哈哈，你好像被嫉恨啦。{wait}'
		'{page}'
		'#13600141V说起来，这几天你好像\n'
		'一直都是和小琪一起睡的吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600142V#0006F#5P不，那是琪雅\n'
		'她擅自爬到我的床上……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600143V#0001F#11P──那个，琪雅，\n'
		'我们都给你准备好单独的房间了，\n'
		'你要一个人乖乖睡哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#13600144V#6P#1106F可是，和罗伊德一起睡，\n'
		'我总觉得很安心嘛。{wait}'
		'{page}'
		'#13600145V#1112F如果给你添麻烦了，\n'
		'那我以后就不再这样了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600146V#0011F#11P不不，没有……\n'
		'也并没有添什么麻烦啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13600147V#0101F喂，罗伊德……\n'
		'你也太冷淡了吧。{wait}'
		'{page}'
		'#13600148V她才刚经历过那种遭遇，\n'
		'肯定还会感到不安。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13600149V#6P#0211F她只是想和你一起睡而已，\n'
		'这点事情总该承担得起吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600150V#0012F#11P你们到底希望我怎么做啊！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600151V#5P#1002F呵呵……\n'
		'算了，你就暂时多陪陪她吧。{wait}'
		'{page}'
		'#13600152V#1003F至于外出嘛……\n'
		'保险起见，还是再加一个人一起去吧。{wait}'
		'{page}'
		'#13600153V#1000F鲁巴彻虽然表示要休战和解，\n'
		'但我们还是小心一点比较好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600154V#0005F#11P啊……{wait}'
		'{page}'
		'#13600155V#0000F明白了，\n'
		'我们会小心的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_SET_VOLUME', b'2\xd0\x07\x00\x00'),
	Insn('CAM_DISTANCE', 25500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('SLEEP', 1000),
	Insn('0xE3', 10),
	Insn('IMG_0xC9', (ResId(2), 3), Color(0xFFFFFFFF), 800, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
	Insn('TEXT_RESET', b'\x03'),
	Insn('IMG_0xC9', (ResId(2), 3), Color(0x00FFFFFF), 800, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
	Insn('0xE3', 11),
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
	Insn('CHAR_FLAG1_SET', Char(32), 128),
	Insn('CHAR_FLAG2_SET', Char(32), 32768),
	Insn('CHAR_FLAG1_SET', Char(33), 128),
	Insn('CHAR_FLAG2_SET', Char(33), 32768),
	Insn('CHAR_FLAG1_SET', Char(34), 128),
	Insn('CHAR_FLAG2_SET', Char(34), 32768),
	Insn('CHAR_FLAG1_SET', Char(35), 128),
	Insn('CHAR_FLAG2_SET', Char(35), 32768),
	Insn('CHAR_FLAG1_SET', Char(36), 128),
	Insn('CHAR_FLAG2_SET', Char(36), 32768),
	Insn('CHAR_FLAG1_SET', Char(37), 128),
	Insn('CHAR_FLAG2_SET', Char(37), 32768),
	Insn('CHAR_FLAG1_SET', Char(38), 128),
	Insn('CHAR_FLAG2_SET', Char(38), 32768),
	Insn('CHAR_FLAG1_SET', Char(39), 128),
	Insn('CHAR_FLAG2_SET', Char(39), 32768),
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
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG1_UNSET', Char(14), 128),
	Insn('CHAR_SET_POS', Char(14), (14350, 850, 12060), 180),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0xD5', 33),
	Insn('0xD5', 34),
	Insn('0xD5', 35),
	Insn('0xD5', 36),
	Insn('0x2F', b'\x01\x00'),
	Insn('0x2F', b'\x02\x00'),
	Insn('0x2F', b'\x03\x00'),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_POS', -1, 30, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}{0x06}{0x18}#1K要选择谁作为同行者呢？{color 0}{wait}'
	)),
	Insn('MENU', 0, -1, -1, 0, Text(
		'【邀请艾莉同行】\n'
		'【邀请缇欧同行】\n'
		'【邀请兰迪同行】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('EXPR_ATTR', 101, Expr([Insn('ATTR', 101), Insn('CONST', 30), Insn('ADD'), Insn('SET'), Insn('END')])),
			Insn('FLAG_SET', Flag(1356)),
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
			Insn('CALL', Function((0, 41))),
			Insn('BREAK'),
		],
		1: [
			Insn('EXPR_ATTR', 102, Expr([Insn('ATTR', 102), Insn('CONST', 30), Insn('ADD'), Insn('SET'), Insn('END')])),
			Insn('FLAG_SET', Flag(1357)),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
			Insn('CALL', Function((0, 42))),
			Insn('BREAK'),
		],
		2: [
			Insn('EXPR_ATTR', 103, Expr([Insn('ATTR', 103), Insn('CONST', 30), Insn('ADD'), Insn('SET'), Insn('END')])),
			Insn('FLAG_SET', Flag(1358)),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CALL', Function((0, 43))),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('RETURN'),
]

data['code'][39] = [
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (256399, 0, 67500), 2000, 0),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 10, 2, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('EMOTE', Char(10), 0, 1700, (8, 9, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('SLEEP', 1500),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (256399, 0, 66600), 1000, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 10, 2, [
		Insn('CHAR_ROTATE', Char(10), 0, 800),
	]),
	Insn('FORK_AWAIT', Char(10), 2),
	Insn('FORK', 10, 2, [
		Insn('CHAR_ROTATE', Char(10), 181, 800),
	]),
	Insn('FORK_AWAIT', Char(10), 2),
	Insn('EMOTE', Char(10), 0, 1700, (10, 11, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('SLEEP', 1500),
	Insn('RETURN'),
]

data['code'][40] = [
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

data['code'][41] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x2E', b'R\xff\xff'),
	Insn('0x2E', b'\x01\xef\xff'),
	Insn('CAM_OFFSET', (1000, 1000, 3700), 0),
	Insn('CAM_ROTATE', 55, 23, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 24000, 0),
	Insn('CHAR_SET_POS', Char(257), (200, 0, 2200), 90),
	Insn('CHAR_SET_POS', Char(258), (1800, 0, 2200), 270),
	Insn('CHAR_SET_POS', Char(339), (1000, 0, 3800), 180),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (1000, 1000, 2700), 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600156V#6P#0000F那么……\n'
		'我们这就出发吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13600157V#0104F#11P目标是东侧大道的游击士协会哦。{wait}'
		'{page}'
		'#13600158V#0100F还是不要去其它地方\n'
		'闲逛比较好吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600159V#6P#0003F不，说不定某些场所\n'
		'正是能使琪雅恢复记忆的契机呢。{wait}'
		'{page}'
		'#13600160V#0000F虽然确实需要小心……\n'
		'但只是去一趟协会而已，在来回的路上，\n'
		'我们就算到处闲逛一下，应该也没有关系吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13600161V#0102F#11P原来如此，也有道理。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(258), Char(339), 500),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(339), 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#13600162V#0109F呵呵，琪雅，\n'
		'那我们这就出门好吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600163V#1109F#5P嗯！{wait}'
		'{page}'
		'#13600164V#1105F不过，要去哪里呢～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13600165V#0103F嗯～\n'
		'是一个叫做游击士协会的地方……{wait}'
		'{page}'
		'#13600166V#0100F你应该没听说过那里吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600167V#1103F#5P游击士……{wait}'
		'{page}'
		'#13600168V#1100F……那个，那些人莫非\n'
		'就是所谓的正义的同伴？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600169V#12P#0005F怎么，原来你知道吗？{wait}'
		'{page}'
		'#13600170V#0000F看来这种程度的一般常识\n'
		'倒是还记得呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13600171V#0100F嗯，看来是这样呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600172V#1100F#5P嘿嘿嘿……\n'
		'虽然不知道为什么要去那里。{wait}'
		'{page}'
		'#13600173V#1109F但只要和罗伊德还有艾莉在一起，\n'
		'琪雅不管去哪里都可以！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(339), 300, 1300, (54, 57, 250, 0)),
	Insn('SOUND_PLAY', 892, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600174V#12P#0011F唔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE_STOP', Char(339)),
	Insn('TEXT_TALK', Char(258), Text(
		'#13600175V#0109F………啊啊，真是的………！\n'
		'为什么会如此可爱啊……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 500),
	Insn('0x82', 50, 0, 1000, 200),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600176V#1109F#5P#4S那我们就快点出发啦～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (1000, 0, 2000), 180),
	Insn('FLAG_SET', Flag(1342)),
	Insn('0xC7', b'\x00\x00\x10\x00\x00'),
	Insn('QUEST', 71, Insn('TASK_SET', 19)),
	Insn('QUEST', 72, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 72, Insn('TASK_SET', 0)),
	Insn('BGM_SET_VOLUME', b'd\xd0\x07\x00\x00'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][42] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x2E', b'R\xff\xff'),
	Insn('0x2E', b'\x02\xef\xff'),
	Insn('CAM_OFFSET', (1000, 1000, 3700), 0),
	Insn('CAM_ROTATE', 55, 23, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 24000, 0),
	Insn('CHAR_SET_POS', Char(257), (200, 0, 2200), 90),
	Insn('CHAR_SET_POS', Char(259), (1800, 0, 2200), 270),
	Insn('CHAR_SET_POS', Char(339), (1000, 0, 3800), 180),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (1000, 1000, 2700), 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600177V#6P#0000F那么……\n'
		'我们这就出发吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13600178V#0204F#11P是东侧大道的游击士协会哦。{wait}'
		'{page}'
		'#13600179V#0201F……果然还是不要\n'
		'去其它的地方闲逛比较好吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600180V#6P#0003F不，说不定某些场所\n'
		'正是能使琪雅恢复记忆的契机呢。{wait}'
		'{page}'
		'#13600181V#0000F虽然确实需要小心……\n'
		'但只是去一趟协会而已，在来回的路上，\n'
		'我们就算到处闲逛一下，应该也没有关系吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13600182V#0204F#11P原来如此，有道理哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(259), Char(339), 500),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(339), 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#13600183V#0202F……那，琪雅，\n'
		'我们这就出发，可以吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600184V#1109F#5P嗯！{wait}'
		'{page}'
		'#13600185V#1105F不过，要去哪里呢～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13600186V#0205F是一个叫做游击士协会的地方……{wait}'
		'{page}'
		'#13600187V#0206F对琪雅来说，\n'
		'可能会有点难懂吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600188V#1103F#5P游击士……{wait}'
		'{page}'
		'#13600189V#1100F……那个，那些人莫非\n'
		'就是所谓的正义的同伴？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600190V#12P#0005F怎么，原来你知道吗？{wait}'
		'{page}'
		'#13600191V#0000F看来这种程度的一般常识\n'
		'倒是还记得呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13600192V#0202F是啊……{wait}'
		'{page}'
		'#13600193V#0204F这毕竟没有涉及到\n'
		'比较复杂的长期记忆。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600194V#1100F#5P嘿嘿嘿……\n'
		'虽然不知道为什么要去那里。{wait}'
		'{page}'
		'#13600195V#1109F但只要和罗伊德还有缇欧在一起，\n'
		'琪雅不管去哪里都可以！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(339), 300, 1300, (54, 57, 250, 0)),
	Insn('SOUND_PLAY', 892, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600196V#12P#0011F唔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE_STOP', Char(339)),
	Insn('TEXT_TALK', Char(259), Text(
		'#13600197V#0209F……这种笑脸，也太犯规了吧，\n'
		'简直让人完全无法抵抗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 500),
	Insn('0x82', 50, 0, 1000, 200),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600198V#1109F#5P#4S那我们就快点出发啦～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (1000, 0, 2000), 180),
	Insn('FLAG_SET', Flag(1342)),
	Insn('0xC7', b'\x00\x00\x10\x00\x00'),
	Insn('QUEST', 71, Insn('TASK_SET', 19)),
	Insn('QUEST', 72, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 72, Insn('TASK_SET', 1)),
	Insn('BGM_SET_VOLUME', b'd\xd0\x07\x00\x00'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][43] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x2E', b'R\xff\xff'),
	Insn('0x2E', b'\x03\xef\xff'),
	Insn('CAM_OFFSET', (1000, 1000, 3700), 0),
	Insn('CAM_ROTATE', 55, 23, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 24000, 0),
	Insn('CHAR_SET_POS', Char(257), (200, 0, 2200), 90),
	Insn('CHAR_SET_POS', Char(260), (1800, 0, 2200), 270),
	Insn('CHAR_SET_POS', Char(339), (1000, 0, 3800), 180),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (1000, 1000, 2700), 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600199V#6P#0000F那么……\n'
		'我们这就出发吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13600200V#0304F#11P是东侧大道的游击士协会啊。{wait}'
		'{page}'
		'#13600201V#0301F怎么样？果然还是应该\n'
		'直奔目标，不要去别处乱逛吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600202V#6P#0003F不，说不定某些场所\n'
		'正是能使琪雅恢复记忆的契机呢。{wait}'
		'{page}'
		'#13600203V#0000F虽然确实需要小心……\n'
		'但只是去一趟协会而已，在来回的路上，\n'
		'我们就算到处闲逛一下，应该也没有关系吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13600204V#0300F#11P原来如此。{wait}'
		'{page}'
		'#13600205V#0309F算啦，反正你我都在，\n'
		'不管遇到什么情况都没关系吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(260), Char(339), 500),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(339), 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#13600206V#0302F好啦～小琪，\n'
		'我们这就出发吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600207V#1109F#5P嗯！{wait}'
		'{page}'
		'#13600208V#1105F不过，要去哪里呢～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13600209V#0305F刚才说了啊，是游击士协会……{wait}'
		'{page}'
		'#13600210V#0302F不过你应该没听说过\n'
		'那种地方吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600211V#1103F#5P游击士……{wait}'
		'{page}'
		'#13600212V#1100F……那个，那些人莫非\n'
		'就是所谓的正义的同伴？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600213V#12P#0005F怎么，原来你知道吗？{wait}'
		'{page}'
		'#13600214V#0000F看来这种程度的一般常识\n'
		'倒是还记得呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13600215V#0300F嗯，看来是这样。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600216V#1100F#5P嘿嘿嘿……\n'
		'虽然不知道为什么要去那里。{wait}'
		'{page}'
		'#13600217V#1109F但只要和罗伊德还有兰迪在一起，\n'
		'琪雅不管去哪里都可以！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(339), 300, 1300, (54, 57, 250, 0)),
	Insn('SOUND_PLAY', 892, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600218V#12P#0011F唔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE_STOP', Char(339)),
	Insn('TEXT_TALK', Char(260), Text(
		'#13600219V#0306F……为孩子而烦恼的父亲是什么心情，\n'
		'我现在好像稍微有点明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 500),
	Insn('0x82', 50, 0, 1000, 200),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600220V#1109F#5P#4S那我们就快点出发啦～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (1000, 0, 2000), 180),
	Insn('FLAG_SET', Flag(1342)),
	Insn('0xC7', b'\x00\x00\x10\x00\x00'),
	Insn('QUEST', 71, Insn('TASK_SET', 19)),
	Insn('QUEST', 72, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 72, Insn('TASK_SET', 2)),
	Insn('BGM_SET_VOLUME', b'd\xd0\x07\x00\x00'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][44] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x2E', b'\x08\xff\xff'),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('LOAD_CHCP', 'apl/ch50090', 32),
	Insn('LOAD_CHCP', 'apl/ch50092', 33),
	Insn('LOAD_CHCP', 'chr/ch00802', 34),
	Insn('LOAD_CHCP', 'chr/ch08201', 35),
	Insn('LOAD_CHCP', 'apl/ch50380', 36),
	Insn('EFF_LOAD', ResId(0), 'event\\ev500_00.eff'),
	Insn('SOUND_LOAD', 821),
	Insn('0x32', Party(8), 0, 29),
	Insn('PARTY_CRAFT_REMOVE', Party(8), -1),
	Insn('0x38', Party(8), 128, 2),
	Insn('0x38', Party(8), 129, 2),
	Insn('0x38', Party(8), 130, 2),
	Insn('0x38', Party(8), 131, 2),
	Insn('0x38', Party(8), 132, 2),
	Insn('0x38', Party(8), 133, 2),
	Insn('0x38', Party(8), 134, 2),
	Insn('0x42', Party(8), 1101, -1),
	Insn('0x42', Party(8), 1513, -1),
	Insn('0x42', Party(8), 1613, -1),
	Insn('PARTY_CRAFT_ADD', Party(8), 230),
	Insn('PARTY_CRAFT_ADD', Party(8), 231),
	Insn('PARTY_CRAFT_ADD', Party(8), 232),
	Insn('PARTY_CRAFT_ADD', Party(8), 290),
	Insn('PARTY_SET_SBREAK', Party(8), 6, 290),
	Insn('PARTY_CRAFT_ADD', Party(8), 324),
	Insn('0x42', Party(8), 111, 0),
	Insn('0x42', Party(8), 146, 4),
	Insn('0x42', Party(8), 123, 3),
	Insn('0x42', Party(8), 129, 2),
	Insn('0x42', Party(8), 101, 1),
	Insn('0x42', Party(8), 107, 6),
	Insn('0x42', Party(8), 172, 5),
	Insn('CAM_OFFSET', (900, 1000, 400), 0),
	Insn('CAM_ROTATE', 50, 21, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 26500, 0),
	Insn('CHAR_SET_POS', Char(257), (800, 0, 500), 0),
	Insn('CHAR_SET_POS', Char(258), (800, 0, 500), 0),
	Insn('CHAR_SET_POS', Char(259), (800, 0, 0), 0),
	Insn('CHAR_SET_POS', Char(260), (800, 0, 0), 0),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(10), 32768),
	Insn('0x90', Char(10), (800, 3000, 14000), b'\xb4\x00'),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis080.itp'),
	Insn('IMG_LOAD', ResId(1), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis081.itp'),
	Insn('IMG_LOAD', ResId(2), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis082.itp'),
	Insn('IMG_LOAD', ResId(3), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu01103.itp'),
	Insn('CAM_OFFSET', (900, 1000, 2400), 2000),
	Insn('CAM_DISTANCE', 25500, 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('SLEEP', 500),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (200, 0, 3000), 2000, 0),
	]),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 250),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (1300, 0, 3000), 2000, 0),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 400),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (200, 0, 1800), 2000, 0),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 250),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (1300, 0, 1800), 2000, 0),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100001V#0000F#12P我们回来了～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100002V#0309F#12P回来啦～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('SOUND_PLAY', 2036, 0, 255, 90),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100003V#4P#1110F啊，你们回来了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CAM_OFFSET', (800, 1900, 8000), 0),
	Insn('CAM_ROTATE', 55, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 24000, 0),
	Insn('FORK_FUNC', Char(10), 3, Function((0, 45))),
	Insn('FORK_LOOP', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(10), 500),
	]),
	Insn('FORK_LOOP', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(10), 500),
	]),
	Insn('SLEEP', 1000),
	Insn('SOUND_PLAY', 2037, 0, 255, 100),
	Insn('TEXT_TALK', Char(10), Text(
		'#1109F#5P#12A欢迎回来！{wait}'
	)),
	Insn('FORK_AWAIT', Char(10), 3),
	Insn('FORK_QUIT', Char(258), 2),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100005V#12P#0014F哈哈，撞得好准呢。{wait}'
		'{page}'
		'#14100006V#0002F我们回来啦，琪雅。\n'
		'今天有没有乖乖的啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IMG_0xC9', (ResId(3), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(3), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(3), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(3), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 500),
	Insn('TEXT_MESSAGE', Char(10), Text(
		'#14100007V#5P嗯～！{wait}'
		'{page}'
		'#14100008V琪雅一直都和赛特一起\n'
		'乖乖看家呢。{wait}'
		'{page}'
		'#14100009V图书馆的书也已经\n'
		'读完三册了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(3), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(3), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(3), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(3), 0))),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100010V#12P#0005F嘿，那可真是厉害啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100011V#0102F#11P呵呵，虽然是儿童读物，\n'
		'但一上午居然能看完三本。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14100012V#0204F#12P这个孩子似乎\n'
		'拥有相当惊人的\n'
		'情报处理能力呢……{wait}'
		'{page}'
		'#14100013V#0202F非常期待她将来的表现啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100014V#0306F#11P真是的，你们整天只知道\n'
		'凑在一起哄小孩啊。{wait}'
		'{page}'
		'#14100015V#0302F哈，不过我好像也没资格说别人吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_CHCP', Char(10), 1),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('FORK', 10, 1, [
		Insn('0x96', Char(254), (200, 0, 4000), 1000, 0),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('CHAR_FLAG1_SET', Char(10), 64),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100016V#1105F#5P哎～？{wait}'
		'{page}'
		'#14100017V#1110F比起那个，\n'
		'琪雅的肚子饿啦。{wait}'
		'{page}'
		'#14100018V#1109F快点做午饭吃吧～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100019V#12P#0002F哈哈，是啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(260), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100020V#6P#0000F今天轮到我做饭了。\n'
		'各位，通心粉可以吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100021V#0102F#11P嗯，好啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14100022V#12P#0204F只要是罗伊德前辈做的，\n'
		'不管是什么都可以。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100023V#0309F#11P要给我多盛一些啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100024V#6P#0002F哈哈，知道啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100025V#1105F#5P罗伊德来做饭吗？{wait}'
		'{page}'
		'#14100026V#1109F那琪雅也要帮忙～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(10), 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100027V#0105F#11P琪雅……\n'
		'难道你做过料理吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14100028V#12P#0200F莫非是，\n'
		'想起什么了吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100029V#1100F#5P刚才看的那本书里\n'
		'有个厨师呢～{wait}'
		'{page}'
		'#14100030V他做出来的料理\n'
		'很～好吃呢～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100031V#0302F#11P哈哈，原来如此啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100032V#12P#0000F那么，既然难得琪雅有兴致，\n'
		'就来帮帮忙吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100033V#1109F#5P嗯～要上啦～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 24500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('CAM_OFFSET', (116700, 1200, 6000), 0),
	Insn('CAM_ROTATE', 60, 17, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 22000, 0),
	Insn('CHAR_SET_POS', Char(257), (116700, 30, 7600), 0),
	Insn('CHAR_SET_POS', Char(10), (116700, 30, 6400), 0),
	Insn('CAM_OFFSET', (116700, 1200, 7000), 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100034V#0003F#11P那么……\n'
		'要做哪种通心粉呢？{wait}'
		'{page}'
		'#14100035V#0000F这里有阿尔摩利卡产的\n'
		'鸡蛋和培根，\n'
		'做奶油通心粉应该不错……{wait}'
		'{page}'
		'#14100036V另外也有利贝尔产的蛤蜊罐头，\n'
		'也可以做蛤蜊面呢。{wait}'
		'{page}'
		'#14100037V#0005F啊，还是用\n'
		'茄子和肉酱来做比较好？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_UNSET', Flag(0)),
	Insn('FLAG_UNSET', Flag(1)),
	Insn('FLAG_UNSET', Flag(2)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('TEXT_SET_POS', -1, 30, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}{0x06}{0x18}#1K要做什么呢？{color 0}{wait}'
	)),
	Insn('MENU', 0, -1, -1, 0, Text(
		'【奶油通心粉】\n'
		'【蛤蜊面】\n'
		'【茄子肉酱面】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('TEXT_TALK', Char(257), Text(
				'#14100038V#0000F#11P好，机会难得，\n'
				'趁着还新鲜，就把这些鸡蛋用掉吧。{wait}'
				'{page}'
				'#14100041V那么，接下来──{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(0)),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(257), Text(
				'#14100039V#0000F#11P好，机会难得，\n'
				'就把蛤蜊罐头用掉吧。{wait}'
				'{page}'
				'#14100041V那么，接下来──{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1)),
			Insn('BREAK'),
		],
		2: [
			Insn('TEXT_TALK', Char(257), Text(
				'#14100040V#0000F#11P好，正好有些肉末，\n'
				'马上将它和茄子一起做成肉酱吧。{wait}'
				'{page}'
				'#14100041V那么，接下来──{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(2)),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100042V#11P#1110F那个～那个～罗伊德。{wait}'
		'{page}'
		'#14100043V琪雅可以帮你做什么呢～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(10), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100044V#0002F#5P那么，就去帮我把\n'
		'接下来说的材料给拿来好吗？{wait}'
		'{page}'
		'#14100045V我来准备\n'
		'煮面条。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100046V#11P#1109F没问题～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (122700, 1000, 8300), 0),
	Insn('CAM_ROTATE', 45, 21, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 21500, 0),
	Insn('CHAR_SET_POS', Char(257), (123700, 30, 8300), 0),
	Insn('CHAR_SET_POS', Char(10), (122700, 30, 8300), 0),
	Insn('OBJ_FLAG_UNSET', Object(15), 4),
	Insn('CHAR_SET_CHCP', Char(25), 33),
	Insn('CHAR_SET_FRAME', Char(25), 9),
	Insn('CHAR_FLAG1_SET', Char(25), 32768),
	Insn('CHAR_SET_POS', Char(25), (123100, 800, 9300), 0),
	Insn('CHAR_FLAG1_UNSET', Char(25), 128),
	Insn('CHAR_FLAG2_UNSET', Char(25), 32768),
	Insn('OBJ_SET_FRAME', Object(15), 'pan00', Insn('1', 1)),
	Insn('OBJ_SET_FRAME', Object(15), 'pan01', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(15), 'kemuri2_add', Insn('0', 1)),
	Insn('SLEEP', 500),
	Insn('CAM_OFFSET', (123700, 1000, 8300), 2000),
	Insn('SOUND_PLAY', 84, 0, 0, 70),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100047V#12P#1100F（开心……激动……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(10), Char(257), 500),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100048V#6P#1101F喂～喂～罗伊德，\n'
		'还没做好吗～！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#14100049V#11P#0004F还要再等一下哦。\n'
				'煮面条时，最重要的就是火候了。{wait}'
				'{page}'
				'#14100050V#0000F在火候正好时将面条捞出，\n'
				'然后在平底锅里把肉、蛋和面条拌好，\n'
				'最后再撒上胡椒粉……{wait}'
				'{page}'
				'#14100053V#0014F这样就算是大功告成啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#14100049V#11P#0004F还要再等一下哦。\n'
				'煮面条时，最重要的就是火候了。{wait}'
				'{page}'
				'#14100051V#0000F在火候正好时将面条捞出，\n'
				'然后在平底锅里把蛤蜊、酱汁和面条拌好，\n'
				'最后再放上大蒜和香芹做调味料……{wait}'
				'{page}'
				'#14100053V#0014F这样就算是大功告成啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#14100049V#11P#0004F还要再等一下哦。\n'
				'煮面条时，最重要的就是火候了。{wait}'
				'{page}'
				'#14100052V#0000F在火候正好时将面条捞出，\n'
				'然后在平底锅里把肉酱和面条拌好，接下来再放入\n'
				'炸熟的茄子，最后撒上奶酪粉……{wait}'
				'{page}'
				'#14100053V#0014F这样就算是大功告成啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100054V#6P#1105F嘿……{wait}'
		'{page}'
		'#14100055V#1110F那，接下来就让\n'
		'琪雅试试看吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_WATCH', Char(257), Char(10), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100056V#11P#0005F哎，没问题吗？{wait}'
		'{page}'
		'#14100057V#0004F（虽然觉得她应该做不好……不过算了，\n'
		'\u3000只要有我在一旁帮忙就没问题了吧。）{wait}'
		'{page}'
		'#14100058V#0000F好，那你就试试看吧。{wait}'
		'{page}'
		'#14100059V不过可要小心，别被火烫伤了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100060V#6P#1109F嗯～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (124090, 1000, 8260), 1500),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (124800, 30, 8300), 1000, 0),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 10, 1, [
		Insn('0x96', Char(254), (123700, 30, 8300), 1000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('CHAR_ROTATE', Char(10), 0, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100061V#1101F#11P#30W那个……{wait}'
		'{page}'
		'#14100062V#30W在火候正好时将面条捞出，\n'
		'然后在平底锅里……{wait}'
		'{page}'
		'#14100063V#1105F#40W……………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 20500, 20000),
	Insn('EMOTE', Char(10), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(10)),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100064V#0006F#11P（果然还是太勉强了啊……）{wait}'
		'{page}'
		'#14100065V#0000F（不过没关系，只要是琪雅做的，\n'
		'\u3000即使有些失败，大家也都会很开心的──）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 931, 0, 0, 80),
	Insn('BGM_SET_VOLUME', b'<\xe8\x03\x00\x00'),
	Insn('EFF_PLAY', (ResId(0), 0), Char(10), 0, 0, 0, 750, 0, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('SLEEP', 1200),
	Insn('SOUND_PLAY', 2038, 0, 255, 100),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100066V#11P#1103F#30W───嗯，我明白啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}琪雅用相当娴熟的动作\n'
		'将已经煮熟的面条从锅中捞起，\n'
		'随后放到平底锅里进行烹调。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100067V#0011F#11P哎……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 81, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('CROSSFADE', 500),
	Insn('0x14', b'\x01\x00\x00\x00\xff\xff\xff\xbb\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
	Insn('CAM_DISTANCE', 20500, 0),
	Insn('OBJ_SET_FRAME', Object(15), 'pan00', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(15), 'pan01', Insn('1', 1)),
	Insn('OBJ_SET_FRAME', Object(15), 'kemuri2_add', Insn('1', 1)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('0x15', b'\x00\x00\x00\x00'),
	Insn('EFF_STOP', (ResId(0), 2)),
	Insn('BGM_SET_VOLUME', b'd\xe8\x03\x00\x00'),
	Insn('SLEEP', 1300),
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100068V#11P#1109F#4S嗯，做好啦～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
			Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
			Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), -10000, 500),
			Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
			Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
		]),
		(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
			Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 500, 0),
			Insn('IMG_0xC9', (ResId(1), 0), Color(0x00000000), -10000, 500),
			Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
			Insn('IMG_0xCA', Insn('0', (ResId(1), 0))),
		]),
		(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
			Insn('IMG_0xC9', (ResId(2), 3), Color(0xFFFFFFFF), 500, 0),
			Insn('IMG_0xC9', (ResId(2), 0), Color(0x00000000), -10000, 500),
			Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
			Insn('IMG_0xCA', Insn('0', (ResId(2), 0))),
		]),
		(None, []),
	]),
	Insn('SLEEP', 1000),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#14100069V#0005F噢噢……\n'
		'很厉害啊！琪雅！？{wait}'
		'{page}'
		'#14100070V你的烹饪技术实在是太好了，\n'
		'不过，到底是怎么掌握的啊！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_WATCH', Char(10), Char(257), 500),
	Insn('TEXT_MESSAGE', Char(10), Text(
		'#14100071V#1104F嘿嘿嘿～\n'
		'不知道是怎么回事，脑中突然就灵光一闪。{wait}'
		'{page}'
		'#14100072V#1110F我的做法，没有弄错吧～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
			Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
			Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
			Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
			Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
		]),
		(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
			Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 500, 0),
			Insn('IMG_0xC9', (ResId(1), 0), Color(0x00000000), 0, 500),
			Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
			Insn('IMG_0xCA', Insn('0', (ResId(1), 0))),
		]),
		(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
			Insn('IMG_0xC9', (ResId(2), 3), Color(0x00FFFFFF), 500, 0),
			Insn('IMG_0xC9', (ResId(2), 0), Color(0x00000000), 0, 500),
			Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
			Insn('IMG_0xCA', Insn('0', (ResId(2), 0))),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100073V#0004F#11P完全没有，不如说\n'
		'比我的技术还要好呢。{wait}'
		'{page}'
		'#14100074V#0000F琪雅……你是不是……\n'
		'以前曾经做过料理呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100075V#6P#1111F嗯～有过那种事吗？{wait}'
		'{page}'
		'#14100076V#1109F算啦，不管了，肚子已经很饿了，\n'
		'快去拿给大家吃吧～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 20000, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('OBJ_FLAG_SET', Object(15), 4),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_SET_CHCP', Char(259), 11),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_SET_CHCP', Char(260), 12),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_POS', Char(257), (13900, 900, 6650), 270),
	Insn('CHAR_SET_POS', Char(260), (13900, 900, 4600), 270),
	Insn('CHAR_SET_POS', Char(258), (11300, 900, 6650), 90),
	Insn('CHAR_SET_POS', Char(259), (11300, 900, 2550), 90),
	Insn('CHAR_FLAG1_SET', Char(10), 4),
	Insn('CHAR_SET_CHCP', Char(10), 7),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('CHAR_SET_POS', Char(10), (11300, 900, 4600), 90),
	Insn('CHAR_FLAG1_SET', Char(14), 128),
	Insn('CHAR_SET_CHCP', Char(12), 9),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('CHAR_SET_POS', Char(12), (16000, 850, 6400), 180),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG2_UNSET', Char(12), 32768),
	Insn('FORK_FUNC', Char(12), 1, Function((0, 40))),
	Insn('CHAR_SET_CHCP', Char(25), 33),
	Insn('CHAR_SET_FRAME', Char(25), 0),
	Insn('CHAR_FLAG1_SET', Char(25), 32768),
	Insn('CHAR_SET_POS', Char(25), (13000, 1400, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(25), 128),
	Insn('CHAR_FLAG2_UNSET', Char(25), 32768),
	Insn('CHAR_SET_CHCP', Char(26), 32),
	Insn('CHAR_SET_FRAME', Char(26), 12),
	Insn('CHAR_FLAG1_SET', Char(26), 32768),
	Insn('CHAR_SET_POS', Char(26), (13400, 1300, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(26), 128),
	Insn('CHAR_FLAG2_UNSET', Char(26), 32768),
	Insn('CHAR_SET_CHCP', Char(27), 33),
	Insn('CHAR_SET_FRAME', Char(27), 0),
	Insn('CHAR_FLAG1_SET', Char(27), 32768),
	Insn('CHAR_SET_POS', Char(27), (12400, 1400, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(27), 128),
	Insn('CHAR_FLAG2_UNSET', Char(27), 32768),
	Insn('CHAR_SET_CHCP', Char(28), 32),
	Insn('CHAR_SET_FRAME', Char(28), 12),
	Insn('CHAR_FLAG1_SET', Char(28), 32768),
	Insn('CHAR_SET_POS', Char(28), (12000, 1300, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(28), 128),
	Insn('CHAR_FLAG2_UNSET', Char(28), 32768),
	Insn('CHAR_SET_CHCP', Char(29), 33),
	Insn('CHAR_SET_FRAME', Char(29), 0),
	Insn('CHAR_FLAG1_SET', Char(29), 32768),
	Insn('CHAR_SET_POS', Char(29), (13000, 1400, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(29), 128),
	Insn('CHAR_FLAG2_UNSET', Char(29), 32768),
	Insn('CHAR_SET_CHCP', Char(30), 32),
	Insn('CHAR_SET_FRAME', Char(30), 12),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('CHAR_SET_POS', Char(30), (13400, 1300, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('CHAR_SET_CHCP', Char(31), 33),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_FLAG1_SET', Char(31), 32768),
	Insn('CHAR_SET_POS', Char(31), (12400, 1400, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_CHCP', Char(32), 32),
	Insn('CHAR_SET_FRAME', Char(32), 12),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_SET_POS', Char(32), (12000, 1300, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_CHCP', Char(33), 33),
	Insn('CHAR_SET_FRAME', Char(33), 0),
	Insn('CHAR_FLAG1_SET', Char(33), 32768),
	Insn('CHAR_SET_POS', Char(33), (12400, 1400, 2600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_CHCP', Char(34), 32),
	Insn('CHAR_SET_FRAME', Char(34), 12),
	Insn('CHAR_FLAG1_SET', Char(34), 32768),
	Insn('CHAR_SET_POS', Char(34), (12000, 1300, 2600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(34), 128),
	Insn('CHAR_FLAG2_UNSET', Char(34), 32768),
	Insn('CHAR_SET_CHCP', Char(35), 33),
	Insn('CHAR_SET_FRAME', Char(35), 0),
	Insn('CHAR_FLAG1_SET', Char(35), 32768),
	Insn('CHAR_SET_POS', Char(35), (13000, 1400, 2600), 0),
	Insn('CHAR_SET_CHCP', Char(36), 32),
	Insn('CHAR_SET_FRAME', Char(36), 14),
	Insn('CHAR_FLAG1_SET', Char(36), 32768),
	Insn('CHAR_SET_POS', Char(36), (13400, 1300, 2600), 0),
	Insn('CHAR_SET_CHCP', Char(37), 32),
	Insn('CHAR_SET_FRAME', Char(37), 7),
	Insn('CHAR_FLAG1_SET', Char(37), 32768),
	Insn('CHAR_SET_POS', Char(37), (12700, 1400, 5500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(37), 128),
	Insn('CHAR_FLAG2_UNSET', Char(37), 32768),
	Insn('CHAR_SET_CHCP', Char(38), 32),
	Insn('CHAR_SET_FRAME', Char(38), 7),
	Insn('CHAR_FLAG1_SET', Char(38), 32768),
	Insn('CHAR_SET_POS', Char(38), (12700, 1400, 3500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(38), 128),
	Insn('CHAR_FLAG2_UNSET', Char(38), 32768),
	Insn('CHAR_SET_CHCP', Char(39), 33),
	Insn('CHAR_SET_FRAME', Char(39), 0),
	Insn('CHAR_FLAG1_SET', Char(39), 32768),
	Insn('CHAR_SET_POS', Char(39), (16000, 750, 5500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(39), 128),
	Insn('CHAR_FLAG2_UNSET', Char(39), 32768),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(25), 12),
			Insn('CHAR_SET_FRAME', Char(27), 12),
			Insn('CHAR_SET_FRAME', Char(29), 12),
			Insn('CHAR_SET_FRAME', Char(31), 12),
			Insn('CHAR_SET_FRAME', Char(33), 12),
			Insn('CHAR_SET_FRAME', Char(35), 12),
			Insn('CHAR_FLAG1_SET', Char(26), 128),
			Insn('CHAR_FLAG2_SET', Char(26), 32768),
			Insn('CHAR_FLAG1_SET', Char(28), 128),
			Insn('CHAR_FLAG2_SET', Char(28), 32768),
			Insn('CHAR_FLAG1_SET', Char(30), 128),
			Insn('CHAR_FLAG2_SET', Char(30), 32768),
			Insn('CHAR_FLAG1_SET', Char(32), 128),
			Insn('CHAR_FLAG2_SET', Char(32), 32768),
			Insn('CHAR_FLAG1_SET', Char(34), 128),
			Insn('CHAR_FLAG2_SET', Char(34), 32768),
			Insn('CHAR_FLAG1_SET', Char(36), 128),
			Insn('CHAR_FLAG2_SET', Char(36), 32768),
			Insn('CHAR_SET_POS', Char(25), (13100, 1400, 6600), 0),
			Insn('CHAR_SET_POS', Char(27), (12300, 1400, 6600), 0),
			Insn('CHAR_SET_POS', Char(29), (13100, 1400, 4600), 0),
			Insn('CHAR_SET_POS', Char(31), (12300, 1400, 4600), 0),
			Insn('CHAR_SET_POS', Char(33), (12300, 1400, 2600), 0),
			Insn('CHAR_SET_POS', Char(35), (13100, 1400, 2600), 0),
		]),
		(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(25), 14),
			Insn('CHAR_SET_FRAME', Char(27), 14),
			Insn('CHAR_SET_FRAME', Char(29), 14),
			Insn('CHAR_SET_FRAME', Char(31), 14),
			Insn('CHAR_SET_FRAME', Char(33), 14),
			Insn('CHAR_SET_FRAME', Char(35), 14),
		]),
		(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(25), 10),
			Insn('CHAR_SET_FRAME', Char(27), 10),
			Insn('CHAR_SET_FRAME', Char(29), 10),
			Insn('CHAR_SET_FRAME', Char(31), 10),
			Insn('CHAR_SET_FRAME', Char(33), 10),
			Insn('CHAR_SET_FRAME', Char(35), 10),
		]),
		(None, []),
	]),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (12600, 2350, 4800), 0),
	Insn('CAM_ROTATE', 40, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CAM_OFFSET', (12600, 1850, 4800), 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#14100077V#0305F#11P喂喂，这实在是相当美味啊！{wait}'
				'{page}'
				'#14100078V这真的是小琪\n'
				'做的吗！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_FRAME', Char(257), 1),
			Insn('SLEEP', 300),
			Insn('TEXT_TALK', Char(257), Text(
				'#14100079V#5P#0004F面条下锅之前的准备工作\n'
				'虽然是我做的……{wait}'
				'{page}'
				'#14100080V#0002F但下锅以后的全部烹调工作\n'
				'都是琪雅一个人完成的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_FRAME', Char(259), 1),
			Insn('SLEEP', 300),
			Insn('TEXT_TALK', Char(259), Text(
				'#14100081V#12P#0202F好厉害……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_FRAME', Char(258), 2),
			Insn('SLEEP', 150),
			Insn('TEXT_TALK', Char(258), Text(
				'#14100082V#0109F#5P嗯……\n'
				'这味道简直可以与餐厅里的相媲美了。{wait}'
				'{page}'
				'#14100083V#0102F琪雅，你实在是太厉害了！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#14100084V#0105F#5P好、好美味……{wait}'
				'{page}'
				'#14100085V这……这真的是琪雅\n'
				'做出来的吗！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#14100086V#11P#0004F面条下锅之前的准备工作\n'
				'虽然是我做的……{wait}'
				'{page}'
				'#14100087V#0000F但下锅以后的全部烹调工作\n'
				'都是琪雅一个人完成的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#14100088V#0305F#11P真的假的啊……！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_FRAME', Char(259), 1),
			Insn('SLEEP', 300),
			Insn('TEXT_TALK', Char(259), Text(
				'#14100089V#12P#0204F这已经可以与餐厅的料理一较高下了……{wait}'
				'{page}'
				'#14100090V#0202F琪雅，干得漂亮啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(259), 1),
			Insn('SLEEP', 300),
			Insn('TEXT_TALK', Char(259), Text(
				'#14100091V#12P#0205F……真美味……{wait}'
				'{page}'
				'#14100092V这个，真的是\n'
				'琪雅做的吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_FRAME', Char(257), 1),
			Insn('SLEEP', 150),
			Insn('TEXT_TALK', Char(257), Text(
				'#14100093V#5P#0000F面条下锅之前的准备工作\n'
				'虽然是我做的……{wait}'
				'{page}'
				'#14100094V但下锅以后的全部烹调工作\n'
				'都是琪雅一个人完成的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_FRAME', Char(258), 2),
			Insn('SLEEP', 150),
			Insn('TEXT_TALK', Char(258), Text(
				'#14100095V#0102F#5P厉、厉害……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#14100096V#0305F#11P哎呀，这绝对达到了\n'
				'餐厅厨师的水准啊。{wait}'
				'{page}'
				'#14100097V#0309F小琪，你很有一套嘛！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100098V#6P#1109F嘿嘿嘿～\n'
		'大家觉得好吃就好啦～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(259), 1),
	Insn('SLEEP', 100),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100099V#5P#0000F莫非琪雅是……\n'
		'厨师家的孩子吗？{wait}'
		'{page}'
		'#14100100V#0006F如果她的父母健在，\n'
		'现在肯定担心得不得了吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100101V#0103F#5P……是啊。\n'
		'不过，这也没办法呢。{wait}'
		'{page}'
		'#14100102V#0108F都已经借助了游击士协会的情报网，\n'
		'却仍然没能查到任何情报……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14100103V#6P#0208F是出身于非常偏僻的边境地区呢，\n'
		'还是有什么隐情……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100104V#6P#1100F嗯～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100105V#0306F#11P算了吧，要是真的开始考虑那些问题，\n'
		'可就没完没了了。{wait}'
		'{page}'
		'#14100106V#0300F在找到线索之前，就把她\n'
		'当成是我们的孩子，这不也很好吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100107V#5P#0004F这个嘛……{wait}'
		'{page}'
		'#14100108V#0002F──哈哈，不过课长他\n'
		'居然不在，还真是不走运啊。{wait}'
		'{page}'
		'#14100109V难得有机会可以吃到琪雅亲手\n'
		'做的料理，他却白白错过了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14100110V#6P#0200F课长是在警察局总部开会吗……\n'
		'最近，会议似乎有些频繁啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100111V#0105F#5P是啊……莫非是出了什么事吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 821, 0, 2, 100),
	Insn('OBJ_FLAG_UNSET', Object(13), 4),
	Insn('OBJ_FLAG_SET', Object(13), 4096),
	Insn('0x70', Object(13), b'\x00\x00'),
	Insn('0x74', Object(13), 7680),
	Insn('0x71', Object(13), b'\x00\x00', 20, 32),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(257), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(258), 1),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(10), 1),
	Insn('CHAR_SET_FRAME', Char(260), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100112V#11P#0005F有通讯联系……是谁呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100113V#0300F#11P没有直接拨打ＥＮＩＧＭＡ，\n'
		'看来应该不是课长或小芙兰啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(257), 4),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_POS', Char(257), (14100, 850, 7600), 270),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('0x0D'),
	Insn('0x92', Char(257), 13800, 12000, 500),
	Insn('CAM_OFFSET', (13800, 1850, 12000), 2500),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (13800, 850, 12000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('CHAR_ROTATE', Char(257), 0, 500),
	Insn('0x6F', b'\x01'),
	Insn('OBJ_FLAG_UNSET', Object(13), 32),
	Insn('0x70', Object(13), b'2\x00'),
	Insn('SOUND_STOP', 821),
	Insn('SOUND_PLAY', 822, 0, 0, 100),
	Insn('FADE_ON', 500, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#14100114V#0000F您好，这里是克洛斯贝尔警察局丄\n'
		'特务支援课。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('女孩的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14100115V啊，罗伊德警官吗？{wait}'
		'{page}'
		'#14100116V那个……我是诺艾儿，\n'
		'就是警备队的希卡上士。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14100117V#0009F啊，好久不见，\n'
		'大概有一个月了吧。{wait}'
		'{page}'
		'#14100118V#0002F怎么了？\n'
		'有什么任务要委托给支援课吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('诺艾儿的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14100119V嗯，其实是……{wait}'
		'{page}'
		'#14100120V我个人有些私事想与\n'
		'支援课的各位商量一下……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14100121V#0005F要商量私事……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('诺艾儿的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14100122V啊，虽然是私事，\n'
		'但应该也属于工作的范畴……{wait}'
		'{page}'
		'#14100123V那个，很抱歉，\n'
		'这么突然和你们联系……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14100124V#0004F哪里，现在正好是午休时间，\n'
		'没关系的。{wait}'
		'{page}'
		'#14100125V#0001F你现在在哪里呢？\n'
		'方便的话，就直接过来和我们面谈如何？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('诺艾儿的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14100126V真、真的吗？{wait}'
		'{page}'
		'#14100127V我现在正好就在\n'
		'克洛斯贝尔市的北出口。{wait}'
		'{page}'
		'#14100128V那么，我可以马上前去拜访吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14100129V#0004F嗯，没问题，我们会在这里等你。{wait}'
		'{page}'
		'#14100130V#0005F对了，如果愿意的话，\n'
		'就来和我们一起吃午餐吧？{wait}'
		'{page}'
		'#14100131V我们准备了一些简单的通心粉，\n'
		'如果不嫌弃，就来一起吃吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('诺艾儿的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14100132V啊，不用，那倒是不必……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('SOUND_PLAY', 932, 0, 0, 100),
	Insn('SLEEP', 2500),
	Insn('SOUND_PLAY', 1496, 0, 255, 100),
	Insn('SLEEP', 2000),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('诺艾儿的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14100133V#2S……不好意思……\n'
		'还是麻烦你们吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14100134V#0002F哈哈，了解。\n'
		'那就快点过来吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('诺艾儿的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14100135V是！{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('OBJ_FLAG_SET', Object(13), 4),
	Insn('SOUND_PLAY', 822, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('CHAR_ROTATE', Char(257), 180, 500),
	Insn('CAM_OFFSET', (12600, 1850, 4800), 2500),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (14100, 850, 7600), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('SLEEP', 300),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(257), 4),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_POS', Char(257), (13900, 900, 6650), 270),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100136V#0105F#6P是谁打来的啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100137V#11P#0000F啊，是诺艾儿上士。{wait}'
		'{page}'
		'#14100138V好像是有什么事情\n'
		'想来和我们商量……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100139V#0305F#11P哎～\n'
		'这可真少见啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100140V#6P#1110F怎么了怎么了，有谁要来吗～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14100141V#12P#0204F嗯，是警备队的大姐姐哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(10), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100142V#6P#1105F警备队？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100143V#5P#0002F她好像还没吃午饭呢，\n'
		'再去多煮一份面条吧。{wait}'
		'{page}'
		'#14100144V琪雅，还要来帮忙吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(10), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100145V#6P#1109F嗯！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 26000, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('CAM_OFFSET', (13090, 1850, 5300), 0),
	Insn('CAM_ROTATE', 40, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 26000, 0),
	Insn('CHAR_FLAG1_SET', Char(265), 4),
	Insn('CHAR_SET_CHCP', Char(265), 34),
	Insn('CHAR_SET_FRAME', Char(265), 0),
	Insn('CHAR_SET_POS', Char(265), (13900, 900, 6650), 270),
	Insn('CHAR_FLAG1_UNSET', Char(265), 128),
	Insn('CHAR_FLAG2_UNSET', Char(265), 32768),
	Insn('CHAR_SET_POS', Char(257), (13900, 900, 4600), 270),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('CHAR_SET_POS', Char(260), (13900, 900, 2550), 270),
	Insn('CHAR_SET_FRAME', Char(260), 2),
	Insn('CHAR_SET_CHCP', Char(25), 33),
	Insn('CHAR_SET_FRAME', Char(25), 0),
	Insn('CHAR_SET_CHCP', Char(26), 32),
	Insn('CHAR_SET_FRAME', Char(26), 24),
	Insn('CHAR_FLAG1_SET', Char(26), 32768),
	Insn('CHAR_SET_POS', Char(26), (13100, 1300, 7250), 0),
	Insn('CHAR_FLAG1_UNSET', Char(26), 128),
	Insn('CHAR_FLAG2_UNSET', Char(26), 32768),
	Insn('CHAR_SET_CHCP', Char(27), 33),
	Insn('CHAR_SET_FRAME', Char(27), 0),
	Insn('CHAR_SET_CHCP', Char(28), 32),
	Insn('CHAR_SET_FRAME', Char(28), 24),
	Insn('CHAR_FLAG1_SET', Char(28), 32768),
	Insn('CHAR_SET_POS', Char(28), (12300, 1300, 7250), 0),
	Insn('CHAR_FLAG1_UNSET', Char(28), 128),
	Insn('CHAR_FLAG2_UNSET', Char(28), 32768),
	Insn('CHAR_SET_CHCP', Char(29), 33),
	Insn('CHAR_SET_FRAME', Char(29), 0),
	Insn('CHAR_SET_CHCP', Char(30), 32),
	Insn('CHAR_SET_FRAME', Char(30), 24),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('CHAR_SET_POS', Char(30), (13100, 1300, 5200), 0),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('CHAR_SET_CHCP', Char(31), 33),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_SET_CHCP', Char(32), 32),
	Insn('CHAR_SET_FRAME', Char(32), 24),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_SET_POS', Char(32), (12300, 1300, 5200), 0),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_CHCP', Char(33), 33),
	Insn('CHAR_SET_FRAME', Char(33), 0),
	Insn('CHAR_SET_CHCP', Char(34), 32),
	Insn('CHAR_SET_FRAME', Char(34), 24),
	Insn('CHAR_FLAG1_SET', Char(34), 32768),
	Insn('CHAR_SET_POS', Char(34), (12300, 1300, 3150), 0),
	Insn('CHAR_FLAG1_UNSET', Char(34), 128),
	Insn('CHAR_FLAG2_UNSET', Char(34), 32768),
	Insn('CHAR_SET_CHCP', Char(35), 33),
	Insn('CHAR_SET_FRAME', Char(35), 0),
	Insn('CHAR_SET_CHCP', Char(36), 32),
	Insn('CHAR_SET_FRAME', Char(36), 24),
	Insn('CHAR_FLAG1_SET', Char(36), 32768),
	Insn('CHAR_SET_POS', Char(36), (13100, 1300, 3150), 0),
	Insn('CHAR_FLAG1_UNSET', Char(35), 128),
	Insn('CHAR_FLAG2_UNSET', Char(35), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(36), 128),
	Insn('CHAR_FLAG2_UNSET', Char(36), 32768),
	Insn('CHAR_FLAG1_SET', Char(37), 128),
	Insn('CHAR_FLAG2_SET', Char(37), 32768),
	Insn('CHAR_FLAG1_SET', Char(38), 128),
	Insn('CHAR_FLAG2_SET', Char(38), 32768),
	Insn('CHAR_FLAG1_SET', Char(39), 128),
	Insn('CHAR_FLAG2_SET', Char(39), 32768),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(25), 13),
			Insn('CHAR_SET_FRAME', Char(27), 13),
			Insn('CHAR_SET_FRAME', Char(29), 13),
			Insn('CHAR_SET_FRAME', Char(31), 13),
			Insn('CHAR_SET_FRAME', Char(33), 13),
			Insn('CHAR_SET_FRAME', Char(35), 13),
		]),
		(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(25), 15),
			Insn('CHAR_SET_FRAME', Char(27), 15),
			Insn('CHAR_SET_FRAME', Char(29), 15),
			Insn('CHAR_SET_FRAME', Char(31), 15),
			Insn('CHAR_SET_FRAME', Char(33), 15),
			Insn('CHAR_SET_FRAME', Char(35), 15),
		]),
		(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(25), 11),
			Insn('CHAR_SET_FRAME', Char(27), 11),
			Insn('CHAR_SET_FRAME', Char(29), 11),
			Insn('CHAR_SET_FRAME', Char(31), 11),
			Insn('CHAR_SET_FRAME', Char(33), 11),
			Insn('CHAR_SET_FRAME', Char(35), 11),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_CHCP', Char(12), 5),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('CHAR_SET_POS', Char(12), (16500, 850, 6400), 225),
	Insn('CHAR_FLAG1_UNSET', Char(12), 1),
	Insn('IMG_0xCA', Insn('1', (ResId(3), 0))),
	Insn('IMG_LOAD', ResId(3), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis160.itp'),
	Insn('SLEEP', 1000),
	Insn('CAM_DISTANCE', 25000, 2000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100146V#11P#0504F多谢款待。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(265), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100147V#5P#0502F──真是太好吃了！\n'
		'这真是琪雅做的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100148V#6P#1100F嗯，是呀～{wait}'
		'{page}'
		'#14100149V#1105F不过下锅之前的……准备工作\n'
		'是罗伊德做的～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100150V#5P#0509F哈哈，那你也已经很厉害啦！{wait}'
		'{page}'
		'#14100151V#0504F嗯～关于琪雅的事情，\n'
		'我从芙兰那里也听说了不少……{wait}'
		'{page}'
		'#14100152V#0502F没想到不仅可爱，\n'
		'而且还身怀这种绝技呢！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100153V#0002F#11P哈哈，芙兰她好像\n'
		'非常喜欢琪雅呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14100154V#6P#0204F#N每次通过终端联系时，\n'
		'她都要我们把琪雅叫过来\n'
		'和她说几句话呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100155V#5P#0509F啊哈哈，我妹妹\n'
		'最喜欢可爱的小孩子了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100156V#6P#1110F那个那个，诺艾儿\n'
		'是芙兰的姐姐吗～？{wait}'
		'{page}'
		'#14100157V这么一说，不止是头发的颜色一样，\n'
		'连长相都非常像呢～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100158V#5P#0505F是、是吗？{wait}'
		'{page}'
		'#14100159V#0502F不过我并不是她那种\n'
		'可爱的类型啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(265), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100160V#5P#0503F噢噢……\n'
		'好险，差点就把正事都给忘了。{wait}'
		'{page}'
		'#14100161V#0501F──那个，我这就开始\n'
		'进入正题了，可以吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100162V#0001F#11P嗯，当然没问题。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100163V#0301F你要说的事，好像与山道尽头的\n'
		'某个遗迹有关吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100164V#5P#0508F嗯，那是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('BGM_STOP', 3500),
	Insn('BGM_WAIT'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#14100165V#0005F──幽灵出没的遗迹？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('BGM_PLAY', b'o\x00\x00'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100166V#5P#0503F……正是。{wait}'
		'{page}'
		'#14100167V正确地说，也不知道是幽灵，\n'
		'还是传说中的妖怪……{wait}'
		'{page}'
		'#14100168V#0501F总之，确实是有前所未见的\n'
		'奇异魔兽在出没……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100169V#0303F当初负责调查那里的\n'
		'贝尔加德门部队已经撤回了……{wait}'
		'{page}'
		'#14100170V#0301F于是就由唐古拉姆门的你们\n'
		'来负责收拾烂摊子吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100171V#5P#0501F嗯……{wait}'
		'{page}'
		'#14100172V#0506F而且，昨天我和几名队员\n'
		'试着进去调查了一下……{wait}'
		'{page}'
		'#14100173V但出现了很多十分诡异的魔兽，\n'
		'大家都吓得不轻……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 1700, (40, 43, 100, 3)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100174V#0105F#6P等、等一下。{wait}'
		'{page}'
		'#14100175V#0109F……莫非……\n'
		'是想让我们帮忙驱赶幽灵吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(265), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100176V#11P#0505F也、也不是啦……\n'
		'主要目的还是希望你们能彻底\n'
		'调查一下遗迹内部……{wait}'
		'{page}'
		'#14100177V#0506F……果然不行吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100178V#0008F#11P嗯、嗯……{wait}'
		'{page}'
		'#14100179V#0003F虽说是要调查遗迹，\n'
		'但具体应该如何着手，\n'
		'我们也完全没有头绪啊……{wait}'
		'{page}'
		'#14100180V#0000F──但既然你都来找我们了，\n'
		'想必已经找到一些着手点了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(265), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(265), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100181V#5P#0500F……所料不错，不愧是罗伊德警官啊。{wait}'
		'{page}'
		'#14100182V#0503F其实……\n'
		'在和那些怪物战斗的时候……{wait}'
		'{page}'
		'#14100183V#0501F感觉导力魔法的效果特性似乎\n'
		'与平常有些不同呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
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
		'#14100184V#0013F#11P什么……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100185V#0105F#6P这，莫非又是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14100186V#6P#0203F#N和我们以前进入\n'
		'『星见之塔』时一样……{wait}'
		'{page}'
		'#14100187V#0201F时、空、幻这三种上级属性\n'
		'也在产生影响……是这种感觉吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100188V#5P#0506F嗯……\n'
		'我也想起了那时的事。{wait}'
		'{page}'
		'#14100189V所以，我才想是不是应该来\n'
		'让大家也了解一下情况，听听你们的意见……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100190V#0003F#11P原来如此……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100191V#0106F#6P所以才来支援课……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100192V#5P#0508F各位，我非常理解\n'
		'你们平时都很忙，可是……{wait}'
		'{page}'
		'#14100193V#0506F再这么下去，司令阁下\n'
		'也许又要下达放置不管的命令了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100194V#0301F哈，那个只懂鸵鸟政策的司令，\n'
		'很有可能会那样做吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100195V#0003F#11P嗯……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100196V#0000F#11P各位，既然上士特意提出请求，\n'
		'我们就协助她一下如何？{wait}'
		'{page}'
		'#14100197V虽然要跑到市外去执行任务，\n'
		'但放着不管的话还是稍微有些在意。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100198V#0108F#5P也、也有道理啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14100199V#6P#0204F#N我没有异议。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100200V#0304F#11P我也没问题啊。{wait}'
		'{page}'
		'#14100201V#0302F不过大小姐看起来\n'
		'好像有点不太愿意啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100202V#0113F#5P才、才没有那种事！{wait}'
		'{page}'
		'#14100203V#0112F谁会幼稚到像小孩子\n'
		'一样害怕幽灵──啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100204V#0304F#11P说漏嘴了吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100205V#6P#1105F艾莉，害怕幽灵吗～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100206V#0109F#5P才、才没有呢！{wait}'
		'{page}'
		'#14100207V只是，那个……面对那种不明究竟的对手，\n'
		'我们是不是应该采取更慎重的对策呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(265), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100208V#11P#0506F我理解你的心情……{wait}'
		'{page}'
		'#14100209V如果不是任务在身，\n'
		'连我也都不想再调查下去了呢。{wait}'
		'{page}'
		'#14100210V#0508F……可是，如果就这么罢手，\n'
		'然后被上面认定为什么事情都没发生的话，\n'
		'我实在是有些难以接受……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100211V#0108F#6P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100212V#0006F#11P这种心情我非常理解。{wait}'
		'{page}'
		'#14100213V#0002F那个，要不这样吧，\n'
		'艾莉就留下来看家好了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100214V#0113F#5P好啦好啦，我明白啦！{wait}'
		'{page}'
		'#14100215V#0107F我也去，和大家一起去！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14100216V#6P#0202F#N艾莉前辈好像豁出去了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100217V#0303F#11P哎呀呀，真是爱逞强。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100218V#0113F先、先不说这些……{wait}'
		'{page}'
		'#14100219V#0100F好像也有其它支援请求呢，\n'
		'那些都要怎么处理？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100220V#0003F#11P说得也是啊，嗯……{wait}'
		'{page}'
		'#14100221V#0008F如果先把那些都处理完，然后\n'
		'再与上士会合的话，未免也太麻烦……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(265), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100222V#5P#0505F啊，这样的话……{wait}'
		'{page}'
		'#14100223V#0502F今天一天，我就和大家\n'
		'一起行动好了。{wait}'
		'{page}'
		'#14100224V而且我开着警备队的车辆，不管大家\n'
		'想去哪里，我都可以开车送你们哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100225V#0005F#11P哎，这样好吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100226V#5P#0504F当然没问题啦，小事一桩。{wait}'
		'{page}'
		'#14100227V#0500F等大家把该办的事情都\n'
		'办完之后，我们再一起去山道的\n'
		'遗迹那边，如何？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100228V#0100F#6P原来如此……\n'
		'这样的话，行动应该会更有效率吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14100229V#6P#0204F#N还要麻烦您开车送我们，\n'
		'真是十分感谢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100230V#0309F嘿，我们这次也能好好体验一下\n'
		'一课那些家伙的待遇了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100231V#0004F#11P──那就这么决定了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100232V#0000F#11P琪雅，\n'
		'我们下午还要再次外出……{wait}'
		'{page}'
		'#14100233V你和赛特一起\n'
		'乖乖看家，可以吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(10), Text(
		'#14100234V#6P#1104F嗯，没问题～{wait}'
		'{page}'
		'#14100235V#1110F罗伊德，你们也要\n'
		'加油赶走幽灵啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 26000, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('0xE3', 10),
	Insn('SLEEP', 1000),
	Insn('IMG_0xC9', (ResId(3), 3), Color(0xFFFFFFFF), 800, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(3), 3))),
	Insn('TEXT_RESET', b'\x03'),
	Insn('IMG_0xC9', (ResId(3), 3), Color(0x00FFFFFF), 800, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(3), 3))),
	Insn('0xE3', 11),
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
	Insn('CHAR_FLAG1_UNSET', Char(265), 4),
	Insn('CHAR_SET_CHCP', Char(265), 255),
	Insn('CHAR_SET_FRAME', Char(265), 0),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0xD5', 33),
	Insn('0xD5', 34),
	Insn('0xD5', 35),
	Insn('0xD5', 36),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 102), Insn('SET'), Insn('END')])),
	Insn('0xB8', 100, 102),
	Insn('SOUND_STOP', 821),
	Insn('FLAG_SET', Flag(746)),
	Insn('NEW_SCENE', 'c0100', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][45] = [
	Insn('CHAR_FLAG1_SET', Char(10), 64),
	Insn('CHAR_FLAG1_UNSET', Char(10), 4),
	Insn('CHAR_SET_CHCP', Char(10), 35),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('FORK', 10, 1, [
		Insn('0x95', Char(254), (800, 850, 10000), 5000, 1),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('CAM_OFFSET', (200, 1000, 3500), 1500),
	Insn('CAM_DISTANCE', 25000, 1500),
	Insn('FORK', 10, 1, [
		Insn('0x95', Char(254), (200, 0, 3500), 5000, 0),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('CHAR_SET_CHCP', Char(10), 36),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('SOUND_PLAY', 819, 0, 0, 100),
	Insn('FORK', 257, 2, [
		Insn('0xA6', Char(254), 0, 50, 500, 3000),
	]),
	Insn('SLEEP', 500),
	Insn('RETURN'),
]

data['code'][46] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('LOAD_CHCP', 'apl/ch50090', 32),
	Insn('LOAD_CHCP', 'apl/ch50092', 33),
	Insn('LOAD_CHCP', 'apl/ch50011', 34),
	Insn('SOUND_LOAD', 806),
	Insn('CAM_OFFSET', (12600, 2350, 4800), 0),
	Insn('CAM_ROTATE', 40, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_SET_CHCP', Char(259), 11),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_SET_CHCP', Char(260), 12),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_POS', Char(257), (13900, 900, 4600), 270),
	Insn('CHAR_SET_POS', Char(258), (11300, 900, 6650), 90),
	Insn('CHAR_SET_POS', Char(259), (11300, 900, 2550), 90),
	Insn('CHAR_SET_POS', Char(260), (13900, 900, 2550), 270),
	Insn('CHAR_FLAG1_SET', Char(10), 4),
	Insn('CHAR_SET_CHCP', Char(10), 7),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('CHAR_SET_POS', Char(10), (11300, 900, 4600), 90),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 4),
	Insn('CHAR_SET_CHCP', Char(8), 4),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('CHAR_SET_POS', Char(8), (13900, 900, 6650), 270),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_SET_CHCP', Char(12), 9),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('CHAR_SET_POS', Char(12), (16000, 850, 6400), 180),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG2_UNSET', Char(12), 32768),
	Insn('FORK_FUNC', Char(12), 1, Function((0, 40))),
	Insn('CHAR_SET_CHCP', Char(25), 33),
	Insn('CHAR_SET_FRAME', Char(25), 5),
	Insn('CHAR_FLAG1_SET', Char(25), 32768),
	Insn('CHAR_SET_POS', Char(25), (13000, 1400, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(25), 128),
	Insn('CHAR_FLAG2_UNSET', Char(25), 32768),
	Insn('CHAR_SET_CHCP', Char(26), 32),
	Insn('CHAR_SET_FRAME', Char(26), 12),
	Insn('CHAR_FLAG1_SET', Char(26), 32768),
	Insn('CHAR_SET_POS', Char(26), (13400, 1300, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(26), 128),
	Insn('CHAR_FLAG2_UNSET', Char(26), 32768),
	Insn('CHAR_SET_CHCP', Char(27), 33),
	Insn('CHAR_SET_FRAME', Char(27), 5),
	Insn('CHAR_FLAG1_SET', Char(27), 32768),
	Insn('CHAR_SET_POS', Char(27), (12400, 1400, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(27), 128),
	Insn('CHAR_FLAG2_UNSET', Char(27), 32768),
	Insn('CHAR_SET_CHCP', Char(28), 32),
	Insn('CHAR_SET_FRAME', Char(28), 12),
	Insn('CHAR_FLAG1_SET', Char(28), 32768),
	Insn('CHAR_SET_POS', Char(28), (12000, 1300, 6600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(28), 128),
	Insn('CHAR_FLAG2_UNSET', Char(28), 32768),
	Insn('CHAR_SET_CHCP', Char(29), 33),
	Insn('CHAR_SET_FRAME', Char(29), 5),
	Insn('CHAR_FLAG1_SET', Char(29), 32768),
	Insn('CHAR_SET_POS', Char(29), (13000, 1400, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(29), 128),
	Insn('CHAR_FLAG2_UNSET', Char(29), 32768),
	Insn('CHAR_SET_CHCP', Char(30), 32),
	Insn('CHAR_SET_FRAME', Char(30), 12),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('CHAR_SET_POS', Char(30), (13400, 1300, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('CHAR_SET_CHCP', Char(31), 33),
	Insn('CHAR_SET_FRAME', Char(31), 5),
	Insn('CHAR_FLAG1_SET', Char(31), 32768),
	Insn('CHAR_SET_POS', Char(31), (12400, 1400, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_CHCP', Char(32), 32),
	Insn('CHAR_SET_FRAME', Char(32), 12),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_SET_POS', Char(32), (12000, 1300, 4600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_CHCP', Char(33), 33),
	Insn('CHAR_SET_FRAME', Char(33), 5),
	Insn('CHAR_FLAG1_SET', Char(33), 32768),
	Insn('CHAR_SET_POS', Char(33), (12400, 1400, 2600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_CHCP', Char(34), 32),
	Insn('CHAR_SET_FRAME', Char(34), 12),
	Insn('CHAR_FLAG1_SET', Char(34), 32768),
	Insn('CHAR_SET_POS', Char(34), (12000, 1300, 2600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(34), 128),
	Insn('CHAR_FLAG2_UNSET', Char(34), 32768),
	Insn('CHAR_SET_CHCP', Char(35), 33),
	Insn('CHAR_SET_FRAME', Char(35), 5),
	Insn('CHAR_FLAG1_SET', Char(35), 32768),
	Insn('CHAR_SET_POS', Char(35), (13000, 1400, 2600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(35), 128),
	Insn('CHAR_FLAG2_UNSET', Char(35), 32768),
	Insn('CHAR_SET_CHCP', Char(36), 32),
	Insn('CHAR_SET_FRAME', Char(36), 12),
	Insn('CHAR_FLAG1_SET', Char(36), 32768),
	Insn('CHAR_SET_POS', Char(36), (13400, 1300, 2600), 0),
	Insn('CHAR_FLAG1_UNSET', Char(36), 128),
	Insn('CHAR_FLAG2_UNSET', Char(36), 32768),
	Insn('CHAR_SET_CHCP', Char(37), 32),
	Insn('CHAR_SET_FRAME', Char(37), 7),
	Insn('CHAR_FLAG1_SET', Char(37), 32768),
	Insn('CHAR_SET_POS', Char(37), (12700, 1400, 5500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(37), 128),
	Insn('CHAR_FLAG2_UNSET', Char(37), 32768),
	Insn('CHAR_SET_CHCP', Char(38), 32),
	Insn('CHAR_SET_FRAME', Char(38), 7),
	Insn('CHAR_FLAG1_SET', Char(38), 32768),
	Insn('CHAR_SET_POS', Char(38), (12700, 1400, 3500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(38), 128),
	Insn('CHAR_FLAG2_UNSET', Char(38), 32768),
	Insn('CHAR_SET_CHCP', Char(39), 33),
	Insn('CHAR_SET_FRAME', Char(39), 0),
	Insn('CHAR_FLAG1_SET', Char(39), 32768),
	Insn('CHAR_SET_POS', Char(39), (16000, 750, 5500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(39), 128),
	Insn('CHAR_FLAG2_UNSET', Char(39), 32768),
	Insn('IMG_LOAD', ResId(0), 180, 0, b'\xb4\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis007.itp'),
	Insn('CAM_OFFSET', (12600, 1850, 4800), 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200001V#0004F#11P话说，这可真让人吃惊啊……{wait}'
		'{page}'
		'#14200002V#0000F这个煎荷包蛋……\n'
		'真的是琪雅做的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200003V#0102F#5P呵呵，是呀。{wait}'
		'{page}'
		'#14200004V#0109F手艺实在太精湛了，\n'
		'我在旁边都看得入迷了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14200005V#11P#1002F嗯，煎得还真是不老不嫩啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200006V#0304F#11P培根也煎得嫩滑酥脆，\n'
		'简直挑不出任何毛病。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200007V#6P#0204F昨天帮我一起做\n'
		'奶汁炖菜时也是，\n'
		'技艺相当高超……{wait}'
		'{page}'
		'#14200008V#0202F果然是有过丰富的\n'
		'料理经验吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14200009V#6P#1111F嗯～有过那种事吗？{wait}'
		'{page}'
		'#14200010V#1102F我好像没想那么多，手\n'
		'不知不觉就自己动起来了～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200011V#0003F#11P嗯～制作料理的记忆\n'
		'大概是牢牢留存在了身体中……{wait}'
		'{page}'
		'#14200012V#0000F（……但即使如此，这么小的年龄\n'
		'\u3000就能做这么好，实在是很厉害……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(10), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(10), 2),
	Insn('TEXT_TALK', Char(10), Text(
		'#14200013V#5P#1101F那个那个，缇欧～{wait}'
		'{page}'
		'#14200014V你今天没事了吧～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(259), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200015V#12P#0205F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(8), 1),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200016V#0108F#5P看脸色好像\n'
		'不是很差，不过……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200017V#0301F#11P还是别太勉强了，\n'
		'多休息一下比较好吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200018V#6P#0204F不，没关系的。{wait}'
		'{page}'
		'#14200019V#0202F昨天也比较早休息。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14200020V#5P#1000F嗯……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200021V#0000F#5P算啦，反正现在也没有什么\n'
		'紧急的工作，不如就先──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 806, 0, 2, 100),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(257), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 1700, (38, 38, 250, 1)),
	Insn('EMOTE', Char(8), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(260), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200022V#0005F#11P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200023V#0305F#11P这么早就来联系，真少见啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200024V#0100F#5P也许是芙兰小姐吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200025V#0001F#11P那个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_SET', Char(257), 32),
	Insn('CHAR_FLAG1_SET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 34),
	Insn('CHAR_SET_FRAME', Char(257), 8),
	Insn('SOUND_STOP', 806),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('FADE_ON', 500, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14200026V#0000F您好，这里是特务支援课，\n'
		'我是罗伊德丄班宁斯──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('少年的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14200027V啊～啊～这些事情\n'
		'早就知道啦，用不着再说～！{wait}'
		'{page}'
		'#14200028V现在在哪里！正在干什么呢！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14200029V#0005F啊，是约纳吗？{wait}'
		'{page}'
		'#14200030V#0002F早安。\n'
		'夜行动物约纳这么早就起床，\n'
		'还真是少见啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('约纳的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14200031V哈，这当然是因为\n'
		'我熬夜干了一通宵啊。{wait}'
		'{page}'
		'#14200032V──啊啊，真是的！\n'
		'这种小事怎样都无所谓啦！{wait}'
		'{page}'
		'#14200033V不过，听你这口气，\n'
		'好像还什么都不知道吧！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14200034V#0005F什么都不知道……是指什么事呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('约纳的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14200035V哈，约纳大人今天就来个特别大服务，\n'
		'免费告诉你好了！{wait}'
		'{page}'
		'#14200036V在昨天的深夜──\n'
		'啊，不对，从日期来看应该算今天了。{wait}'
		'{page}'
		'#14200037V『黑月』的事务所似乎遭到了\n'
		'某些人的袭击呢！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('EMOTE', Char(257), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14200038V#0013F什么……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('约纳的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14200039V而且『黑月』那边似乎\n'
		'被压制得只能单方面的防守！{wait}'
		'{page}'
		'#14200040V受害情况好像相当严重呢！{wait}'
		'{page}'
		'#14200041V哈，至于袭击他们的人，\n'
		'不用说，肯定是鲁巴彻的那些家伙吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14200042V#0003F原来如此啊……{wait}'
		'{page}'
		'#14200043V#0000F谢谢，约纳。\n'
		'感谢你提供情报。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('约纳的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14200044V哈，下次可要记得报答我啊！{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('SOUND_PLAY', 825, 0, 0, 100),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200045V#6P#0205F约纳打来的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(257), 32),
	Insn('CHAR_FLAG1_UNSET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200046V#0006F#11P嗯嗯……看起来，\n'
		'似乎是发生了不得了的事件呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}罗伊德将约纳提供的情报转告了大家。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('EMOTE', Char(8), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(259), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(258), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(260), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200047V#0101F#5P真、真的吗……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200048V#0301F#11P喂喂，真的假的啊！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200049V#6P#0206F虽说是在半夜，\n'
		'但市区里居然会发生这种事……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14200050V#6P#1105F哎～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14200051V#5P#1003F嗯……{wait}'
		'{page}'
		'#14200052V如果情况属实，一课的人\n'
		'大概已经出动了吧……{wait}'
		'{page}'
		'#14200053V#1002F如果在意的话，你们也去吧。\n'
		'──不过还是先把饭吃完再说。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200054V#0001F是，遵命！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200055V#0005F#5P啊……\n'
		'缇欧，你没问题吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200056V#6P#0204F嗯，没问题。{wait}'
		'{page}'
		'#14200057V#0202F吃完早饭后，\n'
		'我们就去港湾区吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 26000, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
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
	Insn('CHAR_FLAG1_SET', Char(32), 128),
	Insn('CHAR_FLAG2_SET', Char(32), 32768),
	Insn('CHAR_FLAG1_SET', Char(33), 128),
	Insn('CHAR_FLAG2_SET', Char(33), 32768),
	Insn('CHAR_FLAG1_SET', Char(34), 128),
	Insn('CHAR_FLAG2_SET', Char(34), 32768),
	Insn('CHAR_FLAG1_SET', Char(35), 128),
	Insn('CHAR_FLAG2_SET', Char(35), 32768),
	Insn('CHAR_FLAG1_SET', Char(36), 128),
	Insn('CHAR_FLAG2_SET', Char(36), 32768),
	Insn('CHAR_FLAG1_SET', Char(37), 128),
	Insn('CHAR_FLAG2_SET', Char(37), 32768),
	Insn('CHAR_FLAG1_SET', Char(38), 128),
	Insn('CHAR_FLAG2_SET', Char(38), 32768),
	Insn('CHAR_FLAG1_SET', Char(39), 128),
	Insn('CHAR_FLAG2_SET', Char(39), 32768),
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
	Insn('CAM_OFFSET', (12000, 1850, 8700), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 340, 0),
	Insn('CAM_DISTANCE', 27500, 0),
	Insn('CHAR_SET_POS', Char(0), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(1), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(2), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(3), (12000, 850, 8700), 270),
	Insn('CHAR_SET_CHCP', Char(10), 1),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('CHAR_FLAG1_UNSET', Char(10), 4),
	Insn('0x4C', Char(10), -1),
	Insn('CHAR_SET_POS', Char(10), (122940, 0, 5100), 180),
	Insn('CHAR_SET_CHCP', Char(8), 0),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('CHAR_FLAG1_UNSET', Char(8), 4),
	Insn('0x4C', Char(8), -1),
	Insn('CHAR_SET_POS', Char(8), (124620, 30, 5490), 90),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(13), 128),
	Insn('CHAR_SET_POS', Char(13), (2970, 0, 4170), 225),
	Insn('FLAG_SET', Flag(1554)),
	Insn('0xC7', b'\x01\x00\x10\x00\x00'),
	Insn('QUEST', 74, Insn('TASK_SET', 7)),
	Insn('QUEST', 75, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 75, Insn('TASK_SET', 0)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 42, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 42, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 42, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 42, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 42, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 44, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 44, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 44, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 54, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 54, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 54, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 54, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 54, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 57, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 57, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('SOUND_STOP', 806),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][47] = [
	Insn('CHAR_SET_FRAME', Char(9), 0),
	Insn('TEXT_END', Char(9)),
	Insn('EVENT_BEGIN', 0),
	Insn('BGM_STOP', 3000),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'\x04\x02\x00'),
	Insn('LOAD_CHCP', 'chr/ch00900', 30),
	Insn('CAM_OFFSET', (64000, 1100, 8600), 0),
	Insn('CAM_ROTATE', 50, 17, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 24000, 0),
	Insn('CHAR_SET_POS', Char(257), (63000, 0, 6700), 0),
	Insn('CHAR_SET_POS', Char(258), (64300, 0, 6700), 0),
	Insn('CHAR_SET_POS', Char(259), (63200, 0, 5400), 0),
	Insn('CHAR_SET_POS', Char(260), (64500, 0, 5400), 0),
	Insn('CHAR_SET_FRAME', Char(9), 0),
	Insn('CHAR_SET_CHCP', Char(22), 30),
	Insn('CHAR_SET_FRAME', Char(22), 0),
	Insn('CHAR_SET_POS', Char(22), (57000, -1030, 3400), 90),
	Insn('CHAR_SET_COLOR', Char(22), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(10), (59000, 30, 3400), 90),
	Insn('CHAR_SET_COLOR', Char(10), Color(0x00FFFFFF), 0),
	Insn('0x4B', Char(10), -1),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis087.itp'),
	Insn('IMG_LOAD', ResId(1), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu00600.itp'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200622V#5P#1001F…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200623V#12P#0005F那个……课长？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200624V#0106F对、对不起，\n'
		'我们的报告大概很难懂吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200625V#5P#1003F不……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(9), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(9)),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200626V#5P#1001F这一连串的情报……{wait}'
		'{page}'
		'#14200627V如果我没猜错的话，\n'
		'应该全部都存在着某种关联。{wait}'
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
		'#14200628V#12P#0011F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200629V#0307F真的假的啊……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200630V#0101F这、这是怎么回事呢！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200631V#12P#0208F…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200632V#5P#1003F连续发生了这么多的事情，\n'
		'也许你们会感到有些混乱……{wait}'
		'{page}'
		'#14200633V但不妨试着把今天经历过的\n'
		'一系列见闻系统地归结到一起吧。{wait}'
		'{page}'
		'#14200634V#1002F特别是罗伊德──正是在这种时候，\n'
		'才需要你发挥出搜查官的本领。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200635V#12P#0011F啊，是的……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200636V#12P#0008F今天我们询问得来的情报，\n'
		'可以粗略归结为三条……{wait}'
		'{page}'
		'#14200637V#0003F从曹先生他们那里听来的，\n'
		'『黑月』受袭方面的情报……{wait}'
		'{page}'
		'#14200638V与格蕾丝小姐交换来的，\n'
		'关于鲁巴彻现状的情报……{wait}'
		'{page}'
		'#14200639V#0001F还有就是，玛因兹的矿工\n'
		'冈兹先生那方面的情报……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('FORK_AWAIT', Char(258), 2),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200640V#0100F应该存在着某些要素，能把这三类\n'
		'情报联系到一起吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200641V#0300F嗯……\n'
		'似乎能看出一点眉目了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(258), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200642V#6P#0000F好，那就来整理一下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EXPR_VAR', 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('FLAG_UNSET', Flag(3)),
	Insn('WHILE', [Insn('FLAG', 3), Insn('NOT'), Insn('END')], [
		Insn('FLAG_SET', Flag(3)),
		Insn('FADE_ON', 300, Color(0x00000000), 100),
		Insn('0x0D'),
		Insn('TEXT_SET_POS', -1, 20, -1, -1),
		Insn('TEXT_SET_NAME', Translate('')),
		Insn('TEXT_MESSAGE', Char(255), Text(
			'{color 5}{0x06}{0x18}#1K在『黑月』受袭方面的情报中，\n'
			'可能存在关联的要素是？{color 0}{wait}'
		)),
		Insn('MENU', 0, -1, -1, 0, Text(
			'袭击者的身体能力\n'
			'『黑月』总部的增援\n'
			'有关琪雅情报的提供者\n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('0x60', 0),
		Insn('TEXT_RESET', b'\x00'),
		Insn('0x5A'),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), [
				Insn('FLAG_UNSET', Flag(3)),
			]),
			(None, []),
		]),
		Insn('TEXT_SET_POS', -1, 20, -1, -1),
		Insn('TEXT_SET_NAME', Translate('')),
		Insn('TEXT_MESSAGE', Char(255), Text(
			'{color 5}{0x06}{0x18}#1K在鲁巴彻现状方面的情报中，\n'
			'可能存在关联的要素是？{color 0}{wait}'
		)),
		Insn('MENU', 0, -1, -1, 0, Text(
			'玛律克尼会长的动向\n'
			'将军犬作为战斗力投入使用\n'
			'无计划的组织运用\n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('0x60', 0),
		Insn('TEXT_RESET', b'\x00'),
		Insn('0x5A'),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 2), Insn('NE'), Insn('END')]), [
				Insn('FLAG_UNSET', Flag(3)),
			]),
			(None, []),
		]),
		Insn('TEXT_SET_POS', -1, 20, -1, -1),
		Insn('TEXT_SET_NAME', Translate('')),
		Insn('TEXT_MESSAGE', Char(255), Text(
			'{color 5}{0x06}{0x18}#1K在矿工冈兹方面的情报中，\n'
			'可能存在关联的要素是？{color 0}{wait}'
		)),
		Insn('MENU', 0, -1, -1, 0, Text(
			'从矿山镇失踪的时间\n'
			'在赌场与雷克多的比试\n'
			'所携带的蓝色药锭\n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('0x60', 0),
		Insn('TEXT_RESET', b'\x00'),
		Insn('0x5A'),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 2), Insn('NE'), Insn('END')]), [
				Insn('FLAG_UNSET', Flag(3)),
			]),
			(None, []),
		]),
		Insn('FADE_OFF', 300, Color(0x00000000)),
		Insn('0x0D'),
		Insn('IF', [
			(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
				Insn('IF', [
					(Expr([Insn('VAR', 5), Insn('CONST', 3), Insn('GT'), Insn('END')]), [
						Insn('EMOTE', Char(257), 0, 2000, (14, 15, 250, 2)),
						Insn('SOUND_PLAY', 23, 0, 0, 100),
						Insn('SLEEP', 1200),
						Insn('TEXT_TALK', Char(257), Text(
							'#14200643V#0006F#6P（嗯……\n'
							'\u3000好像还是不对啊。）{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('EMOTE', Char(257), 0, 2000, (34, 36, 250, 1)),
						Insn('SOUND_PLAY', 28, 0, 0, 100),
						Insn('SLEEP', 1300),
						Insn('TEXT_TALK', Char(257), Text(
							'#14200644V#0005F#6P（莫非，是这样吗……？）{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('FLAG_SET', Flag(3)),
					]),
					(None, [
						Insn('TEXT_TALK', Char(257), Text(
							'#14200645V#6P#0006F（不对……\n'
							'\u3000这些情报之间好像没什么关系。）{wait}'
							'{page}'
							'#14200646V#0001F（重新再选择一次吧。）{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('EXPR_VAR', 5, Expr([Insn('VAR', 5), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
					]),
				]),
			]),
			(None, [
				Insn('SWITCH', [Insn('VAR', 5), Insn('END')], {
					0: [
						Insn('QUEST_BONUS_DP', 76, 2),
						Insn('TEXT_TALK', Char(257), Text(
							'#14200647V#6P#0000F（没错……就是这个。）{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('BREAK'),
					],
					None: [
						Insn('QUEST_BONUS_DP', 76, 1),
						Insn('TEXT_TALK', Char(257), Text(
							'#14200648V#6P#0003F（……多半就是这个了。）{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('BREAK'),
					],
				}),
			]),
		]),
	]),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}【存在关联的要素】\n'
		'①袭击者的身体能力\n'
		'②无计划的组织运用\n'
		'③所携带的蓝色药锭{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200649V#0101F这、这个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200650V#0310F喂喂……\n'
		'这也太可疑了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200651V#6P#0006F但是，将这些联系到一起之后，\n'
		'我们就可以看清很多东西了。{wait}'
		'{page}'
		'#14200652V#0008F袭击『黑月』的那些\n'
		'黑手党所展现的身体能力……{wait}'
		'{page}'
		'#14200653V在赌场有如神助一般\n'
		'连战连胜的矿工冈兹先生……{wait}'
		'{page}'
		'#14200654V#0013F虽然看似毫无关联，\n'
		'但却有着一个相同点──他们的\n'
		'『潜在能力』都得到了提升。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('SLEEP', 500),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#14200655V#0013F如果说，造成这一切的原因\n'
		'是这个『蓝色药锭』……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#14200656V#0203F……也就表明，那些黑手党\n'
		'已经开始染指违禁药物了……{wait}'
		'{page}'
		'#14200657V而且不只将其\n'
		'流到了市民群体中，\n'
		'还用来对战斗力进行强化……{wait}'
		'{page}'
		'#14200658V#0201F……就是这么回事吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#14200659V#0006F嗯……\n'
		'虽然这目前还只是我们的臆测。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200660V#0101F不、不过，这样想的话，\n'
		'确实就可以解开很多疑问了。{wait}'
		'{page}'
		'#14200661V那个副头目在鲁巴彻组织内的\n'
		'统率力也已经开始下降，\n'
		'莫非……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200662V#0306F是因为那些靠药物获得力量，\n'
		'从而变得狂妄自大的部下们\n'
		'开始增多了吗……{wait}'
		'{page}'
		'#14200663V#0301F原来是这么回事吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200664V#5P#1003F──分析得很好。{wait}'
		'{page}'
		'#14200665V#1000F再加上伊安律师\n'
		'昨天说过的传闻。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200666V#12P#0005F是指那两位业绩突然激增的\n'
		'贸易商和证券经理吗……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200667V#0105F那、那难道是因为他们也\n'
		'服用了那种蓝色药锭……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200668V#5P#1006F从现阶段来看，\n'
		'终究也只是猜测而已。{wait}'
		'{page}'
		'#14200669V#1003F但是，一个个点联结成了线，\n'
		'线又渐渐交织成了完整的面……{wait}'
		'{page}'
		'#14200670V#1002F你们应该也有这种感觉吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200671V#12P#0006F嗯……{wait}'
		'{page}'
		'#14200672V#0008F不过，说实话，如此严重的状况，\n'
		'或许不是我们支援课可以独自解决的。{wait}'
		'{page}'
		'#14200673V#0001F特别是关系到那种药品的事件，\n'
		'我想，恐怕有必要\n'
		'与一课联系吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200674V#5P#1004F嗯，关于这点，\n'
		'现在时机正好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200675V#12P#0005F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('CAM_OFFSET', (63000, 1100, 4600), 2000),
	Insn('CAM_ROTATE', 60, 17, 0, 2000),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('FORK', 10, 1, [
		Insn('0x95', Char(254), (62000, 0, 3400), 2000, 0),
	]),
	Insn('FORK', 10, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('CHAR_WATCH', Char(10), Char(257), 500),
	Insn('0x6F', b'A'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14200676V#12P#1110F啊，你们在这里啊～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(10), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(10), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(10), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(10), 500),
	]),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200677V#0005F#5P琪雅，怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200678V#5P#0100F肚子饿了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14200679V#12P#1103F不是～是有客人来啦。{wait}'
		'{page}'
		'#14200680V#1105F是个表情好严肃的\n'
		'叔叔哦～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200681V#0001F#5P表情严肃的叔叔……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_UNSET', Char(22), 128),
	Insn('CHAR_FLAG2_UNSET', Char(22), 32768),
	Insn('SLEEP', 150),
	Insn('SOUND_PLAY', 44906, 216, 255, 100),
	Insn('TEXT_TALK2', Char(22), Translate('男人的声音'), Text(
		'#2P#8A──打扰了。{wait}'
	)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_POS', Char(22), (59000, 30, 3400), 90),
	Insn('FORK_LOOP', 10, 2, [
		Insn('CHAR_WATCH', Char(254), Char(22), 500),
	]),
	Insn('FORK', 22, 1, [
		Insn('0x95', Char(254), (61800, 0, 3400), 2000, 0),
	]),
	Insn('FORK', 22, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 10, 1, [
		Insn('0x96', Char(254), (63700, 0, 3400), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(22), 1),
	Insn('CHAR_WATCH', Char(22), Char(9), 500),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200683V#0011F#5P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200684V#5P#0105F达德利搜查官……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200685V#1002F#5P#N哦，你来得好迟啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (64000, 1100, 8600), 2000),
	Insn('CAM_ROTATE', 50, 17, 0, 2000),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(22), 500),
	]),
	Insn('FORK_LOOP', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(22), 500),
	]),
	Insn('FORK_LOOP', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(22), 500),
	]),
	Insn('FORK_LOOP', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(22), 500),
	]),
	Insn('FORK', 22, 1, [
		Insn('0x95', Char(254), (62800, 0, 7200), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 259, 1, [
		Insn('0x98', Char(254), (1000, 0, 0), 1000, 0),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 260, 1, [
		Insn('0x98', Char(254), (1000, 0, 0), 1000, 0),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 257, 1, [
		Insn('0x98', Char(254), (1000, 0, 0), 1000, 0),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 258, 1, [
		Insn('0x98', Char(254), (1000, 0, 0), 1000, 0),
	]),
	Insn('FORK_AWAIT', Char(22), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('FORK_QUIT', Char(258), 2),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('FORK_QUIT', Char(10), 2),
	Insn('0x6F', b'A'),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(1), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('TEXT_MESSAGE', Char(22), Text(
		'#14200686V……很抱歉，\n'
		'调查会议拖了很久。{wait}'
		'{page}'
		'#14200687V关于那件事情……\n'
		'我们就别浪费时间，\n'
		'立刻进入正题如何？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(1), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 0))),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200688V#5P#1003F哦，可以啊。{wait}'
		'{page}'
		'#14200689V#1002F如果你不介意他们也一起听的话。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(22), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200690V#12P#0601F赛尔盖长官！\n'
		'请不要再开玩笑了！{wait}'
		'{page}'
		'#14200691V这可不是能说给这些\n'
		'菜鸟们听的事啊──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200692V#5P#1004F可是，在这次事件中，\n'
		'他们收集到的情报\n'
		'一定能派得上用场。{wait}'
		'{page}'
		'#14200693V#1000F如果让他们同席旁听，我们的进展也许会快得多哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200694V#12P#0605F您说什么……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(22), Char(257), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200695V#6P#0601F不过话说回来，对『黑月』的\n'
		'询问工作也是由你们完成的呢。{wait}'
		'{page}'
		'#14200696V#0608F既然如此，那就……\n'
		'……不、不行，但是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(22), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(22)),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200697V#11P#0006F那个，课长……{wait}'
		'{page}'
		'#14200698V#0000F如果不太方便的话，\n'
		'我们还是先回避一下吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200699V#5P#1003F不，没那个必要。{wait}'
		'{page}'
		'#14200700V#1002F这个男人身为一课的精英，\n'
		'可不是浪得虚名的。{wait}'
		'{page}'
		'#14200701V在这种情况下，需要做出何种判断，\n'
		'相信他一定能够考虑清楚。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200702V#6P#0603F唔……我明白了。{wait}'
		'{page}'
		'#14200703V#0601F──听好，你们几个。\n'
		'接下来的谈话内容\n'
		'可是警察局内部的机密事项……{wait}'
		'{page}'
		'#14200704V#0607F绝对不允许透露给任何人，\n'
		'记住了吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200705V#11P#0005F明、明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14200706V#1110F什么什么，机密的话～？{wait}'
		'{page}'
		'#14200707V#1109F琪雅也要听～！{wait}'
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
	Insn('EMOTE', Char(9), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(22), 0, 2000, (16, 19, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(10), 500),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(10), 500),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(10), 500),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(10), 500),
	]),
	Insn('FORK', 22, 2, [
		Insn('CHAR_WATCH', Char(254), Char(10), 500),
	]),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200708V#5P#0012F那、那个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200709V#5P#0102F我准备了美味的点心哦，\n'
		'琪雅还是先去和赛特一起吃吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 23500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 3000),
	Insn('BGM_WAIT'),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('CAM_OFFSET', (63880, 1100, 8580), 0),
	Insn('CAM_ROTATE', 50, 17, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 22500, 0),
	Insn('CHAR_SET_POS', Char(22), (65300, 0, 6900), 270),
	Insn('CHAR_SET_POS', Char(257), (62700, 0, 6300), 90),
	Insn('CHAR_SET_POS', Char(258), (62700, 0, 7500), 90),
	Insn('CHAR_SET_POS', Char(259), (61400, 0, 6500), 90),
	Insn('CHAR_SET_POS', Char(260), (61400, 0, 7700), 90),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#14200710V#0013F给搜查一课施加压力……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('BGM_PLAY', b'o\x00\x00'),
	Insn('CAM_DISTANCE', 23000, 2000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200711V#0603F#11P不，倒也并没有\n'
		'那么露骨……{wait}'
		'{page}'
		'#14200712V#0601F之前上级也曾下达过指示，\n'
		'要我们对『黑月』的受袭事件展开调查，\n'
		'并倾尽全力处理黑手党之间的斗争事件。{wait}'
		'{page}'
		'#14200713V#0606F……但在不久之前开始调查的\n'
		'神秘药物事件，却被强行中断了。{wait}'
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
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200714V#6P#0011F什么……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200715V#6P#0205F一课那边也在对\n'
		'药物事件进行调查……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200716V#0603F#11P哼，早在几天之前就已经开始了。{wait}'
		'{page}'
		'#14200717V#0600F就我来说，你们会知道这件事\n'
		'才比较令人吃惊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200718V#5P#1001F不过，一课那边是怎么\n'
		'掌握到关于药物的消息的？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200719V#0603F……自然是经由从以前开始\n'
		'就和我们有所联系的『情报商』。{wait}'
		'{page}'
		'#14200720V#0600F其情报源非常值得信赖，\n'
		'所以我们经常由此来收集信息……{wait}'
		'{page}'
		'#14200721V不过，这次我们所得到的，\n'
		'都是些类似都市传说一类的传闻而已。{wait}'
		'{page}'
		'#14200722V#0606F像是『可以实现愿望的药』，\n'
		'『可以带来幸福的蓝色药物』之类的……{wait}'
		'{page}'
		'#14200723V因为感觉事有蹊跷，所以我们正在\n'
		'着手整理与此类传闻有关的市民名单，\n'
		'但就在调查的途中……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200724V#0605F#11P怎、怎么回事……你们几个的表情\n'
		'就好像是在说『果然如此』一样。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200725V#5P#1003F哼……\n'
		'不出所料啊。{wait}'
		'{page}'
		'#14200726V#1000F罗伊德，把那个给他看。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200727V#6P#0003F……是。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200728V#0605F#11P？？？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(22), 0),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xe8\x03\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200729V#6P#0001F这个──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('SLEEP', 300),
	Insn('SOUND_PLAY', 1558, 0, 255, 100),
	Insn('0x82', 100, 0, 3000, 200),
	Insn('TEXT_MESSAGE', Char(22), Text(
		'#14200730V#0607F#4S什么……！{wait}'
		'{page}'
		'#14200731V这、这难道就是……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#14200732V#0006F……这是我们今天通过\n'
		'某个管道而得到的证物。{wait}'
		'{page}'
		'#14200733V#0001F以严格保护提供者的名誉为条件，\n'
		'暂时将其保管在我们这里……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (62700, 0, 6300), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('CHAR_ROTATE', Char(257), 90, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('SLEEP', 300),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}将至今为止的事情经过向达德利做了说明。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('EMOTE', Char(22), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(22)),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200734V#0608F#11P哼……\n'
		'果然是真实存在的吗……{wait}'
		'{page}'
		'#14200735V#0610F而且很有可能是\n'
		'鲁巴彻的人所流出的……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200736V#5P#1003F命令你们停止对这种药物\n'
		'进行调查的指示……{wait}'
		'{page}'
		'#14200737V#1000F具体是从哪里传达下来的，\n'
		'对此你有什么头绪吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200738V#0606F……总之是高层的某个人吧。{wait}'
		'{page}'
		'#14200739V#0608F连一课的课长都无法接受，\n'
		'但也只能无奈地将指示下达给我们。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200740V#5P#1006F哼，真是最糟糕的情况啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200741V#6P#0105F请、请等一下。{wait}'
		'{page}'
		'#14200742V#0110F难道说，警察局的领导层竟然向\n'
		'黑手党妥协，接受了他们的请求……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(9), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(22), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(9)),
	Insn('EMOTE_STOP', Char(22)),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200743V#6P#0006F怎、怎么会……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200744V#6P#0301F喂喂，不是开玩笑吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200745V#6P#0206F……情况确实是再糟糕不过了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200746V#5P#1003F──达德利。{wait}'
		'{page}'
		'#14200747V#1000F你会来找我们商讨这种事，\n'
		'肯定是因为你已经对上层产生怀疑了吧。{wait}'
		'{page}'
		'#14200748V那么，你有什么打算吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200749V#0608F…………………………………{wait}'
		'{page}'
		'#14200750V#0606F……老实说，关于药物的调查工作，\n'
		'我们这边已经无法再继续展开了。{wait}'
		'{page}'
		'#14200751V如果硬来，上层也许就会\n'
		'直截了当地加以干涉了。{wait}'
		'{page}'
		'#14200752V#0610F可是，身为警察组织的一员，\n'
		'如果就此罢手的话，也未免太过无能了……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200753V#6P#0005F达德利搜查官……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200754V#5P#1002F那么，关于药物方面的\n'
		'调查工作，也只能交给我们负责啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(9), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200755V#5P#1000F──罗伊德、艾莉，\n'
		'还有兰迪和缇欧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(9), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(9), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(9), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(9), 500),
	]),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200756V#5P#1003F接下来，特务支援课将以非正式的\n'
		'形式，与搜查一课进入合作阶段。{wait}'
		'{page}'
		'#14200757V#1001F你们就代替无法采取行动的一课，\n'
		'继续对药物进行调查吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200758V#12P#0001F是……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200759V#12P#0101F明白了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200760V#5P#1003F嗯，作为回报……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(9), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200761V#5P#1002F一课手中的那些与黑手党有关的情报，\n'
		'要无限制地提供给我们。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(22), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(22), 0, 2000, (40, 43, 100, 3)),
	Insn('CHAR_WATCH', Char(22), Char(9), 500),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200762V#0605F赛、赛尔盖长官！？{wait}'
		'{page}'
		'#14200763V再怎么说，那些极其机密的情报\n'
		'也不能毫无限制地随意……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200764V#5P#1002F我们是无所谓哦。{wait}'
		'{page}'
		'#14200765V反正你们那边现在已经无计可施了，\n'
		'不答应的话，我们随意行动就是了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200766V#0601F唔……{wait}'
		'{page}'
		'#14200767V#0606F……明白了，\n'
		'我接受这个条件。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200768V#5P#1002F呵呵，那就这么决定啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200769V#6P#0309F哎呀～真没想到我们竟然能\n'
		'替代那个一课来展开行动啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200770V#6P#0204F真是有种莫名的\n'
		'优越感呀。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(22), 270, 500),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200771V#0610F#11P……………………（瞪眼）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200772V#6P#0305F噢噢，好可怕……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200773V#6P#0206F……女神救命女神救命。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200774V#0603F#11P哼，算了，没办法。{wait}'
		'{page}'
		'#14200775V#0601F在这种情况下，也只能同意\n'
		'由你们来负责药物的调查工作了……{wait}'
		'{page}'
		'#14200776V不过，关于今后的调查方针，你们有什么想法吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200777V#6P#0003F是啊……{wait}'
		'{page}'
		'#14200778V#0001F──不管怎么说，\n'
		'药品的实物就在我们手里。{wait}'
		'{page}'
		'#14200779V无论如何，也有必要\n'
		'查清楚其成分吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200780V#0600F#11P嗯……\n'
		'可是，你们要怎么查呢？{wait}'
		'{page}'
		'#14200781V从现有情报来推测，\n'
		'不难发现这是全新种类的药物。{wait}'
		'{page}'
		'#14200782V总部的鉴定部门恐怕没有能力查明其成分，\n'
		'而且这么做也很容易被上层发觉。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200783V#6P#0008F原来如此……{wait}'
		'{page}'
		'#14200784V#0000F……这样的话，我们也许\n'
		'应该去拜托医科大学那边的人吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('CHAR_WATCH', Char(258), Char(257), 500),
			Insn('TEXT_TALK', Char(258), Text(
				'#14200785V#5P#0100F原来如此……\n'
				'是要请那位医生帮忙吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('CHAR_WATCH', Char(259), Char(257), 500),
			Insn('TEXT_TALK', Char(259), Text(
				'#14200786V#6P#0202F……原来如此，\n'
				'要请那位医生帮忙吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('CHAR_WATCH', Char(260), Char(257), 500),
			Insn('TEXT_TALK', Char(260), Text(
				'#14200787V#3P#0300F原来如此啊……\n'
				'要找那位医生帮忙吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200788V#0605F#11P医科大学……\n'
		'是圣乌尔斯拉医科大学吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200789V#6P#0004F嗯，我们认识那里的一位专门\n'
		'研究药物学的医生。{wait}'
		'{page}'
		'#14200790V#0000F听说他的专业能力相当优秀，\n'
		'如果拜托他来检查药物成分的话，\n'
		'查明的可能性应该很高吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200791V#0600F#11P哼，原来如此啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200792V#5P#1003F看样子，调查药物成分的工作\n'
		'也只能这么办了。{wait}'
		'{page}'
		'#14200793V#1000F达德利，今日之内，\n'
		'把在一课整理好的调查\n'
		'报告书拿给我们。{wait}'
		'{page}'
		'#14200794V我让他们以此为基础，\n'
		'决定今后的调查方针。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(22), Char(9), 500),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200795V#0600F明白了，\n'
		'马上就会送到。{wait}'
		'{page}'
		'#14200796V#0604F──那么，我就先行告辞了，\n'
		'今后也请多多指教。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200797V#5P#1004F嗯，彼此彼此啊。{wait}'
		'{page}'
		'#14200798V#1002F而且，你这句话应该\n'
		'也对他们说一说。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200799V#0610F唔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(22), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(22)),
	Insn('CHAR_ROTATE', Char(22), 270, 500),
	Insn('TEXT_TALK', Char(22), Text(
		'#14200800V#0603F──听好，你们几个。{wait}'
		'{page}'
		'#14200801V#0601F一定要谨慎仔细，不要干出\n'
		'一些蠢事，让事态进一步恶化啊。{wait}'
		'{page}'
		'#14200802V#0607F另外，药物的调查也就算了，\n'
		'黑手党斗争那方面的处理工作就\n'
		'由我们一课来负责！{wait}'
		'{page}'
		'#14200803V你们最好不要胡乱插手，\n'
		'一切都交给我们来办就行了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200804V#6P#0005F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(22), 500),
	]),
	Insn('FORK_LOOP', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(22), 500),
	]),
	Insn('FORK_LOOP', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(22), 500),
	]),
	Insn('FORK_LOOP', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(22), 500),
	]),
	Insn('0x92', Char(22), 62000, 3400, 500),
	Insn('CAM_OFFSET', (62000, 1100, 5500), 2000),
	Insn('FORK', 22, 1, [
		Insn('0x95', Char(254), (62000, 0, 3400), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(22), 1),
	Insn('FORK', 22, 1, [
		Insn('0x95', Char(254), (59000, 0, 3400), 2500, 0),
	]),
	Insn('SLEEP', 500),
	Insn('CHAR_SET_FRAME', Char(9), 2),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('FORK', 22, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(22), 1),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('FORK_QUIT', Char(258), 2),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('CHAR_FLAG1_SET', Char(22), 128),
	Insn('CHAR_FLAG2_SET', Char(22), 32768),
	Insn('0x6F', b'\x01'),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (63500, 1100, 9000), 0),
	Insn('CAM_ROTATE', 50, 17, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 23000, 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200805V#5P#0302F哎呀呀，\n'
		'真是个不坦率的老兄。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200806V#5P#0204F……我想，那可能也是\n'
		'一种掩饰害羞的方式吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200807V#5P#0109F呵呵，或许吧。{wait}'
		'{page}'
		'#14200808V#0102F而且，他是个正派的人，\n'
		'正义感似乎比想像中的还要强呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200809V#11P#0002F是啊……\n'
		'给人一种值得信赖的感觉。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200810V#5P#1004F基本上说，一课的人大多都是\n'
		'这种性格认真，正义感又很强的家伙。{wait}'
		'{page}'
		'#14200811V不过，他们大多也都\n'
		'墨守成规，不懂通融就是了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(9), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200812V#5P#1005F──那么，你们几个，\n'
		'打算立刻出发去医院吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(9), 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(9), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(9), 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_WATCH', Char(260), Char(9), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200813V#12P#0000F嗯，正有此意。{wait}'
		'{page}'
		'#14200814V如果时间充裕，也可以先把\n'
		'其它支援请求都解决，然后再去医院。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200815V#0106F#6P也对哦……\n'
		'上午也没有时间到市外去。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200816V#6P#0300F哈，似乎会很忙啊，\n'
		'还是先把事情都逐一解决之后再去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200817V#5P#1004F哼哼，你们有干劲就好。{wait}'
		'{page}'
		'#14200818V#1002F虽说是要和一课进行合作，\n'
		'但你们也没有必要因此而过于争强。{wait}'
		'{page}'
		'#14200819V就像平时一样，用你们自己的方法\n'
		'来解开药物之谜吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200820V#12P#0000F是！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 22500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'g\x00\x00'),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('CAM_OFFSET', (64000, 1330, 5500), 0),
	Insn('CAM_ROTATE', 45, 26, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(0), (64000, 30, 5500), 180),
	Insn('CHAR_SET_POS', Char(1), (64000, 30, 5500), 180),
	Insn('CHAR_SET_POS', Char(2), (64000, 30, 5500), 180),
	Insn('CHAR_SET_POS', Char(3), (64000, 30, 5500), 180),
	Insn('CHAR_SET_FRAME', Char(9), 0),
	Insn('0x4C', Char(10), -1),
	Insn('FLAG_SET', Flag(1560)),
	Insn('QUEST', 74, Insn('FLAG_UNSET', 16)),
	Insn('QUEST', 75, Insn('FLAG_UNSET', 16)),
	Insn('QUEST', 76, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 76, Insn('TASK_SET', 0)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][48] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (64000, 1100, 8600), 0),
	Insn('CAM_ROTATE', 50, 17, 0, 0),
	Insn('0x6E', 380, 0),
	Insn('CAM_DISTANCE', 24000, 0),
	Insn('CHAR_SET_POS', Char(257), (63000, 0, 6700), 0),
	Insn('CHAR_SET_POS', Char(258), (64300, 0, 6700), 0),
	Insn('CHAR_SET_POS', Char(259), (63200, 0, 5400), 0),
	Insn('CHAR_SET_POS', Char(260), (64500, 0, 5400), 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200821V#5P#1000F乌尔斯拉医院吗……{wait}'
		'{page}'
		'#14200822V你们要找的那位医生，\n'
		'就是之前给琪雅检查\n'
		'记忆丧失症状的那个人吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200823V#12P#0000F嗯，就是那位名叫约亚西姆的医生，\n'
		'他是药物学和神经科的副教授。{wait}'
		'{page}'
		'#14200824V印象中，以前和他谈话时，\n'
		'他对药物学好像有相当详尽的了解呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200825V#5P#1003F嗯，那位医生要是\n'
		'能帮得上忙就最好不过了。可是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(9), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(9)),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200826V#12P#0005F课长……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200827V#0101F那个，您有什么在意的事吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200828V#5P#1006F……算是吧。{wait}'
		'{page}'
		'#14200829V#1003F力量、速度、集中力、直觉。{wait}'
		'{page}'
		'#14200830V这些东西，或许都可以通过药物\n'
		'从生理方面来进行提高。{wait}'
		'{page}'
		'#14200831V#1001F可是……\n'
		'『运气』这种东西，能够提高吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200832V#12P#0011F这、这个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200833V#0106F按照一般的想法，\n'
		'自然是不可能的……{wait}'
		'{page}'
		'#14200834V#0101F可是，那个冈兹先生的运气\n'
		'却惊人地强，您是想说这个吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200835V#0303F嗯，无论是哪种赌局，\n'
		'光靠直觉和策略，恐怕也不可能\n'
		'一直常胜不败。{wait}'
		'{page}'
		'#14200836V#0308F难道是女神站在了他这边？\n'
		'还是说他求助于恶魔了呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200837V#12P#0208F……………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#14200838V#5P#1003F嗯，目前好像还是留有不少谜团。{wait}'
		'{page}'
		'#14200839V#1000F──缇欧。\n'
		'如果可以的话，关于这方面的事情，\n'
		'你就好好确认一下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200840V#12P#0203F是……我正有此意。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 400),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 400),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 400),
	]),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200841V#5P#0005F（为什么是缇欧……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200842V#5P#0105F（有什么隐情吗……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (64000, 30, 5500), 180),
	Insn('FLAG_SET', Flag(1561)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][49] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50011', 30),
	Insn('SOUND_LOAD', 806),
	Insn('CAM_OFFSET', (800, 1700, 3400), 0),
	Insn('CAM_ROTATE', 55, 17, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 23220, 0),
	Insn('CHAR_SET_POS', Char(257), (800, 0, 2400), 0),
	Insn('CHAR_SET_POS', Char(258), (-500, 0, 1300), 0),
	Insn('CHAR_SET_POS', Char(259), (1000, 0, 4500), 180),
	Insn('CHAR_SET_POS', Char(260), (1400, 0, 1500), 0),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_SET_POS', Char(8), (3000, 0, 4700), 225),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_SET_POS', Char(10), (0, 0, 4600), 180),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('CHAR_SET_FRAME', Char(14), 0),
	Insn('CHAR_SET_POS', Char(14), (-320, 0, 5900), 168),
	Insn('CHAR_FLAG1_UNSET', Char(14), 128),
	Insn('CHAR_FLAG2_UNSET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('IMG_LOAD', ResId(0), 180, 0, b'\xb4\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis007.itp'),
	Insn('CAM_OFFSET', (800, 1300, 3400), 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14300001V#0006F#11P──缇欧，你真的没问题吗？{wait}'
		'{page}'
		'#14300002V#0001F如果身体还没恢复的话，你可以\n'
		'和课长、琪雅他们一起留在支援课……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14300003V#0204F#5P……不用担心。{wait}'
		'{page}'
		'#14300004V#0202F我早就已经充分休息过了，\n'
		'现在的状态比平时还要好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14300005V#0002F#11P是吗……\n'
		'嗯，脸色好像也不错。{wait}'
		'{page}'
		'#14300006V#0006F不过，琪雅突然说要\n'
		'和你一起睡的时候，我还真\n'
		'是吃了一惊呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14300007V#5P#1100F嗯～不知为什么，\n'
		'突然就那样想。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(10), Char(259), 500),
	Insn('TEXT_TALK', Char(10), Text(
		'#14300008V#6P#1101F那个那个，缇欧，\n'
		'你睡得好吗～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(259), Char(10), 500),
	Insn('TEXT_TALK', Char(259), Text(
		'#14300009V#11P#0202F嗯，那当然。{wait}'
		'{page}'
		'#14300010V#0204F之所以能有这么好的状态，\n'
		'最大的理由也许就是琪雅\n'
		'给我补充了源源不断的能量呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14300011V#6P#1109F嘿嘿嘿，太好啦～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14300012V#12P#0309F哈哈，原来如此啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14300013V#12P#0109F也许琪雅确实是\n'
		'最棒的特效药呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14300014V#0004F嗯……是啊。{wait}'
		'{page}'
		'#14300015V#0008F──我说，缇欧，\n'
		'答应我一件事吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 100),
	Insn('CHAR_ROTATE', Char(10), 180, 500),
	Insn('TEXT_TALK', Char(259), Text(
		'#14300016V#0205F#5P……什么………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14300017V#0006F#11P如果今后再次发生了像昨天那种事，\n'
		'一定要马上和我们说。{wait}'
		'{page}'
		'#14300018V绝对不要再勉强自己\n'
		'一个人来承受了。{wait}'
		'{page}'
		'#14300019V#0001F这么说也许有些过分……\n'
		'但你如果在战斗时突然倒下，\n'
		'有可能会成为我们的累赘。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14300020V#0204F#5P……是，我一定铭记在心。{wait}'
		'{page}'
		'#14300021V我也是支援课的一员……\n'
		'是大家的同伴。{wait}'
		'{page}'
		'#14300022V#0214F所以……\n'
		'我的痛苦、压力……\n'
		'就请大家来帮我分担吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14300023V#12P#0102F缇欧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14300024V#12P#0309F……哈哈。\n'
		'没问题，小事一桩。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14300025V#0002F#11P嗯……我们\n'
		'都很乐意替你分担哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14300026V#5P#1105F嘿……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14300027V#5P#1009F呵呵，这样的话，\n'
		'也就不需要我这大叔再说什么了。{wait}'
		'{page}'
		'#14300028V#1002F──你们要在今天上午\n'
		'去对那些有使用药物嫌疑的\n'
		'市民们进行询问吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#14300029V#6P#0003F嗯，我准备以一课的资料为参考，\n'
		'再次去确认一下。{wait}'
		'{page}'
		'#14300030V#0000F而且，一旦开始调查，大概就会非常忙了。\n'
		'所以打算趁现在先将\n'
		'其它的支援请求处理一下。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14300031V#6P#0203F是啊……\n'
		'如果错过这个时机，\n'
		'也就没有时间去市外了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14300032V#12P#0306F不过，住宅区的证券经理、\n'
		'剑蛇帮的小弟……{wait}'
		'{page}'
		'#14300033V#0301F还有彩虹剧团的\n'
		'新演员吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1640)), Insn('FLAG', Flag(1647)), Insn('BOOL_AND'), Insn('FLAG', Flag(1651)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST_BONUS_DP', 76, 2),
			Insn('TEXT_TALK', Char(258), Text(
				'#14300034V#0106F#6P全部都是在昨天就感觉\n'
				'样子有些奇怪的人呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1640)), Insn('NOT'), Insn('FLAG', Flag(1647)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1651)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#14300035V#0101F#6P真不愧是一课……\n'
				'全都查到了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('QUEST_BONUS_DP', 76, 1),
			Insn('TEXT_TALK', Char(258), Text(
				'#14300036V#0108F#6P确实，昨天就感觉有些人的样子\n'
				'比较奇怪了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(8), Text(
		'#14300037V#5P#1003F如果有时间的话，最好\n'
		'再去一趟伊安律师的事务所吧。{wait}'
		'{page}'
		'#14300038V#1001F在从伊安律师那里得知的两个人中，\n'
		'证券经理和一课资料中写到的那个好像是\n'
		'同一个人……{wait}'
		'{page}'
		'#14300039V至于贸易公司的那个经营者，\n'
		'资料中好像并没有记录呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14300040V#6P#0003F是啊……\n'
		'也去法律事务所看看吧。{wait}'
		'{page}'
		'#14300041V#0001F然后，等到下午，\n'
		'约亚西姆医生应该就会和我们联系，\n'
		'把药物成分的调查结果告诉我们了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 5000),
	Insn('SOUND_PLAY', 806, 0, 2, 100),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(8), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 300),
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
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14300042V#0001F您好，这里是特务支援课，\n'
		'我是罗伊德丄班宁斯。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('镇长的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14300043V……罗伊德？\n'
		'是我，玛因兹的比克森。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14300044V#0005F啊，镇长先生。{wait}'
		'{page}'
		'#14300045V#0000F──您联系得正是时候，\n'
		'冈兹先生的状态怎么样了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('镇长的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14300046V这、这个嘛……{wait}'
		'{page}'
		'#14300047V那个……冈兹那家伙\n'
		'又消失不见了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14300048V#0013F！？{wait}'
		'{page}'
		'#14300049V#0001F……能请您说得再\n'
		'详细一点吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('镇长的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14300050V在那之后，冈兹\n'
		'在半夜时清醒过来了……{wait}'
		'{page}'
		'#14300051V不过意识好像还很模糊，\n'
		'所以我就让他继续睡下去了。{wait}'
		'{page}'
		'#14300052V谨慎起见，我也留在了房间里。\n'
		'本来是打算第二天早上\n'
		'就和你们联系的……{wait}'
		'{page}'
		'#14300053V结果，等我早上醒来之后……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14300054V#0003F……原来如此。{wait}'
		'{page}'
		'#14300055V#0001F您问过饭店和赌场的工作人员吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('镇长的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14300056V全、全都去问过了，\n'
		'可是好像没人见到过他……{wait}'
		'{page}'
		'#14300057V罗伊德……\n'
		'你认为该怎么办好？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14300058V#0003F……镇长先生请暂时\n'
		'留在饭店吧。{wait}'
		'{page}'
		'#14300059V说不定冈兹先生\n'
		'还会回去的。{wait}'
		'{page}'
		'#14300060V#0000F我们正要出去进行案情询问，\n'
		'同时也会留意一下他的行踪。{wait}'
		'{page}'
		'#14300061V如果有什么新情况，\n'
		'就请再次和我联系吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('镇长的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14300062V明、明白了……那就拜托你了！{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('BGM_PLAY', b'g\x00\x00'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#14300063V#12P#0101F……冈兹先生\n'
		'不见了吗？{wait}'
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
	Insn('TEXT_TALK', Char(257), Text(
		'#14300064V#0006F#5P嗯……好像是\n'
		'今天早上离开饭店的。{wait}'
		'{page}'
		'#14300065V#0008F是自己离开的吗，\n'
		'还是说……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14300066V#0201F#5P……看来，果然有必要\n'
		'去确认一下其他人的状态啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14300067V#12P#0301F是啊……\n'
		'我有种莫名的不祥预感呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14300068V#5P#1003F……看起来，事态的进展速度\n'
		'似乎比我们预想中的还要快呢。{wait}'
		'{page}'
		'#14300069V#1000F不用担心这边，\n'
		'你们快去进行确认吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#14300070V#6P#0000F是！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14300071V#5P#1109F慢走哦～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#14300072V#1200F#5P呜～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 23720, 2000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('CAM_OFFSET', (800, 1000, 2000), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 340, 0),
	Insn('CAM_DISTANCE', 27500, 0),
	Insn('CHAR_SET_POS', Char(0), (750, 0, 3410), 180),
	Insn('CHAR_SET_POS', Char(1), (750, 0, 3410), 180),
	Insn('CHAR_SET_POS', Char(2), (750, 0, 3410), 180),
	Insn('CHAR_SET_POS', Char(3), (750, 0, 3410), 180),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG2_UNSET', Char(11), 32768),
	Insn('CHAR_SET_POS', Char(11), (257620, 350, 68650), 270),
	Insn('CHAR_FLAG1_UNSET', Char(14), 128),
	Insn('CHAR_FLAG2_UNSET', Char(14), 32768),
	Insn('CHAR_SET_POS', Char(14), (256820, 30, 69850), 180),
	Insn('FLAG_SET', Flag(1566)),
	Insn('QUEST', 76, Insn('TASK_SET', 5)),
	Insn('QUEST', 76, Insn('TASK_SET', 6)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 45, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 45, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 45, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 45, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 45, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 48, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 48, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 48, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 48, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 48, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('SOUND_STOP', 806),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][50] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('LOAD_CHCP', 'chr/ch08702', 32),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_SET_CHCP', Char(259), 11),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_SET_CHCP', Char(260), 12),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_POS', Char(257), (13900, 900, 6650), 270),
	Insn('CHAR_SET_POS', Char(258), (13900, 900, 4600), 270),
	Insn('CHAR_SET_POS', Char(259), (11300, 900, 6650), 90),
	Insn('CHAR_SET_POS', Char(260), (11300, 900, 4600), 90),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_SET_POS', Char(10), (256000, 0, 68700), 90),
	Insn('EXPR_CHAR_ATTR', Char(10), 40, Expr([Insn('CONST', 13), Insn('SET'), Insn('END')])),
	Insn('CHAR_SET_CHCP', Char(15), 32),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('CHAR_FLAG1_UNSET', Char(15), 128),
	Insn('CHAR_FLAG2_UNSET', Char(15), 32768),
	Insn('0x4B', Char(15), -1),
	Insn('CHAR_FLAG1_UNSET', Char(15), 1),
	Insn('CHAR_SET_POS', Char(15), (257550, 400, 68700), 270),
	Insn('CHAR_SET_CHCP', Char(12), 6),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG2_UNSET', Char(12), 32768),
	Insn('CHAR_SET_POS', Char(12), (256000, 0, 67200), 45),
	Insn('FORK_FUNC', Char(12), 3, Function((0, 0))),
	Insn('0x7D', b'\xff\xd2\xc8\x00\x00\x00\x00\x00'),
	Insn('CAM_OFFSET', (258000, 1000, 68700), 0),
	Insn('CAM_ROTATE', 40, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CAM_OFFSET', (257000, 1000, 68700), 2000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(10), 0, 1700, (8, 9, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('0x9C', Char(10), b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x01\x00\x00\xb8\x0b\x00\x00'),
	Insn('SLEEP', 100),
	Insn('0x9C', Char(10), b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x01\x00\x00\xb8\x0b\x00\x00'),
	Insn('SLEEP', 300),
	Insn('EMOTE', Char(10), 0, 1700, (8, 9, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(15), 0, 1700, (38, 39, 250, 2)),
	Insn('SLEEP', 1000),
	Insn('FORK', 10, 2, [
		Insn('CHAR_ROTATE', Char(10), 270, 800),
	]),
	Insn('FORK_AWAIT', Char(10), 2),
	Insn('FORK', 10, 2, [
		Insn('CHAR_ROTATE', Char(10), 89, 800),
	]),
	Insn('FORK_AWAIT', Char(10), 2),
	Insn('EMOTE', Char(10), 0, 1700, (38, 39, 250, 2)),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(15), 0, 1700, (8, 9, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('CAM_OFFSET', (256000, 1000, 68700), 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('EXPR_CHAR_ATTR', Char(10), 40, Expr([Insn('CONST', 9), Insn('SET'), Insn('END')])),
	Insn('CAM_OFFSET', (12600, 2350, 5600), 0),
	Insn('CAM_ROTATE', 40, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CAM_OFFSET', (12600, 1850, 5600), 1500),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#15100213V#11P#0003F………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#15100214V#0103F#11P………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#15100215V#6P#0206F………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#15100216V#6P#0306F………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(258), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('SLEEP', 500),
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#15100217V#6P#0307F哇啊啊！\n'
		'好慢，这也太慢了吧！？{wait}'
		'{page}'
		'#15100218V#0301F那个医生不是说好\n'
		'要在下午联系我们的吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#15100219V#0108F#11P和医院的接待员也联系过了，\n'
		'据说他把自己关在研究室里，\n'
		'正在专心地进行成分检验呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#15100220V#6P#0203F检验那种药物成分的工作\n'
		'也许相当棘手吧。{wait}'
		'{page}'
		'#15100221V#0211F……但说不定他也只是在偷懒，\n'
		'其实溜出去钓鱼了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#15100222V#11P#0012F我、我想应该\n'
		'不至于吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_POS', Char(8), (19000, 850, 3500), 270),
	Insn('CHAR_SET_COLOR', Char(8), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('0x4B', Char(8), -1),
	Insn('CAM_OFFSET', (14200, 1850, 5000), 2500),
	Insn('OBJ_FLAG_UNSET', Object(0), 16),
	Insn('0x71', Object(0), b'\x00\x00', 5, 0),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('0x79', b'\x00\x00'),
	Insn('SLEEP', 300),
	Insn('FORK', 8, 1, [
		Insn('0x96', Char(254), (14900, 850, 3500), 2000, 0),
	]),
	Insn('FORK', 8, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(8), 2),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(259), 2),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(258), 1),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(260), 2),
	Insn('SLEEP', 300),
	Insn('0x71', Object(0), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('0x79', b'\x00\x00'),
	Insn('OBJ_FLAG_SET', Object(0), 16),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('CHAR_ROTATE', Char(8), 315, 500),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(8), Text(
		'#15100223V#12P#1005F怎么回事，那个医生\n'
		'还没有联系你们吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#15100224V#5P#0006F嗯，他好像正在专心进行成分检验，\n'
		'把自己关在研究室里，不出一步呢。{wait}'
		'{page}'
		'#15100225V#0000F这样的话，我们也许\n'
		'还是应该直接过去找他吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#15100226V#12P#1003F嗯，或许正该如此。{wait}'
		'{page}'
		'#15100227V#1000F既然已经出现了受害者，\n'
		'最好尽早检验出药物的成分。{wait}'
		'{page}'
		'#15100228V游击士协会那边的联系就交给我，\n'
		'你们赶快去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#15100229V#0100F#5P不好意思，\n'
		'那就拜托您了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#15100230V#6P#0300F那么，我们就赶快搭乘巴士\n'
		'去乌尔斯拉医院吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('0x4C', Char(10), -1),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_SET_POS', Char(10), (256490, 30, 69370), 180),
	Insn('CHAR_SET_CHCP', Char(15), 3),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('0x4C', Char(15), -1),
	Insn('CHAR_FLAG1_UNSET', Char(15), 128),
	Insn('CHAR_FLAG1_SET', Char(15), 1),
	Insn('CHAR_SET_POS', Char(15), (257350, 0, 68870), 225),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 128),
	Insn('CHAR_FLAG2_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(13), 128),
	Insn('CHAR_SET_POS', Char(13), (255850, 0, 67920), 225),
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
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('CAM_OFFSET', (12000, 1850, 8700), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 340, 0),
	Insn('CAM_DISTANCE', 27500, 0),
	Insn('CHAR_SET_POS', Char(0), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(1), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(2), (12000, 850, 8700), 270),
	Insn('CHAR_SET_POS', Char(3), (12000, 850, 8700), 270),
	Insn('FLAG_SET', Flag(1792)),
	Insn('0xC7', b'\x01\x00\x10\x00\x00'),
	Insn('QUEST', 76, Insn('TASK_SET', 27)),
	Insn('QUEST', 77, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 77, Insn('TASK_SET', 0)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 43, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 43, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 47, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 47, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 51, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 51, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 40, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 40, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 40, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 46, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 46, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 46, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 46, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 46, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('SLEEP', 1000),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][51] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1024)), Insn('FLAG', Flag(1025)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 13, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F在出门之前，\n'
				'还是先确认一下\n'
				'支援请求吧……{wait}'
				'{page}'
				'说不定会有什么\n'
				'紧急的案件发来呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (9350, 850, 10320), 89),
			Insn('EVENT_END', 4),
		]),
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(526)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('0x4B', Char(8), -1),
			Insn('CHAR_WATCH', Char(8), Char(257), 500),
			Insn('SLEEP', 100),
			Insn('TEXT_TALK', Char(8), Text(
				'#1000F啊，你们要去哪里啊？{wait}'
				'{page}'
				'快去确认支援请求啊。\n'
				'只要调查这个终端，\n'
				'就可以把情报给调出来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (9350, 850, 10320), 89),
			Insn('CHAR_ROTATE', Char(8), 180, 0),
			Insn('0x4C', Char(8), -1),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][52] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(526)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('0x4B', Char(8), -1),
			Insn('CHAR_WATCH', Char(8), Char(257), 500),
			Insn('SLEEP', 100),
			Insn('TEXT_TALK', Char(8), Text(
				'#1000F啊，你们要去哪里啊？{wait}'
				'{page}'
				'快去确认支援请求啊。\n'
				'只要调查这个终端，\n'
				'就可以把情报给调出来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (11000, 850, 11350), 180),
			Insn('CHAR_ROTATE', Char(8), 180, 0),
			Insn('0x4C', Char(8), -1),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][53] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(526)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('0x4B', Char(8), -1),
			Insn('CHAR_WATCH', Char(8), Char(257), 500),
			Insn('SLEEP', 100),
			Insn('TEXT_TALK', Char(8), Text(
				'#1000F啊，你们要去哪里啊？{wait}'
				'{page}'
				'快去确认支援请求啊。\n'
				'只要调查这个终端，\n'
				'就可以把情报给调出来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (17000, 850, 4000), 270),
			Insn('CHAR_ROTATE', Char(8), 180, 0),
			Insn('0x4C', Char(8), -1),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][54] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 8, Insn('TASK_GET', 1))), Insn('EXEC', Insn('QUEST_GET', 8, Insn('TASK_GET', 2))), Insn('OR'), Insn('EXEC', Insn('QUEST_GET', 8, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 8, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('SOUND_PLAY', 823, 0, 0, 100),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F噢……{wait}'
				'{page}'
				'我们还带着小猫呢。\n'
				'还是不要走太远了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (800, 0, 1890), 0),
			Insn('EVENT_END', 4),
			Insn('RETURN'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][55] = [
	Insn('EVENT_BEGIN', 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1343)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F……这里是后门啊。{wait}'
				'{page}'
				'现在要带琪雅去游击士协会，\n'
				'还是从一楼的正门出去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(548)), Insn('FLAG', Flag(609)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F啊……还是先去\n'
				'导力商店看看吧。{wait}'
				'{page}'
				'#0000F应该就是位于中央广场一角的那个建筑物。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('ATTR', 10), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F了解，那么就去看看吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('ATTR', 10), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#0300F了解，去看看吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('ATTR', 10), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F嗯，这就去看看吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('FLAG', Flag(548)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(11)), Insn('NOT'), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('ATTR', 10), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F啊……这里好像\n'
								'是后门啊。{wait}'
								'{page}'
								'要带大家去街上熟悉环境，\n'
								'还是从一楼的正门出去吧。\n'
								'出去之后应该就是中央广场了。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('ATTR', 10), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
							Insn('TEXT_TALK', Char(258), Text(
								'#0100F啊呀……这里好像是后门呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F不好意思，还是从一楼的正门出去吧。\n'
								'从那边出去，更方便为你们做向导。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(258), Text(
								'#0100F了解，是一楼的正门对吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('ATTR', 10), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
							Insn('TEXT_TALK', Char(259), Text(
								'#0200F啊……这里似乎是后门哦。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F不好意思，还是从一楼的正门出去吧。\n'
								'从那边出去，更方便为你们做向导。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(259), Text(
								'#0200F知道了。\n'
								'是一楼的正门吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('ATTR', 10), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
							Insn('TEXT_TALK', Char(260), Text(
								'#0300F噢，这里看起来是后门。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F不好意思，还是从一楼的正门出去吧。\n'
								'从那边出去，更方便为你们做向导。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(260), Text(
								'#0300FＯＫ，队长。\n'
								'是一楼的正门哦。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, []),
					]),
					Insn('FLAG_SET', Flag(11)),
				]),
				(Expr([Insn('ATTR', 10), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F从一楼的正门出门之后，\n'
						'正面应该就是中央广场了。{wait}'
						'{page}'
						'还要带大家熟悉一下市内哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F从一楼的正门出门之后，\n'
						'正面应该就是中央广场了。{wait}'
						'{page}'
						'想带大家熟悉市内的话，\n'
						'还是从那边出门吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (-2190, 0, 68010), 90),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][56] = [
	Insn('TEXT_START', Char(255)),
	Insn('SOUND_PLAY', 810, 0, 0, 100),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}这里是空房间。\n'
				'平时都上着锁。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(597)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}门上了锁。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这里应该是空房间吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F这栋大楼虽然很旧，\n'
				'但房间倒是有很多呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F一直到前几年，\n'
				'克洛斯贝尔时报周刊都\n'
				'一直在这栋楼里呢。{wait}'
				'{page}'
				'#0003F虽然平时都上着锁……\n'
				'但放假时还是要打扫一下的啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(597)),
		]),
		(None, [
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}这里是空房间。\n'
				'平时都上着锁。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][57] = [
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

data['code'][58] = [
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

data['code'][59] = [
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

data['code'][60] = [
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
