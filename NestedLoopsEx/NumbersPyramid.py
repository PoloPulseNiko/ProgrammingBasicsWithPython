number = int(input())
current = 1
is_bigger_than_num = False
for i in range(1, number + 1):
    for j in range(1, i + 1):
        if current > number:
            is_bigger_than_num = True
            break
        print(str(current) + ' ', end = '')
        current += 1
    if is_bigger_than_num:
        break
    print()