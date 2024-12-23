# Exercise 1: -----------------------------------------------------------------
def check_access(username: str, password: ..., is_active: bool) -> str:
    # Check if the username is "admin", the password is "12345", and the account is active
    if username == "admin" and str(password) == "12345" and is_active:
        return "Accesso consentito"  # Access granted if all conditions are met
    else:
        return "Accesso negato"  # Access denied otherwise
# -----------------------------------------------------------------------------


# Exercise 2: -----------------------------------------------------------------
def is_magic_number(num: int) -> bool:
    # Iterate through each digit of the number by converting it into a string
    for digit in str(num):
        # Check if the digit is "7"
        if digit == "7":
            return True  # Return True if "7" is found in the number
    
    # If no "7" is found after iterating through all digits, return False
    return False
# -----------------------------------------------------------------------------


# Exercise 3: -----------------------------------------------------------------
def rotate_left(elements: list, k: int):
    if not elements:
        return elements
    
    k %= len(elements)
    return elements[k:] + elements[:k]
# -----------------------------------------------------------------------------


# Exercise 4: -----------------------------------------------------------------
numbers: list[int] = [1, 2, 3, 4, 5] # Semicolon and round bracket removed

for i in numbers: # range() removed
    print('Number:', i) # Single quote not closed
# -----------------------------------------------------------------------------


# Exercise 5: -----------------------------------------------------------------
def calculate_average(numbers: list[int]) -> float:
    if len(numbers) != 0:
        return sum(numbers) / len(numbers) # Edited comparison method
    else:
        return 0 # Removed division by 0
# -----------------------------------------------------------------------------


# Exercise 6: -----------------------------------------------------------------
def remove_duplicates(input_list: list) -> list:
    # Create an empty list to store unique elements
    clear_list: list = []
    
    # Create an empty set to keep track of duplicate elements
    duplicates: set = set()
    
    # Iterate through each item in the input list
    for item in input_list:
        # Check if the item is not already in the set of duplicates
        if item not in duplicates:
            # If it's not a duplicate, add it to the clear_list
            clear_list.append(item)
            # Also add it to the set of duplicates to mark it as seen
            duplicates.add(item)
    
    # Return the list containing only unique elements
    return clear_list
# -----------------------------------------------------------------------------


# Exercise 7: -----------------------------------------------------------------
def check_parentheses(expression: str) -> bool:
    # Convert the expression into a list of characters and strip any leading/trailing whitespace
    expression: list = list(expression.strip())
    
    # Initialize a variable to track correctness
    correct: bool = True
    
    # Iterate through each character in the expression
    for char in expression:
        # Check if the character is an opening parenthesis
        if char == "(":
            # Get the index of the opening parenthesis
            check_index: int = expression.index(char)
            
            # Iterate from the index of the opening parenthesis till the end of the expression
            for x in range(check_index, len(expression)):
                # Check if there is a closing parenthesis
                if expression[x] == ")":
                    correct = True  # If found, set correct to True
                else:
                    correct = False  # If any character other than closing parenthesis is found, set correct to False
    
    return correct
# -----------------------------------------------------------------------------


# Exercise 8: -----------------------------------------------------------------
def count_isolated(input_list: list) -> int:
    # If the list has less than two elements, return the length of the list
    if len(input_list) < 2:
        return len(input_list)
    
    # Initialize a counter for isolated elements
    isolated_counter: int = 0
    
    # Check internal numbers of the list
    for x in range(1, len(input_list)-1):
        # If the current element is different from both its neighbors,
        # then it is an isolated element
        if input_list[x] != input_list[x-1] and input_list[x] != input_list[x+1]:
            isolated_counter += 1
        
    # Check the first and last elements separately
    if input_list[0] != input_list[-1]:
        # If the first element is different from the second, it's isolated
        if input_list[0] != input_list[1]:
            isolated_counter += 1
        # If the last element is different from the second last, it's isolated
        if input_list[-1] != input_list[-2]:
            isolated_counter += 1
            
    return isolated_counter
# -----------------------------------------------------------------------------


# Exercise 9: -----------------------------------------------------------------
def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    # Iterate through each element in the list of elements to remove
    for element in elements_to_remove:
        # Check if the element exists in the original set
        if element in original_set:
            # If it exists, remove it from the original set
            original_set.remove(element)
    
    # Return the modified original set after removing elements
    return original_set
# -----------------------------------------------------------------------------


# Exercise 10: -----------------------------------------------------------------
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    # Create a copy of the first dictionary to preserve its original content
    merged_dict = dict1.copy()

    # Iterate through each key-value pair in the second dictionary
    for key, value in dict2.items():
        # Check if the key already exists in the merged dictionary
        if key in merged_dict:
            # If the key exists, add the value from the second dictionary to the existing value
            merged_dict[key] += value
        else:
            # If the key does not exist, add the key-value pair from the second dictionary to the merged dictionary
            merged_dict[key] = value
    
    # Return the merged dictionary
    return merged_dict
# -----------------------------------------------------------------------------