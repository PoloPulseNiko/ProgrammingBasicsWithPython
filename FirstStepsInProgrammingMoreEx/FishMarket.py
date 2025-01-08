mackerel_price = float(input())
sprat_price = float(input())

palamud_kg = float(input())
safrid_kg = float(input())
mussels_kg = int(input())

palamud_price = mackerel_price * 1.60
safrid_price = sprat_price * 1.80
mussels_price = 7.50

total_cost = (palamud_kg * palamud_price) + (safrid_kg * safrid_price) + (mussels_kg * mussels_price)
print(f"{total_cost:.2f}")
