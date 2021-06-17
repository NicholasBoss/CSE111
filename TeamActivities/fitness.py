"""
Team 1B Activity # 2

fitness.py
"""

from datetime import datetime
from time import sleep

def main():

    name = input("What is your name? ")
    gender = input("Please enter your gender (M or F): ")
    birth = input("Please enter your Birthday (YYYY-MM-DD): ")
    weight = int(input("Please enter your weight (In US Pounds): "))
    height = int(input("Please enter your height (In US Inches): "))
    print()



    print(f"Age (years): {compute_age(birth)}")
    print(f"Weight (kg): {kg_from_lb(weight):.2f}")
    print(f"Height (cm): {cm_from_in(height):.1f}")
    print(f"Body mass index: {body_mass_index(weight, height):.1f}")
    print(f"Basal metabolic rate (kcal/day): {basal_metabolic_rate(gender, weight, height, birth):.0f}")

    with open("Fitness.txt", "at") as fitness_file:
        print(f"{name.title()}, {gender}, {compute_age(birth)}, {kg_from_lb(weight)}, {cm_from_in(height)}, {body_mass_index(weight, height)}, {basal_metabolic_rate(gender, weight, height, birth)}", file=fitness_file)


def compute_age(birth):

    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - birthday.year

    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1
    return years

def kg_from_lb(weight):

    org_kg= 0.45359237

    kg = weight * org_kg

    return kg

def cm_from_in(inch):
    """Convert a length in inches to centimeters.
    Parameter inch: a length in inches.
    Return: the length in centimeters.
    """
    cm = 2.54
    return inch * cm


def body_mass_index(weight, height):
    """Calculate and return a person's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
    Return: a person's body mass index.
    """
    
    bmi = (10000 * kg_from_lb(weight))/ cm_from_in(height)**2
    return bmi
    

def basal_metabolic_rate(gender, weight, height, birth):

    if gender.lower() == 'm':
        bmr_m = 88.362 + 13.397 * kg_from_lb(weight) + 4.799 * cm_from_in(height) - 5.677 * compute_age(birth)
        return bmr_m
    
    if gender.lower() == 'f':
        bmr_f = 447.593 + 9.247 * kg_from_lb(weight) + 3.098 * cm_from_in(height) - 4.330 * compute_age(birth)
        return bmr_f

main()