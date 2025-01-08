width = int(input())
length = int(input())
size = width * length

command = input()
while command != 'STOP':
    pieces = int(command)
    size -= pieces
    if size <= 0:
        print(f'No more cake left! You need {abs(size)} pieces more.')
        break
    command = input()

if size > 0:
    print(f'{size} pieces are left.')