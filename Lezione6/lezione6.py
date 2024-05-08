# Simone Antonelli
# 17/04/2024

print("Hello World!")

print("\n") # Formatting



# Teoria ---------------------------------------------------------------------
print("Theory: 1. Classes ↓\n")

class Person: # Calsses name must be capital for each first word letter and without any type of space

    # '__init__' is the costructor, 'self' is used to reference to the current instance of the class, others parameters are the class attributes
    def __init__(self, name: str, surname: str, ssn: str, birth_date: str, birth_place: str, gender: str) -> None:
        '''
        Args:
            - name (str): The name of the person
            - surname (str): The surname of the person
            - ssn (str): The Social Security Number of the person

        Return:
            - None
        '''
        
        # Define the class attributes (underscore before name is used for private)
        self._name: str = name              # Memorize 'name' of the instance
        self._surname: str = surname        # Memorize 'surname' of the instance
        self._ssn: str = ssn                # Memorize 'ssn' of the instance
        self.birth_date: str = birth_date   # Memorize 'birt_date' of the instance
        self.birth_place: str = birth_place # Memorize 'birth_date' of the instance
        self.gender: str = gender           # Memorize 'gender' of the instance

    # Function to get an instance variables (getter, used to obtain values of private class variables)
    def get_name(self) -> str:
        '''
        Get instance name
        
        Args:
            - None

        Return:
            - name (str): Collected object name
        '''
        return self._name
    def get_surname(self) -> str:
        '''
        Get instance surname
        
        Args:
            - None

        Return:
            - surname (str): Collected object surname
        '''
        return self._surname
    def get_ssn(self) -> str:
        '''
        Get instance ssn
        
        Args:
            - None

        Return:
            - ssn (str): Collected object ssn
        '''
        return self._ssn
    
    # Function to set an instance variables (setter, used to set values of private class variables)
    def set_name(self, name) -> None:
        '''
        Set instance name
        
        Args:
            - name (str): New name to asign

        Return:
            - None
        '''
        self._name = name
    def set_surname(self, surname) -> None:
        '''
        Set instance surname
        
        Args:
            - surname (str): New surname to asign

        Return:
            - None
        '''
        self._surname = surname
    def set_ssn(self, ssn) -> None:
        '''
        Set instance ssn
        
        Args:
            - ssn (str): New ssn to asign

        Return:
            - None
        '''
        self._ssn = ssn



# Create new object of class 'Person'
person_1: Person = Person(name="Simone", surname="Antonelli", ssn="NTNSMN", birth_date="17/08/2004", birth_place="Rome", gender="Male")

# Print 'person_1' attributes
print(f"\tPerson name before edit: {person_1.get_name()}")
print(f"\tPerson surname before edit: {person_1.get_surname()}")
print(f"\tPerson ssn before edit: {person_1.get_ssn()}")


# Edit 'person_1' name
person_1.set_name(name="Marco")
person_1.set_surname(surname="Antonelli")
person_1.set_ssn(ssn="NTNMRC")

print() # Formatting output

# Print edited 'person_1' name
print(f"\tPerson name after edit: {person_1.get_name()}")
print(f"\tPerson surname before edit: {person_1.get_surname()}")
print(f"\tPerson ssn before edit: {person_1.get_ssn()}")

print("\n") # Formatting
# ----------------------------------------------------------------------------

