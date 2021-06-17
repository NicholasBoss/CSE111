import csv

def main():
    #indexes for products
    PRODUCT_NUMBER_INDEX = 0
    
    products = read_dict("Week9/products.csv", PRODUCT_NUMBER_INDEX)
    #prints each product on a separate line.
    print("Products:")
    for i in products:
        
    print()
    # Selects and prints each requested item
    request = process_request("Week9/request.csv", PRODUCT_NUMBER_INDEX, products)

def read_dict(filename, key_column_index):
    #Creates an empty dictionary
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2
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
    
def process_request(filename, key_column_index, products):
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
        print("Requested Items: ")
        for i in dictionary:
            product_no = dictionary[i]

            product_info = products[product_no[0]]
            product_name = product_info[1]
            product_price = product_info[2]
            quantity = product_no[1]
        
            print(f"{product_name}: {quantity} @ {product_price} each.")


        
        
    
    
main()