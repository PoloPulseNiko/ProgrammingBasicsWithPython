actor_name = input()
academy_point = float(input())
total_points = academy_point
jurist_amount = int(input())
won = bool(False)
for i in range(0, jurist_amount):
    jurist_name = input()
    points = float(input())
    current_points = (len(jurist_name) * points) / 2
    total_points += current_points
    if total_points >= 1250.5:
        won = bool(True)
        break

if won:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {abs(1250.5 - total_points):.1f} more!")