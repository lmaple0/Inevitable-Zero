# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't4010',
	'name2': 't4010',
	'location': 93,
	'bgm': 124,
	'flags': 8192,
	'includes': [
		None,
		None,
		None,
		None,
		None,
		None,
	],
	'name3': 't4010_1',
	'labels': [],
	'chcp': [],
	'npcs': [],
	'monsters': [],
	'triggers': [],
	'objects': [],
	'unk13': b'\x00\xff\xff',
	'extra': None,
	'code': [None]*30,
	'anim': [],
}

data['code'][0] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('CALL', Function((1, 4))),
		]),
		(None, [
			Insn('EVENT_BEGIN', 0),
			Insn('CROSSFADE', 500),
			Insn('CAM_OFFSET', (152600, 3700, 16650), 0),
			Insn('CAM_ROTATE', 322, 28, 0, 0),
			Insn('0x6E', 300, 0),
			Insn('CAM_DISTANCE', 29870, 0),
			Insn('CHAR_ROTATE', Char(12), 90, 0),
			Insn('CHAR_SET_POS', Char(257), (153300, 200, 16500), 270),
			Insn('CHAR_SET_POS', Char(258), (153300, 200, 17700), 270),
			Insn('CHAR_SET_POS', Char(259), (154500, 200, 16500), 270),
			Insn('CHAR_SET_POS', Char(260), (154500, 200, 17700), 270),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(4), 128),
					Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
					Insn('CHAR_SET_POS', Char(265), (155700, 200, 17100), 270),
				]),
				(None, []),
			]),
			Insn('0x4B', Char(12), -1),
			Insn('CHAR_SET_FRAME', Char(12), 0),
			Insn('CAM_OFFSET', (152600, 1700, 16650), 2000),
			Insn('CAM_DISTANCE', 27870, 2000),
			Insn('0x0D'),
			Insn('EMOTE', Char(12), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('0x6F', b'y'),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('TASK_GET', 0))), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(12), Text(
						'哎呀呀，你们几位……\n'
						'是看到委托而来的吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F是的。似乎又是要在主日学校\n'
						'担任特别老师的委托呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'嗯。托各位之前上课的福，\n'
						'学生们似乎对\n'
						'警察的工作产生兴趣了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'罗伊德老师的授课\n'
						'评价似乎也很好。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'所以，\n'
						'我希望你务必\n'
						'再次前来授课。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F能对警察的活动内容\n'
						'产生兴趣的话，\n'
						'我们也会很感谢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'听你这么说，我就放心了。\n'
						'如何？主日学校的老师委托，\n'
						'你愿意再度接下吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('QUEST', 57, Insn('TASK_SET', 0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(12), Text(
						'哎呀呀。代课老师的\n'
						'委托……你愿意\n'
						'接下了吗？{wait}'
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
						'#0006F不好意思。\n'
						'目前还有其他调查工作……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'这样啊。\n'
						'如果有其他工作的话，那也没办法。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'如果你能抽出时间的话，\n'
						'请再过来找我。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_SET_POS', Char(0), (153260, 200, 16760), 270),
				]),
				(None, [
					Insn('CALL', Function((1, 1))),
					Insn('CALL', Function((1, 2))),
					Insn('CALL', Function((1, 3))),
					Insn('CHAR_SET_POS', Char(0), (5570, 0, 1350), 90),
					Insn('CHAR_SET_POS', Char(12), (150800, 200, 17500), 180),
				]),
			]),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
					Insn('CHAR_FLAG1_SET', Char(4), 128),
					Insn('CHAR_FLAG2_SET', Char(4), 32768),
				]),
				(None, []),
			]),
			Insn('0x4C', Char(12), -1),
			Insn('EVENT_END', 5),
		]),
	]),
	Insn('RETURN'),
]

data['code'][1] = [
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F我知道了。\n'
		'如果孩子们能对警察和\n'
		'防止犯罪有兴趣的话……{wait}'
		'{page}'
		'#0002F我想我们站在讲台上\n'
		'也有意义了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0309F不过，罗伊德还真是辛苦呢──\n'
		'哪像我，光想到\n'
		'要教小孩就……{wait}'
		'{page}'
		'#0310F该怎么说，\n'
		'屁股附近感觉很痒……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0211F兰迪你太下流了。{wait}'
		'{page}'
		'#0206F……话虽如此，\n'
		'我也不太擅长跟小孩相处，\n'
		'所以我能明白你想说什么。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F真是的，你们两个。\n'
		'启蒙活动也是\n'
		'警察重要的工作之一哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F我也觉得艾莉说得对。\n'
		'总之，请让我们尽全力\n'
		'完成这分委托。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'听你这么说，\n'
		'我就放心了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'那么，就麻烦各位了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 80, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'开始进行{color 2}任务【续丄主日学校的特别老师】{color 0}！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('SLEEP', 500),
	Insn('CAM_OFFSET', (7710, 2300, -90), 0),
	Insn('CAM_ROTATE', 315, 25, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 26410, 0),
	Insn('CHAR_SET_POS', Char(257), (7600, 0, 1320), 270),
	Insn('CHAR_SET_POS', Char(258), (5570, 0, 1350), 90),
	Insn('CHAR_SET_POS', Char(259), (4380, 0, 2050), 90),
	Insn('CHAR_SET_POS', Char(260), (4720, 0, 510), 90),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(265), (7510, 0, 3100), 180),
		]),
		(None, []),
	]),
	Insn('SLEEP', 500),
	Insn('CAM_DISTANCE', 25410, 1000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('EMOTE_STOP', Char(12)),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0001F那么，\n'
		'关于上课内容，\n'
		'这次我想稍微改变方向。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F上次是怎样的\n'
				'感觉呢……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F像是警察组织和\n'
				'基本理念……把这些内容\n'
				'浅显易懂地说明给他们听。{wait}'
				'{page}'
				'#0103F这个嘛……\n'
				'与其用同样的上课内容，\n'
				'变更内容应该会比较好……{wait}'
				'{page}'
				'#0102F罗伊德，具体来说\n'
				'你打算怎么做呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F上次是教了\n'
				'怎样的内容呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F是的。关于警察组织的各种事情，\n'
				'还有用举例的方式……{wait}'
				'{page}'
				'#0202F简单来说，\n'
				'就是用问答的方式。{wait}'
				'{page}'
				'#0205F同样的事情做两次也很无趣，\n'
				'所以我同意变更，不过……\n'
				'要改成什么呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F上次是教了\n'
				'怎样的内容呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0302F总之，就是关于警察的\n'
				'各种事情吧。{wait}'
				'{page}'
				'#0304F组织是怎样的、\n'
				'战术导力器的介绍，\n'
				'总之，有各种内容。{wait}'
				'{page}'
				'#0300F要改内容是没问题，\n'
				'不过你有什么好主意吗，\n'
				'罗伊德？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F嗯。我想要教具体的\n'
		'警察活动内容。{wait}'
		'{page}'
		'#0003F比方说，当某种犯罪\n'
		'实际发生的时候……{wait}'
		'{page}'
		'#0000F简单说明\n'
		'从犯罪发生到\n'
		'逮捕犯人的过程。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F原来如此。就是实务内容呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F同时也有提高孩子们\n'
		'防止犯罪意识的目的对吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F嗯。这主意不错吧？\n'
		'虽然罗伊德老师\n'
		'可能会很辛苦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F关于这部分……{wait}'
		'{page}'
		'#0002F这次我想\n'
		'让大家也以\n'
		'老师身分参加。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#0105F咦？我们也要吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0009F嗯。站上讲台当老师\n'
		'会是一个很好的经验。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0205F居然要当老师，\n'
		'我没什么自信呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0303F嗯──没想到我居然会有\n'
		'站在讲台上的一天……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F那么，要怎么\n'
		'进行分工呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0001F通报、初期行动、推理、逮捕。\n'
		'这４个项目，\n'
		'我想让大家各自负责一个。{wait}'
		'{page}'
		'#0002F大家可以告诉我\n'
		'自己擅长的部分吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0101F这个嘛……\n'
		'『初期行动』的话，我想我应该能教。\n'
		'再来就是『通报』吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0301F我想想哦。\n'
		'我不擅长『推理』……\n'
		'也不知道能不能好好说明『通报』……{wait}'
		'{page}'
		'#0309F这样吧，可以的话，\n'
		'我想负责『逮捕』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0203F我的话……\n'
		'我想我能教『通报』吧。{wait}'
		'{page}'
		'还有『推理』的话，应该还可以……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0004F我知道了。\n'
		'那么，上课过程中我会\n'
		'依序指名大家，就拜托你们了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'各位，你们差不多\n'
		'准备好了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 90, 500),
	Insn('SLEEP', 800),
	Insn('TEXT_TALK', Char(257), Text(
		'#0002F我知道了。{wait}'
		'\n'
		'#0000F那么，大家开始上课吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('0x97', Char(254), (3000, 0, 1000), 1000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x97', Char(254), (3000, 0, 1000), 1000, 0),
	]),
	Insn('SLEEP', 150),
	Insn('FORK', 259, 1, [
		Insn('0x97', Char(254), (3000, 0, 0), 1000, 0),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 260, 1, [
		Insn('0x97', Char(254), (3000, 0, 1200), 1000, 0),
	]),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('SLEEP', 500),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('LOAD_CHCP', 'chr/ch21400', 30),
	Insn('LOAD_CHCP', 'chr/ch34200', 31),
	Insn('LOAD_CHCP', 'chr/ch21500', 32),
	Insn('CAM_OFFSET', (151700, 1500, 4100), 0),
	Insn('CAM_ROTATE', 315, 23, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 29780, 0),
	Insn('CHAR_SET_POS', Char(12), (150800, 200, 17500), 180),
	Insn('CHAR_SET_POS', Char(257), (155600, 200, 16300), 270),
	Insn('CHAR_SET_POS', Char(258), (155600, 200, 17500), 270),
	Insn('CHAR_SET_POS', Char(259), (156800, 200, 16300), 270),
	Insn('CHAR_SET_POS', Char(260), (156800, 200, 17500), 270),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(265), (150910, 0, 1530), 0),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_CHCP', Char(19), 30),
	Insn('CHAR_SET_POS', Char(19), (150600, 0, 4100), 90),
	Insn('CHAR_SET_CHCP', Char(20), 31),
	Insn('CHAR_SET_POS', Char(20), (151800, 0, 4100), 270),
	Insn('CHAR_SET_CHCP', Char(30), 32),
	Insn('CHAR_SET_POS', Char(30), (148640, 0, 8000), 180),
	Insn('CHAR_SET_CHCP', Char(25), 6),
	Insn('CHAR_SET_POS', Char(25), (153930, 0, 14010), 135),
	Insn('CHAR_SET_FRAME', Char(29), 1),
	Insn('CHAR_SET_FRAME', Char(27), 2),
	Insn('CHAR_SET_FRAME', Char(28), 1),
	Insn('FORK_FUNC', Char(27), 1, Function((1, 27))),
	Insn('FORK_FUNC', Char(19), 1, Function((1, 27))),
	Insn('SLEEP', 150),
	Insn('FORK_FUNC', Char(28), 1, Function((1, 27))),
	Insn('FORK_FUNC', Char(26), 1, Function((1, 27))),
	Insn('SLEEP', 150),
	Insn('FORK_FUNC', Char(30), 1, Function((1, 27))),
	Insn('SLEEP', 150),
	Insn('FORK_FUNC', Char(20), 1, Function((1, 27))),
	Insn('SLEEP', 150),
	Insn('FORK_FUNC', Char(29), 1, Function((1, 27))),
	Insn('SLEEP', 150),
	Insn('FORK_FUNC', Char(25), 1, Function((1, 27))),
	Insn('CAM_OFFSET', (150830, 1500, 8890), 5000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('FORK_QUIT', Char(27), 1),
	Insn('FORK_QUIT', Char(28), 1),
	Insn('FORK_QUIT', Char(19), 1),
	Insn('FORK_QUIT', Char(26), 1),
	Insn('FORK_QUIT', Char(30), 1),
	Insn('FORK_QUIT', Char(20), 1),
	Insn('FORK_QUIT', Char(29), 1),
	Insn('FORK_QUIT', Char(25), 1),
	Insn('FORK_FUNC', Char(19), 1, Function((1, 28))),
	Insn('TEXT_TALK', Char(12), Text(
		'#3P#5S好，大家安静。\n'
		'坐到座位上。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_QUIT', Char(19), 1),
	Insn('EMOTE', Char(19), 0, 1700, (40, 43, 100, 0)),
	Insn('EMOTE', Char(20), 0, 1700, (40, 43, 100, 0)),
	Insn('EMOTE', Char(26), 0, 1700, (14, 15, 250, 2)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(29), 0, 1700, (8, 9, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('EMOTE', Char(30), 0, 1700, (40, 43, 100, 0)),
	Insn('EMOTE', Char(25), 0, 1700, (40, 43, 100, 0)),
	Insn('FORK_FUNC', Char(19), 3, Function((1, 23))),
	Insn('FORK_FUNC', Char(20), 3, Function((1, 24))),
	Insn('FORK_FUNC', Char(30), 3, Function((1, 25))),
	Insn('FORK_FUNC', Char(25), 3, Function((1, 26))),
	Insn('CHAR_SET_FRAME', Char(29), 0),
	Insn('CAM_OFFSET', (151860, 1500, 10590), 5000),
	Insn('SLEEP', 300),
	Insn('CHAR_SET_FRAME', Char(28), 0),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(27), 0),
	Insn('0x6F', b'\x01'),
	Insn('FORK_AWAIT', Char(19), 3),
	Insn('SLEEP', 2000),
	Insn('TEXT_TALK', Char(12), Text(
		'那么──今天我想\n'
		'再让大家学习一些\n'
		'有关警察的事情。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 11))),
	Insn('FORK_FUNC', Char(258), 3, Function((1, 12))),
	Insn('FORK_FUNC', Char(259), 3, Function((1, 13))),
	Insn('FORK_FUNC', Char(260), 3, Function((1, 14))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('CHAR_SET_POS', Char(257), (147500, 200, 16300), 180),
	Insn('CHAR_SET_POS', Char(258), (149250, 200, 16300), 180),
	Insn('CHAR_SET_POS', Char(259), (152750, 200, 16300), 180),
	Insn('CHAR_SET_POS', Char(260), (154500, 200, 16300), 180),
	Insn('TEXT_TALK', Char(12), Text(
		'老师则是……\n'
		'应该有人认识他们吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'咦？是警察吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(20), Text(
		'该不会，大哥哥你们\n'
		'要当老师吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F嗯。那就拜托你们啰。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (40, 43, 100, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (40, 43, 100, 0)),
	Insn('CAM_OFFSET', (152120, 1700, 16059), 3000),
	Insn('CAM_ROTATE', 315, 28, 0, 3000),
	Insn('CAM_DISTANCE', 33000, 3000),
	Insn('0x6F', b'y'),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('TEXT_TALK', Char(258), Text(
		'#0112F（这还真是……不好意思呢。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0201F（嗯……真让人坐立难安。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F（被小朋友们\n'
		'\u3000正面盯着看……\n'
		'\u3000还真是耀眼呢。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'今天除了罗伊德老师之外，\n'
		'还有其他老师。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'我向大家介绍哦。\n'
		'艾莉老师、缇欧老师跟\n'
		'兰迪老师。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F我是艾莉。\n'
		'大家好，今天还请\n'
		'多多指教。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0209F我是缇欧。\n'
		'呃……一起快乐地学习吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0309F我叫兰迪。\n'
		'今天一整天请多指教啦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (151860, 1500, 10590), 2000),
	Insn('CAM_ROTATE', 315, 23, 0, 2000),
	Insn('0x6E', 300, 2000),
	Insn('CAM_DISTANCE', 29780, 2000),
	Insn('EMOTE', Char(27), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(28), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(19), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(20), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(25), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(26), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(29), 0, 1700, (24, 27, 250, 0)),
	Insn('EMOTE', Char(30), 0, 1700, (24, 27, 250, 0)),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(27)),
	Insn('EMOTE_STOP', Char(28)),
	Insn('EMOTE_STOP', Char(19)),
	Insn('EMOTE_STOP', Char(20)),
	Insn('EMOTE_STOP', Char(25)),
	Insn('EMOTE_STOP', Char(26)),
	Insn('EMOTE_STOP', Char(29)),
	Insn('EMOTE_STOP', Char(30)),
	Insn('SLEEP', 1000),
	Insn('CHAR_FLAG1_SET', Char(258), 8192),
	Insn('CHAR_FLAG1_SET', Char(25), 8192),
	Insn('0x7D', b'ddd\x00\xe8\x03\x00\x00'),
	Insn('TEXT_TALK', Char(25), Text(
		'那位可爱的大姐姐，\n'
		'看起来一点也不厉害。\n'
		'应该不是警察吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (40, 43, 100, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(258)),
	Insn('TEXT_TALK', Char(258), Text(
		'#0109F啊哈哈……\n'
		'应该不是警察\n'
		'是指我吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_UNSET', Char(258), 8192),
	Insn('CHAR_FLAG1_UNSET', Char(25), 8192),
	Insn('CHAR_FLAG1_SET', Char(259), 8192),
	Insn('CHAR_FLAG1_SET', Char(29), 8192),
	Insn('TEXT_TALK', Char(29), Text(
		'#3P我说啊。\n'
		'你个子明明这么小，\n'
		'有办法当老师吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(259), Text(
		'#0209F个、个子小……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_UNSET', Char(259), 8192),
	Insn('CHAR_FLAG1_UNSET', Char(29), 8192),
	Insn('CHAR_FLAG1_SET', Char(260), 8192),
	Insn('CHAR_FLAG1_SET', Char(26), 8192),
	Insn('TEXT_TALK', Char(26), Text(
		'#2P这个人明明是老师，\n'
		'看起来却像不良分子！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(260), Text(
		'#3P#0301F嗯？在我们当中哪有人\n'
		'像是不良分子……{wait}'
		'{page}'
		'#0305F#5S……是说我吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_UNSET', Char(260), 8192),
	Insn('CHAR_FLAG1_UNSET', Char(26), 8192),
	Insn('0x7D', b'\xff\xff\xff\x00\xe8\x03\x00\x00'),
	Insn('TEXT_TALK', Char(12), Text(
		'好了好了，大家安静！\n'
		'关于警察的工作，今天\n'
		'各位老师会教我们更详细的内容。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'大家要好好\n'
		'学习哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_SET_POS', 100, 100, -1, -1),
	Insn('TEXT_SET_NAME', Translate('孩子们')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 0}#5S好～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('0x5A'),
	Insn('CHAR_WATCH', Char(12), Char(257), 300),
	Insn('TEXT_TALK', Char(12), Text(
		'那就万事拜托了。\n'
		'罗伊德老师㈱{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(12), 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F啊，好的。\n'
		'我知道了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 15))),
	Insn('CHAR_ROTATE', Char(12), 270, 300),
	Insn('0x95', Char(12), (146430, 200, 17490), 2000, 0),
	Insn('CHAR_ROTATE', Char(12), 135, 300),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('TEXT_TALK', Char(257), Text(
		'#0012F（嗯……\n'
		'\u3000不管多少次，站上讲台时\n'
		'\u3000还是会紧张呢……）{wait}'
		'{page}'
		'#0000F嗯哼。\n'
		'那么，我们这就\n'
		'开始上课吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 2000),
	Insn('CAM_OFFSET', (151090, 1500, 15660), 3000),
	Insn('CAM_ROTATE', 0, 10, 0, 3000),
	Insn('CAM_DISTANCE', 32470, 3000),
	Insn('0x6F', b'\x01'),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'o\x00\x00'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}\u3000\u3000\u3000开始上课！\n'
		'～关于警察的活动～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}※在各项目挑选\n'
		'\u3000最适合的老师，\n'
		'\u3000让特别课堂成功吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F那么，今天就……\n'
		'针对具体的警察活动内容\n'
		'来学习吧。{wait}'
		'{page}'
		'#0013F在这广阔的克洛斯贝尔当中\n'
		'找出坏人，然后一直到\n'
		'逮捕为止的过程。{wait}'
		'{page}'
		'警察的活动内容，虽然可能\n'
		'只有『逮捕』很明显，不过……{wait}'
		'{page}'
		'#0000F直到逮捕之前，\n'
		'还是会有各种活动。{wait}'
		'{page}'
		'首先是关于『通报』……\n'
		'就让我们来说明\n'
		'这是什么。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}逮捕犯人的第一步！\n'
		'『通报』究竟是什么！？\n'
		'要说明这个项目的是……{0x18}{wait}'
	)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, 200, 0, Text(
		'【①艾莉老师】\n'
		'【②缇欧老师】\n'
		'【③兰迪老师】\n'
		'【④罗伊德老师】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 3), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F请艾莉老师来说明。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(258), 3, Function((1, 19))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(258), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(258), Text(
				'#0101F是的。『通报』指的是，\n'
				'发生事件……像是看到\n'
				'偷窃或交通意外的时候……{wait}'
				'{page}'
				'#0100F由我们去通知警察的\n'
				'这个动作。{wait}'
				'{page}'
				'根据这个『通报』，\n'
				'我们会开始进行调查。{wait}'
				'{page}'
				'#0103F如果大家有看到\n'
				'有人正在做坏事，或是\n'
				'发生交通意外的时候……{wait}'
				'{page}'
				'#0102F就要马上通报警察哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 300),
			Insn('0x82', 100, 0, 3000, 300),
			Insn('TEXT_SET_POS', -1, 150, -1, -1),
			Insn('TEXT_SET_NAME', Translate('孩子们')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 0}#5S好～！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_SET_POS', 14, 280, 60, 3),
			Insn('0x5A'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0109F（嗯。有好好地\n'
				'\u3000说明呢。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F请缇欧老师来说明。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0207F我、我知道了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(259), 3, Function((1, 20))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(259), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(259), Text(
				'#0201F呃……『通报』指的是，\n'
				'回报警察机构发生\n'
				'犯罪或意外的行为。{wait}'
				'{page}'
				'#0203F警察组织了以导力网络\n'
				'为主、能够迅速因应\n'
				'市民通报的系统。{wait}'
				'{page}'
				'#0201F此外……警察总部２４小时\n'
				'都有人员驻守，\n'
				'能够处理市民的通报。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(27), Text(
				'嗯──\n'
				'我大概算是懂了吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F（要是能再说得\n'
				'\u3000更浅显易懂一点就好了……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		2: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F请兰迪老师来说明。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(260), Text(
				'#0305F喂，一开始就叫我吗！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(260), 3, Function((1, 21))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(260), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F呃，也就是说……\n'
				'所谓的『通报』，\n'
				'指的就是找警察告密。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(29), Text(
				'老师！告密是什么？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0310F咦！？{wait}'
				'{page}'
				'#0309F那是，呃……\n'
				'就是告诉警察说\n'
				'有人在做坏事的意思。{wait}'
				'{page}'
				'#0304F没有犯人的话，\n'
				'就没办法开始调查了。{wait}'
				'{page}'
				'#0303F所以，看到可疑的人，\n'
				'总之只要先『通报』……{wait}'
				'{page}'
				'视情况不同，\n'
				'会找出犯人……{wait}'
				'#0309F也说不定。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 16))),
			Insn('TEXT_TALK', Char(260), Text(
				'#0310F（……我好像说出了一件\n'
				'\u3000非常不得了的事。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		3: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0002F这就由我来说明吧。{wait}'
				'{page}'
				'#0001F通报指的是，看到犯罪、\n'
				'事件、意外等情况的时候，\n'
				'通知警察的动作。{wait}'
				'{page}'
				'只要是住在克洛斯贝尔的人，\n'
				'都有所谓的通报义务……{wait}'
				'{page}'
				'如果看到犯罪或事件，\n'
				'必须要迅速通报。{wait}'
				'{page}'
				'#0003F通报的时候，什么时候、在哪里、\n'
				'发生什么事，犯人的特征和逃亡方向\n'
				'之类的情报都很重要。{wait}'
				'{page}'
				'除此之外，\n'
				'还要报告详细的被害状况、\n'
				'通报者姓名、联系方式。{wait}'
				'{page}'
				'#0009F大家懂了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(25), Text(
				'不懂──{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 16))),
			Insn('TEXT_TALK', Char(257), Text(
				'#0012F（糟糕。\n'
				'\u3000我可能说得太详细了……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 29))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 17))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0004F关于『通报』，\n'
		'大概就是这样吧。{wait}'
		'{page}'
		'#0000F那么接下来，\n'
		'『什么时候该进行通报』\n'
		'这部分……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}什么时候该进行\n'
		'通报呢？\n'
		'要说明这个项目的是……{0x18}{wait}'
	)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, 200, 0, Text(
		'【①艾莉老师】\n'
		'【②缇欧老师】\n'
		'【③兰迪老师】\n'
		'【④罗伊德老师】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这个就请艾莉老师\n'
				'来说明吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0105F我、我吗？{wait}'
				'{page}'
				'#0113F……我知道了。嗯、嗯哼。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(258), 3, Function((1, 19))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(258), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F平常在街上，\n'
				'我们警察\n'
				'会进行巡逻。{wait}'
				'{page}'
				'#0108F但是，警察因为裁员等原因，\n'
				'没有足够的人手。{wait}'
				'{page}'
				'#0103F此外，就算在警察内部，\n'
				'各单位之间也有势力均衡，\n'
				'也有无法自由行动的状况。{wait}'
				'{page}'
				'#0100F因此，只要有\n'
				'居民的『通报』，警察就能\n'
				'迅速前往现场。{wait}'
				'{page}'
				'#0109F像这样，\n'
				'来自居民的『通报』\n'
				'是非常重要的。{wait}'
				'{page}'
				'#0113F（虽然我觉得\n'
				'\u3000没有说错……不过总觉得\n'
				'\u3000说了多余的事情……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 3), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这个就请缇欧老师\n'
				'来说明吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0203F我知道了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(259), 3, Function((1, 20))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(259), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F『通报』指的是，\n'
				'发现犯罪或意外的时候，\n'
				'告诉警察的行为。{wait}'
				'{page}'
				'除此之外，\n'
				'觉得『有点奇怪』的时候，\n'
				'也请告诉警察。{wait}'
				'{page}'
				'#0201F像是听到很大的声音、\n'
				'某个地方有大声吵架的人们，\n'
				'诸如此类的情况。{wait}'
				'{page}'
				'能够尽早通报，\n'
				'说不定就能防止\n'
				'事件或犯罪发生。{wait}'
				'{page}'
				'#0203F大家懂了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('SLEEP', 300),
			Insn('0x82', 100, 0, 3000, 300),
			Insn('TEXT_SET_POS', -1, 150, -1, -1),
			Insn('TEXT_SET_NAME', Translate('孩子们')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 0}#5S好～！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_SET_POS', 14, 280, 60, 3),
			Insn('0x5A'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0204F（看来，我似乎\n'
				'\u3000成功完成任务了……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		2: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这个就请兰迪老师\n'
				'来说明吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(260), Text(
				'#0305F居然是我！\n'
				'……唔，真没办法……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(260), 3, Function((1, 21))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(260), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(260), Text(
				'#0304F呃，这个嘛……\n'
				'总之，我想只要看到\n'
				'可疑的家伙就全部都通报吧。{wait}'
				'{page}'
				'#0307F看到在做坏事的人\n'
				'就马上通报，看起来像做坏事的人\n'
				'也先通报……{wait}'
				'{page}'
				'#0309F可疑的家伙当然也要通报。\n'
				'在这当中，如果运气不错有坏人的话，\n'
				'调查就能进行到下一阶段。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(26), Text(
				'那，因为兰迪老师看起来像\n'
				'不良分子，所以我可以去通报吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 16))),
			Insn('TEXT_TALK', Char(260), Text(
				'#0305F咦！？\n'
				'不要啦，饶了我吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		3: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F这就由我来说明吧。{wait}'
				'{page}'
				'住在克洛斯贝尔的人，\n'
				'都有所谓的通报义务。{wait}'
				'{page}'
				'这是指看到犯罪、事件\n'
				'或意外的情况下，\n'
				'必须要迅速通报警察。{wait}'
				'{page}'
				'#0003F虽然也有例外，\n'
				'不过基本上，没有『通报』的话，\n'
				'我们警察也无法行动。{wait}'
				'{page}'
				'#0000F所以，居民的协助\n'
				'是必须的。\n'
				'大家懂了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_SET_POS', -1, 150, -1, -1),
			Insn('TEXT_SET_NAME', Translate('孩子们')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 0}#5S太难了，\n'
				'听不太懂──！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('TEXT_SET_POS', 14, 280, 60, 3),
			Insn('0x5A'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 16))),
			Insn('TEXT_TALK', Char(257), Text(
				'#0011F（唔……！我也觉得，\n'
				'\u3000的确是用了有点困难的\n'
				'\u3000单字……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 29))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 17))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0003F那么，接到来自居民的\n'
		'『通报』之后，接下来警察\n'
		'就要开始调查了。{wait}'
		'{page}'
		'#0001F这叫做『初期行动』，\n'
		'在调查当中也是\n'
		'很重要的一环。{wait}'
		'{page}'
		'#0000F『初期行动』，也就是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}总算可以实际行动了！\n'
		'关于『初期行动』，\n'
		'要负责上课的是……{0x18}{wait}'
	)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, 200, 0, Text(
		'【①艾莉老师】\n'
		'【②缇欧老师】\n'
		'【③兰迪老师】\n'
		'【④罗伊德老师】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 3), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这个就请艾莉老师\n'
				'来说明吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F我明白了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(258), 3, Function((1, 19))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(258), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F『初期行动』指的是，\n'
				'在发生事件的地点\n'
				'所进行的第一次调查。{wait}'
				'{page}'
				'#0101F在刚发生事件的\n'
				'地点，会留下许多\n'
				'犯人的线索。{wait}'
				'{page}'
				'#0103F犯人留下的物品，\n'
				'或者是脚印……{wait}'
				'{page}'
				'#0101F像这些可以成为证据的东西，\n'
				'只要能在一开始就能取回的话……{wait}'
				'{page}'
				'#0100F很快就能将犯人\n'
				'逮捕归案了哦。{wait}'
				'{page}'
				'#0104F（嗯。我有好好地\n'
				'\u3000说明呢。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这个就请缇欧老师\n'
				'来说明吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(259), Text(
				'#0205F我、我知道了。\n'
				'我会想办法完成的……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(259), 3, Function((1, 20))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(259), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F开始调查和字面上的\n'
				'意思一样，指的是\n'
				'第一次的调查。{wait}'
				'{page}'
				'#0201F在刚发生事件的\n'
				'地点，会留下许多\n'
				'犯人的线索。{wait}'
				'{page}'
				'但是，这些线索\n'
				'会随着时间逐渐消失，\n'
				'所以需要迅速处理……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(20), Text(
				'嗯──为什么线索\n'
				'会随着时间\n'
				'逐渐消失呢……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 16))),
			Insn('TEXT_TALK', Char(259), Text(
				'#0208F（……看起来，似乎没能\n'
				'\u3000好好说明呢……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		2: [
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这个就请兰迪老师\n'
				'来说明吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0310F我、我吗？\n'
				'这个嘛……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(260), 3, Function((1, 21))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(260), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F『初期行动』，也就是\n'
				'一开始采取的动作。{wait}'
				'{page}'
				'在发生事件的\n'
				'现场，会留下许多\n'
				'犯人的线索。{wait}'
				'{page}'
				'#0301F比方说，像是犯人的脚印之类的。\n'
				'但是脚印这种东西，\n'
				'被风吹雨淋的话就会消失对吧？{wait}'
				'{page}'
				'#0304F所以，要趁它\n'
				'还没消失的时候\n'
				'确实保存下来。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0302F（总之，我应该\n'
				'\u3000没说错吧……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		3: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这就由我来说明吧。{wait}'
				'{page}'
				'开始调查指的是，\n'
				'保留犯罪现场并且\n'
				'寻找犯人线索的意思。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(19), Text(
				'老师，保留是什么？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0011F啊，保留指的是\n'
				'保持犯罪现场的完整……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(26), Text(
				'保持要怎么完整呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 16))),
			Insn('TEXT_TALK', Char(257), Text(
				'#0012F呃、嗯、这个嘛……{wait}'
				'{page}'
				'#0006F（嗯……\n'
				'要说明得让小孩也能懂，\n'
				'\u3000还真困难呢……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 29))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 17))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F总之，『初期行动』\n'
		'是非常重要的事情。{wait}'
		'{page}'
		'一开始能不能\n'
		'找到证据，也会大幅影响\n'
		'后续的调查。{wait}'
		'{page}'
		'#0003F接着，开始调查时\n'
		'绝对需要某个东西。\n'
		'那就是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}会影响逮捕犯人的『初期行动』。\n'
		'教导大家在调查时\n'
		'所需的东西的是……！{0x18}{wait}'
	)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, 200, 0, Text(
		'【①艾莉老师】\n'
		'【②缇欧老师】\n'
		'【③兰迪老师】\n'
		'【④罗伊德老师】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F艾莉老师，你认为是什么？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(258), 3, Function((1, 19))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(258), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F这个嘛……\n'
				'为了搜集证据，\n'
				'所以需要保留现场。{wait}'
				'{page}'
				'#0101F要让除了\n'
				'警察以外的人\n'
				'迅速离开事件现场……{wait}'
				'{page}'
				'此外，也不能徒手触碰\n'
				'现场的东西。{wait}'
				'{page}'
				'#0104F现场附近如果有发现者、\n'
				'通报者或目击者的话，\n'
				'则必须要请他们协助。{wait}'
				'{page}'
				'#0102F只靠警察是无法\n'
				'解决事件的。还需要\n'
				'许多人的协助。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(29), Text(
				'嗯──\n'
				'我大概算是懂了吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0113F（虽然我觉得\n'
				'\u3000没有说错……不过总觉得\n'
				'\u3000说了多余的事情……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F缇欧老师，你认为是什么？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(259), Text(
				'#0205F那、那是……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(259), 3, Function((1, 20))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(259), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(259), Text(
				'#0201F指视力吗？{wait}'
				'{page}'
				'也就是说，需要有不论多微小的事物\n'
				'都不会看漏的双眼。{wait}'
				'{page}'
				'#0209F还有，呃……毅力。\n'
				'在不知道有没有\n'
				'留下证据的现场……{wait}'
				'{page}'
				'#0206F要找出一粒撒一般的证据，\n'
				'需要非常大的毅力……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 16))),
			Insn('TEXT_TALK', Char(259), Text(
				'#0208F（我太过紧张，\n'
				'\u3000说出来的内容\n'
				'\u3000都变得不知所措了……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		2: [
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 3), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F兰迪老师，你认为是什么？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(260), 3, Function((1, 21))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(260), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F总之就是要迅速行动吧。\n'
				'时间经过越久，\n'
				'搜集证据就会变得越来越困难。{wait}'
				'{page}'
				'#0303F犯人也不是笨蛋。\n'
				'应该会想办法消灭证据，\n'
				'也会逃往远方吧。{wait}'
				'{page}'
				'#0307F初期行动就是和时间赛跑！\n'
				'速度是\n'
				'决定胜负的关键。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(25), Text(
				'哇～感觉好帅！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0309F（嗯，感觉应该\n'
				'\u3000教得很不错吧！）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		3: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这就由我来说明吧。{wait}'
				'{page}'
				'#0004F『初期行动』需要的东西……\n'
				'这个嘛，像是身为警察的\n'
				'一整套装备……{wait}'
				'{page}'
				'#0003F比方说，如果没有\n'
				'警察手册的话，就没办法\n'
				'顺利跟居民打听情报……{wait}'
				'{page}'
				'#0011F如果没有警棍或手枪的话，\n'
				'发生事情的时候，呃，\n'
				'也会很困扰。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 16))),
			Insn('TEXT_TALK', Char(257), Text(
				'#0006F（总觉得说明得\n'
				'\u3000乱七八糟呢……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 29))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 17))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0004F……那么，假设在\n'
		'『初期行动』时，有找到\n'
		'跟犯人有关的证据。{wait}'
		'{page}'
		'#0013F接下来很重要的就是『推理』了。\n'
		'如果没有链接证据物品跟\n'
		'犯人的内容的话……{wait}'
		'{page}'
		'#0000F就没办法进到\n'
		'『逮捕』犯人这一步。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}调查总算渐入佳境！\n'
		'『推理』究竟是什么！？\n'
		'要上课的人是……{0x18}{wait}'
	)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, 200, 0, Text(
		'【①艾莉老师】\n'
		'【②缇欧老师】\n'
		'【③兰迪老师】\n'
		'【④罗伊德老师】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 3), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F艾莉老师，麻烦你了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(258), 3, Function((1, 19))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(258), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F『推理』是什么？{wait}'
				'{page}'
				'#0101F它是指用『初期行动』时\n'
				'搜集到的情报为基础，\n'
				'去预测后续结果的行为。{wait}'
				'{page}'
				'不管是哪种事件，\n'
				'肯定会有线索和证据出现。{wait}'
				'{page}'
				'#0103F搜集这些东西、思考顺序、\n'
				'像拼图一样进行拼凑……\n'
				'借此找出答案。{wait}'
				'{page}'
				'#0100F这就是推理哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(30), Text(
				'原来如此……\n'
				'警察好厉害哦！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0109F（嗯。我有好好地\n'
				'\u3000说明呢。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F缇欧老师，麻烦你了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0207F我、我知道了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(259), 3, Function((1, 20))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(259), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(259), Text(
				'#0203F推理指的是，以调查时搜集到的\n'
				'证据、情报、事实为基础，\n'
				'借此还原事情经过及找出答案的行为。{wait}'
				'{page}'
				'#0201F只要能把证据一个个\n'
				'联系起来，总有一天\n'
				'会找到犯人。{wait}'
				'{page}'
				'#0200F这个作业过程\n'
				'就是『推理』。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(26), Text(
				'虽然有点难，\n'
				'不过我大概懂了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0206F（要是能再说得更\n'
				'\u3000浅显易懂一点就好了……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		2: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F兰迪老师，麻烦你了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(260), Text(
				'#0305F居然叫我教这题！？\n'
				'伤脑筋……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(260), 3, Function((1, 21))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(260), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(260), Text(
				'#0303F嗯，简单来说，就是\n'
				'『犯人就是你！』这句话的\n'
				'上一个阶段。{wait}'
				'{page}'
				'#0301F再说得更简单，就是思考\n'
				'犯人到底是谁，不过……{wait}'
				'{page}'
				'#0309F要怎么去思考谁是犯人，\n'
				'我也很不擅长，所以不太懂。{wait}'
				'{page}'
				'总之，推理是件\n'
				'很辛苦的事。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 16))),
			Insn('TEXT_TALK', Char(260), Text(
				'#0306F……嗯，这种说明不可能搞懂\n'
				'对吧，哈哈哈……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		3: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这就由我来说明吧。{wait}'
				'{page}'
				'推理指的是，\n'
				'思考谁才是犯人……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(19), Text(
				'只要思考就知道犯人是谁吗？\n'
				'好厉害！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F啊，不。不是这个意思。\n'
				'只是根据搜集到的证据，\n'
				'去想谁最有可能是犯人……{wait}'
				'{page}'
				'#0000F推理指的就是思考这件事。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(29), Text(
				'喂。推理一定会猜中吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0012F并、并没有这种事……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(20), Text(
				'如果推理错误的话，\n'
				'会变成怎样？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 16))),
			Insn('TEXT_TALK', Char(257), Text(
				'#0012F那就要从头推理……\n'
				'不，在那之前还要\n'
				'重新再调查一次……{wait}'
				'{page}'
				'#0006F（我完全没想到\n'
				'\u3000会有各种问题……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 29))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 17))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F『推理』是直接影响到能否\n'
		'逮捕犯人的重要过程。\n'
		'大家都懂了吗？{wait}'
		'{page}'
		'#0001F那么，我们来思考进行推理时\n'
		'需要的东西吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}课程来到重要的关键了。\n'
		'『推理』时所需的东西。\n'
		'要说明这个项目的是……！{0x18}{wait}'
	)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, 200, 0, Text(
		'【①艾莉老师】\n'
		'【②缇欧老师】\n'
		'【③兰迪老师】\n'
		'【④罗伊德老师】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这个就请艾莉老师\n'
				'来说明吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(258), Text(
				'#0105F咦？这题罗伊德应该比较适合吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(258), 3, Function((1, 19))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(258), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(258), Text(
				'#0113F呃，『推理』时需要的\n'
				'东西……我想应该\n'
				'还是直觉吧。{wait}'
				'{page}'
				'#0100F从不晓得正确答案的状态，\n'
				'直到解决事件的过程中，\n'
				'看穿事件重点的力量很重要。{wait}'
				'{page}'
				'#0102F顺带一提，\n'
				'在我们的小队里，\n'
				'最擅长推理的是罗伊德老师。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(30), Text(
				'那么，艾莉老师\n'
				'不会推理吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 16))),
			Insn('TEXT_TALK', Char(258), Text(
				'#0112F咦！？\n'
				'这个嘛，呃，那个……{wait}'
				'{page}'
				'#0113F这就随大家想像了……{wait}'
				'{page}'
				'#0106F（虽然大致上有说明成功，\n'
				'\u3000不过为什么会觉得\n'
				'\u3000像是失败了呢……？）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这个就请缇欧老师\n'
				'来说明吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0205F我、我知道了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(259), 3, Function((1, 20))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(259), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F这个嘛，『推理』时\n'
				'所需的东西……\n'
				'或许是想像力吧。{wait}'
				'{page}'
				'#0203F想像尚未揭露的犯人模样，\n'
				'看穿事件本质……{wait}'
				'{page}'
				'需要的应该是\n'
				'这种力量吧。{wait}'
				'{page}'
				'#0202F我也还在持续学习中，\n'
				'虽然无法顺利推理的情况\n'
				'还很多，不过……{wait}'
				'{page}'
				'#0201F总有一天，\n'
				'我想成为像罗伊德老师那样，\n'
				'可以完成『推理』的警察。{wait}'
				'{page}'
				'#0203F（虽然没有就理论\n'
				'\u3000好好说明，不过我想\n'
				'\u3000大概有传达到重点。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		2: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这个就请兰迪老师\n'
				'来说明吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(260), Text(
				'#0310F不、不要叫我啦……\n'
				'我才不懂有关推理的东西。{wait}'
				'{page}'
				'#0306F……现在不是说这种话的时候啊。\n'
				'呃，推理时所需的东西……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(260), 3, Function((1, 21))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(260), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(260), Text(
				'#0303F…………{wait}'
				'{page}'
				'#0307F#5S不知道啦！！#3S{wait}'
				'{page}'
				'#0306F这种东西，\n'
				'我还希望有人能教我呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 16))),
			Insn('TEXT_TALK', Char(19), Text(
				'老师也不懂吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0308F嗯。不是我要说，\n'
				'我们小队负责推理的\n'
				'是罗伊德老师。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 17))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1500),
			Insn('TEXT_TALK', Char(260), Text(
				'#0304F这样啊。推理时所需的东西……\n'
				'就是指罗伊德老师啊。{wait}'
				'{page}'
				'#0309F只要有罗伊德老师\n'
				'在的话，不管是什么事件\n'
				'都能迅速解决。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_WATCH', Char(25), Char(257), 300),
			Insn('EMOTE', Char(25), 300, 1300, (54, 57, 250, 0)),
			Insn('SOUND_PLAY', 892, 0, 0, 100),
			Insn('SLEEP', 1500),
			Insn('EMOTE_STOP', Char(25)),
			Insn('TEXT_TALK', Char(28), Text(
				'这样啊～罗伊德老师\n'
				'好厉害！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		3: [
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 3), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#0003F这就由我来说明吧。\n'
				'『推理』时所需的东西……线索、证据，\n'
				'虽然可以想到很多东西……{wait}'
				'{page}'
				'#0008F不过很遗憾，我想应该没有正确答案。\n'
				'起码，\n'
				'我还没找到答案。{wait}'
				'{page}'
				'#0000F不过，身为警察的\n'
				'广阔知识与经验，\n'
				'会加深推理幅度。{wait}'
				'{page}'
				'#0002F我虽然也还是新人，\n'
				'不过为了成为这样的警察，\n'
				'我也会持续努力。{wait}'
				'{page}'
				'#0004F（虽然不知道是否正确，\n'
				'\u3000不过这是我自己\n'
				'\u3000思考过后的结论。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(30), 0, 1700, (10, 11, 250, 2)),
			Insn('SOUND_PLAY', 27, 0, 0, 100),
			Insn('SLEEP', 1500),
			Insn('TEXT_TALK', Char(30), Text(
				'罗伊德老师……\n'
				'好像很帅气耶……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 29))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 17))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F那么，总算进行到最后了。\n'
		'根据『推理』\n'
		'知道犯人后……{wait}'
		'{page}'
		'#0007F事情终于要\n'
		'进行到最终局面的\n'
		'『逮捕』了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}紧张的瞬间！\n'
		'关于『逮捕』，\n'
		'要负责上课的是……{0x18}{wait}'
	)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, 200, 0, Text(
		'【①艾莉老师】\n'
		'【②缇欧老师】\n'
		'【③兰迪老师】\n'
		'【④罗伊德老师】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F艾莉老师，\n'
				'由你来吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(258), Text(
				'#0105F咦？这、这个嘛……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(258), 3, Function((1, 19))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(258), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(258), Text(
				'#0101F『逮捕』指的是，\n'
				'把有可能犯了罪的\n'
				'嫌犯抓起来。{wait}'
				'{page}'
				'#0103F逮捕分成３种。\n'
				'一般逮捕、紧急逮捕和\n'
				'现行犯逮捕。{wait}'
				'{page}'
				'#0100F被逮捕的嫌犯最多可以\n'
				'拘留７２小时，在这段时间内会决定\n'
				'要起诉还是释放。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 16))),
			Insn('TEXT_TALK', Char(258), Text(
				'#0106F（嗯，好像说明得\n'
				'\u3000太难了呢……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F缇欧老师，由你来说吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(259), Text(
				'#0205F啊，好的。呃……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(259), 3, Function((1, 20))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(259), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F抓住有可能犯罪的人，\n'
				'这就叫做『逮捕』。{wait}'
				'{page}'
				'#0201F如果犯人可能逃走、或是\n'
				'会湮灭犯罪证据的话……{wait}'
				'{page}'
				'就有必要\n'
				'把嫌犯拘留起来。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(20), Text(
				'嗯──听不太懂呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 16))),
			Insn('TEXT_TALK', Char(259), Text(
				'#0206F（可能有点太难了……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		2: [
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 3), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F兰迪老师，由你来说吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0309F很好！\n'
				'轮到我上场了！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(260), 3, Function((1, 21))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(260), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F所谓的『逮捕』，\n'
				'简单来说就是\n'
				'抓住嫌犯。{wait}'
				'{page}'
				'#0310F做坏事的人\n'
				'也有许多类型，\n'
				'警察也很辛苦呢。{wait}'
				'{page}'
				'想要逃跑的人、\n'
				'拿起武器应战的人……{wait}'
				'{page}'
				'#0307F不过，警察绝对不会输。\n'
				'想逃跑的话就持续追捕，\n'
				'想抵抗的人就让他屈服！{wait}'
				'{page}'
				'#0304F不管对方有多强、\n'
				'拿的武器有多厉害，\n'
				'都不可以退缩。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(25), Text(
				'好厉害……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0309F（很好。说得这么单纯的话，\n'
				'\u3000小孩子也很好懂吧。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		3: [
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这就由我来说明吧。{wait}'
				'{page}'
				'所谓的『逮捕』，\n'
				'就是抓住做坏事\n'
				'或是很可疑的人。{wait}'
				'{page}'
				'#0001F在这个时候，\n'
				'还不确定嫌犯就是犯人。{wait}'
				'{page}'
				'嫌犯到底\n'
				'是不是犯人，之后会通过\n'
				'审判来决定……{wait}'
				'{page}'
				'#0000F在那之前，\n'
				'抓住嫌犯就是\n'
				'警察的工作。{wait}'
				'{page}'
				'#0004F（我已经尽量\n'
				'\u3000简单说明过程，这样的话\n'
				'\u3000小孩也能理解吧。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 29))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 17))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F关于『逮捕』，\n'
		'大家都懂了吗？{wait}'
		'{page}'
		'对警察来说，\n'
		'这虽然是很抢眼的工作……{wait}'
		'{page}'
		'#0001F不过同时也是\n'
		'非常危险的任务。{wait}'
		'{page}'
		'毕竟要直接与\n'
		'犯人面对面。{wait}'
		'{page}'
		'如果在这个过程中\n'
		'让嫌犯逃走，到目前为止的\n'
		'任务全部都会白费……{wait}'
		'{page}'
		'#0000F为了不变成这样，\n'
		'最重要的是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, 16, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}在『逮捕』时\n'
		'最重要的东西。\n'
		'要负责说明的老师是……！{0x18}{wait}'
	)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('MENU', 0, -1, 200, 0, Text(
		'【①艾莉老师】\n'
		'【②缇欧老师】\n'
		'【③兰迪老师】\n'
		'【④罗伊德老师】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F艾莉老师，由你来说吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(258), Text(
				'#0112F呃，『逮捕』时\n'
				'最重要的东西……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(258), 3, Function((1, 19))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(258), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(258), Text(
				'#0101F那就是有没有逮捕令。{wait}'
				'{page}'
				'#0100F如果是紧急逮捕、\n'
				'现行犯逮捕以外的情况，\n'
				'要逮捕嫌犯的话……{wait}'
				'{page}'
				'就需要逮捕令。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 16))),
			Insn('TEXT_TALK', Char(258), Text(
				'#0113F（虽然没有说错，\n'
				'\u3000但是总觉得不太对……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F缇欧老师，由你来说吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
			Insn('SOUND_PLAY', 23, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(259), Text(
				'#0205F啊，好的。\n'
				'『逮捕』时最重要的东西……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(259), 3, Function((1, 20))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(259), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(259), Text(
				'#0203F嗯……\n'
				'就是冷静的判断力。{wait}'
				'{page}'
				'跟嫌犯对峙的时候，\n'
				'通常都是很紧张的状况……{wait}'
				'{page}'
				'#0201F我想，不被当下的气氛\n'
				'压倒是很重要的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 16))),
			Insn('TEXT_TALK', Char(259), Text(
				'#0206F（嗯……总觉得\n'
				'\u3000有哪里不对……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		2: [
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这个就请兰迪老师\n'
				'来说明吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FORK_FUNC', Char(257), 3, Function((1, 22))),
			Insn('FORK_FUNC', Char(260), 3, Function((1, 21))),
			Insn('FORK_AWAIT', Char(257), 3),
			Insn('FORK_AWAIT', Char(260), 3),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F『逮捕』时最需要的东西。\n'
				'那就是……{wait}'
				'{page}'
				'#0307F#5S气势和气魄！#3S{wait}'
				'{page}'
				'#0310F跟凶恶嫌犯\n'
				'对峙的时候，绝对不能输的\n'
				'气势和气魄……{wait}'
				'{page}'
				'#0312F这是最重要的。\n'
				'至少对我来说是这样。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(20), Text(
				'总觉得有点恐怖……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0305F（唔……气势有点\n'
				'\u3000太过头了……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		3: [
			Insn('EXPR_VAR', 4, Expr([Insn('CONST', 3), Insn('ADD_SET'), Insn('END')])),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这就由我来说明吧。{wait}'
				'{page}'
				'『逮捕』时最重要的东西……\n'
				'是证据和自信。{wait}'
				'{page}'
				'#0003F所谓的『逮捕』，\n'
				'是夺走个人自由的\n'
				'重大行为。{wait}'
				'{page}'
				'眼前的嫌犯\n'
				'也有可能是无辜的。{wait}'
				'{page}'
				'#0013F话虽如此，有很多时候还是\n'
				'必须逮捕，否则就无法解决\n'
				'事件、无法保护某些事物。{wait}'
				'{page}'
				'#0007F正因如此，所以自己要\n'
				'全心全意进行调查，\n'
				'拥有肯定的证据和自信……{wait}'
				'{page}'
				'#0000F再进行『逮捕』。\n'
				'我总是用这样的心情\n'
				'来面对事件。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(19), Text(
				'罗伊德老师好厉害──！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0009F（我应该统整得\n'
				'\u3000很完美吧？）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('BGM_STOP', 4000),
	Insn('SOUND_PLAY', 935, 0, 0, 100),
	Insn('FORK_FUNC', Char(257), 3, Function((1, 17))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('SLEEP', 2500),
	Insn('TEXT_TALK', Char(12), Text(
		'是的。时间差不多要到了。\n'
		'今天就到此结束吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'关于警察的工作，\n'
		'大家都懂了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('0x82', 100, 0, 3000, 300),
	Insn('TEXT_SET_POS', -1, 150, -1, -1),
	Insn('TEXT_SET_NAME', Translate('孩子们')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 0}#5S懂了──！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('0x5A'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}上课总算结束了。\n'
		'问题是，孩子们\n'
		'到底理解了多少……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('BGM_WAIT'),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('CAM_OFFSET', (7710, 2300, -90), 0),
	Insn('CAM_ROTATE', 315, 25, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 26410, 0),
	Insn('CHAR_SET_POS', Char(12), (7600, 0, 1320), 270),
	Insn('CHAR_SET_POS', Char(257), (6400, 0, 1920), 90),
	Insn('CHAR_SET_POS', Char(258), (6400, 0, 720), 90),
	Insn('CHAR_SET_POS', Char(259), (5200, 0, 1920), 90),
	Insn('CHAR_SET_POS', Char(260), (5200, 0, 720), 90),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(8))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(265), (7510, 0, 3100), 180),
		]),
		(None, []),
	]),
	Insn('SLEEP', 500),
	Insn('BGM_PLAY', b'|\x00\x00'),
	Insn('CAM_DISTANCE', 25410, 1000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(12), Text(
		'辛苦你了，罗伊德。\n'
		'你对教学的感觉如何？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0003F这个嘛……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('VAR', 4), Insn('CONST', 20), Insn('GE'), Insn('END')]), [
			Insn('QUEST', 57, Insn('TASK_SET', 1)),
			Insn('TEXT_TALK', Char(257), Text(
				'#0002F虽然自己这么说有点不好，\n'
				'不过我觉得表现很好。{wait}'
				'{page}'
				'#0009F关于警察的工作，\n'
				'他们应该\n'
				'懂了不少吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'嗯。我也是这么认为的。\n'
				'你变成很了不起的警察了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'这也是托各位小队\n'
				'成员的福吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(258), 300, 1600, (54, 57, 250, 0)),
			Insn('EMOTE', Char(259), 300, 1600, (54, 57, 250, 0)),
			Insn('EMOTE', Char(260), 300, 1600, (54, 57, 250, 0)),
			Insn('SOUND_PLAY', 892, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('EMOTE_STOP', Char(258)),
			Insn('EMOTE_STOP', Char(259)),
			Insn('EMOTE_STOP', Char(260)),
			Insn('TEXT_TALK', Char(260), Text(
				'#0309F不，这个嘛，\n'
				'没有这回事啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0204F不管是罗伊德还是其他人，\n'
				'我总是受到他们照顾。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0109F呵呵。我们应该是个\n'
				'不错的小队吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('VAR', 4), Insn('CONST', 15), Insn('GE'), Insn('END')]), [
			Insn('QUEST', 57, Insn('TASK_SET', 2)),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F我觉得很不错。\n'
				'关于警察的工作，\n'
				'他们应该懂了一些才对。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'嗯，说的也是。\n'
				'我也学习到很多。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'我想肯定也有传达给\n'
				'孩子们才对。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0309F真让人害羞……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0204F你过奖了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0102F要更进一步的话，\n'
				'要是能够再说明得\n'
				'更清楚点就好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('VAR', 4), Insn('CONST', 10), Insn('GE'), Insn('END')]), [
			Insn('QUEST', 57, Insn('TASK_SET', 3)),
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F关于警察的工作，\n'
				'到底有没有好好说明清楚，\n'
				'可能有点难说。{wait}'
				'{page}'
				'#0008F有许多地方\n'
				'需要反省检讨。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'呵呵。我觉得有上进心\n'
				'是件好事。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'……不过的确，或许各位需要\n'
				'再多学习一点呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0103F你说得对……\n'
				'我也深刻感受到学的还不够。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0208F我也是。\n'
				'应该还有更好的\n'
				'说明方式。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0306F就是啊。我们也还\n'
				'需要再多加\n'
				'学习呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('QUEST', 57, Insn('TASK_SET', 4)),
			Insn('TEXT_TALK', Char(257), Text(
				'#0006F……老实说，关于警察的工作内容，\n'
				'说不定让他们误会了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'这个嘛……\n'
				'我也觉得让人不太懂的\n'
				'说明很多。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'看来各位还需要\n'
				'再多学习一点呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0113F让你看笑话了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0206F是的。我也还\n'
				'学得不够……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0306F嗯……要教导别人东西\n'
				'真困难呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('IF', [
		(Expr([Insn('VAR', 4), Insn('CONST', 24), Insn('GE'), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'那么。\n'
				'这是上课的谢礼。\n'
				'不用客气，请收下吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FADE_ON', 300, Color(0x00000000), 100),
			Insn('TEXT_SET_POS', -1, -1, -1, -1),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('SOUND_PLAY', 17, 0, 0, 100),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'已收下{item 97}{color 0}。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('FADE_OFF', 300, Color(0x00000000)),
			Insn('TEXT_SET_POS', 14, 280, 60, 3),
			Insn('0x5A'),
			Insn('QUEST_BONUS_DP', 57, 2),
			Insn('ITEM_ADD', 97, 1),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(12), Text(
		'我接下来还有课，\n'
		'所以要先离开了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'随时欢迎你们再到\n'
		'学校来玩。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'如果是你们的话，\n'
		'孩子们肯定也会\n'
		'很欢迎你们的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F谢谢。\n'
		'那么，我们告辞了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_FUNC', Char(12), 3, Function((0, 52))),
	Insn('SOUND_PLAY', 9, 0, 0, 100),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'达成{color 2}任务【续丄主日学校的特别老师】{color 0}！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('QUEST', 57, Insn('FLAG_UNSET', 16)),
	Insn('FORK_AWAIT', Char(12), 3),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('TEXT_TALK', Char(12), Text(
		'各位，辛苦了。\n'
		'担任老师这种不熟悉的工作，\n'
		'应该够了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'随时欢迎你们再到学校来玩。\n'
		'我想孩子们肯定也会\n'
		'感到很高兴哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(19), Text(
				'大哥哥，你们有事吗？\n'
				'该不会，是来上\n'
				'修女的课吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(19), Text(
				'老师上的课很有趣哦！\n'
				'之后再来教我们吧！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(20), Text(
				'大哥哥的战术导力器\n'
				'很帅呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(20), Text(
				'警察说不定也是\n'
				'很不错的呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(20), Text(
				'警察好厉害哦。\n'
				'我将来也去当\n'
				'警察好了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(20), Text(
				'嗯……不过，游击士\n'
				'这个选择也很难放弃呢……\n'
				'真让人烦恼。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(29), Text(
				'学校上的课真无聊。\n'
				'既然要上的话，我想学其他东西。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(29), Text(
				'像是关于世界局势之类的。\n'
				'目前我对爱普斯泰恩财团\n'
				'很有兴趣。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(29), Text(
				'爱普斯泰恩博士究竟是个\n'
				'怎样的人？之类的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(29), Text(
				'……真没想到，\n'
				'可以在主日学校的课堂\n'
				'听到这么有趣的内容。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(29), Text(
				'有机会再教我关于警察的事吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(26), Text(
				'『为了将来，\n'
				'\u3000你要好好学习』\n'
				'虽然妈妈这么说，可是……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(26), Text(
				'我有时候会想，\n'
				'真的是这样吗？……如此这般，\n'
				'有时会感到困惑哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(26), Text(
				'学习警察的事\n'
				'比数学还要有趣呢。\n'
				'你们还要再来哦！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(30), Text(
				'主日学校的课程太简单了，\n'
				'真无聊！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(30), Text(
				'这样的话，还不如在家里\n'
				'自修可以学到更多。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(30), Text(
				'哦呵呵，罗伊德老师的课\n'
				'很有趣呢！\n'
				'希望你下次来教不同科目！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 57, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(25), Text(
				'呼～\n'
				'只要一想到要开始上课，\n'
				'就会觉得很困呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(25), Text(
				'……呃，如果打哈欠的话，\n'
				'会惹修女生气呢。\n'
				'要忍耐才行……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(25), Text(
				'我还是第一次\n'
				'在上课的时候不想睡呢。\n'
				'老师上的课很有趣。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(25), Text(
				'要再来当老师哦！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('0x95', Char(254), (153500, 200, 18150), 3800, 0),
	Insn('0x95', Char(254), (150500, 200, 18150), 3800, 0),
	Insn('0x95', Char(254), (147500, 200, 16300), 3800, 0),
	Insn('CHAR_ROTATE', Char(254), 180, 300),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('0x95', Char(254), (153500, 200, 18150), 2000, 0),
	Insn('0x95', Char(254), (150500, 200, 18150), 3000, 0),
	Insn('0x95', Char(254), (149250, 200, 16300), 3000, 0),
	Insn('CHAR_ROTATE', Char(254), 180, 300),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('0x95', Char(254), (152750, 200, 16300), 2000, 0),
	Insn('CHAR_ROTATE', Char(254), 180, 300),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('0x95', Char(254), (154500, 200, 16300), 1000, 0),
	Insn('CHAR_ROTATE', Char(254), 180, 300),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('0x95', Char(254), (149500, 200, 17500), 1000, 0),
	Insn('0x95', Char(254), (151000, 200, 17500), 2000, 0),
	Insn('CHAR_ROTATE', Char(254), 180, 300),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('EMOTE', Char(19), 0, 1700, (0, 1, 250, 2)),
		Insn('EMOTE', Char(27), 0, 1700, (0, 1, 250, 2)),
		Insn('SOUND_PLAY', 29, 0, 0, 100),
		Insn('SLEEP', 1000),
		Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 0)),
		Insn('EMOTE', Char(258), 0, 2000, (40, 43, 100, 0)),
		Insn('EMOTE', Char(259), 0, 2000, (40, 43, 100, 0)),
		Insn('EMOTE', Char(260), 0, 2000, (40, 43, 100, 0)),
		Insn('SLEEP', 300),
		Insn('EXPR_VAR', 2, Expr([Insn('RAND'), Insn('CONST', 3), Insn('MOD'), Insn('SET'), Insn('END')])),
		Insn('SWITCH', [Insn('VAR', 2), Insn('END')], {
			0: [
				Insn('CHAR_SET_FRAME', Char(20), 0),
				Insn('BREAK'),
			],
			1: [
				Insn('CHAR_SET_FRAME', Char(20), 1),
				Insn('BREAK'),
			],
			None: [
				Insn('CHAR_SET_FRAME', Char(20), 2),
				Insn('BREAK'),
			],
		}),
		Insn('SLEEP', 500),
		Insn('EMOTE', Char(30), 0, 1700, (0, 1, 250, 2)),
		Insn('SOUND_PLAY', 29, 0, 0, 100),
		Insn('EXPR_VAR', 2, Expr([Insn('RAND'), Insn('CONST', 3), Insn('MOD'), Insn('SET'), Insn('END')])),
		Insn('SWITCH', [Insn('VAR', 2), Insn('END')], {
			0: [
				Insn('CHAR_SET_FRAME', Char(30), 0),
				Insn('BREAK'),
			],
			1: [
				Insn('CHAR_SET_FRAME', Char(30), 1),
				Insn('BREAK'),
			],
			None: [
				Insn('CHAR_SET_FRAME', Char(30), 2),
				Insn('BREAK'),
			],
		}),
		Insn('SLEEP', 350),
		Insn('EMOTE', Char(29), 0, 1700, (0, 1, 250, 2)),
		Insn('SOUND_PLAY', 29, 0, 0, 100),
		Insn('EXPR_VAR', 2, Expr([Insn('RAND'), Insn('CONST', 3), Insn('MOD'), Insn('SET'), Insn('END')])),
		Insn('SWITCH', [Insn('VAR', 2), Insn('END')], {
			0: [
				Insn('CHAR_SET_FRAME', Char(29), 0),
				Insn('BREAK'),
			],
			1: [
				Insn('CHAR_SET_FRAME', Char(29), 1),
				Insn('BREAK'),
			],
			None: [
				Insn('CHAR_SET_FRAME', Char(29), 2),
				Insn('BREAK'),
			],
		}),
		Insn('EMOTE', Char(20), 0, 1700, (0, 1, 250, 2)),
		Insn('SOUND_PLAY', 29, 0, 0, 100),
		Insn('SLEEP', 250),
		Insn('EMOTE', Char(28), 0, 1700, (0, 1, 250, 2)),
		Insn('SOUND_PLAY', 29, 0, 0, 100),
		Insn('SLEEP', 300),
		Insn('EMOTE', Char(26), 0, 1700, (0, 1, 250, 2)),
		Insn('SOUND_PLAY', 29, 0, 0, 100),
		Insn('EXPR_VAR', 2, Expr([Insn('RAND'), Insn('CONST', 3), Insn('MOD'), Insn('SET'), Insn('END')])),
		Insn('SWITCH', [Insn('VAR', 2), Insn('END')], {
			0: [
				Insn('CHAR_SET_FRAME', Char(26), 0),
				Insn('BREAK'),
			],
			1: [
				Insn('CHAR_SET_FRAME', Char(26), 1),
				Insn('BREAK'),
			],
			None: [
				Insn('CHAR_SET_FRAME', Char(26), 2),
				Insn('BREAK'),
			],
		}),
		Insn('SWITCH', [Insn('VAR', 2), Insn('END')], {
			0: [
				Insn('CHAR_SET_FRAME', Char(28), 0),
				Insn('BREAK'),
			],
			1: [
				Insn('CHAR_SET_FRAME', Char(28), 1),
				Insn('BREAK'),
			],
			None: [
				Insn('CHAR_SET_FRAME', Char(28), 2),
				Insn('BREAK'),
			],
		}),
		Insn('SLEEP', 350),
		Insn('EXPR_VAR', 2, Expr([Insn('RAND'), Insn('CONST', 3), Insn('MOD'), Insn('SET'), Insn('END')])),
		Insn('SWITCH', [Insn('VAR', 2), Insn('END')], {
			0: [
				Insn('CHAR_SET_FRAME', Char(19), 0),
				Insn('BREAK'),
			],
			1: [
				Insn('CHAR_SET_FRAME', Char(19), 1),
				Insn('BREAK'),
			],
			None: [
				Insn('CHAR_SET_FRAME', Char(19), 2),
				Insn('BREAK'),
			],
		}),
		Insn('EMOTE', Char(25), 0, 1700, (0, 1, 250, 2)),
		Insn('SOUND_PLAY', 29, 0, 0, 100),
		Insn('SLEEP', 550),
		Insn('EXPR_VAR', 2, Expr([Insn('RAND'), Insn('CONST', 3), Insn('MOD'), Insn('SET'), Insn('END')])),
		Insn('SWITCH', [Insn('VAR', 2), Insn('END')], {
			0: [
				Insn('CHAR_SET_FRAME', Char(25), 0),
				Insn('BREAK'),
			],
			1: [
				Insn('CHAR_SET_FRAME', Char(25), 1),
				Insn('BREAK'),
			],
			None: [
				Insn('CHAR_SET_FRAME', Char(25), 2),
				Insn('BREAK'),
			],
		}),
		Insn('EXPR_VAR', 2, Expr([Insn('RAND'), Insn('CONST', 3), Insn('MOD'), Insn('SET'), Insn('END')])),
		Insn('SWITCH', [Insn('VAR', 2), Insn('END')], {
			0: [
				Insn('CHAR_SET_FRAME', Char(27), 0),
				Insn('BREAK'),
			],
			1: [
				Insn('CHAR_SET_FRAME', Char(27), 1),
				Insn('BREAK'),
			],
			None: [
				Insn('CHAR_SET_FRAME', Char(27), 2),
				Insn('BREAK'),
			],
		}),
		Insn('EMOTE_STOP', Char(257)),
		Insn('EMOTE_STOP', Char(258)),
		Insn('EMOTE_STOP', Char(259)),
		Insn('EMOTE_STOP', Char(260)),
	]),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('EMOTE_STOP', Char(65535)),
	Insn('CHAR_SET_FRAME', Char(19), 0),
	Insn('CHAR_SET_FRAME', Char(20), 0),
	Insn('CHAR_SET_FRAME', Char(25), 0),
	Insn('CHAR_SET_FRAME', Char(26), 0),
	Insn('CHAR_SET_FRAME', Char(29), 0),
	Insn('CHAR_SET_FRAME', Char(30), 0),
	Insn('CHAR_SET_FRAME', Char(27), 0),
	Insn('CHAR_SET_FRAME', Char(28), 0),
	Insn('0x49'),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('0x95', Char(254), (149500, 200, 17500), 3000, 0),
	Insn('0x95', Char(254), (151000, 200, 17500), 3000, 0),
	Insn('CHAR_ROTATE', Char(254), 180, 300),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('0x95', Char(254), (149250, 200, 17300), 3000, 0),
	Insn('0x95', Char(254), (151000, 200, 17500), 3000, 0),
	Insn('CHAR_ROTATE', Char(254), 180, 300),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('0x95', Char(254), (152750, 200, 17300), 3000, 0),
	Insn('0x95', Char(254), (151000, 200, 17500), 3000, 0),
	Insn('CHAR_ROTATE', Char(254), 180, 300),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('0x95', Char(254), (151000, 200, 17500), 3000, 0),
	Insn('CHAR_ROTATE', Char(254), 180, 300),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('0x95', Char(254), (150500, 200, 18150), 3000, 0),
	Insn('0x95', Char(254), (147500, 200, 16300), 3000, 0),
	Insn('CHAR_ROTATE', Char(254), 180, 300),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('0x95', Char(254), (150020, 0, 12070), 3000, 0),
	Insn('CHAR_ROTATE', Char(254), 270, 300),
	Insn('CROSSFADE', 100),
	Insn('CHAR_SET_CHCP', Char(19), 10),
	Insn('CHAR_SET_POS', Char(254), (148490, 150, 12230), 0),
	Insn('CHAR_FLAG1_SET', Char(19), 4),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('0x0D'),
	Insn('EMOTE_STOP', Char(19)),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('0x95', Char(254), (150000, 0, 8150), 3000, 0),
	Insn('0x95', Char(254), (147140, 0, 8150), 3000, 0),
	Insn('CHAR_ROTATE', Char(254), 0, 300),
	Insn('CROSSFADE', 100),
	Insn('CHAR_SET_CHCP', Char(20), 20),
	Insn('CHAR_SET_POS', Char(254), (147140, 150, 9130), 0),
	Insn('CHAR_FLAG1_SET', Char(20), 4),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('0x0D'),
	Insn('EMOTE_STOP', Char(20)),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('0x95', Char(254), (149930, 0, 8000), 3000, 0),
	Insn('0x95', Char(254), (152000, 0, 12130), 3000, 0),
	Insn('CROSSFADE', 100),
	Insn('CHAR_SET_CHCP', Char(30), 21),
	Insn('CHAR_SET_POS', Char(254), (153620, 150, 12230), 0),
	Insn('CHAR_FLAG1_SET', Char(30), 4),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('0x0D'),
	Insn('EMOTE_STOP', Char(30)),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('0x95', Char(254), (152000, 0, 14010), 3000, 0),
	Insn('0x95', Char(254), (152000, 0, 5970), 3000, 0),
	Insn('CHAR_ROTATE', Char(254), 90, 300),
	Insn('CROSSFADE', 100),
	Insn('CHAR_SET_CHCP', Char(25), 7),
	Insn('CHAR_SET_POS', Char(254), (153620, 150, 6150), 0),
	Insn('CHAR_FLAG1_SET', Char(25), 4),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('0x0D'),
	Insn('EMOTE_STOP', Char(25)),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('EMOTE', Char(254), 0, 2000, (38, 39, 250, 2)),
		Insn('SLEEP', 1500),
	]),
	Insn('RETURN'),
]

data['code'][28] = [
	Insn('SLEEP', 300),
	Insn('EMOTE', Char(27), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(28), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(19), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(20), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(26), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(29), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(30), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('EMOTE', Char(25), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('RETURN'),
]

data['code'][29] = [
	Insn('CHAR_SET_POS', Char(257), (151000, 200, 17500), 180),
	Insn('CHAR_SET_POS', Char(258), (149250, 200, 16300), 180),
	Insn('CHAR_SET_POS', Char(259), (152750, 200, 16300), 180),
	Insn('CHAR_SET_POS', Char(260), (154500, 200, 16300), 180),
	Insn('RETURN'),
]
