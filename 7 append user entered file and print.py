import csv

file = open("ICT_clubmembers.csv", "a")

name = input("Enter pupil's FULL name: ")
ictclass = input("Enter Qualification: ")
year = input("Enter Year Group: ")
birthyear = input("Enter Year of Birth: ")
grade = input("Enter Grade: ")

newrecord = name + "," + ictclass + "," + year + "," + birthyear + "," + grade+ "\n"
file.write(str(newrecord))
file.close()

file = open("ICT_clubmembers.csv", "r")
for x in file:
    print(x)
file.close()
