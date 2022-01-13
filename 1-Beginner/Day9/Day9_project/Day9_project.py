#! /usr/bin/env python3

# THE SECRET AUCTION PROGRAM

from replit import clear

from art import logo

all_bids = {}

game_over = False


def find_highest_bidder(bidding_record):
    winning_bid = 0
    winning_bidder = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > winning_bid:
            winning_bid = bid_amount
            winning_bidder = bidder
    print(
        f"The winner of the auction is {winning_bidder} with a bid of ${winning_bid}!"
    )


while not game_over:
    print(logo)
    bidder_name = input("Welcome to the Secret Auction!\nPlease enter your name: ")
    bid = int(input("Enter your bid: $"))
    all_bids[bidder_name] = bid

    continue_bid = input("Are there any other bidders?\nEnter 'yes' or 'no': ")

    if continue_bid == "yes":
        clear()
        game_over = False
    elif continue_bid == "no":
        find_highest_bidder(all_bids)
        game_over = True
