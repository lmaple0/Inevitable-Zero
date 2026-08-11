# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'c1100',
	'name2': 'c1100',
	'location': 22,
	'bgm': 100,
	'flags': 8192,
	'includes': [
		'c1100',
		None,
		't1500_1',
		None,
		None,
		None,
	],
	'name3': 'c1100',
	'labels': [
		{
			'pos': (-31.530000686645508, 0.0, -107.9000015258789),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('中央广场'),
		},
		{
			'pos': (-117.0, 0.0, -102.05000305175781),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('西侧大道'),
		},
		{
			'pos': (3.5799999237060547, 0.0, 7.800000190734863),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('行政区'),
		},
		{
			'pos': (-196.3000030517578, 0.0, -5.199999809265137),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('住宅区'),
		},
		{
			'pos': (-101.4000015258789, 0.0, -15.600000381469727),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('欢乐街'),
		},
		{
			'pos': (74.0999984741211, 0.0, -137.8000030517578),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('东侧大道'),
		},
		{
			'pos': (120.25, 0.0, -209.3000030517578),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('旧市街'),
		},
		{
			'pos': (110.5, 0.0, -52.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('港湾区'),
		},
		{
			'pos': (76.69999694824219, 0.0, 70.19999694824219),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('ＩＢＣ'),
		},
		{
			'pos': (-16.899999618530273, 0.0, -197.60000610351562),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('站前大道'),
		},
		{
			'pos': (-78.0, 0.0, -62.400001525878906),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('小巷'),
		},
		{
			'pos': (-20.799999237060547, 0.0, -237.89999389648438),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('乌尔斯拉小径'),
		},
		{
			'pos': (144.3000030517578, 0.0, -119.5999984741211),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('东克洛斯贝尔街道'),
		},
		{
			'pos': (-183.3000030517578, 0.0, -104.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('西克洛斯贝尔街道'),
		},
		{
			'pos': (-175.5, 0.0, 26.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('玛因兹山道'),
		},
		{
			'pos': (-60.130001068115234, 0.0, -126.0999984741211),
			'unk': b'\x00\x00Q\x00',
			'name': Translate(''),
		},
		{
			'pos': (9.75, 0.0, -92.30000305175781),
			'unk': b'\x00\x00T\x00',
			'name': Translate(''),
		},
		{
			'pos': (-28.280000686645508, 0.0, -136.5),
			'unk': b'\x00\x00W\x00',
			'name': Translate(''),
		},
		{
			'pos': (-61.099998474121094, 0.0, -88.4000015258789),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-34.45000076293945, 0.0, -57.20000076293945),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-100.43000030517578, 0.0, -94.9000015258789),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-113.0999984741211, 0.0, -67.5999984741211),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-81.9000015258789, 0.0, -26.0),
			'unk': b'\x00\x00R\x00',
			'name': Translate(''),
		},
		{
			'pos': (-75.7300033569336, 0.0, -42.900001525878906),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-64.3499984741211, 0.0, -53.95000076293945),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-27.299999237060547, 0.0, 38.349998474121094),
			'unk': b'\x00\x00Q\x00',
			'name': Translate(''),
		},
		{
			'pos': (118.30000305175781, 0.0, -137.8000030517578),
			'unk': b'\x00\x00R\x00',
			'name': Translate(''),
		},
		{
			'pos': (96.19999694824219, 0.0, -255.4499969482422),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (79.30000305175781, 0.0, -231.39999389648438),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-16.899999618530273, 0.0, -123.5),
			'unk': b'\x00\x00V\x00',
			'name': Translate(''),
		},
	],
	'chcp': [
		'chr/ch24900',
		'chr/ch20800',
		'chr/ch28100',
		'chr/ch00900',
		'chr/ch30500',
		'chr/ch20300',
		'chr/ch34200',
		'chr/ch30000',
		'chr/ch30300',
		'chr/ch30200',
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
			'name': Translate('库罗玛'),
			'pos': (6929, 2490, -6650),
			'angle': 225,
			'_1': b'\x05\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((0, 5)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('奥特'),
			'pos': (8369, 2390, -14850),
			'angle': 90,
			'_1': b'\x05\x01\x00\x00\x01\x00\x00\x01',
			'function': Function((0, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('塔吉克'),
			'pos': (-8739, 2500, 6070),
			'angle': 180,
			'_1': b'\x05\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 8)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('弗兰兹巡警'),
			'pos': (-15050, 2500, 27399),
			'angle': 180,
			'_1': b'\x05\x01\x00\x00\x07\x00\x00\x00',
			'function': Function((0, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('达德利搜查官'),
			'pos': (-22500, 2500, 24280),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 10)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('艾玛搜查官'),
			'pos': (-23659, 2500, 24280),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((0, 12)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('夏娜'),
			'pos': (6530, 2500, -8260),
			'angle': 45,
			'_1': b'\x85\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('亚比'),
			'pos': (6969, 2500, -9149),
			'angle': 45,
			'_1': b'\x85\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((0, 14)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('多诺邦警部'),
			'pos': (-21790, 2500, 27280),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x08\x00\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('雷蒙德搜查官'),
			'pos': (-21100, 2500, 26180),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\t\x00\x00\x00',
			'function': Function((0, 16)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('银'),
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
			'pos': (8.539999961853027, -5.630000114440918, 2.450000047683716),
			'range': 68.0625,
			'transform': [
				0.12856483459472656,
				0.23570236563682556,
				-0.0,
				0.0,
				-0.12856492400169373,
				0.23570221662521362,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000001788139343,
				0.0,
				-1.8217642307281494,
				-0.6858947277069092,
				-0.49000003933906555,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 17)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (-5890, 2500, 31840),
			'range': 1200,
			'bubble_pos': (-5890, 4000, 31840),
			'_1': b'|\x00\x00',
			'function': Function((0, 24)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01r\x10\x00\x00\xc4\t\x00\x00\xe2"\x00\x00\x00\x00\x00\x00\x01\x00\x16\x00', Function((0, 3)), Function((0, 4))),
	'code': [None]*25,
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
		Insn('0x95', Char(254), (17250, 2500, -14850), 1000, 0),
		Insn('0x95', Char(254), (17250, 2500, -70), 1000, 0),
		Insn('0x95', Char(254), (3810, 2500, 8270), 1000, 0),
		Insn('0x95', Char(254), (-6210, 2500, 23860), 1000, 0),
		Insn('0x95', Char(254), (-18440, 2500, 23260), 1000, 0),
		Insn('0x95', Char(254), (-20840, 2450, 19170), 1000, 0),
		Insn('0x95', Char(254), (-18240, 2500, 6490), 1000, 0),
		Insn('0x95', Char(254), (-18430, 2500, -3620), 1000, 0),
		Insn('0x95', Char(254), (-7420, 2500, -14630), 1000, 0),
		Insn('0x95', Char(254), (8370, 2390, -14850), 1000, 0),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (8050, -5420), (4250, -10070), 2000),
		Insn('SLEEP', 200),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 107), Insn('EQ'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('0x23', 7), Insn('CONST', 5), Insn('EQ'), Insn('0x23', 7), Insn('CONST', 11), Insn('EQ'), Insn('OR'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (30170, 2500, -90), 270),
					Insn('CHAR_SET_POS', Char(1), (30170, 2500, -90), 270),
					Insn('CHAR_SET_POS', Char(2), (30170, 2500, -90), 270),
					Insn('CHAR_SET_POS', Char(3), (30170, 2500, -90), 270),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (30170, 2500, -90), 270),
							Insn('CHAR_SET_POS', Char(5), (30170, 2500, -90), 270),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (30170, 2500, -90), 270),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 101), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('0x23', 7), Insn('CONST', 6), Insn('EQ'), Insn('0x23', 7), Insn('CONST', 7), Insn('EQ'), Insn('OR'), Insn('0x23', 7), Insn('CONST', 10), Insn('EQ'), Insn('OR'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (-40390, 0, 24150), 90),
					Insn('CHAR_SET_POS', Char(1), (-40390, 0, 24150), 90),
					Insn('CHAR_SET_POS', Char(2), (-40390, 0, 24150), 90),
					Insn('CHAR_SET_POS', Char(3), (-40390, 0, 24150), 90),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-40390, 0, 24150), 90),
							Insn('CHAR_SET_POS', Char(5), (-40390, 0, 24150), 90),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-40390, 0, 24150), 90),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 102), Insn('SET'), Insn('END')])),
				]),
				(None, [
					Insn('CHAR_SET_POS', Char(0), (19940, 0, -37920), 0),
					Insn('CHAR_SET_POS', Char(1), (19940, 0, -37920), 0),
					Insn('CHAR_SET_POS', Char(2), (19940, 0, -37920), 0),
					Insn('CHAR_SET_POS', Char(3), (19940, 0, -37920), 0),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (19940, 0, -37920), 0),
							Insn('CHAR_SET_POS', Char(5), (19940, 0, -37920), 0),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (19940, 0, -37920), 0),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 100), Insn('SET'), Insn('END')])),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('0xD0', 7, Expr([Insn('CONST', 4), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(8), 45, 0),
			Insn('CHAR_FLAG1_SET', Char(11), 128),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(11), 128),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 38, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(8), 128),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_SET_POS', Char(16), (-22770, 2500, 26320), 90),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(11), 128),
		]),
		(Expr([Insn('FLAG', Flag(536)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), []),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('FLAG_SET', Flag(9)),
			Insn('EVENT', Function((0, 21))),
		]),
		(Expr([Insn('FLAG', Flag(737)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(737)),
			Insn('FLAG_SET', Flag(9)),
			Insn('EVENT', Function((0, 22))),
		]),
		(Expr([Insn('FLAG', Flag(738)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(738)),
			Insn('EVENT', Function((0, 23))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(768)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(555)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x09', 268435456),
			Insn('EVENT', Function((0, 20))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(538)), Insn('FLAG', Flag(768)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 111), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('OBJ_FLAG_SET', Object(6), 4),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(536)), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(6), 4),
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
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(9)), Insn('END')]), [
			Insn('SOUND_STOP', 123),
		]),
		(None, [
			Insn('SOUND_POSITION', 123, [
				-19670,
				2460,
				-15580,
				10000,
				100000,
			], 100, 0),
		]),
	]),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 38, Insn('TASK_GET', 2))), Insn('END')]), [
					Insn('OBJ_FLAG_SET', Object(4), 4),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 38, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('0xB5', b'\x01\x00\x80\x00'),
					Insn('OBJ_FLAG_SET', Object(4), 4),
				]),
				(None, []),
			]),
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
				Insn('OPEN_SHOP', 128),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), []),
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
				Insn('IF', [
					(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'啊……差不多\n'
									'也该打烊了哦。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'要买饮料的话，就抓紧最后的机会吧。\n'
									'想喝什么，请随便吩咐。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'要买饮料的话，就抓紧最后的机会吧。\n'
									'想喝什么，请随便吩咐。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
						Insn('TEXT_TALK', Char(254), Text(
							'今早好像有很多\n'
							'警察在晃来晃去呢。{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(254), Text(
							'难道是发生了什么事吗……{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'啊呀，今天是个大晴天呢……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'一下雨就没法做生意了，\n'
									'好天气真是帮了我的大忙呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'今天天气好像会很热呢，\n'
									'生意应该会很红火吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'因为要召开议会，\n'
									'这一带从早到晚都很热闹。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'可是……议员和媒体人士\n'
									'都不常来我这里买东西呢……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'我还是比较喜欢纪念庆典。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'议会之类的，\n'
									'实在是搞不懂……{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'嗯～差不多也该\n'
									'换个地方了吧……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'必须要把握住那些在纪念庆典\n'
									'之后准备回国的客人啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'欢迎光临～！\n'
									'要不要来一杯新鲜果汁～？{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'……在市内观光时要是累了的话，\n'
									'就来和姐姐我说吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'我可以卖给你们\n'
									'美味的果汁哦。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 14))), Insn('BOOL_AND'), Insn('END')]), [
								Insn('CALL', Function((2, 17))),
							]),
							(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'为了应对纪念庆典，\n'
									'我准备多订购一些\n'
									'制作果汁用的水果。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'……说起来，\n'
									'妈妈好像也说过类似的话呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'嗯～我也不能输啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'我妈妈在百货\n'
									'负责食材专柜。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'她对进货流程非常熟悉……\n'
									'我也应该多向她学习一些这方面的窍门吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 14))), Insn('BOOL_AND'), Insn('END')]), [
								Insn('CALL', Function((2, 17))),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'欢迎光临。\n'
									'客人，您想点些什么吗？{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'我妈妈在百货里\n'
									'负责食材专柜。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'她从以前开始就一直从事着进口食材的工作，\n'
									'曾经开过一家很有名气的店呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'呵呵，我之所以会走上经商的道路，\n'
									'说不定也是受了母亲的影响呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'我妈妈在百货\n'
									'负责食材专柜。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'在经营进口食材方面，也算是\n'
									'有着一定的信誉与好评。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'我也想自己试着做些生意，\n'
									'于是就开始经营这家店了。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'不过……为了购买这架三轮货车，\n'
									'我还贷款了呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'……必须要努力赚钱才行哦。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'因为我想尝试着靠自己的力量来创业，\n'
									'所以没有求助于母亲，而是选择了贷款。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'只有把生意做好，顺利还清贷款，\n'
									'才能算是真正意义上的经商。\n'
									'……必须要更加努力才行呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('RECIPE', 22)), Insn('NOT'), Insn('END')]), [
								Insn('CALL', Function((0, 6))),
							]),
							(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'欢迎光临～！\n'
									'要不要来点果汁呢～？{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'……刚才有位游击士\n'
									'来和我搭话呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'而、而且还是个\n'
									'挺帅气的人哦……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'游、游击士果然\n'
									'很帅呀。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('RECIPE', 22)), Insn('NOT'), Insn('END')]), [
								Insn('CALL', Function((0, 6))),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'我这家店很受\n'
									'游客们的欢迎呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'呵呵，走累了的时候，大家\n'
									'肯定都想喝上一杯果汁吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'选择经营果汁店，真是太正确了。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('RECIPE', 22)), Insn('NOT'), Insn('END')]), [
								Insn('CALL', Function((0, 6))),
							]),
							(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'嗯～今天也是个好天气呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'我感觉清凉的果汁\n'
									'应该会卖得很好。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'欢迎光临～！\n'
									'要不要来一杯橙汁呀～！{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'非常冰凉爽口\n'
									'的美味橙汁哦～！{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
						Insn('TEXT_TALK', Char(254), Text(
							'新鲜的果汁哦～！{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(254), Text(
							'在市内四处奔波的疲惫客人，\n'
							'怎么样，要不要来杯果汁呢？{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(254), Text(
							'我这里有非常清凉的\n'
							'新鲜果汁哦～！{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
						Insn('TEXT_TALK', Char(254), Text(
							'欢迎光临～！\n'
							'要不要来一杯新鲜果汁～？{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(254), Text(
							'香橙、蜜瓜……\n'
							'各种果汁一应俱全哦～！{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(None, []),
				]),
			]),
			(None, []),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('TEXT_TALK', Char(254), Text(
		'欢迎光临～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'对了，今天就把\n'
		'美味果汁的制作方法\n'
		'教给各位吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'在长途跋涉或剧烈运动之后，\n'
		'补充水分可是很重要的哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'学习了{item 464}{color 0}的做法。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'记住了{item 464}{color 0}的食谱。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('RECIPE', 22),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'今日的夕阳…\n'
						'总觉得带有一股哀愁的色彩呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'惆怅的晚霞，冰冷的微风，\n'
						'还有那重归于寂静的傍晚钟声……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'简直就是克洛斯贝尔的一道独特风景啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'你们差不多\n'
						'也该早点回家了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'夜晚的欢乐街\n'
						'可是个相当危险的场所呢！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'今天的议会，似乎又像往日一样，\n'
						'继续着没完没了的争论呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，到底要到什么时候才能结束啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'今天都已经是延期的第三天了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'还是一点都没变，自治州的议会\n'
						'每次都只会不断延长会期！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔时报周刊的最新一期\n'
						'好像因故而临时休刊了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'据说有人想去商店里购买，\n'
						'结果也都发现没有到货。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……究竟是怎么回事呢？\n'
						'我要求他们做出能让人信服的说明！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔时报周刊的最新一期\n'
						'竟然会延迟出版……怎么会有这种事！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯……莫非是发生什么事件了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'总觉得最近这段时间有些不太平呢，\n'
				'大概只是我的错觉吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'纪念庆典已经过去了，\n'
				'街上也恢复了往日的平静。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，果然还是平和宁静的感觉最好啊！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'#4S伊莉雅大人～！！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，今天的天气也不错啊！！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我听说，彩虹剧团\n'
						'好像要进行一次\n'
						'对内公开的预演呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……真狡猾！！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我们普通市民\n'
						'明明也很期待的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'据说彩虹剧团准备在公演前\n'
						'进行一次预演给赞助商欣赏呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……真狡猾！\n'
						'我也很想看啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'市政厅那里差不多\n'
						'也该开始讨论预算草案了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'议员们唇枪舌剑的交锋，\n'
						'似乎会很难收场吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，为了克洛斯贝尔的将来，\n'
						'希望大家能努力啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'市长和市政府职员们\n'
						'也必须要努力呀！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'你们很期待彩虹剧团\n'
						'的最新剧码吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我也很期待的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我弄到了Ｂ席的票，\n'
						'就去好好欣赏一下吧！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'伊莉雅大人～！！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，身为死忠支持者，\n'
						'必须要每天叫一次才行啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'警察局的那个副局长，\n'
						'我见过好几次了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'就是那个一脸狡猾之相，\n'
						'身材矮小的人吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我看见他在午休时间里\n'
						'急急忙忙地跑出去了呢！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'警察局的那个副局长\n'
						'长着一张很好记的脸。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然不是什么令人喜爱的类型，\n'
						'但离得很远时就能认出来了！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'如今的市政厅，是一座\n'
						'在五十年前建造的建筑物。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'出自一位名叫Ｊ丄金德尔\n'
						'的著名建筑师之手！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'威风凛凛，而且潇洒气派。\n'
						'真是个非常适合用来代表\n'
						'克洛斯贝尔的建筑啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'市政厅的建筑物，是由一位\n'
						'非常著名的建筑师设计的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'它也很受游客的欢迎，\n'
						'算是一大观光景点呢！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'市长虽然已经上了年纪，\n'
				'但还是经常出差，并参加各种活动。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，希望他也能\n'
				'保重自己的身体啊！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'你知道克洛斯贝尔\n'
						'市政厅的宣传语吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'『让政务对市民开放』……\n'
						'他们是这么宣扬的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'希望他们能多加努力，\n'
						'让这句话早日成为现实啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔市政厅有着\n'
						'『让政务对市民开放』\n'
						'这一口号。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……但实际上，真正会来这里的市民\n'
						'其实很少，平时可以说是门可罗雀呢！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'早安……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，你们几个好像是\n'
						'克洛斯贝尔的市民啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我本来还在想，如果是游客的话，\n'
						'可以对这一带给你们做个详细的介绍呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'本地市民的话，那就没必要了！\n'
						'应该也不用再特意介绍什么了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'这一带是行政机关集中的一个街区，\n'
						'所以市民比较稀少。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'咳咳，我只是出来散散步，\n'
						'无意中转到这附近而已！{wait}'
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
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'听我说啊！\n'
						'预算会议终于结束了！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呼，心中的一块大石头总算是\n'
						'落了地，可以安心回家啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不管怎么说，预算毕竟是件\n'
						'很重要的事情啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'虽然总算是可以安心工作了……\n'
						'但作为财务课的一员，\n'
						'果然还是十分在意呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'刚才有个媒体界的人士\n'
						'纠缠不休地向我发问。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嘿，问什么议会的动向之类，\n'
						'那种事情，我怎么可能知道～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不如说我才比较想知道答案啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'预算会议还在继续进行啊。\n'
						'身为起草预算案的财务课一员，\n'
						'实在是非常在意呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'议事堂那里，今天也是\n'
						'从早上就开始召开预算会议呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……表面上说是什么会议，\n'
						'其实根本就是帝国派与共和国派\n'
						'在对骂而已。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呼……\n'
						'麦克道尔市长也真是很辛苦呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'帝国派和共和国派的人\n'
						'今天也在议事堂那里\n'
						'互相对骂呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'本应起到调解引导作用的\n'
						'哈尔特曼议长却是个帝国派……\n'
						'麦克道尔市长也真是很辛苦呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啊～真闲啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然很担心预算会议的结果，\n'
				'但我终究是什么都做不了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 38, Insn('TASK_GET', 3))), Insn('EXEC', Insn('QUEST_GET', 38, Insn('TASK_GET', 4))), Insn('OR'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊，果汁店的车子\n'
						'跑到站前大道那边了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……不知为何，我也感觉有些口渴了。\n'
						'稍后就去那边看看吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 38, Insn('TASK_GET', 2))), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'嘿，你问果汁店的车子\n'
						'去哪里了？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'说起来，我刚才倒是看见\n'
						'店主把车子推向南出口那边了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'为了提高店铺的知名度，\n'
						'时不时也要去其它\n'
						'地方卖一阵子啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'从明天开始，预算会议总算要正式召开了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'提交预算草案之后，\n'
						'也就没有我们这些政府职员的事了……\n'
						'嗯～但还是很在意啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'从明天开始，预算会议总算要正式召开了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……就算我现在也久经世故了，\n'
						'但那毕竟是自己的工作。\n'
						'果然很在意呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'在刚才的审议中，\n'
						'我看见了哈尔特曼议长呢，\n'
						'虽然只是瞥到了一眼。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……呜呜，\n'
						'那个人确实是与众不同呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'散发着一种难以形容的威严气势。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'哈尔特曼议长基本\n'
						'不会直接参与什么……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但却仍然有着非同寻常的威信，\n'
						'真不愧是重量级的大政治家啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'呼，累死了，累死了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'今天的会议，不如就偷懒不去了吧～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'反正即使我出席，\n'
						'也只会被议员先生们横加干涉而已。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'这种时期，财务课真是很辛苦呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'在自治州议会上，\n'
						'帝国派所占的席位超过半数。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但再怎么说，也没有达到三分之二的人数，\n'
						'仍然无法随心所欲地强行定夺。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'所以每次都争斗得很激烈呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'帝国派与共和国派争斗不休，\n'
						'受此牵连而不幸告吹的\n'
						'预算草案实在是数不胜数。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'比如说……那个正在\n'
						'建设中的新市政厅大楼。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然已经投入了预算，\n'
						'但因为无法决定由哪边来掌握主导权，\n'
						'所以直到如今也在争执不休。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'施工进行到一半，就这么搁置下来了。\n'
						'……要到什么时候才能重新开工呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'在市政厅的会议室，\n'
						'正在对预算草案进行争论呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'为了应对下个月的预算会议，\n'
						'要先商讨出一个基本大纲。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'本来那只是我们这些\n'
						'财政课职员的会议……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……但不知为何，连那些\n'
						'议员先生也都前来参与了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呼，下午的会议\n'
						'也必须要去参加啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'希望议员先生\n'
						'能稍微退避一下啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'警察啊……这个星期好像是\n'
						'你们的防犯强化周吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'难怪感觉最近总是能看到很多警官，\n'
						'大概就是因为这个吧～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'警察也真是的，有这种活动的话，\n'
						'直接发个正式通知不就行了嘛。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'差不多也该继续\n'
						'研讨下一个预算草案了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……又要承受那些\n'
						'大人物施加的压力了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'啊啊，头好疼……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我刚到市政厅就任的时候，\n'
						'也是一个满怀希望的有志青年……！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但经过这两三年的磨练，我才算是明白了。\n'
						'什么才是现实中的政治……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'在克洛斯贝尔自治州行驶的巴士\n'
						'都由交通课来进行管理。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这个部门是在五年前设立的，\n'
						'好像一直都非常忙碌呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，多亏了那些家伙，\n'
						'巴士才能正常运行啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'交通课的人真是很辛苦呢～\n'
						'而我们却老是这么拖拖拉拉的，\n'
						'实在是很难为情啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我的上司就爱\n'
						'没事乱找碴。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'经常下达一些莫名其妙的无聊命令……\n'
						'总是这样的话，根本就不能集中精神工作啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'啊～真不想回去工作啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'市职员的薪酬虽然还不错，\n'
						'但工作环境实在是太糟糕了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'呼……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'像我所在的财务课，\n'
						'总是要承受来自各界的压力。\n'
						'实在是受够了啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'因为财务课是管钱的～\n'
						'所以不管是议员还是高官，\n'
						'都会给我们施加很大的压力。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呼，休息一下吧。\n'
						'偶尔也要出来透透气，不然都要窒息了。{wait}'
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
		(Expr([Insn('FLAG', Flag(631)), Insn('NOT'), Insn('FLAG', Flag(768)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F弗兰兹？\n'
				'好久不见了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'#14502F噢噢……这不是罗伊德嘛！\n'
				'从警察学校毕业之后，\n'
				'都已经过去一个月了呢。{wait}'
				'{page}'
				'#14500F对了，说起来，罗伊德，\n'
				'你好像取得了搜查官资格吧。{wait}'
				'{page}'
				'#14509F他们把你分配到哪里了？\n'
				'肯定是\n'
				'某个搜查课吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0006F哎？那个……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(254), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(254), Text(
				'#14505F什么嘛，怎么吞吞吐吐的……{wait}'
				'{page}'
				'#14502F算啦，反正我也打算\n'
				'考取搜查官资格呢。{wait}'
				'{page}'
				'#14509F要是在念书上遇到什么不明白的地方，\n'
				'就麻烦你多多指教吧！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F啊，好的，这个当然没问题。\n'
				'（……有空时也要向弗兰兹\n'
				'\u3000好好说明一下呢。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(631)),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(536)), Insn('END')]), [
					Insn('FLAG_SET', Flag(10)),
				]),
				(None, []),
			]),
			Insn('TEXT_END', Char(254)),
			Insn('RETURN'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14501F机场那边好像发生了什么事呢。\n'
						'市内的制服警察也要多加注意，\n'
						'……收到了这样的指示。{wait}'
						'{page}'
						'#14505F不过，到底要注意些什么啊？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14505F今天的指示怎么这么含糊不清，\n'
						'……这真的是课长下达的指示吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14502F哎呀，是罗伊德啊。{wait}'
						'{page}'
						'#14500F其实……这次的搜查官考试，\n'
						'我准备去参加了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F噢，弗兰兹……\n'
						'你终于决定了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#14504F哈哈……虽然觉得自己所学还远远不够。\n'
						'实践暂且不说，我实在是很怕念书。{wait}'
						'{page}'
						'#14500F可我觉得，只要去尝试一次，\n'
						'就总能慢慢找到感觉的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(254), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(254), Text(
						'#14501F问题是……最近强化了巡逻工作，\n'
						'实在是挤不出学习的时间呢。\n'
						'这段时间，突发事件实在是太多了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14501F课长最近下达了指示，\n'
						'要对市内巡逻工作进行强化。{wait}'
						'{page}'
						'#14506F呵呵……实在是越来越难腾出\n'
						'时间来学习了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1414)), Insn('NOT'), Insn('END')]), [
					Insn('EMOTE', Char(254), 0, 2000, (38, 38, 250, 1)),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(254), Text(
						'#14505F罗伊德……？{wait}'
						'{page}'
						'#14509F这不是罗伊德嘛！\n'
						'你没事吗！{wait}'
						'{page}'
						'#14500F听说你被鲁巴彻的人给盯上了，\n'
						'我还在想，你这次又惹了什么麻烦呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F哈哈……消息\n'
						'果然都已经传开了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#14503F本来只是署内的秘密呢。{wait}'
						'{page}'
						'#14502F哈，听说你们已经达成了和解协定，\n'
						'我总算能放下心啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1414)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14503F署内流传着各式各样的传闻呢。{wait}'
						'{page}'
						'#14502F算了，听说你们已经达成了和解协定，\n'
						'我也可以暂时把心放下了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_ROTATE', Char(254), 180, 0),
					Insn('TEXT_TALK', Char(254), Text(
						'#14503F嗯嗯，搜查官的七种道具\n'
						'的使用方法是……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(254), Char(0), 500),
					Insn('TEXT_TALK', Char(254), Text(
						'#14505F啊，不好意思，\n'
						'我正在背搜查官考试的题目呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F弗兰兹，你也很努力啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#14509F哈哈，你们正在调查案件吗？\n'
						'执行任务辛苦啦！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14503F听说搜查课的人\n'
						'最近好像很忙呢。{wait}'
						'{page}'
						'#14500F……我也要继续努力，\n'
						'希望能早日取得搜查官的资格。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14500F达德利警官可是\n'
						'搜查一课的希望之星呢。{wait}'
						'{page}'
						'#14510F不仅在年轻警官之中出类拔萃，\n'
						'连资深搜查官们也都对他青睐有加。\n'
						'真是很令人憧憬呢。{wait}'
						'{page}'
						'#14506F……虽然是个有些难接近的人。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14506F达德利警官虽然很能干，\n'
						'但却稍微有些难以亲近。{wait}'
						'{page}'
						'#14503F只是和他走个形式地寒暄一下，\n'
						'对我来说就已经很累了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14503F当了警官之后，最难承受的\n'
						'就是市民们的投诉与抱怨啊。{wait}'
						'{page}'
						'#14501F即使认真尽责地努力工作，\n'
						'也难免会有犯罪现象发生……{wait}'
						'{page}'
						'#14506F虽然很想好好保护市民，\n'
						'但总会遇到很多让人束手无策的情况啊。\n'
						'呼，真是伤心呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14501F即使是警官，也会受到\n'
						'多种制约呢。{wait}'
						'{page}'
						'#14506F有很多事情，仅凭正义感根本就\n'
						'无法解决，真是让人痛苦啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1161)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14502F哎呀，这不是罗伊德和大家嘛。\n'
						'工作辛苦了！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F弗兰兹，最近怎么样啊？\n'
						'你之前说过，很难挤出\n'
						'时间来学习吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#14509F哈哈，是说搜查官考试吗？{wait}'
						'{page}'
						'#14500F如你所见，现在还是要以\n'
						'平时的值勤任务为重。{wait}'
						'{page}'
						'#14504F当然了，考取搜查官资格\n'
						'这个目标我也不会放弃的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F那实在是很辛苦呢……\n'
						'可不要太过勉强啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#14509F放心好啦。\n'
						'……罗伊德，倒是你，\n'
						'可要好好努力啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1161)),
				]),
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14500F对了，罗伊德……\n'
						'你们好像经常和那位接待员聊天啊。{wait}'
						'{page}'
						'#14504F好像是位叫……瑞贝卡的小姐……\n'
						'真是个大美人呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(254), 0, 2000, (40, 43, 100, 3)),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(254), Text(
						'#14505F啊，别误会啦，\n'
						'我没有其它意思！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14504F接待员瑞贝卡小姐…\n'
						'真是个大美人啊……{wait}'
						'{page}'
						'#14505F芙兰小姐虽然也很可爱，\n'
						'但我果然还是只对瑞贝卡小姐……\n'
						'……唔，不说这些奇怪的话题啦！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14502F大家执行任务辛苦了！{wait}'
						'{page}'
						'#14506F就在刚才，搜查一课的人\n'
						'出门了呢。\n'
						'呼，好紧张啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14502F搜查一课的人\n'
						'果然很帅啊。\n'
						'个个都是出类拔萃的搜查官。{wait}'
						'{page}'
						'#14510F……我也想早日考取到\n'
						'搜查官资格啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14500F在市内的巡逻任务中，我选择\n'
						'在这个地方进行警备。{wait}'
						'{page}'
						'#14504F虽然看起来只是很不起眼的工作，\n'
						'但这里也有很多搜查官来来往往呢。{wait}'
						'{page}'
						'#14502F我的目标就是成为一名搜查官……\n'
						'在这里工作的话，能得到很多参考信息吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14504F只要待在这个地方，就可以看到\n'
						'那些搜查官是如何处理工作的。{wait}'
						'{page}'
						'#14509F嗯～我实在是很憧憬\n'
						'搜查官这个职业呢！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(10)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14502F（话说回来……那两个人\n'
						'\u3000好像是搜查一课的人啊！）{wait}'
						'{page}'
						'#14506F（仅、仅从外表上看，\n'
						'\u3000就有种非常优秀的感觉呢。\n'
						'\u3000光是靠近他们就觉得很紧张呢……）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(536)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14502F（……那两个人…\n'
						'\u3000好像是搜查一课的人啊！）{wait}'
						'{page}'
						'#14506F（仅、仅从外表上看，\n'
						'\u3000就有种非常优秀的感觉呢。\n'
						'\u3000光是靠近他们就觉得很紧张呢……）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14502F大家执行任务辛苦了！{wait}'
						'{page}'
						'#14506F……今天是我第一次工作。\n'
						'呼，好紧张啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14504F不管怎么说，这也是为了\n'
						'以后能成为一名搜查官……{wait}'
						'{page}'
						'#14500F不管是什么样的工作，\n'
						'都不能马虎大意。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'#14500F我的目标是加入搜查一课，\n'
				'所以打算考取搜查官资格。{wait}'
				'{page}'
				'#14504F搜查一课果然是\n'
				'大家憧憬的对象啊～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((0, 11))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'#0603F哼……\n'
				'和你们没有关系。{wait}'
				'{page}'
				'#0600F赶快从我眼前消失。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('0x4B', Char(12), -1),
	Insn('0x4B', Char(13), -1),
	Insn('CHAR_ROTATE', Char(12), 270, 0),
	Insn('CHAR_ROTATE', Char(13), 90, 0),
	Insn('TEXT_TALK', Char(12), Text(
		'#0603F嗯，我接下来就会询问\n'
		'共和国那边的人。{wait}'
		'{page}'
		'#0603F艾玛，那方面的调查就拜托你了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'嗯，我马上就会\n'
		'同Ｋ监视班会合。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(12), -1),
	Insn('0x4C', Char(13), -1),
	Insn('FLAG_SET', Flag(3)),
	Insn('FLAG_SET', Flag(4)),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((0, 11))),
		]),
		(None, [
			Insn('EMOTE', Char(254), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(254), Text(
				'特务支援课……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……请不要妨碍我们的调查工作。\n'
				'因为你们只不过是没用的累赘而已。{wait}'
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
				'#0006F（好像被他说得相当不堪呢……）{wait}'
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
		'啊，早安啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'今天的天气也不错呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'我今天也要和妈妈\n'
		'一起去图书馆～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天要处理暴力事件和肇事逃逸犯，\n'
				'然后就是交易诈骗那边的调查了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'要是不赶快搞定，\n'
				'太阳都该下山了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F搜查二课好像也很忙呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……（啪啪）…………\n'
						'你们的案子好像被一课给强行接管了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……算了，这也没办法啊。{wait}'
					)),
					Insn('TEXT_TALK', Char(254), Text(
						'能在一课的管理范围内\n'
						'掺上一脚，就已经\n'
						'很不错了，不是吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0012F哈哈……果然是\n'
						'那个道理吗。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，该说真不愧是\n'
						'赛尔盖的部下吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'算了，总之，尽量不要被人盯上啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'如果你们的行为太过惹眼，\n'
						'可就要做好心理准备，随时遭受\n'
						'副局长那类人的刁难了。{wait}'
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
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F那个……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0306F唉，饶了我吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'竟然能在一课的地盘中\n'
						'掺上一脚……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'赛尔盖的部下吗……\n'
						'呵呵，说不定你们也算是\n'
						'继承了那家伙的某些特点呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F……？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'算了，总之，一定注意不要\n'
						'显眼到被副局长盯上了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……（啪啪）…………\n'
						'话说回来，雷蒙德那家伙\n'
						'怎么磨磨蹭蹭的？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'再这么磨蹭下去，去询问案情之前，\n'
						'我都已经要把香烟抽完了。{wait}'
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
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'真想在纪念庆典的时候\n'
				'和恋人一起出去玩啊～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'比如说，到米修拉姆\n'
				'度过一个愉快的假期～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……算了，根本就不可能的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(8)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵……\n'
				'我们搜查官，在纪念庆典时期\n'
				'是不可能放假的～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (7330, 3500, -6700), 0),
	Insn('CAM_ROTATE', 44, 25, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 17970, 0),
	Insn('CHAR_SET_POS', Char(257), (6820, 2390, -5850), 270),
	Insn('CHAR_SET_POS', Char(339), (8100, 2390, -5930), 225),
	Insn('FORK_FUNC', Char(257), 1, Function((0, 18))),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(258), (8160, 2390, -7190), 180),
			Insn('FORK_FUNC', Char(258), 1, Function((0, 19))),
			Insn('SLEEP', 2000),
			Insn('FORK_QUIT', Char(258), 1),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(259), (8160, 2390, -7190), 180),
			Insn('FORK_FUNC', Char(259), 1, Function((0, 19))),
			Insn('SLEEP', 2000),
			Insn('FORK_QUIT', Char(259), 1),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(260), (8160, 2390, -7190), 180),
			Insn('FORK_FUNC', Char(260), 1, Function((0, 19))),
			Insn('SLEEP', 2000),
			Insn('FORK_QUIT', Char(260), 1),
		]),
		(None, []),
	]),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0005F哎……好奇怪啊。{wait}'
		'{page}'
		'喷泉广场的果汁店，\n'
		'应该就在这一带吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_WATCH', Char(258), Char(257), 500),
			Insn('TEXT_TALK', Char(258), Text(
				'#12P#0105F嗯，我觉得也是……{wait}'
				'{page}'
				'#0103F不过，莫非是\n'
				'搬到别处去了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_WATCH', Char(259), Char(257), 500),
			Insn('TEXT_TALK', Char(259), Text(
				'#12P#0203F嗯，我记得也是如此。{wait}'
				'{page}'
				'#0200F很可能是搬到\n'
				'其它地方了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_WATCH', Char(260), Char(257), 500),
			Insn('TEXT_TALK', Char(260), Text(
				'#12P#0303F是啊，我之前约会时来过那家店，\n'
				'不会有错的。{wait}'
				'{page}'
				'#0301F大概已经搬到其它什么地方了吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_WATCH', Char(339), Char(257), 500),
	Insn('TEXT_TALK', Char(339), Text(
		'#11P#1112F哎～那么，\n'
		'我们就不能给老爷爷\n'
		'买慰问品了吗～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(339), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0003F不，应该还没有\n'
		'搬到市外……{wait}'
		'{page}'
		'#0000F既然都已经接下了委托，\n'
		'就在市内好好找找吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#11P#1100F嗯！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('CHAR_SET_POS', Char(0), (8100, 2390, -5930), 225),
	Insn('QUEST', 38, Insn('TASK_SET', 2)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_ROTATE', Char(254), 0, 550),
		Insn('SLEEP', 500),
		Insn('CHAR_ROTATE', Char(254), 270, 550),
		Insn('SLEEP', 500),
	]),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_ROTATE', Char(254), 180, 600),
		Insn('SLEEP', 500),
		Insn('CHAR_ROTATE', Char(254), 90, 600),
		Insn('SLEEP', 500),
	]),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x0A', 268435456),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CAM_OFFSET', (-18580, 4730, 27420), 0),
	Insn('CAM_ROTATE', 46, 17, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 17500, 0),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (9150, 6030, 14130), 5000),
	Insn('CAM_ROTATE', 46, 11, 0, 5000),
	Insn('0x6E', 700, 5000),
	Insn('CAM_DISTANCE', 20160, 5000),
	Insn('0x6F', b'y'),
	Insn('SLEEP', 1000),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (24420, 6330, -12770), 0),
	Insn('CAM_ROTATE', 71, 22, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 16379, 0),
	Insn('CHAR_FLAG1_SET', Char(8), 32768),
	Insn('CAM_OFFSET', (-12250, 5080, -8260), 7000),
	Insn('CAM_ROTATE', 45, 4, 0, 7000),
	Insn('0x6E', 700, 7000),
	Insn('CAM_DISTANCE', 19000, 7000),
	Insn('0xCB', b'T\x01(\x00', 'c_plac05', b'\x00p\x17'),
	Insn('0x6F', b'y'),
	Insn('SLEEP', 3000),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'#0103F克洛斯贝尔市政厅，\n'
		'还有警察局总部、市立图书馆……{wait}'
		'{page}'
		'#0100F真不愧是市政机构\n'
		'集中的政务区啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#0202F真是个安静闲适的地方呢。\n'
		'连喷泉和长椅都有。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(258), Text(
		'#0104F在整个城市里，这里也算是黄金地段了……\n'
		'平时的氛围倒是一直十分宁静。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#0000F嗯，警察局总部就在这里，\n'
		'我想，今后大概也会多次来访吧。{wait}'
		'{page}'
		'从支援课到这里的具体路线，\n'
		'一定要仔细记清楚。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(260), Text(
		'#0304F了解，队长。{wait}'
		'{page}'
		'#0300F总部不是还向我们发了个\n'
		'『支援请求』，呼叫我们过去吗？\n'
		'就顺路去看看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}行政区是位于城市北侧的政务机关集中区域。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}一些重要的设施与警察局总部都在此地，\n'
		'今后应该有机会多次来访吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}除了克洛斯贝尔市政厅之外，\n'
		'市立图书馆也坐落在此区域，在馆内可阅览\n'
		'介绍了游戏世界观的用语辞典。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('CHAR_FLAG1_UNSET', Char(8), 32768),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 100), Insn('EQ'), Insn('END')]), [
			Insn('CAM_OFFSET', (19940, 2240, -37920), 0),
			Insn('CAM_ROTATE', 45, 17, 0, 0),
			Insn('0x6E', 700, 0),
			Insn('CAM_DISTANCE', 17500, 0),
		]),
		(Expr([Insn('ATTR', 0), Insn('CONST', 102), Insn('EQ'), Insn('END')]), [
			Insn('CAM_OFFSET', (-40390, 2240, 24150), 0),
			Insn('CAM_ROTATE', 45, 17, 0, 0),
			Insn('0x6E', 700, 0),
			Insn('CAM_DISTANCE', 17500, 0),
		]),
		(None, []),
	]),
	Insn('FLAG_SET', Flag(555)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (-7500, 3600, 25000), 0),
	Insn('CAM_ROTATE', 65, 17, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 16000, 0),
	Insn('CHAR_SET_POS', Char(257), (-5500, 2500, 25000), 270),
	Insn('EXPR_CHAR_ATTR', Char(257), 36, Expr([Insn('CONST', 173), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(11), 8),
	Insn('OBJ_FLAG_UNSET', Object(1), 16),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-18500, 2500, 25000), 2000, 0),
	]),
	Insn('CAM_OFFSET', (-18500, 3600, 25000), 7000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('CHAR_ROTATE', Char(257), 0, 500),
	Insn('SLEEP', 500),
	Insn('CAM_OFFSET', (-18500, 4300, 27000), 2500),
	Insn('CAM_ROTATE', 44, 3, 0, 2500),
	Insn('0x6F', b'A'),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-18500, 2500, 28400), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x71', Object(1), b'\x00\x00', 10, 0),
	Insn('0x79', b'\x01\x00'),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-18500, 3100, 31400), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('EXPR_CHAR_ATTR', Char(257), 36, Expr([Insn('CONST', 176), Insn('SET'), Insn('END')])),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('FLAG_UNSET', Flag(9)),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'c1150', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (-18000, 5000, 30500), 0),
	Insn('CAM_ROTATE', 40, 22, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 27500, 0),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('OBJ_FLAG_SET', Object(6), 4),
	Insn('CAM_ROTATE', 0, 10, 0, 7000),
	Insn('CAM_DISTANCE', 17500, 7000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SLEEP', 4000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('FLAG_UNSET', Flag(9)),
	Insn('FLAG_SET', Flag(737)),
	Insn('NEW_SCENE', 'c1160', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00501', 30),
	Insn('LOAD_CHCP', 'apl/ch50220', 31),
	Insn('EFF_LOAD', ResId(0), 'event\\eva04_00.eff'),
	Insn('CHAR_FLAG1_SET', Char(257), 8),
	Insn('CHAR_FLAG1_SET', Char(258), 8),
	Insn('CHAR_FLAG1_SET', Char(259), 8),
	Insn('CHAR_FLAG1_SET', Char(260), 8),
	Insn('CHAR_SET_CHCP', Char(18), 30),
	Insn('CHAR_SET_FRAME', Char(18), 0),
	Insn('CHAR_FLAG1_UNSET', Char(18), 128),
	Insn('CHAR_FLAG2_UNSET', Char(18), 32768),
	Insn('CHAR_FLAG1_SET', Char(18), 32768),
	Insn('CHAR_SET_POS', Char(18), (33000, 12200, 6000), 270),
	Insn('CHAR_SET_POS', Char(18), (33000, 12200, 6000), 270),
	Insn('OBJ_FLAG_SET', Object(2), 4096),
	Insn('CAM_OFFSET', (15000, 11200, 20000), 0),
	Insn('CAM_ROTATE', 55, 0, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 45000, 0),
	Insn('CAM_ROTATE', 35, 0, 0, 7500),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('SLEEP', 500),
	Insn('EXPR_CHAR_ATTR', Char(18), 40, Expr([Insn('CONST', 13), Insn('SET'), Insn('END')])),
	Insn('0x83', b'\x00\x12\x00\x1e\x00,\x01'),
	Insn('CHAR_SET_CHCP', Char(18), 31),
	Insn('CHAR_SET_FRAME', Char(18), 0),
	Insn('FORK', 18, 1, [
		Insn('0x9D', Char(254), 25000, 15200, 6000, 4000, 3000),
	]),
	Insn('SOUND_PLAY', 814, 0, 0, 70),
	Insn('FORK_AWAIT', Char(18), 1),
	Insn('CHAR_SET_FRAME', Char(18), 1),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_CHCP', Char(18), 30),
	Insn('CHAR_SET_FRAME', Char(18), 0),
	Insn('FORK', 18, 1, [
		Insn('0x95', Char(254), (25000, 15200, 19900), 8000, 0),
	]),
	Insn('FORK_AWAIT', Char(18), 1),
	Insn('CHAR_SET_CHCP', Char(18), 31),
	Insn('CHAR_SET_FRAME', Char(18), 1),
	Insn('SLEEP', 50),
	Insn('CHAR_ROTATE', Char(18), 315, 0),
	Insn('CHAR_SET_FRAME', Char(18), 0),
	Insn('FORK', 18, 1, [
		Insn('0x9D', Char(254), 20000, 16500, 24900, 2300, 3000),
	]),
	Insn('SOUND_PLAY', 814, 0, 0, 70),
	Insn('FORK_AWAIT', Char(18), 1),
	Insn('CHAR_SET_FRAME', Char(18), 1),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(18), 0),
	Insn('FORK', 18, 1, [
		Insn('0x9D', Char(254), 15000, 15200, 29900, 1300, 3000),
	]),
	Insn('SOUND_PLAY', 814, 0, 0, 70),
	Insn('FORK_AWAIT', Char(18), 1),
	Insn('CHAR_SET_FRAME', Char(18), 1),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_CHCP', Char(18), 30),
	Insn('CHAR_SET_FRAME', Char(18), 0),
	Insn('FORK', 18, 1, [
		Insn('0x95', Char(254), (2500, 15200, 29900), 8000, 0),
	]),
	Insn('FORK_AWAIT', Char(18), 1),
	Insn('CHAR_SET_CHCP', Char(18), 31),
	Insn('CHAR_SET_FRAME', Char(18), 1),
	Insn('SLEEP', 50),
	Insn('CHAR_FLAG1_UNSET', Char(18), 1),
	Insn('CHAR_SET_FRAME', Char(18), 0),
	Insn('FORK', 18, 1, [
		Insn('0x9D', Char(254), -500, 17000, 29900, 2300, 3000),
	]),
	Insn('SOUND_PLAY', 814, 0, 0, 70),
	Insn('FORK_AWAIT', Char(18), 1),
	Insn('FORK', 18, 1, [
		Insn('0x9D', Char(254), -10500, 17000, 29900, 1500, 3000),
	]),
	Insn('SOUND_PLAY', 814, 0, 0, 70),
	Insn('FORK_AWAIT', Char(18), 1),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-25800, 14500, 37000), 0),
	Insn('CAM_ROTATE', 35, 25, 0, 0),
	Insn('0x6E', 650, 0),
	Insn('CAM_DISTANCE', 17500, 0),
	Insn('CAM_OFFSET', (-40700, 10500, 37000), 2000),
	Insn('CAM_ROTATE', 50, 20, 0, 2000),
	Insn('CHAR_SET_POS', Char(18), (-15800, 15500, 37000), 270),
	Insn('CHAR_FLAG1_SET', Char(18), 1),
	Insn('EXPR_CHAR_ATTR', Char(18), 40, Expr([Insn('CONST', 13), Insn('SET'), Insn('END')])),
	Insn('CHAR_SET_FRAME', Char(18), 0),
	Insn('FORK', 18, 1, [
		Insn('0x9D', Char(254), -25800, 13500, 37000, 700, 3000),
	]),
	Insn('SOUND_PLAY', 814, 0, 0, 100),
	Insn('FORK_AWAIT', Char(18), 1),
	Insn('EFF_PLAY', (ResId(0), -1), Char(18), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('CHAR_SET_FRAME', Char(18), 1),
	Insn('SOUND_PLAY', 31, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(18), 0),
	Insn('FORK', 18, 1, [
		Insn('0x9D', Char(254), -33100, 9500, 37000, 700, 3000),
	]),
	Insn('SOUND_PLAY', 854, 0, 0, 100),
	Insn('FORK_AWAIT', Char(18), 1),
	Insn('EFF_PLAY', (ResId(0), -1), Char(18), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('CHAR_SET_FRAME', Char(18), 1),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_CHCP', Char(18), 30),
	Insn('CHAR_SET_FRAME', Char(18), 0),
	Insn('SOUND_PLAY', 31, 0, 0, 100),
	Insn('SOUND_PLAY', 42, 0, 0, 100),
	Insn('FORK', 18, 1, [
		Insn('0x95', Char(254), (-41700, 9500, 37000), 8000, 0),
	]),
	Insn('FORK_AWAIT', Char(18), 1),
	Insn('CHAR_SET_CHCP', Char(18), 31),
	Insn('CHAR_SET_FRAME', Char(18), 1),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(18), 0),
	Insn('FORK', 18, 1, [
		Insn('0x9D', Char(254), -51700, 9500, 37000, 1900, 3000),
	]),
	Insn('SOUND_PLAY', 854, 0, 0, 100),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(18), 1),
	Insn('CHAR_FLAG1_UNSET', Char(257), 8),
	Insn('CHAR_FLAG1_UNSET', Char(258), 8),
	Insn('CHAR_FLAG1_UNSET', Char(259), 8),
	Insn('CHAR_FLAG1_UNSET', Char(260), 8),
	Insn('FLAG_SET', Flag(737)),
	Insn('NEW_SCENE', 'c0400', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}\u3000\u3000※\u3000新市政厅大楼建设中\u3000※\n'
		'除工程相关人员之外，一律禁止进入。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]
