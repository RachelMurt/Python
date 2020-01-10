print("=======================================")
pupil = input("Search Student's name: ")
print("=======================================")

file = open("ICT_clubmembers.csv","r")
x = 0

for row in file:
    if pupil in str(row):
        print("Student Found: ")
        print(row)
        x = x + 1
if x == 0:
    print("Sorry that student cannot be found.")
file.close()
