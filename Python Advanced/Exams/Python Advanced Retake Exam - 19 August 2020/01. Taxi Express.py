from collections import deque
customers = deque([int(i) for i in input().split(", ")])
taxis = deque([int(i) for i in input().split(", ")])
total_time = 0

while customers and taxis:
    current_customer = customers.popleft()
    current_taxi = taxis.pop()
    if current_taxi >= current_customer:
        total_time += current_customer
    else:
        customers.appendleft(current_customer)

if not customers:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")
else:
    print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join([str(i) for i in customers])}")
