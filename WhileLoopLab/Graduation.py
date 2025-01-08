failed = bool(False)
name = input()
fails = 0
year = 1
while year <= 12:
    grade = float(input())
    if grade < 4.00:
        fails += 1
        if fails >= 2:
            failed = bool(True)
