excursion_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
trucks_count = int(input())
price = (puzzle_count * 2.60) + (doll_count * 3.00) + (bear_count * 4.10) + (minion_count * 8.20) + (trucks_count * 2.00)
if (puzzle_count + doll_count + bear_count + minion_count + trucks_count) >= 50: price *= 0.75
price *= 0.9
if(price >= excursion_price): print(f'Yes! {(price - excursion_price):.2f} lv left.')
else: print(f'Not enough money! {(excursion_price - price):.2f} lv needed.')
