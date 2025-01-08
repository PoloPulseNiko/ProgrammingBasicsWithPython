student_name = input()
total_grades = 0
failed_years = 0
grade_level = 1

while grade_level <= 12:
    grade = float(input())

    if grade < 4.00:
        failed_years += 1
        if failed_years > 1:
            print(f"{student_name} has been excluded at {grade_level} grade")
            break
    else:
        total_grades += grade
        grade_level += 1

if grade_level > 12:
    average_grade = total_grades / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
