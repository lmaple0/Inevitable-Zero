# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'c1130',
	'name2': 'c1130',
	'location': 25,
	'bgm': 100,
	'flags': 8192,
	'includes': [
		'c1130',
		None,
		't1500_1',
		None,
		None,
		None,
	],
	'name3': 'c1130',
	'labels': [],
	'chcp': [
		'chr/ch28200',
		'chr/ch28202',
		'chr/ch29402',
		'chr/ch20300',
		'chr/ch20302',
		'chr/ch34200',
		'chr/ch34202',
		'chr/ch20202',
		'chr/ch28102',
		'chr/ch05502',
		'chr/ch07400',
		'apl/ch50146',
	],
	'npcs': [
		{
			'name': Translate('凯赛尔'),
			'pos': (29309, 4000, -9439),
			'angle': 90,
			'_1': b'\x05\x01\x00\x00\x00\x00\x00\x01',
			'function': Function((0, 4)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('凯赛尔'),
			'pos': (7699, 150, 7980),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x01\x00\xff\xff',
			'function': Function((0, 5)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('诺瓦斯'),
			'pos': (18040, 180, -9699),
			'angle': 180,
			'_1': b'U\x01\x00\x00\x02\x00\xff\xff',
			'function': Function((0, 6)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('夏娜'),
			'pos': (3500, 0, -6989),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 8)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('夏娜'),
			'pos': (13199, 4000, 10529),
			'angle': 180,
			'_1': b'U\x01\x00\x00\x04\x00\xff\xff',
			'function': Function((0, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('亚比'),
			'pos': (3500, 0, -8789),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 10)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('亚比'),
			'pos': (12649, 4000, 10529),
			'angle': 180,
			'_1': b'U\x01\x00\x01\x06\x00\xff\xff',
			'function': Function((0, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('迈尔斯'),
			'pos': (7699, 150, 7980),
			'angle': 270,
			'_1': b'U\x01\x00\x00\x07\x00\xff\xff',
			'function': Function((0, 14)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('塔吉克'),
			'pos': (10449, 180, -12399),
			'angle': 300,
			'_1': b'\xd5\x01\x00\x00\x08\x00\xff\xff',
			'function': Function((0, 22)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('玛利亚贝尔'),
			'pos': (30620, 4000, -15439),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\t\x00\xff\xff',
			'function': Function((0, 23)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('雷克多'),
			'pos': (30540, 4000, -10399),
			'angle': 90,
			'_1': b'\x95\x01\x00\x00\n\x00\x00\x00',
			'function': Function((0, 24)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('亚苏拉主任'),
			'pos': (12949, 4400, 10500),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x0b\x00\xff\xff',
			'function': Function((2, 23)),
			'_2': b'\xff\x00\x00\x00',
		},
	],
	'monsters': [],
	'triggers': [],
	'objects': [
		{
			'pos': (6290, 0, 8000),
			'range': 1300,
			'bubble_pos': (7700, 1500, 7980),
			'_1': b'~\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (2750, 0, 11140),
			'range': 1000,
			'bubble_pos': (2750, 1200, 11140),
			'_1': b'|\x00\x00',
			'function': Function((0, 25)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (18610, 0, -4500),
			'range': 1000,
			'bubble_pos': (18610, 1200, -4500),
			'_1': b'|\x00\x00',
			'function': Function((0, 27)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (23750, 0, -9500),
			'range': 1000,
			'bubble_pos': (23750, 1200, -9500),
			'_1': b'|\x00\x00',
			'function': Function((0, 26)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (6500, 0, -4500),
			'range': 1000,
			'bubble_pos': (6500, 1200, -4500),
			'_1': b'|\x00\x00',
			'function': Function((0, 28)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (9300, 0, -4500),
			'range': 1000,
			'bubble_pos': (9300, 1200, -4500),
			'_1': b'|\x00\x00',
			'function': Function((0, 29)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (21300, 0, -4500),
			'range': 1000,
			'bubble_pos': (21300, 1200, -4500),
			'_1': b'|\x00\x00',
			'function': Function((0, 30)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (23750, 0, -6600),
			'range': 1000,
			'bubble_pos': (23750, 1200, -6600),
			'_1': b'|\x00\x00',
			'function': Function((0, 31)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (23750, 0, -14700),
			'range': 1000,
			'bubble_pos': (23750, 1200, -14700),
			'_1': b'|\x00\x00',
			'function': Function((0, 32)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (23750, 0, -17600),
			'range': 1000,
			'bubble_pos': (23750, 1200, -17600),
			'_1': b'|\x00\x00',
			'function': Function((0, 33)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (18500, 4000, 11800),
			'range': 1000,
			'bubble_pos': (18500, 5200, 11800),
			'_1': b'|\x00\x00',
			'function': Function((0, 34)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (21500, 4000, 11800),
			'range': 1000,
			'bubble_pos': (21450, 5200, 11800),
			'_1': b'|\x00\x00',
			'function': Function((0, 35)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (26400, 4000, 11800),
			'range': 1000,
			'bubble_pos': (26400, 5200, 11800),
			'_1': b'|\x00\x00',
			'function': Function((0, 36)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (29400, 4000, 11800),
			'range': 1000,
			'bubble_pos': (29400, 5200, 11800),
			'_1': b'|\x00\x00',
			'function': Function((0, 37)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (31800, 4000, 9200),
			'range': 1000,
			'bubble_pos': (31750, 5200, 9200),
			'_1': b'|\x00\x00',
			'function': Function((0, 38)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (31800, 4000, 6450),
			'range': 1000,
			'bubble_pos': (31800, 5200, 6450),
			'_1': b'|\x00\x00',
			'function': Function((0, 39)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (31800, 4000, 1440),
			'range': 1000,
			'bubble_pos': (31800, 5200, 1440),
			'_1': b'|\x00\x00',
			'function': Function((0, 40)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (31750, 4000, -1650),
			'range': 1000,
			'bubble_pos': (31750, 5200, -1650),
			'_1': b'|\x00\x00',
			'function': Function((0, 41)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (31750, 4000, -6690),
			'range': 1000,
			'bubble_pos': (31750, 5200, -6690),
			'_1': b'|\x00\x00',
			'function': Function((0, 42)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x19\x00', Function((0, 2)), Function((0, 3))),
	'code': [None]*57,
	'anim': [],
}

data['code'][0] = [
	Insn('EXPR_VAR', 3, Expr([Insn('RAND'), Insn('CONST', 8), Insn('MOD'), Insn('SET'), Insn('END')])),
	Insn('SWITCH', [Insn('VAR', 3), Insn('END')], {
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
		Insn('0x95', Char(254), (29310, 4000, 9100), 1000, 0),
		Insn('0x95', Char(254), (17140, 4000, 9100), 1000, 0),
		Insn('0x95', Char(254), (17140, 4000, 6840), 1000, 0),
		Insn('0x95', Char(254), (27790, 4000, 6840), 1000, 0),
		Insn('0x95', Char(254), (27790, 4000, -9440), 1000, 0),
		Insn('0x95', Char(254), (29310, 4000, -9440), 1000, 0),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_SET', Char(12), 128),
			Insn('CHAR_FLAG1_SET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(15), 128),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(12), 128),
			Insn('CHAR_FLAG1_SET', Char(14), 128),
			Insn('CHAR_FLAG1_SET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(12), 128),
			Insn('CHAR_FLAG1_SET', Char(14), 128),
			Insn('CHAR_FLAG1_SET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(12), 128),
			Insn('CHAR_FLAG1_SET', Char(14), 128),
			Insn('CHAR_FLAG1_SET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(12), 128),
			Insn('CHAR_FLAG1_SET', Char(14), 128),
			Insn('CHAR_FLAG1_SET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(12), 128),
			Insn('CHAR_FLAG1_SET', Char(14), 128),
			Insn('CHAR_FLAG1_SET', Char(15), 128),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 22))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(12), (30500, 4000, -15440), 270),
					Insn('CHAR_SET_POS', Char(14), (30500, 4000, -14890), 270),
					Insn('CHAR_FLAG1_UNSET', Char(19), 128),
					Insn('CHAR_FLAG1_UNSET', Char(19), 2),
					Insn('CHAR_FLAG1_UNSET', Char(19), 16),
					Insn('FORK_FUNC', Char(19), 0, Function((0, 55))),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(12), 128),
			Insn('CHAR_FLAG1_SET', Char(14), 128),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 22))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(19), 128),
					Insn('CHAR_FLAG1_UNSET', Char(19), 2),
					Insn('CHAR_FLAG1_UNSET', Char(19), 16),
					Insn('FORK_FUNC', Char(19), 0, Function((0, 55))),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(15), 128),
			Insn('CHAR_FLAG1_SET', Char(8), 128),
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1464)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 54))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 22))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 2),
			Insn('CHAR_FLAG1_UNSET', Char(19), 16),
			Insn('FORK_FUNC', Char(19), 0, Function((0, 55))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('NOT'), Insn('FLAG', Flag(1280)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x65', 0, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('EXEC', Insn('QUEST_GET', 40, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x65', 0, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 4), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
			Insn('EXIT_SET_ENABLED', 0, 0),
			Insn('EXIT_SET_ENABLED', 1, 1),
		]),
		(None, [
			Insn('EXIT_SET_ENABLED', 0, 1),
			Insn('EXIT_SET_ENABLED', 1, 0),
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
	Insn('0x65', 4, 1),
	Insn('0x65', 6, 1),
	Insn('0x65', 8, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('0x66', 8, 1),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(768)), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('0x66', 3, 1),
					Insn('0x66', 4, 1),
					Insn('0x66', 6, 1),
				]),
				(None, [
					Insn('0x65', 3, 1),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('0x65', 2, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('0x66', 2, 1),
			Insn('0x66', 4, 1),
			Insn('0x66', 6, 1),
		]),
		(None, []),
	]),
	Insn('0x65', 5, 1),
	Insn('0x65', 7, 1),
	Insn('0x65', 9, 1),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('0x66', 5, 1),
			Insn('0x66', 7, 1),
			Insn('0x66', 9, 1),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(254), Text(
								'啊……\n'
								'差不多快到闭馆的时间了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'必须快点锁好门窗。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(0)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(254), Text(
								'借阅、返还的受理即将结束，\n'
								'请各位抓紧时间。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'馆长有事\n'
						'外出了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'而且差不多也快到闭馆时间了，\n'
						'看来今天得由我\n'
						'来锁门窗呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'诺瓦斯先生今天\n'
						'也打算待到\n'
						'闭馆时间再走吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'最近他好像\n'
						'干劲十足啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'啊……对了，古老文献\n'
						'是禁止借出的哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'如果各位想要查阅的话，\n'
						'请在开馆\n'
						'时间内前来。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'今天天气也很好啊，\n'
						'感觉很适合晾晒防虫呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'啊……我并不是想\n'
						'把这里的书籍弄乱哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'只是想让它们通通风而已。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'今天天气也很好啊，\n'
						'感觉很适合野餐。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'等工作上有闲暇了，\n'
						'我也去哪里玩玩吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'这是摆放新发行书籍的地方。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这个作者所着的系列作品\n'
						'很受欢迎……\n'
						'能读到这些书，市民们肯定都会很开心的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'这个作者的作品很受欢迎。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'各位要是想阅读的话，\n'
						'早点借比较好哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'那个……\n'
				'各位是在找儿童书籍吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'儿童书籍的书柜\n'
				'在进门之后的右手边哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'因为比较受欢迎，\n'
				'所以很多都借出去了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……今天准备\n'
						'好好将图书馆打扫一番。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'来馆的人也比较少，\n'
						'对于打扫卫生来说时机正好呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我今天早上也很早就起床了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'今天下午两点就会闭馆，\n'
						'各位要是想借书的话请尽快哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'这个图书馆的二楼\n'
						'可是观看游行的特等席位哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，果然\n'
						'大家都不知道呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我估计连\n'
						'馆长都不知道。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，因为这是只属于我的秘密。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'今天好像比前两天更加热闹了呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'即使在馆内\n'
						'都能听到外面的鼎沸人声。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我要不要\n'
						'也趁午休时出去晃晃呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'都说克洛斯贝尔人\n'
						'很喜欢庆典……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，我果然也是\n'
						'土生土长的克洛斯贝尔人啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'整理返还的书\n'
				'真是辛苦啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'必须趁来馆的人比较少的时候，\n'
				'重新摆放好。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'您好，欢迎光临克洛斯贝尔\n'
						'市立图书馆。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……纪念庆典期间，\n'
						'来馆的人果然急剧减少啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'算了，这也是没办法的事……\n'
						'因为现在正是纪念庆典中最热闹的时候啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'啊……对了对了，\n'
						'馆内禁止饮食。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'在露天店铺买的东西\n'
						'不许带入馆内哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'馆长好像在纪念庆典\n'
						'期间休假。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'算了，反正在庆典的时候，\n'
						'来馆的人会少很多……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然还是有点没信心，\n'
						'但我会一个人好好努力的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'平常工作都是馆长在忙。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'难得有这个机会，\n'
						'我得好好加油。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'那次地下传来了\n'
						'重物倒地的声音……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呼，总之馆长\n'
						'没事就好。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那些书还是\n'
						'很重的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'幸好馆长没受伤。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过当时看到他\n'
						'被埋在书堆里，挣扎着往外爬的场面，\n'
						'我吃惊得都说不出话来了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'彩虹的门票\n'
						'都已经卖光了吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'要是我没放弃，\n'
						'一直排队就好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我总是很容易就会放弃……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'对了……在图书馆的藏书中，\n'
						'有彩虹过去的公演目录\n'
						'和写真集哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……不过一直\n'
						'都没被还回来呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'馆长在休馆日\n'
						'也会来图书馆\n'
						'整理书籍和制作目录。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'他不仅是因为喜欢书，\n'
						'也是为了造福市民\n'
						'而努力。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，虽然算不上位高权重，\n'
						'但我觉得他很了不起。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'对了……图书馆外面的草坪\n'
						'也是馆长亲自修整的哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然并非位高权重，\n'
						'但他是位勤劳且伟大的人。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我听从父母的建议，\n'
						'当上了公务员。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然人们总是认为\n'
						'公务员的报酬与工作量不成正比……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但这个工作地点十分安静，\n'
						'馆长也很和善，\n'
						'所以并非大家想像得那么差。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我听从父母的建议，\n'
						'当上了公务员。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这里工作环境很安静，并且待遇也好。\n'
						'所以并没有大家所想的那么差哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'有白狼出场的童话书……？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，我记得\n'
						'一楼的儿童书籍\n'
						'专区里好像有。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'你们可以\n'
						'去找找看。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'有白狼出场的童话书，\n'
						'我记得一楼的\n'
						'儿童书籍专区里好像有。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'你们可以\n'
						'去找找看。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'唔，这本书是……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我虽然在这里工作五年了，\n'
						'但是还有许多藏书没见过呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这个图书馆的藏书量真的很丰富。\n'
						'我到现在都还没有全部搞清楚。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'这个图书馆\n'
						'藏书量真的很丰富。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'估计只有馆长\n'
						'才能把握全部的藏书情况。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'馆长真的是个爱书之人哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不久前还不小心\n'
						'被埋在了倒下的书堆里。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我当时都看呆了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'馆长之前被\n'
						'埋在了书堆里。\n'
						'我都看呆了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……那个，说实话，\n'
						'其实当时觉得有点好笑。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'这个市立图书馆的藏书量\n'
						'与邻近诸国相比也是数一数二的哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过因为人手不足……\n'
						'所以很多书籍都没有公开供大家借阅。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'虽然这里有很多藏书……\n'
						'但书籍空开手续的办理\n'
						'比较缓慢。{wait}'
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

data['code'][5] = [
	Insn('EXPR_CHAR_ATTR', Char(0), 5, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(9), 5, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('SET'), Insn('END')])),
	Insn('TEXT_START', Char(9)),
	Insn('CHAR_FLAG1_UNSET', Char(9), 16),
	Insn('CHAR_WATCH', Char(9), Char(0), 0),
	Insn('EXPR_CHAR_ATTR', Char(9), 4, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(9), 4, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(9), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(9), 5, Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(9), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
		(Expr([Insn('CHAR_ATTR', Char(9), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(9), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('CHAR_ATTR', Char(9), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(9), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
		]),
		(None, [
			Insn('EXPR_CHAR_ATTR', Char(9), 8, Expr([Insn('CHAR_ATTR', Char(9), 5), Insn('SET'), Insn('END')])),
		]),
	]),
	Insn('EXPR_CHAR_ATTR', Char(9), 4, Expr([Insn('CHAR_ATTR', Char(0), 5), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(0), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(9), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(9), 16),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'欢迎光临\n'
				'克洛斯贝尔市立图书馆。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'今天图书管理员上的是晚班，\n'
				'所以现在馆里就只有我一个人……\n'
				'但仍然可以办理借阅手续哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'各位可以找我办理手续。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(0)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(9), Text(
				'今天迈尔斯先生\n'
				'值晚班……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'……那个，\n'
				'如果想要借阅书籍的话，\n'
				'请不要客气，找我办理手续哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(9), 0),
	Insn('TEXT_END', Char(9)),
	Insn('RETURN'),
]

data['code'][6] = [
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
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(254), 0),
			Insn('TEXT_TALK', Char(254), Text(
				'唔唔，哇哦！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'把这个总结一下，\n'
				'就可以用在下篇论文上了……！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'好资料太多\n'
						'也让人苦恼啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'想要找寻资料的话，\n'
						'果然还是得来市立图书馆。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'好，今天也要奋斗\n'
						'到闭馆时间！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'今天我找到了\n'
						'很棒的东西哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这可是八十年前的\n'
						'商人们留下的笔记哦{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯嗯……通过它，可以了解到\n'
						'克洛斯贝尔当时的许多情况，\n'
						'真是份宝贵的资料啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'八十年前，\n'
						'克洛斯贝尔自治州还没有成立……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'当时不稳定的局势，\n'
						'好像让商人们吃了很多苦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'在论文被打回之后，\n'
				'我就下定了决心。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'今后一定要全心全意\n'
				'投身到研究中。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'因为还有很多文献和\n'
				'资料我都还没看过。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'哼……你们对肯定要留级的诺瓦斯大人我\n'
						'有什么意见吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(339), Text(
						'#1100F？好奇怪的人。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'（严重打击……！！）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('EMOTE', Char(239), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，哈哈哈……\n'
						'结果论文还是没来得及提交。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'算了，\n'
						'再努力一年就好……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('EMOTE', Char(254), 0, 2000, (38, 38, 250, 1)),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(254), Text(
						'现、现在几点了……？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'糟糕……\n'
						'必须马上赶去机场了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不然会来不及交论文……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我在位于雷曼自治州的\n'
						'一所大学里读书……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'如果不计算交通时间，\n'
						'很有可能会来不及……（絮絮叨叨）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'在克洛斯贝尔，『钟』自古以来\n'
						'就拥有特殊的含义……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'早市的开始，运货马车的发车，\n'
						'或是通知敌袭的警报……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔大教堂\n'
						'用鸣钟来报时的方式，\n'
						'据说是从中世纪流传下来的习俗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'啊，怎么觉得\n'
						'意识有点开始恍惚了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'是不是太拼命了呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'外面有庆典活动吗……呵呵呵，\n'
						'我正在拼命赶论文呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'其实游行的起源是\n'
						'本地有权有势的人物\n'
						'在节日期间展示自家彩车。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'在克洛斯贝尔自治州成立之后，\n'
						'这就成为了纪念庆典\n'
						'的庆祝活动……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'然后此传统一直延续至今，\n'
						'游行彩车一般都是由\n'
						'财经界人士和工商协会出资提供的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'…………………………\n'
						'大家好像都在享受庆典呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔从中世纪开始，\n'
						'就是世界首屈一指的贸易都市。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'从地理位置上来看，克洛斯贝尔位于\n'
						'前往大陆西部的交通要道，\n'
						'所以人力资源和资金自然就流向这里了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……时至今日，\n'
						'情况也仍未改变。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'而且现在还有了列车\n'
						'和飞行船这些交通工具……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'可以说克洛斯贝尔比\n'
						'以往聚集了更多资源吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'回、回过神来，\n'
						'才发现现在是纪念庆典……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这么说来，\n'
						'这个月就得提交论文了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'现、现在可不是\n'
						'慢慢品读文献的时候，\n'
						'必须快点写好……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'截、截稿期限……\n'
						'我彻底把这个忘记了……！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'什么……！？\n'
						'你们要去调查\n'
						'『星见之塔』？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'唔唔，太狡猾了……\n'
						'我也想去那里看看的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'『星见之塔』建造于中世纪的\n'
						'一个重要遗迹……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'你们千万不要\n'
						'把它破坏了哦！？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'馆长不允许\n'
						'我进入地下资料室……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'竟然说那里危险。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……………………？？\n'
						'在图书馆里会有什么危险……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'馆长说他会帮我下去找资料的，\n'
						'我只要等着就好。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过图书馆里竟然会有危险……\n'
						'到底是怎么回事啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'论文的截稿期限临近了，\n'
						'不抓紧点的话，又会留级了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'咳咳，总之\n'
						'只能拜托馆长\n'
						'帮我去地下资料室找资料了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'只凭手上的资料，\n'
						'远远不够写论文啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'这里的地下资料室中\n'
						'有许多古老的文献。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'十分具有查阅价值。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'这个市立图书馆的\n'
						'历史很悠久哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'它的前身是资料馆，\n'
						'原本似乎是克洛斯贝尔的商人们\n'
						'保管帐簿的地方。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'所以这里还留有\n'
						'三百多年前的资料。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'对研究历史的学者来说，\n'
						'这里就是资料的宝库。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'当时的资料，都被很好地\n'
						'保存在这个图书馆里。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过那些一般都不对外公开。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'虽然不怎么为人所知，\n'
						'在克洛斯贝尔\n'
						'残存着多处中世纪的遗迹。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'比较著名的有阿尔摩利卡古道尽头的\n'
						'古战场遗迹。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'二十年前左右应该\n'
						'有个大规模的调查团\n'
						'去调查过。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'对了对了，放置在\n'
						'中央广场的\n'
						'那个巨大的钟……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'好像就是\n'
						'古战场出土的文物。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔还有其它\n'
						'几处有名的遗迹哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我也很想去看看……\n'
						'不过现在得赶着写论文……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'在克洛斯贝尔，\n'
						'熟悉历史的人\n'
						'已经很少了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'五十年前的历史倒还好，\n'
						'不过一两百年前的历史\n'
						'大家就都不知道了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我想知道克洛斯贝尔市\n'
						'发展壮大的具体过程。\n'
						'不过大家好像都对这个没有兴趣。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔人，\n'
						'大多数都不了解历史呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'作为学者，我对此感到很寒心。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'研究历史必须脚踏实地，勤勤恳恳……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'寻找文献、搜集传说，\n'
						'偶尔去调查相关的遗迹……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'总之历史就是一门需要不断调查的学问。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'对历史研究者来说，\n'
						'独自进行调查是基础中的基础。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然我就是历史学者，\n'
						'但也觉得这门学问很平实无华。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1248)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 7))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'因为资料完全不够……\n'
						'所以我才去央求馆长，\n'
						'拜托他让我看这些未公开资料的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，这下应该够了吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'要是不快点把论文写好的话，\n'
						'就拿不到博士学位，又要留级……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1248)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 7))),
				]),
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'《克洛斯贝尔的传承》……\n'
						'《玛因兹乡土史》……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不行，资料完全不够……\n'
						'这样会来不及提交论文的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我正在研究\n'
						'克洛斯贝尔的历史。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但找不到好资料。\n'
						'这样就没法写论文了啊……{wait}'
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

data['code'][7] = [
	Insn('TEXT_TALK', Char(254), Text(
		'哈哈哈……没想到\n'
		'写个论文竟然这么难。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'在开始写论文之前，\n'
		'我还买了娱乐小说，\n'
		'想在闲暇之余看看的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'啊，各位。\n'
		'不嫌弃的话，\n'
		'请收下这本书吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'我实在太忙了，\n'
		'根本没时间看。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'收下了{item 710}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 710, 1),
	Insn('FLAG_SET', Flag(1248)),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'今天我要把馆长推荐的书\n'
		'借回家。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'呵呵，因为孩子回家之后\n'
		'还想听我给他读这本书。{wait}'
	)),
	Insn('TEXT_WAIT'),
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
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1573)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(254), Text(
								'《玛尔克与森林中的魔女》下卷\n'
								'终于可以借阅了呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'那本书在图书馆的童话书中\n'
								'是最受欢迎的。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'我在念给亚比\n'
								'听的时候，\n'
								'也不知不觉迷上了它……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(2)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(254), Text(
								'《玛尔克与森林深处的魔女》\n'
								'是图书馆里最受欢迎的\n'
								'童话书哦。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'书就放在一楼的书架上，\n'
								'各位也请读读看吧？{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 12))),
				]),
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'亚比好像很想把自己喜欢的书\n'
						'都推荐琪雅看。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那个，\n'
						'会不会给各位添了很多麻烦啊？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0204F不会，完全没有……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F我们虽然没法经常带琪雅来，\n'
						'但还是请你多跟她玩哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'亚比很喜欢看书，\n'
						'只要图书馆开门，他每天都会来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵……亚比好像\n'
						'很喜欢琪雅啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(254), 0),
			Insn('TEXT_TALK', Char(254), Text(
				'巡警先生\n'
				'一直拼命追赶。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过小猪\n'
				'也一直拼命逃跑……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'纪念庆典之后，\n'
				'亚比就一直求我给他\n'
				'讲巡警先生的故事。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵……他好像\n'
				'喜欢上了巡警先生的制服呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啊……\n'
				'这孩子比我们家亚比大一点吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，你们要好好相处哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啊，糟糕了。\n'
				'都已经是这个时间了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'得赶紧去\n'
				'买点东西。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我们家的孩子如果\n'
				'喜欢上一本书，\n'
				'就会一直求我念给他听。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呼，真没办法。\n'
				'今天都已经读了五遍了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(254), 0),
			Insn('TEXT_TALK', Char(254), Text(
				'那时传来了\n'
				'女神的声音。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'『道路已经开启，\n'
				'\u3000快点回到同伴的身边吧……』{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'小狐狸听到之后，\n'
				'便匆忙跑了出去……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'说起来……\n'
						'听说克洛斯贝尔的大教堂\n'
						'是一座很宏伟的建筑。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'而且其中似乎也有很多\n'
						'优秀的祭司和修女。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'亚比明年就可以去\n'
						'主日学校上学了，\n'
						'所以我准备先去大教堂祷告一下。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'自从搬来克洛斯贝尔，\n'
						'我还没去过大教堂。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'亚比非常喜欢爱德斯女神，\n'
						'他一定会对那里很感兴趣吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'图书馆里有很多\n'
				'儿童读物，真是太好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过看的人\n'
				'出人意料地少。\n'
				'这是因为什么呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我最近刚搬来\n'
				'克洛斯贝尔。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'克洛斯贝尔的街道很漂亮，\n'
				'真是一个很棒的城市呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(254), 0),
			Insn('TEXT_TALK', Char(254), Text(
				'出现在那里的\n'
				'竟然是头恐怖的恶魔。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哇哇哇哇哇……！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(254), 0),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'然后空之女神\n'
						'所降下的光芒……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('SOUND_PLAY', 18, 0, 0, 100),
					Insn('SLEEP', 500),
					Insn('TEXT_TALK', Char(254), Text(
						'充溢了整个世界。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'动物们都大吃一惊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'然后空之女神\n'
						'所降下的光芒充溢了整个世界。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'动物们都大吃一惊……{wait}'
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

data['code'][10] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'回家之后，\n'
		'我还要让妈妈给我讲故事～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][11] = [
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
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1573)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'接下来故事里会发生什么呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'快点念快点念嘛～！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 12))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'下次我要把这书\n'
						'推荐给琪雅姐姐看～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(254), 1),
			Insn('TEXT_TALK', Char(254), Text(
				'哇，巡警先生好帅啊！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'那个那个，\n'
						'琪雅姐姐呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F哈哈，今天她没和我们一起来哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0102F她下次还会来玩的，\n'
						'乖乖等着哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，我乖乖等着！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'替我跟琪雅姐姐\n'
						'问声好哦！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'哇～哦，妈妈要念\n'
						'这本书里的故事给我听哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(339), Text(
						'#1110F真好，琪雅也想听听看。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(254), 0, 1700, (0, 1, 250, 2)),
					Insn('SOUND_PLAY', 29, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(254), Text(
						'姐姐也喜欢这本书吗～？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嘿嘿嘿，跟我一样呢～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(339), Text(
						'#1109F嗯，跟你一样哦～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
							Insn('TEXT_TALK', Char(258), Text(
								'#0102F（小孩子们\n'
								'\u3000果然很快就能玩在一起……）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
							Insn('TEXT_TALK', Char(259), Text(
								'#0204F（小孩子们\n'
								'\u3000果然很快就能玩在一起呢……）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
							Insn('TEXT_TALK', Char(260), Text(
								'#0302F（小孩子们\n'
								'\u3000果然很快就能玩在一起啊……）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, []),
					]),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'姐姐，\n'
						'我们下次再一起玩啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(339), Text(
						'#1110F嗯，好呀～！\n'
						'再见！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(254), 1),
			Insn('TEXT_TALK', Char(254), Text(
				'啊，妈妈！\n'
				'再多念些给我听嘛！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(254), 1),
			Insn('TEXT_TALK', Char(254), Text(
				'那个，还是这本书比较好呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'因为我\n'
				'最喜欢女神了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哇，好兴奋……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'听妈妈念故事书，\n'
				'真的很开心！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我跟你们说哦……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'那边有一个叫做大教堂的，\n'
				'很大的教堂哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我也想去那里看看！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(254), 1),
			Insn('TEXT_TALK', Char(254), Text(
				'啊，妈妈！\n'
				'再多念些给我听嘛！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'等我长大后，{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'一定要\n'
						'当个神父。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'然后给小孩子\n'
						'讲这本书里的故事。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'等我长大后，\n'
						'一定要当个神父。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'然后像妈妈一样，\n'
						'给小孩子讲这本书里的故事。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(254), 1),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵……\n'
				'会怎样呢～？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(254), 1),
			Insn('TEXT_TALK', Char(254), Text(
				'哇～哇～！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'再多念些给我听嘛～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('CHAR_SET_FRAME', Char(254), 1),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('CHAR_SET_FRAME', Char(14), 0),
	Insn('TEXT_TALK', Char(12), Text(
		'最后大家\n'
		'都过上了幸福美好的日子。\n'
		'可喜可贺，可喜可贺。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'……亚比，故事好听吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'嗯，很好听哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'下次我要把这书\n'
		'推荐给琪雅姐姐看。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'呵呵，没错。\n'
		'这也许是个好主意哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(2)),
	Insn('FLAG_SET', Flag(4)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('CALL', Function((0, 14))),
		]),
		(None, [
			Insn('CALL', Function((0, 5))),
		]),
	]),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('EXPR_CHAR_ATTR', Char(0), 5, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(15), 5, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('SET'), Insn('END')])),
	Insn('TEXT_START', Char(15)),
	Insn('CHAR_FLAG1_UNSET', Char(15), 16),
	Insn('CHAR_WATCH', Char(15), Char(0), 0),
	Insn('EXPR_CHAR_ATTR', Char(15), 4, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(15), 4, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(15), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(15), 5, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
		(Expr([Insn('CHAR_ATTR', Char(15), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(15), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('CHAR_ATTR', Char(15), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(15), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
		]),
		(None, [
			Insn('EXPR_CHAR_ATTR', Char(15), 8, Expr([Insn('CHAR_ATTR', Char(15), 5), Insn('SET'), Insn('END')])),
		]),
	]),
	Insn('EXPR_CHAR_ATTR', Char(15), 4, Expr([Insn('CHAR_ATTR', Char(0), 5), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(0), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(15), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(15), 16),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('CALL', Function((0, 21))),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
							Insn('CALL', Function((0, 20))),
						]),
						(None, [
							Insn('TEXT_TALK', Char(15), Text(
								'谢谢你，罗伊德。\n'
								'要是只靠馆员的话，\n'
								'估计没办法全部收回来。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'如果有需要的话，还会找你们帮忙的。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(6)),
						]),
					]),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 5))), Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 7))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 10))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((0, 52))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 1))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
							Insn('CALL', Function((0, 20))),
						]),
						(None, [
							Insn('TEXT_TALK', Char(15), Text(
								'回收逾期未还的书本这个任务，\n'
								'就拜托你们了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'这次的借书人都是住在\n'
								'克洛斯贝尔郊外的，\n'
								'所以你们可以慢慢进行回收。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'收回三本书后，\n'
								'就拿回来交给我。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(6)),
						]),
					]),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 0))), Insn('END')]), [
					Insn('CALL', Function((0, 49))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('CALL', Function((0, 48))),
				]),
				(None, [
					Insn('CALL', Function((0, 20))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
							Insn('CALL', Function((0, 19))),
						]),
						(None, [
							Insn('TEXT_TALK', Char(15), Text(
								'谢谢你，罗伊德。\n'
								'要是只靠馆员的话，\n'
								'估计没办法全部收回来。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'如果有需要的话，还会找你们帮忙的。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(6)),
						]),
					]),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 5))), Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 7))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 10))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((0, 52))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 1))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
							Insn('CALL', Function((0, 19))),
						]),
						(None, [
							Insn('TEXT_TALK', Char(15), Text(
								'回收逾期未还的书本这个任务，\n'
								'就拜托你们了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'这次的借书人都是住在\n'
								'克洛斯贝尔郊外的，\n'
								'所以你们可以慢慢进行回收。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'收回三本书后，\n'
								'就拿回来交给我。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(6)),
						]),
					]),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 0))), Insn('END')]), [
					Insn('CALL', Function((0, 49))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('CALL', Function((0, 48))),
				]),
				(None, [
					Insn('CALL', Function((0, 19))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
							Insn('CALL', Function((0, 18))),
						]),
						(None, [
							Insn('TEXT_TALK', Char(15), Text(
								'谢谢你，罗伊德。\n'
								'要是只靠馆员的话，\n'
								'估计没办法全部收回来。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'如果有需要的话，还会找你们帮忙的。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(6)),
						]),
					]),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 5))), Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 7))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 10))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((0, 52))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 1))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
							Insn('CALL', Function((0, 18))),
						]),
						(None, [
							Insn('TEXT_TALK', Char(15), Text(
								'回收逾期未还的书本这个任务，\n'
								'就拜托你们了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'这次的借书人都是住在\n'
								'克洛斯贝尔郊外的，\n'
								'所以你们可以慢慢进行回收。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'收回三本书后，\n'
								'就拿回来交给我。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(6)),
						]),
					]),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 0))), Insn('END')]), [
					Insn('CALL', Function((0, 49))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('CALL', Function((0, 48))),
				]),
				(None, [
					Insn('CALL', Function((0, 18))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1415)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(339), Text(
						'#1110F那个那个，这里有好多书啊！{wait}'
						'{page}'
						'#1109F琪雅也可以在\n'
						'这里看书吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(15), 0, 2000, (0, 1, 250, 2)),
					Insn('SOUND_PLAY', 29, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('EXPR_CHAR_ATTR', Char(339), 5, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(15), 5, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('SET'), Insn('END')])),
					Insn('TEXT_START', Char(15)),
					Insn('CHAR_FLAG1_UNSET', Char(15), 16),
					Insn('CHAR_WATCH', Char(15), Char(339), 0),
					Insn('EXPR_CHAR_ATTR', Char(15), 4, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(15), 4, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(15), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(15), 5, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
					Insn('IF', [
						(Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
						(Expr([Insn('CHAR_ATTR', Char(15), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
							Insn('EXPR_CHAR_ATTR', Char(15), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
						]),
						(Expr([Insn('CHAR_ATTR', Char(15), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
							Insn('EXPR_CHAR_ATTR', Char(15), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
						]),
						(None, [
							Insn('EXPR_CHAR_ATTR', Char(15), 8, Expr([Insn('CHAR_ATTR', Char(15), 5), Insn('SET'), Insn('END')])),
						]),
					]),
					Insn('EXPR_CHAR_ATTR', Char(15), 4, Expr([Insn('CHAR_ATTR', Char(339), 5), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(339), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(15), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
					Insn('CHAR_FLAG1_SET', Char(15), 16),
					Insn('TEXT_TALK', Char(15), Text(
						'哦，难道……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'你喜欢看书吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(339), Text(
						'#1111F嗯，大概吧！{wait}'
						'{page}'
						'#1110F一看到书的封面，\n'
						'我就觉得很兴奋！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'嗯嗯，我明白这种感觉。\n'
						'我也是因为太喜欢书了，\n'
						'所以才成为图书管理员的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(339), Text(
						'#1105F？？？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EXPR_CHAR_ATTR', Char(257), 5, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(15), 5, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('SET'), Insn('END')])),
					Insn('TEXT_START', Char(15)),
					Insn('CHAR_FLAG1_UNSET', Char(15), 16),
					Insn('CHAR_WATCH', Char(15), Char(257), 0),
					Insn('EXPR_CHAR_ATTR', Char(15), 4, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(15), 4, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(15), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(15), 5, Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
					Insn('IF', [
						(Expr([Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(15), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
						(Expr([Insn('CHAR_ATTR', Char(15), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
							Insn('EXPR_CHAR_ATTR', Char(15), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
						]),
						(Expr([Insn('CHAR_ATTR', Char(15), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
							Insn('EXPR_CHAR_ATTR', Char(15), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
						]),
						(None, [
							Insn('EXPR_CHAR_ATTR', Char(15), 8, Expr([Insn('CHAR_ATTR', Char(15), 5), Insn('SET'), Insn('END')])),
						]),
					]),
					Insn('EXPR_CHAR_ATTR', Char(15), 4, Expr([Insn('CHAR_ATTR', Char(257), 5), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(257), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(15), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
					Insn('CHAR_FLAG1_SET', Char(15), 16),
					Insn('TEXT_TALK', Char(15), Text(
						'罗伊德，你们一定要多借几本书，\n'
						'如果是这孩子要看的话，借几本都行哦！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F谢、谢谢啊，叔叔。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
							Insn('TEXT_TALK', Char(258), Text(
								'#0100F（呵呵，图书管理员跟罗伊德认识，\n'
								'\u3000真是太好了。）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
							Insn('TEXT_TALK', Char(259), Text(
								'#0200F（图书管理员跟罗伊德前辈认识，\n'
								'\u3000真是太好了。）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
							Insn('TEXT_TALK', Char(260), Text(
								'#0300F（图书管理员跟罗伊德认识，\n'
								'\u3000真是太好了。）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, []),
					]),
					Insn('FLAG_SET', Flag(1415)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(15), Text(
						'罗伊德，你一定要\n'
						'借几本书给这孩子看。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'读书对小孩子有好处……\n'
						'你们一定要继续\n'
						'培养她读书的兴趣。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F哈哈哈……\n'
						'那我们就去看看吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 14))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((0, 56))),
				]),
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(15), Text(
						'以前我就一直\n'
						'鼓励赛西儿，\n'
						'叫她做自己喜欢的事……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'但就连我都没想到\n'
						'她会成为一名护理师。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'现在想想，好像她\n'
						'小时候就一直央求我带她\n'
						'去乌尔斯拉医院看看……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'应该是从那时候起\n'
						'就梦想成为护理师了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(15), Text(
						'赛西儿成为了护理师，\n'
						'你阿姨她好像很担心……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'不过这是那孩子自己选择的道路，\n'
						'我们必须支持她。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 14))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((0, 56))),
				]),
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(15), Text(
						'痛痛痛……我刚才在\n'
						'整理地下资料室的时候……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'一堆书突然倒下来，\n'
						'把我埋在了下面。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'如果凯赛尔没来救我的话，\n'
						'我说不定已经窒息死亡了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F没这么夸张吧……{wait}'
						'{page}'
						'#0000F对了，叔叔，\n'
						'如果有什么需要帮忙的，\n'
						'来找我们支援课不就行了嘛。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'哈哈，抱歉抱歉。\n'
						'因为没时间联系你们。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(15), Text(
						'我的梦想是将地下资料室中的文献整理好，\n'
						'然后向市民们公开。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'不过书太多了，\n'
						'实在没法全部都整理完。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(15), Text(
						'今天要总结\n'
						'新书的购买清单。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'在我们图书馆，\n'
						'这位作者的系列作品最受欢迎。\n'
						'必须得多购买些。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F哈哈……克洛斯贝尔市\n'
						'的人口太多了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'所以来借书的人自然也就多了。\n'
						'呵呵，这点很值得高兴啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(15), Text(
						'购买藏书本来用的就是市民的钱。\n'
						'希望大家都不要客气，\n'
						'尽量多来借一些书。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(15), Text(
						'罗伊德，很少见你们\n'
						'下午过来啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'难道今天你们\n'
						'休假吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F叔叔……\n'
						'……啊，并不是呢。{wait}'
						'{page}'
						'支援课的休假非常少，\n'
						'今天也是从早上就开始工作了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F我们也是最近才体会到的，\n'
						'支援课的工作非常忙。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'哈哈，这样子啊。\n'
						'没办法，警察都忙啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'图书馆都会有适当的休假哦，\n'
						'在公务员中也算是特别轻松的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(15), Text(
						'这个市立图书馆\n'
						'每星期都会固定放假一天。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'不过我是图书管理员，\n'
						'就算放假也有很多杂活要做。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
							Insn('TEXT_TALK', Char(15), Text(
								'谢谢啊，罗伊德。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'如果有需要的话，还会找你们帮忙的。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('CALL', Function((0, 17))),
						]),
					]),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 3))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 4))), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 725, 0)), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 726, 0)), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 727, 0)), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((0, 47))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 1))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
							Insn('CALL', Function((0, 15))),
						]),
						(None, [
							Insn('TEXT_TALK', Char(15), Text(
								'回收逾期未还的书本这个任务，\n'
								'就拜托你们了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'收回三本书后，\n'
								'就拿回来交给我。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'因为事情并不紧急，\n'
								'所以你们可以慢慢进行回收。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(6)),
						]),
					]),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 0))), Insn('END')]), [
					Insn('CALL', Function((0, 44))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('CALL', Function((0, 43))),
				]),
				(None, [
					Insn('CALL', Function((0, 15))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
							Insn('TEXT_TALK', Char(15), Text(
								'谢谢啊，罗伊德。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'如果有需要的话，还会找你们帮忙的。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('CALL', Function((0, 17))),
						]),
					]),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 3))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 4))), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 725, 0)), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 726, 0)), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 727, 0)), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((0, 47))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 1))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
							Insn('CALL', Function((0, 16))),
						]),
						(None, [
							Insn('TEXT_TALK', Char(15), Text(
								'回收逾期未还的书本这个任务，\n'
								'就拜托你们了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'收回三本书后，\n'
								'就拿回来交给我。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'因为事情并不紧急，\n'
								'所以你们可以慢慢进行回收。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(6)),
						]),
					]),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 0))), Insn('END')]), [
					Insn('CALL', Function((0, 44))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('CALL', Function((0, 43))),
				]),
				(None, [
					Insn('CALL', Function((0, 16))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
							Insn('TEXT_TALK', Char(15), Text(
								'谢谢啊，罗伊德。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'如果有需要的话，还会找你们帮忙的。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('CALL', Function((0, 17))),
						]),
					]),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 3))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 4))), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 725, 0)), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 726, 0)), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 727, 0)), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((0, 47))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 1))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
							Insn('CALL', Function((0, 16))),
						]),
						(None, [
							Insn('TEXT_TALK', Char(15), Text(
								'回收逾期未还的书本这个任务，\n'
								'就拜托你们了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'收回三本书后，\n'
								'就拿回来交给我。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(15), Text(
								'因为事情并不紧急，\n'
								'所以你们可以慢慢进行回收。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(6)),
						]),
					]),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 0))), Insn('END')]), [
					Insn('CALL', Function((0, 44))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('CALL', Function((0, 43))),
				]),
				(None, [
					Insn('CALL', Function((0, 17))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(623)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F叔叔，\n'
						'好久不见。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'哦？你不是……\n'
						'以前住在隔壁的罗伊德嘛！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'哈哈哈，实在是吃了一惊啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'虽然听说过你快回来了，\n'
						'……但没想到你都长这么大了，简直让人认不出来了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0012F呵呵，只是身高长了，\n'
						'但内在还是很不成熟呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'没那回事。\n'
						'你不是已经顺利\n'
						'通过搜查官考试了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'盖一定\n'
						'也会为你高兴的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0008F……会吗？{wait}'
						'{page}'
						'……如果真是那样就好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'嗯，一定会的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'虽然我因为图书管理员的工作，\n'
						'所以经常不在家……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'不过你阿姨她应该都在家里。\n'
						'如果有什么需要帮忙的，\n'
						'就去找她哦……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F嗯，\n'
						'那就麻烦阿姨了。{wait}'
						'{page}'
						'#0003F……承蒙您照顾了，\n'
						'叔叔。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(623)),
				]),
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(15), Text(
						'唔，罗伊德，\n'
						'你不借本书去看吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0012F哈哈……说起来，叔叔以前\n'
						'也经常给我推荐书啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'呵呵，因为书是好东西哦。\n'
						'只要沉浸在书堆里，心情便能得到放松。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'有空的话，\n'
						'你们就慢慢看看吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'这里的藏书量\n'
						'可是很多的哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(15), Text(
						'有空的话，\n'
						'你们就慢慢看看吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'呵呵，这里的藏书量\n'
						'可是很多的哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), []),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('TEXT_END', Char(15)),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(15), Text(
				'嗯，还有\n'
				'很多书未归还啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'我们这里人手不足，\n'
				'管理上难免存在疏漏。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'所以很多人\n'
				'到期限了都\n'
				'没把书还回来。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F这样子啊。\n'
				'叔叔也很辛苦啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('TEXT_TALK', Char(15), Text(
						'嗯，不过\n'
						'你们可\n'
						'帮了我们不少忙啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'我身为图书管理员，\n'
						'就想把图书馆管理好。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(15), Text(
						'嗯，其中\n'
						'有的人借了很长时间\n'
						'都一直没把书还回来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'估计应该是\n'
						'忘了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('FLAG_SET', Flag(5)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(15), Text(
				'我们这里人手不足，\n'
				'管理上难免存在疏漏。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'看来果然得考虑\n'
				'将管理费也加入预算了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(15), Text(
				'这个图书馆的地下书库里，\n'
				'保存有大量的古代书籍\n'
				'和未整理的资料。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'……时不时下去翻翻，\n'
				'偶尔就会找到很稀有的书，\n'
				'那时就会感到十分幸福。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(15), 0, 2000, (10, 11, 250, 2)),
			Insn('SOUND_PLAY', 27, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F（叔叔还真是\n'
				'\u3000很喜欢书啊……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(5)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(15), Text(
				'地下书库里的书籍\n'
				'都没能来得及办理公开手续，\n'
				'所以一直都没有对外公开……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'对喜欢书的人来说，那里就像是乐园一样。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(15), Text(
				'这个图书馆只允许\n'
				'每个人借三本书。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'因为人手不够，\n'
				'如果大家借书过多的话，\n'
				'我们就会来不及整理归还的图书。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'嗯，要是能允许每个人借五本书的话，\n'
				'对大家来说就方便多了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(5)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(15), Text(
				'这个图书馆的\n'
				'人手严重不足。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'要是人手再多点的话，\n'
				'就能更好的为大家服务了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(15), Text(
				'琪雅非常了不起哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'借回去的书\n'
				'一下子就读完了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F嗯，那孩子\n'
				'好像真的很喜欢书。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'呵呵，看到又多了一个喜欢书的同道中人，\n'
				'我也很高兴。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'欢迎你们再来借书哦，\n'
				'我会准备几本精彩作品的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F嗯，我想她会很开心的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(5)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(15), Text(
				'琪雅非常了不起哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'将来或许能继承我的衣钵，\n'
				'成为一名图书管理员呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0012F啊哈哈哈哈……\n'
				'（看来叔叔已经完全\n'
				'\u3000喜欢上琪雅了啊。）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('TEXT_TALK', Char(15), Text(
		'听说港湾公园那边\n'
		'发生了事件。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'唔，那附近明明\n'
		'是条商业街。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'怎么一大早就听到了这么危险的事件。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(15), Text(
				'以前，盖还是警察的时候，\n'
				'他好像每天都很开心。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'当他还是个新人时，\n'
				'就在餐桌上兴奋地跟我们说过，\n'
				'他遇到了一个很合得来的搭档。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'距离那时候\n'
				'才刚刚过去不到十年……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'但盖、赛西儿还有罗伊德……\n'
				'完全物是人非了呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0008F……………是啊………{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(5)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(15), Text(
				'哈哈，抱歉啊，\n'
				'不自觉就感伤起来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'好像是被你阿姨\n'
				'传染得多愁善感了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('TEXT_TALK', Char(15), Text(
		'太阳快下山了啊……\n'
		'图书馆也快要闭馆了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'罗伊德，回去的时候\n'
		'别落下东西哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'明天再见。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F嗯，叔叔您也辛苦了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('FLAG_SET', Flag(5)),
	Insn('RETURN'),
]

data['code'][22] = [
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
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……我有了个新发现。\n'
						'只要来图书馆，\n'
						'工作就会进展得很顺利。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'安静的气氛可以令人精神集中，\n'
						'旁边也没有唠叨的上司。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'没想到图书馆\n'
						'竟然还有这种功效。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'人少的地方\n'
						'对我来说正合适。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(254), 0),
			Insn('TEXT_TALK', Char(254), Text(
				'既不是这样，也不是那样……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，这里果然\n'
				'还是该这么办吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'（唰唰唰……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我可没有\n'
						'玩乐的闲工夫。\n'
						'工作一大堆啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'（唰唰唰……）\n'
						'必须得认真工作。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'要是书面材料提交晚了，\n'
						'就会没法制作预算的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'市政厅那边都忙成一锅粥了。\n'
						'在那里我没办法集中精神，\n'
						'所以就把工作带来这里做了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'因为一个星期后\n'
						'就是预算会议了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，我为了工作\n'
						'还特意换了办公地点，实在是太认真了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('EXPR_CHAR_ATTR', Char(0), 5, Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(17), 5, Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('SET'), Insn('END')])),
	Insn('TEXT_START', Char(17)),
	Insn('CHAR_FLAG1_UNSET', Char(17), 16),
	Insn('CHAR_WATCH', Char(17), Char(0), 0),
	Insn('EXPR_CHAR_ATTR', Char(17), 4, Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(17), 4, Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(17), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(17), 5, Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
		(Expr([Insn('CHAR_ATTR', Char(17), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(17), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('CHAR_ATTR', Char(17), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(17), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
		]),
		(None, [
			Insn('EXPR_CHAR_ATTR', Char(17), 8, Expr([Insn('CHAR_ATTR', Char(17), 5), Insn('SET'), Insn('END')])),
		]),
	]),
	Insn('EXPR_CHAR_ATTR', Char(17), 4, Expr([Insn('CHAR_ATTR', Char(0), 5), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(0), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(17), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(17), 16),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1447)), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('CROSSFADE', 500),
			Insn('CAM_OFFSET', (29400, 5020, -14320), 0),
			Insn('CAM_ROTATE', 51, 23, 0, 0),
			Insn('0x6E', 440, 0),
			Insn('CAM_DISTANCE', 18590, 0),
			Insn('CHAR_FLAG1_SET', Char(8), 128),
			Insn('CHAR_SET_POS', Char(257), (29930, 4030, -13780), 180),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(258), (28660, 4030, -13530), 135),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(259), (28660, 4030, -13530), 135),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(260), (28660, 4030, -13530), 135),
				]),
				(None, []),
			]),
			Insn('CHAR_SET_POS', Char(339), (27220, 4030, -14020), 135),
			Insn('CHAR_SET_FRAME', Char(17), 2),
			Insn('0x0D'),
			Insn('TEXT_TALK', Char(17), Text(
				'#2905F#11P啊，好巧啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F玛利亚贝尔小姐……！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#0102F#5P贝尔……\n'
						'难得在这种地方见到你呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#0202F#5P难得在这种地方\n'
						'遇见您呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#0305F#5P哦哦。\n'
						'难得在这种地方看到你啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
			Insn('TEXT_TALK', Char(17), Text(
				'#2904F呵呵，偶尔有假期时，\n'
				'我就会来这里坐坐。{wait}'
				'{page}'
				'因为图书馆里有着\n'
				'导力网络远远无法企及的知识……{wait}'
				'{page}'
				'#2902F所以没理由不好好利用啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0012F真、真是让人受益匪浅。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#0104F#5P呵呵……\n'
						'你其实是很爱学习的啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(17), Text(
						'#2904F哎呀，艾莉你不也一样吗。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#0204F#5P……原来如此。\n'
						'确实有一定的道理。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#0309F#5P哈……佩服佩服啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
			Insn('CHAR_SET_FRAME', Char(17), 0),
			Insn('SLEEP', 300),
			Insn('TEXT_TALK', Char(17), Text(
				'#2900F……嗯，先不谈这个。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(339), Text(
				'#1101F（盯……）{wait}'
				'{page}'
				'#1110F那个那个，罗伊德。\n'
				'这位大姐姐也是你们的朋友吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 257, 1, [
				Insn('CHAR_WATCH', Char(257), Char(339), 500),
			]),
			Insn('SLEEP', 50),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('CHAR_WATCH', Char(258), Char(339), 500),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('CHAR_WATCH', Char(259), Char(339), 500),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('CHAR_WATCH', Char(260), Char(339), 500),
				]),
				(None, []),
			]),
			Insn('TEXT_TALK', Char(257), Text(
				'#0002F#11P啊……算是吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(17), Text(
				'#2904F#11P呵呵，事情的经过我已经知道了哦。{wait}'
				'{page}'
				'#2902F这孩子就是原本计划要\n'
				'展出拍卖的『人偶』吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(0), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 50),
			Insn('EMOTE', Char(1), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('FORK', 257, 1, [
				Insn('CHAR_WATCH', Char(257), Char(17), 500),
			]),
			Insn('SLEEP', 50),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('FORK', 258, 1, [
						Insn('CHAR_WATCH', Char(258), Char(17), 500),
					]),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('FORK', 259, 1, [
						Insn('CHAR_WATCH', Char(259), Char(17), 500),
					]),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('FORK', 260, 1, [
						Insn('CHAR_WATCH', Char(260), Char(17), 500),
					]),
				]),
				(None, []),
			]),
			Insn('SLEEP', 200),
			Insn('TEXT_TALK', Char(257), Text(
				'#0011F什么……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#0101F#5P贝尔，你为什么会知道……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#0205F#5P……您为何会知道……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#0305F#5P你怎么会知道……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
			Insn('TEXT_TALK', Char(17), Text(
				'#2906F唉……\n'
				'都引起了那么大的骚乱，\n'
				'要是不知道就奇怪了。{wait}'
				'{page}'
				'#2902F当时我也远远望到了\n'
				'你们逃出宅邸时的样子。{wait}'
				'{page}'
				'#2904F再把这一周以来得到的消息综合分析一下，\n'
				'便很容易推测出来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0006F这、这样啊……{wait}'
				'{page}'
				'#0001F……那个，玛利亚贝尔小姐。\n'
				'这件事还请务必──{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(17), Text(
				'#2903F我知道啦。{wait}'
				'{page}'
				'#2902F话说回来，我当时正好在场，\n'
				'或许也是因为某种缘分吧。{wait}'
				'{page}'
				'如果你们有什么苦恼的事，\n'
				'不用客气，可以尽管来找我帮忙。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0004F玛利亚贝尔小姐……\n'
				'实在非常感谢您。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#0102F#5P贝尔……真的谢谢你。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#0204F#5P……感谢您的关心。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(260), Text(
						'#0304F#5P哎，真是谢谢你啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
			Insn('TEXT_TALK', Char(339), Text(
				'#1105F？？？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x5A'),
			Insn('CHAR_SET_POS', Char(0), (29930, 4030, -13780), 180),
			Insn('CHAR_SET_FRAME', Char(17), 0),
			Insn('FLAG_SET', Flag(1447)),
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('EXPR_CHAR_ATTR', Char(339), 5, Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(17), 5, Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('SET'), Insn('END')])),
			Insn('TEXT_START', Char(17)),
			Insn('CHAR_FLAG1_UNSET', Char(17), 16),
			Insn('CHAR_WATCH', Char(17), Char(339), 0),
			Insn('EXPR_CHAR_ATTR', Char(17), 4, Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(17), 4, Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(17), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(17), 5, Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
			Insn('IF', [
				(Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
				(Expr([Insn('CHAR_ATTR', Char(17), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
					Insn('EXPR_CHAR_ATTR', Char(17), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
				]),
				(Expr([Insn('CHAR_ATTR', Char(17), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
					Insn('EXPR_CHAR_ATTR', Char(17), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, [
					Insn('EXPR_CHAR_ATTR', Char(17), 8, Expr([Insn('CHAR_ATTR', Char(17), 5), Insn('SET'), Insn('END')])),
				]),
			]),
			Insn('EXPR_CHAR_ATTR', Char(17), 4, Expr([Insn('CHAR_ATTR', Char(339), 5), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(339), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(17), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('CHAR_FLAG1_SET', Char(17), 16),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('END')]), [
					Insn('TEXT_TALK', Char(339), Text(
						'#1106F嗯～还是算了吧。{wait}'
						'{page}'
						'#1110F琪雅想和罗伊德他们\n'
						'待在一起呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(17), Text(
						'#2905F啊，这可真是遗憾啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EXPR_CHAR_ATTR', Char(257), 5, Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(17), 5, Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('SET'), Insn('END')])),
					Insn('TEXT_START', Char(17)),
					Insn('CHAR_FLAG1_UNSET', Char(17), 16),
					Insn('CHAR_WATCH', Char(17), Char(257), 0),
					Insn('EXPR_CHAR_ATTR', Char(17), 4, Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(17), 4, Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(17), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(17), 5, Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
					Insn('IF', [
						(Expr([Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(17), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
						(Expr([Insn('CHAR_ATTR', Char(17), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
							Insn('EXPR_CHAR_ATTR', Char(17), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
						]),
						(Expr([Insn('CHAR_ATTR', Char(17), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
							Insn('EXPR_CHAR_ATTR', Char(17), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
						]),
						(None, [
							Insn('EXPR_CHAR_ATTR', Char(17), 8, Expr([Insn('CHAR_ATTR', Char(17), 5), Insn('SET'), Insn('END')])),
						]),
					]),
					Insn('EXPR_CHAR_ATTR', Char(17), 4, Expr([Insn('CHAR_ATTR', Char(257), 5), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(257), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
					Insn('EXPR_CHAR_ATTR', Char(17), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
					Insn('CHAR_FLAG1_SET', Char(17), 16),
					Insn('SLEEP', 300),
					Insn('TEXT_TALK', Char(17), Text(
						'#2910F（瞪……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0011F（是、是我的错吗！？）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(17), Text(
						'#2902F呵呵，不过……{wait}'
						'{page}'
						'真的比罗赞贝尔克的\n'
						'人偶可爱多了。{wait}'
						'{page}'
						'#2909F你是叫做琪雅吗？\n'
						'要不要来姐姐\n'
						'家玩啊？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(339), Text(
						'#1105F罗伊德他们也一起去吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(17), Text(
						'#2901F不，至少\n'
						'罗伊德是不会去的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(0), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('EMOTE', Char(1), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F（又被莫名其妙地敌视了……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(258), Text(
								'#0106F#5P（灾难啊……罗伊德。）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(259), Text(
								'#0204F#5P（真是令人同情。）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(260), Text(
								'#0309F#5P（哇哈哈，大快人心啊。）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, []),
					]),
					Insn('FLAG_SET', Flag(8)),
				]),
			]),
			Insn('CHAR_SET_FRAME', Char(17), 0),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(17), 0),
	Insn('TEXT_END', Char(17)),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1913)), Insn('END')]), [
			Insn('TEXT_TALK', Char(18), Text(
				'#3504F好了，帝国的工作\n'
				'都已经完成了。{wait}'
				'{page}'
				'#3500F要不要在克洛斯贝尔\n'
				'多放松几天呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0003F（……这人真是令人琢磨不透……\n'
				'\u3000他到底知道些什么呢……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('EMOTE', Char(18), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('CHAR_WATCH', Char(18), Char(0), 300),
			Insn('TEXT_TALK', Char(18), Text(
				'#3500F嗯，你们也来看书吗？{wait}'
				'{page}'
				'#3509F哎呀，真是好巧啊。\n'
				'遇到了同样喜欢读书的朋友，我也很高兴哦丅{wait}'
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
				'#0006F那、那个……\n'
				'都不知道该说什么才好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0203F不管怎么想，\n'
				'他肯定都不是来读书的……\n'
				'而且还故意装出一副轻松自然的样子……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0306F（……算了吧，要是跟他认真起来的话，\n'
				'\u3000脑子会坏掉的。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1666)), Insn('END')]), [
					Insn('TEXT_TALK', Char(258), Text(
						'#0105F不过，雷克多先生，\n'
						'您不是有事\n'
						'要回帝国吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(18), Text(
						'#3505F啊，是啊……{wait}'
						'{page}'
						'#3500F虽然说是回帝国，\n'
						'但也用不了多长时间。{wait}'
						'{page}'
						'就在贝尔加德门附近而已。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(0), 0, 2000, (24, 27, 250, 0)),
					Insn('EMOTE', Char(1), 0, 2000, (24, 27, 250, 0)),
					Insn('EMOTE', Char(2), 0, 2000, (24, 27, 250, 0)),
					Insn('EMOTE', Char(3), 0, 2000, (24, 27, 250, 0)),
					Insn('SLEEP', 1000),
					Insn('EMOTE_STOP', Char(65535)),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F（……贝尔加德门附近？）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0105F（莫非是……『加雷利亚要塞』！？）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0305F（也太诡异了吧……\n'
						'\u3000那可是帝国最重要的一个据点啊！？）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0211F（不像是普通平民\n'
						'\u3000会去的地方啊。\n'
						'\u3000他到底是什么人呢……）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(258), Text(
						'#0106F（……我觉得…………\n'
						'\u3000还是不要对他\n'
						'\u3000太认真比较好……）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('CHAR_ROTATE', Char(18), 90, 0),
			Insn('FLAG_SET', Flag(1913)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('TEXT_START', Char(255)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{0x06} \u3000～\u3000本月新刊\u3000～\n'
				'\u3000玛尔克与森林深处的魔女丄下\n'
				'\u3000放置于一楼书架中。\n'
				'\u3000有兴趣的客人请前去借阅。\n'
				'\u3000★该书十分抢手，\n'
				'\u3000\u3000想借书的客人\n'
				'\u3000\u3000请尽快行动！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('0x5A'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{0x06}\u3000\u3000～\u3000本月新刊\u3000～\n'
				'\u3000\u3000\u3000\u3000 准备中{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('0x5A'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{0x06}\u3000\u3000 ～\u3000本月新刊\u3000～\n'
				'\u3000\u3000\u3000圣女与白狼丄下\n'
				'\u3000放置于一楼书架中。\n'
				'\u3000有兴趣的客人请前去借阅。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('0x5A'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{0x06} \u3000～\u3000本月新刊\u3000～\n'
				'\u3000玛尔克与森林深处的魔女丄中\n'
				'\u3000\u3000\u3000\u3000季刊丄垂涎\n'
				'\u3000放置于一楼书架中。\n'
				'\u3000有兴趣的客人请前去借阅。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('0x5A'),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{0x06}\u3000\u3000 ～\u3000本月新刊\u3000～\n'
				'\u3000\u3000\u3000圣女与白狼丄上\n'
				'\u3000放置于一楼书架中。\n'
				'\u3000有兴趣的客人请前去借阅。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('0x5A'),
		]),
		(None, [
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{0x06} \u3000～\u3000本月新刊\u3000～\n'
				'\u3000玛尔克与森林深处的魔女丄上\n'
				'\u3000放置于一楼书架中。\n'
				'\u3000有兴趣的客人请前去借阅。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_SET_POS', -1, 280, 60, 3),
			Insn('0x5A'),
		]),
	]),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}书架上有《玛尔克与森林深处的魔女》一书。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('MENU', 0, -1, -1, 1, Text(
				'【阅读上卷】\n'
				'【阅读中卷】\n'
				'【阅读下卷】\n'
				'【放弃】\n'
			)),
			Insn('MENU_WAIT', 0),
			Insn('0x60', 0),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('0xBB', b'\xd6\x02\xff\x00'),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
					Insn('0xBB', b'\xdd\x02\xff\x00'),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
					Insn('0xBB', b'\xde\x02\xff\x00'),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('MENU', 0, -1, -1, 1, Text(
				'【阅读上卷】\n'
				'【阅读中卷】\n'
				'【放弃】\n'
			)),
			Insn('MENU_WAIT', 0),
			Insn('0x60', 0),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('0xBB', b'\xd6\x02\xff\x00'),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
					Insn('0xBB', b'\xdd\x02\xff\x00'),
				]),
				(None, []),
			]),
		]),
		(None, [
			Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('MENU', 0, -1, -1, 1, Text(
				'【阅读上卷】\n'
				'【放弃】\n'
			)),
			Insn('MENU_WAIT', 0),
			Insn('0x60', 0),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('0xBB', b'\xd6\x02\xff\x00'),
				]),
				(None, []),
			]),
		]),
	]),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}书架上有《季刊丄垂涎》一书。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('MENU', 0, -1, -1, 1, Text(
		'【阅读此书】\n'
		'【放弃】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('0xBB', b'\xdc\x02\xff\x00'),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('RECIPE', 18)), Insn('NOT'), Insn('END')]), [
					Insn('FADE_ON', 300, Color(0x00000000), 100),
					Insn('TEXT_SET_POS', -1, -1, -1, -1),
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('SOUND_PLAY', 17, 0, 0, 100),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'#0C书里写着{item 452}{color 0}的做法。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'#0C记住了{item 452}{color 0}的食谱。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('FADE_OFF', 300, Color(0x00000000)),
					Insn('TEXT_SET_POS', -1, 280, 60, 3),
					Insn('0x5A'),
					Insn('RECIPE', 18),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][28] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}书柜上有《改变大陆的美丽女性》一书。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('MENU', 0, -1, -1, 1, Text(
		'【阅读此书】\n'
		'【放弃】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('0xBB', b'\xd7\x02\xff\x00'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][29] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}书柜上有《５分钟零碎时间的善用方法》一书。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('MENU', 0, -1, -1, 1, Text(
		'【阅读此书】\n'
		'【放弃】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('0xBB', b'\xd8\x02\xff\x00'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][30] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}书柜上有《铁路迷的私房行程》一书。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('MENU', 0, -1, -1, 1, Text(
		'【阅读此书】\n'
		'【放弃】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('0xBB', b'\xd5\x02\xff\x00'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][31] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}书柜上有《克洛斯贝尔怪谈全集》一书。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('MENU', 0, -1, -1, 1, Text(
		'【阅读此书】\n'
		'【放弃】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('0xBB', b'\xd9\x02\xff\x00'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][32] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}书柜上有《圣女与白狼》一书。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('MENU', 0, -1, -1, 1, Text(
				'【阅读上卷】\n'
				'【阅读下卷】\n'
				'【放弃】\n'
			)),
			Insn('MENU_WAIT', 0),
			Insn('0x60', 0),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('0xBB', b'\xdf\x02\xff\x00'),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
					Insn('0xBB', b'\xe0\x02\xff\x00'),
				]),
				(None, []),
			]),
		]),
		(None, [
			Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('MENU', 0, -1, -1, 1, Text(
				'【阅读上卷】\n'
				'【放弃】\n'
			)),
			Insn('MENU_WAIT', 0),
			Insn('0x60', 0),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('0xBB', b'\xdf\x02\xff\x00'),
				]),
				(None, []),
			]),
		]),
	]),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][33] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}书柜上有《彩虹丄剧迷纪念册》一书。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('MENU', 0, -1, -1, 1, Text(
		'【阅读此书】\n'
		'【放弃】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('0xBB', b'\xda\x02\xff\x00'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][34] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('EQ'), Insn('END')], [
		Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('Ａ～Ｚ')),
		Insn('TEXT_SET_NAME', Translate('')),
		Insn('MENU', 0, -1, -1, 1, Text(
			'【ＩＢＣ】\n'
			'【ＺＣＦ】\n'
			'【放弃】\n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('0x60', 0),
		Insn('0xDB'),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('ＩＢＣ（International Bank of Crossbell）')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}『克洛斯贝尔国际银行』的简称。\n'
					'这所巨大银行管理、运用着\n'
					'从大陆全境汇集而来的庞大资产。\n'
					'不仅限于克洛斯贝尔，同时也\n'
					'常年支撑着国际金融、经济市场。{wait}'
					'{page}'
					'除了投资活动和金融商品的开发，\n'
					'其业务还涉及到主题乐园运营等领域，\n'
					'并且也积极为爱普斯泰恩财团的\n'
					'『导力网络计划』提供运作资金。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('ＺＣＦ（Zeiss Central Factory）')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}『蔡斯中央工房』的简称。\n'
					'ＺＣＦ位于利贝尔王国的蔡斯市，\n'
					'由导力器的发明者──爱普斯泰恩博士的\n'
					'直系弟子Ａ丄拉塞尔博士，\n'
					'与蔡斯钟表师工会联合创办，\n'
					'其前身为『蔡斯技术工房』。{wait}'
					'{page}'
					'ＺＣＦ成功率先开发了导力飞行船，\n'
					'是大陆上首屈一指的导力器制造商，\n'
					'近年，它更是成功制造了\n'
					'利贝尔王国军的高速巡洋舰『埃尔赛尤』。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
	]),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][35] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('EQ'), Insn('END')], [
		Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('书架１')),
		Insn('TEXT_SET_NAME', Translate('')),
		Insn('MENU', 0, -1, -1, 1, Text(
			'【彩虹剧团】\n'
			'【亚尔特利亚法典国】\n'
			'【乌尔努公司】\n'
			'【埃雷波尼亚帝国】\n'
			'【爱普斯泰恩财团】\n'
			'【放弃】 \n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('0x60', 0),
		Insn('0xDB'),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('彩虹剧团')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}位于克洛斯贝尔自治州，\n'
					'是世界著名的剧团。{wait}'
					'{page}'
					'其技巧高超的表演\n'
					'与激情华丽的舞台，\n'
					'让许多观众如痴如醉。{wait}'
					'{page}'
					'特别是被誉为『炎之舞姬』的\n'
					'现任红牌女演员伊莉雅丄普拉提耶\n'
					'受到了极大欢迎，\n'
					'其狂热追随者遍布周边各国。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('亚尔特利亚法典国')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}亚尔特利亚法典国是七耀教会的总部所在地。\n'
					'这座城国位于塞姆利亚大陆的中心地区，\n'
					'并作为全大陆的信徒与宗教相关人员\n'
					'齐聚的圣地而声名远扬。{wait}'
					'{page}'
					'其中设有全权负责祭祀仪式相关事宜的『典礼省』，\n'
					'据传负责管理女神圣物的『封圣省』，\n'
					'以及负责城市保卫任务的『僧兵厅』等\n'
					'各式各样的组织。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('乌尔努公司')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}总部位于卡尔瓦德共和国，\n'
					'是一家巨大的综合技术制造商。{wait}'
					'{page}'
					'与埃雷波尼亚帝国的莱恩福尔特公司\n'
					'同为武器和兵器开发领域的两大老牌公司，\n'
					'但自从导力器出现后，\n'
					'就开始着手研究和开发一切导力产品。{wait}'
					'{page}'
					'其中在导力驱动车的领域，\n'
					'以导力巴士为首，从家用车到特殊车辆的开发，\n'
					'乌尔努公司都有着卓越的成绩。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('埃雷波尼亚帝国')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}位于克洛斯贝尔自治州西部，\n'
					'是一个以『黄金战马』为国徽的巨大帝国。\n'
					'现任皇帝为尤根特丄莱泽丄亚诺尔。{wait}'
					'{page}'
					'该国家由大贵族支配，虽然体制陈旧，\n'
					'但在被誉为『铁血宰相』──出身军队的\n'
					'吉利亚斯丄奥斯本宰相的推动下，\n'
					'国土全境铺设了铁路，正逐渐向近代化发展。{wait}'
					'{page}'
					'整个国家除了机械化的正规军之外，\n'
					'还设有贵族的私人军队等，军事力量十分强大，\n'
					'因此周边诸国都对其常年保持警戒。{wait}'
					'{page}'
					'另外，皇帝之子──奥利巴特皇子\n'
					'去年帮助解决了利贝尔的异变事件，\n'
					'这在帝国内引起了很大反响。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 4), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('爱普斯泰恩财团')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}继承了发明导力器的天才导力学者\n'
					'Ｃ丄爱普斯泰恩博士辉煌成就的财团。\n'
					'在研究机关与制造商的领域中也有很强实力，\n'
					'特别擅长通讯及情报处理等领域。{wait}'
					'{page}'
					'另外，此财团是能够驱动魔法的\n'
					'『战术导力器』的唯一开发制造商，\n'
					'近年来，还在致力于研究开发\n'
					'通讯及情报处理技术领域的尖端工程『导力网络计划』。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
	]),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][36] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('EQ'), Insn('END')], [
		Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('书架２')),
		Insn('TEXT_SET_NAME', Translate('')),
		Insn('MENU', 0, -1, -1, 1, Text(
			'【怪盗Ｂ】\n'
			'【卡尔瓦德共和国】\n'
			'【克洛斯贝尔自治州】\n'
			'【结晶回路】\n'
			'【古代遗物】\n'
			'【放弃】\n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('0x60', 0),
		Insn('0xDB'),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('怪盗Ｂ')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}活动领域覆盖大陆全境，神出鬼没的大盗。\n'
					'小到宝石，大至导力战车，\n'
					'无论所有者是国家还是个人，都可以成功盗走，\n'
					'据说由于其手法华丽，甚至获得了\n'
					'一部分狂热的崇拜者。{wait}'
					'{page}'
					'他总是将别有寓意的信息送至各地，\n'
					'虽然有人见到过他戴着面具，身披白色斗篷的样子，\n'
					'但其真实面目一直是个谜。\n'
					'近年来，他号称要进行『美的解放活动』，\n'
					'在埃雷波尼亚帝国犯下了一系列\n'
					'华丽并且无法侦破的罪行，再次引起了新话题。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('卡尔瓦德共和国')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}位于克洛斯贝尔自治州东部，\n'
					'在百年前便推行了民主化。\n'
					'现任国家元首是洛克史密斯总统。{wait}'
					'{page}'
					'该国家幅员辽阔，\n'
					'因有着许多东方移民，\n'
					'所以文化背景也丰富多彩。{wait}'
					'{page}'
					'虽然在《不战条约》签订之后，态度便一直保持低调，\n'
					'但在历史上，该国家与埃雷波尼亚帝国之间\n'
					'曾发生过数次冲突。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('克洛斯贝尔自治州')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}位于塞姆利亚大陆西部。\n'
					'处在埃雷波尼亚帝国\n'
					'和卡尔瓦德共和国这两个大国之间，\n'
					'曾经是激烈领土争端的对象，\n'
					'但七十年前作为自治州成立了。{wait}'
					'{page}'
					'现在，其中心克洛斯贝尔市已经发展为\n'
					'大陆首屈一指的巨大贸易都市，\n'
					'以及连接帝国和共和国的横断大陆铁道\n'
					'和国际定期飞行船的中转站。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('结晶回路')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}用七耀石的碎片『耀晶石』精制加工而成，\n'
					'拥有结晶构造的回路。{wait}'
					'{page}'
					'是既能作为能量源使用，\n'
					'又可以引发各种现象的装置，\n'
					'但若未设置于导力器内部，\n'
					'便发挥不出功效。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 4), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('古代遗物')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}与导力器同样都是利用导力运作，\n'
					'但运转原理不尽相同，是古代文明的导力器。{wait}'
					'{page}'
					'据说是『古代塞姆利亚文明』时代\n'
					'的产物，仅凭现代技术\n'
					'是无法对其进行解析的。{wait}'
					'{page}'
					'古代遗物在大陆各地的遗迹中都\n'
					'有过少量发现，其中有不少遗物\n'
					'甚至拥有超越常理的强大力量。{wait}'
					'{page}'
					'因此七耀教会将古代遗物\n'
					'定义为『女神过早的馈赠』，\n'
					'并负责将其回收管理。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
	]),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][37] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('EQ'), Insn('END')], [
		Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('书架３')),
		Insn('TEXT_SET_NAME', Translate('')),
		Insn('MENU', 0, -1, -1, 1, Text(
			'【七耀教会】\n'
			'【七耀石】\n'
			'【放弃】\n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('0x60', 0),
		Insn('0xDB'),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('七耀教会')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}信奉在塞姆利亚大陆上拥有最多信徒的\n'
					'『空之女神爱德斯』的宗教组织。\n'
					'其总部位于亚尔特利亚法典国。{wait}'
					'{page}'
					'自导力革命之后，虽然影响力略有降低，\n'
					'但目前在大陆上仍然拥有很强的影响力，\n'
					'该组织一般是由知识、教育、医疗等领域\n'
					'来启蒙民众。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('七耀石')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}散布于全大陆的七种珍贵宝石。\n'
					'该宝石自古以来\n'
					'就被视为某种神秘的象征而极其珍贵。{wait}'
					'{page}'
					'近代出现了一种技术，\n'
					'能够将体积过小，无法打磨成宝石的七耀石碎片\n'
					'『耀晶石』进行精制丄加工，制成结晶回路，\n'
					'这项发明使七耀石资源的重要性\n'
					'在大陆各国间陡然增大。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
	]),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][38] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('EQ'), Insn('END')], [
		Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('书架４')),
		Insn('TEXT_SET_NAME', Translate('')),
		Insn('MENU', 0, -1, -1, 1, Text(
			'【大崩坏】\n'
			'【钓公师团】\n'
			'【导力革命】\n'
			'【导力器】\n'
			'【放弃】\n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('0x60', 0),
		Insn('0xDB'),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('大崩坏')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}指发生于一千两百年前，古代塞姆利亚文明\n'
					'的毁灭。有资料称它是由天地异变所引发的，\n'
					'但具体原因仍然不明。{wait}'
					'{page}'
					'『大崩坏』导致文明消失之后，\n'
					'人们度过了漫长的『黑暗时代』。{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('钓公师团')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}旨在普及钓鱼文化，\n'
					'是垂钓界的专业组织。\n'
					'该组织由一位原为贵族的钓鱼爱好者\n'
					'Ｈ丄费瑟尔先生所发起，\n'
					'其总部位于利贝尔王国的格兰赛尔市。{wait}'
					'{page}'
					'主要活动为进行钓场的探访、调查、开发，\n'
					'并致力于发掘培养新一代钓师，\n'
					'另外，钓公师团近年也开始着手开发钓具、钓饵等，\n'
					'其活动领域正在逐年扩大。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('导力革命')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}大约在五十年前，\n'
					'导力器的发明\n'
					'引发了全大陆的技术革新。{wait}'
					'{page}'
					'虽然导力器是划时代的发明，\n'
					'但当时人们却对其持怀疑态度，\n'
					'直到爱普斯泰恩财团的导力通讯器及\n'
					'ＺＣＦ的导力飞行船问世后，\n'
					'其实用性才被全大陆所承认。{wait}'
					'{page}'
					'现在，从取暖设备与照明设备等日用品，\n'
					'到列车、飞行船、战车及大炮等兵器，\n'
					'所有设备都已经得到导力化，\n'
					'导力器对人们来说，\n'
					'已经变得必不可少。{wait}'
					'{page}'
					'近几年，随着导力机械的小型化，\n'
					'乌尔努公司和莱恩福尔特公司对\n'
					'高性能导力驱动车的开发也在不断进步，\n'
					'其产品已经开始在一般民众间普及开来。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('导力器')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}由Ｃ丄爱普斯泰恩博士发明，\n'
					'借由引出七耀石中的导力，\n'
					'来引发种种现象的机械的总称。{wait}'
					'{page}'
					'导力器利用其内在构造及齿轮运转，\n'
					'使由七耀石加工而来的结晶回路互相干涉，\n'
					'从而引发无数种现象。{wait}'
					'{page}'
					'导力器的实用性之强，\n'
					'不仅在于能引发各种现象，并且『随时间流逝内部的\n'
					'导力会逐渐恢复』，从经济效率上看远远\n'
					'高于外燃、内燃机械。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
	]),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][39] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('EQ'), Insn('END')], [
		Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('书架５')),
		Insn('TEXT_SET_NAME', Translate('')),
		Insn('MENU', 0, -1, -1, 1, Text(
			'【导力魔法】\n'
			'【导力网络计划】\n'
			'【东方人街】\n'
			'【放弃】\n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('0x60', 0),
		Insn('0xDB'),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('导力魔法')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}通过将结晶回路装入爱普斯泰恩财团\n'
					'特别设计的『战术导力器』中，\n'
					'从而得以发动的『魔法』。{wait}'
					'{page}'
					'一般被称为『导力魔法』，\n'
					'只要经过训练，每个人都能使用，\n'
					'因此广泛普及于军队、警察、游击士协会等组织。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('导力网络计划')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}爱普斯泰恩财团正在开发研究的，\n'
					'具有革命性意义的信息网路计划。\n'
					'此计划以导力缆线连接各终端，\n'
					'让交换以及处理大量信息成为可能。{wait}'
					'{page}'
					'虽然原本与利贝尔的ＺＣＦ\n'
					'共同推进此计划，但现在\n'
					'由于接受了ＩＢＣ的资金援助，所以开始正\n'
					'式在克洛斯贝尔市进行了导入实验。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('东方人街')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}位于卡尔瓦德共和国，\n'
					'是东方移民所筑起的大规模街道。\n'
					'东方人街汇聚了各种文化、人种、物资，\n'
					'被誉为『东西文化的交叉点』。{wait}'
					'{page}'
					'充满异国情调的建筑物鳞次栉比，\n'
					'是享有盛名的观光地，但遗憾的是\n'
					'据传闻说，东方人街中也存在庞大的黑手党组织。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
	]),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][40] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('EQ'), Insn('END')], [
		Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('书架６')),
		Insn('TEXT_SET_NAME', Translate('')),
		Insn('MENU', 0, -1, -1, 1, Text(
			'【百日战役】\n'
			'【不战条约】\n'
			'【放弃】\n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('0x60', 0),
		Insn('0xDB'),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('百日战役')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}百日战役是七耀历１１９２年，埃雷波尼亚帝国\n'
					'向利贝尔王国发动的一场侵略战争。\n'
					'因为从帝国宣战开始，到七耀教会\n'
					'协调双方结束战争，\n'
					'大约进行了一百天，\n'
					'所以被称为『百日战役』。{wait}'
					'{page}'
					'当时利贝尔处于绝对劣势，\n'
					'领土大半都已被帝国军队占领，\n'
					'但在使用当时最先进的警备飞艇\n'
					'发起闪电般的反击战后，\n'
					'战况瞬间便被颠覆。{wait}'
					'{page}'
					'关于开战理由，\n'
					'因为两国都对此保持沉默，\n'
					'所以至今仍然是个谜。\n'
					'战争结束之后，帝国政府将其称为\n'
					'『由不幸的误会而产生的错误』，\n'
					'并向利贝尔发表了正式的谢罪声明。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('不战条约')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}不战条约是七耀历１２０２年，利贝尔王国、\n'
					'埃雷波尼亚帝国和卡尔瓦德共和国\n'
					'三国间签订的一则国际条约。\n'
					'该条约由利贝尔的艾莉西亚女王发起，\n'
					'在该国的艾尔贝离宫签订。{wait}'
					'{page}'
					'该条约虽然不具备法律强制力，\n'
					'但条约签订后，帝国和共和国便终止了\n'
					'在克洛斯贝尔自治州近郊举行的\n'
					'大规模军事演习，\n'
					'使紧张的局势大为缓和，\n'
					'可以说，此条约起到了立竿见影的效果。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
	]),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][41] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('EQ'), Insn('END')], [
		Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('书架７')),
		Insn('TEXT_SET_NAME', Translate('')),
		Insn('MENU', 0, -1, -1, 1, Text(
			'【米修拉姆】\n'
			'【游击士协会】\n'
			'【放弃】\n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('0x60', 0),
		Insn('0xDB'),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('米修拉姆')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}米修拉姆是位于艾尔姆湖东南边的一处高级游憩区，\n'
					'两年前，ＩＢＣ开始着手进行开发后，\n'
					'此地便建成了度假饭店和主题乐园等，\n'
					'并成为大受欢迎的观光旅游地点。{wait}'
					'{page}'
					'被称为『咪西』\n'
					'的当地吉祥物，\n'
					'也十分受市民和游客的欢迎。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('游击士协会')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}为了保护地区和平与平民的安全，\n'
					'游击士们所成立的民间团体。\n'
					'由于协会在塞姆利亚大陆全境都设有分部，\n'
					'所以影响力与发言力也不容小觑。{wait}'
					'{page}'
					'协会的理念可以说是\n'
					'以保护平民的安全为优先，\n'
					'但相对的，为了不威胁到平民的安全，\n'
					'所以协会无法行使对国家与政府权力者的\n'
					'搜查权和逮捕权，这是其组织守则上的弱点之一。{wait}'
					'{page}'
					'而且克洛斯贝尔分部所接到的国际性案件较多，\n'
					'因此集中于此处的人才都尤其优秀，\n'
					'其中，『风之剑圣』亚里欧斯丄马克莱因\n'
					'更是获得了市民的极大支持。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
	]),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][42] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('EQ'), Insn('END')], [
		Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('书架８')),
		Insn('TEXT_SET_NAME', Translate('')),
		Insn('MENU', 0, -1, -1, 1, Text(
			'【莱恩福尔特公司】\n'
			'【雷米菲利亚公国】\n'
			'【列曼自治州】\n'
			'【利贝尔王国】\n'
			'【猎兵团】\n'
			'【放弃】\n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('0x60', 0),
		Insn('0xDB'),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('莱恩福尔特公司')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}总部位于埃雷波尼亚帝国，\n'
					'是一家巨大的综合技术制造商。\n'
					'前身是专门制造使用火药的\n'
					'大炮以及重型武器的兵器工房。{wait}'
					'{page}'
					'自从导力器问世之后，\n'
					'便转而制造导力枪与导力兵器，\n'
					'并涉足导力列车与飞行船等领域，\n'
					'最终发展为与卡尔瓦德共和国的『乌尔努公司』\n'
					'齐名的，世界两大制造商之一。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('雷米菲利亚公国')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}雷米菲利亚公国位于塞姆利亚大陆北部。\n'
					'虽然处于自然环境严酷的北方，\n'
					'但有着茂密的森林与清澈的湖泊，\n'
					'风光明媚、景色秀丽，\n'
					'吸引了众多游客前来观光。{wait}'
					'{page}'
					'雷米菲利亚公国同时也是著名的医疗发达国家，\n'
					'集中了全大陆的顶尖医疗器械制造商，\n'
					'并且培养了许多优秀的医生。\n'
					'克洛斯贝尔自治州的圣乌尔斯拉医科大学\n'
					'也是由雷米菲利亚公国协助设立的。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('列曼自治州')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}列曼自治州位于塞姆利亚大陆中部。\n'
					'不仅是爱普斯泰恩财团的总部所在地，\n'
					'同时也是Ｃ丄爱普斯泰恩博士的故乡。{wait}'
					'{page}'
					'除此之外，在全大陆都设有分部的\n'
					'游击士协会的总部也设于该国。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('利贝尔王国')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}利贝尔王国位于塞姆利亚大陆西南部。\n'
					'自古以来就拥有丰富绚丽的自然风光，\n'
					'现在，利贝尔王国在老女王艾莉西亚Ⅱ世的治理下，\n'
					'局势稳定，以和平著称。{wait}'
					'{page}'
					'虽然与周边诸国相比，国力稍显逊色，\n'
					'但凭借丰富的七耀石资源和先进的技术，\n'
					'加上灵活的外交政策，\n'
					'使其与各国建立了平等友好的关系。{wait}'
					'{page}'
					'去年，在王国中央的瓦雷利亚湖上\n'
					'出现了神秘的巨大物体（详情不明），\n'
					'并使王国全境的导力全部停止运转，\n'
					'所幸，此危机最后被军队和游击士协会\n'
					'顺利解决了。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('FLAG_SET', Flag(1529)),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 4), Insn('EQ'), Insn('END')]), [
				Insn('MENU_TITLE', b'\xff\xff\x19\x00\x00\x00', Translate('猎兵团')),
				Insn('TEXT_SET_POS', -1, 70, -1, -1),
				Insn('TEXT_SET_NAME', Translate('')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}指代大陆各国的佣兵部队中\n'
					'最优秀的部队时所使用的称号。{wait}'
					'{page}'
					'雇主可依据规模和目的与其灵活地订立合约，\n'
					'再加上猎兵拥有着强大的战斗力，\n'
					'因此常作为私人武装被雇佣，\n'
					'但有的国家也明令禁止其在境内活动。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0xDB'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			]),
			(None, []),
		]),
	]),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][43] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (5720, 800, 8440), 0),
	Insn('CAM_ROTATE', 45, 23, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 18730, 0),
	Insn('CHAR_SET_POS', Char(257), (5000, 150, 7300), 90),
	Insn('CHAR_SET_POS', Char(258), (4750, 150, 8300), 90),
	Insn('CHAR_SET_POS', Char(259), (3500, 150, 7300), 90),
	Insn('CHAR_SET_POS', Char(260), (3250, 150, 8300), 90),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F叔叔，您好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P哦，是罗伊德啊，\n'
		'欢迎欢迎。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P今天你们是来借书的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F不，今天是因为工作而来的。{wait}'
		'{page}'
		'您不是向特务支援课\n'
		'提出了委托吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#5P#0100F好像是……\n'
		'回收逾期未还的书籍。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P哦，没错没错，\n'
		'我确实提出了那样的委托。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P那我就开始说明\n'
		'委托的内容了哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('QUEST', 5, Insn('TASK_SET', 0)),
	Insn('CALL', Function((0, 45))),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('CALL', Function((0, 46))),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_POS', Char(0), (5000, 150, 7800), 90),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][44] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (5720, 800, 8440), 0),
	Insn('CAM_ROTATE', 45, 23, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 18730, 0),
	Insn('CHAR_SET_POS', Char(257), (5000, 150, 7300), 90),
	Insn('CHAR_SET_POS', Char(258), (4750, 150, 8300), 90),
	Insn('CHAR_SET_POS', Char(259), (3500, 150, 7300), 90),
	Insn('CHAR_SET_POS', Char(260), (3250, 150, 8300), 90),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P我确实提出了有关\n'
		'回收逾期未还书籍的委托。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P那我就开始说明\n'
		'委托的内容了哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CALL', Function((0, 45))),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('CALL', Function((0, 46))),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_POS', Char(0), (5000, 150, 7800), 90),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][45] = [
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, -1, 0, Text(
		'【接受】\n'
		'【拒绝】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0006F那个……\n'
				'不好意思，现在有些不太方便……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P嗯，这样啊？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P那就等你们有空了\n'
				'再说吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][46] = [
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F嗯，没问题。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P嗯，谢谢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P最近，有很多人过了还书期限\n'
		'却还没有归还书籍。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P所以就想拜托你们\n'
		'去找那些借书者要回书籍。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0203F……原来如此。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#5P#5P#0300F这任务听上去\n'
		'好像不是很难啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F那么……\n'
		'那些人的住址\n'
		'您都知道吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P嗯，借阅人的资料\n'
		'都记在图书卡上了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P那我念给你们听了哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P首先是……\n'
		'西侧大道的公寓\n'
		'《贝尔海姆》的菲伊先生。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P接着是……\n'
		'东侧大道的公寓\n'
		'《洋槐庄园》的克拉莉丝女士。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P最后是……\n'
		'行政区克洛斯贝尔警察局总部的\n'
		'雷蒙德警官。{wait}'
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
	Insn('TEXT_TALK', Char(258), Text(
		'#5P#0106F雷、雷蒙德警官……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F抱、抱歉啊，叔叔。\n'
		'没想到我们警察局里也会有不按时还书的人……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P没关系，别在意。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P如果是看得太入迷所以\n'
		'忘记归还的话，\n'
		'我反而会感到开心。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0203F……我可不认为\n'
		'那些人不还书全都是出于这个原因……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(259), Char(258), 350),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0211F懒散之人还是很多的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(260), Char(259), 500),
	Insn('TEXT_TALK', Char(260), Text(
		'#5P#0306F什、什么啊，\n'
		'为什么要用那种冷冷的眼神看着我……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(259), 90, 500),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0200F不，没什么。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F总之。{wait}'
		'{page}'
		'#0000F委托内容我们已经明白了，\n'
		'接下来立刻就展开行动。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(260), 90, 500),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P嗯，真是帮大忙了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P收回三本书后，\n'
		'就拿回来交给我。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P罗伊德，\n'
		'万事拜托了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 80, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}任务【回收逾期未还的书籍】{color 0}开始！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('QUEST', 5, Insn('TASK_SET', 1)),
	Insn('RETURN'),
]

data['code'][47] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (5720, 800, 8440), 0),
	Insn('CAM_ROTATE', 45, 23, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 18730, 0),
	Insn('CHAR_SET_POS', Char(257), (5000, 150, 7300), 90),
	Insn('CHAR_SET_POS', Char(258), (4750, 150, 8300), 90),
	Insn('CHAR_SET_POS', Char(259), (3500, 150, 7300), 90),
	Insn('CHAR_SET_POS', Char(260), (3250, 150, 8300), 90),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P哦……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P莫非你们已经把那些\n'
		'逾期未还的书籍都收回来了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#5P#0300F这是当然啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F是的，叔叔。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'归还了{item 725}{color 0}。{wait}'
	)),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'归还了{item 726}{color 0}。{wait}'
	)),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'归还了{item 727}{color 0}。{wait}'
	)),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_WAIT'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_REMOVE', 725, 1),
	Insn('ITEM_REMOVE', 726, 1),
	Insn('ITEM_REMOVE', 727, 1),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P……嗯，\n'
		'三本书确实\n'
		'都收回了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P你们真是帮了大忙呢，\n'
		'能得到你们的帮助，\n'
		'实在太好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#5P#0100F呵呵……\n'
		'您能这么说，是我们的荣幸。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0200F……这样就算是完成任务了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P嗯嗯，辛苦了。\n'
		'如果还有什么需要的话，我会去找你们的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F嗯，请交给我们吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 9, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}任务【回收逾期未还的书籍】{color 0}完成！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FLAG_SET', Flag(6)),
	Insn('CHAR_SET_POS', Char(0), (5000, 150, 7800), 90),
	Insn('QUEST', 5, Insn('TASK_UNSET', 31)),
	Insn('QUEST', 5, Insn('TASK_SET', 5)),
	Insn('QUEST', 5, Insn('FLAG_UNSET', 16)),
	Insn('0x66', 3, 1),
	Insn('0x66', 4, 1),
	Insn('0x66', 6, 1),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][48] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (5720, 1000, 8220), 0),
	Insn('CAM_ROTATE', 44, 20, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 18730, 0),
	Insn('CHAR_SET_POS', Char(257), (5000, 150, 7300), 90),
	Insn('CHAR_SET_POS', Char(258), (4750, 150, 8300), 90),
	Insn('CHAR_SET_POS', Char(259), (3500, 150, 7300), 90),
	Insn('CHAR_SET_POS', Char(260), (3250, 150, 8300), 90),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(265), (4250, 0, 6300), 90),
			Insn('CHAR_FLAG1_UNSET', Char(4), 128),
			Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(266), (4250, 0, 6300), 90),
			Insn('CHAR_FLAG1_UNSET', Char(4), 128),
			Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
		]),
		(None, []),
	]),
	Insn('0x0D'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 0))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F叔叔，您好。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P哦，是罗伊德啊，\n'
				'欢迎欢迎。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P今天你们是来借书的吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F不，今天是因为工作而来的。{wait}'
				'{page}'
				'您不是向特务支援课\n'
				'提出了委托吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#5P#0100F好像是……\n'
				'回收逾期未还的书籍。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P哦，没错没错，\n'
				'我确实提出了那样的委托。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P那我就开始说明\n'
				'委托的内容了哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F叔叔，您好。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P哦，是罗伊德啊，\n'
				'欢迎欢迎。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P莫非，你们今天是为了……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F嗯，是因为工作而来的。{wait}'
				'{page}'
				'您不是向特务支援课\n'
				'提出了委托吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P嗯，果然……\n'
				'是来向我确认委托内容的啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P抱歉啊，还让你们跑一趟。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#5P#0100F任务内容是\n'
				'回收逾期未还的书籍吧，\n'
				'难道……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P嗯，这已经是第二次\n'
				'拜托你们了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P那我就开始说明\n'
				'委托的内容了哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('QUEST', 40, Insn('TASK_SET', 0)),
	Insn('CALL', Function((0, 50))),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('CALL', Function((0, 51))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('OR'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(4), 128),
			Insn('CHAR_FLAG2_SET', Char(4), 32768),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_POS', Char(0), (5000, 150, 7800), 90),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][49] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (5720, 1000, 8220), 0),
	Insn('CAM_ROTATE', 44, 20, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 18730, 0),
	Insn('CHAR_SET_POS', Char(257), (5000, 150, 7300), 90),
	Insn('CHAR_SET_POS', Char(258), (4750, 150, 8300), 90),
	Insn('CHAR_SET_POS', Char(259), (3500, 150, 7300), 90),
	Insn('CHAR_SET_POS', Char(260), (3250, 150, 8300), 90),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(265), (4250, 0, 6300), 90),
			Insn('CHAR_FLAG1_UNSET', Char(4), 128),
			Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(266), (4250, 0, 6300), 90),
			Insn('CHAR_FLAG1_UNSET', Char(4), 128),
			Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
		]),
		(None, []),
	]),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P我确实提出了有关\n'
		'回收逾期未还书籍的委托。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P那我就开始说明\n'
		'委托的内容了哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CALL', Function((0, 50))),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('CALL', Function((0, 51))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('OR'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(4), 128),
			Insn('CHAR_FLAG2_SET', Char(4), 32768),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_POS', Char(0), (5000, 150, 7800), 90),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][50] = [
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, -1, 0, Text(
		'【接受】\n'
		'【拒绝】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0006F抱歉，叔叔，\n'
				'现在有些不太方便……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P嗯，这样啊？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P那就等你们有空了\n'
				'再说吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][51] = [
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F嗯，没问题。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('TASK_GET', 0))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(15), Text(
				'#11P嗯，谢谢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P最近，有很多人过了还书期限\n'
				'却还没有归还书籍。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P所以就想拜托你们\n'
				'去找那些借书者要回书籍。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#6P#0203F……原来如此。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#5P#0300F这任务听上去\n'
				'好像不是很难啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P这个……就是因为并不简单，\n'
				'所以才令人头痛啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0005F……怎么回事？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P其实这次没有按时还书的人，\n'
				'都不是克洛斯贝尔市的市民。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P他们全都住在郊外。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#5P#0103F啊，那可就有点麻烦了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F那么……\n'
				'那些人的住址\n'
				'您都知道吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(15), Text(
				'#11P嗯，谢谢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P其实最近有很多人\n'
				'都没有按时还书。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P实在不好意思，\n'
				'但能不能再次拜托你们\n'
				'去收回逾期未还的书籍呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#6P#0200F不按时还书的人\n'
				'还是这么多啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#5P#0300F好，这次我们也会立刻\n'
				'就帮您解决的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P这个……就是因为并不简单，\n'
				'所以才令人头痛啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0005F……怎么回事？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P其实这次没有按时还书的人，\n'
				'都不是克洛斯贝尔市的市民。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P他们全都住在郊外。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#5P#0103F啊，那可就有点麻烦了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F那么……\n'
				'这批借书者的住址，\n'
				'您也都知道吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P嗯，我们在这方面还是不会马虎的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P首先是……\n'
		'住在阿尔摩利卡村的\n'
		'阿尔弗雷德。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P接着是……\n'
		'住在玛因兹的\n'
		'矿工罗基。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P最后是……\n'
		'乌尔斯拉医院的实习医生\n'
		'芙萝拉。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('EMOTE', Char(265), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
		]),
		(None, []),
	]),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F这还真是……\n'
		'彼此分散得很远啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#5P#0306F看来要绕\n'
		'自治州跑一圈了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0211F………………\n'
		'最讨厌不记得按时还书的散漫之人了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#5P#0100F别、别介意啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P……因为\n'
		'这次的范围实在太广了，\n'
		'所以我们的人手也不够。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P怎么样……\n'
		'你们愿意帮忙吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(265), Text(
				'#12P#0500F现在可以乘坐\n'
				'我的装甲车……\n'
				'这样就能够免去奔波之苦了吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0003F也是……{wait}'
				'{page}'
				'#0000F那就谢谢了，\n'
				'上士。{wait}'
				'{page}'
				'……那么，我们接下来\n'
				'就立刻展开行动。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F嗯，那就马上行动吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(266), Text(
				'#12P#0603F………………………………{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('FORK', 257, 2, [
				Insn('CHAR_ROTATE', Char(257), 315, 400),
			]),
			Insn('FORK', 258, 2, [
				Insn('CHAR_ROTATE', Char(258), 225, 400),
			]),
			Insn('FORK', 260, 2, [
				Insn('CHAR_ROTATE', Char(260), 135, 400),
			]),
			Insn('FORK', 259, 2, [
				Insn('CHAR_ROTATE', Char(259), 45, 400),
			]),
			Insn('FORK_AWAIT', Char(257), 2),
			Insn('FORK_AWAIT', Char(258), 2),
			Insn('FORK_AWAIT', Char(260), 2),
			Insn('FORK_AWAIT', Char(259), 2),
			Insn('TEXT_TALK', Char(258), Text(
				'#0106F（从刚才开始，达德利搜查官的\n'
				'\u3000眼神就很可怕啊……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#5P#0303F（而且还一言不发。\n'
				'\u3000但看样子也没打算阻止我们。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(15), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P怎么了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 257, 2, [
				Insn('CHAR_ROTATE', Char(257), 90, 400),
			]),
			Insn('FORK', 258, 2, [
				Insn('CHAR_ROTATE', Char(258), 90, 400),
			]),
			Insn('FORK', 260, 2, [
				Insn('CHAR_ROTATE', Char(260), 90, 400),
			]),
			Insn('FORK', 259, 2, [
				Insn('CHAR_ROTATE', Char(259), 90, 400),
			]),
			Insn('FORK_AWAIT', Char(257), 2),
			Insn('FORK_AWAIT', Char(258), 2),
			Insn('FORK_AWAIT', Char(260), 2),
			Insn('FORK_AWAIT', Char(259), 2),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F不，没什么。\n'
				'那我们就开始行动了。\n'
				'（尽量快些完成任务吧……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F嗯，请交给我们吧。\n'
				'那我们就开始行动了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P嗯，真是帮大忙了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P收回三本书后，\n'
		'就拿回来交给我。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P那么，支援课的各位，\n'
		'万事拜托了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 80, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}任务【回收自治州内逾期未还的书籍】{color 0}开始！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('QUEST', 40, Insn('TASK_SET', 1)),
	Insn('RETURN'),
]

data['code'][52] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (5720, 1000, 8220), 0),
	Insn('CAM_ROTATE', 44, 20, 0, 0),
	Insn('0x6E', 450, 0),
	Insn('CAM_DISTANCE', 18730, 0),
	Insn('CHAR_SET_POS', Char(257), (5000, 150, 7300), 90),
	Insn('CHAR_SET_POS', Char(258), (4750, 150, 8300), 90),
	Insn('CHAR_SET_POS', Char(259), (3500, 150, 7300), 90),
	Insn('CHAR_SET_POS', Char(260), (3250, 150, 8300), 90),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(265), (4250, 0, 6300), 90),
			Insn('CHAR_FLAG1_UNSET', Char(4), 128),
			Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(266), (4250, 0, 6300), 90),
			Insn('CHAR_FLAG1_UNSET', Char(4), 128),
			Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P哦……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P莫非你们已经把那些\n'
		'逾期未还的书籍都收回来了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#5P#0300F嗯，总算都收回来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F这边，叔叔。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'归还了{item 728}{color 0}。{wait}'
	)),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'归还了{item 729}{color 0}。{wait}'
	)),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'归还了{item 730}{color 0}。{wait}'
	)),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_WAIT'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_REMOVE', 728, 1),
	Insn('ITEM_REMOVE', 729, 1),
	Insn('ITEM_REMOVE', 730, 1),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 5, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('TEXT_TALK', Char(15), Text(
				'#11P……嗯，\n'
				'三本书确实\n'
				'都收回了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P真是不好意思，\n'
				'又麻烦了你们一次。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P加上上一次，\n'
				'实在是很感谢你们啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(15), Text(
				'#11P……嗯，\n'
				'三本书确实\n'
				'都收回了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#11P你们真是帮了大忙呢，\n'
				'能得到你们的帮助，\n'
				'实在太好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F哈哈……被叔叔这样表扬，\n'
		'真有点不好意思啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(265), Text(
				'#12P#0506F话说回来，\n'
				'处理支援请求这种工作\n'
				'好像还真是很辛苦呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#5P#0100F呵呵，这种工作对我们来说\n'
				'已经是家常便饭了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(266), Text(
				'#12P#0603F哼……这就是支援课\n'
				'平时处理的『支援请求』工作啊，\n'
				'真是浪费我的时间。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0006F唔……不、不好意思。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#5P#0103F因为这是我们的日常工作……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(258), Text(
				'#5P#0100F呵呵，虽然有些辛苦，\n'
				'但还是很有意义的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0203F……总之，\n'
		'这样就算是完成任务了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#11P嗯，辛苦了。\n'
		'真的非常感谢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F不用客气。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 9, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}任务【回收自治州内逾期未还的书籍】{color 0}完成！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('CHAR_SET_POS', Char(0), (5000, 150, 7800), 90),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('OR'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(4), 128),
			Insn('CHAR_FLAG2_SET', Char(4), 32768),
		]),
		(None, []),
	]),
	Insn('QUEST', 40, Insn('TASK_UNSET', 31)),
	Insn('QUEST', 40, Insn('TASK_SET', 11)),
	Insn('QUEST', 40, Insn('FLAG_UNSET', 16)),
	Insn('0x66', 5, 1),
	Insn('0x66', 7, 1),
	Insn('0x66', 9, 1),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][53] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (31560, 5020, -6480), 0),
	Insn('CAM_ROTATE', 45, 26, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 18590, 0),
	Insn('CHAR_SET_POS', Char(257), (30740, 4000, -6140), 135),
	Insn('CHAR_SET_POS', Char(258), (30340, 4000, -7790), 45),
	Insn('CHAR_SET_POS', Char(259), (29540, 4030, -6520), 135),
	Insn('CHAR_SET_POS', Char(260), (29440, 4030, -7890), 45),
	Insn('FORK_QUIT', Char(8), 0),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F怪盗Ｂ所说的『白隼』\n'
		'好像是利贝尔王国的国鸟。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#5P#0100F利贝尔王国是\n'
		'克洛斯贝尔的近邻，\n'
		'也是关系最好的国家。{wait}'
		'{page}'
		'难怪总觉得这个词\n'
		'在哪里听过。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_POS', Char(0), (30230, 4000, -6690), 90),
	Insn('CHAR_SET_POS', Char(8), (29310, 4000, 0), 0),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('FORK_FUNC', Char(8), 0, Function((0, 1))),
	Insn('QUEST', 34, Insn('TASK_SET', 4)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][54] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (29750, 5020, 5000), 0),
	Insn('CAM_ROTATE', 45, 26, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 23000, 0),
	Insn('CHAR_SET_POS', Char(257), (1310, 30, 750), 90),
	Insn('CHAR_SET_POS', Char(239), (1310, 30, -750), 90),
	Insn('CHAR_SET_POS', Char(339), (3610, 30, 0), 135),
	Insn('CAM_OFFSET', (29750, 5020, -5500), 5000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x6F', b'\x01'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (17860, 1020, -12620), 0),
	Insn('CAM_ROTATE', 45, 24, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 23000, 0),
	Insn('CAM_OFFSET', (7380, 1030, -11050), 5000),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (2250, 1030, -150), 0),
	Insn('CAM_ROTATE', 45, 24, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 18500, 0),
	Insn('0x0D'),
	Insn('EMOTE', Char(339), 0, 1700, (38, 39, 250, 2)),
	Insn('SLEEP', 500),
	Insn('CHAR_ROTATE', Char(339), 180, 500),
	Insn('SLEEP', 500),
	Insn('CHAR_ROTATE', Char(339), 90, 500),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(339), Text(
		'#1105F#5P哇，好厉害！\n'
		'好多书啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0002F那个……琪雅你\n'
		'喜欢书吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(339), 270, 500),
	Insn('TEXT_TALK', Char(339), Text(
		'#1110F#11P嗯，虽然不知道为什么，但很喜欢！{wait}'
		'{page}'
		'#1109F只要看到书排成一列，\n'
		'就觉得很兴奋！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#0109F#6P那么我们下次\n'
				'再来慢慢逛吧。{wait}'
				'{page}'
				'#0102F克洛斯贝尔的市立图书馆里\n'
				'应该有很多\n'
				'儿童读物。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#0204F#6P那么我们下次\n'
				'再来慢慢逛吧。{wait}'
				'{page}'
				'#0202F克洛斯贝尔的市立图书馆里\n'
				'应该有很多\n'
				'儿童读物。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#0309F#6P那么下次再\n'
				'带你来慢慢逛吧。{wait}'
				'{page}'
				'#0300F这里看上去好像有\n'
				'很多儿童读物。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (2500, 0, 0), 90),
	Insn('FLAG_SET', Flag(1464)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][55] = [
	Insn('EMOTE', Char(254), 0, 1700, (28, 33, 250, 0)),
	Insn('RETURN'),
]

data['code'][56] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 22))), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 23))), Insn('NOT'), Insn('END')]), [
					Insn('EVENT_BEGIN', 0),
					Insn('FADE_ON', 1000, Color(0x00000000), 255),
					Insn('0x0D'),
					Insn('CHAR_SET_POS', Char(257), (5000, 30, 8460), 90),
					Insn('CHAR_SET_POS', Char(258), (5000, 30, 7260), 90),
					Insn('CHAR_SET_POS', Char(259), (3800, 30, 8460), 90),
					Insn('CHAR_SET_POS', Char(260), (3800, 30, 7260), 90),
					Insn('CAM_OFFSET', (6490, 1000, 8670), 0),
					Insn('CAM_ROTATE', 50, 17, 0, 0),
					Insn('0x6E', 440, 0),
					Insn('CAM_DISTANCE', 17000, 0),
					Insn('CAM_DISTANCE', 15000, 1000),
					Insn('FADE_OFF', 1000, Color(0x00000000)),
					Insn('0x0D'),
					Insn('0x6F', b'y'),
					Insn('TEXT_TALK', Char(15), Text(
						'亚苏拉小姐吗？\n'
						'她现在就在这里哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'说是想查一些资料。{wait}'
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
						'#0000F我知道了。\n'
						'大叔，谢谢你！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_SET_POS', Char(0), (5000, 30, 7860), 90),
					Insn('EVENT_END', 5),
					Insn('QUEST', 56, Insn('TASK_SET', 23)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(15), Text(
						'亚苏拉小姐吗？\n'
						'她现在就在这里哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'说是想查一些资料。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, [
			Insn('TEXT_TALK', Char(15), Text(
				'亚苏拉小姐吗？\n'
				'嗯……今天没看到她呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'她应该不在这里吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]
