#random days of week

from random import randint

day = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
for i in range(1):
    print (day[randint(0,6)])
