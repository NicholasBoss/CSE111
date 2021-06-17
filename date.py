from datetime import datetime
from random import randint
today = str(datetime.now())

date_strip = today.strip()
date = date_strip.split(' ')

#date = today.strptime(date_string, format)
print(today)
print(date[0])


name = input("What is your name? ")

print(f"Hello {name.title()}")

value = 0
def randinteger():
    for i in range(1):
        value = randint(0,1000)
    return value

value = randinteger()

print(value)
