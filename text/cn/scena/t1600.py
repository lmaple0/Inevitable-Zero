# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't1600',
	'name2': 't1600',
	'location': 77,
	'bgm': 123,
	'flags': 8192,
	'includes': [
		't1600',
		None,
		't1500_1',
		None,
		None,
		None,
	],
	'name3': 't1600',
	'labels': [
		{
			'pos': (-69.0, 0.0, -8.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('乌尔斯拉小径'),
		},
		{
			'pos': (-23.0, 0.0, 18.0),
			'unk': b'\x00\x00R\x00',
			'name': Translate(''),
		},
		{
			'pos': (-57.900001525878906, 0.0, 4.199999809265137),
			'unk': b'\x00\x00U\x00',
			'name': Translate(''),
		},
	],
	'chcp': [
		'chr/ch29600',
		'chr/ch29900',
		'chr/ch07100',
		'chr/ch29400',
		'chr/ch20200',
		'chr/ch29800',
		'chr/ch34200',
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
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
			'name': Translate('玛萨护理师长'),
			'pos': (-26559, 6000, 14199),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((0, 5)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('护理师希蓉'),
			'pos': (-26559, 6000, 14199),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 6)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('约亚西姆副教授'),
			'pos': (4039, 7000, 2160),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('实习医生利顿'),
			'pos': (4019, 7000, 3849),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 10)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('工友戴森'),
			'pos': (3430, 7000, -9159),
			'angle': 178,
			'_1': b'\x85\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((0, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('护理师梅菲尔'),
			'pos': (-25850, 6000, 14149),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 12)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客托迪'),
			'pos': (13619, 7000, 280),
			'angle': 135,
			'_1': b'\x81\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
	],
	'monsters': [],
	'triggers': [
		{
			'pos': (-4.5, 19.5, 6.0),
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
				1.5,
				-3.9000000953674316,
				-1.2000000476837158,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 20)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (15.0, -14.300000190734863, 6.0),
			'range': 729.0,
			'transform': [
				0.23570217192173004,
				0.03928372263908386,
				-0.0,
				0.0,
				-0.23570233583450317,
				0.039283692836761475,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.19999998807907104,
				0.0,
				-6.906075954437256,
				-0.02749902382493019,
				-1.1999999284744263,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 23)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (-13.5, 20.0, 5.5),
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
				6.75,
				-10.0,
				-1.100000023841858,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 24)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (-1.5, 23.5, 6.5),
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
				0.75,
				-11.75,
				-1.3000000715255737,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 25)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (-22.5, 23.5, 5.5),
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
				11.25,
				-11.75,
				-1.100000023841858,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 26)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (28100, 7000, -16700),
			'range': 2000,
			'bubble_pos': (28100, 8000, -16700),
			'_1': b'|\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (3300, 7000, 0),
			'range': 2000,
			'bubble_pos': (3300, 8000, 0),
			'_1': b'|\x00\x00',
			'function': Function((0, 16)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (22500, 7000, 13500),
			'range': 2000,
			'bubble_pos': (22500, 8000, 13500),
			'_1': b'|\x00\x00',
			'function': Function((0, 17)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-9300, 7000, 18100),
			'range': 2000,
			'bubble_pos': (-9300, 8000, 18100),
			'_1': b'|\x00\x00',
			'function': Function((0, 18)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-30000, 6000, 17000),
			'range': 2000,
			'bubble_pos': (-30000, 7000, 17000),
			'_1': b'|\x00\x00',
			'function': Function((0, 19)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (17500, 7000, -3000),
			'range': 2000,
			'bubble_pos': (18000, 8000, -3000),
			'_1': b'|\x00\x00',
			'function': Function((0, 14)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00M\x00', Function((0, 3)), Function((0, 4))),
	'code': [None]*28,
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
		Insn('CHAR_IDLE', Char(254), (-2910, 18910), (-680, 20850), 1000),
		Insn('SLEEP', 500),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (8180, -5330), (12010, -380), 1000),
		Insn('SLEEP', 500),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(9), (-27540, 6000, 14130), 90),
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(9), (-1790, 7000, 19910), 180),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(9), (-27200, 6000, 20220), 0),
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 22, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(10), (4040, 7000, 2160), 0),
					Insn('CHAR_FLAG1_UNSET', Char(10), 128),
					Insn('CHAR_FLAG1_UNSET', Char(11), 128),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 22, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(11), (10930, 7000, -2350), 180),
					Insn('FORK_FUNC', Char(11), 0, Function((0, 2))),
					Insn('CHAR_FLAG1_UNSET', Char(11), 128),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1280)), Insn('FLAG', Flag(1346)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(784)), Insn('FLAG', Flag(785)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x00\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(786)), Insn('FLAG', Flag(787)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x01\x80\x00'),
		]),
		(None, []),
	]),
	Insn('0x65', 0, 1),
	Insn('0x65', 1, 1),
	Insn('0x65', 2, 1),
	Insn('0x65', 3, 1),
	Insn('0x65', 4, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(787)), Insn('FLAG', Flag(793)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x66', 0, 1),
			Insn('0x66', 1, 1),
			Insn('0x66', 2, 1),
			Insn('0x66', 3, 1),
			Insn('0x66', 4, 1),
		]),
		(None, []),
	]),
	Insn('OBJ_FLAG_UNSET', Object(5), 16),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(799)), Insn('FLAG', Flag(800)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
			Insn('0x11', b'\xfd\xd5\xc6', 25, 200, 0),
		]),
		(Expr([Insn('FLAG', Flag(1359)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
			Insn('0x11', b'\xfd\xd5\xc6', 25, 200, 0),
		]),
		(Expr([Insn('FLAG', Flag(1564)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
			Insn('0x11', b'\xfd\xd5\xc6', 25, 200, 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(255), 'model6', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'model5', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'CA02', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'CA02', Insn('1', 2)),
		]),
		(None, [
			Insn('OBJ_SET_FRAME', Object(255), 'model6', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'model5', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'CA02', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 'CA02', Insn('0', 2)),
		]),
	]),
	Insn('0xB5', b'\x00\x02\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(777)), Insn('FLAG', Flag(784)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x02\x80\x00'),
		]),
		(None, []),
	]),
	Insn('0xB5', b'\x00\x03\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(787)), Insn('FLAG', Flag(793)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x03\x80\x00'),
		]),
		(None, []),
	]),
	Insn('0xB5', b'\x00\x04\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(787)), Insn('FLAG', Flag(792)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x04\x80\x00'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 0, 0),
			Insn('EMOTE', Char(254), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('CHAR_WATCH', Char(254), Char(0), 500),
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀……\n'
				'你们是在找人吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F嗯，我们想找\n'
				'在医院工作的朋友，\n'
				'正打算去接待处……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀，\n'
				'那你们还真是\n'
				'走错地方了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'接待处在病房大楼一楼的大厅哦。\n'
				'好啦，回去回去。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F啊，是这样吗……\n'
				'谢谢您。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(0)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'接待处在病房大楼一楼的大厅啦。\n'
				'好啦，回去回去。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 7))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'梅菲尔虽然有\n'
						'诸多抱怨，但还是会\n'
						'帮我补救失误呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，有个这么善良的朋友真是太好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我把床单的订货单写错了，\n'
						'梅菲尔又发火了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我只是觉得五十张太少了，\n'
						'所以就加了个零而已啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过，算啦。\n'
						'不能总是为\n'
						'失败而烦恼。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'没什么，没什么，我不介意！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'虽然又被梅菲尔\n'
						'骂了……\n'
						'不过我并不介意。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不能总是为失败而烦恼。\n'
						'没什么，没什么，我不介意！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('RECIPE', 11)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 8))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'梅菲尔真是的，\n'
						'又训斥我了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我只是把收到的货物好好保管起来而已……\n'
						'为什么一定要被骂呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'嗯～我被跑过去的\n'
						'小孩子撞到了，晕呼呼的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F对、对不起，\n'
						'那应该是我们监护的孩子。{wait}'
						'{page}'
						'#0005F那个，你没事吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'没、没事哦，\n'
						'只是头有点晕而已。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'不行，可能还要\n'
						'再晕一会……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'啊，刚才的女孩子\n'
						'跑进医院里面去了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我的同事梅菲尔\n'
						'虽然是护理师，却是个急性子。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我总是被她骂……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'今天她说要去\n'
						'盖巴尔先生的病房，\n'
						'没问题吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我的同事梅菲尔\n'
						'虽然是护理师，却是个急性子。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'盖巴尔先生\n'
						'很任性呢，\n'
						'她能忍得下来吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵～天气真好，\n'
						'床单似乎也能很快晾干。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……啊，对了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'把之前不小心弄脏的\n'
						'梅菲尔的衣服\n'
						'也一起晾了吧～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'之前我把药架上的奇怪药品\n'
						'撒到梅菲尔的便服上了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'反正天气不错，\n'
						'偷偷一起晾了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'昨天和赛西儿前辈她们\n'
				'换班去休假了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'和梅菲尔一起逛街\n'
				'好开心哦㈱{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，好漂亮的晚霞。\n'
						'感觉好凉爽。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……哈啾！！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……啊～鼻涕沾到床单上了！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'讨厌，怎么办呀～！\n'
						'又要被梅菲尔骂了～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'怎、怎么办呀～！\n'
						'又要被梅菲尔骂了～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'拜托戴森先生的话，\n'
						'他会不会私下帮我洗了呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('CHAR_WATCH', Char(9), Char(13), 0),
	Insn('CHAR_WATCH', Char(13), Char(9), 0),
	Insn('0x4B', Char(9), -1),
	Insn('0x4B', Char(13), -1),
	Insn('TEXT_TALK', Char(13), Text(
		'希蓉，你这个人啊……\n'
		'只是晾个床单而已，\n'
		'要花多长时间啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'啊，梅菲尔。\n'
		'你再等等，好像只差一点\n'
		'就可以调整到理想的晾晒角度了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'理、理想的角度……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'在你追求这种东西的时候，\n'
		'本该由你做的工作\n'
		'全都转给我了啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'啊，你帮我做完了工作吗？\n'
		'哇，谢谢～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'……唉……算了，\n'
		'我已经连生气的力气都没有了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(9), -1),
	Insn('0x4C', Char(13), -1),
	Insn('FLAG_SET', Flag(1)),
	Insn('FLAG_SET', Flag(3)),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('TEXT_TALK', Char(254), Text(
		'我又被骂了。\n'
		'唉～梅菲尔\n'
		'就是爱生气。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'一定是因为总是不能\n'
		'按时吃午饭，\n'
		'所以才那么暴躁呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'我试着做了一下之前在纪念庆典\n'
		'的露天摊贩看到的汉堡，\n'
		'还挺简单的，要不要教给她呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'啊，有兴趣的话，\n'
		'不妨也教给你们吧。\n'
		'真的很简单的！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'学习了{item 431}{color 0}的做法。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'记住了{item 431}{color 0}的食谱。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('RECIPE', 11),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'#2401F关于琪雅的病症，\n'
						'我查了不少资料……{wait}'
						'{page}'
						'#2406F但还是没有发现相符的病例呢，\n'
						'也有可能是新的症状……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F是吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'#2400F算了，反正现在\n'
						'好像也没有重大异常……\n'
						'暂时先观察一下情况吧。{wait}'
						'{page}'
						'#2406F我还没那么Ｓ，\n'
						'不会把她强行关在\n'
						'医院里检查的。{wait}'
						'{page}'
						'#2409F硬要说的话，当然是Ｍ……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0211F……………………{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0106F您、您在说什么呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0306F唉，真是个让人捉摸不透的人啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'#2400F总之，琪雅的情况并不严重，\n'
						'也不是必须要立刻采取什么治疗对策，\n'
						'耐心观察一阵子就好啦。{wait}'
						'{page}'
						'#2409F……对了，你们听我说哦。\n'
						'我为了转换心情，早上出去钓鱼，\n'
						'结果钓到了相当大的鱼呢。{wait}'
						'{page}'
						'哈哈，钓公师团的\n'
						'塞尔当分部长那惊讶的表情，\n'
						'我直到现在还记忆犹新呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F还真是我行我素啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'#2406F本以为今天终于成功在\n'
						'不被发现的情况下顺利溜走了呢。{wait}'
						'{page}'
						'要不是你们来得那么快，\n'
						'我就可以尽情享受纪念庆典了……{wait}'
						'{page}'
						'#2400F算啦，反正参加了\n'
						'期待已久的钓鱼大赛。\n'
						'这样就足够了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'#2406F本以为今天终于成功在\n'
						'不被发现的情况下顺利溜走了呢。{wait}'
						'{page}'
						'#2400F算啦，反正参加了\n'
						'期待已久的钓鱼大赛。\n'
						'这样就足够了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'#2404F嗯，反正还有时间，\n'
						'不如去钓鱼……{wait}'
						'{page}'
						'#2405F……但要是被一楼的\n'
						'拉格教授发现，\n'
						'一定会被大骂一通的吧。{wait}'
						'{page}'
						'#2406F唉，没办法。\n'
						'今天还是放弃吧，\n'
						'就窝在医院里好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0012F（越来越觉得这位医生很奇怪了……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(10), Text(
						'#2403F钓鱼可是很不错的哦，\n'
						'还可以转换心情。{wait}'
						'{page}'
						'#2400F有时间的话，\n'
						'一定要去探访克洛斯贝尔的各大钓场……\n'
						'真想赶快行动呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 22, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呼……\n'
				'能找到约亚西姆医生\n'
				'真是太好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'约亚西姆医生的话，\n'
				'很快就能把工作做完了，\n'
				'所以请不要推给我啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 22, Insn('FLAG_GET', 2))), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啊啊～真是的！约亚西姆医生\n'
				'到底去哪里了啊！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'这种工作量，我这个实习医生\n'
				'根本不可能完成啊！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'约亚西姆医生他们刚才回来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'好像有人受了重伤要被\n'
				'抬进来，忙得不可开交呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'话说……\n'
				'有个女孩子以超快的速度\n'
				'跑过去了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'你们看起来\n'
				'不像是生病了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'莫非是来研究区有事吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'上级领导们好像出去\n'
				'开什么教授会议了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'当领导也要操心劳神，\n'
				'真是辛苦啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我只要当个轻松的工友就很满足了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'医生和护理师们\n'
				'都对工作尽心尽力。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我也不能偷懒啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'听说绿色有\n'
				'安抚人心的效果。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'为了让病人们\n'
				'多少能安心一点，\n'
				'医院里摆放了很多盆植物。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'之前在宿舍天台上设置的\n'
				'防魔兽护栏……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'保险起见，就一直\n'
				'留在那里了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'因为要是再有魔兽侵入\n'
				'伤人的话，那不就糟糕了嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((0, 7))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'我是不是……\n'
				'太娇纵希蓉了呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'无论是什么事情，我都\n'
				'替她完成，这可不行啊……{wait}'
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
		(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'屋顶上竟然这么宽敞，\n'
				'甚至还建了建筑物，\n'
				'真叫人大吃一惊呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'要是能爬到这栋建筑物的顶部，\n'
				'大概连克洛斯贝尔市都能望得到吧～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(7)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'要是能爬到这栋建筑物的顶部，\n'
				'视野一定非常好吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'但擅自进去的话会被骂吧～？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1352)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_TALK', Char(257), Text(
				'#0006F（结果琪雅\n'
				'\u3000并不在研究区里啊……）{wait}'
				'{page}'
				'#0008F（到底去哪里了呢？）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_END', Char(255)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_START', Char(255)),
			Insn('CALL', Function((2, 11))),
			Insn('TEXT_END', Char(255)),
		]),
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(793)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_START', Char(255)),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F这里是研究区吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0101F怎么办？\n'
						'要去探听一下吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F不……\n'
						'现在最重要的是现场取证吧。{wait}'
						'{page}'
						'#0001F以屋顶为中心，\n'
						'仔细调查一遍吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F现在还是在屋顶进行现场取证吧，\n'
						'要找到有关魔兽的线索才行。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('TEXT_END', Char(255)),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('EXPR_VAR', 2, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('MENU_CUSTOM', Insn('INIT', ResId(0))),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1554)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('OR'), Insn('END')]), [
					Insn('MENU_CUSTOM', Insn('ADD', ResId(0), Translate('【４Ｆ 药物学丄神经科研究室】'))),
					Insn('EXPR_VAR', 2, Expr([Insn('VAR', 2), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 8))), Insn('EXEC', Insn('QUEST_GET', 40, Insn('TASK_GET', 10))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
					Insn('MENU_CUSTOM', Insn('ADD', ResId(0), Translate('【１Ｆ 资料室】'))),
					Insn('EXPR_VAR', 2, Expr([Insn('VAR', 2), Insn('CONST', 2), Insn('ADD'), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('VAR', 2), Insn('CONST', 0), Insn('NE'), Insn('END')]), [
					Insn('EVENT_BEGIN', 2),
					Insn('FADE_ON', 300, Color(0x00000000), 100),
					Insn('0x0D'),
					Insn('MENU_CUSTOM', Insn('ADD', ResId(0), Translate('放弃'))),
					Insn('TEXT_SET_POS', -1, 20, -1, -1),
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'{color 5}{0x06}{0x18}#1K要去哪里？{color 0}{wait}'
					)),
					Insn('MENU_CUSTOM', Insn('FINISH', ResId(0), -1, 0)),
					Insn('MENU_WAIT', 0),
					Insn('0x60', 0),
					Insn('TEXT_RESET', b'\x00'),
					Insn('TEXT_SET_POS', -1, 280, 60, 3),
					Insn('0xDB'),
					Insn('FADE_OFF', 300, Color(0x00000000)),
					Insn('0x0D'),
					Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
						0: [
							Insn('IF', [
								(Expr([Insn('VAR', 2), Insn('CONST', 1), Insn('EQ'), Insn('VAR', 2), Insn('CONST', 3), Insn('EQ'), Insn('OR'), Insn('END')]), [
									Insn('EXPR_VAR', 2, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
								]),
								(Expr([Insn('VAR', 2), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
									Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
								]),
								(None, []),
							]),
							Insn('BREAK'),
						],
						1: [
							Insn('IF', [
								(Expr([Insn('VAR', 2), Insn('CONST', 1), Insn('EQ'), Insn('VAR', 2), Insn('CONST', 2), Insn('EQ'), Insn('OR'), Insn('END')]), [
									Insn('EXPR_VAR', 2, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
								]),
								(Expr([Insn('VAR', 2), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
									Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
								]),
								(None, []),
							]),
							Insn('BREAK'),
						],
						2: [
							Insn('EXPR_VAR', 2, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
							Insn('BREAK'),
						],
						None: [],
					}),
					Insn('SWITCH', [Insn('VAR', 2), Insn('END')], {
						0: [
							Insn('IF', [
								(Expr([Insn('FLAG', Flag(1554)), Insn('FLAG', Flag(1563)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
									Insn('TEXT_TALK', Char(257), Text(
										'#0005F哦……也不知道\n'
										'约亚西姆医生在不在，\n'
										'还是先到接待处确认一下吧。{wait}'
										'{page}'
										'#0003F这里也不是外部人员\n'
										'可以随便进去的地方。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('EVENT_END', 5),
								]),
								(None, [
									Insn('FADE_ON', 1000, Color(0x00000000), 255),
									Insn('0x71', Object(5), b'\x00\x00', 5, 0),
									Insn('SOUND_PLAY', 107, 0, 0, 100),
									Insn('0x79', b'\x05\x00'),
									Insn('0x0D'),
									Insn('IF', [
										(Expr([Insn('FLAG', Flag(1349)), Insn('FLAG', Flag(1350)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
											Insn('FLAG_SET', Flag(736)),
											Insn('NEW_SCENE', 't1650', b'e\x00\x00\x07'),
										]),
										(Expr([Insn('FLAG', Flag(1563)), Insn('FLAG', Flag(1564)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
											Insn('FLAG_SET', Flag(737)),
											Insn('NEW_SCENE', 't1650', b'e\x00\x00\x07'),
										]),
										(None, [
											Insn('EVENT_END', 5),
											Insn('NEW_SCENE', 't1650', b'e\x00\x00\x07'),
										]),
									]),
								]),
							]),
							Insn('BREAK'),
						],
						1: [
							Insn('FADE_ON', 1000, Color(0x00000000), 255),
							Insn('0x71', Object(5), b'\x00\x00', 5, 0),
							Insn('SOUND_PLAY', 107, 0, 0, 100),
							Insn('0x79', b'\x05\x00'),
							Insn('0x0D'),
							Insn('EVENT_END', 5),
							Insn('NEW_SCENE', 't1620', b'r\x00\x00\x07'),
							Insn('BREAK'),
						],
						2: [
							Insn('EVENT_END', 3),
							Insn('BREAK'),
						],
						None: [],
					}),
				]),
				(None, [
					Insn('TEXT_START', Char(255)),
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'{color 5}这里是乌尔斯拉医院的研究区。\n'
						'现在没有什么要事。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('0x5A'),
					Insn('TEXT_END', Char(255)),
				]),
			]),
		]),
		(None, [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}这里是乌尔斯拉医院的研究区。\n'
				'现在没有什么要事。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_END', Char(255)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(788)), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('CROSSFADE', 1000),
			Insn('CAM_OFFSET', (22460, 8000, -25140), 0),
			Insn('CAM_ROTATE', 53, 26, 0, 0),
			Insn('0x6E', 500, 0),
			Insn('CAM_DISTANCE', 25970, 0),
			Insn('CHAR_SET_POS', Char(257), (26480, 7000, -16960), 180),
			Insn('CHAR_SET_POS', Char(258), (27690, 7000, -14290), 180),
			Insn('CHAR_SET_POS', Char(259), (26160, 7000, -15280), 180),
			Insn('CHAR_SET_POS', Char(260), (28420, 7000, -15270), 180),
			Insn('0x0D'),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(260), Text(
				'#11101305V#3P#0306F再怎么说，也不可能\n'
				'是从这里进来的吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#11101306V#0001F嗯……下面是水面呢。{wait}'
				'{page}'
				'#11101307V狼型魔兽根本就\n'
				'爬不上来吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x5A'),
			Insn('CHAR_SET_POS', Char(0), (26380, 6900, -16960), 0),
			Insn('CAM_OFFSET', (26480, 8000, -16960), 0),
			Insn('CAM_ROTATE', 45, 26, 0, 0),
			Insn('0x6E', 500, 0),
			Insn('CAM_DISTANCE', 23000, 0),
			Insn('FLAG_SET', Flag(788)),
			Insn('QUEST', 63, Insn('TASK_SET', 11)),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}此处栏杆距离地面相当高，\n'
				'而且底下还有广阔的水面。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_END', Char(255)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(789)), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('CROSSFADE', 1000),
			Insn('CAM_OFFSET', (-2220, 8000, -4870), 0),
			Insn('CAM_ROTATE', 41, 21, 0, 0),
			Insn('0x6E', 500, 0),
			Insn('CAM_DISTANCE', 16280, 0),
			Insn('CHAR_SET_POS', Char(257), (3970, 7000, 110), 270),
			Insn('CHAR_SET_POS', Char(258), (5190, 7000, -250), 270),
			Insn('CHAR_SET_POS', Char(259), (4160, 7000, 1920), 270),
			Insn('CHAR_SET_POS', Char(260), (5500, 7000, 1650), 270),
			Insn('0x0D'),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(259), Text(
				'#11101308V#0200F#6P高度相当高……\n'
				'但中途有一段屋檐呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#11101309V#0006F#4P嗯～原来如此，\n'
				'一层的高度被分为两段吗……{wait}'
				'{page}'
				'#11101310V#0001F但魔兽要进来的话，\n'
				'应该还是很困难吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x5A'),
			Insn('CHAR_SET_POS', Char(0), (3970, 7000, 110), 90),
			Insn('FLAG_SET', Flag(789)),
			Insn('QUEST', 63, Insn('TASK_SET', 12)),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}可以看到正门部分的屋檐，\n'
				'距离地面似乎有一定的高度。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_END', Char(255)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(790)), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('CROSSFADE', 1000),
			Insn('CAM_OFFSET', (23090, 8000, 14140), 0),
			Insn('CAM_ROTATE', 45, 41, 0, 0),
			Insn('0x6E', 500, 0),
			Insn('CAM_DISTANCE', 25000, 0),
			Insn('CHAR_SET_POS', Char(257), (21870, 7000, 12850), 45),
			Insn('CHAR_SET_POS', Char(258), (21970, 7000, 11830), 45),
			Insn('CHAR_SET_POS', Char(259), (20710, 7000, 11420), 45),
			Insn('CHAR_SET_POS', Char(260), (20470, 7000, 13080), 45),
			Insn('0x0D'),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(258), Text(
				'#11101311V#0101F#12P#N嗯，会不会\n'
				'是从这里进来的？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x5A'),
			Insn('TEXT_TALK', Char(257), Text(
				'#11101312V#0003F#6P嗯～魔兽的确很有可能\n'
				'从这种地形侵入……{wait}'
				'{page}'
				'#11101313V#0001F可是，这种高度\n'
				'仍然是个问题啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x5A'),
			Insn('CHAR_SET_POS', Char(0), (21200, 7000, 12090), 225),
			Insn('FLAG_SET', Flag(790)),
			Insn('QUEST', 63, Insn('TASK_SET', 13)),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}是一片很有可能\n'
				'会出现魔兽的地形。{wait}'
				'{page}'
				'但似乎有一定的高度。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_END', Char(255)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(791)), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('CROSSFADE', 1000),
			Insn('CAM_OFFSET', (-8530, 8000, 17450), 0),
			Insn('CAM_ROTATE', 45, 33, 0, 0),
			Insn('0x6E', 500, 0),
			Insn('CAM_DISTANCE', 24400, 0),
			Insn('CHAR_SET_POS', Char(257), (-8770, 7000, 18960), 180),
			Insn('CHAR_SET_POS', Char(258), (-10030, 7000, 19500), 180),
			Insn('CHAR_SET_POS', Char(259), (-6950, 7000, 19010), 180),
			Insn('CHAR_SET_POS', Char(260), (-7950, 7000, 20200), 180),
			Insn('0x0D'),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(257), Text(
				'#11101314V#0006F#5P再怎么说，也不会是从\n'
				'这里侵入的吧。{wait}'
				'{page}'
				'#11101315V#0001F如果是会飞行的魔兽，\n'
				'倒还能理解……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x5A'),
			Insn('CHAR_SET_POS', Char(0), (-8770, 7000, 18960), 270),
			Insn('FLAG_SET', Flag(791)),
			Insn('QUEST', 63, Insn('TASK_SET', 14)),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}空中走廊距离地面\n'
				'似乎有相当的高度。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_END', Char(255)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(792)), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('CROSSFADE', 1000),
			Insn('CAM_OFFSET', (-30100, 7000, 16720), 0),
			Insn('CAM_ROTATE', 37, 43, 0, 0),
			Insn('0x6E', 500, 0),
			Insn('CAM_DISTANCE', 22550, 0),
			Insn('CHAR_SET_POS', Char(257), (-29060, 6000, 17010), 270),
			Insn('CHAR_SET_POS', Char(258), (-28050, 6000, 16180), 270),
			Insn('CHAR_SET_POS', Char(259), (-28460, 6000, 14890), 270),
			Insn('CHAR_SET_POS', Char(260), (-28620, 6000, 19420), 270),
			Insn('0x0D'),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(257), Text(
				'#11101316V#0005F#11P这里是……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#11101317V#0100F#11P嗯，从这里的话，\n'
				'似乎进得来吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#11101318V#0000F#11P的确，这种高度\n'
				'也不是跳不上来呢。{wait}'
				'{page}'
				'#11101319V#0008F这样的话……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x5A'),
			Insn('CHAR_SET_POS', Char(0), (-28960, 5900, 17010), 0),
			Insn('FLAG_SET', Flag(792)),
			Insn('QUEST', 63, Insn('TASK_SET', 15)),
			Insn('0xB5', b'\x00\x04\x80\x00'),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}栏杆的正下方\n'
				'堆放着木箱和集装箱。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_END', Char(255)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-4500, 8000, 19000), 0),
	Insn('CAM_ROTATE', 45, 20, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 25250, 0),
	Insn('CHAR_SET_POS', Char(257), (-3800, 7000, 18900), 90),
	Insn('CHAR_SET_POS', Char(258), (-3800, 7000, 20100), 90),
	Insn('CHAR_SET_POS', Char(259), (-4900, 7000, 18900), 90),
	Insn('CHAR_SET_POS', Char(260), (-4900, 7000, 20100), 90),
	Insn('CHAR_SET_POS', Char(310), (-1600, 7000, 19500), 270),
	Insn('CAM_OFFSET', (-3000, 8000, 19000), 2500),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('CHAR_ROTATE', Char(257), 180, 300),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(257), 90, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101177V#0001F#6P莫非……\n'
		'这里就是受害者被袭击的地方？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101178V#1303F#11P嗯……\n'
		'是院区的屋顶。{wait}'
		'{page}'
		'#11101179V#1300F怎么办？\n'
		'先调查这里吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101180V#0000F#6P不……在此之前，\n'
		'还是想先听听受害者怎么说。{wait}'
		'{page}'
		'#11101181V稍后再带我们来好吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101182V#1300F#11P明白了。{wait}'
		'{page}'
		'#11101183V遇袭的实习医生\n'
		'在二楼的病房里，我带你们去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101184V#0000F#6P嗯，拜托了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(310), 0, 500),
	Insn('FORK_FUNC', Char(310), 3, Function((0, 21))),
	Insn('SLEEP', 1300),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 22))),
	Insn('SLEEP', 1200),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 22))),
	Insn('SLEEP', 700),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 22))),
	Insn('SLEEP', 1200),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 22))),
	Insn('FORK_AWAIT', Char(310), 3),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x71', Object(4), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 106, 0, 0, 100),
	Insn('0x79', b'\x04\x00'),
	Insn('OBJ_FLAG_SET', Object(4), 16),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FLAG_SET', Flag(815)),
	Insn('FLAG_SET', Flag(737)),
	Insn('NEW_SCENE', 't1540', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-1680, 7000, 22860), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('OBJ_FLAG_UNSET', Object(4), 16),
	Insn('0x71', Object(4), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 105, 0, 0, 100),
	Insn('0x79', b'\x04\x00'),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-1550, 7000, 25460), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-1680, 7000, 22860), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-1550, 7000, 25460), 2000, 0),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (15000, 8000, -13430), 0),
	Insn('CAM_ROTATE', 45, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 24500, 0),
	Insn('CAM_OFFSET', (15000, 8000, -15500), 3000),
	Insn('CHAR_SET_POS', Char(257), (15700, 7000, -14680), 180),
	Insn('CHAR_SET_POS', Char(258), (14280, 7000, -14560), 180),
	Insn('CHAR_SET_POS', Char(259), (14260, 7000, -13000), 180),
	Insn('CHAR_SET_POS', Char(260), (15640, 7000, -13120), 180),
	Insn('CHAR_SET_POS', Char(310), (15040, 7000, -16780), 0),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101283V#0005F#5P从听到的情况看来……\n'
		'这一带就是现场吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 310, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101284V#1301F#5P嗯嗯，利顿医生\n'
		'就是在那条长椅附近\n'
		'晕倒的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101285V#0001F#5P是吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('SLEEP', 500),
	Insn('FORK', 310, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('SLEEP', 400),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CAM_ROTATE', 45, 13, 0, 2000),
	Insn('CAM_OFFSET', (15000, 8500, -15500), 2000),
	Insn('0x6F', b'Q'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101286V#6P#0005F这栋建筑物……\n'
		'好像是『研究区』吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 310, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101287V#12P#1300F嗯，医生和实习医生们\n'
		'都在里面工作。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101288V#0200F#6P有没有为了做实验\n'
		'而饲养什么危险的魔兽……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101289V#12P#1304F呵呵，才不会啦。{wait}'
		'{page}'
		'#11101290V#1300F不过倒是有用来培育研究用的植物，\n'
		'类似温室一样的地方……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101291V#6P#0100F原来如此……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('CAM_OFFSET', (15000, 8000, -15500), 1200),
	Insn('CAM_ROTATE', 45, 18, 0, 1200),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 400),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 310, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 400),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 400),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 400),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 400),
	]),
	Insn('0x6F', b'Q'),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101292V#0004F#5P赛西儿姐姐，谢谢你给我们带路。{wait}'
		'{page}'
		'#11101293V#0000F总之，我们先调查一遍，\n'
		'看能不能发现什么吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(310), Text(
		'#11101294V#1300F#12P嗯，好的。{wait}'
		'{page}'
		'#11101295V#1309F那么，各位，\n'
		'要加油调查哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101296V#0102F#5P好的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101297V#0202F#5P……辛苦了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101298V#0309F#5P敬请期待\n'
		'我们的好消息吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_LOOP', 257, 1, [
		Insn('CHAR_WATCH', Char(257), Char(310), 500),
	]),
	Insn('FORK_LOOP', 258, 1, [
		Insn('CHAR_WATCH', Char(258), Char(310), 500),
	]),
	Insn('FORK_LOOP', 259, 1, [
		Insn('CHAR_WATCH', Char(259), Char(310), 500),
	]),
	Insn('FORK_LOOP', 260, 1, [
		Insn('CHAR_WATCH', Char(260), Char(310), 500),
	]),
	Insn('CHAR_ROTATE', Char(310), 315, 500),
	Insn('CAM_OFFSET', (13760, 8000, -12780), 3000),
	Insn('FORK', 310, 1, [
		Insn('0x95', Char(254), (11170, 7000, -14900), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('FORK', 310, 1, [
		Insn('0x95', Char(254), (10070, 7000, -2850), 2500, 0),
	]),
	Insn('SLEEP', 3000),
	Insn('BGM_STOP', 3000),
	Insn('FORK_AWAIT', Char(310), 1),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(259), 1),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('CAM_OFFSET', (15390, 8000, -13910), 1500),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 315, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 135, 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 300),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('SLEEP', 1000),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'o\x00\x00'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 111), Insn('SET'), Insn('END')])),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101299V#11P#0003F总之，先以屋顶为中心，\n'
		'全部调查一遍吧。{wait}'
		'{page}'
		'#11101300V#0001F狼型魔兽\n'
		'确实出现在了屋顶上──{wait}'
		'{page}'
		'#11101301V以此为前提，要想办法\n'
		'找出侵入地点。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101302V#6P#0100F嗯，明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101303V#0202F#1P是要用罗伊德前辈擅长的\n'
		'排除法吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101304V#5P#0300F那么，就调查看看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('0x2F', b'5\x00'),
	Insn('CHAR_SET_POS', Char(0), (15500, 7000, -13700), 180),
	Insn('0xB5', b'\x00\x01\x80\x00'),
	Insn('0x66', 0, 1),
	Insn('0x66', 1, 1),
	Insn('0x66', 2, 1),
	Insn('0x66', 3, 1),
	Insn('0x66', 4, 1),
	Insn('FLAG_SET', Flag(787)),
	Insn('0xB5', b'\x01\x03\x80\x00'),
	Insn('0xB5', b'\x01\x04\x80\x00'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('EVENT_BEGIN', 1),
	Insn('0x4B', Char(8), -1),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-20770, 7000, 15490), 0),
	Insn('CAM_ROTATE', 45, 27, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('0x0D'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
			Insn('EMOTE', Char(8), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('CHAR_WATCH', Char(8), Char(0), 500),
			Insn('TEXT_TALK', Char(8), Text(
				'……哎呀，你们\n'
				'迷路了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'这里可不是外部人员可以进来的地方哦。\n'
				'先去医院接待处\n'
				'通告一声再来吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 0, 1, [
				Insn('CHAR_WATCH', Char(254), Char(8), 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 1, 1, [
				Insn('CHAR_WATCH', Char(254), Char(8), 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 2, 1, [
				Insn('CHAR_WATCH', Char(254), Char(8), 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 3, 1, [
				Insn('CHAR_WATCH', Char(254), Char(8), 500),
			]),
			Insn('FORK_AWAIT', Char(0), 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F哦……对不起。{wait}'
				'{page}'
				'#0006F（在医院里闲逛之前，\n'
				'\u3000果然还是应该先去和赛西儿姐姐\n'
				'\u3000见个面为好啊……）{wait}'
				'{page}'
				'（接待处应该在\n'
				'\u3000院区一楼的大厅，\n'
				'\u3000在那里让人帮忙传一下话吧。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(4)),
		]),
		(None, [
			Insn('CHAR_WATCH', Char(8), Char(0), 500),
			Insn('TEXT_TALK', Char(8), Text(
				'这里可不是外部人员可以进入的地方哦。\n'
				'先去医院接待处通告一声再来吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'接待处就在院区一楼的大厅。\n'
				'喏，快去那边吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('SLEEP', 50),
	Insn('0x4C', Char(8), -1),
	Insn('CHAR_ROTATE', Char(8), 0, 0),
	Insn('CHAR_SET_POS', Char(0), (-16660, 6000, 19210), 270),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('EVENT_BEGIN', 1),
	Insn('CALL', Function((0, 27))),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (-1500, 6500, 21500), 180),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('EVENT_BEGIN', 1),
	Insn('CALL', Function((0, 27))),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (-22500, 6000, 21500), 182),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#0305F哦……\n'
				'往这边走的话，就回到\n'
				'建筑物里面去了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F还什么都没发现呢，\n'
				'再调查一下吧。{wait}'
				'{page}'
				'这个屋顶上出现了狼型魔兽……\n'
				'我们就来寻找可以证明这一点的证据吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(5)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F还什么都没发现呢，\n'
				'继续在屋顶上寻找\n'
				'狼型魔兽曾经出现的证据吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]
