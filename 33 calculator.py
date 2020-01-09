import math

numb1 = float(input("Please enter a number: "))
operation = input("What do you want to do with the numbers? Choose from: /n +, -, *, / or sq: ")
if operation == 'sq':
    square = float(input("What would you like to square your first number by?: "))
    print (math.pow(numb1, square))
else:
    numb2 = input("Please enter another number: ")


if operation == '+':
    print (float(numb1) + float(numb2))
elif operation == '-':
    print(float(numb1) - float(numb2))
elif operation == '*':
    print(float(numb1) * float(numb2))
elif operation == '/':
    print(float(numb1) / float(numb2))
elif operation == 'sq':
    print(" ")
else:
    print("That was not one of the options")
    
