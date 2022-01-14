#! /usr/bin/env python3

# CALCULATOR

from art import logo

# Functions


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# Dictionary

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Program

print(logo)
print("Welcome to the Python Calculator!")


def calculator():
    num1 = float(input("Enter the first number: "))

    calculation_over = False

    for key in operations:
        print(key)

    while not calculation_over:
        chosen_operation = input("Pick an operation symbol: ")
        num2 = float(input("Enter the next number: "))

        calculation_function = operations[chosen_operation]
        answer = calculation_function(num1, num2)

        print(f"{num1} {chosen_operation} {num2} = {answer}")
        continue_calculation = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        )
        if continue_calculation == "y":
            num1 = answer
            calculation_over = False
        elif continue_calculation == "n":
            calculation_over = True
            print("\n")
            calculator()
        else:
            calculation_over = True


calculator()
