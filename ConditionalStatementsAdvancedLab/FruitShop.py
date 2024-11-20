fruit_type = input()
day = input()
amount = float(input())
price = 0
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if fruit_type == "banana":
        price = amount * 2.50
    elif fruit_type == "apple":
        price = amount * 1.20
    elif fruit_type == "orange":
        price = amount * 0.85
    elif fruit_type == "grapefruit":
        price = amount * 1.45
    elif fruit_type == "kiwi":
        price = amount * 2.70
    elif fruit_type == "pineapple":
        price = amount * 5.50
    elif fruit_type == "grapes":
        price = amount * 3.85
    else:
        price = "error"
elif day in ["Saturday", "Sunday"]:
    if fruit_type == "banana":
        price = amount * 2.70
    elif fruit_type == "apple":
        price = amount * 1.25
    elif fruit_type == "orange":
        price = amount * 0.90
    elif fruit_type == "grapefruit":
        price = amount * 1.60
    elif fruit_type == "kiwi":
        price = amount * 3.00
    elif fruit_type == "pineapple":
        price = amount * 5.60
    elif fruit_type == "grapes":
        price = amount * 4.20
    else:
        price = "error"
else:
    price = "error"

if price == "error":
    print(price)
else:
    print(f'{price:.2f}')