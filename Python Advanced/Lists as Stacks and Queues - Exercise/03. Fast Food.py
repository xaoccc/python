from collections import deque
food_total = int(input())
total_orders = deque(int(i) for i in input().split())
left = []
print(max(total_orders))
for order in total_orders:
    if order <= food_total:
        food_total -= order
    else:
        food_total = 0
        left.append(order)
if len(left) > 0:
    print(f"Orders left: {' '.join([str(i) for i in left])}")
else:
    print("Orders complete")
