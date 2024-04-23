# Simone Antonelli
# 17/04/2024

print("Hello World!")

print("\n") # Formatting



# Exercise 1 --------------------------------------------------------------------------------------------------------------------
print("Exercise: 1. School Grading System ↓\n")

def score_checker(student_name: str, score: list) -> None:

    average_score = sum(score) / len(score)

    if average_score >= 60:
        print(f"\tStudent: {student_name} has passed the exam with an average score of: {average_score:.2f}")
    else:
        print(f"\tStudent: {student_name} has not passed the exam.")


students: list = ["Simone", "Gaia", "Alessio"]
scores: list = [[87, 34, 53], [89, 69, 97], [71, 93, 87]]

for student, score in zip(students, scores):
    score_checker(student_name=student, score=score)

print("\n") # Formatting
# --------------------------------------------------------------------------------------------------------------------------------



# Exercise 2 --------------------------------------------------------------------------------------------------------------------
print("Exercise: 2. Guess the Number Game ↓\n")

'''
from random import randint

def guess_number(min_range, max_range, max_attempts):   
    secret_number = randint(min_range, max_range)
    
    for attempt in range(max_attempts, 0, -1):
        guess = int(input(f"\tGuess the number between {min_range} and {max_range} (attempts left: {attempt}): "))

        if guess == secret_number:
            print(f"\n\tCongratulations! You guessed the number {secret_number}!")
            return
        elif guess < secret_number:
            print("\tToo low!", end=" ")
        elif guess > secret_number:
            print("\tToo high!", end=" ")
        
        print(f"Try again. (Attempts left: {attempt - 1})\n")

    print(f"\tSorry, you have used all {max_attempts} attempts. The correct number was {secret_number}.")

min_range = 1
max_range = 100
max_attempts = 5
guess_number(min_range, max_range, max_attempts)
'''

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 3 --------------------------------------------------------------------------------------------------------------------
print("Exercise: 3. E-commerce Shopping Cart ↓\n")

from src.ex_3 import *

shopcart1: list = []

shopcart1.append(new_product(name="Tomato", price=0.02, quantity=53))
shopcart1.append(new_product(name="Steak", price=1.89, quantity=10))
shopcart1.append(new_product(name="Ketchup", price=2.99, quantity=2))

view_product(shopcart1)

shopcart1_total: float = shopcart_total(shopcart1)

print(f"\n\tThe total for your shopping cart is: {shopcart1_total}€")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 4 --------------------------------------------------------------------------------------------------------------------
print("Exercise: 4. Text Analysis ↓\n")



print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------