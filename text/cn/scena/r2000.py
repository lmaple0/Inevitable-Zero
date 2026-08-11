# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'r2000',
	'name2': 'r2000',
	'location': 98,
	'bgm': 202,
	'flags': 0,
	'includes': [
		'r2000',
		'r0000_1',
		None,
		None,
		None,
		None,
	],
	'name3': 'r2000',
	'labels': [
		{
			'pos': (-1.7999999523162842, 0.0, -15.550000190734863),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('克洛斯贝尔市方向'),
		},
		{
			'pos': (45.0, 0.0, 37.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('克洛斯贝尔大教堂方向'),
		},
		{
			'pos': (-23.0, 0.0, 75.30000305175781),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('矿山镇玛因兹方向'),
		},
		{
			'pos': (11.25, 0.0, 16.450000762939453),
			'unk': b'\x00\x00U\x00',
			'name': Translate(''),
		},
		{
			'pos': (-1.0, 0.0, 19.5),
			'unk': b'\x00\x00V\x00',
			'name': Translate(''),
		},
	],
	'chcp': [],
	'npcs': [
		{
			'name': Translate('哈罗德车'),
			'pos': (8430, 0, 33990),
			'angle': 225,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('巴士'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x00\x00\x00\x00\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('车'),
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
	'triggers': [
		{
			'pos': (0.0, 7.0, -1.0),
			'range': 144.0,
			'transform': [
				0.125,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.3333333432674408,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000001788139343,
				0.0,
				-0.0,
				-2.3333334922790527,
				0.20000001788139343,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 10)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (11200, 0, 16200),
			'range': 1500,
			'bubble_pos': (11200, 1500, 16200),
			'_1': b'|\x00\x00',
			'function': Function((0, 8)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-700, 0, 19910),
			'range': 1800,
			'bubble_pos': (-700, 2000, 19910),
			'_1': b'|\x00\x00',
			'function': Function((0, 9)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-16960, -2000, 50350),
			'range': 1200,
			'bubble_pos': (-16960, -2000, 50350),
			'_1': b'|\x00\x00',
			'function': Function((0, 2)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (4200, 0, 36290),
			'range': 2500,
			'bubble_pos': (4200, 1700, 36290),
			'_1': b'|\x00\x00',
			'function': Function((0, 16)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\xc4\xff\xff\xff$\x04\x00\x00\x92\x0e\x00\x00\x00\x00\x00\x00\x01\x00b\x00', Function((0, 0)), Function((0, 1))),
	'code': [None]*18,
	'anim': [],
}

data['code'][0] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1106)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(1106)),
			Insn('FLAG_SET', Flag(1107)),
		]),
		(None, []),
	]),
	Insn('0xD0', 7, Expr([Insn('CONST', 14), Insn('SET'), Insn('END')])),
	Insn('FLAG_SET', Flag(1998)),
	Insn('FLAG_SET', Flag(2014)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 13))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1008)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(1008)),
			Insn('EVENT', Function((0, 5))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1009)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(1009)),
			Insn('0xD0', 1, Expr([Insn('CONST', 5), Insn('SET'), Insn('END')])),
			Insn('EVENT', Function((0, 7))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 0), Insn('EQ'), Insn('ATTR', 0), Insn('CONST', 100), Insn('EQ'), Insn('OR'), Insn('ATTR', 0), Insn('CONST', 103), Insn('EQ'), Insn('OR'), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(976)),
			Insn('FLAG_UNSET', Flag(977)),
			Insn('FLAG_UNSET', Flag(978)),
			Insn('FLAG_UNSET', Flag(979)),
			Insn('FLAG_UNSET', Flag(980)),
			Insn('FLAG_UNSET', Flag(981)),
			Insn('FLAG_UNSET', Flag(982)),
			Insn('FLAG_UNSET', Flag(983)),
			Insn('FLAG_UNSET', Flag(984)),
			Insn('FLAG_UNSET', Flag(985)),
			Insn('FLAG_UNSET', Flag(986)),
			Insn('FLAG_UNSET', Flag(987)),
			Insn('FLAG_UNSET', Flag(988)),
			Insn('FLAG_UNSET', Flag(989)),
			Insn('FLAG_UNSET', Flag(990)),
			Insn('FLAG_UNSET', Flag(991)),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(976)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(977)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(978)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(979)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(980)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(981)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(982)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(983)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(984)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(985)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(986)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(987)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 2), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(988)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 10), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(989)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 20), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(990)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('RAND'), Insn('CONST', 100), Insn('MOD'), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(991)),
				]),
				(None, []),
			]),
			Insn('FLAG_UNSET', Flag(992)),
			Insn('FLAG_UNSET', Flag(993)),
			Insn('FLAG_UNSET', Flag(994)),
			Insn('FLAG_UNSET', Flag(995)),
			Insn('FLAG_UNSET', Flag(996)),
			Insn('FLAG_UNSET', Flag(997)),
			Insn('FLAG_UNSET', Flag(998)),
			Insn('FLAG_UNSET', Flag(999)),
			Insn('EXPR_VAR', 2, Expr([Insn('RAND'), Insn('CONST', 8), Insn('MOD'), Insn('SET'), Insn('END')])),
			Insn('IF', [
				(Expr([Insn('VAR', 2), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(992)),
				]),
				(Expr([Insn('VAR', 2), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(993)),
				]),
				(Expr([Insn('VAR', 2), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(994)),
				]),
				(Expr([Insn('VAR', 2), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(995)),
				]),
				(Expr([Insn('VAR', 2), Insn('CONST', 4), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(996)),
				]),
				(Expr([Insn('VAR', 2), Insn('CONST', 5), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(997)),
				]),
				(Expr([Insn('VAR', 2), Insn('CONST', 6), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(998)),
				]),
				(Expr([Insn('VAR', 2), Insn('CONST', 7), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(999)),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][1] = [
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(801)), Insn('FLAG', Flag(802)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x00\x80\x00'),
		]),
		(None, []),
	]),
	Insn('OBJ_FLAG_SET', Object(1), 4),
	Insn('0x65', 1, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1536)), Insn('FLAG', Flag(1542)), Insn('NOT'), Insn('BOOL_AND'), Insn('0x23', 1), Insn('CONST', 5), Insn('EQ'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x66', 1, 1),
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
			Insn('CHAR_FLAG1_SET', Char(10), 32768),
			Insn('OBJ_FLAG_UNSET', Object(1), 4),
			Insn('0x78', b'\x01', Char(10)),
			Insn('OBJ_FLAG_SET', Object(1), 4096),
			Insn('OBJ_SET_FRAME', Object(1), 'light', Insn('0', 1)),
			Insn('CHAR_SET_POS', Char(10), (-1120, 0, 19360), 315),
			Insn('0xD3', Char(10), 0, 180000, 0, 0),
			Insn('0x74', Object(1), 7680),
			Insn('0x70', Object(1), b'\x00\x00'),
		]),
		(None, [
			Insn('0x16', Insn('3', b'\x04\x01\x00')),
		]),
	]),
	Insn('0x78', b'\x02', Char(8)),
	Insn('OBJ_FLAG_SET', Object(2), 4),
	Insn('OBJ_SET_FRAME', Object(2), 'light', Insn('0', 1)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(2), 4),
			Insn('0xD3', Char(8), 0, 225000, 0, 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1024)), Insn('FLAG', Flag(1280)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1183)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 15))),
		]),
		(None, []),
	]),
	Insn('CHAR_FLAG1_SET', Char(9), 128),
	Insn('OBJ_FLAG_SET', Object(0), 4),
	Insn('IF', [
		(Expr([Insn('ATTR', 4), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
			Insn('EXIT_SET_ENABLED', 0, 0),
			Insn('EXIT_SET_ENABLED', 3, 1),
		]),
		(None, [
			Insn('EXIT_SET_ENABLED', 0, 1),
			Insn('EXIT_SET_ENABLED', 3, 0),
		]),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
			Insn('0x11', b'\xdc\xb4\xa0', 30, 100, 0),
			Insn('OBJ_SET_FRAME', Object(255), 'model06_shade', Insn('0', 1)),
		]),
		(None, []),
	]),
	Insn('0x65', 2, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(976)), Insn('END')]), [
			Insn('EFF_LOAD', ResId(9), 'event\\eva00_00.eff'),
			Insn('EFF_PLAY', (ResId(9), 9), Char(255), 0, -16960, -1, -2000, -1, -15186, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
			Insn('0x66', 2, 1),
		]),
		(None, []),
	]),
	Insn('0x1B', 2, Function((255, 255)), 255),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('0x1B', 2, Function((0, 17)), 0),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 2, Function((0, 17)), 0),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('TEXT_START', Char(255)),
	Insn('CALL', Function((1, 0))),
	Insn('FLAG_UNSET', Flag(976)),
	Insn('0x65', 2, 1),
	Insn('EFF_STOP', (ResId(9), 2)),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('EVENT_BEGIN', 1),
	Insn('0x09', 134217728),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}有一个巴士车站。\n'
		'要乘坐巴士吗？{wait}'
	)),
	Insn('MENU', 0, -1, -1, 1, Text(
		'矿山镇玛因兹\n'
		'停靠站（人偶工房附近）\n'
		'放弃\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('CALL', Function((0, 4))),
			Insn('0x0A', 134217728),
			Insn('NEW_SCENE', 't0500', b'\x00\x00\x00\x07'),
		]),
		(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
			Insn('CALL', Function((0, 4))),
			Insn('0x0A', 134217728),
			Insn('NEW_SCENE', 'r2030', b'\x00\x00\x00\x07'),
		]),
		(None, []),
	]),
	Insn('0x0A', 134217728),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (10010, 600, 21560), 0),
	Insn('CAM_ROTATE', 45, 26, 0, 0),
	Insn('0x6E', 630, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('0xE0', b'\x01'),
	Insn('CHAR_SET_POS', Char(0), (10190, 0, 16230), 0),
	Insn('CHAR_SET_POS', Char(1), (9210, 0, 16200), 0),
	Insn('CHAR_SET_POS', Char(2), (8170, 0, 16290), 0),
	Insn('CHAR_SET_POS', Char(3), (7240, 0, 16350), 0),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('OBJ_FLAG_UNSET', Object(0), 4),
	Insn('OBJ_FLAG_UNSET', Object(0), 2),
	Insn('0x78', b'\x00', Char(9)),
	Insn('OBJ_SET_FRAME', Object(0), 'light', Insn('0', 1)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(9), (-40, 0, 30670), 105),
	Insn('0xD3', Char(9), 0, 135000, 0, 0),
	Insn('OBJ_FLAG_SET', Object(0), 4096),
	Insn('0x74', Object(0), 7680),
	Insn('0x71', Object(0), b'y\x00', 180, 32),
	Insn('FORK', 9, 1, [
		Insn('0x9E', Char(254), 12660, 33440, -60000, 3000, b'\x01\x00'),
	]),
	Insn('SOUND_PLAY', 466, 0, 0, 100),
	Insn('SOUND_PLAY', 467, 0, 0, 100),
	Insn('FORK_AWAIT', Char(9), 1),
	Insn('0x71', Object(0), b'[\x00', 120, 0),
	Insn('0x79', b'\x00\x00'),
	Insn('SLEEP', 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FLAG_SET', Flag(1008)),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('EVENT_BEGIN', 1),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('CHAR_SET_POS', Char(0), (10030, 0, 16580), 0),
	Insn('CHAR_SET_POS', Char(1), (10030, 0, 16580), 0),
	Insn('CHAR_SET_POS', Char(2), (10030, 0, 16580), 0),
	Insn('CHAR_SET_POS', Char(3), (10030, 0, 16580), 0),
	Insn('CAM_OFFSET', (10030, 600, 16580), 0),
	Insn('CAM_ROTATE', 45, 30, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 20000, 0),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('EVENT_BEGIN', 1),
	Insn('0x09', 134217728),
	Insn('SOUND_PLAY', 1499, 0, 255, 100),
	Insn('SLEEP', 500),
	Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
	Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('EQ'), Insn('END')], [
		Insn('MENU', 0, 32, 26, 1, Text(
			'使用警备队车辆进行移动\n'
			'在此处休息\n'
			'放弃\n'
		)),
		Insn('MENU_WAIT', 0),
		Insn('IF', [
			(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
				Insn('SOUND_PLAY', 1500, 0, 255, 100),
				Insn('MENU_CUSTOM', Insn('INIT', ResId(1))),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄中央广场'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 0)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄中央广场'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄东出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 1)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄东出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄西出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 2)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄西出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 4), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄南出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 3)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄南出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 5), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄北出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 4)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄北出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 6), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★唐古拉姆门'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 5)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000唐古拉姆门'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 7), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★贝尔加德门'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 6)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000贝尔加德门'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 8), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★乌尔斯拉医科大学'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 7)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000乌尔斯拉医科大学'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 9), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★阿尔摩利卡村'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 8)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000阿尔摩利卡村'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 10), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★玛因兹矿山镇'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 9)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000玛因兹矿山镇'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 11), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★玛因兹山道丄隧道内'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 10)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000玛因兹山道丄隧道内'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 3), Insn('CONST', 12), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★星见之塔'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 11)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000星见之塔'))),
					]),
				]),
				Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000放弃'))),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
				Insn('MENU_CUSTOM', Insn('FINISH', ResId(1), 1048816, 1)),
				Insn('MENU_WAIT', 0),
				Insn('0x60', 1),
				Insn('TEXT_RESET', b'\x00'),
				Insn('0x5A'),
				Insn('IF', [
					(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('GE'), Insn('VAR', 0), Insn('CONST', 12), Insn('LT'), Insn('BOOL_AND'), Insn('END')]), [
						Insn('0x60', 0),
						Insn('SLEEP', 500),
						Insn('SOUND_PLAY', 1501, 0, 255, 100),
						Insn('0x74', Object(1), 7680),
						Insn('0x71', Object(1), b'\x01\x00', 30, 0),
						Insn('SOUND_PLAY', 464, 0, 0, 100),
						Insn('0x79', b'\x01\x00'),
						Insn('SLEEP', 500),
						Insn('FADE_ON', 1000, Color(0x00000000), 255),
						Insn('SLEEP', 500),
						Insn('0x0D'),
						Insn('SOUND_PLAY', 488, 0, 0, 100),
						Insn('SLEEP', 2500),
						Insn('FLAG_SET', Flag(1009)),
						Insn('FLAG_SET', Flag(1022)),
						Insn('SWITCH', [Insn('VAR', 0), Insn('END')], {
							0: [
								Insn('NEW_SCENE', 'c0100', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							1: [
								Insn('NEW_SCENE', 'r0000', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							2: [
								Insn('NEW_SCENE', 'r1000', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							3: [
								Insn('NEW_SCENE', 'r1500', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							4: [
								Insn('NEW_SCENE', 'r2000', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							5: [
								Insn('NEW_SCENE', 't2500', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							6: [
								Insn('NEW_SCENE', 't2000', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							7: [
								Insn('NEW_SCENE', 't1500', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							8: [
								Insn('NEW_SCENE', 't0000', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							9: [
								Insn('NEW_SCENE', 't0500', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							10: [
								Insn('NEW_SCENE', 'r2050', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							11: [
								Insn('NEW_SCENE', 'm1000', b'\x00\x00\x00\x07'),
								Insn('BREAK'),
							],
							None: [],
						}),
					]),
					(None, [
						Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
					]),
				]),
			]),
			(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
				Insn('0x60', 0),
				Insn('TEXT_RESET', b'\x00'),
				Insn('BGM_STOP', 3000),
				Insn('FADE_ON', 1000, Color(0x00000000), 255),
				Insn('0x0D'),
				Insn('0x5A'),
				Insn('SOUND_PLAY', 13, 0, 0, 100),
				Insn('0x32', Party(255), -2, 0),
				Insn('0x6A', b'\x00\x00\x00\x00\x00\x00'),
				Insn('SLEEP', 3500),
				Insn('0x1F'),
				Insn('FADE_OFF', 1000, Color(0x00000000)),
				Insn('TEXT_RESET', b'\x00'),
			]),
			(None, [
				Insn('0x60', 0),
				Insn('TEXT_RESET', b'\x00'),
				Insn('SLEEP', 500),
				Insn('0x5A'),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			]),
		]),
	]),
	Insn('0x0A', 134217728),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('EVENT_BEGIN', 1),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('CHAR_SET_POS', Char(0), (2740, 0, 21060), 89),
	Insn('CHAR_SET_POS', Char(1), (2740, 0, 21060), 89),
	Insn('CHAR_SET_POS', Char(2), (2740, 0, 21060), 89),
	Insn('CHAR_SET_POS', Char(3), (2740, 0, 21060), 89),
	Insn('CHAR_SET_POS', Char(4), (2740, 0, 21060), 89),
	Insn('CHAR_SET_POS', Char(5), (2740, 0, 21060), 89),
	Insn('SLEEP', 1),
	Insn('CAM_OFFSET', (2740, 600, 21060), 0),
	Insn('CAM_ROTATE', 45, 21, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('SOUND_PLAY', 489, 0, 0, 100),
	Insn('SLEEP', 2000),
	Insn('IF', [
		(Expr([Insn('RAND'), Insn('CONST', 100), Insn('MOD'), Insn('CONST', 50), Insn('LT'), Insn('END')]), [
			Insn('SOUND_PLAY', 1502, 0, 255, 100),
		]),
		(None, [
			Insn('SOUND_PLAY', 1503, 0, 255, 100),
		]),
	]),
	Insn('SLEEP', 500),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x0A', 134217728),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}有一个巴士停靠站。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_END', Char(255)),
		]),
		(Expr([Insn('ATTR', 4), Insn('CONST', 4), Insn('EQ'), Insn('END')]), [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}有一个巴士停靠站。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_END', Char(255)),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CALL', Function((0, 3))),
		]),
		(None, [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}有一个巴士停靠站。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(809)), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0001F今天还是不要坐巴士了吧。{wait}'
						'{page}'
						'为了进行调查，\n'
						'还是徒步走一走比较好。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1)), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0001F继昨天之后……\n'
						'今天也没法乘坐巴士啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(257), Text(
						'#0001F继昨天之后……\n'
						'今天也没法乘坐巴士啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0104F嗯，走路去吧。{wait}'
						'{page}'
						'#0100F说不定在路上\n'
						'还会发现什么线索呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0201F……加油吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('FLAG_SET', Flag(1)),
			Insn('TEXT_END', Char(255)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1537)), Insn('0x23', 1), Insn('CONST', 5), Insn('EQ'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_VAR', 3, Expr([Insn('CONST', 5), Insn('SET'), Insn('END')])),
			Insn('CALL', Function((0, 6))),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('FLAG', Flag(1542)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1537)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 12))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0xFFFFFFFF), 0),
	Insn('FADE_ON', 500, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FADE_OFF', 0, Color(0xFFFFFFFF)),
	Insn('0xE0', b'\x01'),
	Insn('LOAD_CHCP', 'chr/ch00250', 30),
	Insn('LOAD_CHCP', 'chr/ch00254', 31),
	Insn('EFF_LOAD', ResId(0), 'battle\\mgaria0.eff'),
	Insn('EFF_LOAD', ResId(1), 'event\\eva06_00.eff'),
	Insn('SOUND_LOAD', 840),
	Insn('CAM_OFFSET', (3230, 900, 11740), 0),
	Insn('CAM_ROTATE', 90, 18, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 21500, 0),
	Insn('CHAR_SET_POS', Char(257), (1600, 0, 9670), 0),
	Insn('CHAR_SET_POS', Char(258), (2680, 0, 8580), 0),
	Insn('CHAR_SET_POS', Char(259), (840, 0, 8350), 0),
	Insn('CHAR_SET_POS', Char(260), (1240, 120, 7280), 0),
	Insn('FORK', 257, 1, [
		Insn('0x95', Char(254), (3270, 0, 13110), 2000, 0),
	]),
	Insn('FORK', 258, 1, [
		Insn('0x95', Char(254), (4430, 0, 12180), 2000, 0),
	]),
	Insn('FORK', 259, 1, [
		Insn('0x95', Char(254), (2180, 0, 11520), 2000, 0),
	]),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (2900, 0, 10410), 2000, 0),
	]),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_DISTANCE', 19500, 3000),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200194V#0205F#12P啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'y'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200195V#0005F#5P缇欧，怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200196V#0105F#5P莫非……\n'
		'你又听到什么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200197V#0201F#12P是……\n'
		'我提高一下传感器的感知度！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_ROTATE', Char(259), 270, 500),
	Insn('SLEEP', 300),
	Insn('BGM_SET_VOLUME', b'<\xe8\x03\x00\x00'),
	Insn('SOUND_PLAY', 1278, 0, 255, 100),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(259), 30),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('0x0D'),
	Insn('CHAR_SET_CHCP', Char(259), 31),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('SOUND_PLAY', 831, 0, 0, 100),
	Insn('SOUND_PLAY', 840, 0, 2, 100),
	Insn('EFF_PLAY', (ResId(0), 0), Char(259), 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('EFF_PLAY', (ResId(1), 1), Char(259), 320, 0, 0, 1450, 0, 0, 0, 0, 0, 0, (2000, 2000, 2000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('CHAR_ANIMATION', Char(259), 2000, [
		0,
		1,
		2,
		1,
		0,
		1,
		2,
		1,
	]),
	Insn('CHAR_ANIMATION', Char(259), 2000, [
		0,
		1,
		2,
		1,
		0,
		1,
		2,
		1,
	]),
	Insn('CHAR_ANIMATION', Char(259), 2000, [
		0,
		1,
		2,
		1,
		0,
		1,
		2,
		1,
	]),
	Insn('CHAR_ANIMATION', Char(259), 2000, [
		0,
		1,
		2,
		1,
		0,
		1,
		2,
		1,
	]),
	Insn('SOUND_PLAY', 839, 0, 0, 100),
	Insn('SLEEP', 2000),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(258), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200198V#0007F#5P刚才的是……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200199V#0101F#5P虽然很微弱……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200200V#0303F#11P嗯，大概是魔兽的远吠吧。{wait}'
		'{page}'
		'#11200201V#0300F要不是有小缇注意到，\n'
		'我们就都会听漏了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FORK_QUIT', Char(259), 2),
	Insn('EFF_STOP', (ResId(0), 2)),
	Insn('EFF_STOP', (ResId(1), 2)),
	Insn('SOUND_PLAY', 820, 0, 0, 100),
	Insn('FORK_FUNC', Char(11), 1, Function((0, 11))),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(259), 255),
	Insn('CHAR_SET_FRAME', Char(259), 0),
	Insn('0x0D'),
	Insn('BGM_SET_VOLUME', b'd\xe8\x03\x00\x00'),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200202V#0203F#5P#40W呼……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(259), Char(257), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200203V#0201F#12P……刚才的远吠\n'
		'应该是从山道那边传来的。{wait}'
		'{page}'
		'#11200204V大概是在西北偏北方向，距离此处４０塞尔矩左右的地方。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200205V#0001F#5P西北偏北，距离４０塞尔矩……\n'
		'大概是在山道途中吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200206V#0305F#11P也就是说……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 300),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_ROTATE', Char(254), 45, 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('CHAR_WATCH', Char(257), Char(258), 500),
	Insn('SLEEP', 800),
	Insn('CHAR_WATCH', Char(257), Char(259), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200207V#0006F#5P那个……艾莉、缇欧。{wait}'
		'{page}'
		'#11200208V虽然继昨天之后，\n'
		'这么说有点不太好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(258), Char(257), 500),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200209V#0104F#11P不，不用介意。{wait}'
		'{page}'
		'#11200210V#0100F这也是机缘巧合吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200211V#0204F#12P……我也没问题。{wait}'
		'{page}'
		'#11200212V#0208F而且，刚才的远吠……\n'
		'我感觉好像是在向\n'
		'我们传达什么信息……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 300),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 300),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200213V#0005F#5P传达信息……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200214V#0301F#11P是威吓之类的感觉吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11200215V#0208F#12P不……我感觉到其中包含有\n'
		'更加清晰的意志……{wait}'
		'{page}'
		'#11200216V#0206F……对不起，\n'
		'好像找不到合适的语言来表达。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200217V#0003F#5P是吗……{wait}'
		'{page}'
		'#11200218V#0001F……不管怎样，如果警备队出动，\n'
		'就很可能会被它们逃掉。{wait}'
		'{page}'
		'#11200219V现在也只有靠我们自己\n'
		'想办法将它们找出来了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11200220V#0101F#5P是呀，加油吧。{wait}'
		'{page}'
		'#11200221V要正式调查山道的话，\n'
		'最好多做些准备吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11200222V#0001F#5P嗯，而且到时候也没空闲\n'
		'去处理其它支援请求了吧。{wait}'
		'{page}'
		'#11200223V先把该做的事情都解决掉，\n'
		'再开始探索山道吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11200224V#0302F#11P那么，准备完毕之后，\n'
		'再踏上快乐的远足之行吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('0x49'),
	Insn('0xD5', 30),
	Insn('0xD5', 31),
	Insn('0x37'),
	Insn('CHAR_SET_POS', Char(0), (1200, 0, 13100), 0),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('FLAG_SET', Flag(802)),
	Insn('QUEST', 64, Insn('TASK_SET', 1)),
	Insn('FORK_QUIT', Char(11), 1),
	Insn('SOUND_STOP', 840),
	Insn('0xE0', b'\x00'),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('SOUND_LOOP', 840, 90),
	Insn('SLEEP', 50),
	Insn('SOUND_LOOP', 840, 80),
	Insn('SLEEP', 50),
	Insn('SOUND_LOOP', 840, 70),
	Insn('SLEEP', 50),
	Insn('SOUND_LOOP', 840, 60),
	Insn('SLEEP', 50),
	Insn('SOUND_LOOP', 840, 50),
	Insn('SLEEP', 50),
	Insn('SOUND_LOOP', 840, 40),
	Insn('SLEEP', 50),
	Insn('SOUND_LOOP', 840, 30),
	Insn('SLEEP', 50),
	Insn('SOUND_LOOP', 840, 20),
	Insn('SLEEP', 50),
	Insn('SOUND_LOOP', 840, 10),
	Insn('SLEEP', 50),
	Insn('SOUND_STOP', 840),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('EVENT_BEGIN', 0),
	Insn('0xE0', b'\x01'),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (2110, 2900, 19980), 0),
	Insn('CAM_ROTATE', 32, 20, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 20380, 0),
	Insn('CAM_OFFSET', (2110, 900, 19980), 3000),
	Insn('CHAR_SET_POS', Char(257), (2130, 0, 19420), 270),
	Insn('CHAR_SET_POS', Char(258), (2130, 0, 17710), 270),
	Insn('CHAR_SET_POS', Char(259), (3640, 0, 21250), 270),
	Insn('CHAR_SET_POS', Char(260), (4200, 0, 19810), 270),
	Insn('CHAR_SET_POS', Char(265), (3910, 0, 17590), 270),
	Insn('CHAR_FLAG1_UNSET', Char(4), 128),
	Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100251V#0000F#11P这好像就是上士\n'
		'驾驶的车辆吧？{wait}'
		'{page}'
		'#14100252V以前也曾\n'
		'搭乘过几次……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100253V#0504F#11P嗯，是的。{wait}'
		'{page}'
		'#14100254V#0502F无论路况多么恶劣都能顺利行进，\n'
		'是警备队引以为傲的轻装甲机动车呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#14100255V#0306F#11P不过，大概还是抵挡不了\n'
		'战车的炮轰吧。{wait}'
		'{page}'
		'#14100256V#0300F最多也只能弹开\n'
		'加特林炮弹这种级别的火力吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(265), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_WATCH', Char(265), Char(260), 500),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100257V#0506F#12P呜呜……\n'
		'请不要这么说嘛～{wait}'
		'{page}'
		'#14100258V#0501F它毕竟也算是汇集了最新技术的\n'
		'高性能车辆～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(265), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(265), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(265), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(265), 500),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100259V#0106F#6P嗯，说不定，是因为克洛斯贝尔\n'
		'被限制储备战车……{wait}'
		'{page}'
		'#14100260V#0100F所以就打算\n'
		'凭机动性来弥补吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#14100261V#0203F#5P不仅是战车，连军用飞艇\n'
		'也是一艘都没有呢。{wait}'
		'{page}'
		'#14100262V#0200F以克洛斯贝尔那充足的财政资源来说，\n'
		'完全可以买下很多架了……{wait}'
		'{page}'
		'#14100263V果然还是因为帝国\n'
		'与共和国施加了压力吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100264V#0506F#12P嗯……是啊。{wait}'
		'{page}'
		'#14100265V#0501F特别是帝国，在十二年前\n'
		'的战争中，似乎曾因为利贝尔的\n'
		'军用飞艇而吃尽苦头。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#14100266V#0103F#6P如果让克洛斯贝尔随意拥有，\n'
		'万一敌对起来，对他们就很有威胁了……{wait}'
		'{page}'
		'#14100267V#0101F帝国和共和国的意图\n'
		'都是不言自明啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#14100268V#0003F#5P原来如此……{wait}'
		'{page}'
		'#14100269V#0001F像克洛斯贝尔这样的地形，\n'
		'要是有飞艇的话，\n'
		'巡逻效率一定会更高的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#14100270V#0506F#12P唉，就是说嘛～{wait}'
		'{page}'
		'#14100271V#0504F──算啦，就不提这些啦。{wait}'
		'{page}'
		'#14100272V#0500F如果想乘坐车辆移动，\n'
		'随时都可以和我说。{wait}'
		'{page}'
		'#14100273V只要是车子能去的地方，\n'
		'我都可以送大家去。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}今天一天，可以搭乘诺艾儿的警备队车辆，\n'
		'在自治州各地自由移动。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}请在场景中调查警备队车辆，\n'
		'并选择目的地。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}此外，如果丢下警备队车辆，\n'
		'乘坐巴士或徒步移动至其它地点时，\n'
		'警备队车辆依然会停留在原地。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}请一定留意，\n'
		'不要忘记停车地点。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}※需要前往山道尽头的遗迹时，\n'
		'选择『玛因兹山道丄隧道内』\n'
		'便可以抄近道。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (2850, 0, 18840), 270),
	Insn('CHAR_FLAG1_SET', Char(4), 128),
	Insn('CHAR_FLAG2_SET', Char(4), 32768),
	Insn('FLAG_SET', Flag(1537)),
	Insn('0xE0', b'\x00'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0xE0', b'\x01'),
	Insn('CAM_OFFSET', (-3190, 6260, 780), 0),
	Insn('CAM_ROTATE', 30, 14, 0, 0),
	Insn('0x6E', 550, 0),
	Insn('CAM_DISTANCE', 17120, 0),
	Insn('CAM_OFFSET', (-3190, 2960, 780), 5000),
	Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(258), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(259), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(260), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(265), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('OBJ_FLAG_UNSET', Object(1), 4),
	Insn('OBJ_FLAG_SET', Object(1), 2),
	Insn('OBJ_FLAG_SET', Object(1), 1024),
	Insn('CHAR_FLAG1_SET', Char(10), 32768),
	Insn('0x78', b'\x01', Char(10)),
	Insn('OBJ_FLAG_SET', Object(1), 4096),
	Insn('OBJ_SET_FRAME', Object(1), 'light', Insn('0', 1)),
	Insn('0xD3', Char(10), 0, 180000, 0, 0),
	Insn('0x74', Object(1), 7680),
	Insn('0x70', Object(1), b'\x00\x00'),
	Insn('0x71', Object(1), b'y\x00', 180, 32),
	Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xdc\xb4\xa0', 30, 100, 0),
	Insn('OBJ_SET_FRAME', Object(255), 'model06_shade', Insn('0', 1)),
	Insn('SOUND_PLAY', 485, 0, 0, 100),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CHAR_FLAG1_UNSET', Char(10), 4),
	Insn('CHAR_FLAG1_UNSET', Char(10), 1),
	Insn('CHAR_SET_POS', Char(10), (70, 0, 17900), 0),
	Insn('FORK', 10, 1, [
		Insn('0x95', Char(254), (50, -2930, -8070), 5000, 0),
	]),
	Insn('0x0D'),
	Insn('SLEEP', 1100),
	Insn('FORK_FUNC', Char(10), 3, Function((0, 14))),
	Insn('SOUND_PLAY', 470, 0, 0, 100),
	Insn('SLEEP', 2000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(10), 1),
	Insn('FORK_AWAIT', Char(10), 3),
	Insn('0x6F', b'\x01'),
	Insn('FLAG_SET', Flag(747)),
	Insn('NEW_SCENE', 'c0100', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('0xD3', Char(254), 0, 180000, 0, 0),
	Insn('SLEEP', 50),
	Insn('0xD3', Char(254), 1000, 180000, 0, 0),
	Insn('SLEEP', 50),
	Insn('0xD3', Char(254), 2000, 180000, 0, 0),
	Insn('SLEEP', 50),
	Insn('0xD3', Char(254), 3000, 180000, 0, 0),
	Insn('SLEEP', 50),
	Insn('0xD3', Char(254), 4000, 180000, 0, 0),
	Insn('SLEEP', 50),
	Insn('0xD3', Char(254), 5000, 180000, 0, 0),
	Insn('SLEEP', 50),
	Insn('0xD3', Char(254), 6000, 180000, 0, 0),
	Insn('SLEEP', 50),
	Insn('0xD3', Char(254), 7000, 180000, 0, 0),
	Insn('SLEEP', 50),
	Insn('0xD3', Char(254), 8000, 180000, 0, 0),
	Insn('SLEEP', 50),
	Insn('0xD3', Char(254), 9000, 180000, 0, 0),
	Insn('SLEEP', 50),
	Insn('0xD3', Char(254), 10000, 180000, 0, 0),
	Insn('SLEEP', 50),
	Insn('0xD3', Char(254), 11000, 180000, 0, 0),
	Insn('SLEEP', 50),
	Insn('0xD3', Char(254), 12000, 180000, 0, 0),
	Insn('SLEEP', 50),
	Insn('0xD3', Char(254), 13000, 180000, 0, 0),
	Insn('SLEEP', 50),
	Insn('0xD3', Char(254), 14000, 180000, 0, 0),
	Insn('SLEEP', 50),
	Insn('0xD3', Char(254), 15000, 180000, 0, 0),
	Insn('SLEEP', 50),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('EVENT_BEGIN', 0),
	Insn('SLEEP', 1000),
	Insn('0xEE', 0, 1),
	Insn('CAM_OFFSET', (14140, -670, 19290), 5000),
	Insn('CAM_ROTATE', 45, 21, 0, 5000),
	Insn('0x6E', 510, 5000),
	Insn('CAM_DISTANCE', 23500, 5000),
	Insn('0x6F', b'y'),
	Insn('0xEE', 0, 10),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}调查停靠站的告示牌后，\n'
		'就能乘坐导力巴士。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}进而便可迅速移动至所选目的地，\n'
		'以更高的效率来往于各处。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(1183)),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}\u3000南丄克洛斯贝尔市\n'
		'\u3000东丄克洛斯贝尔大教堂\n'
		'西北丄矿山镇玛因兹３１１塞尔矩{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('EVENT_BEGIN', 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这边是玛因兹山道吗……{wait}'
				'{page}'
				'#0003F现在更加在意乌尔斯拉医院那边。\n'
				'还是不要绕道了，\n'
				'直接去医院吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#0003F可不能带着琪雅\n'
				'在市外乱走啊。{wait}'
				'{page}'
				'#0000F还是不要绕道了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_POS', Char(0), (-27230, -2000, 65230), 135),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]
