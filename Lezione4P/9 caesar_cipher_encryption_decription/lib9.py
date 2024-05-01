def caesar_cipher(string: str, shift_value: int, decrypt: bool = False) -> str:

    '''
    Function to encrypt or decrypt a string using the Caesar cipher.

    Args:
        string (str): The string to encrypt or decrypt.
        shift_value (int): The number of positions to shift in the alphabet.
        decrypt (bool): If the function need to decrypt the string, False by default.

    Returns:
        str: The encrypted or decrypted string.
    '''

    # If decrypt flag is set, adjust the shift value to negative for decryption
    if decrypt:
        shift_value = -shift_value

    result = ''
    # Loop through each character in the input string
    for char in string:
        # Check if the character is in the alphabet
        if char.isalpha():
            # Apply shift to lowercase char
            if char.islower():
                result += chr((ord(char) - ord('a') + shift_value) % 26 + ord('a'))
            # Apply shift to uppercase char
            else:
                result += chr((ord(char) - ord('A') + shift_value) % 26 + ord('A'))
        # If the character is not in the alphabet, do not change it
        else:
            result += char
    return result