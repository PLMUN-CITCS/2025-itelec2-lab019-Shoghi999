def get_student_score():
    return float(input("Enter your score: "))

def calculate_grade(score):
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
    score = get_student_score()
    print("Your Grade is:", calculate_grade(score))

if __name__ == "__main__":
    main()