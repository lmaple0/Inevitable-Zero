# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't105b',
	'name2': 't105b',
	'location': 67,
	'bgm': 513,
	'flags': 8192,
	'includes': [
		None,
		None,
		None,
		None,
		None,
		None,
	],
	'name3': 't105b',
	'labels': [],
	'chcp': [
		'chr/ch25800',
		'chr/ch25600',
		'chr/ch25700',
		'chr/ch32300',
		None,
		None,
		'chr/ch20202',
		'chr/ch20302',
	],
	'npcs': [
		{
			'name': Translate('哈格总管'),
			'pos': (-479, 0, 10050),
			'angle': 180,
			'_1': b'\x01\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((0, 8)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('萝琪'),
			'pos': (-93959, 0, 8260),
			'angle': 270,
			'_1': b'\x01\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('希崔丝'),
			'pos': (94190, 0, 11579),
			'angle': 90,
			'_1': b'\x01\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 10)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (-99480, 0, -80559),
			'angle': 90,
			'_1': b'\x01\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (97559, 150, -84309),
			'angle': 90,
			'_1': b'U\x01\x00\x00\x06\x00\xff\xff',
			'function': Function((0, 12)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (100540, 150, -84309),
			'angle': 270,
			'_1': b'U\x01\x00\x00\x07\x00\xff\xff',
			'function': Function((0, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
	],
	'monsters': [],
	'triggers': [],
	'objects': [
		{
			'pos': (-20, 0, 8270),
			'range': 1500,
			'bubble_pos': (-480, 1500, 10050),
			'_1': b'~\x00\x00',
			'function': Function((0, 7)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (5500, 0, 13500),
			'range': 1200,
			'bubble_pos': (5500, 1500, 13500),
			'_1': b'|\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-96600, 0, 120560),
			'range': 1500,
			'bubble_pos': (-96600, 1000, 120560),
			'_1': b'|\x00\x00',
			'function': Function((0, 6)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00C\x00', Function((0, 4)), Function((0, 5))),
	'code': [None]*16,
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
		Insn('0x95', Char(254), (-106030, 0, 8260), 2000, 0),
		Insn('0x95', Char(254), (-106030, 0, 11300), 2000, 0),
		Insn('0x95', Char(254), (-93960, 0, 11300), 2000, 0),
		Insn('0x95', Char(254), (-93960, 0, 8260), 2000, 0),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('0x95', Char(254), (106130, 0, 11580), 2000, 0),
		Insn('0x95', Char(254), (106130, 0, 8150), 2000, 0),
		Insn('0x95', Char(254), (94190, 0, 8150), 2000, 0),
		Insn('0x95', Char(254), (94190, 0, 11580), 2000, 0),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_IDLE', Char(254), (-101620, -81790), (-98170, -78910), 1000),
		Insn('SLEEP', 400),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 14))),
		]),
		(None, []),
	]),
	Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
	Insn('FORK_FUNC', Char(10), 0, Function((0, 2))),
	Insn('FORK_FUNC', Char(11), 0, Function((0, 3))),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('0xF2', Insn('BED')),
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, -1, 1, Text(
		'在此地休息\n'
		'放弃\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('SOUND_LOAD', 13),
			Insn('BGM_STOP', 3000),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('SLEEP', 700),
			Insn('SOUND_PLAY', 13, 0, 0, 100),
			Insn('0x0D'),
			Insn('0x32', Party(255), -2, 0),
			Insn('0x6A', b'\x00\x00\x00\x00\x00\x00'),
			Insn('0x31', b'\x01\x08\xac\r'),
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

data['code'][7] = [
	Insn('CALL', Function((0, 8))),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('TEXT_START', Char(8)),
	Insn('TEXT_TALK', Char(8), Text(
		'瓦奇先生带来的客人们……\n'
		'要出门吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'如果准备享用晚餐的话，\n'
		'推荐去商店街里面那家名为\n'
		'《幸运》的餐厅哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(8)),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'啊，瓦奇先生\n'
		'不知跑到哪里去了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'我还想再好好欣赏一下\n'
		'他那美丽的面孔呢㈱{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'要申请\n'
		'客房服务吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'请您稍等，\n'
		'稍后会为您送上\n'
		'葡萄酒与小吃。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'呼……\n'
		'还好订到房间了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'哎呀，一直坚持下来，\n'
		'等待别人取消预订，\n'
		'总算是有回报了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'为了纪念庆典的夜晚，干杯。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'呵呵，干杯。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1353)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(257), (-97500, 0, 124700), 0),
			Insn('CHAR_SET_POS', Char(258), (-96400, 0, 124700), 0),
			Insn('CHAR_SET_POS', Char(259), (-96400, 0, 123500), 0),
			Insn('CHAR_SET_POS', Char(260), (-97500, 0, 123500), 0),
			Insn('CHAR_SET_POS', Char(337), (-98000, 0, 121100), 0),
		]),
		(Expr([Insn('FLAG', Flag(1354)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(257), (-97500, 0, 124700), 0),
			Insn('CHAR_SET_POS', Char(258), (-96400, 0, 123500), 0),
			Insn('CHAR_SET_POS', Char(259), (-96400, 0, 124700), 0),
			Insn('CHAR_SET_POS', Char(260), (-97500, 0, 123500), 0),
			Insn('CHAR_SET_POS', Char(337), (-98000, 0, 121100), 0),
		]),
		(Expr([Insn('FLAG', Flag(1355)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(257), (-97500, 0, 124700), 0),
			Insn('CHAR_SET_POS', Char(258), (-97500, 0, 123500), 0),
			Insn('CHAR_SET_POS', Char(259), (-96400, 0, 123500), 0),
			Insn('CHAR_SET_POS', Char(260), (-96400, 0, 124700), 0),
			Insn('CHAR_SET_POS', Char(337), (-98000, 0, 121100), 0),
		]),
		(None, []),
	]),
	Insn('CAM_OFFSET', (-97030, 900, 124240), 0),
	Insn('CAM_ROTATE', 330, 18, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 19350, 0),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('CAM_DISTANCE', 18350, 3000),
	Insn('0x6F', b'\x10'),
	Insn('0x0D'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1353)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13500686V#0202F#6P……好漂亮……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#13500687V#5302F#6P呵呵，是啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#13500688V#5006F#6P没想到晚上\n'
				'居然会放烟火呢。{wait}'
				'{page}'
				'#13500689V#5000F这是纪念庆典的独有节目吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#13500690V#0300F#6P不，好像每天都会如此哦。{wait}'
				'{page}'
				'#13500691V主题乐园的夜晚，\n'
				'才刚刚开始吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1354)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13500686V#5402F#6P……好漂亮……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#13500687V#0102F#6P呵呵，是啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#13500688V#5006F#6P没想到晚上\n'
				'居然会放烟火呢。{wait}'
				'{page}'
				'#13500689V#5000F这是纪念庆典的独有节目吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#13500690V#0300F#6P不，好像每天都会如此哦。{wait}'
				'{page}'
				'#13500691V主题乐园的夜晚，\n'
				'才刚刚开始吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1355)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13500686V#0202F#6P……好漂亮……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#13500687V#0102F#6P呵呵，是啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#13500688V#5006F#6P没想到晚上\n'
				'居然会放烟火呢。{wait}'
				'{page}'
				'#13500689V#5000F这是纪念庆典的独有节目吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#13500690V#5600F#6P不，好像每天都会如此哦。{wait}'
				'{page}'
				'#13500691V主题乐园的夜晚，\n'
				'才刚刚开始吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(337), Text(
		'#13500692V#5704F#6P夜间游行，\n'
		'还有被彩灯装点的观览车……{wait}'
		'{page}'
		'#13500693V呵呵，这可是向女孩子\n'
		'示爱的绝佳场景哦。{wait}'
		'{page}'
		'#13500694V#5700F──那么，\n'
		'我就先走一步啦。{wait}'
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
	Insn('CAM_OFFSET', (-97750, 900, 123480), 2000),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500695V#5000F#11P这样啊……你是要去见\n'
		'某位女士吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(337), Text(
		'#13500696V#5702F#6P呵呵，算是吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(337), 180, 400),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(337), Text(
		'#13500697V#5704F#11P那么，愿女神赐予你们幸运。{wait}'
		'{page}'
		'#13500698V#5702F如果你们没有搞砸的话，\n'
		'我们就在拍卖会场中再见吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 200),
	Insn('SLEEP', 500),
	Insn('CAM_OFFSET', (-99750, 900, 120550), 3500),
	Insn('0x95', Char(337), (-100000, 0, 116800), 2000, 1),
	Insn('FORK', 337, 1, [
		Insn('0x95', Char(254), (-100000, 0, 114300), 2000, 0),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 337, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('SOUND_PLAY', 121, 0, 0, 100),
	Insn('FORK_AWAIT', Char(337), 1),
	Insn('FORK_AWAIT', Char(337), 2),
	Insn('SOUND_PLAY', 890, 0, 0, 100),
	Insn('0x6F', b'y'),
	Insn('SLEEP', 300),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-97040, 900, 124460), 0),
	Insn('CAM_ROTATE', 330, 18, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 17300, 0),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1353)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13500699V#0306F#11P哎呀呀……\n'
				'真是个嚣张的家伙啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#13500700V#0206F#12P既是不良分子的头目，\n'
				'又是上流阶级中的贵客……{wait}'
				'{page}'
				'#13500701V#0211F他在各方面都很可疑呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#13500702V#5304F#11P不过，说实话，他能够告诉我们\n'
				'拍卖会的情报，真是帮大忙了。{wait}'
				'{page}'
				'#13500703V#5300F我们算是欠了他一个人情呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1354)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13500699V#0306F#11P哎呀呀……\n'
				'真是个嚣张的家伙啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#13500700V#5406F#11P既是不良分子的头目，\n'
				'又是上流阶级中的贵客……{wait}'
				'{page}'
				'#13500701V#5411F他在各方面都很可疑呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#13500702V#0104F#12P不过，说实话，他能够告诉我们\n'
				'拍卖会的情报，真是帮大忙了。{wait}'
				'{page}'
				'#13500703V#0100F我们算是欠了他一个人情呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1355)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13500699V#5606F#11P哎呀呀……\n'
				'真是个嚣张的家伙啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#13500700V#0206F#12P既是不良分子的头目，\n'
				'又是上流阶级中的贵客……{wait}'
				'{page}'
				'#13500701V#0211F他在各方面都很可疑呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#13500702V#0104F#11P不过，说实话，他能够告诉我们\n'
				'拍卖会的情报，真是帮大忙了。{wait}'
				'{page}'
				'#13500703V#0100F我们算是欠了他一个人情呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500704V#5000F#11P嗯……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(259), 1),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('CHAR_ROTATE', Char(257), 135, 400),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500705V#5003F#5P──我们差不多也该\n'
		'前往拍卖会场了。{wait}'
		'{page}'
		'#13500706V#5001F必须要想办法混过入口的检查，\n'
		'潜入到会场里。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 500),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1353)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13500707V#5301F#12P嗯……没错！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1354)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13500708V#5401F#12P是……！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1355)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13500709V#5601F#12P明白！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CAM_DISTANCE', 17600, 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('MINIGAME', 24, 0, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
	Insn('PARTY_CLEAR'),
	Insn('0x2E', b'\x00\xff\xff'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1353)), Insn('END')]), [
			Insn('0x2E', b'\x01\xef\xff'),
			Insn('0x2E', b'\x02\xff\xff'),
			Insn('0x2E', b'\x03\xff\xff'),
		]),
		(Expr([Insn('FLAG', Flag(1354)), Insn('END')]), [
			Insn('0x2E', b'\x02\xef\xff'),
			Insn('0x2E', b'\x01\xff\xff'),
			Insn('0x2E', b'\x03\xff\xff'),
		]),
		(Expr([Insn('FLAG', Flag(1355)), Insn('END')]), [
			Insn('0x2E', b'\x03\xef\xff'),
			Insn('0x2E', b'\x01\xff\xff'),
			Insn('0x2E', b'\x02\xff\xff'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_POS', Char(0), (-99730, 0, 120850), 180),
	Insn('FLAG_SET', Flag(1319)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 36, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 36, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 36, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 55, Insn('FLAG_UNSET', 64)),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 55, Insn('FLAG_UNSET', 64)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1353)), Insn('END')]), [
			Insn('0xDE', b'*\x00'),
		]),
		(Expr([Insn('FLAG', Flag(1354)), Insn('END')]), [
			Insn('0xDE', b'+\x00'),
		]),
		(Expr([Insn('FLAG', Flag(1355)), Insn('END')]), [
			Insn('0xDE', b',\x00'),
		]),
		(None, []),
	]),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}{0x06}        ～楼梯间～\n'
		'现在三楼的ＶＩＰ层\n'
		'已被包场，\n'
		'无关人士请勿入内。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]
