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
