import csv

I_NUMBER_INDEX = 0
NAME_INDEX = 1
dictionary ={}
with open("Week9/TeamActivity/students.csv", "rt") as csv_file:

    reader = csv.reader(csv_file)

    next(reader)

    for row in reader:
        key = row[I_NUMBER_INDEX]

        dictionary[key] = row[NAME_INDEX]

print(dictionary)