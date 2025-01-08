vacation_price = float(input())
current_budget = float(input())
days_count = 0
spending_count = 0
while current_budget < vacation_price and spending_count < 5:
    command = input()
    money = float(input())
    days_count += 1
    if command == 'save':
        current_budget += money
        spending_count = 0
    elif command == 'spend':
        current_budget -= money
        spending_count += 1
        if current_budget < 0:
            current_budget = 0

if spending_count == 5:
    print('You can\'t save the money.')
    print(days_count)

if current_budget >= vacation_price:
    print(f'You saved the money for {days_count} days.')