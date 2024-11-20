fruit = input()
type = ""
if fruit in ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]:
    type = "fruit"
elif fruit in ["tomato", "cucumber", "pepper", "carrot"]:
    type = "vegetable"
else:
    type = "unknown"

print(type)