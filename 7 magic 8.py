# Magic 8 ball

import random
import time

#answers
ans = []
ans.append ("Go for it!")
ans.append ("No way!")
ans.append ("I'm not sure. Ask me again.")
ans.append ("Fear of the unknown is what imprisons us.")
ans.append ("It would be madness to do that!")
ans.append ("Only you can save mankind!")
ans.append ("Makes no difference to me, do or don't - whatever.")
ans.append ("Yes, I think that is the right choice.")

print("Welcome to the Magic 8 Ball!")

#get the user's question
question = input("Ask me for advice, then press ENTER to shake me! \n")

print("shaking.....\n")
time.sleep(1)


#shows a random result from the list
result = ""
for i in range(0,1):
    result += random.choice(ans) + " "
    
print(result)
