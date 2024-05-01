def prime_numbers(limit: int) -> list:
    '''
    Finds all prime numbers within a specific range.

    Args:
        limit (int): The maximum number within which to search for prime numbers.

    Returns:
        list: A list containing all the prime numbers within the given range.
    '''

    # Generate a list of numbers from 2 to the specified limit (exclusive)
    numbers: list = list(range(1, limit))
    
    # Initialize a list to store non-prime numbers
    non_prime: list = []

    # Loop through each number in the range
    for number1 in numbers:

        # Check against each number in the range
        for number2 in numbers:

            # Skip if both numbers are the same
            if number1 == number2:
                continue

            # If number2 is divisible by number1, it's not a prime number
            elif number2 % number1 == 0:
                # If number2 is not already marked as non-prime, add it to the list
                if number2 not in non_prime:
                    non_prime.append(number2)
                    # Remove the non-prime number from the list of numbers
                    numbers.remove(number2)

    return numbers
