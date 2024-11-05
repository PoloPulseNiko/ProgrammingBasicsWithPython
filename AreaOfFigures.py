import math
shape = input()
if shape == 'square':
    a = float(input())
    result = a * a
elif shape == 'rectangle':
    a = float(input())
    b = float(input())
    result = a * b
elif shape == 'circle':
    a = float(input())
    result = a * a * math.pi
elif shape == 'triangle':
    a = float(input())
    b = float(input())
    result = a * b / 2

print(f"{result:.3f}")
