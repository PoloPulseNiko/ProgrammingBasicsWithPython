month = input()
nights = int(input())
studio_price = 0
apartment_price = 0
if month == "May" or month == "October":
    studio_price = 50.0 * nights
    apartment_price = 65.00 * nights
elif month == "June" or month == "September":
    studio_price = 75.20 * nights
    apartment_price = 68.70 * nights
elif month == "July" or month == "August":
    studio_price = 76.00 * nights
    apartment_price = 77.00 * nights

if (month == "May" or month == "October") and 7 < nights <= 14:
    studio_price *= 0.95
if nights > 14:
    apartment_price *= 0.9
    if month == "May" or month == "October":
        studio_price *= 0.7
    elif month == "June" or month == "September":
        studio_price *= 0.8

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
