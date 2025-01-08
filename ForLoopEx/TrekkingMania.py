p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
total = 0
reps = int(input())
for i in range(0, reps):
    number = int(input())
    if number <= 5:
        p1 += number
    elif 6 <= number <= 12:
        p2 += number
    elif 13 <= number <= 25:
        p3 += number
    elif 26 <= number <= 40:
        p4 += number
    elif number >= 41:
        p5 += number

    total += number

print(f"{((p1 / total) * 100):.2f}%")
print(f"{((p2 / total) * 100):.2f}%")
print(f"{((p3 / total) * 100):.2f}%")
print(f"{((p4 / total) * 100):.2f}%")
print(f"{((p5 / total) * 100):.2f}%")