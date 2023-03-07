import re
str=input()
print(re.sub('([A-Z][a-z]+)',r' \1', str))