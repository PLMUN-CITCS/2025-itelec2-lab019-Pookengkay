def calculate_grade(score: float) -> str:
  
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

    score = 85  
    grade = calculate_grade(score)  
    print(f"Enter your score: {score}")  
    print(f"Your Grade is: {grade}")  


if __name__ == "__main__":
    main()
