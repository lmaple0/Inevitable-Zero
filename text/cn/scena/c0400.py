# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'c0400',
	'name2': 'c0400',
	'location': 34,
	'bgm': 113,
	'flags': 8192,
	'includes': [
		None,
		None,
		None,
		None,
		None,
		None,
	],
	'name3': 'c0400',
	'labels': [
		{
			'pos': (90.5999984741211, 0.0, -111.88999938964844),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('中央广场'),
		},
		{
			'pos': (-19.209999084472656, 0.0, -104.37999725341797),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('西侧大道'),
		},
		{
			'pos': (135.69000244140625, 0.0, 36.7400016784668),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('行政区'),
		},
		{
			'pos': (-121.08000183105469, 0.0, 20.040000915527344),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('住宅区'),
		},
		{
			'pos': (0.8399999737739563, 0.0, 6.679999828338623),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('欢乐街'),
		},
		{
			'pos': (226.2899932861328, 0.0, -150.3000030517578),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('东侧大道'),
		},
		{
			'pos': (285.57000732421875, 0.0, -242.14999389648438),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('旧市街'),
		},
		{
			'pos': (273.04998779296875, 0.0, -40.08000183105469),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('港湾区'),
		},
		{
			'pos': (229.6300048828125, 0.0, 116.9000015258789),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('ＩＢＣ'),
		},
		{
			'pos': (109.38999938964844, 0.0, -227.1199951171875),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('站前大道'),
		},
		{
			'pos': (30.899999618530273, 0.0, -53.439998626708984),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('小巷'),
		},
		{
			'pos': (104.37999725341797, 0.0, -278.8900146484375),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('乌尔斯拉小径'),
		},
		{
			'pos': (316.4700012207031, 0.0, -126.91999816894531),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('东克洛斯贝尔街道'),
		},
		{
			'pos': (-104.37999725341797, 0.0, -106.87999725341797),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('西克洛斯贝尔街道'),
		},
		{
			'pos': (-94.36000061035156, 0.0, 60.119998931884766),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('玛因兹山道'),
		},
		{
			'pos': (53.86000061035156, 0.0, -135.27000427246094),
			'unk': b'\x00\x00Q\x00',
			'name': Translate(''),
		},
		{
			'pos': (143.6199951171875, 0.0, -91.8499984741211),
			'unk': b'\x00\x00T\x00',
			'name': Translate(''),
		},
		{
			'pos': (94.7699966430664, 0.0, -148.6300048828125),
			'unk': b'\x00\x00W\x00',
			'name': Translate(''),
		},
		{
			'pos': (52.61000061035156, 0.0, -86.83999633789062),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (86.83999633789062, 0.0, -46.7599983215332),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (2.0899999141693115, 0.0, -95.19000244140625),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-14.199999809265137, 0.0, -60.119998931884766),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (25.889999389648438, 0.0, -6.679999828338623),
			'unk': b'\x00\x00R\x00',
			'name': Translate(''),
		},
		{
			'pos': (33.81999969482422, 0.0, -28.389999389648438),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (48.43000030517578, 0.0, -42.59000015258789),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (96.02999877929688, 0.0, 75.98999786376953),
			'unk': b'\x00\x00Q\x00',
			'name': Translate(''),
		},
		{
			'pos': (283.07000732421875, 0.0, -150.3000030517578),
			'unk': b'\x00\x00R\x00',
			'name': Translate(''),
		},
		{
			'pos': (254.67999267578125, 0.0, -301.44000244140625),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (232.97000122070312, 0.0, -270.5400085449219),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (109.38999938964844, 0.0, -131.92999267578125),
			'unk': b'\x00\x00V\x00',
			'name': Translate(''),
		},
	],
	'chcp': [
		'chr/ch20400',
		'chr/ch36300',
		'chr/ch21900',
		'chr/ch34500',
		'chr/ch25900',
		'chr/ch27100',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch30600',
		'chr/ch29300',
		'chr/ch00600',
		'chr/ch00700',
		'chr/ch08700',
		'chr/ch00102',
		'chr/ch24400',
	],
	'npcs': [
		{
			'name': Translate('苏菲尤'),
			'pos': (-10750, 1759, 24469),
			'angle': 175,
			'_1': b'\x05\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 8)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('揽客人员皮姆'),
			'pos': (4360, 0, -10960),
			'angle': 310,
			'_1': b'\x05\x01\x00\x00\x04\x00\x00\x01',
			'function': Function((0, 12)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('宝莉榭'),
			'pos': (379, 1769, 28049),
			'angle': 315,
			'_1': b'\x05\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('塔普'),
			'pos': (1830, 1769, 27899),
			'angle': 315,
			'_1': b'\x05\x01\x00\x00\x0e\x00\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('拉曼妲'),
			'pos': (-50000, 9, 12069),
			'angle': 220,
			'_1': b'\x01\x01\x00\x00\x02\x00\x00\x02',
			'function': Function((0, 16)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('特裘'),
			'pos': (15439, 0, 10340),
			'angle': 45,
			'_1': b'\x05\x01\x00\x00\x00\x00\x00\x03',
			'function': Function((0, 17)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('兔女郎'),
			'pos': (-22049, 0, 12489),
			'angle': 175,
			'_1': b'\x05\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 18)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('凯特巡警'),
			'pos': (-2380, 1990, 18079),
			'angle': 225,
			'_1': b'\x85\x01\x00\x00\x08\x00\x00\x04',
			'function': Function((0, 19)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('罗伯兹主任'),
			'pos': (-9439, 1759, 22709),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\t\x00\x00\x00',
			'function': Function((0, 20)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('艾丝蒂尔'),
			'pos': (-9149, 1759, 24250),
			'angle': 90,
			'_1': b'\x95\x01\x00\x00\n\x00\x00\x00',
			'function': Function((0, 21)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('约书亚'),
			'pos': (-7849, 1799, 23100),
			'angle': 315,
			'_1': b'\x95\x01\x00\x00\x0b\x00\x00\x00',
			'function': Function((0, 21)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('小滴'),
			'pos': (-7650, 1759, 24250),
			'angle': 270,
			'_1': b'\x95\x01\x00\x00\x0c\x00\x00\x00',
			'function': Function((0, 21)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('艾莉'),
			'pos': (-12699, 1899, 26899),
			'angle': 180,
			'_1': b'\x95\x01\x00\x00\r\x00\xff\xff',
			'function': Function((0, 25)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('麦克道尔市长'),
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
			'name': Translate('市长车'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
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
			'name': Translate('伊莉雅'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
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
		{
			'name': Translate('导游'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
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
			'pos': (-2.0, 19.0, 1.0),
			'range': 2626.5625,
			'transform': [
				0.04878048598766327,
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
				0.09756097197532654,
				-3.799999952316284,
				-0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 44)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (-2.0, 19.0, 1.0),
			'range': 2626.5625,
			'transform': [
				0.04878048598766327,
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
				0.09756097197532654,
				-3.799999952316284,
				-0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 46)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (-2.0, 35.0, 1.0),
			'range': 25.0,
			'transform': [
				0.19999998807907104,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.5,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.19999998807907104,
				0.0,
				0.3999999761581421,
				-17.5,
				-0.19999998807907104,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 60)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (-26.5, 16.739999771118164, -0.5),
			'range': 9.0,
			'transform': [
				0.3333333432674408,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.5,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000001788139343,
				0.0,
				8.833333969116211,
				-8.369999885559082,
				0.10000000894069672,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 61)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (-8.279999732971191, 24.030000686645508, 1.7599999904632568),
			'range': 1640.25,
			'transform': [
				0.07856739312410355,
				0.07856745272874832,
				-0.0,
				0.0,
				-0.07856745272874832,
				0.07856739312410355,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				2.5385138988494873,
				-1.237436056137085,
				-0.35199999809265137,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 22)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (7.0, 22.0, 1.0),
			'range': 612.5625,
			'transform': [
				0.222222238779068,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.09090909361839294,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				-1.5555557012557983,
				-2.0,
				-0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 44)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (7.0, 22.0, 1.0),
			'range': 612.5625,
			'transform': [
				0.222222238779068,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.09090909361839294,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				-1.5555557012557983,
				-2.0,
				-0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 46)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (-8160, 1770, 13680),
			'range': 4000,
			'bubble_pos': (-8160, 2270, 13680),
			'_1': b'|\x00\x00',
			'function': Function((0, 29)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (9850, 1760, 27000),
			'range': 3500,
			'bubble_pos': (9850, 3260, 27000),
			'_1': b'|\x00\x00',
			'function': Function((0, 30)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (16850, 0, 3030),
			'range': 3500,
			'bubble_pos': (16850, 1500, 3030),
			'_1': b'|\x00\x00',
			'function': Function((0, 31)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-7810, 1760, 24750),
			'range': 2500,
			'bubble_pos': (-7810, 3260, 24750),
			'_1': b'|\x00\x00',
			'function': Function((0, 32)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-4370, 0, 2950),
			'range': 3500,
			'bubble_pos': (-4370, 500, 2950),
			'_1': b'|\x00\x00',
			'function': Function((0, 33)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00"\x00', Function((0, 6)), Function((0, 7))),
	'code': [None]*65,
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
		Insn('CHAR_IDLE', Char(254), (3800, -4970), (6880, -8670), 1000),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_SET_POS', Char(254), (-50000, 10, 12070), 220),
		Insn('0x95', Char(254), (-18740, 10, 10280), 1500, 0),
		Insn('0x95', Char(254), (-2040, 1770, 9880), 1500, 0),
		Insn('0x95', Char(254), (30970, 0, 12150), 1500, 0),
		Insn('SLEEP', 1500),
		Insn('CHAR_SET_POS', Char(254), (30210, 0, 8600), 270),
		Insn('0x95', Char(254), (17210, 0, 8600), 1500, 0),
		Insn('0x95', Char(254), (15010, 0, 6790), 1500, 0),
		Insn('0x95', Char(254), (10210, 0, -960), 1500, 0),
		Insn('0x95', Char(254), (8450, 0, -7690), 1500, 0),
		Insn('0x95', Char(254), (10100, 0, -11960), 1500, 0),
		Insn('0x95', Char(254), (28170, 0, -38880), 1500, 0),
		Insn('SLEEP', 1500),
		Insn('CHAR_SET_POS', Char(254), (28170, 0, -38880), 315),
		Insn('0x95', Char(254), (9370, 0, -17000), 1500, 0),
		Insn('0x95', Char(254), (4280, 0, -11560), 1500, 0),
		Insn('0x95', Char(254), (-4810, 0, -3900), 1500, 0),
		Insn('0x95', Char(254), (-13140, 0, 1410), 1500, 0),
		Insn('0x95', Char(254), (-21060, 0, 5360), 1500, 0),
		Insn('0x95', Char(254), (-26790, 0, 8090), 1500, 0),
		Insn('0x95', Char(254), (-50000, 10, 12070), 1500, 0),
		Insn('SLEEP', 1500),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1035)), Insn('FLAG', Flag(1036)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
				Insn('0x95', Char(254), (4650, 0, 3100), 1000, 0),
				Insn('0x95', Char(254), (-450, 0, 800), 1000, 0),
				Insn('CHAR_ROTATE', Char(254), 281, 0),
				Insn('SLEEP', 1500),
				Insn('0x95', Char(254), (4150, 0, 3130), 1000, 0),
				Insn('0x95', Char(254), (11400, 0, 7650), 1000, 0),
				Insn('SLEEP', 1500),
			]),
		]),
		(None, [
			Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
				Insn('0x95', Char(254), (8780, 0, 6460), 1000, 0),
				Insn('0x95', Char(254), (2270, 0, 3060), 1000, 0),
				Insn('0x95', Char(254), (-5460, 0, 2360), 1000, 0),
				Insn('0x95', Char(254), (-14070, 0, 5650), 1000, 0),
				Insn('0x95', Char(254), (-19800, 0, 8020), 1000, 0),
				Insn('0x95', Char(254), (-26870, 0, 10100), 1000, 0),
				Insn('SLEEP', 1500),
				Insn('0x95', Char(254), (-19800, 0, 8020), 1000, 0),
				Insn('0x95', Char(254), (-14070, 0, 5650), 1000, 0),
				Insn('0x95', Char(254), (-5460, 0, 2360), 1000, 0),
				Insn('0x95', Char(254), (2270, 0, 3060), 1000, 0),
				Insn('0x95', Char(254), (8780, 0, 6460), 1000, 0),
				Insn('0x95', Char(254), (11400, 0, 7650), 1000, 0),
				Insn('SLEEP', 1500),
			]),
		]),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (-5510, 20120), (280, 18050), 1000),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('CHAR_FLAG1_UNSET', Char(23), 128),
	Insn('0x78', b'\x04', Char(23)),
	Insn('OBJ_SET_FRAME', Object(4), 'light', Insn('0', 1)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(23), (-5300, 0, 1800), 100),
	Insn('0xD3', Char(23), 0, 100000, 0, 0),
	Insn('OBJ_FLAG_SET', Object(4), 4096),
	Insn('0x74', Object(4), 7680),
	Insn('0x70', Object(4), b'\x00\x00'),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 107), Insn('EQ'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('0x23', 7), Insn('CONST', 4), Insn('EQ'), Insn('0x23', 7), Insn('CONST', 5), Insn('EQ'), Insn('OR'), Insn('0x23', 7), Insn('CONST', 11), Insn('EQ'), Insn('OR'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (21040, 0, 11840), 270),
					Insn('CHAR_SET_POS', Char(1), (21040, 0, 11840), 270),
					Insn('CHAR_SET_POS', Char(2), (21040, 0, 11840), 270),
					Insn('CHAR_SET_POS', Char(3), (21040, 0, 11840), 270),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (21040, 0, 11840), 270),
							Insn('CHAR_SET_POS', Char(5), (21040, 0, 11840), 270),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (21040, 0, 11840), 270),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 101), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('0x23', 7), Insn('CONST', 2), Insn('EQ'), Insn('0x23', 7), Insn('CONST', 7), Insn('EQ'), Insn('OR'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (-39280, 0, 12420), 90),
					Insn('CHAR_SET_POS', Char(1), (-39280, 0, 12420), 90),
					Insn('CHAR_SET_POS', Char(2), (-39280, 0, 12420), 90),
					Insn('CHAR_SET_POS', Char(3), (-39280, 0, 12420), 90),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-39280, 0, 12420), 90),
							Insn('CHAR_SET_POS', Char(5), (-39280, 0, 12420), 90),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-39280, 0, 12420), 90),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 102), Insn('SET'), Insn('END')])),
				]),
				(None, [
					Insn('CHAR_SET_POS', Char(0), (13270, 0, -19100), 315),
					Insn('CHAR_SET_POS', Char(1), (13270, 0, -19100), 315),
					Insn('CHAR_SET_POS', Char(2), (13270, 0, -19100), 315),
					Insn('CHAR_SET_POS', Char(3), (13270, 0, -19100), 315),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (13270, 0, -19100), 315),
							Insn('CHAR_SET_POS', Char(5), (13270, 0, -19100), 315),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (13270, 0, -19100), 315),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 100), Insn('SET'), Insn('END')])),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('0xD0', 7, Expr([Insn('CONST', 6), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1029)), Insn('FLAG', Flag(1030)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 45))),
		]),
		(Expr([Insn('FLAG', Flag(1600)), Insn('FLAG', Flag(1601)), Insn('BOOL_AND'), Insn('FLAG', Flag(1602)), Insn('BOOL_AND'), Insn('FLAG', Flag(1567)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 59))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 48))),
		]),
		(Expr([Insn('FLAG', Flag(737)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(737)),
			Insn('EVENT', Function((0, 49))),
		]),
		(Expr([Insn('FLAG', Flag(738)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(738)),
			Insn('EVENT', Function((0, 54))),
		]),
		(Expr([Insn('FLAG', Flag(739)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(739)),
			Insn('EVENT', Function((0, 23))),
		]),
		(Expr([Insn('FLAG', Flag(740)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(740)),
			Insn('EVENT', Function((0, 24))),
		]),
		(Expr([Insn('FLAG', Flag(741)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(741)),
			Insn('EVENT', Function((0, 26))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(10), 16),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1569)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(17), 128),
					Insn('CHAR_FLAG1_UNSET', Char(18), 128),
					Insn('CHAR_FLAG1_UNSET', Char(19), 128),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1560)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(10), 16),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1550)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(8), 128),
			Insn('CHAR_FLAG1_SET', Char(9), 128),
			Insn('CHAR_FLAG1_SET', Char(10), 128),
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_FLAG1_SET', Char(12), 128),
			Insn('CHAR_FLAG1_SET', Char(13), 128),
			Insn('CHAR_FLAG1_SET', Char(14), 128),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_WATCH', Char(10), Char(11), 0),
			Insn('CHAR_WATCH', Char(11), Char(10), 0),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(8), 128),
			Insn('CHAR_FLAG1_SET', Char(9), 128),
			Insn('CHAR_FLAG1_SET', Char(10), 128),
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_FLAG1_SET', Char(12), 128),
			Insn('CHAR_FLAG1_SET', Char(13), 128),
			Insn('CHAR_FLAG1_SET', Char(14), 128),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(10), 16),
			Insn('CHAR_FLAG1_SET', Char(11), 16),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_WATCH', Char(10), Char(11), 0),
					Insn('CHAR_WATCH', Char(11), Char(10), 0),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('TASK_GET', 1))), Insn('FLAG', Flag(1199)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(20), 128),
				]),
				(None, [
					Insn('CHAR_FLAG1_UNSET', Char(16), 128),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(8), (-9610, 1770, 24250), 0),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 16))), Insn('END')]), []),
				(Expr([Insn('FLAG', Flag(1199)), Insn('END')]), []),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('TASK_GET', 1))), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(20), 128),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(10), 16),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('CHAR_WATCH', Char(11), Char(10), 0),
			Insn('CHAR_FLAG1_SET', Char(11), 16),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), []),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(768)), Insn('NOT'), Insn('FLAG', Flag(552)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x09', 268435456),
			Insn('EVENT', Function((0, 43))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 107), Insn('EQ'), Insn('FLAG', Flag(1035)), Insn('BOOL_AND'), Insn('FLAG', Flag(1036)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(0), (-9950, 0, 3770), 220),
			Insn('CHAR_SET_POS', Char(1), (-9950, 0, 3770), 220),
			Insn('CHAR_SET_POS', Char(2), (-9950, 0, 3770), 220),
			Insn('CHAR_SET_POS', Char(3), (-9950, 0, 3770), 220),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1031)), Insn('FLAG', Flag(1037)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 103), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('FLAG', Flag(1038)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 102), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1352)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 105), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('FLAG', Flag(1792)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 103), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('FLAG', Flag(1793)), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 203), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('FLAG', Flag(760)), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('FLAG_UNSET', Flag(760)),
		]),
		(None, []),
	]),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('0xB5', b'\x00\x05\x80\x00'),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('0xB5', b'\x00\x06\x80\x00'),
	Insn('0xB5', b'\x00\x04\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1026)), Insn('FLAG', Flag(1027)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x00\x80\x00'),
			Insn('0xB5', b'\x01\x05\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1035)), Insn('FLAG', Flag(1036)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x01\x80\x00'),
			Insn('0xB5', b'\x01\x06\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1037)), Insn('FLAG', Flag(1038)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
			Insn('0x11', b'\xfe\xcb\xc0', 44, 157, 0),
			Insn('OBJ_SET_FRAME', Object(255), 'sky', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'sky1', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'sd_mul', Insn('0', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
			Insn('0x11', b'\xfe\xcb\xc0', 44, 157, 0),
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
		(Expr([Insn('FLAG', Flag(1060)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'ka01', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'ka02', Insn('1', 1)),
		]),
		(None, [
			Insn('OBJ_SET_FRAME', Object(255), 'ka01', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'ka02', Insn('0', 1)),
		]),
	]),
	Insn('0xB5', b'\x00\x02\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(768)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(564)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x02\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(768)), Insn('FLAG', Flag(1026)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(831)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x02\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1536)), Insn('FLAG', Flag(1550)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1605)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x02\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1558)), Insn('FLAG', Flag(1559)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x02\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1560)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1606)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x02\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('FLAG', Flag(1848)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x02\x80\x00'),
		]),
		(None, []),
	]),
	Insn('0xB5', b'\x00\x03\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(768)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x03\x80\x00'),
		]),
		(None, []),
	]),
	Insn('0x1B', 1, Function((255, 255)), 255),
	Insn('0x1B', 2, Function((255, 255)), 255),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1037)), Insn('FLAG', Flag(1040)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 1, Function((0, 62)), 0),
			Insn('0x1B', 2, Function((0, 63)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1558)), Insn('FLAG', Flag(1559)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 1, Function((0, 62)), 0),
			Insn('0x1B', 2, Function((0, 63)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1035)), Insn('FLAG', Flag(1036)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('FORK_FUNC', Char(23), 0, Function((0, 5))),
		]),
		(None, []),
	]),
	Insn('0x65', 0, 1),
	Insn('0x65', 1, 1),
	Insn('0x65', 2, 1),
	Insn('0x65', 3, 1),
	Insn('0x65', 4, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 16))), Insn('END')]), []),
				(Expr([Insn('FLAG', Flag(1199)), Insn('END')]), []),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('TASK_GET', 5))), Insn('END')]), [
					Insn('0x1B', 1, Function((0, 36)), 0),
					Insn('0x1B', 2, Function((0, 37)), 0),
					Insn('0x1B', 3, Function((0, 38)), 0),
					Insn('0x1B', 4, Function((0, 39)), 0),
					Insn('0x1B', 5, Function((0, 40)), 0),
					Insn('0x1B', 6, Function((0, 41)), 0),
					Insn('CHAR_FLAG1_SET', Char(16), 128),
					Insn('CHAR_FLAG2_SET', Char(16), 32768),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('TASK_GET', 1))), Insn('END')]), [
					Insn('0x66', 0, 1),
					Insn('0x66', 1, 1),
					Insn('0x66', 2, 1),
					Insn('0x66', 3, 1),
					Insn('0x66', 4, 1),
					Insn('0x1B', 0, Function((0, 35)), 0),
					Insn('0x1B', 1, Function((0, 36)), 0),
					Insn('0x1B', 2, Function((0, 37)), 0),
					Insn('0x1B', 3, Function((0, 38)), 0),
					Insn('0x1B', 5, Function((0, 40)), 0),
					Insn('0x1B', 6, Function((0, 41)), 0),
					Insn('CHAR_FLAG1_SET', Char(16), 128),
					Insn('CHAR_FLAG2_SET', Char(16), 32768),
					Insn('IF', [
						(Expr([Insn('ATTR', 0), Insn('CONST', 105), Insn('EQ'), Insn('END')]), [
							Insn('EVENT', Function((0, 42))),
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
		(Expr([Insn('FLAG', Flag(1537)), Insn('FLAG', Flag(1542)), Insn('NOT'), Insn('BOOL_AND'), Insn('0x23', 1), Insn('CONST', 1), Insn('EQ'), Insn('BOOL_AND'), Insn('END')]), []),
		(None, [
			Insn('0x16', Insn('3', b'\x1d\x01\x00')),
		]),
	]),
	Insn('RETURN'),
]

data['code'][8] = [
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
				Insn('OPEN_SHOP', 126),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), []),
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
				Insn('IF', [
					(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'我们店的冰淇淋都是纯手工制作的哦。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'绝对值得您\n'
									'购买品尝～{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(8), Text(
									'我们店的冰淇淋\n'
									'都是纯手工制作的哦。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'……啊，你现在是不是正在想\n'
									'『看上去似乎很好吃』呢！？{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'想吃就要立刻行动哦。\n'
									'来，买一个回去吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('ATTR', 10), Insn('CONST', 9), Insn('EQ'), Insn('END')]), [
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
										Insn('TEXT_TALK', Char(8), Text(
											'最近这段时间，暴躁易怒的人\n'
											'越来越多了呢。{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
									(None, [
										Insn('TEXT_TALK', Char(8), Text(
											'那边的小哥……不，大叔。\n'
											'来个冰淇淋吧！{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(266), Text(
											'#0603F我才只有二十七岁……！{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('FLAG_SET', Flag(0)),
									]),
								]),
							]),
							(None, [
								Insn('TEXT_TALK', Char(8), Text(
									'冰淇淋～来个冰淇淋吧～？{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'这位小哥，\n'
									'你也买一个吧！{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'我们店也有适合成年人的\n'
									'白兰地味冰淇淋哦！{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'肚子痛的时候，\n'
									'可不能吃冰淇淋哦～{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(8), Text(
									'我从彩虹剧团的人\n'
									'那里听说了……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'他们那里的一名成员\n'
									'最近的样子好像很奇怪。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'是怎么了呢？\n'
									'吃坏肚子了吗？{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'冰淇淋～\n'
									'来个冰淇淋吧！{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(8), Text(
									'纪念庆典结束了，\n'
									'可游客的人数并没有减少呢～{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'这可真是件值得高兴的事啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'各位，请尽情\n'
									'把钱花掉吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'我听说在纪念庆典期间，\n'
									'港湾区那边新开了一家好吃的冰淇淋店，\n'
									'本来还有些提心吊胆，不过……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'我这个月仍旧\n'
									'获得了露天店的ＭＶＰ。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'呵呵，这也是\n'
									'托了各位的福啊～{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(8), Text(
									'冰淇淋～来个冰淇淋吧～？{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'……纪念庆典的营业额\n'
									'真是节节攀升呢～\n'
									'大约是平时的二十倍左右吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'必须保持这个势头，\n'
									'死守住露天店销售额\n'
									'第一的宝座呢～{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('TASK_GET', 1))), Insn('FLAG', Flag(1199)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
										Insn('TEXT_TALK', Char(8), Text(
											'冰淇淋～来个冰淇淋吧？{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('CHAR_WATCH', Char(254), Char(284), 500),
										Insn('TEXT_TALK', Char(8), Text(
											'……小狗狗要不要\n'
											'也来个冰淇淋啊～？\n'
											'很好吃的哦～{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
									(None, [
										Insn('TEXT_TALK', Char(8), Text(
											'冰淇淋～来个冰淇淋吧？{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('CHAR_WATCH', Char(8), Char(284), 500),
										Insn('TEXT_TALK', Char(8), Text(
											'……小狗狗要不要\n'
											'也来个冰淇淋啊～？\n'
											'很好吃的哦～{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(284), Text(
											'#1200F呜噜噜噜……{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(259), Text(
											'#0200F（它在说\n'
											'\u3000『我不喜欢甜食』。）{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('FLAG_SET', Flag(0)),
									]),
								]),
								Insn('TEXT_END', Char(8)),
								Insn('RETURN'),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'我们店的冰淇淋，\n'
									'在剧团团员中很受欢迎哦。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'干脆打着剧团指定冰淇淋的旗号，\n'
									'趁势多卖点吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(8), Text(
									'其实剧团的人\n'
									'也经常来买我们店的冰淇淋哦。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'伊莉雅小姐和普莉耶小姐\n'
									'都是我们店的常客。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'干脆打着\n'
									'剧团指定冰淇淋的旗号吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'顾客就是神明～\n'
									'有什么要求请尽管提出来。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(8), Text(
									'啊，早安。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'现在还在做开店准备，不过\n'
									'你们要买冰淇淋吗～？{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'剧团成员喜欢吃的口味，\n'
									'都快要卖光了哦～{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'想吃的话要快点买啊，\n'
									'别留下遗憾。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(8), Text(
									'冰淇淋～来个冰淇淋吧～？{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'彩虹剧团成员\n'
									'喜欢吃的口味，\n'
									'都快要卖光了哦～{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'想吃的话要快点买啊，\n'
									'别留下遗憾。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'剧团的崇拜者都会来买\n'
									'这些口味的冰淇淋哦。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'你们也要跟上潮流啊，\n'
									'来一个怎么样？{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(8), Text(
									'小哥，你们也是\n'
									'彩虹剧团的崇拜者吧！{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'那就一定要买\n'
									'我这里的冰淇淋了～{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'来来，买一个吃吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'我这个月也\n'
									'获得了露天店的ＭＶＰ。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'这都是托了各位的福～{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(8), Text(
									'太好了～销售额第一！{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'承蒙各位的惠顾，\n'
									'我们店这个月的销售额\n'
									'获得了第一名哦。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'这都是托了大家的福，\n'
									'谢谢你们～{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'我最喜欢\n'
									'剧团的崇拜者们了。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(8), Text(
									'各位崇拜者\n'
									'每天早上都会\n'
									'很早就来。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'然后买我这里的冰淇淋\n'
									'当零食哦。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'哎呀～真是值得高兴啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'怎么没有卖饮料的啊，\n'
									'我还想用冰淇淋换饮料喝呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(8), Text(
									'冰淇淋～来个冰淇淋吧～？{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'啊，口好渴啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'哪里有\n'
									'卖饮料的呢～？{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'我建议您趁现在\n'
									'买个冰淇淋吃。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'下午说不定\n'
									'就会卖光了哦。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(8), Text(
									'冰淇淋～来个冰淇淋吧～？{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'……这位小哥，\n'
									'来个冰淇淋吧！{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'今天天气会很热哦～！\n'
									'等下你要是后悔我可不管哦～！{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(0)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(561)), Insn('END')]), [
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('RECIPE', 21)), Insn('NOT'), Insn('END')]), [
										Insn('CALL', Function((0, 11))),
									]),
									(None, [
										Insn('CALL', Function((0, 9))),
									]),
								]),
							]),
							(None, [
								Insn('CALL', Function((0, 9))),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(561)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('RECIPE', 21)), Insn('NOT'), Insn('END')]), [
								Insn('CALL', Function((0, 11))),
							]),
							(None, [
								Insn('CALL', Function((0, 10))),
							]),
						]),
					]),
					(None, [
						Insn('CALL', Function((0, 10))),
					]),
				]),
			]),
			(None, []),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('TEXT_TALK', Char(8), Text(
		'今天傍晚\n'
		'彩虹剧团\n'
		'有场公演呢～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'销售额肯定\n'
		'能上涨许多～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
			Insn('TEXT_TALK', Char(8), Text(
				'我们店的冰淇淋\n'
				'超级好吃的哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(8), Text(
				'冰淇淋～来个冰淇淋吧～？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'……这位小哥，\n'
				'来个冰淇淋吧！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(0)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('TEXT_TALK', Char(254), Text(
		'冰淇淋～来个冰淇淋吧～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'对了，这位小哥，\n'
		'今天有特别大赠送哦～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'我们将教您\n'
		'奶油拿铁的制作方法。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'很好喝哦，\n'
		'请务必试一试～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'学习了{item 461}{color 0}的做法。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'记住了{item 461}{color 0}的食谱。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('RECIPE', 21),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'哎呀……欢迎光临。\n'
						'小哥，你们有时间吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'要不要来喝杯酒啊？\n'
						'我们店有很多不错的女孩子哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嘿嘿，就连警备队司令\n'
						'也经常来光顾哦。\n'
						'绝对会让你们不虚此行。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'嘿嘿，就连警备队司令\n'
						'也经常来光顾哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'怎么样，进来玩一玩吧，\n'
						'绝对会让你们不虚此行。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'好像从昨天开始，警察就\n'
						'一直出入那间饭店。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'哎呀呀，简直是妨碍营业嘛。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'听说从昨天开始，警察就\n'
						'一直出入那间饭店。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'哎呀呀，到底发生了什么事呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'这样会让客人担心受怕，真希望他们别来啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'今天的气氛很奇怪，{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'我都不敢拉客了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'总觉得今天\n'
						'欢乐街的气氛很奇怪……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'警察好像随时\n'
						'都有可能强行进行搜查。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'今天还是应该\n'
						'早点收手为好吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'自纪念庆典之后一直留在\n'
						'这里的游客好像有很多啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'真是让人高兴啊，小哥，\n'
						'我要拉大家一起去\n'
						'玩玩特别娱乐项目。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'纪念庆典都已经过去一个月了，\n'
						'还有很多人不回家，\n'
						'在这里闲逛。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'真让人高兴啊，小哥，\n'
						'我真的很感动哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'他们简直就像是在说：\n'
						'『快来拉我们吧』。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'每年议会期间，我们都会\n'
						'争抢接待工作。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'嘿嘿……工作了工作了，\n'
						'今年也必须得争取多一些预约啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'预算会议快要开始了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'嘿嘿……\n'
						'我们店对接待方面很有信心，{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'绝对不会输给\n'
						'那些乱七八糟的店哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('TASK_GET', 1))), Insn('FLAG', Flag(1199)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
							Insn('CHAR_WATCH', Char(9), Char(284), 0),
							Insn('TEXT_TALK', Char(9), Text(
								'哇，好威风的狗啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(9), Text(
								'这是你们养的吗？\n'
								'真好啊，太让人羡慕了。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('CHAR_WATCH', Char(9), Char(284), 0),
							Insn('TEXT_TALK', Char(9), Text(
								'哇，好威风的狗啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(9), Text(
								'这是你们养的吗？\n'
								'真好啊，太让人羡慕了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(284), Text(
								'#1203F呜噜噜噜……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(259), Text(
								'#0203F（它在说：\n'
								'\u3000『我对你这种小角色没兴趣』。）{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(1)),
						]),
					]),
					Insn('TEXT_END', Char(9)),
					Insn('RETURN'),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'如果做违法生意，\n'
						'游击士协会的人就会找上门来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'哎呀呀，真是很吓人啊，\n'
						'我可不是\n'
						'那么坏的人哦～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'刚才有游击士来店里了，\n'
						'我当时吓了一跳呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'还好，那些人只是因为任务，\n'
						'来询问一些事情的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'真是很吓人啊，\n'
						'我们店也没有\n'
						'做什么违法生意啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'呵呵，今天早上睡醒后心情不错，{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'挫了挫对方的锐气，\n'
						'心情真是好啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'我从毕许的店里\n'
						'拉来了一个女孩子哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'嘿嘿，不过这只是\n'
						'小竞争而已。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'挫了挫对方的锐气，\n'
						'心情真是好啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'嘿嘿，客人们都\n'
						'快来了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'现在必须打起精神努力加油啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'小哥小哥，\n'
						'来得正好啊，{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'要不要\n'
						'来玩一玩啊？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'肯定让您开心呢～\n'
						'疲惫也会一扫而光的哦～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'可不能跟\n'
						'鲁巴彻商会那种\n'
						'组织扯上关系啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'最近黑月那帮家伙\n'
						'好像在扩大势力范围。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'不过，克洛斯贝尔黑道势力\n'
						'的龙头老大\n'
						'还是鲁巴彻商会哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'在这条街上可不能\n'
						'忤逆那些家伙。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'随着议会的临近，\n'
						'要接待的客人也会增多哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'等那些手掌大权的议员来光顾时，\n'
						'我们会给他们特别优待的～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'小哥、小哥，\n'
						'要不要来玩玩啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'……最近，要接待的\n'
						'大客户增多了哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'啊，真开心啊。\n'
						'肯定是因为议会召开临近了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'昨天警察好像\n'
						'在进行什么案件的查访。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'两个刑警一组，\n'
						'四处打听消息呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哎呀呀，我可什么都不知道哦，\n'
						'我只是个善良的揽客员而已～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'欢乐街经常有事件发生，\n'
						'所以时不时就有警察来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哎呀呀，\n'
						'我可什么都不知道哦～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'冰淇淋店的那位小姐，真是可爱啊。\n'
						'如果她失业了，就由我们来收留吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'（舔舔）……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'我去前面那个\n'
						'冰淇淋店采购冰淇淋回来了，{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'冰淇淋店的那位小姐，真是可爱啊～\n'
						'如果她失业了，就由我们来收留吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'毕许说的话，\n'
						'你们可不能听啊。\n'
						'想要玩的话就来我们店吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'那边的小巷里，\n'
						'有个叫毕许的男人吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'他是我的竞争对手。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'那个男人说的话，\n'
						'你们可不能听啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'哪里有\n'
						'好客人啊～？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'啊，都中午了。\n'
						'客人们差不多快来了，{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'路过这里的客人，\n'
						'可是很多的哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'嘿嘿，真是期待啊。\n'
						'今天要拉哪个人呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'我们店就在这附近哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'嘿嘿，怎样，小哥？\n'
				'今天会给你优惠哦～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('IF', [
				(Expr([Insn('ATTR', 10), Insn('CONST', 0), Insn('EQ'), Insn('ATTR', 10), Insn('CONST', 3), Insn('EQ'), Insn('OR'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'嘿嘿嘿，\n'
						'小哥你们来得正是时候啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'怎么样，来我们店喝杯美酒吧，\n'
						'还有很多很棒的女孩子哦～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'啊……我可没\n'
						'叫小孩子哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(9), Char(257), 750),
					Insn('TEXT_TALK', Char(254), Text(
						'怎么样，那位小哥，\n'
						'来我们店喝杯美酒吧，\n'
						'还有很多很棒的女孩子哦～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('TEXT_TALK', Char(9), Text(
				'一小时才一千米拉哦。\n'
				'嘿嘿，来玩玩吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'剧团爱好者的眼睛是雪亮的！\n'
						'一定发生了什么事！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'虽然我去问过接待处的人，\n'
						'但也没问出什么……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'从早上开始，剧团的气氛就很奇怪。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'我虽然去问了接待处的人，\n'
						'但是也问不出什么详细情况……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'今天白天的公演推迟了很久呢，\n'
						'到底发生了什么事呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'我听不到伊莉雅小姐心中的声音了，\n'
						'那个声音平时只有我才能听到的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'到底发生了什么事呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'#4S伊莉雅小姐～！伊莉雅小姐～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'……好奇怪……\n'
						'总觉得今天好安静啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_FLAG1_UNSET', Char(10), 16),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1560)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'伊莉雅小姐～\n'
						'公演请加油哦～！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'今天的公演开始了呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'虽然没有门票，但也没关系，\n'
						'我仍然会站在远处为伊莉雅小姐加油！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_ROTATE', Char(10), 315, 0),
					Insn('CHAR_FLAG1_SET', Char(10), 16),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(10), Text(
				'伊莉雅小姐～请出来\n'
				'向我们挥挥手吧！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'今天要发售『金之太阳、银之月』\n'
						'的写真集哦！\n'
						'这可一定不能错过……！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'喂，你们听说了吗？\n'
						'今天要发售『金之太阳、银之月』\n'
						'的写真集哦！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'里面网罗了\n'
						'公演的精彩看点\n'
						'和所有情节的照片哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'绝、绝对不能错过……\n'
						'我得马上去百货一趟……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'啊，伊莉雅小姐……\n'
						'她现在在做什么呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'彩虹剧团\n'
						'今天休息。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'虽然有几位团员主动来练习了……\n'
						'但伊莉雅小姐好像并没有来……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'#4S伊莉雅小姐～\n'
						'练习要加油哦～！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CALL', Function((0, 14))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(10), Text(
				'伊莉雅小姐今天好像睡懒觉了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'真是少见啊，\n'
				'把这个写进今天的日记里吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), [
			Insn('TEXT_TALK', Char(10), Text(
				'伊莉雅小姐，\n'
				'练习要加油哦～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'咦……真的吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'如果有人偷跑进去，\n'
						'我可不会放过他哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'你们……\n'
						'在彩虹剧团做什么？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'很可疑啊。\n'
						'你们不是剧团的人吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F那个，我们并不是什么可疑的人。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0012F我们有朋友在这里工作。\n'
						'（这应该不算说谎吧……？）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'呜呜呜，我还以为\n'
						'能再一次见到伊莉雅小姐……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'为了这一天，\n'
						'我都忍耐那么久了……！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'#4S呜哇～！！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'在新剧门票发售的日子，\n'
						'我竟然起晚了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'虽然我急急忙忙地跑去买，\n'
						'但排到我时，门票刚好卖光了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'呜呜呜……我这个笨蛋……\n'
						'这样一来，就见不到伊莉雅小姐了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(10), Text(
				'新剧的门票\n'
				'好像从下星期开始出售。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'好想要啊……呵呵……\n'
				'我一定要买到手……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'好想拍伊莉雅小姐穿练习装的样子……\n'
						'……还、还有她穿新剧演出服的\n'
						'各种姿势㈱{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'呵呵，不知道有没有\n'
						'机会可以拍到～！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'伊莉雅小姐，伊莉雅小姐……！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'我拍到了她穿便装、\n'
						'舞台服装还有在休息室穿睡袍的照片。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'剩下的还有她穿练习装的样子……\n'
						'呵呵，不知道有没有\n'
						'机会可以拍到呢～！{wait}'
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
						'伊莉雅小姐要出演\n'
						'这次的新剧哦！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'啊啊，终于能在现场\n'
						'一睹她的英姿了……！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('EMOTE', Char(10), 0, 2000, (38, 39, 250, 2)),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(10), Text(
						'喂，你们听说了吗！？\n'
						'这可是劲爆消息哦！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'彩虹剧团新剧的\n'
						'公演快要开始了！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'听说门票也\n'
						'要开始出售了。\n'
						'这可一定不能错过～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('EMOTE', Char(10), 0, 2000, (10, 11, 250, 2)),
					Insn('SOUND_PLAY', 27, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(10), Text(
						'伊莉雅小姐，请快点出来吧！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'还是说，\n'
						'她已经从后门离开了呢～？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'伊莉雅小姐\n'
						'还没出来吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'我的梦想是能拍到\n'
						'伊莉雅小姐刚练习完的照片。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'为此我还特别花了两万米拉\n'
						'买了一台导力相机呢～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(564)), Insn('END')]), [
			Insn('TEXT_TALK', Char(10), Text(
				'啊，是你们啊！\n'
				'你们在里面看到伊莉雅小姐了吧！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'真狡猾～！\n'
				'我也想看呢～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('CHAR_ROTATE', Char(254), 315, 0),
			Insn('TEXT_TALK', Char(10), Text(
				'不知道有没有机会看到\n'
				'伊莉雅小姐穿练习装的样子……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('0x4B', Char(10), -1),
	Insn('0x4B', Char(11), -1),
	Insn('TEXT_TALK', Char(10), Text(
		'塔普，你买到\n'
		'门票了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'没有买到呢……\n'
		'我去拜托认识的人，\n'
		'但没有一个愿意把票让给我。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'那么，纪念庆典期间要做的事情就只有一件啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'嗯嗯，只有那一件了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 10, 1, [
		Insn('CHAR_ROTATE', Char(10), 315, 750),
	]),
	Insn('FORK', 11, 1, [
		Insn('CHAR_ROTATE', Char(11), 315, 750),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('TEXT_TALK', Char(10), Text(
		'#4S那就是一直\n'
		'默默守护着伊莉雅小姐～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#4S伊莉雅小姐，\n'
		'我会用心一直守护您的～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(2)),
	Insn('0x4C', Char(10), -1),
	Insn('0x4C', Char(11), -1),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(11), Text(
				'今天白天的公演推迟了，\n'
				'到四点左右才开始呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'听说剧团长和总管\n'
				'一直慌慌张张地跑进跑出……\n'
				'不会真的发生了什么事吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'今天白天的公演\n'
						'不知道为什么好像推迟了……\n'
						'发生了什么事吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'剧团里安静得有些可疑……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'公演差不多要开始了吧？\n'
						'他们都在干什么啊～{wait}'
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
						'今天早上我在等伊莉雅小姐的时候，\n'
						'那个孩子一直瞪着我。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'……剧团为什么要雇\n'
						'一个那么没有亲和力的家伙呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'最近彩虹剧团好像\n'
						'新招了一个打杂的孩子……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'那孩子时不时就会瞪我……\n'
						'真是一个没有亲和力的家伙啊。{wait}'
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
						'希望莉夏小姐的写真集\n'
						'可以早点发售啊……\n'
						'大概还要等很久，真是没办法。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'伊莉雅小姐当然毋庸置疑，\n'
						'不过新人莉夏小姐也很厉害哦……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'如果莉夏小姐\n'
						'出个人写真集的话，\n'
						'绝对会大卖的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'还不发售吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'听说莉夏丄毛\n'
						'和伊莉雅小姐的对手戏\n'
						'非常精彩。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呜呜……我也想\n'
						'在现场观看啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'有一个凭借与伊莉雅小姐共同演出\n'
						'而出道的女孩子叫莉夏丄毛吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'大家都评论说她的演技很厉害。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'她和伊莉雅小姐的风格不同，\n'
						'舞姿楚楚可人，\n'
						'却也有着凛然风骨。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呜呜……\n'
						'我也想在现场看啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'#4S伊莉雅小姐～\n'
						'我们这些崇拜者都会紧紧跟随您的～！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CALL', Function((0, 14))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'那人是谁啊……？\n'
						'难道是伊莉雅小姐的新崇拜者？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'今天早上，有一群\n'
						'穿着西服的人进了剧团……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'虽然好像是剧团的相关人员，\n'
						'但眼神都很锐利……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'不过，就算有演出，\n'
						'我这个穷学生\n'
						'也是看不了的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'没关系，能看到夜晚中的剧场\n'
						'我也就满足了！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'彩虹剧团最近正在为\n'
						'新剧公演进行排练。\n'
						'所以今天晚上没有演出。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'不过，能看到夜晚中的剧场\n'
						'就已经让人兴奋不已了，不是吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('TEXT_TALK', Char(11), Text(
				'今天早上，那个新人莉夏小姐\n'
				'出入了剧场好几次……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'是有什么东西忘在家里了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'彩虹剧团的门票，\n'
						'就算是Ｂ席也很昂贵……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……虽然很遗憾，但我这次\n'
						'只能放弃了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'像我这种穷学生，\n'
						'果然是没办法看这种表演的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'气死我了，虽然我\n'
						'去求了父母……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但他们说学生不应该\n'
						'看太多这种表演。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(11), Text(
				'喂，宝莉榭，口水流出来了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(11), Text(
				'可恶，我都\n'
				'没有导力相机……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'那对学生来说\n'
				'也实在太贵了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我每天早上都会来这里。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真想直接在这广场\n'
						'搭个帐篷住下算了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'你们也是来欣赏\n'
						'伊莉雅小姐早上的身姿的吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'追星也要适可而止啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'其实宝莉榭那家伙\n'
						'是跟我一起追随彩虹剧团的伙伴。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哼……我们偶然在\n'
						'同一天看到伊莉雅小姐的舞姿，\n'
						'然后同时被她所俘虏了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(11), Text(
						'《彩虹剧团》在国际上\n'
						'也是享誉盛名的剧团哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'剧团里的艺人\n'
						'也都是顶级的名演员。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'但伊莉雅小姐在其中仍是与众不同的！\n'
						'绝世舞姬，堪称天才的伊莉雅丄普拉提耶……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'我十分理解宝莉榭那家伙\n'
						'为她如痴如狂的心情。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
			Insn('TEXT_TALK', Char(11), Text(
				'《彩虹剧团》平时都是\n'
				'禁止观众进入的哦～\n'
				'所以只能站在外面看呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(11), Text(
				'哦，你们也是来看\n'
				'《彩虹剧团》的情况的吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'虽然里面禁止观众进入，\n'
				'但只从外面看的话可是免费的哦。\n'
				'嗯，我们同为崇拜者，请多关照哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(3)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'今天晚上我们准备\n'
				'全家一起去吃晚餐。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'呵呵，差不多\n'
				'该去做些准备了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'今天大街上有点安静啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'导力车的数量\n'
				'好像也比平时少。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'坎贝尔议员勉强算是\n'
						'哈尔特曼议长的对手。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'不过，应该没有人能胜过\n'
						'那个议长吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'哈尔特曼议长就是\n'
						'那个狂妄自大的人吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'听说他和鲁巴彻\n'
						'有关系，好像一直对\n'
						'鲁巴彻颐指气使……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'呵呵，真是可怕的人啊。\n'
						'要是与他为敌的话，应该会很惨吧。{wait}'
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
						'有段时间，一个中性风格打扮的男公关\n'
						'成了街头巷尾议论的话题哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'不过遗憾的是，纪念庆典之后\n'
						'就没再听过关于他的消息了……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'那个男公关……\n'
						'最近都没听过关于他的消息。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'从容不迫的眼神，\n'
						'再加上中性风格的打扮，\n'
						'有段时间让他受到了一致好评。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'呼……真是令人遗憾啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'纪念庆典短短五天时间里，\n'
				'好像无论哪家店都\n'
				'都赚得盆满钵满。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'呵呵，这些都是\n'
				'游客扔在这里的钱啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'克洛斯贝尔又从\n'
				'世界各地收集了一大笔财富。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'参加各种聚会，去剧场看表演，\n'
				'还要到米修拉姆的主题乐园玩……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵呵，纪念庆典期间大概也会很忙呢，\n'
				'必须合理安排计划呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'有很多游客预料到\n'
				'纪念庆典会很拥挤，\n'
				'所以提前来到了克洛斯贝尔。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'这附近的饭店\n'
				'应该会持续爆满吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'呵呵，我收到了一个\n'
				'今晚举办的社交宴会的邀请。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'必须抓紧时间好好打扮。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'虽然很少听见相关传闻，\n'
						'但最近好像发生了\n'
						'很多事件呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'最近经常有警察\n'
						'来进行案情询问。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'哎呀哎呀……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'是不是哪里又\n'
						'发生什么事件了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'彩虹剧团粉丝的热情\n'
						'丝毫未减，仍然很高涨啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'竟然连我\n'
						'都没能买到门票。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'门票发售当天\n'
						'实在太多人了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'所以我也没能买到门票。\n'
						'唉～真是令人遗憾啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'那么，今天要去哪里玩呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'呵呵，在欢乐街，\n'
				'争吵纠纷是常有的事。\n'
				'不需要去一一关心。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'虽然和阿尔摩利卡村及玛因兹\n'
						'一样位于市外，\n'
						'但乌尔斯拉医院可不一样。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'那是市民\n'
						'常去的一家大学附属医院哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'乌尔斯拉医院位于\n'
						'克洛斯贝尔市南部，\n'
						'有最新的医疗设施哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'呵呵，它和阿尔摩利卡村\n'
						'以及玛因兹不同，\n'
						'是市民常去的地方。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'在克洛斯贝尔，\n'
						'如果受了伤，马上就会被\n'
						'送到乌尔斯拉医院。{wait}'
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
						'你们要注意那群拉客的男人。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'如果上了他们的当，\n'
						'全部财产都会被骗光的哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'那边的小巷里，\n'
						'有好几个拉客的可疑男人。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'你们不熟悉这里，可一定要注意啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'要是放松警惕的话，\n'
						'就会被他们的花言巧语蒙骗。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'克洛斯贝尔的欢乐街\n'
						'即使在周边各国也是非常有名的社交场所。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'前来游玩的游客\n'
						'络绎不绝。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'克洛斯贝尔的欢乐街\n'
						'是有名的社交场所。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'从适合一般大众的赌场到上流阶层\n'
						'专用的会所都聚集于此……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'呵呵，从外国\n'
						'前来游玩的游客\n'
						'络绎不绝。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'这附近有不少家\n'
				'饭店和餐厅哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'如果来克洛斯贝尔游玩，\n'
				'就一定要来这里逛逛。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(12), Text(
				'啊，好陌生的脸孔啊，\n'
				'你们是游客吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'呵呵，如果想玩玩，我推荐你们去赌场，\n'
				'要是观光，那就一定得去『彩虹剧团』了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'这附近有很多很棒的店哦。\n'
				'你们可以自己探索一下。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(4)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(13), Text(
				'好，天黑了！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'今天也要好好玩个痛快！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'先回去睡一觉再来吧～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'昨天已经在老虎机前\n'
						'玩了一个通宵了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'呜～肚子饿得受不了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'真希望我也有那么好的运气。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'在赌场赚了很多米拉的那家伙，\n'
						'现在好像被一群公关小姐围着，\n'
						'过得超级奢靡。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'呜呜呜，真是令人羡慕啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'那种家伙\n'
						'也算是成功者了吧～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'像他那样在赌场连续取胜，\n'
						'可不是谁都能做到的。\n'
						'虽然不知道到底是谁，不过他可真厉害啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'……你们听说了吗？\n'
						'最近好像有一个家伙\n'
						'在赌场连续赢了很多米拉。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'虽然不知道到底是谁，\n'
						'不过他可真厉害啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'今天虽然想玩老虎机，\n'
						'但不知道哪里有比较好的店……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'这是一片充斥着金钱与欲望的土地……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'就算纪念庆典结束了，\n'
						'欢乐街还是欢乐街呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'来这里要做的事\n'
						'可以说只有一件。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'彩虹剧团的\n'
						'赞助商里，\n'
						'有很多有权有势的人和外国的富豪。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'他们每个人都有很豪华的导力车。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'彩虹剧团的预演\n'
						'也临近了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'所以时不时就会有\n'
						'赞助商来露个面……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'他们每个人都有很豪华的导力车，\n'
						'真是让人羡慕啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'那个叫莉夏的女孩子，很可爱吧～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'虽然她才刚入团不久，\n'
						'但给人感觉总是非常努力。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'彩虹剧团的新团员里\n'
						'有一个叫莉夏的女孩子吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'她真是可爱啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'我经常看到她上班，\n'
						'她给人一种对排练非常努力的感觉呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), [
			Insn('TEXT_TALK', Char(13), Text(
				'每天一到这个时间，\n'
				'大教堂的钟就会敲响。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'钟声非常庄严肃穆。\n'
				'这对游客来说，也体现了自治州风情，很受欢迎呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1036)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(254), Text(
								'刚才那辆高级轿车，每到这个时候，\n'
								'总会准时停在\n'
								'彩虹剧团的前面。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'上星期我也看到了，\n'
								'不过马上就开走了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(5)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(254), Text(
								'那么豪华的车，肯定很昂贵吧～\n'
								'到底是哪个资产家的车呢？{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1035)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊，好像停着\n'
						'一辆很豪华的车啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'黑色的高级轿车，\n'
						'这肯定是哪个资产家的车吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'你们要是想订饭店房间，\n'
						'就得快一点哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'不过我想要订今年的已经来不及了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'最近无论哪间饭店，\n'
						'好像都预约满了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'果然是因为纪念庆典的临近啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'我虽然也想买张门票……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'但实在没有勇气\n'
						'挤进那么疯狂的崇拜者中。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'彩虹剧团的新剧码\n'
						'好像叫做『金之太阳、银之月』。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'在公布新剧信息时，\n'
						'这里聚集了许多疯狂的崇拜者，\n'
						'非常喧闹呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(13), Text(
				'那么，今天要去哪里玩呢～？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'《千禧饭店》好像\n'
						'因为换了新总管，\n'
						'装潢变得更为奢华了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'等我赚够了钱，\n'
						'一定要去住一晚享受享受。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'……你们知道吗？\n'
						'《千禧饭店》好像在前年\n'
						'更换了总管。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'因为换了新总管，\n'
						'本来就已经很高级的饭店变得更为奢华了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'等我赚够了钱，\n'
						'一定要去住一晚享受享受。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'赌场的服务很周到，\n'
						'虽然老板是个粗犷的大叔啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'那边有一家叫\n'
						'《巴鲁卡》的赌场，你们知道吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'那里的服务很周到哦。\n'
						'要是输掉了米拉，\n'
						'老板就会请我喝一杯。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'有兴趣的话，\n'
						'你们可以去看看哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'去小巷的酒吧里看看好了，\n'
						'大街上没有吃饭的地方啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'唔～话说肚子好饿啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'玩着玩着\n'
						'都忘记吃饭了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
			Insn('TEXT_TALK', Char(13), Text(
				'只要在克洛斯贝尔，\n'
				'就不愁没有地方玩哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'即使玩一辈子\n'
				'也不会腻啊～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(13), Text(
				'好～今天也要玩个痛快！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'是要去赌场玩玩呢，\n'
				'还是叫个女孩去酒吧喝酒呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(13), Text(
				'要怎么玩比较好～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(5)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(14), Text(
				'Ｈｅｌｌｏ，你们好吗☆{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'那位矿工客人，\n'
				'发生什么事了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'今天都没来呢～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(14), Text(
				'Ｈｅｌｌｏ，你们好吗☆{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'赌场今天的\n'
				'生意也非常好哦～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(14), Text(
				'Ｈｅｌｌｏ，你们好吗☆{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'哎呀……你们还带着小孩子啊？\n'
				'呵呵，非常欢迎哦㈱{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(14), Text(
				'Ｈｅｌｌｏ，你们好吗☆{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'今天有优惠活动哦㈱{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('TEXT_TALK', Char(14), Text(
				'Ｈｅｌｌｏ，你们好吗☆{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'请多关照\n'
				'赌场《巴鲁卡》哦㈱{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(14), Text(
				'Ｈｅｌｌｏ，你们好吗☆{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'呵呵，希望各位玩得尽兴哦㈱{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#15200F今天我值夜班哦，\n'
						'必须先回总部小睡一会。{wait}'
						'{page}'
						'#15200F罗伊德，你们现在要去调查吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F嗯，是的。\n'
						'准备去乌尔斯拉医院看看。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#15202F支援课也很辛苦啊……\n'
						'嗯，一起加油吧！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F哈哈……说得没错呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#15200F今天我值夜班哦，\n'
						'所以必须先回总部一趟。{wait}'
						'{page}'
						'#15203F回来的路上\n'
						'得买点宵夜来吃。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'#15201F最近这段时间，发生在欢乐街\n'
				'的纠纷也开始增多了。{wait}'
				'{page}'
				'#15203F是因为经济太景气了吗……\n'
				'必须加强巡逻啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1175)), Insn('NOT'), Insn('END')]), [
			Insn('CHAR_WATCH', Char(254), Char(259), 0),
			Insn('TEXT_TALK', Char(254), Text(
				'你好啊，缇欧～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'听说这里的手工冰淇淋\n'
				'很好吃，不知道是真是假。{wait}'
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
				'#0005F（缇欧……这位先生好像是\n'
				'\u3000爱普斯泰恩财团的人吧。）{wait}'
				'{page}'
				'（约纳的事，\n'
				'\u3000不说好吗？）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0203F（嗯，暂时\n'
				'\u3000先别说。）{wait}'
				'{page}'
				'#0200F（……因为这会成为\n'
				'\u3000威胁约纳的有力手段。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(260), Text(
				'#0303F（如果他拒绝的话，就向财团告密吗……\n'
				'\u3000这种做法真是太有小缇的风格了。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F（爱普斯泰恩财团的孩子们\n'
				'\u3000好像都很有心计呢。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1175)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'我正在验证这里的\n'
				'手工冰淇淋是否真的好吃。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过可惜，\n'
				'没有桃子味的……\n'
				'我只喜欢吃桃子味的……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0211F主任，好像很闲啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1664)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 22))),
				]),
				(None, [
					Insn('0x4B', Char(17), -1),
					Insn('0x4B', Char(18), -1),
					Insn('0x4B', Char(19), -1),
					Insn('TEXT_TALK', Char(19), Text(
						'#6002F啊，真好吃……！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(17), Text(
						'#0809F对吧！？\n'
						'这是我很喜欢吃的哦。{wait}'
						'{page}'
						'#0806F听说在纪念庆典期间，\n'
						'好像还另开了一家很美味的店呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(18), Text(
						'#0900F真想让小滴\n'
						'也吃吃看。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F（哈哈……\n'
								'\u3000看上去好像很开心呢。）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, []),
					]),
					Insn('FLAG_SET', Flag(7)),
					Insn('0x4C', Char(17), -1),
					Insn('0x4C', Char(18), -1),
					Insn('0x4C', Char(19), -1),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('0x4B', Char(17), -1),
	Insn('0x4B', Char(18), -1),
	Insn('0x4B', Char(19), -1),
	Insn('0x4B', Char(8), -1),
	Insn('CAM_OFFSET', (-9790, 3700, 23610), 0),
	Insn('CAM_ROTATE', 45, 27, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 17250, 0),
	Insn('CHAR_SET_POS', Char(257), (-5470, 1990, 19030), 315),
	Insn('CHAR_SET_POS', Char(258), (-4390, 1990, 19310), 315),
	Insn('CHAR_SET_POS', Char(259), (-4670, 1990, 17970), 315),
	Insn('CHAR_SET_POS', Char(260), (-3730, 1990, 18070), 315),
	Insn('CHAR_FLAG1_SET', Char(257), 128),
	Insn('CHAR_FLAG2_SET', Char(257), 32768),
	Insn('CHAR_FLAG1_SET', Char(258), 128),
	Insn('CHAR_FLAG2_SET', Char(258), 32768),
	Insn('CHAR_FLAG1_SET', Char(259), 128),
	Insn('CHAR_FLAG2_SET', Char(259), 32768),
	Insn('CHAR_FLAG1_SET', Char(260), 128),
	Insn('CHAR_FLAG2_SET', Char(260), 32768),
	Insn('CHAR_WATCH', Char(8), Char(17), 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(17), Text(
		'#0800F小滴，\n'
		'你喜欢哪种口味啊？{wait}'
		'{page}'
		'我请客，\n'
		'喜欢吃什么你随便点哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#6010F这、这怎么行……多不好意思。{wait}'
		'{page}'
		'姐姐都已经抽时间代替爸爸\n'
		'来陪我了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(17), Text(
		'#0809F啊哈哈，没关系没关系！\n'
		'能和小滴在一起，\n'
		'反倒是我占便宜了！{wait}'
		'{page}'
		'#0800F那就点\n'
		'我推荐的吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(17), Char(8), 500),
	Insn('TEXT_TALK', Char(17), Text(
		'#0809F姐姐！{wait}'
		'{page}'
		'请给我来一份巧克力白朗宁、\n'
		'草莓奶酪蛋糕、\n'
		'朗姆葡萄干的三合一冰淇淋！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'好的，让你们久等了，\n'
		'请尽情享用哦～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(18), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(19), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_WATCH', Char(18), Char(19), 350),
	Insn('TEXT_TALK', Char(18), Text(
		'#0906F……抱歉哦，\n'
		'艾丝蒂尔总是这么自作主张。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(19), Char(18), 500),
	Insn('TEXT_TALK', Char(19), Text(
		'#6000F没、没有的事……\n'
		'我很开心……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-7590, 3940, 20060), 0),
	Insn('CAM_ROTATE', 45, 28, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 19390, 0),
	Insn('CHAR_FLAG1_UNSET', Char(257), 128),
	Insn('CHAR_FLAG2_UNSET', Char(257), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(258), 128),
	Insn('CHAR_FLAG2_UNSET', Char(258), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(259), 128),
	Insn('CHAR_FLAG2_UNSET', Char(259), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(260), 128),
	Insn('CHAR_FLAG2_UNSET', Char(260), 32768),
	Insn('CHAR_ROTATE', Char(17), 90, 0),
	Insn('CHAR_ROTATE', Char(19), 270, 0),
	Insn('CHAR_ROTATE', Char(18), 315, 0),
	Insn('CHAR_ROTATE', Char(8), 180, 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F（小滴……\n'
		'\u3000和艾丝蒂尔他们在一起吗。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F（好像不应该去打扰呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F（不过，亚里欧斯先生\n'
		'\u3000去哪里了呢……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_POS', Char(0), (-4470, 1990, 19030), 315),
	Insn('0xB5', b'\x00\x04\x80\x00'),
	Insn('0x4C', Char(17), -1),
	Insn('0x4C', Char(18), -1),
	Insn('0x4C', Char(19), -1),
	Insn('0x4C', Char(8), -1),
	Insn('FLAG_SET', Flag(1664)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch05200', 30),
	Insn('CAM_OFFSET', (-2100, 4610, 34300), 0),
	Insn('CAM_ROTATE', 42, 28, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 21000, 0),
	Insn('CHAR_SET_CHCP', Char(24), 30),
	Insn('CHAR_SET_FRAME', Char(24), 0),
	Insn('CHAR_FLAG1_UNSET', Char(24), 128),
	Insn('CHAR_FLAG2_UNSET', Char(24), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 4),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('CHAR_SET_POS', Char(24), (-2000, 2660, 37550), 180),
	Insn('CHAR_SET_COLOR', Char(24), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(257), (-1510, 2660, 36550), 180),
	Insn('CHAR_SET_POS', Char(258), (-2710, 2660, 36550), 180),
	Insn('CHAR_SET_POS', Char(259), (-1310, 2660, 37550), 180),
	Insn('CHAR_SET_POS', Char(260), (-2910, 2660, 37550), 180),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu01800.itp'),
	Insn('OBJ_FLAG_SET', Object(5), 4096),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('OBJ_FLAG_UNSET', Object(3), 16),
	Insn('0x71', Object(3), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x03\x00'),
	Insn('CAM_OFFSET', (-2100, 4610, 31380), 4000),
	Insn('CAM_ROTATE', 34, 29, 0, 4000),
	Insn('CAM_DISTANCE', 18000, 4000),
	Insn('FORK', 257, 1, [
		Insn('0x97', Char(254), (0, 0, -5000), 2000, 0),
	]),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 1000),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x97', Char(254), (0, 0, -5000), 2000, 0),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 1000),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x97', Char(254), (0, 0, -4750), 2000, 0),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 1000),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('0x97', Char(254), (0, 0, -4750), 2000, 0),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 1000),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(257), Char(260), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(258), Char(259), 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(259), Char(258), 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('CHAR_WATCH', Char(260), Char(257), 500),
	Insn('0x71', Object(3), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x03\x00'),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0006F#12P……呼，失败失败，\n'
		'还以为可以随便进入呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F#5P那个……\n'
		'伊莉雅丄普拉提耶是谁啊？{wait}'
		'{page}'
		'真是很美丽的人呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(260), Text(
		'#0305F#5P什么！？\n'
		'你竟然不知道伊莉雅！？{wait}'
		'{page}'
		'#0309F哎呀呀，太落伍了吧～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0211F#5P（不爽）……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0102F#6P啊哈哈……\n'
		'她在克洛斯贝尔很有名哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(24), Translate('女孩的声音'), Text(
		'#2S#11P那么，我就先告辞了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('OBJ_FLAG_UNSET', Object(3), 16),
	Insn('0x71', Object(3), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x03\x00'),
	Insn('FORK', 24, 1, [
		Insn('0x97', Char(254), (0, 0, -3750), 3000, 0),
	]),
	Insn('FORK', 24, 2, [
		Insn('CHAR_SET_COLOR', Char(24), Color(0xFFFFFFFF), 1000),
	]),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(257), Char(24), 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(258), Char(24), 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(259), Char(24), 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(260), Char(24), 500),
	]),
	Insn('0x71', Object(3), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x03\x00'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('TEXT_SET_NAME', Translate('紫发的女孩')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'呃，抱歉借过一下……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_TALK', Char(257), Text(
		'#0002F#12P啊，不好意思，\n'
		'我们挡了你的路呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('0x98', Char(257), (250, 0, 0), 500, 0),
	]),
	Insn('FORK', 258, 1, [
		Insn('0x98', Char(258), (-250, 0, 0), 500, 0),
	]),
	Insn('FORK', 259, 1, [
		Insn('0x98', Char(259), (250, 0, 0), 500, 0),
	]),
	Insn('FORK', 260, 1, [
		Insn('0x98', Char(260), (-250, 0, 0), 500, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK2', Char(24), Translate('紫发的女孩'), Text(
		'#1804F#5P………………（低头行礼）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_LOOP', 0, 1, [
		Insn('CHAR_WATCH', Char(254), Char(24), 500),
	]),
	Insn('FORK_LOOP', 1, 1, [
		Insn('CHAR_WATCH', Char(254), Char(24), 500),
	]),
	Insn('FORK_LOOP', 2, 1, [
		Insn('CHAR_WATCH', Char(254), Char(24), 500),
	]),
	Insn('FORK_LOOP', 3, 1, [
		Insn('CHAR_WATCH', Char(254), Char(24), 500),
	]),
	Insn('0x95', Char(24), (-2110, 1760, 28460), 3000, 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (430, 4610, 28350), 0),
	Insn('CAM_ROTATE', 53, 17, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 28910, 0),
	Insn('0x95', Char(24), (-1750, 1990, 23060), 3000, 0),
	Insn('0x95', Char(24), (7100, 1770, 15210), 3000, 0),
	Insn('CROSSFADE', 800),
	Insn('CAM_OFFSET', (-2100, 4610, 31380), 0),
	Insn('CAM_ROTATE', 34, 29, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 18000, 0),
	Insn('FORK_QUIT', Char(0), 1),
	Insn('FORK_QUIT', Char(1), 1),
	Insn('FORK_QUIT', Char(2), 1),
	Insn('FORK_QUIT', Char(3), 1),
	Insn('0x0D'),
	Insn('CHAR_FLAG1_SET', Char(24), 128),
	Insn('CHAR_FLAG2_SET', Char(24), 32768),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F#5P好像是剧团的女孩子啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F#5P不过从没见过呢……\n'
		'是最近加入的新人吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('OBJ_FLAG_SET', Object(3), 16),
	Insn('0x71', Object(3), b'\x00\x00', 0, 0),
	Insn('OBJ_FLAG_UNSET', Object(5), 4096),
	Insn('CAM_OFFSET', (-2110, 4610, 31550), 0),
	Insn('CAM_ROTATE', 45, 25, 0, 0),
	Insn('0x6E', 800, 0),
	Insn('CAM_DISTANCE', 17500, 0),
	Insn('CHAR_SET_POS', Char(0), (-2110, 2660, 31550), 180),
	Insn('CHAR_SET_POS', Char(1), (-2110, 2660, 31550), 180),
	Insn('CHAR_SET_POS', Char(2), (-2110, 2660, 31550), 180),
	Insn('CHAR_SET_POS', Char(3), (-2110, 2660, 31550), 180),
	Insn('0xB5', b'\x01\x02\x80\x00'),
	Insn('FLAG_SET', Flag(564)),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-2110, 4610, 31550), 0),
	Insn('CAM_ROTATE', 45, 25, 0, 0),
	Insn('0x6E', 800, 0),
	Insn('CAM_DISTANCE', 17500, 0),
	Insn('CHAR_SET_POS', Char(0), (-2110, 2660, 31550), 180),
	Insn('CHAR_SET_POS', Char(1), (-2110, 2660, 31550), 180),
	Insn('CHAR_SET_POS', Char(2), (-2110, 2660, 31550), 180),
	Insn('CHAR_SET_POS', Char(3), (-2110, 2660, 31550), 180),
	Insn('0xB5', b'\x01\x02\x80\x00'),
	Insn('EVENT_END', 5),
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
		(Expr([Insn('FLAG', Flag(8)), Insn('END')]), [
			Insn('TEXT_TALK', Char(20), Text(
				'#0106F虽然总是被副局长挖苦，\n'
				'没有一点好的回忆……{wait}'
				'{page}'
				'#0100F但他很怕老婆，又喝得酩酊大醉，\n'
				'好像也有很多苦衷啊。{wait}'
				'{page}'
				'#0105F……你们两个还不累吗？\n'
				'暂时回去休息下也没事哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(20), Text(
				'#0100F怎么样，调查还顺利吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F哈哈，还算顺利……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0203F虽然赛特的嗅觉很灵敏，\n'
				'但副局长的行动路线\n'
				'很难确定，所以比较麻烦……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(20), Text(
				'#0106F果然很花时间啊。{wait}'
				'{page}'
				'#0100F如果累了，暂时回去\n'
				'休息一下也没事哦……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(8)),
		]),
	]),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, -1, 0, Text(
		'【继续调查】\n'
		'【中断调查】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0006F嗯……的确累了，\n'
				'暂时回去休息下吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0203F说得也是呢。{wait}'
				'{page}'
				'#0200F想要重新开始\n'
				'调查时，\n'
				'再拜托赛特一起去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(20), Text(
				'#0100F那先把兰迪拉上，\n'
				'一起回去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('BGM_STOP', 4000),
			Insn('BGM_WAIT'),
			Insn('FLAG_SET', Flag(1199)),
			Insn('QUEST', 21, Insn('TASK_SET', 2)),
			Insn('FLAG_SET', Flag(753)),
			Insn('NEW_SCENE', 'c0110', b'\x00\x00\x00\x07'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(20), Text(
				'#0100F是吗，虽然要加油，\n'
				'但也不要勉强哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (-26820, 1750, 11890), 0),
	Insn('CAM_ROTATE', 45, 27, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 17650, 0),
	Insn('CHAR_SET_POS', Char(259), (-26000, 0, 12000), 180),
	Insn('CHAR_SET_POS', Char(284), (-25000, 0, 11000), 180),
	Insn('CHAR_SET_POS', Char(257), (-27000, 0, 12250), 180),
	Insn('CHAR_SET_POS', Char(258), (-26000, 0, 13500), 180),
	Insn('CHAR_SET_POS', Char(260), (-27000, 0, 13750), 180),
	Insn('0x4B', Char(12), -1),
	Insn('0x4B', Char(13), -1),
	Insn('CHAR_FLAG1_SET', Char(14), 128),
	Insn('CHAR_FLAG2_SET', Char(14), 32768),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1199)), Insn('END')]), [
			Insn('FORK', 257, 1, [
				Insn('CHAR_WATCH', Char(257), Char(258), 500),
			]),
			Insn('FORK', 258, 1, [
				Insn('CHAR_WATCH', Char(258), Char(257), 500),
			]),
			Insn('FORK', 259, 1, [
				Insn('CHAR_WATCH', Char(259), Char(260), 500),
			]),
			Insn('FORK', 260, 1, [
				Insn('CHAR_WATCH', Char(260), Char(259), 500),
			]),
			Insn('FORK_AWAIT', Char(257), 1),
			Insn('FORK_AWAIT', Char(258), 1),
			Insn('FORK_AWAIT', Char(259), 1),
			Insn('FORK_AWAIT', Char(260), 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F好，那就重新\n'
				'开始调查吧。{wait}'
				'{page}'
				'艾莉和兰迪……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0309F交给我吧，随时待命！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(260), 1, Function((0, 27))),
			Insn('FORK', 257, 1, [
				Insn('CHAR_ROTATE', Char(257), 0, 500),
			]),
			Insn('FORK', 258, 1, [
				Insn('CHAR_ROTATE', Char(258), 0, 500),
			]),
			Insn('FORK', 259, 1, [
				Insn('CHAR_ROTATE', Char(259), 0, 500),
			]),
			Insn('FORK', 284, 1, [
				Insn('CHAR_ROTATE', Char(284), 315, 500),
			]),
			Insn('FORK_AWAIT', Char(257), 1),
			Insn('FORK_AWAIT', Char(258), 1),
			Insn('FORK_AWAIT', Char(259), 1),
			Insn('FORK_AWAIT', Char(284), 1),
			Insn('FORK_AWAIT', Char(260), 1),
			Insn('SLEEP', 400),
			Insn('FORK', 257, 1, [
				Insn('CHAR_WATCH', Char(257), Char(258), 500),
			]),
			Insn('FORK', 258, 1, [
				Insn('CHAR_WATCH', Char(258), Char(257), 500),
			]),
			Insn('FORK', 259, 1, [
				Insn('CHAR_ROTATE', Char(259), 315, 500),
			]),
			Insn('FORK_AWAIT', Char(257), 1),
			Insn('FORK_AWAIT', Char(258), 1),
			Insn('FORK_AWAIT', Char(259), 1),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F我在那边的\n'
				'露天店旁待命。{wait}'
				'{page}'
				'罗伊德、缇欧，\n'
				'你们加油哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('TASK_GET', 5))), Insn('END')]), [
					Insn('0x1B', 1, Function((0, 36)), 0),
					Insn('0x1B', 2, Function((0, 37)), 0),
					Insn('0x1B', 3, Function((0, 38)), 0),
					Insn('0x1B', 4, Function((0, 39)), 0),
					Insn('0x1B', 5, Function((0, 40)), 0),
					Insn('0x1B', 6, Function((0, 41)), 0),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('TASK_GET', 1))), Insn('END')]), [
					Insn('0x66', 0, 1),
					Insn('0x66', 1, 1),
					Insn('0x66', 2, 1),
					Insn('0x66', 3, 1),
					Insn('0x66', 4, 1),
					Insn('0x1B', 0, Function((0, 35)), 0),
					Insn('0x1B', 1, Function((0, 36)), 0),
					Insn('0x1B', 2, Function((0, 37)), 0),
					Insn('0x1B', 3, Function((0, 38)), 0),
					Insn('0x1B', 5, Function((0, 40)), 0),
					Insn('0x1B', 6, Function((0, 41)), 0),
				]),
				(None, []),
			]),
			Insn('FLAG_UNSET', Flag(1199)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0001F那么……副局长\n'
				'当时是往哪个方向去了呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(284), Text(
				'#11P#1200F………（嗅嗅）…………{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_ROTATE', Char(284), 90, 500),
			Insn('TEXT_TALK', Char(284), Text(
				'#11P#1200F呜噜噜噜………{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 257, 1, [
				Insn('CHAR_ROTATE', Char(257), 90, 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 258, 1, [
				Insn('CHAR_ROTATE', Char(258), 90, 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 259, 1, [
				Insn('CHAR_ROTATE', Char(259), 90, 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 260, 1, [
				Insn('CHAR_ROTATE', Char(260), 90, 500),
			]),
			Insn('FORK_AWAIT', Char(257), 1),
			Insn('FORK_AWAIT', Char(258), 1),
			Insn('FORK_AWAIT', Char(259), 1),
			Insn('FORK_AWAIT', Char(260), 1),
			Insn('TEXT_TALK', Char(259), Text(
				'#11P#0200F好像是……往东去了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 257, 1, [
				Insn('CHAR_WATCH', Char(257), Char(258), 500),
			]),
			Insn('FORK', 258, 1, [
				Insn('CHAR_WATCH', Char(258), Char(257), 500),
			]),
			Insn('FORK', 259, 1, [
				Insn('CHAR_WATCH', Char(259), Char(260), 500),
			]),
			Insn('FORK', 260, 1, [
				Insn('CHAR_WATCH', Char(260), Char(259), 500),
			]),
			Insn('FORK_AWAIT', Char(257), 1),
			Insn('FORK_AWAIT', Char(258), 1),
			Insn('FORK_AWAIT', Char(259), 1),
			Insn('FORK_AWAIT', Char(260), 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0004F那好，接下来就\n'
				'借助赛特的嗅觉\n'
				'来查明副局长的行动路线吧。{wait}'
				'{page}'
				'#0000F在行走过程中，也必须注意\n'
				'路上有没有掉落什么东西。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#11P#0105F不过，罗伊德，\n'
				'全员都参加调查的话，人数有点太多了吧？{wait}'
				'{page}'
				'#0100F而且调查范围只限欢乐街，\n'
				'减少一些人数比较好吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0003F也是……确实是多了。{wait}'
				'{page}'
				'#0000F艾莉、兰迪，\n'
				'能不能请你们暂时待命呢？{wait}'
				'{page}'
				'等我们把范围缩小点后，\n'
				'再请你们帮忙。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_ROTATE', Char(260), 0, 500),
			Insn('TEXT_TALK', Char(260), Text(
				'#5P#0304F收到，我随时待命。{wait}'
				'{page}'
				'#0309F嗯～今天要玩些什么呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(260), 1, Function((0, 27))),
			Insn('FORK', 257, 1, [
				Insn('CHAR_ROTATE', Char(257), 0, 500),
			]),
			Insn('FORK', 258, 1, [
				Insn('CHAR_ROTATE', Char(258), 0, 500),
			]),
			Insn('FORK', 259, 1, [
				Insn('CHAR_ROTATE', Char(259), 0, 500),
			]),
			Insn('FORK', 284, 1, [
				Insn('CHAR_ROTATE', Char(284), 315, 500),
			]),
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0005F啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_AWAIT', Char(257), 1),
			Insn('FORK_AWAIT', Char(258), 1),
			Insn('FORK_AWAIT', Char(259), 1),
			Insn('FORK_AWAIT', Char(284), 1),
			Insn('FORK_AWAIT', Char(260), 1),
			Insn('TEXT_TALK', Char(259), Text(
				'#11P#0211F完全来不及阻止他。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 257, 1, [
				Insn('CHAR_WATCH', Char(257), Char(258), 500),
			]),
			Insn('FORK', 258, 1, [
				Insn('CHAR_WATCH', Char(258), Char(257), 500),
			]),
			Insn('FORK', 259, 1, [
				Insn('CHAR_ROTATE', Char(259), 315, 500),
			]),
			Insn('FORK_AWAIT', Char(257), 1),
			Insn('FORK_AWAIT', Char(258), 1),
			Insn('FORK_AWAIT', Char(259), 1),
			Insn('TEXT_TALK', Char(258), Text(
				'#11P#0106F他总是那个样子……{wait}'
				'{page}'
				'#0100F好吧，到时候\n'
				'再叫他就好。{wait}'
				'{page}'
				'罗伊德，我就在那边的\n'
				'露天店旁待命。\n'
				'需要帮助时就叫我。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F知道了，\n'
				'我会的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_WATCH', Char(258), Char(259), 500),
			Insn('TEXT_TALK', Char(258), Text(
				'#5P#0100F缇欧、赛特，\n'
				'一会见啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 1, Function((0, 28))),
			Insn('FORK_FUNC', Char(259), 1, Function((0, 28))),
			Insn('FORK_FUNC', Char(284), 1, Function((0, 28))),
			Insn('0x97', Char(258), (2000, 0, 0), 2000, 1),
			Insn('0x97', Char(258), (2000, 0, -2000), 2000, 1),
			Insn('0x97', Char(258), (3000, 0, 0), 2000, 1),
			Insn('0x97', Char(258), (8000, 0, 6000), 2000, 1),
			Insn('FORK_QUIT', Char(257), 1),
			Insn('FORK_QUIT', Char(259), 1),
			Insn('FORK_QUIT', Char(284), 1),
			Insn('FORK', 259, 1, [
				Insn('CHAR_WATCH', Char(259), Char(257), 500),
			]),
			Insn('FORK', 284, 1, [
				Insn('CHAR_ROTATE', Char(284), 270, 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 257, 1, [
				Insn('CHAR_WATCH', Char(257), Char(259), 500),
			]),
			Insn('FORK_AWAIT', Char(257), 1),
			Insn('FORK_AWAIT', Char(259), 1),
			Insn('FORK_AWAIT', Char(284), 1),
			Insn('TEXT_TALK', Char(259), Text(
				'#11P#0200F那么，我们开始吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F嗯，开始吧。{wait}'
				'{page}'
				'我们走前面……\n'
				'赛特，如果我们走错路了，\n'
				'你要提醒一下哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(284), Text(
				'#11P#1200F呜～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x66', 0, 1),
			Insn('0x66', 1, 1),
			Insn('0x66', 2, 1),
			Insn('0x66', 3, 1),
			Insn('0x66', 4, 1),
			Insn('0x1B', 0, Function((0, 35)), 0),
			Insn('0x1B', 1, Function((0, 36)), 0),
			Insn('0x1B', 2, Function((0, 37)), 0),
			Insn('0x1B', 3, Function((0, 38)), 0),
			Insn('0x1B', 5, Function((0, 40)), 0),
			Insn('0x1B', 6, Function((0, 41)), 0),
			Insn('QUEST', 21, Insn('TASK_SET', 1)),
		]),
	]),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_FLAG1_SET', Char(258), 128),
	Insn('CHAR_FLAG2_SET', Char(258), 32768),
	Insn('CHAR_FLAG1_SET', Char(260), 128),
	Insn('CHAR_FLAG2_SET', Char(260), 32768),
	Insn('0x49'),
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
	Insn('0x2F', b'\x03\x00'),
	Insn('CAM_OFFSET', (-26500, 1950, 12000), 0),
	Insn('CAM_ROTATE', 40, 8, 0, 0),
	Insn('0x6E', 800, 0),
	Insn('CAM_DISTANCE', 16500, 0),
	Insn('CHAR_SET_POS', Char(257), (-26500, 0, 12000), 180),
	Insn('CHAR_SET_POS', Char(259), (-26500, 0, 12000), 180),
	Insn('CHAR_SET_POS', Char(284), (-26500, 0, 12000), 180),
	Insn('CHAR_FLAG1_UNSET', Char(20), 128),
	Insn('0x4C', Char(12), -1),
	Insn('0x4C', Char(13), -1),
	Insn('CHAR_FLAG1_UNSET', Char(14), 128),
	Insn('CHAR_FLAG2_UNSET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(16), 128),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('0x97', Char(260), (0, 0, 3000), 2000, 0),
	Insn('OBJ_FLAG_UNSET', Object(1), 16),
	Insn('0x71', Object(1), b'\x00\x00', 5, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x01\x00'),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 1500),
	]),
	Insn('0x97', Char(260), (0, 0, 3000), 2000, 0),
	Insn('0x71', Object(1), b'\x05\x00', 0, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x01\x00'),
	Insn('OBJ_FLAG_SET', Object(1), 16),
	Insn('RETURN'),
]

data['code'][28] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
		Insn('SLEEP', 100),
	]),
	Insn('RETURN'),
]

data['code'][29] = [
	Insn('TEXT_START', Char(255)),
	Insn('TEXT_TALK', Char(284), Text(
		'#1200F（嗅嗅）………{wait}'
		'{page}'
		'……呜～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F哦……\n'
		'这应该对了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F嗯，应该就是\n'
		'这条路没错了。{wait}'
		'{page}'
		'就这样前进吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('QUEST', 21, Insn('TASK_SET', 3)),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][30] = [
	Insn('TEXT_START', Char(255)),
	Insn('TEXT_TALK', Char(284), Text(
		'#1200F（嗅嗅）………{wait}'
		'{page}'
		'……呜～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F哦……\n'
		'这里残留有气味吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F看来副局长\n'
		'在这里休息过一阵子。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('QUEST', 21, Insn('TASK_SET', 4)),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][31] = [
	Insn('TEXT_START', Char(255)),
	Insn('TEXT_TALK', Char(284), Text(
		'#1200F（嗅嗅）………{wait}'
		'{page}'
		'呜噜噜……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0003F似乎……不是这里啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F是的，好像没有\n'
		'什么气味。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][32] = [
	Insn('TEXT_START', Char(255)),
	Insn('TEXT_TALK', Char(284), Text(
		'#1200F（嗅嗅）………{wait}'
		'{page}'
		'呜噜噜……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0003F似乎……不是这里啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F是的，好像没有\n'
		'什么气味。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][33] = [
	Insn('TEXT_START', Char(255)),
	Insn('TEXT_TALK', Char(284), Text(
		'#1200F（嗅嗅）………{wait}'
		'{page}'
		'呜噜噜……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0003F似乎……不是这里啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F是的，好像没有\n'
		'什么气味。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][34] = [
	Insn('CHAR_WATCH', Char(284), Char(0), 0),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(10)), Insn('END')]), [
			Insn('TEXT_TALK', Char(284), Text(
				'#1200F……呜～！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F（好像不是这条路。）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(284), Text(
				'#1200F……呜～！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
			Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F不、不是这边吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F好像不是\n'
				'这个方向……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(10)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][35] = [
	Insn('EVENT_BEGIN', 1),
	Insn('CALL', Function((0, 34))),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (13270, 0, -19100), 315),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][36] = [
	Insn('EVENT_BEGIN', 1),
	Insn('CALL', Function((0, 34))),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (20770, 0, 12930), 270),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][37] = [
	Insn('EVENT_BEGIN', 1),
	Insn('CALL', Function((0, 34))),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (-39280, 0, 12420), 90),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][38] = [
	Insn('EVENT_BEGIN', 1),
	Insn('CALL', Function((0, 34))),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (-2110, 2660, 34550), 180),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][39] = [
	Insn('EVENT_BEGIN', 1),
	Insn('CALL', Function((0, 34))),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (17100, 2060, 23000), 270),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][40] = [
	Insn('EVENT_BEGIN', 1),
	Insn('CALL', Function((0, 34))),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (13690, 90, -6130), 270),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][41] = [
	Insn('EVENT_BEGIN', 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#0003F没有必要调查赌场。\n'
		'……去其它地方调查看看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (-26470, 300, 16370), 180),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][42] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (12420, 1000, -5920), 0),
	Insn('CAM_ROTATE', 45, 25, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 17500, 0),
	Insn('CHAR_SET_POS', Char(284), (11520, 0, -5920), 270),
	Insn('CHAR_SET_POS', Char(259), (12100, 0, -5140), 270),
	Insn('CHAR_SET_POS', Char(257), (12680, 0, -6570), 270),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0005F副局长……\n'
		'喝醉后穿过了饭店吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#5P#0206F典型的\n'
		'醉汉行为啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(259), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0000F是啊，不过他好像\n'
		'没在饭店落下什么东西。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(284), 180, 500),
	Insn('TEXT_TALK', Char(284), Text(
		'#6P#1200F呜噜噜噜噜……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('CHAR_ROTATE', Char(259), 180, 750),
	Insn('SLEEP', 750),
	Insn('TEXT_TALK', Char(259), Text(
		'#5P#0200F……接下来\n'
		'好像往南边去了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 180, 750),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0000F那好，我们走吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x65', 0, 1),
	Insn('0x65', 1, 1),
	Insn('0x65', 2, 1),
	Insn('0x65', 3, 1),
	Insn('0x65', 4, 1),
	Insn('0x1B', 0, Function((255, 255)), 255),
	Insn('0x1B', 1, Function((0, 36)), 0),
	Insn('0x1B', 2, Function((0, 37)), 0),
	Insn('0x1B', 3, Function((0, 38)), 0),
	Insn('0x1B', 4, Function((0, 39)), 0),
	Insn('0x1B', 5, Function((0, 40)), 0),
	Insn('0x1B', 6, Function((0, 41)), 0),
	Insn('CHAR_SET_POS', Char(0), (11520, 0, -5920), 270),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG2_UNSET', Char(12), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(13), 128),
	Insn('CHAR_FLAG2_UNSET', Char(13), 32768),
	Insn('QUEST', 21, Insn('TASK_SET', 5)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][43] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x0A', 268435456),
	Insn('LOAD_CHCP', 'chr/ch34600', 30),
	Insn('LOAD_CHCP', 'chr/ch32400', 31),
	Insn('LOAD_CHCP', 'chr/ch34300', 32),
	Insn('LOAD_CHCP', 'chr/ch32200', 33),
	Insn('CHAR_FLAG1_UNSET', Char(27), 128),
	Insn('CHAR_FLAG2_UNSET', Char(27), 32768),
	Insn('CHAR_SET_CHCP', Char(27), 30),
	Insn('CHAR_SET_FRAME', Char(27), 0),
	Insn('CHAR_SET_POS', Char(27), (-1900, 1990, 20550), 180),
	Insn('CHAR_FLAG1_UNSET', Char(28), 128),
	Insn('CHAR_FLAG2_UNSET', Char(28), 32768),
	Insn('CHAR_SET_CHCP', Char(28), 31),
	Insn('CHAR_SET_FRAME', Char(28), 0),
	Insn('CHAR_SET_POS', Char(28), (-1900, 1990, 17860), 0),
	Insn('CHAR_FLAG1_UNSET', Char(29), 128),
	Insn('CHAR_FLAG2_UNSET', Char(29), 32768),
	Insn('CHAR_SET_CHCP', Char(29), 32),
	Insn('CHAR_SET_FRAME', Char(29), 0),
	Insn('CHAR_SET_POS', Char(29), (-3280, 1990, 18520), 45),
	Insn('CHAR_FLAG1_UNSET', Char(30), 128),
	Insn('CHAR_FLAG2_UNSET', Char(30), 32768),
	Insn('CHAR_SET_CHCP', Char(30), 33),
	Insn('CHAR_SET_FRAME', Char(30), 0),
	Insn('CHAR_SET_POS', Char(30), (-590, 1990, 18520), 315),
	Insn('CHAR_FLAG1_SET', Char(27), 32768),
	Insn('CHAR_FLAG1_SET', Char(28), 32768),
	Insn('CHAR_FLAG1_SET', Char(29), 32768),
	Insn('CHAR_FLAG1_SET', Char(30), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 32768),
	Insn('OBJ_FLAG_SET', Object(5), 4096),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CAM_OFFSET', (-26220, 4050, 12750), 0),
	Insn('CAM_ROTATE', 32, 14, 0, 0),
	Insn('0x6E', 800, 0),
	Insn('CAM_DISTANCE', 15680, 0),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (13510, 1950, -6620), 7000),
	Insn('CAM_ROTATE', 56, 21, 0, 7000),
	Insn('0x6E', 800, 7000),
	Insn('CAM_DISTANCE', 16000, 7000),
	Insn('0x6F', b'y'),
	Insn('SLEEP', 500),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-1890, 8610, 32520), 0),
	Insn('CAM_ROTATE', 0, 10, 0, 0),
	Insn('0x6E', 800, 0),
	Insn('CAM_DISTANCE', 25500, 0),
	Insn('CAM_OFFSET', (-2990, 3940, 18300), 8000),
	Insn('CAM_ROTATE', 41, 29, 0, 8000),
	Insn('0x6E', 800, 8000),
	Insn('CAM_DISTANCE', 39500, 8000),
	Insn('0xCB', b'T\x01\xc8\x00', 'c_plac07', b'\x00\xa0\x0f'),
	Insn('0x6F', b'y'),
	Insn('SLEEP', 1000),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(527)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_MESSAGE', Char(257), Text(
				'#0005F嗯？那是……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('CROSSFADE', 500),
			Insn('CAM_DISTANCE', 15000, 0),
			Insn('0x0D'),
			Insn('TEXT_TALK', Char(28), Text(
				'#12P……哇，好棒啊！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(29), Text(
				'#6P这就是那个世界第一的\n'
				'著名剧团『彩虹』吧！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(30), Text(
				'#11P嗯，听说这个剧团的\n'
				'门票很贵……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(27), Text(
				'#5P各位，你们还尽兴吗？\n'
				'那么，就出发去下一个地方吧！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_ROTATE', Char(27), 90, 500),
			Insn('EMOTE', Char(29), 0, 2000, (38, 39, 250, 2)),
			Insn('FORK', 27, 1, [
				Insn('0x95', Char(254), (-160, 1990, 19900), 1500, 0),
			]),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(29), Text(
				'#6P咦咦～不去观看\n'
				'彩虹剧团的公演吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_AWAIT', Char(27), 1),
			Insn('CHAR_ROTATE', Char(27), 225, 500),
			Insn('TEXT_TALK', Char(27), Text(
				'#11P呵呵，其实今天的公演\n'
				'只有夜间场。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(27), Text(
				'#11P晚上是自由活动时间，\n'
				'请各位剧团爱好者\n'
				'一定要来捧场。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(27), Text(
				'#11P……接下来，\n'
				'我将带各位去……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 27, 1, [
				Insn('CHAR_ROTATE', Char(254), 90, 500),
			]),
			Insn('FORK', 30, 1, [
				Insn('CHAR_ROTATE', Char(254), 135, 500),
			]),
			Insn('FORK', 28, 1, [
				Insn('CHAR_ROTATE', Char(254), 135, 500),
			]),
			Insn('FORK', 29, 1, [
				Insn('CHAR_ROTATE', Char(254), 135, 500),
			]),
			Insn('FORK_AWAIT', Char(27), 1),
			Insn('FORK', 27, 1, [
				Insn('0x95', Char(254), (6940, 1760, 13750), 2000, 0),
			]),
			Insn('SLEEP', 1000),
			Insn('FORK_AWAIT', Char(30), 1),
			Insn('FORK', 30, 1, [
				Insn('0x95', Char(254), (6940, 1760, 13750), 2000, 0),
			]),
			Insn('SLEEP', 500),
			Insn('FORK_AWAIT', Char(28), 1),
			Insn('FORK', 28, 1, [
				Insn('0x95', Char(254), (6940, 1760, 13750), 2000, 0),
			]),
			Insn('SLEEP', 300),
			Insn('FORK_AWAIT', Char(29), 1),
			Insn('FORK', 29, 1, [
				Insn('0x95', Char(254), (6940, 1760, 13750), 2000, 0),
			]),
			Insn('FORK_AWAIT', Char(27), 1),
			Insn('FORK', 27, 1, [
				Insn('0x95', Char(254), (22200, 0, 12150), 2000, 0),
			]),
			Insn('FORK_AWAIT', Char(30), 1),
			Insn('FORK', 30, 1, [
				Insn('0x95', Char(254), (22200, 0, 12150), 2000, 0),
			]),
			Insn('FORK_AWAIT', Char(28), 1),
			Insn('FORK', 28, 1, [
				Insn('0x95', Char(254), (22200, 0, 12150), 2000, 0),
			]),
			Insn('FORK_AWAIT', Char(29), 1),
			Insn('FORK', 29, 1, [
				Insn('0x95', Char(254), (22200, 0, 12150), 2000, 0),
			]),
			Insn('TEXT_MESSAGE', Char(260), Text(
				'#0300F虽然我也来这附近玩不少次……\n'
				'不过这里常看见很多游客呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_MESSAGE', Char(257), Text(
				'#0000F嗯，最近有很多外国人\n'
				'乘坐导力巴士来这里观光。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_MESSAGE', Char(258), Text(
				'#0104F这条欢乐街\n'
				'好像是游客必来的地方。{wait}'
				'{page}'
				'#0100F如果外国人发生了什么事，\n'
				'就可能会演变为国际问题……\n'
				'所以我们警察的工作很重要呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_MESSAGE', Char(259), Text(
				'#0200F原来如此，确实有道理。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
		]),
		(None, []),
	]),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}欢乐街是位于城市北侧的商业区。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}饭店、有名的剧场等设施鳞次栉比，\n'
		'并有许多游客前来游玩。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}有一些设施在前期并不会开放，\n'
		'但随着故事的展开，\n'
		'可以前去拜访一番。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_FLAG1_UNSET', Char(27), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(28), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(29), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(30), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(12), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(13), 32768),
	Insn('OBJ_FLAG_UNSET', Object(5), 4096),
	Insn('FORK_QUIT', Char(27), 1),
	Insn('FORK_QUIT', Char(28), 1),
	Insn('FORK_QUIT', Char(29), 1),
	Insn('FORK_QUIT', Char(30), 1),
	Insn('CHAR_FLAG1_SET', Char(27), 128),
	Insn('CHAR_FLAG2_SET', Char(27), 32768),
	Insn('CHAR_FLAG1_SET', Char(28), 128),
	Insn('CHAR_FLAG2_SET', Char(28), 32768),
	Insn('CHAR_FLAG1_SET', Char(29), 128),
	Insn('CHAR_FLAG2_SET', Char(29), 32768),
	Insn('CHAR_FLAG1_SET', Char(30), 128),
	Insn('CHAR_FLAG2_SET', Char(30), 32768),
	Insn('0x49'),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0xD5', 33),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('FORK_QUIT', Char(12), 0),
	Insn('CHAR_SET_POS', Char(12), (-50000, 10, 12070), 220),
	Insn('FORK_FUNC', Char(12), 0, Function((0, 2))),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 101), Insn('EQ'), Insn('END')]), [
			Insn('CAM_OFFSET', (21040, 1950, 11840), 0),
			Insn('CAM_ROTATE', 45, 25, 0, 0),
			Insn('0x6E', 800, 0),
			Insn('CAM_DISTANCE', 17500, 0),
		]),
		(Expr([Insn('ATTR', 0), Insn('CONST', 100), Insn('EQ'), Insn('END')]), [
			Insn('CAM_OFFSET', (13270, 1950, -19100), 0),
			Insn('CAM_ROTATE', 40, 8, 0, 0),
			Insn('0x6E', 800, 0),
			Insn('CAM_DISTANCE', 16500, 0),
		]),
		(Expr([Insn('ATTR', 0), Insn('CONST', 102), Insn('EQ'), Insn('END')]), [
			Insn('CAM_OFFSET', (-39280, 1950, 12420), 0),
			Insn('CAM_ROTATE', 40, 8, 0, 0),
			Insn('0x6E', 800, 0),
			Insn('CAM_DISTANCE', 16500, 0),
		]),
		(None, []),
	]),
	Insn('FLAG_SET', Flag(552)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][44] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-13000, 7940, 33500), 0),
	Insn('CAM_ROTATE', 40, 33, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 23000, 0),
	Insn('CHAR_SET_POS', Char(257), (-2700, 1990, 21500), 0),
	Insn('CHAR_SET_POS', Char(260), (-1300, 1990, 21500), 0),
	Insn('CHAR_SET_POS', Char(259), (-2700, 1990, 20300), 0),
	Insn('CHAR_SET_POS', Char(258), (-1300, 1990, 20300), 0),
	Insn('CHAR_FLAG1_SET', Char(257), 8),
	Insn('CHAR_FLAG1_SET', Char(258), 8),
	Insn('CHAR_FLAG1_SET', Char(259), 8),
	Insn('CHAR_FLAG1_SET', Char(260), 8),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('CAM_OFFSET', (4000, 7940, 33500), 6000),
	Insn('CAM_ROTATE', 40, 13, 0, 6000),
	Insn('CAM_DISTANCE', 30000, 6000),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('SLEEP', 500),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-2000, 11940, 34000), 0),
	Insn('CAM_ROTATE', 31, -13, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 28000, 0),
	Insn('CAM_ROTATE', 21, -13, 0, 9000),
	Insn('CAM_DISTANCE', 37000, 9000),
	Insn('0xCB', b'T\x01\xc8\x00', 'c_plac11', b'\x00\x88\x13'),
	Insn('0x6F', b'y'),
	Insn('SLEEP', 500),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-2000, 2740, 24500), 0),
	Insn('CAM_ROTATE', 32, 17, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 21000, 0),
	Insn('CAM_DISTANCE', 19950, 0),
	Insn('CHAR_FLAG1_UNSET', Char(257), 8),
	Insn('CHAR_FLAG1_UNSET', Char(258), 8),
	Insn('CHAR_FLAG1_UNSET', Char(259), 8),
	Insn('CHAR_FLAG1_UNSET', Char(260), 8),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100387V#4P#0202F仔细一看……\n'
		'还真是一座很气派的建筑物啊。{wait}'
		'{page}'
		'#12100388V而且感觉还很新。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100389V#0104F大概建有二十年了吧。{wait}'
		'{page}'
		'#12100390V#0100F与市政厅那些建筑相比，\n'
		'这里并不算很老。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100391V#6P#0003F（彩虹剧团吗……）{wait}'
		'{page}'
		'#12100392V#0008F（小时候，\n'
		'\u3000大哥和赛西儿姐姐带我\n'
		'\u3000来过几次……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_WATCH', Char(260), Char(257), 500),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100393V#0305F#11P怎么啦？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100394V#6P#0004F不……没什么。{wait}'
		'{page}'
		'#12100395V#0000F我们快点进去调查吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (-2000, 1990, 19500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG2_UNSET', Char(11), 32768),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('0xB5', b'\x00\x05\x80\x00'),
	Insn('FLAG_SET', Flag(1027)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][45] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (-2000, 3760, 35000), 0),
	Insn('CAM_ROTATE', 25, 27, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(257), (-2700, 2660, 35500), 180),
	Insn('CHAR_SET_POS', Char(258), (-1300, 2660, 35500), 180),
	Insn('CHAR_SET_POS', Char(259), (-2700, 2660, 36900), 180),
	Insn('CHAR_SET_POS', Char(260), (-1300, 2660, 36900), 180),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('OBJ_FLAG_SET', Object(5), 4096),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('SLEEP', 500),
	Insn('OBJ_FLAG_UNSET', Object(3), 16),
	Insn('0x71', Object(3), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x03\x00'),
	Insn('CAM_OFFSET', (-2000, 2860, 27500), 5000),
	Insn('CAM_ROTATE', 45, 27, 0, 5000),
	Insn('CAM_DISTANCE', 18000, 5000),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (-2700, 1760, 26800), 2000, 0),
	]),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 250),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (-1300, 1760, 26800), 2000, 0),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (-2700, 1760, 28200), 2000, 0),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 250),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (-1300, 1760, 28200), 2000, 0),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 1000),
	Insn('0x71', Object(3), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x03\x00'),
	Insn('OBJ_FLAG_SET', Object(3), 16),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 315, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100611V#5P#0303F那么……要怎么做呢？{wait}'
		'{page}'
		'#12100612V#0301F眼下，线索只有\n'
		'『鲁巴彻』这一个。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100613V#0200F『银』这个名字\n'
		'也勉强可以算是一条线索……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100614V#6P#0008F……是啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100615V#6P#0003F──各位。{wait}'
		'{page}'
		'#12100616V#0013F我们去拜访\n'
		'一下『鲁巴彻商会』吧？{wait}'
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
	Insn('FORK_AWAIT', Char(258), 2),
	Insn('FORK_AWAIT', Char(259), 2),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100617V#0105F#11P哎……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100618V#5P#0301F真的假的……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100619V#6P#0000F只是作为警察对案件的调查，\n'
		'去进行一下普通的案情询问而已。{wait}'
		'{page}'
		'#12100620V#0003F虽然还不确定恐吓信\n'
		'是不是鲁巴彻的会长\n'
		'寄出的……{wait}'
		'{page}'
		'#12100621V#0001F但我觉得如果一直避开麻烦，\n'
		'是没办法找出真相的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100622V#5P#0303F嗯……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100623V#0201F#5P……确实有一定的道理。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100624V#6P#0006F而且，我觉得这也是一个好机会。{wait}'
		'{page}'
		'#12100625V#0008F做了那种事还能在市里\n'
		'大摇大摆，四处横行的家伙……{wait}'
		'{page}'
		'#12100626V#0013F我们或许可以借此机会，\n'
		'对他们的真实情况一探究竟。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100627V#5P#0302F嗯……原来如此啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('SLEEP', 300),
	Insn('EMOTE_STOP', Char(258)),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100628V#6P#0005F那个，果然还是会担心吗？{wait}'
		'{page}'
		'#12100629V#0000F如果是的话，\n'
		'就由我和兰迪两个人……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(259), Char(257), 500),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100630V#0211F#5P罗伊德前辈……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 3)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100631V#6P#0011F不、不是！\n'
		'我并没有那个意思。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100632V#0104F#11P不……\n'
		'我们并没有担心。{wait}'
		'{page}'
		'#12100633V#0108F嗯，我觉得只是前去拜访的话\n'
		'并不会那么危险。{wait}'
		'{page}'
		'#12100634V这个城市中的黑手党\n'
		'到底是何种存在……{wait}'
		'{page}'
		'#12100635V#0102F这也是个了解他们的好机会吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 2),
	Insn('FORK_AWAIT', Char(259), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100636V#6P#0005F啊，是啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100637V#5P#0305F什么啊，大小姐。\n'
		'你是不是话里有话啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100638V#0104F#11P呵呵，那是你的错觉吧。{wait}'
		'{page}'
		'#12100639V#0100F而关于恐吓信，\n'
		'也有可能会发现一些\n'
		'预料之外的真相呢。{wait}'
		'{page}'
		'#12100640V我们快点去拜访一趟吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12100641V#6P#0000F是啊……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12100642V#0203F#5P根据数据库的情报……{wait}'
		'{page}'
		'#12100643V#0201F『鲁巴彻商会』的大楼\n'
		'在小巷中间\n'
		'小路的最深处。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12100644V#5P#0304F哎，在那么奇怪偏僻的角落啊。{wait}'
		'{page}'
		'#12100645V#0300F怪不得经常能在小巷看到那些家伙，\n'
		'原来那里就是黑手党的据点啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CAM_DISTANCE', 18150, 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(0), (-2000, 1760, 26500), 180),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG2_UNSET', Char(11), 32768),
	Insn('OBJ_FLAG_UNSET', Object(5), 4096),
	Insn('FLAG_SET', Flag(1030)),
	Insn('QUEST', 66, Insn('TASK_SET', 3)),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][46] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0xFFFFFFFF), 0),
	Insn('FADE_ON', 500, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FADE_OFF', 0, Color(0xFFFFFFFF)),
	Insn('0xE0', b'\x01'),
	Insn('LOAD_CHCP', 'chr/ch05800', 30),
	Insn('LOAD_CHCP', 'chr/ch02300', 31),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu02500.itp'),
	Insn('CAM_OFFSET', (-2000, 3000, 20500), 0),
	Insn('CAM_ROTATE', 45, 23, 0, 0),
	Insn('0x6E', 480, 0),
	Insn('CAM_DISTANCE', 20500, 0),
	Insn('CHAR_SET_POS', Char(257), (-1500, 1990, 16500), 0),
	Insn('CHAR_SET_POS', Char(258), (-2700, 1990, 16500), 0),
	Insn('CHAR_SET_POS', Char(259), (-2700, 1990, 15300), 0),
	Insn('CHAR_SET_POS', Char(260), (-1500, 1990, 15300), 0),
	Insn('CHAR_SET_CHCP', Char(21), 30),
	Insn('CHAR_SET_FRAME', Char(21), 0),
	Insn('CHAR_FLAG1_UNSET', Char(21), 128),
	Insn('CHAR_FLAG2_UNSET', Char(21), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(21), 4),
	Insn('CHAR_FLAG1_SET', Char(21), 32768),
	Insn('CHAR_SET_COLOR', Char(21), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(21), (-2000, 2660, 36000), 180),
	Insn('CHAR_SET_CHCP', Char(22), 31),
	Insn('CHAR_SET_FRAME', Char(22), 0),
	Insn('CHAR_FLAG1_UNSET', Char(22), 128),
	Insn('CHAR_FLAG2_UNSET', Char(22), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(22), 4),
	Insn('CHAR_FLAG1_SET', Char(22), 32768),
	Insn('CHAR_SET_COLOR', Char(22), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(22), (-2600, 2660, 36000), 180),
	Insn('CHAR_FLAG1_UNSET', Char(23), 128),
	Insn('0x78', b'\x04', Char(23)),
	Insn('OBJ_SET_FRAME', Object(4), 'light', Insn('0', 1)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(23), (-5300, 0, 1800), 100),
	Insn('0xD3', Char(23), 0, 100000, 0, 0),
	Insn('OBJ_FLAG_SET', Object(4), 4096),
	Insn('0x74', Object(4), 7680),
	Insn('0x70', Object(4), b'\x00\x00'),
	Insn('OBJ_FLAG_UNSET', Object(3), 16),
	Insn('OBJ_FLAG_SET', Object(5), 4096),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (-2700, 1990, 20500), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (-1500, 1990, 20500), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (-2700, 1990, 19300), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (-1500, 1990, 19300), 2000, 0),
	]),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('0x71', Object(3), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x03\x00'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101235V#11P#0005F咦……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('CAM_OFFSET', (-2000, 3600, 32000), 2000),
	Insn('0x6F', b'\x01'),
	Insn('FORK', 21, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 21, 1, [
		Insn('0x95', Char(254), (-2000, 2660, 31800), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 22, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 22, 1, [
		Insn('0x95', Char(254), (-2600, 2660, 32500), 2000, 0),
	]),
	Insn('SLEEP', 700),
	Insn('0x71', Object(3), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x03\x00'),
	Insn('OBJ_FLAG_SET', Object(3), 16),
	Insn('FORK_AWAIT', Char(21), 1),
	Insn('FORK_AWAIT', Char(22), 1),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101236V#0105F#1P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(21), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(22), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK2', Char(21), Translate('老绅士'), Text(
		'#12101237V#2505F#5P哦……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(22), Translate('年轻男性'), Text(
		'#12101238V#2605F#5P艾莉小姐……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 21, 1, [
		Insn('0x95', Char(254), (-2000, 1990, 24000), 2000, 0),
	]),
	Insn('SLEEP', 250),
	Insn('FORK', 22, 1, [
		Insn('0x96', Char(254), (-2700, 1990, 24700), 2000, 0),
	]),
	Insn('SLEEP', 2000),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-2000, 3000, 22800), 0),
	Insn('CAM_ROTATE', 40, 23, 0, 0),
	Insn('0x6E', 480, 0),
	Insn('CAM_DISTANCE', 20000, 0),
	Insn('CHAR_SET_POS', Char(258), (-2000, 1990, 21000), 0),
	Insn('CHAR_SET_POS', Char(257), (100, 1990, 21200), 315),
	Insn('CHAR_SET_POS', Char(259), (-1500, 1990, 20200), 0),
	Insn('CHAR_SET_POS', Char(260), (-700, 1990, 19600), 0),
	Insn('CAM_DISTANCE', 19000, 2000),
	Insn('0x0D'),
	Insn('SLEEP', 600),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (-2000, 1990, 21700), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(21), 1),
	Insn('FORK_AWAIT', Char(22), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101239V#0105F#12P外公……阿奈斯特先生。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101240V#0005F（咦……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101241V#0205F#4P（艾莉前辈的外公……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_NAME', Translate('老绅士')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#12101242V呵呵，最近难得见一面，\n'
		'你看上去好像很有精神啊。{wait}'
		'{page}'
		'#12101243V有没有努力工作呢？{wait}'
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
		'#12101244V#12P#0108F是、是的……{wait}'
		'{page}'
		'#12101245V#0103F……虽然我还是新人，\n'
		'肯定会有一些不足的地方……{wait}'
		'{page}'
		'#12101246V#0102F但我一定会努力加油，\n'
		'不让麦克道尔家蒙羞。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(21), Translate('老绅士'), Text(
		'#12101247V#5P#2503F哈哈……我之前就说过了，\n'
		'你不用介意家里的事。{wait}'
		'{page}'
		'#12101248V#2500F那边的几位，是你的同事们吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101249V#12P#0100F嗯，是的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101250V#0003F#12P──初次见面。{wait}'
		'{page}'
		'#12101251V#0000F我是克洛斯贝尔警察局丄特务支援课的\n'
		'罗伊德丄班宁斯。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101252V#12P#0204F我是缇欧丄普拉托。（低头行礼）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101253V#12P#0300F您好，\n'
		'我叫兰迪丄奥兰多。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(21), Translate('老绅士'), Text(
		'#12101254V#5P#2503F嗯，我的名字是\n'
		'亨利丄麦克道尔。{wait}'
		'{page}'
		'#12101255V#2500F我这个孙女\n'
		'承蒙各位照顾了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101256V#0012F#12P不，没那回事。{wait}'
		'{page}'
		'#12101257V#0000F受照顾的\n'
		'反倒是我们──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101258V#12P#0304F嗯，大小姐在写\n'
		'报告书等书面文件时\n'
		'确实帮了我们大忙。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101259V#6P#0211F我觉得兰迪前辈\n'
		'也应该帮点忙啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101260V#12P#0109F那、那个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(21), Translate('麦克道尔老人'), Text(
		'#12101261V#5P#2500F呵呵……\n'
		'工作内容充实那就再好不过了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#12101262V#2606F#5P不过，小姐……{wait}'
		'{page}'
		'#12101263V#2601F您也该不时\n'
		'回趟家比较好吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101264V#12P#0108F……很、很抱歉。{wait}'
		'{page}'
		'#12101265V#0106F因为总算能自己独立生活了，\n'
		'就不想太依赖家里……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#12101266V#2601F#5P但是──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(21), 270, 400),
	Insn('TEXT_TALK2', Char(21), Translate('麦克道尔老人'), Text(
		'#12101267V#11P#2503F没关系，阿奈斯特。{wait}'
		'{page}'
		'#12101268V#2500F这正说明了\n'
		'艾莉的决心十分坚定。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(21), Char(258), 400),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK2', Char(21), Translate('麦克道尔老人'), Text(
		'#12101269V#5P#2500F你自己所选择的道路……\n'
		'要走到自己满意为止啊。{wait}'
		'{page}'
		'#12101270V虽然不能公私不分，\n'
		'但我也会尽力提供协助的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101271V#12P#0104F……是。\n'
		'谢谢您，外公。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(21), 270, 400),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK2', Char(21), Translate('麦克道尔老人'), Text(
		'#12101272V#11P#2500F──我们走吧，\n'
		'阿奈斯特。{wait}'
		'{page}'
		'#12101273V接下来是跟工商协会的聚会吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'#12101274V#2600F#5P是的，五点开始。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
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
	Insn('0x92', Char(21), -6000, 18000, 500),
	Insn('FORK', 21, 1, [
		Insn('0x97', Char(254), (-4000, 0, -8000), 2000, 0),
	]),
	Insn('SLEEP', 150),
	Insn('0x92', Char(22), -6700, 18700, 500),
	Insn('FORK', 22, 1, [
		Insn('0x97', Char(254), (-4000, 0, -8000), 2000, 0),
	]),
	Insn('SLEEP', 4000),
	Insn('CROSSFADE', 500),
	Insn('FORK_QUIT', Char(21), 1),
	Insn('FORK_QUIT', Char(22), 1),
	Insn('CHAR_SET_POS', Char(21), (-4900, 1770, 9000), 180),
	Insn('CHAR_SET_POS', Char(22), (-4900, 1770, 10400), 180),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('FORK_QUIT', Char(258), 2),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('CHAR_ROTATE', Char(257), 180, 0),
	Insn('CHAR_ROTATE', Char(258), 180, 0),
	Insn('CHAR_ROTATE', Char(259), 180, 0),
	Insn('CHAR_ROTATE', Char(260), 180, 0),
	Insn('CAM_OFFSET', (-3000, 2000, 1800), 0),
	Insn('CAM_ROTATE', 328, 10, 0, 0),
	Insn('0x6E', 660, 0),
	Insn('CAM_DISTANCE', 13000, 0),
	Insn('FORK', 21, 1, [
		Insn('0x97', Char(254), (0, 0, -5000), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 22, 1, [
		Insn('0x97', Char(254), (0, 0, -5000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(21), 1),
	Insn('FORK_AWAIT', Char(22), 1),
	Insn('SOUND_PLAY', 462, 0, 0, 100),
	Insn('0x71', Object(4), b'\xf1\x00', 270, 0),
	Insn('0x79', b'\x04\x00'),
	Insn('FORK', 21, 1, [
		Insn('0x97', Char(254), (0, 0, -1000), 2000, 0),
	]),
	Insn('FORK', 21, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 22, 1, [
		Insn('0x97', Char(254), (0, 0, -2000), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 22, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(21), 2),
	Insn('FORK_AWAIT', Char(22), 2),
	Insn('SOUND_PLAY', 461, 0, 0, 100),
	Insn('0x71', Object(4), b'\x0f\x01', 300, 0),
	Insn('0x79', b'\x04\x00'),
	Insn('0x71', Object(4), b'<\x00', 90, 0),
	Insn('0x79', b'\x04\x00'),
	Insn('0x71', Object(4), b'y\x00', 180, 32),
	Insn('SOUND_PLAY', 470, 0, 0, 100),
	Insn('FORK_FUNC', Char(23), 3, Function((0, 47))),
	Insn('SLEEP', 300),
	Insn('SOUND_PLAY', 457, 0, 0, 100),
	Insn('SLEEP', 1700),
	Insn('FORK_QUIT', Char(23), 255),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (2500, 2000, -500), 0),
	Insn('CAM_ROTATE', 50, 13, 0, 0),
	Insn('0x6E', 720, 0),
	Insn('CAM_DISTANCE', 17500, 0),
	Insn('CHAR_SET_POS', Char(23), (-5300, 0, 1800), 100),
	Insn('0xD3', Char(23), 0, 100000, 0, 0),
	Insn('CAM_OFFSET', (12500, 2000, 6500), 5000),
	Insn('CAM_ROTATE', 36, 13, 0, 5000),
	Insn('0x9F', Insn('0', Char(23))),
	Insn('0x9F', Insn('1', (7500, 0, 3500))),
	Insn('0x9F', Insn('1', (17500, 0, 9500))),
	Insn('0x9F', Insn('1', (31500, 0, 10500))),
	Insn('0x9F', Insn('2', Char(23), 100, 100663321)),
	Insn('CHAR_FLAG1_SET', Char(23), 128),
	Insn('OBJ_FLAG_SET', Object(4), 4),
	Insn('OBJ_FLAG_UNSET', Object(4), 4096),
	Insn('CHAR_FLAG1_SET', Char(21), 128),
	Insn('CHAR_FLAG2_SET', Char(21), 32768),
	Insn('CHAR_FLAG1_SET', Char(22), 128),
	Insn('CHAR_FLAG2_SET', Char(22), 32768),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-700, 3000, 20800), 0),
	Insn('CAM_ROTATE', 45, 23, 0, 0),
	Insn('0x6E', 480, 0),
	Insn('CAM_DISTANCE', 19000, 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101275V#5P#0305F哇哦！\n'
		'好豪华的车啊。{wait}'
		'{page}'
		'#12101276V#0302F大小姐，你家\n'
		'果然很有钱吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101277V#0109F#5P那……那个。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE_STOP', Char(257)),
	Insn('SLEEP', 600),
	Insn('0x82', 200, 0, 3000, 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101278V#5P#0005F#4S啊啊啊啊！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_ROTATE', Char(259), 45, 500),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101279V#12P#0305F啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101280V#6P#0205F罗伊德前辈……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101281V#5P#0007F亨利丄麦克道尔……！{wait}'
		'{page}'
		'#12101282V那不是克洛斯贝尔市\n'
		'市长的名字吗！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101283V#12P#0301F什、什么……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101284V#6P#0201F真、真的吗……？{wait}'
		'{page}'
		'#12101285V#0205F──啊，\n'
		'确实数据库里\n'
		'好像是这么记录的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (14, 15, 250, 2)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101286V#0106F#5P呼……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(258), 135, 400),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101287V#0102F#5P──我倒是觉得，你们之前一直\n'
		'都没有察觉到这点，才比较不可思议。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 315, 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_ROTATE', Char(260), 315, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101288V#11P#0002F也、也不是……\n'
		'最开始听到艾莉的姓时\n'
		'是有些在意。{wait}'
		'{page}'
		'#12101289V不过后来发生了那么多事，\n'
		'也就逐渐淡忘了。{wait}'
		'{page}'
		'#12101290V#0006F──不过确实很丢脸啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101291V#0104F#5P呵呵，这没什么可介意的啊。{wait}'
		'{page}'
		'#12101292V不管外公是什么人，\n'
		'都跟我没关系……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101293V#11P#0005F咦……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101294V#0106F#5P……比起那些，我们还是快点\n'
		'去向伊莉雅小姐他们报告吧。{wait}'
		'{page}'
		'#12101295V#0101F虽然没面子……但也必须去把\n'
		'案子换人接手的事说清楚呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101296V#11P#0001F啊，是啊……说得也是。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101297V#12P#0305F不过，大小姐的外公\n'
		'为什么会来彩虹剧团啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101298V#0105F#5P啊，对哦……{wait}'
		'{page}'
		'#12101299V#0103F好像是因为剧团这次的新剧码，\n'
		'要配合纪念庆典进行公演……{wait}'
		'{page}'
		'#12101300V#0100F所以外公才来这里\n'
		'对相关事宜进行商议的吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('CAM_OFFSET', (-2000, 3940, 21500), 0),
	Insn('CAM_ROTATE', 45, 25, 0, 0),
	Insn('0x6E', 800, 0),
	Insn('CAM_DISTANCE', 17500, 0),
	Insn('CHAR_SET_POS', Char(0), (-2000, 1990, 21500), 0),
	Insn('CHAR_SET_POS', Char(1), (-2000, 1990, 21500), 0),
	Insn('CHAR_SET_POS', Char(2), (-2000, 1990, 21500), 0),
	Insn('CHAR_SET_POS', Char(3), (-2000, 1990, 21500), 0),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG2_UNSET', Char(11), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(13), 128),
	Insn('CHAR_FLAG2_UNSET', Char(13), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG2_UNSET', Char(12), 32768),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('0xB5', b'\x00\x06\x80\x00'),
	Insn('OBJ_FLAG_UNSET', Object(5), 4096),
	Insn('FLAG_SET', Flag(1036)),
	Insn('FORK_QUIT', Char(13), 0),
	Insn('FORK_FUNC', Char(13), 0, Function((0, 3))),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][47] = [
	Insn('FORK', 23, 1, [
		Insn('0x9B', b'\x01', Char(254), b'\x00\x00\x98:\x00\x00\x94\x11\x00\x00\x01'),
	]),
	Insn('SLEEP', 600),
	Insn('FORK', 23, 2, [
		Insn('0x9B', b'\x01', Char(254), b'\x00\x00\x98:\x00\x00|\x15\x00\x00\x01'),
	]),
	Insn('SLEEP', 600),
	Insn('FORK', 23, 1, [
		Insn('0x9B', b'\x01', Char(254), b'\x00\x00\x98:\x00\x00d\x19\x00\x00\x00'),
	]),
	Insn('RETURN'),
]

data['code'][48] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch05200', 30),
	Insn('CAM_OFFSET', (-2000, 2800, 29800), 0),
	Insn('CAM_ROTATE', 55, 21, 0, 0),
	Insn('0x6E', 480, 0),
	Insn('CAM_DISTANCE', 19000, 0),
	Insn('CHAR_SET_POS', Char(257), (-2600, 1850, 25800), 0),
	Insn('CHAR_SET_POS', Char(258), (-1400, 1850, 25800), 0),
	Insn('CHAR_SET_POS', Char(259), (-2600, 1990, 24400), 0),
	Insn('CHAR_SET_POS', Char(260), (-1400, 1990, 24400), 0),
	Insn('CHAR_SET_CHCP', Char(24), 30),
	Insn('CHAR_SET_FRAME', Char(24), 0),
	Insn('CHAR_FLAG1_UNSET', Char(24), 128),
	Insn('CHAR_FLAG2_UNSET', Char(24), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(24), 4),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('CHAR_SET_POS', Char(24), (-2000, 1760, 27800), 180),
	Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xfe\xcb\xc0', 44, 157, 0),
	Insn('OBJ_SET_FRAME', Object(255), 'sky', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'sky1', Insn('1', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'sd_mul', Insn('0', 1)),
	Insn('OBJ_FLAG_SET', Object(5), 4096),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('ITEM_REMOVE', 804, 1),
	Insn('CAM_OFFSET', (-2000, 2800, 26800), 4000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('SOUND_PLAY', 1637, 0, 255, 100),
	Insn('SLEEP', 1500),
	Insn('TEXT_TALK', Char(24), Text(
		'#12101379V#1806F#5P那个……感觉总是在\n'
		'给各位添麻烦啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101380V#12P#0012F没事，别介意哦。{wait}'
		'{page}'
		'#12101381V#0000F警察的工作本来就是要\n'
		'脚踏实地地反复做一些无用功啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101382V#12P#0202F这就是所谓的预防犯罪了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101383V#0302F#12P对对，小莉夏。{wait}'
		'{page}'
		'#12101384V#0309F你别担心我们，\n'
		'预演要加油啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(24), Text(
		'#12101385V#1802F#5P好的，谢谢各位。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('CHAR_WATCH', Char(257), Char(260), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101386V#6P#0005F预演？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(260), Char(257), 500),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101387V#0305F#11P怎么，你不知道啊？{wait}'
		'{page}'
		'#12101388V#0300F彩虹剧团每次在\n'
		'新剧码的正式公演之前，都会\n'
		'举行一次预演，是吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(24), Text(
		'#12101389V#1804F#5P是、是的。\n'
		'我这次是第一次参加……{wait}'
		'{page}'
		'#12101390V#1802F预演时似乎会邀请国内外的\n'
		'相关人员和各家媒体前来观看。{wait}'
		'{page}'
		'#12101391V赞助公演的那些\n'
		'大人物好像也会来……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_ROTATE', Char(260), 0, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101392V#12P#0000F这样啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101393V#0105F#12P难道……\n'
		'也邀请麦克道尔市长了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(24), Text(
		'#12101394V#1805F#5P啊，对啊，\n'
		'市长是主要嘉宾。{wait}'
		'{page}'
		'#12101395V#1804F好像是因为公演配合了纪念庆典，\n'
		'所以市长也给予了大力支持呢。{wait}'
		'{page}'
		'#12101396V#1802F今天市长也在百忙之中\n'
		'抽空来这里慰问我们了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101397V#0100F#12P这样啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(258)),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101398V#0104F#12P──莉夏。\n'
		'预演，请加油哦。{wait}'
		'{page}'
		'#12101399V#0102F莉夏的话，就算是第一次，\n'
		'也绝对没有问题的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(24), Text(
		'#12101400V#1805F#5P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101401V#12P#0002F对啊，看你练习的情况，\n'
		'就完全不需要担心了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101402V#0309F#12P哦哦，你一定会表演得很精彩！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101403V#12P#0204F……我也很期待。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(24), Text(
		'#12101404V#1809F#5P谢、谢谢各位。\n'
		'那个……我现在很有信心了。{wait}'
		'{page}'
		'#12101405V#1802F那么，我回去排练了。{wait}'
		'{page}'
		'#12101406V各位，谢谢你们。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 1638, 0, 255, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(24), 0, 500),
	Insn('CAM_OFFSET', (-2000, 3800, 31800), 3500),
	Insn('FORK', 24, 1, [
		Insn('0x95', Char(254), (-2000, 2660, 34200), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('OBJ_FLAG_UNSET', Object(3), 16),
	Insn('0x71', Object(3), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x03\x00'),
	Insn('0x6F', b'y'),
	Insn('FORK', 24, 1, [
		Insn('0x95', Char(254), (-2000, 2660, 36000), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 24, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(24), 2),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('0x71', Object(3), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x03\x00'),
	Insn('OBJ_FLAG_SET', Object(3), 16),
	Insn('CHAR_FLAG1_SET', Char(24), 128),
	Insn('CHAR_FLAG2_SET', Char(24), 32768),
	Insn('SLEEP', 500),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-2000, 3000, 25100), 0),
	Insn('CAM_ROTATE', 40, 27, 0, 0),
	Insn('0x6E', 480, 0),
	Insn('CAM_DISTANCE', 20000, 0),
	Insn('0x0D'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(260), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 2),
	Insn('FORK_AWAIT', Char(259), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101407V#0006F#5P……呼……{wait}'
		'{page}'
		'#12101408V#0000F我们也回去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101409V#0306F#11P好……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101410V#6P#0206F……总觉得\n'
		'松了一口气。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101411V#0103F#5P……是啊…………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 20500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('0xD5', 30),
	Insn('CAM_OFFSET', (-2000, 3710, 26800), 0),
	Insn('CAM_ROTATE', 45, 25, 0, 0),
	Insn('0x6E', 800, 0),
	Insn('CAM_DISTANCE', 17500, 0),
	Insn('CHAR_SET_POS', Char(257), (-2000, 1760, 26800), 180),
	Insn('CHAR_SET_POS', Char(258), (-2000, 1760, 26800), 180),
	Insn('CHAR_SET_POS', Char(259), (-2000, 1760, 26800), 180),
	Insn('CHAR_SET_POS', Char(260), (-2000, 1760, 26800), 180),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG2_UNSET', Char(11), 32768),
	Insn('OBJ_FLAG_UNSET', Object(5), 4096),
	Insn('FLAG_SET', Flag(1037)),
	Insn('0xC7', b'\x00\x00\x10\x00\x00'),
	Insn('QUEST', 66, Insn('TASK_SET', 9)),
	Insn('0x1B', 1, Function((0, 62)), 0),
	Insn('0x1B', 2, Function((0, 63)), 0),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('0xB8', 100, 0),
	Insn('0xB8', 101, 0),
	Insn('0xB8', 100, 102),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][49] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00500', 30),
	Insn('LOAD_CHCP', 'chr/ch05200', 31),
	Insn('LOAD_CHCP', 'chr/ch05100', 32),
	Insn('LOAD_CHCP', 'apl/ch50219', 33),
	Insn('LOAD_CHCP', 'apl/ch50220', 34),
	Insn('LOAD_CHCP', 'apl/ch50238', 35),
	Insn('LOAD_CHCP', 'apl/ch50239', 36),
	Insn('CAM_OFFSET', (15000, 14100, 24500), 0),
	Insn('CAM_ROTATE', 320, 25, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 17500, 0),
	Insn('CHAR_SET_POS', Char(0), (15000, 0, 15000), 0),
	Insn('CHAR_SET_POS', Char(1), (15000, 0, 15000), 0),
	Insn('CHAR_SET_POS', Char(2), (15000, 0, 15000), 0),
	Insn('CHAR_SET_POS', Char(3), (15000, 0, 15000), 0),
	Insn('CHAR_SET_CHCP', Char(26), 30),
	Insn('CHAR_SET_FRAME', Char(26), 0),
	Insn('CHAR_FLAG1_UNSET', Char(26), 128),
	Insn('CHAR_FLAG2_UNSET', Char(26), 32768),
	Insn('CHAR_FLAG1_SET', Char(26), 32768),
	Insn('CHAR_SET_POS', Char(26), (26300, 14100, 24500), 270),
	Insn('CHAR_SET_CHCP', Char(24), 31),
	Insn('CHAR_SET_FRAME', Char(24), 0),
	Insn('CHAR_FLAG1_UNSET', Char(24), 128),
	Insn('CHAR_FLAG2_UNSET', Char(24), 32768),
	Insn('CHAR_FLAG1_SET', Char(24), 32768),
	Insn('CHAR_SET_COLOR', Char(24), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(24), (19300, 13100, 24500), 270),
	Insn('CHAR_SET_CHCP', Char(25), 32),
	Insn('CHAR_SET_FRAME', Char(25), 0),
	Insn('CHAR_FLAG1_SET', Char(25), 32768),
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
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu01801.itp'),
	Insn('IMG_LOAD', ResId(1), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu01700.itp'),
	Insn('IMG_LOAD', ResId(2), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis155.itp'),
	Insn('EFF_LOAD', ResId(0), 'event\\eva04_00.eff'),
	Insn('CAM_OFFSET', (17000, 14100, 24500), 3000),
	Insn('CAM_DISTANCE', 15500, 3000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('SLEEP', 1000),
	Insn('EXPR_CHAR_ATTR', Char(26), 40, Expr([Insn('CONST', 13), Insn('SET'), Insn('END')])),
	Insn('CHAR_SET_CHCP', Char(26), 34),
	Insn('CHAR_SET_FRAME', Char(26), 0),
	Insn('0x83', b'\x00\x1a\x00\x1e\x00,\x01'),
	Insn('FORK', 26, 1, [
		Insn('0x9D', Char(254), 19300, 13100, 24500, 900, 2500),
	]),
	Insn('SOUND_PLAY', 814, 0, 0, 100),
	Insn('FORK_AWAIT', Char(26), 1),
	Insn('EFF_PLAY', (ResId(0), -1), Char(26), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('CHAR_SET_FRAME', Char(26), 1),
	Insn('SOUND_PLAY', 42, 0, 0, 100),
	Insn('SLEEP', 10),
	Insn('SOUND_PLAY', 31, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('0x83', b'\x01\x1a\x00\x00\x00\x00\x00'),
	Insn('EXPR_CHAR_ATTR', Char(26), 40, Expr([Insn('CONST', 9), Insn('SET'), Insn('END')])),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(26), 33),
	Insn('CHAR_SET_FRAME', Char(26), 0),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(26), Text(
		'{color 3}#12201825V#0700F#11P#40W…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (19300, 13900, 24500), 0),
	Insn('CAM_ROTATE', 50, 31, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 21500, 0),
	Insn('CHAR_FLAG1_SET', Char(26), 32),
	Insn('CHAR_FLAG1_SET', Char(26), 2),
	Insn('CHAR_SET_CHCP', Char(26), 35),
	Insn('CHAR_SET_FRAME', Char(26), 7),
	Insn('CHAR_FLAG1_SET', Char(24), 32),
	Insn('CHAR_FLAG1_SET', Char(24), 2),
	Insn('CHAR_SET_CHCP', Char(24), 36),
	Insn('CHAR_SET_FRAME', Char(24), 0),
	Insn('SLEEP', 1000),
	Insn('SOUND_PLAY', 534, 0, 0, 90),
	Insn('BGM_STOP', 5000),
	Insn('CAM_ROTATE', 40, 31, 0, 2000),
	Insn('CAM_DISTANCE', 20500, 2000),
	Insn('FORK_FUNC', Char(26), 3, Function((0, 53))),
	Insn('FORK', 26, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 1000),
	]),
	Insn('FORK', 24, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 1000),
	]),
	Insn('SLEEP', 600),
	Insn('CHAR_SET_FRAME', Char(24), 1),
	Insn('SLEEP', 130),
	Insn('CHAR_SET_FRAME', Char(24), 2),
	Insn('SLEEP', 130),
	Insn('CHAR_SET_FRAME', Char(24), 3),
	Insn('SLEEP', 400),
	Insn('FORK_AWAIT', Char(26), 2),
	Insn('CHAR_FLAG1_SET', Char(26), 128),
	Insn('CHAR_FLAG2_SET', Char(26), 32768),
	Insn('SOUND_PLAY', 12130, 186, 255, 100),
	Insn('TEXT_MESSAGE', Char(24), Text(
		'{color 0}太好了，赶上了………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 300),
	Insn('TEXT_MESSAGE', Char(24), Text(
		'{color 0}#12201827V#40W……………………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('CHAR_FLAG1_UNSET', Char(24), 32),
	Insn('CHAR_FLAG1_UNSET', Char(24), 2),
	Insn('CHAR_SET_CHCP', Char(24), 31),
	Insn('CHAR_SET_FRAME', Char(24), 0),
	Insn('CHAR_ROTATE', Char(24), 0, 400),
	Insn('SLEEP', 300),
	Insn('CAM_DISTANCE', 21500, 3000),
	Insn('FORK', 24, 1, [
		Insn('0x96', Char(254), (19300, 13100, 30600), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('EFF_PLAY', (ResId(0), -1), Char(24), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('CHAR_FLAG1_SET', Char(24), 32),
	Insn('CHAR_FLAG1_SET', Char(24), 2),
	Insn('CHAR_SET_CHCP', Char(24), 36),
	Insn('CHAR_SET_FRAME', Char(24), 4),
	Insn('EXPR_CHAR_ATTR', Char(24), 40, Expr([Insn('CONST', 13), Insn('SET'), Insn('END')])),
	Insn('FORK', 24, 1, [
		Insn('0x9D', Char(254), 19300, 5100, 35600, 1300, 2000),
	]),
	Insn('SOUND_PLAY', 814, 0, 0, 100),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('0x6F', b'\x10'),
	Insn('CHAR_FLAG1_UNSET', Char(24), 32),
	Insn('CHAR_FLAG1_UNSET', Char(24), 2),
	Insn('CHAR_SET_CHCP', Char(24), 31),
	Insn('CHAR_SET_FRAME', Char(24), 0),
	Insn('EXPR_CHAR_ATTR', Char(24), 40, Expr([Insn('CONST', 9), Insn('SET'), Insn('END')])),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'q\x00\x00'),
	Insn('CAM_OFFSET', (-2000, 2700, 28500), 0),
	Insn('CAM_ROTATE', 320, 23, 0, 0),
	Insn('0x6E', 550, 0),
	Insn('CAM_DISTANCE', 19000, 0),
	Insn('CHAR_FLAG1_UNSET', Char(24), 4),
	Insn('CHAR_SET_POS', Char(24), (6000, 1760, 26000), 270),
	Insn('CHAR_FLAG1_UNSET', Char(25), 4),
	Insn('CHAR_SET_POS', Char(25), (-2000, 1990, 18600), 0),
	Insn('CAM_ROTATE', 330, 17, 0, 3500),
	Insn('CAM_DISTANCE', 17000, 3500),
	Insn('FORK', 24, 1, [
		Insn('0x96', Char(254), (-2000, 1760, 28500), 2500, 0),
	]),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('CHAR_ROTATE', Char(24), 0, 500),
	Insn('0x6F', b'P'),
	Insn('CHAR_FLAG1_UNSET', Char(25), 128),
	Insn('CHAR_FLAG2_UNSET', Char(25), 32768),
	Insn('TEXT_TALK2', Char(25), Translate('女性的声音'), Text(
		'#12201828V你来得很早啊，莉夏。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(24), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('SOUND_PLAY', 1635, 0, 255, 100),
	Insn('CAM_OFFSET', (-2000, 2700, 27600), 3000),
	Insn('FORK', 25, 1, [
		Insn('0x96', Char(254), (-2000, 1760, 26600), 2500, 0),
	]),
	Insn('FORK', 24, 2, [
		Insn('CHAR_WATCH', Char(254), Char(25), 500),
	]),
	Insn('FORK_AWAIT', Char(25), 1),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(24), Text(
		'#12201830V#1805F#11P伊莉雅小姐……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(1), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('TEXT_MESSAGE', Char(25), Text(
		'#12201831V怎么，是因为太期待\n'
		'下午的排练吗？{wait}'
		'{page}'
		'#12201832V我已经是个\n'
		'十足的舞痴了……{wait}'
		'{page}'
		'#12201833V没想到你也\n'
		'很有这个潜质啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(1), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 0))),
	Insn('TEXT_TALK', Char(24), Text(
		'#12201834V#1809F#11P啊哈哈，没有啦……{wait}'
		'{page}'
		'#12201835V我还没有自信能达到伊莉雅小姐\n'
		'那种痴迷的程度……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(25), Text(
		'#12201836V#6P#1704F呵呵，嘴上这么说，\n'
		'预演排练时却很拼命啊。{wait}'
		'{page}'
		'#12201837V#1702F你的演技很不错哦。{wait}'
		'{page}'
		'#12201838V也终于足够\n'
		'当我的小对手了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(24), Text(
		'#12201839V#1802F#11P伊莉雅小姐……{wait}'
		'{page}'
		'#12201840V#1804F……如果真的是那样，\n'
		'也全都是托了伊莉雅小姐的福。{wait}'
		'{page}'
		'#12201841V从前，我只知道那条生来便已被决定好的道路，\n'
		'是你给我带来了崭新的光芒……{wait}'
		'{page}'
		'#12201842V#1802F……呵呵，还有，这次也必须\n'
		'谢谢他们呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(25), Text(
		'#12201843V#6P#1705F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(24), Text(
		'#12201844V#1804F#11P呵呵，没什么。{wait}'
		'{page}'
		'#12201845V#1800F今天的练习，是再\n'
		'完善第三幕的表演吧？{wait}'
		'{page}'
		'#12201846V我会加油的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(25), Text(
		'#12201847V#6P#1702F哦，很有干劲嘛。{wait}'
		'{page}'
		'#12201848V#1700F嗯，我也\n'
		'绝对不会输的哦～{wait}'
		'{page}'
		'#12201849V#1709F好，到下个月的正式公演之前，\n'
		'要练习得比现在好百倍～！{wait}'
		'{page}'
		'#12201850V跟我来，莉夏！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(24), Text(
		'#12201851V#1809F#11P是，伊莉雅小姐……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 22000, 6000),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 50))),
	Insn('SLEEP', 2000),
	Insn('FADE_ON', 3000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(257), 3),
	Insn('BGM_STOP', 5000),
	Insn('BGM_WAIT'),
	Insn('EXPR_VAR', 3, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 14, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('EXPR_VAR', 3, Expr([Insn('VAR', 3), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 15, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('EXPR_VAR', 3, Expr([Insn('VAR', 3), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 16, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('EXPR_VAR', 3, Expr([Insn('VAR', 3), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 17, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('EXPR_VAR', 3, Expr([Insn('VAR', 3), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('EXPR_VAR', 3, Expr([Insn('VAR', 3), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('EXPR_VAR', 3, Expr([Insn('VAR', 3), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 20, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('EXPR_VAR', 3, Expr([Insn('VAR', 3), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('EXPR_VAR', 3, Expr([Insn('VAR', 3), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('EXPR_VAR', 3, Expr([Insn('VAR', 3), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('EXPR_VAR', 3, Expr([Insn('VAR', 3), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
			Insn('QUEST', 58, Insn('TASK_SET', 8)),
			Insn('FLAG_UNSET', Flag(1107)),
			Insn('FLAG_UNSET', Flag(1106)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('VAR', 3), Insn('CONST', 7), Insn('GE'), Insn('END')]), [
			Insn('EXPR_ATTR', 101, Expr([Insn('ATTR', 101), Insn('CONST', 15), Insn('ADD'), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('VAR', 3), Insn('CONST', 5), Insn('GE'), Insn('END')]), [
			Insn('EXPR_ATTR', 101, Expr([Insn('ATTR', 101), Insn('CONST', 10), Insn('ADD'), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('VAR', 3), Insn('CONST', 2), Insn('GE'), Insn('END')]), [
			Insn('EXPR_ATTR', 101, Expr([Insn('ATTR', 101), Insn('CONST', 5), Insn('ADD'), Insn('SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('QUEST', 65, Insn('FLAG_UNSET', 16)),
	Insn('QUEST', 66, Insn('FLAG_UNSET', 16)),
	Insn('QUEST', 67, Insn('FLAG_UNSET', 16)),
	Insn('QUEST', 65, Insn('FLAG_UNSET', 32)),
	Insn('QUEST', 67, Insn('FLAG_UNSET', 32)),
	Insn('ITEM_REMOVE', 805, 1),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 14, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 14, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 14, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 14, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 14, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 16, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 16, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 17, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 17, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 17, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 17, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 17, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 18, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 18, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 18, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 19, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 19, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 19, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 20, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 20, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 20, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 20, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 20, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 21, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 21, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 56, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 56, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 58, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 58, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('ITEM_REMOVE', 833, 1),
	Insn('ITEM_REMOVE', 829, 1),
	Insn('0xE3', 10),
	Insn('SLEEP', 1000),
	Insn('IMG_0xC9', (ResId(2), 3), Color(0xFFFFFFFF), 800, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
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
	Insn('0xDE', b'&\x00'),
	Insn('0xDE', b'\x1e\x00'),
	Insn('0xDE', b'\x1f\x00'),
	Insn('SLEEP', 100),
	Insn('CAM_OFFSET', (-1000000, 0, 0), 0),
	Insn('0xC7', b'\x00\x10\x00\x00\x00'),
	Insn('EXPR_ATTR', 80, Expr([Insn('CONST', 3), Insn('SET'), Insn('END')])),
	Insn('FLAG_SET', Flag(760)),
	Insn('EXPR_ATTR', 49, Expr([Insn('CONST', 152), Insn('SET'), Insn('END')])),
	Insn('SAVE'),
	Insn('FLAG_UNSET', Flag(760)),
	Insn('MINIGAME', 43, 1, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
	Insn('IMG_0xC9', (ResId(2), 3), Color(0x00FFFFFF), 800, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(2), 3))),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xC7', b'\x01\x10\x00\x00\x00'),
	Insn('0xE3', 11),
	Insn('EXPR_ATTR', 4, Expr([Insn('CONST', 3), Insn('SET'), Insn('END')])),
	Insn('FLAG_SET', Flag(737)),
	Insn('NEW_SCENE', 'c1120', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][50] = [
	Insn('FORK_FUNC', Char(25), 3, Function((0, 51))),
	Insn('SLEEP', 100),
	Insn('FORK_FUNC', Char(24), 3, Function((0, 52))),
	Insn('FORK_AWAIT', Char(25), 3),
	Insn('OBJ_FLAG_UNSET', Object(3), 16),
	Insn('0x71', Object(3), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x03\x00'),
	Insn('FORK_AWAIT', Char(24), 3),
	Insn('FORK', 25, 1, [
		Insn('0x98', Char(254), (0, 0, 5000), 2500, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 24, 1, [
		Insn('0x98', Char(254), (0, 0, 5000), 2500, 0),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 25, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 24, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('RETURN'),
]

data['code'][51] = [
	Insn('FORK', 25, 1, [
		Insn('0x96', Char(254), (-2500, 1760, 29600), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(25), 1),
	Insn('FORK', 25, 1, [
		Insn('0x96', Char(254), (-2500, 2660, 33600), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(25), 1),
	Insn('RETURN'),
]

data['code'][52] = [
	Insn('FORK_LOOP', 24, 2, [
		Insn('CHAR_WATCH', Char(254), Char(25), 500),
	]),
	Insn('FORK', 24, 1, [
		Insn('0x96', Char(254), (-1400, 1760, 28800), 1000, 0),
	]),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('SLEEP', 600),
	Insn('FORK_QUIT', Char(24), 2),
	Insn('CHAR_ROTATE', Char(24), 0, 500),
	Insn('FORK', 24, 1, [
		Insn('0x95', Char(254), (-1400, 2660, 32800), 2500, 0),
	]),
	Insn('FORK_AWAIT', Char(24), 1),
	Insn('RETURN'),
]

data['code'][53] = [
	Insn('CHAR_ANIMATION', Char(254), 2000, [
		7,
		6,
		5,
		4,
		3,
		2,
		1,
		0,
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(254), 1),
	Insn('RETURN'),
]

data['code'][54] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (-23500, 1000, 10000), 0),
	Insn('CAM_ROTATE', 75, 27, 0, 0),
	Insn('0x6E', 760, 0),
	Insn('CAM_DISTANCE', 11000, 0),
	Insn('CHAR_SET_POS', Char(257), (-16000, 0, 5500), 300),
	Insn('CHAR_SET_POS', Char(258), (-16000, 0, 4300), 300),
	Insn('CHAR_SET_POS', Char(260), (-14600, 0, 4500), 300),
	Insn('CHAR_SET_POS', Char(259), (-14600, 0, 3300), 300),
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
	Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xfe\xcb\xc0', 44, 157, 0),
	Insn('OBJ_SET_FRAME', Object(255), 'sky', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'sky1', Insn('1', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'sd_mul', Insn('0', 1)),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 57))),
	Insn('SLEEP', 50),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 55))),
	Insn('SLEEP', 100),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 58))),
	Insn('SLEEP', 50),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 56))),
	Insn('CAM_OFFSET', (-26500, 2500, 16000), 10000),
	Insn('CAM_ROTATE', 30, 11, 0, 10000),
	Insn('CAM_DISTANCE', 19000, 10000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('OBJ_FLAG_UNSET', Object(1), 16),
	Insn('0x71', Object(1), b'\x00\x00', 5, 0),
	Insn('0x79', b'\x01\x00'),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK', 257, 1, [
		Insn('0x98', Char(254), (0, 0, 2000), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x98', Char(254), (0, 0, 2000), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('0x98', Char(254), (0, 0, 3000), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x98', Char(254), (0, 0, 3000), 2000, 0),
	]),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('FORK_QUIT', Char(257), 255),
	Insn('FORK_QUIT', Char(258), 255),
	Insn('FORK_QUIT', Char(259), 255),
	Insn('FORK_QUIT', Char(260), 255),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('0xB8', 0, 0),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'c0470', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][55] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-26000, 0, 12500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-26000, 300, 16500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][56] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-26000, 0, 12500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-26000, 300, 15000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][57] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-27200, 0, 12500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-27200, 300, 16100), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][58] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-27200, 0, 12500), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-27200, 300, 14600), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][59] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50011', 30),
	Insn('SOUND_LOAD', 806),
	Insn('CAM_OFFSET', (-2000, 2760, 27500), 0),
	Insn('CAM_ROTATE', 55, 32, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 23000, 0),
	Insn('CHAR_SET_POS', Char(257), (-2700, 1760, 26800), 45),
	Insn('CHAR_SET_POS', Char(258), (-1300, 1760, 26800), 315),
	Insn('CHAR_SET_POS', Char(259), (-2700, 1760, 28200), 135),
	Insn('CHAR_SET_POS', Char(260), (-1300, 1760, 28200), 225),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('IMG_LOAD', ResId(0), 180, 0, b'\xb4\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis007.itp'),
	Insn('CAM_ROTATE', 45, 27, 0, 3000),
	Insn('CAM_DISTANCE', 20000, 3000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14300073V#0106F……没想到所有的人\n'
		'都失踪了啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14300074V#5P#0303F不祥的预感应验了呢…… {wait}'
		'{page}'
		'#14300075V#0301F是自发性的离开，\n'
		'还是被人绑架了呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14300076V#0206F现阶段的情报实在太少了，\n'
		'两种可能性都要考虑到。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1603)), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#14300077V#6P#0003F……这五名失踪人员\n'
				'说不定只是冰山一角。{wait}'
				'{page}'
				'#14300079V#0001F在克洛斯贝尔全市，\n'
				'很可能已经有相当多的人\n'
				'失踪了呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#14300078V#6P#0003F……这四名失踪人员\n'
				'说不定只是冰山一角。{wait}'
				'{page}'
				'#14300079V#0001F在克洛斯贝尔全市，\n'
				'很可能已经有相当多的人\n'
				'失踪了呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(258), Text(
		'#14300080V#0108F嗯……\n'
		'到底有多少人\n'
		'下落不明了呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14300081V#5P#0301F怎么办，罗伊德？{wait}'
		'{page}'
		'#14300082V要一个一个找的话，\n'
		'实在是太勉强了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14300083V#6P#0006F嗯……凭我们的人手，\n'
		'确实是严重不足。{wait}'
		'{page}'
		'#14300084V#0008F在这种时候，一课却迫于上层的压力\n'
		'而无法行动，真是让人头痛啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14300085V#0202F不然去找二课的多诺邦警部，\n'
		'问问他能不能帮忙吧？{wait}'
		'{page}'
		'#14300086V毕竟我们以前也帮过他的忙。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14300087V#6P#0003F不行……这应该也很难。{wait}'
		'{page}'
		'#14300088V#0001F既然连达德利搜查官都无计可施，\n'
		'只能前来请求支援课帮忙，\n'
		'二课想必也承受着相当的压力。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14300089V#0206F原来如此……的确呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14300090V#0108F如此说来，公共安全课\n'
		'的情况应该也是一样吧……{wait}'
		'{page}'
		'#14300091V#0106F如果能借助警队的人力，\n'
		'情况就会大有改善了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 806, 0, 2, 100),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
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
		'{color 0}#14300092V#0001F您好，我是特务支援课的\n'
		'罗伊德丄班宁斯。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('男子的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14300093V喂，新人们……！{wait}'
		'{page}'
		'#14300094V你们没干什么\n'
		'多余的事吧……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14300095V#0011F哎……{wait}'
		'{page}'
		'#14300096V#0001F这声音……莫非是\n'
		'达德利搜查官吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('达德利的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14300097V什么莫非不莫非的！{wait}'
		'{page}'
		'#14300098V你们几个难道又擅自行动，\n'
		'到鲁巴彻那边捣乱了吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14300099V#0005F没、没有……{wait}'
		'{page}'
		'#14300100V#0003F我们现在正在专心\n'
		'调查药物方面的事情呢。{wait}'
		'{page}'
		'#14300101V#0001F……请问发生什么事了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('达德利的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#14300102V那还用问吗！\n'
		'他们的事务所……{wait}'
		'{page}'
		'#14300103V……咳咳，没什么。{wait}'
		'{page}'
		'#14300104V既然不是你们干的，那就没事了。\n'
		'继续调查你们的吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('SOUND_PLAY', 825, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#14300105V#0005F啊……{wait}'
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
	Insn('TEXT_TALK', Char(257), Text(
		'#14300106V#6P#0013F………………………………{wait}'
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
	Insn('TEXT_TALK', Char(258), Text(
		'#14300107V#0101F是达德利搜查官吗？\n'
		'发生什么事了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14300108V#6P#0006F这个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}罗伊德将与达德利的谈话内容\n'
		'转告给了艾莉等人。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_TALK', Char(260), Text(
		'#14300109V#5P#0301F那是什么意思啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14300110V#0206F……明显有蹊跷呢。{wait}'
		'{page}'
		'#14300111V#0201F难道鲁巴彻商会那里\n'
		'发生了什么情况吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14300112V#6P#0003F很有可能……{wait}'
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
	Insn('TEXT_TALK', Char(260), Text(
		'#14300113V#5P#0300F既然如此，我们也只能\n'
		'过去看看情况了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14300114V#0103F是啊……虽然已经被警告过，\n'
		'让我们别再去管黑手党内斗的事情了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14300115V#0202F不过，如果失踪人员与黑手党有关，\n'
		'我们应该就可以名正言顺地展开调查了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14300116V#6P#0001F嗯……\n'
		'赶快前往鲁巴彻商会吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0x4C', Char(10), -1),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('0x4C', Char(11), -1),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG2_UNSET', Char(11), 32768),
	Insn('CHAR_SET_POS', Char(0), (-2000, 1760, 26500), 180),
	Insn('FLAG_SET', Flag(1567)),
	Insn('QUEST', 76, Insn('TASK_SET', 12)),
	Insn('SOUND_STOP', 806),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][60] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(768)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(564)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这里好像禁止\n'
				'无关人员入内……\n'
				'还是别进去了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-2040, 2660, 31410), 180),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(768)), Insn('FLAG', Flag(1026)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(831)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这里好像禁止\n'
				'无关人员入内……\n'
				'还是别进去了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-2040, 2660, 31410), 180),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1536)), Insn('FLAG', Flag(1550)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1605)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}彩虹剧团好像正在公演。\n'
				'还是别进去了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-2040, 2660, 31410), 180),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1558)), Insn('FLAG', Flag(1559)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(317), Text(
						'#2105F咦，要进\n'
						'彩虹剧团吗？{wait}'
						'{page}'
						'#2109F……太好了！！\n'
						'你们认识伊莉雅丄普拉提耶，\n'
						'所以一定可以进去！{wait}'
						'{page}'
						'来，冲吧～！！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F您在起什么哄啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0101F我很在意镇长的话，\n'
						'我们赶紧去赌场吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(9)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(257), Text(
						'#0001F比克森镇长的话很令人在意……\n'
						'我们快点去赌场吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-2040, 2660, 31410), 180),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1560)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1606)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}彩虹剧团好像正在公演。\n'
				'还是别进去了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-2040, 2660, 31410), 180),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('FLAG', Flag(1848)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F啊……彩虹剧团现在\n'
						'正在公演。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0304F舞台那边交给\n'
						'专业人员就行了。{wait}'
						'{page}'
						'#0300F我们去做\n'
						'我们该做的事吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F也对，现在快点去\n'
						'乌尔斯拉医院吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(9)),
				]),
				(None, [
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'{color 5}彩虹剧团好像正在公演。\n'
						'现在快点去乌尔斯拉医院吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('0x5A'),
				]),
			]),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-2040, 2660, 31410), 180),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][61] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(768)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT_BEGIN', 1),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(565)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F这里……好像就是赌场啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0300F赌场《巴鲁卡》──\n'
						'是我常去的店哦。{wait}'
						'{page}'
						'#0309F好！为庆祝上任，\n'
						'大家来决一胜负吧！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0111F那可不行吧，\n'
						'你有没有常识啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0306F喂喂，怎么这么说啊！？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F……我说，今天\n'
						'也算是在职学习，\n'
						'你就先忍耐一下吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(565)),
				]),
				(Expr([Insn('ATTR', 10), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#0300F……今天要坐在……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F兰迪，那可不行哦？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0301F啧，真是一群死板的家伙啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'{color 5}这是赌场。\n'
						'……今天就不进去了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('0x5A'),
				]),
			]),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-26500, 300, 15360), 175),
			Insn('EVENT_END', 4),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][62] = [
	Insn('EVENT_BEGIN', 1),
	Insn('CALL', Function((0, 64))),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (20770, 0, 12930), 270),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][63] = [
	Insn('EVENT_BEGIN', 1),
	Insn('SLEEP', 50),
	Insn('CALL', Function((0, 64))),
	Insn('CHAR_SET_POS', Char(0), (-39280, 0, 12420), 90),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][64] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1037)), Insn('FLAG', Flag(1040)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0006F今天太累了……直接回\n'
				'支援课去吧，还是不要绕路了。{wait}'
				'{page}'
				'#0000F从这里回去的话，走小巷\n'
				'是最快的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1558)), Insn('FLAG', Flag(1559)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F比克森镇长的话很令人在意……\n'
				'我们快点去赌场吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]
