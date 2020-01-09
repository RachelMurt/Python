def spring():
   weather1 = input("Name a weather feature of spring: ")
   weather2 = input("Name another weather feature of spring: ")
   month = input("Name a month in spring: ")

def summer():
   weather1 = input("Name a weather feature of summer: ")
   weather2 = input("Name another weather feature of summer: ")
   month = input("Name a month in summer: ")

def autumn():
   weather1 = input("Name a weather feature of autumn: ")
   weather2 = input("Name another weather feature of autumn: ")
   month = input("Name a month in autumn: ")

def winter():
   weather1 = input("Name a weather feature of winter: ")
   weather2 = input("Name another weather feature of winter: ")
   month = input("Name a month in winter: ")

fave = input("What is your favourite season? ")

if fave == 'spring':
    spring()
elif fave == 'summer':
    summer()
elif fave == 'autumn':
    autumn()
elif fave == 'winter':
    winter()
else:
    print ("That's not a season!")
