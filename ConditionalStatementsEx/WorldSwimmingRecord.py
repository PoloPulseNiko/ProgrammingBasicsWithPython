import math

record_seconds = float(input())
distance = float(input())
speed = float(input())
swimm_time1 = distance * speed
resistance_time_each_15m = (math.floor(distance / 15)) * 12.5
total_time = swimm_time1 + resistance_time_each_15m

if total_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    needed_seconds = total_time - record_seconds
    print(f"No, he failed! He was {needed_seconds:.2f} seconds slower.")