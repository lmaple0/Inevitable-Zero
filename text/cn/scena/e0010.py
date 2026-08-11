# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'e0010',
	'name2': 'e0010',
	'location': 0,
	'bgm': 0,
	'flags': 8192,
	'includes': [
		None,
		None,
		None,
		None,
		None,
		None,
	],
	'name3': 'e0010',
	'labels': [],
	'chcp': [],
	'npcs': [
		{
			'name': Translate('驾驶员'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('乘客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('乘客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('乘客'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('黑发女性'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('老婆婆'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('老人'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('贸易商'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('女性'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('哥哥'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('妹妹'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('父亲'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('男孩'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x00\x00\xff\xff',
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
	'code': [None]*20,
	'anim': [],
}

data['code'][0] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 2))),
		]),
		(Expr([Insn('FLAG', Flag(737)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(737)),
			Insn('EVENT', Function((0, 4))),
		]),
		(Expr([Insn('FLAG', Flag(738)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(738)),
			Insn('EVENT', Function((0, 5))),
		]),
		(Expr([Insn('FLAG', Flag(739)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(739)),
			Insn('EVENT', Function((0, 15))),
		]),
		(Expr([Insn('FLAG', Flag(740)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(740)),
			Insn('EVENT', Function((0, 19))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][1] = [
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('LOAD_CHCP', 'chr/ch00202', 32),
	Insn('LOAD_CHCP', 'chr/ch00302', 33),
	Insn('LOAD_CHCP', 'apl/ch50119', 34),
	Insn('LOAD_CHCP', 'chr/ch20402', 35),
	Insn('LOAD_CHCP', 'chr/ch20302', 36),
	Insn('LOAD_CHCP', 'chr/ch22302', 37),
	Insn('SOUND_LOAD', 468),
	Insn('CAM_OFFSET', (46910, 1100, -180), 0),
	Insn('CAM_ROTATE', 328, 24, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 16350, 0),
	Insn('CAM_OFFSET', (52300, 1100, -180), 10000),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 2),
	Insn('CHAR_SET_CHCP', Char(259), 32),
	Insn('CHAR_SET_FRAME', Char(259), 2),
	Insn('CHAR_SET_CHCP', Char(260), 33),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_SET_CHCP', Char(8), 34),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('CHAR_SET_CHCP', Char(9), 35),
	Insn('CHAR_SET_FRAME', Char(9), 0),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('CHAR_SET_CHCP', Char(10), 36),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG2_UNSET', Char(11), 32768),
	Insn('CHAR_SET_CHCP', Char(11), 37),
	Insn('CHAR_SET_FRAME', Char(11), 0),
	Insn('CHAR_SET_POS', Char(257), (52250, 0, 800), 0),
	Insn('CHAR_SET_POS', Char(258), (55000, 150, 200), 270),
	Insn('CHAR_SET_POS', Char(259), (55000, 150, 1450), 270),
	Insn('CHAR_SET_POS', Char(260), (53300, 150, 1700), 180),
	Insn('CHAR_SET_POS', Char(8), (43870, -200, 1800), 270),
	Insn('CHAR_SET_POS', Char(9), (46150, 150, -1840), 270),
	Insn('CHAR_SET_POS', Char(10), (48050, 150, 1880), 270),
	Insn('CHAR_SET_POS', Char(11), (48050, 150, 880), 270),
	Insn('0x7D', b'\xff\xd2\xc8\x00\x00\x00\x00\x00'),
	Insn('SOUND_PLAY', 468, 0, 2, 100),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 3))),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101647V#0000F#6P………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101648V#0100F#6P黄昏的景色真美呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101649V#0203F#4P是啊……\n'
		'感觉美丽得有些让人不敢直视。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101650V#0304F#11P哈～话说，导力车\n'
		'还真是好方便啊。{wait}'
		'{page}'
		'#11101651V#0300F不过，咱们支援课要是也能\n'
		'配备专用车就更好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(260), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101652V#0006F#6P唉，应该很难吧。{wait}'
		'{page}'
		'#11101653V#0000F虽然其它搜查课\n'
		'好像都有自己的车…{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_CHCP', Char(259), 32),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101654V#0200F#4P……确实，在搜查一课，\n'
		'每名调查员应该都配备有\n'
		'自己的专用车辆呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_CHCP', Char(260), 33),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('CHAR_ROTATE', Char(257), 90, 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101655V#0005F#5P是、是吗！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101656V#0106F#6P那样的话，待遇也\n'
		'实在是太过优厚了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101657V#0306F#5P哎呀呀……这种时候就更加感觉\n'
		'不被重视很辛苦了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101658V#0006F#5P算了，没有的东西，\n'
		'再想也没有用……{wait}'
		'{page}'
		'#11101659V#0000F而且，你们不觉得\n'
		'徒步穿越街道也是一种很好的锻炼吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101660V#0203F#4P虽然并非本意……\n'
		'但也许确实如此呢。{wait}'
		'{page}'
		'#11101661V#0211F不过，今天已经没有时间\n'
		'再继续调查下去了吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101662V#0003F#5P嗯，剩下的就是北部的矿山镇了。{wait}'
		'{page}'
		'#11101663V#0000F就按照刚才说的那样，\n'
		'今天先回去整理一下调查报告书，\n'
		'明天再去拜访那里吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11101664V#0206F#4P呼……了解。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11101665V#0109F#6P呵呵……\n'
		'今天还真是累了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_CHCP', Char(260), 33),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('SLEEP', 200),
	Insn('EMOTE', Char(260), 0, 1700, (10, 11, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(260), Text(
		'#11101666V#0309F#11P嗯……\n'
		'不过，赛西儿小姐真是太棒了。{wait}'
		'{page}'
		'#11101667V#0307F好，要是下次有机会，就以\n'
		'联谊会的名义，与她拉近个人关系吧……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(258), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(259), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('CHAR_WATCH', Char(257), Char(260), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11101668V#0006F#6P兰迪真有精神啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(257), 3),
	Insn('FORK_FUNC', Char(21), 0, Function((0, 16))),
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
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('0x49'),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0xD5', 33),
	Insn('0xD5', 34),
	Insn('0xD5', 35),
	Insn('0xD5', 36),
	Insn('0xD5', 37),
	Insn('FORK_AWAIT', Char(21), 0),
	Insn('SOUND_STOP', 468),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'r1500', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('0x82', 10, 10, 3000, 500),
		Insn('SLEEP', 500),
	]),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('LOAD_CHCP', 'chr/ch00202', 32),
	Insn('LOAD_CHCP', 'chr/ch00302', 33),
	Insn('LOAD_CHCP', 'chr/ch21102', 34),
	Insn('LOAD_CHCP', 'chr/ch21602', 35),
	Insn('LOAD_CHCP', 'apl/ch50382', 36),
	Insn('SOUND_LOAD', 468),
	Insn('CAM_OFFSET', (147980, 1000, 1450), 0),
	Insn('CAM_ROTATE', 330, 18, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 16170, 0),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('CHAR_SET_CHCP', Char(258), 31),
			Insn('CHAR_SET_FRAME', Char(258), 0),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('CHAR_SET_CHCP', Char(259), 32),
			Insn('CHAR_SET_FRAME', Char(259), 0),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('CHAR_SET_CHCP', Char(260), 33),
			Insn('CHAR_SET_FRAME', Char(260), 0),
		]),
		(None, []),
	]),
	Insn('CHAR_FLAG1_SET', Char(239), 4),
	Insn('CHAR_FLAG1_SET', Char(339), 2),
	Insn('CHAR_FLAG1_SET', Char(339), 16),
	Insn('CHAR_FLAG1_SET', Char(339), 4),
	Insn('CHAR_SET_CHCP', Char(339), 36),
	Insn('CHAR_SET_FRAME', Char(339), 0),
	Insn('CHAR_SET_POS', Char(257), (148050, 150, 1800), 180),
	Insn('CHAR_SET_POS', Char(339), (147350, 350, 1800), 0),
	Insn('CHAR_SET_POS', Char(239), (146600, 150, 1800), 180),
	Insn('CHAR_SET_CHCP', Char(9), 34),
	Insn('CHAR_SET_FRAME', Char(9), 0),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('CHAR_SET_POS', Char(9), (145000, 150, 790), 90),
	Insn('CHAR_SET_CHCP', Char(10), 35),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('CHAR_SET_POS', Char(10), (145000, 150, -100), 90),
	Insn('OBJ_SET_FRAME', Object(255), 'bg00_y', Insn('0', 1)),
	Insn('SOUND_PLAY', 468, 0, 2, 100),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 3))),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (146980, 1000, 1450), 3000),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('SOUND_PLAY', 2033, 0, 255, 100),
	Insn('SLEEP', 1800),
	Insn('CHAR_SET_FRAME', Char(339), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600675V#1109F#5P喂喂，罗伊德！\n'
		'好漂亮哦～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (40, 43, 100, 3)),
	Insn('CHAR_SET_FRAME', Char(257), 2),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(239), 1),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600676V#0011F#11P声、声音太大了……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(239), 0),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(239), 2),
	Insn('SLEEP', 200),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600677V#0106F#11P对、对不起……\n'
				'这孩子实在是太吵闹了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600678V#0206F#11P……对不起。\n'
				'这孩子实在是太吵闹了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600679V#0306F#11P不好意思啊。\n'
				'这小鬼实在是太吵闹了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_TALK', Char(9), Text(
		'#13600680V#5P呵呵，没关系啊。\n'
		'小孩子就是应该有活力。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'#13600681V#1P呵呵，你们是要去\n'
		'探望什么人吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600682V#0000F#11P不，我们稍微有些事情，\n'
		'要去咨询医院的医生……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(339), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(339), 0),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600683V#1107F#5P快看快看，那边有\n'
		'小小的孤岛哦～！{wait}'
		'{page}'
		'#13600684V#1109F形状真奇怪，好有趣～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('EMOTE', Char(239), 0, 1700, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(239), 0),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(239), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600685V#0012F#12P哎呀哎呀……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600686V#0102F#6P呵呵……\n'
				'她好像很高兴呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600687V#0202F#6P呵……\n'
				'她好像很开心呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600688V#0309F#6P哈哈……\n'
				'她好像很兴奋啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CAM_DISTANCE', 15670, 2000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(257), 3),
	Insn('CHAR_FLAG1_UNSET', Char(257), 4),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('CHAR_FLAG1_UNSET', Char(239), 4),
	Insn('CHAR_SET_CHCP', Char(239), 255),
	Insn('CHAR_SET_FRAME', Char(239), 0),
	Insn('CHAR_FLAG1_UNSET', Char(339), 4),
	Insn('CHAR_FLAG1_UNSET', Char(339), 2),
	Insn('CHAR_FLAG1_UNSET', Char(339), 16),
	Insn('CHAR_SET_CHCP', Char(339), 255),
	Insn('CHAR_SET_FRAME', Char(339), 0),
	Insn('0x49'),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0xD5', 33),
	Insn('0xD5', 34),
	Insn('0xD5', 35),
	Insn('0xD5', 36),
	Insn('FORK_FUNC', Char(21), 0, Function((0, 16))),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('FORK_AWAIT', Char(21), 0),
	Insn('SOUND_STOP', 468),
	Insn('FLAG_SET', Flag(737)),
	Insn('NEW_SCENE', 't1500', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('CHAR_SET_POS', Char(257), (2600, -500, -450), 270),
	Insn('CHAR_SET_POS', Char(258), (2600, -500, 450), 270),
	Insn('CHAR_SET_POS', Char(259), (3700, -500, 450), 270),
	Insn('CHAR_SET_POS', Char(260), (3700, -500, -450), 270),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CAM_OFFSET', (900, 900, 0), 0),
	Insn('CAM_ROTATE', 270, 30, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 17800, 0),
	Insn('0x7D', b'\xff\xd2\xc8\x00\x00\x00\x00\x00'),
	Insn('OBJ_SET_FRAME', Object(255), 'bg00_y', Insn('2', 'stop')),
	Insn('OBJ_SET_FRAME', Object(255), 'effect00_add', Insn('0', 1)),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (400, 900, 0), 2500),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 6))),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 7))),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 8))),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 9))),
	Insn('FORK_AWAIT', Char(257), 3),
	Insn('FORK_AWAIT', Char(258), 3),
	Insn('FORK_AWAIT', Char(259), 3),
	Insn('FORK_AWAIT', Char(260), 3),
	Insn('0x6F', b'y'),
	Insn('SLEEP', 500),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (0, 900, 0), 0),
	Insn('CAM_OFFSET', (0, 900, -2500), 4000),
	Insn('CAM_ROTATE', 320, 26, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 17800, 0),
	Insn('SLEEP', 1500),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 10))),
	Insn('SLEEP', 200),
	Insn('FORK_FUNC', Char(260), 3, Function((0, 11))),
	Insn('SLEEP', 100),
	Insn('FORK_FUNC', Char(258), 3, Function((0, 12))),
	Insn('SLEEP', 150),
	Insn('FORK_FUNC', Char(259), 3, Function((0, 13))),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(257), 3),
	Insn('FORK_QUIT', Char(260), 3),
	Insn('FORK_QUIT', Char(258), 3),
	Insn('FORK_QUIT', Char(259), 3),
	Insn('SLEEP', 2000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (0, 500, 500), 0),
	Insn('CAM_ROTATE', 320, 20, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 17800, 0),
	Insn('CHAR_SET_POS', Char(257), (600, 0, -4800), 0),
	Insn('CHAR_SET_POS', Char(258), (800, 0, 2300), 0),
	Insn('CHAR_SET_POS', Char(259), (0, 0, 3700), 0),
	Insn('CHAR_SET_POS', Char(260), (-800, 0, 2600), 0),
	Insn('CAM_OFFSET', (0, 500, 4500), 6000),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00|\x15\x00\x00\xdc\x05\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#15100334V#0008F#6P花和慰问品\n'
		'都留在座位上……{wait}'
		'{page}'
		'#15100335V#0013F看起来，像是\n'
		'正要去医院呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#15100336V#0106F#6P嗯……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#15100337V#0208F#6P咪西玩偶……\n'
		'大概是送给\n'
		'小患者的慰问品吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#15100338V#0306F#6P嗯……大概吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('CAM_DISTANCE', 17200, 2500),
	Insn('0x6F', b'y'),
	Insn('0x0D'),
	Insn('FLAG_SET', Flag(738)),
	Insn('NEW_SCENE', 'r1530', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('FORK', 254, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xdc\x05\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('SLEEP', 500),
	Insn('CHAR_ROTATE', Char(254), 180, 300),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('FORK', 254, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xdc\x05\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('SLEEP', 500),
	Insn('CHAR_ROTATE', Char(254), 315, 500),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('FORK', 254, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xdc\x05\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('SLEEP', 500),
	Insn('CHAR_ROTATE', Char(254), 315, 300),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('FORK', 254, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xdc\x05\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('SLEEP', 500),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('SLEEP', 500),
	Insn('CHAR_ROTATE', Char(254), 180, 500),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('CHAR_ROTATE', Char(254), 270, 500),
	Insn('FORK', 254, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xf4\x01\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 180, 500),
	Insn('FORK', 254, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x88\x13\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 270, 500),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('SLEEP', 500),
	Insn('CHAR_ROTATE', Char(254), 270, 500),
	Insn('FORK', 254, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xdc\x05\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 180, 500),
	Insn('FORK', 254, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\x98\x08\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 270, 500),
	Insn('FORK', 254, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xd0\x07\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 0, 500),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('CHAR_ROTATE', Char(254), 270, 500),
	Insn('FORK', 254, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xb0\x04\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 0, 500),
	Insn('FORK', 254, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xd0\x07\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 270, 500),
	Insn('FORK', 254, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00 \x03\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('SLEEP', 500),
	Insn('CHAR_ROTATE', Char(254), 270, 500),
	Insn('FORK', 254, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xd0\x07\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('CHAR_ROTATE', Char(254), 0, 500),
	Insn('FORK', 254, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xa0\x0f\x00\x00\xe8\x03\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('EVENT_BEGIN', 0),
	Insn('MENU', 0, -1, -1, 0, Text(
		'【老人】\n'
		'【老婆婆】\n'
		'【黑发女性】\n'
		'【年轻的女性】\n'
		'【贸易商】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('0x60', 0),
			Insn('QUEST', 27, Insn('TASK_SET', 14)),
			Insn('BREAK'),
		],
		1: [
			Insn('0x60', 0),
			Insn('QUEST', 27, Insn('TASK_SET', 15)),
			Insn('BREAK'),
		],
		2: [
			Insn('0x60', 0),
			Insn('QUEST', 27, Insn('TASK_SET', 16)),
			Insn('BREAK'),
		],
		3: [
			Insn('0x60', 0),
			Insn('QUEST', 27, Insn('TASK_SET', 17)),
			Insn('BREAK'),
		],
		4: [
			Insn('0x60', 0),
			Insn('QUEST', 27, Insn('TASK_SET', 18)),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'r0000', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('LOAD_CHCP', 'chr/ch00202', 32),
	Insn('LOAD_CHCP', 'chr/ch00302', 33),
	Insn('LOAD_CHCP', 'apl/ch50119', 34),
	Insn('LOAD_CHCP', 'chr/ch07302', 35),
	Insn('LOAD_CHCP', 'chr/ch24102', 36),
	Insn('LOAD_CHCP', 'chr/ch20802', 37),
	Insn('LOAD_CHCP', 'chr/ch33000', 38),
	Insn('LOAD_CHCP', 'chr/ch24500', 39),
	Insn('LOAD_CHCP', 'chr/ch21202', 40),
	Insn('LOAD_CHCP', 'chr/ch21302', 41),
	Insn('LOAD_CHCP', 'chr/ch21002', 42),
	Insn('LOAD_CHCP', 'chr/ch21402', 43),
	Insn('SOUND_LOAD', 474),
	Insn('CAM_OFFSET', (47090, 1100, -430), 0),
	Insn('CAM_ROTATE', 328, 27, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 23180, 0),
	Insn('CAM_OFFSET', (51930, 1100, 120), 8000),
	Insn('CHAR_SET_CHCP', Char(257), 30),
	Insn('CHAR_SET_FRAME', Char(257), 1),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_SET_CHCP', Char(259), 32),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_SET_CHCP', Char(260), 33),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_SET_CHCP', Char(8), 34),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('CHAR_FLAG1_UNSET', Char(12), 128),
	Insn('CHAR_FLAG2_UNSET', Char(12), 32768),
	Insn('CHAR_SET_CHCP', Char(12), 35),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('CHAR_FLAG1_UNSET', Char(13), 128),
	Insn('CHAR_FLAG2_UNSET', Char(13), 32768),
	Insn('CHAR_SET_CHCP', Char(13), 36),
	Insn('CHAR_SET_FRAME', Char(13), 1),
	Insn('CHAR_FLAG1_UNSET', Char(14), 128),
	Insn('CHAR_FLAG2_UNSET', Char(14), 32768),
	Insn('CHAR_SET_CHCP', Char(14), 37),
	Insn('CHAR_SET_FRAME', Char(14), 0),
	Insn('CHAR_FLAG1_UNSET', Char(15), 128),
	Insn('CHAR_FLAG2_UNSET', Char(15), 32768),
	Insn('CHAR_SET_CHCP', Char(15), 38),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('CHAR_FLAG1_UNSET', Char(16), 128),
	Insn('CHAR_FLAG2_UNSET', Char(16), 32768),
	Insn('CHAR_SET_CHCP', Char(16), 39),
	Insn('CHAR_SET_FRAME', Char(16), 0),
	Insn('CHAR_FLAG1_UNSET', Char(17), 128),
	Insn('CHAR_FLAG2_UNSET', Char(17), 32768),
	Insn('CHAR_SET_CHCP', Char(17), 40),
	Insn('CHAR_SET_FRAME', Char(17), 2),
	Insn('CHAR_FLAG1_UNSET', Char(18), 128),
	Insn('CHAR_FLAG2_UNSET', Char(18), 32768),
	Insn('CHAR_SET_CHCP', Char(18), 41),
	Insn('CHAR_SET_FRAME', Char(18), 1),
	Insn('CHAR_FLAG1_UNSET', Char(19), 128),
	Insn('CHAR_FLAG2_UNSET', Char(19), 32768),
	Insn('CHAR_SET_CHCP', Char(19), 42),
	Insn('CHAR_SET_FRAME', Char(19), 0),
	Insn('CHAR_FLAG1_UNSET', Char(20), 128),
	Insn('CHAR_FLAG2_UNSET', Char(20), 32768),
	Insn('CHAR_SET_CHCP', Char(20), 43),
	Insn('CHAR_SET_FRAME', Char(20), 2),
	Insn('CHAR_SET_POS', Char(257), (52250, 150, 1700), 180),
	Insn('CHAR_SET_POS', Char(258), (55000, 150, 200), 270),
	Insn('CHAR_SET_POS', Char(259), (55000, 150, 1450), 270),
	Insn('CHAR_SET_POS', Char(260), (53300, 150, 1700), 180),
	Insn('CHAR_SET_POS', Char(8), (43870, -200, 1800), 270),
	Insn('CHAR_SET_POS', Char(12), (48000, 150, -2000), 270),
	Insn('CHAR_SET_POS', Char(13), (44000, 150, -2000), 270),
	Insn('CHAR_SET_POS', Char(14), (46000, 150, -2000), 270),
	Insn('CHAR_SET_POS', Char(15), (50270, -250, -2029), 225),
	Insn('CHAR_SET_POS', Char(16), (49540, -250, 1520), 270),
	Insn('CHAR_SET_POS', Char(17), (48000, 150, 600), 270),
	Insn('CHAR_SET_POS', Char(18), (48000, 150, 1600), 270),
	Insn('CHAR_SET_POS', Char(19), (46000, 150, 600), 270),
	Insn('CHAR_SET_POS', Char(20), (46000, 150, 1600), 270),
	Insn('OBJ_SET_FRAME', Object(255), 'bg00_y', Insn('0', 1)),
	Insn('BGM_PLAY', b'\x04\x02\x00'),
	Insn('SOUND_PLAY', 474, 0, 2, 0),
	Insn('FORK_FUNC', Char(21), 0, Function((0, 17))),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'\x01'),
	Insn('FORK_QUIT', Char(21), 0),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0001F（首先……\n'
		'\u3000来整理一下有关假货贩子\n'
		'\u3000的情报吧。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0203F（那些假货贩子们是从\n'
		'\u3000车站、机场和唐古拉姆门\n'
		'\u3000这几条路线分头而来的……）{wait}'
		'{page}'
		'#0200F（根据从警察局总部得到的情报，\n'
		'\u3000确实就是这样的。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0000F（嗯，正是如此。）{wait}'
		'{page}'
		'#0003F（然后，既然情报准确，\n'
		'\u3000嫌疑人应该就在\n'
		'\u3000这辆巴士的乘客中。）{wait}'
		'{page}'
		'（还有……\n'
		'\u3000根据这些情报来分析，\n'
		'\u3000就有一个事实浮出水面了。）{wait}'
		'{page}'
		'#0001F（这辆巴士中的假货贩子，\n'
		'\u3000恐怕是……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('MENU', 0, -1, -1, 0, Text(
		'【单独行动的】\n'
		'【两人一组行动的】\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
		0: [
			Insn('0x60', 0),
			Insn('QUEST_BONUS_DP', 27, 1),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0001F（……是单独行动的。）{wait}'
				'{page}'
				'#0003F（而且，这个人在假货商组织中，\n'
				'\u3000应该也是头目般的存在。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#11P#0305F（喂喂，真的假的……\n'
				'\u3000头目级的人物，难道会\n'
				'\u3000一个人单独行动吗？）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#12P#0105F（这种情况倒也并非没有可能……\n'
				'\u3000不过，根据在哪里呢？）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0004F（很简单。）{wait}'
				'{page}'
				'（那些家伙为了来这里做生意，\n'
				'\u3000就必须要偷偷把假货\n'
				'\u3000运进克洛斯贝尔。）{wait}'
				'{page}'
				'#0000F（乘坐巴士来通过唐古拉姆门，\n'
				'\u3000明显不是适当的运货通道。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#12P#0203F（确实……如你所说呢。）{wait}'
				'{page}'
				'#0200F（如果我是假货贩子，\n'
				'\u3000恐怕会把运货任务交给从车站和机场\n'
				'\u3000潜入克洛斯贝尔的那些同伴。）{wait}'
				'{page}'
				'（和国境门不同，车站和机场\n'
				'\u3000并不会对共和国和帝国方面的\n'
				'\u3000入境人员进行太过严密的检查。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#11P#0303F（另外，像运货这种危险的任务，\n'
				'\u3000一般都会交给下面的人去做，这也是惯例。）{wait}'
				'{page}'
				'（利用排除法来思考……\n'
				'\u3000车站或机场这两条线路\n'
				'\u3000是用来运送货物的……）{wait}'
				'{page}'
				'#0301F（而头目则只携带少量行李，\n'
				'\u3000完全不会被人怀疑，就这么毫无危险，\n'
				'\u3000悠哉悠哉地前往克洛斯贝尔吗。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0000F（就是这么一回事。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#12P#0103F（虽然只是根据现场情况而做出的推测……\n'
				'\u3000但确实很有说服力呢。）{wait}'
				'{page}'
				'#0101F（这样一来，两人出行的\n'
				'\u3000兄妹游客，还有那位带着小孩的旅行者，\n'
				'\u3000就可以从嫌疑犯的名单中排除了。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0001F（……嗯，然后……）{wait}'
				'{page}'
				'#0003F（刚才，在和乘客们对话的时候……\n'
				'\u3000有一个人说的话让我十分在意。）{wait}'
				'{page}'
				'（如果所料不差，\n'
				'\u3000那个人恐怕就是假货贩子的头目了。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		1: [
			Insn('0x60', 0),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0003F（……是两人一组行动的。）{wait}'
				'{page}'
				'#0001F（在假货商组织中，\n'
				'\u3000多半也有专门负责运货的成员。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#11P#0305F（……运货的二人组！？）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0001F（那些家伙为了来这里做生意，\n'
				'\u3000就必须要偷偷把假货\n'
				'\u3000运进克洛斯贝尔。）{wait}'
				'{page}'
				'#0003F（如果一个人单独带着货物入境，\n'
				'\u3000肯定会非常显眼，未免太过艰难了。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#11P#0305F（也就是说……\n'
				'\u3000嫌疑人是那对兄妹旅行者，\n'
				'\u3000或是那位带着小孩的乘客吗？）{wait}'
				'{page}'
				'#0306F（这个……再怎么说，\n'
				'\u3000未免也太过出人意表了吧。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#12P#0200F（……真的是那样的吗？）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0005F（……哎？）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#12P#0203F（如果我是假货贩子，\n'
				'\u3000恐怕会把运货任务交给从车站和机场\n'
				'\u3000潜入克洛斯贝尔的那些同伴。）{wait}'
				'{page}'
				'#0200F（和国境门不同，车站和机场\n'
				'\u3000并不会对共和国和帝国方面的\n'
				'\u3000入境人员进行太过严密的检查。）{wait}'
				'{page}'
				'（所以，唐古拉姆门\n'
				'\u3000实在不是一条适合\n'
				'\u3000运送货物的路线。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#12P#0103F（确实……）{wait}'
				'{page}'
				'#0101F（这样看来，乘坐这辆巴士\n'
				'\u3000的假货商人，恐怕……\n'
				'\u3000是单独行动的可能性会比较高呢。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0005F单独行动……！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#12P#0101F（嗯，而且……\n'
				'\u3000这个人，在假货商组织中，\n'
				'\u3000应该也是个首领级别的角色。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#11P#0305F（……是吗……）{wait}'
				'{page}'
				'#0303F（像运货这种危险的任务，\n'
				'\u3000一般都会交给下面的人去做，这也是惯例。）{wait}'
				'{page}'
				'（利用排除法来思考……\n'
				'\u3000车站或机场这两条线路\n'
				'\u3000是用来运送货物的……）{wait}'
				'{page}'
				'#0301F（而头目则只携带少量行李，\n'
				'\u3000完全不会被人怀疑，就这么毫无危险，\n'
				'\u3000悠哉悠哉地前往克洛斯贝尔吗。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0005F（原来是这么回事吗……）{wait}'
				'{page}'
				'#0006F（多谢了，各位。\n'
				'\u3000看来是我考虑得不太周全。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#12P#0100F（呵呵，没关系啦。\n'
				'\u3000如果总是将问题交给你一个人来思考，\n'
				'\u3000我们也会无法成长的。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#12P#0200F（也不能总是让前辈一个人出风头啊。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#11P#0309F（哈哈，说的对呢。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0001F（不过，这样一来……\n'
				'\u3000我也想到了一名\n'
				'\u3000可疑的人物呢。）{wait}'
				'{page}'
				'#0003F（刚才，在和乘客们对话的时候……\n'
				'\u3000有一个人说的话让我十分在意。）{wait}'
				'{page}'
				'#0001F（如果所料不差，\n'
				'\u3000那个人恐怕就是假货贩子的头目了。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('BREAK'),
		],
		None: [],
	}),
	Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('TEXT_TALK', Char(260), Text(
		'#11P#0301F（就是你刚才说的那个家伙吗……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0203F（……嫌疑人还剩下五名。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (45920, 1100, -1670), 0),
	Insn('CAM_ROTATE', 358, 27, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 18520, 0),
	Insn('0x0D'),
	Insn('TEXT_SET_POS', 350, 0, -1, -1),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#0200F （①声称自己是要来克洛斯贝尔钓鱼的\n'
		'\u3000那个倔强乖僻的老人。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (43880, 1100, -1880), 0),
	Insn('CAM_ROTATE', 358, 27, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 18520, 0),
	Insn('0x0D'),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#0200F（②说自己和孙子已经三年未见的\n'
		'\u3000那位温和的老婆婆。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (48010, 1100, -1960), 0),
	Insn('CAM_ROTATE', 52, 27, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 17640, 0),
	Insn('0x0D'),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#0200F（③让人感觉到明显不是等闲之辈的\n'
		'\u3000那位黑发女性。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (49460, 1100, 1460), 0),
	Insn('CAM_ROTATE', 335, 27, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 18520, 0),
	Insn('0x0D'),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#0200F（④对那位黑发女性抱有很深怀疑的\n'
		'\u3000那个年轻女性。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (50240, 1100, -1870), 0),
	Insn('CAM_ROTATE', 47, 27, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 19450, 0),
	Insn('0x0D'),
	Insn('TEXT_MESSAGE', Char(259), Text(
		'#0200F（⑤还有，来往于克洛斯贝尔和共和国的\n'
		'\u3000那名贸易商人……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (51930, 1100, 120), 0),
	Insn('CAM_ROTATE', 328, 27, 0, 0),
	Insn('0x6E', 350, 0),
	Insn('CAM_DISTANCE', 23180, 0),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0105F（不过，真的就在这些人当中……？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0003F（……嗯，不会有错。）{wait}'
		'{page}'
		'#0001F（在这些人之中，\n'
		'\u3000假货商人的头目正是……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 255), Insn('NE'), Insn('END')], [
		Insn('MENU', 0, -1, -1, 0, Text(
			'【老人】\n'
			'【老婆婆】\n'
			'【黑发女性】\n'
			'【年轻的女性】\n'
			'【贸易商】\n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
			0: [
				Insn('0x60', 0),
				Insn('TEXT_TALK', Char(257), Text(
					'#5P#0001F（……是那位老人。）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('QUEST', 27, Insn('TASK_SET', 14)),
				Insn('BREAK'),
			],
			1: [
				Insn('0x60', 0),
				Insn('TEXT_TALK', Char(257), Text(
					'#5P#0001F（是那位老婆婆。）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('QUEST', 27, Insn('TASK_SET', 15)),
				Insn('BREAK'),
			],
			2: [
				Insn('0x60', 0),
				Insn('TEXT_TALK', Char(257), Text(
					'#5P#0001F（是那个黑发女性。）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('QUEST', 27, Insn('TASK_SET', 16)),
				Insn('BREAK'),
			],
			3: [
				Insn('0x60', 0),
				Insn('TEXT_TALK', Char(257), Text(
					'#5P#0001F（是那个年轻的女性。）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('QUEST', 27, Insn('TASK_SET', 17)),
				Insn('BREAK'),
			],
			4: [
				Insn('0x60', 0),
				Insn('TEXT_TALK', Char(257), Text(
					'#5P#0001F（是那个贸易商人。）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('QUEST', 27, Insn('TASK_SET', 18)),
				Insn('BREAK'),
			],
			None: [],
		}),
		Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
		Insn('TEXT_TALK', Char(260), Text(
			'#11P#0301F（……真的没错吗？）{wait}'
		)),
		Insn('TEXT_WAIT'),
		Insn('MENU', 0, -1, -1, 0, Text(
			'【没错】\n'
			'【重新思考】\n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
			0: [
				Insn('0x60', 0),
				Insn('IF', [
					(Expr([Insn('EXEC', Insn('QUEST_GET', 27, Insn('TASK_GET', 15))), Insn('END')]), [
						Insn('QUEST_BONUS_DP', 27, 2),
					]),
					(None, []),
				]),
				Insn('TEXT_TALK', Char(257), Text(
					'#5P#0001F（……嗯。\n'
					'\u3000假货商人的头目，除了那个人\n'
					'\u3000之外，再没有别的可能了。）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('TEXT_TALK', Char(258), Text(
					'#12P#0105F（是……这样啊。）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('SOUND_PLAY', 801, 0, 0, 100),
				Insn('SLEEP', 500),
				Insn('TEXT_SET_POS', -1, -1, -1, -1),
				Insn('TEXT_SET_NAME', Translate('广播通知')),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}──本巴士即将达到\n'
					'克洛斯贝尔市东出口。{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('TEXT_MESSAGE', Char(255), Text(
					'{color 5}在下车时，\n'
					'请您注意不要遗忘随身物品。{color 0}{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('TEXT_RESET', b'\x00'),
				Insn('0x5A'),
				Insn('TEXT_SET_POS', -1, 280, 60, 3),
				Insn('TEXT_TALK', Char(259), Text(
					'#12P#0200F（好像马上就要到站了呢。）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('TEXT_TALK', Char(258), Text(
					'#12P#0101F（……接下来就是重头戏了。）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('TEXT_TALK', Char(257), Text(
					'#5P#0001F（到站之后，一定要\n'
					'\u3000盯紧嫌疑人。）{wait}'
					'{page}'
					'（各位，请一定要集中注意力啊。）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('TEXT_TALK', Char(260), Text(
					'#11P#0304F（不用你说我们也知道啦。）{wait}'
					'{page}'
					'#0300F（罗伊德，首先由你\n'
					'\u3000去将嫌疑人的伪装\n'
					'\u3000揭开吧。）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('TEXT_TALK', Char(257), Text(
					'#5P#0001F（嗯，交给我吧……！）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('SLEEP', 500),
				Insn('CROSSFADE', 500),
				Insn('CAM_OFFSET', (47810, 1100, -1860), 0),
				Insn('CAM_ROTATE', 44, 27, 0, 0),
				Insn('0x6E', 350, 0),
				Insn('CAM_DISTANCE', 18710, 0),
				Insn('0x0D'),
				Insn('CAM_DISTANCE', 17710, 2000),
				Insn('0x6F', b'\x10'),
				Insn('TEXT_TALK', Char(12), Text(
					'#11P#3403F………………………………{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 255), Insn('SET'), Insn('END')])),
				Insn('BREAK'),
			],
			1: [
				Insn('0x60', 0),
				Insn('TEXT_TALK', Char(257), Text(
					'#5P#0003F（……这么一说，\n'
					'\u3000稍微有点没自信呢。）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('TEXT_TALK', Char(260), Text(
					'#11P#0306F（呃……你在干什么嘛！）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('TEXT_TALK', Char(258), Text(
					'#12P#0106F（唉……打起精神来啊。）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('TEXT_TALK', Char(257), Text(
					'#5P#0011F（抱、抱歉，\n'
					'\u3000让我再重新考虑一下。）{wait}'
					'{page}'
					'#0003F（那个时候……\n'
					'\u3000有个人明显的说漏了嘴，\n'
					'\u3000讲了些很奇怪的话。）{wait}'
					'{page}'
					'（把某些根本就不可能发生的事情，\n'
					'\u3000说得理所当然……）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('TEXT_TALK', Char(260), Text(
					'#11P#0300F（马上就要到克洛斯贝尔市了。\n'
					'\u3000赶快做出判断吧。）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('TEXT_TALK', Char(257), Text(
					'#5P#0001F（在这些人当中，\n'
					'\u3000假货商人的头目就是……）{wait}'
				)),
				Insn('TEXT_WAIT'),
				Insn('QUEST', 27, Insn('TASK_UNSET', 14)),
				Insn('QUEST', 27, Insn('TASK_UNSET', 15)),
				Insn('QUEST', 27, Insn('TASK_UNSET', 16)),
				Insn('QUEST', 27, Insn('TASK_UNSET', 17)),
				Insn('QUEST', 27, Insn('TASK_UNSET', 18)),
				Insn('BREAK'),
			],
			None: [],
		}),
	]),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_FUNC', Char(21), 0, Function((0, 18))),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 111), Insn('SET'), Insn('END')])),
	Insn('FORK_AWAIT', Char(21), 0),
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 128),
	Insn('CHAR_FLAG2_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 128),
	Insn('CHAR_FLAG2_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 128),
	Insn('CHAR_FLAG2_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(15), 128),
	Insn('CHAR_FLAG2_SET', Char(15), 32768),
	Insn('CHAR_FLAG1_SET', Char(16), 128),
	Insn('CHAR_FLAG2_SET', Char(16), 32768),
	Insn('CHAR_FLAG1_SET', Char(17), 128),
	Insn('CHAR_FLAG2_SET', Char(17), 32768),
	Insn('CHAR_FLAG1_SET', Char(18), 128),
	Insn('CHAR_FLAG2_SET', Char(18), 32768),
	Insn('CHAR_FLAG1_SET', Char(19), 128),
	Insn('CHAR_FLAG2_SET', Char(19), 32768),
	Insn('CHAR_FLAG1_SET', Char(20), 128),
	Insn('CHAR_FLAG2_SET', Char(20), 32768),
	Insn('0x49'),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0xD5', 33),
	Insn('0xD5', 34),
	Insn('0xD5', 35),
	Insn('0xD5', 36),
	Insn('0xD5', 37),
	Insn('0xD5', 38),
	Insn('0xD5', 39),
	Insn('0xD5', 40),
	Insn('0xD5', 41),
	Insn('0xD5', 42),
	Insn('0xD5', 43),
	Insn('SOUND_STOP', 474),
	Insn('FLAG_SET', Flag(736)),
	Insn('NEW_SCENE', 'r0000', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('SOUND_LOOP', 468, 90),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 468, 80),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 468, 70),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 468, 60),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 468, 50),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 468, 40),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 468, 30),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 468, 20),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 468, 10),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 468, 0),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('SOUND_LOOP', 474, 10),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 20),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 30),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 40),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 50),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 60),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 70),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 80),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 90),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 100),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('SOUND_LOOP', 474, 90),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 80),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 70),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 60),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 50),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 40),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 30),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 20),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 10),
	Insn('SLEEP', 80),
	Insn('SOUND_LOOP', 474, 0),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('QUEST', 56, Insn('TASK_SET', 14)),
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch00002', 30),
	Insn('LOAD_CHCP', 'chr/ch00102', 31),
	Insn('LOAD_CHCP', 'chr/ch00202', 32),
	Insn('LOAD_CHCP', 'chr/ch00302', 33),
	Insn('LOAD_CHCP', 'apl/ch50119', 34),
	Insn('LOAD_CHCP', 'chr/ch20402', 35),
	Insn('LOAD_CHCP', 'chr/ch20302', 36),
	Insn('LOAD_CHCP', 'chr/ch22302', 37),
	Insn('SOUND_LOAD', 468),
	Insn('CAM_OFFSET', (99540, 1000, 6650), 0),
	Insn('CAM_ROTATE', 315, 25, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 20000, 0),
	Insn('CHAR_SET_CHCP', Char(258), 31),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_SET_CHCP', Char(259), 32),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('CHAR_SET_CHCP', Char(260), 33),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('CHAR_FLAG1_SET', Char(257), 4),
	Insn('CHAR_FLAG1_SET', Char(258), 4),
	Insn('CHAR_FLAG1_SET', Char(259), 4),
	Insn('CHAR_FLAG1_SET', Char(260), 4),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG2_UNSET', Char(8), 32768),
	Insn('CHAR_SET_CHCP', Char(8), 34),
	Insn('CHAR_SET_FRAME', Char(8), 0),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG2_UNSET', Char(9), 32768),
	Insn('CHAR_SET_CHCP', Char(9), 35),
	Insn('CHAR_SET_FRAME', Char(9), 0),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('CHAR_SET_CHCP', Char(10), 36),
	Insn('CHAR_SET_FRAME', Char(10), 0),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG2_UNSET', Char(11), 32768),
	Insn('CHAR_SET_CHCP', Char(11), 37),
	Insn('CHAR_SET_FRAME', Char(11), 0),
	Insn('CHAR_SET_POS', Char(257), (99340, 0, -2300), 180),
	Insn('CHAR_SET_POS', Char(258), (99470, 150, -5170), 0),
	Insn('CHAR_SET_POS', Char(259), (100670, 150, -5170), 0),
	Insn('CHAR_SET_POS', Char(260), (98270, 150, -3720), 90),
	Insn('CHAR_SET_POS', Char(8), (101780, -200, 6150), 0),
	Insn('CHAR_SET_POS', Char(9), (101780, 150, 1960), 0),
	Insn('CHAR_SET_POS', Char(10), (100890, 150, 1960), 0),
	Insn('CHAR_SET_POS', Char(11), (98270, 150, 5800), 0),
	Insn('SOUND_PLAY', 468, 0, 2, 100),
	Insn('FORK_FUNC', Char(257), 3, Function((0, 3))),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (98750, 1000, -2330), 10000),
	Insn('CAM_DISTANCE', 14000, 10000),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('BGM_PLAY', b'\x04\x02\x00'),
	Insn('TEXT_TALK', Char(260), Text(
		'#1P#0303F等回到克洛斯贝尔之后，\n'
		'就要正式开始找\n'
		'下落不明的主任了……{wait}'
		'{page}'
		'但在毫无头绪的情况下，\n'
		'就克洛斯贝尔来说，\n'
		'范围实在有点大。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(260), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#1P#0300F该怎么办，罗伊德？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(260), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#2P#0003F但也只能一个一个问了吧。{wait}'
		'{page}'
		'#0000F人多就表示\n'
		'很有可能会有目击者。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#1P#0100F这是警察的基本功吧。\n'
		'搜查就要抱着\n'
		'磨平鞋底的决心……对吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('CHAR_WATCH', Char(257), Char(258), 500),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(260), 2),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#1P#0306F真是的，只希望在\n'
		'鞋底不见之前就能找到人。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#2P#0200F那要从哪边开始问呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(259), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#2P#0000F先从巴士站周边开始吧。\n'
		'如果是附近的站前大道，\n'
		'应该会有目击证词才对。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 100),
	Insn('CHAR_SET_FRAME', Char(260), 0),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#1P#0300F明白。\n'
		'就打起精神开始查吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 4000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(257), 3),
	Insn('FORK_FUNC', Char(21), 0, Function((0, 16))),
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
	Insn('CHAR_FLAG1_SET', Char(8), 128),
	Insn('CHAR_FLAG2_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('CHAR_FLAG2_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(11), 128),
	Insn('CHAR_FLAG2_SET', Char(11), 32768),
	Insn('0x49'),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0xD5', 32),
	Insn('0xD5', 33),
	Insn('0xD5', 34),
	Insn('0xD5', 35),
	Insn('0xD5', 36),
	Insn('0xD5', 37),
	Insn('FORK_AWAIT', Char(21), 0),
	Insn('BGM_WAIT'),
	Insn('SOUND_STOP', 468),
	Insn('NEW_SCENE', 'r1500', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]
