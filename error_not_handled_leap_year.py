# CS362_Winter21
# HW3
# Program: error_not_handled_leap_year.py
# Author: Kwanghyuk Kim

###########################################################################
# Program Description
# : An application that calculates whether the year is a leap year or not
#   without error handled input.
#
# To compile and run this code, please just enter the commands as below: 
#
# python3 error_not_handled_leap_year.py
###########################################################################

###########################################################################
# is_leap() function
# 1. Set the variable leap to False.
# 2. Calculates whether the year is a leap year or not.
#   2-1. If year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# 3. Return True or False
###########################################################################
def is_leap(year):    
    leap = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True    
    return leap

cont = '1'
while (cont == '1'):
    print("Enter a year: ", end="")
    year = int(input())
    if is_leap(year) == True:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
    print("\nContinue(1) or exit(anykey): ", end="")
    cont = input()
    print()