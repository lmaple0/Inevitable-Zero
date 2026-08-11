import json
import subprocess
import tempfile
from pathlib import Path

import insn
import translate


class VitaCnEncoding:
	def __init__(self, charmap_path):
		data = json.loads(Path(charmap_path).read_text(encoding="utf-8"))
		self.mapping = {bytes.fromhex(code): item["char"] for code, item in data.items()}
		self.unknown_codes = set()

	def decode(self, data):
		output = []
		index = 0
		while index < len(data):
			byte = data[index]
			if byte < 0x80:
				output.append(chr(byte))
				index += 1
				continue
			if index + 1 >= len(data):
				raise UnicodeDecodeError("vita-cn", data, index, index + 1, "orphan high byte")
			token = data[index:index + 2]
			try:
				output.append(self.mapping[token])
			except KeyError:
				code = token.hex().upper()
				self.unknown_codes.add(code)
				output.append(f"<VITA_{code}>")
			index += 2
		return "".join(output)

	def encode(self, text):
		raise UnicodeEncodeError("vita-cn", text, 0, len(text), "read-only source encoding")


def walk_untranslated(obj):
	if isinstance(obj, insn.Translate):
		if not getattr(obj, "translated", False):
			yield str(obj)
		return
	if isinstance(obj, insn.Insn):
		yield from walk_untranslated(obj.args)
	elif isinstance(obj, (list, tuple)):
		for item in obj:
			yield from walk_untranslated(item)
	elif isinstance(obj, dict):
		for key, value in obj.items():
			yield from walk_untranslated(key)
			yield from walk_untranslated(value)


def collect_strings(scripts, quests):
	strings = []
	for script in scripts.values():
		strings.extend(walk_untranslated(script))
	for quest in quests:
		for key in ("name", "client", "description"):
			strings.append(quest[key])
		strings.extend(quest["steps"])
	return list(dict.fromkeys(strings))


def unresolved_strings(strings):
	return [string for string in strings if "<VITA_" in string]


def opencc_tw2sp(strings, zcodec):
	with tempfile.TemporaryDirectory(prefix="inevitable-zero-cn-") as temporary:
		root = Path(temporary)
		input_path = root / "strings.json"
		output_dir = root / "converted"
		output_dir.mkdir()
		input_path.write_text(json.dumps(strings, ensure_ascii=False), encoding="utf-8")
		subprocess.check_call([str(zcodec), "-tw2s", str(input_path), "-o", str(output_dir)])
		converted = json.loads((output_dir / input_path.name).read_text(encoding="utf-8"))
	if len(strings) != len(converted):
		raise ValueError("OpenCC output length mismatch")
	return dict(zip(strings, converted))


class MappingTranslator(translate.BaseTranslator):
	def __init__(self, mapping):
		super().__init__()
		self.mapping = mapping

	def translate(self, string):
		return self.mapping[string]


def convert_plain_strings(obj, mapping):
	if isinstance(obj, str):
		return mapping.get(obj, obj)
	if isinstance(obj, list):
		return [convert_plain_strings(item, mapping) for item in obj]
	if isinstance(obj, tuple):
		return type(obj)(convert_plain_strings(item, mapping) for item in obj)
	if isinstance(obj, dict):
		return {key: convert_plain_strings(value, mapping) for key, value in obj.items()}
	return obj
