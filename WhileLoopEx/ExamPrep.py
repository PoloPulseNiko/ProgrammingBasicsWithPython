max_fails = int(input())
last_problem = ''
problem_count = 0
total_grades = 0
failed_problems = 0
failed = False
current_problem = input()
while current_problem != 'Enough':
    grade = float(input())
    total_grades += grade
    problem_count += 1
    last_problem = current_problem
    if grade <= 4:
        failed_problems += 1
    if failed_problems >= max_fails:
        print(f'You need a break, {failed_problems} poor grades.')
        failed = True
        break
    current_problem = input()

if not failed:
    print(f"Average score: {(total_grades / problem_count):.2f}")
    print(f"Number of problems: {problem_count}")
    print(f"Last problem: {last_problem}")