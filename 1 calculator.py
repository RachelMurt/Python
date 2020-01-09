import math

def menu():
    print("=================================================")
    print("Choose a function.")
    print("=================================================")

    print("[1] + Addition")
    print("[2] - Subtraction")
    print("[3] * Multiplication")
    print("[4] / Division")
    print("[5] ^ Exponents")
    print("[6] √ Square Root")
    global function
    function = input("What would you like to do?: ")


menu()


def addition():
    numb1 = float(input("Please enter your first number: "))
    numb2 = float(input("Please enter your second number: "))

    print("The answer is: ", numb1 + numb2)

def subtraction():
    numb1 = float(input("Please enter your first number: "))
    numb2 = float(input("Please enter your second number: "))

    print("The answer is: ", numb1 - numb2)

def multiplication():
    numb1 = float(input("Please enter your first number: "))
    numb2 = float(input("Please enter your second number: "))

    print("The answer is: ", numb1 * numb2)

def division():
    numb1 = float(input("Please enter your first number: "))
    numb2 = float(input("Please enter your second number: "))

    print("The answer is: ", numb1 / numb2)

def exponents():
    numb1 = input("Please enter a number: ")
    power = float(input("What would you like to raise the number to the power of: "))
    print ("The answer is: ", math.pow(numb1, power))

def root():
    numb1 = float(input("Please enter a number: "))
    print("The answer is: ", math.sqrt(numb1))

def error():
    print("That was not an option")
    menu()

if int(function) == 1:
    addition()

elif int(function) == 2:
    division()

elif int(function) == 3:
    multiplication()

elif int(function) == 4:
    division()

elif int(function) == 5:
    exponents()

elif int(function) == 6:
    root()

else:
    error()
