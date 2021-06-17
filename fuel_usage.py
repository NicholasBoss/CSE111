
def miles_per_gallon(ending_odometer, starting_odometer, fuel):
    
    mpg = (ending_odometer - starting_odometer)/ fuel
    return mpg


def lp100k_from_mpg(mpg):

    lp100k = 235.215/mpg
    return lp100k

def main():

    starting_odometer = float(input("What is the starting odometer reading (in miles)? "))
    ending_odometer = float(input("What is the ending odometer reading (in miles)? "))
    fuel = float(input("How many gallons of fuel do you have? "))

    miles_per_gallon(ending_odometer,starting_odometer,fuel)

    mpg = miles_per_gallon(ending_odometer,starting_odometer,fuel)

    lp100k_from_mpg(mpg)

    lp100k = lp100k_from_mpg(mpg)

    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")
    pass

main()