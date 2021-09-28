import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    # store pupils.csv list in a new variable
    students_list = read_compound_list("pupils.csv")
    print("Sorted by Birthdate.")
    sorted_students_list_1 = sorted(students_list, key = lambda student: student[BIRTHDATE_INDEX], reverse= True)
    #prints list
    print_list(sorted_students_list_1)
    print()
    print("Sorted by given name")
    sorted_students_list_2 = sorted(students_list, key = lambda student: student[GIVEN_NAME_INDEX], reverse= False)
    #prints list
    print_list(sorted_students_list_2)
    print()
    print("Sorted by birth month and day.")
    #sort student list
    sorted_students_list_3 = sorted(students_list, key = lambda student: student[BIRTHDATE_INDEX][5:9], reverse= False)
    #prints list
    print_list(sorted_students_list_3)
    

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(students_list):
    for i in students_list:
        print(i)

main()