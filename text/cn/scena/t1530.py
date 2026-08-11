# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't1530',
	'name2': 't1530',
	'location': 79,
	'bgm': 123,
	'flags': 8192,
	'includes': [
		't1530',
		't1530_1',
		't1500_1',
		None,
		None,
		None,
	],
	'name3': 't1530',
	'labels': [],
	'chcp': [
		'chr/ch05300',
		'chr/ch28200',
		'chr/ch28000',
		'chr/ch29700',
		'chr/ch21002',
		'chr/ch20002',
		'chr/ch20402',
		'chr/ch20302',
		'chr/ch22300',
		'chr/ch29202',
		'chr/ch29500',
		'chr/ch32702',
		'chr/ch32800',
		'chr/ch07100',
		'chr/ch29300',
		'chr/ch32900',
		'chr/ch29200',
		'chr/ch32700',
		'chr/ch29400',
		'chr/ch21602',
		'chr/ch20600',
		'chr/ch22702',
		'chr/ch21802',
		'chr/ch23702',
		'chr/ch23602',
		'chr/ch21902',
		'chr/ch22202',
		'chr/ch20502',
		'chr/ch22802',
		'chr/ch20102',
		'chr/ch21600',
		'chr/ch24402',
		'chr/ch24502',
		'chr/ch32200',
		'chr/ch21102',
		'chr/ch20602',
		'chr/ch20802',
		'chr/ch21502',
		'chr/ch21702',
		'apl/ch50146',
		'chr/ch05600',
		'apl/ch50385',
		'chr/ch24400',
		'chr/ch32000',
		'chr/ch32100',
	],
	'npcs': [
		{
			'name': Translate('接待小姐榭拉'),
			'pos': (17209, 0, 7429),
			'angle': 266,
			'_1': b'\x05\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((1, 1)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('克拉克事务长'),
			'pos': (19739, 0, 4889),
			'angle': 180,
			'_1': b'\x05\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((1, 3)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('护理师兰恩'),
			'pos': (10539, 0, -4489),
			'angle': 325,
			'_1': b'\x05\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((1, 4)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('拉格教授'),
			'pos': (55650, 0, 500),
			'angle': 180,
			'_1': b'\x95\x01\x00\x00\x10\x00\x00\x00',
			'function': Function((1, 6)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('拉格教授'),
			'pos': (50979, 119, 59069),
			'angle': 300,
			'_1': b'\xd5\x01\x00\x00\t\x00\xff\xff',
			'function': Function((1, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('实习医生古恩'),
			'pos': (58849, 0, 58389),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\n\x00\x00\x00',
			'function': Function((1, 8)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('凯瑞教授'),
			'pos': (55650, 0, -620),
			'angle': 0,
			'_1': b'\x95\x01\x00\x00\x11\x00\x00\x00',
			'function': Function((1, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('凯瑞教授'),
			'pos': (49930, 119, -59340),
			'angle': 260,
			'_1': b'\xd5\x01\x00\x00\x0b\x00\xff\xff',
			'function': Function((1, 10)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('实习医生夏鲁鲁'),
			'pos': (60270, 0, -56930),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x0c\x00\x00\x00',
			'function': Function((1, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('约亚西姆副教授'),
			'pos': (17180, 0, -4079),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\r\x00\x00\x00',
			'function': Function((1, 14)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('诊断医生贝尔达因'),
			'pos': (17180, 0, -5289),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x0e\x00\x00\x00',
			'function': Function((1, 15)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('亚苏拉主任'),
			'pos': (56430, 0, -55270),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x0f\x00\x00\x00',
			'function': Function((1, 17)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('亚苏拉主任'),
			'pos': (56889, 800, -58250),
			'angle': 0,
			'_1': b"\xd5\x01\x00\x00'\x00\xff\xff",
			'function': Function((1, 18)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('实习医生利顿'),
			'pos': (53970, 0, 51840),
			'angle': 135,
			'_1': b'\x85\x01\x00\x00\x12\x00\x00\x00',
			'function': Function((1, 19)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('亚米萨'),
			'pos': (16049, 100, -6989),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00%\x00\xff\xff',
			'function': Function((1, 20)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('迪塔总裁'),
			'pos': (14470, 0, 7309),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00(\x00\x00\x00',
			'function': Function((1, 24)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('琴兹'),
			'pos': (14470, 0, 7309),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00)\x00\x00\x00',
			'function': Function((1, 25)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (18850, 119, -3970),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x04\x00\xff\xff',
			'function': Function((1, 27)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (16559, 119, -9979),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x05\x00\xff\xff',
			'function': Function((1, 28)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (8340, 119, 9890),
			'angle': 180,
			'_1': b'\xd5\x01\x00\x00\x06\x00\xff\xff',
			'function': Function((1, 29)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (5000, 119, 4530),
			'angle': 90,
			'_1': b'\xd5\x01\x00\x00\x07\x00\xff\xff',
			'function': Function((1, 30)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (18850, 119, -3970),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x13\x00\xff\xff',
			'function': Function((1, 31)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (21840, 119, -7219),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x06\x00\xff\xff',
			'function': Function((1, 32)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (5099, 119, 4739),
			'angle': 90,
			'_1': b'\xd5\x01\x00\x00\x07\x00\xff\xff',
			'function': Function((1, 33)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (21840, 119, -4429),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x15\x00\xff\xff',
			'function': Function((1, 34)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (16799, 119, -6889),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x16\x00\xff\xff',
			'function': Function((1, 35)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (7400, 119, 6849),
			'angle': 180,
			'_1': b'\xd5\x01\x00\x00\x17\x00\xff\xff',
			'function': Function((1, 36)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (2000, 119, 7880),
			'angle': 90,
			'_1': b'\xd5\x01\x00\x00\x18\x00\xff\xff',
			'function': Function((1, 37)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (18850, 119, -3970),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x13\x00\xff\xff',
			'function': Function((1, 38)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (19729, 119, -9960),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x05\x00\xff\xff',
			'function': Function((1, 39)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (5110, 119, 5170),
			'angle': 90,
			'_1': b'\xd5\x01\x00\x00\x19\x00\xff\xff',
			'function': Function((1, 40)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (5110, 119, 4329),
			'angle': 90,
			'_1': b'\xd5\x01\x00\x00\x1a\x00\xff\xff',
			'function': Function((1, 41)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (18850, 119, -3970),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x04\x00\xff\xff',
			'function': Function((1, 42)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (18850, 119, -5050),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x1b\x00\xff\xff',
			'function': Function((1, 43)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (7750, 119, 9800),
			'angle': 180,
			'_1': b'\xd5\x01\x00\x00\x1c\x00\xff\xff',
			'function': Function((1, 44)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (16809, 119, -6920),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x06\x00\xff\xff',
			'function': Function((1, 45)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (21840, 119, -8199),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x05\x00\xff\xff',
			'function': Function((1, 46)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (21840, 119, -7449),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x1d\x00\xff\xff',
			'function': Function((1, 47)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (18850, 119, -4309),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x1f\x00\xff\xff',
			'function': Function((1, 48)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (18850, 119, -5219),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00 \x00\xff\xff',
			'function': Function((1, 49)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (7519, 119, 6840),
			'angle': 180,
			'_1': b'\xd5\x01\x00\x00\x13\x00\xff\xff',
			'function': Function((1, 50)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (21829, 119, -3789),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x13\x00\xff\xff',
			'function': Function((1, 51)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (21829, 119, -4869),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00"\x00\xff\xff',
			'function': Function((1, 52)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (4989, 119, 5469),
			'angle': 90,
			'_1': b'\xd5\x01\x00\x00\x05\x00\xff\xff',
			'function': Function((1, 54)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (4989, 119, 4360),
			'angle': 90,
			'_1': b'\xd5\x01\x00\x00\x07\x00\xff\xff',
			'function': Function((1, 55)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (18819, 119, -4750),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00#\x00\xff\xff',
			'function': Function((1, 56)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (19659, 119, -9970),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x1c\x00\xff\xff',
			'function': Function((1, 57)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (7349, 119, 6849),
			'angle': 180,
			'_1': b'\xd5\x01\x00\x00\x19\x00\xff\xff',
			'function': Function((1, 58)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (2000, 119, 4139),
			'angle': 90,
			'_1': b'\xd5\x01\x00\x00$\x00\xff\xff',
			'function': Function((1, 59)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (2000, 119, 7510),
			'angle': 90,
			'_1': b'\xd5\x01\x00\x00\x04\x00\xff\xff',
			'function': Function((1, 60)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (18909, 119, -4409),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00"\x00\xff\xff',
			'function': Function((1, 61)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (18909, 119, -5349),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00%\x00\xff\xff',
			'function': Function((1, 62)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (16049, 119, -6989),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x06\x00\xff\xff',
			'function': Function((1, 63)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (21829, 119, -4110),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00 \x00\xff\xff',
			'function': Function((1, 64)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (8069, 119, 9880),
			'angle': 180,
			'_1': b'\xd5\x01\x00\x00\x13\x00\xff\xff',
			'function': Function((1, 65)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('门诊患者'),
			'pos': (5099, 119, 4739),
			'angle': 90,
			'_1': b'\xd5\x01\x00\x00&\x00\xff\xff',
			'function': Function((1, 66)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('女孩'),
			'pos': (7250, 0, -7599),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x08\x00\x00\x00',
			'function': Function((1, 67)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('男孩'),
			'pos': (7400, 0, 3740),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x14\x00\x00\x00',
			'function': Function((1, 68)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (18930, 0, 2579),
			'angle': 15,
			'_1': b'\x85\x01\x00\x00\x1e\x00\x00\x00',
			'function': Function((1, 69)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (2000, 0, -7670),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00!\x00\x00\x00',
			'function': Function((1, 70)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('赛西儿'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((1, 22)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('米修'),
			'pos': (11579, 0, 5699),
			'angle': 225,
			'_1': b'\x85\x01\x00\x00*\x00\x00\x04',
			'function': Function((1, 71)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游击士林'),
			'pos': (22700, 0, 1799),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00+\x00\x00\x00',
			'function': Function((1, 72)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游击士艾欧莉雅'),
			'pos': (49849, 0, 58180),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00,\x00\x00\x00',
			'function': Function((1, 73)),
			'_2': b'\xff\x00\x00\x00',
		},
	],
	'monsters': [],
	'triggers': [
		{
			'pos': (12.0, 12.0, -0.5),
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
				-6.0,
				-6.0,
				0.10000000149011612,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (24.93000030517578, 0.1899999976158142, -0.0),
			'range': 20.25,
			'transform': [
				0.23570220172405243,
				0.23570235073566437,
				-0.0,
				0.0,
				-0.23570235073566437,
				0.23570220172405243,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.3333333432674408,
				0.0,
				-5.831272602081299,
				-5.920843124389648,
				0.0,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 16)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (16000, 0, 7000),
			'range': 2000,
			'bubble_pos': (17210, 1500, 7430),
			'_1': b'~\x00\x01',
			'function': Function((0, 0)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (19680, 0, 3710),
			'range': 2000,
			'bubble_pos': (19740, 1500, 4890),
			'_1': b'~\x00\x01',
			'function': Function((0, 2)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (65800, 0, 2430),
			'range': 1200,
			'bubble_pos': (65800, 1500, 2430),
			'_1': b'|\x00\x00',
			'function': Function((0, 17)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00O\x00', Function((0, 5)), Function((0, 7))),
	'code': [None]*18,
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
		Insn('CHAR_ANIMATION', Char(254), 1200, []),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('0x95', Char(254), (7400, 0, -1600), 1500, 0),
		Insn('0x95', Char(254), (7400, 0, 1420), 1500, 0),
		Insn('0x95', Char(254), (10380, 0, 4530), 1500, 0),
		Insn('0x95', Char(254), (13330, 0, 4550), 1500, 0),
		Insn('0x95', Char(254), (16420, 0, 1470), 1500, 0),
		Insn('0x95', Char(254), (16420, 0, -1430), 1500, 0),
		Insn('0x95', Char(254), (13440, 0, -4490), 1500, 0),
		Insn('0x95', Char(254), (10540, 0, -4490), 1500, 0),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (6450, 5260), (7610, 3530), 1000),
		Insn('SLEEP', 400),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (9940, 3020), (13550, 9050), 1000),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 102), Insn('EQ'), Insn('FLAG', Flag(761)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(761)),
			Insn('CALL', Function((0, 6))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(10), (16050, 0, -5480), 180),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
			Insn('CHAR_SET_POS', Char(21), (56790, 0, 5200), 180),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_SET_POS', Char(16), (57420, 0, -56730), 180),
			Insn('CHAR_FLAG1_UNSET', Char(20), 128),
			Insn('CHAR_FLAG1_UNSET', Char(60), 128),
			Insn('CHAR_FLAG1_UNSET', Char(61), 128),
			Insn('CHAR_FLAG1_UNSET', Char(62), 128),
			Insn('CHAR_FLAG1_UNSET', Char(63), 128),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(10), (59030, 0, -1090), 90),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('CHAR_FLAG1_UNSET', Char(57), 128),
			Insn('CHAR_FLAG1_UNSET', Char(58), 128),
			Insn('CHAR_FLAG1_UNSET', Char(59), 128),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('FORK_FUNC', Char(10), 0, Function((0, 2))),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('CHAR_FLAG1_UNSET', Char(57), 128),
			Insn('CHAR_FLAG1_UNSET', Char(58), 128),
			Insn('CHAR_FLAG1_UNSET', Char(59), 128),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(10), (17630, 0, -4730), 90),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
			Insn('CHAR_SET_POS', Char(21), (6660, 0, -5660), 90),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('CHAR_FLAG1_UNSET', Char(53), 128),
			Insn('CHAR_FLAG1_UNSET', Char(54), 128),
			Insn('CHAR_FLAG1_UNSET', Char(55), 128),
			Insn('CHAR_FLAG1_UNSET', Char(56), 128),
			Insn('CHAR_FLAG1_UNSET', Char(69), 128),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('FORK_FUNC', Char(10), 0, Function((0, 2))),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
			Insn('CHAR_SET_POS', Char(21), (6660, 0, -5660), 90),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(24), 128),
			Insn('CHAR_FLAG1_UNSET', Char(49), 128),
			Insn('CHAR_FLAG1_UNSET', Char(50), 128),
			Insn('CHAR_FLAG1_UNSET', Char(51), 128),
			Insn('CHAR_FLAG1_UNSET', Char(52), 128),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('FORK_FUNC', Char(10), 0, Function((0, 2))),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
			Insn('CHAR_SET_POS', Char(21), (6660, 0, -5660), 90),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(49), 128),
			Insn('CHAR_FLAG1_UNSET', Char(50), 128),
			Insn('CHAR_FLAG1_UNSET', Char(51), 128),
			Insn('CHAR_FLAG1_UNSET', Char(52), 128),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('FORK_FUNC', Char(10), 0, Function((0, 2))),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_SET_POS', Char(13), (51570, 0, 57430), 90),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
			Insn('CHAR_SET_POS', Char(21), (49240, 0, 59850), 0),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_SET_POS', Char(16), (48750, 0, -59740), 180),
			Insn('CHAR_FLAG1_UNSET', Char(46), 128),
			Insn('CHAR_FLAG1_UNSET', Char(47), 128),
			Insn('CHAR_FLAG1_UNSET', Char(48), 128),
			Insn('CHAR_FLAG1_UNSET', Char(67), 128),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_SET_POS', Char(13), (56790, 0, 5200), 180),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_SET_POS', Char(16), (54470, 0, -4240), 0),
			Insn('CHAR_FLAG1_UNSET', Char(68), 128),
			Insn('CHAR_SET_POS', Char(68), (8160, 0, 400), 180),
			Insn('CHAR_SET_POS', Char(10), (8160, 0, -630), 0),
			Insn('CHAR_FLAG1_UNSET', Char(43), 128),
			Insn('CHAR_FLAG1_UNSET', Char(44), 128),
			Insn('CHAR_FLAG1_UNSET', Char(45), 128),
			Insn('CHAR_FLAG1_UNSET', Char(66), 128),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('FORK_FUNC', Char(10), 0, Function((0, 2))),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('FORK_FUNC', Char(19), 0, Function((0, 1))),
			Insn('CHAR_FLAG1_UNSET', Char(23), 128),
			Insn('CHAR_FLAG1_UNSET', Char(40), 128),
			Insn('CHAR_FLAG1_UNSET', Char(41), 128),
			Insn('CHAR_FLAG1_UNSET', Char(42), 128),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('FORK_FUNC', Char(10), 0, Function((0, 2))),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('FORK_FUNC', Char(19), 0, Function((0, 1))),
			Insn('CHAR_FLAG1_UNSET', Char(22), 128),
			Insn('CHAR_FLAG1_UNSET', Char(36), 128),
			Insn('CHAR_FLAG1_UNSET', Char(37), 128),
			Insn('CHAR_FLAG1_UNSET', Char(38), 128),
			Insn('CHAR_FLAG1_UNSET', Char(39), 128),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('FORK_FUNC', Char(10), 0, Function((0, 2))),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(19), 128),
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('END')]), [
							Insn('CHAR_SET_POS', Char(19), (48580, 0, -59600), 90),
						]),
						(None, []),
					]),
				]),
				(None, []),
			]),
			Insn('CHAR_FLAG1_UNSET', Char(32), 128),
			Insn('CHAR_FLAG1_UNSET', Char(33), 128),
			Insn('CHAR_FLAG1_UNSET', Char(34), 128),
			Insn('CHAR_FLAG1_UNSET', Char(35), 128),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('FORK_FUNC', Char(10), 0, Function((0, 2))),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
			Insn('CHAR_FLAG1_UNSET', Char(22), 128),
			Insn('CHAR_SET_POS', Char(21), (16050, 0, -5480), 180),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('CHAR_SET_POS', Char(19), (48580, 0, -59600), 90),
			Insn('CHAR_FLAG1_UNSET', Char(29), 128),
			Insn('CHAR_FLAG1_UNSET', Char(30), 128),
			Insn('CHAR_FLAG1_UNSET', Char(31), 128),
			Insn('CHAR_FLAG1_UNSET', Char(65), 128),
			Insn('FORK_FUNC', Char(65), 0, Function((0, 3))),
			Insn('CHAR_FLAG1_UNSET', Char(70), 128),
			Insn('CHAR_FLAG1_UNSET', Char(71), 128),
			Insn('CHAR_SET_POS', Char(11), (49790, 0, 59830), 180),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('FORK_FUNC', Char(10), 0, Function((0, 2))),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_SET_POS', Char(13), (56870, 0, 2560), 180),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('FORK_FUNC', Char(10), 0, Function((0, 2))),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
			Insn('CHAR_FLAG1_UNSET', Char(27), 128),
			Insn('CHAR_FLAG1_UNSET', Char(28), 128),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(10), (9660, 0, 2050), 0),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(25), 128),
			Insn('CHAR_FLAG1_UNSET', Char(26), 128),
			Insn('CHAR_FLAG1_UNSET', Char(27), 128),
			Insn('CHAR_FLAG1_UNSET', Char(28), 128),
			Insn('CHAR_FLAG1_UNSET', Char(64), 128),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(10), 16),
			Insn('CHAR_SET_POS', Char(10), (17680, 0, -3850), 90),
			Insn('CHAR_FLAG1_UNSET', Char(22), 128),
			Insn('CHAR_FLAG1_UNSET', Char(25), 128),
			Insn('CHAR_FLAG1_UNSET', Char(26), 128),
			Insn('CHAR_FLAG1_UNSET', Char(27), 128),
			Insn('CHAR_FLAG1_UNSET', Char(28), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(782)), Insn('FLAG', Flag(783)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 8))),
			Insn('0x09', 268435456),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('FLAG', Flag(785)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x09', 268435456),
			Insn('EVENT', Function((0, 10))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 12))),
		]),
		(Expr([Insn('FLAG', Flag(737)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(737)),
			Insn('EVENT', Function((1, 77))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('SOUND_PLAY', 160, 0, 0, 100),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('EXPR_CHAR_ATTR', Char(20), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('END')]), [
					Insn('FORK_FUNC', Char(19), 0, Function((0, 0))),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(777)), Insn('FLAG', Flag(784)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x00\x80\x00'),
			Insn('0xB5', b'\x01\x01\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(799)), Insn('FLAG', Flag(800)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xd2\xc8\x00\x00\x00\x00\x00'),
		]),
		(Expr([Insn('FLAG', Flag(1359)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xd2\xc8\x00\x00\x00\x00\x00'),
		]),
		(Expr([Insn('FLAG', Flag(1564)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xd2\xc8\x00\x00\x00\x00\x00'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (20530, 1000, 0), 0),
	Insn('CAM_ROTATE', 45, 28, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 28000, 0),
	Insn('CHAR_SET_POS', Char(257), (2200, 0, -700), 90),
	Insn('CHAR_SET_POS', Char(258), (2200, 0, 600), 90),
	Insn('CHAR_SET_POS', Char(259), (900, 0, -700), 90),
	Insn('CHAR_SET_POS', Char(260), (900, 0, 600), 90),
	Insn('CAM_OFFSET', (4000, 1000, 0), 7000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (2520, 1000, -280), 0),
	Insn('CAM_ROTATE', 45, 25, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 21610, 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101058V#6P#0000F太好了……\n'
		'人好像没有想像中的多呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101059V#0104F#5P是啊……人多的时候，\n'
		'连候诊席都会没有空位。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101060V#0100F#5P快点去接待处\n'
		'问问你姐姐的事吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101061V#12P#0000F是啊，请他们帮忙叫她出来吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (1500, 0, -100), 90),
	Insn('FLAG_SET', Flag(783)),
	Insn('0x0A', 268435456),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('EVENT_BEGIN', 2),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('EVENT_BEGIN', 0),
	Insn('LOAD_CHCP', 'apl/ch50014', 60),
	Insn('LOAD_CHCP', 'apl/ch50102', 61),
	Insn('0x4B', Char(8), -1),
	Insn('CAM_OFFSET', (15690, 600, 7270), 0),
	Insn('CAM_ROTATE', 51, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 23130, 0),
	Insn('CHAR_SET_POS', Char(257), (14410, 0, 6710), 90),
	Insn('CHAR_SET_POS', Char(258), (14130, 0, 5550), 90),
	Insn('CHAR_SET_POS', Char(259), (12820, 0, 5690), 90),
	Insn('CHAR_SET_POS', Char(260), (13070, 0, 6870), 90),
	Insn('CHAR_SET_POS', Char(8), (17210, 0, 7430), 266),
	Insn('CHAR_FLAG1_UNSET', Char(68), 4),
	Insn('CHAR_FLAG1_UNSET', Char(68), 128),
	Insn('0x4B', Char(68), -1),
	Insn('CHAR_SET_POS', Char(68), (12000, 1050, 13300), 180),
	Insn('CHAR_SET_COLOR', Char(68), Color(0x00FFFFFF), 0),
	Insn('CAM_DISTANCE', 22630, 1000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101062V#11P欢迎来到乌尔斯拉医院。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101063V#11P今天是来就诊的吗？\n'
		'还是来探病的？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101064V#0005F#6P啊，不是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_SET', Char(257), 16),
	Insn('CHAR_FLAG1_SET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 60),
	Insn('CHAR_SET_FRAME', Char(257), 3),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101065V#0000F#6P我是克洛斯贝尔警察局丄\n'
		'特务支援课的罗伊德丄班宁斯。{wait}'
		'{page}'
		'#11101066V今天是为了调查案件\n'
		'而来这里的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(8), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101067V#11P啊，原来是警察啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101068V#11P你说是来调查的……\n'
		'莫非是为了之前的魔兽骚乱吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 150),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(257), 16),
	Insn('CHAR_FLAG1_UNSET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101069V#0003F#6P嗯……\n'
		'我们应警备队的请求，\n'
		'来这里进行调查。{wait}'
		'{page}'
		'#11101070V#0001F能让我与\n'
		'相关人员谈谈吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101071V#11P呵呵，我知道了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101072V#11P不过现在院长不在，\n'
		'要我帮你把护理师长叫来吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 3)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101073V#0011F#6P那、那个……其实……{wait}'
		'{page}'
		'#11101074V我有个朋友\n'
		'在这里工作……{wait}'
		'{page}'
		'#11101075V#0012F如果那个人不忙的话，\n'
		'希望能让她为我们带路……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1200),
	Insn('EMOTE_STOP', Char(65535)),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101076V#0202F#6P（总感觉他有点紧张呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(260), Char(259), 500),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101077V#0301F（姐姐是护理师还是个美女，\n'
		'\u3000当然会紧张了！）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(258), Char(260), 500),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101078V#0106F#11P（只有你才会那样吧……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(68), Translate('女性的声音'), Text(
		'#11101079V──罗伊德？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(8), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_FLAG1_SET', Char(27), 128),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(68), 300),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(68), 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(68), 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(68), 300),
	]),
	Insn('FORK', 8, 1, [
		Insn('CHAR_WATCH', Char(254), Char(68), 300),
	]),
	Insn('CAM_OFFSET', (14050, 600, 9110), 3000),
	Insn('CAM_ROTATE', 30, 18, 0, 3000),
	Insn('FORK', 68, 1, [
		Insn('0x95', Char(254), (11970, 0, 10920), 1000, 0),
	]),
	Insn('SLEEP', 200),
	Insn('FORK', 68, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(68), 1),
	Insn('FORK_AWAIT', Char(68), 2),
	Insn('0x6F', b'y'),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK2', Char(68), Translate('女性护理师'), Text(
		'#11101080V#1305F#5P#40W…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101081V#0005F#12P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101082V#0305F#6P哦哦……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101083V#0105F#12P……好漂亮的人啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101084V#0205F#6P……好有魅力……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101085V#2P哎呀，赛西儿。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101086V#2P你来得正好，\n'
		'这些人好像是警察……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (13560, 600, 9860), 1500),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (12960, 0, 8710), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('0x6F', b'y'),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(258), Char(68), 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(259), Char(68), 300),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(260), Char(68), 500),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101087V#0011F#12P那个……那个。{wait}'
		'{page}'
		'#11101088V#0009F抱歉，突然就跑过来了……\n'
		'还是应该先联系你一下比较好吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(68), Text(
		'#11101089V#1301F#5P…………唔………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (13660, 600, 9340), 500),
	Insn('CHAR_FLAG1_SET', Char(68), 64),
	Insn('FORK', 68, 1, [
		Insn('0x95', Char(254), (12750, 0, 9200), 4000, 0),
	]),
	Insn('FORK_AWAIT', Char(68), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('CROSSFADE', 500),
	Insn('FORK', 257, 2, [
		Insn('0xA6', Char(254), 0, 30, 500, 2000),
	]),
	Insn('CAM_DISTANCE', 22130, 0),
	Insn('CHAR_SET_CHCP', Char(68), 61),
	Insn('CHAR_SET_FRAME', Char(68), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('EMOTE', Char(8), 0, 2000, (2, 7, 80, 1)),
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
		'#11101090V#0011F#12P啊，赛西儿姐姐……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(68), Text(
		'#11101091V#1304F#5P#40W终于……终于见到你了。{wait}'
		'{page}'
		'#11101092V欢迎回来……\n'
		'真的好久不见了呢，罗伊德……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101093V#0002F#12P嗯、嗯……{wait}'
		'{page}'
		'#11101094V#0004F抽不出时间来找你，真的很抱歉。\n'
		'最近这段时间一直很忙……{wait}'
		'{page}'
		'#11101095V#0011F比、比起这个，这样抱着\n'
		'让人觉得有些不好意思……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(68), Text(
		'#11101096V#1304F#5P#30W……好了，就这样\n'
		'让姐姐抱一会吧。{wait}'
		'{page}'
		'#11101097V#1302F呵呵……\n'
		'都已经长这么高了……{wait}'
		'{page}'
		'#11101098V之前离开的时候，\n'
		'还只跟我差不多高呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101099V#0012F#12P那、那是当然了，\n'
		'那三年正是身体的成长期嘛……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(8), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1500),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101100V#2P那、那个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101101V#0109F#4P（该、该怎么说呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101102V#0206F#12P（比想像中的还要亲密呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101103V#0307F#6P（可恶的罗伊德……！\n'
		'\u3000竟然有个这么美丽的姐姐……！）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('CAM_DISTANCE', 23130, 3000),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 't1510', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (2200, 1000, -100), 0),
	Insn('CAM_ROTATE', 47, 20, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 24440, 0),
	Insn('CAM_OFFSET', (3670, 1000, 220), 3000),
	Insn('CHAR_SET_POS', Char(310), (1800, 0, -100), 90),
	Insn('CHAR_SET_POS', Char(257), (0, 0, -700), 90),
	Insn('CHAR_SET_POS', Char(258), (0, 0, 600), 90),
	Insn('CHAR_SET_POS', Char(259), (0, 0, -700), 90),
	Insn('CHAR_SET_POS', Char(260), (0, 0, 600), 90),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('FORK', 310, 1, [
		Insn('0x96', Char(254), (4400, 0, -100), 2000, 0),
	]),
	Insn('SLEEP', 600),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (2200, 0, -700), 2000, 0),
	]),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (2200, 0, 600), 2000, 0),
	]),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 1200),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (900, 0, -700), 2000, 0),
	]),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (900, 0, 600), 2000, 0),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('FORK', 310, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101174V#1300F#11P这栋院区的\n'
		'二楼与三楼是病房。{wait}'
		'{page}'
		'#11101175V受害的实习医生\n'
		'在二楼病房，我给你们带路吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101176V#0000F#6P嗯，拜托了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 310, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('CAM_OFFSET', (11450, 1000, 7080), 12000),
	Insn('FORK_FUNC', Char(310), 3, Function((0, 11))),
	Insn('SLEEP', 800),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 11))),
	Insn('SLEEP', 800),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 11))),
	Insn('SLEEP', 800),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 11))),
	Insn('SLEEP', 800),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 11))),
	Insn('SLEEP', 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FLAG_SET', Flag(814)),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 't1540', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (4400, 0, -100), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (11980, 0, 6820), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (11760, 0, 10650), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (12190, 140, 12390), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (17660, 1000, 7870), 0),
	Insn('CAM_ROTATE', 66, 14, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 26750, 0),
	Insn('CHAR_SET_POS', Char(257), (14410, 0, 6710), 45),
	Insn('CHAR_SET_POS', Char(339), (12450, 0, 6560), 45),
	Insn('CHAR_SET_POS', Char(239), (11920, 0, 5340), 45),
	Insn('0x4B', Char(68), -1),
	Insn('CHAR_FLAG1_UNSET', Char(68), 128),
	Insn('CHAR_FLAG2_UNSET', Char(68), 32768),
	Insn('CHAR_SET_POS', Char(68), (13290, 0, 8050), 90),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_SET_POS', Char(8), (20770, 0, 9100), 45),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_DISTANCE', 25000, 2500),
	Insn('0x6F', b'\x10'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600813V#5P……是、是。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600814V#5P知道了，\n'
		'那么我让他们直接去研究室。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(8), Char(257), 500),
	Insn('CAM_OFFSET', (16430, 1000, 7320), 2500),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (17210, 0, 7430), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600815V#5P约亚西姆医生\n'
		'现在刚好有时间。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600816V#5P请直接去\n'
		'研究区里的研究室吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600817V#0004F#6P这样啊……太好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(68), Char(339), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(68), Text(
		'#13600818V#1302F#5P呵呵，那么我\n'
		'就先失陪了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(68), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 239, 1, [
		Insn('CHAR_WATCH', Char(254), Char(68), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 339, 1, [
		Insn('CHAR_WATCH', Char(254), Char(68), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(239), 1),
	Insn('FORK_AWAIT', Char(339), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600819V#0002F#11P嗯，真是多谢了，\n'
		'回去之前，我们会去和你打声招呼的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(68), Text(
		'#13600820V#1302F#5P呵呵，好的。{wait}'
		'{page}'
		'#13600821V#1309F琪雅，待会见了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600822V#1109F#12P嗯！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(68), 0, 500),
	Insn('CAM_OFFSET', (15600, 1000, 9190), 3000),
	Insn('FORK_LOOP', 257, 1, [
		Insn('CHAR_WATCH', Char(257), Char(68), 500),
	]),
	Insn('FORK_LOOP', 239, 1, [
		Insn('CHAR_WATCH', Char(239), Char(68), 500),
	]),
	Insn('FORK_LOOP', 339, 1, [
		Insn('CHAR_WATCH', Char(339), Char(68), 500),
	]),
	Insn('FORK_LOOP', 8, 1, [
		Insn('CHAR_WATCH', Char(8), Char(68), 500),
	]),
	Insn('FORK_FUNC', Char(68), 3, Function((0, 13))),
	Insn('FORK_AWAIT', Char(68), 3),
	Insn('0x6F', b'\x01'),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(239), 1),
	Insn('FORK_QUIT', Char(339), 1),
	Insn('FORK_QUIT', Char(8), 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600823V#0100F还是和以前一样忙呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600824V#0200F依然很忙呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600825V#0300F哈……\n'
				'和以前一样忙呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600826V#11P呵呵，在这所医院里，\n'
		'像赛西儿小姐那样勤劳的人\n'
		'实在是很少呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600827V#11P真希望那些爱偷懒的医生们\n'
		'也都学学她啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600828V#0012F#5P哈哈……{wait}'
		'{page}'
		'#13600829V#0000F（不过我倒不希望\n'
		'\u3000她太过于勉强自己……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(8), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (16430, 1000, 7320), 1500),
	Insn('CHAR_WATCH', Char(8), Char(257), 500),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600830V#5P对了……\n'
		'约亚西姆医生的研究室，\n'
		'各位知道在哪里吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13600831V#5P研究室位于研究区的四楼，\n'
		'需要我给各位带路吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 239, 1, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 339, 1, [
		Insn('CHAR_WATCH', Char(254), Char(8), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(239), 1),
	Insn('FORK_AWAIT', Char(339), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600832V#0002F#6P不用麻烦了，我想我们应该可以找到。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(339), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 239, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 339, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600833V#0000F#5P好，那我们这就去\n'
		'见见那位医生吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600834V#1110F#6P嗯，我们走吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('0x4C', Char(68), -1),
	Insn('CHAR_SET_POS', Char(8), (17210, 0, 7430), 266),
	Insn('0x4C', Char(8), -1),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('CHAR_SET_POS', Char(0), (14000, 0, 6500), 90),
	Insn('FLAG_SET', Flag(1349)),
	Insn('QUEST', 72, Insn('TASK_SET', 7)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (11960, 0, 11140), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (12060, 1030, 13280), 2000, 0),
	]),
	Insn('SLEEP', 250),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('CHAR_FLAG1_SET', Char(254), 128),
	Insn('CHAR_FLAG2_SET', Char(254), 32768),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('EVENT_BEGIN', 0),
	Insn('0x4B', Char(8), -1),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (16430, 800, 7320), 0),
	Insn('CAM_ROTATE', 66, 14, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(257), (14410, 0, 6710), 45),
	Insn('CHAR_SET_POS', Char(258), (12450, 0, 6560), 45),
	Insn('CHAR_SET_POS', Char(259), (11920, 0, 5340), 45),
	Insn('CHAR_SET_POS', Char(260), (13560, 0, 5070), 45),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14200847V#5P哎呀，各位，\n'
		'你们是来找赛西儿的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200848V#0005F#6P啊，不是……{wait}'
		'{page}'
		'#14200849V#0000F其实又是来麻烦约亚西姆\n'
		'医生的，想和他商量点事情。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14200850V#0100F#6P能否帮我们问下，\n'
		'可不可以占用他一点时间？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14200851V#5P嗯，小事一桩。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(8), 45, 500),
	Insn('CAM_OFFSET', (17660, 800, 7870), 3000),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (20770, 0, 9100), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14200852V#5P啊，约亚西姆医生，\n'
		'您在啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14200853V#5P有客人来拜访您，\n'
		'现在有时间吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14200854V#5P哎，现在没空？\n'
		'难道正在进行诊察或者研究吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14200855V#5P──哦，我知道了，\n'
		'您是想去钓鱼吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14200856V#5P不行，现在是上班时间，\n'
		'请认真工作。{wait}'
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
		'#14200857V#0012F#6P（好像还是和以前一样呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14200858V#0211F#6P#N（虽然平时是一个\n'
		'\u3000非常优秀的医生……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14200859V#5P没错，是支援课的\n'
		'罗伊德警官他们。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14200860V#5P……好的，好的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14200861V#5P那么，我就让他们直接\n'
		'去研究室了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('CHAR_ROTATE', Char(8), 225, 500),
	Insn('CAM_OFFSET', (16430, 800, 7320), 2300),
	Insn('FORK', 8, 1, [
		Insn('0x95', Char(254), (17210, 0, 7430), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(8), 1),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14200862V#5P约亚西姆医生\n'
		'说愿意见你们。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14200863V#5P那么，请各位去研究区吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14200864V#0002F#6P谢、谢谢了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14200865V#0309F#12P哈哈，好像\n'
		'给您添麻烦了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_ROTATE', Char(8), 270, 0),
	Insn('0x4C', Char(8), -1),
	Insn('CHAR_SET_POS', Char(0), (14000, 0, 6500), 90),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('FLAG_SET', Flag(1563)),
	Insn('QUEST', 76, Insn('TASK_SET', 2)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('EVENT_BEGIN', 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#0003F……先去接待处，\n'
		'请接待人员把赛西儿姐姐叫出来吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (11400, 0, 9830), 180),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('EVENT_BEGIN', 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#0003F……先去接待处，\n'
		'请接待人员把赛西儿姐姐叫出来吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (21960, 0, -230), 270),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}ＩＣＵ（加护病房）\n'
		'未经允许禁止进入。\n'
		'※入室者必须进行等级２以上的\n'
		'杀菌处理。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]
