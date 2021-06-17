"""
File: lifeexpectancy.py
Author: Nicholas Boss

Purpose: to analyze data in a file
"""

line_count = 0
#values for Data set calculation
big_life = 0
small_life = 999999999
big_year = 0
small_year = 0
big_entity = ""
small_entity = ""
life_expectancy_sum = 0
#values for the specified year calculation
big_life_search = 0
small_life_search = 999999999
big_year_search = 0
small_year_search = 0
big_entity_search = ""
small_entity_search = ""

smallest_year = 9999999999
greatest_year = 0
#lists
avle = []
countries = []

# Finding the life expectancy of the data file as a whole
with open("life-expectancy.csv") as life_file:

    for line in life_file:
        if line_count != 0:
            line = line.strip()
            # print(line)
            columns = line.split(",")
            # print(columns)
            entity = columns[0]
            code = columns[1]
            year = int(columns[2])
            life_expectancy = float(columns[3])
            
            #largest of Data Set

            if life_expectancy > big_life:
                big_life = life_expectancy
                big_year = year
                big_entity = entity
                
            #smallest of Data set
                
            if life_expectancy < small_life and life_expectancy > 0:
                small_life = life_expectancy
                small_year = year
                small_entity = entity
            
            if year < smallest_year:
                smallest_year = year
                
            if year > greatest_year:
                greatest_year = year

        line_count += 1
    print("The biggest and smallest values from the Data Set are: ")
    print(f"The maximum life expectancy is {big_life:.2f} years in {big_entity} from the year {big_year}.")
    print(f"The smallest life expectancy is {small_life:.2f} years in {small_entity} from the year {small_year}.")
    print(f"The furthest year back of the set is {smallest_year}")
    print(f"The most recent year of the set is {greatest_year}")

    print()

# Finding the average of the user input year
with open("life-expectancy.csv") as newlife_file:
        year_search = (input("What year do you want to explore? "))

        for line in newlife_file:
            line = line.strip()
            columns1 = line.split(",")
            country1 = columns1[0]
            year = columns1[2]
            life_exp = columns1[3]
            
            if year_search in line:
                avle.append(life_exp)
                if country1 != line:
                    countries.append(country1)
                

        total_lifeex = 0
        for lifeex in avle:
            lifeex = float(lifeex)
            total_lifeex += lifeex

        average_life_year = total_lifeex / len(avle)

        location = 0
        for i in range(len(countries)):
            location += 1
            place = countries[i]
            print(f"{location}) {place}")

        integer = avle.index(min(avle))
        maxint = avle.index(max(avle))
        
        
        print(f"The lowest life expectancy of {countries[integer]} in {year_search} is {float(avle[integer]):.2f} years.")
        print(f"The highest life expectancy of {countries[maxint]} in {year_search} is {float(avle[maxint]):.2f} years.")
        print(f"The average life expectancy of {year_search} is {average_life_year:.2f} years.")

    
print()

# Finding the average life expectancy of a country 
with open("life-expectancy.csv") as newlife_file:
    country_search = input("What country do you want to see? ")
    new_countries = []
    life_expectancies = []
    for line in newlife_file:
        new_line = line.split(",")
        
        if country_search.capitalize() in new_line:
            country_search = new_line[0]
            life_expect = new_line[3]
            new_countries.append(country_search)
            life_expectancies.append(life_expect)
        
            
    total_life = 0
    for life in life_expectancies:
        life = float(life)
        total_life += life

    average = total_life / len(life_expectancies)
    
    for i in range(len(new_countries)):
        
        place = new_countries[i]
        

    print(f"The average years of life in {place} is {average:.2f} years.")
    print()
