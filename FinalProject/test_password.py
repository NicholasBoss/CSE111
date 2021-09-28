"""
Function Test file for Password.py
"""

import pytest
import os

from password import userinput, intinput, generate_password, saveinput, \
    deletepassword, write_file, rewrite_file, read_file

def test_userinput():
    # response1 = "generate"
    # response2 = "quit"
    # answers = iter([response1, response2])

    # monkeypatch.setattr('builtins.input',lambda name: next(answers))

    assert userinput("Enter 'generate': ") == "generate"
    assert userinput("Enter 'quit': ") == "quit"
    assert userinput("Enter 'view': ") == "view"
    assert userinput("Enter 'save': ") == "save"
    assert userinput("Enter 'yes': ") == "yes"

def test_intinput():
    assert intinput("Enter a number: ") >= 4


def test_generate_password():
    assert len(generate_password(password_length=8)) == 16

def test_saveinput():
    assert saveinput("Enter 'save': ") == "save"
    assert saveinput("Enter 'quit': ") == "quit"
    

def test_delete_password():
    dictionary = {'test': "delete me"}
    specifiedDelete = "test"
    assert deletepassword(dictionary,specifiedDelete) == {}

def test_write_file():
    """Verify that the write_file function works correctly."""
    password = "h8e6Mr5sl"
    filename = "test.txt"
    purpose = "test"
    # Call the write_file function to write a file named test.txt.
    write_file(filename, password, purpose)

    # Read the contents of the test.txt file.
    with open(filename, "rt") as infile:

        # Read all the characters in the file into a string.
        string = infile.read()

    # Split the string into a list of strings named
    # written. Each line of text from the text file
    # will be stored in its own element in the list.
    written = string.split(",")
    
    password_test = written[1]
    
    # Delete the test.txt file.
    os.remove(filename)

    # Verify that write_file correctly wrote the test.txt file.
    assert password == password_test

def test_rewrite_file():
    """Verify that the rewrite_file function works correctly."""
    password = "h8e6Mr5sl"
    filename = "test.txt"
    purpose = "test"
    date = "Tuesday 13 2021"
    # Call the write_file function to write a file named test.txt.
    rewrite_file(filename, date, password, purpose)

    # Read the contents of the test.txt file.
    with open(filename, "rt") as infile:

        # Read all the characters in the file into a string.
        string = infile.read()

    # Split the string into a list of strings named
    # written. Each line of text from the text file
    # will be stored in its own element in the list.
    written = string.split(",")
    
    password_test = written[1]
    
    # Delete the test.txt file.
    os.remove(filename)

    # Verify that write_file correctly wrote the test.txt file.
    assert password == password_test

def test_read_file():
    """Verify that the read_file function works correctly."""
    # Write a sample file with three lines
    filename = "lines.txt"
    line1 = "first"
    line2 = "second"
    line3 = "third"
    with open(filename, "wt") as outfile:
        print(f"{line1},{line2},{line3}", file=outfile)

    # Call read_file to read the sample file.
    read = read_file(filename, 2)
    for row in read:
        key = row

    # Delete the lines.txt file.
    os.remove(filename)

    # Verify that read_file read the file correctly.
    assert key == line3

pytest.main(["-v", "--tb=line", "-rN", "-s", "test_password.py"])