import re
def read_file(fpath:str):
    with open(fpath, mode='r', encoding='utf8') as f:
        return f.read()
file=read_file("row.txt")
print(re.sub("[\n,.]", ":", file))