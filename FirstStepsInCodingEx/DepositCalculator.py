deposit = float(input())
time = int(input())
tax = float(input())
print(deposit + (((deposit * (tax / 100)) / 12) * time))