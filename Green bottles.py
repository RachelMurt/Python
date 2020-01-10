import time
number = 10

while number > 0:
    print(number, "green bottles sitting on the wall.")
    print(number, "green bottles sitting on the wall.")
    print("and if one green bottle would accidentally fall")
    print("there would be", number - 1, "green bottles sitting on the wall")
    print(" ")
    number = number -1
    time.sleep(1)

print("no green bottles sitting on the wall")
