import string
import random

def pswd_generator(length: int, **options) -> str:
     
    """
    Generate a random password with custom options.

    Parameters:
    - length (int): Length of the password to be generated.
    - **options: Additional keyword arguments to specify which character types to include in the password.
      Valid keyword arguments:
        - lower (bool): If True, include lowercase letters. Default: True.
        - upper (bool): If True, include uppercase letters. Default: True.
        - numbers (bool): If True, include numbers. Default: True.
        - symbols (bool): If True, include symbols. Default: True.

    Returns:
    - str: Generated password.
    """

    chars_dict: dict = {
        'lower': string.ascii_lowercase,
        'upper': string.ascii_uppercase,
        'numbers': string.digits,
        'symbols': string.punctuation
    }

    chars: str = ''
    for category, include in options.items():
        if include:
            chars += chars_dict[category]

    chars: str = ''.join(random.sample(chars, len(chars)))

    password: str = ''
    for _ in range(length):
        password += random.choice(chars)

    password = ''.join(random.sample(password, len(password)))

    return password