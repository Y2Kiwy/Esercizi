# Exercise 8.1 -------------------------------------------------------------------------------------------------------------------
print("Exercise: 8-1. Creating an Abstract Class with Abstract Methods ↓\n")

from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass

import math

class Circle(Shape):

    def __init__(self, radius: float) -> None:
        super().__init__()
        self.radius: float = radius

    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):

    def __init__(self, edge1: float, edge2: float) -> None:
        super().__init__()
        self.edge1: float = edge1
        self.edge2: float = edge2

    def area(self):
        return self.edge1 * self.edge2
    
    def perimeter(self):
        return (self.edge1 * 2) + (self.edge2 * 2)

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.2 -------------------------------------------------------------------------------------------------------------------
print("Exercise: 8-2. Implementing Static Methods ↓\n")

class MathOperations():

    def __init__(self) -> None:
        pass

    @staticmethod
    def add(n1: float, n2: float) -> float:
        return n1 + n2
    
    @staticmethod
    def multiply (n1: float, n2: float) -> float:
        return n1 * n2

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.3 -------------------------------------------------------------------------------------------------------------------
print("Exercise: 8-3. Library Management System ↓\n")

class Book:
    
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title: str = title
        self.author: str = author
        self.isbn: str = isbn

    def __str__(self) -> str:
        return f"{self.title}, {self.author}, {self.isbn}"
    
    @classmethod
    def from_string(cls, book_str: str):
        book_param: list[str] = book_str.split(", ")
        return cls(book_param[0], book_param[1], book_param[2])
    
class Member:

    def __init__(self, name: str, member_id: str) -> None:
        self.name: str = name
        self.member_id: str = member_id
        self.borrowed_books: list = []

    def borrow_book(self, book: Book) -> None:
        self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        self.borrowed_books.remove(book)

    def __str__(self) -> str:
        borrowed_books_str = ', '.join(str(book) for book in self.borrowed_books)
        return f"{self.name}, {self.member_id}, Borrowed books: [{borrowed_books_str}]"
    
    @classmethod
    def from_string(cls, member_str: str) -> "Member":
        member_param: list[str] = member_str.split(", ")
        return cls(member_param[0], member_param[1])
    
class Library:
    total_books = 0

    def __init__(self) -> None:
        self.books: list[Book] = []
        self.members: list[Member] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        Library.total_books += 1

    def remove_book(self, book: Book) -> None:
        self.books.remove(book)
        Library.total_books -= 1

    def register_member(self, member: Member) -> None:
        self.members.append(member)

    def lend_book(self, book: Book, member: Member) -> None:
        if book in self.books and member in self.members:
            member.borrow_book(book)
            self.remove_book(book)

    def __str__(self) -> str:
        books_str = ', '.join(str(book) for book in self.books)
        members_str = ', '.join(str(member) for member in self.members)
        return f"Library has books: [{books_str}] and members: [{members_str}]"
    
    @classmethod
    def library_statistics(cls) -> None:
        print(f"Totale libri: {cls.total_books}")



def main():
    # Creare istanze di libri utilizzando il metodo from_string
    book1 = Book.from_string("La Divina Commedia, D. Alighieri, 999000666")
    book2 = Book.from_string("I Promessi Sposi, A. Manzoni, 888111333")
    book3 = Book.from_string("Il Nome della Rosa, U. Eco, 777222444")

    # Verificare la creazione dei libri
    print(f"\t{book1}")  # Output atteso: La Divina Commedia, D. Alighieri, 999000666
    print(f"\t{book2}")  # Output atteso: I Promessi Sposi, A. Manzoni, 888111333
    print(f"\t{book3}")  # Output atteso: Il Nome della Rosa, U. Eco, 777222444

    # Creare istanze di membri utilizzando il metodo from_string
    member1 = Member.from_string("Giovanni Rossi, 001")
    member2 = Member.from_string("Maria Bianchi, 002")

    # Verificare la creazione dei membri
    print(f"\t{member1}")  # Output atteso: Giovanni Rossi, 001, []
    print(f"\t{member2}")  # Output atteso: Maria Bianchi, 002, []

    # Creare una istanza della libreria
    library = Library()

    # Registrare i membri nella libreria
    library.register_member(member1)
    library.register_member(member2)

    # Aggiungere i libri alla libreria
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Verificare lo stato della libreria
    print(f"\t{library}")  # Output atteso: Libreria con lista di libri e membri

    # Prestare un libro ad un membro
    library.lend_book(book1, member1)

    # Verificare lo stato della libreria dopo aver prestato il libro
    print(f"\t{library}")  # Output atteso: Libreria aggiornata senza il libro prestato
    print(f"\t{member1}")  # Output atteso: Giovanni Rossi, 001, [La Divina Commedia]

    # Restituire il libro
    member1.return_book(book1)
    library.add_book(book1)

    # Verificare lo stato della libreria dopo la restituzione
    print(f"\t{library}")  # Output atteso: Libreria aggiornata con il libro restituito
    print(f"\t{member1}")  # Output atteso: Giovanni Rossi, 001, []

    # Stampare le statistiche della libreria
    Library.library_statistics()  # Output atteso: Totale libri: 3

if __name__ == "__main__":
    main()

print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------



# Exercise 8.4 -------------------------------------------------------------------------------------------------------------------
print("Exercise: 8-4. University Management System ↓\n")

class Person(ABC):

    def __init__(self, name: str, age: int) -> None:
        super().__init__()
        self.name: str = name
        self.age: int = age

    '''
    @abstractmethod
    def get_role():
        pass
    '''

    def __str__ (self):
        return f"{self.name}, {self.age} years old"
    
class Student(Person):

    def __init__(self, name: str, age: int, student_id: str) -> None:
        super().__init__(name, age)
        self.student_id: str = student_id
        self.courses: list = []

    def enroll(self, course: "Course") -> None:
        self.courses.append(course)

class Professor(Person):

    def __init__(self, name: str, age: int, professor_id : str, department: str) -> None:
        super().__init__(name, age)
        self.professor_id : str = professor_id 
        self.course: Course = None
        self.department: str = department

    def assign_to_course(self, course: "Course") -> None:
        self.course = course

class Course:

    def __init__(self, course_name: str, course_code: str) -> None:
        self.course_name: str = course_name
        self.course_code: str = course_code
        self.students: list[Student] = []
        self.professor: Professor = None

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def set_professor(self, professor: Professor) -> None:
        self.professor = professor

    def __str__(self) -> str:
        professor_name = self.professor.name if self.professor else "None"
        student_names = ", ".join(student.name for student in self.students)
        return f"Course: {self.course_name}, Code: {self.course_code}, Professor: {professor_name}, Students: [{student_names}]"
    
class Department:

    def __init__(self, department_name: str) -> None:
        self.department_name: str = department_name
        self.courses: list[Course] = []
        self.professors : list[Professor] = []

    def add_course(self, course: Course) -> None:
        self.courses.append(course)

    def add_professor(self, professor: Professor) -> None:
        self.professors.append(professor)

    def __str__(self) -> str:
            course_names = ", ".join(course.course_name for course in self.courses)
            professor_names = ", ".join(professor.name for professor in self.professors)
            return f"Department: {self.department_name}, Courses: [{course_names}], Professors: [{professor_names}]"
    
class University:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.departments: list[Department] = []
        self.students: list[Student] = []

    def add_department(self, department: Department) -> None:
        self.departments.append(department)

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def __str__(self) -> str:
        department_names = ", ".join(department.department_name for department in self.departments)
        student_names = ", ".join(student.name for student in self.students)
        return f"University: {self.name}, Departments: [{department_names}], Students: [{student_names}]"
    
def main():
    # Creazione delle istanze di dipartimenti
    comp_sci_dept = Department("Computer Science")
    physics_dept = Department("Physics")

    # Creazione delle istanze di professori
    prof_smith = Professor("John Smith", 45, "P001", "Computer Science")
    prof_doe = Professor("Jane Doe", 50, "P002", "Physics")

    # Creazione delle istanze di corsi
    comp_sci_course = Course("Computer Science Fundamentals", "CS101")
    physics_course = Course("Physics Mechanics", "PHY101")

    # Aggiunta dei corsi ai rispettivi dipartimenti
    comp_sci_dept.add_course(comp_sci_course)
    physics_dept.add_course(physics_course)

    # Assegnazione dei professori ai corsi
    comp_sci_course.set_professor(prof_smith)
    physics_course.set_professor(prof_doe)

    # Creazione delle istanze di studenti
    student1 = Student("Alice Johnson", 20, "S001")
    student2 = Student("Bob Smith", 22, "S002")

    # Iscrizione degli studenti ai corsi
    comp_sci_course.add_student(student1)
    comp_sci_course.add_student(student2)
    physics_course.add_student(student2)

    # Creazione dell'istanza dell'università
    university = University("My University")

    # Aggiunta dei dipartimenti all'università
    university.add_department(comp_sci_dept)
    university.add_department(physics_dept)

    # Aggiunta degli studenti all'università
    university.add_student(student1)
    university.add_student(student2)

    # Stampa lo stato dell'università
    print(f"\t{university}")


if __name__ == "__main__":
    main()


print("\n") # Formatting
# -------------------------------------------------------------------------------------------------------------------------------