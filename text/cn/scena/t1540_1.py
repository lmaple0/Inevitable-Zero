# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't1540',
	'name2': 't1540',
	'location': 81,
	'bgm': 123,
	'flags': 8192,
	'includes': [
		't1540',
		't1540_1',
		't1500_1',
		None,
		None,
		None,
	],
	'name3': 't1540_1',
	'labels': [],
	'chcp': [],
	'npcs': [],
	'monsters': [],
	'triggers': [],
	'objects': [],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00Q\x00', Function((0, 1)), Function((0, 3))),
	'code': [None]*53,
	'anim': [],
}

data['code'][0] = [
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
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'对了，\n'
						'约亚西姆医生说\n'
						'我明天应该就可以出院了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呜啊～工作一定堆积如山了。\n'
						'还想再睡一下啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'唉，难得明天可以出院了，\n'
						'但一想到工作还真郁闷啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊，我说你们几个。\n'
						'屋顶调查得怎么样了？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0001F嗯，虽然还残留着一些谜团……\n'
						'不过已经发现了魔兽去过的痕迹。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真、真的吗！？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯～那果然\n'
						'不是我在做梦啊………………{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……嗯，谢谢你们了。\n'
						'光是确定了这一点，\n'
						'对我来说，就算是有收获了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F不用客气。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F那么……\n'
						'去向赛西儿小姐\n'
						'报告吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(796)), Insn('END')]), [
							Insn('TEXT_TALK', Char(260), Text(
								'#0300F她好像去了院区\n'
								'三楼的单人间吧。\n'
								'赶快过去看看吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('TEXT_TALK', Char(260), Text(
								'#0300F去护理师中心那里问问，\n'
								'应该就能知道她在哪里了。\n'
								'赶快过去看看吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'那果然不是我在做梦啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'嗯……那果然\n'
						'是我的幻觉吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'如果真的只是梦就好了，\n'
						'可我全身都受了伤……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……总之，调查就拜托你们了。\n'
						'无论是梦还是现实，\n'
						'我都想知道受伤的原因呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][1] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 2))),
				]),
				(None, [
					Insn('CHAR_WATCH', Char(12), Char(9), 0),
					Insn('0x4B', Char(12), -1),
					Insn('TEXT_TALK', Char(254), Text(
						'嘿嘿，又失败了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不要介意，不要介意。\n'
						'人生在世，\n'
						'孰能无过嘛。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(12), Text(
						'但你的过失也太多了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('0x4C', Char(12), -1),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 2))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'米海尔和艾妲\n'
						'出去散步了～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'大概在水边吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((2, 8))),
				]),
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 3))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵……\n'
						'有这么多体温计的话，\n'
						'再怎么失败也不怕了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 3))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，失败失败。\n'
						'原来体温计放在\n'
						'这边的口袋里了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 2))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呼……\n'
						'梅菲尔真是\n'
						'爱生气。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'待会还要去\n'
						'盖巴尔先生那里啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('CHAR_WATCH', Char(9), Char(12), 0),
	Insn('CHAR_WATCH', Char(12), Char(9), 0),
	Insn('0x4B', Char(9), -1),
	Insn('0x4B', Char(12), -1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'希蓉，你啊……\n'
				'连杯咖啡也泡不好吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'为什么咖啡里\n'
				'会有红茶的香味啊？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'嗯～大概是因为……\n'
				'我可能把咖啡\n'
				'和红茶放在一起泡了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'这我知道！\n'
				'所以我才想问你为什么总是这样……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'……唉，真是累死人了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'那个～梅菲尔，\n'
				'米海尔得的到底是什么病？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'嗯……是很难治的病，\n'
				'想痊愈的话，似乎必须要动手术。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'但是，外科手术给人感觉很恐怖吧？\n'
				'米海尔似乎也不例外，\n'
				'总是无法下定决心，接受手术呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'呼，是这样啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'只要有接受手术的勇气，\n'
				'米海尔的病也是能治好的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'要是能有什么让他产生勇气的\n'
				'契机就好了～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'你啊……偶尔也会\n'
				'说两句正经话呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('TEXT_TALK', Char(12), Text(
				'听说你昨天……把番茄酱\n'
				'洒到盖巴尔先生的床单上了？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'是呀～\n'
				'真是吓我一跳。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'偶然来查房的医生\n'
				'误以为是大出血而吓得昏倒……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'你、你这人啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'总之，床单算是\n'
				'洗干净了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'你可要把干净的\n'
				'新床单拿过去，\n'
				'并向盖巴尔先生好好道歉哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'哎……可是我不太喜欢\n'
				'那个大叔哎……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'不准发牢骚！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('FLAG_SET', Flag(1)),
	Insn('FLAG_SET', Flag(2)),
	Insn('0x4C', Char(9), -1),
	Insn('0x4C', Char(12), -1),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('CHAR_WATCH', Char(9), Char(27), 0),
	Insn('CHAR_SET_FRAME', Char(27), 2),
	Insn('0x4B', Char(9), -1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'来～到了今天量体温的时间了哦。\n'
				'要夹体温计了哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(27), Text(
				'……护、护理师小姐。\n'
				'要量体温是没问题……\n'
				'但你为什么拿着十支体温计？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'因为，有这么多的话，就算量的时候\n'
				'断掉几根，至少应该也有一根能正常量出来嘛！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(27), Text(
				'（好、好不安……）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'来～到了量体温的时间了哦。\n'
				'要夹体温计了哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(27), Text(
				'……护、护理师小姐。\n'
				'你没有像昨天一样，\n'
				'错把注射器拿来吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'讨厌，没有啦。\n'
				'就算是我，也不会重复\n'
				'同样的错误啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'…………啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(27), Text(
				'…………………………{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('FLAG_SET', Flag(1)),
	Insn('CHAR_SET_FRAME', Char(27), 0),
	Insn('0x4C', Char(9), -1),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('CALL', Function((1, 5))),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(793)), Insn('FLAG', Flag(796)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 11))),
		]),
		(None, [
			Insn('TEXT_START', Char(10)),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(10), Text(
								'再过几天，就是久违的假日了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'呵呵，兰迪先生……\n'
								'下次大家再一起去玩吧！{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(260), Text(
								'#0300F好，等你们哦！{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('IF', [
								(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('NE'), Insn('END')]), [
									Insn('TEXT_TALK', Char(266), Text(
										'#0603F……执行任务时，竟敢当着我的面\n'
										'约定出游，真是好大的胆子啊。{wait}'
										'{page}'
										'#0600F如果你是一课的成员，\n'
										'回去以后就得给我\n'
										'拼死写检讨书了。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(260), Text(
										'#0305F呃……！？{wait}'
									)),
									Insn('TEXT_WAIT'),
								]),
								(None, []),
							]),
							Insn('FLAG_SET', Flag(3)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(10), Text(
								'自纪念庆典以来，终于\n'
								'可以请到假了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'我会把兰恩和艾妲也约上，\n'
								'下次再一起去玩吧～{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'差不多快到晚饭的时间了呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'要去琪秀宿舍长那里\n'
						'给病人们取餐点才行～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'今天送来的那些伤患，\n'
						'轻伤的那位躺在\n'
						'２０１号室哦～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(10), Text(
								'那个叫盖巴尔的议员大叔\n'
								'住在三楼的单人病房……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'有一次，他喝得大醉，\n'
								'然后闯进了护理站，\n'
								'还说什么来人给他倒酒呢～{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'之后护理师长很快就赶了回来，\n'
								'把他轰走了……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'真是的，该不会是把护理师\n'
								'当成公关小姐之类的吧～{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(3)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(10), Text(
								'偶尔也会有盖巴尔议员\n'
								'那种给人添麻烦的患者呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'要么就是在医院里住得很舒服，赖着不出院，\n'
								'要么就是对护理师们进行骚扰……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'真是的，感觉好讨厌啊～{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'有个脸蛋涨得通红的小女孩\n'
						'往楼下跑去了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'好像在生气闹别扭的样子……\n'
						'不过还真是可爱啊～㈱{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'啊，这不是警察弟弟嘛。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'赛西儿前辈\n'
						'去３０１号室了哦～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'医生不在的话，\n'
						'总是会觉得不安呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'虽然听说各位实习医生也是很优秀的，\n'
						'但还是比不上教授呀～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(10), Text(
								'肚子饿了……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'护理师的午休是轮流制，\n'
								'所以经常会错过\n'
								'午饭时间呢～{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'给病人量体温的时候，肚子突然叫起来，\n'
								'会很难为情的啊～{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(3)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(10), Text(
								'（咕……）{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'唉……好想早点午休啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(10), Text(
								'明天真想再多休息一天呀，\n'
								'哪怕只多一天也好～{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'因为明天会有游行哦。\n'
								'不观赏那个的话，\n'
								'就不能算是参加了纪念庆典呀～{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'好羡慕当警察的各位呀。\n'
								'可以以工作为借口，\n'
								'去看游行吧？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0006F我、我们才不会\n'
								'做那样的事……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(3)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(10), Text(
								'虽然很想看明天的游行……\n'
								'唉，但毕竟要工作，也没办法呢～{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'昨天值班的梅菲尔\n'
						'和希蓉今天休息～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'我们昨天玩得很开心呢，\n'
						'所以今天一天可得努力工作才行～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('END')]), [
							Insn('CALL', Function((1, 50))),
						]),
						(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(10), Text(
								'那个伊莉雅丄普拉提耶的朋友\n'
								'竟然就在我的身边，真是令人吃惊呢～{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'……能不能拜托\n'
								'赛西儿前辈\n'
								'向伊莉雅小姐要个签名呢？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F（伊莉雅小姐的崇拜者……\n'
								'\u3000还真多啊。）{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(3)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(10), Text(
								'……能不能拜托\n'
								'赛西儿前辈\n'
								'向伊莉雅小姐要个签名呢？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'下次找个机会\n'
								'问问看吧……{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'唉～唉，结果还是没有\n'
						'弄到彩虹剧团的票啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'护理师长虽然很得意地说她以前看过，\n'
						'但现在的彩虹剧团\n'
						'肯定已经更厉害了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'３６度６……很正常呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'接下来是利顿医生了吧～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
					Insn('TEXT_TALK', Char(10), Text(
						'……玛萨护理师长是顺风耳，\n'
						'真有点怕她呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(10), Text(
						'不知道她会不会躲在某处听到\n'
						'我们谈话，可要小心才行……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(849)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(10), Text(
								'啊，赛西儿前辈。\n'
								'辛苦了～{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'休息时间很快\n'
								'就要结束了……\n'
								'你在干什么呢？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(310), Text(
								'#1300F我在帮他们做点事情。\n'
								'抱歉哦，我马上就回来。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'啊，没事没事～\n'
								'稍微迟到一会应该没关系的。\n'
								'……嗯，这几位是？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(260), Text(
								'#0304F我叫兰迪，唐突造访，\n'
								'真是十分抱歉。{wait}'
								'{page}'
								'#0300F……请问小姐芳名？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'那个，我叫菲莉亚……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0006F唉，好了啦，兰迪，\n'
								'你就先安分一下吧……{wait}'
								'{page}'
								'#0000F……咳咳，抱歉，还没有自我介绍。\n'
								'我是警察局丄特务支援课的罗伊德。{wait}'
								'{page}'
								'我们是来调查实习医生利顿\n'
								'遇袭事件的……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'哦，那件事啊～{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'（莫非这个人就是\n'
								'\u3000赛西儿前辈说的……）{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(10), Text(
								'……呵呵，请加油哦～{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0003F（刚、刚才的停顿是什么意思……）{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(849)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(10), Text(
								'调查要加油哦～{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0003F（怎么一直\n'
								'\u3000露出诡异的笑容……）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
				(None, []),
			]),
			Insn('TEXT_END', Char(10)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(799)), Insn('NOT'), Insn('FLAG', Flag(796)), Insn('BOOL_AND'), Insn('FLAG', Flag(797)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 12))),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_START', Char(11)),
			Insn('CALL', Function((2, 0))),
			Insn('TEXT_END', Char(11)),
		]),
		(None, [
			Insn('TEXT_START', Char(11)),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'好，今天一天也要努力工作啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'我们护理师必须要为病人\n'
						'尽心尽力才行。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
							Insn('CHAR_WATCH', Char(11), Char(259), 0),
							Insn('TEXT_TALK', Char(11), Text(
								'……哎呀，缇欧，\n'
								'你的脸色好像不太好啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(259), Text(
								'#0203F……没那回事，\n'
								'请不必介意……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'嗯嗯……是错觉吗？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(4)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(11), Text(
								'是错觉吧……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'……算啦，天也快黑了，\n'
								'回去时可要小心啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'虽然从早上开始就手忙脚乱的，\n'
						'但刚刚总算是稳定下来了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'不管怎么说，\n'
						'病人能够保住性命就好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(11), Text(
								'小滴最近这段时间\n'
								'似乎变得开朗多了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'她很开心地告诉我说，\n'
								'自己交到了新的朋友。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'呵呵，太好啦。\n'
								'朋友就是人生之宝嘛。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(4)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(11), Text(
								'小滴最近这段时间\n'
								'似乎变得开朗多了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'这都是因为她交到了新朋友吧，\n'
								'我们也很替她开心呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(11), Text(
								'赛西儿真是个工作勤奋的女孩啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'而且其他护理师和医生，\n'
								'还有病人们都很信任她。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'真想让赛西儿来继承\n'
								'护理师长的位置啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0006F好、好像突然\n'
								'听到了很重大的消息啊……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'哈哈，但现在说这些还为时尚早啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(4)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(11), Text(
								'真想让赛西儿来继承\n'
								'护理师长的位置啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'不过，我还打算\n'
								'再干二十年呢，\n'
								'现在说这些还为时尚早。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(11), Text(
								'真希望在３０２号室住院的\n'
								'盖巴尔先生能早点出院啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'护理师们都有各自的工作在身，\n'
								'可没有闲工夫去应付\n'
								'装病的人啊……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(4)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(11), Text(
								'……唉，但既然名义上算是病人，\n'
								'也总不能硬赶他出去啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'只能等他待到腻烦为止吗……{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(11), Text(
								'……呼。\n'
								'统领护理师们\n'
								'其实也很辛苦呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'不过，赛西儿来了之后，\n'
								'多少就轻松了点。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(4)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(11), Text(
								'我让赛西儿\n'
								'负责相当于\n'
								'护士主任的工作。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'她可帮了我大忙呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'菲莉亚还差得远呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'虽然工作时间是不能吃东西，\n'
						'但也不用那么认真地\n'
						'等待午休吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'完全可以在走路时，或者趁我不注意时，\n'
						'三口两口把东西吃掉啊！\n'
						'这点胆量还是该有的嘛。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(11), Text(
								'赛西儿去小滴的\n'
								'病房了哦。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'……小滴这孩子的情况也很难办呢。\n'
								'大概因为母亲去世得早，\n'
								'所以态度总是很老成。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'我倒是觉得，她可以\n'
								'再多一点孩子气的。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(4)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(11), Text(
								'小滴她\n'
								'大概是因为母亲去世得早，\n'
								'所以态度总是很老成。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'我倒是觉得，她可以\n'
								'再多一点孩子气的。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(11), Text(
								'你问我？\n'
								'昨天当然也出勤了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'病人可是等不得的嘛。\n'
								'我们基本上是没有休假的。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(4)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(11), Text(
								'为了预防突然有患者被送来，\n'
								'医院是不能休息的呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'约亚西姆医生有偷懒的习惯，\n'
								'真是令人伤脑筋呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
					Insn('TEXT_TALK', Char(11), Text(
						'在听说赛西儿是那个伊莉雅丄普拉提耶\n'
						'的朋友之后，女孩子们好像\n'
						'都兴奋不已呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'真是的，多少也学学\n'
						'赛西儿努力工作的样子吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(11), Text(
								'彩虹剧团的公演传单\n'
								'也发到医院来了呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'我年轻的时候，\n'
								'伊莉雅丄普拉提耶还没有加入彩虹剧团，\n'
								'剧团也没有现在这么有名。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'现在彩虹已经成为名震克洛斯贝尔的\n'
								'实力派剧团……\n'
								'感觉他们在成功之路上真是越走越远了呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(4)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(11), Text(
								'彩虹剧团的表演……\n'
								'我年轻的时候也经常去看呢。\n'
								'啊，好怀念呢……{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(797)), Insn('END')]), [
							Insn('TEXT_TALK', Char(11), Text(
								'话说回来……\n'
								'那个小缇欧\n'
								'竟然都长得这么大了啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'今天已经要回去了吧？\n'
								'有时间再来吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('TEXT_TALK', Char(11), Text(
								'多亏你们，\n'
								'应该不会再发生\n'
								'魔兽侵害了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'请让我代替工作人员和病人们\n'
								'向你们道声谢吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(797)), Insn('END')]), [
							Insn('IF', [
								(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
									Insn('TEXT_TALK', Char(11), Text(
										'只要是见过一次的病人，\n'
										'我就一定不会忘记……\n'
										'哎呀，但这次真是差点没认出来啊。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(11), Text(
										'缇欧，下次再来哦。\n'
										'要是有机会的话，\n'
										'再一起慢慢聊吧。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('FLAG_SET', Flag(4)),
								]),
								(None, [
									Insn('TEXT_TALK', Char(11), Text(
										'对了对了，赛西儿\n'
										'就在三楼最里面的病房哦。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(11), Text(
										'那里住的是个情况特殊，\n'
										'但是非常乖的好孩子。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('TEXT_TALK', Char(11), Text(
										'方便的话，希望\n'
										'你们也能去看看她。{wait}'
									)),
									Insn('TEXT_WAIT'),
								]),
							]),
						]),
						(None, [
							Insn('TEXT_TALK', Char(11), Text(
								'啊，抱歉哦。\n'
								'我现在正在记帐，\n'
								'腾不出手来。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'不好意思，要是有事的话，\n'
								'能不能去问外面的菲莉亚？{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(11), Text(
								'哎呀，赛西儿。\n'
								'是在给客人带路吗？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(310), Text(
								'#1300F是的，其实……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_SET_NAME', Translate('')),
							Insn('TEXT_MESSAGE', Char(255), Text(
								'{color 5}赛西儿向护理师长说明了事由。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'原来如此，既然是这样，\n'
								'你就给他们带路吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'你们是那个什么支援课的吧？\n'
								'调查就拜托你们了哦。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0005F是、是的。\n'
								'（好有魄力的人啊……）{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(259), Text(
								'#0208F………………………………{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(4)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(11), Text(
								'要是真的有魔兽出没，\n'
								'情况可就严重了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(11), Text(
								'你们几位，\n'
								'可要努力调查哦。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
				(None, []),
			]),
			Insn('TEXT_END', Char(11)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 2))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'唉～这孩子\n'
						'真是让人难以理解啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我发现，拜托希蓉办事\n'
						'根本就是个错误的决定……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我们医院使用的床单\n'
						'是从贸易商哈罗德先生那里购买的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'之前拜托希蓉写了订单……\n'
						'明明说要订五十张的，\n'
						'但她竟然订了五百张。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'五百张啊，五百张！\n'
						'幸好哈罗德先生发现\n'
						'情况不对，马上告诉了我……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但希蓉她真是让人头痛啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'如果贸易商不是哈罗德先生，\n'
						'肯定就会强迫我们买下\n'
						'五百张床单吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真是的，希蓉虽然爱犯迷糊，\n'
						'运气倒是很强……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'其实，那条缎带\n'
						'是希蓉怂恿我买的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'希蓉真是的，\n'
						'到底要怎样捉弄我\n'
						'才会甘心啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 1))), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'不用将缎带白白扔掉，\n'
						'真是太好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这种长度的话，\n'
						'应该可以用来包装哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'请加油继续收集材料吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('CALL', Function((1, 49))),
				]),
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……希蓉那家伙，最近才刚安分了没多久，\n'
						'结果就又闯祸了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'她竟然把刚从雷米菲利亚\n'
						'送来的输血用血液包\n'
						'放进了家庭用的冷柜！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我毫不知情地打开时，\n'
						'真是吓得连心脏都要跳出来了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'希蓉的那些失误，\n'
						'可不是一般形容为『天然呆』的\n'
						'那种可爱小错误。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'竟然把输血用的血液包\n'
						'放进家庭用的冷柜保存……\n'
						'这根本就是恐怖分子啊，恐怖分子。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'希蓉那家伙……\n'
						'竟然擅自把我的\n'
						'居家服拿到别处去了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'没了那个，我在房间里\n'
						'也只能穿着护士服……\n'
						'我得赶快抓住希蓉，好好盘问一番才行。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'希蓉那家伙……跑到哪里去了？\n'
						'快把我的衣服还回来～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 2))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'小滴也是，\n'
						'米海尔也是……\n'
						'虽然只是小孩子，但还真是坚强呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((2, 9))),
				]),
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……唔唔……\n'
						'我总感觉，希蓉那家伙\n'
						'好像又在哪里做什么奇怪的事了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……真讨厌啊。\n'
						'相处的时间一长，\n'
						'就会有种奇怪的直觉。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'唉……就算是希蓉，\n'
						'量体温这种小事总该做得来吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'保险起见，待会还是去看看情况吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我的同事希蓉是个冒失鬼，\n'
						'而且是非同寻常的冒失。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'像使用医疗器具时出现失误，险些引发医疗事故啦，\n'
						'还有把危险的药品洒在地上之类的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'只是，在酿成大错之前，\n'
						'她周围的人都会努力补救，\n'
						'所以才能一直将受害人数保持为零。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'唉，她要是能有赛西儿前辈\n'
						'的一个小指头尖可靠就好了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'希蓉的冒失程度可是非同寻常的。\n'
						'至今为止居然都没有受害者出现，\n'
						'真是太不可思议了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'唉，她要是能有赛西儿前辈\n'
						'的一个小指头尖可靠就好了……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'呃啊～太慢了！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'希蓉那家伙，\n'
						'不过就是晒个床单而已，\n'
						'到底要花多长时间啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'啊啊，我总有种不祥的预感……\n'
						'感觉好不容易洗干净的\n'
						'床单又要被弄脏了！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'希蓉那家伙……\n'
						'不会把洗好的床单又弄脏了吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(796)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'希蓉那家伙，\n'
				'有没有向盖巴尔议员\n'
				'好好道歉啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'那孩子实在是太冒失了，\n'
				'出了什么问题都不稀奇呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎，赛西儿前辈？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯～我想她应该\n'
				'还没回护理站……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'是不是直接\n'
				'去做其它工作了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 2))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'希蓉真是的，\n'
						'总是会犯些\n'
						'不小的失误。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'可不知为何，在病人之中反倒很受欢迎……\n'
						'真是莫名其妙啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][8] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1125)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'#1302F哎呀，罗伊德。\n'
						'这么快就开始工作了呀。{wait}'
						'{page}'
						'#1309F呵呵……\n'
						'大家都过了个有意义的假日吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0102F是呀……\n'
						'好久都没有回过家了，总算回去待了一天。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0202F……嗯，算是稍微清闲了一下呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0306F唉，不过只有一天，\n'
						'这假期也太短了啊。{wait}'
						'{page}'
						'#0300F其实还想和赛西儿小姐\n'
						'一起去玩呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0004F（嗯～虽然发生了不少事，\n'
						'\u3000但那天还算是充实吧……？）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1125)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'#1304F我昨天度过了一个很有意义\n'
						'的假日呢，伊莉雅还把\n'
						'莉夏小姐介绍给我了……{wait}'
						'{page}'
						'#1302F对了对了，伊莉雅还说，\n'
						'原本应该也邀请罗伊德来的，\n'
						'你没来，她觉得很遗憾呢。{wait}'
						'{page}'
						'#1309F呵呵，罗伊德还真受欢迎呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0012F我怎么觉得自己只是\n'
						'被她当成了玩具呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((2, 10))),
				]),
				(Expr([Insn('FLAG', Flag(1124)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'#1300F啊，罗伊德。\n'
						'来得正好。{wait}'
						'{page}'
						'其实呢，伊莉雅\n'
						'给了我两张下个月的\n'
						'彩虹剧团公演门票。{wait}'
						'{page}'
						'#1309F要是行程有空的话，\n'
						'要不要一起去呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0009F好啊，太感谢了！\n'
						'真是求之不得呢。{wait}'
						'{page}'
						'#0004F虽然工作很忙，\n'
						'不知道能否抽出时间……\n'
						'但真想去看看啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'#1309F呵呵，明白了。\n'
						'那我就帮你把票留着了哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0004F（从那排练的情景来看……\n'
						'\u3000正式演出时一定会更加精彩吧。\n'
						'\u3000……………………嗯？）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0211F（瞪…………）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0111F（竟然在工作中敲定了约会呢，\n'
						'\u3000……真是好大的派头。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0301F（这个混蛋弟弟……\n'
						'\u3000为什么只有你……！！）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F（呜……大家的视线好锐利……！）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1124)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'#1300F彩虹剧团的公演……\n'
						'真希望能一起去看啊。{wait}'
						'{page}'
						'#1309F呵呵，期待你能请到假哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0011F是、是啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0211F（瞪……）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(13), Text(
						'#1305F哎呀，罗伊德，忘了什么东西吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F不，倒不是\n'
						'因为这个……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(13), Text(
						'#1305F啊，难不成……\n'
						'你是来向我汇报的吗！？{wait}'
						'{page}'
						'#1309F艾莉、缇欧\n'
						'和兰迪……{wait}'
						'{page}'
						'最后，你决定\n'
						'要和谁交往了？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F……也不是为了这个啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(13), Text(
						'#1300F呵呵，开个玩笑啦。{wait}'
						'{page}'
						'要是再有什么事的话……\n'
						'不，就算没什么事，\n'
						'也可以再来找我哦。{wait}'
						'{page}'
						'#1304F……那么，\n'
						'我还要去给小滴\n'
						'送晚餐才行呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][9] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 0, 0),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然只是个小手术，\n'
				'但也不可轻视哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……要安心静养哦，\n'
				'知道了吗。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'那位病人……\n'
				'似乎也没有\n'
				'乱发脾气的表现。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……总之，看起来像是\n'
				'讲道理的人。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'今天早上，有几名伤患被送到了医院。\n'
						'据说他们都隶属于一个名为『黑月』的组织。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'然后，有一个人恢复到可以\n'
						'开口说话了，就被转移到这边来了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'可是，那种伤势……\n'
						'明显不是普通人会受的伤……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真是些可疑的人啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'今早入院的那些\n'
						'隶属于黑月的成员……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'除了转移到这个病房的人以外，\n'
						'都还需要继续静养。\n'
						'他们应该睡在ＩＣＵ病房吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过……还真是些可疑的人啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'刚才我给小滴\n'
						'诊察过了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……以她的病情来说，\n'
						'凭现在的医疗技术，很难完全治愈。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'外科、内科、神经科……\n'
						'各个领域的问题错综复杂，相互干涉，\n'
						'阻碍了治疗的进行。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'因为还没有完全失明，\n'
						'所以还有极小的治愈可能……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(254), 0, 2000, (24, 27, 250, 0)),
					Insn('SLEEP', 2000),
					Insn('EMOTE_STOP', Char(254)),
					Insn('TEXT_TALK', Char(254), Text(
						'……我真是的，\n'
						'竟然将病人的情况说了出来，\n'
						'真是太轻率了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……刚才的话请你们忘了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……我真是的，\n'
						'竟然将病人的情况说了出来，\n'
						'真是太轻率了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……刚才的话，请你们忘掉吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'……我可没兴趣给健康的人看病哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我现在要去查房。\n'
				'趁着还没打扰到其他病人，\n'
				'快点回去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'今天是纪念庆典第二天了吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'太过兴奋，注意不到周围的时候\n'
						'便有受伤的危险。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'希望明天不要\n'
						'再有克洛斯贝尔市的\n'
						'不良分子成员被送到这里。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'太过兴奋，注意不到周围的时候\n'
						'便有受伤的危险，\n'
						'你们也多加小心吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'这次虽然只是个小手术……\n'
				'但我绝对不会松懈大意的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'身为外科医生，\n'
				'这是在面对手术时\n'
				'最低限度的原则。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 180, 0),
			Insn('TEXT_TALK', Char(254), Text(
				'会觉得外科手术\n'
				'很可怕也是难免的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过，这次手术的危险度\n'
				'可以说是相当低。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'太过担心的话对身体也不好。\n'
				'今天就请放宽心，\n'
				'早点休息吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'接下来要去２０２号室查房。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你不是住院患者吧？\n'
				'趁天还没黑，赶快回家吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(14)), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((1, 12))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'从早上一直坚持到现在……\n'
				'差不多也该撤退了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……话说回来，黑月似乎是\n'
				'相当难缠的对手啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我是第一次跟他们交涉，\n'
				'感觉就连底层的成员\n'
				'也都很有组织纪律性。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(15)), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((1, 12))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'可恶，搜查一课的那些家伙，\n'
				'我早就看他们不顺眼了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'平时总是理直气壮地\n'
				'强行接管我们处理的事件，\n'
				'到这种时候却又把人呼来唤去……！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('0x4B', Char(15), -1),
	Insn('0x4B', Char(16), -1),
	Insn('CHAR_WATCH', Char(15), Char(0), 0),
	Insn('CHAR_WATCH', Char(16), Char(0), 0),
	Insn('TEXT_TALK', Char(15), Text(
		'啧，那就是黑月吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'说话都统一口径，\n'
		'真是不讨人喜欢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(0), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(1), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(2), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(3), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#0105F警部，你们是来找黑月成员们\n'
		'询问案情的吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'是受搜查一课的请求才来的～\n'
		'他们要我们去找住院的成员们做笔录。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'但那些人的口风实在太紧，\n'
		'根本不可能露出破绽的～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(16), Text(
		'可恶，搜查一课的混蛋们。\n'
		'肯定是明知如此，才把工作推给我们的～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0011F哈哈……\n'
		'（大概只是被派来做个\n'
		'形式上的笔录吧。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0306F（搜查二课也够辛苦啊。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(15), 270, 0),
	Insn('CHAR_ROTATE', Char(16), 90, 0),
	Insn('0x4C', Char(15), -1),
	Insn('0x4C', Char(16), -1),
	Insn('FLAG_SET', Flag(14)),
	Insn('FLAG_SET', Flag(15)),
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
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'都傍晚了吗……\n'
				'一直睡着，就感觉一天过得很快。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'虽说还在实习，\n'
				'但医生竟然会受伤住院。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'这就是所谓的勤于谋人、疏于谋己吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'从刚才起就一直吵吵嚷嚷的。\n'
		'难道就不能安静点吗。{wait}'
	)),
	Insn('TEXT_WAIT'),
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
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'住院生活真是闲啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'那位美女护理师\n'
				'可没来这里哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'什、什么啊……\n'
						'刚才那个戴眼镜的医生。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'本以为他要谈谈治疗的事情，\n'
						'没想到一开口就是虐待啊被虐啊什么的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(310), Text(
						'#1306F对不起，\n'
						'请不要太放在心上。\n'
						'约亚西姆医生就是那种人……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F……就这么纵容他也不太好吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(8)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'刚才那位戴眼镜的医生……\n'
						'怎么看都不像是个医生啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但说到副教授，那就是地位仅次于\n'
						'教授的人了，应该很了不起吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][16] = [
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
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'那位老婆婆，好像很幸福呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯～我也要好好加油，\n'
				'直到痊愈出院。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'那位老婆婆……\n'
				'好像有孙女来看她了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'她总是在抱怨，说没人来看她，\n'
				'但现在不是挺好的吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'唉，那位老婆婆……\n'
				'总是在抱怨\n'
				'没人来看她。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'真是的……\n'
				'连我都觉得郁闷起来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][17] = [
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
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'孙女来看我了，\n'
				'不过我让她趁着天还没黑，快点回去。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'唔……多亏了她，总算是精神点了。\n'
				'我得加油啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 19))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'孙女自己一个人\n'
						'特意过来看我……\n'
						'没有比这更令人开心的事啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'她说我的儿子和儿媳\n'
						'都相当忙碌……\n'
						'真为自己之前那迁怒于他们的想法感到羞愧啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(785)), Insn('END')]), [
							Insn('CALL', Function((1, 18))),
						]),
						(None, [
							Insn('TEXT_TALK', Char(254), Text(
								'住院之后到现在，\n'
								'没有一个家人来看我……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'唉，好想念孙女啊……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(9)),
						]),
					]),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'唉……好想念孙女啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('CHAR_ROTATE', Char(48), 180, 0),
	Insn('CHAR_SET_FRAME', Char(21), 2),
	Insn('0x4B', Char(48), -1),
	Insn('TEXT_TALK', Char(21), Text(
		'住院之后到现在，\n'
		'没有一个家人来看我……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'唉，好想念孙女啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'我可不管儿子儿媳忙不忙，\n'
		'他们也太不关心人了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(48), Text(
		'#2406F是啊……\n'
		'嗯，真是可悲可叹啊。{wait}'
		'{page}'
		'#2400F不过，既然您这么有精神，\n'
		'大概用不了多久就能出院吧。\n'
		'很快就能见到孙女啦。{wait}'
		'{page}'
		'#2409F对了，吃不吃点心啊？\n'
		'可以让人镇定下来哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'唉，会对我这么体贴的人，\n'
		'也只有医生啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F（真、真是位奇怪的医生啊……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(21), 0),
	Insn('0x4C', Char(48), -1),
	Insn('FLAG_SET', Flag(9)),
	Insn('FLAG_SET', Flag(13)),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('CHAR_WATCH', Char(22), Char(21), 0),
	Insn('CHAR_SET_FRAME', Char(21), 2),
	Insn('0x4B', Char(22), -1),
	Insn('TEXT_TALK', Char(22), Text(
		'奶奶，听我说！\n'
		'我还是第一次\n'
		'一个人坐定期巴士哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'比和爸爸妈妈一起乘坐\n'
		'还要让人兴奋，好开心啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'是吗是吗，真了不起呀。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'来，把约亚西姆医生刚才\n'
		'送我的糖球给你吃吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'哇～谢谢！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(21), 0),
	Insn('0x4C', Char(22), -1),
	Insn('FLAG_SET', Flag(9)),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((1, 19))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'奶奶比我想像的还有精神，\n'
				'真是太好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][21] = [
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
	Insn('TEXT_TALK', Char(254), Text(
		'虽然膝盖还有些痛，\n'
		'但看今天的情况，离出院也不远了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'呵呵，真令人期待啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][22] = [
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
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今、今天终于要动手术了，\n'
				'主刀医生似乎是\n'
				'这位贝尔达因医生。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……唉，真是好紧张啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'唉……好郁闷啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然医生说是个小手术，\n'
				'叫我不要担心……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯咕……嗯咕……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呼啊啊，嗯咕……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯咕……嗯咕……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][24] = [
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
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'这家医院待着很舒服，\n'
				'住下就不想走了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'医生和护理师们都很温柔……\n'
				'呵呵，要是不想出院了，\n'
				'可该怎么办呀。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'医院的床睡着很舒服呢。\n'
				'即使一声不吭，也会有饭菜端过来，\n'
				'有多少年没享受过这种生活了啊？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][25] = [
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
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 3))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'到底要怎么做\n'
						'才能折断体温计啊……？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 3))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……面对这位冒失的护理师小姐，\n'
						'真是有几条命都不够赔啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过……看她那么可爱，也就算了吧。{wait}'
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

data['code'][26] = [
	Insn('EXPR_CHAR_ATTR', Char(0), 5, Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(28), 5, Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('SET'), Insn('END')])),
	Insn('TEXT_START', Char(28)),
	Insn('CHAR_FLAG1_UNSET', Char(28), 16),
	Insn('CHAR_WATCH', Char(28), Char(0), 0),
	Insn('EXPR_CHAR_ATTR', Char(28), 4, Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 360), Insn('ADD'), Insn('CONST', 360), Insn('MOD'), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(28), 4, Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 360), Insn('ADD'), Insn('CHAR_ATTR', Char(28), 5), Insn('SUB'), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(28), 5, Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 180), Insn('DIV'), Insn('SET'), Insn('END')])),
	Insn('IF', [
		(Expr([Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 45), Insn('LE'), Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 315), Insn('GE'), Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 405), Insn('LE'), Insn('BOOL_AND'), Insn('OR'), Insn('CHAR_ATTR', Char(28), 4), Insn('CONST', 675), Insn('GE'), Insn('OR'), Insn('END')]), []),
		(Expr([Insn('CHAR_ATTR', Char(28), 5), Insn('CONST', 1), Insn('LT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(28), 8, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
		]),
		(Expr([Insn('CHAR_ATTR', Char(28), 5), Insn('CONST', 2), Insn('GT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(28), 8, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
		]),
		(None, [
			Insn('EXPR_CHAR_ATTR', Char(28), 8, Expr([Insn('CHAR_ATTR', Char(28), 5), Insn('SET'), Insn('END')])),
		]),
	]),
	Insn('EXPR_CHAR_ATTR', Char(28), 4, Expr([Insn('CHAR_ATTR', Char(0), 5), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(0), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(28), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(28), 16),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(28), Text(
				'自从我藏起来的写真杂志被发现以后，\n'
				'感觉护理师们的眼神\n'
				'都变得冷淡起来了……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(28), Text(
				'都怪对面那个大叔，\n'
				'硬把那种杂志塞给我啦……！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(28), Text(
				'对面那个大叔昨天\n'
				'给我的写真杂志……\n'
				'在量体温的时候被发现了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(28), Text(
				'我真是从来都没有那么丢人过……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(28), Text(
				'（……这个人，真的是\n'
				'\u3000很厉害的医生吗……？）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(28), Text(
				'唉～唉……\n'
				'要是没受这种伤的话，\n'
				'现在应该正在享受庆典了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(28), 0),
	Insn('TEXT_END', Char(28)),
	Insn('RETURN'),
]

data['code'][27] = [
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
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'自从把写真杂志送给对面的孩子\n'
				'之后，他就经常瞪着我。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯～莫非是还想要吗？\n'
				'没办法，作为友好的证明，\n'
				'再送他一本我珍藏的好杂志吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我昨天送了本写真杂志\n'
				'给对面的孩子。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'看他量体温时\n'
				'那慌张的样子，\n'
				'似乎已经精神起来了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'大叔我在跟人交往的时候，\n'
				'都会赠送自己收藏的写真杂志，\n'
				'当作见面礼呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'约亚西姆医生\n'
				'很爽快地就收下了哦。\n'
				'哎呀，真是个容易亲近的人。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'对面床位的孩子，\n'
				'怎么无精打采的啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'没办法，偷偷送他一本\n'
				'大叔我秘藏的\n'
				'写真杂志吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][28] = [
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
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我调查了一下今天来\n'
				'查房的医生……\n'
				'凯瑞教授是谁啊？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我想让约亚西姆医生\n'
				'来帮我诊察呀！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(13)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 47))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'约亚西姆医生\n'
						'就是爱害羞，真是的㈱{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'约亚西姆医生好像还是单身呢～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，让我来\n'
				'填补医生\n'
				'心中的空虚吧㈱{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啊啊，约亚西姆医生\n'
				'怎么还不来查房呢㈱{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'那种超然于世的感觉……\n'
				'是阿姨我最喜欢的类型呀～㈱{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][29] = [
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
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天预定有外科的医生\n'
				'来查房的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'希望我的腰腿好些了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀呀，好可爱的医生。\n'
				'一定很受欢迎吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'护理师们对我\n'
				'真的很好。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，虽然也有几个奇怪的孩子……\n'
				'但大家都是很体贴人的好孩子。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'这家医院真是个\n'
				'舒服的好地方呀。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'在腰腿感觉好些之前，\n'
				'就在这里享受一阵子吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][30] = [
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
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(10)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'刚才量体温的时候，\n'
						'护理师小姐发现了\n'
						'我的写真杂志。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然她只是对我微笑了一下，\n'
						'但这反而更加让人难堪……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(10)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'唉，果然不该收下\n'
						'旁边那个大叔给的\n'
						'写真杂志啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嘿嘿……\n'
				'这家医院的护理师小姐真漂亮啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'比起写真杂志里的美女，\n'
				'还是现实中的美女更好啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][31] = [
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
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'其实我已经快出院了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'要和同病房中意气相投的朋友分别，真是很失落……\n'
				'但这也是没办法的事啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'好……作为饯别礼，就把我\n'
				'秘藏的写真杂志送给旁边的孩子吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'作为友好的证明，\n'
				'我送给邻床的孩子\n'
				'好几本写真杂志。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然查房的时候差点被发现……\n'
				'啊哈哈，真是刺激啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][32] = [
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
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'刚才有个孩子从走廊跑过去了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'真是的，父母是怎么教育的啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'拉格教授上周给我看过病了，\n'
				'似乎在本周之内就可以出院了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'乱吃东西果然很恐怖啊，\n'
				'你们也小心点吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][33] = [
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
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎……你们去见过约亚西姆医生了？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'太让人生气了～！\n'
				'有空见这些孩子的话，\n'
				'为什么不来查房啊！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我还在奇怪为什么约亚西姆医生\n'
				'最近不来查房了呢……\n'
				'原来不知不觉间，主治医师竟然被换了！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'太让人生气了～！\n'
				'约亚西姆医生太坏了！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][34] = [
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
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(11)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 36))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'算、算啦，总而言之，\n'
						'你能来看我，我很开心。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(11)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'昨天我的朋友联系过我，\n'
						'说是要来探望，\n'
						'结果又没来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……真令人担心啊。\n'
						'那家伙是个令人\n'
						'难以置信的路痴呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(11)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'那家伙真的能顺利\n'
						'找到病房吗……？{wait}'
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

data['code'][35] = [
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
		(Expr([Insn('FLAG', Flag(11)), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((1, 36))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀，真是累死人了。\n'
				'不知道病房在哪里，让我找得好辛苦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][36] = [
	Insn('CHAR_WATCH', Char(45), Char(36), 0),
	Insn('CHAR_SET_FRAME', Char(36), 1),
	Insn('0x4B', Char(45), -1),
	Insn('TEXT_TALK', Char(45), Text(
		'哟，\n'
		'住院生活还算充实吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(36), Text(
		'哈哈，你竟然找到路了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(36), Text(
		'话说，\n'
		'进行导力通讯的时候，\n'
		'你不是说准备昨天来吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(45), Text(
		'我是来医院了，\n'
		'但是一直找不到病房啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(45), Text(
		'无奈之下，只好在\n'
		'住宿设施里住了一晚。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(36), Text(
		'你果然还是个路痴啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(11)),
	Insn('CHAR_SET_FRAME', Char(36), 0),
	Insn('0x4C', Char(45), -1),
	Insn('RETURN'),
]

data['code'][37] = [
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
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'昨天住院的人，\n'
				'今天早上不知何时出院了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'那家伙肯定是做了什么\n'
				'亏心事吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'那个新来的……\n'
				'好像在斗殴中受了重伤……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'跟那种人同病房，不要紧吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'拉格教授之前\n'
				'来查过房了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'能让那么厉害的医生给我看病，\n'
				'真是太幸运了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][38] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'唔……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呼…………呼…………{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][39] = [
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
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'昨天我女朋友来探病，\n'
				'真是丢脸丢大了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'真是的……\n'
				'多难为情啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'笨……不要为了专门\n'
				'说这种话来探病呀～！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'才没给别人添麻烦呢～\n'
				'……真的啦！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我女朋友今天要来探病。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我都跟她说不用来了……\n'
				'多难为情啊～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啧，医院这种地方\n'
				'真是无聊到让人不耐烦啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'赶快让我出院吧～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][40] = [
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
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('CHAR_WATCH', Char(254), Char(39), 0),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，我放心了。\n'
				'你看起来似乎很有精神嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'没给大家添麻烦吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][41] = [
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
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'同室的老爷爷\n'
				'跟护理师小姐出去散步了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，真好呢。\n'
				'我要不要也拜托\n'
				'护理师小姐带我去散步呢～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，病房里的人\n'
				'都很有个性，挺有趣的嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀哎呀，这么多人来病房……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'是来探望什么人吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我在家都是一个人住，\n'
				'所以觉得这种集体生活很开心呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'大家看上去都很不错，\n'
				'可要和他们友好相处啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][42] = [
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
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'明天我儿子和婆婆\n'
				'会来看我。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'婆婆这次\n'
				'为我做了很多，\n'
				'我得好好道谢才行。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'听说这家医院的\n'
				'餐点水准也很高呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，好期待啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我婆婆发来联系说，\n'
				'下次会带我儿子来看我。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哇哇～怎么办？\n'
				'总觉得很过意不去啊……！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我来住院时，\n'
				'把儿子交给婆婆带了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我们之间的婆媳关系本来并不算好，\n'
				'但没想到在关键时刻也能得到她的帮助呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][43] = [
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
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我觉得肚子莫名地痛了起来，\n'
				'结果医生说是盲肠炎……什么的，\n'
				'突然就让我住院了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'啊～讨厌！\n'
				'好想早点回家～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][44] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呜～感觉肚子\n'
				'又在一阵一阵地刺痛……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然手术已经做完了，\n'
				'但还是要再休养一阵才行吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'……我早上刚做了手术，所以要睡觉。\n'
				'能不能不要吵我？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呜……我早上\n'
				'做了治疗盲肠炎的手术。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'好痛……什么也不想干……\n'
				'好困……肚子饿了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][45] = [
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
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(254), 0),
			Insn('TEXT_TALK', Char(254), Text(
				'（……待太久的话，\n'
				'\u3000会给周围的人带来不安，\n'
				'\u3000进而对公司不利呢。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'（等同伴们明天醒了以后，\n'
				'\u3000就带着大家立刻出院吧。）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(12)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'哎呀呀，警察也真是令人伤脑筋啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'就算再怎么刨根问底，\n'
						'我也没有什么\n'
						'可以回答的啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'而且，再怎么说，我也算是住院的人，\n'
						'就不能稍微体谅一点吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(12)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'一起被送来的同伴们\n'
						'似乎还在ＩＣＵ室……\n'
						'听说明天就会醒来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，不愧是著名的\n'
						'乌尔斯拉医院呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][46] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(13)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 47))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(48), Text(
						'#2406F呼……难得受欢迎一次，却这么累人啊。\n'
						'我还想尽快查完房，\n'
						'早点回去呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(13)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(48), Text(
						'#2400F纪念庆典玩得开心吗？{wait}'
						'{page}'
						'#2409F我昨天也找到了新的钓场，\n'
						'稍后正打算去看看呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F那个……您的工作呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(48), Text(
						'#2409F哈哈哈……\n'
						'请不要告诉其他医生哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(0), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 50),
					Insn('EMOTE', Char(1), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 50),
					Insn('EMOTE', Char(2), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 50),
					Insn('EMOTE', Char(3), 0, 2000, (16, 19, 250, 1)),
					Insn('SOUND_PLAY', 23, 0, 0, 100),
					Insn('SLEEP', 1000),
					Insn('FLAG_SET', Flag(13)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(48), Text(
						'#2405F啊，话说在先，\n'
						'我已经把今天该做的事情\n'
						'全部认真完成了哦。{wait}'
						'{page}'
						'#2400F这可是我自己挤出来的休息时间，\n'
						'没理由被人教训吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F（既然如此，那就堂堂正正地走嘛……）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(13)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 18))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(48), Text(
						'#2403F俗话说，病由心生啊。\n'
						'既然这么有精神，应该很快就能出院了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(310), Text(
						'#1306F……请您说点像是医生\n'
						'该说的话吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][47] = [
	Insn('CHAR_WATCH', Char(48), Char(30), 0),
	Insn('CHAR_SET_FRAME', Char(30), 2),
	Insn('0x4B', Char(48), -1),
	Insn('TEXT_TALK', Char(30), Text(
		'约亚西姆医生\n'
		'有没有女朋友呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(48), Text(
		'#2409F哈哈哈，不管怎么说，\n'
		'我也是以单身贵族自居的。\n'
		'女性大多都觉得我难以接近，所以不怎么受欢迎呢。{wait}'
		'{page}'
		'#2400F这个暂且不提，\n'
		'还是先来诊察吧──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(30), Text(
		'哎呀，是这样吗？\n'
		'好可惜呀～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(30), Text(
		'呵呵，既丄然丄如丄此……\n'
		'那我就来当候补吧㈱{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(48), Text(
		'#2406F呃，这个……\n'
		'哈哈哈，伤脑筋啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(13)),
	Insn('CHAR_SET_FRAME', Char(30), 0),
	Insn('0x4C', Char(48), -1),
	Insn('RETURN'),
]

data['code'][48] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(16)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'作为将来的参考，我正在参观\n'
				'医生们的工作。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'看到他们办事干脆俐落的样子，\n'
				'就知道他们有多优秀呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(16)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'作为将来的参考，我正在参观\n'
				'医生们的工作。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……待太久的话，\n'
				'还是会妨碍到他们吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][49] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (110090, 1000, -5610), 0),
	Insn('CAM_ROTATE', 68, 34, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 20480, 0),
	Insn('CHAR_SET_POS', Char(257), (110500, 0, -6000), 0),
	Insn('CHAR_SET_POS', Char(258), (109200, 0, -6000), 45),
	Insn('CHAR_SET_POS', Char(259), (110500, 0, -7300), 0),
	Insn('CHAR_SET_POS', Char(260), (109200, 0, -7300), 45),
	Insn('CHAR_SET_POS', Char(265), (109200, 0, -4700), 90),
	Insn('CHAR_FLAG1_UNSET', Char(4), 128),
	Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
	Insn('CHAR_WATCH', Char(12), Char(257), 0),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P嗯……那个东西，\n'
		'不然还是退给店里算了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0005F请问……\n'
		'您有什么麻烦吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P嗯？不，\n'
		'倒不算是\n'
		'麻烦啦……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P之前纪念庆典的时候，\n'
		'我去了克洛斯贝尔市，\n'
		'在那里买了一条缎带。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P买的时候觉得\n'
		'很可爱……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P但仔细想想的话，\n'
		'这未免可爱过头了，\n'
		'不太适合我呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0003F（缎带吗……）{wait}'
		'{page}'
		'（用来包装礼物的话，\n'
		'\u3000似乎不错呢。）{wait}'
		'{page}'
		'#0000F那个，有件事想和您商量一下……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P哎，什么？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}罗伊德说明了正在收集\n'
		'礼物材料的事由。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0000F因此……\n'
		'如果您愿意的话，\n'
		'能不能将那条缎带让给我们呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P哦，小滴她……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0304F我们绝对不会用来做\n'
		'一些不正经的事情，请不必担心。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#6P#0506F兰、兰迪前辈……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0200F……你说这种话，\n'
		'反而更容易被怀疑。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P哈哈……嗯，好吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P既然如此，\n'
		'就请有效地利用它吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'收下了{item 836}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 836, 1),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0100F不好意思，\n'
		'是我们强人所难了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P不会不会，没关系啦。物尽其用最好，\n'
		'给你们的话，也就不用白白扔掉这条缎带了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P请加油继续收集材料吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0000F嗯，非常感谢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('QUEST', 44, Insn('TASK_SET', 1)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 0))), Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 2))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 4))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 44, Insn('TASK_SET', 5)),
			Insn('TEXT_TALK', Char(257), Text(
				'#12P#0000F（制作礼物的材料收集齐了，\n'
				'\u3000包装用的盒子与缎带也找到了……）{wait}'
				'{page}'
				'（好，差不多该拿去\n'
				'\u3000给小滴了。）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (110500, 1000, -6000), 0),
	Insn('CAM_ROTATE', 45, 28, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 22000, 0),
	Insn('CHAR_ROTATE', Char(12), 90, 0),
	Insn('CHAR_SET_POS', Char(0), (110500, 0, -6000), 0),
	Insn('CHAR_SET_POS', Char(1), (110500, 0, -6000), 0),
	Insn('CHAR_SET_POS', Char(2), (110500, 0, -6000), 0),
	Insn('CHAR_SET_POS', Char(3), (110500, 0, -6000), 0),
	Insn('CHAR_FLAG1_SET', Char(4), 128),
	Insn('CHAR_FLAG2_SET', Char(4), 32768),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][50] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('END')]), [
			Insn('TEXT_TALK', Char(10), Text(
				'果然被我料中了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'主任是踏上寻书之旅了吧～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 7))), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('0x4B', Char(10), -1),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CAM_OFFSET', (22780, 1510, -1100), 0),
			Insn('CAM_ROTATE', 45, 23, 0, 0),
			Insn('0x6E', 440, 0),
			Insn('CAM_DISTANCE', 22000, 0),
			Insn('CHAR_ROTATE', Char(10), 225, 0),
			Insn('CHAR_SET_POS', Char(257), (22490, 0, -730), 45),
			Insn('CHAR_SET_POS', Char(258), (23210, 0, -1450), 45),
			Insn('CHAR_SET_POS', Char(259), (21620, 0, -1600), 45),
			Insn('CHAR_SET_POS', Char(260), (22320, 0, -2340), 45),
			Insn('CAM_DISTANCE', 20000, 1000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(10), Text(
				'啊，罗伊德先生。\n'
				'你找到亚苏拉主任了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F不，还没。\n'
				'所以现在正在收集情报……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0300F如果有什么线索\n'
				'可以告诉我们吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'这个嘛～\n'
				'线索、线索……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(10), 0, 2000, (24, 27, 250, 0)),
			Insn('SLEEP', 1000),
			Insn('EMOTE_STOP', Char(10)),
			Insn('SLEEP', 600),
			Insn('EMOTE', Char(10), 0, 2000, (34, 36, 250, 1)),
			Insn('SOUND_PLAY', 28, 0, 0, 100),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(10), Text(
				'啊，对了！{wait}'
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
				'#0005F你有什么线索吗！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'嗯，之前主任曾这么说过。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'这间医院虽然买了\n'
				'很多最新的机器，\n'
				'但书和资料却少得可怜……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'就算想查资料，\n'
				'光靠这些资源\n'
				'也没办法做研究。{wait}'
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
			Insn('TEXT_TALK', Char(10), Text(
				'所以，我想主任一定是\n'
				'踏上寻书之旅了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F……但这应该跟这次的事\n'
				'没什么太大的关系吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0100F嗯，可能就像你说的。\n'
				'但可能性也不完全为零。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
			Insn('SLEEP', 1000),
			Insn('EMOTE_STOP', Char(257)),
			Insn('TEXT_TALK', Char(257), Text(
				'#0003F……书吗。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0105F罗伊德，怎么了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F不，没什么。\n'
				'继续听其他人怎么说吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_POS', Char(257), (22710, 0, -1250), 45),
			Insn('EVENT_END', 5),
			Insn('0x4C', Char(10), -1),
			Insn('QUEST', 56, Insn('TASK_SET', 7)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(10), Text(
				'主任曾抱怨过\n'
				'医院内的藏书实在太少了～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(10), Text(
				'所以，我想主任一定是\n'
				'踏上寻书之旅了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][51] = [
	Insn('EVENT_BEGIN', 0),
	Insn('0x4B', Char(11), -1),
	Insn('0x4B', Char(13), -1),
	Insn('0x4B', Char(12), -1),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'chr/ch32900', 30),
	Insn('LOAD_CHCP', 'chr/ch32700', 31),
	Insn('CHAR_FLAG1_UNSET', Char(49), 128),
	Insn('CHAR_FLAG1_UNSET', Char(50), 128),
	Insn('CHAR_SET_CHCP', Char(49), 30),
	Insn('CHAR_SET_FRAME', Char(49), 0),
	Insn('CHAR_SET_CHCP', Char(50), 31),
	Insn('CHAR_SET_FRAME', Char(50), 0),
	Insn('CAM_OFFSET', (102270, 1000, 60), 0),
	Insn('CAM_ROTATE', 55, 25, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 19000, 0),
	Insn('CHAR_SET_POS', Char(257), (101750, 0, -1250), 0),
	Insn('CHAR_SET_POS', Char(258), (102950, 0, -1250), 0),
	Insn('CHAR_SET_POS', Char(259), (101750, 0, -2450), 0),
	Insn('CHAR_SET_POS', Char(260), (102950, 0, -2450), 0),
	Insn('CHAR_SET_POS', Char(49), (102350, 0, 200), 0),
	Insn('CHAR_SET_POS', Char(13), (104750, 0, 800), 270),
	Insn('CHAR_SET_POS', Char(12), (104750, 0, -400), 270),
	Insn('CHAR_SET_POS', Char(50), (101750, 0, 1950), 180),
	Insn('CHAR_SET_POS', Char(11), (102950, 0, 1950), 180),
	Insn('CAM_DISTANCE', 17000, 1000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F总之，我们平安找到\n'
		'亚苏拉主任了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(49), Text(
		'啊，呃。\n'
		'我回来了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(13), Char(49), 100),
	Insn('0x98', Char(13), (-300, 0, 0), 2000, 0),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(13), Text(
		'#1303F真是的，亚苏拉主任……！\n'
		'大家都很担心你呢……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(49), Char(12), 500),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(13), Text(
		'#1302F人能平安无事真是太好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(49), 300, 1600, (54, 57, 250, 0)),
	Insn('SOUND_PLAY', 892, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(49)),
	Insn('TEXT_TALK', Char(49), Text(
		'赛西儿小姐……\n'
		'你人真好。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_STOP', 1500),
	Insn('EMOTE', Char(50), 0, 2000, (12, 13, 250, 2)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('CHAR_WATCH', Char(50), Char(49), 500),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(50), Text(
		'在呵呵傻笑之前，\n'
		'你是不是该说些什么啊，\n'
		'亚苏拉？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('BGM_PLAY', b'\x06\x02\x00'),
	Insn('CHAR_WATCH', Char(49), Char(50), 500),
	Insn('EMOTE', Char(49), 0, 2000, (40, 43, 100, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(49)),
	Insn('TEXT_TALK', Char(49), Text(
		'讨、讨厌啦，凯瑞教授。\n'
		'请不要摆出这么可怕的表情嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(49), Text(
		'既然你的学生都平安回来了，\n'
		'就应该要表现出重逢的喜悦\n'
		'或感动的眼泪……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(50), Text(
		'嗯……你说的有道理。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(50), Text(
		'但不知道为什么。\n'
		'我一看到你的脸，\n'
		'就半滴感动的眼泪都流不出来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(50), Text(
		'涌现的只有对你的愤怒\n'
		'和想该怎么对你说教。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(49), Text(
		'这、这样啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(50), Text(
		'那么，你这次在医院里\n'
		'引起了这么大的风波……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(50), Text(
		'欠的这笔帐\n'
		'你打算怎么还呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(49), Text(
		'呃，那个……\n'
		'我、我以后会注意的！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(50), Text(
		'「以后」也太晚了吧，亚苏拉。\n'
		'再怎么说，你这次可是\n'
		'搞到连警察都出动了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(49), Text(
		'就算你这么说……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(50), Text(
		'嗯，看来我得好好跟你\n'
		'聊一下之后的事呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_LOOP', 49, 1, [
		Insn('CHAR_WATCH', Char(254), Char(50), 0),
	]),
	Insn('FORK', 50, 2, [
		Insn('0x98', Char(254), (0, 0, -1600), 1500, 0),
	]),
	Insn('FORK_AWAIT', Char(50), 2),
	Insn('TEXT_TALK', Char(50), Text(
		'我们换个地方说话吧。\n'
		'虽然内容可能会有点长，\n'
		'但应该不会比被浪费掉的时间还久。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_LOOP', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(49), 0),
	]),
	Insn('FORK_LOOP', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(49), 0),
	]),
	Insn('FORK_LOOP', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(49), 0),
	]),
	Insn('FORK_LOOP', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(49), 0),
	]),
	Insn('CHAR_ROTATE', Char(13), 270, 500),
	Insn('FORK_LOOP', 11, 1, [
		Insn('CHAR_WATCH', Char(254), Char(49), 0),
	]),
	Insn('FORK_QUIT', Char(49), 1),
	Insn('CAM_DISTANCE', 16000, 7000),
	Insn('FORK_FUNC', Char(50), 3, Function((1, 52))),
	Insn('TEXT_TALK', Char(49), Text(
		'#20A噫、噫！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x6F', b'\x10'),
	Insn('BGM_STOP', 4000),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(11), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(13), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(12), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('EMOTE_STOP', Char(11)),
	Insn('EMOTE_STOP', Char(13)),
	Insn('EMOTE_STOP', Char(12)),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(259), 1),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('FORK_QUIT', Char(11), 1),
	Insn('SLEEP', 1500),
	Insn('0x1F'),
	Insn('FORK', 11, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('SLEEP', 100),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(11), 300),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(11), 300),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(11), 300),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(11), 300),
	]),
	Insn('FORK', 13, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('FORK', 12, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(13), 1),
	Insn('FORK_AWAIT', Char(12), 1),
	Insn('FORK_AWAIT', Char(11), 1),
	Insn('FORK_AWAIT', Char(50), 3),
	Insn('TEXT_TALK', Char(11), Text(
		'能平安找到我们家\n'
		'那个冒失主任真是太好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 9, 0, 0, 100),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}任务【贪睡医生的搜索委托】{color 0}完成！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('QUEST', 56, Insn('FLAG_UNSET', 16)),
	Insn('TEXT_TALK', Char(11), Text(
		'真的很谢谢你们。\n'
		'这些是谢礼，请收下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'收下了４个{item 510}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', 14, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 510, 4),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F谢谢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(11), Text(
		'接下来就交给我们吧。\n'
		'主任给大家添了这么多麻烦，\n'
		'我们一定会好好算这笔帐的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0203F虽说是自作自受，\n'
		'但我也有点同情她呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0108F看来惩罚是逃不掉了呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0309F如果是在白衣天使的\n'
		'包围下接受盘问的话，\n'
		'我很乐意代替她。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F总之，任务顺利完成了。\n'
		'我们回去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_SET', Char(49), 128),
	Insn('CHAR_FLAG1_SET', Char(50), 128),
	Insn('0x4C', Char(11), -1),
	Insn('0x4C', Char(13), -1),
	Insn('0x4C', Char(12), -1),
	Insn('CHAR_SET_POS', Char(0), (101750, 0, -1250), 0),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][52] = [
	Insn('FORK', 50, 2, [
		Insn('CHAR_ROTATE', Char(254), 270, 500),
	]),
	Insn('FORK', 49, 2, [
		Insn('CHAR_ROTATE', Char(254), 90, 500),
	]),
	Insn('FORK_AWAIT', Char(49), 2),
	Insn('FORK', 50, 2, [
		Insn('0x98', Char(254), (-10000, 0, -700), 1000, 0),
	]),
	Insn('EMOTE', Char(49), 0, 2000, (40, 43, 100, 0)),
	Insn('FORK', 49, 2, [
		Insn('0x98', Char(254), (-10000, 0, -700), 1000, 0),
	]),
	Insn('SLEEP', 3000),
	Insn('FORK', 50, 0, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK', 49, 0, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 0),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('EMOTE_STOP', Char(49)),
	Insn('SLEEP', 1000),
	Insn('RETURN'),
]
