# Exercise 1: -----------------------------------------------------------------
def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    """
    Removes elements from a list based on the provided dictionary.

    Args:
    - lista (list[int]): The list from which elements are to be removed.
    - da_rimuovere (dict[int:int]): A dictionary containing elements to be removed and their occurrences.

    Returns:
    - list[int]: The list with elements removed as per the provided dictionary.
    """
    # Create a copy of the original list
    lista_copy: list[int] = lista

    # Extract the element to be removed and its occurrence count from the dictionary
    number_to_remove: int = int(list(da_rimuovere.keys())[0])
    time_to_remove: int = int(list(da_rimuovere.values())[0])

    # Initialize a counter to keep track of removed elements
    removed_counter: int = 0
    
    # Initialize an index for iteration through the list
    i: int = 0

    # Iterate through the list elements
    while i < len(lista):
        print(f"Checking index: {i}")
        # Check if the current element matches the element to be removed and if the occurrence count hasn't been exceeded
        if lista_copy[i] == number_to_remove and removed_counter < time_to_remove:
            print(f"Found correspondence between 'number_to_remove': {number_to_remove} and list index: {i}: {lista_copy[i]}")
            print(f"Occurrences remaining to delete: {time_to_remove - removed_counter}")
            # Delete the element from the list and increment the removed elements counter
            del lista_copy[i]
            removed_counter += 1
        else:
            # Move to the next element in the list
            i += 1

    # Return the modified list with elements removed
    return lista_copy
# ----------------------------------------------------------------------------

# Exercise 2: -----------------------------------------------------------------
def aggrega_voti(voti: list[dict]) -> dict[str, list[int]]:
    """
    Aggregates votes for each student from a list of dictionaries.

    Args:
    - voti (list[dict]): A list of dictionaries containing student names and their respective votes.

    Returns:
    - dict[str, list[int]]: A dictionary where each key represents a student name and the corresponding value is a list of their votes.
    """
    # Initialize an empty dictionary to store aggregated votes for all students
    all_students_votes: dict[str, list[int]] = {}
    
    # Iterate through each dictionary in the list of votes
    for student_dict in voti:
        # Extract the student name and vote from the dictionary
        student_name: str = student_dict['nome']  
        student_vote: int = student_dict['voto']
        
        # Check if the student name is already in the aggregated votes dictionary
        if student_name not in all_students_votes:
            # If not, create a new empty list for the student's votes
            all_students_votes[student_name] = []
            
        # Append the student's vote to their list of votes
        all_students_votes[student_name].append(student_vote)
    
    # Return the dictionary containing aggregated votes for all students
    return all_students_votes
# ----------------------------------------------------------------------------

# Exercise 3: -----------------------------------------------------------------
def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    """
    Filters and maps products based on their prices.

    Args:
    - prodotti (dict[str:float]): A dictionary where keys are product names and values are their prices.

    Returns:
    - list[str:float]: A dictionary containing only the expensive products with discounted prices.
    """
    # Extract product names and prices into separate lists
    products_name: list[str] = list(prodotti.keys())
    products_price: list[float] = list(prodotti.values())

    # Initialize an empty dictionary to store expensive products with discounted prices
    expensive_products: dict = {}

    # Iterate through the products' prices
    for i in range(len(products_price)):
        # Check if the product price is greater than $20.00
        if products_price[i] > 20.00:
            # Calculate the discounted price for expensive products (10% off)
            discounted_price = products_price[i] - (products_price[i] * 0.1)
            # Add the expensive product and its discounted price to the dictionary
            expensive_products[products_name[i]] = discounted_price

    # Return the dictionary containing expensive products with discounted prices
    return expensive_products
# ----------------------------------------------------------------------------

# Exercise 4: -----------------------------------------------------------------
def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    new_contact: dict = {
        "profile": name,
        "email": email,
        "telefono": telefono
    }
    return new_contact

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    if email:
        dictionary["email"] = email
    if telefono:
        dictionary["telefono"] = telefono

    return dictionary
# ----------------------------------------------------------------------------