import csv
import re
I_NUMBER_INDEX = 0
NAME_INDEX = 1
LETTER_INDEX = 2
dictionary ={}
with open("Week9/TeamActivity/students.csv", "rt") as csv_file:

    reader = csv.reader(csv_file)

    next(reader)

    for row in reader:
        key = row[I_NUMBER_INDEX]

        dictionary[key] = row[NAME_INDEX]


i_number = input("Please enter an I-Number (xxxxxxxxx): ")

for i in i_number:
    if i == '-':
        i_number= i_number.replace("-","")
        
if i_number in dictionary:
    name = dictionary[i_number]
    print(name)
else:
    print("No such student.")
    


