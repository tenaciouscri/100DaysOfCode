#! /usr/bin/env python3

import random

# 1. HEADS OR TAILS

# You are going to write a virtual coin toss program. It will randomly tell the user
# "Heads" or "Tails".

# DO NOT EDIT
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# DO NOT EDIT

heads_or_tails = random.randint(0, 1)

if heads_or_tails == 1:
    print("Heads")
else:
    print("Tails")

# 2. BANKER ROULETTE

# You are going to write a program that will select a random name from a list of
# names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# DO NOT EDIT
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# DO NOT EDIT

whos_paying = random.randint(0, len(names) - 1)

print(f"{names[whos_paying]} is going to buy the meal today!")

# 3. TREASURE MAP

# You are going to write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list.

# Your job is to write a program that allows you to mark a square on the map using a
# two-digit system. The first digit is the vertical column number and the second digit
# is the horizontal row number.

# DO NOT EDIT
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# DO NOT EDIT

chosen_column = int(position[0]) -1
chosen_row = int(position[1]) -1

map[chosen_row][chosen_column] = "X"

# DO NOT EDIT
print(f"{row1}\n{row2}\n{row3}")
# DO NOT EDIT