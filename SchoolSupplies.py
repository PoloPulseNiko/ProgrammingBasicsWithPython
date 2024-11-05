pen_packs = int(input())
marker_packs = int(input())
cleaning_agent = int(input())
discount_percentage = int(input())
pen_price = pen_packs * 5.80
marker_price = marker_packs * 7.20
cleaner_price = cleaning_agent * 1.20
discountdec = discount_percentage / 100
final_price = (pen_price + marker_price + cleaner_price) * (1 - discountdec)
print(final_price)