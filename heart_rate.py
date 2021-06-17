"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""
#To get the user's age
age = input("What is your age? ")

#Converting age into an integer value
age2 = int(age)

#Calculation of max heart beat rate
max_rate = int(220 - age2)

#Finding the minimum and maximum values of heart rate
smallest = max_rate * 0.65

greatest = max_rate * 0.85

#Printing out information for user to see
print(f"When you exercise to strengthen your heart, you should keep your "
      f"heart rate between {smallest:.0f} and {greatest:.0f} beats per minute.")