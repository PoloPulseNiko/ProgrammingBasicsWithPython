import math

absence_days = int(input())
food_left = int(input())
deer1_daily = float(input())
deer2_daily = float(input())
deer3_daily = float(input())
total_food = (deer1_daily + deer2_daily + deer3_daily) * absence_days
if food_left >= total_food:
    print(f'{math.floor(food_left - total_food)} kilos of food left.')
else:
    print(f'{math.ceil(total_food - food_left)} more kilos of food are needed.')