#! /usr/bin/env python3

# TREASURE ISLAND

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. Good luck!\n")


print("You find yourself at a crossroad in the middle of a forest.\nOn the left, you can hear water flowing in the distance.\nOn the right, you can hear the wind howling.\n")
left_or_right = input("Do you go left or right? ").lower()
if left_or_right == "left":
    print("You reach the bank of a river.\nNearby, you see a sign reading 'Next boat ride in 1 hour.'\n")
    swim_or_wait = input("Do you wait for a ride, or do you cross the river swimming? ").lower()
    if swim_or_wait == "wait":
        print("You wait until the boat service brings you safely to the other side of the river.")
        print("There, you find a cave.\nInside, right in front of you, stand three doors.\nOne red, one blue, and one yellow.\n")
        which_door = input("Which door do you want to open? ").lower()
        if which_door == "red":
            print("You cross the red door. Behind it, there's a room full of lava.")
            print("This fiery hell leads you to your inevitable doom. GAME OVER")
        elif which_door == "blue":
            print("You cross the blue door. Inside, there's a famished troop of lions.")
            print("They devour you in an instant. GAME OVER")
        elif which_door == "yellow":
            print("You cross the yellow door. Inside, you see a treasure chest overflowing with gems and gold.")
            print("Congratulations, YOU'VE WON!")
        else:
            print("You can't decide, so you spend the rest of your days thinking about it. GAME OVER")
    else:
        print("You're quite impatient, so you decide to swim to the other side of the river.")
        print("However, a giant trout attacks you, leading you to your inevitable doom. GAME OVER")
else:
    print("You fall down a cliff to your inevitable doom. GAME OVER")
