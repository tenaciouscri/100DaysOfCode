#! /usr/bin/env python3

# ROCK, PAPER, SCISSORS

# Make a rock, paper, scissors game.

# Start the game by asking the player:

# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

# From there you will need to figure out:

# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner
# (or a draw).
# And also how you will give feedback to the player.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))
computer_choice = random.randint(0, len(options)-1)

print(options[player_choice])
print(f"Computer chose:\n{options[computer_choice]}")

if player_choice == computer_choice:
    print("It's a draw!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")
elif player_choice == 1 and computer_choice == 0:
    print("You win!")
elif player_choice > 2:
    print("Don't cheat! Input invalid.")
else:
    print("You lose!")