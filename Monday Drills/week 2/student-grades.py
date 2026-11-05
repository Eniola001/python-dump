print("##### STUDENT-GRADES #####")


def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"

students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68]
]

for student in students:
    student_name = student[0]

    total_score = 0
    for score in student[1:]:
        total_score += score

    average = total_score / (len(student) - 1)

    grade = calculate_grade(average)

    print(f"{student_name} → Average: {average:.2f} → Grade: {grade}")
