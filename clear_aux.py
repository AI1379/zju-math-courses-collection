#!/usr/bin/env python3
"""recursively remove LaTeX auxiliary/generated files by extension

Usage examples:
  python clear_aux.py          # dry-run (list files that would be removed)
  python clear_aux.py --yes    # actually delete files
  python clear_aux.py --ext .pdf,.tmp --yes  # add extensions

This script walks the current directory and all subdirectories (skipping
common VCS dirs) and removes files whose extensions match the configured set.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Set, Iterable


DEFAULT_EXTS = {
	".aux",
	".log",
	".out",
	".toc",
	".lof",
	".lot",
	".fls",
	".fdb_latexmk",
	".synctex.gz",
	".synctex",
	".bbl",
	".blg",
	".nav",
	".snm",
	".vrb",
	".idx",
	".ilg",
	".ind",
	".pyg",
	".xdv",
	".dvi",
	".synctex.gz",
	".run.xml",
}

SKIP_DIRS = {".git", ".svn", "node_modules", "build", "dist"}


def parse_ext_list(s: str) -> Set[str]:
	parts = [p.strip() for p in s.split(",") if p.strip()]
	out = set()
	for p in parts:
		if not p.startswith("."):
			p = "." + p
		out.add(p.lower())
	return out


def find_files(root: Path, exts: Iterable[str]) -> list[Path]:
	exts = {e.lower() for e in exts}
	found: list[Path] = []
	for path in root.rglob("*"):
		if not path.is_file():
			continue
		# skip files inside skip dirs
		parts = {p for p in path.parts}
		if parts & SKIP_DIRS:
			continue
		name = path.name.lower()
		for e in exts:
			if e.endswith(".gz"):
				# handle compressed extensions like .synctex.gz
				if name.endswith(e):
					found.append(path)
					break
			else:
				if path.suffix.lower() == e:
					found.append(path)
					break
	return found


def confirm(prompt: str) -> bool:
	try:
		resp = input(prompt).strip().lower()
	except EOFError:
		return False
	return resp in ("y", "yes")


def main() -> None:
	p = argparse.ArgumentParser(description="Recursively remove LaTeX auxiliary/generated files by extension")
	p.add_argument("--yes", "-y", action="store_true", help="actually delete files (default: dry-run)")
	p.add_argument("--ext", "-e", type=str, default="", help="additional comma-separated extensions to remove (e.g. .pdf,.tmp)")
	p.add_argument("--include-pdf", action="store_true", help="include PDF files in removal (adds .pdf to extensions)")
	p.add_argument("--root", "-r", type=str, default=".", help="root directory to start (default: current directory)")
	p.add_argument("--quiet", "-q", action="store_true", help="only print summary")
	args = p.parse_args()

	root = Path(args.root).resolve()
	exts = set(DEFAULT_EXTS)
	if args.include_pdf:
		exts.add(".pdf")
	if args.ext:
		exts.update(parse_ext_list(args.ext))

	files = find_files(root, exts)

	if not args.quiet:
		if files:
			print(f"Found {len(files)} file(s) matching extensions: {', '.join(sorted(exts))}\n")
			for f in files:
				print(f)
		else:
			print("No files found matching configured extensions.")

	if not files:
		return

	if not args.yes:
		if not confirm("Proceed to delete these files? [y/N]: "):
			print("Aborted — no files were deleted.")
			return

	removed = 0
	for f in files:
		try:
			f.unlink()
			removed += 1
		except Exception as exc:
			print(f"Failed to remove {f}: {exc}")

	print(f"Removed {removed} file(s).")


if __name__ == "__main__":
	main()

