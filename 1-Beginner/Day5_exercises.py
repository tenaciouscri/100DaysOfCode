#! /usr/bin/env python3

# 1. AVERAGE HEIGHT

# You are going to write a program that calculates the average student height from a
# List of heights.

# Important: you should not use the sum() or len() functions in your answer.

# DO NOT EDIT
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# DO NOT EDIT

number_of_students = 0
sum_of_heights = 0

for student in student_heights:
    number_of_students += 1
    sum_of_heights += student

average_height = round(sum_of_heights / number_of_students)
print(average_height)

# 2. HIGH SCORE

# You are going to write a program that calculates the highest score from a List of
# scores.

# Important you are not allowed to use the max or min functions.

# DO NOT EDIT
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# DO NOT EDIT

highscore = 0
for score in student_scores:
    if score > highscore:
        highscore = score

print(f"The highest score in the class is: {highscore}")

# 3. ADDING EVEN NUMBERS

# You are going to write a program that calculates the sum of all the even numbers
# from 1 to 100.

total = 0
for n in range(1, 101):
    if n % 2 == 0:
        total += n

print(total)

# 4. FIZZBUZZ

# You are going to write a program that automatically prints the solution to the
# FizzBuzz game.

# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should
# print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should
# print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number
# it should print "FizzBuzz"

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
