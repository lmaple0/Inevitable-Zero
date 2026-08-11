# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'c020c',
	'name2': 'c020c',
	'location': 10,
	'bgm': 100,
	'flags': 8192,
	'includes': [
		'c020c',
		'c0210_1',
		None,
		None,
		None,
		None,
	],
	'name3': 'c020c',
	'labels': [
		{
			'pos': (70.75, 0.0, -7.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('中央广场'),
		},
		{
			'pos': (5.0, 0.0, -2.5),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('西侧大道'),
		},
		{
			'pos': (97.75, 0.0, 82.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('行政区'),
		},
		{
			'pos': (-56.0, 0.0, 72.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('住宅区'),
		},
		{
			'pos': (17.0, 0.0, 64.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('欢乐街'),
		},
		{
			'pos': (152.0, 0.0, -30.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('东侧大道'),
		},
		{
			'pos': (187.5, 0.0, -85.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('旧市街'),
		},
		{
			'pos': (180.0, 0.0, 36.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('港湾区'),
		},
		{
			'pos': (154.0, 0.0, 130.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('ＩＢＣ'),
		},
		{
			'pos': (82.0, 0.0, -76.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('站前大道'),
		},
		{
			'pos': (35.0, 0.0, 28.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('小巷'),
		},
		{
			'pos': (79.0, 0.0, -107.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('乌尔斯拉小径'),
		},
		{
			'pos': (206.0, 0.0, -16.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('东克洛斯贝尔街道'),
		},
		{
			'pos': (-46.0, 0.0, -4.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('西克洛斯贝尔街道'),
		},
		{
			'pos': (-40.0, 0.0, 96.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('玛因兹山道'),
		},
		{
			'pos': (48.75, 0.0, -21.0),
			'unk': b'\x00\x00Q\x00',
			'name': Translate(''),
		},
		{
			'pos': (102.5, 0.0, 5.0),
			'unk': b'\x00\x00T\x00',
			'name': Translate(''),
		},
		{
			'pos': (73.25, 0.0, -29.0),
			'unk': b'\x00\x00W\x00',
			'name': Translate(''),
		},
		{
			'pos': (48.0, 0.0, 8.0),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (68.5, 0.0, 32.0),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (17.75, 0.0, 3.0),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (8.0, 0.0, 24.0),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (32.0, 0.0, 56.0),
			'unk': b'\x00\x00R\x00',
			'name': Translate(''),
		},
		{
			'pos': (36.75, 0.0, 43.0),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (45.5, 0.0, 34.5),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (74.0, 0.0, 105.5),
			'unk': b'\x00\x00Q\x00',
			'name': Translate(''),
		},
		{
			'pos': (186.0, 0.0, -30.0),
			'unk': b'\x00\x00R\x00',
			'name': Translate(''),
		},
		{
			'pos': (169.0, 0.0, -120.5),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (156.0, 0.0, -102.0),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
	],
	'chcp': [
		'chr/ch20200',
		'chr/ch20402',
		'chr/ch34300',
		'chr/ch10400',
		'chr/ch20700',
		'chr/ch21600',
		'chr/ch20100',
		'chr/ch20400',
		'chr/ch20500',
		'chr/ch21800',
		'chr/ch24500',
		'chr/ch22100',
		'chr/ch21602',
		'chr/ch21100',
		'chr/ch21602',
		'chr/ch24400',
		'chr/ch17200',
		'chr/ch17300',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
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
			'name': Translate('庞斯'),
			'pos': (-25120, 0, 4139),
			'angle': 180,
			'_1': b'\x05\x01\x00\x00\x00\x00\x00\x01',
			'function': Function((0, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('布利克'),
			'pos': (6570, -150, 5119),
			'angle': 90,
			'_1': b'U\x01\x00\x00\x01\x00\xff\xff',
			'function': Function((0, 10)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('贝奈特'),
			'pos': (4869, 0, 629),
			'angle': 225,
			'_1': b'\x05\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 12)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('爱尔莎'),
			'pos': (4820, 3000, 17420),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('小桃'),
			'pos': (6309, 3000, 17329),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((0, 14)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('路维克老先生'),
			'pos': (-6579, 0, 7170),
			'angle': 90,
			'_1': b'\x05\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('奥莉嘉夫人'),
			'pos': (-5219, 0, 7170),
			'angle': 270,
			'_1': b'\x05\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((0, 17)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('卡缇莉娜'),
			'pos': (-15020, -2599, -8350),
			'angle': 180,
			'_1': b'\x95\x01\x00\x00\n\x00\x00\x00',
			'function': Function((0, 18)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('琪露露'),
			'pos': (-13739, -2599, -8350),
			'angle': 180,
			'_1': b'\x95\x01\x00\x00\x08\x00\x00\x00',
			'function': Function((0, 19)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (3349, 0, -9760),
			'angle': 270,
			'_1': b'\x05\x01\x00\x00\x0f\x00\x00\x00',
			'function': Function((0, 20)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (2089, 0, -9760),
			'angle': 90,
			'_1': b'\x05\x01\x00\x00\x0b\x00\x00\x00',
			'function': Function((0, 21)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (1629, 3000, 13079),
			'angle': 180,
			'_1': b'\x05\x01\x00\x00\t\x00\x00\x00',
			'function': Function((0, 22)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (8039, -150, 6960),
			'angle': 180,
			'_1': b'\xd5\x01\x00\x00\x0c\x00\xff\xff',
			'function': Function((0, 23)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (6980, -300, 7619),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\r\x00\x00\x00',
			'function': Function((0, 24)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('雷兹老人'),
			'pos': (5500, -200, 8000),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x0e\x00\xff\xff',
			'function': Function((0, 25)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('肯恩'),
			'pos': (-3500, 0, -7599),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x10\x00\x00\x02',
			'function': Function((0, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('娜娜'),
			'pos': (-10779, -2599, -6699),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x11\x00\x00\x00',
			'function': Function((0, 8)),
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
			'name': Translate('修利'),
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
			'pos': (39.5, -19.0, -4.5),
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
				-19.75,
				9.5,
				0.9000000357627869,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 42)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (14410, -6500, -13590),
			'range': 1200,
			'bubble_pos': (14410, -5500, -13590),
			'_1': b'|\x00\x00',
			'function': Function((0, 5)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-32070, -1000, 11050),
			'range': 1200,
			'bubble_pos': (-32070, 0, 11050),
			'_1': b'|\x00\x00',
			'function': Function((0, 6)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (4050, 0, -190),
			'range': 1000,
			'bubble_pos': (4870, 1500, 630),
			'_1': b'~\x00\x00',
			'function': Function((0, 11)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-31040, -1000, 9420),
			'range': 1500,
			'bubble_pos': (-29950, 1000, 8850),
			'_1': b'|\x00\x00',
			'function': Function((0, 33)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\n\x00', Function((0, 3)), Function((0, 4))),
	'code': [None]*43,
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
		Insn('CHAR_IDLE', Char(254), (-28870, 2540), (-21090, 6380), 1000),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (-2830, -6400), (-1500, -8300), 1000),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 111), Insn('EQ'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('0x23', 7), Insn('CONST', 6), Insn('EQ'), Insn('0x23', 7), Insn('CONST', 7), Insn('EQ'), Insn('OR'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (110, 3000, 22760), 180),
					Insn('CHAR_SET_POS', Char(1), (110, 3000, 22760), 180),
					Insn('CHAR_SET_POS', Char(2), (110, 3000, 22760), 180),
					Insn('CHAR_SET_POS', Char(3), (110, 3000, 22760), 180),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (110, 3000, 22760), 180),
							Insn('CHAR_SET_POS', Char(5), (110, 3000, 22760), 180),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (110, 3000, 22760), 180),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 101), Insn('SET'), Insn('END')])),
				]),
				(None, [
					Insn('CHAR_SET_POS', Char(0), (24460, 0, -8180), 270),
					Insn('CHAR_SET_POS', Char(1), (24460, 0, -8180), 270),
					Insn('CHAR_SET_POS', Char(2), (24460, 0, -8180), 270),
					Insn('CHAR_SET_POS', Char(3), (24460, 0, -8180), 270),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (24460, 0, -8180), 270),
							Insn('CHAR_SET_POS', Char(5), (24460, 0, -8180), 270),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (24460, 0, -8180), 270),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 100), Insn('SET'), Insn('END')])),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('0xD0', 7, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(19), (21980, 0, -10790), 135),
			Insn('CHAR_FLAG1_UNSET', Char(22), 128),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(19), (-2410, 0, -1730), 90),
			Insn('CHAR_FLAG1_UNSET', Char(20), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
					Insn('EFF_LOAD', ResId(0), 'event\\eva02_00.eff'),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_ROTATE', Char(13), 180, 0),
			Insn('CHAR_ROTATE', Char(14), 225, 0),
			Insn('CHAR_SET_POS', Char(19), (-6580, 0, 5810), 0),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 29, Insn('TASK_GET', 3))), Insn('EXEC', Insn('QUEST_GET', 29, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 29, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(13), 128),
					Insn('CHAR_FLAG1_SET', Char(14), 128),
					Insn('CHAR_FLAG1_SET', Char(19), 128),
				]),
				(None, []),
			]),
			Insn('CHAR_FLAG1_UNSET', Char(23), 128),
			Insn('CHAR_FLAG1_UNSET', Char(24), 128),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1487)), Insn('FLAG', Flag(1303)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 27))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 30))),
		]),
		(Expr([Insn('FLAG', Flag(737)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(737)),
			Insn('EVENT', Function((0, 31))),
		]),
		(Expr([Insn('FLAG', Flag(738)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(738)),
			Insn('EVENT', Function((0, 34))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('OBJ_FLAG_UNSET', Object(9), 16),
	Insn('0x70', Object(9), b'\x1e\x00'),
	Insn('0x1B', 1, Function((255, 255)), 255),
	Insn('0x1B', 8, Function((255, 255)), 255),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1294)), Insn('FLAG', Flag(1303)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 1, Function((0, 40)), 0),
			Insn('0x1B', 8, Function((0, 41)), 0),
			Insn('0xB5', b'\x01\x00\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1303)), Insn('FLAG', Flag(1307)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 1, Function((0, 40)), 0),
		]),
		(None, []),
	]),
	Insn('0x65', 3, 1),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 29, Insn('TASK_GET', 8))), Insn('EXEC', Insn('QUEST_GET', 29, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x66', 3, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 29, Insn('TASK_GET', 3))), Insn('EXEC', Insn('QUEST_GET', 29, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(2177)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x65', 1, 1),
			Insn('0x66', 3, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(2176)), Insn('NOT'), Insn('END')]), [
			Insn('0x70', Object(7), b'\x00\x00'),
		]),
		(None, [
			Insn('0x70', Object(7), b'\x1e\x00'),
		]),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(2177)), Insn('NOT'), Insn('END')]), [
			Insn('0x70', Object(8), b'\x00\x00'),
		]),
		(None, [
			Insn('0x70', Object(8), b'\x1e\x00'),
		]),
	]),
	Insn('EFF_LOAD', ResId(7), 'event\\ev308_02.eff'),
	Insn('EFF_PLAY', (ResId(7), -1), Char(255), 0, -25000, -1, -4000, -1, 4000, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('EFF_PLAY', (ResId(7), -1), Char(255), 0, 0, 0, -4000, -1, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('EFF_PLAY', (ResId(7), -1), Char(255), 0, 24000, 0, -4000, -1, -8000, -1, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('EFF_PLAY', (ResId(7), -1), Char(255), 0, 4000, 0, -1000, -1, 18000, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('0xF2', Insn('CHEST')),
	Insn('0x09', 134217728),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(2176)), Insn('NOT'), Insn('END')]), [
			Insn('SOUND_PLAY', 14, 0, 0, 100),
			Insn('0x71', Object(7), b'\x00\x00', 30, 0),
			Insn('SLEEP', 500),
			Insn('0x70', Object(7), b'\x1e\x00'),
			Insn('SOUND_PLAY', 17, 0, 0, 100),
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('SEPITH_ADD', b'\x00P\x00'),
			Insn('SEPITH_ADD', b'\x01P\x00'),
			Insn('SEPITH_ADD', b'\x02P\x00'),
			Insn('SEPITH_ADD', b'\x03P\x00'),
			Insn('SEPITH_ADD', b'\x04P\x00'),
			Insn('SEPITH_ADD', b'\x05P\x00'),
			Insn('SEPITH_ADD', b'\x06P\x00'),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'获得了{color 2}#56I地之耀晶石×８０{color 0}\n'
				'{color 2}#57I水之耀晶石×８０{color 0}\n'
				'{color 2}#58I火之耀晶石×８０{color 0}\n'
				'{color 2}#59I风之耀晶石×８０{color 0}\n'
				'{color 2}#60I时之耀晶石×８０{color 0}\n'
				'{color 2}#61I空之耀晶石×８０{color 0}\n'
				'{color 2}#62I幻之耀晶石×８０{color 0}。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('FLAG_SET', Flag(2176)),
			Insn('0xDE', b'\x06\x00'),
		]),
		(None, [
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(999), Text(
				'{0x06}{color 5}宝箱内空无一物。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
		]),
	]),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_END', Char(255)),
	Insn('0x0A', 134217728),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('0xF2', Insn('CHEST')),
	Insn('0x09', 134217728),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(2177)), Insn('NOT'), Insn('END')]), [
			Insn('SOUND_PLAY', 14, 0, 0, 100),
			Insn('0x71', Object(8), b'\x00\x00', 30, 0),
			Insn('SLEEP', 500),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('ITEM_ADD', 167, 1)), Insn('END')]), [
					Insn('FADE_ON', 300, Color(0x00000000), 100),
					Insn('SOUND_PLAY', 17, 0, 0, 100),
					Insn('TEXT_SET_POS', -1, -1, -1, -1),
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(999), Text(
						'{color 0}已取得{item 167}{color 0}。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('TEXT_SET_POS', -1, 280, 60, 3),
					Insn('FADE_OFF', 300, Color(0x00000000)),
					Insn('FLAG_SET', Flag(2177)),
					Insn('0xDE', b'\x06\x00'),
				]),
				(None, [
					Insn('FADE_ON', 300, Color(0x00000000), 100),
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(999), Text(
						'宝箱内装着{item 167}{color 0}。\n'
						'但因持有物品已满而放弃{item 167}{color 0}。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('FADE_OFF', 300, Color(0x00000000)),
					Insn('SOUND_PLAY', 15, 0, 0, 100),
					Insn('0x71', Object(8), b'\x1e\x00', 0, 0),
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
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 29, Insn('TASK_GET', 3))), Insn('EXEC', Insn('QUEST_GET', 29, Insn('TASK_GET', 8))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 32))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(23), 16),
					Insn('0x4B', Char(23), -1),
					Insn('CHAR_WATCH', Char(23), Char(24), 0),
					Insn('TEXT_TALK', Char(23), Text(
						'赶快出发啦！我等不及了！\n'
						'今天要比昨天逛更多的店！{wait}'
						'{page}'
						'『纪念庆典』可是不会等人的～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(9)),
					Insn('CHAR_FLAG1_UNSET', Char(23), 16),
				]),
				(None, [
					Insn('TEXT_TALK', Char(23), Text(
						'『纪念庆典』可是不会等人的～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('0x4C', Char(23), -1),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(10)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(24), Text(
						'妈妈到底在做什么呀……\n'
						'肯恩等不住快一个人先走了呢。{wait}'
						'{page}'
						'不过娜娜会等妈妈的！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(24), Text(
						'娜娜会等妈妈的！\n'
						'──怎么还不出来呀……{wait}'
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
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天日落之后，\n'
				'将会有压轴的烟火哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'这可不能错过呢。\n'
				'要占个好位置才行。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'７０周年纪念日快乐！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'{color 5}庞斯架好了导力相机。{color 0}{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('0x5A'),
					Insn('SOUND_PLAY', 817, 0, 0, 100),
					Insn('EFF_PLAY', (ResId(0), -1), Char(254), 192, 0, 0, 1200, 0, 400, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
					Insn('SLEEP', 800),
					Insn('EFF_PLAY', (ResId(0), -1), Char(254), 192, 0, 0, 1200, 0, 400, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
					Insn('SLEEP', 600),
					Insn('TEXT_TALK', Char(254), Text(
						'你们怎么样？\n'
						'开心吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'今天拍到的照片\n'
						'都很棒呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，克洛斯贝尔万岁～！\n'
						'７０周年纪念日快乐！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯～大家的笑容\n'
				'都很不错呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'真期待显像结果啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哦哦，连飞行船也出来了啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'来来，再拍一张\n'
				'留作纪念吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯～不愧是创立纪念庆典啊！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不愁找不到摄影题材呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][10] = [
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
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天下午将要\n'
				'在市政厅召开闭幕式。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'麦克道尔市长也会出席，\n'
				'我也去看看吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'像这样和外国人\n'
				'悠闲聊着天，\n'
				'还真有纪念庆典的气氛啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'可以的话，希望他们\n'
				'明年也能来克洛斯贝尔呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(254), 1),
			Insn('TEXT_TALK', Char(254), Text(
				'哈哈，不要拘束啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'来吧，一起干杯～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'观光巴士加上飞行船啊……\n'
				'今年可真是大手笔啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'都没法安心看书了，\n'
				'我也去转一圈吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我昨天去听了\n'
						'市长的开幕演讲。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'麦克道尔市长\n'
						'都已经年过七十了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'明明刚发生过那种事件，\n'
						'却感觉不到他有丝毫衰弱。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'麦克道尔市长果然厉害呀。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'距离引退应该\n'
						'还早得很吧。{wait}'
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

data['code'][11] = [
	Insn('CALL', Function((0, 12))),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('TEXT_START', Char(10)),
	Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('EQ'), Insn('END')], [
		Insn('FADE_ON', 300, Color(0x00000000), 100),
		Insn('MENU', 0, -1, -1, 1, Text(
			'对话\n'
			'购物\n'
			'放弃\n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('NE'), Insn('END')]), [
				Insn('0x60', 0),
				Insn('FADE_OFF', 300, Color(0x00000000)),
				Insn('0x0D'),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
				Insn('OPEN_SHOP', 207),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), []),
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
				Insn('IF', [
					(Expr([Insn('ATTR', 4), Insn('CONST', 3), Insn('EQ'), Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 32))), Insn('BOOL_AND'), Insn('FLAG', Flag(1106)), Insn('BOOL_AND'), Insn('FLAG', Flag(1107)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(9)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
						Insn('CALL', Function((1, 14))),
						Insn('FLAG_SET', Flag(9)),
					]),
					(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
						Insn('TEXT_TALK', Char(10), Text(
							'#14804F呵呵……\n'
							'奥斯卡，你就玩去吧。{wait}'
							'{page}'
							'#14801F趁此机会，我会好好\n'
							'研究新品面包的。{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(Expr([Insn('FLAG', Flag(1303)), Insn('END')]), [
						Insn('TEXT_TALK', Char(10), Text(
							'#14810F呵呵，人这么多，真是求之不得啊。{wait}'
							'{page}'
							'#14802F要将我烤的面包\n'
							'宣传给所有人！{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(Expr([Insn('FLAG', Flag(1294)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(1384)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(257), Text(
									'#0001F（嗯，这个人\n'
									'\u3000可能知道些什么吧……）{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_MESSAGE', Char(255), Text(
									'{color 5}罗伊德出示了柯林的照片，\n'
									'并询问对方是否有什么线索。{color 0}{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_RESET', b'\x00'),
								Insn('0x5A'),
								Insn('TEXT_TALK', Char(10), Text(
									'#14805F…………？\n'
									'这孩子好像在哪里见过……{wait}'
									'{page}'
									'#14800F……不过今天没看见呢。\n'
									'小孩子孤身一个人的话，应该是很显眼的。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(257), Text(
									'#0000F是吗……\n'
									'谢谢您了。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(1384)),
								Insn('0xD0', 2, Expr([Insn('0x23', 2), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
								Insn('CALL', Function((0, 26))),
							]),
							(None, [
								Insn('TEXT_TALK', Char(10), Text(
									'#14800F至少可以确定，\n'
									'他没来试吃过新品呢。{wait}'
									'{page}'
									'#14804F……如果来的话，我一定会\n'
									'给他推荐面包的。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
						Insn('TEXT_TALK', Char(10), Text(
							'#14810F呵呵，人这么多，真是求之不得啊。{wait}'
							'{page}'
							'#14802F要将我烤的面包\n'
							'宣传给所有人！{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
						Insn('TEXT_TALK', Char(10), Text(
							'#14809F欢迎光临～！{wait}'
							'{page}'
							'#14802F呵呵，不要客气，\n'
							'尽量多买哦。{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
						Insn('TEXT_TALK', Char(10), Text(
							'#14804F呵呵……这个月的新品面包\n'
							'是由我负责的哦。{wait}'
							'{page}'
							'#14802F纪念庆典的人这么多，\n'
							'一定会卖得很好！\n'
							'趁此机会，给奥斯卡个下马威吧。{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(10), Text(
									'#14810F……请、请品尝一下吧。{wait}'
									'{page}'
									'#14802F如果觉得好吃，就请买一点吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(1)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(10), Text(
									'#14810F今天的面包是我烤的。{wait}'
									'{page}'
									'#14802F不、不嫌弃的话，就请买一点吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(None, []),
				]),
			]),
			(None, []),
		]),
	]),
	Insn('TEXT_END', Char(10)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'欢迎光临塔里兹商店～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'请进来看看～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'小桃真是的，\n'
						'又缩在家里不出来了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯～人这么多，\n'
						'对那个内向的孩子来说，\n'
						'也许很不自在吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'欢迎光临～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我那老公，还是和平时一样\n'
				'悠然自得，什么都不做。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我可得努力推销才行呢。{wait}'
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
		(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'庆典……\n'
				'来了好多客人啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(3)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'欢、欢迎光临……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天去中央广场一带\n'
				'逛逛看吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'说不定能买到\n'
				'适合我们家的日用品呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1294)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 90, 0),
			Insn('TEXT_TALK', Char(254), Text(
				'唔唔，今晚我受邀\n'
				'参加晚餐会。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你该不会\n'
				'完全忘记了吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀呀，已经走了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽说每年都是这样，\n'
				'但一旦结束，还是感觉有些寂寥呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 90, 0),
			Insn('TEXT_TALK', Char(254), Text(
				'去高一点的地方，\n'
				'会比较容易看到吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你还真是不机灵啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('CALL', Function((0, 16))),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'这是难得的庆典，\n'
				'大家一起开开心心地度过吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'庆典期间可以不拘小节啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('0x4B', Char(13), -1),
	Insn('0x4B', Char(19), -1),
	Insn('CHAR_WATCH', Char(13), Char(19), 0),
	Insn('CHAR_WATCH', Char(19), Char(13), 0),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(19), Text(
				'哎呀，这不是议员嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(19), Text(
				'哦，已经引退了，\n'
				'所以现在是前议员了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'记得你是\n'
				'委员会的官员……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'呵呵，别来无恙吧？\n'
				'那就再好不过了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(4)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(13), Text(
				'呵呵，我已经\n'
				'不过问政治了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'话说，不如来我家坐坐，\n'
				'一起喝一杯吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(19), Text(
				'哈哈哈，那我就\n'
				'恭敬不如从命了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('0x4C', Char(13), -1),
	Insn('0x4C', Char(19), -1),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 270, 0),
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀，今天不是要去\n'
				'彩虹剧团看演出吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'要是去别处闲逛的话，\n'
				'公演可就要结束了哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1294)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 270, 0),
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀，先去那边的面包摊子\n'
				'试吃一点也没关系嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'顺便买点\n'
				'回去也不错吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'虽然每年都有，\n'
				'不过看着游行真是令人心情愉快啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'平日累积的怨气\n'
				'也都抛到九霄云外去了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 270, 0),
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀，游行队伍\n'
				'要从那边过来哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'在这里等待\n'
				'当然是最好的了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我老伴曾经当过议员。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'所以还是有一定人脉的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'至少在纪念庆典期间，\n'
				'就夫妇两人一起好好享受吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'啊，快看快看，是飞行船哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'呜哇……\n'
		'装饰得好华丽。\n'
		'不愧是纪念庆典呢～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('TEXT_START', Char(254)),
	Insn('0x4B', Char(15), -1),
	Insn('TEXT_TALK', Char(254), Text(
		'呜～我还想\n'
		'在家睡觉呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(15), Char(254), 500),
	Insn('TEXT_TALK', Char(15), Text(
		'哎～那多可惜啊～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'琪露露，一起逛吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(15), 180, 0),
	Insn('0x4C', Char(15), -1),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呼，已经到最终日了啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'城市太广阔，\n'
				'我连一半都没逛到呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'（嚼嚼）……\n'
				'那边的面包店\n'
				'正在举办试吃活动呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你们也去吃点如何？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'你们知道吗？\n'
				'在那个漂亮的喷泉前面，\n'
				'有个什么村的人在开露天店呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'超级推荐哦！\n'
				'那个蛋包饭真是太美味了！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我从帝国过来，\n'
				'在铁道上摇晃了三个小时……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'终于到达\n'
				'克洛斯贝尔了～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 90, 0),
			Insn('TEXT_TALK', Char(254), Text(
				'好，去欢乐街那边看看吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'难得从家里\n'
				'溜出来嘛。\n'
				'一定要玩个痛快！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 90, 0),
			Insn('TEXT_TALK', Char(254), Text(
				'喂，花心鬼！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不要转移\n'
				'话题！！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我觉得中央广场的\n'
				'甜品店不错呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'那里的东西超～美味的呀！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'因为妈妈一直不准我出来，\n'
				'所以这么迟才能逛庆典。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'既然如此，就更要\n'
				'玩个痛快呢！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我记得那栋建筑物\n'
						'以前是克洛斯贝尔时报周刊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过，现在应该\n'
						'搬到商业街去了，\n'
						'不知那栋建筑物现在是做什么的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'在街上随便逛逛，\n'
						'就会有许多新发现呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那栋建筑物，\n'
						'现在的主人究竟是谁呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呼，今年的游行\n'
				'真是华丽又热闹啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'好吧，就在这边占个位置\n'
				'来看游行吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'这是纪念庆典的焦点活动，\n'
				'可不能错过呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('CALL', Function((0, 16))),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'纪念庆典还是\n'
						'随意乱逛比较有趣啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'城市会显得\n'
						'和平时大不相同呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'到处都有店主\n'
						'在开露天店啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'唔唔，城市会显得\n'
						'和平时大不相同呢。{wait}'
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
	Insn('TEXT_TALK', Char(254), Text(
		'克洛斯贝尔人会\n'
		'热情地迎接外地人呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'看来这是个\n'
		'很适合居住的城市嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'真是精彩的\n'
				'游行呀！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯～果然是\n'
				'来对了～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'说到克洛斯贝尔的庆典，\n'
				'就一定少不了游行！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我就是为了看这个，\n'
				'才会远道而来的～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
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
		(Expr([Insn('FLAG', Flag(7)), Insn('END')]), [
			Insn('TEXT_TALK', Char(22), Text(
				'今天就在西侧大道\n'
				'悠闲地度过吧，\n'
				'呵呵。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(22), Text(
				'虽然我平时\n'
				'都是在住宅区悠闲度日的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(22), Text(
				'但我喜欢的那个长椅，今天却被一个\n'
				'一脸疲惫的穿西装男子给占了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(22), Text(
				'呵呵，看他一副没精打采的样子，\n'
				'我就把那座位让给他了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(7)),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('IF', [
		(Expr([Insn('0x23', 2), Insn('CONST', 5), Insn('EQ'), Insn('END')]), [
			Insn('QUEST', 70, Insn('TASK_SET', 11)),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F（这样一来，西侧大道\n'
				'\u3000也都调查过了……）{wait}'
				'{page}'
				'（……不知大家的\n'
				'\u3000调查状况怎么样了。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(352), Text(
				'#3308F（…………………………）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0xD0', 2, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('FLAG_SET', Flag(1487)),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50011', 30),
	Insn('SOUND_LOAD', 806),
	Insn('CAM_OFFSET', (13500, 1000, -8500), 0),
	Insn('CAM_ROTATE', 35, 24, 0, 0),
	Insn('0x6E', 550, 0),
	Insn('CAM_DISTANCE', 21500, 0),
	Insn('CHAR_SET_POS', Char(257), (12700, 0, -8500), 90),
	Insn('CHAR_SET_POS', Char(352), (14300, 0, -8500), 270),
	Insn('IMG_LOAD', ResId(0), 180, 0, b'\xb4\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis007.itp'),
	Insn('CAM_ROTATE', 40, 19, 0, 3000),
	Insn('CAM_DISTANCE', 17500, 3000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 806, 0, 2, 100),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_SET', Char(257), 32),
	Insn('CHAR_FLAG1_SET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 4),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('CHAR_SET_FRAME', Char(257), 5),
	Insn('SOUND_STOP', 806),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('FADE_ON', 500, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#13400435V#0001F喂，我是罗伊德。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FORK', 352, 1, [
		Insn('0x9A', Char(254), b'\x01\x01', 700, 1000, b'\x00'),
	]),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('艾莉的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400436V我是艾莉，\n'
		'查到一点令人担心的事，\n'
		'所以向你报告哦。{wait}'
		'{page}'
		'#13400437V我现在刚好\n'
		'跟缇欧在一起……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 240, 80, -1, -1),
	Insn('TEXT_SET_NAME', Translate('缇欧的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400438V是我，罗伊德前辈。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#13400439V#0000F嗯，你们会合了啊。{wait}'
		'{page}'
		'#13400440V那么，怎么样了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('艾莉的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400441V关于柯林，他好像曾经在栈桥这里\n'
		'眺望过水上巴士。{wait}'
		'{page}'
		'#13400442V但不清楚他之后\n'
		'又去了哪里……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 240, 80, -1, -1),
	Insn('TEXT_SET_NAME', Translate('缇欧的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400443V于是我就拜托赛特\n'
		'探寻了一下气味。{wait}'
		'{page}'
		'#13400444V然后……\n'
		'气味似乎是在栈桥到阶梯\n'
		'的位置就突然中断了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#13400445V#0005F气味中断了……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('艾莉的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400446V嗯，是在港湾区的东南端……{wait}'
		'{page}'
		'#13400447V这到底是怎么回事呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#13400448V#0008F……莫非是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FORK_AWAIT', Char(352), 1),
	Insn('MENU', 0, -1, -1, 0, Text(
		'【进入车辆里面了】\n'
		'【掉进河里去了】\n'
		'【被谁抱走了】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('QUEST_BONUS_DP', 70, 2),
			Insn('SLEEP', 300),
			Insn('TEXT_SET_POS', 90, 130, -1, -1),
			Insn('TEXT_MESSAGE', Char(257), Text(
				'#13400449V#0003F具有一定程度的密闭性，\n'
				'气味不易外泄的地方……{wait}'
				'{page}'
				'#13400450V#0001F有可能是\n'
				'乘上某辆车了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_SET_POS', 170, 50, -1, -1),
			Insn('TEXT_SET_NAME', Translate('艾莉的声音')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}#13400451V啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_SET_POS', 240, 80, -1, -1),
			Insn('TEXT_SET_NAME', Translate('缇欧的声音')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}#13400452V原来如此……\n'
				'这样就可以理解了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_SET_POS', 50, 30, -1, -1),
			Insn('TEXT_MESSAGE', Char(352), Text(
				'{color 0}#13400453V#3304F嗯，蕾恩也同意哦。{wait}'
				'{page}'
				'#13400454V#3301F这样一来，接下来的问题就是，\n'
				'他究竟上了什么车呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('BREAK'),
		],
		1: [
			Insn('SLEEP', 300),
			Insn('TEXT_SET_POS', 90, 130, -1, -1),
			Insn('TEXT_MESSAGE', Char(257), Text(
				'#13400455V#0011F该不会……\n'
				'是掉进河里了吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_SET_POS', 50, 30, -1, -1),
			Insn('TEXT_MESSAGE', Char(352), Text(
				'#13400456V#3306F真是的，大哥哥。\n'
				'你是怎么听的啊。{wait}'
				'{page}'
				'#13400457V#3301F狼先生说的是\n'
				'栈桥到阶梯的位置吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_SET_POS', 90, 130, -1, -1),
			Insn('TEXT_MESSAGE', Char(257), Text(
				'#13400458V#0006F啊，是哦……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_SET_POS', 50, 30, -1, -1),
			Insn('TEXT_MESSAGE', Char(352), Text(
				'#13400459V#3303F即使是被人抱走了，\n'
				'应该也会留下些许气味的。{wait}'
				'{page}'
				'#13400460V#3300F不过，如果是进入了\n'
				'具有一定程度的密闭性的地方……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_SET_POS', 90, 130, -1, -1),
			Insn('TEXT_MESSAGE', Char(257), Text(
				'#13400461V#0005F对了……是车辆吗！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_SET_POS', 170, 50, -1, -1),
			Insn('TEXT_SET_NAME', Translate('艾莉的声音')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}#13400462V啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_SET_POS', 240, 80, -1, -1),
			Insn('TEXT_SET_NAME', Translate('缇欧的声音')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}#13400463V原来如此……\n'
				'这样就可以理解了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_SET_POS', 50, 30, -1, -1),
			Insn('TEXT_MESSAGE', Char(352), Text(
				'{color 0}#13400464V#3304F嗯，就是这样。{wait}'
				'{page}'
				'#13400465V#3301F这样一来，接下来的问题就是，\n'
				'他究竟上了什么车呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('BREAK'),
		],
		2: [
			Insn('QUEST_BONUS_DP', 70, 1),
			Insn('SLEEP', 300),
			Insn('TEXT_SET_POS', 90, 130, -1, -1),
			Insn('TEXT_MESSAGE', Char(257), Text(
				'#13400466V#0013F他被人抱着\n'
				'离开了那里……{wait}'
				'{page}'
				'#13400467V#0008F不……应该不是。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_SET_POS', 50, 30, -1, -1),
			Insn('TEXT_MESSAGE', Char(352), Text(
				'#13400468V#3303F嗯，即使是被人抱走了，\n'
				'应该也会留下些许气味的。{wait}'
				'{page}'
				'#13400469V#3300F不过，如果是进入了\n'
				'具有一定程度的密闭性的地方……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_SET_POS', 90, 130, -1, -1),
			Insn('TEXT_MESSAGE', Char(257), Text(
				'#13400470V#0005F对了……是车辆吗！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_SET_POS', 170, 50, -1, -1),
			Insn('TEXT_SET_NAME', Translate('艾莉的声音')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}#13400471V啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_SET_POS', 240, 80, -1, -1),
			Insn('TEXT_SET_NAME', Translate('缇欧的声音')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}#13400472V原来如此……\n'
				'这样就可以理解了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_SET_POS', 50, 30, -1, -1),
			Insn('TEXT_MESSAGE', Char(352), Text(
				'{color 0}#13400473V#3304F嗯，就是这样。{wait}'
				'{page}'
				'#13400474V#3301F这样一来，接下来的问题就是，\n'
				'他究竟上了什么车呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('EMOTE', Char(352), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(352)),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('艾莉的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400475V对了……\n'
		'你旁边还有什么人吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 240, 80, -1, -1),
	Insn('TEXT_SET_NAME', Translate('缇欧的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400476V这个女孩子的声音好像\n'
		'在哪里听过呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#13400477V#0006F嗯，说来话长啦。{wait}'
		'{page}'
		'#13400478V#0001F总之，大家暂时先集合，\n'
		'整理一下情报比较──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FORK', 352, 1, [
		Insn('0x96', Char(254), (14300, 0, -8500), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(352), 1),
	Insn('TEXT_SET_POS', 50, 30, -1, -1),
	Insn('TEXT_MESSAGE', Char(352), Text(
		'#13400479V#3304F──喂，大哥哥。{wait}'
		'{page}'
		'#13400480V#3300F支援课的终端，借我用一下哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#13400481V#0005F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FORK_FUNC', Char(352), 3, Function((0, 28))),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('CHAR_SET_FRAME', Char(257), 4),
	Insn('SLEEP', 300),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 3)),
	Insn('TEXT_TALK', Char(257), Text(
		'#13400482V#5P#0011F等、等一下！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(257), 5),
	Insn('SLEEP', 300),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('FADE_ON', 500, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#13400483V#0013F──艾莉、缇欧！\n'
		'你们联系兰迪，\n'
		'暂时先回支援课吧！{wait}'
		'{page}'
		'#13400484V到时候我再一起说明！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('艾莉的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400485V嗯、嗯……我明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 240, 80, -1, -1),
	Insn('TEXT_SET_NAME', Translate('缇欧的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#13400486V不太清楚状况，不过好吧。{color 0}{wait}'
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
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(257), 32),
	Insn('CHAR_FLAG1_UNSET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x0D'),
	Insn('CAM_DISTANCE', 18500, 3000),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 29))),
	Insn('SLEEP', 1000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('FORK_QUIT', Char(257), 255),
	Insn('FORK_QUIT', Char(352), 255),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0x2E', b'\x01\xff\xff'),
	Insn('0x2E', b'\x02\xff\xff'),
	Insn('0x2E', b'\x03\xff\xff'),
	Insn('SOUND_STOP', 806),
	Insn('FLAG_SET', Flag(739)),
	Insn('NEW_SCENE', 'c011c', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][28] = [
	Insn('0x92', Char(352), 18000, -11200, 500),
	Insn('FORK', 352, 1, [
		Insn('0x95', Char(254), (18000, 0, -11200), 2500, 1),
	]),
	Insn('FORK_AWAIT', Char(352), 1),
	Insn('FORK', 352, 1, [
		Insn('0x95', Char(254), (18000, -2000, -19600), 2500, 1),
	]),
	Insn('FORK_AWAIT', Char(352), 1),
	Insn('FORK', 352, 1, [
		Insn('0x95', Char(254), (27000, -4000, -19600), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(352), 1),
	Insn('RETURN'),
]

data['code'][29] = [
	Insn('0x92', Char(257), 18000, -11200, 500),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (18000, 0, -11200), 5000, 1),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (18000, -2000, -19600), 5000, 1),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (27000, -4000, -19600), 5000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('RETURN'),
]

data['code'][30] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch07200', 30),
	Insn('LOAD_CHCP', 'chr/ch09300', 31),
	Insn('LOAD_CHCP', 'chr/ch09400', 32),
	Insn('CAM_OFFSET', (32800, -3000, -19000), 0),
	Insn('CAM_ROTATE', 38, 25, 0, 0),
	Insn('0x6E', 650, 0),
	Insn('CAM_DISTANCE', 17500, 0),
	Insn('CHAR_SET_POS', Char(257), (35000, -4000, -19500), 270),
	Insn('CHAR_SET_POS', Char(258), (35000, -4000, -18500), 270),
	Insn('CHAR_SET_POS', Char(259), (36300, -4000, -19500), 270),
	Insn('CHAR_SET_POS', Char(260), (36300, -4000, -18500), 270),
	Insn('CHAR_SET_CHCP', Char(25), 30),
	Insn('CHAR_SET_FRAME', Char(25), 0),
	Insn('CHAR_SET_POS', Char(25), (31300, -4000, -19000), 90),
	Insn('CHAR_FLAG1_UNSET', Char(25), 4),
	Insn('CHAR_FLAG1_SET', Char(25), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(25), 128),
	Insn('CHAR_FLAG2_UNSET', Char(25), 32768),
	Insn('CHAR_SET_CHCP', Char(26), 31),
	Insn('CHAR_SET_FRAME', Char(26), 0),
	Insn('CHAR_SET_POS', Char(26), (30300, -4000, -18300), 90),
	Insn('CHAR_FLAG1_UNSET', Char(26), 4),
	Insn('CHAR_FLAG1_SET', Char(26), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(26), 128),
	Insn('CHAR_FLAG2_UNSET', Char(26), 32768),
	Insn('CHAR_SET_CHCP', Char(27), 32),
	Insn('CHAR_SET_FRAME', Char(27), 0),
	Insn('CHAR_SET_POS', Char(27), (30300, -4000, -19700), 90),
	Insn('CHAR_FLAG1_UNSET', Char(27), 4),
	Insn('CHAR_FLAG1_SET', Char(27), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(27), 128),
	Insn('CHAR_FLAG2_UNSET', Char(27), 32768),
	Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xff\xcf\xb5', 35, 150, 0),
	Insn('OBJ_SET_FRAME', Object(255), 'sky', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'sky1', Insn('1', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'sd_mul', Insn('0', 1)),
	Insn('CAM_ROTATE', 43, 23, 0, 11000),
	Insn('CAM_DISTANCE', 21500, 11000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('SLEEP', 1000),
	Insn('EXPR_CHAR_ATTR', Char(25), 40, Expr([Insn('CONST', 13), Insn('SET'), Insn('END')])),
	Insn('0x9C', Char(25), b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x01\x00\x00\xb8\x0b\x00\x00'),
	Insn('SLEEP', 100),
	Insn('0x9C', Char(25), b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x01\x00\x00\xb8\x0b\x00\x00'),
	Insn('SLEEP', 300),
	Insn('EMOTE', Char(25), 0, 1700, (38, 39, 250, 2)),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(257), 0, 2000, (38, 39, 250, 2)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 39, 250, 2)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (38, 39, 250, 2)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 39, 250, 2)),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(25), 270, 500),
	Insn('FORK_LOOP', 26, 2, [
		Insn('CHAR_WATCH', Char(254), Char(25), 500),
	]),
	Insn('FORK_LOOP', 27, 2, [
		Insn('CHAR_WATCH', Char(254), Char(25), 500),
	]),
	Insn('FORK', 25, 1, [
		Insn('0x96', Char(254), (30200, -4000, -19000), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(25), 1),
	Insn('FORK_QUIT', Char(26), 2),
	Insn('FORK_QUIT', Char(27), 2),
	Insn('EMOTE', Char(25), 0, 1600, (8, 9, 250, 0)),
	Insn('FORK', 26, 1, [
		Insn('0x97', Char(254), (-4000, 0, -1100), 1000, 1),
	]),
	Insn('FORK', 27, 1, [
		Insn('0x97', Char(254), (-4000, 0, -1100), 1000, 1),
	]),
	Insn('FORK', 25, 1, [
		Insn('0x98', Char(254), (-4000, 0, -1100), 1000, 1),
	]),
	Insn('FORK_AWAIT', Char(26), 1),
	Insn('FORK', 26, 1, [
		Insn('0x97', Char(254), (-7000, 0, 0), 1000, 1),
	]),
	Insn('FORK', 27, 1, [
		Insn('0x97', Char(254), (-7000, 0, 0), 1000, 1),
	]),
	Insn('FORK', 25, 1, [
		Insn('0x98', Char(254), (-7000, 0, 0), 1000, 1),
	]),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('EMOTE_STOP', Char(25)),
	Insn('FORK_QUIT', Char(26), 1),
	Insn('FORK_QUIT', Char(27), 1),
	Insn('FORK_QUIT', Char(25), 1),
	Insn('0x6F', b'y'),
	Insn('FLAG_SET', Flag(741)),
	Insn('NEW_SCENE', 'c011c', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][31] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CAM_OFFSET', (160, 5000, 20460), 0),
	Insn('CAM_ROTATE', 23, 30, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 17000, 0),
	Insn('CHAR_SET_POS', Char(257), (-1000, 3000, 22200), 180),
	Insn('CHAR_SET_POS', Char(258), (400, 3000, 22700), 180),
	Insn('CHAR_SET_POS', Char(259), (400, 3000, 24260), 180),
	Insn('CHAR_SET_POS', Char(260), (-1000, 3000, 23860), 180),
	Insn('SLEEP', 50),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x05\x004!\x00\x00\xdc\x05\x00\x00\x00'),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 258, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x05\x004!\x00\x00\xdc\x05\x00\x00\x00'),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x05\x004!\x00\x00\xdc\x05\x00\x00\x00'),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 260, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x05\x004!\x00\x00\xdc\x05\x00\x00\x00'),
	]),
	Insn('CAM_OFFSET', (-2940, 5000, 12880), 4800),
	Insn('CAM_ROTATE', 41, 28, 0, 4800),
	Insn('0x6E', 600, 4800),
	Insn('CAM_DISTANCE', 16500, 4800),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SLEEP', 3500),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'c0240', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][32] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 800),
	Insn('CAM_OFFSET', (-29840, 700, 9950), 0),
	Insn('CAM_ROTATE', 301, 36, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 13500, 0),
	Insn('CHAR_SET_POS', Char(257), (-31110, -1000, 11250), 270),
	Insn('CHAR_SET_POS', Char(258), (-28840, -1000, 11440), 270),
	Insn('CHAR_SET_POS', Char(259), (-29910, -1000, 11720), 270),
	Insn('CHAR_SET_POS', Char(260), (-27680, -1000, 11600), 270),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('0x0D'),
	Insn('SLEEP', 200),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 300),
	Insn('CHAR_ROTATE', Char(257), 180, 400),
	Insn('SLEEP', 600),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0005F咦……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_LOOP', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('FORK_LOOP', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('FORK_LOOP', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('0x95', Char(257), (-31250, -1000, 9570), 700, 0),
	Insn('CHAR_ROTATE', Char(257), 135, 500),
	Insn('SLEEP', 200),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}栏杆上有很新的刮痕。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0305F罗伊德，发现什么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0001F嗯……好像有\n'
		'一些刮痕。{wait}'
		'{page}'
		'#0003F而且还是在靠里侧……\n'
		'应该不会是过路的人\n'
		'造成的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11P#0200F说起来，这个后门\n'
		'最适合侵入公寓呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 200),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(259), 1),
	Insn('CHAR_WATCH', Char(257), Char(259), 500),
	Insn('EMOTE', Char(257), 0, 2300, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2300, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2300, (38, 38, 250, 1)),
	Insn('SLEEP', 800),
	Insn('FORK', 0, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('SLEEP', 10),
	Insn('FORK', 1, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK', 2, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('SLEEP', 12),
	Insn('FORK', 3, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('SLEEP', 200),
	Insn('CAM_OFFSET', (-19620, 700, 13840), 4000),
	Insn('CAM_ROTATE', 16, 20, 0, 4000),
	Insn('SLEEP', 5200),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-29840, 700, 9950), 0),
	Insn('CAM_ROTATE', 301, 36, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 13500, 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0305F的确，走这里的话，就可以\n'
		'避开大道，轻松溜进来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0103F目击情报很少，\n'
		'就是这个原因吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('QUEST', 29, Insn('TASK_SET', 8)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 29, Insn('TASK_GET', 4))), Insn('EXEC', Insn('QUEST_GET', 29, Insn('TASK_GET', 5))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 29, Insn('TASK_GET', 6))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 29, Insn('TASK_GET', 7))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 29, Insn('TASK_GET', 8))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0000F好，预先调查就到此为止吧。{wait}'
				'{page}'
				'先回伊莉雅小姐的房间，\n'
				'整理一下情报吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#12P#0300F明白，差不多也该考虑作战计划了吧！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('QUEST', 29, Insn('TASK_SET', 9)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0003F…………………………{wait}'
				'{page}'
				'#0001F现在就下判断还很危险，\n'
				'再探听一下情报吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#12P#0300F明白，这就去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_POS', Char(0), (-30970, -1000, 11070), 270),
	Insn('0x66', 3, 1),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][33] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 29, Insn('TASK_GET', 3))), Insn('EXEC', Insn('QUEST_GET', 29, Insn('TASK_GET', 8))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 32))),
			Insn('RETURN'),
		]),
		(None, []),
	]),
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}栏杆上有\n'
		'刮擦过的痕迹。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}似乎是最近才有的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][34] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch10100', 30),
	Insn('CAM_OFFSET', (-19540, 660, 12830), 0),
	Insn('CAM_ROTATE', 53, 41, 0, 0),
	Insn('0x6E', 420, 0),
	Insn('CAM_DISTANCE', 31000, 0),
	Insn('CHAR_SET_POS', Char(257), (-29500, -1000, 11640), 56),
	Insn('CHAR_SET_POS', Char(258), (-8400, 0, 6880), 0),
	Insn('CHAR_SET_POS', Char(259), (-8400, 0, 6880), 0),
	Insn('CHAR_SET_POS', Char(260), (-10300, 0, 13950), 0),
	Insn('CHAR_SET_POS', Char(28), (-19560, -1000, 14750), 180),
	Insn('CHAR_FLAG1_UNSET', Char(28), 128),
	Insn('CHAR_FLAG1_SET', Char(28), 32768),
	Insn('CHAR_SET_CHCP', Char(28), 30),
	Insn('CHAR_SET_FRAME', Char(28), 0),
	Insn('EXPR_CHAR_ATTR', Char(28), 40, Expr([Insn('CONST', 13), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(19), 128),
	Insn('CHAR_FLAG2_SET', Char(19), 32768),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('OBJ_FLAG_UNSET', Object(1), 16),
	Insn('0x70', Object(1), b'\n\x00'),
	Insn('CAM_ROTATE', 37, 31, 0, 3900),
	Insn('FORK', 28, 1, [
		Insn('0x95', Char(254), (-19560, -1000, 12750), 2000, 0),
	]),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SLEEP', 1200),
	Insn('0x95', Char(260), (-10300, 0, 7880), 4000, 0),
	Insn('SLEEP', 900),
	Insn('TEXT_TALK2', Char(260), Translate('声音'), Text(
		'#5C#1P找到了吗……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(258), Translate('声音'), Text(
		'#5C#1P已经不见踪影了，\n'
		'大街上似乎也没人看见过。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(259), Translate('声音'), Text(
		'#5C#3P真奇怪呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(28), Translate('少年'), Text(
		'#14002F#5P哼……\n'
		'……以为那么简单\n'
		'就可以抓到我吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-19540, 660, 12830), 0),
	Insn('CAM_ROTATE', 40, 36, 0, 0),
	Insn('0x6E', 320, 0),
	Insn('CAM_DISTANCE', 27430, 0),
	Insn('0x0D'),
	Insn('SLEEP', 200),
	Insn('CHAR_ROTATE', Char(28), 270, 400),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK2', Char(28), Translate('少年'), Text(
		'#14003F#5P这种城市里的\n'
		'窝囊废……{wait}'
		'{page}'
		'#14007F#5P哼，看着吧。\n'
		'之后我再好好整你们……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('CAM_OFFSET', (-22720, 660, 11450), 1200),
	Insn('CAM_ROTATE', 56, 36, 0, 1200),
	Insn('0x95', Char(28), (-19900, -1000, 11430), 6000, 1),
	Insn('0x95', Char(28), (-22720, -1000, 11450), 6000, 0),
	Insn('EMOTE', Char(28), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('0x9C', Char(28), b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x03\x00\x00\xe0.\x00\x00'),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK2', Char(28), Translate('少年'), Text(
		'#14011F#11P啊……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(257), Translate('声音'), Text(
		'#2P事情可没那么简单哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-24890, 660, 11580), 2000),
	Insn('CAM_DISTANCE', 31610, 2000),
	Insn('0x95', Char(257), (-26250, -1000, 12160), 1800, 0),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0001F我们知道你走的是这条路线，\n'
		'这次是我们的作战胜利了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(28), Translate('少年'), Text(
		'#14007F#11P可恶……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 28, 1, [
		Insn('0x95', Char(254), (-21200, -1000, 11420), 5000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0007F你还是放弃挣扎吧！{wait}'
	)),
	Insn('CAM_OFFSET', (-20560, 660, 11200), 2000),
	Insn('CAM_ROTATE', 306, 36, 0, 2000),
	Insn('0x95', Char(257), (-21850, -1000, 11450), 6000, 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('SOUND_PLAY', 819, 0, 0, 100),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(28), Translate('少年'), Text(
		'#14015F#12P哇……可恶……！！\n'
		'你这混帐……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(28), 0, 2000, (40, 43, 100, 0)),
	Insn('FORK_FUNC', Char(28), 2, Function((0, 35))),
	Insn('SLEEP', 100),
	Insn('FORK_FUNC', Char(257), 2, Function((0, 35))),
	Insn('TEXT_TALK2', Char(28), Translate('少年'), Text(
		'#14015F#12P放、放手……放开我……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0001F那可不行。\n'
		'你的行为是犯罪……{wait}'
		'{page}'
		'#0006F……我说你，\n'
		'老实一点啦……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('FORK_FUNC', Char(29), 1, Function((0, 39))),
	Insn('TEXT_TALK2', Char(28), Translate('少年'), Text(
		'#14007F#12P可恶……混帐！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0010F好痛……\n'
		'喂，不要乱甩胳膊啊！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_POS', Char(260), (-11580, 0, 6930), 261),
	Insn('CHAR_SET_POS', Char(258), (-10570, 0, 6180), 261),
	Insn('CHAR_SET_POS', Char(259), (-10050, 0, 7210), 261),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F哈哈，这家伙真是\n'
		'很有活力嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE_STOP', Char(28)),
	Insn('EMOTE', Char(28), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 300),
	Insn('FORK_QUIT', Char(28), 2),
	Insn('FORK', 28, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('CAM_OFFSET', (-18900, 860, 8630), 2000),
	Insn('CAM_ROTATE', 309, 24, 0, 2000),
	Insn('FORK_FUNC', Char(260), 1, Function((0, 38))),
	Insn('SLEEP', 200),
	Insn('FORK_FUNC', Char(258), 1, Function((0, 36))),
	Insn('SLEEP', 200),
	Insn('FORK_FUNC', Char(259), 1, Function((0, 37))),
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK2', Char(28), Translate('少年'), Text(
		'#14005F#11P你、你们是刚才的……{wait}'
		'{page}'
		'#14011F#11P你、你们竟敢骗我……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0202F#12P嘻……\n'
		'要演戏还真是累人呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#6P#0100F虽然被你的敏捷身手\n'
		'吓了一跳，\n'
		'不过总算是抓到了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0000F嗯，不过……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 7000),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('CHAR_ROTATE', Char(28), 90, 500),
	Insn('CHAR_ROTATE', Char(257), 90, 500),
	Insn('FORK_FUNC', Char(28), 2, Function((0, 35))),
	Insn('SLEEP', 800),
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
	Insn('TEXT_TALK', Char(260), Text(
		'#6P#0303F好像跟想像中的不太一样啊。{wait}'
		'{page}'
		'#0300F听说是个朴素的家伙，\n'
		'实际一看，倒不如说是不修边幅，\n'
		'或者是有点脏兮兮吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#6P#0105F而且好像不是\n'
		'克洛斯贝尔的孩子……{wait}'
		'{page}'
		'是出身于某处边境地区吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0200F从犯罪行为来看，\n'
		'与其说是狂热的崇拜者，\n'
		'反而更像是偷闯空门的吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0001F嗯，具体的事由，\n'
		'还要请你一五一十交代清楚。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0006F话说……\n'
		'你差不多快给我老实点吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(28), Translate('少年'), Text(
		'#14007F#11P住手，放开我……！\n'
		'……放手啊，你这个混帐！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('CAM_DISTANCE', 35190, 1800),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(29), 1),
	Insn('FLAG_SET', Flag(737)),
	Insn('NEW_SCENE', 'c0240', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][35] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('0xA6', Char(254), 0, 20, 600, 3000),
		Insn('SLEEP', 800),
		Insn('0xA6', Char(254), 0, 30, 600, 3000),
		Insn('SLEEP', 1200),
	]),
	Insn('RETURN'),
]

data['code'][36] = [
	Insn('0x95', Char(258), (-17370, 0, 6510), 2000, 0),
	Insn('CHAR_ROTATE', Char(254), 315, 500),
	Insn('RETURN'),
]

data['code'][37] = [
	Insn('0x95', Char(259), (-16239, 0, 7090), 2000, 0),
	Insn('CHAR_ROTATE', Char(254), 315, 500),
	Insn('RETURN'),
]

data['code'][38] = [
	Insn('0x95', Char(260), (-17830, 0, 7480), 2000, 0),
	Insn('CHAR_ROTATE', Char(254), 315, 500),
	Insn('RETURN'),
]

data['code'][39] = [
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('SOUND_PLAY', 819, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('SOUND_PLAY', 819, 0, 0, 100),
	Insn('RETURN'),
]

data['code'][40] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1294)), Insn('FLAG', Flag(1303)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F住宅区那边应该由\n'
						'哈罗德先生在负责寻找……{wait}'
						'{page}'
						'如果找到的话，\n'
						'肯定会马上联系我的吧。{wait}'
						'{page}'
						'#0001F还是按照原定计划，\n'
						'继续在我负责的街区探听吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(8)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F住宅区那边应该由\n'
						'哈罗德先生在负责寻找……{wait}'
						'{page}'
						'#0001F还是按照原定计划，\n'
						'继续在我负责的街区探听吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (110, 3000, 22760), 180),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1303)), Insn('FLAG', Flag(1307)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F现在可不是绕道的时候……{wait}'
				'{page}'
				'还是尽快\n'
				'前往西克洛斯贝尔街道吧！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (110, 3000, 22760), 180),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][41] = [
	Insn('EVENT_BEGIN', 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F现在就算离开市区，\n'
		'也打听不到情报的。{wait}'
		'{page}'
		'……还是在这一带\n'
		'再仔细探听一下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (-34230, 0, 4210), 90),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][42] = [
	Insn('EVENT_BEGIN', 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F现在没有什么要事……\n'
		'还是专心寻找柯林吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (36500, -4000, -19000), 270),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]
