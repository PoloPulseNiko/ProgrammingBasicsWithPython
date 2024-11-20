import math
start_hour = int(input())
start_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())
start_time = (start_hour * 60) + start_minute
arrival_time = (arrival_hour * 60) + (arrival_minute)
if start_time >= arrival_time:
    if start_time == arrival_time or start_time - arrival_time <= 30:
        print("On time")
    else:
        print("Early")
    if(arrival_time < start_time):
        if(start_time - arrival_time < 60):
            print(f"{start_time - arrival_time} minutes before the start")
        else:
            diff = start_time - arrival_time
            print(f"{math.floor(diff / 60)}:{(diff % 60):02} hours before the start")
else:
    print("Late")
    if (arrival_time - start_time < 60):
        print(f"{arrival_time - start_time} minutes after the start")
    else:
        diff = arrival_time - start_time
        print(f"{math.floor(diff / 60)}:{(diff % 60):02} hours after the start")