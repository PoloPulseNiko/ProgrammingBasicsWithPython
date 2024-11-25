repetitions = int(input())
left_sum = 0
right_sum = 0
for i in range(0, repetitions):
    cur_int = int(input())
    left_sum += cur_int

for i in range(0, repetitions):
    cur_int = int(input())
    right_sum += cur_int

if left_sum == right_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")