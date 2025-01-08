steps_count = 0
while steps_count < 10000:
    command = input()
    if command == 'Going home':
        steps = int(input())
        steps_count += steps
        break
    steps_count += int(command)

if steps_count < 10000:
    print(f'{10000 - steps_count} more steps to reach goal.')
else:
    print('Goal reached! Good job!')
    print(f'{steps_count - 10000} steps over the goal!')