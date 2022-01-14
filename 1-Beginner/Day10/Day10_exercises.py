#! /usr/bin/env python3

# DAYS IN MONTH

# In the starting code, you'll find the solution from the Leap Year challenge. First,
# convert this function is_leap() so that instead of printing "Leap year." or "Not
# leap year." it should return True if it is a leap year and return False if it is not
# a leap year.
# You are then going to create a function called days_in_month() which will take a year
# and a month as inputs.
# And it will use this information to work out the number of days in the month, then
# return that as the output.

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(user_year, user_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if user_month == 2:
        user_year_is_leap = is_leap(user_year)
        if user_year_is_leap == True:
            days_in_month = 29
            return days_in_month
        else:
            days_in_month = month_days[user_month - 1]
            return days_in_month
    else:
        days_in_month = month_days[user_month - 1]
        return days_in_month

# DO NOT EDIT
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
# DO NOT EDIT
