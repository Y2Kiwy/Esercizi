def new_product(name: str, price: float, quantity: int) -> dict:
    product: dict = {
        "name": name,
        "price": price,
        "quantity": quantity
        }
    
    return product


def add_product(products_list: list, name: str, price: float, quantity: int) -> list:
    new_product: dict = {
        "name": name,
        "price": price,
        "quantity": quantity
        }
    
    products_list.append(new_product)

    return products_list


def remove_product(products_list: list, name_to_remove: str) -> list:

    new_products_list: list = []

    for product in products_list:
        if product.get("name") != name_to_remove:
            new_products_list.append(product)

    return new_products_list


def view_product(products_list: list) -> None:

    cycle = 0

    for product_dict in products_list:

        cycle += 1

        print(f"\n\tProduct nº{cycle} info:")
        print(f"\t\tName: {product_dict['name']}")
        print(f"\t\tPrice: {product_dict['price']}")
        print(f"\t\tQuantity: {product_dict['quantity']}")


def shopcart_total(products_list: list, discount: float = 0.0, taxes: float = 0.0) -> float:

    total_cost: float = 0

    for product_dict in products_list:
        total_cost += (product_dict['price'] * product_dict['quantity'])

    taxes_value: float = total_cost * (taxes / 100)
    total_cost += taxes_value

    discount_value: float = total_cost * (discount / 100)
    total_cost -= discount_value

    return round(total_cost, 2)
