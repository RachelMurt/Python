import csv

filename = "SWMovies.csv"
file = open(filename, "r")
for line in file:
    print(line)
