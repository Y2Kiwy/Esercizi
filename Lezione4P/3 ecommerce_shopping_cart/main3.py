from lib3 import *

shopcart1: list = []

shopcart1.append(new_product(name="Tomato", price=0.02, quantity=53))
shopcart1.append(new_product(name="Steak", price=1.89, quantity=10))
shopcart1.append(new_product(name="Ketchup", price=2.99, quantity=2))

view_product(shopcart1)

shopcart1_total: float = shopcart_total(shopcart1)

print(f"\n\tThe total for your shopping cart is: {shopcart1_total}€")
