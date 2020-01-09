import csv

print("Welcome to the Search Tool")
print("Please choose what you want to search for:")
choice = int(input("Student Name [1], Subject [2], Date of Birth [3], Grade [4], Please choose a number: "))

def student():
  pupil = input("Search Student's name: ")
  
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

def subject():
  subject = input("Search students by Subject: ")
  
  file = open("ICT_clubmembers.csv","r")
  x = 0
  
  for row in file:
    if subject in str(row):
      print("Subjects Found: ")
      print(row)
      x = x + 1
      
  if x == 0:
    print("Sorry, that subject doesn't exist.")
  file.close()
  
def date():
  print("Range search - Searching for student by years of birth ")
  
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
      
def grade():
  grade = input("Search students by Grade: ")
  
  file = open("ICT_clubmembers.csv","r")
  x = 0
  
  print("Students Found: ")
  print(" ")
  
  for row in file:
    if grade in str(row):
      print(row)
      x = x + 1
      
  if x == 0:
    print("Sorry, no student has that grade.")
  file.close()

    

if choice == 1:
  student()
  
elif choice == 2:
  subject()
  
elif choice == 3:
  date()
  
elif choice == 4:
  grade()
  
else:
  print("That was not an option. Please try again.")
