import re
str=input()
print(re.sub('(?<!^)(?=[A-Z])', '_', str).lower())