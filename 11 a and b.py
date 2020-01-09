a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if a > b:
    a = a + b
    b = a - b
    a = a - b

    print("Always done")
