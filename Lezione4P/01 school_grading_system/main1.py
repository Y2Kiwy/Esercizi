from lib1 import *

students: list = ["Simone", "Gaia", "Alessio"]
scores: list = [[87, 34, 53], [89, 69, 97], [71, 93, 87]]

for student, score in zip(students, scores):
    average_score = score_checker(student_name=student, scores=score)

    if average_score >= 60:
        print(f"\tStudent: {student} has passed the exam with an average score of: {average_score:.2f}")
    else:
        print(f"\tStudent: {student} has not passed the exam.")