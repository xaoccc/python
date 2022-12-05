orders_num = int(input())
total_price = 0
for i in range(orders_num):
  capsule_price = float(input())
  days = int(input())
  capsules_day = int(input())
  if capsule_price < 0.01 or capsule_price > 100 or days < 1 or days > 31 or capsules_day < 1 or capsules_day > 2000:
    continue

  coffee_price = capsule_price * capsules_day * days
  print(f"The price for the coffee is: ${coffee_price:.2f}")
  total_price += coffee_price
print(f"Total: ${total_price:.2f}")
