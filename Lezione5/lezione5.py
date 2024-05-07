# Simone Antonelli
# 17/04/2024

print("Hello World!")

print("\n") # Formatting



# Exercise 1 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 1. Create a playlist ↓\n")

# Function to create a playlist with a given name and list of songs
def create_playlist(name: str, songs: list) -> dict:
    # Create a new playlist dictionary with the given name and list of songs
    new_playlist: dict = {name: songs}
    # Return the newly created playlist
    return new_playlist

# Create three playlists using the create_playlist function
playlist_1: dict = create_playlist("Road Trip", ["Song 1", "Song 2"])
playlist_2: dict = create_playlist("Fire", ["Song 1", "Song 2", "Song 3"])
playlist_3: dict = create_playlist("Sky", ["Song 1", "Song 2", "Song 3", "Song 4"])

# Print the created playlists
print(f"\t{playlist_1}\n\t{playlist_2}\n\t{playlist_3}")


# Function to add like to a playlist
def add_like(dictionary: dict, playlist_name: str, liked: bool=True):
    # Iterate through each playlist in the dictionary
    for playlist in dictionary.values():
        # Check if the given playlist name exists in the current playlist
        if playlist_name in playlist:
            # Add a 'liked' key to the playlist with the specified value
            playlist['liked'] = liked
            # Return the updated dictionary
            return dictionary

# Dictionary containing the playlists created earlier
playlists: dict = {"playlist1": playlist_1, "playlist2": playlist_2, "playlist3": playlist_3}

# Update the playlists by adding a like to the "Road Trip" playlist
updated_playlists = add_like(playlists, "Road Trip", liked=True)

# Print the updated playlists
print(f"\n\t{updated_playlists}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------


# Exercise 2 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 2. Book Collection ↓\n")

# Function to add a book with the author's name and a list of titles
def add_book(author_name: str, titles: list) -> dict:
    # Create a new dictionary with the author's name as the key and the list of titles as the value
    new_playlist: dict = {author_name: titles}
    # Return the newly created dictionary
    return new_playlist

# Create dictionaries for authors and their respective books using the add_book function
author_1: dict = add_book("Author 1", ["book 1", "book 2"])
author_2: dict = add_book("Author 2", ["book 1", "book 2", "book 3"])
author_3: dict = add_book("Author 3", ["book 1", "book 2", "book 3", "book 4"])

# Print the dictionaries containing authors and their books
print(f"\t{author_1}\n\t{author_2}\n\t{author_3}")

# Create a dictionary containing authors and their books
authors: dict = {"author1": author_1, "author2": author_2, "author3": author_3}

# Function to delete a book by author's name from the dictionary of authors
def delete_book(dictionary: dict, author_name: str) -> dict:
    # Delete the entry with the specified author's name from the dictionary
    del dictionary[author_name]
    # Return the updated dictionary
    return dictionary

# Delete an author and their books from the authors dictionary
updated_authors: dict = delete_book(authors, "author2")

# Print the updated authors dictionary after deletion
print(f"\n\t{updated_authors}")


print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------


# Exercise 3 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 3. Personal Info ↓\n")

def build_profile(name: str, surname: str, occupation: str = None, location: str = None, age: int = None) -> dict:
    new_profile: dict = {"name": name, "surname": surname, "occupation": occupation, "location": location, "age": age}
    return new_profile

profile_1: dict = build_profile("Simone", "Antonelli", "Student", age=20)

print(f"\t{profile_1}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------


# Exercise 4 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 4. Event Organizer ↓\n")

# Function to plan an event with a name, list of participants, and time
def plan_event(name: str, participants: list, hour: str) -> dict:
    # Create a new dictionary representing the event with the given details
    new_event: dict = {"name": name, "participants": participants, "hour": hour}
    # Return the newly created event dictionary
    return new_event

# Plan an event called "Public Speech" with participants and a specific hour
event_1: dict = plan_event("Public Speech", ["p1", "p2", "p3"], "15:30")

# Print the details of the planned event
print(f"\t{event_1}")

# Create a dictionary to store events, initially containing one event
events: dict = {"event1": event_1}

# Function to modify an event's participants and time
def modify_event(dictionary: dict, event_name: str, new_participants: list, new_hour: str) -> dict:
    # Iterate through each key-value pair in the events dictionary
    for event_key, event_value in dictionary.items():
        # Check if the event name matches the specified event key
        if event_name == event_key:
            # Update the participants and hour of the event
            event_value["participants"] = new_participants
            event_value["hour"] = new_hour
            # Return the updated dictionary
            return dictionary
    # If the event name is not found, return the original dictionary
    return dictionary

# Modify the details of "event1" by adding new participants and changing the time
updated_event: dict = modify_event(events, "event1", ["p1", "p2", "p3", "p4", "p5"], "16:00")

# Print the updated event details
print(f"\t{updated_event}")

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------


# Exercise 5 ------------------------------------------------------------------------------------------------------------------
print("Exercise: 5. Shopping List ↓\n")

# Function to create a shopping list for a specific store with a list of items
def create_shopping_list(store_name: str, items: list) -> dict:
    # Create a new dictionary representing the shopping list with the store name and items
    new_shopping_list: dict = {"store_name": store_name, "items": items}
    # Return the newly created shopping list dictionary
    return new_shopping_list

# Create a shopping list for Walmart with some items
shopping_list_1: dict = create_shopping_list("Walmart", ["Pizza", "Pasta", "Flour"])

# Create a dictionary to store shopping lists, initially containing one shopping list
shopping_lists: dict = {"shopping_list1": shopping_list_1}

# Function to print the details of a specific shopping list
def print_shopping_list(dictionary: dict, shopping_list_name: str) -> None:
    # Iterate through each key-value pair in the shopping lists dictionary
    for shopping_list_key, shopping_list_value in dictionary.items():
        # Check if the shopping list name matches the specified shopping list key
        if shopping_list_name == shopping_list_key:
            # Print the details of the shopping list
            print(f"\n\t{shopping_list_value}")

# Print the details of the "shopping_list1"
print_shopping_list(shopping_lists, "shopping_list1")


print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------