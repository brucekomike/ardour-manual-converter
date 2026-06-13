import re
import os


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
for page in index_list:
  print(page)
  if page[3] == 1:
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
    index_files[index_index].write("```{toctree}\n")
  else:
    index_files[index_index].write(f"/{page[1]}\n")
    page_dir=os.path.dirname(f"{outdir}/{page[1]}")
    os.makedirs(f"{page_dir}", exist_ok=True)
    os.system(f"echo \"# {page[0]}\" > {outdir}/{page[1]}.md")
    os.system(f"pandoc -i manual/include/{page[3]} -t markdown -o - >> {outdir}/{page[1]}.md")

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