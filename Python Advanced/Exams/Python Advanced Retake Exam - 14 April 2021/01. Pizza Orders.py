from collections import deque
# orders == number of pizzas in the order 
orders, employees = deque([int(i) for i in input().split(", ")]), deque([int(i) for i in input().split(", ")])
pizzas_made = 0

while orders and employees:
    current_order, current_employee = orders.popleft(), employees.pop()
    if current_order > 10 or current_order <= 0:
        employees.append(current_employee)
        continue
    if current_order <= current_employee:
        pizzas_made += current_order
    else:
        orders.appendleft(current_order - current_employee)
        if employees:
            pizzas_made += current_employee      

if not orders:
    print(f"All orders are successfully completed!\nTotal pizzas made: {pizzas_made}\nEmployees: {', '.join([str(i) for i in employees])}")
else:
    print(f"Not all orders are completed.\nOrders left: {', '.join([str(i) for i in orders])}")
