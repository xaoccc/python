from collections import deque
ramen, customers = deque([int(i) for i in input().split(", ")]), deque([int(i) for i in input().split(", ")])

while ramen and customers:
    current_ramen = ramen.pop()
    current_customer = customers.popleft()
    if current_ramen == current_customer:
        continue
    elif current_ramen > current_customer:
        ramen.append(current_ramen - current_customer)
    elif current_ramen < current_customer:
        customers.appendleft(current_customer - current_ramen)
        
if not customers:
    print("Great job! You served all the customers.")
    if ramen:
        print(f"Bowls of ramen left: {', '.join([str(i) for i in ramen])}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(i) for i in customers])}")
