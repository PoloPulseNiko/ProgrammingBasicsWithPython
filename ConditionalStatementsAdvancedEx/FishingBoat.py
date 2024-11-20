budget = int(input())
season = input()
amount = int(input())
price = 0
if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if amount <= 6:
    price *= 0.9
elif 7 <= amount <= 11:
    price *= 0.85
elif amount >= 12:
    price *= 0.75

if amount % 2 == 0 and season != "Autumn":
    price *= 0.95

if budget < price:
    print(f"Not enough money! You need {(price - budget):.2f} leva.")
else:
    print(f"Yes! You have {(budget - price):.2f} leva left.")