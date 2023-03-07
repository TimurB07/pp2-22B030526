import re
def read_file(fpath:str):
    with open(fpath, mode='r', encoding='utf8') as f:
        return f.read()
file=read_file("row.txt")
pattern = 'a[b]{2,3}'
print(re.findall(pattern, file))