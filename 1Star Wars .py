# importing CSV for file handling
import csv

file = open("SWMovies.csv","w") #creates the SWMovies file in same directory
newrecord="Episode IV, A New Hope, 1977\n" # creating individual records
file.write(str(newrecord)) # write record to the file
newrecord="Episode V, The Empire Strikes Back, 1981\n"
file.write(str(newrecord))
newrecord="Episode VI, The Return of the Jedi, 1985\n"
file.write(str(newrecord))
newrecord="Episode VII, The Force Awakens, 2015\n"
file.write(str(newrecord))
newrecord="Episode VIII, The Last Jedi, 2017\n"
file.write(str(newrecord))
file.close() # close the file























































#Written by Nichola Lacey and copyright owned by (c) Nichola Wilkin Ltd. 2017
