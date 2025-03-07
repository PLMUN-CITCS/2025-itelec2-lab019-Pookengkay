def get_student_score() -> float:
    """Gets a valid student score from user input."""
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
            continue

def calculate_grade(score: float) -> str:
    """Determines the grade based on the score."""
    if score >= 90:
        return 'A'
    elif score > 80:
        return 'B'
    elif score > 70:
        return 'C'
    elif score > 60:
        return 'D'
    else:
        return 'F'

if __name__ == "__main__":
    student_score = get_student_score()
    grade = calculate_grade(student_score)
    print(f"Your Grade is: {grade}")