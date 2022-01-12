#! /usr/bin/env python3

# CAESAR CIPHER

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(user_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    if shift_amount > 26:
        shift_amount %= 26
    for char in user_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    
    print(f"The {cipher_direction}d text is: \n{end_text}")

# GAME

print(logo)

game_over = False
while not game_over:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    end_game = input("Type 'yes' if you want to go again. Otherwise, type 'no'. ")
    if end_game == "yes":
        game_over = False
    elif end_game == "no":
        print("Goodbye!")
        game_over = True



