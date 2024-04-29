def score_checker(student_name: str, score: list) -> None:

    average_score = sum(score) / len(score)

    if average_score >= 60:
        print(f"\tStudent: {student_name} has passed the exam with an average score of: {average_score:.2f}")
    else:
        print(f"\tStudent: {student_name} has not passed the exam.")