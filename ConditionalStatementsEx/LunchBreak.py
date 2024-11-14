import math
show_name = input()
episode_length = int(input())
break_length = int(input())
break_length -= (break_length * 0.375)
if(episode_length <= break_length):
    print(f'You have enough time to watch {show_name} and left with {math.ceil(break_length - episode_length)} minutes free time.')
else:
    print(f"You don't have enough time to watch {show_name}, you need {math.ceil(episode_length - break_length)} more minutes.")


#I'm Batman