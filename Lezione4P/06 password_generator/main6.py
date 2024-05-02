from lib6 import *

password = pswd_generator(length=12, lower=True, upper=True, numbers=True, symbols=False)

print(f"\nGenerated password: {password}\n")