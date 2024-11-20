days = int(input())
room_type = input()
rating = input()
price = 0
if room_type == "room for one person":
    price = (days - 1) * 18.00
elif room_type == "apartment":
    price = (days - 1) * 25.00
    if days < 10:
        price *= 0.7
    elif 10 <= days <= 15:
        price *= 0.65
    elif days > 15:
        price *= 0.5
elif room_type == "president apartment":
    price = (days - 1) * 35.00
    if days < 10:
        price *= 0.9
    elif 10 <= days <= 15:
        price *= 0.85
    elif days > 15:
        price *= 0.8

if rating == "positive":
    price *= 1.25
elif rating == "negative":
    price *= 0.9

print(f"{price:.2f}")