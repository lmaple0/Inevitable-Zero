# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 't1530',
	'name2': 't1530',
	'location': 79,
	'bgm': 123,
	'flags': 8192,
	'includes': [
		't1530',
		't1530_1',
		't1500_1',
		None,
		None,
		None,
	],
	'name3': 't1530_1',
	'labels': [],
	'chcp': [],
	'npcs': [],
	'monsters': [],
	'triggers': [],
	'objects': [],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00O\x00', Function((0, 255)), Function((0, 255))),
	'code': [None]*82,
	'anim': [],
}

data['code'][0] = [
	Insn('CALL', Function((1, 1))),
	Insn('RETURN'),
]

data['code'][1] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(783)), Insn('FLAG', Flag(784)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 9))),
		]),
		(Expr([Insn('FLAG', Flag(1562)), Insn('FLAG', Flag(1563)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 14))),
		]),
		(Expr([Insn('EXEC', Insn('QUEST_GET', 22, Insn('FLAG_GET', 2))), Insn('EXEC', Insn('QUEST_GET', 22, Insn('TASK_GET', 0))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((1, 76))),
		]),
		(None, [
			Insn('TEXT_START', Char(8)),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(8), Text(
								'今天早上，黑月贸易公司的诸位\n'
								'都自行出院了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'明明还没有痊愈呢，\n'
								'只是刚刚能行走，就坚持要……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('IF', [
								(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('NE'), Insn('END')]), [
									Insn('TEXT_TALK', Char(266), Text(
										'#0603F哼……该说不愧是曹的部下吗，\n'
										'看来都经受过相当严酷的体能训练啊。{wait}'
									)),
									Insn('TEXT_WAIT'),
								]),
								(None, []),
							]),
							Insn('FLAG_SET', Flag(0)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(8), Text(
								'今天早上，黑月贸易公司的诸位\n'
								'都自行出院了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'我本来是想阻止的，\n'
								'因为他们的枪伤还没有治好……{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'看来你们已经和约亚西姆医生谈过了啊，\n'
						'这真是再好不过了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'随时都欢迎诸位再来哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'约亚西姆医生正在研究区四楼的\n'
						'研究室里等候各位。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'……最好趁他还没有偷懒出去玩，\n'
						'赶快过去找他吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1733)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(8), Text(
								'欢迎来到圣乌尔斯拉医院。\n'
								'您今天有何贵干呢？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(265), Text(
								'#0500F真是很久都没来\n'
								'乌尔斯拉医院了啊。{wait}'
								'{page}'
								'从那场狼型魔兽事件以后，\n'
								'最多也就是巡逻时路过这里而已。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F哈哈，这么说也许有些失礼，\n'
								'不过，上士好像从不会生病啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(265), Text(
								'#0504F嗯，那当然啦。{wait}'
								'{page}'
								'#0500F自从进了警备队，\n'
								'我就一直很注重保持身体健康，\n'
								'尽量让自己连小病也不要得。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'呵呵，真厉害啊。\n'
								'尽量不要让自己生病就医，\n'
								'这可比什么都重要。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'不过，身体一旦真的出现了什么问题，\n'
								'也还是应该立刻来医院的。\n'
								'因为有些事情，光靠自己是无法解决的。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(1733)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(8), Text(
								'调理好自己的身体，保持健康，\n'
								'尽量不来医院，比什么都重要呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'呵呵，这位警备队员的健康理念\n'
								'是非常正确的。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
					Insn('CALL', Function((1, 26))),
				]),
				(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'约亚西姆医生的研究室\n'
						'就在研究区的四楼。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'只要去院区的屋顶，\n'
						'就很容易看到研究区的位置了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(8), Text(
								'欢迎光临乌尔斯拉医院。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'各位教授今天都出差\n'
								'参加教授会议去了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'在确认过主治医生之后，\n'
								'请办理诊察手续。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(0)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(8), Text(
								'各位教授今天都出差\n'
								'参加教授会议去了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'在确认过主治医生之后，\n'
								'请办理诊察手续。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(8), Text(
								'今天好像有游客\n'
								'前来接受身体检查。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'我虽然也能理解他们很想体验\n'
								'最先进医疗设备的心情……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'但那样做的话，就可能会耽误\n'
								'重病患者的检查。\n'
								'总觉得有些不太好呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(0)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(8), Text(
								'好像有一些游客前来\n'
								'做健康检查之类的。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'……既然是外来的客人，\n'
								'我们就不能怠慢……\n'
								'但一想到他们的动机，心情还是很复杂。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
					Insn('CHAR_ROTATE', Char(8), 266, 0),
					Insn('0x4B', Char(23), -1),
					Insn('TEXT_TALK', Char(8), Text(
						'啊，迪塔总裁……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'真是十分感谢您\n'
						'今年也能光临本院。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'患者们一定也会很高兴吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(23), Text(
						'#2804F哪里的话，别那么客气。{wait}'
						'{page}'
						'这只是我的个人行为而已。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('0x4C', Char(23), -1),
				]),
				(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 22, Insn('FLAG_GET', 16))), Insn('FLAG', Flag(0)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
							Insn('TEXT_TALK', Char(8), Text(
								'听说赛西儿小姐和其他护理师们\n'
								'顺利地分配好工作，安排出假期。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'真是羡慕她们啊。\n'
								'事务部门这边的人手比较少，\n'
								'所以几乎都没有休假。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('EXEC', Insn('QUEST_GET', 22, Insn('FLAG_GET', 16))), Insn('END')]), [
							Insn('TEXT_TALK', Char(8), Text(
								'如果今后再有什么问题，\n'
								'欢迎随时光临本院。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'我们一定会诚心诚意地\n'
								'为您服务。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('EXEC', Insn('QUEST_GET', 22, Insn('TASK_GET', 0))), Insn('END')]), [
							Insn('TEXT_TALK', Char(8), Text(
								'必须让约亚西姆医生\n'
								'快点回来……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'诸位，一切都拜托你们了。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('EXEC', Insn('QUEST_GET', 22, Insn('FLAG_GET', 2))), Insn('END')]), []),
						(None, []),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('END')]), [
							Insn('CALL', Function((1, 79))),
						]),
						(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(8), Text(
								'职员宿舍的琪秀宿舍长和\n'
								'玛洛妮虽然算是\n'
								'克拉克事务长的部下，不过……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'你可不要把这些话告诉别人哦，\n'
								'其实事务长在琪秀宿舍长\n'
								'的面前很恭顺呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(0)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(8), Text(
								'你可不要告诉别人哦，\n'
								'其实克拉克事务长在琪秀宿舍长\n'
								'的面前很恭顺呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(8), Text(
								'院长一直都巡游于各个国家之间，\n'
								'进行技术交流并挖掘人才，\n'
								'很少会出现在医院里。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'其实，这么一说，\n'
								'连我也没有见到过院长……\n'
								'到底是个怎样的人呢？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(0)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(8), Text(
								'院长十分忙碌，\n'
								'几乎都不会\n'
								'出现在医院里。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'实际上，医院的经营是\n'
								'交由教授们来负责的。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'今天的来访者接待就到此为止了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'如果太晚的话，也会不安全，\n'
						'请前来探病的客人抓紧时间。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
					Insn('TEXT_TALK', Char(8), Text(
						'临近傍晚，外来的患者及访客\n'
						'也逐渐散去了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(8), Text(
						'之前发生过利顿医生受伤的事情，\n'
						'所以一定要趁天还没黑之前，\n'
						'让大家都回到市里呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(8), Text(
								'……那个，赛西儿小姐。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'再怎么说，这里也是工作场所，\n'
								'是不是也该稍微收敛一点，\n'
								'不要在别人面前进行太亲密的身体接触呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0006F……真不好意思。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(310), Text(
								'#1305F哎呀，罗伊德有什么\n'
								'好道歉的啊？{wait}'
								'{page}'
								'#1309F呵呵……榭拉小姐，\n'
								'你是在羡慕我吧？\n'
								'我有个这～么可爱的弟弟。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(8), Text(
								'唉……随你去好了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(0)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(8), Text(
								'……反正我已经不想阻止你了，\n'
								'你们想继续抱在一起也好，\n'
								'还是怎样也好，都请随意吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0006F（哑口无言……）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
				(None, []),
			]),
			Insn('TEXT_END', Char(8)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('CALL', Function((1, 3))),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('TEXT_START', Char(9)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'虽然院长一直不在，\n'
				'但医院的经营状况却非常不错。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'长年以来，在市民中累积的深厚信赖感\n'
				'也起到了很大作用。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'榭拉负责接待以及院内联系的工作，\n'
				'她做得非常努力。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'单看工作量的话，\n'
				'甚至都不会输给赛西儿小姐呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'只要是送来的患者，就一定要救助。\n'
				'这就是乌尔斯拉医院的座右铭。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'即使是面对十恶不赦的坏人，\n'
				'本院也会贯彻这个原则。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'虽然本医院从各国的各机关\n'
				'领取资金。\n'
				'但在经营方针上，仍然是推崇节俭。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'要把资金尽量都用于补贴\n'
				'那些负担不起医疗费用\n'
				'的患者们。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'既然在这间医院工作，\n'
				'我们便不是普通的业务人员，\n'
				'而是为了救助患者而工作。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'如果患者能面带笑容地出院，\n'
				'我就会感到很幸福呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'教授们既要搞研究，又要指导实习医生，\n'
				'还要兼任复诊的工作，\n'
				'所以非常繁忙。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'不过，约亚西姆医生例外，\n'
				'他好像一直都不怎么忙呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'我负责管理这间医院的\n'
						'一切事务。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'从设备的预算分配，\n'
						'到导力网络的调整……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'虽然工作多到让人头痛，\n'
						'但是很有挑战性啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'尤其是导力网络的调整，真是非常辛苦。\n'
						'因为医院里除了我之外，\n'
						'再没有会操作的人了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'如果可以的话，真希望能从\n'
						'克洛斯贝尔市那边调来一位技师呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(9), 180, 0),
			Insn('CHAR_ROTATE', Char(66), 15, 0),
			Insn('0x4B', Char(66), -1),
			Insn('TEXT_TALK', Char(9), Text(
				'您想做健康诊断吗？\n'
				'那么，请在这边的\n'
				'文件上签名。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'因为是初诊，\n'
				'所以可能会多花一些时间。\n'
				'您可以等待一下吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(66), Text(
				'嗯，没问题。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x4C', Char(66), -1),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'迪塔总裁每年都会\n'
				'送来很多礼物，就算分给\n'
				'全部患者也是足够的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'哎呀，真是位了不起的人啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'我们正在商讨，是否应该\n'
						'在接待处实行卡片制度。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'预先准备好记载着\n'
						'个人信息的卡片钥匙，\n'
						'这样就可以大大缩减接待处的手续量了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'只是，由于目前还存在着卡片量产体制，\n'
						'以及个人情报保护工作等问题，\n'
						'新制度的实行还很艰难呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'我们正在商讨，是否应该\n'
						'在接待处实行卡片制度。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'不过，也有不少问题\n'
						'阻碍了新制度的施行……\n'
						'看来在短时间之内还难以实现。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((1, 80))),
				]),
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'我本来在宿舍的食堂吃午饭，\n'
						'结果宿舍长说『职员不要在中午过来』，\n'
						'然后就把我赶出来了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'哎呀呀……\n'
						'琪秀宿舍长真是\n'
						'让人敬畏啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'哎呀呀……\n'
						'琪秀宿舍长真是\n'
						'让人敬畏啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'……这就是所谓的女强人吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(9), Text(
						'导力网络将乌尔斯拉医院\n'
						'与克洛斯贝尔市紧密联系在了一起。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'市民还可以通过导力网络\n'
						'进行预约服务，\n'
						'虽然目前还在试验阶段。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'不过，因为普及率的问题，\n'
						'它并没有被广泛利用。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(9), Text(
						'如果在导力网络上进行事先\n'
						'预约服务，就可以免去等待\n'
						'时间，顺利进行诊察。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(9), Text(
						'不过，因为普及率的问题，\n'
						'它并没有被广泛利用。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'警察局的诸位……\n'
				'感谢你们帮助\n'
				'安置防护栏。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'但愿这样就能让\n'
				'魔兽无法再进来……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'警察局的诸位……\n'
				'你们的调查有什么进展了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'实在是不愿意相信有魔兽\n'
				'闯入了医院……\n'
				'如果那是真的，事情可就严重了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'关于利顿是否真的遭到了魔兽袭击，\n'
				'我希望你们能找出确凿的证据。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(9), Text(
				'欢迎您光临圣乌尔斯拉\n'
				'医科大学附属医院。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(9), Text(
				'旁边的接待处负责\n'
				'接待业务。\n'
				'如有需要，请您去那边咨询。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(9)),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('CHAR_WATCH', Char(254), Char(60), 0),
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀，今天有何贵干呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'初诊的客人，请先在接待处\n'
				'办理相关的手续。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'之前送进来的那些伤患，\n'
				'现在正在ＩＣＵ区的病房里休息。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'他们倒是没有性命之忧，\n'
				'明天应该就能下地行走了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天送来的那些伤患，\n'
				'总算是保住了性命。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……从伤势状况可以看出，\n'
				'似乎是遭受了枪击与殴打呢。\n'
				'火药味真是相当重啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('CHAR_WATCH', Char(254), Char(53), 0),
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀，小朋友，你不要紧吗？\n'
				'你好像发烧得很严重呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'把这个温度计夹在腋窝下面，\n'
				'老老实实待一会哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'怎么回事，又被卷入到\n'
						'什么纠纷中了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F没、没有啦……\n'
						'并不是那么\n'
						'严重的问题。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，警察弟弟真是有趣呢，\n'
						'平常聊天时总是谈起你。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(258), Text(
								'#0100F呵呵，罗伊德好受欢迎啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(259), Text(
								'#0200F或许正是因为\n'
								'有罗伊德前辈在，\n'
								'才会发生各式各样的事件呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(260), Text(
								'#0306F罗伊德在护理师们间\n'
								'成为热门话题了吗？\n'
								'真是个让人嫉妒的家伙啊……{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, []),
					]),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F饶了我吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，警察弟弟真是有趣呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那个……你和赛西儿前辈\n'
						'自那次之后又有什么进展了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0011F现、现在可不是说这些的时候，\n'
						'我们先告辞了！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'在我睡觉的时候，也经常会有急诊患者被送到，\n'
						'然后被突然叫起来，几乎都没有休息时间呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'仔细想想，\n'
						'像这种工作，如果不是非常喜欢的话，\n'
						'实在是很难坚持下来啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我虽然是一个\n'
						'没多少耐心的人，\n'
						'但却意外地有韧性……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'如果不是非常喜欢的话，\n'
						'真是很难把这项工作坚持做下去。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'赛西儿前辈似乎\n'
						'非常喜欢护理师这项工作呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'里面的房间是\n'
						'加护病房#8RＩＣＵ#\n'
						'和Ｘ光照片拍摄室。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'所谓的Ｘ光照片，\n'
						'是我们最近同雷米菲利亚的设备制造厂商\n'
						'共同开发的最新型医疗器材。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'它使用了特殊的感光结晶回路，\n'
						'是一种可以通过人体，把骨头与内脏\n'
						'的状况映照在相片上的设备。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'只要有了它，无需开刀，\n'
						'就可以直接发现病因了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0205F我之前听说过有关它的开发消息……\n'
						'原来都已经进展到正式使用的阶段了啊。{wait}'
						'{page}'
						'#0204F真不愧是乌尔斯拉医院呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F……哈哈，虽说我\n'
						'只听懂了一半……\n'
						'但也能感觉到，那是个非常厉害的东西呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'所谓的Ｘ光照片，\n'
						'是一种可以通过人体，把骨头与内脏\n'
						'的状况映照在相片上的医疗器械。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'只要有了它，无需开刀，\n'
						'就可以直接发现病因了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……不过，关于详细的原理，\n'
						'其实我也不怎么懂啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 23))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'赛西儿前辈真是个很勤劳的人。\n'
						'不仅会把自己的工作做好，\n'
						'还经常会给别人帮忙。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'像约亚西姆医生那样的人，\n'
						'真应该好好向她学习啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我在乌尔斯拉医院工作了很多年，\n'
						'一到这个时期就很忙呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'忙到根本没时间休息，\n'
						'也是很平常的事情啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'这样一想的话，庆典第一天的时候，\n'
						'我还休了一天假，已经很幸运了……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'凯瑞教授的儿子\n'
				'似乎混迹在克洛斯贝尔市的\n'
				'不良分子里……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'大概是正处于叛逆期吧。\n'
				'我想，代沟这种东西，\n'
				'随着时间的流逝就会慢慢消失的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我去问过了赛西儿前辈，\n'
				'问她是不是认识彩虹剧团的\n'
				'伊莉雅丄普拉提耶。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……结果她大大方方地直接承认了，\n'
				'好像根本就没把它当成什么秘密呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'赛西儿前辈好像\n'
						'和一位超级名人很熟呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'警察弟弟，你知道吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1029)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(257), Text(
								'#0005F…………是、是吗……？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('CHAR_WATCH', Char(10), Char(257), 500),
							Insn('TEXT_TALK', Char(254), Text(
								'哦，你也不知道吗，\n'
								'那究竟会是谁呢？{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('TEXT_TALK', Char(257), Text(
								'#0003F（……多半是指伊莉雅小姐吧。）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'赛西儿前辈好像\n'
						'和一位超级名人很熟呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那究竟会是谁呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'凯瑞教授的儿子\n'
				'似乎正和一群可疑的人混在一起。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'他明明有那么出色的父亲，\n'
				'到底还有什么不满的呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀，您是等候诊察的病人吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'如果您已经登记过了，\n'
				'就请坐在这里候诊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'……下一个接受诊察的……是那位患者吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 5))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'请把这个体温计\n'
						'夹在腋下。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('CHAR_SET_FRAME', Char(25), 0),
	Insn('0x4B', Char(10), -1),
	Insn('TEXT_TALK', Char(10), Text(
		'今天有什么地方不舒服吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(25), Text(
		'啊，好像有点发烧……\n'
		'大概是感冒了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'那么，在等待诊察的这段时间，\n'
		'请先测量一下体温吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(10), -1),
	Insn('CHAR_SET_FRAME', Char(25), 0),
	Insn('FLAG_SET', Flag(2)),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 11))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'哇哇哇哇……！{wait}'
					)),
					Insn('TEXT_WAIT'),
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
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 11))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呀呀呀呀……！！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(19)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 73))),
				]),
				(None, [
					Insn('0x4B', Char(71), -1),
					Insn('0x4B', Char(11), -1),
					Insn('TEXT_TALK', Char(11), Text(
						'对了……之前那件事，\n'
						'你考虑了没有啊？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(71), Text(
						'#08705F啊……是让我在研究区\n'
						'进行特别讲座的事吗？{wait}'
						'{page}'
						'#08706F嗯，因为临近纪念庆典，\n'
						'现在越来越忙了，所以……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'嗯……真可惜，\n'
						'但既然如此，我也就不勉强你了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('0x4C', Char(71), -1),
					Insn('0x4C', Char(11), -1),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 11))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'呜呼呼呼……！！{wait}'
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

data['code'][7] = [
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
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'在接待内科患者时，\n'
						'我总是会这样想……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'像内科医术这种以促进身体自愈为主\n'
						'的医疗方式，有时也存在效率不足的情况，\n'
						'而此时凭借外科医术的速度优势，便有可能拯救患者。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'灵活地结合两种医术，互相弥补彼此的不足，\n'
						'这才是理想中的医疗形态吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……我与凯瑞教授之间可以说是水火不容，\n'
						'所以从我嘴里说出这样的话，或许有点奇怪吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……咳咳！啊，算啦。\n'
						'你就把我刚才说的话给忘掉吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……我刚才说的话，\n'
						'无论如何也不能\n'
						'告诉凯瑞教授哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'咳咳！\n'
				'凯瑞教授那家伙，好像用外科手术\n'
				'顺利救助了今早的那些伤患呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……哼，外科医术\n'
				'倒也有点用啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'约亚西姆最近似乎\n'
				'总是在研究室里埋头研究。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽说他平时总有偷懒的坏习惯，\n'
				'但在专业研究方面，\n'
				'却是个很能干的男人呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯……你们那么着急做什么？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'除了患者以外，\n'
				'谁也没有来过这里哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'咳咳！\n'
						'干什么？你们几个。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F那个，我们稍微有些事情，\n'
						'要来找神经丄药物学科的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'啊，原来如此。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'神经丄药物学科确实是\n'
						'属于内科的范畴，\n'
						'但说到底，也还只是研究中的领域。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'要是有什么事的话，\n'
						'直接去找约亚西姆就可以了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'神经丄药物学科确实是\n'
						'属于内科的范畴，\n'
						'但说到底，也还只是研究中的领域。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'要是有什么事的话，\n'
						'直接去找约亚西姆就可以了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'前段时间，\n'
						'我试着把内科的诊断工作\n'
						'托付给了古恩。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'她的技术水准虽然无可挑剔，\n'
						'但对患者的关怀却还不够……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'为了不辱乌尔斯拉医院的\n'
						'实习医生之名，\n'
						'我希望她能更上一层楼。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'如果想掌握确切的病情，\n'
						'就需要拥有能与患者\n'
						'良好沟通的能力。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'古恩在那方面\n'
						'还不够成熟呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'自从纪念庆典开始之后，\n'
				'实习医生们似乎就\n'
				'有些松懈呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯哼！\n'
				'这种时候，就要给他们\n'
				'一记当头棒喝才行。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(254), Text(
								'给你们添了不少\n'
								'麻烦呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'我马上还要讲课，\n'
								'下次有机会再聊吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'以后也请多多关照。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(3)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(254), Text(
								'在七耀教会学习的日子，\n'
								'真是让人难以忘怀。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'以后得找个时间去向艾拉尔达\n'
								'大主教表示感谢才行啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('TASK_GET', 2))), Insn('END')]), [
					Insn('CALL', Function((1, 75))),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('TASK_GET', 0))), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'请去克洛斯贝尔大教堂，\n'
						'帮我向艾拉尔达大主教\n'
						'要来『羽扇豆草』吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'对了，我事先提醒一下……\n'
						'大主教可是比我还要难相处的人……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'一定不能有失礼节啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 19, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('CALL', Function((1, 74))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……唔，只是这种无关紧要的请求，\n'
						'他们真的会来吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'果然还是应该\n'
						'去拜托游击士吗……？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过，我又不想因为这种\n'
						'程度的小事而花费米拉……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'那天，让利顿\n'
				'交报告的人是我……\n'
				'真没想到会发生那样的事情。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，其他的实习医生\n'
				'没有再遭到袭击，\n'
				'真是不幸中的万幸啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'嗯哼！……有什么事吗？\n'
						'你们好像不是这里的学生啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……嗯，仔细一看的话，\n'
						'似乎都是很聪明的孩子呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'你们几个，要不要来挑战一下\n'
						'明年的入学考试呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0305F噢！原来我们还有这种潜质吗！{wait}'
						'{page}'
						'#0304F兰迪医生华丽的\n'
						'护理师后宫生活……\n'
						'听起来好像很不错呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F喂喂……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0111F话说回来，这间乌尔斯拉医院\n'
						'也从邻国吸引了很多考生，\n'
						'接受考试的人数可是非常多的。{wait}'
						'{page}'
						'#0103F去年的录取率……\n'
						'好像是一百二十分之一吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0303F这么难啊，那还是放弃吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0211F……放弃得真干脆。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'这间乌尔斯拉医院，\n'
						'是一家连医疗大国雷米菲利亚也敬畏三分\n'
						'的最尖端医疗研究所。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔本地就不必说了，\n'
						'埃雷波尼亚帝国、卡尔瓦德共和国、\n'
						'雷米菲利亚公国以及利贝尔王国……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'各国的优秀年轻人都以这里为目标，\n'
						'经过拼命学习，并通过严格的考试，\n'
						'才能得到入学的机会。{wait}'
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

data['code'][8] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'据说，今天用救护车送来的那些伤患\n'
				'已经恢复意识了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'本院医生的水准真是一流呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'前段时间，我又参加了\n'
				'临床实习……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我尽可能用\n'
				'最温和的态度来接触患者，\n'
				'结果，评价从Ｂ－变成了Ｂ＋呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然只是很小的进步……\n'
				'不过，距离我成为内科医生的梦想，\n'
				'总算是又向前迈进了一步。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'刚才拉格教授在为病人诊察，\n'
						'我看着他时，\n'
						'忽然注意到一件事。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'就连那个难以相处的教授，\n'
						'在患者面前也都会\n'
						'表现得那么耐心和蔼……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'仔细想想，\n'
						'我原来只注重技术方面的评价，\n'
						'却忽视了这个重要的部分啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'就连那个坏脾气的拉格教授，\n'
						'在患者的面前也都会\n'
						'表现得那么耐心和蔼……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我所缺少的东西，\n'
						'大概就是那种态度吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'拉格教授\n'
						'给我的评价\n'
						'总是不高呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'就算我去问他到底有什么不足，\n'
						'他也只会说『自己去体会』。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'可恶，既然如此，\n'
						'我平时就要多观察教授了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'既然如此，\n'
						'我就来观察拉格教授好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'无论如何我也要找出\n'
						'得到好评价的秘诀。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'教授今天不在，\n'
				'所以必须努力和利顿配合，\n'
				'把工作做好才行。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'但是……\n'
				'这好像和评定分数没什么关系，\n'
				'做起来真是没什么动力啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'那两位教授，彼此之间的关系很差呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真搞不懂，两人在各方面都那么相似，\n'
						'为什么就是看对方不顺眼呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'不过，毕竟没有像某些医院那样，\n'
						'内外科之间还进行着龌龊的党派斗争……\n'
						'也还算好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'昨天有临床实习呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然我个人觉得\n'
						'自己做得不错。\n'
						'但教授却给了我Ｂ－的评价……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'可恶，通往女强人医生的\n'
						'道路真是意外地艰难呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'这几天的临床实习……\n'
						'虽然我个人觉得\n'
						'自己的表现足以拿到Ａ＋评价。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但最后竟然是Ｂ－啊……\n'
						'一定要继续努力才行啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'利顿的伤好像已经治好了，\n'
				'正在干劲十足地工作呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'但是，因为他太过努力，\n'
				'好像连约亚西姆医生也把工作\n'
				'都推到他身上了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 180, 0),
			Insn('TEXT_TALK', Char(254), Text(
				'教、教授～！\n'
				'请冷静一点啊！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'不过，利顿\n'
				'也真是不走运呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'好不容易把报告写好了，\n'
				'竟然遇到了那样的事。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'居然会在自己学习的地方住院，\n'
				'他一定没想到\n'
				'自己会遇到这样的倒霉事吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'由于利顿受伤的缘故，\n'
				'轮值变得更加辛苦了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'真是的……\n'
				'说是被魔兽袭击了，\n'
				'但到底是真的假的啊？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
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
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 11))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'哇哦哦哦哦……！{wait}'
					)),
					Insn('TEXT_WAIT'),
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
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 11))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'哦呀呀呀呀……！！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 11))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'哇呀呀呀呀……！！{wait}'
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

data['code'][10] = [
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
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'今天早上救治重伤患者的时候……\n'
						'不，其实我一直都在考虑\n'
						'这个问题……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'即使是在外科的治疗现场，\n'
						'也必须要有麻醉及\n'
						'点滴之类的内科医疗技术呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我想，只有外科与内科\n'
						'携手合作、互相弥补，\n'
						'才是最理想的医疗状态吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……但我和拉格教授\n'
						'总是吵个没完，\n'
						'说出这样的话，或许有点奇怪吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……咳咳！\n'
						'一不小心说漏嘴了，\n'
						'讲出了不该讲的话呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'听好，刚才那些话可千万不能\n'
						'透露给拉格教授哦！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'就在刚才，从克洛斯贝尔市那边\n'
						'送来了几名急救患者。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我和约亚西姆他们一起\n'
						'为患者做了些基本处理。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呼，真是累坏了。\n'
						'我也上年纪了吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'从克洛斯贝尔市送来一些急救患者，\n'
						'总算是做完了基本处理。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呼，真是累坏了。\n'
						'我也上年纪了吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'趁着还没忘记的时候，\n'
						'不断复习学过的东西，\n'
						'就能让它变成长期记忆。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'也就是说，作为『知识』\n'
						'清晰地刻在脑子里。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我们这里的实习医生之所以很优秀，\n'
						'或许就是得益于养成了经常复习的\n'
						'好习惯吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'趁着还没忘记的时候，\n'
						'不断复习学过的东西，\n'
						'它就会变成『知识』，储藏在脑海里。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……哈，这也是从约亚西姆那里现学现卖的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'护理师刚才通知我说，\n'
						'我儿子琴兹\n'
						'来医院了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'大概是我妻子让他来送饭，\n'
						'他才会过来的吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然他现在可能\n'
						'正在满嘴抱怨……\n'
						'但我还是非常高兴呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我儿子琴兹\n'
						'好像来医院\n'
						'给我送饭了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我真是很高兴啊。\n'
						'呵呵，这样的表情，\n'
						'可不能让拉格教授看见啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'在院区屋顶的那个研究区里，\n'
				'保存着在至今为止的研究中\n'
				'所得到的贵重资料。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'如果没有必要，\n'
				'我希望外部人员最好不要进去。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……克洛斯贝尔市昨天发生的那起骚乱，\n'
						'我的儿子琴兹似乎也参加了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'多亏有警察的干预，\n'
						'好像并没有人受伤……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……唉……\n'
						'真希望他能让我少操点心。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'本来应该要好好教训他一番，\n'
						'但我却无法到场……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……唉……\n'
						'我真是个不称职的父亲啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我本来打算明天和儿子一起去看\n'
				'彩虹剧团的演出……\n'
				'但目前看来，应该是去不成了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……竟然去讨好孩子，\n'
				'身为父亲，我真是很失败。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('END')]), [
							Insn('CALL', Function((1, 81))),
						]),
						(None, [
							Insn('CALL', Function((2, 6))),
						]),
					]),
				]),
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_SET_FRAME', Char(254), 0),
					Insn('TEXT_TALK', Char(254), Text(
						'在上上个月，那群不良分子的成员\n'
						'不是被送到医院了吗。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我当时很担心伤患中会不会有我儿子琴兹，\n'
						'吓得脊背发凉。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……明明发生了那样的事情，\n'
						'他却还要继续\n'
						'留在不良分子里面……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真是的，真希望\n'
						'他能让我少操点心啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……我在儿子心中的形象\n'
						'似乎并不怎么好呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'一直以来，我因为工作繁忙的缘故，\n'
						'总是待在医院，很少在家里陪伴家人，\n'
						'所以才得不到儿子的尊敬吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我儿子会成为不良分子的成员，\n'
						'我或许应该承担一部分责任……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 12))),
				]),
				(None, [
					Insn('CHAR_SET_FRAME', Char(254), 0),
					Insn('TEXT_TALK', Char(254), Text(
						'听好了，亚苏拉。\n'
						'你已经是负责教授\n'
						'机械医疗课程的主任了，{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'总保持这种学生的心态可不行哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'所谓外科，就是在近年\n'
						'逐渐普及开来的\n'
						'一种近代医疗手段。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但是，不管怎么说，\n'
						'它还是一种新技术。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'用手术刀割开身体，\n'
						'这样的事，直到现在\n'
						'也难以得到大众的理解。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'包括那个拉格教授在内，\n'
						'对外科医术持有偏见的人\n'
						'并不在少数，这便是现状。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过，那种跟不上近代医疗\n'
						'进化速度的落伍老头，\n'
						'我才懒得理呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'亚苏拉……\n'
				'今天好像也迟到了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'真是的……\n'
				'都多少次了，总是不知悔改。{wait}'
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

data['code'][11] = [
	Insn('0x4B', Char(11), -1),
	Insn('0x4B', Char(14), -1),
	Insn('CHAR_WATCH', Char(11), Char(14), 0),
	Insn('CHAR_WATCH', Char(14), Char(11), 0),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(11), Text(
				'嗯哼！\n'
				'我还以为是谁呢，这不是凯瑞教授嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'哎呀，原来是拉格教授。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'……啊，对了。\n'
				'关于昨天那个重伤患者的处理……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'啊呀，您已经听说了\n'
				'我昨天的成果了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'哼哼哼，你们内科的时代\n'
				'就快要面临终结了吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'#4S……你说什么！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#4S……想打架吗！？{wait}'
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
			Insn('TEXT_TALK', Char(11), Text(
				'嗯哼！我还以为是谁呢，\n'
				'这不是凯瑞教授嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'您那脏兮兮的胡子，\n'
				'今天也给医生的形象抹黑了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'哎呀呀，\n'
				'拉格教授您也不逊色啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'您那好像被野火烧尽一样的秃头，\n'
				'竟然还没有春风吹又生，真是让人吃惊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'……您那难看的胡子……\n'
				'就用您擅长的外科手术，\n'
				'把它永久拔除如何？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'……您那荒芜的头顶才是呢，\n'
				'您对内科医疗这么拿手，\n'
				'怎么就没让它恢复茂密啊？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'#4S……你说什么！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#4S……想打架吗！？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('TEXT_TALK', Char(11), Text(
				'嗯哼！\n'
				'……那张肮脏的胡子脸，我还以为是谁呢，\n'
				'这不是凯瑞教授嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'哎呀呀，原来是拉格教授啊。\n'
				'哎呀，您的光头今天也亮得刺眼啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'……哼！\n'
				'真是让人叹息啊，{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'那些前途无量的实习医生们竟然要\n'
				'向您这样的人学习用刀子切人的手法。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'……哼！\n'
				'这么说来，您可真是轻松呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'有了七耀教会遗留的，现成的过时技术……\n'
				'光凭这点本事，就能摆出资深教授的架子了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(11), Text(
				'#4S……你说什么！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(14), Text(
				'#4S……想打架吗！？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('FLAG_SET', Flag(5)),
	Insn('0x4C', Char(11), -1),
	Insn('0x4C', Char(14), -1),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('0x4B', Char(19), -1),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('CHAR_WATCH', Char(19), Char(15), 0),
	Insn('TEXT_TALK', Char(15), Text(
		'亚苏拉……\n'
		'你又迟到了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'都已经是讲课的老师了，\n'
		'竟然还迟到，真是岂有此理！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'非、非常抱歉……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'我昨天光顾着研究新到的器材，\n'
		'结果完全入迷了，不知不觉就\n'
		'研究了一整夜。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'然后稍微小睡了一下，\n'
		'结果一直睡到刚才……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'……呼……\n'
		'你和学生时代相比，\n'
		'真是完全没有变化呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(19), -1),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('FLAG_SET', Flag(4)),
	Insn('FLAG_SET', Flag(8)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_WATCH', Char(254), Char(20), 0),
					Insn('TEXT_TALK', Char(254), Text(
						'亚苏拉主任……\n'
						'不管怎么说，在这里\n'
						'睡觉还是不太好吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哎呀，趁凯瑞教授他们\n'
						'吵架结束之前，要快点起来才行……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(20), Text(
						'嗯～嗯……再睡五分钟……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'还是不行啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'没办法，最后还是\n'
						'纵容了亚苏拉主任呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'她困得不行……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'亚苏拉主任最活跃\n'
						'的研究时间，\n'
						'毫无疑问是在晚上。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……只不过，出于这个原因，\n'
						'主任变成了睡懒觉大王，\n'
						'这也是事实。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然拥有副教授的头衔，\n'
						'但在她身上却感觉不到主任的威严，\n'
						'或许就是因为这个缘故吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'亚苏拉主任就是所谓的夜猫子呢，\n'
						'因此也是个睡懒觉大王。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然拥有副教授的头衔，\n'
						'但在她身上却感觉不到主任的威严，\n'
						'或许就是因为这个缘故吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'虽然器械的开发很困难，\n'
				'但能使用新技术\n'
				'也是乐趣所在。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'一想到在这里研发出来的医疗器械\n'
				'将会在未来的医疗领域中发挥巨大作用，\n'
				'就不由自主地心潮澎湃。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀……真希望亚苏拉主任\n'
				'别再硬撑了，继续睡懒觉去吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'话说回来，她毕竟都熬了快一个通宵，\n'
				'早上很难起得来吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'亚苏拉主任睡懒觉\n'
				'是预料之中的事情……\n'
				'事到如今，连教授都懒得再生气了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呼，我也耐心地\n'
				'等着她来吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'……亚苏拉主任今天好像\n'
				'又睡懒觉了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'没办法，今天研究的准备工作\n'
				'就让我来做吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'凯瑞教授和亚苏拉主任\n'
				'不在的时候，\n'
				'这间诊察室真是冷清呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'现在有些人手不足，\n'
				'要不要把芙萝拉叫来呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'……一切都和往日没有任何不同，\n'
				'根本感觉不到自己处在纪念庆典中呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'看样子，就算我去劝解应该也没用，\n'
				'不如还是去找本书看看吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'……已经是纪念庆典的第二天了吧，{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我陪着亚苏拉主任进行了\n'
				'三天三夜的研究，一直没有睡觉，\n'
				'所以都不太清楚日期了呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((2, 5))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'亚苏拉主任的职位虽然是\n'
						'『主任』，但实际地位\n'
						'却相当于副教授。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但是，比起去传道授业，\n'
						'主任更愿意闷在研究室\n'
						'里面搞开发呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'在某种意义上说，\n'
						'或许算是个地位很特殊的人物吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'目前，诸多国家都在致力于开发\n'
						'各式各样的导力器，其中，医疗器械的研究\n'
						'还是要属雷米菲利亚公国的技术最为尖端。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'在这所医院中所使用的医疗器械，\n'
						'也几乎都是由雷米菲利亚公国的\n'
						'赛兰德公司所制造的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'说起赛兰德公司，\n'
						'可是整个大陆中首屈一指的医疗器械制造商，\n'
						'同时也是这所医院的赞助商之一呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'所谓的医疗器械科，\n'
						'主要工作就是将医疗器械进行临床应用，\n'
						'同时摸索它们的改良余地。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'在这栋研究区中，\n'
						'正在研究着最先进的\n'
						'医疗技术。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'特别是『医疗器械科』，\n'
						'正在日夜不停地研究着\n'
						'运用导力的医疗器械。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……医疗器械科中有位亚苏拉主任，\n'
						'今天还没来上班，\n'
						'她是那里的一把手呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'医疗器械的研究工作，比所谓的\n'
						'近代医学领域──外科还要更加高深……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'你能想像在这个部门担任一把手的\n'
						'亚苏拉主任有多么优秀了吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我的梦想，就是在祖国埃雷波尼亚帝国\n'
				'建立一所大医院。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'这所乌尔斯拉医院\n'
				'正是最适合实现\n'
				'这个梦想的地方。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'因为这里拥有最尖端的医学技术，\n'
				'并汇聚了最优秀的医生呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((1, 16))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(17), Text(
				'#2400F虽然我也会帮忙查房，\n'
				'不过日常工作还是以研究为主。{wait}'
				'{page}'
				'以现在的状况来看，似乎是一直在给\n'
				'贝尔达因医生增加负担呢。{wait}'
				'{page}'
				'#2406F利顿可要尽快恢复过来，\n'
				'给我精精神神地干活才行。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((1, 16))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'我接待了一位病情比较复杂的患者，\n'
				'刚刚才结束了诊察工作。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……呼……\n'
				'去食堂喝杯红茶吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('CHAR_WATCH', Char(17), Char(18), 0),
	Insn('CHAR_WATCH', Char(18), Char(17), 0),
	Insn('0x4B', Char(17), -1),
	Insn('0x4B', Char(18), -1),
	Insn('TEXT_TALK', Char(17), Text(
		'#2400F贝尔达因医生，\n'
		'您好像是累坏了啊。{wait}'
		'{page}'
		'不介意的话，给您开一剂\n'
		'添加了蜂王浆的营养剂如何？{wait}'
		'{page}'
		'#2409F那可是阿尔摩利卡产的东西，\n'
		'效果很不错呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(18), Text(
		'啊，还是算了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(18), Text(
		'因为你的营养剂实在是太有效果了。\n'
		'要是产生了依赖性可就麻烦啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(17), -1),
	Insn('0x4C', Char(18), -1),
	Insn('FLAG_SET', Flag(9)),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哼哼哼哼……丅{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，一到了晚上就睡不着，\n'
				'工作效率反倒会提升呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'很好，从现在开始的十二个小时……\n'
				'要好好干活啦～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'对于医疗类导力器的开发而言，\n'
						'首先应该保证的就是安全性。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'既然作用对象是人体，\n'
						'就绝对不能出现什么差错。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这就是开发医疗器械的困难之处吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(8)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'对于医疗类导力器的开发而言，\n'
						'安全性比什么都重要。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'有关对人体影响的确切资料，\n'
						'并不一定仅仅通过小白鼠实验\n'
						'就能得到。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('FLAG_GET', 16))), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊，那个挂坠扣\n'
						'派上什么用场了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那是用即使被魔兽踩踏也不会损坏\n'
						'的耐久型合金制成的，\n'
						'一定能保存很久呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 2))), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'那个挂坠扣可是非常结实的东西，\n'
						'它曾被卷入到实验失败时的爆炸中，\n'
						'但也仍然完好无损呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'运气这么好的东西，\n'
						'一定非常适合当作制作礼物的材料呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('FLAG_GET', 2))), Insn('END')]), [
					Insn('CALL', Function((1, 78))),
				]),
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我总是睡懒觉，\n'
						'经常给夏鲁鲁添麻烦，\n'
						'所以从上周开始就想努力早起。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'早晨设定十二个闹铃，\n'
						'我差不多就能起床了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哎呀，就算熬了将近一通宵，\n'
						'只要努努力，也还是可以起来的嘛。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('EMOTE', Char(254), 0, 2000, (24, 27, 250, 0)),
					Insn('SLEEP', 1000),
					Insn('EMOTE_STOP', Char(254)),
					Insn('TEXT_TALK', Char(254), Text(
						'………………唔。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(8)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'………………呼。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'啊、啊啊……我可没睡着哦！\n'
						'只是稍微有点累了而已。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'好、好啦！今天也要努力地研究研究再研究！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'………………唔。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_ROTATE', Char(254), 90, 0),
					Insn('TEXT_TALK', Char(254), Text(
						'…………啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(254), Char(0), 500),
					Insn('TEXT_TALK', Char(254), Text(
						'那、那个，开始讲课了哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'今天的课程是关于\n'
						'医疗器械中使用的结晶回路的构造……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F那个……\n'
						'我们并不是这里的学生……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F好像是睡迷糊了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(8)),
					Insn('FORK_FUNC', Char(19), 0, Function((0, 0))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'啊……那个……对不起。\n'
						'授课的时候，外部人员是禁止进入的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('CHAR_ROTATE', Char(254), 90, 0),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……呼……呼…………{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F站、站着就睡着了……！？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F真厉害啊，\n'
						'真想学会这个绝技。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(8)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……呼……呼…………\n'
						'……呼噜。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……呼……呼…………{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 32))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((1, 81))),
				]),
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我身为一个技术人员，\n'
						'有个非常尊敬的人。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那就是利贝尔丄ＺＣＦ的\n'
						'艾莉卡丄拉塞尔博士……\n'
						'也就是那个有名的Ａ丄拉塞尔博士的女儿。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'她虽然身为女性，\n'
						'却拥有利贝尔王国\n'
						'最顶级的技术知识……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'身为一名女医生，我也想在医疗器械\n'
						'领域建立伟大的功绩。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(8)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'利贝尔的艾莉卡博士……\n'
						'她是足以与Ａ丄拉塞尔博士比肩的\n'
						'优秀技术员。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'身为一名女医生，我也想在医疗器械\n'
						'领域建立伟大的功绩。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 12))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'（唔……这么下去的话，想从凯瑞教授\n'
						'\u3000手中逃出去就难了……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'……你在听吗，亚苏拉！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(254), Char(15), 500),
					Insn('TEXT_TALK', Char(254), Text(
						'啊，是！\n'
						'我以后会多加注意的！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_ROTATE', Char(254), 90, 0),
					Insn('TEXT_TALK', Char(254), Text(
						'（稀里哗啦\n'
						'\u3000稀里哗啦）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……原来如此……\n'
						'这个结晶回路应该这样……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0101F（似乎完全没有注意到我们。\n'
						'\u3000好强的专注力啊……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(8)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……嗯？\n'
						'房间外面似乎有些吵啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'算啦，不管了，不管了。\n'
						'继续继续～丅{wait}'
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

data['code'][18] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'……呼……呼…………{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……呵呵，完成了…………{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'这样一来……与我的偶像艾莉卡博士\n'
				'之间的距离就又拉近了一步……吧。\n'
				'……唔。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(4)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'……呼……呼…………{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'这样一来……与我的偶像艾莉卡博士\n'
				'之间的距离就又拉近了一步……吧。\n'
				'……唔。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啊啊……\n'
				'又开始了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'他们两位应该都很认同对方的实力，\n'
				'但彼此之间的关系却莫名地恶劣呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天的值班是到傍晚为止。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'一想到可以离开约亚西姆医生，\n'
				'我的心情就感到无比平静……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，回到自己的房间之后，\n'
				'好好放松一下吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'约亚西姆医生所在的药物学丄神经科\n'
				'一直进行着各式各样的研究。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'在外科手术中使用的麻醉剂，\n'
				'还有用于滋补健体的营养剂等药剂，\n'
				'都是在那里研究调配出的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(10)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'约亚西姆医生所管理的\n'
						'药物学丄神经科，\n'
						'是一个让人深感兴趣的领域呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'作为近代医疗体系的一部分，\n'
						'同时也涉及到心理与精神领域……\n'
						'真是非常神秘啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我之所以会以内科医生为目标，\n'
						'也是出于对约亚西姆医生的崇拜之情。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(10)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'约亚西姆医生所管理的\n'
						'药物学丄神经科，\n'
						'是一个让人深感兴趣的领域呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我之所以会以内科医生为目标，\n'
						'也是出于对约亚西姆医生的崇拜之情。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，你们是要去\n'
				'约亚西姆医生那里吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'教授和副教授的研究室\n'
				'在研究区的四楼。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'其他教授的研究室也都在那里，\n'
				'你们可别搞错了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(10)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'拉格教授他们要出席教授会议，\n'
						'今天不会回来了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'在教授会议中，\n'
						'众多医院的教授们\n'
						'为了医术交流而聚集一堂。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'医学就是依靠这样的互补互助，\n'
						'才能一步一步向前发展吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(10)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'在教授会议中，\n'
						'众多医院的教授们\n'
						'为了医术交流而聚集一堂。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'为了医学的进步，\n'
						'教授们每天也都在进行学习呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(10)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 21))),
				]),
				(None, [
					Insn('CHAR_WATCH', Char(21), Char(22), 0),
					Insn('TEXT_TALK', Char(254), Text(
						'算了，这种事情，\n'
						'我也没办法强行执行啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'跟你的爷爷说，让他趁着\n'
						'病情恶化之前到这里来哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), []),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][20] = [
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
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我是来\n'
				'帮爷爷取药的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我希望爷爷能够\n'
				'按时吃药呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(11)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 21))),
				]),
				(None, [
					Insn('CHAR_SET_FRAME', Char(22), 0),
					Insn('TEXT_TALK', Char(254), Text(
						'一直都是我替他来……\n'
						'医生，真对不起。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(799)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(11)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我是来\n'
						'帮爷爷取药的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'因为爷爷讨厌医院，\n'
						'所以不自己来取。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我的爷爷\n'
						'特别顽固呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呼…其实医生本来\n'
						'要求他住院呢。{wait}'
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

data['code'][21] = [
	Insn('CHAR_WATCH', Char(21), Char(22), 0),
	Insn('CHAR_SET_FRAME', Char(22), 0),
	Insn('0x4B', Char(21), -1),
	Insn('0x4B', Char(22), -1),
	Insn('TEXT_TALK', Char(22), Text(
		'我爷爷\n'
		'还是应该来住院才\n'
		'比较利于病情的恢复吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'话是这么说……\n'
		'但他实在太顽固了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(22), Text(
		'对、对不起……\n'
		'我虽然一直劝他，\n'
		'哪怕偶尔来趟医院也好……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(21), -1),
	Insn('0x4C', Char(22), -1),
	Insn('FLAG_SET', Flag(10)),
	Insn('FLAG_SET', Flag(11)),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
			Insn('CALL', Function((1, 23))),
		]),
		(None, [
			Insn('TEXT_TALK', Char(68), Text(
				'#1305F……啊，罗伊德！{wait}'
				'{page}'
				'#1306F我虽然很想和你多聊聊，\n'
				'但今天的时间实在有些紧呢。\n'
				'……抱歉哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0003F（赛西儿姐姐……似乎很忙呢。）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('0x4B', Char(68), -1),
	Insn('0x4B', Char(10), -1),
	Insn('CHAR_WATCH', Char(68), Char(10), 0),
	Insn('CHAR_WATCH', Char(10), Char(68), 0),
	Insn('TEXT_TALK', Char(68), Text(
		'#1300F贝尔达因医生要的\n'
		'病例就是这个。{wait}'
		'{page}'
		'稍后可以帮我交给他吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(10), Text(
		'嗯，明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(68), Text(
		'#1309F呵呵，拜托了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(68), -1),
	Insn('0x4C', Char(10), -1),
	Insn('FLAG_SET', Flag(2)),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1395)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F迪塔总裁……？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(23), Text(
				'#2800F呀，诸位，\n'
				'能在这里会面，真是很巧啊。{wait}'
				'{page}'
				'#2805F……难道你们在执行任务时\n'
				'受了什么重伤吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0305F不，这倒是\n'
				'没有啦……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F总裁您呢，不会是哪里不舒服吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#0102F呵呵……{wait}'
				'{page}'
				'其实叔叔他也是位慈善家呢，\n'
				'平时都会以个人名义从事着许多慈善事业。{wait}'
				'{page}'
				'作为其中的一环，\n'
				'在每年的这个时候，他都会给\n'
				'正在住院的患者们赠送礼品。{wait}'
				'{page}'
				'#0102F算是弥补他们无法参加纪念庆典的遗憾。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F……原来如此啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(23), Text(
				'#2804F哈哈……虽说是慈善事业，\n'
				'但其实根本就没花多少钱。{wait}'
				'{page}'
				'#2800F偶尔做些这样的事情，\n'
				'也可以暂时从工作中解脱出来。{wait}'
				'{page}'
				'或许有人会说我只是为了自我满足，\n'
				'但不管别人怎么说，这也是我自己的原则。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0303F（这、这还真是……\n'
				'\u3000让人意外的一面呢。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F（一直都感觉是个单纯爽朗的大叔，\n'
				'\u3000但也考虑得很多呢。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1395)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(23), Text(
				'#2803F虽说是慈善事业，\n'
				'但其实根本就没花多少钱，\n'
				'只是我个人的一点坚持而已。{wait}'
				'{page}'
				'#2800F尽管如此……玛利亚贝尔\n'
				'每年也都会陪我一起来。{wait}'
				'{page}'
				'哈哈，身边的人一直都给予\n'
				'着我理解与支持啊。{wait}'
				'{page}'
				'#2803F……这份温暖的感觉，\n'
				'我想尽可能地分享给周围的人。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('TEXT_START', Char(254)),
	Insn('CALL', Function((1, 26))),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('0x4B', Char(8), -1),
	Insn('0x4B', Char(24), -1),
	Insn('CHAR_WATCH', Char(8), Char(24), 0),
	Insn('CHAR_WATCH', Char(24), Char(8), 0),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(8), Text(
				'啊，你是凯瑞医生的\n'
				'儿子吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'如果要找医生的话，\n'
				'我可以立刻帮你去叫……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(24), Text(
				'哼……哼……！\n'
				'那种男人，\n'
				'我根本就连他的脸都不想看到。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(24), Text(
				'帮我把饭交给他就好啦。\n'
				'我这就回去了！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'呵呵……老是这样子，\n'
				'一点也不坦率呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(0)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(24), Text(
				'我、我只是受老妈所托，\n'
				'来给他送东西而已。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(24), Text(
				'行了，只要帮我把东西\n'
				'给他送去就好啦！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'好的，那我就\n'
				'先保管了哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('0x4C', Char(8), -1),
	Insn('0x4C', Char(24), -1),
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
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'好像果然有点感冒啊……\n'
				'提前过来真是太对了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('CALL', Function((1, 5))),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'唔，体温计……\n'
						'刚夹的时候会被冰一下，\n'
						'所以稍微有点怕这东西呢。{wait}'
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
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎，做饭的时候被烫伤了，\n'
				'我还以为会有多严重呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'结果没什么大碍，\n'
				'真是太好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天人不多，真是得救了。\n'
				'我最害怕的就是排队了。{wait}'
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
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我还是第一次来医院，\n'
				'稍微有点不知所措呢。\n'
				'诊察终于结束了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯嗯，这还真是个不错的地方。\n'
				'今后我会再来的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(12)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'……哦，那个护理师，\n'
						'正偷偷看向这边呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，护理师小姐大多都是\n'
						'非常漂亮的美人呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0309F完全赞同！\n'
						'是吧，赛西儿小姐！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(310), Text(
						'#1309F哎呀呀……呵呵。\n'
						'就算你这么说，我也没有任何好东西给你哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F（赛西儿姐姐，太容易亲近了……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(12)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，马上就要轮到我了。\n'
						'得作好心理准备才行。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，我是第一次来这个医院……\n'
				'倒是个干净漂亮的地方啊。{wait}'
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
		(Expr([Insn('FLAG', Flag(793)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天就是最后一天了。\n'
				'呼，这么快就能将病治愈，真是太好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(784)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'如果只是治病的话，\n'
				'去大教堂那里配药\n'
				'倒是更便宜些。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过在这里能接受各式各样的检查，\n'
				'感觉更加放心一点呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'这间医院真不错呢，\n'
				'医生会非常亲切地为病人进行诊察。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽然离市区稍微有点远，\n'
				'不过幸好有巴士，所以花费不了多长时间。{wait}'
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
	Insn('TEXT_TALK', Char(254), Text(
		'我至今为止，只服用过\n'
		'七耀教会开的药呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'像医院这种地方，总觉得不太可信……{wait}'
	)),
	Insn('TEXT_WAIT'),
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
	Insn('TEXT_TALK', Char(254), Text(
		'嘿嘿……希望有个漂亮\n'
		'的女医生为我诊察。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'一定不要是个大叔啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
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
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_TALK', Char(254), Text(
		'喂！\n'
		'在医院里安静一点！{wait}'
	)),
	Insn('TEXT_WAIT'),
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
	Insn('TEXT_TALK', Char(254), Text(
		'知道给我看病的医生\n'
		'是位教授的时候，\n'
		'我还稍微有点害怕呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'不过他说话很和蔼，\n'
		'是位很不错的医生呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
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
	Insn('TEXT_TALK', Char(254), Text(
		'啊，今天还有生意要谈，\n'
		'希望能早点回去啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'唔，好想睡。\n'
		'真希望能快点排到我啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][36] = [
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
		'我稍微有点\n'
		'着凉了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'……在大半夜\n'
		'一直开着窗子睡觉，\n'
		'果然是不行的啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
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
		(Expr([Insn('FLAG', Flag(13)), Insn('NOT'), Insn('END')]), [
			Insn('CHAR_SET_FRAME', Char(254), 0),
			Insn('TEXT_TALK', Char(254), Text(
				'呼噜……{wait}'
			)),
			Insn('TEXT_WAIT'),
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
				'……啊！\n'
				'都已经等了好久了，\n'
				'差点睡过去。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(13)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'呼，好险好险。\n'
				'总觉得医院的候诊室\n'
				'有点催眠效果呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][38] = [
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
		'我去参观了一下开幕式，\n'
		'结果在人群中被挤得腰痛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'纪念庆典才刚刚开始。\n'
		'真想赶快治好，去玩个痛快啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
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
	Insn('TEXT_TALK', Char(254), Text(
		'这间医院还是老样子，\n'
		'看起来好像很忙呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
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
		(Expr([Insn('FLAG', Flag(14)), Insn('NOT'), Insn('END')]), [
			Insn('EXPR_CHAR_ATTR', Char(39), 5, Expr([Insn('CHAR_ATTR', Char(254), 4), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(254), 5, Expr([Insn('CHAR_ATTR', Char(254), 4), Insn('SET'), Insn('END')])),
			Insn('TEXT_START', Char(254)),
			Insn('CHAR_FLAG1_UNSET', Char(254), 16),
			Insn('CHAR_WATCH', Char(254), Char(39), 0),
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
			Insn('EXPR_CHAR_ATTR', Char(254), 4, Expr([Insn('CHAR_ATTR', Char(39), 5), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(39), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('EXPR_CHAR_ATTR', Char(254), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('CHAR_FLAG1_SET', Char(254), 16),
			Insn('TEXT_TALK', Char(254), Text(
				'喂喂，\n'
				'在医院里要安静一点哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'只要烧退下去，\n'
				'我就带你去看纪念庆典哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_FRAME', Char(254), 0),
			Insn('FLAG_SET', Flag(14)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'这孩子，似乎因为太期待\n'
				'纪念庆典而失眠，\n'
				'所以发烧了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
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
	Insn('TEXT_TALK', Char(254), Text(
		'哇哇，我想去纪念庆典。{wait}'
	)),
	Insn('TEXT_WAIT'),
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
	Insn('TEXT_TALK', Char(254), Text(
		'咳咳……\n'
		'呜，好难受。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'该不会是被传染了吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
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
	Insn('CHAR_SET_FRAME', Char(254), 2),
	Insn('TEXT_TALK', Char(254), Text(
		'喂喂，\n'
		'你可别传染给我啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][44] = [
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
		(Expr([Insn('FLAG', Flag(15)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'昨天，在克洛斯贝尔市的旧市街\n'
				'发生了非常热闹的事件哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我也去观战了，\n'
				'因为兴奋过头，不小心摔了一跤。\n'
				'结果就成了这副德行。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0306F（……从某种意义上说，\n'
				'\u3000好像是我们间接\n'
				'\u3000导致他受伤了吧？）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0005F（这、这个嘛……\n'
				'\u3000我觉得你有点\n'
				'\u3000想多了吧……）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'算啦，虽然受伤了，不过都怪自己。\n'
				'不管怎么说，反正那天挺开心的，无所谓啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(15)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'那个比赛，如果每年都搞一场的话，\n'
				'肯定会相当受欢迎吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
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
	Insn('TEXT_TALK', Char(254), Text(
		'呼～复查日偏偏赶在今天，\n'
		'真是倒霉啊。\n'
		'看来是彻底错过游行活动了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'算啦，只要不是明天就好。\n'
		'赶快接受诊察，然后回家去吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][46] = [
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
		'按照预定的话，\n'
		'我的疗程到今天就结束了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'接受完诊察之后，\n'
		'就陪老伴一起\n'
		'逛逛纪念庆典吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][47] = [
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
		'呵呵，\n'
		'我老伴的心态\n'
		'一直都很年轻呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][48] = [
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
		'现在去接受诊察，\n'
		'然后坐巴士回到市里，\n'
		'接着去乘坐水上巴士……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'嗯，好像还有时间玩呢。\n'
		'太好了，太好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][49] = [
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
		'我今天傍晚和男朋友\n'
		'约好要去米修拉姆呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EXPR_CHAR_ATTR', Char(46), 5, Expr([Insn('CHAR_ATTR', Char(254), 4), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(254), 5, Expr([Insn('CHAR_ATTR', Char(254), 4), Insn('SET'), Insn('END')])),
	Insn('TEXT_START', Char(254)),
	Insn('CHAR_FLAG1_UNSET', Char(254), 16),
	Insn('CHAR_WATCH', Char(254), Char(46), 0),
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
	Insn('EXPR_CHAR_ATTR', Char(254), 4, Expr([Insn('CHAR_ATTR', Char(46), 5), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(46), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(254), 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(254), 16),
	Insn('TEXT_TALK', Char(254), Text(
		'……哎呀，下一个就是我了吧，\n'
		'快点叫我啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][50] = [
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
		'明明是纪念庆典最后一天了，\n'
		'但今天也有不少人来呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][51] = [
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
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我被忠告说，不应该依赖药物，\n'
				'而应该换一种更加健康的生活方式。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'但由于工作原因，这很困难吧……\n'
				'呼，没有任何东西能够替代健康呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'咳咳……果然还是该早点来\n'
				'接受诊察呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我总是全心投入到\n'
				'工作之中……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][52] = [
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
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'已经从医生那里开完药了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'吃下这个药，公公的病情\n'
				'应该就会有所好转吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'在大厅里排队，\n'
				'总会感觉时间特别漫长。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'如果是陪同别人前来，\n'
				'这种感觉就更明显了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][53] = [
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
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'按顺序算的话，就快到我了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，要是带本书来就好了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呼，真够麻烦的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过，为了让诊察顺利进行，\n'
				'这也是没办法的事啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][54] = [
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
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我的老毛病似乎\n'
				'快要完全治好了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'坚持来接受复查，\n'
				'真是值得啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'真希望快点轮到我……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][55] = [
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
		(Expr([Insn('FLAG', Flag(1351)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，爷爷的病情似乎好转了，\n'
				'我也总算放下心来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1346)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'爷爷，静下心来，慢慢等吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][56] = [
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
		'嗯……\n'
		'似乎有点发热……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][57] = [
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
		'咳咳……\n'
		'我自作主张，不来复诊，\n'
		'结果病症很快就复发了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'过于相信自己的判断，\n'
		'果然很危险呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][58] = [
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
		'这里的实习医生都在\n'
		'专心学习着，真不错呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'我不由自主就想给他们加油呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][59] = [
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
		'为了健康，我正在练习一种\n'
		'模仿东方拳法动作的运动……\n'
		'结果用力过猛摔倒了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'哎呀，真不该勉强呢，\n'
		'哇哈哈。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][60] = [
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
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'马上就要轮到我接受诊察了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'如果耗到太晚，\n'
				'还是住在院内的招待所为好吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我还是第一次看到\n'
				'被救护车送来的患者。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哎呀……还是不看为好……\n'
				'好像真的很疼呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][61] = [
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
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'虽然已经接受医生的诊察了……\n'
				'但真的只是普通的感冒吗！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'要是出现什么严重的并发症，\n'
				'那可如何是好啊！？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哦，女神啊，\n'
				'求您保佑我的女儿\n'
				'不要患上重病……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][62] = [
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
		(Expr([Insn('FLAG', Flag(1565)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'……真是的，妈妈\n'
				'吓得惊慌失措的，\n'
				'真让人难为情……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'医生都说过了，\n'
				'只是普通的感冒，不必担心啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'咳咳……\n'
				'真是的，妈妈就是爱操心，\n'
				'只是普通的感冒而已。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][63] = [
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
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_TALK', Char(254), Text(
		'嗯，原来是这样的内部构造啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'哎呀，这里太大了，\n'
		'我都有点转晕了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][64] = [
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
		'说起医院，\n'
		'好像总有一种特殊的味道。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'应该是消毒用的酒精……\n'
		'我好像有些喜欢呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][65] = [
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
		'刚刚上午就有这么多人……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'对于克洛斯贝尔人来说，\n'
		'这里似乎是非常值得信赖的设施呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][66] = [
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
		'我明明是一大早赶来的，\n'
		'竟然要等这么久……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'快点啊，真是的！\n'
		'我的腰部正在发出悲鸣啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_SET_FRAME', Char(254), 0),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][67] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'嗯，奶奶的病房\n'
		'是在哪里呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][68] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'哇哇～医院可真大啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][69] = [
	Insn('TEXT_START', Char(254)),
	Insn('CHAR_ROTATE', Char(9), 180, 0),
	Insn('CHAR_ROTATE', Char(66), 15, 0),
	Insn('0x4B', Char(9), -1),
	Insn('TEXT_TALK', Char(9), Text(
		'您想做健康诊断吗？\n'
		'那么，请在这边的\n'
		'文件上签名。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'因为是初诊，\n'
		'所以可能会多花一些时间。\n'
		'您可以等待一下吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'嗯，没问题。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(9), -1),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][70] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(16)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯？写着什么？\n'
				'『关于健康检查的通知』……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'『为了在早期发现体内隐藏的疾病，\n'
				'我们推荐您做一次\n'
				'使用最新器械的综合检查』……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'原来如此，不愧是\n'
				'有名的乌尔斯拉医院呢。\n'
				'在别处都见不到这种东西呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'健康检查吗……\n'
				'虽然现在没时间做……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'但乌尔斯拉医院果然很先进呢。\n'
				'这里被誉为最新医疗技术的宝库，\n'
				'看来真是名不虚传。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][71] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(17)), Insn('END')]), [
			Insn('TEXT_TALK', Char(69), Text(
				'我、我昨天宵夜吃得太多了。\n'
				'肚子好疼啊……！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(69), Text(
				'肚、肚子好疼……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(69), Text(
				'还没轮到我吗……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(17)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][72] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(18)), Insn('NOT'), Insn('END')]), [
					Insn('EMOTE', Char(0), 0, 2000, (38, 38, 250, 1)),
					Insn('EMOTE', Char(1), 0, 2000, (38, 38, 250, 1)),
					Insn('EMOTE', Char(2), 0, 2000, (38, 38, 250, 1)),
					Insn('EMOTE', Char(3), 0, 2000, (38, 38, 250, 1)),
					Insn('SLEEP', 500),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F哎，这不是那位游击士吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0101F难道是……\n'
						'发生了什么事情吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#08601F嗯，有位旅行者钻入密林，\n'
						'似乎是被毒蛇之类的东西\n'
						'咬伤了呢。{wait}'
						'{page}'
						'#08601F我们急忙赶了过去，\n'
						'然后就把他送来了。{wait}'
						'{page}'
						'#08600F还好，艾欧莉雅已经为他\n'
						'做了适当处理，应该不会有什么大碍。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0305F处理吗……\n'
						'游击士竟然连\n'
						'这种技术都会啊？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#08602F是艾欧莉雅比较特殊啦。{wait}'
						'{page}'
						'#08600F她出身于医疗发达国家雷米菲利亚，\n'
						'而且好像还拥有医生资格证呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0211F……真难想像现在说的这个人，\n'
						'就是每次见面时都要粘着我的那位游击士啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#08609F哈哈，虽然她平时那个样子，\n'
						'但其实是个非常厉害的人呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(18)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#08600F艾欧莉雅出身于雷米菲利亚，\n'
						'而且还持有医生资格证。{wait}'
						'{page}'
						'#08609F虽然平时对可爱的东西没有抵抗力，\n'
						'但其实是个非常厉害的人呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][73] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(19)), Insn('NOT'), Insn('END')]), [
					Insn('0x4B', Char(71), -1),
					Insn('0x4B', Char(11), -1),
					Insn('CHAR_WATCH', Char(71), Char(11), 0),
					Insn('TEXT_TALK', Char(11), Text(
						'那位旅行者正在加护病房\n'
						'保持静养。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'哎呀，那个时候如果稍有闪失，\n'
						'搞不好就必须得截肢了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(11), Text(
						'幸好有艾欧莉雅在，\n'
						'才避免了那么严重的后果。\n'
						'总是给你们添麻烦啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(71), Text(
						'#08710F哪里哪里，身为游击士，\n'
						'这些都是我们应该做的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0307F#4S（可恶，真让人羡慕！！）{wait}'
						'{page}'
						'#0304F（我也好想接受\n'
						'\u3000艾欧莉雅小姐的温柔护理啊！）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0211F（……请不要莫名其妙地兴奋起来。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(19)),
					Insn('0x4C', Char(71), -1),
					Insn('0x4C', Char(11), -1),
				]),
				(None, [
					Insn('TEXT_TALK', Char(71), Text(
						'#08714F啊～！！\n'
						'这不是小缇欧和各位嘛！{wait}'
						'{page}'
						'#08712F呵呵，稍等一下哦。\n'
						'等我的工作结束之后，\n'
						'就把满腔的爱意献给你㈱{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0206F……恕我谢绝。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][74] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (49870, 1000, 57910), 0),
	Insn('CAM_ROTATE', 64, 30, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 20540, 0),
	Insn('CHAR_SET_POS', Char(257), (48800, 0, 57000), 0),
	Insn('CHAR_SET_POS', Char(258), (50000, 0, 57000), 0),
	Insn('CHAR_SET_POS', Char(259), (48800, 0, 55500), 0),
	Insn('CHAR_SET_POS', Char(260), (50000, 0, 55500), 0),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('SLEEP', 500),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P……唔，只是这种无关紧要的请求，\n'
		'他们真的会来吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P果然还是应该\n'
		'去拜托游击士吗……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P不过，我又不想因为这种\n'
		'程度的小事而花费米拉……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0006F（呃，不太好搭话呢……）{wait}'
		'{page}'
		'#0000F那、那个……\n'
		'我们是克洛斯贝尔警察局\n'
		'特务支援课的成员……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(12), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_SET_FRAME', Char(12), 1),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P哦哦……你们来了啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P我一直在等你们呢，\n'
		'来来，快过来坐。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0003F不用了，我们站着就行。{wait}'
		'{page}'
		'#0000F可以请您将委托内容\n'
		'详细说给我们听听吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P嗯，好、好的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P……咳咳。\n'
		'那个，所谓的委托其实很简单。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P这次内科研究中，需要用到一种药草，\n'
		'希望你们能帮我取来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P它的名字叫做『羽扇豆草』……\n'
		'如今已是一种\n'
		'很稀少的药草了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0205F说到羽扇豆的话……\n'
		'就会让人联想起流经\n'
		'克洛斯贝尔港湾区的『羽扇河』呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0300F您是想让我们去采摘\n'
		'那种珍奇的药草吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P不，严格来说并非如此。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P其实，这种药草在\n'
		'克洛斯贝尔大教堂有少量储备。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P我已经和艾拉尔达大主教\n'
		'联系过了，希望你们\n'
		'能作为我的代理人，去帮我取来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P……其实本来应该由我亲自去的……\n'
		'嗯……不过因为有些忙嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0005F……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0100F原来如此，我们知道了。\n'
		'去找克洛斯贝尔大教堂的\n'
		'艾拉尔达大主教就可以了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P嗯，那就拜托你们了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P拿到『羽扇豆草』之后，\n'
		'请把它拿到我这里来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 80, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}任务【稀有药草的回收】{color 0}开始！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (50500, 1000, 57500), 0),
	Insn('CAM_ROTATE', 45, 28, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 22000, 0),
	Insn('QUEST', 19, Insn('TASK_SET', 0)),
	Insn('CHAR_SET_POS', Char(0), (50500, 0, 57500), 0),
	Insn('CHAR_SET_POS', Char(1), (50500, 0, 57500), 0),
	Insn('CHAR_SET_POS', Char(2), (50500, 0, 57500), 0),
	Insn('CHAR_SET_POS', Char(3), (50500, 0, 57500), 0),
	Insn('SLEEP', 500),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][75] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (49870, 1000, 57910), 0),
	Insn('CAM_ROTATE', 64, 30, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 20540, 0),
	Insn('CHAR_SET_POS', Char(257), (48800, 0, 57000), 0),
	Insn('CHAR_SET_POS', Char(258), (50000, 0, 57000), 0),
	Insn('CHAR_SET_POS', Char(259), (48800, 0, 55500), 0),
	Insn('CHAR_SET_POS', Char(260), (50000, 0, 55500), 0),
	Insn('CHAR_SET_FRAME', Char(12), 1),
	Insn('SLEEP', 500),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P哦，是你们啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P已经帮我把羽扇豆草\n'
		'顺利取来了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0000F嗯，已经拿来了。{wait}'
		'{page}'
		'这就是我们取来的物品。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'交出了{item 833}{color 0}。{wait}'
	)),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_WAIT'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_RESET', b'\x00'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_REMOVE', 833, 1),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P嗯，就是它，\n'
		'我要向你们表示感谢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P嗯……嗯……\n'
		'然后，那个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P……艾拉尔达大主教\n'
		'说过什么关于我的话吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0203F……不，并没说什么。{wait}'
		'{page}'
		'#0200F而且他似乎也没有看过\n'
		'教授您写给他的信。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P……唔，果然是这样啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P我等了好久也没有等到\n'
		'回音，就已经想到\n'
		'会是这么一回事了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0301F什么嘛，之前还说已经联系过了，\n'
		'原来是骗人的啊。{wait}'
		'{page}'
		'#0306F我们到了之后，才发现你们根本就\n'
		'没有联系过，紧张得都冒冷汗了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P唔……真抱歉啊，\n'
		'因为有些难以启齿。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P我有些害怕见到大主教，\n'
		'所以没法自己去取，\n'
		'不得已之下，才会拜托你们呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0100F祭司和我们说了很多。{wait}'
		'{page}'
		'他说，艾拉尔达大主教虽然有些顽固，\n'
		'但对拉格教授肯定\n'
		'还是持认同态度的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P是吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P我当然也是一样啊。\n'
		'直到如今，我也非常\n'
		'尊敬艾拉尔达大主教。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P我一直在想，如果有朝一日\n'
		'先进的医疗技术能得到普及，\n'
		'我一定要去向他道歉，并郑重表示感谢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0000F是吗……\n'
		'那真是再好不过了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P……那么，真是\n'
		'给你们添麻烦了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(12), Text(
		'#5P以后也请多多关照。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0000F嗯，我们随时恭候。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 9, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}任务【稀有药草的回收】{color 0}完成！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (50500, 1000, 57500), 0),
	Insn('CAM_ROTATE', 45, 28, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 22000, 0),
	Insn('QUEST', 19, Insn('TASK_SET', 3)),
	Insn('QUEST', 19, Insn('FLAG_UNSET', 16)),
	Insn('CHAR_SET_POS', Char(0), (50500, 0, 57500), 0),
	Insn('CHAR_SET_POS', Char(1), (50500, 0, 57500), 0),
	Insn('CHAR_SET_POS', Char(2), (50500, 0, 57500), 0),
	Insn('CHAR_SET_POS', Char(3), (50500, 0, 57500), 0),
	Insn('SLEEP', 500),
	Insn('CHAR_SET_FRAME', Char(12), 0),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][76] = [
	Insn('0x4B', Char(8), -1),
	Insn('0x4B', Char(21), -1),
	Insn('CHAR_WATCH', Char(8), Char(0), 0),
	Insn('CHAR_WATCH', Char(0), Char(8), 0),
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (15620, 400, 7920), 0),
	Insn('CAM_ROTATE', 45, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 25000, 0),
	Insn('CHAR_SET_POS', Char(257), (14410, 0, 6710), 90),
	Insn('CHAR_SET_POS', Char(258), (13420, 0, 4760), 90),
	Insn('CHAR_SET_POS', Char(259), (12160, 0, 4910), 90),
	Insn('CHAR_SET_POS', Char(260), (12810, 0, 6540), 90),
	Insn('CHAR_SET_POS', Char(8), (17210, 0, 7430), 266),
	Insn('CHAR_SET_POS', Char(21), (11940, 1230, 16600), 0),
	Insn('CHAR_FLAG1_SET', Char(21), 64),
	Insn('CHAR_FLAG1_UNSET', Char(21), 4),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(38), 128),
	Insn('CHAR_FLAG2_SET', Char(38), 32768),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P哎呀……医生到底去哪里了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0001F榭拉小姐，您好。{wait}'
		'{page}'
		'我们是接到了支援请求而来的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(8), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P特务支援课的诸位……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P太好了，\n'
		'你们能来，可真是帮了我大忙。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(0), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(1), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(2), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(3), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(0)),
	Insn('EMOTE_STOP', Char(1)),
	Insn('EMOTE_STOP', Char(2)),
	Insn('EMOTE_STOP', Char(3)),
	Insn('SLEEP', 300),
	Insn('EMOTE', Char(8), 0, 2000, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P……嗯，怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0006F那、那个……{wait}'
		'{page}'
		'#0005F委托中好像说一位副教授失踪了，\n'
		'希望我们进行搜寻……对吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#6P#0305F但是，您却这么镇定，\n'
		'让人感觉有些奇怪呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P哦，这个嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P与其说是镇定……\n'
		'倒不如说是\n'
		'已经麻木了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0105F麻、麻木了……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0203F……那个，如果可以的话，\n'
		'请把详细情况告诉我们吧。{wait}'
		'{page}'
		'#0200F看样子，这和我们所想像的失踪事件\n'
		'似乎在严重程度上有很大差距呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P嗯，好的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P失踪的那位\n'
		'副教授名叫\n'
		'约亚西姆丄琼塔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P约亚西姆医生他，那个……\n'
		'虽然是位很优秀的医生，但是\n'
		'偶尔却会突然失踪。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F约亚西姆医生……\n'
		'啊，就是那位蓝色头发，戴眼镜的……{wait}'
		'{page}'
		'#0005F也就是说，那个……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#6P#0306F简单来说，就是偷懒旷工吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P没错，说白了其实就是那样。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P今天也是，把大量的工作丢下不管，\n'
		'不知跑到哪里去了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0106F……就是说……{wait}'
		'{page}'
		'#0100F约亚西姆医生只是不知道\n'
		'跑到哪里去玩了……\n'
		'是这样吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P就、就是这样啦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P对不起，我把委托写成\n'
		'『行踪不明』，\n'
		'也许是有些轻率了。{wait}'
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
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F……要怎么办呢，各位？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0203F……说实话，我觉得这个不妨延后处理。{wait}'
		'{page}'
		'#0200F从了解到的情报来看，\n'
		'紧急性似乎很低呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#6P#0306F但毕竟是榭拉小姐的请求，\n'
		'我还是很想帮忙的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0105F不过，那位医生也许真的被卷入到\n'
		'某些事件中了呢。以防万一，或许还是应该……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(21), Translate('男人的声音'), Text(
		'#4S榭、榭──榭拉小姐！！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(8), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(0), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(1), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(2), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(3), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 500),
	Insn('FORK', 0, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK', 1, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK', 2, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK', 3, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_LOOP', 8, 1, [
		Insn('CHAR_WATCH', Char(254), Char(21), 500),
	]),
	Insn('CAM_OFFSET', (14200, 600, 9330), 1500),
	Insn('CAM_ROTATE', 45, 18, 0, 1500),
	Insn('0x6E', 400, 1500),
	Insn('CAM_DISTANCE', 25000, 1500),
	Insn('SLEEP', 1500),
	Insn('CHAR_FLAG1_UNSET', Char(21), 128),
	Insn('0x95', Char(21), (11810, 0, 9710), 7000, 0),
	Insn('FORK', 21, 1, [
		Insn('0x95', Char(254), (13460, 0, 8990), 6000, 0),
	]),
	Insn('CAM_OFFSET', (14770, 600, 8480), 500),
	Insn('CAM_ROTATE', 45, 18, 0, 500),
	Insn('0x6E', 400, 500),
	Insn('CAM_DISTANCE', 25000, 500),
	Insn('SLEEP', 500),
	Insn('FORK_QUIT', Char(8), 1),
	Insn('CHAR_ROTATE', Char(8), 270, 0),
	Insn('TEXT_TALK', Char(21), Text(
		'#5P呼、呼、呼……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P啊……利顿医生，\n'
		'在医院里不可以大声喊叫哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#5P呼、呼……\n'
		'对……对不起……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#6P#0300F啊，这不是之前住院的\n'
		'那位实习医生吗？\n'
		'身体还好吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(21), Char(260), 0),
	Insn('TEXT_TALK', Char(21), Text(
		'#5P……啊，你、你们好。\n'
		'当时可真是多谢了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(21), Char(8), 0),
	Insn('TEXT_TALK', Char(21), Text(
		'#5P……不对！现在不是说这些的时候！\n'
		'榭拉小姐，约亚西姆医生呢！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P那个，对不起。\n'
		'他好像还没回来……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#5P怎、怎么会这样……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#5P呜呜……\n'
		'那么大的工作量，让我这个\n'
		'实习医生如何是好啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(21), Text(
		'#5P……啊啊，没时间在这里抱怨了！\n'
		'再不赶快去处理的话，可就……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_LOOP', 8, 1, [
		Insn('CHAR_WATCH', Char(254), Char(21), 500),
	]),
	Insn('0x95', Char(21), (11810, 0, 9710), 6000, 0),
	Insn('0x95', Char(21), (11940, 1230, 16600), 7000, 0),
	Insn('CHAR_FLAG1_SET', Char(21), 128),
	Insn('SLEEP', 800),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0005F刚、刚才那是……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 200),
	Insn('FORK', 0, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 300),
	]),
	Insn('FORK', 1, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 300),
	]),
	Insn('FORK', 2, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 300),
	]),
	Insn('FORK', 3, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 300),
	]),
	Insn('SLEEP', 100),
	Insn('FORK_QUIT', Char(8), 1),
	Insn('CHAR_ROTATE', Char(8), 270, 300),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P约亚西姆医生经常把\n'
		'工作硬推给利顿医生。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P医生这次偷跑出去，\n'
		'留下的一大堆烂摊子也正是\n'
		'由他在拼命收拾呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0106F真、真是辛苦啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#6P#0306F嗯，看起来，这件事\n'
		'果然还是不能放着不管啊。{wait}'
		'{page}'
		'#0300F其它的先不说，\n'
		'毕竟那个家伙太可怜了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0206F……我也有同感。\n'
		'不过，该说他是倒霉才对吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0006F是啊……{wait}'
		'{page}'
		'#0000F榭拉小姐，关于约亚西姆医生\n'
		'有可能去的地方，\n'
		'您有没有什么线索……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(8), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P啊，诸位愿意接受\n'
		'这个委托吗，\n'
		'真是很感谢你们！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P约亚西姆医生最近好像\n'
		'一直在到处宣扬\n'
		'『要在纪念庆典中参加钓鱼大赛』。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P他这次的行踪或许跟这个大赛\n'
		'有什么关联吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P约亚西姆医生是在\n'
		'工作途中直接偷跑出去的，\n'
		'身上应该还穿着白大褂。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P所以一定比较显眼，即使离很远也能认出来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0006F钓鱼大赛吗……\n'
		'他还真是很喜欢钓鱼啊。{wait}'
		'{page}'
		'#0003F（既然如此，去东侧大道的那个设施里\n'
		'\u3000问问的话，说不定会有什么线索呢。）{wait}'
		'{page}'
		'#0000F……总之，我们正式接受委托。\n'
		'找到他之后，会再与您联系的。\n'
		'可以先在这里等我们的消息吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P明白了，\n'
		'那就拜托各位了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 80, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}任务【搜寻副教授的请求】{color 0}开始！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (14410, 1000, 6710), 0),
	Insn('CAM_ROTATE', 45, 28, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 24000, 0),
	Insn('CHAR_SET_POS', Char(0), (14410, 0, 6710), 90),
	Insn('CHAR_SET_POS', Char(1), (14410, 0, 6710), 90),
	Insn('CHAR_SET_POS', Char(2), (14410, 0, 6710), 90),
	Insn('CHAR_SET_POS', Char(3), (14410, 0, 6710), 90),
	Insn('0x4C', Char(8), -1),
	Insn('0x4C', Char(21), -1),
	Insn('CHAR_FLAG1_UNSET', Char(21), 64),
	Insn('CHAR_FLAG1_SET', Char(21), 4),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(38), 128),
	Insn('CHAR_FLAG2_UNSET', Char(38), 32768),
	Insn('QUEST', 22, Insn('TASK_SET', 0)),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][77] = [
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('EVENT_BEGIN', 0),
	Insn('0x4B', Char(8), -1),
	Insn('0x4B', Char(17), -1),
	Insn('CAM_OFFSET', (15690, 500, 7880), 0),
	Insn('CAM_ROTATE', 51, 20, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 25880, 0),
	Insn('CHAR_SET_POS', Char(257), (14410, 0, 6210), 0),
	Insn('CHAR_SET_POS', Char(258), (13420, 0, 4260), 0),
	Insn('CHAR_SET_POS', Char(260), (12160, 0, 4410), 0),
	Insn('CHAR_SET_POS', Char(259), (12810, 0, 6140), 0),
	Insn('CHAR_SET_POS', Char(8), (17210, 0, 7430), 266),
	Insn('CHAR_SET_POS', Char(17), (13650, 0, 7450), 90),
	Insn('CHAR_FLAG1_SET', Char(17), 64),
	Insn('CHAR_FLAG1_UNSET', Char(17), 128),
	Insn('CHAR_FLAG1_UNSET', Char(17), 4),
	Insn('CHAR_FLAG1_SET', Char(10), 128),
	Insn('CHAR_FLAG2_SET', Char(10), 32768),
	Insn('CHAR_FLAG1_SET', Char(38), 128),
	Insn('CHAR_FLAG2_SET', Char(38), 32768),
	Insn('SLEEP', 500),
	Insn('CAM_DISTANCE', 24880, 2000),
	Insn('FADE_OFF', 2000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P真是的……您之前\n'
		'到底跑到哪里去了啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P因为医生您擅自离开，给别人添了\n'
		'多大的麻烦，您到底知不知道啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(17), Text(
		'#6P#2409F哈哈哈，其实我去参加了一个叫做\n'
		'『费瑟尔杯』的重要比赛呢。{wait}'
		'{page}'
		'#2400F既然我肩负着钓公师团的名誉，\n'
		'就绝对不能错过这种比赛，对不对？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P真是的，您多少也该对本职工作\n'
		'认真一点吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P利顿他直到现在，\n'
		'都在替约亚西姆医生\n'
		'您拼命工作呢！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(17), Text(
		'#6P#2405F哦哦，利顿啊！{wait}'
		'{page}'
		'#2400F哎呀，能有这么一个有出息的学生，\n'
		'我可真是幸福啊。{wait}'
		'{page}'
		'#2403F我现在过去打断他的积极工作也不好……\n'
		'不然，干脆就把剩下的工作\n'
		'都交给他算了～{wait}'
		'{page}'
		'#2409F嗯嗯，果然还是这样最好啊。\n'
		'对他的成长也一定很有帮助……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P#4S#200W请您赶快\n'
		'回去工作好吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(17), Text(
		'#6P#2406F……是。{wait}'
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
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(257), Text(
		'#12P#0006F（这个人……一直\n'
		'\u3000都是那种状态吗？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0200F（既然身为副教授，\n'
		'\u3000应该是一位很优秀的人才对……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0309F（天才和那个什么，其实只有一线之隔吧。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#12P#0106F（喂……会被听到啦。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(17), 180, 300),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(17), Text(
		'#5P#2400F……那么，诸位，\n'
		'我就此失陪啦。{wait}'
		'{page}'
		'#2409F如果今后再有机会，\n'
		'我们还要一起去享受钓鱼的乐趣哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_LOOP', 0, 1, [
		Insn('CHAR_WATCH', Char(254), Char(17), 300),
	]),
	Insn('FORK_LOOP', 1, 1, [
		Insn('CHAR_WATCH', Char(254), Char(17), 300),
	]),
	Insn('FORK_LOOP', 2, 1, [
		Insn('CHAR_WATCH', Char(254), Char(17), 300),
	]),
	Insn('FORK_LOOP', 3, 1, [
		Insn('CHAR_WATCH', Char(254), Char(17), 300),
	]),
	Insn('FORK_LOOP', 8, 1, [
		Insn('CHAR_WATCH', Char(254), Char(17), 300),
	]),
	Insn('0x95', Char(17), (11810, 0, 9710), 2000, 0),
	Insn('0x95', Char(17), (11940, 1230, 16600), 2000, 0),
	Insn('CHAR_FLAG1_SET', Char(17), 128),
	Insn('SLEEP', 800),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P……还要？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_QUIT', Char(0), 1),
	Insn('FORK_QUIT', Char(1), 1),
	Insn('FORK_QUIT', Char(2), 1),
	Insn('FORK_QUIT', Char(3), 1),
	Insn('FORK', 0, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 300),
	]),
	Insn('FORK', 1, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 300),
	]),
	Insn('FORK', 2, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 300),
	]),
	Insn('FORK', 3, 1, [
		Insn('CHAR_ROTATE', Char(254), 90, 300),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F那、那个……\n'
		'请您不必在意。{wait}'
		'{page}'
		'#0000F总之……\n'
		'这样应该就算是\n'
		'完成任务了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_QUIT', Char(8), 1),
	Insn('CHAR_ROTATE', Char(8), 270, 300),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P嗯，是的。\n'
		'真是非常感谢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P医生能这么快就\n'
		'回到这里，\n'
		'全都是诸位的功劳。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P如果今后再有什么问题，\n'
		'欢迎随时光临本院。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(8), Text(
		'#11P我们一定会诚心诚意地\n'
		'为您服务。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F嗯，到时候就要麻烦你们了。\n'
		'……那么，我们告辞了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('SOUND_PLAY', 9, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 2}任务【搜寻副教授的请求】{color 0}完成！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (14410, 1000, 6710), 0),
	Insn('CAM_ROTATE', 45, 28, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 24000, 0),
	Insn('CHAR_SET_POS', Char(0), (14410, 0, 6710), 90),
	Insn('CHAR_SET_POS', Char(1), (14410, 0, 6710), 90),
	Insn('CHAR_SET_POS', Char(2), (14410, 0, 6710), 90),
	Insn('CHAR_SET_POS', Char(3), (14410, 0, 6710), 90),
	Insn('0x4C', Char(8), -1),
	Insn('0x4C', Char(17), -1),
	Insn('CHAR_FLAG1_UNSET', Char(17), 64),
	Insn('CHAR_FLAG1_SET', Char(17), 4),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG2_UNSET', Char(10), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(38), 128),
	Insn('CHAR_FLAG2_UNSET', Char(38), 32768),
	Insn('QUEST', 22, Insn('FLAG_UNSET', 16)),
	Insn('QUEST', 22, Insn('TASK_SET', 6)),
	Insn('FLAG_SET', Flag(0)),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][78] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CAM_OFFSET', (55410, 1000, -55440), 0),
	Insn('CAM_ROTATE', 55, 15, 0, 0),
	Insn('0x6E', 440, 0),
	Insn('CAM_DISTANCE', 18950, 0),
	Insn('CHAR_SET_POS', Char(257), (55250, 0, -54750), 135),
	Insn('CHAR_SET_POS', Char(258), (54080, 0, -54680), 90),
	Insn('CHAR_SET_POS', Char(259), (54670, 0, -57660), 45),
	Insn('CHAR_SET_POS', Char(260), (53490, 0, -57740), 45),
	Insn('CHAR_SET_POS', Char(265), (52630, 0, -56430), 90),
	Insn('CHAR_FLAG1_UNSET', Char(4), 128),
	Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
	Insn('CHAR_ROTATE', Char(19), 270, 0),
	Insn('CHAR_SET_FRAME', Char(19), 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11P呼啊啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11P昨天我通宵研究了\n'
		'医疗器械呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11P虽然想出了非常方便的\n'
		'可携式设计，\n'
		'但是进行得并不顺利……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0005F（这个人……\n'
		'\u3000是负责开发医疗器械的啊。）{wait}'
		'{page}'
		'#0003F（对了！要帮小滴\n'
		'\u3000找的礼物材料……\n'
		'\u3000她这里或许会有什么合适的东西吧。）{wait}'
		'{page}'
		'#0000F那个……打扰一下。\n'
		'可以和您说几句话吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11P啊？有什么事吗？{wait}'
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
		'#5P#0000F……事情就是这样，\n'
		'如果您有什么不需要的东西，\n'
		'可以送给我们吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11P啊，原来如此，\n'
		'想亲手给父亲做礼物，\n'
		'小滴她还真是很可爱呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11P这个嘛，嗯……\n'
		'这个东西应该很合适吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('SOUND_PLAY', 17, 0, 0, 100),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'收下了{item 834}{color 0}。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('0x5A'),
	Insn('ITEM_ADD', 834, 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0005F这是……\n'
		'可以镶嵌宝石的\n'
		'挂坠扣吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11P嗯，没错。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11P这是我在研究\n'
		'『坠饰型可携式医疗器械』的过程中，\n'
		'失败之后得到的副产品。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0205F可携式医疗器械……\n'
		'竟然还出了那种东西吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11P不不，目前还只是试制品而已，\n'
		'还无法投入到实际应用中呢～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11P使用带有治疗效果的结晶回路，\n'
		'通过它来促进身体的自愈能力。\n'
		'这就是我的构想。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0305F呼……\n'
		'真不愧是乌尔斯拉医院，\n'
		'所做的研究都很厉害啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#6P#0500F如果以后能成为警备队的\n'
		'实战装备，应该会非常有用吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#6P#0105F不过，您刚才好像说，\n'
		'实验失败了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11P嗯，昨天晚上，\n'
		'我试着做出了试制品……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11P但不知是哪里出了差错，\n'
		'将做完的试制品启动之后，\n'
		'竟然发生了爆炸。{wait}'
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
	Insn('EMOTE', Char(4), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0006F啊，真危险啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11P不过，那个挂坠扣\n'
		'当时就在爆炸的正中心，\n'
		'结果却奇迹般地毫无伤痕呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11P运气这么好的东西，\n'
		'一定很适合作为制作礼物的材料吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0006F（身为研究医疗器械的人，\n'
		'\u3000说的话还真是缺乏科学性啊……）{wait}'
		'{page}'
		'#0000F……那么，非常感谢您。\n'
		'我们就不客气地收下了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(19), Text(
		'#11P收下吧～收下吧～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 4))), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0003F（把小滴的\n'
				'\u3000石头镶嵌在里面，\n'
				'\u3000就可以做成护身符了吧。）{wait}'
				'{page}'
				'#0000F（只要再有个链子之类的东西，\n'
				'\u3000就能做成一条漂亮的\n'
				'\u3000项链了。）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('QUEST', 44, Insn('TASK_SET', 2)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 0))), Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 1))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 2))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 44, Insn('TASK_GET', 4))), Insn('BOOL_AND'), Insn('END')]), [
			Insn('QUEST', 44, Insn('TASK_SET', 5)),
			Insn('TEXT_TALK', Char(257), Text(
				'#5P#0000F（制作礼物的材料收集齐了，\n'
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
	Insn('CHAR_ROTATE', Char(19), 90, 0),
	Insn('CHAR_SET_POS', Char(0), (54500, 0, -55500), 90),
	Insn('CHAR_SET_POS', Char(1), (54500, 0, -55500), 90),
	Insn('CHAR_SET_POS', Char(2), (54500, 0, -55500), 90),
	Insn('CHAR_SET_POS', Char(3), (54500, 0, -55500), 90),
	Insn('CHAR_FLAG1_SET', Char(4), 128),
	Insn('CHAR_FLAG2_SET', Char(4), 32768),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][79] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 11))), Insn('NOT'), Insn('END')]), [
			Insn('EVENT_BEGIN', 0),
			Insn('FADE_ON', 1000, Color(0x00000000), 255),
			Insn('0x0D'),
			Insn('CHAR_ROTATE', Char(8), 270, 0),
			Insn('CHAR_SET_POS', Char(0), (14380, 0, 8029), 90),
			Insn('CHAR_SET_POS', Char(1), (14380, 0, 6830), 90),
			Insn('CHAR_SET_POS', Char(2), (13180, 0, 8029), 90),
			Insn('CHAR_SET_POS', Char(3), (13180, 0, 6830), 90),
			Insn('CAM_OFFSET', (15460, 1000, 7600), 0),
			Insn('CAM_ROTATE', 45, 28, 0, 0),
			Insn('0x6E', 440, 0),
			Insn('CAM_DISTANCE', 18000, 0),
			Insn('CAM_DISTANCE', 16000, 1000),
			Insn('FADE_OFF', 1000, Color(0x00000000)),
			Insn('0x0D'),
			Insn('0x6F', b'y'),
			Insn('TEXT_TALK', Char(8), Text(
				'啊，罗伊德先生！\n'
				'你查到亚苏拉主任的\n'
				'下落了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0001F不，还没。\n'
				'目前正打算\n'
				'将院区内都搜索一遍……{wait}'
				'{page}'
				'#0002F对了，你今天早上\n'
				'有看到主任走过去吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'没有，我没看到。\n'
				'至少在我来之后都没看到。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'不过，我来也是\n'
				'早上七点之后的事了。{wait}'
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
				'#0000F也就是说，七点以前\n'
				'你也不清楚吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'是。\n'
				'克拉克事务长和我\n'
				'都是早上七点之后的班。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0303F那就算主任早上七点之前\n'
				'真的经过这里也没有人知道吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'但我想这点应该不用担心。\n'
				'因为如果主任会七点以前起床……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'#5S天\u3000就\u3000要\u3000塌\u3000下\u3000来\u3000了\u3000！#3S{wait}'
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
				'#0106F看来她睡过头的问题真的……\n'
				'很严重呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_SET_POS', Char(0), (14380, 0, 7430), 90),
			Insn('EVENT_END', 5),
			Insn('QUEST', 56, Insn('TASK_SET', 11)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(8), Text(
				'我们站在这里是\n'
				'七点之后的事了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'所以，如果主任在那之前\n'
				'真的有经过这里，\n'
				'我们也无从得知……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(8), Text(
				'但如果主任会七点以前起床……\n'
				'天就要塌下来了！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('RETURN'),
]

data['code'][80] = [
	Insn('TEXT_TALK', Char(9), Text(
		'亚苏拉主任……\n'
		'真教人担心。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(9), Text(
		'请你们一定要\n'
		'尽快找到主任！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('RETURN'),
]

data['code'][81] = [
	Insn('0x4B', Char(19), -1),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('CHAR_WATCH', Char(19), Char(15), 0),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
			Insn('FLAG_SET', Flag(4)),
			Insn('TEXT_TALK', Char(15), Text(
				'以后会注意……吗。\n'
				'这句话还真是万能呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'回想起来，你好像从学生时代开始\n'
				'就老是在重复这句话呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'但说来也奇怪，\n'
				'你的生活态度完全没有改进，\n'
				'看起来也没有想改的意愿。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'想想也挺了不起的呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(19), Text(
				'对、对不起……\n'
				'不小心就忘记了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(19), Text(
				'我这次绝对会好好反省。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(15), Text(
				'这句话我也听好几次了。\n'
				'……你从学生时代开始\n'
				'就一点也没变呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_WATCH', Char(19), Char(0), 300),
	Insn('TEXT_TALK', Char(19), Text(
		'（呜呜……凯瑞教授\n'
		'\u3000就是不肯放过我……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(15), 0, 2000, (12, 13, 250, 2)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(15), Text(
		'#4S……你有在听吗，亚苏拉！#3s{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(19), Char(15), 1000),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(19), Text(
		'有、有的！\n'
		'我以后一定会注意！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4C', Char(19), -1),
	Insn('CHAR_SET_FRAME', Char(15), 0),
	Insn('RETURN'),
]
