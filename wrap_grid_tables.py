#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from pathlib import Path


BORDER_RE = re.compile(r"^\+[+=\- ]+\+$")


def is_grid_table_border(line: str) -> bool:
  return bool(BORDER_RE.match(line.rstrip("\n")))


def is_grid_table_row(line: str) -> bool:
  return line.lstrip().startswith("|")


def fence_delimiter(line: str) -> str | None:
  stripped = line.lstrip()
  if stripped.startswith("```"):
    return "```"
  if stripped.startswith("~~~"):
    return "~~~"
  return None


def wrap_grid_tables(text: str) -> tuple[str, int]:
  lines = text.splitlines(keepends=True)
  output: list[str] = []
  index = 0
  wrapped_tables = 0
  active_fence: str | None = None

  while index < len(lines):
    line = lines[index]

    if active_fence is not None:
      output.append(line)
      if line.lstrip().startswith(active_fence):
        active_fence = None
      index += 1
      continue

    fence = fence_delimiter(line)
    if fence is not None:
      active_fence = fence
      output.append(line)
      index += 1
      continue

    if is_grid_table_border(line) and index + 1 < len(lines) and is_grid_table_row(lines[index + 1]):
      table_start = index
      table_end = index + 1

      while table_end < len(lines) and (
        is_grid_table_border(lines[table_end]) or is_grid_table_row(lines[table_end])
      ):
        table_end += 1

      if output and output[-1].strip():
        output.append("\n")

      output.append("```{eval-rst}\n")
      output.extend(lines[table_start:table_end])
      if output[-1] and not output[-1].endswith("\n"):
        output.append("\n")
      output.append("```\n")
      wrapped_tables += 1
      index = table_end
      continue

    output.append(line)
    index += 1

  return "".join(output), wrapped_tables


def process_markdown_file(path: Path) -> int:
  original_text = path.read_text(encoding="utf-8")
  updated_text, wrapped_tables = wrap_grid_tables(original_text)
  if updated_text != original_text:
    path.write_text(updated_text, encoding="utf-8")
  return wrapped_tables


def main() -> int:
  parser = argparse.ArgumentParser(
    description="Wrap grid tables in markdown files inside eval-rst fences."
  )
  parser.add_argument(
    "root",
    nargs="?",
    default="docs/source",
    help="Root directory to scan recursively for markdown files.",
  )
  args = parser.parse_args()

  root = Path(args.root)
  if not root.exists():
    raise SystemExit(f"Path not found: {root}")

  touched_files = 0
  wrapped_tables = 0

  for path in root.rglob("*.md"):
    original_text = path.read_text(encoding="utf-8")
    updated_text, file_wrapped_tables = wrap_grid_tables(original_text)
    if updated_text != original_text:
      path.write_text(updated_text, encoding="utf-8")
      touched_files += 1
    wrapped_tables += file_wrapped_tables

  print(f"Updated {touched_files} file(s), wrapped {wrapped_tables} table(s).")
  return 0


if __name__ == "__main__":
  raise SystemExit(main())