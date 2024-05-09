# Simone Antonelli
# 17/04/2024

print("\nHello World!")

print("\n") # Formatting



# Exercise 2-3 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 2-3. Personal Message ↓\n")

name: str = "Gaia"

print(f"\tHello {name}, would you like to learn some Python today?")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 2-4 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 2-4. Name Cases ↓\n")

name: str = "gAiA"

lower_name: str = name.lower()
upper_name: str = name.upper()
title_name: str = name.title()

#print(f"\tNormal name: {name}.\n\tLowercase name: {lower_name}.\n\tUppercase name: {upper_name}.\n\tTitle case name: {title_name}.")

print(f"\tNormal name: {name}.")
print(f"\tLowercase name: {lower_name}.")
print(f"\tUppercase name: {upper_name}.")
print(f"\tTitle case name: {upper_name}.")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 2-5 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 2-5. Famous Quote ↓\n")

print('\tAlbert Einstein once said, “A person who never made a mistake never tried anything new."')

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 2-6 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 2-6. Famous Quote 2 ↓\n")

famous_person: str = "Elon Musk"

message: str = f"\tHello {famous_person}, would you like to learn some Python today?"

print(message)

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 2-8 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 2-8. File extension ↓\n")

filename: str = "python_notes.txt"

filename_clear: str = filename.removesuffix(".txt")

print(f"\tFilename: {filename_clear}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 3-1 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 3-1. Names ↓\n")

names: list = ["Simone", "Alessio", "Matteo", "Luca", "Valerio"]

print(f"\tIndex 0: {names[0]}")
print(f"\tIndex 1: {names[1]}")
print(f"\tIndex 2: {names[2]}")
print(f"\tIndex 3: {names[3]}")
print(f"\tIndex 4: {names[4]}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 3-2 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 3-2. Greetings ↓\n")

print(f"\tHello {names[0]}, would you like to learn some Python today?")
print(f"\tHello {names[1]}, would you like to learn some Python today?")
print(f"\tHello {names[2]}, would you like to learn some Python today?")
print(f"\tHello {names[3]}, would you like to learn some Python today?")
print(f"\tHello {names[4]}, would you like to learn some Python today?")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 3-3 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 3-3. Your Own List ↓\n")

motorcycles: list = ["Ducati", "Yamaha", "Triumph", "Honda", "Suzuki"]

print(f"\tI would like to have a {motorcycles[0]} motorcycle!")
print(f"\tI currently have a {motorcycles[1]} motorcycle!")
print(f"\tI like {motorcycles[2]}'s motorcycles!")
print(f"\tI hope i never have a {motorcycles[3]} motorcycle!")
print(f"\tI don't wish for anyone to have a {motorcycles[4]} motorcycle!")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 3-4 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 3-4. Guest List ↓\n")

guests: list = ["Elon Musk", "Albert Einstein", "David Beckham"]

print(f"\tDear {guests[0]}, would you like to have dinner tomorrow night?")
print(f"\tDear {guests[1]}, would you like to have dinner tomorrow night?")
print(f"\tDear {guests[2]}, would you like to have dinner tomorrow night?")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 3-5 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 3-5. Changing Guest List ↓\n")

print(f"\tOh no {guests[1]} seams busy and he can't come to the tomorrow dinner!")

guests[1] = "Nicolas Latifi"
print(f"\tDear {guests[0]}, would you like to have dinner tomorrow night?")
print(f"\tDear {guests[1]}, would you like to have dinner tomorrow night?")
print(f"\tDear {guests[2]}, would you like to have dinner tomorrow night?")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 3-6 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 3-6. More Guests ↓\n")

print(f"\tDear guests, i found a bigger table for the tomorrow dinner, so other guests will be invitated.\n")

guests.insert(0, "Luka Doncic")
guests.insert(2, "Matteo Paiella")
guests.append("Dua Lipa")

print(f"\tDear {guests[0]}, would you like to have dinner tomorrow night?")
print(f"\tDear {guests[1]}, would you like to have dinner tomorrow night?")
print(f"\tDear {guests[2]}, would you like to have dinner tomorrow night?")
print(f"\tDear {guests[3]}, would you like to have dinner tomorrow night?")
print(f"\tDear {guests[4]}, would you like to have dinner tomorrow night?")
print(f"\tDear {guests[5]}, would you like to have dinner tomorrow night?")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 3-7 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 3-7. Shrinking Guest List ↓\n")

print(f"\tDear guests, i can invite only two guests, i'm sorry.\n")

guests.pop(0)
guests.pop(0)
guests.pop(2)
guests.pop(2)

print(f"\t{guests[0]} and {guests[1]}, you two guys, are still invited to the dinner, se you tomorrow.\n")

del guests[0]
del guests[0]

print(f"\tChecking empty list: {guests}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 3-8 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 3-8. Seeing the World ↓\n")

wonderful_places: list = ["Japan", "California", "South Africa", "Brazil", "Norway"]

print(f"\tCheck normal list order: {wonderful_places}\n")

print(f"\tAlphabetic order sorted list: {sorted(wonderful_places)}")
print(f"\tCheck normal list order: {wonderful_places}\n")

print(f"\tReverse alphabetic order sorted list: {sorted(wonderful_places)[::-1]}")
print(f"\tCheck normal list order: {wonderful_places}\n")

wonderful_places.reverse()
print(f"\tReverse order list: {wonderful_places}")
wonderful_places.reverse()
print(f"\tCheck normal list order: {wonderful_places}\n")

print(f"\tAlphabetic order sort list: {wonderful_places.sort()}")
print(f"\tCheck normal list order: {wonderful_places}\n")

print(f"\tReverse alphabetic order sort list: {wonderful_places.sort(reverse=True)}")
print(f"\tCheck normal list order: {wonderful_places}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 3-9 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 3-9. Dinner Guests ↓\n")

print(f"\tCurrenty there are {len(guests)} guests invited to the tomorrow dinner.")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------


# Exercise 3-10 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 3-10. Every Function ↓\n")

# Done in precedent exercises

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 6.1 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 6-1. Person ↓\n")

me: dict = {"first_name": "Simone", "last_name": "Antonelli", "age": 19, "city": "Rome"}

print(f"\tSubject name: {me['first_name']}")
print(f"\tSubject last name: {me['last_name']}")
print(f"\tSubject age: {me['age']}")
print(f"\tSubject city: {me['city']}")


print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 6.2 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 6-2. Favorite Numbers ↓\n")

favorite_numbers: dict = {
    "Simone": 5,
    "Alessio": 17,
    "Gaia": 18,
}

for person, number in favorite_numbers.items():
    print(f"\t{person}'s favorite number is {number}.")


print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 6.3 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 6-3. Glossary ↓\n")

glossary: dict = {
    "variable": "A placeholder for storing data.",
    "function": "A named block of code that performs a specific task.",
    "loop": "A control structure that repeats a block of code until a condition is met.",
    "list": "An ordered collection of items.",
    "dictionary": "A collection of key-value pairs."
}

for word, meaning in glossary.items():
    print(f"\t{word}: {meaning}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 6.7 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 6-7. People ↓\n")

alessio: dict = {"first_name": "Alessio", "last_name": "x", "age": 19, "city": "Rome"}

gaia: dict = {"first_name": "Gaia", "last_name": "x", "age": 20, "city": "Rome"}


people: list = [me, alessio, gaia]

for person in people:
    print(f"\tSubject name: {person['first_name']}")
    print(f"\tSubject last name: {person['last_name']}")
    print(f"\tSubject age: {person['age']}")
    print(f"\tSubject city: {person['city']}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 6.8 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 6-8. Pets ↓\n")

pets: list = [
    {"kind": "Dog", "owner": "Alessio"},
    {"kind": "Cat", "owner": "Simone"},
    {"kind": "Horse", "owner": "Gaia"},
]

# Stampare tutto ciò che si sa su ogni animale domestico
for pet in pets:
    print(f"\t{pet['kind']} owned by: {pet['owner']}.")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 6.9 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 6-9. Favorite Places ↓\n")

favorite_places: dict = {
    "Simone": ["Rome", "Los Angeles", "Sydney"],
    "Alessio": ["London", "Cape Verde", "Los Angeles"],
    "Gaia": ["New York", "Vienna", "Paris"]
}

for person, places in favorite_places.items():
    print(f"\t{person}'s favorite places are:")
    for place in places:
        print(f"\t\t- {place}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 6.10 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 6-10. Favorite Numbers ↓\n")

favorite_numbers: dict = {
    "Simone": [5, 3],
    "Alessio": [17, 7],
    "Gaia": [18, 6],
}

for person, numbers in favorite_numbers.items():
    print(f"\t{person}'s favorite numbers are: {numbers[0]}", end="")
    for num in numbers[1:]:
        print(f" and {num}\n", end="")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 6.11 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 6-11. Cities ↓\n")

cities: dict = {
    "New York": {"country": "USA", "population": 8000000, "fact": "New York City is known as the 'Big Apple'."},
    "Sydney": {"country": "Australia", "population": 5000000, "fact": "Sydney Opera House is a famous landmark of Sydney."},
    "Tokyo": {"country": "Japan", "population": 9000000, "fact": "Tokyo is the most populous metropolitan area in the world."}
}

for city, info in cities.items():
    print(f"\n\t{city}:")
    print(f"\t\tCountry: {info['country']}")
    print(f"\t\tPopulation: {info['population']}")
    print(f"\t\tFact: {info['fact']}")


print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 6.12 ------------------------------------------------------------------------------------------------------------------
print("Excercise: 6-12. Extensions ↓\n")

favorites = {
    "Simone": {"numbers": [5, 3], "colors": ["blue", "green"]},
    "Alessio": {"numbers": [17, 7], "colors": ["cyan", "yellow"]},
    "Gaia": {"numbers": [18, 6], "colors": ["cyan", "white"]},
}

show_colors = input("Do you want to display favorite colors as well? (Y/N): ").strip().upper() == "Y"

for person, favorites_info in favorites.items():
    print(f"\n\t{person}'s favorites:")
    numbers = favorites_info["numbers"]
    print(f"\t\tFavorite Numbers are: {numbers[0]}", end="")

    for num in numbers[1:]:
        print(f" and {num}", end="")
        
    print("." if not show_colors else ",")

    if show_colors:
        colors = favorites_info["colors"]
        print(f"\t\tFavorite Colors are: {colors[0]}", end="")

        for color in colors[1:]:
            print(f" and {color}", end="")
        print(".")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------