# Exercise 1: -----------------------------------------------------------------
def blackjack_hand_total(cards: list[int]) -> int:

    hand_total: int = 0
    ace_counter: int = 0

    # Sum every card of the hand except for aces
    for card in cards:
        if card != 1 and card != 11:
            hand_total += card

        # Keep track of how many aces do the hand has
        elif card == 1 or card == 11:
            ace_counter += 1

    # If only one ace and the hand total is under 10, add 11
    if ace_counter == 1 and hand_total <= 10:
        hand_total += 11
    
    # If only one ace and the hand total is above 11, add 1
    elif ace_counter == 1 and hand_total >= 11:
        hand_total += 1

    else:
        # For each aces calculate its value in base of hand total
        for _ in range(ace_counter):

            if hand_total <= 10:
                hand_total += 11

            else:
                hand_total -= 10
                hand_total += 1
        
    return hand_total
# -----------------------------------------------------------------------------


# Exercise 2: -----------------------------------------------------------------
import math
def construct_rectangle(area: int) -> list[int]:

    # Calculate the square root of the area and convert it to an integer
    l: int = int(math.sqrt(area))  

    # Calculate the width by dividing the area by the length
    w: int = int(area / l)  

    # Check if the product of length and width matches the target area
    while l * w != area:  
        # Increment the length
        l += 1  
        
        # Recalculate the width based on the new length
        w = int(area / l)  

    # Return a list containing the length and width of the constructed web page
    return [l, w]  
# -----------------------------------------------------------------------------


# Exercise 3: -----------------------------------------------------------------
import string
import copy

def word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:
    
    # Define a string containing all lowercase letters of the alphabet along with a space character.
    alphabet: str = string.ascii_lowercase + " "
    
    # Convert the input text to lowercase.
    text: str = text.lower()
    
    # Create a deep copy of the lowercase text.
    text_copy: str = copy.deepcopy(text)

    # Iterate over each character in the copied text.
    for char in text_copy:
        # Check if the character is not in the alphabet string.
        if not char in alphabet:
            # Replace the character with an empty string in the original text.
            text = text.replace(char, "")

    # Update the copy of the text
    text_copy: str = copy.deepcopy(text)

    # Iterate over each word in the copied text after splitting it.
    for word in text_copy.split():
        # Check if the word is in the list of stopwords.
        if word in stopwords:
            # Replace the word with an empty string in the original text.
            text = text.replace(word, "")

    # Initialize an empty dictionary to store word counts.
    word_counts = {}
    
    # Iterate over each word in the processed text after splitting it.
    for word in text.split():
        # Check if the word is not already in the word_counts dictionary.
        if word not in word_counts:
            # Add the word to the dictionary with a count of 1.
            word_counts[word] = 1
        else:
            # Increment the count of the word in the dictionary by 1.
            word_counts[word] += 1

    # Return the dictionary containing word counts.
    return word_counts
# -----------------------------------------------------------------------------


# Exercise 4: -----------------------------------------------------------------
import copy

def find_disappeared_numbers(nums: list[int]) -> list[int]:
    
    missing_nums: list[int] = []

    for x in range(1, len(nums) + 1):
        if x not in nums:
            missing_nums.append(x)

    return missing_nums

# -----------------------------------------------------------------------------


# Exercise 5: -----------------------------------------------------------------
def is_subsequence(s: str, t: str) -> bool:
    # Initialize indices for both strings
    s_index = 0
    t_index = 0
    
    # If the strings are equal, return True
    if s == t:
        return True
    else:
        # Iterate through both strings simultaneously
        while s_index < len(s) and t_index < len(t):
            # If characters match, move to the next character in s
            if s[s_index] == t[t_index]:
                s_index += 1
            # Move to the next character in t regardless
            t_index += 1
        
        # If s_index reaches the end of s, it means all characters in s were found in t in the correct order
        return s_index == len(s)

# -----------------------------------------------------------------------------


# Exercise 6: -----------------------------------------------------------------
def even_odd_pattern(nums: list[int]) -> list[int]:
    # Initialize empty lists to store even and odd numbers
    even_numbers: list = []
    odd_numbers: list = []
    
    # Iterate through the list of numbers
    for num in nums:
        # Check if the number is even
        if num % 2 == 0:
            # If even, append it to the list of even numbers
            even_numbers.append(num)
        else:
            # If odd, append it to the list of odd numbers
            odd_numbers.append(num)
    
    # Merge the lists of even and odd numbers
    merged_even_odd: list = even_numbers + odd_numbers
    
    # Return the merged list
    return merged_even_odd

def even_odd_pattern_v2(nums: list[int]) -> list[int]:
    return sorted(nums, key=lambda x: (x % 2, x))
# -----------------------------------------------------------------------------


# Exercise 7: -----------------------------------------------------------------
def prime_factors(n: int) -> list[int]:
    # Initialize an empty list to store the prime factors
    prime_factors: list = []
    # Initialize the divider to 2
    divider: int = 2
    
    # Continue the loop until n is greater than 1
    while n > 1:
        # Continue dividing n by divider until it"s no longer divisible
        while n % divider == 0:
            # If n is divisible by divider, append divider to the prime factors list
            prime_factors.append(divider)
            # Update n by dividing it by divider
            n //= divider
        
        # Move to the next potential divider
        divider += 1
    
    # Return the list of prime factors
    return prime_factors
# -----------------------------------------------------------------------------


# Exercise 8: -----------------------------------------------------------------
def third_max(nums: list[int]) -> int:
    # Remove duplicates by converting the list to a set and back to a list
    nums = list(set(nums))
    # Sort the list in ascending order
    nums.sort()
    
    # Check if there are at least three distinct numbers in the list
    if len(nums) >= 3:
        # Get the three largest numbers
        bigger_nums: list = nums[-3:]
        # Get the third largest number
        third_max: int = bigger_nums[-3]

        return third_max
    else:
        # If there are less than three distinct numbers, return the maximum number
        return max(nums)
# -----------------------------------------------------------------------------




# Exercise additional 1: ------------------------------------------------------
def find_lhs(nums: list[int]) -> int:
    
    possible_length: list = []
    counter_length1: int = 0
    counter_length2: int = 0
    repetition: bool = True
    
    for num1 in nums:
        for num2 in nums:

            print(f"Checking if {num1} and {num2} are close")

            if num1 == num2:
                counter_length1 += 1
                counter_length2 += 1
                print(f"Same, +1 -> cl1: {counter_length1} - cl2 -> {counter_length2}")

            elif num1 - num2 == 1:
                counter_length1 += 1
                repetition = False
                print(f"Close by 1, added +1 -> cl1: {counter_length1} - cl2 -> {counter_length2}")

            elif num1 - num2 == -1:
                counter_length2 += 1
                repetition = False
                print(f"Close by -1, added +1 -> cl1: {counter_length1} - cl2 -> {counter_length2}")

            else:
                print(f"Not close -> cl1: {counter_length1} - cl2 -> {counter_length2}")
        
        print(f"Length: -> cl1: {counter_length1} - cl2 -> {counter_length2}\n")

        if repetition:
            return 0

        elif counter_length1 >= counter_length2:
            possible_length.append(counter_length1)

        elif counter_length1 < counter_length2:
            possible_length.append(counter_length1)

        counter_length1: int = 0
        counter_length2: int = 0

    print(possible_length)

    return max(possible_length)

print(find_lhs([10,20,30,40,50]))
# -----------------------------------------------------------------------------


# Exercise additional 2: ------------------------------------------------------
def ransom(note: str, magazine: str) -> bool:
    # Convert the note and magazine strings to lowercase and remove spaces
    note_list: list = list(note.replace(" ", "").lower())
    magazine_list: list = list(magazine.replace(" ", "").lower())
    
    # Iterate through each character in the note list
    for char in note_list:
        # Check if the character is present in the magazine list
        if char in magazine_list:
            # If present, remove the character from the magazine list
            magazine_list.remove(char)
        else:
            # If the character is not present in the magazine list, return False
            return False

    # If all characters in the note are found in the magazine, return True
    return True
# -----------------------------------------------------------------------------


# Exercise additional 3: ------------------------------------------------------
def to_hex(num: int) -> str:
    # Dictionary mapping decimal values to hexadecimal characters
    hexadecimal_dict = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'a',
        11: 'b',
        12: 'c',
        13: 'd',
        14: 'e',
        15: 'f'
    }

    # Handle the case of negative numbers in input
    if num < 0:
    # Convert the negative number to its two's complement
        num = 2 ** 32 + num
        
    hexadecimal = '' 
    # Convert the decimal number to hexadecimal
    while(num > 0): 
        hex_value = num % 16
        # Prepend the hexadecimal character to the result string
        hexadecimal = hexadecimal_dict[hex_value] + hexadecimal 
        # Update the number by integer division with 16
        num = num // 16
      
    return hexadecimal
# -----------------------------------------------------------------------------


# Exercise additional 4: ------------------------------------------------------
def ugly_number(num: int) -> bool:
    # Check if the input number is less than or equal to 0
    if num <= 0:
        return False

    # List of ugly prime numbers
    ugly_prime: list = [2, 3, 5]
    
    # Iterate through each ugly prime number
    for ugly in ugly_prime:
        # Continue dividing the number by the current ugly prime until it's not divisible anymore
        while num % ugly == 0:
            num //= ugly
            
    # If the number becomes 1 after all divisions, it's an ugly number
    return num == 1
# -----------------------------------------------------------------------------