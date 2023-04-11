customer = input()
queue = []
while customer != "End":
    
    if customer == "Paid":
        print(*queue, sep="\n")
        queue = []
    else:
        queue.append(customer)
    customer = input()

print(f"{len(queue)} people remaining.")


# from collections import deque
# queue = deque()
# while True:
#     customer = input()
#     if customer == "Paid":
#         while len(queue):
#             print(queue.popleft())
#     elif customer == "End":
#         print(f"{len(queue)} people remaining.")
#         break
#     else:
#         queue.append(customer)
