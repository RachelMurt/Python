import csv # using the csv library

filename = "SWmovies.csv" #open the CVS file
file = open(filename, "r") # "r" indicates READ
for line in file: # using iteration to loop through the file
   print (line) # prints the contents of the file
    
