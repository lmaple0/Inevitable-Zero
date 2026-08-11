# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'c0100',
	'name2': 'c0100',
	'location': 4,
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
	'name3': 'c0100_1',
	'labels': [],
	'chcp': [],
	'npcs': [],
	'monsters': [],
	'triggers': [],
	'objects': [],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01L\x04\x00\x00\x00\x00\x00\x00T\xf2\xff\xff\x00\x00\x00\x00\x01\x00\x04\x00', Function((0, 5)), Function((0, 6))),
	'code': [None]*18,
	'anim': [],
}

data['code'][0] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天的东西已经都买完了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'按照预定计划完成目标，\n'
				'心情真是不错啊～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'呼啊……早安啊～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'希望今天也是不错的一天啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'港湾区那边人山人海啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'连警察都来了，\n'
						'总觉得气氛好像有点恐怖，\n'
						'是不是发生什么事了啊～？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'港湾区那里好像出了什么事，\n'
						'……希望不是什么恐怖的事件啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1550)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'不知怎么回事，预算会议\n'
				'好像要延长了呢～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'算了，反正好像每年\n'
				'都会像这样推延……\n'
				'大家都已经不会很在意了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'纪念庆典最终日的时候，\n'
						'我在米修拉姆看了烟火哦，\n'
						'真漂亮呀～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过，听说那天晚上发生了骚乱，\n'
						'真是够危险的啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'拿不出在米修拉姆住宿的钱，\n'
						'反而算是走运呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'听说在纪念庆典最终日那晚，\n'
						'米修拉姆发生了骚乱。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我在那之前就回去了，或许算是幸运的呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'麦克道尔市长\n'
						'给人的感觉是个非常\n'
						'严肃正派的老爷爷啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽然是政治家，但却很亲切，\n'
						'而且好像还很有活力呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过……他一直都拄着\n'
						'根拐杖呢。\n'
						'身体果然还是不太好吗～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'爸爸说麦克道尔市长今年\n'
						'就要退休了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但那是真的吗～？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'今年的纪念庆典将会\n'
						'是什么样子的呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'所有的店铺好像都在\n'
						'为庆典做准备呢，\n'
						'呵呵，真是期待呀～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔最盛大的庆典活动──\n'
						'创立纪念庆典已经临近了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，好期待啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'买完东西后才发现天已经快黑了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我只要一进入商店，\n'
				'就会不知不觉逛上很长时间呢～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天看到了好多警察啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'从早上到现在就遇到了五六个。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'似乎也没有什么事件\n'
				'发生啊……\n'
				'到底是怎么了呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'唉～最后也还是没能弄到\n'
						'彩虹剧团的门票。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我和朋友两个人都已经\n'
						'很努力地排队了～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'就在只剩下五个人就排到我们时，\n'
						'票便全部卖光了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呜呜，真是很受打击啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'啊啊啊！光是回忆一下就好不甘心～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'而且那里的门票\n'
						'未免太贵了吧！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'就算把零用钱全部都贴进去\n'
						'好像也不够。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'据说阿尔摩利卡村产的蔬菜\n'
				'对健康大有益助呢，{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'能让皮肤变得润滑透亮，\n'
				'我也吃吃看好了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'今天准备去西侧大道的亲戚\n'
						'家里玩。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过市内没有\n'
						'巴士可以坐啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真是不方便。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔市很广阔的，\n'
						'我觉得市内也应该通车\n'
						'才对。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'刚才看到一辆绿色的大车开过去了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'车身还印有克洛斯贝尔警备队的徽章呢，\n'
				'车上的是不是警备队的人呢～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'本来想和朋友找个\n'
						'公寓住的……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但是都没有找到便宜的\n'
						'房子啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'看来还是要和父母一起住，\n'
						'暂时就别想独立了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'最近的经济很景气，\n'
						'房租也都变得很高。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呼，实在不行的话，\n'
						'是不是要考虑找人分租了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'我的爸爸在大公司里\n'
						'上班……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'说是公司里最近设置了\n'
						'叫做『导力网络』的东西。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过爸爸弄不懂使用方法，\n'
						'每天都很郁闷呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'真是的，爸爸好没用哦～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(0)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'『导力网络』这种东西，好像\n'
						'是种非常便利的装置……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但要是不知道使用方法，\n'
						'那不还是和没有一样嘛～{wait}'
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

data['code'][1] = [
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
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'听说延迟了很久的预算会议\n'
				'总算是结束了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'后天要向市民发表结果……\n'
				'哎呀呀，最后会是如何呢～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'和去年相比，希望至少也能\n'
				'通过一些浪费比较少的\n'
				'预算案啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'预算会议好像在今天\n'
				'就能结束了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'今年似乎比往年\n'
				'拖得都要长呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'你们听说了吗，黑手党之间开战的传闻……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'真是令人厌恶啊……\n'
				'在以前，如果发生了这种事件，\n'
				'往往都会死人的。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'本以为克洛斯贝尔多少也都\n'
				'变得和平一些了，\n'
				'但看来还是不能安心啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1550)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'通向玛因兹矿山镇的隧道内有条岔路，\n'
						'岔路的尽头有个遗迹。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'传说每到满月之夜，那里就会响起\n'
						'美妙的钟声哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那处遗迹好像是在中世纪建造的建筑，\n'
						'除此之外就一无所知了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'通向玛因兹矿山镇的隧道内有条岔路，\n'
						'岔路的尽头有个遗迹。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'传说每到满月之夜，那里就会响起\n'
						'美妙的钟声哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'从明天开始，预算会议就要在\n'
						'市政厅召开了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那是决定克洛斯贝尔的各种公共事业\n'
						'预算的重要会议……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'但是每年都没法在\n'
						'预定的结束日顺利得出结论。\n'
						'今年又会如何呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔的预算会议\n'
						'每年都迟迟得不出结论。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'大概是市长与议长的对立\n'
						'延迟了决议吧。\n'
						'今年又会如何呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'位于克洛斯贝尔市南部的\n'
						'『星见之塔』据说是个建造于\n'
						'中世纪的建筑。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔似乎从那时开始就是个\n'
						'充斥着交易与战乱的地区。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'传闻说，那是当时的掌权者\n'
						'为了进行占星术\n'
						'而下令建造的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'据说『星见之塔』是中世纪时\n'
						'为了占星术而建造的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不过，这种说法并没有\n'
						'什么实际依据，\n'
						'连真伪都无法断定。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'ＩＢＣ的总裁迪塔先生，\n'
				'一直都是支撑着克洛斯贝尔的\n'
				'经济界第一人。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'他并不只会赚钱，\n'
				'对公共事业和慈善丄支援机关\n'
				'也积极捐款。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'虽说是人无完人……\n'
				'但感觉迪塔先生好像\n'
				'真的是个非常完美的人啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'那么，我差不多也该回去了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'总是在这种地方待着，\n'
				'说不定会感冒呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'彩虹剧团那传闻中的新剧，\n'
				'听说第二主角会由新人出演。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'如果那新人真如传闻所说，是被\n'
				'那个伊莉雅丄普拉提耶亲自发掘的，\n'
				'那应该是个具有相当实力的人吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'住在克洛斯贝尔的人\n'
				'最喜欢热闹场面。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'特别是像庆典这样的活动，\n'
				'无论老少，全都会因此而热情高涨。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'下个月举办的将是７０周年的创立纪念庆典。\n'
				'今年到底会热闹到什么程度呢？我非常期待啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'《彩虹剧团》可是克洛斯贝尔\n'
				'引以为傲的明星集团。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'在国外的名流阶层中都很受欢迎，\n'
				'听说偷偷潜入自治州来欣赏的人\n'
				'也都不在少数呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'前段时间，我在小巷那边\n'
						'发现了一家\n'
						'诡异的古董店。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'店里陈列着各种奇怪的商品，\n'
						'店主老婆婆也给人一种\n'
						'很奇怪的感觉。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'前段时间，我在小巷那边\n'
						'发现了一家\n'
						'诡异的古董店。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'唔……以前有那样\n'
						'一家店吗。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔的人\n'
						'最喜欢各种小道传闻了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'光是每天出门散散步，\n'
						'就能听到不少消息呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'从事件的背后隐情\n'
						'到外国的经济动向……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'在克洛斯贝尔，\n'
						'能打听到所有情报，\n'
						'这么说都不过分。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔的人\n'
						'最喜欢各种小道传闻了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵，毕竟是一直都从事着贸易业的\n'
						'人民啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'鲁巴彻商会的那群家伙\n'
						'在很早以前就在克洛斯贝尔扎根了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……也就是所谓的黑手党啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'可悲的是，警察根本就\n'
						'没有办法将他们取缔。\n'
						'你们还是不要和他们扯上关系为好。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'连警察都制裁不了\n'
						'鲁巴彻商会，\n'
						'……你们还是不要和他们扯上关系为好。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'百货的翻修，\n'
						'还有全新的导力商店……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔的街道格局\n'
						'可真是日新月异啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'这虽然是好事，\n'
						'但也让人看得眼花缭乱，\n'
						'似乎一不小心就会迷路呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'街道的格局变化如此之大，\n'
						'连我这种土生土长的克洛斯贝尔人\n'
						'一不小心都会迷路呢。{wait}'
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

data['code'][2] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'刚才有警察从机场那边\n'
				'撤离呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'好像在说什么\n'
				'爆炸物之类的东西……\n'
				'嗯嗯，果然是很危险啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'警车慌慌张张地\n'
						'往机场那边驶去了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'是不是发生什么事了？\n'
						'总有种不好的预感啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'警察一慌张，\n'
						'就肯定不会有什么好事。\n'
						'总有不好的预感呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'你们听说……港湾区的事件了吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……看来以后不能让小孩子\n'
						'跑太远了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'咪咪，不要从爸爸的\n'
						'身边离开哦！不然会\n'
						'很危险的～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1550)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'在导力车已经普及的今天，\n'
				'我认为应该积极对\n'
				'道路进行整顿。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'特别是中央广场的人流量很大，\n'
				'如果有投入预算，\n'
				'真希望能把道路扩张一下啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_WATCH', Char(254), Char(339), 0),
					Insn('TEXT_TALK', Char(254), Text(
						'啊呀，你是……\n'
						'特务支援课的那个孩子吧？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'如果愿意的话，和我家咪咪\n'
						'也做个好朋友吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(339), Text(
						'#1109F嗯，好呀～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0002F（这么快就能和对方混熟…\n'
						'\u3000也是天性使然吧……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('CHAR_WATCH', Char(254), Char(339), 0),
					Insn('TEXT_TALK', Char(254), Text(
						'你和我家咪咪差不多大吧？\n'
						'愿意的话，你们就做个好朋友吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'纪念庆典期间，市内的交通状况\n'
				'实在是令人担忧啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'有不少游客都是开着导力车\n'
				'来克洛斯贝尔的，但愿他们\n'
				'不要做出什么出格行为……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'好像有很多媒体行业的人\n'
						'被招待去欣赏彩虹剧团的\n'
						'新剧预演了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'他们都能抢先享受到\n'
						'新剧的舞台吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'稍微有点羡慕呢，哈哈哈。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'再过不久就是彩虹的新剧预演了……\n'
						'虽然明知道自己无缘欣赏，\n'
						'但还是很兴奋啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), [
			Insn('CHAR_WATCH', Char(254), Char(11), 0),
			Insn('TEXT_TALK', Char(254), Text(
				'喂～咪咪，\n'
				'天色已经变暗了，\n'
				'差不多也该回去啦～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'彩虹剧团的新剧码\n'
				'好像是『金之太阳、银之月』吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'能看到那个伊莉雅丄普拉提耶，\n'
				'一定很令人期待吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过，因为我没有买到票……\n'
				'所以只能通过写真集来一饱眼福了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'彩虹剧团公演的门票，\n'
						'连我都没有买到呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'百货的门口排起了长龙，\n'
						'听说其它售票处也都在转瞬之间\n'
						'就把票都给卖光了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'本来还想让咪咪也见识一下\n'
						'伊莉雅丄普拉提耶的精彩表演呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'没办法了，等两个月之后\n'
						'再碰碰运气吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'如果想成为导力车的驾驶员，\n'
				'只要在政府部门办理正式的手续就行了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'但现在似乎有很多驾驶技术\n'
				'不佳的人开车上路呢，\n'
				'撞车事故也时有发生。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我觉得还是应该对驾照的发放\n'
				'设立更严格的标准。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'你们几个……莫非是\n'
						'被人用导力车送回来的吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'…………………………{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呀，没什么，我只是有点羡慕而已啦。\n'
						'哈哈哈……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'刚才那辆导力车是\n'
						'共和国的乌尔努公司制造的哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'虽说只是价格最实惠的\n'
						'一款车型……\n'
						'但有车果然就是好啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'随着导力车的普及，\n'
						'违规停车渐渐也成了隐患。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'随便停在路边的话，不是会给后面的车辆\n'
						'与行人造成很大麻烦吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'道路是我们大家的，\n'
						'希望每个人都能严格遵守规则啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(2)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'违规停车也成问题了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'道路是我们大家的，\n'
						'希望每个人都能严格遵守规则啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我是城市规划课的，\n'
				'负责交通流量的调查。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……话虽如此，但今天是和女儿一起\n'
				'出来玩的，所以彻底放假呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'这里是克洛斯贝尔地区\n'
				'人流量最大的广场哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'夕阳好美啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'该和爸爸一起回家啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'小孩子该回去了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'早安～罗伊德哥哥，还有大家！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'特务支援课今天也有工作吗？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F嗯，算是有一点呢。\n'
						'……话说回来……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0300F哈哈，终于把我们\n'
						'给记住了呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哎～？\n'
						'咪咪至今为止，可是\n'
						'连一次都没有说错过吧～？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F嗯、嗯～\n'
						'算了，\n'
						'就当是这样好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0202F玩的时候要注意车哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯！大家工作也要加油哦！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'特务支援课的各位，\n'
						'工作要加油啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'不知道为什么，爸爸今天\n'
				'好严厉呀～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不过，他说那都是为了咪咪好，\n'
				'所以咪咪会乖乖听话的～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1550)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天琪雅没和你们\n'
				'在一起吗～？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哎，本来还想叫她一起玩呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_WATCH', Char(254), Char(339), 0),
					Insn('TEXT_TALK', Char(254), Text(
						'咦，不认识的孩子呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'好羡慕哦～罗伊德大哥哥他们\n'
						'在陪你一起玩吗～？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(339), Text(
						'#1104F嘿嘿，羡慕吧～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(1))), Insn('CONST', 1), Insn('NEG'), Insn('NE'), Insn('END')]), [
							Insn('TEXT_TALK', Char(258), Text(
								'#0106F其实不是在玩啊……{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(2))), Insn('CONST', 1), Insn('NEG'), Insn('NE'), Insn('END')]), [
							Insn('TEXT_TALK', Char(259), Text(
								'#0206F这并不是在玩呢……{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('TEXT_TALK', Char(260), Text(
								'#0306F这哪里像是在玩啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F嗯～不过，这一个星期确实……{wait}'
						'{page}'
						'只要跟琪雅在一起，\n'
						'就会不知不觉地玩起来了呢……\n'
						'……必须要注意一点了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'喂，下次也和我一起玩吧～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(339), Text(
						'#1109F嘿嘿嘿，好呀～！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'那边的那个姐姐，\n'
				'说她会在庆典期间开店呢～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'咪咪还没吃过爆米花哦，\n'
				'所以很期待的～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'爸爸还有市里的大家\n'
				'好像都很在意下个月的庆典。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'到时肯定会有很多\n'
				'有趣的活动吧！\n'
				'咪咪也很期待～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎～还想再多玩一会呢！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'爸爸好像没有抢到\n'
				'彩虹剧团的票。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'哈，那也是没办法的事啊，\n'
				'毕竟彩虹剧团的公演那么受欢迎。\n'
				'咪咪倒是不在意有没有票～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊，是罗伊德哥哥还有大家。\n'
						'你们好呀～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F你好啊。\n'
						'哈哈，最近终于能把我的\n'
						'名字记住了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'记住了呀～\n'
						'特务支援课的\n'
						'罗伊德哥哥一行！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0106F嗯、嗯～\n'
						'看来还是没能把『特务支援课』\n'
						'这个全名记住呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F……话说回来……\n'
						'人名好像也只记住了\n'
						'罗伊德前辈一个人的啊……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0303F哼哼哼……罗伊德，真有一手啊。\n'
						'竟然把本大爷撇在一边，\n'
						'让这位年幼的小姐只对你一个人留下印象……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0011F你、你在说什么梦话呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'特务支援课的各位，\n'
						'今天在做什么工作呢？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'咪咪会声援你们的，所以一定要加油哦～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天天气也很好啊～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'要小心路上的车子啊～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊！特务……\n'
						'………特务什么课的哥哥姐姐们！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'辛苦啦～！\n'
						'要加油工作哦～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0002F哈哈，谢谢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0106F（还是没能把名字\n'
						'\u3000给记住啊……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'我爸爸他啊，一直都\n'
						'梦想着买一辆导力车。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'总是拿着车子的目录，\n'
						'研究个没完～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊，你们好啊！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F嗯，你好。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哎～那个……\n'
						'特务……特务……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F……是特务支援课。\n'
						'呵，这名字可能是有些拗口。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'是特务炫课对吧！\n'
						'咪咪记住啦～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'今天也要加油工作呀～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0106F感、感觉稍微有点不对……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0300F算了，毕竟才刚刚一个月。\n'
						'慢慢总会记住的，这样就行了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'特务炫课的各位～\n'
						'今天也要加油工作呀～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嘟嘟～嘟嘟……\n'
				'很多车子开过去了哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'知道吗？\n'
				'这里可是克洛斯贝尔\n'
				'车子最多的地方。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('EMOTE', Char(254), 0, 2000, (38, 38, 250, 1)),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(254), Text(
						'啊，你们好！\n'
						'你们是游客吗～？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哎，不是吗？\n'
						'真遗憾……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'咪咪本来还想带你们\n'
						'参观克洛斯贝尔呢～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'咪咪将来要\n'
						'成为一名导游哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'到那时，咪咪\n'
						'会带你们游遍克洛斯贝尔的！{wait}'
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

data['code'][4] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'……我说你啊……\n'
				'你现在大吃大喝，刚才\n'
				'辛苦跑步的意义不就全没了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呼～早知如此的话，\n'
				'就不称赞你了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啊……总觉得脸似乎变瘦了一些呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'嗯嗯，\n'
				'你节食很努力嘛，\n'
				'了不起～了不起～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啊～在百货买零食吃，\n'
				'果然是最幸福的\n'
				'时刻呀。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'（嚼嚼嚼）……\n'
				'怎么了，你干嘛一脸怨恨的表情啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'……最近没人说你变胖了吗？\n'
				'你啊，脸都快变成圆球了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'就是因为对节食有所懈怠，\n'
				'体重才会反弹的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哎？\n'
				'你在吃什么呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'明明说好要一起减肥的，\n'
				'偷偷吃零食可不行啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我们认识也有很长时间了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你就没有过什么浪漫艳遇吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'说起来，纪念庆典也快到了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你有什么安排吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啊，这么一说……\n'
				'彩虹剧团的票好像已经\n'
				'开始出售了吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'完全忘记了。\n'
				'太糟糕了……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'不久前我看到ＩＢＣ总裁的\n'
				'豪华轿车了～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'总裁先生人也很帅气潇洒，\n'
				'完全是我喜欢的类型哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'今天要去哪里？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'也没心情去逛\n'
				'百货啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'亚里欧斯大人好像又出差了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'暂时没法见到\n'
				'他了呢……\n'
				'真遗憾。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'真想找个有车的\n'
				'男朋友啊～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'那样就可以让他开车\n'
				'带我去任何地方了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'好像发生魔兽闯入\n'
				'城镇和村子的事件了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'真是的～好可怕啊。\n'
				'警备队的人到底在干什么呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'不过，话说回来，\n'
				'你们看到克洛斯贝尔时报周刊上\n'
				'刊登的那张照片了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'亚里欧斯大人果然\n'
				'很英俊帅气呀。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'亚里欧斯大人好像又\n'
				'立下了新功劳呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我也好想被亚里欧斯大人\n'
				'救出来呀～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'但、但是啊！\n'
				'因为开始变瘦了嘛，\n'
				'所以觉得就吃一点点，也可以吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'啊啊～不要丢下我嘛～！\n'
				'我会继续加油的～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('0x4B', Char(12), -1),
			Insn('TEXT_TALK', Char(254), Text(
				'是、是吗～\n'
				'虽然自己还没发现……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'但跑步的成果已经有所显现了呢！\n'
				'好……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(12), Text(
				'（嗯，只要她能拿出干劲，撒谎也值了。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x4C', Char(12), -1),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'啊啊～太狡猾啦！\n'
				'我明明还在节食减肥呢，\n'
				'却故意让我看到食物……！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……我说，稍微给我点食物嘛～！\n'
				'就当是我努力晨跑的奖励啦！！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1550)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'好过分～！\n'
				'就像事不关己一样……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我从今天开始就要节食了，\n'
				'帮忙监督我啦……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'（嚼嚼）……所以说呢，\n'
				'一日吃两餐是不可能的吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'没关系，从明天开始努力就好啦～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'如果有什么浪漫艳遇的话，\n'
				'也就不会总是和你一起玩了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……唉。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯～和平常一样，\n'
				'只是不停地逛街啊～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'算了，反正都已经卖光了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'彩虹剧团的门票，\n'
				'永远都是刚发售就被一抢而空。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'至少没有浪费时间去排队，\n'
				'也算是幸运了～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'亚里欧斯先生也罢，\n'
				'迪塔先生也罢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你的眼里还真是\n'
				'就只有帅气的大叔啊～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'找个地方喝杯茶去如何～？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……虽然想这么说，但我没钱啊……\n'
				'果然还是只能在百货里随便逛逛吧～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'亚里欧斯先生很受人欢迎，\n'
				'但却总是在出差呢～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'警察这么靠不住，\n'
				'真希望他能一直留在克洛斯贝尔啊～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'不过，导力车是\n'
				'非常贵的吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'如果能钓到一个\n'
				'有钱男人就好了，\n'
				'但现实可是很严酷的啊～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'算了，反正在克洛斯贝尔市\n'
				'大概也不会出现那种事件，\n'
				'应该可以安心吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不管怎么样，\n'
				'也都有游击士协会呢～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我看到了～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你们就是当时傻站在后面的\n'
				'那些警察吧，\n'
				'看起来就像是跟班一样呢～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'警察似乎也帮了\n'
				'亚里欧斯大人的\n'
				'一点忙吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'呵呵，最后功劳不还是\n'
				'全都被人家占了嘛～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'一想到孩子们接过气球那一\n'
						'瞬间的笑脸……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，就觉得自己的工作\n'
						'十分有意义啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'希望将来能受到孩子们的仰慕，\n'
						'被喊为气球叔叔啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'总是可以看见孩子们的笑脸，\n'
						'我觉得这份工作\n'
						'真的很有价值。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'希望将来能受到孩子们的仰慕，\n'
						'被喊为气球叔叔啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'气球，要不要气球啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'请注意，\n'
						'不要把气球拿到\n'
						'拥挤的地方哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'它是橡胶制成的，\n'
						'受到挤压的话，很容易就会破掉。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'气球终究也只是橡胶制品，\n'
						'受到挤压的话，很容易就会破掉了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那刺耳的破裂声，\n'
						'我到现在都无法习惯……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'只要把气球拿在手里，\n'
				'心情马上就会平静下来。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'看啊，这可爱的形状。\n'
				'那些小小的烦恼都变得可笑起来了吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1550)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'气球，拿个气球吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'喔，今天没带着\n'
				'那个活泼开朗的小女孩啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'所谓小孩子，如果不抽时间陪陪她，\n'
				'可是会闹别扭的哦～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊，小姑娘，\n'
						'来个气球怎么样？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哈哈哈，你很喜欢气球吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(339), Text(
						'#1111F嗯～？……一般啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'不、不会吧……？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'怎么会这样呢，小孩子\n'
						'不是应该都很喜欢气球才对吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0006F（这是什么偏见……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……小孩子的话，\n'
						'应该都喜欢气球才对吧……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'给气球充入瓦斯这种事情，必须要在\n'
				'别人看不见的时候做。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不然会打破大家的幻想吧？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'瓦斯比空气更轻，\n'
						'所以气球才能优雅地飘浮在空中。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……喂，在这附近可一定\n'
						'要小心火源啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'瓦斯遇火的话，会把我\n'
						'都给炸飞的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'一定要非常小心火源啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我虽然喜欢气球，但也不想\n'
						'像气球一样在天上飞。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1037)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'嗯，今天就到这里吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'这份工作也并不轻松呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'如今到处都在用导力器，\n'
				'几乎都已经见不到瓦斯驱动的机器了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你不觉得给气球充气算是瓦斯为数不多的\n'
				'有效使用方法之一吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'气球、气球哦～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不小心松手的话，气球会飞掉的，\n'
				'一定要注意啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哈，今天也要充满干劲地\n'
				'分发气球呀。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'从上午开始，中央广场的\n'
				'游客就已经很多了，非常热闹呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'小兄弟，你们要不要来个气球呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不是游客也无所谓，\n'
				'反正我也是随便发的。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'旅游业已经被公认为\n'
				'克洛斯贝尔的主要产业之一了，\n'
				'市里也都下发了补助预算。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'派发气球也是让旅游业更加兴旺的\n'
				'重要工作哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'要来个气球吗～？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'……啊啊，并不是有什么\n'
						'特别的庆典啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'我只是一直都在派发气球而已。\n'
						'克洛斯贝尔的人\n'
						'都喜欢外表华丽的东西。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'克洛斯贝尔的人都喜欢\n'
						'华丽的东西，热闹的气氛。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'好啦好啦，\n'
						'别客气，拿去吧！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'要来个气球吗～？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'游客可以来我这里\n'
				'免费领取气球啦～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'那么，店铺的位置也\n'
						'已经确认完毕了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'反正机会难得，\n'
						'稍微观光一下再回去吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'毕竟庆典开始之后\n'
						'可能就再也没有观光的闲暇了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'那么，要去哪里观光好呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'话虽如此，因为是一日游，\n'
						'也不能去太远的地方……{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'下个月的纪念庆典，\n'
						'我会摆摊卖爆米花哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'呵呵，能占上个好位置真不错啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'下个月的纪念庆典，\n'
						'我会摆摊卖爆米花哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'今天是来检查位置的，\n'
						'下个月还请多关照呀。{wait}'
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

data['code'][8] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_ROTATE', Char(254), 197, 0),
					Insn('TEXT_TALK', Char(254), Text(
						'#15200F哔哔～哔哔～！\n'
						'导力车请缓慢行驶～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(254), Char(0), 500),
					Insn('TEXT_TALK', Char(254), Text(
						'#15203F……感觉今天的车流量\n'
						'似乎有些少啊……\n'
						'大概是错觉吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(9)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#15203F我每天都要疏导交通，\n'
						'感觉今天街上似乎稍微有些寂寥啊。\n'
						'或许是错觉吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1424)), Insn('NOT'), Insn('END')]), [
					Insn('EMOTE', Char(254), 0, 2000, (38, 38, 250, 1)),
					Insn('SLEEP', 1000),
					Insn('TEXT_TALK', Char(254), Text(
						'#15205F啊……这不是罗伊德嘛！{wait}'
						'{page}'
						'#15214F那个，听说你们经历了\n'
						'很危险的事情啊？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0008F抱歉，凯特前辈，\n'
						'让你担心了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
							Insn('TEXT_TALK', Char(258), Text(
								'#0100F我们没事的。{wait}'
								'{page}'
								'比起这个……\n'
								'最近街上的状况怎么样了？{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
							Insn('TEXT_TALK', Char(259), Text(
								'#0200F我们没事的。{wait}'
								'{page}'
								'比起这个……\n'
								'最近街上的状况怎么样了？{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
							Insn('TEXT_TALK', Char(260), Text(
								'#0300F哈，我们什么事\n'
								'都没有啦。{wait}'
								'{page}'
								'比起这个……\n'
								'最近街上的情况如何了？{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, []),
					]),
					Insn('TEXT_TALK', Char(254), Text(
						'#15203F街上很安静啊，\n'
						'几乎都没有受到纪念庆典\n'
						'余韵的影响。{wait}'
						'{page}'
						'#15200F麻烦事减少，倒是很令人高兴啦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0003F是吗……\n'
						'（自那之后，鲁巴彻的家伙们\n'
						'\u3000也暂时安分下来了吗……）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1424)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#15201F最近这一周，街上都很安静啊。{wait}'
						'{page}'
						'#15206F似乎完全都没有\n'
						'受到纪念庆典的影响啊。{wait}'
						'{page}'
						'#15200F比起那个，实在是很担心\n'
						'你们支援课的情况啊。\n'
						'请不要做太危险的事情哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 14))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((2, 16))),
				]),
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#15211F呼……今天早上也\n'
						'发现有人违规停车。{wait}'
						'{page}'
						'#15206F真是的，你们昨天才刚刚\n'
						'取缔过的～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F哈哈，是那样吗……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0300F算了，违规停车这种事\n'
						'一直是屡禁不止的。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#15201F不过，你们不觉得不甘心吗？{wait}'
						'{page}'
						'#15207F我很不甘心。\n'
						'所以要对那些违规停车的\n'
						'车主提出严重警告！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(9)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#15201F违规停车就是犯罪行为，\n'
						'坏习惯就必须要改正。{wait}'
						'{page}'
						'#15207F小恶可是会发展为大恶的！\n'
						'必须要对他们严重警告才行。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('FLAG_GET', 64))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 56, Insn('TASK_GET', 14))), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CALL', Function((2, 16))),
				]),
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_ROTATE', Char(254), 197, 0),
					Insn('TEXT_TALK', Char(254), Text(
						'#15200F哔哔～哔哔～！\n'
						'导力车请缓慢行驶～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(254), Char(0), 0),
					Insn('TEXT_TALK', Char(254), Text(
						'#15204F警察的工作就是要\n'
						'踏踏实实地不断努力。{wait}'
						'{page}'
						'#15202F好，罗伊德，还有各位，\n'
						'今天也一起加油吧！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F哈哈，也是呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(9)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#15204F警察的工作就是要\n'
						'踏踏实实地不断努力。{wait}'
						'{page}'
						'#15202F好，今天也一起加油吧！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1169)), Insn('NOT'), Insn('END')]), [
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1168)), Insn('END')]), [
							Insn('TEXT_TALK', Char(254), Text(
								'#15200F啊，罗伊德，是你们啊。\n'
								'还在调查案件吗？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0003F嗯，稍微有些事情……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
							Insn('SLEEP', 1000),
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F对了，凯特前辈\n'
								'一直都在市内巡逻吧。{wait}'
								'{page}'
								'对『银』这个名字\n'
								'有没有什么印象呢？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'#15203F……『银』？\n'
								'从没听说过啊……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('EMOTE', Char(254), 0, 2000, (38, 38, 250, 1)),
							Insn('SLEEP', 1000),
							Insn('TEXT_TALK', Char(254), Text(
								'#15205F啊，说起来！{wait}'
								'{page}'
								'#15202F彩虹剧团的\n'
								'新剧码好像就叫\n'
								'『金之太阳、银之月』啊！{wait}'
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
								'#0006F唔～这样啊……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'#15206F唔，嗯。\n'
								'没能帮上忙，真抱歉啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('EMOTE', Char(254), 0, 2000, (38, 38, 250, 1)),
							Insn('SLEEP', 1000),
							Insn('TEXT_TALK', Char(254), Text(
								'#15202F啊，是罗伊德，还有兰迪！{wait}'
								'{page}'
								'#15209F之前真是多谢你们\n'
								'帮忙进行交通管理了……{wait}'
								'{page}'
								'#15203F……啊，不对。{wait}'
								'{page}'
								'#15200F罗伊德搜查官以及\n'
								'特务支援课的各位，\n'
								'衷心感谢你们的协助！{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0002F哈哈哈……\n'
								'凯特前辈，不用那么\n'
								'在意形式吧。{wait}'
								'{page}'
								'我们也经常受你\n'
								'关照的啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'#15204F呵呵，说来也是呢。{wait}'
								'{page}'
								'#15200F那，以后如果有什么事情，\n'
								'还能请你们助我一臂之力吗。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(260), Text(
								'#0304F噢～那当然，\n'
								'请不要客气，随时联系我们吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'#15210F谢谢，帮大忙了。{wait}'
								'{page}'
								'#15200F……不过，罗伊德，你们\n'
								'还在进行调查吗？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0003F嗯，稍微有些事情……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
							Insn('SLEEP', 1000),
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F对了，凯特前辈\n'
								'一直都在市内巡逻吧。{wait}'
								'{page}'
								'对『银』这个名字\n'
								'有没有什么印象呢？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'#15203F……『银』？\n'
								'从没听说过啊……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('EMOTE', Char(254), 0, 2000, (38, 38, 250, 1)),
							Insn('SLEEP', 1000),
							Insn('TEXT_TALK', Char(254), Text(
								'#15205F啊，说起来！{wait}'
								'{page}'
								'#15202F彩虹剧团的\n'
								'新剧码好像就叫\n'
								'『金之太阳、银之月』啊！{wait}'
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
								'#0006F唔～这样啊……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'#15206F唔，嗯。\n'
								'没能帮上忙，真抱歉啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
					Insn('FLAG_SET', Flag(1169)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#15203F『银』……\n'
						'没有什么特别的印象呢……{wait}'
						'{page}'
						'#15206F嗯～抱歉啊，\n'
						'好像没能帮上忙呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(536)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F哪里，请不用在意。\n'
								'我们正准备去拜访一位\n'
								'相识的律师呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F哪里，是我们麻烦你了。\n'
								'相关线索我们已经基本掌握了，\n'
								'请不用在意。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1168)), Insn('NOT'), Insn('END')]), [
					Insn('EMOTE', Char(254), 0, 2000, (38, 38, 250, 1)),
					Insn('SLEEP', 1000),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1025)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(254), Text(
								'#15209F啊，罗伊德，还有兰迪！\n'
								'之前真是多谢你们\n'
								'帮忙进行交通管理了……{wait}'
								'{page}'
								'#15203F……啊，不对。{wait}'
								'{page}'
								'#15200F罗伊德搜查官以及\n'
								'特务支援课的各位，\n'
								'衷心感谢你们的协助！{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('TEXT_TALK', Char(254), Text(
								'#15200F啊，罗伊德，是你们啊！\n'
								'工作辛苦了～{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F啊，凯特前辈。\n'
								'你辛苦了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(260), Text(
								'#0300F嗨～今天早上承蒙指导了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'#15209F对了对了，你们两位今天早上\n'
								'还帮忙进行交通管理了啊。\n'
								'真是多谢啦……{wait}'
								'{page}'
								'#15203F……啊，不对。{wait}'
								'{page}'
								'#15200F罗伊德搜查官以及\n'
								'特务支援课的各位，\n'
								'衷心感谢你们的协助！{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
					Insn('TEXT_TALK', Char(257), Text(
						'#0002F哈哈哈……\n'
						'凯特前辈，不用那么\n'
						'在意形式吧。{wait}'
						'{page}'
						'我们也经常受你\n'
						'关照的啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#15204F呵呵，说来也是呢。{wait}'
						'{page}'
						'#15200F那，以后如果有什么事情，\n'
						'还能请你们助我一臂之力吗。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0304F噢～那当然，\n'
						'请不要客气，随时联系我们吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'#15210F谢谢，帮大忙了。{wait}'
						'{page}'
						'#15202F那么，任务辛苦啦！\n'
						'你们也要加油哦。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1168)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#15201F或许是因为纪念庆典的临近，\n'
						'各种小事件也在不断增多。{wait}'
						'{page}'
						'#15203F市内的巡逻工作还是不能掉以轻心啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(9)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_ROTATE', Char(254), 197, 0),
					Insn('TEXT_TALK', Char(254), Text(
						'#15201F哔哔～哔哔～！{wait}'
						'{page}'
						'#15200F导力车请缓慢行驶。\n'
						'为了市民们的安全，\n'
						'请各位配合～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(254), Char(0), 500),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(863)), Insn('END')]), [
							Insn('TEXT_TALK', Char(254), Text(
								'#15200F啊，是罗伊德和各位，\n'
								'准备去执行任务吗？\n'
								'小心导力车呀！{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F哈哈，谢谢了。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('TEXT_TALK', Char(254), Text(
								'#15202F啊……罗伊德？\n'
								'好久不见了啊～！{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F凯特前辈……\n'
								'真是好久不见了，\n'
								'在警察学校时承蒙你多加关照。{wait}'
								'{page}'
								'……今天是在工作吗？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'#15210F嗯，我经常在这里进行\n'
								'交通管理。{wait}'
								'{page}'
								'#15200F罗伊德，你们也要去执行任务了吗？\n'
								'要小心导力车呀！{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F哈哈，谢谢了。{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(863)),
						]),
					]),
					Insn('FLAG_SET', Flag(9)),
				]),
				(None, [
					Insn('CHAR_ROTATE', Char(254), 197, 0),
					Insn('TEXT_TALK', Char(254), Text(
						'#15200F导力车请缓慢行驶。\n'
						'为了市民们的安全，\n'
						'请各位配合～！{wait}'
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

data['code'][9] = [
	Insn('TEXT_START', Char(254)),
	Insn('FLAG_UNSET', Flag(12)),
	Insn('CALL', Function((1, 11))),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(851)), Insn('FLAG', Flag(656)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(12)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0004F（说起来……\n'
				'\u3000有些东西似乎可以用来喂猫。）{wait}'
				'{page}'
				'#0000F（说不定可以拿来\n'
				'\u3000喂柯贝呢。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(656)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(656)), Insn('ATTR', 4), Insn('CONST', 0), Insn('EQ'), Insn('FLAG', Flag(603)), Insn('NOT'), Insn('BOOL_AND'), Insn('ATTR', 4), Insn('CONST', 1), Insn('EQ'), Insn('FLAG', Flag(657)), Insn('NOT'), Insn('BOOL_AND'), Insn('OR'), Insn('ATTR', 4), Insn('CONST', 2), Insn('EQ'), Insn('FLAG', Flag(658)), Insn('NOT'), Insn('BOOL_AND'), Insn('OR'), Insn('ATTR', 4), Insn('CONST', 3), Insn('EQ'), Insn('FLAG', Flag(659)), Insn('NOT'), Insn('BOOL_AND'), Insn('OR'), Insn('ATTR', 4), Insn('CONST', 4), Insn('EQ'), Insn('FLAG', Flag(660)), Insn('NOT'), Insn('BOOL_AND'), Insn('OR'), Insn('ATTR', 4), Insn('CONST', 5), Insn('EQ'), Insn('FLAG', Flag(661)), Insn('NOT'), Insn('BOOL_AND'), Insn('OR'), Insn('ATTR', 4), Insn('CONST', 6), Insn('EQ'), Insn('FLAG', Flag(662)), Insn('NOT'), Insn('BOOL_AND'), Insn('OR'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
			Insn('WHILE', [Insn('VAR', 0), Insn('CONST', 99), Insn('EQ'), Insn('END')], [
				Insn('FADE_ON', 300, Color(0x00000000), 100),
				Insn('MENU_CUSTOM', Insn('INIT', ResId(1))),
				Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('对话'))),
				Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('喂饲料'))),
				Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('放弃'))),
				Insn('FLAG_UNSET', Flag(12)),
				Insn('CALL', Function((1, 11))),
				Insn('IF', [
					(Expr([Insn('FLAG', Flag(12)), Insn('NOT'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 1)),
					]),
					(None, []),
				]),
				Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
				Insn('MENU_CUSTOM', Insn('FINISH', ResId(1), -1, 1)),
				Insn('MENU_WAIT', 0),
				Insn('0x60', 1),
				Insn('0x5A'),
				Insn('IF', [
					(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('NE'), Insn('END')]), [
						Insn('FADE_OFF', 300, Color(0x00000000)),
						Insn('0x0D'),
					]),
					(None, []),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
						Insn('EXPR_VAR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
						Insn('MENU_CUSTOM', Insn('INIT', ResId(1))),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 350, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('雪花蟹'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 351, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('阿尔摩利卡鲫鱼'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 352, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('橙河鱼'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 353, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('岩穴鱼'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 354, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('鲤鱼'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 355, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('冷水鱼'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 356, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('蓝带神仙鱼'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 357, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('银伞鱼'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 358, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('虹鳟鱼'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 359, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('黑鲑'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 360, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('鲑鱼'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 361, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('鳗鱼'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 362, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('珍珠草鱼'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 363, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('大口鲈鱼'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 364, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('云斑蛇头'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 365, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('暗纹蛇鱼'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 366, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('巨鲶'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 367, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('巨血蟹'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 368, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('电鳗'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 369, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('魔鬼巨鲶'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 370, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('巨型蟹'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 371, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('金鲑'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 372, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('锦鲤'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 373, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('霸王蛇鱼'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('IF', [
							(Expr([Insn('EXEC', Insn('ITEM_GET', 473, 0)), Insn('END')]), [
								Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('猫饭'))),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
							]),
							(None, []),
						]),
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('放弃'))),
						Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
						Insn('MENU_CUSTOM', Insn('FINISH', ResId(1), -1, 1)),
						Insn('MENU_WAIT', 0),
						Insn('FADE_OFF', 300, Color(0x00000000)),
						Insn('0x60', 1),
						Insn('TEXT_RESET', b'\x00'),
						Insn('0x5A'),
						Insn('IF', [
							(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('GE'), Insn('VAR', 0), Insn('CONST', 0), Insn('LT'), Insn('OR'), Insn('END')]), []),
							(None, [
								Insn('EVENT_BEGIN', 1),
								Insn('CROSSFADE', 500),
								Insn('CHAR_SET_POS', Char(19), (-21980, 1300, -19300), 270),
								Insn('CHAR_SET_POS', Char(0), (-23900, 1300, -19070), 89),
								Insn('CHAR_SET_POS', Char(1), (-23540, 1300, -20210), 89),
								Insn('CHAR_SET_POS', Char(2), (-25020, 1300, -19860), 89),
								Insn('CHAR_SET_POS', Char(3), (-25130, 1300, -18930), 89),
								Insn('CHAR_SET_POS', Char(4), (-26200, 1300, -19870), 89),
								Insn('CHAR_SET_POS', Char(5), (-26790, 1300, -19180), 89),
								Insn('CAM_OFFSET', (-23130, 3900, -19610), 0),
								Insn('CAM_ROTATE', 45, 14, 0, 0),
								Insn('0x6E', 700, 0),
								Insn('CAM_DISTANCE', 17000, 0),
								Insn('0x0D'),
								Insn('TEXT_TALK', Char(254), Text(
									'喵喵喵……㈱{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('FORK_LOOP', 0, 1, [
									Insn('CHAR_WATCH', Char(0), Char(19), 0),
								]),
								Insn('FORK_LOOP', 1, 1, [
									Insn('CHAR_WATCH', Char(1), Char(19), 0),
								]),
								Insn('FORK_LOOP', 2, 1, [
									Insn('CHAR_WATCH', Char(2), Char(19), 0),
								]),
								Insn('FORK_LOOP', 3, 1, [
									Insn('CHAR_WATCH', Char(3), Char(19), 0),
								]),
								Insn('FORK_LOOP', 4, 1, [
									Insn('CHAR_WATCH', Char(4), Char(19), 0),
								]),
								Insn('FORK_LOOP', 5, 1, [
									Insn('CHAR_WATCH', Char(5), Char(19), 0),
								]),
								Insn('CHAR_FLAG1_SET', Char(19), 32768),
								Insn('CHAR_ROTATE', Char(19), 0, 500),
								Insn('SLEEP', 50),
								Insn('CHAR_FLAG1_UNSET', Char(19), 1),
								Insn('SOUND_PLAY', 814, 0, 0, 80),
								Insn('FORK', 19, 1, [
									Insn('0x9D', Char(254), -22230, 1500, -15580, 1800, 8000),
								]),
								Insn('FORK_AWAIT', Char(19), 1),
								Insn('SOUND_PLAY', 814, 0, 0, 80),
								Insn('FORK', 19, 1, [
									Insn('0x9D', Char(254), -22580, 4300, -14690, 4400, 5000),
								]),
								Insn('FORK_AWAIT', Char(19), 1),
								Insn('SOUND_PLAY', 854, 0, 0, 80),
								Insn('FORK', 19, 1, [
									Insn('0x9D', Char(254), -22690, 1300, -8260, 1800, 3000),
								]),
								Insn('FORK_AWAIT', Char(19), 1),
								Insn('SLEEP', 2000),
								Insn('CHAR_ROTATE', Char(19), 180, 500),
								Insn('SOUND_PLAY', 814, 0, 0, 80),
								Insn('FORK', 19, 1, [
									Insn('0x9D', Char(254), -22580, 4300, -14690, 4500, 4000),
								]),
								Insn('FORK_AWAIT', Char(19), 1),
								Insn('SOUND_PLAY', 814, 0, 0, 80),
								Insn('FORK', 19, 1, [
									Insn('0x9D', Char(254), -22230, 1500, -15580, 1600, 5000),
								]),
								Insn('FORK_AWAIT', Char(19), 1),
								Insn('SOUND_PLAY', 854, 0, 0, 80),
								Insn('FORK', 19, 1, [
									Insn('0x9D', Char(254), -21980, 1300, -19300, 1500, 6000),
								]),
								Insn('FORK_AWAIT', Char(19), 1),
								Insn('CHAR_FLAG1_SET', Char(19), 1),
								Insn('CHAR_ROTATE', Char(19), 270, 500),
								Insn('CHAR_FLAG1_UNSET', Char(19), 32768),
								Insn('FORK_QUIT', Char(0), 1),
								Insn('FORK_QUIT', Char(1), 1),
								Insn('FORK_QUIT', Char(2), 1),
								Insn('FORK_QUIT', Char(3), 1),
								Insn('FORK_QUIT', Char(4), 1),
								Insn('FORK_QUIT', Char(5), 1),
								Insn('TEXT_TALK', Char(254), Text(
									'喵～……{wait}'
								)),
								Insn('TEXT_WAIT'),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
								Insn('EXPR_VAR', 2, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
								Insn('FADE_ON', 300, Color(0x00000000), 100),
								Insn('TEXT_SET_POS', -1, -1, -1, -1),
								Insn('TEXT_SET_NAME', Translate('')),
								Insn('SOUND_PLAY', 17, 0, 0, 100),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 350, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 350, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 112}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 112, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 351, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 1), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 351, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 121}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 121, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 352, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 2), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 352, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 106}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 106, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 353, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 3), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 353, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 109}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 109, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 354, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 4), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 354, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 115}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 115, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 355, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 5), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 355, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 103}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 103, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 356, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 6), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 356, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 138}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 138, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 357, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 7), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 357, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 133}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 133, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 358, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 8), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 358, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 153}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 153, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 359, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 9), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 359, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 130}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 130, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 360, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 10), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 360, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 146}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 146, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 361, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 11), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 361, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 127}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 127, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 362, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 12), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 362, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 118}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 118, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 363, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 13), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 363, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 124}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 124, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 364, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 14), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 364, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 139}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 139, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 365, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 15), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 365, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 141}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 141, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 366, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 16), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 366, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 142}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 142, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 367, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 17), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 367, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 131}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 131, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 368, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 18), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 368, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 169}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 169, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 369, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 19), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 369, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 129}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 129, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 370, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 20), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 370, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 114}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 114, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 371, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 21), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 371, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 154}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 154, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 372, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 22), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 372, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 149}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 149, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 373, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 23), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 373, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 160}{color 0}。{wait}'
												)),
												Insn('ITEM_ADD', 160, 1),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('EXEC', Insn('ITEM_GET', 473, 0)), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('VAR', 0), Insn('VAR', 1), Insn('EQ'), Insn('END')]), [
												Insn('EXPR_VAR', 2, Expr([Insn('CONST', 24), Insn('SET'), Insn('END')])),
												Insn('ITEM_REMOVE', 473, 1),
												Insn('TEXT_MESSAGE', Char(255), Text(
													'收下了{item 301}{color 0}×３。{wait}'
												)),
												Insn('ITEM_ADD', 301, 3),
											]),
											(None, []),
										]),
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('TEXT_WAIT'),
								Insn('TEXT_RESET', b'\x00'),
								Insn('FADE_OFF', 300, Color(0x00000000)),
								Insn('TEXT_SET_POS', -1, 280, 60, 3),
								Insn('0x5A'),
								Insn('IF', [
									(Expr([Insn('ATTR', 4), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
										Insn('FLAG_SET', Flag(603)),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('ATTR', 4), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
										Insn('FLAG_SET', Flag(657)),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('ATTR', 4), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
										Insn('FLAG_SET', Flag(658)),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('ATTR', 4), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
										Insn('FLAG_SET', Flag(659)),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('ATTR', 4), Insn('CONST', 4), Insn('EQ'), Insn('END')]), [
										Insn('FLAG_SET', Flag(660)),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('ATTR', 4), Insn('CONST', 5), Insn('EQ'), Insn('END')]), [
										Insn('FLAG_SET', Flag(661)),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('ATTR', 4), Insn('CONST', 6), Insn('EQ'), Insn('END')]), [
										Insn('FLAG_SET', Flag(662)),
									]),
									(None, []),
								]),
								Insn('EXPR_VAR', 1, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(657)), Insn('END')]), [
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(658)), Insn('END')]), [
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(659)), Insn('END')]), [
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(660)), Insn('END')]), [
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(661)), Insn('END')]), [
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('FLAG', Flag(662)), Insn('END')]), [
										Insn('EXPR_VAR', 1, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('VAR', 1), Insn('CONST', 6), Insn('EQ'), Insn('END')]), [
										Insn('TEXT_TALK', Char(254), Text(
											'喵喵喵～呜……丅{wait}'
										)),
										Insn('TEXT_WAIT'),
										Insn('FADE_ON', 300, Color(0x00000000), 100),
										Insn('TEXT_SET_POS', -1, -1, -1, -1),
										Insn('TEXT_SET_NAME', Translate('')),
										Insn('SOUND_PLAY', 17, 0, 0, 100),
										Insn('TEXT_MESSAGE', Char(255), Text(
											'收下了{item 166}{color 0}。{wait}'
										)),
										Insn('ITEM_ADD', 166, 1),
										Insn('TEXT_WAIT'),
										Insn('TEXT_RESET', b'\x00'),
										Insn('FADE_OFF', 300, Color(0x00000000)),
										Insn('TEXT_SET_POS', -1, 280, 60, 3),
										Insn('0x5A'),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('ATTR', 10), Insn('CONST', 1), Insn('EQ'), Insn('ATTR', 10), Insn('CONST', 8), Insn('EQ'), Insn('OR'), Insn('END')]), [
										Insn('TEXT_TALK', Char(258), Text(
											'#0105F啊……要把这个给我们吗？{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
									(Expr([Insn('ATTR', 10), Insn('CONST', 2), Insn('EQ'), Insn('ATTR', 10), Insn('CONST', 9), Insn('EQ'), Insn('OR'), Insn('END')]), [
										Insn('TEXT_TALK', Char(259), Text(
											'#0205F要把这个给我们吗？{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
									(Expr([Insn('ATTR', 10), Insn('CONST', 0), Insn('EQ'), Insn('ATTR', 10), Insn('CONST', 3), Insn('EQ'), Insn('OR'), Insn('END')]), [
										Insn('IF', [
											(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(3))), Insn('CONST', 1), Insn('NEG'), Insn('GT'), Insn('END')]), [
												Insn('TEXT_TALK', Char(260), Text(
													'#0305F要把这东西给我们吗？{wait}'
												)),
												Insn('TEXT_WAIT'),
											]),
											(None, [
												Insn('TEXT_TALK', Char(257), Text(
													'#0005F这个是要给我们的吗……？{wait}'
												)),
												Insn('TEXT_WAIT'),
											]),
										]),
									]),
									(None, []),
								]),
								Insn('IF', [
									(Expr([Insn('VAR', 1), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
										Insn('TEXT_TALK', Char(257), Text(
											'#0000F哈哈，多谢啦。\n'
											'我们会好好使用的。{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
									(None, [
										Insn('TEXT_TALK', Char(257), Text(
											'#0000F哈哈，多谢啦。\n'
											'……不过，究竟是从什么地方\n'
											'拿来的呢。{wait}'
										)),
										Insn('TEXT_WAIT'),
									]),
								]),
								Insn('TEXT_END', Char(254)),
								Insn('EVENT_END', 4),
								Insn('RETURN'),
							]),
						]),
						Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
					]),
					(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('NE'), Insn('END')]), []),
					(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
						Insn('EXPR_VAR', 0, Expr([Insn('CONST', 99), Insn('SET'), Insn('END')])),
						Insn('CALL', Function((1, 10))),
					]),
					(None, []),
				]),
			]),
		]),
		(None, [
			Insn('CALL', Function((1, 10))),
		]),
	]),
	Insn('TEXT_END', Char(19)),
	Insn('RETURN'),
]

data['code'][10] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(851)), Insn('NOT'), Insn('FLAG', Flag(1024)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#0105F啊，这种地方竟然有小猫……{wait}'
				'{page}'
				'#0109F呵呵，好可爱！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(596)), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F嗯，似乎在支援课搬进这里之前，\n'
						'它就已经住在这里了。{wait}'
						'{page}'
						'#0004F我记得克洛斯贝尔时报周刊\n'
						'原来就在这栋楼里……\n'
						'说不定那个时候它就在了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F嗯～在支援课入驻之前\n'
						'就已经定居在此的猫吗？{wait}'
						'{page}'
						'#0004F我记得克洛斯贝尔时报周刊\n'
						'原来就在这栋楼里……\n'
						'说不定那个时候它就在了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('TEXT_TALK', Char(260), Text(
				'#0309F……来来！\n'
				'你叫什么名字呀～？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_WATCH', Char(19), Char(260), 500),
			Insn('SOUND_PLAY', 823, 0, 0, 100),
			Insn('SLEEP', 500),
			Insn('TEXT_TALK', Char(259), Text(
				'#0200F…………………………{wait}'
				'{page}'
				'这孩子的名字是柯贝。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('IF', [
				(Expr([Insn('ATTR', 10), Insn('CONST', 2), Insn('NE'), Insn('END')]), [
					Insn('EMOTE', Char(0), 0, 2000, (38, 38, 250, 1)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('ATTR', 11), Insn('CONST', 2), Insn('NE'), Insn('END')]), [
					Insn('EMOTE', Char(1), 0, 2000, (38, 38, 250, 1)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('ATTR', 12), Insn('CONST', 2), Insn('NE'), Insn('END')]), [
					Insn('EMOTE', Char(2), 0, 2000, (38, 38, 250, 1)),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('ATTR', 13), Insn('CONST', 2), Insn('NE'), Insn('END')]), [
					Insn('EMOTE', Char(3), 0, 2000, (38, 38, 250, 1)),
				]),
				(None, []),
			]),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(258), Text(
				'#0102F是缇欧起的吗？\n'
				'好可爱的名字啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#0203F不，这并不是\n'
				'我起的名字……{wait}'
				'{page}'
				'#0202F……总之，我想\n'
				'称呼这孩子为柯贝就好。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#0304F嗯，那就叫这个吧。{wait}'
				'{page}'
				'#0300F以后时不时带点\n'
				'吃的来喂它吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(851)),
		]),
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(19), Text(
				'喵……？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(19), Text(
						'喵～～嗝。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('EXEC', Insn('PARTY_POSITION', Party(9))), Insn('CONST', 1), Insn('NEG'), Insn('NE'), Insn('END')]), [
							Insn('TEXT_TALK', Char(266), Text(
								'#0605F（嗯……这只猫\n'
								'\u3000好像是克洛斯贝尔通讯社\n'
								'\u3000以前饲养的，不过……）{wait}'
								'{page}'
								'#0603F（现在已经交托给特务支援课了吗？\n'
								'\u3000必须要补记在\n'
								'\u3000一课的资料里啊……）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, []),
					]),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(19), Text(
						'喵～～嗝。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('TEXT_TALK', Char(19), Text(
				'喵啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(19), Text(
						'咕咕，喵～{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('ATTR', 10), Insn('CONST', 8), Insn('EQ'), Insn('ATTR', 11), Insn('CONST', 8), Insn('EQ'), Insn('OR'), Insn('ATTR', 12), Insn('CONST', 8), Insn('EQ'), Insn('OR'), Insn('ATTR', 13), Insn('CONST', 8), Insn('EQ'), Insn('OR'), Insn('END')]), [
							Insn('EMOTE', Char(265), 0, 2000, (2, 7, 80, 1)),
							Insn('SOUND_PLAY', 28, 0, 0, 100),
							Insn('SLEEP', 1000),
						]),
						(None, []),
					]),
					Insn('TEXT_TALK', Char(265), Text(
						'#0502F（嗯～好可爱……）{wait}'
						'{page}'
						'#0506F（屋顶上竟然养着猫……\n'
						'\u3000我是不是也该在国境门那里养一只呢。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(5)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(19), Text(
						'咕咕，喵～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1398)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(339), Text(
						'#1105F啊！是小猫～{wait}'
						'{page}'
						'#1109F小小的好可爱哦！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F说起来，这好像是第一次\n'
						'带琪雅来屋顶啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
							Insn('TEXT_TALK', Char(258), Text(
								'#0104F是啊，在这里会被街上的人看到。{wait}'
								'{page}'
								'#0100F考虑到琪雅的安全，\n'
								'这也是没办法的事情啊。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
							Insn('TEXT_TALK', Char(259), Text(
								'#0204F是啊，在这里会被别人看得清清楚楚。{wait}'
								'{page}'
								'#0202F考虑到琪雅的安全，\n'
								'这也没办法呢。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
							Insn('TEXT_TALK', Char(260), Text(
								'#0302F哈，在这里会被别人看个一清二楚，\n'
								'考虑到小琪的实际情况，这也没办法吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, []),
					]),
					Insn('FLAG_SET', Flag(1398)),
					Insn('FLAG_SET', Flag(851)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(339), Text(
						'#1110F小猫咪，到这边来～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('CHAR_WATCH', Char(19), Char(339), 500),
					Insn('SLEEP', 300),
					Insn('TEXT_TALK', Char(19), Text(
						'喵呜呜呜……㈱{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('TEXT_TALK', Char(19), Text(
				'喵啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('TEXT_TALK', Char(19), Text(
				'喵……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('TEXT_TALK', Char(19), Text(
				'喵～{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('TEXT_TALK', Char(19), Text(
				'喵？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(801)), Insn('END')]), [
			Insn('TEXT_TALK', Char(19), Text(
				'喵喵。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('TEXT_TALK', Char(19), Text(
				'喵啊……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('TEXT_TALK', Char(19), Text(
				'喵～～嗝。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(603)), Insn('END')]), [
					Insn('TEXT_TALK', Char(19), Text(
						'喵喵喵喵喵～㈱{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(19), Text(
						'喵～～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(526)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(603)), Insn('END')]), [
					Insn('TEXT_TALK', Char(19), Text(
						'喵喵喵喵喵～㈱{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(Expr([Insn('FLAG', Flag(596)), Insn('END')]), [
					Insn('TEXT_TALK', Char(19), Text(
						'喵～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(19), Text(
						'喵喵？{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(851)), Insn('NOT'), Insn('FLAG', Flag(1024)), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0004F（柯贝是一直住在\n'
				'\u3000支援课的猫吧……）{wait}'
				'{page}'
				'#0000F（嗯，这家伙挺随性的，\n'
				'\u3000我们也只是偶尔给它\n'
				'\u3000带些吃的来而已。）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(851)),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 350, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 351, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 352, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 353, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 354, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 355, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 356, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 357, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 358, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 359, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 360, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 361, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 362, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 363, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 364, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 365, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 366, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 367, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 368, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 369, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 370, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 371, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 372, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('ITEM_GET', 473, 0)), Insn('END')]), [
			Insn('FLAG_SET', Flag(12)),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(259), Text(
						'#0202F赛特，琪雅就\n'
						'拜托你照顾了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(20), Text(
						'#1200F呜噜噜噜……！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('ATTR', 10), Insn('CONST', 8), Insn('EQ'), Insn('ATTR', 11), Insn('CONST', 8), Insn('EQ'), Insn('OR'), Insn('ATTR', 12), Insn('CONST', 8), Insn('EQ'), Insn('OR'), Insn('ATTR', 13), Insn('CONST', 8), Insn('EQ'), Insn('OR'), Insn('END')]), [
							Insn('EMOTE', Char(265), 0, 2000, (16, 19, 250, 1)),
							Insn('SOUND_PLAY', 23, 0, 0, 100),
							Insn('SLEEP', 1000),
						]),
						(None, []),
					]),
					Insn('TEXT_TALK', Char(265), Text(
						'#0508F（呜呜……\n'
						'\u3000我好像还是有点怕狗。）{wait}'
						'{page}'
						'#0505F（啊，说来这不是狗，是狼呢。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(20), Text(
						'#1200F呜噜噜噜噜……{wait}'
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

data['code'][13] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('CHAR_ROTATE', Char(254), 0, 0),
					Insn('TEXT_TALK', Char(21), Text(
						'#1110F嗯～好温暖啊～！{wait}'
						'{page}'
						'#1109F赛特，来午睡吧～！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(20), Text(
						'#1200F呜噜噜噜噜……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(265), Text(
						'#0509F（好、好可爱……！）{wait}'
						'{page}'
						'#0502F（嗯～难怪大家\n'
						'\u3000都那么喜欢她呢。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0012F（哈哈……是啊。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(8)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(21), Text(
						'#1110F啊，是大家。\n'
						'一路顺风哦～！{wait}'
						'{page}'
						'#1109F消灭幽灵，要加油哦！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0109F嗯、嗯……\n'
						'当然会努力啦！{wait}'
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

data['code'][14] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(533)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(10)), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'格蕾丝前辈～！\n'
						'原稿可怎么办啊～！？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'拜托请快点出现救救我啊～！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'真是败了～格蕾丝前辈\n'
						'又不见踪影了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'前辈不在的话，\n'
						'原稿可就无法完成了……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(10)),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(10)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'格蕾丝前辈～你在哪里呀～！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……不会是又在哪个酒吧里面\n'
				'大吃大喝吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'真是的，格蕾丝前辈\n'
				'到底去哪里了呢……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'原稿的截止日期都已经临近了……\n'
				'（自言自语）……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(10)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0xFFFFFFFF), 0),
	Insn('FADE_ON', 500, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FADE_OFF', 0, Color(0xFFFFFFFF)),
	Insn('SOUND_LOAD', 803),
	Insn('SOUND_PLAY', 803, 0, 2, 0),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 55))),
	Insn('CHAR_SET_POS', Char(257), (1420, 0, -14130), 0),
	Insn('CHAR_SET_POS', Char(258), (-290, 0, -16530), 45),
	Insn('CHAR_SET_POS', Char(259), (-700, 0, -14800), 90),
	Insn('CHAR_SET_POS', Char(260), (1500, 0, -16379), 0),
	Insn('CAM_OFFSET', (-660, 3000, 3390), 0),
	Insn('CAM_ROTATE', 55, 0, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 16370, 0),
	Insn('CAM_ROTATE', 35, 3, 0, 5000),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('0x6F', b'y'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-21970, 1900, 6540), 0),
	Insn('CAM_ROTATE', 351, 8, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 14980, 0),
	Insn('CAM_ROTATE', 356, 8, 0, 3000),
	Insn('0x6F', b'y'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (19900, 3000, 6130), 0),
	Insn('CAM_ROTATE', 57, 4, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 18430, 0),
	Insn('CAM_ROTATE', 55, -2, 0, 5000),
	Insn('0x6F', b'y'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-60, 5700, 23250), 0),
	Insn('CAM_ROTATE', 359, 18, 0, 0),
	Insn('0x6E', 700, 0),
	Insn('CAM_DISTANCE', 11620, 0),
	Insn('CHAR_FLAG1_SET', Char(12), 32768),
	Insn('CHAR_FLAG1_SET', Char(13), 32768),
	Insn('0x6F', b'y'),
	Insn('CAM_OFFSET', (-5540, 4000, 5000), 10000),
	Insn('CAM_ROTATE', 24, 29, 0, 10000),
	Insn('0x6E', 800, 10000),
	Insn('CAM_DISTANCE', 35000, 10000),
	Insn('SLEEP', 2000),
	Insn('0xCB', b'T\x01\xc8\x00', 'c_plac02', b'\x00\xdc\x05'),
	Insn('0x6F', b'y'),
	Insn('FORK_QUIT', Char(35), 1),
	Insn('TEXT_TALK', Char(260), Text(
		'#0300F哎呀呀……还是一点都没变，\n'
		'真是条喧嚣吵闹的街道啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0004F因为这里算是克洛斯贝尔的\n'
		'中心地区呢。{wait}'
		'{page}'
		'#0000F到处都是大型商店，\n'
		'如果需要买东西，基本都能在这里解决……{wait}'
		'{page}'
		'想去其它街区的话，从这里走也都很方便。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F最近导力车的数量也增加了，\n'
		'这里似乎越来越热闹了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0002F哈哈，看来是这样呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('FORK_FUNC', Char(35), 1, Function((0, 56))),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (190, 1500, -15740), 0),
	Insn('CAM_ROTATE', 39, 18, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 17000, 0),
	Insn('CHAR_FLAG1_UNSET', Char(12), 32768),
	Insn('CHAR_FLAG1_UNSET', Char(13), 32768),
	Insn('0x0D'),
	Insn('CHAR_WATCH', Char(257), Char(258), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F对了，各位，\n'
		'我们去『导力商店』里看看如何？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#0305F啊，是那个大叔刚才\n'
		'说过的导力工房吗？{wait}'
		'{page}'
		'#0300F听说是个内部装修\n'
		'焕然一新，十分时尚的工房呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#0203F算是个提高了商业性的\n'
		'新型工房吧。{wait}'
		'{page}'
		'#0200F而且已经与警察方面签下了合约，\n'
		'所以应该也可以进行战术导力器的改造，\n'
		'或是结晶回路的采购。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0104F#6P以后大概会频繁去那里吧。{wait}'
		'{page}'
		'#0100F那么，在去其它街区之前，\n'
		'不如先进店里问候一下吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F嗯，就是街角的那个建筑。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x5A'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('SOUND_PLAY', 828, 0, 0, 100),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}在中央广场，有百货、导力商店、\n'
		'武器商会、餐厅等各种设施。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}各种购物场所一应俱全，\n'
		'因此，若想整理装备，\n'
		'便可以前往中央广场。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}另外，导力商店『原点』\n'
		'位于广场的东侧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(0), (-290, 0, -16530), 45),
	Insn('0xB5', b'\x00\x02\x80\x00'),
	Insn('FLAG_SET', Flag(548)),
	Insn('FORK_QUIT', Char(35), 1),
	Insn('SOUND_STOP', 803),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('EVENT_BEGIN', 1),
	Insn('CHAR_SET_POS', Char(24), (-6460, -4200, -21000), 135),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(24), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(11)), Insn('NOT'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('ATTR', 10), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F噢……街角的那个店\n'
						'看起来像是武器商会啊。{wait}'
						'{page}'
						'#0000F之前也听课长说起过，\n'
						'去里面看看吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FORK', 258, 1, [
						Insn('CHAR_WATCH', Char(254), Char(24), 500),
					]),
					Insn('FORK', 259, 1, [
						Insn('CHAR_WATCH', Char(254), Char(24), 500),
					]),
					Insn('FORK', 260, 1, [
						Insn('CHAR_WATCH', Char(254), Char(24), 500),
					]),
					Insn('FORK_AWAIT', Char(258), 1),
					Insn('FORK_AWAIT', Char(259), 1),
					Insn('FORK_AWAIT', Char(260), 1),
					Insn('TEXT_TALK', Char(258), Text(
						'#0100F也是呢，进去看看吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F噢……等一下。\n'
						'街角的那个店好像是武器商会啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FORK', 258, 1, [
						Insn('CHAR_WATCH', Char(254), Char(24), 500),
					]),
					Insn('FORK', 259, 1, [
						Insn('CHAR_WATCH', Char(254), Char(24), 500),
					]),
					Insn('FORK', 260, 1, [
						Insn('CHAR_WATCH', Char(254), Char(24), 500),
					]),
					Insn('FORK_AWAIT', Char(258), 1),
					Insn('FORK_AWAIT', Char(259), 1),
					Insn('FORK_AWAIT', Char(260), 1),
					Insn('IF', [
						(Expr([Insn('ATTR', 10), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
							Insn('TEXT_TALK', Char(259), Text(
								'#0203F好像是呢。{wait}'
								'{page}'
								'#0200F了解，先去武器\n'
								'商会看看吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(Expr([Insn('ATTR', 10), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
							Insn('TEXT_TALK', Char(260), Text(
								'#0305F哦，看来没错呢。{wait}'
								'{page}'
								'#0300F嗯，那就先去武器商会\n'
								'里面看看吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('TEXT_TALK', Char(258), Text(
								'#0105F啊，真的呢……{wait}'
								'{page}'
								'#0100F那就先进去\n'
								'看看吧。{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
				]),
			]),
			Insn('FLAG_SET', Flag(11)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F街角的那个店\n'
				'好像是武器商会。{wait}'
				'{page}'
				'之前也听课长说起过，\n'
				'先去里面看看吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('CHAR_SET_POS', Char(0), (-8660, -4200, -18220), 180),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x2E', b'\x9e\xff\xff'),
	Insn('CAM_OFFSET', (-640, 1500, 12830), 0),
	Insn('CAM_ROTATE', 45, 28, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 17000, 0),
	Insn('CHAR_FLAG1_UNSET', Char(4), 128),
	Insn('CHAR_FLAG2_UNSET', Char(4), 32768),
	Insn('CHAR_SET_POS', Char(257), (0, 0, 14500), 180),
	Insn('CHAR_SET_POS', Char(415), (750, 0, 13750), 270),
	Insn('CHAR_SET_POS', Char(265), (750, 0, 12750), 315),
	Insn('CHAR_SET_POS', Char(258), (-1250, 0, 14250), 135),
	Insn('CHAR_SET_POS', Char(259), (-1500, 0, 13000), 90),
	Insn('CHAR_SET_POS', Char(260), (-1250, 0, 12000), 45),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0000F那么，我们赶快去\n'
		'挑选礼物吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0303F话虽如此，但我们已经没有时间了啊。{wait}'
		'{page}'
		'#0300F小芙兰\n'
		'不是应该已经前往\n'
		'餐厅了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#5P#0103F是啊……如果让应邀而来的\n'
		'芙兰小姐久等，\n'
		'也很过意不去呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(415), Text(
		'#11P那、那么……\n'
		'该怎么办才好呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0203F还是先来分工吧。{wait}'
		'{page}'
		'#0200F我和艾莉前辈、兰迪前辈\n'
		'先去餐厅。{wait}'
		'{page}'
		'跟芙兰小姐说你们\n'
		'会晚一点到。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0003F在这期间，我和上士\n'
		'还有安敦先生\n'
		'赶快去挑选礼物……{wait}'
		'{page}'
		'#0000F……这样安排似乎比较好呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(415), Text(
		'#11P太谢谢了，\n'
		'该怎么感谢你们大家……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(415), Text(
		'#11P我的运气实在太好了啊，\n'
		'竟然有幸得到如此亲切\n'
		'之人的帮助……{wait}'
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
	Insn('EMOTE', Char(265), 0, 2000, (16, 19, 250, 1)),
	Insn('SOUND_PLAY', 23, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(265), Text(
		'#11P#0506F请、请不要眼泪汪汪啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(259), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0003F总、总之，\n'
		'就这么分工吧。{wait}'
		'{page}'
		'#0000F艾莉、缇欧、兰迪，\n'
		'那边就拜托你们了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(258), Char(257), 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(259), Char(257), 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(260), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('TEXT_TALK', Char(258), Text(
		'#5P#0100F明白了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#6P#0200F那么，稍后见。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0300F一定要选个能\n'
		'让她发自内心地感到惊喜的\n'
		'好礼物哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 259, 1, [
		Insn('0x97', Char(259), (-7000, 0, 0), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('0x97', Char(260), (-7000, 0, 0), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('0x97', Char(258), (-7000, 0, 0), 2000, 0),
	]),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(257), 270, 500),
	]),
	Insn('FORK', 265, 1, [
		Insn('CHAR_ROTATE', Char(265), 270, 500),
	]),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(265), 1),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(257), Char(265), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 265, 1, [
		Insn('CHAR_WATCH', Char(265), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(265), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#5P#0000F那么，我们就\n'
		'去百货看看吧。{wait}'
		'{page}'
		'上士，请你帮忙推荐一些\n'
		'芙兰可能会\n'
		'喜欢的礼物吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(265), Text(
		'#11P#0506F……唉，没办法，我也来帮忙吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(415), Char(265), 500),
	Insn('TEXT_TALK', Char(415), Text(
		'#11P拜托了啊，姐姐！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-10, 2700, 26140), 0),
	Insn('CAM_ROTATE', 45, 21, 0, 0),
	Insn('0x6E', 500, 0),
	Insn('CAM_DISTANCE', 17500, 0),
	Insn('CHAR_SET_POS', Char(257), (0, 800, 24000), 0),
	Insn('CHAR_SET_POS', Char(265), (750, 800, 23250), 0),
	Insn('CHAR_SET_POS', Char(415), (-750, 800, 22500), 0),
	Insn('FORK', 257, 1, [
		Insn('0x97', Char(257), (0, 0, 5000), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 265, 1, [
		Insn('0x97', Char(265), (0, 0, 5000), 2000, 0),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 415, 1, [
		Insn('0x97', Char(415), (0, 0, 5000), 2000, 0),
	]),
	Insn('0x0D'),
	Insn('OBJ_FLAG_UNSET', Object(4), 16),
	Insn('0x71', Object(4), b'\x00\x00', 5, 0),
	Insn('SOUND_PLAY', 100, 0, 0, 100),
	Insn('SLEEP', 750),
	Insn('FORK', 257, 2, [
		Insn('CHAR_SET_COLOR', Char(257), Color(0x00FFFFFF), 1000),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 265, 2, [
		Insn('CHAR_SET_COLOR', Char(265), Color(0x00FFFFFF), 1000),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 415, 2, [
		Insn('CHAR_SET_COLOR', Char(415), Color(0x00FFFFFF), 1000),
	]),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(257), 2),
	Insn('FORK_QUIT', Char(265), 1),
	Insn('FORK_QUIT', Char(265), 2),
	Insn('FORK_QUIT', Char(415), 1),
	Insn('FORK_QUIT', Char(415), 2),
	Insn('MINIGAME', 24, 0, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
	Insn('PARTY_CLEAR'),
	Insn('0x2E', b'\x00\xff\xff'),
	Insn('0x2E', b'\x08\xff\xff'),
	Insn('0x2E', b'\x9e\xff\xff'),
	Insn('QUEST', 42, Insn('TASK_SET', 3)),
	Insn('NEW_SCENE', 'c0170', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]
