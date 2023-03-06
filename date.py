import datetime
date1 = datetime.datetime(2023, 2, 7)
date2 = datetime.datetime(2022, 12, 7)
dif = (date1 - date2).total_seconds()
print(dif)