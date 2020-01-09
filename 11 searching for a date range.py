import csv

print("==========================================================")
print("Range search - Searching for student by years of birth ")
print("==========================================================")

dateStart = int(input("Enter Year From: "))
dateEnd = int(input("Enter Year To: "))

file = list(csv.reader(open("ICT_clubmembers.csv")))

temp =[]
for row in file:
    temp.append(row)

x = 0
for row in temp:
    if int(temp[x][3]) >= dateStart and int(temp[x][3]) <= dateEnd:
        print(temp[x])
    x = x + 1
