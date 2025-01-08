coins_count = 0
sum = float(input())

while(sum > 0.00):
    if sum >= 2.00:
        sum -= 2.00
    elif 1.00 <= sum < 2.00:
        sum -= 1.00
    elif 0.50 <= sum < 1.00:
        sum -= 0.50
    elif 0.20 <= sum < 0.50:
        sum -= 0.20
    elif 0.10 <= sum < 0.20:
        sum -= 0.10
    elif 0.05 <= sum < 0.10:
        sum -= 0.05
    elif 0.02 <= sum < 0.05:
        sum -= 0.02
    elif 0.01 <= sum < 0.02:
        sum -= 0.01
    sum = round(sum, 2)
    coins_count += 1

print(coins_count)