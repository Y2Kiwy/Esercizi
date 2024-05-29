from lib5 import *
import time


# Function 'new_item()'
item1: dict = new_item(code=1234, name="Engine lube", quantity=7, price=25.49)
item2: dict = new_item(code=1324, name="Akrapovic exshaust", quantity=1, price=1_899)
item3: dict = new_item(code=1432, name="Brembo pads", quantity=4, price=39.99)
items_list: list = [item1, item2, item3]

# Function 'new_dictionary()'
inventory1: dict = new_inventory(items_list)
print(f"\tNormal 'inventory1':")
for key, value in inventory1.items():
    print(f"\t{key}: {value}")
print()

# Function 'add_item()'
inventory1 = add_item(inventory1, code=1243, name="Brembo lever", quantity=2, price=229)
print(f"\tAdded one item to 'inventory1':")
for key, value in inventory1.items():
    print(f"\t{key}: {value}")
print()

# Function 'remove_item()'
inventory1 = remove_item(inventory1, code_to_remove=1234)
print(f"\tRemoved one item from 'inventory1':")
for key, value in inventory1.items():
    print(f"\t{key}: {value}")
print()

# Function 'search_item()'
akra_exhaust: dict = search_item(inventory1, code_to_search=1324)
print(f"\tAkrapovic exhaust from 'inventory1': {akra_exhaust}\n")

# Function 'update_item()'
item2_update: dict = new_item(code=1324, name="Mivv exshaust", quantity=1, price=799)
inventory1 = update_item(inventory1, code_to_update=1324, new_item=item2_update)
print(f"\tUpdate one item from 'inventory1':")
for key, value in inventory1.items():
    print(f"\t{key}: {value}")