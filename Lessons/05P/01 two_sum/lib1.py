def find_pairs(nums: list, to_find: int) -> list:
    """
    Finds pairs of numbers in a list that sum up to a given target.

    Args:
    - nums (list): A list of integers.
    - to_find (int): The target sum to find pairs for.

    Returns:
    - list: A list of pairs of numbers from 'nums' that sum up to 'to_find'.
    """
    # Initialize an empty list to store pairs of numbers that sum up to 'to_find'
    two_pairs: list = []

    # Iterate through each element in the list 'nums' using two nested loops
    for i in range(len(nums)):
        for j in range(len(nums)):
            # Skip if both indices are the same to avoid considering the same number twice
            if i == j:
                continue
            else:
                # Check if the sum of the numbers at indices 'i' and 'j' equals 'to_find'
                # and if the pair is not already present in 'two_pairs'
                if nums[i] + nums[j] == to_find and [nums[i], nums[j]] not in two_pairs:
                    # Add the pair [nums[i], nums[j]] to 'two_pairs'
                    two_pairs.append([nums[i], nums[j]])
                    # Continue to the next iteration
                    continue

    # Return the list of pairs that sum up to 'to_find'
    return two_pairs