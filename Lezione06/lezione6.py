# Simone Antonelli
# 17/04/2024

print("\nHello World!")

print("\n") # Formatting



# Exercise 9.1 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 9-1. Restaurant ↓\n")

class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\tRestaurant name: '{self.restaurant_name}'\n\tRestaurant cuisine type: '{self.cuisine_type}'")


    def open_restaurant(self):
        print(f"\n\tRestaurant '{self.restaurant_name}' is now open!")

r1: Restaurant = Restaurant("La Boca", "Argentine meat")
r1.describe_restaurant()
r1.open_restaurant()

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 9.2 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 9-2. Three Restaurants ↓\n")

r2: Restaurant = Restaurant("Enoteca Ponziani", "Wine shop, Mediterranean")
r3: Restaurant = Restaurant("Oro", "Luxury mediterranean")

r1.describe_restaurant()
print() # Formatting
r2.describe_restaurant()
print() # Formatting
r3.describe_restaurant()

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 9.3 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 9-3. Users ↓\n")

import random
class User:
    def __init__(self, first_name: str, last_name: str, age: int, gender: str, height: int, weight: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender        
        self.height = height                
        self.weight = weight

    def describe_restaurant(self):
        print(f"\tFull name: {self.first_name} {self.last_name}" \
              f"\n\tAge: {self.age}" \
              f"\n\tGender: {self.gender}" \
              f"\n\tHeight: {self.height}" \
              f"\n\tWeight: {self.weight}")
        
    def greet_user(self):
        greetings: list[str] = [
            f"\tHi, {self.first_name} {self.last_name}, it's nice to see you!",
            f"\tHello, {self.first_name} {self.last_name}! How are you doing today?",
            f"\tHey there, {self.first_name} {self.last_name}, hope you're having a great day!",
            f"\tGood day, {self.first_name} {self.last_name}! What's new?",
            f"\tWelcome back, {self.first_name} {self.last_name}! Ready to get things done?"
        ]

        selected_greeting = random.choice(greetings)
        print(selected_greeting)


user1: User = User("Alice", "Smith", 30, "Female", 165, 60)
user1.greet_user()

user2: User = User("Bob", "Johnson", 25, "Male", 180, 75)
user2.greet_user()

user3: User = User("Charlie", "Brown", 40, "Male", 175, 80)
user3.greet_user()

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 9.4 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 9-4. Number Served ↓\n")

class RestaurantV2(Restaurant):

    def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int = 0) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.number_served = number_served

    def set_number_served(self, new_number_served: int):
        self.number_served = new_number_served

    def increment_number_served(self, number_served_increment: int):
        self.number_served += number_served_increment

r4 = RestaurantV2("Pascucci al Porticciolo", "Italian")

print(f"\t{r4.restaurant_name} today has served {r4.number_served} customers! Current time: 11:46 AM")
r4.set_number_served(18)
print(f"\t{r4.restaurant_name} today has served {r4.number_served} customers! Current time: 05:32 PM")
r4.increment_number_served(14)
print(f"\t{r4.restaurant_name} made 14 new customers, today has made {r4.number_served}! Current time: 10:05 PM")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 9.5 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 9-5. Login Attempts ↓\n")

import random
class UserV2(User):
    def __init__(self, first_name: str, last_name: str, age: int, gender: str, height: int, weight: int, login_attempts: int = 0) -> None:
        super().__init__(first_name, last_name, age, gender, height, weight)
        self.login_attempts = login_attempts

    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

users = [
    UserV2("Alice", "Smith", 30, "Female", 165, 50),
    UserV2("Bob", "Johnson", 25, "Male", 180, 75),
    UserV2("Charlie", "Brown", 40, "Male", 155, 45)
]

for user in users:
    for _ in range(random.randint(1, 10)):
        user.increment_login_attempts()
    print(f"\tUser {user.first_name} {user.last_name} attempted to login {user.login_attempts} times")

print() # Formatting

for user in users:
    user.reset_login_attempts()
    print(f"\tUser {user.first_name} {user.last_name} login attempts has been resetted: {user.login_attempts}")


print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 9.6 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 9-6. Ice Cream Stand ↓\n")

class RestaurantV3(Restaurant):

    def __init__(self, restaurant_name: str, cuisine_type: str, flavors : list[str]) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f"\tAvailable ice cream flavors in {self.restaurant_name} restaurant are: {', '.join(self.flavors)}")

r5: RestaurantV3 = RestaurantV3("Pops", "Hamburgers", ["Chocolate", "Vanilla", "Mascarpone", "Strawberry", "coffee"])

r5.display_flavors()

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 9.7 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 9-7. Admin ↓\n")

class Admin(User):

    def __init__(self, first_name: str, last_name: str, age: int, gender: str, height: int, weight: int, privileges: list[str]) -> None:
        super().__init__(first_name, last_name, age, gender, height, weight)
        self.privileges = privileges

    def show_privileges(self):
        print(f"\tUser {user.first_name} {user.last_name} privileges")
        for privilege in self.privileges:
            print(f"\t\t{privilege}")

admin_privileges: list[str] = ["Add Posts", "Remove Posts", "Mute Users"]

admin1: Admin = Admin("Robert", "Clark", 30, "Male", 185, 85, admin_privileges)

admin1.show_privileges()

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 9.8 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 9-8. Privileges ↓\n")

class Privileges:
    
    def __init__(self, privileges: list[str]) -> None:
        self.privileges: list[str] = privileges

    def show_privileges(self):
        print(f"\tActive privileges")
        for privilege in self.privileges:
            print(f"\t\t{privilege}")


class AdminV2(User):

    def __init__(self, first_name: str, last_name: str, age: int, gender: str, height: int, weight: int, privileges: Privileges) -> None:
        super().__init__(first_name, last_name, age, gender, height, weight)
        self.privileges = privileges


admin_privilegesV2: Privileges = Privileges(["Add Posts", "Remove Posts", "Mute Users"])

admin2: AdminV2 = AdminV2("Frederik", "Jhonson", 26, "Male", 175, 65, admin_privilegesV2)

admin2.privileges.show_privileges()

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 9.9 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 9-9. Battery Upgrade ↓\n")

# Exercise electric_car.py do not exists in "Esercizi Lezione 6 (Obbligatori)"

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 9.10 -------------------------------------------------------------------------------------------------------------------
print("Exercise: 9-10. Imported Restaurant ↓\n")

pass

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 9.11 -------------------------------------------------------------------------------------------------------------------
print("Exercise: 9-11. Imported Admin ↓\n")

pass

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 9.12 -------------------------------------------------------------------------------------------------------------------
print("Exercise: 9-12. Multiple Modules ↓\n")

pass

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 9.13 -------------------------------------------------------------------------------------------------------------------
print("Exercise: 9-13. Dice ↓\n")

class Dice:

    def __init__(self, sides: int) -> None:
        self.sides: int = sides

    def roll_die(self):
        print(f"Number rolled on the {self.sides} sides dice: {random.randint(1, self.sides)}")

dice1: Dice = Dice(6)
for _ in range(10):
    dice1.roll_die()

print() # Formatting

dice2: Dice = Dice(10)
for _ in range(10):
    dice2.roll_die()

print() # Formatting

dice3: Dice = Dice(20)
for _ in range(10):
    dice3.roll_die()

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 9.14 -------------------------------------------------------------------------------------------------------------------
print("Exercise: 9-14. Lottery ↓\n")

possible_charts: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'G', 'M', 'C', 'L']

winning_charts: list = [chart for chart in random.sample(possible_charts, 4)]

print(f"These are the winning charts -> {winning_charts}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 9.15 -------------------------------------------------------------------------------------------------------------------
print("Exercise: 9-15. Lottery Analysis ↓\n")

import time

ticket_pulls: int = 0

my_ticket: list = ['7', 'A', '6', 'G']

start: int = time.time()
while True:
    
    ticket_pulls += 1
    
    if my_ticket == winning_charts:
        end: int = time.time()
        print(f"\tYout ticket wins after {ticket_pulls} ticket pulls and {end - start:.3f} seconds")
        break
    else:
        winning_charts: list = [chart for chart in random.sample(possible_charts, 4)]
        

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------