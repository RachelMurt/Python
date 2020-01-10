import csv

file = open("SWMovies.csv", "w")
newrecord ="Episode IV, A New Hope, 1977\n"
file.write(str(newrecord))
newrecord ="Episode V, The Empire Strikes Back, 1981\n"
file.write(str(newrecord))
newrecord ="Episode VI, Thre Return of the Jedi, 1985\n"
file.write(str(newrecord))
newrecord ="Episode VII, The Force Awakens, 2015\n"
file.write(str(newrecord))
newrecord ="Episode VIII, the Last Jedi, 2017\n"
file.write(str(newrecord))
file.close()
