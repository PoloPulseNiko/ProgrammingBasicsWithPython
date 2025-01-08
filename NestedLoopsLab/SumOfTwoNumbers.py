interval_start = int(input())
interval_end = int(input())
magic_number = int(input())
magic_num1 = 0
magic_num2 = 0
combinations = 0
found = False
for i in range(interval_start, interval_end + 1):
    for j in range(interval_start, interval_end + 1):
        combinations += 1
        if(i + j == magic_number):
            found = True
            magic_num1 = i
            magic_num2 = j
            break
    if found:
        break

if found:
    print(f"Combination N:{combinations} ({magic_num1} + {magic_num2} = {magic_number})")
else:
    print(f"{combinations} combinations - neither equals {magic_number}")