#! /usr/bin/env python3

# BLACKJACK

from random import choice
from art import logo
from replit import clear

# Functions
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_scores(user_score, cpu_score):
    if user_score == cpu_score:
        return "It's a draw!"
    elif cpu_score == 0:
        return "You lose, dealer has Blackjack!"
    elif user_score == 0:
        return "Blackjack, you win!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif cpu_score > 21:
        return "Dealer went over. You win!"
    elif user_score > cpu_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    print(logo)

    # The user and cpu should each get 2 random cards
    user_cards = []
    cpu_cards = []
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        cpu_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        cpu_score = calculate_score(cpu_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {cpu_cards[0]}")

        # If the cpu or the user have a blackjack (0) or if the user's score is over 21,
        # the the game ends.

        if user_score == 0 or cpu_score == 0 or user_score > 21:
            game_over = True
        else:
            user_hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_hit == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while cpu_score != 0 and cpu_score < 17:
        cpu_cards.append(deal_card())
        cpu_score = calculate_score(cpu_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {cpu_cards}, final score: {cpu_score}")
    print(compare_scores(user_score, cpu_score))


print("\n")
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
