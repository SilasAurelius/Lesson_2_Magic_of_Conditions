"""
Task 1: Leap Year Checker
Definition of a leap year: Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

Expected Outcome: If you test the year 1900, is should be False. The year 2000 should be True. The year 2024 should be True

"""
leap_year = True
def start():

    year = int(input("Enter a year: "))

    if   (year % 4 == 0) and (year % 100 == 0):
        print("TRUE. This is a leap year. ")
    
    elif (year % 4 == 0) and (year % 100 != 0): 
        print("TRUE. This is a leap year.")
        
    else:
        print(" FALSE. This is not a leap year.")   
         
while leap_year:
    start()