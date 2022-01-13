#! /usr/bin/env python3

# HANGMAN

import random

from hangman_art import stages, logo
from hangman_words import word_list

from replit import clear

print(logo)

lives = 6

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []

for i in range(word_length):
    display += "_"

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
# print(f"{' '.join(display)}")

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()
    guessed_letters = []

    clear()

    if guess in guessed_letters:
        print(f"You've already guessed {guess}. Try with another letter!")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            guessed_letters += guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, which is not in the word. You lose a life.")
        lives -= 1
        guessed_letters += guess
        if lives == 0:
            print(f"You lose!\nThe solution was {chosen_word}!")
            game_over = True

    print(stages[lives])
    print(f"{' '.join(display)}")

    if "_" not in display:
        print("You won!")
        game_over = True
