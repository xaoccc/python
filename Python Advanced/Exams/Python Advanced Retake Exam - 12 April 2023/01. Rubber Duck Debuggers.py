from collections import deque
time_needed = deque([int(i) for i in input().split()])
tasks = deque([int(i) for i in input().split()])
products = {"Darth Vader Ducky": [0, 0, 60], "Thor Ducky": [0, 61, 120], "Big Blue Rubber Ducky": [0, 121, 180], "Small Yellow Rubber Ducky": [0, 181, 240]}

while tasks:
    current_time = time_needed.popleft()
    task = tasks.pop()
    current_task = current_time * task
    if current_task > 240:
        tasks.append(task - 2)
        time_needed.append(current_time)
    else:
        for product, product_data in products.items():
            if product_data[1] <= current_task <= product_data[2]:
                product_data[0] += 1

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for product, product_data in products.items():
    print(f"{product}: {product_data[0]}")
