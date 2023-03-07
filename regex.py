import re
str=input()
print(re.sub('(?:^|_)([a-z])', lambda x: x.group(1).upper(), str))