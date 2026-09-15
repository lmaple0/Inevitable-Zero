# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'c1200',
	'name2': 'c1200',
	'location': 26,
	'bgm': 100,
	'flags': 8192,
	'includes': [
		'c1200',
		None,
		't1500_1',
		None,
		None,
		None,
	],
	'name3': 'c1200',
	'labels': [
		{
			'pos': (-123.13999938964844, 0.0, -85.1500015258789),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('中央广场'),
		},
		{
			'pos': (-209.27000427246094, 0.0, -79.26000213623047),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('西侧大道'),
		},
		{
			'pos': (-87.7699966430664, 0.0, 31.440000534057617),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('行政区'),
		},
		{
			'pos': (-289.17999267578125, 0.0, 18.34000015258789),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('住宅区'),
		},
		{
			'pos': (-193.5500030517578, 0.0, 7.860000133514404),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('欢乐街'),
		},
		{
			'pos': (-16.700000762939453, 0.0, -115.27999877929688),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('东侧大道'),
		},
		{
			'pos': (29.799999237060547, 0.0, -187.3300018310547),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('旧市街'),
		},
		{
			'pos': (19.979999542236328, 0.0, -28.81999969482422),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('港湾区'),
		},
		{
			'pos': (-14.079999923706055, 0.0, 94.31999969482422),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('ＩＢＣ'),
		},
		{
			'pos': (-108.4000015258789, 0.0, -175.5399932861328),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('站前大道'),
		},
		{
			'pos': (-169.97000122070312, 0.0, -39.29999923706055),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('小巷'),
		},
		{
			'pos': (-112.33000183105469, 0.0, -216.14999389648438),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('乌尔斯拉小径'),
		},
		{
			'pos': (54.040000915527344, 0.0, -96.94000244140625),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('东克洛斯贝尔街道'),
		},
		{
			'pos': (-276.0799865722656, 0.0, -81.22000122070312),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('西克洛斯贝尔街道'),
		},
		{
			'pos': (-268.2200012207031, 0.0, 49.779998779296875),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('玛因兹山道'),
		},
		{
			'pos': (-151.9600067138672, 0.0, -103.48999786376953),
			'unk': b'\x00\x00Q\x00',
			'name': Translate(''),
		},
		{
			'pos': (-81.55000305175781, 0.0, -69.43000030517578),
			'unk': b'\x00\x00T\x00',
			'name': Translate(''),
		},
		{
			'pos': (-119.87000274658203, 0.0, -113.97000122070312),
			'unk': b'\x00\x00W\x00',
			'name': Translate(''),
		},
		{
			'pos': (-152.94000244140625, 0.0, -65.5),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-126.08999633789062, 0.0, -34.060001373291016),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-192.57000732421875, 0.0, -72.05000305175781),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-205.33999633789062, 0.0, -44.540000915527344),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-173.89999389648438, 0.0, -2.619999885559082),
			'unk': b'\x00\x00R\x00',
			'name': Translate(''),
		},
		{
			'pos': (-167.67999267578125, 0.0, -19.649999618530273),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-156.22000122070312, 0.0, -30.790000915527344),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-118.87999725341797, 0.0, 62.22999954223633),
			'unk': b'\x00\x00Q\x00',
			'name': Translate(''),
		},
		{
			'pos': (27.84000015258789, 0.0, -115.27999877929688),
			'unk': b'\x00\x00R\x00',
			'name': Translate(''),
		},
		{
			'pos': (5.570000171661377, 0.0, -233.83999633789062),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-11.460000038146973, 0.0, -209.60000610351562),
			'unk': b'\x00\x00S\x00',
			'name': Translate(''),
		},
		{
			'pos': (-108.4000015258789, 0.0, -100.87000274658203),
			'unk': b'\x00\x00V\x00',
			'name': Translate(''),
		},
	],
	'chcp': [
		'chr/ch22100',
		'chr/ch25200',
		'chr/ch26000',
		'apl/ch50168',
		'chr/ch21500',
		'chr/ch29300',
		'chr/ch31500',
		'chr/ch28100',
		'chr/ch06000',
		'chr/ch30000',
		'chr/ch21102',
		'chr/ch20600',
		'chr/ch20400',
		'chr/ch21900',
		'chr/ch20700',
		'chr/ch20800',
		'chr/ch26600',
		'chr/ch27200',
		'chr/ch26600',
		'chr/ch28900',
		'chr/ch29100',
		'chr/ch31400',
		'chr/ch24000',
		'chr/ch21300',
		'chr/ch24400',
		'chr/ch34200',
		'chr/ch21100',
	],
	'npcs': [
		{
			'name': Translate('库妮雅'),
			'pos': (-13199, 0, 11500),
			'angle': 90,
			'_1': b'\x01\x01\x00\x00\x00\x00\x00\x01',
			'function': Function((0, 12)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('欧赛尔'),
			'pos': (-10470, 0, 13340),
			'angle': 180,
			'_1': b'\x05\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('毕肖普'),
			'pos': (-52470, 2000, 21149),
			'angle': 90,
			'_1': b'\x01\x01\x00\x00\x02\x00\x00\x02',
			'function': Function((0, 15)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('奎因老人'),
			'pos': (39669, -2500, -19379),
			'angle': 180,
			'_1': b'\x15\x01\x00\x00\x03\x00\xff\xff',
			'function': Function((0, 16)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('亚米萨'),
			'pos': (38439, -2490, -18079),
			'angle': 135,
			'_1': b'\x05\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((0, 17)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (7469, -699, 3029),
			'angle': 180,
			'_1': b'\xc5\x01\x00\x00\n\x00\xff\xff',
			'function': Function((0, 24)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (9489, -699, 129),
			'angle': 64,
			'_1': b'\x85\x01\x00\x00\x0b\x00\x00\t',
			'function': Function((0, 25)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (42000, -2500, 0),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x0c\x00\x00\x00',
			'function': Function((0, 26)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (40000, -2500, 0),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\r\x00\x00\x00',
			'function': Function((0, 27)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (40000, -2500, -1250),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x0e\x00\x00\x00',
			'function': Function((0, 28)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (38000, -2500, 0),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x0f\x00\x00\x00',
			'function': Function((0, 29)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (17629, 0, -2130),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x17\x00\x00\x00',
			'function': Function((0, 30)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (9409, 0, 13489),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x0c\x00\x00\x00',
			'function': Function((0, 31)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (22500, 0, 1019),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x18\x00\x00\x00',
			'function': Function((0, 32)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (2900, 0, 9310),
			'angle': 90,
			'_1': b'\x95\x01\x00\x00\x19\x00\x00\x00',
			'function': Function((0, 33)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (3730, 0, 8510),
			'angle': 45,
			'_1': b'\x85\x01\x00\x00\x1a\x00\x00\x00',
			'function': Function((0, 34)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('水上巴士向导'),
			'pos': (42450, -2500, 2329),
			'angle': 235,
			'_1': b'\x85\x01\x00\x00\x10\x00\x00\x00',
			'function': Function((0, 36)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('黑月成员'),
			'pos': (18989, 9, 19649),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((0, 35)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('格蕾丝'),
			'pos': (3069, -699, 1110),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x08\x00\x00\x00',
			'function': Function((0, 21)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('雷因兹'),
			'pos': (21620, 0, 14909),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x07\x00\x00\x00',
			'function': Function((0, 20)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('罗伯兹主任'),
			'pos': (-9189, -9, 12270),
			'angle': 315,
			'_1': b'\x85\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 19)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游击士斯克特'),
			'pos': (3259, -699, 1440),
			'angle': 90,
			'_1': b'\x95\x01\x00\x00\x11\x00\x00\x00',
			'function': Function((0, 22)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('帕尔'),
			'pos': (5159, -699, 1639),
			'angle': 270,
			'_1': b'\x95\x01\x00\x00\x12\x00\x00\x00',
			'function': Function((0, 23)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('尼克鲁'),
			'pos': (-18000, 0, -5750),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x13\x00\x00\x03',
			'function': Function((0, 38)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('瑟蕾奴'),
			'pos': (-16979, 0, -13449),
			'angle': 45,
			'_1': b'\x85\x01\x00\x00\x14\x00\x00\x00',
			'function': Function((0, 39)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('弗兰兹巡警'),
			'pos': (19100, 0, 16600),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\t\x00\x00\x00',
			'function': Function((0, 37)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('黑月成员'),
			'pos': (22399, 0, 19500),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('黑月成员'),
			'pos': (24000, 0, 17899),
			'angle': 45,
			'_1': b'\xc5\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('刘'),
			'pos': (19879, 0, 19629),
			'angle': 225,
			'_1': b'\x85\x01\x00\x00\x15\x00\x00\x00',
			'function': Function((0, 40)),
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
			'name': Translate('银'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('达德利的车'),
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
			'pos': (21.0, 5.5, -1.5),
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
				-1.4000000953674316,
				-1.8333333730697632,
				0.30000001192092896,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 54)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (13.5, 11.5, -1.0),
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
				-4.5,
				-1.149999976158142,
				0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 54)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (19200, 250, 20500),
			'range': 2000,
			'bubble_pos': (19200, 1250, 20500),
			'_1': b'|\x00\x00',
			'function': Function((0, 42)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (68620, -2500, 15400),
			'range': 1200,
			'bubble_pos': (68040, -3500, 11820),
			'_1': b'|\x00\x00',
			'function': Function((0, 41)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (34000, -2500, 3400),
			'range': 1500,
			'bubble_pos': (34000, -1500, 3400),
			'_1': b'|\x00\x00',
			'function': Function((0, 57)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (77440, -2500, 19770),
			'range': 1200,
			'bubble_pos': (77440, -1000, 19770),
			'_1': b'|\x00\x00',
			'function': Function((0, 58)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x1a\x00', Function((0, 10)), Function((0, 11))),
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
		Insn('0x95', Char(254), (14600, 0, 11500), 1000, 0),
		Insn('0x95', Char(254), (20200, 0, 8200), 1000, 0),
		Insn('0x95', Char(254), (20200, 0, -6200), 1000, 0),
		Insn('0x95', Char(254), (14000, 0, -11700), 1000, 0),
		Insn('0x95', Char(254), (-14000, 0, -11700), 1000, 0),
		Insn('0x95', Char(254), (-20000, 0, -6400), 1000, 0),
		Insn('0x95', Char(254), (-20000, 0, 6000), 1000, 0),
		Insn('0x95', Char(254), (-13200, 0, 11500), 1000, 0),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('SLEEP', 3000),
		Insn('0x95', Char(254), (-13000, 2000, 21150), 5000, 0),
		Insn('0x95', Char(254), (-13000, 2000, 24150), 5000, 0),
		Insn('0xA0', Char(254), 5000, 64256),
		Insn('0xA0', Char(254), 4000, 64256),
		Insn('0xA0', Char(254), 5000, 64256),
		Insn('0xA0', Char(254), 4000, 64256),
		Insn('0x95', Char(254), (1760, 2000, 24150), 5000, 0),
		Insn('0x95', Char(254), (1760, 5080, 38700), 8000, 0),
		Insn('SLEEP', 3000),
		Insn('0x95', Char(254), (1760, 2000, 24150), 5000, 0),
		Insn('0x95', Char(254), (-13000, 2000, 24150), 5000, 0),
		Insn('0x95', Char(254), (-13000, 0, 14240), 5000, 0),
		Insn('0x95', Char(254), (-22130, 0, 5860), 5000, 0),
		Insn('0x95', Char(254), (-22020, 0, -46700), 5000, 0),
		Insn('SLEEP', 3000),
		Insn('0x95', Char(254), (-22130, 0, 5860), 5000, 0),
		Insn('0x95', Char(254), (-15540, 0, 14240), 5000, 0),
		Insn('0x95', Char(254), (-15540, 2000, 21150), 5000, 0),
		Insn('0x95', Char(254), (-52470, 2000, 21150), 5000, 0),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('0x95', Char(254), (-13000, 0, -10000), 4000, 0),
		Insn('0x95', Char(254), (13000, 0, -10000), 4000, 0),
		Insn('0x95', Char(254), (18000, 0, -4300), 4000, 0),
		Insn('0x95', Char(254), (18000, 0, 7040), 4000, 0),
		Insn('0x95', Char(254), (13000, 0, 10000), 4000, 0),
		Insn('0x95', Char(254), (-12700, 0, 10000), 4000, 0),
		Insn('0x95', Char(254), (-18000, 0, 5200), 4000, 0),
		Insn('0x95', Char(254), (-18000, 0, -5750), 4000, 0),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (1800, 3890), (-1630, 3130), 1000),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('CHAR_ROTATE', Char(254), 180, 500),
	Insn('CHAR_ROTATE', Char(254), 270, 500),
	Insn('CHAR_ROTATE', Char(254), 0, 500),
	Insn('CHAR_ROTATE', Char(254), 90, 500),
	Insn('CHAR_ROTATE', Char(254), 180, 500),
	Insn('CHAR_ROTATE', Char(254), 270, 500),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('CHAR_ROTATE', Char(254), 180, 700),
	Insn('CHAR_ROTATE', Char(254), 90, 700),
	Insn('CHAR_ROTATE', Char(254), 0, 700),
	Insn('CHAR_ROTATE', Char(254), 270, 700),
	Insn('CHAR_ROTATE', Char(254), 180, 700),
	Insn('CHAR_ROTATE', Char(254), 90, 700),
	Insn('CHAR_ROTATE', Char(254), 0, 700),
	Insn('CHAR_ROTATE', Char(254), 270, 700),
	Insn('CHAR_ROTATE', Char(254), 180, 700),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('CHAR_ROTATE', Char(254), 270, 920),
	Insn('CHAR_ROTATE', Char(254), 0, 920),
	Insn('CHAR_ROTATE', Char(254), 90, 920),
	Insn('CHAR_ROTATE', Char(254), 180, 920),
	Insn('CHAR_ROTATE', Char(254), 270, 920),
	Insn('CHAR_ROTATE', Char(254), 0, 920),
	Insn('CHAR_ROTATE', Char(254), 90, 920),
	Insn('CHAR_ROTATE', Char(254), 180, 920),
	Insn('CHAR_ROTATE', Char(254), 315, 920),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('CHAR_ROTATE', Char(254), 0, 650),
	Insn('CHAR_ROTATE', Char(254), 90, 650),
	Insn('CHAR_ROTATE', Char(254), 180, 650),
	Insn('CHAR_ROTATE', Char(254), 270, 650),
	Insn('CHAR_ROTATE', Char(254), 0, 650),
	Insn('CHAR_ROTATE', Char(254), 90, 650),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (7970, 1350), (2009, -2050), 1000),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 106), Insn('EQ'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('0x23', 7), Insn('CONST', 11), Insn('EQ'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (4870, 3350, 31570), 180),
					Insn('CHAR_SET_POS', Char(1), (4870, 3350, 31570), 180),
					Insn('CHAR_SET_POS', Char(2), (4870, 3350, 31570), 180),
					Insn('CHAR_SET_POS', Char(3), (4870, 3350, 31570), 180),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (4870, 3350, 31570), 180),
							Insn('CHAR_SET_POS', Char(5), (4870, 3350, 31570), 180),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (4870, 3350, 31570), 180),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 101), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('0x23', 7), Insn('CONST', 4), Insn('EQ'), Insn('0x23', 7), Insn('CONST', 6), Insn('EQ'), Insn('OR'), Insn('0x23', 7), Insn('CONST', 7), Insn('EQ'), Insn('OR'), Insn('0x23', 7), Insn('CONST', 10), Insn('EQ'), Insn('OR'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(0), (-28110, 2000, 23520), 90),
					Insn('CHAR_SET_POS', Char(1), (-28110, 2000, 23520), 90),
					Insn('CHAR_SET_POS', Char(2), (-28110, 2000, 23520), 90),
					Insn('CHAR_SET_POS', Char(3), (-28110, 2000, 23520), 90),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-28110, 2000, 23520), 90),
							Insn('CHAR_SET_POS', Char(5), (-28110, 2000, 23520), 90),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-28110, 2000, 23520), 90),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 102), Insn('SET'), Insn('END')])),
				]),
				(None, [
					Insn('CHAR_SET_POS', Char(0), (-19600, 0, -27950), 0),
					Insn('CHAR_SET_POS', Char(1), (-19600, 0, -27950), 0),
					Insn('CHAR_SET_POS', Char(2), (-19600, 0, -27950), 0),
					Insn('CHAR_SET_POS', Char(3), (-19600, 0, -27950), 0),
					Insn('IF', [
						(Expr([Insn('ATTR', 15), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-19600, 0, -27950), 0),
							Insn('CHAR_SET_POS', Char(5), (-19600, 0, -27950), 0),
						]),
						(Expr([Insn('ATTR', 14), Insn('CONST', 255), Insn('NE'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(4), (-19600, 0, -27950), 0),
						]),
						(None, []),
					]),
					Insn('EXPR_ATTR', 0, Expr([Insn('CONST', 100), Insn('SET'), Insn('END')])),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('0xD0', 7, Expr([Insn('CONST', 5), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 46))),
		]),
		(Expr([Insn('FLAG', Flag(737)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(737)),
			Insn('EVENT', Function((0, 52))),
		]),
		(Expr([Insn('FLAG', Flag(738)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(738)),
			Insn('EVENT', Function((0, 53))),
		]),
		(Expr([Insn('FLAG', Flag(739)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(739)),
			Insn('EVENT', Function((0, 55))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(27), 128),
			Insn('CHAR_SET_POS', Char(27), (2870, -700, -1190), 0),
			Insn('CHAR_FLAG1_UNSET', Char(26), 128),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 49, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(28), 128),
					Insn('CHAR_ROTATE', Char(9), 135, 0),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(27), 128),
			Insn('CHAR_FLAG1_UNSET', Char(25), 128),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(33), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('CHAR_FLAG1_UNSET', Char(20), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
			Insn('CHAR_FLAG1_UNSET', Char(22), 128),
			Insn('CHAR_FLAG1_UNSET', Char(23), 128),
			Insn('CHAR_SET_POS', Char(8), (7270, 200, 16400), 135),
			Insn('FORK_FUNC', Char(8), 0, Function((0, 0))),
			Insn('CHAR_SET_POS', Char(11), (17010, 0, -6810), 0),
			Insn('CHAR_SET_POS', Char(12), (15600, 0, -7280), 45),
			Insn('CHAR_SET_CHCP', Char(11), 22),
			Insn('FORK_FUNC', Char(11), 0, Function((0, 0))),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1556)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(34), 128),
					Insn('CHAR_FLAG1_UNSET', Char(35), 128),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1555)), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(33), (20500, 0, 15200), 180),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(12), 16),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(29), 128),
			Insn('CHAR_FLAG1_UNSET', Char(30), 128),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(12), 16),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(12), 128),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1034)), Insn('FLAG', Flag(1035)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(36), 128),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(12), 128),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(12), 16),
			Insn('CHAR_FLAG1_SET', Char(11), 16),
			Insn('CHAR_FLAG1_UNSET', Char(31), 128),
			Insn('CHAR_FLAG1_UNSET', Char(32), 128),
			Insn('CHAR_SET_POS', Char(32), (800, -700, 3300), 270),
			Insn('FORK_FUNC', Char(32), 0, Function((0, 4))),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(31), 128),
			Insn('CHAR_FLAG1_UNSET', Char(32), 128),
			Insn('CHAR_FLAG1_UNSET', Char(24), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_SET_POS', Char(15), (33460, -2500, 1730), 0),
			Insn('CHAR_FLAG1_SET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(31), 128),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(31), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG2_UNSET', Char(14), 32768),
		]),
		(None, [
			Insn('CHAR_FLAG1_SET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(31), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG2_UNSET', Char(13), 32768),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG2_UNSET', Char(14), 32768),
		]),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(768)), Insn('NOT'), Insn('FLAG', Flag(554)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x09', 268435456),
			Insn('EVENT', Function((0, 44))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('0x65', 0, 1),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1033)), Insn('FLAG', Flag(1034)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x66', 0, 1),
			Insn('OBJ_FLAG_UNSET', Object(4), 16),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1554)), Insn('FLAG', Flag(1555)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x00\x80\x00'),
			Insn('0xB5', b'\x01\x01\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1554)), Insn('NOT'), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'kurotuki01', Insn('0', 1)),
		]),
		(None, [
			Insn('OBJ_SET_FRAME', Object(255), 'kurotuki00', Insn('0', 1)),
		]),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(1033)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x66', 0, 1),
			Insn('OBJ_FLAG_UNSET', Object(4), 16),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1035)), Insn('FLAG', Flag(1554)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x66', 0, 1),
			Insn('OBJ_FLAG_UNSET', Object(4), 16),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1556)), Insn('END')]), [
			Insn('0x66', 0, 1),
			Insn('OBJ_FLAG_UNSET', Object(4), 16),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('FLAG', Flag(1792)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x65', 0, 1),
			Insn('OBJ_FLAG_UNSET', Object(4), 16),
		]),
		(None, []),
	]),
	Insn('OBJ_FLAG_SET', Object(6), 4),
	Insn('OBJ_FLAG_SET', Object(8), 4),
	Insn('OBJ_FLAG_SET', Object(9), 4),
	Insn('OBJ_FLAG_SET', Object(10), 4),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(777)), Insn('FLAG', Flag(801)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(6), 4),
			Insn('OBJ_FLAG_UNSET', Object(8), 4),
			Insn('OBJ_FLAG_UNSET', Object(9), 4),
			Insn('OBJ_FLAG_UNSET', Object(10), 4),
			Insn('OBJ_SET_FRAME', Object(6), 'light', Insn('0', 1)),
			Insn('0x71', Object(6), b',\x01', 300, 0),
		]),
		(None, []),
	]),
	Insn('OBJ_FLAG_SET', Object(5), 4),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1033)), Insn('FLAG', Flag(1035)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(5), 4),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 50, 0)), Insn('CONST', 0), Insn('EQ'), Insn('EXEC', Insn('ITEM_GET', 51, 0)), Insn('CONST', 0), Insn('EQ'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 52, 0)), Insn('CONST', 0), Insn('EQ'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 53, 0)), Insn('CONST', 0), Insn('EQ'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 54, 0)), Insn('CONST', 0), Insn('EQ'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 55, 0)), Insn('CONST', 0), Insn('EQ'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x65', 1, 1),
		]),
		(None, []),
	]),
	Insn('EFF_LOAD', ResId(8), 'eff\\mgm03_02.eff'),
	Insn('EFF_PLAY', (ResId(8), 8), Char(255), 0, 2504, 1, -3500, -1, 11820, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('SOUND_POSITION', 126, [
		81470,
		0,
		-30350,
		80000,
		50000,
	], 100, 0),
	Insn('0xE1', (81380, 0, 29160)),
	Insn('0xE1', (80980, 0, 53680)),
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
		(Expr([Insn('FLAG', Flag(1537)), Insn('FLAG', Flag(1542)), Insn('NOT'), Insn('BOOL_AND'), Insn('0x23', 1), Insn('CONST', 1), Insn('EQ'), Insn('BOOL_AND'), Insn('END')]), []),
		(None, [
			Insn('0x16', Insn('3', b'\x1d\x01\x00')),
		]),
	]),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 2, Insn('TASK_GET', 3))), Insn('EXEC', Insn('QUEST_GET', 2, Insn('TASK_GET', 4))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 2, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_WATCH', Char(0), Char(8), 0),
			Insn('0x4B', Char(8), -1),
			Insn('CALL', Function((0, 56))),
			Insn('RETURN'),
		]),
		(None, []),
	]),
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(17)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'竟然把车票弄丢，\n'
				'真是位粗心的游客呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'一想到他正在满城寻找，\n'
				'就觉得很可怜啊。\n'
				'快点给他送过去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'自治州议会\n'
						'终于结束了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真期待预算的发表。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'听说自治州议会\n'
						'终于结束了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呼……真是开了很久啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不知道麦克道尔市长\n'
						'最后是否为我们努力了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'克洛斯贝尔时报周刊的记者\n'
				'采访了我。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'是个感觉有些娃娃脸的好青年……㈱{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然男子气概还差了那么一点，\n'
				'不过应该很有前途。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天我本来想去散步……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'但竟然有警察在守卫着，\n'
				'气氛还真是有些紧张呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'哈尔特曼议长\n'
						'几乎不在媒体上露面，\n'
						'是那种喜欢在幕后指挥的人吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'可是，作为市民，\n'
						'还是想多了解他一点呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'哈尔特曼议长那沉着的架势，\n'
						'给人有滴水不漏的感觉。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'他几乎不曾出现在媒体上呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但有传言说，\n'
						'他准备参加这次市长选举……\n'
						'对市民来说，他是个值得关注的人物吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'米修拉姆的商店街\n'
						'好像发生了事件……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但是，既没有看到新闻，\n'
						'也听不到什么传言呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我听小道消息说，\n'
						'米修拉姆的商店街\n'
						'好像发生了事件呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'在纪念庆典期间，\n'
						'竟然出现了那种大乱子。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但奇怪的是……\n'
						'新闻中却没有进行任何报道。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 14))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((2, 20))),
				]),
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'今年会有什么样\n'
						'的娱乐表演呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'从下个月开始，就是纪念庆典了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'今年的庆典好像要持续五天，\n'
						'必须安排好日程啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 14))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((2, 20))),
				]),
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'唯一的遗憾就是，\n'
						'只能从杂志上欣赏他的照片……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'ＩＢＣ的库罗伊斯总裁\n'
						'只有四十多岁呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'在年轻时就已历任要职，\n'
						'是个超级精干的人。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'再加上又帅又成熟……！\n'
						'实在是个完美的男人啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'彩虹剧团的男演员\n'
						'各有各的风格。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然我都很喜欢……\n'
						'但一定要选一个的话，\n'
						'我还是首选尤金大人哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'彩虹剧团的那两位\n'
						'男演员都很棒呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'『金发王子』尤金大人和\n'
						'『沉默贵公子』缇奥多尔大人。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，要让我选一个的话，\n'
						'我还是会选尤金大人吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'因为他是王子殿下嘛。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'最近，在这附近\n'
						'能看到市长的首席秘书。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……他是个很不错的人，\n'
						'还会对我打招呼呢㈱{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'最近，在这附近\n'
						'能看到一个\n'
						'衣着讲究的青年。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那个人……好像是\n'
						'市长的首席秘书吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'他对工作很热心。\n'
						'还会对我打招呼。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔的政治局面，\n'
						'有点乱糟糟的感觉。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但是我觉得，\n'
						'至少市长还是可以信赖的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我是市长的支持者呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'市长看起来是个意志坚定的人，\n'
						'给人的感觉很好。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'至少对市长，\n'
						'我还是支持的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'最近，在这个公园里运动\n'
				'的人好像多起来了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'难道是正在兴起\n'
				'什么热潮吗。\n'
				'……我也去看看好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'在米修拉姆的主题乐园里，\n'
				'有一个很大很大的摩天轮。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'除此之外，\n'
				'还有云霄飞车和鬼屋之类的游戏设施。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我好想坐一次云霄飞车看看啊。\n'
				'还一次都没有坐过呢～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'最近，在公园的附近，\n'
						'好像成立了一家东方风格的公司。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'几乎看不到他们的职员，\n'
						'到底是做什么的公司呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'最近，在公园的附近，\n'
						'好像成立了一家东方风格的公司。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'他们那栋东方风格的红色建筑\n'
						'看上去还挺可爱的，\n'
						'不知什么时候就已经建好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……他们之前有施工过吗，\n'
						'我都没有注意到呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'在这附近，每到早晨就有很多\n'
				'穿西装的人路过～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'那些人就是通常所说的\n'
				'『商务人士』吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……穿着整洁西装\n'
				'的男人……\n'
				'感觉有些帅气呢㈱{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(2)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'穿西装的男人\n'
				'还挺帅的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'每到早晨就能看见很多，\n'
				'不知不觉就看花了眼呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 2, Insn('TASK_GET', 0))), Insn('EXEC', Insn('QUEST_GET', 2, Insn('TASK_GET', 3))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 2, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F（港湾区的公园……\n'
				'\u3000这里是遗失了物品的特伦特先生\n'
				'\u3000途中经过的地方。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F不好意思，请问您在这附近\n'
				'捡到过什么失物吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呃，你们在找东西吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'这么说来……昨天有个看上去\n'
				'傻呼呼的青年去过那边的公园。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'走到半路时，突然大喊『背包破啦～』\n'
				'什么的，吵闹了好久呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(0), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 30),
			Insn('EMOTE', Char(1), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('EMOTE', Char(2), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 50),
			Insn('EMOTE', Char(3), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 1200),
			Insn('TEXT_TALK', Char(259), Text(
				'#0203F应该就是他吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'但是，\n'
				'我只是站在远处看到的而已。\n'
				'并不知道他丢了什么东西。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0006F是这样啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，不过……\n'
				'今天早晨，有一位客人\n'
				'说是捡到了什么。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'那是一位经常在附近散步的小姑娘，\n'
				'你们不妨去问问她吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('QUEST', 2, Insn('TASK_SET', 3)),
			Insn('TEXT_END', Char(254)),
			Insn('RETURN'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 2, Insn('TASK_GET', 0))), Insn('EXEC', Insn('QUEST_GET', 2, Insn('TASK_GET', 4))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 2, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天早晨，有一位客人\n'
				'说是捡到了什么。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'那是一位经常在附近散步的小姑娘。\n'
				'如果你们正在寻找失物，\n'
				'不妨去问问她吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_END', Char(254)),
			Insn('RETURN'),
		]),
		(None, []),
	]),
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
				Insn('OPEN_SHOP', 123),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), []),
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
				Insn('IF', [
					(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('RECIPE', 1)), Insn('NOT'), Insn('END')]), [
								Insn('CALL', Function((0, 14))),
							]),
							(Expr([Insn('EXEC', Insn('QUEST_GET', 49, Insn('FLAG_GET', 16))), Insn('END')]), [
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
										Insn('TEXT_TALK', Char(254), Text(
											'这位客人，您可真有眼光……{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(254), Text(
											'我一定会为您准备\n'
											'最美味的面条。{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
									(None, [
										Insn('TEXT_TALK', Char(254), Text(
											'这位客人，\n'
											'您是想要最有嚼劲的面条吧。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(254), Text(
											'嗯……交给我好了，\n'
											'就让我为您奉上最美味的面条吧。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('FLAG_SET', Flag(3)),
									]),
								]),
							]),
							(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'那个记者好像是\n'
									'克洛斯贝尔时报周刊的……\n'
									'到底在调查什么呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'那些记者们\n'
									'好像在到处打听呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'在我这里也\n'
									'没完没了地问了半天。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'比如身边有没有人\n'
									'变得异常之类的……\n'
									'……到底在调查些什么呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(3)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('RECIPE', 1)), Insn('NOT'), Insn('END')]), [
								Insn('CALL', Function((0, 14))),
							]),
							(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'那个公司的职员\n'
									'看起来很沉着大胆呢。\n'
									'已经完全平静下来了啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'据说那个公司昨天遭到了袭击，\n'
									'但现在已经完全平静下来了。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'墙上虽然还残留着弹痕，\n'
									'但职员们却没有表现出丝毫的惊惶……\n'
									'还真是非常沉着大胆啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(3)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('RECIPE', 1)), Insn('NOT'), Insn('END')]), [
								Insn('CALL', Function((0, 14))),
							]),
							(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'不过是这种程度的骚乱罢了，\n'
									'我才没有关张停业的打算呢。\n'
									'哼……别小看我啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'夜里好像发生了什么事件。\n'
									'从早上开始，警察们就慌慌张张的。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'……我吗？\n'
									'我可没有关张停业的打算。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'哼……只是这种程度的小骚乱而已，\n'
									'我怎么可能会因此而关张。\n'
									'还有很多老顾客在期待我的汤面呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(3)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('RECIPE', 1)), Insn('NOT'), Insn('END')]), [
								Insn('CALL', Function((0, 14))),
							]),
							(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'坐在桌子前不停地写文件，\n'
									'这种工作究竟哪里有乐趣啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'所谓的商务人士，\n'
									'真是一种让人难以理解的职业。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'最近，有一位事业状况\n'
									'好得出奇的客人。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'据说他们公司的事业\n'
									'进展得非常顺利，\n'
									'所以心情特别好……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'嗯，所谓的商务人士，\n'
									'真是一种让人难以理解的职业啊。{wait}'
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
									'发音不标准也就罢了，\n'
									'但你可不要说这里是\n'
									'奇形怪状的哦。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'像我这种摊子，\n'
									'在东方可是很常见的呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('EMOTE', Char(339), 0, 2000, (0, 1, 250, 2)),
								Insn('SOUND_PLAY', 29, 0, 0, 100),
								Insn('SLEEP', 1000),
								Insn('TEXT_TALK', Char(339), Text(
									'#1110F喂，这也是露天店吗？\n'
									'还真是奇形怪状呢！{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'嗯……？竟敢说我的摊子奇形怪状！？\n'
									'这叫东方风格啦！！{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(339), Text(
									'#1107F……洞～方～风～格！{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('EMOTE', Char(254), 0, 2000, (14, 15, 250, 2)),
								Insn('SOUND_PLAY', 23, 0, 0, 100),
								Insn('SLEEP', 1000),
								Insn('TEXT_TALK', Char(254), Text(
									'发音错了……\n'
									'算、算了……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(3)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 14))), Insn('BOOL_AND'), Insn('END')]), [
								Insn('CALL', Function((2, 19))),
								Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
							]),
							(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'嗯……世界真是很大呢，\n'
									'我也要继续努力才行。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'前几天，我去光顾了\n'
									'东侧大道的那家东方风味饭店。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'他们做的面相当不错呢。\n'
									'几乎和我做的不相上下，\n'
									'甚至可能在我之上……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'唔唔……真是服了，\n'
									'看来我的修行仍然有所不足啊……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(3)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 14))), Insn('BOOL_AND'), Insn('END')]), [
								Insn('CALL', Function((2, 19))),
								Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
							]),
							(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'在克洛斯贝尔，\n'
									'只要向『克洛斯贝尔工商协会』\n'
									'提交申请，就可以开露天店呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'他们不像其它机关那么麻烦，\n'
									'是一群很好说话的人。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'就快到纪念庆典了……\n'
									'如果要在庆典时开露天店，\n'
									'就必须去登记申请。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'另外，克洛斯贝尔的露天店\n'
									'是由一个叫做『克洛斯贝尔工商协会』\n'
									'的团体所管理的。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'那个团体的人很不错，都很好说话。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(3)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'以前，在我的老顾客之中，\n'
									'有一对年轻的警察搭档。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'他们经常一边吃面条，\n'
									'一边谈论着警察的未来。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(257), Text(
									'#0002F…………………………\n'
									'（哈哈，莫非是……）{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'别看我的露天店不起眼，\n'
									'其实有很多回头客呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'其中有两位据说都是\n'
									'警察的青年顾客。\n'
									'他们以前经常来光顾呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'没记错的话，其中一位是个子很高，性格沉着\n'
									'的男人，还有一位是栗色头发的热血青年……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('CHAR_WATCH', Char(254), Char(257), 500),
								Insn('SLEEP', 500),
								Insn('TEXT_TALK', Char(254), Text(
									'对了，那个栗色头发的青年\n'
									'好像和你长得很像呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
								Insn('SLEEP', 1000),
								Insn('TEXT_TALK', Char(257), Text(
									'#0005F哎，和我……吗？{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'这么一说的话，气质好像也相似呢。\n'
									'嗯，那位青年看起来也很诚实。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('CHAR_WATCH', Char(254), Char(0), 0),
								Insn('FLAG_SET', Flag(3)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'我至今仍在\n'
									'对面条进行研究。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'吃面的时候，如果有什么意见，\n'
									'请不要有所顾虑，欢迎多多指点。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'今天的面可是别具一格呢！{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'尽管是粗面条，\n'
									'但在汤汁的搭配下，口感非常柔滑……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'这面条在杆制的时候，\n'
									'使用了玛因兹山道的小河水。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'这筋道又紧绷的面条，\n'
									'你们只要一吃便知。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(3)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'不好意思，我可没义务听人发牢骚哦。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'你们也一样，如果想发什么牢骚，\n'
									'可不要找我哦。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'商人这种职业，\n'
									'好像非常累人呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'有很多客人在下班的路上来这里吃饭，\n'
									'全都在这里大发牢骚。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'……听别人发牢骚又不是我的义务。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(3)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'嗯……在面条这一点上，\n'
									'我可是讲究独树一帜的。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'我这里和一般的露天店相比，\n'
									'可是有本质区别的呢，本质区别！{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'虽说是露天店的面条，\n'
									'但你可不能小看哦。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'我每天早晨都在家制面，\n'
									'并将那些在最适当的时间制作出的发酵物\n'
									'在这里煮熟。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'我这里和一般的露天店相比，\n'
									'可是有本质区别的呢，本质区别！{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(3)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
								Insn('TEXT_TALK', Char(254), Text(
									'好啦，不必客气。\n'
									'来尝尝我做的面条吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'我是放弃了祖父传下来的店面，\n'
									'开始经营这个摊位的。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'这也是为了追求极致，\n'
									'做出最好的面条而进行的修行……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'为了听取更多顾客的意见，\n'
									'所以我才做出了这个选择。\n'
									'你们也一定要尝一尝啊。{wait}'
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
									'在这附近，\n'
									'旧市街的不良少年有时会出现。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'真是的……\n'
									'再闹个没完，小心我把面条塞进他们嘴里。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(None, [
								Insn('TEXT_TALK', Char(254), Text(
									'在这附近，经常有\n'
									'旧市街的不良少年出没。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(254), Text(
									'从傍晚到深夜，\n'
									'动不动就大叫大嚷地胡闹。\n'
									'真是没少给我们添乱。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(3)),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
						Insn('TEXT_TALK', Char(254), Text(
							'我做的面条可是天下第一呢。\n'
							'您要是怀疑的话，尝尝便知！{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(None, [
						Insn('TEXT_TALK', Char(254), Text(
							'面条就是要有弹力才好吃！{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(254), Text(
							'必须要像这样富有弹性！{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(254), Text(
							'怎么样啊，你们也\n'
							'来一碗尝尝吧。{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('FLAG_SET', Flag(3)),
					]),
				]),
			]),
			(None, []),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('TEXT_TALK', Char(254), Text(
		'我想要挑战一下新口味，\n'
		'于是尝试着做了一下\n'
		'龙老饭店的汤面……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'模仿果然是行不通的啊。\n'
		'这个食谱就送给你们好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'学习了{item 401}{color 0}的做法。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'记住了{item 401}{color 0}的食谱。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('RECIPE', 1),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'ＩＢＣ的安保体系\n'
						'好像是世界顶尖的呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'据说花了不少米拉……\n'
						'或许比警察局还要可靠吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'ＩＢＣ的保安部门很厉害呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'好像连送来的邮包都要\n'
						'先用导力探知机来检测呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'负责警备工作的全是些\n'
						'性情温和的人，\n'
						'但他们的能力都很优秀呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天的航空邮件\n'
				'还没有送到啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'好奇怪啊……\n'
				'出了什么事呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天总是\n'
				'有警车停驻呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'出什么事了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'从今往后，克洛斯贝尔\n'
						'应该会越发繁荣起来吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但我们的工作量也会因此而增加呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'自从纪念庆典开始，\n'
						'这条商业街变得热闹了很多。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'目睹了纪念庆典的兴隆，\n'
						'似乎有非常多的公司\n'
						'计划进驻至此。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哎呀呀……\n'
						'工作量又要增加了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'糟糕，今天是\n'
				'ＩＢＣ的休息日呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'啊啊，白将货物\n'
				'搬来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'最近好像有不少企业在\n'
						'引进一种叫做导力网络的东西，\n'
						'不知那是零件还是什么。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'要小心些处理。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'最近，标记为精密仪器的\n'
						'小包裹变多了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'好像是结晶回路什么的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'要小心些处理。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'有一些公司\n'
				'会给很多的小费呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'到那些公司去送快递，\n'
				'还真是令人期待啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我们公司要是也能\n'
				'给我们配备导力车就好了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'之前的休假，因为突然\n'
				'接到紧急工作，被迫取消了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵……服务业真是很辛苦啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'这个假期，我准备去米修拉姆\n'
				'好好放松一下。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'现在就有些等不及了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯～这个公司在哪里呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'好像是不久前刚建成的，\n'
				'一时想不起地址呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'据说旧市街那里\n'
				'发生了斗殴事件？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'真可怕啊，我们也得小心一点。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'这一带的建筑物大多都是公司。\n'
				'包裹多得送不过来。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，接下来的配送地点是……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'喂，让开让开～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我让孙女\n'
						'费了不少心呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我似乎是有些\n'
						'顽固过头了吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……我的孙女真是个好孩子。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我这个老家伙真不该\n'
						'让她那么操心……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'孙女说，哪怕只有今天一天也好，\n'
						'希望一直陪在我身边……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……难不成，是在\n'
						'担心我的身体吗…… {wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我都和孙女说了，\n'
						'让她赶快回家去……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(11), 0, 2000, (14, 15, 250, 2)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(254), Text(
						'据说昨天发生了枪击事件，\n'
						'小孩子应该赶快回家啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('CHAR_WATCH', Char(254), Char(0), 0),
			Insn('TEXT_TALK', Char(254), Text(
				'真是一起让人不安的事件啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……今天还是让孙女\n'
				'早点回去为好吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我无论如何也不希望\n'
				'让孙女遇到什么危险。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_ROTATE', Char(254), 0, 0),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我才不想吃药呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我只要能钓鱼就好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我已经决定了，\n'
				'就要这么度过余生。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'在纪念庆典这段时间，\n'
				'都没能好好钓鱼。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哼，所有人都\n'
				'兴奋过头了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 19))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((0, 59))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……孙女的心情我也明白。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'她是个好孩子，\n'
						'心地很善良呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但是我也活不了多久了，\n'
						'人生的最后一段，就让我随心所欲地享受吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 19))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((0, 59))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……孙女今天也来了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'唔，但是不巧，\n'
						'我今天也很忙呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'钓鱼是我唯一的乐趣……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'今天也靠钓鱼来打发一整天的时间吧，\n'
				'可别打扰我哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'哼，我可不喜欢\n'
						'集体活动。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'最近有一伙叫什么『钓公师团』\n'
						'的家伙们来邀请我加入。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哼，但我可不喜欢集体活动。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'说什么『享受钓鱼的乐趣』？真是不知所谓。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我可是早就决定好了，\n'
						'要把剩下的时间全部用来专心钓鱼。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然有些对不起孙女，但是我可不想吃药。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CALL', Function((0, 18))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'这样下去的话，连条鱼都钓不上来了。\n'
						'真是的……！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'啧，没事搞什么水上巴士……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'是不是存心给我捣乱啊。\n'
						'真讨厌，让人火大……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'警察局的搜查一课中\n'
						'汇集了很多精英男子。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'比如我在几年前遇到的那个搜查官，\n'
						'年纪轻轻的，眼神却坚定诚实，感觉很不错……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'男人若是没有那种程度的热忱和实力，\n'
						'我是不会认可的！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔的公务人员都让人信不过。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'其中最差的当属警察了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'连调查工作都做不好，\n'
						'还会迫于政治家的压力，\n'
						'做出保释坏人之类的事情。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哼，真是群一无是处的家伙们。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'能得到老夫认同的，\n'
						'也就只有『搜查一课』了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'哼，我非常不喜欢克洛斯贝尔人，{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'厌恶到了想吐的程度。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我很反感克洛斯贝尔人，{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'整天就只想着赚钱，\n'
						'不懂尊重古来的传统与规矩……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'他们很容易被流行牵着鼻子走，\n'
						'只关注那些风言风语的报道。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'而且还都喜欢聚在一起搞什么庆典。\n'
						'真是群只知道胡闹的无聊家伙啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……算啦，说到底，其实我也是\n'
						'生长在克洛斯贝尔的啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(5)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'一个一个的全都这么\n'
				'不成气候，唉……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'怎么，年轻人，\n'
				'你们是来给我捣乱的吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'赶快走开，\n'
				'你们把鱼都吓跑了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(5)),
			Insn('CHAR_FLAG1_SET', Char(11), 16),
			Insn('CHAR_ROTATE', Char(11), 180, 0),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我想通了，\n'
						'以后不必太勉强爷爷。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'因为爷爷还是\n'
						'非常有精神的嘛。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我决定了，\n'
						'以后不再缠着爷爷了～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然我还是很想让爷爷\n'
						'去医院看病，好好按时吃药。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但不管怎么说，\n'
						'爷爷毕竟还是\n'
						'很有精神的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'希望爷爷今天\n'
						'能钓到一大堆鱼啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，我决定了，\n'
						'今天要陪在\n'
						'爷爷的身边。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'因为，让爷爷独自一人的话，\n'
						'我会担心嘛……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'钓鱼的时候，爷爷好像很开心，\n'
						'我最喜欢这样的爷爷了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀～发生什么事了？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我来啦，爷爷。\n'
				'我又把药取来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'您按时吃药了吗？\n'
				'不听医生的话\n'
				'可不行哦～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'明年要是能和爷爷一起\n'
						'开心地逛庆典就好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呼，纪念庆典\n'
						'结束了呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我最后\n'
						'也没能去玩。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我原本很想\n'
						'和爷爷一起去逛逛呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'呼，我很想为爷爷\n'
						'做点什么……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'直到去年为止，\n'
						'爷爷他一直都在住院。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但他说不喜欢医院，\n'
						'于是就自作主张地溜出来了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呼，爷爷的心情，我也很理解……\n'
						'但是，这样下去还是不好吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'爷爷他总是\n'
						'皱着眉头钓鱼。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'医院开的药也不吃……\n'
						'呼，我好担心啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'爷爷，今天难道\n'
						'不想去东侧大道看看吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'好不好嘛，一起去逛逛吧！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
					Insn('CHAR_FLAG1_UNSET', Char(12), 16),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我爷爷是个\n'
				'非常顽固的人呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'而且他很讨厌医院。\n'
				'呼，很让人担心啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('CALL', Function((0, 18))),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('0x4B', Char(12), -1),
	Insn('0x4B', Char(11), -1),
	Insn('TEXT_TALK', Char(12), Text(
		'爷爷～\n'
		'我把药拿来了哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'我说……您有没有\n'
		'每天按时吃药啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'烦死人了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'我才不需要吃什么药，\n'
		'赶快回家去。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'又这样说……\n'
		'这怎么行啊，爷爷！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(6)),
	Insn('0x4C', Char(12), -1),
	Insn('0x4C', Char(11), -1),
	Insn('CHAR_FLAG1_UNSET', Char(12), 16),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'缇欧，在这种时间，\n'
				'你要去哪里啊？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'警察的工作也很辛苦啊……\n'
				'一定要当心哦！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F嗯，没问题的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(7)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'警察的工作也很辛苦啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'缇欧和各位\n'
				'都要注意安全哦！{wait}'
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
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'格蕾丝前辈从早上开始就\n'
						'特别在意那个传闻呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'好像是有什么情况吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'有消息说，从今天早晨开始，\n'
						'就有人相继失踪。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'现在正在进行调查，\n'
						'并搜集相关的情报……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这个事件肯定有写成新闻的价值吧？\n'
						'虽然是比较古怪的事件……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(8)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(8)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啊啊，好想早点回家……\n'
				'但又不能把前辈一个人扔下……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呼，我到底该如何是好……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀呀，怎么办呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'格蕾丝前辈扔下我一个人，\n'
				'去紧急采访了呢！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(0), 0, 2000, (38, 38, 250, 1)),
			Insn('EMOTE', Char(1), 0, 2000, (38, 38, 250, 1)),
			Insn('EMOTE', Char(2), 0, 2000, (38, 38, 250, 1)),
			Insn('EMOTE', Char(3), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F难、难道是……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0205F去了黑月的事务所吗……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……（紧张）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'前辈……还是放弃吧。\n'
				'我可没法和你一起去啊～！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(8)),
			Insn('FLAG_SET', Flag(1667)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1908)), Insn('END')]), [
			Insn('TEXT_TALK', Char(26), Text(
				'#2103F鲁巴彻也好，\n'
				'失踪的市民也好……{wait}'
				'{page}'
				'好像总有种\n'
				'不详的预感呢。{wait}'
				'{page}'
				'#2101F如果你们准备继续调查的话，\n'
				'一定要多加小心。{wait}'
				'{page}'
				'#2109F然后，还要平安无事地\n'
				'把独家新闻拿给我！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0002F哈哈……明白了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0104F格蕾丝小姐也\n'
						'不要太勉强啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(9)),
				]),
				(None, []),
			]),
		]),
		(None, [
			Insn('TEXT_TALK', Char(26), Text(
				'#2105F啊呀，这不是支援课的诸位嘛。{wait}'
				'{page}'
				'#2101F据说，黑手党的人都失踪了，\n'
				'是真的吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0011F这、这个……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0101F这件事……\n'
				'您是从哪里听来的？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(26), Text(
				'#2103F哈，我们也有\n'
				'一些自己的情报网呢。{wait}'
				'{page}'
				'先不提这些，听说，冈兹先生\n'
				'昨天也失踪了……{wait}'
				'{page}'
				'#2101F除此之外，市内的失踪人数\n'
				'还在急剧增加。{wait}'
				'{page}'
				'这种情况……总感觉～\n'
				'非常不妙啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0013F……嗯。\n'
				'总之，无论如何也要尽快\n'
				'查清究竟发生了什么……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(26), Text(
				'#2104F嗯，这么说来，\n'
				'你们也正在追查这件事吧……\n'
				'（做笔记……）{wait}'
				'{page}'
				'#2110F好啦～基本明白了。\n'
				'要是有什么发现的话，请再通知我！{wait}'
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
				'#0211F罗伊德前辈，\n'
				'你还是说漏嘴了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0006F……真惭愧，\n'
				'我明明还留心提防了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F算啦，在刚才那种情况下，\n'
				'说漏嘴也是没办法的，别介意啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1908)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(11)), Insn('NOT'), Insn('END')]), [
					Insn('0x4B', Char(29), -1),
					Insn('0x4B', Char(30), -1),
					Insn('TEXT_TALK', Char(29), Text(
						'#08405F呦，帕、帕尔，\n'
						'好久不见了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(30), Text(
						'嗯，是啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(30), Text(
						'……我以为你把我忘得\n'
						'干干净净了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(29), 0, 2000, (40, 43, 100, 3)),
					Insn('SLEEP', 500),
					Insn('TEXT_TALK', Char(29), Text(
						'#08405F那、那怎么可能嘛！\n'
						'因为游击士的工作\n'
						'太忙了啊……！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(30), Text(
						'……呵呵，开玩笑啦㈱{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(30), Text(
						'你在游击士的工作中所付出的努力，\n'
						'我可是最清楚不过了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(29), Text(
						'#08402F帕、帕尔……㈱{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(29), 0, 2000, (10, 11, 250, 2)),
					Insn('SOUND_PLAY', 27, 0, 0, 100),
					Insn('SLEEP', 20),
					Insn('EMOTE', Char(30), 0, 2000, (10, 11, 250, 2)),
					Insn('SOUND_PLAY', 27, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(339), Text(
						'#1109F……气氛真好呀～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(29), Char(339), 500),
					Insn('CHAR_WATCH', Char(30), Char(339), 500),
					Insn('EMOTE', Char(29), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('EMOTE', Char(30), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 1200),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F（琪、琪雅！\n'
						'\u3000不要去给人家捣乱……！）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(30), Text(
						'那、那个……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(29), Text(
						'#08400F哈、哈哈……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_ROTATE', Char(29), 90, 0),
					Insn('CHAR_ROTATE', Char(30), 270, 0),
					Insn('0x4C', Char(29), -1),
					Insn('0x4C', Char(30), -1),
					Insn('FLAG_SET', Flag(11)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#08402F那、那么……\n'
						'我们就重振精神，\n'
						'先去吃个饭如何？{wait}'
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
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(11)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 22))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……嗯，是啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'机会难得，\n'
						'到处看看吧。{wait}'
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

data['code'][24] = [
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
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀呀，这个料理\n'
				'很好吃呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'是在那边的摊位买的，\n'
				'有种让人怀念的味道呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'这里正好有个公园，\n'
				'就稍微休息一下吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀呀，克洛斯贝尔市可真大啊。\n'
				'带着小孩来逛，似乎是个错误呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'那个摊位的荞麦面\n'
				'非常非常好吃哦！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'逛来逛去的，真是累坏了呢～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'好想吃冰淇淋啊～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'吃过午饭之后，\n'
				'没能赶上水上巴士呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'但是没想到，很快就又来了一艘。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'早知如此，\n'
				'根本就不该着急嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯嗯，前往米修拉姆的\n'
				'水上巴士是在这里搭乘吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'听说米修拉姆\n'
				'有很多漂亮的店铺，\n'
				'很令人期待呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'我要和女儿一起去米修拉姆。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'可以乘坐水上巴士，\n'
		'真让人有点兴奋呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][28] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'哇～好大的船啊～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'我是第一次坐船呢～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][29] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'听说米修拉姆\n'
		'有很多的娱乐场所呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'嘿嘿嘿，很期待呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][30] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'（嘀嘀咕咕）……\n'
		'果然是鲁巴彻搞的鬼啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'所以说，黑手党就是可怕……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][31] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'黑月贸易公司……\n'
		'从来没听说过呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'难道是做了什么\n'
		'招人怨恨的事情吗？\n'
		'女神保佑，女神保佑……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][32] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(13)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'这种事件，经常会发生吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过，办公区的公司遭遇袭击，\n'
				'或许还真是第一次呢。\n'
				'实在是让我也吃了一惊啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(13)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'也不知道警察都在干些什么。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'每次都是等到事件发生之后，\n'
				'他们才慢悠悠地到来……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][33] = [
	Insn('TEXT_START', Char(254)),
	Insn('0x4B', Char(23), -1),
	Insn('TEXT_TALK', Char(254), Text(
		'哇，好破烂啊～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(23), Char(254), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(23), Text(
		'嘘，不可以靠近哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(23), 45, 0),
	Insn('0x4C', Char(23), -1),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][34] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'我经常来这个公园\n'
		'玩呢，竟然会……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'真是的，警察到底\n'
		'都在干什么啊……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][35] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'……您有什么事吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F啊，没什么……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1667)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#0106F（格蕾丝小姐也真是\n'
				'\u3000够厉害的……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][36] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(10)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'前往米修拉姆的乘客，\n'
				'请稍等片刻。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'本班水上巴士将于\n'
				'五分钟之后出航。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'前往米修拉姆的乘客，\n'
				'请稍等片刻。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'本班水上巴士将于\n'
				'五分钟之后出航。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F哦，这就是开往那个著名『米修拉姆』\n'
				'的水上巴士啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F听说那边有主题乐园\n'
				'和商店街之类的地方，\n'
				'非常适合游玩呢。{wait}'
				'{page}'
				'#0305F……对了，罗伊德，\n'
				'你去过那边吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0006F没有，那里毕竟是\n'
				'在我离开克洛斯贝尔的期间\n'
				'建成的设施。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F算了，不管怎么说，\n'
				'现在可没有闲工夫乘坐哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(10)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][37] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1556)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(12)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14501F说起来，刚才还被\n'
						'达德利警官和艾玛警官\n'
						'狠狠瞪了一下。{wait}'
						'{page}'
						'#14506F黑月的成员也在这附近晃来晃去的……\n'
						'真是不想负责这种地方\n'
						'的巡逻工作啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14506F哎呀，从刚才开始，\n'
						'黑月的成员就\n'
						'一直在晃来晃去的呢……{wait}'
						'{page}'
						'#14501F啊，不是成员，\n'
						'该说是『职员』才对。{wait}'
						'{page}'
						'#14503F虽然现在不见了……\n'
						'但稍后肯定还会再出现吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F不好意思，弗兰兹，这里就拜托你了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F不过，应该不会有人来袭击的。\n'
						'我觉得不必担心。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(254), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(254), Text(
						'#14501F呼，话是这么说啦……\n'
						'但还是没法彻底放心啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(12)),
				]),
			]),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'#14501F虽说是大半夜，\n'
				'但竟然会在离公园这么近的地方\n'
				'真枪实弹地发生战斗……{wait}'
				'{page}'
				'#14501F对了，至于达德利警官那边，\n'
				'你能帮我稍微敷衍一下吗？{wait}'
				'{page}'
				'#14506F我可不想再遭他的白眼。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][38] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哼，我这次一定要争取到角色。\n'
				'一、二……一、二……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(14)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'瑟、瑟蕾奴前辈来了吗……！？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'下周就要公布演员表了。\n'
						'谁都坐不住了吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(14)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'下周就要公布了呢……\n'
						'呼，压力好大……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(14)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'每天练习跑步的话，\n'
						'肚子会饿得不行呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但体重增加的话，\n'
						'弹跳力就会下降……\n'
						'呼，真辛苦……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(14)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呼，必须要\n'
						'努力锻炼……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(14)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'一、二……一、二……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……听说，在这个公园附近，\n'
						'有家东西很好吃的摊贩呢。\n'
						'嗯～好想尝尝……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(14)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'啊……肚子饿了……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(14)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'一、二……一、二……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……嘿哟……\n'
						'首先要从基础的体力开始锻炼啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(14)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'干、干什么……？\n'
						'你可别妨碍我啊！{wait}'
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

data['code'][39] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
				Insn('IF', [
					(Expr([Insn('FLAG', Flag(16)), Insn('END')]), [
						Insn('0x4C', Char(32), -1),
					]),
					(None, [
						Insn('BREAK'),
					]),
				]),
				Insn('SLEEP', 200),
			]),
			Insn('0x4B', Char(32), -1),
			Insn('CHAR_WATCH', Char(254), Char(0), 500),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(15)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'马上就要正式公布演员阵容了，\n'
						'可不是悠闲享乐的时候。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'在休息日也\n'
						'一定要努力练习……！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(15)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我这次可是以二号主角为目标呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'一定要争取到一个\n'
						'重要的角色……！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('0x4C', Char(32), -1),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(15)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'尼克鲁那家伙，竟然在\n'
						'这种地方做跑步训练啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我也不会输给他的！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'光是一个莉夏就让人压力很大了……\n'
						'…………呼………{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(15)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我、我也不会输给他的！{wait}'
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

data['code'][40] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK2', Char(36), Translate('东方长相的男人'), Text(
		'#5P分公司社长愿意见你们。\n'
		'──请入内吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][41] = [
	Insn('EVENT_BEGIN', 1),
	Insn('SOUND_PLAY', 1094, 0, 255, 100),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F这里的话似乎可以钓到鱼。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (63790, 0, 7940), 1500),
	Insn('CAM_ROTATE', 45, 23, 0, 1500),
	Insn('0x6E', 280, 1500),
	Insn('CAM_DISTANCE', 29000, 1500),
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
			Insn('MINIGAME', 6, 1, [
				68580,
				-2500,
				16500,
				180,
				68040,
				-3500,
				11820,
			]),
		]),
		(None, []),
	]),
	Insn('0xE0', b'\x02'),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][42] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(1033)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_START', Char(255)),
			Insn('CALL', Function((0, 43))),
			Insn('TEXT_END', Char(255)),
		]),
		(Expr([Insn('FLAG', Flag(1033)), Insn('FLAG', Flag(1034)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 45))),
		]),
		(Expr([Insn('FLAG', Flag(1035)), Insn('FLAG', Flag(1554)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_START', Char(255)),
			Insn('CALL', Function((0, 43))),
			Insn('TEXT_END', Char(255)),
		]),
		(Expr([Insn('FLAG', Flag(1556)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_START', Char(255)),
			Insn('CALL', Function((0, 43))),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0001F（想再进去一次的话……\n'
						'\u3000……恐怕很难吧。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0103F（那位分公司社长\n'
						'\u3000大概也正忙着应付\n'
						'\u3000各式各样的『工作』吧……）{wait}'
						'{page}'
						'#0101F（能问到这些话，\n'
						'\u3000已经算是幸运了。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, []),
			]),
			Insn('TEXT_END', Char(255)),
		]),
		(None, [
			Insn('TEXT_START', Char(255)),
			Insn('CALL', Function((0, 43))),
			Insn('TEXT_END', Char(255)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][43] = [
	Insn('SOUND_PLAY', 810, 0, 0, 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}大门上着锁，\n'
		'并挂着一块牌子。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}『黑月贸易公司丄克洛斯贝尔分公司』\n'
		'※若有要事，敬请敲门。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(536)), Insn('FLAG', Flag(1033)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1184)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F『黑月贸易公司』……{wait}'
				'{page}'
				'难道这里就是\n'
				'伊安律师曾说过的……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0301F是从共和国进驻这里的\n'
				'那个黑手党组织的据点吧。{wait}'
				'{page}'
				'#0306F话虽如此，\n'
				'不过，看起来还真像是个普通的公司啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0101F普通的也只是外表而已吧。{wait}'
				'{page}'
				'内部是个什么样的组织，\n'
				'却完全弄不清楚。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F不管怎么说，他们应该和鲁巴彻一样，\n'
				'都不是我们可以随便\n'
				'干涉的对象呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F嗯，而且我们目前\n'
				'也没有任何证据\n'
				'能表明他们是犯罪组织。{wait}'
				'{page}'
				'#0003F（……但如果有机会，真想好好调查\n'
				'\u3000一下这个地方呢……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('FLAG_SET', Flag(1184)),
	Insn('RETURN'),
]

data['code'][44] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x0A', 268435456),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CAM_OFFSET', (45480, 0, 3700), 0),
	Insn('CAM_ROTATE', 45, 8, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 29000, 0),
	Insn('CHAR_FLAG1_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 32768),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (1340, 1800, -380), 10000),
	Insn('CAM_ROTATE', 45, 24, 0, 10000),
	Insn('0x6E', 600, 10000),
	Insn('CAM_DISTANCE', 26000, 10000),
	Insn('0x6F', b'y'),
	Insn('SLEEP', 500),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-7040, 4500, 24940), 0),
	Insn('CAM_ROTATE', 20, 24, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 26000, 0),
	Insn('CAM_OFFSET', (-2790, 2500, 5490), 8000),
	Insn('CAM_ROTATE', 35, 32, 0, 8000),
	Insn('0x6E', 600, 8000),
	Insn('CAM_DISTANCE', 51580, 8000),
	Insn('0xCB', b'T\x01\xc8\x00', 'c_plac31', b'\x00\xa0\x0f'),
	Insn('0x6F', b'y'),
	Insn('SLEEP', 1000),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(527)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_MESSAGE', Char(258), Text(
				'#0104F面朝羽扇河，\n'
				'南望艾鲁姆湖的港湾区域……{wait}'
				'{page}'
				'#0100F这附近是办公区吧。\n'
				'北侧的建筑全都是公司呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_MESSAGE', Char(260), Text(
				'#0309F哈哈，但是也有个\n'
				'感觉很不错的公园呢。{wait}'
				'{page}'
				'#0302F那里是给人休息的地方吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_MESSAGE', Char(259), Text(
				'#0203F据数据库的记载，那个地方\n'
				'好像叫做『港湾公园』。\n'
				'……很直接了当的名字。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_MESSAGE', Char(257), Text(
				'#0005F啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x5A'),
			Insn('CROSSFADE', 500),
			Insn('CAM_OFFSET', (-13890, 5100, 25220), 0),
			Insn('CAM_ROTATE', 0, 12, 0, 0),
			Insn('0x6E', 600, 0),
			Insn('CAM_DISTANCE', 26000, 0),
			Insn('0x0D'),
			Insn('SLEEP', 500),
			Insn('TEXT_MESSAGE', Char(257), Text(
				'#0000F是克洛斯贝尔时报周刊。\n'
				'原来已经搬到那里了啊。{wait}'
				'{page}'
				'#0003F（嗯，过了三年的时间，\n'
				'\u3000果然变化不少呢。）{wait}'
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
		'{color 5}港湾区是位于城市东北方向的商业街。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}面向克洛斯贝尔最大的河流──羽扇河，\n'
		'有一座公园，是游客与市民们的休息之所。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}除了各大公司，知名的『克洛斯贝尔通讯社』\n'
		'大楼也矗立于此。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('CHAR_FLAG1_UNSET', Char(10), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(9), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(8), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(13), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(14), 32768),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 100), Insn('EQ'), Insn('END')]), [
			Insn('CAM_OFFSET', (-19600, 2500, -27950), 0),
			Insn('CAM_ROTATE', 45, 25, 0, 0),
			Insn('0x6E', 600, 0),
			Insn('CAM_DISTANCE', 25000, 0),
		]),
		(None, []),
	]),
	Insn('FLAG_SET', Flag(554)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][45] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('CHAR_SET_POS', Char(257), (18600, 0, 17800), 0),
	Insn('CHAR_SET_POS', Char(258), (19700, 0, 17800), 0),
	Insn('CHAR_SET_POS', Char(259), (18600, 0, 16600), 0),
	Insn('CHAR_SET_POS', Char(260), (19700, 0, 16600), 0),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1091)), Insn('NOT'), Insn('END')]), [
			Insn('CAM_OFFSET', (22000, 3700, 20500), 0),
			Insn('CAM_ROTATE', 24, 15, 0, 0),
			Insn('0x6E', 600, 0),
			Insn('CAM_DISTANCE', 21500, 0),
			Insn('CAM_ROTATE', 37, 6, 0, 6000),
			Insn('CAM_DISTANCE', 18000, 6000),
			Insn('0x0D'),
			Insn('0xCB', b'T\x01\xc8\x00', 'c_plac13', b'\x00\xe8\x03'),
			Insn('0x6F', b'y'),
			Insn('SLEEP', 1000),
			Insn('CROSSFADE', 500),
			Insn('CAM_OFFSET', (22000, 1000, 21000), 0),
			Insn('CAM_ROTATE', 45, 18, 0, 0),
			Insn('0x6E', 560, 0),
			Insn('CAM_DISTANCE', 21500, 0),
			Insn('CAM_OFFSET', (22000, 0, 21000), 2000),
			Insn('0x6F', b'\x01'),
			Insn('0x0D'),
		]),
		(None, [
			Insn('CAM_OFFSET', (22000, 0, 21000), 0),
			Insn('CAM_ROTATE', 45, 18, 0, 0),
			Insn('0x6E', 560, 0),
			Insn('CAM_DISTANCE', 21500, 0),
			Insn('0x0D'),
		]),
	]),
	Insn('CALL', Function((0, 43))),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1091)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#12100962V#12P#0001F是这里吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1091)),
		]),
		(None, []),
	]),
	Insn('CHAR_WATCH', Char(258), Char(257), 500),
	Insn('TEXT_TALK', Char(258), Text(
		'#12100963V#11P#0101F……要怎么办呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('MENU', 0, -1, -1, 0, Text(
		'【敲门】\n'
		'【离开】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('FORK_LOOP', 258, 2, [
				Insn('CHAR_WATCH', Char(254), Char(257), 500),
			]),
			Insn('FORK', 257, 1, [
				Insn('0x96', Char(254), (19100, 0, 19700), 2000, 0),
			]),
			Insn('FORK_AWAIT', Char(257), 1),
			Insn('FORK_QUIT', Char(258), 2),
			Insn('SLEEP', 300),
			Insn('SOUND_PLAY', 811, 0, 0, 100),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(257), Text(
				'#12100964V#11P#0001F──不好意思！\n'
				'请问有人在吗！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 500),
			Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
			Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
			Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
			Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
			Insn('SLEEP', 2000),
			Insn('EMOTE_STOP', Char(257)),
			Insn('EMOTE_STOP', Char(258)),
			Insn('EMOTE_STOP', Char(259)),
			Insn('EMOTE_STOP', Char(260)),
			Insn('BGM_SET_VOLUME', b'<,\x01\x00\x00'),
			Insn('SOUND_PLAY', 855, 0, 0, 100),
			Insn('SLEEP', 3000),
			Insn('CHAR_SET_POS', Char(36), (19100, 350, 21500), 180),
			Insn('0x4B', Char(36), -1),
			Insn('CHAR_FLAG1_UNSET', Char(36), 128),
			Insn('CHAR_FLAG2_UNSET', Char(36), 32768),
			Insn('TEXT_TALK2', Char(36), Translate('男人的声音'), Text(
				'#12100965V#5P#2S……请问是哪位？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#12100966V#12P#0003F………我们是克洛斯贝尔警察局丄\n'
				'特务支援课的成员。{wait}'
				'{page}'
				'#12100967V#0001F关于某个事件，\n'
				'希望能向贵公司的分公司社长\n'
				'进行简短的询问。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK2', Char(36), Translate('男人的声音'), Text(
				'#12100968V#5P#2S#40W………………………………{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK2', Char(36), Translate('男人的声音'), Text(
				'#12100969V#5P#2S……请各位稍等。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SOUND_PLAY', 855, 0, 0, 100),
			Insn('SLEEP', 3000),
			Insn('BGM_SET_VOLUME', b'd,\x01\x00\x00'),
			Insn('CHAR_ROTATE', Char(257), 180, 500),
			Insn('TEXT_TALK', Char(257), Text(
				'#12100970V#0006F#5P那么……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#12100971V#12P#0303F那位社长究竟是龙是蛇呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#12100972V#6P#0201F#6P……还真是很期待\n'
				'会面的瞬间啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CHAR_FLAG1_UNSET', Char(36), 4),
			Insn('CHAR_SET_POS', Char(36), (19100, 350, 21500), 180),
			Insn('CHAR_SET_COLOR', Char(36), Color(0x00FFFFFF), 0),
			Insn('CHAR_SET_POS', Char(257), (18600, 0, 17800), 0),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('SOUND_PLAY', 809, 0, 0, 100),
			Insn('SLEEP', 500),
			Insn('0x71', Object(4), b'\x00\x00', 5, 0),
			Insn('SOUND_PLAY', 103, 0, 0, 100),
			Insn('0x79', b'\x04\x00'),
			Insn('FORK', 36, 1, [
				Insn('0x95', Char(254), (19100, 0, 19700), 1500, 0),
			]),
			Insn('FORK', 36, 2, [
				Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
			]),
			Insn('FORK_AWAIT', Char(36), 1),
			Insn('FORK_AWAIT', Char(36), 2),
			Insn('SLEEP', 300),
			Insn('TEXT_TALK2', Char(36), Translate('东方长相的男人'), Text(
				'#12100973V#5P──让各位久等了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK2', Char(36), Translate('东方长相的男人'), Text(
				'#12100974V#5P分公司社长愿意见你们，\n'
				'请入内吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_ROTATE', Char(36), 225, 400),
			Insn('FORK', 36, 1, [
				Insn('0x96', Char(254), (19880, 0, 19630), 1000, 0),
			]),
			Insn('FORK_AWAIT', Char(36), 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#12100975V#6P#0000F谢、谢谢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#12100976V#12P#0103F……打扰了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x5A'),
			Insn('CHAR_SET_POS', Char(0), (19100, 0, 17200), 0),
			Insn('0x4C', Char(36), -1),
			Insn('0x4C', Char(8), -1),
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
			Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
			Insn('OBJ_FLAG_SET', Object(4), 16),
			Insn('OBJ_FLAG_UNSET', Object(4), 2),
			Insn('0x65', 0, 1),
			Insn('FLAG_SET', Flag(1034)),
			Insn('EVENT_END', 5),
			Insn('BREAK'),
		],
		1: [
			Insn('CHAR_SET_POS', Char(0), (19100, 0, 17200), 0),
			Insn('0x4C', Char(8), -1),
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
			Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
			Insn('EVENT_END', 5),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('RETURN'),
]

data['code'][46] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00900', 30),
	Insn('CAM_OFFSET', (22000, 0, 19000), 0),
	Insn('CAM_ROTATE', 45, 18, 0, 0),
	Insn('0x6E', 560, 0),
	Insn('CAM_DISTANCE', 24500, 0),
	Insn('CHAR_SET_POS', Char(257), (19100, 350, 21500), 180),
	Insn('CHAR_SET_POS', Char(258), (19100, 350, 21500), 180),
	Insn('CHAR_SET_POS', Char(259), (19100, 350, 21500), 180),
	Insn('CHAR_SET_POS', Char(260), (19100, 350, 21500), 180),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_CHCP', Char(37), 30),
	Insn('CHAR_SET_FRAME', Char(37), 0),
	Insn('CHAR_FLAG1_UNSET', Char(36), 4),
	Insn('CHAR_SET_POS', Char(36), (19100, 350, 21500), 180),
	Insn('CHAR_SET_COLOR', Char(36), Color(0x00FFFFFF), 0),
	Insn('0x4B', Char(36), -1),
	Insn('CHAR_FLAG1_UNSET', Char(36), 128),
	Insn('CHAR_FLAG2_UNSET', Char(36), 32768),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(39), 128),
	Insn('0x78', b'\x05', Char(39)),
	Insn('OBJ_SET_FRAME', Object(5), 'light', Insn('0', 1)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(39), (5300, 0, -12500), 270),
	Insn('0xD3', Char(39), 0, 270000, 0, 0),
	Insn('OBJ_FLAG_SET', Object(5), 4096),
	Insn('0x74', Object(5), 7680),
	Insn('0x70', Object(5), b'\x00\x00'),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu00600.itp'),
	Insn('CAM_DISTANCE', 20500, 6000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('SLEEP', 1000),
	Insn('0x71', Object(4), b'\x00\x00', 5, 0),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('0x79', b'\x04\x00'),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (19700, 0, 14600), 2000, 0),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (18600, 0, 14600), 2000, 0),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 600),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (19700, 0, 15800), 2000, 0),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (18600, 0, 15800), 2000, 0),
	]),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK', 36, 1, [
		Insn('0x95', Char(254), (19100, 0, 17700), 2000, 0),
	]),
	Insn('FORK', 36, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(36), 1),
	Insn('FORK_AWAIT', Char(36), 2),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK2', Char(36), Translate('东方长相的男人'), Text(
		'#12101080V#5P……各位辛苦了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(36), Translate('东方长相的男人'), Text(
		'#12101081V#5P如果还有什么事情，\n'
		'欢迎随时光临。\n'
		'这是分公司社长让我给各位的传言。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101082V#12P#0003F……多谢关照。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(36), 0, 500),
	Insn('FORK', 36, 1, [
		Insn('0x95', Char(254), (19100, 0, 21500), 2000, 0),
	]),
	Insn('SLEEP', 1000),
	Insn('FORK', 36, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(36), 1),
	Insn('FORK_AWAIT', Char(36), 2),
	Insn('0x71', Object(4), b'\x05\x00', 0, 0),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('0x79', b'\x04\x00'),
	Insn('OBJ_FLAG_UNSET', Object(4), 16),
	Insn('CHAR_FLAG1_SET', Char(36), 128),
	Insn('CHAR_FLAG2_SET', Char(36), 32768),
	Insn('SLEEP', 700),
	Insn('SOUND_PLAY', 809, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('CAM_OFFSET', (22000, 0, 17870), 2000),
	Insn('CAM_ROTATE', 45, 20, 0, 2000),
	Insn('CAM_DISTANCE', 18950, 2000),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101083V#0006F#5P继鲁巴彻之后，\n'
		'这里也是如此吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101084V#0306F#12P呼，不过和那边相比，\n'
		'这边的态度起码要友好了很多……{wait}'
		'{page}'
		'#12101085V#0301F但也可能正好相反，他们其实更加瞧不起我们。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101086V#12P#0206F#6P那种可能性也无法否认……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(258)),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_WATCH', Char(260), Char(258), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101087V#6P#0005F艾莉，怎么了……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101088V#6P#0201F难道……\n'
		'你身体不舒服吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(258), 225, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101089V#5P#0104F不，没事的。{wait}'
		'{page}'
		'#12101090V#0108F……话说回来，\n'
		'按照曹先生的说法，那个叫『银』的\n'
		'强大刺客已经潜入到克洛斯贝尔了……{wait}'
		'{page}'
		'#12101091V#0101F感觉这个情报应该是真的呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101092V#6P#0001F嗯……\n'
		'从他的态度来看，应该没错。{wait}'
		'{page}'
		'#12101093V#0008F只是，我觉得那个分公司社长\n'
		'并不是向彩虹剧团和伊莉雅小姐\n'
		'发出恐吓的人呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(260), Char(257), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101094V#0301F#11P嗯，我也有同感。{wait}'
		'{page}'
		'#12101095V如果他们真是犯人的话，\n'
		'也就完全没有必要把自己\n'
		'与『银』的关系暗示给我们了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101096V#6P#0208F……如此说来……{wait}'
		'{page}'
		'#12101097V#0201F莫非恐吓信只是那个名叫『银』\n'
		'的暗杀者擅自做出的行动，\n'
		'与其雇主『黑月』完全无关？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 180, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101098V#0006F#5P如果是那样的话……\n'
		'我们的调查工作可就真的无从下手了。{wait}'
		'{page}'
		'#12101099V#0001F假如刚才那些话都是真的……\n'
		'那么，也许连那个分公司社长\n'
		'也都不了解『银』的底细吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101100V#0301F也就是说，目前唯一的办法\n'
		'就只有抓住他本人，把情况问清楚了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101101V#5P#0108F也许吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(258)),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101102V#5P#0103F如果那个叫『银』的刺客\n'
		'是以伊莉雅小姐为目标的话……{wait}'
		'{page}'
		'#12101103V事情恐怕就已经超出了\n'
		'我们的任务范围。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_WATCH', Char(260), Char(258), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101104V#6P#0005F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101105V#5P#0100F他的身手似乎非常高超，\n'
		'单凭我们，完全没有把握将其顺利抓捕。{wait}'
		'{page}'
		'#12101106V所以说，如今是不是应该\n'
		'把任务转交给警察局总部呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101107V#6P#0011F这个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101108V#6P#0205F但他们也许又会像旧市街事件时一样，\n'
		'假装什么都没听到呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101109V#5P#0103F不，对于克洛斯贝尔市而言，\n'
		'彩虹剧团与伊莉雅丄普拉提耶\n'
		'都是极其重要的存在。{wait}'
		'{page}'
		'#12101110V#0101F如果她陷入了危险状况，\n'
		'警察局总部也绝对不会坐视不理……{wait}'
		'{page}'
		'#12101111V即使赌上警察的威信，也必须将事件解决吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('CHAR_FLAG1_SET', Char(37), 32768),
	Insn('CHAR_SET_POS', Char(37), (19400, 0, 6200), 0),
	Insn('CHAR_FLAG1_UNSET', Char(37), 128),
	Insn('CHAR_FLAG2_UNSET', Char(37), 32768),
	Insn('SOUND_PLAY', 1557, 0, 255, 100),
	Insn('TEXT_TALK2', Char(37), Translate('男人的声音'), Text(
		'#12101112V──正是如此。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (22000, 0, 16000), 2500),
	Insn('CAM_DISTANCE', 20500, 2500),
	Insn('FORK', 37, 1, [
		Insn('0x96', Char(254), (19400, 0, 11200), 2000, 0),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 300),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 300),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 258, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 300),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 180, 300),
	]),
	Insn('FORK_AWAIT', Char(37), 1),
	Insn('0x6F', b'\x11'),
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
	Insn('TEXT_TALK', Char(257), Text(
		'#12101113V#0011F#5P您、您是……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101114V#5P#0105F是搜查一课的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101115V#11P#0603F一课的达德利。{wait}'
		'{page}'
		'#12101116V#0601F跟我来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101117V#0005F#5P哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101118V#11P#0601F……怎么会有人蠢到\n'
		'在这种地方闲聊个没完。{wait}'
		'{page}'
		'#12101119V好了，赶快跟我过来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101120V#0011F#5P明、明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101121V#5P#0301F喂，这是怎么回事啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(37), 180, 500),
	Insn('CAM_DISTANCE', 21000, 1500),
	Insn('FORK', 37, 1, [
		Insn('0x97', Char(254), (0, 0, -10000), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('FORK', 260, 1, [
		Insn('0x97', Char(254), (0, 0, -10000), 2000, 0),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 259, 1, [
		Insn('0x97', Char(254), (0, 0, -10000), 2000, 0),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 258, 1, [
		Insn('0x97', Char(254), (0, 0, -10000), 2000, 0),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 257, 1, [
		Insn('0x97', Char(254), (0, 0, -10000), 2000, 0),
	]),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(37), 1),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('FORK_QUIT', Char(259), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('0x6F', b'\x10'),
	Insn('CAM_OFFSET', (12300, 900, -10300), 0),
	Insn('CAM_ROTATE', 310, 33, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 25500, 0),
	Insn('CHAR_SET_POS', Char(37), (17600, 0, -6000), 225),
	Insn('CHAR_SET_POS', Char(257), (19600, 0, -4000), 225),
	Insn('CHAR_SET_POS', Char(258), (20600, 0, -3000), 225),
	Insn('CHAR_SET_POS', Char(259), (21600, 0, -2000), 225),
	Insn('CHAR_SET_POS', Char(260), (22600, 0, -1000), 225),
	Insn('FORK_FUNC', Char(37), 3, Function((0, 47))),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 48))),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 49))),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 50))),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 51))),
	Insn('CAM_OFFSET', (8200, 900, -10300), 8000),
	Insn('CAM_ROTATE', 315, 25, 0, 8000),
	Insn('CAM_DISTANCE', 19500, 8000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(37), 3),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x6F', b'y'),
	Insn('CHAR_ROTATE', Char(37), 90, 500),
	Insn('SLEEP', 150),
	Insn('SOUND_PLAY', 1555, 0, 255, 100),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 500),
	Insn('TEXT_MESSAGE', Char(37), Text(
		'#12101122V……你们难道是白痴吗？{wait}'
		'{page}'
		'#12101123V虽然不知你们有何目的，\n'
		'但怎么能如此冒失地闯进去……{wait}'
		'{page}'
		'#12101124V而且居然还在对方的门前\n'
		'若无其事地悠闲讨论案情。{wait}'
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
		'#12101125V#6P#0006F对、对不起……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101126V#0108F#12P……我们确实\n'
		'有些考虑不周。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101127V#5P#0603F哼……算了。{wait}'
		'{page}'
		'#12101128V#0600F──那么，说吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101129V#6P#0005F说……说什么啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101130V#5P#0601F你们刚才不是一直\n'
		'在说什么彩虹剧团吗？{wait}'
		'{page}'
		'#12101131V你们前来探访『黑月』，\n'
		'与它有何关系……{wait}'
		'{page}'
		'#12101132V一五一十地说出来吧。{wait}'
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
	Insn('0x82', 100, 0, 3000, 200),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101133V#6P#0013F什么……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101134V#12P#0301F喂喂……\n'
		'你在说什么啊，太唐突了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101135V#12P#0211F突然出现，还理所当然似地\n'
		'提出这么厚脸皮的要求……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101136V#5P#0604F哼……\n'
		'到底是谁更厚脸皮啊？{wait}'
		'{page}'
		'#12101137V我们一课从一个多月以前\n'
		'就已经盯上了『黑月』……{wait}'
		'{page}'
		'#12101138V#0601F什么招呼也没打，\n'
		'突然插手进来的可是你们。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101139V#6P#0011F是、是这样吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101140V#0101F#12P难道说……\n'
		'一课那边也在调查『银』？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101141V#5P#0603F哼……\n'
		'你们也知道这个名字了吗？{wait}'
		'{page}'
		'#12101142V#0601F总之，把你们了解到的情报\n'
		'毫无隐瞒地交代清楚。{wait}'
		'{page}'
		'#12101143V如果不服从的话……\n'
		'我就会以妨碍一课调查案件为由，\n'
		'向赛尔盖长官提出严重抗议。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101144V#6P#0008F可恶……明白了。{wait}'
		'{page}'
		'#12101145V#0013F只是……\n'
		'这毕竟是我们支援课接受的委托。{wait}'
		'{page}'
		'#12101146V希望您不要随便外传，可以吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101147V#5P#0603F那要由我来判断。{wait}'
		'{page}'
		'#12101148V#0601F好了，快说吧──这是命令。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 3000),
	Insn('CAM_DISTANCE', 19000, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(37), 0, 2000, (24, 27, 250, 0)),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'\x04\x02\x00'),
	Insn('CAM_DISTANCE', 19500, 2000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(37)),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101149V#5P#0604F──嗯，原来如此。{wait}'
		'{page}'
		'#12101150V本以为毫无头绪……\n'
		'结果他总算露出狐狸尾巴了吗。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101151V#0101F#12P狐狸尾巴……\n'
		'是指『银』吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101152V#5P#0600F……是的。{wait}'
		'{page}'
		'#12101153V#0603F为了与『鲁巴彻』对抗，\n'
		'『黑月』特别雇佣的强悍刺客，\n'
		'算得上是『黑月』的最终王牌。{wait}'
		'{page}'
		'#12101154V从经由某个途径得到情报以来，\n'
		'我们一课就一直在监视『黑月』。{wait}'
		'{page}'
		'#12101155V#0601F不过……\n'
		'真是没想到，竟会被你们这些\n'
		'菜鸟们误打误撞地发现了马脚。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101156V#12P#0304F嘿……\n'
		'还真会说呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101157V#12P#0201F不过……\n'
		'为什么只监视『黑月』呢？{wait}'
		'{page}'
		'#12101158V警察局对『鲁巴彻』那边\n'
		'好像一直都是放任不管的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101159V#5P#0604F哼，这叫什么话？{wait}'
		'{page}'
		'#12101160V『鲁巴彻』的大体动向，\n'
		'我们也已经掌握了。{wait}'
		'{page}'
		'#12101161V#0602F旧市街的事件与军犬的使用……{wait}'
		'{page}'
		'#12101162V你们处理的那一连串的事件，\n'
		'我们在事前都有一定程度的了解。{wait}'
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
		'#12101163V#6P#0005F#4S什么……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101164V#12P#0201F既然如此，为什么……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101165V#5P#0603F哼……那种程度的小事情，\n'
		'要是处理起来就没完没了了，还不值得我们浪费人力。{wait}'
		'{page}'
		'#12101166V#0600F又不是什么杀人事件，\n'
		'只不过是一些小小的纷争而已。{wait}'
		'{page}'
		'#12101167V我们怎能把其它重要案件搁置不管，\n'
		'将有限的人力用于这等琐碎小事？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101168V#6P#0007F话虽如此，但是……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101169V#5P#0601F──我们搜查一课\n'
		'和你们这群半吊子可不一样！{wait}'
		'{page}'
		'#12101170V#0603F在这座正义难以得到彻底伸张的城市中，\n'
		'我们至少要将基本秩序维持住……{wait}'
		'{page}'
		'#12101171V遏止杀人一类的重大犯罪，\n'
		'与犯罪组织和国外的间谍机关对抗，\n'
		'保障市民与社会的安全……{wait}'
		'{page}'
		'#12101172V#0601F我们的艰辛，你们理解得了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101173V#6P#0005F！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101174V#0108F#12P果然……是这样吗……{wait}'
		'{page}'
		'#12101175V#0106F克洛斯贝尔的和平与繁荣……\n'
		'只是建立在一层薄冰之上。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101176V#5P#0606F哼，但大多数市民\n'
		'却注意不到这个事实。{wait}'
		'{page}'
		'#12101177V#0600F『鲁巴彻』与帝国派议员\n'
		'相互勾结，可以说是众所周知了……{wait}'
		'{page}'
		'#12101178V而『黑月』与共和国派议员关系密切的\n'
		'事情却鲜有人知。{wait}'
		'{page}'
		'#12101179V#0603F以目前的形势来看，无论针对哪一方，\n'
		'我们都不可能直接出手。{wait}'
		'{page}'
		'#12101180V#0601F不仅如此……\n'
		'由于没有处理外国间谍的相关法律，\n'
		'所以，外国谍报员根本就是为所欲为。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101181V#6P#0013F……怎么会………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101182V#12P#0206F……真是难以置信。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101183V#12P#0306F好像有种……\n'
		'无药可救的感觉啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101184V#0108F#40W#12P……………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101185V#5P#0603F然而，即使在这种绝望的状态之下，\n'
		'我们也仍然坚定信念，做好自己力所能及之事。{wait}'
		'{page}'
		'#12101186V我们会权衡所有案件的危险程度，\n'
		'就算无法从根本上解决问题，\n'
		'至少也要为了抑制犯罪而不断努力……{wait}'
		'{page}'
		'#12101187V#0600F『银』的问题也只不过是其中的一环罢了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101188V#6P#0005F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101189V#5P#0600F关于彩虹剧团的事情，\n'
		'我们并没有察觉到。{wait}'
		'{page}'
		'#12101190V感谢你们提供的情报。{wait}'
		'{page}'
		'#12101191V以后的事情就交给我们一课来处理，\n'
		'你们可以回去执行日常任务了。{wait}'
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
		'#12101192V#6P#0007F#4S什么……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101193V#12P#0307F喂喂，为什么会是这样啊！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101194V#5P#0603F根据目前的情况来看，\n'
		'基本可以确定『银』是真实存在的了。{wait}'
		'{page}'
		'#12101195V既要监视『黑月』的动向，\n'
		'同时还要在神秘杀手的威胁之下，\n'
		'保护好伊莉雅丄普拉提耶……{wait}'
		'{page}'
		'#12101196V#0602F你们能胜任这项工作吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101197V#6P#0010F唔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101198V#12P#0206F……如果没有足够的人手，\n'
		'或许真的很勉强呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(37), 270, 500),
	Insn('CAM_OFFSET', (6890, 900, -9560), 2000),
	Insn('FORK', 37, 1, [
		Insn('0x95', Char(254), (5000, 0, -10300), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(37), 1),
	Insn('CHAR_ROTATE', Char(37), 180, 500),
	Insn('0x71', Object(5), b'\xf1\x00', 270, 0),
	Insn('SOUND_PLAY', 462, 0, 0, 100),
	Insn('0x79', b'\x05\x00'),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(37), Text(
		'#12101199V#0603F#5P联系彩虹剧团的任务\n'
		'就交给你们吧。{wait}'
		'{page}'
		'#12101200V至于恐吓事件的应对工作，\n'
		'就由我们搜查一课来接手……{wait}'
		'{page}'
		'#12101201V#0600F你们去把状况解释清楚吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 37, 1, [
		Insn('0x95', Char(254), (5000, 0, -11800), 2000, 0),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 37, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(37), 1),
	Insn('FORK_AWAIT', Char(37), 2),
	Insn('0x71', Object(5), b'\x0f\x01', 300, 0),
	Insn('SOUND_PLAY', 461, 0, 0, 100),
	Insn('0x79', b'\x05\x00'),
	Insn('0x71', Object(5), b'<\x00', 90, 0),
	Insn('0x79', b'\x05\x00'),
	Insn('SOUND_PLAY', 457, 0, 0, 100),
	Insn('0x71', Object(5), b'y\x00', 180, 32),
	Insn('FORK', 39, 1, [
		Insn('0x95', Char(254), (-14000, 0, -12500), 6500, 0),
	]),
	Insn('SLEEP', 1250),
	Insn('SOUND_PLAY', 458, 0, 0, 100),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-14500, 1000, -12500), 0),
	Insn('CAM_ROTATE', 40, 35, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 15500, 0),
	Insn('CAM_OFFSET', (-19500, 1000, -19500), 4000),
	Insn('CAM_ROTATE', 60, 25, 0, 4000),
	Insn('CAM_DISTANCE', 16500, 4000),
	Insn('FORK_AWAIT', Char(39), 1),
	Insn('FORK', 39, 1, [
		Insn('0x9E', Char(254), -14000, -18500, -90000, 6500, b'\x01\x00'),
	]),
	Insn('FORK_AWAIT', Char(39), 1),
	Insn('FORK', 39, 1, [
		Insn('0x95', Char(254), (-20000, 0, -33500), 6500, 0),
	]),
	Insn('FORK_AWAIT', Char(39), 1),
	Insn('0x6F', b'y'),
	Insn('CHAR_FLAG1_UNSET', Char(37), 32768),
	Insn('CHAR_FLAG1_SET', Char(37), 128),
	Insn('CHAR_FLAG2_SET', Char(37), 32768),
	Insn('CHAR_FLAG1_SET', Char(39), 128),
	Insn('OBJ_FLAG_SET', Object(5), 4),
	Insn('OBJ_FLAG_UNSET', Object(5), 4096),
	Insn('BGM_STOP', 6000),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (7700, 900, -10300), 0),
	Insn('CAM_ROTATE', 315, 27, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 19500, 0),
	Insn('CAM_OFFSET', (9810, 900, -10230), 3000),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101202V#0301F#12P可恶，把自己想说的话说完之后\n'
		'就立刻走掉了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101203V#12P#0211F而且还有专用车，\n'
		'更是让人感到火大……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101204V#0103F#11P#40W………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101205V#0008F#5P……不过，他说的这些话，\n'
		'也并不是无法理解。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_WATCH', Char(258), Char(257), 500),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101206V#0105F#11P哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 89, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_ROTATE', Char(260), 225, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101207V#0006F#5P这次的事件，确实已经超出了\n'
		'我们的能力范畴。{wait}'
		'{page}'
		'#12101208V至于莉夏与伊莉雅小姐那边，我们能做的\n'
		'也只有说明缘由和道歉了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101209V#0306F呼，也只能这样了吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101210V#12P#0208F没有……办法了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101211V#0107F#11P等、等一下！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_WATCH', Char(260), Char(258), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101212V#6P#0005F哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'\x03\x02\x00'),
	Insn('CAM_DISTANCE', 19000, 20000),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101213V#0106F#11P罗伊德……\n'
		'你竟然会说这种话！？{wait}'
		'{page}'
		'#12101214V#0101F你不是说过，要跨越『障壁』吗……\n'
		'只要大家齐心协力，就一定能跨越任何障壁，\n'
		'这不是你自己说过的话吗……！{wait}'
		'{page}'
		'#12101215V#0107F但现在，你为什么会……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101216V#6P#0011F艾、艾莉……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101217V#12P#0305F喂喂，怎么了啊？{wait}'
		'{page}'
		'#12101218V#0301F大小姐，\n'
		'你刚才不是也说过，\n'
		'应该把工作交给警察局总部吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101219V#0105F#11P#40W啊……{wait}'
		'{page}'
		'#12101220V#0108F#50W……是、是啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101221V#6P#0205F艾莉前辈……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101222V#6P#0006F那个……{wait}'
		'{page}'
		'#12101223V那个，其实我也很不甘心啊，\n'
		'也想要做点什么。{wait}'
		'{page}'
		'#12101224V#0000F既然艾莉都这么说了，\n'
		'那我们就考虑一些其它办法……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101225V#0106F#11P不必了……{wait}'
		'{page}'
		'#12101226V#0102F……对不起，\n'
		'我好像是有点累了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101227V#6P#0001F艾莉……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12101228V#12P#0306F唔，这也难怪。\n'
		'毕竟今天交涉的对象\n'
		'全都是一些难缠的家伙。{wait}'
		'{page}'
		'#12101229V#0300F先去彩虹剧团，\n'
		'向伊莉雅小姐他们报告一下，\n'
		'然后就回去休息吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12101230V#6P#0203F是啊……\n'
		'我也赞成。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12101231V#6P#0003F……嗯。{wait}'
		'{page}'
		'#12101232V#0000F艾莉，可以吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12101233V#0104F#11P嗯……谢谢大家……{wait}'
		'{page}'
		'#12101234V#0100F那我们现在\n'
		'就去彩虹剧团吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CAM_DISTANCE', 19500, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0x4C', Char(8), -1),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('0x4C', Char(10), -1),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('BGM_STOP', 3000),
	Insn('CHAR_SET_POS', Char(0), (9600, 0, -10300), 270),
	Insn('FLAG_SET', Flag(1035)),
	Insn('QUEST', 66, Insn('TASK_SET', 8)),
	Insn('0x66', 0, 1),
	Insn('OBJ_FLAG_UNSET', Object(4), 16),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'g\x00\x00'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][47] = [
	Insn('FORK', 37, 1, [
		Insn('0x95', Char(254), (13300, 0, -10300), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(37), 1),
	Insn('FORK', 37, 1, [
		Insn('0x95', Char(254), (6700, 0, -10300), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(37), 1),
	Insn('RETURN'),
]

data['code'][48] = [
	Insn('SLEEP', 500),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (13300, 0, -10300), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (9600, 0, -11100), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('CHAR_ROTATE', Char(257), 270, 500),
	Insn('RETURN'),
]

data['code'][49] = [
	Insn('SLEEP', 600),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (13300, 0, -10300), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (9600, 0, -9800), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('CHAR_ROTATE', Char(258), 270, 500),
	Insn('RETURN'),
]

data['code'][50] = [
	Insn('SLEEP', 700),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (13300, 0, -10300), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (11000, 0, -11100), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('CHAR_ROTATE', Char(259), 270, 500),
	Insn('RETURN'),
]

data['code'][51] = [
	Insn('SLEEP', 800),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (13300, 0, -10300), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (11000, 0, -9800), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('CHAR_ROTATE', Char(260), 270, 500),
	Insn('RETURN'),
]

data['code'][52] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (-1600, 2500, 5600), 0),
	Insn('CAM_ROTATE', 55, 5, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 29000, 0),
	Insn('CHAR_SET_POS', Char(0), (-19600, 0, -28000), 0),
	Insn('CHAR_SET_POS', Char(1), (-19600, 0, -28000), 0),
	Insn('CHAR_SET_POS', Char(2), (-19600, 0, -28000), 0),
	Insn('CHAR_SET_POS', Char(3), (-19600, 0, -28000), 0),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('CHAR_SET_POS', Char(9), (-10500, 0, 12000), 180),
	Insn('CHAR_FLAG1_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_SET_POS', Char(8), (8000, 0, 10000), 270),
	Insn('CHAR_FLAG1_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_SET_POS', Char(10), (-18000, 0, 12500), 180),
	Insn('CHAR_FLAG1_SET', Char(10), 32768),
	Insn('FORK', 8, 1, [
		Insn('0x98', Char(254), (-20000, 0, 0), 2000, 0),
	]),
	Insn('CAM_OFFSET', (-1600, 1500, 5600), 5000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('SLEEP', 1000),
	Insn('FORK', 10, 1, [
		Insn('0x98', Char(254), (0, 0, -30000), 6000, 0),
	]),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (22140, 2500, 20700), 0),
	Insn('CAM_ROTATE', 35, 20, 0, 0),
	Insn('0x6E', 660, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CAM_DISTANCE', 21000, 4000),
	Insn('SLEEP', 3000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'c1210', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][53] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00500', 30),
	Insn('LOAD_CHCP', 'apl/ch50220', 31),
	Insn('EFF_LOAD', ResId(0), 'event\\eva04_00.eff'),
	Insn('EFF_LOAD', ResId(1), 'event\\ev202_00.eff'),
	Insn('CAM_OFFSET', (21500, 7900, 24500), 0),
	Insn('CAM_ROTATE', 45, 15, 0, 0),
	Insn('0x6E', 650, 0),
	Insn('CAM_DISTANCE', 15000, 0),
	Insn('CHAR_SET_CHCP', Char(38), 30),
	Insn('CHAR_SET_FRAME', Char(38), 0),
	Insn('CHAR_FLAG1_UNSET', Char(38), 128),
	Insn('CHAR_FLAG2_UNSET', Char(38), 32768),
	Insn('CHAR_FLAG1_SET', Char(38), 32768),
	Insn('CHAR_SET_COLOR', Char(38), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(38), (23000, 9500, 24500), 270),
	Insn('EXPR_CHAR_ATTR', Char(38), 40, Expr([Insn('CONST', 13), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CAM_OFFSET', (21500, 10400, 24500), 5000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('SLEEP', 3000),
	Insn('EFF_PLAY', (ResId(1), -1), Char(38), 64, 0, 0, 1000, 0, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('SOUND_PLAY', 859, 0, 0, 100),
	Insn('CHAR_FLAG1_UNSET', Char(38), 128),
	Insn('CHAR_FLAG2_UNSET', Char(38), 32768),
	Insn('0x83', b'\x00&\x00\x1e\x00,\x01'),
	Insn('FORK', 38, 1, [
		Insn('0x95', Char(254), (21500, 9500, 24500), 1000, 0),
	]),
	Insn('FORK', 38, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 1500),
	]),
	Insn('FORK_AWAIT', Char(38), 1),
	Insn('FORK_AWAIT', Char(38), 2),
	Insn('0x83', b'\x01&\x00\x00\x00\x00\x00'),
	Insn('0x6F', b'\x01'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(38), 31),
	Insn('CHAR_SET_FRAME', Char(38), 1),
	Insn('SLEEP', 500),
	Insn('CAM_OFFSET', (14000, 9400, 24500), 700),
	Insn('CAM_ROTATE', 40, 18, 0, 700),
	Insn('CAM_DISTANCE', 17500, 700),
	Insn('0x83', b'\x00&\x00\x1e\x00,\x01'),
	Insn('CHAR_SET_FRAME', Char(38), 0),
	Insn('FORK', 38, 1, [
		Insn('0x9D', Char(254), 14000, 8500, 24500, 900, 3000),
	]),
	Insn('SOUND_PLAY', 854, 0, 0, 100),
	Insn('FORK_AWAIT', Char(38), 1),
	Insn('EFF_PLAY', (ResId(0), -1), Char(38), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('CHAR_SET_FRAME', Char(38), 1),
	Insn('SLEEP', 50),
	Insn('0x6F', b'y'),
	Insn('CAM_OFFSET', (14000, 11800, 31000), 700),
	Insn('CAM_ROTATE', 35, 15, 0, 700),
	Insn('CAM_DISTANCE', 18500, 700),
	Insn('CHAR_SET_FRAME', Char(38), 0),
	Insn('FORK', 38, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 0),
	]),
	Insn('FORK', 38, 1, [
		Insn('0x9D', Char(254), 14000, 10800, 31000, 3300, 3000),
	]),
	Insn('SOUND_PLAY', 854, 0, 0, 100),
	Insn('FORK_AWAIT', Char(38), 1),
	Insn('EFF_PLAY', (ResId(0), -1), Char(38), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('CHAR_SET_FRAME', Char(38), 1),
	Insn('SLEEP', 50),
	Insn('0x6F', b'y'),
	Insn('CAM_OFFSET', (-4000, 11200, 31000), 2000),
	Insn('CAM_ROTATE', 45, 27, 0, 2000),
	Insn('CAM_DISTANCE', 22500, 2000),
	Insn('CHAR_SET_FRAME', Char(38), 0),
	Insn('FORK', 38, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 0),
	]),
	Insn('FORK', 38, 1, [
		Insn('0x9D', Char(254), 9400, 11300, 31000, 900, 3000),
	]),
	Insn('SOUND_PLAY', 854, 0, 0, 100),
	Insn('FORK_AWAIT', Char(38), 1),
	Insn('CHAR_SET_FRAME', Char(38), 1),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(38), 0),
	Insn('FORK', 38, 1, [
		Insn('0x9D', Char(254), -3000, 9800, 31000, 1500, 3000),
	]),
	Insn('SOUND_PLAY', 854, 0, 0, 100),
	Insn('FORK_AWAIT', Char(38), 1),
	Insn('EFF_PLAY', (ResId(0), -1), Char(38), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('CHAR_SET_FRAME', Char(38), 1),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(38), 0),
	Insn('FORK', 38, 1, [
		Insn('0x9D', Char(254), -11500, 13400, 31000, 4900, 3000),
	]),
	Insn('SOUND_PLAY', 854, 0, 0, 100),
	Insn('FORK_AWAIT', Char(38), 1),
	Insn('EFF_PLAY', (ResId(0), -1), Char(38), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('CHAR_SET_FRAME', Char(38), 1),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(38), 0),
	Insn('FORK', 38, 1, [
		Insn('0x9D', Char(254), -21500, 13400, 31000, 1500, 3000),
	]),
	Insn('SOUND_PLAY', 854, 0, 0, 100),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(38), 1),
	Insn('FLAG_SET', Flag(738)),
	Insn('NEW_SCENE', 'c1100', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][54] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (22000, 2000, 20100), 0),
	Insn('CAM_ROTATE', 45, 30, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 20000, 0),
	Insn('CHAR_SET_POS', Char(257), (18600, 0, 12400), 0),
	Insn('CHAR_SET_POS', Char(258), (19600, 0, 12400), 0),
	Insn('CHAR_SET_POS', Char(259), (18600, 0, 11000), 0),
	Insn('CHAR_SET_POS', Char(260), (19600, 0, 11000), 0),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_POS', Char(33), (19100, 0, 16600), 0),
	Insn('CAM_ROTATE', 30, 30, 0, 5000),
	Insn('CAM_DISTANCE', 17000, 5000),
	Insn('0x6F', b'y'),
	Insn('SLEEP', 500),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (19100, 1100, 13600), 0),
	Insn('CAM_ROTATE', 45, 19, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 21500, 0),
	Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200058V#12P#0013F这是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200059V#12P#0201F是袭击的痕迹吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200060V#0303F似乎正是之前说过的那个\n'
		'重型机关枪的弹痕呢……{wait}'
		'{page}'
		'#14200061V#0301F至少没有使用炸弹，\n'
		'真是谢天谢地了啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4B', Char(33), -1),
	Insn('EMOTE', Char(33), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(33), 180, 500),
	Insn('TEXT_TALK', Char(33), Text(
		'#14502F#14200062V#5P呀，这不是罗伊德和各位嘛！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (19100, 1100, 14000), 1200),
	Insn('FORK', 33, 1, [
		Insn('0x95', Char(254), (19100, 0, 14800), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(33), 1),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200063V#12P#0001F弗兰兹……\n'
		'现在什么状况？{wait}'
		'{page}'
		'#14200064V我们刚刚得知了情况，\n'
		'就匆忙赶过来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(33), Text(
		'#14501F#14200065V#5P我也不太清楚呢。{wait}'
		'{page}'
		'#14503F#14200066V#5P只知道在昨天半夜，\n'
		'似乎发生了枪击事件呢。{wait}'
		'{page}'
		'#14501F#14200067V#5P达德利警官他们现在\n'
		'正在进行案情询问。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 30),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200068V#0106F果然又被一课\n'
		'捷足先登了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200069V#12P#0206F行动果然迅速。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200070V#12P#0003F我们也希望从『黑月』\n'
		'那里探听一些情报……{wait}'
		'{page}'
		'#14200071V#0000F能让我们进去吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(33), Text(
		'#14505F#14200072V#5P嗯，好吧……{wait}'
		'{page}'
		'#14503F#14200073V#5P因为长官只是吩咐我说，\n'
		'不要让一般市民进来。{wait}'
		'{page}'
		'#14501F#14200074V#5P不过，达德利警官那边，\n'
		'你们可得想办法敷衍过去哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200075V#12P#0002F没问题，多谢了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (19100, 0, 13000), 0),
	Insn('0x4C', Char(33), -1),
	Insn('CHAR_SET_POS', Char(33), (20500, 0, 15200), 180),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('FLAG_SET', Flag(1555)),
	Insn('QUEST', 75, Insn('TASK_SET', 1)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][55] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (22000, 0, 21000), 0),
	Insn('CAM_ROTATE', 45, 18, 0, 0),
	Insn('0x6E', 560, 0),
	Insn('CAM_DISTANCE', 24500, 0),
	Insn('CHAR_SET_POS', Char(257), (19100, 350, 21500), 180),
	Insn('CHAR_SET_POS', Char(258), (19100, 350, 21500), 180),
	Insn('CHAR_SET_POS', Char(259), (19100, 350, 21500), 180),
	Insn('CHAR_SET_POS', Char(260), (19100, 350, 21500), 180),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_SET', Char(19), 128),
	Insn('CHAR_FLAG2_SET', Char(19), 32768),
	Insn('CHAR_FLAG1_SET', Char(21), 128),
	Insn('CHAR_FLAG2_SET', Char(21), 32768),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(33), 128),
	Insn('CHAR_FLAG2_UNSET', Char(33), 32768),
	Insn('CHAR_SET_POS', Char(33), (20500, 0, 15200), 180),
	Insn('CHAR_FLAG1_SET', Char(34), 128),
	Insn('CHAR_FLAG2_SET', Char(34), 32768),
	Insn('CHAR_FLAG1_SET', Char(35), 128),
	Insn('CHAR_FLAG2_SET', Char(35), 32768),
	Insn('CAM_DISTANCE', 22500, 4000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('SLEEP', 1000),
	Insn('SOUND_PLAY', 103, 0, 0, 100),
	Insn('OBJ_FLAG_UNSET', Object(4), 16),
	Insn('0x71', Object(4), b'\x00\x00', 5, 0),
	Insn('0x79', b'\x04\x00'),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (19100, 0, 8500), 2000, 0),
	]),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 650),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (19100, 0, 8500), 2000, 0),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 650),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (19100, 0, 8500), 2000, 0),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 650),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (19100, 0, 8500), 2000, 0),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 1000),
	Insn('SOUND_PLAY', 104, 0, 0, 100),
	Insn('0x71', Object(4), b'\x05\x00', 0, 0),
	Insn('0x4B', Char(257), -1),
	Insn('0x4B', Char(258), -1),
	Insn('0x4B', Char(259), -1),
	Insn('0x4B', Char(260), -1),
	Insn('FORK', 257, 3, [
		Insn('CHAR_WATCH', Char(254), Char(33), 500),
	]),
	Insn('FORK', 258, 3, [
		Insn('CHAR_WATCH', Char(254), Char(33), 500),
	]),
	Insn('FORK', 259, 3, [
		Insn('CHAR_WATCH', Char(254), Char(33), 500),
	]),
	Insn('FORK', 260, 3, [
		Insn('CHAR_WATCH', Char(254), Char(33), 500),
	]),
	Insn('SLEEP', 100),
	Insn('0x4B', Char(33), -1),
	Insn('CHAR_WATCH', Char(33), Char(257), 500),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE', Char(33), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(33)),
	Insn('FORK_LOOP', 33, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK', 257, 3, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK', 258, 3, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK', 259, 3, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK', 260, 3, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x4C', Char(257), -1),
	Insn('0x4C', Char(258), -1),
	Insn('0x4C', Char(259), -1),
	Insn('0x4C', Char(260), -1),
	Insn('0x79', b'\x04\x00'),
	Insn('OBJ_FLAG_SET', Object(4), 16),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (21100, 1000, 1800), 0),
	Insn('CAM_ROTATE', 55, 21, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 16500, 0),
	Insn('FORK_QUIT', Char(33), 2),
	Insn('0x4C', Char(33), -1),
	Insn('CHAR_SET_POS', Char(33), (20500, 0, 15200), 180),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(259), 1),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('CHAR_SET_POS', Char(257), (21100, 0, 3800), 180),
	Insn('CHAR_SET_POS', Char(258), (21600, 0, 5300), 180),
	Insn('CHAR_SET_POS', Char(259), (20600, 0, 4800), 180),
	Insn('CHAR_SET_POS', Char(260), (21100, 0, 6500), 180),
	Insn('CAM_OFFSET', (21100, 1000, -2200), 4000),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (21100, 0, -3200), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (22100, 0, -1800), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (20100, 0, -2200), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (21100, 0, -900), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'\x11'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200231V#12P#0006F……真是服了他们。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200232V#5P#0106F是啊，虽然很感谢他\n'
		'能告诉我们这么多……{wait}'
		'{page}'
		'#14200233V#0101F但真没想到，竟会那么露骨地暗示\n'
		'他们准备认真开战啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200234V#0303F#5P再这样下去，\n'
		'真有可能会演变为惨烈的血战呢。{wait}'
		'{page}'
		'#14200235V#0301F搞不好的话，下次就有可能直接在市中心开战了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200236V#6P#0206F而且，还有从『黑月』总部\n'
		'派来增援的可能性……{wait}'
		'{page}'
		'#14200237V#0211F火药味真是相当浓烈啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200238V#12P#0003F……不过，既然曹先生那样说，\n'
		'他们目前应该也还有些犹豫吧。{wait}'
		'{page}'
		'#14200239V#0013F总而言之，关于鲁巴彻\n'
		'这次的袭击，疑点实在是太多了。{wait}'
		'{page}'
		'#14200240V在黑月发起正式反击之前，\n'
		'我们还是努力多调查一下为好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200241V#5P#0101F嗯，是啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200242V#6P#0205F也就是说，今天也\n'
		'要去各处打探吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200243V#12P#0003F不……{wait}'
		'{page}'
		'#14200244V#0000F──在如今这种情况下，\n'
		'还是直接去鲁巴彻一趟吧？{wait}'
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
	Insn('TEXT_TALK', Char(260), Text(
		'#14200245V#0305F#5P你认真的吗……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200246V#5P#0106F虽、虽然以前也\n'
		'曾去拜访过……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200247V#6P#0201F但是毕竟发生过那起拍卖会事件，\n'
		'直接过去的话，终究还是太过鲁莽了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200248V#12P#0006F……嗯。\n'
		'所谓的和解，也仅限于琪雅\n'
		'那一件事情而已。{wait}'
		'{page}'
		'#14200249V#0008F只是，有件事情，\n'
		'我实在是非常在意……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200250V#6P#0205F非常在意的事是指……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200251V#12P#0001F加尔西亚的动向。{wait}'
		'{page}'
		'#14200252V交手的这几次看起来，\n'
		'那个人绝不是愚蠢无谋之辈。{wait}'
		'{page}'
		'#14200253V而且，他还给人一种很能服众，\n'
		'统率能力极强的感觉。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200254V#0303F#5P的确，因为他原本就是\n'
		'一个有名猎兵团的部队长呢。{wait}'
		'{page}'
		'#14200255V#0301F从常理来说，这种人绝不会\n'
		'轻易发动毫无意义的袭击……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200256V#5P#0103F昨晚那场袭击，到底是他的指示，\n'
		'还是他的手下擅自妄为呢……{wait}'
		'{page}'
		'#14200257V#0101F这个问题的确很令人在意呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200258V#12P#0000F对吧？{wait}'
		'{page}'
		'#14200259V哪怕只是在鲁巴彻商会\n'
		'的附近打听一下情况也好。{wait}'
		'{page}'
		'#14200260V我们现在就去看看，如何？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200261V#5P#0102F唉……真拿你没办法啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200262V#6P#0202F算了，如果只是在附近打探一下，\n'
		'应该也不会有什么危险吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200263V#0302F#5P好，那我们就去看看吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 16750, 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(0), (21100, 0, -2500), 180),
	Insn('FLAG_SET', Flag(1556)),
	Insn('QUEST', 75, Insn('TASK_SET', 2)),
	Insn('0x66', 0, 1),
	Insn('OBJ_FLAG_UNSET', Object(4), 16),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG2_UNSET', Char(11), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(19), 128),
	Insn('CHAR_FLAG2_UNSET', Char(19), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(21), 128),
	Insn('CHAR_FLAG2_UNSET', Char(21), 32768),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][56] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (18120, 2300, 5600), 0),
	Insn('CAM_ROTATE', 45, 20, 0, 0),
	Insn('0x6E', 580, 0),
	Insn('CAM_DISTANCE', 14010, 0),
	Insn('CHAR_SET_POS', Char(8), (19940, 0, 9410), 180),
	Insn('CHAR_SET_POS', Char(257), (19200, 0, 7270), 0),
	Insn('CHAR_SET_POS', Char(258), (20640, 0, 7470), 0),
	Insn('CHAR_SET_POS', Char(259), (19150, 0, 5850), 0),
	Insn('CHAR_SET_POS', Char(260), (20640, 0, 6050), 0),
	Insn('CHAR_FLAG1_SET', Char(31), 128),
	Insn('CHAR_FLAG2_SET', Char(31), 32768),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F那个，不好意思。\n'
		'请问您在这附近\n'
		'捡到过什么失物吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P哎呀，我是捡到过类似失物的东西呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P我之前发现公园边上的\n'
		'草丛里挂着一个东西，\n'
		'于是就捡了起来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P当时好像都快要被风吹走了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(0), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(1), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(2), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(3), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F快要被风吹走……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F#12P这么一说，\n'
		'委托人当时好像也曾说过，\n'
		'已经忘记最后一件遗失物是什么了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F#11P到底会是什么呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#5P你们正在找它吗？\n'
		'那就交给你们吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'拿到了{item 825}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 825, 1),
	Insn('TEXT_TALK', Char(260), Text(
		'#11P#0305F原来是导力列车的车票啊……{wait}'
		'{page}'
		'#0306F话说，要是没有这个的话，\n'
		'他就无法回国了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 823, 0)), Insn('EXEC', Insn('ITEM_GET', 824, 0)), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 825, 0)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0003F不、不管怎么说，\n'
				'这样一来，总算全部找到了啊。{wait}'
				'{page}'
				'#0000F立刻去向特伦特先生汇报吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F#11P嗯，去把这些失物还给他吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0003F……稍后就把失物交还给他吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(0), (20110, 0, 7370), 225),
	Insn('0x4C', Char(8), -1),
	Insn('CHAR_FLAG1_UNSET', Char(31), 128),
	Insn('CHAR_FLAG2_UNSET', Char(31), 32768),
	Insn('QUEST', 2, Insn('TASK_SET', 4)),
	Insn('FLAG_SET', Flag(17)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 2, Insn('TASK_GET', 1))), Insn('EXEC', Insn('QUEST_GET', 2, Insn('TASK_GET', 2))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 2, Insn('TASK_GET', 4))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 2, Insn('TASK_SET', 31)),
		]),
		(None, []),
	]),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][57] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}前往『米修拉姆』的水上巴士丄时刻表\n'
		'※米修拉姆引以为豪的主题乐园\n'
		' 『奇幻乐园』开园中！\n'
		' 请尽情享受欢乐时光！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][58] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}『羽扇河丄第一灯塔』\n'
		'\n'
		'\u3000无关人员禁止进入。\n'
		'\u3000\u3000～克洛斯贝尔市～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][59] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 20))), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('0x4B', Char(254), -1),
			Insn('0x4B', Char(12), -1),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CAM_OFFSET', (40190, 840, -17820), 0),
			Insn('CAM_ROTATE', 50, 4, 0, 0),
			Insn('0x6E', 600, 0),
			Insn('CAM_DISTANCE', 16000, 0),
			Insn('CHAR_SET_POS', Char(257), (41420, -2500, -19430), 270),
			Insn('CHAR_SET_POS', Char(258), (37720, -2500, -17500), 135),
			Insn('CHAR_SET_POS', Char(259), (39620, -2500, -17390), 187),
			Insn('CHAR_SET_POS', Char(260), (40930, -2500, -18040), 208),
			Insn('CHAR_WATCH', Char(12), Char(258), 0),
			Insn('FORK_FUNC', Char(258), 3, Function((0, 60))),
			Insn('CAM_OFFSET', (40190, -840, -17820), 2000),
			Insn('CAM_DISTANCE', 15000, 2000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(254), Text(
				'穿白袍的医生\n'
				'和穿蓝色衣服的少年？\n'
				'嗯，我刚刚的确有看到。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_QUIT', Char(258), 3),
			Insn('EMOTE', Char(0), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('EMOTE', Char(1), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('EMOTE', Char(2), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('EMOTE', Char(3), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 500),
			Insn('CHAR_ROTATE', Char(12), 135, 500),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(254), Text(
				'看起来像是要掩人耳目一样，\n'
				'医生似乎拿了个东西给少年。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_WATCH', Char(12), Char(258), 500),
			Insn('FORK_FUNC', Char(258), 3, Function((0, 60))),
			Insn('TEXT_TALK', Char(254), Text(
				'白白的……像是药的东西。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F药……该不会是\n'
				'违法的东西吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0301F但如果以医生的身分，\n'
				'应该想要什么都能拿到手……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_QUIT', Char(258), 3),
			Insn('TEXT_TALK', Char(258), Text(
				'#0101F那他们两人之后呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 12, 2, [
				Insn('CHAR_WATCH', Char(254), Char(11), 800),
			]),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，他们稍微打个招呼之后\n'
				'就各走各的了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'去了哪里我就不清楚了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_AWAIT', Char(12), 2),
			Insn('0x4C', Char(254), -1),
			Insn('0x4C', Char(12), -1),
			Insn('CAM_OFFSET', (38720, 0, -13800), 7000),
			Insn('CAM_ROTATE', 56, 17, 0, 5000),
			Insn('0x6E', 600, 4000),
			Insn('CAM_DISTANCE', 17000, 7000),
			Insn('FORK', 257, 1, [
				Insn('0x95', Char(254), (38570, -2500, -12330), 2000, 0),
			]),
			Insn('SLEEP', 500),
			Insn('FORK', 258, 1, [
				Insn('0x95', Char(254), (39770, -2500, -12330), 2000, 0),
			]),
			Insn('SLEEP', 500),
			Insn('FORK', 260, 1, [
				Insn('0x95', Char(254), (39770, -2500, -13530), 2000, 0),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 259, 1, [
				Insn('0x95', Char(254), (38570, -2500, -13530), 2000, 0),
			]),
			Insn('FORK_AWAIT', Char(257), 1),
			Insn('FORK', 257, 2, [
				Insn('CHAR_WATCH', Char(254), Char(260), 500),
			]),
			Insn('FORK_AWAIT', Char(258), 1),
			Insn('FORK', 258, 2, [
				Insn('CHAR_WATCH', Char(254), Char(259), 500),
			]),
			Insn('FORK_AWAIT', Char(260), 1),
			Insn('FORK', 259, 2, [
				Insn('CHAR_WATCH', Char(254), Char(258), 500),
			]),
			Insn('FORK_AWAIT', Char(259), 1),
			Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
			Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
			Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
			Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
			Insn('SLEEP', 1500),
			Insn('EMOTE_STOP', Char(257)),
			Insn('EMOTE_STOP', Char(258)),
			Insn('EMOTE_STOP', Char(259)),
			Insn('EMOTE_STOP', Char(260)),
			Insn('SLEEP', 300),
			Insn('FORK_AWAIT', Char(259), 2),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0206F寻找亚苏拉主任的线索\n'
				'又断掉了呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0306F就像沉入海底的船一样\n'
				'消失得无影无踪呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0101F看来……只能直接去\n'
				'找圣约帮的人问问看了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F嗯，我们走吧！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_POS', Char(0), (39170, -2500, -12330), 0),
			Insn('EVENT_END', 5),
			Insn('QUEST', 56, Insn('TASK_SET', 20)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'穿白袍的医生\n'
				'和穿蓝色衣服的少年？\n'
				'嗯，我刚刚的确有看到。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'他们稍微打个招呼之后\n'
				'就各走各的了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'去了哪里我就不清楚了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][60] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('EMOTE', Char(12), 0, 1700, (38, 38, 250, 1)),
		Insn('SLEEP', 800),
		Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
		Insn('SLEEP', 500),
		Insn('EMOTE', Char(12), 0, 1700, (38, 38, 250, 1)),
		Insn('SLEEP', 600),
		Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
		Insn('SLEEP', 1200),
	]),
	Insn('RETURN'),
]
