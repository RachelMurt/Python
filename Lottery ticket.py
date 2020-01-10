from random import randint
numb = []

for i in range(6):
    numb.append(randint(1,59))
numb.sort()
print("Your numbers are:")
print(numb)
