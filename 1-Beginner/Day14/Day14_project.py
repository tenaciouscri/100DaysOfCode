#! /usr/bin/env python3

# HIGHER OR LOWER

from art import logo, vs
from game_data import data

from replit import clear
import random

# Functions
def account_format(account):
    """
    Format the account data into printable format
    """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}."


def check_answer(guess, a_followers, b_followers):
    """
    Take the user guess and follower counts and returns if they got it right.
    """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display art
print(logo)
score = 0
game_over = False
account_b = random.choice(data)

# Make the game repeatable
while not game_over:

    # Generate a random account from the game data
    # Move b to a
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    # Format the account data into printable format
    print(f"Compare A: {account_format(account_a)}")
    print(vs)
    print(f"Against B: {account_format(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Use if statement to check if user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds
    clear()
    print(logo)

    # Give user feedback on their guess
    # Score keeping
    if is_correct == True:
        game_over = False
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}")
