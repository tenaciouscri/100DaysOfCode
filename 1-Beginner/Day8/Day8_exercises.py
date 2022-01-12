#! /usr/bin/env python3

from math import ceil

# 1. PAINT AREA CALCULATOR
# 
# You are painting a wall. The instructions on the paint can says that 1 can of
# paint can cover 5 square meters of wall. Given a random height and width of
# wall, calculate how many cans of paint you'll need to buy.

def paint_calc(height, width, cover):
    number_of_cans = ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint.")

# Define a function called paint_calc() so that the code below works.   

# DO NOT EDIT
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
# DO NOT EDIT

# 2. PRIME NUMBERS

# You need to write a function that checks whether if the number passed into it is
# a prime number or not.

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Do NOT EDIT
n = int(input("Check this number: "))
prime_checker(number=n)
# DO NOT EDIT