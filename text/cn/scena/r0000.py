# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'r0000',
	'name2': 'r0000',
	'location': 94,
	'bgm': 204,
	'flags': 0,
	'includes': [
		'r0000',
		'r0000_1',
		None,
		None,
		None,
		None,
	],
	'name3': 'r0000',
	'labels': [
		{
			'pos': (-17.0, 0.0, -7.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('克洛斯贝尔市方向'),
		},
		{
			'pos': (203.0, 0.0, 27.5),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('阿尔摩利卡村丄唐古拉姆门方向'),
		},
		{
			'pos': (0.5899999737739563, 0.0, 4.840000152587891),
			'unk': b'\x00\x00U\x00',
			'name': Translate(''),
		},
		{
			'pos': (14.899999618530273, 0.0, 6.0),
			'unk': b'\x00\x00V\x00',
			'name': Translate(''),
		},
	],
	'chcp': [
		'chr/ch24200',
		'chr/ch30000',
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
		'monster/ch66550',
		'monster/ch66551',
		'monster/ch69950',
		'monster/ch69950',
	],
	'npcs': [
		{
			'name': Translate('男性'),
			'pos': (26100, 0, -3000),
			'angle': 270,
			'_1': b'\x95\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((0, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('警官'),
			'pos': (24799, 0, -3000),
			'angle': 90,
			'_1': b'\x95\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 12)),
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
			'name': Translate('黑发女性'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('老婆婆'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('老人'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('贸易商'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('女性'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('哥哥'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('妹妹'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('父亲'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('男孩'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('车00'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('车01'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('车02'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('车03'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('车04'),
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
	'monsters': [
		{
			'pos': (130449, 2000, 38270),
			'angle': 0,
			'unk1': 257,
			'battle': {
				'flags': 0,
				'level': 8,
				'unk': 6,
				'vision': 45,
				'moveRange': 6,
				'canMove': 1,
				'moveSpeed': 25,
				'unk2': 0,
				'battlefield': 'br0000',
				'sepith': (5, 2, 3, 0, 0, 3, 0),
				'setups': [
					(50, {
						'enemies': [
							('ms66500', (8, 8, 180), (7, 4, 0)),
							(None, (5, 9, 180), (10, 11, 225)),
							(None, (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(50, {
						'enemies': [
							('ms66500', (7, 9, 180), (7, 4, 0)),
							('ms66500', (11, 10, 180), (10, 11, 225)),
							(None, (10, 13, 180), (4, 7, 90)),
							(None, (5, 11, 180), (12, 7, 270)),
							(None, (12, 12, 180), (4, 11, 135)),
							(None, (4, 14, 180), (11, 4, 315)),
							(None, (14, 14, 180), (7, 12, 180)),
							(None, (2, 13, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
				],
			},
			'flag': 0,
			'chcpIdx': 16,
			'standAnim': 0,
			'moveAnim': 1,
		},
		{
			'pos': (133810, 3000, 75570),
			'angle': 0,
			'unk1': 257,
			'battle': {
				'flags': 0,
				'level': 8,
				'unk': 6,
				'vision': 45,
				'moveRange': 6,
				'canMove': 1,
				'moveSpeed': 25,
				'unk2': 0,
				'battlefield': 'br0000',
				'sepith': (1, 6, 0, 3, 2, 1, 1),
				'setups': [
					(50, {
						'enemies': [
							('ms69900', (8, 8, 180), (7, 4, 0)),
							(None, (5, 9, 180), (10, 11, 225)),
							(None, (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(50, {
						'enemies': [
							('ms69900', (7, 9, 180), (7, 4, 0)),
							('ms69900', (11, 10, 180), (10, 11, 225)),
							(None, (10, 13, 180), (4, 7, 90)),
							(None, (5, 11, 180), (12, 7, 270)),
							(None, (12, 12, 180), (4, 11, 135)),
							(None, (4, 14, 180), (11, 4, 315)),
							(None, (14, 14, 180), (7, 12, 180)),
							(None, (2, 13, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
				],
			},
			'flag': 0,
			'chcpIdx': 18,
			'standAnim': 2,
			'moveAnim': 3,
		},
	],
	'triggers': [],
	'objects': [
		{
			'pos': (111510, -2000, 78150),
			'range': 1200,
			'bubble_pos': (111510, -1000, 78150),
			'_1': b'|\x00\x00',
			'function': Function((0, 3)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (118170, 3000, 85350),
			'range': 1200,
			'bubble_pos': (118170, 4000, 85350),
			'_1': b'|\x00\x00',
			'function': Function((0, 4)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (550, 0, 4660),
			'range': 1200,
			'bubble_pos': (550, 1000, 4660),
			'_1': b'|\x00\x00',
			'function': Function((0, 26)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (121570, 3000, 68820),
			'range': 1200,
			'bubble_pos': (121570, 3000, 68820),
			'_1': b'|\x00\x00',
			'function': Function((0, 5)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (14350, 0, 4400),
			'range': 1200,
			'bubble_pos': (14350, 2000, 4400),
			'_1': b'|\x00\x00',
			'function': Function((0, 27)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (134500, 3000, 82200),
			'range': 1200,
			'bubble_pos': (134470, 4000, 82230),
			'_1': b'|\x00\x00',
			'function': Function((0, 51)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (6200, 0, -5000),
			'range': 800,
			'bubble_pos': (6200, 1500, -5000),
			'_1': b'|\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (2200, 0, -5000),
			'range': 800,
			'bubble_pos': (2200, 1500, -5000),
			'_1': b'|\x00\x00',
			'function': Function((0, 14)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (13550, 0, -5000),
			'range': 800,
			'bubble_pos': (13550, 1500, -5000),
			'_1': b'|\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (8450, 0, -5000),
			'range': 800,
			'bubble_pos': (8450, 1500, -5000),
			'_1': b'|\x00\x00',
			'function': Function((0, 16)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (16950, 0, 5800),
			'range': 800,
			'bubble_pos': (16950, 1500, 5800),
			'_1': b'|\x00\x00',
			'function': Function((0, 17)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (11850, 0, 5800),
			'range': 800,
			'bubble_pos': (11850, 1500, 5800),
			'_1': b'|\x00\x00',
			'function': Function((0, 18)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (22600, 0, -5000),
			'range': 800,
			'bubble_pos': (22600, 1500, -5000),
			'_1': b'|\x00\x00',
			'function': Function((0, 19)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (18350, 0, -5000),
			'range': 800,
			'bubble_pos': (18360, 1500, -5000),
			'_1': b'|\x00\x00',
			'function': Function((0, 20)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (29400, 0, -5000),
			'range': 800,
			'bubble_pos': (29400, 1500, -5000),
			'_1': b'|\x00\x00',
			'function': Function((0, 21)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (24900, 0, -5000),
			'range': 800,
			'bubble_pos': (24900, 1500, -5000),
			'_1': b'|\x00\x00',
			'function': Function((0, 22)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (4010, 0, 6840),
			'range': 1500,
			'bubble_pos': (4010, 1700, 6840),
			'_1': b'|\x00\x00',
			'function': Function((0, 52)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00D\x16\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00^\x00', Function((0, 1)), Function((0, 2))),
	'code': [None]*53,
	'anim': [
		{
			'speed': 1000,
			'_': 0,
			'count': 8,
			'frames': [
				0,
				1,
				2,
				3,
				4,
				3,
				2,
				1,
			],
		},
		{
			'speed': 2000,
			'_': 0,
			'count': 8,
			'frames': [
				0,
				1,
				2,
				3,
				4,
				3,
				2,
				1,
			],
		},
		{
			'speed': 500,
			'_': 0,
			'count': 6,
			'frames': [
				0,
				1,
				2,
				3,
				4,
				5,
				0,
				0,
			],
		},
		{
			'speed': 1000,
			'_': 0,
			'count': 6,
			'frames': [
				0,
				1,
				2,
				3,
				4,
				5,
				0,
				0,
			],
		},
	],
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
		(Expr([Insn('FLAG', Flag(1106)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(1106)),
			Insn('FLAG_SET', Flag(1107)),
		]),
		(None, []),
	]),
	Insn('0xD0', 7, Expr([Insn('CONST', 12), Insn('SET'), Insn('END')])),
	Insn('FLAG_SET', Flag(1996)),
	Insn('FLAG_SET', Flag(2012)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 31))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(768)), Insn('FLAG', Flag(769)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x09', 268435456),
			Insn('EVENT', Function((0, 28))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1008)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(1008)),
			Insn('EVENT', Function((0, 8))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1009)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(1009)),
			Insn('0xD0', 1, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
			Insn('EVENT', Function((0, 10))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 0), Insn('EQ'), Insn('ATTR', 0), Insn('CONST', 100), Insn('EQ'), Insn('OR'), Insn('ATTR', 0), Insn('CONST', 102), Insn('EQ'), Insn('OR'), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(976)),
			Insn('FLAG_UNSET', Flag(977)),
			Insn('FLAG_UNSET', Flag(978)),
			Insn('FLAG_UNSET', Flag(979)),
			Insn('FLAG_UNSET', Flag(980)),
			Insn('FLAG_UNSET', Flag(981)),
			Insn('FLAG_UNSET', Flag(982)),
			Insn('FLAG_UNSET', Flag(983)),
			Insn('FLAG_UNSET', Flag(984)),
			Insn('FLAG_UNSET', Flag(985)),
			Insn('FLAG_UNSET', Flag(986)),
			Insn('FLAG_UNSET', Flag(987)),
			Insn('FLAG_UNSET', Flag(988)),
			Insn('FLAG_UNSET', Flag(989)),
			Insn('FLAG_UNSET', Flag(990)),
			Insn('FLAG_UNSET', Flag(991)),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(976)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(977)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(978)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(979)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(980)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(981)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(982)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(983)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(984)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(985)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(986)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(987)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(988)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 10), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(989)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 20), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(990)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 100), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(991)),
				]),
				(None, []),
			]),
			Insn('FLAG_UNSET', Flag(992)),
			Insn('FLAG_UNSET', Flag(993)),
			Insn('FLAG_UNSET', Flag(994)),
			Insn('FLAG_UNSET', Flag(995)),
			Insn('FLAG_UNSET', Flag(996)),
			Insn('FLAG_UNSET', Flag(997)),
			Insn('FLAG_UNSET', Flag(998)),
			Insn('FLAG_UNSET', Flag(999)),
			Insn('EXPR_VAR', 4, Expr([Insn('RAND'), Insn('CONST', 8), Insn('MOD'), Insn('SET'), Insn('END')])),
			Insn('IF', [
				(Expr([Insn('VAR', 4), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(992)),
				]),
				(Expr([Insn('VAR', 4), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(993)),
				]),
				(Expr([Insn('VAR', 4), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(994)),
				]),
				(Expr([Insn('VAR', 4), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(995)),
				]),
				(Expr([Insn('VAR', 4), Insn('CONST', 4), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(996)),
				]),
				(Expr([Insn('VAR', 4), Insn('CONST', 5), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(997)),
				]),
				(Expr([Insn('VAR', 4), Insn('CONST', 6), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(998)),
				]),
				(Expr([Insn('VAR', 4), Insn('CONST', 7), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(999)),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 20))), Insn('END')]), [
							Insn('CHAR_FLAG1_UNSET', Char(8), 128),
							Insn('CHAR_FLAG1_UNSET', Char(9), 128),
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
		(Expr([Insn('FLAG', Flag(1024)), Insn('FLAG', Flag(1280)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1183)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 30))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(769)), Insn('NOT'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 100), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 4), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
			Insn('EXIT_SET_ENABLED', 0, 0),
			Insn('EXIT_SET_ENABLED', 2, 1),
		]),
		(None, [
			Insn('EXIT_SET_ENABLED', 0, 1),
			Insn('EXIT_SET_ENABLED', 2, 0),
		]),
	]),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('OBJ_FLAG_SET', Object(0), 4),
	Insn('OBJ_FLAG_SET', Object(5), 4),
	Insn('0x65', 4, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1537)), Insn('FLAG', Flag(1542)), Insn('NOT'), Insn('BOOL_AND'), Insn('0x23', 1), Insn('CONST', 2), Insn('EQ'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(5), 'light', Insn('0', 1)),
			Insn('OBJ_FLAG_UNSET', Object(5), 4),
			Insn('0x66', 4, 1),
		]),
		(None, [
			Insn('0x16', Insn('3', b'\x03\x01\x00')),
		]),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(2048)), Insn('NOT'), Insn('END')]), [
			Insn('0x70', Object(2), b'\x00\x00'),
		]),
		(None, [
			Insn('0x70', Object(2), b'\x1e\x00'),
		]),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(2049)), Insn('NOT'), Insn('END')]), [
			Insn('0x70', Object(3), b'\x00\x00'),
		]),
		(None, [
			Insn('0x70', Object(3), b'\x1e\x00'),
		]),
	]),
	Insn('0x65', 3, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(976)), Insn('END')]), [
			Insn('EFF_LOAD', ResId(9), 'event\\eva00_00.eff'),
			Insn('EFF_PLAY', (ResId(9), 9), Char(255), 0, -9502, 1, 3000, 0, 3284, 1, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
			Insn('0x66', 3, 1),
		]),
		(None, []),
	]),
	Insn('0x65', 5, 1),
	Insn('OBJ_FLAG_SET', Object(11), 4),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 46, Insn('TASK_GET', 1))), Insn('EXEC', Insn('QUEST_GET', 46, Insn('TASK_GET', 5))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x66', 5, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(11), 4),
		]),
		(None, []),
	]),
	Insn('0x78', b'\x06', Char(20)),
	Insn('0x78', b'\x07', Char(21)),
	Insn('0x78', b'\x08', Char(22)),
	Insn('0x78', b'\t', Char(23)),
	Insn('0x78', b'\n', Char(24)),
	Insn('OBJ_FLAG_SET', Object(6), 4),
	Insn('OBJ_FLAG_SET', Object(7), 4),
	Insn('OBJ_FLAG_SET', Object(8), 4),
	Insn('OBJ_FLAG_SET', Object(9), 4),
	Insn('OBJ_FLAG_SET', Object(10), 4),
	Insn('OBJ_SET_FRAME', Object(6), 'light', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(7), 'light', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(8), 'light', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(9), 'light', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(10), 'light', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(6), 'chukin', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(7), 'chukin', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(8), 'chukin', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(9), 'chukin', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(10), 'chukin', Insn('0', 1)),
	Insn('0x65', 6, 1),
	Insn('0x65', 7, 1),
	Insn('0x65', 8, 1),
	Insn('0x65', 9, 1),
	Insn('0x65', 10, 1),
	Insn('0x65', 11, 1),
	Insn('0x65', 12, 1),
	Insn('0x65', 13, 1),
	Insn('0x65', 14, 1),
	Insn('0x65', 15, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(6), 4),
			Insn('OBJ_FLAG_UNSET', Object(7), 4),
			Insn('OBJ_FLAG_UNSET', Object(8), 4),
			Insn('CHAR_SET_POS', Char(20), (4270, 0, -5000), 270),
			Insn('0xD3', Char(20), 0, 270000, 0, 0),
			Insn('CHAR_SET_POS', Char(21), (10750, 0, -5000), 270),
			Insn('0xD3', Char(21), 0, 270000, 0, 0),
			Insn('CHAR_SET_POS', Char(22), (14000, 0, 5750), 270),
			Insn('0xD3', Char(22), 0, 270000, 0, 0),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 20))), Insn('END')]), []),
						(None, [
							Insn('OBJ_FLAG_UNSET', Object(10), 4),
							Insn('CHAR_SET_POS', Char(24), (27500, 0, -5000), 270),
							Insn('0xD3', Char(24), 0, 270000, 0, 0),
						]),
					]),
				]),
				(None, [
					Insn('OBJ_FLAG_UNSET', Object(9), 4),
					Insn('OBJ_FLAG_UNSET', Object(10), 4),
					Insn('CHAR_SET_POS', Char(23), (20500, 0, -5000), 270),
					Insn('0xD3', Char(23), 0, 270000, 0, 0),
					Insn('CHAR_SET_POS', Char(24), (27500, 0, -5000), 270),
					Insn('0xD3', Char(24), 0, 270000, 0, 0),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(6), 4),
			Insn('OBJ_FLAG_UNSET', Object(7), 4),
			Insn('OBJ_FLAG_UNSET', Object(8), 4),
			Insn('OBJ_FLAG_UNSET', Object(10), 4),
			Insn('CHAR_SET_POS', Char(20), (4270, 0, -5000), 270),
			Insn('0xD3', Char(20), 0, 270000, 0, 0),
			Insn('CHAR_SET_POS', Char(21), (10750, 0, -5000), 270),
			Insn('0xD3', Char(21), 0, 270000, 0, 0),
			Insn('CHAR_SET_POS', Char(22), (14000, 0, 5750), 270),
			Insn('0xD3', Char(22), 0, 270000, 0, 0),
			Insn('CHAR_SET_POS', Char(24), (27500, 0, -5000), 270),
			Insn('0xD3', Char(24), 0, 270000, 0, 0),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('FLAG_GET', 16))), Insn('END')]), []),
				(None, [
					Insn('OBJ_FLAG_UNSET', Object(9), 4),
					Insn('CHAR_SET_POS', Char(23), (20500, 0, -5000), 270),
					Insn('0xD3', Char(23), 0, 270000, 0, 0),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(6), 4),
			Insn('OBJ_FLAG_UNSET', Object(7), 4),
			Insn('OBJ_FLAG_UNSET', Object(8), 4),
			Insn('OBJ_FLAG_UNSET', Object(9), 4),
			Insn('OBJ_FLAG_UNSET', Object(10), 4),
			Insn('CHAR_SET_POS', Char(20), (4270, 0, -5000), 270),
			Insn('0xD3', Char(20), 0, 270000, 0, 0),
			Insn('CHAR_SET_POS', Char(21), (10750, 0, -5000), 270),
			Insn('0xD3', Char(21), 0, 270000, 0, 0),
			Insn('CHAR_SET_POS', Char(22), (14000, 0, 5750), 270),
			Insn('0xD3', Char(22), 0, 270000, 0, 0),
			Insn('CHAR_SET_POS', Char(23), (20500, 0, -5000), 270),
			Insn('0xD3', Char(23), 0, 270000, 0, 0),
			Insn('CHAR_SET_POS', Char(24), (27500, 0, -5000), 270),
			Insn('0xD3', Char(24), 0, 270000, 0, 0),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('FLAG_GET', 16))), Insn('END')]), []),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 0))), Insn('END')]), [
					Insn('0x66', 6, 1),
					Insn('0x66', 7, 1),
					Insn('0x66', 8, 1),
					Insn('0x66', 9, 1),
					Insn('0x66', 10, 1),
					Insn('0x66', 11, 1),
					Insn('0x66', 12, 1),
					Insn('0x66', 13, 1),
					Insn('0x66', 14, 1),
					Insn('0x66', 15, 1),
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 10))), Insn('END')]), [
							Insn('OBJ_SET_FRAME', Object(6), 'chukin', Insn('1', 1)),
						]),
						(None, []),
					]),
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 12))), Insn('END')]), [
							Insn('OBJ_SET_FRAME', Object(7), 'chukin', Insn('1', 1)),
						]),
						(None, []),
					]),
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 14))), Insn('END')]), [
							Insn('OBJ_SET_FRAME', Object(8), 'chukin', Insn('1', 1)),
						]),
						(None, []),
					]),
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 16))), Insn('END')]), [
							Insn('OBJ_SET_FRAME', Object(9), 'chukin', Insn('1', 1)),
						]),
						(None, []),
					]),
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 18))), Insn('END')]), [
							Insn('OBJ_SET_FRAME', Object(10), 'chukin', Insn('1', 1)),
						]),
						(None, []),
					]),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('0xF2', Insn('CHEST')),
	Insn('0x09', 134217728),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(2048)), Insn('NOT'), Insn('END')]), [
			Insn('SOUND_PLAY', 14, 0, 0, 100),
			Insn('0x71', Object(2), b'\x00\x00', 30, 0),
			Insn('SLEEP', 500),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('ITEM_ADD', 501, 1)), Insn('END')]), [
					Insn('FADE_ON', 300, Color(0x00000000), 100),
					Insn('SOUND_PLAY', 17, 0, 0, 100),
					Insn('TEXT_SET_POS', -1, -1, -1, -1),
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(999), Text(
						'{color 0}已取得{item 501}{color 0}。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('TEXT_SET_POS', -1, 280, 60, 3),
					Insn('FADE_OFF', 300, Color(0x00000000)),
					Insn('FLAG_SET', Flag(2048)),
					Insn('0xDE', b'\x06\x00'),
				]),
				(None, [
					Insn('FADE_ON', 300, Color(0x00000000), 100),
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(999), Text(
						'宝箱内装着{item 501}{color 0}。\n'
						'但因持有物品已满而放弃{item 501}{color 0}。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('FADE_OFF', 300, Color(0x00000000)),
					Insn('SOUND_PLAY', 15, 0, 0, 100),
					Insn('0x71', Object(2), b'\x1e\x00', 0, 0),
				]),
			]),
		]),
		(None, [
			Insn('FADE_ON', 300, Color(0x00000000), 100),
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(999), Text(
				'{0x06}{color 5}宝箱内空无一物。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('FADE_OFF', 300, Color(0x00000000)),
		]),
	]),
	Insn('SLEEP', 30),
	Insn('TEXT_END', Char(255)),
	Insn('0x0A', 134217728),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('0xF2', Insn('CHEST')),
	Insn('0x09', 134217728),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(2049)), Insn('NOT'), Insn('END')]), [
			Insn('SOUND_PLAY', 14, 0, 0, 100),
			Insn('0x71', Object(3), b'\x00\x00', 30, 0),
			Insn('SLEEP', 500),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('ITEM_ADD', 1503, 1)), Insn('END')]), [
					Insn('FADE_ON', 300, Color(0x00000000), 100),
					Insn('SOUND_PLAY', 17, 0, 0, 100),
					Insn('TEXT_SET_POS', -1, -1, -1, -1),
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(999), Text(
						'{color 0}已取得{item 1503}{color 0}。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('TEXT_SET_POS', -1, 280, 60, 3),
					Insn('FADE_OFF', 300, Color(0x00000000)),
					Insn('FLAG_SET', Flag(2049)),
					Insn('0xDE', b'\x06\x00'),
				]),
				(None, [
					Insn('FADE_ON', 300, Color(0x00000000), 100),
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(999), Text(
						'宝箱内装着{item 1503}{color 0}。\n'
						'但因持有物品已满而放弃{item 1503}{color 0}。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('FADE_OFF', 300, Color(0x00000000)),
					Insn('SOUND_PLAY', 15, 0, 0, 100),
					Insn('0x71', Object(3), b'\x1e\x00', 0, 0),
				]),
			]),
		]),
		(None, [
			Insn('FADE_ON', 300, Color(0x00000000), 100),
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(999), Text(
				'{0x06}{color 5}宝箱内空无一物。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('FADE_OFF', 300, Color(0x00000000)),
		]),
	]),
	Insn('SLEEP', 30),
	Insn('TEXT_END', Char(255)),
	Insn('0x0A', 134217728),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('TEXT_START', Char(255)),
	Insn('CALL', Function((1, 0))),
	Insn('FLAG_UNSET', Flag(976)),
	Insn('0x65', 3, 1),
	Insn('EFF_STOP', (ResId(9), 2)),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('EVENT_BEGIN', 1),
	Insn('0x09', 134217728),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}有个巴士车站。\n'
		'要乘坐巴士吗？{wait}'
	)),
	Insn('MENU', 0, -1, -1, 1, Text(
		'阿尔摩利卡村\n'
		'唐古拉姆门\n'
		'停靠站（三岔路）\n'
		'放弃\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('CALL', Function((0, 7))),
			Insn('0x0A', 134217728),
			Insn('NEW_SCENE', 't0000', b'\x00\x00\x00\x07'),
		]),
		(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
			Insn('CALL', Function((0, 7))),
			Insn('0x0A', 134217728),
			Insn('NEW_SCENE', 't2500', b'\x00\x00\x00\x07'),
		]),
		(Expr([Insn('VAR', 0), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
			Insn('CALL', Function((0, 7))),
			Insn('0x0A', 134217728),
			Insn('NEW_SCENE', 'r0030', b'\x00\x00\x00\x07'),
		]),
		(None, []),
	]),
	Insn('0x0A', 134217728),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-620, 600, 4110), 0),
	Insn('CAM_ROTATE', 45, 25, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 27000, 0),
	Insn('0xE0', b'\x01'),
	Insn('CHAR_SET_POS', Char(0), (-1000, 0, 4500), 180),
	Insn('CHAR_SET_POS', Char(1), (-1000, 0, 5600), 180),
	Insn('CHAR_SET_POS', Char(2), (-1000, 0, 6700), 180),
	Insn('CHAR_SET_POS', Char(3), (-1000, 0, 7800), 180),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('OBJ_FLAG_UNSET', Object(0), 4),
	Insn('0x78', b'\x00', Char(10)),
	Insn('OBJ_SET_FRAME', Object(0), 'light', Insn('0', 1)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(10), (16000, 0, 0), 0),
	Insn('0xD3', Char(10), 0, 270000, 0, 0),
	Insn('OBJ_FLAG_SET', Object(0), 4096),
	Insn('0x74', Object(0), 7680),
	Insn('0x0D'),
	Insn('0x71', Object(0), b'y\x00', 180, 32),
	Insn('FORK', 10, 1, [
		Insn('0x98', Char(254), (-16000, 0, 0), 4000, 0),
	]),
	Insn('SOUND_PLAY', 466, 0, 0, 100),
	Insn('SOUND_PLAY', 467, 0, 0, 100),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('0x71', Object(0), b'[\x00', 120, 0),
	Insn('0x79', b'\x00\x00'),
	Insn('SLEEP', 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FLAG_SET', Flag(1008)),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('EVENT_BEGIN', 1),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('CHAR_SET_POS', Char(0), (-1000, 0, 4500), 180),
	Insn('CHAR_SET_POS', Char(1), (-1000, 0, 4500), 180),
	Insn('CHAR_SET_POS', Char(2), (-1000, 0, 4500), 180),
	Insn('CHAR_SET_POS', Char(3), (-1000, 0, 4500), 180),
	Insn('SLEEP', 1),
	Insn('CAM_OFFSET', (-1000, 600, 4500), 0),
	Insn('CAM_ROTATE', 45, 21, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][9] = [
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
					(Expr([Insn('VAR', 5), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄中央广场'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 0)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄中央广场'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 5), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄东出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 1)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄东出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 5), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄西出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 2)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄西出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 5), Insn('CONST', 4), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄南出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 3)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄南出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 5), Insn('CONST', 5), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄北出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 4)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄北出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 5), Insn('CONST', 6), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★唐古拉姆门'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 5)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000唐古拉姆门'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 5), Insn('CONST', 7), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★贝尔加德门'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 6)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000贝尔加德门'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 5), Insn('CONST', 8), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★乌尔斯拉医科大学'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 7)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000乌尔斯拉医科大学'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 5), Insn('CONST', 9), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★阿尔摩利卡村'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 8)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000阿尔摩利卡村'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 5), Insn('CONST', 10), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★玛因兹矿山镇'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 9)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000玛因兹矿山镇'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 5), Insn('CONST', 11), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★玛因兹山道丄隧道内'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 10)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000玛因兹山道丄隧道内'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 5), Insn('CONST', 12), Insn('EQ'), Insn('END')]), [
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
						Insn('0x74', Object(5), 7680),
						Insn('0x71', Object(5), b'\xf1\x00', 270, 0),
						Insn('SOUND_PLAY', 464, 0, 0, 100),
						Insn('0x79', b'\x05\x00'),
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

data['code'][10] = [
	Insn('EVENT_BEGIN', 1),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('CHAR_SET_POS', Char(0), (14360, 0, 2630), 180),
	Insn('CHAR_SET_POS', Char(1), (14360, 0, 2630), 180),
	Insn('CHAR_SET_POS', Char(2), (14360, 0, 2630), 180),
	Insn('CHAR_SET_POS', Char(3), (14360, 0, 2630), 180),
	Insn('CHAR_SET_POS', Char(4), (14360, 0, 2630), 180),
	Insn('CHAR_SET_POS', Char(5), (14360, 0, 2630), 180),
	Insn('SLEEP', 1),
	Insn('CAM_OFFSET', (14360, 600, 2630), 0),
	Insn('CAM_ROTATE', 45, 21, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 25000, 0),
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

data['code'][11] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(8), Text(
		'可恶～还是\n'
		'被发现了吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'还以为在纪念庆典期间\n'
		'就不会有事呢……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(9), Text(
		'嗯，您就是用一封申请书\n'
		'停了两辆车的先生吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'来，请在这里签名……\n'
		'罚金的话则是…{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('TEXT_START', Char(255)),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}似乎是乌尔努公司制造的高级车。{wait}'
		'{page}'
		'车牌号码是『ＶＥ\u3000４３１０』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FLAG_SET', Flag(1521)),
	Insn('CALL', Function((0, 24))),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('TEXT_START', Char(255)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 10))), Insn('END')]), [
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}车上贴着违规停车的\n'
				'警告标志。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
		]),
		(None, [
			Insn('CALL', Function((0, 23))),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('NOT'), Insn('END')]), [
					Insn('SLEEP', 300),
					Insn('SOUND_PLAY', 959, 0, 0, 100),
					Insn('OBJ_SET_FRAME', Object(6), 'chukin', Insn('1', 1)),
					Insn('QUEST', 23, Insn('TASK_SET', 10)),
				]),
				(None, []),
			]),
		]),
	]),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('TEXT_START', Char(255)),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}似乎是乌尔努公司制造的导力搬运车。{wait}'
		'{page}'
		'车牌号码是『ＥＳ\u3000４５２１』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FLAG_SET', Flag(1522)),
	Insn('CALL', Function((0, 24))),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('TEXT_START', Char(255)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 12))), Insn('END')]), [
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}车上贴着违规停车的\n'
				'警告标志。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
		]),
		(None, [
			Insn('CALL', Function((0, 23))),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('NOT'), Insn('END')]), [
					Insn('SLEEP', 300),
					Insn('SOUND_PLAY', 959, 0, 0, 100),
					Insn('OBJ_SET_FRAME', Object(7), 'chukin', Insn('1', 1)),
					Insn('QUEST', 23, Insn('TASK_SET', 12)),
				]),
				(None, []),
			]),
		]),
	]),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('TEXT_START', Char(255)),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}似乎是乌尔努公司制造的导力搬运车。{wait}'
		'{page}'
		'车牌号码是『ＬＡ\u3000５８２８』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FLAG_SET', Flag(1523)),
	Insn('CALL', Function((0, 24))),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('TEXT_START', Char(255)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 14))), Insn('END')]), [
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}车上贴着违规停车的\n'
				'警告标志。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
		]),
		(None, [
			Insn('CALL', Function((0, 23))),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('NOT'), Insn('END')]), [
					Insn('SLEEP', 300),
					Insn('SOUND_PLAY', 959, 0, 0, 100),
					Insn('OBJ_SET_FRAME', Object(8), 'chukin', Insn('1', 1)),
					Insn('QUEST', 23, Insn('TASK_SET', 14)),
				]),
				(None, []),
			]),
		]),
	]),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('TEXT_START', Char(255)),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}似乎是乌尔努公司制造的家用车。{wait}'
		'{page}'
		'车牌号码是『ＣＷ\u3000６４２２』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FLAG_SET', Flag(1524)),
	Insn('CALL', Function((0, 24))),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('TEXT_START', Char(255)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 16))), Insn('END')]), [
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}车上贴着违规停车的\n'
				'警告标志。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
		]),
		(None, [
			Insn('CALL', Function((0, 23))),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('NOT'), Insn('END')]), [
					Insn('SLEEP', 300),
					Insn('SOUND_PLAY', 959, 0, 0, 100),
					Insn('OBJ_SET_FRAME', Object(9), 'chukin', Insn('1', 1)),
					Insn('QUEST', 23, Insn('TASK_SET', 16)),
				]),
				(None, []),
			]),
		]),
	]),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('TEXT_START', Char(255)),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}似乎是莱恩福尔特公司制造的高级车。{wait}'
		'{page}'
		'车牌号码是『ＣＬ\u3000１１０１』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 20))), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F（记得这个车牌号码\n'
				'\u3000在西出口那边也出现过……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 19))), Insn('FLAG', Flag(1509)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 25))),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 19))), Insn('FLAG', Flag(1508)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F（咦…………？）{wait}'
				'{page}'
				'#0003F（这个号码，好像在哪里\n'
				'\u3000看到过呢……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1508)), Insn('NOT'), Insn('END')]), [
			Insn('FLAG_SET', Flag(1509)),
		]),
		(None, []),
	]),
	Insn('FLAG_SET', Flag(1525)),
	Insn('CALL', Function((0, 24))),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('TEXT_START', Char(255)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 18))), Insn('END')]), [
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}车上贴着违规停车的\n'
				'警告标志。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
		]),
		(None, [
			Insn('CALL', Function((0, 23))),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('NOT'), Insn('END')]), [
					Insn('SLEEP', 300),
					Insn('SOUND_PLAY', 959, 0, 0, 100),
					Insn('OBJ_SET_FRAME', Object(10), 'chukin', Insn('1', 1)),
					Insn('QUEST', 23, Insn('TASK_SET', 18)),
				]),
				(None, []),
			]),
		]),
	]),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}要贴警告标志吗？{0x18}{wait}'
	)),
	Insn('MENU', 0, -1, 150, 1, Text(
		'【贴】\n'
		'【不贴】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1517)), Insn('FLAG', Flag(1518)), Insn('BOOL_AND'), Insn('FLAG', Flag(1519)), Insn('BOOL_AND'), Insn('FLAG', Flag(1520)), Insn('BOOL_AND'), Insn('FLAG', Flag(1521)), Insn('BOOL_AND'), Insn('FLAG', Flag(1522)), Insn('BOOL_AND'), Insn('FLAG', Flag(1523)), Insn('BOOL_AND'), Insn('FLAG', Flag(1524)), Insn('BOOL_AND'), Insn('FLAG', Flag(1525)), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 23, Insn('TASK_GET', 19))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F好……这样一来，\n'
				'所有车辆的号码\n'
				'都检查过了吧。{wait}'
				'{page}'
				'把剩下的标志贴完，\n'
				'就回去报告吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F好，就这样吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F反正也不急，\n'
				'回去之前还是\n'
				'确认一遍比较好吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F但就算贴错了，\n'
				'也没法再撕掉……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F哈哈……\n'
				'我想应该没问题吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('QUEST', 23, Insn('TASK_SET', 19)),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('0xE0', b'\x01'),
	Insn('CAM_OFFSET', (31390, 600, -2940), 0),
	Insn('CAM_ROTATE', 42, 24, 0, 0),
	Insn('0x6E', 490, 0),
	Insn('CAM_DISTANCE', 19340, 0),
	Insn('CHAR_SET_POS', Char(257), (31050, 0, -4940), 270),
	Insn('CHAR_SET_POS', Char(258), (32700, 0, -4120), 270),
	Insn('CHAR_SET_POS', Char(259), (31500, 0, -3440), 225),
	Insn('CHAR_SET_POS', Char(260), (31000, 0, -2310), 225),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0005F……………………？{wait}'
		'{page}'
		'#0001F这个号码……\n'
		'在西出口好像也出现过吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11P#0105F这么说来……\n'
		'似乎还真的有印象呢。{wait}'
		'{page}'
		'#0100F但那边的好像\n'
		'并不是家用车。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#5P#0200F牌号相同的车辆，\n'
		'本来应该不可能出现的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#5P#0303F唔……这是个得到过许可\n'
		'的车号啊。{wait}'
		'{page}'
		'#0300F嗯，姑且还是记下来\n'
		'为好吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0000F也是……\n'
		'稍后再向公共安全课\n'
		'的人汇报吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0xE0', b'\x00'),
	Insn('CHAR_SET_POS', Char(0), (31050, 0, -4940), 270),
	Insn('QUEST', 23, Insn('TASK_SET', 20)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CALL', Function((0, 6))),
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
				'#0006F……还是努力\n'
				'步行去阿尔摩利卡村吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_END', Char(255)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('EXPR_VAR', 5, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
	Insn('CALL', Function((0, 9))),
	Insn('RETURN'),
]

data['code'][28] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (-5000, 1000, 0), 0),
	Insn('CAM_ROTATE', 36, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(257), (-7100, 0, -700), 90),
	Insn('CHAR_SET_POS', Char(258), (-8500, 0, -700), 90),
	Insn('CHAR_SET_POS', Char(259), (-8500, 0, 700), 90),
	Insn('CHAR_SET_POS', Char(260), (-7100, 0, 700), 90),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('OBJ_FLAG_UNSET', Object(0), 4),
	Insn('0x78', b'\x00', Char(10)),
	Insn('OBJ_SET_FRAME', Object(0), 'light', Insn('0', 1)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(10), (16000, 0, 6000), 0),
	Insn('0xD3', Char(10), 0, 270000, 0, 0),
	Insn('OBJ_FLAG_SET', Object(0), 4096),
	Insn('0x74', Object(0), 7680),
	Insn('0x70', Object(0), b'\x1e\x00'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('FORK', 257, 1, [
		Insn('0x97', Char(254), (2000, 0, 0), 2000, 0),
	]),
	Insn('FORK', 258, 1, [
		Insn('0x97', Char(254), (2000, 0, 0), 2000, 0),
	]),
	Insn('FORK', 260, 1, [
		Insn('0x97', Char(254), (2000, 0, 0), 2000, 0),
	]),
	Insn('FORK', 259, 1, [
		Insn('0x97', Char(254), (2000, 0, 0), 2000, 0),
	]),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
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
	Insn('CAM_OFFSET', (15320, 1000, 6120), 2500),
	Insn('0x6F', b'\x01'),
	Insn('0x71', Object(0), b'\x1f\x00', 60, 0),
	Insn('SOUND_PLAY', 463, 0, 0, 100),
	Insn('0x79', b'\x00\x00'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100261V#0011F糟了……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_FUNC', Char(25), 1, Function((0, 29))),
	Insn('0x71', Object(0), b'<\x00', 90, 0),
	Insn('0x79', b'\x00\x00'),
	Insn('0x71', Object(0), b'\xb4\x00', 121, 32),
	Insn('FORK', 10, 1, [
		Insn('0x98', Char(254), (1000, 0, 0), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('SLEEP', 100),
	Insn('CAM_OFFSET', (15320, 1000, 0), 4000),
	Insn('0x71', Object(0), b'y\x00', 180, 32),
	Insn('FORK', 10, 1, [
		Insn('0x9E', Char(254), 17000, 2000, -180000, 3000, b'\x01\x00'),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('0x71', Object(0), b'<\x00', 90, 0),
	Insn('0x79', b'\x00\x00'),
	Insn('0x71', Object(0), b'y\x00', 180, 32),
	Insn('FORK', 10, 1, [
		Insn('0x98', Char(254), (20000, 0, 0), 6000, 0),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('OBJ_FLAG_SET', Object(0), 4),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('0x6F', b'\x01'),
	Insn('CAM_OFFSET', (3200, 800, 0), 2000),
	Insn('FORK', 257, 1, [
		Insn('0x97', Char(254), (7000, 0, 0), 4000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x97', Char(254), (7000, 0, 0), 4000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('0x97', Char(254), (7000, 0, 0), 4000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x97', Char(254), (7000, 0, 0), 4000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100262V#0106F#6P走掉了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100263V#0306F#5P喂喂，不是吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(260), 180, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100264V#0308F#5P导力巴士\n'
		'有多少班啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 0, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100265V#0006F#12P嗯，这个……\n'
		'应该还挺多的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(259), 0, 500),
	Insn('SLEEP', 500),
	Insn('FORK_LOOP', 257, 1, [
		Insn('CHAR_WATCH', Char(257), Char(259), 500),
	]),
	Insn('FORK_LOOP', 258, 1, [
		Insn('CHAR_WATCH', Char(258), Char(259), 500),
	]),
	Insn('FORK_LOOP', 260, 1, [
		Insn('CHAR_WATCH', Char(260), Char(259), 500),
	]),
	Insn('CAM_OFFSET', (1810, 800, 2340), 2000),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (610, 0, 3820), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('0x6F', b'\x01'),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100266V#0203F#6P根据时刻表……{wait}'
		'{page}'
		'#11100267V#0200F下一班车\n'
		'好像是两小时后来呢。{wait}'
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
	Insn('TEXT_TALK', Char(258), Text(
		'#11100268V#0105F#6P那、那么久……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100269V#0306F#11P这么说，一天内也只有\n'
		'区区几班啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100270V#0006F#12P……伤脑筋呢。\n'
		'原本想在今天至少去一趟医院的。{wait}'
		'{page}'
		'#11100271V#0008F可是，改变原定计划，\n'
		'先去其他地方似乎也不太好……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100272V#0106F#6P是呀……\n'
		'我们刚刚才决定了调查方针呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(259)),
	Insn('CHAR_ROTATE', Char(259), 180, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100273V#0200F#5P──既然如此，\n'
		'走过去不就好了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100274V#0005F#12P哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100275V#0105F#6P缇欧……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100276V#0305F#2P喂喂……真的假的？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (1980, 800, 790), 1500),
	Insn('FORK_LOOP', 257, 1, [
		Insn('CHAR_WATCH', Char(257), Char(259), 500),
	]),
	Insn('FORK_LOOP', 258, 1, [
		Insn('CHAR_WATCH', Char(258), Char(259), 500),
	]),
	Insn('FORK_LOOP', 260, 1, [
		Insn('CHAR_WATCH', Char(260), Char(259), 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (500, 0, 700), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100277V#0204F#5P从地图上来看，\n'
		'从这里到阿尔摩利卡村\n'
		'步行大约需要一个半小时。{wait}'
		'{page}'
		'#11100278V#0202F如果乘坐下一班巴士去，\n'
		'加上等车时间，\n'
		'应该要两个半小时。{wait}'
		'{page}'
		'#11100279V相比之下，步行的话\n'
		'不是更有效率吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100280V#0100F#6P原来如此……计算起来确实是这样呢。{wait}'
		'{page}'
		'#11100281V#0104F我听说，在阿尔摩利卡村前，\n'
		'有一条放远望去都是田园风光的\n'
		'石板路……{wait}'
		'{page}'
		'#11100282V#0102F就当是一次远足，\n'
		'说不定也很惬意呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1500),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100283V#0306F#5P（喂喂，小姐们\n'
		'\u3000竟然敢这样说啊……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100284V#0006F#11P（这话听起来就像是\n'
		'\u3000从没在郊外走过路的样子呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 300),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100285V#0105F#6P你们两个怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(258), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100286V#0012F#11P不，没什么……{wait}'
		'{page}'
		'#11100287V#0001F那个，郊外还有魔兽徘徊，\n'
		'你们两个没问题吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100288V#0106F#6P嗯……这么说来，魔兽也是个问题呢。{wait}'
		'{page}'
		'#11100289V#0100F不过，我们之前也潜入过\n'
		'地下区域好几次了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100290V#0203F#6P而且我也需要\n'
		'测试魔导杖。{wait}'
		'{page}'
		'#11100291V#0200F适当的实战\n'
		'正是求之不得的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100292V#0006F#11P嗯……{wait}'
		'{page}'
		'#11100293V#0000F──好吧。\n'
		'既然你们都这么说了，那就走过去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100294V#0100F#6P嗯，走吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 1500),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 400),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 400),
	]),
	Insn('SLEEP', 500),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'\xcc\x00\x00'),
	Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 204), Insn('SET'), Insn('END')])),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100295V#0109F#12P呵呵，真有点期待呢。{wait}'
		'{page}'
		'#11100296V#0102F早知道这样的话，\n'
		'事先做个便当带来就好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100297V#0204F#5P……的确。{wait}'
		'{page}'
		'#11100298V#0202F不过，中午之前\n'
		'应该能到达村子，\n'
		'午饭就在那边吃好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (8, 9, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 2000, (8, 9, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100299V#0008F#11P（……她们两个要是\n'
		'\u3000累了的话，就由我们负责支援吧。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100300V#0302F#5P（是是，明白。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CAM_DISTANCE', 25500, 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (-1070, 600, -160), 0),
	Insn('CAM_ROTATE', 45, 21, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(0), (-1070, 0, -160), 90),
	Insn('FLAG_SET', Flag(769)),
	Insn('QUEST', 63, Insn('TASK_SET', 1)),
	Insn('FORK_QUIT', Char(25), 1),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][29] = [
	Insn('SOUND_PLAY', 470, 0, 0, 100),
	Insn('SLEEP', 2000),
	Insn('SOUND_PLAY', 465, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 467, 0, 0, 100),
	Insn('SLEEP', 4500),
	Insn('SOUND_PLAY', 469, 0, 0, 100),
	Insn('SLEEP', 2000),
	Insn('SOUND_LOOP', 469, 90),
	Insn('SLEEP', 300),
	Insn('SOUND_LOOP', 469, 80),
	Insn('SLEEP', 300),
	Insn('SOUND_LOOP', 469, 70),
	Insn('SLEEP', 300),
	Insn('SOUND_LOOP', 469, 60),
	Insn('SLEEP', 300),
	Insn('SOUND_LOOP', 469, 50),
	Insn('SLEEP', 300),
	Insn('SOUND_LOOP', 469, 40),
	Insn('SLEEP', 300),
	Insn('SOUND_LOOP', 469, 30),
	Insn('SLEEP', 300),
	Insn('SOUND_LOOP', 469, 20),
	Insn('SLEEP', 300),
	Insn('SOUND_LOOP', 469, 10),
	Insn('RETURN'),
]

data['code'][30] = [
	Insn('EVENT_BEGIN', 0),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (920, 600, 5160), 5000),
	Insn('CAM_ROTATE', 45, 21, 0, 5000),
	Insn('0x6E', 450, 5000),
	Insn('CAM_DISTANCE', 25000, 5000),
	Insn('0x6F', b'y'),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}调查停靠站的告示牌后，\n'
		'就能乘坐导力巴士。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}进而便可迅速移动至所选目的地，\n'
		'以更高的效率来往于各处。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(1183)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][31] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0xE0', b'\x01'),
	Insn('LOAD_CHCP', 'chr/ch07300', 35),
	Insn('LOAD_CHCP', 'chr/ch24100', 36),
	Insn('LOAD_CHCP', 'chr/ch20800', 37),
	Insn('LOAD_CHCP', 'chr/ch33000', 38),
	Insn('LOAD_CHCP', 'chr/ch24500', 39),
	Insn('LOAD_CHCP', 'chr/ch21200', 40),
	Insn('LOAD_CHCP', 'chr/ch21300', 41),
	Insn('LOAD_CHCP', 'chr/ch21000', 42),
	Insn('LOAD_CHCP', 'chr/ch21400', 43),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG2_UNSET', Char(11), 32768),
	Insn('CHAR_SET_CHCP', Char(11), 35),
	Insn('CHAR_SET_FRAME', Char(11), 0),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG2_UNSET', Char(12), 32768),
	Insn('CHAR_SET_CHCP', Char(12), 36),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('CHAR_FLAG1_UNSET', Char(13), 128),
	Insn('CHAR_FLAG2_UNSET', Char(13), 32768),
	Insn('CHAR_SET_CHCP', Char(13), 37),
	Insn('CHAR_SET_FRAME', Char(13), 0),
	Insn('CHAR_FLAG1_UNSET', Char(14), 128),
	Insn('CHAR_FLAG2_UNSET', Char(14), 32768),
	Insn('CHAR_SET_CHCP', Char(14), 38),
	Insn('CHAR_SET_FRAME', Char(14), 0),
	Insn('CHAR_FLAG1_UNSET', Char(15), 128),
	Insn('CHAR_FLAG2_UNSET', Char(15), 32768),
	Insn('CHAR_SET_CHCP', Char(15), 39),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('CHAR_FLAG1_UNSET', Char(16), 128),
	Insn('CHAR_FLAG2_UNSET', Char(16), 32768),
	Insn('CHAR_SET_CHCP', Char(16), 40),
	Insn('CHAR_SET_FRAME', Char(16), 0),
	Insn('CHAR_FLAG1_UNSET', Char(17), 128),
	Insn('CHAR_FLAG2_UNSET', Char(17), 32768),
	Insn('CHAR_SET_CHCP', Char(17), 41),
	Insn('CHAR_SET_FRAME', Char(17), 0),
	Insn('CHAR_FLAG1_UNSET', Char(18), 128),
	Insn('CHAR_FLAG2_UNSET', Char(18), 32768),
	Insn('CHAR_SET_CHCP', Char(18), 42),
	Insn('CHAR_SET_FRAME', Char(18), 0),
	Insn('CHAR_FLAG1_UNSET', Char(19), 128),
	Insn('CHAR_FLAG2_UNSET', Char(19), 32768),
	Insn('CHAR_SET_CHCP', Char(19), 43),
	Insn('CHAR_SET_FRAME', Char(19), 0),
	Insn('CHAR_SET_POS', Char(257), (9700, 0, 1350), 270),
	Insn('CHAR_SET_POS', Char(258), (9700, 0, 2950), 270),
	Insn('CHAR_SET_POS', Char(259), (11200, 0, 1350), 270),
	Insn('CHAR_SET_POS', Char(260), (11200, 0, 2950), 270),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(11), (16000, 600, 5380), 180),
	Insn('CHAR_SET_POS', Char(12), (16000, 600, 5380), 180),
	Insn('CHAR_SET_POS', Char(13), (16000, 600, 5380), 180),
	Insn('CHAR_SET_POS', Char(14), (16000, 600, 5380), 180),
	Insn('CHAR_SET_POS', Char(15), (16000, 600, 5380), 180),
	Insn('CHAR_SET_POS', Char(16), (16000, 600, 5380), 180),
	Insn('CHAR_SET_POS', Char(17), (16000, 600, 5380), 180),
	Insn('CHAR_SET_POS', Char(18), (16000, 600, 5380), 180),
	Insn('CHAR_SET_POS', Char(19), (16000, 600, 5380), 180),
	Insn('CHAR_SET_COLOR', Char(11), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(12), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(13), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(14), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(15), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(16), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(17), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(18), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(19), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('OBJ_FLAG_UNSET', Object(0), 4),
	Insn('0x78', b'\x00', Char(10)),
	Insn('OBJ_SET_FRAME', Object(0), 'light', Insn('0', 1)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(10), (16000, 0, 6000), 0),
	Insn('0xD3', Char(10), 0, 270000, 0, 0),
	Insn('OBJ_FLAG_SET', Object(0), 4096),
	Insn('0x74', Object(0), 7680),
	Insn('0x70', Object(0), b'\x1e\x00'),
	Insn('OBJ_FLAG_SET', Object(7), 4),
	Insn('OBJ_FLAG_SET', Object(8), 4),
	Insn('CAM_OFFSET', (16230, 600, 5720), 0),
	Insn('CAM_ROTATE', 29, 23, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 28500, 0),
	Insn('CAM_DISTANCE', 26000, 12000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 27, Insn('TASK_GET', 14))), Insn('END')]), [
			Insn('CALL', Function((0, 36))),
			Insn('QUEST', 27, Insn('TASK_SET', 20)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 27, Insn('TASK_GET', 15))), Insn('END')]), [
			Insn('CALL', Function((0, 32))),
			Insn('QUEST', 27, Insn('TASK_SET', 19)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 27, Insn('TASK_GET', 16))), Insn('END')]), [
			Insn('CALL', Function((0, 33))),
			Insn('QUEST', 27, Insn('TASK_SET', 20)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 27, Insn('TASK_GET', 17))), Insn('END')]), [
			Insn('CALL', Function((0, 35))),
			Insn('QUEST', 27, Insn('TASK_SET', 20)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 27, Insn('TASK_GET', 18))), Insn('END')]), [
			Insn('CALL', Function((0, 34))),
			Insn('QUEST', 27, Insn('TASK_SET', 20)),
		]),
		(None, []),
	]),
	Insn('SLEEP', 1500),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 128),
	Insn('CHAR_FLAG2_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(15), 128),
	Insn('CHAR_FLAG2_SET', Char(15), 32768),
	Insn('CHAR_FLAG1_SET', Char(16), 128),
	Insn('CHAR_FLAG2_SET', Char(16), 32768),
	Insn('CHAR_FLAG1_SET', Char(17), 128),
	Insn('CHAR_FLAG2_SET', Char(17), 32768),
	Insn('CHAR_FLAG1_SET', Char(18), 128),
	Insn('CHAR_FLAG2_SET', Char(18), 32768),
	Insn('CHAR_FLAG1_SET', Char(19), 128),
	Insn('CHAR_FLAG2_SET', Char(19), 32768),
	Insn('0x49'),
	Insn('0xD5', 35),
	Insn('0xD5', 36),
	Insn('0xD5', 37),
	Insn('0xD5', 38),
	Insn('0xD5', 39),
	Insn('0xD5', 40),
	Insn('0xD5', 41),
	Insn('0xD5', 42),
	Insn('0xD5', 43),
	Insn('FLAG_SET', Flag(737)),
	Insn('NEW_SCENE', 'c100c', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][32] = [
	Insn('FORK_FUNC', Char(19), 3, Function((0, 38))),
	Insn('SLEEP', 750),
	Insn('FORK_FUNC', Char(18), 3, Function((0, 37))),
	Insn('SLEEP', 4000),
	Insn('FORK_FUNC', Char(13), 3, Function((0, 41))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(16), 3, Function((0, 39))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(17), 3, Function((0, 40))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(14), 3, Function((0, 41))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(15), 3, Function((0, 42))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(11), 3, Function((0, 41))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(12), 3, Function((0, 43))),
	Insn('SLEEP', 2500),
	Insn('0x6F', b'\x10'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (2130, 1200, 2100), 0),
	Insn('CAM_ROTATE', 317, 22, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 19910, 0),
	Insn('0x0D'),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('FORK_AWAIT', Char(12), 3),
	Insn('TEXT_TALK', Char(257), Text(
		'#1P#0001F……请您\n'
		'稍等一下好吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(12), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 12, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 44))),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 45))),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 46))),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 47))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P哎呀哎呀，这不是刚才\n'
		'在国境门那边聊过天的孩子们嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P找我有什么事吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F抱歉，还没做自我介绍……{wait}'
		'{page}'
		'#0001F我们是\n'
		'克洛斯贝尔警察局丄特务\n'
		'支援课的成员。{wait}'
		'{page}'
		'老婆婆，麻烦您……\n'
		'跟我们走一趟吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P……哎，怎、怎么会……\n'
		'我做了什么啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P再、再怎么说，\n'
		'这也太过分了……\n'
		'让我这样身体虚弱的老人家……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F……今日，根据警察局的情报来源，\n'
		'我们得知了这样一条消息。{wait}'
		'{page}'
		'某个犯罪集团\n'
		'企图潜入\n'
		'克洛斯贝尔……{wait}'
		'{page}'
		'#0001F我们接到任务，\n'
		'其内容是赶往唐古拉姆门盯梢，\n'
		'观察众游客。{wait}'
		'{page}'
		'而其中有个人\n'
		'说出了明显很可疑的话……\n'
		'没错，那就是您。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P什、什么意思……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0001F老婆婆，您在\n'
		'唐古拉姆门的食堂\n'
		'说了很奇怪的话。{wait}'
		'{page}'
		'#0003F『三年没来克洛斯贝尔了』……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P……那、那有什么问题？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P住在共和国那么远的地方，\n'
		'三年没来也\n'
		'没什么好奇怪的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F……问题还在后面。{wait}'
		'{page}'
		'#0001F『之前来的时候，带孙子去\n'
		'\u3000米修拉姆的主题乐园玩过』……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0104F……原、原来是这样。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0300F原来如此，我明白了。\n'
		'这话的确是充满疑点呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0200F您自掘坟墓了呢，老婆婆。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P哎？呃，那个……\n'
		'我不太懂你们的意思……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F很简单。{wait}'
		'{page}'
		'您说自己最后一次到访\n'
		'克洛斯贝尔是在三年前……{wait}'
		'{page}'
		'#0001F但游憩区米修拉姆的\n'
		'主题乐园在那时\n'
		'还没有建成呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P……哎！？\n'
		'这、这不可能……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P……不……\n'
		'呃，那是，那个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P……对，是我弄错了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P呵呵，我可真是的，\n'
		'把在别处看到的主题乐园的报道\n'
		'错当成了自己的回忆……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F原来如此……是弄错了吗。{wait}'
		'{page}'
		'#0000F那么……\n'
		'能麻烦您把令郎夫妇\n'
		'叫来吗？{wait}'
		'{page}'
		'只要联系警察的话，\n'
		'应该马上就能把他们找来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P……！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F……办不到吧，\n'
		'因为那些人物根本就不存在。{wait}'
		'{page}'
		'#0003F真是不可思议。\n'
		'在不存在的主题乐园里，\n'
		'和不存在的孙子游玩……{wait}'
		'{page}'
		'您并不是三年没来，\n'
		'而正是因为定期到访克洛斯贝尔，\n'
		'所以才会弄错的吧。{wait}'
		'{page}'
		'#0001F没错，正是为了非法行商，\n'
		'定期到访克洛斯贝尔，所以才会如此。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P我、我、我……\n'
		'我不知道你在说什么！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P什么贩卖假冒的名牌商品……\n'
		'那种过分的事我才不会……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0101F……老婆婆，我们\n'
		'的确是在追查\n'
		'假货商……{wait}'
		'{page}'
		'但是这件事好像\n'
		'一次也没对您说过啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(12), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P啊、啊、啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0309F哈哈，这么老套的陷阱\n'
		'也能让您上钩啊，老婆婆。{wait}'
		'{page}'
		'#0300F该到算总帐的时候啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0200F您为什么会说出\n'
		'本不可能知道的信息……{wait}'
		'{page}'
		'请到警察局总部\n'
		'的笔录室中慢慢解释吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P…………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F（这样就解决了吧……）{wait}'
		'{page}'
		'#0001F……老婆婆，\n'
		'我再说一遍，\n'
		'请跟我们到警察局总部走一趟……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P#200W……谁#200W……………………\n'
		'………#200W……………谁……{wait}'
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
	Insn('0x82', 0, 100, 3000, 200),
	Insn('TEXT_TALK2', Char(12), Translate('假货商'), Text(
		'#5P#5S……谁要跟你们走啊，\n'
		'这群臭小鬼！！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0011F哎！！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0105F呀！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0305F怎、怎么回事……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0200F……原形毕露了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x82', 0, 100, 3000, 200),
	Insn('TEXT_TALK2', Char(12), Translate('假货商'), Text(
		'#5P#5S竟敢搞这种引人上钩的\n'
		'骗子把戏！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x82', 0, 100, 3000, 200),
	Insn('TEXT_TALK2', Char(12), Translate('假货商'), Text(
		'#5P#5S你们做这种缺德事，\n'
		'总有一天会遭到女神的天谴啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0203F……竟然说出这种\n'
		'恬不知耻的话。{wait}'
		'{page}'
		'#0201F做着骗人买卖的\n'
		'不正是您吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x82', 0, 100, 3000, 200),
	Insn('TEXT_TALK2', Char(12), Translate('假货商'), Text(
		'#5P#5S吵死了，你这个矮冬瓜！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0205F矮……矮冬瓜……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x82', 0, 100, 3000, 200),
	Insn('TEXT_TALK2', Char(12), Translate('假货商'), Text(
		'#5P#5S啊啊～讨厌讨厌！所以说\n'
		'我最讨厌警察、游击士这群人了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x82', 0, 100, 3000, 200),
	Insn('TEXT_TALK2', Char(12), Translate('假货商'), Text(
		'#5P#5S你们以为自己永远\n'
		'都是正确的吗，呆瓜们！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0011F总、总而言之，请您先镇定一点！\n'
		'只要老老实实跟我们走……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x82', 0, 100, 3000, 200),
	Insn('TEXT_TALK2', Char(12), Translate('假货商'), Text(
		'#5P#5S闭嘴，小子！\n'
		'我都说过不去了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x82', 0, 100, 3000, 200),
	Insn('TEXT_TALK2', Char(12), Translate('假货商'), Text(
		'#5P#5S同样的话，\n'
		'不要让我重复很多遍！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0006F（同样的话，\n'
		'\u3000也不要让我重复很多遍啊……！）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(12), Translate('假货商'), Text(
		'#5P要是你有本事\n'
		'抓到我的话……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 2000),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('FORK', 12, 1, [
		Insn('0x98', Char(254), (-500, 0, -500), 2000, 0),
	]),
	Insn('SLEEP', 1000),
	Insn('FORK', 12, 1, [
		Insn('0x98', Char(254), (-500, 0, 500), 2000, 0),
	]),
	Insn('SLEEP', 1000),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'\x91\x01\x00'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 401), Insn('SET'), Insn('END')])),
	Insn('CAM_DISTANCE', 21000, 3000),
	Insn('FORK', 12, 1, [
		Insn('0x95', Char(254), (-22570, 0, 2200), 10000, 0),
	]),
	Insn('SOUND_PLAY', 250, 0, 0, 80),
	Insn('0x82', 0, 100, 3000, 200),
	Insn('TEXT_SET_POS', -50, 20, -1, -1),
	Insn('TEXT_SET_NAME', Translate('假货商')),
	Insn('TEXT_MESSAGE', Char(12), Text(
		'#5P#5S就来抓抓看啊！！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FORK_AWAIT', Char(12), 1),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(259)),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F……不、不是吧……\n'
		'这是什么速度啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0306F我说～之前那副\n'
		'慈祥优雅的老婆婆的面具\n'
		'都扔到哪里去了啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0206F矮冬瓜……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0103F好、好啦！你们还有空发呆！？{wait}'
		'{page}'
		'#0101F再不赶快追上去……\n'
		'就真要被她逃掉了啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0001F说、说得对啊……\n'
		'赶快追吧，各位！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 48))),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 48))),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 48))),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 48))),
	Insn('RETURN'),
]

data['code'][33] = [
	Insn('FORK_FUNC', Char(19), 3, Function((0, 38))),
	Insn('SLEEP', 750),
	Insn('FORK_FUNC', Char(18), 3, Function((0, 37))),
	Insn('SLEEP', 4000),
	Insn('FORK_FUNC', Char(13), 3, Function((0, 41))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(16), 3, Function((0, 39))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(17), 3, Function((0, 40))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(14), 3, Function((0, 41))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(15), 3, Function((0, 42))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(12), 3, Function((0, 41))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(11), 3, Function((0, 43))),
	Insn('SLEEP', 2500),
	Insn('0x6F', b'\x10'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (2130, 1200, 2100), 0),
	Insn('CAM_ROTATE', 317, 22, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 19910, 0),
	Insn('0x0D'),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('FORK_AWAIT', Char(11), 3),
	Insn('TEXT_TALK', Char(257), Text(
		'#1P#0001F……请您\n'
		'稍等一下好吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(11), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 11, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 44))),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 45))),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 46))),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 47))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3405F哎呀……找我有什么事吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F抱歉，还没做自我介绍……{wait}'
		'{page}'
		'我们是\n'
		'克洛斯贝尔警察局丄特务\n'
		'支援课的成员。{wait}'
		'{page}'
		'麻烦您……\n'
		'跟我们走一趟吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F……唔。{wait}'
		'{page}'
		'刚才你们在巴士里说\n'
		'假货贩子什么的……{wait}'
		'{page}'
		'#3400F莫非以为是我吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F……哎？{wait}'
		'{page}'
		'（听、听到了吗……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F……着眼点倒是不错。{wait}'
		'{page}'
		'我没有对你们\n'
		'透露任何有关自身的详情……\n'
		'这的确可以作为怀疑的理由。{wait}'
		'{page}'
		'#3401F但是……应该还有条\n'
		'更重要，而且更明显的线索，\n'
		'而你们却没有发现。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F明显的线索……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F我在食堂听到了\n'
		'你们和乘客们的对话……\n'
		'其中有个不自然的地方。{wait}'
		'{page}'
		'#3401F那就是……那位看似慈祥的\n'
		'老婆婆所说的话。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0105F快要见到阔别三年的孙子，\n'
		'看起来非常开心的……\n'
		'那位老婆婆吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F到底从何说起……？\n'
		'那个人说的话里，没有什么可疑的地方啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F仔细想想她说过的话。{wait}'
		'{page}'
		'『三年没来克洛斯贝尔了』……{wait}'
		'{page}'
		'以及……\n'
		'『之前来的时候，带孙子去米修拉姆的\n'
		'\u3000主题乐园玩过』这两句话。{wait}'
		'{page}'
		'#3402F如果你们是克洛斯贝尔的居民，\n'
		'应该能发现其中的明显矛盾。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F……啊……！！{wait}'
		'{page}'
		'对了，原来如此啊……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0200F……三年前的米修拉姆\n'
		'还没有主题乐园。{wait}'
		'{page}'
		'她回忆中的地方\n'
		'根本就不存在……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0301F……这么说，在场众人中，\n'
		'说话最可疑的就是\n'
		'那位老婆婆吗。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0106F这么明显的破绽，\n'
		'我们竟然没有注意到……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3400F被她戴着的那副\n'
		'『慈祥老婆婆』的面具\n'
		'彻底欺骗了吧。{wait}'
		'{page}'
		'她不是三年没来，\n'
		'而正是因为定期到访克洛斯贝尔，\n'
		'所以才会犯下这种失误……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F身为假货贩子，\n'
		'定期到访克洛斯贝尔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 315, 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F……那、那位老婆婆呢！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0200F她现在恐怕已经到东侧大道了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0301F不赶快追上去的话，可能会跟丢啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0101F罗、罗伊德！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0001F啊……我明白！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0006F真、真是太对不起您了！\n'
		'还有……非常感谢！{wait}'
		'{page}'
		'#0001F稍后我们会再次向您谢罪的，\n'
		'所以现在就先……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F没关系的。{wait}'
		'{page}'
		'你们现在可没有\n'
		'慢慢道歉的空闲吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F啊……是！{wait}'
		'{page}'
		'#0001F快追，各位！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 21000, 3000),
	Insn('FORK', 11, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 100),
	]),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 49))),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 49))),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 49))),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 49))),
	Insn('RETURN'),
]

data['code'][34] = [
	Insn('FORK_FUNC', Char(19), 3, Function((0, 38))),
	Insn('SLEEP', 750),
	Insn('FORK_FUNC', Char(18), 3, Function((0, 37))),
	Insn('SLEEP', 4000),
	Insn('FORK_FUNC', Char(13), 3, Function((0, 41))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(16), 3, Function((0, 39))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(17), 3, Function((0, 40))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(15), 3, Function((0, 41))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(12), 3, Function((0, 42))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(11), 3, Function((0, 41))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(14), 3, Function((0, 43))),
	Insn('SLEEP', 2500),
	Insn('0x6F', b'\x10'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (2130, 1200, 2100), 0),
	Insn('CAM_ROTATE', 317, 22, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 19910, 0),
	Insn('0x0D'),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('FORK_AWAIT', Char(14), 3),
	Insn('TEXT_TALK', Char(257), Text(
		'#1P#0001F……请您\n'
		'稍等一下好吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(14), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 14, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 44))),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 45))),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 46))),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 47))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P哎呀，这不是刚才在\n'
		'唐古拉姆门见过的几位嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P找我有什么事吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0001F抱歉，还没做自我介绍……{wait}'
		'{page}'
		'我们是\n'
		'克洛斯贝尔警察局丄特务\n'
		'支援课的成员。{wait}'
		'{page}'
		'麻烦您……\n'
		'跟我们走一趟吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P……警、警察！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P我、我到底做了什么……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F……现在就告诉您我们的推理。{wait}'
		'{page}'
		'#0001F您听好，首先……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -50, 20, -1, -1),
	Insn('TEXT_SET_NAME', Translate('女性的声音')),
	Insn('TEXT_MESSAGE', Char(11), Text(
		'#1P──没有那个必要。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F哎……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_SET_POS', Char(11), (-10500, 0, 2200), 90),
	Insn('FORK', 11, 1, [
		Insn('0x95', Char(254), (-800, 0, 2200), 2000, 0),
	]),
	Insn('FORK', 14, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(14), 1),
	Insn('SLEEP', 3800),
	Insn('FORK', 14, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK', 14, 2, [
		Insn('0x98', Char(254), (0, 0, 1500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F您、您是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0305F黑发的姐姐！？\n'
		'你不是已经进城了吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3404F嗯，是啊。{wait}'
		'{page}'
		'#3400F不过，看到你们叫住\n'
		'这个人，就掉头回来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0205F这是怎么回事？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3401F我就直截了当地说吧。{wait}'
		'{page}'
		'刚才你们在巴士里说\n'
		'假货贩子什么的……{wait}'
		'{page}'
		'#3403F犯人并不是这个人。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F……哎？{wait}'
		'{page}'
		'您……您说什么……！？{wait}'
		'{page}'
		'（话说，巴士里的对话\n'
		'\u3000都被她听到了吗……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F……着眼点倒是不错。{wait}'
		'{page}'
		'他的职业是贸易商……\n'
		'很容易和假货贩子\n'
		'这个词联系起来。{wait}'
		'{page}'
		'#3401F但是……应该还有条\n'
		'更重要，而且更明显的线索，\n'
		'而你们却没有发现。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F明显的线索……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F我在食堂听到了\n'
		'你们和乘客们的对话……\n'
		'其中有个不自然的地方。{wait}'
		'{page}'
		'#3401F那就是……那位看似慈祥的\n'
		'老婆婆所说的话。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0105F快要见到阔别三年的孙子，\n'
		'看起来非常开心的……\n'
		'那位老婆婆吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F到底从何说起……？\n'
		'那个人说的话里，没有什么可疑的地方啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F仔细想想她说过的话。{wait}'
		'{page}'
		'『三年没来克洛斯贝尔了』……{wait}'
		'{page}'
		'以及……\n'
		'『之前来的时候，带孙子去米修拉姆的\n'
		'\u3000主题乐园玩过』这两句话。{wait}'
		'{page}'
		'#3402F如果你们是克洛斯贝尔的居民，\n'
		'应该能发现其中的明显矛盾。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F……啊……！！{wait}'
		'{page}'
		'对了，原来如此啊……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0200F……三年前的米修拉姆\n'
		'还没有主题乐园。{wait}'
		'{page}'
		'她回忆中的地方\n'
		'根本就不存在……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0301F……这么说，在场众人中，\n'
		'说话最可疑的就是\n'
		'那位老婆婆吗。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0106F这么明显的破绽，\n'
		'我们竟然没有注意到……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3400F被她戴着的那副\n'
		'『慈祥老婆婆』的面具\n'
		'彻底欺骗了吧。{wait}'
		'{page}'
		'她不是三年没来，\n'
		'而正是因为定期到访克洛斯贝尔，\n'
		'所以才会犯下这种失误……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F身为假货贩子，\n'
		'定期到访克洛斯贝尔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 315, 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F……那、那位老婆婆呢！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0200F她现在恐怕已经到东侧大道了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0301F不赶快追上去的话，可能会跟丢啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0101F罗、罗伊德！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0001F啊……我明白！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0006F真、真是太对不起您了！\n'
		'我们太失礼了……{wait}'
		'{page}'
		'稍后我们会再次向您谢罪的，\n'
		'所以现在就先……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 14, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK_AWAIT', Char(14), 1),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P哦，哦。\n'
		'我是完全一头雾水啦……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F……你们现在可没有\n'
		'慢慢道歉的空闲吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F啊……是！{wait}'
		'{page}'
		'#0001F快追，各位！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 21000, 3000),
	Insn('FORK', 11, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 100),
	]),
	Insn('FORK', 14, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 100),
	]),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 49))),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 49))),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 49))),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 49))),
	Insn('RETURN'),
]

data['code'][35] = [
	Insn('FORK_FUNC', Char(19), 3, Function((0, 38))),
	Insn('SLEEP', 750),
	Insn('FORK_FUNC', Char(18), 3, Function((0, 37))),
	Insn('SLEEP', 4000),
	Insn('FORK_FUNC', Char(13), 3, Function((0, 41))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(16), 3, Function((0, 39))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(17), 3, Function((0, 40))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(14), 3, Function((0, 41))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(12), 3, Function((0, 42))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(11), 3, Function((0, 41))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(15), 3, Function((0, 43))),
	Insn('SLEEP', 2500),
	Insn('0x6F', b'\x10'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (2130, 1200, 2100), 0),
	Insn('CAM_ROTATE', 317, 22, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 19910, 0),
	Insn('0x0D'),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('FORK_AWAIT', Char(15), 3),
	Insn('TEXT_TALK', Char(257), Text(
		'#1P#0001F……请您\n'
		'稍等一下好吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(15), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 15, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 44))),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 45))),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 46))),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 47))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P哎呀……是刚才的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P找我有什么事吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0001F抱歉，还没做自我介绍……{wait}'
		'{page}'
		'我们是\n'
		'克洛斯贝尔警察局丄特务\n'
		'支援课的成员。{wait}'
		'{page}'
		'麻烦您……\n'
		'跟我们走一趟吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P……啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P我到底做了什么啊？\n'
		'梦话也要等睡着了以后再说吧！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F……现在就告诉您我们的推理。{wait}'
		'{page}'
		'#0001F您听好，首先……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -50, 20, -1, -1),
	Insn('TEXT_SET_NAME', Translate('女性的声音')),
	Insn('TEXT_MESSAGE', Char(11), Text(
		'#1P──没有那个必要。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F哎……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_SET_POS', Char(11), (-10500, 0, 2200), 90),
	Insn('FORK', 11, 1, [
		Insn('0x95', Char(254), (-800, 0, 2200), 2000, 0),
	]),
	Insn('FORK', 15, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(15), 1),
	Insn('SLEEP', 3800),
	Insn('FORK', 15, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK', 15, 2, [
		Insn('0x98', Char(254), (0, 0, 1500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F您、您是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0305F黑发的姐姐！？\n'
		'你不是已经进城了吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3404F嗯，是啊。{wait}'
		'{page}'
		'#3400F不过，看到你们叫住\n'
		'这个人，就掉头回来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0205F这是怎么回事？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3401F我就直截了当地说吧。{wait}'
		'{page}'
		'刚才你们在巴士里说\n'
		'假货贩子什么的……{wait}'
		'{page}'
		'#3403F犯人并不是这个人。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F……哎？{wait}'
		'{page}'
		'您……您说什么……！？{wait}'
		'{page}'
		'（话说，巴士里的对话\n'
		'\u3000都被她听到了吗……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F……着眼点倒是不错。{wait}'
		'{page}'
		'她说我很可疑，可以将这种做法当成\n'
		'是在试图将你们的注意力转向他人……\n'
		'你们大概是这样想的吧。{wait}'
		'{page}'
		'#3401F但是……应该还有条\n'
		'更重要，而且更明显的线索，\n'
		'而你们却没有发现。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F明显的线索……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F我在食堂听到了\n'
		'你们和乘客们的对话……\n'
		'其中有个不自然的地方。{wait}'
		'{page}'
		'#3401F那就是……那位看似慈祥的\n'
		'老婆婆所说的话。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0105F快要见到阔别三年的孙子，\n'
		'看起来非常开心的……\n'
		'那位老婆婆吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F到底从何说起……？\n'
		'那个人说的话里，没有什么可疑的地方啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F仔细想想她说过的话。{wait}'
		'{page}'
		'『三年没来克洛斯贝尔了』……{wait}'
		'{page}'
		'以及……\n'
		'『之前来的时候，带孙子去米修拉姆的\n'
		'\u3000主题乐园玩过』这两句话。{wait}'
		'{page}'
		'#3402F如果你们是克洛斯贝尔的居民，\n'
		'应该能发现其中的明显矛盾。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F……啊……！！{wait}'
		'{page}'
		'对了，原来如此啊……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0200F……三年前的米修拉姆\n'
		'还没有主题乐园。{wait}'
		'{page}'
		'她回忆中的地方\n'
		'根本就不存在……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0301F……这么说，在场众人中，\n'
		'说话最可疑的就是\n'
		'那位老婆婆吗。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0106F这么明显的破绽，\n'
		'我们竟然没有注意到……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3400F被她戴着的那副\n'
		'『慈祥老婆婆』的面具\n'
		'彻底欺骗了吧。{wait}'
		'{page}'
		'她不是三年没来，\n'
		'而正是因为定期到访克洛斯贝尔，\n'
		'所以才会犯下这种失误……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F身为假货贩子，\n'
		'定期到访克洛斯贝尔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 315, 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F……那、那位老婆婆呢！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0200F她现在恐怕已经到东侧大道了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0301F不赶快追上去的话，可能会跟丢啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0101F罗、罗伊德！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0001F啊……我明白！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0006F真、真是太对不起您了！\n'
		'我们太失礼了……{wait}'
		'{page}'
		'稍后我们会再次向您谢罪的，\n'
		'所以现在就先……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 15, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK_AWAIT', Char(15), 1),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P就、就是嘛！\n'
		'太无礼了，真是的……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F……你们现在可没有\n'
		'慢慢道歉的空闲吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F啊……是！{wait}'
		'{page}'
		'#0001F快追，各位！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 21000, 3000),
	Insn('FORK', 11, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 100),
	]),
	Insn('FORK', 15, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 100),
	]),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 49))),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 49))),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 49))),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 49))),
	Insn('RETURN'),
]

data['code'][36] = [
	Insn('FORK_FUNC', Char(19), 3, Function((0, 38))),
	Insn('SLEEP', 750),
	Insn('FORK_FUNC', Char(18), 3, Function((0, 37))),
	Insn('SLEEP', 4000),
	Insn('FORK_FUNC', Char(15), 3, Function((0, 41))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(16), 3, Function((0, 39))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(17), 3, Function((0, 40))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(14), 3, Function((0, 41))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(12), 3, Function((0, 42))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(11), 3, Function((0, 41))),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(13), 3, Function((0, 43))),
	Insn('SLEEP', 2500),
	Insn('0x6F', b'\x10'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (2130, 1200, 2100), 0),
	Insn('CAM_ROTATE', 317, 22, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 19910, 0),
	Insn('0x0D'),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('FORK_AWAIT', Char(13), 3),
	Insn('TEXT_TALK', Char(257), Text(
		'#1P#0001F……请您\n'
		'稍等一下好吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(13), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 13, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 44))),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 45))),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 46))),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 47))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(13), Text(
		'#5P…………怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#5P又打算\n'
		'耍弄我吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0001F抱歉，还没做自我介绍……{wait}'
		'{page}'
		'我们是\n'
		'克洛斯贝尔警察局丄特务\n'
		'支援课的成员。{wait}'
		'{page}'
		'麻烦您……\n'
		'跟我们走一趟吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#5P……什、什、什么……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#5P别、别把我当傻瓜！\n'
		'竟然开这种恶劣的玩笑……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F……现在就告诉您我们的推理。{wait}'
		'{page}'
		'#0001F您听好，首先……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -50, 20, -1, -1),
	Insn('TEXT_SET_NAME', Translate('女性的声音')),
	Insn('TEXT_MESSAGE', Char(11), Text(
		'#1P──没有那个必要。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F哎……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_SET_POS', Char(11), (-10500, 0, 2200), 90),
	Insn('FORK', 11, 1, [
		Insn('0x95', Char(254), (-800, 0, 2200), 2000, 0),
	]),
	Insn('FORK', 13, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(13), 1),
	Insn('SLEEP', 3800),
	Insn('FORK', 13, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK', 13, 2, [
		Insn('0x98', Char(254), (0, 0, 1500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F您、您是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0305F黑发的姐姐！？\n'
		'你不是已经进城了吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3404F嗯，是啊。{wait}'
		'{page}'
		'#3400F不过，看到你们叫住\n'
		'这个人，就掉头回来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0205F这是怎么回事？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3401F我就直截了当地说吧。{wait}'
		'{page}'
		'刚才你们在巴士里说\n'
		'假货贩子什么的……{wait}'
		'{page}'
		'#3403F犯人并不是这个人。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F……哎？{wait}'
		'{page}'
		'您……您说什么……！？{wait}'
		'{page}'
		'（话说，巴士里的对话\n'
		'\u3000都被她听到了吗……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F……着眼点倒是不错。{wait}'
		'{page}'
		'因为不太爱和别人说话，\n'
		'所以他的性格很可疑……\n'
		'你们是这样想的吧。{wait}'
		'{page}'
		'#3401F但是……应该还有条\n'
		'更重要，而且更明显的线索，\n'
		'而你们却没有发现。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F明显的线索……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F我在食堂听到了\n'
		'你们和乘客们的对话……\n'
		'其中有个不自然的地方。{wait}'
		'{page}'
		'#3401F那就是……那位看似慈祥的\n'
		'老婆婆所说的话。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0105F快要见到阔别三年的孙子，\n'
		'看起来非常开心的……\n'
		'那位老婆婆吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F到底从何说起……？\n'
		'那个人说的话里，没有什么可疑的地方啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F仔细想想她说过的话。{wait}'
		'{page}'
		'『三年没来克洛斯贝尔了』……{wait}'
		'{page}'
		'以及……\n'
		'『之前来的时候，带孙子去米修拉姆的\n'
		'\u3000主题乐园玩过』这两句话。{wait}'
		'{page}'
		'#3402F如果你们是克洛斯贝尔的居民，\n'
		'应该能发现其中的明显矛盾。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F……啊……！！{wait}'
		'{page}'
		'对了，原来如此啊……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0200F……三年前的米修拉姆\n'
		'还没有主题乐园。{wait}'
		'{page}'
		'她回忆中的地方\n'
		'根本就不存在……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0301F……这么说，在场众人中，\n'
		'说话最可疑的就是\n'
		'那位老婆婆吗。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0106F这么明显的破绽，\n'
		'我们竟然没有注意到……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3400F被她戴着的那副\n'
		'『慈祥老婆婆』的面具\n'
		'彻底欺骗了吧。{wait}'
		'{page}'
		'她不是三年没来，\n'
		'而正是因为定期到访克洛斯贝尔，\n'
		'所以才会犯下这种失误……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F身为假货贩子，\n'
		'定期到访克洛斯贝尔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 315, 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F……那、那位老婆婆呢！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0200F她现在恐怕已经到东侧大道了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0301F不赶快追上去的话，可能会跟丢啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0101F罗、罗伊德！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0001F啊……我明白！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0006F真、真是太对不起您了！\n'
		'我们太失礼了……{wait}'
		'{page}'
		'稍后我们会再次向您谢罪的，\n'
		'所以现在就先……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 13, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK_AWAIT', Char(13), 1),
	Insn('TEXT_TALK', Char(13), Text(
		'不、不可原谅，不可原谅啊……！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#5P#3403F……你们现在可没有\n'
		'慢慢道歉的空闲吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F啊……是！{wait}'
		'{page}'
		'#0001F快追，各位！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 21000, 3000),
	Insn('FORK', 11, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 100),
	]),
	Insn('FORK', 13, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 100),
	]),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 49))),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 49))),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 49))),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 49))),
	Insn('RETURN'),
]

data['code'][37] = [
	Insn('SLEEP', 1200),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (16000, 0, 2700), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('EMOTE', Char(254), 0, 2000, (38, 39, 250, 2)),
	Insn('SLEEP', 1000),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-12000, 0, 1200), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('CHAR_FLAG1_SET', Char(254), 128),
	Insn('RETURN'),
]

data['code'][38] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (16000, 0, 1200), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('EMOTE', Char(254), 0, 2000, (38, 39, 250, 2)),
	Insn('SLEEP', 2250),
	Insn('FORK', 254, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-12000, 0, 2700), 4000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('CHAR_FLAG1_SET', Char(254), 128),
	Insn('RETURN'),
]

data['code'][39] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (16000, 0, 1200), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-12000, 0, 1200), 2000, 0),
	]),
	Insn('EMOTE', Char(254), 0, 2000, (38, 39, 250, 2)),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(254), 0, 2000, (38, 39, 250, 2)),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(254), 0, 2000, (38, 39, 250, 2)),
	Insn('SLEEP', 1000),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('CHAR_FLAG1_SET', Char(254), 128),
	Insn('RETURN'),
]

data['code'][40] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (16000, 0, 2700), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-12000, 0, 2700), 2000, 0),
	]),
	Insn('EMOTE', Char(254), 0, 2000, (38, 39, 250, 2)),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(254), 0, 2000, (38, 39, 250, 2)),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(254), 0, 2000, (38, 39, 250, 2)),
	Insn('SLEEP', 1000),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('CHAR_FLAG1_SET', Char(254), 128),
	Insn('RETURN'),
]

data['code'][41] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (16000, 0, 2200), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-12000, 0, 2200), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('CHAR_FLAG1_SET', Char(254), 128),
	Insn('RETURN'),
]

data['code'][42] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (16000, 0, 2700), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-12000, 0, 2700), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('CHAR_FLAG1_SET', Char(254), 128),
	Insn('RETURN'),
]

data['code'][43] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (16000, 0, 2200), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (0, 0, 2200), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('RETURN'),
]

data['code'][44] = [
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (3000, 0, 1350), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('RETURN'),
]

data['code'][45] = [
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (3000, 0, 2950), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('RETURN'),
]

data['code'][46] = [
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (4500, 0, 1350), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('RETURN'),
]

data['code'][47] = [
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (4500, 0, 2950), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('RETURN'),
]

data['code'][48] = [
	Insn('FORK', 254, 1, [
		Insn('0x98', Char(254), (-10000, 0, 0), 4000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][49] = [
	Insn('CHAR_ROTATE', Char(254), 180, 0),
	Insn('FORK', 254, 1, [
		Insn('0x98', Char(254), (0, 0, -1800), 4000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 270, 0),
	Insn('FORK', 254, 1, [
		Insn('0x98', Char(254), (-10000, 0, 0), 4000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][50] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-10000, 0, 3000), 4000, 0),
	]),
	Insn('FORK', 254, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('RETURN'),
]

data['code'][51] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (133180, 4800, 81440), 0),
	Insn('CAM_ROTATE', 8, 31, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 17670, 0),
	Insn('0xE0', b'\x02'),
	Insn('0x09', 134217728),
	Insn('CHAR_SET_POS', Char(257), (133170, 3000, 82030), 90),
	Insn('CHAR_SET_POS', Char(258), (133230, 3000, 83640), 135),
	Insn('CHAR_SET_POS', Char(259), (132220, 3000, 81240), 45),
	Insn('CHAR_SET_POS', Char(260), (131880, 3000, 83280), 135),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(266), (131150, 3000, 81780), 90),
			Insn('CHAR_FLAG1_UNSET', Char(4), 128),
			Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
		]),
		(None, []),
	]),
	Insn('0x0D'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'获得了{item 843}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 843, 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0000F白色的花……\n'
		'是菲奈尔之花吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#11P#0100F这里离克洛斯贝尔市很近，\n'
		'自己来摘的人\n'
		'似乎也有不少哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#5P#0300F嗯，这里的话，应该\n'
		'也不会出现太强的魔兽吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#06P#0200F即使如此，对老人和孩子\n'
		'肯定也是有威胁的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0003F嗯，是啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(266), Text(
				'#6P#0603F……花都摘到了，那就快点走吧，\n'
				'没工夫磨磨蹭蹭了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0003F嗯，是啊。{wait}'
				'{page}'
				'#0000F好，那就走吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('0x65', 5, 1),
	Insn('QUEST', 46, Insn('TASK_SET', 5)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 46, Insn('TASK_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 46, Insn('TASK_GET', 4))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 46, Insn('TASK_GET', 5))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 46, Insn('TASK_SET', 6)),
		]),
		(None, []),
	]),
	Insn('0x0A', 134217728),
	Insn('0x37'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(4), 128),
			Insn('CHAR_FLAG2_SET', Char(4), 32768),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_POS', Char(0), (133170, 3000, 82030), 90),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][52] = [
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}西丄克洛斯贝尔市\n'
		'东丄阿尔摩利卡村\u3000２７４塞尔矩\n'
		'\u3000\u3000唐古拉姆门\u3000２０６塞尔矩{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]
