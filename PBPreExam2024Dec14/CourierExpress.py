weight = float(input())
service_type = input()
distance = int(input())
price = 0

if weight < 1:
    price = 0.03 * distance
    if service_type == 'express':
        price += (0.03 * 0.8 * weight * distance)
elif 1 <= weight < 10:
    price = 0.05 * distance
    if service_type == 'express':
        price += (0.05 * 0.4 * weight * distance)
elif 10 <= weight < 40:
    price = 0.10 * distance
    if service_type == 'express':
        price += (0.10 * 0.05 * weight * distance)
elif 40 <= weight < 90:
    price = 0.15 * distance
    if service_type == 'express':
        price += (0.02 * 0.15 * weight * distance)
elif 90 <= weight < 150:
    price = 0.20 * distance
    if service_type == 'express':
        price += (0.20 * 0.01 * weight * distance)

print(f'The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.')