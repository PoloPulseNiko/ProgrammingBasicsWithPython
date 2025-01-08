k = int(input())
l = int(input())
m = int(input())
n = int(input())

switch_count = 0
stop_flag = False

for first1 in range(k, 9):
    for second1 in range(9, l - 1, -1):
        for first2 in range(m, 9):
            for second2 in range(9, n - 1, -1):
                if first1 % 2 == 0 and second1 % 2 != 0:
                    if first2 % 2 == 0 and second2 % 2 != 0:
                        if first1 != first2 or second1 != second2:
                            print(f"{first1}{second1} - {first2}{second2}")
                            switch_count += 1
                            if switch_count >= 6:
                                stop_flag = True
                                break
                        else:
                            print("Cannot change the same player.")
            if stop_flag: break
        if stop_flag: break
    if stop_flag: break
