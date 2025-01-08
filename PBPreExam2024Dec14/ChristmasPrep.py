paper_amount = int(input())
textile_amount = int(input())
glue_amount = float(input())
discount_percent = int(input())
paper_price = paper_amount * 5.80
textile_price = textile_amount * 7.20
glue_price = glue_amount * 1.20
discount = 1 - (discount_percent / 100)
total_price = (paper_price + textile_price + glue_price) * discount
print(f'{total_price:.3f}')