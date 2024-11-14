budget = float(input())
graphics_cards = int(input())
processors = int(input())
memory = int(input())
video_price = 250.00 * graphics_cards
processor_price = 0.35 * video_price * processors
memory_price = memory * 0.10 * video_price
total_price = video_price + processor_price + memory_price
if graphics_cards > processors: total_price *= 0.85
if budget >= total_price:
    print(f'You have {(budget - total_price):.2f} leva left!')
else:
    print(f'Not enough money! You need {(total_price - budget):.2f} leva more!')
