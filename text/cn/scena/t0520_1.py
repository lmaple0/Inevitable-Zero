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
		None,
		None,
		None,
		None,
		None,
		None,
	],
	'name3': 't0520_1',
	'labels': [],
	'chcp': [],
	'npcs': [],
	'monsters': [],
	'triggers': [],
	'objects': [],
	'unk13': b'\x00\xff\xff',
	'extra': None,
	'code': [None]*23,
	'anim': [],
}

data['code'][0] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CALL', Function((1, 15))),
	Insn('TEXT_TALK', Char(8), Text(
		'#1P哦，来了来了！\n'
		'真是的，我已经等到不耐烦了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0011F#2P不、不好意思。\n'
		'那么，关于委托的事……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#1P嗯，是有关露卡的事。\n'
		'她是在这里工作的服务生。\n'
		'你们应该也有看过她吧？{wait}'
		'{page}'
		'那孩子态度很冷淡呢。\n'
		'不过，这间店几乎都是常客，\n'
		'所以是没有问题……{wait}'
		'{page}'
		'但是，她笑起来超可爱的。\n'
		'这不是很可惜吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0305F#4P你说她……超可爱！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#1P是啊。如果我是男人的话，\n'
		'绝对会爱上她。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0307F#4P#5S真的假的！？{wait}'
		'{page}'
		'#0304F#3S……罗伊德，看来这个工作\n'
		'我们只能接下了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0106F#2P（一知道是可爱的女孩，\n'
		'\u3000马上就变成这样……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0206F#4P（兰迪真现实。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0012F#2P呃……那么，具体来说，\n'
		'你希望我们怎么做呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#1P很简单。\n'
		'只要让那孩子笑就可以了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0001F#2P让她笑吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F#2P听起来好像\n'
		'很简单，可是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#1P那孩子如果可以\n'
		'多点笑容待客的话，\n'
		'我想店里的业绩也会上升。{wait}'
		'{page}'
		'你们愿意接下这个委托吗？\n'
		'为了让本店生意兴隆，拜托你们了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][1] = [
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, -1, 0, Text(
		'【接受】\n'
		'【放弃】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#2P#0006F不好意思，我们现在工作\n'
				'有点忙不过来……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#1P什么嘛，是这样啊。\n'
				'那就没办法了……{wait}'
				'{page}'
				'等你们有空的时候，\n'
				'再来承接委托吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('CALL', Function((1, 2))),
		]),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('QUEST', 54, Insn('TASK_SET', 1)),
	Insn('FLAG_UNSET', Flag(1)),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F我知道了。我们接受这分委托。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#1P就是要这样才对。\n'
		'如果能顺利完成，\n'
		'我会好好答谢你们。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0309F#4P那就拜托你了，大婶。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F#2P但是，我们要怎么\n'
		'让她笑出来呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F#4P那太简单了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F#2P你有什么好主意吗？\n'
		'兰迪。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0304F#4P嗯！我去搭讪那女孩，\n'
		'把她迷得晕头转向！\n'
		'怎样？这个战术很完美吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(8), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
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
	Insn('TEXT_TALK', Char(259), Text(
		'#0211F#2P我觉得你脑袋有问题……{wait}'
		'{page}'
		'#0203F我的点子很老套，不过，\n'
		'如果送对方喜欢的礼物的话，\n'
		'这个办法如何？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0102F#2P我觉得这是个好方法。\n'
		'收到喜欢的东西，\n'
		'我想没有人会不高兴吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0301F#4P我还是觉得我去搭讪\n'
		'应该比较快……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0012F#2P总之，各种方法都试试看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 80, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'开始进行{color 2}任务【店员的待客指导】{color 0}！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('VITA_C7', b'\x02\x01')), Insn('CONST', 1510), Insn('EQ'), Insn('EXEC', Insn('VITA_C7', b'\x02\x02')), Insn('CONST', 1610), Insn('EQ'), Insn('BOOL_AND'), Insn('EXEC', Insn('VITA_C7', b'\x02\x03')), Insn('CONST', 83), Insn('EQ'), Insn('EXEC', Insn('VITA_C7', b'\x02\x04')), Insn('CONST', 84), Insn('EQ'), Insn('BOOL_AND'), Insn('EXEC', Insn('VITA_C7', b'\x02\x03')), Insn('CONST', 84), Insn('EQ'), Insn('EXEC', Insn('VITA_C7', b'\x02\x04')), Insn('CONST', 83), Insn('EQ'), Insn('BOOL_AND'), Insn('OR'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((1, 9))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'……欢迎光临。\n'
				'要点餐请到柜台。{wait}'
				'{page}'
				'……怎么？\n'
				'你们找我有事吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EXPR_VAR', 2, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('EQ'), Insn('END')], [
				Insn('FADE_ON', 300, Color(0x00000000), 100),
				Insn('MENU', 0, -1, -1, 1, Text(
					'【交付道具】\n'
					'【搭讪】\n'
					'【放弃】\n'
				)),
				Insn('MENU_WAIT', 0),
				Insn('0x60', 0),
				Insn('FADE_OFF', 300, Color(0x00000000)),
				Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
					0: [
						Insn('CALL', Function((1, 16))),
						Insn('IF', [
							(Expr([Insn('VAR', 2), Insn('CONST', 0), Insn('NE'), Insn('END')]), [
								Insn('EXPR_VAR', 0, Expr([Insn('CONST', 255), Insn('SET'), Insn('END')])),
							]),
							(None, [
								Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
							]),
						]),
						Insn('BREAK'),
					],
					1: [
						Insn('CALL', Function((1, 7))),
						Insn('BREAK'),
					],
					None: [
						Insn('CALL', Function((1, 4))),
						Insn('BREAK'),
					],
				}),
			]),
		]),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('TEXT_TALK', Char(254), Text(
		'没事的话，可以不要找我说话吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F呃……我想送你这个。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'……这是什么？\n'
		'收到这种东西，\n'
		'我也只会觉得困扰而已。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F（这个礼物似乎没有效果……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('BGM_PLAY', b'\x04\x02\x00'),
	Insn('QUEST', 54, Insn('TASK_SET', 5)),
	Insn('EVENT_BEGIN', 0),
	Insn('0x4B', Char(9), -1),
	Insn('0x4B', Char(8), -1),
	Insn('CHAR_ROTATE', Char(254), 270, 800),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (1120, 1500, 970), 0),
	Insn('CAM_ROTATE', 41, 6, 0, 0),
	Insn('0x6E', 360, 0),
	Insn('CAM_DISTANCE', 13000, 0),
	Insn('CHAR_SET_POS', Char(257), (-6560, -750, -250), 90),
	Insn('CHAR_SET_POS', Char(258), (-6560, -750, -1250), 90),
	Insn('CHAR_SET_POS', Char(259), (-7560, -750, -250), 90),
	Insn('CHAR_SET_POS', Char(260), (-7560, -750, -1250), 90),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(4), 128),
			Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
			Insn('CHAR_SET_POS', Char(265), (-7060, -750, -2250), 90),
		]),
		(None, []),
	]),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(8), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(8), 270, 500),
	Insn('SLEEP', 400),
	Insn('CAM_OFFSET', (-5720, 1500, -1440), 1400),
	Insn('CAM_ROTATE', 30, 14, 0, 1400),
	Insn('0x6E', 240, 1400),
	Insn('CAM_DISTANCE', 29000, 1400),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F呃……我想送你这个。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(254), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(254), Text(
		'#5S……！#3S{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(254), 0, 2000, (10, 11, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(254), Text(
		'好、好可爱……\n'
		'哇啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0001F（哦！感觉不错！）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'……什、什么啦，\n'
		'你打算叫我穿上这个吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0012F咦？不是的，如果当作\n'
		'礼物的话，不知道这个怎样……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(254), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'……哼。\n'
		'就算我穿上这个，\n'
		'也一点都不可爱啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(254), 89, 500),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(8), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 800),
	Insn('EMOTE', Char(8), 0, 2000, (40, 43, 100, 0)),
	Insn('CHAR_ROTATE', Char(8), 90, 1000),
	Insn('SLEEP', 400),
	Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 400),
	Insn('TEXT_TALK', Char(254), Text(
		'把它送给\n'
		'黏在你身旁的\n'
		'那些女孩比较好吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F（嗯，失败了吗……\n'
		'\u3000不过，感觉有希望呢。）{wait}'
		'{page}'
		'（该不会……\n'
		'\u3000比起自己穿可爱的东西，\n'
		'她更喜欢看别人穿吗……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 500, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x4C', Char(8), -1),
	Insn('EMOTE_STOP', Char(8)),
	Insn('CHAR_ROTATE', Char(8), 180, 1000),
	Insn('0x1F'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(4), 128),
			Insn('CHAR_FLAG2_SET', Char(4), 32768),
		]),
		(None, []),
	]),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 54, Insn('TASK_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 54, Insn('TASK_SET', 2)),
			Insn('TEXT_TALK', Char(260), Text(
				'#0309F哦！就是要这样才对！{wait}'
				'{page}'
				'#0304F要让你见识一下\n'
				'大哥我华丽的\n'
				'搭讪技巧才行呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0012F哈哈……我不会抱太大的期待哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x4B', Char(9), -1),
			Insn('BGM_PLAY', b'\x06\x02\x00'),
			Insn('EVENT_BEGIN', 0),
			Insn('CROSSFADE', 1000),
			Insn('CAM_OFFSET', (-8460, 750, 1310), 0),
			Insn('CAM_ROTATE', 90, 20, 0, 0),
			Insn('0x6E', 260, 0),
			Insn('CAM_DISTANCE', 38500, 0),
			Insn('CHAR_SET_POS', Char(254), (-8630, -750, 2960), 45),
			Insn('CHAR_SET_POS', Char(258), (-6520, -750, 1500), 270),
			Insn('CHAR_SET_POS', Char(257), (-6520, -750, 700), 270),
			Insn('CHAR_SET_POS', Char(259), (-6520, -750, -100), 270),
			Insn('CHAR_SET_POS', Char(260), (-10360, -750, 1190), 45),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(4), 128),
					Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
					Insn('CHAR_SET_POS', Char(265), (-6520, -750, -900), 270),
				]),
				(None, []),
			]),
			Insn('0x4C', Char(9), -1),
			Insn('0x0D'),
			Insn('FORK_FUNC', Char(9), 3, Function((1, 8))),
			Insn('CAM_ROTATE', 35, 23, 0, 1500),
			Insn('CAM_DISTANCE', 23000, 1500),
			Insn('0x6F', b'\x10'),
			Insn('TEXT_TALK', Char(254), Text(
				'……有事吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0312F#4P这位美丽的小姐。\n'
				'你愿意稍微停下手边的工作，\n'
				'陪我聊聊天吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……我拒绝。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0306F#4P唔……！\n'
				'居、居然这么冷淡……\n'
				'只要一下子就好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(254), 0, 2000, (8, 9, 250, 2)),
			Insn('SOUND_PLAY', 27, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(254), Text(
				'擦啊擦啊……\n'
				'很好，这样就\n'
				'把桌子擦干净了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0305F#4P唔！完全被忽视了！\n'
				'呃，喂喂──？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_QUIT', Char(9), 3),
			Insn('EMOTE', Char(254), 0, 2000, (12, 13, 250, 2)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('0x4B', Char(9), -1),
			Insn('SLEEP', 1000),
			Insn('CHAR_ROTATE', Char(254), 225, 500),
			Insn('TEXT_TALK', Char(254), Text(
				'……我说啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F#4P哦哦！你总算转过来看我了，\n'
				'这位小姐！\n'
				'你愿意听我说了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你别太死缠烂打，\n'
				'否则我会拜托常客\n'
				'把你赶出去哦。{wait}'
				'{page}'
				'本店的常客很多都是矿工，\n'
				'我想你会受到很粗鲁的对待。\n'
				'怎样？还要继续说吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_ROTATE', Char(254), 45, 500),
			Insn('0x4C', Char(9), -1),
			Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
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
			Insn('TEXT_TALK', Char(260), Text(
				'#0309F#4P…………{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0106F虽然有料到，不过……\n'
				'彻底失败了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0211F明明应该让她笑，\n'
				'结果反而让她非常生气……\n'
				'反效果也该有个程度。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('CHAR_SET_POS', Char(254), (-4880, -750, -860), 270),
			Insn('CHAR_SET_POS', Char(0), (-7190, -750, -1850), 90),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(4), 128),
					Insn('CHAR_FLAG2_SET', Char(4), 32768),
				]),
				(None, []),
			]),
			Insn('0x1F'),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_TALK', Char(260), Text(
				'#0307F只被甩个一两次就挫折的话，\n'
				'是没办法搭讪女孩的！\n'
				'我要再度挑战……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'怎么？又来搭讪吗？\n'
				'看来这次真的要请矿工他们\n'
				'把你赶出去了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0309F不、是假的！开玩笑的！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('SOUND_PLAY', 50, 0, 0, 100),
		Insn('0x96', Char(254), (-8830, -750, 3150), 2000, 0),
		Insn('SLEEP', 1000),
		Insn('SOUND_PLAY', 51, 0, 0, 100),
		Insn('0x96', Char(254), (-8630, -750, 2960), 2000, 0),
		Insn('SLEEP', 1000),
	]),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 1000),
	Insn('0x4B', Char(9), -1),
	Insn('CHAR_ROTATE', Char(254), 270, 800),
	Insn('CAM_OFFSET', (-6630, 750, -2160), 0),
	Insn('CAM_ROTATE', 45, 17, 0, 0),
	Insn('0x6E', 260, 0),
	Insn('CAM_DISTANCE', 28000, 0),
	Insn('CHAR_SET_POS', Char(257), (-5940, -750, -3340), 0),
	Insn('CHAR_SET_POS', Char(258), (-5940, -750, 1280), 180),
	Insn('CHAR_SET_POS', Char(260), (-7560, -750, -500), 90),
	Insn('CHAR_SET_POS', Char(259), (-7560, -750, -1550), 90),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(4), 128),
			Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
			Insn('CHAR_SET_POS', Char(265), (-4080, -750, 1640), 225),
		]),
		(None, []),
	]),
	Insn('CAM_DISTANCE', 24500, 1200),
	Insn('0x6F', b'\x10'),
	Insn('0x0D'),
	Insn('BGM_STOP', 500),
	Insn('EMOTE', Char(254), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CAM_ROTATE', 45, 18, 0, 400),
	Insn('CAM_DISTANCE', 15000, 400),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(254), Text(
		'#2P你、你……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_PLAY', b'\x04\x02\x00'),
	Insn('CAM_ROTATE', 45, 17, 0, 800),
	Insn('CAM_DISTANCE', 24500, 800),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0205F#3P……你说我吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'#2P你、你那身装备究竟是……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F#3P哦，这叫作\n'
		'『美喵装备』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'#2P美喵……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(254), 0, 2000, (10, 11, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(254), Text(
		'#2P好、好、好可爱……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F#4P（哦！感觉非常好！）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F#1P（你看！她的嘴角！\n'
		'\u3000已经在抖动了。\n'
		'\u3000看来她迟早会笑出来。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0101F#1P（但是……如果不再推她一把的话，\n'
		'\u3000似乎有点困难。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'#2P……呃、我说啊，\n'
		'我有一个请求……\n'
		'你愿意帮我吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F#3P请求……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'#2P呃……我希望……\n'
		'你可以说声……\n'
		'『喵喵～』……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0205F#3P……咦？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'#2P没事，我乱说的！抱歉！请你忘了吧！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(260), 180, 800),
	Insn('SLEEP', 600),
	Insn('TEXT_TALK', Char(260), Text(
		'#0307F#1P（小缇，快说！快说给她听！）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 800),
	Insn('TEXT_TALK', Char(259), Text(
		'#0211F#3P（你是认真的吗……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 315, 800),
	Insn('SLEEP', 600),
	Insn('TEXT_TALK', Char(257), Text(
		'#0001F#4P（我看她只差一点就要笑出来了。\n'
		'\u3000拜托你了，缇欧。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 2000),
	Insn('TEXT_TALK', Char(259), Text(
		'#0206F#3P……唉，真拿你们没辙。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IMG_LOAD', ResId(0), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'bu06900.itp'),
	Insn('CHAR_ROTATE', Char(260), 90, 400),
	Insn('CHAR_ROTATE', Char(257), 0, 400),
	Insn('0x95', Char(259), (-5940, -750, -1000), 3000, 0),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(259), 300, 1600, (54, 57, 250, 0)),
	Insn('SOUND_PLAY', 186, 0, 0, 100),
	Insn('CHAR_ROTATE', Char(259), 180, 600),
	Insn('CHAR_ROTATE', Char(259), 270, 600),
	Insn('CHAR_ROTATE', Char(259), 0, 600),
	Insn('CHAR_ROTATE', Char(259), 90, 600),
	Insn('CHAR_ROTATE', Char(259), 180, 600),
	Insn('CHAR_ROTATE', Char(259), 270, 600),
	Insn('CHAR_ROTATE', Char(259), 0, 600),
	Insn('CHAR_ROTATE', Char(259), 90, 600),
	Insn('EMOTE_STOP', Char(259)),
	Insn('SOUND_PLAY', 823, 0, 0, 100),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('TEXT_SET_POS', 14, 280, 35, 3),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'……喵、\n'
		'喵喵……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(0), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 0))),
	Insn('0x95', Char(259), (-7560, -750, -1550), 6000, 0),
	Insn('SLEEP', 600),
	Insn('TEXT_TALK', Char(259), Text(
		'#0208F#3P……好丢脸……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(254), 0, 2000, (24, 27, 250, 1)),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 1)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('EMOTE', Char(265), 0, 2000, (24, 27, 250, 1)),
		]),
		(None, []),
	]),
	Insn('SLEEP', 1500),
	Insn('CAM_ROTATE', 45, 18, 0, 400),
	Insn('CAM_DISTANCE', 15000, 400),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(254), Text(
		'#2P好……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_PLAY', b'\x98\x01\x00'),
	Insn('0x82', 0, 200, 3000, 800),
	Insn('0x9C', Char(9), b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x03\x00\x00\xe0.\x00\x00'),
	Insn('0x14', b'\x00\x00\x00\x00\xff\xff\xff\xbb\x00\x00\x00\x00\x01\xc8\x00\x00\x00'),
	Insn('0x15', b'`\t\x00\x00'),
	Insn('CAM_ROTATE', 45, 17, 0, 2400),
	Insn('CAM_DISTANCE', 24500, 2400),
	Insn('TEXT_TALK', Char(254), Text(
		'#5S#2P好可爱──！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(254), Text(
		'#3S#2P怎么会……怎么会这么可爱呢……！？\n'
		'啊～不行了！光是看着，\n'
		'脸上就快要露出笑容了……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0305F#1P哦哦──！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0114F#1P她笑了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0002F#4P的确……\n'
		'笑起来就判若二人，\n'
		'真的很可爱……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0309F#1P干得好啊！小缇！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F#3P…………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F#4P缇欧，你怎么了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0203F#3P该怎么说……{wait}'
		'{page}'
		'#0210F……要让别人露出笑容，\n'
		'居然会是伴随着如此强烈的\n'
		'心灵创痛的一件事……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_PLAY', b'i\x00\x00'),
	Insn('CALL', Function((1, 15))),
	Insn('TEXT_TALK', Char(8), Text(
		'#1P对吧？那孩子的笑容\n'
		'非常可爱吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0304F#4P嗯，的确。\n'
		'如果她能一直保持那个笑容的话，\n'
		'我也会为了成为这里的常客而来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#1P的确会让人这么想呢。{wait}'
		'{page}'
		'对了，那边那位小姐。\n'
		'你要不要来我们店里工作？{wait}'
		'{page}'
		'只要穿上刚才那套美喵装备，\n'
		'站在店里就好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0201F#4P……我郑重拒绝。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#1P什么嘛，真没意思。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0014F#2P啊哈哈……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#1P不过，这也没办法。\n'
		'你们依照约定让她笑出来了。{wait}'
		'{page}'
		'这是谢礼。\n'
		'请收下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'已收下５个{item 466}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 466, 5),
	Insn('TEXT_TALK', Char(257), Text(
		'#0002F#2P谢谢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#1P……喂，这位小姐，\n'
		'我会提高打工的工资，\n'
		'刚才那件事……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0201F#4P我全心全意郑重拒绝。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0012F#2P啊、啊哈哈哈……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 9, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'达成{color 2}任务【店员的待客指导】{color 0}了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('QUEST', 54, Insn('TASK_SET', 6)),
	Insn('QUEST', 54, Insn('FLAG_UNSET', 16)),
	Insn('CHAR_SET_POS', Char(0), (3500, 0, 1900), 0),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_FLAG1_SET', Char(4), 128),
			Insn('CHAR_FLAG2_SET', Char(4), 32768),
		]),
		(None, []),
	]),
	Insn('0x1F'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('QUEST', 54, Insn('TASK_SET', 3)),
	Insn('TEXT_TALK', Char(8), Text(
		'#1P那就拜托你们啰。\n'
		'只要有露卡的笑容，\n'
		'店里的业绩肯定会翻倍。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0012F#4P呃……话说回来，\n'
		'你知道露卡有可能\n'
		'喜欢什么东西吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#1P喜欢的东西？嗯……\n'
		'她这孩子很少会\n'
		'提到这些事情呢……{wait}'
		'{page}'
		'如果是我们的常客，\n'
		'说不定会知道些什么。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('TEXT_TALK', Char(8), Text(
		'#1P你们也看到了吧？\n'
		'露卡那让人陶醉的笑容！{wait}'
		'{page}'
		'哎呀～\n'
		'有缘欣赏到这么稀奇的东西，\n'
		'我真是太幸运啦。{wait}'
		'{page}'
		'……唉，只不过\n'
		'她马上就恢复成\n'
		'平常的冷淡表情了。{wait}'
		'{page}'
		'得想想其他办法才行呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
			Insn('FLAG_SET', Flag(1)),
			Insn('TEXT_TALK', Char(254), Text(
				'真是的，居然特地\n'
				'陪老板娘一起恶作剧……\n'
				'警察有这么清闲吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0012F不是的，因为那件事\n'
				'是委托……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F再说，你的笑容的确\n'
				'非常可爱呢。\n'
				'平常要是能多笑一点就好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……不用你多管闲事。\n'
				'好了，我还有晚上的工作要准备。\n'
				'可以不要找我说话吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'真是的……\n'
				'让人看那种美喵装备，\n'
				'肯定会露出笑容的啊……{wait}'
				'{page}'
				'……喵喵……呵呵……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('QUEST', 54, Insn('TASK_SET', 4)),
	Insn('TEXT_TALK', Char(254), Text(
		'你想问哪种礼物\n'
		'会让露卡感到高兴吗？\n'
		'这个嘛……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(254), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(254)),
	Insn('SLEEP', 600),
	Insn('EMOTE', Char(254), 0, 2000, (34, 36, 250, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1500),
	Insn('TEXT_TALK', Char(254), Text(
		'啊，之前她看猫咪的照片\n'
		'看得很入迷呢。{wait}'
		'{page}'
		'她似乎在收集\n'
		'有关猫咪的周边商品，\n'
		'这类东西应该不错吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CALL', Function((1, 15))),
	Insn('TEXT_TALK', Char(8), Text(
		'#1P啊！是你们！\n'
		'现在有空了吗？{wait}'
		'{page}'
		'不，就算没空也没关系，\n'
		'我们店里的服务生露卡，\n'
		'希望你们可以让她笑出来。{wait}'
		'{page}'
		'那孩子如果可以\n'
		'多点笑容待客的话，\n'
		'我想店里的业绩也会上升。{wait}'
		'{page}'
		'你们愿意接下这个委托吗？\n'
		'为了让本店生意兴隆，拜托你们了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('CHAR_ROTATE', Char(8), 180, 0),
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
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(4), 128),
			Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
			Insn('CHAR_SET_POS', Char(265), (3500, 0, -500), 0),
		]),
		(None, []),
	]),
	Insn('0x0D'),
	Insn('EMOTE', Char(8), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('EXPR_VAR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('CALL', Function((1, 18))),
	Insn('CALL', Function((1, 20))),
	Insn('CALL', Function((1, 22))),
	Insn('IF', [
		(Expr([Insn('VAR', 1), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}虽然想要送礼物给她，\n'
				'不过没有任何可以给她的东西。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F要送礼物的话，\n'
				'防具、鞋子和配件\n'
				'应该不错吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}要送礼物给露卡吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('NE'), Insn('END')], [
				Insn('MENU_CUSTOM', Insn('INIT', ResId(1))),
				Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('配件'))),
				Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('防具'))),
				Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('鞋子'))),
				Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('放弃'))),
				Insn('MENU_CUSTOM', Insn('FINISH', ResId(1), -1, 1)),
				Insn('MENU_WAIT', 0),
				Insn('0x60', 1),
				Insn('TEXT_RESET', b'\x00'),
				Insn('0x5A'),
				Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
					0: [
						Insn('CALL', Function((1, 17))),
						Insn('BREAK'),
					],
					1: [
						Insn('CALL', Function((1, 19))),
						Insn('BREAK'),
					],
					2: [
						Insn('CALL', Function((1, 21))),
						Insn('BREAK'),
					],
					None: [
						Insn('EXPR_VAR', 2, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
						Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
					],
				}),
				Insn('SWITCH', [Insn('VAR', 2), Insn('END')], {
					1: [
						Insn('CALL', Function((1, 5))),
						Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
						Insn('BREAK'),
					],
					2: [
						Insn('CALL', Function((1, 6))),
						Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
						Insn('BREAK'),
					],
					None: [],
				}),
			]),
		]),
	]),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('EXPR_VAR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('MENU_CUSTOM', Insn('INIT', ResId(1))),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 60, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('银胸针'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 61, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('珊瑚戒指'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 62, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('大理石戒指'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 63, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('夜光眼镜'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 64, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('凉爽项链'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 65, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('打火机'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 66, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('幻彩围巾'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 67, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('叮当耳环'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 68, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('钢手镯'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 69, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('花之瓶'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 70, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('神圣之链'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 71, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('云之使者'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 72, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('月亮坠饰'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 73, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('太阳坠饰'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 74, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('星之坠饰'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 75, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('长枪管'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 76, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('英勇纹章'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 77, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('精神徽章'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 78, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('正义硬币'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 79, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('必胜头巾'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 80, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('斗魂皮带'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 81, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('星杯挂坠'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 82, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('银之链'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 83, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('猫咪之尾'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 84, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('猫耳头饰'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 85, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('替身傀儡'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 86, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('寂静之蓝'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 87, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('激情之红'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 88, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('常青之绿'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 89, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('深邃之黄'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 90, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('草帽'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 91, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('安全头盔'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 92, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('抗菌口罩'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 93, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('咪西玩偶'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 94, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('猫咪存钱筒'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 95, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('青蛙存钱筒'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 96, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('钓圣纹章'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 97, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('神圣挂坠'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 98, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('小滴的胸针'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 99, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('五彩风车'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('放弃'))),
	Insn('MENU_CUSTOM', Insn('FINISH', ResId(1), -1, 1)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 1),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('EXPR_VAR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('EXPR_VAR', 2, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 60, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 61, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 62, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 63, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 64, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 65, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 66, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 67, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 68, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 69, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 70, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 71, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 72, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 73, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 74, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 75, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 76, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 77, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 78, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 79, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 80, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 81, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 82, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 83, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 84, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 85, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 86, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 87, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 88, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 89, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 90, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 91, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 92, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 93, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 94, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 95, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 96, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 97, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 98, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 99, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 60, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 61, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 62, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 63, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 64, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 65, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 66, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 67, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 68, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 69, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 70, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 71, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 72, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 73, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 74, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 75, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 76, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 77, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 78, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 79, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 80, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 81, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 82, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 83, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 84, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 85, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 86, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 87, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 88, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 89, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 90, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 91, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 92, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 93, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 94, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 95, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 96, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 97, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 98, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 99, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('EXPR_VAR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('MENU_CUSTOM', Insn('INIT', ResId(1))),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1500, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('皮背心'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1501, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('牛仔夹克'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1502, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('阳光衬衫'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1503, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('皮夹克'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1504, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('符文十字衣'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1505, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('纤维大衣'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1506, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('战士套装'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1507, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('防弹外套'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1508, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('高贵大衣'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1509, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('碎花连身裙'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1510, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('猫咪装'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1511, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('战斗夹克'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1512, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('武道服'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1513, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('坚硬皮衣'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1514, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('黑色套装'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1515, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('动力服'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1516, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('全金属大衣'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1517, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('天光铠甲'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1518, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('极光礼服'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1519, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('高级服饰Ｌ'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1520, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('高级服饰Ｅ'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1521, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('高级服饰Ｔ'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1522, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('高级服饰Ｒ'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('放弃'))),
	Insn('MENU_CUSTOM', Insn('FINISH', ResId(1), -1, 1)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 1),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('EXPR_VAR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('EXPR_VAR', 2, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1500, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1501, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1502, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1503, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1504, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1505, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1506, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1507, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1508, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1509, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1510, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1511, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1512, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1513, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1514, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1515, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1516, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1517, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1518, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1519, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1520, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1521, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1522, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1500, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1501, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1502, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1503, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1504, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1505, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1506, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1507, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1508, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1509, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1510, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1511, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1512, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1513, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1514, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1515, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1516, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1517, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1518, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1519, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1520, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1521, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1522, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('EXPR_VAR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('MENU_CUSTOM', Insn('INIT', ResId(1))),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1600, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('皮靴'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1601, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('舒适凉鞋'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1602, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('花漾包鞋'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1603, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('蚱蜢运动鞋'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1604, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('短跑鞋'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1605, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('技师鞋'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1606, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('铁皮绑腿'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1607, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('斯托雷加Σ'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1608, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('踩踏跳跃者'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1609, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('美行高跟鞋'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1610, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('猫咪靴'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1611, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('战斗靴'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1612, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('铁木屐'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1613, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('野战靴'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1614, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('铁板鞋'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1615, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('斯托雷加Ｐ'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1616, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('双重防护靴'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1617, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('战神护胫靴'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1618, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('调和之靴'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1619, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('云霄九天之靴'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1620, 0)), Insn('END')]), [
			Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('七耀天国之靴'))),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('放弃'))),
	Insn('MENU_CUSTOM', Insn('FINISH', ResId(1), -1, 1)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 1),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('EXPR_VAR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('EXPR_VAR', 2, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1600, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1601, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1602, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1603, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1604, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1605, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1606, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1607, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1608, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1609, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1610, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1611, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1612, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1613, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1614, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1615, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1616, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1617, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1618, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1619, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1620, 0)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
					Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1600, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1601, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1602, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1603, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1604, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1605, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1606, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1607, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1608, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1609, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1610, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1611, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1612, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1613, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1614, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1615, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1616, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1617, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1618, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1619, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 1620, 0)), Insn('END')]), [
			Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]
