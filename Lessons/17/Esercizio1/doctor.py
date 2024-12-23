from person import *

class Doctor(Person):
    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float) -> None:
        super().__init__(first_name, last_name)

        if isinstance(specialization, str):
            self._specialization: str = specialization
        else:
            print(f"Inserted specialization is not a string -> {type(specialization)}")
            self._specialization: str = None

        if isinstance(parcel, float):
            self._parcel: float = parcel
        else:
            print(f"Inserted parcel is not a float -> {type(parcel)}")
            self._parcel: str = None

    def setSpecialization(self, specialization: str) -> None:
        if isinstance(specialization, str):
            self._specialization = specialization
        else:
            print(f"Inserted specialization is not a string -> {type(specialization)}")

    def setParcel(self, parcel: float) -> None:
        if isinstance(parcel, float):
            self._parcel = parcel
        else:
            print(f"Inserted parcel is not a float -> {type(parcel)}")

    def getSpecialization(self) -> str:
        return self._specialization

    def getParcel(self) -> float:
        return self._parcel
    
    def isAValidDoctor(self) -> bool:
        if self.getAge() > 30:
            print(f"Doctor {self.getName()} {self.getLastname()} is valid!")
            return True
        else:
            print(f"Doctor {self.getName()} {self.getLastname()} is not valid!")
            return False

    def doctorGreet(self) -> None:
        self.greet()
        print(f"I am a doctor in {self._specialization}")