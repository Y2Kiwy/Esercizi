# Simone Antonelli
# 17/04/2024

print("Hello World!")

print("\n") # Formatting



# Teoria ---------------------------------------------------------------------
print("Theory: 1. Classes ↓\n")

import time

start: time = time.time()
import re
import pandas as pd
from pathlib import Path
end: time = time.time()
print(f"\tElapsed time to import needed libs: {end - start}") # Virtual machines (2 cores and 10GB ram) is a bit slow

CSV_PATH = Path(__file__).parent / "gi_db_comuni-2024-04-10-a9b29" / "csv"

class Person:

    def __init__(self, name: str, surname: str, birth_date: str, birth_place: str, gender: str) -> None:

        self._name: str = name
        self._surname: str = surname
        self._birth_date: str = birth_date
        self._birth_place: str = birth_place
        self._gender: str = gender

        self._ssn: str = self.compute_ssn(name, surname, birth_date, birth_place, gender)


    def get_name(self) -> str:
        return self._name
    def set_name(self, value: str) -> None:
        self._name = value
        self._ssn = self.compute_ssn(self._name, self._surname, self._birth_date, self._birth_place, self._gender)


    def get_surname(self) -> str:
        return self._surname
    def set_surname(self, value: str) -> None:
        self._surname = value
        self._ssn = self.compute_ssn(self._name, self._surname, self._birth_date, self._birth_place, self._gender)


    def get_birth_date(self) -> str:
        return self._birth_date
    def set_birth_date(self, value: str) -> None:
        self._birth_date = value
        self._ssn = self.compute_ssn(self._name, self._surname, self._birth_date, self._birth_place, self._gender)


    def get_birth_place(self) -> str:
        return self._birth_place
    def set_birth_place(self, value: str) -> None:
        self._birth_place = value
        self._ssn = self.compute_ssn(self._name, self._surname, self._birth_date, self._birth_place, self._gender)


    def get_gender(self) -> str:
        return self._gender
    def set_gender(self, value: str) -> None:
        self._gender = value
        self._ssn = self.compute_ssn(self._name, self._surname, self._birth_date, self._birth_place, self._gender)


    def get_ssn(self) -> str:
        return self._ssn


    def compute_ssn(self, name: str, surname: str, birth_date: str, birth_place: str, gender: str) -> str:
        
        first_6: str = self.compute_name_surname(name, surname)

        birth_day_5: str = self.compute_birthday(birth_date, gender)

        birth_place_4: str = self.compute_cadastral_code(birth_place)

        digits_15: str = ''.join([first_6, birth_day_5, birth_place_4])

        control_1: str = self.compute_control(digits_15)

        return ''.join([first_6, birth_day_5, birth_place_4, control_1])


    def compute_name_surname(self, name: str, surname: str) -> str:

        first_6: str = self.extract_surname(surname) + self.extract_name(name)

        return first_6


    def extract_surname(self, surname: str) -> str:
        surname = surname.replace(" ", "").upper()
    
        surname_consonants = re.findall(r'[BCDFGHJKLMNPQRSTVWXYZ]', surname)
        
        if len(surname_consonants) < 3:
            surname_vowels = re.findall(r'[AEIOU]', surname)
            needed_letters = 3 - len(surname_consonants)
            surname_consonants += surname_vowels[:needed_letters]
        
        if len(surname_consonants) < 3:
            surname_consonants += ['X'] * (3 - len(surname_consonants))
        
        return ''.join(surname_consonants[:3])


    def extract_name(self, name: str) -> str:
        name = name.replace(" ", "").upper()

        name_consonants = re.findall(r'[BCDFGHJKLMNPQRSTVWXYZ]', name)

        if len(name_consonants) >= 4:
            return ''.join([name_consonants[0], name_consonants[2], name_consonants[3]])
        
        elif len(name_consonants) == 3:
            return ''.join(name_consonants[:3])
        
        else:

            if len(name_consonants) < 4:
                name_vowels = re.findall(r'[AEIOU]', name)
                remaining_letters = 4 - len(name_consonants)
                name_consonants += name_vowels[:remaining_letters]
            
            if len(name_consonants) < 4:
                name_consonants += ['X'] * (4 - len(name_consonants))
            
            return ''.join(name_consonants[:3])


    def compute_birthday(self, birth_date: str, gender: str) -> str:

        y_m_d: list[str] = birth_date.split("-")

        year: str = y_m_d[0][-2:]

        months_letters: dict = {
            "01": "A",
            "02": "B",
            "03": "C",
            "04": "D",
            "05": "E",
            "06": "H",
            "07": "L",
            "08": "M",
            "09": "P",
            "10": "R",
            "11": "S",
            "12": "T"
        }

        month: str = months_letters[y_m_d[1]]

        if "f" in gender.lower():
            day: str = int(y_m_d[2]) + 40
        else:
            day: str = y_m_d[2]


        return ''.join([year, month, str(day)])
    

    def compute_cadastral_code(self, birth_place: str) -> str:

        cadastral_codes: pd.DataFrame = pd.read_csv(CSV_PATH / "gi_comuni_nazioni_cf.csv", delimiter=';')

        city_name_corrispondency = cadastral_codes[cadastral_codes['denominazione_ita'] == birth_place.upper()]

        # Se trova una corrispondenza, restituisci il codice catastale
        if not city_name_corrispondency.empty:
            codice_catastale = city_name_corrispondency.iloc[0]['codice_belfiore']

            return str(codice_catastale)

    def compute_control(self, digits_15: str) -> str:

        even_nums: dict = {
            " ": " ",
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
            'H': 7,
            'I': 8,
            'J': 9,
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'K': 10,
            'L': 11,
            'M': 12,
            'N': 13,
            'O': 14,
            'P': 15,
            'Q': 16,
            'R': 17,
            'S': 18,
            'T': 19,
            'U': 20,
            'V': 21,
            'W': 22,
            'X': 23,
            'Y': 24,
            'Z': 25
        }

        odd_nums = {
            " ": " ",
            'A': 1,
            'B': 0,
            'C': 5,
            'D': 7,
            'E': 9,
            'F': 13,
            'G': 15,
            'H': 17,
            'I': 19,
            'J': 21,
            '0': 1,
            '1': 0,
            '2': 5,
            '3': 7,
            '4': 9,
            '5': 13,
            '6': 15,
            '7': 17,
            '8': 19,
            '9': 21,
            'K': 2,
            'L': 4,
            'M': 18,
            'N': 20,
            'O': 11,
            'P': 3,
            'Q': 6,
            'R': 8,
            'S': 12,
            'T': 14,
            'U': 16,
            'V': 10,
            'W': 22,
            'X': 25,
            'Y': 24,
            'Z': 23
        }

        control_digits: dict = {
            0: 'A',
            1: 'B',
            2: 'C',
            3: 'D',
            4: 'E',
            5: 'F',
            6: 'G',
            7: 'H',
            8: 'I',
            9: 'J',
            10: 'K',
            11: 'L',
            12: 'M',
            13: 'N',
            14: 'O',
            15: 'P',
            16: 'Q',
            17: 'R',
            18: 'S',
            19: 'T',
            20: 'U',
            21: 'V',
            22: 'W',
            23: 'X',
            24: 'Y',
            25: 'Z'
        }

        digits_15: str = " " + digits_15

        digits_num_sum: int = 0

        for i in range(1, len(digits_15)):

            if i % 2 == 0:
                digits_num_sum += even_nums[digits_15[i]]
                #print(f"\tChar {digits_15[i]} in position {i} (even) has a value of {even_nums[digits_15[i]]}")

            else:
                digits_num_sum += odd_nums[digits_15[i]]
                #print(f"\tChar {digits_15[i]} in position {i} (odd) has a value of {odd_nums[digits_15[i]]}")


        control_digits_id: int = digits_num_sum % 26

        #print(f"\n\tDigits relative value sum: {digits_num_sum} % 26 = {control_digits_id}")

        return control_digits[control_digits_id]


# p1: Person = Person("Simone", "Antonelli", "2004-08-17", "Roma", "Male")

# print(f"\tThe ssn for {p1.get_name()} {p1.get_surname()} is: {p1.get_ssn()}")

# p1.set_name("Sophia")
# p1.set_birth_date("2031-06-18")
# p1.set_gender("f")

# print(f"\tThe ssn for edited person {p1.get_name()} {p1.get_surname()} is: {p1.get_ssn()}")



p2: Person = Person("Leonardo", "Brussani", "2004-07-24", "Roma", "male")

print(f"\n\tThe ssn for {p2.get_name()} {p2.get_surname()} is: {p2.get_ssn()}")


print("\n") # Formatting
# ----------------------------------------------------------------------------



# Teoria esercizio 3 ---------------------------------------------------------

print("Theory exercise: 3. Animals ↓\n")

class Animal:
    def __init__(self, name: str, legs: int) -> None:
        self._name = name
        self._legs = legs

    def get_all(self) -> str:
        return f"\tObject name: {self._name}\n\tObject legs: {self._legs}"

    def get_name(self) -> str:
        return self._name
    def set_name(self, value: str) -> None:
        self._name = value


    def get_legs(self) -> int:
        return self._legs
    def set_legs(self, value: int) -> None:
        if value >= 0:
            self._legs = value
        else:
            raise ValueError("Il numero di zampe non può essere negativo.")



a1: Animal = Animal("Cane", 4)

print(f"\ta1 name: {a1.get_name()}")

a2: Animal = Animal("Millepiedi", 1000)

print(f"\n\ta2 name: {a2.get_name()}")

a2.set_legs(100)

print(f"\n{a2.get_all()}")

print("\n") # Formatting
# ----------------------------------------------------------------------------