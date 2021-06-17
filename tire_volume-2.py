"""
File: tire_volume.py
Author: Nicholas Boss

Purpose: To calculate the volume of a tire
"""
#Importing libraries
import math
from time import sleep
from datetime import datetime
from random import randint

def volume_calc(width, aspect_ratio, diameter):
    print()
    print("One moment...")
    sleep(1)
    print("Inserting values...\n")
    sleep(2)

    #Simulating machine calculation
    sleep(2)
    print("Values inserted\n")
    sleep(0.5)
    for i in range(3, 0 , -1):
        print("Calculating...")
        sleep(1.5)
    #Calculating the volume of the tire
    volume = (math.pi * (width**2) * aspect_ratio*(width*aspect_ratio+2540*diameter))/10000000
    return volume

#Preset variables
width = 0
aspect_ratio = 0
diameter = 0
model = ''
value = 0
def randinteger():
    for i in range(1):
        value = randint(0,1000)
        return value


def userinput():
    choice = input("Which would you like to find the volume for (tire, cube, sphere)? "
                   "(Type 'quit' to leave) ")
    return choice


#Calculation of today's date
print("Welcome to the volume calculator!\n")
today = datetime.now()
today_str = str(datetime.now())
date_strip = today_str.strip()
date = date_strip.split(' ')
if today.month == 1:
    current_month = 'January'

elif today.month == 2:
    current_month = 'Feburary'

elif today.month == 3:
    current_month = 'March'

elif today.month == 4:
    current_month = 'April'

elif today.month == 5:
    current_month = 'May'

elif today.month == 6:
    current_month = 'June'

elif today.month == 7:
    current_month = 'July'

elif today.month == 8:
    current_month = 'August'

elif today.month == 9:
    current_month = 'September'

elif today.month == 10:
    current_month = 'October'

elif today.month == 11:
    current_month = 'November'

elif today.month == 12:
    current_month = 'December'

#Asking the user for data values
print(f"Today is the {today.day} of {current_month}, {today.year}.")
name = input("What is your name? ")
print(f"Welcome {name.title()},\n")
choice = ''
while choice.lower() != 'quit':

    choice = userinput()

    if choice.lower() == 'tire':
        selection = int(input("Do you want to see our selection of tires (1) or enter values"
                          " to find a specific tire (2)? "))

        if selection == 2:
            width = float(input("Please enter the width of the tire in mm (ex 205): "))
            aspect_ratio = float(input("Please enter the aspect ratio of the tire (ex 60): "))
            diameter = float(input("Please enter the diameter of the wheel in inches (ex 15): "))
            #If the entered values maatch then they will be referred to this brand
            if width == 205 and aspect_ratio == 60 and diameter == 15:
                print("These dimensions are similar to a brand of tire we have in stock.")
                print(f"The dimensions of your current tire are: {width}, {aspect_ratio}, and {diameter}.")
                print("These dimensions are that of the 'Kelly Edge A/S' model.\n"
                      "The current asking price per tire is $81.00. For a set it is $324.00.")

                buy = input("Would you like to buy this tire (Yes or No)? ")

                if buy.lower() == 'yes':

                    volume = volume_calc(width, aspect_ratio, diameter)
                    #Printing out the result of the calculation
                    print(f"The approximate volume of a single tire is {volume:.1f} cubic cm.")
                    
                    price_select = int(input("Do you want a single tire (1) or a set of tires (2)? "))

                    if price_select == 1:
                        price = 81
                        
                    elif price_select == 2:
                        price = 324
                    model = 'Kelly Edge A/S'
                    phone = input("Please enter your phone number to confirm your purchase: \n")

                elif buy.lower() == 'no':
                    print("We are sorry for your decision, please come again soon.")
                    
            #If the entered values maatch then they will be referred to this brand
            elif width == 185 and aspect_ratio == 55 and diameter == 15:
                print("These dimensions are similar to a brand of tire we have in stock.")
                print(f"The dimensions of your current tire are: {width}, {aspect_ratio}, and {diameter}.")
                print("These dimensions are that of the 'Goodyear Integrity' model.\n"
                      "The current asking price per tire is $103.00. For a set it is $412.00.")

                buy = input("Do you want to buy this tire (Yes or No)? ")

                if buy.lower() == 'yes':
                    volume = volume_calc(width, aspect_ratio, diameter)
                    print(f"The approximate volume of a single tire is {volume:.1f} cubic cm.")

                    price_select = int(input("Do you want a single tire (1) or a set of tires (2)? "))

                    if price_select == 1:
                        price = 103
                        
                    elif price_select == 2:
                        price = 412
                    model = 'Goodyear Integrity'
                    phone = input("Please enter your phone number to confirm your purchase: \n")

                elif buy.lower() == 'no':
                    print("We are sorry for your decision, please come again soon.")
                    
            #If the entered values maatch then they will be referred to this brand
            elif width == 185 and aspect_ratio == 55 and diameter == 15:
                print("These dimensions are similar to a brand of tire we have in stock.")
                print(f"The dimensions of your current tire are: {width}, {aspect_ratio}, and {diameter}.")
                print("These dimensions are that of the 'Goodyear Integrity' model.\n"
                      "The current asking price per tire is $103.00. For a set it is $412.00.")

                buy = input("Do you want to buy this tire (Yes or No)? ")

                if buy.lower() == 'yes':
                    volume = volume_calc(width, aspect_ratio, diameter)
                    print(f"The approximate volume of a single tire is {volume:.1f} cubic cm.")

                    price_select = int(input("Do you want a single tire (1) or a set of tires (2)? "))

                    if price_select == 1:
                        price = 103
                        
                    elif price_select == 2:
                        price = 412
                    model = 'Goodyear Wrangler MT/R with Kevlar'
                    phone = input("Please enter your phone number to confirm your purchase: \n")

                elif buy.lower() == 'no':
                    print("We are sorry for your decision, please come again soon.")
                    
            #If the entered values maatch then they will be referred to this brand
            elif width == 40 and aspect_ratio == 13.5 and diameter == 17:
                print("These dimensions are similar to a brand of tire we have in stock.")
                print(f"The dimensions of your current tire are: {width}, {aspect_ratio}, and {diameter}.")
                print("These dimensions are that of the 'Goodyear Wrangler TrailRunner AT' model.\n"
                      "The current asking price per tire is $582.00. For a set it is $2,328.00.")

                buy = input("Do you want to buy this tire (Yes or No)? ")

                if buy.lower() == 'yes':
                    volume = volume_calc(width, aspect_ratio, diameter)
                    print(f"The approximate volume of a single tire is {volume:.1f} cubic cm.")

                    price_select = int(input("Do you want a single tire (1) or a set of tires (2)? "))

                    if price_select == 1:
                        price = 582
                        
                    elif price_select == 2:
                        price = 2328
                    model = 'Goodyear Wrangler TrailRunner AT'
                    phone = input("Please enter your phone number to confirm your purchase: \n")

                elif buy.lower() == 'no':
                    print("We are sorry for your decision, please come again soon.")
                    
            #If values entered do not match, they will get a random price for the tires from the company 'Questionable Tiers'
            else:
                value = randinteger()
                print(f"The price for the dimensions you entered is ${value:.2f}")

                buy = input("Would you like to buy a set of these tires (Yes or No)? ")

                if buy.lower() == 'yes':
                    volume = volume_calc(width, aspect_ratio, diameter)
                    print(f"The approximate volume of a single tire is {volume:.1f} cubic cm.")
                    phone = input("Please enter your phone number to complete the purchase: ")
                    model = 'Questionable Tiers'
                    price = value

        #Providing pre programmed brands to the user
        elif selection == 1:
            print("Our selection of tires is as follows:")
            print("(1) The 'Kelly Edge A/S'")
            print("(2) The 'Goodyear Integrity'")
            print("(3) The 'Goodyear Wrangler MT/R with Kevlar'")
            print("(4) The 'Goodyear Wrangler TrailRunner AT'")
            print()

            brand_choice = int(input("Which set of tires do you want to learn more about? "))
            #Brand options
            if brand_choice == 1:
                print("The measurements of the 'Kelly Edge A/S' tire are: ")
                print("Width: 205, Aspect Ratio: 60, Diameter: 15")
                print("Price per tire: $81.00")
                print("Price for a set of four: $324.00")

                select_price = int(input("Do you want a single tire (1) or a set of tires (2)? "))

                if select_price == 1:
                    price = 81
                elif select_price == 2:
                    price = 324
                width = 205
                aspect_ratio = 60
                diameter = 15
                volume = (math.pi * (width**2) * aspect_ratio*(width*aspect_ratio+2540*diameter))/10000000
                model = 'Kelly Edge A/S'
                print(f"The volume of your tire is {volume:.1f} cubic meters.")
                phone = input("Please enter your phone number to confirm purchase: \n")

            elif brand_choice == 2:
                print("The measurements of the 'Goodyear Integrity' are:")
                print("Width: 185, Aspect Ratio: 55, Diameter: 15")
                print("Price per tire: $103.00")
                print("Price for a set of four: $412.00")

                select_price = int(input("Do you want a single tire (1) or a set of tires (2)? "))
                
                if select_price == 1:
                    price = 103
                elif select_price == 2:
                    price = 412
                width = 185
                aspect_ratio = 55
                diameter = 15
                volume = (math.pi * (width**2) * aspect_ratio*(width*aspect_ratio+2540*diameter))/10000000
                model = 'Goodyear Integrity'
                phone = input("Please enter your phone number to confirm purchase: \n")
                
            elif brand_choice == 3:
                print("The measurements of the 'Goodyear Wrangler MT/R with Kevlar' are:")
                print("Width: 40, Aspect Ratio: 13.5, Diameter: 17")
                print("Price per tire: $582.00")
                print("Price for a set of four: $2,328.00")

                select_price = int(input("Do you want a single tire (1) or a set of tires (2)? "))

                if select_price == 1:
                    price = 582
                elif select_price == 2:
                    price = 2328
                width = 40
                aspect_ratio = 13.5
                diameter = 17
                volume = (math.pi * (width**2) * aspect_ratio*(width*aspect_ratio+2540*diameter))/10000000
                model = 'Goodyear Wrangler Mt/R with Kevlar'
                phone = input("Please enter your phone number to confirm purchase: \n")
            
            elif brand_choice == 4:
                print("The measurements of the 'Goodyear Wrangler TrailRunner AT' are:")
                print("Width: 215, Aspect Ratio: 85, Diameter: 16")
                print("Price per tire: $201.00")
                print("Price for a set of four: $804.00")

                select_price = int(input("Do you want a single tire (1) or a set of tires (2)? "))

                if select_price == 1:
                    price = 201
                elif select_price == 2:
                    price = 804
                width = 215
                aspect_ratio = 85
                diameter = 16
                volume = (math.pi * (width**2) * aspect_ratio*(width*aspect_ratio+2540*diameter))/10000000
                model = 'Goodyear Wrangler TrailRunner AT (Light Truck)'
                phone = input("Please enter your phone number to confirm purchase: \n")

            #Appending the information into the volume file.
            with open("volume.txt", "at") as volume_file:
                print(f"{date[0]}, {width}, {aspect_ratio}, {diameter}, {volume:.1f}, {phone}, ${price:.2f}, {model}, {name.title()}", file=volume_file)
            print(f"Thank you for your purchase {name.title()}!")

    #Other volume calculators:
    elif choice.lower() == 'cube':
        edge = input("What is the length of the side of the cube in cm? ")
        print("Value recieved.")
        sleep(3)
        
        #simulating machine calculation
        edge = int(edge)
        print("Value converted.")
        sleep(2)

        print("Inserting value.")
        vol_cube = edge**3
        sleep(2)
        print("Calculating...")
        sleep(1)

        #Output of the equation
        print(f"The volume of your cube is {vol_cube} cubic cm.")

    elif choice.lower() == 'sphere':
        choice2 = input("Do you want to enter a radius or a diameter? ")

        if choice2.lower() == 'radius':
            radius = int(input("What is the radius of the sphere in cm? "))

            #Simulating machine processing
            print("Radius recieved.")
            sleep(2)
            print("Inserting value.")
            sleep(1)

            vol_sphere = (4/3)*math.pi*(radius)**3
            print("Calculating...")
            sleep(2)

            print(f"The volume of your sphere is approximately {vol_sphere:.3f} cubic cm.")
        
        elif choice2.lower() == 'diameter':
            diameter = int(input("What is the diameter of the sphere in cm? "))
            print("Diameter recieved.")
            sleep(2)

            print("Converting to radius.")
            radius = diameter/2
            sleep(3)
            print("Converted")
            sleep(2)

            print("Inserting value into equation.")
            sleep(2)
            vol_sphere = (4/3)*math.pi*(radius)**3
            print("Calculating...")
            sleep(2)

            print(f"The volume of your sphere is approximately {vol_sphere:.3f} cubic cm.")
print("Shutting down!")
sleep(2)
for i in range(5, 0, -1):
    print(i)
    sleep(1)