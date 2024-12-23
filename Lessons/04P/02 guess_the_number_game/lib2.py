from random import randint

def guess_number(min_range: int, max_range: int, max_attempts: int):   
    """
    Guess the secret number within a given range with limited attempts.

    Args:
        min_range (int): The lower bound of the range.
        max_range (int): The upper bound of the range.
        max_attempts (int): The maximum number of attempts allowed.

    Returns:
        None
    """
    secret_number = randint(min_range, max_range)
    
    for attempt in range(max_attempts, 0, -1):
        guess = int(input(f"\tGuess the number between {min_range} and {max_range} (attempts left: {attempt}): "))

        if guess == secret_number:
            print(f"\n\tCongratulations! You guessed the number {secret_number}!")
            return
        elif guess < secret_number:
            print("\tToo low!", end=" ")
        elif guess > secret_number:
            print("\tToo high!", end=" ")
        
        print(f"Try again. (Attempts left: {attempt - 1})\n")

    print(f"\tSorry, you have used all {max_attempts} attempts. The correct number was {secret_number}.")
