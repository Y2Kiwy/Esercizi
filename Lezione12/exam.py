# Exercise 1: ----------------------------------------------------------------

class Contatore:

    def __init__(self) -> None:
        self.conteggio: int = 0

    def setZero(self) -> None:
        self.conteggio = 0

    def add1(self) -> None:
        self.conteggio += 1

    def sub1(self) -> None:
        if self.conteggio == 0:
            print("Non è possibile eseguire la sottrazione")
        else:
            self.conteggio -= 1

    def get(self) -> int:
        return self.conteggio
    
    def mostra(self) -> None:
        print(f"Conteggio attuale: {self.conteggio}")

# ----------------------------------------------------------------------------



# Exercise 2: ----------------------------------------------------------------

class RecipeManager:

    def __init__(self) -> None:
        self.recipes: dict[str, list[str]] = {}

    def create_recipe(self, name: str, ingredients: list[str]) -> dict:
        if name not in self.recipes:
            self.recipes[name] = ingredients
            return {name: self.recipes[name]}
        else:
            return "La ricetta già esiste"
        
    def add_ingredient(self, recipe_name: str, ingredient: str) -> None:
        if recipe_name in self.recipes:
            self.recipes[recipe_name].append(ingredient)
            return {recipe_name: self.recipes[recipe_name]}
        else:
            return "La ricetta non esiste"
        
    def remove_ingredient(self, recipe_name: str, ingredient: str): 
        if recipe_name in self.recipes:
            if ingredient in self.recipes[recipe_name]:
                self.recipes[recipe_name].remove(ingredient)
                return {recipe_name: self.recipes[recipe_name]}
            else:
                return "L'ingrediente non esiste"
        else:
            return "La ricetta non esiste"
        
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str):
        if recipe_name in self.recipes:
            if old_ingredient in self.recipes[recipe_name]:
                self.recipes[recipe_name] = [ingredient.replace(old_ingredient, new_ingredient) for ingredient in self.recipes[recipe_name]]
                return {recipe_name: self.recipes[recipe_name]}
            else:
                return "L'ingrediente non esiste"
        else:
            return "La ricetta non esiste"
        
    def list_recipes(self) -> None:
        return f"{list(self.recipes.keys())}"

    def list_ingredients(self, recipe_name: str):
        if recipe_name in self.recipes:
            return self.recipes[recipe_name]
        else:
            return "La ricetta non esiste"
        
    def search_recipe_by_ingredient(self, ingredient: str):
        possible_recipes: dict[str, list[str]] = {}
        for recipe_name, recipe_ingredients in self.recipes.items():
            if ingredient in recipe_ingredients:
                possible_recipes[recipe_name] = recipe_ingredients
        if possible_recipes:
            return possible_recipes
        else:
            return f"Nessuna ricetta trovata con l'ingrediente {ingredient}"

# ----------------------------------------------------------------------------



# Exercise 3: ----------------------------------------------------------------

class Veicolo:

    def __init__(self, marca: str, modello: str, anno: int) -> None:
        self.marca: str = marca
        self.modello: str = modello
        self.anno: int = anno

    def descrivi_veicolo(self) -> None:
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")

class Auto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, n_porte: int) -> None:
        super().__init__(marca, modello, anno)
        self.n_porte: int = n_porte

    def descrivi_veicolo(self) -> None:
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.n_porte}")

class Moto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, tipo: str) -> None:
        super().__init__(marca, modello, anno)
        self.tipo: int = tipo

    def descrivi_veicolo(self) -> None:
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")

# ----------------------------------------------------------------------------



# Exercise 4: ----------------------------------------------------------------



# ----------------------------------------------------------------------------