import sys
repetitions = int(input())
min_value = sys.maxsize
max_value = -sys.maxsize - 1
for i in range(0, repetitions):
    current_line = int(input())
    if current_line < min_value:
        min_value = current_line
    if current_line > max_value:
        max_value = current_line

print(f"Max number: {max_value}")
print(f"Min number: {min_value}")