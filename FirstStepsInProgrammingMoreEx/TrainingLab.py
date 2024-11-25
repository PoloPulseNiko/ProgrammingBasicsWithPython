length = float(input()) * 100
width = float(input()) * 100

corridor_width = 100
usable_width = width - corridor_width
desks_per_row = usable_width // 70
rows = length // 120
total_seats = desks_per_row * rows
final_seats = total_seats - 3
print(int(final_seats))
