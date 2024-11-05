points = int(input())
bonus = 0
if points <= 100: bonus = 5
elif 100 < points <= 1000: bonus = 0.2 * points
else: bonus = 0.10 * points

if points % 2 == 0: bonus += 1
if (points % 5 == 0) & (points % 2 != 0): bonus += 2
print(bonus)
print(points + bonus)