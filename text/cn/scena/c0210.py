# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'c0210',
	'name2': 'c0210',
	'location': 11,
	'bgm': 100,
	'flags': 8192,
	'includes': [
		'c0210',
		'c0210_1',
		None,
		None,
		None,
		None,
	],
	'name3': 'c0210',
	'labels': [],
	'chcp': [
		'chr/ch07000',
		'chr/ch25000',
		'chr/ch34300',
		'chr/ch24500',
		'chr/ch21600',
		'chr/ch21100',
		'chr/ch24800',
		'chr/ch10400',
		'chr/ch20700',
		'chr/ch22200',
		'chr/ch20300',
		'chr/ch02707',
		'chr/ch09300',
		'chr/ch32100',
	],
	'npcs': [
		{
			'name': Translate('奥斯卡'),
			'pos': (56290, 0, 2019),
			'angle': 270,
			'_1': b'\x05\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((0, 5)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('摩尔吉'),
			'pos': (119120, 0, -660),
			'angle': 275,
			'_1': b'\x05\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 8)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('贝奈特'),
			'pos': (51279, 1000, 12869),
			'angle': 90,
			'_1': b'\x05\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('卡缇莉娜'),
			'pos': (58540, 0, -2329),
			'angle': 0,
			'_1': b'\x05\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (53500, 0, 5010),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((0, 14)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (53500, 0, 6010),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游击士艾欧莉雅'),
			'pos': (57319, 0, -1980),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\r\x00\x00\x00',
			'function': Function((0, 24)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('塔里兹'),
			'pos': (200, 0, 8500),
			'angle': 180,
			'_1': b'\x05\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((0, 17)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('爱尔莎'),
			'pos': (-65370, 0, 2009),
			'angle': 90,
			'_1': b'\x05\x01\x00\x00\x07\x00\x00\x00',
			'function': Function((0, 18)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('小桃'),
			'pos': (3089, 0, 4199),
			'angle': 90,
			'_1': b'\x05\x01\x00\x00\x08\x00\x00\x00',
			'function': Function((0, 19)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('彼特'),
			'pos': (-3630, 0, 3509),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\t\x00\x00\x00',
			'function': Function((0, 20)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('布里吉塔'),
			'pos': (-3569, 0, 2450),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\n\x00\x00\x00',
			'function': Function((0, 21)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('赛特'),
			'pos': (2589, 0, 1320),
			'angle': 225,
			'_1': b'\x94\x01\x00\x00\x0b\x00\x00\x00',
			'function': Function((0, 22)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('哈罗德'),
			'pos': (2089, 0, 2250),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x0c\x00\x00\x00',
			'function': Function((0, 23)),
			'_2': b'\xff\x00\x00\x00',
		},
	],
	'monsters': [],
	'triggers': [],
	'objects': [
		{
			'pos': (54900, 0, 1720),
			'range': 1000,
			'bubble_pos': (56290, 1500, 2020),
			'_1': b'~\x00\x00',
			'function': Function((0, 4)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (300, 0, 6960),
			'range': 1000,
			'bubble_pos': (200, 1500, 8500),
			'_1': b'~\x00\x00',
			'function': Function((0, 16)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x0b\x00', Function((0, 2)), Function((0, 3))),
	'code': [None]*34,
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
		Insn('CHAR_IDLE', Char(254), (-69710, 410), (-67290, 3040), 1000),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('IF', [
		(Expr([Insn('ATTR', 4), Insn('CONST', 3), Insn('EQ'), Insn('ATTR', 0), Insn('CONST', 103), Insn('EQ'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 9))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 10))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 11))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 32))), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(95))), Insn('CONST', 1), Insn('NEG'), Insn('EQ'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x09', 268435456),
			Insn('EVENT', Function((1, 9))),
			Insn('0x49'),
			Insn('0x0A', 268435456),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 101), Insn('EQ'), Insn('FLAG', Flag(561)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x09', 268435456),
			Insn('EVENT', Function((0, 26))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(10), 128),
			Insn('CHAR_SET_POS', Char(17), (-68430, 0, 1820), 180),
			Insn('FORK_FUNC', Char(17), 0, Function((0, 1))),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(9), (51330, 1000, 13550), 90),
			Insn('CHAR_SET_POS', Char(10), (120860, 0, 2360), 0),
			Insn('CHAR_SET_POS', Char(16), (3090, 0, 4200), 90),
			Insn('CHAR_FLAG1_SET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(8), (122290, 0, -2810), 90),
			Insn('CHAR_SET_POS', Char(9), (56290, 0, 2020), 270),
			Insn('CHAR_SET_POS', Char(10), (120860, 0, 2360), 0),
			Insn('CHAR_FLAG1_SET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(9), (51330, 1000, 13550), 90),
			Insn('CHAR_SET_POS', Char(10), (119120, 0, -660), 275),
			Insn('CHAR_SET_POS', Char(16), (3090, 0, 4200), 90),
			Insn('CHAR_FLAG1_SET', Char(17), 128),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(9), (51330, 1000, 13550), 90),
			Insn('CHAR_SET_POS', Char(10), (119120, 0, -660), 275),
			Insn('CHAR_FLAG1_SET', Char(16), 128),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1514)), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(17), 128),
				]),
				(None, [
					Insn('CHAR_SET_POS', Char(17), (-68430, 0, 1820), 180),
					Insn('FORK_FUNC', Char(17), 0, Function((0, 1))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(10), 128),
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_SET', Char(16), 128),
			Insn('CHAR_FLAG1_SET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
		]),
		(Expr([Insn('FLAG', Flag(1294)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(9), (51330, 1000, 13550), 90),
			Insn('CHAR_FLAG1_SET', Char(10), 128),
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_FLAG1_SET', Char(16), 128),
			Insn('CHAR_FLAG1_SET', Char(17), 128),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(9), (51330, 1000, 13550), 90),
			Insn('CHAR_FLAG1_SET', Char(10), 128),
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_FLAG1_SET', Char(16), 128),
			Insn('CHAR_FLAG1_SET', Char(17), 128),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(9), (51330, 1000, 13550), 90),
			Insn('CHAR_FLAG1_SET', Char(10), 128),
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_FLAG1_SET', Char(16), 128),
			Insn('CHAR_FLAG1_SET', Char(17), 128),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(9), (120860, 0, 2360), 0),
			Insn('CHAR_FLAG1_SET', Char(10), 128),
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_SET', Char(16), 128),
			Insn('CHAR_SET_POS', Char(17), (-68430, 0, 1820), 180),
			Insn('FORK_FUNC', Char(17), 0, Function((0, 1))),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(10), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_SET', Char(16), 128),
			Insn('CHAR_FLAG1_SET', Char(17), 128),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(9), (51330, 1000, 13550), 90),
			Insn('CHAR_SET_POS', Char(10), (119120, 0, -660), 275),
			Insn('CHAR_SET_POS', Char(17), (-72880, 0, 6950), 0),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(9), (119050, 0, -140), 180),
			Insn('CHAR_SET_POS', Char(10), (119050, 0, -1650), 0),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(17), (-72880, 0, 6950), 0),
				]),
				(None, [
					Insn('CHAR_SET_POS', Char(17), (2240, 0, 2350), 180),
					Insn('CHAR_FLAG1_UNSET', Char(20), 128),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(10), (55920, 1000, 10640), 90),
			Insn('CHAR_FLAG1_SET', Char(17), 128),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(10), (55920, 1000, 10640), 90),
			Insn('CHAR_FLAG1_SET', Char(17), 128),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(10), (55170, 1000, 14200), 270),
			Insn('CHAR_SET_POS', Char(16), (2090, 0, 3530), 180),
			Insn('CHAR_FLAG1_SET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(10), (55170, 1000, 14200), 270),
			Insn('CHAR_FLAG1_SET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(10), (55170, 1000, 14200), 270),
			Insn('CHAR_SET_POS', Char(9), (120860, 0, 2360), 0),
			Insn('CHAR_FLAG1_SET', Char(17), 128),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(16), 128),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(534)), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(17), (-68430, 0, 1820), 180),
					Insn('FORK_FUNC', Char(17), 0, Function((0, 1))),
					Insn('CHAR_FLAG1_UNSET', Char(18), 128),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(16), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(9), (120820, 0, 2070), 180),
			Insn('CHAR_SET_POS', Char(10), (55170, 1000, 14200), 270),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('EXPR_CHAR_ATTR', Char(20), 45, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(20), 46, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(20), 47, Expr([Insn('CONST', 1050), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('ATTR', 4), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
			Insn('EXIT_SET_ENABLED', 0, 0),
			Insn('EXIT_SET_ENABLED', 2, 1),
			Insn('EXIT_SET_ENABLED', 1, 0),
			Insn('EXIT_SET_ENABLED', 3, 1),
		]),
		(None, [
			Insn('EXIT_SET_ENABLED', 0, 1),
			Insn('EXIT_SET_ENABLED', 2, 0),
			Insn('EXIT_SET_ENABLED', 1, 1),
			Insn('EXIT_SET_ENABLED', 3, 0),
		]),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1037)), Insn('FLAG', Flag(1038)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xd2\xc8\x00\x00\x00\x00\x00'),
		]),
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('0x7D', b'\xff\xd2\xc8\x00\x00\x00\x00\x00'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('FLAG', Flag(1554)), Insn('NOT'), Insn('OR'), Insn('END')]), [
			Insn('CALL', Function((0, 5))),
		]),
		(None, [
			Insn('CALL', Function((0, 8))),
		]),
	]),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1107)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((1, 10))),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 6, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 6, Insn('TASK_GET', 0))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 6, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x4B', Char(8), -1),
			Insn('CHAR_WATCH', Char(0), Char(8), 0),
			Insn('CALL', Function((0, 29))),
			Insn('RETURN'),
		]),
		(None, []),
	]),
	Insn('TEXT_START', Char(8)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 6, Insn('TASK_GET', 0))), Insn('EXEC', Insn('QUEST_GET', 6, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 301, 0)), Insn('CONST', 4), Insn('GE'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 303, 0)), Insn('CONST', 3), Insn('GE'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 6, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(8), Text(
				'#14700F罗伊德，收集食材的事情\n'
				'怎么样了？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('FADE_ON', 300, Color(0x00000000), 100),
			Insn('MENU', 0, -1, -1, 0, Text(
				'【交出收集的食材】\n'
				'【放弃】\n'
			)),
			Insn('MENU_WAIT', 0),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('0x60', 0),
			Insn('0x5A'),
			Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
				0: [
					Insn('CALL', Function((0, 30))),
					Insn('TEXT_END', Char(8)),
					Insn('RETURN'),
				],
				1: [
					Insn('TEXT_TALK', Char(8), Text(
						'#14709F那就下次吧，\n'
						'等你办妥之后再来找我。\n'
						'拜托你们啦！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('BREAK'),
				],
				None: [],
			}),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('FLAG', Flag(1554)), Insn('NOT'), Insn('OR'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 6, Insn('TASK_GET', 0))), Insn('EXEC', Insn('QUEST_GET', 6, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 6, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
					Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
					Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('EQ'), Insn('END')], [
						Insn('FADE_ON', 300, Color(0x00000000), 100),
						Insn('MENU', 0, -1, -1, 1, Text(
							'对话\n'
							'购物\n'
							'询问委托的事情\n'
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
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
										Insn('OPEN_SHOP', 206),
									]),
									(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
										Insn('OPEN_SHOP', 205),
									]),
									(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
										Insn('OPEN_SHOP', 204),
									]),
									(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
										Insn('OPEN_SHOP', 203),
									]),
									(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
										Insn('OPEN_SHOP', 202),
									]),
									(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
										Insn('OPEN_SHOP', 201),
									]),
									(None, [
										Insn('OPEN_SHOP', 200),
									]),
								]),
								Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
							]),
							(Expr([Insn('VAR', 0), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'#14700F我希望你们收集的是\n'
									'四个『魔兽鱼肉』\n'
									'和三个『魔兽之蛋』。{wait}'
									'{page}'
									'#14702F食材好像不太够啊，\n'
									'忙其它事情的时候顺便\n'
									'帮我收集一下就可以啦。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(911)), Insn('NOT'), Insn('END')]), [
										Insn('TEXT_TALK', Char(260), Text(
											'#0304F『魔兽鱼肉』一般可以在\n'
											'鱼形魔兽的身上得到。{wait}'
											'{page}'
											'而『魔兽之蛋』则会从\n'
											'鸟形或蛇形的魔兽身上掉落。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(257), Text(
											'#0000F哦，兰迪果然对这些\n'
											'很熟悉啊。\n'
											'真不愧是原警备队员。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(260), Text(
											'#0300F哈哈，战斗之类的事情，\n'
											'我早就习惯啦。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(258), Text(
											'#0100F魔兽所掉落的食材，\n'
											'也能用于制作料理哦。{wait}'
											'{page}'
											'趁这个机会记住，\n'
											'以后探索时也会轻松许多。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('FLAG_SET', Flag(911)),
									]),
									(Expr([Insn('EXEC', Insn('ITEM_GET', 301, 0)), Insn('CONST', 4), Insn('GE'), Insn('EXEC', Insn('ITEM_GET', 303, 0)), Insn('CONST', 3), Insn('GE'), Insn('BOOL_AND'), Insn('NOT'), Insn('END')]), [
										Insn('TEXT_TALK', Char(260), Text(
											'#0300F『魔兽鱼肉』是鱼形魔兽掉落的，\n'
											'『魔兽之蛋』可以从鸟形或蛇形的魔兽\n'
											'身上得到。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(257), Text(
											'#0000F总之，只要在郊外多绕绕，\n'
											'就能收集到这些东西。{wait}'
											'{page}'
											'#0004F好，那我们这就\n'
											'开始收集吧。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'#14709F哇哈哈，那就拜托你们啦！{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
									(None, []),
								]),
								Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
							]),
							(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), []),
							(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
								Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
								Insn('CALL', Function((0, 6))),
							]),
							(None, []),
						]),
					]),
				]),
				(None, [
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
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
										Insn('OPEN_SHOP', 206),
									]),
									(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
										Insn('OPEN_SHOP', 205),
									]),
									(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
										Insn('OPEN_SHOP', 204),
									]),
									(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
										Insn('OPEN_SHOP', 203),
									]),
									(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
										Insn('OPEN_SHOP', 202),
									]),
									(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
										Insn('OPEN_SHOP', 201),
									]),
									(None, [
										Insn('OPEN_SHOP', 200),
									]),
								]),
								Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
							]),
							(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), []),
							(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
								Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
								Insn('IF', [
									(Expr([Insn('ATTR', 4), Insn('CONST', 3), Insn('EQ'), Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 32))), Insn('BOOL_AND'), Insn('FLAG', Flag(1106)), Insn('BOOL_AND'), Insn('FLAG', Flag(1107)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(15)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
										Insn('CALL', Function((1, 12))),
										Insn('FLAG_SET', Flag(15)),
									]),
									(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1107)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
										Insn('CALL', Function((1, 11))),
									]),
									(None, [
										Insn('CALL', Function((0, 6))),
									]),
								]),
							]),
							(None, []),
						]),
					]),
				]),
			]),
		]),
		(None, [
			Insn('CALL', Function((0, 6))),
		]),
	]),
	Insn('TEXT_END', Char(8)),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(13)), Insn('END')]), [
			Insn('TEXT_TALK', Char(8), Text(
				'#14702F今天真是得救了。\n'
				'你们就顺便尝尝\n'
				'我烤的面包吧。{wait}'
				'{page}'
				'#14709F呵呵，免费赠送哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F谢啦，那就让我选一点吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1898)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F哟，罗伊德，\n'
						'你还在调查什么案子吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F嗯，差不多吧。{wait}'
						'{page}'
						'#0001F……奥斯卡，为求谨慎，\n'
						'我想问你这附近\n'
						'有没有发生什么奇怪的事？{wait}'
						'{page}'
						'比如看见一些黑衣人什么的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14703F奇怪的事啊……嗯～{wait}'
						'{page}'
						'#14705F其实，贝奈特刚才\n'
						'突然很生气，\n'
						'然后就跑出去了。{wait}'
						'{page}'
						'#14701F到底发生了什么事呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1897)), Insn('NOT'), Insn('END')]), [
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
								'#0006F你啊，真是的，\n'
								'对这方面太迟钝了吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(258), Text(
								'#0100F西侧大道附近好像\n'
								'没什么事件发生吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
							Insn('SOUND_PLAY', 23, 0, 0, 100),
							Insn('SLEEP', 1000),
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F不、不太清楚呢……{wait}'
								'{page}'
								'但说不定是奥斯卡的错吧？\n'
								'你有时的确很迟钝……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'#14705F哎，是吗？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(258), Text(
								'#0100F（嗯，西侧大道一带好像\n'
								'\u3000没发生什么特别的事件。）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
					Insn('FLAG_SET', Flag(1898)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14703F贝奈特今天\n'
						'烤了很美味的面包\n'
						'给我吃呢。{wait}'
						'{page}'
						'#14706F然后，我坦率地说出了想法后，\n'
						'她就突然生气地跑出去了。{wait}'
						'{page}'
						'#14701F唔，到底是怎么了啊？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14705F昨天，在港湾区那边\n'
						'好像发生了枪击事件吧？{wait}'
						'{page}'
						'#14701F黑手党如果认真起来，\n'
						'就会毫无顾忌地展开争斗，\n'
						'将市民都牵连进去……{wait}'
						'{page}'
						'#14706F真是群棘手的家伙啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14703F难得店里的营业额\n'
						'刚刚有起色呢。{wait}'
						'{page}'
						'#14701F希望不要碰到麻烦事。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_ROTATE', Char(8), 90, 0),
					Insn('TEXT_TALK', Char(8), Text(
						'#14703F那个，毛毯在哪里啊……？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(8), Char(0), 500),
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F贝奈特为了研究新面包的烤制方法，\n'
						'几乎都没有睡过觉。{wait}'
						'{page}'
						'#14709F哈哈，还真是费事啊，\n'
						'就像小时候那个一直\n'
						'被赛西儿小姐照顾的罗伊德一样。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F不、不要突然\n'
						'提起过去的事情啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14704F哎呀呀，先得把她带回房去，\n'
						'免得她生病着凉。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1643)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F罗伊德，你们好啊。\n'
						'今天带稀客来了啊？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F嗯，这位是警备队的\n'
						'诺艾儿上士。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(265), Text(
						'#0500F呵呵，初次见面。{wait}'
						'{page}'
						'话说……\n'
						'我听芙兰提起过\n'
						'这家名叫『摩尔吉』的面包店。{wait}'
						'{page}'
						'据说有位年轻的天才面包师，\n'
						'还曾被杂志报道过呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14705F哦，是指那次的采访啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0300F好厉害啊，竟然能\n'
						'接受杂志的采访。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F不过，这家店的面包确实很美味，\n'
						'会被杂志报道也并不奇怪。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F呵呵，我也还在学习中，\n'
						'所以对这种事不是很感兴趣。{wait}'
						'{page}'
						'#14703F不过师傅倒是很热衷，\n'
						'而且也有助于提高营业额，\n'
						'所以就勉强接受了采访。{wait}'
						'{page}'
						'#14706F结果拜其所赐，研制这个月的面包新品\n'
						'让我很有压力呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F哈哈，你还真会说。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F呵呵，既然如此，\n'
						'那我们也来尝尝那个新品面包吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1643)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14706F我哪里是什么天才啊，\n'
						'和师傅比起来还差得很远。{wait}'
						'{page}'
						'#14704F技术方面也有很多东西\n'
						'需要贝奈特教我。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1389)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 7))),
					Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
					Insn('RETURN'),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(339), Text(
						'#1110F这里的味道好香啊！\n'
						'大哥哥，你是做什么的～？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F噢，我是面包师哦。{wait}'
						'{page}'
						'#14702F琪雅要不要也来一个啊？\n'
						'我们的面包很好吃哦～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(339), Text(
						'#1109F嗯，我要吃～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F喂喂……\n'
						'别不经过我就擅自决定啊。{wait}'
						'{page}'
						'#0000F（不过，她好像不认得\n'
						'\u3000这家面包店啊。）{wait}'
						'{page}'
						'（果然不是\n'
						'\u3000克洛斯贝尔出身吧……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14702F罗伊德，给琪雅\n'
						'买点什么吧。{wait}'
						'{page}'
						'#14700F我推荐\n'
						'限时供应的\n'
						'甜蜜牛奶面包哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1388)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F听说已经找到\n'
						'那个男孩子了？{wait}'
						'{page}'
						'#14706F哈，真是太好了。\n'
						'参加纪念庆典的人那么多，\n'
						'做父母的一定会很担心吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F嗯，他们非常担心呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F话说回来，奥斯卡。{wait}'
						'{page}'
						'#0000F你去过『米修拉姆』\n'
						'这个地方吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(8), 0, 2000, (38, 38, 250, 1)),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F很不巧，没去过。{wait}'
						'{page}'
						'#14704F听说是什么主题乐园，\n'
						'不过我没什么兴趣呢。{wait}'
						'{page}'
						'#14702F温蒂似乎倒是\n'
						'去那里玩过好几次。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F这样啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14704F据说那里是\n'
						'非常受欢迎的度假地哦。{wait}'
						'{page}'
						'#14700F已经成为了约会和\n'
						'家庭出游的必选之地了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1388)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F对了，师傅要在今天下午\n'
						'给我放假呢。{wait}'
						'{page}'
						'#14704F我对主题乐园没什么兴趣，\n'
						'还是在市内随便逛逛好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1303)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F哟，罗伊德，是你们啊。\n'
						'找到那个男孩了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0001F不，我们还在找，\n'
						'不过已经有线索了，\n'
						'别担心。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14704F是吗，那真是太好了。{wait}'
						'{page}'
						'#14700F他现在可能很害怕呢，\n'
						'所以要赶紧找到他才行！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(352), Text(
						'#3300F……嗯，是啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14704F还好已经有\n'
						'线索了。{wait}'
						'{page}'
						'#14700F他现在可能很害怕呢，\n'
						'所以要赶紧找到他才行！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1294)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1383)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F哦，这不是罗伊德嘛。{wait}'
						'{page}'
						'#14702F带着那么可爱的小姑娘，\n'
						'在干什么呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F啊，只是\n'
						'正在找人……{wait}'
						'{page}'
						'#0001F奥斯卡，你见过\n'
						'这张照片上的孩子吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'{color 5}罗伊德出示了柯林的照片，\n'
						'并询问对方是否有什么线索。{color 0}{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('0x5A'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14705F咦，这孩子\n'
						'不是柯林吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F哎，你认识他吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14704F嗯，是住在住宅区的孩子吧？{wait}'
						'{page}'
						'#14700F他们一家人\n'
						'偶尔会一起来买面包呢。{wait}'
						'{page}'
						'#14703F只是……\n'
						'今天没有见过他。{wait}'
						'{page}'
						'#14700F去看游行的时候，\n'
						'在西侧大道也没见到过。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F果然是这样啊……\n'
						'谢啦，真是帮大忙了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1383)),
					Insn('0xD0', 2, Expr([Insn('0x23', 2), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
					Insn('CALL', Function((0, 25))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F这孩子我认识，\n'
						'不过今天没有见过。{wait}'
						'{page}'
						'#14703F至少他没有从\n'
						'我们店门前经过呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14705F欢迎光临……\n'
						'罗伊德，是你们啊。{wait}'
						'{page}'
						'#14700F今天我一整天\n'
						'都要烤面包。{wait}'
						'{page}'
						'#14704F没想到竟然\n'
						'会有这么多人啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14704F今年的人流真是格外壮观啊。{wait}'
						'{page}'
						'#14700F师傅说，他也是\n'
						'第一次见到那么多人呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(8), Text(
				'#14700F游行队伍好像\n'
				'也会经过我们店门口哦。{wait}'
				'{page}'
				'#14703F希望不要有人因为太过兴奋\n'
				'而不小心受伤啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14704F贝奈特的试吃活动\n'
						'好像很顺利。{wait}'
						'{page}'
						'#14702F看来今天能卖出更多面包呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14704F贝奈特提议的试吃活动已经开始了。{wait}'
						'{page}'
						'#14702F真是个好主意啊，\n'
						'看来今天能卖出更多呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F罗伊德，你们好啊。{wait}'
						'{page}'
						'#14704F纪念庆典期间，我们店也很忙。\n'
						'面包的销量是平时的\n'
						'三倍左右。{wait}'
						'{page}'
						'#14704F那起暗杀麦克道尔市长的事件之后，\n'
						'我还在担心今后会怎么样，\n'
						'不过，好像对客流没什么影响呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14702F针对纪念庆典，\n'
						'我也试做了新的面包。{wait}'
						'{page}'
						'#14700F有兴趣的话，就来尝尝吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F最近，经常有\n'
						'警察到店里来。{wait}'
						'{page}'
						'#14704F虽然穿着便装，\n'
						'不过看那架势就知道是搜查官。{wait}'
						'{page}'
						'#14700F大概是在监视什么吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F……奥斯卡先生，\n'
						'你的观察力真是不错啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F他在这方面\n'
						'倒是一直很敏锐的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14709F哈哈，也没有这么夸张啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14704F最近，经常有\n'
						'警察到店里来。{wait}'
						'{page}'
						'#14700F好像在对什么情况进行监视。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F彩虹剧团的新剧码\n'
						'下个月就要开始公演了。{wait}'
						'{page}'
						'#14704F虽然我没有什么兴趣，\n'
						'不过客人们一直\n'
						'都在谈论这个呢。{wait}'
						'{page}'
						'#14702F──对了，罗伊德。\n'
						'要是愿意的话，一起去吧？{wait}'
						'{page}'
						'#14700F我有门票哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
					Insn('SOUND_PLAY', 28, 0, 0, 100),
					Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
					Insn('SOUND_PLAY', 28, 0, 0, 100),
					Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
					Insn('SOUND_PLAY', 28, 0, 0, 100),
					Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
					Insn('SOUND_PLAY', 28, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F奥斯卡……\n'
						'你竟然有门票！？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F嗯，是一个老顾客给我的。{wait}'
						'{page}'
						'#14702F她就住在那边的公寓里，\n'
						'是个非常漂亮的美人呢。{wait}'
						'{page}'
						'#14704F我偶尔会送她面包，\n'
						'所以她就送票来答谢我了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1145)), Insn('END')]), [
							Insn('EMOTE', Char(0), 0, 2000, (16, 19, 250, 1)),
							Insn('SOUND_PLAY', 23, 0, 0, 100),
							Insn('EMOTE', Char(1), 0, 2000, (16, 19, 250, 1)),
							Insn('SOUND_PLAY', 23, 0, 0, 100),
							Insn('EMOTE', Char(2), 0, 2000, (16, 19, 250, 1)),
							Insn('SOUND_PLAY', 23, 0, 0, 100),
							Insn('EMOTE', Char(3), 0, 2000, (16, 19, 250, 1)),
							Insn('SOUND_PLAY', 23, 0, 0, 100),
							Insn('SLEEP', 1000),
							Insn('TEXT_TALK', Char(260), Text(
								'#0300F（喂喂，难不成……）{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(259), Text(
								'#0200F（多半是\n'
								'\u3000伊莉雅小姐吧……）{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0006F（不愧是奥斯卡……\n'
								'\u3000在这方面真是很迟钝啊。）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('TEXT_TALK', Char(260), Text(
								'#0300F真、真是个慷慨的客人啊……{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F她就住在那边的公寓里，\n'
						'是个非常漂亮的美人呢。{wait}'
						'{page}'
						'#14702F每天早上六点左右，\n'
						'她都会来买很多很多面包。{wait}'
						'{page}'
						'#14704F我偶尔会赠送给她一些新品面包，\n'
						'所以她就送门票来答谢我了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1137)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14701F我们店门口正好\n'
						'是一条能通往主干道的大街。{wait}'
						'{page}'
						'#14706F最近有很多导力车\n'
						'来来往往呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F说起来，最近\n'
						'有很多运输公司\n'
						'开始使用导力卡车了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14705F对了，还有……{wait}'
						'{page}'
						'#14703F大概是凌晨三点左右，\n'
						'我正准备开始制作面包的时候，\n'
						'看到了一辆黑色的搬运车。{wait}'
						'{page}'
						'#14701F据说那是『鲁巴彻』的车，\n'
						'是不是真的啊？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F（西克洛斯贝尔街道……\n'
						'\u3000会不会是与帝国之间的\n'
						'\u3000走私路线呢？）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0300F（无限接近黑暗的\n'
						'\u3000灰色地带啊……）{wait}'
						'{page}'
						'（他们也在矿山镇露过面，\n'
						'\u3000最近的活动好像很频繁啊。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1137)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14703F最近大概凌晨三点左右，\n'
						'我正准备开始制作面包的时候，\n'
						'看到了一辆黑色的搬运车。{wait}'
						'{page}'
						'#14701F据说那是『鲁巴彻』的车，\n'
						'是不是真的啊？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1136)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F罗伊德，你们好啊。{wait}'
						'{page}'
						'#14702F你们最近备受好评，\n'
						'客人们都在谈论你们呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F哈哈，总觉得有点难为情。{wait}'
						'{page}'
						'因为我们最近\n'
						'处理的都是一些\n'
						'很普通的支援请求……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F即使是平淡无奇的事情，\n'
						'只要持之以恒，自然就会受到好评呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14702F哈哈，\n'
						'不过更受好评的\n'
						'还是那条白色的警犬呢。{wait}'
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
						'#0006F果然是赛特啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14702F早上做准备工作的时候，\n'
						'偶尔会看到它，\n'
						'真是很帅啊～{wait}'
						'{page}'
						'#14709F我也很喜欢狗，\n'
						'下次把它介绍给我吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1136)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14702F那条警犬，在这附近\n'
						'已经成了热门话题呢。{wait}'
						'{page}'
						'#14709F我也很喜欢狗，\n'
						'下次把它介绍给我吧。{wait}'
						'{page}'
						'#14709F我会请它尝尝\n'
						'这个月的新品面包。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14702F贝奈特是师傅的女儿，\n'
						'制作面包的技术很厉害呢。{wait}'
						'{page}'
						'#14700F我刚来这里做学徒的时候，\n'
						'还是贝奈特教我入门知识的。{wait}'
						'{page}'
						'#14703F不过她的性格不太好，\n'
						'总是因为一点小事生气。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F其实她长得还是很可爱的，\n'
						'总是生气的话，真是太可惜了。{wait}'
						'{page}'
						'#14704F下次我要做\n'
						'高钙的牛奶面包。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(8), Text(
				'#14702F我们的蔬菜面包\n'
				'使用了阿尔摩利卡出产的\n'
				'小麦和蔬菜。{wait}'
				'{page}'
				'#14700F虽然共和国产的食材最近比较便宜，\n'
				'不过新鲜度还是不能相比啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F哈哈，你们对食材\n'
				'还是很讲究的嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14705F罗伊德，你们今天好早啊。\n'
						'遇到什么好事了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 6, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F不，没什么特别的理由。{wait}'
								'{page}'
								'奥斯卡才是，一直都起得这么早……\n'
								'呃……不过对面包师来说，这也是应该的吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('TEXT_TALK', Char(257), Text(
								'#0006F不，我们是为工作而来的。{wait}'
								'{page}'
								'#0000F奥斯卡才是，一直都起得这么早……\n'
								'呃……不过对面包师来说，这也是应该的吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F呵呵，早安。\n'
						'今天也是香气四溢呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14702F哈哈哈，那是当然啦。\n'
						'这边的架子上是刚烤好的\n'
						'本月新品面包哦。{wait}'
						'{page}'
						'#14709F有兴趣的话，就请尝尝吧。\n'
						'刚烤出来的面包最好吃了！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14704F面包师在凌晨三点就要开工。\n'
						'开始新一天工作的时候，\n'
						'感觉真是意外地神清气爽啊。{wait}'
						'{page}'
						'#14700F我也是因为憧憬这一点，\n'
						'所以才选择了面包师这个职业。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(599)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(619)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(8), Text(
								'#14702F哟，罗伊德，这么快就来了啊。{wait}'
								'{page}'
								'#14704F我们都有半年没见了吧……\n'
								'不，已经有一年了吧？\n'
								'真是过了很久呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0003F……那个。\n'
								'我们都已经有三年没见面了吧？{wait}'
								'{page}'
								'之前你自己也都这么说过啊。\n'
								'你这方面还真是一点没变，\n'
								'总是这么粗枝大叶……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'#14709F哇哈哈，不要在意这种小事啦！{wait}'
								'{page}'
								'#14702F话说，你好像\n'
								'长高了很多呢。\n'
								'不过还是一张娃娃脸。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0011F唔……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(260), Text(
								'#0309F哈哈。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(258), Text(
								'#0100F嘻嘻……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(259), Text(
								'#0204F呵呵……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('EMOTE', Char(257), 0, 2000, (14, 15, 250, 2)),
							Insn('SOUND_PLAY', 23, 0, 0, 100),
							Insn('SLEEP', 1000),
							Insn('TEXT_TALK', Char(257), Text(
								'#0006F好了，这话题到此为止。{wait}'
								'{page}'
								'#0000F说起来……奥斯卡，\n'
								'你的手艺好像长进了不少啊？{wait}'
								'{page}'
								'温蒂在信里也写了哦，\n'
								'听说你每月推出的新品面包\n'
								'都很受大家好评呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'#14703F哪里哪里，我还在学习呢。\n'
								'没有比面包师\n'
								'更深奥的工作了。{wait}'
								'{page}'
								'#14700F不过，这个月的新品，\n'
								'我觉得确实很不错呢。{wait}'
								'{page}'
								'#14702F有兴趣的话……罗伊德的同事们\n'
								'也都尝尝看吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(260), Text(
								'#0300F哦，那我就挑一些啦。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(258), Text(
								'#0100F这些面包看上去都很好吃啊，\n'
								'我也买一些\n'
								'带回去吃吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(619)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(8), Text(
								'#14704F虽然我还在学习之中，\n'
								'不过对本月的新品倒很有自信。{wait}'
								'{page}'
								'#14702F有兴趣的话，就来尝尝吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(619)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F对了，罗伊德，\n'
						'你见过温蒂了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F嗯，刚刚偶然遇到了。{wait}'
						'{page}'
						'作为一个技师，\n'
						'她似乎做得很不错……{wait}'
						'{page}'
						'#0003F但作为她的老朋友，\n'
						'我一直都有些担心……\n'
						'她会不会发起火来拿扳手揍客人呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14709F哇哈哈，说得没错。{wait}'
						'{page}'
						'#14700F不过，没问题的。\n'
						'温蒂表面虽然这样，\n'
						'但其实很能掌握分寸的。{wait}'
						'{page}'
						'#14704F顶多也就把人家\n'
						'打出个肿包罢了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(8), 0, 2000, (38, 39, 250, 2)),
					Insn('EMOTE', Char(257), 0, 2000, (38, 39, 250, 2)),
					Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(258), Text(
						'#0105F（我觉得这已经非常严重了……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0306F（唉，小温蒂她居然会这样。\n'
						'\u3000明明那么可爱……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F（兰迪前辈最好也\n'
						'\u3000小心一点呢。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(619)),
				]),
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F对了，最近有很多警方人士\n'
						'光顾我们店呢。{wait}'
						'{page}'
						'#14704F我们旁边不就是法律事务所吗？\n'
						'他们有事去那里的话，\n'
						'顺道就会光顾这边。{wait}'
						'{page}'
						'#14702F哎呀～真是太好了，\n'
						'我们的面包竟能让那么严肃的大叔\n'
						'也露出笑容，实在是光荣啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F最近有很多警察\n'
						'光顾我们店呢。{wait}'
						'{page}'
						'#14704F他们要去旁边的法律事务所，\n'
						'顺道就会光顾这里。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F奥斯卡，你的手艺\n'
						'好像长进了不少啊？{wait}'
						'{page}'
						'温蒂在信里也写了哦，\n'
						'听说你每月推出的新品面包\n'
						'都很受大家好评呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F哪里，我还在学习呢。{wait}'
						'{page}'
						'#14703F没有比面包师\n'
						'更深奥的工作了。{wait}'
						'{page}'
						'#14700F不过，这个月的新品，\n'
						'我觉得确实很不错呢。{wait}'
						'{page}'
						'#14702F有兴趣的话，就来尝尝吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14704F虽然我还在学习之中，\n'
						'不过对本月的新品倒很有自信。{wait}'
						'{page}'
						'#14702F有兴趣的话，就来尝尝吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('EVENT_BEGIN', 0),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu08300.itp'),
	Insn('FADE_ON', 500, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (54330, 1500, 1490), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 30000, 0),
	Insn('CHAR_SET_POS', Char(257), (52480, 0, 1350), 90),
	Insn('CHAR_SET_POS', Char(239), (51860, 0, 2300), 90),
	Insn('CHAR_SET_POS', Char(339), (52000, 0, 260), 90),
	Insn('CHAR_ROTATE', Char(8), 270, 0),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SLEEP', 750),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 300),
	Insn('TEXT_SET_NAME', Translate('奥斯卡')),
	Insn('TEXT_MESSAGE', Char(8), Text(
		'哟，罗伊德，\n'
		'有一周没见了啊。{wait}'
		'{page}'
		'平时不是经常过来吗，\n'
		'难道发生什么事了吗？{wait}'
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
		'#0000F不，其实……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#1110F哇，好高的帽子！\n'
		'好有趣哦！{wait}'
		'{page}'
		'#1104F而且……\n'
		'嗯嗯，好香的味道啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(8), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(8)),
	Insn('TEXT_TALK', Char(8), Text(
		'#14705F………那个………{wait}'
		'{page}'
		'#14702F这是罗伊德的妹妹吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0006F……不是的，\n'
		'我没有妹妹啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14709F哇哈哈，\n'
		'当然是开玩笑啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F这个孩子叫琪雅，\n'
				'因为某些原因，暂时由我们照顾。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F这孩子叫琪雅，\n'
				'由于某些原因，暂时由我们照顾。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F这小鬼叫琪雅，\n'
				'稍微有些原因，所以暂时由我们来照顾。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(8), Text(
		'#14700F哦，是这样啊。{wait}'
		'{page}'
		'#14709F好，作为初次见面的纪念，\n'
		'不嫌弃的话就尝尝吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}琪雅收下了牛奶瓶。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(339), Text(
		'#1105F哇，可以吗～？{wait}'
		'{page}'
		'#1109F（咕噜咕噜……）真好喝啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14709F哈哈哈！\n'
		'我们店里的牛奶是阿尔摩利卡产的哟。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F哈哈，让你费心了，真不好意思啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(1389)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('TEXT_START', Char(9)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('FLAG', Flag(1554)), Insn('BOOL_AND'), Insn('END')]), [
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
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
								Insn('OPEN_SHOP', 206),
							]),
							(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
								Insn('OPEN_SHOP', 205),
							]),
							(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
								Insn('OPEN_SHOP', 204),
							]),
							(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
								Insn('OPEN_SHOP', 203),
							]),
							(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
								Insn('OPEN_SHOP', 202),
							]),
							(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
								Insn('OPEN_SHOP', 201),
							]),
							(None, [
								Insn('OPEN_SHOP', 200),
							]),
						]),
						Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
					]),
					(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), []),
					(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
						Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
						Insn('CALL', Function((0, 9))),
					]),
					(None, []),
				]),
			]),
		]),
		(None, [
			Insn('CALL', Function((0, 9))),
		]),
	]),
	Insn('TEXT_END', Char(9)),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('IF', [
		(Expr([Insn('ATTR', 4), Insn('CONST', 3), Insn('EQ'), Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 32))), Insn('BOOL_AND'), Insn('FLAG', Flag(1106)), Insn('BOOL_AND'), Insn('FLAG', Flag(1107)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(16)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((1, 6))),
			Insn('FLAG_SET', Flag(16)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1107)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((1, 5))),
			Insn('RETURN'),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 6, Insn('FLAG_GET', 16))), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(878)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'哦，我听说了呢。\n'
				'已经帮我们收集到食材了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'太高兴了，这么一来就能\n'
				'尽情烤面包了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F如果还有什么事，\n'
				'请尽管联系支援课。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F这些小事\n'
				'都是举手之劳啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'你们真是可靠啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'呵呵，说不定以后还要请你们帮忙哦。\n'
				'到时候就拜托啦！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(878)),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 6, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'哎呀，食材配送时间\n'
						'居然比预定要晚呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'今天只能节省着材料\n'
						'来烤面包了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'感觉真是束手束脚啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'唉，真没办法……\n'
						'但愿明天能快点送来。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'贝奈特做的新面包，\n'
						'我和奥斯卡都赞许有加呢……\n'
						'但她本人却不这么觉得。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'嗯，对味道已经很满意了……\n'
						'但却不能接受奥斯卡的反应吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'嗯，真是想不明白啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'这个年纪的女孩，\n'
						'心思真是难以琢磨。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'哦……贝奈特那家伙，\n'
						'烤的面包可真香啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'这次的面包，\n'
						'看来很值得期待啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'贝奈特也开始\n'
						'很认真地做面包了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'……真是很香啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'最近增加了很多\n'
				'从远方而来的客人。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'真让人高兴啊，\n'
				'这也是奥斯卡\n'
				'努力的成果。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'多亏了他，\n'
				'竟然连克洛斯贝尔时报周刊\n'
				'都过来采访我们呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'贝奈特也一直在\n'
						'认真地钻研呢，\n'
						'于是我重新考虑了一下新品面包的上架方式。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'简单来说，就是三个人各自拿出自己的试做品，\n'
						'然后投票决定最好吃的面包。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'……怎么样，这种方法很合理吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'原来一直是\n'
						'由我试吃后决定的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'不过，奥斯卡和贝奈特\n'
						'现在都已经可以独当一面了，\n'
						'所以还是投票决定比较公平。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'贝奈特最近\n'
						'总是霸占着厨房。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'真拿她没办法啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'伤脑筋，\n'
						'我也想烤面包啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'客流差不多也该减少了，\n'
				'我们也稍微休息一下吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'……做面包是需要腕力的，\n'
				'我也有些累了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'啪啪啦啪啪，啪啪啪～！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'游行时放的曲子，\n'
				'每年都是一样的啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'每当听到这首曲子，\n'
				'就感觉自己恢复了童心。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'今天有纪念庆典期间\n'
				'最盛大的一项活动──游行。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'熬过这段时间，\n'
				'就能稍微轻松些了。\n'
				'再继续坚持一下吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'嘿，嘿……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'今年的客流量真是不错啊，\n'
				'无论烤多少面包也都供不应求。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'那个别扭的贝奈特要进行\n'
						'店前零售……？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'而且她还很努力地\n'
						'保持着职业微笑。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'……这家伙变化太大，\n'
						'让我这个做爸爸的都有点担心了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'那家伙，最近真是\n'
						'变得很积极了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'……呵，真是吓了一跳呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'自从奥斯卡来了之后，\n'
				'贝奈特就变得很积极了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'嗯，真是收了个\n'
				'好徒弟呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 12))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'奥斯卡那家伙的手艺非常不错，\n'
						'更重要的是，他很有男子汉气概。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'这样店里也就安稳了，哇哈哈！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('RECIPE', 23)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 10))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'好了，我也要\n'
						'想想下一款新面包了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'如果一直都交给奥斯卡去做，\n'
						'也不太好呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('RECIPE', 23)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 10))),
				]),
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'虽然贝奈特\n'
						'好几次都想挑战奥斯卡……\n'
						'但怎么也赢不了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'所以她才变得那么拼命啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'奥斯卡的面包\n'
						'很受欢迎呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'不仅是因为制作材料和手法，\n'
						'也是因为那家伙在揉合方面的\n'
						'技巧感很好。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'最近的新品面包\n'
						'都是交给奥斯卡来做的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'那家伙确实富有才能。\n'
						'而且，他不仅非常努力，\n'
						'更拥有出类拔萃的天赋。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'我已经没有什么\n'
						'可以教他的了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'奥斯卡的天赋实在是出类拔萃。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'呵呵，贝奈特一直对他\n'
						'抱有竞争意识，也是因为这个原因吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'虽然也许没人察觉到，\n'
						'不过我做面包的基准是『香味』。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'研制新品面包的时候，\n'
						'也会注重香味。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'这也等同于必须将\n'
						'食材的优点引发出来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'我制作新的面包，\n'
						'说到底就是为了\n'
						'不断探求活用素材的方法。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'当然，赢得顾客的认可\n'
						'也是理由之一。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'好了，第二炉烤好了～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'嗯，真是香气扑鼻啊。\n'
						'正因为能够享受这种香味，我才无法放弃当面包师啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'我们店的面包从五点开始烤制。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'在那以前一直在做生面团。\n'
						'之后就是烤啊烤，\n'
						'尽情享受香味的快乐时光了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'我女儿最讨厌的就是输给别人，\n'
						'最近好像对奥斯卡\n'
						'燃起了强烈的竞争意识呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'之前明明说过\n'
						'不想当面包师的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'哈哈，真不知道她在想什么啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'这个年纪的女孩，真是让人猜不透。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'……哦，欢迎光临！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'虽然我们是面包店，\n'
						'但店门前也设置了能够\n'
						'享用咖啡的露天座位区哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'坐在那里吃点东西，很方便吧？\n'
						'还请随意使用啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'我们店门前设置了能够\n'
						'享用咖啡的露天座位区哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'而且还提供饮料，\n'
						'请随意就坐吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('TEXT_TALK', Char(254), Text(
		'哟，欢迎光临。\n'
		'这个月的新面包已经开始销售了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'对了，这个月的面包\n'
		'搭配这款咖啡很不错呢。\n'
		'有兴趣的话就记下来吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'学习了{item 467}{color 0}的做法。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'记住了{item 467}{color 0}的食谱。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('RECIPE', 23),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 6, Insn('TASK_GET', 0))), Insn('EXEC', Insn('QUEST_GET', 6, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 6, Insn('TASK_GET', 2))), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_WATCH', Char(0), Char(10), 0),
			Insn('0x4B', Char(10), -1),
			Insn('CALL', Function((0, 31))),
			Insn('RETURN'),
		]),
		(None, []),
	]),
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1107)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((1, 13))),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 6, Insn('TASK_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 6, Insn('TASK_GET', 3))), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('ITEM_GET', 303, 0)), Insn('CONST', 2), Insn('GE'), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'#14805F啊……{wait}'
						'{page}'
						'#14800F帮我把食材拿来了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
					Insn('FADE_ON', 300, Color(0x00000000), 100),
					Insn('MENU', 0, -1, -1, 0, Text(
						'【交出收集的食材】\n'
						'【放弃】\n'
					)),
					Insn('MENU_WAIT', 0),
					Insn('FADE_OFF', 300, Color(0x00000000)),
					Insn('0x60', 0),
					Insn('0x5A'),
					Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
						0: [
							Insn('CALL', Function((0, 32))),
							Insn('BREAK'),
						],
						1: [
							Insn('TEXT_TALK', Char(10), Text(
								'#14801F是吗……\n'
								'请你们尽快啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('BREAK'),
						],
						None: [],
					}),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14800F我的委托是\n'
						'两个『魔兽之蛋』。{wait}'
						'{page}'
						'#14801F因为我在研制新面包。\n'
						'希望能尽量快一点，\n'
						'还有请对奥斯卡保密哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(14)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'#14812F今、今天真是多谢了。\n'
				'多亏有你们啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(906)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14804F哼哼……这样一来，就能超越\n'
						'奥斯卡那个家伙了……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14810F虽然好像晚了一点……\n'
						'不过先不管这些啦。{wait}'
						'{page}'
						'#14804F哼哼，可恶的奥斯卡……\n'
						'这次我一定会打败你的……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F面包师的修行，\n'
				'请努力加油哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14804F哼哼哼……我的最高杰作\n'
						'总算烤好了。{wait}'
						'{page}'
						'#14802F经过我这一个月的反复研究，\n'
						'终于制作出了这款香气十足的核桃面包！{wait}'
						'{page}'
						'#14807F颤抖吧，奥斯卡！！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14804F哼哼哼……我的最高杰作\n'
						'总算烤好了。{wait}'
						'{page}'
						'#14807F好了，乖乖认输吧，奥斯卡！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 0, 0),
			Insn('TEXT_TALK', Char(254), Text(
				'#14803F（昏昏欲睡）……\n'
				'６２度下……发酵两小时……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14803F我们店被最新一期的\n'
						'克洛斯贝尔时报周刊\n'
						'报道了哦。{wait}'
						'{page}'
						'#14801F可是……介绍的不是我，\n'
						'也不是爸爸，\n'
						'不知为何，竟然是采访奥斯卡。{wait}'
						'{page}'
						'#14806F呜呜，这是为什么啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14801F而且居然还把他称作什么\n'
						'『年轻的天才面包师』……{wait}'
						'{page}'
						'#14807F呜呜，我绝对不承认……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14800F我正在研制新款面包。{wait}'
						'{page}'
						'#14803F这次的面包是用大量的\n'
						'蜂蜜和核桃制成的。{wait}'
						'{page}'
						'#14804F虽然还在研究烤制方法……\n'
						'……哼哼，但这次是胜券在握了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14803F虽然在纪念庆典中的销售量\n'
						'算是平分秋色……{wait}'
						'{page}'
						'#14807F哼哼，走着瞧吧，奥斯卡。\n'
						'这次我绝对会让你彻底败北的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_ROTATE', Char(10), 270, 0),
					Insn('TEXT_TALK', Char(254), Text(
						'#14804F………………………（捏捏）\n'
						'嗯，生面团差不多就是这样了。{wait}'
						'{page}'
						'#14801F这次一定……这次一定要让\n'
						'奥斯卡彻底哑口无言。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14810F为了迎接纪念庆典，\n'
						'我正在制作原创的面包。{wait}'
						'{page}'
						'#14802F……敬、敬请期待吧。\n'
						'我会做出很棒的面包的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 12))),
				]),
				(None, [
					Insn('CHAR_WATCH', Char(10), Char(9), 0),
					Insn('TEXT_TALK', Char(254), Text(
						'#14801F总、总之，我想\n'
						'使用厨房！{wait}'
						'{page}'
						'#14807F借我用一段时间\n'
						'有什么关系嘛！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_ROTATE', Char(10), 90, 0),
					Insn('TEXT_TALK', Char(254), Text(
						'#14805F奇怪，我准备好的\n'
						'高级小麦粉怎么没了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(10), 0, 1900, (44, 47, 150, 1)),
					Insn('SOUND_PLAY', 25, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(254), Text(
						'#14807F又是爸爸。\n'
						'竟然随便动用别人的食材……！{wait}'
						'{page}'
						'#14811F这样一来，\n'
						'不就做不了面包了吗！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14807F我就是讨厌爸爸这一点。\n'
						'总是这么不顾别人……！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14803F做面包的第一步\n'
						'就是挑选食材。{wait}'
						'{page}'
						'#14810F现在有了横跨全大陆的铁路，\n'
						'很容易就能订购到各种食材。{wait}'
						'{page}'
						'#14804F这次就试试奥雷德自治州\n'
						'出产的小麦粉吧……\n'
						'感觉一定能做出好面包呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14813F在、在我看来，\n'
						'我和奥斯卡应该是平分秋色。{wait}'
						'{page}'
						'#14801F我还没有输呢。\n'
						'我要在材料上取胜……！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'#14810F……今天的面包是我烤的。{wait}'
				'{page}'
				'#14802F愿、愿意的话，请去尝尝吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14801F我承认，奥斯卡的确是有才能的。\n'
						'只用了两年的时间，\n'
						'就获得了爸爸的认可。{wait}'
						'{page}'
						'#14803F哼……但这并不\n'
						'意味着我会输给他。{wait}'
						'{page}'
						'#14807F明天我一定要让他哑口无言。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14804F哼哼，奥斯卡，\n'
						'咱们走着瞧吧。{wait}'
						'{page}'
						'#14807F明天一定要让你\n'
						'哑口无言……！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'#14800F……欢迎光临。{wait}'
				'{page}'
				'#14806F我们今天也照常营业哦。\n'
				'面包店是不会休息的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14800F有一天，奥斯卡\n'
						'来到我们店里，\n'
						'说想要做学徒。{wait}'
						'{page}'
						'#14803F然后得到了父亲的同意，\n'
						'之后一直在这里学习……{wait}'
						'{page}'
						'#14801F他现在已经是最有出息的大弟子了。{wait}'
						'{page}'
						'#14807F呜……\n'
						'竟然无视我这个亲生女儿，\n'
						'将他看成大弟子……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14801F我做面包的资历\n'
						'可要比他长多了。{wait}'
						'{page}'
						'#14813F竟然无视我这个亲生女儿，\n'
						'将他看成大弟子……\n'
						'不可原谅……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14800F……欢迎光临。{wait}'
						'{page}'
						'#14800F要结帐的话，请到柜台。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#14800F我们店的新品面包很受欢迎哦。{wait}'
						'{page}'
						'#14813F继承这个特色，负责制作新面包的人，\n'
						'应该是我这个店中的招牌美女才对……\n'
						'（自言自语）……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14813F明明应该是由我来\n'
						'继承制作新品面包的……\n'
						'（自言自语）……{wait}'
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

data['code'][12] = [
	Insn('0x4B', Char(9), -1),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_WATCH', Char(9), Char(10), 0),
	Insn('CHAR_WATCH', Char(10), Char(9), 0),
	Insn('TEXT_TALK', Char(10), Text(
		'#14800F爸爸，你偶尔也\n'
		'到店面看看如何？{wait}'
		'{page}'
		'#14803F最近你老是\n'
		'待在厨房里啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'哼，小丫头懂什么。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'那当然是因为\n'
		'奥斯卡一表人才！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'比你不修边幅的老爸我受欢迎多了～丅\n'
		'自从他来了之后，\n'
		'女性客人也增加了不少呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(10), 0, 1700, (14, 15, 250, 2)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(10), Text(
		'#14806F唔，爸爸他一直\n'
		'都是这个样子……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(9), -1),
	Insn('0x4C', Char(10), -1),
	Insn('FLAG_SET', Flag(1)),
	Insn('FLAG_SET', Flag(2)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'贝奈特小姐\n'
				'刚才是怎么了？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'突然就冲了出去……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天烤出来的\n'
				'面包好香啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'啊啊，好想尝尝啊……\n'
				'是不是这次的新品面包呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我买了这家店的面包\n'
						'给爸爸妈妈吃。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'然后问他们想不想每天都吃，\n'
						'他们竟然默认了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，很成功呢！\n'
						'这样就能经常来面包店了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'嗯～这个月的\n'
						'新品是奶油面包啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'好像也很好吃呢……\n'
						'正好刚刚烤好，\n'
						'配一杯咖啡来尝尝看吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我经常来面包店的事，\n'
						'被爸爸和妈妈发现了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'他们两个都很死板，\n'
						'说绝对不许在外面吃东西。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哼～这有什么不好嘛！\n'
						'这里的面包真的很好吃啊～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'再这样下去，\n'
						'零用钱也会被停掉的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'爸爸和妈妈都很顽固呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'纪念庆典和朋友一起玩，\n'
				'真是很开心呢～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……但是琪露露\n'
				'好像又要出去旅行了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'真是个不爱待在城市里的人啊～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'明明和朋友约好了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'结果却没有来……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'琪露露到底在做什么啊？\n'
						'明明说好要在面包店碰面的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'真是的……她该不会是\n'
						'把约会给忘记了吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'（……奥斯卡今天\n'
						'\u3000多送给我一个面包呢！）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'（说是谢谢我平时\n'
						'\u3000一直来光顾。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'（心跳加速……\n'
						'\u3000呼，真是吓了一跳……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'（因为奥斯卡\n'
						'\u3000很帅嘛。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'（如、如果是常客，\n'
						'\u3000就会得到很多优惠呢。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'（嗯，从明天开始，我要天天过来。）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我和朋友约好了\n'
						'在纪念庆典期间要一起逛逛……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但她到底能不能按时赶回来呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'平时总爱说些什么『对人类没兴趣』，\n'
						'所以很让人担心啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'琪露露真的能在纪念庆典期间\n'
						'赶回来吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'应该不会忘记约定，\n'
						'跑去很远的国家吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'琪露露真是的，\n'
						'好像又出去旅行了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这次又想去哪里呢？\n'
						'本来还想和她一起尝尝新面包的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'琪露露真是个怪人呢。\n'
						'这次又想去哪里啊？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊，这个月的新款面包出了！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这家店的新款面包\n'
						'实在是太美味了。\n'
						'所以我总是忍不住过来买～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……要对我爸爸和妈妈保密哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呼……最近都快成为\n'
						'这里的常客了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但是真的很美味啊。\n'
						'这也是没办法的～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'奥斯卡挺英俊的呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'容姿端正，很帅气啊。\n'
						'而且一直都很开朗从容……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'总觉得他做面包师\n'
						'有点浪费了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不对，就算做面包师\n'
						'也很帅气啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F（……奥斯卡这家伙，\n'
						'\u3000一直都很受欢迎呢。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'奥斯卡很帅呢，{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'总觉得他做面包师\n'
						'有点浪费了……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'鸡蛋三明治和牛角面包……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，再买个甜甜圈带回去吧。\n'
						'做点心正好呢㈱{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'啊，但是会不会买得太多了……\n'
						'可是又好想吃点心啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'那边的面包是刚刚出炉的，\n'
						'这边又是限时销售的新品……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，真不知该怎么选择啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我的朋友很奇怪吧～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'只要有空就会出去旅行。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我今天也来找她玩，\n'
						'但她都已经出门了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'琪露露真是的，\n'
						'又出去旅行了啊。\n'
						'今天又见不到她了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，真没办法，\n'
						'今天买完面包就回去吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_ROTATE', Char(254), 0, 0),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯嗯，这个月的新款面包……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'有脆皮培根的\n'
						'香辣面包……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'唔……而且还是刚烤好的。\n'
						'看起来很好吃啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'这家面包店\n'
						'好像每个月都有新品呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，看上去真好吃……\n'
						'……实在忍不住了，\n'
						'还是买一个带回家吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'哇～好帅的\n'
						'面包师啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我本来是到西侧大道\n'
						'来和朋友见面的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'顺道就发现了\n'
						'这家不错的店㈱{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'这家面包店的\n'
						'氛围很棒呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，我很喜欢哦，\n'
						'要不要买个面包带回家呢？{wait}'
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

data['code'][14] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天必须要回国了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'得多买一些\n'
				'特产带回去。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'不然就在露天座位区，\n'
				'配上咖啡一起享用吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'逛庆典的时候，\n'
				'发现了这家不错的店。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，都是些看起来\n'
				'就很美味的面包呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'庆典的游行队伍\n'
				'也已经参观过了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'接下来，就悠闲地\n'
				'在街上随便逛逛吧～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我取消了饭店的餐点服务，\n'
				'跑到这里来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'还是在街上吃东西\n'
				'更有庆典的节日气氛呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔市实在很大啊，\n'
						'我都走累了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'爸爸总是一个人\n'
						'走得飞快。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'干脆在这家面包\n'
						'咖啡店休息一下好了。{wait}'
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
	Insn('CALL', Function((0, 17))),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('TEXT_START', Char(15)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 46, Insn('TASK_GET', 1))), Insn('EXEC', Insn('QUEST_GET', 46, Insn('TASK_GET', 3))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 46, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 33))),
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
				Insn('IF', [
					(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
						Insn('OPEN_SHOP', 47),
					]),
					(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
						Insn('OPEN_SHOP', 46),
					]),
					(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
						Insn('OPEN_SHOP', 45),
					]),
					(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
						Insn('OPEN_SHOP', 44),
					]),
					(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
						Insn('OPEN_SHOP', 43),
					]),
					(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
						Insn('OPEN_SHOP', 42),
					]),
					(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
						Insn('OPEN_SHOP', 41),
					]),
					(None, [
						Insn('OPEN_SHOP', 40),
					]),
				]),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), []),
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
				Insn('IF', [
					(Expr([Insn('EXEC', Insn('QUEST_GET', 46, Insn('TASK_GET', 4))), Insn('EXEC', Insn('QUEST_GET', 46, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1792)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
						Insn('TEXT_TALK', Char(15), Text(
							'哦，你们好像已经\n'
							'采到利奎姆之花了啊。{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(15), Text(
							'让你们费心了，真不好意思。\n'
							'稍后必须要去向昆特先生\n'
							'好好道歉才行。{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(Expr([Insn('EXEC', Insn('QUEST_GET', 46, Insn('TASK_GET', 3))), Insn('EXEC', Insn('QUEST_GET', 46, Insn('TASK_GET', 4))), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1792)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
						Insn('TEXT_TALK', Char(15), Text(
							'进入位于山道的隧道后，\n'
							'途中折向通往遗迹的岔路，\n'
							'利奎姆之花应该就开在那条路的某处。{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(15), Text(
							'路上小心点吧。{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(Expr([Insn('FLAG', Flag(1280)), Insn('NOT'), Insn('FLAG', Flag(1024)), Insn('BOOL_AND'), Insn('FLAG', Flag(1190)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
						Insn('TEXT_TALK', Char(15), Text(
							'我家的小桃很喜欢看书呢。\n'
							'最近好像在看\n'
							'一部娱乐小说。{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(15), Text(
							'不过，好像只得到了\n'
							'其中的几卷……{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(15), Text(
							'因为看她一脸失落，\n'
							'就忍不住进了几本到店里。{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(15), Text(
							'哈哈，有兴趣的话，\n'
							'你们也看看吧。\n'
							'虽然只有几卷而已。{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('FLAG_SET', Flag(1190)),
					]),
					(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
						Insn('TEXT_TALK', Char(15), Text(
							'小桃今天回家的时候，好像都快要哭出来了……{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(15), Text(
							'发生了什么事吗？{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
						Insn('TEXT_TALK', Char(15), Text(
							'听说最近有很多人失踪，是真的吗？{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(15), Text(
							'难道是……人口贩子吗？{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(15), Text(
							'好可怕啊……\n'
							'一会要提醒小桃留意点。{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(15), Text(
									'我家的小桃，最近\n'
									'好像开始和朋友一起玩了。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'她终于克服害羞内向的毛病了啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'虽然最近听说了一些\n'
									'可怕事件的传闻……\n'
									'但这件事还是让我稍微觉得好过了一点。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(5)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'虽然最近听说了一些可怕的传闻，\n'
									'不过能看到孩子的笑容，比什么都重要啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'希望能早日恢复和平呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(15), Text(
									'哟，欢迎光临。\n'
									'欢迎来到塔里兹商店。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'……最近到处都能听到\n'
									'关于鲁巴彻的传闻。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'比如他们又在市区里\n'
									'引起了什么纠纷……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'我们家也有小孩子，\n'
									'所以得注意一点呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(5)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'和我有来往的商人之中，\n'
									'好像也有被鲁巴彻找过麻烦的人。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'好可怕啊……我家也有小孩子，\n'
									'必须得小心点啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(15), Text(
									'哎呀哎呀，终于能恢复到\n'
									'正常的生活了。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'连续闹了五天，还真想享受一下\n'
									'悠闲的时光啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'虽然爱尔莎\n'
									'听了之后就对我说：\n'
									'『你不是一直很悠闲吗』。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(5)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'纪念庆典结束之后，\n'
									'感觉终于回到了正常的生活。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'嗯，果然还是安宁平静的日子最棒了。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(15), Text(
									'爱尔莎和小桃\n'
									'去了米修拉姆哦。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'我对她们说，\n'
									'要玩得尽兴一点。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'她们总在店里帮忙，\n'
									'偶尔也得休息一下呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(5)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'爱尔莎和小桃现在\n'
									'应该已经去了米修拉姆。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'虽然店里忙翻了……\n'
									'不过只有今天的话，还是能撑过去的。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1303)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(15), Text(
									'对了，今天是\n'
									'游行的日子。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'唔，糟了。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'我对这种活动没什么兴趣，\n'
									'所以都没注意\n'
									'庆典的日程。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(5)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'今天可是游行的日子啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'希望爱尔莎和小桃\n'
									'能玩得尽兴。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1294)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(1387)), Insn('NOT'), Insn('END')]), [
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
								Insn('TEXT_TALK', Char(15), Text(
									'走丢的孩子啊……\n'
									'那情况还真是紧急呢……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'唔，我错过\n'
									'游行了。\n'
									'只看到了一点点……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'而且还是远远地眺望了一下，\n'
									'所以没看太清楚啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(257), Text(
									'#0000F这样啊……\n'
									'谢谢您了。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(1387)),
								Insn('0xD0', 2, Expr([Insn('0x23', 2), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
								Insn('CALL', Function((0, 25))),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'我错过游行了呢，\n'
									'只是远远地眺望了一下。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'所以不知道那个孩子\n'
									'到底有没有出现过。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(15), Text(
									'对了，今天是\n'
									'游行的日子。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'唔，糟了。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'我对这种活动没什么兴趣，\n'
									'所以都没注意\n'
									'庆典的日程。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(5)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'今天可是游行的日子啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'希望爱尔莎和小桃\n'
									'能玩得尽兴。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(15), Text(
									'爱尔莎和小桃\n'
									'现在正在街上逛着呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'因为机会难得，所以我\n'
									'就让她们出去逛一圈。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'虽然我还要看店，但至少希望家人能\n'
									'玩得开开心心。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(5)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'毕竟是难得的庆典，\n'
									'希望家人能够玩得开心点。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(15), Text(
									'虽然是纪念庆典，\n'
									'但我并没打算\n'
									'做什么特别的事……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'今年的庆典\n'
									'办得很隆重啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'唔，我们店里\n'
									'是不是也该办点活动呢？{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(5)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'我们店是不是也该\n'
									'办个大减价之类的活动啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'哈哈……那样的话，可真是\n'
									'迟来的优惠呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(15), Text(
									'克洛斯贝尔自治州到今年\n'
									'也创立７０周年了啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'算起来……它正好是在\n'
									'我爷爷年轻的时候\n'
									'诞生的呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'这样想的话，\n'
									'真让人有点感慨啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(5)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'平时都不太会\n'
									'去想自治州的事情……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'但仔细想想的话，\n'
									'还真是让人感慨啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(15), Text(
									'我和布里吉塔\n'
									'刚才在聊那条警犬的事。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'刚刚还来过我家……\n'
									'不知道又去哪里了……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(5)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'那条警犬\n'
									'不知道又去哪里了……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'它好像总在这附近\n'
									'给我们巡逻呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
										Insn('TEXT_TALK', Char(15), Text(
											'啊、啊哈哈……\n'
											'真是条大狗呢……{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(15), Text(
											'对了，最近客人们常议论的\n'
											'就是那条警犬啊……{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('FLAG_SET', Flag(5)),
									]),
									(None, [
										Insn('TEXT_TALK', Char(15), Text(
											'看起来的确是条\n'
											'很可靠的警犬……\n'
											'但感觉它的架子很大呢。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(15), Text(
											'刚刚和它打招呼，\n'
											'竟然只哼了一声当作回应。{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
								]),
							]),
							(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(15), Text(
									'那条警犬每周\n'
									'会来我们店里两三次。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'刚刚虽然也来过……\n'
									'但不知道又去哪里了……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(5)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'那条警犬\n'
									'不知道又去哪里了……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'它好像总在这附近\n'
									'给我们巡逻呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
						Insn('TEXT_TALK', Char(15), Text(
							'爱尔莎一直在说\n'
							'彩虹剧团的事。{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(15), Text(
							'唔，果然是\n'
							'很想去看吧。{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(15), Text(
							'虽然她很少提起，\n'
							'不过她从以前开始就很向往\n'
							'彩虹剧团呢。{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
						Insn('TEXT_TALK', Char(15), Text(
							'哈罗德先生家里\n'
							'好像也有小孩啊。{wait}'
						)),
						Insn('TEXT_WAIT'),
						Insn('TEXT_TALK', Char(15), Text(
							'他们和我们家一样，\n'
							'从事家族经营式的买卖。\n'
							'总觉得很有亲切感啊。{wait}'
						)),
						Insn('TEXT_WAIT'),
					]),
					(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(15), Text(
									'哈罗德先生说，\n'
									'这次蜂蜜的价格确定之后，\n'
									'他就会来通知我。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'真是很诚恳啊。\n'
									'身为店主我也很高兴呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'到时候顺便谈谈\n'
									'下次进货的事情吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(5)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'我和哈罗德先生\n'
									'也有三年的交情了，\n'
									'他真是个很诚恳的人啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'到时候顺便谈谈\n'
									'下次进货的事情吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(15), Text(
									'最近都没有看见过\n'
									'龙和安里呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'平时经常会在\n'
									'我们店门口玩……\n'
									'到底去哪里了呢？{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(5)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'最近都没有看见过\n'
									'龙和安里呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'我记得龙应该是\n'
									'住在贝尔海姆的。\n'
									'是不是生病了，在家睡觉休息呢？{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(15), Text(
									'有位商人会从阿尔摩利卡村\n'
									'帮我们批发蜂蜜。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'由于最近的行情很不错，\n'
									'对方就来通知我说\n'
									'价格可能会上涨。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'只要有什么情况，\n'
									'那个人都会事先告诉我。\n'
									'不但有生意头脑，人品也很不错。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(5)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'他总会提早告诉我情报，\n'
									'这点真是让人很感谢啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'因为价格要上涨了，\n'
									'所以我得提前多进点货啊。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(534)), Insn('END')]), [
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
										Insn('TEXT_TALK', Char(15), Text(
											'我家的小桃很怕生呢。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(15), Text(
											'一有客人来，\n'
											'她就会躲到里面去。\n'
											'唔，真拿她没办法啊。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('FLAG_SET', Flag(5)),
									]),
									(None, [
										Insn('TEXT_TALK', Char(15), Text(
											'我家的小桃很怕生呢。{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
								]),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'我们这里是杂货店，\n'
									'贩卖食材和日用品。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'我进的都是一些\n'
									'能给大家带来便利的商品，\n'
									'不嫌弃的话请看看吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
						]),
					]),
					(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
						Insn('IF', [
							(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
								Insn('TEXT_TALK', Char(15), Text(
									'哟，欢迎光临。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'想买日用品就来我这里吧！\n'
									'我们是招牌老店『塔里兹商店』～{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'顺便一提，『悠闲地生活吧』\n'
									'就是我们的口号。\n'
									'请随便看看吧。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FLAG_SET', Flag(5)),
							]),
							(None, [
								Insn('TEXT_TALK', Char(15), Text(
									'我们的口号就是\n'
									'『悠闲地生活吧』。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(15), Text(
									'如你所见，这里的气氛悠闲轻松，\n'
									'请随便看看吧。{wait}'
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
	Insn('TEXT_END', Char(15)),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'小桃真是的……\n'
						'今天和朋友们发生什么事了？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'一直在闹别扭，\n'
						'都不和我说话。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'孩子之间总会产生\n'
						'各式各样的问题啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'做点好吃的东西，\n'
						'去安慰安慰她吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'伊安律师最近好像很忙啊……\n'
						'手头似乎有很多工作。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'助手彼特也很辛苦呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我丈夫说过，\n'
						'最近的事件好像增加了不少，\n'
						'大概就是这个原因吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'伊安律师和彼特都很辛苦啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……我刚刚看了看外面，\n'
						'发现小桃在和朋友们一起玩呢～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那个害羞内向的孩子也开始改变了……\n'
						'身为母亲，我真是很高兴啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'今天晚上就煮\n'
						'红豆糯米饭吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'小桃终于有所改变了啊～\n'
						'我和丈夫都在暗地里高兴呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'今晚可要好好庆祝一下。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天有新商品送来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'因为价格有点贵，\n'
				'所以摆放的时候要小心一点。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'小桃也会来帮忙，\n'
						'她很懂事，真是帮了大忙呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过……她总是\n'
						'在店里帮忙，\n'
						'要不然就一个人看书。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'如果偶尔也能去\n'
						'外面玩玩就好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'虽然给店里帮忙\n'
						'是件好事……\n'
						'不过，小桃真的觉得开心吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'事实上，\n'
						'她或许也想去外面玩玩呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'马上就要到创立纪念庆典了～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但是我丈夫好像没兴趣\n'
						'搞大减价之类的活动。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呼，对这类节日庆典毫无兴趣，\n'
						'倒真是很符合他的个性。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'话说回来……\n'
						'感觉下面很安静呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我丈夫他，\n'
						'不会是在打瞌睡吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'彩虹剧团的新剧，\n'
						'好像会有新演员参加演出呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'而且刚刚出道，\n'
						'就和那个大明星伊莉雅小姐同台表演。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'感觉好厉害啊……\n'
						'到底是个什么样的人呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔的女孩子们\n'
						'都曾憧憬过彩虹剧团。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'出道作就能和伊莉雅小姐\n'
						'同台表演……\n'
						'真是像梦幻般幸运呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'小桃今天去主日学校上课了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'那孩子相当害羞内向，\n'
				'我有点担心\n'
				'她是否能融入集体。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'以后有空时，我去找修女\n'
				'问问上课时的情况吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('0x4B', Char(21), -1),
			Insn('CHAR_ROTATE', Char(254), 180, 0),
			Insn('TEXT_TALK', Char(254), Text(
				'不不，我才是\n'
				'一直受您的照顾。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'那么，\n'
				'下个月的采购\n'
				'就按照这个方案吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(21), Text(
				'#3603F食材增加一成。\n'
				'嗯，但希望价格能优惠点吗……{wait}'
				'{page}'
				'#3600F哈哈哈，请包在我身上吧。\n'
				'塔里兹先生\n'
				'是老客户了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x4C', Char(21), -1),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我刚才去中央广场\n'
						'买东西……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'结果发现旁边那幢旧大楼\n'
						'不知何时搬进了一家\n'
						'不知名的公司。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'到底是什么时候搬进去的呢？\n'
						'完全没有注意到啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0305F（……是在说支援课的那栋楼吧？）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0012F（哈哈……知名度果然还\n'
						'\u3000差得远呢……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'中央广场边缘的那栋大楼，\n'
						'不知在何时，搬进了\n'
						'一家不知名的公司。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那一带的变化\n'
						'相当频繁呀。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'做菜做菜……丅{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'卖剩的蔬菜不会扔掉，\n'
				'而是我们自家吃掉呢。\n'
				'很能省钱吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呜呜，龙\n'
				'果然很爱捉弄人……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1390)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'纪念庆典最后一天，\n'
						'我和龙一起去逛了露天店。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'庆典我过得好开心啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'要是再能一起玩就好了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(339), 0, 1700, (0, 1, 250, 2)),
					Insn('SOUND_PLAY', 29, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(339), Text(
						'#1110F庆典～？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(254), 0, 1700, (2, 7, 80, 1)),
					Insn('SOUND_PLAY', 28, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('EMOTE', Char(254), 0, 1700, (40, 43, 100, 0)),
					Insn('SLEEP', 1000),
					Insn('CHAR_WATCH', Char(254), Char(339), 500),
					Insn('EMOTE_STOP', Char(254)),
					Insn('TEXT_TALK', Char(254), Text(
						'不、不……\n'
						'没、没什么……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那个，庆典和朋友一起玩了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'非常开心呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(339), Text(
						'#1105F嗯，真不错呢……{wait}'
						'{page}'
						'#1109F喂，罗伊德，\n'
						'下次大家也一起去庆典玩吧～？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('EMOTE', Char(239), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F说、说得也是……\n'
						'这提议不坏呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
							Insn('TEXT_TALK', Char(258), Text(
								'#0100F不过要等明年了。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
							Insn('TEXT_TALK', Char(259), Text(
								'#0202F但是要到明年了。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
							Insn('TEXT_TALK', Char(260), Text(
								'#0300F不过也只能等到明年啦。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, []),
					]),
					Insn('FLAG_SET', Flag(1390)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'纪念庆典最后一天，\n'
						'我和龙一起去逛了露天店。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'庆典我过得好开心啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'要是再能一起玩就好了……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呜呜……我要休息了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'因为和客人说话\n'
				'很累嘛……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嘿嘿嘿，狗狗\n'
				'好可爱啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'以后还想再和它玩，\n'
				'它还会和我玩吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 21, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'嘿嘿嘿，狗狗\n'
						'好可爱啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'以后还想再和它玩，\n'
						'它还会和我玩吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_ROTATE', Char(254), 180, 0),
					Insn('TEXT_TALK', Char(254), Text(
						'（摸摸）……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(254), Char(0), 500),
					Insn('TEXT_TALK', Char(254), Text(
						'嘿嘿嘿，狗狗\n'
						'好像感觉很舒服哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('CHAR_ROTATE', Char(254), 180, 0),
					Insn('TEXT_TALK', Char(254), Text(
						'（摸摸）……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'狗狗，好可爱啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 90, 0),
			Insn('TEXT_TALK', Char(254), Text(
				'（忙忙碌碌）……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_WATCH', Char(254), Char(0), 500),
			Insn('TEXT_TALK', Char(254), Text(
				'新商品到货了，\n'
				'所以要摆放起来。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'瓶子的标签要擦干净，\n'
				'让大家都能看到。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'龙说他被一只\n'
						'很大的狗狗救了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真好啊……\n'
						'小桃也想玩……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不、不行……\n'
						'不能在路上玩。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'会有导力车经过的，\n'
						'所以不能在路上玩。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'龙，一定要\n'
						'好好听大人的话才行……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(534)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(254), Text(
								'……我不太擅长和彼特相处。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'之前他对我发火，\n'
								'让我『把话说得\n'
								'更清楚些』……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(7)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(254), Text(
								'彼特虽然人很好，但我就是不擅长和他相处……{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'龙、安里，\n'
						'我们一起玩吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#2S我、我们一起玩吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……为了到时候不紧张，\n'
						'要多练习几次。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我、我们一起玩吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……要是能说出口就好了……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'龙和安里，\n'
				'一直都很开心啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'小桃也想和他们一起玩……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'伊安律师最近很忙，\n'
						'教我学习法律知识的时间\n'
						'都减少了很多。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但是，看着伊安律师工作时的样子，\n'
						'我也有种自豪感。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我也想早日学成，\n'
						'帮上伊安律师的忙。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(8)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'真希望能早日成为合格的律师，\n'
						'帮上伊安律师的忙。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'说起伊安律师，\n'
				'他午饭就只喝一杯咖啡了事，\n'
				'不注重健康也要有个限度啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'所以我要\n'
				'为他准备好食物才行。{wait}'
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
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我丈夫从早上开始，\n'
						'就在事务所里坐立不安的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，因为我丈夫一直\n'
						'对那栋大楼有特殊感情呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(9)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我丈夫从一大早\n'
						'就开始坐立不安的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，得早点回去呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'那条传说中的狗，\n'
						'好像刚刚还来过\n'
						'塔里兹先生这里。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真遗憾，\n'
						'我也想见见它啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(9)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'塔里兹先生说，\n'
						'它好像偶尔会过来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，明天\n'
						'要更早一点\n'
						'过来看看啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我之前和小桃打了个招呼，\n'
						'但她扭扭捏捏地逃到楼上去了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'小桃她\n'
						'一直都很怕生啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(9)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我小的时候\n'
						'也很不擅长与人交往……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'所以就会忍不住\n'
						'和小桃打招呼呢。{wait}'
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

data['code'][22] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(10)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'#1200F呜噜噜噜噜…………{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F赛特，今天\n'
				'竟然在这种地方啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F这家伙完全变成大明星了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(10)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'#1200F呜噜噜噜噜…………{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(876)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(11)), Insn('END')]), [
					Insn('TEXT_TALK', Char(21), Text(
						'#3600F各位，请加油啊，\n'
						'我也会在心里默默支持你们的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(21), Text(
						'#3600F各位，请加油啊，\n'
						'我也会在心里默默支持你们的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F（有人支援的话，\n'
						'\u3000就会干劲十足呢……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F（嗯嗯，我也深有感触啊。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(11)),
				]),
			]),
		]),
		(None, [
			Insn('EMOTE', Char(21), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(21), Text(
				'#3600F哦，大家好……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F啊，是哈罗德先生……{wait}'
				'{page}'
				'莫非在谈生意吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(21), Text(
				'#3600F嗯，是的。\n'
				'塔里兹先生一直\n'
				'都很关照我的生意。{wait}'
				'{page}'
				'他经常从我这里\n'
				'进一些商品呢。{wait}'
				'{page}'
				'各位是……\n'
				'还在调查那个魔兽事件吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F嗯，昨天\n'
				'还没有把事情解决。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F现在正要\n'
				'赶去玛因兹呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(21), Text(
				'#3600F真是辛苦啊……{wait}'
				'{page}'
				'各位，请加油啊，\n'
				'我会在心里默默支持你们的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(876)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(12)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#08700F哎呀，午安。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F艾欧莉雅小姐，\n'
						'竟然会在这种地方相遇，\n'
						'真是少见啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#08702F这家店的面包\n'
						'最近很受欢迎。{wait}'
						'{page}'
						'#08709F我一直在这里\n'
						'买午饭呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(12)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#08705F说起来，\n'
						'刚刚有个人来协会了，\n'
						'好像是林的前辈呢。{wait}'
						'{page}'
						'#08704F她们两个现在到\n'
						'『龙老饭店』吃午饭去了……\n'
						'不知道聊得愉不愉快呢。{wait}'
						'{page}'
						'#08711F呵呵，看来好像是久别重逢，\n'
						'所以还是不要打扰她们比较好。{wait}'
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

data['code'][25] = [
	Insn('IF', [
		(Expr([Insn('0x23', 2), Insn('CONST', 5), Insn('EQ'), Insn('END')]), [
			Insn('QUEST', 70, Insn('TASK_SET', 11)),
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F（这样一来，西侧大道\n'
				'\u3000也都调查过了……）{wait}'
				'{page}'
				'#0003F（……不知大家的\n'
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

data['code'][26] = [
	Insn('EVENT_BEGIN', 0),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu08300.itp'),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x4B', Char(8), -1),
	Insn('CAM_OFFSET', (52500, 1500, 0), 0),
	Insn('CAM_ROTATE', 45, 22, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 27000, 0),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 27))),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('CAM_DISTANCE', 26000, 1500),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('SLEEP', 300),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('CHAR_WATCH', Char(257), Char(8), 500),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F#1P哟，奥斯卡！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 28))),
	Insn('EMOTE', Char(8), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 300),
	Insn('TEXT_SET_NAME', Translate('奥斯卡')),
	Insn('TEXT_MESSAGE', Char(8), Text(
		'哎呀，这不是罗伊德嘛！{wait}'
		'{page}'
		'哈哈哈！\n'
		'你这家伙终于来见我了啊！{wait}'
		'{page}'
		'好久不见了啊。\n'
		'嗯，有一年了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#0006F……那个。\n'
		'我们都已经有三年没见面了吧？{wait}'
		'{page}'
		'你这方面还真是一点都没变，\n'
		'总是这么粗枝大叶……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14709F哇哈哈！\n'
		'我们一直都在通信啊，\n'
		'所以感觉没有分别那么久。{wait}'
		'{page}'
		'#14702F你好像长高了很多啊，\n'
		'不过还是一副娃娃脸。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0011F唔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F哈哈。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F嘻嘻……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F看起来，好像是\n'
		'罗伊德前辈的朋友吧……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14702F嗯，我叫奥斯卡。\n'
		'是这家面包店『摩尔吉』的\n'
		'见习面包师。{wait}'
		'{page}'
		'#14700F你们是……\n'
		'罗伊德的同事吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F嗯，我是兰迪。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F我叫艾莉，请多指教。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F……我叫缇欧丄普拉托。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14709F哦哦，请多指教啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#0003F（我们也没有穿制服啊，\n'
		'\u3000竟然能看出我们是同事……）{wait}'
		'{page}'
		'（他还是老样子，真不知\n'
		'\u3000该算是直觉敏锐还是粗枝大叶……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14705F怎么了，你的表情很奇怪哦。{wait}'
		'{page}'
		'#14700F对了，罗伊德。\n'
		'你还在做料理吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F哎，嗯……{wait}'
		'{page}'
		'#0000F算是在做吧，我在叔叔家里\n'
		'也会帮忙做家务，总会做一点。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14702F那么，作为再会的纪念，\n'
		'这东西就送给你吧。{wait}'
		'{page}'
		'#14700F希望能对你有帮助。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'获得了{item 2}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 2, 1),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('RECIPE', 13)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(8), Text(
				'#14700F还有，既然机会难得……\n'
				'我来教你三明治的做法吧。{wait}'
				'{page}'
				'#14702F这很简单，最适合用来练习了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FADE_ON', 300, Color(0x00000000), 100),
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('SOUND_PLAY', 17, 0, 0, 100),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'学习了{item 437}{color 0}的做法。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'记住了{item 437}{color 0}的食谱。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('0x5A'),
			Insn('RECIPE', 13),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F谢、谢啦。{wait}'
				'{page}'
				'#0000F……呵，这东西倒挺有趣啊。\n'
				'竟然还能记录\n'
				'食谱的各种变化。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#14700F嗯，因为可以大家共用，\n'
				'所以有各式各样的使用方法。{wait}'
				'{page}'
				'#14702F你们也多尝试一下吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('0x5A'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F谢、谢啦。{wait}'
				'{page}'
				'#0000F……呵，这东西倒挺有趣啊。\n'
				'竟然还能记录\n'
				'食谱的各种变化。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#14700F嗯，因为可以大家共用，\n'
				'所以有各式各样的使用方法，\n'
				'你们也多尝试一下吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(258), Text(
		'#0105F说、说得也是呢……{wait}'
		'{page}'
		'#0104F不过，至今为止，\n'
		'我也只制作过点心之类的东西……{wait}'
		'{page}'
		'#0100F兰迪和缇欧呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0303F唔……\n'
		'我只擅长做那些只要\n'
		'煮煮烧烧就能搞定的野外料理。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F如果是那种可以按照流程制作的料理，\n'
		'我大概没问题……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F哈哈，要是有兴趣的话，\n'
		'我也可以教你们哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}※和不同的人交谈，或调查一些特定的场所，\n'
		'\u3000就有机会得到各种『食谱』。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}※『食谱』会被记录在『料理手册』中。\n'
		'\u3000只要使用『料理手册』，随时都可以\n'
		'\u3000制作各种效果不同的料理。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}※此外，做出的料理还有一定的概率会成为\n'
		'\u3000『大成功』料理或『预料之外』料理。\n'
		'\u3000（同时，料理也有『制作失败』的可能。）{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}※制作料理所需要的『食材』，\n'
		'\u3000可以在杂货店之类的商店中购得。\n'
		'\u3000此外，一些魔兽有时也会掉落。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('CHAR_SET_POS', Char(0), (53750, 0, 2000), 90),
	Insn('0x4C', Char(8), -1),
	Insn('0x0A', 268435456),
	Insn('FLAG_SET', Flag(561)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('CHAR_SET_POS', Char(257), (47500, 0, 0), 90),
	Insn('CHAR_SET_POS', Char(258), (46350, 0, -500), 90),
	Insn('CHAR_SET_POS', Char(259), (46450, 0, 750), 90),
	Insn('CHAR_SET_POS', Char(260), (45250, 0, 250), 90),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('FORK', 257, 1, [
		Insn('0x98', Char(257), (5000, 0, 0), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x98', Char(259), (5000, 0, 0), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x98', Char(258), (5000, 0, 0), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('0x98', Char(260), (5000, 0, 0), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(257), Color(0xFFFFFFFF), 1000),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 2, [
		Insn('CHAR_SET_COLOR', Char(259), Color(0xFFFFFFFF), 1000),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 2, [
		Insn('CHAR_SET_COLOR', Char(258), Color(0xFFFFFFFF), 1000),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 2, [
		Insn('CHAR_SET_COLOR', Char(260), Color(0xFFFFFFFF), 1000),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('RETURN'),
]

data['code'][28] = [
	Insn('CAM_OFFSET', (54000, 1500, 2000), 3000),
	Insn('CHAR_WATCH', Char(8), Char(257), 500),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(257), (53750, 0, 2000), 1500, 0),
	]),
	Insn('SLEEP', 210),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(259), (52800, 0, 2750), 1400, 0),
	]),
	Insn('SLEEP', 280),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(258), (52700, 0, 1500), 1600, 0),
	]),
	Insn('SLEEP', 140),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(260), (51500, 0, 2250), 1500, 0),
	]),
	Insn('SLEEP', 300),
	Insn('CHAR_WATCH', Char(8), Char(257), 500),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(257), 90, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(259), 90, 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(258), 90, 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(260), 90, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'\x01'),
	Insn('RETURN'),
]

data['code'][29] = [
	Insn('EVENT_BEGIN', 0),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu08300.itp'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (53470, 1500, 1600), 0),
	Insn('CAM_ROTATE', 36, 20, 0, 0),
	Insn('0x6E', 420, 0),
	Insn('CAM_DISTANCE', 20740, 0),
	Insn('CHAR_SET_POS', Char(257), (53650, 0, 1940), 90),
	Insn('CHAR_SET_POS', Char(258), (52230, 0, 1940), 90),
	Insn('CHAR_SET_POS', Char(259), (53650, 0, 520), 90),
	Insn('CHAR_SET_POS', Char(260), (52230, 0, 520), 90),
	Insn('CHAR_ROTATE', Char(8), 270, 0),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 300),
	Insn('TEXT_SET_NAME', Translate('奥斯卡')),
	Insn('TEXT_MESSAGE', Char(8), Text(
		'#11P哟，罗伊德，\n'
		'今天也来了啊。{wait}'
		'{page}'
		'#11P哇哈哈，要不要吃点面包啊？{wait}'
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
		'#5P#0006F这种时候，该说的并不是什么\n'
		'『要不要吃点面包』吧……？{wait}'
		'{page}'
		'#0000F奥斯卡，你不是向支援课\n'
		'提出委托了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14705F#11P哎，有这种事吗？{wait}'
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
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0200F支援课这里的确\n'
		'是收到了委托……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0003F拜托，奥斯卡……\n'
		'我们是为工作而来的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14705F#11P哦，对了，我想起来啦。{wait}'
		'{page}'
		'#14704F#11P我就是想让你们帮我\n'
		'收集用于制作新品面包的食材。{wait}'
		'{page}'
		'#14700F#11P其实，我拜托的商家\n'
		'好像因故而延迟送货了。\n'
		'所以材料似乎有些不足。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#6P#0300F原来如此，所以你才\n'
		'希望我们帮忙收集食材啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#6P#0100F的确，没有食材的话，\n'
		'就做不成面包了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14700F#11P就是这样，\n'
		'你们愿意接受吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0000F嗯，只是收集食材的话，\n'
		'就交给我们吧。{wait}'
		'{page}'
		'那么……具体需要\n'
		'什么食材呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14704F#11P这个嘛，小麦粉和奶油\n'
		'倒是没问题……{wait}'
		'{page}'
		'#14700F#11P我希望你们收集的是\n'
		'四个『魔兽鱼肉』\n'
		'和三个『魔兽之蛋』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#6P#0304F嗯，这两种东西的话，\n'
		'只要出了城，都能轻松弄到呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0000F明白了，我们处理其它任务时\n'
		'顺便收集一下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 80, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}任务【收集食材的委托】{color 0}开始！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x4C', Char(8), -1),
	Insn('CHAR_SET_POS', Char(0), (53210, 0, 1200), 90),
	Insn('CHAR_SET_POS', Char(1), (53210, 0, 1200), 90),
	Insn('CHAR_SET_POS', Char(2), (53210, 0, 1200), 90),
	Insn('CHAR_SET_POS', Char(3), (53210, 0, 1200), 90),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG2_UNSET', Char(11), 32768),
	Insn('QUEST', 6, Insn('TASK_SET', 0)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][30] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (53470, 1500, 1600), 0),
	Insn('CAM_ROTATE', 36, 20, 0, 0),
	Insn('0x6E', 420, 0),
	Insn('CAM_DISTANCE', 20740, 0),
	Insn('CHAR_SET_POS', Char(257), (53650, 0, 1940), 90),
	Insn('CHAR_SET_POS', Char(258), (52230, 0, 1940), 90),
	Insn('CHAR_SET_POS', Char(259), (53650, 0, 520), 90),
	Insn('CHAR_SET_POS', Char(260), (52230, 0, 520), 90),
	Insn('CHAR_ROTATE', Char(8), 270, 0),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0000F嗯，按照你的委托，\n'
		'都拿来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'交给了对方{item 301}{color 0}×４、\n'
		'{item 303}{color 0}×３。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_REMOVE', 301, 4),
	Insn('ITEM_REMOVE', 303, 3),
	Insn('TEXT_TALK', Char(8), Text(
		'#14702F#11P谢啦，这下得救了。\n'
		'罗伊德果然\n'
		'很可靠啊……{wait}'
		'{page}'
		'#14704F#11P呵呵，从以前开始就是这样，\n'
		'每当有困难的时候，你总是来帮我！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#6P#0309F哈哈，罗伊德果然\n'
		'从以前就是这样啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0200F从罗伊德前辈平时有求必应的\n'
		'老好人样子来看，隐约就能察觉到了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#5P#0109F呵呵……这不正是\n'
		'罗伊德的优点嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('CHAR_ROTATE', Char(257), 225, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0003F那个，怎么感觉你们\n'
		'是在说我的坏话？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14709F#11P他们只是在说\n'
		'罗伊德是个好人而已吧。{wait}'
		'{page}'
		'#14705F#11P啊啊，对了，要不要\n'
		'顺便尝尝\n'
		'我烤的面包呢。{wait}'
		'{page}'
		'#14702F#11P今天免费赠送给你们哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 90, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0000F好啊，\n'
		'那我们稍后就挑几个吧。{wait}'
		'{page}'
		'那么，奥斯卡。\n'
		'要努力学习做面包啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#14709F#11P噢，放心吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 9, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}任务【收集食材的委托】{color 0}完成！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x4C', Char(8), -1),
	Insn('CHAR_SET_POS', Char(0), (53210, 0, 1200), 90),
	Insn('CHAR_SET_POS', Char(1), (53210, 0, 1200), 90),
	Insn('CHAR_SET_POS', Char(2), (53210, 0, 1200), 90),
	Insn('CHAR_SET_POS', Char(3), (53210, 0, 1200), 90),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG2_UNSET', Char(11), 32768),
	Insn('QUEST', 6, Insn('FLAG_UNSET', 16)),
	Insn('QUEST', 6, Insn('TASK_SET', 1)),
	Insn('FLAG_SET', Flag(13)),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][31] = [
	Insn('EVENT_BEGIN', 0),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu08310.itp'),
	Insn('CROSSFADE', 800),
	Insn('CAM_OFFSET', (55260, 2500, 12530), 0),
	Insn('CAM_ROTATE', 40, 25, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 29710, 0),
	Insn('CHAR_SET_POS', Char(257), (55190, 1000, 12700), 0),
	Insn('CHAR_SET_POS', Char(258), (55190, 1000, 11280), 0),
	Insn('CHAR_SET_POS', Char(259), (55940, 1000, 12200), 0),
	Insn('CHAR_SET_POS', Char(260), (55940, 1000, 10780), 0),
	Insn('CHAR_ROTATE', Char(10), 180, 0),
	Insn('0x0D'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 300),
	Insn('TEXT_SET_NAME', Translate('贝奈特')),
	Insn('TEXT_MESSAGE', Char(10), Text(
		'#5P……你们几个，\n'
		'奥斯卡好像拜托你们\n'
		'帮他收集食材吧。{wait}'
		'{page}'
		'#5P好狡猾……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('EMOTE', Char(0), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(1), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(2), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(3), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F#11P哎……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14801F#5P我也在\n'
		'研究新品面包呢。{wait}'
		'{page}'
		'#14813F#5P为什么只接受奥斯卡的委托……\n'
		'（自言自语）……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11P#0200F（这个人\n'
		'\u3000到底怎么了？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F#11P（好像对那位老兄\n'
		'\u3000抱有竞争意识啊。）{wait}'
		'{page}'
		'（看到我们接受了他的委托，\n'
		'\u3000感觉很不开心吧？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0006F#11P（这么麻烦啊……）{wait}'
		'{page}'
		'#0005F（……哎，对了。）{wait}'
		'{page}'
		'#0000F那个，我听说食材的\n'
		'运送因故延迟了……\n'
		'难道你也在为此烦恼吗？{wait}'
		'{page}'
		'不介意的话，\n'
		'我们也帮你收集吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(10), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(10), 0, 2000, (40, 43, 100, 3)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(10), Text(
		'#14805F#5P…………那、那么………{wait}'
		'{page}'
		'#14813F#5P请帮我收集两个『魔兽之蛋』吧。{wait}'
		'{page}'
		'#14818F#5P……请快一点哦。\n'
		'我想比奥斯卡\n'
		'更早地研制出新品面包。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F#11P嗯，明白了。\n'
		'给我们一点时间吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('TEXT_TALK', Char(260), Text(
		'#0305F（罗伊德那家伙，\n'
		'\u3000竟然交涉得如此巧妙啊？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0111F#12P（而且应对得非常自然呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(260), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F#5P怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(259), Char(257), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#11P#0211F不，没什么……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('CROSSFADE', 800),
	Insn('CHAR_ROTATE', Char(10), 270, 0),
	Insn('CHAR_SET_POS', Char(0), (55190, 1000, 12700), 0),
	Insn('0x4C', Char(10), -1),
	Insn('QUEST', 6, Insn('TASK_SET', 2)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][32] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 800),
	Insn('CAM_OFFSET', (55260, 2500, 12530), 0),
	Insn('CAM_ROTATE', 40, 25, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 29710, 0),
	Insn('CHAR_SET_POS', Char(257), (55190, 1000, 12700), 0),
	Insn('CHAR_SET_POS', Char(258), (55190, 1000, 11280), 0),
	Insn('CHAR_SET_POS', Char(259), (55940, 1000, 12200), 0),
	Insn('CHAR_SET_POS', Char(260), (55940, 1000, 10780), 0),
	Insn('CHAR_ROTATE', Char(10), 180, 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0000F嗯，按照你的委托，\n'
		'都拿来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'交给了对方{item 303}{color 0}×２。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_REMOVE', 303, 2),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 6, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(10), Text(
				'#14802F#5P帮大忙啦，谢谢你们。{wait}'
				'{page}'
				'#14804F#5P哼哼……这样一来，\n'
				'就能打败奥斯卡了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(10), Text(
				'#14802F#5P帮大忙啦，谢谢你们。{wait}'
				'{page}'
				'#14808F#5P但是……还是稍微有点慢啊。\n'
				'我明明说过请快一点的。\n'
				'（自言自语）……{wait}'
				'{page}'
				'#14806F#5P按照我的预定计划，\n'
				'本想比奥斯卡快一步，\n'
				'让他哑口无言的……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(906)),
		]),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 6, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST_BONUS_DP', 6, 3),
		]),
		(None, []),
	]),
	Insn('EMOTE', Char(0), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(1), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(2), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(3), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(257), Text(
		'#11P#0003F（唔，明明是看她很困扰，\n'
		'\u3000所以才顺便接受委托的……）{wait}'
		'{page}'
		'（这种结果真的好吗？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11P#0304F（算啦，不是挺好的吗。）{wait}'
		'{page}'
		'#0300F（互相竞争才能\n'
		'\u3000提高技术，\n'
		'\u3000这也是件好事啊。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('CROSSFADE', 800),
	Insn('CHAR_ROTATE', Char(10), 270, 0),
	Insn('CHAR_SET_POS', Char(0), (55190, 1000, 12700), 0),
	Insn('CHAR_SET_POS', Char(1), (55190, 1000, 12700), 0),
	Insn('CHAR_SET_POS', Char(2), (55190, 1000, 12700), 0),
	Insn('CHAR_SET_POS', Char(3), (55190, 1000, 12700), 0),
	Insn('0x4C', Char(10), -1),
	Insn('QUEST', 6, Insn('TASK_SET', 3)),
	Insn('FLAG_SET', Flag(14)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][33] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-1260, 1800, 5200), 0),
	Insn('CAM_ROTATE', 40, 21, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 27520, 0),
	Insn('CHAR_SET_POS', Char(257), (-600, 0, 5400), 0),
	Insn('CHAR_SET_POS', Char(258), (600, 0, 5400), 0),
	Insn('CHAR_SET_POS', Char(259), (-600, 0, 4200), 0),
	Insn('CHAR_SET_POS', Char(260), (600, 0, 4200), 0),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(266), (0, 0, 3000), 0),
			Insn('CHAR_FLAG1_UNSET', Char(4), 128),
			Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
		]),
		(None, []),
	]),
	Insn('0x4B', Char(15), -1),
	Insn('CHAR_ROTATE', Char(15), 180, 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P哟，欢迎光临。\n'
		'欢迎来到『塔里兹商店』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P有什么需要的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F#12P那个……\n'
		'我们在找一种\n'
		'名叫『利奎姆』的花。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P啊，莫非是……\n'
		'来取昆特先生之前订购的花吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(0), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(1), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(2), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(3), 0, 2000, (38, 38, 250, 1)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('EMOTE', Char(4), 0, 2000, (38, 38, 250, 1)),
		]),
		(None, []),
	]),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0005F是的……\n'
		'原来他已经在您这里预订过了啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P是啊，在我们这里，\n'
		'会买这种花的人主要就是他了。\n'
		'再有就是一小部分很虔诚的人……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P稍等……\n'
		'我记得柜台这边\n'
		'是有货的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(15), 0, 500),
	Insn('FORK', 15, 1, [
		Insn('0x98', Char(254), (0, 0, 1000), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(15), 1),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('TEXT_TALK', Char(260), Text(
		'#0306F呼，还以为\n'
		'要帮他垫钱呢。{wait}'
		'{page}'
		'因为他没有给钱，\n'
		'所以有点担心。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(260), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F嗯～\n'
		'对方是个实在的老人，\n'
		'应该不会发生这种事。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0200F既然是这样，\n'
		'多告诉我们一些\n'
		'具体情况不是更好嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F是啊……\n'
		'只说了花的大致\n'
		'位置而已。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(15), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(15)),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P唔、唔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(0), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('EMOTE', Char(1), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('EMOTE', Char(2), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('EMOTE', Char(3), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('EMOTE', Char(4), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
		]),
		(None, []),
	]),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0005F请问怎么了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(15), 180, 500),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P抱歉……那种花\n'
		'好像没货了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0006F这、这样啊……\n'
		'真伤脑筋。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P哎，真对不起啊，\n'
		'能不能稍微等等呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P我现在就去拜托游击士\n'
		'采点回来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('EMOTE', Char(266), 0, 2000, (38, 38, 250, 1)),
		]),
		(None, []),
	]),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0005F原来平时都是\n'
		'拜托游击士的吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(266), Text(
				'#12P#0603F……你应该明白，\n'
				'我们可没有时间等游击士了。{wait}'
				'{page}'
				'#0600F如果没办法解决的话，\n'
				'我们就马上返回鲁巴彻\n'
				'那边进行调查吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 257, 1, [
				Insn('CHAR_WATCH', Char(254), Char(266), 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 258, 1, [
				Insn('CHAR_WATCH', Char(254), Char(266), 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 260, 1, [
				Insn('CHAR_WATCH', Char(254), Char(266), 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 259, 1, [
				Insn('CHAR_WATCH', Char(254), Char(266), 500),
			]),
			Insn('SLEEP', 50),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0012F也、也对啊。{wait}'
				'{page}'
				'#0003F（可是，这样的话……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 258, 1, [
				Insn('CHAR_WATCH', Char(254), Char(257), 500),
			]),
			Insn('TEXT_TALK', Char(258), Text(
				'#0101F……那个，罗伊德。\n'
				'既然都已经接受委托了，我们就帮忙\n'
				'去把那种花采回来吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(266), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(266), Text(
				'#12P#0605F什么……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('FORK', 258, 1, [
				Insn('CHAR_WATCH', Char(254), Char(257), 500),
			]),
			Insn('TEXT_TALK', Char(258), Text(
				'#0101F那个，罗伊德……\n'
				'既然都已经接受委托了，我们就帮忙\n'
				'去把那种花采回来吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F哦哦，说得没错，\n'
		'我们可不能输给游击士啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0200F深有同感。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(260), 500),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F嗯，我也是这么想的。{wait}'
		'{page}'
		'这样的话，要比等待游击士\n'
		'有效率得多吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 50),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0000F请问，那个利奎姆之花\n'
		'开在什么地方呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P啊，你们打算\n'
		'自己去采摘吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P利奎姆之花\n'
		'开在玛因兹山道外缘。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P进入位于山道的隧道后，\n'
		'途中折向通往遗迹的岔路，\n'
		'在那条路上应该就有利奎姆之花。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0000F原来如此，我明白了。\n'
		'我们去找找看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#5P抱歉啊，\n'
		'到时帮我向昆特先生\n'
		'道歉吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(266), Text(
				'#12P#0606F（……本想催他们快点，\n'
				'\u3000结果好像弄巧成拙了。）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('QUEST', 46, Insn('TASK_SET', 3)),
	Insn('0x4C', Char(15), -1),
	Insn('CHAR_SET_POS', Char(0), (0, 0, 5400), 0),
	Insn('CHAR_SET_POS', Char(15), (200, 0, 8500), 180),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]
