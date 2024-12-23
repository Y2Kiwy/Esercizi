def new_inventory(items: list) -> dict:
    inventory = {}
    for item in items:
        code = item.get("code")
        inventory[code] = item # The key for each dictionary is its own code for efficency improvment in 'remove_item()' function
    return inventory



def new_item(code: int, name: str, quantity: int, price: float) -> dict:
    item: dict = {
        "code": code,
        "name": name,
        "quantity": quantity,
        "price": price
    }

    return item


def add_item(inventory_dict: dict, code: int, name: str, quantity: int, price: float) -> dict:
    index = len(inventory_dict)
    new_item: dict = {
        "code": code,
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    inventory_dict[code] = new_item

    return inventory_dict



def remove_item(inventory_dict: dict, code_to_remove: int) -> dict:
    if code_to_remove in inventory_dict:
        del inventory_dict[code_to_remove]
        return inventory_dict
    

def search_item(inventory_dict: dict, code_to_search: int) -> dict:
    if code_to_search in inventory_dict:
        return inventory_dict[code_to_search]
    

def update_item(inventory_dict: dict, code_to_update: int, new_item: dict) -> dict:
    if code_to_update in inventory_dict:
        inventory_dict[code_to_update] = new_item
    return inventory_dict