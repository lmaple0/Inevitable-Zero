# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't0520',
	'name2': 't0520',
	'location': 63,
	'bgm': 121,
	'flags': 8192,
	'includes': [
		't0520',
		't0520_1',
		None,
		None,
		None,
		None,
	],
	'name3': 't0520',
	'labels': [],
	'chcp': [
		'chr/ch23500',
		'chr/ch25700',
		'chr/ch00000',
		'chr/ch00000',
		'apl/ch50130',
		'chr/ch33300',
		'chr/ch34500',
		'chr/ch00602',
		'chr/ch00702',
		'chr/ch27202',
		'chr/ch27302',
		'chr/ch00000',
		'chr/ch24402',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
	],
	'npcs': [
		{
			'name': Translate('诺玛'),
			'pos': (3700, 0, 4289),
			'angle': 180,
			'_1': b'\x05\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((0, 5)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('琉卡'),
			'pos': (-4880, -750, -860),
			'angle': 270,
			'_1': b'\x05\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 6)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('矿工罗基'),
			'pos': (147360, 500, 4599),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x04\x00\xff\xff',
			'function': Function((0, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('弗里吉亚'),
			'pos': (204809, 0, 560),
			'angle': 270,
			'_1': b'\x05\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 8)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('莱缇娜'),
			'pos': (203350, 0, 560),
			'angle': 90,
			'_1': b'\x05\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((0, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('艾丝蒂尔'),
			'pos': (-7530, -600, -3140),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\x07\x00\xff\xff',
			'function': Function((0, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('约书亚'),
			'pos': (-8640, -600, -4380),
			'angle': 0,
			'_1': b'\xd5\x01\x00\x00\x08\x00\xff\xff',
			'function': Function((0, 12)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游击士斯克特'),
			'pos': (-6199, -600, 4199),
			'angle': 270,
			'_1': b'\xd5\x01\x00\x00\t\x00\xff\xff',
			'function': Function((0, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游击士温蔡尔'),
			'pos': (-9289, -600, 3869),
			'angle': 90,
			'_1': b'\xd5\x01\x00\x00\n\x00\xff\xff',
			'function': Function((0, 14)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客沃伦斯'),
			'pos': (-9510, -600, -1200),
			'angle': 180,
			'_1': b'\x95\x01\x00\x00\x0c\x00\xff\xff',
			'function': Function((0, 15)),
			'_2': b'\xff\x00\x00\x00',
		},
	],
	'monsters': [],
	'triggers': [],
	'objects': [
		{
			'pos': (3700, 0, 2920),
			'range': 1000,
			'bubble_pos': (3700, 1500, 4290),
			'_1': b'~\x00\x00',
			'function': Function((0, 4)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00?\x00', Function((0, 2)), Function((0, 3))),
	'code': [None]*24,
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
		Insn('CHAR_IDLE', Char(254), (202360, -230), (205240, 990), 1000),
		Insn('SLEEP', 300),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_FLAG1_SET', Char(12), 128),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_FLAG1_SET', Char(12), 128),
		]),
		(Expr([Insn('FLAG', Flag(1547)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_FLAG1_SET', Char(12), 128),
		]),
		(Expr([Insn('FLAG', Flag(1544)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_FLAG1_SET', Char(12), 128),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(11), 128),
			Insn('CHAR_FLAG1_SET', Char(12), 128),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(11), (204010, 0, 560), 270),
			Insn('FORK_FUNC', Char(11), 0, Function((0, 1))),
			Insn('CHAR_SET_POS', Char(12), (199530, 0, 3160), 225),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(11), (204010, 0, 560), 270),
			Insn('FORK_FUNC', Char(11), 0, Function((0, 1))),
			Insn('CHAR_SET_POS', Char(12), (199530, 0, 3160), 225),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(11), (204010, 0, 560), 270),
			Insn('FORK_FUNC', Char(11), 0, Function((0, 1))),
			Insn('CHAR_SET_POS', Char(12), (199530, 0, 3160), 225),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_SET_POS', Char(11), (204010, 0, 560), 270),
			Insn('FORK_FUNC', Char(11), 0, Function((0, 1))),
			Insn('CHAR_SET_POS', Char(12), (199530, 0, 3160), 225),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
					Insn('CHAR_SET_POS', Char(9), (10680, 0, -830), 90),
					Insn('CHAR_FLAG1_UNSET', Char(13), 128),
					Insn('CHAR_FLAG1_UNSET', Char(14), 128),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(11), (204010, 0, 560), 270),
			Insn('FORK_FUNC', Char(11), 0, Function((0, 1))),
			Insn('CHAR_SET_POS', Char(12), (199530, 0, 3160), 225),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
		]),
		(Expr([Insn('FLAG', Flag(813)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(812)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), []),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1280)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('EXPR_CHAR_ATTR', Char(10), 51, Expr([Insn('CONST', 1200), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(812)), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xd2\xc8\x00\x00\x00\x00\x00'),
		]),
		(Expr([Insn('FLAG', Flag(1547)), Insn('FLAG', Flag(1548)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xd2\xc8\x00\x00\x00\x00\x00'),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('CALL', Function((0, 5))),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(812)), Insn('FLAG', Flag(813)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 17))),
		]),
		(None, [
			Insn('TEXT_START', Char(8)),
			Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('EQ'), Insn('END')], [
				Insn('FADE_ON', 300, Color(0x00000000), 100),
				Insn('MENU', 0, -1, -1, 1, Text(
					'对话\n'
					'购物\n'
					'休息\n'
					'放弃\n'
				)),
				Insn('MENU_WAIT', 0),
				Insn('IF', [
					(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('LT'), Insn('VAR', 0), Insn('CONST', 2), Insn('GT'), Insn('OR'), Insn('END')]), [
						Insn('0x60', 0),
						Insn('FADE_OFF', 300, Color(0x00000000)),
						Insn('0x0D'),
					]),
					(None, []),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
						Insn('OPEN_SHOP', 82),
						Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
					]),
					(Expr([Insn('VAR', 0), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
						Insn('OPEN_SHOP', 80),
						Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
					]),
					(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), []),
					(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
						Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('QUEST_GET', 54, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 54, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 54, Insn('FLAG_GET', 2))), Insn('BOOL_AND'), Insn('END')]), [
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('QUEST_GET', 54, Insn('FLAG_GET', 16))), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('FLAG', Flag(0)), Insn('END')]), [
												Insn('IF', [
													(Expr([Insn('FLAG', Flag(1547)), Insn('END')]), [
														Insn('CALL', Function((0, 20))),
													]),
													(Expr([Insn('FLAG', Flag(1544)), Insn('END')]), [
														Insn('CALL', Function((0, 19))),
													]),
													(None, [
														Insn('CALL', Function((0, 18))),
													]),
												]),
											]),
											(None, [
												Insn('CALL', Function((1, 11))),
												Insn('FLAG_SET', Flag(0)),
											]),
										]),
									]),
									(Expr([Insn('EXEC', Insn('QUEST_GET', 54, Insn('TASK_GET', 1))), Insn('END')]), [
										Insn('CALL', Function((1, 10))),
									]),
									(None, [
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('QUEST_GET', 54, Insn('TASK_GET', 0))), Insn('END')]), [
												Insn('CALL', Function((1, 14))),
											]),
											(None, [
												Insn('QUEST', 54, Insn('TASK_SET', 0)),
												Insn('CALL', Function((1, 0))),
											]),
										]),
										Insn('CALL', Function((1, 1))),
										Insn('CHAR_SET_POS', Char(0), (3500, 0, 1900), 0),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
												Insn('CHAR_FLAG1_SET', Char(4), 128),
												Insn('CHAR_FLAG2_SET', Char(4), 32768),
											]),
											(None, []),
										]),
										Insn('EVENT_END', 5),
									]),
								]),
							]),
							(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'冈兹先生失踪的原因，\n'
									'以及镇长还没回来的理由……\n'
									'我们直到现在都还一无所知。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'唉，好担心啊……{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'我当时看到了\n'
									'正打算上巴士的镇长，\n'
									'他的表情似乎很阴沉呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'冈兹先生出了什么事吗？{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(Expr([Insn('FLAG', Flag(1547)), Insn('END')]), [
								Insn('CALL', Function((0, 20))),
							]),
							(Expr([Insn('FLAG', Flag(1544)), Insn('END')]), [
								Insn('CALL', Function((0, 19))),
							]),
							(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
								Insn('CALL', Function((0, 18))),
							]),
							(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
										Insn('TEXT_TALK', Char(8), Text(
											'我们这里的酒\n'
											'都是从一位名叫哈罗德\n'
											'的商人那里进的货哦。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'他穿得那么体面，\n'
											'拿来的酒果然\n'
											'也都是好酒。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'麦酒最近差不多\n'
											'都快被矿工们喝光了……\n'
											'他下次再来的时候，得再订一些货呢。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('FLAG_SET', Flag(0)),
									]),
									(None, [
										Insn('TEXT_TALK', Char(8), Text(
											'哈罗德先生卖给我们的酒\n'
											'大多都是好酒呢。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'对我们来说，真是必不可少的。{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
								]),
							]),
							(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
										Insn('TEXT_TALK', Char(8), Text(
											'女招待琉卡总是\n'
											'一脸不高兴的样子。\n'
											'只会说些刻薄的话呢。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'……下次要不要给她灌点酒呢。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'那孩子的酒量非常非常小，\n'
											'喝醉时的表情特别好玩哦。{wait}'
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
										Insn('TEXT_TALK', Char(258), Text(
											'#0106F这算不算轻度犯罪啊……{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('FLAG_SET', Flag(0)),
									]),
									(None, [
										Insn('TEXT_TALK', Char(8), Text(
											'……下次要不要给琉卡灌点酒呢。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'那孩子的酒量非常非常小，\n'
											'喝醉时的表情特别好玩哦。{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
								]),
							]),
							(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'毕竟是创立７０周年嘛。\n'
									'今年的游客比去年多了不少，\n'
									'真是太好了。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'纪念庆典期间，矿工们都去市里玩了，\n'
									'酒馆完全赚不到钱呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
										Insn('TEXT_TALK', Char(8), Text(
											'昨天，全体矿工在这开了个宴会。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'虽然很忙碌，\n'
											'但能让他们那么开心，\n'
											'就算是酒馆最大的幸福了。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('FLAG_SET', Flag(0)),
									]),
									(None, [
										Insn('TEXT_TALK', Char(8), Text(
											'说起来，矿工罗基\n'
											'完全醉倒了呢。\n'
											'没办法，只好让他在店里睡下了。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'真是的，年纪轻轻，\n'
											'竟然这么没出息呢。{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
								]),
							]),
							(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
								Insn('TEXT_TALK', Char(8), Text(
									'今天来的客人好像很年轻，\n'
									'但听说是游击士呢。{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('TEXT_TALK', Char(8), Text(
									'……气氛好像很沉重，\n'
									'是出了什么事吗？{wait}'
								)),
								Insn('TEXT_WAIT'),
							]),
							(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
										Insn('TEXT_TALK', Char(8), Text(
											'这家店在白天\n'
											'还真是闲啊。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'……好吧，反正也很闲，\n'
											'就告诉你们一个秘密吧。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'女招待琉卡\n'
											'虽然总是一脸不高兴的表情……{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'但笑起来时可是超级可爱的。\n'
											'我要是男人的话，\n'
											'一定会迷上她哦。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('FLAG_SET', Flag(0)),
									]),
									(None, [
										Insn('TEXT_TALK', Char(8), Text(
											'琉卡虽然总是一脸不高兴的样子，\n'
											'但笑容可是超级可爱的哦。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'不过她很少露出\n'
											'那种笑容，\n'
											'还真是很可惜呢。{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
								]),
							]),
							(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
										Insn('TEXT_TALK', Char(8), Text(
											'魔兽骚动平息了，\n'
											'我们镇子也恢复了平静。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'虽然矿工们\n'
											'老是抱怨什么『不能提早回家了』\n'
											'之类的胡话。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'总而言之，\n'
											'不会再遭遇危险，\n'
											'真是太好了。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('FLAG_SET', Flag(0)),
									]),
									(None, [
										Insn('TEXT_TALK', Char(8), Text(
											'魔兽骚动平息了，\n'
											'矿工和镇上的人\n'
											'也不会再受到袭击了。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'这都多亏了你们，\n'
											'真是太谢谢了。{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
								]),
							]),
							(Expr([Insn('FLAG', Flag(812)), Insn('END')]), [
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
										Insn('TEXT_TALK', Char(8), Text(
											'嗯，要出门吗？{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'最近镇上有些不太平静，\n'
											'所以最好早点回来哦。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('FLAG_SET', Flag(0)),
									]),
									(None, [
										Insn('TEXT_TALK', Char(8), Text(
											'要不就来喝点酒，\n'
											'暖暖身子吧？{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'……虽然已经满座了。{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
								]),
							]),
							(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(820)), Insn('NOT'), Insn('END')]), [
										Insn('FLAG_SET', Flag(820)),
										Insn('0xD0', 2, Expr([Insn('0x23', 2), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
										Insn('TEXT_TALK', Char(8), Text(
											'哎呀，你们看上去很面生呢。\n'
											'是从克洛斯贝尔市来的吗？{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'话说回来，\n'
											'你们来的时机真是不巧啊。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'最近有狼型魔兽\n'
											'在这一带肆虐呢。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'不久前，我们这里的粮仓也被破坏了。\n'
											'真是的，太可恶了。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('FLAG_SET', Flag(0)),
									]),
									(None, [
										Insn('TEXT_TALK', Char(8), Text(
											'对了对了，\n'
											'不嫌弃的话，要不要吃点什么？{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'要是想好好休息一下的话，\n'
											'最好趁现在休息哦。{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_TALK', Char(8), Text(
											'到了晚上，\n'
											'收工回来的矿工们\n'
											'就会把席位都占满的。{wait}'
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
			Insn('TEXT_END', Char(8)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 54, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 54, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 54, Insn('FLAG_GET', 2))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 54, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('CALL', Function((1, 12))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 54, Insn('TASK_GET', 1))), Insn('END')]), [
					Insn('CALL', Function((1, 3))),
				]),
				(Expr([Insn('FLAG', Flag(1547)), Insn('END')]), [
					Insn('CALL', Function((0, 23))),
				]),
				(Expr([Insn('FLAG', Flag(1544)), Insn('END')]), [
					Insn('CALL', Function((0, 22))),
				]),
				(None, [
					Insn('CALL', Function((0, 21))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我感觉冈兹先生失踪\n'
				'事件的背后……\n'
				'隐藏着巨大的谜团。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……是悬疑小说\n'
				'看多了吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'既然找到冈兹先生了……\n'
				'很可能会再开一场庆祝宴会吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'唉……收拾残局又会很辛苦呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1547)), Insn('END')]), [
			Insn('CALL', Function((0, 23))),
		]),
		(Expr([Insn('FLAG', Flag(1544)), Insn('END')]), [
			Insn('CALL', Function((0, 22))),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('CALL', Function((0, 21))),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'纪念庆典在今天就要结束了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'游客们也许要走了，\n'
				'不过矿工们也该回来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'唉唉～好忙好忙。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'算啦，虽然有点忙……\n'
				'不过，你们要不要也喝点什么？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……但就算你们因此搞砸了工作，我也不负责哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'在举办纪念庆典的时候\n'
				'特地跑到这种冷清之地的\n'
				'游客吗……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……不过，心情也可以理解吧。\n'
				'我也很讨厌人山人海。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'真是的，每天都快累死了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……酒这种东西，到底好在哪里啊？\n'
						'我完全不能喝酒，所以真是不明白它有什么吸引人的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F以、以酒馆女招待的身份来说，\n'
						'这种发言还真是意外呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'你好烦啊，客人。\n'
						'这是我的自由吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'真是的，酒这种东西，到底好在哪里啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……之前因为好奇而喝了一点，\n'
						'但现在已经完全不记得当时的情况了，\n'
						'所以真不明白酒这东西有什么吸引人的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……干什么啊，\n'
						'不要一直盯着人家看啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'要点菜就去找老板娘。\n'
						'我只管送菜。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……完毕。\n'
						'听明白的话，\n'
						'就别再烦我了好吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'每天晚上都要应付\n'
						'喝醉的矿工，累死人了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'别再烦我了好吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'呼啊……\n'
						'啊～真是的，好困好困。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'矿工们收工回来\n'
						'就会开宴会，\n'
						'所以我和老板娘都睡眠不足。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真是的，\n'
						'那个『击退魔兽纪念宴会』\n'
						'到底要开到什么时候啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'那些矿工们，直到现在，\n'
						'每天晚上还都要开什么\n'
						'『击退魔兽纪念宴会』。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'只不过就是想找个借口\n'
						'喝酒而已吧。\n'
						'真是的……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(813)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(812)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我擦我擦……\n'
						'好，这样就没问题了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，接下来会很忙……\n'
						'稍微休息一下吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，接下来会很忙……\n'
						'稍微休息一下吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(821)), Insn('NOT'), Insn('END')]), [
					Insn('FLAG_SET', Flag(821)),
					Insn('0xD0', 2, Expr([Insn('0x23', 2), Insn('CONST', 1), Insn('ADD'), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……欢迎光临，\n'
						'要点菜的话请去柜台。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……怎么了，\n'
						'找我有什么事吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'想点菜的话，能不能去柜台？\n'
						'我正忙着为晚场做准备呢。{wait}'
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

data['code'][7] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呕…………\n'
				'已经……喝不下了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'让、让我一个人待着…………{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(2)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'让、让我一个人待着…………{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵呵！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'终于、终于……\n'
						'我终于成功收购到\n'
						'七耀石的结晶了！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'而且还是\n'
						'这么大的红耀石……\n'
						'我还是第一次见呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，这样应该就能向\n'
						'身在帝国的父亲提交令他满意的报告了！\n'
						'距离大商人的目标又迈进了一步啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'竟然能开采到\n'
						'这么大的红耀石……\n'
						'不愧是七耀石的产地呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，似乎能向身在帝国的父亲\n'
						'提交令他满意的报告了呢！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我今晚要去镇长家\n'
				'进行收购七耀石的交涉。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'在弄到手之前……\n'
				'我绝对不会放弃的！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我为了收购到\n'
						'七耀石的结晶，\n'
						'从之前开始就一直与镇长交涉……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'可是那个镇长也很难对付呢，\n'
						'怎么都不肯说ＹＥＳ。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不，我可不能\n'
						'一直消沉下去。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'父亲是大商人，而我是继承他血脉的人，\n'
						'一定要将它弄到手，对此我志在必得！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'既然决定了，\n'
						'就必须要好好考虑交涉的手段了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'首先要将收购价\n'
						'下狠心提高……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呜呜……一楼昨天好吵，\n'
				'害得我都没睡着。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'好困啊……\n'
				'今天要好好睡一觉。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我想在玛因兹\n'
						'收购的七耀石结晶\n'
						'是相当贵重的物品。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，据说开采量很少，\n'
						'如果运气不好\n'
						'就肯定买不到呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'昨天的交涉结果很令人遗憾，\n'
						'是我被拒绝了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……没关系，\n'
						'我准备了很充足的滞留资金，\n'
						'一定要坚持到最后一刻！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'滞留资金我多得是，\n'
						'为了照顾我兼供我消遣，\n'
						'还带了莱缇娜来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵呵，\n'
						'直到买到结晶为止，\n'
						'我一定不会放弃交涉的！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'贵重的七耀石结晶……\n'
						'我就是想买这个，\n'
						'才会一直留在这里的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'结晶可不是像魔兽掉落的\n'
						'耀晶石那样的小东西。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'每一块都蕴藏着妖艳的光辉，\n'
						'帝国的贵族阶层\n'
						'都将它用来做首饰的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'如果能顺利收购，带回帝国的话，\n'
						'一定可以卖到很高的价钱呢。\n'
						'呵呵呵……！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'七耀石的结晶\n'
						'可不是魔兽掉落的\n'
						'那种小小的耀晶石哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'如果能顺利收购，带回帝国的话，\n'
						'一定可以卖到很高的价钱呢。\n'
						'呵呵呵……！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(813)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(812)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 10))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'差不多快到矿工们\n'
						'回来的时候了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'要是还像昨天那样\n'
						'大吵大嚷的，\n'
						'可没法吃饭呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 10))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'哎呀……你们\n'
						'也是来收购七耀石的吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵～！\n'
						'你们的交涉手腕\n'
						'能赢过我吗！？{wait}'
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

data['code'][9] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'小姐买到了七耀石结晶……\n'
						'唉……太久了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然确实是非常不错的商品……\n'
						'但是用了将近四个月的滞留费，\n'
						'她真的明白这一点吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'…………\n'
						'还是不要想太多为好吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……总而言之，\n'
						'这下总算能回帝国了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'离家出走了将近四个月，\n'
						'家中现在怎么样了呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'（小姐只要\n'
						'\u3000一说到交易的事，\n'
						'\u3000就变得这么认真……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'（结、结果到底会怎样呢……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'（紧张紧张……\n'
						'\u3000今晚的交易，\n'
						'\u3000结果到底会怎样呢……）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'小姐凭借她特有的强硬态度\n'
				'和雄厚的资金在进行交涉……\n'
				'但似乎还是很困难呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……真是的，既然都走到这一步，就已经没有退路了。\n'
				'希望小姐\n'
				'能努力到最后一步！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'昨天矿工们开宴会\n'
						'好像开到很晚。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……我也一直努力\n'
						'想让小姐睡着，熬到很晚，\n'
						'真是好辛苦……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'镇长先生今天似乎也很累……\n'
						'收购的交涉只好暂缓了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……要到什么时候\n'
						'才能回帝国呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'小姐的滞留资金……\n'
						'好像是从家中的金库里\n'
						'偷偷拿出来的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'在这里待上一年都绰绰有余……\n'
						'小姐是这样说的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呜呜，她到底\n'
						'偷拿了多少米拉啊……！？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'可以供我们在此滞留一年的米拉，\n'
						'外加两张往返列车票……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呜呜，家里现在\n'
						'大概已经闹翻天了吧……！？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'小姐是埃雷波尼亚帝国中\n'
						'屈指可数的大商人的独生女。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'她希望自己将来\n'
						'也能成为一个厉害的女商人，\n'
						'所以就把我拖来这个自治州……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'唉，瞒着老爷离家出走，\n'
						'回去以后一定会被\n'
						'骂死的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'总之，再不快点回去的话，\n'
						'我百分之百会被解雇的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真希望能早点将七耀石的结晶\n'
						'弄到手呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(813)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(812)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 10))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呜呜……\n'
						'得去取晚餐才行了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我笨手笨脚的……\n'
						'真担心会不会\n'
						'从楼梯上滚下来……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 10))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'小姐和我\n'
						'是从帝国来这里\n'
						'收购七耀石的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'可是，听说最近镇子周边\n'
						'有魔兽出没，\n'
						'真有点害怕呢……{wait}'
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

data['code'][10] = [
	Insn('0x4B', Char(11), -1),
	Insn('0x4B', Char(12), -1),
	Insn('CHAR_WATCH', Char(11), Char(12), 0),
	Insn('CHAR_WATCH', Char(12), Char(11), 0),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(812)), Insn('END')]), [
			Insn('TEXT_TALK', Char(11), Text(
				'哎呀，都这么晚了啊。\n'
				'肚子饿了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'莱缇娜，你去老板娘那里\n'
				'拿晚餐来吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'那、那个……\n'
				'直接去上面的餐桌\n'
				'吃不好吗……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'不好，太麻烦。\n'
				'好啦，你快去。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'呜呜……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(11), Text(
				'呵呵～\n'
				'不愧是大陆首屈一指的\n'
				'七耀石产地呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'是、是呀，小姐。\n'
				'昨天也和比克森镇长\n'
				'做了笔成功的交易……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'看这样子，\n'
				'购买到七耀石的结晶\n'
				'也只是时间问题了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'嗯，虽然之前有点犹豫，\n'
				'但我决定暂时留在这里了！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('0x4C', Char(11), -1),
	Insn('0x4C', Char(12), -1),
	Insn('FLAG_SET', Flag(3)),
	Insn('FLAG_SET', Flag(4)),
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
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1188)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 16))),
				]),
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'#0805F啊、罗伊德，是你们……{wait}'
						'{page}'
						'#0809F啊哈哈……\n'
						'我完全没注意到。\n'
						'你们来工作吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0002F啊，是的，\n'
						'差不多吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0108F（艾丝蒂尔……\n'
						'\u3000似乎在强颜欢笑呢。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0303F（嗯……\n'
						'\u3000的确有点令人在意……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0208F（……这是困惑……？\n'
						'\u3000还是深沉的哀伤……？）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'#0809F好、好了～！\n'
						'稍微休息一下，就要赶快回市里啦！{wait}'
						'{page}'
						'#0802F罗伊德，你们也要加油哦！{wait}'
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

data['code'][12] = [
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
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1188)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((0, 16))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(14), Text(
						'#0903F（抱歉，发生了一些事……）{wait}'
						'{page}'
						'#0900F（现在能不能让艾丝蒂尔\n'
						'\u3000一个人静一静呢？）{wait}'
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

data['code'][13] = [
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
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#08400F警察局的孩子们吗，\n'
						'辛苦了。{wait}'
						'{page}'
						'#08402F那些黑手党的事\n'
						'好像已经立案了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F……是鲁巴彻吧。\n'
						'但只过了两天就被释放了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#08409F哈哈，别那么沮丧啦。{wait}'
						'{page}'
						'#08400F就算是游击士，\n'
						'也会经常碰到这种事的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#08400F自从那次的魔兽事件以来，\n'
						'我们在解决各地委托的时候，\n'
						'都会顺便巡视一下。{wait}'
						'{page}'
						'#08403F虽然更加忙碌了……\n'
						'不过，这也是必要的。{wait}'
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

data['code'][14] = [
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
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#08500F那起事件的解决……\n'
						'就你们一贯的实力来说，算是干得漂亮了。{wait}'
						'{page}'
						'#08504F不过，可不要骄傲哦。\n'
						'要经常保持上进心，\n'
						'不断进取。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F（好像稍微\n'
						'\u3000认可我们了吧……？）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#08503F成功往往会招致骄傲。\n'
						'要是沉溺于自满中，\n'
						'就无法获得下一次的成功。{wait}'
						'{page}'
						'#08500F要经常保持上进心，\n'
						'不断进取。{wait}'
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

data['code'][15] = [
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
		(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'（唠唠叨叨）……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呼……\n'
				'大白天的就一个人来酒馆，\n'
				'真是太奢侈啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过，只是喝杯冰茶而已啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(8)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'（咕嘟咕嘟）……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呼～好喝～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CHAR_SET_FRAME', Char(13), 0),
	Insn('CHAR_SET_FRAME', Char(14), 0),
	Insn('CAM_OFFSET', (-8200, 750, -3800), 0),
	Insn('CAM_ROTATE', 55, 30, 0, 0),
	Insn('0x6E', 260, 0),
	Insn('CAM_DISTANCE', 30000, 0),
	Insn('CHAR_SET_POS', Char(257), (-6100, -750, -4050), 270),
	Insn('CHAR_SET_POS', Char(258), (-5950, -750, -5050), 270),
	Insn('CHAR_SET_POS', Char(259), (-5100, -750, -4050), 270),
	Insn('CHAR_SET_POS', Char(260), (-4950, -750, -5050), 270),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(13), Text(
		'#0808F#11P…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0906F#12P看来，和我们调查的一样，\n'
		'是一位相当正派的人呢。{wait}'
		'{page}'
		'#0908F那孩子果然是误会了……\n'
		'不，或许是钻进牛角尖了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#0808F#11P……我明白……\n'
		'那并不是那个人的错。{wait}'
		'{page}'
		'当然，也绝对不是\n'
		'那孩子的错……{wait}'
		'{page}'
		'#0811F那个，约书亚……\n'
		'我们……该怎么办才好？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(14), Text(
		'#0903F#12P……冷静点，艾丝蒂尔。\n'
		'这并不是能够简单解决的问题。{wait}'
		'{page}'
		'#0900F不要焦躁，要踏踏实实地努力尝试，\n'
		'关于这点，在来之前不是就已经决定了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'#0806F#11P……嗯。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0001F#11P（好像在谈什么\n'
		'\u3000严肃的话题啊……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_POS', Char(0), (-6100, -750, -4550), 270),
	Insn('FLAG_SET', Flag(1188)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('EVENT_BEGIN', 0),
	Insn('0x4B', Char(8), -1),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (3040, 1500, 1600), 0),
	Insn('CAM_ROTATE', 30, 19, 0, 0),
	Insn('0x6E', 260, 0),
	Insn('CAM_DISTANCE', 34000, 0),
	Insn('CHAR_SET_POS', Char(257), (2900, 0, 1900), 0),
	Insn('CHAR_SET_POS', Char(258), (4100, 0, 1900), 0),
	Insn('CHAR_SET_POS', Char(259), (2900, 0, 700), 0),
	Insn('CHAR_SET_POS', Char(260), (4100, 0, 700), 0),
	Insn('0x0D'),
	Insn('EMOTE', Char(8), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200611V#1P呀，你们几个……\n'
		'都已经是傍晚了哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200612V#1P巴士的末班车是在八点左右，\n'
		'不用去赶车吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200613V#0100F#2P没关系……我们今天\n'
		'打算在这里住下。{wait}'
		'{page}'
		'#11200614V请问，还有带着桌子\n'
		'的大房间空着吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200615V#1P嗯，有啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200616V#1P呵呵，好开心啊。\n'
		'像你们这样的年轻人\n'
		'也会住我们这里。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200617V#1P晚餐也在我们这里吃吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200618V#0000F#2P嗯，麻烦您了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200619V#1P好啊，那就让我大展身手，\n'
		'给你们做点好吃的吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11200620V#1P房间在下楼之后左手边的最里面。\n'
		'吃晚饭之前，先去休息休息吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200621V#0300F#4P谢啦，阿姨。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200622V#0200F#4P……打扰了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 516), Insn('SET'), Insn('END')])),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 't052b', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('TEXT_TALK', Char(8), Text(
		'感觉最近总是提不起劲呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'是不是因为喝酒最豪爽\n'
		'的那位没来呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('TEXT_TALK', Char(8), Text(
		'你们看起来好像很累啊，\n'
		'要不要住宿呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('TEXT_TALK', Char(8), Text(
		'几个月前的魔兽骚动也好，\n'
		'这次的矿工失踪也罢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'总觉得在短短时间内\n'
		'发生了好多事啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'希望这不是什么\n'
		'坏事即将发生的征兆……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'好了～要趁客人不在时快点打扫才行。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'话说回来，最近好像\n'
				'都不怎么开宴会了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'最近一直没什么宴会，\n'
				'所以打扫很轻松呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('TEXT_TALK', Char(254), Text(
		'嗯，打扫得差不多了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'只是少了冈兹先生一个人，\n'
		'打扫就变得简单多了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('TEXT_TALK', Char(254), Text(
		'冈兹先生好像真的\n'
		'很不擅长赌博呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'在这里喝醉的时候，\n'
		'大概都是在抱怨输钱。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]
