film_budget = float(input())
static_count = int(input())
clothing_price = float(input())
film_budget *= 0.9
clothing_cost = static_count * clothing_price
if static_count > 150: clothing_cost *= 0.9
if film_budget >= clothing_cost:
    print('Action!')
    print(f'Wingard starts filming with {(film_budget - clothing_cost):.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {(clothing_cost - film_budget):.2f} leva more.')