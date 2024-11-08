vegetable_price = float(input())
fruit_price = float(input())
vegetable_kilo = int(input())
fruit_kilo = int(input())
final_price = ((vegetable_price * vegetable_kilo) + (fruit_price * fruit_kilo)) / 1.94
print(f'{final_price:.2f}')