# Exercise 18.1 -------------------------------------------------------------------------------------------------------------------
print("Exercise: 18-1. Safe Square Root ↓\n")

import math

def safe_sqrt(number: float) -> float:

    if number >= 0:
        result: float = math.sqrt(number)
    else:
        raise ValueError("Value cannot be negative")
# -------------------------------------------------------------------------------------------------------------------------------