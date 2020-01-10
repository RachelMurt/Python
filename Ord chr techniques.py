name=input("What is your name?")
if ord(name[0])>96:
       name=chr(ord(name[0])-32) + name[1:]
       print("Did you mean " + name + "?")
       else:
           print("Hello " + name + ",it's nice to meet you!")
           
       
