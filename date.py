import datetime
td = datetime.date.today()
print(td)
yd=td - datetime.timedelta(days=1)
print(yd)
tm=td+datetime.timedelta(days=1)
print(tm)
