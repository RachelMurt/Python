#code for calculating the area of a room
#imports the time component
import time

#prints the questions for user input
print ("Calculating the area of a room")
length = int(input("What is the length of the room in metres? "))
width = int(input("What is the width of the room in metres? "))

#calulates the area
area = length * width

#waits for a second before printing the answer
print("Calculating the area...")
time.sleep(1)

print("The area of the room is:", area,"metres squared")

