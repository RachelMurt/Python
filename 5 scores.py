#a program to calculate the total score from various subjects + an average score

#prints the question then asks for an input, will convert the string to an integer
name = input("What is your name? ")
maths = int(input("What score did you achieve in maths? "))
science = int(input("What score did you achieve in science? "))
english = int(input("What score did you achieve in english? "))
ict = int(input("What score did you achieve in ICT? "))

#adds the scores together for a total, also provides an average, assigns them to a variable
total = maths + science + english + ict
average = total / 4

#prints the values on the screen for the user
print (name, "Your total score is:", total)
print ("Your average score is:", average)

if average <= 56:
    print("Your score is below average")
else:
    print("Your score is above average")
