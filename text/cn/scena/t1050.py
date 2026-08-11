# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't1050',
	'name2': 't1050',
	'location': 67,
	'bgm': 111,
	'flags': 8192,
	'includes': [
		't1050',
		't1030_1',
		None,
		None,
		None,
		None,
	],
	'name3': 't1050',
	'labels': [],
	'chcp': [
		'chr/ch25800',
		'chr/ch25600',
		'chr/ch25700',
		'chr/ch20400',
		'chr/ch20500',
		'chr/ch20200',
		'chr/ch20300',
		'chr/ch08000',
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
			'pos': (-100709, 0, 8859),
			'angle': 270,
			'_1': b'\x01\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('希崔丝'),
			'pos': (-101819, 0, 8859),
			'angle': 90,
			'_1': b'\x01\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 10)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (8970, 0, 6630),
			'angle': 225,
			'_1': b'\x81\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 14)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (8250, 0, 5920),
			'angle': 45,
			'_1': b'\x81\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('瓦奇'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x07\x00\x00\x03',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('托马'),
			'pos': (96220, 0, 121949),
			'angle': 270,
			'_1': b'\x05\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 12)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('阿尔维娜'),
			'pos': (103230, 0, 124330),
			'angle': 0,
			'_1': b'\x05\x01\x00\x00\x04\x00\x00\x00',
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
			'function': Function((0, 28)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-99830, 0, 13590),
			'range': 1200,
			'bubble_pos': (-99830, 1500, 13590),
			'_1': b'|\x00\x00',
			'function': Function((0, 29)),
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
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00C\x00', Function((0, 4)), Function((0, 5))),
	'code': [None]*31,
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
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 104), Insn('EQ'), Insn('FLAG', Flag(1317)), Insn('BOOL_AND'), Insn('FLAG', Flag(1360)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('FLAG_SET', Flag(1360)),
			Insn('OBJ_FLAG_UNSET', Object(2), 16),
			Insn('0x70', Object(2), b'\n\x00'),
			Insn('CHAR_FLAG1_UNSET', Char(254), 128),
			Insn('CHAR_FLAG2_UNSET', Char(254), 32768),
			Insn('CHAR_SET_POS', Char(254), (-100040, 0, 13630), 0),
			Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xdc\x05\x00\x00\xd0\x07\x00\x00\x00'),
			Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
			Insn('CHAR_FLAG1_SET', Char(13), 128),
			Insn('CHAR_FLAG2_SET', Char(13), 32768),
			Insn('0x71', Object(2), b'\n\x00', 0, 0),
			Insn('SOUND_PLAY', 890, 0, 0, 100),
			Insn('0x79', b'\x02\x00'),
			Insn('OBJ_FLAG_SET', Object(2), 16),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 107), Insn('EQ'), Insn('FLAG', Flag(1317)), Insn('BOOL_AND'), Insn('FLAG', Flag(1318)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 19))),
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
			Insn('CHAR_SET_POS', Char(9), (-93960, 0, 8260), 0),
			Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
			Insn('CHAR_SET_POS', Char(10), (94190, 0, 11580), 0),
			Insn('FORK_FUNC', Char(10), 0, Function((0, 2))),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('0x65', 2, 1),
	Insn('OBJ_FLAG_SET', Object(2), 16),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1312)), Insn('FLAG', Flag(1317)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x66', 2, 1),
			Insn('OBJ_FLAG_UNSET', Object(2), 16),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1360)), Insn('END')]), [
			Insn('FORK_QUIT', Char(13), 255),
			Insn('CHAR_FLAG1_SET', Char(13), 128),
			Insn('CHAR_FLAG2_SET', Char(13), 32768),
		]),
		(None, []),
	]),
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
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1316)), Insn('FLAG', Flag(1317)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 16))),
		]),
		(None, [
			Insn('TEXT_START', Char(8)),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1333)), Insn('END')]), []),
				(Expr([Insn('FLAG', Flag(1330)), Insn('END')]), []),
				(Expr([Insn('FLAG', Flag(1329)), Insn('END')]), []),
				(Expr([Insn('FLAG', Flag(1320)), Insn('END')]), []),
				(Expr([Insn('FLAG', Flag(1319)), Insn('END')]), []),
				(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
							Insn('CHAR_WATCH', Char(8), Char(337), 0),
							Insn('TEXT_TALK', Char(8), Text(
								'瓦奇先生，您要出门吗？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'那么，在此期间，\n'
								'我来为您\n'
								'整理床铺吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(337), Text(
								'#5700F是啊，大概会出去一段时间……\n'
								'那就拜托你了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'明白了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(0)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(8), Text(
								'那么，\n'
								'在您外出期间，我会帮您\n'
								'整理好床铺的。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'请您慢走。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1317)), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'客人是瓦奇先生的朋友吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'从左边那扇门进去，\n'
						'右手边就是瓦奇先生的房间了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(8), Text(
								'欢迎，\n'
								'欢迎光临翠雀饭店。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'今天在本店住宿的\n'
								'客人实在不少。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'在本店住宿的客人们\n'
								'似乎都出门\n'
								'观光游玩了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(0)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(8), Text(
								'今天在本店住宿的\n'
								'客人实在不少。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'在本店住宿的客人们\n'
								'似乎都出门\n'
								'观光游玩了。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
				(None, []),
			]),
			Insn('TEXT_END', Char(8)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1333)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1330)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1329)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1320)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1319)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_WATCH', Char(254), Char(337), 0),
					Insn('TEXT_TALK', Char(254), Text(
						'啊，客人…………\n'
						'………………{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(337), Text(
						'#5705F……嗯？找我有事吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'（啊啊……果然\n'
						'\u3000长得好漂亮啊……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(337), Text(
						'#5702F……呵呵，真是个奇怪的女孩。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'啊……您要出门吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'路上请小心，\n'
						'呵呵……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1317)), Insn('END')]), [
			Insn('CHAR_WATCH', Char(254), Char(10), 0),
			Insn('0x4B', Char(10), -1),
			Insn('TEXT_TALK', Char(254), Text(
				'呀～怎么办！\n'
				'看到脸了！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'好啦，你冷静点。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x4C', Char(10), -1),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 11))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'那位办理完登记入住手续之后\n'
						'就马上外出的客人……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'长得真是\n'
						'好可爱哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1333)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1330)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1329)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1320)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1319)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CALL', Function((0, 30))),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'要是有什么问题，\n'
						'请不要客气，尽管告诉我。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我会诚心诚意为您服务的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1317)), Insn('END')]), [
			Insn('CALL', Function((0, 30))),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'这孩子真是的，\n'
						'在客人面前也太不成体统了……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('CALL', Function((0, 30))),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
							Insn('CALL', Function((0, 11))),
						]),
						(None, [
							Insn('TEXT_TALK', Char(254), Text(
								'我说你啊，要是有时间闲聊，\n'
								'还不赶快去打扫下走廊。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('0x4B', Char(9), -1),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_WATCH', Char(9), Char(10), 0),
	Insn('CHAR_WATCH', Char(10), Char(9), 0),
	Insn('TEXT_TALK', Char(9), Text(
		'那个，你看见了吗？\n'
		'刚才的客人……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'虽然长得超级可爱，\n'
		'不过是男孩子吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'你又～来了……\n'
		'别说这种话了，\n'
		'赶快打扫完吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'啊～好在意……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(9), -1),
	Insn('0x4C', Char(10), -1),
	Insn('FLAG_SET', Flag(1)),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'这样应该就能\n'
						'实行我那在烟火下求婚\n'
						'的计划了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'谢谢，真不知道\n'
						'该怎么感谢你们才好。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'好吧……为了晚上能顺利求婚，\n'
						'要开始做心理准备了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(254), Text(
								'好、好的……接下来\n'
								'就要准备去主题乐园了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'虽说已经定好了计划，\n'
								'但是真的能求婚成功吗。\n'
								'我开始紧张起来了……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'不、不行……难得你们\n'
								'帮我找到了戒指。\n'
								'我可不能打退堂鼓啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'总而言之，\n'
								'多重复几次\n'
								'脑内模拟训练吧……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(2)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(254), Text(
								'请和我结婚吧！\n'
								'……嗯。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'我们结婚吧！\n'
								'……这个也不错啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'跟我结婚吧混帐！\n'
								'……这个不行吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'好吧……为了晚上能顺利求婚，\n'
						'要开始做心理准备了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我觉得，阿尔维娜是否会\n'
						'接受我的求婚……\n'
						'也就决定了我的生死……！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F这话也太夸张了……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 9))), Insn('END')]), [
			Insn('CALL', Function((0, 27))),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 7))), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'总、总而言之，你们！\n'
				'能不能去高级住宅区\n'
				'那边帮我看看！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'戒指说不定\n'
				'还在那个长椅\n'
				'附近呢……！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 1))), Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 2))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 26))),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 3))), Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 4))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 26))),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 5))), Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 6))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 26))),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('FLAG_GET', 2))), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我完全不记得\n'
				'将戒指丢在哪里了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过可以确定的是……\n'
				'我和阿尔维娜来到这边以后，\n'
				'基本上到处都逛了一遍。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'总、总而言之……\n'
				'要是你们捡到了类似的东西，\n'
				'就都拿来给我看看吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('CALL', Function((0, 25))),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'托马好像很开心呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'是不是有什么\n'
						'好事呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'托马好像打算\n'
						'在主题乐园做什么。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，他有什么心事，都马上会显露在脸上，\n'
						'真是太容易看穿了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'别人经常问我，\n'
						'为什么会和托马\n'
						'交往……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'你们不觉得托马\n'
						'看起来就很搞笑吗？\n'
						'那就是他的魅力啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 7))), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'托马真是的……\n'
				'今天一会消沉沮丧，一会又大喊大叫的，\n'
				'好像不太对劲呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哎，算了。\n'
				'反正他自己也说没什么事。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'今晚我要和托马两个人\n'
				'去夜晚的主题乐园。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'听说到时候会放很多烟火，\n'
				'可以度过一个非常浪漫的\n'
				'夜晚呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，好期待哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'太阳也西沉了，\n'
		'今天就和我太太回来休息了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'在房间里一边欣赏主题乐园的烟火，\n'
		'一边品尝葡萄酒，也别有一番风致吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'事先\n'
		'预约了饭店，\n'
		'真是太好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('0x4B', Char(8), -1),
	Insn('0x4B', Char(13), -1),
	Insn('CHAR_FLAG1_UNSET', Char(13), 128),
	Insn('CHAR_FLAG2_UNSET', Char(13), 32768),
	Insn('CHAR_SET_POS', Char(13), (-16950, 0, 11920), 45),
	Insn('CHAR_SET_COLOR', Char(13), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_SET', Char(13), 32768),
	Insn('CAM_OFFSET', (-240, 1100, 7180), 0),
	Insn('CAM_ROTATE', 327, 16, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 16470, 0),
	Insn('CHAR_SET_POS', Char(257), (-500, 0, 6400), 0),
	Insn('CHAR_SET_POS', Char(258), (500, 0, 6400), 0),
	Insn('CHAR_SET_POS', Char(259), (500, 0, 5000), 0),
	Insn('CHAR_SET_POS', Char(260), (-500, 0, 5000), 0),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu05700.itp'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13500440V#11P欢迎，\n'
		'欢迎光临翠雀饭店。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13500441V#11P莫非……\n'
		'各位想在本饭店住宿吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500442V#0100F#6P嗯，是的，\n'
		'不过现在都已经住满了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13500443V#11P是的，非常抱歉。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13500444V#11P其实就在不久前，\n'
		'刚好有位客人取消了预订的房间，\n'
		'但是那个房间马上就又被预约了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500445V#0106F#6P是这样吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500446V#0206F#6P……真可惜。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500447V#0306F#6P没办法，\n'
		'去餐厅那边吧。{wait}'
		'{page}'
		'#13500448V#0300F至少可以坐下来讲。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500449V#0006F#11P是啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK2', Char(13), Translate('冷静的声音'), Text(
		'#13500450V#4P#17A呵呵……\n'
		'你们好像有烦恼啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (-1880, 1100, 6720), 5100),
	Insn('CAM_ROTATE', 307, 16, 0, 5100),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 315, 300),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 315, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 315, 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 315, 300),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 8, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 500),
	]),
	Insn('OBJ_FLAG_UNSET', Object(5), 16),
	Insn('0x70', Object(5), b'\n\x00'),
	Insn('CHAR_SET_COLOR', Char(13), Color(0xFFFFFFFF), 0),
	Insn('FORK_FUNC', Char(13), 3, Function((0, 17))),
	Insn('0x71', Object(5), b'\n\x00', 0, 0),
	Insn('0x79', b'\x05\x00'),
	Insn('OBJ_FLAG_SET', Object(5), 16),
	Insn('FORK_AWAIT', Char(13), 3),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(8), 1),
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
	Insn('TEXT_TALK', Char(257), Text(
		'#13500451V#0005F#12P哎……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500452V#0105F#12P瓦、瓦奇……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13500453V#2P啊，瓦奇先生……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 200),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 700),
	Insn('TEXT_MESSAGE', Char(13), Text(
		'#13500454V你们似乎正因为订不到房间\n'
		'而发愁吧……{wait}'
		'{page}'
		'#13500455V是不是需要一个\n'
		'可以安静谈话的地方呢？{wait}'
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
		'#13500456V#0000F#12P啊，是的，\n'
		'是这样没错……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13500457V#5704F#5P#N那就好说了。{wait}'
		'{page}'
		'#13500458V把我的房间借给你们吧。{wait}'
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
	Insn('TEXT_TALK', Char(257), Text(
		'#13500459V#0011F#12P哎！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500460V#0305F#6P喂喂，真突然啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13500461V#5702F#5P#N呵呵，来这边。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (-3940, 1200, 6960), 5000),
	Insn('FORK_FUNC', Char(13), 3, Function((0, 18))),
	Insn('FORK_AWAIT', Char(13), 3),
	Insn('0x6F', b'\x01'),
	Insn('CAM_OFFSET', (-1350, 1100, 6510), 1200),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 300),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500462V#0101F#12P怎、怎么办……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500463V#0211F#6P他的穿着打扮\n'
		'明显很可疑……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500464V#0301F#6P我说，不良分子的\n'
		'首领为什么会在\n'
		'这种地方啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500465V#0006F#5P好、好啦，\n'
		'反正也不是不认识的陌生人……{wait}'
		'{page}'
		'#13500466V#0000F总之，跟去看看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (40, 0, 6580), 270),
	Insn('CHAR_SET_POS', Char(8), (-480, 0, 10050), 180),
	Insn('0x4C', Char(8), -1),
	Insn('CHAR_FLAG1_UNSET', Char(13), 32768),
	Insn('CHAR_SET_POS', Char(13), (0, 0, 0), 0),
	Insn('0x4C', Char(13), -1),
	Insn('FLAG_SET', Flag(1317)),
	Insn('QUEST', 71, Insn('TASK_SET', 4)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('0x95', Char(254), (-4000, 0, 8400), 3000, 0),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('CHAR_ROTATE', Char(254), 270, 500),
	Insn('0x96', Char(254), (-16329, 0, 12010), 2500, 0),
	Insn('OBJ_FLAG_UNSET', Object(5), 16),
	Insn('0x71', Object(5), b'\x00\x00', 10, 0),
	Insn('SOUND_PLAY', 121, 0, 0, 100),
	Insn('0x79', b'\x05\x00'),
	Insn('FORK', 254, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xb8\x0b\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 200),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('0x71', Object(5), b'\n\x00', 0, 0),
	Insn('SOUND_PLAY', 890, 0, 0, 100),
	Insn('0x79', b'\x05\x00'),
	Insn('OBJ_FLAG_SET', Object(5), 16),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50353', 30),
	Insn('CAM_OFFSET', (-99800, 1100, 124250), 0),
	Insn('CAM_ROTATE', 315, 17, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 17000, 0),
	Insn('0x4B', Char(13), -1),
	Insn('CHAR_SET_CHCP', Char(13), 30),
	Insn('CHAR_SET_FRAME', Char(13), 2),
	Insn('CHAR_FLAG1_UNSET', Char(13), 128),
	Insn('CHAR_FLAG2_UNSET', Char(13), 32768),
	Insn('CHAR_SET_COLOR', Char(13), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_POS', Char(13), (-102200, 150, 124000), 90),
	Insn('CHAR_SET_POS', Char(257), (-101400, 0, 121700), 0),
	Insn('CHAR_SET_POS', Char(258), (-100300, 0, 121700), 315),
	Insn('CHAR_SET_POS', Char(259), (-100300, 0, 120400), 315),
	Insn('CHAR_SET_POS', Char(260), (-101400, 0, 120400), 0),
	Insn('IMG_LOAD', ResId(0), 112, 8, b'p\x01\x08\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis063.itp'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (-101070, 1100, 122980), 3000),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13500467V#5709F#11P呵呵，话说回来，\n'
		'你们也很有雅兴嘛。{wait}'
		'{page}'
		'#13500468V#5702F在纪念庆典的最终日，\n'
		'竟然请假来米修拉姆挥霍。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500469V#0012F#6P啊……\n'
		'嗯，算是养精蓄锐吧。{wait}'
		'{page}'
		'#13500470V#0001F话说回来，瓦奇，\n'
		'你这身打扮是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13500471V#5704F#11P呵呵，很适合我吧？{wait}'
		'{page}'
		'#13500472V#5700F这个算是我\n'
		'副业的制服啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500473V#0005F#6P副、副业……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500474V#0101F#6P那到底是什么工作呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13500475V#5703F#11P在冰冷的上流阶级世界中\n'
		'有着许多迷失了爱的、\n'
		'美丽而寂寞的贵妇人们……{wait}'
		'{page}'
		'#13500476V#5702F为她们营造短暂的梦境，\n'
		'就是我的工作。{wait}'
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
	Insn('TEXT_TALK', Char(257), Text(
		'#13500477V#0011F#6P什么……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500478V#0105F#6P这、这莫非就是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500479V#0211F#6P所谓的『男公关』吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500480V#0307F#6P喂喂！\n'
		'你竟然做这种令人羡慕──\n'
		'不对，是不知廉耻的工作！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13500481V#5702F#11P呵呵，我可不是\n'
		'因为缺钱才干这行的。{wait}'
		'{page}'
		'#13500482V只是一直被她们纠缠不休，\n'
		'无奈之下才稍作奉陪的。{wait}'
		'{page}'
		'#13500483V#5709F嗯，可以算是行善吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500484V#0006F#6P这是什么借口……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500485V#0306F#6P也就是说，还有不少\n'
		'太太喜欢这种\n'
		'冷酷的家伙啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500486V#0103F#6P唉……\n'
		'说实话，我可是不敢苟同。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500487V#0200F#6P这么说，瓦奇先生\n'
		'是因为男公关的工作而来这里的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13500488V#5702F#11P嗯，其实也就是所谓的\n'
		'护花使者吧。{wait}'
		'{page}'
		'#13500489V我要陪同\n'
		'某位夫人出席一个\n'
		'有点隐情的宴会。{wait}'
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
	Insn('TEXT_TALK', Char(257), Text(
		'#13500490V#0005F#6P哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500491V#0101F#6P这……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(13), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(13), Text(
		'#13500492V#5704F#11P呵呵……原来如此啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 0)),
	Insn('EMOTE', Char(258), 0, 2000, (40, 43, 100, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (40, 43, 100, 0)),
	Insn('EMOTE', Char(260), 0, 2000, (40, 43, 100, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500493V#0012F#6P原来如此是指……\n'
		'嗯，你在说什么呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13500494V#5702F#11P『黑之拍卖会#10RSchwarz Auction#』……{wait}'
		'{page}'
		'#13500495V#5702F你们多半是得知了这个名字，\n'
		'才过来调查的吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500496V#0001F#6P唔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500497V#0306F#6P唉……\n'
		'目的好像暴露了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500498V#0101F#6P如此说来，你说要出席的\n'
		'那个有点隐情的宴会也就是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13500499V#5700F#11P嗯，就是那个拍卖会。{wait}'
		'{page}'
		'#13500500V#5704F去年也陪别的夫人\n'
		'去过，所以今年是第二次去了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500501V#0006F#6P是这样啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500502V#0206F#6P没想到了解那个拍卖会\n'
		'的人就近在身边呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13500503V#5705F#11P不过，你们是打算\n'
		'揭发那个拍卖会吗？{wait}'
		'{page}'
		'#13500504V我觉得，那实在是有点勉强。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500505V#0006F#6P不……虽然不甘心，\n'
		'不过我们原本就没打算去揭发它。{wait}'
		'{page}'
		'#13500506V#0008F只是想了解一下。{wait}'
		'{page}'
		'#13500507V象征着克洛斯贝尔扭曲现状的，\n'
		'豪华绚烂的地下社交宴会……{wait}'
		'{page}'
		'#13500508V#0013F我们需要跨越的『障壁』\n'
		'究竟高到何种程度。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500509V#0105F#6P罗伊德……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13500510V#5702F#11P呵呵……原来如此啊。{wait}'
		'{page}'
		'#13500511V#5704F你们的志气我很欣赏，\n'
		'不过，想参加『拍卖会』的话，\n'
		'没有邀请卡可是进不去的哦。{wait}'
		'{page}'
		'#13500512V他们每年都会在卡片上设计不同的蔷薇标志，\n'
		'而且上面还附带通行号码，\n'
		'要伪造恐怕很难……{wait}'
		'{page}'
		'#13500513V#5702F我觉得，应该是没办法混进去的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500514V#0000F#6P关于这点不必担心……\n'
		'其实，我们有邀请卡的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 18, 0, 0, 100),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('SLEEP', 500),
	Insn('TEXT_MESSAGE', Char(13), Text(
		'#13500515V#5705F哎……{wait}'
		'{page}'
		'#13500516V#5709F如果问你们是怎么得到的，\n'
		'是不是就有点不识趣了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#13500517V#0004F嗯，稍微有点内情。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500518V#0108F#6P说到这张邀请卡……\n'
		'在拿着它入场时，会不会被检查身份呢？{wait}'
		'{page}'
		'#13500519V#0101F比如仅限会员，或是只有登记过的人\n'
		'才能进去之类的……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13500520V#5705F#11P不，我想应该不会。{wait}'
		'{page}'
		'#13500521V#5704F这场活动也有地下社交的含义在内，\n'
		'所以好像很欢迎新来的客人。{wait}'
		'{page}'
		'#13500522V#5702F再加上拍卖品中还有赃物，\n'
		'所以很多有权人士也会\n'
		'想要隐藏身份。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500523V#0300F#6P唔，这样的话，\n'
		'说不定能顺利混进去。{wait}'
		'{page}'
		'#13500524V#0305F话说回来，一张邀请卡\n'
		'可以让几个人进去呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13500525V#5703F#11P关于这点，好像并没有硬性规定……\n'
		'不过基本都是两人一组去的。{wait}'
		'{page}'
		'#13500526V#5700F四人一组进去的话，\n'
		'未免也太显眼了，我可不推荐呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500527V#0201F#6P原来如此……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500528V#0106F#6P……这么一说，\n'
		'的确有道理呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13500529V#5704F#11P而且，那终究是场宴会，\n'
		'最好还是穿正装参加吧。{wait}'
		'{page}'
		'#13500530V#5702F不过，穿成我这样，\n'
		'故意引人注目也是一种选择。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500531V#0006F#6P那还是免了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(258), 400),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500532V#0001F#5P──那个，艾莉。{wait}'
		'{page}'
		'#13500533V有没有可以弄到\n'
		'宴会正装的地方呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(258), Char(257), 400),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500534V#0102F#12P要换正装的话，楼下的时装店\n'
		'应该正合适。{wait}'
		'{page}'
		'#13500535V我以前来的时候也去过，\n'
		'衣服钱就先由我垫付吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500536V#0011F#5P不，这个就……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500537V#0104F#12P这点小事就不必客气了。{wait}'
		'{page}'
		'#13500538V#0100F现在更重要的问题是\n'
		'决定潜入的成员吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500539V#0006F#5P嗯……是啊。{wait}'
		'{page}'
		'#13500540V#0008F用抽签或猜拳\n'
		'来决定好像也不太合适……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500541V#0306F#6P喂喂，说什么呢。{wait}'
		'{page}'
		'#13500542V#0300F至少你肯定要去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500543V#0005F#5P哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(259), 400),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500544V#0204F#6P对于这次的事情，最介意的\n'
		'就是罗伊德前辈……{wait}'
		'{page}'
		'#13500545V#0202F而且你是我们的队长，\n'
		'你去是理所当然的吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500546V#0005F#5P可、可是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500547V#0103F#12P真是的，你就坦率地\n'
		'接受吧。{wait}'
		'{page}'
		'#13500548V#0102F你也很想亲眼看看吧？\n'
		'克洛斯贝尔那『扭曲』的实态。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500549V#0004F#5P──好吧，\n'
		'那我就接受了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#13500550V#5704F#11P呵呵，那你再决定一个\n'
		'同行的人选就好了。{wait}'
		'{page}'
		'#13500551V#5702F如果一个人参加的话，\n'
		'反而会更加显眼吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500552V#0006F#5P是啊……嗯～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500553V#0103F#12P是选我、缇欧，还是兰迪。{wait}'
		'{page}'
		'#13500554V#0100F选择的时候，或许也应该\n'
		'考虑到有黑手党在场的情况呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500555V#0204F#6P剩下的两人就在会场外\n'
		'待命，以防紧急状况发生。{wait}'
		'{page}'
		'#13500556V#0202F任务分配应该就是这样吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500557V#0302F#6P嗯，不管怎么分工，\n'
		'现在还是先去楼下的时装店看看吧。{wait}'
		'{page}'
		'#13500558V在换上正装之前\n'
		'决定好带谁去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500559V#0000F#5P……嗯，\n'
		'就这么办吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 17500, 2000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('CHAR_SET_CHCP', Char(13), 0),
	Insn('CHAR_SET_FRAME', Char(13), 0),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 30),
	Insn('0x2E', b'P\xff\xff'),
	Insn('CAM_OFFSET', (-100000, 1250, 12500), 0),
	Insn('CAM_ROTATE', 315, 18, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 18600, 0),
	Insn('CHAR_SET_POS', Char(257), (-100030, 0, 14990), 180),
	Insn('CHAR_SET_POS', Char(258), (-100030, 0, 14990), 180),
	Insn('CHAR_SET_POS', Char(259), (-100030, 0, 14990), 180),
	Insn('CHAR_SET_POS', Char(260), (-100030, 0, 14990), 180),
	Insn('CHAR_SET_POS', Char(337), (-100030, 0, 14990), 180),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(337), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_DISTANCE', 17600, 2500),
	Insn('0x6F', b'\x10'),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 121, 0, 0, 100),
	Insn('OBJ_FLAG_UNSET', Object(2), 16),
	Insn('0x71', Object(2), b'\x00\x00', 10, 0),
	Insn('0x79', b'\x02\x00'),
	Insn('CAM_OFFSET', (-100000, 1250, 10500), 4000),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 20))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 21))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 22))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 23))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(337), 3, Function((0, 24))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('FORK_AWAIT', Char(337), 3),
	Insn('0x71', Object(2), b'\n\x00', 0, 0),
	Insn('SLEEP', 100),
	Insn('SOUND_PLAY', 890, 0, 0, 100),
	Insn('0x79', b'\x02\x00'),
	Insn('OBJ_FLAG_SET', Object(2), 16),
	Insn('0x6F', b'\x01'),
	Insn('CHAR_WATCH', Char(257), Char(337), 400),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500560V#0011F#6P──等一下。{wait}'
		'{page}'
		'#13500561V#0001F为什么连瓦奇\n'
		'也要跟来？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(337), 500),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(337), 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(337), 300),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(337), Text(
		'#13500562V#5709F#11P呵呵，机会难得，\n'
		'我可以给你们提供一些\n'
		'搭配服装的诀窍嘛。{wait}'
		'{page}'
		'#13500563V#5702F还可以教你们如何混过\n'
		'黑手党的盘查哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500564V#0006F#6P嗯……\n'
		'好吧，既然是这样的话。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500565V#0211F#6P但你明显只是\n'
		'为了满足自己的兴趣而已。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500566V#0302F#5P好啦，就姑且听听他能说出些什么吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500567V#0100F#5P那么，我们现在就去\n'
		'楼下的时装店吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (-99720, 0, 10000), 90),
	Insn('FLAG_SET', Flag(1318)),
	Insn('QUEST', 71, Insn('TASK_SET', 5)),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('CHAR_SET_POS', Char(9), (-93960, 0, 8260), 0),
	Insn('FORK_FUNC', Char(9), 0, Function((0, 1))),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('CHAR_SET_POS', Char(10), (94190, 0, 11580), 0),
	Insn('FORK_FUNC', Char(10), 0, Function((0, 2))),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-100000, 0, 9000), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-100000, 0, 13000), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-101200, 0, 10800), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-100000, 0, 13000), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-98800, 0, 10200), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-100000, 0, 12000), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-98610, 0, 11590), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('FORK', 254, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (97820, 900, 122220), 0),
	Insn('CAM_ROTATE', 313, 25, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 20810, 0),
	Insn('CHAR_SET_POS', Char(257), (98200, 0, 121000), 270),
	Insn('CHAR_SET_POS', Char(258), (98200, 0, 122200), 270),
	Insn('CHAR_SET_POS', Char(259), (99400, 0, 121000), 270),
	Insn('CHAR_SET_POS', Char(260), (99400, 0, 122200), 270),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(337), (100600, 0, 121600), 270),
		]),
		(None, []),
	]),
	Insn('0x4B', Char(14), -1),
	Insn('CHAR_ROTATE', Char(14), 270, 0),
	Insn('CHAR_SET_FRAME', Char(14), 0),
	Insn('0x4B', Char(15), -1),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P为什么啊……\n'
		'我到底做了什么啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(14), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(14), 90, 500),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P你们……\n'
		'在游憩区米修拉姆\n'
		'有没有捡到什么？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P怎么说呢，那个……\n'
		'比如说，类似订婚戒指的指环什么的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0005F不，什么也没捡到过……{wait}'
		'{page}'
		'#0001F……您把订婚戒指\n'
		'弄丢了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P#5S哇～声音太大啦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (99540, 1200, 123070), 2000),
	Insn('0x6F', b'\x01'),
	Insn('EMOTE', Char(15), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(15), 270, 500),
	Insn('TEXT_TALK', Char(15), Text(
		'#12P托马？你怎么了，\n'
		'突然叫得那么大声。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(14), 0, 2000, (40, 43, 100, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(14)),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P呃……啊，不……\n'
		'没、没什么啦，\n'
		'阿尔维娜。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'#12P……是吗？\n'
		'呵呵，托马好奇怪啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(15), 0, 500),
	Insn('CAM_OFFSET', (97820, 900, 122220), 2000),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P……差、差点就被\n'
		'阿尔维娜发现啦。\n'
		'你可真是的……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0006F哦、哦……对不起。\n'
		'（刚才那是我的错吗……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P总而言之……\n'
		'作为道歉，你要帮我的忙。\n'
		'帮我找戒指。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0303F喂喂……\n'
		'为了什么道歉啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0203F我觉得完全没有这个义务。\n'
		'无视他就好，我们走吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P失、失礼了，是我用词不当。\n'
		'求你们了，帮帮我吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P你们知道在今晚的\n'
		'主题乐园夜场会燃放烟火吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P那枚戒指，我无论如何\n'
		'也想在那种绝佳的\n'
		'气氛中交给女朋友啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('TEXT_TALK', Char(337), Text(
				'#5700F#12P呵呵，还挺浪漫呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#12P#0102F嗯，是呀。{wait}'
				'{page}'
				'#0100F虽然我们也\n'
				'没多少闲置时间……\n'
				'不过就帮您留意一下吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(258), Text(
				'#12P#0102F呵呵……真不错呢。{wait}'
				'{page}'
				'#0100F虽然我们也\n'
				'没多少闲置时间……\n'
				'不过就帮您留意一下吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P哦哦……真的吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0011F……艾、艾莉？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0104F呵呵，没关系嘛。{wait}'
		'{page}'
		'这是他为了女朋友\n'
		'拼命想出来的\n'
		'求婚方案啊。{wait}'
		'{page}'
		'#0100F如果不能顺利实施，\n'
		'他的女朋友也很可怜嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#006F话虽如此，\n'
				'但终究不能让瓦奇这个民间人士\n'
				'跟我们一起到处跑……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(337), Text(
				'#5704F#12P我可是完全不介意哦。{wait}'
				'{page}'
				'#5700F反正，只要别忘记\n'
				'自己来此的首要目的\n'
				'就没问题了吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0003F嗯，是啊……\n'
				'的确是有点\n'
				'可怜……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0100F呵呵，那就这么定了。{wait}'
		'{page}'
		'#0105F那么……关于弄丢的地点，\n'
		'你有没有头绪呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P很遗憾，没有。\n'
		'我完全没有印象了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P非要说的话……\n'
		'我和阿尔维娜来到这边以后，\n'
		'基本上到处都逛了一遍。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P不过在宝石店吃了闭门羹呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0203F……这提示\n'
		'也太粗略了点。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P总、总而言之……\n'
		'要是你们捡到了类似的东西，\n'
		'就都拿来给我看看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P到了晚上，\n'
		'我们就要进主题乐园了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P知道了吗，拜托了哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 80, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}任务【订婚戒指在何处】{color 0}开始！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('CHAR_ROTATE', Char(14), 270, 0),
	Insn('0x4C', Char(14), -1),
	Insn('0x4C', Char(15), -1),
	Insn('CHAR_SET_POS', Char(0), (97960, 0, 122140), 270),
	Insn('QUEST', 36, Insn('FLAG_UNSET', 2)),
	Insn('QUEST', 36, Insn('TASK_SET', 0)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (97820, 900, 122220), 0),
	Insn('CAM_ROTATE', 313, 25, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 20810, 0),
	Insn('CHAR_SET_POS', Char(257), (98200, 0, 121000), 270),
	Insn('CHAR_SET_POS', Char(258), (98200, 0, 122200), 270),
	Insn('CHAR_SET_POS', Char(259), (99400, 0, 121000), 270),
	Insn('CHAR_SET_POS', Char(260), (99400, 0, 122200), 270),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(337), (100600, 0, 121600), 270),
		]),
		(None, []),
	]),
	Insn('0x4B', Char(14), -1),
	Insn('CHAR_ROTATE', Char(14), 90, 0),
	Insn('CHAR_SET_FRAME', Char(14), 0),
	Insn('0x4B', Char(15), -1),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('0x0D'),
	Insn('EMOTE', Char(14), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P难不成……\n'
		'你们帮我\n'
		'找到戒指了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0000F嗯，这是在游憩区米修拉姆内\n'
		'捡到的。{wait}'
		'{page}'
		'请确认一下\n'
		'是不是您的东西。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 1))), Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 2))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('SOUND_PLAY', 17, 0, 0, 100),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'交出了{item 844}{color 0}。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 3))), Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 4))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('SOUND_PLAY', 17, 0, 0, 100),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'交出了{item 845}{color 0}。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 5))), Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 6))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('SOUND_PLAY', 17, 0, 0, 100),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'交出了{item 846}{color 0}。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
		]),
		(None, []),
	]),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P唔，我看看……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(14), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(14)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 1))), Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 2))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(14), Text(
				'#5P……这枚金戒指……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P……不对，\n'
				'不是这个戒指啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P虽然外观设计相似，\n'
				'但是色泽完全不对。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('QUEST', 36, Insn('TASK_SET', 2)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 3))), Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 4))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(14), Text(
				'#5P……这枚珍珠戒指……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P……不对，\n'
				'不是这个啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P虽然的确很漂亮……\n'
				'但是和我买的\n'
				'一点也不像。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('QUEST', 36, Insn('TASK_SET', 4)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 5))), Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 6))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(14), Text(
				'#5P……这枚白金戒指……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P……不对，\n'
				'不是这个啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P这么俗气的东西，\n'
				'怎么能送给女朋友呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('QUEST', 36, Insn('TASK_SET', 6)),
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
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0006F是、是吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P这个戒指还给你，\n'
		'随你怎么处置吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}托马把交给他的戒指还了回来。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 4))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 6))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EMOTE', Char(14), 0, 2000, (24, 27, 250, 0)),
			Insn('SLEEP', 1000),
			Insn('EMOTE_STOP', Char(14)),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P……明明都找到了\n'
				'这么多戒指，\n'
				'竟然没有我的戒指……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P唉……\n'
				'到底丢在\n'
				'哪里了呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#12P#0100F那个……\n'
				'请不要泄气。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
					Insn('TEXT_TALK', Char(337), Text(
						'#5706F#12P不过……还能\n'
						'到哪里去找呢？{wait}'
						'{page}'
						'#5702F说不定都已经\n'
						'被别人捡走了吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#6P#0011F瓦、瓦奇……！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(14), Text(
						'#5P……果、果然是这样吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(14), 0, 2000, (24, 27, 250, 0)),
					Insn('SLEEP', 1000),
					Insn('EMOTE_STOP', Char(14)),
					Insn('TEXT_TALK', Char(260), Text(
						'#12P#0306F喂喂，他消沉了哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(337), Text(
						'#5709F#12P啊哈哈，\n'
						'开个小玩笑嘛。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(260), Text(
						'#12P#0306F话说，都已经找了这么多地方，\n'
						'却还是没找到，该不会是已经\n'
						'被别人捡走了吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#6P#0011F兰、兰迪……！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(14), Text(
						'#5P……果、果然是这样吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(14), 0, 2000, (24, 27, 250, 0)),
					Insn('SLEEP', 1000),
					Insn('EMOTE_STOP', Char(14)),
					Insn('TEXT_TALK', Char(259), Text(
						'#12P#0203F……完全\n'
						'消沉下去了呢，\n'
						'都怪兰迪前辈。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#12P#0306F怎、怎么怪我啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('CAM_OFFSET', (99540, 1200, 123070), 2000),
			Insn('0x6F', b'\x01'),
			Insn('CHAR_ROTATE', Char(15), 270, 500),
			Insn('EMOTE', Char(15), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 1000),
			Insn('CAM_OFFSET', (99270, 1200, 122850), 2000),
			Insn('0x95', Char(15), (102010, 0, 123530), 2000, 0),
			Insn('CHAR_WATCH', Char(15), Char(14), 500),
			Insn('0x6F', b'\x01'),
			Insn('TEXT_TALK', Char(15), Text(
				'#12P……托马？怎么了，\n'
				'你好像很没精神啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 14, 1, [
				Insn('CHAR_WATCH', Char(254), Char(15), 500),
			]),
			Insn('SLEEP', 100),
			Insn('FORK', 257, 1, [
				Insn('CHAR_ROTATE', Char(254), 45, 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 258, 1, [
				Insn('CHAR_ROTATE', Char(254), 45, 500),
			]),
			Insn('SLEEP', 100),
			Insn('FORK', 259, 1, [
				Insn('CHAR_ROTATE', Char(254), 45, 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 260, 1, [
				Insn('CHAR_ROTATE', Char(254), 45, 500),
			]),
			Insn('SLEEP', 50),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
					Insn('FORK', 337, 1, [
						Insn('CHAR_ROTATE', Char(254), 45, 500),
					]),
				]),
				(None, []),
			]),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P哎！？\n'
				'不，呃，那个……\n'
				'什么事也没有，嗯。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#12P……是吗？\n'
				'你看起来可不像没事啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#12P那个，托马，\n'
				'如果你不舒服的话，\n'
				'要不要去高级住宅区那边透透气？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#12P上午散步的时候，\n'
				'我们不是一起在\n'
				'湖畔的长椅上休息了一下嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P嗯，是啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P………………………………{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(14), 0, 2000, (24, 27, 250, 0)),
			Insn('SLEEP', 1000),
			Insn('EMOTE_STOP', Char(14)),
			Insn('EMOTE', Char(14), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P#5S啊……啊啊啊啊啊啊啊啊啊！！{wait}'
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
			Insn('FORK', 257, 1, [
				Insn('CHAR_ROTATE', Char(254), 270, 500),
			]),
			Insn('SLEEP', 100),
			Insn('FORK', 258, 1, [
				Insn('CHAR_ROTATE', Char(254), 270, 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 259, 1, [
				Insn('CHAR_ROTATE', Char(254), 270, 500),
			]),
			Insn('SLEEP', 100),
			Insn('FORK', 260, 1, [
				Insn('CHAR_ROTATE', Char(254), 270, 500),
			]),
			Insn('SLEEP', 50),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
					Insn('FORK', 337, 1, [
						Insn('CHAR_ROTATE', Char(254), 270, 500),
					]),
				]),
				(None, []),
			]),
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0005F托、托马先生？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 14, 1, [
				Insn('CHAR_ROTATE', Char(254), 90, 500),
			]),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P想起来了，我想起来了！\n'
				'一定是那个时候！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P和阿尔维娜一起\n'
				'坐在长椅上的时候……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P我曾经把手伸进口袋，\n'
				'确认了一下那个的存在啊！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P之后回到饭店，\n'
				'再掏口袋的时候，\n'
				'就已经不见了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P如果真是弄丢了，\n'
				'也只可能是在那个时候，\n'
				'丢在那个地方了！！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0005F真、真的吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#12P#0200F突然就给出了\n'
				'很重要的线索呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#12P……那个，托马，\n'
				'你从刚才起，一直在说什么呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 14, 1, [
				Insn('CHAR_WATCH', Char(254), Char(15), 500),
			]),
			Insn('EMOTE', Char(14), 0, 2000, (40, 43, 100, 0)),
			Insn('SLEEP', 1000),
			Insn('EMOTE_STOP', Char(14)),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P不、不，真的\n'
				'没什么。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P好啦，阿尔维娜，\n'
				'你就好好欣赏一下\n'
				'米修拉姆的美丽街景吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'#12P……是吗？\n'
				'真奇怪呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CAM_OFFSET', (97670, 1200, 121980), 2000),
			Insn('0x95', Char(15), (103230, 0, 124330), 2000, 0),
			Insn('CHAR_ROTATE', Char(15), 0, 500),
			Insn('0x6F', b'\x01'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P好、好险……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 14, 1, [
				Insn('CHAR_ROTATE', Char(254), 90, 500),
			]),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P总、总而言之，你们！\n'
				'能不能去高级住宅区\n'
				'那边帮我看看！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P戒指说不定\n'
				'还在那个长椅\n'
				'附近呢……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#12P#0100F是啊……\n'
				'罗伊德，过去确认\n'
				'一下吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0000F是啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
					Insn('TEXT_TALK', Char(337), Text(
						'#5709F#12P哈哈，和你们在一起，\n'
						'真是不会无聊啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
			Insn('QUEST', 36, Insn('TASK_SET', 7)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(14), Text(
				'#5P唉……\n'
				'到底丢在\n'
				'哪里了呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#5P总而言之……\n'
				'要是你们捡到了类似的戒指，\n'
				'就再拿来给我看吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_ROTATE', Char(14), 270, 0),
	Insn('0x4C', Char(14), -1),
	Insn('0x4C', Char(15), -1),
	Insn('CHAR_SET_POS', Char(0), (97960, 0, 122140), 270),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (97820, 900, 122220), 0),
	Insn('CAM_ROTATE', 313, 25, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 20810, 0),
	Insn('CHAR_SET_POS', Char(257), (98200, 0, 121000), 270),
	Insn('CHAR_SET_POS', Char(258), (98200, 0, 122200), 270),
	Insn('CHAR_SET_POS', Char(259), (99400, 0, 121000), 270),
	Insn('CHAR_SET_POS', Char(260), (99400, 0, 122200), 270),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(337), (100600, 0, 121600), 270),
		]),
		(None, []),
	]),
	Insn('0x4B', Char(14), -1),
	Insn('CHAR_ROTATE', Char(14), 90, 0),
	Insn('CHAR_SET_FRAME', Char(14), 0),
	Insn('0x4B', Char(15), -1),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('0x0D'),
	Insn('EMOTE', Char(14), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P啊！是你们……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P难不成……\n'
		'终于帮我\n'
		'找到戒指了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0000F嗯，找到了类似的东西，\n'
		'请您确认一下。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'交出了{item 847}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_REMOVE', 847, 1),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P唔，我看看……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(14), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(14)),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P……就、就是这个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P就是这个戒指啊，没错！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P银耀石材质的戒指上刻着\n'
		'我和阿尔维娜的名字……\n'
		'的确是我的，没错啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0012F是、是吗，\n'
		'那可太好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0306F哎呀哎呀，\n'
		'我还在担心，你如果又说不是，\n'
		'可该怎么办呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('TEXT_TALK', Char(337), Text(
				'#5702F#12P呵呵，那样的话，\n'
				'再到别处去找不就好了嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#12P#0206F这玩笑开过头了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(259), Text(
				'#12P#0206F真是的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0100F呵呵，太好了呢，\n'
		'顺利找到了戒指。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P嗯，谢谢你们……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P在进入主题乐园之前\n'
		'能够找到，真是太好了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P这样应该就能\n'
		'实行我那烟火下的\n'
		'求婚计划了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P谢谢，真不知道\n'
		'该怎么感谢你们才好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P对了，不嫌弃的话，\n'
		'能不能收下这个？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'获得了{item 154}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 154, 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0005F哎……这、这样好吗？\n'
		'将这么好的东西送给我们……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P嗯，请不必客气，\n'
		'这是我对你们的一片感激之情。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P好吧……为了晚上能顺利求婚，\n'
		'要开始做心理准备了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#5P如果以后还有机会见面的话，\n'
		'还请多多关照啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 9, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}任务【订婚戒指在何处】{color 0}完成！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('CHAR_ROTATE', Char(14), 270, 0),
	Insn('0x4C', Char(14), -1),
	Insn('0x4C', Char(15), -1),
	Insn('CHAR_SET_POS', Char(0), (97960, 0, 122140), 270),
	Insn('QUEST', 36, Insn('TASK_SET', 10)),
	Insn('QUEST', 36, Insn('FLAG_UNSET', 16)),
	Insn('FLAG_SET', Flag(3)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][28] = [
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

data['code'][29] = [
	Insn('TEXT_START', Char(255)),
	Insn('SOUND_PLAY', 810, 0, 0, 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}门似乎上了锁。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][30] = [
	Insn('FLAG_UNSET', Flag(4)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 55, Insn('TASK_GET', 4))), Insn('END')]), [
					Insn('FLAG_SET', Flag(4)),
					Insn('CALL', Function((1, 10))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 55, Insn('TASK_GET', 3))), Insn('END')]), [
					Insn('FLAG_SET', Flag(4)),
					Insn('0x4B', Char(9), -1),
					Insn('CALL', Function((1, 9))),
					Insn('0x4C', Char(9), -1),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]
