budget = float(input())
season = input()
location = ""
price = 0
accommodation = ""
if budget <= 100:
    location = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        price = 0.3 * budget
    elif season == "winter":
        accommodation = "Hotel"
        price = 0.7 * budget
elif 100 < budget <= 1000:
    location = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        price = 0.4 * budget
    elif season == "winter":
        accommodation = "Hotel"
        price = 0.8 * budget
else:
    location = "Europe"
    accommodation = "Hotel"
    price = 0.9 * budget

print(f"Somewhere in {location}")
print(f"{accommodation} - {price:.2f}")