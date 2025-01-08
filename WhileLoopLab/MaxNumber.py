import sys

max_num = -sys.maxsize
command = input()
while command != 'Stop':
    command = int(command)
    if command > max_num:
        max_num = command
    command = input()

print(max_num)