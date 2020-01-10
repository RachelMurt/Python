from random import randint
balls = []

for i in range(6):
    balls.append(randint(1,49))
balls.sort()
print(balls)
