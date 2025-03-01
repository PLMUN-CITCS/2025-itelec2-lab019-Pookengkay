def get_student_score() -> float:
    """
    Purpose: Handles user input to obtain the student's score.
    
    Returns:
        float: The numerical score entered by the user.
    """
    while True:
        try:
            # Prompt user for input and ensure it can be converted to a float.
            score = float(input("Enter your score: "))
            # Check if the score is within a valid range (0 to 100)
            if 0 <= score <= 100:
                return score
            else:
                print("Error: Please enter a score between 0 and 100.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

def calculate_grade(score: float) -> str:
    """
    Purpose: Determines the letter grade based on the given score.
    
    Parameters:
        score (float): The student's numerical score.
    
    Returns:
        str: The letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    # Determine the grade based on score ranges
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    """
    Main program flow:
    - Calls get_student_score() to obtain the student's score.
    - Calls calculate_grade() to determine the grade.
    - Displays the grade to the user.
    """
    score = get_student_score()  # Get the score from the user
    grade = calculate_grade(score)  # Calculate the grade
    print(f"Your Grade is: {grade}")  # Display the grade

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
