import re
def read_file(fpath:str):
    with open(fpath, mode='r', encoding='utf8') as f:
        return f.read()
file=read_file("row.txt")
pattern = '[А-Я][а-я]+'
print(re.findall(pattern, file))