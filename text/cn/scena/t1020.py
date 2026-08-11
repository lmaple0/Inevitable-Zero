# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't1020',
	'name2': 't1020',
	'location': 149,
	'bgm': 111,
	'flags': 8192,
	'includes': [
		't1020',
		't1030_1',
		None,
		None,
		None,
		None,
	],
	'name3': 't1020',
	'labels': [],
	'chcp': [
		'chr/ch23600',
		'chr/ch26700',
		'chr/ch21600',
		'chr/ch21100',
		'chr/ch20700',
		'chr/ch33200',
		'chr/ch25900',
	],
	'npcs': [
		{
			'name': Translate('艾丽洁'),
			'pos': (-24909, 0, 5570),
			'angle': 90,
			'_1': b'\x01\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 5)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('青年'),
			'pos': (100139, 0, 18219),
			'angle': 0,
			'_1': b'\x81\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((0, 6)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (4190, 0, 13079),
			'angle': 0,
			'_1': b'\x01\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (97510, 0, 5429),
			'angle': 270,
			'_1': b'\x81\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('女性'),
			'pos': (-23930, 0, 11470),
			'angle': 0,
			'_1': b'\x81\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 10)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('女孩'),
			'pos': (-22840, 0, 10689),
			'angle': 315,
			'_1': b'\x91\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((0, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('店员'),
			'pos': (-18940, 0, 12609),
			'angle': 180,
			'_1': b'\x81\x01\x00\x00\x06\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('女孩'),
			'pos': (16440, 0, 10779),
			'angle': 180,
			'_1': b'\x81\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((0, 19)),
			'_2': b'\xff\x00\x00\x00',
		},
	],
	'monsters': [],
	'triggers': [
		{
			'pos': (26.5, 8.0, -1.0),
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
				-8.833333969116211,
				-0.800000011920929,
				0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 14)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (8.5, 8.0, -1.0),
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
				-2.8333334922790527,
				-0.800000011920929,
				0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (-11.0, 8.0, -1.0),
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
				3.6666667461395264,
				-0.800000011920929,
				0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (-19.030000686645508, 11.899999618530273, -1.0),
			'range': 2.4964001178741455,
			'transform': [
				0.5,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.6329113841056824,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				9.515000343322754,
				-7.53164529800415,
				0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (27660, 0, 10070),
			'range': 1200,
			'bubble_pos': (27660, 1500, 10070),
			'_1': b'|\x00\x00',
			'function': Function((0, 18)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (19000, 0, 11850),
			'range': 2000,
			'bubble_pos': (19000, 1000, 11850),
			'_1': b'|\x00\x00',
			'function': Function((0, 16)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x95\x00', Function((0, 3)), Function((0, 4))),
	'code': [None]*21,
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
		Insn('CHAR_IDLE', Char(254), (97550, 16140), (102740, 18340), 1000),
		Insn('SLEEP', 150),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (940, 10450), (4860, 14310), 1000),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 107), Insn('EQ'), Insn('FLAG', Flag(1313)), Insn('BOOL_AND'), Insn('FLAG', Flag(1314)), Insn('BOOL_AND'), Insn('FLAG', Flag(1315)), Insn('BOOL_AND'), Insn('FLAG', Flag(1316)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 15))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1333)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1330)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1329)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1320)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1319)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(8), (-13780, 0, 6020), 90),
			Insn('CHAR_SET_POS', Char(10), (-12240, 0, 6020), 270),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
			Insn('FORK_FUNC', Char(10), 0, Function((0, 2))),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 55, Insn('TASK_GET', 2))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(13), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('FORK_FUNC', Char(15), 0, Function((0, 20))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('0xB5', b'\x00\x02\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1312)), Insn('FLAG', Flag(1315)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x00\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1313)), Insn('FLAG', Flag(1314)), Insn('BOOL_AND'), Insn('FLAG', Flag(1315)), Insn('BOOL_AND'), Insn('FLAG', Flag(1316)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x01\x80\x00'),
			Insn('0xB5', b'\x01\x02\x80\x00'),
		]),
		(None, []),
	]),
	Insn('0x65', 1, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('FLAG', Flag(1319)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(3), 16),
			Insn('0x66', 1, 1),
		]),
		(None, []),
	]),
	Insn('OBJ_FLAG_UNSET', Object(2), 16),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1333)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1330)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1329)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1320)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1319)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 8))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……真是的，一点教养都没有的游客。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呼……真是的，\n'
				'这里无论何时都很混乱啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'想买个东西都那么辛苦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'唔啊啊啊啊！！！\n'
		'等一下啊，咪西────！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1333)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1330)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1329)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1320)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1319)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 8))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'怎么会这样……\n'
						'仅仅是有钱的话，\n'
						'是无法吸引这里的女孩子的……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'不愧是高级游憩区……\n'
				'有好多大小姐类型\n'
				'的女孩子啊！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'好……不如去\n'
				'尝试搭讪吧！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('0x4B', Char(8), -1),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_WATCH', Char(8), Char(10), 0),
	Insn('CHAR_WATCH', Char(10), Char(8), 0),
	Insn('TEXT_TALK', Char(10), Text(
		'嘿，小姐……\n'
		'不介意的话，一起去\n'
		'那边的餐厅吃个饭如何啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'放心，我带了\n'
		'足够的米拉哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'……不用了，\n'
		'我没有理由\n'
		'让你请客哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'而且，要论米拉数量的话，\n'
		'我带的也许\n'
		'比你还多呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#4S（打击！）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(8), -1),
	Insn('0x4C', Char(10), -1),
	Insn('FLAG_SET', Flag(0)),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'这里是餐厅《幸运》……\n'
				'嗯，果然是家\n'
				'豪华的餐厅啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……但重点是料理的味道！\n'
				'身为美食家的我，\n'
				'是不会被餐厅的装修迷惑的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'来吧，著名游憩区的\n'
				'餐厅的料理……\n'
				'就让我亲口品尝一下吧！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'这家珠宝店……\n'
		'不允许我这种\n'
		'普通的游客入内。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'啊！真不甘心！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'妈妈……\n'
		'不要看宝石了，\n'
		'我们去主题乐园玩吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('0xF2', Insn('CHARGING_STATION')),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_MESSAGE', Char(999), Text(
		'{color 5}设有可回复导力器的装置。{color 0}{wait}'
	)),
	Insn('MENU', 0, -1, -1, 1, Text(
		'在此地休息\n'
		'放弃\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('FADE_OFF', 100, Color(0x00000000)),
			Insn('SLEEP', 500),
			Insn('SOUND_LOAD', 13),
			Insn('0x74', Object(7), 7680),
			Insn('SOUND_PLAY', 7, 0, 0, 100),
			Insn('0x70', Object(7), b'\x00\x00'),
			Insn('0x71', Object(7), b'\x00\x00', 30, 0),
			Insn('0x79', b'\x07\x00'),
			Insn('0x71', Object(7), b'\x1f\x00', 390, 32),
			Insn('SLEEP', 1000),
			Insn('BGM_STOP', 3000),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('SLEEP', 700),
			Insn('SOUND_PLAY', 13, 0, 0, 100),
			Insn('0x0D'),
			Insn('0x32', Party(255), -2, 0),
			Insn('0x6A', b'\x00\x00\x00\x00\x00\x00'),
			Insn('0x31', b'\x01\x08\xac\r'),
			Insn('0x70', Object(7), b'\x00\x00'),
			Insn('0x1F'),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_END', Char(255)),
			Insn('RETURN'),
		]),
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), [
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('TEXT_END', Char(255)),
			Insn('RETURN'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1393)), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('CROSSFADE', 1000),
			Insn('CAM_OFFSET', (-19000, 1000, 11800), 0),
			Insn('CHAR_SET_POS', Char(257), (-19330, 0, 8810), 0),
			Insn('CHAR_SET_POS', Char(258), (-17960, 0, 8810), 0),
			Insn('CHAR_SET_POS', Char(259), (-20760, 0, 10150), 45),
			Insn('CHAR_SET_POS', Char(260), (-16940, 0, 9380), 315),
			Insn('IF', [
				(Expr([Insn('ATTR', 14), Insn('CONST', 80), Insn('EQ'), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(337), (-18610, 0, 7180), 0),
				]),
				(None, []),
			]),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_SET_POS', Char(14), (-19000, 0, 12900), 180),
			Insn('CHAR_SET_COLOR', Char(14), Color(0x00FFFFFF), 0),
			Insn('0x0D'),
			Insn('0x74', Object(2), 7680),
			Insn('0x71', Object(2), b'\x00\x00', 10, 0),
			Insn('SOUND_PLAY', 107, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('FORK', 14, 1, [
				Insn('0x96', Char(254), (-19000, 0, 11310), 2000, 0),
			]),
			Insn('CHAR_SET_COLOR', Char(14), Color(0xFFFFFFFF), 200),
			Insn('FORK_AWAIT', Char(14), 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F哇……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#11P欢迎来到\n'
				'珠宝店『亮饰』。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#11P……不好意思，这位客人。\n'
				'请问您持有\n'
				'哪位贵宾的介绍信？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0105F请问……\n'
				'必须要持有介绍信吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#11P正是。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#11P本店实行会员制，\n'
				'非会员谢绝入内。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#11P那么，很抱歉……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_ROTATE', Char(14), 0, 500),
			Insn('SLEEP', 100),
			Insn('FORK', 14, 1, [
				Insn('0x96', Char(254), (-19000, 0, 12900), 2000, 0),
			]),
			Insn('SLEEP', 300),
			Insn('CHAR_SET_COLOR', Char(14), Color(0x00FFFFFF), 300),
			Insn('FORK_AWAIT', Char(14), 1),
			Insn('0x71', Object(2), b'\n\x00', 0, 0),
			Insn('SOUND_PLAY', 107, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('CHAR_FLAG1_SET', Char(14), 128),
			Insn('EMOTE', Char(0), 0, 2000, (24, 27, 250, 0)),
			Insn('EMOTE', Char(1), 0, 2000, (24, 27, 250, 0)),
			Insn('EMOTE', Char(2), 0, 2000, (24, 27, 250, 0)),
			Insn('EMOTE', Char(3), 0, 2000, (24, 27, 250, 0)),
			Insn('SLEEP', 1000),
			Insn('EMOTE_STOP', Char(0)),
			Insn('EMOTE_STOP', Char(1)),
			Insn('EMOTE_STOP', Char(2)),
			Insn('EMOTE_STOP', Char(3)),
			Insn('TEXT_TALK', Char(259), Text(
				'#0211F……一眼就看出我们不是会员了吗。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0310F感、感觉真不爽啊……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('ATTR', 14), Insn('CONST', 80), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(337), Text(
						'#5704F这种地方的店，\n'
						'很多都是会员制的。{wait}'
						'{page}'
						'要是能佩戴一些高级饰品，\n'
						'正好就可以\n'
						'与礼服搭配了……{wait}'
						'{page}'
						'#5702F不过，没办法，这次就放弃吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F说、说的也对啊……\n'
						'总之，先去时装店看看吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F总、总之……\n'
						'进不去的话也没办法啊。\n'
						'这次就先放弃吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('0x5A'),
			Insn('FLAG_SET', Flag(1393)),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('EVENT_BEGIN', 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F这家珠宝店\n'
				'好像实行会员制，\n'
				'这次就先放弃吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x5A'),
			Insn('CHAR_SET_POS', Char(0), (-18610, 0, 9950), 180),
			Insn('EVENT_END', 4),
		]),
	]),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (27100, 1600, 7920), 0),
	Insn('CAM_ROTATE', 315, 15, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 17870, 0),
	Insn('CHAR_SET_POS', Char(257), (25000, 0, 7600), 90),
	Insn('CHAR_SET_POS', Char(258), (23800, 0, 8900), 90),
	Insn('CHAR_SET_POS', Char(259), (23800, 0, 7600), 90),
	Insn('CHAR_SET_POS', Char(260), (25000, 0, 8900), 90),
	Insn('CAM_OFFSET', (25100, 1600, 7920), 3000),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500417V#0001F#5P前方是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500418V#0105F#5P好像\n'
		'被封锁了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500419V#0305F#5P啊，好像写着什么。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (26500, 1600, 7920), 3000),
	Insn('FORK', 260, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xd0\x07\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xd0\x07\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 258, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xd0\x07\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xd0\x07\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 300),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'\x01'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}前方区域正在开发，\n'
		'禁止进入。\n'
		'──米修拉姆开发事业部{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500420V#0200F#6P……看来前方\n'
		'还在开发呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500421V#0103F#5P嗯，米修拉姆的开发计划\n'
		'好像还在进行当中……{wait}'
		'{page}'
		'#13500422V#0100F说不定，这边以后也会\n'
		'建造起一些设施呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500423V#0306F#5P哎呀呀，真是够奢侈……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500424V#0000F#6P总之，我们现在也不需要去那边，\n'
		'还是先去别的地方绕绕吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (25630, 0, 8109), 270),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('FLAG_SET', Flag(1315)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1313)), Insn('FLAG', Flag(1314)), Insn('BOOL_AND'), Insn('FLAG', Flag(1315)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x01\x80\x00'),
			Insn('0xB5', b'\x01\x02\x80\x00'),
		]),
		(None, []),
	]),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('CAM_OFFSET', (-50, 1100, 8000), 0),
	Insn('CAM_ROTATE', 335, 18, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 20090, 0),
	Insn('CAM_DISTANCE', 18590, 2000),
	Insn('CHAR_SET_POS', Char(257), (0, 0, 9300), 180),
	Insn('CHAR_SET_POS', Char(258), (0, 0, 6700), 0),
	Insn('CHAR_SET_POS', Char(259), (1200, 0, 8000), 270),
	Insn('CHAR_SET_POS', Char(260), (-1200, 0, 8000), 90),
	Insn('0x6F', b'\x10'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500425V#0003F#11P已经绕了一圈了……{wait}'
		'{page}'
		'#13500426V#0001F看样子，要想进入拍卖会场，\n'
		'果然还是需要想点办法。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500427V#0301F#5P是啊，毕竟盘查人员好像\n'
		'就是那些黑手党。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500428V#0205F#12P说起来，那张邀请卡\n'
		'可以就这样直接使用吗？{wait}'
		'{page}'
		'#13500429V#0201F应该很有可能\n'
		'会被核查身份……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500430V#0103F#6P……的确如此。{wait}'
		'{page}'
		'#13500431V#0108F这方面的事情，如果之前\n'
		'仔细向蕾恩咨询一下就好了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500432V#0000F#11P算了，\n'
		'光是把邀请卡让给我们这一点，\n'
		'就已经非常感激了。{wait}'
		'{page}'
		'#13500433V#0006F不管怎么说……要先找到一个\n'
		'安静的地方，好考虑对策啊。{wait}'
		'{page}'
		'#13500434V#0008F餐厅……\n'
		'那里的人未免也太多了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500435V#0200F#12P那么，上面的饭店\n'
		'没有空房间了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500436V#0106F#6P嗯，在这种时期，\n'
		'我想客房应该都被订满了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500437V#0300F#5P不过，说不定也会有\n'
		'客人取消预订而空出来的房间吧。{wait}'
		'{page}'
		'#13500438V去总服务台问问看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500439V#0000F#11P说得对，去问下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (400, 0, 7770), 0),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('0xB5', b'\x00\x02\x80\x00'),
	Insn('FLAG_SET', Flag(1316)),
	Insn('QUEST', 71, Insn('TASK_SET', 3)),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (19000, 1000, 10600), 0),
	Insn('CAM_ROTATE', 315, 18, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 20500, 0),
	Insn('CHAR_SET_POS', Char(257), (19000, 0, 10600), 0),
	Insn('CHAR_SET_POS', Char(258), (18350, 0, 9300), 0),
	Insn('CHAR_SET_POS', Char(259), (19650, 0, 9300), 0),
	Insn('CHAR_SET_POS', Char(260), (18350, 0, 8000), 0),
	Insn('CHAR_SET_POS', Char(337), (19650, 0, 8000), 0),
	Insn('CAM_DISTANCE', 19500, 2000),
	Insn('0x6F', b'y'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0003F#5P（……换上正装之后，\n'
		'\u3000就不能在周围打探情况了。）{wait}'
		'{page}'
		'#0001F（而且也需要决定带谁去会场才行，\n'
		'\u3000怎么办呢……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('MENU', 0, -1, -1, 0, Text(
		'【继续在周围打探情况】\n'
		'【去时装店换正装】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x0D'),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('CHAR_SET_POS', Char(0), (19000, 0, 9300), 180),
			Insn('EVENT_END', 5),
			Insn('BREAK'),
		],
		1: [
			Insn('OBJ_FLAG_UNSET', Object(3), 16),
			Insn('0x71', Object(3), b'\x00\x00', 30, 0),
			Insn('SOUND_PLAY', 107, 0, 0, 100),
			Insn('0x79', b'\x03\x00'),
			Insn('CAM_OFFSET', (19000, 1000, 11600), 5000),
			Insn('FORK_FUNC', Char(257), 3, Function((0, 17))),
			Insn('SLEEP', 300),
			Insn('FORK_FUNC', Char(258), 3, Function((0, 17))),
			Insn('SLEEP', 800),
			Insn('FORK_FUNC', Char(259), 3, Function((0, 17))),
			Insn('SLEEP', 300),
			Insn('FORK_FUNC', Char(260), 3, Function((0, 17))),
			Insn('SLEEP', 800),
			Insn('FORK_FUNC', Char(337), 3, Function((0, 17))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(258), 3),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('FORK_QUIT', Char(259), 3),
			Insn('FORK_QUIT', Char(260), 3),
			Insn('FORK_QUIT', Char(337), 3),
			Insn('NEW_SCENE', 't1040', b'd\x00\x00\x07'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('0x95', Char(254), (19000, 0, 10600), 2000, 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (19000, 0, 13000), 2000, 0),
	]),
	Insn('SLEEP', 400),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}前方区域正在开发，\n'
		'禁止进入。\n'
		'──米修拉姆开发事业部{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 55, Insn('TASK_GET', 3))), Insn('END')]), [
			Insn('CALL', Function((1, 8))),
		]),
		(None, [
			Insn('CALL', Function((1, 7))),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (10140, 11040), (17700, 5720), 3000),
		Insn('SLEEP', 150),
	]),
	Insn('RETURN'),
]
