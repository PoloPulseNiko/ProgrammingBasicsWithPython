money_added = 10.00
age = int(input())
machine_price = float(input())
toy_price = int(input())
toy_count = 0
total_money = 0.00
for i in range (1, age + 1):
    if i % 2 == 0:
        total_money += money_added - 1.00
        money_added += 10.00
    else:
        toy_count += 1

total_money += (toy_count * toy_price)
if total_money >= machine_price:
    print(f"Yes! {(abs(total_money - machine_price)):.2f}")
else:
    print(f"No! {(abs(total_money - machine_price)):.2f}")