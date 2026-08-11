# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't1500',
	'name2': 't1500',
	'location': 77,
	'bgm': 123,
	'flags': 8192,
	'includes': [
		None,
		None,
		None,
		None,
		None,
		None,
	],
	'name3': 't1500_1',
	'labels': [],
	'chcp': [],
	'npcs': [],
	'monsters': [],
	'triggers': [],
	'objects': [],
	'unk13': b'\x00\xff\xff',
	'extra': None,
	'code': [None]*31,
	'anim': [],
}

data['code'][0] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('CALL', Function((2, 24))),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('END')]), [
			Insn('CALL', Function((2, 3))),
		]),
		(None, [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 0))), Insn('NOT'), Insn('END')]), [
					Insn('QUEST', 56, Insn('TASK_SET', 0)),
					Insn('TEXT_TALK', Char(254), Text(
						'真是的……\n'
						'亚苏拉主任\n'
						'真让人伤脑筋。{wait}'
						'{page}'
						'不需要挑在\n'
						'这么忙的时候\n'
						'搞失踪吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F呃，不好意思。\n'
						'我们是警察接到委托后\n'
						'派来的人……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哎呀……\n'
						'警察已经来了吗？{wait}'
						'{page}'
						'主任要是也有这种程度的\n'
						'行动力就好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CALL', Function((2, 2))),
					Insn('CAM_OFFSET', (107090, 1000, -2520), 3000),
					Insn('CAM_ROTATE', 45, 28, 0, 3000),
					Insn('CAM_DISTANCE', 20000, 3000),
					Insn('FADE_OFF', 1000, Color(0x00000000)),
					Insn('0x0D'),
					Insn('0x6F', b'y'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F呃，关于那位亚苏拉主任\n'
						'失踪的事情。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F可以告诉我们事情的\n'
						'详细经过吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'是这样的。\n'
						'如果只是每天迟到的话，\n'
						'这还没有任何问题……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0303F每天都迟到，\n'
						'我觉得这也是个\n'
						'问题啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_SET_FRAME', Char(259), 0),
					Insn('SLEEP', 300),
					Insn('TEXT_TALK', Char(259), Text(
						'#0211F这话由兰迪来说，\n'
						'一点说服力也没有。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_SET_FRAME', Char(260), 0),
					Insn('CHAR_SET_FRAME', Char(257), 0),
					Insn('CHAR_SET_FRAME', Char(258), 0),
					Insn('SLEEP', 150),
					Insn('CHAR_SET_FRAME', Char(257), 2),
					Insn('CHAR_SET_FRAME', Char(258), 1),
					Insn('SLEEP', 1000),
					Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 2000),
					Insn('CHAR_SET_FRAME', Char(257), 0),
					Insn('CHAR_SET_FRAME', Char(258), 0),
					Insn('SLEEP', 100),
					Insn('CHAR_SET_FRAME', Char(257), 1),
					Insn('CHAR_SET_FRAME', Char(258), 2),
					Insn('CHAR_SET_FRAME', Char(259), 1),
					Insn('CHAR_SET_FRAME', Char(260), 2),
					Insn('TEXT_TALK', Char(254), Text(
						'然后，玛洛妮\n'
						'到宿舍去看\n'
						'发生了什么事……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0001F结果发现\n'
						'亚苏拉主任\n'
						'人不在那里。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'就是这么一回事。\n'
						'今天没有预计要出诊，\n'
						'应该也没有其他外出的事由才对。{wait}'
						'{page}'
						'找遍医院内也没有看到她，\n'
						'这不是很奇怪吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0101F没有任何\n'
						'像是留言的东西吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不，没有呢。\n'
						'只不过……{wait}'
						'{page}'
						'前阵子，\n'
						'有护理师看到\n'
						'主任在烦恼事情的样子。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0001F也就是说，她可能\n'
						'遇到了什么麻烦吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这我就不是很清楚了。\n'
						'起码在我看来，\n'
						'我是不觉得她有麻烦。{wait}'
						'{page}'
						'只是，说不定\n'
						'也有这种可能。{wait}'
						'{page}'
						'总之，如果她卷入事件里\n'
						'就糟了，你们可以想办法\n'
						'找到主任吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('CALL', Function((2, 2))),
					Insn('CAM_OFFSET', (107090, 1000, -2520), 0),
					Insn('CAM_ROTATE', 45, 28, 0, 0),
					Insn('CAM_DISTANCE', 20000, 0),
					Insn('FADE_OFF', 1000, Color(0x00000000)),
					Insn('0x0D'),
					Insn('TEXT_TALK', Char(254), Text(
						'唉呀，你们不是\n'
						'特务什么的人吗？{wait}'
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
					Insn('TEXT_TALK', Char(254), Text(
						'你们改变主意，\n'
						'打算帮忙找我们的主任了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('CALL', Function((2, 1))),
		]),
	]),
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
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('QUEST', 56, Insn('TASK_SET', 1)),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F嗯。我了解情况了。\n'
				'我们接受这分委托。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'这样啊，谢谢你。\n'
				'虽然很抱歉，\n'
				'那就拜托你们啰。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FADE_ON', 300, Color(0x00000000), 100),
			Insn('SOUND_PLAY', 80, 0, 0, 100),
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'开始进行{color 2}任务【寻找贪睡医师】{color 0}！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('TEXT_SET_POS', 14, 280, 60, 3),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#0006F不好意思。\n'
				'虽然我了解状况了，\n'
				'不过现在还有其他调查工作。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'这样啊。\n'
				'既然如此，那也没办法了。{wait}'
				'{page}'
				'嗯，主任就由我们\n'
				'找看看吧。{wait}'
				'{page}'
				'说不定她只是到\n'
				'医院外面散步而已。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'对了对了。找这里的护理师\n'
				'跟医师他们\n'
				'打听或许不错。{wait}'
				'{page}'
				'就算是我\n'
				'不知道的事，或许\n'
				'有人知道也不一定。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0002F我知道了。{wait}'
				'{page}'
				'#0000F大家，首先开始\n'
				'四处打听吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F了解。这是调查的基本呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_FLAG1_UNSET', Char(257), 4),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_FLAG1_UNSET', Char(258), 4),
	Insn('CHAR_SET_CHCP', Char(258), 255),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_FLAG1_UNSET', Char(259), 4),
	Insn('CHAR_SET_CHCP', Char(259), 255),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_FLAG1_UNSET', Char(260), 4),
	Insn('CHAR_SET_CHCP', Char(260), 255),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('CHAR_SET_POS', Char(254), (108930, 0, 1450), 45),
	Insn('CHAR_SET_POS', Char(0), (104500, 0, 90), 270),
	Insn('0x49'),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0xD5', 33),
	Insn('0x4C', Char(254), -1),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('EVENT_BEGIN', 0),
	Insn('0x4B', Char(254), -1),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (107090, 1000, -2520), 0),
	Insn('CAM_ROTATE', 45, 27, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 22000, 0),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('LOAD_CHCP', 'chr/ch00202', 32),
	Insn('LOAD_CHCP', 'chr/ch00302', 33),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('CHAR_SET_CHCP', Char(259), 32),
	Insn('CHAR_SET_FRAME', Char(259), 1),
	Insn('CHAR_SET_CHCP', Char(260), 33),
	Insn('CHAR_SET_FRAME', Char(260), 2),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_SET_POS', Char(254), (107170, 0, 1380), 180),
	Insn('CHAR_SET_POS', Char(257), (105770, 250, -2000), 90),
	Insn('CHAR_SET_POS', Char(258), (108770, 250, -2000), 270),
	Insn('CHAR_SET_POS', Char(259), (105730, 250, -5250), 90),
	Insn('CHAR_SET_POS', Char(260), (108730, 250, -5250), 270),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 2))), Insn('NOT'), Insn('END')]), [
			Insn('QUEST', 56, Insn('TASK_SET', 2)),
			Insn('TEXT_TALK', Char(254), Text(
				'最早发现\n'
				'主任失踪的是\n'
				'玛洛妮对吧？{wait}'
				'{page}'
				'每天去叫醒睡过头的主任，\n'
				'是她的例行公事。{wait}'
				'{page}'
				'说不定她知道些\n'
				'什么呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'每天去叫醒睡过头的主任，\n'
				'是她的例行公事。{wait}'
				'{page}'
				'说不定她知道些\n'
				'什么呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('CALL', Function((2, 25))),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 3))), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('0x4B', Char(254), -1),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CAM_OFFSET', (-80, 1000, 17080), 0),
			Insn('CAM_ROTATE', 55, 21, 0, 0),
			Insn('0x6E', 440, 0),
			Insn('CAM_DISTANCE', 19500, 0),
			Insn('CHAR_SET_POS', Char(254), (-90, 0, 17420), 180),
			Insn('CHAR_SET_POS', Char(257), (-690, 0, 16219), 0),
			Insn('CHAR_SET_POS', Char(258), (590, 0, 16219), 0),
			Insn('CHAR_SET_POS', Char(259), (-690, 0, 15020), 0),
			Insn('CHAR_SET_POS', Char(260), (590, 0, 15020), 0),
			Insn('CAM_DISTANCE', 17500, 1000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(254), Text(
				'亚苏拉主任\n'
				'真的每天都睡过头。{wait}'
				'{page}'
				'因此，每天去叫醒她\n'
				'就是我的工作。{wait}'
				'{page}'
				'所以我可以肯定。\n'
				'那位亚苏拉主任\n'
				'绝对不可能早起！{wait}'
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
			Insn('TEXT_TALK', Char(254), Text(
				'绝对不会错。\n'
				'主任肯定被卷入\n'
				'什么事件了！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0012F#4P什么事件……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_POS', Char(0), (950, 50, 19020), 225),
			Insn('QUEST', 56, Insn('TASK_SET', 3)),
			Insn('0x4C', Char(254), -1),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'那位\n'
				'亚苏拉主任\n'
				'绝对不可能早起！{wait}'
				'{page}'
				'绝对不会错。\n'
				'主任肯定被卷入\n'
				'什么事件了！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('CALL', Function((2, 26))),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 4))), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('0x4B', Char(254), -1),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CAM_OFFSET', (59820, 1000, -57540), 0),
			Insn('CAM_ROTATE', 45, 23, 0, 0),
			Insn('0x6E', 440, 0),
			Insn('CAM_DISTANCE', 18500, 0),
			Insn('CHAR_SET_POS', Char(254), (59680, 0, -56750), 180),
			Insn('CHAR_SET_POS', Char(257), (59080, 0, -57950), 0),
			Insn('CHAR_SET_POS', Char(258), (60280, 0, -57950), 0),
			Insn('CHAR_SET_POS', Char(259), (59080, 0, -59150), 0),
			Insn('CHAR_SET_POS', Char(260), (60280, 0, -59150), 0),
			Insn('CAM_DISTANCE', 16500, 1000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(254), Text(
				'亚苏拉前辈\n'
				'究竟去哪了……{wait}'
				'{page}'
				'该不会，\n'
				'因为每天都被凯瑞教授说教，\n'
				'所以感到厌烦了吗……？{wait}'
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
			Insn('TEXT_TALK', Char(259), Text(
				'#0205F她每天都被\n'
				'说教吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯。不要老是以为\n'
				'你还是学生！\n'
				'之类的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'前辈也是个悠闲的人，\n'
				'就算被说教\n'
				'也是若无其事的样子…{wait}'
				'{page}'
				'说不定，她的内心\n'
				'其实有受伤呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x4C', Char(254), -1),
			Insn('QUEST', 56, Insn('TASK_SET', 4)),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'亚苏拉前辈\n'
				'因为惹凯瑞教授生气，\n'
				'所以说不定对研究感到厌烦了。{wait}'
				'{page}'
				'前辈也是个悠闲的人，\n'
				'就算被说教\n'
				'也是若无其事的样子…{wait}'
				'{page}'
				'说不定，她的内心\n'
				'其实有受伤呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 5))), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CAM_OFFSET', (50090, 1000, -58250), 0),
			Insn('CAM_ROTATE', 56, 23, 0, 0),
			Insn('0x6E', 440, 0),
			Insn('CAM_DISTANCE', 20000, 0),
			Insn('CHAR_SET_FRAME', Char(254), 2),
			Insn('CHAR_SET_POS', Char(257), (49420, 0, -58320), 180),
			Insn('CHAR_SET_POS', Char(258), (50540, 0, -58320), 180),
			Insn('CHAR_SET_POS', Char(259), (49420, 0, -57360), 180),
			Insn('CHAR_SET_POS', Char(260), (50540, 0, -57360), 180),
			Insn('CAM_DISTANCE', 18000, 1000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(254), Text(
				'真是的，亚苏拉还真是\n'
				'让人伤脑筋。{wait}'
				'{page}'
				'不需要挑在这么忙的\n'
				'时候搞失踪吧……{wait}'
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
				'#0012F不，如果是事件的话，\n'
				'我想她应该也是\n'
				'不想被卷进去的吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('QUEST', 56, Insn('TASK_SET', 5)),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'她当上主任之后到现在\n'
				'也过去不少时间了，\n'
				'却还是无法摆脱学生心理。{wait}'
				'{page}'
				'真是的，亚苏拉还真是\n'
				'让人伤脑筋。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('CALL', Function((2, 27))),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 6))), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('0x4B', Char(254), -1),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CAM_OFFSET', (202980, 1000, 310), 0),
			Insn('CAM_ROTATE', 37, 23, 0, 0),
			Insn('0x6E', 440, 0),
			Insn('CAM_DISTANCE', 17000, 0),
			Insn('CHAR_SET_POS', Char(254), (203830, 0, 340), 270),
			Insn('CHAR_SET_POS', Char(257), (202630, 0, 940), 90),
			Insn('CHAR_SET_POS', Char(258), (202630, 0, -340), 90),
			Insn('CHAR_SET_POS', Char(259), (201430, 0, 940), 90),
			Insn('CHAR_SET_POS', Char(260), (201430, 0, -340), 90),
			Insn('CAM_DISTANCE', 15000, 1000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(254), Text(
				'亚苏拉主任……\n'
				'这么说来，我记得她有说过\n'
				'自己有烦恼。{wait}'
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
				'#1P#0001F烦恼吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#3P#0100F你知道是什么烦恼吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，这我就不清楚了……{wait}'
				'{page}'
				'只不过，\n'
				'她说是在这家医院\n'
				'也无法解决的烦恼。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0203F说不定和这次的\n'
				'失踪事件有关系。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_POS', Char(0), (202630, 0, 340), 90),
			Insn('0x4C', Char(254), -1),
			Insn('QUEST', 56, Insn('TASK_SET', 6)),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'亚苏拉主任……\n'
				'这么说来，我记得她有说过\n'
				'自己有烦恼。{wait}'
				'{page}'
				'虽然我不清楚\n'
				'是怎样的烦恼。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('CALL', Function((2, 28))),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 8))), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('0x4B', Char(254), -1),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CAM_OFFSET', (760, 1000, -54540), 0),
			Insn('CAM_ROTATE', 52, 22, 0, 0),
			Insn('0x6E', 440, 0),
			Insn('CAM_DISTANCE', 21500, 0),
			Insn('CHAR_SET_POS', Char(254), (-450, 0, -53600), 180),
			Insn('CHAR_SET_POS', Char(257), (-1050, 0, -54800), 0),
			Insn('CHAR_SET_POS', Char(258), (150, 0, -54800), 0),
			Insn('CHAR_SET_POS', Char(259), (-1050, 0, -56000), 0),
			Insn('CHAR_SET_POS', Char(260), (150, 0, -56000), 0),
			Insn('CAM_DISTANCE', 19500, 1000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(254), Text(
				'啊！罗伊德，不好了！\n'
				'到处都找不到\n'
				'亚苏拉主任～！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'主任又睡过头\n'
				'这件事是真的吗！？{wait}'
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
				'#0012F不、这个嘛，还不晓得。\n'
				'话说，这是值得惊讶的事情？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'唉呀，真的呢。\n'
				'主任总是\n'
				'睡过头嘛～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'奇怪，那事件是指什么？\n'
				'大家都在讨论呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F今天早上开始，\n'
				'不管哪里都找不到亚苏拉主任，\n'
				'所以我们接下寻找她的委托。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0203F她有可能是失踪，\n'
				'或是卷入事件当中。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'啊──这样啊！\n'
				'原来是这么回事啊！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我总算知道\n'
				'从早上开始大家\n'
				'乱成一团的理由了～！{wait}'
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
			Insn('TEXT_TALK', Char(260), Text(
				'#0309F希伦该不会\n'
				'是个……少根筋的人？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_POS', Char(0), (-450, 0, -53600), 0),
			Insn('CHAR_SET_POS', Char(254), (-4330, 0, -55480), 180),
			Insn('0x4C', Char(254), -1),
			Insn('QUEST', 56, Insn('TASK_SET', 8)),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'我总算知道\n'
				'从早上开始大家\n'
				'乱成一团的理由了～！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯哼！太好了～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('CALL', Function((2, 29))),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 9))), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('0x4B', Char(254), -1),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CHAR_ROTATE', Char(254), 0, 0),
			Insn('CAM_OFFSET', (101970, 1000, -750), 0),
			Insn('CAM_ROTATE', 56, 22, 0, 0),
			Insn('0x6E', 440, 0),
			Insn('CAM_DISTANCE', 16000, 0),
			Insn('CHAR_SET_POS', Char(257), (101780, 0, -1010), 180),
			Insn('CHAR_SET_POS', Char(258), (102980, 0, -1010), 180),
			Insn('CHAR_SET_POS', Char(259), (101780, 0, 190), 180),
			Insn('CHAR_SET_POS', Char(260), (102980, 0, 190), 180),
			Insn('CAM_DISTANCE', 14000, 1000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(254), Text(
				'以我个人来说，\n'
				'我不认为\n'
				'主任在医院里。{wait}'
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
				'#0000F这是为什么呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你想，在医院里没办法\n'
				'悠闲地睡懒觉对吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'特别是最近，\n'
				'凯瑞教授似乎很啰唆的样子。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我想她可能是去\n'
				'可以悠闲睡懒觉的地方了吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F我想她有可能\n'
				'是失踪了，或是\n'
				'被卷入事件当中。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'是这样吗……\n'
				'主任的确老是在发呆，\n'
				'看起来很好诱旋。{wait}'
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
			Insn('TEXT_TALK', Char(254), Text(
				'不过，就算诱旋主任又能怎样……对吧？\n'
				'再说，她也没有神经质到\n'
				'会搞失踪啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0012F嗯，如果不是事件\n'
				'当然是最好的，不过……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x4C', Char(254), -1),
			Insn('QUEST', 56, Insn('TASK_SET', 9)),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'我想\n'
				'主任应该不是\n'
				'被卷入事件。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'她可能是去\n'
				'可以悠闲睡懒觉的地方了吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('CALL', Function((2, 30))),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 10))), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('0x4B', Char(254), -1),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CAM_OFFSET', (109680, 1000, -6130), 0),
			Insn('CAM_ROTATE', 56, 22, 0, 0),
			Insn('0x6E', 440, 0),
			Insn('CAM_DISTANCE', 16000, 0),
			Insn('CHAR_SET_POS', Char(254), (110000, 0, -4320), 180),
			Insn('CHAR_SET_POS', Char(257), (109400, 0, -5520), 0),
			Insn('CHAR_SET_POS', Char(258), (110600, 0, -5520), 0),
			Insn('CHAR_SET_POS', Char(259), (109400, 0, -6720), 0),
			Insn('CHAR_SET_POS', Char(260), (110600, 0, -6720), 0),
			Insn('CAM_DISTANCE', 14000, 1000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(254), Text(
				'#1300F啊，罗伊德！\n'
				'你接下寻找亚苏拉主任的\n'
				'委托了对吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#2P#0000F嗯，正是如此。\n'
				'虽然还不清楚状况就是了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'#1303F这样啊……真让人担心。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F赛西儿，\n'
				'如果你知道任何事的话，\n'
				'可以告诉我们吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'#1301F好啊。\n'
				'主任最近看起来\n'
				'好像在烦恼一些事。{wait}'
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
				'#2P#0001F烦恼是指……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'#1308F总是很悠闲的主任，\n'
				'这几天看起来\n'
				'很忧郁。{wait}'
				'{page}'
				'#1306F主任的工作是\n'
				'研究医疗装置，\n'
				'不过进展似乎不顺利。{wait}'
				'{page}'
				'#1303F凯瑞教授好像也有\n'
				'要求她说要快点\n'
				'提交报告的样子。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0103F因为研究进展不如预期而\n'
				'感到痛苦，所以搞失踪……{wait}'
				'{page}'
				'#0101F这种情况也是\n'
				'有可能的吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#2P#0001F现阶段虽然还不清楚……\n'
				'不过作为其中一种可能性，\n'
				'或许也是不无可能吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F好啊。继续进行调查吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_POS', Char(254), (110710, 0, -4320), 90),
			Insn('0x4C', Char(254), -1),
			Insn('QUEST', 56, Insn('TASK_SET', 10)),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'#1306F真担心\n'
				'亚苏拉主任……\n'
				'究竟为什么会失踪呢……{wait}'
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
				'#0012F还没有确定\n'
				'她是失踪哦，\n'
				'赛西儿姐姐……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F这里是研究所啊……\n'
		'非相关人士似乎不要进去比较好。\n'
		'去调查别的地方吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 13))), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F如果她走回来的话，可能会跟丢。\n'
				'我们搭乘巴士吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 12))), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F跟警备员打听看看吧。\n'
				'如果她离开医院的话，警备员应该会看到才对。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('EVENT_BEGIN', 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F打听得还不够多呢。\n'
				'再稍微跟大家\n'
				'打听一下吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 50),
			Insn('CHAR_SET_POS', Char(0), (-43600, 0, 0), 90),
			Insn('EVENT_END', 4),
		]),
	]),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CHAR_SET_POS', Char(257), (-9140, 0, 8220), 225),
	Insn('CHAR_SET_POS', Char(258), (-9140, 0, 7020), 315),
	Insn('CHAR_SET_POS', Char(259), (-10340, 0, 8220), 135),
	Insn('CHAR_SET_POS', Char(260), (-10340, 0, 7020), 45),
	Insn('CAM_OFFSET', (-7070, 1930, 1540), 0),
	Insn('CAM_ROTATE', 24, 23, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 42500, 0),
	Insn('CAM_OFFSET', (-8710, 1000, 8390), 5500),
	Insn('CAM_ROTATE', 45, 22, 0, 5000),
	Insn('CAM_DISTANCE', 19000, 6000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F嗯──在医院里\n'
		'没有看到主任呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F果然她人已经\n'
		'不在医院里了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F这个可能性很高。\n'
		'问题是她究竟在哪里。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F对了，如果是警备员的话……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (-42650, 850, 4180), 5000),
	Insn('CAM_ROTATE', 65, 14, 0, 5000),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F医院的警备是２４小时制。\n'
		'如果是在门口警备的人，\n'
		'说不定会知道什么……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F很好，去打听看看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0xB5', b'\x00\x05\x80\x00'),
	Insn('QUEST', 56, Insn('TASK_SET', 12)),
	Insn('CHAR_SET_POS', Char(0), (-10340, 0, 7020), 180),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 13))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'唉呀，是特务支援课的人。\n'
				'看你们大惊失色，发生什么事了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F嗯，其实是……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EVENT_BEGIN', 0),
			Insn('0x4B', Char(254), -1),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CHAR_ROTATE', Char(254), 270, 0),
			Insn('CHAR_SET_POS', Char(257), (-49370, 0, 4500), 90),
			Insn('CHAR_SET_POS', Char(258), (-49370, 0, 3300), 90),
			Insn('CHAR_SET_POS', Char(259), (-50570, 0, 4500), 90),
			Insn('CHAR_SET_POS', Char(260), (-50570, 0, 3300), 90),
			Insn('CAM_OFFSET', (-49130, 1000, 4340), 0),
			Insn('CAM_ROTATE', 44, 27, 0, 0),
			Insn('0x6E', 500, 0),
			Insn('CAM_DISTANCE', 17000, 0),
			Insn('CAM_DISTANCE', 15000, 1000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(254), Text(
				'#2P嗯。如果是亚苏拉主任的话，\n'
				'她今天早上出去了哦。{wait}'
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
			Insn('TEXT_TALK', Char(258), Text(
				'#4P#0100F果然没错……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#1P#0300F那么，你知道她去哪里了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'#2P她搭上了第一班巴士。\n'
				'只不过……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'#2P她似乎在\n'
				'思考些什么，跟她打招呼\n'
				'也没有回应呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#1P#0000F原来如此……\n'
				'谢谢你。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 257, 2, [
				Insn('CHAR_WATCH', Char(254), Char(260), 500),
			]),
			Insn('FORK', 258, 2, [
				Insn('CHAR_WATCH', Char(254), Char(259), 500),
			]),
			Insn('FORK', 259, 2, [
				Insn('CHAR_WATCH', Char(254), Char(258), 500),
			]),
			Insn('FORK', 260, 2, [
				Insn('CHAR_WATCH', Char(254), Char(257), 500),
			]),
			Insn('SLEEP', 300),
			Insn('FORK_AWAIT', Char(257), 2),
			Insn('FORK_AWAIT', Char(258), 2),
			Insn('FORK_AWAIT', Char(259), 2),
			Insn('FORK_AWAIT', Char(260), 2),
			Insn('TEXT_TALK', Char(257), Text(
				'#1P#0000F没有错，\n'
				'亚苏拉主任果然\n'
				'坐上巴士了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#4P#0100F这么一来……她应该是前往\n'
				'克洛斯贝尔市街了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#1P#0000F恐怕是吧。\n'
				'总之，我们也先回\n'
				'克洛斯贝尔一趟。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x4C', Char(254), -1),
			Insn('QUEST', 56, Insn('TASK_SET', 13)),
			Insn('CHAR_SET_POS', Char(0), (-49370, 0, 3900), 270),
			Insn('EVENT_END', 5),
		]),
		(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
			Insn('FLAG_SET', Flag(0)),
			Insn('TEXT_TALK', Char(254), Text(
				'亚苏拉主任的话，\n'
				'我记得她搭上\n'
				'第一班巴士啰。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我想她应该是去\n'
				'克洛斯贝尔了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'话说回来，发生什么事了吗？\n'
				'今天医院里\n'
				'似乎非常吵闹。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F这位警备员真是悠闲呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'亚苏拉主任的话，\n'
				'我记得她搭上\n'
				'第一班巴士啰。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我想她应该是去\n'
				'克洛斯贝尔了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('0x4B', Char(254), -1),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CHAR_ROTATE', Char(254), 135, 0),
			Insn('CHAR_SET_POS', Char(257), (-510, 0, -3910), 315),
			Insn('CHAR_SET_POS', Char(258), (310, 0, -3060), 315),
			Insn('CHAR_SET_POS', Char(259), (210, 0, -4580), 315),
			Insn('CHAR_SET_POS', Char(260), (1020, 0, -3750), 315),
			Insn('CAM_OFFSET', (110, 3360, -6720), 0),
			Insn('CAM_ROTATE', 4, 27, 0, 0),
			Insn('0x6E', 700, 0),
			Insn('CAM_DISTANCE', 10500, 0),
			Insn('CAM_DISTANCE', 8500, 1000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(254), Text(
		'穿着白衣的医师……？\n'
		'这么说来，\n'
		'早上巡逻时我有看到。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'我记得她是走向\n'
		'行政区的方向。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('0x4C', Char(254), -1),
			Insn('QUEST', 56, Insn('TASK_SET', 16)),
			Insn('EVENT_END', 5),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 17))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'欢迎光临！\n'
				'要不要来杯好喝的果汁呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F呃，我想打听一件事，\n'
				'你有在这附近看到\n'
				'穿着白衣的医师吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'穿着白衣……？\n'
				'啊，经你这么一说。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'今天早上的第一个客人，\n'
				'的确是这种感觉的人。{wait}'
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
			Insn('EVENT_BEGIN', 0),
			Insn('0x4B', Char(254), -1),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CAM_OFFSET', (4650, 4730, -3150), 0),
			Insn('CAM_ROTATE', 75, 27, 0, 0),
			Insn('0x6E', 700, 0),
			Insn('CAM_DISTANCE', 12500, 0),
			Insn('CHAR_SET_POS', Char(254), (6060, 2390, -3850), 315),
			Insn('CHAR_SET_POS', Char(257), (6170, 2390, -2570), 135),
			Insn('CHAR_SET_POS', Char(258), (5170, 2390, -3540), 135),
			Insn('CHAR_SET_POS', Char(259), (5070, 2390, -1660), 135),
			Insn('CHAR_SET_POS', Char(260), (4120, 2390, -2580), 135),
			Insn('CAM_OFFSET', (4650, 4530, -3150), 2000),
			Insn('CAM_ROTATE', 78, 19, 0, 2000),
			Insn('CAM_DISTANCE', 11000, 2000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(254), Text(
				'她好像有事要去\n'
				'图书馆的样子，\n'
				'但是来得有点太早了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'图书馆还没有开门。\n'
				'她说想吃点东西止饥，\n'
				'所以来我的摊贩。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(258), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(258), Text(
				'#0105F哎呀呀。但是，这里卖的是\n'
				'果汁对吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯。所以\n'
				'她很失望呢。\n'
				'肚子明明饿了～她这么说。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'于是，\n'
				'我告诉她在港湾区\n'
				'有卖食物的摊贩。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'在那之后，她就摇摇晃晃地\n'
				'走向港湾区了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0002F原来如此。\n'
				'非常感谢你。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(254), 3, Function((2, 18))),
			Insn('FORK', 257, 2, [
				Insn('CHAR_WATCH', Char(254), Char(260), 500),
			]),
			Insn('FORK', 258, 2, [
				Insn('CHAR_WATCH', Char(254), Char(259), 500),
			]),
			Insn('FORK', 259, 2, [
				Insn('CHAR_WATCH', Char(254), Char(258), 500),
			]),
			Insn('FORK', 260, 2, [
				Insn('CHAR_WATCH', Char(254), Char(257), 500),
			]),
			Insn('SLEEP', 300),
			Insn('FORK_AWAIT', Char(257), 2),
			Insn('FORK_AWAIT', Char(258), 2),
			Insn('FORK_AWAIT', Char(259), 2),
			Insn('FORK_AWAIT', Char(260), 2),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F主任似乎到\n'
				'港湾区去了呢。\n'
				'我们也去看看吧！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
			Insn('SLEEP', 1000),
			Insn('EMOTE_STOP', Char(257)),
			Insn('TEXT_TALK', Char(257), Text(
				'#0003F真奇怪……{wait}'
				'{page}'
				'#0001F亚苏拉主任因为有事\n'
				'到图书馆，所以\n'
				'才过来的吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0101F这么说也对……\n'
				'亚苏拉主任的目的地\n'
				'是图书馆吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F说不定是呢。{wait}'
				'{page}'
				'不过，总之她似乎\n'
				'先前往港湾区了。\n'
				'我们也赶快去吧！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_AWAIT', Char(254), 3),
			Insn('EXPR_VAR', 0, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
			Insn('QUEST', 56, Insn('TASK_SET', 17)),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'我的确有看到\n'
				'穿着白衣的人。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我想她应该是为了找\n'
				'卖食物的摊贩，所以才前往港湾区。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (4820, 2500, -5100), 1000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (6930, 2490, -6650), 1000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('CHAR_ROTATE', Char(254), 225, 800),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('0x4C', Char(254), -1),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 18))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天的面特别好吃哦！\n'
				'明明比较粗，却柔软的\n'
				'漂浮在汤中的面……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F请、请问。\n'
				'我们正在找人。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EVENT_BEGIN', 0),
			Insn('0x4B', Char(254), -1),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CHAR_SET_POS', Char(254), (-10000, 0, 13340), 270),
			Insn('CHAR_SET_POS', Char(257), (-11200, 0, 12740), 90),
			Insn('CHAR_SET_POS', Char(258), (-11200, 0, 13940), 90),
			Insn('CHAR_SET_POS', Char(259), (-12400, 0, 12740), 90),
			Insn('CHAR_SET_POS', Char(260), (-12400, 0, 13940), 90),
			Insn('CAM_OFFSET', (-12470, 2500, 12270), 0),
			Insn('CAM_ROTATE', 44, 27, 0, 0),
			Insn('0x6E', 500, 0),
			Insn('CAM_DISTANCE', 17000, 0),
			Insn('CAM_DISTANCE', 15000, 1000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(254), Text(
				'穿着白衣的女医师吗？\n'
				'她的确有来吃\n'
				'我们的面。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'看起来肚子似乎非常饿。\n'
				'就坐在那边的长椅上，\n'
				'津津有味地吃着面。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'在那之后的事情……我就不清楚了。\n'
				'毕竟后来有其他人点餐，\n'
				'我很拼命地在煮面呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这样啊。\n'
				'非常感谢你。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_POS', Char(254), (-10470, 0, 13340), 180),
			Insn('CHAR_SET_POS', Char(0), (-12000, 0, 13340), 180),
			Insn('0x4C', Char(254), -1),
			Insn('QUEST', 56, Insn('TASK_SET', 18)),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'穿着白衣的女医师吗？\n'
				'她的确有来吃\n'
				'我们的面。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'看起来肚子似乎非常饿。\n'
				'就坐在那边的长椅上，\n'
				'很专心地吃着面。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'在那之后的事情……我就不清楚了。\n'
				'毕竟后来有其他人点餐，\n'
				'我很拼命地在煮面呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 19))), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('0x4B', Char(254), -1),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CHAR_SET_POS', Char(254), (-2120, -800, 670), 315),
			Insn('CHAR_SET_POS', Char(257), (-2280, -800, 1880), 135),
			Insn('CHAR_SET_POS', Char(258), (-3350, -800, 880), 135),
			Insn('CHAR_SET_POS', Char(259), (-3100, -800, 2800), 135),
			Insn('CHAR_SET_POS', Char(260), (-4130, -800, 1800), 135),
			Insn('CAM_OFFSET', (-3460, 1800, 1490), 0),
			Insn('CAM_ROTATE', 2, 15, 0, 0),
			Insn('0x6E', 600, 0),
			Insn('CAM_DISTANCE', 17500, 0),
			Insn('CAM_DISTANCE', 15500, 1000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(254), Text(
				'穿白衣的人……？\n'
				'哦哦，我的确有看到。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'她坐在那边的长椅上，\n'
				'似乎在吃些什么。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'吃完之后，\n'
				'出现像是不良少年的人，\n'
				'她们似乎在说些什么。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'那位少年的确\n'
				'穿着蓝色的衣服。{wait}'
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
			Insn('TEXT_TALK', Char(258), Text(
				'#0105F咦……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F蓝色衣服的不良分子……\n'
				'是指圣约帮的人吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0301F这个可能性变高了呢。\n'
				'话说回来，为什么\n'
				'会跟他们扯上关系呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0101F该不会，\n'
				'她跟圣约帮之间\n'
				'也有什么纠纷的可能性……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(0), 0, 2000, (24, 27, 250, 0)),
			Insn('EMOTE', Char(1), 0, 2000, (24, 27, 250, 0)),
			Insn('EMOTE', Char(2), 0, 2000, (24, 27, 250, 0)),
			Insn('EMOTE', Char(3), 0, 2000, (24, 27, 250, 0)),
			Insn('SLEEP', 1000),
			Insn('EMOTE_STOP', Char(0)),
			Insn('EMOTE_STOP', Char(1)),
			Insn('EMOTE_STOP', Char(2)),
			Insn('EMOTE_STOP', Char(3)),
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F那么，白衣的人在那之后\n'
				'怎样了呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我也很在意，\n'
				'所以一直看着他们。\n'
				'结果……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_ROTATE', Char(254), 90, 500),
			Insn('CAM_OFFSET', (-2530, 2790, 1530), 3500),
			Insn('CAM_ROTATE', 80, 3, 0, 3500),
			Insn('SLEEP', 200),
			Insn('CHAR_ROTATE', Char(257), 90, 500),
			Insn('SLEEP', 100),
			Insn('FORK', 258, 2, [
				Insn('CHAR_ROTATE', Char(254), 90, 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 259, 2, [
				Insn('CHAR_ROTATE', Char(254), 90, 500),
			]),
			Insn('SLEEP', 30),
			Insn('FORK', 260, 2, [
				Insn('CHAR_ROTATE', Char(254), 90, 500),
			]),
			Insn('SLEEP', 300),
			Insn('FORK_AWAIT', Char(258), 2),
			Insn('FORK_AWAIT', Char(259), 2),
			Insn('FORK_AWAIT', Char(260), 2),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(254), Text(
				'他说这里会引人注目，\n'
				'就走向码头的方向了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0306F喂喂喂……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0103F我觉得好像真的开始\n'
				'有事件的嫌疑了呢。{wait}'
				'{page}'
				'#0101F怎么办？罗伊德？\n'
				'要去码头打听看看吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0201F或者直接前往\n'
				'圣约帮的基地，\n'
				'这也是一个办法。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0303F码头啊……\n'
				'希望她没有被装上重物\n'
				'沉到海里就好了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0011F他们又不是黑手党，\n'
				'应该不至于做到这种程度……{wait}'
				'{page}'
				'#0001F总之，我们先继续打听吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_POS', Char(254), (-4450, 0, -2110), 90),
			Insn('CHAR_SET_POS', Char(0), (-3140, -700, -540), 90),
			Insn('0x4C', Char(254), -1),
			Insn('QUEST', 56, Insn('TASK_SET', 19)),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'穿白衣的人……？\n'
				'哦哦，我的确有看到。{wait}'
				'{page}'
				'她坐在那边的长椅上，\n'
				'似乎在吃些什么。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'吃完之后，\n'
				'出现像是不良少年的人，\n'
				'带着她往码头的方向去了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'在那之后\n'
				'我就不知道了，不过\n'
				'那可不是一般的氛围……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 21))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'#0402F怎么了吗？\n'
				'找我有什么事吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F嗯，有点事。\n'
				'我就直说了。\n'
				'其实是……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EVENT_BEGIN', 0),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CHAR_SET_POS', Char(257), (-3460, 0, 11500), 45),
			Insn('CHAR_SET_POS', Char(258), (-2050, 0, 11190), 315),
			Insn('CHAR_SET_POS', Char(259), (-4260, 0, 10110), 45),
			Insn('CHAR_SET_POS', Char(260), (-2750, 0, 9940), 0),
			Insn('CAM_OFFSET', (-4090, 1670, 11450), 0),
			Insn('CAM_ROTATE', 73, 17, 0, 0),
			Insn('0x6E', 360, 0),
			Insn('CAM_DISTANCE', 19500, 0),
			Insn('CHAR_SET_FRAME', Char(254), 1),
			Insn('CAM_DISTANCE', 17500, 1000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(254), Text(
				'#1P#0409F啊哈哈哈！所以你才\n'
				'特地跑来\n'
				'这里啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#2P#0001F嗯。如果你知道什么的话，\n'
				'希望你告诉我。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'#1P#0400F和白衣人碰面的，\n'
				'恐怕是我们的成员吧。{wait}'
				'{page}'
				'#0402F在柜台那边工作的\n'
				'阿赛尔就是了。\n'
				'你去找他打听吧。{wait}'
				'{page}'
				'#0404F虽然可能听不到\n'
				'你们期待的回答就是了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#2P#0005F什么意思？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'#1P#0404F在圣约帮\n'
				'是禁止使用\n'
				'这类药品的。{wait}'
				'{page}'
				'因为没有\n'
				'任何好处呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 800),
			Insn('CHAR_ROTATE', Char(257), 0, 800),
			Insn('FORK', 259, 2, [
				Insn('CHAR_ROTATE', Char(254), 0, 800),
			]),
			Insn('SLEEP', 300),
			Insn('FORK_AWAIT', Char(259), 2),
			Insn('CAM_OFFSET', (-2460, 1670, 14780), 2000),
			Insn('CAM_ROTATE', 78, 20, 0, 2000),
			Insn('CAM_DISTANCE', 22000, 2000),
			Insn('TEXT_TALK', Char(254), Text(
				'#11P#0402F总之，详细内容\n'
				'你就找柜台那边的\n'
				'阿赛尔打听吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x6F', b'y'),
			Insn('CHAR_SET_POS', Char(0), (-4090, 0, 11450), 0),
			Insn('QUEST', 56, Insn('TASK_SET', 21)),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'#0404F在圣约帮\n'
				'是禁止使用\n'
				'这类药品的。{wait}'
				'{page}'
				'因为没有\n'
				'任何好处呢。{wait}'
				'{page}'
				'#0402F总之，详细内容\n'
				'你就找柜台那边的\n'
				'阿赛尔打听吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 22))), Insn('NOT'), Insn('END')]), [
			Insn('0x4B', Char(254), -1),
			Insn('TEXT_TALK', Char(254), Text(
				'什、什么事？\n'
				'警察找我要干嘛！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F嗯，其实是……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EVENT_BEGIN', 0),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CHAR_SET_POS', Char(254), (15530, 0, 8360), 270),
			Insn('CHAR_SET_POS', Char(257), (14330, 0, 7760), 90),
			Insn('CHAR_SET_POS', Char(258), (14330, 0, 8960), 90),
			Insn('CHAR_SET_POS', Char(259), (13130, 0, 7760), 90),
			Insn('CHAR_SET_POS', Char(260), (13130, 0, 8960), 90),
			Insn('CAM_OFFSET', (15530, 1100, 8360), 0),
			Insn('CAM_ROTATE', 39, 18, 0, 0),
			Insn('0x6E', 360, 0),
			Insn('CAM_DISTANCE', 27000, 0),
			Insn('CAM_DISTANCE', 25000, 1000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯。早上在码头\n'
				'跟亚苏拉小姐碰面的\n'
				'的确是我。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0101F呃，听说你从她那边\n'
				'收下了什么东西。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你们居然连这种事\n'
				'都知道啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……我拿的其实是\n'
				'止痛药。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0011F止、止痛药？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯。伤口虽然\n'
				'治好了，但是却会\n'
				'一直偏头痛。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'住院时我找她商量了一下，\n'
				'她就开药给我。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然我说我没有米拉，\n'
				'不过她说，\n'
				'这种程度就当成是额外服务。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然我也觉得\n'
				'不付米拉拿药不太好。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0105F原来是这样……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK', 257, 2, [
				Insn('CHAR_WATCH', Char(254), Char(260), 500),
			]),
			Insn('FORK', 258, 2, [
				Insn('CHAR_WATCH', Char(254), Char(259), 500),
			]),
			Insn('FORK', 259, 2, [
				Insn('CHAR_WATCH', Char(254), Char(258), 500),
			]),
			Insn('FORK', 260, 2, [
				Insn('CHAR_WATCH', Char(254), Char(257), 500),
			]),
			Insn('SLEEP', 300),
			Insn('FORK_AWAIT', Char(257), 2),
			Insn('FORK_AWAIT', Char(258), 2),
			Insn('FORK_AWAIT', Char(259), 2),
			Insn('FORK_AWAIT', Char(260), 2),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F看来，主任卖不好的药品\n'
				'给市街里的不良少年\n'
				'这条线索已经不成立了呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F那么，主任究竟来\n'
				'克洛斯贝尔做什么？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(254), 0, 2000, (0, 1, 250, 2)),
			Insn('SOUND_PLAY', 29, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(254), Text(
				'怎么，你们在找\n'
				'亚苏拉小姐吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(0), 0, 2000, (38, 38, 250, 1)),
			Insn('EMOTE', Char(1), 0, 2000, (38, 38, 250, 1)),
			Insn('EMOTE', Char(2), 0, 2000, (38, 38, 250, 1)),
			Insn('EMOTE', Char(3), 0, 2000, (38, 38, 250, 1)),
			Insn('SLEEP', 500),
			Insn('CHAR_ROTATE', Char(257), 90, 500),
			Insn('SLEEP', 100),
			Insn('FORK', 258, 2, [
				Insn('CHAR_ROTATE', Char(254), 90, 500),
			]),
			Insn('SLEEP', 50),
			Insn('FORK', 259, 2, [
				Insn('CHAR_ROTATE', Char(254), 90, 500),
			]),
			Insn('SLEEP', 30),
			Insn('FORK', 260, 2, [
				Insn('CHAR_ROTATE', Char(254), 90, 500),
			]),
			Insn('SLEEP', 300),
			Insn('FORK_AWAIT', Char(258), 2),
			Insn('FORK_AWAIT', Char(259), 2),
			Insn('FORK_AWAIT', Char(260), 2),
			Insn('TEXT_TALK', Char(254), Text(
				'她啊，她说\n'
				'她要去图书馆哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0011F图书馆！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯。她说有件事\n'
				'想调查一下。{wait}'
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
			Insn('SLEEP', 500),
			Insn('FORK', 257, 2, [
				Insn('CHAR_WATCH', Char(254), Char(260), 500),
			]),
			Insn('FORK', 258, 2, [
				Insn('CHAR_WATCH', Char(254), Char(259), 500),
			]),
			Insn('FORK', 259, 2, [
				Insn('CHAR_WATCH', Char(254), Char(258), 500),
			]),
			Insn('FORK', 260, 2, [
				Insn('CHAR_WATCH', Char(254), Char(257), 500),
			]),
			Insn('SLEEP', 300),
			Insn('FORK_AWAIT', Char(257), 2),
			Insn('FORK_AWAIT', Char(258), 2),
			Insn('FORK_AWAIT', Char(259), 2),
			Insn('FORK_AWAIT', Char(260), 2),
			Insn('TEXT_TALK', Char(258), Text(
				'#0106F原来如此……\n'
				'事情其实很单纯呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0006F似乎是这样呢。{wait}'
				'\n'
				'#0000F很好，去图书馆看看吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0206F嗯……总觉得\n'
				'我们在克洛斯贝尔市内\n'
				'四处奔波呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_POS', Char(254), (-4000, 0, 16690), 0),
			Insn('CHAR_SET_POS', Char(0), (13130, 0, 8060), 270),
			Insn('0x4C', Char(254), -1),
			Insn('QUEST', 56, Insn('TASK_SET', 22)),
			Insn('EVENT_END', 5),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'你们找亚苏拉小姐的话，\n'
				'她说她要去图书馆哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'她说有件事\n'
				'想调查一下。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('LOAD_CHCP', 'chr/ch32900', 30),
	Insn('CHAR_SET_POS', Char(257), (14590, 4000, 10280), 270),
	Insn('CHAR_SET_POS', Char(258), (14590, 4000, 9080), 270),
	Insn('CHAR_SET_POS', Char(259), (15790, 4000, 9080), 270),
	Insn('CHAR_SET_POS', Char(260), (15790, 4000, 10280), 270),
	Insn('CAM_OFFSET', (13950, 5020, 9560), 0),
	Insn('CAM_ROTATE', 32, 28, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 15500, 0),
	Insn('BGM_PLAY', b'j\x00\x00'),
	Insn('CAM_DISTANCE', 13500, 1000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(254), Text(
		'嗯……\n'
		'凯瑞教授真是的……\n'
		'不要那么生气……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'呼……呼……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F她很幸福地沉睡着呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F真是的，完全不晓得别人有多辛苦。\n'
		'喂──主任！\n'
		'醒醒啊──！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE_STOP', Char(254)),
	Insn('EMOTE', Char(254), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SOUND_PLAY', 612, 0, 0, 100),
	Insn('0x9C', Char(254), b'\x00\x00\x00\x00\x00\x00\x00\x00P\xfb\xff\xff\xe8\x03\x00\x00\xb8\x0b\x00\x00'),
	Insn('SOUND_PLAY', 830, 0, 0, 100),
	Insn('0x82', 100, 0, 3000, 300),
	Insn('SLEEP', 1000),
	Insn('CROSSFADE', 250),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('CHAR_SET_CHCP', Char(254), 30),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('CHAR_ROTATE', Char(254), 270, 0),
	Insn('0x0D'),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(254), 0, 2000, (40, 43, 100, 0)),
	Insn('TEXT_TALK', Char(254), Text(
		'嗯啊！\n'
		'是的！凯瑞教授！？\n'
		'我没睡！我没有睡着！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(254), 359, 900),
	Insn('SLEEP', 400),
	Insn('CHAR_ROTATE', Char(254), 181, 900),
	Insn('SLEEP', 400),
	Insn('CHAR_ROTATE', Char(254), 359, 900),
	Insn('SLEEP', 400),
	Insn('CHAR_ROTATE', Char(254), 181, 900),
	Insn('SLEEP', 400),
	Insn('EMOTE_STOP', Char(254)),
	Insn('CHAR_ROTATE', Char(254), 225, 900),
	Insn('SLEEP', 600),
	Insn('EMOTE', Char(254), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(254)),
	Insn('EMOTE', Char(254), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(254), Text(
		'……咦？是梦吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(254), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 500),
	Insn('CHAR_ROTATE', Char(254), 90, 500),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(254), Text(
		'嗯？你们是……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F我们是特务支援课的人。\n'
		'我们是为了寻找下落不明的\n'
		'亚苏拉主任而来的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(254), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(254), Text(
		'咦咦！？\n'
		'我下落不明吗！？{wait}'
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
		'#0100F上班日的早晨，\n'
		'突然不见人影的话，\n'
		'不论是谁都会这么觉得哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'哈哈哈！这怎么可能呢？\n'
		'我今天是休假……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'咦？仔细想想，\n'
		'我的休假似乎是明天……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'#5S糟了！#3S\n'
		'我把休假日记错了！{wait}'
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
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F你能理解现状\n'
		'实在是太好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(254), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'啊哈哈……对不起，\n'
		'是我太粗心了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'因为我想尽快到\n'
		'图书馆查资料，\n'
		'所以似乎搞错了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'你看，医院的书很少。\n'
		'连查资料都办不到，\n'
		'所以我很困扰呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'所以我才想说，\n'
		'下次休假要待在\n'
		'图书馆里看书。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 7))), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#0306F唉，结果是\n'
				'菲莉亚猜中了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0106F是寻找书本之旅呢。\n'
				'没想到那个\n'
				'真的会猜中……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F总之，医院里的大家\n'
		'都很担心你。{wait}'
		'{page}'
		'跟我们一起\n'
		'回去医院吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'啊哈哈，说的也是。\n'
		'……话说回来，\n'
		'你们觉得我会被骂吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F我不知道。\n'
		'不过，我想你最好\n'
		'做好心理准备。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(254), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(254), Text(
		'啊哈哈……唉……\n'
		'伤脑筋，凯瑞教授唠叨起来\n'
		'真是没完没了呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 1500),
	Insn('FLAG_SET', Flag(739)),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('QUEST', 56, Insn('TASK_SET', 24)),
	Insn('NEW_SCENE', 't1540', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('TEXT_TALK', Char(254), Text(
		'总之，\n'
		'多亏你们帮助了我。\n'
		'谢谢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('TEXT_TALK', Char(254), Text(
		'我本来还以为\n'
		'主任肯定被卷入\n'
		'什么事件了……{wait}'
		'{page}'
		'看起来似乎是\n'
		'我会错意了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('TEXT_TALK', Char(254), Text(
		'亚苏拉前辈\n'
		'究竟去哪了？{wait}'
		'{page}'
		'该不会，\n'
		'因为每天都被凯瑞教授说教，\n'
		'所以真的感到厌烦了吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('TEXT_TALK', Char(254), Text(
		'主任真会\n'
		'给人添麻烦呢。{wait}'
		'{page}'
		'不过，这次肯定\n'
		'会被凯瑞教授\n'
		'好好教训一顿吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][28] = [
	Insn('TEXT_TALK', Char(254), Text(
		'总之，有找到主任\n'
		'真是太好了～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'不过，各位护理师\n'
		'其实也没有\n'
		'那么担心哦，呵呵！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][29] = [
	Insn('TEXT_TALK', Char(254), Text(
		'毕竟主任的\n'
		'脱线程度，说不定比\n'
		'希伦还要高呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][30] = [
	Insn('TEXT_TALK', Char(254), Text(
		'#1300F总之，亚苏拉主任\n'
		'没事就好了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 300, 1600, (54, 57, 250, 0)),
	Insn('SOUND_PLAY', 892, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(260)),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F赛西儿的温柔笑容……\n'
		'简直就像天使一样呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]
