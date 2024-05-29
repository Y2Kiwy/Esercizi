def score_checker(scores: list) -> int:
    '''Calculate the average score for a student exams scores and return an int

    Args:
        scores: list -> The scores of the student exams
    '''

    # Calculate the average of the list numbers
    average_score: int = sum(scores) / len(scores)

    return average_score