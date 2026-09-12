import re
import os
import subprocess

RAW_IMAGE_BASE_URL = "https://raw.githubusercontent.com/Ardour/manual/refs/heads/master/source/images/"
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")
MARKDOWN_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
HTML_IMAGE_RE = re.compile(r'(<img\b[^>]*\bsrc=["\'])([^"\']+)(["\'])', re.IGNORECASE)
MALFORMED_KBD_RE = re.compile(r"(<kbd\b[^>]*>[^<]*)<kbd>", re.IGNORECASE)
HEADING_ANCHOR_RE = re.compile(
  r"^(?P<heading>[ \t]{0,3}#{1,6}[ \t]+.*?)[ \t]+\{#(?P<anchor>[^}\r\n]+)\}[ \t]*$",
  re.MULTILINE,
)


def parse_block(block: str) -> dict[str, str]:
  data = {}
  for line in block.splitlines():
    if ":" not in line:
      continue
    key, value = line.split(":", 1)
    data[key.strip()] = value.strip()
  return data


def slugify(value: str) -> str:
  value = (value or "").strip().lower()
  value = re.sub(r"[^a-z0-9]+", "-", value)
  return re.sub(r"-+", "-", value).strip("-")


def is_grid_table_border(line: str) -> bool:
  return bool(re.match(r"^\+[+=\- ]+\+$", line.rstrip("\n")))


def is_grid_table_row(line: str) -> bool:
  return line.lstrip().startswith("|")


def wrap_grid_tables(text: str) -> str:
  lines = text.splitlines(keepends=True)
  output = []
  index = 0

  while index < len(lines):
    if is_grid_table_border(lines[index]) and index + 1 < len(lines) and is_grid_table_row(lines[index + 1]):
      table_start = index
      table_end = index + 1

      while table_end < len(lines) and (
        is_grid_table_border(lines[table_end]) or is_grid_table_row(lines[table_end])
      ):
        table_end += 1

      output.append("```{eval-rst}\n")
      output.extend(lines[table_start:table_end])
      if output and not output[-1].endswith("\n"):
        output.append("\n")
      output.append("```\n")
      index = table_end
      continue

    output.append(lines[index])
    index += 1

  return "".join(output)


def wrap_grid_tables_in_markdown_tree(root_dir: str) -> None:
  for current_root, _, files in os.walk(root_dir):
    for file_name in files:
      if not file_name.endswith(".md"):
        continue

      file_path = os.path.join(current_root, file_name)
      with open(file_path, "r", encoding="utf-8") as file:
        original_text = file.read()

      updated_text = wrap_grid_tables(original_text)
      if updated_text == original_text:
        continue

      with open(file_path, "w", encoding="utf-8") as file:
        file.write(updated_text)


def _normalize_image_path(path: str) -> str | None:
  candidate = path.strip()
  if not candidate:
    return None
  if candidate.startswith(("http://", "https://", "data:", "mailto:", "#")):
    return None

  normalized = candidate.replace("\\", "/")
  lower_normalized = normalized.lower()

  image_path = None
  if "source/images/" in lower_normalized:
    image_path = normalized[lower_normalized.index("source/images/") + len("source/images/") :]
  elif "/images/" in lower_normalized:
    image_path = normalized[lower_normalized.index("/images/") + len("/images/") :]
  elif lower_normalized.startswith("images/"):
    image_path = normalized[len("images/") :]
  elif normalized.lower().endswith(IMAGE_EXTENSIONS) and "/" not in normalized:
    image_path = normalized

  if not image_path:
    return None

  image_path = image_path.lstrip("./")
  return f"{RAW_IMAGE_BASE_URL}{image_path}"


def rewrite_image_links(text: str) -> str:
  def markdown_replacer(match: re.Match[str]) -> str:
    alt_text = match.group(1)
    destination = match.group(2).strip()

    has_angle_brackets = destination.startswith("<")
    link_target = destination
    trailing = ""

    if has_angle_brackets:
      closing_index = destination.find(">")
      if closing_index != -1:
        link_target = destination[1:closing_index]
        trailing = destination[closing_index + 1 :]
    elif " " in destination:
      link_target, trailing = destination.split(" ", 1)
      trailing = f" {trailing}"

    rewritten = _normalize_image_path(link_target)
    if not rewritten:
      return match.group(0)

    if has_angle_brackets:
      return f"![{alt_text}](<{rewritten}>{trailing})"
    return f"![{alt_text}]({rewritten}{trailing})"

  def html_replacer(match: re.Match[str]) -> str:
    rewritten = _normalize_image_path(match.group(2))
    if not rewritten:
      return match.group(0)
    return f"{match.group(1)}{rewritten}{match.group(3)}"

  text = MARKDOWN_IMAGE_RE.sub(markdown_replacer, text)
  return HTML_IMAGE_RE.sub(html_replacer, text)


def sanitize_html_for_pandoc(text: str) -> str:
  return MALFORMED_KBD_RE.sub(r"\1</kbd>", text)


def move_heading_anchors(text: str) -> str:
  return HEADING_ANCHOR_RE.sub(r"\g<heading>\n{#\g<anchor>}", text)


def convert_html_to_markdown(include_path: str) -> str:
  with open(include_path, "r", encoding="utf-8") as html_file:
    html_input = sanitize_html_for_pandoc(html_file.read())

  pandoc_output = subprocess.check_output(
    ["pandoc", "-f", "html", "-t", "markdown-multiline_tables-simple_tables", "-o", "-"],
    input=html_input,
    text=True,
  )
  return move_heading_anchors(rewrite_image_links(pandoc_output))


def main() -> None:
  with open("manual/master-doc.txt", "r", encoding="utf-8") as file:
    file_contents = file.read()

  raw_blocks = re.split(r"^---\s*$", file_contents, flags=re.MULTILINE)
  file_blocks = [block.strip() for block in raw_blocks if block.strip()]

  outdir="docs/source"
  index_list=[]

  for block in file_blocks:
    page_info=[]
    #0 page title
    #1 page uri
    #2 parrent level
    #3 index flag / include html
    data = parse_block(block)
    # uri check
    if data.get("uri") is None:
      current_uri = slugify(data.get("title"))
    else:
      current_uri = data.get("uri")
    page_info.append(data.get("title"))
    page_info.append(current_uri)
    # index check
    if data.get("part") == "part":
      page_info.append(0)
    if data.get("part") == "chapter":
      page_info.append(1)
    if data.get("part") == "subchapter":
      page_info.append(2)
    if data.get("part") == "section":
      page_info.append(3)

    if data.get("include") is None:
      page_info.append(1)
    else:
      page_info.append(data.get("include"))

    index_list.append(page_info)
    # print(page_info)

  index_list=index_list[1:]
  index_files=[0,0,0,0]
  index_index=0
  page_index=0
  for page in index_list:
    try:
      index_list[page_index+1]
      if page[2] < index_list[page_index+1][2]:
        embed_index_flag=True
      else:
        embed_index_flag=False
    except IndexError:
      pass

    print(page)
    
    if page[3] == 1 or embed_index_flag:
      if page[2] > index_index:
        index_index += 1
      elif page[2] < index_index:
        index_index = page[2]
      os.makedirs(f"{outdir}/{page[1]}", exist_ok=True)
      if index_files[index_index] != 0:
        index_files[index_index].write("```\n")
        index_files[index_index].close()
        index_files[index_index] = 0
      if index_index > 0:
        index_files[index_index-1].write(f"/{page[1]}/index.md\n")
      index_files[index_index] = open(f"{outdir}/{page[1]}/index.md", "w", encoding="utf-8")
      index_files[index_index].write(f"# {page[0]}\n")
      if page[3] != 1:
        pandoc_output = convert_html_to_markdown(f"manual/include/{page[3]}")
        index_files[index_index].write(pandoc_output)
        index_files[index_index].write("\n")
      index_files[index_index].write("```{toctree}\n")
    else:
      index_files[index_index].write(f"/{page[1]}\n")
      page_dir=os.path.dirname(f"{outdir}/{page[1]}")
      os.makedirs(f"{page_dir}", exist_ok=True)
      pandoc_output = convert_html_to_markdown(f"manual/include/{page[3]}")
      with open(f"{outdir}/{page[1]}.md", "w", encoding="utf-8") as markdown_file:
        markdown_file.write(f"# {page[0]}\n")
        markdown_file.write(pandoc_output)
    page_index+=1

  for index in index_files:
    if index != 0:
      index.write("```\n")
      index.close()

  with open(f"{outdir}/index.md", "w", encoding="utf-8") as index_file:
    index_file.write("# index\n")
    index_file.write("```{toctree}\n")
    for page in index_list:
      if page[3] == 1 and page[2] == 0:
        index_file.write(f"/{page[1]}/index.md\n")
    index_file.write("```\n")
    index_file.close()

  wrap_grid_tables_in_markdown_tree(outdir)


if __name__ == "__main__":
  main()