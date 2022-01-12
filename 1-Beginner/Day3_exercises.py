#! /usr/bin/env

# 1. EVEN OR ODD

# Write a program that works out whether if a given number is an odd or even number.

# DO NOT EDIT
number = int(input("Which number do you want to check? "))
# DO NOT EDIT

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# 2. BMI 2.0

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight
# and height.

# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# DO NOT EDIT
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# DO NOT EDIT

bmi = round(weight / (height ** 2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# 3. LEAP YEAR

# Write a program that works out whether if a given year is a leap year.

# This is how you work out whether if a particular year is a leap year:
# - on every year that is evenly divisible by 4
# - **except** every year that is evenly divisible by 100
# - **unless** the year is also evenly divisible by 400

# DO NOT EDIT
year = int(input("Which year do you want to check? "))
# DO NOT EDIT

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# 4. PIZZA ORDER PRACTICE

# Congratulations, you've got a job at Python Pizza. Your first job is to build an
# automatic pizza order program.

# Based on a user's order, work out their final bill.

# DO NOT EDIT
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# DO NOT EDIT

bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

total = f"Your final bill is ${bill}."
print(total)

# 5. LOVE CALCULATOR

# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word
# TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.

# DO NOT EDIT
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# DO NOT EDIT

lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

both_names = lowercase_name1 + lowercase_name2

count_t = both_names.count("t")
count_r = both_names.count("r")
count_u = both_names.count("u")
count_e = both_names.count("e")

first_digit = count_t + count_r + count_u + count_e

count_l = both_names.count("l")
count_o = both_names.count("o")
count_v = both_names.count("v")
count_e = both_names.count("e")

second_digit = count_l + count_o + count_v + count_e

score = int(str(first_digit) + str(second_digit))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
