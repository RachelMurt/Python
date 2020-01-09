import time
number = input("Please choose a number: ")
print(" ")

times = 1

while times < 13:
    print(number, " x ", times, "=", int(number) * int(times))
    times = times + 1
    time.sleep(0.2)

print(" ")
print("Learn your", number, "times tables!")
print("======================================================")
print(" ")

number2 = input("Please choose another number: ")
print(" ")

times2 = 1

while times2 < 13:
    print(number2, " x ", times2, "=", int(number2) * int(times2))
    times2 = times2 + 1
    time.sleep(0.2)

print(" ")
print("Now learn your", number2, "times tables!")

