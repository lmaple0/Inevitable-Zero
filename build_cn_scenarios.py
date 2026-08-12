#!/usr/bin/env python3
"""Rebuild the checked-in Chinese merged scenario dumps without a Vita donor."""

import argparse
import shutil
from pathlib import Path

import kouzou
import scena
import insn


def load_dump(path: Path):
	namespace = {"data": None}
	exec(path.read_text(encoding="utf-8"), dict(insn.__dict__), namespace)
	if namespace["data"] is None:
		raise ValueError(f"dump did not define data: {path}")
	return namespace["data"]


def main(source: Path, output: Path) -> None:
	if not source.is_dir():
		raise ValueError(f"source directory does not exist: {source}")
	if output.exists():
		shutil.rmtree(output)
	output.mkdir(parents=True)

	files = sorted(source.glob("*.py"))
	if not files:
		raise ValueError(f"no Python scenario dumps found in {source}")

	params = {"_insns": insn.insn_zero_22, "_encoding": "gbk"}
	for path in files:
		out = output / path.with_suffix(".bin").name
		with out.open("wb") as stream:
			kouzou.write(scena.scenaStruct, stream, load_dump(path), params)
		print(out)

	print(f"rebuilt {len(files)} Chinese scenarios")


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"--source",
		type=Path,
		default=Path("text/cn/scena"),
		help="directory containing checked-in Chinese .py scenario dumps",
	)
	parser.add_argument("output", type=Path, help="new output directory for .bin files")
	args = parser.parse_args()
	main(args.source, args.output)
