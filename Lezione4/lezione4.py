# Simone Antonelli
# 17/04/2024

print("Hello World!")

print("\n") # Formatting



# Exercise 8.1 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 8-1. Message ↓\n")

def display_message() -> None:
    print("\tI'm learning Python functions!")

display_message()

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.2 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 8-2. Favorite Book ↓\n")

def favorite_book(title: str) -> None:
    print(f"\tOne of my favorite books is {title}")

favorite_book("Three Laws of Robotic")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.3 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 8-3. T-Shirt ↓\n")

def make_shirt(size: str, message: str) -> None:
    print(f"\tThe t-shirt size will be {size} and it will have the message: '{message}'")

# Quest 1
make_shirt("M", "Divide and Conquire")

# Quest 2
make_shirt(message="Divide et impera", size="XL")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.4 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 8-4. Large Shirts ↓\n")

def make_shirt(size: str = "L", message: str = "I love Python") -> None:

    print(f"\tThe t-shirt size will be {size} and it will have the message: '{message}'")

# Quest 1
make_shirt()

# Quest 2
make_shirt(size="M")

# Quest 3
make_shirt(size="M", message="Eh comosemo")


print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.5 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 8-5. Cities ↓\n")

def describe_city(city_name: str, country: str = "Italy") -> None:
    print(f"\t{city_name} is in {country}")

# Quest 1
describe_city(city_name="Rome")

# Quest 2
describe_city(city_name="San Paulo", country="Brazil")

# Quest 3
describe_city(city_name="Alicante", country="Spain")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.6 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 8-6. City Names ↓\n")

def city_country(city_name: str, country: str) -> str:
    output_message = f"\t{city_name}, {country}"
    return output_message

# Quest 1
italy: str = city_country(city_name="Rome", country="Italy")
print(italy)

# Quest 2
brazil: str = city_country(city_name="San Paulo", country="Brazil")
print(brazil)

# Quest 3
spain: str = city_country(city_name="Alciante", country="Spain")
print(spain)

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.7 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 8-7. Album ↓\n")

def make_album(artist_name: str, album_title: str) -> dict:
    album: dict = {"artist_name": artist_name, "album_title": album_title}
    return album

# Quest 1
cuco = make_album(artist_name="Cuco", album_title="wonnabewithu")
print(cuco)

# Quest 2
fabrizio = make_album(artist_name="Fabrizio De André", album_title="Volume 3")
print(fabrizio)

# Quest 3
tyler = make_album(artist_name="Tyler, The Creator", album_title="IGOR")
print(tyler)

# Quest 4
def make_album(artist_name: str, album_title: str, songs_number = None) -> dict:
    if songs_number == None:
        album: dict = {"artist_name": artist_name, "album_title": album_title}
    else:
        album: dict = {"artist_name": artist_name, "album_title": album_title, "songs_number": songs_number}
    return album

tyler = make_album(artist_name="Cuco", album_title="Para Mi", songs_number=13)
print(tyler)

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.8 ------------------------------------------------------------------------------------------------------------------
'''
print("Exercise: 8-8. User Albums ↓\n")

while True:
    try:
        artist_name = input("\tInsert the artist name: ")
        if not artist_name:
            raise ValueError("\tThe artist name can't be 'None'")
        
        album_title = input("\tInserisci il nome dell'album: ")
        if not album_title:
            raise ValueError("\tThe album name can't be 'None'")
        
        songs_number = input("\tInserisci il numero di brani: ")
        if songs_number == "":
            user_album: dict = make_album(artist_name=artist_name, album_title=album_title) 

        else:
            user_album: dict = make_album(artist_name=artist_name, album_title=album_title, songs_number=songs_number) 

        break
    
    except ValueError as ve:
        print("Errore:", ve)
        print("Per favore, inserisci valori validi.")

print(f"\t{user_album}")

print("\n") # Formatting
'''
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.9 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 8-9. Messages ↓\n")

def print_list(list: list) -> None:
    for item in list:
        print(f"\t{item}")

messages: list = ["Hi, how are you?", "Everything's fine, and you?", "I'm okay, thank you."]

print_list(list=messages)

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.10 -----------------------------------------------------------------------------------------------------------------
print("Exercise: 8-10. Sending Messages ↓\n")



print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.11 -----------------------------------------------------------------------------------------------------------------
print("Exercise: 8-11. Archived Messages ↓\n")



print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.12 -----------------------------------------------------------------------------------------------------------------
print("Exercise: 8-12. Sandwiches ↓\n")



print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.13 -----------------------------------------------------------------------------------------------------------------
print("Exercise: 8-13. User Profile ↓\n")



print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.14 -----------------------------------------------------------------------------------------------------------------
print("Exercise: 8-14. Cars ↓\n")



print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.15 -----------------------------------------------------------------------------------------------------------------
print("Exercise: 8-15. Printing Models ↓\n")



print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.16 -----------------------------------------------------------------------------------------------------------------
print("Exercise: 8-16. Imports ↓\n")



print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.17 -----------------------------------------------------------------------------------------------------------------
print("Exercise: 8-17. Styling Functions ↓\n")



print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 'Fibonacci' ----------------------------------------------------------------------------------------------------------
print("Exercise: 'Fibonacci' ↓\n")

def fibonacci(n: int) -> int:
    if n <= 2:
        return 1
    else: 
        return fibonacci(n=n-1) + fibonacci(n=n-2)
    
user_input: int = int(input("\tInsert the number for Fibonacci sequence: "))

result = fibonacci(user_input)

print(f"\tResult: {result}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 'Fibonacci_for' ------------------------------------------------------------------------------------------------------
print("Exercise: 'Fibonacci_for' ↓\n")

def fibonacci_for(n: int) -> int:
    memo:list = [0, 1]
    for i in range(1, n):
        result: int = memo[i-1] + memo[i]
        memo.append(result)
    return memo[-1]
    
user_input: int = int(input("\tInsert the number for Fibonacci sequence: "))

result = fibonacci_for(user_input)

print(f"\tResult: {result}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------