# Exercise 18.1 -------------------------------------------------------------------------------------------------------------------
print("Exercise: 18-1. Safe Square Root ↓\n")

import math

def safe_sqrt(number: float) -> float:

    if number >= 0:
        result: float = math.sqrt(number)
    else:
        raise ValueError("Value cannot be negative")
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 18.2 -------------------------------------------------------------------------------------------------------------------
print("Exercise: 18-2. Password Validation ↓\n")

import string

class InvalidPasswordError(Exception):
    '''Password non valid'''

def validate_password(password: str) -> None:

    if not len(password) >= 20:
        raise InvalidPasswordError("Password must have at least 20 total chars")
    
    upper_counter: int = 0
    special_counter: int = 0

    for char in password:
        if char in string.ascii_uppercase:
            upper_counter += 1

        elif char in string.punctuation:
            special_counter += 1

    if not upper_counter >= 3:
        raise InvalidPasswordError("Password must have at least three upper chars")
    
    if not special_counter >= 4:
        raise InvalidPasswordError("Password must have at least three special chars")
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 18.3 -------------------------------------------------------------------------------------------------------------------
print("Exercise: 18-3. Context Managers for File Handling ↓\n")

with open("test.txt", "w") as file:

    try:
        file.write("Hello, World!")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
    finally:
        file.close()
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 18.4 -------------------------------------------------------------------------------------------------------------------
print("Exercise: 18-4. Database of dates ↓\n")


# -------------------------------------------------------------------------------------------------------------------------------