from lib9 import *

crypted_text = caesar_cipher(string="ciao, mi chiamo simone", shift_value=6, decrypt=False)

print(crypted_text)

decrypted_text = caesar_cipher(string=crypted_text, shift_value=6, decrypt=True)

print(decrypted_text)