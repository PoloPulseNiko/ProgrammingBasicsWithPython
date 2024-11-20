day = input()
work = ""

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    work = "Working day"
elif day in ["Saturday", "Sunday"]:
    work = "Weekend"
else:
    work = "Error"

print(work)