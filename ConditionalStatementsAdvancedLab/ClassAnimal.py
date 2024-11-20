animal = input()
type = ""
if animal == "dog":
    type = "mammal"
elif animal in ["crocodile", "tortoise", "snake"]:
    type = "reptile"
else:
    type = "unknown"

print(type)