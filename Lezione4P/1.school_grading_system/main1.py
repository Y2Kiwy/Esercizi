from lib1 import *

students: list = ["Simone", "Gaia", "Alessio"]
scores: list = [[87, 34, 53], [89, 69, 97], [71, 93, 87]]

for student, score in zip(students, scores):
    score_checker(student_name=student, score=score)