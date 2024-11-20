flower_type = input()
flower_amount = int(input())
budget = int(input())
price = 0.00
if flower_type == "Roses":
    price = flower_amount * 5.00
    if flower_amount > 80:
        price *= 0.9
elif flower_type == "Dahlias":
    price = flower_amount * 3.80
    if flower_amount > 90:
        price *= 0.85
elif flower_type == "Tulips":
    price = flower_amount * 2.80
    if flower_amount > 80:
        price *= 0.85
elif flower_type == "Narcissus":
    price = flower_amount * 3.00
    if flower_amount < 120:
        price *= 1.15
elif flower_type == "Gladiolus":
    price = flower_amount * 2.50
    if flower_amount < 80:
        price *= 1.20

if budget < price:
    print(f"Not enough money, you need {(price - budget):.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {flower_amount} {flower_type} and {(budget - price):.2f} leva left.")