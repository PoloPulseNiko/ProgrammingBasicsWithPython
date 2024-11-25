reps = int(input())
even_sum = 0
odd_sum = 0
for i in range(0, reps):
    num = int(input())
    if(i % 2 == 0):
        even_sum += num
    elif(i % 2 == 1):
        odd_sum += num

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {abs(even_sum - odd_sum)}")