#a program calculate how many years until retirement.
print ("*****************************************************")
print ("*************RETIREMENT AGE CALCULATOR***************")
print ("*****************************************************")
name = input("Please enter your name:")
age= input("Please enter your age:")
retireage = input("What age do you intend retiring at: ")

ans = int(retireage) - int(age)
print (name," you are currently ",age," years old.  You wish to retire at ",retireage, " years old.")
print ("It will be ",ans," years until you retire.  Keep taking the Weetabix until then!")

