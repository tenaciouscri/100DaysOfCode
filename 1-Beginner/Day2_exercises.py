#! /usr/bin/env python3

# 1. DATA TYPES

# Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Type a two digit number: ")

first_num = int(two_digit_number[0])
second_num = int(two_digit_number[1])

print(first_num + second_num)

# 2. BMI CALCULATOR

# Write a program that calculates the Body Mass Index (BMI) from
# a user's weight and height.
# The BMI is calculated by dividing a person's weight (in kg) by
# the square of their height (in m)

# DO NOT EDIT
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# DO NOT EDIT

bmi = float(weight) / (float(height)**2)

print(int(bmi))

# 3. LIFE IN WEEKS

# Create a program using maths and f-Strings that tells us how many
# days, or weeks, or months we have left if we live until 90 years old.

# DO NOT EDIT
age = input("What is your current age? ")
# DO NOT EDIT

years_left = 90 - int(age)

days_left = 365 * years_left
weeks_left = 52 * years_left
months_left = 12 * years_left

print(f"You have {days_left} days, or {weeks_left} weeks, or {months_left} months left.")
