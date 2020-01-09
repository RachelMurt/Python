import csv

file = open("ICT_clubmembers.csv", "w")
#NAME, EXAM, YEAR GROUP, GRADE, YEAR OF BIRTH

newrecord="James Bond, GCSE ICT, Year 12, 2001, B\n"
file.write(str(newrecord))

newrecord="Dr Who, A'Level ICT, Year 14, 1999, A\n"
file.write(str(newrecord))

newrecord="Luke Skywalker, BTEC ICT, Year 13, 2000, A\n"
file.write(str(newrecord))

newrecord="Rocky Balboa, GCSE ICT, Year 11, 2000, A\n"
file.write(str(newrecord))

newrecord="Diana Prince, A'Level ICT, Year 14, 1999, B\n"
file.write(str(newrecord))

file.close()
