import unittest
from person import *
from doctor import *
from patient import *
from invoice import *

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("Mario", "Rossi")
        self.person.setAge(30)

    def test_init(self):
        self.assertEqual(self.person.getName(), "Mario")
        self.assertEqual(self.person.getLastname(), "Rossi")
        self.assertEqual(self.person.getAge(), 30)

    def test_setName(self):
        self.person.setName("Luigi")
        self.assertEqual(self.person.getName(), "Luigi")

    def test_setLastName(self):
        self.person.setLastName("Verdi")
        self.assertEqual(self.person.getLastname(), "Verdi")

    def test_setAge(self):
        self.person.setAge(25)
        self.assertEqual(self.person.getAge(), 25)

class TestDoctor(unittest.TestCase):
    def setUp(self):
        self.doctor = Doctor("Matteo", "Martelli", "Neurology", 150.0)

    def test_init(self):
        self.assertEqual(self.doctor.getName(), "Matteo")
        self.assertEqual(self.doctor.getLastname(), "Martelli")
        self.assertEqual(self.doctor.getAge(), 0)

    def test_isValidDoctor(self):
        self.doctor.setAge(30)
        self.assertEqual(self.doctor.isAValidDoctor(), False)

        self.doctor.setAge(57)
        self.assertEqual(self.doctor.isAValidDoctor(), True)

class TestPatient(unittest.TestCase):
    def setUp(self):
        self.patient = Patient("Giorgio", "Santoro", "GS01")

    def test_init(self):
        self.assertEqual(self.patient.getName(), "Giorgio")
        self.assertEqual(self.patient.getLastname(), "Santoro")
        self.assertEqual(self.patient.getAge(), 0)
        self.assertEqual(self.patient.getIdCode(), "GS01")

class TestInvoice(unittest.TestCase):

    doctor1 = Doctor("Marco", "Silvestri", "Neurology", 150.0)
    doctor1.setAge(48)

    patient1 = Patient("Alessia", "Romano", "AR02")
    patient2 = Patient("Giulia", "Bianchi", "GB03")
    patient3 = Patient("Luca", "Verdi", "LV04")
    patient4  = Patient("Michele", "Poretti", "MP05")

    def setUp(self):
        self.invoice = Invoice([self.patient1, self.patient2, self.patient3], self.doctor1)

    def test_init(self):
        self.assertEqual(self.invoice._doctor.getName(), "Marco")
        self.assertEqual(self.invoice._doctor.getLastname(), "Silvestri")
        self.assertEqual(self.invoice._doctor.getAge(), 48)
        self.assertEqual(self.invoice._doctor.getSpecialization(), "Neurology")
        self.assertEqual(self.invoice._doctor.getParcel(), 150.0)

        self.assertIn("Alessia Romano", [patient.getName() + " " + patient.getLastname() for patient in self.invoice._patients])
        self.assertIn("Giulia Bianchi", [patient.getName() + " " + patient.getLastname() for patient in self.invoice._patients])
        self.assertIn("Luca Verdi", [patient.getName() + " " + patient.getLastname() for patient in self.invoice._patients])

    def test_invoice(self):
        self.assertEqual(self.invoice.getInvoice(), 3)

    def test_salary(self):
        self.assertEqual(self.invoice.getSalary(), 450)

    def test_addPatient(self):
        self.invoice.addPatient(self.patient4)

        self.assertIn("Alessia Romano", [patient.getName() + " " + patient.getLastname() for patient in self.invoice._patients])
        self.assertIn("Giulia Bianchi", [patient.getName() + " " + patient.getLastname() for patient in self.invoice._patients])
        self.assertIn("Luca Verdi", [patient.getName() + " " + patient.getLastname() for patient in self.invoice._patients])
        self.assertIn("Michele Poretti", [patient.getName() + " " + patient.getLastname() for patient in self.invoice._patients])

    def test_removePatient(self):
        self.invoice.removePatient("GB03")

        self.assertIn("Alessia Romano", [patient.getName() + " " + patient.getLastname() for patient in self.invoice._patients])
        self.assertNotIn("Giulia Bianchi", [patient.getName() + " " + patient.getLastname() for patient in self.invoice._patients])
        self.assertIn("Luca Verdi", [patient.getName() + " " + patient.getLastname() for patient in self.invoice._patients])

if __name__ == '__main__':
    unittest.main()