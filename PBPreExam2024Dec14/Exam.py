student_count = int(input())
top_student_count = 0
good_student_count = 0
average_student_count = 0
failed_student_count = 0
total_grade = 0
for i in range(0, student_count):
    grade = float(input())
    total_grade += grade
    if grade >= 5.00:
        top_student_count += 1
    elif 4.00 <= grade <= 4.99:
        good_student_count += 1
    elif 3.00 <= grade <= 3.99:
        average_student_count += 1
    elif grade < 3.00:
        failed_student_count += 1

print(f'Top students: {((top_student_count / student_count) * 100):.2f}%')
print(f'Between 4.00 and 4.99: {((good_student_count / student_count) * 100):.2f}%')
print(f'Between 3.00 and 3.99: {((average_student_count / student_count) * 100):.2f}%')
print(f'Fail: {((failed_student_count / student_count) * 100):.2f}%')
print(f'Average: {(total_grade / student_count):.2f}')