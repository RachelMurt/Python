def longName():
    print("Your name is quite long! \n"
          "How old are you? \n")
    age = int(input("Age: "))
    if age == 17:
              print("That's the same as me!")
    else:
              print("We're not the same age!")
              
def shortName():
    print("Your name is kind of short! \n"
          "Are you also short?")
    height = str(input(""))
    if height == 'yes':
        print("I knew it!")
    else:
        print("That's weird!")
              


name = input ("What is your name?: ")

if len(name) >= 7:
    longName()
elif len(name) < 7:
    shortName()
else:
    print ("this shouldn't happen.")

