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

# for i in i_number:
#     if i == '-':
#         i_number_new = re.sub("-","",i_number)
        
#     # else: 
#     #     i_number_new = i_number


# print(i_number_new)

# i_number.replace("-", "")

# i_list = list(i_number)
# for i in i_list:
#     if i == "-":
#         i_list.remove(i)
# i_number = ""
# for i in i_list:
#     i_number += i
# print(i_number)


# if i_number in dictionary:
#     name = dictionary[i_number]
#     print(name)
# else:
#     print("No such student.")
    
# print(dictionary)

