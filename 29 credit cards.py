numb1 = input("Please input your credit card number: ")
numbList = list(numb1)

i = 0
while i < 16:
    print(numbList[i])
    i = i+1

print("Credit card number: ************" + (numbList[12]) + (numbList[13]) + (numbList[14]) + (numbList[15]))
