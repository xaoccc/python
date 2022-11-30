from math import ceil, floor
rocket_price = float(input())
rockets_num = int(input())
snickers_num = int(input())
snickers_price = rocket_price / 6
total_sum = (rocket_price * rockets_num + snickers_num * snickers_price) * 1.2
print(f"Price to be paid by Djokovic {floor(total_sum / 8)}")
print(f"Price to be paid by sponsors {ceil(total_sum * 7 / 8)}")
