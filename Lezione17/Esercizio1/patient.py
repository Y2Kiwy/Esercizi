from person import *

class Patient(Person):
    def __init__(self, first_name: str, last_name: str, id_code: str) -> None:
        super().__init__(first_name, last_name)
        if isinstance(id_code, str):
            self._id_code: str = id_code
        else:
            print(f"inserted id code is not a string -> {type(id_code)}")
            self._id_code: str = None

    def setIdCode(self, id_code: str) -> None:
        if isinstance(id_code, str):
            self._id_code = id_code
        else:
            print(f"inserted id code is not a string -> {type(id_code)}")

    def getIdCode(self) -> str:
        return self._id_code

    def patientInfo(self) -> None:
        print(f"Patient: {self.getName()} {self.getLastname()}\nID: {self._id_code}")
