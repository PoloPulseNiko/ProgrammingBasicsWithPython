turns = int(input())
beginning_points = int(input())
points = beginning_points
w_amount = 0
for i in range(0, turns):
    play = input()
    if play == "W":
        w_amount += 1
        points += 2000
    elif play == "F":
        points += 1200
    elif play == "SF":
        points += 720

print(f"Final points: {points}")
print(f"Average points: {int((points - beginning_points) / turns)}")
print(f"{((w_amount / turns) * 100):.2f}%")