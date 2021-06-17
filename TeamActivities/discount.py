"""
Team 1B Activity # 1

discount.py
"""

# Core Objectives:
#Find device's date and time.
#Take a customer's subtotal
#If subtotal is greater than $50, and it is Tuesday or Wednesday, discount = 10% of subtotal.
#Add 6% sales tax to subtotal
#Print discount, sales tax and total amount.

from datetime import datetime

today = datetime.now()
weekday = today.isoweekday()
weekday = 2

# print(today)
# print(weekday)
discount = 0
subtotal = 0
price = ''

while price.lower() != 'done':
    price = input("Please enter the price (Type 'done' when finished): ")
            
    if price.lower() != 'done':
        quantity = int(input("Please enter a quantity: "))

        subtotal += float(price) * quantity
        print("Price updated.\n")
        print(f"Your subtotal is: ${subtotal:.2f}\n")

# Is discount available?   
if weekday in (2,3):

    if subtotal >= 50:
        discount = subtotal * 0.1
        print(f"Discount amount: ${discount:.2f}")

    else:
        difference = 50 - subtotal
        print(f"If you spend ${difference:.2f} more, you can receive a 10% discount.")


#Calculating final total
discounted_total = subtotal - discount

sales_tax = discounted_total * 0.06

total = discounted_total + sales_tax


print(f"Sales tax amount: ${sales_tax:.2f}\n")
print(f"Total: ${total:.2f}\n")