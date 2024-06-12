class Person:
    def __init__(self, first_name: str, last_name: str) -> None:
        if isinstance(first_name, str):
            self._first_name: str = first_name
        else:
            print(f"Inserted first name is not a string -> {type(first_name)}")
            self._first_name: str = None

        if isinstance(last_name, str):
            self._last_name: str = last_name
        else:
            print(f"Inserted last name is not a string -> {type(last_name)}")
            self._last_name: str = None

        if isinstance(first_name, str) and isinstance(last_name, str):
            self._age: int = 0
        else:
            self._age: int = None

    def setName(self, first_name: str) -> None:
        if isinstance(first_name, str):
            self._first_name: str = first_name
        else:
            print(f"Inserted first name is not a string -> {type(first_name)}")

    def setLastName(self, last_name: str) -> None:
        if isinstance(last_name, str):
            self._last_name: str = last_name
        else:
            print(f"Inserted last name is not a string -> {type(last_name)}")

    def setAge(self, age: int) -> None:
        if isinstance(age, int):
            self._age = age
        else:
            print(f"Inserted age is not an int -> {type(age)}")

    def getName(self) -> str:
        return self._first_name

    def getLastname(self) -> str:
        return self._last_name

    def getAge(self) -> int:
        return self._age
    
    def greet(self) -> None:
        print(f"Hello, my name is {self._first_name} {self._last_name}! I am {self._age} years old!")

