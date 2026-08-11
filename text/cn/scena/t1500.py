# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't1500',
	'name2': 't1500',
	'location': 77,
	'bgm': 123,
	'flags': 8192,
	'includes': [
		't1500',
		None,
		't1500_1',
		None,
		None,
		None,
	],
	'name3': 't1500',
	'labels': [
		{
			'pos': (-69.0, 0.0, -8.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('乌尔斯拉小径'),
		},
		{
			'pos': (-23.0, 0.0, 18.0),
			'unk': b'\x00\x00R\x00',
			'name': Translate(''),
		},
		{
			'pos': (-57.900001525878906, 0.0, 4.199999809265137),
			'unk': b'\x00\x00U\x00',
			'name': Translate(''),
		},
		{
			'pos': (-48.0, 0.0, 17.25),
			'unk': b'\x00\x00V\x00',
			'name': Translate(''),
		},
	],
	'chcp': [
		'chr/ch33400',
		'chr/ch22300',
		'chr/ch28600',
		'chr/ch29800',
		'chr/ch20200',
		'chr/ch00000',
		'chr/ch34002',
		'chr/ch20400',
		'chr/ch20500',
		'chr/ch09300',
		'chr/ch31700',
		'apl/ch50385',
		'chr/ch30600',
		'apl/ch50165',
		'apl/ch50169',
		'chr/ch05500',
		'chr/ch32702',
		'chr/ch07100',
		'chr/ch32302',
		'chr/ch34500',
		'chr/ch29900',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
	],
	'npcs': [
		{
			'name': Translate('警备员东尼'),
			'pos': (-47560, 0, 4000),
			'angle': 270,
			'_1': b'\x05\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 6)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('护理师艾妲'),
			'pos': (-23040, -1000, -25909),
			'angle': 0,
			'_1': b'\x01\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('工友戴森'),
			'pos': (-30000, -1000, -20299),
			'angle': 246,
			'_1': b'\x85\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((0, 8)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('米海尔'),
			'pos': (-31450, -899, -16190),
			'angle': 180,
			'_1': b'\xd5\x01\x00\x00\x06\x00\xff\xff',
			'function': Function((0, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (-25180, -1000, -26069),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((0, 10)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('女孩'),
			'pos': (-22350, 0, -1309),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('探视者'),
			'pos': (-21309, 0, 2299),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x07\x00\x00\x00',
			'function': Function((0, 12)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('探视者'),
			'pos': (-28590, 0, 2440),
			'angle': 135,
			'_1': b'\x85\x01\x00\x00\x08\x00\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('哈罗德'),
			'pos': (-52279, 0, 16629),
			'angle': 267,
			'_1': b'\x85\x01\x00\x00\t\x00\x00\x00',
			'function': Function((0, 14)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('杰德'),
			'pos': (-18430, 0, -11560),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\n\x00\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('琴兹'),
			'pos': (-16340, 0, -330),
			'angle': 45,
			'_1': b'\x85\x01\x00\x00\x0b\x00\x00\x02',
			'function': Function((0, 16)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('凯特巡警'),
			'pos': (-52270, 0, 13590),
			'angle': 305,
			'_1': b'\x85\x01\x00\x00\x0c\x00\x00\x00',
			'function': Function((0, 17)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('彼得'),
			'pos': (-21770, -1000, -26059),
			'angle': 180,
			'_1': b'\x95\x01\x00\x00\r\x00\xff\xff',
			'function': Function((0, 18)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('特级钓师罗伊德'),
			'pos': (-24059, -1000, -26069),
			'angle': 180,
			'_1': b'\x95\x01\x00\x00\x0e\x00\xff\xff',
			'function': Function((0, 19)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('玛利亚贝尔'),
			'pos': (-51279, 0, 15350),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x0f\x00\x00\x00',
			'function': Function((0, 21)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('凯瑞教授'),
			'pos': (-16829, -1000, -16360),
			'angle': 180,
			'_1': b'\xd5\x01\x00\x00\x10\x00\xff\xff',
			'function': Function((0, 20)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('约亚西姆副教授'),
			'pos': (-29469, -990, -26069),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x11\x00\x00\x00',
			'function': Function((0, 22)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客奥希尔'),
			'pos': (-21010, 150, -9489),
			'angle': 270,
			'_1': b'\x95\x01\x00\x00\x12\x00\xff\xff',
			'function': Function((0, 23)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客拉皮斯'),
			'pos': (-9789, 0, 6489),
			'angle': 90,
			'_1': b'\x81\x01\x00\x00\x13\x00\x00\x00',
			'function': Function((0, 24)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('护理师希蓉'),
			'pos': (-27200, 6000, 20219),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x14\x00\x00\x00',
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
			'name': Translate('巴士２'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\x00\x03',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('赛西儿'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('小滴'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('琪雅'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('亚里欧斯'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('罗伯特事务长'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('玛萨护理师长'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('职员'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('巴士乘客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('巴士乘客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('巴士乘客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('巴士乘客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('巴士乘客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
	],
	'monsters': [],
	'triggers': [
		{
			'pos': (-42.5, 0.0, -1.0),
			'range': 225.0,
			'transform': [
				0.3333333432674408,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.10000000149011612,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				14.166666984558105,
				-0.0,
				0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 36)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (-25.0, 0.0, -1.0),
			'range': 5625.0,
			'transform': [
				0.20000000298023224,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.03333333134651184,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				5.0,
				-0.0,
				0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 55)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (-24.0, -17.0, -2.0),
			'range': 76.5625,
			'transform': [
				0.20000000298023224,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.2857142686843872,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				4.800000190734863,
				4.857142448425293,
				0.4000000059604645,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 57)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (-42.5, 0.0, -1.0),
			'range': 225.0,
			'transform': [
				0.3333333432674408,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.10000000149011612,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				14.166666984558105,
				-0.0,
				0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 58)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (-47.5, 0.0, -1.0),
			'range': 225.0,
			'transform': [
				0.3333333432674408,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.10000000149011612,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				15.833333969116211,
				-0.0,
				0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 59)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (-47.5, 0.0, -1.0),
			'range': 225.0,
			'transform': [
				0.3333333432674408,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.10000000149011612,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				15.833333969116211,
				-0.0,
				0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x02',
			'function': Function((0, 12)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (-58000, 0, 4000),
			'range': 1500,
			'bubble_pos': (-58000, 1500, 4000),
			'_1': b'|\x00\x00',
			'function': Function((0, 32)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-35100, 3000, 17000),
			'range': 2000,
			'bubble_pos': (-35100, 4000, 17000),
			'_1': b'|\x00\x00',
			'function': Function((0, 33)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-36600, 3000, 25600),
			'range': 2000,
			'bubble_pos': (-36600, 4000, 25600),
			'_1': b'|\x00\x00',
			'function': Function((0, 34)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-42000, 3000, 20600),
			'range': 2000,
			'bubble_pos': (-42000, 4000, 20600),
			'_1': b'|\x00\x00',
			'function': Function((0, 35)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-16830, -1000, -27510),
			'range': 1200,
			'bubble_pos': (-17180, -2000, -32770),
			'_1': b'|\x00\x00',
			'function': Function((0, 31)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-7880, 0, 6560),
			'range': 1200,
			'bubble_pos': (-7880, 1500, 6560),
			'_1': b'|\x00\x00',
			'function': Function((0, 65)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-36860, 0, 14360),
			'range': 1200,
			'bubble_pos': (-36860, 1500, 14360),
			'_1': b'|\x00\x00',
			'function': Function((0, 66)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-49630, 0, 17190),
			'range': 1200,
			'bubble_pos': (-49630, 2000, 17190),
			'_1': b'|\x00\x00',
			'function': Function((0, 30)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-35100, 3000, 17000),
			'range': 2000,
			'bubble_pos': (-35100, 4000, 17000),
			'_1': b'|\x00\x00',
			'function': Function((0, 63)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00M\x00', Function((0, 4)), Function((0, 5))),
	'code': [None]*67,
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
		Insn('0x95', Char(254), (-23040, 0, -6950), 2000, 0),
		Insn('0x95', Char(254), (-24930, 0, -6950), 2000, 0),
		Insn('0x95', Char(254), (-24930, -1000, -23250), 2000, 0),
		Insn('0x95', Char(254), (-23040, -1000, -23250), 2000, 0),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (-20450, -1830), (-13890, 1380), 1000),
		Insn('SLEEP', 400),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('CHAR_SET_POS', Char(254), (-58500, 0, 500), 4000),
	Insn('0x97', Char(254), (-30000, 0, 0), 5000, 0),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), []),
		(None, [
			Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
		]),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(8), (-24640, 0, -1950), 135),
			Insn('CHAR_SET_POS', Char(9), (-23350, 0, -3110), 315),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 0))),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_FLAG1_UNSET', Char(23), 128),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(9), 128),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
			Insn('IF', [
				(Expr([Insn('ATTR', 0), Insn('CONST', 105), Insn('EQ'), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(27), 128),
					Insn('CHAR_FLAG1_SET', Char(27), 32768),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_SET_POS', Char(9), (-30620, -1000, -17090), 317),
			Insn('CHAR_FLAG1_UNSET', Char(20), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(22), 128),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 6))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 11))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 12))), Insn('NOT'), Insn('BOOL_AND'), Insn('ATTR', 0), Insn('CONST', 101), Insn('EQ'), Insn('ATTR', 0), Insn('CONST', 102), Insn('EQ'), Insn('OR'), Insn('BOOL_AND'), Insn('END')]), [
					Insn('EVENT', Function((2, 13))),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
			Insn('CHAR_FLAG1_UNSET', Char(24), 128),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(10), (-39100, 3000, 21560), 315),
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_SET_POS', Char(13), (-26990, 0, 1930), 270),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_SET_POS', Char(9), (-26490, -1000, -25270), 180),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_SET_POS', Char(9), (-26490, -1000, -25270), 180),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_SET_POS', Char(9), (-26490, -1000, -25270), 180),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1280)), Insn('FLAG', Flag(1346)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(25), 128),
			Insn('CHAR_FLAG1_UNSET', Char(26), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 44))),
		]),
		(Expr([Insn('FLAG', Flag(737)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(737)),
			Insn('EVENT', Function((0, 48))),
		]),
		(Expr([Insn('FLAG', Flag(738)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(738)),
			Insn('EVENT', Function((0, 56))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1008)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(1008)),
			Insn('EVENT', Function((0, 27))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1009)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(1009)),
			Insn('0xD0', 1, Expr([Insn('CONST', 8), Insn('SET'), Insn('END')])),
			Insn('EVENT', Function((0, 29))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('OBJ_FLAG_SET', Object(7), 4),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('0xB5', b'\x00\x02\x80\x00'),
	Insn('0xB5', b'\x00\x03\x80\x00'),
	Insn('0xB5', b'\x00\x04\x80\x00'),
	Insn('0xB5', b'\x00\x05\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(779)), Insn('FLAG', Flag(782)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x00\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1348)), Insn('FLAG', Flag(1349)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x01\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1352)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x02\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1560)), Insn('FLAG', Flag(1562)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x03\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1565)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x04\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 12))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x05\x80\x00'),
		]),
		(None, []),
	]),
	Insn('0x65', 1, 1),
	Insn('0x65', 2, 1),
	Insn('0x65', 3, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(792)), Insn('FLAG', Flag(793)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x66', 1, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(793)), Insn('FLAG', Flag(800)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x66', 2, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(794)), Insn('FLAG', Flag(800)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x66', 3, 1),
		]),
		(None, []),
	]),
	Insn('0x65', 8, 1),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 3))), Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 4))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x66', 8, 1),
		]),
		(None, []),
	]),
	Insn('EFF_LOAD', ResId(8), 'eff\\mgm03_02.eff'),
	Insn('EFF_PLAY', (ResId(8), 8), Char(255), 0, -17180, -1, -2000, -1, 32766, -1, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1352)), Insn('FLAG', Flag(1359)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), []),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(799)), Insn('FLAG', Flag(800)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x11', b'\xfd\xd5\xc6', 25, 200, 0),
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
		]),
		(Expr([Insn('FLAG', Flag(1359)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x11', b'\xfd\xd5\xc6', 25, 200, 0),
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
		]),
		(Expr([Insn('FLAG', Flag(1564)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x11', b'\xfd\xd5\xc6', 25, 200, 0),
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'model6', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'model5', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'CA02', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'CA02', Insn('1', 2)),
			Insn('0x65', 2, 1),
			Insn('0x65', 3, 1),
		]),
		(None, [
			Insn('OBJ_SET_FRAME', Object(255), 'model6', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'model5', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'CA02', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'CA02', Insn('0', 2)),
		]),
	]),
	Insn('OBJ_FLAG_SET', Object(11), 4),
	Insn('0x65', 7, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1537)), Insn('FLAG', Flag(1542)), Insn('NOT'), Insn('BOOL_AND'), Insn('0x23', 1), Insn('CONST', 8), Insn('EQ'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(11), 'light', Insn('0', 1)),
			Insn('OBJ_FLAG_UNSET', Object(11), 4),
			Insn('0x66', 7, 1),
		]),
		(None, [
			Insn('0x16', Insn('3', b'\x03\x01\x00')),
		]),
	]),
	Insn('OBJ_FLAG_SET', Object(8), 4),
	Insn('OBJ_SET_FRAME', Object(8), 'light', Insn('0', 1)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1040)), Insn('NOT'), Insn('FLAG', Flag(1024)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(8), 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1565)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\n\x80\x00'),
		]),
		(None, []),
	]),
	Insn('OBJ_FLAG_SET', Object(9), 4),
	Insn('OBJ_SET_FRAME', Object(9), 'light', Insn('0', 1)),
	Insn('OBJ_FLAG_SET', Object(10), 4),
	Insn('OBJ_SET_FRAME', Object(10), 'light', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(10), 'patlight', Insn('0', 1)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1292)), Insn('NOT'), Insn('FLAG', Flag(1282)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(9), 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('FLAG', Flag(1554)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(10), 4),
		]),
		(None, []),
	]),
	Insn('0x1B', 0, Function((255, 255)), 255),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(784)), Insn('FLAG', Flag(793)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 0, Function((0, 64)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(793)), Insn('FLAG', Flag(799)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 0, Function((0, 64)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(799)), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 0, Function((0, 64)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 14))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 0, Function((0, 64)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1346)), Insn('FLAG', Flag(1351)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 0, Function((0, 64)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1351)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 0, Function((0, 64)), 0),
		]),
		(None, []),
	]),
	Insn('OBJ_FLAG_UNSET', Object(6), 16),
	Insn('0x70', Object(6), b'\n\x00'),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊！欢迎来到圣乌尔斯拉医院。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'说起来，那个蓝头发的孩子……\n'
						'你的身体已经好了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0205F嗯，是的……\n'
						'托您的福。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这样啊，不管怎么说，\n'
						'身体没有大碍就好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'那个蓝头发的孩子昨天突然\n'
						'就倒下了，真是吓了我一跳。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过现在看起来很精神，这就好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('CHAR_WATCH', Char(254), Char(9), 0),
			Insn('TEXT_TALK', Char(254), Text(
				'因为不久之前的狼型魔兽事件，\n'
				'我的工作时间也稍微延长了一些呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'说实话，大家都很辛苦啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'清晨时分，\n'
				'一些让人感觉很阴森恐怖的人\n'
				'接二连三被送了进来。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀……被吓了一跳呢，\n'
				'克洛斯贝尔市发生什么事件了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啊！欢迎来到圣乌尔斯拉医院。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'今天没有把那个可爱的孩子\n'
				'也带来吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'绿色头发的女孩子吗……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'没有在医院外面见到呢。\n'
				'会不会还在医院里面啊？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊！欢迎来到乌尔斯拉医科大学附属医院。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(339), Text(
						'#1109F哟，你好啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哈哈，精神真好呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我想你们也都知道，\n'
						'接待处在院区那边。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'巴士才刚刚开走，\n'
						'暂时应该不会回来哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'接待处在院区那边。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'刚才约亚西姆医生\n'
						'打算去郊外钓鱼。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我觉得很危险，本想要阻止他，\n'
						'但是他给了我一米拉，\n'
						'让我为他保密。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……该怎么说呢，\n'
						'没想到他是一个这么小气的人啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'约亚西姆医生想要\n'
						'偷偷去钓鱼，\n'
						'还给了我一米拉的封口费。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……不过，他最后还是被\n'
						'护理师和实习医生们\n'
						'给拖了回去。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啊！欢迎来到圣乌尔斯拉医院。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你们应该没有受伤吧？\n'
				'难得的纪念庆典，\n'
				'注意不要闹过头，最后反而乐极生悲。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊！欢迎来到圣乌尔斯拉医院。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……停在那边的那辆车，真是好棒啊！\n'
						'是加长型豪华轿车吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，有钱人开的车\n'
						'果然别具格调。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'快看那边的加长轿车。\n'
						'那可是最新型的，\n'
						'价格肯定非常昂贵吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，有钱人开的车\n'
						'果然别具格调。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啊！欢迎来到圣乌尔斯拉医院。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'现在，克洛斯贝尔市内\n'
				'正在举行纪念庆典吧。\n'
				'很热闹吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 12))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((2, 14))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'啊！欢迎来到圣乌尔斯拉医院。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'现在彩虹剧团的话题好像\n'
						'在外面闹得沸沸扬扬呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'如果可以的话，我也想去看看啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'这所医院里配备有专用的车辆──\n'
						'『救护车』。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'即使是来不及等定期巴士的急诊病人，\n'
						'只要使用导力通讯联系我们，\n'
						'无论他在克洛斯贝尔何处，我们都能迅速赶到。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'前段时间之所以能及时救治\n'
						'身受重伤的街头混混，\n'
						'也是多亏了救护车的速度。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'急诊病人的话，\n'
						'只要使用导力通讯联系我们，\n'
						'无论他在克洛斯贝尔何处，我们都能迅速赶到。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'跟普通马力的导力车相比，\n'
						'救护车的速度可以轻松把它们甩在身后。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'嗯……已经准备回去了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'如果想要回克洛斯贝尔市，\n'
						'在那边的巴士站等一会就好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'今天的巴士应该还有几班，\n'
						'没必要急急忙忙的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'如果想要回克洛斯贝尔市，\n'
						'在那边的巴士站等一会就好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'话说，夕阳真是漂亮呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'利顿被袭击的那天晚上，\n'
						'来了一个很烦的商人。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'想以非常高的价格\n'
						'向我们推销床单，\n'
						'我被叫去应付他了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'因此刚好就\n'
						'不在这里。\n'
						'没有帮到你们，真是抱歉。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'嗯……我那天晚上\n'
						'刚好不在这里呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不好意思，我没有什么线索。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'刚才有联系说，\n'
						'开在郊外的定期巴士\n'
						'受到了魔兽的袭击。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但是英勇登场的两位游击士\n'
						'瞬间就将那些家伙给收拾了。\n'
						'好厉害啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0306F联系中完全没提到我们……\n'
						'说明对方对我们\n'
						'根本就没有印象呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0011F好了好了……\n'
						'是因为艾丝蒂尔和约书亚\n'
						'实在很强，给人印象太深吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(310), Text(
						'#1300F呵呵，你们也必须多加努力了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'哎呀～游击士果然好厉害啊，\n'
						'要着重注意呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哟，你们好。\n'
				'这里是乌尔斯拉医科大学附属医院……\n'
				'简称乌尔斯拉医院。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你们不是医院相关人员吧？\n'
				'进门之后请直接进入里面的建筑物。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'早上散步有益身体健康。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我跟患者一起散步的同时，\n'
				'也促进了自己的健康，真是一举两得呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天是我负责值班呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'护理师这个工作很忙的。\n'
				'必须要多加注意，\n'
				'不能把身体累坏了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'之前的那些伤患\n'
				'被送进了ＩＣＵ（加护病房），\n'
				'他们不会有事吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我们与患者也有私交，\n'
				'所以免不了经常劳心伤神。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'也就是说，\n'
				'必须要打起精神来啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀，警察弟弟……\n'
				'你带着一个好可爱的小女孩啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵……\n'
				'注意不要让她\n'
				'迷路了哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'纪念庆典今天就要结束了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我想你们这几天\n'
						'工作也都很忙吧，\n'
						'不过也就到今天为止了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'只剩一点了，\n'
						'大家都努力加油吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'纪念庆典今天就要结束了……\n'
						'虽然最近都没怎么好好休息，\n'
						'不过马上就熬到头啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'今天一整天都\n'
						'努力加油吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'米海尔今天的状态不错，\n'
				'还获得了外出许可哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然只能在医院用地里走一走而已。\n'
				'不过平时他都躺在床上，\n'
				'所以应该也能放松心情了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'在纪念庆典期间，\n'
						'有很多住院患者都想要\n'
						'获得临时外出许可。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过他们的病情各不相同，\n'
						'如果不向医生确认一下，\n'
						'我也不知道该怎么处理。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'因为是难得的纪念庆典，\n'
						'所以我也很理解他们想要去玩的心情……\n'
						'但就算和我说这些也无济于事啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'哎呀，午安。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1361)), Insn('END')]), [
							Insn('TEXT_TALK', Char(254), Text(
								'呵呵，兰迪先生，\n'
								'昨天的演唱会真不错，\n'
								'谢谢你邀请我。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'兰恩和菲莉亚\n'
								'好像都玩得很开心呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(260), Text(
								'#0304F哈哈，让女士开心\n'
								'正是男人的使命啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0006F竟然同时跟三个护理师约会，\n'
								'兰迪你还真是个中高手呢……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(258), Text(
								'#0105F确实呢……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(259), Text(
								'#0211F不如说是气血旺盛得过头了吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('TEXT_TALK', Char(254), Text(
								'兰迪先生，罗伊德，\n'
								'昨天的演唱会真不错。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'兰恩和菲莉亚\n'
								'好像都玩得很开心呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(260), Text(
								'#0304F哈哈，让女士开心\n'
								'正是男人的使命啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F那个……\n'
								'我才应该\n'
								'谢谢你们的邀请。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(258), Text(
								'#0105F原来你们……\n'
								'还和护理师小姐们\n'
								'二对三的约会了呀。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(259), Text(
								'#0211F真是血气旺盛呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0006F（别用那种眼神看我……）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'昨天玩得很开心……\n'
						'呵呵，感觉今天一整天都能努力工作了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'说起来，下个月就是纪念庆典了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然菲莉亚邀请我去玩……\n'
						'但不知道能不能申请到休假呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0309F哈哈，我很期待呢。\n'
						'要努力争取到休假哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(254), Char(260), 500),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯……好吧，我会试着努力的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F（好像是兰迪约了她们……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'不知道能不能在纪念庆典期间请到假呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'算了，只能好好努力了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'哎呀，这不是赛西儿前辈的弟弟吗，\n'
						'最近过得好吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F总、总觉得好像\n'
						'不知不觉就在护理师间\n'
						'成为了名人呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'这不是赛西儿前辈的弟弟吗，\n'
						'最近过得好吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'夕阳下的艾鲁姆湖真美啊，\n'
				'让人觉得心灵都被治愈了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……好了，今天也要好好加油值夜班！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_WATCH', Char(254), Char(12), 0),
					Insn('TEXT_TALK', Char(254), Text(
						'好啦，老爷爷。\n'
						'太阳都快要下山了……\n'
						'我们回病房吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'呵呵，说得也是呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'总算快要出院了，\n'
						'还是别勉强的好。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'好了，差不多该把老爷爷\n'
						'带回病房了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊，赛西儿前辈。\n'
						'那几位是……？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(310), Text(
						'#1300F是我弟弟罗伊德……\n'
						'和他的恋人们。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'咦、咦咦……！？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0011F等、等一下，赛西儿姐姐！\n'
						'玩笑开过头了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(310), Text(
						'#1309F呵呵，只是想稍微\n'
						'开个玩笑而已。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'什、什么啊，吓死我了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'关于罗伊德警官的事，\n'
						'已经从赛西儿前辈那里\n'
						'听说过了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'赛西儿前辈所说的事\n'
						'到底是真的还是在开玩笑……\n'
						'偶尔会让人搞不清楚呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'哎呀，下午好。\n'
						'请问几位是来探病的吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0305F哦哦，真不错、真不错！{wait}'
						'{page}'
						'#0309F嗯，真正的白衣天使\n'
						'果然就是不一样呢！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0205F……真正的？\n'
						'那是什么意思……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0104F好了好了，这个话题就到此为止吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那、那个……？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F……总觉得很对不起您呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，看起来非常有精神呢。\n'
						'是来探望朋友的吗？{wait}'
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

data['code'][8] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'虽然工友的工作\n'
				'偶尔会被人小看……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'但是要做的事情有很多，\n'
				'而且，最重要的是它十分有意义。\n'
				'我很喜欢这份工作哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'凯瑞教授坐在长椅上\n'
				'不停地叹着气呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，即使是了不起的医生，\n'
				'也会有各式各样的烦恼吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'为了不让花朵枯萎，\n'
				'必须多花点心思照料它们呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'大概是因为眺望了艾鲁姆湖的美景吧，\n'
				'我现在的心情非常平静。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'对于在纪念庆典期间也无法外出的\n'
				'住院患者来说，\n'
				'这里就如同沙漠中的绿洲一样。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'绿色有让人心情\n'
				'平静的效果。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然作用不是非常大，但我们希望\n'
				'可以借此让患者们稍微安心一些。\n'
				'所以医院里放置了很多植物呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'装上防护栏之后，\n'
				'医院看起来气派了不少呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我也必须要小心魔兽了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'屋顶的调查结束了吗……\n'
				'有什么线索了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哦哦，要是屋顶空出来了，\n'
				'我就过去打扫吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'虽然在医院工作很长时间了，\n'
				'但还是觉得这里的建筑\n'
				'相当气派呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'好了，必须好好整理一下了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯？怎么了？迷路了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'要找院区的话，\n'
				'里面那栋高大的建筑就是。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][9] = [
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
		(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'昨天从ＩＢＣ的人那里\n'
				'得到了玩偶。\n'
				'嘿嘿……好高兴哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'迪塔先生\n'
				'真是一个亲切的叔叔呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(2)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，清新的空气真让人心情舒畅。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'下次找小滴\n'
				'一起散步好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
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
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，说得也是呢。\n'
				'我们回去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'难得就快要出院了，\n'
				'如果太过勉强而把身体搞坏，\n'
				'那可就是得不偿失了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(310), Text(
						'#1300F老爷爷，\n'
						'那之后膝盖的情况怎么样了？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，好得就像没受过伤一样。\n'
						'在这里接受治疗真是太正确了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(310), Text(
						'#1300F呵呵，那真是太好了。{wait}'
						'{page}'
						'贝尔达因医生也说\n'
						'您马上就可以出院了，\n'
						'再稍微努力一下吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0004F（赛西儿姐姐……\n'
						'\u3000看来已经非常\n'
						'\u3000习惯护理师的工作了。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'马上就要出院了吗……\n'
						'呵～呵～呵～真是高兴啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我在澡堂摔倒，\n'
						'弄伤了膝盖。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'多亏了这里的医生替我治疗\n'
						'才能恢复成现在这样，\n'
						'可以到外面行走了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'话说回来，我都没想到那么快\n'
						'就可以走动了……\n'
						'这里的医生们真的很优秀。{wait}'
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

data['code'][11] = [
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
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'奶奶看起来充满活力，真是太好了。\n'
				'而且听说她马上就可以出院了呢！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'奶奶出院时，我一定会跟爸爸妈妈\n'
				'一起来接她的！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯……\n'
				'好大的医院啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'希望奶奶\n'
				'一切都好呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我来探望\n'
				'因为受伤而住院的朋友。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过，那家伙的病房\n'
				'究竟在什么地方呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(4)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'朋友的病房……在哪里呢？\n'
				'……算了，随便走走总会找到的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'我今天是来探望\n'
		'男朋友的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'他非常固执，\n'
		'希望不要给其他患者\n'
		'添麻烦才好啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1134)), Insn('END')]), [
			Insn('TEXT_TALK', Char(16), Text(
				'#3600F好了，必须把这些\n'
				'医疗用品搬出去……{wait}'
				'{page}'
				'哈哈哈，各位\n'
				'还请加油工作。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F咦，哈罗德先生……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(16), Text(
				'#3600F各位好……很久不见了呢，\n'
				'没想到会在这种地方再会。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F哈哈……自从上次的事件以来，\n'
				'市外的工作也增加了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F哈罗德先生也是因为工作来这里的吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(16), Text(
				'#3600F嗯，我是来给乌尔斯拉医院\n'
				'送医疗用品跟日用品的。{wait}'
				'{page}'
				'购买导力车果然是个正确的决定，\n'
				'来回方便了很多呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F您的生意好像也很顺利呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1134)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
			Insn('TEXT_TALK', Char(17), Text(
				'……话说……迪诺那家伙\n'
				'是什么时候拥有了那种力量的……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(17), Text(
				'啧，该死的……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(17), Text(
				'该死的……竟敢瞧不起\n'
				'身为干部的我。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(17), Text(
				'可恶的迪诺，等我回去之后，\n'
				'一定要好好收拾你……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(5)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
			Insn('TEXT_TALK', Char(18), Text(
				'说实话，我本来是不想\n'
				'来见那种家伙的……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(18), Text(
				'妈妈竟然让我过来\n'
				'给老爸送饭。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(18), Text(
				'……可恶，\n'
				'他到底在什么地方啊……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(6)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1655)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F咦，凯特前辈……？\n'
				'你为什么会在这种地方！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F警察局的正规军有\n'
				'市外活动吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'#15200F是啊，不过我只是个跟班而已。{wait}'
				'{page}'
				'#15203F黑月的人正在\n'
				'乌尔斯拉医院住院呢。{wait}'
				'{page}'
				'#15200F搜查二课的人要来\n'
				'进行案情查访，\n'
				'我才开巡逻车送他们过来的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(254), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(254), Text(
				'#15206F虽然我很不擅长\n'
				'开车。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F哈哈……原来是这样啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F真是辛苦您了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1655)),
		]),
		(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'#15208F黑月是……黑手党组织啊，\n'
				'我以前完全不知道呢……{wait}'
				'{page}'
				'#15201F……话说回来，\n'
				'二课的人花得时间可真长呢。{wait}'
				'{page}'
				'#15206F都已经耗去整整一上午了，\n'
				'大概是碰到棘手的人了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(7)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'#15201F二课的人到底在干什么啊？\n'
				'时间花得太长了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'在这个医院里\n'
				'有我们的成员──\n'
				'约亚西姆团员在。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，待会\n'
				'试着去邀请他一下吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我们团长费瑟尔，\n'
						'在克洛斯贝尔设立分部\n'
						'已经是两年前的事情了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这两年，克洛斯贝尔分部\n'
						'的活动确实丰富了很多呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'没有什么能比热爱垂钓的伙伴\n'
						'增加更让人高兴了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(8)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'被热爱垂钓的伙伴们\n'
						'邀请去旅游……\n'
						'没有比这更高兴的事情了。{wait}'
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
		(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'……我差不多也该\n'
				'回诊察室了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'就算已经很累了，\n'
				'不过我也不想因为一直休息\n'
				'而被拉格教授取笑。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 4))), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(9)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'本来还指望你们\n'
						'能全部都拿走的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呼……\n'
						'毕竟是辟邪用的人偶，\n'
						'再怎么说也不能随便丢弃啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'你们在放在露台的杂物中……\n'
						'找到什么有用的东西了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……皮绳吗？\n'
						'只要那个就好了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'你们多拿走一些\n'
						'也是可以的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F（那些杂货和人偶\n'
						'\u3000实在是太占地方了吧……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(9)),
				]),
			]),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 3))), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'放有杂货的集装箱\n'
				'在位于宿舍二楼，穿过男性职员\n'
				'宿舍尽头的露台上。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'要是发现了什么\n'
				'有用的东西，就随便\n'
				'拿走吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'说实话，我正烦恼该怎么处理那些东西呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('FLAG_GET', 2))), Insn('END')]), [
			Insn('CALL', Function((0, 62))),
		]),
		(Expr([Insn('FLAG', Flag(9)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'由于家庭和工作方面的问题，\n'
				'让我感到很疲惫了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'做教授\n'
				'也很辛苦呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'……最近似乎有点累了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'拜托护理师希蓉小姐\n'
				'订购一些医疗用品，\n'
				'却送来了其它东西……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'儿子琴兹也还是\n'
				'跟以前一样，\n'
				'没有退出不良分子的意思……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'做教授\n'
				'也很辛苦呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(9)),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1446)), Insn('NOT'), Insn('END')]), [
			Insn('EMOTE', Char(22), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(22), Text(
				'#2900F哎呀，艾莉，真是好巧呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0105F贝尔……？\n'
				'你在这种地方干什么呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(22), Text(
				'#2900F啊，我是陪父亲\n'
				'过来的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F陪迪塔总裁吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F总裁生了什么病吗……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0109F啊哈哈……我想大概\n'
				'不是那么回事……{wait}'
				'{page}'
				'#0100F贝尔，是为那件事而来吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(22), Text(
				'#2904F嗯，没错。{wait}'
				'{page}'
				'#2900F你们去接待处看看就明白了。\n'
				'如果各位时间宽裕的话，\n'
				'去见见我父亲怎么样？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1446)),
		]),
		(Expr([Insn('FLAG', Flag(13)), Insn('END')]), [
			Insn('TEXT_TALK', Char(22), Text(
				'#2906F父亲好慢啊，\n'
				'到底在干什么呢。{wait}'
				'{page}'
				'离商谈的时间\n'
				'只剩下三十分钟了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(22), Text(
				'#2906F竟在这种商谈众多的繁忙时期……\n'
				'我真是服了他呢。{wait}'
				'{page}'
				'#2900F不过，算啦，因为这是父亲\n'
				'为数不多的美德之一。{wait}'
				'{page}'
				'作为女儿，也不能斤斤计较，\n'
				'不去陪他吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0102F呵呵，嘴上虽然这样说，\n'
				'但你每年都会陪他来呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(22), Text(
				'#2904F……哈，只不过是每年都\n'
				'刚好有时间而已，没办法啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(13)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(10)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(24), Text(
						'#2400F利顿也重回工作岗位了，\n'
						'他工作很努力呢。{wait}'
						'{page}'
						'而且还悄悄\n'
						'把我偷偷推给他的，\n'
						'原本属于我的工作也给做完了。{wait}'
						'{page}'
						'#2409F哈～哈～哈～\n'
						'有个好学生的我真是幸福啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(10)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(24), Text(
						'#2400F还好有利顿帮我把工作\n'
						'给做完了。{wait}'
						'{page}'
						'#2409F空出来的时间就去钓钓鱼，\n'
						'有效地利用一下吧。{wait}'
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
		(Expr([Insn('FLAG', Flag(14)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'旅行最重要的事情\n'
				'就是享受当地的特色。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'即使是以医疗研究而闻名的医院，\n'
				'也完全有资本成为景点。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(14)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'旅行最重要的事情\n'
				'就是享受当地的特色。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'克洛斯贝尔可以参观的地方太多了，\n'
				'所以玩起来也有点辛苦呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(15)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'在这所医院里面设置有\n'
				'检查身体健康状态的，\n'
				'被称为『全面健康检查』的设备……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'因为每天都要干各种家务杂活，\n'
				'使身体囤积了相当多的疲劳……\n'
				'一定要去检查一下呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(15)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'要是我因为工作过度疲劳，\n'
				'而被那个『全面健康检查』设备\n'
				'诊断出什么坏结果……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'就以这个为借口，\n'
				'让主人给我\n'
				'多放几天假好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('EVENT_BEGIN', 1),
	Insn('0x09', 134217728),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}有一个巴士车站。\n'
		'要乘坐巴士吗？{wait}'
	)),
	Insn('MENU', 0, -1, -1, 1, Text(
		'克洛斯贝尔市南出口\n'
		'岔口停靠站（沙洲附近）\n'
		'放弃\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('CALL', Function((0, 26))),
			Insn('0x0A', 134217728),
			Insn('NEW_SCENE', 'r1500', b'\x00\x00\x00\x07'),
		]),
		(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
			Insn('CALL', Function((0, 26))),
			Insn('0x0A', 134217728),
			Insn('NEW_SCENE', 'r1530', b'\x00\x00\x00\x07'),
		]),
		(None, []),
	]),
	Insn('0x0A', 134217728),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-59000, 1000, 2200), 0),
	Insn('CAM_ROTATE', 45, 26, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 23000, 0),
	Insn('0xE0', b'\x01'),
	Insn('CHAR_SET_POS', Char(0), (-56600, 0, 3800), 180),
	Insn('CHAR_SET_POS', Char(1), (-56600, 0, 4900), 180),
	Insn('CHAR_SET_POS', Char(2), (-56600, 0, 6000), 180),
	Insn('CHAR_SET_POS', Char(3), (-56600, 0, 7200), 180),
	Insn('OBJ_FLAG_SET', Object(7), 4096),
	Insn('OBJ_FLAG_UNSET', Object(7), 4),
	Insn('CHAR_FLAG1_UNSET', Char(28), 128),
	Insn('0x78', b'\x07', Char(28)),
	Insn('OBJ_SET_FRAME', Object(7), 'light', Insn('0', 1)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(28), (-75000, 0, 500), 90),
	Insn('0xD3', Char(28), 0, 90000, 0, 0),
	Insn('0x74', Object(7), 7680),
	Insn('0x71', Object(7), b'y\x00', 180, 32),
	Insn('0x0D'),
	Insn('FORK', 28, 1, [
		Insn('0x95', Char(254), (-59000, 0, 500), 4000, 0),
	]),
	Insn('SOUND_PLAY', 466, 0, 0, 100),
	Insn('SOUND_PLAY', 467, 0, 0, 100),
	Insn('FORK_AWAIT', Char(28), 1),
	Insn('0x71', Object(7), b'[\x00', 65656, 0),
	Insn('0x79', b'\x07\x00'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FLAG_SET', Flag(1008)),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('EVENT_BEGIN', 1),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('CHAR_SET_POS', Char(0), (-56560, 0, 4080), 180),
	Insn('CHAR_SET_POS', Char(1), (-56560, 0, 4080), 180),
	Insn('CHAR_SET_POS', Char(2), (-56560, 0, 4080), 180),
	Insn('CHAR_SET_POS', Char(3), (-56560, 0, 4080), 180),
	Insn('CAM_OFFSET', (-56560, 1000, 4080), 0),
	Insn('CAM_ROTATE', 45, 26, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 22000, 0),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][28] = [
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
						Insn('0x74', Object(11), 7680),
						Insn('0x71', Object(11), b'\xf1\x00', 270, 0),
						Insn('SOUND_PLAY', 464, 0, 0, 100),
						Insn('0x79', b'\x0b\x00'),
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

data['code'][29] = [
	Insn('EVENT_BEGIN', 1),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('CHAR_SET_POS', Char(0), (-51320, 0, 17590), 270),
	Insn('CHAR_SET_POS', Char(1), (-51320, 0, 17590), 270),
	Insn('CHAR_SET_POS', Char(2), (-51320, 0, 17590), 270),
	Insn('CHAR_SET_POS', Char(3), (-51320, 0, 17590), 270),
	Insn('CHAR_SET_POS', Char(4), (-51320, 0, 17590), 270),
	Insn('CHAR_SET_POS', Char(5), (-51320, 0, 17590), 270),
	Insn('SLEEP', 1),
	Insn('CAM_OFFSET', (-51320, 1000, 17590), 0),
	Insn('CAM_ROTATE', 45, 26, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 22000, 0),
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

data['code'][30] = [
	Insn('EXPR_VAR', 3, Expr([Insn('CONST', 8), Insn('SET'), Insn('END')])),
	Insn('CALL', Function((0, 28))),
	Insn('RETURN'),
]

data['code'][31] = [
	Insn('EVENT_BEGIN', 1),
	Insn('SOUND_PLAY', 1094, 0, 255, 100),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F这里的话似乎可以钓到鱼。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-17220, 0, -31290), 1500),
	Insn('CAM_ROTATE', 60, 36, 0, 1500),
	Insn('0x6E', 500, 1500),
	Insn('CAM_DISTANCE', 22000, 1500),
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
			Insn('MINIGAME', 6, 14, [
				-16450,
				-1000,
				-26020,
				180,
				-17180,
				-2000,
				-32770,
			]),
		]),
		(None, []),
	]),
	Insn('0xE0', b'\x02'),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][32] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 14))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 13))), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_START', Char(255)),
					Insn('CALL', Function((2, 12))),
					Insn('TEXT_END', Char(255)),
				]),
				(None, [
					Insn('EVENT_BEGIN', 2),
					Insn('FADE_ON', 300, Color(0x00000000), 100),
					Insn('0x0D'),
					Insn('MENU', 0, -1, -1, 0, Text(
						'【等待导力巴士】\n'
						'【放弃】\n'
					)),
					Insn('MENU_WAIT', 0),
					Insn('0x60', 0),
					Insn('FADE_OFF', 300, Color(0x00000000)),
					Insn('0x0D'),
					Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
						0: [
							Insn('CALL', Function((0, 26))),
							Insn('FLAG_SET', Flag(740)),
							Insn('NEW_SCENE', 'e0010', b'\x00\x00\x00\x07'),
							Insn('BREAK'),
						],
						1: [
							Insn('BREAK'),
						],
						None: [],
					}),
					Insn('EVENT_END', 3),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
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
		(Expr([Insn('FLAG', Flag(799)), Insn('FLAG', Flag(800)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 2),
			Insn('FADE_ON', 300, Color(0x00000000), 100),
			Insn('0x0D'),
			Insn('MENU', 0, -1, -1, 0, Text(
				'【等待导力巴士】\n'
				'【放弃】\n'
			)),
			Insn('MENU_WAIT', 0),
			Insn('0x60', 0),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('0x0D'),
			Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
				0: [
					Insn('CALL', Function((0, 47))),
					Insn('BREAK'),
				],
				1: [
					Insn('BREAK'),
				],
				None: [],
			}),
			Insn('EVENT_END', 3),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CALL', Function((0, 25))),
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
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F对了……回去之前\n'
						'必须得去跟赛西儿姐姐报告。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F在回克洛斯贝尔市之前，\n'
						'必须对魔兽进行调查。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('TEXT_END', Char(255)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][33] = [
	Insn('CALL', Function((0, 37))),
	Insn('RETURN'),
]

data['code'][34] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(794)), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((0, 42))),
		]),
		(None, [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}木箱上面布满了灰尘。{wait}'
				'{page}'
				'看来很长一段时间\n'
				'都没有人管过了。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_END', Char(255)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][35] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(795)), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((0, 43))),
		]),
		(None, [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}扶手上部的油漆\n'
				'有多处剥落的痕迹。{wait}'
				'{page}'
				'看上去像是最近才留下的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_END', Char(255)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][36] = [
	Insn('EVENT_BEGIN', 0),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('CROSSFADE', 1000),
	Insn('CHAR_SET_POS', Char(257), (-37200, 0, -1000), 90),
	Insn('CHAR_SET_POS', Char(258), (-38600, 0, -1000), 90),
	Insn('CHAR_SET_POS', Char(259), (-38600, 0, 400), 90),
	Insn('CHAR_SET_POS', Char(260), (-37200, 0, 400), 90),
	Insn('CAM_OFFSET', (-27020, -500, 13870), 0),
	Insn('CAM_ROTATE', 53, 17, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 47750, 0),
	Insn('0xCB', b'T\x01\xc8\x00', 'c_plac15', b'\x00\x88\x13'),
	Insn('CAM_OFFSET', (-16610, -500, 50), 10000),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-34620, 700, -20), 0),
	Insn('CAM_ROTATE', 42, 21, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 24700, 0),
	Insn('CHAR_SET_POS', Char(257), (-35740, 0, -950), 90),
	Insn('CHAR_SET_POS', Char(258), (-37220, 0, 560), 90),
	Insn('CHAR_SET_POS', Char(259), (-37220, 0, -950), 90),
	Insn('CHAR_SET_POS', Char(260), (-35740, 0, 560), 90),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101031V#0300F#5P这里就是医科大学啊……\n'
		'嘿，看上去很气派嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101032V#0203F#6P……『圣乌尔斯拉医科大学』。{wait}'
		'{page}'
		'#11101033V#0200F大陆首屈一指的综合医院，\n'
		'是一家非常著名的医疗研究机构。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101034V#6P#0005F原来这么有名啊。{wait}'
		'{page}'
		'#11101035V#0000F确实，巴士的班次这么频繁，\n'
		'说明前来就诊的人应该非常多吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101036V#0104F听说原本是由医疗发达国家──\n'
		'雷米菲利亚公国\n'
		'帮助建造的。{wait}'
		'{page}'
		'#11101037V#0100F据说周边各国的重症患者\n'
		'也会被送到这里来呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 2000, (10, 11, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101038V#0302F#5P对了，这里有穿着\n'
		'护士服的姐姐们吧！{wait}'
		'{page}'
		'#11101039V#0309F哎呀，真养眼真养眼丅{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(260), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(260), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(260), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101040V#0012F#12P兰迪真有精神呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101041V#0103F#6P虽然之前坐车\n'
		'来过很多次了……{wait}'
		'{page}'
		'#11101042V#0100F不过步行的话，\n'
		'果然要走很长时间呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101043V#0208F#6P……………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101044V#11P#0005F缇欧……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101045V#0105F果然还是太累了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101046V#0203F#6P……不，没事的。{wait}'
		'{page}'
		'#11101047V#0200F还没有去\n'
		'阿尔摩利卡村的距离那么长……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101048V#11P#0001F你没事就好……\n'
		'不过别太勉强自己了哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(259), Char(257), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101049V#0204F#6P嗯，不用担心。{wait}'
		'{page}'
		'#11101050V#0202F……比起这个，\n'
		'罗伊德前辈还不快去\n'
		'见见你那个姐姐吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101051V#0305F#5P说得也是，还有这件事呢！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('SLEEP', 300),
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101052V#0307F#5P好了好了，罗伊德！\n'
		'快点去见见那位姐姐吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 300),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101053V#0006F#12P……为什么兰迪的\n'
		'兴致那么高啊。{wait}'
		'{page}'
		'#11101054V#0000F算了，赛西儿姐姐\n'
		'也比较好说话……{wait}'
		'{page}'
		'#11101055V请医院的接待员叫她出来吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101056V#0309F#5P好！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(258), Char(257), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101057V#0102F呵呵，那么\n'
		'我们去正面的院区吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(0), (-37900, 0, -300), 90),
	Insn('FLAG_SET', Flag(782)),
	Insn('QUEST', 63, Insn('TASK_SET', 8)),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][37] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 500, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('LOAD_CHCP', 'chr/ch00001', 30),
	Insn('LOAD_CHCP', 'chr/ch00301', 31),
	Insn('CAM_OFFSET', (-34930, 3900, 16980), 0),
	Insn('CAM_ROTATE', 45, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 26500, 0),
	Insn('CHAR_SET_POS', Char(257), (-36910, 3000, 16290), 90),
	Insn('CHAR_SET_POS', Char(258), (-38300, 3000, 16300), 90),
	Insn('CHAR_SET_POS', Char(259), (-38300, 3000, 17300), 90),
	Insn('CHAR_SET_POS', Char(260), (-37000, 3000, 17300), 90),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101320V#0000F#6P那么……\n'
		'来调查一下这上面吧。{wait}'
		'{page}'
		'#11101321V兰迪，帮把手。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101322V#0300F#5P收到。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-34930, 4700, 16980), 2500),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 38))),
	Insn('SLEEP', 300),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 39))),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 5300),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}布满灰尘的木箱上\n'
		'有着某种痕迹。{wait}'
		'{page}'
		'似乎是野兽的脚印。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101323V#0004F#6P……猜中了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101324V#0300F#6P嗯，魔兽的足迹……\n'
		'而且还是狼型魔兽的足迹。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101325V#0101F#5P果然……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101326V#0203F这样看来……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-36200, 4000, 20200), 4000),
	Insn('CAM_ROTATE', 35, 16, 0, 4000),
	Insn('CAM_DISTANCE', 34000, 4000),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (-36480, 3000, 20450), 1500, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 300),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 300),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('CHAR_ROTATE', Char(259), 0, 500),
	Insn('0x6F', b'\x11'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101327V#0200F#6P魔兽很可能是从\n'
		'那边侵入的呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101328V#0000F嗯，大概没错。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-36930, 3900, 16980), 3000),
	Insn('CAM_DISTANCE', 26500, 3000),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 40))),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 41))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'y'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101329V#0300F#6P这样看起来，\n'
		'那里也不是很高。{wait}'
		'{page}'
		'#11101330V为了防止它们再次闯入，\n'
		'还是制定相关对策比较好呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101331V#0103F#6P说得也是呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101332V#0100F#6P不过，对这里的调查工作，\n'
		'这样就算告一段落了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101333V#0001F#11P嗯，对啊……{wait}'
		'{page}'
		'#11101334V#0003F……不过它们为什么要特地\n'
		'闯入这种地方呢……{wait}'
		'{page}'
		'#11101335V还有，为什么对利顿医生的\n'
		'袭击行为只进行了一半……{wait}'
		'{page}'
		'#11101336V#0001F谜团还有很多呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101337V#0205F#5P那种事情\n'
		'就只有魔兽\n'
		'才知道了吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101338V#0302F#5P没错没错。{wait}'
		'{page}'
		'#11101339V能将警备队的调查书补充完整，\n'
		'就已经算是不错的收获了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101340V#0004F#12P对啊……{wait}'
		'{page}'
		'#11101341V#0000F好了，总之，\n'
		'回去之前先向赛西儿姐姐报告吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101342V#0102F#6P说得也是呢……\n'
		'必须去向赛西儿小姐报告和道谢呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101343V#0309F#5P那么，\n'
		'我们就向护理师中心出发吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('CAM_DISTANCE', 26000, 2000),
	Insn('0x6F', b'y'),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(0), (-37600, 3000, 16800), 270),
	Insn('0x65', 1, 1),
	Insn('0x66', 2, 1),
	Insn('FLAG_SET', Flag(793)),
	Insn('QUEST', 63, Insn('TASK_SET', 16)),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('BGM_STOP', 3000),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'{\x00\x00'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][38] = [
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_SET_CHCP', Char(254), 30),
	Insn('CHAR_SET_FRAME', Char(254), 3),
	Insn('0x9D', Char(257), -35000, 3650, 16560, 1000, 5000),
	Insn('CHAR_SET_CHCP', Char(254), 255),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('SOUND_PLAY', 30, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('CHAR_SET_CHCP', Char(254), 30),
	Insn('CHAR_SET_FRAME', Char(254), 3),
	Insn('0x9D', Char(257), -34000, 4150, 16530, 1000, 5000),
	Insn('CHAR_SET_CHCP', Char(254), 255),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('SOUND_PLAY', 55, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-32689, 4150, 16470), 1000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(257), 0, 500),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('CHAR_ROTATE', Char(257), 90, 500),
	Insn('SLEEP', 1500),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('RETURN'),
]

data['code'][39] = [
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_CHCP', Char(254), 31),
	Insn('CHAR_SET_FRAME', Char(254), 3),
	Insn('0x9D', Char(260), -35140, 3650, 17520, 1000, 5000),
	Insn('CHAR_SET_CHCP', Char(254), 255),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('SOUND_PLAY', 31, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('CHAR_SET_CHCP', Char(254), 31),
	Insn('CHAR_SET_FRAME', Char(254), 3),
	Insn('0x9D', Char(260), -34130, 4150, 17590, 1000, 5000),
	Insn('CHAR_SET_CHCP', Char(254), 255),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('SOUND_PLAY', 54, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (-34130, 4150, 17090), 1000, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(260)),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (-34130, 4150, 17590), 1000, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('SLEEP', 1050),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('RETURN'),
]

data['code'][40] = [
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-34000, 4150, 16530), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('CHAR_SET_CHCP', Char(254), 30),
	Insn('CHAR_SET_FRAME', Char(254), 3),
	Insn('0x9D', Char(257), -35000, 3650, 16560, 1000, 5000),
	Insn('CHAR_SET_CHCP', Char(254), 255),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('SOUND_PLAY', 58, 0, 0, 100),
	Insn('SOUND_PLAY', 30, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('CHAR_SET_CHCP', Char(254), 30),
	Insn('CHAR_SET_FRAME', Char(254), 3),
	Insn('0x9D', Char(257), -36910, 3000, 16290, 1000, 5000),
	Insn('CHAR_SET_CHCP', Char(254), 255),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('SOUND_PLAY', 59, 0, 0, 100),
	Insn('SOUND_PLAY', 30, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('CHAR_FLAG1_UNSET', Char(257), 4),
	Insn('RETURN'),
]

data['code'][41] = [
	Insn('CHAR_ROTATE', Char(260), 270, 500),
	Insn('CHAR_SET_CHCP', Char(254), 31),
	Insn('CHAR_SET_FRAME', Char(254), 3),
	Insn('0x9D', Char(260), -35140, 3650, 17520, 1000, 5000),
	Insn('CHAR_SET_CHCP', Char(254), 255),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('SOUND_PLAY', 60, 0, 0, 100),
	Insn('SOUND_PLAY', 30, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_CHCP', Char(254), 31),
	Insn('CHAR_SET_FRAME', Char(254), 3),
	Insn('0x9D', Char(260), -37000, 3000, 17300, 1000, 5000),
	Insn('CHAR_SET_CHCP', Char(254), 255),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('SOUND_PLAY', 61, 0, 0, 100),
	Insn('SOUND_PLAY', 30, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('CHAR_FLAG1_UNSET', Char(260), 4),
	Insn('RETURN'),
]

data['code'][42] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-37000, 4000, 24200), 0),
	Insn('CAM_ROTATE', 45, 20, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(257), (-37000, 3000, 24200), 0),
	Insn('CHAR_SET_POS', Char(258), (-36800, 3000, 21670), 0),
	Insn('CHAR_SET_POS', Char(259), (-37670, 3000, 22640), 0),
	Insn('CHAR_SET_POS', Char(260), (-36210, 3000, 22900), 0),
	Insn('0x0D'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}木箱上面布满了灰尘。{wait}'
		'{page}'
		'看来很长一段时间\n'
		'都没有人管过了。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('EMOTE', Char(257), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101344V#0005F#2P（咦……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101345V#0105F#12P……怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101346V#0003F#2P没什么……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101347V#0008F#2P（如果从对面跳过来的话，\n'
		'\u3000应该会在上面留下足迹，不过……）{wait}'
		'{page}'
		'#11101348V（这上面还是布满了灰尘，也就是说，\n'
		'\u3000这种状态保持很长一段时间了……）{wait}'
		'{page}'
		'#11101349V#0000F（不过，这也不是什么非常\n'
		'\u3000奇怪的事情吧……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(0), (-37000, 3000, 23200), 0),
	Insn('CAM_OFFSET', (-37000, 4000, 23200), 0),
	Insn('CAM_ROTATE', 45, 23, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 26000, 0),
	Insn('0x66', 3, 1),
	Insn('FLAG_SET', Flag(794)),
	Insn('QUEST', 63, Insn('TASK_SET', 17)),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][43] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-40800, 4200, 21500), 0),
	Insn('CAM_ROTATE', 45, 20, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(257), (-40800, 3000, 21500), 270),
	Insn('CHAR_SET_POS', Char(258), (-38230, 3000, 22130), 270),
	Insn('CHAR_SET_POS', Char(259), (-39000, 3000, 20760), 270),
	Insn('CHAR_SET_POS', Char(260), (-39000, 3000, 22800), 270),
	Insn('0x0D'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101350V#0001F#5P（这是……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}扶手上部的油漆\n'
		'有多处剥落的痕迹。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101351V#0205F#11P罗伊德前辈……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101352V#0305F#11P怎么了吗？从刚才开始就若有所思的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101353V#0012F#5P没事……\n'
		'没什么大不了的。{wait}'
		'{page}'
		'#11101354V#0008F（嗯……\n'
		'\u3000似乎是最近才留下的痕迹。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(0), (-39800, 3000, 21500), 270),
	Insn('CAM_OFFSET', (-39800, 4000, 21500), 0),
	Insn('CAM_ROTATE', 45, 23, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 26000, 0),
	Insn('FLAG_SET', Flag(795)),
	Insn('QUEST', 63, Insn('TASK_SET', 18)),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][44] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
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
	Insn('CAM_OFFSET', (-34700, 4000, 20700), 0),
	Insn('CAM_ROTATE', 45, 20, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 26500, 0),
	Insn('CHAR_SET_POS', Char(257), (-35700, 3000, 20000), 270),
	Insn('CHAR_SET_POS', Char(258), (-35700, 3000, 21400), 270),
	Insn('CHAR_SET_POS', Char(259), (-34500, 3000, 20000), 270),
	Insn('CHAR_SET_POS', Char(260), (-34500, 3000, 21400), 270),
	Insn('CHAR_SET_POS', Char(310), (-37300, 3000, 20700), 270),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu01300.itp'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (-35700, 4000, 20700), 3000),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('CHAR_ROTATE', Char(310), 180, 300),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(310), 350, 500),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101577V#1301F#12P原来如此……\n'
		'魔兽就是从这里闯入的啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 310, 1, [
		Insn('0x95', Char(254), (-37280, 3000, 23830), 1000, 0),
	]),
	Insn('FORK_LOOP', 257, 1, [
		Insn('CHAR_WATCH', Char(257), Char(310), 500),
	]),
	Insn('FORK_LOOP', 258, 1, [
		Insn('CHAR_WATCH', Char(258), Char(310), 500),
	]),
	Insn('FORK_LOOP', 259, 1, [
		Insn('CHAR_WATCH', Char(259), Char(310), 500),
	]),
	Insn('FORK_LOOP', 260, 1, [
		Insn('CHAR_WATCH', Char(260), Char(310), 500),
	]),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101578V#0001F#12P虽然还不清楚魔兽\n'
		'为什么要进来……{wait}'
		'{page}'
		'#11101579V但以防万一，还是制定一下\n'
		'相关对策比较好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101580V#1308F#5P是啊，虽然时间上\n'
		'不太宽裕……{wait}'
		'{page}'
		'#11101581V#1301F我想至少可以装上一个\n'
		'防止魔兽入侵的防护栏。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101582V#0300F#11P嗯，光是装上那个，\n'
		'就会安全很多了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101583V#0200F#11P既要有一定的强度，\n'
		'又必须是可活动的……{wait}'
		'{page}'
		'#11101584V这所医院有那样的设备吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(310), 180, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101585V#1304F#5P嗯，记得用于野外治疗的设备中\n'
		'应该有这样的东西。{wait}'
		'{page}'
		'#11101586V#1300F和事务长商量一下，\n'
		'把它安装上去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(259), 1),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (-36180, 4000, 30470), 0),
	Insn('CAM_ROTATE', 36, 22, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 30450, 0),
	Insn('CAM_OFFSET', (-37360, 4000, 21820), 10000),
	Insn('OBJ_SET_FRAME', Object(255), 'model6', Insn('1', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'model5', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'CA02', Insn('0', 1)),
	Insn('LOAD_CHCP', 'chr/ch28000', 30),
	Insn('LOAD_CHCP', 'chr/ch29600', 31),
	Insn('LOAD_CHCP', 'chr/ch26000', 32),
	Insn('CHAR_FLAG1_UNSET', Char(34), 128),
	Insn('CHAR_FLAG2_UNSET', Char(34), 32768),
	Insn('CHAR_SET_CHCP', Char(34), 30),
	Insn('CHAR_SET_FRAME', Char(34), 0),
	Insn('CHAR_SET_POS', Char(34), (-34230, 3000, 24220), 90),
	Insn('CHAR_FLAG1_SET', Char(34), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(35), 128),
	Insn('CHAR_FLAG2_UNSET', Char(35), 32768),
	Insn('CHAR_SET_CHCP', Char(35), 31),
	Insn('CHAR_SET_FRAME', Char(35), 0),
	Insn('CHAR_SET_POS', Char(35), (-32750, 3000, 24110), 270),
	Insn('CHAR_FLAG1_SET', Char(35), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(36), 128),
	Insn('CHAR_FLAG2_UNSET', Char(36), 32768),
	Insn('CHAR_SET_CHCP', Char(36), 32),
	Insn('CHAR_SET_FRAME', Char(36), 0),
	Insn('CHAR_SET_POS', Char(36), (-36060, 3390, 24850), 0),
	Insn('CHAR_FLAG1_SET', Char(36), 32768),
	Insn('FORK_FUNC', Char(36), 0, Function((0, 46))),
	Insn('CHAR_SET_POS', Char(257), (-11300, 0, -700), 90),
	Insn('CHAR_SET_POS', Char(258), (-11300, 0, 700), 90),
	Insn('CHAR_SET_POS', Char(259), (-12700, 0, -700), 90),
	Insn('CHAR_SET_POS', Char(260), (-12700, 0, 700), 90),
	Insn('CHAR_SET_POS', Char(310), (-9000, 0, 0), 270),
	Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xfd\xd5\xc6', 25, 200, 0),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('FORK_QUIT', Char(36), 3),
	Insn('CROSSFADE', 2000),
	Insn('CAM_OFFSET', (-10300, 2000, 0), 0),
	Insn('CAM_ROTATE', 40, 20, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CAM_OFFSET', (-10300, 1000, 0), 4000),
	Insn('0x6F', b'\x01'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('TEXT_MESSAGE', Char(310), Text(
		'#11101587V呵呵，辛苦了。{wait}'
		'{page}'
		'#11101588V这样一来，大家就都可以安心了，\n'
		'真是多亏了你们呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101589V#0309F#6P没有那回事啦，过奖了丅{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101590V#0004F#6P哈哈，事实上\n'
		'我们并没有做什么。{wait}'
		'{page}'
		'#11101591V#0000F只是证明了是真的\n'
		'有魔兽入侵过而已。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101592V#1304F#11P但是，如果连魔兽是否入侵过都不确定，\n'
		'那么就无法采取正确的防范措施，\n'
		'问题也就一直得不到解决。{wait}'
		'{page}'
		'#11101593V#1300F我想你们总有一天\n'
		'一定能像亚里欧斯先生那样，\n'
		'漂亮地完成任务。{wait}'
		'{page}'
		'#11101594V#1309F姐姐向你们保证㈱{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101595V#0005F#6P赛西儿姐姐……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 2000, (10, 11, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101596V#0301F#6P感、感激不尽……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101597V#0109F#6P非常感谢，\n'
		'这番话对我们来说真是很大的鼓励。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101598V#0202F#6P……我们会加油的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101599V#1309F#11P呵呵……{wait}'
		'{page}'
		'#11101600V#1302F罗伊德，等我们两个都有时间了，\n'
		'再好好聚聚吧。{wait}'
		'{page}'
		'#11101601V我也想和你一起去扫墓呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101602V#0002F#6P……嗯，说得也是。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101603V#1304F#11P还有就是……{wait}'
		'{page}'
		'#11101604V#1302F如果你和艾莉或者小缇欧\n'
		'开始交往了，\n'
		'一定要跟我报告哦！{wait}'
		'{page}'
		'#11101605V#1309F我一定会好好为你庆祝的㈱{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 3)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101606V#0011F#6P不，我说啊……\n'
		'为什么会突然扯到这上面啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101607V#1306F#11P要不然，你和兰迪交往\n'
		'也是可以的……{wait}'
		'{page}'
		'#11101608V#1301F到时候要联系我哦！\n'
		'我会先看点那方面的书，\n'
		'做好心理准备的！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101609V#0006F#6P哪方面的书啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101610V#0309F#6P哎呀～！\n'
		'要是能让赛西儿小姐高兴的话，\n'
		'我是不介意的哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(260), 1000),
	Insn('SLEEP', 300),
	Insn('0x82', 0, 100, 3000, 200),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101611V#0011F#4S#11P喂，你给我介意一下啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101612V#1309F#11P呵呵，那么我\n'
		'就先失陪了。{wait}'
		'{page}'
		'#11101613V#1302F各位，回去的路上要小心哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101614V#0002F#6P──嗯。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101615V#0102F#6P承蒙您照顾了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_FUNC', Char(310), 3, Function((0, 45))),
	Insn('SLEEP', 3000),
	Insn('CAM_OFFSET', (-12000, 1000, 0), 4000),
	Insn('FORK_AWAIT', Char(310), 3),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101616V#0309F#6P哈，真好啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101617V#0104F#6P性格温和，又有包容力，\n'
		'也很可靠……{wait}'
		'{page}'
		'#11101618V#0102F呵呵，是非常优秀的人呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101619V#0009F#6P哈哈……\n'
		'你们能这么说，我很高兴。{wait}'
		'{page}'
		'#11101620V#0002F因为她比\n'
		'亲姐姐还要照顾我。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101621V#0204F#6P……那么，罗伊德前辈。{wait}'
		'{page}'
		'#11101622V#0202F你实际上跟赛西儿小姐是\n'
		'何种关系呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_WATCH', Char(257), Char(259), 600),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101623V#0011F#11P咦……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101624V#0104F#5P说得也是呢……\n'
		'我也有点在意。{wait}'
		'{page}'
		'#11101625V#0102F你看上去比平常\n'
		'更有弟弟的感觉呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101626V#0001F#11P那、那是什么意思啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101627V#0310F#5P罗伊德，你这家伙……！{wait}'
		'{page}'
		'#11101628V居然和那样优秀的姐姐\n'
		'关系甜蜜暧昧吗！？{wait}'
		'{page}'
		'#11101629V#0307F真是太让人羡慕了！\n'
		'请跟我交换身体吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101630V#0006F#11P怎么可能做得到。{wait}'
		'{page}'
		'#11101631V#0001F别说傻话了，\n'
		'差不多该回克洛斯贝尔了。{wait}'
		'{page}'
		'#11101632V太阳已经下山了……\n'
		'回去之后还要整理总结\n'
		'今天的调查报告书呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101633V#0211F#6P（……在转移话题了……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101634V#0111F#5P（嗯……做得真明显……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101635V#0310F#5P（可恶的罗伊德……！\n'
		'\u3000竟然把那么符合我喜好的人……！）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (14, 15, 250, 2)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 315, 1000),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('SLEEP', 300),
	Insn('0x82', 0, 100, 3000, 200),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101636V#0003F#4S#11P你们几个，不要在那里嘀咕个没完了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_FLAG1_SET', Char(34), 128),
	Insn('CHAR_FLAG2_SET', Char(34), 32768),
	Insn('CHAR_FLAG1_SET', Char(35), 128),
	Insn('CHAR_FLAG2_SET', Char(35), 32768),
	Insn('CHAR_FLAG1_SET', Char(36), 128),
	Insn('CHAR_FLAG2_SET', Char(36), 32768),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0x2F', b'5\x00'),
	Insn('CHAR_SET_POS', Char(0), (-11510, 0, -140), 270),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(13), 128),
	Insn('CHAR_FLAG2_UNSET', Char(13), 32768),
	Insn('CHAR_SET_POS', Char(13), (-26990, 0, 1930), 270),
	Insn('FLAG_SET', Flag(799)),
	Insn('QUEST', 63, Insn('TASK_SET', 20)),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][45] = [
	Insn('CHAR_ROTATE', Char(254), 90, 300),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (1500, 1000, 0), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('OBJ_FLAG_UNSET', Object(2), 16),
	Insn('0x71', Object(2), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x02\x00'),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (4500, 1000, 0), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('0x71', Object(2), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x02\x00'),
	Insn('OBJ_FLAG_SET', Object(2), 16),
	Insn('RETURN'),
]

data['code'][46] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('0x98', Char(254), (-1000, 0, 0), 2000, 0),
		Insn('SLEEP', 1000),
		Insn('0x98', Char(254), (-1000, 0, 0), 2000, 0),
		Insn('SLEEP', 1000),
		Insn('0x98', Char(254), (1000, 0, 0), 2000, 0),
		Insn('SLEEP', 1000),
		Insn('0x98', Char(254), (1000, 0, 0), 2000, 0),
		Insn('SLEEP', 1000),
	]),
	Insn('RETURN'),
]

data['code'][47] = [
	Insn('EVENT_BEGIN', 2),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('LOAD_CHCP', 'chr/ch20400', 30),
	Insn('LOAD_CHCP', 'chr/ch20300', 31),
	Insn('CHAR_SET_CHCP', Char(37), 30),
	Insn('CHAR_SET_FRAME', Char(37), 0),
	Insn('CHAR_SET_CHCP', Char(38), 31),
	Insn('CHAR_SET_FRAME', Char(38), 0),
	Insn('0x4B', Char(13), -1),
	Insn('CHAR_FLAG1_SET', Char(13), 64),
	Insn('EVENT_BEGIN', 0),
	Insn('CAM_OFFSET', (-59370, 1400, 2570), 0),
	Insn('CAM_ROTATE', 49, 15, 0, 0),
	Insn('0x6E', 460, 0),
	Insn('CAM_DISTANCE', 18500, 0),
	Insn('CHAR_SET_POS', Char(257), (-58140, 0, 2890), 0),
	Insn('CHAR_SET_POS', Char(258), (-57140, 0, 1620), 0),
	Insn('CHAR_SET_POS', Char(259), (-59300, 0, 1290), 0),
	Insn('CHAR_SET_POS', Char(260), (-58230, 0, 0), 0),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101637V#0000F#6P那么……\n'
		'我们就等巴士来吧。{wait}'
		'{page}'
		'#11101638V根据时刻表来看……\n'
		'下一班车大概在十五分钟之后到达呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101639V#0305F#4P话说这个真的很方便呢。{wait}'
		'{page}'
		'#11101640V似乎一直运行到\n'
		'晚上十一点。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101641V#0203F#6P车费也不贵……{wait}'
		'{page}'
		'#11101642V#0200F据说运营方是市政府，\n'
		'不知道能不能保证收支平衡呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(258), Char(259), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101643V#0102F呵呵，市政府对医院\n'
		'似乎也是非常重视的。{wait}'
		'{page}'
		'#11101644V毕竟财政方面还算宽裕，\n'
		'而且市民对这方面的需求也比较高。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(259), Char(258), 500),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101645V#0202F#6P原来如此……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(260), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101646V#0000F#5P不管怎么说，来医院的交通如此便利，\n'
		'实在是很值得庆幸呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (-59000, 1000, 2200), 0),
	Insn('CAM_ROTATE', 66, 30, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 23000, 0),
	Insn('CHAR_FLAG1_UNSET', Char(37), 128),
	Insn('CHAR_FLAG2_UNSET', Char(37), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(38), 128),
	Insn('CHAR_FLAG2_UNSET', Char(38), 32768),
	Insn('CHAR_SET_POS', Char(257), (-56600, 0, 3800), 180),
	Insn('CHAR_SET_POS', Char(258), (-56600, 0, 4900), 180),
	Insn('CHAR_SET_POS', Char(259), (-56600, 0, 6000), 180),
	Insn('CHAR_SET_POS', Char(260), (-56600, 0, 7100), 180),
	Insn('CHAR_SET_POS', Char(37), (-56600, 0, 8200), 180),
	Insn('CHAR_SET_POS', Char(38), (-56600, 0, 9300), 180),
	Insn('CHAR_SET_POS', Char(13), (-56600, 0, 10400), 180),
	Insn('OBJ_FLAG_SET', Object(7), 4096),
	Insn('OBJ_FLAG_UNSET', Object(7), 4),
	Insn('CHAR_FLAG1_UNSET', Char(28), 128),
	Insn('0x78', b'\x07', Char(28)),
	Insn('OBJ_SET_FRAME', Object(7), 'light', Insn('0', 1)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(28), (-75000, 0, 500), 90),
	Insn('0xD3', Char(28), 0, 90000, 0, 0),
	Insn('0x74', Object(7), 7680),
	Insn('0x71', Object(7), b'y\x00', 180, 32),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('FORK', 28, 1, [
		Insn('0x95', Char(254), (-59000, 0, 500), 4000, 0),
	]),
	Insn('SOUND_PLAY', 466, 0, 0, 100),
	Insn('SOUND_PLAY', 467, 0, 0, 100),
	Insn('FORK_AWAIT', Char(28), 1),
	Insn('0x71', Object(7), b'[\x00', 65656, 0),
	Insn('0x79', b'\x07\x00'),
	Insn('SLEEP', 300),
	Insn('0x71', Object(7), b'\x01\x00', 65566, 0),
	Insn('0x79', b'\x07\x00'),
	Insn('SOUND_PLAY', 464, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xd8\x0e\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 258, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00$\x13\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 80),
	Insn('FORK', 259, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00p\x17\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 0),
	Insn('FORK', 260, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xbc\x1b\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 200),
	Insn('FORK', 37, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x08 \x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 38, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00T$\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 13, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xa0(\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(37), 1),
	Insn('FORK_AWAIT', Char(38), 1),
	Insn('SOUND_PLAY', 463, 0, 0, 100),
	Insn('FORK_AWAIT', Char(13), 1),
	Insn('SLEEP', 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (-58690, 1000, 2150), 0),
	Insn('CAM_ROTATE', 75, 13, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 23360, 0),
	Insn('CHAR_SET_POS', Char(28), (-59000, 0, 500), 270),
	Insn('0xD3', Char(28), 0, 270000, 0, 0),
	Insn('CHAR_FLAG1_SET', Char(37), 128),
	Insn('CHAR_FLAG2_SET', Char(37), 32768),
	Insn('CHAR_FLAG1_SET', Char(38), 128),
	Insn('CHAR_FLAG2_SET', Char(38), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('0x70', Object(7), b'\x00\x00'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x71', Object(7), b'<\x00', 90, 0),
	Insn('SOUND_PLAY', 467, 0, 0, 100),
	Insn('SOUND_PLAY', 465, 0, 0, 100),
	Insn('0x79', b'\x07\x00'),
	Insn('CAM_OFFSET', (-62690, 1000, 2150), 4000),
	Insn('0x71', Object(7), b'y\x00', 180, 32),
	Insn('FORK', 28, 1, [
		Insn('0x95', Char(254), (-75000, 0, 500), 4000, 0),
	]),
	Insn('SLEEP', 2000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('0xB8', 0, 0),
	Insn('0x6F', b'\x01'),
	Insn('FORK_QUIT', Char(28), 1),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('0x49'),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'r1530', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][48] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch21100', 30),
	Insn('LOAD_CHCP', 'chr/ch21600', 31),
	Insn('LOAD_CHCP', 'chr/ch21800', 32),
	Insn('LOAD_CHCP', 'chr/ch21900', 33),
	Insn('CAM_OFFSET', (-51620, 2800, 4480), 0),
	Insn('CAM_ROTATE', 86, 17, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 23730, 0),
	Insn('CHAR_SET_POS', Char(257), (-50500, 0, -800), 270),
	Insn('CHAR_SET_POS', Char(239), (-51500, 0, -800), 270),
	Insn('CHAR_SET_POS', Char(339), (-52500, 0, -800), 270),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(239), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(339), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_CHCP', Char(37), 30),
	Insn('CHAR_SET_FRAME', Char(37), 0),
	Insn('CHAR_SET_COLOR', Char(37), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(37), 128),
	Insn('CHAR_FLAG2_UNSET', Char(37), 32768),
	Insn('CHAR_SET_CHCP', Char(38), 31),
	Insn('CHAR_SET_FRAME', Char(38), 0),
	Insn('CHAR_SET_COLOR', Char(38), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(38), 128),
	Insn('CHAR_FLAG2_UNSET', Char(38), 32768),
	Insn('CHAR_SET_CHCP', Char(39), 7),
	Insn('CHAR_SET_FRAME', Char(39), 0),
	Insn('CHAR_FLAG1_UNSET', Char(39), 128),
	Insn('CHAR_FLAG2_UNSET', Char(39), 32768),
	Insn('CHAR_SET_CHCP', Char(40), 32),
	Insn('CHAR_SET_FRAME', Char(40), 0),
	Insn('CHAR_FLAG1_UNSET', Char(40), 128),
	Insn('CHAR_FLAG2_UNSET', Char(40), 32768),
	Insn('CHAR_SET_CHCP', Char(41), 33),
	Insn('CHAR_SET_FRAME', Char(41), 0),
	Insn('CHAR_FLAG1_UNSET', Char(41), 128),
	Insn('CHAR_FLAG2_UNSET', Char(41), 32768),
	Insn('CHAR_SET_POS', Char(39), (-56040, 0, 5750), 180),
	Insn('CHAR_SET_POS', Char(40), (-56040, 0, 6950), 180),
	Insn('CHAR_SET_POS', Char(41), (-56040, 0, 8150), 180),
	Insn('0x4B', Char(29), -1),
	Insn('OBJ_FLAG_SET', Object(7), 4096),
	Insn('OBJ_FLAG_UNSET', Object(7), 4),
	Insn('CHAR_FLAG1_UNSET', Char(29), 128),
	Insn('0x78', b'\x07', Char(29)),
	Insn('OBJ_SET_FRAME', Object(7), 'light', Insn('0', 1)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(29), (-75000, 0, 500), 90),
	Insn('0xD3', Char(29), 0, 90000, 0, 0),
	Insn('0x74', Object(7), 7680),
	Insn('0x71', Object(7), b'y\x00', 180, 32),
	Insn('FORK', 29, 1, [
		Insn('0x95', Char(254), (-56000, 0, 500), 4000, 0),
	]),
	Insn('SOUND_PLAY', 466, 0, 0, 100),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (-51620, 200, 4480), 6000),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(29), 1),
	Insn('0x71', Object(7), b'[\x00', 65656, 0),
	Insn('0x79', b'\x07\x00'),
	Insn('0x71', Object(7), b'\x01\x00', 65566, 0),
	Insn('SOUND_PLAY', 464, 0, 0, 100),
	Insn('0x79', b'\x07\x00'),
	Insn('FORK_FUNC', Char(37), 3, Function((0, 49))),
	Insn('SLEEP', 750),
	Insn('FORK_FUNC', Char(38), 3, Function((0, 49))),
	Insn('SLEEP', 750),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 50))),
	Insn('SLEEP', 750),
	Insn('FORK_FUNC', Char(339), 3, Function((0, 52))),
	Insn('SLEEP', 750),
	Insn('FORK_FUNC', Char(239), 3, Function((0, 51))),
	Insn('SLEEP', 750),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(39), 3, Function((0, 53))),
	Insn('SLEEP', 350),
	Insn('FORK_FUNC', Char(40), 3, Function((0, 53))),
	Insn('SLEEP', 350),
	Insn('FORK_FUNC', Char(41), 3, Function((0, 53))),
	Insn('SLEEP', 350),
	Insn('SLEEP', 1500),
	Insn('FORK_QUIT', Char(39), 3),
	Insn('FORK_QUIT', Char(40), 3),
	Insn('FORK_QUIT', Char(41), 3),
	Insn('CHAR_FLAG1_SET', Char(39), 128),
	Insn('CHAR_FLAG2_SET', Char(39), 32768),
	Insn('CHAR_FLAG1_SET', Char(40), 128),
	Insn('CHAR_FLAG2_SET', Char(40), 32768),
	Insn('CHAR_FLAG1_SET', Char(41), 128),
	Insn('CHAR_FLAG2_SET', Char(41), 32768),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-46640, 200, 360), 0),
	Insn('CAM_ROTATE', 40, 24, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 21360, 0),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(339), 3),
	Insn('FORK_AWAIT', Char(239), 3),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600689V#1109F#6P嘿嘿……\n'
		'实在是太开心了！{wait}'
		'{page}'
		'#13600690V#1110F虽然走路很开心，\n'
		'但坐巴士也很开心呢！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600691V#0014F#11P哈哈，这样啊。{wait}'
		'{page}'
		'#13600692V#0008F（琪雅看起来好像是\n'
		'\u3000第一次坐导力车呢……）{wait}'
		'{page}'
		'#13600693V#0001F（莫非她也没坐过\n'
		'\u3000导力列车或飞行船吗……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600694V#1105F#6P话说……\n'
		'这里就是叫做医院的地方吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600695V#0004F#11P是啊，叫做医科大学，\n'
		'也是一个进行各种研究的医院哦。{wait}'
		'{page}'
		'#13600696V#0000F说不定可以帮琪雅把\n'
		'忘记的事情想起来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(339), Text(
				'#13600697V#1106F#6P嗯……琪雅其实\n'
				'并不在乎想不想得起来。{wait}'
				'{page}'
				'#13600698V#1100F但如果琪雅想起来的话，\n'
				'罗伊德和艾莉会更高兴吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(339), Text(
				'#13600697V#1106F#6P嗯……琪雅其实\n'
				'并不在乎想不想得起来。{wait}'
				'{page}'
				'#13600699V#1100F但如果琪雅想起来的话，\n'
				'罗伊德和缇欧会更高兴吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(339), Text(
				'#13600697V#1106F#6P嗯……琪雅其实\n'
				'并不在乎想不想得起来。{wait}'
				'{page}'
				'#13600700V#1100F但如果琪雅想起来的话，\n'
				'罗伊德和兰迪会更高兴吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(239), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600701V#0002F#11P嗯、嗯……\n'
		'当然会更高兴。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600702V#0104F#5P琪雅肯定有许多\n'
				'非常珍贵的回忆。{wait}'
				'{page}'
				'#13600703V#0102F所以要加油\n'
				'想起来哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600704V#0203F#5P……琪雅应该会有非常\n'
				'珍贵的回忆。{wait}'
				'{page}'
				'#13600705V#0202F所以努力\n'
				'加油回想起来吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600706V#0306F#5P小琪应该有很多\n'
				'珍贵的回忆。{wait}'
				'{page}'
				'#13600707V#0300F不取回来怎么行呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600708V#1104F#6P嗯，我知道了。{wait}'
		'{page}'
		'#13600709V#1110F琪雅会加油\n'
		'想起来的！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600710V#0004F#11P嗯，就是要有那股气势。{wait}'
		'{page}'
		'#13600711V#0000F……但是，\n'
		'也不要太勉强哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600712V#1109F#6P嗯！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600713V#0102F#5P呵呵，那么\n'
				'去接待处问问关于\n'
				'『神经科』的事吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600714V#0202F#5P……那么去\n'
				'接待处问问关于\n'
				'『神经科』的事吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600715V#0302F#5P好了，那么\n'
				'去接待处问问关于\n'
				'『神经科』的事吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 471, 0, 0, 100),
	Insn('CHAR_FLAG1_SET', Char(37), 128),
	Insn('CHAR_FLAG2_SET', Char(37), 32768),
	Insn('CHAR_FLAG1_SET', Char(38), 128),
	Insn('CHAR_FLAG2_SET', Char(38), 32768),
	Insn('0x49'),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0xD5', 33),
	Insn('CHAR_SET_POS', Char(0), (-48100, 0, -400), 90),
	Insn('0xB5', b'\x01\x01\x80\x00'),
	Insn('FLAG_SET', Flag(1348)),
	Insn('QUEST', 72, Insn('TASK_SET', 6)),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('0x70', Object(7), b'\x00\x00'),
	Insn('0x71', Object(7), b'y\x00', 180, 32),
	Insn('0x4C', Char(29), -1),
	Insn('RETURN'),
]

data['code'][49] = [
	Insn('CHAR_SET_POS', Char(254), (-55990, 600, 1320), 270),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-56010, 0, 4180), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-50520, 0, 3410), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-46150, 0, 30), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-33950, 0, -50), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('RETURN'),
]

data['code'][50] = [
	Insn('CHAR_FLAG1_SET', Char(254), 4),
	Insn('CHAR_SET_POS', Char(254), (-55990, 600, 1320), 270),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-56010, 0, 4180), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-50520, 0, 3410), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-47080, 0, -1280), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('CHAR_ROTATE', Char(254), 270, 500),
	Insn('CHAR_FLAG1_UNSET', Char(254), 4),
	Insn('RETURN'),
]

data['code'][51] = [
	Insn('CHAR_FLAG1_SET', Char(254), 4),
	Insn('CHAR_SET_POS', Char(254), (-55990, 600, 1320), 270),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-56010, 0, 4180), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-50520, 0, 3410), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-47530, 0, 180), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('CHAR_ROTATE', Char(254), 225, 500),
	Insn('CHAR_FLAG1_UNSET', Char(254), 4),
	Insn('RETURN'),
]

data['code'][52] = [
	Insn('CHAR_FLAG1_SET', Char(254), 4),
	Insn('CHAR_SET_POS', Char(254), (-55990, 600, 1320), 270),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-56010, 0, 4180), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-50520, 0, 3410), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-48510, 0, -1230), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('CHAR_ROTATE', Char(254), 90, 500),
	Insn('CHAR_FLAG1_UNSET', Char(254), 4),
	Insn('RETURN'),
]

data['code'][53] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-56060, 0, 3950), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-55990, 600, 1320), 2000, 0),
	]),
	Insn('SLEEP', 1200),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('RETURN'),
]

data['code'][54] = [
	Insn('SLEEP', 7000),
	Insn('OBJ_FLAG_UNSET', Object(6), 16),
	Insn('0x71', Object(6), b'\x00\x00', 10, 0),
	Insn('0x79', b'\x06\x00'),
	Insn('RETURN'),
]

data['code'][55] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('LOAD_CHCP', 'chr/ch05300', 30),
	Insn('CAM_OFFSET', (-22700, 1000, -500), 0),
	Insn('CAM_ROTATE', 45, 21, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 24000, 0),
	Insn('CHAR_SET_POS', Char(257), (-26700, 0, -1100), 90),
	Insn('CHAR_SET_POS', Char(339), (-28000, 0, -500), 90),
	Insn('CHAR_SET_POS', Char(239), (-26700, 0, 100), 90),
	Insn('CHAR_SET_POS', Char(30), (-9000, 0, -500), 270),
	Insn('CHAR_SET_CHCP', Char(30), 30),
	Insn('CHAR_SET_FRAME', Char(30), 0),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('0x4B', Char(30), -1),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu01300.itp'),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('CHAR_FLAG1_SET', Char(14), 128),
	Insn('CHAR_FLAG2_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(18), 128),
	Insn('CHAR_FLAG2_SET', Char(18), 32768),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xd0\x07\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 239, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xd0\x07\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 339, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xd0\x07\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(339), 1),
	Insn('FORK_AWAIT', Char(239), 1),
	Insn('0x0D'),
	Insn('TEXT_TALK2', Char(30), Translate('女性的声音'), Text(
		'#13600716V咦……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(239), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(339), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600717V#0002F#6P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-14700, 1000, -500), 3000),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 500),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-21000, 1000, -500), 0),
	Insn('CAM_DISTANCE', 23000, 0),
	Insn('0x98', Char(30), (-6000, 0, 0), 0, 0),
	Insn('FORK', 30, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x94\x11\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xb8\x0b\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 239, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xb8\x0b\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 339, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xb8\x0b\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(339), 1),
	Insn('FORK_AWAIT', Char(239), 1),
	Insn('FORK_AWAIT', Char(30), 1),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600718V#0000F#6P赛西儿姐姐……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600719V#0102F#6P赛西儿小姐，\n'
				'您好，好久不见了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600720V#0202F#6P……好久不见了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600721V#0309F#6P哦哦，赛西儿小姐！\n'
				'你好，好久不见了！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 500),
	Insn('TEXT_MESSAGE', Char(30), Text(
		'#13600722V呵呵……\n'
		'你们两个都很有精神呢。{wait}'
		'{page}'
		'#13600723V纪念庆典期间辛苦你们了。\n'
		'很多事情忙得不可开交吧？{wait}'
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
		'#13600724V#0012F#6P哈哈……算是吧。{wait}'
		'{page}'
		'#13600725V#0006F说实话，那五天的\n'
		'工作量真不是一般的大。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600726V#0106F#6P而且在那之后的一周里\n'
				'也发生了很多事情……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600727V#0206F#6P而且在那之后的一周里\n'
				'也发生了很多事情……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600728V#0306F#6P而且在那之后的一周里\n'
				'也发生了很多事情……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(30), Text(
		'#13600729V#1302F#11P哎呀，但是你们两人看上去\n'
		'并不是很疲倦呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(30), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(30), Text(
		'#13600730V#1305F#11P啊，这孩子是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(30), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('FORK', 339, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xf4\x01\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(339), 1),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600731V#1110F#6P那个那个，罗伊德。{wait}'
		'{page}'
		'#13600732V这个姐姐也是\n'
		'罗伊德的朋友吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(339), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 239, 1, [
		Insn('CHAR_WATCH', Char(254), Char(339), 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600733V#0000F#11P嗯，没错哦。{wait}'
		'{page}'
		'#13600734V她是赛西儿姐姐，\n'
		'就像我的\n'
		'亲姐姐一样──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE_STOP', Char(30)),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(30), Text(
		'#13600735V#1303F#11P#40W……怎、怎么会……{wait}'
		'{page}'
		'#13600736V#1308F#40W罗、罗伊德居然\n'
		'一直……瞒着我……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(30), 500),
	]),
	Insn('FORK', 239, 1, [
		Insn('CHAR_WATCH', Char(254), Char(30), 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(239), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600737V#0005F#6P咦……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 500),
	Insn('0x82', 200, 0, 3000, 300),
	Insn('TEXT_TALK', Char(30), Text(
		'#13600738V#1306F#11P罗伊德居然背着我\n'
		'结婚了……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(239), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('0x82', 200, 0, 3000, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600739V#0011F#4S#6P啊！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(30), Text(
		'#13600740V#1303F#11P嗯，不用对我隐瞒了！{wait}'
		'{page}'
		'#13600741V#1301F小朋友，\n'
		'你叫什么名字！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600742V#1110F#6P我叫琪雅。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(30), Text(
				'#13600743V#1309F#11P琪雅啊……\n'
				'呵呵，真是可爱的名字。{wait}'
				'{page}'
				'#13600744V#1308F不过长得不太像罗伊德呢，\n'
				'莫非是像母亲……{wait}'
				'{page}'
				'#13600745V但是，长得也不像\n'
				'艾莉呀……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#13600746V#0112F#6P那、那个，赛西儿小姐……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(30), Text(
				'#13600743V#1309F#11P琪雅啊……\n'
				'呵呵，真是可爱的名字。{wait}'
				'{page}'
				'#13600744V#1308F不过长得不太像罗伊德呢，\n'
				'莫非是像母亲……{wait}'
				'{page}'
				'#13600747V但是，长得也不像\n'
				'小缇欧呀……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#13600748V#0211F#6P那个，赛西儿小姐……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(30), Text(
				'#13600743V#1309F#11P琪雅啊……\n'
				'呵呵，真是可爱的名字。{wait}'
				'{page}'
				'#13600744V#1308F不过长得不太像罗伊德呢，\n'
				'莫非是像母亲……{wait}'
				'{page}'
				'#13600749V#1301F还是说，是兰迪跟其他女人\n'
				'生的孩子吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#13600750V#0305F#6P等、等等，赛西儿小姐……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600751V#0012F#6P啊啊啊啊！\n'
		'你冷静一点啦！{wait}'
		'{page}'
		'#13600752V#0011F说什么我是琪雅的父亲……\n'
		'从年龄上来看，\n'
		'也根本不可能吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(30), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1100),
	Insn('EMOTE', Char(30), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(30)),
	Insn('TEXT_TALK', Char(30), Text(
		'#13600753V#1305F#11P咦……{wait}'
		'{page}'
		'#13600754V#1309F……仔细一想的话，\n'
		'说得也是呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(239), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600755V#0012F#6P这、这种事根本不用仔细想\n'
		'也能明白吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600756V#0106F#6P赛西儿小姐……\n'
				'有点天然呆啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600757V#0206F#6P赛西儿小姐……\n'
				'没想到竟然那么天然呆。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600758V#0309F#6P赛西儿小姐……\n'
				'这种天然呆的性格也好棒啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600759V#1105F#6P咦咦～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('CAM_DISTANCE', 24000, 2000),
	Insn('0x6F', b'\x10'),
	Insn('0x0D'),
	Insn('CHAR_FLAG1_UNSET', Char(14), 128),
	Insn('CHAR_FLAG2_UNSET', Char(14), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(18), 128),
	Insn('CHAR_FLAG2_UNSET', Char(18), 32768),
	Insn('FLAG_SET', Flag(737)),
	Insn('NEW_SCENE', 't1510', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][56] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('EFF_STOP', (ResId(8), 0)),
	Insn('LOAD_CHCP', 'chr/ch08200', 30),
	Insn('LOAD_CHCP', 'chr/ch05400', 31),
	Insn('CAM_OFFSET', (1400, 1700, 530), 0),
	Insn('CAM_ROTATE', 46, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 31300, 0),
	Insn('CHAR_SET_POS', Char(257), (100000, 0, 0), 0),
	Insn('CHAR_SET_POS', Char(239), (100000, 0, 0), 0),
	Insn('CHAR_SET_CHCP', Char(32), 30),
	Insn('CHAR_SET_FRAME', Char(32), 0),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_POS', Char(32), (4000, 1000, 0), 270),
	Insn('CHAR_SET_COLOR', Char(32), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(32), 4),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_SET_CHCP', Char(31), 31),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_POS', Char(31), (-23770, -1000, -26000), 180),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_DISTANCE', 29800, 2500),
	Insn('0x6F', b'\x10'),
	Insn('0x0D'),
	Insn('OBJ_FLAG_UNSET', Object(2), 16),
	Insn('0x71', Object(2), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x02\x00'),
	Insn('FORK', 32, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xac\r\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK', 32, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(32), 1),
	Insn('FORK_AWAIT', Char(32), 2),
	Insn('0x71', Object(2), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x02\x00'),
	Insn('OBJ_FLAG_SET', Object(2), 16),
	Insn('TEXT_TALK', Char(32), Text(
		'#13600987V#1101F#11P真是的，罗伊德\n'
		'完全不了解别人的心情。{wait}'
		'{page}'
		'#13600988V#1108F……记忆那种东西，\n'
		'即使没有也无所谓的……{wait}'
		'{page}'
		'#13600989V#1106F为什么大家\n'
		'都那么在意呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('CAM_OFFSET', (-1400, 1700, 530), 5000),
	Insn('FORK', 32, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x000u\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 3000),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-24820, 1700, -1120), 0),
	Insn('CAM_ROTATE', 46, 22, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 29800, 0),
	Insn('CAM_DISTANCE', 25490, 3500),
	Insn('FORK_QUIT', Char(32), 1),
	Insn('CHAR_SET_POS', Char(32), (-17660, 0, -310), 270),
	Insn('FORK', 32, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x9c\x18\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(32), 1),
	Insn('EMOTE', Char(32), 0, 1700, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('CHAR_ROTATE', Char(32), 180, 300),
	Insn('SLEEP', 750),
	Insn('CHAR_ROTATE', Char(32), 270, 500),
	Insn('CHAR_ROTATE', Char(32), 0, 500),
	Insn('SLEEP', 750),
	Insn('CHAR_ROTATE', Char(32), 270, 300),
	Insn('SLEEP', 750),
	Insn('TEXT_TALK', Char(32), Text(
		'#13600990V#1105F#11P咦咦……{wait}'
		'{page}'
		'#13600991V这里是哪里啊？{wait}'
		'{page}'
		'#13600992V？？？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(32), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(32)),
	Insn('CHAR_ROTATE', Char(32), 180, 300),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(32), Text(
		'#13600993V#1114F#5P嗯……{wait}'
		'{page}'
		'#13600994V#1101F……琪雅这是\n'
		'迷路了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 4000),
	Insn('EMOTE', Char(32), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(32), Text(
		'#13600995V#1105F#5P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-24820, 1700, -4120), 3000),
	Insn('SLEEP', 500),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('SLEEP', 1000),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'\x0b\x02\x00'),
	Insn('CAM_OFFSET', (-24150, 0, -34360), 0),
	Insn('CAM_ROTATE', 46, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 22830, 0),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (-24020, 0, -26990), 6000),
	Insn('CAM_DISTANCE', 20600, 6000),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(31), Text(
		'#13600996V#1502F#5P……呵呵，好清爽的风啊…………{wait}'
		'{page}'
		'#13600997V爸爸……\n'
		'今天什么时候过来呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_POS', Char(32), (-24000, 0, -14410), 180),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(32), Text(
		'#13600998V喂喂！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(31), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(31), 0, 400),
	Insn('CAM_OFFSET', (-23780, 0, -25230), 2500),
	Insn('FORK', 32, 1, [
		Insn('0x95', Char(254), (-23770, -1000, -24500), 3000, 0),
	]),
	Insn('FORK_AWAIT', Char(32), 1),
	Insn('TEXT_TALK', Char(31), Text(
		'#13600999V#1505F#12P你是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601000V#1110F#5P那个，从这里能看到什么吗？{wait}'
		'{page}'
		'#13601001V#1109F莫非\n'
		'有鱼在水里游吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601002V#1500F#12P呵呵……{wait}'
		'{page}'
		'#13601003V虽然我看不见，\n'
		'但我想应该有鱼在水里游哦。{wait}'
		'{page}'
		'#13601004V有时候能听到\n'
		'鱼儿欢快地跳出水面的声音……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(32), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CAM_ROTATE', 46, 14, 0, 1500),
	Insn('CAM_OFFSET', (-24970, 0, -26730), 1500),
	Insn('FORK', 32, 1, [
		Insn('0x95', Char(254), (-24860, -1000, -26000), 2000, 0),
	]),
	Insn('FORK_LOOP', 31, 1, [
		Insn('CHAR_WATCH', Char(254), Char(32), 400),
	]),
	Insn('FORK_AWAIT', Char(32), 1),
	Insn('FORK_QUIT', Char(31), 1),
	Insn('CHAR_ROTATE', Char(32), 180, 500),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(32), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601005V#1105F#5P啊，真的呢！\n'
		'好像有很多哦！{wait}'
		'{page}'
		'#13601006V#1109F嗯，琪雅\n'
		'也想钓鱼。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(31), 270, 400),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601007V#1500F#11P呵呵……\n'
		'你叫琪雅吗？{wait}'
		'{page}'
		'#13601008V我是滴，\n'
		'滴丄马克莱因。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(32), 90, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601009V#1111F#5P小滴……小滴……{wait}'
		'{page}'
		'#13601010V#1109F嗯，真是好名字！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601011V#1500F#11P呵呵，谢谢。{wait}'
		'{page}'
		'#13601012V我觉得琪雅的名字\n'
		'也很棒。{wait}'
		'{page}'
		'#13601013V你是来这里探病的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601014V#1105F#5P啊，不是哦。{wait}'
		'{page}'
		'#13601015V#1108F琪雅是来\n'
		'让医生找回记忆的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601016V#1505F#11P记忆……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601017V#1101F#5P那个戴眼镜的医生\n'
		'要让琪雅跟罗伊德他们分开，\n'
		'所以琪雅就逃了出来。{wait}'
		'{page}'
		'#13601018V#1104F呵呵，\n'
		'也就是所谓的战略性撤退。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(31), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601019V#1508F#11P你说逃出来……{wait}'
		'{page}'
		'#13601020V#1505F（咦，罗伊德他们？\n'
		'\u3000莫非……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601021V#1110F#5P喂喂，小滴。{wait}'
		'{page}'
		'#13601022V为什么从刚才开始\n'
		'就一直闭着眼睛呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601023V#1500F#11P啊，那个……{wait}'
		'{page}'
		'#13601024V因为我的眼睛看不见东西，\n'
		'所以才会住院的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601025V#1105F#5P哦，原来是这样啊。{wait}'
		'{page}'
		'#13601026V#1100F琪雅也没有记忆，\n'
		'我们同病相怜呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(31), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601027V#1505F#11P啊……记忆……{wait}'
		'{page}'
		'#13601028V#1508F嗯，原来是这样啊……{wait}'
		'{page}'
		'#13601029V……你什么都记不起来了吗？\n'
		'爸爸、妈妈之类的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601030V#1100F#5P……嗯，好像是这样的。{wait}'
		'{page}'
		'#13601031V#1109F但是，有罗伊德他们在，\n'
		'所以一点也不寂寞！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601032V#1500F#11P呵呵，这样啊……{wait}'
		'{page}'
		'#13601033V#1508F……我也一样，\n'
		'虽然妈妈已经不在人世了……{wait}'
		'{page}'
		'#13601034V#1510F但我还有爸爸在，\n'
		'医院的各位也都很温柔，\n'
		'所以应该是不寂寞的吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 19600, 3000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('SLEEP', 1000),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('FLAG_SET', Flag(1352)),
	Insn('FLAG_SET', Flag(1359)),
	Insn('BGM_STOP', 5000),
	Insn('BGM_WAIT'),
	Insn('EVENT_END', 5),
	Insn('NEW_SCENE', 't1600', b'h\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][57] = [
	Insn('EVENT_BEGIN', 2),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('EVENT_BEGIN', 0),
	Insn('LOAD_CHCP', 'chr/ch08200', 30),
	Insn('LOAD_CHCP', 'chr/ch05400', 31),
	Insn('LOAD_CHCP', 'chr/ch02400', 32),
	Insn('LOAD_CHCP', 'apl/ch50384', 33),
	Insn('CAM_OFFSET', (-23910, 800, -12480), 0),
	Insn('CAM_ROTATE', 41, 15, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 23640, 0),
	Insn('CHAR_SET_POS', Char(257), (-23500, 0, -15070), 180),
	Insn('CHAR_SET_POS', Char(239), (-24520, 0, -14530), 180),
	Insn('CHAR_SET_CHCP', Char(32), 30),
	Insn('CHAR_SET_FRAME', Char(32), 0),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_POS', Char(32), (-24570, -1000, -26000), 90),
	Insn('CHAR_SET_CHCP', Char(31), 31),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_POS', Char(31), (-23240, -1000, -26000), 270),
	Insn('CHAR_SET_CHCP', Char(33), 32),
	Insn('CHAR_SET_FRAME', Char(33), 0),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_POS', Char(33), (-23910, 0, -2470), 180),
	Insn('CHAR_SET_COLOR', Char(33), Color(0x00FFFFFF), 0),
	Insn('0xB5', b'\x00\x02\x80\x00'),
	Insn('BGM_STOP', 4000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (-23910, 800, -15480), 2500),
	Insn('0x6F', b'y'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13601035V#0000F#5P找到了……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13601036V#0102F#5P终于找到了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13601037V#0202F#5P终于找到了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13601038V#0300F#5P原来在这里啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('0x5A'),
	Insn('CROSSFADE', 1000),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(239), Color(0x00FFFFFF), 0),
	Insn('CAM_OFFSET', (-24970, 0, -26730), 0),
	Insn('CAM_ROTATE', 46, 14, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 20600, 0),
	Insn('CAM_DISTANCE', 20000, 20000),
	Insn('0x0D'),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'\x02\x02\x00'),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601039V#1110F#5P还有、还有哦！{wait}'
		'{page}'
		'#13601040V还有一条叫赛特的大狗，\n'
		'它非常非常大哦！{wait}'
		'{page}'
		'#13601041V平时总是一副很骄傲的样子，\n'
		'全身毛茸茸的。{wait}'
		'{page}'
		'#13601042V#1109F如果骑在它背上的话，\n'
		'肯定会非常舒服呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601043V#1500F#11P呵呵，这样啊。{wait}'
		'{page}'
		'#13601044V#1502F很大的狗……\n'
		'身上的毛应该很柔软吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601045V#1110F#5P小滴偶尔也会\n'
		'来市里吧？{wait}'
		'{page}'
		'#13601046V到时候来一起\n'
		'跟赛特玩吧！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601047V#1500F#11P啊哈哈……嗯。\n'
		'是不是该拜托下爸爸呢？{wait}'
		'{page}'
		'#13601048V#1505F啊，拜托艾丝蒂尔他们的话，\n'
		'应该会陪我去的吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(32), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601049V#1105F#5P啊，艾丝蒂尔就是\n'
		'那个游击士姐姐吧？{wait}'
		'{page}'
		'#13601050V#1100F小滴也认识她啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601051V#1500F#11P呵呵，有时去市里时，\n'
		'她会陪我去买东西。{wait}'
		'{page}'
		'#13601052V因为爸爸一直都很忙……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('CROSSFADE', 1000),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(239), Color(0xFFFFFFFF), 0),
	Insn('CAM_OFFSET', (-23930, 900, -16040), 0),
	Insn('CAM_ROTATE', 47, 17, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 23640, 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13601053V#0002F#5P哈哈……\n'
		'原来是和小滴在一起啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13601054V#0109F#5P呵呵，好像\n'
				'聊得很开心呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13601055V#0204F#5P……聊得\n'
				'非常开心呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13601056V#0309F#5P话说她们似乎聊得\n'
				'非常起劲呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK2', Char(33), Translate('男人的声音'), Text(
		'#13601057V#4P呵呵……\n'
		'小孩子都是很快就能互相熟悉起来的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(239), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 359, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 239, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('CAM_OFFSET', (-23930, 900, -14040), 5000),
	Insn('CHAR_SET_COLOR', Char(33), Color(0xFFFFFFFF), 0),
	Insn('FORK', 33, 1, [
		Insn('0x95', Char(254), (-23910, 0, -12470), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(33), 1),
	Insn('0x6F', b'\x01'),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(239), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#13601058V#0005F#12P亚、亚里欧斯先生……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13601059V#0104F#12P上次的事件承蒙您照顾了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13601060V#0204F#12P上次的事件真是感激不尽……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13601061V#0303F#12P上次的事件谢谢了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(33), Text(
		'#13601062V#1404F#5P之前那件事，\n'
		'你们并没有必要觉得欠我人情。{wait}'
		'{page}'
		'#13601063V#1400F话说回来──\n'
		'那个女孩就是……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13601064V#0000F#12P是啊，您是从蜜雪儿先生\n'
		'那里听说的吧。{wait}'
		'{page}'
		'#13601065V#0004F嗯……\n'
		'她的名字叫做琪雅。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(33), Text(
		'#13601066V#1405F#5P是吗……{wait}'
		'{page}'
		'#13601067V………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('EMOTE', Char(239), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(257), Text(
		'#13601068V#0005F#12P那个……\n'
		'琪雅怎么了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13601069V#0101F#12P难道您和琪雅以前见过面……！？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13601070V#0201F#12P难道您以前见过琪雅……！？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13601071V#0301F#12P难道您以前见过琪雅……！？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(33), Text(
		'#13601072V#1402F#5P没有……\n'
		'只是觉得她是个很不可思议的女孩子。{wait}'
		'{page}'
		'#13601073V#1404F虽然我女儿──小滴是个懂礼貌，\n'
		'而且待人随和的孩子，\n'
		'但她有时会对人客气过头。{wait}'
		'{page}'
		'#13601074V因此跟同龄的孩子\n'
		'不怎么亲近……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13601075V#0012F#12P啊，原来如此。{wait}'
		'{page}'
		'#13601076V#0002F……感觉她们\n'
		'两个相处得很好呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(33), Text(
		'#13601077V#1402F#5P对啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(33), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(33)),
	Insn('TEXT_TALK', Char(33), Text(
		'#13601078V#1403F#5P……虽然不知道那个女孩子\n'
		'究竟有什么样的背景。{wait}'
		'{page}'
		'#13601079V#1400F但是既然与她扯上关系了，\n'
		'你们就要负责任到底。{wait}'
		'{page}'
		'#13601080V#1404F而且……\n'
		'还要认真将她照顾好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13601081V#0005F#12P啊……{wait}'
		'{page}'
		'#13601082V#0004F是，我也正有此意。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601083V#1505F#1P……爸爸？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(32), Text(
				'#13601084V#1107F#1P啊……\n'
				'罗伊德和艾莉！？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(32), Text(
				'#13601085V#1107F#1P啊……\n'
				'罗伊德和缇欧！？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(32), Text(
				'#13601086V#1107F#1P啊……\n'
				'罗伊德和兰迪！？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 181, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 239, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#13601087V#0012F#5P发现我们了啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(33), Text(
		'#13601088V#1402F#5P……嗯。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-24710, 200, -23740), 0),
	Insn('CAM_ROTATE', 44, 16, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 27550, 0),
	Insn('CAM_DISTANCE', 24550, 3000),
	Insn('CHAR_SET_POS', Char(31), (-23760, -1000, -24640), 0),
	Insn('CHAR_SET_POS', Char(32), (-25130, -1000, -24700), 45),
	Insn('CHAR_SET_POS', Char(257), (-24850, -1000, -17000), 180),
	Insn('CHAR_SET_POS', Char(239), (-26280, -1000, -17870), 180),
	Insn('CHAR_SET_POS', Char(33), (-23900, -1000, -18210), 180),
	Insn('FORK_LOOP', 32, 2, [
		Insn('CHAR_WATCH', Char(254), Char(33), 500),
	]),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x88\x13\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 239, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x88\x13\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 33, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x88\x13\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(239), 1),
	Insn('FORK', 239, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 300),
	]),
	Insn('FORK_AWAIT', Char(239), 1),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(33), 1),
	Insn('FORK_QUIT', Char(32), 2),
	Insn('0x6F', b'y'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601089V#1500F#12P爸爸，欢迎回来。{wait}'
		'{page}'
		'#13601090V工作辛苦吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(33), Text(
		'#13601091V#1404F#5P不……\n'
		'这次并不辛苦。{wait}'
		'{page}'
		'#13601092V#1402F我回来了，小滴。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601093V#1105F#6P这个人就是\n'
		'小滴的爸爸吗？{wait}'
		'{page}'
		'#13601094V#1110F好高啊。{wait}'
		'{page}'
		'#13601095V#1109F而且看起来好像很强！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(31), 270, 400),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601096V#1502F#11P嘿嘿……是吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(31), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 31, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 400),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 33, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 400),
	]),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601097V#1500F#12P还有两位也是……\n'
		'傍晚好，好久不见了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13601098V#0002F#5P嗯，好久不见。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13601099V#0109F#5P呵呵，好像和琪雅\n'
				'成为朋友了吧？谢谢你哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13601100V#0202F#5P谢谢你和琪雅\n'
				'做朋友哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13601101V#0309F#5P哈哈，谢谢你跟小琪\n'
				'做朋友啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601102V#1502F#12P啊，不，我才应该感谢\n'
		'琪雅跟我成为朋友呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(32), 0, 500),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601103V#1103F#12P……罗伊德。{wait}'
		'{page}'
		'#13601104V#1101F琪雅绝对不要\n'
		'搬到这里来哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13601105V#0006F#5P嗯，琪雅的决心我已经充分理解了。{wait}'
		'{page}'
		'#13601106V#0002F啊，但是……\n'
		'如果搬到这里的话，说不定\n'
		'可以跟小滴在一起哦。{wait}'
		'{page}'
		'#13601107V你们不是成了好朋友吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(32), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601108V#1110F#12P真的吗！？{wait}'
		'{page}'
		'#13601109V#1108F啊，但是……琪雅还是不想\n'
		'跟罗伊德还有大家分开……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601110V#1508F#12P真是的，罗伊德警官……\n'
		'不可以说欺负人的话哦。{wait}'
		'{page}'
		'#13601111V琪雅会困扰的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13601112V#0012F#5P哈哈，说得也是呢。{wait}'
		'{page}'
		'#13601113V#0000F对不起，琪雅。\n'
		'今天差不多该回去了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601114V#1112F#12P咦，但琪雅还想跟小滴\n'
		'再说一会话。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13601115V#0104F#5P呵呵，下次再来玩就好了。{wait}'
				'{page}'
				'#13601116V#0100F小滴来市里时，\n'
				'也可以让她来我们那里玩。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13601117V#0204F#5P……下次再来玩就好了。{wait}'
				'{page}'
				'#13601118V#0202F小滴来市里的时候，\n'
				'也可以让她来我们支援课玩。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13601119V#0304F#5P哈哈，下次再来玩就好了啊。{wait}'
				'{page}'
				'#13601120V#0300F小滴来市里时，\n'
				'也可以让她来我们那边玩。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601121V#1110F#12P嗯，这样啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(33), Text(
		'#13601122V#1404F#5P呵呵……\n'
		'那到时就拜托了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(33), 180, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(33), Text(
		'#13601123V#1402F#5P──小滴，我要抱你起来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(31), Text(
		'#13601124V#1500F#12P嗯……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-24710, 200, -23540), 2000),
	Insn('0x9B', b'\x00', Char(31), b'\x00\x00\xe8\x03\x00\x00\xdc\x05\x00\x00\x00'),
	Insn('0x6F', b'y'),
	Insn('CROSSFADE', 500),
	Insn('CHAR_SET_CHCP', Char(33), 33),
	Insn('CHAR_SET_FRAME', Char(33), 0),
	Insn('CHAR_FLAG1_SET', Char(31), 128),
	Insn('CHAR_FLAG2_SET', Char(31), 32768),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x0D'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(33), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 239, 1, [
		Insn('CHAR_WATCH', Char(254), Char(33), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 32, 1, [
		Insn('CHAR_WATCH', Char(254), Char(33), 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13601125V#0000F#5P亚里欧斯先生今天\n'
		'要住在这里吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(33), Char(239), 400),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(33), Text(
		'#13601126V#1404F#11P是啊，准备住一晚上。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(33), 225, 400),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(33), Text(
		'#13601127V#1402F#11P──琪雅，\n'
		'今后也请和小滴好好相处。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601128V#1109F#6P嗯！{wait}'
		'{page}'
		'#13601129V#1110F小滴，下次见！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(33), Translate('小滴'), Text(
		'#13601130V#1502F#5P嗯……！\n'
		'琪雅，再见！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_UNSET', Char(33), 4),
	Insn('CHAR_FLAG1_SET', Char(33), 32768),
	Insn('CHAR_ROTATE', Char(33), 0, 400),
	Insn('SLEEP', 300),
	Insn('CAM_OFFSET', (-24710, 200, -23040), 5000),
	Insn('FORK_LOOP', 257, 1, [
		Insn('CHAR_WATCH', Char(257), Char(33), 500),
	]),
	Insn('FORK_LOOP', 239, 1, [
		Insn('CHAR_WATCH', Char(239), Char(33), 500),
	]),
	Insn('FORK_LOOP', 32, 1, [
		Insn('CHAR_WATCH', Char(32), Char(33), 500),
	]),
	Insn('FORK', 33, 1, [
		Insn('0x95', Char(254), (-23810, 0, -9390), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(33), 1),
	Insn('CHAR_FLAG1_UNSET', Char(33), 32768),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(239), 1),
	Insn('FORK_QUIT', Char(32), 1),
	Insn('0x6F', b'\x01'),
	Insn('CHAR_FLAG1_SET', Char(33), 128),
	Insn('CHAR_FLAG2_SET', Char(33), 32768),
	Insn('CHAR_FLAG1_SET', Char(31), 128),
	Insn('CHAR_FLAG2_SET', Char(31), 32768),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (-25130, 200, -23360), 1000),
	Insn('CAM_ROTATE', 36, 16, 0, 1000),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 239, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('CHAR_ROTATE', Char(32), 0, 500),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(239), 1),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13601131V#0002F#5P那么……\n'
		'我们也差不多该回去了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13601132V#0102F#5P呵呵，说得也是呢，\n'
				'不知不觉已经黄昏了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13601133V#0202F#5P说得也是呢……\n'
				'不知不觉已经黄昏了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13601134V#0302F#5P是啊，\n'
				'不知不觉已经黄昏了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601135V#1105F#12P这么说来……\n'
		'哇，天空好红哦！{wait}'
		'{page}'
		'#13601136V#1109F琪雅肚子饿了！{wait}'
		'{page}'
		'#13601137V#1110F今天晚饭要吃什么呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13601138V#0012F#5P哈哈……\n'
		'琪雅真的很有活力呢。{wait}'
		'{page}'
		'#13601139V#0000F那么，去跟赛西儿姐打声招呼，\n'
		'然后就坐巴士回去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(32), Text(
		'#13601140V#1109F#12P嗯！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 23550, 3000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('MINIGAME', 24, 0, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('0x2F', b'\x01\x00'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('0x2F', b'\x02\x00'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('0x2F', b'\x03\x00'),
		]),
		(None, []),
	]),
	Insn('0x2E', b'\x01\xff\xff'),
	Insn('0x2E', b'\x02\xff\xff'),
	Insn('0x2E', b'\x03\xff\xff'),
	Insn('BGM_STOP', 5000),
	Insn('BGM_WAIT'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 302), Insn('SET'), Insn('END')])),
	Insn('FLAG_SET', Flag(739)),
	Insn('NEW_SCENE', 'c010b', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][58] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-35700, 900, 0), 0),
	Insn('CAM_ROTATE', 35, 19, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 23000, 0),
	Insn('CAM_DISTANCE', 21000, 2500),
	Insn('CHAR_SET_POS', Char(257), (-42200, 0, -1000), 90),
	Insn('CHAR_SET_POS', Char(258), (-42200, 0, 400), 90),
	Insn('CHAR_SET_POS', Char(259), (-43600, 0, -1000), 90),
	Insn('CHAR_SET_POS', Char(260), (-43600, 0, 400), 90),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x88\x13\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x88\x13\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x88\x13\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x88\x13\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('CHAR_FLAG1_SET', Char(15), 128),
	Insn('CHAR_FLAG2_SET', Char(15), 32768),
	Insn('0xB5', b'\x00\x03\x80\x00'),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200843V#0001F#6P那么，赶快去确认一下，\n'
		'看看约亚西姆医生现在是否有时间吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200844V#0100F#5P嗯，\n'
		'先去接待处吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200845V#0306F#5P但愿他不要\n'
		'又出去钓鱼了才好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200846V#0211F#6P……很有可能呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (-37900, 0, -300), 90),
	Insn('CHAR_FLAG1_UNSET', Char(15), 128),
	Insn('CHAR_FLAG2_UNSET', Char(15), 32768),
	Insn('FLAG_SET', Flag(1562)),
	Insn('QUEST', 76, Insn('TASK_SET', 1)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][59] = [
	Insn('EVENT_BEGIN', 0),
	Insn('LOAD_CHCP', 'apl/ch50410', 30),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-50560, 1300, 0), 0),
	Insn('CAM_ROTATE', 45, 19, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 20000, 0),
	Insn('CAM_DISTANCE', 18250, 3000),
	Insn('OBJ_FLAG_UNSET', Object(6), 16),
	Insn('0x71', Object(6), b'\n\x00', 10, 0),
	Insn('0x79', b'\x06\x00'),
	Insn('CHAR_SET_POS', Char(257), (-44720, 0, -560), 270),
	Insn('CHAR_SET_POS', Char(258), (-43930, 0, 910), 270),
	Insn('CHAR_SET_POS', Char(259), (-42520, 0, -220), 270),
	Insn('CHAR_SET_POS', Char(260), (-46240, 0, 700), 270),
	Insn('FORK', 260, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x88\x13\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x88\x13\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x88\x13\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x88\x13\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0xB5', b'\x00\x04\x80\x00'),
	Insn('0x6F', b'\x10'),
	Insn('0x0D'),
	Insn('CHAR_ROTATE', Char(260), 90, 500),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200982V#0302F#6P好了，已经黄昏了。\n'
		'快点坐巴士回去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200983V#0002F#11P对啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200984V#0102F#11P呵呵，这种时候\n'
		'就会庆幸有巴士坐呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200985V#0208F#11P#50W…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (-49060, 1300, 0), 1500),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 300),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200986V#0005F#6P缇欧……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200987V#0305F#6P总感觉小缇你……\n'
		'从刚才开始就安静得有些不对劲啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200988V#0206F#11P#60W……没那回事。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 258, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00R\x03\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200989V#0101F#5P缇欧……！？{wait}'
		'{page}'
		'#14200990V虽然被夕阳照得有些看不出来……\n'
		'但你的脸色很苍白啊！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200991V#0011F#6P哎！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200992V#0202F#11P#50W……没问题，\n'
		'只是有一点不舒服而已……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200993V#0306F#6P喂喂，\n'
		'怎么会没问题啊。{wait}'
		'{page}'
		'#14200994V#0301F总之，先找个\n'
		'地方休──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 6000),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200995V#0206F#11P#60W……啊………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_SET', Char(259), 2),
	Insn('CHAR_FLAG1_SET', Char(259), 16),
	Insn('CHAR_SET_CHCP', Char(259), 30),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('SOUND_PLAY', 910, 0, 0, 100),
	Insn('0x0D'),
	Insn('SLEEP', 150),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('CHAR_SET_FRAME', Char(259), 1),
	Insn('SLEEP', 150),
	Insn('CHAR_SET_FRAME', Char(259), 2),
	Insn('SLEEP', 300),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200996V#0007F#6P缇欧！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200997V#0101F#5P不、不好了……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200998V#11P#60W…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200999V#0307F#6P我马上就去叫\n'
		'医生或护理师过来！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14201000V#0007F#5P嗯……拜托了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 60))),
	Insn('SLEEP', 300),
	Insn('CAM_OFFSET', (-48210, 1300, -210), 2000),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(260), 3),
	Insn('CHAR_SET_CHCP', Char(259), 255),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_FLAG1_UNSET', Char(259), 2),
	Insn('CHAR_FLAG1_UNSET', Char(259), 16),
	Insn('0x49'),
	Insn('0xD5', 30),
	Insn('SLEEP', 2000),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 515), Insn('SET'), Insn('END')])),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 't150b', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][60] = [
	Insn('0x95', Char(254), (-49190, 0, 2050), 5000, 0),
	Insn('0x95', Char(254), (-35480, 0, 180), 5000, 0),
	Insn('RETURN'),
]

data['code'][61] = [
	Insn('CHAR_ANIMATION', Char(254), 1000, [
		2,
		3,
		4,
		3,
	]),
	Insn('RETURN'),
]

data['code'][62] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (-18180, 0, -17650), 0),
	Insn('CAM_ROTATE', 352, 22, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 17500, 0),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CHAR_SET_POS', Char(257), (-18160, -1000, -18590), 45),
	Insn('CHAR_SET_POS', Char(258), (-18950, -1000, -17790), 45),
	Insn('CHAR_SET_POS', Char(259), (-19750, -1000, -18590), 45),
	Insn('CHAR_SET_POS', Char(260), (-18950, -1000, -19390), 45),
	Insn('CHAR_SET_POS', Char(265), (-18160, -1000, -20020), 45),
	Insn('CHAR_FLAG1_UNSET', Char(4), 128),
	Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
	Insn('CHAR_SET_FRAME', Char(23), 2),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11P……最近似乎有点累了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11P拜托护理师希蓉小姐\n'
		'订购一些医疗用品，\n'
		'却送来了其它东西……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11P儿子琴兹也还是\n'
		'跟以前一样，\n'
		'没有退出不良分子的意思……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11P做教授\n'
		'也很辛苦呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F（他是这所医院的教授吗……\n'
		'\u3000看起来好像很疲惫呢。）{wait}'
		'{page}'
		'#0003F（但是，教授的话，\n'
		'\u3000应该会对做礼物的材料\n'
		'\u3000有什么线索吧。）{wait}'
		'{page}'
		'#0000F那个，不好意思。\n'
		'有点事情想请教您……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11P……噢，什么事情呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}罗伊德说明了正在收集\n'
		'礼物材料的事由。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F……也就是说，\n'
		'我们正在寻找合适的材料。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11P是为了小滴吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11P如果是这样的话，在那里\n'
		'也许能找到什么。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0200F那里……\n'
		'您有什么头绪吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11P是啊……在这所医院\n'
		'里面，闲置着大量的\n'
		'进口杂货。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11P而且基本上都是\n'
		'还没有人用过的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#5P#0105F进口杂货指的是……\n'
		'为什么医院会有那种东西……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11P以前，我拜托护理师希蓉\n'
		'订购外科手术用\n'
		'的手术刀等医疗器具。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11P但不知为何，送来的不是医疗器具，\n'
		'而是放在那里的一堆杂货。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11P为什么会出现这种情况……\n'
		'我自己都还想搞清楚呢。{wait}'
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
	Insn('EMOTE', Char(4), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(260), Text(
		'#6P#0300F您看起来很辛苦呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#6P#0506F该怎么说呢……经常为司令而头痛的\n'
		'我们也感同身受呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F那、那就是说……\n'
		'我们可以从那里拿点什么吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11P嗯，没问题。\n'
		'说实话，我正在烦恼要怎么处理那堆杂物呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11P放有杂货的集装箱\n'
		'在位于宿舍二楼，穿过男性职员\n'
		'宿舍尽头的露台上。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#11P要是发现了什么\n'
		'有用的东西，就随便\n'
		'拿走吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F好，谢谢您了。{wait}'
		'{page}'
		'#0003F（二楼露台是指……\n'
		'\u3000狼型魔兽事件中，\n'
		'\u3000安装了防护栏的地方吧。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(0), (-18160, -1000, -18590), 45),
	Insn('CHAR_FLAG1_SET', Char(4), 128),
	Insn('CHAR_FLAG2_SET', Char(4), 32768),
	Insn('CHAR_SET_FRAME', Char(23), 0),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('CHAR_SET_POS', Char(9), (-23040, -1000, -25910), 0),
	Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
	Insn('QUEST', 44, Insn('TASK_SET', 3)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][63] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (-36870, 4000, 16950), 0),
	Insn('CAM_ROTATE', 35, 29, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 23790, 0),
	Insn('CHAR_SET_POS', Char(257), (-36910, 3000, 16290), 90),
	Insn('CHAR_SET_POS', Char(258), (-38300, 3000, 16300), 90),
	Insn('CHAR_SET_POS', Char(259), (-38300, 3000, 17300), 90),
	Insn('CHAR_SET_POS', Char(260), (-37000, 3000, 17300), 90),
	Insn('CHAR_SET_POS', Char(265), (-37000, 3000, 18600), 135),
	Insn('CHAR_FLAG1_UNSET', Char(4), 128),
	Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
	Insn('CHAR_SET_FRAME', Char(23), 2),
	Insn('SLEEP', 500),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F这个好像就是\n'
		'教授所说的集装箱了。{wait}'
		'{page}'
		'那么，\n'
		'稍微找一找吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(265), Text(
		'#5P#0505F怎么样？\n'
		'有什么可以用的东西吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 315, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0000F嗯，找到了这样的东西。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#6P#0105F啊……皮绳吗？{wait}'
		'{page}'
		'#0100F似乎编得\n'
		'很结实呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0200F……还有其它\n'
		'可用的东西吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0006F呃，那个，\n'
		'翻过一遍后……{wait}'
		'{page}'
		'虽然不知道原因，\n'
		'但尽是一些奇怪的装饰品，\n'
		'还有辟邪的人偶。{wait}'
		'{page}'
		'#0000F看样子，\n'
		'除了这根皮绳之外，\n'
		'就找不到其它的有用之物了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11P#0306F算啦，那个医生不是也\n'
		'正在头痛要怎么处理这些东西吗。{wait}'
		'{page}'
		'#0300F即使只找到一件看起来可以用的\n'
		'东西，也算很幸运了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'获得了{item 835}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 835, 1),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0003F（如果是这么结实的绳子，\n'
				'\u3000即使是亚里欧斯先生用\n'
				'\u3000应该也不会断吧……）{wait}'
				'{page}'
				'（之后再找个\n'
				'\u3000可以镶嵌小滴那块石头的\n'
				'\u3000挂坠扣就好了。）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('QUEST', 44, Insn('TASK_SET', 4)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 0))), Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 2))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 4))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 44, Insn('TASK_SET', 5)),
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0000F（制作礼物的材料收集齐了，\n'
				'\u3000包装用的盒子与缎带也找到了……）{wait}'
				'{page}'
				'（好，差不多该拿去\n'
				'\u3000给小滴了。）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(0), (-37600, 3000, 16800), 270),
	Insn('CHAR_FLAG1_SET', Char(4), 128),
	Insn('CHAR_FLAG2_SET', Char(4), 32768),
	Insn('0x65', 8, 1),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][64] = [
	Insn('EVENT_BEGIN', 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(784)), Insn('FLAG', Flag(793)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F这里是通往郊外的方向……{wait}'
				'{page}'
				'#0003F怎么说也不能把赛西儿姐姐\n'
				'带到那种地方去。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(785)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(310), Text(
						'#1300F呵呵，是要进行\n'
						'魔兽骚乱的调查吧。{wait}'
						'{page}'
						'跟我来，\n'
						'我带你们去院区二楼。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(310), Text(
						'#1300F呵呵，是要进行\n'
						'魔兽骚乱的调查吧。{wait}'
						'{page}'
						'事发现场在院区的屋顶，\n'
						'我带你们去吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(793)), Insn('FLAG', Flag(799)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这里是通往郊外的方向……{wait}'
				'{page}'
				'#0003F回去之前\n'
				'必须向赛西儿姐姐报告一下。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(799)), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F已经黄昏了，\n'
				'回去的时候乘坐巴士吧。{wait}'
				'{page}'
				'只要调查巴士站，\n'
				'应该就能知道下一班巴士的抵达时间了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 14))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((2, 12))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1346)), Insn('FLAG', Flag(1349)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F哎呀……\n'
				'好不容易来到这了，\n'
				'得去医院找医生商量一下呢。{wait}'
				'{page}'
				'到接待处去询问下有关\n'
				'『神经科』的事吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1349)), Insn('FLAG', Flag(1351)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0003F不能带着琪雅\n'
				'去市外啊……{wait}'
				'{page}'
				'#0000F而且还必须向约亚西姆医生\n'
				'询问有关琪雅记忆的事。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1351)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(11)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F……琪雅大概\n'
						'还在医院用地的范围内。{wait}'
						'{page}'
						'#0001F必须快一点找到她呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(257), Text(
						'#0001F快一点把琪雅找出来吧。\n'
						'她应该还在医院用地的范围内。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (-61000, 0, 0), 90),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][65] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}St.Ursula \n'
		'Medical College{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][66] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}Medical College\n'
		'～招待所《雷库切》～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]
