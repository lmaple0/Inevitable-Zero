# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't1030',
	'name2': 't1030',
	'location': 65,
	'bgm': 111,
	'flags': 8192,
	'includes': [
		None,
		None,
		None,
		None,
		None,
		None,
	],
	'name3': 't1030_1',
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
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (3420, 6850, -600), 0),
	Insn('CAM_ROTATE', 32, 19, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 28000, 0),
	Insn('CHAR_ROTATE', Char(254), 270, 0),
	Insn('CHAR_SET_POS', Char(257), (3400, 4400, 640), 90),
	Insn('CHAR_SET_POS', Char(258), (3400, 4400, -800), 90),
	Insn('CHAR_SET_POS', Char(259), (2200, 4400, 640), 90),
	Insn('CHAR_SET_POS', Char(260), (2200, 4400, -800), 90),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(337), (1000, 4400, -100), 90),
		]),
		(None, []),
	]),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (3420, 5850, -600), 1000),
	Insn('CAM_DISTANCE', 29000, 1000),
	Insn('0x0D'),
	Insn('0x6F', b'\x10'),
	Insn('RETURN'),
]

data['code'][1] = [
	Insn('0x4B', Char(254), -1),
	Insn('CALL', Function((1, 0))),
	Insn('EMOTE', Char(254), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(254), Text(
		'欢迎来到米修拉姆\n'
		'引以为傲的主题乐园。\n'
		'请问有带入场券吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F呃，我们是克洛斯贝尔\n'
		'警察丄特务支援课的人。\n'
		'我们看到支援委托才过来拜访……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'哦哦！我恭候多时了！\n'
		'我已经不知道\n'
		'到底该如何是好了……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0011F请、请你冷静下来。\n'
		'……到底发生了什么事？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'是的，呃……\n'
		'这件事我想请你们\n'
		'务必要保密……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'其实，是关于咪西的事。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0001F咪西是这个主题乐园的\n'
		'吉祥物，没错吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0201F该不会是咪西出事了吧……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'嗯，是这样的……\n'
		'咪西它失踪了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F失踪了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'趁我稍微不注意的时候，\n'
		'它似乎就不知道\n'
		'跑到哪里去了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0207F该不会……是被诱旋了吧？{wait}'
		'{page}'
		'#0201F想要在自己家里把玩\n'
		'可爱的咪西……\n'
		'这个犯罪动机可以理解。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0306F（该不会只是\n'
		'\u3000里面的人想偷懒吧？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'总之，我想拜托你们迅速、而且\n'
		'神不知鬼不觉地将它找出来！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'为了守护孩子们的梦想，\n'
		'请务必助我一臂之力！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('0x4B', Char(254), -1),
	Insn('CALL', Function((1, 0))),
	Insn('TEXT_TALK', Char(254), Text(
		'我想请你们在不让\n'
		'任何人发现的情况下，\n'
		'暗中将咪西带回来！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'为了守护孩子们的梦想，\n'
		'请务必助我一臂之力！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][3] = [
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
				'#0006F虽然很抱歉……\n'
				'不过我们无法马上接下委托。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0205F怎么会……！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F（为什么她看起来\n'
				'\u3000比委托人更受到打击啊……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'这样啊……\n'
				'这下伤脑筋了，\n'
				'我到底该怎么办呢……？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('CALL', Function((1, 4))),
		]),
	]),
	Insn('0x4C', Char(254), -1),
	Insn('CHAR_SET_POS', Char(0), (3490, 4000, -2340), 180),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('QUEST', 55, Insn('TASK_SET', 1)),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F我知道了。\n'
		'我们就接下\n'
		'这个委托了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'嗯！谢谢你们！\n'
		'真的很谢谢你们！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0203F我们只是做了该做的事而已。\n'
		'身为克洛斯贝尔市民，\n'
		'协助咪西度过危机是我们的义务。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0012F啊哈哈……是、是这样吗？{wait}'
		'{page}'
		'#0000F呃，那就马上开始吧，\n'
		'你知道咪西有可能\n'
		'会去的地方吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'这个嘛，咪西是布偶装……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'不对不对，我说错了。\n'
		'因为咪西是猫，\n'
		'我想它应该没有离开太远才对。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0001F这么说来，是在米修拉姆的\n'
		'某个地方啰？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'这只是我的推测。\n'
		'话虽如此，如果它要坐船前往市街，\n'
		'我想应该是非常困难的吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0201F但是，如果是诱旋的话，\n'
		'也有可能会坐船吧。{wait}'
		'{page}'
		'我想先到停船处\n'
		'打听消息，应该比较好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F好，就这么办。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 80, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'开始进行{color 2}任务【寻找某人】{color 0}！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('TEXT_TALK', Char(254), Text(
		'请你们尽快\n'
		'找出咪西！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'为了守护孩子们的梦想，\n'
		'就麻烦你们了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('QUEST', 55, Insn('TASK_SET', 2)),
	Insn('EVENT_BEGIN', 0),
	Insn('0x4B', Char(254), -1),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (23460, -1400, -48070), 0),
	Insn('CAM_ROTATE', 309, 18, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 29500, 0),
	Insn('CHAR_ROTATE', Char(254), 225, 0),
	Insn('CHAR_SET_POS', Char(257), (21740, -4000, -47580), 45),
	Insn('CHAR_SET_POS', Char(258), (22520, -4000, -48510), 45),
	Insn('CHAR_SET_POS', Char(259), (20930, -4000, -48460), 45),
	Insn('CHAR_SET_POS', Char(260), (21620, -4000, -49280), 45),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(337), (13000, -4000, -46590), 270),
		]),
		(None, []),
	]),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (23460, -2400, -48070), 1000),
	Insn('CAM_DISTANCE', 30500, 1000),
	Insn('0x0D'),
	Insn('EMOTE', Char(254), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('0x6F', b'\x10'),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(254), Text(
		'咪西？\n'
		'哦，那个猫咪的布偶装啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'那只猫咪的话，它先是四处跑来跑去，\n'
		'然后就跑向时装店的方向去了，\n'
		'它怎么了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0009F没事，没什么。\n'
		'谢谢你告诉我们。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(257), (12500, -4000, -37560), 270),
	Insn('CHAR_SET_POS', Char(258), (12500, -4000, -36420), 270),
	Insn('CHAR_SET_POS', Char(259), (12500, -4000, -38700), 270),
	Insn('CHAR_SET_POS', Char(260), (12500, -4000, -39860), 270),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(337), (15500, -4000, -39730), 90),
		]),
		(None, []),
	]),
	Insn('CAM_OFFSET', (20920, 1400, -37560), 0),
	Insn('CAM_ROTATE', 299, 27, 0, 0),
	Insn('0x6E', 300, 0),
	Insn('CAM_DISTANCE', 55500, 0),
	Insn('SLEEP', 1500),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('CAM_OFFSET', (15490, -1400, -37760), 3000),
	Insn('CAM_ROTATE', 299, 22, 0, 3000),
	Insn('CAM_DISTANCE', 48500, 3000),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0103F四处跑来跑去……\n'
		'这是怎么回事呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0201F如果它是在躲避追兵，\n'
		'这样推测的话就很合理。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0305F追兵是指谁啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0207F当然是打算捕捉\n'
		'咪西的罪犯啰。{wait}'
		'{page}'
		'#0201F他打算捕捉咪西，并且\n'
		'一个人独占毛绒绒的触感。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(260), Text(
		'#0306F…………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 0)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#0012F呃……总之，\n'
		'我们先追上去吧。\n'
		'它似乎往时装店方向去了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE_STOP', Char(257)),
	Insn('0x4C', Char(254), -1),
	Insn('CHAR_SET_POS', Char(0), (14390, -4000, -38090), 0),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('TEXT_TALK', Char(254), Text(
		'你们问猫咪的布偶装啊，\n'
		'它摇摇晃晃地\n'
		'朝时装店走去啰！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('QUEST', 55, Insn('TASK_SET', 3)),
	Insn('EVENT_BEGIN', 0),
	Insn('0x4B', Char(254), -1),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(254), (16760, 0, 10830), 140),
	Insn('CHAR_SET_POS', Char(257), (18410, 0, 9220), 335),
	Insn('CHAR_SET_POS', Char(258), (17610, 0, 7980), 335),
	Insn('CHAR_SET_POS', Char(259), (19440, 0, 8730), 300),
	Insn('CHAR_SET_POS', Char(260), (18630, 0, 7480), 300),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(337), (15610, 0, 11480), 180),
		]),
		(None, []),
	]),
	Insn('CAM_OFFSET', (18650, 3290, 10040), 0),
	Insn('CAM_ROTATE', 1, 10, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 22500, 0),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (18650, 2290, 10040), 1000),
	Insn('CAM_DISTANCE', 20500, 1000),
	Insn('0x6F', b'y'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(254), Text(
		'咦？咪西？\n'
		'嗯，我有看到哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'它先是啪哒啪哒！地跑过去，然后\n'
		'哇啊──！地惨叫，然后\n'
		'咻～！地又不见了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F#11P啪哒啪哒、\n'
		'哇啊、\n'
		'咻……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'嗯！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0201F#11P果然没错，咪西肯定\n'
		'发生了什么事。{wait}'
		'{page}'
		'#0210F为了躲避追兵，\n'
		'它慌张地逃跑着，\n'
		'我仍然可以看见它痛苦的神情。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0306F#5P它是布偶装耶，\n'
		'表情应该不会有变化吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0201F#11P兰迪你太过\n'
		'在意细节了。{wait}'
		'{page}'
		'#0200F请问，咪西后来\n'
		'跑去哪里了呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'这个嘛……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(254), 270, 500),
	Insn('CAM_OFFSET', (-4260, 2600, 13140), 2000),
	Insn('CAM_ROTATE', 315, 2, 0, 2000),
	Insn('CAM_DISTANCE', 19000, 2000),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(254), Text(
		'#1P它跑去那边了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0102F#1P饭店的方向啊。\n'
		'非常感谢你。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(254), -1),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('TEXT_TALK', Char(254), Text(
		'咪西它啊，\n'
		'边叫着哇啊──\n'
		'边跑到那边了哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0201F那边是饭店的方向。\n'
		'快点追上去吧，罗伊德。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('QUEST', 55, Insn('TASK_SET', 4)),
	Insn('0x4B', Char(254), -1),
	Insn('TEXT_TALK', Char(254), Text(
		'咪西是吗……？\n'
		'嗯，我刚才有看到。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'不知为何，它用很惊人的气势\n'
		'冲过走廊，然后就跑走了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0310F#1P唉～又没赶上啊。{wait}'
		'\n'
		'#0300F那么，它朝哪边去了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'嗯，从方向来看，\n'
		'我想应该是住宅区那边。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0101F#4P关于咪西，\n'
		'它的样子看起来怎样呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'它边冲刺着、边跳着\n'
		'诡异的舞蹈。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F#1P舞蹈……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'双手不断挥来挥去，\n'
		'简直像是要甩掉什么一样，\n'
		'是这种感觉的舞蹈。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0309F#1P它在搞什么啊？\n'
		'小缇，你知道些什么吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0201F#3P该不会……\n'
		'它被人施了某种魔法，\n'
		'并且受到操控了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0305F#1P操控？为了什么？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0201F#3P我也不清楚。但是……\n'
		'总觉得有股可怕的犯罪气息。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0012F#1P（我觉得事情好像朝\n'
		'\u3000完全错误的方向发展了……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'话说回来……为什么\n'
		'主题乐园的吉祥物会在\n'
		'我们饭店里全速奔跑呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F#1P这、这个嘛……那个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0207F#3P因、因为它运动不足！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'运动不足是吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0201F#3P没错。\n'
		'咪西为了健康管理，\n'
		'所以在进行适度运动！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'虽然这理由让人\n'
		'有点无法接受，不过……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'既然客人都这么说了，\n'
		'那就当作是这样吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0012F#1P（呼……好险啊。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(254), -1),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('TEXT_TALK', Char(254), Text(
		'如果是指咪西的话，\n'
		'它刚才用惊人的气势\n'
		'冲刺经过走廊跑走啰。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'从方向来看，\n'
		'我想应该是往住宅区去了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0201F我有危险的预感。\n'
		'我们快赶往住宅区吧，罗伊德。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_ROTATE', Char(13), 60, 0),
		Insn('0x9B', b'\x00', Char(13), b'-\x00\xb8\x0b\x00\x00(#\x00\x00\x01'),
		Insn('CHAR_ROTATE', Char(13), 105, 0),
		Insn('0x9B', b'\x00', Char(13), b'-\x00\xb8\x0b\x00\x00(#\x00\x00\x01'),
		Insn('CHAR_ROTATE', Char(13), 150, 0),
		Insn('0x9B', b'\x00', Char(13), b'-\x00\xb8\x0b\x00\x00(#\x00\x00\x01'),
		Insn('CHAR_ROTATE', Char(13), 195, 0),
		Insn('0x9B', b'\x00', Char(13), b'-\x00\xb8\x0b\x00\x00(#\x00\x00\x01'),
		Insn('CHAR_ROTATE', Char(13), 240, 0),
		Insn('0x9B', b'\x00', Char(13), b'-\x00\xb8\x0b\x00\x00(#\x00\x00\x01'),
		Insn('CHAR_ROTATE', Char(13), 285, 0),
		Insn('0x9B', b'\x00', Char(13), b'-\x00\xb8\x0b\x00\x00(#\x00\x00\x01'),
		Insn('CHAR_ROTATE', Char(13), 330, 0),
		Insn('0x9B', b'\x00', Char(13), b'-\x00\xb8\x0b\x00\x00(#\x00\x00\x01'),
		Insn('CHAR_ROTATE', Char(13), 15, 0),
		Insn('0x9B', b'\x00', Char(13), b'-\x00\xb8\x0b\x00\x00(#\x00\x00\x01'),
	]),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('SLEEP', 250),
		Insn('0x98', Char(260), (-300, 0, 0), 2000, 0),
		Insn('SLEEP', 100),
		Insn('0x98', Char(260), (500, 0, 0), 6000, 0),
		Insn('SLEEP', 1100),
		Insn('0x98', Char(260), (-200, 0, 0), 2000, 0),
		Insn('SLEEP', 350),
	]),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('0x98', Char(257), (-300, 0, 0), 2000, 0),
		Insn('0x98', Char(257), (500, 0, 0), 6000, 0),
		Insn('SLEEP', 1250),
		Insn('0x98', Char(257), (-200, 0, 0), 2000, 0),
		Insn('SLEEP', 550),
	]),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_ANIMATION', Char(13), 1500, [
			0,
			1,
			2,
			3,
			4,
			5,
		]),
	]),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('SOUND_PLAY', 612, 0, 0, 100),
		Insn('0x9C', Char(13), b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x01\x00\x00\xa0\x0f\x00\x00'),
		Insn('SLEEP', 400),
		Insn('SOUND_PLAY', 612, 0, 0, 100),
		Insn('0x9C', Char(13), b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x01\x00\x00\xa0\x0f\x00\x00'),
		Insn('CHAR_ROTATE', Char(13), 90, 1000),
		Insn('0x9B', b'\x00', Char(13), b'\x00\x00\x88\x13\x00\x00(#\x00\x00\x01'),
		Insn('SOUND_PLAY', 612, 0, 0, 100),
		Insn('0x9C', Char(13), b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x01\x00\x00\xa0\x0f\x00\x00'),
		Insn('SLEEP', 400),
		Insn('SOUND_PLAY', 612, 0, 0, 100),
		Insn('0x9C', Char(13), b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x01\x00\x00\xa0\x0f\x00\x00'),
		Insn('CHAR_ROTATE', Char(13), 270, 1000),
		Insn('0x9B', b'\x00', Char(13), b'\x00\x00\x88\x13\x00\x00(#\x00\x00\x01'),
	]),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('EXPR_CHAR_ATTR', Char(13), 40, Expr([Insn('CONST', 13), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('SOUND_PLAY', 612, 0, 0, 100),
		Insn('0x9C', Char(13), b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x01\x00\x00\xb8\x0b\x00\x00'),
		Insn('SLEEP', 600),
	]),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CAM_OFFSET', (34220, -910, -600), 0),
	Insn('CAM_ROTATE', 319, 19, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 23000, 0),
	Insn('CHAR_SET_POS', Char(257), (33750, -2000, -1000), 270),
	Insn('CHAR_SET_POS', Char(258), (33750, -2000, 450), 270),
	Insn('CHAR_SET_POS', Char(259), (35000, -2000, -1000), 270),
	Insn('CHAR_SET_POS', Char(260), (35000, -2000, 450), 270),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(337), (36250, -2000, -320), 270),
		]),
		(None, []),
	]),
	Insn('SOUND_STOP', 126),
	Insn('BGM_STOP', 500),
	Insn('FORK_FUNC', Char(13), 0, Function((1, 11))),
	Insn('EMOTE', Char(13), 0, 2300, (40, 43, 100, 0)),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(259), Text(
		'#0207F#11P罗伊德，在那里……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('SLEEP', 50),
			Insn('EMOTE', Char(337), 0, 2000, (2, 7, 80, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
		]),
		(None, []),
	]),
	Insn('SLEEP', 1500),
	Insn('BGM_PLAY', b'\xfb\x01\x00'),
	Insn('CAM_OFFSET', (550, 0, -570), 3000),
	Insn('CAM_DISTANCE', 27000, 3000),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(13), Text(
		'{color 10}#5P呜哇～～！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (14060, -2000, -2640), 6000, 0),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (14680, -2000, -1370), 6000, 0),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (15500, -2000, -220), 6000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (14000, -2000, 960), 6000, 0),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('SLEEP', 50),
			Insn('FORK', 337, 1, [
				Insn('0x95', Char(254), (15000, -2000, 960), 6000, 0),
			]),
		]),
		(None, []),
	]),
	Insn('CAM_OFFSET', (8720, -200, -1500), 3000),
	Insn('CAM_DISTANCE', 27500, 3000),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('FORK_AWAIT', Char(337), 1),
		]),
		(None, []),
	]),
	Insn('0x6F', b'\x10'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0105F#5P它用感觉很惊人的气势\n'
		'在四处奔跑呢……{wait}'
		'{page}'
		'#0101F是有什么恐怖的东西吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(260), 500),
	Insn('SLEEP', 50),
	Insn('TEXT_TALK', Char(257), Text(
		'#0013F#2P兰迪，我们两个人\n'
		'联手来阻止它。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(259), 500),
	Insn('SLEEP', 50),
	Insn('TEXT_TALK', Char(257), Text(
		'#0007F#2P可能会有危险，艾莉跟缇欧\n'
		'在这里待命。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (11350, -2000, -2190), 2000, 0),
	]),
	Insn('TEXT_TALK', Char(260), Text(
		'#0301F了解！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (11550, -2000, -350), 2000, 0),
	]),
	Insn('FORK', 258, 1, [
		Insn('0x96', Char(254), (15400, -2000, -1500), 2000, 0),
	]),
	Insn('TEXT_TALK', Char(258), Text(
		'#0101F#5P我明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0201F#2P了解……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('CAM_OFFSET', (880, -270, -3870), 2000),
	Insn('CAM_ROTATE', 348, 13, 0, 2000),
	Insn('0x6E', 400, 2000),
	Insn('CAM_DISTANCE', 27500, 2000),
	Insn('0x6F', b'\x10'),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (4490, -1800, -3270), 6000, 0),
	]),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (5270, -1800, 1390), 6000, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('CHAR_ROTATE', Char(260), 315, 0),
	Insn('CHAR_ROTATE', Char(257), 225, 0),
	Insn('EMOTE', Char(260), 0, 2000, (40, 43, 100, 0)),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 0)),
	Insn('SLEEP', 1200),
	Insn('FORK_LOOP', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(13), 0),
	]),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(13), 0),
	]),
	Insn('FORK_FUNC', Char(260), 1, Function((1, 12))),
	Insn('FORK_FUNC', Char(257), 1, Function((1, 13))),
	Insn('TEXT_TALK', Char(260), Text(
		'#0307F#4P喂！不许动！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (13870, -1080, -550), 1000),
	Insn('CAM_ROTATE', 0, 6, 0, 1000),
	Insn('CAM_DISTANCE', 27000, 1000),
	Insn('0x6F', b'\x01'),
	Insn('FORK_QUIT', Char(13), 0),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('CHAR_SET_POS', Char(13), (330, -1800, -190), 90),
	Insn('TEXT_TALK', Char(257), Text(
		'#0011F#2P拜托你停下来！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'{color 10}#4P呜哇～～！！\n'
		'谁、谁来救救我～～！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F#11P…………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F#12P缇欧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x97', Char(259), (-500, 0, 0), 2000, 0),
	Insn('TEXT_TALK', Char(259), Text(
		'#0201F#11P再这样下去也不是办法。\n'
		'我也加入他们去抓住咪西。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_WALK_TO', Char(258), Char(259), 3000, 2000, 0),
	Insn('TEXT_TALK', Char(258), Text(
		'#0105F#12P不、不行啦！\n'
		'罗伊德叫我们\n'
		'在这里待命哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0207F#11P可是……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'{color 10}#2P让开让开让开～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0205F#11P咦？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_SET_VOLUME', b'\x00\xd0\x07\x00\x00'),
	Insn('0x14', b'\x00\x00\x00\x00\xff\xff\xff\xbb\x00\x00\x00\x00\x01\xc8\x00\x00\x00'),
	Insn('0x15', b'\xd0\x07\x00\x00'),
	Insn('CAM_OFFSET', (13290, -200, -930), 1500),
	Insn('CAM_ROTATE', 315, 5, 0, 1500),
	Insn('CAM_DISTANCE', 30000, 1500),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 150),
	Insn('CHAR_WALK_TO', Char(13), Char(259), 1000, 10000, 0),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('0x6F', b'\x10'),
	Insn('SOUND_PLAY', 298, 0, 0, 100),
	Insn('FADE_ON', 250, Color(0x00FFFFFF), 255),
	Insn('TEXT_TALK', Char(259), Text(
		'#0210F#2P呜哇啊！{wait}'
	)),
	Insn('TEXT_TALK', Char(13), Text(
		'{color 10}#3P好痛～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('LOAD_CHCP', 'apl/ch50411', 30),
	Insn('LOAD_CHCP', 'chr/ch00156', 31),
	Insn('LOAD_CHCP', 'apl/ch50393', 32),
	Insn('CAM_OFFSET', (16510, -200, -1480), 0),
	Insn('CAM_ROTATE', 329, 27, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 21500, 0),
	Insn('CHAR_FLAG1_SET', Char(259), 2),
	Insn('CHAR_FLAG1_SET', Char(259), 16),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(13), 2),
	Insn('CHAR_FLAG1_SET', Char(13), 16),
	Insn('CHAR_FLAG1_SET', Char(13), 4),
	Insn('CHAR_SET_CHCP', Char(259), 30),
	Insn('CHAR_SET_FRAME', Char(259), 31),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_SET_CHCP', Char(13), 32),
	Insn('CHAR_SET_FRAME', Char(13), 0),
	Insn('CHAR_SET_POS', Char(259), (16110, -2300, 1710), 180),
	Insn('CHAR_SET_POS', Char(258), (17000, -2000, 1980), 205),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(337), (13000, -2000, 3300), 90),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_POS', Char(13), (12850, -2000, -4150), 60),
	Insn('FORK_FUNC', Char(13), 1, Function((1, 14))),
	Insn('SOUND_PLAY', 819, 0, 0, 100),
	Insn('EMOTE_STOP', Char(13)),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('EMOTE', Char(259), 0, 1600, (48, 50, 150, 0)),
	Insn('SOUND_PLAY', 24, 0, 0, 100),
	Insn('EMOTE', Char(13), 0, 2200, (48, 50, 150, 0)),
	Insn('SOUND_PLAY', 24, 0, 0, 100),
	Insn('SOUND_PLAY', 126, 0, 1, 80),
	Insn('FADE_OFF', 2000, Color(0x00FFFFFF)),
	Insn('0x0D'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WALK_TO', Char(254), Char(259), 1000, 6000, 0),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#15A#30W#0011F缇欧！{wait}'
	)),
	Insn('SLEEP', 2500),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WALK_TO', Char(254), Char(259), 2200, 6000, 0),
	]),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#13A#30W#0305F小缇！你没事吧！？{wait}'
	)),
	Insn('SLEEP', 3000),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('TEXT_TALK', Char(259), Text(
		'#0206F#2P晕～…{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F#3P她昏倒了……\n'
		'乍看之下似乎是没有受伤。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0101F#4P暂时让她静躺着休息吧。\n'
		'罗伊德，你看一下咪西。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('CHAR_WATCH', Char(257), Char(13), 500),
	Insn('CHAR_WATCH', Char(260), Char(13), 600),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_WATCH', Char(337), Char(13), 600),
		]),
		(None, []),
	]),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F#4P说、说的也是。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WALK_TO', Char(257), Char(13), 2200, 6000, 0),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F#2P你没事吧？\n'
		'振作点！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE_STOP', Char(13)),
	Insn('TEXT_TALK', Char(13), Text(
		'{color 10}#5P呃、嗯～…{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_QUIT', Char(13), 1),
	Insn('CHAR_ANIMATION', Char(13), 1000, [
		0,
		1,
		2,
		3,
		4,
		5,
	]),
	Insn('CHAR_ANIMATION', Char(13), 500, [
		0,
		1,
		2,
		3,
		4,
		5,
	]),
	Insn('FORK_LOOP', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(13), 0),
	]),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(13), 0),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('FORK_LOOP', 337, 2, [
				Insn('CHAR_WATCH', Char(254), Char(13), 0),
			]),
		]),
		(None, []),
	]),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(13), 5),
	Insn('CHAR_SET_FRAME', Char(13), 0),
	Insn('CHAR_FLAG1_UNSET', Char(13), 2),
	Insn('CHAR_FLAG1_UNSET', Char(13), 16),
	Insn('CHAR_FLAG1_UNSET', Char(13), 4),
	Insn('SLEEP', 1500),
	Insn('0x95', Char(13), (14350, -2000, -3220), 1000, 0),
	Insn('EMOTE', Char(13), 0, 2300, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(13), Text(
		'{color 10}#5P啊！\n'
		'呜、呜哇啊！救命呀！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_SET_VOLUME', b'd\xe8\x03\x00\x00'),
	Insn('EMOTE', Char(13), 0, 2300, (40, 43, 100, 0)),
	Insn('FORK_FUNC', Char(13), 1, Function((1, 15))),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(258), 255),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x49'),
	Insn('0xD5', 31),
	Insn('0x0D'),
	Insn('FORK_LOOP', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(13), 0),
	]),
	Insn('TEXT_TALK', Char(258), Text(
		'#0105F#4P你、你冷静点！\n'
		'我们是打算\n'
		'保护你……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'{color 10}#5P蜜、蜜蜂！里面有蜜蜂！\n'
		'蜜蜂跑进布偶装里了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0305F#4P……蜜蜂？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F#1P该不会，咪西四处逃跑\n'
		'是因为……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0105F#4P有蜜蜂跑进布偶装\n'
		'里面的关系……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'{color 10}#5P谁、谁快来救救我……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 1500),
	Insn('FORK_QUIT', Char(13), 1),
	Insn('0x95', Char(13), (16110, -2000, -3220), 9000, 0),
	Insn('EMOTE_STOP', Char(13)),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('FORK_QUIT', Char(258), 2),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('FORK_QUIT', Char(337), 2),
		]),
		(None, []),
	]),
	Insn('CHAR_WATCH', Char(13), Char(260), 500),
	Insn('EMOTE', Char(13), 0, 2300, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(13)),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(13), 0, 2300, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(13), Text(
		'{color 10}#5P……咦？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0306F#4P喂喂喂，这次又怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'{color 10}#5P没听到蜜蜂振翅的声音……\n'
		'明明到刚刚为止都在我耳边嗡嗡叫。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0305F#4P你说什么？\n'
		'那么蜜蜂究竟\n'
		'跑去哪里了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0012F#4P大概是……\n'
		'刚才跟缇欧撞上的冲击，\n'
		'导致蜜蜂被压扁了吧……在里面。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(260), Text(
		'#0310F#4P呃！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'{color 10}#5P呼……\n'
		'得救了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0102F#4P呃……问题似乎已经解决了，\n'
		'快点将它带回委托人那边\n'
		'应该比较好吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F#4P那倒也是。\n'
		'等缇欧醒来后\n'
		'就带它走吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(13), Char(259), 500),
	Insn('TEXT_TALK', Char(13), Text(
		'{color 10}#5P缇欧？你是指倒在那里的\n'
		'小不点吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE_STOP', Char(259)),
	Insn('CHAR_WATCH', Char(257), Char(259), 500),
	Insn('CHAR_WATCH', Char(260), Char(259), 500),
	Insn('CHAR_WATCH', Char(258), Char(259), 500),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_WATCH', Char(337), Char(259), 500),
		]),
		(None, []),
	]),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(259), Text(
		'#0210F#6P呃、嗯……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ANIMATION', Char(259), 1000, [
		31,
		30,
		29,
	]),
	Insn('SLEEP', 2000),
	Insn('CHAR_ANIMATION', Char(259), 1000, [
		31,
		30,
		29,
	]),
	Insn('SLEEP', 300),
	Insn('CHAR_ANIMATION', Char(259), 1000, [
		31,
		30,
		29,
	]),
	Insn('SLEEP', 1000),
	Insn('CROSSFADE', 250),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('CHAR_ANIMATION', Char(259), 1000, [
		30,
		31,
		32,
		33,
		34,
		35,
		36,
		37,
	]),
	Insn('0x0D'),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(259), Text(
		'#211F……咦？罗伊德？\n'
		'我……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(259), 255),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_FLAG1_UNSET', Char(259), 2),
	Insn('CHAR_FLAG1_UNSET', Char(259), 16),
	Insn('CHAR_FLAG1_UNSET', Char(259), 4),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x49'),
	Insn('0xD5', 30),
	Insn('0x0D'),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(259), Text(
		'#205F#6P对了！咪西呢！？{wait}'
		'{page}'
		'#207F#6P它没事吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F#1P嗯，问题已经解决了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_LOOP', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(13), 0),
	]),
	Insn('FORK_LOOP', 257, 2, [
		Insn('CHAR_WATCH', Char(254), Char(13), 0),
	]),
	Insn('FORK_LOOP', 259, 2, [
		Insn('CHAR_WATCH', Char(254), Char(13), 0),
	]),
	Insn('FORK_LOOP', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(13), 0),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('FORK_LOOP', 337, 2, [
				Insn('CHAR_WATCH', Char(254), Char(13), 0),
			]),
		]),
		(None, []),
	]),
	Insn('0x97', Char(259), (0, 0, -700), 1000, 0),
	Insn('SOUND_PLAY', 86, 0, 0, 100),
	Insn('CHAR_ROTATE', Char(13), 90, 900),
	Insn('CHAR_ROTATE', Char(13), 180, 900),
	Insn('CHAR_ROTATE', Char(13), 270, 900),
	Insn('CHAR_ROTATE', Char(13), 0, 900),
	Insn('CHAR_ROTATE', Char(13), 90, 900),
	Insn('CHAR_ROTATE', Char(13), 180, 900),
	Insn('CHAR_ROTATE', Char(13), 270, 900),
	Insn('CHAR_ROTATE', Char(13), 0, 900),
	Insn('SLEEP', 1000),
	Insn('FORK_QUIT', Char(260), 2),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('FORK_QUIT', Char(258), 2),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('FORK_QUIT', Char(337), 2),
		]),
		(None, []),
	]),
	Insn('FORK_LOOP', 13, 2, [
		Insn('0xA0', Char(254), 1500, 64256),
	]),
	Insn('FORK_FUNC', Char(13), 1, Function((1, 16))),
	Insn('TEXT_TALK', Char(13), Text(
		'{color 10}#1P咪西西☆\n'
		'我没事～噗！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(13), Text(
		'{color 10}#1P这都是托你的福呀！\n'
		'谢谢你啰☆{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 300, 1600, (54, 57, 250, 0)),
	Insn('SOUND_PLAY', 186, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(259), Text(
		'#0200F#2P咪西……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0305F#4P（变身的程度也太恐怖了……\n'
		'\u3000居然连声音都改变了。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#0012F#1P（里面的人也很辛苦呢……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(13), 1),
	Insn('FORK_QUIT', Char(13), 2),
	Insn('EMOTE_STOP', Char(259)),
	Insn('QUEST', 55, Insn('TASK_SET', 5)),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 't1030', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('EFF_LOAD', ResId(0), 'event\\ev309_00.eff'),
	Insn('CHAR_SET_POS', Char(257), (-2050, 0, -43940), 90),
	Insn('CHAR_SET_POS', Char(258), (-2490, 0, -44620), 90),
	Insn('CHAR_SET_POS', Char(259), (-2330, 0, -45400), 90),
	Insn('CHAR_SET_POS', Char(260), (-2880, 0, -46460), 90),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(337), (-3300, 0, -47000), 90),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_POS', Char(10), (2180, 0, -43910), 270),
	Insn('CHAR_SET_POS', Char(8), (2720, 0, -45860), 270),
	Insn('0x4B', Char(8), -1),
	Insn('FORK_FUNC', Char(10), 1, Function((1, 22))),
	Insn('CAM_OFFSET', (50, 12580, -45830), 0),
	Insn('CAM_ROTATE', 359, 7, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 19000, 0),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('EFF_PLAY', (ResId(0), 0), Char(255), 0, 0, 0, 250, 0, 21536, -1, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('CAM_OFFSET', (50, 2200, -45830), 6000),
	Insn('CAM_ROTATE', 0, 3, 0, 6000),
	Insn('CAM_DISTANCE', 20000, 6000),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('EFF_STOP', (ResId(0), 0)),
	Insn('FORK_QUIT', Char(10), 1),
	Insn('0x4B', Char(10), -1),
	Insn('TEXT_TALK', Char(8), Text(
		'唉呀，真是得救了！\n'
		'真不知道该怎么道谢才好……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'不过，没想到是因为蜜蜂\n'
		'造成恐慌……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0309F我们还以为是诱旋之类的，\n'
		'结果居然是这样，太夸张了啦，\n'
		'对吧？小缇？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0203F…………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0002F哎呀，这不是很好吗？\n'
		'在事情闹大之前就结束了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'各位说得没错。\n'
		'平安无事才是最好的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0201F呃……\n'
		'咪西不会因为这次的事情\n'
		'被处罚吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'这次的事情是不幸的意外。\n'
		'我没有打算\n'
		'处罚咪西哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0206F呼……太好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'各位，真的非常感谢你们。\n'
		'这是谢礼。请你们务必收下。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'已收下{item 93}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 93, 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F谢谢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'这次虽然是以\n'
		'任务的方式前来……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'不过，下次请务必到\n'
		'本主题乐园来尽情游玩。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0302F事情才刚解决，\n'
		'马上就开始揽客了啊。\n'
		'哈哈！还真现实呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'是的，毕竟这也是我的工作。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'我会跟各位找回的咪西一起\n'
		'欢迎各位前来游玩。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0209F我一定会来……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 9, 0, 0, 100),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'达成{color 2}任务【寻找某人】{color 0}了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('QUEST', 55, Insn('FLAG_UNSET', 16)),
	Insn('CHAR_SET_POS', Char(10), (360, 4160, -15840), 180),
	Insn('CHAR_SET_POS', Char(8), (4750, 4400, 0), 180),
	Insn('0x4C', Char(10), -1),
	Insn('0x4C', Char(8), -1),
	Insn('CHAR_SET_POS', Char(0), (240, 0, -35290), 0),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('TEXT_TALK', Char(254), Text(
		'这个嘛，咪西是布偶装……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'不对不对，我说错了。\n'
		'因为咪西是猫，\n'
		'我想它应该没有离开太远才对。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'这只是我的推测，不过……\n'
		'如果它要坐船前往市街，\n'
		'我想应该是非常困难的吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('TEXT_TALK', Char(254), Text(
		'欢迎来到米修拉姆\n'
		'引以为傲的主题乐园。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'哦，真巧啊。\n'
		'各位今天是私底下\n'
		'来游玩的吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'本主题乐园\n'
		'无论何时都\n'
		'恭候各位大驾光临。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
			Insn('FLAG_SET', Flag(5)),
			Insn('TEXT_TALK', Char(254), Text(
				'{color 10}啊！是你们！\n'
				'把我从蜜蜂手中救出来的！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'{color 10}那时真是谢谢你们了！\n'
				'咪西西☆{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F……这是为什么呢？\n'
				'这种对方明明是在道谢，\n'
				'听起来却很火大的感觉。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F咪西只会治愈人的心灵，\n'
				'怎么可能会让人火大呢？{wait}'
				'{page}'
				'兰迪你的心灵太荒废了。\n'
				'我强烈建议你到《米修拉姆》\n'
				'让咪西治愈你。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'{color 10}咪西西☆\n'
				'我随时都等你来呀！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'{color 10}你好！\n'
				'欢迎来到奇幻乐园☆{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'{color 10}咪西西！要好好享受哦～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('EXPR_CHAR_ATTR', Char(10), 40, Expr([Insn('CONST', 13), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('SOUND_PLAY', 612, 0, 0, 100),
		Insn('0x9C', Char(10), b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x01\x00\x00\xb8\x0b\x00\x00'),
		Insn('SLEEP', 600),
	]),
	Insn('RETURN'),
]
