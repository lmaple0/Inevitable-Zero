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
		't1030',
		't1030_1',
		None,
		None,
		None,
		None,
	],
	'name3': 't1030',
	'labels': [
		{
			'pos': (10.0, 0.0, -68.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('翠雀饭店方向'),
		},
		{
			'pos': (-5.0, 0.0, 20.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('主题乐园方向'),
		},
	],
	'chcp': [
		'chr/ch28300',
		'chr/ch23500',
		'chr/ch23900',
		'chr/ch24600',
		'chr/ch24200',
		'chr/ch32200',
		'chr/ch10200',
		'chr/ch27600',
		'chr/ch33300',
		'chr/ch34400',
		'chr/ch39000',
	],
	'npcs': [
		{
			'name': Translate('工作人员'),
			'pos': (4750, 4400, 0),
			'angle': 180,
			'_1': b'\x01\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((0, 3)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('工作人员'),
			'pos': (-4000, 4400, 0),
			'angle': 180,
			'_1': b'\x01\x01\x00\x00\x00\x00\x00\x00',
			'function': Function((0, 4)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('咪西'),
			'pos': (360, 4159, -15840),
			'angle': 180,
			'_1': b'\x81\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((0, 5)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('女性'),
			'pos': (-9810, 4000, -5130),
			'angle': 45,
			'_1': b'\x81\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 6)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('女孩'),
			'pos': (-8970, 4000, -4289),
			'angle': 225,
			'_1': b'\x81\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 7)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('男孩'),
			'pos': (-3690, 4000, -19149),
			'angle': 180,
			'_1': b'\x81\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 8)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('男性'),
			'pos': (-3690, 1639, -23280),
			'angle': 0,
			'_1': b'\x81\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((0, 9)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (-7409, 4000, -6219),
			'angle': 180,
			'_1': b'\x81\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 10)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('邦德'),
			'pos': (7699, 4000, -1519),
			'angle': 135,
			'_1': b'\x85\x01\x00\x00\x07\x00\x00\x00',
			'function': Function((0, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('克蕾优'),
			'pos': (9159, 4000, -1759),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x08\x00\x00\x00',
			'function': Function((0, 12)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('桑妮塔'),
			'pos': (7889, 4000, -3069),
			'angle': 360,
			'_1': b'\x95\x01\x00\x00\t\x00\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('玛丽'),
			'pos': (6949, 4000, -3160),
			'angle': 45,
			'_1': b'\x85\x01\x00\x00\n\x00\x00\x00',
			'function': Function((0, 14)),
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
			'pos': (0.0, -48.0, -1.0),
			'range': 225.0,
			'transform': [
				0.10000000149011612,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.3333333432674408,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				-0.0,
				16.0,
				0.20000000298023224,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 16)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
		{
			'pos': (0.0, 4.150000095367432, 3.0),
			'range': 81.0,
			'transform': [
				0.0833333358168602,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.6666666865348816,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.20000000298023224,
				0.0,
				-0.0,
				-2.766666889190674,
				-0.6000000238418579,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (-14170, 4000, -6040),
			'range': 1200,
			'bubble_pos': (-14170, 5500, -6040),
			'_1': b'|\x00\x00',
			'function': Function((0, 18)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (-6650, 4000, 1550),
			'range': 1200,
			'bubble_pos': (-6650, 5500, 1550),
			'_1': b'|\x00\x00',
			'function': Function((0, 19)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (4180, 4250, -9540),
			'range': 1200,
			'bubble_pos': (4180, 4250, -9540),
			'_1': b'|\x00\x00',
			'function': Function((0, 17)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00A\x00', Function((0, 1)), Function((0, 2))),
	'code': [None]*22,
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
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1333)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1330)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1329)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1320)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1319)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 55, Insn('TASK_GET', 5))), Insn('OR'), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(10), 128),
				]),
				(None, []),
			]),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 2))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 55, Insn('TASK_GET', 5))), Insn('OR'), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(10), 128),
				]),
				(None, []),
			]),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((1, 18))),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('0xB5', b'\x01\x01\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1312)), Insn('FLAG', Flag(1314)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0xB5', b'\x01\x00\x80\x00'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('FLAG', Flag(1342)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
			Insn('OBJ_SET_FRAME', Object(255), 't1030_sky', Insn('0', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 't1030_sky_y', Insn('1', 1)),
		]),
		(None, [
			Insn('OBJ_SET_FRAME', Object(255), 't1030_sky', Insn('1', 1)),
			Insn('OBJ_SET_FRAME', Object(255), 't1030_sky_y', Insn('0', 1)),
		]),
	]),
	Insn('0x65', 2, 1),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 36, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 36, Insn('TASK_GET', 3))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EFF_LOAD', ResId(1), 'event\\eva00_00.eff'),
			Insn('EFF_PLAY', (ResId(1), 1), Char(255), 0, 4180, 0, 4250, 0, -9540, -1, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
			Insn('0x66', 2, 1),
		]),
		(None, []),
	]),
	Insn('SOUND_POSITION', 885, [
		37600,
		4000,
		17620,
		90000,
		60000,
	], 100, 0),
	Insn('0xE1', (-2490, 4000, 10240)),
	Insn('0xE1', (-77760, 4000, 18030)),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 2))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(6)), Insn('END')]), [
							Insn('IF', [
								(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
									Insn('CALL', Function((0, 21))),
								]),
								(None, [
									Insn('CALL', Function((0, 20))),
								]),
							]),
						]),
						(None, [
							Insn('CALL', Function((1, 20))),
							Insn('FLAG_SET', Flag(6)),
						]),
					]),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 55, Insn('TASK_GET', 1))), Insn('END')]), [
					Insn('CALL', Function((1, 19))),
				]),
				(None, [
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 55, Insn('TASK_GET', 0))), Insn('END')]), [
							Insn('CALL', Function((1, 2))),
						]),
						(None, [
							Insn('CALL', Function((1, 1))),
							Insn('QUEST', 55, Insn('TASK_SET', 0)),
						]),
					]),
					Insn('CALL', Function((1, 3))),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1333)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1330)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1329)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1320)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1319)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CALL', Function((0, 21))),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('CALL', Function((0, 20))),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][4] = [
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
					Insn('TEXT_TALK', Char(254), Text(
						'园内除了各种游乐设施之外，\n'
						'还有贩卖咪西\n'
						'周边产品的商店哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'其中最推荐的是\n'
						'『咪西猫耳头饰』！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'在园内特有的热烈气氛中，\n'
						'体验一下彻底放松的感觉如何呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'园内除了各种游乐设施之外，\n'
						'还有贩卖咪西\n'
						'周边产品的商店哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'除了『咪西猫耳头饰』之外，\n'
						'还有挂绳等小装饰，\n'
						'各种周边应有尽有哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'刚才进去的旅行者……\n'
						'真是很有趣的人呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'说着『要确认一下\n'
						'主题乐园里\n'
						'有没有另一只咪西！』{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……感觉气势十足哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F（是雷克多先生吧……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0106F（他到底在干什么呢……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，不必担心。\n'
						'咪西是不可能\n'
						'出现第二只的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F（嗯～因为扮演人员的值班日程\n'
						'\u3000一定排得很紧吧。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0211F（……请不要说这种\n'
						'\u3000破坏别人梦想的话。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0011F（对、对不起。）{wait}'
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

data['code'][5] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 55, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('CALL', Function((1, 21))),
		]),
		(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'{color 10}大家好！\n'
				'欢迎来到奇幻乐园。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'{color 10}咪嘻嘻，要玩得开心哦～！{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0201F……真的咪西……！！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F缇、缇欧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0203F……咳，\n'
				'没什么。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(5)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'{color 10}大家好！\n'
				'欢迎来到奇幻乐园。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'{color 10}咪嘻嘻，要玩得开心哦～！{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'哇……\n'
		'这就是主题乐园啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'……真是好大啊，\n'
		'要是能玩个遍就好了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'哇！\n'
		'我早就想来这里了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('TEXT_START', Char(254)),
	Insn('CHAR_ROTATE', Char(254), 180, 0),
	Insn('TEXT_TALK', Char(254), Text(
		'爸爸～快进去吧～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 0, 0),
			Insn('TEXT_TALK', Char(13), Text(
				'爸爸～！\n'
				'你在干什么～？\n'
				'快点进去啦！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'好好，知道了，知道了，\n'
				'稍微等一下。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(2)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'话说，小孩子还真是\n'
				'喜欢这种地方啊。\n'
				'都已经傍晚了，竟然还那么精神。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'要是不管他的话，一定会\n'
				'玩到精疲力尽为止吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'虽然刚刚傍晚，不过还是趁着\n'
		'开始拥挤之前先回饭店吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(4)), Insn('END')]), [
			Insn('TEXT_TALK', Char(16), Text(
				'其实我还有工作没做完。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(16), Text(
				'不能一直玩啊……\n'
				'算、算了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(16), Text(
				'偶尔也要照顾到家人的情绪……\n'
				'……虽然这么想。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(16), Text(
				'但她们两个的热情也太高涨了吧……\n'
				'算、算了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(4)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(17), Text(
		'今天我先生\n'
		'带我们来玩了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(17), Text(
		'呵呵，好期待\n'
		'主题乐园哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(18), Text(
		'爸爸，桑妮塔\n'
		'想去坐摩天轮。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(18), Text(
		'想和玛丽一起\n'
		'升上最高\n'
		'的地方。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(19), Text(
		'喵～呜……丅{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('EVENT_BEGIN', 0),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1333)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1330)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1329)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1320)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1319)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(337), Text(
						'#5705F……现在要去\n'
						'主题乐园玩吗？{wait}'
						'{page}'
						'#5702F买套咪西的玩偶服，\n'
						'然后穿去参加拍卖会\n'
						'似乎也挺有趣的呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F但那未免也太诡异了吧……{wait}'
						'{page}'
						'#0000F总、总而言之，\n'
						'现在还是先去时装店吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F现在不需要去主题乐园，\n'
						'先去时装店买正装吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1312)), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0003F这次的目标是『黑之拍卖会#10RSchwarz Auction#』，\n'
				'主题乐园只好放弃了吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#0208F…………………………{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0011F（果、果然还是……觉得有些遗憾吗？）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(None, []),
	]),
	Insn('CHAR_SET_POS', Char(0), (0, 4400, -1250), 180),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('EVENT_BEGIN', 2),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('EVENT_BEGIN', 0),
	Insn('EFF_LOAD', ResId(0), 'event\\ev309_00.eff'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (0, 2200, -47400), 0),
	Insn('CAM_ROTATE', 0, 20, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 22940, 0),
	Insn('CAM_DISTANCE', 21940, 2500),
	Insn('CHAR_SET_POS', Char(257), (600, 0, -49200), 0),
	Insn('CHAR_SET_POS', Char(258), (-600, 0, -49200), 0),
	Insn('CHAR_SET_POS', Char(259), (1200, 0, -50700), 0),
	Insn('CHAR_SET_POS', Char(260), (-1200, 0, -50700), 0),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xc4\t\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK', 258, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xc4\t\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK', 259, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xc4\t\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK', 260, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00\xc4\t\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('CHAR_FLAG1_SET', Char(8), 32768),
	Insn('CHAR_FLAG1_SET', Char(9), 32768),
	Insn('CHAR_FLAG1_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(11), 32768),
	Insn('CHAR_FLAG1_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 32768),
	Insn('CHAR_FLAG1_SET', Char(14), 32768),
	Insn('CHAR_FLAG1_SET', Char(15), 32768),
	Insn('CHAR_FLAG1_SET', Char(16), 32768),
	Insn('CHAR_FLAG1_SET', Char(17), 32768),
	Insn('CHAR_FLAG1_SET', Char(18), 32768),
	Insn('CHAR_FLAG1_SET', Char(19), 32768),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500395V#0205F#11P啊……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500396V#0005F#5P那就是主题乐园吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CAM_OFFSET', (0, 4500, -47400), 3000),
	Insn('CAM_ROTATE', 0, 0, 0, 3000),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 10020, 3000),
	Insn('0x6F', b'y'),
	Insn('CROSSFADE', 1000),
	Insn('EFF_PLAY', (ResId(0), 0), Char(255), 0, 0, 0, 4250, 0, -9800, -1, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('CAM_OFFSET', (-20, 9500, -8210), 0),
	Insn('CAM_ROTATE', 337, 10, 0, 0),
	Insn('0x6E', 600, 0),
	Insn('CAM_DISTANCE', 27300, 0),
	Insn('CAM_OFFSET', (-20, 5300, -8210), 8000),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('CROSSFADE', 1000),
	Insn('EFF_STOP', (ResId(0), 0)),
	Insn('CAM_OFFSET', (-2830, 2200, -34120), 0),
	Insn('CAM_ROTATE', 315, 20, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 27290, 0),
	Insn('CAM_DISTANCE', 25290, 3000),
	Insn('0x90', Char(257), (-3930, 4000, -37980), b'\x00\x00'),
	Insn('0x90', Char(258), (-4800, 4000, -38790), b'\x00\x00'),
	Insn('0x90', Char(259), (-2750, 4000, -39310), b'\x00\x00'),
	Insn('0x90', Char(260), (-3800, 4000, -40070), b'\x00\x00'),
	Insn('FORK', 257, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00|\x15\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00|\x15\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00|\x15\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('0x9B', b'\x00', Char(254), b'\x00\x00|\x15\x00\x00\xd0\x07\x00\x00\x00'),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('0x6F', b'\x10'),
	Insn('0x0D'),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500397V#0205F#6P………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500398V#0012F#5P怎么说呢……\n'
		'看上去，的确是个很欢乐的地方啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500399V#0302F#6P嗯，实际上也非常不错哦。{wait}'
		'{page}'
		'#13500400V#0304F有摩天轮和云霄飞车。{wait}'
		'{page}'
		'#13500401V还有鬼屋和\n'
		'旋转木马。{wait}'
		'{page}'
		'#13500402V#0300F甚至还建有童话故事里出现的\n'
		'中世纪城堡哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500403V#0011F好、好像很厉害呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500404V#0104F#5P呵呵，这里是ＩＢＣ作为\n'
		'旅游热点而开发的设施，\n'
		'的确下了不少功夫呢。{wait}'
		'{page}'
		'#13500405V#0102F我也曾受贝尔的邀请，\n'
		'进去玩过一次，\n'
		'真是逛都逛不完哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500406V#0205F#6P…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_WATCH', Char(257), Char(259), 500),
	Insn('FORK', 258, 2, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('FORK', 260, 2, [
		Insn('CHAR_WATCH', Char(254), Char(259), 300),
	]),
	Insn('TEXT_TALK', Char(257), Text(
		'#13500407V#0012F#5P嗯……{wait}'
		'{page}'
		'#13500408V#0000F……虽然不能耽误太多时间，\n'
		'不过，要不要稍微进去看一下呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500409V#0208F#6P…………不………………{wait}'
		'{page}'
		'#13500410V#0206F我们又不是来玩的，\n'
		'没必要特意进去。{wait}'
		'{page}'
		'#13500411V而且门票似乎也很贵。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#13500412V#0303F#6P嗯，的确不便宜啊。{wait}'
		'{page}'
		'#13500413V#0300F现在才进去的话，\n'
		'根本就玩不回本吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#13500414V#0109F#5P还是等到下次休假时，\n'
		'大家一起过来玩吧。{wait}'
		'{page}'
		'#13500415V#0102F到时候，一定要从上午开始，\n'
		'痛痛快快地玩上一整天哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(259), Char(258), 500),
	Insn('TEXT_TALK', Char(259), Text(
		'#13500416V#0202F#12P……好的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CHAR_SET_POS', Char(0), (-3890, 0, -32460), 0),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('FLAG_SET', Flag(1314)),
	Insn('CHAR_FLAG1_UNSET', Char(8), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(9), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(10), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(11), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(12), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(13), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(14), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(15), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(16), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(17), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(18), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(19), 32768),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('EVENT_BEGIN', 0),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (8380, 7250, -13860), 0),
	Insn('CAM_ROTATE', 313, 28, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 20350, 0),
	Insn('CHAR_SET_POS', Char(257), (4970, 4250, -11650), 0),
	Insn('CHAR_SET_POS', Char(258), (4400, 4250, -13060), 0),
	Insn('CHAR_SET_POS', Char(259), (6270, 4000, -12400), 315),
	Insn('CHAR_SET_POS', Char(260), (7200, 4000, -11960), 315),
	Insn('EFF_STOP', (ResId(1), 2)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1318)), Insn('END')]), [
			Insn('CHAR_SET_POS', Char(337), (5580, 4000, -13450), 0),
		]),
		(None, []),
	]),
	Insn('0x0D'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'获得了{item 845}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 845, 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0005F嗯，这个戒指是……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0300F说不定正是托马\n'
		'那家伙说的订婚戒指啊。{wait}'
		'{page}'
		'#0306F没办法，\n'
		'稍后拿到饭店的房间里\n'
		'给他看看吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('QUEST', 36, Insn('TASK_SET', 3)),
	Insn('0x65', 2, 1),
	Insn('CHAR_SET_POS', Char(0), (4970, 4250, -11650), 0),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('TEXT_START', Char(255)),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}这里画着\n'
		'主题乐园的平面图。{wait}'
		'{page}'
		'广阔的区域内\n'
		'似乎遍布着\n'
		'各式各样的游乐设施。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('TEXT_START', Char(255)),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}   ～致各位来园宾客～\n'
		'本主题乐园内\n'
		'严禁喧闹生事，\n'
		'或携带危险物品入园。\n'
		'\n'
		'此外，儿童必须\n'
		'由监护人陪同入园，\n'
		'敬请配合。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'欢迎来到米修拉姆\n'
				'引以为傲的主题乐园。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'请问您有门票吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F不……这次还有要事。\n'
				'不好意思，就不进去了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哦哦，是吗……\n'
				'那可真遗憾。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'期待您下次前来时\n'
				'入园游玩。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(0)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'您这次似乎\n'
				'不打算进入主题乐园……\n'
				'真是遗憾。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过，米修拉姆还有其它很多\n'
				'值得一去的好地方。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'入夜后，就算在园外，\n'
				'应该也可以看到烟火，\n'
				'请不要错过哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('TEXT_TALK', Char(254), Text(
		'为了参加主题乐园的夜场\n'
		'而在这个时间入园的客人\n'
		'也非常多。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'充满浪漫气氛的夜场，\n'
		'非常受情侣们欢迎哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]
