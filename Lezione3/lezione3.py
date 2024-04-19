# Simone Antonelli
# 17/04/2024

print("Hello World!")

print("\n") # Formatting



# Exercise 4.1 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 4-1. Pizzas ↓\n")

pizzas: list = ["Margherita", "Diavola", "Vegetariana"]

print("\tMy favorites pizza are:")

for pizza in pizzas:
    print(f"\t\t-{pizza}")

print(f"\n\tI really love {pizzas[1]}, {pizza[0]} is my second favorite. {pizzas[2]} is okay.")


print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 4.2 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 4-2. Animals ↓\n")

animals: list = ["Dog", "Cat", "Horse"]

for animal in animals:

    if animal == animals[0]:
        print("\tSome dogs barks so much!")

    elif animal == animals[1]:
        print("\tSome cats are very jealous of their owners!")

    elif animal == animals[2]:
        print("\tHorses are so big!")

print(f"\n\tEach of the three above has four legs")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 4.3 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 4-3. Counting to Twenty ↓\n")

for a in range(1, 21):
    print(f"\t{a}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 4.4 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 4-4. One Million ↓\n")

milion: list = list(range(1, 1_000_001))

choiche = input("\tPrint 1 milion numbers (Y/N)? ")

choiche = choiche.upper()

if choiche == "Y":
    for b in range(1, 1_000_001):
        print(f"\t{b}")

        if b == 1_000_000:
            print("\n\tDone!")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 4.5 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 4-5. Summing a Million ↓\n")

import time

milion_min: int = min(milion)
milion_max: int = max(milion)

print(f"\tThe lower value of 'milion' list is: {milion_min} and the higher is: {milion_max}")

start_time = time.time()
milion_sum = sum(milion)
end_time = time.time()

elpsed_time = end_time - start_time

print(f"\n\tElapsed time to sum 1 milion numbers: {elpsed_time} seconds. Sum result: {milion_sum}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 4.6 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 4-6. Odd Numbers ↓\n")

odd_numbers: list = list(range(1, 20, 2))

for number in odd_numbers:
    print(f"\t{number}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 4.7 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 4-7. Threes ↓\n")

multiples_three: list = list(range(3, 30, 3))

for number in multiples_three:
    print(f"\t{number}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 4.8 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 4-8. Cubes ↓\n")

cubes: list = [""]

for c in range(1, 11):
    cubes.append(c**3)
    print(f"\t{c}**3 = {cubes[c]}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 4.9 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 4-9. Cube Comprehension ↓\n")

comprehension: list = [f"cube**{cube}" for cube in range(11)]

print(f"\t{comprehension}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 4.10 -----------------------------------------------------------------------------------------------------------------
print("Excercise: 4-10. Slices ↓\n")

slices: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"\tThe firt three elemento of the list are: {slices[:3]}.")
print(f"\tThe middle three elemento of the list are: {slices[3:6]}.")
print(f"\tThe last three elemento of the list are: {slices[-3:]}.")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------

# Exercise 4.11 -----------------------------------------------------------------------------------------------------------------
print("Excercise: 4-11. My Pizzas, Your Pizzas ↓\n")

friend_pizzas: list = pizzas

pizzas.append("Tonno e cipolla")
friend_pizzas.append("4 Stagioni")

print(f"\tMy favorite pizzas are:\n")
for pizza in pizzas:
    print(f"\t\t-{pizza}")

print(f"\n\tMy friend's favorite pizzas are:\n")
for pizza in friend_pizzas:
    print(f"\t\t-{pizza}")
     
print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 4.12 -----------------------------------------------------------------------------------------------------------------
print("Excercise: 4-12. More Loops ↓\n")


     
print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------


# Exercise 4.14 -----------------------------------------------------------------------------------------------------------------
print("Excercise: 4-14. PEP 8 ↓\n")

# Done
     
print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 4.15 -----------------------------------------------------------------------------------------------------------------
print("Excercise: 4-15. Code Review ↓\n")

# I have formatted previus exercise to respect PEP 8
     
print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 5.1 -----------------------------------------------------------------------------------------------------------------
print("Excercise: 5-1. Conditional Tests ↓\n")

motorbike: str = "Yamaha"
print('\tis motorbike == "Yamaha"? I predict True')
print(f"\t{motorbike == 'Yamaha'}")

motorbike: str = "Honda"
print('\n\tis motorbike == "kawasaki"? I predict False')
print(f"\t{motorbike == 'Yamaha'}")

motorbike: str = "BMW"
print('\n\tis motorbike == "BMW"? I predict True')
print(f"\t{motorbike == 'BMW'}")

motorbike: str = "Suzuki"
print('\n\tis motorbike == "MV Agusta"? I predict Flase')
print(f"\t{motorbike == 'Yamaha'}")

motorbike: str = "Ducati"
print('\n\tis motorbike == "Ducati"? I predict True')
print(f"\t{motorbike == 'Ducati'}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 5.2 -----------------------------------------------------------------------------------------------------------------
print("Excercise: 5-2. More Conditional Tests ↓\n")



print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 5.3 #1 ---------------------------------------------------------------------------------------------------------------
print("Excercise: 5-3. Alien Colors #1 ↓\n")

alien_color: str = "Green"
if alien_color == "Green":
    print("\tGood shoot, you have earned 5 points!")

else:
    print("\n\tTry again")

alien_color: str = "Black"
if alien_color == "Green":
    print("\n\tGood shoot, you have earned 5 points!")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 5.4 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 5-4. Alien Colors #2 ↓\n")

alien_color: str = "Red"
if alien_color == "Green":
    print("\tGood shoot, you have earned 5 points!")

else:
    print("\tGreat shoot, you have earned 10 points!")

alien_color: str = "Green"
if alien_color == "Green":
    print("\n\tGood shoot, you have earned 5 points!")

else:
    print("\tGreat shoot, you have earned 10 points!")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 5.5 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 5-5. Alien Colors #3 ↓\n")

alien_color: str = "Green"
if alien_color == "Green":
    print("\tGood shoot, you have earned 5 points!")

elif alien_color == "Yellow":
    print("\tGreat shoot, you have earned 10 points!")

else:
    print("\tGreat shoot, you have earned 15 points!")

alien_color: str = "Yellow"
if alien_color == "Green":
    print("\tGood shoot, you have earned 5 points!")

elif alien_color == "Yellow":
    print("\tGreat shoot, you have earned 10 points!")

else:
    print("\tGreat shoot, you have earned 15 points!")

alien_color: str = "Red"
if alien_color == "Green":
    print("\tGood shoot, you have earned 5 points!")

elif alien_color == "Yellow":
    print("\tGreat shoot, you have earned 10 points!")

else:
    print("\tGreat shoot, you have earned 15 points!")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------