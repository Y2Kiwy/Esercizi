class Room:

    def __init__(self, id: int, floor: int, seats: int) -> None:
        self.id: int = id
        self.floor: int = floor
        self.seats: int = seats
        self.area: int = self.seats * 2

    def get_id(self) -> int:
        return self.id
    
    def get_floor(self) -> int:
        return self.floor
    
    def get_seats(self) -> int:
        return self.seats
    
    def get_area(self) -> int:
        return self.area
    

class Building:

    def __init__(self, name: str, address: str, floors: tuple[int]) -> None:
        self.name: str = name
        self.address: str = address
        self.floors: int = floors
        self.rooms: list[Room] = []

    def get_floors(self) -> int:
        return self.floors
    
    def get_rooms(self) -> list[Room]:
        return self.rooms
    
    def add_room(self, room: Room) -> None:
        if self.floors[0] <= room.floor <= self.floors[1] :
            if not room in self.rooms:
                self.rooms.append(room)

    def area(self) -> int:
        return int(sum(room.get_area() for room in self.rooms))
    


class Person:

    def __init__(self, cf: str, name: str, surname: str, age: int):
        self.cf: str = cf
        self.name: str = name
        self.surname: str = surname
        self.age: int = age

class Student(Person):

    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)
        self.group: "Group" = None

    def set_group(self, group: "Group") -> None:
        self.group = group


class Lecturer(Person):

    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)


class Group:
    
    def __init__(self, name: str, limit: int):
        self.name: str = name
        self.limit: int = limit
        self.students: list[Student] = []
        self.lecturers: list[Lecturer] = []

    def get_name(self) -> str:
        return self.name

    def get_limit(self) -> int:
        return self.limit

    def get_students(self) -> list[Student]:
        return self.students
    
    def get_limit_lecturers(self) -> int:
        if len(self.students) <= 10:
            return 1
        else:
            return len(self.students) // 10

    def add_student(self, student: Student) -> None:
        if len(self.students) < self.limit:
            self.students.append(student)

    def add_lecturer(self, lecturer: Lecturer) -> None:
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)



class Course:
    
    def __init__(self, name: str):
        self.name: str = name
        self.groups: list[Group] = []

    def register(self, student: Student) -> None:
        for group in self.groups:
            if len(group.students) < group.limit:
                group.add_student(student)
                return

    def get_groups(self):
        return self.groups

    def add_group(self, group: Group):
        self.groups.append(group)





# Creazione degli edifici
smi = Building(name="SMI", address="Via Sierra Nevada 60", floors=(-2, 3))
armellini = Building(name="ITIS", address="Basilica San Paolo", floors=(0, 4))

# Aggiunta delle stanze all'edificio smi
smi.add_room(Room(id="123", floor=3, seats=32))
smi.add_room(Room(id="333", floor=0, seats=42))
smi.add_room(Room(id="111", floor=6, seats=32))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
smi.add_room(Room(id="111", floor=-1, seats=32))

# Aggiunta delle stanze all'edificio smi
armellini.add_room(Room(id="567", floor=3, seats=22))
armellini.add_room(Room(id="888", floor=0, seats=32))
armellini.add_room(Room(id="999", floor=6, seats=22))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
armellini.add_room(Room(id="999", floor=2, seats=22))

# Output dei risultati
print("### SMI ###")
print(f"Stanze nell'edificio SMI: {[room.get_id() for room in smi.get_rooms()]}")
print(f"Area totale dell'edificio SMI: {smi.area()} m²")
print("### ARMELLINI ###")
print(f"Stanze nell'edificio ITIS: {[room.get_id() for room in armellini.get_rooms()]}")
print(f"Area totale dell'edificio ITIS: {armellini.area()} m²")


# Creazione dei gruppi
fullstack = Group(name="Fullstack", limit=1)
cloud = Group(name="Cloud", limit=10)
cyber = Group(name="Cyber", limit=10)

# Creazione di un corso e aggiunta dei gruppi al corso
course = Course(name="Python")
course.add_group(fullstack)
course.add_group(cloud)
course.add_group(cyber)

# Registrazione degli studenti al corso
course.register(Student(cf="1234", name="Flavio", surname="Maggi", age=29))
course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))
course.register(Student(cf="9101", name="Luca", surname="Bianchi", age=25))
course.register(Student(cf="2345", name="Marco", surname="Rossi", age=32))
course.register(Student(cf="6789", name="Paolo", surname="Verdi", age=38))
course.register(Student(cf="1011", name="Giulia", surname="Neri", age=21))
course.register(Student(cf="3456", name="Anna", surname="Gialli", age=27))
course.register(Student(cf="7890", name="Maria", surname="Blu", age=35))
course.register(Student(cf="1112", name="Sara", surname="Viola", age=23))
course.register(Student(cf="4567", name="Giovanni", surname="Arancione", age=31))
course.register(Student(cf="8901", name="Andrea", surname="Rosa", age=24))
course.register(Student(cf="1123", name="Matteo", surname="Marrone", age=30))
course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))

print("### COURSE DETAILS ###")
print(f"Studenti nel gruppo Fullstack: {[student.cf for student in fullstack.get_students()]}")
print(f"Studenti nel gruppo Cloud: {[student.cf for student in cloud.get_students()]}")
print(f"Studenti nel gruppo Cyber: {[student.cf for student in cyber.get_students()]}")