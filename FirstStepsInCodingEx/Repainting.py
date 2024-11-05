nylon = (int(input()) + 2) * 1.50
paint = int(input()) * 1.1 * 14.50
thinner = int(input()) * 5.00
hours = int(input())
material_price = nylon + paint + thinner + 0.40
print(f'{(material_price + (material_price * 0.3 * hours)):.2f}')