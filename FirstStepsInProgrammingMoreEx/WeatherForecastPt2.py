temp = float(input())
weather = ""

if 5.00 <= temp <= 11.9:
    weather = "Cold"
elif 12.00 <= temp <= 14.9:
    weather = "Cool"
elif 15.00 <= temp <= 20.00:
    weather = "Mild"
elif 20.1 <= temp <= 25.9:
    weather = "Warm"
elif 26.00 <= temp <= 35.00:
    weather = "Hot"
else:
    weather = "unknown"

print(weather)