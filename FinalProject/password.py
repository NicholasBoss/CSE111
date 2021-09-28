"""
Password Generator and Manager

"""

import os
import random
import csv
import string
from datetime import datetime
from time import sleep


DATE_INDEX = 0
PASSWORD_INDEX = 1
PURPOSE_INDEX = 2
def main():
    start = True
    print("Welcome to the Password Generator and Manager.")
    while start == True:
        print()
        # Asking user to choose which part of the manager they want to use
        choice = userinput("Would you like to generate a password or view your existing passwords?\n"
                        "(Enter Generate or View to continue. Enter 'Quit' to exit program).\n")
        print()
        if choice == "generate":
            #ask user to enter password length
            password_length =intinput("How long do you want your password to be?\n"
                                    "The length will double the password.\n"
                                    "Ex. You enter 8, the length will be 16.\n")
            print("Generating password...")
            sleep(3)
            pregen_password = generate_password(password_length)
            #A saveinput function to run for each time the user wants to save the password.
            sleep(3)
            print()
            new_choice = saveinput("Would you like to save this password or generate a new one?\n"
                    "(Enter 'Save' or 'Generate' to continue. Enter 'Quit' to exit program.\n"
                    "Warning: Exiting without saving the password will cause generated password to be lost.\n")
            
            if new_choice == 'generate':
                #asking the user to enter how long their password will be if they want to generate a new password
                print()
                password_length =intinput("How long do you want your password to be?\n"
                                        "The length will double the password.\n"
                                        "Ex. You enter 8, the length will be 16.\n")
                print("Generating password...") 
                sleep(3)
                pregen_password = generate_password(password_length)
                sleep(3)
                print()
                new_choice1 = saveinput("Would you like to save this password or generate a new one?\n"
                    "(Enter 'Save' or 'Generate' to continue. Enter 'Quit' to exit program.\n"
                    "Warning: Exiting without saving the password will cause generated password to be lost.\n")
                if new_choice1 == "save":
                    #if user chose to save the password, they are asked to enter the 'use' or purpose for the password
                    print()
                    purpose = input("What is this password going to be used for? \n")
                    write_file("password_database.csv", pregen_password, purpose)
                    #Asking the user if they want to see their saved passwords.
                    print()
                    view = userinput("Do you want to view your saved passwords?\n"
                        "Enter 'View' to continue. Enter 'Quit' to exit the program.\n")
                    if view == "view":
                        #If they chose to view, then the passwords will be printed.
                        read_file("password_database.csv", PURPOSE_INDEX)
                        dictionary= read_file("password_database.csv", PURPOSE_INDEX)
                        print()
                        for row, value in dictionary.items():
                            print(f"{row}: {value}")
                    elif view == "quit":
                        print("Deleting generated password.")
                        sleep(3)
                        print("Goodbye.")
                        start == False
                        break
                elif new_choice1 == "quit":
                    print("Goodbye.")
                    start == False
                    break
            elif new_choice == 'save':
                #if user chose to save the password, they are asked to enter the 'use' or purpose for the password
                print()
                purpose = input("What is this password going to be used for? \n")
                write_file("password_database.csv", pregen_password, purpose)
                #Asking the user if they want to see their saved passwords.
                print()
                view = userinput("Do you want to view your saved passwords?\n"
                        "Enter 'View' to continue. Enter 'Quit' to exit the program.\n")
                if view == "view":
                    #If they chose to view, then the passwords will be printed.
                    read_file("password_database.csv", PURPOSE_INDEX)
                    dictionary= read_file("password_database.csv", PURPOSE_INDEX)
                    print()
                    for row, value in dictionary.items():
                        print(f"{row}: {value}")
            elif new_choice == "quit":
                print("Deleting generated password.")
                sleep(3)
                print("Goodbye.")
                start == False
                break
        elif choice == "view":
            #if the user wants to view the passwords they have
            print("Grabbing database of passwords.")
            try:
                #reads the password_database file
                read_file("password_database.csv", PURPOSE_INDEX)
                #returns the passwords as a dictionary
                dictionary = read_file("password_database.csv", PURPOSE_INDEX)
                print()
                #prints the passwords in this specified format
                for row, value in dictionary.items():
                    print(f"{row}: {value}")
                #Asking the user if they want to delete a password
                print()
                deletechoice = userinput("Do you want to delete a password, or the whole database?\n"
                                        "(Enter 'single' to delete one password. \n"
                                        "Enter 'full' to delete the whole database.\n"
                                        "Enter 'Quit' to exit program)\n")
                if deletechoice == "single":
                    #This allows the user to delete a specific password based on its purpose.
                    print()
                    specifiedDelete = input("Which password do you want to delete?\n"
                                            "Enter the purpose of the password you want to delete:\n")
                    #The password file is read, turned into a dictionary and the specific password is deleted.
                    new_dictionary = deletepassword(dictionary, specifiedDelete)
                    #replaces password_database.csv file with the new dictionary.
                    print("Changes successful.")
                    sleep(2)
                    os.remove("password_database.csv")
                    for row,value in new_dictionary.items():
                        new_purpose = row
                        new_values = value.split(",")
                        password = new_values[0]
                        date = new_values[1]
                        rewrite_file("password_database.csv",date,password,new_purpose)
                    print("Here are the remaining passwords:\n")
                    #reads the password_database file
                    read_file("password_database.csv", PURPOSE_INDEX)
                    #returns the passwords as a dictionary
                    dictionary = read_file("password_database.csv", PURPOSE_INDEX)
                    print()
                    #prints the passwords in this specified format
                    for row, value in dictionary.items():
                        print(f"{row}: {value}")
                elif deletechoice == 'full':
                    ultimate_choice = userinput("Are you sure? \n"
                                                "(Enter 'yes' to continue.\n"
                                                "Enter 'quit' to exit program).\n")
                    if ultimate_choice == "yes":
                        os.remove("password_database.csv")
                        print("Database deleted.")
                    elif ultimate_choice == "quit":
                        print("Goodbye.")
                        start == False
                        break
                    else:
                        print("Please enter a valid choice.")
                elif deletechoice == "quit":
                    print("Goodbye.")
                    start == False
                    break
            #handles the errors if the file is not found or it is empty.
            except FileNotFoundError:
                print(f"Error: File does not exist, has not been created, "
                    "or has just been deleted.\n"
                    "Please generate and save a password to view this file")
            except StopIteration:
                print(f"Error: File is empty.")
        elif choice == "quit":
            print("Goodbye.")
            start == False
            break


def userinput(msg):
    """
    Takes the user's input and checks to see if it matches
    the choices given. If not, it will continue prompting 
    the user until they type 'quit' or one of the other options.
    """
    while True:
        try:
            choice = input(msg)
            if choice.lower() == "generate":
                return choice.lower()
            elif choice.lower() == "view":
                return choice.lower()
            elif choice.lower() == "save":
                return choice.lower()
            elif choice.lower() == "yes":
                return choice.lower()
            elif choice.lower() == "single":
                return choice.lower()
            elif choice.lower() == "full":
                return choice.lower()
            elif choice.lower() == "quit":
                return choice.lower()
            else:
                print("Please enter a valid input.\n")
        except ValueError as val_err:
            print(f"Error: {val_err}")

def intinput(msg):
    """
    Checks to see if the password length will allow for a secure password.
    """
    while True:
        try:
            choice = int(input(msg))
            if choice >= 4:
                return choice
            else:
                print("That password will not be secure.\n"
                      "Please enter a bigger number\n"
                      "so your password will be secure.\n")
        except ValueError:
            print(f"Error: Please enter an Integer.")
        except IndexError:
            print(f"Error: please enter an Integer.")


def generate_password(password_length):
    """
    Generates a password according to the length
    of the password, given by the user, multiplied by 2. 
    """
    pass_len = password_length 
    alphabet_string_lower = string.ascii_lowercase
    alphabet_string_upper = string.ascii_uppercase
    letters_list = list(alphabet_string_lower) + list(alphabet_string_upper)
    numbers_list = []
    pregen_password = []
    for i in range(10):
        numbers_list.append(0 + i)
    
    for i in range(pass_len):
        letter = random.choice(letters_list)
        number = str(random.choice(numbers_list))
        pregen_password.append(letter + number)
    print("Here is your secure password:")
    
    #joins the list into one string
    listToString = ''.join(map(str, pregen_password))

    print(listToString)
    return listToString

def saveinput(new_choice):
    """
    saves the password to the csv file 
    or prompts the user for a new password length.
    """
    while True:
        try:
            choice = input(new_choice)
            if choice.lower() == "save":
                return choice.lower()
            elif choice.lower() == "generate":
                return choice.lower()
            elif choice.lower() == "quit":
                return choice.lower()
            else:
                print("Please enter a valid input.")
        except ValueError:
            print("error")

def deletepassword(dictionary, specifiedDelete):
    """
    Deletes a password based on its purpose.
    """
    new_dict = dictionary
    for row in new_dict:
        if row == specifiedDelete:
            del new_dict[specifiedDelete]
            print("Delete successful.")
            sleep(4)
            return new_dict
            
    return new_dict


def write_file(filename, pregen_password, purpose):
    """
    appends the date, the currently created password, and the purpose
    to the csv file.
    """
    current_date_and_time = datetime.now()
    with open(filename, "at") as pass_file:
        print(f"{current_date_and_time:%A %I:%M %p %Y},{pregen_password},{purpose}", file = pass_file)
        print("save successful.")

def rewrite_file(filename,date,password,new_purpose):
    """
    This function will overwrite the csv file when the user deletes a password.
    """
    with open(filename, "at") as new_pass_file:
        print(f"{date},{password},{new_purpose}", file = new_pass_file)
    


def read_file(filename, key_column_index):
    """
    Reads the csv file and returns the information
    in a dictionary.
    """
    dictionary = {}
    with open(filename, "rt") as pass_file:
        reader = csv.reader(pass_file)

        for row in reader:
            key = row[key_column_index]

            dictionary[key] = row[PASSWORD_INDEX] + ',' + row[DATE_INDEX]
        
    return dictionary
main()