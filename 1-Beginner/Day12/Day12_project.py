#! /usr/bin/env python3

# THE NUMBER GUESSING GAME

from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Functions
def check_answer(guess, answer, turns):
    """
    Checks answer against guess. Returns the number of turns remaining.
    """
    if guess > answer:
        print("Too high.")
        return turns - 1
    if guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS


def game():
    # Welcome message
    print(logo + "\n")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Setting up answer
    answer = randint(1, 101)

    # Debug
    # print(f"Pssst, the correct answer is {answer}")

    # Difficulty selection / Setting up guesses
    turns = set_difficulty()

    guess = 0
    # Let the user guess a number
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose!")
            return


game()
