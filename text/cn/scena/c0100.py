# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'c0100',
	'name2': 'c0100',
	'location': 4,
	'bgm': 100,
	'flags': 8192,
	'includes': [
		'c0100',
		'c0100_1',
		't1500_1',
		None,
		None,
		None,
	],
	'name3': 'c0100',
	'labels': [
		{
			'pos': (-5.449999809265137, 0.0, -2.7200000286102295),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('中央广场'),
		},
		{
			'pos': (-70.54000091552734, 0.0, 1.7300000190734863),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('西侧大道'),
		},
		{
			'pos': (21.290000915527344, 0.0, 85.38999938964844),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('行政区'),
		},
		{
			'pos': (-130.92999267578125, 0.0, 75.48999786376953),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('住宅区'),
		},
		{
			'pos': (-58.65999984741211, 0.0, 67.56999969482422),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('欢乐街'),
		},
		{
			'pos': (74.98999786376953, 0.0, -25.489999771118164),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('东侧大道'),
		},
		{
			'pos': (110.13999938964844, 0.0, -79.94000244140625),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('旧市街'),
		},
		{
			'pos': (102.70999908447266, 0.0, 39.849998474121094),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('港湾区'),
		},
		{
			'pos': (76.97000122070312, 0.0, 132.91000366210938),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('ＩＢＣ'),
		},
		{
			'pos': (5.690000057220459, 0.0, -71.02999877929688),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('站前大道'),
		},
		{
			'pos': (-40.84000015258789, 0.0, 31.93000030517578),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('小巷'),
		},
		{
			'pos': (2.7200000286102295, 0.0, -101.72000122070312),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('乌尔斯拉小径'),
		},
		{
			'pos': (128.4499969482422, 0.0, -11.630000114440918),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('东克洛斯贝尔街道'),
		},
		{
			'pos': (-121.02999877929688, 0.0, 0.25),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('西克洛斯贝尔街道'),
		},
		{
			'pos': (-115.08999633789062, 0.0, 99.25),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('玛因兹山道'),
		},
		{
			'pos': (-27.229999542236328, 0.0, -16.579999923706055),
			'unk': b'\x00\x00Q\x00',
			'name': Translate(''),
		},
		{
			'pos': (25.989999771118164, 0.0, 9.15999984741211),
			'unk': b'\x00\x00T\x00',
			'name': Translate(''),
		},
		{
			'pos': (-2.9700000286102295, 0.0, -24.5),
			'unk': b'\x00\x00W\x00',
			'name': Translate(''),
		},
		{
			'pos': (-27.969999313354492, 0.0, 12.130000114440918),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-7.670000076293945, 0.0, 35.88999938964844),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-57.91999816894531, 0.0, 7.179999828338623),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-67.56999969482422, 0.0, 27.969999313354492),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-43.810001373291016, 0.0, 59.650001525878906),
			'unk': b'\x00\x00R\x00',
			'name': Translate(''),
		},
		{
			'pos': (-39.11000061035156, 0.0, 46.779998779296875),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-30.440000534057617, 0.0, 38.36000061035156),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-2.2300000190734863, 0.0, 108.6500015258789),
			'unk': b'\x00\x00Q\x00',
			'name': Translate(''),
		},
		{
			'pos': (108.6500015258789, 0.0, -25.489999771118164),
			'unk': b'\x00\x00R\x00',
			'name': Translate(''),
		},
		{
			'pos': (91.81999969482422, 0.0, -115.08999633789062),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (78.94999694824219, 0.0, -96.7699966430664),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (5.690000057220459, 0.0, -14.600000381469727),
			'unk': b'\x00\x00V\x00',
			'name': Translate(''),
		},
	],
	'chcp': [
		'chr/ch21300',
		'chr/ch20002',
		'chr/ch20200',
		'chr/ch20700',
		'chr/ch20400',
		'chr/ch22100',
		'chr/ch28100',
		'chr/ch24900',
		'chr/ch21800',
		'chr/ch20600',
		'chr/ch21200',
		'chr/ch20800',
		'chr/ch20100',
		'chr/ch21900',
		'chr/ch27800',
		'chr/ch20500',
		'chr/ch26000',
		'chr/ch20900',
		'chr/ch39200',
		'chr/ch02708',
		'chr/ch20300',
		'chr/ch08200',
		'chr/ch30600',
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
			'name': Translate('吉娜'),
			'pos': (30000, 0, -1799),
			'angle': 270,
			'_1': b'\x05\x01\x00\x00\x00\x00\x00\x01',
			'function': Function((1, 0)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('昆提老人'),
			'pos': (-6090, 150, 4449),
			'angle': 270,
			'_1': b'U\x01\x00\x00\x01\x00\xff\xff',
			'function': Function((1, 1)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('阿贝尔'),
			'pos': (-6099, 0, -9409),
			'angle': 90,
			'_1': b'\x05\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((1, 2)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('咪咪'),
			'pos': (-289, 0, -10319),
			'angle': 225,
			'_1': b'\x05\x01\x00\x00\x03\x00\x00\x02',
			'function': Function((1, 3)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('普露娜'),
			'pos': (850, 0, 17969),
			'angle': 90,
			'_1': b'\x15\x01\x00\x00\x0f\x00\x00\x00',
			'function': Function((1, 4)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('瑞娜莉'),
			'pos': (2539, 0, 17870),
			'angle': 270,
			'_1': b'\x15\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((1, 5)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('哈斯'),
			'pos': (14130, 0, 340),
			'angle': 270,
			'_1': b'\x05\x01\x00\x00\x10\x00\x00\x00',
			'function': Function((1, 6)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('阿罗纳'),
			'pos': (2650, 0, -2960),
			'angle': 315,
			'_1': b'\x85\x01\x00\x00\x14\x00\x00\x00',
			'function': Function((1, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('凯特巡警'),
			'pos': (-1210, 0, -2390),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x16\x00\x00\x00',
			'function': Function((1, 8)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('雷因兹'),
			'pos': (-16760, 29, 6889),
			'angle': 315,
			'_1': b'\x85\x01\x00\x00\x06\x00\x00\x04',
			'function': Function((1, 14)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('车１'),
			'pos': (-8010, 0, 16229),
			'angle': 225,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('柯贝'),
			'pos': (-22809, 1299, -18829),
			'angle': 180,
			'_1': b'\x05\x01\x00\x00\x12\x00\x00\x03',
			'function': Function((1, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('赛特'),
			'pos': (-25440, 1299, -17040),
			'angle': 180,
			'_1': b'\x94\x01\x00\x00\x13\x00\x00\x00',
			'function': Function((1, 12)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('琪雅'),
			'pos': (-25440, 1299, -18170),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x15\x00\x00\x00',
			'function': Function((1, 13)),
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
			'name': Translate('车１'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('车２'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
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
			'name': Translate('赛尔盖课长'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('阿奈斯特秘书'),
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
			'name': Translate('事件用ＮＰＣ'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('事件用ＮＰＣ'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('事件用ＮＰＣ'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('事件用ＮＰＣ'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('事件用ＮＰＣ'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\x00\x00',
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
			'pos': (-19.200000762939453, -23.0, -9.199999809265137),
			'range': 625.0,
			'transform': [
				0.07071065902709961,
				0.14142140746116638,
				-0.0,
				0.0,
				-0.07071070373058319,
				0.14142131805419922,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				-0.2687014639377594,
				5.967981338500977,
				1.840000033378601,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 29)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (0.0, -17.0, -1.0),
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
				-0.0,
				3.4000000953674316,
				0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 32)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (0.0, -17.0, -1.0),
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
				-0.0,
				3.4000000953674316,
				0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x01',
			'function': Function((0, 15)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (-5.900000095367432, -17.1299991607666, -3.2799999713897705),
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
				1.9666666984558105,
				3.425999879837036,
				0.656000018119812,
				1.0,
			],
			'_1': b'\x00\x00\x01',
			'function': Function((0, 16)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (1740, -950, 3070),
			'range': 1100,
			'bubble_pos': (1740, 550, 3070),
			'_1': b'|\x00\x00',
			'function': Function((0, 7)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-290, -1000, 4400),
			'range': 600,
			'bubble_pos': (-290, -1000, 4400),
			'_1': b'|\x00\x00',
			'function': Function((0, 9)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-270, 0, -980),
			'range': 800,
			'bubble_pos': (130, 1500, -10),
			'_1': b'|\x00\x00',
			'function': Function((0, 8)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (4090, 0, -16900),
			'range': 1200,
			'bubble_pos': (4090, 2000, -16900),
			'_1': b'|\x00\x00',
			'function': Function((0, 12)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01L\x04\x00\x00\x00\x00\x00\x00T\xf2\xff\xff\x00\x00\x00\x00\x01\x00\x04\x00', Function((0, 5)), Function((0, 6))),
	'code': [None]*57,
	'anim': [
		{
			'speed': 1000,
			'_': 0,
			'count': 8,
			'frames': [
				0,
				1,
				2,
				1,
				0,
				3,
				4,
				3,
			],
		},
		{
			'speed': 5000,
			'_': 0,
			'count': 8,
			'frames': [
				0,
				1,
				2,
				1,
				0,
				3,
				4,
				3,
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
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('0x95', Char(254), (11850, 0, -1800), 2000, 0),
		Insn('0x95', Char(254), (11850, 0, 39440), 2000, 0),
		Insn('SLEEP', 2000),
		Insn('CHAR_SET_POS', Char(254), (30000, 0, -3010), 270),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (870, -7530), (-3530, -11930), 1000),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (-23420, -19640), (-22750, -17990), 1000),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (-16850, 8580), (-19570, 4180), 1000),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 112), Insn('EQ'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('0x23', 7), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (-26950, -1160, -4340), 90),
					Insn('CHAR_SET_POS', Char(1), (-26950, -1160, -4340), 90),
					Insn('CHAR_SET_POS', Char(2), (-26950, -1160, -4340), 90),
					Insn('CHAR_SET_POS', Char(3), (-26950, -1160, -4340), 90),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-26950, -1160, -4340), 90),
							Insn('CHAR_SET_POS', Char(5), (-26950, -1160, -4340), 90),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-26950, -1160, -4340), 90),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 104), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('0x23', 7), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (16840, 0, -3910), 270),
					Insn('CHAR_SET_POS', Char(1), (16840, 0, -3910), 270),
					Insn('CHAR_SET_POS', Char(2), (16840, 0, -3910), 270),
					Insn('CHAR_SET_POS', Char(3), (16840, 0, -3910), 270),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (16840, 0, -3910), 270),
							Insn('CHAR_SET_POS', Char(5), (16840, 0, -3910), 270),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (16840, 0, -3910), 270),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 101), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('0x23', 7), Insn('CONST', 4), Insn('EQ'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (11850, 0, 28440), 180),
					Insn('CHAR_SET_POS', Char(1), (11850, 0, 28440), 180),
					Insn('CHAR_SET_POS', Char(2), (11850, 0, 28440), 180),
					Insn('CHAR_SET_POS', Char(3), (11850, 0, 28440), 180),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (11850, 0, 28440), 180),
							Insn('CHAR_SET_POS', Char(5), (11850, 0, 28440), 180),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (11850, 0, 28440), 180),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 102), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('0x23', 7), Insn('CONST', 5), Insn('EQ'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (16840, 0, -3910), 270),
					Insn('CHAR_SET_POS', Char(1), (16840, 0, -3910), 270),
					Insn('CHAR_SET_POS', Char(2), (16840, 0, -3910), 270),
					Insn('CHAR_SET_POS', Char(3), (16840, 0, -3910), 270),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (16840, 0, -3910), 270),
							Insn('CHAR_SET_POS', Char(5), (16840, 0, -3910), 270),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (16840, 0, -3910), 270),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 101), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('0x23', 7), Insn('CONST', 6), Insn('EQ'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (-13380, 0, 14530), 135),
					Insn('CHAR_SET_POS', Char(1), (-13380, 0, 14530), 135),
					Insn('CHAR_SET_POS', Char(2), (-13380, 0, 14530), 135),
					Insn('CHAR_SET_POS', Char(3), (-13380, 0, 14530), 135),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-13380, 0, 14530), 135),
							Insn('CHAR_SET_POS', Char(5), (-13380, 0, 14530), 135),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-13380, 0, 14530), 135),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 103), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('0x23', 7), Insn('CONST', 7), Insn('EQ'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (-13380, 0, 14530), 135),
					Insn('CHAR_SET_POS', Char(1), (-13380, 0, 14530), 135),
					Insn('CHAR_SET_POS', Char(2), (-13380, 0, 14530), 135),
					Insn('CHAR_SET_POS', Char(3), (-13380, 0, 14530), 135),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-13380, 0, 14530), 135),
							Insn('CHAR_SET_POS', Char(5), (-13380, 0, 14530), 135),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-13380, 0, 14530), 135),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 103), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('0x23', 7), Insn('CONST', 8), Insn('EQ'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (16840, 0, -3910), 270),
					Insn('CHAR_SET_POS', Char(1), (16840, 0, -3910), 270),
					Insn('CHAR_SET_POS', Char(2), (16840, 0, -3910), 270),
					Insn('CHAR_SET_POS', Char(3), (16840, 0, -3910), 270),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (16840, 0, -3910), 270),
							Insn('CHAR_SET_POS', Char(5), (16840, 0, -3910), 270),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (16840, 0, -3910), 270),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 101), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('0x23', 7), Insn('CONST', 9), Insn('EQ'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (4040, 0, -21980), 0),
					Insn('CHAR_SET_POS', Char(1), (4040, 0, -21980), 0),
					Insn('CHAR_SET_POS', Char(2), (4040, 0, -21980), 0),
					Insn('CHAR_SET_POS', Char(3), (4040, 0, -21980), 0),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (4040, 0, -21980), 0),
							Insn('CHAR_SET_POS', Char(5), (4040, 0, -21980), 0),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (4040, 0, -21980), 0),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 100), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('0x23', 7), Insn('CONST', 10), Insn('EQ'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (-13380, 0, 14530), 135),
					Insn('CHAR_SET_POS', Char(1), (-13380, 0, 14530), 135),
					Insn('CHAR_SET_POS', Char(2), (-13380, 0, 14530), 135),
					Insn('CHAR_SET_POS', Char(3), (-13380, 0, 14530), 135),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-13380, 0, 14530), 135),
							Insn('CHAR_SET_POS', Char(5), (-13380, 0, 14530), 135),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-13380, 0, 14530), 135),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 103), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('0x23', 7), Insn('CONST', 11), Insn('EQ'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (16840, 0, -3910), 270),
					Insn('CHAR_SET_POS', Char(1), (16840, 0, -3910), 270),
					Insn('CHAR_SET_POS', Char(2), (16840, 0, -3910), 270),
					Insn('CHAR_SET_POS', Char(3), (16840, 0, -3910), 270),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (16840, 0, -3910), 270),
							Insn('CHAR_SET_POS', Char(5), (16840, 0, -3910), 270),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (16840, 0, -3910), 270),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 101), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('0xD0', 7, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1550)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(20), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 13))),
		]),
		(Expr([Insn('FLAG', Flag(737)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(737)),
		]),
		(Expr([Insn('FLAG', Flag(738)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(738)),
			Insn('EVENT', Function((0, 18))),
		]),
		(Expr([Insn('FLAG', Flag(739)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(739)),
			Insn('EVENT', Function((0, 20))),
		]),
		(Expr([Insn('FLAG', Flag(740)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(740)),
			Insn('EVENT', Function((0, 23))),
		]),
		(Expr([Insn('FLAG', Flag(741)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(741)),
			Insn('EVENT', Function((0, 25))),
		]),
		(Expr([Insn('FLAG', Flag(742)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(742)),
		]),
		(Expr([Insn('FLAG', Flag(743)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(743)),
			Insn('EVENT', Function((0, 30))),
		]),
		(Expr([Insn('FLAG', Flag(744)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(744)),
			Insn('EVENT', Function((0, 31))),
		]),
		(Expr([Insn('FLAG', Flag(745)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(745)),
			Insn('EVENT', Function((0, 33))),
		]),
		(Expr([Insn('FLAG', Flag(746)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(746)),
			Insn('EVENT', Function((0, 39))),
		]),
		(Expr([Insn('FLAG', Flag(747)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(747)),
			Insn('EVENT', Function((0, 44))),
		]),
		(Expr([Insn('FLAG', Flag(748)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(748)),
			Insn('EVENT', Function((0, 45))),
		]),
		(Expr([Insn('FLAG', Flag(749)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(749)),
			Insn('EVENT', Function((0, 46))),
		]),
		(Expr([Insn('FLAG', Flag(750)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(750)),
		]),
		(Expr([Insn('FLAG', Flag(751)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(751)),
			Insn('FLAG_SET', Flag(13)),
			Insn('EVENT', Function((0, 47))),
		]),
		(Expr([Insn('FLAG', Flag(752)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(752)),
			Insn('EVENT', Function((1, 17))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1009)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(1009)),
			Insn('0xD0', 1, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
			Insn('EVENT', Function((0, 11))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1352)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('FLAG', Flag(13)), Insn('FLAG', Flag(1792)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('EXPR_CHAR_ATTR', Char(20), 45, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(20), 46, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(20), 47, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('0x78', b'\t', Char(18)),
	Insn('0xD3', Char(18), 0, 245000, 0, 0),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1037)), Insn('FLAG', Flag(1038)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x00\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1343)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x01\x80\x00'),
		]),
		(None, []),
	]),
	Insn('0xB5', b'\x00\x02\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(548)), Insn('NOT'), Insn('END')]), [
			Insn('0xB5', b'\x01\x02\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1037)), Insn('FLAG', Flag(1038)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
			Insn('0x11', b'\xd5\x8f{', 38, 120, 0),
			Insn('OBJ_SET_FRAME', Object(255), 'sky', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'sky1', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'sd_mul', Insn('0', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
			Insn('0x11', b'\xd5\x8f{', 38, 120, 0),
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
	Insn('EXIT_SET_ENABLED', 11, 0),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(2184)), Insn('NOT'), Insn('END')]), [
			Insn('0x70', Object(10), b'\x00\x00'),
		]),
		(None, [
			Insn('0x70', Object(10), b'\x1e\x00'),
		]),
	]),
	Insn('OBJ_FLAG_SET', Object(11), 4),
	Insn('0x65', 3, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1537)), Insn('FLAG', Flag(1542)), Insn('NOT'), Insn('BOOL_AND'), Insn('0x23', 1), Insn('CONST', 1), Insn('EQ'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(11), 4),
			Insn('0x78', b'\x0b', Char(24)),
			Insn('OBJ_FLAG_SET', Object(11), 4096),
			Insn('OBJ_SET_FRAME', Object(11), 'light', Insn('0', 1)),
			Insn('CHAR_SET_POS', Char(24), (6000, 0, -16200), 0),
			Insn('0xD3', Char(24), 0, 0, 0, 0),
			Insn('0x74', Object(11), 7680),
			Insn('0x70', Object(11), b'\x00\x00'),
			Insn('0x66', 3, 1),
		]),
		(None, [
			Insn('0x16', Insn('3', b'\x1d\x01\x00')),
		]),
	]),
	Insn('0x1B', 0, Function((255, 255)), 255),
	Insn('0x1B', 1, Function((255, 255)), 255),
	Insn('0x1B', 2, Function((255, 255)), 255),
	Insn('0x1B', 3, Function((255, 255)), 255),
	Insn('0x1B', 4, Function((255, 255)), 255),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(526)), Insn('FLAG', Flag(609)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 0, Function((0, 48)), 0),
			Insn('0x1B', 1, Function((0, 49)), 0),
			Insn('0x1B', 2, Function((0, 50)), 0),
			Insn('0x1B', 3, Function((0, 51)), 0),
			Insn('0x1B', 4, Function((0, 52)), 0),
		]),
		(None, []),
	]),
	Insn('0xB5', b'\x00\x03\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(526)), Insn('FLAG', Flag(610)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x03\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1037)), Insn('FLAG', Flag(1038)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 0, Function((0, 48)), 0),
			Insn('0x1B', 1, Function((0, 49)), 0),
			Insn('0x1B', 2, Function((0, 50)), 0),
			Insn('0x1B', 4, Function((0, 52)), 0),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('0xF2', Insn('CHEST')),
	Insn('0x09', 134217728),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(2184)), Insn('NOT'), Insn('END')]), [
			Insn('SOUND_PLAY', 14, 0, 0, 100),
			Insn('0x71', Object(10), b'\x00\x00', 30, 0),
			Insn('SLEEP', 500),
			Insn('0x70', Object(10), b'\x1e\x00'),
			Insn('SOUND_PLAY', 17, 0, 0, 100),
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('SEPITH_ADD', b'\x00\x1e\x00'),
			Insn('SEPITH_ADD', b'\x01\x1e\x00'),
			Insn('SEPITH_ADD', b'\x02\x1e\x00'),
			Insn('SEPITH_ADD', b'\x03\x1e\x00'),
			Insn('SEPITH_ADD', b'\x04\x1e\x00'),
			Insn('SEPITH_ADD', b'\x05\x1e\x00'),
			Insn('SEPITH_ADD', b'\x06\x1e\x00'),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'获得了{color 2}#56I地之耀晶石×３０{color 0}\n'
				'{color 2}#57I水之耀晶石×３０{color 0}\n'
				'{color 2}#58I火之耀晶石×３０{color 0}\n'
				'{color 2}#59I风之耀晶石×３０{color 0}\n'
				'{color 2}#60I时之耀晶石×３０{color 0}\n'
				'{color 2}#61I空之耀晶石×３０{color 0}\n'
				'{color 2}#62I幻之耀晶石×３０{color 0}。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('FLAG_SET', Flag(2184)),
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

data['code'][8] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}       『克洛斯贝尔之钟』\n'
		'Ｓ１１８５\u3000在克洛斯贝尔自治州\n'
		'发掘出土的巨型大钟。\n'
		'依据出土遗迹的情况来看，\n'
		'可推断为中世纪时期的物品。\n'
		'使用多种金属打造而成，\n'
		'敲打时会发出悦耳的低音。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}据推测，是由当时的权贵人士所制造，\n'
		'但关于其具体用途，\n'
		'目前仍然诸说纷纭。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('EVENT_BEGIN', 1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}有梯子。\n'
		'要下去吗？{wait}'
	)),
	Insn('MENU', 0, -1, -1, 1, Text(
		'是\n'
		'否\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('EVENT_END', 5),
			Insn('NEW_SCENE', 'm0000', b'}\x00\x00\x07'),
		]),
		(None, [
			Insn('EVENT_END', 5),
		]),
	]),
	Insn('RETURN'),
]

data['code'][10] = [
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
					(Expr([Insn('VAR', 4), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄中央广场'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 0)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄中央广场'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄东出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 1)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄东出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄西出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 2)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄西出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 4), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄南出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 3)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄南出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 5), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄北出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 4)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄北出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 6), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★唐古拉姆门'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 5)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000唐古拉姆门'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 7), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★贝尔加德门'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 6)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000贝尔加德门'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 8), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★乌尔斯拉医科大学'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 7)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000乌尔斯拉医科大学'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 9), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★阿尔摩利卡村'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 8)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000阿尔摩利卡村'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 10), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★玛因兹矿山镇'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 9)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000玛因兹矿山镇'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 11), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★玛因兹山道丄隧道内'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 10)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000玛因兹山道丄隧道内'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 12), Insn('EQ'), Insn('END')]), [
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
						Insn('0x71', Object(11), b'\x01\x00', 30, 0),
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

data['code'][11] = [
	Insn('EVENT_BEGIN', 1),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('CHAR_SET_POS', Char(0), (2400, 0, -16530), 270),
	Insn('CHAR_SET_POS', Char(1), (2400, 0, -16530), 270),
	Insn('CHAR_SET_POS', Char(2), (2400, 0, -16530), 270),
	Insn('CHAR_SET_POS', Char(3), (2400, 0, -16530), 270),
	Insn('CHAR_SET_POS', Char(4), (2400, 0, -16530), 270),
	Insn('CHAR_SET_POS', Char(5), (2400, 0, -16530), 270),
	Insn('SLEEP', 1),
	Insn('CAM_OFFSET', (2400, 1900, -16530), 0),
	Insn('CAM_ROTATE', 45, 21, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 21500, 0),
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

data['code'][12] = [
	Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
	Insn('CALL', Function((0, 10))),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50003', 30),
	Insn('LOAD_CHCP', 'apl/ch50004', 31),
	Insn('LOAD_CHCP', 'apl/ch50005', 32),
	Insn('LOAD_CHCP', 'chr/ch20800', 33),
	Insn('LOAD_CHCP', 'chr/ch20900', 34),
	Insn('LOAD_CHCP', 'chr/ch21100', 35),
	Insn('SOUND_LOAD', 803),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis030.itp'),
	Insn('IMG_LOAD', ResId(1), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis163.itp'),
	Insn('CAM_OFFSET', (-18000, 2000, 7500), 0),
	Insn('CAM_ROTATE', 28, 9, 0, 0),
	Insn('0x6E', 820, 0),
	Insn('CAM_DISTANCE', 13000, 0),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_SET_POS', Char(257), (2900, 0, -21300), 0),
	Insn('CHAR_SET_CHCP', Char(22), 33),
	Insn('CHAR_SET_FRAME', Char(22), 0),
	Insn('CHAR_SET_CHCP', Char(23), 34),
	Insn('CHAR_SET_FRAME', Char(23), 0),
	Insn('CHAR_FLAG1_UNSET', Char(22), 128),
	Insn('CHAR_FLAG1_UNSET', Char(23), 128),
	Insn('CHAR_SET_POS', Char(22), (2600, 0, -23600), 0),
	Insn('CHAR_SET_POS', Char(23), (3700, 0, -23800), 0),
	Insn('CHAR_FLAG1_SET', Char(22), 32768),
	Insn('CHAR_FLAG1_SET', Char(23), 32768),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG1_SET', Char(14), 128),
	Insn('CHAR_FLAG1_SET', Char(15), 128),
	Insn('CHAR_FLAG1_SET', Char(16), 128),
	Insn('CHAR_FLAG1_SET', Char(17), 128),
	Insn('CHAR_FLAG1_UNSET', Char(17), 128),
	Insn('CHAR_SET_POS', Char(17), (-16700, 0, 2500), 315),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_SET_POS', Char(10), (7100, 0, -16600), 90),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_SET_POS', Char(8), (200, 0, -2300), 270),
	Insn('CHAR_SET_POS', Char(11), (-1100, 0, -2300), 90),
	Insn('CHAR_FLAG1_UNSET', Char(15), 128),
	Insn('CHAR_SET_CHCP', Char(16), 35),
	Insn('CHAR_SET_FRAME', Char(16), 0),
	Insn('CHAR_FLAG1_UNSET', Char(16), 128),
	Insn('CHAR_SET_POS', Char(15), (-6300, 0, -9200), 135),
	Insn('CHAR_SET_POS', Char(16), (-5300, 0, -10200), 315),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG1_UNSET', Char(13), 128),
	Insn('CHAR_SET_POS', Char(12), (-4300, 0, 17300), 270),
	Insn('CHAR_SET_POS', Char(13), (-6200, 0, 17300), 90),
	Insn('CHAR_FLAG1_UNSET', Char(14), 128),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_SET_POS', Char(9), (-6300, 100, 4300), 270),
	Insn('0x4B', Char(8), -1),
	Insn('FORK_FUNC', Char(8), 0, Function((0, 0))),
	Insn('0x4B', Char(11), -1),
	Insn('FORK_FUNC', Char(11), 0, Function((0, 0))),
	Insn('0x4B', Char(17), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(11), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(15), 32768),
	Insn('CHAR_FLAG1_SET', Char(16), 32768),
	Insn('CHAR_FLAG1_SET', Char(17), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 128),
	Insn('CHAR_FLAG1_UNSET', Char(25), 128),
	Insn('0x78', b'\x08', Char(24)),
	Insn('0x78', b'\t', Char(25)),
	Insn('OBJ_FLAG_SET', Object(8), 4096),
	Insn('OBJ_FLAG_SET', Object(9), 4096),
	Insn('OBJ_SET_FRAME', Object(8), 'light', Insn('0', 1)),
	Insn('OBJ_FLAG_SET', Object(8), 4),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('CHAR_FLAG1_SET', Char(25), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 4),
	Insn('CHAR_FLAG1_UNSET', Char(25), 4),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(24), (11500, 0, 19500), 0),
	Insn('0xD3', Char(24), 0, 180000, 0, 0),
	Insn('CHAR_SET_POS', Char(25), (0, 0, 14000), 0),
	Insn('0xD3', Char(25), 0, 270000, 0, 0),
	Insn('0x70', Object(9), b'\x1e\x00'),
	Insn('0xE5'),
	Insn('SOUND_PLAY', 803, 0, 2, 0),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 55))),
	Insn('CAM_OFFSET', (-17000, 2000, 7000), 9000),
	Insn('CAM_ROTATE', 18, 9, 0, 9000),
	Insn('CAM_DISTANCE', 17000, 9000),
	Insn('FORK_FUNC', Char(17), 3, Function((0, 16))),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(25), 3, Function((0, 14))),
	Insn('FORK_FUNC', Char(35), 2, Function((0, 17))),
	Insn('0x6F', b'\x01'),
	Insn('0x6F', b'@'),
	Insn('0x6F', b'\x10'),
	Insn('SLEEP', 300),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (2500, 1900, -1600), 0),
	Insn('CAM_ROTATE', 42, 5, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 27000, 0),
	Insn('OBJ_FLAG_UNSET', Object(8), 4),
	Insn('CAM_DISTANCE', 32000, 8000),
	Insn('FORK_FUNC', Char(24), 3, Function((0, 15))),
	Insn('0x6F', b'\x10'),
	Insn('CROSSFADE', 1000),
	Insn('0xCB', b'T\x01\xc8\x00', 'c_plac02', b'\x00\xdc\x05'),
	Insn('CAM_OFFSET', (0, 800, 4000), 0),
	Insn('CAM_ROTATE', 18, 22, 0, 0),
	Insn('0x6E', 860, 0),
	Insn('CAM_DISTANCE', 28000, 0),
	Insn('OBJ_FLAG_SET', Object(8), 4),
	Insn('OBJ_FLAG_SET', Object(9), 4),
	Insn('CAM_ROTATE', 42, 22, 0, 9000),
	Insn('CAM_DISTANCE', 33000, 9000),
	Insn('0x6F', b'@'),
	Insn('0x6F', b'\x10'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (3400, 800, -12300), 0),
	Insn('CAM_ROTATE', 45, 19, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 22000, 0),
	Insn('SLEEP', 1),
	Insn('CAM_DISTANCE', 19000, 5000),
	Insn('FORK_QUIT', Char(35), 1),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 56))),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (2900, 0, -11300), 2000, 0),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 22, 1, [
		Insn('0x95', Char(254), (2600, 0, -13600), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 23, 1, [
		Insn('0x95', Char(254), (3700, 0, -13800), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('CHAR_ROTATE', Char(257), 270, 500),
	Insn('SLEEP', 750),
	Insn('CHAR_ROTATE', Char(257), 80, 500),
	Insn('SLEEP', 500),
	Insn('FORK_QUIT', Char(35), 1),
	Insn('FORK_QUIT', Char(35), 2),
	Insn('0xE6'),
	Insn('SOUND_PLAY', 1080, 0, 255, 90),
	Insn('SLEEP', 1250),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100122V#0005F#5P哇……\n'
		'还真是大大变了样啊。{wait}'
		'{page}'
		'#10100123V#0012F连百货也完全\n'
		'焕然一新了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 45, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100124V#0005F#5P哎，那边的建筑物是……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#10100125V#12P那是去年才刚刚开业的\n'
		'『导力商店』哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#10100126V#12P那家店不仅经营各种最新的导力制品，\n'
		'甚至连导力车都有销售呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#10100127V#12P帝国产、共和国产、利贝尔产、\n'
		'爱普斯泰恩产……可谓一应俱全呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 0, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100128V#0006F#5P哈～那可真是不得了啊。{wait}'
		'{page}'
		'#10100129V#0000F而且……\n'
		'导力车的数量好像也明显增加了。{wait}'
		'{page}'
		'#10100130V三年前都还几乎\n'
		'见不到一辆呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#10100131V呵呵，即使是现在，那终究也只是\n'
		'有钱人专用的奢侈品啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#10100132V不过说心里话，导力巴士增加了班数，\n'
		'这倒真是一大幸事。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#10100133V像南边的医院，坐车的话\n'
		'只要三十分钟左右就能到了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100134V#0002F#5P嘿，那可真是比以前便利许多啊。{wait}'
		'{page}'
		'#10100135V#0004F是吗……\n'
		'仅仅三年，就有了如此大的变化。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#10100136V#12P那么，就在这里说再见吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#10100137V#12P你还要去就职单位报到吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 180, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100138V#0005F#5P啊，是啊……{wait}'
		'{page}'
		'#10100139V不过，难得相遇，本来还想帮二位\n'
		'把行李送到家里呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#10100140V哎呀呀，那可不行哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#10100141V第一次报到出勤，\n'
		'怎么能迟到呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#10100142V#12P没错没错。\n'
		'无论做什么，良好的开端都是最重要的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100143V#0012F#5P哈哈，确实如此呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x95', Char(257), (2700, 0, -12500), 2000, 0),
	Insn('CROSSFADE', 250),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('CHAR_SET_CHCP', Char(22), 31),
	Insn('CHAR_SET_FRAME', Char(22), 0),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('0x0D'),
	Insn('0x96', Char(257), (2900, 0, -11300), 2000, 0),
	Insn('TEXT_TALK', Char(22), Text(
		'#10100144V#12P不过，你刚刚回来，\n'
		'有住的地方吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#10100145V#12P如果愿意来东侧大道，\n'
		'我倒是能给你介绍个住宿的地方。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100146V#0002F#5P啊，多谢您的好意了，\n'
		'不过我们那里似乎会提供宿舍。{wait}'
		'{page}'
		'#10100147V托运的行李\n'
		'应该也都送到那边去了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#10100148V#12P哦，是这样啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#10100149V我们就住在东侧大道的\n'
		'出口附近。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#10100150V要是以后遇到了什么困难，\n'
		'随时都可以来找我们哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100151V#0009F#5P嗯！那就先谢谢您了。{wait}'
		'{page}'
		'#10100152V#0002F等我安顿下来之后，\n'
		'一定会去拜访两位的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#10100153V#12P唔，要保重啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(23), Text(
		'#10100154V那就在这里说再见啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x92', Char(22), 11800, -5300, 500),
	Insn('FORK', 22, 1, [
		Insn('0x95', Char(254), (11800, 0, -5300), 2200, 0),
	]),
	Insn('SLEEP', 300),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(22), 500),
	]),
	Insn('SLEEP', 200),
	Insn('0x92', Char(23), 11300, -7000, 500),
	Insn('FORK', 23, 1, [
		Insn('0x95', Char(254), (11300, 0, -7000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(22), 1),
	Insn('FORK', 22, 1, [
		Insn('0x95', Char(254), (21800, 0, -5300), 2200, 0),
	]),
	Insn('FORK_AWAIT', Char(23), 1),
	Insn('FORK', 23, 1, [
		Insn('0x95', Char(254), (21300, 0, -7000), 2000, 0),
	]),
	Insn('SLEEP', 1000),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(257), 270, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100155V#0005F#11P咦……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_SET', Char(22), 128),
	Insn('CHAR_FLAG1_SET', Char(23), 128),
	Insn('CAM_OFFSET', (-25800, -1600, -16400), 3500),
	Insn('CAM_ROTATE', 45, 14, 0, 3500),
	Insn('0x6E', 700, 3500),
	Insn('CAM_DISTANCE', 30500, 3500),
	Insn('0x6F', b'y'),
	Insn('SLEEP', 500),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#10100156V#0000F那座混居大楼……\n'
		'还完好地保留着啊。{wait}'
		'{page}'
		'#10100157V我记得克洛斯贝尔时报周刊以前\n'
		'好像就在这里……{wait}'
		'{page}'
		'#10100158V#0012F哈哈，虽然很怀念，但如此破旧的大楼\n'
		'坐落在这光鲜亮丽的街道上，看起来还真是突兀呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (3120, 800, -11310), 0),
	Insn('CAM_ROTATE', 45, 19, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 19000, 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100159V#0003F#11P那么……时间差不多也快到了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 250),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('CHAR_SET_CHCP', Char(257), 32),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('0x0D'),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}罗伊德从怀中\n'
		'取出一封书信。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('SOUND_PLAY', 18, 0, 0, 100),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), -10000, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}任命罗伊德丄班宁斯警官\n'
		'至克洛斯贝尔警察局总部的\n'
		'特务支援课就职。\n'
		'请于指定日期来警察局总部报到。\n'
		'\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000克洛斯贝尔警察局丄人事课{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#10100160V#0001F#11P特务支援课……\n'
		'在警察学校上课时从来\n'
		'没听过这个名字。{wait}'
		'{page}'
		'#10100161V连制服都还没有收到，\n'
		'到底是个怎样的部门呢……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100162V#0004F#11P──算了。\n'
		'总之去了就知道了。{wait}'
		'{page}'
		'#10100163V幸好警察局的位置应该\n'
		'没有什么变化……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 0, 500),
	Insn('SLEEP', 300),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#10100164V#0000F#11P好，这就去报到吧！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (9000, 0, 4000), 2500, 0),
	]),
	Insn('SLEEP', 2000),
	Insn('CAM_DISTANCE', 19500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('0x6F', b'\x10'),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('SLEEP', 2000),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('SOUND_STOP', 803),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'c1100', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('SLEEP', 1000),
	Insn('SOUND_PLAY', 461, 0, 0, 70),
	Insn('0x71', Object(9), b'\x1f\x00', 60, 0),
	Insn('0x79', b'\t\x00'),
	Insn('SLEEP', 1000),
	Insn('0x71', Object(9), b'<\x00', 90, 0),
	Insn('0x79', b'\t\x00'),
	Insn('FORK', 25, 2, [
		Insn('0x9E', Char(254), 0, 5000, -180000, 6000, b'\x01\x00'),
	]),
	Insn('0x71', Object(9), b'y\x00', 180, 32),
	Insn('FORK_AWAIT', Char(25), 2),
	Insn('FORK', 25, 1, [
		Insn('0x98', Char(254), (40000, 0, 0), 7000, 0),
	]),
	Insn('FORK_AWAIT', Char(25), 1),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('FORK', 24, 1, [
		Insn('0x96', Char(254), (11500, 0, 6500), 6000, 0),
	]),
	Insn('0x71', Object(8), b'y\x00', 180, 32),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('FORK_AWAIT', Char(25), 2),
	Insn('SOUND_PLAY', 458, 0, 0, 100),
	Insn('FORK', 24, 1, [
		Insn('0x9E', Char(254), 0, 6500, 90000, 6000, b'\x01\x00'),
	]),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('FORK', 24, 1, [
		Insn('0x98', Char(254), (-40000, 0, 0), 6000, 0),
	]),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('FORK', 17, 1, [
		Insn('0x95', Char(254), (-21700, 100, 7500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(17), 1),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('OBJ_FLAG_UNSET', Object(6), 16),
	Insn('0x71', Object(6), b'\x00\x00', 10, 0),
	Insn('0x79', b'\x06\x00'),
	Insn('FORK', 17, 1, [
		Insn('0x95', Char(254), (-22700, 0, 8500), 2000, 0),
	]),
	Insn('FORK', 17, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(17), 1),
	Insn('FORK_AWAIT', Char(17), 2),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('0x71', Object(6), b'\n\x00', 0, 0),
	Insn('0x79', b'\x06\x00'),
	Insn('OBJ_FLAG_SET', Object(6), 16),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('SLEEP', 4000),
	Insn('SOUND_PLAY', 457, 0, 0, 100),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch28100', 30),
	Insn('LOAD_CHCP', 'chr/ch21200', 31),
	Insn('LOAD_CHCP', 'chr/ch21400', 32),
	Insn('LOAD_CHCP', 'chr/ch20000', 33),
	Insn('LOAD_CHCP', 'chr/ch23600', 34),
	Insn('SOUND_LOAD', 803),
	Insn('CAM_OFFSET', (-1000, 2500, 11000), 0),
	Insn('CAM_ROTATE', 23, 6, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 34500, 0),
	Insn('CHAR_SET_POS', Char(0), (-19000, -4200, -11700), 0),
	Insn('CHAR_SET_POS', Char(1), (-19000, -4200, -11700), 0),
	Insn('CHAR_SET_POS', Char(2), (-19000, -4200, -11700), 0),
	Insn('CHAR_SET_POS', Char(3), (-19000, -4200, -11700), 0),
	Insn('0x7D', b'\xff\xff\xff\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xb4\xd7\xe6', 15, 130, 0),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 128),
	Insn('CHAR_FLAG2_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_SET', Char(15), 128),
	Insn('CHAR_FLAG2_SET', Char(15), 32768),
	Insn('CHAR_FLAG1_SET', Char(16), 128),
	Insn('CHAR_FLAG2_SET', Char(16), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 128),
	Insn('0x78', b'\t', Char(24)),
	Insn('OBJ_FLAG_SET', Object(9), 4096),
	Insn('OBJ_FLAG_UNSET', Object(9), 4),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 4),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(24), (15000, 0, -3000), 0),
	Insn('0xD3', Char(24), 0, 270000, 0, 0),
	Insn('0x70', Object(9), b'\x00\x00'),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('CHAR_FLAG1_SET', Char(31), 32768),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_FLAG1_SET', Char(33), 32768),
	Insn('CHAR_FLAG1_SET', Char(34), 32768),
	Insn('CHAR_SET_CHCP', Char(30), 30),
	Insn('CHAR_SET_FRAME', Char(30), 0),
	Insn('0x4B', Char(30), -1),
	Insn('CHAR_SET_POS', Char(30), (-15000, 0, -6300), 90),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('CHAR_SET_CHCP', Char(31), 31),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_SET_POS', Char(31), (-6800, 0, 4000), 270),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_CHCP', Char(32), 32),
	Insn('CHAR_SET_FRAME', Char(32), 0),
	Insn('CHAR_SET_POS', Char(32), (-8300, 0, 2500), 90),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_CHCP', Char(33), 33),
	Insn('CHAR_SET_FRAME', Char(33), 0),
	Insn('0x4B', Char(33), -1),
	Insn('CHAR_SET_POS', Char(33), (-19300, 0, 19400), 180),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_CHCP', Char(34), 34),
	Insn('CHAR_SET_FRAME', Char(34), 0),
	Insn('0x4B', Char(34), -1),
	Insn('CHAR_SET_POS', Char(34), (7000, 0, 12000), 0),
	Insn('CHAR_FLAG1_UNSET', Char(34), 128),
	Insn('CHAR_FLAG2_UNSET', Char(34), 32768),
	Insn('FORK', 30, 1, [
		Insn('0x96', Char(254), (5000, 0, -6300), 2000, 0),
	]),
	Insn('FORK', 33, 1, [
		Insn('0x98', Char(254), (10000, 0, -10000), 1500, 0),
	]),
	Insn('FORK', 34, 1, [
		Insn('0x9E', Char(254), 0, 5000, 180000, 2500, b'\x01\x00'),
	]),
	Insn('SOUND_PLAY', 458, 0, 0, 100),
	Insn('FORK', 24, 1, [
		Insn('0x96', Char(254), (-26000, 1000, -3000), 6000, 0),
	]),
	Insn('0x71', Object(9), b'y\x00', 180, 32),
	Insn('CAM_OFFSET', (-1000, 1500, 11000), 5000),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 19))),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-25800, -7600, -16800), 0),
	Insn('CAM_ROTATE', 35, 12, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('CAM_DISTANCE', 20500, 4000),
	Insn('SLEEP', 3000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('FORK_QUIT', Char(35), 1),
	Insn('SOUND_STOP', 803),
	Insn('FLAG_SET', Flag(738)),
	Insn('NEW_SCENE', 'c0110', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('SOUND_PLAY', 803, 0, 2, 100),
	Insn('SLEEP', 4000),
	Insn('SOUND_LOOP', 803, 90),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 80),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 70),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 60),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 50),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 40),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 30),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 20),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 10),
	Insn('SLEEP', 100),
	Insn('SOUND_STOP', 803),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch09300', 30),
	Insn('CAM_OFFSET', (-1000, 2500, 11000), 0),
	Insn('CAM_ROTATE', 23, 6, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 34500, 0),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(24), 128),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('OBJ_FLAG_SET', Object(8), 4096),
	Insn('OBJ_FLAG_UNSET', Object(8), 4),
	Insn('0x78', b'\x08', Char(24)),
	Insn('OBJ_SET_FRAME', Object(8), 'light', Insn('0', 1)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(24), (25000, 0, -2600), 270),
	Insn('0xD3', Char(24), 0, 270000, 0, 0),
	Insn('0x74', Object(8), 7680),
	Insn('0x71', Object(8), b'y\x00', 180, 32),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_SET', Char(31), 32768),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_FLAG1_SET', Char(33), 32768),
	Insn('CHAR_FLAG1_SET', Char(34), 32768),
	Insn('CHAR_SET_CHCP', Char(31), 3),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_SET_POS', Char(31), (-9300, 0, -7200), 0),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_CHCP', Char(32), 2),
	Insn('CHAR_SET_FRAME', Char(32), 0),
	Insn('CHAR_SET_POS', Char(32), (-9700, 0, -5500), 180),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_CHCP', Char(33), 15),
	Insn('CHAR_SET_FRAME', Char(33), 0),
	Insn('0x4B', Char(33), -1),
	Insn('CHAR_SET_POS', Char(33), (-14500, 0, -500), 90),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_CHCP', Char(34), 5),
	Insn('CHAR_SET_FRAME', Char(34), 0),
	Insn('0x4B', Char(34), -1),
	Insn('CHAR_SET_POS', Char(34), (-15500, 0, 1000), 90),
	Insn('CHAR_FLAG1_UNSET', Char(34), 128),
	Insn('CHAR_FLAG2_UNSET', Char(34), 32768),
	Insn('FORK', 33, 1, [
		Insn('0x98', Char(254), (10000, 0, 12000), 1500, 0),
	]),
	Insn('FORK', 34, 1, [
		Insn('0x98', Char(254), (10000, 0, 12000), 1500, 0),
	]),
	Insn('CAM_OFFSET', (-1000, 1500, 11000), 5000),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 19))),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('FORK', 24, 1, [
		Insn('0x96', Char(254), (0, 0, -2600), 6000, 0),
	]),
	Insn('SLEEP', 2000),
	Insn('FORK', 24, 1, [
		Insn('0x96', Char(254), (0, 0, -2600), 5000, 0),
	]),
	Insn('SLEEP', 1000),
	Insn('SOUND_PLAY', 456, 0, 0, 100),
	Insn('FORK', 24, 1, [
		Insn('0x96', Char(254), (0, 0, -2600), 4000, 0),
	]),
	Insn('SLEEP', 1000),
	Insn('FORK', 24, 1, [
		Insn('0x96', Char(254), (0, 0, -2600), 3000, 0),
	]),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('0x6F', b'y'),
	Insn('0x71', Object(8), b'[\x00', 65656, 0),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x79', b'\x08\x00'),
	Insn('CAM_OFFSET', (0, 1000, -6600), 0),
	Insn('CAM_ROTATE', 50, 19, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 19000, 0),
	Insn('CHAR_SET_POS', Char(257), (-600, 0, -7800), 0),
	Insn('CHAR_SET_POS', Char(258), (700, 0, -7800), 0),
	Insn('CHAR_SET_POS', Char(259), (-600, 0, -9100), 0),
	Insn('CHAR_SET_POS', Char(260), (700, 0, -9100), 0),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_CHCP', Char(26), 30),
	Insn('CHAR_SET_FRAME', Char(26), 0),
	Insn('CHAR_SET_POS', Char(26), (0, 0, -5500), 180),
	Insn('CHAR_FLAG1_UNSET', Char(26), 128),
	Insn('CHAR_FLAG2_UNSET', Char(26), 32768),
	Insn('CHAR_SET_POS', Char(24), (0, 0, -2600), 270),
	Insn('0xD3', Char(24), 0, 270000, 0, 0),
	Insn('CHAR_FLAG1_UNSET', Char(31), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(32), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(33), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(34), 32768),
	Insn('CHAR_FLAG1_SET', Char(31), 128),
	Insn('CHAR_FLAG2_SET', Char(31), 32768),
	Insn('CHAR_FLAG1_SET', Char(32), 128),
	Insn('CHAR_FLAG2_SET', Char(32), 32768),
	Insn('CHAR_FLAG1_SET', Char(33), 128),
	Insn('CHAR_FLAG2_SET', Char(33), 32768),
	Insn('CHAR_FLAG1_SET', Char(34), 128),
	Insn('CHAR_FLAG2_SET', Char(34), 32768),
	Insn('0x70', Object(8), b'\x1e\x00'),
	Insn('SLEEP', 500),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100721V#12P#0002F──真是非常感谢，\n'
		'还麻烦您把我们送到这里。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(26), Text(
		'#11100722V#3609F#5P哈哈，这没什么，\n'
		'不过就是顺路而已。{wait}'
		'{page}'
		'#11100723V#3600F各位，事件的调查\n'
		'还请加油。{wait}'
		'{page}'
		'#11100724V我也会声援大家的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100725V#0102F谢谢您。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100726V#12P#0202F……既然要为我们声援，那以后您如果遇到\n'
		'什么困难，请务必来支援课找我们。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100727V#0309F对对，可以的话，别去找游击士协会了。\n'
		'优先考虑我们吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 0)),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (40, 43, 100, 0)),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(260), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('SLEEP', 500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100728V#1P#0011F你、你们两个！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100729V#5P#0106F这也……说得太露骨了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100730V#0302F哈哈哈，偶尔也要\n'
		'打打广告才行嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100731V#12P#0204F业务活动可是很重要的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('TEXT_TALK', Char(26), Text(
		'#11100732V#3609F#5P哈哈，明白了。{wait}'
		'{page}'
		'#11100733V#3600F如果以后遇到了什么困难，\n'
		'我就不客气地登门拜访了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('EMOTE', Char(26), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(26), Text(
		'#11100734V#3605F#5P对了……这东西\n'
		'对各位有用处吗？{wait}'
		'{page}'
		'#11100735V#3600F哈哈，对警察来说，\n'
		'说不定没有什么用吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'收下了{item 6}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 6, 1),
	Insn('0xC7', b'\x01\x00\x10\x00\x00'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100736V#0105F这个……\n'
		'好像是市内的地图啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(26), Text(
		'#11100737V#3600F#5P这是从上个月开始，\n'
		'为游客准备的商品。\n'
		'不嫌弃的话，就请各位拿去用吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100738V#12P#0002F这个……在市内巡逻时，\n'
		'说不定真的很便利呢。{wait}'
		'{page}'
		'#11100739V#0004F哈罗德先生，非常感谢您。\n'
		'我们会善加使用的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(26), Text(
		'#11100740V#3609F#5P哈哈，请不要客气，只是一点小东西而已。{wait}'
		'{page}'
		'#11100741V#3600F那么，我就先行告辞了，\n'
		'各位，工作还请多多加油。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('0x92', Char(26), 0, -4200, 500),
	Insn('FORK', 26, 1, [
		Insn('0x95', Char(254), (0, 0, -4200), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(26), 1),
	Insn('FORK', 26, 1, [
		Insn('0x95', Char(254), (0, 0, -3300), 2000, 0),
	]),
	Insn('FORK', 26, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(26), 1),
	Insn('FORK_AWAIT', Char(26), 2),
	Insn('SOUND_PLAY', 461, 0, 0, 100),
	Insn('0x71', Object(8), b'\x1f\x00', 60, 0),
	Insn('0x79', b'\x08\x00'),
	Insn('FORK_LOOP', 257, 1, [
		Insn('CHAR_WATCH', Char(257), Char(24), 500),
	]),
	Insn('FORK_LOOP', 258, 1, [
		Insn('CHAR_WATCH', Char(258), Char(24), 500),
	]),
	Insn('FORK_LOOP', 259, 1, [
		Insn('CHAR_WATCH', Char(259), Char(24), 500),
	]),
	Insn('FORK_LOOP', 260, 1, [
		Insn('CHAR_WATCH', Char(260), Char(24), 500),
	]),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (0, 500, -2600), 0),
	Insn('CAM_ROTATE', 30, 30, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 15500, 0),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 457, 0, 0, 100),
	Insn('0x71', Object(8), b'<\x00', 90, 0),
	Insn('0x79', b'\x08\x00'),
	Insn('0x71', Object(8), b'y\x00', 180, 32),
	Insn('CAM_OFFSET', (-10000, 500, -2600), 3000),
	Insn('CAM_DISTANCE', 18500, 3000),
	Insn('CAM_ROTATE', 0, 30, 0, 3000),
	Insn('FORK', 24, 1, [
		Insn('0x98', Char(254), (-25000, 0, 0), 5000, 0),
	]),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('0x6F', b'\x11'),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(259), 1),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('CHAR_FLAG1_SET', Char(26), 128),
	Insn('CHAR_FLAG1_SET', Char(24), 128),
	Insn('CHAR_FLAG1_UNSET', Char(24), 32768),
	Insn('OBJ_FLAG_UNSET', Object(8), 4096),
	Insn('OBJ_FLAG_SET', Object(8), 4),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (190, 1000, -8370), 0),
	Insn('CAM_ROTATE', 337, 26, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 17580, 0),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100742V#11P#0000F呼……\n'
		'真是个大好人啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100743V#6P#0204F……是啊。{wait}'
		'{page}'
		'#11100744V#0202F好人等级几乎可以和\n'
		'罗伊德前辈相媲美了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(259), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100745V#11P#0006F那个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100746V#0303F#12P哈，但再怎么说，\n'
		'他也是个贸易商。{wait}'
		'{page}'
		'#11100747V#0300F如果只是个单纯的老好人，\n'
		'我想根本就干不下去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100748V#0104F#2P不过，哈罗德先生似乎与\n'
		'当地产业保持着良好的合作关系，\n'
		'同时稳定踏实地发展自身业务。{wait}'
		'{page}'
		'#11100749V#0100F一直都听说克洛斯贝尔的贸易商\n'
		'大多都通过国际贸易来不择手段地\n'
		'大发横财……{wait}'
		'{page}'
		'#11100750V在这些人之中，哈罗德先生的\n'
		'诚实善良算是十分难能可贵吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100751V#0305F#12P原来如此，是这样啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 270, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100752V#11P#0003F既有哈罗德先生这样正直的好人，\n'
		'也有鲁巴彻商会那种组织。{wait}'
		'{page}'
		'#11100753V#0000F……这就是如今的克洛斯贝尔吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100754V#0103F#2P嗯，是啊……{wait}'
		'{page}'
		'#11100755V#0100F所以我才觉得，现在的克洛斯贝尔\n'
		'也并非无可救药。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100756V#11P#0004F是啊……我也是这么想的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100757V#5P#0000F──那么，都已经过中午了。{wait}'
		'{page}'
		'#11100758V接下来，该前往下个目的地了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100759V#0100F#2P嗯……\n'
		'是『圣乌尔斯拉医科大学』吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100760V#6P#0203F……………………………………{wait}'
		'{page}'
		'#11100761V#0200F……是在南出口方向吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100762V#5P#0000F嗯，从这里一直向南走，\n'
		'就能看到巴士站了。{wait}'
		'{page}'
		'#11100763V听说巴士每三十分钟\n'
		'就会来一班。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100764V#0305F#12P这样啊，那还真是方便。{wait}'
		'{page}'
		'#11100765V#0300F好了。\n'
		'总之，我们就先出发吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100766V#5P#0000F好的……{wait}'
		'{page}'
		'#11100767V#0004F（医科大学吗……\n'
		'\u3000终于能见到赛西儿姐姐了。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('IMG_LOAD', ResId(0), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis203.itp'),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}可以使用克洛斯贝尔市内地图了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}在市内的原野上按下#176I，\n'
		'就能开启整个市街的地图。\n'
		'（再次按下#176I，\n'
		'\u3000将会显示自治州的地图。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 18, 0, 0, 100),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}在市内打开地图时，\n'
		'可以直接移动到\n'
		'各区域内。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}想要直接移动，请在左边的街区列表中\n'
		'选择要去的场所。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}不过，在某些特殊状况下，\n'
		'是无法使用市内地图的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0xD5', 30),
	Insn('0x4C', Char(11), -1),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG2_UNSET', Char(11), 32768),
	Insn('0x4C', Char(10), -1),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('0x4C', Char(8), -1),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(9), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(14), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG2_UNSET', Char(12), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(13), 128),
	Insn('CHAR_FLAG2_UNSET', Char(13), 32768),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('CHAR_SET_POS', Char(0), (0, 0, -7800), 0),
	Insn('FLAG_SET', Flag(777)),
	Insn('QUEST', 63, Insn('TASK_SET', 5)),
	Insn('FORK_QUIT', Char(35), 1),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('0x9F', Insn('0', Char(24))),
	Insn('0x9F', Insn('1', (17420, 0, -4780))),
	Insn('0x9F', Insn('1', (9540, 0, -2690))),
	Insn('0x9F', Insn('1', (1040, 0, -2580))),
	Insn('0x9F', Insn('2', Char(24), 112, 100663319)),
	Insn('0x71', Object(8), b'[\x00', 65656, 0),
	Insn('0x79', b'\x08\x00'),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('CHAR_ROTATE', Char(254), 260, 50),
	Insn('0x9F', Insn('0', Char(24))),
	Insn('0x9F', Insn('1', (-5850, 0, -3450))),
	Insn('0x9F', Insn('1', (-16290, 0, -3810))),
	Insn('0x9F', Insn('1', (-28280, -1380, -3420))),
	Insn('0x9F', Insn('2', Char(24), 112, 100663319)),
	Insn('0x71', Object(8), b'[\x00', 65656, 0),
	Insn('0x79', b'\x08\x00'),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch02500', 30),
	Insn('LOAD_CHCP', 'chr/ch28100', 31),
	Insn('LOAD_CHCP', 'chr/ch21200', 32),
	Insn('LOAD_CHCP', 'chr/ch21400', 33),
	Insn('LOAD_CHCP', 'chr/ch20000', 34),
	Insn('LOAD_CHCP', 'chr/ch23600', 35),
	Insn('EFF_LOAD', ResId(0), 'event\\eva05_00.eff'),
	Insn('CAM_OFFSET', (-1000, 2500, 11000), 0),
	Insn('CAM_ROTATE', 23, 6, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 34500, 0),
	Insn('CHAR_FLAG1_SET', Char(257), 8),
	Insn('CHAR_FLAG1_SET', Char(258), 8),
	Insn('CHAR_FLAG1_SET', Char(259), 8),
	Insn('CHAR_FLAG1_SET', Char(260), 8),
	Insn('CHAR_SET_CHCP', Char(27), 30),
	Insn('CHAR_SET_FRAME', Char(27), 0),
	Insn('CHAR_FLAG1_UNSET', Char(27), 128),
	Insn('CHAR_FLAG2_UNSET', Char(27), 32768),
	Insn('CHAR_FLAG1_SET', Char(27), 32768),
	Insn('CHAR_SET_POS', Char(27), (-30600, -8200, -24900), 270),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 128),
	Insn('CHAR_FLAG2_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_SET', Char(16), 128),
	Insn('CHAR_FLAG2_SET', Char(16), 32768),
	Insn('OBJ_FLAG_SET', Object(0), 4096),
	Insn('CHAR_FLAG1_UNSET', Char(24), 128),
	Insn('0x78', b'\t', Char(24)),
	Insn('OBJ_FLAG_SET', Object(9), 4096),
	Insn('OBJ_FLAG_UNSET', Object(9), 4),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 4),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(24), (15000, 0, -3000), 0),
	Insn('0xD3', Char(24), 0, 270000, 0, 0),
	Insn('0x70', Object(9), b'\x00\x00'),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('CHAR_FLAG1_SET', Char(31), 32768),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_FLAG1_SET', Char(33), 32768),
	Insn('CHAR_FLAG1_SET', Char(34), 32768),
	Insn('CHAR_SET_CHCP', Char(30), 31),
	Insn('CHAR_SET_FRAME', Char(30), 0),
	Insn('0x4B', Char(30), -1),
	Insn('CHAR_SET_POS', Char(30), (-15000, 0, -6300), 90),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('CHAR_SET_CHCP', Char(31), 32),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_SET_POS', Char(31), (-6800, 0, 4000), 270),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_CHCP', Char(32), 33),
	Insn('CHAR_SET_FRAME', Char(32), 0),
	Insn('CHAR_SET_POS', Char(32), (-8300, 0, 2500), 90),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_CHCP', Char(33), 34),
	Insn('CHAR_SET_FRAME', Char(33), 0),
	Insn('0x4B', Char(33), -1),
	Insn('CHAR_SET_POS', Char(33), (-19300, 0, 19400), 180),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_CHCP', Char(34), 35),
	Insn('CHAR_SET_FRAME', Char(34), 0),
	Insn('0x4B', Char(34), -1),
	Insn('CHAR_SET_POS', Char(34), (7000, 0, 12000), 0),
	Insn('CHAR_FLAG1_UNSET', Char(34), 128),
	Insn('CHAR_FLAG2_UNSET', Char(34), 32768),
	Insn('FORK', 30, 1, [
		Insn('0x96', Char(254), (5000, 0, -6300), 2000, 0),
	]),
	Insn('FORK', 33, 1, [
		Insn('0x98', Char(254), (10000, 0, -10000), 1500, 0),
	]),
	Insn('FORK', 34, 1, [
		Insn('0x9E', Char(254), 0, 5000, 180000, 2500, b'\x01\x00'),
	]),
	Insn('SOUND_PLAY', 458, 0, 0, 100),
	Insn('FORK', 24, 1, [
		Insn('0x96', Char(254), (-26000, 1000, -3000), 6000, 0),
	]),
	Insn('0x71', Object(9), b'y\x00', 180, 32),
	Insn('CAM_OFFSET', (-1000, 1500, 11000), 5000),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 19))),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('CHAR_SET_POS', Char(257), (10600, 0, 24000), 180),
	Insn('CHAR_SET_POS', Char(258), (12000, 0, 24000), 180),
	Insn('CHAR_SET_POS', Char(259), (10600, 0, 25400), 180),
	Insn('CHAR_SET_POS', Char(260), (12000, 0, 25400), 180),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (10600, 0, 19000), 1500, 0),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (12000, 0, 19000), 1500, 0),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (10600, 0, 20400), 1500, 0),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (12000, 0, 20400), 1500, 0),
	]),
	Insn('SOUND_PLAY', 829, 0, 0, 100),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (11300, 1000, 19700), 0),
	Insn('CAM_ROTATE', 45, 17, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 22500, 0),
	Insn('CAM_DISTANCE', 20500, 3000),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(257), 8),
	Insn('CHAR_FLAG1_UNSET', Char(258), 8),
	Insn('CHAR_FLAG1_UNSET', Char(259), 8),
	Insn('CHAR_FLAG1_UNSET', Char(260), 8),
	Insn('CHAR_FLAG1_UNSET', Char(30), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(31), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(32), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(33), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(34), 32768),
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
	Insn('OBJ_FLAG_SET', Object(9), 4),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11201009V#6P#0006F呼啊啊啊啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11201010V#0106F#5P真的好困……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11201011V#5P#0306F毕竟我们昨天\n'
		'差不多熬了一个晚上啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11201012V#0206F……已经要到极限了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
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
		'#11201013V#6P#0004F总之，回去以后，\n'
		'大家好好睡一觉吧。{wait}'
		'{page}'
		'#11201014V#0000F之后再向课长报告。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11201015V#0100F好啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 200),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 2),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (10600, 0, 8800), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 2),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (12000, 0, 8800), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 2),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (10600, 0, 10200), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (12000, 0, 10200), 1500, 0),
	]),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(259), 1),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('0x6F', b'\x10'),
	Insn('FORK_QUIT', Char(35), 1),
	Insn('CAM_OFFSET', (-19000, -7100, -22800), 0),
	Insn('CAM_ROTATE', 35, 23, 0, 0),
	Insn('0x6E', 550, 0),
	Insn('CAM_DISTANCE', 19500, 0),
	Insn('0x90', Char(257), (-16400, -6350, -19400), b'\xe1\x00'),
	Insn('0x90', Char(258), (-15600, -6350, -20200), b'\xe1\x00'),
	Insn('0x90', Char(260), (-15200, -5350, -18200), b'\xe1\x00'),
	Insn('0x90', Char(259), (-14400, -5350, -19000), b'\xe1\x00'),
	Insn('EFF_PLAY', (ResId(0), 0), Char(27), 320, 0, 0, 1300, 0, 350, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (-19700, -8200, -22700), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (-18900, -8200, -23500), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-20900, -8200, -23900), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (-20100, -8200, -24700), 2000, 0),
	]),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('0x6F', b'\x11'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#11201016V#11P#0105F哎呀……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-28620, -7100, -24980), 2000),
	Insn('CAM_ROTATE', 35, 23, 0, 2000),
	Insn('CAM_DISTANCE', 17000, 2000),
	Insn('0x6F', b'y'),
	Insn('CHAR_ROTATE', Char(27), 90, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(27), Text(
		'#11201017V#6P#1002F哟～大家辛苦了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-29600, -7100, -24900), 2000),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (-28600, -8200, -24400), 3000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (-28600, -8200, -25500), 3000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (-27200, -8200, -24400), 3000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (-27200, -8200, -25500), 3000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11201018V#11P#0011F课长……怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11201019V#0302F难道是特意出来迎接\n'
		'我们的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('0x23', 6), Insn('CONST', 8), Insn('GE'), Insn('END')]), [
			Insn('TEXT_TALK', Char(27), Text(
				'#11201020V#6P#1011F哈，我怎么会做\n'
				'那种肉麻的事情。{wait}'
				'{page}'
				'#11201021V#1002F总之呢，事情的经过，\n'
				'我在和索妮亚的导力通讯中已经听说了。{wait}'
				'{page}'
				'#11201022V就初次进行市外活动来说，\n'
				'你们已经算是相当努力了哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#11201023V#11P#0000F谢、谢谢……\n'
				'（……这是在夸奖我们吗？）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('0x23', 6), Insn('CONST', 5), Insn('GE'), Insn('END')]), [
			Insn('TEXT_TALK', Char(27), Text(
				'#11201020V#6P#1011F哈，我怎么会做\n'
				'那种肉麻的事情。{wait}'
				'{page}'
				'#11201021V#1002F总之呢，事情的经过，\n'
				'我在和索妮亚的导力通讯中已经听说了。{wait}'
				'{page}'
				'#11201024V#1004F虽然有些运气成分在内，\n'
				'但你们也算是很努力了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#11201025V#11P#0005F是、是的。\n'
				'（我们果然还是不够成熟吗……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(27), Text(
				'#11201020V#6P#1011F哈，我怎么会做\n'
				'那种肉麻的事情。{wait}'
				'{page}'
				'#11201021V#1002F总之呢，事情的经过，\n'
				'我在和索妮亚的导力通讯中已经听说了。{wait}'
				'{page}'
				'#11201026V#1003F虽然觉得你们实在是太过依赖运气了，\n'
				'不过算了，只要结果ＯＫ就好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#11201027V#11P#0006F……十分抱歉。\n'
				'（无言以对啊……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('0xD0', 6, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('TEXT_TALK', Char(258), Text(
		'#11201028V#11P#0100F那……\n'
		'课长您究竟是在这里做什么呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11201029V#11P#0200F如果只是为了在早饭之后出来吸烟，\n'
		'这地方也太奇怪了吧……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(27), Text(
		'#11201030V#6P#1011F呵……那也没办法吧？{wait}'
		'{page}'
		'#11201031V#1001F突然来了那种客人，再怎么说，\n'
		'也没法继续在那里安安稳稳地吸烟了。{wait}'
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
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(257), Text(
		'#11201032V#11P#0005F那种客人……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11201033V#0305F到底是谁来了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(27), Text(
		'#11201034V#6P#1000F不认识……\n'
		'不是来找你们的吗？{wait}'
		'{page}'
		'#11201035V该说是莫名其妙地自来熟吗……\n'
		'总之真是一点也不客气啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11201036V#11P#0001F哎？\n'
		'总之，那位客人还在里面吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(258), 0, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#11201037V#12P#0101F……进去看看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 0, 500),
	Insn('SLEEP', 400),
	Insn('FORK_LOOP', 27, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_LOOP', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_LOOP', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 24))),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-28600, -8200, -22600), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('OBJ_FLAG_UNSET', Object(0), 16),
	Insn('0x71', Object(0), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('0x79', b'\x00\x00'),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xb8\x0b\x00\x00\xdc\x05\x00\x00\x00'),
	]),
	Insn('SLEEP', 1200),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 2),
	Insn('SLEEP', 300),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 2),
	Insn('SLEEP', 300),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('SLEEP', 300),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(259), 2),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('FORK_QUIT', Char(27), 2),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(259), 1),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('EFF_STOP', (ResId(0), 0)),
	Insn('FLAG_SET', Flag(741)),
	Insn('NEW_SCENE', 'c0110', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('SLEEP', 600),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (-29300, -8200, -23000), 1500, 0),
	]),
	Insn('SLEEP', 800),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (-28600, -8200, -24000), 1500, 0),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (-29300, -8200, -24400), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 1, [
		Insn('0x97', Char(254), (0, 0, 5000), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 1, [
		Insn('0x97', Char(254), (0, 0, 5000), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 1, [
		Insn('0x97', Char(254), (0, 0, 5000), 1500, 0),
	]),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('SOUND_LOAD', 803),
	Insn('CAM_OFFSET', (-1000, 2500, 11000), 0),
	Insn('CAM_ROTATE', 23, 6, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 34500, 0),
	Insn('CHAR_FLAG1_SET', Char(258), 8),
	Insn('CHAR_FLAG1_SET', Char(259), 8),
	Insn('CHAR_SET_POS', Char(257), (-23800, -8200, -23800), 270),
	Insn('CHAR_SET_POS', Char(260), (-23000, -8200, -24600), 270),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_SET', Char(16), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 128),
	Insn('0x78', b'\x08', Char(24)),
	Insn('OBJ_FLAG_SET', Object(8), 4096),
	Insn('OBJ_SET_FRAME', Object(8), 'light', Insn('0', 1)),
	Insn('OBJ_FLAG_UNSET', Object(8), 4),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 4),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(24), (-1500, 0, -5500), 0),
	Insn('0xD3', Char(24), 0, 270000, 0, 0),
	Insn('0x70', Object(8), b'\x00\x00'),
	Insn('CHAR_FLAG1_SET', Char(31), 32768),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_FLAG1_SET', Char(33), 32768),
	Insn('CHAR_FLAG1_SET', Char(34), 32768),
	Insn('CHAR_SET_CHCP', Char(31), 3),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_SET_POS', Char(31), (-9300, 0, -7200), 0),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_CHCP', Char(32), 2),
	Insn('CHAR_SET_FRAME', Char(32), 0),
	Insn('CHAR_SET_POS', Char(32), (-9700, 0, -5500), 180),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_CHCP', Char(33), 15),
	Insn('CHAR_SET_FRAME', Char(33), 0),
	Insn('0x4B', Char(33), -1),
	Insn('CHAR_SET_POS', Char(33), (-14500, 0, -500), 90),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_CHCP', Char(34), 5),
	Insn('CHAR_SET_FRAME', Char(34), 0),
	Insn('0x4B', Char(34), -1),
	Insn('CHAR_SET_POS', Char(34), (-15500, 0, 1000), 90),
	Insn('CHAR_FLAG1_UNSET', Char(34), 128),
	Insn('CHAR_FLAG2_UNSET', Char(34), 32768),
	Insn('FORK', 33, 1, [
		Insn('0x98', Char(254), (10000, 0, 12000), 1500, 0),
	]),
	Insn('FORK', 34, 1, [
		Insn('0x98', Char(254), (10000, 0, 12000), 1500, 0),
	]),
	Insn('CAM_OFFSET', (-1000, 1500, 11000), 5000),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 28))),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('SLEEP', 4850),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 26))),
	Insn('SLEEP', 150),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 27))),
	Insn('0x6F', b'\x01'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-25800, -7600, -16800), 0),
	Insn('CAM_ROTATE', 35, 12, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('CAM_DISTANCE', 20500, 4000),
	Insn('SLEEP', 3000),
	Insn('FORK_QUIT', Char(35), 1),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(258), 8),
	Insn('CHAR_FLAG1_UNSET', Char(259), 8),
	Insn('SOUND_STOP', 803),
	Insn('FLAG_SET', Flag(742)),
	Insn('NEW_SCENE', 'c0110', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-28400, -8200, -23800), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-28400, -8200, -22300), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('OBJ_FLAG_UNSET', Object(0), 16),
	Insn('0x71', Object(0), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('0x79', b'\x00\x00'),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-28400, -8200, -20300), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (-28800, -8200, -24000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (-28800, -8200, -20300), 2000, 0),
	]),
	Insn('SLEEP', 1500),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('RETURN'),
]

data['code'][28] = [
	Insn('SOUND_PLAY', 803, 0, 2, 100),
	Insn('SLEEP', 5000),
	Insn('SOUND_LOOP', 803, 90),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 80),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 70),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 60),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 50),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 40),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 30),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 20),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 10),
	Insn('SLEEP', 200),
	Insn('SOUND_STOP', 803),
	Insn('RETURN'),
]

data['code'][29] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0xFFFFFFFF), 0),
	Insn('FADE_ON', 500, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FADE_OFF', 0, Color(0xFFFFFFFF)),
	Insn('LOAD_CHCP', 'chr/ch02300', 30),
	Insn('CAM_OFFSET', (-21100, -7100, -24900), 0),
	Insn('CAM_ROTATE', 40, 17, 0, 0),
	Insn('0x6E', 550, 0),
	Insn('CAM_DISTANCE', 17000, 0),
	Insn('CHAR_SET_POS', Char(257), (-20800, -8200, -25500), 270),
	Insn('CHAR_SET_POS', Char(258), (-20800, -8200, -24300), 270),
	Insn('CHAR_SET_POS', Char(259), (-19400, -8200, -25700), 270),
	Insn('CHAR_SET_POS', Char(260), (-19400, -8200, -24500), 270),
	Insn('CHAR_SET_CHCP', Char(28), 30),
	Insn('CHAR_SET_FRAME', Char(28), 0),
	Insn('CHAR_FLAG1_UNSET', Char(28), 128),
	Insn('CHAR_FLAG2_UNSET', Char(28), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(28), 4),
	Insn('CHAR_FLAG1_SET', Char(28), 32768),
	Insn('CHAR_SET_POS', Char(28), (-29000, -8200, -24900), 0),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu02600.itp'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('SLEEP', 600),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101412V#11P#0105F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101413V#11P#0005F那个人是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-27700, -7100, -24900), 2500),
	Insn('0x6F', b'\x01'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-27960, -7100, -24530), 0),
	Insn('CAM_ROTATE', 318, 17, 0, 0),
	Insn('0x6E', 550, 0),
	Insn('CAM_DISTANCE', 15420, 0),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (-26800, -8200, -24300), 2000, 0),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-26800, -8200, -25500), 2000, 0),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (-25400, -8200, -25700), 2000, 0),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (-25400, -8200, -24500), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(28), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(28), 90, 500),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('SLEEP', 300),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 500),
	Insn('TEXT_MESSAGE', Char(28), Text(
		'#12101414V──啊啊，太好了！{wait}'
		'{page}'
		'#12101415V我还在疑惑到底\n'
		'是不是在这里。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101416V#12P#0105F阿奈斯特先生……{wait}'
		'{page}'
		'#12101417V#0100F……莫非你是来\n'
		'找我的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(28), Text(
		'#12101418V#5P#2600F是啊，正好有些事情要去事务所，\n'
		'所以就顺路过来拜访你了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(28), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(28), Text(
		'#12101419V#5P#2605F……艾莉？{wait}'
		'{page}'
		'#12101420V#2601F怎么了？\n'
		'气色好像很不好啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101421V#12P#0108F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(28), Text(
		'#12101422V#5P#2603F之前你们似乎去了\n'
		'彩虹剧团……{wait}'
		'{page}'
		'#12101423V#2601F是不是警务工作遇到了什么问题？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101424V#12P#0106F……没、没什么。\n'
		'只是些小事而已。{wait}'
		'{page}'
		'#12101425V#0108F那个，其实是剧团的相关人员\n'
		'曾来找我们进行过商谈……{wait}'
		'{page}'
		'#12101426V#0102F只是前去报告一下而已。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(28), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(28)),
	Insn('TEXT_TALK', Char(28), Text(
		'#12101427V#5P#2606F……呼，我本来还在犹豫\n'
		'是不是该来这里。{wait}'
		'{page}'
		'#12101428V#2600F看来选择过来，果然还是正确的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101429V#12P#0105F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(28), Text(
		'#12101430V#5P#2603F……我就直截了当地说好了。{wait}'
		'{page}'
		'#12101431V#2601F艾莉……\n'
		'要不要从警察局辞职，然后回来工作？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101432V#12P#0105F！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101433V#6P#0011F（什、什么……！？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101434V#12P#0301F（喂喂……\n'
		'\u3000怎么回事，这事态发展也太唐突了吧。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101435V#12P#0205F（看来似乎也不是……\n'
		'\u3000与恋爱有关。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(28), Text(
		'#12101436V#5P#2603F我知道你会选择当警察，\n'
		'也是有自己的想法的。{wait}'
		'{page}'
		'#12101437V#2601F但是，看看你那疲惫的面孔……\n'
		'像孩子般迷茫的目光。{wait}'
		'{page}'
		'#12101438V这真的是……\n'
		'你该走的道路吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101439V#12P#0108F那、那个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(28), Text(
		'#12101440V#5P#2603F……我也明白，你对\n'
		'目前的政治状况感到绝望。{wait}'
		'{page}'
		'#12101441V而你之所以想加入成为警察，\n'
		'恐怕也与这一点有一定关系吧。{wait}'
		'{page}'
		'#12101442V#2601F可是，艾莉……\n'
		'我希望你能稍微体谅一下\n'
		'市长的辛苦与心情。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101443V#12P#0105F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(28), Text(
		'#12101444V#5P#2601F由于下个月将要举办纪念庆典……\n'
		'市长现在已经忙到焦头烂额了。{wait}'
		'{page}'
		'#12101445V纪念庆典之后，又必须\n'
		'在财政预算方面\n'
		'与帝国派和共和国派双方周旋……{wait}'
		'{page}'
		'#12101446V#2603F还有半年之后的市长选举……{wait}'
		'{page}'
		'#12101447V虽然市长已经决定要从政界引退了，\n'
		'但由于没有发现可以放心托付的接班人，\n'
		'所以似乎还在对引退一事相当犹豫。{wait}'
		'{page}'
		'#12101448V#2600F要是有你在身边的话，\n'
		'市长肯定会比现在感到安心许多。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101449V#12P#0106F……………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(28), Text(
		'#12101450V#5P#2606F……抱歉，\n'
		'似乎说了很多僭越之言。{wait}'
		'{page}'
		'#12101451V可是，无论如何，我也无法做到\n'
		'视而不见。{wait}'
		'{page}'
		'#12101452V#2600F身为一直尊敬着市长的人……\n'
		'身为看着你从小长大的人……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101453V#12P#0108F……阿奈斯特先生……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(28), Text(
		'#12101454V#5P#2604F当然，你的道路\n'
		'最终还是要由你自己来决定。可是……{wait}'
		'{page}'
		'#12101455V#2600F希望你能再次考虑一下，\n'
		'自己如今的选择真的是正确的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101456V#12P#0108F#30W……………………………………{wait}'
		'{page}'
		'#12101457V#0106F#40W……请容我再稍微考虑一下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(258), 135, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101458V#5P#0102F各位，对不起。{wait}'
		'{page}'
		'#12101459V#0103F……我稍微有点累了，\n'
		'先回自己的房间休息一下。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(258), 300),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_WATCH', Char(259), Char(258), 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101460V#6P#0005F啊……好的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(258), 315, 500),
	Insn('FORK_LOOP', 28, 2, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (-28600, -8200, -23000), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (-28600, -8200, -21800), 1500, 0),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 315, 300),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('OBJ_FLAG_UNSET', Object(0), 16),
	Insn('0x71', Object(0), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('0x79', b'\x00\x00'),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (-28600, -8200, -20000), 1500, 0),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 2),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('0x71', Object(0), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('0x79', b'\x00\x00'),
	Insn('OBJ_FLAG_SET', Object(0), 16),
	Insn('FORK_QUIT', Char(28), 2),
	Insn('SLEEP', 500),
	Insn('CHAR_ROTATE', Char(28), 90, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(28), Text(
		'#12101461V#5P#2603F──你们几位……\n'
		'突然说这些，实在很抱歉。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_ROTATE', Char(260), 270, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101462V#6P#0006F……不，大家毕竟\n'
		'似乎也都各有苦衷。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101463V#12P#0301F不过，不要再说\n'
		'那种让大小姐难受的话了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101464V#12P#0203F……是啊。{wait}'
		'{page}'
		'#12101465V#0211F您说出那些话，好像是想把艾莉前辈\n'
		'从我们的身边夺走一样呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(28), Text(
		'#12101466V#5P#2604F哈哈，其实我的本意也\n'
		'并非如此……{wait}'
		'{page}'
		'#12101467V#2600F只是……她曾经一直都想成为\n'
		'一名政治家，你们知道吗？{wait}'
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
		'#12101468V#6P#0005F哎……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101469V#12P#0305F喂喂，还有那种事吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101470V#12P#0205F确实，她对政治和经济方面\n'
		'都有着非常详细的了解……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(28), Text(
		'#12101471V#5P#2600F嗯，她当时是作为市长的后继者，\n'
		'一直都立志步入政治之道，\n'
		'所以学习了很多这方面的知识。{wait}'
		'{page}'
		'#12101472V#2603F也正因如此，她才会去各国留学，\n'
		'以加深修养，以及培养国际化的\n'
		'政治嗅觉……{wait}'
		'{page}'
		'#12101473V#2601F……可是，自从去年回国之后，\n'
		'她却突然改变主意要当警察了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101474V#6P#0001F原来是这样的吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101475V#12P#0206F……之前都不知道呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101476V#12P#0306F嗯，虽然很奇怪这种出身名门的大小姐\n'
		'为什么会愿意当警察……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(28), Text(
		'#12101477V#5P#2603F可以的话，在她的结论得出之前，\n'
		'希望各位能在一旁默默地守护她。{wait}'
		'{page}'
		'#12101478V#2601F就算她能继续坚持下去……\n'
		'但仍怀抱着迷惘之心的话，\n'
		'应该是无法走到底的吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 856, 0, 0, 100),
	Insn('SLEEP', 1500),
	Insn('EMOTE', Char(28), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(28), Text(
		'#12101479V#5P#2605F都已经这么晚了吗……{wait}'
		'{page}'
		'#12101480V#2600F实在很抱歉，打扰你们了，\n'
		'我这就告辞了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101481V#6P#0000F啊，好的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-26080, -6900, -25260), 0),
	Insn('CAM_ROTATE', 40, 17, 0, 0),
	Insn('0x6E', 550, 0),
	Insn('CAM_DISTANCE', 17000, 0),
	Insn('CAM_OFFSET', (-23700, -7100, -24900), 6000),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(28), 500),
	]),
	Insn('FORK_LOOP', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(28), 500),
	]),
	Insn('FORK_LOOP', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(28), 500),
	]),
	Insn('FORK', 28, 1, [
		Insn('0x95', Char(254), (-27600, -8200, -23500), 2000, 1),
	]),
	Insn('FORK_AWAIT', Char(28), 1),
	Insn('FORK', 28, 1, [
		Insn('0x95', Char(254), (-20600, -8200, -23500), 2000, 1),
	]),
	Insn('FORK_AWAIT', Char(28), 1),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('FORK', 28, 1, [
		Insn('0x95', Char(254), (-13800, -4200, -16600), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(28), 1),
	Insn('0x6F', b'\x01'),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('CHAR_FLAG1_SET', Char(28), 128),
	Insn('CHAR_FLAG2_SET', Char(28), 32768),
	Insn('CAM_OFFSET', (-26080, -6900, -25260), 1500),
	Insn('CAM_DISTANCE', 15000, 1500),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101482V#6P#0006F……呼。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101483V#0206F#11P总觉得今天……\n'
		'令人头痛的事也太多了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101484V#5P#0306F是啊……沉重的事情\n'
		'真是一件接着一件。{wait}'
		'{page}'
		'#12101485V#0301F怎么说呢，精神极度疲劳啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101486V#6P#0003F……是啊。{wait}'
		'{page}'
		'#12101487V#0000F向课长报告之后，\n'
		'我们也早点回去休息吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 15500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('FLAG_SET', Flag(744)),
	Insn('NEW_SCENE', 'c0110', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][30] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch02707', 30),
	Insn('LOAD_CHCP', 'chr/ch28100', 31),
	Insn('LOAD_CHCP', 'chr/ch21200', 32),
	Insn('LOAD_CHCP', 'chr/ch21400', 33),
	Insn('LOAD_CHCP', 'chr/ch20000', 34),
	Insn('LOAD_CHCP', 'chr/ch23600', 35),
	Insn('CAM_OFFSET', (-1000, 2500, 11000), 0),
	Insn('CAM_ROTATE', 23, 6, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 34500, 0),
	Insn('CHAR_SET_POS', Char(0), (-19000, -4200, -11700), 0),
	Insn('CHAR_SET_POS', Char(1), (-19000, -4200, -11700), 0),
	Insn('CHAR_SET_POS', Char(2), (-19000, -4200, -11700), 0),
	Insn('CHAR_SET_POS', Char(3), (-19000, -4200, -11700), 0),
	Insn('CHAR_SET_CHCP', Char(29), 30),
	Insn('CHAR_SET_FRAME', Char(29), 0),
	Insn('CHAR_FLAG1_UNSET', Char(29), 128),
	Insn('CHAR_FLAG2_UNSET', Char(29), 32768),
	Insn('CHAR_FLAG1_SET', Char(29), 32768),
	Insn('CHAR_SET_POS', Char(29), (-29000, -8150, -24000), 180),
	Insn('FORK_FUNC', Char(29), 3, Function((0, 0))),
	Insn('EXPR_CHAR_ATTR', Char(29), 45, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(29), 46, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(29), 47, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_UNSET', Char(29), 1),
	Insn('0x7D', b'\xff\xff\xff\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xb4\xd7\xe6', 15, 130, 0),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 128),
	Insn('CHAR_FLAG2_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_SET', Char(15), 128),
	Insn('CHAR_FLAG2_SET', Char(15), 32768),
	Insn('CHAR_FLAG1_SET', Char(16), 128),
	Insn('CHAR_FLAG2_SET', Char(16), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 128),
	Insn('0x78', b'\t', Char(24)),
	Insn('OBJ_FLAG_SET', Object(9), 4096),
	Insn('OBJ_FLAG_UNSET', Object(9), 4),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 4),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(24), (15000, 0, -3000), 0),
	Insn('0xD3', Char(24), 0, 270000, 0, 0),
	Insn('0x70', Object(9), b'\x00\x00'),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('CHAR_FLAG1_SET', Char(31), 32768),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_FLAG1_SET', Char(33), 32768),
	Insn('CHAR_FLAG1_SET', Char(34), 32768),
	Insn('CHAR_SET_CHCP', Char(30), 31),
	Insn('CHAR_SET_FRAME', Char(30), 0),
	Insn('0x4B', Char(30), -1),
	Insn('CHAR_SET_POS', Char(30), (-15000, 0, -6300), 90),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('CHAR_SET_CHCP', Char(31), 32),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_SET_POS', Char(31), (-6800, 0, 4000), 270),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_CHCP', Char(32), 33),
	Insn('CHAR_SET_FRAME', Char(32), 0),
	Insn('CHAR_SET_POS', Char(32), (-8300, 0, 2500), 90),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_CHCP', Char(33), 34),
	Insn('CHAR_SET_FRAME', Char(33), 0),
	Insn('0x4B', Char(33), -1),
	Insn('CHAR_SET_POS', Char(33), (-19300, 0, 19400), 180),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_CHCP', Char(34), 35),
	Insn('CHAR_SET_FRAME', Char(34), 0),
	Insn('0x4B', Char(34), -1),
	Insn('CHAR_SET_POS', Char(34), (7000, 0, 12000), 0),
	Insn('CHAR_FLAG1_UNSET', Char(34), 128),
	Insn('CHAR_FLAG2_UNSET', Char(34), 32768),
	Insn('FORK', 30, 1, [
		Insn('0x96', Char(254), (5000, 0, -6300), 2000, 0),
	]),
	Insn('FORK', 33, 1, [
		Insn('0x98', Char(254), (10000, 0, -10000), 1500, 0),
	]),
	Insn('FORK', 34, 1, [
		Insn('0x9E', Char(254), 0, 5000, 180000, 2500, b'\x01\x00'),
	]),
	Insn('FORK', 24, 1, [
		Insn('0x96', Char(254), (-26000, 1000, -3000), 6000, 0),
	]),
	Insn('0x71', Object(9), b'y\x00', 180, 32),
	Insn('CAM_OFFSET', (-1000, 1500, 11000), 5000),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 19))),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 458, 0, 0, 100),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-25800, -7600, -16800), 0),
	Insn('CAM_ROTATE', 35, 12, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('CAM_DISTANCE', 20500, 4000),
	Insn('SLEEP', 3000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('FORK_QUIT', Char(35), 1),
	Insn('EXPR_CHAR_ATTR', Char(29), 45, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(29), 46, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(29), 47, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(29), 1),
	Insn('FLAG_SET', Flag(745)),
	Insn('NEW_SCENE', 'c0110', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][31] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50109', 30),
	Insn('SOUND_LOAD', 803),
	Insn('CAM_OFFSET', (-1000, 2500, 11000), 0),
	Insn('CAM_ROTATE', 23, 6, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 34500, 0),
	Insn('CHAR_SET_POS', Char(257), (1000, 0, -16800), 90),
	Insn('CHAR_SET_POS', Char(258), (1000, 0, -15600), 90),
	Insn('CHAR_SET_POS', Char(259), (-200, 0, -16800), 90),
	Insn('CHAR_SET_POS', Char(260), (-200, 0, -15600), 90),
	Insn('CHAR_SET_POS', Char(265), (3200, 0, -16200), 270),
	Insn('CHAR_FLAG1_UNSET', Char(4), 128),
	Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
	Insn('0x78', b'\x0b', Char(24)),
	Insn('OBJ_FLAG_SET', Object(11), 4096),
	Insn('OBJ_SET_FRAME', Object(11), 'light', Insn('0', 1)),
	Insn('OBJ_FLAG_UNSET', Object(11), 4),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 4),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(24), (6000, 0, -16200), 0),
	Insn('0xD3', Char(24), 0, 0, 0, 0),
	Insn('0x74', Object(11), 7680),
	Insn('0x70', Object(11), b'\x00\x00'),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_SET', Char(15), 128),
	Insn('CHAR_FLAG2_SET', Char(15), 32768),
	Insn('CHAR_FLAG1_SET', Char(16), 128),
	Insn('CHAR_FLAG2_SET', Char(16), 32768),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('CHAR_FLAG1_SET', Char(31), 32768),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_FLAG1_SET', Char(33), 32768),
	Insn('CHAR_FLAG1_SET', Char(34), 32768),
	Insn('CHAR_SET_CHCP', Char(30), 0),
	Insn('CHAR_SET_FRAME', Char(30), 0),
	Insn('0x4B', Char(30), -1),
	Insn('CHAR_SET_POS', Char(30), (0, 0, -5000), 270),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('CHAR_SET_CHCP', Char(31), 3),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_SET_POS', Char(31), (-9300, 0, -7200), 0),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_CHCP', Char(32), 2),
	Insn('CHAR_SET_FRAME', Char(32), 0),
	Insn('CHAR_SET_POS', Char(32), (-9700, 0, -5500), 180),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_CHCP', Char(33), 15),
	Insn('CHAR_SET_FRAME', Char(33), 0),
	Insn('0x4B', Char(33), -1),
	Insn('CHAR_SET_POS', Char(33), (-4500, 0, 11500), 270),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_CHCP', Char(34), 5),
	Insn('CHAR_SET_FRAME', Char(34), 0),
	Insn('0x4B', Char(34), -1),
	Insn('CHAR_SET_POS', Char(34), (-5500, 0, 13000), 270),
	Insn('CHAR_FLAG1_UNSET', Char(34), 128),
	Insn('CHAR_FLAG2_UNSET', Char(34), 32768),
	Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xd5\x8f{', 38, 120, 0),
	Insn('OBJ_SET_FRAME', Object(255), 'sky', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'sky1', Insn('1', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'sd_mul', Insn('0', 1)),
	Insn('FORK', 30, 1, [
		Insn('0x9E', Char(254), 0, 5000, -180000, 2500, b'\x01\x00'),
	]),
	Insn('FORK', 33, 1, [
		Insn('0x98', Char(254), (-10000, 0, -12000), 1500, 0),
	]),
	Insn('FORK', 34, 1, [
		Insn('0x98', Char(254), (-10000, 0, -12000), 1500, 0),
	]),
	Insn('CAM_OFFSET', (-1000, 1500, 11000), 5000),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 28))),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (2700, 900, -14200), 0),
	Insn('CAM_ROTATE', 50, 21, 0, 0),
	Insn('0x6E', 550, 0),
	Insn('CAM_DISTANCE', 18000, 0),
	Insn('CAM_OFFSET', (2700, 900, -16200), 3000),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(265), Text(
		'#12201354V#11P#0500F各位，辛苦了。{wait}'
		'{page}'
		'#12201355V#0506F本来我也很想协助\n'
		'大家的，可是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12201356V#0102F#6P哪里，能协助我们探索那座塔\n'
		'就已经足够了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12201357V#0300F#6P是啊是啊，真是帮大忙了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12201358V#6P#0204F是啊……\n'
		'而且还把我们送到了这里。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12201359V#6P#0002F上士，真是谢谢了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#12201360V#11P#0509F呵呵，没什么。{wait}'
		'{page}'
		'#12201361V#0501F如果再有什么情况，请不用客气，\n'
		'随时和唐古拉姆门这边联系哦。{wait}'
		'{page}'
		'#12201362V今天的事情，\n'
		'我会向副司令报告的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12201363V#6P#0000F好的……\n'
		'那到时就万事拜托了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12201364V#0300F#6P那么，下次再见啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#12201365V#11P#0502F好的……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('CHAR_SET_CHCP', Char(265), 30),
	Insn('CHAR_SET_FRAME', Char(265), 0),
	Insn('0x0D'),
	Insn('SLEEP', 150),
	Insn('SOUND_PLAY', 11670, 186, 255, 90),
	Insn('TEXT_TALK', Char(265), Text(
		'#11P#0500F#20A各位，辛苦了。{wait}'
	)),
	Insn('SLEEP', 2500),
	Insn('CHAR_SET_CHCP', Char(265), 255),
	Insn('CHAR_SET_FRAME', Char(265), 0),
	Insn('0x92', Char(265), 3700, -16700, 500),
	Insn('FORK', 265, 1, [
		Insn('0x96', Char(254), (3700, 0, -16700), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(265), 1),
	Insn('CHAR_ROTATE', Char(265), 90, 500),
	Insn('0x71', Object(11), b'\x01\x00', 30, 0),
	Insn('SOUND_PLAY', 464, 0, 0, 100),
	Insn('0x79', b'\x0b\x00'),
	Insn('CHAR_FLAG1_SET', Char(265), 4),
	Insn('FORK', 265, 1, [
		Insn('0x96', Char(254), (4700, 500, -16700), 2000, 0),
	]),
	Insn('FORK', 265, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(265), 1),
	Insn('CHAR_FLAG1_UNSET', Char(265), 4),
	Insn('0x71', Object(11), b'\x1f\x00', 60, 0),
	Insn('SOUND_PLAY', 463, 0, 0, 100),
	Insn('0x79', b'\x0b\x00'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (6000, 1000, -16200), 0),
	Insn('CAM_ROTATE', 25, 19, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 17500, 0),
	Insn('SOUND_PLAY', 470, 0, 0, 100),
	Insn('0x71', Object(11), b'<\x00', 90, 0),
	Insn('0x79', b'\x0b\x00'),
	Insn('0x71', Object(11), b'y\x00', 180, 32),
	Insn('CAM_OFFSET', (12000, 1000, -4400), 4000),
	Insn('CAM_ROTATE', 60, 11, 0, 4000),
	Insn('CAM_DISTANCE', 19500, 4000),
	Insn('FORK', 24, 1, [
		Insn('0x96', Char(254), (6000, 0, -9200), 4000, 0),
	]),
	Insn('SOUND_PLAY', 486, 0, 0, 100),
	Insn('SLEEP', 1500),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('SOUND_PLAY', 471, 0, 0, 100),
	Insn('FORK', 24, 1, [
		Insn('0x9E', Char(254), 12000, -9200, 90000, 4000, b'\x01\x00'),
	]),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('FORK', 24, 1, [
		Insn('0x98', Char(254), (40000, 0, 0), 6000, 0),
	]),
	Insn('SLEEP', 3000),
	Insn('0x6F', b'y'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (400, 1000, -16200), 0),
	Insn('CAM_ROTATE', 55, 21, 0, 0),
	Insn('0x6E', 550, 0),
	Insn('CAM_DISTANCE', 18000, 0),
	Insn('FORK_QUIT', Char(24), 1),
	Insn('CHAR_FLAG1_SET', Char(24), 128),
	Insn('CHAR_FLAG1_UNSET', Char(24), 32768),
	Insn('OBJ_FLAG_UNSET', Object(11), 4096),
	Insn('OBJ_FLAG_SET', Object(11), 4),
	Insn('0x0D'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 315, 500),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#12201367V#0003F#11P那么……{wait}'
		'{page}'
		'#12201368V#0001F首先是对本周末举行的\n'
		'预演进行警戒啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12201369V#5P#0103F总之先回到支援课，\n'
		'讨论一下具体的行动安排吧。{wait}'
		'{page}'
		'#12201370V#0100F而且还要和彩虹剧团进行联系。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12201371V#6P#0203F……搜查一课的动向\n'
		'也有必要掌握啊。{wait}'
		'{page}'
		'#12201372V#0202F我想到时应该可以委托课长\n'
		'来帮忙探查……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12201373V#0302F#5P算了，反正肯定是\n'
		'有得忙了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 18500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('FORK_QUIT', Char(35), 1),
	Insn('BGM_STOP', 5000),
	Insn('BGM_WAIT'),
	Insn('0xB8', 100, 0),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}之后──罗伊德一行\n'
		'与彩虹剧团的相关人员进行联系后，\n'
		'讨论了预演时警戒工作的行动安排。{wait}'
		'{page}'
		'最后的结果，是罗伊德和艾莉\n'
		'当天在剧场内警戒……{wait}'
		'{page}'
		'兰迪和缇欧则在\n'
		'剧场外待命。{wait}'
		'{page}'
		'到了预演当日──{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('MINIGAME', 24, 0, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
	Insn('0xBA', 8),
	Insn('PARTY_CLEAR'),
	Insn('0x2E', b'\x00\xff\xff'),
	Insn('0x2E', b'\x01\xff\xff'),
	Insn('0x2E', b'\x02\xff\xff'),
	Insn('0x2E', b'\x03\xff\xff'),
	Insn('SOUND_STOP', 803),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'c040b', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][32] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (0, 800, 4000), 0),
	Insn('CAM_ROTATE', 18, 22, 0, 0),
	Insn('0x6E', 860, 0),
	Insn('CAM_DISTANCE', 28000, 0),
	Insn('SOUND_PLAY', 803, 0, 2, 0),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 55))),
	Insn('CHAR_SET_POS', Char(257), (2600, 0, -16600), 0),
	Insn('CHAR_SET_POS', Char(239), (3700, 0, -16800), 0),
	Insn('CHAR_SET_POS', Char(339), (2900, 0, -14300), 0),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(239), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(339), Color(0x00FFFFFF), 0),
	Insn('0x78', b'\t', Char(18)),
	Insn('OBJ_FLAG_SET', Object(9), 4096),
	Insn('OBJ_FLAG_SET', Object(9), 4),
	Insn('CHAR_FLAG1_SET', Char(18), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(18), 128),
	Insn('CHAR_FLAG1_UNSET', Char(18), 4),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(18), (16000, 0, -6000), 270),
	Insn('0xD3', Char(18), 0, 270000, 0, 0),
	Insn('0x74', Object(9), 7680),
	Insn('0x71', Object(9), b'y\x00', 180, 32),
	Insn('CHAR_FLAG1_SET', Char(11), 32768),
	Insn('CHAR_FLAG1_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 32768),
	Insn('CAM_ROTATE', 42, 22, 0, 9000),
	Insn('CAM_DISTANCE', 33000, 9000),
	Insn('0x6F', b'@'),
	Insn('0x6F', b'\x10'),
	Insn('0x0D'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (3400, 800, -10300), 0),
	Insn('CAM_ROTATE', 45, 19, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 19500, 0),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(239), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(339), Color(0xFFFFFFFF), 0),
	Insn('FORK', 339, 1, [
		Insn('0x95', Char(254), (2900, 0, -9300), 2000, 0),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (2600, 0, -11600), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 239, 1, [
		Insn('0x95', Char(254), (3700, 0, -11800), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(339), 1),
	Insn('CHAR_ROTATE', Char(339), 80, 700),
	Insn('SLEEP', 750),
	Insn('CHAR_ROTATE', Char(339), 270, 700),
	Insn('SLEEP', 500),
	Insn('FORK_QUIT', Char(35), 1),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600221V#1109F#11P哇～！\n'
		'有好多人哦～！{wait}'
		'{page}'
		'#13600222V#1110F这么多人全都是\n'
		'罗伊德的朋友吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(239), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600223V#12P#0012F不、不是啦……\n'
		'那再怎么说也是不可能的。{wait}'
		'{page}'
		'#13600224V#0000F不过，和纪念庆典的时候相比，\n'
		'这种人流已经算少了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600225V#12P#0108F琪雅不是克洛斯贝尔\n'
				'出身的吗……？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600226V#12P#0208F琪雅不是克洛斯贝尔\n'
				'出身的吧……？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600227V#12P#0308F也就是说，小琪不是克洛斯贝尔\n'
				'出身的啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('EMOTE', Char(339), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(339), 80, 500),
	Insn('SOUND_PLAY', 2032, 0, 255, 100),
	Insn('TEXT_TALK', Char(339), Text(
		'#1105F#5P#5A欸……{wait}'
	)),
	Insn('SLEEP', 800),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (9000, 1200, -6000), 0),
	Insn('CAM_ROTATE', 75, 20, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 14000, 0),
	Insn('OBJ_FLAG_UNSET', Object(9), 4),
	Insn('FORK_LOOP', 339, 2, [
		Insn('CHAR_WATCH', Char(254), Char(18), 100),
	]),
	Insn('CAM_OFFSET', (-2000, 1200, -6000), 4000),
	Insn('CAM_ROTATE', 45, 20, 0, 4000),
	Insn('CAM_DISTANCE', 16000, 4000),
	Insn('FORK', 18, 1, [
		Insn('0x98', Char(254), (-30000, 0, 0), 6000, 0),
	]),
	Insn('SOUND_PLAY', 458, 0, 0, 100),
	Insn('SLEEP', 2000),
	Insn('EMOTE', Char(339), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('SOUND_PLAY', 2033, 0, 255, 100),
	Insn('FORK_AWAIT', Char(18), 1),
	Insn('FORK_QUIT', Char(339), 2),
	Insn('OBJ_FLAG_UNSET', Object(9), 4096),
	Insn('CHAR_FLAG1_UNSET', Char(18), 32768),
	Insn('CHAR_FLAG1_SET', Char(18), 128),
	Insn('CHAR_FLAG1_SET', Char(18), 4),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 56))),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (3400, 800, -10300), 0),
	Insn('CAM_ROTATE', 45, 19, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 19500, 0),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(18), (-8010, 0, 16230), 225),
	Insn('0xD3', Char(18), 0, 245000, 0, 0),
	Insn('0x70', Object(9), b'\x00\x00'),
	Insn('EMOTE', Char(339), 0, 1700, (8, 9, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('0x9C', Char(339), b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x01\x00\x00\xb8\x0b\x00\x00'),
	Insn('SLEEP', 100),
	Insn('0x9C', Char(339), b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x01\x00\x00\xb8\x0b\x00\x00'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600228V#1107F#11P刚才有一个好大的铁箱子\n'
		'轰隆隆隆～地跑过去了啊！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600229V#12P#0014F哈哈，那个是车哦。{wait}'
		'{page}'
		'#13600230V#0002F你感觉自己是初次见到那个吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(339), 180, 500),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600231V#1109F#5P嗯，大概是第一次～！{wait}'
		'{page}'
		'#13600232V#1100F嘿嘿，是吗！\n'
		'那个东西叫做车呀～！{wait}'
		'{page}'
		'#13600233V#1110F那个那个，罗伊德，\n'
		'你们没有车吗～！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(239), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600234V#12P#0012F嗯～很遗憾啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600235V#1100F#5P嗯～这样啊。{wait}'
		'{page}'
		'#13600236V我还在想，要是大家一起坐的话，\n'
		'应该会很有意思呢～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600237V#12P#0106F嗯～突然有点羡慕起\n'
				'搜查一课了……{wait}'
				'{page}'
				'#13600238V#0101F不过，这么看来，琪雅确实\n'
				'不是克洛斯贝尔人吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600239V#12P#0206F总觉得有些羡慕起\n'
				'搜查一课了……{wait}'
				'{page}'
				'#13600240V#0201F不过，这么看来，琪雅果然\n'
				'不是克洛斯贝尔人吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600241V#12P#0306F真是的，都有些羡慕起\n'
				'搜查一课了……{wait}'
				'{page}'
				'#13600242V#0301F不过，这么看来，小琪果然\n'
				'不是克洛斯贝尔人啊？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600243V#6P#0006F嗯，如果曾住在这里，\n'
		'应该已经对车子司空见惯了吧。{wait}'
		'{page}'
		'#13600244V#0001F（可是，琪雅好像却知道\n'
		'\u3000这是可以乘坐的交通工具……）{wait}'
		'{page}'
		'#13600245V（……这究竟是怎么回事呢？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(339), 0, 1700, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600246V#1100F#5P怎么了，罗伊德？{wait}'
		'{page}'
		'#13600247V不是要去见什么\n'
		'游击士的吗～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600248V#12P#0000F是啊，那就出发吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600249V#12P#0100F去东侧大道吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600250V#12P#0202F去东侧大道吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600251V#12P#0300F向东侧大道出发吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (3400, 0, -10300), 0),
	Insn('CHAR_FLAG1_UNSET', Char(11), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(10), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(8), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(9), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(14), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(12), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(13), 32768),
	Insn('0x4C', Char(8), -1),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('0x4C', Char(11), -1),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG2_UNSET', Char(11), 32768),
	Insn('0x4C', Char(10), -1),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('FLAG_SET', Flag(1343)),
	Insn('0xC7', b'\x01\x00\x10\x00\x00'),
	Insn('FORK_QUIT', Char(35), 1),
	Insn('SOUND_STOP', 803),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][33] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('SOUND_LOAD', 803),
	Insn('CAM_OFFSET', (-1000, 2500, 11000), 0),
	Insn('CAM_ROTATE', 23, 6, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 34500, 0),
	Insn('CHAR_SET_POS', Char(257), (-24800, -8200, -23800), 270),
	Insn('CHAR_SET_POS', Char(258), (-24000, -8200, -24600), 270),
	Insn('CHAR_SET_POS', Char(259), (-22400, -8200, -23800), 270),
	Insn('CHAR_SET_POS', Char(260), (-21600, -8200, -24600), 270),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_SET', Char(15), 128),
	Insn('CHAR_FLAG2_SET', Char(15), 32768),
	Insn('CHAR_FLAG1_SET', Char(16), 128),
	Insn('CHAR_FLAG2_SET', Char(16), 32768),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('CHAR_FLAG1_SET', Char(31), 32768),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_FLAG1_SET', Char(33), 32768),
	Insn('CHAR_FLAG1_SET', Char(34), 32768),
	Insn('CHAR_SET_CHCP', Char(30), 0),
	Insn('CHAR_SET_FRAME', Char(30), 0),
	Insn('0x4B', Char(30), -1),
	Insn('CHAR_SET_POS', Char(30), (9000, 0, 5000), 180),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('CHAR_SET_CHCP', Char(31), 3),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_SET_POS', Char(31), (-9300, 0, -7200), 0),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_CHCP', Char(32), 2),
	Insn('CHAR_SET_FRAME', Char(32), 0),
	Insn('CHAR_SET_POS', Char(32), (-9700, 0, -5500), 180),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_CHCP', Char(33), 15),
	Insn('CHAR_SET_FRAME', Char(33), 0),
	Insn('0x4B', Char(33), -1),
	Insn('CHAR_SET_POS', Char(33), (-14500, 0, -500), 90),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_CHCP', Char(34), 5),
	Insn('CHAR_SET_FRAME', Char(34), 0),
	Insn('0x4B', Char(34), -1),
	Insn('CHAR_SET_POS', Char(34), (-15500, 0, 1000), 90),
	Insn('CHAR_FLAG1_UNSET', Char(34), 128),
	Insn('CHAR_FLAG2_UNSET', Char(34), 32768),
	Insn('SLEEP', 1000),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}之后过了三周──{wait}'
		'{page}'
		'琪雅的记忆完全没有恢复的迹象，\n'
		'而游击士协会的情报网\n'
		'最后也没有什么发现。{wait}'
		'{page}'
		'创立纪念庆典结束，\n'
		'距离市长选举还有数个月，\n'
		'相对平静的生活一天天过去……{wait}'
		'{page}'
		'罗伊德等人已经完全习惯了\n'
		'与琪雅一同生活，\n'
		'同时也重新开始处理日常公务。{wait}'
		'{page}'
		'而琪雅似乎也理解了\n'
		'罗伊德等人需要工作，\n'
		'不再任性，而是乖乖留下来看家。{wait}'
		'{page}'
		'之后──{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('BGM_PLAY', b'\xc9\x00\x00'),
	Insn('0xB8', 100, 201),
	Insn('FORK', 30, 1, [
		Insn('0x9E', Char(254), 0, 5000, 180000, 2500, b'\x01\x00'),
	]),
	Insn('FORK', 33, 1, [
		Insn('0x98', Char(254), (10000, 0, 12000), 1500, 0),
	]),
	Insn('FORK', 34, 1, [
		Insn('0x98', Char(254), (10000, 0, 12000), 1500, 0),
	]),
	Insn('CAM_OFFSET', (-1000, 1500, 11000), 5000),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 38))),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('SLEEP', 4750),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 34))),
	Insn('SLEEP', 150),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 35))),
	Insn('SLEEP', 50),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 36))),
	Insn('SLEEP', 50),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 37))),
	Insn('0x6F', b'\x01'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-25800, -7600, -16800), 0),
	Insn('CAM_ROTATE', 35, 12, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('CAM_DISTANCE', 20500, 4000),
	Insn('SLEEP', 3000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('FORK_QUIT', Char(257), 255),
	Insn('FORK_QUIT', Char(258), 255),
	Insn('FORK_QUIT', Char(259), 255),
	Insn('FORK_QUIT', Char(260), 255),
	Insn('FORK_AWAIT', Char(35), 1),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('SOUND_STOP', 803),
	Insn('FLAG_SET', Flag(748)),
	Insn('NEW_SCENE', 'c0110', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][34] = [
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-28400, -8200, -23800), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-28400, -8200, -22300), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('OBJ_FLAG_UNSET', Object(0), 16),
	Insn('0x71', Object(0), b'\x00\x00', 10, 0),
	Insn('0x79', b'\x00\x00'),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-28400, -8200, -20300), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('RETURN'),
]

data['code'][35] = [
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (-28800, -8200, -24000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (-28800, -8200, -20300), 2000, 0),
	]),
	Insn('SLEEP', 1500),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('RETURN'),
]

data['code'][36] = [
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (-28400, -8200, -23800), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (-28400, -8200, -20300), 2000, 0),
	]),
	Insn('SLEEP', 1500),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('RETURN'),
]

data['code'][37] = [
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (-28800, -8200, -24000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (-28800, -8200, -20300), 2000, 0),
	]),
	Insn('SLEEP', 1500),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('RETURN'),
]

data['code'][38] = [
	Insn('SOUND_PLAY', 803, 0, 2, 100),
	Insn('SLEEP', 7000),
	Insn('SOUND_LOOP', 803, 90),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 80),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 70),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 60),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 50),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 40),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 30),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 20),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 10),
	Insn('SLEEP', 200),
	Insn('SOUND_STOP', 803),
	Insn('RETURN'),
]

data['code'][39] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (-28700, -7200, -21900), 0),
	Insn('CAM_ROTATE', 50, 27, 0, 0),
	Insn('0x6E', 550, 0),
	Insn('CAM_DISTANCE', 17500, 0),
	Insn('CHAR_SET_POS', Char(257), (-28700, -8200, -19500), 180),
	Insn('CHAR_SET_POS', Char(258), (-28700, -8200, -19500), 180),
	Insn('CHAR_SET_POS', Char(259), (-28700, -8200, -19500), 180),
	Insn('CHAR_SET_POS', Char(260), (-28700, -8200, -19500), 180),
	Insn('CHAR_SET_POS', Char(265), (-28700, -8200, -19500), 180),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(265), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(4), 128),
	Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('OBJ_FLAG_UNSET', Object(0), 16),
	Insn('0x71', Object(0), b'\x00\x00', 10, 0),
	Insn('0x79', b'\x00\x00'),
	Insn('CAM_OFFSET', (-28700, -7200, -24900), 6000),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 40))),
	Insn('SLEEP', 700),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 41))),
	Insn('SLEEP', 700),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 43))),
	Insn('SLEEP', 700),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 42))),
	Insn('SLEEP', 1500),
	Insn('FORK', 265, 1, [
		Insn('0x95', Char(254), (-28700, -8200, -23500), 2000, 0),
	]),
	Insn('FORK', 265, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 1500),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('0x71', Object(0), b'\n\x00', 0, 0),
	Insn('0x79', b'\x00\x00'),
	Insn('OBJ_FLAG_SET', Object(0), 16),
	Insn('FORK_AWAIT', Char(265), 1),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100236V#5P#0500F──警备队的车辆就\n'
		'停在城市的北出口。{wait}'
		'{page}'
		'#14100237V我想，只要是在自治州的范围之内，\n'
		'可以送大家去任何地方。\n'
		'如果有什么要求，请不要客气，随时告诉我。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1087)), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#14100238V#12P#0004F好的，明白了。{wait}'
				'{page}'
				'#14100239V#0000F所说的遗迹，应该就是\n'
				'位于山道隧道中部的\n'
				'岔路尽头的那个遗迹吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#14100240V#6P#0203F以前曾经去过那个遗迹的\n'
				'入口附近呢。{wait}'
				'{page}'
				'#14100241V#0200F但当时被警备队的\n'
				'路障封锁了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(807)), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#14100242V#12P#0004F好的，明白了。{wait}'
				'{page}'
				'#14100243V#0000F所说的遗迹，应该就是\n'
				'位于山道隧道中部的\n'
				'岔路尽头的那个遗迹吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#14100244V#6P#0202F和矿山镇不是同一个\n'
				'方向呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#14100245V#12P#0004F好的，明白了。{wait}'
				'{page}'
				'#14100246V#0000F所说的遗迹，应该就是\n'
				'位于山道隧道中部的\n'
				'岔路尽头的那个遗迹吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#14100247V#6P#0202F确实，在隧道的中段部分\n'
				'有条很狭窄的岔路呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100248V#5P#0500F嗯，那边的道路比较险峻，\n'
		'所以从隧道的中段开始\n'
		'就要徒步行进了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100249V#11P#0309F那么，把手头的事情都办完之后，\n'
		'就前往山道的隧道吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100250V#12P#0108F（……呼，\n'
		'\u3000幽灵出没的遗迹吗……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(0), (-28700, -8200, -25000), 90),
	Insn('CHAR_FLAG1_SET', Char(4), 128),
	Insn('CHAR_FLAG2_SET', Char(4), 32768),
	Insn('FLAG_SET', Flag(1536)),
	Insn('CHAR_FLAG1_UNSET', Char(20), 128),
	Insn('CHAR_FLAG1_UNSET', Char(21), 128),
	Insn('CHAR_FLAG1_SET', Char(16), 128),
	Insn('QUEST', 72, Insn('TASK_SET', 9)),
	Insn('QUEST', 73, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 73, Insn('TASK_SET', 0)),
	Insn('0xD0', 1, Expr([Insn('CONST', 5), Insn('SET'), Insn('END')])),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][40] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-28700, -8200, -23000), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (-28100, -8200, -26000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 2, [
		Insn('0x92', Char(254), -28700, -23500, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 2),
	Insn('RETURN'),
]

data['code'][41] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-28700, -8200, -23000), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (-29400, -8200, -26000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 2, [
		Insn('0x92', Char(254), -28700, -23500, 500),
	]),
	Insn('FORK_AWAIT', Char(258), 2),
	Insn('RETURN'),
]

data['code'][42] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-28700, -8200, -23000), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (-30400, -8200, -25300), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 2, [
		Insn('0x92', Char(254), -28700, -23500, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 2),
	Insn('RETURN'),
]

data['code'][43] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-28700, -8200, -23000), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (-27000, -8200, -25300), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 2, [
		Insn('0x92', Char(254), -28700, -23500, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('RETURN'),
]

data['code'][44] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50109', 30),
	Insn('SOUND_LOAD', 803),
	Insn('CAM_OFFSET', (-1000, 2500, 11000), 0),
	Insn('CAM_ROTATE', 23, 6, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 34500, 0),
	Insn('CHAR_SET_POS', Char(257), (1000, 0, -16800), 90),
	Insn('CHAR_SET_POS', Char(258), (1000, 0, -15600), 90),
	Insn('CHAR_SET_POS', Char(259), (-200, 0, -16800), 90),
	Insn('CHAR_SET_POS', Char(260), (-200, 0, -15600), 90),
	Insn('CHAR_SET_POS', Char(265), (3200, 0, -16200), 270),
	Insn('CHAR_FLAG1_UNSET', Char(4), 128),
	Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
	Insn('0x78', b'\x0b', Char(24)),
	Insn('OBJ_FLAG_SET', Object(11), 4096),
	Insn('OBJ_SET_FRAME', Object(11), 'light', Insn('0', 1)),
	Insn('OBJ_FLAG_UNSET', Object(11), 4),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 4),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(24), (6000, 0, -16200), 0),
	Insn('0xD3', Char(24), 0, 0, 0, 0),
	Insn('0x74', Object(11), 7680),
	Insn('0x70', Object(11), b'\x00\x00'),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('CHAR_FLAG1_SET', Char(31), 32768),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_FLAG1_SET', Char(33), 32768),
	Insn('CHAR_FLAG1_SET', Char(34), 32768),
	Insn('CHAR_SET_CHCP', Char(30), 0),
	Insn('CHAR_SET_FRAME', Char(30), 0),
	Insn('0x4B', Char(30), -1),
	Insn('CHAR_SET_POS', Char(30), (0, 0, -5000), 270),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('CHAR_SET_CHCP', Char(31), 3),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_SET_POS', Char(31), (-9300, 0, -7200), 0),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_CHCP', Char(32), 2),
	Insn('CHAR_SET_FRAME', Char(32), 0),
	Insn('CHAR_SET_POS', Char(32), (-9700, 0, -5500), 180),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_CHCP', Char(33), 15),
	Insn('CHAR_SET_FRAME', Char(33), 0),
	Insn('0x4B', Char(33), -1),
	Insn('CHAR_SET_POS', Char(33), (-4500, 0, 11500), 270),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_CHCP', Char(34), 5),
	Insn('CHAR_SET_FRAME', Char(34), 0),
	Insn('0x4B', Char(34), -1),
	Insn('CHAR_SET_POS', Char(34), (-5500, 0, 13000), 270),
	Insn('CHAR_FLAG1_UNSET', Char(34), 128),
	Insn('CHAR_FLAG2_UNSET', Char(34), 32768),
	Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xd5\x8f{', 38, 120, 0),
	Insn('OBJ_SET_FRAME', Object(255), 'sky', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'sky1', Insn('1', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'sd_mul', Insn('0', 1)),
	Insn('FORK', 30, 1, [
		Insn('0x9E', Char(254), 0, 5000, -180000, 2500, b'\x01\x00'),
	]),
	Insn('FORK', 33, 1, [
		Insn('0x98', Char(254), (-10000, 0, -12000), 1500, 0),
	]),
	Insn('FORK', 34, 1, [
		Insn('0x98', Char(254), (-10000, 0, -12000), 1500, 0),
	]),
	Insn('CAM_OFFSET', (-1000, 1500, 11000), 5000),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 28))),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (2700, 900, -14200), 0),
	Insn('CAM_ROTATE', 50, 21, 0, 0),
	Insn('0x6E', 550, 0),
	Insn('CAM_DISTANCE', 18000, 0),
	Insn('CAM_OFFSET', (2700, 900, -16200), 3000),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100559V#11P#0509F──今天真是\n'
		'非常感谢！{wait}'
		'{page}'
		'#14100560V#0502F这份恩情，我一定会\n'
		'尽早回报的！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100561V#6P#0002F哈哈，太夸张啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100562V#0304F#6P呵呵，我们也经历了一次\n'
		'很有趣的体验啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100563V#0106F#6P关于那个遗迹──\n'
		'『僧院』……{wait}'
		'{page}'
		'#14100564V#0108F还是去和克洛斯贝尔\n'
		'大教堂的人商谈一下\n'
		'比较好吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14100565V#6P#0206F……是啊。{wait}'
		'{page}'
		'#14100566V如果涉及到古代遗物的话，\n'
		'我们也就无能为力了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100567V#11P#0503F这样啊……{wait}'
		'{page}'
		'#14100568V#0500F明白了，那我先去和副司令商讨\n'
		'相关对策。{wait}'
		'{page}'
		'#14100569V#0505F各位……\n'
		'接下来还要继续在市内探问情报吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100570V#6P#0004F嗯，准备至少去赌场\n'
		'调查一下。{wait}'
		'{page}'
		'#14100571V#0000F如果你们警备队\n'
		'有了那方面的情报，就请与\n'
		'我们进行联系吧，可以吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100572V#11P#0500F明白了，\n'
		'是有关矿山镇的冈兹先生对吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(265), 30),
	Insn('CHAR_SET_FRAME', Char(265), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100573V#2P#0502F#11P那我就先告辞了。\n'
		'各位，辛苦了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100574V#0302F#6P噢，彼此彼此，你也是啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_CHCP', Char(265), 255),
	Insn('CHAR_SET_FRAME', Char(265), 0),
	Insn('0x92', Char(265), 3700, -16700, 500),
	Insn('FORK', 265, 1, [
		Insn('0x96', Char(254), (3700, 0, -16700), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(265), 1),
	Insn('CHAR_ROTATE', Char(265), 90, 500),
	Insn('0x71', Object(11), b'\x01\x00', 30, 0),
	Insn('SOUND_PLAY', 464, 0, 0, 100),
	Insn('0x79', b'\x0b\x00'),
	Insn('CHAR_FLAG1_SET', Char(265), 4),
	Insn('FORK', 265, 1, [
		Insn('0x96', Char(254), (4700, 500, -16700), 2000, 0),
	]),
	Insn('FORK', 265, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(265), 1),
	Insn('CHAR_FLAG1_UNSET', Char(265), 4),
	Insn('0x71', Object(11), b'\x1f\x00', 60, 0),
	Insn('SOUND_PLAY', 463, 0, 0, 100),
	Insn('0x79', b'\x0b\x00'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (6000, 1000, -16200), 0),
	Insn('CAM_ROTATE', 25, 19, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 17500, 0),
	Insn('SOUND_PLAY', 470, 0, 0, 100),
	Insn('0x71', Object(11), b'<\x00', 90, 0),
	Insn('0x79', b'\x0b\x00'),
	Insn('0x71', Object(11), b'y\x00', 180, 32),
	Insn('CAM_OFFSET', (12000, 1000, -4400), 4000),
	Insn('CAM_ROTATE', 60, 11, 0, 4000),
	Insn('CAM_DISTANCE', 19500, 4000),
	Insn('SOUND_PLAY', 486, 0, 0, 100),
	Insn('FORK', 24, 1, [
		Insn('0x96', Char(254), (6000, 0, -9200), 4000, 0),
	]),
	Insn('SLEEP', 1500),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('SOUND_PLAY', 471, 0, 0, 100),
	Insn('FORK', 24, 1, [
		Insn('0x9E', Char(254), 12000, -9200, 90000, 4000, b'\x01\x00'),
	]),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('FORK', 24, 1, [
		Insn('0x98', Char(254), (40000, 0, 0), 6000, 0),
	]),
	Insn('SLEEP', 3000),
	Insn('0x6F', b'y'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (400, 1000, -16200), 0),
	Insn('CAM_ROTATE', 55, 21, 0, 0),
	Insn('0x6E', 550, 0),
	Insn('CAM_DISTANCE', 18000, 0),
	Insn('FORK_QUIT', Char(24), 1),
	Insn('CHAR_FLAG1_SET', Char(24), 128),
	Insn('CHAR_FLAG1_UNSET', Char(24), 32768),
	Insn('OBJ_FLAG_UNSET', Object(11), 4096),
	Insn('OBJ_FLAG_SET', Object(11), 4),
	Insn('0x0D'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 315, 500),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100575V#0000F那么……\n'
		'已经没有多少时间了，\n'
		'现在就直接去赌场吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x62', Char(258)),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100576V#5P#0100F嗯，必须去收集那位叫冈兹的\n'
		'矿工的情报呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100577V#0309F那咱们就赶快去\n'
		'欢乐街那边吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 18500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('MINIGAME', 24, 0, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
	Insn('0xBA', 8),
	Insn('PARTY_CLEAR'),
	Insn('0x2E', b'\x00\xff\xff'),
	Insn('0x2E', b'\x01\xff\xff'),
	Insn('0x2E', b'\x02\xff\xff'),
	Insn('0x2E', b'\x03\xff\xff'),
	Insn('FLAG_SET', Flag(1548)),
	Insn('0xD0', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('QUEST', 74, Insn('TASK_SET', 3)),
	Insn('FORK_QUIT', Char(35), 1),
	Insn('SOUND_STOP', 803),
	Insn('FLAG_SET', Flag(738)),
	Insn('NEW_SCENE', 'c0400', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][45] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch28100', 30),
	Insn('LOAD_CHCP', 'chr/ch21200', 31),
	Insn('LOAD_CHCP', 'chr/ch21400', 32),
	Insn('LOAD_CHCP', 'chr/ch20000', 33),
	Insn('LOAD_CHCP', 'chr/ch23600', 34),
	Insn('CAM_OFFSET', (-1000, 2500, 11000), 0),
	Insn('CAM_ROTATE', 23, 6, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 34500, 0),
	Insn('CHAR_SET_POS', Char(0), (-19000, -4200, -11700), 0),
	Insn('CHAR_SET_POS', Char(1), (-19000, -4200, -11700), 0),
	Insn('CHAR_SET_POS', Char(2), (-19000, -4200, -11700), 0),
	Insn('CHAR_SET_POS', Char(3), (-19000, -4200, -11700), 0),
	Insn('0x7D', b'\xff\xff\xff\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xb4\xd7\xe6', 15, 130, 0),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 128),
	Insn('CHAR_FLAG2_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 128),
	Insn('0x78', b'\t', Char(24)),
	Insn('OBJ_FLAG_SET', Object(9), 4096),
	Insn('OBJ_FLAG_UNSET', Object(9), 4),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 4),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(24), (15000, 0, -3000), 0),
	Insn('0xD3', Char(24), 0, 270000, 0, 0),
	Insn('0x70', Object(9), b'\x00\x00'),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('CHAR_FLAG1_SET', Char(31), 32768),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_FLAG1_SET', Char(33), 32768),
	Insn('CHAR_FLAG1_SET', Char(34), 32768),
	Insn('CHAR_SET_CHCP', Char(30), 30),
	Insn('CHAR_SET_FRAME', Char(30), 0),
	Insn('0x4B', Char(30), -1),
	Insn('CHAR_SET_POS', Char(30), (-15000, 0, -6300), 90),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('CHAR_SET_CHCP', Char(31), 31),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_SET_POS', Char(31), (-6800, 0, 4000), 270),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_CHCP', Char(32), 32),
	Insn('CHAR_SET_FRAME', Char(32), 0),
	Insn('CHAR_SET_POS', Char(32), (-8300, 0, 2500), 90),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_CHCP', Char(33), 33),
	Insn('CHAR_SET_FRAME', Char(33), 0),
	Insn('0x4B', Char(33), -1),
	Insn('CHAR_SET_POS', Char(33), (-19300, 0, 19400), 180),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_CHCP', Char(34), 34),
	Insn('CHAR_SET_FRAME', Char(34), 0),
	Insn('0x4B', Char(34), -1),
	Insn('CHAR_SET_POS', Char(34), (7000, 0, 12000), 0),
	Insn('CHAR_FLAG1_UNSET', Char(34), 128),
	Insn('CHAR_FLAG2_UNSET', Char(34), 32768),
	Insn('FORK', 30, 1, [
		Insn('0x96', Char(254), (5000, 0, -6300), 2000, 0),
	]),
	Insn('FORK', 33, 1, [
		Insn('0x98', Char(254), (10000, 0, -10000), 1500, 0),
	]),
	Insn('FORK', 34, 1, [
		Insn('0x9E', Char(254), 0, 5000, 180000, 2500, b'\x01\x00'),
	]),
	Insn('SOUND_PLAY', 458, 0, 0, 100),
	Insn('FORK', 24, 1, [
		Insn('0x96', Char(254), (-26000, 1000, -3000), 6000, 0),
	]),
	Insn('0x71', Object(9), b'y\x00', 180, 32),
	Insn('CAM_OFFSET', (-1000, 1500, 11000), 5000),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 19))),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-25800, -7600, -16800), 0),
	Insn('CAM_ROTATE', 35, 12, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('CAM_DISTANCE', 20500, 4000),
	Insn('SLEEP', 3000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('FORK_QUIT', Char(35), 1),
	Insn('FLAG_SET', Flag(749)),
	Insn('NEW_SCENE', 'c0110', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][46] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch28100', 30),
	Insn('LOAD_CHCP', 'chr/ch21200', 31),
	Insn('LOAD_CHCP', 'chr/ch21400', 32),
	Insn('LOAD_CHCP', 'chr/ch20000', 33),
	Insn('LOAD_CHCP', 'chr/ch23600', 34),
	Insn('CAM_OFFSET', (-1000, 2500, 11000), 0),
	Insn('CAM_ROTATE', 23, 6, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 34500, 0),
	Insn('CHAR_SET_POS', Char(0), (-19000, -4200, -11700), 0),
	Insn('CHAR_SET_POS', Char(1), (-19000, -4200, -11700), 0),
	Insn('CHAR_SET_POS', Char(2), (-19000, -4200, -11700), 0),
	Insn('CHAR_SET_POS', Char(3), (-19000, -4200, -11700), 0),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 128),
	Insn('CHAR_FLAG2_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_SET', Char(16), 128),
	Insn('CHAR_FLAG2_SET', Char(16), 32768),
	Insn('0x7D', b'\xff\xff\xff\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xb4\xd7\xe6', 15, 130, 0),
	Insn('CHAR_FLAG1_UNSET', Char(24), 128),
	Insn('0x78', b'\t', Char(24)),
	Insn('OBJ_FLAG_SET', Object(9), 4096),
	Insn('OBJ_FLAG_UNSET', Object(9), 4),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 4),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(24), (15000, 0, -3000), 0),
	Insn('0xD3', Char(24), 0, 270000, 0, 0),
	Insn('0x70', Object(9), b'\x00\x00'),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('CHAR_FLAG1_SET', Char(31), 32768),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_FLAG1_SET', Char(33), 32768),
	Insn('CHAR_FLAG1_SET', Char(34), 32768),
	Insn('CHAR_SET_CHCP', Char(30), 30),
	Insn('CHAR_SET_FRAME', Char(30), 0),
	Insn('0x4B', Char(30), -1),
	Insn('CHAR_SET_POS', Char(30), (-15000, 0, -6300), 90),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('CHAR_SET_CHCP', Char(31), 31),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_SET_POS', Char(31), (-6800, 0, 4000), 270),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_CHCP', Char(32), 32),
	Insn('CHAR_SET_FRAME', Char(32), 0),
	Insn('CHAR_SET_POS', Char(32), (-8300, 0, 2500), 90),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_CHCP', Char(33), 33),
	Insn('CHAR_SET_FRAME', Char(33), 0),
	Insn('0x4B', Char(33), -1),
	Insn('CHAR_SET_POS', Char(33), (-19300, 0, 19400), 180),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_CHCP', Char(34), 34),
	Insn('CHAR_SET_FRAME', Char(34), 0),
	Insn('0x4B', Char(34), -1),
	Insn('CHAR_SET_POS', Char(34), (7000, 0, 12000), 0),
	Insn('CHAR_FLAG1_UNSET', Char(34), 128),
	Insn('CHAR_FLAG2_UNSET', Char(34), 32768),
	Insn('SLEEP', 1000),
	Insn('0xC7', b'\x00\x00\x08\x00\x00'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{0x18}{color 0}#1K翌日，８：００──{wait}'
	)),
	Insn('SLEEP', 2500),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0xC7', b'\x01\x00\x08\x00\x00'),
	Insn('BGM_PLAY', b'\x01\x00\x00'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
	Insn('FORK', 30, 1, [
		Insn('0x96', Char(254), (5000, 0, -6300), 2000, 0),
	]),
	Insn('FORK', 33, 1, [
		Insn('0x98', Char(254), (10000, 0, -10000), 1500, 0),
	]),
	Insn('FORK', 34, 1, [
		Insn('0x9E', Char(254), 0, 5000, 180000, 2500, b'\x01\x00'),
	]),
	Insn('FORK', 24, 1, [
		Insn('0x96', Char(254), (-26000, 1000, -3000), 6000, 0),
	]),
	Insn('SOUND_PLAY', 458, 0, 0, 100),
	Insn('0x71', Object(9), b'y\x00', 180, 32),
	Insn('CAM_OFFSET', (-1000, 1500, 11000), 5000),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 19))),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-25800, -7600, -16800), 0),
	Insn('CAM_ROTATE', 35, 12, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('CAM_DISTANCE', 20500, 4000),
	Insn('SLEEP', 3000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('FLAG_SET', Flag(750)),
	Insn('NEW_SCENE', 'c0110', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][47] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('SOUND_LOAD', 803),
	Insn('CAM_OFFSET', (-1000, 2500, 11000), 0),
	Insn('CAM_ROTATE', 23, 6, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 34500, 0),
	Insn('CHAR_SET_POS', Char(0), (-19000, -4200, -11700), 0),
	Insn('CHAR_SET_POS', Char(1), (-19000, -4200, -11700), 0),
	Insn('CHAR_SET_POS', Char(2), (-19000, -4200, -11700), 0),
	Insn('CHAR_SET_POS', Char(3), (-19000, -4200, -11700), 0),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('CHAR_FLAG1_SET', Char(31), 32768),
	Insn('CHAR_FLAG1_SET', Char(32), 32768),
	Insn('CHAR_FLAG1_SET', Char(33), 32768),
	Insn('CHAR_FLAG1_SET', Char(34), 32768),
	Insn('CHAR_SET_CHCP', Char(30), 0),
	Insn('CHAR_SET_FRAME', Char(30), 0),
	Insn('0x4B', Char(30), -1),
	Insn('CHAR_SET_POS', Char(30), (0, 0, -5000), 270),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('CHAR_SET_CHCP', Char(31), 3),
	Insn('CHAR_SET_FRAME', Char(31), 0),
	Insn('CHAR_SET_POS', Char(31), (-9300, 0, -7200), 0),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('CHAR_SET_CHCP', Char(32), 2),
	Insn('CHAR_SET_FRAME', Char(32), 0),
	Insn('CHAR_SET_POS', Char(32), (-9700, 0, -5500), 180),
	Insn('CHAR_FLAG1_UNSET', Char(32), 128),
	Insn('CHAR_FLAG2_UNSET', Char(32), 32768),
	Insn('CHAR_SET_CHCP', Char(33), 15),
	Insn('CHAR_SET_FRAME', Char(33), 0),
	Insn('0x4B', Char(33), -1),
	Insn('CHAR_SET_POS', Char(33), (-4500, 0, 11500), 270),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_CHCP', Char(34), 5),
	Insn('CHAR_SET_FRAME', Char(34), 0),
	Insn('0x4B', Char(34), -1),
	Insn('CHAR_SET_POS', Char(34), (-5500, 0, 13000), 270),
	Insn('CHAR_FLAG1_UNSET', Char(34), 128),
	Insn('CHAR_FLAG2_UNSET', Char(34), 32768),
	Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xd5\x8f{', 38, 120, 0),
	Insn('OBJ_SET_FRAME', Object(255), 'sky', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'sky1', Insn('1', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'sd_mul', Insn('0', 1)),
	Insn('SLEEP', 1000),
	Insn('0xC7', b'\x00\x00\x08\x00\x00'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{0x18}{color 0}#1K同日，１７：００──{wait}'
	)),
	Insn('SLEEP', 2500),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0xC7', b'\x01\x00\x08\x00\x00'),
	Insn('BGM_PLAY', b'd\x00\x00'),
	Insn('FORK', 30, 1, [
		Insn('0x9E', Char(254), 0, 5000, -180000, 2500, b'\x01\x00'),
	]),
	Insn('FORK', 33, 1, [
		Insn('0x98', Char(254), (-10000, 0, -12000), 1500, 0),
	]),
	Insn('FORK', 34, 1, [
		Insn('0x98', Char(254), (-10000, 0, -12000), 1500, 0),
	]),
	Insn('CAM_OFFSET', (-1000, 1500, 11000), 5000),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 28))),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-25800, -600, -16800), 0),
	Insn('CAM_ROTATE', 35, 12, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 23500, 0),
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
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 128),
	Insn('CHAR_FLAG2_SET', Char(14), 32768),
	Insn('CAM_DISTANCE', 20500, 4000),
	Insn('SLEEP', 3000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('FLAG_UNSET', Flag(13)),
	Insn('FORK_QUIT', Char(35), 1),
	Insn('SOUND_STOP', 803),
	Insn('FLAG_SET', Flag(751)),
	Insn('NEW_SCENE', 'c0110', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][48] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1037)), Insn('FLAG', Flag(1038)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('CALL', Function((0, 54))),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (4240, 0, -20650), 0),
			Insn('EVENT_END', 4),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('FLAG', Flag(609)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('CALL', Function((0, 53))),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (4240, 0, -20650), 0),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][49] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1037)), Insn('FLAG', Flag(1038)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('CALL', Function((0, 54))),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (16840, 0, -3910), 270),
			Insn('EVENT_END', 4),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('FLAG', Flag(609)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('CALL', Function((0, 53))),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (16840, 0, -3910), 270),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][50] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1037)), Insn('FLAG', Flag(1038)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('CALL', Function((0, 54))),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (13060, 0, 27590), 180),
			Insn('EVENT_END', 4),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('FLAG', Flag(609)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('CALL', Function((0, 53))),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (13060, 0, 27590), 180),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][51] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(526)), Insn('FLAG', Flag(609)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('CALL', Function((0, 53))),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-13380, 0, 14530), 135),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][52] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1037)), Insn('FLAG', Flag(1038)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('CALL', Function((0, 54))),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-26950, -1160, -4340), 90),
			Insn('EVENT_END', 4),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('FLAG', Flag(609)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('CALL', Function((0, 53))),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-26950, -1160, -4340), 90),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][53] = [
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F啊……还是先去\n'
		'导力商店看看吧。{wait}'
		'{page}'
		'#0000F就是街角的那个建筑。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F了解。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('ATTR', 10), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F了解，这就走吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('ATTR', 10), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F是啊，那我们就去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][54] = [
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F今天已经很累了啊……\n'
		'别绕远路了，径直回支援课吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][55] = [
	Insn('SOUND_LOOP', 803, 0),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 10),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 20),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 30),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 40),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 50),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 60),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 70),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 80),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 90),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 803, 100),
	Insn('RETURN'),
]

data['code'][56] = [
	Insn('SOUND_LOOP', 803, 100),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 90),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 80),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 70),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 60),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 50),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 40),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 30),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 20),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 10),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 803, 0),
	Insn('SOUND_STOP', 803),
	Insn('RETURN'),
]
