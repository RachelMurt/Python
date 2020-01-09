phrase = "THE QUICK BROWN FOX JUMPED OVER THE MOON"
count = 0
count2 = 0
phrase = phrase.lower()

## check the number of O's and the number of E's in statement

for letter in phrase:
    if letter == "o":
        count = count + 1
    if letter == "e":
        count2 = count2 + 1
print ("There are " + str(count) + " O's in the phrase and " + str(count2) + " e's")

if count == count2:
    print ("the number of O's is the same as the number of e's ")
    if count != count2:
        print ("the numbers are not equal for each letter")
