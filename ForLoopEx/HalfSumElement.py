import sys
max_number = -sys.maxsize
sum = 0
reps = int(input())
for i in range(0, reps):
    number = int(input())
    if number > max_number:
        max_number = number
    sum += number

if(sum - max_number == max_number):
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    sum = sum - max_number
    print(f"Diff = {abs(max_number - sum)}")