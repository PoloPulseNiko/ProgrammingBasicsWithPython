jury_count = int(input())

total_sum = 0
presentation_count = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break

    presentation_count += 1
    presentation_sum = 0

    for _ in range(jury_count):
        grade = float(input())
        presentation_sum += grade

    average_grade = presentation_sum / jury_count
    total_sum += average_grade
    print(f"{presentation_name} - {average_grade:.2f}.")

final_assessment = total_sum / presentation_count
print(f"Student's final assessment is {final_assessment:.2f}.")