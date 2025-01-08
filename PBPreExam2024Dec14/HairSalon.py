daily_goal = int(input())
earned_money = 0
command = input()
while command != 'closed':
    if command == 'haircut':
        client_type = input()
        if client_type == 'mens':
            earned_money += 15
        elif client_type == 'ladies':
            earned_money += 20
        elif client_type == 'kids':
            earned_money += 10
    elif command == 'color':
        service_type = input()
        if service_type == 'touch up':
            earned_money += 20
        elif service_type == 'full color':
            earned_money += 30

    if earned_money >= daily_goal:
        break

    command = input()

if earned_money >= daily_goal:
    print('You have reached your target for the day!')
else:
    print(f'Target not reached! You need {daily_goal - earned_money}lv. more.')

print(f'Earned money: {earned_money}lv.')