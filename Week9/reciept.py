import csv
from datetime import datetime

#indexes for products
PRODUCT_NUMBER_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

def main():
    while True:
        try:
            products = read_dict("Week9/products.csv", PRODUCT_NUMBER_INDEX)
            print("Inkom Emporium\n")
            # Selects and prints each requested item
            request = process_request("Week9/request.csv", PRODUCT_NUMBER_INDEX, products)
            break
        except FileNotFoundError:
            print("File does not exist. Please find the correct file.")
            break
        except PermissionError:
            print("You do not have permission to view this file.")
            break

def read_dict(filename, key_column_index):
    #Creates an empty dictionary
    while True:
        try:
            dictionary = {}
            #Opens the products.csv file and iterates through each row adding it to the dictionary
            with open(filename, "rt") as csv_file:
                reader = csv.reader(csv_file)

                next(reader)

                for row in reader:

                    key = row[key_column_index]

                    dictionary[key] = [row[PRODUCT_NAME_INDEX], row[PRODUCT_PRICE_INDEX]]
            #returns the full dictionary
            return dictionary
        except KeyError:
            print("Dictionary does not exist.")
            break
    
def process_request(filename, key_column_index, products):
    while True:
        try:
            #Creates an empty dictionary
            dictionary = {}
            #Opens the request.csv file and adds it to the dictionary
            with open(filename, "rt") as csv_file:

                reader = csv.reader(csv_file)

                next(reader)

                for row in reader:
                    
                    key = row[key_column_index]

                    dictionary[key] = row
                #Prints the requested items if they match the products in the products dictionary
                #defining terms for calculation and date
                total_items = 0
                subtotal_price = 0
                current_date_and_time = datetime.now()
                for i in dictionary:
                    product_no = dictionary[i]

                    product_info = products[product_no[0]]
                    product_name = product_info[0]
                    product_price = product_info[1]
                    quantity = product_no[1]

                    total_items += int(quantity)
                    subtotal_price += float(product_price) * int(quantity)
                    sales_tax = subtotal_price * 0.06
                    total_price = subtotal_price + sales_tax
                
                    print(f"{product_name}: {quantity} @ ${product_price} each.")
                print()
                print(f"Number of items: {total_items}")
                print(f"Subtotal: ${subtotal_price}")
                print(f"Sales Tax: ${sales_tax:.2f}")
                print(f"Total: ${total_price:.2f}")
                print()
                print("Thank you for shopping at Inkom Emporium!")
                print(f"{current_date_and_time:%A %I:%M %p %Y}")
                break
        except KeyError:
            print("Dictionary does not exist.")
            break
 
main()