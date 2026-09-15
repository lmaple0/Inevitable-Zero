# pyright: reportImplicitStringConcatenation=none
import typing as T
if T.TYPE_CHECKING:
	from ..insn import Insn, Expr, Text, Translate, Char, Flag, Function, Color, Party, ResId, Object

data = {
	'name1': 'r1500',
	'name2': 'r1500',
	'location': 96,
	'bgm': 200,
	'flags': 0,
	'includes': [
		'r1500',
		'r0000_1',
		None,
		None,
		None,
		None,
	],
	'name3': 'r1500',
	'labels': [
		{
			'pos': (2.0, 0.0, 20.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('克洛斯贝尔市方向'),
		},
		{
			'pos': (-27.0, 0.0, -159.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('乌尔斯拉医科大学方向'),
		},
		{
			'pos': (45.0, 0.0, -24.0),
			'unk': b'\x00\x00\x00\x00',
			'name': Translate('克洛斯贝尔机场方向'),
		},
		{
			'pos': (-10.649999618530273, 0.0, -11.800000190734863),
			'unk': b'\x00\x00U\x00',
			'name': Translate(''),
		},
		{
			'pos': (8.25, 0.0, -10.0),
			'unk': b'\x00\x00V\x00',
			'name': Translate(''),
		},
	],
	'chcp': [
		'chr/ch28100',
		'chr/ch21900',
		'chr/ch20800',
		'chr/ch24400',
		'chr/ch20500',
		'chr/ch21600',
		'chr/ch21100',
		'chr/ch23600',
		'chr/ch21200',
		'chr/ch21300',
		'chr/ch21000',
		'chr/ch20700',
		'chr/ch20300',
		'chr/ch21800',
		'chr/ch20000',
		'chr/ch20100',
		'chr/ch20200',
		'chr/ch20400',
		'chr/ch23700',
		'chr/ch24500',
		'chr/ch27800',
		'chr/ch28100',
		'chr/ch30200',
		'chr/ch30500',
		'chr/ch30300',
		'chr/ch26800',
		'chr/ch22100',
		'chr/ch00000',
		'chr/ch00000',
		'chr/ch00000',
		'monster/ch62150',
		'monster/ch62151',
		'monster/ch66650',
		'monster/ch66651',
		'monster/ch63650',
		'monster/ch63650',
		'monster/ch65850',
		'monster/ch65851',
		'monster/ch69750',
		'monster/ch69750',
	],
	'npcs': [
		{
			'name': Translate('市民'),
			'pos': (-9779, 180, -10890),
			'angle': 135,
			'_1': b'\x85\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 35)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (-9560, 180, -8470),
			'angle': 135,
			'_1': b'\x85\x01\x00\x00\x02\x00\x00\x00',
			'function': Function((0, 36)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (-9479, 180, -7039),
			'angle': 315,
			'_1': b'\x85\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 37)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (-9409, 180, -5860),
			'angle': 225,
			'_1': b'\x85\x01\x00\x00\x04\x00\x00\x00',
			'function': Function((0, 38)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (-8899, 180, -4000),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x05\x00\x00\x00',
			'function': Function((0, 39)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (-7699, 180, -4000),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x06\x00\x00\x00',
			'function': Function((0, 40)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (-10020, 180, -9489),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x07\x00\x00\x00',
			'function': Function((0, 41)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('搜查官'),
			'pos': (12989, 0, -17559),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x14\x00\x00\x00',
			'function': Function((0, 42)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (-9810, 180, -9920),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\t\x00\x00\x00',
			'function': Function((0, 43)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (-7010, 180, -4260),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\n\x00\x00\x00',
			'function': Function((0, 44)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('女孩'),
			'pos': (9979, 0, -14819),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x0b\x00\x00\x00',
			'function': Function((0, 11)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (9859, 0, -16450),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x0c\x00\x00\x00',
			'function': Function((0, 12)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (10609, 0, -14939),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\r\x00\x00\x00',
			'function': Function((0, 13)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (10609, 0, -14939),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\t\x00\x00\x00',
			'function': Function((0, 14)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (10609, 0, -14939),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 15)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (9979, 0, -14819),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x0e\x00\x00\x00',
			'function': Function((0, 16)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (9859, 0, -16450),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x0f\x00\x00\x00',
			'function': Function((0, 17)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (10609, 0, -14939),
			'angle': 90,
			'_1': b'\x85\x01\x00\x00\x10\x00\x00\x00',
			'function': Function((0, 18)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (10609, 0, -14939),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x19\x00\x00\x00',
			'function': Function((0, 19)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('记者'),
			'pos': (9979, 0, -14819),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\n\x00\x00\x00',
			'function': Function((0, 20)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('记者'),
			'pos': (9859, 0, -16450),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x08\x00\x00\x00',
			'function': Function((0, 21)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (9979, 0, -14819),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 22)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (9859, 0, -16450),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x13\x00\x00\x00',
			'function': Function((0, 23)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (9979, 0, -14819),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x12\x00\x00\x00',
			'function': Function((0, 24)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (9859, 0, -16450),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x1a\x00\x00\x00',
			'function': Function((0, 25)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (5340, 0, -20360),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x13\x00\x00\x00',
			'function': Function((0, 26)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (5340, 0, -19159),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x03\x00\x00\x00',
			'function': Function((0, 27)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (9859, 0, -16450),
			'angle': 0,
			'_1': b'\x85\x01\x00\x00\x01\x00\x00\x00',
			'function': Function((0, 28)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('游客'),
			'pos': (9979, 0, -14819),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\r\x00\x00\x00',
			'function': Function((0, 29)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('市民'),
			'pos': (10609, 0, -14939),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x14\x00\x00\x00',
			'function': Function((0, 30)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('比利'),
			'pos': (4980, 0, -12670),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x07\x00\x00\x00',
			'function': Function((0, 31)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('交通课的职员'),
			'pos': (2210, 0, -34220),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x15\x00\x00\x00',
			'function': Function((0, 32)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('雷蒙德搜查官'),
			'pos': (-5639, 180, -4260),
			'angle': 270,
			'_1': b'\x85\x01\x00\x00\x16\x00\x00\x00',
			'function': Function((0, 34)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('艾玛搜查官'),
			'pos': (13060, 0, -16149),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x17\x00\x00\x00',
			'function': Function((0, 45)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('多诺邦警部'),
			'pos': (11449, 0, -15000),
			'angle': 180,
			'_1': b'\x85\x01\x00\x00\x18\x00\x00\x00',
			'function': Function((0, 33)),
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
			'name': Translate('巴士站'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x01\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('巴士站'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x02\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('巴士站'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x03\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('巴士站'),
			'pos': (0, 0, 0),
			'angle': 0,
			'_1': b'\xc5\x01\x00\x00\x04\x00\xff\xff',
			'function': Function((255, 255)),
			'_2': b'\xff\x00\x00\x00',
		},
		{
			'name': Translate('交通课的职员'),
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
			'name': Translate('比利的货车'),
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
	'monsters': [
		{
			'pos': (-18740, 0, -70990),
			'angle': 0,
			'unk1': 257,
			'battle': {
				'flags': 0,
				'level': 12,
				'unk': 6,
				'vision': 45,
				'moveRange': 10,
				'canMove': 1,
				'moveSpeed': 30,
				'unk2': 0,
				'battlefield': 'br1500',
				'sepith': (4, 2, 0, 8, 0, 3, 2),
				'setups': [
					(30, {
						'enemies': [
							('ms62100', (8, 8, 180), (7, 4, 0)),
							(None, (5, 9, 180), (10, 11, 225)),
							(None, (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(45, {
						'enemies': [
							('ms62100', (7, 9, 180), (7, 4, 0)),
							('ms62100', (11, 10, 180), (10, 11, 225)),
							(None, (10, 13, 180), (4, 7, 90)),
							(None, (5, 11, 180), (12, 7, 270)),
							(None, (12, 12, 180), (4, 11, 135)),
							(None, (4, 14, 180), (11, 4, 315)),
							(None, (14, 14, 180), (7, 12, 180)),
							(None, (2, 13, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(20, {
						'enemies': [
							('ms62100', (8, 8, 180), (7, 4, 0)),
							('ms69700', (5, 9, 180), (10, 11, 225)),
							('ms62100', (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(5, {
						'enemies': [
							('ms62100', (7, 9, 180), (7, 4, 0)),
							('ms62100', (11, 10, 180), (10, 11, 225)),
							('ms65800', (10, 13, 180), (4, 7, 90)),
							('ms62100', (5, 11, 180), (12, 7, 270)),
							(None, (12, 12, 180), (4, 11, 135)),
							(None, (4, 14, 180), (11, 4, 315)),
							(None, (14, 14, 180), (7, 12, 180)),
							(None, (2, 13, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
				],
			},
			'flag': 0,
			'chcpIdx': 30,
			'standAnim': 0,
			'moveAnim': 1,
		},
		{
			'pos': (-19320, 10, -73460),
			'angle': 0,
			'unk1': 257,
			'battle': {
				'flags': 0,
				'level': 12,
				'unk': 6,
				'vision': 45,
				'moveRange': 10,
				'canMove': 1,
				'moveSpeed': 30,
				'unk2': 0,
				'battlefield': 'br1500',
				'sepith': (4, 2, 0, 8, 0, 3, 2),
				'setups': [
					(30, {
						'enemies': [
							('ms62100', (8, 8, 180), (7, 4, 0)),
							(None, (5, 9, 180), (10, 11, 225)),
							(None, (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(45, {
						'enemies': [
							('ms62100', (7, 9, 180), (7, 4, 0)),
							('ms62100', (11, 10, 180), (10, 11, 225)),
							(None, (10, 13, 180), (4, 7, 90)),
							(None, (5, 11, 180), (12, 7, 270)),
							(None, (12, 12, 180), (4, 11, 135)),
							(None, (4, 14, 180), (11, 4, 315)),
							(None, (14, 14, 180), (7, 12, 180)),
							(None, (2, 13, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(20, {
						'enemies': [
							('ms62100', (8, 8, 180), (7, 4, 0)),
							('ms69700', (5, 9, 180), (10, 11, 225)),
							('ms62100', (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(5, {
						'enemies': [
							('ms62100', (7, 9, 180), (7, 4, 0)),
							('ms62100', (11, 10, 180), (10, 11, 225)),
							('ms65800', (10, 13, 180), (4, 7, 90)),
							('ms62100', (5, 11, 180), (12, 7, 270)),
							(None, (12, 12, 180), (4, 11, 135)),
							(None, (4, 14, 180), (11, 4, 315)),
							(None, (14, 14, 180), (7, 12, 180)),
							(None, (2, 13, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
				],
			},
			'flag': 0,
			'chcpIdx': 30,
			'standAnim': 0,
			'moveAnim': 1,
		},
		{
			'pos': (-9910, 10, -96620),
			'angle': 0,
			'unk1': 257,
			'battle': {
				'flags': 0,
				'level': 12,
				'unk': 6,
				'vision': 45,
				'moveRange': 10,
				'canMove': 1,
				'moveSpeed': 25,
				'unk2': 0,
				'battlefield': 'br1500',
				'sepith': (8, 2, 0, 0, 3, 0, 5),
				'setups': [
					(30, {
						'enemies': [
							('ms65800', (8, 8, 180), (7, 4, 0)),
							(None, (5, 9, 180), (10, 11, 225)),
							(None, (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(45, {
						'enemies': [
							('ms65800', (8, 8, 180), (7, 4, 0)),
							('ms65800', (5, 9, 180), (10, 11, 225)),
							(None, (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(20, {
						'enemies': [
							('ms65800', (8, 8, 180), (7, 4, 0)),
							('ms63600', (5, 9, 180), (10, 11, 225)),
							('ms65800', (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(5, {
						'enemies': [
							('ms65800', (8, 8, 180), (7, 4, 0)),
							('ms65800', (5, 9, 180), (10, 11, 225)),
							('ms66600', (11, 10, 180), (4, 7, 90)),
							('ms65800', (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
				],
			},
			'flag': 0,
			'chcpIdx': 36,
			'standAnim': 6,
			'moveAnim': 7,
		},
		{
			'pos': (-20260, 0, -97980),
			'angle': 0,
			'unk1': 257,
			'battle': {
				'flags': 16,
				'level': 12,
				'unk': 6,
				'vision': 45,
				'moveRange': 10,
				'canMove': 1,
				'moveSpeed': 30,
				'unk2': 0,
				'battlefield': 'br1500',
				'sepith': (0, 8, 0, 4, 4, 2, 0),
				'setups': [
					(60, {
						'enemies': [
							('ms63600', (8, 8, 180), (7, 4, 0)),
							('ms63600', (5, 9, 180), (10, 11, 225)),
							('ms63600', (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							('ms63600', (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(25, {
						'enemies': [
							('ms63600', (7, 9, 180), (7, 4, 0)),
							('ms63600', (11, 10, 180), (10, 11, 225)),
							('ms63600', (10, 13, 180), (4, 7, 90)),
							('ms63600', (5, 11, 180), (12, 7, 270)),
							(None, (12, 12, 180), (4, 11, 135)),
							(None, (4, 14, 180), (11, 4, 315)),
							('ms63600', (14, 14, 180), (7, 12, 180)),
							(None, (2, 13, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(10, {
						'enemies': [
							('ms63600', (8, 8, 180), (7, 4, 0)),
							('ms66600', (5, 9, 180), (10, 11, 225)),
							('ms63600', (11, 10, 180), (4, 7, 90)),
							('ms63600', (6, 12, 180), (12, 7, 270)),
							('ms63600', (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							('ms63600', (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(5, {
						'enemies': [
							('ms63600', (7, 9, 180), (7, 4, 0)),
							('ms63600', (11, 10, 180), (10, 11, 225)),
							('ms62100', (10, 13, 180), (4, 7, 90)),
							('ms63600', (5, 11, 180), (12, 7, 270)),
							('ms63600', (12, 12, 180), (4, 11, 135)),
							('ms63600', (4, 14, 180), (11, 4, 315)),
							('ms63600', (14, 14, 180), (7, 12, 180)),
							(None, (2, 13, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
				],
			},
			'flag': 0,
			'chcpIdx': 34,
			'standAnim': 4,
			'moveAnim': 5,
		},
		{
			'pos': (16920, 10, -84000),
			'angle': 0,
			'unk1': 257,
			'battle': {
				'flags': 0,
				'level': 12,
				'unk': 6,
				'vision': 45,
				'moveRange': 10,
				'canMove': 1,
				'moveSpeed': 25,
				'unk2': 0,
				'battlefield': 'br1500',
				'sepith': (8, 2, 0, 0, 3, 0, 5),
				'setups': [
					(30, {
						'enemies': [
							('ms65800', (8, 8, 180), (7, 4, 0)),
							(None, (5, 9, 180), (10, 11, 225)),
							(None, (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(45, {
						'enemies': [
							('ms65800', (8, 8, 180), (7, 4, 0)),
							('ms65800', (5, 9, 180), (10, 11, 225)),
							(None, (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(20, {
						'enemies': [
							('ms65800', (8, 8, 180), (7, 4, 0)),
							('ms63600', (5, 9, 180), (10, 11, 225)),
							('ms65800', (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(5, {
						'enemies': [
							('ms65800', (8, 8, 180), (7, 4, 0)),
							('ms65800', (5, 9, 180), (10, 11, 225)),
							('ms66600', (11, 10, 180), (4, 7, 90)),
							('ms65800', (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
				],
			},
			'flag': 0,
			'chcpIdx': 36,
			'standAnim': 6,
			'moveAnim': 7,
		},
		{
			'pos': (22580, 10, -65740),
			'angle': 0,
			'unk1': 257,
			'battle': {
				'flags': 0,
				'level': 12,
				'unk': 6,
				'vision': 45,
				'moveRange': 10,
				'canMove': 1,
				'moveSpeed': 45,
				'unk2': 0,
				'battlefield': 'br1500',
				'sepith': (8, 0, 5, 2, 0, 0, 4),
				'setups': [
					(30, {
						'enemies': [
							('ms66600', (8, 8, 180), (7, 4, 0)),
							(None, (5, 9, 180), (10, 11, 225)),
							(None, (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(45, {
						'enemies': [
							('ms66600', (7, 9, 180), (7, 4, 0)),
							('ms66600', (11, 10, 180), (10, 11, 225)),
							(None, (10, 13, 180), (4, 7, 90)),
							(None, (5, 11, 180), (12, 7, 270)),
							(None, (12, 12, 180), (4, 11, 135)),
							(None, (4, 14, 180), (11, 4, 315)),
							(None, (14, 14, 180), (7, 12, 180)),
							(None, (2, 13, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(20, {
						'enemies': [
							('ms66600', (8, 8, 180), (7, 4, 0)),
							('ms62100', (5, 9, 180), (10, 11, 225)),
							('ms66600', (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(5, {
						'enemies': [
							('ms66600', (7, 9, 180), (7, 4, 0)),
							('ms66600', (11, 10, 180), (10, 11, 225)),
							('ms69700', (10, 13, 180), (4, 7, 90)),
							('ms66600', (5, 11, 180), (12, 7, 270)),
							(None, (12, 12, 180), (4, 11, 135)),
							(None, (4, 14, 180), (11, 4, 315)),
							(None, (14, 14, 180), (7, 12, 180)),
							(None, (2, 13, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
				],
			},
			'flag': 0,
			'chcpIdx': 32,
			'standAnim': 2,
			'moveAnim': 3,
		},
		{
			'pos': (32310, 0, -111280),
			'angle': 0,
			'unk1': 257,
			'battle': {
				'flags': 0,
				'level': 12,
				'unk': 6,
				'vision': 45,
				'moveRange': 10,
				'canMove': 1,
				'moveSpeed': 25,
				'unk2': 0,
				'battlefield': 'br1500',
				'sepith': (2, 8, 0, 6, 2, 0, 0),
				'setups': [
					(30, {
						'enemies': [
							('ms69700', (8, 8, 180), (7, 4, 0)),
							(None, (5, 9, 180), (10, 11, 225)),
							(None, (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(45, {
						'enemies': [
							('ms69700', (8, 8, 180), (7, 4, 0)),
							('ms69700', (5, 9, 180), (10, 11, 225)),
							(None, (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(20, {
						'enemies': [
							('ms69700', (8, 8, 180), (7, 4, 0)),
							('ms69700', (5, 9, 180), (10, 11, 225)),
							('ms69900', (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(5, {
						'enemies': [
							('ms69700', (8, 8, 180), (7, 4, 0)),
							('ms69700', (5, 9, 180), (10, 11, 225)),
							('ms69900', (11, 10, 180), (4, 7, 90)),
							('ms69800', (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
				],
			},
			'flag': 0,
			'chcpIdx': 38,
			'standAnim': 8,
			'moveAnim': 9,
		},
		{
			'pos': (46440, 900, -108530),
			'angle': 0,
			'unk1': 257,
			'battle': {
				'flags': 0,
				'level': 12,
				'unk': 6,
				'vision': 45,
				'moveRange': 10,
				'canMove': 1,
				'moveSpeed': 45,
				'unk2': 0,
				'battlefield': 'br1500',
				'sepith': (8, 0, 5, 2, 0, 0, 4),
				'setups': [
					(30, {
						'enemies': [
							('ms66600', (8, 8, 180), (7, 4, 0)),
							(None, (5, 9, 180), (10, 11, 225)),
							(None, (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(45, {
						'enemies': [
							('ms66600', (7, 9, 180), (7, 4, 0)),
							('ms66600', (11, 10, 180), (10, 11, 225)),
							(None, (10, 13, 180), (4, 7, 90)),
							(None, (5, 11, 180), (12, 7, 270)),
							(None, (12, 12, 180), (4, 11, 135)),
							(None, (4, 14, 180), (11, 4, 315)),
							(None, (14, 14, 180), (7, 12, 180)),
							(None, (2, 13, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(20, {
						'enemies': [
							('ms66600', (8, 8, 180), (7, 4, 0)),
							('ms62100', (5, 9, 180), (10, 11, 225)),
							('ms66600', (11, 10, 180), (4, 7, 90)),
							(None, (6, 12, 180), (12, 7, 270)),
							(None, (10, 12, 180), (4, 11, 135)),
							(None, (13, 13, 180), (11, 4, 315)),
							(None, (4, 14, 180), (7, 12, 180)),
							(None, (8, 14, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
					(5, {
						'enemies': [
							('ms66600', (7, 9, 180), (7, 4, 0)),
							('ms66600', (11, 10, 180), (10, 11, 225)),
							('ms69700', (10, 13, 180), (4, 7, 90)),
							('ms66600', (5, 11, 180), (12, 7, 270)),
							(None, (12, 12, 180), (4, 11, 135)),
							(None, (4, 14, 180), (11, 4, 315)),
							(None, (14, 14, 180), (7, 12, 180)),
							(None, (2, 13, 180), (5, 5, 45)),
						],
						'bgm': 400,
						'bgm2': 403,
						'atRoll': {
							'none': 100,
							'hp10': 5,
							'hp50': 1,
							'ep10': 5,
							'ep50': 1,
							'cp10': 5,
							'cp50': 1,
							'sepith_up': 5,
							'critical': 5,
							'vanish': 0,
							'death': 0,
							'guard': 0,
							'rush': 1,
							'arts_guard': 0,
							'teamrush': 0,
							'unknown': 0,
						},
					}),
				],
			},
			'flag': 0,
			'chcpIdx': 32,
			'standAnim': 2,
			'moveAnim': 3,
		},
	],
	'triggers': [
		{
			'pos': (14.0, -17.5, -0.5),
			'range': 100.0,
			'transform': [
				0.5,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.09999999403953552,
				-0.0,
				0.0,
				0.0,
				-0.0,
				0.19999998807907104,
				0.0,
				-7.0,
				1.7499998807907104,
				0.09999999403953552,
				1.0,
			],
			'_1': b'\x00\x00\x00',
			'function': Function((0, 66)),
			'_2': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
		},
	],
	'objects': [
		{
			'pos': (-10300, 180, -13000),
			'range': 1500,
			'bubble_pos': (-10300, 1680, -13000),
			'_1': b'|\x00\x00',
			'function': Function((0, 47)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (53350, 900, -104390),
			'range': 1200,
			'bubble_pos': (67060, -5900, -100200),
			'_1': b'|\x00\x00',
			'function': Function((0, 46)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (22470, 0, -63690),
			'range': 1200,
			'bubble_pos': (22470, 0, -63690),
			'_1': b'|\x00\x00',
			'function': Function((0, 3)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (8160, 0, -11670),
			'range': 1200,
			'bubble_pos': (8160, 2000, -11670),
			'_1': b'|\x00\x00',
			'function': Function((0, 10)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (44690, 900, -108690),
			'range': 7500,
			'bubble_pos': (44690, 900, -108690),
			'_1': b'|\x00\x00',
			'function': Function((0, 64)),
			'_2': b'\x00\x00\x00',
		},
		{
			'pos': (9210, 0, -24210),
			'range': 1500,
			'bubble_pos': (9210, 1700, -24210),
			'_1': b'|\x00\x00',
			'function': Function((0, 69)),
			'_2': b'\x00\x00\x00',
		},
	],
	'unk13': b'\x00\xff\xff',
	'extra': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc4\t\x00\x00\xd0\x84\x00\x00\x06\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x18\x02\xff\xff\x00\x00\x00\x00\x01\x00`\x00', Function((0, 1)), Function((0, 2))),
	'code': [None]*70,
	'anim': [
		{
			'speed': 1000,
			'_': 0,
			'count': 8,
			'frames': [
				0,
				1,
				2,
				3,
				4,
				3,
				2,
				1,
			],
		},
		{
			'speed': 2000,
			'_': 0,
			'count': 8,
			'frames': [
				0,
				1,
				2,
				1,
				0,
				3,
				4,
				3,
			],
		},
		{
			'speed': 1000,
			'_': 0,
			'count': 8,
			'frames': [
				0,
				1,
				2,
				1,
				0,
				3,
				4,
				3,
			],
		},
		{
			'speed': 2000,
			'_': 0,
			'count': 8,
			'frames': [
				0,
				1,
				2,
				1,
				0,
				3,
				4,
				3,
			],
		},
		{
			'speed': 800,
			'_': 0,
			'count': 8,
			'frames': [
				0,
				1,
				2,
				3,
				4,
				5,
				6,
				7,
			],
		},
		{
			'speed': 1500,
			'_': 0,
			'count': 8,
			'frames': [
				0,
				1,
				2,
				3,
				4,
				5,
				6,
				7,
			],
		},
		{
			'speed': 1000,
			'_': 0,
			'count': 8,
			'frames': [
				0,
				1,
				2,
				1,
				0,
				3,
				4,
				3,
			],
		},
		{
			'speed': 2000,
			'_': 0,
			'count': 8,
			'frames': [
				0,
				1,
				2,
				1,
				0,
				3,
				4,
				3,
			],
		},
		{
			'speed': 500,
			'_': 0,
			'count': 6,
			'frames': [
				0,
				1,
				2,
				3,
				4,
				5,
				0,
				0,
			],
		},
		{
			'speed': 1000,
			'_': 0,
			'count': 6,
			'frames': [
				0,
				1,
				2,
				3,
				4,
				5,
				0,
				0,
			],
		},
	],
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
		(Expr([Insn('FLAG', Flag(1106)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(1106)),
			Insn('FLAG_SET', Flag(1107)),
		]),
		(None, []),
	]),
	Insn('0xD0', 7, Expr([Insn('CONST', 13), Insn('SET'), Insn('END')])),
	Insn('FLAG_SET', Flag(1997)),
	Insn('FLAG_SET', Flag(2013)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('FLAG', Flag(1793)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x09', 268435456),
			Insn('EVENT', Function((0, 62))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(736)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(736)),
			Insn('EVENT', Function((0, 50))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_FLAG1_UNSET', Char(14), 128),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_SET_POS', Char(10), (-10010, 180, -11740), 180),
			Insn('CHAR_SET_POS', Char(11), (-10010, 180, -10540), 180),
			Insn('CHAR_SET_POS', Char(14), (-10010, 180, -9240), 180),
			Insn('CHAR_SET_POS', Char(15), (-10010, 180, -8039), 180),
			Insn('CHAR_SET_POS', Char(16), (-10010, 180, -6840), 180),
		]),
		(Expr([Insn('FLAG', Flag(1569)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(40), 128),
			Insn('CHAR_FLAG1_UNSET', Char(41), 128),
			Insn('CHAR_SET_POS', Char(15), (15000, 0, -16570), 0),
			Insn('CHAR_SET_POS', Char(41), (15000, 0, -15170), 180),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(15), 128),
			Insn('CHAR_FLAG1_UNSET', Char(17), 128),
			Insn('CHAR_FLAG1_UNSET', Char(40), 128),
		]),
		(Expr([Insn('FLAG', Flag(1348)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(12), 128),
			Insn('CHAR_FLAG1_UNSET', Char(13), 128),
		]),
		(Expr([Insn('FLAG', Flag(782)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(779)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(39), 128),
		]),
		(Expr([Insn('FLAG', Flag(778)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(8), 128),
			Insn('CHAR_FLAG1_UNSET', Char(9), 128),
			Insn('CHAR_FLAG1_UNSET', Char(10), 128),
			Insn('CHAR_FLAG1_UNSET', Char(11), 128),
			Insn('CHAR_FLAG1_UNSET', Char(16), 128),
			Insn('CHAR_FLAG1_UNSET', Char(39), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1554)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(37), 128),
		]),
		(Expr([Insn('FLAG', Flag(1536)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(36), 128),
			Insn('CHAR_FLAG1_UNSET', Char(35), 128),
			Insn('CHAR_FLAG1_SET', Char(36), 16),
		]),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(38), 128),
			Insn('CHAR_FLAG1_UNSET', Char(34), 128),
			Insn('CHAR_FLAG1_UNSET', Char(33), 128),
			Insn('CHAR_FLAG1_SET', Char(34), 16),
			Insn('CHAR_FLAG1_SET', Char(33), 16),
		]),
		(Expr([Insn('FLAG', Flag(1362)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(32), 128),
			Insn('CHAR_FLAG1_UNSET', Char(31), 128),
			Insn('CHAR_FLAG1_SET', Char(32), 16),
			Insn('CHAR_FLAG1_SET', Char(31), 16),
		]),
		(Expr([Insn('FLAG', Flag(1292)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(30), 128),
			Insn('CHAR_FLAG1_UNSET', Char(29), 128),
		]),
		(Expr([Insn('FLAG', Flag(1282)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(28), 128),
			Insn('CHAR_FLAG1_UNSET', Char(27), 128),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 27, Insn('TASK_GET', 1))), Insn('EXEC', Insn('QUEST_GET', 27, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
					Insn('CHAR_FLAG1_UNSET', Char(40), 128),
					Insn('CHAR_SET_POS', Char(40), (11450, 0, -16500), 0),
					Insn('CHAR_FLAG1_UNSET', Char(42), 128),
				]),
				(None, []),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(26), 128),
		]),
		(Expr([Insn('FLAG', Flag(1055)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(25), 128),
		]),
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(24), 128),
			Insn('CHAR_FLAG1_UNSET', Char(23), 128),
		]),
		(Expr([Insn('FLAG', Flag(1031)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(22), 128),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(21), 128),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(20), 128),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('END')]), [
			Insn('CHAR_FLAG1_UNSET', Char(18), 128),
			Insn('CHAR_FLAG1_UNSET', Char(19), 128),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1040)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1031)), Insn('FLAG', Flag(1024)), Insn('OR'), Insn('END')]), [
			Insn('EVENT', Function((0, 4))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1024)), Insn('FLAG', Flag(1280)), Insn('NOT'), Insn('BOOL_AND'), Insn('FLAG', Flag(1183)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('EVENT', Function((0, 63))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1008)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(1008)),
			Insn('EVENT', Function((0, 7))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1009)), Insn('END')]), [
			Insn('FLAG_UNSET', Flag(1009)),
			Insn('0xD0', 1, Expr([Insn('CONST', 4), Insn('SET'), Insn('END')])),
			Insn('EVENT', Function((0, 9))),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 0), Insn('EQ'), Insn('ATTR', 0), Insn('CONST', 100), Insn('EQ'), Insn('OR'), Insn('ATTR', 0), Insn('CONST', 105), Insn('EQ'), Insn('OR'), Insn('ATTR', 0), Insn('CONST', 103), Insn('EQ'), Insn('OR'), Insn('END')]), [
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
			Insn('EXPR_VAR', 3, Expr([Insn('RAND'), Insn('CONST', 8), Insn('MOD'), Insn('SET'), Insn('END')])),
			Insn('IF', [
				(Expr([Insn('VAR', 3), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(992)),
				]),
				(Expr([Insn('VAR', 3), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(993)),
				]),
				(Expr([Insn('VAR', 3), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(994)),
				]),
				(Expr([Insn('VAR', 3), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(995)),
				]),
				(Expr([Insn('VAR', 3), Insn('CONST', 4), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(996)),
				]),
				(Expr([Insn('VAR', 3), Insn('CONST', 5), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(997)),
				]),
				(Expr([Insn('VAR', 3), Insn('CONST', 6), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(998)),
				]),
				(Expr([Insn('VAR', 3), Insn('CONST', 7), Insn('EQ'), Insn('END')]), [
					Insn('FLAG_SET', Flag(999)),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('RETURN'),
]

data['code'][2] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1793)), Insn('NOT'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('ATTR', 0), Insn('CONST', 100), Insn('EQ'), Insn('ATTR', 0), Insn('CONST', 102), Insn('EQ'), Insn('OR'), Insn('ATTR', 0), Insn('CONST', 104), Insn('EQ'), Insn('OR'), Insn('ATTR', 0), Insn('CONST', 105), Insn('EQ'), Insn('OR'), Insn('ATTR', 0), Insn('CONST', 0), Insn('EQ'), Insn('OR'), Insn('END')]), [
					Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 100), Insn('SET'), Insn('END')])),
				]),
				(None, [
					Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 200), Insn('SET'), Insn('END')])),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1793)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('ATTR', 0), Insn('CONST', 100), Insn('EQ'), Insn('ATTR', 0), Insn('CONST', 102), Insn('EQ'), Insn('OR'), Insn('ATTR', 0), Insn('CONST', 104), Insn('EQ'), Insn('OR'), Insn('ATTR', 0), Insn('CONST', 105), Insn('EQ'), Insn('OR'), Insn('ATTR', 0), Insn('CONST', 0), Insn('EQ'), Insn('OR'), Insn('END')]), [
					Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 200), Insn('SET'), Insn('END')])),
				]),
				(None, [
					Insn('EXPR_ATTR', 1, Expr([Insn('CONST', 200), Insn('SET'), Insn('END')])),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('ATTR', 4), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
			Insn('EXIT_SET_ENABLED', 0, 0),
			Insn('EXIT_SET_ENABLED', 5, 1),
		]),
		(None, [
			Insn('EXIT_SET_ENABLED', 0, 1),
			Insn('EXIT_SET_ENABLED', 5, 0),
		]),
	]),
	Insn('OBJ_FLAG_SET', Object(1), 4),
	Insn('OBJ_FLAG_SET', Object(2), 4),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 100), Insn('EQ'), Insn('ATTR', 0), Insn('CONST', 102), Insn('EQ'), Insn('OR'), Insn('ATTR', 0), Insn('CONST', 104), Insn('EQ'), Insn('OR'), Insn('ATTR', 0), Insn('CONST', 105), Insn('EQ'), Insn('OR'), Insn('ATTR', 0), Insn('CONST', 0), Insn('EQ'), Insn('OR'), Insn('END')]), [
			Insn('0x09', 8192),
			Insn('0xE0', b'\x01'),
			Insn('FLAG_UNSET', Flag(8)),
		]),
		(None, [
			Insn('0x0A', 8192),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(8)), Insn('NOT'), Insn('END')]), [
					Insn('0xE0', b'\x00'),
					Insn('FLAG_SET', Flag(8)),
				]),
				(None, []),
			]),
		]),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1307)), Insn('END')]), [
			Insn('OBJ_FLAG_UNSET', Object(2), 4),
			Insn('OBJ_SET_FRAME', Object(2), 'light', Insn('0', 1)),
			Insn('OBJ_FLAG_SET', Object(2), 2),
		]),
		(None, []),
	]),
	Insn('OBJ_FLAG_SET', Object(0), 4),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
			Insn('0x11', b'\xd2\xae\x9b', 5, 400, 0),
			Insn('OBJ_SET_FRAME', Object(255), 'sky', Insn('2', 'red')),
			Insn('OBJ_SET_FRAME', Object(255), 'water00', Insn('2', 'red')),
			Insn('OBJ_SET_FRAME', Object(255), 'water01', Insn('2', 'red')),
		]),
		(None, []),
	]),
	Insn('0x65', 4, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('END')]), []),
		(Expr([Insn('FLAG', Flag(1280)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 24, Insn('FLAG_GET', 16))), Insn('END')]), []),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 4))), Insn('END')]), []),
				(Expr([Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 1))), Insn('END')]), [
					Insn('0x66', 4, 1),
					Insn('0x65', 1, 1),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('OBJ_FLAG_SET', Object(3), 4),
	Insn('0x65', 3, 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1537)), Insn('FLAG', Flag(1542)), Insn('NOT'), Insn('BOOL_AND'), Insn('0x23', 1), Insn('CONST', 4), Insn('EQ'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('OBJ_SET_FRAME', Object(3), 'light', Insn('0', 1)),
			Insn('OBJ_FLAG_UNSET', Object(3), 4),
			Insn('0x66', 3, 1),
		]),
		(None, [
			Insn('0x16', Insn('3', b'\x04\x01\x00')),
		]),
	]),
	Insn('0x1B', 4, Function((255, 255)), 255),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(525)), Insn('FLAG', Flag(1342)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 34, Insn('TASK_GET', 3))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 4, Function((0, 65)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 45, Insn('TASK_GET', 8))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 4, Function((0, 65)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('FLAG', Flag(1569)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 4, Function((0, 65)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1569)), Insn('FLAG', Flag(1792)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 4, Function((0, 65)), 0),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1611)), Insn('NOT'), Insn('END')]), [
					Insn('0xB5', b'\x01\x00\x80\x00'),
				]),
				(None, []),
			]),
		]),
		(None, []),
	]),
	Insn('0x1B', 2, Function((255, 255)), 255),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1560)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 48, Insn('TASK_GET', 5))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 48, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 2, Function((0, 67)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(768)), Insn('FLAG', Flag(778)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 2, Function((0, 67)), 0),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x1B', 2, Function((0, 67)), 0),
		]),
		(None, []),
	]),
	Insn('0x65', 2, 1),
	Insn('EFF_LOAD', ResId(9), 'event\\eva00_00.eff'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(976)), Insn('END')]), [
			Insn('EFF_PLAY', (ResId(9), 9), Char(255), 0, 22470, 0, 0, 0, 1846, -1, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
			Insn('0x66', 2, 1),
		]),
		(None, []),
	]),
	Insn('EFF_LOAD', ResId(8), 'eff\\mgm03_02.eff'),
	Insn('EFF_PLAY', (ResId(8), 8), Char(255), 0, 1524, 1, -5900, -1, 30872, -2, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
	Insn('IF', [
		(Expr([Insn('ATTR', 0), Insn('CONST', 100), Insn('EQ'), Insn('ATTR', 0), Insn('CONST', 102), Insn('EQ'), Insn('OR'), Insn('ATTR', 0), Insn('CONST', 104), Insn('EQ'), Insn('OR'), Insn('ATTR', 0), Insn('CONST', 105), Insn('EQ'), Insn('OR'), Insn('ATTR', 0), Insn('CONST', 0), Insn('EQ'), Insn('OR'), Insn('END')]), [
			Insn('SOUND_STOP', 125),
		]),
		(None, [
			Insn('SOUND_POSITION', 125, [
				13510,
				0,
				-160490,
				90000,
				70000,
			], 100, 0),
			Insn('0xE1', (40270, 280, -128759)),
			Insn('0xE1', (57450, 900, -93640)),
			Insn('0xE1', (64730, 90, -55250)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][3] = [
	Insn('TEXT_START', Char(255)),
	Insn('CALL', Function((1, 0))),
	Insn('FLAG_UNSET', Flag(976)),
	Insn('0x65', 2, 1),
	Insn('EFF_STOP', (ResId(9), 2)),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][4] = [
	Insn('CHAR_FLAG1_UNSET', Char(50), 128),
	Insn('CHAR_FLAG1_SET', Char(50), 32768),
	Insn('OBJ_FLAG_UNSET', Object(2), 4),
	Insn('OBJ_SET_FRAME', Object(2), 'light', Insn('0', 1)),
	Insn('OBJ_FLAG_SET', Object(2), 4096),
	Insn('0x78', b'\x02', Char(50)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(50), (2000, 1000, 14000), 0),
	Insn('0xD3', Char(50), 0, 180000, 0, 0),
	Insn('RETURN'),
]

data['code'][5] = [
	Insn('EVENT_BEGIN', 1),
	Insn('0x09', 134217728),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}有一个巴士站。\n'
		'要乘坐巴士吗？{wait}'
	)),
	Insn('MENU', 0, -1, -1, 1, Text(
		'圣乌尔斯拉医科大学\n'
		'岔口停靠站（沙洲附近）\n'
		'放弃\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('CALL', Function((0, 6))),
			Insn('0x0A', 134217728),
			Insn('NEW_SCENE', 't1500', b'\x00\x00\x00\x07'),
		]),
		(Expr([Insn('VAR', 0), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
			Insn('CALL', Function((0, 6))),
			Insn('0x0A', 134217728),
			Insn('NEW_SCENE', 'r1530', b'\x00\x00\x00\x07'),
		]),
		(None, []),
	]),
	Insn('0x0A', 134217728),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][6] = [
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (0, 600, -32000), 0),
	Insn('CAM_ROTATE', 45, 21, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('0xE0', b'\x01'),
	Insn('CHAR_SET_POS', Char(0), (-9800, 180, -11100), 89),
	Insn('CHAR_SET_POS', Char(1), (-9800, 180, -10100), 89),
	Insn('CHAR_SET_POS', Char(2), (-9800, 180, -9100), 89),
	Insn('CHAR_SET_POS', Char(3), (-9800, 180, -8100), 89),
	Insn('CHAR_FLAG1_UNSET', Char(43), 128),
	Insn('CHAR_FLAG1_SET', Char(43), 32768),
	Insn('OBJ_FLAG_UNSET', Object(1), 4),
	Insn('OBJ_FLAG_SET', Object(1), 4096),
	Insn('0x78', b'\x01', Char(43)),
	Insn('OBJ_SET_FRAME', Object(1), 'light', Insn('0', 1)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(43), (0, 0, -40000), 0),
	Insn('0xD3', Char(43), 0, 0, 0, 0),
	Insn('0x74', Object(1), 7680),
	Insn('0x71', Object(1), b'y\x00', 180, 32),
	Insn('FORK', 43, 1, [
		Insn('0x98', Char(254), (0, 0, 30000), 4000, 0),
	]),
	Insn('SOUND_PLAY', 466, 0, 0, 100),
	Insn('SOUND_PLAY', 467, 0, 0, 100),
	Insn('SLEEP', 2500),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-10500, 780, -11600), 0),
	Insn('CAM_ROTATE', 45, 21, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('CHAR_SET_POS', Char(43), (-6300, 0, -21000), 0),
	Insn('FORK', 43, 1, [
		Insn('0x96', Char(254), (-6300, 0, -11500), 4000, 0),
	]),
	Insn('FORK_AWAIT', Char(43), 1),
	Insn('0x71', Object(1), b'[\x00', 120, 0),
	Insn('0x79', b'\x01\x00'),
	Insn('0x0D'),
	Insn('SLEEP', 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FLAG_SET', Flag(1008)),
	Insn('RETURN'),
]

data['code'][7] = [
	Insn('EVENT_BEGIN', 1),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('CHAR_SET_POS', Char(0), (-9830, 180, -11430), 90),
	Insn('CHAR_SET_POS', Char(1), (-9830, 180, -11430), 90),
	Insn('CHAR_SET_POS', Char(2), (-9830, 180, -11430), 90),
	Insn('CHAR_SET_POS', Char(3), (-9830, 180, -11430), 90),
	Insn('CAM_OFFSET', (-9830, 780, -11430), 0),
	Insn('CAM_ROTATE', 45, 21, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][8] = [
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
					(Expr([Insn('VAR', 4), Insn('CONST', 1), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄中央广场'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 0)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄中央广场'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄东出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 1)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄东出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 3), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄西出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 2)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄西出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 4), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄南出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 3)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄南出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 5), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★克洛斯贝尔市丄北出口'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 4)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000克洛斯贝尔市丄北出口'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 6), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★唐古拉姆门'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 5)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000唐古拉姆门'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 7), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★贝尔加德门'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 6)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000贝尔加德门'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 8), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★乌尔斯拉医科大学'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 7)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000乌尔斯拉医科大学'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 9), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★阿尔摩利卡村'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 8)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000阿尔摩利卡村'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 10), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★玛因兹矿山镇'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 9)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000玛因兹矿山镇'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 11), Insn('EQ'), Insn('END')]), [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('★玛因兹山道丄隧道内'))),
						Insn('MENU_CUSTOM', Insn('SELECT', ResId(1), 10)),
					]),
					(None, [
						Insn('MENU_CUSTOM', Insn('ADD', ResId(1), Translate('\u3000玛因兹山道丄隧道内'))),
					]),
				]),
				Insn('IF', [
					(Expr([Insn('VAR', 4), Insn('CONST', 12), Insn('EQ'), Insn('END')]), [
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
						Insn('0x74', Object(3), 7680),
						Insn('0x71', Object(3), b'\x01\x00', 30, 0),
						Insn('SOUND_PLAY', 464, 0, 0, 100),
						Insn('0x79', b'\x03\x00'),
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

data['code'][9] = [
	Insn('EVENT_BEGIN', 1),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0x6F', b'\x01'),
	Insn('SLEEP', 1),
	Insn('CHAR_SET_POS', Char(0), (8280, 0, -13050), 180),
	Insn('CHAR_SET_POS', Char(1), (8280, 0, -13050), 180),
	Insn('CHAR_SET_POS', Char(2), (8280, 0, -13050), 180),
	Insn('CHAR_SET_POS', Char(3), (8280, 0, -13050), 180),
	Insn('CHAR_SET_POS', Char(4), (8280, 0, -13050), 180),
	Insn('CHAR_SET_POS', Char(5), (8280, 0, -13050), 180),
	Insn('SLEEP', 1),
	Insn('CAM_OFFSET', (8280, 600, -13050), 0),
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

data['code'][10] = [
	Insn('EXPR_VAR', 4, Expr([Insn('CONST', 4), Insn('SET'), Insn('END')])),
	Insn('CALL', Function((0, 8))),
	Insn('RETURN'),
]

data['code'][11] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'我喜欢在这里\n'
		'看飞行船起飞～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'那么大的船竟然能飞上天，\n'
		'好厉害哦～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][12] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'我正要和孩子\n'
		'一起去利贝尔旅行。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'听说那边的\n'
		'饭菜非常好吃呢。\n'
		'呵呵，好期待。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][13] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'因为要从铁路换乘，\n'
		'便顺便来了克洛斯贝尔。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'这里有铁路、巴士、飞行船……\n'
		'方便的交通工具应有尽有，\n'
		'真是个便利的地方啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][14] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(2)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'我正打算去\n'
				'雷米菲利亚。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'说起来，那个国家\n'
				'好像也有警察机关……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'他们应该比克洛斯贝尔的警察\n'
				'优秀很多吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#0006F（呃啊！）{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(2)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'听说雷米菲利亚\n'
				'也有警察机关。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'他们应该比克洛斯贝尔的警察\n'
				'优秀很多吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][15] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'我刚刚在机场\n'
		'替老公送行。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'我真是的，\n'
		'这么大年纪了还挥手道别。\n'
		'呵呵，好难为情哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][16] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'我和老伴要去\n'
		'利贝尔旅行。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'听说柏斯市的超市\n'
		'也十分热闹，不逊于\n'
		'克洛斯贝尔的百货呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][17] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'老伴自从两年前\n'
		'去看过武术大会以后，\n'
		'就非常喜欢利贝尔的气氛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'我也受了他的影响，\n'
		'对利贝尔产生了兴趣，\n'
		'想去看看那是个怎样的国家呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'呵呵，我们会玩个尽兴的。\n'
		'呵呵……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][18] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'我是个贸易商。\n'
		'为了准备下个月的纪念庆典，\n'
		'正打算去进货呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'在庆典开始前都得待在外国，\n'
		'好好充实一下货物才行啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][19] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'我一直想一个人\n'
		'到外国旅游一趟呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'克洛斯贝尔这里\n'
		'有着各种传闻，\n'
		'似乎很刺激，很有趣呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][20] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'我是共和国通讯社的人。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'这次是为了报道盛况空前的\n'
		'克洛斯贝尔创立纪念庆典而来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'好，鼓足精神去拍照吧～！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][21] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'露天店整整齐齐排成一排的画面，\n'
		'读者应该会很喜欢吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'有没有哪条路的景色\n'
		'适合拍成好照片呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][22] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'为了今天，\n'
		'我存了好多零用钱呢！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'要用这些钱带女朋友\n'
		'玩遍克洛斯贝尔哦！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][23] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'嗯～我觉得，像我们这个年龄的人，\n'
		'应该没有足够的米拉\n'
		'把这里玩遍……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'呵呵，但看他这么起劲，\n'
		'我就好好期待吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][24] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'每年都是两个女生\n'
		'一起旅行……也太奇怪了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'今年这时期也不对……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][25] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'没、没有那回事～\n'
		'大家都是这样的，也有两个男人一起旅行的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'我们两个好朋友难得出来玩，\n'
		'不要说这种扫兴的话啦～{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][26] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'都到最终日了吗……\n'
		'快乐的时间\n'
		'总是一下就过去了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][27] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'不是挺好的吗，\n'
		'因此也留下了\n'
		'很多美好的回忆嘛。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][28] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'唉……\n'
		'我在米修拉姆住宿的时候\n'
		'真是倒了大霉了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'晚上竟然有军犬到处跑哦！\n'
		'但这个人竟然\n'
		'还睡得那么死……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][29] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'喂喂，别生气啦。\n'
		'只是偶尔有\n'
		'魔兽闯进来了而已吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'所以不要再耍性子，\n'
		'说什么明年不去了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][30] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'呼～去雷米菲利亚出差，\n'
		'而且还是当天往返，\n'
		'果然够辛苦啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'……嗯，老婆还在家等着，\n'
		'真想早点回去休息啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][31] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 34, Insn('TASK_GET', 2))), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'机场有飞往利贝尔和雷米菲利亚的\n'
						'国际定期船。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'今天会有货物从利贝尔那边\n'
						'送过来。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'好了～那个什么卡普亚特急便\n'
						'应该快到了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(3)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'今天会有货物从利贝尔那边\n'
						'送过来。\n'
						'我正在这里等呢。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'那个什么卡普亚特急便\n'
						'应该快到了吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('TEXT_END', Char(254)),
			Insn('RETURN'),
		]),
		(None, []),
	]),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(3)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'哦……是你们，\n'
				'又有工作了吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'……要不是我疏忽大意，\n'
				'昨天那个孩子\n'
				'也就不会遭遇危险了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'今后在工作方面，\n'
				'我决心加强责任感，\n'
				'认真处事。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(3)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'好了～今天\n'
				'预计要接收外国\n'
				'运输公司送来的货物。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'昨天被老爸\n'
				'教训了，\n'
				'一定要将功补过才行。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][32] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(779)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(872)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'啊，是你们……\n'
						'巴士怎么样了！？{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0000F嗯，果然是出现了\n'
						'引擎故障……{wait}'
						'{page}'
						'我们把魔兽赶走，\n'
						'成功确保了安全。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F至于故障方面，路过的游击士\n'
						'正在进行处理。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'哦，这样啊，\n'
						'那就好。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯嗯，交给游击士处理的话，\n'
						'就不会有问题了。{wait}'
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
						'#0006F是、是啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0108F艾丝蒂尔和约书亚\n'
						'也救了我们……\n'
						'真是无言以对呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0306F风头完全被他们\n'
						'抢走了呢……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(872)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'总之，巴士很快\n'
						'就会回来了吧？\n'
						'没出大事就好了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'也得谢谢你们呢。\n'
						'偶然路过，\n'
						'真是帮大忙了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(5)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(257), Text(
								'#0000F哈哈，谢谢……\n'
								'（下次可不能再依赖偶然，\n'
								'要更加努力地工作啊。）{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(5)),
						]),
						(None, []),
					]),
				]),
			]),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'巴士的通讯\n'
				'好像完全断绝了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'只要去郊外\n'
				'看看情况就好了。\n'
				'总之就拜托你们啦！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][33] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'#15301F我们打算在车站和机场盯梢。{wait}'
		'{page}'
		'#15301F唐古拉姆门那边就拜托你们了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][34] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1566)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('ATTR', 10), Insn('CONST', 9), Insn('EQ'), Insn('ATTR', 11), Insn('CONST', 9), Insn('EQ'), Insn('OR'), Insn('ATTR', 12), Insn('CONST', 9), Insn('EQ'), Insn('OR'), Insn('ATTR', 13), Insn('CONST', 9), Insn('EQ'), Insn('OR'), Insn('END')]), [
					Insn('CHAR_WATCH', Char(254), Char(266), 0),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1738)), Insn('NOT'), Insn('END')]), [
							Insn('TEXT_TALK', Char(254), Text(
								'#15412F呃啊……\n'
								'一课的达德利搜查官！？{wait}'
								'{page}'
								'#15402F……嘿嘿，早安～{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(266), Text(
								'#0603F都已经快中午了，说什么呢！{wait}'
								'{page}'
								'#0600F雷蒙德，探听工作\n'
								'有进展吗？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'#15411F啊，没问题啦。\n'
								'非常顺利～{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(266), Text(
								'#0603F………………………………\n'
								'（就说搜查二课靠不住……）{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('FLAG_SET', Flag(1738)),
							Insn('FLAG_SET', Flag(4)),
						]),
						(None, [
							Insn('TEXT_TALK', Char(254), Text(
								'#15400F嘿嘿，要努力探听才行呢。{wait}'
								'{page}'
								'#15404F工作，工作……{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
					Insn('CHAR_ROTATE', Char(254), 270, 0),
				]),
				(Expr([Insn('FLAG', Flag(4)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'#15402F咦～这不是支援课的各位吗？{wait}'
						'{page}'
						'#15400F莫非是来帮忙的吗？\n'
						'喏，就是机场那件事。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('IF', [
						(Expr([Insn('FLAG', Flag(1569)), Insn('NOT'), Insn('END')]), [
							Insn('EMOTE', Char(0), 0, 2000, (0, 1, 250, 2)),
							Insn('SOUND_PLAY', 29, 0, 0, 100),
							Insn('EMOTE', Char(1), 0, 2000, (0, 1, 250, 2)),
							Insn('SOUND_PLAY', 29, 0, 0, 100),
							Insn('EMOTE', Char(2), 0, 2000, (0, 1, 250, 2)),
							Insn('SOUND_PLAY', 29, 0, 0, 100),
							Insn('EMOTE', Char(3), 0, 2000, (0, 1, 250, 2)),
							Insn('SOUND_PLAY', 29, 0, 0, 100),
							Insn('SLEEP', 1000),
							Insn('TEXT_TALK', Char(258), Text(
								'#0105F机场出什么事了吗……？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'#15405F啊～你们还没听说吗～{wait}'
								'{page}'
								'#15400F算啦，也许还是不知道为好。\n'
								'不然会被一课随意使唤到死呢～{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(257), Text(
								'#0005F（？？？\n'
								'\u3000到底发生了什么事呢……）{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
						(None, [
							Insn('EMOTE', Char(0), 0, 2000, (38, 38, 250, 1)),
							Insn('EMOTE', Char(1), 0, 2000, (38, 38, 250, 1)),
							Insn('EMOTE', Char(2), 0, 2000, (38, 38, 250, 1)),
							Insn('EMOTE', Char(3), 0, 2000, (38, 38, 250, 1)),
							Insn('SLEEP', 1000),
							Insn('TEXT_TALK', Char(257), Text(
								'#0005F啊，不，倒不是这样……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(260), Text(
								'#0300F话说～情况\n'
								'怎么样了？{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'#15401F嗯～虽然不好大声宣扬，\n'
								'总之，可以说是『尚在搜索』吧～{wait}'
								'{page}'
								'#15406F二课也被编入了搜索小组，\n'
								'我和警部今天\n'
								'都被使唤得很惨呢～{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(258), Text(
								'#0108F虽然有可能是假情报，\n'
								'但也得以防万一呢……{wait}'
							)),
							Insn('TEXT_WAIT'),
							Insn('TEXT_TALK', Char(254), Text(
								'#15406F说得没错。\n'
								'真是麻烦的事件啊～{wait}'
							)),
							Insn('TEXT_WAIT'),
						]),
					]),
					Insn('FLAG_SET', Flag(4)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'#15401F今天要努力探听情报呢～{wait}'
						'{page}'
						'#15403F要在对市民隐瞒实情的同时\n'
						'进行调查工作，还真是麻烦啊～{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'#15406F本来就人手不足了……\n'
				'唉，也只好尽力而为了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][35] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'巴士还没来吗？\n'
		'我还有急事呢……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][36] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'我要去探望孙子。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'他住院很久了，\n'
		'应该很无聊吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][37] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'咦？巴士怎么还不来啊！{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'不是又出\n'
				'什么意外了吧……{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(0)), Insn('NOT'), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'咳咳……\n'
				'喂，到底要等到什么时候啊？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'应该早就过了\n'
				'发车时刻了啊！？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(0)),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'我可是感冒了呢。\n'
				'不能快点来吗！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][38] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK', Char(254), Text(
				'探病探病～㈱{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'我现在要去\n'
				'探望我男朋友！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'我们正要\n'
				'去医院看病……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'到底发生什么事了呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][39] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'感冒好像恶化了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'咳咳……\n'
		'嗯～因为最近经常\n'
		'熬夜工作吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][40] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'我今天要陪公公\n'
		'去医院。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'真是的……\n'
		'我明明和他说过，\n'
		'让他早点去医院的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][41] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'真让人头痛啊……\n'
		'探病时间是到五点半为止。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'这样下去的话，\n'
		'刚到那里就得直接回头了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][42] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_TALK2', Char(254), Translate('市民'), Text(
				'喂～巴士怎么还没个影啊～{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK2', Char(254), Translate('市民'), Text(
				'这到底怎么回事啊～！{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1569)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('ATTR', 10), Insn('CONST', 9), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'达德利搜查官，您辛苦了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'自那以来，高层也是一言不发，\n'
						'我们很难把握情况……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'机场这边的事情就交给我们吧，\n'
						'日落之前会解决好的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'……机场现在\n'
						'被我们搜查一课封锁了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'特务支援课，你们不要多管闲事，\n'
						'拖我们后腿啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'这里由我们\n'
				'搜查一课管辖。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'禁止擅自入内。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('FLAG_SET', Flag(1694)),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][43] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(1)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'真是的，\n'
						'又要去向\n'
						'市政厅投诉了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(1)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'真是的……\n'
						'今天还是别等了，直接回去吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'我们是要去\n'
				'探望一个朋友……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'到底发生什么事了呢？{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][44] = [
	Insn('TEXT_START', Char(254)),
	Insn('TEXT_TALK', Char(254), Text(
		'警察在问有没有见过\n'
		'可疑人物……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(254), Text(
		'但光说什么可疑，\n'
		'谁会知道啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][45] = [
	Insn('TEXT_START', Char(254)),
	Insn('IF', [
		(Expr([Insn('ATTR', 10), Insn('CONST', 9), Insn('EQ'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(6)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(254), Text(
						'辛苦了，\n'
						'我们这边正在进行周边排查。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'搜查二课也出动了，\n'
						'再有三个小时应该就能弄清楚了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(266), Text(
						'#0608F是吗……{wait}'
						'{page}'
						'#0600F我暂时要单独行动，\n'
						'艾玛，这边就交给你了。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'嗯，请放心吧！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(6)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(254), Text(
						'辛苦了，\n'
						'我们这边正在进行周边排查。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(254), Text(
						'搜查二课也出动了，\n'
						'再有三个小时应该就能弄清楚了。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(None, [
			Insn('TEXT_TALK', Char(254), Text(
				'特务支援课，你们\n'
				'不要太多管闲事。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'你们目前应该处于\n'
				'达德利长官的指挥之下……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(254), Text(
				'绝不允许抛下达德利长官，\n'
				'擅自行动哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('TEXT_END', Char(254)),
	Insn('RETURN'),
]

data['code'][46] = [
	Insn('EVENT_BEGIN', 1),
	Insn('SOUND_PLAY', 1094, 0, 255, 100),
	Insn('TEXT_TALK', Char(257), Text(
		'#0000F这里的话似乎可以钓到鱼。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_OFFSET', (52890, 2860, -105330), 1500),
	Insn('CAM_ROTATE', 57, 25, 0, 1500),
	Insn('0x6E', 510, 1500),
	Insn('CAM_DISTANCE', 16000, 1500),
	Insn('SLEEP', 1000),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}要钓鱼吗？{color 0}{wait}'
	)),
	Insn('MENU', 0, -1, -1, 1, Text(
		'钓鱼\n'
		'放弃\n'
	)),
	Insn('MENU_WAIT', 0),
	Insn('0x60', 0),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('0x6F', b'\x01'),
	Insn('IF', [
		(Expr([Insn('VAR', 0), Insn('CONST', 0), Insn('EQ'), Insn('END')]), [
			Insn('0xE0', b'\x02'),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(844)), Insn('END')]), [
					Insn('MINIGAME', 6, 10, [
						52120,
						900,
						-104140,
						101,
						67060,
						-5900,
						-100200,
					]),
				]),
				(None, [
					Insn('MINIGAME', 6, 11, [
						52120,
						900,
						-104140,
						101,
						67060,
						-5900,
						-100200,
					]),
					Insn('IF', [
						(Expr([Insn('ATTR', 69), Insn('CONST', 2), Insn('EQ'), Insn('END')]), [
							Insn('IF', [
								(Expr([Insn('EXEC', Insn('GET_NOTE_FISH', Insn('FISH', 23, Insn('COUNT')))), Insn('CONST', 0), Insn('GT'), Insn('FLAG', Flag(844)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
									Insn('FADE_ON', 0, Color(0x00000000), 255),
									Insn('EVENT_BEGIN', 0),
									Insn('CAM_OFFSET', (53380, 2860, -106080), 0),
									Insn('CAM_ROTATE', 58, 20, 0, 0),
									Insn('0x6E', 510, 0),
									Insn('CAM_DISTANCE', 13540, 0),
									Insn('LOAD_CHCP', 'apl/ch50161', 40),
									Insn('CHAR_SET_CHCP', Char(0), 40),
									Insn('CHAR_SET_FRAME', Char(0), 18),
									Insn('CHAR_FLAG1_SET', Char(0), 2),
									Insn('CHAR_SET_POS', Char(0), (52120, 900, -104140), 101),
									Insn('CHAR_FLAG1_SET', Char(1), 8),
									Insn('CHAR_FLAG1_SET', Char(2), 8),
									Insn('CHAR_FLAG1_SET', Char(3), 8),
									Insn('0x0D'),
									Insn('FADE_OFF', 1000, Color(0x00000000)),
									Insn('0x0D'),
									Insn('TEXT_TALK2', Char(0), Translate('罗伊德'), Text(
										'#0011F呜哇……！！？\n'
										'这、这、这是什么超级大鱼啊……！？{wait}'
										'{page}'
										'#0006F还以为鱼竿都要折断了……\n'
										'这种体积……真的能算是普通的鱼类吗？{wait}'
										'{page}'
										'#0000F哈哈，算了。\n'
										'……去跟钓公师团的分部长报告的话，\n'
										'他一定会很开心的。{wait}'
									)),
									Insn('TEXT_WAIT'),
									Insn('FADE_ON', 1000, Color(0x00000000), 255),
									Insn('0x0D'),
									Insn('CHAR_FLAG1_UNSET', Char(1), 8),
									Insn('CHAR_FLAG1_UNSET', Char(2), 8),
									Insn('CHAR_FLAG1_UNSET', Char(3), 8),
									Insn('CHAR_SET_POS', Char(1), (52120, 900, -104140), 101),
									Insn('CHAR_SET_POS', Char(2), (52120, 900, -104140), 101),
									Insn('CHAR_SET_POS', Char(3), (52120, 900, -104140), 101),
									Insn('CHAR_SET_POS', Char(4), (52120, 900, -104140), 101),
									Insn('CHAR_SET_POS', Char(5), (52120, 900, -104140), 101),
									Insn('CHAR_SET_CHCP', Char(0), 255),
									Insn('CHAR_SET_FRAME', Char(0), 0),
									Insn('CHAR_FLAG1_UNSET', Char(0), 2),
									Insn('0x49'),
									Insn('0xD5', 40),
									Insn('0x37'),
									Insn('FLAG_SET', Flag(844)),
								]),
								(None, []),
							]),
						]),
						(None, []),
					]),
				]),
			]),
		]),
		(None, []),
	]),
	Insn('0xE0', b'\x02'),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][47] = [
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1792)), Insn('END')]), [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}有一个巴士停靠站。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}现在似乎早已过了\n'
				'巴士的到达时间。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_END', Char(255)),
		]),
		(Expr([Insn('FLAG', Flag(1560)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 48, Insn('TASK_GET', 5))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 48, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 68))),
		]),
		(Expr([Insn('FLAG', Flag(777)), Insn('FLAG', Flag(778)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 48))),
		]),
		(Expr([Insn('FLAG', Flag(1347)), Insn('FLAG', Flag(1348)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CALL', Function((0, 56))),
		]),
		(Expr([Insn('FLAG', Flag(1024)), Insn('END')]), [
			Insn('CALL', Function((0, 5))),
		]),
		(None, [
			Insn('TEXT_START', Char(255)),
			Insn('TEXT_SET_NAME', Translate('')),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}有一个巴士停靠站。{color 0}{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_MESSAGE', Char(255), Text(
				'{color 5}现在早已过了\n'
				'巴士的到达时间。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_RESET', b'\x00'),
			Insn('0x5A'),
			Insn('TEXT_END', Char(255)),
		]),
	]),
	Insn('RETURN'),
]

data['code'][48] = [
	Insn('EVENT_BEGIN', 2),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('EVENT_BEGIN', 0),
	Insn('CAM_OFFSET', (-10000, 1300, -10900), 0),
	Insn('CAM_ROTATE', 45, 18, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 18000, 0),
	Insn('CHAR_SET_POS', Char(257), (-10300, 180, -11500), 180),
	Insn('CHAR_SET_POS', Char(258), (-10300, 180, -10000), 180),
	Insn('CHAR_SET_POS', Char(260), (-8500, 180, -9400), 225),
	Insn('CHAR_SET_POS', Char(259), (-9800, 180, -8300), 180),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100768V#0000F#5P下一班车的发车时间是……\n'
		'十分钟之后吗。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100769V#0100F#5P在这里稍等一下，\n'
		'很快就会来了吧。{wait}'
		'{page}'
		'#11100770V#0104F乌尔斯拉医院啊……\n'
		'好久没去那里了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(258), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100771V#0000F#12P嗯，我也是。{wait}'
		'{page}'
		'#11100772V#0006F本来打算回来之后\n'
		'马上就过去拜访的，\n'
		'可是每天都很忙呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100773V#0105F#5P哎……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100774V#0305F#5P你说要去医院，\n'
		'难道有哪里不舒服吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100775V#0004F#12P不……\n'
		'我有熟人在那里工作。{wait}'
		'{page}'
		'#11100776V#0002F人家以前很照顾我，\n'
		'所以回来后一直都想去打个招呼的。{wait}'
		'{page}'
		'#11100777V不过我们双方都很忙，\n'
		'就一直拖了下来。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100778V#0100F#5P原来如此，是这样啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100779V#0300F#5P在医院工作啊，\n'
		'是个医生吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(260), 500),
	Insn('SLEEP', 200),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100780V#0000F#6P不，是护理师。{wait}'
		'{page}'
		'#11100781V好像是年轻护理师们的领头，\n'
		'每天都忙得不可开交。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100782V#0305F#5P护理师……就是那种形象吧？{wait}'
		'{page}'
		'#11100783V穿着护士服，\n'
		'温柔地给人量体温的姐姐？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100784V#0005F#6P哎……{wait}'
		'{page}'
		'#11100785V#0000F嗯、嗯，护士服毕竟\n'
		'是工作装嘛，我想应该会穿的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100786V#0301F#5P那位姐姐，多大了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100787V#0004F#6P比我大五岁，\n'
		'所以是二十三岁吧……？{wait}'
		'{page}'
		'#11100788V#0000F就住在我家的隔壁，\n'
		'对我而言，就如同亲姐姐一样。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100789V#0301F#5P是美女？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100790V#0011F#6P嗯、嗯……\n'
		'我认为她很漂亮。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100791V#0303F#5P大我两岁的姐姐……\n'
		'而且还穿着护士服吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 300),
	Insn('0x82', 300, 0, 3000, 300),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100792V#5P#0307F#4S完全符合我的喜好！\n'
		'我热血沸腾了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(260), 0, 2000, (8, 9, 250, 2)),
	Insn('SOUND_PLAY', 27, 0, 0, 100),
	Insn('SLEEP', 1200),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100793V#5P#0309F哎呀～我可真幸福啊！{wait}'
		'{page}'
		'#11100794V能够遇到你这样的\n'
		'挚友！{wait}'
		'{page}'
		'#11100795V#0302F所以呢，就麻烦你介绍一下啦☆{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100796V#0006F#6P我说你啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100797V#0106F#5P唉……\n'
		'男人就是这样。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 3)),
	Insn('CHAR_WATCH', Char(257), Char(258), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100798V#0011F#12P喂，不要\n'
		'把我也算进去啊！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_WATCH', Char(258), Char(259), 500),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100799V#0105F#6P缇欧，你怎么了？{wait}'
		'{page}'
		'#11100800V从刚才起，好像就\n'
		'一直在想什么心事……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 300),
	]),
	Insn('EMOTE', Char(259), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100801V#0208F#5P啊……没有……\n'
		'只是我不太喜欢医院。{wait}'
		'{page}'
		'#11100802V#0206F消毒液的气味，\n'
		'还有打针什么的，有点……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100803V#0102F#6P是吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100804V#0001F#12P那个，没问题吗？{wait}'
		'{page}'
		'#11100805V不然的话，缇欧可以──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100806V#0203F#5P──没有问题。{wait}'
		'{page}'
		'#11100807V只是不太喜欢而已，\n'
		'倒也算不上讨厌。{wait}'
		'{page}'
		'#11100808V#0211F要是说我不用去也可以，\n'
		'我可是会生气的哦……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100809V#0011F#12P我、我不会说的啦。{wait}'
		'{page}'
		'#11100810V#0006F（好险好险……\n'
		'\u3000看来得当心点才行。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100811V#0204F#5P而且，我也想\n'
		'见见罗伊德前辈的\n'
		'那位熟人……{wait}'
		'{page}'
		'#11100812V#0202F就是之前和你用通讯器聊天，\n'
		'聊得很开心的那个人吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100813V#0005F#12P你、你怎么会知道……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(258), Char(257), 500),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100814V#0104F#5P呵呵，像罗伊德的\n'
		'姐姐一样的人啊。{wait}'
		'{page}'
		'#11100815V#0102F有点期待和她\n'
		'见面了呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100816V#0309F#5P噢噢，要说的话，\n'
		'见姐姐都快变成主要活动了呢！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (40, 43, 100, 3)),
	Insn('CHAR_WATCH', Char(257), Char(260), 500),
	Insn('SLEEP', 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100817V#0011F#6P还、还是要以调查为重吧！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CAM_DISTANCE', 19000, 2000),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('BGM_STOP', 4000),
	Insn('BGM_WAIT'),
	Insn('CHAR_SET_POS', Char(257), (-10000, 180, -11500), 180),
	Insn('CHAR_SET_POS', Char(258), (-10000, 180, -8900), 180),
	Insn('CHAR_SET_POS', Char(260), (-10000, 180, -10200), 180),
	Insn('CHAR_SET_POS', Char(259), (-10000, 180, -7600), 180),
	Insn('CHAR_FLAG1_UNSET', Char(44), 128),
	Insn('CHAR_SET_POS', Char(44), (-10000, 180, -6300), 180),
	Insn('CHAR_FLAG1_UNSET', Char(45), 128),
	Insn('CHAR_SET_POS', Char(45), (-10000, 180, -5000), 180),
	Insn('CHAR_FLAG1_UNSET', Char(46), 128),
	Insn('CHAR_SET_POS', Char(46), (-8700, 180, -5000), 270),
	Insn('CHAR_FLAG1_UNSET', Char(47), 128),
	Insn('CHAR_SET_POS', Char(47), (-7400, 180, -5000), 270),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (-10000, 1800, -10900), 0),
	Insn('CAM_ROTATE', 45, 18, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 18000, 0),
	Insn('BGM_PLAY', b'f\x00\x00'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (-10000, 1400, -10900), 3000),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100818V#0106F#5P……还没来呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100819V#0203F#5P都等三十分钟了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100820V#0306F#5P喂喂，罗伊德。{wait}'
		'{page}'
		'#11100821V#0301F不是说十分钟之后\n'
		'就会来的吗～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(260), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100822V#0006F#12P……你跟我说也没用啊。{wait}'
		'{page}'
		'#11100823V#0008F不过，还真奇怪啊。\n'
		'确实是有些太迟了……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_FLAG1_UNSET', Char(48), 128),
	Insn('CHAR_FLAG1_UNSET', Char(48), 4),
	Insn('CHAR_SET_POS', Char(48), (-1000, 900, 3000), 180),
	Insn('TEXT_TALK2', Char(48), Translate('青年的声音'), Text(
		'#11100824V#4P#2S啊……\n'
		'果然没来啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK_FUNC', Char(48), 3, Function((0, 49))),
	Insn('FORK_LOOP', 257, 1, [
		Insn('CHAR_WATCH', Char(257), Char(48), 500),
	]),
	Insn('FORK_LOOP', 258, 1, [
		Insn('CHAR_WATCH', Char(258), Char(48), 500),
	]),
	Insn('FORK_LOOP', 259, 1, [
		Insn('CHAR_WATCH', Char(259), Char(48), 500),
	]),
	Insn('FORK_LOOP', 260, 1, [
		Insn('CHAR_WATCH', Char(260), Char(48), 500),
	]),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (-8590, 1000, -11890), 6000),
	Insn('0x6F', b'\x01'),
	Insn('FORK_AWAIT', Char(48), 1),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(259), 1),
	Insn('FORK_QUIT', Char(260), 1),
	Insn('TEXT_TALK2', Char(48), Translate('事务人员打扮的青年'), Text(
		'#11100825V#5P伤脑筋啊……\n'
		'这可怎么办才好啊？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(48), Translate('事务人员打扮的青年'), Text(
		'#11100826V#5P即使尝试和那边进行导力通讯，\n'
		'也根本无人应答……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-8910, 1000, -11110), 0),
	Insn('CAM_ROTATE', 61, 23, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 18000, 0),
	Insn('CHAR_SET_POS', Char(257), (-9780, 180, -11560), 90),
	Insn('CHAR_SET_POS', Char(260), (-9650, 180, -10110), 135),
	Insn('CHAR_SET_POS', Char(258), (-10840, 180, -10750), 90),
	Insn('CHAR_SET_POS', Char(259), (-10640, 180, -9430), 135),
	Insn('CHAR_SET_POS', Char(44), (-10080, 180, -7470), 135),
	Insn('CHAR_SET_POS', Char(45), (-8550, 180, -5520), 180),
	Insn('CHAR_SET_POS', Char(46), (-9820, 180, -5930), 135),
	Insn('CHAR_SET_POS', Char(47), (-7450, 180, -5520), 180),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100827V#0001F#6P请问……\n'
		'出什么事了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100828V#0101F#6P巴士好像\n'
		'迟到很久了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(48), Char(257), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK2', Char(48), Translate('事务人员打扮的青年'), Text(
		'#11100829V#11P那个～好像是\n'
		'出了什么意外了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(48), Translate('事务人员打扮的青年'), Text(
		'#11100830V#11P巴士的司机使用导力通讯\n'
		'和这边联系过一次……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(48), Translate('事务人员打扮的青年'), Text(
		'#11100831V#11P但是中途突然断掉了，\n'
		'之后就毫无应答了。{wait}'
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
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(260), 0, 2000, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100832V#0005F#6P这……！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100833V#0203F#6P……感觉好像有麻烦呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100834V#0305F#1P对了……\n'
		'小哥，你是什么人？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(48), Translate('事务人员打扮的青年'), Text(
		'#11100835V#11P啊，我是克洛斯贝尔市\n'
		'交通课的人。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(48), Text(
		'#11100836V#11P负责管理在自治州\n'
		'运行的巴士……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(48), Text(
		'#11100837V#11P嗯～联系警备队又有些小题大做，\n'
		'也只能拜托协会了吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(259), 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100838V#0001F#11P（……各位，可以吗？）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100839V#0101F#6P（嗯，明白。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100840V#0203F#6P（呼……没办法呢。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100841V#0300F#1P（哎，这也是机缘巧合吧。）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(48), 500),
	]),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(48), 300),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(48), 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(48), 300),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100842V#0000F#6P请问……{wait}'
		'{page}'
		'#11100843V这个任务，能不能\n'
		'交给我们去办？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(48), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(48), Text(
		'#11100844V#11P哎？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(48), Text(
		'#11100845V#11P你们是……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100846V#0000F#6P克洛斯贝尔警察局丄\n'
		'特务支援课的人。{wait}'
		'{page}'
		'#11100847V我们正准备前往医科大学\n'
		'执行调查任务。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(48), Text(
		'#11100848V#11P哎，你们是警察局的人？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(48), Text(
		'#11100849V#11P对了……\n'
		'我在杂志上看到过。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(48), Text(
		'#11100850V#11P说警察也像协会一样，\n'
		'开始为市民服务了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100851V#0006F#6P……那个，确切地说，\n'
		'其实也不太一样。{wait}'
		'{page}'
		'#11100852V#0000F不过，去看看巴士的情况\n'
		'应该还是没问题的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(48), Text(
		'#11100853V#11P是吗……\n'
		'那就拜托你们了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(48), Text(
		'#11100854V#11P要不，我再去委托\n'
		'游击士协助你们吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100855V#0012F#6P不、不用了。\n'
		'我想应该没问题的。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(259), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#11100856V#0000F#11P──各位，走吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#11100857V#0100F#6P嗯……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#11100858V#0302F#1P噢！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#11100859V#0202F#6P……明白。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('CAM_DISTANCE', 18250, 1000),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_FLAG1_SET', Char(48), 128),
	Insn('CHAR_FLAG2_SET', Char(48), 32768),
	Insn('CHAR_FLAG1_SET', Char(44), 128),
	Insn('CHAR_FLAG2_SET', Char(44), 32768),
	Insn('CHAR_FLAG1_SET', Char(45), 128),
	Insn('CHAR_FLAG2_SET', Char(45), 32768),
	Insn('CHAR_FLAG1_SET', Char(46), 128),
	Insn('CHAR_FLAG2_SET', Char(46), 32768),
	Insn('CHAR_FLAG1_SET', Char(47), 128),
	Insn('CHAR_FLAG2_SET', Char(47), 32768),
	Insn('CHAR_SET_POS', Char(0), (-5110, 0, -13100), 180),
	Insn('FLAG_SET', Flag(778)),
	Insn('QUEST', 63, Insn('TASK_SET', 6)),
	Insn('0x1B', 2, Function((255, 255)), 255),
	Insn('CHAR_FLAG1_UNSET', Char(8), 128),
	Insn('CHAR_FLAG1_UNSET', Char(9), 128),
	Insn('CHAR_FLAG1_UNSET', Char(10), 128),
	Insn('CHAR_FLAG1_UNSET', Char(11), 128),
	Insn('CHAR_FLAG1_UNSET', Char(16), 128),
	Insn('CHAR_FLAG1_UNSET', Char(39), 128),
	Insn('CHAR_SET_POS', Char(8), (-9780, 180, -10890), 180),
	Insn('CHAR_SET_POS', Char(9), (-9560, 180, -8470), 180),
	Insn('CHAR_SET_POS', Char(10), (-9480, 180, -7040), 180),
	Insn('CHAR_SET_POS', Char(11), (-9410, 180, -5860), 180),
	Insn('CHAR_SET_POS', Char(16), (-9810, 180, -9920), 180),
	Insn('SLEEP', 500),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][49] = [
	Insn('FORK', 48, 1, [
		Insn('0x95', Char(254), (-1000, 0, -7000), 3000, 0),
	]),
	Insn('FORK_AWAIT', Char(48), 1),
	Insn('FORK', 48, 1, [
		Insn('0x95', Char(254), (-7000, 0, -13000), 3000, 0),
	]),
	Insn('FORK_AWAIT', Char(48), 1),
	Insn('CHAR_ROTATE', Char(48), 180, 500),
	Insn('RETURN'),
]

data['code'][50] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('0xE0', b'\x01'),
	Insn('LOAD_CHCP', 'chr/ch02600', 40),
	Insn('LOAD_CHCP', 'chr/ch02651', 41),
	Insn('LOAD_CHCP', 'chr/ch02602', 42),
	Insn('CHAR_SET_POS', Char(0), (0, 0, -80000), 0),
	Insn('CHAR_SET_POS', Char(1), (0, 0, -80000), 0),
	Insn('CHAR_SET_POS', Char(2), (0, 0, -80000), 0),
	Insn('CHAR_SET_POS', Char(3), (0, 0, -80000), 0),
	Insn('CHAR_SET_COLOR', Char(0), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(1), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(2), Color(0x00FFFFFF), 0),
	Insn('CHAR_SET_COLOR', Char(3), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(49), 128),
	Insn('CHAR_FLAG1_SET', Char(49), 32768),
	Insn('CHAR_SET_CHCP', Char(49), 41),
	Insn('CHAR_SET_FRAME', Char(49), 0),
	Insn('CHAR_SET_POS', Char(43), (1850, 0, -99380), 0),
	Insn('CHAR_SET_COLOR', Char(49), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(43), 128),
	Insn('CHAR_FLAG1_SET', Char(43), 32768),
	Insn('OBJ_FLAG_SET', Object(1), 4096),
	Insn('OBJ_FLAG_UNSET', Object(1), 4),
	Insn('0x78', b'\x01', Char(43)),
	Insn('OBJ_SET_FRAME', Object(1), 'light', Insn('0', 1)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(49), (-15190, 0, -65690), 90),
	Insn('0xD3', Char(43), 0, 0, 0, 0),
	Insn('0x74', Object(1), 7680),
	Insn('0x71', Object(1), b'y\x00', 180, 32),
	Insn('0x7D', b'\xff\xbe\xb4\x00\x00\x00\x00\x00'),
	Insn('0x11', b'\xd2\xae\x9b', 5, 400, 0),
	Insn('OBJ_SET_FRAME', Object(255), 'sky', Insn('2', 'red')),
	Insn('OBJ_SET_FRAME', Object(255), 'water00', Insn('2', 'red')),
	Insn('OBJ_SET_FRAME', Object(255), 'water01', Insn('2', 'red')),
	Insn('IMG_LOAD', ResId(0), 0, 8, b'\xe0\x01\x08\x01\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\xe0\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis163.itp'),
	Insn('IMG_LOAD', ResId(1), 234, 0, b'\xea\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x02\x00\x02\xff\xff\xff\x00\x01', 'bu01200.itp'),
	Insn('FORK_FUNC', Char(51), 1, Function((0, 53))),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_OFFSET', (4940, 600, -80110), 0),
	Insn('CAM_ROTATE', 46, 11, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 34420, 0),
	Insn('CAM_OFFSET', (3390, 600, -61360), 8000),
	Insn('FORK', 43, 1, [
		Insn('0x95', Char(254), (-320, 0, -25730), 6000, 0),
	]),
	Insn('0x6F', b'\x01'),
	Insn('0x0D'),
	Insn('SLEEP', 2000),
	Insn('BGM_STOP', 6000),
	Insn('FORK_AWAIT', Char(43), 1),
	Insn('EXPR_CHAR_ATTR', Char(49), 45, Expr([Insn('CONST', 1100), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(49), 46, Expr([Insn('CONST', 1100), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(49), 47, Expr([Insn('CONST', 1100), Insn('SET'), Insn('END')])),
	Insn('CHAR_SET_COLOR', Char(49), Color(0xFFFFFFFF), 0),
	Insn('CHAR_SET_CHCP', Char(49), 41),
	Insn('CHAR_SET_FRAME', Char(49), 0),
	Insn('EXPR_CHAR_ATTR', Char(49), 7, Expr([Insn('CONST', 1500), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_UNSET', Char(49), 1),
	Insn('FORK', 49, 1, [
		Insn('0x9D', Char(254), -7800, 0, -64700, 3000, 2500),
	]),
	Insn('FORK_AWAIT', Char(49), 1),
	Insn('CHAR_FLAG1_SET', Char(49), 1),
	Insn('SOUND_PLAY', 46, 0, 0, 100),
	Insn('CHAR_SET_FRAME', Char(49), 1),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(49), 2),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_FRAME', Char(49), 3),
	Insn('SLEEP', 50),
	Insn('CHAR_FLAG1_SET', Char(49), 32),
	Insn('FORK_FUNC', Char(49), 3, Function((0, 51))),
	Insn('FORK_FUNC', Char(51), 1, Function((0, 54))),
	Insn('FORK', 49, 1, [
		Insn('0x96', Char(254), (950, 0, -63790), 6000, 0),
	]),
	Insn('SLEEP', 1000),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (2880, 600, -60120), 0),
	Insn('CAM_ROTATE', 41, 17, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 24800, 0),
	Insn('0x0D'),
	Insn('FORK_AWAIT', Char(49), 1),
	Insn('FORK_QUIT', Char(49), 3),
	Insn('FORK_QUIT', Char(51), 1),
	Insn('CHAR_FLAG1_UNSET', Char(49), 32),
	Insn('FORK', 49, 1, [
		Insn('CHAR_ROTATE', Char(254), 0, 500),
	]),
	Insn('FORK_AWAIT', Char(49), 1),
	Insn('CHAR_SET_CHCP', Char(49), 42),
	Insn('CHAR_SET_FRAME', Char(49), 0),
	Insn('EXPR_CHAR_ATTR', Char(49), 7, Expr([Insn('CONST', 1500), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(49), 45, Expr([Insn('CONST', 1100), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(49), 46, Expr([Insn('CONST', 1100), Insn('SET'), Insn('END')])),
	Insn('EXPR_CHAR_ATTR', Char(49), 47, Expr([Insn('CONST', 1100), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(49), 32),
	Insn('FORK_FUNC', Char(49), 3, Function((0, 52))),
	Insn('SLEEP', 800),
	Insn('SOUND_PLAY', 2053, 0, 255, 80),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(1), 0), Color(0xFFFFD8F0), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 0))),
	Insn('TEXT_SET_POS', -1, 280, 35, 3),
	Insn('SLEEP', 800),
	Insn('TEXT_SET_NAME', Translate('白狼')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'#11101670V…………………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(1), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xC9', (ResId(1), 0), Color(0x00000000), 0, 500),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 3))),
	Insn('IMG_0xCA', Insn('0', (ResId(1), 0))),
	Insn('SLEEP', 300),
	Insn('FORK_QUIT', Char(49), 3),
	Insn('CHAR_FLAG1_UNSET', Char(49), 32),
	Insn('CHAR_ROTATE', Char(49), 270, 500),
	Insn('CHAR_SET_CHCP', Char(49), 41),
	Insn('CHAR_SET_FRAME', Char(49), 0),
	Insn('EXPR_CHAR_ATTR', Char(49), 7, Expr([Insn('CONST', 1500), Insn('SET'), Insn('END')])),
	Insn('CHAR_FLAG1_SET', Char(49), 32),
	Insn('FORK_FUNC', Char(49), 3, Function((0, 51))),
	Insn('FORK_FUNC', Char(51), 1, Function((0, 55))),
	Insn('CAM_DISTANCE', 30800, 3000),
	Insn('CAM_OFFSET', (1020, 600, -61950), 3000),
	Insn('FORK', 49, 1, [
		Insn('0x96', Char(254), (-14250, 0, -71020), 7000, 0),
	]),
	Insn('SLEEP', 2500),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('FORK_AWAIT', Char(49), 1),
	Insn('FORK_QUIT', Char(49), 3),
	Insn('FORK_QUIT', Char(51), 1),
	Insn('CHAR_FLAG1_UNSET', Char(49), 32),
	Insn('0x0D'),
	Insn('BGM_WAIT'),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
	Insn('FORK_QUIT', Char(51), 1),
	Insn('SLEEP', 2000),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}当天晚上……\n'
		'回到支援课的罗伊德等人\n'
		'开始整理当天的调查报告。{wait}'
		'{page}'
		'在将最新查明的事实与证言，\n'
		'以及更多疑点和目前的推测等情报\n'
		'进行简单明了的总结时……{wait}'
		'{page}'
		'不知不觉间已经过了凌晨零点，\n'
		'身心疲惫的罗伊德等人\n'
		'便回到各自的房间休息去了。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 13, 0, 0, 100),
	Insn('SLEEP', 4000),
	Insn('MINIGAME', 24, 0, [
		0,
		0,
		0,
		0,
		0,
		0,
		0,
	]),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('SLEEP', 2000),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('FLAG_SET', Flag(800)),
	Insn('FLAG_SET', Flag(740)),
	Insn('NEW_SCENE', 'c0110', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][51] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_ANIMATION', Char(254), 1500, [
			0,
			1,
			2,
			3,
			4,
		]),
	]),
	Insn('RETURN'),
]

data['code'][52] = [
	Insn('WHILE', [Insn('CONST', 1), Insn('END')], [
		Insn('CHAR_ANIMATION', Char(254), 1500, [
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

data['code'][53] = [
	Insn('SOUND_PLAY', 465, 0, 0, 100),
	Insn('SLEEP', 4500),
	Insn('SOUND_PLAY', 471, 0, 0, 100),
	Insn('RETURN'),
]

data['code'][54] = [
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 832, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 832, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 832, 0, 0, 100),
	Insn('RETURN'),
]

data['code'][55] = [
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 832, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 832, 0, 0, 85),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 832, 0, 0, 70),
	Insn('SLEEP', 500),
	Insn('SOUND_PLAY', 832, 0, 0, 55),
	Insn('RETURN'),
]

data['code'][56] = [
	Insn('EVENT_BEGIN', 0),
	Insn('SOUND_LOAD', 468),
	Insn('CROSSFADE', 1000),
	Insn('CAM_OFFSET', (-9140, 780, -11210), 0),
	Insn('CAM_ROTATE', 55, 18, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 25710, 0),
	Insn('CHAR_SET_POS', Char(257), (-10500, 180, -11600), 180),
	Insn('CHAR_SET_POS', Char(339), (-9630, 180, -10060), 180),
	Insn('CHAR_SET_POS', Char(239), (-9220, 180, -11310), 225),
	Insn('CHAR_FLAG1_UNSET', Char(43), 128),
	Insn('OBJ_FLAG_SET', Object(1), 2),
	Insn('OBJ_FLAG_SET', Object(1), 4096),
	Insn('0x78', b'\x01', Char(43)),
	Insn('OBJ_SET_FRAME', Object(1), 'light', Insn('0', 1)),
	Insn('0x49'),
	Insn('CHAR_SET_POS', Char(43), (0, 0, -40000), 0),
	Insn('0xD3', Char(43), 0, 0, 0, 0),
	Insn('0x74', Object(1), 7680),
	Insn('0x71', Object(1), b'y\x00', 180, 32),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600652V#0000F#5P下一班车的发车时间是……\n'
		'啊，好像就快来了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600653V#0109F#11P呵呵……\n'
				'时间赶得正好呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600654V#0204F#11P时机正好。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600655V#0304F#11P时候赶得刚好啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('EMOTE', Char(339), 0, 1700, (0, 1, 250, 2)),
	Insn('SOUND_PLAY', 29, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600656V#1110F#5P什么来了～？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(339), 500),
	Insn('CHAR_WATCH', Char(239), Char(339), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600657V#0004F#12P嗯，就是琪雅\n'
		'想坐的东西。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600658V#1105F#5P哎……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 467, 0, 0, 100),
	Insn('FORK_FUNC', Char(51), 1, Function((0, 60))),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(239), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(339), 0, 1700, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 257, 1, [
		Insn('CHAR_ROTATE', Char(254), 180, 500),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_ROTATE', Char(239), 180, 500),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600659V#0102F已经来了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600660V#0202F已经来了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600661V#0302F已经来了啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('FORK_QUIT', Char(51), 1),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (2080, 600, -29850), 0),
	Insn('CAM_ROTATE', 50, 18, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 23500, 0),
	Insn('OBJ_FLAG_UNSET', Object(1), 4),
	Insn('FORK', 43, 1, [
		Insn('0x98', Char(254), (0, 0, 30000), 6000, 0),
	]),
	Insn('SOUND_PLAY', 466, 0, 0, 100),
	Insn('FORK_FUNC', Char(51), 1, Function((0, 61))),
	Insn('SLEEP', 3000),
	Insn('FORK_QUIT', Char(51), 1),
	Insn('CROSSFADE', 500),
	Insn('CAM_OFFSET', (-8650, 780, -10720), 0),
	Insn('CAM_ROTATE', 55, 18, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 18760, 0),
	Insn('0x4B', Char(12), -1),
	Insn('0x4B', Char(13), -1),
	Insn('CHAR_SET_POS', Char(257), (-11000, 180, -11600), 90),
	Insn('CHAR_SET_POS', Char(339), (-11000, 180, -10400), 90),
	Insn('CHAR_SET_POS', Char(239), (-11000, 180, -9200), 90),
	Insn('CHAR_SET_POS', Char(12), (-11000, 180, -8000), 180),
	Insn('CHAR_SET_POS', Char(13), (-11000, 180, -6800), 180),
	Insn('CHAR_SET_POS', Char(43), (-5300, 0, -21000), 0),
	Insn('FORK', 43, 1, [
		Insn('0x96', Char(254), (-5300, 0, -13000), 4000, 0),
	]),
	Insn('SLEEP', 1000),
	Insn('EMOTE', Char(339), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('FORK_AWAIT', Char(43), 1),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600662V#1107F#6P哇啊啊啊啊！？\n'
		'好大的车哦！{wait}'
	)),
	Insn('0x71', Object(1), b'[\x00', 120, 0),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600663V#0002F#6P琪雅，这就叫\n'
		'巴士哦。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x71', Object(1), b'\x01\x00', 65566, 0),
	Insn('SOUND_PLAY', 464, 0, 0, 100),
	Insn('0x79', b'\x01\x00'),
	Insn('FORK_FUNC', Char(12), 3, Function((0, 57))),
	Insn('SLEEP', 3000),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600664V#1105F#6P哇哇……\n'
		'出来了好多人哦！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600665V#0004F#6P嗯，是去医院的人\n'
		'回到市里来了。{wait}'
		'{page}'
		'#13600666V#0000F我们也要乘坐\n'
		'这个去医院呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(339), 0, 1700, (2, 7, 80, 1)),
	Insn('SOUND_PLAY', 28, 0, 0, 100),
	Insn('SLEEP', 1000),
	Insn('CHAR_WATCH', Char(339), Char(257), 500),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600667V#1101F#5P琪雅要坐这个吗～！？{wait}'
		'{page}'
		'#13600668V罗伊德，你们也一起！？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(339), 500),
	Insn('CHAR_WATCH', Char(239), Char(339), 500),
	Insn('TEXT_TALK', Char(257), Text(
		'#13600669V#0002F#12P嗯，当然。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(339), Text(
		'#13600670V#1109F#5P嘿嘿……{wait}'
		'{page}'
		'#13600671V#1110F那个那个，赶快坐上去吧！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1356)), Insn('END')]), [
			Insn('TEXT_TALK', Char(258), Text(
				'#13600672V#0109F#5P呵呵……\n'
				'小心脚下哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1357)), Insn('END')]), [
			Insn('TEXT_TALK', Char(259), Text(
				'#13600673V#0204F#5P呵……\n'
				'请注意脚下。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1358)), Insn('END')]), [
			Insn('TEXT_TALK', Char(260), Text(
				'#13600674V#0309F#5P哈哈……\n'
				'当心脚下啦。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FORK_QUIT', Char(12), 3),
	Insn('CALL', Function((0, 58))),
	Insn('CHAR_SET_POS', Char(12), (-8900, 180, -4000), 90),
	Insn('CHAR_SET_POS', Char(13), (-7700, 180, -4000), 270),
	Insn('0x4C', Char(12), -1),
	Insn('0x4C', Char(13), -1),
	Insn('EXPR_ATTR', 76, Expr([Insn('CONST', 105), Insn('SET'), Insn('END')])),
	Insn('SOUND_STOP', 468),
	Insn('FLAG_SET', Flag(737)),
	Insn('NEW_SCENE', 'r1530', b'\x00\x00\x00\x07'),
	Insn('RETURN'),
]

data['code'][57] = [
	Insn('FORK_FUNC', Char(24), 3, Function((0, 59))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(23), 3, Function((0, 59))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(30), 3, Function((0, 59))),
	Insn('SLEEP', 1000),
	Insn('FORK_FUNC', Char(17), 3, Function((0, 59))),
	Insn('SLEEP', 1000),
	Insn('FORK_AWAIT', Char(24), 3),
	Insn('FORK_AWAIT', Char(23), 3),
	Insn('FORK_AWAIT', Char(30), 3),
	Insn('FORK_AWAIT', Char(17), 3),
	Insn('RETURN'),
]

data['code'][58] = [
	Insn('FORK_QUIT', Char(24), 3),
	Insn('FORK_QUIT', Char(23), 3),
	Insn('FORK_QUIT', Char(30), 3),
	Insn('FORK_QUIT', Char(17), 3),
	Insn('RETURN'),
]

data['code'][59] = [
	Insn('CHAR_SET_POS', Char(254), (-6080, 600, -13010), 270),
	Insn('CHAR_SET_COLOR', Char(254), Color(0x00FFFFFF), 0),
	Insn('CHAR_FLAG1_UNSET', Char(254), 128),
	Insn('CHAR_FLAG2_UNSET', Char(254), 32768),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-8730, 180, -12970), 2000, 0),
	]),
	Insn('FORK', 254, 2, [
		Insn('CHAR_SET_COLOR', Char(254), Color(0xFFFFFFFF), 500),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-8850, 180, -7610), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-1260, 0, -7620), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK', 254, 1, [
		Insn('0x95', Char(254), (-50, 900, 3490), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(254), 1),
	Insn('FORK_AWAIT', Char(254), 2),
	Insn('RETURN'),
]

data['code'][60] = [
	Insn('SOUND_PLAY', 468, 0, 2, 0),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 10),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 20),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 30),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 40),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 50),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 60),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 70),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 80),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 90),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 100),
	Insn('RETURN'),
]

data['code'][61] = [
	Insn('SOUND_LOOP', 468, 90),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 80),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 70),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 60),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 50),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 40),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 30),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 20),
	Insn('SLEEP', 100),
	Insn('SOUND_LOOP', 468, 10),
	Insn('SLEEP', 100),
	Insn('SOUND_STOP', 468),
	Insn('RETURN'),
]

data['code'][62] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0x00000000), 255),
	Insn('LOAD_CHCP', 'apl/ch50011', 40),
	Insn('LOAD_CHCP', 'apl/ch50111', 41),
	Insn('SOUND_LOAD', 806),
	Insn('SOUND_LOAD', 891),
	Insn('CAM_OFFSET', (-5810, 1000, -9380), 0),
	Insn('CAM_ROTATE', 45, 19, 0, 0),
	Insn('0x6E', 400, 0),
	Insn('CAM_DISTANCE', 24150, 0),
	Insn('CHAR_SET_POS', Char(257), (-5570, 0, -9390), 270),
	Insn('CHAR_SET_POS', Char(258), (-4760, 0, -10050), 270),
	Insn('CHAR_SET_POS', Char(259), (-3220, 0, -9280), 270),
	Insn('CHAR_SET_POS', Char(260), (-3850, 0, -8250), 270),
	Insn('IMG_LOAD', ResId(0), 180, 0, b'\xb4\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\xff\xff\xff\x00\x01', 'c_vis007.itp'),
	Insn('FADE_OFF', 1000, Color(0x00000000)),
	Insn('CAM_DISTANCE', 23150, 2500),
	Insn('0x6F', b'y'),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(257), Text(
		'#15100231V#0005F#11P咦……\n'
		'排了好长的队啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#15100232V#0100F#11P以这个时间来说，真是少见呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 1500),
	Insn('EMOTE_STOP', Char(259)),
	Insn('TEXT_TALK', Char(259), Text(
		'#15100233V#0203F#11P……很奇怪呢。{wait}'
		'{page}'
		'#15100234V#0200F五分钟之前应该\n'
		'刚走了一班车才对……{wait}'
	)),
	Insn('TEXT_WAIT'),
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
		'#15100235V#0001F#6P是这样吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#15100236V#0301F#5P唔……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(260), 270, 500),
	Insn('CAM_OFFSET', (-7200, 1000, -7930), 2500),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (-6860, 0, -8060), 2000, 0),
	]),
	Insn('SLEEP', 300),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(14), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(14), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(14), 500),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('CHAR_WATCH', Char(260), Char(14), 500),
	Insn('0x6F', b'y'),
	Insn('TEXT_TALK', Char(260), Text(
		'#15100237V#0300F#11P哟，这位老兄。{wait}'
		'{page}'
		'#15100238V莫非巴士\n'
		'迟到了吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('0x4B', Char(14), -1),
	Insn('EMOTE', Char(14), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('CHAR_WATCH', Char(14), Char(260), 500),
	Insn('TEXT_TALK2', Char(14), Translate('青年'), Text(
		'#15100239V#5P嗯，好像是啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(14), Translate('青年'), Text(
		'#15100240V#5P我已经在这里等了\n'
		'足足二十分钟了，\n'
		'但一直没车来呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK2', Char(14), Translate('青年'), Text(
		'#15100241V#5P伤脑筋啊……\n'
		'探病时间都要过了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#15100242V#0301F#11P是吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(14), 180, 500),
	Insn('0x4C', Char(14), -1),
	Insn('CHAR_ROTATE', Char(260), 90, 500),
	Insn('CAM_OFFSET', (-3580, 1000, -8640), 3000),
	Insn('FORK_LOOP', 257, 1, [
		Insn('CHAR_WATCH', Char(257), Char(260), 500),
	]),
	Insn('FORK_LOOP', 258, 1, [
		Insn('CHAR_WATCH', Char(258), Char(260), 500),
	]),
	Insn('FORK_LOOP', 259, 1, [
		Insn('CHAR_WATCH', Char(259), Char(260), 500),
	]),
	Insn('FORK', 260, 1, [
		Insn('0x95', Char(254), (-3850, 0, -8250), 2000, 0),
	]),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('CHAR_WATCH', Char(260), Char(258), 500),
	Insn('FORK_QUIT', Char(257), 1),
	Insn('FORK_QUIT', Char(258), 1),
	Insn('FORK_QUIT', Char(259), 1),
	Insn('0x6F', b'\x01'),
	Insn('TEXT_TALK', Char(260), Text(
		'#15100243V#0306F#5P看来果然迟到了啊。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#15100244V#0108F#12P难不成……\n'
		'又是引擎故障吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#15100245V#0206F#11P有这个可能呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_PLAY', 806, 0, 2, 100),
	Insn('SLEEP', 500),
	Insn('EMOTE', Char(257), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(258), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(259), 0, 2000, (38, 38, 250, 1)),
	Insn('EMOTE', Char(260), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 258, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('SLEEP', 50),
	Insn('FORK', 260, 1, [
		Insn('CHAR_WATCH', Char(254), Char(257), 500),
	]),
	Insn('FORK_AWAIT', Char(258), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('FORK_AWAIT', Char(260), 1),
	Insn('CHAR_ROTATE', Char(257), 90, 500),
	Insn('SLEEP', 150),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_SET', Char(257), 32),
	Insn('CHAR_FLAG1_SET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 40),
	Insn('CHAR_SET_FRAME', Char(257), 4),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('SLEEP', 500),
	Insn('SOUND_STOP', 806),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('CHAR_SET_FRAME', Char(257), 5),
	Insn('SLEEP', 300),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0xFFFFFFFF), 500, 0),
	Insn('FADE_ON', 500, Color(0x00000000), 100),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'#15100246V#0001F您好，我是特务支援课的\n'
		'罗伊德丄班宁斯。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('男人的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#15100247V我是达德利，\n'
		'你们那边的情况如何了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#15100248V#0005F啊，您辛苦了。{wait}'
		'{page}'
		'#15100249V#0000F我们已经顺利取得\n'
		'游击士协会的协助了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}将克洛斯贝尔分部的全体游击士\n'
		'接受委托，对黑手党及失踪者\n'
		'进行搜索的情况做了说明。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('达德利的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#15100250V哼……\n'
		'欠了马克莱因一个人情啊。{wait}'
		'{page}'
		'#15100251V也罢，凭他们那些人的实力，\n'
		'应该能取得些什么成果吧。{wait}'
		'{page}'
		'#15100252V──至于我们这边，\n'
		'上层那些人总算开始对\n'
		'黑手党成员的消失感到不安了。{wait}'
		'{page}'
		'#15100253V但是，在正式出动之前，\n'
		'可能还要花点时间。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#15100254V#0003F明白了。{wait}'
		'{page}'
		'#15100255V#0001F对了──\n'
		'我们现在正在机场附近，\n'
		'炸弹恐吓事件怎么样了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('达德利的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#15100256V哼，那个很可能只是\n'
		'彻头彻尾的假情报。{wait}'
		'{page}'
		'#15100257V已经用最新的导力探测器\n'
		'在机场内整个查询一遍，\n'
		'但是什么也没找到。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#15100258V#0013F这件事果然和黑手党的动向\n'
		'存在什么关系吧……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('达德利的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#15100259V我们现在也正朝这个方向调查。{wait}'
		'{page}'
		'#15100260V──慢着，\n'
		'你们说在机场附近……{wait}'
		'{page}'
		'#15100261V难不成，又打算\n'
		'插手那边的事？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#15100262V#0000F不，其实我们\n'
		'正准备去乌尔斯拉医院。{wait}'
		'{page}'
		'#15100263V关于药物成分调查的联系迟迟未到，\n'
		'所以我们打算直接过去问问。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('达德利的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#15100264V怎么，还没问来吗？{wait}'
		'{page}'
		'#15100265V真是的，所以说新手就是新手。\n'
		'像这种重要的联系，应该事先定好\n'
		'确切的时间，迅速了结……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#15100266V#0006F对、对不起。\n'
		'（确实太过马虎了吗……）{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('达德利的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#15100267V只要能检明药物的成分，\n'
		'我这边也就更容易说动上层。{wait}'
		'{page}'
		'#15100268V现在一切都寄希望于\n'
		'那名医生的努力……{wait}'
		'{page}'
		'#15100269V……说起来，\n'
		'那名医生叫什么名字？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#15100270V#0005F啊，我没说过吗？{wait}'
		'{page}'
		'#15100271V#0000F他叫做约亚西姆丄琼塔，\n'
		'是负责神经科与药物学的副教授。{wait}'
		'{page}'
		'#15100272V虽然才三十多岁，\n'
		'但据说能力很强，评价很高。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('达德利的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#15100273V唔，那样的话，\n'
		'可能还有点希望……{wait}'
		'{page}'
		'#15100274V──嗯？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#15100275V#0001F嗯？怎么了？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('达德利的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#15100276V等一下……\n'
		'你说约亚西姆丄琼塔？{wait}'
		'{page}'
		'#15100277V是个戴着眼镜，\n'
		'感觉有点超然的男子吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#15100278V#0005F嗯，没错……\n'
		'您见过他吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('BGM_STOP', 5000),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('达德利的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#15100279V#40W…………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#15100280V#0001F那个，达德利警官……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('达德利的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#15100281V……大概是在\n'
		'两个多月之前见过。{wait}'
		'{page}'
		'#15100282V在审问于彩虹剧团的预演中\n'
		'企图暗杀市长的犯人──{wait}'
		'{page}'
		'#15100283V原秘书阿奈斯特\n'
		'的时候。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#15100284V#0005F哎？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('BGM_WAIT'),
	Insn('SLEEP', 10),
	Insn('BGM_PLAY', b'\xcb\x00\x00'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('达德利的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#15100285V赛尔盖长官可能告诉过你们，\n'
		'阿奈斯特精神完全错乱了。{wait}'
		'{page}'
		'#15100286V无奈之下，就把他以前\n'
		'经常找的心理咨询师\n'
		'从乌尔斯拉医院叫来了。{wait}'
		'{page}'
		'#15100287V这样一来，总算才能\n'
		'顺利进行审问……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#15100288V#0011F请、请等一下。{wait}'
		'{page}'
		'#15100289V莫非……\n'
		'约亚西姆医生就是阿奈斯特的……？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('达德利的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#15100290V嗯，就是他的主治医生。{wait}'
		'{page}'
		'#15100291V当时觉得不愧是乌尔斯拉医院的\n'
		'医生，还挺佩服的……{wait}'
		'{page}'
		'#15100292V………………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#15100293V#0003F……………………………………{wait}'
		'{page}'
		'#15100294V#0013F……明白了，\n'
		'我会不动声色地试探他一下。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', 170, 50, -1, -1),
	Insn('TEXT_SET_NAME', Translate('达德利的声音')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}#15100295V嗯，你去试试吧。{wait}'
		'{page}'
		'#15100296V总之，尽量抓紧时间。\n'
		'──我会再联系你。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('SOUND_PLAY', 825, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('TEXT_SET_POS', 90, 130, -1, -1),
	Insn('TEXT_MESSAGE', Char(257), Text(
		'{color 0}#15100297V#0008F#30W……………………………………{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('IMG_0xC9', (ResId(0), 3), Color(0x00FFFFFF), 500, 0),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('IMG_0xCA', Insn('0', (ResId(0), 3))),
	Insn('CHAR_SET_FRAME', Char(257), 4),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(258), Text(
		'#15100298V#0105F#12P怎、怎么了？\n'
		'好像说了什么奇怪的事……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#15100299V#0205F#11P那个秘书与约亚西姆医生\n'
		'之间有什么关系吗？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SLEEP', 150),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_UNSET', Char(257), 32),
	Insn('CHAR_FLAG1_UNSET', Char(257), 2),
	Insn('CHAR_SET_CHCP', Char(257), 255),
	Insn('CHAR_SET_FRAME', Char(257), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(257), Text(
		'#15100300V#0003F#6P嗯……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}将达德利透露的情报转告给了艾莉等人。{color 0}{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(258), Text(
		'#15100301V#0101F#12P这、这……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#15100302V#0303F#5P感觉事情没有那么单纯啊……{wait}'
		'{page}'
		'#15100303V#0301F现在回想起来，\n'
		'那个混蛋秘书当时的态度\n'
		'与惊人蛮力，不管怎么想都……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#15100304V#0206F#11P好像与矿工冈兹先生的情况\n'
		'别无二致呢。{wait}'
		'{page}'
		'#15100305V#0208F而且，他的主治医生\n'
		'居然就是约亚西姆医生……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('TEXT_TALK', Char(258), Text(
		'#15100306V#0101F#12P我、我现在就向医院的\n'
		'服务台确认一下。{wait}'
		'{page}'
		'#15100307V问问约亚西姆医生\n'
		'在那之后有没有外出──{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FORK', 257, 1, [
		Insn('CHAR_WATCH', Char(254), Char(258), 300),
	]),
	Insn('FORK', 259, 1, [
		Insn('CHAR_WATCH', Char(254), Char(258), 500),
	]),
	Insn('FORK_AWAIT', Char(257), 1),
	Insn('FORK_AWAIT', Char(259), 1),
	Insn('TEXT_TALK', Char(257), Text(
		'#15100308V#0001F#6P嗯，拜托了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_ROTATE', Char(258), 180, 400),
	Insn('SLEEP', 300),
	Insn('CROSSFADE', 250),
	Insn('CHAR_FLAG1_SET', Char(258), 2),
	Insn('CHAR_FLAG1_SET', Char(258), 16),
	Insn('CHAR_SET_CHCP', Char(258), 41),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x0D'),
	Insn('SLEEP', 200),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('SLEEP', 800),
	Insn('SOUND_PLAY', 891, 0, 2, 100),
	Insn('SLEEP', 2500),
	Insn('TEXT_TALK', Char(258), Text(
		'#15100309V#0103F#5P…………………………………{wait}'
		'{page}'
		'#15100310V#0108F……不行，没人接。{wait}'
		'{page}'
		'#15100311V好像也不在\n'
		'忙线中……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('SOUND_STOP', 891),
	Insn('SOUND_PLAY', 807, 0, 0, 100),
	Insn('SLEEP', 150),
	Insn('CROSSFADE', 250),
	Insn('CHAR_SET_CHCP', Char(258), 255),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('CHAR_FLAG1_UNSET', Char(258), 2),
	Insn('CHAR_FLAG1_UNSET', Char(258), 16),
	Insn('SOUND_PLAY', 804, 0, 0, 100),
	Insn('0x0D'),
	Insn('SLEEP', 300),
	Insn('CHAR_ROTATE', Char(258), 0, 400),
	Insn('EMOTE', Char(257), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(258), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(259), 0, 2000, (24, 27, 250, 0)),
	Insn('EMOTE', Char(260), 0, 2000, (24, 27, 250, 0)),
	Insn('SLEEP', 2000),
	Insn('EMOTE_STOP', Char(257)),
	Insn('EMOTE_STOP', Char(258)),
	Insn('EMOTE_STOP', Char(259)),
	Insn('EMOTE_STOP', Char(260)),
	Insn('CHAR_WATCH', Char(259), Char(257), 500),
	Insn('SLEEP', 300),
	Insn('TEXT_TALK', Char(259), Text(
		'#15100312V#0203F#11P──迟到的巴士加上\n'
		'联系不上的医院……{wait}'
		'{page}'
		'#15100313V#0201F还有最新得知的\n'
		'意外人际关系吗……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#15100314V#0301F#5P……再怎么说，这也很难\n'
		'用单纯的巧合来解释吧？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('CHAR_WATCH', Char(257), Char(259), 500),
	Insn('SLEEP', 150),
	Insn('TEXT_TALK', Char(257), Text(
		'#15100315V#0003F#6P嗯……{wait}'
		'{page}'
		'#15100316V#0013F──天很快就要黑了，\n'
		'尽快赶往乌尔斯拉医院吧。{wait}'
		'{page}'
		'#15100317V要是遇到巴士的话，\n'
		'就半路拦车乘上去好了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#15100318V#0101F#12P嗯……！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('0x5A'),
	Insn('FADE_ON', 2000, Color(0x00000000), 255),
	Insn('CAM_DISTANCE', 21650, 2500),
	Insn('0x6F', b'y'),
	Insn('0x0D'),
	Insn('0x49'),
	Insn('IMG_0xCA', Insn('1', (ResId(255), 0))),
	Insn('0xD5', 40),
	Insn('0xD5', 41),
	Insn('CHAR_SET_POS', Char(0), (-4680, 0, -11060), 180),
	Insn('FLAG_SET', Flag(1793)),
	Insn('QUEST', 77, Insn('TASK_SET', 1)),
	Insn('0xB8', 0, 0),
	Insn('0xB8', 200, 203),
	Insn('0xB8', 202, 203),
	Insn('0xB8', 100, 203),
	Insn('0xB8', 101, 203),
	Insn('0xB8', 111, 203),
	Insn('0xB8', 116, 203),
	Insn('0xB8', 117, 203),
	Insn('0xB8', 124, 203),
	Insn('SOUND_STOP', 806),
	Insn('SOUND_STOP', 891),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][63] = [
	Insn('EVENT_BEGIN', 0),
	Insn('SLEEP', 1000),
	Insn('CAM_OFFSET', (-9260, 1500, -12230), 3000),
	Insn('CAM_ROTATE', 45, 21, 0, 3000),
	Insn('0x6E', 510, 5000),
	Insn('CAM_DISTANCE', 23500, 5000),
	Insn('0x6F', b'y'),
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

data['code'][64] = [
	Insn('EVENT_BEGIN', 0),
	Insn('FADE_ON', 0, Color(0xFFFFFFFF), 0),
	Insn('FADE_ON', 500, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('FADE_OFF', 0, Color(0xFFFFFFFF)),
	Insn('0xE0', b'\x02'),
	Insn('0x09', 134217728),
	Insn('CHAR_FLAG1_SET', Char(59), 128),
	Insn('CAM_OFFSET', (50680, 2860, -111330), 0),
	Insn('CAM_ROTATE', 55, 14, 0, 0),
	Insn('0x6E', 510, 0),
	Insn('CAM_DISTANCE', 17280, 0),
	Insn('LOAD_CHCP', 'apl/ch50387', 50),
	Insn('EFF_LOAD', ResId(0), 'event\\eva02_00.eff'),
	Insn('CHAR_SET_POS', Char(257), (49980, 900, -106970), 102),
	Insn('CHAR_SET_POS', Char(258), (52090, 900, -107470), 102),
	Insn('CHAR_SET_POS', Char(259), (50300, 900, -109260), 102),
	Insn('CHAR_SET_POS', Char(260), (51400, 900, -110070), 102),
	Insn('FADE_OFF', 500, Color(0x00000000)),
	Insn('0x0D'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0300F这条大河\n'
		'就是羽扇河吗？{wait}'
		'{page}'
		'#0305F浮在正中的\n'
		'那座建筑是什么呢？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0003F嗯～我想是某种遗迹吧……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(259), Text(
		'#12P#0203F数据库里也没有相关的详细情报呢。{wait}'
		'{page}'
		'#0200F只是，这里好像被指定为\n'
		'禁止进入的区域了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#6P#0100F不知道是真是假，\n'
		'不过，听说向那个遗迹\n'
		'祈求姻缘很灵验哦。{wait}'
		'{page}'
		'#0104F据说，只要男方站在这个观景台的左边，\n'
		'女方站在右边来祈祷，\n'
		'两人就能一生永不分开了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(260), Text(
		'#12P#0306F这、这还真是\n'
		'像模像样的都市传说啊……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(257), Text(
		'#6P#0000F格蕾丝小姐委托我们拍摄的照片，\n'
		'在这里似乎能拍到很不错的呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('IF', [
		(Expr([Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 2))), Insn('NOT'), Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 3))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 4))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 5))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 6))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 7))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 8))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 9))), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 10))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('CHAR_WATCH', Char(257), Char(258), 500),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F那么艾莉，\n'
				'可以拜托你来拍照吗？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_WATCH', Char(258), Char(257), 500),
			Insn('TEXT_TALK', Char(258), Text(
				'#6P#0108F哎，好的。\n'
				'虽然我没什么自信……{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_WATCH', Char(260), Char(258), 500),
			Insn('TEXT_TALK', Char(260), Text(
				'#12P#0300F哪里哪里，应该没问题吧。{wait}'
				'{page}'
				'只要看看镜头，\n'
				'然后咔嚓一下拍下来\n'
				'不就搞定了嘛。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_WATCH', Char(258), Char(260), 500),
			Insn('TEXT_TALK', Char(258), Text(
				'#6P#0103F我说你啊……\n'
				'要拍出好照片，\n'
				'可没有那么简单哦。{wait}'
				'{page}'
				'#0100F要注意确认\n'
				'拍摄对象有没有被收入取景框中，\n'
				'还要构思摄影角度……{wait}'
				'{page}'
				'而且受到天气和风的影响，\n'
				'照片所呈现出的感觉也会有很大不同。{wait}'
				'{page}'
				'有时只要错过那一瞬的时机，\n'
				'就再也拍不到\n'
				'那么好的风景了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#12P#0200F外行和专家所拍出的照片，\n'
				'差别可是一目了然的。{wait}'
				'{page}'
				'#0203F不过，某些粗神经的人\n'
				'大概无法理解这种细致的工作吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('CHAR_WATCH', Char(260), Char(259), 500),
			Insn('TEXT_TALK', Char(260), Text(
				'#12P#0306F唔……\n'
				'你在说谁啊，说谁啊。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F好啦好啦，\n'
				'总之就交给艾莉吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#6P#0100F那么……\n'
				'我来试试看吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x5A'),
			Insn('CHAR_ROTATE', Char(258), 102, 500),
			Insn('CHAR_ROTATE', Char(257), 102, 500),
			Insn('CHAR_ROTATE', Char(259), 102, 500),
			Insn('CHAR_ROTATE', Char(260), 102, 500),
			Insn('CROSSFADE', 1000),
			Insn('CHAR_SET_CHCP', Char(258), 50),
			Insn('CHAR_SET_FRAME', Char(258), 0),
			Insn('0x0D'),
			Insn('SOUND_PLAY', 817, 0, 0, 100),
			Insn('EFF_PLAY', (ResId(0), -1), Char(258), 192, 0, 0, 1200, 0, 400, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
			Insn('SLEEP', 1000),
			Insn('SOUND_PLAY', 817, 0, 0, 100),
			Insn('EFF_PLAY', (ResId(0), -1), Char(258), 192, 0, 0, 1200, 0, 400, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
			Insn('SLEEP', 1000),
			Insn('SOUND_PLAY', 817, 0, 0, 100),
			Insn('EFF_PLAY', (ResId(0), -1), Char(258), 192, 0, 0, 1200, 0, 400, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(258), Text(
				'#6P#0103F……呼，\n'
				'为了保险起见，我多拍了几张。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F看样子，似乎已经拍好了呢。{wait}'
				'{page}'
				'感觉怎么样啊？{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#6P#0100F在没有实际显像出来之前，\n'
				'还无法确定……{wait}'
				'{page}'
				'不过，我觉得至少\n'
				'不会很差吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(259), Text(
				'#12P#0200F艾莉前辈似乎\n'
				'找回感觉了呢。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(260), Text(
				'#12P#0300F哼……\n'
				'反正只有我完全搞不懂。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F如果发现了这种风景漂亮的地方，\n'
				'就再拍些照片吧。{wait}'
				'{page}'
				'那么，我们走吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, [
			Insn('CHAR_WATCH', Char(257), Char(258), 500),
			Insn('TEXT_TALK', Char(257), Text(
				'#6P#0000F那么……\n'
				'艾莉，麻烦你拍照了哦。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('TEXT_TALK', Char(258), Text(
				'#6P#0100F嗯，知道了。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('0x5A'),
			Insn('CHAR_ROTATE', Char(258), 102, 500),
			Insn('CHAR_ROTATE', Char(257), 102, 500),
			Insn('CHAR_ROTATE', Char(259), 102, 500),
			Insn('CHAR_ROTATE', Char(260), 102, 500),
			Insn('CROSSFADE', 1000),
			Insn('CHAR_SET_CHCP', Char(258), 50),
			Insn('CHAR_SET_FRAME', Char(258), 0),
			Insn('0x0D'),
			Insn('SOUND_PLAY', 817, 0, 0, 100),
			Insn('EFF_PLAY', (ResId(0), -1), Char(258), 192, 0, 0, 1200, 0, 400, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
			Insn('SLEEP', 1000),
			Insn('SOUND_PLAY', 817, 0, 0, 100),
			Insn('EFF_PLAY', (ResId(0), -1), Char(258), 192, 0, 0, 1200, 0, 400, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
			Insn('SLEEP', 1000),
			Insn('SOUND_PLAY', 817, 0, 0, 100),
			Insn('EFF_PLAY', (ResId(0), -1), Char(258), 192, 0, 0, 1200, 0, 400, 0, 0, 0, 0, (1000, 1000, 1000), 255, 0, 0, 0, 0, 0, 0, 0),
			Insn('SLEEP', 1000),
			Insn('TEXT_TALK', Char(258), Text(
				'#6P#0100F……呼，\n'
				'大概就这样吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
			Insn('EXPR_VAR', 5, Expr([Insn('CONST', 0), Insn('SET'), Insn('END')])),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 2))), Insn('END')]), [
					Insn('EXPR_VAR', 5, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 3))), Insn('END')]), [
					Insn('EXPR_VAR', 5, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 4))), Insn('END')]), [
					Insn('EXPR_VAR', 5, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 5))), Insn('END')]), [
					Insn('EXPR_VAR', 5, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 6))), Insn('END')]), [
					Insn('EXPR_VAR', 5, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 7))), Insn('END')]), [
					Insn('EXPR_VAR', 5, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 8))), Insn('END')]), [
					Insn('EXPR_VAR', 5, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 9))), Insn('END')]), [
					Insn('EXPR_VAR', 5, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('EXEC', Insn('QUEST_GET', 24, Insn('TASK_GET', 10))), Insn('END')]), [
					Insn('EXPR_VAR', 5, Expr([Insn('CONST', 1), Insn('ADD_SET'), Insn('END')])),
				]),
				(None, []),
			]),
			Insn('IF', [
				(Expr([Insn('VAR', 5), Insn('CONST', 4), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(257), Text(
						'#6P#0000F辛苦了，\n'
						'看来已经顺利拍好了啊。{wait}'
						'{page}'
						'这样一来，就拍完了格蕾丝小姐\n'
						'所要求的五张照片了。\n'
						'现在随时都可以去交付了啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(257), Text(
						'#6P#0000F辛苦了，\n'
						'看来已经顺利拍好了啊。{wait}'
						'{page}'
						'那么，我们走吧。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
	]),
	Insn('FADE_ON', 1000, Color(0x00000000), 255),
	Insn('0x0D'),
	Insn('CHAR_SET_POS', Char(0), (52100, 900, -107040), 102),
	Insn('CHAR_SET_CHCP', Char(258), 255),
	Insn('CHAR_SET_FRAME', Char(258), 0),
	Insn('0xD5', 50),
	Insn('QUEST', 24, Insn('TASK_SET', 4)),
	Insn('SLEEP', 500),
	Insn('0x0A', 134217728),
	Insn('0x37'),
	Insn('0x65', 4, 1),
	Insn('0x66', 1, 1),
	Insn('EVENT_END', 5),
	Insn('RETURN'),
]

data['code'][65] = [
	Insn('EVENT_BEGIN', 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1569)), Insn('FLAG', Flag(1792)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('IF', [
				(Expr([Insn('ATTR', 10), Insn('CONST', 9), Insn('EQ'), Insn('END')]), [
					Insn('TEXT_TALK', Char(266), Text(
						'#0603F……这边的事\n'
						'交给一课的人就行了……{wait}'
						'{page}'
						'#0601F若是没有高层那边的问题，\n'
						'本应集中全部人手去\n'
						'调查鲁巴彻那边的事……{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(259), Text(
						'#0200F达德利警官\n'
						'似乎很烦恼。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(260), Text(
						'#0300F哈哈，一课好像也有\n'
						'各种麻烦事嘛。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(266), Text(
						'#0600F……闭嘴，\n'
						'我们只需做好\n'
						'自己该做的事！{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
				(None, [
					Insn('TEXT_TALK', Char(266), Text(
						'#0601F……你想去哪里？\n'
						'机场的事\n'
						'就交给搜查一课处理！{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F是、是啊。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(258), Text(
						'#0108F（达德利警官好像\n'
						'\u3000十分焦躁呢。）{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
		]),
		(Expr([Insn('FLAG', Flag(1566)), Insn('FLAG', Flag(1569)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('0x4B', Char(15), -1),
			Insn('CHAR_WATCH', Char(15), Char(0), 500),
			Insn('IF', [
				(Expr([Insn('FLAG', Flag(7)), Insn('NOT'), Insn('END')]), [
					Insn('TEXT_TALK', Char(15), Text(
						'……慢着，特务支援课。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(15), Text(
						'克洛斯贝尔机场\n'
						'正在进行临时设备检查，\n'
						'禁止进入。{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('TEXT_TALK', Char(257), Text(
						'#0005F（临时设备检查……？\n'
						'\u3000有点古怪啊。）{wait}'
					)),
					Insn('TEXT_WAIT'),
					Insn('FLAG_SET', Flag(7)),
				]),
				(None, [
					Insn('TEXT_TALK', Char(15), Text(
						'……慢着，特务支援课。\n'
						'克洛斯贝尔机场\n'
						'现在是禁止进入的。{wait}'
					)),
					Insn('TEXT_WAIT'),
				]),
			]),
			Insn('CHAR_ROTATE', Char(15), 270, 500),
			Insn('0x4C', Char(15), -1),
		]),
		(None, [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F这边是克洛斯贝尔机场。\n'
				'……没什么事要去。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
	]),
	Insn('SLEEP', 50),
	Insn('CHAR_SET_POS', Char(0), (11250, 0, -17610), 270),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][66] = [
	Insn('EVENT_BEGIN', 1),
	Insn('0x4B', Char(41), -1),
	Insn('0x4B', Char(15), -1),
	Insn('EMOTE', Char(41), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 50),
	Insn('EMOTE', Char(15), 0, 2000, (38, 38, 250, 1)),
	Insn('SLEEP', 1000),
	Insn('FORK', 41, 1, [
		Insn('CHAR_WATCH', Char(254), Char(0), 500),
	]),
	Insn('FORK', 15, 1, [
		Insn('CHAR_WATCH', Char(254), Char(0), 500),
	]),
	Insn('TEXT_TALK', Char(41), Text(
		'达德利长官……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'达德利搜查官，您辛苦了！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'……话说回来，您怎么会和\n'
		'特务支援课在一起……{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(266), Text(
		'#0603F详情稍后再说明……{wait}'
		'{page}'
		'#0600F对了，你们这边的情况如何？{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(41), Text(
		'嗯，看样子，果然是假情报……\n'
		'现在刚刚收工。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(266), Text(
		'#0608F……是吗。{wait}'
		'{page}'
		'#0600F我很快就会与你们会合的，\n'
		'在此之前，一课内的事务就拜托你们了。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(15), Text(
		'是！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(41), Text(
		'是！{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('FLAG_SET', Flag(1611)),
	Insn('0xB5', b'\x00\x00\x80\x00'),
	Insn('SLEEP', 50),
	Insn('CHAR_ROTATE', Char(41), 180, 0),
	Insn('CHAR_ROTATE', Char(15), 0, 0),
	Insn('CHAR_SET_POS', Char(0), (11250, 0, -17610), 270),
	Insn('0x4C', Char(41), -1),
	Insn('0x4C', Char(15), -1),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][67] = [
	Insn('EVENT_BEGIN', 1),
	Insn('IF', [
		(Expr([Insn('FLAG', Flag(1560)), Insn('FLAG', Flag(1566)), Insn('NOT'), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 48, Insn('TASK_GET', 5))), Insn('BOOL_AND'), Insn('EXEC', Insn('QUEST_GET', 48, Insn('FLAG_GET', 16))), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0003F（如此说来，我们的手上还有人偶工房\n'
				'\u3000交付的箱子呢……）{wait}'
				'{page}'
				'#0000F（似乎是很昂贵的东西，\n'
				'\u3000还是先拿去交给伊美黛夫人吧。）{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(768)), Insn('FLAG', Flag(778)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0000F难得有机会，还是坐巴士吧。{wait}'
				'{page}'
				'去那边的公车站看看，\n'
				'应该就能查到下一班巴士的发车时间了。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(Expr([Insn('FLAG', Flag(1342)), Insn('FLAG', Flag(1536)), Insn('NOT'), Insn('BOOL_AND'), Insn('END')]), [
			Insn('TEXT_TALK', Char(257), Text(
				'#0003F可不能带着琪雅\n'
				'在市外走啊。{wait}'
				'{page}'
				'#0000F这次还是坐巴士吧。{wait}'
			)),
			Insn('TEXT_WAIT'),
		]),
		(None, []),
	]),
	Insn('CHAR_SET_POS', Char(0), (0, 0, -46000), 0),
	Insn('EVENT_END', 4),
	Insn('RETURN'),
]

data['code'][68] = [
	Insn('TEXT_START', Char(255)),
	Insn('TEXT_TALK', Char(257), Text(
		'#0005F如此说来……\n'
		'我们的手上还有人偶工房\n'
		'交付的箱子呢。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_TALK', Char(258), Text(
		'#0100F里面的人偶是很昂贵的作品，\n'
		'在去医院之前，\n'
		'还是先拿去交给伊美黛夫人吧。{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]

data['code'][69] = [
	Insn('FADE_ON', 300, Color(0x00000000), 100),
	Insn('TEXT_SET_NAME', Translate('')),
	Insn('TEXT_SET_POS', -1, -1, -1, -1),
	Insn('TEXT_MESSAGE', Char(255), Text(
		'{color 5}北丄克洛斯贝尔市\n'
		'东丄克洛斯贝尔机场\n'
		'南丄圣乌尔斯拉医科大学\u3000１５３塞尔矩{wait}'
	)),
	Insn('TEXT_WAIT'),
	Insn('TEXT_RESET', b'\x00'),
	Insn('FADE_OFF', 300, Color(0x00000000)),
	Insn('TEXT_SET_POS', -1, 280, 60, 3),
	Insn('TEXT_END', Char(255)),
	Insn('RETURN'),
]
