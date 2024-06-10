from doctor import *
from patient import *

class Invoice:
    def __init__(self, patients: list[Patient], doctor: Doctor) -> None:
        if doctor.isAValidDoctor():
            self._patients: list[Patient] = patients
            self._doctor: Doctor = doctor
            self._invoice: int = len(patients)
            self._salary: int = 0
        else:
            self._patients: list[Patient] = None
            self._doctor: Doctor = None
            self._invoice: int = None
            self._salary: int = None

    def getSalary(self) -> int:
        self._salary = self._doctor._parcel * self._invoice
        return self._salary

    def getInvoice(self) -> int:
        self._invoice: int = len(self._patients)
        return self._invoice

    def addPatient(self, newPatient: Patient) -> None:
        self._patients.append(newPatient)
        self.getInvoice()
        self.getSalary()
        print(f"Patient {newPatient.getIdCode()} added to doctor {self._doctor.getLastname()} list")

    def removePatient(self, oldPatientId: str):
        patients_copy: list[Patient] = self._patients
        for patient in patients_copy:
            if patient.getIdCode() == oldPatientId:
                self._patients.remove(patient)
                self.getInvoice()
                self.getSalary()
                print(f"Patient {oldPatientId} removed from doctor {self._doctor.getLastname()} list")
                break
