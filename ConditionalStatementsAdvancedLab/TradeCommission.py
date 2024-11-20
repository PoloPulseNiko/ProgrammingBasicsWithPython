city = input()
sales = float(input())
commission = 0
if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 0.05 * sales
    elif 500 < sales <= 1000:
        commission = 0.07 * sales
    elif 1000 <= sales <= 10000:
        commission = 0.08 * sales
    elif 10000 < sales:
        commission = 0.12 * sales
    else:
        commission = "error"
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = 0.045 * sales
    elif 500 < sales <= 1000:
        commission = 0.075 * sales
    elif 1000 <= sales <= 10000:
        commission = 0.1 * sales
    elif 10000 < sales:
        commission = 0.13 * sales
    else:
        commission = "error"
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 0.055 * sales
    elif 500 < sales <= 1000:
        commission = 0.08 * sales
    elif 1000 <= sales <= 10000:
        commission = 0.12 * sales
    elif 10000 < sales:
        commission = 0.145 * sales
    else:
        commission = "error"
else:
    commission = "error"

if commission == "error":
    print(commission)
else:
    print(f'{commission:.2f}')