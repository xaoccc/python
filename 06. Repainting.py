nylon_price = 1.5
paint_price = 14.5
thinner_price = 5.0
bags = 0.4

nylon_q = int(input())
paint_q = int(input())
thinner_q = int(input())
work_hours = int(input())

mat_price = ((nylon_q + 2) * nylon_price) + ((paint_q * 1.1) * paint_price) + (thinner_price * thinner_q) + bags
work_price = (mat_price * 0.3) * work_hours
total_price = mat_price + work_price

print(total_price)
