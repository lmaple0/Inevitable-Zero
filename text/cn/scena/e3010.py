# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'e3010',
	'name2': 'e3010',
	'location': 0,
	'bgm': 515,
	'flags': 8192,
	'includes': [
		None,
		None,
		None,
		None,
		None,
		None,
	],
	'name3': 'e3010',
	'labels': [],
	'chcp': [],
	'npcs': [
		{
			'name': Translate('赛尔盖课长'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('赛特'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('船'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('SE控制'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
	],
	'monsters': [],
	'triggers': [],
	'objects': [],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00', Function((0, 0)), Function((0, 1))),
	'code': [None]*9,
	'anim': [],
}

data['code'][0] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 2))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][1] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(760)), Insn('END')]), [
			Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('FLAG_UNSET', Flag(760)),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch02702', 30),
	Insn('LOAD_CHCP', 'apl/ch50542', 31),
	Insn('SOUND_LOAD', 483),
	Insn('SOUND_LOAD', 126),
	Insn('PARTY_SET_SBREAK', Party(0), 1, 0),
	Insn('0xC0'),
	Insn('IMG_LOAD', ResId(0), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis157.itp'),
	Insn('CHAR_SET_CHCP', Char(9), 30),
	Insn('CHAR_SET_FRAME', Char(9), 0),
	Insn('FORK_FUNC', Char(9), 3, Function((0, 3))),
	Insn('CHAR_SET_CHCP', Char(8), 31),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('CHAR_FLAG1_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(4), 128),
	Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(5), 128),
	Insn('CHAR_FLAG2_UNSET', Char(5), 32768),
	Insn('CHAR_SET_POS', Char(8), (0, 300, -1500), 180),
	Insn('CHAR_SET_POS', Char(307), (0, 900, 3300), 0),
	Insn('CHAR_SET_POS', Char(9), (-750, 900, 3300), 0),
	Insn('CHAR_SET_POS', Char(257), (0, 900, 300), 0),
	Insn('CHAR_SET_POS', Char(258), (-900, 900, 1000), 90),
	Insn('CHAR_SET_POS', Char(259), (900, 900, 1000), 270),
	Insn('CHAR_SET_POS', Char(260), (-900, 900, 2100), 90),
	Insn('CHAR_SET_POS', Char(261), (900, 900, 2100), 270),
	Insn('FORK_FUNC', Char(11), 0, Function((0, 7))),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('FORK_FUNC', Char(11), 1, Function((0, 4))),
	Insn('CAM_OFFSET', (690, 9850, 800), 0),
	Insn('CAM_ROTATE', 250, 6, 0, 0),
	Insn('0x6E', 650, 0),
	Insn('CAM_DISTANCE', 46340, 0),
	Insn('CAM_OFFSET', (690, 3850, 800), 5000),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1000),
	Insn('FORK_QUIT', Char(11), 0),
	Insn('FORK_QUIT', Char(11), 1),
	Insn('0x0D'),
	Insn('CROSSFADE', 1000),
	Insn('FORK_FUNC', Char(11), 1, Function((0, 5))),
	Insn('CAM_OFFSET', (160, 1750, 1530), 0),
	Insn('CAM_ROTATE', 219, 25, 0, 0),
	Insn('0x6E', 650, 0),
	Insn('CAM_DISTANCE', 15070, 0),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('FORK_QUIT', Char(11), 1),
	Insn('TEXT_TALK', Char(8), Text(
		'#13501979V#1003F#5P……原来如此。{wait}'
		'{page}'
		'#13501980V#1001F算了，彻底无视\n'
		'我的忠告这件事\n'
		'先暂且不谈……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 180, 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#13501981V#0008F#11P对、对不起……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13501982V#1000F#5P问题是那个孩子。{wait}'
		'{page}'
		'#13501983V#1003F根据事情的发展走向，\n'
		'有可能会演变成很严重的问题。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(257), 0, 500),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(307), 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(307), 300),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(307), 500),
	]),
	Insn('FORK', 261, 1, [
		Insn('CHAR_WATCH', Char(254), Char(307), 300),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(261), 1),
	Insn('TEXT_TALK', Char(260), Text(
		'#13501984V#0303F#11P是啊……{wait}'
		'{page}'
		'#13501985V#0301F在竞拍会上，差点被当作人偶\n'
		'进行拍卖的孩子……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(261), Text(
		'#13501986V#0406F#5P嗯，真是会引发很多\n'
		'不好的联想呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13501987V#0208F#5P…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13501988V#0106F#5P……真是没想到，\n'
		'我本以为，即使是黑手党，也不会\n'
		'愚蠢到做出这种事情呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(307), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_ROTATE', Char(307), 180, 500),
	Insn('TEXT_TALK', Char(307), Text(
		'#13501989V#5805F#12P嗯～？{wait}'
		'{page}'
		'#13501990V#5810F琪雅会遇到\n'
		'很不好的事情吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13501991V#0004F#5P别担心……\n'
		'我们不会让那种事情发生的。{wait}'
		'{page}'
		'#13501992V#0001F对了，琪雅。{wait}'
		'{page}'
		'#13501993V除了名字之外，\n'
		'你有没有想起其它的事情呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(307), Text(
		'#13501994V#5811F#12P嗯……{wait}'
		'{page}'
		'#13501995V#5809F……嘿嘿嘿，\n'
		'完全想不起来哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13501996V#0006F#5P是吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13501997V#0108F#5P这可麻烦了呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13501998V#0308F#11P………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#13501999V#0001F#5P说起来，兰迪……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(260), Char(257), 400),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#13502000V#0304F#11P──哦，关于我的事情，\n'
		'以后有机会时会告诉你们的。{wait}'
		'{page}'
		'#13502001V#0300F……如果我还能\n'
		'继续留在支援课的话。{wait}'
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
	Insn('SLEEP', 1000),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(260), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(260), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 261, 1, [
		Insn('CHAR_WATCH', Char(254), Char(260), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(261), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#13502002V#0013F#5P……我要生气了，兰迪。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13502003V#0201F#6P兰迪前辈，\n'
		'想开玩笑也要看看气氛啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13502004V#0101F#5P嗯，不要说那种\n'
		'根本不好笑的玩笑啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13502005V#0302F#11P………抱歉。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(307), Text(
		'#13502006V#5801F#12P嗯……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(307), Char(9), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(307), Text(
		'#13502007V#5810F#6P喂，狗狗，\n'
		'罗伊德他们怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'#13502008V#1203F#11P呜噜噜噜……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(261), 0, 400),
	Insn('TEXT_TALK', Char(261), Text(
		'#13502009V#0409F#5P呵呵，这也算是\n'
		'青春的一种吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(307), 180, 500),
	Insn('TEXT_TALK', Char(307), Text(
		'#13502010V#5805F#12P青春～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(260), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(307), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(307), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(307), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(260), Text(
		'#13502011V#0309F#11P哈哈……\n'
		'一点都不紧张了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13502012V#0012F#5P说起来，\n'
		'直到刚才，我们还一直处在\n'
		'被黑手党追击的危机中呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13502013V#0102F#5P总觉得没有什么真实感呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13502014V#0202F#5P……但很遗憾，\n'
		'那些并不是梦啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#13502015V#1004F#5P呵呵……{wait}'
		'{page}'
		'#13502016V#1002F算了，总之，一切事情\n'
		'都等回到支援课之后再说吧。{wait}'
		'{page}'
		'#13502017V我想，从明天开始……\n'
		'暂时就要进入严守戒备的状态了。{wait}'
	)),
	Insn('TEXT_WAIT'),
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
	Insn('SLEEP', 50),
	Insn('FORK', 261, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(261), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#13502018V#0001F#12P……是……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(307), Text(
		'#13502019V#5809F#12P是～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (0, 6850, -23170), 0),
	Insn('CAM_ROTATE', 180, 1, 0, 0),
	Insn('0x6E', 550, 0),
	Insn('CAM_DISTANCE', 35770, 0),
	Insn('CAM_OFFSET', (0, 6850, 20170), 6000),
	Insn('FORK_FUNC', Char(11), 1, Function((0, 6))),
	Insn('0x0D'),
	Insn('SLEEP', 4000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('FORK_AWAIT', Char(11), 0),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('FLAG_SET', Flag(722)),
	Insn('FLAG_UNSET', Flag(723)),
	Insn('0xBA', 4),
	Insn('0x2F', b'\x04\x00'),
	Insn('0x2F', b'2\x00'),
	Insn('QUEST', 68, Insn('FLAG_UNSET', 16)),
	Insn('QUEST', 71, Insn('FLAG_UNSET', 16)),
	Insn('QUEST', 69, Insn('FLAG_UNSET', 32)),
	Insn('ITEM_REMOVE', 809, 1),
	Insn('ITEM_REMOVE', 810, 1),
	Insn('ITEM_REMOVE', 816, 1),
	Insn('ITEM_REMOVE', 731, 1),
	Insn('ITEM_REMOVE', 840, 1),
	Insn('ITEM_REMOVE', 839, 1),
	Insn('ITEM_REMOVE', 827, 1),
	Insn('ITEM_REMOVE', 844, 1),
	Insn('ITEM_REMOVE', 847, 1),
	Insn('ITEM_REMOVE', 845, 1),
	Insn('ITEM_REMOVE', 846, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1106)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(1106)),
			Insn('FLAG_SET', Flag(1107)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 9))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 10))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 58, Insn('TASK_GET', 11))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 58, Insn('FLAG_GET', 32))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 58, Insn('TASK_SET', 14)),
			Insn('FLAG_SET', Flag(1107)),
		]),
		(None, []),
	]),
	Insn('0xE3', 10),
	Insn('SLEEP', 1000),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 800, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('TEXT_RESET', b'\x03'),
	Insn('0xE3', 3),
	Insn('SLEEP', 100),
	Insn('MINIGAME', 43, 0, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
	Insn('0xDE', b"'\x00"),
	Insn('0xDE', b'\x1e\x00'),
	Insn('0xDE', b'\x1f\x00'),
	Insn('SLEEP', 100),
	Insn('CAM_OFFSET', (-1000000, 0, 0), 0),
	Insn('0xC7', b'\x00\x10\x00\x00\x00'),
	Insn('EXPR_ATTR', 80, Expr([Insn('CONST', 4), Insn('SET'), Insn('END')])),
	Insn('FLAG_SET', Flag(760)),
	Insn('EXPR_ATTR', 49, Expr([Insn('CONST', 153), Insn('SET'), Insn('END')])),
	Insn('SAVE'),
	Insn('FLAG_UNSET', Flag(760)),
	Insn('MINIGAME', 43, 1, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 800, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xC7', b'\x01\x10\x00\x00\x00'),
	Insn('0xE3', 11),
	Insn('EXPR_ATTR', 4, Expr([Insn('CONST', 4), Insn('SET'), Insn('END')])),
	Insn('SOUND_STOP', 483),
	Insn('SOUND_STOP', 126),
	Insn('FLAG_SET', Flag(747)),
	Insn('NEW_SCENE', 'c0110', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('EXPR_CHAR_ATTR', Char(254), 7, Expr([Insn('CONST', 1700), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_ANIMATION', Char(254), 1000, [
			0,
			1,
			2,
			1,
			0,
			3,
			4,
			3,
		]),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('SOUND_PLAY', 483, 0, 2, 0),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 483, 10),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 483, 20),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 483, 30),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 483, 40),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 483, 50),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 483, 60),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('SOUND_LOOP', 483, 70),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 483, 80),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 483, 90),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 483, 100),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('SLEEP', 2500),
	Insn('SOUND_LOOP', 483, 90),
	Insn('SLEEP', 400),
	Insn('SOUND_LOOP', 483, 80),
	Insn('SLEEP', 400),
	Insn('SOUND_LOOP', 483, 70),
	Insn('SLEEP', 400),
	Insn('SOUND_LOOP', 483, 60),
	Insn('SLEEP', 400),
	Insn('SOUND_LOOP', 483, 50),
	Insn('SLEEP', 400),
	Insn('SOUND_LOOP', 483, 40),
	Insn('SLEEP', 400),
	Insn('SOUND_LOOP', 483, 30),
	Insn('SLEEP', 400),
	Insn('FORK_FUNC', Char(11), 0, Function((0, 8))),
	Insn('SOUND_LOOP', 483, 20),
	Insn('SLEEP', 400),
	Insn('SOUND_LOOP', 483, 10),
	Insn('SLEEP', 400),
	Insn('SOUND_STOP', 483),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('SOUND_PLAY', 126, 0, 2, 0),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 126, 10),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 126, 20),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 126, 30),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 126, 40),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 126, 50),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 126, 60),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 126, 70),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 126, 80),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('SOUND_LOOP', 126, 60),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 126, 50),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 126, 40),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 126, 30),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 126, 20),
	Insn('SLEEP', 200),
	Insn('SOUND_LOOP', 126, 10),
	Insn('SLEEP', 200),
	Insn('SOUND_STOP', 126),
	Insn('RETURN'),
]
