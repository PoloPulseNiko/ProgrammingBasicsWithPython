sum = 0.00
command = input()
while command != 'NoMoreMoney':
    number = float(command)
    if number < 0:
        print("Invalid operation!")
        break
    print(f'Increase: {number:.2f}')
    sum += number
    command = input()

print(f'Total: {sum:.2f}')