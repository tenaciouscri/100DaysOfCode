#! /usr/bin/env python3

# 1. GRADING PROGRAM

# You have access to a database of student_scores in the format of a dictionary.
# The keys in student_scores are the names of the students and the values are their
# exam scores.

# Write a program that converts their scores to grades. By the end of your program,
# you should have a new dictionary called student_grades that should contain student
# names for keys and their grades for values. The final version of the student_grades
# dictionary will be checked.

# DO NOT write any print statements.

# DO NOT EDIT
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# DO NOT EDIT

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score <= 70:
        student_grades[student] = "Fail"
    elif score <= 80:
        student_grades[student] = "Acceptable"
    elif score <= 90:
        student_grades[student] = "Exceeds Expectations"
    else:
        student_grades[student] = "Outstanding"

# DO NOT EDIT
print(student_grades)
# DO NOT EDIT

# 2. DICTIONARY IN LIST

# You are going to write a program that adds to a travel_log. You can see a travel_log
# which is a List that contains 2 Dictionaries.
# Write a function that will work with the following line of code on line 21 to add the
# entry for Russia to the travel_log.

# DO NOT EDIT
travel_log = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]
# DO NOT EDIT


def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)


# DO NOT EDIT
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
# DO NOT EDIT
