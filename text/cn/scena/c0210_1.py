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
		None,
		None,
		None,
		None,
		None,
		None,
	],
	'name3': 'c0210_1',
	'labels': [],
	'chcp': [],
	'npcs': [],
	'monsters': [],
	'triggers': [],
	'objects': [],
	'unk13': b'\x00\xff\xff',
	'extra': None,
	'code': [None]*19,
	'anim': [],
}

data['code'][0] = [
	Insn('CHAR_SET_COLOR', Char(8), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(8), (119500, 0, -5600), 0),
	Insn('FORK', 8, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('0x95', Char(8), (119500, 0, 1000), 2000, 0),
	Insn('0x95', Char(8), (121420, 0, 1000), 2000, 0),
	Insn('CHAR_ROTATE', Char(8), 180, 500),
	Insn('FORK_AWAIT', Char(8), 2),
	Insn('0x4B', Char(8), -1),
	Insn('RETURN'),
]

data['code'][1] = [
	Insn('CHAR_SET_COLOR', Char(10), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(10), (119500, 0, -5600), 0),
	Insn('FORK', 10, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('0x95', Char(10), (119500, 0, 1000), 2000, 0),
	Insn('0x95', Char(10), (120220, 0, 1000), 2000, 0),
	Insn('CHAR_ROTATE', Char(10), 180, 500),
	Insn('FORK_AWAIT', Char(10), 2),
	Insn('0x4B', Char(10), -1),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('0x4C', Char(8), -1),
	Insn('0x95', Char(8), (119500, 0, 1000), 2000, 0),
	Insn('0x95', Char(8), (119500, 0, -5600), 2000, 0),
	Insn('CHAR_SET_COLOR', Char(8), Color(0x00FFFFFF), 500),
	Insn('CHAR_SET_POS', Char(8), (56290, 0, 2020), 270),
	Insn('CHAR_SET_COLOR', Char(8), Color(0xFFFFFFFF), 0),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('0x4C', Char(10), -1),
	Insn('0x95', Char(10), (119500, 0, 1000), 2000, 0),
	Insn('0x95', Char(10), (119500, 0, -5600), 2000, 0),
	Insn('CHAR_SET_COLOR', Char(10), Color(0x00FFFFFF), 500),
	Insn('CHAR_SET_POS', Char(10), (55920, 1000, 10640), 90),
	Insn('CHAR_SET_COLOR', Char(10), Color(0xFFFFFFFF), 0),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 6000),
	Insn('EMOTE_STOP', Char(258)),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 1))), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('0x4B', Char(9), -1),
			Insn('CHAR_ROTATE', Char(254), 180, 0),
			Insn('CHAR_SET_POS', Char(257), (120220, 0, -200), 0),
			Insn('CHAR_SET_POS', Char(258), (121420, 0, -200), 0),
			Insn('CHAR_SET_POS', Char(259), (120220, 0, -1400), 0),
			Insn('CHAR_SET_POS', Char(260), (121420, 0, -1400), 0),
			Insn('CAM_OFFSET', (120110, 1500, -1180), 0),
			Insn('CAM_ROTATE', 54, 22, 0, 0),
			Insn('0x6E', 240, 0),
			Insn('CAM_DISTANCE', 31000, 0),
			Insn('CAM_DISTANCE', 30000, 1500),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('EMOTE', Char(254), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('0x6F', b'\x10'),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 0))), Insn('NOT'), Insn('END')]), [
					Insn('QUEST', 58, Insn('TASK_SET', 0)),
					Insn('TEXT_TALK', Char(254), Text(
						'#3P嗨，之前你似乎\n'
						'立了大功对吧？\n'
						'我们店里的常客有聊到呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#3P因为活跃受到认可，\n'
						'所以也分配到了警犬对吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#4P#0012F咦？呃……是啊（警犬指的是\n'
						'\u3000赛特吧……）{wait}'
						'{page}'
						'#0000F话说回来，我们是看到委托才过来的……\n'
						'听说似乎要作终极面包？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#3P嗯。委托里也有写，\n'
						'我们家的贝奈特\n'
						'似乎很在意奥斯卡。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#3P看来，身为面包师傅，\n'
						'她似乎绝对不想输给他。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#2P#0309F哈哈！她给人的感觉的确\n'
						'是位不服输的小姐呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#3P虽然我觉得，\n'
						'她对奥斯卡的竞争心\n'
						'似乎有点太多，不过……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#3P有上进心不是坏事。\n'
						'就让这两人彻底\n'
						'竞争一次吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#2P#0100F原来如此……\n'
						'所以才要请我们搜集材料，\n'
						'就是这么回事吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#3P嗯。面包师傅的工作终究是\n'
						'做出好吃的面包。\n'
						'并不是击退魔兽。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#3P你们打算怎么做？\n'
						'愿意接下委托吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#3P嗯，怎么了？\n'
						'你们改变主意，\n'
						'想要接下委托了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
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
						'#4P#0006F不好意思。\n'
						'目前还有其他调查工作……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#3P这样啊。\n'
						'嗯，警察的工作也很辛苦，\n'
						'我不会勉强你们。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#3P如果你们改变主意\n'
						'要接下委托的话，\n'
						'再来找我吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('BGM_STOP', 3000),
					Insn('TEXT_TALK', Char(254), Text(
						'#3P很好，就这么决定了。\n'
						'那么，就让我来\n'
						'详细说明吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#3P#5S喂──奥斯卡、贝奈特！\n'
						'过来一下！#3S{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('SLEEP', 500),
					Insn('BGM_WAIT'),
					Insn('BGM_PLAY', b'j\x00\x00'),
					Insn('FORK', 257, 1, [
						Insn('CHAR_ROTATE', Char(254), 180, 500),
					]),
					Insn('FORK', 258, 1, [
						Insn('CHAR_ROTATE', Char(254), 180, 500),
					]),
					Insn('FORK', 259, 1, [
						Insn('CHAR_ROTATE', Char(254), 180, 500),
					]),
					Insn('FORK', 260, 1, [
						Insn('CHAR_ROTATE', Char(254), 180, 500),
					]),
					Insn('FORK_AWAIT', Char(257), 1),
					Insn('FORK_AWAIT', Char(258), 1),
					Insn('FORK_AWAIT', Char(259), 1),
					Insn('FORK_AWAIT', Char(260), 1),
					Insn('SLEEP', 800),
					Insn('CHAR_SET_POS', Char(8), (121420, 0, -7600), 0),
					Insn('CHAR_SET_POS', Char(10), (120220, 0, -7600), 0),
					Insn('FORK_LOOP', 257, 1, [
						Insn('CHAR_WATCH', Char(257), Char(10), 500),
					]),
					Insn('FORK_LOOP', 258, 1, [
						Insn('CHAR_WATCH', Char(258), Char(8), 500),
					]),
					Insn('FORK_LOOP', 259, 1, [
						Insn('CHAR_WATCH', Char(259), Char(10), 500),
					]),
					Insn('FORK_LOOP', 260, 1, [
						Insn('CHAR_WATCH', Char(260), Char(8), 500),
					]),
					Insn('FORK_FUNC', Char(8), 3, Function((1, 0))),
					Insn('SLEEP', 1200),
					Insn('FORK_FUNC', Char(10), 3, Function((1, 1))),
					Insn('FORK_AWAIT', Char(8), 3),
					Insn('FORK_AWAIT', Char(10), 3),
					Insn('FORK_QUIT', Char(257), 1),
					Insn('FORK_QUIT', Char(258), 1),
					Insn('FORK_QUIT', Char(259), 1),
					Insn('FORK_QUIT', Char(260), 1),
					Insn('SLEEP', 800),
					Insn('CHAR_WATCH', Char(8), Char(257), 500),
					Insn('SLEEP', 500),
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F#1P哦，罗伊德。\n'
						'你接下搜集材料的委托了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(257), Char(8), 500),
					Insn('SLEEP', 500),
					Insn('TEXT_TALK', Char(257), Text(
						'#3P#0000F嗯。现在正好有空，\n'
						'而且我对终极面包\n'
						'也有兴趣。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#4P#0200F到各地去\n'
						'搜集材料……这是很适合\n'
						'我们的工作呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14702F#1P听你这样讲，我就放心了。\n'
						'我正好也想出了\n'
						'新面包的点子。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F#1P其中也有比较难获得的材料，\n'
						'我正觉得困扰呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CAM_OFFSET', (120250, 1500, -40), 3000),
					Insn('CAM_ROTATE', 45, 22, 0, 3000),
					Insn('0x6E', 180, 3000),
					Insn('TEXT_TALK', Char(10), Text(
						'#14803F#3P这一天总算来临了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('0x6F', b'y'),
					Insn('CHAR_WATCH', Char(10), Char(8), 500),
					Insn('SLEEP', 500),
					Insn('TEXT_TALK', Char(10), Text(
						'#14807F#3P奥斯卡，究竟谁才是\n'
						'更厉害的面包师傅，\n'
						'我们就来一决胜负吧……！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(8), 0, 2000, (38, 38, 250, 1)),
					Insn('SLEEP', 500),
					Insn('CHAR_WATCH', Char(8), Char(10), 500),
					Insn('SLEEP', 500),
					Insn('TEXT_TALK', Char(8), Text(
						'#14709F#2P哦。你很起劲呢，贝奈特。\n'
						'彼此都加油吧！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CAM_OFFSET', (120110, 1500, -1180), 1800),
					Insn('CAM_ROTATE', 54, 22, 0, 1800),
					Insn('0x6E', 240, 1800),
					Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
					Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
					Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
					Insn('0x6F', b'y'),
					Insn('SLEEP', 1000),
					Insn('EMOTE_STOP', Char(258)),
					Insn('EMOTE_STOP', Char(259)),
					Insn('EMOTE_STOP', Char(260)),
					Insn('FORK', 258, 1, [
						Insn('CHAR_ROTATE', Char(254), 225, 500),
					]),
					Insn('FORK', 259, 1, [
						Insn('CHAR_ROTATE', Char(254), 45, 500),
					]),
					Insn('FORK', 260, 1, [
						Insn('CHAR_ROTATE', Char(254), 315, 500),
					]),
					Insn('FORK_AWAIT', Char(258), 1),
					Insn('FORK_AWAIT', Char(259), 1),
					Insn('FORK_AWAIT', Char(260), 1),
					Insn('SLEEP', 500),
					Insn('TEXT_TALK', Char(260), Text(
						'#2P#0306F（奥斯卡似乎\n'
						'\u3000没发现自己被\n'
						'\u3000当成劲敌了呢……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#4P#0206F（嗯。感觉不愧是\n'
						'\u3000罗伊德的朋友呢。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
					Insn('SLEEP', 1000),
					Insn('CHAR_WATCH', Char(257), Char(260), 500),
					Insn('SLEEP', 500),
					Insn('TEXT_TALK', Char(257), Text(
						'#3P#0009F嗯？我怎么了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(258), 0, 2000, (40, 43, 100, 0)),
					Insn('CHAR_WATCH', Char(258), Char(257), 500),
					Insn('SLEEP', 800),
					Insn('TEXT_TALK', Char(258), Text(
						'#2P#0112F不，没什么。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE_STOP', Char(258)),
					Insn('CHAR_ROTATE', Char(258), 0, 500),
					Insn('SLEEP', 500),
					Insn('TEXT_TALK', Char(258), Text(
						'#2P#0109F更重要的是，请详细告诉我们\n'
						'关于想要搜集的材料的事。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FORK', 257, 1, [
						Insn('CHAR_ROTATE', Char(254), 0, 500),
					]),
					Insn('FORK', 259, 1, [
						Insn('CHAR_ROTATE', Char(254), 0, 500),
					]),
					Insn('FORK', 260, 1, [
						Insn('CHAR_ROTATE', Char(254), 0, 500),
					]),
					Insn('FORK', 8, 1, [
						Insn('CHAR_ROTATE', Char(254), 180, 500),
					]),
					Insn('FORK', 10, 1, [
						Insn('CHAR_ROTATE', Char(254), 180, 500),
					]),
					Insn('FORK_AWAIT', Char(257), 1),
					Insn('FORK_AWAIT', Char(259), 1),
					Insn('FORK_AWAIT', Char(260), 1),
					Insn('FORK_AWAIT', Char(8), 1),
					Insn('FORK_AWAIT', Char(10), 1),
					Insn('SLEEP', 500),
					Insn('TEXT_TALK', Char(8), Text(
						'#14704F#1P嗯，说的也是。\n'
						'我希望你们搜集的是……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CALL', Function((1, 15))),
					Insn('TEXT_TALK', Char(10), Text(
						'#14804F#3P我希望你们搜集的是……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CALL', Function((1, 16))),
					Insn('TEXT_TALK', Char(258), Text(
						'#2P#0100F原来如此。\n'
						'请稍等，我把材料记录到\n'
						'搜查手册里。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FORK_FUNC', Char(258), 1, Function((1, 4))),
					Insn('TEXT_TALK', Char(254), Text(
						'#3P毕竟是两人分的材料。\n'
						'要搜集应该也很辛苦吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#3P为了公平竞争，\n'
						'所以必须搜集到\n'
						'两个人都满意的材料。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#3P我想会费很多工夫，\n'
						'不过还是麻烦你们了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#4P#0201F这还真是……责任重大呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(8), Char(257), 500),
					Insn('SLEEP', 500),
					Insn('TEXT_TALK', Char(8), Text(
						'#14706F#1P虽然是工作，不过还是很抱歉\n'
						'拜托你这种麻烦事，罗伊德。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(257), Char(8), 500),
					Insn('SLEEP', 500),
					Insn('TEXT_TALK', Char(257), Text(
						'#4P#0002F不用在意。\n'
						'既然已经接下委托，\n'
						'我就会尽力做到最好。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14709F#1P听你这么说，我就放心了。\n'
						'那就拜托你了，罗伊德！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FORK_AWAIT', Char(258), 1),
					Insn('FORK_FUNC', Char(10), 3, Function((1, 3))),
					Insn('SLEEP', 500),
					Insn('FORK_FUNC', Char(8), 3, Function((1, 2))),
					Insn('CHAR_ROTATE', Char(257), 0, 500),
					Insn('FADE_ON', 1000, Color(0x00000000), 255),
					Insn('0x0D'),
					Insn('SOUND_PLAY', 80, 0, 0, 100),
					Insn('TEXT_SET_POS', -1, -1, -1, -1),
					Insn('TEXT_SET_NAME', Translate('')),
					Insn('TEXT_MESSAGE', Char(255), Text(
						'开始进行{color 2}任务【终极面包对决！】{color 0}！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_RESET', b'\x00'),
					Insn('FADE_OFF', 300, Color(0x00000000)),
					Insn('TEXT_SET_POS', 14, 280, 60, 3),
					Insn('SLEEP', 500),
					Insn('QUEST', 58, Insn('TASK_SET', 1)),
					Insn('BGM_STOP', 3000),
					Insn('TEXT_TALK', Char(258), Text(
						'#2P#0100F那么，我们开始\n'
						'搜集材料吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#3P#0000F嗯，你说得对。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FORK_AWAIT', Char(10), 3),
					Insn('FORK_AWAIT', Char(8), 3),
					Insn('BGM_WAIT'),
					Insn('0x1F'),
				]),
			]),
			Insn('CHAR_SET_POS', Char(0), (120820, 0, -200), 0),
			Insn('0x4C', Char(9), -1),
			Insn('EVENT_END', 5),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 4))), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((1, 17))),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'哦，怎样啦？罗伊德？\n'
						'你搜集到我拜托你的\n'
						'材料了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FADE_ON', 300, Color(0x00000000), 100),
					Insn('MENU', 0, -1, -1, 0, Text(
						'【交付搜集到的材料】\n'
						'【算了】\n'
					)),
					Insn('MENU_WAIT', 0),
					Insn('0x60', 0),
					Insn('FADE_OFF', 300, Color(0x00000000)),
					Insn('IF', [
						(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), [
							Insn('TEXT_TALK', Char(254), Text(
								'你还没搜集到吗？\n'
								'那么，搜集到的话\n'
								'再跟我说吧！{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('CALL', Function((1, 18))),
							Insn('TEXT_TALK', Char(257), Text(
								'#0005F（对了……\n'
								'\u3000除了拜托的材料之外，\n'
								'\u3000也送慰问品给他们吧。）{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('EXPR_VAR', 3, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
							Insn('WHILE', [Insn('VAR', 3), Insn('CONST', 2), Insn('LT'), Insn('END')], [
								Insn('IF', [
									(Expr([Insn('VAR', 3), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
										Insn('TEXT_TALK', Char(257), Text(
											'#0004F（很好，给奥斯卡的是……）{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
									(None, [
										Insn('TEXT_TALK', Char(257), Text(
											'#0004F（还有，给贝奈特的是……）{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
								]),
								Insn('FADE_ON', 300, Color(0x00000000), 100),
								Insn('MENU', 0, -1, -1, 0, Text(
									'【交付慰问品】\n'
									'【不交付慰问品】\n'
								)),
								Insn('MENU_WAIT', 0),
								Insn('0x60', 0),
								Insn('FADE_OFF', 300, Color(0x00000000)),
								Insn('IF', [
									(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
										Insn('TEXT_SET_POS', -1, -1, -1, -1),
										Insn('TEXT_SET_NAME', Translate('')),
										Insn('TEXT_MESSAGE', Char(255), Text(
											'{color 5}请选择慰问品食材{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('TEXT_RESET', b'\x00'),
										Insn('0x5A'),
										Insn('TEXT_SET_POS', 14, 280, 60, 3),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
										Insn('MENU_CUSTOM', Insn('INIT', ResId(1))),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 308, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('纯白白米'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 309, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('五彩味噌'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 310, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('灼热火酒'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 311, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('皇家香叶'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 312, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('新鲜香草'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 313, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('黑胡椒'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 314, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('红辣椒'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 315, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('香油'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 316, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('蜂蜜糖浆'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 317, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('粗碎岩盐'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 318, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('现磨面粉'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 319, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('鲜奶'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 320, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('新鲜奶酪'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 321, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('新鲜的蛋'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 322, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('热情橘子'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 323, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('成熟苹果'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 324, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('七彩豆'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 325, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('国王马铃薯'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 326, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('痛哭洋葱'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 327, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('晴天胡萝卜'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 328, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('苦番茄'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 329, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('霜降腰肉'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('ITEM_GET', 330, 0)), Insn('END')]), [
												Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('鲜弹白肉'))),
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
											]),
											(None, []),
										]),
										Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('放弃'))),
										Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
										Insn('MENU_CUSTOM', Insn('FINISH', ResId(1), -1, 1)),
										Insn('MENU_WAIT', 0),
										Insn('0x60', 1),
										Insn('TEXT_RESET', b'\x00'),
										Insn('0x5A'),
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('GE'), Insn('VAR', 0), Insn('CONST', 0), Insn('LT'), Insn('OR'), Insn('END')]), [
												Insn('TEXT_TALK', Char(257), Text(
													'#0003F（不给任何东西也没差吧……）{wait}'
												)),
												Insn('TEXT_WAIT'),
											]),
											(None, [
												Insn('EXPR_VAR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
												Insn('TEXT_SET_NAME', Translate('')),
												Insn('TEXT_SET_POS', -1, -1, -1, -1),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 308, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 308, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 308}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 309, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 309, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 309}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 310, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 310, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 310}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 311, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 311, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 311}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 312, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 312, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 312}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 313, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 313, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 313}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 314, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 314, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 314}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 315, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 315, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 315}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 316, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 316, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 316}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 317, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 317, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 317}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 318, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 318, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 318}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 319, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 319, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 319}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 320, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 320, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 320}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 321, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 321, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 321}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 322, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 322, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 322}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 323, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 323, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 323}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 324, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 324, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 324}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 325, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 325, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 325}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 326, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 3), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 326, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 326}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 327, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 327, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 327}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 328, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 328, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 328}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 329, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 329, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 329}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('IF', [
													(Expr([Insn('EXEC', Insn('ITEM_GET', 330, 0)), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
																Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
																Insn('ITEM_REMOVE', 330, 1),
																Insn('TEXT_MESSAGE', Char(255), Text(
																	'赠送{item 330}{color 0}当慰问品了。{wait}'
																)),
															]),
															(None, []),
														]),
														Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
													]),
													(None, []),
												]),
												Insn('TEXT_WAIT'),
												Insn('TEXT_RESET', b'\x00'),
												Insn('0x5A'),
												Insn('TEXT_SET_POS', 14, 280, 60, 3),
												Insn('IF', [
													(Expr([Insn('VAR', 3), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
														Insn('IF', [
															(Expr([Insn('VAR', 2), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
																Insn('FLAG_SET', Flag(1104)),
																Insn('QUEST_BONUS_DP', 58, 1),
															]),
															(None, []),
														]),
														Insn('QUEST', 58, Insn('TASK_SET', 5)),
													]),
													(None, [
														Insn('IF', [
															(Expr([Insn('VAR', 2), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
																Insn('FLAG_SET', Flag(1105)),
																Insn('QUEST_BONUS_DP', 58, 1),
															]),
															(None, []),
														]),
														Insn('IF', [
															(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 5))), Insn('END')]), [
																Insn('QUEST', 58, Insn('TASK_UNSET', 5)),
																Insn('QUEST', 58, Insn('TASK_SET', 7)),
															]),
															(None, [
																Insn('QUEST', 58, Insn('TASK_SET', 6)),
															]),
														]),
													]),
												]),
											]),
										]),
									]),
									(None, [
										Insn('TEXT_TALK', Char(257), Text(
											'#0003F（不给任何东西也没差吧……）{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
								]),
								Insn('EXPR_VAR', 3, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F这是你们\n'
								'委托的材料。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'嗯、嗯……没错，的确是！{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('IF', [
								(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 5))), Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 6))), Insn('OR'), Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 7))), Insn('OR'), Insn('END')]), [
									Insn('TEXT_TALK', Char(254), Text(
										'……哎呀？似乎有我们没委托的材料\n'
										'混在里面……？{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(257), Text(
										'#0009F啊，那是……\n'
										'当成慰问品的东西。{wait}'
										'{page}'
										'请你告诉他们，如果方便的话，\n'
										'请使用这个材料。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(254), Text(
										'嗯……\n'
										'好吧，我知道了。\n'
										'我就收下了。{wait}'
									)),
									Insn('TEXT_WAIT'),
								]),
								(None, []),
							]),
							Insn('TEXT_TALK', Char(254), Text(
								'这是他们最近开始贩售的新面包。\n'
								'若不介意的话，还请收下。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FADE_ON', 300, Color(0x00000000), 100),
							Insn('TEXT_SET_POS', -1, -1, -1, -1),
							Insn('TEXT_SET_NAME', Translate('')),
							Insn('SOUND_PLAY', 17, 0, 0, 100),
							Insn('TEXT_MESSAGE', Char(255), Text(
								'已收下４个{item 531}{color 0}。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('0x5A'),
							Insn('SOUND_PLAY', 17, 0, 0, 100),
							Insn('TEXT_MESSAGE', Char(255), Text(
								'已收下４个{item 534}{color 0}。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('0x5A'),
							Insn('FADE_OFF', 300, Color(0x00000000)),
							Insn('TEXT_SET_POS', 14, 280, 60, 3),
							Insn('0x5A'),
							Insn('ITEM_ADD', 531, 4),
							Insn('ITEM_ADD', 534, 4),
							Insn('IF', [
								(Expr([Insn('EXEC', Insn('RECIPE', 23)), Insn('NOT'), Insn('END')]), [
									Insn('TEXT_TALK', Char(254), Text(
										'对了。\n'
										'你们知道这种咖啡吗？\n'
										'顺便也学一下这个吧。{wait}'
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
									Insn('TEXT_SET_POS', 14, 280, 60, 3),
									Insn('0x5A'),
									Insn('RECIPE', 23),
								]),
								(None, []),
							]),
							Insn('TEXT_TALK', Char(257), Text(
								'#0002F谢谢你。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'这次的对决，\n'
								'对他们来说肯定会是\n'
								'很好的经验。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'如果能创作出新面包，\n'
								'客人也会增加吧。\n'
								'谢谢你们。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FADE_ON', 300, Color(0x00000000), 100),
							Insn('SOUND_PLAY', 9, 0, 0, 100),
							Insn('TEXT_SET_POS', -1, -1, -1, -1),
							Insn('TEXT_SET_NAME', Translate('')),
							Insn('TEXT_MESSAGE', Char(255), Text(
								'达成{color 2}任务【终极面包对决！】{color 0}了！{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_RESET', b'\x00'),
							Insn('FADE_OFF', 300, Color(0x00000000)),
							Insn('TEXT_SET_POS', 14, 280, 60, 3),
							Insn('FLAG_UNSET', Flag(0)),
							Insn('QUEST', 58, Insn('TASK_SET', 4)),
							Insn('QUEST', 58, Insn('FLAG_UNSET', 16)),
							Insn('FLAG_SET', Flag(1106)),
						]),
					]),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'委托的物品数量不少，\n'
						'搜集起来会很辛苦吧，不过……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'奥斯卡跟贝奈特\n'
						'都很期待。\n'
						'不好意思，要拜托你们了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'奥斯卡跟贝奈特\n'
				'似乎都开始\n'
				'制作新面包了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'胜负要以贩售数量来决定。\n'
				'究竟哪边会获胜，我也很期待。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'这次的对决，\n'
				'对他们来说肯定会是\n'
				'很好的经验。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'他们的新面包比赛结果，\n'
				'你们一定要过来确认哦！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('TEXT_TALK', Char(254), Text(
		'这次的对决，\n'
		'对他们来说肯定会是\n'
		'很好的经验。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'顺道也让客人数量增加许多。\n'
		'哎呀，真是感谢他们！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('CHAR_SET_COLOR', Char(9), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_POS', Char(9), (60500, 0, 6500), 0),
	Insn('FORK', 9, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('0x95', Char(9), (60500, 0, 1400), 2000, 0),
	Insn('CHAR_ROTATE', Char(9), 270, 500),
	Insn('FORK_AWAIT', Char(9), 2),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('EXPR_CHAR_ATTR', Char(10), 40, Expr([Insn('CONST', 13), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('SOUND_PLAY', 612, 0, 0, 100),
		Insn('FORK', 10, 2, [
			Insn('0x9C', Char(254), b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x01\x00\x00\xb8\x0b\x00\x00'),
		]),
		Insn('FORK_AWAIT', Char(254), 2),
	]),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x4B', Char(9), -1),
	Insn('0x4B', Char(8), -1),
	Insn('0x4B', Char(10), -1),
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
	Insn('TEXT_TALK', Char(8), Text(
		'#14700F哦，罗伊德，\n'
		'你来得正好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F嗯？怎么了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (56840, 1500, 720), 2000),
	Insn('CAM_ROTATE', 45, 12, 0, 2000),
	Insn('0x6E', 300, 2000),
	Insn('CAM_DISTANCE', 21000, 2000),
	Insn('FORK_FUNC', Char(9), 3, Function((1, 7))),
	Insn('FORK_AWAIT', Char(9), 3),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(9), Text(
		'终极面包对决的\n'
		'比赛结果刚好出来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 4000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('EFF_LOAD', ResId(7), 'event\\ev308_00.eff'),
	Insn('CHAR_SET_POS', Char(9), (120820, 0, 2070), 180),
	Insn('CHAR_SET_POS', Char(8), (121420, 0, 1000), 180),
	Insn('CHAR_SET_POS', Char(10), (120220, 0, 1000), 180),
	Insn('CHAR_SET_POS', Char(257), (120220, 0, -1200), 0),
	Insn('CHAR_SET_POS', Char(258), (121420, 0, -1200), 0),
	Insn('CHAR_SET_POS', Char(259), (120220, 0, -2400), 0),
	Insn('CHAR_SET_POS', Char(260), (121420, 0, -2400), 0),
	Insn('CAM_OFFSET', (120110, 1500, -1180), 0),
	Insn('CAM_ROTATE', 54, 22, 0, 0),
	Insn('0x6E', 240, 0),
	Insn('CAM_DISTANCE', 31000, 0),
	Insn('CAM_DISTANCE', 30000, 1500),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('BGM_WAIT'),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F那么……\n'
		'是哪边赢了呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (120580, 1500, 460), 500),
	Insn('CAM_ROTATE', 45, 22, 0, 500),
	Insn('0x6E', 300, 500),
	Insn('CAM_DISTANCE', 17000, 500),
	Insn('TEXT_TALK', Char(9), Text(
		'嗯。结果是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x6F', b'y'),
	Insn('EMOTE', Char(9), 300, 1600, (54, 57, 250, 0)),
	Insn('SOUND_PLAY', 860, 0, 0, 100),
	Insn('SLEEP', 600),
	Insn('EMOTE_STOP', Char(9)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 5))), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1104)), Insn('END')]), [
					Insn('EXPR_VAR', 3, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
					Insn('QUEST', 58, Insn('TASK_SET', 12)),
				]),
				(None, [
					Insn('EXPR_VAR', 3, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
					Insn('QUEST', 58, Insn('TASK_SET', 13)),
				]),
			]),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 6))), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1105)), Insn('END')]), [
					Insn('EXPR_VAR', 3, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
					Insn('QUEST', 58, Insn('TASK_SET', 12)),
				]),
				(None, [
					Insn('EXPR_VAR', 3, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
					Insn('QUEST', 58, Insn('TASK_SET', 13)),
				]),
			]),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 7))), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1104)), Insn('FLAG', Flag(1105)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
					Insn('EXPR_VAR', 3, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
					Insn('QUEST', 58, Insn('TASK_SET', 12)),
				]),
				(Expr([Insn('FLAG', Flag(1104)), Insn('NOT'), Insn('FLAG', Flag(1105)), Insn('BOOL_AND'), Insn('END')]), [
					Insn('EXPR_VAR', 3, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
					Insn('QUEST', 58, Insn('TASK_SET', 12)),
				]),
				(None, [
					Insn('EXPR_VAR', 3, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
				]),
			]),
		]),
		(None, [
			Insn('EXPR_VAR', 3, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		]),
	]),
	Insn('SOUND_PLAY', 896, 0, 0, 100),
	Insn('EFF_PLAY', (ResId(7), 7), Char(255), 0, -10252, 1, 0, 0, 1000, 0, 0, 0, 0, (400, 400, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('SWITCH', [Insn('VAR', 3), Insn('END')], {
		0: [
			Insn('TEXT_TALK', Char(9), Text(
				'#2P#5S双方平手。#3S{wait}'
				'{page}'
				'双方做出数量相同的面包，\n'
				'而且都卖光了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BGM_PLAY', b'n\x00\x00'),
			Insn('CHAR_ROTATE', Char(10), 270, 500),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(10), Text(
				'#14806F#3P真不甘心……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#14704F#2P我倒是还好。\n'
				'我已经尽力了，\n'
				'所以不会遗憾。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_WATCH', Char(8), Char(10), 500),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(8), Text(
				'#14702F#2P再说，贝奈特的面包\n'
				'也很好吃。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(10), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 500),
			Insn('CHAR_WATCH', Char(10), Char(8), 500),
			Insn('EMOTE', Char(10), 0, 2000, (40, 43, 100, 0)),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(10), Text(
				'#14815F#3P什，什么啦……\n'
				'居然称赞对手，\n'
				'你有毛病吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE_STOP', Char(10)),
			Insn('QUEST', 58, Insn('TASK_SET', 11)),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(9), Text(
				'#5S奥斯卡获胜。#3S{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BGM_PLAY', b'i\x00\x00'),
			Insn('TEXT_TALK', Char(8), Text(
				'#14702F#2P哈哈。\n'
				'这都是托罗伊德你们的福。\n'
				'谢谢你。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1104)), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14704F#2P特别是慰问品\n'
						'『{item 322}』很有用。\n'
						'我是因为那个材料才想出点子的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
			Insn('CHAR_ROTATE', Char(10), 270, 500),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(10), Text(
				'#14811F#3P真、真不甘心……！\n'
				'本来想说这次\n'
				'一定要赢过你的说！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(8), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 500),
			Insn('CHAR_WATCH', Char(8), Char(10), 500),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(8), Text(
				'#14705F#2P什么嘛，不管是谁获胜\n'
				'都没关系吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#14702F#2P贝奈特的面包也很好吃。\n'
				'创作出两种新面包，\n'
				'这样客人也会增加吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_WATCH', Char(10), Char(8), 500),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(10), Text(
				'#14813F#3P什、什么嘛……\n'
				'你这样是在安慰我吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#14702F#2P嗯？我不是那个意思。\n'
				'贝奈特创作的新面包，\n'
				'我觉得做得很好。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('QUEST', 58, Insn('TASK_SET', 9)),
			Insn('BREAK'),
		],
		None: [
			Insn('TEXT_TALK', Char(9), Text(
				'#5S贝奈特获胜。#3S{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(10), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 500),
			Insn('BGM_PLAY', b'\x98\x01\x00'),
			Insn('TEXT_TALK', Char(10), Text(
				'#14809F#3P咦……是、是真的吗！？\n'
				'……太好了！太好了──！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(10), 1, Function((1, 8))),
			Insn('CHAR_WATCH', Char(8), Char(10), 500),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(8), Text(
				'#14709F#2P哈哈。恭喜你，贝奈特。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_QUIT', Char(10), 1),
			Insn('CHAR_WATCH', Char(10), Char(8), 500),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(10), Text(
				'#14805F#3P什、什么嘛……\n'
				'你不觉得不甘心吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#14704F#2P嗯？不会啊。\n'
				'因为我也做了\n'
				'自己觉得满意的新面包。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#14702F#2P再说，贝奈特的面包\n'
				'的确做得很好。\n'
				'既好吃，也能让人了解里面包含了她的心意。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(10), 0, 2000, (40, 43, 100, 0)),
			Insn('SLEEP', 1000),
			Insn('EMOTE_STOP', Char(10)),
			Insn('TEXT_TALK', Char(10), Text(
				'#14813F#3P什、什么嘛……\n'
				'就算你大力称赞我，\n'
				'我也不会感谢你……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'#14808F#3P……这、这次能够获胜，\n'
				'也有罗伊德他们搜集的材料\n'
				'很好的因素在里面……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1105)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'#14804F#3P如果没有『{item 326}』的话，\n'
						'老实说，\n'
						'我想我不会获胜……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
			Insn('QUEST', 58, Insn('TASK_SET', 10)),
			Insn('BREAK'),
		],
	}),
	Insn('TEXT_TALK', Char(8), Text(
		'#14709F#2P哈哈！今后也\n'
		'彼此都加油吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#14813F#3P如、如果你都这么说的话，\n'
		'要这么做也可以……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (120820, 1500, -1800), 1000),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('SLEEP', 500),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(258), Text(
		'#2P#0109F（该怎么说……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#4P#0202F（这两个人\n'
		'\u3000还蛮登对的嘛，\n'
		'\u3000我有这种感觉呢。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(1106)),
	Insn('BGM_STOP', 3000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(8), (56290, 0, 2020), 270),
	Insn('CHAR_SET_POS', Char(9), (119120, 0, -660), 275),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_SET_POS', Char(0), (120820, 0, -600), 0),
	Insn('0x4C', Char(9), -1),
	Insn('0x4C', Char(8), -1),
	Insn('0x4C', Char(10), -1),
	Insn('EFF_STOP', (ResId(7), 2)),
	Insn('BGM_WAIT'),
	Insn('0x1F'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('TEXT_START', Char(8)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 1))), Insn('NOT'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('FLAG_SET', Flag(0)),
					Insn('TEXT_TALK', Char(8), Text(
						'#14702F嗨，罗伊德。\n'
						'我们店里有提出委托，\n'
						'你有看到吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F嗯。据说是要做\n'
						'终极面包……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14704F没错。\n'
						'虽然我对比赛或胜负\n'
						'没有太大兴趣……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F只是贝奈特对这次比赛\n'
						'好像很积极。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14709F不过，制作终极面包\n'
						'很有趣。\n'
						'以面包师傅来说，会令人跃跃欲试。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14702F就是这样，如果你能接下委托的话，\n'
						'我会很高兴。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F总之，详细内容去问\n'
						'里面的老板吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 4))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(8), Text(
				'#14702F嗨，罗伊德。\n'
				'材料搜集得还顺利吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(8), Text(
				'#14709F托罗伊德你们的福，\n'
				'似乎可以做出不错的新面包。\n'
				'以面包师傅来说，会令人跃跃欲试。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(8)),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 1))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(8), Text(
				'#14702F如果你能接下委托的话，\n'
				'我会很高兴。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#14700F总之，详细内容去问\n'
				'里面的老板吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 4))), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((1, 17))),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('NE'), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'#14704F以面包师傅来说，\n'
						'创作新面包是一件\n'
						'很需要干劲的工作呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14702F……虽然这么说，\n'
						'不过这次的新面包，\n'
						'我总觉得还差一点冲击。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14703F该怎么说呢？要是能多加入一些\n'
						'『热情』就好了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F哎呀，不过这是我的问题。\n'
						'材料搜集就拜托\n'
						'罗伊德你们了！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('QUEST', 58, Insn('TASK_SET', 2)),
				]),
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('FLAG_SET', Flag(0)),
					Insn('TEXT_TALK', Char(8), Text(
						'#14702F哦，罗伊德。\n'
						'食材搜集得怎样了？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F嗯。\n'
						'你说的东西都收齐了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14709F哦！不愧是罗伊德。\n'
						'办事效率真高！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14702F这么一来，我就可以投入\n'
						'制作新面包的准备了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14709F谢啦，罗伊德。\n'
						'果然你很值得依赖呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0014F没这回事，这没什么大不了的。\n'
						'比起这个，\n'
						'我会期待你的新面包。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14702F啊，对了。我差点忘了。\n'
						'材料交给在里面的老板吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F委托的报酬应该也可以\n'
						'从老板那拿到。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14703F……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F材料交给在里面的老板吧。\n'
						'应该可以拿到委托的报酬。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14703F……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0001F……？\n'
						'怎么了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14706F嗯，难得你帮忙准备材料，\n'
						'我还说这种话，真的很抱歉，不过……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14701F这次的新面包，\n'
						'我总觉得还差一点冲击。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14703F该怎么说，要是能多加入一些\n'
						'『热情』就好了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'#14700F嗯～有点过于模糊了对吧？\n'
						'抱歉，你别放在心上！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('QUEST', 58, Insn('TASK_SET', 2)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
			Insn('FLAG_SET', Flag(0)),
			Insn('TEXT_TALK', Char(8), Text(
				'#14702F我马上就开始投入\n'
				'制作新面包的准备吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#14709F你就期待面包出炉吧！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(8), Text(
				'#14700F贝奈特那家伙，\n'
				'似乎马上就开始\n'
				'准备作新面包了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#14702F我也很期待，想知道\n'
				'她会做出怎样的面包呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 9))), Insn('END')]), [
			Insn('TEXT_TALK', Char(8), Text(
				'#14702F托新面包的福，\n'
				'客人也增加许多了。\n'
				'谢谢你，罗伊德。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#14703F只不过，\n'
				'贝奈特那家伙\n'
				'感觉非常后悔……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#14700F不管是哪边获胜，\n'
				'我觉得只要\n'
				'客人有增加就好。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(8), Text(
				'#14702F托新面包的福，\n'
				'客人也增加许多了。\n'
				'谢谢你。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#14704F贝奈特那家伙\n'
				'也很感谢罗伊德。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 1))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'#14803F从我的角度来看，\n'
				'我跟奥斯卡的本领不相上下……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'#14807F正因为如此……\n'
				'就用这次比赛来一决高下吧！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 4))), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((1, 17))),
			Insn('IF', [
				(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('NE'), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(254), Text(
								'#14803F嘀咕嘀咕……\n'
								'要让吃的人感动……\n'
								'眼泪……？『痛哭』……？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'#14805F……啊，对、对不起。\n'
								'我正在思考\n'
								'新面包的点子。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(2)),
							Insn('QUEST', 58, Insn('TASK_SET', 3)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(254), Text(
								'#14804F如果是这次构思中的\n'
								'新面包，一定可以做得比\n'
								'奥斯卡更好吃……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'#14807F……为了这个目标，\n'
								'我无论如何都需要那个材料。\n'
								'因为我不想输给奥斯卡……！{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(260), Text(
								'#0305F真有干劲呢……{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('FLAG_SET', Flag(2)),
					Insn('EMOTE', Char(10), 0, 2000, (24, 27, 250, 1)),
					Insn('SLEEP', 1200),
					Insn('TEXT_TALK', Char(254), Text(
						'#14803F嘀咕嘀咕……到底、到底\n'
						'是什么不够呢？嗯……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(10), 0, 2000, (38, 38, 250, 1)),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(254), Text(
						'#14800F哎、哎呀呀，是你们啊……\n'
						'搜集食材这件事有进展吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F嗯。\n'
						'你说的东西都收齐了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#14805F这、这样啊！\n'
						'比我想像中的还快呢！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#14810F把材料交给在工房里的\n'
						'爸爸就可以了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#14803F……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#14803F嘀咕嘀咕……\n'
						'要让吃的人感动……\n'
						'眼泪……？『痛哭』……？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#14805F……啊，对、对不起。\n'
						'我正在思考\n'
						'新面包的点子。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#14810F把材料交给工房里的\n'
						'爸爸吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#14817F还、还有，呃……\n'
						'谢谢你的帮忙。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('QUEST', 58, Insn('TASK_SET', 3)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
			Insn('FLAG_SET', Flag(2)),
			Insn('TEXT_TALK', Char(254), Text(
				'#14803F奥斯卡\n'
				'似乎开始\n'
				'制作新面包了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'#14807F我也不能输给他。\n'
				'我绝对会赢过他……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'#14803F……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'#14810F……谢、谢谢你，罗伊德。\n'
				'还有各位也是。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'#14802F……敬、敬请期待哦。\n'
				'我会做出好面包的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'#14809F只要能完成我现在构思中的\n'
				'新面包，肯定能赢过奥斯卡。\n'
				'呵呵……真令人期待。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'#14810F……我、我打从心底\n'
				'感谢各位。\n'
				'……非常谢谢你们。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 10))), Insn('END')]), [
			Insn('TEXT_TALK', Char(10), Text(
				'#14809F呵呵……我总算\n'
				'赢过奥斯卡了！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'#14801F……不过，\n'
				'奥斯卡那家伙居然恭喜我……\n'
				'真让人搞不懂……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 11))), Insn('END')]), [
			Insn('TEXT_TALK', Char(10), Text(
				'#14806F没想到居然会平手……\n'
				'明明这次就可以分出胜负了！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'#14804F非常好。\n'
				'在下次比赛之前，我会更加更加磨练技术，\n'
				'绝──对要让你认输！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(10), Text(
				'#14806F真、真不甘心！\n'
				'我又输了……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'#14807F……但是，这次是输在材料差别。\n'
				'技术上我可没有输！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'#14813F迟早我绝对会\n'
				'一雪前耻……！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('TEXT_TALK', Char(8), Text(
		'#14700F{item 300}#3P\u3000\u3000\u3000×５\n'
		'{item 306}\u3000\u3000\u3000×３\n'
		'{item 357}\u3000\u3000\u3000\u3000×３吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('TEXT_TALK', Char(10), Text(
		'#14800F{item 301}#3P\u3000\u3000×３\n'
		'{item 303}\u3000\u3000×５\n'
		'{item 356}\u3000×３哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 300, 0)), Insn('CONST', 5), Insn('GE'), Insn('EXEC', Insn('ITEM_GET', 306, 0)), Insn('CONST', 3), Insn('GE'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 357, 0)), Insn('CONST', 3), Insn('GE'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 301, 0)), Insn('CONST', 3), Insn('GE'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 303, 0)), Insn('CONST', 5), Insn('GE'), Insn('BOOL_AND'), Insn('EXEC', Insn('ITEM_GET', 356, 0)), Insn('CONST', 3), Insn('GE'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_VAR', 0, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
		]),
		(None, [
			Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		]),
	]),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('ITEM_REMOVE', 300, 5),
	Insn('ITEM_REMOVE', 306, 3),
	Insn('ITEM_REMOVE', 357, 3),
	Insn('ITEM_REMOVE', 301, 3),
	Insn('ITEM_REMOVE', 303, 5),
	Insn('ITEM_REMOVE', 356, 3),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}罗伊德将两人的面包对决材料交给他们。\n'
		'{item 300}\u3000\u3000×５\u3000{item 301}\u3000\u3000×３\n'
		'{item 306}\u3000\u3000×３\u3000{item 303}\u3000\u3000×５\n'
		'{item 357}\u3000\u3000\u3000×３\u3000{item 356}\u3000×３{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('0x5A'),
	Insn('RETURN'),
]
