destination = input()
while destination != "End":
    minimum_budget = float(input())
    saved_cash = 0
    while saved_cash < minimum_budget:
        money = float(input())
        saved_cash += money
    print(f"Going to {destination}!")
    saved_cash = 0
    destination = input()