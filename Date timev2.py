import datetime

#format = "%a %b %d %H:%M:%S %Y"
#format = "%H:%M:%S %Y"
format = "%a %d %b %Y"

today = datetime.datetime.today()
print('ISO     :', today)

s = today.strftime(format)
print('strftime:', s)

d = datetime.datetime.strptime(s, format)
print('strptime:', d.strftime(format))
