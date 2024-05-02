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
    alphabet: str = string.ascii_lowercase + ' '
    
    # Convert the input text to lowercase.
    text: str = text.lower()
    
    # Create a deep copy of the lowercase text.
    text_copy: str = copy.deepcopy(text)

    # Iterate over each character in the copied text.
    for char in text_copy:
        # Check if the character is not in the alphabet string.
        if not char in alphabet:
            # Replace the character with an empty string in the original text.
            text = text.replace(char, '')
            # Print a message indicating the removal of the character.
            print(f"Removed {char}")

    # Update the copy of the text
    text_copy: str = copy.deepcopy(text)

    # Iterate over each word in the copied text after splitting it.
    for word in text_copy.split():
        # Check if the word is in the list of stopwords.
        if word in stopwords:
            # Replace the word with an empty string in the original text.
            text = text.replace(word, '')
            # Print a message indicating the removal of the word.
            print(f"Removed {word}")

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

stopwords = ['be']
text4 = "To be, or not to be, that is the question."
print(word_frequency(text4, stopwords))
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