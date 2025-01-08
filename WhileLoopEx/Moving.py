width = int(input())
length = int(input())
height = int(input())
space = width * length * height
total_size = 0
command = input()
while command != 'Done':
    size = int(command)
    total_size += size
    if total_size >= space:
        print(f'No more free space! You need {total_size - space} Cubic meters more.')
        break
    command = input()

if total_size < space:
    print(f'{space - total_size} Cubic meters left.')