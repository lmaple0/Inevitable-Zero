# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'c0000',
	'name2': 'c0000',
	'location': 2,
	'bgm': 100,
	'flags': 8192,
	'includes': [
		'c0000',
		None,
		None,
		None,
		None,
		None,
	],
	'name3': 'c0000',
	'labels': [
		{
			'pos': (-9.25, 0.0, 67.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('中央广场'),
		},
		{
			'pos': (-75.0, 0.0, 71.5),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('西侧大道'),
		},
		{
			'pos': (17.75, 0.0, 156.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('行政区'),
		},
		{
			'pos': (-136.0, 0.0, 146.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('住宅区'),
		},
		{
			'pos': (-63.0, 0.0, 138.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('欢乐街'),
		},
		{
			'pos': (72.0, 0.0, 44.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('东侧大道'),
		},
		{
			'pos': (107.5, 0.0, -11.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('旧市街'),
		},
		{
			'pos': (100.0, 0.0, 110.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('港湾区'),
		},
		{
			'pos': (74.0, 0.0, 204.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('ＩＢＣ'),
		},
		{
			'pos': (2.0, 0.0, -2.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('站前大道'),
		},
		{
			'pos': (-45.0, 0.0, 102.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('小巷'),
		},
		{
			'pos': (-1.0, 0.0, -33.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('乌尔斯拉小径'),
		},
		{
			'pos': (126.0, 0.0, 58.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('东克洛斯贝尔街道'),
		},
		{
			'pos': (-126.0, 0.0, 70.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('西克洛斯贝尔街道'),
		},
		{
			'pos': (-120.0, 0.0, 170.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('玛因兹山道'),
		},
		{
			'pos': (-31.25, 0.0, 53.0),
			'unk': b'\x00\x00Q\x00',
			'name': Translate(''),
		},
		{
			'pos': (22.5, 0.0, 79.0),
			'unk': b'\x00\x00T\x00',
			'name': Translate(''),
		},
		{
			'pos': (-6.75, 0.0, 45.0),
			'unk': b'\x00\x00W\x00',
			'name': Translate(''),
		},
		{
			'pos': (-32.0, 0.0, 82.0),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-11.5, 0.0, 106.0),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-62.25, 0.0, 77.0),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-72.0, 0.0, 98.0),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-48.0, 0.0, 130.0),
			'unk': b'\x00\x00R\x00',
			'name': Translate(''),
		},
		{
			'pos': (-43.25, 0.0, 117.0),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-34.5, 0.0, 108.5),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-6.0, 0.0, 179.5),
			'unk': b'\x00\x00Q\x00',
			'name': Translate(''),
		},
		{
			'pos': (106.0, 0.0, 44.0),
			'unk': b'\x00\x00R\x00',
			'name': Translate(''),
		},
		{
			'pos': (89.0, 0.0, -46.5),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (76.0, 0.0, -28.0),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (2.0, 0.0, 55.0),
			'unk': b'\x00\x00V\x00',
			'name': Translate(''),
		},
	],
	'chcp': [
		'chr/ch23600',
		'chr/ch20400',
		'chr/ch21000',
		'chr/ch21100',
		'chr/ch21600',
		'chr/ch21700',
		'chr/ch22800',
		'chr/ch24400',
		'chr/ch21300',
		'chr/ch21800',
		'chr/ch21900',
		'chr/ch21200',
		'chr/ch27700',
		'chr/ch27800',
		'chr/ch22100',
		'chr/ch22000',
		'chr/ch32200',
		'chr/ch32300',
		'chr/ch20200',
		'chr/ch20300',
		'chr/ch33300',
		'chr/ch34500',
		'chr/ch24900',
	],
	'npcs': [
		{
			'name': Translate('比利'),
			'pos': (4000, 0, -7000),
			'angle': 270,
			'_1': b'\x05\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((0, 5)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('里德'),
			'pos': (-1830, 0, 13000),
			'angle': 180,
			'_1': b'\x05\x01\x00\x00\x01\x00\x00\x01',
			'function': Function((0, 6)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('弗里吉亚'),
			'pos': (5849, 0, 1759),
			'angle': 315,
			'_1': b'\x85\x01\x00\x00\x14\x00\x00\x00',
			'function': Function((0, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('莱缇娜'),
			'pos': (4650, 0, 2950),
			'angle': 135,
			'_1': b'\x85\x01\x00\x00\x15\x00\x00\x00',
			'function': Function((0, 8)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('玛夏'),
			'pos': (4389, 0, -4900),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x15\x00\x00\x00',
			'function': Function((0, 10)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (4880, 0, 2930),
			'angle': 35,
			'_1': b'\x85\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (6039, 0, 2779),
			'angle': 292,
			'_1': b'\x85\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 12)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (4940, 0, 3049),
			'angle': 111,
			'_1': b'\x85\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (5920, 0, 2700),
			'angle': 291,
			'_1': b'\x95\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 14)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (4750, 0, 3109),
			'angle': 111,
			'_1': b'\x85\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (5909, 0, 2680),
			'angle': 291,
			'_1': b'\x85\x01\x00\x00\x07\x00\x00\x00',
			'function': Function((0, 16)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (5239, 0, 2819),
			'angle': 286,
			'_1': b'\x85\x01\x00\x00\x08\x00\x00\x00',
			'function': Function((0, 17)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (6539, 0, 1690),
			'angle': 81,
			'_1': b'\x85\x01\x00\x00\t\x00\x00\x00',
			'function': Function((0, 18)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (6320, 0, 2339),
			'angle': 177,
			'_1': b'\x85\x01\x00\x00\n\x00\x00\x00',
			'function': Function((0, 19)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (5130, 0, 2099),
			'angle': 290,
			'_1': b'\x85\x01\x00\x00\x0b\x00\x00\x00',
			'function': Function((0, 20)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (4079, 0, 2480),
			'angle': 110,
			'_1': b'\x85\x01\x00\x00\x08\x00\x00\x00',
			'function': Function((0, 21)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('商务人士'),
			'pos': (3369, 0, 1950),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x0c\x00\x00\x00',
			'function': Function((0, 22)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('商务人士'),
			'pos': (3480, 0, 529),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\r\x00\x00\x00',
			'function': Function((0, 23)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (4369, 0, 2119),
			'angle': 101,
			'_1': b'\x85\x01\x00\x00\x10\x00\x00\x00',
			'function': Function((0, 24)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (5940, 0, 1970),
			'angle': 281,
			'_1': b'\x85\x01\x00\x00\x11\x00\x00\x00',
			'function': Function((0, 25)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (4539, 0, 3069),
			'angle': 45,
			'_1': b'\x85\x01\x00\x00\x12\x00\x00\x00',
			'function': Function((0, 26)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (5880, 0, 2589),
			'angle': 315,
			'_1': b'\x85\x01\x00\x00\x13\x00\x00\x00',
			'function': Function((0, 27)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (5110, 0, 3750),
			'angle': 112,
			'_1': b'\x85\x01\x00\x00\x0e\x00\x00\x00',
			'function': Function((0, 28)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (5909, 0, 3420),
			'angle': 292,
			'_1': b'\x85\x01\x00\x00\x0f\x00\x00\x00',
			'function': Function((0, 29)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (6360, 0, 2480),
			'angle': 225,
			'_1': b'\x85\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 30)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (5239, 0, 2789),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 31)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (4579, 0, 1519),
			'angle': 252,
			'_1': b'\x85\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((0, 32)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('赛尔盖课长'),
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
			'name': Translate('老妇人'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('格蕾丝'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
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
			'name': Translate('列车'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((255, 255)),
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
			'name': Translate('库罗玛'),
			'pos': (699, 0, 13149),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x16\x00\x00\x00',
			'function': Function((0, 33)),
			'_2': b'\xff\x00\x00\x00',
		},
	],
	'monsters': [],
	'triggers': [
		{
			'pos': (-11.670000076293945, 17.1200008392334, -5.5),
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
				5.835000038146973,
				-8.5600004196167,
				1.100000023841858,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 56)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (8.5, -2.0, -0.5),
			'range': 16.0,
			'transform': [
				0.5,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.25,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				-4.25,
				0.5,
				0.10000000149011612,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 58)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (-22300, -5000, 20700),
			'range': 2000,
			'bubble_pos': (-21950, -4000, 21360),
			'_1': b'|\x00\x00',
			'function': Function((0, 35)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00', Function((0, 3)), Function((0, 4))),
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
		Insn('CHAR_ROTATE', Char(254), 180, 500),
		Insn('SLEEP', 300),
		Insn('0x95', Char(254), (-1830, 0, -9000), 2000, 0),
		Insn('SLEEP', 300),
		Insn('CHAR_ROTATE', Char(254), 0, 500),
		Insn('SLEEP', 300),
		Insn('0x95', Char(254), (-1830, 0, 13000), 2000, 0),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('0x95', Char(254), (-1830, 0, -23430), 2000, 0),
		Insn('SLEEP', 800),
		Insn('CHAR_SET_POS', Char(254), (-1830, 0, 25870), 180),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 104), Insn('EQ'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(0), (0, 0, 21840), 180),
			Insn('CHAR_SET_POS', Char(1), (0, 0, 21840), 180),
			Insn('CHAR_SET_POS', Char(2), (0, 0, 21840), 180),
			Insn('CHAR_SET_POS', Char(3), (0, 0, 21840), 180),
			Insn('IF', [
				(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(4), (0, 0, 21840), 180),
					Insn('CHAR_SET_POS', Char(5), (0, 0, 21840), 180),
				]),
				(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(4), (0, 0, 21840), 180),
				]),
				(None, []),
			]),
			Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 100), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('0xD0', 7, Expr([Insn('CONST', 9), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('FLAG_SET', Flag(671)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 53, Insn('FLAG_GET', 16))), Insn('FLAG', Flag(527)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 55))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 36))),
		]),
		(Expr([Insn('FLAG', Flag(737)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(737)),
			Insn('EVENT', Function((0, 43))),
		]),
		(Expr([Insn('FLAG', Flag(738)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(738)),
			Insn('EVENT', Function((0, 44))),
		]),
		(Expr([Insn('FLAG', Flag(739)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(739)),
			Insn('EVENT', Function((0, 53))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(34), 128),
			Insn('CHAR_SET_POS', Char(8), (3030, 0, -8220), 270),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 45, Insn('TASK_GET', 14))), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(12), 128),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(32), 128),
			Insn('CHAR_FLAG1_UNSET', Char(33), 128),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(30), 128),
			Insn('CHAR_FLAG1_UNSET', Char(31), 128),
		]),
		(Expr([Insn('FLAG', Flag(1547)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(28), 128),
			Insn('CHAR_FLAG1_UNSET', Char(29), 128),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(26), 128),
			Insn('CHAR_FLAG1_UNSET', Char(27), 128),
			Insn('CHAR_FLAG1_SET', Char(27), 16),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 38, Insn('TASK_GET', 2))), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(45), 128),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(24), 128),
			Insn('CHAR_FLAG1_UNSET', Char(25), 128),
			Insn('CHAR_FLAG1_SET', Char(25), 16),
			Insn('CHAR_FLAG1_SET', Char(8), 128),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(22), 128),
			Insn('CHAR_FLAG1_UNSET', Char(23), 128),
			Insn('CHAR_FLAG1_SET', Char(8), 128),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(20), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
			Insn('CHAR_FLAG1_SET', Char(20), 16),
			Insn('CHAR_FLAG1_SET', Char(21), 16),
			Insn('CHAR_SET_POS', Char(8), (1990, 0, -10980), 180),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_SET', Char(13), 16),
			Insn('CHAR_FLAG1_SET', Char(14), 16),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 102), Insn('EQ'), Insn('FLAG', Flag(777)), Insn('BOOL_AND'), Insn('FLAG', Flag(1286)), Insn('FLAG', Flag(1292)), Insn('NOT'), Insn('BOOL_AND'), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xC7', b'\x01\x00\x10\x00\x00'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(513)), Insn('FLAG', Flag(519)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 111), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('FLAG', Flag(520)), Insn('FLAG', Flag(521)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 102), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('FLAG', Flag(538)), Insn('FLAG', Flag(768)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 110), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('OBJ_FLAG_SET', Object(11), 4),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(560)), Insn('NOT'), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(0), 16),
		]),
		(None, [
			Insn('0x65', 0, 1),
		]),
	]),
	Insn('OBJ_FLAG_SET', Object(12), 4),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(12), 4),
			Insn('OBJ_FLAG_SET', Object(12), 2),
			Insn('OBJ_SET_FRAME', Object(12), 'light', Insn('0', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(12), 4),
			Insn('OBJ_FLAG_SET', Object(12), 2),
			Insn('OBJ_SET_FRAME', Object(12), 'light', Insn('0', 1)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1037)), Insn('FLAG', Flag(1038)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
			Insn('OBJ_SET_FRAME', Object(255), 'sky', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'sky1', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'sd_mul', Insn('0', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
			Insn('OBJ_SET_FRAME', Object(255), 'sky', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'sky1', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'sd_mul', Insn('0', 1)),
		]),
		(None, [
			Insn('OBJ_SET_FRAME', Object(255), 'sky', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'sky1', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'sd_mul', Insn('1', 1)),
		]),
	]),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('NOT'), Insn('END')]), [
			Insn('0xB5', b'\x01\x00\x80\x00'),
		]),
		(None, []),
	]),
	Insn('0x1B', 3, Function((255, 255)), 255),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(768)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 3, Function((0, 57)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(768)), Insn('FLAG', Flag(777)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 3, Function((0, 57)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(801)), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 3, Function((0, 57)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1346)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 3, Function((0, 57)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1554)), Insn('FLAG', Flag(1560)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 3, Function((0, 57)), 0),
		]),
		(None, []),
	]),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 9, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x01\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1024)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 45, Insn('TASK_GET', 9))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x01\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('0xB5', b'\x01\x01\x80\x00'),
		]),
		(None, []),
	]),
	Insn('0x78', b'\r', Char(44)),
	Insn('OBJ_FLAG_SET', Object(13), 4),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 38, Insn('TASK_GET', 2))), Insn('END')]), [
					Insn('OBJ_FLAG_UNSET', Object(13), 4),
					Insn('CHAR_SET_POS', Char(44), (2250, 0, 12500), 180),
					Insn('0xD3', Char(44), 0, 180000, 0, 0),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 45, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('FLAG_SET', Flag(1688)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1537)), Insn('FLAG', Flag(1542)), Insn('NOT'), Insn('BOOL_AND'), Insn('0x23', 1), Insn('CONST', 1), Insn('EQ'), Insn('BOOL_AND'), Insn('END')]), []),
		(None, [
			Insn('0x16', Insn('3', b'\x1d\x01\x00')),
		]),
	]),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊～！！\n'
						'总算收到货物啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哎，都这么晚了啊！\n'
						'再不抓紧的话，今天可就送不完了……！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'没空胡思乱想了啊……\n'
						'总之得赶紧去送货了！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'车站现在似乎处于戒严状态啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不光是客车，\n'
				'货物列车的安检好像也推迟了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀呀……\n'
				'真是伤脑筋啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呼……\n'
				'和平时一样，\n'
				'我正在等待列车运来的货物。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，基本上\n'
				'我也已经习惯\n'
				'很晚才能拿到货了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'只有学会享受这段等待的时光，\n'
				'才称得上是职业人士啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天很难得，一早就\n'
				'拿到货物了哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'好～赶快去送货吧！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'虽然纪念庆典结束了，\n'
				'可还是这么忙呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'物流业的工作者\n'
				'真是没有假日啊……\n'
				'老板真是找了个辛苦的买卖。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'总算把货物\n'
						'都搬进来了，\n'
						'……真够累人啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'唉，明天还要去贝尔加德门卸货啊，\n'
						'这可真不是人干的活啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'难得开通了货物列车专线，\n'
						'要是能把我这些货一起运过去该多好啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'警备队员都在执勤地点住宿，\n'
						'所以他们的家人经常会托我们\n'
						'送些慰问品过去……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'难得开通了货物列车专线，\n'
						'要是能把我这些货一起运过去该多好啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'停在那边的，\n'
				'是我们公司用的\n'
				'搬运车。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'要送过去的货物\n'
				'好像有很多，\n'
				'所以开了车出来……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……难道要我一个人搬进车里吗？\n'
				'麻烦死啦……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'从外国运来的货物\n'
				'经常会延迟到达。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'可送货晚了的话，\n'
				'我就会被老爸训斥。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'唉～真叫人着急啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'从共和国送来的\n'
						'货物刚刚到了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'收件地址是……\n'
						'呃，是矿山镇玛因兹吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'唉～再不赶快送去的话，\n'
						'天都要黑了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'要去矿山镇玛因兹，\n'
						'就必须要走那条\n'
						'狭窄的山道……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'唉～再不赶快送去的话，\n'
						'天都要黑了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天应该有从共和国\n'
				'发来的货物。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'今天我来早了点……\n'
				'货物好像还没运来。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……嗯～真不该\n'
				'这么认真的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀呀，\n'
				'总算收到货物了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不赶快送到收件人那里的话，\n'
				'又要被老爸教训啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'真是的，要是不满意的话，\n'
				'就自己去送啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我们是『莱姆斯运送』，\n'
						'是一间自营的运输公司。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'负责把外国发来的货物\n'
						'配送给市民们。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我来领取\n'
						'运到车站来的货物……\n'
						'好慢啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我们是『莱姆斯运送』，\n'
						'是一间自营的运输公司。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我来领取\n'
						'运到车站来的货物……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'送得这么迟，\n'
						'可叫人怎么干活啊。{wait}'
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

data['code'][6] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'听别人说，机场和车站\n'
				'都有警备人员驻守，\n'
				'大概在严查危险物品吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'到底是什么人啊！\n'
				'竟敢让我心爱的列车们\n'
				'身陷险境……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'真是太过分了……\n'
						'感觉今天经过的列车好像少了点。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……不，好像是所有列车的发车时间\n'
						'都推迟了……？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'列车发车延迟的状况\n'
						'如此频发，可真奇怪啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'虽然我对开发出各种列车的\n'
						'帝国文化表示敬意……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但帝国的兵器，比如『列车炮』之类的东西，\n'
						'我绝对不能接受。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'因为，所谓的列车……是满载着乘客和货物，\n'
						'以及像我这种列车迷的\n'
						'梦想的交通工具……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'对于帝国的『列车炮』之类的东西，\n'
						'我实在是没有好感啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'列车可不是战斗的工具。\n'
						'而是满载乘客与货物，\n'
						'以及梦想的交通工具……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我现在非常非常想要\n'
						'一部导力相机啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……你问为什么，\n'
						'当然是为了拍列车的照片啦！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'只不过，那终究不是\n'
						'平民可以轻易买下的\n'
						'廉价商品啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'虽然我也曾尝试过\n'
						'去克洛斯贝尔通讯社\n'
						'应聘摄影师的职位……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过，他们当然\n'
						'不会录用我这种\n'
						'只想拍铁道照片的人……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'纪念庆典结束了，铁路列车的运行班次\n'
				'也恢复正常了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……唉……\n'
				'感觉有点寂寞呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 14))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((0, 60))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'下个月的纪念庆典时，\n'
						'会有许多游客乘坐列车\n'
						'来这里吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……哈哈，我要将列车的英姿\n'
						'一个不漏地尽收眼底。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 14))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((0, 60))),
				]),
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'听说帝国有些富裕的\n'
						'收藏家，还会收集\n'
						'铁道模型。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真叫人羡慕啊……！\n'
						'为什么我不是贵族出身呢！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'铁道模型几乎都是\n'
						'职业工匠手工制作的，\n'
						'所以价格非常高昂。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'如果以后发了大财，\n'
						'我就想每天欣赏着铁道模型\n'
						'安享晚年啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'要说临近纪念庆典有什么值得高兴的事，\n'
				'那就是列车要大显身手啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'从列车里涌出的人群\n'
				'仿佛群虫出巢一般，\n'
				'这景象真是震撼人心啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'横贯大陆的铁路轨道，\n'
						'是耗时数年，一点一点\n'
						'铺设而成的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那么长的铁轨，要小心铺设，\n'
						'避免列车运行时发生事故，\n'
						'肯定是相当困难的吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这正是前人种树后人凉。\n'
						'我真是太崇敬各位施工者了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'横贯大陆的铁路轨道，在铺设长度\n'
						'惊人的同时还要保持施工精准，\n'
						'这是需要花费漫长年月的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这正是前人种树后人凉。\n'
						'我真是太崇敬各位施工者了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'为什么大家\n'
				'都没发觉铁道的魅力呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'那些与克洛斯贝尔的发展史密不可分的\n'
				'贸易产业，可都是靠这种重要的\n'
				'交通工具支撑起来的啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我小时候，\n'
						'一直憧憬着能当上列车驾驶员。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过有一天，我突然发现了。\n'
						'我真正的爱好其实是\n'
						'『疼爱』列车……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'如今，我已经是个名副其实的铁道迷了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我的爱好是疼爱列车。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'小时候虽然想当驾驶员……\n'
						'至于现在的话，相比之下\n'
						'倒是更想当车站站员了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'横贯大陆铁道，\n'
						'大约是在二十年前开通的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'现在，只要坐一趟列车\n'
						'就能抵达大陆东端了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'现在，只要坐一趟列车\n'
						'就能抵达大陆东端了哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然是花钱又费时的漫长旅途……\n'
						'但作为列车爱好者，总有一天想试试看呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'飞行船、列车、导力车……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那么庞大的东西\n'
						'竟能在天上自由飞翔，\n'
						'或在地上飞速驰骋。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'在如今虽是司空见惯的技术，\n'
						'但仔细想想的话，还真是很了不起呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这真让人感到浪漫啊，\n'
						'你们能够理解我的这种心情吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'飞行船、列车、导力车……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我的嗜好虽然更偏向于铁道，\n'
						'但觉得交通工具有浪漫感的人\n'
						'应该也为数不少呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'你们是要去车站吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'根据我的情报网……\n'
						'开往共和国的列车\n'
						'差不多快到达了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'现在这个时间段\n'
						'十分拥挤，要小心哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我想，开往共和国的列车\n'
						'应该差不多快到了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯～若不是有急事的话，\n'
						'还真想听听\n'
						'发车时的汽笛声呢。{wait}'
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

data['code'][7] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 9))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'真是的，莱缇娜\n'
						'总是对一些琐事发牢骚……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……呵呵，算了。\n'
						'真期待快点到家啊～丅{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呼，总算能喘口气了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'七耀石的产地克洛斯贝尔……\n'
				'呵呵，真是激动人心啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'目标是七耀石的结晶……\n'
				'我一定要弄到手！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(2)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'目标是七耀石的结晶……\n'
				'我一定要弄到手！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哦，在此之前……\n'
				'先要找旅馆才行呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 9))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呜呜……好郁闷。\n'
						'回到家以后，不知会被骂成什么样……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'啊啊，女神啊。\n'
						'求您保佑我不要\n'
						'受到严厉的惩罚……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我和大小姐是从埃雷波尼亚帝国\n'
				'来这里采购七耀石的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过也有一半的原因是离家出走。\n'
				'家里现在必定已经乱成一团了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……心情好沉重……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(3)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'结果竟然\n'
				'跑到这种地方来……\n'
				'心情真沉重……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('0x4B', Char(10), -1),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_WATCH', Char(10), Char(11), 0),
	Insn('CHAR_WATCH', Char(11), Char(10), 0),
	Insn('TEXT_TALK', Char(10), Text(
		'作为目标的七耀石的结晶\n'
		'也弄到手了……\n'
		'终于可以回帝国了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'这么大的红耀石……\n'
		'我的脑海里已经浮现出父亲那大吃一惊的表情了！\n'
		'呵呵呵！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'从家里拿了一大笔钱，\n'
		'离家出走将近四个月……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'突然回去的话，\n'
		'家里人当然会大吃一惊吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'……你好烦呀，笨女仆！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'呜……好过分……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(10), -1),
	Insn('0x4C', Char(11), -1),
	Insn('FLAG_SET', Flag(2)),
	Insn('FLAG_SET', Flag(3)),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我……还是追着\n'
				'大小姐来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'因为……我还是\n'
				'放心不下她呀……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1917)), Insn('NOT'), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 45, Insn('TASK_GET', 9))), Insn('END')]), [
							Insn('TEXT_TALK', Char(257), Text(
								'#0005F咦，这位女仆……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(258), Text(
								'#0105F记得是坎贝尔议员家的……{wait}'
								'{page}'
								'#0106F感、感觉她好像\n'
								'一副心事重重的表情呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('TEXT_TALK', Char(257), Text(
								'#0005F咦，这位女仆是……？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(258), Text(
								'#0105F好像是在某座\n'
								'大宅里工作呢……{wait}'
								'{page}'
								'（好像在哪里\n'
								'\u3000见到过似的……）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(None, []),
			]),
			Insn('FLAG_SET', Flag(5)),
			Insn('FLAG_SET', Flag(1917)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'老爷，对不起……\n'
				'但是，我还是要\n'
				'去大小姐身边……！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'克洛斯贝尔车站……\n'
		'是这里没错吧，好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'城市太大，有点迷路了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'老公，赶快走吧。\n'
		'再不快点，列车就要开了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'回程要是耽误了，\n'
		'那可都是你的错哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'克洛斯贝尔市里，\n'
		'稀奇的东西可真不少啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'哎呀呀，真令人兴奋不已呀。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'哎，老头子你真是的，\n'
		'像小孩子一样两眼放光。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'好了，镇定一点吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'我正要往市外走呢，\n'
		'就被过路的人阻止了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'嗯～要观光的话，\n'
		'还是老老实实\n'
		'坐巴士比较好啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'我十分能理解\n'
		'想去市外\n'
		'逛逛的心情。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'这里都是高层建筑，\n'
		'对于在乡下长大的人来说，真是太压抑啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'嗯，市中心在……\n'
		'哎呀，不就在车站边上吗。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'呼，还好\n'
		'买了地图啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'在列车上一路摇晃……\n'
		'感觉有点不舒服。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'呜呕……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'唉，老公你真是的，\n'
		'总是很容易就晕车了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'你这个样子，\n'
		'还怎么去别处\n'
		'观光呀？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'下个月会有纪念庆典吧？\n'
		'我本来是想等到那时候再来的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'不过，我不太喜欢拥挤的地方，\n'
		'还是趁人少的时候好好享受一下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'唉～为什么选在\n'
		'这种淡季过来啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'在热闹的人群中\n'
		'旅行才有乐趣啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'这次是因公来ＩＢＣ大楼\n'
		'办事的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'事不宜迟，就马上\n'
		'前往拜访吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'部长！我陪您去！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'纪念庆典过后的克洛斯贝尔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'正是因为庆典刚过，\n'
		'才有做生意的机会！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'难道你不这么想吗！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'老师！\n'
		'既然决定了，就去检查\n'
		'要采购的商品吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'天色完全暗下来了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'希望旅馆还有空房……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'毕竟，\n'
		'长途旅行都把我饿坏了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'真想找个地方吃饭啊～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][28] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'我们是从帝国私奔而来的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'在这里的话，父亲就找不到了。\n'
		'我们两人一定能幸福的……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][29] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'若不是爱上身份卑微的我，\n'
		'她也就不会和父亲失和了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'我真是罪孽深重的男人啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'可是……只要看到她那幸福的表情，\n'
		'这种阴郁的心情\n'
		'也就烟消云散了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][30] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'安检官的检查\n'
		'相当仔细呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'说是要检查危险物品什么的……\n'
		'真是令人不安啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][31] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'车站月台里弥漫着一股莫名的紧张气氛，\n'
		'搞得人心惶惶的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'到底出了什么事呢……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][32] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'都到了月台，\n'
		'还让人等了将近一小时，\n'
		'真是累死人了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'克洛斯贝尔这地方\n'
		'原来这么重视警备吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][33] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 38, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(45), Text(
						'遗憾的是，\n'
						'特制苦番茄奶昔平时\n'
						'一般没法出售呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(45), Text(
						'因为原材料很难进货，\n'
						'而且基本卖不出去……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(45), Text(
						'现在店里的一点点原料\n'
						'完全是为市长先生准备的哦～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(45), Text(
						'啊，饮料已经\n'
						'交给市长先生了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F嗯，托您的福。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(339), Text(
						'#1109F谢谢您了～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(45), Text(
						'哪里哪里，不客气。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 38, Insn('TASK_GET', 3))), Insn('EXEC', Insn('QUEST_GET', 38, Insn('TASK_GET', 4))), Insn('OR'), Insn('END')]), [
			Insn('TEXT_TALK', Char(45), Text(
				'请把那杯奶昔\n'
				'送给市长先生，聊表慰问吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(45), Text(
				'市长先生是我的老主顾，\n'
				'一直承蒙他关照呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('CALL', Function((0, 34))),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][34] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CAM_OFFSET', (-530, 1300, 12810), 0),
	Insn('CAM_ROTATE', 44, 25, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 17490, 0),
	Insn('CHAR_SET_POS', Char(257), (-700, 0, 13150), 90),
	Insn('CHAR_SET_POS', Char(339), (-850, 0, 11920), 45),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(258), (-960, 0, 14520), 135),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(259), (-960, 0, 14520), 135),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(260), (-960, 0, 14520), 135),
		]),
		(None, []),
	]),
	Insn('CHAR_ROTATE', Char(45), 270, 0),
	Insn('CHAR_SET_FRAME', Char(45), 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(45), Text(
		'#11P欢迎光临～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(45), Text(
		'#11P要不要喝杯\n'
		'可口的饮料呢～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#12P#1110F啊～是卖果汁的～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F您就是平时在喷泉广场附近\n'
		'营业的那位店主吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(45), Text(
		'#11P啊，是的。\n'
		'但偶尔也会来这边\n'
		'做做生意……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(45), Text(
		'#11P真令人高兴啊～\n'
		'莫非是特地过来买\n'
		'喜爱的果汁吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#6P#0102F是的，其实……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#6P#0200F不，其实是……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#6P#0300F不，其实呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}向对方说明了来意，\n'
		'并要求购买市长平时爱喝的饮料。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('EMOTE', Char(45), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(45), Text(
		'#11P原来如此，是来买给市长先生的\n'
		'慰问品啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(45), Text(
		'#11P这样的话，请稍等一下。\n'
		'我马上为你们做出来！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('EFF_LOAD', ResId(0), 'battle\\it002_00.eff'),
	Insn('SLEEP', 500),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(45), Text(
		'#11P给，就是这个。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'获得了{item 856}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 856, 1),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
		]),
		(None, []),
	]),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F这、这是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#6P#0105F外公的确是\n'
				'很喜欢苦的东西……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#6P#0206F……光是想像一下，\n'
				'就觉得嘴里有股苦味弥漫开来。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#6P#0306F真厉害……\n'
				'不愧是市长先生啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(45), Text(
		'#11P这种奶昔对缓解疲劳很有效果，\n'
		'可是因为太苦了，\n'
		'所以只能作为特别订制的饮料来卖呢～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(45), Text(
		'#11P……正好我多做了一点，\n'
		'各位要不要喝喝看呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0011F呜……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, -1, 0, Text(
		'喝喝看\n'
		'婉言谢绝\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0012F那、那么，\n'
				'就尝一点点……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#6P#0106F呜呜……\n'
						'（既然是外公喜欢的饮料，\n'
						'\u3000总该了解一下才是……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'{color 5}罗伊德和艾莉\n'
						'拿起特制苦番茄奶昔，\n'
						'战战兢兢地喝了下去──{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('0x5A'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#6P#0206F……真的要喝吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'{color 5}罗伊德和缇欧\n'
						'拿起特制苦番茄奶昔，\n'
						'战战兢兢地喝了下去──{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('0x5A'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#6P#0306F唉，真是没办法。\n'
						'我也要下定决心试一下吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'{color 5}罗伊德和兰迪\n'
						'拿起特制苦番茄奶昔，\n'
						'战战兢兢地喝了下去──{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('0x5A'),
				]),
				(None, []),
			]),
			Insn('SOUND_PLAY', 887, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
					Insn('SOUND_PLAY', 28, 0, 0, 100),
					Insn('SLEEP', 1500),
					Insn('EMOTE', Char(257), 0, 2000, (20, 23, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('EMOTE', Char(258), 0, 2000, (20, 23, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
					Insn('SOUND_PLAY', 28, 0, 0, 100),
					Insn('SLEEP', 1500),
					Insn('EMOTE', Char(257), 0, 2000, (20, 23, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('EMOTE', Char(259), 0, 2000, (20, 23, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
					Insn('SOUND_PLAY', 28, 0, 0, 100),
					Insn('SLEEP', 1500),
					Insn('EMOTE', Char(257), 0, 2000, (20, 23, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('EMOTE', Char(260), 0, 2000, (20, 23, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
				]),
				(None, []),
			]),
			Insn('SLEEP', 1000),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}无与伦比的苦味饮料\n'
				'顺着喉咙滑了下去……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('EFF_PLAY', (ResId(0), 0), Char(257), 0, 0, 0, 500, 0, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
			Insn('SOUND_PLAY', 228, 0, 0, 100),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('EFF_PLAY', (ResId(0), 1), Char(258), 0, 0, 0, 500, 0, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('EFF_PLAY', (ResId(0), 1), Char(259), 0, 0, 0, 500, 0, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('EFF_PLAY', (ResId(0), 1), Char(260), 0, 0, 0, 500, 0, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
				]),
				(None, []),
			]),
			Insn('0x89', 0),
			Insn('0x89', 1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}罗伊德等人的ＣＰ上升了！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('0x32', Party(0), 5, 200),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('0x32', Party(1), 5, 200),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('0x32', Party(2), 5, 200),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('0x32', Party(3), 5, 200),
				]),
				(None, []),
			]),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0010F咳、咳……！{wait}'
				'{page}'
				'#0006F好、好像的确对身体\n'
				'很有益处……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#6P#0110F不、不过，这苦味……\n'
						'对第一次喝的人来说，真是太强烈了……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#6P#0208F苦、苦得难以形容……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#6P#0310F还、还真是够要命啊……\n'
						'怎么这么苦……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
			Insn('TEXT_TALK', Char(45), Text(
				'#11P啊哈哈，说得是呢～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(339), Text(
				'#12P#1111F嗯……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_ROTATE', Char(339), 90, 500),
			Insn('0x96', Char(339), (700, 0, 11920), 1000, 0),
			Insn('SLEEP', 500),
			Insn('CHAR_ROTATE', Char(339), 0, 500),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}琪雅拿起剩下的\n'
				'苦番茄奶昔，\n'
				'把吸管放入口中。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('FORK', 257, 1, [
				Insn('CHAR_WATCH', Char(257), Char(339), 500),
			]),
			Insn('FORK', 45, 1, [
				Insn('CHAR_WATCH', Char(45), Char(339), 500),
			]),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
					Insn('SOUND_PLAY', 28, 0, 0, 100),
					Insn('CHAR_WATCH', Char(258), Char(339), 500),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
					Insn('SOUND_PLAY', 28, 0, 0, 100),
					Insn('CHAR_WATCH', Char(259), Char(339), 500),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
					Insn('SOUND_PLAY', 28, 0, 0, 100),
					Insn('CHAR_WATCH', Char(260), Char(339), 500),
				]),
				(None, []),
			]),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0011F等、等一下……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#6P#0105F琪、琪雅！？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#6P#0205F琪雅……！？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#6P#0305F喂，小琪！？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
			Insn('TEXT_TALK', Char(339), Text(
				'#12P#1103F（吸吸）……{wait}'
				'{page}'
				'#1100F（咽下）……{wait}'
				'{page}'
				'#1109F呼哇～！\n'
				'好好喝哦～！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
				]),
				(None, []),
			]),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0011F全、全都喝掉了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#6P#0105F琪、琪雅好厉害……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#6P#0205F琪雅，你太厉害了……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#6P#0302F小琪……\n'
						'你好强啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
			Insn('CHAR_WATCH', Char(339), Char(257), 500),
			Insn('TEXT_TALK', Char(339), Text(
				'#12P#1101F哎～为什么～？{wait}'
				'{page}'
				'#1100F虽然有一点点苦，\n'
				'但是很好喝呀～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0006F呃，琪雅你觉得\n'
				'好喝就好……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(45), Text(
				'#11P啊哈哈……\n'
				'好有趣的小姑娘啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 257, 1, [
				Insn('CHAR_WATCH', Char(257), Char(45), 500),
			]),
			Insn('FORK', 339, 1, [
				Insn('CHAR_WATCH', Char(339), Char(45), 500),
			]),
			Insn('FORK', 45, 1, [
				Insn('CHAR_WATCH', Char(45), Char(257), 500),
			]),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('CHAR_WATCH', Char(258), Char(45), 500),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('CHAR_WATCH', Char(259), Char(45), 500),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('CHAR_WATCH', Char(260), Char(45), 500),
				]),
				(None, []),
			]),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F总、总之，\n'
				'真是多谢您了。{wait}'
				'{page}'
				'算上我们喝掉的，\n'
				'总共多少钱？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('QUEST', 38, Insn('TASK_SET', 3)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0006F不，好意还是\n'
				'心领了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(339), Text(
				'#12P#1105F哎～为什么～？{wait}'
				'{page}'
				'#1107F琪雅想喝\n'
				'苦番茄汁嘛～！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#6P#0102F啊哈哈……\n'
						'琪雅喝这种东西\n'
						'似乎还早了一点吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#6P#0200F我认为，琪雅喝这个\n'
						'似乎还太早了点……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#6P#0300F还是算了吧，小琪。\n'
						'会喝得一嘴苦味，很难受的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F对了，\n'
				'要多少钱呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('QUEST', 38, Insn('TASK_SET', 4)),
		]),
	]),
	Insn('TEXT_TALK', Char(45), Text(
		'#11P不用不用，今天就\n'
		'特别算你们免费吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(45), Text(
		'#11P市长先生是我的老主顾，\n'
		'一直承蒙他关照呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(45), Text(
		'#11P请把那杯奶昔\n'
		'送给市长先生，聊表慰问吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F但、但是……{wait}'
		'{page}'
		'#0000F……明白了，\n'
		'那我们就不客气地收下啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#6P#0102F呵呵……\n'
				'我们会把您的心意也转达给市长的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#6P#0202F我们会把您的心意也转达给市长的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#6P#0302F我们一定会把您的心意转达给市长先生。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('CHAR_SET_POS', Char(0), (-700, 0, 13150), 90),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][35] = [
	Insn('EVENT_BEGIN', 2),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(544)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('0xBD', b'\x00c')), Insn('EXEC', Insn('0xBD', b'\x03c')), Insn('BOOL_AND'), Insn('EXEC', Insn('0xBD', b'\x02c')), Insn('BOOL_AND'), Insn('EXEC', Insn('0xBD', b'\x01c')), Insn('BOOL_AND'), Insn('END')]), []),
				(None, [
					Insn('TEXT_TALK', Char(259), Text(
						'#0203F……还没给所有人的战术导力器\n'
						'镶嵌好结晶回路。{wait}'
						'{page}'
						'#0200F进入里面之前，先准备妥当吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('SOUND_PLAY', 828, 0, 0, 100),
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'{color 5}请为全体成员的战术导力器镶嵌结晶回路。{wait}'
						'{page}'
						'从营地菜单开启［ＯＲＢＭＥＮＴ］，\n'
						'再选择［ＱＵＡＲＴＺ］即可安装结晶回路。{color 0}{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('0x5A'),
					Insn('EVENT_END', 3),
					Insn('RETURN'),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('SOUND_PLAY', 810, 0, 0, 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}门上了锁。{wait}'
		'{page}'
		'使用地下区域Ａ区块的钥匙\n'
		'应该就可以将门打开。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('MENU', 0, -1, -1, 1, Text(
		'使用钥匙\n'
		'不使用钥匙\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('SOUND_PLAY', 809, 0, 0, 100),
			Insn('SLEEP', 500),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}打开了门锁。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('OBJ_FLAG_SET', Object(0), 16),
			Insn('0x65', 0, 1),
			Insn('FLAG_SET', Flag(560)),
			Insn('0xC7', b'\x01\x00\x00\x08\x00'),
			Insn('BREAK'),
		],
		1: [
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('EVENT_END', 3),
	Insn('RETURN'),
]

data['code'][36] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch20800', 30),
	Insn('LOAD_CHCP', 'chr/ch20900', 31),
	Insn('LOAD_CHCP', 'chr/ch21400', 32),
	Insn('LOAD_CHCP', 'apl/ch50003', 33),
	Insn('CAM_OFFSET', (4200, 3100, -1900), 0),
	Insn('CAM_ROTATE', 90, 16, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 19000, 0),
	Insn('CHAR_SET_CHCP', Char(257), 33),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_POS', Char(257), (10000, 500, -1900), 270),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_CHCP', Char(36), 30),
	Insn('CHAR_SET_FRAME', Char(36), 0),
	Insn('CHAR_SET_CHCP', Char(37), 31),
	Insn('CHAR_SET_FRAME', Char(37), 0),
	Insn('CHAR_FLAG1_UNSET', Char(36), 128),
	Insn('CHAR_FLAG1_UNSET', Char(37), 128),
	Insn('CHAR_FLAG1_UNSET', Char(36), 4),
	Insn('CHAR_FLAG1_UNSET', Char(37), 4),
	Insn('CHAR_FLAG1_SET', Char(36), 32768),
	Insn('CHAR_FLAG1_SET', Char(37), 32768),
	Insn('CHAR_SET_POS', Char(36), (10000, 500, -2800), 270),
	Insn('CHAR_SET_POS', Char(37), (10000, 500, -1000), 270),
	Insn('CHAR_SET_COLOR', Char(36), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(37), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG1_UNSET', Char(41), 128),
	Insn('CHAR_FLAG1_UNSET', Char(42), 128),
	Insn('CHAR_FLAG1_UNSET', Char(43), 128),
	Insn('0x4B', Char(9), -1),
	Insn('CHAR_FLAG1_SET', Char(9), 64),
	Insn('CHAR_SET_CHCP', Char(41), 15),
	Insn('CHAR_SET_FRAME', Char(41), 0),
	Insn('CHAR_FLAG1_SET', Char(41), 32768),
	Insn('CHAR_SET_CHCP', Char(42), 8),
	Insn('CHAR_SET_FRAME', Char(42), 0),
	Insn('CHAR_FLAG1_SET', Char(42), 32768),
	Insn('CHAR_SET_CHCP', Char(43), 32),
	Insn('CHAR_SET_FRAME', Char(43), 0),
	Insn('CHAR_FLAG1_SET', Char(43), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 32768),
	Insn('CHAR_SET_POS', Char(42), (900, 0, -8000), 0),
	Insn('CHAR_SET_POS', Char(41), (4600, 0, 3300), 45),
	Insn('CHAR_SET_POS', Char(43), (-4100, 0, -700), 315),
	Insn('CHAR_SET_POS', Char(9), (-1100, 0, 11000), 180),
	Insn('0xE5'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 100, 0, 0, 100),
	Insn('OBJ_FLAG_UNSET', Object(1), 16),
	Insn('0x71', Object(1), b'\x00\x00', 10, 0),
	Insn('0x79', b'\x01\x00'),
	Insn('FORK', 42, 1, [
		Insn('0x95', Char(254), (900, 0, 40000), 2000, 0),
	]),
	Insn('FORK', 9, 1, [
		Insn('0x95', Char(254), (-1100, 0, -40000), 2000, 0),
	]),
	Insn('CAM_OFFSET', (1200, 1100, -1900), 6000),
	Insn('CAM_ROTATE', 90, 12, 0, 6000),
	Insn('CAM_DISTANCE', 22000, 6000),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 37))),
	Insn('SLEEP', 800),
	Insn('FORK_FUNC', Char(36), 3, Function((0, 39))),
	Insn('SLEEP', 500),
	Insn('FORK_FUNC', Char(37), 3, Function((0, 41))),
	Insn('SLEEP', 2000),
	Insn('SOUND_PLAY', 101, 0, 0, 100),
	Insn('0x71', Object(1), b'\n\x00', 0, 0),
	Insn('0x79', b'\x01\x00'),
	Insn('OBJ_FLAG_SET', Object(1), 16),
	Insn('0x6F', b'y'),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('SLEEP', 2000),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (1200, 1100, -1900), 0),
	Insn('CAM_ROTATE', 48, 14, 0, 0),
	Insn('0x6E', 800, 0),
	Insn('CAM_DISTANCE', 24000, 0),
	Insn('CAM_ROTATE', 42, 14, 0, 8000),
	Insn('CAM_DISTANCE', 30000, 8000),
	Insn('0x0D'),
	Insn('0xCB', b'd\x00\xc8\x00', 'c_plac01', b'\x00\xd0\x07'),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 38))),
	Insn('SLEEP', 400),
	Insn('FORK_FUNC', Char(36), 3, Function((0, 40))),
	Insn('SLEEP', 1100),
	Insn('FORK_FUNC', Char(37), 3, Function((0, 42))),
	Insn('0x6F', b'@'),
	Insn('0x6F', b'\x10'),
	Insn('SLEEP', 1000),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-700, 700, 12800), 0),
	Insn('CAM_ROTATE', 41, 21, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 17500, 0),
	Insn('CHAR_FLAG1_SET', Char(41), 128),
	Insn('CHAR_FLAG1_SET', Char(42), 128),
	Insn('CHAR_FLAG1_SET', Char(43), 128),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(36), 1),
	Insn('FORK_QUIT', Char(37), 1),
	Insn('CHAR_SET_POS', Char(257), (-700, 0, 10000), 0),
	Insn('CHAR_SET_POS', Char(36), (-1000, 0, 7800), 0),
	Insn('CHAR_SET_POS', Char(37), (0, 0, 7400), 0),
	Insn('FORK', 257, 1, [
		Insn('0x97', Char(254), (0, 0, 30000), 2000, 0),
	]),
	Insn('FORK', 36, 1, [
		Insn('0x97', Char(254), (0, 0, 30000), 2000, 0),
	]),
	Insn('FORK', 37, 1, [
		Insn('0x97', Char(254), (0, 0, 30000), 2000, 0),
	]),
	Insn('CAM_OFFSET', (1400, 2700, 17000), 8000),
	Insn('CAM_ROTATE', 41, 5, 0, 8000),
	Insn('CAM_DISTANCE', 19500, 8000),
	Insn('SLEEP', 7000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(257), 255),
	Insn('0xE6'),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'c0100', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][37] = [
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (600, 0, -1900), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('SLEEP', 500),
	Insn('CHAR_ROTATE', Char(257), 90, 1000),
	Insn('RETURN'),
]

data['code'][38] = [
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-200, 0, -1100), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-200, 0, 40000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('RETURN'),
]

data['code'][39] = [
	Insn('FORK', 36, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 36, 1, [
		Insn('0x95', Char(254), (1800, 0, -2800), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(36), 1),
	Insn('SLEEP', 500),
	Insn('FORK_LOOP', 254, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('RETURN'),
]

data['code'][40] = [
	Insn('FORK_QUIT', Char(36), 2),
	Insn('FORK', 36, 1, [
		Insn('0x95', Char(254), (-600, 0, -1000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(36), 1),
	Insn('FORK', 36, 1, [
		Insn('0x95', Char(254), (-600, 0, 40000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(36), 1),
	Insn('RETURN'),
]

data['code'][41] = [
	Insn('FORK', 37, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 37, 1, [
		Insn('0x95', Char(254), (2000, 0, -1000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(37), 1),
	Insn('SLEEP', 300),
	Insn('FORK_LOOP', 254, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('RETURN'),
]

data['code'][42] = [
	Insn('FORK_QUIT', Char(37), 2),
	Insn('FORK', 37, 1, [
		Insn('0x95', Char(254), (400, 0, 600), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(37), 1),
	Insn('FORK', 37, 1, [
		Insn('0x95', Char(254), (400, 0, 40000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(37), 1),
	Insn('RETURN'),
]

data['code'][43] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch02500', 30),
	Insn('LOAD_CHCP', 'chr/ch00050', 31),
	Insn('LOAD_CHCP', 'chr/ch00150', 32),
	Insn('LOAD_CHCP', 'chr/ch00250', 33),
	Insn('LOAD_CHCP', 'chr/ch00350', 34),
	Insn('CAM_OFFSET', (-500, 3000, 18800), 0),
	Insn('CAM_ROTATE', 30, 17, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 16500, 0),
	Insn('CHAR_SET_CHCP', Char(35), 30),
	Insn('CHAR_SET_FRAME', Char(35), 0),
	Insn('CHAR_FLAG1_UNSET', Char(35), 128),
	Insn('CHAR_FLAG1_UNSET', Char(35), 4),
	Insn('CHAR_SET_POS', Char(35), (-500, 0, 22000), 180),
	Insn('CHAR_SET_POS', Char(257), (-1300, 0, 25000), 180),
	Insn('CHAR_SET_POS', Char(258), (300, 0, 25000), 180),
	Insn('CHAR_SET_POS', Char(259), (-1300, 0, 26600), 180),
	Insn('CHAR_SET_POS', Char(260), (300, 0, 26600), 180),
	Insn('0x4B', Char(9), -1),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis001.itp'),
	Insn('IMG_LOAD', ResId(1), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis002.itp'),
	Insn('IMG_LOAD', ResId(2), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis003.itp'),
	Insn('IMG_LOAD', ResId(3), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis004.itp'),
	Insn('FORK', 35, 1, [
		Insn('0x95', Char(254), (-500, 0, 17500), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-1300, 0, 18000), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (300, 0, 18000), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (-1300, 0, 19600), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (300, 0, 19600), 2000, 0),
	]),
	Insn('CAM_OFFSET', (-500, 1000, 18800), 4000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('FORK_AWAIT', Char(35), 1),
	Insn('FORK', 35, 1, [
		Insn('0x95', Char(254), (-8500, -2800, 17500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 2),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100268V#12P#0005F这里是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10100269V#12P#0105F站前大道的角落……\n'
		'到底有什么东西呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10100270V#11P#0306F说是善后……{wait}'
		'{page}'
		'#10100271V#0301F该不会是要我们来\n'
		'收拾建材什么的吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10100272V#5P#0200F………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FORK_AWAIT', Char(35), 1),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-15500, -3900, 17500), 0),
	Insn('CAM_ROTATE', 45, 16, 0, 0),
	Insn('0x6E', 540, 0),
	Insn('CAM_DISTANCE', 19000, 0),
	Insn('CHAR_SET_POS', Char(35), (-10500, -4000, 17500), 270),
	Insn('CHAR_SET_POS', Char(257), (-8500, -2300, 17000), 270),
	Insn('CHAR_SET_POS', Char(258), (-7540, -1800, 16100), 270),
	Insn('CHAR_SET_POS', Char(259), (-6900, -1500, 17800), 270),
	Insn('CHAR_SET_POS', Char(260), (-5900, -1300, 16700), 270),
	Insn('CAM_OFFSET', (-22500, -3900, 17500), 6000),
	Insn('CAM_ROTATE', 38, 16, 0, 6000),
	Insn('CAM_DISTANCE', 17000, 6000),
	Insn('FORK', 35, 1, [
		Insn('0x95', Char(35), (-19500, -5000, 17500), 2000, 0),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(257), (-22500, -5000, 17000), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(258), (-21540, -5000, 16100), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(259), (-20900, -5000, 17800), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(260), (-19900, -5000, 16700), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(35), 1),
	Insn('FORK', 35, 1, [
		Insn('0x95', Char(254), (-22500, -5000, 19500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(35), 1),
	Insn('CHAR_ROTATE', Char(35), 0, 700),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 315, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 315, 500),
	]),
	Insn('CHAR_ROTATE', Char(35), 180, 500),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(257), Char(35), 500),
	]),
	Insn('FORK_LOOP', 258, 2, [
		Insn('CHAR_WATCH', Char(258), Char(35), 500),
	]),
	Insn('FORK_LOOP', 259, 2, [
		Insn('CHAR_WATCH', Char(259), Char(35), 500),
	]),
	Insn('FORK_LOOP', 260, 2, [
		Insn('CHAR_WATCH', Char(260), Char(35), 500),
	]),
	Insn('0x6F', b'Q'),
	Insn('TEXT_TALK', Char(35), Text(
		'#10100273V#5P#1003F──这扇门的后面，\n'
		'就是克洛斯贝尔市地下广阔的\n'
		'『地下区域』。{wait}'
		'{page}'
		'#10100274V#1000F接下来，你们要潜入到里面去。{wait}'
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
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100275V#12P#0005F哎！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10100276V#12P#0105F潜、潜入……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10100277V#11P#0301F喂喂，\n'
		'这是怎么回事？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(35), Text(
		'#10100278V#5P#1004F这是为了测试你们的\n'
		'综合能力以及实战技巧。{wait}'
		'{page}'
		'#10100279V#1002F地下区域内部\n'
		'徘徊着一些不算\n'
		'太难对付的魔兽。{wait}'
		'{page}'
		'#10100280V你们要一路消灭掉这些魔兽，\n'
		'前进到最深处去。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10100281V#12P#0100F原来如此……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10100282V#11P#0304F实战测试吗……\n'
		'哈，这样一说我反而轻松了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100283V#12P#0011F请、请等一下！{wait}'
		'{page}'
		'#10100284V#0003F测试暂且不提……\n'
		'但为什么要特地进入\n'
		'有魔兽徘徊的地方呢？{wait}'
		'{page}'
		'#10100285V#0001F我们又不是警备队……\n'
		'这应该不是搜查官的工作吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(35), Text(
		'#10100286V#5P#1004F哼哼，这的确不是\n'
		'普通搜查官的工作。{wait}'
		'{page}'
		'#10100287V#1001F──不过，如果是特务支援课的\n'
		'所属成员，那就另当别论了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100288V#12P#0011F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(35), Text(
		'#10100289V#5P#1000F──详情之后再说。{wait}'
		'{page}'
		'#10100290V先收下这个吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x95', Char(35), (-22500, -5000, 18000), 2000, 0),
	Insn('SLEEP', 300),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}赛尔盖将类似可携式终端的东西\n'
		'交给了罗伊德等人。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('SLEEP', 500),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#10100291V#0005F这个是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'#10100292V#0105F新型的战术导力器？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(260), Text(
		'#10100293V#0305F嘿……\n'
		'款式还真时髦啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#10100294V#0203F第５代战术导力器，\n'
		'通称『ＥＮＩＧＭＡ』……{wait}'
		'{page}'
		'#10100295V#0200F终于用于实战配备了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('CHAR_WATCH', Char(35), Char(259), 250),
	Insn('IMG_0xCA', Insn('1', (ResId(0), 0))),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis005.itp'),
	Insn('TEXT_TALK', Char(35), Text(
		'#10100296V#6P#1002F嗯，这是财团的人在\n'
		'前些日子刚送来的新品。{wait}'
		'{page}'
		'#10100297V已经根据你们各自的特性\n'
		'而进行了调整。{wait}'
		'{page}'
		'#10100298V#1004F至于使用方法──缇欧，\n'
		'由你来给他们讲解一下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10100299V#11P#0203F……好吧，虽然很麻烦。{wait}'
		'{page}'
		'#10100300V#0200F有用于新型导力器的结晶回路吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(35), Text(
		'#10100301V#6P#1002F嗯，虽然不多，拿去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'获得了{color 2}各种结晶回路{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('CHAR_WATCH', Char(35), Char(257), 500),
	Insn('TEXT_TALK', Char(35), Text(
		'#10100302V#5P#1000F还有，这才是最关键的东西。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'获得了{item 801}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 801, 1),
	Insn('TEXT_TALK', Char(35), Text(
		'#10100303V#5P#1003F那么，把魔兽都\n'
		'清理完之后，就回总部来吧。{wait}'
		'{page}'
		'#10100304V其它细节问题到时再谈。{wait}'
		'{page}'
		'#10100305V#1005F对了──顺便\n'
		'把这个也给你们吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'获得了{item 1}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'获得了{item 4}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('SLEEP', 300),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}※关于『搜查手册』。{wait}'
		'{page}'
		'※『搜查手册』会自动\n'
		'\u3000记录游戏中发生的\n'
		'\u3000各种事件。{wait}'
		'{page}'
		'※可从营地菜单开启［ＩＴＥＭＳ］\n'
		'\u3000并使用『搜查手册』\n'
		'\u3000或在原野上按下『#165I + #174I』\n'
		'\u3000来观看内容。{wait}'
		'{page}'
		'※各类资料与指南也可在手册中查阅，\n'
		'\u3000请多加运用。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}※关于『战斗手册』。{wait}'
		'{page}'
		'※『战斗手册』会自动\n'
		'\u3000记录曾经交战过的\n'
		'\u3000敌人情报。{wait}'
		'{page}'
		'※同搜查手册一样\n'
		'\u3000使用［ＩＴＥＭＳ］的『战斗手册』\n'
		'\u3000或直接按下『#165I + #175I』\n'
		'\u3000即可查阅其内容。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 1, 1),
	Insn('ITEM_ADD', 4, 1),
	Insn('CAM_OFFSET', (-19500, -3900, 17500), 3000),
	Insn('FORK', 35, 1, [
		Insn('0x95', Char(254), (-20000, -5000, 19500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(35), 1),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 3)),
	Insn('FORK', 35, 1, [
		Insn('0x95', Char(254), (-17500, -5000, 17500), 2000, 0),
	]),
	Insn('SOUND_PLAY', 1082, 0, 255, 100),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100306V#6P#0011F请、请等等，课长！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_AWAIT', Char(35), 1),
	Insn('0x6F', b'\x01'),
	Insn('CHAR_WATCH', Char(35), Char(257), 500),
	Insn('TEXT_TALK', Char(35), Text(
		'#10100307V#11P#1002F──啊，对了，罗伊德。{wait}'
		'{page}'
		'#10100308V暂且由你来当队长吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100309V#6P#0005F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(35), Text(
		'#10100310V#11P#1004F目前拥有正式\n'
		'搜查官资格的人\n'
		'可只有你哦。{wait}'
		'{page}'
		'#10100311V所以就交给你了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(35), 90, 500),
	Insn('FORK', 35, 1, [
		Insn('0x95', Char(254), (-8500, -2800, 17500), 2000, 0),
	]),
	Insn('SLEEP', 2000),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('FORK_AWAIT', Char(35), 1),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-21200, -3900, 17300), 0),
	Insn('CAM_ROTATE', 335, 21, 0, 0),
	Insn('0x6E', 550, 0),
	Insn('CAM_DISTANCE', 17000, 0),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('FORK_QUIT', Char(258), 2),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('CHAR_SET_POS', Char(257), (-22500, -5000, 17300), 90),
	Insn('CHAR_SET_POS', Char(258), (-20900, -5000, 16000), 90),
	Insn('CHAR_SET_POS', Char(259), (-21500, -5000, 18600), 90),
	Insn('CHAR_SET_POS', Char(260), (-19900, -5000, 17300), 90),
	Insn('CHAR_FLAG1_SET', Char(35), 128),
	Insn('0x0D'),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('SOUND_PLAY', 1362, 0, 255, 100),
	Insn('TEXT_TALK', Char(260), Text(
		'#10100312V#12P#0309F哈哈哈，\n'
		'你被派了个苦差事啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10100313V#12P#0104F呵呵，不过有个拥有搜查官资格的\n'
		'人在队里，可就令人安心多了。{wait}'
		'{page}'
		'#10100314V#0102F罗伊德先生，\n'
		'还请多多关照了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(258), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100315V#0000F#5P啊……\n'
		'不用客气，直接叫我的名字就好啦。{wait}'
		'{page}'
		'#10100316V看起来，我们的年龄应该也很相近。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10100317V#12P#0100F是吗？\n'
		'顺带一提，我十八岁……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100318V#0000F#5P啊，那跟我同龄啊。{wait}'
		'{page}'
		'#10100319V#0005F那你们呢……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10100320V#12P#0304F我二十一岁，\n'
		'但也不必对我使用死板的敬语。{wait}'
		'{page}'
		'#10100321V#0300F多关照啦，罗伊德、艾莉。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(258), Char(260), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#10100322V#6P#0102F嗯，彼此彼此。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100323V#0002F#5P嗯，请多关照了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(259), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100324V#6P#0001F……嗯……\n'
		'那，你呢……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('TEXT_TALK', Char(259), Text(
		'#10100325V#11P#0203F──十四岁，有问题吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100326V#6P#0012F没、没有啦～\n'
		'怎么会有问题……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('SOUND_PLAY', 1081, 0, 255, 100),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100327V#6P#0011F呃，十四岁！？{wait}'
	)),
	Insn('SLEEP', 100),
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10100328V#12P#0309F哈哈，怎么了，\n'
		'跟外表看起来一样小嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10100329V#6P#0105F真令人惊讶……这么年轻\n'
		'也能当警察啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100330V#6P#0011F不不！\n'
		'怎么想也都不对劲吧！{wait}'
		'{page}'
		'#10100331V#0006F我记得，普通警察的入职年龄\n'
		'也被限制在十六岁以上……{wait}'
		'{page}'
		'#10100332V#0001F连主日学校都还没毕业的孩子，\n'
		'怎么可能当警察──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10100333V#11P#0200F……确切地说，\n'
		'我并不是警察。{wait}'
		'{page}'
		'#10100334V而是爱普斯泰恩财团派来的\n'
		'测试人员。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100335V#6P#0005F哎……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10100336V#12P#0305F说到爱普斯泰恩，\n'
		'不就是刚才那个战术导力器的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10100337V#6P#0104F是吗……原来如此。{wait}'
		'{page}'
		'#10100338V#0100F我听说，最近数年来，克洛斯贝尔市\n'
		'与财团合作，正在推行某些\n'
		'大规模的计划……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(259), Char(258), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#10100339V#5P#0200F是指『导力网络计划』吧。{wait}'
		'{page}'
		'#10100340V和那个也略有一点关系，\n'
		'但这次财团派我来是另有目的的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 250),
	Insn('SOUND_PLAY', 808, 0, 0, 100),
	Insn('CHAR_SET_CHCP', Char(259), 33),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_SET_POS', Char(259), (-21500, -5000, 18800), 180),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 1268, 0, 255, 100),
	Insn('IMG_0xC9', (ResId(3), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(3), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(3), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(3), 0))),
	Insn('SLEEP', 1000),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#10100341V#0005F那个是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'#10100342V#0105F装设了机械装置的……手杖？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#10100343V#0204F这个叫做『魔导杖』。{wait}'
		'{page}'
		'#10100344V为了对这种新武器进行实战测试，\n'
		'财团才把我派来的。{wait}'
		'{page}'
		'#10100345V#0200F……罗伊德前辈，\n'
		'你可以理解了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(3), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(3), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(3), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(3), 0))),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100346V#6P#0001F等、等一下！{wait}'
		'{page}'
		'#10100347V难道说……\n'
		'你要使用这把手杖参与战斗吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10100348V#11P#0203F……你明明拥有搜查官资格，\n'
		'但理解能力却令人不敢恭维呢。{wait}'
		'{page}'
		'#10100349V#0211F刚才都已经说过了，我是来进行\n'
		'『实战』测试的啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100350V#6P#0011F呜……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10100351V#12P#0304F好啦好啦，\n'
		'在这里争论也无济于事啊。{wait}'
		'{page}'
		'#10100352V#0300F虽然还不知道这扇门后面的\n'
		'地下区域到底有多危险……{wait}'
		'{page}'
		'#10100353V不过，现在还是优先考虑\n'
		'如何才能完成那个大叔\n'
		'硬塞给我们的任务吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10100354V#6P#0103F是啊……\n'
		'虽然还有很多事情没想通。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100355V#6P#0006F………明白了。{wait}'
		'{page}'
		'#10100356V#0000F抱歉，缇欧。\n'
		'如果害你不高兴的话，我在此道歉。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(259), 255),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('CHAR_SET_POS', Char(259), (-21500, -5000, 18600), 180),
	Insn('CHAR_WATCH', Char(259), Char(257), 0),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#10100357V#11P#0203F没什么……我认为\n'
		'你的反应是正常人应有的。{wait}'
		'{page}'
		'#10100358V#0200F话说回来，我的武器\n'
		'是这把『魔导杖』……{wait}'
		'{page}'
		'#10100359V各位的武器都是什么呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100360V#6P#0005F嗯，那么──{wait}'
		'{page}'
		'#10100361V#0000F我的武器，是这个。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 250),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('SOUND_PLAY', 808, 0, 0, 80),
	Insn('CHAR_SET_CHCP', Char(257), 31),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_POS', Char(257), (-22700, -5000, 17300), 90),
	Insn('0x0D'),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('SOUND_PLAY', 1083, 0, 255, 100),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(1), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 0))),
	Insn('SLEEP', 1000),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'#10100362V#0105F这个，是警棍的一种……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(260), Text(
		'#10100363V#0300F『旋棍』啊，\n'
		'是东方式的武器呢。{wait}'
		'{page}'
		'#10100364V听说，相对于杀伤力而言，\n'
		'防御力与压制力更为优秀……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'#10100365V#0102F原来如此，\n'
		'很有警官风格的装备呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(1), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 0))),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('CHAR_SET_POS', Char(257), (-22500, -5000, 17300), 90),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100366V#0004F#5P我也试过很多武器，\n'
		'但还是这个最称手啊。{wait}'
		'{page}'
		'#10100367V#0000F那，艾莉和兰迪的武器呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10100368V#12P#0100F我的……是这个。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 250),
	Insn('SOUND_PLAY', 531, 0, 0, 100),
	Insn('CHAR_SET_CHCP', Char(258), 32),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_ROTATE', Char(258), 0, 0),
	Insn('0x0D'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('SOUND_PLAY', 1173, 0, 255, 100),
	Insn('IMG_0xC9', (ResId(2), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(2), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 0))),
	Insn('SLEEP', 1000),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#10100369V#0205F导力枪……\n'
		'款式有点旧呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#10100370V#0005F好漂亮的枪啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'#10100371V#0102F针对竞技性而专门\n'
		'进行过特殊调整哦。{wait}'
		'{page}'
		'#10100372V虽然是旧式，但瞄准的精确性\n'
		'应该还是值得期待的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(2), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(2), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 0))),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(258), 255),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#10100373V#11P#0302F哦，信心十足嘛。{wait}'
		'{page}'
		'#10100374V#0300F那么，我的是这家伙。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 250),
	Insn('SOUND_PLAY', 808, 0, 0, 100),
	Insn('CHAR_SET_CHCP', Char(260), 34),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('CHAR_SET_POS', Char(260), (-19500, -5000, 17300), 270),
	Insn('0x0D'),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(260), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(260), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(260), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('SOUND_PLAY', 1363, 0, 255, 100),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('SLEEP', 1000),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#10100375V#0001F那个是……\n'
		'相当巨大的武器啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'#10100376V#0101F形状很像是中世纪的骑士\n'
		'所使用的『斧枪』啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#10100377V#0200F……我在财团的武器工房中\n'
		'见过这个。{wait}'
		'{page}'
		'#10100378V上面装设了可以将导力\n'
		'转化成冲击力的组件吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(260), Text(
		'#10100379V#0304F嗯，这是冲击斧枪。{wait}'
		'{page}'
		'#10100380V#0300F虽然重了点，导致操作不便，\n'
		'不过攻击的威力可是非常了得哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(260), 255),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('CHAR_SET_POS', Char(260), (-19900, -5000, 17300), 270),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100381V#0003F#5P原来如此……{wait}'
		'{page}'
		'#10100382V#0000F虽然还不清楚缇欧的魔导杖\n'
		'具体是什么原理……{wait}'
		'{page}'
		'#10100383V但要和魔兽作战的话，\n'
		'这种阵容应该还算是平衡吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('TEXT_TALK', Char(258), Text(
		'#10100384V#12P#0100F的确……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10100385V#12P#0300F嗯，说不定正是连这一点也考虑到了，\n'
		'所以才会把我们几个召集起来的吧。{wait}'
		'{page}'
		'#10100386V那位大叔看起来没精打采的，\n'
		'其实可不是等闲之辈啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10100387V#11P#0203F……是啊。{wait}'
		'{page}'
		'#10100388V#0200F关于这把魔导杖的性能，\n'
		'以后再慢慢说明……{wait}'
		'{page}'
		'#10100389V要先对刚才配发给我们的\n'
		'战术导力器的性能\n'
		'进行一下说明吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('MENU', 0, -1, -1, 0, Text(
		'请缇欧说明一下\n'
		'还是算了\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('FORK', 258, 1, [
				Insn('CHAR_WATCH', Char(254), Char(259), 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 260, 1, [
				Insn('CHAR_WATCH', Char(254), Char(259), 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 257, 1, [
				Insn('CHAR_WATCH', Char(254), Char(259), 500),
			]),
			Insn('SLEEP', 50),
			Insn('TEXT_TALK', Char(257), Text(
				'#10100390V#0002F#5P嗯，麻烦你了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#10100391V#11P#0203F……明白了。{wait}'
				'{page}'
				'#10100392V#0200F一般来说，所谓的『导力器』，\n'
				'是指利用导力能源\n'
				'而引发各种现象的机械。{wait}'
				'{page}'
				'#10100393V从照明和冷暖气设备等日用品，\n'
				'到车辆与铁路的动力，\n'
				'全都使用了导力器的能量。{wait}'
				'{page}'
				'#10100394V而所谓的『战术导力器』，\n'
				'则是专门针对个人战斗而进行了\n'
				'特殊处理的小型可携式导力器。{wait}'
				'{page}'
				'#10100395V#0203F这次发配给我们的，\n'
				'是由『爱普斯泰恩财团』开发的\n'
				'最新型战术导力器。{wait}'
				'{page}'
				'#10100396V和以前的型号一样，\n'
				'它需要镶嵌被通称为『回路』的\n'
				'结晶回路来进行运作。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#10100397V#6P#0105F结晶回路……\n'
				'就是用七耀石碎片制作而成的\n'
				'导力器专用回路吧。{wait}'
				'{page}'
				'#10100398V#0100F课长刚才好像\n'
				'给了我们几个……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#10100399V#11P#0200F嗯，只要把它嵌入\n'
				'战术导力器中已解锁过的\n'
				'插槽内，就能发挥作用了。{wait}'
				'{page}'
				'#10100400V另外，镶嵌有结晶回路的线\n'
				'都有『属性值』，当其达到一定程度时，\n'
				'就可以使用导力魔法了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#10100401V#5P#0004F针对魔兽的种类，\n'
				'有时候，与其用武器直接攻击，\n'
				'不如使用魔法更为有效。{wait}'
				'{page}'
				'#10100402V#0000F所以，在和魔兽进行战斗之前，\n'
				'一定要事先\n'
				'准备好才行。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#10100403V#6P#0100F原来如此……\n'
				'这么说，在与魔兽战斗中，\n'
				'这也是十分重要的一环呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#10100404V#12P#0304F毕竟连游击士协会\n'
				'和警备队都将其投入使用了嘛。\n'
				'这么想肯定没错啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#10100405V#11P#0208F还有……对了。{wait}'
				'{page}'
				'#10100406V#0200F战术导力器依照个人的特性进行过调整，\n'
				'因此，根据所有者的不同，\n'
				'导力器的构造也会存在差异。{wait}'
				'{page}'
				'#10100407V例如，某些插槽会有属性限制，\n'
				'或是连接插槽之间的线的形态有所不同。{wait}'
				'{page}'
				'#10100408V#0203F总之，至于具体的区别，\n'
				'只要稍后自行比较一下就知道了。{wait}'
				'{page}'
				'#10100409V#0200F关于导力魔法的具体使用方法，\n'
				'还是在实战中自行摸索为好……\n'
				'说明就到此为止吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#10100410V#6P#0102F多亏你的解释，我已经非常明白了。\n'
				'谢谢你，缇欧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#10100411V#11P#0203F……不客气。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#10100412V#12P#0305F话说，虽然是新型，\n'
				'但使用方法好像和\n'
				'以前的没什么区别啊？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#10100413V#11P#0203F嗯，如果有过使用旧型号的经验，\n'
				'只需按照之前的感觉操作即可。{wait}'
				'{page}'
				'#10100414V#0200F要说区别的话，\n'
				'主要就在于这次的升级版\n'
				'增加了其它功能……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(257), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('EMOTE', Char(258), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('EMOTE', Char(260), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(257), Text(
				'#10100415V#5P#0005F……其它功能？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#10100416V#11P#0204F不过，目前应该还用不上，\n'
				'所以请不必在意。{wait}'
				'{page}'
				'#10100417V#0200F现在还是优先\n'
				'完成此次任务吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#10100418V#5P#0000F嗯，也对。\n'
				'（……稍微有些在意呢……）{wait}'
				'{page}'
				'#10100419V#0004F……总而言之，\n'
				'在进入地下区域之前，\n'
				'先调整好战术导力器吧。{wait}'
				'{page}'
				'#10100420V#0000F镶嵌好课长给的结晶回路，\n'
				'然后再进去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#10100421V#12P#0100F嗯，是啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#10100422V#12P#0300F那好，赶快做好准备吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('ITEM_ADD', 100, 1),
			Insn('ITEM_ADD', 106, 1),
			Insn('ITEM_ADD', 109, 1),
			Insn('ITEM_ADD', 121, 1),
			Insn('FADE_ON', 300, Color(0x00000000), 100),
			Insn('SLEEP', 300),
			Insn('SOUND_PLAY', 828, 0, 0, 100),
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}请为全体成员的战术导力器镶嵌结晶回路。{wait}'
				'{page}'
				'从营地菜单开启［ＯＲＢＭＥＮＴ］，\n'
				'再选择［ＱＵＡＲＴＺ］即可安装结晶回路。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('FLAG_SET', Flag(544)),
			Insn('0xC7', b'\x00\x00\x00\x08\x00'),
			Insn('BREAK'),
		],
		1: [
			Insn('FORK', 258, 1, [
				Insn('CHAR_WATCH', Char(254), Char(259), 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 260, 1, [
				Insn('CHAR_WATCH', Char(254), Char(259), 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 257, 1, [
				Insn('CHAR_WATCH', Char(254), Char(259), 500),
			]),
			Insn('SLEEP', 50),
			Insn('TEXT_TALK', Char(257), Text(
				'#10100423V#5P#0000F不……没问题的。{wait}'
				'{page}'
				'#10100424V看起来，使用方法\n'
				'好像和以前的型号\n'
				'没什么变化嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#10100425V#11P#0203F嗯，那倒是。{wait}'
				'{page}'
				'#10100426V#0200F要说区别的话，\n'
				'主要就在于这次的升级版\n'
				'增加了其它功能……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(257), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('EMOTE', Char(258), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('EMOTE', Char(260), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(257), Text(
				'#10100427V#5P#0005F……其它功能？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#10100428V#11P#0204F不过，目前应该还用不上，\n'
				'所以请不必在意。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#10100429V#5P#0006F（……稍微有些在意呢……）{wait}'
				'{page}'
				'#10100430V#0000F那么……\n'
				'总之，就先进去看看吧。{wait}'
				'{page}'
				'#10100431V首先还是要注意安全，\n'
				'谨慎前进为好啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#10100432V#12P#0100F嗯，是啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#10100433V#11P#0200F……明白了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#10100434V#12P#0300F那好，快进去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x42', Party(0), 109, 0),
			Insn('0x42', Party(1), 121, 0),
			Insn('0x42', Party(2), 100, 0),
			Insn('0x42', Party(3), 106, 0),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x32', Party(1), 0, 3),
	Insn('PARTY_CRAFT_REMOVE', Party(1), -1),
	Insn('0x38', Party(1), 128, 1),
	Insn('0x42', Party(1), 1020, -1),
	Insn('0x42', Party(1), 1500, -1),
	Insn('0x42', Party(1), 1600, -1),
	Insn('PARTY_CRAFT_ADD', Party(1), 160),
	Insn('PARTY_CRAFT_ADD', Party(1), 255),
	Insn('PARTY_SET_SBREAK', Party(1), 6, 255),
	Insn('0x32', Party(2), 0, 3),
	Insn('PARTY_CRAFT_REMOVE', Party(2), -1),
	Insn('0x38', Party(2), 128, 1),
	Insn('0x42', Party(2), 1040, -1),
	Insn('0x42', Party(2), 1500, -1),
	Insn('0x42', Party(2), 1600, -1),
	Insn('PARTY_CRAFT_ADD', Party(2), 170),
	Insn('PARTY_CRAFT_ADD', Party(2), 260),
	Insn('PARTY_SET_SBREAK', Party(2), 6, 260),
	Insn('0x32', Party(3), 0, 3),
	Insn('PARTY_CRAFT_REMOVE', Party(3), -1),
	Insn('0x38', Party(3), 128, 1),
	Insn('0x42', Party(3), 1060, -1),
	Insn('0x42', Party(3), 1500, -1),
	Insn('0x42', Party(3), 1600, -1),
	Insn('PARTY_CRAFT_ADD', Party(3), 180),
	Insn('PARTY_CRAFT_ADD', Party(3), 265),
	Insn('PARTY_SET_SBREAK', Party(3), 6, 265),
	Insn('0x4C', Char(9), -1),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('CAM_OFFSET', (-21000, -2800, 17500), 0),
	Insn('CAM_ROTATE', 45, 10, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 18500, 0),
	Insn('CHAR_SET_POS', Char(0), (-21000, -5000, 17500), 270),
	Insn('CHAR_SET_POS', Char(1), (-21000, -5000, 17500), 270),
	Insn('CHAR_SET_POS', Char(2), (-21000, -5000, 17500), 270),
	Insn('CHAR_SET_POS', Char(3), (-21000, -5000, 17500), 270),
	Insn('FLAG_SET', Flag(514)),
	Insn('QUEST', 60, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 60, Insn('TASK_SET', 0)),
	Insn('ACHIEVEMENT', b'\x01\x00'),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('0xDE', b'\x00\x00')), Insn('END')]), [
			Insn('SLEEP', 1500),
			Insn('FADE_ON', 300, Color(0x00000000), 100),
			Insn('0x0D'),
			Insn('SOUND_PLAY', 828, 0, 0, 100),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}※由于收到了搜查手册，\n'
				'\u3000因此获得了『新人搜查官』的成就。{wait}'
				'{page}'
				'※同理，在游戏进行的过程中，\n'
				'\u3000只要满足了一定条件，\n'
				'\u3000就可以获得『成就』。{wait}'
				'{page}'
				'※『成就』含有一定的点数，\n'
				'\u3000在游戏通关之后，\n'
				'\u3000可以使用这些点数来开启各种功能。{wait}'
				'{page}'
				'※进入营地菜单开启［SYSTEM］，\n'
				'\u3000选择［RECORD］，\n'
				'\u3000即可确认已获得的成就。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('0x5A'),
			Insn('FADE_OFF', 300, Color(0x00000000)),
		]),
		(None, []),
	]),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][44] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch06000', 30),
	Insn('LOAD_CHCP', 'chr/ch02400', 31),
	Insn('LOAD_CHCP', 'apl/ch50010', 32),
	Insn('LOAD_CHCP', 'apl/ch50011', 33),
	Insn('SOUND_LOAD', 806),
	Insn('CAM_OFFSET', (-22500, -4100, 17300), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 18500, 0),
	Insn('CHAR_SET_POS', Char(258), (-22000, -5000, 21000), 180),
	Insn('CHAR_SET_POS', Char(257), (-22000, -5000, 21000), 180),
	Insn('CHAR_SET_POS', Char(259), (-22000, -5000, 21000), 180),
	Insn('CHAR_SET_POS', Char(260), (-22000, -5000, 21000), 180),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(408), (-17100, -5000, 19300), 135),
	Insn('CHAR_SET_POS', Char(407), (-18000, -5000, 19300), 135),
	Insn('FORK_LOOP', 408, 2, [
		Insn('CHAR_WATCH', Char(254), Char(38), 500),
	]),
	Insn('FORK_LOOP', 407, 2, [
		Insn('CHAR_WATCH', Char(254), Char(38), 500),
	]),
	Insn('CHAR_SET_CHCP', Char(38), 32),
	Insn('CHAR_SET_FRAME', Char(38), 0),
	Insn('CHAR_SET_CHCP', Char(39), 31),
	Insn('CHAR_SET_FRAME', Char(39), 0),
	Insn('CHAR_FLAG1_UNSET', Char(38), 4),
	Insn('CHAR_FLAG1_UNSET', Char(39), 4),
	Insn('CHAR_SET_POS', Char(38), (-16000, -5000, 17300), 270),
	Insn('CHAR_SET_POS', Char(39), (-18000, -5000, 17300), 90),
	Insn('CHAR_FLAG1_UNSET', Char(38), 128),
	Insn('CHAR_FLAG2_UNSET', Char(38), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(39), 128),
	Insn('CHAR_FLAG2_UNSET', Char(39), 32768),
	Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xfc\xc3\xb6', 40, 120, 0),
	Insn('OBJ_SET_FRAME', Object(255), 'sky', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'sky1', Insn('1', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'sd_mul', Insn('0', 1)),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis001.itp'),
	Insn('IMG_LOAD', ResId(1), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu02100.itp'),
	Insn('IMG_LOAD', ResId(2), 180, 0, b'\xb4\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis007.itp'),
	Insn('EFF_LOAD', ResId(0), 'event\\eva02_00.eff'),
	Insn('OBJ_FLAG_UNSET', Object(0), 16),
	Insn('FORK_FUNC', Char(38), 3, Function((0, 45))),
	Insn('CAM_DISTANCE', 19500, 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('SLEEP', 500),
	Insn('0x71', Object(0), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 102, 0, 0, 100),
	Insn('0x79', b'\x00\x00'),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 47))),
	Insn('SLEEP', 700),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 48))),
	Insn('SLEEP', 700),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 49))),
	Insn('SLEEP', 700),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 50))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100753V#6P#0005F怎么……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-16500, -4100, 17300), 2000),
	Insn('CAM_DISTANCE', 19000, 2000),
	Insn('0x6F', b'\x01'),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(1), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('TEXT_SET_NAME', Translate('女性')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#10100754V哎呀～亚里欧斯先生！\n'
		'您又立了大功呢！{wait}'
		'{page}'
		'#10100755V在城市设施管理不善的情况下，\n'
		'以高超的技艺，漂亮地\n'
		'拯救了陷入危机的少年……！{wait}'
		'{page}'
		'#10100756V一定要在最新刊上\n'
		'登一条独家消息！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(1), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 0))),
	Insn('TEXT_TALK', Char(408), Text(
		'#10100757V#5P太棒了！\n'
		'我们要上杂志了吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(407), Text(
		'#10100758V#1P但、但是，\n'
		'这好像并不值得高兴……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(39), Text(
		'#10100759V#6P#1403F……格蕾丝。\n'
		'最好不要大肆宣传。{wait}'
		'{page}'
		'#10100760V#1400F虽然市内的管理确实存在问题，\n'
		'但这两个孩子的行为也有一定责任。{wait}'
		'{page}'
		'#10100761V有失偏颇的报道，我可不敢苟同。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(38), Translate('女性'), Text(
		'#10100762V#11P#2109F哪里哪里，我纯粹就是在\n'
		'迎合读者的喜好而已啦丅{wait}'
		'{page}'
		'#10100763V#2102F──而且，这次好像\n'
		'还有有趣的嘉宾呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100764V#0001F#5P！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_QUIT', Char(38), 3),
	Insn('CAM_OFFSET', (-20080, -4100, 17580), 2500),
	Insn('CAM_DISTANCE', 19500, 2500),
	Insn('CHAR_SET_CHCP', Char(38), 30),
	Insn('CHAR_SET_FRAME', Char(38), 0),
	Insn('FORK', 38, 1, [
		Insn('0x96', Char(254), (-18000, -5000, 16000), 2000, 1),
	]),
	Insn('FORK_AWAIT', Char(38), 1),
	Insn('FORK', 38, 1, [
		Insn('0x96', Char(254), (-20200, -5000, 17600), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 39, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(38), 1),
	Insn('0x6F', b'\x11'),
	Insn('FORK_FUNC', Char(38), 3, Function((0, 46))),
	Insn('TEXT_TALK2', Char(38), Translate('女性'), Text(
		'#10100765V#11P#2104F肩负着克洛斯贝尔警察局未来的\n'
		'『特务支援课』首次出动！{wait}'
		'{page}'
		'#10100766V然而，由于实力不足，\n'
		'仍然如同往常一般，被游击士抢走了功劳！{wait}'
		'{page}'
		'#10100767V#2110F啊，这些年轻人们深切感受到了自己的不成熟，\n'
		'而他们又能否通过等待在前方的\n'
		'种种试炼呢！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100768V#6P#0011F说、说什么呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10100769V#6P#0301F（喂喂……\n'
		'\u3000到底是怎么回事？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10100770V#6P#0200F（好像是\n'
		'\u3000媒体的人……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10100771V#6P#0106F（……看样子，\n'
		'\u3000似乎是《克洛斯贝尔时报周刊》的\n'
		'\u3000记者呢。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(39), Text(
		'#10100772V#11P#1403F──我不赞成\n'
		'过早对他们妄下定论。{wait}'
		'{page}'
		'#10100773V况且，最先解救了\n'
		'两个孩子的也是他们。{wait}'
		'{page}'
		'#10100774V#1400F不过，似乎确实还不够成熟啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100775V#6P#0001F！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(38), Translate('女性'), Text(
		'#10100776V#11P#2106F哎呀呀，果然是这么回事啊。{wait}'
		'{page}'
		'#10100777V#2100F好，我会在报道里好好描述一番的，\n'
		'不过，你们不用太介意啦～{wait}'
		'{page}'
		'#10100778V#2109F就当作是姐姐对你们的声援，\n'
		'今后也要多加努力哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_QUIT', Char(38), 3),
	Insn('CHAR_SET_CHCP', Char(38), 30),
	Insn('CHAR_SET_FRAME', Char(38), 0),
	Insn('CHAR_WATCH', Char(38), Char(39), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK2', Char(38), Translate('女性'), Text(
		'#10100779V#6P#2110F──那么，亚里欧斯先生。\n'
		'请让我做一次独家专访吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(39), Text(
		'#10100780V#11P#1403F关于这件事，\n'
		'之前我已经拒绝过了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(39), 90, 500),
	Insn('FORK_QUIT', Char(408), 2),
	Insn('FORK_QUIT', Char(407), 2),
	Insn('FORK', 39, 1, [
		Insn('0x97', Char(254), (12000, 0, 0), 2000, 0),
	]),
	Insn('FORK', 408, 2, [
		Insn('CHAR_WATCH', Char(254), Char(39), 500),
	]),
	Insn('FORK', 407, 2, [
		Insn('CHAR_WATCH', Char(254), Char(39), 500),
	]),
	Insn('SLEEP', 400),
	Insn('FORK_FUNC', Char(408), 3, Function((0, 51))),
	Insn('SLEEP', 400),
	Insn('FORK_FUNC', Char(407), 3, Function((0, 52))),
	Insn('SLEEP', 400),
	Insn('FORK', 38, 1, [
		Insn('0x97', Char(254), (15000, 0, 0), 2000, 0),
	]),
	Insn('SLEEP', 4000),
	Insn('CAM_OFFSET', (-22500, -4000, 17300), 2000),
	Insn('CAM_ROTATE', 40, 23, 0, 2000),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('SLEEP', 50),
	Insn('EMOTE_STOP', Char(258)),
	Insn('SLEEP', 50),
	Insn('EMOTE_STOP', Char(259)),
	Insn('SLEEP', 50),
	Insn('EMOTE_STOP', Char(260)),
	Insn('0x6F', b'\x01'),
	Insn('FORK_AWAIT', Char(39), 1),
	Insn('FORK_AWAIT', Char(408), 3),
	Insn('FORK_AWAIT', Char(407), 3),
	Insn('FORK_AWAIT', Char(38), 1),
	Insn('CHAR_FLAG1_SET', Char(39), 128),
	Insn('CHAR_FLAG2_SET', Char(39), 32768),
	Insn('CHAR_FLAG1_SET', Char(38), 128),
	Insn('CHAR_FLAG2_SET', Char(38), 32768),
	Insn('TEXT_TALK', Char(259), Text(
		'#10100781V#6P#0211F……刚才那算什么啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10100782V#0301F#6P好像是打算拿我们当小丑，\n'
		'让人看笑话呢……{wait}'
		'{page}'
		'#10100783V#0306F那位姐姐算是我喜欢的类型，\n'
		'不过，性格好像有点奇怪啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10100784V#0106F#6P唉……\n'
		'问题并不在这里吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(258), Char(257), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#10100785V#0101F#5P那么，罗伊德，现在该怎么办？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('CHAR_WATCH', Char(257), Char(258), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100786V#11P#0005F啊……{wait}'
		'{page}'
		'#10100787V#0006F……赛尔盖课长交给我们的\n'
		'课题也算是完成了……\n'
		'先回警察局总部去吧。{wait}'
		'{page}'
		'#10100788V#0008F关于孩子们的事情，\n'
		'也需要详细报告……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 806, 0, 2, 100),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100789V#11P#0011F这个是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_SET', Char(257), 32),
	Insn('CHAR_FLAG1_SET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 33),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100790V#0005F#11P刚才发给我们的\n'
		'战术导力器……{wait}'
		'{page}'
		'#10100791V#0001F莫非有通讯\n'
		'联系吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#10100792V#0203F#6P嗯，看来是这样呢。{wait}'
		'{page}'
		'#10100793V#0200F按下那个红色按钮，\n'
		'就能切换到通讯模式。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100794V#0000F#11P哦，这个吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('SOUND_STOP', 806),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('SLEEP', 300),
	Insn('IMG_0xC9', (ResId(2), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('FADE_ON', 500, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#10100795V#0001F喂……\n'
		'我是罗伊德丄班宁斯。{wait}'
		'{page}'
		'#10100796V是赛尔盖课长吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('SOUND_PLAY', 2083, 0, 255, 100),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('女孩的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#10100797V啊，罗伊德警官！{wait}'
		'{page}'
		'#10100798V那个，是我。\n'
		'刚才在接待处见过面的──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#10100799V#0005F啊，是刚才的……{wait}'
		'{page}'
		'#10100800V#0000F嗯，请问有什么事呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('柜台小姐的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#10100801V嗯，是这样的……{wait}'
		'{page}'
		'#10100802V那个，能麻烦你们尽快\n'
		'返回警察局总部吗？{wait}'
		'{page}'
		'#10100803V副局长好像找你们有事……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#10100804V#0011F副、副局长……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(2), 3), Color(0x00FFFFFF), 2000, 0),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
	Insn('CHAR_FLAG1_UNSET', Char(257), 32),
	Insn('CHAR_FLAG1_UNSET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0x2F', b'\x96\x00'),
	Insn('0x2F', b'\x97\x00'),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('SOUND_STOP', 806),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'c1160', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][45] = [
	Insn('SLEEP', 1000),
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_SET_CHCP', Char(38), 30),
		Insn('CHAR_SET_FRAME', Char(38), 0),
		Insn('FORK', 38, 1, [
			Insn('0x96', Char(254), (-16000, -5000, 17000), 2000, 0),
		]),
		Insn('FORK_AWAIT', Char(38), 1),
		Insn('CHAR_SET_CHCP', Char(38), 32),
		Insn('CHAR_SET_FRAME', Char(38), 0),
		Insn('SLEEP', 50),
		Insn('SOUND_PLAY', 817, 0, 0, 100),
		Insn('EFF_PLAY', (ResId(0), -1), Char(38), 192, 0, 0, 1200, 0, 400, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
		Insn('SLEEP', 1000),
		Insn('CHAR_SET_CHCP', Char(38), 30),
		Insn('CHAR_SET_FRAME', Char(38), 0),
		Insn('FORK', 38, 1, [
			Insn('0x96', Char(254), (-16000, -5000, 17600), 2000, 0),
		]),
		Insn('FORK_AWAIT', Char(38), 1),
		Insn('CHAR_SET_CHCP', Char(38), 32),
		Insn('CHAR_SET_FRAME', Char(38), 0),
		Insn('SLEEP', 50),
		Insn('SOUND_PLAY', 817, 0, 0, 100),
		Insn('EFF_PLAY', (ResId(0), -1), Char(38), 192, 0, 0, 1200, 0, 400, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
		Insn('SLEEP', 1000),
	]),
	Insn('RETURN'),
]

data['code'][46] = [
	Insn('SLEEP', 1000),
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_SET_CHCP', Char(38), 30),
		Insn('CHAR_SET_FRAME', Char(38), 0),
		Insn('FORK', 38, 1, [
			Insn('0x96', Char(254), (-20200, -5000, 17300), 2000, 0),
		]),
		Insn('FORK_AWAIT', Char(38), 1),
		Insn('CHAR_SET_CHCP', Char(38), 32),
		Insn('CHAR_SET_FRAME', Char(38), 0),
		Insn('SLEEP', 50),
		Insn('SOUND_PLAY', 817, 0, 0, 100),
		Insn('EFF_PLAY', (ResId(0), -1), Char(38), 192, 0, 0, 1200, 0, 400, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
		Insn('SLEEP', 1000),
		Insn('CHAR_SET_CHCP', Char(38), 30),
		Insn('CHAR_SET_FRAME', Char(38), 0),
		Insn('FORK', 38, 1, [
			Insn('0x96', Char(254), (-20200, -5000, 17900), 2000, 0),
		]),
		Insn('FORK_AWAIT', Char(38), 1),
		Insn('CHAR_SET_CHCP', Char(38), 32),
		Insn('CHAR_SET_FRAME', Char(38), 0),
		Insn('SLEEP', 50),
		Insn('SOUND_PLAY', 817, 0, 0, 100),
		Insn('EFF_PLAY', (ResId(0), -1), Char(38), 192, 0, 0, 1200, 0, 400, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
		Insn('SLEEP', 1000),
	]),
	Insn('RETURN'),
]

data['code'][47] = [
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-22000, -5000, 19500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-21700, -5000, 17100), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('CHAR_ROTATE', Char(257), 90, 500),
	Insn('RETURN'),
]

data['code'][48] = [
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (-22000, -5000, 19500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (-22500, -5000, 17700), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('CHAR_ROTATE', Char(258), 90, 500),
	Insn('RETURN'),
]

data['code'][49] = [
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (-22000, -5000, 19500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (-23900, -5000, 17000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('CHAR_ROTATE', Char(259), 90, 500),
	Insn('RETURN'),
]

data['code'][50] = [
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (-22000, -5000, 19500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (-22700, -5000, 19100), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('CHAR_ROTATE', Char(260), 90, 500),
	Insn('0x71', Object(0), b'\n\x00', 0, 0),
	Insn('RETURN'),
]

data['code'][51] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-16000, -5000, 17000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x97', Char(254), (12000, 0, 0), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][52] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-16900, -5000, 17000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x97', Char(254), (12000, 0, 0), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][53] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch28300', 30),
	Insn('LOAD_CHCP', 'chr/ch28400', 31),
	Insn('CAM_OFFSET', (10000, -2500, 2000), 0),
	Insn('CAM_ROTATE', 55, 25, 0, 0),
	Insn('0x6E', 800, 0),
	Insn('CAM_DISTANCE', 43000, 0),
	Insn('CHAR_SET_POS', Char(257), (-4500, -10300, -1900), 0),
	Insn('CHAR_SET_POS', Char(258), (-4500, -10300, -1900), 0),
	Insn('CHAR_SET_POS', Char(259), (-4500, -10300, -1900), 0),
	Insn('CHAR_SET_POS', Char(260), (-4500, -10300, -1900), 0),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(40), 128),
	Insn('0x78', b'\x0b', Char(40)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(40), (40000, -11500, -11500), 0),
	Insn('0xD3', Char(40), 0, 270000, 0, 0),
	Insn('OBJ_FLAG_UNSET', Object(11), 4),
	Insn('OBJ_FLAG_SET', Object(11), 4096),
	Insn('CHAR_SET_CHCP', Char(41), 30),
	Insn('CHAR_SET_FRAME', Char(41), 0),
	Insn('CHAR_FLAG1_UNSET', Char(41), 128),
	Insn('CHAR_FLAG2_UNSET', Char(41), 32768),
	Insn('CHAR_SET_POS', Char(41), (5000, 0, 0), 180),
	Insn('CHAR_FLAG1_SET', Char(41), 32768),
	Insn('CHAR_SET_CHCP', Char(42), 31),
	Insn('CHAR_SET_FRAME', Char(42), 0),
	Insn('CHAR_FLAG1_UNSET', Char(42), 128),
	Insn('CHAR_FLAG2_UNSET', Char(42), 32768),
	Insn('CHAR_SET_POS', Char(42), (5000, 0, -1800), 0),
	Insn('CHAR_FLAG1_SET', Char(42), 32768),
	Insn('CHAR_SET_CHCP', Char(43), 16),
	Insn('CHAR_SET_FRAME', Char(43), 0),
	Insn('CHAR_FLAG1_UNSET', Char(43), 128),
	Insn('CHAR_FLAG2_UNSET', Char(43), 32768),
	Insn('CHAR_SET_POS', Char(43), (0, 0, 22000), 180),
	Insn('CHAR_FLAG1_SET', Char(43), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('0x4B', Char(9), -1),
	Insn('CHAR_SET_POS', Char(9), (-2400, 0, -8000), 270),
	Insn('CHAR_FLAG1_SET', Char(9), 32768),
	Insn('FORK_FUNC', Char(9), 0, Function((0, 0))),
	Insn('0x11', b'\xf0\xf2\xfc', 20, 100, 0),
	Insn('0x7D', b'\xc8\xdc\xe6\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xf0\xf2\xfc', 30, 110, 8000),
	Insn('0x7D', b'\xdc\xf0\xff\x00@\x1f\x00\x00'),
	Insn('SOUND_PLAY', 829, 0, 0, 100),
	Insn('CAM_OFFSET', (-5000, -2500, 2000), 10000),
	Insn('CAM_DISTANCE', 48000, 10000),
	Insn('FORK', 43, 1, [
		Insn('0x96', Char(254), (0, 0, -2000), 2000, 0),
	]),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(40), 3, Function((0, 54))),
	Insn('SLEEP', 2000),
	Insn('SOUND_PLAY', 451, 0, 0, 100),
	Insn('SLEEP', 4000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(40), 3),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('FLAG_SET', Flag(738)),
	Insn('NEW_SCENE', 'c0100', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][54] = [
	Insn('FORK', 40, 1, [
		Insn('0x96', Char(254), (-80000, -11500, -11500), 15000, 0),
	]),
	Insn('FORK_AWAIT', Char(40), 1),
	Insn('RETURN'),
]

data['code'][55] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50011', 30),
	Insn('SOUND_LOAD', 806),
	Insn('CAM_OFFSET', (-21900, -3900, 19000), 0),
	Insn('CAM_ROTATE', 37, 20, 0, 0),
	Insn('0x6E', 550, 0),
	Insn('CAM_DISTANCE', 17000, 0),
	Insn('CHAR_SET_POS', Char(257), (-21900, -5000, 22000), 180),
	Insn('CHAR_SET_POS', Char(258), (-21900, -5000, 22000), 180),
	Insn('CHAR_SET_POS', Char(259), (-21900, -5000, 22000), 180),
	Insn('CHAR_SET_POS', Char(260), (-21900, -5000, 22000), 180),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('IMG_LOAD', ResId(0), 180, 0, b'\xb4\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis007.itp'),
	Insn('CAM_DISTANCE', 18000, 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('OBJ_FLAG_UNSET', Object(0), 16),
	Insn('0x71', Object(0), b'\x00\x00', 10, 0),
	Insn('0x79', b'\x00\x00'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (-22600, -5000, 18300), 2000, 0),
	]),
	Insn('SLEEP', 400),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (-21300, -5000, 18300), 2000, 0),
	]),
	Insn('SLEEP', 400),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (-22600, -5000, 19600), 2000, 0),
	]),
	Insn('SLEEP', 400),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (-21300, -5000, 19600), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('0x6F', b'\x10'),
	Insn('0x71', Object(0), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 102, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 806, 0, 2, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x79', b'\x00\x00'),
	Insn('OBJ_FLAG_SET', Object(0), 16),
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
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#10300113V#0005F您好，我是特务支援课的\n'
		'罗伊德丄班宁斯。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('赛尔盖的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#10300114V哦～是我。{wait}'
		'{page}'
		'#10300115V情况怎么样了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#10300116V#0000F赛尔盖课长。{wait}'
		'{page}'
		'#10300117V#0000F嗯，刚刚打倒了\n'
		'通缉中的魔兽。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('赛尔盖的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#10300118V很好，顺利就好。{wait}'
		'{page}'
		'#10300119V你们现在在哪里？{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#10300120V#0005F嗯……\n'
		'地下区域的出口附近。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('赛尔盖的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#10300121V唔，那也不算\n'
		'很远嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#10300122V#0011F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('赛尔盖的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#10300123V──现在交给你们\n'
		'一件紧急任务。{wait}'
		'{page}'
		'#10300124V将其它支援请求延后也没关系，\n'
		'总之优先处理这个吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#10300125V#0001F──明白！{wait}'
		'{page}'
		'#10300126V那么……\n'
		'到底是什么任务！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('赛尔盖的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#10300127V位置是城市东南角的旧市街……\n'
		'你们尽快赶往那边吧。{wait}'
		'{page}'
		'#10300128V有居民报警了。{wait}'
		'{page}'
		'#10300129V据说有两组危险的不良分子\n'
		'就要开始斗殴了。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#10300130V#0005F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('赛尔盖的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#10300131V赶快去阻止，要解决得干净俐落。\n'
		'──就这样。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('SOUND_PLAY', 825, 0, 0, 100),
	Insn('SLEEP', 200),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'{color 0}#10300132V#6P#0011F请、请等一下！{wait}'
		'{page}'
		'#10300133V阻止斗殴……\n'
		'这也属于我们的工作吗──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(257), 6),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300134V#6P#0013F──怎么已经挂断了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10300135V#0105F课长打来的？\n'
		'到底怎么回事？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#10300136V#0302F看这样子，\n'
		'好像不是什么好事吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(257), 32),
	Insn('CHAR_FLAG1_UNSET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('0x0D'),
	Insn('CHAR_WATCH', Char(257), Char(260), 400),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300137V#6P#0006F不，其实呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}将赛尔盖交代的任务内容\n'
		'简略做了说明。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_TALK', Char(258), Text(
		'#10300138V#0101F旧市街的不良分子……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(668)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#10300139V#0301F就是之前在旧市街见到的\n'
				'那些危险的小鬼们吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(553)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#10300140V#0301F我们之前在旧市街\n'
				'见到过那样的人吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(260), Text(
				'#10300141V#0301F旧市街……\n'
				'竟然还有那种地方吗。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(259), Text(
		'#10300142V#0203F#5P据数据库显示……{wait}'
		'{page}'
		'#10300143V#0200F的确有『剑蛇帮』和\n'
		'『圣约帮』这两个分子\n'
		'在旧市街拉帮结派。{wait}'
		'{page}'
		'#10300144V据说，斗殴之类的事情是家常便饭。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10300145V#6P#0005F在我离开城市这段期间，\n'
		'竟然冒出了那种家伙吗……{wait}'
		'{page}'
		'#10300146V#0003F──也罢，不管怎么说，\n'
		'我们赶快去旧市街看看吧。{wait}'
		'{page}'
		'#10300147V#0001F在发生小规模冲突之前，\n'
		'必须想办法阻止他们才行。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#10300148V#0101F嗯，是啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(553)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#10300149V#0305F对了，罗伊德。\n'
				'旧市街在哪里啊？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#10300150V#6P#0000F嗯，到了东侧大道之后往南走，\n'
				'经过一道小桥就是了。{wait}'
				'{page}'
				'#10300151V总而言之，先去东侧大道吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#10300152V#0300F好。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(260), Text(
				'#10300153V#0300F那好，我们这就\n'
				'前往旧市街吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('CHAR_SET_POS', Char(0), (-21900, -5000, 18000), 180),
	Insn('FLAG_SET', Flag(527)),
	Insn('QUEST', 62, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 62, Insn('TASK_SET', 0)),
	Insn('SOUND_STOP', 806),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][56] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这次的任务\n'
				'姑且也算是实战测试……{wait}'
				'{page}'
				'还是不要绕道了，\n'
				'快点去地下区域的\n'
				'深处看看吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('ATTR', 10), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F明白，专心执行任务吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('ATTR', 10), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F说得也是。\n'
						'集中精神来执行任务吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('ATTR', 10), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#0300F嗯，就这么办吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-13150, -5000, 17120), 270),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][57] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(768)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F这边是城市的南出口吧。{wait}'
						'{page}'
						'现在没有外出的必要……\n'
						'专心做好市区内的工作吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'{color 5}现在没有必要去市外。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('0x5A'),
				]),
			]),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-230, 0, -17470), 0),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(768)), Insn('FLAG', Flag(777)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F要去阿尔摩利卡村的话，\n'
				'得从城市的东出口出去才行啊。{wait}'
				'{page}'
				'先绕到东侧大道那边吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-230, 0, -17470), 0),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(801)), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F要去玛因兹的话，\n'
				'得从城市的北出口出去才行啊。{wait}'
				'{page}'
				'先绕到住宅区那边吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-230, 0, -17470), 0),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1346)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F啊，这边是南出口。{wait}'
						'{page}'
						'现在要避免让琪雅\n'
						'遭遇到危险，\n'
						'还是不要外出了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'{color 5}现在没有离开市区的必要。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('0x5A'),
				]),
			]),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-230, 0, -17470), 0),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1554)), Insn('FLAG', Flag(1560)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F这边是城市的南出口吧。{wait}'
						'{page}'
						'考虑到黑月的事……\n'
						'……现在还是专心在市内进行调查吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'{color 5}现在还是专心在市内进行调查吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('0x5A'),
				]),
			]),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-230, 0, -17470), 0),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][58] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 9, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这边是克洛斯贝尔车站。\n'
				'……现在应该不需要进去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (5480, 0, -2680), 270),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1024)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 45, Insn('TASK_GET', 9))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这边是克洛斯贝尔车站。\n'
				'……现在应该不需要进去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (5480, 0, -2680), 270),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这边是克洛斯贝尔车站。\n'
				'……现在应该不需要进去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (5480, 0, -2680), 270),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][59] = [
	Insn('FORK', 40, 1, [
		Insn('0x96', Char(254), (-80000, -11500, -11500), 20000, 0),
	]),
	Insn('FORK_AWAIT', Char(40), 1),
	Insn('RETURN'),
]

data['code'][60] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 15))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F那个，不好意思。\n'
				'我们是克洛斯贝尔警察\n'
				'特务支援课的人……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x4B', Char(254), -1),
			Insn('EVENT_BEGIN', 0),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CAM_OFFSET', (-22140, 650, -19110), 0),
			Insn('CAM_ROTATE', 40, 10, 0, 0),
			Insn('0x6E', 700, 0),
			Insn('CAM_DISTANCE', 18500, 0),
			Insn('CHAR_SET_POS', Char(9), (-5000, 0, -2070), 90),
			Insn('CHAR_SET_POS', Char(257), (-3800, 0, -2670), 270),
			Insn('CHAR_SET_POS', Char(258), (-3800, 0, -1470), 270),
			Insn('CHAR_SET_POS', Char(259), (-2600, 0, -2670), 270),
			Insn('CHAR_SET_POS', Char(260), (-2600, 0, -1470), 270),
			Insn('CHAR_FLAG1_UNSET', Char(40), 128),
			Insn('0x78', b'\x0b', Char(40)),
			Insn('0x49'),
			Insn('CHAR_SET_POS', Char(40), (40000, -11500, -11500), 0),
			Insn('0xD3', Char(40), 0, 270000, 0, 0),
			Insn('OBJ_FLAG_UNSET', Object(11), 4),
			Insn('OBJ_FLAG_SET', Object(11), 4096),
			Insn('CAM_OFFSET', (-3800, 3690, -2670), 6500),
			Insn('CAM_ROTATE', 90, 25, 0, 6500),
			Insn('CAM_DISTANCE', 15000, 6500),
			Insn('FADE_OFF', 2000, Color(0x00000000)),
			Insn('FORK_FUNC', Char(40), 3, Function((0, 59))),
			Insn('SLEEP', 2000),
			Insn('SOUND_PLAY', 451, 0, 0, 100),
			Insn('SLEEP', 4000),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('FORK_AWAIT', Char(40), 3),
			Insn('TEXT_TALK', Char(254), Text(
				'哦，那个人的话，\n'
				'我记得今天早上有看到。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(0), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('EMOTE', Char(1), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('EMOTE', Char(2), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('EMOTE', Char(3), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(257), Text(
				'#2P#0000F真的吗！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F那么那个人\n'
				'到哪里去了！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哦，\n'
				'看起来一脸很困的样子……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CAM_OFFSET', (-2830, 2200, 3900), 2000),
			Insn('CAM_ROTATE', 44, 8, 0, 2000),
			Insn('CAM_DISTANCE', 15000, 2000),
			Insn('CHAR_ROTATE', Char(9), 45, 500),
			Insn('SLEEP', 200),
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
			Insn('FORK_AWAIT', Char(257), 2),
			Insn('FORK_AWAIT', Char(258), 2),
			Insn('FORK_AWAIT', Char(259), 2),
			Insn('FORK_AWAIT', Char(260), 2),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(254), Text(
				'好像往\n'
				'中央广场的方向去了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_ROTATE', Char(9), 90, 500),
			Insn('FORK', 257, 2, [
				Insn('CHAR_ROTATE', Char(254), 270, 500),
			]),
			Insn('FORK', 258, 2, [
				Insn('CHAR_ROTATE', Char(254), 270, 500),
			]),
			Insn('FORK', 259, 2, [
				Insn('CHAR_ROTATE', Char(254), 270, 500),
			]),
			Insn('FORK', 260, 2, [
				Insn('CHAR_ROTATE', Char(254), 270, 500),
			]),
			Insn('FORK_AWAIT', Char(257), 2),
			Insn('FORK_AWAIT', Char(258), 2),
			Insn('FORK_AWAIT', Char(259), 2),
			Insn('FORK_AWAIT', Char(260), 2),
			Insn('TEXT_TALK', Char(254), Text(
				'因为走起来的步伐有些不稳，\n'
				'所以我印象很深。\n'
				'不会错的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#2P#0000F这样啊，\n'
				'谢谢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_WATCH', Char(257), Char(260), 500),
			Insn('SLEEP', 100),
			Insn('FORK', 258, 2, [
				Insn('CHAR_WATCH', Char(254), Char(259), 500),
			]),
			Insn('FORK', 259, 2, [
				Insn('CHAR_WATCH', Char(254), Char(258), 500),
			]),
			Insn('FORK', 260, 2, [
				Insn('CHAR_WATCH', Char(254), Char(257), 500),
			]),
			Insn('SLEEP', 300),
			Insn('FORK_AWAIT', Char(258), 2),
			Insn('FORK_AWAIT', Char(259), 2),
			Insn('FORK_AWAIT', Char(260), 2),
			Insn('TEXT_TALK', Char(259), Text(
				'#1P#0200F看来接下来要去中央广场了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#2P#0000F嗯，去看看吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_POS', Char(0), (-4450, 0, -2110), 90),
			Insn('EVENT_END', 5),
			Insn('0x4C', Char(254), -1),
			Insn('QUEST', 56, Insn('TASK_SET', 15)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'如果是穿着白袍像是医生的人，\n'
				'我记得今天早上有看到。{wait}'
				'{page}'
				'一脸很困的样子，\n'
				'往中央广场的方向走去。{wait}'
				'{page}'
				'因为走起来的步伐有些不稳，\n'
				'所以我印象很深。\n'
				'不会错的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]
