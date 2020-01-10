#12 days of Christmas

giftList = ['partridge in a pear tree', 'turtle doves', 'french hens', 'calling birds', 'gold rings', 'geese a-laying', 'swans a swimming', 'maids a-milking', 'ladies dancing', 'lords a-leaping', 'pipers piping', 'drummers drumming']
numbOfDays = len(giftList) #12 gifts, prints an extra one per day

for day in range (1, numbOfDays + 1):
    if day == 1:
        verse = "On the " + str(day) + "st"
    elif day == 2:
        verse = "On the " + str(day) + "nd"
    elif day == 3:
        verse = "On the " + str(day) + "rd"
    else:
        verse = "On the " + str(day) + "th"


    verse = verse + " day of christmas my true love sent to me "
    #loops through the list in reverse
    for giftNumb in range (day -1,-1,-1):
        if giftNumb == 0:
            if day == 1:
                verse += " a " + giftList[giftNumb] + "."
            else:
                verse += " and a " + giftList[giftNumb] + "."
        else:
            verse += " " + str(giftNumb + 1) + " " + giftList[giftNumb] + ","
    print (verse + "\n")
