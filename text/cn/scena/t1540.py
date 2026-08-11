# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't1540',
	'name2': 't1540',
	'location': 81,
	'bgm': 123,
	'flags': 8192,
	'includes': [
		't1540',
		't1540_1',
		't1500_1',
		None,
		None,
		None,
	],
	'name3': 't1540',
	'labels': [],
	'chcp': [
		'apl/ch50150',
		'chr/ch29900',
		'apl/ch50133',
		'apl/ch50137',
		'chr/ch29600',
		'chr/ch29800',
		'chr/ch07100',
		'apl/ch50143',
		'chr/ch33100',
		'apl/ch50132',
		'chr/ch22300',
		None,
		'chr/ch05300',
		'chr/ch29300',
		'apl/ch50135',
		'apl/ch50141',
		'apl/ch50139',
		'chr/ch20400',
		'apl/ch50152',
		'apl/ch50142',
		'chr/ch20500',
		'chr/ch30300',
		'chr/ch30200',
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
			'name': Translate('实习医生利顿'),
			'pos': (-4150, 699, -56970),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((1, 0)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('护理师希蓉'),
			'pos': (110709, 0, -5639),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((1, 1)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('护理师菲莉亚'),
			'pos': (24610, 0, 680),
			'angle': 225,
			'_1': b'\x05\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((1, 5)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('玛萨护理师长'),
			'pos': (108930, 0, 1450),
			'angle': 45,
			'_1': b'\x05\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((1, 6)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('护理师梅菲尔'),
			'pos': (110709, 0, -4320),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((1, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('赛西儿'),
			'pos': (110709, 0, -4320),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x0c\x00\x00\x00',
			'function': Function((1, 8)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('诊断医生贝尔达因'),
			'pos': (110720, 0, -4239),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\r\x00\x00\x00',
			'function': Function((1, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('多诺邦警部'),
			'pos': (12779, 0, 1299),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x15\x00\x00\x00',
			'function': Function((1, 10)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('雷蒙德搜查官'),
			'pos': (11350, 0, 1299),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x16\x00\x00\x00',
			'function': Function((1, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (4849, 699, -52060),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x02\x00\xff\xff',
			'function': Function((1, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (4809, 400, -51959),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\t\x00\xff\xff',
			'function': Function((1, 14)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (-4150, 699, -52060),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x03\x00\xff\xff',
			'function': Function((1, 15)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (4949, 699, 57029),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x07\x00\xff\xff',
			'function': Function((1, 16)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (-4000, 699, 52029),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x0e\x00\xff\xff',
			'function': Function((1, 17)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('女孩'),
			'pos': (-3440, 0, 53919),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\n\x00\x00\x00',
			'function': Function((1, 20)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (4949, 699, 52029),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x02\x00\xff\xff',
			'function': Function((1, 21)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (-4000, 699, 52029),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x03\x00\xff\xff',
			'function': Function((1, 22)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (4829, 400, 57029),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\t\x00\xff\xff',
			'function': Function((1, 23)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (4849, 699, -52060),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x0e\x00\xff\xff',
			'function': Function((1, 24)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (-4150, 699, -56970),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x0f\x00\xff\xff',
			'function': Function((1, 25)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (4949, 699, 57029),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x0f\x00\xff\xff',
			'function': Function((1, 26)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (4949, 699, 52029),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x03\x00\xff\xff',
			'function': Function((1, 27)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (-4150, 699, -56970),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x10\x00\xff\xff',
			'function': Function((1, 28)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (-4150, 699, -52060),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x0e\x00\xff\xff',
			'function': Function((1, 29)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (4949, 699, 57029),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x0f\x00\xff\xff',
			'function': Function((1, 30)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (4949, 699, 52029),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x03\x00\xff\xff',
			'function': Function((1, 31)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (-4000, 699, 52029),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x02\x00\xff\xff',
			'function': Function((1, 32)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (-4150, 699, -56970),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x10\x00\xff\xff',
			'function': Function((1, 33)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (-4150, 699, -52060),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x0f\x00\xff\xff',
			'function': Function((1, 34)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (-4000, 699, 57029),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x02\x00\xff\xff',
			'function': Function((1, 37)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (-4230, 400, 57029),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\t\x00\xff\xff',
			'function': Function((1, 38)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (-4000, 699, 52029),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x0f\x00\xff\xff',
			'function': Function((1, 39)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (-4150, 699, -52060),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x0e\x00\xff\xff',
			'function': Function((1, 41)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (-4150, 699, -56970),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x10\x00\xff\xff',
			'function': Function((1, 42)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (4849, 699, -52060),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x07\x00\xff\xff',
			'function': Function((1, 43)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('住院患者'),
			'pos': (4809, 400, -51959),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x13\x00\xff\xff',
			'function': Function((1, 44)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('黑月成员'),
			'pos': (4949, 699, 52029),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x12\x00\xff\xff',
			'function': Function((1, 45)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('探视者'),
			'pos': (-4800, 0, -53659),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x11\x00\x00\x00',
			'function': Function((1, 35)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('探视者'),
			'pos': (-4409, 0, 53549),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x14\x00\x00\x00',
			'function': Function((1, 40)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客威利安'),
			'pos': (30569, 0, -21719),
			'angle': 315,
			'_1': b'\x81\x01\x00\x00\x08\x00\x00\x00',
			'function': Function((1, 48)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('约亚西姆副教授'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((1, 46)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('亚苏拉主任'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('凯瑞教授'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
	],
	'monsters': [],
	'triggers': [],
	'objects': [
		{
			'pos': (23500, 0, -830),
			'range': 1500,
			'bubble_pos': (24610, 1500, 680),
			'_1': b'~\x00\x01',
			'function': Function((0, 4)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (3960, 0, 56230),
			'range': 1500,
			'bubble_pos': (4950, 1700, 57030),
			'_1': b'~\x00\x01',
			'function': Function((0, 26)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00Q\x00', Function((0, 1)), Function((0, 3))),
	'code': [None]*14,
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
		(Expr([Insn('ATTR', 0), Insn('CONST', 103), Insn('EQ'), Insn('FLAG', Flag(761)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(761)),
			Insn('CALL', Function((0, 2))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_SET_POS', Char(12), (110710, 0, -4320), 180),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_SET_POS', Char(14), (5150, 0, -53670), 0),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(37), 128),
			Insn('CHAR_FLAG1_UNSET', Char(39), 128),
			Insn('CHAR_FLAG1_UNSET', Char(40), 128),
			Insn('CHAR_FLAG1_UNSET', Char(41), 128),
			Insn('CHAR_FLAG1_UNSET', Char(43), 128),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(14), (7320, 0, 4420), 180),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(38), 128),
			Insn('CHAR_FLAG1_UNSET', Char(39), 128),
			Insn('CHAR_FLAG1_UNSET', Char(40), 128),
			Insn('CHAR_FLAG1_UNSET', Char(41), 128),
			Insn('CHAR_FLAG1_UNSET', Char(43), 128),
			Insn('CHAR_FLAG1_UNSET', Char(44), 128),
			Insn('CHAR_FLAG1_UNSET', Char(46), 128),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_SET_POS', Char(14), (7320, 0, 4420), 180),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(37), 128),
			Insn('CHAR_FLAG1_UNSET', Char(39), 128),
			Insn('CHAR_FLAG1_UNSET', Char(40), 128),
			Insn('CHAR_FLAG1_UNSET', Char(41), 128),
			Insn('CHAR_FLAG1_UNSET', Char(43), 128),
			Insn('CHAR_FLAG1_UNSET', Char(44), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(37), 128),
			Insn('CHAR_FLAG1_UNSET', Char(39), 128),
			Insn('CHAR_FLAG1_UNSET', Char(40), 128),
			Insn('CHAR_FLAG1_UNSET', Char(41), 128),
			Insn('CHAR_FLAG1_UNSET', Char(42), 128),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(14), (29100, 0, -20520), 270),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(32), 128),
			Insn('CHAR_FLAG1_UNSET', Char(33), 128),
			Insn('CHAR_FLAG1_UNSET', Char(34), 128),
			Insn('CHAR_FLAG1_UNSET', Char(35), 128),
			Insn('CHAR_FLAG1_UNSET', Char(36), 128),
			Insn('CHAR_FLAG1_UNSET', Char(45), 128),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(32), 128),
			Insn('CHAR_FLAG1_UNSET', Char(33), 128),
			Insn('CHAR_FLAG1_UNSET', Char(34), 128),
			Insn('CHAR_FLAG1_UNSET', Char(35), 128),
			Insn('CHAR_FLAG1_UNSET', Char(36), 128),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(28), 128),
			Insn('CHAR_FLAG1_UNSET', Char(29), 128),
			Insn('CHAR_FLAG1_UNSET', Char(30), 128),
			Insn('CHAR_FLAG1_UNSET', Char(31), 128),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(48), (-4130, 0, -55400), 180),
			Insn('CHAR_FLAG1_UNSET', Char(48), 128),
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_SET_POS', Char(12), (110710, 0, -4320), 180),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_SET_POS', Char(14), (7320, 0, 4420), 180),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(28), 128),
			Insn('CHAR_FLAG1_UNSET', Char(29), 128),
			Insn('CHAR_FLAG1_UNSET', Char(30), 128),
			Insn('CHAR_FLAG1_UNSET', Char(31), 128),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(48), (4830, 0, 54990), 0),
			Insn('CHAR_FLAG1_UNSET', Char(48), 128),
			Insn('CHAR_FLAG1_UNSET', Char(28), 128),
			Insn('CHAR_FLAG1_UNSET', Char(29), 128),
			Insn('CHAR_FLAG1_UNSET', Char(30), 128),
			Insn('CHAR_FLAG1_UNSET', Char(31), 128),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_SET_POS', Char(14), (7320, 0, 4420), 180),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(28), 128),
			Insn('CHAR_FLAG1_UNSET', Char(29), 128),
			Insn('CHAR_FLAG1_UNSET', Char(30), 128),
			Insn('CHAR_FLAG1_UNSET', Char(31), 128),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(9), (-4330, 0, -55480), 180),
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_SET_POS', Char(12), (102380, 0, -2210), 180),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_SET_POS', Char(14), (-4630, 0, 53520), 180),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(24), 128),
			Insn('CHAR_FLAG1_UNSET', Char(25), 128),
			Insn('CHAR_FLAG1_UNSET', Char(26), 128),
			Insn('CHAR_FLAG1_UNSET', Char(27), 128),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(9), (-4330, 0, -55480), 180),
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_SET_POS', Char(14), (-4630, 0, 53520), 180),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(24), 128),
			Insn('CHAR_FLAG1_UNSET', Char(25), 128),
			Insn('CHAR_FLAG1_UNSET', Char(26), 128),
			Insn('CHAR_FLAG1_UNSET', Char(27), 128),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
			Insn('CHAR_SET_POS', Char(10), (-4010, 0, -53520), 0),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_SET_POS', Char(12), (102380, 0, -2210), 180),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_SET_POS', Char(14), (29230, 0, -21560), 225),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('CHAR_FLAG1_UNSET', Char(20), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
			Insn('CHAR_FLAG1_UNSET', Char(23), 128),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('CHAR_FLAG1_UNSET', Char(20), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
			Insn('CHAR_FLAG1_UNSET', Char(22), 128),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(796)), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(10), (109200, 0, -8240), 180),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_SET_POS', Char(12), (110710, 0, -4320), 180),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('CHAR_FLAG1_UNSET', Char(20), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(785)), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(48), (-4700, 0, 53690), 180),
					Insn('CHAR_FLAG1_UNSET', Char(48), 128),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(11), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1280)), Insn('FLAG', Flag(1346)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(47), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 104), Insn('EQ'), Insn('FLAG', Flag(785)), Insn('BOOL_AND'), Insn('FLAG', Flag(786)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 10))),
		]),
		(Expr([Insn('ATTR', 0), Insn('CONST', 107), Insn('EQ'), Insn('FLAG', Flag(797)), Insn('BOOL_AND'), Insn('FLAG', Flag(798)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 13))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 4))),
		]),
		(Expr([Insn('FLAG', Flag(737)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(737)),
			Insn('EVENT', Function((0, 5))),
		]),
		(Expr([Insn('FLAG', Flag(738)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(738)),
			Insn('EVENT', Function((0, 9))),
		]),
		(Expr([Insn('FLAG', Flag(739)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(739)),
			Insn('EVENT', Function((1, 51))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('SOUND_PLAY', 160, 0, 0, 100),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('EXPR_CHAR_ATTR', Char(8), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(17), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(18), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(19), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(20), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(21), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(23), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(24), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(25), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(26), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(27), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(28), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(29), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(30), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(31), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(32), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(33), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(34), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(35), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(36), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(37), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(38), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(39), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(40), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(41), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(42), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(43), 51, Expr([Insn('CONST', 1500), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(44), 51, Expr([Insn('CONST', 1000), Insn('SET'), Insn('END')])),
	Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'BED02', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'BED03', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'BED04', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'BED05', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'BED06', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'BED07', Insn('0', 1)),
	Insn('OBJ_SET_FRAME', Object(255), 'BED08', Insn('0', 1)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED03', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED04', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED07', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED08', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED05', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED03', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED04', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED07', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED08', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED05', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED02', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED03', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED04', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED07', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED08', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED05', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED02', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED03', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED04', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED07', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED08', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED05', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED04', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED02', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED08', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED07', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED04', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED02', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED08', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED07', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED02', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED08', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED07', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED02', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED08', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED07', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED02', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED08', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED07', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED02', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED08', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED07', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED04', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED05', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED08', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED04', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED05', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED08', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED08', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED05', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED07', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED04', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED02', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED08', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED05', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED07', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED04', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'BED08', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED05', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED07', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED01', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'BED04', Insn('1', 1)),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('0x65', 1, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('0x66', 1, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('0x65', 0, 1),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(796)), Insn('END')]), [
					Insn('0x65', 0, 1),
				]),
				(None, []),
			]),
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

data['code'][4] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (4640, 1000, 2930), 0),
	Insn('CAM_ROTATE', 45, 20, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(257), (2750, 0, 2430), 90),
	Insn('CHAR_SET_POS', Char(258), (2800, 0, 3550), 90),
	Insn('CHAR_SET_POS', Char(259), (1240, 0, 2380), 90),
	Insn('CHAR_SET_POS', Char(260), (1190, 0, 3580), 90),
	Insn('CHAR_SET_POS', Char(310), (4680, 0, 2930), 90),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (10640, 1000, 2930), 5000),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (11750, 0, 2430), 2000, 0),
	]),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (11800, 0, 3550), 2000, 0),
	]),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (10240, 0, 2380), 2000, 0),
	]),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (10190, 0, 3580), 2000, 0),
	]),
	Insn('FORK', 310, 1, [
		Insn('0x95', Char(254), (13680, 0, 2930), 2000, 0),
	]),
	Insn('0x0D'),
	Insn('SLEEP', 2000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('0x6F', b'\x01'),
	Insn('CALL', Function((0, 7))),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (36760, 1000, -18000), 0),
	Insn('CAM_ROTATE', 45, 20, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(257), (39350, 100, -18000), 270),
	Insn('CHAR_SET_POS', Char(258), (39350, 100, -18000), 270),
	Insn('CHAR_SET_POS', Char(259), (39350, 100, -18000), 270),
	Insn('CHAR_SET_POS', Char(260), (39350, 100, -18000), 270),
	Insn('CHAR_SET_POS', Char(310), (39350, 100, -18000), 270),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(310), Color(0x00FFFFFF), 0),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('FORK_FUNC', Char(310), 3, Function((0, 6))),
	Insn('SLEEP', 800),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 6))),
	Insn('SLEEP', 800),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 6))),
	Insn('SLEEP', 800),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 6))),
	Insn('SLEEP', 800),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 6))),
	Insn('0x0D'),
	Insn('SLEEP', 2000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('FORK_AWAIT', Char(310), 3),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_QUIT', Char(259), 1),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x0D'),
	Insn('CALL', Function((0, 7))),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (27690, 0, -18220), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (27000, 1300, -23530), 0),
	Insn('CAM_ROTATE', 49, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 23010, 0),
	Insn('CHAR_SET_POS', Char(257), (26200, 0, -20300), 180),
	Insn('CHAR_SET_POS', Char(258), (27700, 0, -20300), 180),
	Insn('CHAR_SET_POS', Char(259), (26200, 0, -18900), 180),
	Insn('CHAR_SET_POS', Char(260), (27700, 0, -18900), 180),
	Insn('CHAR_SET_POS', Char(310), (27000, 0, -22000), 180),
	Insn('CAM_OFFSET', (27000, 1300, -25030), 2000),
	Insn('FORK', 310, 1, [
		Insn('0x95', Char(254), (27000, 0, -26000), 2000, 0),
	]),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (26200, 0, -24300), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (27700, 0, -24300), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (26200, 0, -22900), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (27700, 0, -22900), 2000, 0),
	]),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('FORK', 310, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101185V#1300F#12P就是这个病房……{wait}'
		'{page}'
		'#11101186V还有其他病人也在，\n'
		'不要太吵闹哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101187V#0000F#5P嗯，没问题。\n'
		'我们只是询问一下情况而已。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101188V#1309F#12P呵呵……\n'
		'那就进去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (-3410, 1000, -55120), 0),
	Insn('CAM_ROTATE', 30, 19, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 26050, 0),
	Insn('0x4B', Char(48), -1),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_SET_FRAME', Char(8), 2),
	Insn('CHAR_FLAG1_UNSET', Char(48), 128),
	Insn('CHAR_SET_POS', Char(48), (-4130, 0, -55510), 180),
	Insn('CHAR_SET_POS', Char(310), (0, 0, -49400), 180),
	Insn('CHAR_SET_POS', Char(257), (-600, 0, -48200), 180),
	Insn('CHAR_SET_POS', Char(258), (600, 0, -48200), 180),
	Insn('CHAR_SET_POS', Char(259), (-600, 0, -47000), 180),
	Insn('CHAR_SET_POS', Char(260), (600, 0, -47000), 180),
	Insn('CHAR_SET_COLOR', Char(310), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK2', Char(48), Translate('医生'), Text(
		'#11101189V#2404F#5P唔……\n'
		'似乎恢复良好啊。{wait}'
		'{page}'
		'#11101190V#2400F嗯，这样的话，\n'
		'明天应该就可以出院了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(8), Translate('青年实习医生'), Text(
		'#11101191V#4P真、真的吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(48), Translate('医生'), Text(
		'#11101192V#2400F#5P嗯，我不会说谎的。{wait}'
		'{page}'
		'#11101193V#2409F呵呵……\n'
		'先做好出院之后的心理准备吧。{wait}'
		'{page}'
		'#11101194V我准备了堆积如山的工作\n'
		'给你做呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(8), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK2', Char(8), Translate('青年实习医生'), Text(
		'#11101195V#4P等一下啊，约亚西姆医生！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(8), Translate('青年实习医生'), Text(
		'#11101196V#4P对待伤势初愈的人，\n'
		'怎么能这么残酷……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(48), Translate('医生'), Text(
		'#11101197V#2403F#5P只是割伤、撞伤和扭伤而已，\n'
		'别说这么没出息的话。{wait}'
		'{page}'
		'#11101198V#2400F休息了这么久，\n'
		'你的体力反而更加充沛了吧？{wait}'
		'{page}'
		'#11101199V#2409F嗯，一定能比以前\n'
		'工作得更卖力吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(8), Translate('青年实习医生'), Text(
		'#11101200V#4P……医生，是不是\n'
		'常有人说你是虐待狂？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(48), Translate('医生'), Text(
		'#11101201V#2403F#5P嗯～可我倒觉得\n'
		'自己是被虐的那一方呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('OBJ_FLAG_UNSET', Object(3), 16),
	Insn('0x71', Object(3), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x03\x00'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK2', Char(310), Translate('赛西儿的声音'), Text(
		'#11101202V#4P真是的……\n'
		'你们到底在说什么啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(48), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(8), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (-1940, 1000, -54350), 3000),
	Insn('FORK', 48, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK_AWAIT', Char(48), 1),
	Insn('FORK', 310, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x94\x11\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK', 310, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 200),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x94\x11\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 258, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x94\x11\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 259, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x94\x11\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 260, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x94\x11\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('FORK', 310, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 300),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 300),
	]),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('FORK', 310, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xc4\t\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('SLEEP', 100),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xc4\t\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 258, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xc4\t\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('SLEEP', 80),
	Insn('FORK', 259, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xc4\t\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 80),
	Insn('FORK', 260, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xc4\t\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('FORK', 310, 1, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('FORK_AWAIT', Char(310), 2),
	Insn('FORK_AWAIT', Char(257), 2),
	Insn('FORK_AWAIT', Char(258), 2),
	Insn('FORK_AWAIT', Char(259), 2),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('0x6F', b'\x01'),
	Insn('0x71', Object(3), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x03\x00'),
	Insn('OBJ_FLAG_SET', Object(3), 16),
	Insn('TEXT_TALK2', Char(48), Translate('医生'), Text(
		'#11101203V#2405F#6P哎呀……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(8), Translate('青年实习医生'), Text(
		'#11101204V#6P啊……赛西儿小姐！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101205V#1306F#11P你们两位真是的……\n'
		'还有其他病人也在呢，\n'
		'不要说些太奇怪的话哦。{wait}'
		'{page}'
		'#11101206V#1301F要是被小孩子听到怎么办呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(8), Translate('青年实习医生'), Text(
		'#11101207V#6P对、对不起……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(48), Translate('医生'), Text(
		'#11101208V#2406F#6P哈哈，说不过你呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(48), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK2', Char(48), Translate('医生'), Text(
		'#11101209V#2405F#6P哎呀，这几位是？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101210V#1300F#11P克洛斯贝尔警察局的人。{wait}'
		'{page}'
		'#11101211V那个……就之前那次事件，\n'
		'他们好像想直接听听\n'
		'利顿医生的说法。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(8), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101212V#6P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(48), Translate('医生'), Text(
		'#11101213V#2410F#6P原来如此，是这样啊。{wait}'
		'{page}'
		'#11101214V#2400F那我还是先\n'
		'回避一下吧。{wait}'
		'{page}'
		'#11101215V正好也要到其它病房查房呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101216V#1302F#11P您辛苦了。{wait}'
		'{page}'
		'#11101217V#1300F……可不能偷懒哦。\n'
		'比如偷跑出去，到水边钓鱼什么的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(48), Translate('医生'), Text(
		'#11101218V#2405F#6P呃……\n'
		'不会不会，我怎么会那样做。{wait}'
		'{page}'
		'#11101219V#2404F──那么，失陪了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_LOOP', 257, 1, [
		Insn('CHAR_WATCH', Char(257), Char(48), 500),
	]),
	Insn('FORK_LOOP', 258, 1, [
		Insn('CHAR_WATCH', Char(258), Char(48), 500),
	]),
	Insn('FORK_LOOP', 259, 1, [
		Insn('CHAR_WATCH', Char(259), Char(48), 500),
	]),
	Insn('FORK_LOOP', 260, 1, [
		Insn('CHAR_WATCH', Char(260), Char(48), 500),
	]),
	Insn('FORK_LOOP', 310, 1, [
		Insn('CHAR_WATCH', Char(310), Char(48), 500),
	]),
	Insn('FORK', 310, 2, [
		Insn('0x96', Char(254), (-1830, 0, -56820), 2000, 0),
	]),
	Insn('FORK_FUNC', Char(48), 3, Function((0, 8))),
	Insn('FORK_AWAIT', Char(48), 3),
	Insn('FORK_AWAIT', Char(310), 2),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(259), 1),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('FORK_QUIT', Char(310), 1),
	Insn('CHAR_FLAG1_SET', Char(48), 128),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(310), 300),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(310), 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(310), 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(310), 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101220V#0005F#5P那个，刚才的人是？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(310), Char(257), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101221V#1300F#12P他是约亚西姆医生，\n'
		'是位副教授哦。{wait}'
		'{page}'
		'#11101222V#1306F虽然是位非常优秀的医生，\n'
		'但是太过沉溺于个人的兴趣爱好……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(310), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(310), 315, 500),
	Insn('CAM_OFFSET', (-2550, 1000, -54720), 3000),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 215, 300),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 215, 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 215, 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 215, 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 310, 1, [
		Insn('0x95', Char(254), (-3180, 0, -55730), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('FORK', 310, 1, [
		Insn('0x95', Char(254), (-4030, 0, -55490), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('FORK', 310, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xee\x02\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xee\x02\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xee\x02\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 80),
	Insn('FORK', 260, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xee\x02\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101223V#1300F#5P……那么，利顿医生。\n'
		'能占用您一点时间吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101224V#6P嗯、嗯。\n'
		'那倒是没问题……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101225V#6P不过，为什么\n'
		'克洛斯贝尔警察局的人会来呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101226V#6P负责这次事件调查的\n'
		'不是警备队吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101227V#0003F#5P这个，警备队\n'
		'似乎也无计可施了……{wait}'
		'{page}'
		'#11101228V#0001F所以我们就来\n'
		'协助调查。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101229V#6P是这样吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101230V#6P嗯～他们果然认为\n'
		'那只是我在做梦吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101231V#6P还是觉得我有梦游症？\n'
		'不不，那应该不可能……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101232V#0103F#11P那个，如果可以的话，\n'
		'能不能请您从头说起？{wait}'
		'{page}'
		'#11101233V#0101F关于一周前的晚上发生的事情。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101234V#6P啊，好的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 3000),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('SLEEP', 200),
	Insn('EMOTE', Char(8), 0, 1700, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(8)),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101235V#11P──让我想想……\n'
		'那件事发生在深夜，\n'
		'当时我正好刚写完实习报告。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 516), Insn('SET'), Insn('END')])),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 't160b', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (10, 0, -55640), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (10, 0, -51540), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 0, 500),
	Insn('OBJ_FLAG_UNSET', Object(3), 16),
	Insn('0x71', Object(3), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x03\x00'),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (30, 0, -48960), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('SLEEP', 500),
	Insn('0x71', Object(3), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x03\x00'),
	Insn('OBJ_FLAG_SET', Object(3), 16),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0xFFFFFFFF), 0),
	Insn('FADE_ON', 0, Color(0x00FFFFFF), 255),
	Insn('CAM_OFFSET', (-3120, 2000, -54300), 0),
	Insn('CAM_ROTATE', 35, 25, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 26050, 0),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_SET_FRAME', Char(8), 2),
	Insn('CHAR_SET_POS', Char(257), (-3700, 0, -55250), 180),
	Insn('CHAR_SET_POS', Char(258), (-4600, 0, -55250), 180),
	Insn('CHAR_SET_POS', Char(259), (-3700, 0, -54150), 180),
	Insn('CHAR_SET_POS', Char(260), (-4600, 0, -54150), 180),
	Insn('CHAR_SET_POS', Char(310), (-2500, 0, -55250), 225),
	Insn('FADE_OFF', 0, Color(0xFFFFFFFF)),
	Insn('FADE_OFF', 1000, Color(0x00FFFFFF)),
	Insn('CAM_OFFSET', (-3120, 500, -54300), 3000),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101240V#4P……其实我的记忆\n'
		'就到这里了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101241V#4P第二天早上，工友先生\n'
		'在屋顶上发现了全身是伤，\n'
		'已经晕过去的我……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101242V#4P在办理了紧急住院手续之后，\n'
		'就一直躺到了现在。{wait}'
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
	Insn('TEXT_TALK', Char(257), Text(
		'#11101243V#0003F#5P……原来如此，\n'
		'情况已经基本掌握了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101244V#0301F#5P至于袭击你的那些魔兽，\n'
		'你没有看清楚它们的样子吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101245V#4P哎呀，说到这里，实在难为情，\n'
		'我好像是因为受惊过度而晕过去了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101246V#4P只记得血红发光的眼睛\n'
		'和白色的锐利牙齿，\n'
		'还有黑色的皮毛……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101247V#4P话说，警备队的人也向我确认过这些了，\n'
		'他们认为我说的是狼，我也觉得的确很像。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101248V#0203F#5P原来如此……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101249V#0101F#5P那个……\n'
		'您的伤势怎样？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101250V#4P嗯，右肩上\n'
		'有被牙咬过的痕迹。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101251V#4P但除此以外的伤\n'
		'就只是撞伤和扭伤而已了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101252V#4P我想，可能是被咬\n'
		'之后就直接倒在了\n'
		'地上吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101253V#0003F#5P……但不知为何，\n'
		'魔兽却没有继续袭击你。{wait}'
		'{page}'
		'#11101254V#0001F奇怪的地方就在这里吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101255V#4P对对，就是这样！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101256V#4P那种情况下，就算被撕成碎片\n'
		'也不奇怪呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101257V#4P而且地点还是屋顶，\n'
		'所以警备队的人也都用充满怀疑的\n'
		'目光看着我。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101258V#4P最后还怀疑我是不是\n'
		'晚上迷迷糊糊地跑到郊外，\n'
		'在外面被魔兽袭击的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101259V#0200F#5P但是，你是在\n'
		'这栋建筑物的屋顶被发现的吧……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101260V#4P嗯～但遭到袭击之后，惊惶失措地\n'
		'逃到屋顶上，然后再晕过去……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101261V#4P这种可能性或许也并非为零吧。{wait}'
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
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101262V#0006F#5P这、这个终究还是\n'
		'不太可能吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101263V#1306F#11P真是的，利顿医生。{wait}'
		'{page}'
		'#11101264V#1301F遭遇袭击的你\n'
		'怎么可以对自己的记忆\n'
		'这么没有自信呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101265V#4P呃，那个……对不起。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101266V#4P可是，无法说明的事就这么\n'
		'一直摆在那里，也会让人难以释怀吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101267V#4P与其那样的话，还不如相信\n'
		'是自己的记忆模糊了，\n'
		'反而会比较轻松……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101268V#4P而且，如果真的有魔兽\n'
		'出现在屋顶上，\n'
		'……岂不是太可怕了吗？{wait}'
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
	Insn('TEXT_TALK', Char(310), Text(
		'#11101269V#1306F#11P呼……你的心情\n'
		'也不是无法理解。{wait}'
		'{page}'
		'#11101270V#1301F可是，如果真的是这样，\n'
		'就更要认真思考对策……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101271V#0003F#5P…………………………………………{wait}'
		'{page}'
		'#11101272V#0000F谢谢您的合作。{wait}'
		'{page}'
		'#11101273V我们也会再去调查一下\n'
		'您遇袭的现场。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101274V#4P啊，好的，拜托了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11101275V#4P如果能给出说明\n'
		'并采取对策的话，\n'
		'就真是再好不过了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('BGM_STOP', 2000),
	Insn('CHAR_SET_POS', Char(0), (-2910, 0, -54690), 90),
	Insn('FLAG_SET', Flag(785)),
	Insn('QUEST', 63, Insn('TASK_SET', 10)),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('0x4C', Char(8), -1),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'{\x00\x00'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (26720, 1000, -24500), 0),
	Insn('CAM_ROTATE', 49, 19, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 21500, 0),
	Insn('CHAR_SET_POS', Char(257), (26940, 0, -23600), 180),
	Insn('CHAR_SET_POS', Char(258), (27970, 0, -24220), 270),
	Insn('CHAR_SET_POS', Char(259), (28250, 0, -25380), 270),
	Insn('CHAR_SET_POS', Char(260), (26030, 0, -25470), 0),
	Insn('CHAR_SET_POS', Char(310), (25110, 0, -23850), 90),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(815)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#11101276V#12P#0300F那么……\n'
				'这次是要去屋顶调查吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(260), Text(
				'#11101277V#12P#0300F那么……\n'
				'就是这栋楼的屋顶吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101278V#5P#0001F嗯，先去\n'
		'实习医生遇袭的现场看看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(310), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101279V#0005F#11P赛西儿姐姐，时间没问题吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101280V#6P#1306F对哦，休息时间\n'
		'好像也快结束了……{wait}'
		'{page}'
		'#11101281V#1300F不过，我至少先把你们\n'
		'带到利顿医生被发现的地方吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101282V#0000F#11P嗯，拜托啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (27000, 0, -26000), 0),
	Insn('FLAG_SET', Flag(786)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('0x70', Object(2), b'\x00\x00'),
	Insn('CAM_OFFSET', (23570, 1000, -500), 0),
	Insn('CAM_ROTATE', 68, 15, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 26180, 0),
	Insn('CHAR_SET_POS', Char(257), (22560, 0, -1490), 45),
	Insn('CHAR_SET_POS', Char(258), (21620, 0, -3050), 45),
	Insn('CHAR_SET_POS', Char(259), (21010, 0, -2400), 45),
	Insn('CHAR_SET_POS', Char(260), (22860, 0, -3470), 45),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_SET_POS', Char(10), (24600, 0, 300), 225),
	Insn('0x4B', Char(11), -1),
	Insn('CHAR_SET_POS', Char(11), (30540, 0, 20), 270),
	Insn('CHAR_SET_COLOR', Char(11), Color(0x00FFFFFF), 0),
	Insn('0x0D'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(849)), Insn('END')]), [
			Insn('TEXT_TALK', Char(10), Text(
				'#11101355V#5P啊，辛苦了～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'#11101356V#5P调查的情况怎么样了～？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(10), Text(
				'#11101357V#5P啊，辛苦了～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'#11101358V#5P你们好像是警察吧？\n'
				'调查的情况怎么样了～？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101359V#0004F#6P嗯，基本查完一遍了。{wait}'
		'{page}'
		'#11101360V#0000F所以想跟赛西儿姐姐……\n'
		'不，是跟赛西儿小姐\n'
		'报告一下。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#11101361V#5P啊，是这样吗～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(10), 0, 2000, (10, 11, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(10), Text(
		'#11101362V#5P呵呵……\n'
		'话说回来，还真是和赛西儿前辈\n'
		'说的一模一样呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101363V#0005F#6P哎……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#11101364V#5P呵呵，她经常\n'
		'跟我们说起罗伊德呢～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#11101365V#5P赛西儿前辈告诉我们你最近回到克洛斯贝尔了，\n'
		'她看上去真的非常开心呢～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#11101366V#5P呵呵……\n'
		'原来你这么可爱，那就可以理解了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 3)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101367V#0011F#6P可、可爱……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101368V#0211F#6P（……一副猥琐的表情。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101369V#0103F#12P（真是的……\n'
		'\u3000在执勤中可真是不成体统呢。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 225, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101370V#0013F#5P（我、我才没有猥琐，\n'
		'\u3000也没有不成体统啦！）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101371V#0304F#12P（呼……\n'
		'\u3000好了，看着吧，罗伊德。）{wait}'
		'{page}'
		'#11101372V#0302F（这里就交给哥哥我好了。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101373V#0005F#5P（哎……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (23600, 1000, -700), 1000),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (22880, 0, -1560), 2000, 0),
	]),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (20840, 0, -1430), 1500, 0),
	]),
	Insn('FORK', 257, 2, [
		Insn('CHAR_ROTATE', Char(254), 90, 300),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(257), 2),
	Insn('CHAR_ROTATE', Char(260), 45, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101374V#0309F#2P哈哈……\n'
		'可爱这个词，应该用来\n'
		'形容像你这样的女孩子呀。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(10), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(10), Text(
		'#11101375V#5P哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(849)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#11101376V#0304F#2P虽然我也同意\n'
				'这小子很可爱就是了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(260), Text(
				'#11101377V#0302F#2P出言冒昧，抱歉了。\n'
				'我叫兰迪。{wait}'
				'{page}'
				'#11101378V请问你的名字是……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'#11101379V#5P那个……我叫菲莉亚～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'#11101380V#5P兰迪先生\n'
				'是罗伊德的同事吗～？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#11101381V#0304F#2P嗯，我也是一名警官哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101382V#0302F#2P如何，作为友好的证明，\n'
		'周末要不要一起开个联谊会？{wait}'
		'{page}'
		'#11101383V当然也会带这家伙去的，\n'
		'而且我们这边也有女孩子，\n'
		'大家一定都会玩得很开心哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101384V#0001F#6P等、等一下……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#11101385V#5P嗯～这个嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#11101386V#5P我倒是偶尔也想放松一下，\n'
		'要是找到行程安排合适的女孩，\n'
		'我就邀请一下试试吧～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101387V#0309F#2P嗯嗯，那就拜托啦。{wait}'
		'{page}'
		'#11101388V#0300F地点就定在克洛斯贝尔的酒馆怎么样？\n'
		'就由我来负责订位吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101389V#0200F#6P（……还真是滴水不漏啊。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101390V#0106F#12P（不愧是把搭讪\n'
		'\u3000当作兴趣爱好的人……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101391V#0006F#6P（话说，我们可是来找\n'
		'\u3000赛西儿姐姐报告的啊……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101392V#0309F#2P哎呀～话说，还真是荣幸啊。{wait}'
		'{page}'
		'#11101393V能够与你这样的白衣天使\n'
		'交上朋友。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#11101394V#5P哎～但我们这里的护士服\n'
		'并不是白色的哦～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#11101395V#5P那也没关系吗～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101396V#0304F#2P没问题啦。{wait}'
		'{page}'
		'#11101397V#0302F这套衣服也很可爱的，\n'
		'而且更重要的是，穿着它的女孩们\n'
		'也个个可爱超群。{wait}'
		'{page}'
		'#11101398V#0309F特别是你哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#11101399V#5P讨厌～兰迪先生真是的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('OBJ_FLAG_UNSET', Object(2), 16),
	Insn('0x71', Object(2), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x02\x00'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK2', Char(11), Translate('中年女性的声音'), Text(
		'#11101400V哎呀，还说什么可爱超群，\n'
		'真是让人不好意思呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(10), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 11, 1, [
		Insn('0x95', Char(254), (24940, 0, -190), 2000, 0),
	]),
	Insn('FORK', 11, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK', 10, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('SLEEP', 500),
	Insn('FORK', 10, 2, [
		Insn('0x96', Char(254), (24080, 0, 600), 1000, 0),
	]),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('FORK_AWAIT', Char(11), 2),
	Insn('FORK_AWAIT', Char(10), 2),
	Insn('OBJ_FLAG_SET', Object(2), 16),
	Insn('0x71', Object(2), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x02\x00'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101401V#0305F#2P哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#11101402V#5P啊哈哈，护理师长……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 11, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101403V#2P你还有空说什么『啊哈哈』吗。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101404V#2P下午测量体温的工作完成了吗？\n'
		'那是你负责的吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(10), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(10), Text(
		'#11101405V#5P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101406V#2P而且，说到周末，\n'
		'你难道忘了这周末\n'
		'还有个大手术吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#11101407V#5P啊哈哈，是这样呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 10, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('TEXT_TALK', Char(10), Text(
		'#11101408V#5P抱歉哦，兰迪先生。\n'
		'下次有机会再说吧～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#11101409V#5P罗伊德和诸位，下次见哦～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_LOOP', 260, 1, [
		Insn('CHAR_WATCH', Char(260), Char(10), 500),
	]),
	Insn('FORK_LOOP', 11, 1, [
		Insn('CHAR_WATCH', Char(11), Char(10), 500),
	]),
	Insn('FORK', 10, 1, [
		Insn('0x95', Char(254), (26210, 0, 1130), 3000, 0),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('FORK', 10, 1, [
		Insn('0x95', Char(254), (28770, 0, -20), 3000, 0),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('OBJ_FLAG_UNSET', Object(2), 16),
	Insn('0x71', Object(2), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x02\x00'),
	Insn('FORK', 10, 1, [
		Insn('0x95', Char(254), (31000, 0, 10), 3000, 0),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 10, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('FORK_AWAIT', Char(10), 2),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('OBJ_FLAG_SET', Object(2), 16),
	Insn('0x71', Object(2), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x02\x00'),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('FORK_QUIT', Char(11), 1),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101410V#0305F#2P哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 11, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101411V#5P不然的话，作为补偿，\n'
		'这周末我就替她们陪你联谊吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101412V#5P再怎么说，我也\n'
		'同样算是个白衣天使吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101413V#0309F#2P还、还是不必了……啊哈哈。\n'
		'这实在是消受不起啊。{wait}'
		'{page}'
		'#11101414V#0306F（换你上了……罗伊德。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 135, 500),
	Insn('FORK', 260, 1, [
		Insn('0x96', Char(254), (22860, 0, -3470), 2000, 0),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_ROTATE', Char(254), 45, 100),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(260), 2),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101415V#0001F#5P唉，真是的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 90, 400),
	Insn('CAM_OFFSET', (23820, 1000, -720), 1000),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (21650, 0, -1260), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101416V#0006F#6P……不好意思。\n'
		'我们刚才太吵闹了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(257), 2),
	Insn('FORK', 11, 1, [
		Insn('CHAR_ROTATE', Char(254), 260, 500),
	]),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101417V#5P呼，算了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101418V#5P话说回来，调查结束了吗？\n'
		'你们好像是要找赛西儿吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101419V#0000F#6P嗯，基本查完一遍了。{wait}'
		'{page}'
		'#11101420V所以打算向她报告\n'
		'几个已经查明的疑点。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101421V#5P这个时间的话，赛西儿\n'
		'好像会去找那个孩子……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101422V#5P嗯～用广播喊她\n'
		'似乎也不太好……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(11), 0, 2000, (34, 36, 250, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101423V#5P对了，你们几个。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101424V#5P我想她现在应该在\n'
		'楼上最里面的病房。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101425V#5P你们能不能直接过去找她？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101426V#0005F#6P病房……吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101427V#0105F#12P我们过去打扰不要紧吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101428V#5P嗯，那间病房里住的是个\n'
		'情况比较特殊的孩子。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101429V#5P可以的话，希望你们\n'
		'也能去探望一下她。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101430V#0000F#6P原来如此……\n'
		'明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101431V#0300F#12P适当陪那孩子玩一会\n'
		'就行了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101432V#5P嗯，就是这样。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101433V#5P那么就拜托你们了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101434V#0200F#6P………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(11), 90, 500),
	Insn('FORK', 11, 1, [
		Insn('0x95', Char(254), (28870, 0, 20), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('OBJ_FLAG_UNSET', Object(2), 16),
	Insn('0x71', Object(2), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x02\x00'),
	Insn('FORK', 11, 1, [
		Insn('0x95', Char(254), (30850, 0, 10), 2000, 0),
	]),
	Insn('SLEEP', 200),
	Insn('FORK', 11, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('FORK_AWAIT', Char(11), 2),
	Insn('OBJ_FLAG_SET', Object(2), 16),
	Insn('OBJ_FLAG_SET', Object(2), 2),
	Insn('0x71', Object(2), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 107, 0, 0, 100),
	Insn('0x79', b'\x02\x00'),
	Insn('CHAR_SET_POS', Char(11), (108930, 0, 1450), 45),
	Insn('0x4C', Char(11), -1),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('CHAR_SET_POS', Char(10), (109200, 0, -8240), 180),
	Insn('0x4C', Char(10), -1),
	Insn('CHAR_SET_POS', Char(0), (22400, 0, -1750), 45),
	Insn('0x65', 0, 1),
	Insn('FLAG_SET', Flag(796)),
	Insn('QUEST', 63, Insn('TASK_SET', 19)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('EVENT_BEGIN', 0),
	Insn('0x4B', Char(11), -1),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (107900, 1000, 1500), 0),
	Insn('CAM_ROTATE', 45, 20, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(11), (108930, 0, 1450), 270),
	Insn('CHAR_SET_POS', Char(257), (107230, 0, 850), 90),
	Insn('CHAR_SET_POS', Char(258), (107230, 0, 2180), 90),
	Insn('CHAR_SET_POS', Char(259), (105980, 0, 850), 90),
	Insn('CHAR_SET_POS', Char(260), (105980, 0, 2180), 90),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101435V#11P哎呀，是你们。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101436V#11P赛西儿在\n'
		'三楼最里面的病房。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(11), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101437V#11P咦……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (106400, 1000, 1500), 3000),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(257), Char(11), 500),
	]),
	Insn('FORK_LOOP', 258, 2, [
		Insn('CHAR_WATCH', Char(258), Char(11), 500),
	]),
	Insn('FORK_LOOP', 260, 2, [
		Insn('CHAR_WATCH', Char(260), Char(11), 500),
	]),
	Insn('FORK', 11, 1, [
		Insn('0x96', Char(254), (105980, 0, 850), 1000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 257, 1, [
		Insn('0x96', Char(254), (107230, 0, 450), 1000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(259), 0, 2000, (40, 43, 100, 0)),
	Insn('FORK', 259, 1, [
		Insn('0x96', Char(254), (104580, 0, 850), 1000, 0),
	]),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('EMOTE_STOP', Char(259)),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('FORK_QUIT', Char(258), 2),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101438V#0005F#11P护理师长……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101439V#0208F#6P#40W……您有什么事………？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(11), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101440V#11P果然没错！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101441V#11P你是缇欧吧！？{wait}'
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
		'#11101442V#0011F#11P哎……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101443V#0105F#5P为什么……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101444V#0208F#6P#40W………………………………{wait}'
		'{page}'
		'#11101445V#0206F#40W……久疏……问候了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101446V#11P哈哈，果然是啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101447V#11P你长大了呢！\n'
		'都长得这么漂亮了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101448V#11P嗯，我都要认不出你了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(11), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('CHAR_ROTATE', Char(11), 45, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101449V#5P哎，可是你怎么会和\n'
		'这些小警察们……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(11), 270, 400),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101450V#11P嗯……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101451V#0208F#6P#40W那个……\n'
		'……有许多原因。{wait}'
		'{page}'
		'#11101452V#0203F#40W近期我会\n'
		'再来打招呼……{wait}'
		'{page}'
		'#11101453V#0202F#40W今天要赶时间，先失陪了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101454V#11P啊，好的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'#11101455V#11P──也是啊，\n'
		'那下次有机会再慢慢聊吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (104070, 0, 940), 270),
	Insn('CHAR_SET_POS', Char(11), (108930, 0, 1450), 45),
	Insn('0x4C', Char(11), -1),
	Insn('FLAG_SET', Flag(797)),
	Insn('FLAG_UNSET', Flag(4)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50104', 30),
	Insn('CAM_OFFSET', (27690, 1000, -9660), 0),
	Insn('CAM_ROTATE', 52, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 25500, 0),
	Insn('CHAR_SET_POS', Char(257), (26000, 0, -6300), 180),
	Insn('CHAR_SET_POS', Char(258), (27600, 0, -6000), 180),
	Insn('CHAR_SET_POS', Char(259), (26800, 0, -8400), 180),
	Insn('CHAR_SET_POS', Char(260), (26800, 0, -5000), 180),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_DISTANCE', 24000, 3000),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (26000, 0, -8800), 1000, 0),
	]),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (27600, 0, -8500), 1000, 0),
	]),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (26800, 0, -10400), 1000, 0),
	]),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (26800, 0, -7500), 1000, 0),
	]),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101456V#0208F#5P………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101457V#0001F#5P缇欧……\n'
		'你以前曾在这里住过院？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101458V#0208F#5P……嗯。{wait}'
		'{page}'
		'#11101459V大约是在六年之前。{wait}'
		'{page}'
		'#11101460V#0206F关于这点，其实我并没\n'
		'打算刻意向大家隐瞒……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101461V#0303F#5P唔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101462V#0006F#5P那个……该怎么说呢。{wait}'
		'{page}'
		'#11101463V#0000F不必太在意啦。\n'
		'任何人都会有自己的\n'
		'难言之隐……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101464V#0208F#5P……但是………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(258)),
	Insn('CAM_OFFSET', (27590, 1000, -9860), 1000),
	Insn('CAM_DISTANCE', 23500, 1000),
	Insn('0x95', Char(258), (26970, 0, -9830), 2000, 0),
	Insn('CROSSFADE', 500),
	Insn('FORK', 259, 2, [
		Insn('0xA6', Char(254), 0, 30, 500, 2000),
	]),
	Insn('CAM_DISTANCE', 22330, 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_SET', Char(259), 2),
	Insn('CHAR_FLAG1_SET', Char(259), 16),
	Insn('CHAR_SET_CHCP', Char(259), 30),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101465V#0104F#5P哎～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101466V#0205F#5P艾、艾莉前辈……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101467V#0102F#5P别摆出那种表情。{wait}'
		'{page}'
		'#11101468V你长得这么可爱，这样实在太浪费了哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101469V#0205F#5P…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101470V#0304F#5P嗯，毕竟是活了十多年的人，\n'
		'彼此都会有自己的秘密吧。{wait}'
		'{page}'
		'#11101471V#0300F更何况，从我们相遇到现在，\n'
		'也不过才一个月左右。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101472V#0004F#5P而且年龄和性别也不同……\n'
		'兴趣多半也是南辕北辙吧。{wait}'
		'{page}'
		'#11101473V即使如此，我们还是像现在这样，\n'
		'作为同伴，一起行动了……{wait}'
		'{page}'
		'#11101474V#0000F眼下，这样就已经足够了，不是吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101475V#0208F#5P罗伊德前辈、兰迪前辈……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(259), 1),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(259), 2),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(259), 3),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(259), 4),
	Insn('SLEEP', 300),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(259)),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101476V#0204F#5P……是呀。{wait}'
		'{page}'
		'#11101477V#0202F看来我似乎是\n'
		'有点神经过敏了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(259), 4),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(259), 3),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(259), 2),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(259), 1),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('SLEEP', 100),
	Insn('CROSSFADE', 500),
	Insn('CHAR_SET_CHCP', Char(259), 255),
	Insn('CHAR_SET_FRAME', Char(259), 4),
	Insn('CHAR_FLAG1_UNSET', Char(259), 2),
	Insn('CHAR_FLAG1_UNSET', Char(259), 16),
	Insn('CHAR_ROTATE', Char(259), 180, 0),
	Insn('CHAR_SET_POS', Char(258), (27070, 0, -9460), 180),
	Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 0),
	Insn('0x0D'),
	Insn('CHAR_ROTATE', Char(259), 0, 300),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101478V#0204F#12P……耽误了不少时间，\n'
		'我们赶快去赛西儿小姐那里吧。{wait}'
		'{page}'
		'#11101479V#0202F还要去报告调查结果呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101480V#0000F#5P是啊，\n'
		'去三楼的病房看看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 22580, 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(0), (26590, 0, -12170), 180),
	Insn('EXPR_ATTR', 102, Expr([Insn('ATTR', 102), Insn('CONST', 10), Insn('ADD'), Insn('SET'), Insn('END')])),
	Insn('FLAG_SET', Flag(798)),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]
