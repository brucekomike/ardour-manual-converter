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
index_index=-1
index_dir_flag = False
page_list=[]
local_chapter_list=[]
for block in file_blocks:
    data = parse_block(block)
    if data == {}:
        continue
    if data.get("part") == "part":
        file_path = f"{outdir}/{slugify(data.get('title'))}"
        if data.get("uri") is not None:
            file_path = f"{outdir}/{data.get('uri')}"
        index_list.append(file_path)
        index_index += 1
        print(f"\n{index_list[index_index]}", end=" ")
        index_list[index_index] = f"{file_path}/index.md"
        os.makedirs(file_path, exist_ok=True)
        
        if len(local_chapter_list) > 0:
            page_list.append(local_chapter_list)
            
        local_chapter_list=[]
        
    else:
        print(index_index, end=" ")
        if data.get("uri") is None:
            file_path = f"{outdir}/{data.get('link')}.md"
        else:
            file_path = f"{outdir}/{data.get('uri')}.md"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        os.system(f"pandoc -i manual/include/{data.get('include')} -o {file_path}")
        local_chapter_list.append(file_path)

page_list.append(local_chapter_list)


index_file = f"{outdir}/index.md"
os.system(f"echo '# index' > {index_file}")
os.system("echo '```{toctree}' >> "+f"{index_file}")
for index in index_list:
    os.system(f"echo '{index}' >> {index_file}")
    os.system(f"echo '# {index}' > {index}")
    os.system("echo '```{toctree}' >> "+f"{index}")
    for page in page_list[index_list.index(index)]:
        os.system(f"echo '{page}' >> {index}")
    os.system(f"echo '```' >> {index}")
os.system(f"echo '```' >> {index_file}")



