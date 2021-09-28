# calculate circle area based on user input with multiple circles
from math import expm1, pi as p

# def main():
#     radius = 999999999999
#     radius_list = []
#     while radius != 0:
#         radius = float(input("What is the radius (enter '0' to quit)? "))
#         radius_list.append(radius)

#     radius_list.pop()
#     for i in radius_list:
#         radius = i

#         print(f"Area: {caclulate_circle_area(radius):.2f}")

# def caclulate_circle_area(radius):
#     area_of_circle = p * radius**2
#     return area_of_circle
# main()
import math
def main():
    ## prompt user for how many cirlces they have
    numberOfCircles = integerInput("How many circles are we working with? ")
    areasList = loopForCircles(numberOfCircles)
    displayAreas(areasList)
   

def displayAreas(areasList):
    areasList = [round(i,2) for i in areasList]
    print(areasList)

def integerInput(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print("Please, please...enter a number. :)")
    

def loopForCircles(numberOfCircles):
    circleAreas = []
    ##loop x times: compute area for each circle
    while True:
        try:
            for _ in range(numberOfCircles):
                ## get radius for each circle
                r = integerInput("Please enter the radius: ")
                circleAreas.append(computeCircleArea(r))
            break
        except ValueError:
            print("You have entered a wrong number. Please try again.")
            pass
    return circleAreas
    

def computeCircleArea(r): # compute and return circle area
    return math.pi * r**2

if __name__ == '__main__':
    main()
