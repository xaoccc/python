pen_price = 5.8
marker_price = 7.2
chem_price = 1.2

pens = int(input()) * pen_price
markers = int(input()) * marker_price
chem = int(input()) * chem_price
discount = float(input()) / 100
discount_sum = (pens + markers + chem) * discount
total_price = pens + markers + chem - discount_sum

print(total_price)
